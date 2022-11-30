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
        :param AppId: 应用的唯一标识。不同的业务系统可以采用不同的AppId，不同AppId下的数据是隔离的。可以由控制台开发者中心-应用集成自主生成。
        :type AppId: str
        :param ProxyOrganizationOpenId: 渠道平台自定义，对于渠道子客企业的唯一标识。一个渠道子客企业主体与子客企业ProxyOrganizationOpenId是一一对应的，不可更改，不可重复使用。（例如，可以使用企业名称的hash值，或者社会统一信用代码的hash值，或者随机hash值，需要渠道平台保存），最大64位字符串
        :type ProxyOrganizationOpenId: str
        :param ProxyOperator: 渠道子客企业中的员工/经办人，通过渠道平台进入电子签完成实名、且被赋予相关权限后，可以参与到企业资源的管理或签署流程中。
        :type ProxyOperator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param ProxyAppId: 在子客企业开通电子签后，会生成唯一的子客应用Id（ProxyAppId）用于代理调用时的鉴权，在子客开通的回调中获取。
        :type ProxyAppId: str
        :param ProxyOrganizationId: 内部参数，暂未开放使用
        :type ProxyOrganizationId: str
        """
        self.AppId = None
        self.ProxyOrganizationOpenId = None
        self.ProxyOperator = None
        self.ProxyAppId = None
        self.ProxyOrganizationId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.ProxyOrganizationOpenId = params.get("ProxyOrganizationOpenId")
        if params.get("ProxyOperator") is not None:
            self.ProxyOperator = UserInfo()
            self.ProxyOperator._deserialize(params.get("ProxyOperator"))
        self.ProxyAppId = params.get("ProxyAppId")
        self.ProxyOrganizationId = params.get("ProxyOrganizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApproverOption(AbstractModel):
    """签署人个性化能力信息

    """

    def __init__(self):
        r"""
        :param HideOneKeySign: 是否隐藏一键签署 false-不隐藏,默认 true-隐藏
        :type HideOneKeySign: bool
        """
        self.HideOneKeySign = None


    def _deserialize(self, params):
        self.HideOneKeySign = params.get("HideOneKeySign")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApproverRestriction(AbstractModel):
    """指定签署人限制项

    """

    def __init__(self):
        r"""
        :param Name: 指定签署人名字
        :type Name: str
        :param Mobile: 指定签署人手机号
        :type Mobile: str
        :param IdCardType: 指定签署人证件类型
        :type IdCardType: str
        :param IdCardNumber: 指定签署人证件号码
        :type IdCardNumber: str
        """
        self.Name = None
        self.Mobile = None
        self.IdCardType = None
        self.IdCardNumber = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Mobile = params.get("Mobile")
        self.IdCardType = params.get("IdCardType")
        self.IdCardNumber = params.get("IdCardNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthFailMessage(AbstractModel):
    """授权出错信息

    """

    def __init__(self):
        r"""
        :param ProxyOrganizationOpenId: 合作企业Id
        :type ProxyOrganizationOpenId: str
        :param Message: 出错信息
        :type Message: str
        """
        self.ProxyOrganizationOpenId = None
        self.Message = None


    def _deserialize(self, params):
        self.ProxyOrganizationOpenId = params.get("ProxyOrganizationOpenId")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizedUser(AbstractModel):
    """授权用户

    """

    def __init__(self):
        r"""
        :param OpenId: 用户openid
        :type OpenId: str
        """
        self.OpenId = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcInfo(AbstractModel):
    """抄送信息

    """

    def __init__(self):
        r"""
        :param Mobile: 被抄送人手机号，大陆11位手机号
        :type Mobile: str
        """
        self.Mobile = None


    def _deserialize(self, params):
        self.Mobile = params.get("Mobile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelBatchCancelFlowsRequest(AbstractModel):
    """ChannelBatchCancelFlows请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param FlowIds: 签署流程Id数组，最多100个，超过100不处理
        :type FlowIds: list of str
        :param CancelMessage: 撤销理由
        :type CancelMessage: str
        :param CancelMessageFormat: 撤销理由自定义格式；选项：
0 默认格式
1 只保留身份信息：展示为【发起方】
2 保留身份信息+企业名称：展示为【发起方xxx公司】
3 保留身份信息+企业名称+经办人名称：展示为【发起方xxxx公司-经办人姓名】
        :type CancelMessageFormat: int
        :param Operator: 操作人信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.FlowIds = None
        self.CancelMessage = None
        self.CancelMessageFormat = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.FlowIds = params.get("FlowIds")
        self.CancelMessage = params.get("CancelMessage")
        self.CancelMessageFormat = params.get("CancelMessageFormat")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelBatchCancelFlowsResponse(AbstractModel):
    """ChannelBatchCancelFlows返回参数结构体

    """

    def __init__(self):
        r"""
        :param FailMessages: 签署流程批量撤销失败原因，错误信息与流程Id一一对应，如果部分流程不可撤销，不会返回错误信息，只会撤销可撤销流程
        :type FailMessages: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FailMessages = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailMessages = params.get("FailMessages")
        self.RequestId = params.get("RequestId")


class ChannelCancelFlowRequest(AbstractModel):
    """ChannelCancelFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 签署流程编号
        :type FlowId: str
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param CancelMessage: 撤回原因，最大不超过200字符
        :type CancelMessage: str
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param CancelMessageFormat: 撤销理由自定义格式；选项：
0 默认格式
1 只保留身份信息：展示为【发起方】
2 保留身份信息+企业名称：展示为【发起方xxx公司】
3 保留身份信息+企业名称+经办人名称：展示为【发起方xxxx公司-经办人姓名】
        :type CancelMessageFormat: int
        """
        self.FlowId = None
        self.Agent = None
        self.CancelMessage = None
        self.Operator = None
        self.CancelMessageFormat = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.CancelMessage = params.get("CancelMessage")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.CancelMessageFormat = params.get("CancelMessageFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCancelFlowResponse(AbstractModel):
    """ChannelCancelFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ChannelCancelMultiFlowSignQRCodeRequest(AbstractModel):
    """ChannelCancelMultiFlowSignQRCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param QrCodeId: 二维码id
        :type QrCodeId: str
        :param Operator: 用户信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.QrCodeId = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.QrCodeId = params.get("QrCodeId")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCancelMultiFlowSignQRCodeResponse(AbstractModel):
    """ChannelCancelMultiFlowSignQRCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ChannelCreateBatchCancelFlowUrlRequest(AbstractModel):
    """ChannelCreateBatchCancelFlowUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param FlowIds: 签署流程Id数组
        :type FlowIds: list of str
        :param Operator: 操作人信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.FlowIds = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.FlowIds = params.get("FlowIds")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateBatchCancelFlowUrlResponse(AbstractModel):
    """ChannelCreateBatchCancelFlowUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param BatchCancelFlowUrl: 批量撤销url
        :type BatchCancelFlowUrl: str
        :param FailMessages: 签署流程批量撤销失败原因
        :type FailMessages: list of str
        :param UrlExpireOn: 签署撤销url过期时间-年月日-时分秒
        :type UrlExpireOn: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BatchCancelFlowUrl = None
        self.FailMessages = None
        self.UrlExpireOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchCancelFlowUrl = params.get("BatchCancelFlowUrl")
        self.FailMessages = params.get("FailMessages")
        self.UrlExpireOn = params.get("UrlExpireOn")
        self.RequestId = params.get("RequestId")


