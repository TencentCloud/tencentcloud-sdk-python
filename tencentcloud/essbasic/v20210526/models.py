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


class Agent(AbstractModel):
    """应用相关信息

    """

    def __init__(self):
        r"""
        :param AppId: 腾讯电子签颁发给渠道的应用ID，32位字符串
        :type AppId: str
        :param ProxyOrganizationId: 腾讯电子签颁发给渠道侧合作企业的企业ID
        :type ProxyOrganizationId: str
        :param ProxyAppId: 腾讯电子签颁发给渠道侧合作企业的应用ID
        :type ProxyAppId: str
        :param ProxyOperator: 渠道/平台合作企业经办人（操作员）
        :type ProxyOperator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param ProxyOrganizationOpenId: 渠道/平台合作企业的企业ID
        :type ProxyOrganizationOpenId: str
        """
        self.AppId = None
        self.ProxyOrganizationId = None
        self.ProxyAppId = None
        self.ProxyOperator = None
        self.ProxyOrganizationOpenId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.ProxyOrganizationId = params.get("ProxyOrganizationId")
        self.ProxyAppId = params.get("ProxyAppId")
        if params.get("ProxyOperator") is not None:
            self.ProxyOperator = UserInfo()
            self.ProxyOperator._deserialize(params.get("ProxyOperator"))
        self.ProxyOrganizationOpenId = params.get("ProxyOrganizationOpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Component(AbstractModel):
    """此结构体 (Component) 用于描述控件属性。

    """

    def __init__(self):
        r"""
        :param ComponentId: 控件编号

注：
当GenerateMode=3时，通过"^"来决定是否使用关键字整词匹配能力。
例：
当GenerateMode=3时，如果传入关键字"^甲方签署^"，则会在PDF文件中有且仅有"甲方签署"关键字的地方进行对应操作。
如传入的关键字为"甲方签署"，则PDF文件中每个出现关键字的位置都会执行相应操作。

创建控件时，此值为空
查询时返回完整结构
        :type ComponentId: str
        :param ComponentType: 如果是Component控件类型，则可选的字段为：
TEXT - 普通文本控件；
DATE - 普通日期控件；跟TEXT相比会有校验逻辑
如果是SignComponent控件类型，则可选的字段为
SIGN_SEAL - 签署印章控件；
SIGN_DATE - 签署日期控件；
SIGN_SIGNATURE - 用户签名控件；
SIGN_PERSONAL_SEAL - 个人签署印章控件；

表单域的控件不能作为印章和签名控件
        :type ComponentType: str
        :param ComponentName: 控件简称
        :type ComponentName: str
        :param ComponentRequired: 定义控件是否为必填项，默认为false
        :type ComponentRequired: bool
        :param FileIndex: 控件所属文件的序号 (文档中文件的排列序号)
        :type FileIndex: int
        :param GenerateMode: 控件生成的方式：
NORMAL - 普通控件
FIELD - 表单域
KEYWORD - 关键字
        :type GenerateMode: str
        :param ComponentWidth: 参数控件宽度，默认100，单位px
表单域和关键字转换控件不用填
        :type ComponentWidth: float
        :param ComponentHeight: 参数控件高度，默认100，单位px
表单域和关键字转换控件不用填
        :type ComponentHeight: float
        :param ComponentPage: 参数控件所在页码
        :type ComponentPage: int
        :param ComponentPosX: 参数控件X位置，单位px
        :type ComponentPosX: float
        :param ComponentPosY: 参数控件Y位置，单位px
        :type ComponentPosY: float
        :param ComponentExtra: 参数控件样式，json格式表述
不同类型的控件会有部分非通用参数
TEXT控件可以指定字体
例如：{"FontSize":12}
        :type ComponentExtra: str
        :param ComponentValue: 印章 ID，传参 DEFAULT_COMPANY_SEAL 表示使用默认印章。
控件填入内容，印章控件里面，如果是手写签名内容为PNG图片格式的base64编码
        :type ComponentValue: str
        :param ComponentDateFontSize: 日期签署控件的字号，默认为 12

签署区日期控件会转换成图片格式并带存证，需要通过字体决定图片大小
        :type ComponentDateFontSize: int
        :param DocumentId: 控件所属文档的Id, 模块相关接口为空值
        :type DocumentId: str
        :param ComponentDescription: 控件描述
        :type ComponentDescription: str
        """
        self.ComponentId = None
        self.ComponentType = None
        self.ComponentName = None
        self.ComponentRequired = None
        self.FileIndex = None
        self.GenerateMode = None
        self.ComponentWidth = None
        self.ComponentHeight = None
        self.ComponentPage = None
        self.ComponentPosX = None
        self.ComponentPosY = None
        self.ComponentExtra = None
        self.ComponentValue = None
        self.ComponentDateFontSize = None
        self.DocumentId = None
        self.ComponentDescription = None


    def _deserialize(self, params):
        self.ComponentId = params.get("ComponentId")
        self.ComponentType = params.get("ComponentType")
        self.ComponentName = params.get("ComponentName")
        self.ComponentRequired = params.get("ComponentRequired")
        self.FileIndex = params.get("FileIndex")
        self.GenerateMode = params.get("GenerateMode")
        self.ComponentWidth = params.get("ComponentWidth")
        self.ComponentHeight = params.get("ComponentHeight")
        self.ComponentPage = params.get("ComponentPage")
        self.ComponentPosX = params.get("ComponentPosX")
        self.ComponentPosY = params.get("ComponentPosY")
        self.ComponentExtra = params.get("ComponentExtra")
        self.ComponentValue = params.get("ComponentValue")
        self.ComponentDateFontSize = params.get("ComponentDateFontSize")
        self.DocumentId = params.get("DocumentId")
        self.ComponentDescription = params.get("ComponentDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsoleLoginUrlRequest(AbstractModel):
    """CreateConsoleLoginUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 应用信息
此接口Agent.ProxyOrganizationOpenId 和 Agent. ProxyOperator.OpenId 必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param ProxyOrganizationName: 渠道侧合作企业名称
        :type ProxyOrganizationName: str
        :param UniformSocialCreditCode: 渠道侧合作企业统一社会信用代码
        :type UniformSocialCreditCode: str
        :param ProxyOperatorName: 渠道侧合作企业经办人的姓名
        :type ProxyOperatorName: str
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param Module: 控制台指定模块，文件/合同管理:"DOCUMENT"，模版管理:"TEMPLATE"，印章管理:"SEAL"，组织架构/人员:"OPERATOR"，空字符串："账号信息"
        :type Module: str
        :param ModuleId: 控制台指定模块Id
        :type ModuleId: str
        """
        self.Agent = None
        self.ProxyOrganizationName = None
        self.UniformSocialCreditCode = None
        self.ProxyOperatorName = None
        self.Operator = None
        self.Module = None
        self.ModuleId = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.ProxyOrganizationName = params.get("ProxyOrganizationName")
        self.UniformSocialCreditCode = params.get("UniformSocialCreditCode")
        self.ProxyOperatorName = params.get("ProxyOperatorName")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.Module = params.get("Module")
        self.ModuleId = params.get("ModuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsoleLoginUrlResponse(AbstractModel):
    """CreateConsoleLoginUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param ConsoleUrl: 控制台url
        :type ConsoleUrl: str
        :param IsActivated: 渠道合作企业是否认证开通腾讯电子签。
当渠道合作企业未完成认证开通腾讯电子签,建议先调用同步企业信息(SyncProxyOrganization)和同步经办人信息(SyncProxyOrganizationOperators)接口成功后再跳转到登录页面。
        :type IsActivated: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ConsoleUrl = None
        self.IsActivated = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ConsoleUrl = params.get("ConsoleUrl")
        self.IsActivated = params.get("IsActivated")
        self.RequestId = params.get("RequestId")


class CreateFlowsByTemplatesRequest(AbstractModel):
    """CreateFlowsByTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param FlowInfos: 多个合同（流程）信息
        :type FlowInfos: list of FlowInfo
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.FlowInfos = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        if params.get("FlowInfos") is not None:
            self.FlowInfos = []
            for item in params.get("FlowInfos"):
                obj = FlowInfo()
                obj._deserialize(item)
                self.FlowInfos.append(obj)
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowsByTemplatesResponse(AbstractModel):
    """CreateFlowsByTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowIds: 多个合同ID
        :type FlowIds: list of str
        :param CustomerData: 渠道的业务信息，限制1024字符
        :type CustomerData: list of str
        :param ErrorMessages: 创建消息，对应多个合同ID，
成功为“”,创建失败则对应失败消息
        :type ErrorMessages: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowIds = None
        self.CustomerData = None
        self.ErrorMessages = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowIds = params.get("FlowIds")
        self.CustomerData = params.get("CustomerData")
        self.ErrorMessages = params.get("ErrorMessages")
        self.RequestId = params.get("RequestId")


class CreateSignUrlsRequest(AbstractModel):
    """CreateSignUrls请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param FlowIds: 所签署合同ID数组
        :type FlowIds: list of str
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param Endpoint: 签署链接类型，默认：“WEIXINAPP”-直接跳小程序; “CHANNEL”-跳转H5页面; “APP”-第三方APP或小程序跳转电子签小程序;
        :type Endpoint: str
        :param JumpUrl: 签署完成后H5引导页跳转URL
        :type JumpUrl: str
        """
        self.Agent = None
        self.FlowIds = None
        self.Operator = None
        self.Endpoint = None
        self.JumpUrl = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.FlowIds = params.get("FlowIds")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.Endpoint = params.get("Endpoint")
        self.JumpUrl = params.get("JumpUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSignUrlsResponse(AbstractModel):
    """CreateSignUrls返回参数结构体

    """

    def __init__(self):
        r"""
        :param SignUrlInfos: 签署参与者签署H5链接信息数组
        :type SignUrlInfos: list of SignUrlInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SignUrlInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SignUrlInfos") is not None:
            self.SignUrlInfos = []
            for item in params.get("SignUrlInfos"):
                obj = SignUrlInfo()
                obj._deserialize(item)
                self.SignUrlInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTemplatesRequest(AbstractModel):
    """DescribeTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param TemplateId: 模版唯一标识
        :type TemplateId: str
        """
        self.Agent = None
        self.Operator = None
        self.TemplateId = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTemplatesResponse(AbstractModel):
    """DescribeTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param Templates: 模板详情
        :type Templates: list of TemplateInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Templates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = TemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUsageRequest(AbstractModel):
    """DescribeUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 应用信息
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param StartDate: 开始时间 eg:2021-03-21
        :type StartDate: str
        :param EndDate: 结束时间 eg:2021-06-21 
开始时间到结束时间的区间长度小于等于90天
        :type EndDate: str
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param NeedAggregate: 是否汇总数据，默认不汇总
不汇总:返回在统计区间内渠道下所有企业的每日明细，即每个企业N条数据，N为统计天数
汇总:返回在统计区间内渠道下所有企业的汇总后数据，即每个企业一条数据
        :type NeedAggregate: bool
        :param Limit: 单次返回的最多条目数量,默认为1000,且不能超过1000
        :type Limit: int
        :param Offset: 偏移量,默认是0
        :type Offset: int
        """
        self.Agent = None
        self.StartDate = None
        self.EndDate = None
        self.Operator = None
        self.NeedAggregate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.NeedAggregate = params.get("NeedAggregate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsageResponse(AbstractModel):
    """DescribeUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 用量明细条数
        :type Total: int
        :param Details: 用量明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of UsageDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Details = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = UsageDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        self.RequestId = params.get("RequestId")


class FlowApproverInfo(AbstractModel):
    """创建流程签署人入参

    """

    def __init__(self):
        r"""
        :param Name: 签署人姓名
        :type Name: str
        :param Mobile: 签署人手机号，脱敏显示
        :type Mobile: str
        :param IdCardNumber: 经办人身份证号
        :type IdCardNumber: str
        :param JumpUrl: 签署完前端跳转的url，暂未使用
        :type JumpUrl: str
        :param Deadline: 签署截止时间
        :type Deadline: int
        :param CallbackUrl: 签署完回调url
        :type CallbackUrl: str
        :param ApproverType: 签署人类型，PERSON和ORGANIZATION
        :type ApproverType: str
        :param OpenId: 用户侧第三方id
        :type OpenId: str
        """
        self.Name = None
        self.Mobile = None
        self.IdCardNumber = None
        self.JumpUrl = None
        self.Deadline = None
        self.CallbackUrl = None
        self.ApproverType = None
        self.OpenId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Mobile = params.get("Mobile")
        self.IdCardNumber = params.get("IdCardNumber")
        self.JumpUrl = params.get("JumpUrl")
        self.Deadline = params.get("Deadline")
        self.CallbackUrl = params.get("CallbackUrl")
        self.ApproverType = params.get("ApproverType")
        self.OpenId = params.get("OpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowInfo(AbstractModel):
    """此结构体 (FlowInfo) 用于描述流程信息。

    """

    def __init__(self):
        r"""
        :param FlowName: 合同名字
        :type FlowName: str
        :param Deadline: 签署截止时间戳，超过有效签署时间则该签署流程失败
        :type Deadline: int
        :param TemplateId: 模版ID
        :type TemplateId: str
        :param FlowType: 合同类型：
1. “劳务”
2. “销售”
3. “租赁”
4. “其他”
        :type FlowType: str
        :param CallbackUrl: 回调地址
        :type CallbackUrl: str
        :param FlowApprovers: 多个签署人信息
        :type FlowApprovers: list of FlowApproverInfo
        :param FormFields: 表单K-V对列表
        :type FormFields: list of FormField
        :param FlowDescription: 合同描述
        :type FlowDescription: str
        :param CustomerData: 渠道的业务信息，限制1024字符
        :type CustomerData: str
        """
        self.FlowName = None
        self.Deadline = None
        self.TemplateId = None
        self.FlowType = None
        self.CallbackUrl = None
        self.FlowApprovers = None
        self.FormFields = None
        self.FlowDescription = None
        self.CustomerData = None


    def _deserialize(self, params):
        self.FlowName = params.get("FlowName")
        self.Deadline = params.get("Deadline")
        self.TemplateId = params.get("TemplateId")
        self.FlowType = params.get("FlowType")
        self.CallbackUrl = params.get("CallbackUrl")
        if params.get("FlowApprovers") is not None:
            self.FlowApprovers = []
            for item in params.get("FlowApprovers"):
                obj = FlowApproverInfo()
                obj._deserialize(item)
                self.FlowApprovers.append(obj)
        if params.get("FormFields") is not None:
            self.FormFields = []
            for item in params.get("FormFields"):
                obj = FormField()
                obj._deserialize(item)
                self.FormFields.append(obj)
        self.FlowDescription = params.get("FlowDescription")
        self.CustomerData = params.get("CustomerData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FormField(AbstractModel):
    """此结构 (FormField) 用于描述内容控件填充结构。

    """

    def __init__(self):
        r"""
        :param ComponentValue: 表单域或控件的Value
        :type ComponentValue: str
        :param ComponentId: 表单域或控件的ID，跟ComponentName二选一，不能全为空
注意：此字段可能返回 null，表示取不到有效值。
        :type ComponentId: str
        :param ComponentName: 控件的名字，跟ComponentId二选一，不能全为空
注意：此字段可能返回 null，表示取不到有效值。
        :type ComponentName: str
        """
        self.ComponentValue = None
        self.ComponentId = None
        self.ComponentName = None


    def _deserialize(self, params):
        self.ComponentValue = params.get("ComponentValue")
        self.ComponentId = params.get("ComponentId")
        self.ComponentName = params.get("ComponentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrepareFlowsRequest(AbstractModel):
    """PrepareFlows请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param FlowInfos: 多个合同（流程）信息
        :type FlowInfos: list of FlowInfo
        :param JumpUrl: 操作完成后的跳转地址
        :type JumpUrl: str
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.FlowInfos = None
        self.JumpUrl = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        if params.get("FlowInfos") is not None:
            self.FlowInfos = []
            for item in params.get("FlowInfos"):
                obj = FlowInfo()
                obj._deserialize(item)
                self.FlowInfos.append(obj)
        self.JumpUrl = params.get("JumpUrl")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrepareFlowsResponse(AbstractModel):
    """PrepareFlows返回参数结构体

    """

    def __init__(self):
        r"""
        :param ConfirmUrl: 待发起文件确认页
        :type ConfirmUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ConfirmUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ConfirmUrl = params.get("ConfirmUrl")
        self.RequestId = params.get("RequestId")


class ProxyOrganizationOperator(AbstractModel):
    """合作企业经办人列表信息

    """

    def __init__(self):
        r"""
        :param Id: 经办人ID（渠道颁发）
        :type Id: str
        :param Name: 经办人姓名
        :type Name: str
        :param IdCardType: 经办人身份证件类型
用户证件类型：默认ID_CARD
1. ID_CARD - 居民身份证
2. HOUSEHOLD_REGISTER - 户口本
3. TEMP_ID_CARD - 临时居民身份证
        :type IdCardType: str
        :param IdCardNumber: 经办人身份证号
        :type IdCardNumber: str
        :param Mobile: 经办人手机号
        :type Mobile: str
        """
        self.Id = None
        self.Name = None
        self.IdCardType = None
        self.IdCardNumber = None
        self.Mobile = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.IdCardType = params.get("IdCardType")
        self.IdCardNumber = params.get("IdCardNumber")
        self.Mobile = params.get("Mobile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Recipient(AbstractModel):
    """签署参与者信息

    """

    def __init__(self):
        r"""
        :param RecipientId: 签署人唯一标识
        :type RecipientId: str
        :param RecipientType: 签署方类型：ENTERPRISE-企业INDIVIDUAL-自然人
        :type RecipientType: str
        :param Description: 描述
        :type Description: str
        :param RoleName: 签署方备注信息
        :type RoleName: str
        :param RequireValidation: 是否需要校验
        :type RequireValidation: bool
        :param RequireSign: 是否必须填写
        :type RequireSign: bool
        :param SignType: 签署类型
        :type SignType: int
        :param RoutingOrder: 签署顺序：数字越小优先级越高
        :type RoutingOrder: int
        """
        self.RecipientId = None
        self.RecipientType = None
        self.Description = None
        self.RoleName = None
        self.RequireValidation = None
        self.RequireSign = None
        self.SignType = None
        self.RoutingOrder = None


    def _deserialize(self, params):
        self.RecipientId = params.get("RecipientId")
        self.RecipientType = params.get("RecipientType")
        self.Description = params.get("Description")
        self.RoleName = params.get("RoleName")
        self.RequireValidation = params.get("RequireValidation")
        self.RequireSign = params.get("RequireSign")
        self.SignType = params.get("SignType")
        self.RoutingOrder = params.get("RoutingOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignUrlInfo(AbstractModel):
    """签署链接内容

    """

    def __init__(self):
        r"""
        :param SignUrl: 签署链接
注意：此字段可能返回 null，表示取不到有效值。
        :type SignUrl: str
        :param Deadline: 链接失效时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Deadline: int
        :param SignOrder: 当流程为顺序签署此参数有效时，数字越小优先级越高，暂不支持并行签署 可选
注意：此字段可能返回 null，表示取不到有效值。
        :type SignOrder: int
        :param SignId: 签署人编号
注意：此字段可能返回 null，表示取不到有效值。
        :type SignId: str
        :param CustomUserId: 自定义用户编号
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomUserId: str
        :param Name: 用户姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Mobile: 用户手机号码
注意：此字段可能返回 null，表示取不到有效值。
        :type Mobile: str
        :param OrganizationName: 签署参与者机构名字
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationName: str
        :param ApproverType: 参与者类型:
ORGANIZATION 企业经办人
PERSON 自然人
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproverType: str
        :param IdCardNumber: 经办人身份证号
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardNumber: str
        :param FlowId: 签署链接对应流程Id
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: str
        :param OpenId: 企业经办人 用户在渠道的编号
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        """
        self.SignUrl = None
        self.Deadline = None
        self.SignOrder = None
        self.SignId = None
        self.CustomUserId = None
        self.Name = None
        self.Mobile = None
        self.OrganizationName = None
        self.ApproverType = None
        self.IdCardNumber = None
        self.FlowId = None
        self.OpenId = None


    def _deserialize(self, params):
        self.SignUrl = params.get("SignUrl")
        self.Deadline = params.get("Deadline")
        self.SignOrder = params.get("SignOrder")
        self.SignId = params.get("SignId")
        self.CustomUserId = params.get("CustomUserId")
        self.Name = params.get("Name")
        self.Mobile = params.get("Mobile")
        self.OrganizationName = params.get("OrganizationName")
        self.ApproverType = params.get("ApproverType")
        self.IdCardNumber = params.get("IdCardNumber")
        self.FlowId = params.get("FlowId")
        self.OpenId = params.get("OpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncFailReason(AbstractModel):
    """同步经办人失败原因

    """

    def __init__(self):
        r"""
        :param Id: 经办人Id
        :type Id: str
        :param Message: 失败原因
例如：Id不符合规范、证件号码不合法等
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self.Id = None
        self.Message = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncProxyOrganizationOperatorsRequest(AbstractModel):
    """SyncProxyOrganizationOperators请求参数结构体

    """

    def __init__(self):
        r"""
        :param OperatorType: 操作类型，新增:"CREATE"，修改:"UPDATE"，离职:"RESIGN"
        :type OperatorType: str
        :param Agent: 应用信息
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param ProxyOrganizationOperators: 经办人信息列表
        :type ProxyOrganizationOperators: list of ProxyOrganizationOperator
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.OperatorType = None
        self.Agent = None
        self.ProxyOrganizationOperators = None
        self.Operator = None


    def _deserialize(self, params):
        self.OperatorType = params.get("OperatorType")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        if params.get("ProxyOrganizationOperators") is not None:
            self.ProxyOrganizationOperators = []
            for item in params.get("ProxyOrganizationOperators"):
                obj = ProxyOrganizationOperator()
                obj._deserialize(item)
                self.ProxyOrganizationOperators.append(obj)
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncProxyOrganizationOperatorsResponse(AbstractModel):
    """SyncProxyOrganizationOperators返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: Status 同步状态,全部同步失败接口会直接报错
1-成功 
2-部分成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param FailedList: 同步失败经办人及其失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedList: list of SyncFailReason
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.FailedList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        if params.get("FailedList") is not None:
            self.FailedList = []
            for item in params.get("FailedList"):
                obj = SyncFailReason()
                obj._deserialize(item)
                self.FailedList.append(obj)
        self.RequestId = params.get("RequestId")


class SyncProxyOrganizationRequest(AbstractModel):
    """SyncProxyOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 应用信息
此接口Agent.ProxyOrganizationOpenId必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param ProxyOrganizationName: 渠道侧合作企业名称
        :type ProxyOrganizationName: str
        :param UniformSocialCreditCode: 渠道侧合作企业统一社会信用代码
        :type UniformSocialCreditCode: str
        :param BusinessLicense: 营业执照正面照(PNG或JPG) base64格式, 大小不超过5M
        :type BusinessLicense: str
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.ProxyOrganizationName = None
        self.UniformSocialCreditCode = None
        self.BusinessLicense = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.ProxyOrganizationName = params.get("ProxyOrganizationName")
        self.UniformSocialCreditCode = params.get("UniformSocialCreditCode")
        self.BusinessLicense = params.get("BusinessLicense")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncProxyOrganizationResponse(AbstractModel):
    """SyncProxyOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TemplateInfo(AbstractModel):
    """此结构体 (TemplateInfo) 用于描述模板的信息。

    """

    def __init__(self):
        r"""
        :param TemplateId: 模板ID
        :type TemplateId: str
        :param TemplateName: 模板名字
        :type TemplateName: str
        :param Description: 模板描述信息
        :type Description: str
        :param Components: 模板控件信息结构
        :type Components: list of Component
        :param SignComponents: 签署区模板信息结构
        :type SignComponents: list of Component
        :param Creator: 模板的创建者信息
        :type Creator: str
        :param CreatedOn: 模板创建的时间戳（精确到秒）
        :type CreatedOn: int
        :param TemplateType: 模板类型：1-静默签；2-静默签授权；3-普通模版
        :type TemplateType: int
        :param Recipients: 模板中的流程参与人信息
        :type Recipients: list of Recipient
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.Components = None
        self.SignComponents = None
        self.Creator = None
        self.CreatedOn = None
        self.TemplateType = None
        self.Recipients = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        if params.get("Components") is not None:
            self.Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self.Components.append(obj)
        if params.get("SignComponents") is not None:
            self.SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self.SignComponents.append(obj)
        self.Creator = params.get("Creator")
        self.CreatedOn = params.get("CreatedOn")
        self.TemplateType = params.get("TemplateType")
        if params.get("Recipients") is not None:
            self.Recipients = []
            for item in params.get("Recipients"):
                obj = Recipient()
                obj._deserialize(item)
                self.Recipients.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageDetail(AbstractModel):
    """用量明细

    """

    def __init__(self):
        r"""
        :param ProxyOrganizationOpenId: 渠道侧合作企业唯一标识
        :type ProxyOrganizationOpenId: str
        :param Usage: 消耗量
        :type Usage: int
        :param Date: 日期，当需要汇总数据时日期为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Date: str
        """
        self.ProxyOrganizationOpenId = None
        self.Usage = None
        self.Date = None


    def _deserialize(self, params):
        self.ProxyOrganizationOpenId = params.get("ProxyOrganizationOpenId")
        self.Usage = params.get("Usage")
        self.Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    """接口调用者信息

    """

    def __init__(self):
        r"""
        :param CustomUserId: 自定义用户编号
        :type CustomUserId: str
        :param Channel: 用户的来源渠道
        :type Channel: str
        :param OpenId: 用户在渠道的编号
        :type OpenId: str
        :param ClientIp: 用户真实IP
        :type ClientIp: str
        :param ProxyIp: 用户代理IP
        :type ProxyIp: str
        """
        self.CustomUserId = None
        self.Channel = None
        self.OpenId = None
        self.ClientIp = None
        self.ProxyIp = None


    def _deserialize(self, params):
        self.CustomUserId = params.get("CustomUserId")
        self.Channel = params.get("Channel")
        self.OpenId = params.get("OpenId")
        self.ClientIp = params.get("ClientIp")
        self.ProxyIp = params.get("ProxyIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        