# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class AddCustomRuleRequest(AbstractModel):
    """AddCustomRule请求参数结构体

    """

    def __init__(self):
        """
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


class AddCustomRuleResponse(AbstractModel):
    """AddCustomRule返回参数结构体

    """

    def __init__(self):
        """
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


class CreateAttackDownloadTaskRequest(AbstractModel):
    """CreateAttackDownloadTask请求参数结构体

    """

    def __init__(self):
        """
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


class CreateAttackDownloadTaskResponse(AbstractModel):
    """CreateAttackDownloadTask返回参数结构体

    """

    def __init__(self):
        """
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


class DeleteAttackDownloadRecordRequest(AbstractModel):
    """DeleteAttackDownloadRecord请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 下载任务记录唯一标记
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class DeleteAttackDownloadRecordResponse(AbstractModel):
    """DeleteAttackDownloadRecord返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param Flow: 记录id
        :type Flow: str
        """
        self.Flow = None


    def _deserialize(self, params):
        self.Flow = params.get("Flow")


class DeleteDownloadRecordResponse(AbstractModel):
    """DeleteDownloadRecord返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DeleteSessionResponse(AbstractModel):
    """DeleteSession返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeCustomRulesPagingInfo(AbstractModel):
    """DescribeCustomRules接口的翻页参数

    """

    def __init__(self):
        """
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


class DescribeCustomRulesRequest(AbstractModel):
    """DescribeCustomRules请求参数结构体

    """

    def __init__(self):
        """
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


class DescribeCustomRulesResponse(AbstractModel):
    """DescribeCustomRules返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DescribeUserClbWafRegionsRequest(AbstractModel):
    """DescribeUserClbWafRegions请求参数结构体

    """


class DescribeUserClbWafRegionsResponse(AbstractModel):
    """DescribeUserClbWafRegions返回参数结构体

    """

    def __init__(self):
        """
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


class ModifyCustomRuleStatusRequest(AbstractModel):
    """ModifyCustomRuleStatus请求参数结构体

    """

    def __init__(self):
        """
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


class ModifyCustomRuleStatusResponse(AbstractModel):
    """ModifyCustomRuleStatus返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class Strategy(AbstractModel):
    """自定义规则的匹配条件结构体

    """

    def __init__(self):
        """
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