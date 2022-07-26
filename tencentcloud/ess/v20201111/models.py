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


class ApproverInfo(AbstractModel):
    """参与者信息

    """

    def __init__(self):
        r"""
        :param ApproverType: 参与者类型：
0：企业
1：个人
3：企业静默签署
注：类型为3（企业静默签署）时，此接口会默认完成该签署方的签署。
        :type ApproverType: int
        :param ApproverName: 本环节需要操作人的名字
        :type ApproverName: str
        :param ApproverMobile: 本环节需要操作人的手机号
        :type ApproverMobile: str
        :param SignComponents: 本环节操作人签署控件配置，为企业静默签署时，只允许类型为SIGN_SEAL（印章）和SIGN_DATE（日期）控件，并且传入印章编号。
        :type SignComponents: list of Component
        :param OrganizationName: 如果是企业,则为企业的名字
        :type OrganizationName: str
        :param ApproverIdCardNumber: 身份证号
        :type ApproverIdCardNumber: str
        :param ApproverIdCardType: 证件类型 
ID_CARD 身份证
HONGKONG_AND_MACAO 港澳居民来往内地通行证
HONGKONG_MACAO_AND_TAIWAN 港澳台居民居住证(格式同居民身份证)
        :type ApproverIdCardType: str
        :param NotifyType: sms--短信，none--不通知
        :type NotifyType: str
        :param ApproverRole: 1--收款人、2--开具人、3--见证人
        :type ApproverRole: int
        :param VerifyChannel: 签署意愿确认渠道,WEIXINAPP:人脸识别
        :type VerifyChannel: list of str
        :param PreReadTime: 合同的强制预览时间：3~300s，未指定则按合同页数计算
        :type PreReadTime: int
        """
        self.ApproverType = None
        self.ApproverName = None
        self.ApproverMobile = None
        self.SignComponents = None
        self.OrganizationName = None
        self.ApproverIdCardNumber = None
        self.ApproverIdCardType = None
        self.NotifyType = None
        self.ApproverRole = None
        self.VerifyChannel = None
        self.PreReadTime = None


    def _deserialize(self, params):
        self.ApproverType = params.get("ApproverType")
        self.ApproverName = params.get("ApproverName")
        self.ApproverMobile = params.get("ApproverMobile")
        if params.get("SignComponents") is not None:
            self.SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self.SignComponents.append(obj)
        self.OrganizationName = params.get("OrganizationName")
        self.ApproverIdCardNumber = params.get("ApproverIdCardNumber")
        self.ApproverIdCardType = params.get("ApproverIdCardType")
        self.NotifyType = params.get("NotifyType")
        self.ApproverRole = params.get("ApproverRole")
        self.VerifyChannel = params.get("VerifyChannel")
        self.PreReadTime = params.get("PreReadTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Caller(AbstractModel):
    """此结构体 (Caller) 用于描述调用方属性。

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用号
        :type ApplicationId: str
        :param OrganizationId: 主机构ID
        :type OrganizationId: str
        :param OperatorId: 经办人的用户ID
        :type OperatorId: str
        :param SubOrganizationId: 下属机构ID
        :type SubOrganizationId: str
        """
        self.ApplicationId = None
        self.OrganizationId = None
        self.OperatorId = None
        self.SubOrganizationId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.OrganizationId = params.get("OrganizationId")
        self.OperatorId = params.get("OperatorId")
        self.SubOrganizationId = params.get("SubOrganizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelFlowRequest(AbstractModel):
    """CancelFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param FlowId: 签署流程id
        :type FlowId: str
        :param CancelMessage: 撤销原因，最长200个字符；
        :type CancelMessage: str
        :param Agent: 应用相关信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.FlowId = None
        self.CancelMessage = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowId = params.get("FlowId")
        self.CancelMessage = params.get("CancelMessage")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelFlowResponse(AbstractModel):
    """CancelFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CancelMultiFlowSignQRCodeRequest(AbstractModel):
    """CancelMultiFlowSignQRCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 用户信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param QrCodeId: 二维码id
        :type QrCodeId: str
        :param Agent: 应用信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.QrCodeId = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.QrCodeId = params.get("QrCodeId")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelMultiFlowSignQRCodeResponse(AbstractModel):
    """CancelMultiFlowSignQRCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CcInfo(AbstractModel):
    """抄送信息

    """

    def __init__(self):
        r"""
        :param Mobile: 被抄送人手机号
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
        


class Component(AbstractModel):
    """模板控件信息

    """

    def __init__(self):
        r"""
        :param ComponentType: 如果是 Component 控件类型，则可选类型为：
TEXT - 内容文本控件
DATE - 内容日期控件
CHECK_BOX - 勾选框控件
如果是 SignComponent 控件类型，则可选类型为：
SIGN_SEAL - 签署印章控件
SIGN_DATE - 签署日期控件
SIGN_SIGNATURE - 手写签名控件
        :type ComponentType: str
        :param ComponentWidth: 参数控件宽度，单位pt
        :type ComponentWidth: float
        :param ComponentHeight: 参数控件高度，单位pt
        :type ComponentHeight: float
        :param ComponentPage: 参数控件所在页码，取值为：1-N
        :type ComponentPage: int
        :param ComponentPosX: 参数控件X位置，单位pt
        :type ComponentPosX: float
        :param ComponentPosY: 参数控件Y位置，单位pt
        :type ComponentPosY: float
        :param FileIndex: 控件所属文件的序号（模板中的resourceId排列序号，取值为：0-N）
        :type FileIndex: int
        :param ComponentId: GenerateMode==KEYWORD 指定关键字
        :type ComponentId: str
        :param ComponentName: GenerateMode==FIELD 指定表单域名称
        :type ComponentName: str
        :param ComponentRequired: 是否必选，默认为false
        :type ComponentRequired: bool
        :param ComponentExtra: 扩展参数：
ComponentType为SIGN_SIGNATURE类型可以控制签署方式
{“ComponentTypeLimit”: [“xxx”]}
xxx可以为：
HANDWRITE – 手写签名
BORDERLESS_ESIGN – 自动生成无边框腾讯体
OCR_ESIGN -- AI智能识别手写签名
ESIGN -- 个人印章类型
如：{“ComponentTypeLimit”: [“BORDERLESS_ESIGN”]}
        :type ComponentExtra: str
        :param ComponentRecipientId: 控件关联的签署人ID
        :type ComponentRecipientId: str
        :param ComponentValue: 控件所填写的内容
        :type ComponentValue: str
        :param IsFormType: 是否是表单域类型，默认不存在
        :type IsFormType: bool
        :param GenerateMode: NORMAL 正常模式，使用坐标制定签署控件位置
FIELD 表单域，需使用ComponentName指定表单域名称
KEYWORD 关键字，使用ComponentId指定关键字
        :type GenerateMode: str
        :param ComponentDateFontSize: 日期控件类型字号
        :type ComponentDateFontSize: int
        :param OffsetX: 指定关键字时横坐标偏移量，单位pt
        :type OffsetX: float
        :param OffsetY: 指定关键字时纵坐标偏移量，单位pt
        :type OffsetY: float
        """
        self.ComponentType = None
        self.ComponentWidth = None
        self.ComponentHeight = None
        self.ComponentPage = None
        self.ComponentPosX = None
        self.ComponentPosY = None
        self.FileIndex = None
        self.ComponentId = None
        self.ComponentName = None
        self.ComponentRequired = None
        self.ComponentExtra = None
        self.ComponentRecipientId = None
        self.ComponentValue = None
        self.IsFormType = None
        self.GenerateMode = None
        self.ComponentDateFontSize = None
        self.OffsetX = None
        self.OffsetY = None


    def _deserialize(self, params):
        self.ComponentType = params.get("ComponentType")
        self.ComponentWidth = params.get("ComponentWidth")
        self.ComponentHeight = params.get("ComponentHeight")
        self.ComponentPage = params.get("ComponentPage")
        self.ComponentPosX = params.get("ComponentPosX")
        self.ComponentPosY = params.get("ComponentPosY")
        self.FileIndex = params.get("FileIndex")
        self.ComponentId = params.get("ComponentId")
        self.ComponentName = params.get("ComponentName")
        self.ComponentRequired = params.get("ComponentRequired")
        self.ComponentExtra = params.get("ComponentExtra")
        self.ComponentRecipientId = params.get("ComponentRecipientId")
        self.ComponentValue = params.get("ComponentValue")
        self.IsFormType = params.get("IsFormType")
        self.GenerateMode = params.get("GenerateMode")
        self.ComponentDateFontSize = params.get("ComponentDateFontSize")
        self.OffsetX = params.get("OffsetX")
        self.OffsetY = params.get("OffsetY")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDocumentRequest(AbstractModel):
    """CreateDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param FlowId: 签署流程编号,由CreateFlow接口返回
        :type FlowId: str
        :param TemplateId: 用户上传的模板ID
        :type TemplateId: str
        :param FileNames: 文件名列表,单个文件名最大长度200个字符
        :type FileNames: list of str
        :param FormFields: 内容控件信息数组
        :type FormFields: list of FormField
        :param NeedPreview: 是否需要生成预览文件 默认不生成；
预览链接有效期300秒；
        :type NeedPreview: bool
        :param ClientToken: 客户端Token，保持接口幂等性,最大长度64个字符
        :type ClientToken: str
        :param Agent: 应用相关信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.FlowId = None
        self.TemplateId = None
        self.FileNames = None
        self.FormFields = None
        self.NeedPreview = None
        self.ClientToken = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowId = params.get("FlowId")
        self.TemplateId = params.get("TemplateId")
        self.FileNames = params.get("FileNames")
        if params.get("FormFields") is not None:
            self.FormFields = []
            for item in params.get("FormFields"):
                obj = FormField()
                obj._deserialize(item)
                self.FormFields.append(obj)
        self.NeedPreview = params.get("NeedPreview")
        self.ClientToken = params.get("ClientToken")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDocumentResponse(AbstractModel):
    """CreateDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param DocumentId: 签署流程电子文档ID
        :type DocumentId: str
        :param PreviewFileUrl: 签署流程文件的预览地址, 5分钟内有效。仅当NeedPreview为true 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewFileUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DocumentId = None
        self.PreviewFileUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DocumentId = params.get("DocumentId")
        self.PreviewFileUrl = params.get("PreviewFileUrl")
        self.RequestId = params.get("RequestId")


class CreateFlowByFilesRequest(AbstractModel):
    """CreateFlowByFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param FlowName: 签署流程名称,最大长度200个字符
        :type FlowName: str
        :param Approvers: 签署参与者信息
        :type Approvers: list of ApproverInfo
        :param FileIds: 签署pdf文件的资源编号列表，通过UploadFiles接口获取
        :type FileIds: list of str
        :param FlowType: 签署流程的类型(如销售合同/入职合同等)，最大长度200个字符
        :type FlowType: str
        :param Components: 经办人内容控件配置。可选类型为：
TEXT - 内容文本控件
MULTI_LINE_TEXT - 多行文本控件
CHECK_BOX - 勾选框控件
ATTACHMENT - 附件
注：默认字体大小为 字号12
        :type Components: list of Component
        :param CcInfos: 被抄送人的信息列表。
注:此功能为白名单功能，若有需要，请联系电子签客服开白使用
        :type CcInfos: list of CcInfo
        :param NeedPreview: 是否需要预览，true：预览模式，false：非预览（默认）；
预览链接有效期300秒；
        :type NeedPreview: bool
        :param FlowDescription: 签署流程描述,最大长度1000个字符
        :type FlowDescription: str
        :param Deadline: 签署流程的签署截止时间。
值为unix时间戳,精确到秒,不传默认为当前时间一年后
        :type Deadline: int
        :param Unordered: 发送类型：
true：无序签
false：有序签
注：默认为false（有序签）
        :type Unordered: bool
        :param CustomShowMap: 合同显示的页卡模板，说明：只支持{合同名称}, {发起方企业}, {发起方姓名}, {签署方N企业}, {签署方N姓名}，且N不能超过签署人的数量，N从1开始
        :type CustomShowMap: str
        :param Agent: 应用号信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.FlowName = None
        self.Approvers = None
        self.FileIds = None
        self.FlowType = None
        self.Components = None
        self.CcInfos = None
        self.NeedPreview = None
        self.FlowDescription = None
        self.Deadline = None
        self.Unordered = None
        self.CustomShowMap = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowName = params.get("FlowName")
        if params.get("Approvers") is not None:
            self.Approvers = []
            for item in params.get("Approvers"):
                obj = ApproverInfo()
                obj._deserialize(item)
                self.Approvers.append(obj)
        self.FileIds = params.get("FileIds")
        self.FlowType = params.get("FlowType")
        if params.get("Components") is not None:
            self.Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self.Components.append(obj)
        if params.get("CcInfos") is not None:
            self.CcInfos = []
            for item in params.get("CcInfos"):
                obj = CcInfo()
                obj._deserialize(item)
                self.CcInfos.append(obj)
        self.NeedPreview = params.get("NeedPreview")
        self.FlowDescription = params.get("FlowDescription")
        self.Deadline = params.get("Deadline")
        self.Unordered = params.get("Unordered")
        self.CustomShowMap = params.get("CustomShowMap")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowByFilesResponse(AbstractModel):
    """CreateFlowByFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 签署流程编号
        :type FlowId: str
        :param PreviewUrl: 合同预览链接
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.PreviewUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.PreviewUrl = params.get("PreviewUrl")
        self.RequestId = params.get("RequestId")


class CreateFlowRequest(AbstractModel):
    """CreateFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param FlowName: 签署流程名称,最大长度200个字符
        :type FlowName: str
        :param Approvers: 签署流程参与者信息
        :type Approvers: list of FlowCreateApprover
        :param FlowType: 签署流程的类型(如销售合同/入职合同等)，最大长度200个字符
        :type FlowType: str
        :param ClientToken: 客户端Token，保持接口幂等性,最大长度64个字符
        :type ClientToken: str
        :param CallbackUrl: 暂未开放
        :type CallbackUrl: str
        :param DeadLine: 签署流程的签署截止时间。
值为unix时间戳,精确到秒,不传默认为当前时间一年后
        :type DeadLine: int
        :param UserData: 用户自定义字段(需进行base64 encode),回调的时候会进行透传, 长度需要小于20480
        :type UserData: str
        :param FlowDescription: 签署流程描述,最大长度1000个字符
        :type FlowDescription: str
        :param Unordered: 发送类型：
true：无序签
false：有序签
注：默认为false（有序签），请和模板中的配置保持一致
        :type Unordered: bool
        :param CustomShowMap: 合同显示的页卡模板，说明：只支持{合同名称}, {发起方企业}, {发起方姓名}, {签署方N企业}, {签署方N姓名}，且N不能超过签署人的数量，N从1开始
        :type CustomShowMap: str
        :param RelatedFlowId: 暂未开放
        :type RelatedFlowId: str
        :param Agent: 应用相关信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.FlowName = None
        self.Approvers = None
        self.FlowType = None
        self.ClientToken = None
        self.CallbackUrl = None
        self.DeadLine = None
        self.UserData = None
        self.FlowDescription = None
        self.Unordered = None
        self.CustomShowMap = None
        self.RelatedFlowId = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowName = params.get("FlowName")
        if params.get("Approvers") is not None:
            self.Approvers = []
            for item in params.get("Approvers"):
                obj = FlowCreateApprover()
                obj._deserialize(item)
                self.Approvers.append(obj)
        self.FlowType = params.get("FlowType")
        self.ClientToken = params.get("ClientToken")
        self.CallbackUrl = params.get("CallbackUrl")
        self.DeadLine = params.get("DeadLine")
        self.UserData = params.get("UserData")
        self.FlowDescription = params.get("FlowDescription")
        self.Unordered = params.get("Unordered")
        self.CustomShowMap = params.get("CustomShowMap")
        self.RelatedFlowId = params.get("RelatedFlowId")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowResponse(AbstractModel):
    """CreateFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 签署流程编号
        :type FlowId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateMultiFlowSignQRCodeRequest(AbstractModel):
    """CreateMultiFlowSignQRCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 模板ID
        :type TemplateId: str
        :param FlowName: 签署流程名称，最大长度不超过200字符
        :type FlowName: str
        :param Operator: 用户信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param Agent: 应用信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param CallbackUrl: 回调地址,最大长度1000字符串
回调时机：
用户通过签署二维码发起签署流程时，企业额度不足导致失败
        :type CallbackUrl: str
        :param MaxFlowNum: 最大可发起签署流程份数，默认5份 
发起流程数量超过此上限后二维码自动失效
        :type MaxFlowNum: int
        :param FlowEffectiveDay: 签署流程有效天数 默认7天 最高设置不超过30天
        :type FlowEffectiveDay: int
        :param QrEffectiveDay: 二维码有效天数 默认7天 最高设置不超过90天
        :type QrEffectiveDay: int
        """
        self.TemplateId = None
        self.FlowName = None
        self.Operator = None
        self.Agent = None
        self.CallbackUrl = None
        self.MaxFlowNum = None
        self.FlowEffectiveDay = None
        self.QrEffectiveDay = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.FlowName = params.get("FlowName")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.CallbackUrl = params.get("CallbackUrl")
        self.MaxFlowNum = params.get("MaxFlowNum")
        self.FlowEffectiveDay = params.get("FlowEffectiveDay")
        self.QrEffectiveDay = params.get("QrEffectiveDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMultiFlowSignQRCodeResponse(AbstractModel):
    """CreateMultiFlowSignQRCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param QrCode: 签署二维码对象
        :type QrCode: :class:`tencentcloud.ess.v20201111.models.SignQrCode`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.QrCode = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QrCode") is not None:
            self.QrCode = SignQrCode()
            self.QrCode._deserialize(params.get("QrCode"))
        self.RequestId = params.get("RequestId")


class CreateSchemeUrlRequest(AbstractModel):
    """CreateSchemeUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param OrganizationName: 企业名称
        :type OrganizationName: str
        :param Name: 姓名,最大长度50个字符
        :type Name: str
        :param Mobile: 手机号，大陆手机号11位
        :type Mobile: str
        :param EndPoint: 链接类型
HTTP：跳转电子签小程序的http_url，
APP：第三方APP或小程序跳转电子签小程序的path。
默认为HTTP类型
        :type EndPoint: str
        :param FlowId: 签署流程编号 (PathType=1时必传)
        :type FlowId: str
        :param PathType: 跳转页面 1: 小程序合同详情 2: 小程序合同列表页 0: 不传, 默认主页
        :type PathType: int
        :param AutoJumpBack: 是否自动回跳 true：是， false：否。该参数只针对"APP" 类型的签署链接有效
        :type AutoJumpBack: bool
        :param Agent: 应用相关信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.OrganizationName = None
        self.Name = None
        self.Mobile = None
        self.EndPoint = None
        self.FlowId = None
        self.PathType = None
        self.AutoJumpBack = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.OrganizationName = params.get("OrganizationName")
        self.Name = params.get("Name")
        self.Mobile = params.get("Mobile")
        self.EndPoint = params.get("EndPoint")
        self.FlowId = params.get("FlowId")
        self.PathType = params.get("PathType")
        self.AutoJumpBack = params.get("AutoJumpBack")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSchemeUrlResponse(AbstractModel):
    """CreateSchemeUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param SchemeUrl: 小程序链接地址
        :type SchemeUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SchemeUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SchemeUrl = params.get("SchemeUrl")
        self.RequestId = params.get("RequestId")


class DescribeFileUrlsRequest(AbstractModel):
    """DescribeFileUrls请求参数结构体

    """

    def __init__(self):
        r"""
        :param BusinessType: 文件对应的业务类型，目前支持：
- 模板 "TEMPLATE"
- 文档 "DOCUMENT"
- 印章  “SEAL”
- 流程 "FLOW"
        :type BusinessType: str
        :param BusinessIds: 业务编号的数组，如模板编号、文档编号、印章编号
最大支持20个资源
        :type BusinessIds: list of str
        :param Operator: 操作者信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param Agent: 应用相关信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param FileName: 下载后的文件命名，只有fileType为zip的时候生效
        :type FileName: str
        :param FileType: 文件类型，"JPG", "PDF","ZIP"等
        :type FileType: str
        :param Offset: 指定资源起始偏移量，默认0
        :type Offset: int
        :param Limit: 指定资源数量，查询全部资源则传入-1
        :type Limit: int
        :param UrlTtl: 下载url过期时间，单位秒。0: 按默认值5分钟，允许范围：1s~24x60x60s(1天)
        :type UrlTtl: int
        :param Scene: 暂不开放
        :type Scene: str
        :param CcToken: 暂不开放
        :type CcToken: str
        """
        self.BusinessType = None
        self.BusinessIds = None
        self.Operator = None
        self.Agent = None
        self.FileName = None
        self.FileType = None
        self.Offset = None
        self.Limit = None
        self.UrlTtl = None
        self.Scene = None
        self.CcToken = None


    def _deserialize(self, params):
        self.BusinessType = params.get("BusinessType")
        self.BusinessIds = params.get("BusinessIds")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.FileName = params.get("FileName")
        self.FileType = params.get("FileType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.UrlTtl = params.get("UrlTtl")
        self.Scene = params.get("Scene")
        self.CcToken = params.get("CcToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileUrlsResponse(AbstractModel):
    """DescribeFileUrls返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileUrls: URL信息
        :type FileUrls: list of FileUrl
        :param TotalCount: URL数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileUrls = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileUrls") is not None:
            self.FileUrls = []
            for item in params.get("FileUrls"):
                obj = FileUrl()
                obj._deserialize(item)
                self.FileUrls.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeFlowBriefsRequest(AbstractModel):
    """DescribeFlowBriefs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param FlowIds: 需要查询的流程ID列表
        :type FlowIds: list of str
        :param Agent: 应用相关信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.FlowIds = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowIds = params.get("FlowIds")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowBriefsResponse(AbstractModel):
    """DescribeFlowBriefs返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowBriefs: 流程列表
        :type FlowBriefs: list of FlowBrief
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowBriefs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FlowBriefs") is not None:
            self.FlowBriefs = []
            for item in params.get("FlowBriefs"):
                obj = FlowBrief()
                obj._deserialize(item)
                self.FlowBriefs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlowTemplatesRequest(AbstractModel):
    """DescribeFlowTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param Filters: 搜索条件，具体参考Filter结构体。本接口取值：template-id：按照【 **模板唯一标识** 】进行过滤
        :type Filters: list of Filter
        :param Limit: 查询个数，默认20，最大100
        :type Limit: int
        :param Offset: 查询偏移位置，默认0
        :type Offset: int
        :param ContentType: 查询内容：0-模板列表及详情（默认），1-仅模板列表
        :type ContentType: int
        :param GenerateSource: 暂未开放
        :type GenerateSource: int
        :param Agent: 应用相关信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.ContentType = None
        self.GenerateSource = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ContentType = params.get("ContentType")
        self.GenerateSource = params.get("GenerateSource")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowTemplatesResponse(AbstractModel):
    """DescribeFlowTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param Templates: 模板详情列表
        :type Templates: list of TemplateInfo
        :param TotalCount: 查询到的总个数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Templates = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = TemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeThirdPartyAuthCodeRequest(AbstractModel):
    """DescribeThirdPartyAuthCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param AuthCode: 电子签小程序跳转客户小程序时携带的授权查看码
        :type AuthCode: str
        """
        self.AuthCode = None


    def _deserialize(self, params):
        self.AuthCode = params.get("AuthCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeThirdPartyAuthCodeResponse(AbstractModel):
    """DescribeThirdPartyAuthCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param VerifyStatus: 用户是否实名，VERIFIED 为实名，UNVERIFIED 未实名
        :type VerifyStatus: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VerifyStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VerifyStatus = params.get("VerifyStatus")
        self.RequestId = params.get("RequestId")


class FileInfo(AbstractModel):
    """二期接口返回的模板中文件的信息结构

    """

    def __init__(self):
        r"""
        :param FileId: 文件Id
        :type FileId: str
        :param FileName: 文件名
        :type FileName: str
        :param FileSize: 文件大小，单位为Byte
        :type FileSize: int
        :param CreatedOn: 文件上传时间，10位时间戳（精确到秒）
        :type CreatedOn: int
        """
        self.FileId = None
        self.FileName = None
        self.FileSize = None
        self.CreatedOn = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.CreatedOn = params.get("CreatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileUrl(AbstractModel):
    """下载文件的URL信息

    """

    def __init__(self):
        r"""
        :param Url: 下载文件的URL
        :type Url: str
        :param Option: 下载文件的附加信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Option: str
        """
        self.Url = None
        self.Option = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Option = params.get("Option")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """查询过滤条件

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
        


class FlowBrief(AbstractModel):
    """流程信息摘要

    """

    def __init__(self):
        r"""
        :param FlowId: 流程的编号
        :type FlowId: str
        :param FlowName: 流程的名称
        :type FlowName: str
        :param FlowDescription: 流程的描述
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowDescription: str
        :param FlowType: 流程的类型
        :type FlowType: str
        :param FlowStatus: 流程状态
- `1` 未签署
- `2`  部分签署
- `3`  已退回
- `4`  完成签署
- `5`  已过期
- `6`  已取消
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowStatus: int
        :param CreatedOn: 流程创建的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedOn: int
        :param FlowMessage: 拒签或者取消的原因描述
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowMessage: str
        """
        self.FlowId = None
        self.FlowName = None
        self.FlowDescription = None
        self.FlowType = None
        self.FlowStatus = None
        self.CreatedOn = None
        self.FlowMessage = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.FlowName = params.get("FlowName")
        self.FlowDescription = params.get("FlowDescription")
        self.FlowType = params.get("FlowType")
        self.FlowStatus = params.get("FlowStatus")
        self.CreatedOn = params.get("CreatedOn")
        self.FlowMessage = params.get("FlowMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowCreateApprover(AbstractModel):
    """创建流程的签署方信息

    """

    def __init__(self):
        r"""
        :param ApproverType: 参与者类型：
0：企业
1：个人
3：企业静默签署
注：类型为3（企业静默签署）时，此接口会默认完成该签署方的签署。
        :type ApproverType: int
        :param OrganizationName: 如果签署方为企业，需要填入企业全称
        :type OrganizationName: str
        :param ApproverName: 签署方经办人姓名
        :type ApproverName: str
        :param ApproverMobile: 签署方经办人手机号码
        :type ApproverMobile: str
        :param ApproverIdCardType: 签署方经办人证件类型ID_CARD 身份证
HONGKONG_AND_MACAO 港澳居民来往内地通行证
HONGKONG_MACAO_AND_TAIWAN 港澳台居民居住证(格式同居民身份证)
        :type ApproverIdCardType: str
        :param ApproverIdCardNumber: 签署方经办人证件号码
        :type ApproverIdCardNumber: str
        :param RecipientId: 签署方经办人在模板中的角色ID
        :type RecipientId: str
        :param VerifyChannel: 签署意愿确认渠道,WEIXINAPP:人脸识别
        :type VerifyChannel: list of str
        :param NotifyType: 是否发送短信，sms--短信通知，none--不通知，默认为sms
        :type NotifyType: str
        :param IsFullText: 签署前置条件：是否需要阅读全文，默认为不需要
        :type IsFullText: bool
        :param PreReadTime: 签署前置条件：阅读时长限制，默认为不需要
        :type PreReadTime: int
        :param UserId: 签署方经办人的用户ID,和签署方经办人姓名+手机号+证件必须有一个
        :type UserId: str
        :param Required: 当前只支持true，默认为true
        :type Required: bool
        """
        self.ApproverType = None
        self.OrganizationName = None
        self.ApproverName = None
        self.ApproverMobile = None
        self.ApproverIdCardType = None
        self.ApproverIdCardNumber = None
        self.RecipientId = None
        self.VerifyChannel = None
        self.NotifyType = None
        self.IsFullText = None
        self.PreReadTime = None
        self.UserId = None
        self.Required = None


    def _deserialize(self, params):
        self.ApproverType = params.get("ApproverType")
        self.OrganizationName = params.get("OrganizationName")
        self.ApproverName = params.get("ApproverName")
        self.ApproverMobile = params.get("ApproverMobile")
        self.ApproverIdCardType = params.get("ApproverIdCardType")
        self.ApproverIdCardNumber = params.get("ApproverIdCardNumber")
        self.RecipientId = params.get("RecipientId")
        self.VerifyChannel = params.get("VerifyChannel")
        self.NotifyType = params.get("NotifyType")
        self.IsFullText = params.get("IsFullText")
        self.PreReadTime = params.get("PreReadTime")
        self.UserId = params.get("UserId")
        self.Required = params.get("Required")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FormField(AbstractModel):
    """电子文档的控件填充信息

    """

    def __init__(self):
        r"""
        :param ComponentValue: 控件填充value
        :type ComponentValue: str
        :param ComponentId: 控件id
        :type ComponentId: str
        :param ComponentName: 控件名字，最大长度不超过30字符
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
        


class Recipient(AbstractModel):
    """签署参与者信息

    """

    def __init__(self):
        r"""
        :param RecipientId: 签署参与者ID
        :type RecipientId: str
        :param RecipientType: 参与者类型（ENTERPRISE/INDIVIDUAL）
        :type RecipientType: str
        :param Description: 描述信息
        :type Description: str
        :param RoleName: 角色名称
        :type RoleName: str
        :param RequireValidation: 是否需要验证，默认为false
        :type RequireValidation: bool
        :param RequireSign: 是否需要签署，默认为true
        :type RequireSign: bool
        :param RoutingOrder: 添加序列
        :type RoutingOrder: int
        :param RequireDelivery: 是否需要发送，默认为true
        :type RequireDelivery: bool
        :param Email: 邮箱地址
        :type Email: str
        :param Mobile: 电话号码
        :type Mobile: str
        :param UserId: 关联的用户ID
        :type UserId: str
        :param DeliveryMethod: 发送方式（EMAIL/MOBILE）
        :type DeliveryMethod: str
        :param RecipientExtra: 附属信息
        :type RecipientExtra: str
        """
        self.RecipientId = None
        self.RecipientType = None
        self.Description = None
        self.RoleName = None
        self.RequireValidation = None
        self.RequireSign = None
        self.RoutingOrder = None
        self.RequireDelivery = None
        self.Email = None
        self.Mobile = None
        self.UserId = None
        self.DeliveryMethod = None
        self.RecipientExtra = None


    def _deserialize(self, params):
        self.RecipientId = params.get("RecipientId")
        self.RecipientType = params.get("RecipientType")
        self.Description = params.get("Description")
        self.RoleName = params.get("RoleName")
        self.RequireValidation = params.get("RequireValidation")
        self.RequireSign = params.get("RequireSign")
        self.RoutingOrder = params.get("RoutingOrder")
        self.RequireDelivery = params.get("RequireDelivery")
        self.Email = params.get("Email")
        self.Mobile = params.get("Mobile")
        self.UserId = params.get("UserId")
        self.DeliveryMethod = params.get("DeliveryMethod")
        self.RecipientExtra = params.get("RecipientExtra")
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
        


class StartFlowRequest(AbstractModel):
    """StartFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param FlowId: 签署流程编号，由CreateFlow接口返回
        :type FlowId: str
        :param ClientToken: 客户端Token，保持接口幂等性,最大长度64个字符
        :type ClientToken: str
        :param Agent: 应用相关信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.FlowId = None
        self.ClientToken = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowId = params.get("FlowId")
        self.ClientToken = params.get("ClientToken")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartFlowResponse(AbstractModel):
    """StartFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 返回描述，START-发起成功， REVIEW-提交审核成功，EXECUTING-已提交发起任务
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class TemplateInfo(AbstractModel):
    """二期接口返回的模板的信息结构

    """

    def __init__(self):
        r"""
        :param TemplateId: 模板ID
        :type TemplateId: str
        :param TemplateName: 模板名字
        :type TemplateName: str
        :param Description: 模板描述信息
        :type Description: str
        :param DocumentResourceIds: 模板关联的资源IDs
        :type DocumentResourceIds: list of str
        :param FileInfos: 返回的文件信息结构
        :type FileInfos: list of FileInfo
        :param AttachmentResourceIds: 附件关联的资源ID是
        :type AttachmentResourceIds: list of str
        :param SignOrder: 签署顺序
        :type SignOrder: list of int
        :param Recipients: 签署参与者的信息
        :type Recipients: list of Recipient
        :param Components: 模板信息结构
        :type Components: list of Component
        :param SignComponents: 签署区模板信息结构
        :type SignComponents: list of Component
        :param Status: 模板状态(-1:不可用；0:草稿态；1:正式态)
        :type Status: int
        :param Creator: 模板的创建人
        :type Creator: str
        :param CreatedOn: 模板创建的时间戳（精确到秒）
        :type CreatedOn: int
        :param Promoter: 发起人角色信息
        :type Promoter: :class:`tencentcloud.ess.v20201111.models.Recipient`
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.DocumentResourceIds = None
        self.FileInfos = None
        self.AttachmentResourceIds = None
        self.SignOrder = None
        self.Recipients = None
        self.Components = None
        self.SignComponents = None
        self.Status = None
        self.Creator = None
        self.CreatedOn = None
        self.Promoter = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.DocumentResourceIds = params.get("DocumentResourceIds")
        if params.get("FileInfos") is not None:
            self.FileInfos = []
            for item in params.get("FileInfos"):
                obj = FileInfo()
                obj._deserialize(item)
                self.FileInfos.append(obj)
        self.AttachmentResourceIds = params.get("AttachmentResourceIds")
        self.SignOrder = params.get("SignOrder")
        if params.get("Recipients") is not None:
            self.Recipients = []
            for item in params.get("Recipients"):
                obj = Recipient()
                obj._deserialize(item)
                self.Recipients.append(obj)
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
        self.Status = params.get("Status")
        self.Creator = params.get("Creator")
        self.CreatedOn = params.get("CreatedOn")
        if params.get("Promoter") is not None:
            self.Promoter = Recipient()
            self.Promoter._deserialize(params.get("Promoter"))
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
        :param FileName: 文件名，最大长度不超过200字符
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
        :param BusinessType: 文件对应业务类型，用于区分文件存储路径：
1. TEMPLATE - 模板； 文件类型：.pdf/.html
2. DOCUMENT - 签署过程及签署后的合同文档 文件类型：.pdf/.html
3. SEAL - 印章； 文件类型：.jpg/.jpeg/.png
        :type BusinessType: str
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.ess.v20201111.models.Caller`
        :param FileInfos: 上传文件内容数组，最多支持20个文件
        :type FileInfos: list of UploadFile
        :param FileUrls: 上传文件链接数组，最多支持20个URL
        :type FileUrls: str
        :param CoverRect: 此参数只对 PDF 文件有效。是否将pdf灰色矩阵置白
true--是，处理置白
false--否，不处理
        :type CoverRect: bool
        :param FileType: 文件类型， 默认通过文件内容解析得到文件类型，客户可以显示的说明上传文件的类型。
如：PDF 表示上传的文件 xxx.pdf的文件类型是 PDF
        :type FileType: str
        :param CustomIds: 用户自定义ID数组，与上传文件一一对应
        :type CustomIds: list of str
        """
        self.BusinessType = None
        self.Caller = None
        self.FileInfos = None
        self.FileUrls = None
        self.CoverRect = None
        self.FileType = None
        self.CustomIds = None


    def _deserialize(self, params):
        self.BusinessType = params.get("BusinessType")
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        if params.get("FileInfos") is not None:
            self.FileInfos = []
            for item in params.get("FileInfos"):
                obj = UploadFile()
                obj._deserialize(item)
                self.FileInfos.append(obj)
        self.FileUrls = params.get("FileUrls")
        self.CoverRect = params.get("CoverRect")
        self.FileType = params.get("FileType")
        self.CustomIds = params.get("CustomIds")
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
        :param FileIds: 文件id数组
        :type FileIds: list of str
        :param TotalCount: 上传成功文件数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileIds = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileIds = params.get("FileIds")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class UserInfo(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param UserId: 用户在平台的编号
        :type UserId: str
        :param Channel: 用户的来源渠道
        :type Channel: str
        :param OpenId: 用户在渠道的编号
        :type OpenId: str
        :param ClientIp: 用户真实IP
        :type ClientIp: str
        :param ProxyIp: 用户代理IP
        :type ProxyIp: str
        """
        self.UserId = None
        self.Channel = None
        self.OpenId = None
        self.ClientIp = None
        self.ProxyIp = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
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
        