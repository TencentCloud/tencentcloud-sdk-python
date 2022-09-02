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


class AccessFullTextInfo(AbstractModel):
    """DescribeAccessIndex

    """

    def __init__(self):
        r"""
        :param CaseSensitive: 是否大小写敏感
注意：此字段可能返回 null，表示取不到有效值。
        :type CaseSensitive: bool
        :param Tokenizer: 全文索引的分词符，字符串中每个字符代表一个分词符
注意：此字段可能返回 null，表示取不到有效值。
        :type Tokenizer: str
        :param ContainZH: 是否包含中文
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainZH: bool
        """
        self.CaseSensitive = None
        self.Tokenizer = None
        self.ContainZH = None


    def _deserialize(self, params):
        self.CaseSensitive = params.get("CaseSensitive")
        self.Tokenizer = params.get("Tokenizer")
        self.ContainZH = params.get("ContainZH")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessKeyValueInfo(AbstractModel):
    """用于 DescribeAccessIndex 的出参

    """

    def __init__(self):
        r"""
        :param Key: 需要配置键值或者元字段索引的字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: 字段的索引描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.waf.v20180125.models.AccessValueInfo`
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        if params.get("Value") is not None:
            self.Value = AccessValueInfo()
            self.Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessLogInfo(AbstractModel):
    """单条日志数据描述

    """

    def __init__(self):
        r"""
        :param Time: 日志时间，单位ms
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: int
        :param TopicId: 日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param TopicName: 日志主题名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param Source: 日志来源IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param FileName: 日志文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param PkgId: 日志上报请求包的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgId: str
        :param PkgLogId: 请求包内日志的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgLogId: str
        :param LogJson: 日志内容的Json序列化字符串
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type LogJson: str
        """
        self.Time = None
        self.TopicId = None
        self.TopicName = None
        self.Source = None
        self.FileName = None
        self.PkgId = None
        self.PkgLogId = None
        self.LogJson = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Source = params.get("Source")
        self.FileName = params.get("FileName")
        self.PkgId = params.get("PkgId")
        self.PkgLogId = params.get("PkgLogId")
        self.LogJson = params.get("LogJson")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessLogItem(AbstractModel):
    """日志KeyValue对

    """

    def __init__(self):
        r"""
        :param Key: 日记Key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: 日志Value
注意：此字段可能返回 null，表示取不到有效值。
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
        


