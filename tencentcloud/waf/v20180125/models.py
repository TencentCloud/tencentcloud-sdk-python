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


class AddCustomRuleRequest(AbstractModel):
    """AddCustomRule请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 规则名称\n        :type Name: str\n        :param SortId: 优先级\n        :type SortId: str\n        :param ExpireTime: 过期时间\n        :type ExpireTime: str\n        :param Strategies: 策略详情\n        :type Strategies: list of Strategy\n        :param Domain: 需要添加策略的域名\n        :type Domain: str\n        :param ActionType: 动作类型\n        :type ActionType: str\n        :param Redirect: 如果动作是重定向，则表示重定向的地址；其他情况可以为空\n        :type Redirect: str\n        :param Edition: "clb-waf"或者"sparta-waf"\n        :type Edition: str\n        :param Bypass: 放行的详情\n        :type Bypass: str\n        """
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
        """
        :param Success: 操作的状态码，如果所有的资源操作成功则返回的是成功的状态码，如果有资源操作失败则需要解析Message的内容来查看哪个资源失败\n        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`\n        :param RuleId: 添加成功的规则ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param TimeStamp: 横坐标\n        :type TimeStamp: str\n        :param Key: value的所属对象\n        :type Key: str\n        :param Value: 纵列表\n        :type Value: int\n        :param Label: Key对应的页面展示内容\n        :type Label: str\n        """
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
        


class CreateAttackDownloadTaskRequest(AbstractModel):
    """CreateAttackDownloadTask请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名，所有域名填写all\n        :type Domain: str\n        :param FromTime: 查询起始时间\n        :type FromTime: str\n        :param ToTime: 查询结束时间\n        :type ToTime: str\n        :param Name: 下载任务名字\n        :type Name: str\n        :param RiskLevel: 风险等级\n        :type RiskLevel: int\n        :param Status: 拦截状态\n        :type Status: int\n        :param RuleId: 自定义策略ID\n        :type RuleId: int\n        :param AttackIp: 攻击者IP\n        :type AttackIp: str\n        :param AttackType: 攻击类型\n        :type AttackType: str\n        """
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
        """
        :param Flow: 任务ID\n        :type Flow: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Flow = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Flow = params.get("Flow")
        self.RequestId = params.get("RequestId")


class DeleteAttackDownloadRecordRequest(AbstractModel):
    """DeleteAttackDownloadRecord请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 下载任务记录唯一标记\n        :type Id: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDownloadRecordRequest(AbstractModel):
    """DeleteDownloadRecord请求参数结构体

    """

    def __init__(self):
        """
        :param Flow: 记录id\n        :type Flow: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSessionRequest(AbstractModel):
    """DeleteSession请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param Edition: clb-waf 或者 sprta-waf\n        :type Edition: str\n        """
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
        """
        :param Data: 结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeCustomRulesPagingInfo(AbstractModel):
    """DescribeCustomRules接口的翻页参数

    """

    def __init__(self):
        """
        :param Offset: 当前页码\n        :type Offset: int\n        :param Limit: 当前页的最大数据条数\n        :type Limit: int\n        """
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
        """
        :param Domain: 域名\n        :type Domain: str\n        :param Paging: 分页参数\n        :type Paging: :class:`tencentcloud.waf.v20180125.models.DescribeCustomRulesPagingInfo`\n        :param Edition: clb-waf或者sparta-waf\n        :type Edition: str\n        :param ActionType: 过滤参数：动作类型：0放行，1阻断，2人机识别，3观察，4重定向\n        :type ActionType: str\n        :param Search: 过滤参数：规则名称过滤条件\n        :type Search: str\n        """
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
        """
        :param RuleList: 规则详情\n        :type RuleList: list of DescribeCustomRulesRspRuleListItem\n        :param TotalCount: 规则条数\n        :type TotalCount: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ActionType: 动作类型\n        :type ActionType: str\n        :param Bypass: 跳过的策略\n        :type Bypass: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param ExpireTime: 过期时间\n        :type ExpireTime: str\n        :param Name: 策略名称\n        :type Name: str\n        :param Redirect: 重定向地址\n        :type Redirect: str\n        :param RuleId: 策略ID\n        :type RuleId: str\n        :param SortId: 优先级\n        :type SortId: str\n        :param Status: 状态\n        :type Status: str\n        :param Strategies: 策略详情\n        :type Strategies: list of Strategy\n        """
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
        """
        :param Domain: 需要获取流量趋势的域名, all表示所有域名\n        :type Domain: str\n        :param StartTs: 起始时间戳，精度秒\n        :type StartTs: int\n        :param EndTs: 结束时间戳，精度秒\n        :type EndTs: int\n        """
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
        """
        :param Data: 流量趋势数据\n        :type Data: list of BotStatPointItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Data: 地域（标准的ap-格式）列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class ModifyAccessPeriodRequest(AbstractModel):
    """ModifyAccessPeriod请求参数结构体

    """

    def __init__(self):
        """
        :param Period: 访问日志保存期限，范围为[1, 30]\n        :type Period: int\n        :param TopicId: 日志主题\n        :type TopicId: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCustomRuleStatusRequest(AbstractModel):
    """ModifyCustomRuleStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param RuleId: 规则ID\n        :type RuleId: int\n        :param Status: 开关的状态，1是开启、0是关闭\n        :type Status: int\n        :param Edition: WAF的版本，clb-waf代表负载均衡WAF、sparta-waf代表SaaS WAF，默认是sparta-waf。\n        :type Edition: str\n        """
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
        """
        :param Success: 操作的状态码，如果所有的资源操作成功则返回的是成功的状态码，如果有资源操作失败则需要解析Message的内容来查看哪个资源失败\n        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Code: 如果成功则返回Success，失败则返回yunapi定义的错误码\n        :type Code: str\n        :param Message: 如果成功则返回Success，失败则返回WAF定义的二级错误码\n        :type Message: str\n        """
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
        


class Strategy(AbstractModel):
    """自定义规则的匹配条件结构体

    """

    def __init__(self):
        """
        :param Field: 匹配字段\n        :type Field: str\n        :param CompareFunc: 逻辑符号\n        :type CompareFunc: str\n        :param Content: 匹配内容\n        :type Content: str\n        :param Arg: 匹配参数\n        :type Arg: str\n        """
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
        