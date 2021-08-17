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
        :param Count: 日志导出数量
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


class CreateAttackDownloadTaskRequest(AbstractModel):
    """CreateAttackDownloadTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名，所有域名填写all
        :type Domain: str
        :param FromTime: 查询起始时间
        :type FromTime: str
        :param ToTime: 查询结束时间
        :type ToTime: str
        :param Name: 下载任务名字
        :type Name: str
        :param RiskLevel: 风险等级
        :type RiskLevel: int
        :param Status: 拦截状态
        :type Status: int
        :param RuleId: 自定义策略ID
        :type RuleId: int
        :param AttackIp: 攻击者IP
        :type AttackIp: str
        :param AttackType: 攻击类型
        :type AttackType: str
        """
        self.Domain = None
        self.FromTime = None
        self.ToTime = None
        self.Name = None
        self.RiskLevel = None
        self.Status = None
        self.RuleId = None
        self.AttackIp = None
        self.AttackType = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.FromTime = params.get("FromTime")
        self.ToTime = params.get("ToTime")
        self.Name = params.get("Name")
        self.RiskLevel = params.get("RiskLevel")
        self.Status = params.get("Status")
        self.RuleId = params.get("RuleId")
        self.AttackIp = params.get("AttackIp")
        self.AttackType = params.get("AttackType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAttackDownloadTaskResponse(AbstractModel):
    """CreateAttackDownloadTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Flow: 任务ID
        :type Flow: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Flow = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Flow = params.get("Flow")
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


class DescribeCustomRulesPagingInfo(AbstractModel):
    """DescribeCustomRules接口的翻页参数

    """

    def __init__(self):
        r"""
        :param Offset: 当前页码
        :type Offset: int
        :param Limit: 当前页的最大数据条数
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
        


class DescribeCustomRulesRequest(AbstractModel):
    """DescribeCustomRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param Paging: 分页参数
        :type Paging: :class:`tencentcloud.waf.v20180125.models.DescribeCustomRulesPagingInfo`
        :param Edition: clb-waf或者sparta-waf
        :type Edition: str
        :param ActionType: 过滤参数：动作类型：0放行，1阻断，2人机识别，3观察，4重定向
        :type ActionType: str
        :param Search: 过滤参数：规则名称过滤条件
        :type Search: str
        """
        self.Domain = None
        self.Paging = None
        self.Edition = None
        self.ActionType = None
        self.Search = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("Paging") is not None:
            self.Paging = DescribeCustomRulesPagingInfo()
            self.Paging._deserialize(params.get("Paging"))
        self.Edition = params.get("Edition")
        self.ActionType = params.get("ActionType")
        self.Search = params.get("Search")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomRulesResponse(AbstractModel):
    """DescribeCustomRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleList: 规则详情
        :type RuleList: list of DescribeCustomRulesRspRuleListItem
        :param TotalCount: 规则条数
        :type TotalCount: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleList") is not None:
            self.RuleList = []
            for item in params.get("RuleList"):
                obj = DescribeCustomRulesRspRuleListItem()
                obj._deserialize(item)
                self.RuleList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCustomRulesRspRuleListItem(AbstractModel):
    """DescribeCustomRules接口回包中的复杂类型

    """

    def __init__(self):
        r"""
        :param ActionType: 动作类型
        :type ActionType: str
        :param Bypass: 跳过的策略
        :type Bypass: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ExpireTime: 过期时间
        :type ExpireTime: str
        :param Name: 策略名称
        :type Name: str
        :param Redirect: 重定向地址
        :type Redirect: str
        :param RuleId: 策略ID
        :type RuleId: str
        :param SortId: 优先级
        :type SortId: str
        :param Status: 状态
        :type Status: str
        :param Strategies: 策略详情
        :type Strategies: list of Strategy
        """
        self.ActionType = None
        self.Bypass = None
        self.CreateTime = None
        self.ExpireTime = None
        self.Name = None
        self.Redirect = None
        self.RuleId = None
        self.SortId = None
        self.Status = None
        self.Strategies = None


    def _deserialize(self, params):
        self.ActionType = params.get("ActionType")
        self.Bypass = params.get("Bypass")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.Name = params.get("Name")
        self.Redirect = params.get("Redirect")
        self.RuleId = params.get("RuleId")
        self.SortId = params.get("SortId")
        self.Status = params.get("Status")
        if params.get("Strategies") is not None:
            self.Strategies = []
            for item in params.get("Strategies"):
                obj = Strategy()
                obj._deserialize(item)
                self.Strategies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        