class AccessLogItems(AbstractModel):
    """日志KeyValue对数组，用于搜索访问日志

    """

    def __init__(self):
        r"""
        :param Data: 分析结果返回的KV数据对
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of AccessLogItem
        """
        self.Data = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = AccessLogItem()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessRuleInfo(AbstractModel):
    """DescribeAccessIndex接口的出参数

    """

    def __init__(self):
        r"""
        :param FullText: 全文索引配置
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type FullText: :class:`tencentcloud.waf.v20180125.models.AccessFullTextInfo`
        :param KeyValue: 键值索引配置
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyValue: :class:`tencentcloud.waf.v20180125.models.AccessRuleKeyValueInfo`
        :param Tag: 元字段索引配置
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: :class:`tencentcloud.waf.v20180125.models.AccessRuleTagInfo`
        """
        self.FullText = None
        self.KeyValue = None
        self.Tag = None


    def _deserialize(self, params):
        if params.get("FullText") is not None:
            self.FullText = AccessFullTextInfo()
            self.FullText._deserialize(params.get("FullText"))
        if params.get("KeyValue") is not None:
            self.KeyValue = AccessRuleKeyValueInfo()
            self.KeyValue._deserialize(params.get("KeyValue"))
        if params.get("Tag") is not None:
            self.Tag = AccessRuleTagInfo()
            self.Tag._deserialize(params.get("Tag"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessRuleKeyValueInfo(AbstractModel):
    """DescribeAccessIndex接口的出参

    """

    def __init__(self):
        r"""
        :param CaseSensitive: 是否大小写敏感
注意：此字段可能返回 null，表示取不到有效值。
        :type CaseSensitive: bool
        :param KeyValues: 需要建立索引的键值对信息；最大只能配置100个键值对
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyValues: list of AccessKeyValueInfo
        """
        self.CaseSensitive = None
        self.KeyValues = None


    def _deserialize(self, params):
        self.CaseSensitive = params.get("CaseSensitive")
        if params.get("KeyValues") is not None:
            self.KeyValues = []
            for item in params.get("KeyValues"):
                obj = AccessKeyValueInfo()
                obj._deserialize(item)
                self.KeyValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessRuleTagInfo(AbstractModel):
    """DescribeAccessIndex接口的出参

    """

    def __init__(self):
        r"""
        :param CaseSensitive: 是否大小写敏感
注意：此字段可能返回 null，表示取不到有效值。
        :type CaseSensitive: bool
        :param KeyValues: 标签索引配置中的字段信息
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyValues: list of AccessKeyValueInfo
        """
        self.CaseSensitive = None
        self.KeyValues = None


    def _deserialize(self, params):
        self.CaseSensitive = params.get("CaseSensitive")
        if params.get("KeyValues") is not None:
            self.KeyValues = []
            for item in params.get("KeyValues"):
                obj = AccessKeyValueInfo()
                obj._deserialize(item)
                self.KeyValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessValueInfo(AbstractModel):
    """用于DescribeAccessIndex接口的出参

    """

    def __init__(self):
        r"""
        :param Type: 字段类型，目前支持的类型有：long、text、double
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Tokenizer: 字段的分词符，只有当字段类型为text时才有意义；输入字符串中的每个字符代表一个分词符
注意：此字段可能返回 null，表示取不到有效值。
        :type Tokenizer: str
        :param SqlFlag: 字段是否开启分析功能
注意：此字段可能返回 null，表示取不到有效值。
        :type SqlFlag: bool
        :param ContainZH: 是否包含中文
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainZH: bool
        """
        self.Type = None
        self.Tokenizer = None
        self.SqlFlag = None
        self.ContainZH = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Tokenizer = params.get("Tokenizer")
        self.SqlFlag = params.get("SqlFlag")
        self.ContainZH = params.get("ContainZH")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCustomRuleRequest(AbstractModel):
    """AddCustomRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 规则名称
        :type Name: str
        :param SortId: 优先级
        :type SortId: str
        :param ExpireTime: 过期时间
        :type ExpireTime: str
        :param Strategies: 策略详情
        :type Strategies: list of Strategy
        :param Domain: 需要添加策略的域名
        :type Domain: str
        :param ActionType: 动作类型
        :type ActionType: str
        :param Redirect: 如果动作是重定向，则表示重定向的地址；其他情况可以为空
        :type Redirect: str
        :param Edition: "clb-waf"或者"sparta-waf"
        :type Edition: str
        :param Bypass: 放行的详情
        :type Bypass: str
        """
        self.Name = None
        self.SortId = None
        self.ExpireTime = None
        self.Strategies = None
        self.Domain = None
        self.ActionType = None
        self.Redirect = None
        self.Edition = None
        self.Bypass = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.SortId = params.get("SortId")
        self.ExpireTime = params.get("ExpireTime")
        if params.get("Strategies") is not None:
            self.Strategies = []
            for item in params.get("Strategies"):
                obj = Strategy()
                obj._deserialize(item)
                self.Strategies.append(obj)
        self.Domain = params.get("Domain")
        self.ActionType = params.get("ActionType")
        self.Redirect = params.get("Redirect")
        self.Edition = params.get("Edition")
        self.Bypass = params.get("Bypass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCustomRuleResponse(AbstractModel):
    """AddCustomRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param Success: 操作的状态码，如果所有的资源操作成功则返回的是成功的状态码，如果有资源操作失败则需要解析Message的内容来查看哪个资源失败
        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`
        :param RuleId: 添加成功的规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = ResponseCode()
            self.Success._deserialize(params.get("Success"))
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class AddDomainWhiteRuleRequest(AbstractModel):
    """AddDomainWhiteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 需要添加的域名
        :type Domain: str
        :param Rules: 需要添加的规则
        :type Rules: list of int non-negative
        :param Url: 需要添加的规则url
        :type Url: str
        :param Function: 规则的方法
        :type Function: str
        :param Status: 规则的开关
        :type Status: int
        """
        self.Domain = None
        self.Rules = None
        self.Url = None
        self.Function = None
        self.Status = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Rules = params.get("Rules")
        self.Url = params.get("Url")
        self.Function = params.get("Function")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDomainWhiteRuleResponse(AbstractModel):
    """AddDomainWhiteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 规则id
        :type Id: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class AddSpartaProtectionRequest(AbstractModel):
    """AddSpartaProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 需要防御的域名
        :type Domain: str
        :param CertType: 证书类型，0表示没有证书，CertType=1表示自有证书,2 为托管证书
        :type CertType: int
        :param IsCdn: 表示是否开启了CDN代理，1：有部署CDN，0：未部署CDN
        :type IsCdn: int
        :param UpstreamType: 回源类型，0表示通过IP回源,1 表示通过域名回源
        :type UpstreamType: int
        :param IsWebsocket: 是否开启WebSocket支持，1表示开启，0不开启
        :type IsWebsocket: int
        :param LoadBalance: 负载均衡策略，0表示轮徇，1表示IP hash
        :type LoadBalance: str
        :param Cert: CertType=1时，需要填次参数，表示证书内容
        :type Cert: str
        :param PrivateKey: CertType=1时，需要填次参数，表示证书的私钥
        :type PrivateKey: str
        :param SSLId: CertType=2时，需要填次参数，表示证书的ID
        :type SSLId: str
        :param ResourceId: Waf的资源ID
        :type ResourceId: str
        :param UpstreamScheme: HTTPS回源协议，填http或者https
        :type UpstreamScheme: str
        :param HttpsUpstreamPort: HTTPS回源端口,仅UpstreamScheme为http时需要填当前字段
        :type HttpsUpstreamPort: str
        :param IsGray: 是否开启灰度，0表示不开启灰度
        :type IsGray: int
        :param GrayAreas: 灰度的地区
        :type GrayAreas: list of str
        :param UpstreamDomain: UpstreamType=1时，填次字段表示回源域名
        :type UpstreamDomain: str
        :param SrcList: UpstreamType=0时，填次字段表示回源IP
        :type SrcList: list of str
        :param IsHttp2: 是否开启HTTP2,开启HTTP2需要HTTPS支持
        :type IsHttp2: int
        :param HttpsRewrite: 表示是否强制跳转到HTTPS，1强制跳转Https，0不强制跳转
        :type HttpsRewrite: int
        :param Ports: 服务有多端口需要设置此字段
        :type Ports: list of PortItem
        :param Edition: 版本：sparta-waf、clb-waf、cdn-waf
        :type Edition: str
        :param IsKeepAlive: 是否开启长连接，仅IP回源时可以用填次参数，域名回源时这个参数无效
        :type IsKeepAlive: str
        :param InstanceID: 实例id，上线之后带上此字段
        :type InstanceID: str
        :param Anycast: anycast IP类型开关： 0 普通IP 1 Anycast IP
        :type Anycast: int
        :param Weights: src权重
        :type Weights: list of int
        """
        self.Domain = None
        self.CertType = None
        self.IsCdn = None
        self.UpstreamType = None
        self.IsWebsocket = None
        self.LoadBalance = None
        self.Cert = None
        self.PrivateKey = None
        self.SSLId = None
        self.ResourceId = None
        self.UpstreamScheme = None
        self.HttpsUpstreamPort = None
        self.IsGray = None
        self.GrayAreas = None
        self.UpstreamDomain = None
        self.SrcList = None
        self.IsHttp2 = None
        self.HttpsRewrite = None
        self.Ports = None
        self.Edition = None
        self.IsKeepAlive = None
        self.InstanceID = None
        self.Anycast = None
        self.Weights = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.CertType = params.get("CertType")
        self.IsCdn = params.get("IsCdn")
        self.UpstreamType = params.get("UpstreamType")
        self.IsWebsocket = params.get("IsWebsocket")
        self.LoadBalance = params.get("LoadBalance")
        self.Cert = params.get("Cert")
        self.PrivateKey = params.get("PrivateKey")
        self.SSLId = params.get("SSLId")
        self.ResourceId = params.get("ResourceId")
        self.UpstreamScheme = params.get("UpstreamScheme")
        self.HttpsUpstreamPort = params.get("HttpsUpstreamPort")
        self.IsGray = params.get("IsGray")
        self.GrayAreas = params.get("GrayAreas")
        self.UpstreamDomain = params.get("UpstreamDomain")
        self.SrcList = params.get("SrcList")
        self.IsHttp2 = params.get("IsHttp2")
        self.HttpsRewrite = params.get("HttpsRewrite")
        if params.get("Ports") is not None:
            self.Ports = []
            for item in params.get("Ports"):
                obj = PortItem()
                obj._deserialize(item)
                self.Ports.append(obj)
        self.Edition = params.get("Edition")
        self.IsKeepAlive = params.get("IsKeepAlive")
        self.InstanceID = params.get("InstanceID")
        self.Anycast = params.get("Anycast")
        self.Weights = params.get("Weights")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSpartaProtectionResponse(AbstractModel):
    """AddSpartaProtection返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AutoDenyDetail(AbstractModel):
    """Waf 攻击自动封禁详情

    """

    def __init__(self):
        r"""
        :param AttackTags: 攻击封禁类型标签
        :type AttackTags: list of str
        :param AttackThreshold: 攻击次数阈值
        :type AttackThreshold: int
        :param DefenseStatus: 自动封禁状态
        :type DefenseStatus: int
        :param TimeThreshold: 攻击时间阈值
        :type TimeThreshold: int
        :param DenyTimeThreshold: 自动封禁时间
        :type DenyTimeThreshold: int
        :param LastUpdateTime: 最后更新时间
        :type LastUpdateTime: str
        """
        self.AttackTags = None
        self.AttackThreshold = None
        self.DefenseStatus = None
        self.TimeThreshold = None
        self.DenyTimeThreshold = None
        self.LastUpdateTime = None


    def _deserialize(self, params):
        self.AttackTags = params.get("AttackTags")
        self.AttackThreshold = params.get("AttackThreshold")
        self.DefenseStatus = params.get("DefenseStatus")
        self.TimeThreshold = params.get("TimeThreshold")
        self.DenyTimeThreshold = params.get("DenyTimeThreshold")
        self.LastUpdateTime = params.get("LastUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotPkg(AbstractModel):
    """Bot资源信息

    """

    def __init__(self):
        r"""
        :param ResourceIds: 资源id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: int
        :param BeginTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: str
        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param InquireNum: 申请数量
注意：此字段可能返回 null，表示取不到有效值。
        :type InquireNum: int
        :param UsedNum: 使用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedNum: int
        :param Type: 子产品code
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.ResourceIds = None
        self.Status = None
        self.Region = None
        self.BeginTime = None
        self.EndTime = None
        self.InquireNum = None
        self.UsedNum = None
        self.Type = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.Status = params.get("Status")
        self.Region = params.get("Region")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.InquireNum = params.get("InquireNum")
        self.UsedNum = params.get("UsedNum")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotQPS(AbstractModel):
    """bot的qps详情

    """

    def __init__(self):
        r"""
        :param ResourceIds: 资源id
        :type ResourceIds: str
        :param ValidTime: 有效时间
        :type ValidTime: str
        :param Count: 资源数量
        :type Count: int
        :param Region: 资源所在地区
        :type Region: str
        :param MaxBotQPS: 使用qps的最大值
        :type MaxBotQPS: int
        """
        self.ResourceIds = None
        self.ValidTime = None
        self.Count = None
        self.Region = None
        self.MaxBotQPS = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.ValidTime = params.get("ValidTime")
        self.Count = params.get("Count")
        self.Region = params.get("Region")
        self.MaxBotQPS = params.get("MaxBotQPS")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotStatPointItem(AbstractModel):
    """bot的趋势图对象

    """

    def __init__(self):
        r"""
        :param TimeStamp: 横坐标
        :type TimeStamp: str
        :param Key: value的所属对象
        :type Key: str
        :param Value: 纵列表
        :type Value: int
        :param Label: Key对应的页面展示内容
        :type Label: str
        """
        self.TimeStamp = None
        self.Key = None
        self.Value = None
        self.Label = None


    def _deserialize(self, params):
        self.TimeStamp = params.get("TimeStamp")
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdcCluster(AbstractModel):
    """CDC场景下负载均衡WAF的集群信息

    """

    def __init__(self):
        r"""
        :param Id: cdc的集群id
        :type Id: str
        :param Name: cdc的集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdcRegion(AbstractModel):
    """CDC场景下负载均衡WAF的地域信息

    """

    def __init__(self):
        r"""
        :param Region: 地域
        :type Region: str
        :param Clusters: 该地域对应的集群信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Clusters: list of CdcCluster
        """
        self.Region = None
        self.Clusters = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        if params.get("Clusters") is not None:
            self.Clusters = []
            for item in params.get("Clusters"):
                obj = CdcCluster()
                obj._deserialize(item)
                self.Clusters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessExportRequest(AbstractModel):
    """CreateAccessExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param TopicId: 客户要查询的日志主题ID，每个客户都有对应的一个主题
        :type TopicId: str
        :param From: 要查询的日志的起始时间，Unix时间戳，单位ms
        :type From: int
        :param To: 要查询的日志的结束时间，Unix时间戳，单位ms
        :type To: int
        :param Query: 日志导出检索语句
        :type Query: str
        :param Count: 日志导出数量，最大值100w
        :type Count: int
        :param Format: 日志导出数据格式。json，csv，默认为json
        :type Format: str
        :param Order: 日志导出时间排序。desc，asc，默认为desc
        :type Order: str
        """
        self.TopicId = None
        self.From = None
        self.To = None
        self.Query = None
        self.Count = None
        self.Format = None
        self.Order = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.From = params.get("From")
        self.To = params.get("To")
        self.Query = params.get("Query")
        self.Count = params.get("Count")
        self.Format = params.get("Format")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessExportResponse(AbstractModel):
    """CreateAccessExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param ExportId: 日志导出ID。
        :type ExportId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ExportId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ExportId = params.get("ExportId")
        self.RequestId = params.get("RequestId")


class DeleteAccessExportRequest(AbstractModel):
    """DeleteAccessExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ExportId: 日志导出ID
        :type ExportId: str
        :param TopicId: 日志主题
        :type TopicId: str
        """
        self.ExportId = None
        self.TopicId = None


    def _deserialize(self, params):
        self.ExportId = params.get("ExportId")
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccessExportResponse(AbstractModel):
    """DeleteAccessExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAttackDownloadRecordRequest(AbstractModel):
    """DeleteAttackDownloadRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 下载任务记录唯一标记
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
        


class DeleteAttackDownloadRecordResponse(AbstractModel):
    """DeleteAttackDownloadRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDomainWhiteRulesRequest(AbstractModel):
    """DeleteDomainWhiteRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 需要删除的规则域名
        :type Domain: str
        :param Ids: 需要删除的白名单规则
        :type Ids: list of int non-negative
        """
        self.Domain = None
        self.Ids = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainWhiteRulesResponse(AbstractModel):
    """DeleteDomainWhiteRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DeleteDownloadRecordRequest(AbstractModel):
    """DeleteDownloadRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param Flow: 记录id
        :type Flow: str
        """
        self.Flow = None


    def _deserialize(self, params):
        self.Flow = params.get("Flow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDownloadRecordResponse(AbstractModel):
    """DeleteDownloadRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteIpAccessControlRequest(AbstractModel):
    """DeleteIpAccessControl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param Items: 删除的ip数组
        :type Items: list of str
        :param DeleteAll: 删除对应的域名下的所有黑/白IP名额单
        :type DeleteAll: bool
        """
        self.Domain = None
        self.Items = None
        self.DeleteAll = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Items = params.get("Items")
        self.DeleteAll = params.get("DeleteAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIpAccessControlResponse(AbstractModel):
    """DeleteIpAccessControl返回参数结构体

    """

    def __init__(self):
        r"""
        :param FailedItems: 删除失败的条目
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedItems: str
        :param FailedCount: 删除失败的条目数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FailedItems = None
        self.FailedCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailedItems = params.get("FailedItems")
        self.FailedCount = params.get("FailedCount")
        self.RequestId = params.get("RequestId")


class DeleteSessionRequest(AbstractModel):
    """DeleteSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param Edition: clb-waf 或者 sprta-waf
        :type Edition: str
        """
        self.Domain = None
        self.Edition = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Edition = params.get("Edition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSessionResponse(AbstractModel):
    """DeleteSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeAccessExportsRequest(AbstractModel):
    """DescribeAccessExports请求参数结构体

    """

    def __init__(self):
        r"""
        :param TopicId: 客户要查询的日志主题ID，每个客户都有对应的一个主题
        :type TopicId: str
        :param Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param Limit: 分页单页限制数目，默认值为20，最大值100
        :type Limit: int
        """
        self.TopicId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessExportsResponse(AbstractModel):
    """DescribeAccessExports返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 日志导出ID。
        :type TotalCount: int
        :param Exports: 日志导出列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Exports: list of ExportAccessInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Exports = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Exports") is not None:
            self.Exports = []
            for item in params.get("Exports"):
                obj = ExportAccessInfo()
                obj._deserialize(item)
                self.Exports.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAccessFastAnalysisRequest(AbstractModel):
    """DescribeAccessFastAnalysis请求参数结构体

    """

    def __init__(self):
        r"""
        :param TopicId: 客户要查询的日志主题ID，每个客户都有对应的一个主题
        :type TopicId: str
        :param From: 要查询的日志的起始时间，Unix时间戳，单位ms
        :type From: int
        :param To: 要查询的日志的结束时间，Unix时间戳，单位ms
        :type To: int
        :param Query: 查询语句，语句长度最大为4096，由于本接口是分析接口，如果无过滤条件，必须传 * 表示匹配所有，参考CLS的分析统计语句的文档
        :type Query: str
        :param FieldName: 需要分析统计的字段名
        :type FieldName: str
        """
        self.TopicId = None
        self.From = None
        self.To = None
        self.Query = None
        self.FieldName = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.From = params.get("From")
        self.To = params.get("To")
        self.Query = params.get("Query")
        self.FieldName = params.get("FieldName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessFastAnalysisResponse(AbstractModel):
    """DescribeAccessFastAnalysis返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccessIndexRequest(AbstractModel):
    """DescribeAccessIndex请求参数结构体

    """


class DescribeAccessIndexResponse(AbstractModel):
    """DescribeAccessIndex返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 是否生效
        :type Status: bool
        :param Rule: 索引配置信息
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Rule: :class:`tencentcloud.waf.v20180125.models.AccessRuleInfo`
        :param ModifyTime: 索引修改时间，初始值为索引创建时间。
        :type ModifyTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Rule = None
        self.ModifyTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        if params.get("Rule") is not None:
            self.Rule = AccessRuleInfo()
            self.Rule._deserialize(params.get("Rule"))
        self.ModifyTime = params.get("ModifyTime")
        self.RequestId = params.get("RequestId")


class DescribeAutoDenyIPRequest(AbstractModel):
    """DescribeAutoDenyIP请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param Ip: 查询IP自动封禁状态
        :type Ip: str
        :param Count: 计数标识
        :type Count: int
        :param Category: 类别
        :type Category: str
        :param VtsMin: 有效时间最小时间戳
        :type VtsMin: int
        :param VtsMax: 有效时间最大时间戳
        :type VtsMax: int
        :param CtsMin: 创建时间最小时间戳
        :type CtsMin: int
        :param CtsMax: 创建时间最大时间戳
        :type CtsMax: int
        :param Skip: 偏移量
        :type Skip: int
        :param Limit: 限制条数
        :type Limit: int
        :param Name: 策略名字
        :type Name: str
        :param Sort: 排序参数
        :type Sort: str
        """
        self.Domain = None
        self.Ip = None
        self.Count = None
        self.Category = None
        self.VtsMin = None
        self.VtsMax = None
        self.CtsMin = None
        self.CtsMax = None
        self.Skip = None
        self.Limit = None
        self.Name = None
        self.Sort = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Ip = params.get("Ip")
        self.Count = params.get("Count")
        self.Category = params.get("Category")
        self.VtsMin = params.get("VtsMin")
        self.VtsMax = params.get("VtsMax")
        self.CtsMin = params.get("CtsMin")
        self.CtsMax = params.get("CtsMax")
        self.Skip = params.get("Skip")
        self.Limit = params.get("Limit")
        self.Name = params.get("Name")
        self.Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoDenyIPResponse(AbstractModel):
    """DescribeAutoDenyIP返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 查询IP封禁状态返回结果
        :type Data: :class:`tencentcloud.waf.v20180125.models.IpHitItemsData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = IpHitItemsData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeDomainWhiteRulesRequest(AbstractModel):
    """DescribeDomainWhiteRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 需要查询的域名
        :type Domain: str
        :param Url: 请求的白名单匹配路径
        :type Url: str
        :param Page: 翻到多少页
        :type Page: int
        :param Count: 每页展示的条数
        :type Count: int
        :param Sort: 排序方式
        :type Sort: str
        :param RuleId: 规则ID
        :type RuleId: str
        """
        self.Domain = None
        self.Url = None
        self.Page = None
        self.Count = None
        self.Sort = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.Page = params.get("Page")
        self.Count = params.get("Count")
        self.Sort = params.get("Sort")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainWhiteRulesResponse(AbstractModel):
    """DescribeDomainWhiteRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleList: 规则列表
        :type RuleList: list of RuleList
        :param Total: 规则的数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleList = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleList") is not None:
            self.RuleList = []
            for item in params.get("RuleList"):
                obj = RuleList()
                obj._deserialize(item)
                self.RuleList.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移
        :type Offset: int
        :param Limit: 容量
        :type Limit: int
        :param Filters: 过滤数组
        :type Filters: list of FiltersItemNew
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
                obj = FiltersItemNew()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainsResponse(AbstractModel):
    """DescribeDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
        :type Total: int
        :param Domains: domain列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Domains: list of DomainInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Domains = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = DomainInfo()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlowTrendRequest(AbstractModel):
    """DescribeFlowTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 需要获取流量趋势的域名, all表示所有域名
        :type Domain: str
        :param StartTs: 起始时间戳，精度秒
        :type StartTs: int
        :param EndTs: 结束时间戳，精度秒
        :type EndTs: int
        """
        self.Domain = None
        self.StartTs = None
        self.EndTs = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.StartTs = params.get("StartTs")
        self.EndTs = params.get("EndTs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowTrendResponse(AbstractModel):
    """DescribeFlowTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 流量趋势数据
        :type Data: list of BotStatPointItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = BotStatPointItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移
        :type Offset: int
        :param Limit: 容量
        :type Limit: int
        :param Filters: 过滤数组
        :type Filters: list of FiltersItemNew
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
                obj = FiltersItemNew()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
        :type Total: int
        :param Instances: instance列表
        :type Instances: list of InstanceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIpAccessControlRequest(AbstractModel):
    """DescribeIpAccessControl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param Count: 计数标识
        :type Count: int
        :param ActionType: 动作
        :type ActionType: int
        :param VtsMin: 有效时间最小时间戳
        :type VtsMin: int
        :param VtsMax: 有效时间最大时间戳
        :type VtsMax: int
        :param CtsMin: 创建时间最小时间戳
        :type CtsMin: int
        :param CtsMax: 创建时间最大时间戳
        :type CtsMax: int
        :param OffSet: 偏移
        :type OffSet: int
        :param Limit: 限制
        :type Limit: int
        :param Source: 来源
        :type Source: str
        :param Sort: 排序参数
        :type Sort: str
        :param Ip: ip
        :type Ip: str
        """
        self.Domain = None
        self.Count = None
        self.ActionType = None
        self.VtsMin = None
        self.VtsMax = None
        self.CtsMin = None
        self.CtsMax = None
        self.OffSet = None
        self.Limit = None
        self.Source = None
        self.Sort = None
        self.Ip = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Count = params.get("Count")
        self.ActionType = params.get("ActionType")
        self.VtsMin = params.get("VtsMin")
        self.VtsMax = params.get("VtsMax")
        self.CtsMin = params.get("CtsMin")
        self.CtsMax = params.get("CtsMax")
        self.OffSet = params.get("OffSet")
        self.Limit = params.get("Limit")
        self.Source = params.get("Source")
        self.Sort = params.get("Sort")
        self.Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpAccessControlResponse(AbstractModel):
    """DescribeIpAccessControl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 输出
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.waf.v20180125.models.IpAccessControlData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = IpAccessControlData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeIpHitItemsRequest(AbstractModel):
    """DescribeIpHitItems请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param Count: 计数标识
        :type Count: int
        :param Category: 类别
        :type Category: str
        :param VtsMin: 有效时间最小时间戳
        :type VtsMin: int
        :param VtsMax: 有效时间最大时间戳
        :type VtsMax: int
        :param CtsMin: 创建时间最小时间戳
        :type CtsMin: int
        :param CtsMax: 创建时间最大时间戳
        :type CtsMax: int
        :param Skip: 偏移参数
        :type Skip: int
        :param Limit: 限制数目
        :type Limit: int
        :param Name: 策略名称
        :type Name: str
        :param Sort: 排序参数
        :type Sort: str
        :param Ip: IP
        :type Ip: str
        """
        self.Domain = None
        self.Count = None
        self.Category = None
        self.VtsMin = None
        self.VtsMax = None
        self.CtsMin = None
        self.CtsMax = None
        self.Skip = None
        self.Limit = None
        self.Name = None
        self.Sort = None
        self.Ip = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Count = params.get("Count")
        self.Category = params.get("Category")
        self.VtsMin = params.get("VtsMin")
        self.VtsMax = params.get("VtsMax")
        self.CtsMin = params.get("CtsMin")
        self.CtsMax = params.get("CtsMax")
        self.Skip = params.get("Skip")
        self.Limit = params.get("Limit")
        self.Name = params.get("Name")
        self.Sort = params.get("Sort")
        self.Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpHitItemsResponse(AbstractModel):
    """DescribeIpHitItems返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.waf.v20180125.models.IpHitItemsData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = IpHitItemsData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeUserCdcClbWafRegionsRequest(AbstractModel):
    """DescribeUserCdcClbWafRegions请求参数结构体

    """


class DescribeUserCdcClbWafRegionsResponse(AbstractModel):
    """DescribeUserCdcClbWafRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: CdcRegion的类型描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CdcRegion
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CdcRegion()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserClbWafRegionsRequest(AbstractModel):
    """DescribeUserClbWafRegions请求参数结构体

    """


class DescribeUserClbWafRegionsResponse(AbstractModel):
    """DescribeUserClbWafRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 地域（标准的ap-格式）列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeWafAutoDenyRulesRequest(AbstractModel):
    """DescribeWafAutoDenyRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWafAutoDenyRulesResponse(AbstractModel):
    """DescribeWafAutoDenyRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param AttackThreshold: 攻击次数阈值
        :type AttackThreshold: int
        :param TimeThreshold: 攻击时间阈值
        :type TimeThreshold: int
        :param DenyTimeThreshold: 自动封禁时间
        :type DenyTimeThreshold: int
        :param DefenseStatus: 自动封禁状态
        :type DefenseStatus: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AttackThreshold = None
        self.TimeThreshold = None
        self.DenyTimeThreshold = None
        self.DefenseStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AttackThreshold = params.get("AttackThreshold")
        self.TimeThreshold = params.get("TimeThreshold")
        self.DenyTimeThreshold = params.get("DenyTimeThreshold")
        self.DefenseStatus = params.get("DefenseStatus")
        self.RequestId = params.get("RequestId")


class DescribeWafAutoDenyStatusRequest(AbstractModel):
    """DescribeWafAutoDenyStatus请求参数结构体

    """


class DescribeWafAutoDenyStatusResponse(AbstractModel):
    """DescribeWafAutoDenyStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param WafAutoDenyDetails: WAF 自动封禁详情
        :type WafAutoDenyDetails: :class:`tencentcloud.waf.v20180125.models.AutoDenyDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WafAutoDenyDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WafAutoDenyDetails") is not None:
            self.WafAutoDenyDetails = AutoDenyDetail()
            self.WafAutoDenyDetails._deserialize(params.get("WafAutoDenyDetails"))
        self.RequestId = params.get("RequestId")


class DescribeWafThreatenIntelligenceRequest(AbstractModel):
    """DescribeWafThreatenIntelligence请求参数结构体

    """


class DescribeWafThreatenIntelligenceResponse(AbstractModel):
    """DescribeWafThreatenIntelligence返回参数结构体

    """

    def __init__(self):
        r"""
        :param WafThreatenIntelligenceDetails: WAF 威胁情报封禁信息
        :type WafThreatenIntelligenceDetails: :class:`tencentcloud.waf.v20180125.models.WafThreatenIntelligenceDetails`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WafThreatenIntelligenceDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WafThreatenIntelligenceDetails") is not None:
            self.WafThreatenIntelligenceDetails = WafThreatenIntelligenceDetails()
            self.WafThreatenIntelligenceDetails._deserialize(params.get("WafThreatenIntelligenceDetails"))
        self.RequestId = params.get("RequestId")


class DomainInfo(AbstractModel):
    """域名的详细信息

    """


class DomainPackageNew(AbstractModel):
    """clb-waf 域名扩展套餐

    """

    def __init__(self):
        r"""
        :param ResourceIds: 资源ID
        :type ResourceIds: str
        :param ValidTime: 过期时间
        :type ValidTime: str
        :param RenewFlag: 是否自动续费，1：自动续费，0：不自动续费
        :type RenewFlag: int
        :param Count: 套餐购买个数
        :type Count: int
        :param Region: 套餐购买地域，clb-waf暂时没有用到
        :type Region: str
        """
        self.ResourceIds = None
        self.ValidTime = None
        self.RenewFlag = None
        self.Count = None
        self.Region = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.ValidTime = params.get("ValidTime")
        self.RenewFlag = params.get("RenewFlag")
        self.Count = params.get("Count")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadAttackRecordInfo(AbstractModel):
    """下载攻击日志记录数据项

    """

    def __init__(self):
        r"""
        :param Id: 记录ID
        :type Id: int
        :param TaskName: 下载任务名
        :type TaskName: str
        :param TaskId: 任务ID
        :type TaskId: str
        :param Host: 域名
        :type Host: str
        :param Count: 当前下载任务的日志条数
        :type Count: int
        :param Status: 下载任务运行状态：-1-下载超时，0-下载等待，1-下载完成，2-下载失败，4-正在下载
        :type Status: int
        :param Url: 下载文件URL
        :type Url: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 最后更新修改时间
        :type ModifyTime: str
        :param ExpireTime: 过期时间
        :type ExpireTime: str
        :param TotalCount: 下载任务需下载的日志总条数
        :type TotalCount: int
        """
        self.Id = None
        self.TaskName = None
        self.TaskId = None
        self.Host = None
        self.Count = None
        self.Status = None
        self.Url = None
        self.CreateTime = None
        self.ModifyTime = None
        self.ExpireTime = None
        self.TotalCount = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.TaskName = params.get("TaskName")
        self.TaskId = params.get("TaskId")
        self.Host = params.get("Host")
        self.Count = params.get("Count")
        self.Status = params.get("Status")
        self.Url = params.get("Url")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.ExpireTime = params.get("ExpireTime")
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportAccessInfo(AbstractModel):
    """DescribeAccessExports接口

    """

    def __init__(self):
        r"""
        :param ExportId: 日志导出任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ExportId: str
        :param Query: 日志导出查询语句
注意：此字段可能返回 null，表示取不到有效值。
        :type Query: str
        :param FileName: 日志导出文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param FileSize: 日志文件大小
        :type FileSize: int
        :param Order: 日志导出时间排序
注意：此字段可能返回 null，表示取不到有效值。
        :type Order: str
        :param Format: 日志导出格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Format: str
        :param Count: 日志导出数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param Status: 日志下载状态。Processing:导出正在进行中，Complete:导出完成，Failed:导出失败，Expired:日志导出已过期（三天有效期）
        :type Status: str
        :param From: 日志导出起始时间
        :type From: int
        :param To: 日志导出结束时间
        :type To: int
        :param CosPath: 日志导出路径
        :type CosPath: str
        :param CreateTime: 日志导出创建时间
        :type CreateTime: str
        """
        self.ExportId = None
        self.Query = None
        self.FileName = None
        self.FileSize = None
        self.Order = None
        self.Format = None
        self.Count = None
        self.Status = None
        self.From = None
        self.To = None
        self.CosPath = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ExportId = params.get("ExportId")
        self.Query = params.get("Query")
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.Order = params.get("Order")
        self.Format = params.get("Format")
        self.Count = params.get("Count")
        self.Status = params.get("Status")
        self.From = params.get("From")
        self.To = params.get("To")
        self.CosPath = params.get("CosPath")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FiltersItemNew(AbstractModel):
    """实例入参过滤器

    """

    def __init__(self):
        r"""
        :param Name: 字段名
        :type Name: str
        :param Values: 过滤值
        :type Values: list of str
        :param ExactMatch: 是否精确查找
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
        


class FraudPkg(AbstractModel):
    """业务安全资源信息

    """

    def __init__(self):
        r"""
        :param ResourceIds: 资源id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: int
        :param BeginTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: str
        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param InquireNum: 申请数量
注意：此字段可能返回 null，表示取不到有效值。
        :type InquireNum: int
        :param UsedNum: 使用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedNum: int
        """
        self.ResourceIds = None
        self.Status = None
        self.Region = None
        self.BeginTime = None
        self.EndTime = None
        self.InquireNum = None
        self.UsedNum = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.Status = params.get("Status")
        self.Region = params.get("Region")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.InquireNum = params.get("InquireNum")
        self.UsedNum = params.get("UsedNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAttackDownloadRecordsRequest(AbstractModel):
    """GetAttackDownloadRecords请求参数结构体

    """


class GetAttackDownloadRecordsResponse(AbstractModel):
    """GetAttackDownloadRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param Records: 下载攻击日志记录数组
        :type Records: list of DownloadAttackRecordInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Records = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = DownloadAttackRecordInfo()
                obj._deserialize(item)
                self.Records.append(obj)
        self.RequestId = params.get("RequestId")


class InstanceInfo(AbstractModel):
    """一个实例的详细信息

    """

    def __init__(self):
        r"""
        :param InstanceId: id
        :type InstanceId: str
        :param InstanceName: name
        :type InstanceName: str
        :param ResourceIds: 资源id
        :type ResourceIds: str
        :param Region: 地域
        :type Region: str
        :param PayMode: 付费模式
        :type PayMode: int
        :param RenewFlag: 自动续费
        :type RenewFlag: int
        :param Mode: 弹性计费
        :type Mode: int
        :param Level: 套餐版本
        :type Level: int
        :param ValidTime: 过期时间
        :type ValidTime: str
        :param BeginTime: 开始时间
        :type BeginTime: str
        :param DomainCount: 已用
        :type DomainCount: int
        :param SubDomainLimit: 上限
        :type SubDomainLimit: int
        :param MainDomainCount: 已用
        :type MainDomainCount: int
        :param MainDomainLimit: 上限
        :type MainDomainLimit: int
        :param MaxQPS: 峰值
        :type MaxQPS: int
        :param QPS: qps套餐
        :type QPS: :class:`tencentcloud.waf.v20180125.models.QPSPackageNew`
        :param DomainPkg: 域名套餐
        :type DomainPkg: :class:`tencentcloud.waf.v20180125.models.DomainPackageNew`
        :param AppId: 用户appid
        :type AppId: int
        :param Edition: clb或saas
        :type Edition: str
        :param FraudPkg: 业务安全包
注意：此字段可能返回 null，表示取不到有效值。
        :type FraudPkg: :class:`tencentcloud.waf.v20180125.models.FraudPkg`
        :param BotPkg: Bot资源包
注意：此字段可能返回 null，表示取不到有效值。
        :type BotPkg: :class:`tencentcloud.waf.v20180125.models.BotPkg`
        :param BotQPS: bot的qps详情
注意：此字段可能返回 null，表示取不到有效值。
        :type BotQPS: :class:`tencentcloud.waf.v20180125.models.BotQPS`
        """
        self.InstanceId = None
        self.InstanceName = None
        self.ResourceIds = None
        self.Region = None
        self.PayMode = None
        self.RenewFlag = None
        self.Mode = None
        self.Level = None
        self.ValidTime = None
        self.BeginTime = None
        self.DomainCount = None
        self.SubDomainLimit = None
        self.MainDomainCount = None
        self.MainDomainLimit = None
        self.MaxQPS = None
        self.QPS = None
        self.DomainPkg = None
        self.AppId = None
        self.Edition = None
        self.FraudPkg = None
        self.BotPkg = None
        self.BotQPS = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ResourceIds = params.get("ResourceIds")
        self.Region = params.get("Region")
        self.PayMode = params.get("PayMode")
        self.RenewFlag = params.get("RenewFlag")
        self.Mode = params.get("Mode")
        self.Level = params.get("Level")
        self.ValidTime = params.get("ValidTime")
        self.BeginTime = params.get("BeginTime")
        self.DomainCount = params.get("DomainCount")
        self.SubDomainLimit = params.get("SubDomainLimit")
        self.MainDomainCount = params.get("MainDomainCount")
        self.MainDomainLimit = params.get("MainDomainLimit")
        self.MaxQPS = params.get("MaxQPS")
        if params.get("QPS") is not None:
            self.QPS = QPSPackageNew()
            self.QPS._deserialize(params.get("QPS"))
        if params.get("DomainPkg") is not None:
            self.DomainPkg = DomainPackageNew()
            self.DomainPkg._deserialize(params.get("DomainPkg"))
        self.AppId = params.get("AppId")
        self.Edition = params.get("Edition")
        if params.get("FraudPkg") is not None:
            self.FraudPkg = FraudPkg()
            self.FraudPkg._deserialize(params.get("FraudPkg"))
        if params.get("BotPkg") is not None:
            self.BotPkg = BotPkg()
            self.BotPkg._deserialize(params.get("BotPkg"))
        if params.get("BotQPS") is not None:
            self.BotQPS = BotQPS()
            self.BotQPS._deserialize(params.get("BotQPS"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpAccessControlData(AbstractModel):
    """数据封装

    """

    def __init__(self):
        r"""
        :param Res: ip黑白名单
注意：此字段可能返回 null，表示取不到有效值。
        :type Res: list of IpAccessControlItem
        :param TotalCount: 计数
        :type TotalCount: int
        """
        self.Res = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("Res") is not None:
            self.Res = []
            for item in params.get("Res"):
                obj = IpAccessControlItem()
                obj._deserialize(item)
                self.Res.append(obj)
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpAccessControlItem(AbstractModel):
    """ip黑白名单

    """

    def __init__(self):
        r"""
        :param ActionType: 动作
        :type ActionType: int
        :param Ip: ip
        :type Ip: str
        :param Note: 备注
        :type Note: str
        :param Source: 来源
        :type Source: str
        :param TsVersion: 更新时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type TsVersion: int
        :param ValidTs: 有效截止时间戳
        :type ValidTs: int
        """
        self.ActionType = None
        self.Ip = None
        self.Note = None
        self.Source = None
        self.TsVersion = None
        self.ValidTs = None


    def _deserialize(self, params):
        self.ActionType = params.get("ActionType")
        self.Ip = params.get("Ip")
        self.Note = params.get("Note")
        self.Source = params.get("Source")
        self.TsVersion = params.get("TsVersion")
        self.ValidTs = params.get("ValidTs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpHitItem(AbstractModel):
    """ip封堵状态数据

    """

    def __init__(self):
        r"""
        :param Action: 动作
        :type Action: int
        :param Category: 类别
        :type Category: str
        :param Ip: ip
        :type Ip: str
        :param Name: 规则名称
        :type Name: str
        :param TsVersion: 时间戳
        :type TsVersion: int
        :param ValidTs: 有效截止时间戳
        :type ValidTs: int
        """
        self.Action = None
        self.Category = None
        self.Ip = None
        self.Name = None
        self.TsVersion = None
        self.ValidTs = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Category = params.get("Category")
        self.Ip = params.get("Ip")
        self.Name = params.get("Name")
        self.TsVersion = params.get("TsVersion")
        self.ValidTs = params.get("ValidTs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpHitItemsData(AbstractModel):
    """封装参数

    """

    def __init__(self):
        r"""
        :param Res: 数组封装
        :type Res: list of IpHitItem
        :param TotalCount: 总数目
        :type TotalCount: int
        """
        self.Res = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("Res") is not None:
            self.Res = []
            for item in params.get("Res"):
                obj = IpHitItem()
                obj._deserialize(item)
                self.Res.append(obj)
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessPeriodRequest(AbstractModel):
    """ModifyAccessPeriod请求参数结构体

    """

    def __init__(self):
        r"""
        :param Period: 访问日志保存期限，范围为[1, 30]
        :type Period: int
        :param TopicId: 日志主题
        :type TopicId: str
        """
        self.Period = None
        self.TopicId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessPeriodResponse(AbstractModel):
    """ModifyAccessPeriod返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCustomRuleStatusRequest(AbstractModel):
    """ModifyCustomRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param RuleId: 规则ID
        :type RuleId: int
        :param Status: 开关的状态，1是开启、0是关闭
        :type Status: int
        :param Edition: WAF的版本，clb-waf代表负载均衡WAF、sparta-waf代表SaaS WAF，默认是sparta-waf。
        :type Edition: str
        """
        self.Domain = None
        self.RuleId = None
        self.Status = None
        self.Edition = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RuleId = params.get("RuleId")
        self.Status = params.get("Status")
        self.Edition = params.get("Edition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomRuleStatusResponse(AbstractModel):
    """ModifyCustomRuleStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Success: 操作的状态码，如果所有的资源操作成功则返回的是成功的状态码，如果有资源操作失败则需要解析Message的内容来查看哪个资源失败
        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = ResponseCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDomainWhiteRuleRequest(AbstractModel):
    """ModifyDomainWhiteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 需要更改的规则的域名
        :type Domain: str
        :param Id: 白名单id
        :type Id: int
        :param Rules: 规则的id列表
        :type Rules: list of int non-negative
        :param Url: 规则匹配路径
        :type Url: str
        :param Function: 规则匹配方法
        :type Function: str
        :param Status: 规则的开关状态
        :type Status: int
        """
        self.Domain = None
        self.Id = None
        self.Rules = None
        self.Url = None
        self.Function = None
        self.Status = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Id = params.get("Id")
        self.Rules = params.get("Rules")
        self.Url = params.get("Url")
        self.Function = params.get("Function")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainWhiteRuleResponse(AbstractModel):
    """ModifyDomainWhiteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWafAutoDenyRulesRequest(AbstractModel):
    """ModifyWafAutoDenyRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param AttackThreshold: 攻击次数阈值
        :type AttackThreshold: int
        :param TimeThreshold: 攻击时间阈值
        :type TimeThreshold: int
        :param DenyTimeThreshold: 自动封禁时间
        :type DenyTimeThreshold: int
        :param DefenseStatus: 自动封禁状态
        :type DefenseStatus: int
        """
        self.Domain = None
        self.AttackThreshold = None
        self.TimeThreshold = None
        self.DenyTimeThreshold = None
        self.DefenseStatus = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.AttackThreshold = params.get("AttackThreshold")
        self.TimeThreshold = params.get("TimeThreshold")
        self.DenyTimeThreshold = params.get("DenyTimeThreshold")
        self.DefenseStatus = params.get("DefenseStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWafAutoDenyRulesResponse(AbstractModel):
    """ModifyWafAutoDenyRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param Success: 成功的状态码，需要JSON解码后再使用，返回的格式是{"域名":"状态"}，成功的状态码为Success，其它的为失败的状态码（yunapi定义的错误码）
        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = ResponseCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyWafAutoDenyStatusRequest(AbstractModel):
    """ModifyWafAutoDenyStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param WafAutoDenyDetails: WAF 自动封禁配置项
        :type WafAutoDenyDetails: :class:`tencentcloud.waf.v20180125.models.AutoDenyDetail`
        """
        self.WafAutoDenyDetails = None


    def _deserialize(self, params):
        if params.get("WafAutoDenyDetails") is not None:
            self.WafAutoDenyDetails = AutoDenyDetail()
            self.WafAutoDenyDetails._deserialize(params.get("WafAutoDenyDetails"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWafAutoDenyStatusResponse(AbstractModel):
    """ModifyWafAutoDenyStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param WafAutoDenyDetails: WAF 自动封禁配置项
        :type WafAutoDenyDetails: :class:`tencentcloud.waf.v20180125.models.AutoDenyDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WafAutoDenyDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WafAutoDenyDetails") is not None:
            self.WafAutoDenyDetails = AutoDenyDetail()
            self.WafAutoDenyDetails._deserialize(params.get("WafAutoDenyDetails"))
        self.RequestId = params.get("RequestId")


class ModifyWafThreatenIntelligenceRequest(AbstractModel):
    """ModifyWafThreatenIntelligence请求参数结构体

    """

    def __init__(self):
        r"""
        :param WafThreatenIntelligenceDetails: 配置WAF威胁情报封禁模块详情
        :type WafThreatenIntelligenceDetails: :class:`tencentcloud.waf.v20180125.models.WafThreatenIntelligenceDetails`
        """
        self.WafThreatenIntelligenceDetails = None


    def _deserialize(self, params):
        if params.get("WafThreatenIntelligenceDetails") is not None:
            self.WafThreatenIntelligenceDetails = WafThreatenIntelligenceDetails()
            self.WafThreatenIntelligenceDetails._deserialize(params.get("WafThreatenIntelligenceDetails"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWafThreatenIntelligenceResponse(AbstractModel):
    """ModifyWafThreatenIntelligence返回参数结构体

    """

    def __init__(self):
        r"""
        :param WafThreatenIntelligenceDetails: 当前WAF威胁情报封禁模块详情
        :type WafThreatenIntelligenceDetails: :class:`tencentcloud.waf.v20180125.models.WafThreatenIntelligenceDetails`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WafThreatenIntelligenceDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WafThreatenIntelligenceDetails") is not None:
            self.WafThreatenIntelligenceDetails = WafThreatenIntelligenceDetails()
            self.WafThreatenIntelligenceDetails._deserialize(params.get("WafThreatenIntelligenceDetails"))
        self.RequestId = params.get("RequestId")


class PortItem(AbstractModel):
    """防护域名端口配置信息

    """

    def __init__(self):
        r"""
        :param Port: 监听端口配置
        :type Port: str
        :param Protocol: 与Port一一对应，表示端口对应的协议
        :type Protocol: str
        :param UpstreamPort: 与Port一一对应,  表示回源端口
        :type UpstreamPort: str
        :param UpstreamProtocol: 与Port一一对应,  表示回源协议
        :type UpstreamProtocol: str
        :param NginxServerId: Nginx的服务器ID
        :type NginxServerId: str
        """
        self.Port = None
        self.Protocol = None
        self.UpstreamPort = None
        self.UpstreamProtocol = None
        self.NginxServerId = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.Protocol = params.get("Protocol")
        self.UpstreamPort = params.get("UpstreamPort")
        self.UpstreamProtocol = params.get("UpstreamProtocol")
        self.NginxServerId = params.get("NginxServerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostAttackDownloadTaskRequest(AbstractModel):
    """PostAttackDownloadTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 查询的域名，所有域名使用all
        :type Domain: str
        :param StartTime: 查询起始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        :param QueryString: Lucene语法
        :type QueryString: str
        :param TaskName: 任务名称
        :type TaskName: str
        :param Sort: 默认为desc，可以取值desc和asc
        :type Sort: str
        """
        self.Domain = None
        self.StartTime = None
        self.EndTime = None
        self.QueryString = None
        self.TaskName = None
        self.Sort = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.QueryString = params.get("QueryString")
        self.TaskName = params.get("TaskName")
        self.Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostAttackDownloadTaskResponse(AbstractModel):
    """PostAttackDownloadTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Flow: 任务task id
        :type Flow: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Flow = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Flow = params.get("Flow")
        self.RequestId = params.get("RequestId")


class QPSPackageNew(AbstractModel):
    """clb-waf QPS套餐 New

    """

    def __init__(self):
        r"""
        :param ResourceIds: 资源ID
        :type ResourceIds: str
        :param ValidTime: 过期时间
        :type ValidTime: str
        :param RenewFlag: 是否自动续费，1：自动续费，0：不自动续费
        :type RenewFlag: int
        :param Count: 套餐购买个数
        :type Count: int
        :param Region: 套餐购买地域，clb-waf暂时没有用到
        :type Region: str
        """
        self.ResourceIds = None
        self.ValidTime = None
        self.RenewFlag = None
        self.Count = None
        self.Region = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.ValidTime = params.get("ValidTime")
        self.RenewFlag = params.get("RenewFlag")
        self.Count = params.get("Count")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseCode(AbstractModel):
    """响应体的返回码

    """

    def __init__(self):
        r"""
        :param Code: 如果成功则返回Success，失败则返回yunapi定义的错误码
        :type Code: str
        :param Message: 如果成功则返回Success，失败则返回WAF定义的二级错误码
        :type Message: str
        """
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleList(AbstractModel):
    """规则白名单

    """

    def __init__(self):
        r"""
        :param Id: 规则Id
        :type Id: int
        :param Rules: 规则列表的id
        :type Rules: list of int non-negative
        :param Url: 请求url
        :type Url: str
        :param Function: 请求的方法
        :type Function: str
        :param Time: 时间戳
        :type Time: str
        :param Status: 开关状态
        :type Status: int
        """
        self.Id = None
        self.Rules = None
        self.Url = None
        self.Function = None
        self.Time = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Rules = params.get("Rules")
        self.Url = params.get("Url")
        self.Function = params.get("Function")
        self.Time = params.get("Time")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchAccessLogRequest(AbstractModel):
    """SearchAccessLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param TopicId: 客户要查询的日志主题ID，每个客户都有对应的一个主题
        :type TopicId: str
        :param From: 要查询的日志的起始时间，Unix时间戳，单位ms
        :type From: int
        :param To: 要查询的日志的结束时间，Unix时间戳，单位ms
        :type To: int
        :param Query: 查询语句，语句长度最大为4096
        :type Query: str
        :param Limit: 单次查询返回的日志条数，最大值为100
        :type Limit: int
        :param Context: 加载更多日志时使用，透传上次返回的Context值，获取后续的日志内容
        :type Context: str
        :param Sort: 日志接口是否按时间排序返回；可选值：asc(升序)、desc(降序)，默认为 desc
        :type Sort: str
        """
        self.TopicId = None
        self.From = None
        self.To = None
        self.Query = None
        self.Limit = None
        self.Context = None
        self.Sort = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.From = params.get("From")
        self.To = params.get("To")
        self.Query = params.get("Query")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")
        self.Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchAccessLogResponse(AbstractModel):
    """SearchAccessLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param Context: 加载后续内容的Context
        :type Context: str
        :param ListOver: 日志查询结果是否全部返回
        :type ListOver: bool
        :param Analysis: 返回的是否为分析结果
        :type Analysis: bool
        :param ColNames: 如果Analysis为True，则返回分析结果的列名，否则为空
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ColNames: list of str
        :param Results: 日志查询结果；当Analysis为True时，可能返回为null
注意：此字段可能返回 null，表示取不到有效值
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of AccessLogInfo
        :param AnalysisResults: 日志分析结果；当Analysis为False时，可能返回为null
注意：此字段可能返回 null，表示取不到有效值
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisResults: list of AccessLogItems
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Context = None
        self.ListOver = None
        self.Analysis = None
        self.ColNames = None
        self.Results = None
        self.AnalysisResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.ListOver = params.get("ListOver")
        self.Analysis = params.get("Analysis")
        self.ColNames = params.get("ColNames")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = AccessLogInfo()
                obj._deserialize(item)
                self.Results.append(obj)
        if params.get("AnalysisResults") is not None:
            self.AnalysisResults = []
            for item in params.get("AnalysisResults"):
                obj = AccessLogItems()
                obj._deserialize(item)
                self.AnalysisResults.append(obj)
        self.RequestId = params.get("RequestId")


class Strategy(AbstractModel):
    """自定义规则的匹配条件结构体

    """

    def __init__(self):
        r"""
        :param Field: 匹配字段
        :type Field: str
        :param CompareFunc: 逻辑符号
        :type CompareFunc: str
        :param Content: 匹配内容
        :type Content: str
        :param Arg: 匹配参数
        :type Arg: str
        """
        self.Field = None
        self.CompareFunc = None
        self.Content = None
        self.Arg = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.CompareFunc = params.get("CompareFunc")
        self.Content = params.get("Content")
        self.Arg = params.get("Arg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpsertIpAccessControlRequest(AbstractModel):
    """UpsertIpAccessControl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param Items: ip 参数列表，json数组由ip，source，note，action，valid_ts组成。ip对应配置的ip地址，source固定为custom值，note为注释，action值42为黑名单，40为白名单，valid_ts为有效日期，值为秒级时间戳
        :type Items: list of str
        :param Edition: clb-waf或者sparta-waf
        :type Edition: str
        """
        self.Domain = None
        self.Items = None
        self.Edition = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Items = params.get("Items")
        self.Edition = params.get("Edition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpsertIpAccessControlResponse(AbstractModel):
    """UpsertIpAccessControl返回参数结构体

    """

    def __init__(self):
        r"""
        :param FailedItems: 添加或修改失败的条目
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedItems: str
        :param FailedCount: 添加或修改失败的数目
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FailedItems = None
        self.FailedCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailedItems = params.get("FailedItems")
        self.FailedCount = params.get("FailedCount")
        self.RequestId = params.get("RequestId")


class WafThreatenIntelligenceDetails(AbstractModel):
    """Waf 威胁情报封禁模块配置详情

    """

    def __init__(self):
        r"""
        :param DefenseStatus: 封禁模组启用状态
        :type DefenseStatus: int
        :param Tags: 封禁属性标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param LastUpdateTime: 最后更新时间
        :type LastUpdateTime: str
        """
        self.DefenseStatus = None
        self.Tags = None
        self.LastUpdateTime = None


    def _deserialize(self, params):
        self.DefenseStatus = params.get("DefenseStatus")
        self.Tags = params.get("Tags")
        self.LastUpdateTime = params.get("LastUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        