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


class ApplicationProxy(AbstractModel):
    """应用代理实例

    """

    def __init__(self):
        r"""
        :param ProxyId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyId: str
        :param ProxyName: 实例名称
        :type ProxyName: str
        :param PlatType: 调度模式：
ip表示Anycast IP
domain表示CNAME
        :type PlatType: str
        :param SecurityType: 0关闭安全，1开启安全
        :type SecurityType: int
        :param AccelerateType: 0关闭加速，1开启加速
        :type AccelerateType: int
        :param ForwardClientIp: 字段已经移至Rule.ForwardClientIp
        :type ForwardClientIp: str
        :param SessionPersist: 字段已经移至Rule.SessionPersist
        :type SessionPersist: bool
        :param Rule: 规则列表
        :type Rule: list of ApplicationProxyRule
        :param Status: 状态：
online：启用
offline：停用
progress：部署中
stopping：停用中
fail：部署失败/停用失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param ScheduleValue: 调度信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduleValue: list of str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param ZoneId: 站点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param ZoneName: 站点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneName: str
        :param SessionPersistTime: 会话保持时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionPersistTime: int
        :param ProxyType: 服务类型
hostname：子域名
instance：实例
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyType: str
        :param HostId: 七层实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type HostId: str
        """
        self.ProxyId = None
        self.ProxyName = None
        self.PlatType = None
        self.SecurityType = None
        self.AccelerateType = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.Rule = None
        self.Status = None
        self.ScheduleValue = None
        self.UpdateTime = None
        self.ZoneId = None
        self.ZoneName = None
        self.SessionPersistTime = None
        self.ProxyType = None
        self.HostId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        self.PlatType = params.get("PlatType")
        self.SecurityType = params.get("SecurityType")
        self.AccelerateType = params.get("AccelerateType")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        self.Status = params.get("Status")
        self.ScheduleValue = params.get("ScheduleValue")
        self.UpdateTime = params.get("UpdateTime")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
        self.HostId = params.get("HostId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationProxyRule(AbstractModel):
    """应用代理规则

    """

    def __init__(self):
        r"""
        :param Proto: 协议，取值为TCP或者UDP
        :type Proto: str
        :param Port: 端口，支持格式：
80：80端口
81-90：81至90端口
        :type Port: list of str
        :param OriginType: 源站类型，取值：
custom：手动添加
origins：源站组
load_balancing：负载均衡
        :type OriginType: str
        :param OriginValue: 源站信息：
当OriginType=custom时，表示多个：
IP:端口
域名:端口
当OriginType=origins时，包含一个元素，表示源站组ID
当OriginType=load_balancing时，包含一个元素，表示负载均衡ID
        :type OriginValue: list of str
        :param RuleId: 规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: str
        :param Status: 状态：
online：启用
offline：停用
progress：部署中
stopping：停用中
fail：部署失败/停用失败
        :type Status: str
        :param ForwardClientIp: 传递客户端IP，当Proto=TCP时，取值：
TOA：TOA
PPV1: Proxy Protocol传递，协议版本V1
PPV2: Proxy Protocol传递，协议版本V2
OFF：不传递
当Proto=UDP时，取值：
PPV2: Proxy Protocol传递，协议版本V2
OFF：不传递
        :type ForwardClientIp: str
        :param SessionPersist: 是否开启会话保持
        :type SessionPersist: bool
        """
        self.Proto = None
        self.Port = None
        self.OriginType = None
        self.OriginValue = None
        self.RuleId = None
        self.Status = None
        self.ForwardClientIp = None
        self.SessionPersist = None


    def _deserialize(self, params):
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.OriginType = params.get("OriginType")
        self.OriginValue = params.get("OriginValue")
        self.RuleId = params.get("RuleId")
        self.Status = params.get("Status")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfig(AbstractModel):
    """缓存规则配置。

    """

    def __init__(self):
        r"""
        :param Cache: 缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfigCache`
        :param NoCache: 不缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type NoCache: :class:`tencentcloud.teo.v20220106.models.CacheConfigNoCache`
        :param FollowOrigin: 遵循源站配置
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowOrigin: :class:`tencentcloud.teo.v20220106.models.CacheConfigFollowOrigin`
        """
        self.Cache = None
        self.NoCache = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self.Cache = CacheConfigCache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("NoCache") is not None:
            self.NoCache = CacheConfigNoCache()
            self.NoCache._deserialize(params.get("NoCache"))
        if params.get("FollowOrigin") is not None:
            self.FollowOrigin = CacheConfigFollowOrigin()
            self.FollowOrigin._deserialize(params.get("FollowOrigin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigCache(AbstractModel):
    """缓存时间设置

    """

    def __init__(self):
        r"""
        :param Switch: 缓存配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param CacheTime: 缓存过期时间设置
单位为秒，最大可设置为 365 天
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheTime: int
        :param IgnoreCacheControl: 是否开启强制缓存
开启：on
关闭：off
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreCacheControl: str
        """
        self.Switch = None
        self.CacheTime = None
        self.IgnoreCacheControl = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CacheTime = params.get("CacheTime")
        self.IgnoreCacheControl = params.get("IgnoreCacheControl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigFollowOrigin(AbstractModel):
    """缓存遵循源站配置

    """

    def __init__(self):
        r"""
        :param Switch: 遵循源站配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigNoCache(AbstractModel):
    """不缓存配置

    """

    def __init__(self):
        r"""
        :param Switch: 不缓存配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheKey(AbstractModel):
    """缓存键配置

    """

    def __init__(self):
        r"""
        :param FullUrlCache: 是否开启全路径缓存
on：开启全路径缓存（即关闭参数忽略）
off：关闭全路径缓存（即开启参数忽略）
注意：此字段可能返回 null，表示取不到有效值。
        :type FullUrlCache: str
        :param IgnoreCase: 是否忽略大小写缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreCase: str
        :param QueryString: CacheKey中包含请求参数
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryString: :class:`tencentcloud.teo.v20220106.models.QueryString`
        """
        self.FullUrlCache = None
        self.IgnoreCase = None
        self.QueryString = None


    def _deserialize(self, params):
        self.FullUrlCache = params.get("FullUrlCache")
        self.IgnoreCase = params.get("IgnoreCase")
        if params.get("QueryString") is not None:
            self.QueryString = QueryString()
            self.QueryString._deserialize(params.get("QueryString"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertFilter(AbstractModel):
    """证书查询过滤条件

    """

    def __init__(self):
        r"""
        :param Name: 过滤字段名，支持的列表如下:
 - host：域名。
 - certId: 证书ID
 - certAlias: 证书备用名
 - certType: default: 默认证书, upload: 上传证书, managed:腾讯云证书
        :type Name: str
        :param Values: 过滤字段值
        :type Values: list of str
        :param Fuzzy: 是否启用模糊查询，仅支持过滤字段名host。
模糊查询时，Value长度最大为1。
        :type Fuzzy: bool
        """
        self.Name = None
        self.Values = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertSort(AbstractModel):
    """查询结果排序条件。

    """

    def __init__(self):
        r"""
        :param Key: 排序字段，当前支持：
createTime，域名创建时间
certExpireTime，证书过期时间
certDeployTime,  证书部署时间
        :type Key: str
        :param Sequence: asc/desc，默认desc。
        :type Sequence: str
        """
        self.Key = None
        self.Sequence = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Sequence = params.get("Sequence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateRequest(AbstractModel):
    """CheckCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Certificate: 证书
        :type Certificate: str
        :param PrivateKey: 私钥
        :type PrivateKey: str
        """
        self.Certificate = None
        self.PrivateKey = None


    def _deserialize(self, params):
        self.Certificate = params.get("Certificate")
        self.PrivateKey = params.get("PrivateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateResponse(AbstractModel):
    """CheckCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ClientIp(AbstractModel):
    """客户端IP头部

    """

    def __init__(self):
        r"""
        :param Switch: 客户端IP头部配置开关
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param HeaderName: 回源客户端IP请求头名称
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderName: str
        """
        self.Switch = None
        self.HeaderName = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.HeaderName = params.get("HeaderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CnameStatus(AbstractModel):
    """CNAME 状态

    """

    def __init__(self):
        r"""
        :param Name: 记录名称
        :type Name: str
        :param Cname: CNAME 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        :param Status: 状态
生效：active
不生效：moved
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self.Name = None
        self.Cname = None
        self.Status = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Cname = params.get("Cname")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Compression(AbstractModel):
    """智能压缩配置

    """

    def __init__(self):
        r"""
        :param Switch: 智能压缩配置开关
on：开启
off：关闭
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyRequest(AbstractModel):
    """CreateApplicationProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ZoneName: 站点名称
        :type ZoneName: str
        :param ProxyName: 四层代理名称
        :type ProxyName: str
        :param PlatType: 调度模式：
ip表示Anycast IP
domain表示CNAME
        :type PlatType: str
        :param SecurityType: 0关闭安全，1开启安全
        :type SecurityType: int
        :param AccelerateType: 0关闭加速，1开启加速
        :type AccelerateType: int
        :param ForwardClientIp: 字段已经移至Rule.ForwardClientIp
        :type ForwardClientIp: str
        :param SessionPersist: 字段已经移至Rule.SessionPersist
        :type SessionPersist: bool
        :param Rule: 规则详细信息
        :type Rule: list of ApplicationProxyRule
        :param SessionPersistTime: 会话保持时间，取值范围：30-3600，单位：秒
        :type SessionPersistTime: int
        :param ProxyType: 服务类型
hostname：子域名
instance：实例
        :type ProxyType: str
        """
        self.ZoneId = None
        self.ZoneName = None
        self.ProxyName = None
        self.PlatType = None
        self.SecurityType = None
        self.AccelerateType = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.Rule = None
        self.SessionPersistTime = None
        self.ProxyType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.ProxyName = params.get("ProxyName")
        self.PlatType = params.get("PlatType")
        self.SecurityType = params.get("SecurityType")
        self.AccelerateType = params.get("AccelerateType")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyResponse(AbstractModel):
    """CreateApplicationProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 新增的四层代理应用ID
        :type ProxyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProxyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.RequestId = params.get("RequestId")


class CreateApplicationProxyRuleRequest(AbstractModel):
    """CreateApplicationProxyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 代理ID
        :type ProxyId: str
        :param Proto: 协议，取值为TCP或者UDP
        :type Proto: str
        :param Port: 端口，支持格式：
80：80端口
81-90：81至90端口
        :type Port: list of str
        :param OriginType: 源站类型，取值：
custom：手动添加
origins：源站组
load_balancing：负载均衡
        :type OriginType: str
        :param OriginValue: 源站信息：
当OriginType=custom时，表示多个：
IP:端口
域名:端口
当OriginType=origins时，包含一个元素，表示源站组ID
当OriginType=load_balancing时，包含一个元素，表示负载均衡ID
        :type OriginValue: list of str
        :param ForwardClientIp: 传递客户端IP，当Proto=TCP时，取值：
TOA：TOA
PPV1: Proxy Protocol传递，协议版本V1
PPV2: Proxy Protocol传递，协议版本V2
OFF：不传递
当Proto=UDP时，取值：
PPV2: Proxy Protocol传递，协议版本V2
OFF：不传递
        :type ForwardClientIp: str
        :param SessionPersist: 是否开启会话保持
        :type SessionPersist: bool
        """
        self.ZoneId = None
        self.ProxyId = None
        self.Proto = None
        self.Port = None
        self.OriginType = None
        self.OriginValue = None
        self.ForwardClientIp = None
        self.SessionPersist = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.OriginType = params.get("OriginType")
        self.OriginValue = params.get("OriginValue")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyRuleResponse(AbstractModel):
    """CreateApplicationProxyRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 规则ID
        :type RuleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class CreateApplicationProxyRulesRequest(AbstractModel):
    """CreateApplicationProxyRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 代理ID
        :type ProxyId: str
        :param Rule: 规则列表
        :type Rule: list of ApplicationProxyRule
        """
        self.ZoneId = None
        self.ProxyId = None
        self.Rule = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyRulesResponse(AbstractModel):
    """CreateApplicationProxyRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 新增的规则ID数组
        :type RuleId: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class CreateDnsRecordRequest(AbstractModel):
    """CreateDnsRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID
        :type ZoneId: str
        :param Type: 记录类型
        :type Type: str
        :param Name: 记录名
        :type Name: str
        :param Content: 记录内容
        :type Content: str
        :param Mode: 代理模式，可选值：dns_only, cdn_only, secure_cdn
        :type Mode: str
        :param Ttl: 生存时间值
        :type Ttl: int
        :param Priority: 优先级
        :type Priority: int
        """
        self.ZoneId = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Mode = None
        self.Ttl = None
        self.Priority = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Mode = params.get("Mode")
        self.Ttl = params.get("Ttl")
        self.Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDnsRecordResponse(AbstractModel):
    """CreateDnsRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 记录 ID
        :type Id: str
        :param Type: 记录类型
        :type Type: str
        :param Name: 记录名称
        :type Name: str
        :param Content: 记录内容
        :type Content: str
        :param Ttl: 生存时间值
        :type Ttl: int
        :param Priority: 优先级
        :type Priority: int
        :param Mode: 代理模式
        :type Mode: str
        :param Status: 解析状态
active: 生效
pending: 不生效
        :type Status: str
        :param Locked: 已锁定
        :type Locked: bool
        :param CreatedOn: 创建时间
        :type CreatedOn: str
        :param ModifiedOn: 修改时间
        :type ModifiedOn: str
        :param ZoneId: 站点 ID
        :type ZoneId: str
        :param ZoneName: 站点名称
        :type ZoneName: str
        :param Cname: CNAME 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Ttl = None
        self.Priority = None
        self.Mode = None
        self.Status = None
        self.Locked = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.ZoneId = None
        self.ZoneName = None
        self.Cname = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Ttl = params.get("Ttl")
        self.Priority = params.get("Priority")
        self.Mode = params.get("Mode")
        self.Status = params.get("Status")
        self.Locked = params.get("Locked")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.Cname = params.get("Cname")
        self.RequestId = params.get("RequestId")


class CreateLoadBalancingRequest(AbstractModel):
    """CreateLoadBalancing请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param Host: 子域名，填写@表示根域
        :type Host: str
        :param Type: 代理模式：
dns_only: 仅DNS
proxied: 开启代理
        :type Type: str
        :param OriginId: 使用的源站组ID
        :type OriginId: list of str
        :param TTL: 当Type=dns_only表示DNS的TTL时间
        :type TTL: int
        """
        self.ZoneId = None
        self.Host = None
        self.Type = None
        self.OriginId = None
        self.TTL = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        self.Type = params.get("Type")
        self.OriginId = params.get("OriginId")
        self.TTL = params.get("TTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancingResponse(AbstractModel):
    """CreateLoadBalancing返回参数结构体

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.RequestId = params.get("RequestId")


class CreatePrefetchTaskRequest(AbstractModel):
    """CreatePrefetchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: Zone ID
        :type ZoneId: str
        :param Targets: 要预热的资源列表，每个元素格式类似如下:
http://www.example.com/example.txt
        :type Targets: list of str
        :param EncodeUrl: 是否对url进行encode
若内容含有非 ASCII 字符集的字符，请开启此开关，编码转换（编码规则遵循 RFC3986）
        :type EncodeUrl: bool
        :param Headers: 附带的http头部信息
        :type Headers: list of Header
        """
        self.ZoneId = None
        self.Targets = None
        self.EncodeUrl = None
        self.Headers = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Targets = params.get("Targets")
        self.EncodeUrl = params.get("EncodeUrl")
        if params.get("Headers") is not None:
            self.Headers = []
            for item in params.get("Headers"):
                obj = Header()
                obj._deserialize(item)
                self.Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrefetchTaskResponse(AbstractModel):
    """CreatePrefetchTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param FailedList: 失败的任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedList: list of FailReason
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.FailedList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self.FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self.FailedList.append(obj)
        self.RequestId = params.get("RequestId")


class CreatePurgeTaskRequest(AbstractModel):
    """CreatePurgeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: Zone ID
        :type ZoneId: str
        :param Type: 类型，当前支持的类型：
- purge_url：URL
- purge_prefix：前缀
- purge_host：Hostname
- purge_all：全部缓存
        :type Type: str
        :param Targets: 要刷新的资源列表，每个元素格式依据Type而定
1) Type = purge_host 时
形如：www.example.com 或 foo.bar.example.com
2) Type = purge_prefix 时
形如：http://www.example.com/example
3) Type = purge_url 时
形如：https://www.example.com/example.jpg
4）Type = purge_all 时
Targets可为空，不需要填写
        :type Targets: list of str
        :param EncodeUrl: 若有编码转换，仅清除编码转换后匹配的资源
若内容含有非 ASCII 字符集的字符，请开启此开关，编码转换（编码规则遵循 RFC3986）
        :type EncodeUrl: bool
        """
        self.ZoneId = None
        self.Type = None
        self.Targets = None
        self.EncodeUrl = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        self.Targets = params.get("Targets")
        self.EncodeUrl = params.get("EncodeUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePurgeTaskResponse(AbstractModel):
    """CreatePurgeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param FailedList: 失败的任务列表及原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedList: list of FailReason
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.FailedList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self.FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self.FailedList.append(obj)
        self.RequestId = params.get("RequestId")


class CreateZoneRequest(AbstractModel):
    """CreateZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 站点名字
        :type Name: str
        :param Type: 接入方式，默认full
- full NS接入
- partial CNAME接入
        :type Type: str
        :param JumpStart: 是否跳过站点历史解析记录扫描
        :type JumpStart: bool
        """
        self.Name = None
        self.Type = None
        self.JumpStart = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.JumpStart = params.get("JumpStart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateZoneResponse(AbstractModel):
    """CreateZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点ID
        :type Id: str
        :param Name: 站点名称
        :type Name: str
        :param Type: 站点接入方式
        :type Type: str
        :param Status: 站点状态
- pending 未切换NS
- active NS 已切换到分配的 NS
- moved NS 从腾讯云切走
        :type Status: str
        :param OriginalNameServers: 当前使用的 NS 列表
        :type OriginalNameServers: list of str
        :param NameServers: 给用户分配的 NS 列表
        :type NameServers: list of str
        :param CreatedOn: 站点创建时间
        :type CreatedOn: str
        :param ModifiedOn: 站点更新时间
        :type ModifiedOn: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Type = None
        self.Status = None
        self.OriginalNameServers = None
        self.NameServers = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.NameServers = params.get("NameServers")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class DataItem(AbstractModel):
    """统计曲线数据项

    """

    def __init__(self):
        r"""
        :param Time: 时间
        :type Time: str
        :param Value: 数值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: int
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DefaultServerCertInfo(AbstractModel):
    """https 服务端证书配置

    """

    def __init__(self):
        r"""
        :param CertId: 服务器证书 ID, 默认证书ID, 或在 SSL 证书管理进行证书托管时自动生成
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param Alias: 证书备注名
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Type: 证书类型:
default: 默认证书
upload:用户上传
managed:腾讯云托管
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param ExpireTime: 证书过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param EffectiveTime: 证书生效时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EffectiveTime: str
        :param CommonName: 证书公用名
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonName: str
        :param SubjectAltName: 证书SAN域名
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param Status: 证书状态:
applying: 证书申请中
failed: 证书(申请)失败
processing: 证书部署中
deployed: 证书已部署
disabled: 证书被禁用
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Message: Status为失败时,此字段返回失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self.CertId = None
        self.Alias = None
        self.Type = None
        self.ExpireTime = None
        self.EffectiveTime = None
        self.CommonName = None
        self.SubjectAltName = None
        self.Status = None
        self.Message = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.Alias = params.get("Alias")
        self.Type = params.get("Type")
        self.ExpireTime = params.get("ExpireTime")
        self.EffectiveTime = params.get("EffectiveTime")
        self.CommonName = params.get("CommonName")
        self.SubjectAltName = params.get("SubjectAltName")
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyRequest(AbstractModel):
    """DeleteApplicationProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 代理ID
        :type ProxyId: str
        """
        self.ZoneId = None
        self.ProxyId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyResponse(AbstractModel):
    """DeleteApplicationProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 代理ID
        :type ProxyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProxyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.RequestId = params.get("RequestId")


class DeleteApplicationProxyRuleRequest(AbstractModel):
    """DeleteApplicationProxyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 代理ID
        :type ProxyId: str
        :param RuleId: 规则ID
        :type RuleId: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.RuleId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyRuleResponse(AbstractModel):
    """DeleteApplicationProxyRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 规则ID
        :type RuleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class DeleteDnsRecordsRequest(AbstractModel):
    """DeleteDnsRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID
        :type ZoneId: str
        :param Ids: 记录 ID
        :type Ids: list of str
        """
        self.ZoneId = None
        self.Ids = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDnsRecordsResponse(AbstractModel):
    """DeleteDnsRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: 记录 ID
        :type Ids: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ids = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancingRequest(AbstractModel):
    """DeleteLoadBalancing请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        """
        self.ZoneId = None
        self.LoadBalancingId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LoadBalancingId = params.get("LoadBalancingId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancingResponse(AbstractModel):
    """DeleteLoadBalancing返回参数结构体

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.RequestId = params.get("RequestId")


class DeleteZoneRequest(AbstractModel):
    """DeleteZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
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
        


class DeleteZoneResponse(AbstractModel):
    """DeleteZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class DescribeApplicationProxyDetailRequest(AbstractModel):
    """DescribeApplicationProxyDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 实例ID
        :type ProxyId: str
        """
        self.ZoneId = None
        self.ProxyId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationProxyDetailResponse(AbstractModel):
    """DescribeApplicationProxyDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 实例ID
        :type ProxyId: str
        :param ProxyName: 实例名称
        :type ProxyName: str
        :param PlatType: 调度模式：
ip表示Anycast IP
domain表示CNAME
        :type PlatType: str
        :param SecurityType: 0关闭安全，1开启安全
        :type SecurityType: int
        :param AccelerateType: 0关闭加速，1开启加速
        :type AccelerateType: int
        :param ForwardClientIp: 字段已经移至Rule.ForwardClientIp
        :type ForwardClientIp: str
        :param SessionPersist: 字段已经移至Rule.SessionPersist
        :type SessionPersist: bool
        :param Rule: 规则列表
        :type Rule: list of ApplicationProxyRule
        :param Status: 状态：
online：启用
offline：停用
progress：部署中
        :type Status: str
        :param ScheduleValue: 调度信息
        :type ScheduleValue: list of str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ZoneName: 站点名称
        :type ZoneName: str
        :param SessionPersistTime: 会话保持时间
        :type SessionPersistTime: int
        :param ProxyType: 服务类型
hostname：子域名
instance：实例
        :type ProxyType: str
        :param HostId: 七层实例ID
        :type HostId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProxyId = None
        self.ProxyName = None
        self.PlatType = None
        self.SecurityType = None
        self.AccelerateType = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.Rule = None
        self.Status = None
        self.ScheduleValue = None
        self.UpdateTime = None
        self.ZoneId = None
        self.ZoneName = None
        self.SessionPersistTime = None
        self.ProxyType = None
        self.HostId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        self.PlatType = params.get("PlatType")
        self.SecurityType = params.get("SecurityType")
        self.AccelerateType = params.get("AccelerateType")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        self.Status = params.get("Status")
        self.ScheduleValue = params.get("ScheduleValue")
        self.UpdateTime = params.get("UpdateTime")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
        self.HostId = params.get("HostId")
        self.RequestId = params.get("RequestId")


class DescribeApplicationProxyRequest(AbstractModel):
    """DescribeApplicationProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param Offset: 分页参数Offset
        :type Offset: int
        :param Limit: 分页参数Limit
        :type Limit: int
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationProxyResponse(AbstractModel):
    """DescribeApplicationProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ApplicationProxy
        :param TotalCount: 记录总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Quota: 当ZoneId不为空时，表示当前站点允许创建的实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Quota: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.Quota = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ApplicationProxy()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.Quota = params.get("Quota")
        self.RequestId = params.get("RequestId")


class DescribeCnameStatusRequest(AbstractModel):
    """DescribeCnameStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID
        :type ZoneId: str
        :param Names: 域名列表
        :type Names: list of str
        """
        self.ZoneId = None
        self.Names = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCnameStatusResponse(AbstractModel):
    """DescribeCnameStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 状态列表
        :type Status: list of CnameStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Status") is not None:
            self.Status = []
            for item in params.get("Status"):
                obj = CnameStatus()
                obj._deserialize(item)
                self.Status.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDefaultCertificatesRequest(AbstractModel):
    """DescribeDefaultCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: Zone ID
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultCertificatesResponse(AbstractModel):
    """DescribeDefaultCertificates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 证书总数
        :type TotalCount: int
        :param CertInfo: 默认证书列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CertInfo: list of DefaultServerCertInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.CertInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CertInfo") is not None:
            self.CertInfo = []
            for item in params.get("CertInfo"):
                obj = DefaultServerCertInfo()
                obj._deserialize(item)
                self.CertInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDnsDataRequest(AbstractModel):
    """DescribeDnsData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Filters: 过滤参数
        :type Filters: list of DnsDataFilter
        :param Interval: 时间粒度，默认为1分钟粒度，服务端根据时间范围自适应。
支持指定以下几种粒度：
min：1分钟粒度
5min：5分钟粒度
hour：1小时粒度
day：天粒度
        :type Interval: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Filters = None
        self.Interval = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = DnsDataFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDnsDataResponse(AbstractModel):
    """DescribeDnsData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 统计曲线数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DataItem
        :param Interval: 时间粒度
注意：此字段可能返回 null，表示取不到有效值。
        :type Interval: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Interval = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Interval = params.get("Interval")
        self.RequestId = params.get("RequestId")


class DescribeDnsRecordsRequest(AbstractModel):
    """DescribeDnsRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 查询条件过滤器
        :type Filters: list of DnsRecordFilter
        :param Order: 排序
        :type Order: str
        :param Direction: 可选值 asc, desc
        :type Direction: str
        :param Match: 可选值 all, any
        :type Match: str
        :param Limit: 分页查询限制数目，默认为 100，最大可设置为 1000
        :type Limit: int
        :param Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param ZoneId: 站点 ID
        :type ZoneId: str
        """
        self.Filters = None
        self.Order = None
        self.Direction = None
        self.Match = None
        self.Limit = None
        self.Offset = None
        self.ZoneId = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = DnsRecordFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.Direction = params.get("Direction")
        self.Match = params.get("Match")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDnsRecordsResponse(AbstractModel):
    """DescribeDnsRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数，用于分页查询
        :type TotalCount: int
        :param Records: DNS 记录列表
        :type Records: list of DnsRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Records = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = DnsRecord()
                obj._deserialize(item)
                self.Records.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDnssecRequest(AbstractModel):
    """DescribeDnssec请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
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
        


class DescribeDnssecResponse(AbstractModel):
    """DescribeDnssec返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Name: 站点名称
        :type Name: str
        :param Status: DNSSEC 状态
- enabled 开启
- disabled 关闭
        :type Status: str
        :param Dnssec: DNSSEC 相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Dnssec: :class:`tencentcloud.teo.v20220106.models.DnssecInfo`
        :param ModifiedOn: 修改时间
        :type ModifiedOn: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Status = None
        self.Dnssec = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        if params.get("Dnssec") is not None:
            self.Dnssec = DnssecInfo()
            self.Dnssec._deserialize(params.get("Dnssec"))
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class DescribeHostsCertificateRequest(AbstractModel):
    """DescribeHostsCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: Zone ID
        :type ZoneId: str
        :param Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param Limit: 分页查询限制数目，默认为 100，最大可设置为 1000
        :type Limit: int
        :param Filters: 查询条件过滤器
        :type Filters: list of CertFilter
        :param Sort: 排序方式
        :type Sort: :class:`tencentcloud.teo.v20220106.models.CertSort`
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.Sort = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = CertFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("Sort") is not None:
            self.Sort = CertSort()
            self.Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostsCertificateResponse(AbstractModel):
    """DescribeHostsCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数，用于分页查询
        :type TotalCount: int
        :param Hosts: 域名证书配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Hosts: list of HostCertSetting
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Hosts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Hosts") is not None:
            self.Hosts = []
            for item in params.get("Hosts"):
                obj = HostCertSetting()
                obj._deserialize(item)
                self.Hosts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHostsSettingRequest(AbstractModel):
    """DescribeHostsSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param Limit: 分页查询限制数目，默认为 100，最大可设置为 1000
        :type Limit: int
        :param Hosts: 指定域名查询
        :type Hosts: list of str
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.Hosts = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Hosts = params.get("Hosts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostsSettingResponse(AbstractModel):
    """DescribeHostsSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param Hosts: 域名列表
        :type Hosts: list of DetailHost
        :param TotalNumber: 域名数量
        :type TotalNumber: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Hosts = None
        self.TotalNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Hosts") is not None:
            self.Hosts = []
            for item in params.get("Hosts"):
                obj = DetailHost()
                obj._deserialize(item)
                self.Hosts.append(obj)
        self.TotalNumber = params.get("TotalNumber")
        self.RequestId = params.get("RequestId")


class DescribeIdentificationRequest(AbstractModel):
    """DescribeIdentification请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 站点名称
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
        


class DescribeIdentificationResponse(AbstractModel):
    """DescribeIdentification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 站点名称
        :type Name: str
        :param Status: 验证状态
- pending 验证中
- finished 验证完成
        :type Status: str
        :param Subdomain: 子域
        :type Subdomain: str
        :param RecordType: 记录类型
        :type RecordType: str
        :param RecordValue: 记录值
        :type RecordValue: str
        :param OriginalNameServers: 域名当前的 NS 记录
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalNameServers: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Status = None
        self.Subdomain = None
        self.RecordType = None
        self.RecordValue = None
        self.OriginalNameServers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.Subdomain = params.get("Subdomain")
        self.RecordType = params.get("RecordType")
        self.RecordValue = params.get("RecordValue")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancingDetailRequest(AbstractModel):
    """DescribeLoadBalancingDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        """
        self.ZoneId = None
        self.LoadBalancingId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LoadBalancingId = params.get("LoadBalancingId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancingDetailResponse(AbstractModel):
    """DescribeLoadBalancingDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param Host: 子域名，填写@表示根域
        :type Host: str
        :param Type: 代理模式：
dns_only: 仅DNS
proxied: 开启代理
        :type Type: str
        :param TTL: 当Type=dns_only表示DNS的TTL时间
        :type TTL: int
        :param OriginId: 使用的源站组ID
        :type OriginId: list of str
        :param Origin: 使用的源站信息
        :type Origin: list of OriginGroup
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Status: 状态
        :type Status: str
        :param Cname: 调度域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.ZoneId = None
        self.Host = None
        self.Type = None
        self.TTL = None
        self.OriginId = None
        self.Origin = None
        self.UpdateTime = None
        self.Status = None
        self.Cname = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        self.Type = params.get("Type")
        self.TTL = params.get("TTL")
        self.OriginId = params.get("OriginId")
        if params.get("Origin") is not None:
            self.Origin = []
            for item in params.get("Origin"):
                obj = OriginGroup()
                obj._deserialize(item)
                self.Origin.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        self.Cname = params.get("Cname")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancingRequest(AbstractModel):
    """DescribeLoadBalancing请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param Offset: 分页参数Offset
        :type Offset: int
        :param Limit: 分页参数Limit
        :type Limit: int
        :param Host: 过滤参数Host
        :type Host: str
        :param Fuzzy: 过滤参数Host是否支持模糊匹配
        :type Fuzzy: bool
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.Host = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Host = params.get("Host")
        self.Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancingResponse(AbstractModel):
    """DescribeLoadBalancing返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param Data: 负载均衡信息
        :type Data: list of LoadBalancing
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = LoadBalancing()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrefetchTasksRequest(AbstractModel):
    """DescribePrefetchTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param StartTime: 查询起始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        :param Offset: 查询起始偏移量
        :type Offset: int
        :param Limit: 查询最大返回的结果条数
        :type Limit: int
        :param Statuses: 查询的状态
允许的值为：processing、success、failed、timeout、invalid
        :type Statuses: list of str
        :param ZoneId: zone id
        :type ZoneId: str
        :param Domains: 查询的域名列表
        :type Domains: list of str
        :param Target: 查询的资源
        :type Target: str
        """
        self.JobId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Statuses = None
        self.ZoneId = None
        self.Domains = None
        self.Target = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Statuses = params.get("Statuses")
        self.ZoneId = params.get("ZoneId")
        self.Domains = params.get("Domains")
        self.Target = params.get("Target")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrefetchTasksResponse(AbstractModel):
    """DescribePrefetchTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 该查询条件总共条目数
        :type TotalCount: int
        :param Tasks: 任务结果列表
        :type Tasks: list of Task
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
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param Type: 类型
        :type Type: str
        :param StartTime: 查询起始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        :param Offset: 查询起始偏移量
        :type Offset: int
        :param Limit: 查询最大返回的结果条数
        :type Limit: int
        :param Statuses: 查询的状态
允许的值为：processing、success、failed、timeout、invalid
        :type Statuses: list of str
        :param ZoneId: zone id
        :type ZoneId: str
        :param Domains: 查询的域名列表
        :type Domains: list of str
        :param Target: 查询内容
        :type Target: str
        """
        self.JobId = None
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Statuses = None
        self.ZoneId = None
        self.Domains = None
        self.Target = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Statuses = params.get("Statuses")
        self.ZoneId = params.get("ZoneId")
        self.Domains = params.get("Domains")
        self.Target = params.get("Target")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 该查询条件总共条目数
        :type TotalCount: int
        :param Tasks: 任务结果列表
        :type Tasks: list of Task
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
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneDetailsRequest(AbstractModel):
    """DescribeZoneDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
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
        


class DescribeZoneDetailsResponse(AbstractModel):
    """DescribeZoneDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Name: 站点名称
        :type Name: str
        :param OriginalNameServers: 用户当前使用的 NS 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalNameServers: list of str
        :param NameServers: 腾讯云分配给用户的 NS 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NameServers: list of str
        :param Status: 站点状态
- active：NS 已切换
- pending：NS 未切换
- moved：NS 已切走
- deactivated：被封禁
        :type Status: str
        :param Type: 站点接入方式
- full：NS 接入
- partial：CNAME 接入
        :type Type: str
        :param Paused: 站点是否关闭
        :type Paused: bool
        :param CreatedOn: 站点创建时间
        :type CreatedOn: str
        :param ModifiedOn: 站点修改时间
        :type ModifiedOn: str
        :param VanityNameServers: 用户自定义 NS 信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VanityNameServers: :class:`tencentcloud.teo.v20220106.models.VanityNameServers`
        :param VanityNameServersIps: 用户自定义 NS IP 信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VanityNameServersIps: list of VanityNameServersIps
        :param CnameSpeedUp: 是否开启 CNAME 加速
- enabled：开启
- disabled：关闭
        :type CnameSpeedUp: str
        :param CnameStatus: cname切换验证状态
- finished 切换完成
- pending 切换验证中
注意：此字段可能返回 null，表示取不到有效值。
        :type CnameStatus: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.OriginalNameServers = None
        self.NameServers = None
        self.Status = None
        self.Type = None
        self.Paused = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.VanityNameServers = None
        self.VanityNameServersIps = None
        self.CnameSpeedUp = None
        self.CnameStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.NameServers = params.get("NameServers")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Paused = params.get("Paused")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        if params.get("VanityNameServers") is not None:
            self.VanityNameServers = VanityNameServers()
            self.VanityNameServers._deserialize(params.get("VanityNameServers"))
        if params.get("VanityNameServersIps") is not None:
            self.VanityNameServersIps = []
            for item in params.get("VanityNameServersIps"):
                obj = VanityNameServersIps()
                obj._deserialize(item)
                self.VanityNameServersIps.append(obj)
        self.CnameSpeedUp = params.get("CnameSpeedUp")
        self.CnameStatus = params.get("CnameStatus")
        self.RequestId = params.get("RequestId")


class DescribeZoneSettingRequest(AbstractModel):
    """DescribeZoneSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneSettingResponse(AbstractModel):
    """DescribeZoneSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param Cache: 缓存过期时间配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfig`
        :param CacheKey: 节点缓存键配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`tencentcloud.teo.v20220106.models.CacheKey`
        :param MaxAge: 浏览器缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: :class:`tencentcloud.teo.v20220106.models.MaxAge`
        :param OfflineCache: 离线缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineCache: :class:`tencentcloud.teo.v20220106.models.OfflineCache`
        :param Quic: Quic访问
注意：此字段可能返回 null，表示取不到有效值。
        :type Quic: :class:`tencentcloud.teo.v20220106.models.Quic`
        :param PostMaxSize: POST请求传输配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PostMaxSize: :class:`tencentcloud.teo.v20220106.models.PostMaxSize`
        :param Compression: 智能压缩配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Compression: :class:`tencentcloud.teo.v20220106.models.Compression`
        :param UpstreamHttp2: http2回源配置
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220106.models.UpstreamHttp2`
        :param ForceRedirect: 访问协议强制https跳转配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`tencentcloud.teo.v20220106.models.ForceRedirect`
        :param Https: Https 加速配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Https: :class:`tencentcloud.teo.v20220106.models.Https`
        :param Origin: 源站配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: :class:`tencentcloud.teo.v20220106.models.Origin`
        :param SmartRouting: 动态加速配置
注意：此字段可能返回 null，表示取不到有效值。
        :type SmartRouting: :class:`tencentcloud.teo.v20220106.models.SmartRouting`
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param Zone: 站点域名
        :type Zone: str
        :param WebSocket: WebSocket配置
注意：此字段可能返回 null，表示取不到有效值。
        :type WebSocket: :class:`tencentcloud.teo.v20220106.models.WebSocket`
        :param ClientIpHeader: 客户端IP回源请求头配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220106.models.ClientIp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Cache = None
        self.CacheKey = None
        self.MaxAge = None
        self.OfflineCache = None
        self.Quic = None
        self.PostMaxSize = None
        self.Compression = None
        self.UpstreamHttp2 = None
        self.ForceRedirect = None
        self.Https = None
        self.Origin = None
        self.SmartRouting = None
        self.ZoneId = None
        self.Zone = None
        self.WebSocket = None
        self.ClientIpHeader = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self.Cache = CacheConfig()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("OfflineCache") is not None:
            self.OfflineCache = OfflineCache()
            self.OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("Quic") is not None:
            self.Quic = Quic()
            self.Quic._deserialize(params.get("Quic"))
        if params.get("PostMaxSize") is not None:
            self.PostMaxSize = PostMaxSize()
            self.PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("UpstreamHttp2") is not None:
            self.UpstreamHttp2 = UpstreamHttp2()
            self.UpstreamHttp2._deserialize(params.get("UpstreamHttp2"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("SmartRouting") is not None:
            self.SmartRouting = SmartRouting()
            self.SmartRouting._deserialize(params.get("SmartRouting"))
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        if params.get("ClientIpHeader") is not None:
            self.ClientIpHeader = ClientIp()
            self.ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页参数，页偏移
        :type Offset: int
        :param Limit: 分页参数，每页返回的站点个数
        :type Limit: int
        :param Filters: 查询条件过滤器，复杂类型
        :type Filters: list of ZoneFilter
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
                obj = ZoneFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的站点数
        :type TotalCount: int
        :param Zones: 站点详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Zones: list of Zone
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Zones = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Zones") is not None:
            self.Zones = []
            for item in params.get("Zones"):
                obj = Zone()
                obj._deserialize(item)
                self.Zones.append(obj)
        self.RequestId = params.get("RequestId")


class DetailHost(AbstractModel):
    """域名配置信息

    """

    def __init__(self):
        r"""
        :param AppId: 腾讯云账号ID
        :type AppId: int
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param Status: 加速服务状态
process：部署中
online：已启动
offline：已关闭
        :type Status: str
        :param Host: 域名
        :type Host: str
        """
        self.AppId = None
        self.ZoneId = None
        self.Status = None
        self.Host = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.ZoneId = params.get("ZoneId")
        self.Status = params.get("Status")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsDataFilter(AbstractModel):
    """Dns数据曲线过滤参数

    """

    def __init__(self):
        r"""
        :param Name: 参数名称，取值范围：
zone：站点名
host：域名
type：dns解析类型
code：dns返回状态码
area：解析服务器所在区域
        :type Name: str
        :param Value: 参数值
当Name=area时，Value取值范围：
亚洲：Asia
欧洲：Europe
非洲：Africa
大洋洲：Oceania
美洲：Americas

当Name=code时，Value取值范围：
NoError：成功的响应
NXDomain：只在权威域名服务器的响应消息中有效，标示请求中请求的域不存在
NotImp：域名服务器不支持请求的类型
Refused：域名服务器因为策略的原因拒绝执行请求的操作
        :type Value: str
        :param Values: 参数值
当Name=area时，Value取值范围：
亚洲：Asia
欧洲：Europe
非洲：Africa
大洋洲：Oceania
美洲：Americas

当Name=code时，Value取值范围：
NoError：成功的响应
NXDomain：只在权威域名服务器的响应消息中有效，标示请求中请求的域不存在
NotImp：域名服务器不支持请求的类型
Refused：域名服务器因为策略的原因拒绝执行请求的操作
        :type Values: list of str
        """
        self.Name = None
        self.Value = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsRecord(AbstractModel):
    """DNS 记录

    """

    def __init__(self):
        r"""
        :param Id: 记录 ID
        :type Id: str
        :param Type: 记录类型
        :type Type: str
        :param Name: 主机记录
        :type Name: str
        :param Content: 记录值
        :type Content: str
        :param Mode: 代理模式
        :type Mode: str
        :param Ttl: TTL 值
        :type Ttl: int
        :param Priority: 优先级
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        :param CreatedOn: 创建时间
        :type CreatedOn: str
        :param ModifiedOn: 修改时间
        :type ModifiedOn: str
        :param Locked: 域名锁
        :type Locked: bool
        :param ZoneId: 站点 ID
        :type ZoneId: str
        :param ZoneName: 站点名称
        :type ZoneName: str
        :param Status: 解析状态
active: 生效
pending: 不生效
        :type Status: str
        :param Cname: CNAME 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        :param DomainStatus: 域名是否开启了lb，四层，安全
- lb 负载均衡
- security 安全
- l4 四层
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainStatus: list of str
        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Mode = None
        self.Ttl = None
        self.Priority = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.Locked = None
        self.ZoneId = None
        self.ZoneName = None
        self.Status = None
        self.Cname = None
        self.DomainStatus = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Mode = params.get("Mode")
        self.Ttl = params.get("Ttl")
        self.Priority = params.get("Priority")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.Locked = params.get("Locked")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.Status = params.get("Status")
        self.Cname = params.get("Cname")
        self.DomainStatus = params.get("DomainStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsRecordFilter(AbstractModel):
    """DNS 记录查询过滤条件

    """

    def __init__(self):
        r"""
        :param Name: 过滤字段名，支持的列表如下：
- name: 站点名。
- status: 站点状态
        :type Name: str
        :param Values: 过滤字段值
        :type Values: list of str
        :param Fuzzy: 是否启用模糊查询，仅支持过滤字段名为name。模糊查询时，Values长度最大为1
        :type Fuzzy: bool
        """
        self.Name = None
        self.Values = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnssecInfo(AbstractModel):
    """DNSSEC 相关信息

    """

    def __init__(self):
        r"""
        :param Flags: 标志
        :type Flags: int
        :param Algorithm: 加密算法
        :type Algorithm: str
        :param KeyType: 加密类型
        :type KeyType: str
        :param DigestType: 摘要类型
        :type DigestType: str
        :param DigestAlgorithm: 摘要算法
        :type DigestAlgorithm: str
        :param Digest: 摘要信息
        :type Digest: str
        :param DS: DS 记录值
        :type DS: str
        :param KeyTag: 密钥标签
        :type KeyTag: int
        :param PublicKey: 公钥
        :type PublicKey: str
        """
        self.Flags = None
        self.Algorithm = None
        self.KeyType = None
        self.DigestType = None
        self.DigestAlgorithm = None
        self.Digest = None
        self.DS = None
        self.KeyTag = None
        self.PublicKey = None


    def _deserialize(self, params):
        self.Flags = params.get("Flags")
        self.Algorithm = params.get("Algorithm")
        self.KeyType = params.get("KeyType")
        self.DigestType = params.get("DigestType")
        self.DigestAlgorithm = params.get("DigestAlgorithm")
        self.Digest = params.get("Digest")
        self.DS = params.get("DS")
        self.KeyTag = params.get("KeyTag")
        self.PublicKey = params.get("PublicKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL7LogsRequest(AbstractModel):
    """DownloadL7Logs请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 起始时间(需严格按照RFC3339标准传参)
        :type StartTime: str
        :param EndTime: 结束时间(需严格按照RFC3339标准传参)
        :type EndTime: str
        :param PageSize: 每页展示条数
        :type PageSize: int
        :param PageNo: 当前页
        :type PageNo: int
        :param Zones: 站点集合
        :type Zones: list of str
        :param Domains: 域名集合
        :type Domains: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.Zones = None
        self.Domains = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.Zones = params.get("Zones")
        self.Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL7LogsResponse(AbstractModel):
    """DownloadL7Logs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 七层离线日志data
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of L7OfflineLog
        :param PageSize: 页面大小
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param PageNo: 页号
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNo: int
        :param Pages: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type Pages: int
        :param TotalSize: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.PageSize = None
        self.PageNo = None
        self.Pages = None
        self.TotalSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = L7OfflineLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        self.RequestId = params.get("RequestId")


class FailReason(AbstractModel):
    """失败原因

    """

    def __init__(self):
        r"""
        :param Reason: 失败原因
        :type Reason: str
        :param Targets: 处理失败的资源列表。
该列表元素来源于输入参数中的Targets，因此格式和入参中的Targets保持一致
        :type Targets: list of str
        """
        self.Reason = None
        self.Targets = None


    def _deserialize(self, params):
        self.Reason = params.get("Reason")
        self.Targets = params.get("Targets")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceRedirect(AbstractModel):
    """访问协议强制https跳转配置

    """

    def __init__(self):
        r"""
        :param Switch: 访问强制跳转配置开关
on：开启
off：关闭
        :type Switch: str
        :param RedirectStatusCode: 重定向状态码
301
302
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectStatusCode: int
        """
        self.Switch = None
        self.RedirectStatusCode = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RedirectStatusCode = params.get("RedirectStatusCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Header(AbstractModel):
    """刷新预热附带的头部信息

    """

    def __init__(self):
        r"""
        :param Name: HTTP头部
        :type Name: str
        :param Value: HTTP头部值
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
        


class HostCertSetting(AbstractModel):
    """域名证书配置

    """

    def __init__(self):
        r"""
        :param Host: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param CertInfo: 服务端证书配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CertInfo: list of ServerCertInfo
        """
        self.Host = None
        self.CertInfo = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        if params.get("CertInfo") is not None:
            self.CertInfo = []
            for item in params.get("CertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self.CertInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hsts(AbstractModel):
    """Hsts配置

    """

    def __init__(self):
        r"""
        :param Switch: 是否开启，on或off。
        :type Switch: str
        :param MaxAge: MaxAge数值。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: int
        :param IncludeSubDomains: 是否包含子域名，on或off。
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeSubDomains: str
        :param Preload: 是否预加载，on或off。
注意：此字段可能返回 null，表示取不到有效值。
        :type Preload: str
        """
        self.Switch = None
        self.MaxAge = None
        self.IncludeSubDomains = None
        self.Preload = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.MaxAge = params.get("MaxAge")
        self.IncludeSubDomains = params.get("IncludeSubDomains")
        self.Preload = params.get("Preload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Https(AbstractModel):
    """域名 https 加速配置，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param Http2: http2 配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Http2: str
        :param OcspStapling: OCSP 配置开关
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type OcspStapling: str
        :param TlsVersion: Tls版本设置，支持设置 TLSv1, TLSV1.1, TLSV1.2, TLSv1.3，修改时必须开启连续的版本
注意：此字段可能返回 null，表示取不到有效值。
        :type TlsVersion: list of str
        :param Hsts: HSTS 配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Hsts: :class:`tencentcloud.teo.v20220106.models.Hsts`
        """
        self.Http2 = None
        self.OcspStapling = None
        self.TlsVersion = None
        self.Hsts = None


    def _deserialize(self, params):
        self.Http2 = params.get("Http2")
        self.OcspStapling = params.get("OcspStapling")
        self.TlsVersion = params.get("TlsVersion")
        if params.get("Hsts") is not None:
            self.Hsts = Hsts()
            self.Hsts._deserialize(params.get("Hsts"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdentifyZoneRequest(AbstractModel):
    """IdentifyZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 站点名称
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
        


class IdentifyZoneResponse(AbstractModel):
    """IdentifyZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 站点名称
        :type Name: str
        :param Subdomain: 子域
        :type Subdomain: str
        :param RecordType: 记录类型
        :type RecordType: str
        :param RecordValue: 记录值
        :type RecordValue: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Subdomain = None
        self.RecordType = None
        self.RecordValue = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Subdomain = params.get("Subdomain")
        self.RecordType = params.get("RecordType")
        self.RecordValue = params.get("RecordValue")
        self.RequestId = params.get("RequestId")


class ImportDnsRecordsRequest(AbstractModel):
    """ImportDnsRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID
        :type ZoneId: str
        :param File: 文件内容
        :type File: str
        """
        self.ZoneId = None
        self.File = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.File = params.get("File")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportDnsRecordsResponse(AbstractModel):
    """ImportDnsRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: 记录 ID
        :type Ids: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ids = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        self.RequestId = params.get("RequestId")


class L7OfflineLog(AbstractModel):
    """离线日志详细信息

    """

    def __init__(self):
        r"""
        :param LogTime: 日志打包开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LogTime: int
        :param Domain: 站点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Size: 原始大小 单位byte
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param Url: 下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param LogPacketName: 日志数据包名
注意：此字段可能返回 null，表示取不到有效值。
        :type LogPacketName: str
        """
        self.LogTime = None
        self.Domain = None
        self.Size = None
        self.Url = None
        self.LogPacketName = None


    def _deserialize(self, params):
        self.LogTime = params.get("LogTime")
        self.Domain = params.get("Domain")
        self.Size = params.get("Size")
        self.Url = params.get("Url")
        self.LogPacketName = params.get("LogPacketName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancing(AbstractModel):
    """负载均衡信息

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param Host: 子域名，填写@表示根域
        :type Host: str
        :param Type: 代理模式：
dns_only: 仅DNS
proxied: 开启代理
        :type Type: str
        :param TTL: 当Type=dns_only表示DNS的TTL时间
        :type TTL: int
        :param OriginId: 使用的源站组ID
        :type OriginId: list of str
        :param Origin: 使用的源站信息
        :type Origin: list of OriginGroup
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Status: 状态
        :type Status: str
        :param Cname: 调度域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        """
        self.LoadBalancingId = None
        self.ZoneId = None
        self.Host = None
        self.Type = None
        self.TTL = None
        self.OriginId = None
        self.Origin = None
        self.UpdateTime = None
        self.Status = None
        self.Cname = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        self.Type = params.get("Type")
        self.TTL = params.get("TTL")
        self.OriginId = params.get("OriginId")
        if params.get("Origin") is not None:
            self.Origin = []
            for item in params.get("Origin"):
                obj = OriginGroup()
                obj._deserialize(item)
                self.Origin.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        self.Cname = params.get("Cname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAge(AbstractModel):
    """浏览器缓存规则配置，用于设置 MaxAge 默认值，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param MaxAgeTime: MaxAge 时间设置，单位秒，最大365天
注意：时间为0，即不缓存。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAgeTime: int
        :param FollowOrigin: 是否遵循源站，on或off，开启时忽略时间设置。
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowOrigin: str
        """
        self.MaxAgeTime = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        self.MaxAgeTime = params.get("MaxAgeTime")
        self.FollowOrigin = params.get("FollowOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRequest(AbstractModel):
    """ModifyApplicationProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 四层代理ID
        :type ProxyId: str
        :param ProxyName: 四层代理名称
        :type ProxyName: str
        :param ForwardClientIp: 参数已经废弃
        :type ForwardClientIp: str
        :param SessionPersist: 参数已经废弃
        :type SessionPersist: bool
        :param SessionPersistTime: 会话保持时间，取值范围：30-3600，单位：秒
        :type SessionPersistTime: int
        :param ProxyType: 服务类型
hostname：子域名
instance：实例
        :type ProxyType: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.ProxyName = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.SessionPersistTime = None
        self.ProxyType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyResponse(AbstractModel):
    """ModifyApplicationProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 四层代理ID
        :type ProxyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProxyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.RequestId = params.get("RequestId")


class ModifyApplicationProxyRuleRequest(AbstractModel):
    """ModifyApplicationProxyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 代理ID
        :type ProxyId: str
        :param RuleId: 规则ID
        :type RuleId: str
        :param Proto: 协议，取值为TCP或者UDP
        :type Proto: str
        :param Port: 端口，支持格式：
80：80端口
81-90：81至90端口
        :type Port: list of str
        :param OriginType: 源站类型，取值：
custom：手动添加
origins：源站组
load_balancing：负载均衡
        :type OriginType: str
        :param OriginValue: 源站信息：
当OriginType=custom时，表示多个：
IP:端口
域名:端口
当OriginType=origins时，包含一个元素，表示源站组ID
当OriginType=load_balancing时，包含一个元素，表示负载均衡ID
        :type OriginValue: list of str
        :param ForwardClientIp: 传递客户端IP，当Proto=TCP时，取值：
TOA：TOA
PPV1: Proxy Protocol传递，协议版本V1
PPV2: Proxy Protocol传递，协议版本V2
OFF：不传递
当Proto=UDP时，取值：
PPV2: Proxy Protocol传递，协议版本V2
OFF：不传递
        :type ForwardClientIp: str
        :param SessionPersist: 是否开启会话保持
        :type SessionPersist: bool
        """
        self.ZoneId = None
        self.ProxyId = None
        self.RuleId = None
        self.Proto = None
        self.Port = None
        self.OriginType = None
        self.OriginValue = None
        self.ForwardClientIp = None
        self.SessionPersist = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.RuleId = params.get("RuleId")
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.OriginType = params.get("OriginType")
        self.OriginValue = params.get("OriginValue")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRuleResponse(AbstractModel):
    """ModifyApplicationProxyRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 规则ID
        :type RuleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class ModifyApplicationProxyRuleStatusRequest(AbstractModel):
    """ModifyApplicationProxyRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 四层代理ID
        :type ProxyId: str
        :param RuleId: 规则ID
        :type RuleId: str
        :param Status: 状态
offline: 停用
online: 启用
        :type Status: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.RuleId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.RuleId = params.get("RuleId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRuleStatusResponse(AbstractModel):
    """ModifyApplicationProxyRuleStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 规则ID
        :type RuleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class ModifyApplicationProxyStatusRequest(AbstractModel):
    """ModifyApplicationProxyStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 四层代理ID
        :type ProxyId: str
        :param Status: 状态
offline: 停用
online: 启用
        :type Status: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyStatusResponse(AbstractModel):
    """ModifyApplicationProxyStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 四层代理ID
        :type ProxyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProxyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.RequestId = params.get("RequestId")


class ModifyDefaultCertificateRequest(AbstractModel):
    """ModifyDefaultCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: Zone ID
        :type ZoneId: str
        :param CertId: 默认证书ID
        :type CertId: str
        :param Status: 证书状态
deployed: 部署证书
disabled:禁用证书
失败状态下重新deployed即可重试失败
        :type Status: str
        """
        self.ZoneId = None
        self.CertId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.CertId = params.get("CertId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDefaultCertificateResponse(AbstractModel):
    """ModifyDefaultCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDnsRecordRequest(AbstractModel):
    """ModifyDnsRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 记录 ID
        :type Id: str
        :param ZoneId: 站点 ID
        :type ZoneId: str
        :param Type: 记录类型
        :type Type: str
        :param Name: 记录名称
        :type Name: str
        :param Content: 记录内容
        :type Content: str
        :param Ttl: 生存时间值
        :type Ttl: int
        :param Priority: 优先级
        :type Priority: int
        :param Mode: 代理模式
        :type Mode: str
        """
        self.Id = None
        self.ZoneId = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Ttl = None
        self.Priority = None
        self.Mode = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Ttl = params.get("Ttl")
        self.Priority = params.get("Priority")
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDnsRecordResponse(AbstractModel):
    """ModifyDnsRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 记录 ID
        :type Id: str
        :param Type: 记录类型
        :type Type: str
        :param Name: 记录名称
        :type Name: str
        :param Content: 记录内容
        :type Content: str
        :param Ttl: 生存时间值
        :type Ttl: int
        :param Priority: 优先级
        :type Priority: int
        :param Mode: 代理模式
        :type Mode: str
        :param Status: 解析状态
        :type Status: str
        :param Cname: CNAME 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        :param Locked: 锁定状态
        :type Locked: bool
        :param CreatedOn: 创建时间
        :type CreatedOn: str
        :param ModifiedOn: 修改时间
        :type ModifiedOn: str
        :param ZoneId: 站点 ID
        :type ZoneId: str
        :param ZoneName: 站点名称
        :type ZoneName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Ttl = None
        self.Priority = None
        self.Mode = None
        self.Status = None
        self.Cname = None
        self.Locked = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.ZoneId = None
        self.ZoneName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Ttl = params.get("Ttl")
        self.Priority = params.get("Priority")
        self.Mode = params.get("Mode")
        self.Status = params.get("Status")
        self.Cname = params.get("Cname")
        self.Locked = params.get("Locked")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.RequestId = params.get("RequestId")


class ModifyDnssecRequest(AbstractModel):
    """ModifyDnssec请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Status: DNSSEC 状态
- enabled 开启
- disabled 关闭
        :type Status: str
        """
        self.Id = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDnssecResponse(AbstractModel):
    """ModifyDnssec返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Name: 站点名称
        :type Name: str
        :param Status: DNSSEC 状态
- enabled 开启
- disabled 关闭
        :type Status: str
        :param Dnssec: DNSSEC 相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Dnssec: :class:`tencentcloud.teo.v20220106.models.DnssecInfo`
        :param ModifiedOn: 修改时间
        :type ModifiedOn: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Status = None
        self.Dnssec = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        if params.get("Dnssec") is not None:
            self.Dnssec = DnssecInfo()
            self.Dnssec._deserialize(params.get("Dnssec"))
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class ModifyHostsCertificateRequest(AbstractModel):
    """ModifyHostsCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: Zone ID
        :type ZoneId: str
        :param Hosts: 本次变更的域名
        :type Hosts: list of str
        :param CertInfo: 证书信息, 只需要传入 CertId 即可, 如果为空, 则使用默认证书
        :type CertInfo: list of ServerCertInfo
        """
        self.ZoneId = None
        self.Hosts = None
        self.CertInfo = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Hosts = params.get("Hosts")
        if params.get("CertInfo") is not None:
            self.CertInfo = []
            for item in params.get("CertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self.CertInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHostsCertificateResponse(AbstractModel):
    """ModifyHostsCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancingRequest(AbstractModel):
    """ModifyLoadBalancing请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        :param Type: 代理模式：
dns_only: 仅DNS
proxied: 开启代理
        :type Type: str
        :param OriginId: 使用的源站组ID
        :type OriginId: list of str
        :param TTL: 当Type=dns_only表示DNS的TTL时间
        :type TTL: int
        """
        self.ZoneId = None
        self.LoadBalancingId = None
        self.Type = None
        self.OriginId = None
        self.TTL = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.Type = params.get("Type")
        self.OriginId = params.get("OriginId")
        self.TTL = params.get("TTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancingResponse(AbstractModel):
    """ModifyLoadBalancing返回参数结构体

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancingStatusRequest(AbstractModel):
    """ModifyLoadBalancingStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        :param Status: 状态
online: 启用
offline: 停用
        :type Status: str
        """
        self.ZoneId = None
        self.LoadBalancingId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancingStatusResponse(AbstractModel):
    """ModifyLoadBalancingStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.RequestId = params.get("RequestId")


class ModifyZoneCnameSpeedUpRequest(AbstractModel):
    """ModifyZoneCnameSpeedUp请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Status: CNAME 加速状态
- enabled 开启
- disabled 关闭
        :type Status: str
        """
        self.Id = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneCnameSpeedUpResponse(AbstractModel):
    """ModifyZoneCnameSpeedUp返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Name: 站点名称
        :type Name: str
        :param Status: CNAME 加速状态
- enabled 开启
- disabled 关闭
        :type Status: str
        :param ModifiedOn: 更新时间
        :type ModifiedOn: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Status = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class ModifyZoneRequest(AbstractModel):
    """ModifyZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID，用于唯一标识站点信息
        :type Id: str
        :param Type: 站点接入方式
- full NS 接入
- partial CNAME 接入
        :type Type: str
        :param VanityNameServers: 自定义站点信息
        :type VanityNameServers: :class:`tencentcloud.teo.v20220106.models.VanityNameServers`
        """
        self.Id = None
        self.Type = None
        self.VanityNameServers = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        if params.get("VanityNameServers") is not None:
            self.VanityNameServers = VanityNameServers()
            self.VanityNameServers._deserialize(params.get("VanityNameServers"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneResponse(AbstractModel):
    """ModifyZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Name: 站点名称
        :type Name: str
        :param OriginalNameServers: 站点当前使用的 NS
        :type OriginalNameServers: list of str
        :param Status: 站点状态
- pending 未接入 NS
- active 已接入 NS
- moved NS 已切走
        :type Status: str
        :param Type: 站点接入方式
- full NS 接入
- partial CNAME 接入
        :type Type: str
        :param NameServers: 腾讯云分配的 NS 列表
        :type NameServers: list of str
        :param CreatedOn: 创建时间
        :type CreatedOn: str
        :param ModifiedOn: 修改时间
        :type ModifiedOn: str
        :param CnameStatus: cname 接入状态
- finished 站点验证完成
- pending 站点验证中
注意：此字段可能返回 null，表示取不到有效值。
        :type CnameStatus: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.OriginalNameServers = None
        self.Status = None
        self.Type = None
        self.NameServers = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.CnameStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.NameServers = params.get("NameServers")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.CnameStatus = params.get("CnameStatus")
        self.RequestId = params.get("RequestId")


class ModifyZoneSettingRequest(AbstractModel):
    """ModifyZoneSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 待变更的站点ID
        :type ZoneId: str
        :param Cache: 缓存过期时间配置
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfig`
        :param CacheKey: 节点缓存键配置
        :type CacheKey: :class:`tencentcloud.teo.v20220106.models.CacheKey`
        :param MaxAge: 浏览器缓存配置
        :type MaxAge: :class:`tencentcloud.teo.v20220106.models.MaxAge`
        :param OfflineCache: 离线缓存
        :type OfflineCache: :class:`tencentcloud.teo.v20220106.models.OfflineCache`
        :param Quic: Quic访问
        :type Quic: :class:`tencentcloud.teo.v20220106.models.Quic`
        :param PostMaxSize: POST请求传输配置
        :type PostMaxSize: :class:`tencentcloud.teo.v20220106.models.PostMaxSize`
        :param Compression: 智能压缩配置
        :type Compression: :class:`tencentcloud.teo.v20220106.models.Compression`
        :param UpstreamHttp2: http2回源配置
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220106.models.UpstreamHttp2`
        :param ForceRedirect: 访问协议强制https跳转配置
        :type ForceRedirect: :class:`tencentcloud.teo.v20220106.models.ForceRedirect`
        :param Https: Https 加速配置
        :type Https: :class:`tencentcloud.teo.v20220106.models.Https`
        :param Origin: 源站配置
        :type Origin: :class:`tencentcloud.teo.v20220106.models.Origin`
        :param SmartRouting: 智能加速配置
        :type SmartRouting: :class:`tencentcloud.teo.v20220106.models.SmartRouting`
        :param WebSocket: WebSocket配置
        :type WebSocket: :class:`tencentcloud.teo.v20220106.models.WebSocket`
        :param ClientIpHeader: 客户端IP回源请求头配置
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220106.models.ClientIp`
        """
        self.ZoneId = None
        self.Cache = None
        self.CacheKey = None
        self.MaxAge = None
        self.OfflineCache = None
        self.Quic = None
        self.PostMaxSize = None
        self.Compression = None
        self.UpstreamHttp2 = None
        self.ForceRedirect = None
        self.Https = None
        self.Origin = None
        self.SmartRouting = None
        self.WebSocket = None
        self.ClientIpHeader = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("Cache") is not None:
            self.Cache = CacheConfig()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("OfflineCache") is not None:
            self.OfflineCache = OfflineCache()
            self.OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("Quic") is not None:
            self.Quic = Quic()
            self.Quic._deserialize(params.get("Quic"))
        if params.get("PostMaxSize") is not None:
            self.PostMaxSize = PostMaxSize()
            self.PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("UpstreamHttp2") is not None:
            self.UpstreamHttp2 = UpstreamHttp2()
            self.UpstreamHttp2._deserialize(params.get("UpstreamHttp2"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("SmartRouting") is not None:
            self.SmartRouting = SmartRouting()
            self.SmartRouting._deserialize(params.get("SmartRouting"))
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        if params.get("ClientIpHeader") is not None:
            self.ClientIpHeader = ClientIp()
            self.ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneSettingResponse(AbstractModel):
    """ModifyZoneSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ZoneId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RequestId = params.get("RequestId")


class ModifyZoneStatusRequest(AbstractModel):
    """ModifyZoneStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Paused: 站点状态
- false 开启站点
- true 关闭站点
        :type Paused: bool
        """
        self.Id = None
        self.Paused = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Paused = params.get("Paused")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneStatusResponse(AbstractModel):
    """ModifyZoneStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Name: 站点名称
        :type Name: str
        :param Paused: 站点状态
- false 开启站点
- true 关闭站点
        :type Paused: bool
        :param ModifiedOn: 更新时间
        :type ModifiedOn: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Paused = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Paused = params.get("Paused")
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class OfflineCache(AbstractModel):
    """离线缓存是否开启

    """

    def __init__(self):
        r"""
        :param Switch: on | off, 离线缓存是否开启
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Origin(AbstractModel):
    """源站配置。

    """

    def __init__(self):
        r"""
        :param OriginPullProtocol: 回源协议配置
http：强制 http 回源
follow：协议跟随回源
https：强制 https 回源，https 回源时仅支持源站 443 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginPullProtocol: str
        """
        self.OriginPullProtocol = None


    def _deserialize(self, params):
        self.OriginPullProtocol = params.get("OriginPullProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginGroup(AbstractModel):
    """源站组信息

    """

    def __init__(self):
        r"""
        :param OriginId: 源站组ID
        :type OriginId: str
        :param OriginName: 源站组名称
        :type OriginName: str
        :param Type: 配置类型
        :type Type: str
        :param Record: 记录
        :type Record: list of OriginRecord
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ZoneName: 站点名称
        :type ZoneName: str
        :param OriginType: 源站类型
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginType: str
        :param ApplicationProxyUsed: 是否为四层代理使用
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationProxyUsed: bool
        :param LoadBalancingUsed: 是否为负载均衡使用
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancingUsed: bool
        """
        self.OriginId = None
        self.OriginName = None
        self.Type = None
        self.Record = None
        self.UpdateTime = None
        self.ZoneId = None
        self.ZoneName = None
        self.OriginType = None
        self.ApplicationProxyUsed = None
        self.LoadBalancingUsed = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.OriginName = params.get("OriginName")
        self.Type = params.get("Type")
        if params.get("Record") is not None:
            self.Record = []
            for item in params.get("Record"):
                obj = OriginRecord()
                obj._deserialize(item)
                self.Record.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.OriginType = params.get("OriginType")
        self.ApplicationProxyUsed = params.get("ApplicationProxyUsed")
        self.LoadBalancingUsed = params.get("LoadBalancingUsed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginRecord(AbstractModel):
    """源站组记录

    """

    def __init__(self):
        r"""
        :param Record: 记录值
        :type Record: str
        :param Area: 当源站配置类型Type=area时，表示区域
当源站类型Type=area时，为空表示默认区域
        :type Area: list of str
        :param Weight: 当源站配置类型Type=weight时，表示权重
        :type Weight: int
        :param Port: 端口
        :type Port: int
        :param RecordId: 记录ID
        :type RecordId: str
        :param Private: 是否私有鉴权
当源站类型OriginType=third_part时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Private: bool
        :param PrivateParameter: 私有鉴权参数
当源站类型Private=true时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateParameter: list of OriginRecordPrivateParameter
        """
        self.Record = None
        self.Area = None
        self.Weight = None
        self.Port = None
        self.RecordId = None
        self.Private = None
        self.PrivateParameter = None


    def _deserialize(self, params):
        self.Record = params.get("Record")
        self.Area = params.get("Area")
        self.Weight = params.get("Weight")
        self.Port = params.get("Port")
        self.RecordId = params.get("RecordId")
        self.Private = params.get("Private")
        if params.get("PrivateParameter") is not None:
            self.PrivateParameter = []
            for item in params.get("PrivateParameter"):
                obj = OriginRecordPrivateParameter()
                obj._deserialize(item)
                self.PrivateParameter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginRecordPrivateParameter(AbstractModel):
    """源站记录私有鉴权参数

    """

    def __init__(self):
        r"""
        :param Name: 私有鉴权参数名称：
"AccessKeyId"：Access Key ID
"SecretAccessKey"：Secret Access Key
        :type Name: str
        :param Value: 私有鉴权参数数值
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
        


class PostMaxSize(AbstractModel):
    """POST请求上传文件流式传输最大限制

    """

    def __init__(self):
        r"""
        :param Switch: 是调整POST请求限制，平台默认为32MB。
关闭：off，
开启：on。
        :type Switch: str
        :param MaxSize: 最大限制，取值在1MB和500MB之间。单位字节
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxSize: int
        """
        self.Switch = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryString(AbstractModel):
    """CacheKey中包含请求参数

    """

    def __init__(self):
        r"""
        :param Switch: on | off CacheKey是否由QueryString组成
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Action: includeCustom:使用部分url参数
excludeCustom:排除部分url参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param Value: 使用/排除的url参数数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of str
        """
        self.Switch = None
        self.Action = None
        self.Value = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Action = params.get("Action")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quic(AbstractModel):
    """Quic配置项

    """

    def __init__(self):
        r"""
        :param Switch: 是否启动Quic配置
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReclaimZoneRequest(AbstractModel):
    """ReclaimZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 站点名称
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
        


class ReclaimZoneResponse(AbstractModel):
    """ReclaimZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 站点名称
        :type Name: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.RequestId = params.get("RequestId")


class ScanDnsRecordsRequest(AbstractModel):
    """ScanDnsRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanDnsRecordsResponse(AbstractModel):
    """ScanDnsRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 扫描状态
- doing 扫描中
- done 扫描完成
        :type Status: str
        :param RecordsAdded: 扫描后添加的记录数
        :type RecordsAdded: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RecordsAdded = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RecordsAdded = params.get("RecordsAdded")
        self.RequestId = params.get("RequestId")


class ServerCertInfo(AbstractModel):
    """https 服务端证书配置

    """

    def __init__(self):
        r"""
        :param CertId: 服务器证书 ID, 默认证书ID, 或在 SSL 证书管理进行证书托管时自动生成
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param Alias: 证书备注名
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Type: 证书类型:
default: 默认证书
upload:用户上传
managed:腾讯云托管
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param ExpireTime: 证书过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param DeployTime: 证书部署时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployTime: str
        :param Status: 部署状态:
processing: 部署中
deployed: 已部署
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self.CertId = None
        self.Alias = None
        self.Type = None
        self.ExpireTime = None
        self.DeployTime = None
        self.Status = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.Alias = params.get("Alias")
        self.Type = params.get("Type")
        self.ExpireTime = params.get("ExpireTime")
        self.DeployTime = params.get("DeployTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartRouting(AbstractModel):
    """智能加速配置

    """

    def __init__(self):
        r"""
        :param Switch: 智能加速配置开关
on：开启
off：关闭
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """内容管理任务结果

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param Status: 状态
        :type Status: str
        :param Target: 资源
        :type Target: str
        :param Type: 任务类型
        :type Type: str
        :param CreateTime: 任务创建时间
        :type CreateTime: str
        :param UpdateTime: 任务完成时间
        :type UpdateTime: str
        """
        self.JobId = None
        self.Status = None
        self.Target = None
        self.Type = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Status = params.get("Status")
        self.Target = params.get("Target")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpstreamHttp2(AbstractModel):
    """Http2回源配置

    """

    def __init__(self):
        r"""
        :param Switch: http2回源配置开关
on：开启
off：关闭
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VanityNameServers(AbstractModel):
    """自定义 nameservers

    """

    def __init__(self):
        r"""
        :param Switch: 自定义 ns 开关
- on 开启
- off 关闭
        :type Switch: str
        :param Servers: 自定义 ns 列表
        :type Servers: list of str
        """
        self.Switch = None
        self.Servers = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Servers = params.get("Servers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VanityNameServersIps(AbstractModel):
    """自定义名字服务器 IP 信息

    """

    def __init__(self):
        r"""
        :param Name: 自定义名字服务器名称
        :type Name: str
        :param IPv4: 自定义名字服务器 IPv4 地址
        :type IPv4: str
        """
        self.Name = None
        self.IPv4 = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.IPv4 = params.get("IPv4")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebSocket(AbstractModel):
    """WebSocket配置

    """

    def __init__(self):
        r"""
        :param Switch: WebSocket 超时配置开关, 开关为off时，平台仍支持WebSocket连接，此时超时时间默认为15秒，若需要调整超时时间，将开关置为on.
        :type Switch: str
        :param Timeout: 设置超时时间，单位为秒，最大超时时间120秒。
        :type Timeout: int
        """
        self.Switch = None
        self.Timeout = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Zone(AbstractModel):
    """站点信息

    """

    def __init__(self):
        r"""
        :param Id: 站点ID
        :type Id: str
        :param Name: 站点名称
        :type Name: str
        :param OriginalNameServers: 站点当前使用的 NS 列表
        :type OriginalNameServers: list of str
        :param NameServers: 腾讯云分配的 NS 列表
        :type NameServers: list of str
        :param Status: 站点状态
- active：NS 已切换
- pending：NS 未切换
- moved：NS 已切走
- deactivated：被封禁
        :type Status: str
        :param Type: 站点接入方式
- full：NS 接入
- partial：CNAME 接入
        :type Type: str
        :param Paused: 站点是否关闭
        :type Paused: bool
        :param CreatedOn: 站点创建时间
        :type CreatedOn: str
        :param ModifiedOn: 站点修改时间
        :type ModifiedOn: str
        :param CnameStatus: cname 接入状态
- finished 站点已验证
- pending 站点验证中
注意：此字段可能返回 null，表示取不到有效值。
        :type CnameStatus: str
        """
        self.Id = None
        self.Name = None
        self.OriginalNameServers = None
        self.NameServers = None
        self.Status = None
        self.Type = None
        self.Paused = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.CnameStatus = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.NameServers = params.get("NameServers")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Paused = params.get("Paused")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.CnameStatus = params.get("CnameStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneFilter(AbstractModel):
    """站点查询过滤条件

    """

    def __init__(self):
        r"""
        :param Name: 过滤字段名，支持的列表如下：
- name: 站点名。
- status: 站点状态
        :type Name: str
        :param Values: 过滤字段值
        :type Values: list of str
        :param Fuzzy: 是否启用模糊查询，仅支持过滤字段名为name。模糊查询时，Values长度最大为1
        :type Fuzzy: bool
        """
        self.Name = None
        self.Values = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        