class ChannelCreateBoundFlowsRequest(AbstractModel):
    """ChannelCreateBoundFlows请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 应用信息
此接口Agent.AppId、Agent.ProxyOrganizationOpenId 和 Agent. ProxyOperator.OpenId 必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param FlowIds: 领取的合同id列表
        :type FlowIds: list of str
        :param Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.FlowIds = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.FlowIds = params.get("FlowIds")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateBoundFlowsResponse(AbstractModel):
    """ChannelCreateBoundFlows返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ChannelCreateConvertTaskApiRequest(AbstractModel):
    """ChannelCreateConvertTaskApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param ResourceType: 资源类型 取值范围doc,docx,html,xls,xlsx之一
        :type ResourceType: str
        :param ResourceName: 资源名称，长度限制为256字符
        :type ResourceName: str
        :param ResourceId: 资源Id，通过UploadFiles获取
        :type ResourceId: str
        :param Operator: 操作者信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param Organization: 暂未开放
        :type Organization: :class:`tencentcloud.essbasic.v20210526.models.OrganizationInfo`
        """
        self.Agent = None
        self.ResourceType = None
        self.ResourceName = None
        self.ResourceId = None
        self.Operator = None
        self.Organization = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        self.ResourceId = params.get("ResourceId")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        if params.get("Organization") is not None:
            self.Organization = OrganizationInfo()
            self.Organization._deserialize(params.get("Organization"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateConvertTaskApiResponse(AbstractModel):
    """ChannelCreateConvertTaskApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ChannelCreateFlowByFilesRequest(AbstractModel):
    """ChannelCreateFlowByFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param FlowName: 签署流程名称，长度不超过200个字符
        :type FlowName: str
        :param FlowApprovers: 签署流程签约方列表，最多不超过5个参与方
        :type FlowApprovers: list of FlowApproverInfo
        :param FileIds: 签署文件资源Id列表，目前仅支持单个文件
        :type FileIds: list of str
        :param Components: 签署文件中的发起方的填写控件，需要在发起的时候进行填充
        :type Components: list of Component
        :param Deadline: 签署流程截止时间，十位数时间戳，最大值为33162419560，即3020年
        :type Deadline: int
        :param CallbackUrl: 签署流程回调地址，长度不超过255个字符
        :type CallbackUrl: str
        :param Unordered: 合同签署顺序类型(无序签,顺序签)，默认为false，即有序签署。有序签署时以传入FlowApprovers数组的顺序作为签署顺序
        :type Unordered: bool
        :param FlowType: 签署流程的类型，长度不超过255个字符
        :type FlowType: str
        :param FlowDescription: 签署流程的描述，长度不超过1000个字符
        :type FlowDescription: str
        :param CustomShowMap: 合同显示的页卡模板，说明：只支持{合同名称}, {发起方企业}, {发起方姓名}, {签署方N企业}, {签署方N姓名}，且N不能超过签署人的数量，N从1开始
        :type CustomShowMap: str
        :param CustomerData: 渠道的业务信息，最大长度1000个字符。发起自动签署时，需设置对应自动签署场景，目前仅支持场景：处方单-E_PRESCRIPTION_AUTO_SIGN
        :type CustomerData: str
        :param NeedSignReview: 发起方企业的签署人进行签署操作是否需要企业内部审批。 若设置为true,审核结果需通过接口 ChannelCreateFlowSignReview 通知电子签，审核通过后，发起方企业签署人方可进行签署操作，否则会阻塞其签署操作。  注：企业可以通过此功能与企业内部的审批流程进行关联，支持手动、静默签署合同。
        :type NeedSignReview: bool
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param ApproverVerifyType: 签署人校验方式
VerifyCheck: 人脸识别（默认）
MobileCheck：手机号验证
参数说明：可选人脸识别或手机号验证两种方式，若选择后者，未实名个人签署方在签署合同时，无需经过实名认证和意愿确认两次人脸识别，该能力仅适用于个人签署方。
        :type ApproverVerifyType: str
        :param SignBeanTag: 标识是否允许发起后添加控件。0为不允许1为允许。如果为1，创建的时候不能有签署控件，只能创建后添加。注意发起后添加控件功能不支持添加骑缝章和签批控件
        :type SignBeanTag: int
        """
        self.Agent = None
        self.FlowName = None
        self.FlowApprovers = None
        self.FileIds = None
        self.Components = None
        self.Deadline = None
        self.CallbackUrl = None
        self.Unordered = None
        self.FlowType = None
        self.FlowDescription = None
        self.CustomShowMap = None
        self.CustomerData = None
        self.NeedSignReview = None
        self.Operator = None
        self.ApproverVerifyType = None
        self.SignBeanTag = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.FlowName = params.get("FlowName")
        if params.get("FlowApprovers") is not None:
            self.FlowApprovers = []
            for item in params.get("FlowApprovers"):
                obj = FlowApproverInfo()
                obj._deserialize(item)
                self.FlowApprovers.append(obj)
        self.FileIds = params.get("FileIds")
        if params.get("Components") is not None:
            self.Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self.Components.append(obj)
        self.Deadline = params.get("Deadline")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Unordered = params.get("Unordered")
        self.FlowType = params.get("FlowType")
        self.FlowDescription = params.get("FlowDescription")
        self.CustomShowMap = params.get("CustomShowMap")
        self.CustomerData = params.get("CustomerData")
        self.NeedSignReview = params.get("NeedSignReview")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.ApproverVerifyType = params.get("ApproverVerifyType")
        self.SignBeanTag = params.get("SignBeanTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateFlowByFilesResponse(AbstractModel):
    """ChannelCreateFlowByFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 合同签署流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ChannelCreateFlowGroupByFilesRequest(AbstractModel):
    """ChannelCreateFlowGroupByFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowFileInfos: 每个子合同的发起所需的信息，数量限制2-100
        :type FlowFileInfos: list of FlowFileInfo
        :param FlowGroupName: 合同组名称，长度不超过200个字符
        :type FlowGroupName: str
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.FlowFileInfos = None
        self.FlowGroupName = None
        self.Agent = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("FlowFileInfos") is not None:
            self.FlowFileInfos = []
            for item in params.get("FlowFileInfos"):
                obj = FlowFileInfo()
                obj._deserialize(item)
                self.FlowFileInfos.append(obj)
        self.FlowGroupName = params.get("FlowGroupName")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateFlowGroupByFilesResponse(AbstractModel):
    """ChannelCreateFlowGroupByFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowGroupId: 合同组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowGroupId: str
        :param FlowIds: 子合同ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowGroupId = None
        self.FlowIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowGroupId = params.get("FlowGroupId")
        self.FlowIds = params.get("FlowIds")
        self.RequestId = params.get("RequestId")


class ChannelCreateFlowSignReviewRequest(AbstractModel):
    """ChannelCreateFlowSignReview请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param FlowId: 签署流程编号
        :type FlowId: str
        :param ReviewType: 企业内部审核结果
PASS: 通过
REJECT: 拒绝
SIGN_REJECT:拒签(流程结束)
        :type ReviewType: str
        :param ReviewMessage: 审核原因 
当ReviewType 是REJECT 时此字段必填,字符串长度不超过200
        :type ReviewMessage: str
        :param RecipientId: 签署节点审核时需要指定
        :type RecipientId: str
        """
        self.Agent = None
        self.FlowId = None
        self.ReviewType = None
        self.ReviewMessage = None
        self.RecipientId = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.FlowId = params.get("FlowId")
        self.ReviewType = params.get("ReviewType")
        self.ReviewMessage = params.get("ReviewMessage")
        self.RecipientId = params.get("RecipientId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateFlowSignReviewResponse(AbstractModel):
    """ChannelCreateFlowSignReview返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ChannelCreateMultiFlowSignQRCodeRequest(AbstractModel):
    """ChannelCreateMultiFlowSignQRCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。
此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param TemplateId: 模版ID
        :type TemplateId: str
        :param FlowName: 签署流程名称，最大长度200个字符。
        :type FlowName: str
        :param MaxFlowNum: 最大可发起签署流程份数，默认5份；发起签署流程数量超过此上限后，二维码自动失效。
        :type MaxFlowNum: int
        :param FlowEffectiveDay: 签署流程有效天数 默认7天 最高设置不超过30天
        :type FlowEffectiveDay: int
        :param QrEffectiveDay: 二维码有效天数 默认7天 最高设置不超过90天
        :type QrEffectiveDay: int
        :param Restrictions: 限制二维码用户条件
        :type Restrictions: list of ApproverRestriction
        :param CallbackUrl: 回调地址，最大长度1000个字符
不传默认使用渠道应用号配置的回调地址
回调时机:用户通过签署二维码发起合同时，企业额度不足导致失败
        :type CallbackUrl: str
        :param Operator: 用户信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param ApproverRestrictions: 限制二维码用户条件（已弃用）
        :type ApproverRestrictions: :class:`tencentcloud.essbasic.v20210526.models.ApproverRestriction`
        """
        self.Agent = None
        self.TemplateId = None
        self.FlowName = None
        self.MaxFlowNum = None
        self.FlowEffectiveDay = None
        self.QrEffectiveDay = None
        self.Restrictions = None
        self.CallbackUrl = None
        self.Operator = None
        self.ApproverRestrictions = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.TemplateId = params.get("TemplateId")
        self.FlowName = params.get("FlowName")
        self.MaxFlowNum = params.get("MaxFlowNum")
        self.FlowEffectiveDay = params.get("FlowEffectiveDay")
        self.QrEffectiveDay = params.get("QrEffectiveDay")
        if params.get("Restrictions") is not None:
            self.Restrictions = []
            for item in params.get("Restrictions"):
                obj = ApproverRestriction()
                obj._deserialize(item)
                self.Restrictions.append(obj)
        self.CallbackUrl = params.get("CallbackUrl")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        if params.get("ApproverRestrictions") is not None:
            self.ApproverRestrictions = ApproverRestriction()
            self.ApproverRestrictions._deserialize(params.get("ApproverRestrictions"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateMultiFlowSignQRCodeResponse(AbstractModel):
    """ChannelCreateMultiFlowSignQRCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param QrCode: 签署二维码对象
        :type QrCode: :class:`tencentcloud.essbasic.v20210526.models.SignQrCode`
        :param SignUrls: 签署链接对象
        :type SignUrls: :class:`tencentcloud.essbasic.v20210526.models.SignUrl`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.QrCode = None
        self.SignUrls = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QrCode") is not None:
            self.QrCode = SignQrCode()
            self.QrCode._deserialize(params.get("QrCode"))
        if params.get("SignUrls") is not None:
            self.SignUrls = SignUrl()
            self.SignUrls._deserialize(params.get("SignUrls"))
        self.RequestId = params.get("RequestId")


class ChannelCreateReleaseFlowRequest(AbstractModel):
    """ChannelCreateReleaseFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param NeedRelievedFlowId: 待解除的流程编号（即原流程的编号）
        :type NeedRelievedFlowId: str
        :param ReliveInfo: 解除协议内容
        :type ReliveInfo: :class:`tencentcloud.essbasic.v20210526.models.RelieveInfo`
        :param ReleasedApprovers: 非必须，解除协议的本企业签署人列表，默认使用原流程的签署人列表；当解除协议的签署人与原流程的签署人不能相同时（例如原流程签署人离职了），需要指定本企业的其他签署人来替换原流程中的原签署人，注意需要指明ApproverNumber来代表需要替换哪一个签署人，解除协议的签署人数量不能多于原流程的签署人数量
        :type ReleasedApprovers: list of ReleasedApprover
        :param CallbackUrl: 签署完回调url，最大长度1000个字符
        :type CallbackUrl: str
        :param Organization: 机构信息
        :type Organization: :class:`tencentcloud.essbasic.v20210526.models.OrganizationInfo`
        :param Operator: 用户信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.NeedRelievedFlowId = None
        self.ReliveInfo = None
        self.ReleasedApprovers = None
        self.CallbackUrl = None
        self.Organization = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.NeedRelievedFlowId = params.get("NeedRelievedFlowId")
        if params.get("ReliveInfo") is not None:
            self.ReliveInfo = RelieveInfo()
            self.ReliveInfo._deserialize(params.get("ReliveInfo"))
        if params.get("ReleasedApprovers") is not None:
            self.ReleasedApprovers = []
            for item in params.get("ReleasedApprovers"):
                obj = ReleasedApprover()
                obj._deserialize(item)
                self.ReleasedApprovers.append(obj)
        self.CallbackUrl = params.get("CallbackUrl")
        if params.get("Organization") is not None:
            self.Organization = OrganizationInfo()
            self.Organization._deserialize(params.get("Organization"))
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateReleaseFlowResponse(AbstractModel):
    """ChannelCreateReleaseFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 解除协议流程编号
        :type FlowId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ChannelDescribeEmployeesRequest(AbstractModel):
    """ChannelDescribeEmployees请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回最大数量，最大为20
        :type Limit: int
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param Filters: 查询过滤实名用户，Key为Status，Values为["IsVerified"]
根据第三方系统openId过滤查询员工时,Key为StaffOpenId,Values为["OpenId","OpenId",...]
查询离职员工时，Key为Status，Values为["QuiteJob"]
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0，最大为20000
        :type Offset: int
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Limit = None
        self.Agent = None
        self.Filters = None
        self.Offset = None
        self.Operator = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelDescribeEmployeesResponse(AbstractModel):
    """ChannelDescribeEmployees返回参数结构体

    """

    def __init__(self):
        r"""
        :param Employees: 员工数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Employees: list of Staff
        :param Offset: 偏移量，默认为0，最大为20000
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: int
        :param Limit: 返回最大数量，最大为20
        :type Limit: int
        :param TotalCount: 符合条件的员工数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Employees = None
        self.Offset = None
        self.Limit = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Employees") is not None:
            self.Employees = []
            for item in params.get("Employees"):
                obj = Staff()
                obj._deserialize(item)
                self.Employees.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ChannelDescribeOrganizationSealsRequest(AbstractModel):
    """ChannelDescribeOrganizationSeals请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param Limit: 返回最大数量，最大为100
        :type Limit: int
        :param Offset: 偏移量，默认为0，最大为20000
        :type Offset: int
        :param InfoType: 查询信息类型，为1时返回授权用户，为其他值时不返回
        :type InfoType: int
        :param SealId: 印章id（没有输入返回所有）
        :type SealId: str
        """
        self.Agent = None
        self.Limit = None
        self.Offset = None
        self.InfoType = None
        self.SealId = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.InfoType = params.get("InfoType")
        self.SealId = params.get("SealId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelDescribeOrganizationSealsResponse(AbstractModel):
    """ChannelDescribeOrganizationSeals返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 在设置了SealId时返回0或1，没有设置时返回公司的总印章数量，可能比返回的印章数组数量多
        :type TotalCount: int
        :param Seals: 查询到的印章结果数组
        :type Seals: list of OccupiedSeal
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Seals = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Seals") is not None:
            self.Seals = []
            for item in params.get("Seals"):
                obj = OccupiedSeal()
                obj._deserialize(item)
                self.Seals.append(obj)
        self.RequestId = params.get("RequestId")


class ChannelGetTaskResultApiRequest(AbstractModel):
    """ChannelGetTaskResultApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param TaskId: 任务Id，通过ChannelCreateConvertTaskApi接口获得
        :type TaskId: str
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param Organization: 暂未开放
        :type Organization: :class:`tencentcloud.essbasic.v20210526.models.OrganizationInfo`
        """
        self.Agent = None
        self.TaskId = None
        self.Operator = None
        self.Organization = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.TaskId = params.get("TaskId")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        if params.get("Organization") is not None:
            self.Organization = OrganizationInfo()
            self.Organization._deserialize(params.get("Organization"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelGetTaskResultApiResponse(AbstractModel):
    """ChannelGetTaskResultApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务Id
        :type TaskId: str
        :param TaskStatus: 任务状态，需要关注的状态
0  :NeedTranform   - 任务已提交
4  :Processing     - 文档转换中
8  :TaskEnd        - 任务处理完成
-2 :DownloadFailed - 下载失败
-6 :ProcessFailed  - 转换失败
-13:ProcessTimeout - 转换文件超时
        :type TaskStatus: int
        :param TaskMessage: 状态描述，需要关注的状态
NeedTranform   - 任务已提交
Processing     - 文档转换中
TaskEnd        - 任务处理完成
DownloadFailed - 下载失败
ProcessFailed  - 转换失败
ProcessTimeout - 转换文件超时
        :type TaskMessage: str
        :param ResourceId: 资源Id，也是FileId，用于文件发起使用
        :type ResourceId: str
        :param PreviewUrl: 预览文件Url，有效期30分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.TaskStatus = None
        self.TaskMessage = None
        self.ResourceId = None
        self.PreviewUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskStatus = params.get("TaskStatus")
        self.TaskMessage = params.get("TaskMessage")
        self.ResourceId = params.get("ResourceId")
        self.PreviewUrl = params.get("PreviewUrl")
        self.RequestId = params.get("RequestId")


class ChannelVerifyPdfRequest(AbstractModel):
    """ChannelVerifyPdf请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 合同Id，流程Id
        :type FlowId: str
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.FlowId = None
        self.Agent = None
        self.Operator = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelVerifyPdfResponse(AbstractModel):
    """ChannelVerifyPdf返回参数结构体

    """

    def __init__(self):
        r"""
        :param VerifyResult: 验签结果，1-文件未被篡改，全部签名在腾讯电子签完成； 2-文件未被篡改，部分签名在腾讯电子签完成；3-文件被篡改；4-异常：文件内没有签名域；5-异常：文件签名格式错误
        :type VerifyResult: int
        :param PdfVerifyResults: 验签结果详情,内部状态1-验签成功，在电子签签署；2-验签成功，在其他平台签署；3-验签失败；4-pdf文件没有签名域
；5-文件签名格式错误
        :type PdfVerifyResults: list of PdfVerifyResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VerifyResult = None
        self.PdfVerifyResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VerifyResult = params.get("VerifyResult")
        if params.get("PdfVerifyResults") is not None:
            self.PdfVerifyResults = []
            for item in params.get("PdfVerifyResults"):
                obj = PdfVerifyResult()
                obj._deserialize(item)
                self.PdfVerifyResults.append(obj)
        self.RequestId = params.get("RequestId")


class Component(AbstractModel):
    """此结构体 (Component) 用于描述控件属性。

    在通过文件发起合同时，对应的component有三种定位方式
    1. 绝对定位方式
    2. 表单域(FIELD)定位方式
    3. 关键字(KEYWORD)定位方式
    可以参考官网说明
    https://cloud.tencent.com/document/product/1323/78346#component-.E4.B8.89.E7.A7.8D.E5.AE.9A.E4.BD.8D.E6.96.B9.E5.BC.8F.E8.AF.B4.E6.98.8E

    """

    def __init__(self):
        r"""
        :param ComponentId: 控件编号

CreateFlowByTemplates发起合同时优先以ComponentId（不为空）填充；否则以ComponentName填充

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
MULTI_LINE_TEXT - 多行文本控件；
CHECK_BOX - 勾选框控件；
FILL_IMAGE - 图片控件；
DYNAMIC_TABLE - 动态表格控件；
ATTACHMENT - 附件控件；
SELECTOR - 选择器控件；
DATE - 日期控件；默认是格式化为xxxx年xx月xx日；
DISTRICT - 省市区行政区划控件；

如果是SignComponent控件类型，则可选的字段为
SIGN_SEAL - 签署印章控件；
SIGN_DATE - 签署日期控件；
SIGN_SIGNATURE - 用户签名控件；
SIGN_PERSONAL_SEAL - 个人签署印章控件（使用文件发起暂不支持此类型）；
SIGN_PAGING_SEAL - 骑缝章；若文件发起，需要对应填充ComponentPosY、ComponentWidth、ComponentHeight

表单域的控件不能作为印章和签名控件
        :type ComponentType: str
        :param ComponentName: 控件简称，不能超过30个字符
        :type ComponentName: str
        :param ComponentRequired: 定义控件是否为必填项，默认为false
        :type ComponentRequired: bool
        :param ComponentRecipientId: 控件关联的签署方id
        :type ComponentRecipientId: str
        :param FileIndex: 控件所属文件的序号 (文档中文件的排列序号，从0开始)
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
        :param ComponentPage: 参数控件所在页码，从1开始
        :type ComponentPage: int
        :param ComponentPosX: 参数控件X位置，单位px
        :type ComponentPosX: float
        :param ComponentPosY: 参数控件Y位置，单位px
        :type ComponentPosY: float
        :param ComponentExtra: 参数控件样式，json格式表述

不同类型的控件会有部分非通用参数

TEXT/MULTI_LINE_TEXT控件可以指定
1 Font：目前只支持黑体、宋体
2 FontSize： 范围12-72
3 FontAlign： Left/Right/Center，左对齐/居中/右对齐
例如：{"FontSize":12}

ComponentType为FILL_IMAGE时，支持以下参数：
NotMakeImageCenter：bool。是否设置图片居中。false：居中（默认）。 true: 不居中
FillMethod: int. 填充方式。0-铺满（默认）；1-等比例缩放

ComponentType为SIGN_SIGNATURE类型可以控制签署方式
{“ComponentTypeLimit”: [“xxx”]}
xxx可以为：
HANDWRITE – 手写签名
BORDERLESS_ESIGN – 自动生成无边框腾讯体
OCR_ESIGN -- AI智能识别手写签名
ESIGN -- 个人印章类型
如：{“ComponentTypeLimit”: [“BORDERLESS_ESIGN”]}
        :type ComponentExtra: str
        :param ComponentValue: 控件填充vaule，ComponentType和传入值类型对应关系：
TEXT - 文本内容
MULTI_LINE_TEXT - 文本内容
CHECK_BOX - true/false
FILL_IMAGE、ATTACHMENT - 附件的FileId，需要通过UploadFiles接口上传获取
SELECTOR - 选项值
DATE - 默认是格式化为xxxx年xx月xx日
DYNAMIC_TABLE - 传入json格式的表格内容，具体见数据结构FlowInfo：https://cloud.tencent.com/document/api/1420/61525#FlowInfo
SIGN_SEAL - 印章ID
SIGN_PAGING_SEAL - 可以指定印章ID
        :type ComponentValue: str
        :param ComponentDateFontSize: 日期签署控件的字号，默认为 12

签署区日期控件会转换成图片格式并带存证，需要通过字体决定图片大小
        :type ComponentDateFontSize: int
        :param DocumentId: 控件所属文档的Id, 模块相关接口为空值
        :type DocumentId: str
        :param ComponentDescription: 控件描述，不能超过30个字符
        :type ComponentDescription: str
        :param OffsetX: 指定关键字时横坐标偏移量，单位pt
        :type OffsetX: float
        :param OffsetY: 指定关键字时纵坐标偏移量，单位pt
        :type OffsetY: float
        :param ChannelComponentId: 渠道控件ID。
如果不为空，属于渠道预设控件；
        :type ChannelComponentId: str
        :param KeywordPage: 指定关键字页码，可选参数，指定页码后，将只在指定的页码内查找关键字，非该页码的关键字将不会查询出来
        :type KeywordPage: int
        :param RelativeLocation: 关键字位置模式，Middle-居中，Below-正下方，Right-正右方，LowerRight-右上角，UpperRight-右下角。示例：如果设置Middle的关键字盖章，则印章的中心会和关键字的中心重合，如果设置Below，则印章在关键字的正下方
        :type RelativeLocation: str
        :param KeywordIndexes: 关键字索引，可选参数，如果一个关键字在PDF文件中存在多个，可以通过关键字索引指定使用第几个关键字作为最后的结果，可指定多个索引。示例[0,2]，说明使用PDF文件内第1个和第3个关键字位置。
        :type KeywordIndexes: list of int
        """
        self.ComponentId = None
        self.ComponentType = None
        self.ComponentName = None
        self.ComponentRequired = None
        self.ComponentRecipientId = None
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
        self.OffsetX = None
        self.OffsetY = None
        self.ChannelComponentId = None
        self.KeywordPage = None
        self.RelativeLocation = None
        self.KeywordIndexes = None


    def _deserialize(self, params):
        self.ComponentId = params.get("ComponentId")
        self.ComponentType = params.get("ComponentType")
        self.ComponentName = params.get("ComponentName")
        self.ComponentRequired = params.get("ComponentRequired")
        self.ComponentRecipientId = params.get("ComponentRecipientId")
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
        self.OffsetX = params.get("OffsetX")
        self.OffsetY = params.get("OffsetY")
        self.ChannelComponentId = params.get("ChannelComponentId")
        self.KeywordPage = params.get("KeywordPage")
        self.RelativeLocation = params.get("RelativeLocation")
        self.KeywordIndexes = params.get("KeywordIndexes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateChannelFlowEvidenceReportRequest(AbstractModel):
    """CreateChannelFlowEvidenceReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 签署流程编号
        :type FlowId: str
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.FlowId = None
        self.Agent = None
        self.Operator = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateChannelFlowEvidenceReportResponse(AbstractModel):
    """CreateChannelFlowEvidenceReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReportUrl: 废除，字段无效
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportUrl: str
        :param ReportId: 出证报告 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportId: str
        :param Status: 执行中：EvidenceStatusExecuting
成功：EvidenceStatusSuccess
失败：EvidenceStatusFailed
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReportUrl = None
        self.ReportId = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReportUrl = params.get("ReportUrl")
        self.ReportId = params.get("ReportId")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class CreateConsoleLoginUrlRequest(AbstractModel):
    """CreateConsoleLoginUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 应用信息
此接口Agent.AppId、Agent.ProxyOrganizationOpenId 和 Agent. ProxyOperator.OpenId 必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param ProxyOrganizationName: 渠道子客企业名称，最大长度64个字符
        :type ProxyOrganizationName: str
        :param ProxyOperatorName: 渠道子客企业经办人的姓名，最大长度50个字符
        :type ProxyOperatorName: str
        :param Module: 控制台指定模块，文件/合同管理:"DOCUMENT"，模板管理:"TEMPLATE"，印章管理:"SEAL"，组织架构/人员:"OPERATOR"，空字符串："账号信息"
        :type Module: str
        :param ModuleId: 控制台指定模块Id
        :type ModuleId: str
        :param UniformSocialCreditCode: 渠道子客企业统一社会信用代码，最大长度200个字符
        :type UniformSocialCreditCode: str
        :param MenuStatus: 是否展示左侧菜单栏 是：ENABLE（默认） 否：DISABLE
        :type MenuStatus: str
        :param Endpoint: 链接跳转类型："PC"-PC控制台，“CHANNEL”-H5跳转到电子签小程序；“APP”-第三方APP或小程序跳转电子签小程序，默认为PC控制台
        :type Endpoint: str
        :param AutoJumpBackEvent: 触发自动跳转事件，仅对App类型有效，"VERIFIED":企业认证完成/员工认证完成后跳回原App/小程序
        :type AutoJumpBackEvent: str
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param AuthorizationTypes: 支持的授权方式,授权方式: "1" - 上传授权书认证  "2" - 法定代表人认证
        :type AuthorizationTypes: list of int
        """
        self.Agent = None
        self.ProxyOrganizationName = None
        self.ProxyOperatorName = None
        self.Module = None
        self.ModuleId = None
        self.UniformSocialCreditCode = None
        self.MenuStatus = None
        self.Endpoint = None
        self.AutoJumpBackEvent = None
        self.Operator = None
        self.AuthorizationTypes = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.ProxyOrganizationName = params.get("ProxyOrganizationName")
        self.ProxyOperatorName = params.get("ProxyOperatorName")
        self.Module = params.get("Module")
        self.ModuleId = params.get("ModuleId")
        self.UniformSocialCreditCode = params.get("UniformSocialCreditCode")
        self.MenuStatus = params.get("MenuStatus")
        self.Endpoint = params.get("Endpoint")
        self.AutoJumpBackEvent = params.get("AutoJumpBackEvent")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.AuthorizationTypes = params.get("AuthorizationTypes")
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
        :param ConsoleUrl: 子客Web控制台url注意事项：
1. 所有类型的链接在企业未认证/员工未认证完成时，只要在有效期内（一年）都可以访问
2. 若企业认证完成且员工认证完成后，重新获取pc端的链接5分钟之内有效，且只能访问一次
3. 若企业认证完成且员工认证完成后，重新获取H5/APP的链接只要在有效期内（一年）都可以访问
4. 此链接仅单次有效，使用后需要再次创建新的链接（部分聊天软件，如企业微信默认会对链接进行解析，此时需要使用类似“代码片段”的方式或者放到txt文件里发送链接）
5. 创建的链接应避免被转义，如：&被转义为\u0026；如使用Postman请求后，请选择响应类型为 JSON，否则链接将被转义
        :type ConsoleUrl: str
        :param IsActivated: 渠道子客企业是否已开通腾讯电子签
        :type IsActivated: bool
        :param ProxyOperatorIsVerified: 当前经办人是否已认证（false:未认证 true:已认证）
        :type ProxyOperatorIsVerified: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ConsoleUrl = None
        self.IsActivated = None
        self.ProxyOperatorIsVerified = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ConsoleUrl = params.get("ConsoleUrl")
        self.IsActivated = params.get("IsActivated")
        self.ProxyOperatorIsVerified = params.get("ProxyOperatorIsVerified")
        self.RequestId = params.get("RequestId")


class CreateFlowsByTemplatesRequest(AbstractModel):
    """CreateFlowsByTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param FlowInfos: 多个合同（签署流程）信息，最多支持20个
        :type FlowInfos: list of FlowInfo
        :param NeedPreview: 是否为预览模式；默认为false，即非预览模式，此时发起合同并返回FlowIds；若为预览模式，不会发起合同，会返回PreviewUrls；
预览链接有效期300秒；
同时，如果预览的文件中指定了动态表格控件，需要进行异步合成；此时此接口返回的是合成前的文档预览链接，而合成完成后的文档预览链接会通过：回调通知的方式、或使用返回的TaskInfo中的TaskId通过ChannelGetTaskResultApi接口查询；
        :type NeedPreview: bool
        :param PreviewType: 预览链接类型 默认:0-文件流, 1- H5链接 注意:此参数在NeedPreview 为true 时有效,
        :type PreviewType: int
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.FlowInfos = None
        self.NeedPreview = None
        self.PreviewType = None
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
        self.NeedPreview = params.get("NeedPreview")
        self.PreviewType = params.get("PreviewType")
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
        :param PreviewUrls: 预览模式下返回的预览文件url数组
        :type PreviewUrls: list of str
        :param TaskInfos: 复杂文档合成任务（如，包含动态表格的预览任务）的任务信息数组；
如果文档需要异步合成，此字段会返回该异步任务的任务信息，后续可以通过ChannelGetTaskResultApi接口查询任务详情；
        :type TaskInfos: list of TaskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowIds = None
        self.CustomerData = None
        self.ErrorMessages = None
        self.PreviewUrls = None
        self.TaskInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowIds = params.get("FlowIds")
        self.CustomerData = params.get("CustomerData")
        self.ErrorMessages = params.get("ErrorMessages")
        self.PreviewUrls = params.get("PreviewUrls")
        if params.get("TaskInfos") is not None:
            self.TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = TaskInfo()
                obj._deserialize(item)
                self.TaskInfos.append(obj)
        self.RequestId = params.get("RequestId")


class CreateSealByImageRequest(AbstractModel):
    """CreateSealByImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param SealName: 印章名称，最大长度不超过50字符
        :type SealName: str
        :param SealImage: 印章图片base64，大小不超过10M（原始图片不超过7.6M）
        :type SealImage: str
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.SealName = None
        self.SealImage = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.SealName = params.get("SealName")
        self.SealImage = params.get("SealImage")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSealByImageResponse(AbstractModel):
    """CreateSealByImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param SealId: 印章id
        :type SealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SealId = params.get("SealId")
        self.RequestId = params.get("RequestId")


class CreateSignUrlsRequest(AbstractModel):
    """CreateSignUrls请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param FlowIds: 签署流程编号数组，最多支持100个。(备注：该参数和合同组编号必须二选一)
        :type FlowIds: list of str
        :param FlowGroupId: 合同组编号(备注：该参数和合同(流程)编号数组必须二选一)
        :type FlowGroupId: str
        :param Endpoint: 签署链接类型：“WEIXINAPP”-短链直接跳小程序；“CHANNEL”-跳转H5页面；“APP”-第三方APP或小程序跳转电子签小程序；"LONGURL2WEIXINAPP"-长链接跳转小程序；默认“WEIXINAPP”类型，即跳转至小程序；
        :type Endpoint: str
        :param GenerateType: 签署链接生成类型，默认是 "ALL"；
"ALL"：全部签署方签署链接，此时不会给自动签署的签署方创建签署链接；
"CHANNEL"：渠道合作企业；
"NOT_CHANNEL"：非渠道合作企业；
"PERSON"：个人；
"FOLLOWER"：关注方，目前是合同抄送方；
        :type GenerateType: str
        :param OrganizationName: 非渠道合作企业参与方的企业名称，GenerateType为"NOT_CHANNEL"时必填
        :type OrganizationName: str
        :param Name: 参与人姓名，GenerateType为"PERSON"时必填
        :type Name: str
        :param Mobile: 参与人手机号；
GenerateType为"PERSON"或"FOLLOWER"时必填
        :type Mobile: str
        :param OrganizationOpenId: 渠道合作企业的企业Id，GenerateType为"CHANNEL"时必填
        :type OrganizationOpenId: str
        :param OpenId: 渠道合作企业参与人OpenId，GenerateType为"CHANNEL"时可用，指定到具体参与人
        :type OpenId: str
        :param AutoJumpBack: Endpoint为"APP" 类型的签署链接，可以设置此值；支持调用方小程序打开签署链接，在电子签小程序完成签署后自动回跳至调用方小程序
        :type AutoJumpBack: bool
        :param JumpUrl: 签署完之后的H5页面的跳转链接，针对Endpoint为CHANNEL时有效，最大长度1000个字符。
        :type JumpUrl: str
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.FlowIds = None
        self.FlowGroupId = None
        self.Endpoint = None
        self.GenerateType = None
        self.OrganizationName = None
        self.Name = None
        self.Mobile = None
        self.OrganizationOpenId = None
        self.OpenId = None
        self.AutoJumpBack = None
        self.JumpUrl = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.FlowIds = params.get("FlowIds")
        self.FlowGroupId = params.get("FlowGroupId")
        self.Endpoint = params.get("Endpoint")
        self.GenerateType = params.get("GenerateType")
        self.OrganizationName = params.get("OrganizationName")
        self.Name = params.get("Name")
        self.Mobile = params.get("Mobile")
        self.OrganizationOpenId = params.get("OrganizationOpenId")
        self.OpenId = params.get("OpenId")
        self.AutoJumpBack = params.get("AutoJumpBack")
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
        


class CreateSignUrlsResponse(AbstractModel):
    """CreateSignUrls返回参数结构体

    """

    def __init__(self):
        r"""
        :param SignUrlInfos: 签署参与者签署H5链接信息数组
        :type SignUrlInfos: list of SignUrlInfo
        :param ErrorMessages: 生成失败时的错误信息，成功返回”“，顺序和出参SignUrlInfos保持一致
        :type ErrorMessages: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SignUrlInfos = None
        self.ErrorMessages = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SignUrlInfos") is not None:
            self.SignUrlInfos = []
            for item in params.get("SignUrlInfos"):
                obj = SignUrlInfo()
                obj._deserialize(item)
                self.SignUrlInfos.append(obj)
        self.ErrorMessages = params.get("ErrorMessages")
        self.RequestId = params.get("RequestId")


class Department(AbstractModel):
    """渠道版员工部门信息

    """

    def __init__(self):
        r"""
        :param DepartmentId: 部门id
注意：此字段可能返回 null，表示取不到有效值。
        :type DepartmentId: str
        :param DepartmentName: 部门名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DepartmentName: str
        """
        self.DepartmentId = None
        self.DepartmentName = None


    def _deserialize(self, params):
        self.DepartmentId = params.get("DepartmentId")
        self.DepartmentName = params.get("DepartmentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChannelFlowEvidenceReportRequest(AbstractModel):
    """DescribeChannelFlowEvidenceReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ReportId: 出证报告编号
        :type ReportId: str
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.ReportId = None
        self.Agent = None
        self.Operator = None


    def _deserialize(self, params):
        self.ReportId = params.get("ReportId")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChannelFlowEvidenceReportResponse(AbstractModel):
    """DescribeChannelFlowEvidenceReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReportUrl: 出证报告 URL
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportUrl: str
        :param Status: 执行中：EvidenceStatusExecuting
成功：EvidenceStatusSuccess
失败：EvidenceStatusFailed
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReportUrl = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReportUrl = params.get("ReportUrl")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeFlowDetailInfoRequest(AbstractModel):
    """DescribeFlowDetailInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param FlowIds: 合同(流程)编号数组，最多支持100个。
（备注：该参数和合同组编号必须二选一）
        :type FlowIds: list of str
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param FlowGroupId: 合同组编号（备注：该参数和合同(流程)编号数组必须二选一）
        :type FlowGroupId: str
        """
        self.Agent = None
        self.FlowIds = None
        self.Operator = None
        self.FlowGroupId = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.FlowIds = params.get("FlowIds")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowGroupId = params.get("FlowGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowDetailInfoResponse(AbstractModel):
    """DescribeFlowDetailInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 渠道侧应用号Id
        :type ApplicationId: str
        :param ProxyOrganizationOpenId: 渠道侧企业第三方Id
        :type ProxyOrganizationOpenId: str
        :param FlowInfo: 合同(签署流程)的具体详细描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowInfo: list of FlowDetailInfo
        :param FlowGroupId: 合同组编号
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowGroupId: str
        :param FlowGroupName: 合同组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowGroupName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ApplicationId = None
        self.ProxyOrganizationOpenId = None
        self.FlowInfo = None
        self.FlowGroupId = None
        self.FlowGroupName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ProxyOrganizationOpenId = params.get("ProxyOrganizationOpenId")
        if params.get("FlowInfo") is not None:
            self.FlowInfo = []
            for item in params.get("FlowInfo"):
                obj = FlowDetailInfo()
                obj._deserialize(item)
                self.FlowInfo.append(obj)
        self.FlowGroupId = params.get("FlowGroupId")
        self.FlowGroupName = params.get("FlowGroupName")
        self.RequestId = params.get("RequestId")


class DescribeResourceUrlsByFlowsRequest(AbstractModel):
    """DescribeResourceUrlsByFlows请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。
此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param FlowIds: 查询资源所对应的签署流程Id，最多支持50个
        :type FlowIds: list of str
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.FlowIds = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.FlowIds = params.get("FlowIds")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceUrlsByFlowsResponse(AbstractModel):
    """DescribeResourceUrlsByFlows返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowResourceUrlInfos: 签署流程资源对应链接信息
        :type FlowResourceUrlInfos: list of FlowResourceUrlInfo
        :param ErrorMessages: 创建消息，对应多个合同ID，
成功为“”,创建失败则对应失败消息
        :type ErrorMessages: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowResourceUrlInfos = None
        self.ErrorMessages = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FlowResourceUrlInfos") is not None:
            self.FlowResourceUrlInfos = []
            for item in params.get("FlowResourceUrlInfos"):
                obj = FlowResourceUrlInfo()
                obj._deserialize(item)
                self.FlowResourceUrlInfos.append(obj)
        self.ErrorMessages = params.get("ErrorMessages")
        self.RequestId = params.get("RequestId")


class DescribeTemplatesRequest(AbstractModel):
    """DescribeTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param TemplateId: 模板唯一标识，查询单个模板时使用
        :type TemplateId: str
        :param ContentType: 查询内容：0-模板列表及详情（默认），1-仅模板列表
        :type ContentType: int
        :param Limit: 查询个数，默认20，最大100；在查询列表的时候有效
        :type Limit: int
        :param Offset: 查询偏移位置，默认0；在查询列表的时候有效
        :type Offset: int
        :param QueryAllComponents: 是否返回所有组件信息。默认false，只返回发起方控件；true，返回所有签署方控件
        :type QueryAllComponents: bool
        :param TemplateName: 模糊搜索模板名称，最大长度200
        :type TemplateName: str
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param WithPreviewUrl: 是否获取模板预览链接
        :type WithPreviewUrl: bool
        :param WithPdfUrl: 是否获取模板的PDF文件链接-渠道版需要开启白名单时才能使用。
        :type WithPdfUrl: bool
        """
        self.Agent = None
        self.TemplateId = None
        self.ContentType = None
        self.Limit = None
        self.Offset = None
        self.QueryAllComponents = None
        self.TemplateName = None
        self.Operator = None
        self.WithPreviewUrl = None
        self.WithPdfUrl = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.TemplateId = params.get("TemplateId")
        self.ContentType = params.get("ContentType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.QueryAllComponents = params.get("QueryAllComponents")
        self.TemplateName = params.get("TemplateName")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.WithPreviewUrl = params.get("WithPreviewUrl")
        self.WithPdfUrl = params.get("WithPdfUrl")
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
        :param TotalCount: 查询总数
        :type TotalCount: int
        :param Limit: 查询数量
        :type Limit: int
        :param Offset: 查询起始偏移
        :type Offset: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Templates = None
        self.TotalCount = None
        self.Limit = None
        self.Offset = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = TemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.RequestId = params.get("RequestId")


class DescribeUsageRequest(AbstractModel):
    """DescribeUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 应用信息
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param StartDate: 开始时间，例如：2021-03-21
        :type StartDate: str
        :param EndDate: 结束时间，例如：2021-06-21；
开始时间到结束时间的区间长度小于等于90天。
        :type EndDate: str
        :param NeedAggregate: 是否汇总数据，默认不汇总。
不汇总：返回在统计区间内渠道下所有企业的每日明细，即每个企业N条数据，N为统计天数；
汇总：返回在统计区间内渠道下所有企业的汇总后数据，即每个企业一条数据；
        :type NeedAggregate: bool
        :param Limit: 单次返回的最多条目数量。默认为1000，且不能超过1000。
        :type Limit: int
        :param Offset: 偏移量，默认是0。
        :type Offset: int
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.StartDate = None
        self.EndDate = None
        self.NeedAggregate = None
        self.Limit = None
        self.Offset = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.NeedAggregate = params.get("NeedAggregate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
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


class DownloadFlowInfo(AbstractModel):
    """签署流程下载信息

    """

    def __init__(self):
        r"""
        :param FileName: 文件夹名称
        :type FileName: str
        :param FlowIdList: 签署流程的标识数组
        :type FlowIdList: list of str
        """
        self.FileName = None
        self.FlowIdList = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FlowIdList = params.get("FlowIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """此结构体 (Filter) 用于描述查询过滤条件。

    """

    def __init__(self):
        r"""
        :param Key: 查询过滤条件的Key
        :type Key: str
        :param Values: 查询过滤条件的Value列表
        :type Values: list of str
        """
        self.Key = None
        self.Values = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowApproverDetail(AbstractModel):
    """签署人的流程信息明细

    """

    def __init__(self):
        r"""
        :param ReceiptId: 模板配置时候的签署人id,与控件绑定
        :type ReceiptId: str
        :param ProxyOrganizationOpenId: 渠道侧企业的第三方id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyOrganizationOpenId: str
        :param ProxyOperatorOpenId: 渠道侧企业操作人的第三方id
        :type ProxyOperatorOpenId: str
        :param ProxyOrganizationName: 渠道侧企业名称
        :type ProxyOrganizationName: str
        :param Mobile: 签署人手机号
        :type Mobile: str
        :param SignOrder: 签署人签署顺序
        :type SignOrder: int
        :param ApproveName: 签署人姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveName: str
        :param ApproveStatus: 当前签署人的状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveStatus: str
        :param ApproveMessage: 签署人信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveMessage: str
        :param ApproveTime: 签署人签署时间
        :type ApproveTime: int
        :param ApproveType: 参与者类型 (ORGANIZATION企业/PERSON个人)
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveType: str
        """
        self.ReceiptId = None
        self.ProxyOrganizationOpenId = None
        self.ProxyOperatorOpenId = None
        self.ProxyOrganizationName = None
        self.Mobile = None
        self.SignOrder = None
        self.ApproveName = None
        self.ApproveStatus = None
        self.ApproveMessage = None
        self.ApproveTime = None
        self.ApproveType = None


    def _deserialize(self, params):
        self.ReceiptId = params.get("ReceiptId")
        self.ProxyOrganizationOpenId = params.get("ProxyOrganizationOpenId")
        self.ProxyOperatorOpenId = params.get("ProxyOperatorOpenId")
        self.ProxyOrganizationName = params.get("ProxyOrganizationName")
        self.Mobile = params.get("Mobile")
        self.SignOrder = params.get("SignOrder")
        self.ApproveName = params.get("ApproveName")
        self.ApproveStatus = params.get("ApproveStatus")
        self.ApproveMessage = params.get("ApproveMessage")
        self.ApproveTime = params.get("ApproveTime")
        self.ApproveType = params.get("ApproveType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowApproverInfo(AbstractModel):
    """创建签署流程签署人入参。

    其中签署方FlowApproverInfo需要传递的参数
    非单C、单B、B2C合同，ApproverType、RecipientId（模板发起合同时）必传，建议都传。其他身份标识
    1-个人：Name、Mobile必传
    2-渠道子客企业指定经办人：OpenId必传，OrgName必传、OrgOpenId必传；
    3-渠道合作企业不指定经办人：（暂不支持）
    4-非渠道合作企业：Name、Mobile必传，OrgName必传，且NotChannelOrganization=True。

    RecipientId参数：
    从DescribeTemplates接口中，可以得到模板下的签署方Recipient列表，根据模板自定义的Rolename在此结构体中确定其RecipientId

    """

    def __init__(self):
        r"""
        :param Name: 签署人姓名，最大长度50个字符
        :type Name: str
        :param IdCardType: 签署人身份证件类型
1.ID_CARD 居民身份证
2.HONGKONG_MACAO_AND_TAIWAN 港澳台居民居住证
3.HONGKONG_AND_MACAO 港澳居民来往内地通行证
        :type IdCardType: str
        :param IdCardNumber: 签署人证件号
        :type IdCardNumber: str
        :param Mobile: 签署人手机号，脱敏显示。大陆手机号为11位，暂不支持海外手机号。
        :type Mobile: str
        :param OrganizationName: 企业签署方工商营业执照上的企业名称，签署方为非发起方企业场景下必传，最大长度64个字符；
        :type OrganizationName: str
        :param NotChannelOrganization: 指定签署人非渠道企业下员工，在ApproverType为ORGANIZATION时指定。
默认为false，即签署人位于同一个渠道应用号下；
        :type NotChannelOrganization: bool
        :param OpenId: 用户侧第三方id，最大长度64个字符
当签署方为同一渠道下的员工时，该字段若不指定，则发起【待领取】的流程
        :type OpenId: str
        :param OrganizationOpenId: 企业签署方在同一渠道下的其他合作企业OpenId，签署方为非发起方企业场景下必传，最大长度64个字符；
        :type OrganizationOpenId: str
        :param ApproverType: 签署人类型，PERSON-个人；
PERSON_AUTO_SIGN-个人自动签；
ORGANIZATION-企业；
ENTERPRISESERVER-企业静默签;
注：ENTERPRISESERVER 类型仅用于使用文件创建签署流程（ChannelCreateFlowByFiles）接口；
        :type ApproverType: str
        :param RecipientId: 签署流程签署人在模板中对应的签署人Id；在非单方签署、以及非B2C签署的场景下必传，用于指定当前签署方在签署流程中的位置；
        :type RecipientId: str
        :param Deadline: 签署截止时间，默认一年
        :type Deadline: int
        :param CallbackUrl: 签署完回调url，最大长度1000个字符
        :type CallbackUrl: str
        :param SignComponents: 使用PDF文件直接发起合同时，签署人指定的签署控件
        :type SignComponents: list of Component
        :param ComponentLimitType: 个人签署方指定签署控件类型，目前仅支持：OCR_ESIGN(AI智慧手写签名)
        :type ComponentLimitType: list of str
        :param PreReadTime: 合同的强制预览时间：3~300s，未指定则按合同页数计算
        :type PreReadTime: int
        :param JumpUrl: 签署完前端跳转的url，暂未使用
        :type JumpUrl: str
        :param ApproverOption: 签署人个性化能力值
        :type ApproverOption: :class:`tencentcloud.essbasic.v20210526.models.ApproverOption`
        :param ApproverNeedSignReview: 当前签署方进行签署操作是否需要企业内部审批，true 则为需要
        :type ApproverNeedSignReview: bool
        """
        self.Name = None
        self.IdCardType = None
        self.IdCardNumber = None
        self.Mobile = None
        self.OrganizationName = None
        self.NotChannelOrganization = None
        self.OpenId = None
        self.OrganizationOpenId = None
        self.ApproverType = None
        self.RecipientId = None
        self.Deadline = None
        self.CallbackUrl = None
        self.SignComponents = None
        self.ComponentLimitType = None
        self.PreReadTime = None
        self.JumpUrl = None
        self.ApproverOption = None
        self.ApproverNeedSignReview = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.IdCardType = params.get("IdCardType")
        self.IdCardNumber = params.get("IdCardNumber")
        self.Mobile = params.get("Mobile")
        self.OrganizationName = params.get("OrganizationName")
        self.NotChannelOrganization = params.get("NotChannelOrganization")
        self.OpenId = params.get("OpenId")
        self.OrganizationOpenId = params.get("OrganizationOpenId")
        self.ApproverType = params.get("ApproverType")
        self.RecipientId = params.get("RecipientId")
        self.Deadline = params.get("Deadline")
        self.CallbackUrl = params.get("CallbackUrl")
        if params.get("SignComponents") is not None:
            self.SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self.SignComponents.append(obj)
        self.ComponentLimitType = params.get("ComponentLimitType")
        self.PreReadTime = params.get("PreReadTime")
        self.JumpUrl = params.get("JumpUrl")
        if params.get("ApproverOption") is not None:
            self.ApproverOption = ApproverOption()
            self.ApproverOption._deserialize(params.get("ApproverOption"))
        self.ApproverNeedSignReview = params.get("ApproverNeedSignReview")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowDetailInfo(AbstractModel):
    """此结构体(FlowDetailInfo)描述的是合同(流程)的详细信息

    """

    def __init__(self):
        r"""
        :param FlowId: 合同(流程)的Id
        :type FlowId: str
        :param FlowName: 合同(流程)的名字
        :type FlowName: str
        :param FlowType: 合同(流程)的类型
        :type FlowType: str
        :param FlowStatus: 合同(流程)的状态
        :type FlowStatus: str
        :param FlowMessage: 合同(流程)的信息
        :type FlowMessage: str
        :param CreateOn: 合同(流程)的创建时间戳
        :type CreateOn: int
        :param DeadLine: 合同(流程)的签署截止时间戳
        :type DeadLine: int
        :param CustomData: 用户自定义数据
        :type CustomData: str
        :param FlowApproverInfos: 合同(流程)的签署人数组
        :type FlowApproverInfos: list of FlowApproverDetail
        """
        self.FlowId = None
        self.FlowName = None
        self.FlowType = None
        self.FlowStatus = None
        self.FlowMessage = None
        self.CreateOn = None
        self.DeadLine = None
        self.CustomData = None
        self.FlowApproverInfos = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.FlowName = params.get("FlowName")
        self.FlowType = params.get("FlowType")
        self.FlowStatus = params.get("FlowStatus")
        self.FlowMessage = params.get("FlowMessage")
        self.CreateOn = params.get("CreateOn")
        self.DeadLine = params.get("DeadLine")
        self.CustomData = params.get("CustomData")
        if params.get("FlowApproverInfos") is not None:
            self.FlowApproverInfos = []
            for item in params.get("FlowApproverInfos"):
                obj = FlowApproverDetail()
                obj._deserialize(item)
                self.FlowApproverInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowFileInfo(AbstractModel):
    """合同组中每个子合同的发起信息

    """

    def __init__(self):
        r"""
        :param FileIds: 签署文件资源Id列表，目前仅支持单个文件
        :type FileIds: list of str
        :param FlowName: 签署流程名称，长度不超过200个字符
        :type FlowName: str
        :param FlowApprovers: 签署流程签约方列表，最多不超过5个参与方
        :type FlowApprovers: list of FlowApproverInfo
        :param Deadline: 签署流程截止时间，十位数时间戳，最大值为33162419560，即3020年
        :type Deadline: int
        :param FlowDescription: 签署流程的描述，长度不超过1000个字符
        :type FlowDescription: str
        :param FlowType: 签署流程的类型，长度不超过255个字符
        :type FlowType: str
        :param CallbackUrl: 签署流程回调地址，长度不超过255个字符
        :type CallbackUrl: str
        :param CustomerData: 渠道的业务信息，最大长度1000个字符。发起自动签署时，需设置对应自动签署场景，目前仅支持场景：处方单-E_PRESCRIPTION_AUTO_SIGN
        :type CustomerData: str
        :param Unordered: 合同签署顺序类型(无序签,顺序签)，默认为false，即有序签署
        :type Unordered: bool
        :param CustomShowMap: 合同显示的页卡模板，说明：只支持{合同名称}, {发起方企业}, {发起方姓名}, {签署方N企业}, {签署方N姓名}，且N不能超过签署人的数量，N从1开始
        :type CustomShowMap: str
        :param NeedSignReview: 本企业(发起方企业)是否需要签署审批
        :type NeedSignReview: bool
        """
        self.FileIds = None
        self.FlowName = None
        self.FlowApprovers = None
        self.Deadline = None
        self.FlowDescription = None
        self.FlowType = None
        self.CallbackUrl = None
        self.CustomerData = None
        self.Unordered = None
        self.CustomShowMap = None
        self.NeedSignReview = None


    def _deserialize(self, params):
        self.FileIds = params.get("FileIds")
        self.FlowName = params.get("FlowName")
        if params.get("FlowApprovers") is not None:
            self.FlowApprovers = []
            for item in params.get("FlowApprovers"):
                obj = FlowApproverInfo()
                obj._deserialize(item)
                self.FlowApprovers.append(obj)
        self.Deadline = params.get("Deadline")
        self.FlowDescription = params.get("FlowDescription")
        self.FlowType = params.get("FlowType")
        self.CallbackUrl = params.get("CallbackUrl")
        self.CustomerData = params.get("CustomerData")
        self.Unordered = params.get("Unordered")
        self.CustomShowMap = params.get("CustomShowMap")
        self.NeedSignReview = params.get("NeedSignReview")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowInfo(AbstractModel):
    """此结构体 (FlowInfo) 用于描述签署流程信息。

    【动态表格传参说明】
    当模板的 ComponentType='DYNAMIC_TABLE'时（渠道版或集成版），FormField.ComponentValue需要传递json格式的字符串参数，用于确定表头&填充动态表格（支持内容的单元格合并）
    输入示例1：

    ```
    {
        "headers":[
            {
                "content":"head1"
            },
            {
                "content":"head2"
            },
            {
                "content":"head3"
            }
        ],
        "rowCount":3,
        "body":{
            "cells":[
                {
                    "rowStart":1,
                    "rowEnd":1,
                    "columnStart":1,
                    "columnEnd":1,
                    "content":"123"
                },
                {
                    "rowStart":2,
                    "rowEnd":3,
                    "columnStart":1,
                    "columnEnd":2,
                    "content":"456"
                },
                {
                    "rowStart":3,
                    "rowEnd":3,
                    "columnStart":3,
                    "columnEnd":3,
                    "content":"789"
                }
            ]
        }
    }

    ```

    输入示例2（表格表头宽度比例配置）：

    ```
    {
        "headers":[
            {
                "content":"head1",
                "widthPercent": 30
            },
            {
                "content":"head2",
                "widthPercent": 30
            },
            {
                "content":"head3",
                "widthPercent": 40
            }
        ],
        "rowCount":3,
        "body":{
            "cells":[
                {
                    "rowStart":1,
                    "rowEnd":1,
                    "columnStart":1,
                    "columnEnd":1,
                    "content":"123"
                },
                {
                    "rowStart":2,
                    "rowEnd":3,
                    "columnStart":1,
                    "columnEnd":2,
                    "content":"456"
                },
                {
                    "rowStart":3,
                    "rowEnd":3,
                    "columnStart":3,
                    "columnEnd":3,
                    "content":"789"
                }
            ]
        }
    }

    ```
    表格参数说明

    | 名称                | 类型    | 描述                                              |
    | ------------------- | ------- | ------------------------------------------------- |
    | headers             | Array   | 表头：不超过10列，不支持单元格合并，字数不超过100 |
    | rowCount            | Integer | 表格内容最大行数                                  |
    | cells.N.rowStart    | Integer | 单元格坐标：行起始index                           |
    | cells.N.rowEnd      | Integer | 单元格坐标：行结束index                           |
    | cells.N.columnStart | Integer | 单元格坐标：列起始index                           |
    | cells.N.columnEnd   | Integer | 单元格坐标：列结束index                           |
    | cells.N.content     | String  | 单元格内容，字数不超过100                         |

    表格参数headers说明

    | 名称                | 类型    | 描述                                              |
    | ------------------- | ------- | ------------------------------------------------- |
    | widthPercent   | Integer | 表头单元格列占总表头的比例，例如1：30表示 此列占表头的30%，不填写时列宽度平均拆分；例如2：总2列，某一列填写40，剩余列可以为空，按照60计算。；例如3：总3列，某一列填写30，剩余2列可以为空，分别为(100-30)/2=35                    |
    | content    | String  | 表头单元格内容，字数不超过100                         |

    """

    def __init__(self):
        r"""
        :param FlowName: 合同名字，最大长度200个字符
        :type FlowName: str
        :param Deadline: 签署截止时间戳，超过有效签署时间则该签署流程失败，默认一年
        :type Deadline: int
        :param TemplateId: 模板ID
        :type TemplateId: str
        :param FlowApprovers: 多个签署人信息，最大支持50个签署方
        :type FlowApprovers: list of FlowApproverInfo
        :param FormFields: 表单K-V对列表
        :type FormFields: list of FormField
        :param CallbackUrl: 回调地址，最大长度1000个字符
        :type CallbackUrl: str
        :param FlowType: 合同类型，如：1. “劳务”；2. “销售”；3. “租赁”；4. “其他”，最大长度200个字符
        :type FlowType: str
        :param FlowDescription: 合同描述，最大长度1000个字符
        :type FlowDescription: str
        :param CustomerData: 渠道的业务信息，最大长度1000个字符。发起自动签署时，需设置对应自动签署场景，目前仅支持场景：处方单-E_PRESCRIPTION_AUTO_SIGN
        :type CustomerData: str
        :param CustomShowMap: 合同显示的页卡模板，说明：只支持{合同名称}, {发起方企业}, {发起方姓名}, {签署方N企业}, {签署方N姓名}，且N不能超过签署人的数量，N从1开始
        :type CustomShowMap: str
        :param CcInfos: 被抄送人的信息列表，抄送功能暂不开放
        :type CcInfos: list of CcInfo
        :param NeedSignReview: 发起方企业的签署人进行签署操作是否需要企业内部审批。
若设置为true,审核结果需通过接口 ChannelCreateFlowSignReview 通知电子签，审核通过后，发起方企业签署人方可进行签署操作，否则会阻塞其签署操作。

注：企业可以通过此功能与企业内部的审批流程进行关联，支持手动、静默签署合同。
        :type NeedSignReview: bool
        """
        self.FlowName = None
        self.Deadline = None
        self.TemplateId = None
        self.FlowApprovers = None
        self.FormFields = None
        self.CallbackUrl = None
        self.FlowType = None
        self.FlowDescription = None
        self.CustomerData = None
        self.CustomShowMap = None
        self.CcInfos = None
        self.NeedSignReview = None


    def _deserialize(self, params):
        self.FlowName = params.get("FlowName")
        self.Deadline = params.get("Deadline")
        self.TemplateId = params.get("TemplateId")
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
        self.CallbackUrl = params.get("CallbackUrl")
        self.FlowType = params.get("FlowType")
        self.FlowDescription = params.get("FlowDescription")
        self.CustomerData = params.get("CustomerData")
        self.CustomShowMap = params.get("CustomShowMap")
        if params.get("CcInfos") is not None:
            self.CcInfos = []
            for item in params.get("CcInfos"):
                obj = CcInfo()
                obj._deserialize(item)
                self.CcInfos.append(obj)
        self.NeedSignReview = params.get("NeedSignReview")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowResourceUrlInfo(AbstractModel):
    """流程对应资源链接信息

    """

    def __init__(self):
        r"""
        :param FlowId: 流程对应Id
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: str
        :param ResourceUrlInfos: 流程对应资源链接信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceUrlInfos: list of ResourceUrlInfo
        """
        self.FlowId = None
        self.ResourceUrlInfos = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("ResourceUrlInfos") is not None:
            self.ResourceUrlInfos = []
            for item in params.get("ResourceUrlInfos"):
                obj = ResourceUrlInfo()
                obj._deserialize(item)
                self.ResourceUrlInfos.append(obj)
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
        :param ComponentValue: 控件填充vaule，ComponentType和传入值类型对应关系：
TEXT - 文本内容
MULTI_LINE_TEXT - 文本内容
CHECK_BOX - true/false
FILL_IMAGE、ATTACHMENT - 附件的FileId，需要通过UploadFiles接口上传获取
SELECTOR - 选项值
DYNAMIC_TABLE - 传入json格式的表格内容，具体见数据结构FlowInfo：https://cloud.tencent.com/document/api/1420/61525#FlowInfo
        :type ComponentValue: str
        :param ComponentId: 表单域或控件的ID，跟ComponentName二选一，不能全为空；
CreateFlowsByTemplates 接口不使用此字段。
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
        


class GetDownloadFlowUrlRequest(AbstractModel):
    """GetDownloadFlowUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param DownLoadFlows: 文件夹数组，签署流程总数不能超过50个，一个文件夹下，不能超过20个签署流程
        :type DownLoadFlows: list of DownloadFlowInfo
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.DownLoadFlows = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        if params.get("DownLoadFlows") is not None:
            self.DownLoadFlows = []
            for item in params.get("DownLoadFlows"):
                obj = DownloadFlowInfo()
                obj._deserialize(item)
                self.DownLoadFlows.append(obj)
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDownloadFlowUrlResponse(AbstractModel):
    """GetDownloadFlowUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownLoadUrl: 合同（流程）下载地址
        :type DownLoadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownLoadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownLoadUrl = params.get("DownLoadUrl")
        self.RequestId = params.get("RequestId")


class OccupiedSeal(AbstractModel):
    """持有的电子印章信息

    """

    def __init__(self):
        r"""
        :param SealId: 电子印章编号
        :type SealId: str
        :param SealName: 电子印章名称
        :type SealName: str
        :param CreateOn: 电子印章授权时间戳
        :type CreateOn: int
        :param Creator: 电子印章授权人
        :type Creator: str
        :param SealPolicyId: 电子印章策略Id
        :type SealPolicyId: str
        :param SealStatus: 印章状态，有以下六种：CHECKING（审核中）SUCCESS（已启用）FAIL（审核拒绝）CHECKING-SADM（待超管审核）DISABLE（已停用）STOPPED（已终止）
        :type SealStatus: str
        :param FailReason: 审核失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param Url: 印章图片url，5分钟内有效
        :type Url: str
        :param SealType: 印章类型
        :type SealType: str
        :param IsAllTime: 用印申请是否为永久授权
        :type IsAllTime: bool
        :param AuthorizedUsers: 授权人列表
        :type AuthorizedUsers: list of AuthorizedUser
        """
        self.SealId = None
        self.SealName = None
        self.CreateOn = None
        self.Creator = None
        self.SealPolicyId = None
        self.SealStatus = None
        self.FailReason = None
        self.Url = None
        self.SealType = None
        self.IsAllTime = None
        self.AuthorizedUsers = None


    def _deserialize(self, params):
        self.SealId = params.get("SealId")
        self.SealName = params.get("SealName")
        self.CreateOn = params.get("CreateOn")
        self.Creator = params.get("Creator")
        self.SealPolicyId = params.get("SealPolicyId")
        self.SealStatus = params.get("SealStatus")
        self.FailReason = params.get("FailReason")
        self.Url = params.get("Url")
        self.SealType = params.get("SealType")
        self.IsAllTime = params.get("IsAllTime")
        if params.get("AuthorizedUsers") is not None:
            self.AuthorizedUsers = []
            for item in params.get("AuthorizedUsers"):
                obj = AuthorizedUser()
                obj._deserialize(item)
                self.AuthorizedUsers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperateChannelTemplateRequest(AbstractModel):
    """OperateChannelTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param OperateType: 操作类型，查询:"SELECT"，删除:"DELETE"，更新:"UPDATE"
        :type OperateType: str
        :param TemplateId: 渠道方模板库模板唯一标识
        :type TemplateId: str
        :param ProxyOrganizationOpenIds: 合作企业方第三方机构唯一标识数据，支持多个， 用","进行分隔
        :type ProxyOrganizationOpenIds: str
        :param AuthTag: 模板可见性, 全部可见-"all", 部分可见-"part"
        :type AuthTag: str
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.OperateType = None
        self.TemplateId = None
        self.ProxyOrganizationOpenIds = None
        self.AuthTag = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.OperateType = params.get("OperateType")
        self.TemplateId = params.get("TemplateId")
        self.ProxyOrganizationOpenIds = params.get("ProxyOrganizationOpenIds")
        self.AuthTag = params.get("AuthTag")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperateChannelTemplateResponse(AbstractModel):
    """OperateChannelTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param AppId: 腾讯电子签颁发给渠道的应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param TemplateId: 渠道方模板库模板唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param OperateResult: 全部成功-"all-success",部分成功-"part-success", 全部失败-"fail"失败的会在FailMessageList中展示
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateResult: str
        :param AuthTag: 模板可见性, 全部可见-"all", 部分可见-"part"
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthTag: str
        :param ProxyOrganizationOpenIds: 合作企业方第三方机构唯一标识数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyOrganizationOpenIds: list of str
        :param FailMessageList: 操作失败信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type FailMessageList: list of AuthFailMessage
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppId = None
        self.TemplateId = None
        self.OperateResult = None
        self.AuthTag = None
        self.ProxyOrganizationOpenIds = None
        self.FailMessageList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.TemplateId = params.get("TemplateId")
        self.OperateResult = params.get("OperateResult")
        self.AuthTag = params.get("AuthTag")
        self.ProxyOrganizationOpenIds = params.get("ProxyOrganizationOpenIds")
        if params.get("FailMessageList") is not None:
            self.FailMessageList = []
            for item in params.get("FailMessageList"):
                obj = AuthFailMessage()
                obj._deserialize(item)
                self.FailMessageList.append(obj)
        self.RequestId = params.get("RequestId")


class OrganizationInfo(AbstractModel):
    """机构信息

    """

    def __init__(self):
        r"""
        :param OrganizationOpenId: 用户在渠道的机构编号
        :type OrganizationOpenId: str
        :param ClientIp: 用户真实的IP
        :type ClientIp: str
        :param ProxyIp: 机构的代理IP
        :type ProxyIp: str
        :param OrganizationId: 机构在平台的编号
        :type OrganizationId: str
        :param Channel: 用户渠道
        :type Channel: str
        """
        self.OrganizationOpenId = None
        self.ClientIp = None
        self.ProxyIp = None
        self.OrganizationId = None
        self.Channel = None


    def _deserialize(self, params):
        self.OrganizationOpenId = params.get("OrganizationOpenId")
        self.ClientIp = params.get("ClientIp")
        self.ProxyIp = params.get("ProxyIp")
        self.OrganizationId = params.get("OrganizationId")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PdfVerifyResult(AbstractModel):
    """合同文件验签单个结果结构体

    """

    def __init__(self):
        r"""
        :param VerifyResult: 验签结果
        :type VerifyResult: int
        :param SignPlatform: 签署平台
        :type SignPlatform: str
        :param SignerName: 签署人名称
        :type SignerName: str
        :param SignTime: 签署时间
        :type SignTime: int
        :param SignAlgorithm: 签名算法
        :type SignAlgorithm: str
        :param CertSn: 签名证书序列号
        :type CertSn: str
        :param CertNotBefore: 证书起始时间
        :type CertNotBefore: int
        :param CertNotAfter: 证书过期时间
        :type CertNotAfter: int
        :param SignType: 签名类型
        :type SignType: int
        :param ComponentPosX: 签名域横坐标
        :type ComponentPosX: float
        :param ComponentPosY: 签名域纵坐标
        :type ComponentPosY: float
        :param ComponentWidth: 签名域宽度
        :type ComponentWidth: float
        :param ComponentHeight: 签名域高度
        :type ComponentHeight: float
        :param ComponentPage: 签名域所在页码
        :type ComponentPage: int
        """
        self.VerifyResult = None
        self.SignPlatform = None
        self.SignerName = None
        self.SignTime = None
        self.SignAlgorithm = None
        self.CertSn = None
        self.CertNotBefore = None
        self.CertNotAfter = None
        self.SignType = None
        self.ComponentPosX = None
        self.ComponentPosY = None
        self.ComponentWidth = None
        self.ComponentHeight = None
        self.ComponentPage = None


    def _deserialize(self, params):
        self.VerifyResult = params.get("VerifyResult")
        self.SignPlatform = params.get("SignPlatform")
        self.SignerName = params.get("SignerName")
        self.SignTime = params.get("SignTime")
        self.SignAlgorithm = params.get("SignAlgorithm")
        self.CertSn = params.get("CertSn")
        self.CertNotBefore = params.get("CertNotBefore")
        self.CertNotAfter = params.get("CertNotAfter")
        self.SignType = params.get("SignType")
        self.ComponentPosX = params.get("ComponentPosX")
        self.ComponentPosY = params.get("ComponentPosY")
        self.ComponentWidth = params.get("ComponentWidth")
        self.ComponentHeight = params.get("ComponentHeight")
        self.ComponentPage = params.get("ComponentPage")
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
        :param Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param FlowInfos: 多个合同（签署流程）信息，最大支持20个签署流程。
        :type FlowInfos: list of FlowInfo
        :param JumpUrl: 操作完成后的跳转地址，最大长度200
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
        :param Id: 对应Agent-ProxyOperator-OpenId。渠道平台自定义，对渠道子客企业员的唯一标识。一个OpenId在一个子客企业内唯一对应一个真实员工，不可在其他子客企业内重复使用。（比如，可以使用经办人企业名+员工身份证的hash值，需要渠道平台保存），最大64位字符串
        :type Id: str
        :param Name: 经办人姓名，最大长度50个字符
        :type Name: str
        :param IdCardType: 经办人身份证件类型
1.ID_CARD 居民身份证
2.HONGKONG_MACAO_AND_TAIWAN 港澳台居民居住证
3.HONGKONG_AND_MACAO 港澳居民来往内地通行证
        :type IdCardType: str
        :param IdCardNumber: 经办人证件号
        :type IdCardNumber: str
        :param Mobile: 经办人手机号，大陆手机号输入11位，暂不支持海外手机号。
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
        :param IsPromoter: 是否是发起方
        :type IsPromoter: bool
        """
        self.RecipientId = None
        self.RecipientType = None
        self.Description = None
        self.RoleName = None
        self.RequireValidation = None
        self.RequireSign = None
        self.SignType = None
        self.RoutingOrder = None
        self.IsPromoter = None


    def _deserialize(self, params):
        self.RecipientId = params.get("RecipientId")
        self.RecipientType = params.get("RecipientType")
        self.Description = params.get("Description")
        self.RoleName = params.get("RoleName")
        self.RequireValidation = params.get("RequireValidation")
        self.RequireSign = params.get("RequireSign")
        self.SignType = params.get("SignType")
        self.RoutingOrder = params.get("RoutingOrder")
        self.IsPromoter = params.get("IsPromoter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleasedApprover(AbstractModel):
    """解除协议的签署人，如不指定，默认使用待解除流程（即原流程）中的签署人。
    注意：不支持更换C端（个人身份类型）签署人，如果原流程中含有C端签署人，默认使用原流程中的该签署人。

    如果需要指定B端（机构身份类型）签署人，其中ReleasedApprover需要传递的参数如下：
    ApproverNumber, OrganizationName, ApproverType必传。
    对于其他身份标识
    - 渠道子客企业指定经办人：OpenId必传，OrganizationOpenId必传；
    - 非渠道合作企业：Name、Mobile必传。

    """

    def __init__(self):
        r"""
        :param OrganizationName: 企业签署方工商营业执照上的企业名称，签署方为非发起方企业场景下必传，最大长度64个字符
        :type OrganizationName: str
        :param ApproverNumber: 签署人在原流程中的签署人列表中的顺序序号（从0开始，按顺序依次递增），如果不清楚原流程中的签署人列表，可以通过DescribeFlows接口查看
        :type ApproverNumber: int
        :param ApproverType: 签署人类型，目前仅支持
ORGANIZATION-企业
        :type ApproverType: str
        :param Name: 签署人姓名，最大长度50个字符
        :type Name: str
        :param IdCardType: 签署人身份证件类型
1.ID_CARD 居民身份证
2.HONGKONG_MACAO_AND_TAIWAN 港澳台居民居住证
3.HONGKONG_AND_MACAO 港澳居民来往内地通行证
        :type IdCardType: str
        :param IdCardNumber: 签署人证件号
        :type IdCardNumber: str
        :param Mobile: 签署人手机号，脱敏显示。大陆手机号为11位，暂不支持海外手机号
        :type Mobile: str
        :param OrganizationOpenId: 企业签署方在同一渠道下的其他合作企业OpenId，签署方为非发起方企业场景下必传，最大长度64个字符
        :type OrganizationOpenId: str
        :param OpenId: 用户侧第三方id，最大长度64个字符
当签署方为同一渠道下的员工时，该字必传
        :type OpenId: str
        """
        self.OrganizationName = None
        self.ApproverNumber = None
        self.ApproverType = None
        self.Name = None
        self.IdCardType = None
        self.IdCardNumber = None
        self.Mobile = None
        self.OrganizationOpenId = None
        self.OpenId = None


    def _deserialize(self, params):
        self.OrganizationName = params.get("OrganizationName")
        self.ApproverNumber = params.get("ApproverNumber")
        self.ApproverType = params.get("ApproverType")
        self.Name = params.get("Name")
        self.IdCardType = params.get("IdCardType")
        self.IdCardNumber = params.get("IdCardNumber")
        self.Mobile = params.get("Mobile")
        self.OrganizationOpenId = params.get("OrganizationOpenId")
        self.OpenId = params.get("OpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelieveInfo(AbstractModel):
    """解除协议文档中内容信息，包括但不限于：解除理由、解除后仍然有效的条款-保留条款、原合同事项处理-费用结算、原合同事项处理-其他事项、其他约定等。

    """

    def __init__(self):
        r"""
        :param Reason: 解除理由，最大支持200个字
        :type Reason: str
        :param RemainInForceItem: 解除后仍然有效的条款，保留条款，最大支持200个字
        :type RemainInForceItem: str
        :param OriginalExpenseSettlement: 原合同事项处理-费用结算，最大支持200个字
        :type OriginalExpenseSettlement: str
        :param OriginalOtherSettlement: 原合同事项处理-其他事项，最大支持200个字
        :type OriginalOtherSettlement: str
        :param OtherDeals: 其他约定，最大支持200个字
        :type OtherDeals: str
        """
        self.Reason = None
        self.RemainInForceItem = None
        self.OriginalExpenseSettlement = None
        self.OriginalOtherSettlement = None
        self.OtherDeals = None


    def _deserialize(self, params):
        self.Reason = params.get("Reason")
        self.RemainInForceItem = params.get("RemainInForceItem")
        self.OriginalExpenseSettlement = params.get("OriginalExpenseSettlement")
        self.OriginalOtherSettlement = params.get("OriginalOtherSettlement")
        self.OtherDeals = params.get("OtherDeals")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceUrlInfo(AbstractModel):
    """资源链接信息

    """

    def __init__(self):
        r"""
        :param Url: 资源链接地址，过期时间5分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param Name: 资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Type: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.Url = None
        self.Name = None
        self.Type = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignQrCode(AbstractModel):
    """一码多扫签署二维码对象

    """

    def __init__(self):
        r"""
        :param QrCodeId: 二维码id
        :type QrCodeId: str
        :param QrCodeUrl: 二维码url
        :type QrCodeUrl: str
        :param ExpiredTime: 二维码过期时间
        :type ExpiredTime: int
        """
        self.QrCodeId = None
        self.QrCodeUrl = None
        self.ExpiredTime = None


    def _deserialize(self, params):
        self.QrCodeId = params.get("QrCodeId")
        self.QrCodeUrl = params.get("QrCodeUrl")
        self.ExpiredTime = params.get("ExpiredTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignUrl(AbstractModel):
    """一码多扫签署二维码签署信息

    """

    def __init__(self):
        r"""
        :param AppSignUrl: 小程序签署链接
        :type AppSignUrl: str
        :param EffectiveTime: 签署链接有效时间
        :type EffectiveTime: str
        :param HttpSignUrl: 移动端签署链接
        :type HttpSignUrl: str
        """
        self.AppSignUrl = None
        self.EffectiveTime = None
        self.HttpSignUrl = None


    def _deserialize(self, params):
        self.AppSignUrl = params.get("AppSignUrl")
        self.EffectiveTime = params.get("EffectiveTime")
        self.HttpSignUrl = params.get("HttpSignUrl")
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
        :param SignUrl: 签署链接，过期时间为30天
注意：此字段可能返回 null，表示取不到有效值。
        :type SignUrl: str
        :param Deadline: 合同过期时间
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
        :param FlowGroupId: 合同组签署链接对应的合同组id
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowGroupId: str
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
        self.FlowGroupId = None


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
        self.FlowGroupId = params.get("FlowGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Staff(AbstractModel):
    """企业员工信息

    """

    def __init__(self):
        r"""
        :param UserId: 员工在电子签平台的id
        :type UserId: str
        :param DisplayName: 显示的员工名
        :type DisplayName: str
        :param Mobile: 员工手机号
        :type Mobile: str
        :param Email: 员工邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param OpenId: 员工在第三方平台id
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param Roles: 员工角色
注意：此字段可能返回 null，表示取不到有效值。
        :type Roles: list of StaffRole
        :param Department: 员工部门
注意：此字段可能返回 null，表示取不到有效值。
        :type Department: :class:`tencentcloud.essbasic.v20210526.models.Department`
        :param Verified: 员工是否实名
        :type Verified: bool
        :param CreatedOn: 员工创建时间戳
        :type CreatedOn: int
        :param VerifiedOn: 员工实名时间戳
        :type VerifiedOn: int
        """
        self.UserId = None
        self.DisplayName = None
        self.Mobile = None
        self.Email = None
        self.OpenId = None
        self.Roles = None
        self.Department = None
        self.Verified = None
        self.CreatedOn = None
        self.VerifiedOn = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.DisplayName = params.get("DisplayName")
        self.Mobile = params.get("Mobile")
        self.Email = params.get("Email")
        self.OpenId = params.get("OpenId")
        if params.get("Roles") is not None:
            self.Roles = []
            for item in params.get("Roles"):
                obj = StaffRole()
                obj._deserialize(item)
                self.Roles.append(obj)
        if params.get("Department") is not None:
            self.Department = Department()
            self.Department._deserialize(params.get("Department"))
        self.Verified = params.get("Verified")
        self.CreatedOn = params.get("CreatedOn")
        self.VerifiedOn = params.get("VerifiedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffRole(AbstractModel):
    """渠道版员工角色信息

    """

    def __init__(self):
        r"""
        :param RoleId: 角色id
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleId: str
        :param RoleName: 角色名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleName: str
        """
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
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
        :param Agent: 渠道应用相关信息。 此接口Agent.AppId 和 Agent.ProxyOrganizationOpenId必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param OperatorType: 操作类型，新增:"CREATE"，修改:"UPDATE"，离职:"RESIGN"
        :type OperatorType: str
        :param ProxyOrganizationOperators: 经办人信息列表，最大长度200
        :type ProxyOrganizationOperators: list of ProxyOrganizationOperator
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.OperatorType = None
        self.ProxyOrganizationOperators = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.OperatorType = params.get("OperatorType")
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
此接口Agent.AppId、Agent.ProxyOrganizationOpenId必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param ProxyOrganizationName: 渠道侧合作企业名称，最大长度64个字符
        :type ProxyOrganizationName: str
        :param BusinessLicense: 营业执照正面照(PNG或JPG) base64格式, 大小不超过5M
        :type BusinessLicense: str
        :param UniformSocialCreditCode: 渠道侧合作企业统一社会信用代码，最大长度200个字符
        :type UniformSocialCreditCode: str
        :param ProxyLegalName: 渠道侧合作企业法人/负责人姓名
        :type ProxyLegalName: str
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.ProxyOrganizationName = None
        self.BusinessLicense = None
        self.UniformSocialCreditCode = None
        self.ProxyLegalName = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.ProxyOrganizationName = params.get("ProxyOrganizationName")
        self.BusinessLicense = params.get("BusinessLicense")
        self.UniformSocialCreditCode = params.get("UniformSocialCreditCode")
        self.ProxyLegalName = params.get("ProxyLegalName")
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


class TaskInfo(AbstractModel):
    """复杂文档合成任务的任务信息

    """

    def __init__(self):
        r"""
        :param TaskId: 合成任务Id，可以通过 ChannelGetTaskResultApi 接口获取任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param TaskStatus: 任务状态：READY - 任务已完成；NOTREADY - 任务未完成；
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskStatus: str
        """
        self.TaskId = None
        self.TaskStatus = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param Recipients: 模板中的流程参与人信息
        :type Recipients: list of Recipient
        :param SignComponents: 签署区模板信息结构
        :type SignComponents: list of Component
        :param TemplateType: 模板类型：1-静默签；3-普通模板
        :type TemplateType: int
        :param IsPromoter: 是否是发起人 ,已弃用
        :type IsPromoter: bool
        :param Creator: 模板的创建者信息
        :type Creator: str
        :param CreatedOn: 模板创建的时间戳（精确到秒）
        :type CreatedOn: int
        :param PreviewUrl: 模板的H5预览链接,可以通过浏览器打开此链接预览模板，或者嵌入到iframe中预览模板。
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewUrl: str
        :param ChannelTemplateId: 渠道模板ID
        :type ChannelTemplateId: str
        :param PdfUrl: 渠道版-模板PDF文件链接
注意：此字段可能返回 null，表示取不到有效值。
        :type PdfUrl: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.Components = None
        self.Recipients = None
        self.SignComponents = None
        self.TemplateType = None
        self.IsPromoter = None
        self.Creator = None
        self.CreatedOn = None
        self.PreviewUrl = None
        self.ChannelTemplateId = None
        self.PdfUrl = None


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
        if params.get("Recipients") is not None:
            self.Recipients = []
            for item in params.get("Recipients"):
                obj = Recipient()
                obj._deserialize(item)
                self.Recipients.append(obj)
        if params.get("SignComponents") is not None:
            self.SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self.SignComponents.append(obj)
        self.TemplateType = params.get("TemplateType")
        self.IsPromoter = params.get("IsPromoter")
        self.Creator = params.get("Creator")
        self.CreatedOn = params.get("CreatedOn")
        self.PreviewUrl = params.get("PreviewUrl")
        self.ChannelTemplateId = params.get("ChannelTemplateId")
        self.PdfUrl = params.get("PdfUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFile(AbstractModel):
    """此结构体 (UploadFile) 用于描述多文件上传的文件信息。

    """

    def __init__(self):
        r"""
        :param FileBody: Base64编码后的文件内容
        :type FileBody: str
        :param FileName: 文件名
        :type FileName: str
        """
        self.FileBody = None
        self.FileName = None


    def _deserialize(self, params):
        self.FileBody = params.get("FileBody")
        self.FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFilesRequest(AbstractModel):
    """UploadFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param Agent: 应用相关信息，若是渠道版调用 appid 和proxyappid 必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param BusinessType: 文件对应业务类型
1. TEMPLATE - 模板； 文件类型：.pdf/.doc/.docx/.html
2. DOCUMENT - 签署过程及签署后的合同文档/图片控件 文件类型：.pdf/.doc/.docx/.jpg/.png/.xls.xlsx/.html
        :type BusinessType: str
        :param FileInfos: 上传文件内容数组，最多支持20个文件
        :type FileInfos: list of UploadFile
        :param Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self.Agent = None
        self.BusinessType = None
        self.FileInfos = None
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.BusinessType = params.get("BusinessType")
        if params.get("FileInfos") is not None:
            self.FileInfos = []
            for item in params.get("FileInfos"):
                obj = UploadFile()
                obj._deserialize(item)
                self.FileInfos.append(obj)
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFilesResponse(AbstractModel):
    """UploadFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileIds: 文件id数组，有效期一个小时；有效期内此文件id可以反复使用
        :type FileIds: list of str
        :param TotalCount: 上传成功文件数量
        :type TotalCount: int
        :param FileUrls: 文件Url
        :type FileUrls: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileIds = None
        self.TotalCount = None
        self.FileUrls = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileIds = params.get("FileIds")
        self.TotalCount = params.get("TotalCount")
        self.FileUrls = params.get("FileUrls")
        self.RequestId = params.get("RequestId")


class UsageDetail(AbstractModel):
    """用量明细

    """

    def __init__(self):
        r"""
        :param ProxyOrganizationOpenId: 渠道侧合作企业唯一标识
        :type ProxyOrganizationOpenId: str
        :param ProxyOrganizationName: 渠道侧合作企业名
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyOrganizationName: str
        :param Date: 日期，当需要汇总数据时日期为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Date: str
        :param Usage: 消耗数量
        :type Usage: int
        :param Cancel: 撤回数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Cancel: int
        :param FlowChannel: 消耗渠道
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowChannel: str
        """
        self.ProxyOrganizationOpenId = None
        self.ProxyOrganizationName = None
        self.Date = None
        self.Usage = None
        self.Cancel = None
        self.FlowChannel = None


    def _deserialize(self, params):
        self.ProxyOrganizationOpenId = params.get("ProxyOrganizationOpenId")
        self.ProxyOrganizationName = params.get("ProxyOrganizationName")
        self.Date = params.get("Date")
        self.Usage = params.get("Usage")
        self.Cancel = params.get("Cancel")
        self.FlowChannel = params.get("FlowChannel")
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
        :param OpenId: 渠道平台自定义，对渠道子客企业员的唯一标识。一个OpenId在一个子客企业内唯一对应一个真实员工，不可在其他子客企业内重复使用。（例如，可以使用经办人企业名+员工身份证的hash值，需要渠道平台保存），最大64位字符串
        :type OpenId: str
        :param Channel: 内部参数，暂未开放使用
        :type Channel: str
        :param CustomUserId: 内部参数，暂未开放使用
        :type CustomUserId: str
        :param ClientIp: 内部参数，暂未开放使用
        :type ClientIp: str
        :param ProxyIp: 内部参数，暂未开放使用
        :type ProxyIp: str
        """
        self.OpenId = None
        self.Channel = None
        self.CustomUserId = None
        self.ClientIp = None
        self.ProxyIp = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.Channel = params.get("Channel")
        self.CustomUserId = params.get("CustomUserId")
        self.ClientIp = params.get("ClientIp")
        self.ProxyIp = params.get("ProxyIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        