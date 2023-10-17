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
        :param _AppId: 应用的唯一标识。不同的业务系统可以采用不同的AppId，不同AppId下的数据是隔离的。可以由控制台开发者中心-应用集成自主生成。
        :type AppId: str
        :param _ProxyOrganizationOpenId: 第三方应用平台自定义，对应第三方平台子客企业的唯一标识。一个第三方平台子客企业主体与子客企业ProxyOrganizationOpenId是一一对应的，不可更改，不可重复使用。（例如，可以使用企业名称的hash值，或者社会统一信用代码的hash值，或者随机hash值，需要第三方应用平台保存），最大64位字符串
        :type ProxyOrganizationOpenId: str
        :param _ProxyOperator: 第三方平台子客企业中的员工/经办人，通过第三方应用平台进入电子签完成实名、且被赋予相关权限后，可以参与到企业资源的管理或签署流程中。
        :type ProxyOperator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param _ProxyAppId: 非必需参数，在第三方平台子客企业开通电子签后，会生成唯一的子客应用Id（ProxyAppId）用于代理调用时的鉴权，在子客开通的回调中获取。
        :type ProxyAppId: str
        :param _ProxyOrganizationId: 内部参数，暂未开放使用
        :type ProxyOrganizationId: str
        """
        self._AppId = None
        self._ProxyOrganizationOpenId = None
        self._ProxyOperator = None
        self._ProxyAppId = None
        self._ProxyOrganizationId = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ProxyOrganizationOpenId(self):
        return self._ProxyOrganizationOpenId

    @ProxyOrganizationOpenId.setter
    def ProxyOrganizationOpenId(self, ProxyOrganizationOpenId):
        self._ProxyOrganizationOpenId = ProxyOrganizationOpenId

    @property
    def ProxyOperator(self):
        return self._ProxyOperator

    @ProxyOperator.setter
    def ProxyOperator(self, ProxyOperator):
        self._ProxyOperator = ProxyOperator

    @property
    def ProxyAppId(self):
        return self._ProxyAppId

    @ProxyAppId.setter
    def ProxyAppId(self, ProxyAppId):
        self._ProxyAppId = ProxyAppId

    @property
    def ProxyOrganizationId(self):
        warnings.warn("parameter `ProxyOrganizationId` is deprecated", DeprecationWarning) 

        return self._ProxyOrganizationId

    @ProxyOrganizationId.setter
    def ProxyOrganizationId(self, ProxyOrganizationId):
        warnings.warn("parameter `ProxyOrganizationId` is deprecated", DeprecationWarning) 

        self._ProxyOrganizationId = ProxyOrganizationId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ProxyOrganizationOpenId = params.get("ProxyOrganizationOpenId")
        if params.get("ProxyOperator") is not None:
            self._ProxyOperator = UserInfo()
            self._ProxyOperator._deserialize(params.get("ProxyOperator"))
        self._ProxyAppId = params.get("ProxyAppId")
        self._ProxyOrganizationId = params.get("ProxyOrganizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApproverComponentLimitType(AbstractModel):
    """指定签署方经办人控件类型是个人印章签署控件（SIGN_SIGNATURE） 时，可选的签名方式。

    """

    def __init__(self):
        r"""
        :param _RecipientId: 签署方经办人在模板中配置的参与方ID，与控件绑定，是控件的归属方，ID为32位字符串。
        :type RecipientId: str
        :param _Values: 签署方经办人控件类型是个人印章签署控件（SIGN_SIGNATURE） 时，可选的签名方式。

签名方式：
<ul>
<li>HANDWRITE-手写签名</li>
<li>ESIGN-个人印章类型</li>
<li>OCR_ESIGN-AI智能识别手写签名</li>
<li>SYSTEM_ESIGN-系统签名</li>
</ul>
        :type Values: list of str
        """
        self._RecipientId = None
        self._Values = None

    @property
    def RecipientId(self):
        return self._RecipientId

    @RecipientId.setter
    def RecipientId(self, RecipientId):
        self._RecipientId = RecipientId

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._RecipientId = params.get("RecipientId")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApproverItem(AbstractModel):
    """签署方信息，发起合同后可获取到对应的签署方信息，如角色ID，角色名称

    """

    def __init__(self):
        r"""
        :param _SignId: 签署方唯一编号

在动态签署人场景下，可以用此编号确定参与方
注意：此字段可能返回 null，表示取不到有效值。
        :type SignId: str
        :param _RecipientId: 签署方角色编号
注意：此字段可能返回 null，表示取不到有效值。
        :type RecipientId: str
        :param _ApproverRoleName: 签署方角色名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproverRoleName: str
        """
        self._SignId = None
        self._RecipientId = None
        self._ApproverRoleName = None

    @property
    def SignId(self):
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def RecipientId(self):
        return self._RecipientId

    @RecipientId.setter
    def RecipientId(self, RecipientId):
        self._RecipientId = RecipientId

    @property
    def ApproverRoleName(self):
        return self._ApproverRoleName

    @ApproverRoleName.setter
    def ApproverRoleName(self, ApproverRoleName):
        self._ApproverRoleName = ApproverRoleName


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        self._RecipientId = params.get("RecipientId")
        self._ApproverRoleName = params.get("ApproverRoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApproverOption(AbstractModel):
    """签署人个性化能力信息

    """

    def __init__(self):
        r"""
        :param _HideOneKeySign: 是否隐藏一键签署 默认false-不隐藏true-隐藏
        :type HideOneKeySign: bool
        :param _FillType: 签署人信息补充类型，默认无需补充。

<ul><li> **1** : ( 动态签署人（可发起合同后再补充签署人信息）</li>
</ul>
        :type FillType: int
        """
        self._HideOneKeySign = None
        self._FillType = None

    @property
    def HideOneKeySign(self):
        return self._HideOneKeySign

    @HideOneKeySign.setter
    def HideOneKeySign(self, HideOneKeySign):
        self._HideOneKeySign = HideOneKeySign

    @property
    def FillType(self):
        return self._FillType

    @FillType.setter
    def FillType(self, FillType):
        self._FillType = FillType


    def _deserialize(self, params):
        self._HideOneKeySign = params.get("HideOneKeySign")
        self._FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApproverRestriction(AbstractModel):
    """指定签署人限制项

    """

    def __init__(self):
        r"""
        :param _Name: 指定签署人姓名
        :type Name: str
        :param _Mobile: 指定签署人手机号，11位数字
        :type Mobile: str
        :param _IdCardType: 指定签署人证件类型，ID_CARD-身份证，HONGKONG_AND_MACAO-港澳居民来往内地通行证，HONGKONG_MACAO_AND_TAIWAN-港澳台居民居住证
        :type IdCardType: str
        :param _IdCardNumber: 指定签署人证件号码，其中字母大写
        :type IdCardNumber: str
        """
        self._Name = None
        self._Mobile = None
        self._IdCardType = None
        self._IdCardNumber = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def IdCardType(self):
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def IdCardNumber(self):
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Mobile = params.get("Mobile")
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthFailMessage(AbstractModel):
    """授权出错信息

    """

    def __init__(self):
        r"""
        :param _ProxyOrganizationOpenId: 第三方应用平台的子客企业OpenId
        :type ProxyOrganizationOpenId: str
        :param _Message: 错误信息
        :type Message: str
        """
        self._ProxyOrganizationOpenId = None
        self._Message = None

    @property
    def ProxyOrganizationOpenId(self):
        return self._ProxyOrganizationOpenId

    @ProxyOrganizationOpenId.setter
    def ProxyOrganizationOpenId(self, ProxyOrganizationOpenId):
        self._ProxyOrganizationOpenId = ProxyOrganizationOpenId

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._ProxyOrganizationOpenId = params.get("ProxyOrganizationOpenId")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizedUser(AbstractModel):
    """授权用户

    """

    def __init__(self):
        r"""
        :param _OpenId: 第三方应用平台的用户openid
        :type OpenId: str
        """
        self._OpenId = None

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId


    def _deserialize(self, params):
        self._OpenId = params.get("OpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoSignConfig(AbstractModel):
    """自动签开启、签署相关配置

    """

    def __init__(self):
        r"""
        :param _UserInfo: 自动签开通个人用户的三要素
        :type UserInfo: :class:`tencentcloud.essbasic.v20210526.models.UserThreeFactor`
        :param _CertInfoCallback: 是否回调证书信息
        :type CertInfoCallback: bool
        :param _UserDefineSeal: 是否支持用户自定义签名印章
        :type UserDefineSeal: bool
        :param _SealImgCallback: 是否需要回调的时候返回印章(签名) 图片的 base64
        :type SealImgCallback: bool
        :param _CallbackUrl: 回调链接，如果渠道已经配置了，可以不传
        :type CallbackUrl: str
        :param _VerifyChannels: 开通时候的验证方式，取值：WEIXINAPP（微信人脸识别），INSIGHT（慧眼人脸认别），TELECOM（运营商三要素验证）。如果是小程序开通链接，支持传 WEIXINAPP / TELECOM。如果是 H5 开通链接，支持传 INSIGHT / TELECOM。默认值 WEIXINAPP / INSIGHT。
        :type VerifyChannels: list of str
        :param _LicenseType: 设置用户开通自动签时是否绑定个人自动签账号许可。一旦绑定后，将扣减购买的个人自动签账号许可一次（1年有效期），不可解绑释放。不传默认为绑定自动签账号许可。 0-绑定个人自动签账号许可，开通后将扣减购买的个人自动签账号许可一次
        :type LicenseType: int
        """
        self._UserInfo = None
        self._CertInfoCallback = None
        self._UserDefineSeal = None
        self._SealImgCallback = None
        self._CallbackUrl = None
        self._VerifyChannels = None
        self._LicenseType = None

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def CertInfoCallback(self):
        return self._CertInfoCallback

    @CertInfoCallback.setter
    def CertInfoCallback(self, CertInfoCallback):
        self._CertInfoCallback = CertInfoCallback

    @property
    def UserDefineSeal(self):
        return self._UserDefineSeal

    @UserDefineSeal.setter
    def UserDefineSeal(self, UserDefineSeal):
        self._UserDefineSeal = UserDefineSeal

    @property
    def SealImgCallback(self):
        return self._SealImgCallback

    @SealImgCallback.setter
    def SealImgCallback(self, SealImgCallback):
        self._SealImgCallback = SealImgCallback

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def VerifyChannels(self):
        return self._VerifyChannels

    @VerifyChannels.setter
    def VerifyChannels(self, VerifyChannels):
        self._VerifyChannels = VerifyChannels

    @property
    def LicenseType(self):
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = UserThreeFactor()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._CertInfoCallback = params.get("CertInfoCallback")
        self._UserDefineSeal = params.get("UserDefineSeal")
        self._SealImgCallback = params.get("SealImgCallback")
        self._CallbackUrl = params.get("CallbackUrl")
        self._VerifyChannels = params.get("VerifyChannels")
        self._LicenseType = params.get("LicenseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaseFlowInfo(AbstractModel):
    """基础流程信息

    """

    def __init__(self):
        r"""
        :param _FlowName: 合同流程名称
        :type FlowName: str
        :param _FlowType: 合同流程类型
<br/>客户自定义，用于合同分类展示
        :type FlowType: str
        :param _FlowDescription: 合同流程描述信息
        :type FlowDescription: str
        :param _Deadline: 合同流程截止时间，unix时间戳，单位秒
        :type Deadline: int
        :param _Unordered: 是否顺序签署(true:无序签,false:顺序签)
<br/>默认false，有序签署合同
        :type Unordered: bool
        :param _IntelligentStatus: 是否打开智能添加填写区(默认开启，打开:"OPEN" 关闭："CLOSE")
        :type IntelligentStatus: str
        :param _FormFields: 填写控件内容
        :type FormFields: list of FormField
        :param _NeedSignReview: 本企业(发起方企业)是否需要签署审批
<br/>true：开启发起方签署审批
<br/>false：不开启发起方签署审批
<br/>开启后，使用ChannelCreateFlowSignReview接口提交审批结果，才能继续完成签署
        :type NeedSignReview: bool
        :param _UserData: 用户流程自定义数据参数
        :type UserData: str
        :param _CcInfos: 抄送人信息
        :type CcInfos: list of CcInfo
        :param _NeedCreateReview: 是否需要开启发起方发起前审核
<br/>true：开启发起方发起前审核
<br/>false：不开启发起方发起前审核
<br/>当指定NeedCreateReview=true，则提交审核后，需要使用接口：ChannelCreateFlowSignReview，来完成发起前审核，审核通过后，可以继续查看，签署合同
        :type NeedCreateReview: bool
        :param _Components: 填写控件：文件发起使用
        :type Components: list of Component
        """
        self._FlowName = None
        self._FlowType = None
        self._FlowDescription = None
        self._Deadline = None
        self._Unordered = None
        self._IntelligentStatus = None
        self._FormFields = None
        self._NeedSignReview = None
        self._UserData = None
        self._CcInfos = None
        self._NeedCreateReview = None
        self._Components = None

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowType(self):
        return self._FlowType

    @FlowType.setter
    def FlowType(self, FlowType):
        self._FlowType = FlowType

    @property
    def FlowDescription(self):
        return self._FlowDescription

    @FlowDescription.setter
    def FlowDescription(self, FlowDescription):
        self._FlowDescription = FlowDescription

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def Unordered(self):
        return self._Unordered

    @Unordered.setter
    def Unordered(self, Unordered):
        self._Unordered = Unordered

    @property
    def IntelligentStatus(self):
        return self._IntelligentStatus

    @IntelligentStatus.setter
    def IntelligentStatus(self, IntelligentStatus):
        self._IntelligentStatus = IntelligentStatus

    @property
    def FormFields(self):
        return self._FormFields

    @FormFields.setter
    def FormFields(self, FormFields):
        self._FormFields = FormFields

    @property
    def NeedSignReview(self):
        return self._NeedSignReview

    @NeedSignReview.setter
    def NeedSignReview(self, NeedSignReview):
        self._NeedSignReview = NeedSignReview

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def CcInfos(self):
        return self._CcInfos

    @CcInfos.setter
    def CcInfos(self, CcInfos):
        self._CcInfos = CcInfos

    @property
    def NeedCreateReview(self):
        return self._NeedCreateReview

    @NeedCreateReview.setter
    def NeedCreateReview(self, NeedCreateReview):
        self._NeedCreateReview = NeedCreateReview

    @property
    def Components(self):
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components


    def _deserialize(self, params):
        self._FlowName = params.get("FlowName")
        self._FlowType = params.get("FlowType")
        self._FlowDescription = params.get("FlowDescription")
        self._Deadline = params.get("Deadline")
        self._Unordered = params.get("Unordered")
        self._IntelligentStatus = params.get("IntelligentStatus")
        if params.get("FormFields") is not None:
            self._FormFields = []
            for item in params.get("FormFields"):
                obj = FormField()
                obj._deserialize(item)
                self._FormFields.append(obj)
        self._NeedSignReview = params.get("NeedSignReview")
        self._UserData = params.get("UserData")
        if params.get("CcInfos") is not None:
            self._CcInfos = []
            for item in params.get("CcInfos"):
                obj = CcInfo()
                obj._deserialize(item)
                self._CcInfos.append(obj)
        self._NeedCreateReview = params.get("NeedCreateReview")
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self._Components.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcInfo(AbstractModel):
    """抄送信息

    """

    def __init__(self):
        r"""
        :param _Mobile: 被抄送人手机号，大陆11位手机号
        :type Mobile: str
        :param _Name: 被抄送人姓名
        :type Name: str
        :param _CcType: 被抄送人类型
0--个人. 1--员工
        :type CcType: int
        :param _CcPermission: 被抄送人权限
0--可查看
1--可查看也可下载
        :type CcPermission: int
        """
        self._Mobile = None
        self._Name = None
        self._CcType = None
        self._CcPermission = None

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CcType(self):
        return self._CcType

    @CcType.setter
    def CcType(self, CcType):
        self._CcType = CcType

    @property
    def CcPermission(self):
        return self._CcPermission

    @CcPermission.setter
    def CcPermission(self, CcPermission):
        self._CcPermission = CcPermission


    def _deserialize(self, params):
        self._Mobile = params.get("Mobile")
        self._Name = params.get("Name")
        self._CcType = params.get("CcType")
        self._CcPermission = params.get("CcPermission")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelBatchCancelFlowsRequest(AbstractModel):
    """ChannelBatchCancelFlows请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowIds: 签署流程Id数组，最多100个，超过100不处理
        :type FlowIds: list of str
        :param _CancelMessage: 撤销理由,不超过200个字符
        :type CancelMessage: str
        :param _CancelMessageFormat: 撤销理由自定义格式；选项：

- 0 默认格式
- 1 只保留身份信息：展示为【发起方】
- 2 保留身份信息+企业名称：展示为【发起方xxx公司】
- 3 保留身份信息+企业名称+经办人名称：展示为【发起方xxxx公司-经办人姓名】
        :type CancelMessageFormat: int
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._FlowIds = None
        self._CancelMessage = None
        self._CancelMessageFormat = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def CancelMessage(self):
        return self._CancelMessage

    @CancelMessage.setter
    def CancelMessage(self, CancelMessage):
        self._CancelMessage = CancelMessage

    @property
    def CancelMessageFormat(self):
        return self._CancelMessageFormat

    @CancelMessageFormat.setter
    def CancelMessageFormat(self, CancelMessageFormat):
        self._CancelMessageFormat = CancelMessageFormat

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._FlowIds = params.get("FlowIds")
        self._CancelMessage = params.get("CancelMessage")
        self._CancelMessageFormat = params.get("CancelMessageFormat")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelBatchCancelFlowsResponse(AbstractModel):
    """ChannelBatchCancelFlows返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailMessages: 签署流程批量撤销失败原因，错误信息与流程Id一一对应，成功为“”,失败则对应失败消息
        :type FailMessages: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailMessages = None
        self._RequestId = None

    @property
    def FailMessages(self):
        return self._FailMessages

    @FailMessages.setter
    def FailMessages(self, FailMessages):
        self._FailMessages = FailMessages

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailMessages = params.get("FailMessages")
        self._RequestId = params.get("RequestId")


class ChannelCancelFlowRequest(AbstractModel):
    """ChannelCancelFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 签署流程编号
        :type FlowId: str
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _CancelMessage: 撤回原因，最大不超过200字符
        :type CancelMessage: str
        :param _CancelMessageFormat: 撤销理由自定义格式；选项：
0 默认格式
1 只保留身份信息：展示为【发起方】
2 保留身份信息+企业名称：展示为【发起方xxx公司】
3 保留身份信息+企业名称+经办人名称：展示为【发起方xxxx公司-经办人姓名】
        :type CancelMessageFormat: int
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._FlowId = None
        self._Agent = None
        self._CancelMessage = None
        self._CancelMessageFormat = None
        self._Operator = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def CancelMessage(self):
        return self._CancelMessage

    @CancelMessage.setter
    def CancelMessage(self, CancelMessage):
        self._CancelMessage = CancelMessage

    @property
    def CancelMessageFormat(self):
        return self._CancelMessageFormat

    @CancelMessageFormat.setter
    def CancelMessageFormat(self, CancelMessageFormat):
        self._CancelMessageFormat = CancelMessageFormat

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._CancelMessage = params.get("CancelMessage")
        self._CancelMessageFormat = params.get("CancelMessageFormat")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCancelFlowResponse(AbstractModel):
    """ChannelCancelFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ChannelCancelMultiFlowSignQRCodeRequest(AbstractModel):
    """ChannelCancelMultiFlowSignQRCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _QrCodeId: 二维码id
        :type QrCodeId: str
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._QrCodeId = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def QrCodeId(self):
        return self._QrCodeId

    @QrCodeId.setter
    def QrCodeId(self, QrCodeId):
        self._QrCodeId = QrCodeId

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._QrCodeId = params.get("QrCodeId")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCancelMultiFlowSignQRCodeResponse(AbstractModel):
    """ChannelCancelMultiFlowSignQRCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ChannelCancelUserAutoSignEnableUrlRequest(AbstractModel):
    """ChannelCancelUserAutoSignEnableUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 渠道应用相关信息
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _Operator: 操作人信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param _SceneKey: 自动签场景: E_PRESCRIPTION_AUTO_SIGN 电子处方
        :type SceneKey: str
        :param _UserInfo: 指定撤销链接的用户信息，包含姓名、证件类型、证件号码。
        :type UserInfo: :class:`tencentcloud.essbasic.v20210526.models.UserThreeFactor`
        """
        self._Agent = None
        self._Operator = None
        self._SceneKey = None
        self._UserInfo = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def SceneKey(self):
        return self._SceneKey

    @SceneKey.setter
    def SceneKey(self, SceneKey):
        self._SceneKey = SceneKey

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._SceneKey = params.get("SceneKey")
        if params.get("UserInfo") is not None:
            self._UserInfo = UserThreeFactor()
            self._UserInfo._deserialize(params.get("UserInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCancelUserAutoSignEnableUrlResponse(AbstractModel):
    """ChannelCancelUserAutoSignEnableUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ChannelCreateBatchCancelFlowUrlRequest(AbstractModel):
    """ChannelCreateBatchCancelFlowUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowIds: 签署流程Id数组
        :type FlowIds: list of str
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._FlowIds = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._FlowIds = params.get("FlowIds")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateBatchCancelFlowUrlResponse(AbstractModel):
    """ChannelCreateBatchCancelFlowUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchCancelFlowUrl: 批量撤销url
        :type BatchCancelFlowUrl: str
        :param _FailMessages: 签署流程批量撤销失败原因
        :type FailMessages: list of str
        :param _UrlExpireOn: 签署撤销url过期时间-年月日-时分秒
        :type UrlExpireOn: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchCancelFlowUrl = None
        self._FailMessages = None
        self._UrlExpireOn = None
        self._RequestId = None

    @property
    def BatchCancelFlowUrl(self):
        return self._BatchCancelFlowUrl

    @BatchCancelFlowUrl.setter
    def BatchCancelFlowUrl(self, BatchCancelFlowUrl):
        self._BatchCancelFlowUrl = BatchCancelFlowUrl

    @property
    def FailMessages(self):
        return self._FailMessages

    @FailMessages.setter
    def FailMessages(self, FailMessages):
        self._FailMessages = FailMessages

    @property
    def UrlExpireOn(self):
        return self._UrlExpireOn

    @UrlExpireOn.setter
    def UrlExpireOn(self, UrlExpireOn):
        self._UrlExpireOn = UrlExpireOn

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BatchCancelFlowUrl = params.get("BatchCancelFlowUrl")
        self._FailMessages = params.get("FailMessages")
        self._UrlExpireOn = params.get("UrlExpireOn")
        self._RequestId = params.get("RequestId")


class ChannelCreateBatchSignUrlRequest(AbstractModel):
    """ChannelCreateBatchSignUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 关于渠道应用的相关信息，包括子客企业及应用编、号等详细内容，您可以参阅开发者中心所提供的 Agent 结构体以获取详细定义。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _Name: 签署方经办人的姓名。
经办人的姓名将用于身份认证和电子签名，请确保填写的姓名为签署方的真实姓名，而非昵称等代名。

注：`请确保和合同中填入的一致`
        :type Name: str
        :param _Mobile: 手机号码， 支持国内手机号11位数字(无需加+86前缀或其他字符)。
请确认手机号所有方为此业务通知方。

注：`请确保和合同中填入的一致,  若无法保持一致，请确保在发起和生成批量签署链接时传入相同的参与方证件信息`
        :type Mobile: str
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param _IdCardType: 证件类型，支持以下类型
<ul><li>**ID_CARD** : 居民身份证 (默认值)</li>
<li>**HONGKONG_AND_MACAO** : 港澳居民来往内地通行证</li>
<li>**HONGKONG_MACAO_AND_TAIWAN** : 港澳台居民居住证(格式同居民身份证)</li></ul>

注：`请确保和合同中填入的一致`
        :type IdCardType: str
        :param _IdCardNumber: 证件号码，应符合以下规则
<ul><li>居民身份证号码应为18位字符串，由数字和大写字母X组成（如存在X，请大写）。</li>
<li>港澳居民来往内地通行证号码应为9位字符串，第1位为“C”，第2位为英文字母（但“I”、“O”除外），后7位为阿拉伯数字。</li>
<li>港澳台居民居住证号码编码规则与中国大陆身份证相同，应为18位字符串。</li></ul>

注：`请确保和合同中填入的一致`
        :type IdCardNumber: str
        :param _NotifyType: 通知用户方式：
<ul>
<li>**NONE** : 不通知（默认）</li>
<li>**SMS** : 短信通知（发送短信通知到Mobile参数所传的手机号）</li>
</ul>
        :type NotifyType: str
        :param _FlowIds: 本次需要批量签署的合同流程ID列表。
可以不传,  如不传则是发给对方的所有待签署合同流程。

        :type FlowIds: list of str
        :param _OrganizationName: 目标签署人的企业名称，签署人如果是企业员工身份，需要传此参数。

注：
<ul>
<li>请确认该名称与企业营业执照中注册的名称一致。</li>
<li>如果名称中包含英文括号()，请使用中文括号（）代替。</li>
<li>请确保此企业已完成腾讯电子签企业认证。</li>
</ul>
        :type OrganizationName: str
        :param _JumpToDetail: 是否直接跳转至合同内容页面进行签署
<ul>
<li>**false**: 会跳转至批量合同流程的列表,  点击需要批量签署合同后进入合同内容页面进行签署(默认)</li>
<li>**true**: 跳过合同流程列表, 直接进入合同内容页面进行签署</li>
</ul>
        :type JumpToDetail: bool
        """
        self._Agent = None
        self._Name = None
        self._Mobile = None
        self._Operator = None
        self._IdCardType = None
        self._IdCardNumber = None
        self._NotifyType = None
        self._FlowIds = None
        self._OrganizationName = None
        self._JumpToDetail = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def IdCardType(self):
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def IdCardNumber(self):
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def NotifyType(self):
        return self._NotifyType

    @NotifyType.setter
    def NotifyType(self, NotifyType):
        self._NotifyType = NotifyType

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def JumpToDetail(self):
        return self._JumpToDetail

    @JumpToDetail.setter
    def JumpToDetail(self, JumpToDetail):
        self._JumpToDetail = JumpToDetail


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._Name = params.get("Name")
        self._Mobile = params.get("Mobile")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
        self._NotifyType = params.get("NotifyType")
        self._FlowIds = params.get("FlowIds")
        self._OrganizationName = params.get("OrganizationName")
        self._JumpToDetail = params.get("JumpToDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateBatchSignUrlResponse(AbstractModel):
    """ChannelCreateBatchSignUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SignUrl: 批量签署链接，以短链形式返回，短链的有效期参考回参中的 ExpiredTime。

注: `非小程序和APP集成使用`
        :type SignUrl: str
        :param _ExpiredTime: 链接过期时间以 Unix 时间戳格式表示，从生成链接时间起，往后7天有效期。过期后短链将失效，无法打开。
        :type ExpiredTime: int
        :param _MiniAppPath: 从客户小程序或者客户APP跳转至腾讯电子签小程序进行批量签署的跳转路径

注: `小程序和APP集成使用`
        :type MiniAppPath: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SignUrl = None
        self._ExpiredTime = None
        self._MiniAppPath = None
        self._RequestId = None

    @property
    def SignUrl(self):
        return self._SignUrl

    @SignUrl.setter
    def SignUrl(self, SignUrl):
        self._SignUrl = SignUrl

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def MiniAppPath(self):
        return self._MiniAppPath

    @MiniAppPath.setter
    def MiniAppPath(self, MiniAppPath):
        self._MiniAppPath = MiniAppPath

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SignUrl = params.get("SignUrl")
        self._ExpiredTime = params.get("ExpiredTime")
        self._MiniAppPath = params.get("MiniAppPath")
        self._RequestId = params.get("RequestId")


class ChannelCreateBoundFlowsRequest(AbstractModel):
    """ChannelCreateBoundFlows请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用信息
此接口Agent.AppId、Agent.ProxyOrganizationOpenId 和 Agent. ProxyOperator.OpenId 必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowIds: 领取的合同id列表
        :type FlowIds: list of str
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._FlowIds = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._FlowIds = params.get("FlowIds")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateBoundFlowsResponse(AbstractModel):
    """ChannelCreateBoundFlows返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ChannelCreateConvertTaskApiRequest(AbstractModel):
    """ChannelCreateConvertTaskApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _ResourceType: 资源类型 支持doc,docx,html,xls,xlsx,jpg,jpeg,png,bmp文件类型
        :type ResourceType: str
        :param _ResourceName: 资源名称，长度限制为256字符
        :type ResourceName: str
        :param _ResourceId: 文件Id，通过UploadFiles获取
        :type ResourceId: str
        :param _Operator: 调用方用户信息，不用传
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param _Organization: 暂未开放
        :type Organization: :class:`tencentcloud.essbasic.v20210526.models.OrganizationInfo`
        """
        self._Agent = None
        self._ResourceType = None
        self._ResourceName = None
        self._ResourceId = None
        self._Operator = None
        self._Organization = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator

    @property
    def Organization(self):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        self._Organization = Organization


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._ResourceType = params.get("ResourceType")
        self._ResourceName = params.get("ResourceName")
        self._ResourceId = params.get("ResourceId")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("Organization") is not None:
            self._Organization = OrganizationInfo()
            self._Organization._deserialize(params.get("Organization"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateConvertTaskApiResponse(AbstractModel):
    """ChannelCreateConvertTaskApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ChannelCreateEmbedWebUrlRequest(AbstractModel):
    """ChannelCreateEmbedWebUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 渠道应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _EmbedType: 要生成WEB嵌入界面的类型, 可以选择的值如下: 

- CREATE_SEAL: 生成创建印章的嵌入页面
- CREATE_TEMPLATE：生成创建模板的嵌入页面
- MODIFY_TEMPLATE：生成修改模板的嵌入页面
- PREVIEW_TEMPLATE：生成预览模板的嵌入页面
- PREVIEW_FLOW：生成预览合同文档的嵌入页面
- PREVIEW_FLOW_DETAIL：生成预览合同详情的嵌入页面
- PREVIEW_SEAL_LIST：生成预览印章列表的嵌入页面
- PREVIEW_SEAL_DETAIL：生成预览印章详情的嵌入页面
- EXTEND_SERVICE：生成扩展服务的嵌入页面
        :type EmbedType: str
        :param _BusinessId: WEB嵌入的业务资源ID

- 当EmbedType取值MODIFY_TEMPLATE，PREVIEW_TEMPLATE时需要填写模板id作为BusinessId
- 当EmbedType取值PREVIEW_FLOW，PREVIEW_FLOW_DETAIL时需要填写合同id作为BusinessId
- 当EmbedType取值PREVIEW_SEAL_DETAIL需要填写印章id作为BusinessId
        :type BusinessId: str
        :param _HiddenComponents: 是否隐藏控件，只有预览模板时生效
        :type HiddenComponents: bool
        :param _Operator: 渠道操作者信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._EmbedType = None
        self._BusinessId = None
        self._HiddenComponents = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def EmbedType(self):
        return self._EmbedType

    @EmbedType.setter
    def EmbedType(self, EmbedType):
        self._EmbedType = EmbedType

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def HiddenComponents(self):
        return self._HiddenComponents

    @HiddenComponents.setter
    def HiddenComponents(self, HiddenComponents):
        self._HiddenComponents = HiddenComponents

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._EmbedType = params.get("EmbedType")
        self._BusinessId = params.get("BusinessId")
        self._HiddenComponents = params.get("HiddenComponents")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateEmbedWebUrlResponse(AbstractModel):
    """ChannelCreateEmbedWebUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WebUrl: 嵌入的web链接
        :type WebUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WebUrl = None
        self._RequestId = None

    @property
    def WebUrl(self):
        return self._WebUrl

    @WebUrl.setter
    def WebUrl(self, WebUrl):
        self._WebUrl = WebUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._WebUrl = params.get("WebUrl")
        self._RequestId = params.get("RequestId")


class ChannelCreateFlowApproversRequest(AbstractModel):
    """ChannelCreateFlowApprovers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 渠道应用相关信息
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowId: 合同唯一编号
        :type FlowId: str
        :param _Approvers: 补充企业签署人信息。

- 如果发起方指定的补充签署人是企业签署人，则需要提供企业名称或者企业OpenId；

- 如果不指定，则使用姓名和手机号进行补充。
        :type Approvers: list of FillApproverInfo
        :param _Operator: 操作人信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param _FillApproverType: 签署人信息补充方式

<ul><li>**0**: 补充或签人，支持补充多个企业经办签署人（默认）注: `不可补充个人签署人`</li>
<li>**1**: 补充动态签署人，可补充企业和个人签署人。注: `每个签署方节点签署人是唯一的，一个节点只支持传入一个签署人信息`</li></ul>
        :type FillApproverType: int
        """
        self._Agent = None
        self._FlowId = None
        self._Approvers = None
        self._Operator = None
        self._FillApproverType = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Approvers(self):
        return self._Approvers

    @Approvers.setter
    def Approvers(self, Approvers):
        self._Approvers = Approvers

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def FillApproverType(self):
        return self._FillApproverType

    @FillApproverType.setter
    def FillApproverType(self, FillApproverType):
        self._FillApproverType = FillApproverType


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._FlowId = params.get("FlowId")
        if params.get("Approvers") is not None:
            self._Approvers = []
            for item in params.get("Approvers"):
                obj = FillApproverInfo()
                obj._deserialize(item)
                self._Approvers.append(obj)
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FillApproverType = params.get("FillApproverType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateFlowApproversResponse(AbstractModel):
    """ChannelCreateFlowApprovers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FillError: 批量补充签署人时，补充失败的报错说明 
注:`目前仅补充动态签署人时会返回补充失败的原因`	
注意：此字段可能返回 null，表示取不到有效值。
        :type FillError: list of FillError
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FillError = None
        self._RequestId = None

    @property
    def FillError(self):
        return self._FillError

    @FillError.setter
    def FillError(self, FillError):
        self._FillError = FillError

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FillError") is not None:
            self._FillError = []
            for item in params.get("FillError"):
                obj = FillError()
                obj._deserialize(item)
                self._FillError.append(obj)
        self._RequestId = params.get("RequestId")


class ChannelCreateFlowByFilesRequest(AbstractModel):
    """ChannelCreateFlowByFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 关于渠道应用的相关信息，包括渠道应用标识、第三方平台子客企业标识及第三方平台子客企业中的员工标识等内容，您可以参阅开发者中心所提供的 Agent 结构体以获取详细定义。

此接口下面信息必填。
<ul>
<li>渠道应用标识:  Agent.ProxyOrganizationOpenId</li>
<li>第三方平台子客企业标识: Agent. ProxyOperator.OpenId</li>
<li>第三方平台子客企业中的员工标识: Agent.AppId</li>
</ul>
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowName: 合同流程的名称（可自定义此名称），长度不能超过200，只能由中文、字母、数字和下划线组成。
        :type FlowName: str
        :param _FlowDescription: 合同流程描述信息(可自定义此描述)，最大长度1000个字符。
        :type FlowDescription: str
        :param _FlowApprovers: 合同流程的参与方列表, 最多可支持50个参与方，可在列表中指定企业B端签署方和个人C端签署方的联系和认证方式等信息，具体定义可以参考开发者中心的<a href="https://qian.tencent.com/developers/partnerApis/dataTypes/#flowapproverinfo" target="_blank">FlowApproverInfo结构体</a>。

如果合同流程是有序签署，Approvers列表中参与人的顺序就是默认的签署顺序, 请确保列表中参与人的顺序符合实际签署顺序。
        :type FlowApprovers: list of FlowApproverInfo
        :param _FileIds: 本合同流程需包含的PDF文件资源编号列表，通过<a href="https://qian.tencent.com/developers/partnerApis/files/UploadFiles" target="_blank">UploadFiles</a>接口获取PDF文件资源编号。

注: `目前，此接口仅支持单个文件发起。`
        :type FileIds: list of str
        :param _Components: 模板或者合同中的填写控件列表，列表中可支持下列多种填写控件，控件的详细定义参考开发者中心的Component结构体
<ul><li>单行文本控件</li>
<li>多行文本控件</li>
<li>勾选框控件</li>
<li>数字控件</li>
<li>图片控件</li>
<li>数据表格等填写控件</li></ul>
        :type Components: list of Component
        :param _Deadline: 合同流程的签署截止时间，格式为Unix标准时间戳（秒），如果未设置签署截止时间，则默认为合同流程创建后的365天时截止。
如果在签署截止时间前未完成签署，则合同状态会变为已过期，导致合同作废。
        :type Deadline: int
        :param _CallbackUrl: 执行结果的回调URL，长度不超过255个字符，该URL仅支持HTTP或HTTPS协议，建议采用HTTPS协议以保证数据传输的安全性。
腾讯电子签服务器将通过POST方式，application/json格式通知执行结果，请确保外网可以正常访问该URL。
回调的相关说明可参考开发者中心的<a href="https://qian.tencent.com/developers/partner/callback_data_types" target="_blank">回调通知</a>模块。

注:
`如果不传递回调地址， 则默认是配置应用号时候使用的回调地址`
        :type CallbackUrl: str
        :param _Unordered: 合同流程的签署顺序类型：
<ul><li> **false**：(默认)有序签署, 本合同多个参与人需要依次签署 </li>
<li> **true**：无序签署, 本合同多个参与人没有先后签署限制</li></ul>

注
`有序签署时以传入FlowApprovers数组的顺序作为签署顺序`
        :type Unordered: bool
        :param _FlowType: 合同流程的类别分类（可自定义名称，如销售合同/入职合同等），最大长度为255个字符，仅限中文、字母、数字和下划线组成。
        :type FlowType: str
        :param _CustomShowMap: 您可以自定义腾讯电子签小程序合同列表页展示的合同内容模板，模板中支持以下变量：
<ul><li>{合同名称}   </li>
<li>{发起方企业} </li>
<li>{发起方姓名} </li>
<li>{签署方N企业}</li>
<li>{签署方N姓名}</li></ul>
其中，N表示签署方的编号，从1开始，不能超过签署人的数量。

例如，如果是腾讯公司张三发给李四名称为“租房合同”的合同，您可以将此字段设置为：`合同名称:{合同名称};发起方: {发起方企业}({发起方姓名});签署方:{签署方1姓名}`，则小程序中列表页展示此合同为以下样子

合同名称：租房合同 
发起方：腾讯公司(张三) 
签署方：李四


        :type CustomShowMap: str
        :param _CustomerData: 调用方自定义的个性化字段(可自定义此名称)，并以base64方式编码，支持的最大数据大小为 1000长度。

在合同状态变更的回调信息等场景中，该字段的信息将原封不动地透传给贵方。回调的相关说明可参考开发者中心的<a href="https://qian.tencent.com/developers/partner/callback_types_contracts_sign" target="_blank">回调通知</a>模块。
        :type CustomerData: str
        :param _NeedSignReview: 发起方企业的签署人进行签署操作前，是否需要企业内部走审批流程，取值如下：
<ul><li> **false**：（默认）不需要审批，直接签署。</li>
<li> **true**：需要走审批流程。当到对应参与人签署时，会阻塞其签署操作，等待企业内部审批完成。</li></ul>
企业可以通过ChannelCreateFlowSignReview审批接口通知腾讯电子签平台企业内部审批结果
<ul><li> 如果企业通知腾讯电子签平台审核通过，签署方可继续签署动作。</li>
<li> 如果企业通知腾讯电子签平台审核未通过，平台将继续阻塞签署方的签署动作，直到企业通知平台审核通过。</li></ul>
注：`此功能可用于与企业内部的审批流程进行关联，支持手动、静默签署合同`
        :type NeedSignReview: bool
        :param _ApproverVerifyType: 签署人校验方式
VerifyCheck: 人脸识别（默认）
MobileCheck：手机号验证，用户手机号和参与方手机号（ApproverMobile）相同即可查看合同内容（当手写签名方式为OCR_ESIGN时，该校验方式无效，因为这种签名方式依赖实名认证）
参数说明：可选人脸识别或手机号验证两种方式，若选择后者，未实名个人签署方在签署合同时，无需经过实名认证和意愿确认两次人脸识别，该能力仅适用于个人签署方。
        :type ApproverVerifyType: str
        :param _SignBeanTag: 签署方签署控件（印章/签名等）的生成方式：
<ul><li> **0**：在合同流程发起时，由发起人指定签署方的签署控件的位置和数量。</li>
<li> **1**：签署方在签署时自行添加签署控件，可以拖动位置和控制数量。</li></ul>

注:
`发起后添加控件功能不支持添加签批控件`
        :type SignBeanTag: int
        :param _CcInfos: 合同流程的抄送人列表，最多可支持50个抄送人，抄送人可查看合同内容及签署进度，但无需参与合同签署。
        :type CcInfos: list of CcInfo
        :param _CcNotifyType: 可以设置以下时间节点来给抄送人发送短信通知来查看合同内容：
<ul><li> **0**：合同发起时通知（默认值）</li>
<li> **1**：签署完成后通知</li></ul>
        :type CcNotifyType: int
        :param _AutoSignScene: 个人自动签名的使用场景包括以下, 个人自动签署(即ApproverType设置成个人自动签署时)业务此值必传：
<ul><li> **E_PRESCRIPTION_AUTO_SIGN**：处方单（医疗自动签）  </li></ul>
注: `个人自动签名场景是白名单功能，使用前请与对接的客户经理联系沟通。`
        :type AutoSignScene: str
        :param _Operator: 操作者的信息，不用传
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._FlowName = None
        self._FlowDescription = None
        self._FlowApprovers = None
        self._FileIds = None
        self._Components = None
        self._Deadline = None
        self._CallbackUrl = None
        self._Unordered = None
        self._FlowType = None
        self._CustomShowMap = None
        self._CustomerData = None
        self._NeedSignReview = None
        self._ApproverVerifyType = None
        self._SignBeanTag = None
        self._CcInfos = None
        self._CcNotifyType = None
        self._AutoSignScene = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowDescription(self):
        return self._FlowDescription

    @FlowDescription.setter
    def FlowDescription(self, FlowDescription):
        self._FlowDescription = FlowDescription

    @property
    def FlowApprovers(self):
        return self._FlowApprovers

    @FlowApprovers.setter
    def FlowApprovers(self, FlowApprovers):
        self._FlowApprovers = FlowApprovers

    @property
    def FileIds(self):
        return self._FileIds

    @FileIds.setter
    def FileIds(self, FileIds):
        self._FileIds = FileIds

    @property
    def Components(self):
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def Unordered(self):
        return self._Unordered

    @Unordered.setter
    def Unordered(self, Unordered):
        self._Unordered = Unordered

    @property
    def FlowType(self):
        return self._FlowType

    @FlowType.setter
    def FlowType(self, FlowType):
        self._FlowType = FlowType

    @property
    def CustomShowMap(self):
        return self._CustomShowMap

    @CustomShowMap.setter
    def CustomShowMap(self, CustomShowMap):
        self._CustomShowMap = CustomShowMap

    @property
    def CustomerData(self):
        return self._CustomerData

    @CustomerData.setter
    def CustomerData(self, CustomerData):
        self._CustomerData = CustomerData

    @property
    def NeedSignReview(self):
        return self._NeedSignReview

    @NeedSignReview.setter
    def NeedSignReview(self, NeedSignReview):
        self._NeedSignReview = NeedSignReview

    @property
    def ApproverVerifyType(self):
        return self._ApproverVerifyType

    @ApproverVerifyType.setter
    def ApproverVerifyType(self, ApproverVerifyType):
        self._ApproverVerifyType = ApproverVerifyType

    @property
    def SignBeanTag(self):
        return self._SignBeanTag

    @SignBeanTag.setter
    def SignBeanTag(self, SignBeanTag):
        self._SignBeanTag = SignBeanTag

    @property
    def CcInfos(self):
        return self._CcInfos

    @CcInfos.setter
    def CcInfos(self, CcInfos):
        self._CcInfos = CcInfos

    @property
    def CcNotifyType(self):
        return self._CcNotifyType

    @CcNotifyType.setter
    def CcNotifyType(self, CcNotifyType):
        self._CcNotifyType = CcNotifyType

    @property
    def AutoSignScene(self):
        return self._AutoSignScene

    @AutoSignScene.setter
    def AutoSignScene(self, AutoSignScene):
        self._AutoSignScene = AutoSignScene

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._FlowName = params.get("FlowName")
        self._FlowDescription = params.get("FlowDescription")
        if params.get("FlowApprovers") is not None:
            self._FlowApprovers = []
            for item in params.get("FlowApprovers"):
                obj = FlowApproverInfo()
                obj._deserialize(item)
                self._FlowApprovers.append(obj)
        self._FileIds = params.get("FileIds")
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self._Components.append(obj)
        self._Deadline = params.get("Deadline")
        self._CallbackUrl = params.get("CallbackUrl")
        self._Unordered = params.get("Unordered")
        self._FlowType = params.get("FlowType")
        self._CustomShowMap = params.get("CustomShowMap")
        self._CustomerData = params.get("CustomerData")
        self._NeedSignReview = params.get("NeedSignReview")
        self._ApproverVerifyType = params.get("ApproverVerifyType")
        self._SignBeanTag = params.get("SignBeanTag")
        if params.get("CcInfos") is not None:
            self._CcInfos = []
            for item in params.get("CcInfos"):
                obj = CcInfo()
                obj._deserialize(item)
                self._CcInfos.append(obj)
        self._CcNotifyType = params.get("CcNotifyType")
        self._AutoSignScene = params.get("AutoSignScene")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateFlowByFilesResponse(AbstractModel):
    """ChannelCreateFlowByFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 合同签署流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: str
        :param _Approvers: 签署方信息，如角色ID、角色名称等
注意：此字段可能返回 null，表示取不到有效值。
        :type Approvers: list of ApproverItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._Approvers = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Approvers(self):
        return self._Approvers

    @Approvers.setter
    def Approvers(self, Approvers):
        self._Approvers = Approvers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("Approvers") is not None:
            self._Approvers = []
            for item in params.get("Approvers"):
                obj = ApproverItem()
                obj._deserialize(item)
                self._Approvers.append(obj)
        self._RequestId = params.get("RequestId")


class ChannelCreateFlowGroupByFilesRequest(AbstractModel):
    """ChannelCreateFlowGroupByFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowFileInfos: 每个子合同的发起所需的信息，数量限制2-50
        :type FlowFileInfos: list of FlowFileInfo
        :param _FlowGroupName: 合同组名称，长度不超过200个字符
        :type FlowGroupName: str
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _ApproverVerifyType: 签署人校验方式
VerifyCheck: 人脸识别（默认）
MobileCheck：手机号验证
参数说明：若选择后者，未实名的个人签署方查看合同时，无需进行人脸识别实名认证（但签署合同时仍然需要人脸实名），该能力仅适用于个人签署方。
        :type ApproverVerifyType: str
        :param _FlowGroupOptions: 合同组的配置项信息包括：在合同组签署过程中，是否需要对每个子合同进行独立的意愿确认。
        :type FlowGroupOptions: :class:`tencentcloud.essbasic.v20210526.models.FlowGroupOptions`
        :param _Operator: 操作者的信息，此参数不用传
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._FlowFileInfos = None
        self._FlowGroupName = None
        self._Agent = None
        self._ApproverVerifyType = None
        self._FlowGroupOptions = None
        self._Operator = None

    @property
    def FlowFileInfos(self):
        return self._FlowFileInfos

    @FlowFileInfos.setter
    def FlowFileInfos(self, FlowFileInfos):
        self._FlowFileInfos = FlowFileInfos

    @property
    def FlowGroupName(self):
        return self._FlowGroupName

    @FlowGroupName.setter
    def FlowGroupName(self, FlowGroupName):
        self._FlowGroupName = FlowGroupName

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def ApproverVerifyType(self):
        return self._ApproverVerifyType

    @ApproverVerifyType.setter
    def ApproverVerifyType(self, ApproverVerifyType):
        self._ApproverVerifyType = ApproverVerifyType

    @property
    def FlowGroupOptions(self):
        return self._FlowGroupOptions

    @FlowGroupOptions.setter
    def FlowGroupOptions(self, FlowGroupOptions):
        self._FlowGroupOptions = FlowGroupOptions

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("FlowFileInfos") is not None:
            self._FlowFileInfos = []
            for item in params.get("FlowFileInfos"):
                obj = FlowFileInfo()
                obj._deserialize(item)
                self._FlowFileInfos.append(obj)
        self._FlowGroupName = params.get("FlowGroupName")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._ApproverVerifyType = params.get("ApproverVerifyType")
        if params.get("FlowGroupOptions") is not None:
            self._FlowGroupOptions = FlowGroupOptions()
            self._FlowGroupOptions._deserialize(params.get("FlowGroupOptions"))
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateFlowGroupByFilesResponse(AbstractModel):
    """ChannelCreateFlowGroupByFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowGroupId: 合同组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowGroupId: str
        :param _FlowIds: 子合同ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowGroupId = None
        self._FlowIds = None
        self._RequestId = None

    @property
    def FlowGroupId(self):
        return self._FlowGroupId

    @FlowGroupId.setter
    def FlowGroupId(self, FlowGroupId):
        self._FlowGroupId = FlowGroupId

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowGroupId = params.get("FlowGroupId")
        self._FlowIds = params.get("FlowIds")
        self._RequestId = params.get("RequestId")


class ChannelCreateFlowGroupByTemplatesRequest(AbstractModel):
    """ChannelCreateFlowGroupByTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowInfos: 每个子合同的发起所需的信息，数量限制2-50（合同组暂不支持抄送功能）
        :type FlowInfos: list of FlowInfo
        :param _FlowGroupName: 合同组名称，长度不超过200个字符
        :type FlowGroupName: str
        """
        self._Agent = None
        self._FlowInfos = None
        self._FlowGroupName = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowInfos(self):
        return self._FlowInfos

    @FlowInfos.setter
    def FlowInfos(self, FlowInfos):
        self._FlowInfos = FlowInfos

    @property
    def FlowGroupName(self):
        return self._FlowGroupName

    @FlowGroupName.setter
    def FlowGroupName(self, FlowGroupName):
        self._FlowGroupName = FlowGroupName


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("FlowInfos") is not None:
            self._FlowInfos = []
            for item in params.get("FlowInfos"):
                obj = FlowInfo()
                obj._deserialize(item)
                self._FlowInfos.append(obj)
        self._FlowGroupName = params.get("FlowGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateFlowGroupByTemplatesResponse(AbstractModel):
    """ChannelCreateFlowGroupByTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowGroupId: 合同组ID
        :type FlowGroupId: str
        :param _FlowIds: 子合同ID列表
        :type FlowIds: list of str
        :param _TaskInfos: 复杂文档合成任务（如，包含动态表格的预览任务）的任务信息数组；
如果文档需要异步合成，此字段会返回该异步任务的任务信息，后续可以通过ChannelGetTaskResultApi接口查询任务详情；
        :type TaskInfos: list of TaskInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowGroupId = None
        self._FlowIds = None
        self._TaskInfos = None
        self._RequestId = None

    @property
    def FlowGroupId(self):
        return self._FlowGroupId

    @FlowGroupId.setter
    def FlowGroupId(self, FlowGroupId):
        self._FlowGroupId = FlowGroupId

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def TaskInfos(self):
        return self._TaskInfos

    @TaskInfos.setter
    def TaskInfos(self, TaskInfos):
        self._TaskInfos = TaskInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowGroupId = params.get("FlowGroupId")
        self._FlowIds = params.get("FlowIds")
        if params.get("TaskInfos") is not None:
            self._TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = TaskInfo()
                obj._deserialize(item)
                self._TaskInfos.append(obj)
        self._RequestId = params.get("RequestId")


class ChannelCreateFlowRemindsRequest(AbstractModel):
    """ChannelCreateFlowReminds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowIds: 签署流程Id数组，最多100个，超过100不处理
        :type FlowIds: list of str
        """
        self._Agent = None
        self._FlowIds = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._FlowIds = params.get("FlowIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateFlowRemindsResponse(AbstractModel):
    """ChannelCreateFlowReminds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RemindFlowRecords: 合同催办详情信息
        :type RemindFlowRecords: list of RemindFlowRecords
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RemindFlowRecords = None
        self._RequestId = None

    @property
    def RemindFlowRecords(self):
        return self._RemindFlowRecords

    @RemindFlowRecords.setter
    def RemindFlowRecords(self, RemindFlowRecords):
        self._RemindFlowRecords = RemindFlowRecords

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RemindFlowRecords") is not None:
            self._RemindFlowRecords = []
            for item in params.get("RemindFlowRecords"):
                obj = RemindFlowRecords()
                obj._deserialize(item)
                self._RemindFlowRecords.append(obj)
        self._RequestId = params.get("RequestId")


class ChannelCreateFlowSignReviewRequest(AbstractModel):
    """ChannelCreateFlowSignReview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowId: 签署流程编号
        :type FlowId: str
        :param _ReviewType: 企业内部审核结果
PASS: 通过
REJECT: 拒绝
SIGN_REJECT:拒签(流程结束)
        :type ReviewType: str
        :param _ReviewMessage: 审核原因 
当ReviewType 是REJECT 时此字段必填,字符串长度不超过200
        :type ReviewMessage: str
        :param _RecipientId: 签署节点审核时需要指定，给个人审核时必填。
        :type RecipientId: str
        :param _OperateType: 操作类型，默认：SignReview；SignReview:签署审核，CreateReview：发起审核
注：接口通过该字段区分操作类型
该字段不传或者为空，则默认为SignReview签署审核，走签署审核流程
若想使用发起审核，请指定该字段为：CreateReview
若发起个人审核，则指定该字段为：SignReview
        :type OperateType: str
        """
        self._Agent = None
        self._FlowId = None
        self._ReviewType = None
        self._ReviewMessage = None
        self._RecipientId = None
        self._OperateType = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ReviewType(self):
        return self._ReviewType

    @ReviewType.setter
    def ReviewType(self, ReviewType):
        self._ReviewType = ReviewType

    @property
    def ReviewMessage(self):
        return self._ReviewMessage

    @ReviewMessage.setter
    def ReviewMessage(self, ReviewMessage):
        self._ReviewMessage = ReviewMessage

    @property
    def RecipientId(self):
        return self._RecipientId

    @RecipientId.setter
    def RecipientId(self, RecipientId):
        self._RecipientId = RecipientId

    @property
    def OperateType(self):
        return self._OperateType

    @OperateType.setter
    def OperateType(self, OperateType):
        self._OperateType = OperateType


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._FlowId = params.get("FlowId")
        self._ReviewType = params.get("ReviewType")
        self._ReviewMessage = params.get("ReviewMessage")
        self._RecipientId = params.get("RecipientId")
        self._OperateType = params.get("OperateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateFlowSignReviewResponse(AbstractModel):
    """ChannelCreateFlowSignReview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ChannelCreateFlowSignUrlRequest(AbstractModel):
    """ChannelCreateFlowSignUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowId: 流程编号
        :type FlowId: str
        :param _FlowApproverInfos: 流程签署人，其中Name和Mobile必传，其他可不传，ApproverType目前只支持PERSON类型的签署人，如果不传默认为该值。还需注意签署人只能有手写签名和时间类型的签署控件，其他类型的填写控件和签署控件暂时都未支持。
        :type FlowApproverInfos: list of FlowApproverInfo
        :param _Operator: 用户信息，暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param _Organization: 机构信息，暂未开放
        :type Organization: :class:`tencentcloud.essbasic.v20210526.models.OrganizationInfo`
        :param _JumpUrl: 签署完之后的H5页面的跳转链接，此链接支持http://和https://，最大长度1000个字符。
        :type JumpUrl: str
        """
        self._Agent = None
        self._FlowId = None
        self._FlowApproverInfos = None
        self._Operator = None
        self._Organization = None
        self._JumpUrl = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def FlowApproverInfos(self):
        return self._FlowApproverInfos

    @FlowApproverInfos.setter
    def FlowApproverInfos(self, FlowApproverInfos):
        self._FlowApproverInfos = FlowApproverInfos

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator

    @property
    def Organization(self):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        self._Organization = Organization

    @property
    def JumpUrl(self):
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._FlowId = params.get("FlowId")
        if params.get("FlowApproverInfos") is not None:
            self._FlowApproverInfos = []
            for item in params.get("FlowApproverInfos"):
                obj = FlowApproverInfo()
                obj._deserialize(item)
                self._FlowApproverInfos.append(obj)
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("Organization") is not None:
            self._Organization = OrganizationInfo()
            self._Organization._deserialize(params.get("Organization"))
        self._JumpUrl = params.get("JumpUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateFlowSignUrlResponse(AbstractModel):
    """ChannelCreateFlowSignUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowApproverUrlInfos: 签署人签署链接信息
        :type FlowApproverUrlInfos: list of FlowApproverUrlInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowApproverUrlInfos = None
        self._RequestId = None

    @property
    def FlowApproverUrlInfos(self):
        return self._FlowApproverUrlInfos

    @FlowApproverUrlInfos.setter
    def FlowApproverUrlInfos(self, FlowApproverUrlInfos):
        self._FlowApproverUrlInfos = FlowApproverUrlInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FlowApproverUrlInfos") is not None:
            self._FlowApproverUrlInfos = []
            for item in params.get("FlowApproverUrlInfos"):
                obj = FlowApproverUrlInfo()
                obj._deserialize(item)
                self._FlowApproverUrlInfos.append(obj)
        self._RequestId = params.get("RequestId")


class ChannelCreateMultiFlowSignQRCodeRequest(AbstractModel):
    """ChannelCreateMultiFlowSignQRCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。
此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _TemplateId: 模版ID
        :type TemplateId: str
        :param _FlowName: 签署流程名称，最大长度200个字符。
        :type FlowName: str
        :param _MaxFlowNum: 最大可发起签署流程份数
<br/>默认5份
<br/>备注：发起签署流程数量超过此上限后，二维码自动失效。
        :type MaxFlowNum: int
        :param _FlowEffectiveDay: 签署流程有效天数 默认7天 最高设置不超过30天
        :type FlowEffectiveDay: int
        :param _QrEffectiveDay: 二维码有效天数 默认7天 最高设置不超过90天
        :type QrEffectiveDay: int
        :param _Restrictions: 指定的签署二维码签署人
<br/>指定后，只允许知道的人操作和签署
        :type Restrictions: list of ApproverRestriction
        :param _CallbackUrl: 已废弃，回调配置统一使用企业应用管理-应用集成-第三方应用中的配置
<br/> 通过一码多扫二维码发起的合同，回调消息可参考文档 https://qian.tencent.com/developers/partner/callback_types_contracts_sign
<br/> 用户通过签署二维码发起合同时，因企业额度不足导致失败 会触发签署二维码相关回调,具体参考文档 https://qian.tencent.com/developers/partner/callback_types_commons#%E7%AD%BE%E7%BD%B2%E4%BA%8C%E7%BB%B4%E7%A0%81%E7%9B%B8%E5%85%B3%E5%9B%9E%E8%B0%83
        :type CallbackUrl: str
        :param _ApproverRestrictions: 限制二维码用户条件（已弃用）
        :type ApproverRestrictions: :class:`tencentcloud.essbasic.v20210526.models.ApproverRestriction`
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param _ApproverComponentLimitTypes: 指定签署方经办人控件类型是个人印章签署控件（SIGN_SIGNATURE） 时，可选的签名方式。
        :type ApproverComponentLimitTypes: list of ApproverComponentLimitType
        """
        self._Agent = None
        self._TemplateId = None
        self._FlowName = None
        self._MaxFlowNum = None
        self._FlowEffectiveDay = None
        self._QrEffectiveDay = None
        self._Restrictions = None
        self._CallbackUrl = None
        self._ApproverRestrictions = None
        self._Operator = None
        self._ApproverComponentLimitTypes = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def MaxFlowNum(self):
        return self._MaxFlowNum

    @MaxFlowNum.setter
    def MaxFlowNum(self, MaxFlowNum):
        self._MaxFlowNum = MaxFlowNum

    @property
    def FlowEffectiveDay(self):
        return self._FlowEffectiveDay

    @FlowEffectiveDay.setter
    def FlowEffectiveDay(self, FlowEffectiveDay):
        self._FlowEffectiveDay = FlowEffectiveDay

    @property
    def QrEffectiveDay(self):
        return self._QrEffectiveDay

    @QrEffectiveDay.setter
    def QrEffectiveDay(self, QrEffectiveDay):
        self._QrEffectiveDay = QrEffectiveDay

    @property
    def Restrictions(self):
        return self._Restrictions

    @Restrictions.setter
    def Restrictions(self, Restrictions):
        self._Restrictions = Restrictions

    @property
    def CallbackUrl(self):
        warnings.warn("parameter `CallbackUrl` is deprecated", DeprecationWarning) 

        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        warnings.warn("parameter `CallbackUrl` is deprecated", DeprecationWarning) 

        self._CallbackUrl = CallbackUrl

    @property
    def ApproverRestrictions(self):
        warnings.warn("parameter `ApproverRestrictions` is deprecated", DeprecationWarning) 

        return self._ApproverRestrictions

    @ApproverRestrictions.setter
    def ApproverRestrictions(self, ApproverRestrictions):
        warnings.warn("parameter `ApproverRestrictions` is deprecated", DeprecationWarning) 

        self._ApproverRestrictions = ApproverRestrictions

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator

    @property
    def ApproverComponentLimitTypes(self):
        return self._ApproverComponentLimitTypes

    @ApproverComponentLimitTypes.setter
    def ApproverComponentLimitTypes(self, ApproverComponentLimitTypes):
        self._ApproverComponentLimitTypes = ApproverComponentLimitTypes


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._TemplateId = params.get("TemplateId")
        self._FlowName = params.get("FlowName")
        self._MaxFlowNum = params.get("MaxFlowNum")
        self._FlowEffectiveDay = params.get("FlowEffectiveDay")
        self._QrEffectiveDay = params.get("QrEffectiveDay")
        if params.get("Restrictions") is not None:
            self._Restrictions = []
            for item in params.get("Restrictions"):
                obj = ApproverRestriction()
                obj._deserialize(item)
                self._Restrictions.append(obj)
        self._CallbackUrl = params.get("CallbackUrl")
        if params.get("ApproverRestrictions") is not None:
            self._ApproverRestrictions = ApproverRestriction()
            self._ApproverRestrictions._deserialize(params.get("ApproverRestrictions"))
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("ApproverComponentLimitTypes") is not None:
            self._ApproverComponentLimitTypes = []
            for item in params.get("ApproverComponentLimitTypes"):
                obj = ApproverComponentLimitType()
                obj._deserialize(item)
                self._ApproverComponentLimitTypes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateMultiFlowSignQRCodeResponse(AbstractModel):
    """ChannelCreateMultiFlowSignQRCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QrCode: 签署二维码对象
        :type QrCode: :class:`tencentcloud.essbasic.v20210526.models.SignQrCode`
        :param _SignUrls: 签署链接对象
        :type SignUrls: :class:`tencentcloud.essbasic.v20210526.models.SignUrl`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QrCode = None
        self._SignUrls = None
        self._RequestId = None

    @property
    def QrCode(self):
        return self._QrCode

    @QrCode.setter
    def QrCode(self, QrCode):
        self._QrCode = QrCode

    @property
    def SignUrls(self):
        return self._SignUrls

    @SignUrls.setter
    def SignUrls(self, SignUrls):
        self._SignUrls = SignUrls

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("QrCode") is not None:
            self._QrCode = SignQrCode()
            self._QrCode._deserialize(params.get("QrCode"))
        if params.get("SignUrls") is not None:
            self._SignUrls = SignUrl()
            self._SignUrls._deserialize(params.get("SignUrls"))
        self._RequestId = params.get("RequestId")


class ChannelCreateOrganizationBatchSignUrlRequest(AbstractModel):
    """ChannelCreateOrganizationBatchSignUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 关于渠道应用的相关信息，包括子客企业及应用编、号等详细内容，您可以参阅开发者中心所提供的 Agent 结构体以获取详细定义。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowIds: 请指定需执行批量签署的流程ID，数量范围为1-100。 您可登录腾讯电子签控制台，浏览 "合同"->"合同中心" 以查阅某一合同的FlowId（在页面中显示为合同ID）。 用户将利用链接对这些合同实施批量操作。	
        :type FlowIds: list of str
        :param _OpenId: 第三方应用平台的用户openid。 您可登录腾讯电子签控制台，在 "更多能力"->"组织管理" 中查阅某位员工的OpenId。 OpenId必须是传入合同（FlowId）中的签署人。 - 1. 若OpenId为空，Name和Mobile 必须提供。 - 2. 若OpenId 与 Name，Mobile均存在，将优先采用OpenId对应的员工。	
        :type OpenId: str
        :param _Name: 签署方经办人的姓名。
经办人的姓名将用于身份认证和电子签名，请确保填写的姓名为签署方的真实姓名，而非昵称等代名。

注：`请确保和合同中填入的一致`
        :type Name: str
        :param _Mobile: 员工手机号，必须与姓名一起使用。 如果OpenId为空，则此字段不能为空。同时，姓名和手机号码必须与传入合同（FlowId）中的签署人信息一致。	
        :type Mobile: str
        """
        self._Agent = None
        self._FlowIds = None
        self._OpenId = None
        self._Name = None
        self._Mobile = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._FlowIds = params.get("FlowIds")
        self._OpenId = params.get("OpenId")
        self._Name = params.get("Name")
        self._Mobile = params.get("Mobile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateOrganizationBatchSignUrlResponse(AbstractModel):
    """ChannelCreateOrganizationBatchSignUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SignUrl: 批量签署入口链接，用户可使用这个链接跳转到控制台页面对合同进行签署操作。	
        :type SignUrl: str
        :param _ExpiredTime: 链接过期时间以 Unix 时间戳格式表示，从生成链接时间起，往后7天有效期。过期后短链将失效，无法打开。
        :type ExpiredTime: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SignUrl = None
        self._ExpiredTime = None
        self._RequestId = None

    @property
    def SignUrl(self):
        return self._SignUrl

    @SignUrl.setter
    def SignUrl(self, SignUrl):
        self._SignUrl = SignUrl

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SignUrl = params.get("SignUrl")
        self._ExpiredTime = params.get("ExpiredTime")
        self._RequestId = params.get("RequestId")


class ChannelCreateOrganizationModifyQrCodeRequest(AbstractModel):
    """ChannelCreateOrganizationModifyQrCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        """
        self._Agent = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateOrganizationModifyQrCodeResponse(AbstractModel):
    """ChannelCreateOrganizationModifyQrCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QrCodeUrl: 二维码下载链接
        :type QrCodeUrl: str
        :param _ExpiredTime: 二维码失效时间 UNIX 时间戳 精确到秒
        :type ExpiredTime: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QrCodeUrl = None
        self._ExpiredTime = None
        self._RequestId = None

    @property
    def QrCodeUrl(self):
        return self._QrCodeUrl

    @QrCodeUrl.setter
    def QrCodeUrl(self, QrCodeUrl):
        self._QrCodeUrl = QrCodeUrl

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._QrCodeUrl = params.get("QrCodeUrl")
        self._ExpiredTime = params.get("ExpiredTime")
        self._RequestId = params.get("RequestId")


class ChannelCreatePrepareFlowRequest(AbstractModel):
    """ChannelCreatePrepareFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源id，与ResourceType对应
        :type ResourceId: str
        :param _ResourceType: 资源类型，与ResourceId对应1：模板   2: 文件
        :type ResourceType: int
        :param _FlowInfo: 合同流程基础信息
        :type FlowInfo: :class:`tencentcloud.essbasic.v20210526.models.BaseFlowInfo`
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowOption: 合同流程配置信息，用于配置发起合同时定制化
        :type FlowOption: :class:`tencentcloud.essbasic.v20210526.models.CreateFlowOption`
        :param _FlowApproverList: 合同签署人信息
        :type FlowApproverList: list of CommonFlowApprover
        :param _FlowId: 通过flowid快速获得之前成功通过页面发起的合同生成链接
        :type FlowId: str
        :param _NeedPreview: 该参数不可用，请通过获取 web 可嵌入接口获取合同流程预览 URL
        :type NeedPreview: bool
        :param _Organization: 企业机构信息，不用传
        :type Organization: :class:`tencentcloud.essbasic.v20210526.models.OrganizationInfo`
        :param _Operator: 操作人（用户）信息，不用传
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._ResourceId = None
        self._ResourceType = None
        self._FlowInfo = None
        self._Agent = None
        self._FlowOption = None
        self._FlowApproverList = None
        self._FlowId = None
        self._NeedPreview = None
        self._Organization = None
        self._Operator = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def FlowInfo(self):
        return self._FlowInfo

    @FlowInfo.setter
    def FlowInfo(self, FlowInfo):
        self._FlowInfo = FlowInfo

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowOption(self):
        return self._FlowOption

    @FlowOption.setter
    def FlowOption(self, FlowOption):
        self._FlowOption = FlowOption

    @property
    def FlowApproverList(self):
        return self._FlowApproverList

    @FlowApproverList.setter
    def FlowApproverList(self, FlowApproverList):
        self._FlowApproverList = FlowApproverList

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def NeedPreview(self):
        warnings.warn("parameter `NeedPreview` is deprecated", DeprecationWarning) 

        return self._NeedPreview

    @NeedPreview.setter
    def NeedPreview(self, NeedPreview):
        warnings.warn("parameter `NeedPreview` is deprecated", DeprecationWarning) 

        self._NeedPreview = NeedPreview

    @property
    def Organization(self):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        self._Organization = Organization

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        if params.get("FlowInfo") is not None:
            self._FlowInfo = BaseFlowInfo()
            self._FlowInfo._deserialize(params.get("FlowInfo"))
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("FlowOption") is not None:
            self._FlowOption = CreateFlowOption()
            self._FlowOption._deserialize(params.get("FlowOption"))
        if params.get("FlowApproverList") is not None:
            self._FlowApproverList = []
            for item in params.get("FlowApproverList"):
                obj = CommonFlowApprover()
                obj._deserialize(item)
                self._FlowApproverList.append(obj)
        self._FlowId = params.get("FlowId")
        self._NeedPreview = params.get("NeedPreview")
        if params.get("Organization") is not None:
            self._Organization = OrganizationInfo()
            self._Organization._deserialize(params.get("Organization"))
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreatePrepareFlowResponse(AbstractModel):
    """ChannelCreatePrepareFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PrepareFlowUrl: 预发起的合同链接， 可以直接点击进入进行合同发起
        :type PrepareFlowUrl: str
        :param _PreviewFlowUrl: 合同发起后预览链接， 注意此时合同并未发起，仅只是展示效果
        :type PreviewFlowUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PrepareFlowUrl = None
        self._PreviewFlowUrl = None
        self._RequestId = None

    @property
    def PrepareFlowUrl(self):
        return self._PrepareFlowUrl

    @PrepareFlowUrl.setter
    def PrepareFlowUrl(self, PrepareFlowUrl):
        self._PrepareFlowUrl = PrepareFlowUrl

    @property
    def PreviewFlowUrl(self):
        return self._PreviewFlowUrl

    @PreviewFlowUrl.setter
    def PreviewFlowUrl(self, PreviewFlowUrl):
        self._PreviewFlowUrl = PreviewFlowUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PrepareFlowUrl = params.get("PrepareFlowUrl")
        self._PreviewFlowUrl = params.get("PreviewFlowUrl")
        self._RequestId = params.get("RequestId")


class ChannelCreatePreparedPersonalEsignRequest(AbstractModel):
    """ChannelCreatePreparedPersonalEsign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _UserName: 个人用户姓名
        :type UserName: str
        :param _IdCardNumber: 身份证件号码
        :type IdCardNumber: str
        :param _SealName: 印章名称
        :type SealName: str
        :param _SealImage: 印章图片的base64，最大不超过 8M
        :type SealImage: str
        :param _Operator: 操作者信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param _IdCardType: 身份证件类型
        :type IdCardType: str
        :param _SealImageCompress: 是否开启印章图片压缩处理，默认不开启，如需开启请设置为 true。当印章超过 2M 时建议开启，开启后图片的 hash 将发生变化。
        :type SealImageCompress: bool
        :param _Mobile: 手机号码；当需要开通自动签时，该参数必传
        :type Mobile: str
        :param _EnableAutoSign: 是否开通自动签，该功能需联系运营工作人员开通后使用
        :type EnableAutoSign: bool
        :param _LicenseType: 设置用户开通自动签时是否绑定个人自动签账号许可。一旦绑定后，将扣减购买的个人自动签账号许可一次（1年有效期），不可解绑释放。不传默认为绑定自动签账号许可。 0-绑定个人自动签账号许可，开通后将扣减购买的个人自动签账号许可一次 1-不绑定，发起合同时将按标准合同套餐进行扣减	
        :type LicenseType: int
        """
        self._Agent = None
        self._UserName = None
        self._IdCardNumber = None
        self._SealName = None
        self._SealImage = None
        self._Operator = None
        self._IdCardType = None
        self._SealImageCompress = None
        self._Mobile = None
        self._EnableAutoSign = None
        self._LicenseType = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def IdCardNumber(self):
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def SealName(self):
        return self._SealName

    @SealName.setter
    def SealName(self, SealName):
        self._SealName = SealName

    @property
    def SealImage(self):
        return self._SealImage

    @SealImage.setter
    def SealImage(self, SealImage):
        self._SealImage = SealImage

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def IdCardType(self):
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def SealImageCompress(self):
        return self._SealImageCompress

    @SealImageCompress.setter
    def SealImageCompress(self, SealImageCompress):
        self._SealImageCompress = SealImageCompress

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def EnableAutoSign(self):
        return self._EnableAutoSign

    @EnableAutoSign.setter
    def EnableAutoSign(self, EnableAutoSign):
        self._EnableAutoSign = EnableAutoSign

    @property
    def LicenseType(self):
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._UserName = params.get("UserName")
        self._IdCardNumber = params.get("IdCardNumber")
        self._SealName = params.get("SealName")
        self._SealImage = params.get("SealImage")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._IdCardType = params.get("IdCardType")
        self._SealImageCompress = params.get("SealImageCompress")
        self._Mobile = params.get("Mobile")
        self._EnableAutoSign = params.get("EnableAutoSign")
        self._LicenseType = params.get("LicenseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreatePreparedPersonalEsignResponse(AbstractModel):
    """ChannelCreatePreparedPersonalEsign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SealId: 导入的印章 ID
        :type SealId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SealId = None
        self._RequestId = None

    @property
    def SealId(self):
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SealId = params.get("SealId")
        self._RequestId = params.get("RequestId")


class ChannelCreateReleaseFlowRequest(AbstractModel):
    """ChannelCreateReleaseFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _NeedRelievedFlowId: 待解除的流程编号（即原流程的编号）
        :type NeedRelievedFlowId: str
        :param _ReliveInfo: 解除协议内容
        :type ReliveInfo: :class:`tencentcloud.essbasic.v20210526.models.RelieveInfo`
        :param _ReleasedApprovers: 非必须，解除协议的本企业签署人列表，默认使用原流程的签署人列表；当解除协议的签署人与原流程的签署人不能相同时（例如原流程签署人离职了），需要指定本企业的其他签署人来替换原流程中的原签署人，注意需要指明ApproverNumber来代表需要替换哪一个签署人，已转发的签署人不包含在内，解除协议的签署人数量不能多于原流程的签署人数量
        :type ReleasedApprovers: list of ReleasedApprover
        :param _CallbackUrl: 签署完回调url，最大长度1000个字符
        :type CallbackUrl: str
        :param _Organization: 暂未开放
        :type Organization: :class:`tencentcloud.essbasic.v20210526.models.OrganizationInfo`
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param _Deadline: 签署流程的签署截止时间。 值为unix时间戳,精确到秒,不传默认为当前时间七天后
        :type Deadline: int
        """
        self._Agent = None
        self._NeedRelievedFlowId = None
        self._ReliveInfo = None
        self._ReleasedApprovers = None
        self._CallbackUrl = None
        self._Organization = None
        self._Operator = None
        self._Deadline = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def NeedRelievedFlowId(self):
        return self._NeedRelievedFlowId

    @NeedRelievedFlowId.setter
    def NeedRelievedFlowId(self, NeedRelievedFlowId):
        self._NeedRelievedFlowId = NeedRelievedFlowId

    @property
    def ReliveInfo(self):
        return self._ReliveInfo

    @ReliveInfo.setter
    def ReliveInfo(self, ReliveInfo):
        self._ReliveInfo = ReliveInfo

    @property
    def ReleasedApprovers(self):
        return self._ReleasedApprovers

    @ReleasedApprovers.setter
    def ReleasedApprovers(self, ReleasedApprovers):
        self._ReleasedApprovers = ReleasedApprovers

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def Organization(self):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        self._Organization = Organization

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._NeedRelievedFlowId = params.get("NeedRelievedFlowId")
        if params.get("ReliveInfo") is not None:
            self._ReliveInfo = RelieveInfo()
            self._ReliveInfo._deserialize(params.get("ReliveInfo"))
        if params.get("ReleasedApprovers") is not None:
            self._ReleasedApprovers = []
            for item in params.get("ReleasedApprovers"):
                obj = ReleasedApprover()
                obj._deserialize(item)
                self._ReleasedApprovers.append(obj)
        self._CallbackUrl = params.get("CallbackUrl")
        if params.get("Organization") is not None:
            self._Organization = OrganizationInfo()
            self._Organization._deserialize(params.get("Organization"))
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._Deadline = params.get("Deadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateReleaseFlowResponse(AbstractModel):
    """ChannelCreateReleaseFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 解除协议流程编号
        :type FlowId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ChannelCreateRoleRequest(AbstractModel):
    """ChannelCreateRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 角色名称，最大长度为20个字符，仅限中文、字母、数字和下划线组成。
        :type Name: str
        :param _Agent: 代理企业和员工的信息。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _Description: 角色描述，最大长度为50个字符
        :type Description: str
        :param _PermissionGroups: 权限树，权限树内容 PermissionGroups 可参考接口 DescribeIntegrationRoles 的输出
        :type PermissionGroups: list of PermissionGroup
        """
        self._Name = None
        self._Agent = None
        self._Description = None
        self._PermissionGroups = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PermissionGroups(self):
        return self._PermissionGroups

    @PermissionGroups.setter
    def PermissionGroups(self, PermissionGroups):
        self._PermissionGroups = PermissionGroups


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._Description = params.get("Description")
        if params.get("PermissionGroups") is not None:
            self._PermissionGroups = []
            for item in params.get("PermissionGroups"):
                obj = PermissionGroup()
                obj._deserialize(item)
                self._PermissionGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateRoleResponse(AbstractModel):
    """ChannelCreateRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色id
        :type RoleId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleId = None
        self._RequestId = None

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._RequestId = params.get("RequestId")


class ChannelCreateSealPolicyRequest(AbstractModel):
    """ChannelCreateSealPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _SealId: 指定印章ID
        :type SealId: str
        :param _UserIds: 指定待授权的用户ID数组,电子签的用户ID
可以填写OpenId，系统会通过组织+渠道+OpenId查询得到UserId进行授权。
        :type UserIds: list of str
        :param _Operator: 操作人（用户）信息，不用传
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param _Organization: 企业机构信息，不用传
        :type Organization: :class:`tencentcloud.essbasic.v20210526.models.OrganizationInfo`
        """
        self._Agent = None
        self._SealId = None
        self._UserIds = None
        self._Operator = None
        self._Organization = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def SealId(self):
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator

    @property
    def Organization(self):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        self._Organization = Organization


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._SealId = params.get("SealId")
        self._UserIds = params.get("UserIds")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("Organization") is not None:
            self._Organization = OrganizationInfo()
            self._Organization._deserialize(params.get("Organization"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateSealPolicyResponse(AbstractModel):
    """ChannelCreateSealPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserIds: 最终授权成功的电子签系统用户ID数组。其他的跳过的是已经授权了的。
请求参数填写OpenId时，返回授权成功的 Openid。
        :type UserIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserIds = None
        self._RequestId = None

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserIds = params.get("UserIds")
        self._RequestId = params.get("RequestId")


class ChannelCreateUserAutoSignEnableUrlRequest(AbstractModel):
    """ChannelCreateUserAutoSignEnableUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 渠道应用相关信息
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _SceneKey: 自动签场景:
E_PRESCRIPTION_AUTO_SIGN 电子处方
        :type SceneKey: str
        :param _Operator: 操作人信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param _AutoSignConfig: 自动签开通，签署相关配置
        :type AutoSignConfig: :class:`tencentcloud.essbasic.v20210526.models.AutoSignConfig`
        :param _UrlType: 链接类型，空-默认小程序端链接，H5SIGN-h5端链接
        :type UrlType: str
        :param _NotifyType: 通知类型，默认不填为不通知开通方，填写 SMS 为短信通知。
        :type NotifyType: str
        :param _NotifyAddress: 若上方填写为 SMS，则此处为手机号
        :type NotifyAddress: str
        :param _ExpiredTime: 链接的过期时间，格式为Unix时间戳，不能早于当前时间，且最大为30天。如果不传，默认有效期为7天。
        :type ExpiredTime: int
        """
        self._Agent = None
        self._SceneKey = None
        self._Operator = None
        self._AutoSignConfig = None
        self._UrlType = None
        self._NotifyType = None
        self._NotifyAddress = None
        self._ExpiredTime = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def SceneKey(self):
        return self._SceneKey

    @SceneKey.setter
    def SceneKey(self, SceneKey):
        self._SceneKey = SceneKey

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def AutoSignConfig(self):
        return self._AutoSignConfig

    @AutoSignConfig.setter
    def AutoSignConfig(self, AutoSignConfig):
        self._AutoSignConfig = AutoSignConfig

    @property
    def UrlType(self):
        return self._UrlType

    @UrlType.setter
    def UrlType(self, UrlType):
        self._UrlType = UrlType

    @property
    def NotifyType(self):
        return self._NotifyType

    @NotifyType.setter
    def NotifyType(self, NotifyType):
        self._NotifyType = NotifyType

    @property
    def NotifyAddress(self):
        return self._NotifyAddress

    @NotifyAddress.setter
    def NotifyAddress(self, NotifyAddress):
        self._NotifyAddress = NotifyAddress

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._SceneKey = params.get("SceneKey")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("AutoSignConfig") is not None:
            self._AutoSignConfig = AutoSignConfig()
            self._AutoSignConfig._deserialize(params.get("AutoSignConfig"))
        self._UrlType = params.get("UrlType")
        self._NotifyType = params.get("NotifyType")
        self._NotifyAddress = params.get("NotifyAddress")
        self._ExpiredTime = params.get("ExpiredTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateUserAutoSignEnableUrlResponse(AbstractModel):
    """ChannelCreateUserAutoSignEnableUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 跳转短链
        :type Url: str
        :param _AppId: 小程序AppId
        :type AppId: str
        :param _AppOriginalId: 小程序 原始 Id
        :type AppOriginalId: str
        :param _Path: 跳转路径
        :type Path: str
        :param _QrCode: base64格式跳转二维码
        :type QrCode: str
        :param _UrlType: 链接类型，空-默认小程序端链接，H5SIGN-h5端链接
        :type UrlType: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._AppId = None
        self._AppOriginalId = None
        self._Path = None
        self._QrCode = None
        self._UrlType = None
        self._RequestId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppOriginalId(self):
        return self._AppOriginalId

    @AppOriginalId.setter
    def AppOriginalId(self, AppOriginalId):
        self._AppOriginalId = AppOriginalId

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def QrCode(self):
        return self._QrCode

    @QrCode.setter
    def QrCode(self, QrCode):
        self._QrCode = QrCode

    @property
    def UrlType(self):
        return self._UrlType

    @UrlType.setter
    def UrlType(self, UrlType):
        self._UrlType = UrlType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._AppId = params.get("AppId")
        self._AppOriginalId = params.get("AppOriginalId")
        self._Path = params.get("Path")
        self._QrCode = params.get("QrCode")
        self._UrlType = params.get("UrlType")
        self._RequestId = params.get("RequestId")


class ChannelCreateUserAutoSignSealUrlRequest(AbstractModel):
    """ChannelCreateUserAutoSignSealUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 渠道应用相关信息。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _SceneKey: 自动签使用的场景值, 可以选择的场景值如下:
<ul><li> **E_PRESCRIPTION_AUTO_SIGN** :  电子处方场景</li></ul>

注: `现在仅支持电子处方场景`
        :type SceneKey: str
        :param _UserInfo: 自动签开通个人用户信息，包括名字，身份证等。
        :type UserInfo: :class:`tencentcloud.essbasic.v20210526.models.UserThreeFactor`
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param _ExpiredTime: 链接的过期时间，格式为Unix时间戳，不能早于当前时间，且最大为当前时间往后30天。`如果不传，默认过期时间为当前时间往后7天。`
        :type ExpiredTime: int
        """
        self._Agent = None
        self._SceneKey = None
        self._UserInfo = None
        self._Operator = None
        self._ExpiredTime = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def SceneKey(self):
        return self._SceneKey

    @SceneKey.setter
    def SceneKey(self, SceneKey):
        self._SceneKey = SceneKey

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._SceneKey = params.get("SceneKey")
        if params.get("UserInfo") is not None:
            self._UserInfo = UserThreeFactor()
            self._UserInfo._deserialize(params.get("UserInfo"))
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._ExpiredTime = params.get("ExpiredTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateUserAutoSignSealUrlResponse(AbstractModel):
    """ChannelCreateUserAutoSignSealUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: 腾讯电子签小程序的AppId，用于其他小程序/APP等应用跳转至腾讯电子签小程序使用。
        :type AppId: str
        :param _AppOriginalId: 腾讯电子签小程序的原始Id，用于其他小程序/APP等应用跳转至腾讯电子签小程序使用。
        :type AppOriginalId: str
        :param _Url: 个人用户自动签的开通链接, 短链形式。过期时间受 `ExpiredTime` 参数控制。
        :type Url: str
        :param _Path: 腾讯电子签小程序的跳转路径，用于其他小程序/APP等应用跳转至腾讯电子签小程序使用。
        :type Path: str
        :param _QrCode: base64格式的跳转二维码图片，可通过微信扫描后跳转到腾讯电子签小程序的开通界面。
        :type QrCode: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppId = None
        self._AppOriginalId = None
        self._Url = None
        self._Path = None
        self._QrCode = None
        self._RequestId = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppOriginalId(self):
        return self._AppOriginalId

    @AppOriginalId.setter
    def AppOriginalId(self, AppOriginalId):
        self._AppOriginalId = AppOriginalId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def QrCode(self):
        return self._QrCode

    @QrCode.setter
    def QrCode(self, QrCode):
        self._QrCode = QrCode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._AppOriginalId = params.get("AppOriginalId")
        self._Url = params.get("Url")
        self._Path = params.get("Path")
        self._QrCode = params.get("QrCode")
        self._RequestId = params.get("RequestId")


class ChannelCreateUserRolesRequest(AbstractModel):
    """ChannelCreateUserRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _RoleIds: 绑定角色的角色id列表，最多 100 个
        :type RoleIds: list of str
        :param _UserIds: 电子签用户ID列表，与OpenIds参数二选一,优先UserIds参数，最多 100 个
        :type UserIds: list of str
        :param _OpenIds: 客户系统用户ID列表，与UserIds参数二选一,优先UserIds参数，最多 100 个
        :type OpenIds: list of str
        :param _Operator: 操作者信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._RoleIds = None
        self._UserIds = None
        self._OpenIds = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def RoleIds(self):
        return self._RoleIds

    @RoleIds.setter
    def RoleIds(self, RoleIds):
        self._RoleIds = RoleIds

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def OpenIds(self):
        return self._OpenIds

    @OpenIds.setter
    def OpenIds(self, OpenIds):
        self._OpenIds = OpenIds

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._RoleIds = params.get("RoleIds")
        self._UserIds = params.get("UserIds")
        self._OpenIds = params.get("OpenIds")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateUserRolesResponse(AbstractModel):
    """ChannelCreateUserRoles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailedCreateRoleData: 绑定失败的用户角色列表
        :type FailedCreateRoleData: list of FailedCreateRoleData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailedCreateRoleData = None
        self._RequestId = None

    @property
    def FailedCreateRoleData(self):
        return self._FailedCreateRoleData

    @FailedCreateRoleData.setter
    def FailedCreateRoleData(self, FailedCreateRoleData):
        self._FailedCreateRoleData = FailedCreateRoleData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FailedCreateRoleData") is not None:
            self._FailedCreateRoleData = []
            for item in params.get("FailedCreateRoleData"):
                obj = FailedCreateRoleData()
                obj._deserialize(item)
                self._FailedCreateRoleData.append(obj)
        self._RequestId = params.get("RequestId")


class ChannelCreateWebThemeConfigRequest(AbstractModel):
    """ChannelCreateWebThemeConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _ThemeType: 主题类型<br/>EMBED_WEB_THEME：嵌入式主题
<br/>目前只支持EMBED_WEB_THEME，web页面嵌入的主题风格配置
        :type ThemeType: str
        :param _WebThemeConfig: 主题配置
        :type WebThemeConfig: :class:`tencentcloud.essbasic.v20210526.models.WebThemeConfig`
        """
        self._Agent = None
        self._ThemeType = None
        self._WebThemeConfig = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def ThemeType(self):
        return self._ThemeType

    @ThemeType.setter
    def ThemeType(self, ThemeType):
        self._ThemeType = ThemeType

    @property
    def WebThemeConfig(self):
        return self._WebThemeConfig

    @WebThemeConfig.setter
    def WebThemeConfig(self, WebThemeConfig):
        self._WebThemeConfig = WebThemeConfig


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._ThemeType = params.get("ThemeType")
        if params.get("WebThemeConfig") is not None:
            self._WebThemeConfig = WebThemeConfig()
            self._WebThemeConfig._deserialize(params.get("WebThemeConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCreateWebThemeConfigResponse(AbstractModel):
    """ChannelCreateWebThemeConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ChannelDeleteRoleRequest(AbstractModel):
    """ChannelDeleteRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 代理企业和员工的信息。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _RoleIds: 角色id，最多20个
        :type RoleIds: list of str
        """
        self._Agent = None
        self._RoleIds = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def RoleIds(self):
        return self._RoleIds

    @RoleIds.setter
    def RoleIds(self, RoleIds):
        self._RoleIds = RoleIds


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._RoleIds = params.get("RoleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelDeleteRoleResponse(AbstractModel):
    """ChannelDeleteRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ChannelDeleteRoleUsersRequest(AbstractModel):
    """ChannelDeleteRoleUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 代理信息此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _RoleId: 角色Id（非超管或法人角色Id）
        :type RoleId: str
        :param _UserIds: 电子签用户ID列表，与OpenIds参数二选一,优先UserIds参数，最多两百
        :type UserIds: list of str
        :param _Operator: 操作人信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param _OpenIds: 客户系统用户ID列表，与UserIds参数二选一,优先UserIds参数，最多两百
        :type OpenIds: list of str
        """
        self._Agent = None
        self._RoleId = None
        self._UserIds = None
        self._Operator = None
        self._OpenIds = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator

    @property
    def OpenIds(self):
        return self._OpenIds

    @OpenIds.setter
    def OpenIds(self, OpenIds):
        self._OpenIds = OpenIds


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._RoleId = params.get("RoleId")
        self._UserIds = params.get("UserIds")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._OpenIds = params.get("OpenIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelDeleteRoleUsersResponse(AbstractModel):
    """ChannelDeleteRoleUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色id
        :type RoleId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleId = None
        self._RequestId = None

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._RequestId = params.get("RequestId")


class ChannelDeleteSealPoliciesRequest(AbstractModel):
    """ChannelDeleteSealPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _SealId: 指定印章ID
        :type SealId: str
        :param _UserIds: 指定用户ID数组，电子签系统用户ID
可以填写OpenId，系统会通过组织+渠道+OpenId查询得到UserId进行授权取消。
        :type UserIds: list of str
        :param _Organization: 组织机构信息，不用传
        :type Organization: :class:`tencentcloud.essbasic.v20210526.models.OrganizationInfo`
        :param _Operator: 操作人（用户）信息，不用传
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._SealId = None
        self._UserIds = None
        self._Organization = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def SealId(self):
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def Organization(self):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        self._Organization = Organization

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._SealId = params.get("SealId")
        self._UserIds = params.get("UserIds")
        if params.get("Organization") is not None:
            self._Organization = OrganizationInfo()
            self._Organization._deserialize(params.get("Organization"))
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelDeleteSealPoliciesResponse(AbstractModel):
    """ChannelDeleteSealPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ChannelDescribeEmployeesRequest(AbstractModel):
    """ChannelDescribeEmployees请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _Limit: 指定每页多少条数据，单页最大20
        :type Limit: int
        :param _Filters: 查询过滤实名用户，Key为Status，Values为["IsVerified"]
根据第三方系统openId过滤查询员工时,Key为StaffOpenId,Values为["OpenId","OpenId",...]
查询离职员工时，Key为Status，Values为["QuiteJob"]
        :type Filters: list of Filter
        :param _Offset: 查询结果分页返回，此处指定第几页，如果不传默认从第一页返回。页码从 0 开始，即首页为 0,最大为20000
        :type Offset: int
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._Limit = None
        self._Filters = None
        self._Offset = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelDescribeEmployeesResponse(AbstractModel):
    """ChannelDescribeEmployees返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Employees: 员工数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Employees: list of Staff
        :param _Offset: 查询结果分页返回，此处指定第几页，如果不传默认从第一页返回。页码从 0 开始，即首页为 0，最大20000
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: int
        :param _Limit: 指定每页多少条数据，单页最大20
        :type Limit: int
        :param _TotalCount: 符合条件的员工数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Employees = None
        self._Offset = None
        self._Limit = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Employees(self):
        return self._Employees

    @Employees.setter
    def Employees(self, Employees):
        self._Employees = Employees

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Employees") is not None:
            self._Employees = []
            for item in params.get("Employees"):
                obj = Staff()
                obj._deserialize(item)
                self._Employees.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ChannelDescribeFlowComponentsRequest(AbstractModel):
    """ChannelDescribeFlowComponents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowId: 电子签流程的Id
        :type FlowId: str
        """
        self._Agent = None
        self._FlowId = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelDescribeFlowComponentsResponse(AbstractModel):
    """ChannelDescribeFlowComponents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecipientComponentInfos: 流程关联的填写控件信息，控件会按照参与方进行分类。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecipientComponentInfos: list of RecipientComponentInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecipientComponentInfos = None
        self._RequestId = None

    @property
    def RecipientComponentInfos(self):
        return self._RecipientComponentInfos

    @RecipientComponentInfos.setter
    def RecipientComponentInfos(self, RecipientComponentInfos):
        self._RecipientComponentInfos = RecipientComponentInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RecipientComponentInfos") is not None:
            self._RecipientComponentInfos = []
            for item in params.get("RecipientComponentInfos"):
                obj = RecipientComponentInfo()
                obj._deserialize(item)
                self._RecipientComponentInfos.append(obj)
        self._RequestId = params.get("RequestId")


class ChannelDescribeOrganizationSealsRequest(AbstractModel):
    """ChannelDescribeOrganizationSeals请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _Limit: 返回最大数量，最大为100
        :type Limit: int
        :param _Offset: 偏移量，默认为0，最大为20000
        :type Offset: int
        :param _InfoType: 查询信息类型，为1时返回授权用户，为其他值时不返回
        :type InfoType: int
        :param _SealId: 印章id（没有输入返回所有）
        :type SealId: str
        :param _SealTypes: 印章类型列表（都是组织机构印章）。
为空时查询所有类型的印章。
目前支持以下类型：
OFFICIAL：企业公章；
CONTRACT：合同专用章；
ORGANIZATION_SEAL：企业印章(图片上传创建)；
LEGAL_PERSON_SEAL：法定代表人章
        :type SealTypes: list of str
        """
        self._Agent = None
        self._Limit = None
        self._Offset = None
        self._InfoType = None
        self._SealId = None
        self._SealTypes = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def InfoType(self):
        return self._InfoType

    @InfoType.setter
    def InfoType(self, InfoType):
        self._InfoType = InfoType

    @property
    def SealId(self):
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def SealTypes(self):
        return self._SealTypes

    @SealTypes.setter
    def SealTypes(self, SealTypes):
        self._SealTypes = SealTypes


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._InfoType = params.get("InfoType")
        self._SealId = params.get("SealId")
        self._SealTypes = params.get("SealTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelDescribeOrganizationSealsResponse(AbstractModel):
    """ChannelDescribeOrganizationSeals返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 在设置了SealId时返回0或1，没有设置时返回公司的总印章数量，可能比返回的印章数组数量多
        :type TotalCount: int
        :param _Seals: 查询到的印章结果数组
        :type Seals: list of OccupiedSeal
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Seals = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Seals(self):
        return self._Seals

    @Seals.setter
    def Seals(self, Seals):
        self._Seals = Seals

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Seals") is not None:
            self._Seals = []
            for item in params.get("Seals"):
                obj = OccupiedSeal()
                obj._deserialize(item)
                self._Seals.append(obj)
        self._RequestId = params.get("RequestId")


class ChannelDescribeRolesRequest(AbstractModel):
    """ChannelDescribeRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _Limit: 指定每页多少条数据，单页最大200
        :type Limit: str
        :param _Filters: 查询的关键字段:
Key:"RoleType",Values:["1"]查询系统角色，Values:["2"]查询自定义角色
Key:"RoleStatus",Values:["1"]查询启用角色，Values:["2"]查询禁用角色
Key:"IsReturnPermissionGroup"，Values:["0"]:表示接口不返回角色对应的权限树字段，Values:["1"]表示接口返回角色对应的权限树字段
        :type Filters: list of Filter
        :param _Offset: 查询结果分页返回，此处指定第几页，如果不传默认从第一页返回。页码从 0 开始，即首页为 0，最大2000
        :type Offset: int
        :param _Operator: 操作人信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._Limit = None
        self._Filters = None
        self._Offset = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelDescribeRolesResponse(AbstractModel):
    """ChannelDescribeRoles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 查询结果分页返回，此处指定第几页，如果不传默认从第一页返回。页码从 0 开始，即首页为 0，最大2000
        :type Offset: int
        :param _Limit: 指定每页多少条数据，单页最大200
        :type Limit: int
        :param _TotalCount: 查询角色的总数量
        :type TotalCount: int
        :param _ChannelRoles: 角色信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelRoles: list of ChannelRole
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Offset = None
        self._Limit = None
        self._TotalCount = None
        self._ChannelRoles = None
        self._RequestId = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ChannelRoles(self):
        return self._ChannelRoles

    @ChannelRoles.setter
    def ChannelRoles(self, ChannelRoles):
        self._ChannelRoles = ChannelRoles

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TotalCount = params.get("TotalCount")
        if params.get("ChannelRoles") is not None:
            self._ChannelRoles = []
            for item in params.get("ChannelRoles"):
                obj = ChannelRole()
                obj._deserialize(item)
                self._ChannelRoles.append(obj)
        self._RequestId = params.get("RequestId")


class ChannelDescribeUserAutoSignStatusRequest(AbstractModel):
    """ChannelDescribeUserAutoSignStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 渠道应用相关信息
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _SceneKey: 自动签场景:
E_PRESCRIPTION_AUTO_SIGN 电子处方
        :type SceneKey: str
        :param _UserInfo: 查询开启状态的用户信息
        :type UserInfo: :class:`tencentcloud.essbasic.v20210526.models.UserThreeFactor`
        :param _Operator: 操作人信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._SceneKey = None
        self._UserInfo = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def SceneKey(self):
        return self._SceneKey

    @SceneKey.setter
    def SceneKey(self, SceneKey):
        self._SceneKey = SceneKey

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._SceneKey = params.get("SceneKey")
        if params.get("UserInfo") is not None:
            self._UserInfo = UserThreeFactor()
            self._UserInfo._deserialize(params.get("UserInfo"))
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelDescribeUserAutoSignStatusResponse(AbstractModel):
    """ChannelDescribeUserAutoSignStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsOpen: 是否开通
        :type IsOpen: bool
        :param _LicenseFrom: 自动签许可生效时间。当且仅当已开通自动签时有值。
        :type LicenseFrom: int
        :param _LicenseTo: 自动签许可到期时间。当且仅当已开通自动签时有值。
        :type LicenseTo: int
        :param _LicenseType: 设置用户开通自动签时是否绑定个人自动签账号许可。一旦绑定后，将扣减购买的个人自动签账号许可一次（1年有效期），不可解绑释放。不传默认为绑定自动签账号许可。 0-绑定个人自动签账号许可，开通后将扣减购买的个人自动签账号许可一次
        :type LicenseType: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsOpen = None
        self._LicenseFrom = None
        self._LicenseTo = None
        self._LicenseType = None
        self._RequestId = None

    @property
    def IsOpen(self):
        return self._IsOpen

    @IsOpen.setter
    def IsOpen(self, IsOpen):
        self._IsOpen = IsOpen

    @property
    def LicenseFrom(self):
        return self._LicenseFrom

    @LicenseFrom.setter
    def LicenseFrom(self, LicenseFrom):
        self._LicenseFrom = LicenseFrom

    @property
    def LicenseTo(self):
        return self._LicenseTo

    @LicenseTo.setter
    def LicenseTo(self, LicenseTo):
        self._LicenseTo = LicenseTo

    @property
    def LicenseType(self):
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsOpen = params.get("IsOpen")
        self._LicenseFrom = params.get("LicenseFrom")
        self._LicenseTo = params.get("LicenseTo")
        self._LicenseType = params.get("LicenseType")
        self._RequestId = params.get("RequestId")


class ChannelDisableUserAutoSignRequest(AbstractModel):
    """ChannelDisableUserAutoSign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 渠道应用相关信息
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _SceneKey: 自动签场景:
E_PRESCRIPTION_AUTO_SIGN 电子处方
        :type SceneKey: str
        :param _UserInfo: 关闭自动签的个人的三要素
        :type UserInfo: :class:`tencentcloud.essbasic.v20210526.models.UserThreeFactor`
        :param _Operator: 操作人信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._SceneKey = None
        self._UserInfo = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def SceneKey(self):
        return self._SceneKey

    @SceneKey.setter
    def SceneKey(self, SceneKey):
        self._SceneKey = SceneKey

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._SceneKey = params.get("SceneKey")
        if params.get("UserInfo") is not None:
            self._UserInfo = UserThreeFactor()
            self._UserInfo._deserialize(params.get("UserInfo"))
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelDisableUserAutoSignResponse(AbstractModel):
    """ChannelDisableUserAutoSign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ChannelGetTaskResultApiRequest(AbstractModel):
    """ChannelGetTaskResultApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _TaskId: 任务Id，通过ChannelCreateConvertTaskApi接口获得
        :type TaskId: str
        :param _Operator: 操作者的信息，不用传
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param _Organization: 暂未开放
        :type Organization: :class:`tencentcloud.essbasic.v20210526.models.OrganizationInfo`
        """
        self._Agent = None
        self._TaskId = None
        self._Operator = None
        self._Organization = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator

    @property
    def Organization(self):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        self._Organization = Organization


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._TaskId = params.get("TaskId")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("Organization") is not None:
            self._Organization = OrganizationInfo()
            self._Organization._deserialize(params.get("Organization"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelGetTaskResultApiResponse(AbstractModel):
    """ChannelGetTaskResultApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
        :type TaskId: str
        :param _TaskStatus: 任务状态，需要关注的状态
0  :NeedTranform   - 任务已提交
4  :Processing     - 文档转换中
8  :TaskEnd        - 任务处理完成
-2 :DownloadFailed - 下载失败
-6 :ProcessFailed  - 转换失败
-13:ProcessTimeout - 转换文件超时
        :type TaskStatus: int
        :param _TaskMessage: 状态描述，需要关注的状态
NeedTranform   - 任务已提交
Processing     - 文档转换中
TaskEnd        - 任务处理完成
DownloadFailed - 下载失败
ProcessFailed  - 转换失败
ProcessTimeout - 转换文件超时
        :type TaskMessage: str
        :param _ResourceId: 资源Id，也是FileId，用于文件发起使用
        :type ResourceId: str
        :param _PreviewUrl: 预览文件Url，有效期30分钟 
当前字段返回为空，发起的时候，将ResourceId 放入发起即可
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._TaskStatus = None
        self._TaskMessage = None
        self._ResourceId = None
        self._PreviewUrl = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskMessage(self):
        return self._TaskMessage

    @TaskMessage.setter
    def TaskMessage(self, TaskMessage):
        self._TaskMessage = TaskMessage

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def PreviewUrl(self):
        warnings.warn("parameter `PreviewUrl` is deprecated", DeprecationWarning) 

        return self._PreviewUrl

    @PreviewUrl.setter
    def PreviewUrl(self, PreviewUrl):
        warnings.warn("parameter `PreviewUrl` is deprecated", DeprecationWarning) 

        self._PreviewUrl = PreviewUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskMessage = params.get("TaskMessage")
        self._ResourceId = params.get("ResourceId")
        self._PreviewUrl = params.get("PreviewUrl")
        self._RequestId = params.get("RequestId")


class ChannelModifyRoleRequest(AbstractModel):
    """ChannelModifyRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 代理企业和员工的信息。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _Name: 角色名称，最大长度为20个字符，仅限中文、字母、数字和下划线组成。
        :type Name: str
        :param _RoleId: 角色Id，可通过接口 ChannelDescribeRoles 查询获取
        :type RoleId: str
        :param _Description: 角色描述，最大长度为50个字符
        :type Description: str
        :param _PermissionGroups: 权限树，权限树内容 PermissionGroups 可参考接口 DescribeIntegrationRoles 的输出
        :type PermissionGroups: list of PermissionGroup
        """
        self._Agent = None
        self._Name = None
        self._RoleId = None
        self._Description = None
        self._PermissionGroups = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PermissionGroups(self):
        return self._PermissionGroups

    @PermissionGroups.setter
    def PermissionGroups(self, PermissionGroups):
        self._PermissionGroups = PermissionGroups


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._Name = params.get("Name")
        self._RoleId = params.get("RoleId")
        self._Description = params.get("Description")
        if params.get("PermissionGroups") is not None:
            self._PermissionGroups = []
            for item in params.get("PermissionGroups"):
                obj = PermissionGroup()
                obj._deserialize(item)
                self._PermissionGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelModifyRoleResponse(AbstractModel):
    """ChannelModifyRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色id
        :type RoleId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleId = None
        self._RequestId = None

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._RequestId = params.get("RequestId")


class ChannelRole(AbstractModel):
    """渠道角色信息

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色id
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleId: str
        :param _RoleName: 角色名
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleName: str
        :param _RoleStatus: 角色状态：1-启用；2-禁用
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleStatus: int
        :param _PermissionGroups: 权限树
注意：此字段可能返回 null，表示取不到有效值。
        :type PermissionGroups: list of PermissionGroup
        """
        self._RoleId = None
        self._RoleName = None
        self._RoleStatus = None
        self._PermissionGroups = None

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def RoleStatus(self):
        return self._RoleStatus

    @RoleStatus.setter
    def RoleStatus(self, RoleStatus):
        self._RoleStatus = RoleStatus

    @property
    def PermissionGroups(self):
        return self._PermissionGroups

    @PermissionGroups.setter
    def PermissionGroups(self, PermissionGroups):
        self._PermissionGroups = PermissionGroups


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        self._RoleStatus = params.get("RoleStatus")
        if params.get("PermissionGroups") is not None:
            self._PermissionGroups = []
            for item in params.get("PermissionGroups"):
                obj = PermissionGroup()
                obj._deserialize(item)
                self._PermissionGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelUpdateSealStatusRequest(AbstractModel):
    """ChannelUpdateSealStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _Status: 操作的印章状态，DISABLE-停用印章
        :type Status: str
        :param _SealId: 印章ID
        :type SealId: str
        :param _Reason: 更新印章状态原因说明
        :type Reason: str
        :param _Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._Status = None
        self._SealId = None
        self._Reason = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SealId(self):
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._Status = params.get("Status")
        self._SealId = params.get("SealId")
        self._Reason = params.get("Reason")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelUpdateSealStatusResponse(AbstractModel):
    """ChannelUpdateSealStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ChannelVerifyPdfRequest(AbstractModel):
    """ChannelVerifyPdf请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: str
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._FlowId = None
        self._Agent = None
        self._Operator = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelVerifyPdfResponse(AbstractModel):
    """ChannelVerifyPdf返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VerifyResult: 验签结果，1-文件未被篡改，全部签名在腾讯电子签完成； 2-文件未被篡改，部分签名在腾讯电子签完成；3-文件被篡改；4-异常：文件内没有签名域；5-异常：文件签名格式错误
        :type VerifyResult: int
        :param _PdfVerifyResults: 验签结果详情,内部状态1-验签成功，在电子签签署；2-验签成功，在其他平台签署；3-验签失败；4-pdf文件没有签名域；5-文件签名格式错误
        :type PdfVerifyResults: list of PdfVerifyResult
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VerifyResult = None
        self._PdfVerifyResults = None
        self._RequestId = None

    @property
    def VerifyResult(self):
        return self._VerifyResult

    @VerifyResult.setter
    def VerifyResult(self, VerifyResult):
        self._VerifyResult = VerifyResult

    @property
    def PdfVerifyResults(self):
        return self._PdfVerifyResults

    @PdfVerifyResults.setter
    def PdfVerifyResults(self, PdfVerifyResults):
        self._PdfVerifyResults = PdfVerifyResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VerifyResult = params.get("VerifyResult")
        if params.get("PdfVerifyResults") is not None:
            self._PdfVerifyResults = []
            for item in params.get("PdfVerifyResults"):
                obj = PdfVerifyResult()
                obj._deserialize(item)
                self._PdfVerifyResults.append(obj)
        self._RequestId = params.get("RequestId")


class CommonApproverOption(AbstractModel):
    """签署人配置信息

    """

    def __init__(self):
        r"""
        :param _CanEditApprover: 是否允许修改签署人信息
        :type CanEditApprover: bool
        """
        self._CanEditApprover = None

    @property
    def CanEditApprover(self):
        return self._CanEditApprover

    @CanEditApprover.setter
    def CanEditApprover(self, CanEditApprover):
        self._CanEditApprover = CanEditApprover


    def _deserialize(self, params):
        self._CanEditApprover = params.get("CanEditApprover")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonFlowApprover(AbstractModel):
    """通用签署人信息

    """

    def __init__(self):
        r"""
        :param _NotChannelOrganization: 指定当前签署人为第三方应用集成子客，默认false：当前签署人为第三方应用集成子客，true：当前签署人为saas企业用户
        :type NotChannelOrganization: bool
        :param _ApproverType: 签署人类型,目前支持：0-企业签署人，1-个人签署人，3-企业静默签署人
        :type ApproverType: int
        :param _OrganizationId: 企业id
        :type OrganizationId: str
        :param _OrganizationOpenId: 企业OpenId，第三方应用集成非静默签子客企业签署人发起合同必传
        :type OrganizationOpenId: str
        :param _OrganizationName: 企业名称，第三方应用集成非静默签子客企业签署人必传，saas企业签署人必传
        :type OrganizationName: str
        :param _UserId: 用户id
        :type UserId: str
        :param _OpenId: 用户openId，第三方应用集成非静默签子客企业签署人必传
        :type OpenId: str
        :param _ApproverName: 签署人名称，saas企业签署人，个人签署人必传
        :type ApproverName: str
        :param _ApproverMobile: 签署人手机号，saas企业签署人，个人签署人必传
        :type ApproverMobile: str
        :param _RecipientId: 签署人Id，使用模板发起是，对应模板配置中的签署人RecipientId
注意：模板发起时该字段必填
        :type RecipientId: str
        :param _PreReadTime: 签署前置条件：阅读时长限制，不传默认10s,最大300s，最小3s
        :type PreReadTime: int
        :param _IsFullText: 签署前置条件：阅读全文限制
        :type IsFullText: bool
        :param _NotifyType: 通知类型：SMS（短信） NONE（不做通知）, 不传 默认SMS
        :type NotifyType: str
        :param _ApproverOption: 签署人配置
        :type ApproverOption: :class:`tencentcloud.essbasic.v20210526.models.CommonApproverOption`
        :param _SignComponents: 签署控件：文件发起使用
        :type SignComponents: list of Component
        :param _ApproverVerifyTypes: 签署人查看合同时认证方式, 1-实名查看 2-短信验证码查看(企业签署方不支持该方式) 如果不传默认为1 查看合同的认证方式 Flow层级的优先于approver层级的 （当手写签名方式为OCR_ESIGN时，合同认证方式2无效，因为这种签名方式依赖实名认证）
        :type ApproverVerifyTypes: list of int
        :param _ApproverSignTypes: 签署人签署合同时的认证方式 1-人脸认证 2-签署密码 3-运营商三要素(默认为1,2)	
        :type ApproverSignTypes: list of int
        """
        self._NotChannelOrganization = None
        self._ApproverType = None
        self._OrganizationId = None
        self._OrganizationOpenId = None
        self._OrganizationName = None
        self._UserId = None
        self._OpenId = None
        self._ApproverName = None
        self._ApproverMobile = None
        self._RecipientId = None
        self._PreReadTime = None
        self._IsFullText = None
        self._NotifyType = None
        self._ApproverOption = None
        self._SignComponents = None
        self._ApproverVerifyTypes = None
        self._ApproverSignTypes = None

    @property
    def NotChannelOrganization(self):
        return self._NotChannelOrganization

    @NotChannelOrganization.setter
    def NotChannelOrganization(self, NotChannelOrganization):
        self._NotChannelOrganization = NotChannelOrganization

    @property
    def ApproverType(self):
        return self._ApproverType

    @ApproverType.setter
    def ApproverType(self, ApproverType):
        self._ApproverType = ApproverType

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def OrganizationOpenId(self):
        return self._OrganizationOpenId

    @OrganizationOpenId.setter
    def OrganizationOpenId(self, OrganizationOpenId):
        self._OrganizationOpenId = OrganizationOpenId

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def ApproverName(self):
        return self._ApproverName

    @ApproverName.setter
    def ApproverName(self, ApproverName):
        self._ApproverName = ApproverName

    @property
    def ApproverMobile(self):
        return self._ApproverMobile

    @ApproverMobile.setter
    def ApproverMobile(self, ApproverMobile):
        self._ApproverMobile = ApproverMobile

    @property
    def RecipientId(self):
        return self._RecipientId

    @RecipientId.setter
    def RecipientId(self, RecipientId):
        self._RecipientId = RecipientId

    @property
    def PreReadTime(self):
        return self._PreReadTime

    @PreReadTime.setter
    def PreReadTime(self, PreReadTime):
        self._PreReadTime = PreReadTime

    @property
    def IsFullText(self):
        return self._IsFullText

    @IsFullText.setter
    def IsFullText(self, IsFullText):
        self._IsFullText = IsFullText

    @property
    def NotifyType(self):
        return self._NotifyType

    @NotifyType.setter
    def NotifyType(self, NotifyType):
        self._NotifyType = NotifyType

    @property
    def ApproverOption(self):
        return self._ApproverOption

    @ApproverOption.setter
    def ApproverOption(self, ApproverOption):
        self._ApproverOption = ApproverOption

    @property
    def SignComponents(self):
        return self._SignComponents

    @SignComponents.setter
    def SignComponents(self, SignComponents):
        self._SignComponents = SignComponents

    @property
    def ApproverVerifyTypes(self):
        return self._ApproverVerifyTypes

    @ApproverVerifyTypes.setter
    def ApproverVerifyTypes(self, ApproverVerifyTypes):
        self._ApproverVerifyTypes = ApproverVerifyTypes

    @property
    def ApproverSignTypes(self):
        return self._ApproverSignTypes

    @ApproverSignTypes.setter
    def ApproverSignTypes(self, ApproverSignTypes):
        self._ApproverSignTypes = ApproverSignTypes


    def _deserialize(self, params):
        self._NotChannelOrganization = params.get("NotChannelOrganization")
        self._ApproverType = params.get("ApproverType")
        self._OrganizationId = params.get("OrganizationId")
        self._OrganizationOpenId = params.get("OrganizationOpenId")
        self._OrganizationName = params.get("OrganizationName")
        self._UserId = params.get("UserId")
        self._OpenId = params.get("OpenId")
        self._ApproverName = params.get("ApproverName")
        self._ApproverMobile = params.get("ApproverMobile")
        self._RecipientId = params.get("RecipientId")
        self._PreReadTime = params.get("PreReadTime")
        self._IsFullText = params.get("IsFullText")
        self._NotifyType = params.get("NotifyType")
        if params.get("ApproverOption") is not None:
            self._ApproverOption = CommonApproverOption()
            self._ApproverOption._deserialize(params.get("ApproverOption"))
        if params.get("SignComponents") is not None:
            self._SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self._SignComponents.append(obj)
        self._ApproverVerifyTypes = params.get("ApproverVerifyTypes")
        self._ApproverSignTypes = params.get("ApproverSignTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param _ComponentId: 控件编号

CreateFlowByTemplates发起合同时优先以ComponentId（不为空）填充；否则以ComponentName填充

注：
当GenerateMode=KEYWORD时，通过"^"来决定是否使用关键字整词匹配能力。
例：当GenerateMode=KEYWORD时，如果传入关键字"^甲方签署^"，则会在PDF文件中有且仅有"甲方签署"关键字的地方进行对应操作。
如传入的关键字为"甲方签署"，则PDF文件中每个出现关键字的位置都会执行相应操作。

创建控件时，此值为空
查询时返回完整结构
        :type ComponentId: str
        :param _ComponentType: 如果是Component控件类型，则可选的字段为：
TEXT - 普通文本控件，输入文本字符串；
MULTI_LINE_TEXT - 多行文本控件，输入文本字符串；
CHECK_BOX - 勾选框控件，若选中填写ComponentValue 填写 true或者 false 字符串；
FILL_IMAGE - 图片控件，ComponentValue 填写图片的资源 ID；
DYNAMIC_TABLE - 动态表格控件；
ATTACHMENT - 附件控件,ComponentValue 填写附件图片的资源 ID列表，以逗号分割；
SELECTOR - 选择器控件，ComponentValue填写选择的字符串内容；
DATE - 日期控件；默认是格式化为xxxx年xx月xx日字符串；
DISTRICT - 省市区行政区控件，ComponentValue填写省市区行政区字符串内容；

如果是SignComponent控件类型，则可选的字段为
SIGN_SEAL - 签署印章控件；
SIGN_DATE - 签署日期控件；
SIGN_SIGNATURE - 用户签名控件；
SIGN_PERSONAL_SEAL - 个人签署印章控件（使用文件发起暂不支持此类型）；
SIGN_PAGING_SEAL - 骑缝章；若文件发起，需要对应填充ComponentPosY、ComponentWidth、ComponentHeight
SIGN_OPINION - 签署意见控件，用户需要根据配置的签署意见内容，完成对意见内容的确认;
SIGN_LEGAL_PERSON_SEAL - 企业法定代表人控件。

表单域的控件不能作为印章和签名控件
        :type ComponentType: str
        :param _ComponentName: 控件简称，不超过30个字符
        :type ComponentName: str
        :param _ComponentRequired: 控件是否为必填项，
默认为false-非必填
        :type ComponentRequired: bool
        :param _ComponentRecipientId: 控件关联的参与方ID，对应Recipient结构体中的RecipientId	
        :type ComponentRecipientId: str
        :param _FileIndex: 控件所属文件的序号 (文档中文件的排列序号，从0开始)
        :type FileIndex: int
        :param _GenerateMode: 控件生成的方式：
NORMAL - 普通控件
FIELD - 表单域
KEYWORD - 关键字
        :type GenerateMode: str
        :param _ComponentWidth: 参数控件宽度，默认100，单位px
表单域和关键字转换控件不用填
        :type ComponentWidth: float
        :param _ComponentHeight: 参数控件高度，默认100，单位px
表单域和关键字转换控件不用填
        :type ComponentHeight: float
        :param _ComponentPage: 参数控件所在页码，从1开始
        :type ComponentPage: int
        :param _ComponentPosX: 参数控件X位置，单位px
        :type ComponentPosX: float
        :param _ComponentPosY: 参数控件Y位置，单位px
        :type ComponentPosY: float
        :param _ComponentExtra: 扩展参数：
为JSON格式。
不同类型的控件会有部分非通用参数

ComponentType为TEXT、MULTI_LINE_TEXT时，支持以下参数：
1 Font：目前只支持黑体、宋体
2 FontSize： 范围12-72
3 FontAlign： Left/Right/Center，左对齐/居中/右对齐
4 FontColor：字符串类型，格式为RGB颜色数字
参数样例：{\"FontColor\":\"255,0,0\",\"FontSize\":12}

ComponentType为FILL_IMAGE时，支持以下参数：
NotMakeImageCenter：bool。是否设置图片居中。false：居中（默认）。 true: 不居中
FillMethod: int. 填充方式。0-铺满（默认）；1-等比例缩放

ComponentType为SIGN_SIGNATURE类型可以控制签署方式
{“ComponentTypeLimit”: [“xxx”]}
xxx可以为：
HANDWRITE – 手写签名
OCR_ESIGN -- AI智能识别手写签名
ESIGN -- 个人印章类型
SYSTEM_ESIGN -- 系统签名（该类型可以在用户签署时根据用户姓名一键生成一个签名来进行签署）
如：{“ComponentTypeLimit”: [“SYSTEM_ESIGN”]}

ComponentType为SIGN_DATE时，支持以下参数：
1 Font：字符串类型目前只支持"黑体"、"宋体"，如果不填默认为"黑体"
2 FontSize： 数字类型，范围6-72，默认值为12
3 FontAlign： 字符串类型，可取Left/Right/Center，对应左对齐/居中/右对齐
4 Format： 字符串类型，日期格式，必须是以下五种之一 “yyyy m d”，”yyyy年m月d日”，”yyyy/m/d”，”yyyy-m-d”，”yyyy.m.d”。
5 Gaps:： 字符串类型，仅在Format为“yyyy m d”时起作用，格式为用逗号分开的两个整数，例如”2,2”，两个数字分别是日期格式的前后两个空隙中的空格个数
如果extra参数为空，默认为”yyyy年m月d日”格式的居中日期
特别地，如果extra中Format字段为空或无法被识别，则extra参数会被当作默认值处理（Font，FontSize，Gaps和FontAlign都不会起效）
参数样例： "ComponentExtra": "{"Format":“yyyy m d”,"FontSize":12,"Gaps":"2,2", "FontAlign":"Right"}"

ComponentType为SIGN_SEAL类型时，支持以下参数：
1.PageRanges：PageRange的数组，通过PageRanges属性设置该印章在PDF所有页面上盖章（适用于标书在所有页面盖章的情况）
参数样例： "ComponentExtra":"{"PageRange":[{"BeginPage":1,"EndPage":-1}]}"
        :type ComponentExtra: str
        :param _ComponentValue: 控件填充vaule，ComponentType和传入值类型对应关系：
TEXT - 文本内容
MULTI_LINE_TEXT - 文本内容
CHECK_BOX - true/false
FILL_IMAGE、ATTACHMENT - 附件的FileId，需要通过UploadFiles接口上传获取
SELECTOR - 选项值
DATE - 默认是格式化为xxxx年xx月xx日
DYNAMIC_TABLE - 传入json格式的表格内容，具体见数据结构FlowInfo：https://cloud.tencent.com/document/api/1420/61525#FlowInfo
SIGN_SEAL - 印章ID
SIGN_PAGING_SEAL - 可以指定印章ID

控件值约束说明：
企业全称控件：
  约束：企业名称中文字符中文括号
  检查正则表达式：/^[\u3400-\u4dbf\u4e00-\u9fa5（）]+$/

统一社会信用代码控件：
  检查正则表达式：/^[A-Z0-9]{1,18}$/

法人名称控件：
  约束：最大50个字符，2到25个汉字或者1到50个字母
  检查正则表达式：/^([\u3400-\u4dbf\u4e00-\u9fa5.·]{2,25}|[a-zA-Z·,\s-]{1,50})$/

签署意见控件：
  约束：签署意见最大长度为50字符

签署人手机号控件：
  约束：国内手机号 13,14,15,16,17,18,19号段长度11位

签署人身份证控件：
  约束：合法的身份证号码检查

控件名称：
  约束：控件名称最大长度为20字符

单行文本控件：
  约束：只允许输入中文，英文，数字，中英文标点符号

多行文本控件：
  约束：只允许输入中文，英文，数字，中英文标点符号

勾选框控件：
  约束：选择填字符串true，不选填字符串false

选择器控件：
  约束：同单行文本控件约束，填写选择值中的字符串

数字控件：
  约束：请输入有效的数字(可带小数点) 
  检查正则表达式：/^(-|\+)?\d+(\.\d+)?$/

日期控件：
  约束：格式：yyyy年mm月dd日

附件控件：
  约束：JPG或PNG图片，上传数量限制，1到6个，最大6个附件

图片控件：
  约束：JPG或PNG图片，填写上传的图片资源ID

邮箱控件：
  约束：请输入有效的邮箱地址, w3c标准
  检查正则表达式：/^([A-Za-z0-9_\-.!#$%&])+@([A-Za-z0-9_\-.])+\.([A-Za-z]{2,4})$/
  参考：https://emailregex.com/

地址控件：
  同单行文本控件约束

省市区控件：
  同单行文本控件约束

性别控件：
  同单行文本控件约束，填写选择值中的字符串

学历控件：
  同单行文本控件约束，填写选择值中的字符串
        :type ComponentValue: str
        :param _ComponentDateFontSize: 日期签署控件的字号，默认为 12

签署区日期控件会转换成图片格式并带存证，需要通过字体决定图片大小
        :type ComponentDateFontSize: int
        :param _DocumentId: 控件所属文档的Id, 模板相关接口为空值
        :type DocumentId: str
        :param _ComponentDescription: 控件描述，不超过30个字符
        :type ComponentDescription: str
        :param _OffsetX: 指定关键字时横坐标偏移量，单位pt
        :type OffsetX: float
        :param _OffsetY: 指定关键字时纵坐标偏移量，单位pt
        :type OffsetY: float
        :param _ChannelComponentId: 平台企业控件ID。
如果不为空，属于平台企业预设控件；
        :type ChannelComponentId: str
        :param _KeywordOrder: 指定关键字排序规则，
Positive-正序，
Reverse-倒序。
传入Positive时会根据关键字在PDF文件内的顺序进行排列。在指定KeywordIndexes时，0代表在PDF内查找内容时，查找到的第一个关键字。
传入Reverse时会根据关键字在PDF文件内的反序进行排列。在指定KeywordIndexes时，0代表在PDF内查找内容时，查找到的最后一个关键字。
        :type KeywordOrder: str
        :param _KeywordPage: 指定关键字页码。
指定页码后，将只在指定的页码内查找关键字，非该页码的关键字将不会查询出来
        :type KeywordPage: int
        :param _RelativeLocation: 关键字位置模式，
Middle-居中，
Below-正下方，
Right-正右方，
LowerRight-右上角，
UpperRight-右下角。
示例：如果设置Middle的关键字盖章，则印章的中心会和关键字的中心重合，如果设置Below，则印章在关键字的正下方
        :type RelativeLocation: str
        :param _KeywordIndexes: 关键字索引，如果一个关键字在PDF文件中存在多个，可以通过关键字索引指定使用第几个关键字作为最后的结果，可指定多个索引。
示例[0,2]，说明使用PDF文件内第1个和第3个关键字位置。
        :type KeywordIndexes: list of int
        :param _Placeholder: 填写提示的内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Placeholder: str
        :param _LockComponentValue: 是否锁定控件值不允许编辑（嵌入式发起使用） <br/>默认false：不锁定控件值，允许在页面编辑控件值	
注意：此字段可能返回 null，表示取不到有效值。
        :type LockComponentValue: bool
        :param _ForbidMoveAndDelete: 是否禁止移动和删除控件 <br/>默认false，不禁止移动和删除控件	
注意：此字段可能返回 null，表示取不到有效值。
        :type ForbidMoveAndDelete: bool
        """
        self._ComponentId = None
        self._ComponentType = None
        self._ComponentName = None
        self._ComponentRequired = None
        self._ComponentRecipientId = None
        self._FileIndex = None
        self._GenerateMode = None
        self._ComponentWidth = None
        self._ComponentHeight = None
        self._ComponentPage = None
        self._ComponentPosX = None
        self._ComponentPosY = None
        self._ComponentExtra = None
        self._ComponentValue = None
        self._ComponentDateFontSize = None
        self._DocumentId = None
        self._ComponentDescription = None
        self._OffsetX = None
        self._OffsetY = None
        self._ChannelComponentId = None
        self._KeywordOrder = None
        self._KeywordPage = None
        self._RelativeLocation = None
        self._KeywordIndexes = None
        self._Placeholder = None
        self._LockComponentValue = None
        self._ForbidMoveAndDelete = None

    @property
    def ComponentId(self):
        return self._ComponentId

    @ComponentId.setter
    def ComponentId(self, ComponentId):
        self._ComponentId = ComponentId

    @property
    def ComponentType(self):
        return self._ComponentType

    @ComponentType.setter
    def ComponentType(self, ComponentType):
        self._ComponentType = ComponentType

    @property
    def ComponentName(self):
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def ComponentRequired(self):
        return self._ComponentRequired

    @ComponentRequired.setter
    def ComponentRequired(self, ComponentRequired):
        self._ComponentRequired = ComponentRequired

    @property
    def ComponentRecipientId(self):
        return self._ComponentRecipientId

    @ComponentRecipientId.setter
    def ComponentRecipientId(self, ComponentRecipientId):
        self._ComponentRecipientId = ComponentRecipientId

    @property
    def FileIndex(self):
        return self._FileIndex

    @FileIndex.setter
    def FileIndex(self, FileIndex):
        self._FileIndex = FileIndex

    @property
    def GenerateMode(self):
        return self._GenerateMode

    @GenerateMode.setter
    def GenerateMode(self, GenerateMode):
        self._GenerateMode = GenerateMode

    @property
    def ComponentWidth(self):
        return self._ComponentWidth

    @ComponentWidth.setter
    def ComponentWidth(self, ComponentWidth):
        self._ComponentWidth = ComponentWidth

    @property
    def ComponentHeight(self):
        return self._ComponentHeight

    @ComponentHeight.setter
    def ComponentHeight(self, ComponentHeight):
        self._ComponentHeight = ComponentHeight

    @property
    def ComponentPage(self):
        return self._ComponentPage

    @ComponentPage.setter
    def ComponentPage(self, ComponentPage):
        self._ComponentPage = ComponentPage

    @property
    def ComponentPosX(self):
        return self._ComponentPosX

    @ComponentPosX.setter
    def ComponentPosX(self, ComponentPosX):
        self._ComponentPosX = ComponentPosX

    @property
    def ComponentPosY(self):
        return self._ComponentPosY

    @ComponentPosY.setter
    def ComponentPosY(self, ComponentPosY):
        self._ComponentPosY = ComponentPosY

    @property
    def ComponentExtra(self):
        return self._ComponentExtra

    @ComponentExtra.setter
    def ComponentExtra(self, ComponentExtra):
        self._ComponentExtra = ComponentExtra

    @property
    def ComponentValue(self):
        return self._ComponentValue

    @ComponentValue.setter
    def ComponentValue(self, ComponentValue):
        self._ComponentValue = ComponentValue

    @property
    def ComponentDateFontSize(self):
        return self._ComponentDateFontSize

    @ComponentDateFontSize.setter
    def ComponentDateFontSize(self, ComponentDateFontSize):
        self._ComponentDateFontSize = ComponentDateFontSize

    @property
    def DocumentId(self):
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId

    @property
    def ComponentDescription(self):
        return self._ComponentDescription

    @ComponentDescription.setter
    def ComponentDescription(self, ComponentDescription):
        self._ComponentDescription = ComponentDescription

    @property
    def OffsetX(self):
        return self._OffsetX

    @OffsetX.setter
    def OffsetX(self, OffsetX):
        self._OffsetX = OffsetX

    @property
    def OffsetY(self):
        return self._OffsetY

    @OffsetY.setter
    def OffsetY(self, OffsetY):
        self._OffsetY = OffsetY

    @property
    def ChannelComponentId(self):
        return self._ChannelComponentId

    @ChannelComponentId.setter
    def ChannelComponentId(self, ChannelComponentId):
        self._ChannelComponentId = ChannelComponentId

    @property
    def KeywordOrder(self):
        return self._KeywordOrder

    @KeywordOrder.setter
    def KeywordOrder(self, KeywordOrder):
        self._KeywordOrder = KeywordOrder

    @property
    def KeywordPage(self):
        return self._KeywordPage

    @KeywordPage.setter
    def KeywordPage(self, KeywordPage):
        self._KeywordPage = KeywordPage

    @property
    def RelativeLocation(self):
        return self._RelativeLocation

    @RelativeLocation.setter
    def RelativeLocation(self, RelativeLocation):
        self._RelativeLocation = RelativeLocation

    @property
    def KeywordIndexes(self):
        return self._KeywordIndexes

    @KeywordIndexes.setter
    def KeywordIndexes(self, KeywordIndexes):
        self._KeywordIndexes = KeywordIndexes

    @property
    def Placeholder(self):
        return self._Placeholder

    @Placeholder.setter
    def Placeholder(self, Placeholder):
        self._Placeholder = Placeholder

    @property
    def LockComponentValue(self):
        return self._LockComponentValue

    @LockComponentValue.setter
    def LockComponentValue(self, LockComponentValue):
        self._LockComponentValue = LockComponentValue

    @property
    def ForbidMoveAndDelete(self):
        return self._ForbidMoveAndDelete

    @ForbidMoveAndDelete.setter
    def ForbidMoveAndDelete(self, ForbidMoveAndDelete):
        self._ForbidMoveAndDelete = ForbidMoveAndDelete


    def _deserialize(self, params):
        self._ComponentId = params.get("ComponentId")
        self._ComponentType = params.get("ComponentType")
        self._ComponentName = params.get("ComponentName")
        self._ComponentRequired = params.get("ComponentRequired")
        self._ComponentRecipientId = params.get("ComponentRecipientId")
        self._FileIndex = params.get("FileIndex")
        self._GenerateMode = params.get("GenerateMode")
        self._ComponentWidth = params.get("ComponentWidth")
        self._ComponentHeight = params.get("ComponentHeight")
        self._ComponentPage = params.get("ComponentPage")
        self._ComponentPosX = params.get("ComponentPosX")
        self._ComponentPosY = params.get("ComponentPosY")
        self._ComponentExtra = params.get("ComponentExtra")
        self._ComponentValue = params.get("ComponentValue")
        self._ComponentDateFontSize = params.get("ComponentDateFontSize")
        self._DocumentId = params.get("DocumentId")
        self._ComponentDescription = params.get("ComponentDescription")
        self._OffsetX = params.get("OffsetX")
        self._OffsetY = params.get("OffsetY")
        self._ChannelComponentId = params.get("ChannelComponentId")
        self._KeywordOrder = params.get("KeywordOrder")
        self._KeywordPage = params.get("KeywordPage")
        self._RelativeLocation = params.get("RelativeLocation")
        self._KeywordIndexes = params.get("KeywordIndexes")
        self._Placeholder = params.get("Placeholder")
        self._LockComponentValue = params.get("LockComponentValue")
        self._ForbidMoveAndDelete = params.get("ForbidMoveAndDelete")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentLimit(AbstractModel):
    """签署控件的类型和范围限制条件，用于控制文件发起后签署人拖拽签署区时可使用的控件类型和具体的印章或签名方式。

    """

    def __init__(self):
        r"""
        :param _ComponentType: 控件类型，支持以下类型
<ul><li>SIGN_SEAL : 印章控件</li>
<li>SIGN_PAGING_SEAL : 骑缝章控件</li>
<li>SIGN_LEGAL_PERSON_SEAL : 企业法定代表人控件</li>
<li>SIGN_SIGNATURE : 用户签名控件</li></ul>
        :type ComponentType: str
        :param _ComponentValue: 签署控件类型的值(可选)，用与限制签署时印章或者签名的选择范围

1.当ComponentType 是 SIGN_SEAL 或者 SIGN_PAGING_SEAL 时可传入企业印章Id（支持多个）

2.当ComponentType 是 SIGN_SIGNATURE 时可传入以下类型（支持多个）

<ul><li>HANDWRITE : 手写签名</li>
<li>OCR_ESIGN : OCR印章（智慧手写签名）</li>
<li>ESIGN : 个人印章</li>
<li>SYSTEM_ESIGN : 系统印章</li></ul>

3.当ComponentType 是 SIGN_LEGAL_PERSON_SEAL 时无需传递此参数。
        :type ComponentValue: list of str
        """
        self._ComponentType = None
        self._ComponentValue = None

    @property
    def ComponentType(self):
        return self._ComponentType

    @ComponentType.setter
    def ComponentType(self, ComponentType):
        self._ComponentType = ComponentType

    @property
    def ComponentValue(self):
        return self._ComponentValue

    @ComponentValue.setter
    def ComponentValue(self, ComponentValue):
        self._ComponentValue = ComponentValue


    def _deserialize(self, params):
        self._ComponentType = params.get("ComponentType")
        self._ComponentValue = params.get("ComponentValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateChannelFlowEvidenceReportRequest(AbstractModel):
    """CreateChannelFlowEvidenceReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowId: 签署流程编号
        :type FlowId: str
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._FlowId = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._FlowId = params.get("FlowId")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateChannelFlowEvidenceReportResponse(AbstractModel):
    """CreateChannelFlowEvidenceReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportId: 出证报告 ID，可用户DescribeChannelFlowEvidenceReport接口查询出证PDF的下载地址

注意：此字段可能返回 null，表示取不到有效值。
        :type ReportId: str
        :param _Status: 出征任务的执行状态,状态列表如下

- EvidenceStatusExecuting : 出征任务正在执行中
- EvidenceStatusSuccess : 出征任务执行成功
- EvidenceStatusFailed : 出征任务执行失败
        :type Status: str
        :param _ReportUrl: 废除，字段无效
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReportId = None
        self._Status = None
        self._ReportUrl = None
        self._RequestId = None

    @property
    def ReportId(self):
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ReportUrl(self):
        return self._ReportUrl

    @ReportUrl.setter
    def ReportUrl(self, ReportUrl):
        self._ReportUrl = ReportUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReportId = params.get("ReportId")
        self._Status = params.get("Status")
        self._ReportUrl = params.get("ReportUrl")
        self._RequestId = params.get("RequestId")


class CreateChannelOrganizationInfoChangeUrlRequest(AbstractModel):
    """CreateChannelOrganizationInfoChangeUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 关于渠道应用的相关信息，包括子客企业及应用编、号等详细内容，您可以参阅开发者中心所提供的 Agent 结构体以获取详细定义。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _ChangeType: 企业信息变更类型，可选类型如下：
<ul><li>**1**：企业超管变更</li><li>**2**：企业基础信息变更</li></ul>
        :type ChangeType: int
        """
        self._Agent = None
        self._ChangeType = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def ChangeType(self):
        return self._ChangeType

    @ChangeType.setter
    def ChangeType(self, ChangeType):
        self._ChangeType = ChangeType


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._ChangeType = params.get("ChangeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateChannelOrganizationInfoChangeUrlResponse(AbstractModel):
    """CreateChannelOrganizationInfoChangeUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 创建的企业信息变更链接。
        :type Url: str
        :param _ExpiredTime: 链接过期时间。链接7天有效。
        :type ExpiredTime: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._ExpiredTime = None
        self._RequestId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._ExpiredTime = params.get("ExpiredTime")
        self._RequestId = params.get("RequestId")


class CreateConsoleLoginUrlRequest(AbstractModel):
    """CreateConsoleLoginUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用信息
此接口Agent.AppId、Agent.ProxyOrganizationOpenId 和 Agent. ProxyOperator.OpenId 必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _ProxyOrganizationName: 子客企业名称，最大长度64个字符
注意：
1、如果您的企业已经在认证授权中或者激活完成，这里修改子客企业名字将不会生效。
2、该名称需要与Agent.ProxyOrganizationOpenId相匹配。
        :type ProxyOrganizationName: str
        :param _UniformSocialCreditCode: 子客企业统一社会信用代码，最大长度200个字符
注意：
1、如果您的企业已经在认证授权中或者激活完成，这里修改子客企业名字将不会生效。
        :type UniformSocialCreditCode: str
        :param _ProxyOperatorName: 子客企业经办人的姓名，最大长度50个字符
注意：
1、若经办人已经实名，这里修改经办人名字传入将不会生效。
2、该名称需要和Agent. ProxyOperator.OpenId相匹配
        :type ProxyOperatorName: str
        :param _Module: PC控制台登录后进入该参数指定的模块，如果不传递，将默认进入控制台首页。支持的模块包括：
1、DOCUMENT:合同管理模块，
2、TEMPLATE:企业模板管理模块，
3、SEAL:印章管理模块，
4、OPERATOR:组织管理模块，
默认将进入企业中心模块
注意：
1、如果EndPoint选择"CHANNEL"或"APP"，该参数仅支持传递"SEAL"，进入印章管理模块
2、该参数仅在企业和员工激活完成，登录控制台场景才生效。
        :type Module: str
        :param _ModuleId: 该参数和Module参数配合使用，用于指定模块下的资源Id，指定后链接登录将展示该资源的详情。
根据Module参数的不同所代表的含义不同。当前支持：
1、如果Module="SEAL"，ModuleId代表印章Id, 登录链接将直接查看指定印章的详情。
2、如果Module="TEMPLATE"，ModuleId代表模版Id，登录链接将直接查看指定模版的详情。
3、如果Module="1、DOCUMENT"，ModuleId代表合同Id，登录链接将直接查看指定合同的详情。
注意：
1、该参数仅在企业和员工激活完成，登录控制台场景才生效。
2、ModuleId需要和Module对应，ModuleId可以通过API或者控制台获取到。
        :type ModuleId: str
        :param _MenuStatus: 是否展示左侧菜单栏 
"ENABLE": 是，展示 
“DISABLE”: 否，不展示
默认值为ENABLE
注意：
1、该参数仅在企业和员工激活完成，登录控制台场景才生效。
        :type MenuStatus: str
        :param _Endpoint: 生成链接的类型：
"PC"：PC控制台链接
"CHANNEL"：H5跳转到电子签小程序链接
"APP"：第三方APP或小程序跳转电子签小程序链接
默认将生成PC控制台链接
        :type Endpoint: str
        :param _AutoJumpBackEvent: 触发自动跳转事件，仅对EndPoint为App类型有效，可选值包括：
"VERIFIED":企业认证完成/员工认证完成后跳回原App/小程序
        :type AutoJumpBackEvent: str
        :param _AuthorizationTypes: 可选的企业授权方式: 
1：上传授权书 
2：转法定代表人授权
4：企业实名认证（信任第三方认证源）（此项仅支持单选）
未选择信任第三方认证源时，如果是法人进行企业激活，仅支持法人扫脸直接授权，该配置不生效；选择信任第三方认证源时，请先通过“同步企业信息”接口同步信息。
该参数仅在企业激活场景生效
        :type AuthorizationTypes: list of int
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._ProxyOrganizationName = None
        self._UniformSocialCreditCode = None
        self._ProxyOperatorName = None
        self._Module = None
        self._ModuleId = None
        self._MenuStatus = None
        self._Endpoint = None
        self._AutoJumpBackEvent = None
        self._AuthorizationTypes = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def ProxyOrganizationName(self):
        return self._ProxyOrganizationName

    @ProxyOrganizationName.setter
    def ProxyOrganizationName(self, ProxyOrganizationName):
        self._ProxyOrganizationName = ProxyOrganizationName

    @property
    def UniformSocialCreditCode(self):
        return self._UniformSocialCreditCode

    @UniformSocialCreditCode.setter
    def UniformSocialCreditCode(self, UniformSocialCreditCode):
        self._UniformSocialCreditCode = UniformSocialCreditCode

    @property
    def ProxyOperatorName(self):
        return self._ProxyOperatorName

    @ProxyOperatorName.setter
    def ProxyOperatorName(self, ProxyOperatorName):
        self._ProxyOperatorName = ProxyOperatorName

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def ModuleId(self):
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def MenuStatus(self):
        return self._MenuStatus

    @MenuStatus.setter
    def MenuStatus(self, MenuStatus):
        self._MenuStatus = MenuStatus

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def AutoJumpBackEvent(self):
        return self._AutoJumpBackEvent

    @AutoJumpBackEvent.setter
    def AutoJumpBackEvent(self, AutoJumpBackEvent):
        self._AutoJumpBackEvent = AutoJumpBackEvent

    @property
    def AuthorizationTypes(self):
        return self._AuthorizationTypes

    @AuthorizationTypes.setter
    def AuthorizationTypes(self, AuthorizationTypes):
        self._AuthorizationTypes = AuthorizationTypes

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._ProxyOrganizationName = params.get("ProxyOrganizationName")
        self._UniformSocialCreditCode = params.get("UniformSocialCreditCode")
        self._ProxyOperatorName = params.get("ProxyOperatorName")
        self._Module = params.get("Module")
        self._ModuleId = params.get("ModuleId")
        self._MenuStatus = params.get("MenuStatus")
        self._Endpoint = params.get("Endpoint")
        self._AutoJumpBackEvent = params.get("AutoJumpBackEvent")
        self._AuthorizationTypes = params.get("AuthorizationTypes")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsoleLoginUrlResponse(AbstractModel):
    """CreateConsoleLoginUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConsoleUrl: 子客企业Web控制台url注意事项：
1. 所有类型的链接在企业未认证/员工未认证完成时，只要在有效期内（一年）都可以访问
2. 若企业认证完成且员工认证完成后，重新获取pc端的链接在5分钟之内有效，且只能访问一次
3. 若企业认证完成且员工认证完成后，重新获取CHANNEL/APP的链接只要在有效期内（一年）都可以访问
4. 此链接仅单次有效，每次登录需要需要重新创建新的链接，尽量不要做链接存储，多次使用。
5. 创建的链接应避免被转义，如：&被转义为\u0026；如使用Postman请求后，请选择响应类型为 JSON，否则链接将被转义
        :type ConsoleUrl: str
        :param _IsActivated: 子客企业是否已开通腾讯电子签，true-是，false-否
注意：
1、企业是否实名根据传参Agent.ProxyOrganizationOpenId进行判断，非企业名称或者社会信用代码
        :type IsActivated: bool
        :param _ProxyOperatorIsVerified: 当前经办人是否已认证，true-是，false-否
注意：
1、经办人是否实名是根据Agent.ProxyOperator.OpenId判断，非经办人姓名
        :type ProxyOperatorIsVerified: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConsoleUrl = None
        self._IsActivated = None
        self._ProxyOperatorIsVerified = None
        self._RequestId = None

    @property
    def ConsoleUrl(self):
        return self._ConsoleUrl

    @ConsoleUrl.setter
    def ConsoleUrl(self, ConsoleUrl):
        self._ConsoleUrl = ConsoleUrl

    @property
    def IsActivated(self):
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def ProxyOperatorIsVerified(self):
        return self._ProxyOperatorIsVerified

    @ProxyOperatorIsVerified.setter
    def ProxyOperatorIsVerified(self, ProxyOperatorIsVerified):
        self._ProxyOperatorIsVerified = ProxyOperatorIsVerified

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ConsoleUrl = params.get("ConsoleUrl")
        self._IsActivated = params.get("IsActivated")
        self._ProxyOperatorIsVerified = params.get("ProxyOperatorIsVerified")
        self._RequestId = params.get("RequestId")


class CreateFlowOption(AbstractModel):
    """创建合同个性化参数

    """

    def __init__(self):
        r"""
        :param _CanEditFlow: 是否允许修改合同信息，true-是，false-否
        :type CanEditFlow: bool
        :param _HideShowFlowName: 是否允许发起合同弹窗隐藏合同名称，true-允许，false-不允许
        :type HideShowFlowName: bool
        :param _HideShowFlowType: 是否允许发起合同弹窗隐藏合同类型，true-允许，false-不允许
        :type HideShowFlowType: bool
        :param _HideShowDeadline: 是否允许发起合同弹窗隐藏合同到期时间，true-允许，false-不允许
        :type HideShowDeadline: bool
        :param _CanSkipAddApprover: 是否允许发起合同步骤跳过指定签署方步骤，true-允许，false-不允许
        :type CanSkipAddApprover: bool
        :param _CustomCreateFlowDescription: 定制化发起合同弹窗的描述信息，描述信息最长500
        :type CustomCreateFlowDescription: str
        """
        self._CanEditFlow = None
        self._HideShowFlowName = None
        self._HideShowFlowType = None
        self._HideShowDeadline = None
        self._CanSkipAddApprover = None
        self._CustomCreateFlowDescription = None

    @property
    def CanEditFlow(self):
        return self._CanEditFlow

    @CanEditFlow.setter
    def CanEditFlow(self, CanEditFlow):
        self._CanEditFlow = CanEditFlow

    @property
    def HideShowFlowName(self):
        return self._HideShowFlowName

    @HideShowFlowName.setter
    def HideShowFlowName(self, HideShowFlowName):
        self._HideShowFlowName = HideShowFlowName

    @property
    def HideShowFlowType(self):
        return self._HideShowFlowType

    @HideShowFlowType.setter
    def HideShowFlowType(self, HideShowFlowType):
        self._HideShowFlowType = HideShowFlowType

    @property
    def HideShowDeadline(self):
        return self._HideShowDeadline

    @HideShowDeadline.setter
    def HideShowDeadline(self, HideShowDeadline):
        self._HideShowDeadline = HideShowDeadline

    @property
    def CanSkipAddApprover(self):
        return self._CanSkipAddApprover

    @CanSkipAddApprover.setter
    def CanSkipAddApprover(self, CanSkipAddApprover):
        self._CanSkipAddApprover = CanSkipAddApprover

    @property
    def CustomCreateFlowDescription(self):
        return self._CustomCreateFlowDescription

    @CustomCreateFlowDescription.setter
    def CustomCreateFlowDescription(self, CustomCreateFlowDescription):
        self._CustomCreateFlowDescription = CustomCreateFlowDescription


    def _deserialize(self, params):
        self._CanEditFlow = params.get("CanEditFlow")
        self._HideShowFlowName = params.get("HideShowFlowName")
        self._HideShowFlowType = params.get("HideShowFlowType")
        self._HideShowDeadline = params.get("HideShowDeadline")
        self._CanSkipAddApprover = params.get("CanSkipAddApprover")
        self._CustomCreateFlowDescription = params.get("CustomCreateFlowDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowsByTemplatesRequest(AbstractModel):
    """CreateFlowsByTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 均必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowInfos: 要创建的合同信息列表，最多支持一次创建20个合同
        :type FlowInfos: list of FlowInfo
        :param _NeedPreview: 是否为预览模式；默认为false，即非预览模式，此时发起合同并返回FlowIds；若为预览模式，不会发起合同，会返回PreviewUrls；
预览链接有效期300秒；
同时，如果预览的文件中指定了动态表格控件，需要进行异步合成；此时此接口返回的是合成前的文档预览链接，而合成完成后的文档预览链接会通过：回调通知的方式、或使用返回的TaskInfo中的TaskId通过ChannelGetTaskResultApi接口查询；
        :type NeedPreview: bool
        :param _PreviewType: 预览链接类型 默认:0-文件流, 1- H5链接 注意:此参数在NeedPreview 为true 时有效,
        :type PreviewType: int
        :param _Operator: 操作者的信息，不用传
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._FlowInfos = None
        self._NeedPreview = None
        self._PreviewType = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowInfos(self):
        return self._FlowInfos

    @FlowInfos.setter
    def FlowInfos(self, FlowInfos):
        self._FlowInfos = FlowInfos

    @property
    def NeedPreview(self):
        return self._NeedPreview

    @NeedPreview.setter
    def NeedPreview(self, NeedPreview):
        self._NeedPreview = NeedPreview

    @property
    def PreviewType(self):
        return self._PreviewType

    @PreviewType.setter
    def PreviewType(self, PreviewType):
        self._PreviewType = PreviewType

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("FlowInfos") is not None:
            self._FlowInfos = []
            for item in params.get("FlowInfos"):
                obj = FlowInfo()
                obj._deserialize(item)
                self._FlowInfos.append(obj)
        self._NeedPreview = params.get("NeedPreview")
        self._PreviewType = params.get("PreviewType")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowsByTemplatesResponse(AbstractModel):
    """CreateFlowsByTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowIds: 多个合同ID
        :type FlowIds: list of str
        :param _CustomerData: 第三方应用平台的业务信息, 与创建合同的FlowInfos数组中的CustomerData一一对应
        :type CustomerData: list of str
        :param _ErrorMessages: 创建消息，对应多个合同ID，
成功为“”,创建失败则对应失败消息
        :type ErrorMessages: list of str
        :param _PreviewUrls: 预览模式下返回的预览文件url数组
        :type PreviewUrls: list of str
        :param _TaskInfos: 复杂文档合成任务（如，包含动态表格的预览任务）的任务信息数组；
如果文档需要异步合成，此字段会返回该异步任务的任务信息，后续可以通过ChannelGetTaskResultApi接口查询任务详情；
        :type TaskInfos: list of TaskInfo
        :param _FlowApprovers: 签署方信息，如角色ID、角色名称等
        :type FlowApprovers: list of FlowApproverItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowIds = None
        self._CustomerData = None
        self._ErrorMessages = None
        self._PreviewUrls = None
        self._TaskInfos = None
        self._FlowApprovers = None
        self._RequestId = None

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def CustomerData(self):
        return self._CustomerData

    @CustomerData.setter
    def CustomerData(self, CustomerData):
        self._CustomerData = CustomerData

    @property
    def ErrorMessages(self):
        return self._ErrorMessages

    @ErrorMessages.setter
    def ErrorMessages(self, ErrorMessages):
        self._ErrorMessages = ErrorMessages

    @property
    def PreviewUrls(self):
        return self._PreviewUrls

    @PreviewUrls.setter
    def PreviewUrls(self, PreviewUrls):
        self._PreviewUrls = PreviewUrls

    @property
    def TaskInfos(self):
        return self._TaskInfos

    @TaskInfos.setter
    def TaskInfos(self, TaskInfos):
        self._TaskInfos = TaskInfos

    @property
    def FlowApprovers(self):
        return self._FlowApprovers

    @FlowApprovers.setter
    def FlowApprovers(self, FlowApprovers):
        self._FlowApprovers = FlowApprovers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowIds = params.get("FlowIds")
        self._CustomerData = params.get("CustomerData")
        self._ErrorMessages = params.get("ErrorMessages")
        self._PreviewUrls = params.get("PreviewUrls")
        if params.get("TaskInfos") is not None:
            self._TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = TaskInfo()
                obj._deserialize(item)
                self._TaskInfos.append(obj)
        if params.get("FlowApprovers") is not None:
            self._FlowApprovers = []
            for item in params.get("FlowApprovers"):
                obj = FlowApproverItem()
                obj._deserialize(item)
                self._FlowApprovers.append(obj)
        self._RequestId = params.get("RequestId")


class CreateSealByImageRequest(AbstractModel):
    """CreateSealByImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _SealName: 印章名称，最大长度不超过50字符
        :type SealName: str
        :param _SealImage: 印章图片base64，大小不超过10M（原始图片不超过7.6M）
        :type SealImage: str
        :param _Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param _GenerateSource: 本接口支持上传图片印章及系统直接生成印章； 如果要使用系统生成印章，此值传：SealGenerateSourceSystem； 如果要使用图片上传请传字段 SealImage
        :type GenerateSource: str
        :param _SealType: 电子印章类型：
<ul><li>OFFICIAL-公章</li>
<li>CONTRACT-合同专用章;</li>
<li>FINANCE-合财务专用章;</li>
<li>PERSONNEL-人事专用章
</li>
<li>默认：OFFICIAL</li>
</ul>
        :type SealType: str
        :param _SealHorizontalText: 企业印章横向文字，最多可填15个汉字（若超过印章最大宽度，优先压缩字间距，其次缩小字号
        :type SealHorizontalText: str
        :param _SealStyle: 印章样式:

<ul><li>cycle:圆形印章</li>
<li>ellipse:椭圆印章</li>
<li> 注：默认圆形印章</li></ul>
        :type SealStyle: str
        :param _SealSize: 印章尺寸取值描述：<ul><li> 42_42 圆形企业公章直径42mm</li>
<li> 40_40 圆形企业印章直径40mm</li>
<li> 45_30 椭圆形印章45mm x 30mm</li>
</ul>
        :type SealSize: str
        """
        self._Agent = None
        self._SealName = None
        self._SealImage = None
        self._Operator = None
        self._GenerateSource = None
        self._SealType = None
        self._SealHorizontalText = None
        self._SealStyle = None
        self._SealSize = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def SealName(self):
        return self._SealName

    @SealName.setter
    def SealName(self, SealName):
        self._SealName = SealName

    @property
    def SealImage(self):
        return self._SealImage

    @SealImage.setter
    def SealImage(self, SealImage):
        self._SealImage = SealImage

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator

    @property
    def GenerateSource(self):
        return self._GenerateSource

    @GenerateSource.setter
    def GenerateSource(self, GenerateSource):
        self._GenerateSource = GenerateSource

    @property
    def SealType(self):
        return self._SealType

    @SealType.setter
    def SealType(self, SealType):
        self._SealType = SealType

    @property
    def SealHorizontalText(self):
        return self._SealHorizontalText

    @SealHorizontalText.setter
    def SealHorizontalText(self, SealHorizontalText):
        self._SealHorizontalText = SealHorizontalText

    @property
    def SealStyle(self):
        return self._SealStyle

    @SealStyle.setter
    def SealStyle(self, SealStyle):
        self._SealStyle = SealStyle

    @property
    def SealSize(self):
        return self._SealSize

    @SealSize.setter
    def SealSize(self, SealSize):
        self._SealSize = SealSize


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._SealName = params.get("SealName")
        self._SealImage = params.get("SealImage")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._GenerateSource = params.get("GenerateSource")
        self._SealType = params.get("SealType")
        self._SealHorizontalText = params.get("SealHorizontalText")
        self._SealStyle = params.get("SealStyle")
        self._SealSize = params.get("SealSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSealByImageResponse(AbstractModel):
    """CreateSealByImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SealId: 电子印章ID，为32位字符串。
建议开发者保留此印章ID，后续指定签署区印章或者操作印章需此印章ID。
可登录腾讯电子签控制台，在 "印章"->"印章中心"选择查看的印章，在"印章详情" 中查看某个印章的SealId(在页面中展示为印章ID)。
        :type SealId: str
        :param _ImageUrl: 电子印章预览链接地址，地址默认失效时间为24小时。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SealId = None
        self._ImageUrl = None
        self._RequestId = None

    @property
    def SealId(self):
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SealId = params.get("SealId")
        self._ImageUrl = params.get("ImageUrl")
        self._RequestId = params.get("RequestId")


class CreateSignUrlsRequest(AbstractModel):
    """CreateSignUrls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowIds: 流程(合同)的编号列表，最多支持100个。(备注：该参数和合同组编号必须二选一)
        :type FlowIds: list of str
        :param _FlowGroupId: 合同组编号(备注：该参数和合同(流程)编号数组必须二选一)
        :type FlowGroupId: str
        :param _Endpoint: 签署链接类型,可以设置的参数如下

- WEIXINAPP:短链直接跳小程序 (默认类型)
- CHANNEL:跳转H5页面
- APP:第三方APP或小程序跳转电子签小程序
- LONGURL2WEIXINAPP:长链接跳转小程序
        :type Endpoint: str
        :param _GenerateType: 签署链接生成类型，可以选择的类型如下

- ALL：全部签署方签署链接，此时不会给自动签署的签署方创建签署链接(默认类型)
- CHANNEL：第三方平台子客企业企业
- NOT_CHANNEL：非第三方平台子客企业企业
- PERSON：个人
- FOLLOWER：关注方，目前是合同抄送方
- RECIPIENT：获取RecipientId对应的签署链接，可用于生成动态签署人补充链接
        :type GenerateType: str
        :param _OrganizationName: 非第三方平台子客企业参与方的企业名称，GenerateType为"NOT_CHANNEL"时必填
        :type OrganizationName: str
        :param _Name: 参与人姓名
GenerateType为"PERSON"(即个人签署方)时必填
        :type Name: str
        :param _Mobile: 参与人手机号
GenerateType为"PERSON"或"FOLLOWER"时必填
        :type Mobile: str
        :param _OrganizationOpenId: 第三方平台子客企业的企业OpenId，GenerateType为"CHANNEL"时必填
        :type OrganizationOpenId: str
        :param _OpenId: 第三方平台子客企业参与人OpenId，GenerateType为"CHANNEL"时可用，指定到具体参与人, 仅展示已经实名的经办人信息
        :type OpenId: str
        :param _AutoJumpBack: Endpoint为"APP" 类型的签署链接，可以设置此值；支持调用方小程序打开签署链接，在电子签小程序完成签署后自动回跳至调用方小程序
        :type AutoJumpBack: bool
        :param _JumpUrl: 签署完之后的H5页面的跳转链接，针对Endpoint为CHANNEL时有效，最大长度1000个字符。
        :type JumpUrl: str
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param _Hides: 生成的签署链接在签署过程隐藏的按钮列表, 可以设置隐藏的按钮列表如下

- 0:合同签署页面更多操作按钮
- 1:合同签署页面更多操作的拒绝签署按钮
- 2:合同签署页面更多操作的转他人处理按钮
- 3:签署成功页的查看详情按钮
        :type Hides: list of int
        :param _RecipientIds: 签署节点ID，用于补充动态签署人，使用此参数需要与flow_ids数量一致并且一一对应
        :type RecipientIds: list of str
        """
        self._Agent = None
        self._FlowIds = None
        self._FlowGroupId = None
        self._Endpoint = None
        self._GenerateType = None
        self._OrganizationName = None
        self._Name = None
        self._Mobile = None
        self._OrganizationOpenId = None
        self._OpenId = None
        self._AutoJumpBack = None
        self._JumpUrl = None
        self._Operator = None
        self._Hides = None
        self._RecipientIds = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def FlowGroupId(self):
        return self._FlowGroupId

    @FlowGroupId.setter
    def FlowGroupId(self, FlowGroupId):
        self._FlowGroupId = FlowGroupId

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def GenerateType(self):
        return self._GenerateType

    @GenerateType.setter
    def GenerateType(self, GenerateType):
        self._GenerateType = GenerateType

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def OrganizationOpenId(self):
        return self._OrganizationOpenId

    @OrganizationOpenId.setter
    def OrganizationOpenId(self, OrganizationOpenId):
        self._OrganizationOpenId = OrganizationOpenId

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def AutoJumpBack(self):
        return self._AutoJumpBack

    @AutoJumpBack.setter
    def AutoJumpBack(self, AutoJumpBack):
        self._AutoJumpBack = AutoJumpBack

    @property
    def JumpUrl(self):
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator

    @property
    def Hides(self):
        return self._Hides

    @Hides.setter
    def Hides(self, Hides):
        self._Hides = Hides

    @property
    def RecipientIds(self):
        return self._RecipientIds

    @RecipientIds.setter
    def RecipientIds(self, RecipientIds):
        self._RecipientIds = RecipientIds


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._FlowIds = params.get("FlowIds")
        self._FlowGroupId = params.get("FlowGroupId")
        self._Endpoint = params.get("Endpoint")
        self._GenerateType = params.get("GenerateType")
        self._OrganizationName = params.get("OrganizationName")
        self._Name = params.get("Name")
        self._Mobile = params.get("Mobile")
        self._OrganizationOpenId = params.get("OrganizationOpenId")
        self._OpenId = params.get("OpenId")
        self._AutoJumpBack = params.get("AutoJumpBack")
        self._JumpUrl = params.get("JumpUrl")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._Hides = params.get("Hides")
        self._RecipientIds = params.get("RecipientIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSignUrlsResponse(AbstractModel):
    """CreateSignUrls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SignUrlInfos: 签署参与者签署H5链接信息数组
        :type SignUrlInfos: list of SignUrlInfo
        :param _ErrorMessages: 生成失败时的错误信息，成功返回”“，顺序和出参SignUrlInfos保持一致
        :type ErrorMessages: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SignUrlInfos = None
        self._ErrorMessages = None
        self._RequestId = None

    @property
    def SignUrlInfos(self):
        return self._SignUrlInfos

    @SignUrlInfos.setter
    def SignUrlInfos(self, SignUrlInfos):
        self._SignUrlInfos = SignUrlInfos

    @property
    def ErrorMessages(self):
        return self._ErrorMessages

    @ErrorMessages.setter
    def ErrorMessages(self, ErrorMessages):
        self._ErrorMessages = ErrorMessages

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SignUrlInfos") is not None:
            self._SignUrlInfos = []
            for item in params.get("SignUrlInfos"):
                obj = SignUrlInfo()
                obj._deserialize(item)
                self._SignUrlInfos.append(obj)
        self._ErrorMessages = params.get("ErrorMessages")
        self._RequestId = params.get("RequestId")


class Department(AbstractModel):
    """第三方应用集成员工部门信息

    """

    def __init__(self):
        r"""
        :param _DepartmentId: 部门id
注意：此字段可能返回 null，表示取不到有效值。
        :type DepartmentId: str
        :param _DepartmentName: 部门名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DepartmentName: str
        """
        self._DepartmentId = None
        self._DepartmentName = None

    @property
    def DepartmentId(self):
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def DepartmentName(self):
        return self._DepartmentName

    @DepartmentName.setter
    def DepartmentName(self, DepartmentName):
        self._DepartmentName = DepartmentName


    def _deserialize(self, params):
        self._DepartmentId = params.get("DepartmentId")
        self._DepartmentName = params.get("DepartmentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChannelFlowEvidenceReportRequest(AbstractModel):
    """DescribeChannelFlowEvidenceReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _ReportId: 出证报告编号
        :type ReportId: str
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._ReportId = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def ReportId(self):
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._ReportId = params.get("ReportId")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChannelFlowEvidenceReportResponse(AbstractModel):
    """DescribeChannelFlowEvidenceReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportUrl: 出证报告下载 URL
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportUrl: str
        :param _Status: 出征任务的执行状态,状态列表如下

- EvidenceStatusExecuting : 出征任务正在执行中
- EvidenceStatusSuccess : 出征任务执行成功
- EvidenceStatusFailed : 出征任务执行失败
        :type Status: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReportUrl = None
        self._Status = None
        self._RequestId = None

    @property
    def ReportUrl(self):
        return self._ReportUrl

    @ReportUrl.setter
    def ReportUrl(self, ReportUrl):
        self._ReportUrl = ReportUrl

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReportUrl = params.get("ReportUrl")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeExtendedServiceAuthInfoRequest(AbstractModel):
    """DescribeExtendedServiceAuthInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填

注: 此接口 参数Agent. ProxyOperator.OpenId 需要传递超管或者法人的OpenId

        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        """
        self._Agent = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExtendedServiceAuthInfoResponse(AbstractModel):
    """DescribeExtendedServiceAuthInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AuthInfo: 企业扩展服务授权信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthInfo: list of ExtentServiceAuthInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AuthInfo = None
        self._RequestId = None

    @property
    def AuthInfo(self):
        return self._AuthInfo

    @AuthInfo.setter
    def AuthInfo(self, AuthInfo):
        self._AuthInfo = AuthInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AuthInfo") is not None:
            self._AuthInfo = []
            for item in params.get("AuthInfo"):
                obj = ExtentServiceAuthInfo()
                obj._deserialize(item)
                self._AuthInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFlowDetailInfoRequest(AbstractModel):
    """DescribeFlowDetailInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowIds: 合同(流程)编号数组，最多支持100个。
<br/>备注：该参数和合同组编号必须二选一, 如果填写FlowGroupId则忽略此FlowIds的入参
        :type FlowIds: list of str
        :param _FlowGroupId: 合同组编号
<br/>备注：该参数和合同(流程)编号数组必须二选一
        :type FlowGroupId: str
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._FlowIds = None
        self._FlowGroupId = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def FlowGroupId(self):
        return self._FlowGroupId

    @FlowGroupId.setter
    def FlowGroupId(self, FlowGroupId):
        self._FlowGroupId = FlowGroupId

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._FlowIds = params.get("FlowIds")
        self._FlowGroupId = params.get("FlowGroupId")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowDetailInfoResponse(AbstractModel):
    """DescribeFlowDetailInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 第三方平台应用号Id
        :type ApplicationId: str
        :param _ProxyOrganizationOpenId: 第三方平台子客企业OpenId
        :type ProxyOrganizationOpenId: str
        :param _FlowInfo: 合同(签署流程)的具体详细描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowInfo: list of FlowDetailInfo
        :param _FlowGroupId: 合同组编号
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowGroupId: str
        :param _FlowGroupName: 合同组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowGroupName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicationId = None
        self._ProxyOrganizationOpenId = None
        self._FlowInfo = None
        self._FlowGroupId = None
        self._FlowGroupName = None
        self._RequestId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ProxyOrganizationOpenId(self):
        return self._ProxyOrganizationOpenId

    @ProxyOrganizationOpenId.setter
    def ProxyOrganizationOpenId(self, ProxyOrganizationOpenId):
        self._ProxyOrganizationOpenId = ProxyOrganizationOpenId

    @property
    def FlowInfo(self):
        return self._FlowInfo

    @FlowInfo.setter
    def FlowInfo(self, FlowInfo):
        self._FlowInfo = FlowInfo

    @property
    def FlowGroupId(self):
        return self._FlowGroupId

    @FlowGroupId.setter
    def FlowGroupId(self, FlowGroupId):
        self._FlowGroupId = FlowGroupId

    @property
    def FlowGroupName(self):
        return self._FlowGroupName

    @FlowGroupName.setter
    def FlowGroupName(self, FlowGroupName):
        self._FlowGroupName = FlowGroupName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ProxyOrganizationOpenId = params.get("ProxyOrganizationOpenId")
        if params.get("FlowInfo") is not None:
            self._FlowInfo = []
            for item in params.get("FlowInfo"):
                obj = FlowDetailInfo()
                obj._deserialize(item)
                self._FlowInfo.append(obj)
        self._FlowGroupId = params.get("FlowGroupId")
        self._FlowGroupName = params.get("FlowGroupName")
        self._RequestId = params.get("RequestId")


class DescribeResourceUrlsByFlowsRequest(AbstractModel):
    """DescribeResourceUrlsByFlows请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。
此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowIds: 查询资源所对应的签署流程Id，最多支持50个
        :type FlowIds: list of str
        :param _Operator: 操作者的信息，不用传
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._FlowIds = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._FlowIds = params.get("FlowIds")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceUrlsByFlowsResponse(AbstractModel):
    """DescribeResourceUrlsByFlows返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowResourceUrlInfos: 签署流程资源对应链接信息
        :type FlowResourceUrlInfos: list of FlowResourceUrlInfo
        :param _ErrorMessages: 创建消息，对应多个合同ID，
成功为“”,创建失败则对应失败消息
        :type ErrorMessages: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowResourceUrlInfos = None
        self._ErrorMessages = None
        self._RequestId = None

    @property
    def FlowResourceUrlInfos(self):
        return self._FlowResourceUrlInfos

    @FlowResourceUrlInfos.setter
    def FlowResourceUrlInfos(self, FlowResourceUrlInfos):
        self._FlowResourceUrlInfos = FlowResourceUrlInfos

    @property
    def ErrorMessages(self):
        return self._ErrorMessages

    @ErrorMessages.setter
    def ErrorMessages(self, ErrorMessages):
        self._ErrorMessages = ErrorMessages

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FlowResourceUrlInfos") is not None:
            self._FlowResourceUrlInfos = []
            for item in params.get("FlowResourceUrlInfos"):
                obj = FlowResourceUrlInfo()
                obj._deserialize(item)
                self._FlowResourceUrlInfos.append(obj)
        self._ErrorMessages = params.get("ErrorMessages")
        self._RequestId = params.get("RequestId")


class DescribeTemplatesRequest(AbstractModel):
    """DescribeTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 
此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _TemplateId: 模板唯一标识，查询单个模板时使用
        :type TemplateId: str
        :param _ContentType: 查询内容：
0-模板列表及详情（默认），
1-仅模板列表
        :type ContentType: int
        :param _Limit: 指定每页多少条数据，如果不传默认为20，单页最大100。
        :type Limit: int
        :param _Offset: 查询结果分页返回，此处指定第几页，如果不传默从第一页返回。页码从0开始，即首页为0。
        :type Offset: int
        :param _QueryAllComponents: 是否返回所有组件信息。
默认false，只返回发起方控件；
true，返回所有签署方控件
        :type QueryAllComponents: bool
        :param _TemplateName: 模糊搜索模板名称，最大长度200
        :type TemplateName: str
        :param _WithPreviewUrl: 是否获取模板预览链接，
默认false-不获取
true-获取
        :type WithPreviewUrl: bool
        :param _WithPdfUrl: 是否获取模板的PDF文件链接。
默认false-不获取
true-获取
请联系客户经理开白后使用。
        :type WithPdfUrl: bool
        :param _ChannelTemplateId: 对应第三方应用平台企业的模板ID
        :type ChannelTemplateId: str
        :param _Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._TemplateId = None
        self._ContentType = None
        self._Limit = None
        self._Offset = None
        self._QueryAllComponents = None
        self._TemplateName = None
        self._WithPreviewUrl = None
        self._WithPdfUrl = None
        self._ChannelTemplateId = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def ContentType(self):
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def QueryAllComponents(self):
        return self._QueryAllComponents

    @QueryAllComponents.setter
    def QueryAllComponents(self, QueryAllComponents):
        self._QueryAllComponents = QueryAllComponents

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def WithPreviewUrl(self):
        return self._WithPreviewUrl

    @WithPreviewUrl.setter
    def WithPreviewUrl(self, WithPreviewUrl):
        self._WithPreviewUrl = WithPreviewUrl

    @property
    def WithPdfUrl(self):
        return self._WithPdfUrl

    @WithPdfUrl.setter
    def WithPdfUrl(self, WithPdfUrl):
        self._WithPdfUrl = WithPdfUrl

    @property
    def ChannelTemplateId(self):
        return self._ChannelTemplateId

    @ChannelTemplateId.setter
    def ChannelTemplateId(self, ChannelTemplateId):
        self._ChannelTemplateId = ChannelTemplateId

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._TemplateId = params.get("TemplateId")
        self._ContentType = params.get("ContentType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._QueryAllComponents = params.get("QueryAllComponents")
        self._TemplateName = params.get("TemplateName")
        self._WithPreviewUrl = params.get("WithPreviewUrl")
        self._WithPdfUrl = params.get("WithPdfUrl")
        self._ChannelTemplateId = params.get("ChannelTemplateId")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTemplatesResponse(AbstractModel):
    """DescribeTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Templates: 模板列表
        :type Templates: list of TemplateInfo
        :param _TotalCount: 查询到的总数
        :type TotalCount: int
        :param _Limit: 每页多少条数据
        :type Limit: int
        :param _Offset: 查询结果分页返回，此处指定第几页。页码从0开始，即首页为0。
        :type Offset: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Templates = None
        self._TotalCount = None
        self._Limit = None
        self._Offset = None
        self._RequestId = None

    @property
    def Templates(self):
        return self._Templates

    @Templates.setter
    def Templates(self, Templates):
        self._Templates = Templates

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self._Templates = []
            for item in params.get("Templates"):
                obj = TemplateInfo()
                obj._deserialize(item)
                self._Templates.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._RequestId = params.get("RequestId")


class DescribeUsageRequest(AbstractModel):
    """DescribeUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用信息，此接口Agent.AppId必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _StartDate: 开始时间，例如：2021-03-21
        :type StartDate: str
        :param _EndDate: 结束时间，例如：2021-06-21；
开始时间到结束时间的区间长度小于等于90天。
        :type EndDate: str
        :param _NeedAggregate: 是否汇总数据，默认不汇总。
不汇总：返回在统计区间内第三方平台下所有企业的每日明细，即每个企业N条数据，N为统计天数；
汇总：返回在统计区间内第三方平台下所有企业的汇总后数据，即每个企业一条数据；
        :type NeedAggregate: bool
        :param _Limit: 单次返回的最多条目数量。默认为1000，且不能超过1000。
        :type Limit: int
        :param _Offset: 偏移量，默认是0。
        :type Offset: int
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._StartDate = None
        self._EndDate = None
        self._NeedAggregate = None
        self._Limit = None
        self._Offset = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def NeedAggregate(self):
        return self._NeedAggregate

    @NeedAggregate.setter
    def NeedAggregate(self, NeedAggregate):
        self._NeedAggregate = NeedAggregate

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._NeedAggregate = params.get("NeedAggregate")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsageResponse(AbstractModel):
    """DescribeUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 用量明细条数
        :type Total: int
        :param _Details: 用量明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of UsageDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Details = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = UsageDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DownloadFlowInfo(AbstractModel):
    """签署流程下载信息

    """

    def __init__(self):
        r"""
        :param _FileName: 文件夹名称
        :type FileName: str
        :param _FlowIdList: 签署流程的标识数组
        :type FlowIdList: list of str
        """
        self._FileName = None
        self._FlowIdList = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FlowIdList(self):
        return self._FlowIdList

    @FlowIdList.setter
    def FlowIdList(self, FlowIdList):
        self._FlowIdList = FlowIdList


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FlowIdList = params.get("FlowIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtentServiceAuthInfo(AbstractModel):
    """企业扩展服务授权信息

    """

    def __init__(self):
        r"""
        :param _Type: 扩展服务类型
<ul>
  <li>AUTO_SIGN             企业静默签（自动签署）</li>
<li>  OVERSEA_SIGN          企业与港澳台居民*签署合同</li>
<li>  MOBILE_CHECK_APPROVER 使用手机号验证签署方身份</li>
 <li> PAGING_SEAL           骑缝章</li>
 <li> DOWNLOAD_FLOW         授权渠道下载合同 </li>
<li>AGE_LIMIT_EXPANSION 拓宽签署方年龄限制</li>
</ul>
        :type Type: str
        :param _Name: 扩展服务名称 
        :type Name: str
        :param _Status: 服务状态 
ENABLE 开启 
DISABLE 关闭
        :type Status: str
        :param _OperatorOpenId: 最近操作人第三方应用平台的用户openid
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorOpenId: str
        :param _OperateOn: 最近操作时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateOn: int
        """
        self._Type = None
        self._Name = None
        self._Status = None
        self._OperatorOpenId = None
        self._OperateOn = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OperatorOpenId(self):
        return self._OperatorOpenId

    @OperatorOpenId.setter
    def OperatorOpenId(self, OperatorOpenId):
        self._OperatorOpenId = OperatorOpenId

    @property
    def OperateOn(self):
        return self._OperateOn

    @OperateOn.setter
    def OperateOn(self, OperateOn):
        self._OperateOn = OperateOn


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._OperatorOpenId = params.get("OperatorOpenId")
        self._OperateOn = params.get("OperateOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FailedCreateRoleData(AbstractModel):
    """绑定失败的用户角色信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户userId
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _RoleIds: 角色RoleId列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleIds: list of str
        """
        self._UserId = None
        self._RoleIds = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoleIds(self):
        return self._RoleIds

    @RoleIds.setter
    def RoleIds(self, RoleIds):
        self._RoleIds = RoleIds


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._RoleIds = params.get("RoleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FillApproverInfo(AbstractModel):
    """指定补充签署人信息
    - RecipientId 必须指定

    """

    def __init__(self):
        r"""
        :param _RecipientId: 签署方经办人在模板中配置的参与方ID，与控件绑定，是控件的归属方，ID为32位字符串。

        :type RecipientId: str
        :param _OpenId: 指定企业经办签署人OpenId
        :type OpenId: str
        :param _ApproverName: 签署人姓名
        :type ApproverName: str
        :param _ApproverMobile: 签署人手机号码
        :type ApproverMobile: str
        :param _OrganizationName: 企业名称
        :type OrganizationName: str
        :param _OrganizationOpenId: 企业OpenId
        :type OrganizationOpenId: str
        :param _NotChannelOrganization: 签署企业非渠道子客，默认为false，即表示同一渠道下的企业；如果为true，则目前表示接收方企业为SaaS企业, 为渠道子客时，organization_open_id+open_id 必传
        :type NotChannelOrganization: str
        """
        self._RecipientId = None
        self._OpenId = None
        self._ApproverName = None
        self._ApproverMobile = None
        self._OrganizationName = None
        self._OrganizationOpenId = None
        self._NotChannelOrganization = None

    @property
    def RecipientId(self):
        return self._RecipientId

    @RecipientId.setter
    def RecipientId(self, RecipientId):
        self._RecipientId = RecipientId

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def ApproverName(self):
        return self._ApproverName

    @ApproverName.setter
    def ApproverName(self, ApproverName):
        self._ApproverName = ApproverName

    @property
    def ApproverMobile(self):
        return self._ApproverMobile

    @ApproverMobile.setter
    def ApproverMobile(self, ApproverMobile):
        self._ApproverMobile = ApproverMobile

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def OrganizationOpenId(self):
        return self._OrganizationOpenId

    @OrganizationOpenId.setter
    def OrganizationOpenId(self, OrganizationOpenId):
        self._OrganizationOpenId = OrganizationOpenId

    @property
    def NotChannelOrganization(self):
        return self._NotChannelOrganization

    @NotChannelOrganization.setter
    def NotChannelOrganization(self, NotChannelOrganization):
        self._NotChannelOrganization = NotChannelOrganization


    def _deserialize(self, params):
        self._RecipientId = params.get("RecipientId")
        self._OpenId = params.get("OpenId")
        self._ApproverName = params.get("ApproverName")
        self._ApproverMobile = params.get("ApproverMobile")
        self._OrganizationName = params.get("OrganizationName")
        self._OrganizationOpenId = params.get("OrganizationOpenId")
        self._NotChannelOrganization = params.get("NotChannelOrganization")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FillError(AbstractModel):
    """批量补充签署人时，补充失败的报错说明

    """

    def __init__(self):
        r"""
        :param _RecipientId: 为签署方经办人在签署合同中的参与方ID，与控件绑定，是控件的归属方，ID为32位字符串。与入参中补充的签署人角色ID对应，批量补充部分失败返回对应的错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecipientId: str
        :param _ErrMessage: 补充失败错误说明
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        """
        self._RecipientId = None
        self._ErrMessage = None

    @property
    def RecipientId(self):
        return self._RecipientId

    @RecipientId.setter
    def RecipientId(self, RecipientId):
        self._RecipientId = RecipientId

    @property
    def ErrMessage(self):
        return self._ErrMessage

    @ErrMessage.setter
    def ErrMessage(self, ErrMessage):
        self._ErrMessage = ErrMessage


    def _deserialize(self, params):
        self._RecipientId = params.get("RecipientId")
        self._ErrMessage = params.get("ErrMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilledComponent(AbstractModel):
    """文档内的填充控件返回结构体，返回控件的基本信息和填写内容值

    """

    def __init__(self):
        r"""
        :param _ComponentId: 控件Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ComponentId: str
        :param _ComponentName: 控件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ComponentName: str
        :param _ComponentFillStatus: 控件填写状态；0-未填写；1-已填写
注意：此字段可能返回 null，表示取不到有效值。
        :type ComponentFillStatus: str
        :param _ComponentValue: 控件填写内容
注意：此字段可能返回 null，表示取不到有效值。
        :type ComponentValue: str
        :param _ImageUrl: 图片填充控件下载链接，如果是图片填充控件时，这里返回图片的下载链接。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: str
        """
        self._ComponentId = None
        self._ComponentName = None
        self._ComponentFillStatus = None
        self._ComponentValue = None
        self._ImageUrl = None

    @property
    def ComponentId(self):
        return self._ComponentId

    @ComponentId.setter
    def ComponentId(self, ComponentId):
        self._ComponentId = ComponentId

    @property
    def ComponentName(self):
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def ComponentFillStatus(self):
        return self._ComponentFillStatus

    @ComponentFillStatus.setter
    def ComponentFillStatus(self, ComponentFillStatus):
        self._ComponentFillStatus = ComponentFillStatus

    @property
    def ComponentValue(self):
        return self._ComponentValue

    @ComponentValue.setter
    def ComponentValue(self, ComponentValue):
        self._ComponentValue = ComponentValue

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ComponentId = params.get("ComponentId")
        self._ComponentName = params.get("ComponentName")
        self._ComponentFillStatus = params.get("ComponentFillStatus")
        self._ComponentValue = params.get("ComponentValue")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """此结构体 (Filter) 用于描述查询过滤条件。

    """

    def __init__(self):
        r"""
        :param _Key: 查询过滤条件的Key
        :type Key: str
        :param _Values: 查询过滤条件的Value列表
        :type Values: list of str
        """
        self._Key = None
        self._Values = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowApproverDetail(AbstractModel):
    """签署人的流程信息明细

    """

    def __init__(self):
        r"""
        :param _ReceiptId: 模板配置时候的签署人id,与控件绑定
        :type ReceiptId: str
        :param _ProxyOrganizationOpenId: 平台企业的第三方id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyOrganizationOpenId: str
        :param _ProxyOperatorOpenId: 平台企业操作人的第三方id
        :type ProxyOperatorOpenId: str
        :param _ProxyOrganizationName: 平台企业名称
        :type ProxyOrganizationName: str
        :param _Mobile: 签署人手机号
        :type Mobile: str
        :param _SignOrder: 签署人签署顺序
        :type SignOrder: int
        :param _ApproveName: 签署人姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveName: str
        :param _ApproveStatus: 当前签署人的状态, 状态如下
<br/>PENDING 待签署	
<br/>FILLPENDING 待填写
<br/>FILLACCEPT 填写完成	
<br/>FILLREJECT 拒绝填写	
<br/>WAITPICKUP 待领取	
<br/>ACCEPT 已签署	
<br/>REJECT 拒签 
<br/>DEADLINE 过期没人处理 
<br/>CANCEL 流程已撤回	
<br/>FORWARD 已经转他人处理
<br/>STOP 流程已终止	
<br/>RELIEVED 解除协议（已解除）

注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveStatus: str
        :param _ApproveMessage: 签署人自定义信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveMessage: str
        :param _ApproveTime: 签署人签署时间戳，单位秒
        :type ApproveTime: int
        :param _ApproveType: 参与者类型 
<br/>ORGANIZATION：企业签署人
<br/>PERSON：个人签署人
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveType: str
        :param _ApproverRoleName: 自定义签署人角色
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproverRoleName: str
        """
        self._ReceiptId = None
        self._ProxyOrganizationOpenId = None
        self._ProxyOperatorOpenId = None
        self._ProxyOrganizationName = None
        self._Mobile = None
        self._SignOrder = None
        self._ApproveName = None
        self._ApproveStatus = None
        self._ApproveMessage = None
        self._ApproveTime = None
        self._ApproveType = None
        self._ApproverRoleName = None

    @property
    def ReceiptId(self):
        return self._ReceiptId

    @ReceiptId.setter
    def ReceiptId(self, ReceiptId):
        self._ReceiptId = ReceiptId

    @property
    def ProxyOrganizationOpenId(self):
        return self._ProxyOrganizationOpenId

    @ProxyOrganizationOpenId.setter
    def ProxyOrganizationOpenId(self, ProxyOrganizationOpenId):
        self._ProxyOrganizationOpenId = ProxyOrganizationOpenId

    @property
    def ProxyOperatorOpenId(self):
        return self._ProxyOperatorOpenId

    @ProxyOperatorOpenId.setter
    def ProxyOperatorOpenId(self, ProxyOperatorOpenId):
        self._ProxyOperatorOpenId = ProxyOperatorOpenId

    @property
    def ProxyOrganizationName(self):
        return self._ProxyOrganizationName

    @ProxyOrganizationName.setter
    def ProxyOrganizationName(self, ProxyOrganizationName):
        self._ProxyOrganizationName = ProxyOrganizationName

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def SignOrder(self):
        return self._SignOrder

    @SignOrder.setter
    def SignOrder(self, SignOrder):
        self._SignOrder = SignOrder

    @property
    def ApproveName(self):
        return self._ApproveName

    @ApproveName.setter
    def ApproveName(self, ApproveName):
        self._ApproveName = ApproveName

    @property
    def ApproveStatus(self):
        return self._ApproveStatus

    @ApproveStatus.setter
    def ApproveStatus(self, ApproveStatus):
        self._ApproveStatus = ApproveStatus

    @property
    def ApproveMessage(self):
        return self._ApproveMessage

    @ApproveMessage.setter
    def ApproveMessage(self, ApproveMessage):
        self._ApproveMessage = ApproveMessage

    @property
    def ApproveTime(self):
        return self._ApproveTime

    @ApproveTime.setter
    def ApproveTime(self, ApproveTime):
        self._ApproveTime = ApproveTime

    @property
    def ApproveType(self):
        return self._ApproveType

    @ApproveType.setter
    def ApproveType(self, ApproveType):
        self._ApproveType = ApproveType

    @property
    def ApproverRoleName(self):
        return self._ApproverRoleName

    @ApproverRoleName.setter
    def ApproverRoleName(self, ApproverRoleName):
        self._ApproverRoleName = ApproverRoleName


    def _deserialize(self, params):
        self._ReceiptId = params.get("ReceiptId")
        self._ProxyOrganizationOpenId = params.get("ProxyOrganizationOpenId")
        self._ProxyOperatorOpenId = params.get("ProxyOperatorOpenId")
        self._ProxyOrganizationName = params.get("ProxyOrganizationName")
        self._Mobile = params.get("Mobile")
        self._SignOrder = params.get("SignOrder")
        self._ApproveName = params.get("ApproveName")
        self._ApproveStatus = params.get("ApproveStatus")
        self._ApproveMessage = params.get("ApproveMessage")
        self._ApproveTime = params.get("ApproveTime")
        self._ApproveType = params.get("ApproveType")
        self._ApproverRoleName = params.get("ApproverRoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowApproverInfo(AbstractModel):
    """创建签署流程签署人入参。

    其中签署方FlowApproverInfo需要传递的参数
    非单C、单B、B2C合同，ApproverType、RecipientId（模板发起合同时）必传，建议都传。

    其他身份标识，注：`如果发起的是动态签署方（即ApproverOption.FillType指定为1），可以不指定具体签署人信息`

    <ul><li>1-个人：Name、Mobile必传</li>
    <li>2-第三方平台子客企业指定经办人：OpenId必传，OrgName必传、OrgOpenId必传；</li>
    <li>3-第三方平台子客企业不指定经办人：OrgName必传、OrgOpenId必传；</li>
    <li>4-非第三方平台子客企业(平台企业)：Name、Mobile必传，OrgName必传，且NotChannelOrganization=True。</li></ul>

    RecipientId参数：
    从DescribeTemplates接口中，可以得到模板下的签署方Recipient列表，根据模板自定义的Rolename在此结构体中确定其RecipientId。

    """

    def __init__(self):
        r"""
        :param _Name: 签署方经办人的姓名。
经办人的姓名将用于身份认证和电子签名，请确保填写的姓名为签署方的真实姓名，而非昵称等代名。
        :type Name: str
        :param _IdCardType: 签署方经办人的证件类型，支持以下类型
<ul><li>ID_CARD : 居民身份证  (默认值)</li>
<li>HONGKONG_AND_MACAO : 港澳居民来往内地通行证</li>
<li>HONGKONG_MACAO_AND_TAIWAN : 港澳台居民居住证(格式同居民身份证)</li>
<li>OTHER_CARD_TYPE : 其他证件</li></ul>

注: `其他证件类型为白名单功能，使用前请联系对接的客户经理沟通。`
        :type IdCardType: str
        :param _IdCardNumber: 签署方经办人的证件号码，应符合以下规则
<ul><li>居民身份证号码应为18位字符串，由数字和大写字母X组成（如存在X，请大写）。</li>
<li>港澳居民来往内地通行证号码应为9位字符串，第1位为“C”，第2位为英文字母（但“I”、“O”除外），后7位为阿拉伯数字。</li>
<li>港澳台居民居住证号码编码规则与中国大陆身份证相同，应为18位字符串。</li></ul>
        :type IdCardNumber: str
        :param _Mobile: 签署方经办人手机号码， 支持国内手机号11位数字(无需加+86前缀或其他字符)， 不支持海外手机号。
请确认手机号所有方为此合同签署方。
        :type Mobile: str
        :param _OrganizationName: 组织机构名称。
请确认该名称与企业营业执照中注册的名称一致。
如果名称中包含英文括号()，请使用中文括号（）代替。
        :type OrganizationName: str
        :param _NotChannelOrganization: 指定签署人非第三方平台子客企业下员工还是SaaS平台企业，在ApproverType为ORGANIZATION时指定。
<ul>
<li>false: 默认值，第三方平台子客企业下员工</li>
<li>true: SaaS平台企业下的员工</li>
</ul>

        :type NotChannelOrganization: bool
        :param _OpenId: 第三方平台子客企业员工的唯一标识，长度不能超过64，只能由字母和数字组成

当签署方为同一第三方平台下的员工时，该字段若不指定，则发起【待领取】的流程
        :type OpenId: str
        :param _OrganizationOpenId: 同应用下第三方平台子客企业的唯一标识，定义Agent中的ProxyOrganizationOpenId一样，签署方为非发起方企业场景下必传，最大长度64个字符
        :type OrganizationOpenId: str
        :param _ApproverType: 在指定签署方时，可选择企业B端或个人C端等不同的参与者类型，可选类型如下:
<ul><li> **PERSON** :个人/自然人</li>
<li> **PERSON_AUTO_SIGN** :个人/自然人自动签署，适用于个人自动签场景</li>
<li> **ORGANIZATION** :企业/企业员工（企业签署方或模板发起时的企业静默签）</li>
<li> **ENTERPRISESERVER** :企业/企业员自动签（他方企业自动签署或文件发起时的本方企业自动签）</li></ul>

注:  
`1. 个人自动签场景(PERSON_AUTO_SIGN)为白名单功能, 使用前请联系对接的客户经理沟通。`
`2. 若要实现他方企业（同一应用下）自动签，需要满足3个条件：`
<ul><li>条件1：ApproverType 设置为ENTERPRISESERVER</li>
<li>条件2：子客之间完成授权</li>
<li>条件3：联系对接的客户经理沟通如何使用</li></ul>
        :type ApproverType: str
        :param _RecipientId: 签署流程签署人在模板中对应的签署人Id；在非单方签署、以及非B2C签署的场景下必传，用于指定当前签署方在签署流程中的位置；
        :type RecipientId: str
        :param _Deadline: 本签署人在此合同流程的签署截止时间，格式为Unix标准时间戳（秒），如果未设置签署截止时间，则默认为合同流程创建后的365天时截止。
如果在签署截止时间前未完成签署，则合同状态会变为已过期，导致合同作废。
        :type Deadline: int
        :param _CallbackUrl: 签署完回调url，最大长度1000个字符
        :type CallbackUrl: str
        :param _SignComponents: 使用PDF文件直接发起合同时，签署人指定的签署控件；<br/>使用模板发起合同时，指定本企业印章签署控件的印章ID: <br/>通过ComponentId或ComponenetName指定签署控件，ComponentValue为印章ID。
        :type SignComponents: list of Component
        :param _ComponentLimitType: 签署方控件类型为 SIGN_SIGNATURE时，可以指定签署方签名方式
	HANDWRITE – 手写签名
	OCR_ESIGN -- AI智能识别手写签名
	ESIGN -- 个人印章类型
	SYSTEM_ESIGN -- 系统签名（该类型可以在用户签署时根据用户姓名一键生成一个签名来进行签署）
        :type ComponentLimitType: list of str
        :param _PreReadTime: 签署方在签署合同之前，需要强制阅读合同的时长，可指定为3秒至300秒之间的任意值。

若未指定阅读时间，则会按照合同页数大小计算阅读时间，计算规则如下：
<ul>
<li>合同页数少于等于2页，阅读时间为3秒；</li>
<li>合同页数为3到5页，阅读时间为5秒；</li>
<li>合同页数大于等于6页，阅读时间为10秒。</li>
</ul>
        :type PreReadTime: int
        :param _JumpUrl: 签署完前端跳转的url，此字段的用法场景请联系客户经理确认
        :type JumpUrl: str
        :param _ApproverOption: 可以控制签署方在签署合同时能否进行某些操作，例如拒签、转交他人等。
详细操作可以参考开发者中心的ApproverOption结构体。
        :type ApproverOption: :class:`tencentcloud.essbasic.v20210526.models.ApproverOption`
        :param _ApproverNeedSignReview: 当前签署方进行签署操作是否需要企业内部审批，true 则为需要
        :type ApproverNeedSignReview: bool
        :param _ApproverVerifyTypes: 签署人查看合同时认证方式, 1-实名查看 2-短信验证码查看(企业签署方不支持该方式) 如果不传默认为1
查看合同的认证方式 Flow层级的优先于approver层级的
（当手写签名方式为OCR_ESIGN时，合同认证方式2无效，因为这种签名方式依赖实名认证）
        :type ApproverVerifyTypes: list of int
        :param _ApproverSignTypes: 签署人签署合同时的认证方式
1-人脸认证 2-签署密码 3-运营商三要素(默认为1,2)
        :type ApproverSignTypes: list of int
        :param _SignId: 签署ID
- 发起流程时系统自动补充
- 创建签署链接时，可以通过查询详情接口获得签署人的SignId，然后可传入此值为该签署人创建签署链接，无需再传姓名、手机号、证件号等其他信息
        :type SignId: str
        :param _NotifyType: 通知签署方经办人的方式, 有以下途径:
<ul><li> **SMS** :(默认)短信</li>
<li> **NONE** : 不通知</li></ul>

注: `签署方为第三方子客企业时会被置为NONE,   不会发短信通知`
        :type NotifyType: str
        :param _AddSignComponentsLimits: [通过文件创建签署流程](https://qian.tencent.com/developers/partnerApis/startFlows/ChannelCreateFlowByFiles)时,如果设置了外层参数SignBeanTag=1(允许签署过程中添加签署控件),则可通过此参数明确规定合同所使用的签署控件类型（骑缝章、普通章法人章等）和具体的印章（印章ID）或签名方式。

注：`限制印章控件或骑缝章控件情况下,仅本企业签署方可以指定具体印章（通过传递ComponentValue,支持多个），他方企业或个人只支持限制控件类型。`
        :type AddSignComponentsLimits: list of ComponentLimit
        :param _ApproverRoleName: 自定义签署人角色名，如收款人、开具人、见证人等
        :type ApproverRoleName: str
        """
        self._Name = None
        self._IdCardType = None
        self._IdCardNumber = None
        self._Mobile = None
        self._OrganizationName = None
        self._NotChannelOrganization = None
        self._OpenId = None
        self._OrganizationOpenId = None
        self._ApproverType = None
        self._RecipientId = None
        self._Deadline = None
        self._CallbackUrl = None
        self._SignComponents = None
        self._ComponentLimitType = None
        self._PreReadTime = None
        self._JumpUrl = None
        self._ApproverOption = None
        self._ApproverNeedSignReview = None
        self._ApproverVerifyTypes = None
        self._ApproverSignTypes = None
        self._SignId = None
        self._NotifyType = None
        self._AddSignComponentsLimits = None
        self._ApproverRoleName = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCardType(self):
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def IdCardNumber(self):
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def NotChannelOrganization(self):
        return self._NotChannelOrganization

    @NotChannelOrganization.setter
    def NotChannelOrganization(self, NotChannelOrganization):
        self._NotChannelOrganization = NotChannelOrganization

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def OrganizationOpenId(self):
        return self._OrganizationOpenId

    @OrganizationOpenId.setter
    def OrganizationOpenId(self, OrganizationOpenId):
        self._OrganizationOpenId = OrganizationOpenId

    @property
    def ApproverType(self):
        return self._ApproverType

    @ApproverType.setter
    def ApproverType(self, ApproverType):
        self._ApproverType = ApproverType

    @property
    def RecipientId(self):
        return self._RecipientId

    @RecipientId.setter
    def RecipientId(self, RecipientId):
        self._RecipientId = RecipientId

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def CallbackUrl(self):
        warnings.warn("parameter `CallbackUrl` is deprecated", DeprecationWarning) 

        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        warnings.warn("parameter `CallbackUrl` is deprecated", DeprecationWarning) 

        self._CallbackUrl = CallbackUrl

    @property
    def SignComponents(self):
        return self._SignComponents

    @SignComponents.setter
    def SignComponents(self, SignComponents):
        self._SignComponents = SignComponents

    @property
    def ComponentLimitType(self):
        return self._ComponentLimitType

    @ComponentLimitType.setter
    def ComponentLimitType(self, ComponentLimitType):
        self._ComponentLimitType = ComponentLimitType

    @property
    def PreReadTime(self):
        return self._PreReadTime

    @PreReadTime.setter
    def PreReadTime(self, PreReadTime):
        self._PreReadTime = PreReadTime

    @property
    def JumpUrl(self):
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl

    @property
    def ApproverOption(self):
        return self._ApproverOption

    @ApproverOption.setter
    def ApproverOption(self, ApproverOption):
        self._ApproverOption = ApproverOption

    @property
    def ApproverNeedSignReview(self):
        return self._ApproverNeedSignReview

    @ApproverNeedSignReview.setter
    def ApproverNeedSignReview(self, ApproverNeedSignReview):
        self._ApproverNeedSignReview = ApproverNeedSignReview

    @property
    def ApproverVerifyTypes(self):
        return self._ApproverVerifyTypes

    @ApproverVerifyTypes.setter
    def ApproverVerifyTypes(self, ApproverVerifyTypes):
        self._ApproverVerifyTypes = ApproverVerifyTypes

    @property
    def ApproverSignTypes(self):
        return self._ApproverSignTypes

    @ApproverSignTypes.setter
    def ApproverSignTypes(self, ApproverSignTypes):
        self._ApproverSignTypes = ApproverSignTypes

    @property
    def SignId(self):
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def NotifyType(self):
        return self._NotifyType

    @NotifyType.setter
    def NotifyType(self, NotifyType):
        self._NotifyType = NotifyType

    @property
    def AddSignComponentsLimits(self):
        return self._AddSignComponentsLimits

    @AddSignComponentsLimits.setter
    def AddSignComponentsLimits(self, AddSignComponentsLimits):
        self._AddSignComponentsLimits = AddSignComponentsLimits

    @property
    def ApproverRoleName(self):
        return self._ApproverRoleName

    @ApproverRoleName.setter
    def ApproverRoleName(self, ApproverRoleName):
        self._ApproverRoleName = ApproverRoleName


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
        self._Mobile = params.get("Mobile")
        self._OrganizationName = params.get("OrganizationName")
        self._NotChannelOrganization = params.get("NotChannelOrganization")
        self._OpenId = params.get("OpenId")
        self._OrganizationOpenId = params.get("OrganizationOpenId")
        self._ApproverType = params.get("ApproverType")
        self._RecipientId = params.get("RecipientId")
        self._Deadline = params.get("Deadline")
        self._CallbackUrl = params.get("CallbackUrl")
        if params.get("SignComponents") is not None:
            self._SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self._SignComponents.append(obj)
        self._ComponentLimitType = params.get("ComponentLimitType")
        self._PreReadTime = params.get("PreReadTime")
        self._JumpUrl = params.get("JumpUrl")
        if params.get("ApproverOption") is not None:
            self._ApproverOption = ApproverOption()
            self._ApproverOption._deserialize(params.get("ApproverOption"))
        self._ApproverNeedSignReview = params.get("ApproverNeedSignReview")
        self._ApproverVerifyTypes = params.get("ApproverVerifyTypes")
        self._ApproverSignTypes = params.get("ApproverSignTypes")
        self._SignId = params.get("SignId")
        self._NotifyType = params.get("NotifyType")
        if params.get("AddSignComponentsLimits") is not None:
            self._AddSignComponentsLimits = []
            for item in params.get("AddSignComponentsLimits"):
                obj = ComponentLimit()
                obj._deserialize(item)
                self._AddSignComponentsLimits.append(obj)
        self._ApproverRoleName = params.get("ApproverRoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowApproverItem(AbstractModel):
    """签署方信息，如角色ID、角色名称等

    """

    def __init__(self):
        r"""
        :param _FlowId: 合同编号
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: str
        :param _Approvers: 签署方信息，如角色ID、角色名称等
注意：此字段可能返回 null，表示取不到有效值。
        :type Approvers: list of ApproverItem
        """
        self._FlowId = None
        self._Approvers = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Approvers(self):
        return self._Approvers

    @Approvers.setter
    def Approvers(self, Approvers):
        self._Approvers = Approvers


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("Approvers") is not None:
            self._Approvers = []
            for item in params.get("Approvers"):
                obj = ApproverItem()
                obj._deserialize(item)
                self._Approvers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowApproverUrlInfo(AbstractModel):
    """签署人签署链接信息

    """

    def __init__(self):
        r"""
        :param _SignUrl: 签署短链接，不支持小程序嵌入，只支持移动端浏览器打开。注意该链接有效期为30分钟，同时需要注意保密，不要外泄给无关用户。
        :type SignUrl: str
        :param _ApproverType: 签署人类型 PERSON-个人
        :type ApproverType: str
        :param _Name: 签署人姓名
        :type Name: str
        :param _Mobile: 签署人手机号
        :type Mobile: str
        :param _LongUrl: 签署长链接，支持小程序嵌入。注意该链接有效期为30分钟，同时需要注意保密，不要外泄给无关用户。
注意：此字段可能返回 null，表示取不到有效值。
        :type LongUrl: str
        """
        self._SignUrl = None
        self._ApproverType = None
        self._Name = None
        self._Mobile = None
        self._LongUrl = None

    @property
    def SignUrl(self):
        return self._SignUrl

    @SignUrl.setter
    def SignUrl(self, SignUrl):
        self._SignUrl = SignUrl

    @property
    def ApproverType(self):
        return self._ApproverType

    @ApproverType.setter
    def ApproverType(self, ApproverType):
        self._ApproverType = ApproverType

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def LongUrl(self):
        return self._LongUrl

    @LongUrl.setter
    def LongUrl(self, LongUrl):
        self._LongUrl = LongUrl


    def _deserialize(self, params):
        self._SignUrl = params.get("SignUrl")
        self._ApproverType = params.get("ApproverType")
        self._Name = params.get("Name")
        self._Mobile = params.get("Mobile")
        self._LongUrl = params.get("LongUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowDetailInfo(AbstractModel):
    """此结构体(FlowDetailInfo)描述的是合同(流程)的详细信息

    """

    def __init__(self):
        r"""
        :param _FlowId: 合同(流程)的Id
        :type FlowId: str
        :param _FlowName: 合同(流程)的名字
        :type FlowName: str
        :param _FlowType: 合同(流程)的类型
        :type FlowType: str
        :param _FlowStatus: 合同(流程)的状态, 状态如下

INIT 合同创建
PART 合同签署中
REJECT 合同拒签
ALL 合同签署完成
DEADLINE 合同流签(合同过期)
CANCEL 合同撤回
RELIEVED 解除协议（已解除）
 
        :type FlowStatus: str
        :param _FlowMessage: 合同(流程)的信息
        :type FlowMessage: str
        :param _CreateOn: 合同(流程)的创建时间戳，单位秒
        :type CreateOn: int
        :param _DeadLine: 合同(流程)的签署截止时间戳，单位秒
        :type DeadLine: int
        :param _CustomData: 用户自定义数据
        :type CustomData: str
        :param _FlowApproverInfos: 合同(流程)的签署人数组
        :type FlowApproverInfos: list of FlowApproverDetail
        :param _CcInfos: 合同(流程)关注方信息列表
        :type CcInfos: list of FlowApproverDetail
        :param _NeedCreateReview: 是否需要发起前审批，当NeedCreateReview为true，表明当前流程是需要发起前审核的合同，可能无法进行查看，签署操作，需要等审核完成后，才可以继续后续流程
        :type NeedCreateReview: bool
        """
        self._FlowId = None
        self._FlowName = None
        self._FlowType = None
        self._FlowStatus = None
        self._FlowMessage = None
        self._CreateOn = None
        self._DeadLine = None
        self._CustomData = None
        self._FlowApproverInfos = None
        self._CcInfos = None
        self._NeedCreateReview = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowType(self):
        return self._FlowType

    @FlowType.setter
    def FlowType(self, FlowType):
        self._FlowType = FlowType

    @property
    def FlowStatus(self):
        return self._FlowStatus

    @FlowStatus.setter
    def FlowStatus(self, FlowStatus):
        self._FlowStatus = FlowStatus

    @property
    def FlowMessage(self):
        return self._FlowMessage

    @FlowMessage.setter
    def FlowMessage(self, FlowMessage):
        self._FlowMessage = FlowMessage

    @property
    def CreateOn(self):
        return self._CreateOn

    @CreateOn.setter
    def CreateOn(self, CreateOn):
        self._CreateOn = CreateOn

    @property
    def DeadLine(self):
        return self._DeadLine

    @DeadLine.setter
    def DeadLine(self, DeadLine):
        self._DeadLine = DeadLine

    @property
    def CustomData(self):
        return self._CustomData

    @CustomData.setter
    def CustomData(self, CustomData):
        self._CustomData = CustomData

    @property
    def FlowApproverInfos(self):
        return self._FlowApproverInfos

    @FlowApproverInfos.setter
    def FlowApproverInfos(self, FlowApproverInfos):
        self._FlowApproverInfos = FlowApproverInfos

    @property
    def CcInfos(self):
        return self._CcInfos

    @CcInfos.setter
    def CcInfos(self, CcInfos):
        self._CcInfos = CcInfos

    @property
    def NeedCreateReview(self):
        return self._NeedCreateReview

    @NeedCreateReview.setter
    def NeedCreateReview(self, NeedCreateReview):
        self._NeedCreateReview = NeedCreateReview


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._FlowName = params.get("FlowName")
        self._FlowType = params.get("FlowType")
        self._FlowStatus = params.get("FlowStatus")
        self._FlowMessage = params.get("FlowMessage")
        self._CreateOn = params.get("CreateOn")
        self._DeadLine = params.get("DeadLine")
        self._CustomData = params.get("CustomData")
        if params.get("FlowApproverInfos") is not None:
            self._FlowApproverInfos = []
            for item in params.get("FlowApproverInfos"):
                obj = FlowApproverDetail()
                obj._deserialize(item)
                self._FlowApproverInfos.append(obj)
        if params.get("CcInfos") is not None:
            self._CcInfos = []
            for item in params.get("CcInfos"):
                obj = FlowApproverDetail()
                obj._deserialize(item)
                self._CcInfos.append(obj)
        self._NeedCreateReview = params.get("NeedCreateReview")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowFileInfo(AbstractModel):
    """合同组中每个子合同的发起信息

    """

    def __init__(self):
        r"""
        :param _FileIds: 签署文件资源Id列表，目前仅支持单个文件
        :type FileIds: list of str
        :param _FlowName: 签署流程名称，长度不超过200个字符
        :type FlowName: str
        :param _FlowApprovers: 签署流程签约方列表，最多不超过5个参与方
        :type FlowApprovers: list of FlowApproverInfo
        :param _Deadline: 签署流程截止时间，十位数时间戳，最大值为33162419560，即3020年
        :type Deadline: int
        :param _FlowDescription: 签署流程的描述，长度不超过1000个字符
        :type FlowDescription: str
        :param _FlowType: 签署流程的类型，长度不超过255个字符
        :type FlowType: str
        :param _CallbackUrl: 签署流程回调地址，长度不超过255个字符
        :type CallbackUrl: str
        :param _CustomerData: 第三方应用的业务信息，最大长度1000个字符。发起自动签署时，需设置对应自动签署场景，目前仅支持场景：处方单-E_PRESCRIPTION_AUTO_SIGN
        :type CustomerData: str
        :param _Unordered: 合同签署顺序类型(无序签,顺序签)，默认为false，即有序签署
        :type Unordered: bool
        :param _Components: 签署文件中的发起方的填写控件，需要在发起的时候进行填充
        :type Components: list of Component
        :param _CustomShowMap: 合同显示的页卡模板，说明：只支持{合同名称}, {发起方企业}, {发起方姓名}, {签署方N企业}, {签署方N姓名}，且N不能超过签署人的数量，N从1开始
        :type CustomShowMap: str
        :param _NeedSignReview: 本企业(发起方企业)是否需要签署审批
        :type NeedSignReview: bool
        """
        self._FileIds = None
        self._FlowName = None
        self._FlowApprovers = None
        self._Deadline = None
        self._FlowDescription = None
        self._FlowType = None
        self._CallbackUrl = None
        self._CustomerData = None
        self._Unordered = None
        self._Components = None
        self._CustomShowMap = None
        self._NeedSignReview = None

    @property
    def FileIds(self):
        return self._FileIds

    @FileIds.setter
    def FileIds(self, FileIds):
        self._FileIds = FileIds

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowApprovers(self):
        return self._FlowApprovers

    @FlowApprovers.setter
    def FlowApprovers(self, FlowApprovers):
        self._FlowApprovers = FlowApprovers

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def FlowDescription(self):
        return self._FlowDescription

    @FlowDescription.setter
    def FlowDescription(self, FlowDescription):
        self._FlowDescription = FlowDescription

    @property
    def FlowType(self):
        return self._FlowType

    @FlowType.setter
    def FlowType(self, FlowType):
        self._FlowType = FlowType

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def CustomerData(self):
        return self._CustomerData

    @CustomerData.setter
    def CustomerData(self, CustomerData):
        self._CustomerData = CustomerData

    @property
    def Unordered(self):
        return self._Unordered

    @Unordered.setter
    def Unordered(self, Unordered):
        self._Unordered = Unordered

    @property
    def Components(self):
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def CustomShowMap(self):
        return self._CustomShowMap

    @CustomShowMap.setter
    def CustomShowMap(self, CustomShowMap):
        self._CustomShowMap = CustomShowMap

    @property
    def NeedSignReview(self):
        return self._NeedSignReview

    @NeedSignReview.setter
    def NeedSignReview(self, NeedSignReview):
        self._NeedSignReview = NeedSignReview


    def _deserialize(self, params):
        self._FileIds = params.get("FileIds")
        self._FlowName = params.get("FlowName")
        if params.get("FlowApprovers") is not None:
            self._FlowApprovers = []
            for item in params.get("FlowApprovers"):
                obj = FlowApproverInfo()
                obj._deserialize(item)
                self._FlowApprovers.append(obj)
        self._Deadline = params.get("Deadline")
        self._FlowDescription = params.get("FlowDescription")
        self._FlowType = params.get("FlowType")
        self._CallbackUrl = params.get("CallbackUrl")
        self._CustomerData = params.get("CustomerData")
        self._Unordered = params.get("Unordered")
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self._Components.append(obj)
        self._CustomShowMap = params.get("CustomShowMap")
        self._NeedSignReview = params.get("NeedSignReview")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowGroupOptions(AbstractModel):
    """合同组的配置项信息包括：在合同组签署过程中，是否需要对每个子合同进行独立的意愿确认。

    """

    def __init__(self):
        r"""
        :param _SelfOrganizationApproverSignEach: 发起方企业经办人（即签署人为发起方企业员工）是否需要对子合同进行独立的意愿确认：
fasle：发起方企业经办人签署时对所有子合同进行统一的意愿确认
true：发起方企业经办人签署时需要对子合同进行独立的意愿确认
默认为fasle。
        :type SelfOrganizationApproverSignEach: bool
        :param _OtherApproverSignEach: 非发起方企业经办人（即：签署人为个人或者不为发起方企业的员工）是否需要对子合同进行独立的意愿确认：
fasle：非发起方企业经办人签署时对所有子合同进行统一的意愿确认
true：非发起方企业经办人签署时需要对子合同进行独立的意愿确认
默认为false。
        :type OtherApproverSignEach: bool
        """
        self._SelfOrganizationApproverSignEach = None
        self._OtherApproverSignEach = None

    @property
    def SelfOrganizationApproverSignEach(self):
        return self._SelfOrganizationApproverSignEach

    @SelfOrganizationApproverSignEach.setter
    def SelfOrganizationApproverSignEach(self, SelfOrganizationApproverSignEach):
        self._SelfOrganizationApproverSignEach = SelfOrganizationApproverSignEach

    @property
    def OtherApproverSignEach(self):
        return self._OtherApproverSignEach

    @OtherApproverSignEach.setter
    def OtherApproverSignEach(self, OtherApproverSignEach):
        self._OtherApproverSignEach = OtherApproverSignEach


    def _deserialize(self, params):
        self._SelfOrganizationApproverSignEach = params.get("SelfOrganizationApproverSignEach")
        self._OtherApproverSignEach = params.get("OtherApproverSignEach")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowInfo(AbstractModel):
    """此结构体 (FlowInfo) 用于描述签署流程信息。

    【数据表格传参说明】
    当模板的 ComponentType='DYNAMIC_TABLE'时（ 第三方应用集成或集成版），FormField.ComponentValue需要传递json格式的字符串参数，用于确定表头&填充数据表格（支持内容的单元格合并）
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
        :param _FlowName: 合同名字，最大长度200个字符
        :type FlowName: str
        :param _Deadline: 签署截止时间戳，超过有效签署时间则该签署流程失败，默认一年
        :type Deadline: int
        :param _TemplateId: 模板ID
        :type TemplateId: str
        :param _FlowApprovers: 多个签署人信息，最大支持50个签署方
        :type FlowApprovers: list of FlowApproverInfo
        :param _FormFields: 表单K-V对列表
        :type FormFields: list of FormField
        :param _CallbackUrl: 回调地址，最大长度1000个字符
        :type CallbackUrl: str
        :param _FlowType: 合同类型，如：1. “劳务”；2. “销售”；3. “租赁”；4. “其他”，最大长度200个字符
        :type FlowType: str
        :param _FlowDescription: 合同描述，最大长度1000个字符
        :type FlowDescription: str
        :param _CustomerData:  第三方应用平台的业务信息，最大长度1000个字符。
        :type CustomerData: str
        :param _CustomShowMap: 合同显示的页卡模板，说明：只支持{合同名称}, {发起方企业}, {发起方姓名}, {签署方N企业}, {签署方N姓名}，且N不能超过签署人的数量，N从1开始
        :type CustomShowMap: str
        :param _CcInfos: 被抄送人的信息列表，抄送功能暂不开放
        :type CcInfos: list of CcInfo
        :param _NeedSignReview: 发起方企业的签署人进行签署操作是否需要企业内部审批。
若设置为true,审核结果需通过接口 ChannelCreateFlowSignReview 通知电子签，审核通过后，发起方企业签署人方可进行签署操作，否则会阻塞其签署操作。

注：企业可以通过此功能与企业内部的审批流程进行关联，支持手动、静默签署合同。
        :type NeedSignReview: bool
        :param _CcNotifyType: 给关注人发送短信通知的类型，0-合同发起时通知 1-签署完成后通知
        :type CcNotifyType: int
        :param _AutoSignScene: 个人自动签场景。发起自动签署时，需设置对应自动签署场景，目前仅支持场景：处方单-E_PRESCRIPTION_AUTO_SIGN
        :type AutoSignScene: str
        """
        self._FlowName = None
        self._Deadline = None
        self._TemplateId = None
        self._FlowApprovers = None
        self._FormFields = None
        self._CallbackUrl = None
        self._FlowType = None
        self._FlowDescription = None
        self._CustomerData = None
        self._CustomShowMap = None
        self._CcInfos = None
        self._NeedSignReview = None
        self._CcNotifyType = None
        self._AutoSignScene = None

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def FlowApprovers(self):
        return self._FlowApprovers

    @FlowApprovers.setter
    def FlowApprovers(self, FlowApprovers):
        self._FlowApprovers = FlowApprovers

    @property
    def FormFields(self):
        return self._FormFields

    @FormFields.setter
    def FormFields(self, FormFields):
        self._FormFields = FormFields

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def FlowType(self):
        return self._FlowType

    @FlowType.setter
    def FlowType(self, FlowType):
        self._FlowType = FlowType

    @property
    def FlowDescription(self):
        return self._FlowDescription

    @FlowDescription.setter
    def FlowDescription(self, FlowDescription):
        self._FlowDescription = FlowDescription

    @property
    def CustomerData(self):
        return self._CustomerData

    @CustomerData.setter
    def CustomerData(self, CustomerData):
        self._CustomerData = CustomerData

    @property
    def CustomShowMap(self):
        return self._CustomShowMap

    @CustomShowMap.setter
    def CustomShowMap(self, CustomShowMap):
        self._CustomShowMap = CustomShowMap

    @property
    def CcInfos(self):
        return self._CcInfos

    @CcInfos.setter
    def CcInfos(self, CcInfos):
        self._CcInfos = CcInfos

    @property
    def NeedSignReview(self):
        return self._NeedSignReview

    @NeedSignReview.setter
    def NeedSignReview(self, NeedSignReview):
        self._NeedSignReview = NeedSignReview

    @property
    def CcNotifyType(self):
        return self._CcNotifyType

    @CcNotifyType.setter
    def CcNotifyType(self, CcNotifyType):
        self._CcNotifyType = CcNotifyType

    @property
    def AutoSignScene(self):
        return self._AutoSignScene

    @AutoSignScene.setter
    def AutoSignScene(self, AutoSignScene):
        self._AutoSignScene = AutoSignScene


    def _deserialize(self, params):
        self._FlowName = params.get("FlowName")
        self._Deadline = params.get("Deadline")
        self._TemplateId = params.get("TemplateId")
        if params.get("FlowApprovers") is not None:
            self._FlowApprovers = []
            for item in params.get("FlowApprovers"):
                obj = FlowApproverInfo()
                obj._deserialize(item)
                self._FlowApprovers.append(obj)
        if params.get("FormFields") is not None:
            self._FormFields = []
            for item in params.get("FormFields"):
                obj = FormField()
                obj._deserialize(item)
                self._FormFields.append(obj)
        self._CallbackUrl = params.get("CallbackUrl")
        self._FlowType = params.get("FlowType")
        self._FlowDescription = params.get("FlowDescription")
        self._CustomerData = params.get("CustomerData")
        self._CustomShowMap = params.get("CustomShowMap")
        if params.get("CcInfos") is not None:
            self._CcInfos = []
            for item in params.get("CcInfos"):
                obj = CcInfo()
                obj._deserialize(item)
                self._CcInfos.append(obj)
        self._NeedSignReview = params.get("NeedSignReview")
        self._CcNotifyType = params.get("CcNotifyType")
        self._AutoSignScene = params.get("AutoSignScene")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowResourceUrlInfo(AbstractModel):
    """流程对应资源链接信息

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程对应Id
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: str
        :param _ResourceUrlInfos: 流程对应资源链接信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceUrlInfos: list of ResourceUrlInfo
        """
        self._FlowId = None
        self._ResourceUrlInfos = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ResourceUrlInfos(self):
        return self._ResourceUrlInfos

    @ResourceUrlInfos.setter
    def ResourceUrlInfos(self, ResourceUrlInfos):
        self._ResourceUrlInfos = ResourceUrlInfos


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("ResourceUrlInfos") is not None:
            self._ResourceUrlInfos = []
            for item in params.get("ResourceUrlInfos"):
                obj = ResourceUrlInfo()
                obj._deserialize(item)
                self._ResourceUrlInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FormField(AbstractModel):
    """电子文档的控件填充信息。按照控件类型进行相应的填充。

    当控件的 ComponentType='TEXT'时，FormField.ComponentValue填入文本内容
    ```
    FormField输入示例：
    {
        "ComponentId": "componentId1",
        "ComponentValue": "文本内容"
    }
    ```
    当控件的 ComponentType='MULTI_LINE_TEXT'时，FormField.ComponentValue填入文本内容，支持自动换行。
    ```
    FormField输入示例：
    {
        "ComponentId": "componentId1",
        "ComponentValue": "多行文本内容"
    }
    ```
    当控件的 ComponentType='CHECK_BOX'时，FormField.ComponentValue填入true或false文本
    ```
    FormField输入示例：
    {
        "ComponentId": "componentId1",
        "ComponentValue": "true"
    }
    ```
    当控件的 ComponentType='FILL_IMAGE'时，FormField.ComponentValue填入图片的资源ID
    ```
    FormField输入示例：
    {
        "ComponentId": "componentId1",
        "ComponentValue": "yDwhsxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
    ```
    当控件的 ComponentType='ATTACHMENT'时，FormField.ComponentValue填入附件图片的资源ID列表，以逗号分隔，单个附件控件最多支持6个资源ID；
    ```
    FormField输入示例：
    {
        "ComponentId": "componentId1",
        "ComponentValue": "yDwhsxxxxxxxxxxxxxxxxxxxxxxxxxx1,yDwhsxxxxxxxxxxxxxxxxxxxxxxxxxx2,yDwhsxxxxxxxxxxxxxxxxxxxxxxxxxx3"
    }
    ```
    当控件的 ComponentType='SELECTOR'时，FormField.ComponentValue填入选择的选项内容；
    ```
    FormField输入示例：
    {
        "ComponentId": "componentId1",
        "ComponentValue": "选择的内容"
    }
    ```
    当控件的 ComponentType='DATE'时，FormField.ComponentValue填入日期内容；
    ```
    FormField输入示例：
    {
        "ComponentId": "componentId1",
        "ComponentValue": "2023年01月01日"
    }
    ```
    当控件的 ComponentType='DISTRICT'时，FormField.ComponentValue填入省市区内容；
    ```
    FormField输入示例：
    {
        "ComponentId": "componentId1",
        "ComponentValue": "广东省深圳市福田区"
    }
    ```
    【数据表格传参说明】
    当控件的 ComponentType='DYNAMIC_TABLE'时，FormField.ComponentValue需要传递json格式的字符串参数，用于确定表头&填充数据表格（支持内容的单元格合并）
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
    widthPercent Integer 表头单元格列占总表头的比例，例如1：30表示 此列占表头的30%，不填写时列宽度平均拆分；例如2：总2列，某一列填写40，剩余列可以为空，按照60计算。；例如3：总3列，某一列填写30，剩余2列可以为空，分别为(100-30)/2=35
    content String 表头单元格内容，字数不超过100

    """

    def __init__(self):
        r"""
        :param _ComponentValue: 控件填充值，ComponentType和传入值格式对应关系如下：
<ul>
<li>TEXT - 普通文本控件，需输入文本字符串；</li>
<li>MULTI_LINE_TEXT - 多行文本控件，需输入文本字符串；</li>
<li>CHECK_BOX - 勾选框控件，若选中需填写ComponentValue，填写 true或者 false 字符串；</li>
<li>FILL_IMAGE - 图片控件，需填写ComponentValue为图片的资源 ID；</li>
<li>DYNAMIC_TABLE - 动态表格控件；</li>
<li>ATTACHMENT - 附件控件，需填写ComponentValue为附件图片的资源 ID列表，以逗号分割；</li>
<li>DATE - 日期控件；格式为 <b>xxxx年xx月xx日</b> 字符串；</li>
<li>DISTRICT - 省市区行政区控件，需填写ComponentValue为省市区行政区字符串内容；</li>
</ul>

        :type ComponentValue: str
        :param _ComponentId: 表单域或控件的ID，跟ComponentName二选一，不能全为空；
CreateFlowsByTemplates 接口不使用此字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type ComponentId: str
        :param _ComponentName: 控件的名字，跟ComponentId二选一，不能全为空
注意：此字段可能返回 null，表示取不到有效值。
        :type ComponentName: str
        :param _LockComponentValue: 是否锁定模板控件值，锁定后无法修改（用于嵌入式发起合同），true-锁定，false-不锁定
注意：此字段可能返回 null，表示取不到有效值。
        :type LockComponentValue: bool
        """
        self._ComponentValue = None
        self._ComponentId = None
        self._ComponentName = None
        self._LockComponentValue = None

    @property
    def ComponentValue(self):
        return self._ComponentValue

    @ComponentValue.setter
    def ComponentValue(self, ComponentValue):
        self._ComponentValue = ComponentValue

    @property
    def ComponentId(self):
        return self._ComponentId

    @ComponentId.setter
    def ComponentId(self, ComponentId):
        self._ComponentId = ComponentId

    @property
    def ComponentName(self):
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def LockComponentValue(self):
        return self._LockComponentValue

    @LockComponentValue.setter
    def LockComponentValue(self, LockComponentValue):
        self._LockComponentValue = LockComponentValue


    def _deserialize(self, params):
        self._ComponentValue = params.get("ComponentValue")
        self._ComponentId = params.get("ComponentId")
        self._ComponentName = params.get("ComponentName")
        self._LockComponentValue = params.get("LockComponentValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDownloadFlowUrlRequest(AbstractModel):
    """GetDownloadFlowUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _DownLoadFlows: 文件夹数组，签署流程总数不能超过50个，一个文件夹下，不能超过20个签署流程
        :type DownLoadFlows: list of DownloadFlowInfo
        :param _Operator: 操作者的信息，不用传
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._DownLoadFlows = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def DownLoadFlows(self):
        return self._DownLoadFlows

    @DownLoadFlows.setter
    def DownLoadFlows(self, DownLoadFlows):
        self._DownLoadFlows = DownLoadFlows

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("DownLoadFlows") is not None:
            self._DownLoadFlows = []
            for item in params.get("DownLoadFlows"):
                obj = DownloadFlowInfo()
                obj._deserialize(item)
                self._DownLoadFlows.append(obj)
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDownloadFlowUrlResponse(AbstractModel):
    """GetDownloadFlowUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownLoadUrl: 合同（流程）下载地址
        :type DownLoadUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownLoadUrl = None
        self._RequestId = None

    @property
    def DownLoadUrl(self):
        return self._DownLoadUrl

    @DownLoadUrl.setter
    def DownLoadUrl(self, DownLoadUrl):
        self._DownLoadUrl = DownLoadUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownLoadUrl = params.get("DownLoadUrl")
        self._RequestId = params.get("RequestId")


class ModifyExtendedServiceRequest(AbstractModel):
    """ModifyExtendedService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。

注: 此接口 参数Agent. ProxyOperator.OpenId 需要传递超管或者法人的OpenId
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _ServiceType:   扩展服务类型
<ul>
  <li>AUTO_SIGN             企业自动签（自动签署）</li>
<li>  OVERSEA_SIGN          企业与港澳台居民*签署合同</li>
<li>  MOBILE_CHECK_APPROVER 使用手机号验证签署方身份</li>
 <li> PAGING_SEAL           骑缝章</li>
 <li> DOWNLOAD_FLOW         授权渠道下载合同 </li>
<li>AGE_LIMIT_EXPANSION 拓宽签署方年龄限制</li>
</ul>
        :type ServiceType: str
        :param _Operate: 操作类型 
OPEN:开通 
CLOSE:关闭
        :type Operate: str
        :param _Endpoint: 链接跳转类型，支持以下类型
<ul><li>WEIXINAPP : 短链直接跳转到电子签小程序  (默认值)</li>
<li>APP : 第三方APP或小程序跳转电子签小程序</li></ul>
        :type Endpoint: str
        """
        self._Agent = None
        self._ServiceType = None
        self._Operate = None
        self._Endpoint = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def Operate(self):
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._ServiceType = params.get("ServiceType")
        self._Operate = params.get("Operate")
        self._Endpoint = params.get("Endpoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyExtendedServiceResponse(AbstractModel):
    """ModifyExtendedService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OperateUrl: 操作跳转链接，有效期24小时
若操作时没有返回跳转链接，表示无需跳转操作，此时会直接开通/关闭服务。

当操作类型是 OPEN 且 扩展服务类型是  AUTO_SIGN 或 DOWNLOAD_FLOW 或者 OVERSEA_SIGN 时返回操作链接，
返回的链接需要平台方自行触达超管或法人，超管或法人点击链接完成服务开通操作。
        :type OperateUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OperateUrl = None
        self._RequestId = None

    @property
    def OperateUrl(self):
        return self._OperateUrl

    @OperateUrl.setter
    def OperateUrl(self, OperateUrl):
        self._OperateUrl = OperateUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OperateUrl = params.get("OperateUrl")
        self._RequestId = params.get("RequestId")


class OccupiedSeal(AbstractModel):
    """持有的电子印章信息

    """

    def __init__(self):
        r"""
        :param _SealId: 电子印章编号
        :type SealId: str
        :param _SealName: 电子印章名称
        :type SealName: str
        :param _CreateOn: 电子印章授权时间戳，单位秒
        :type CreateOn: int
        :param _Creator: 电子印章授权人，电子签的UserId
        :type Creator: str
        :param _SealPolicyId: 电子印章策略Id
        :type SealPolicyId: str
        :param _SealStatus: 印章状态，有以下六种：CHECKING（审核中）SUCCESS（已启用）FAIL（审核拒绝）CHECKING-SADM（待超管审核）DISABLE（已停用）STOPPED（已终止）
        :type SealStatus: str
        :param _FailReason: 审核失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param _Url: 印章图片url，5分钟内有效
        :type Url: str
        :param _SealType: 印章类型，OFFICIAL-企业公章，CONTRACT-合同专用章，LEGAL_PERSON_SEAL-法人章
        :type SealType: str
        :param _IsAllTime: 用印申请是否为永久授权
        :type IsAllTime: bool
        :param _AuthorizedUsers: 授权人列表
        :type AuthorizedUsers: list of AuthorizedUser
        """
        self._SealId = None
        self._SealName = None
        self._CreateOn = None
        self._Creator = None
        self._SealPolicyId = None
        self._SealStatus = None
        self._FailReason = None
        self._Url = None
        self._SealType = None
        self._IsAllTime = None
        self._AuthorizedUsers = None

    @property
    def SealId(self):
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def SealName(self):
        return self._SealName

    @SealName.setter
    def SealName(self, SealName):
        self._SealName = SealName

    @property
    def CreateOn(self):
        return self._CreateOn

    @CreateOn.setter
    def CreateOn(self, CreateOn):
        self._CreateOn = CreateOn

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def SealPolicyId(self):
        return self._SealPolicyId

    @SealPolicyId.setter
    def SealPolicyId(self, SealPolicyId):
        self._SealPolicyId = SealPolicyId

    @property
    def SealStatus(self):
        return self._SealStatus

    @SealStatus.setter
    def SealStatus(self, SealStatus):
        self._SealStatus = SealStatus

    @property
    def FailReason(self):
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def SealType(self):
        return self._SealType

    @SealType.setter
    def SealType(self, SealType):
        self._SealType = SealType

    @property
    def IsAllTime(self):
        return self._IsAllTime

    @IsAllTime.setter
    def IsAllTime(self, IsAllTime):
        self._IsAllTime = IsAllTime

    @property
    def AuthorizedUsers(self):
        return self._AuthorizedUsers

    @AuthorizedUsers.setter
    def AuthorizedUsers(self, AuthorizedUsers):
        self._AuthorizedUsers = AuthorizedUsers


    def _deserialize(self, params):
        self._SealId = params.get("SealId")
        self._SealName = params.get("SealName")
        self._CreateOn = params.get("CreateOn")
        self._Creator = params.get("Creator")
        self._SealPolicyId = params.get("SealPolicyId")
        self._SealStatus = params.get("SealStatus")
        self._FailReason = params.get("FailReason")
        self._Url = params.get("Url")
        self._SealType = params.get("SealType")
        self._IsAllTime = params.get("IsAllTime")
        if params.get("AuthorizedUsers") is not None:
            self._AuthorizedUsers = []
            for item in params.get("AuthorizedUsers"):
                obj = AuthorizedUser()
                obj._deserialize(item)
                self._AuthorizedUsers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperateChannelTemplateRequest(AbstractModel):
    """OperateChannelTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 
此接口Agent.AppId必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _OperateType: 操作类型，
查询:"SELECT"，
删除:"DELETE"，
更新:"UPDATE"
        :type OperateType: str
        :param _TemplateId: 第三方应用平台模板库模板唯一标识
        :type TemplateId: str
        :param _ProxyOrganizationOpenIds: 合作企业方第三方机构唯一标识数据.
支持多个， 用","进行分隔
        :type ProxyOrganizationOpenIds: str
        :param _AuthTag: 模板可见性, 
全部可见-"all",
 部分可见-"part"
        :type AuthTag: str
        :param _Available: 当OperateType=UPDATE时，可以通过设置此字段对模板启停用状态进行操作。
若此字段值为0，则不会修改模板Available，
1为启用模板，
2为停用模板。
启用后模板可以正常领取。停用后，推送方式为【自动推送】的模板则无法被子客使用，推送方式为【手动领取】的模板则无法出现被模板库被子客领用。如果Available更新失败，会直接返回错误。
        :type Available: int
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._OperateType = None
        self._TemplateId = None
        self._ProxyOrganizationOpenIds = None
        self._AuthTag = None
        self._Available = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def OperateType(self):
        return self._OperateType

    @OperateType.setter
    def OperateType(self, OperateType):
        self._OperateType = OperateType

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def ProxyOrganizationOpenIds(self):
        return self._ProxyOrganizationOpenIds

    @ProxyOrganizationOpenIds.setter
    def ProxyOrganizationOpenIds(self, ProxyOrganizationOpenIds):
        self._ProxyOrganizationOpenIds = ProxyOrganizationOpenIds

    @property
    def AuthTag(self):
        return self._AuthTag

    @AuthTag.setter
    def AuthTag(self, AuthTag):
        self._AuthTag = AuthTag

    @property
    def Available(self):
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._OperateType = params.get("OperateType")
        self._TemplateId = params.get("TemplateId")
        self._ProxyOrganizationOpenIds = params.get("ProxyOrganizationOpenIds")
        self._AuthTag = params.get("AuthTag")
        self._Available = params.get("Available")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperateChannelTemplateResponse(AbstractModel):
    """OperateChannelTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: 腾讯电子签颁发给第三方应用平台的应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _TemplateId: 第三方应用平台模板库模板唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param _OperateResult: 描述模板可见性更改的结果，和参数中Available无关。
全部成功-"all-success",
部分成功-"part-success", 
全部失败-"fail"，失败的会在FailMessageList中展示。
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateResult: str
        :param _AuthTag: 模板可见性, 
全部可见-"all", 
部分可见-"part"
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthTag: str
        :param _ProxyOrganizationOpenIds: 合作企业方第三方机构唯一标识数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyOrganizationOpenIds: list of str
        :param _FailMessageList: 操作失败信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type FailMessageList: list of AuthFailMessage
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppId = None
        self._TemplateId = None
        self._OperateResult = None
        self._AuthTag = None
        self._ProxyOrganizationOpenIds = None
        self._FailMessageList = None
        self._RequestId = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def OperateResult(self):
        return self._OperateResult

    @OperateResult.setter
    def OperateResult(self, OperateResult):
        self._OperateResult = OperateResult

    @property
    def AuthTag(self):
        return self._AuthTag

    @AuthTag.setter
    def AuthTag(self, AuthTag):
        self._AuthTag = AuthTag

    @property
    def ProxyOrganizationOpenIds(self):
        return self._ProxyOrganizationOpenIds

    @ProxyOrganizationOpenIds.setter
    def ProxyOrganizationOpenIds(self, ProxyOrganizationOpenIds):
        self._ProxyOrganizationOpenIds = ProxyOrganizationOpenIds

    @property
    def FailMessageList(self):
        return self._FailMessageList

    @FailMessageList.setter
    def FailMessageList(self, FailMessageList):
        self._FailMessageList = FailMessageList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._TemplateId = params.get("TemplateId")
        self._OperateResult = params.get("OperateResult")
        self._AuthTag = params.get("AuthTag")
        self._ProxyOrganizationOpenIds = params.get("ProxyOrganizationOpenIds")
        if params.get("FailMessageList") is not None:
            self._FailMessageList = []
            for item in params.get("FailMessageList"):
                obj = AuthFailMessage()
                obj._deserialize(item)
                self._FailMessageList.append(obj)
        self._RequestId = params.get("RequestId")


class OrganizationInfo(AbstractModel):
    """机构信息

    """

    def __init__(self):
        r"""
        :param _OrganizationOpenId: 用户在渠道的机构编号
        :type OrganizationOpenId: str
        :param _OrganizationId: 机构在平台的编号
        :type OrganizationId: str
        :param _Channel: 用户渠道
        :type Channel: str
        :param _ClientIp: 用户真实的IP
        :type ClientIp: str
        :param _ProxyIp: 机构的代理IP
        :type ProxyIp: str
        """
        self._OrganizationOpenId = None
        self._OrganizationId = None
        self._Channel = None
        self._ClientIp = None
        self._ProxyIp = None

    @property
    def OrganizationOpenId(self):
        return self._OrganizationOpenId

    @OrganizationOpenId.setter
    def OrganizationOpenId(self, OrganizationOpenId):
        self._OrganizationOpenId = OrganizationOpenId

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def ClientIp(self):
        warnings.warn("parameter `ClientIp` is deprecated", DeprecationWarning) 

        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        warnings.warn("parameter `ClientIp` is deprecated", DeprecationWarning) 

        self._ClientIp = ClientIp

    @property
    def ProxyIp(self):
        warnings.warn("parameter `ProxyIp` is deprecated", DeprecationWarning) 

        return self._ProxyIp

    @ProxyIp.setter
    def ProxyIp(self, ProxyIp):
        warnings.warn("parameter `ProxyIp` is deprecated", DeprecationWarning) 

        self._ProxyIp = ProxyIp


    def _deserialize(self, params):
        self._OrganizationOpenId = params.get("OrganizationOpenId")
        self._OrganizationId = params.get("OrganizationId")
        self._Channel = params.get("Channel")
        self._ClientIp = params.get("ClientIp")
        self._ProxyIp = params.get("ProxyIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PdfVerifyResult(AbstractModel):
    """合同文件验签单个结果结构体

    """

    def __init__(self):
        r"""
        :param _VerifyResult: 验签结果。0-签名域未签名；1-验签成功； 3-验签失败；4-未找到签名域：文件内没有签名域；5-签名值格式不正确。
        :type VerifyResult: int
        :param _SignPlatform: 签署平台，如果文件是在腾讯电子签平台签署，则返回腾讯电子签，如果文件不在腾讯电子签平台签署，则返回其他平台。
        :type SignPlatform: str
        :param _SignerName: 签署人名称
        :type SignerName: str
        :param _SignTime: 签署时间戳，单位秒
        :type SignTime: int
        :param _SignAlgorithm: 签名算法
        :type SignAlgorithm: str
        :param _CertSn: 签名证书序列号
        :type CertSn: str
        :param _CertNotBefore: 证书起始时间戳，单位秒
        :type CertNotBefore: int
        :param _CertNotAfter: 证书过期时间戳，单位秒
        :type CertNotAfter: int
        :param _SignType: 签名类型
        :type SignType: int
        :param _ComponentPosX: 签名域横坐标，单位px
        :type ComponentPosX: float
        :param _ComponentPosY: 签名域纵坐标，单位px
        :type ComponentPosY: float
        :param _ComponentWidth: 签名域宽度，单位px
        :type ComponentWidth: float
        :param _ComponentHeight: 签名域高度，单位px
        :type ComponentHeight: float
        :param _ComponentPage: 签名域所在页码，1～N
        :type ComponentPage: int
        """
        self._VerifyResult = None
        self._SignPlatform = None
        self._SignerName = None
        self._SignTime = None
        self._SignAlgorithm = None
        self._CertSn = None
        self._CertNotBefore = None
        self._CertNotAfter = None
        self._SignType = None
        self._ComponentPosX = None
        self._ComponentPosY = None
        self._ComponentWidth = None
        self._ComponentHeight = None
        self._ComponentPage = None

    @property
    def VerifyResult(self):
        return self._VerifyResult

    @VerifyResult.setter
    def VerifyResult(self, VerifyResult):
        self._VerifyResult = VerifyResult

    @property
    def SignPlatform(self):
        return self._SignPlatform

    @SignPlatform.setter
    def SignPlatform(self, SignPlatform):
        self._SignPlatform = SignPlatform

    @property
    def SignerName(self):
        return self._SignerName

    @SignerName.setter
    def SignerName(self, SignerName):
        self._SignerName = SignerName

    @property
    def SignTime(self):
        return self._SignTime

    @SignTime.setter
    def SignTime(self, SignTime):
        self._SignTime = SignTime

    @property
    def SignAlgorithm(self):
        return self._SignAlgorithm

    @SignAlgorithm.setter
    def SignAlgorithm(self, SignAlgorithm):
        self._SignAlgorithm = SignAlgorithm

    @property
    def CertSn(self):
        return self._CertSn

    @CertSn.setter
    def CertSn(self, CertSn):
        self._CertSn = CertSn

    @property
    def CertNotBefore(self):
        return self._CertNotBefore

    @CertNotBefore.setter
    def CertNotBefore(self, CertNotBefore):
        self._CertNotBefore = CertNotBefore

    @property
    def CertNotAfter(self):
        return self._CertNotAfter

    @CertNotAfter.setter
    def CertNotAfter(self, CertNotAfter):
        self._CertNotAfter = CertNotAfter

    @property
    def SignType(self):
        return self._SignType

    @SignType.setter
    def SignType(self, SignType):
        self._SignType = SignType

    @property
    def ComponentPosX(self):
        return self._ComponentPosX

    @ComponentPosX.setter
    def ComponentPosX(self, ComponentPosX):
        self._ComponentPosX = ComponentPosX

    @property
    def ComponentPosY(self):
        return self._ComponentPosY

    @ComponentPosY.setter
    def ComponentPosY(self, ComponentPosY):
        self._ComponentPosY = ComponentPosY

    @property
    def ComponentWidth(self):
        return self._ComponentWidth

    @ComponentWidth.setter
    def ComponentWidth(self, ComponentWidth):
        self._ComponentWidth = ComponentWidth

    @property
    def ComponentHeight(self):
        return self._ComponentHeight

    @ComponentHeight.setter
    def ComponentHeight(self, ComponentHeight):
        self._ComponentHeight = ComponentHeight

    @property
    def ComponentPage(self):
        return self._ComponentPage

    @ComponentPage.setter
    def ComponentPage(self, ComponentPage):
        self._ComponentPage = ComponentPage


    def _deserialize(self, params):
        self._VerifyResult = params.get("VerifyResult")
        self._SignPlatform = params.get("SignPlatform")
        self._SignerName = params.get("SignerName")
        self._SignTime = params.get("SignTime")
        self._SignAlgorithm = params.get("SignAlgorithm")
        self._CertSn = params.get("CertSn")
        self._CertNotBefore = params.get("CertNotBefore")
        self._CertNotAfter = params.get("CertNotAfter")
        self._SignType = params.get("SignType")
        self._ComponentPosX = params.get("ComponentPosX")
        self._ComponentPosY = params.get("ComponentPosY")
        self._ComponentWidth = params.get("ComponentWidth")
        self._ComponentHeight = params.get("ComponentHeight")
        self._ComponentPage = params.get("ComponentPage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Permission(AbstractModel):
    """权限树节点权限

    """

    def __init__(self):
        r"""
        :param _Name: 权限名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Key: 权限key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Type: 权限类型 1前端，2后端
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _Hide: 是否隐藏
注意：此字段可能返回 null，表示取不到有效值。
        :type Hide: int
        :param _DataLabel: 数据权限标签 1:表示根节点，2:表示叶子结点
注意：此字段可能返回 null，表示取不到有效值。
        :type DataLabel: int
        :param _DataType: 数据权限独有，1:关联其他模块鉴权，2:表示关联自己模块鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :type DataType: int
        :param _DataRange: 数据权限独有，表示数据范围，1：全公司，2:部门及下级部门，3:自己
注意：此字段可能返回 null，表示取不到有效值。
        :type DataRange: int
        :param _DataTo: 关联权限, 表示这个功能权限要受哪个数据权限管控
注意：此字段可能返回 null，表示取不到有效值。
        :type DataTo: str
        :param _ParentKey: 父级权限key
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentKey: str
        :param _IsChecked: 是否选中
注意：此字段可能返回 null，表示取不到有效值。
        :type IsChecked: bool
        :param _Children: 子权限集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Children: list of Permission
        """
        self._Name = None
        self._Key = None
        self._Type = None
        self._Hide = None
        self._DataLabel = None
        self._DataType = None
        self._DataRange = None
        self._DataTo = None
        self._ParentKey = None
        self._IsChecked = None
        self._Children = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Hide(self):
        return self._Hide

    @Hide.setter
    def Hide(self, Hide):
        self._Hide = Hide

    @property
    def DataLabel(self):
        return self._DataLabel

    @DataLabel.setter
    def DataLabel(self, DataLabel):
        self._DataLabel = DataLabel

    @property
    def DataType(self):
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def DataRange(self):
        return self._DataRange

    @DataRange.setter
    def DataRange(self, DataRange):
        self._DataRange = DataRange

    @property
    def DataTo(self):
        return self._DataTo

    @DataTo.setter
    def DataTo(self, DataTo):
        self._DataTo = DataTo

    @property
    def ParentKey(self):
        return self._ParentKey

    @ParentKey.setter
    def ParentKey(self, ParentKey):
        self._ParentKey = ParentKey

    @property
    def IsChecked(self):
        return self._IsChecked

    @IsChecked.setter
    def IsChecked(self, IsChecked):
        self._IsChecked = IsChecked

    @property
    def Children(self):
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Key = params.get("Key")
        self._Type = params.get("Type")
        self._Hide = params.get("Hide")
        self._DataLabel = params.get("DataLabel")
        self._DataType = params.get("DataType")
        self._DataRange = params.get("DataRange")
        self._DataTo = params.get("DataTo")
        self._ParentKey = params.get("ParentKey")
        self._IsChecked = params.get("IsChecked")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = Permission()
                obj._deserialize(item)
                self._Children.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PermissionGroup(AbstractModel):
    """权限树中的权限组

    """

    def __init__(self):
        r"""
        :param _GroupName: 权限组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _GroupKey: 权限组key
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupKey: str
        :param _Hide: 是否隐藏分组，0否1是
注意：此字段可能返回 null，表示取不到有效值。
        :type Hide: int
        :param _Permissions: 权限集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Permissions: list of Permission
        """
        self._GroupName = None
        self._GroupKey = None
        self._Hide = None
        self._Permissions = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupKey(self):
        return self._GroupKey

    @GroupKey.setter
    def GroupKey(self, GroupKey):
        self._GroupKey = GroupKey

    @property
    def Hide(self):
        return self._Hide

    @Hide.setter
    def Hide(self, Hide):
        self._Hide = Hide

    @property
    def Permissions(self):
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._GroupKey = params.get("GroupKey")
        self._Hide = params.get("Hide")
        if params.get("Permissions") is not None:
            self._Permissions = []
            for item in params.get("Permissions"):
                obj = Permission()
                obj._deserialize(item)
                self._Permissions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrepareFlowsRequest(AbstractModel):
    """PrepareFlows请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _FlowInfos: 多个合同（签署流程）信息，最大支持20个签署流程。
        :type FlowInfos: list of FlowInfo
        :param _JumpUrl: 操作完成后的跳转地址，最大长度200
        :type JumpUrl: str
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._FlowInfos = None
        self._JumpUrl = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowInfos(self):
        return self._FlowInfos

    @FlowInfos.setter
    def FlowInfos(self, FlowInfos):
        self._FlowInfos = FlowInfos

    @property
    def JumpUrl(self):
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("FlowInfos") is not None:
            self._FlowInfos = []
            for item in params.get("FlowInfos"):
                obj = FlowInfo()
                obj._deserialize(item)
                self._FlowInfos.append(obj)
        self._JumpUrl = params.get("JumpUrl")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrepareFlowsResponse(AbstractModel):
    """PrepareFlows返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfirmUrl: 待发起文件确认页
        :type ConfirmUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConfirmUrl = None
        self._RequestId = None

    @property
    def ConfirmUrl(self):
        return self._ConfirmUrl

    @ConfirmUrl.setter
    def ConfirmUrl(self, ConfirmUrl):
        self._ConfirmUrl = ConfirmUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ConfirmUrl = params.get("ConfirmUrl")
        self._RequestId = params.get("RequestId")


class ProxyOrganizationOperator(AbstractModel):
    """合作企业经办人列表信息

    """

    def __init__(self):
        r"""
        :param _Id: 对应Agent-ProxyOperator-OpenId。第三方应用平台自定义，对子客企业员的唯一标识。一个OpenId在一个子客企业内唯一对应一个真实员工，不可在其他子客企业内重复使用。（例如，可以使用经办人企业名+员工身份证的hash值，需要第三方应用平台保存），最大64位字符串
        :type Id: str
        :param _Name: 经办人姓名，最大长度50个字符
        :type Name: str
        :param _IdCardType: 经办人身份证件类型
1.ID_CARD 居民身份证
2.HONGKONG_MACAO_AND_TAIWAN 港澳台居民居住证
3.HONGKONG_AND_MACAO 港澳居民来往内地通行证
        :type IdCardType: str
        :param _IdCardNumber: 经办人证件号
        :type IdCardNumber: str
        :param _Mobile: 经办人手机号，大陆手机号输入11位，暂不支持海外手机号。
        :type Mobile: str
        :param _DefaultRole: 默认角色，值为以下三个对应的英文：
业务管理员：admin
经办人：channel-normal-operator
业务员：channel-sales-man
        :type DefaultRole: str
        """
        self._Id = None
        self._Name = None
        self._IdCardType = None
        self._IdCardNumber = None
        self._Mobile = None
        self._DefaultRole = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCardType(self):
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def IdCardNumber(self):
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def DefaultRole(self):
        return self._DefaultRole

    @DefaultRole.setter
    def DefaultRole(self, DefaultRole):
        self._DefaultRole = DefaultRole


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
        self._Mobile = params.get("Mobile")
        self._DefaultRole = params.get("DefaultRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Recipient(AbstractModel):
    """流程中参与方的信息结构

    """

    def __init__(self):
        r"""
        :param _RecipientId: 签署人唯一标识，在通过模板发起合同的时候对应签署方ID
        :type RecipientId: str
        :param _RecipientType: 参与者类型，默认为空。
ENTERPRISE-企业；
INDIVIDUAL-个人；
PROMOTER-发起方
        :type RecipientType: str
        :param _Description: 描述信息	
        :type Description: str
        :param _RoleName: 角色名称	
        :type RoleName: str
        :param _RequireValidation: 是否需要校验，
true-是，
false-否
        :type RequireValidation: bool
        :param _RequireSign: 是否必须填写，
true-是，
false-否
        :type RequireSign: bool
        :param _SignType: 内部字段，签署类型
        :type SignType: int
        :param _RoutingOrder: 签署顺序：数字越小优先级越高
        :type RoutingOrder: int
        :param _IsPromoter: 是否是发起方，
true-是 
false-否
        :type IsPromoter: bool
        """
        self._RecipientId = None
        self._RecipientType = None
        self._Description = None
        self._RoleName = None
        self._RequireValidation = None
        self._RequireSign = None
        self._SignType = None
        self._RoutingOrder = None
        self._IsPromoter = None

    @property
    def RecipientId(self):
        return self._RecipientId

    @RecipientId.setter
    def RecipientId(self, RecipientId):
        self._RecipientId = RecipientId

    @property
    def RecipientType(self):
        return self._RecipientType

    @RecipientType.setter
    def RecipientType(self, RecipientType):
        self._RecipientType = RecipientType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def RequireValidation(self):
        return self._RequireValidation

    @RequireValidation.setter
    def RequireValidation(self, RequireValidation):
        self._RequireValidation = RequireValidation

    @property
    def RequireSign(self):
        return self._RequireSign

    @RequireSign.setter
    def RequireSign(self, RequireSign):
        self._RequireSign = RequireSign

    @property
    def SignType(self):
        return self._SignType

    @SignType.setter
    def SignType(self, SignType):
        self._SignType = SignType

    @property
    def RoutingOrder(self):
        return self._RoutingOrder

    @RoutingOrder.setter
    def RoutingOrder(self, RoutingOrder):
        self._RoutingOrder = RoutingOrder

    @property
    def IsPromoter(self):
        return self._IsPromoter

    @IsPromoter.setter
    def IsPromoter(self, IsPromoter):
        self._IsPromoter = IsPromoter


    def _deserialize(self, params):
        self._RecipientId = params.get("RecipientId")
        self._RecipientType = params.get("RecipientType")
        self._Description = params.get("Description")
        self._RoleName = params.get("RoleName")
        self._RequireValidation = params.get("RequireValidation")
        self._RequireSign = params.get("RequireSign")
        self._SignType = params.get("SignType")
        self._RoutingOrder = params.get("RoutingOrder")
        self._IsPromoter = params.get("IsPromoter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecipientComponentInfo(AbstractModel):
    """参与方填写控件信息

    """

    def __init__(self):
        r"""
        :param _RecipientId: 参与方Id
注意：此字段可能返回 null，表示取不到有效值。
        :type RecipientId: str
        :param _RecipientFillStatus: 参与方填写状态
注意：此字段可能返回 null，表示取不到有效值。
        :type RecipientFillStatus: str
        :param _IsPromoter: 是否发起方
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPromoter: bool
        :param _Components: 填写控件内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Components: list of FilledComponent
        """
        self._RecipientId = None
        self._RecipientFillStatus = None
        self._IsPromoter = None
        self._Components = None

    @property
    def RecipientId(self):
        return self._RecipientId

    @RecipientId.setter
    def RecipientId(self, RecipientId):
        self._RecipientId = RecipientId

    @property
    def RecipientFillStatus(self):
        return self._RecipientFillStatus

    @RecipientFillStatus.setter
    def RecipientFillStatus(self, RecipientFillStatus):
        self._RecipientFillStatus = RecipientFillStatus

    @property
    def IsPromoter(self):
        return self._IsPromoter

    @IsPromoter.setter
    def IsPromoter(self, IsPromoter):
        self._IsPromoter = IsPromoter

    @property
    def Components(self):
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components


    def _deserialize(self, params):
        self._RecipientId = params.get("RecipientId")
        self._RecipientFillStatus = params.get("RecipientFillStatus")
        self._IsPromoter = params.get("IsPromoter")
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = FilledComponent()
                obj._deserialize(item)
                self._Components.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleasedApprover(AbstractModel):
    """解除协议的签署人，如不指定，默认使用待解除流程（即原流程）中的签署人。
    注意：不支持更换C端（个人身份类型）签署人，如果原流程中含有C端签署人，默认使用原流程中的该签署人。
    注意：目前不支持替换C端（个人身份类型）签署人，但是可以指定C端签署人的签署方自定义控件别名，具体见参数ApproverSignRole描述。
    注意：当指定C端签署人的签署方自定义控件别名不空时，除参数ApproverNumber外，可以只参数ApproverSignRole。

    如果需要指定B端（机构身份类型）签署人，其中ReleasedApprover需要传递的参数如下：
    ApproverNumber, OrganizationName, ApproverType必传。
    对于其他身份标识
    - 子客企业指定经办人：OpenId必传，OrganizationOpenId必传；
    - 非子客企业：Name、Mobile必传。

    """

    def __init__(self):
        r"""
        :param _OrganizationName: 企业签署方工商营业执照上的企业名称，签署方为非发起方企业场景下必传，最大长度64个字符
        :type OrganizationName: str
        :param _ApproverNumber: 签署人在原流程中的签署人列表中的顺序序号（从0开始，按顺序依次递增），如果不清楚原流程中的签署人列表，可以通过DescribeFlows接口查看
        :type ApproverNumber: int
        :param _ApproverType: 签署人类型，目前仅支持
ORGANIZATION-企业
ENTERPRISESERVER-企业静默签
        :type ApproverType: str
        :param _Name: 签署人姓名，最大长度50个字符
        :type Name: str
        :param _IdCardType: 签署人身份证件类型
1.ID_CARD 居民身份证
2.HONGKONG_MACAO_AND_TAIWAN 港澳台居民居住证
3.HONGKONG_AND_MACAO 港澳居民来往内地通行证
        :type IdCardType: str
        :param _IdCardNumber: 签署人证件号
        :type IdCardNumber: str
        :param _Mobile: 签署人手机号，脱敏显示。大陆手机号为11位，暂不支持海外手机号
        :type Mobile: str
        :param _OrganizationOpenId: 企业签署方在同一第三方应用下的其他合作企业OpenId，签署方为非发起方企业场景下必传，最大长度64个字符
        :type OrganizationOpenId: str
        :param _OpenId: 用户侧第三方id，最大长度64个字符
当签署方为同一第三方应用下的员工时，该字必传
        :type OpenId: str
        :param _ApproverSignComponentType: 签署控件类型，支持自定义企业签署方的签署控件为“印章”或“签名”
- SIGN_SEAL-默认为印章控件类型
- SIGN_SIGNATURE-手写签名控件类型
        :type ApproverSignComponentType: str
        :param _ApproverSignRole: 签署方自定义控件别名，最大长度20个字符
        :type ApproverSignRole: str
        """
        self._OrganizationName = None
        self._ApproverNumber = None
        self._ApproverType = None
        self._Name = None
        self._IdCardType = None
        self._IdCardNumber = None
        self._Mobile = None
        self._OrganizationOpenId = None
        self._OpenId = None
        self._ApproverSignComponentType = None
        self._ApproverSignRole = None

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def ApproverNumber(self):
        return self._ApproverNumber

    @ApproverNumber.setter
    def ApproverNumber(self, ApproverNumber):
        self._ApproverNumber = ApproverNumber

    @property
    def ApproverType(self):
        return self._ApproverType

    @ApproverType.setter
    def ApproverType(self, ApproverType):
        self._ApproverType = ApproverType

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCardType(self):
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def IdCardNumber(self):
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def OrganizationOpenId(self):
        return self._OrganizationOpenId

    @OrganizationOpenId.setter
    def OrganizationOpenId(self, OrganizationOpenId):
        self._OrganizationOpenId = OrganizationOpenId

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def ApproverSignComponentType(self):
        return self._ApproverSignComponentType

    @ApproverSignComponentType.setter
    def ApproverSignComponentType(self, ApproverSignComponentType):
        self._ApproverSignComponentType = ApproverSignComponentType

    @property
    def ApproverSignRole(self):
        return self._ApproverSignRole

    @ApproverSignRole.setter
    def ApproverSignRole(self, ApproverSignRole):
        self._ApproverSignRole = ApproverSignRole


    def _deserialize(self, params):
        self._OrganizationName = params.get("OrganizationName")
        self._ApproverNumber = params.get("ApproverNumber")
        self._ApproverType = params.get("ApproverType")
        self._Name = params.get("Name")
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
        self._Mobile = params.get("Mobile")
        self._OrganizationOpenId = params.get("OrganizationOpenId")
        self._OpenId = params.get("OpenId")
        self._ApproverSignComponentType = params.get("ApproverSignComponentType")
        self._ApproverSignRole = params.get("ApproverSignRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelieveInfo(AbstractModel):
    """解除协议文档中内容信息，包括但不限于：解除理由、解除后仍然有效的条款-保留条款、原合同事项处理-费用结算、原合同事项处理-其他事项、其他约定等。

    """

    def __init__(self):
        r"""
        :param _Reason: 解除理由，最大支持200个字
        :type Reason: str
        :param _RemainInForceItem: 解除后仍然有效的条款，保留条款，最大支持200个字
        :type RemainInForceItem: str
        :param _OriginalExpenseSettlement: 原合同事项处理-费用结算，最大支持200个字
        :type OriginalExpenseSettlement: str
        :param _OriginalOtherSettlement: 原合同事项处理-其他事项，最大支持200个字
        :type OriginalOtherSettlement: str
        :param _OtherDeals: 其他约定，最大支持200个字
        :type OtherDeals: str
        """
        self._Reason = None
        self._RemainInForceItem = None
        self._OriginalExpenseSettlement = None
        self._OriginalOtherSettlement = None
        self._OtherDeals = None

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def RemainInForceItem(self):
        return self._RemainInForceItem

    @RemainInForceItem.setter
    def RemainInForceItem(self, RemainInForceItem):
        self._RemainInForceItem = RemainInForceItem

    @property
    def OriginalExpenseSettlement(self):
        return self._OriginalExpenseSettlement

    @OriginalExpenseSettlement.setter
    def OriginalExpenseSettlement(self, OriginalExpenseSettlement):
        self._OriginalExpenseSettlement = OriginalExpenseSettlement

    @property
    def OriginalOtherSettlement(self):
        return self._OriginalOtherSettlement

    @OriginalOtherSettlement.setter
    def OriginalOtherSettlement(self, OriginalOtherSettlement):
        self._OriginalOtherSettlement = OriginalOtherSettlement

    @property
    def OtherDeals(self):
        return self._OtherDeals

    @OtherDeals.setter
    def OtherDeals(self, OtherDeals):
        self._OtherDeals = OtherDeals


    def _deserialize(self, params):
        self._Reason = params.get("Reason")
        self._RemainInForceItem = params.get("RemainInForceItem")
        self._OriginalExpenseSettlement = params.get("OriginalExpenseSettlement")
        self._OriginalOtherSettlement = params.get("OriginalOtherSettlement")
        self._OtherDeals = params.get("OtherDeals")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemindFlowRecords(AbstractModel):
    """催办接口返回详细信息

    """

    def __init__(self):
        r"""
        :param _CanRemind: 是否能够催办，true-是，false-否
        :type CanRemind: bool
        :param _FlowId: 合同id
        :type FlowId: str
        :param _RemindMessage: 催办详情信息
        :type RemindMessage: str
        """
        self._CanRemind = None
        self._FlowId = None
        self._RemindMessage = None

    @property
    def CanRemind(self):
        return self._CanRemind

    @CanRemind.setter
    def CanRemind(self, CanRemind):
        self._CanRemind = CanRemind

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RemindMessage(self):
        return self._RemindMessage

    @RemindMessage.setter
    def RemindMessage(self, RemindMessage):
        self._RemindMessage = RemindMessage


    def _deserialize(self, params):
        self._CanRemind = params.get("CanRemind")
        self._FlowId = params.get("FlowId")
        self._RemindMessage = params.get("RemindMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceUrlInfo(AbstractModel):
    """资源链接信息

    """

    def __init__(self):
        r"""
        :param _Url: 资源链接地址，过期时间5分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _Name: 资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Type: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self._Url = None
        self._Name = None
        self._Type = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignQrCode(AbstractModel):
    """一码多扫签署二维码对象

    """

    def __init__(self):
        r"""
        :param _QrCodeId: 二维码id
        :type QrCodeId: str
        :param _QrCodeUrl: 二维码url
        :type QrCodeUrl: str
        :param _ExpiredTime: 二维码过期时间
        :type ExpiredTime: int
        """
        self._QrCodeId = None
        self._QrCodeUrl = None
        self._ExpiredTime = None

    @property
    def QrCodeId(self):
        return self._QrCodeId

    @QrCodeId.setter
    def QrCodeId(self, QrCodeId):
        self._QrCodeId = QrCodeId

    @property
    def QrCodeUrl(self):
        return self._QrCodeUrl

    @QrCodeUrl.setter
    def QrCodeUrl(self, QrCodeUrl):
        self._QrCodeUrl = QrCodeUrl

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime


    def _deserialize(self, params):
        self._QrCodeId = params.get("QrCodeId")
        self._QrCodeUrl = params.get("QrCodeUrl")
        self._ExpiredTime = params.get("ExpiredTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignUrl(AbstractModel):
    """一码多扫签署二维码签署信息

    """

    def __init__(self):
        r"""
        :param _AppSignUrl: 小程序签署链接
        :type AppSignUrl: str
        :param _EffectiveTime: 签署链接有效时间
        :type EffectiveTime: str
        :param _HttpSignUrl: 移动端签署链接
        :type HttpSignUrl: str
        """
        self._AppSignUrl = None
        self._EffectiveTime = None
        self._HttpSignUrl = None

    @property
    def AppSignUrl(self):
        return self._AppSignUrl

    @AppSignUrl.setter
    def AppSignUrl(self, AppSignUrl):
        self._AppSignUrl = AppSignUrl

    @property
    def EffectiveTime(self):
        return self._EffectiveTime

    @EffectiveTime.setter
    def EffectiveTime(self, EffectiveTime):
        self._EffectiveTime = EffectiveTime

    @property
    def HttpSignUrl(self):
        return self._HttpSignUrl

    @HttpSignUrl.setter
    def HttpSignUrl(self, HttpSignUrl):
        self._HttpSignUrl = HttpSignUrl


    def _deserialize(self, params):
        self._AppSignUrl = params.get("AppSignUrl")
        self._EffectiveTime = params.get("EffectiveTime")
        self._HttpSignUrl = params.get("HttpSignUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignUrlInfo(AbstractModel):
    """签署链接内容

    """

    def __init__(self):
        r"""
        :param _SignUrl: 签署链接，过期时间为90天
注意：此字段可能返回 null，表示取不到有效值。
        :type SignUrl: str
        :param _Deadline: 合同过期时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Deadline: int
        :param _SignOrder: 当流程为顺序签署此参数有效时，数字越小优先级越高，暂不支持并行签署 可选
注意：此字段可能返回 null，表示取不到有效值。
        :type SignOrder: int
        :param _SignId: 签署人编号
注意：此字段可能返回 null，表示取不到有效值。
        :type SignId: str
        :param _CustomUserId: 自定义用户编号
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomUserId: str
        :param _Name: 用户姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Mobile: 用户手机号码
注意：此字段可能返回 null，表示取不到有效值。
        :type Mobile: str
        :param _OrganizationName: 签署参与者机构名字
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationName: str
        :param _ApproverType: 参与者类型:
ORGANIZATION 企业经办人
PERSON 自然人
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproverType: str
        :param _IdCardNumber: 经办人身份证号
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardNumber: str
        :param _FlowId: 签署链接对应流程Id
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: str
        :param _OpenId: 企业经办人 用户在渠道的编号
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param _FlowGroupId: 合同组签署链接对应的合同组id
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowGroupId: str
        :param _SignQrcodeUrl: 二维码，在生成动态签署人跳转封面页链接时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type SignQrcodeUrl: str
        """
        self._SignUrl = None
        self._Deadline = None
        self._SignOrder = None
        self._SignId = None
        self._CustomUserId = None
        self._Name = None
        self._Mobile = None
        self._OrganizationName = None
        self._ApproverType = None
        self._IdCardNumber = None
        self._FlowId = None
        self._OpenId = None
        self._FlowGroupId = None
        self._SignQrcodeUrl = None

    @property
    def SignUrl(self):
        return self._SignUrl

    @SignUrl.setter
    def SignUrl(self, SignUrl):
        self._SignUrl = SignUrl

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def SignOrder(self):
        return self._SignOrder

    @SignOrder.setter
    def SignOrder(self, SignOrder):
        self._SignOrder = SignOrder

    @property
    def SignId(self):
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def CustomUserId(self):
        warnings.warn("parameter `CustomUserId` is deprecated", DeprecationWarning) 

        return self._CustomUserId

    @CustomUserId.setter
    def CustomUserId(self, CustomUserId):
        warnings.warn("parameter `CustomUserId` is deprecated", DeprecationWarning) 

        self._CustomUserId = CustomUserId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def ApproverType(self):
        return self._ApproverType

    @ApproverType.setter
    def ApproverType(self, ApproverType):
        self._ApproverType = ApproverType

    @property
    def IdCardNumber(self):
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def FlowGroupId(self):
        return self._FlowGroupId

    @FlowGroupId.setter
    def FlowGroupId(self, FlowGroupId):
        self._FlowGroupId = FlowGroupId

    @property
    def SignQrcodeUrl(self):
        return self._SignQrcodeUrl

    @SignQrcodeUrl.setter
    def SignQrcodeUrl(self, SignQrcodeUrl):
        self._SignQrcodeUrl = SignQrcodeUrl


    def _deserialize(self, params):
        self._SignUrl = params.get("SignUrl")
        self._Deadline = params.get("Deadline")
        self._SignOrder = params.get("SignOrder")
        self._SignId = params.get("SignId")
        self._CustomUserId = params.get("CustomUserId")
        self._Name = params.get("Name")
        self._Mobile = params.get("Mobile")
        self._OrganizationName = params.get("OrganizationName")
        self._ApproverType = params.get("ApproverType")
        self._IdCardNumber = params.get("IdCardNumber")
        self._FlowId = params.get("FlowId")
        self._OpenId = params.get("OpenId")
        self._FlowGroupId = params.get("FlowGroupId")
        self._SignQrcodeUrl = params.get("SignQrcodeUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Staff(AbstractModel):
    """企业员工信息

    """

    def __init__(self):
        r"""
        :param _UserId: 员工在电子签平台的用户ID
        :type UserId: str
        :param _DisplayName: 显示的员工名
        :type DisplayName: str
        :param _Mobile: 员工手机号
        :type Mobile: str
        :param _Email: 员工邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _OpenId: 员工在第三方应用平台的用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param _Roles: 员工角色
注意：此字段可能返回 null，表示取不到有效值。
        :type Roles: list of StaffRole
        :param _Department: 员工部门
注意：此字段可能返回 null，表示取不到有效值。
        :type Department: :class:`tencentcloud.essbasic.v20210526.models.Department`
        :param _Verified: 员工是否实名
        :type Verified: bool
        :param _CreatedOn: 员工创建时间戳，单位秒
        :type CreatedOn: int
        :param _VerifiedOn: 员工实名时间戳，单位秒
        :type VerifiedOn: int
        :param _QuiteJob: 员工是否离职：0-未离职，1-离职
        :type QuiteJob: int
        """
        self._UserId = None
        self._DisplayName = None
        self._Mobile = None
        self._Email = None
        self._OpenId = None
        self._Roles = None
        self._Department = None
        self._Verified = None
        self._CreatedOn = None
        self._VerifiedOn = None
        self._QuiteJob = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def Roles(self):
        return self._Roles

    @Roles.setter
    def Roles(self, Roles):
        self._Roles = Roles

    @property
    def Department(self):
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def Verified(self):
        return self._Verified

    @Verified.setter
    def Verified(self, Verified):
        self._Verified = Verified

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def VerifiedOn(self):
        return self._VerifiedOn

    @VerifiedOn.setter
    def VerifiedOn(self, VerifiedOn):
        self._VerifiedOn = VerifiedOn

    @property
    def QuiteJob(self):
        return self._QuiteJob

    @QuiteJob.setter
    def QuiteJob(self, QuiteJob):
        self._QuiteJob = QuiteJob


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._DisplayName = params.get("DisplayName")
        self._Mobile = params.get("Mobile")
        self._Email = params.get("Email")
        self._OpenId = params.get("OpenId")
        if params.get("Roles") is not None:
            self._Roles = []
            for item in params.get("Roles"):
                obj = StaffRole()
                obj._deserialize(item)
                self._Roles.append(obj)
        if params.get("Department") is not None:
            self._Department = Department()
            self._Department._deserialize(params.get("Department"))
        self._Verified = params.get("Verified")
        self._CreatedOn = params.get("CreatedOn")
        self._VerifiedOn = params.get("VerifiedOn")
        self._QuiteJob = params.get("QuiteJob")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffRole(AbstractModel):
    """第三方应用集成员工角色信息

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色id
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleId: str
        :param _RoleName: 角色名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleName: str
        """
        self._RoleId = None
        self._RoleName = None

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncFailReason(AbstractModel):
    """同步经办人失败原因

    """

    def __init__(self):
        r"""
        :param _Id: 对应Agent-ProxyOperator-OpenId。第三方应用平台自定义，对子客企业员的唯一标识。一个OpenId在一个子客企业内唯一对应一个真实员工，不可在其他子客企业内重复使用。（例如，可以使用经办人企业名+员工身份证的hash值，需要第三方应用平台保存），最大64位字符串
        :type Id: str
        :param _Message: 失败原因
例如：Id不符合规范、证件号码不合法等
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self._Id = None
        self._Message = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncProxyOrganizationOperatorsRequest(AbstractModel):
    """SyncProxyOrganizationOperators请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息。 此接口Agent.AppId 和 Agent.ProxyOrganizationOpenId必填。
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _OperatorType: 操作类型，新增:"CREATE"，修改:"UPDATE"，离职:"RESIGN"
        :type OperatorType: str
        :param _ProxyOrganizationOperators: 经办人信息列表，最大长度200
        :type ProxyOrganizationOperators: list of ProxyOrganizationOperator
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._OperatorType = None
        self._ProxyOrganizationOperators = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def OperatorType(self):
        return self._OperatorType

    @OperatorType.setter
    def OperatorType(self, OperatorType):
        self._OperatorType = OperatorType

    @property
    def ProxyOrganizationOperators(self):
        return self._ProxyOrganizationOperators

    @ProxyOrganizationOperators.setter
    def ProxyOrganizationOperators(self, ProxyOrganizationOperators):
        self._ProxyOrganizationOperators = ProxyOrganizationOperators

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._OperatorType = params.get("OperatorType")
        if params.get("ProxyOrganizationOperators") is not None:
            self._ProxyOrganizationOperators = []
            for item in params.get("ProxyOrganizationOperators"):
                obj = ProxyOrganizationOperator()
                obj._deserialize(item)
                self._ProxyOrganizationOperators.append(obj)
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncProxyOrganizationOperatorsResponse(AbstractModel):
    """SyncProxyOrganizationOperators返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: Status 同步状态,全部同步失败接口会直接报错
1-成功 
2-部分成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _FailedList: 同步失败经办人及其失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedList: list of SyncFailReason
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._FailedList = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailedList(self):
        return self._FailedList

    @FailedList.setter
    def FailedList(self, FailedList):
        self._FailedList = FailedList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        if params.get("FailedList") is not None:
            self._FailedList = []
            for item in params.get("FailedList"):
                obj = SyncFailReason()
                obj._deserialize(item)
                self._FailedList.append(obj)
        self._RequestId = params.get("RequestId")


class SyncProxyOrganizationRequest(AbstractModel):
    """SyncProxyOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用信息
此接口Agent.AppId、Agent.ProxyOrganizationOpenId必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _ProxyOrganizationName: 第三方平台子客企业名称，最大长度64个字符
        :type ProxyOrganizationName: str
        :param _BusinessLicense: 营业执照正面照(PNG或JPG) base64格式, 大小不超过5M
        :type BusinessLicense: str
        :param _UniformSocialCreditCode: 第三方平台子客企业统一社会信用代码，最大长度200个字符
        :type UniformSocialCreditCode: str
        :param _ProxyLegalName: 第三方平台子客企业法人/负责人姓名
        :type ProxyLegalName: str
        :param _Operator: 暂未开放
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        :param _ProxyLegalIdCardType: 第三方平台子客企业法人/负责人证件类型，默认居民身份证（ID_CARD）类型，暂不支持其他类型
        :type ProxyLegalIdCardType: str
        :param _ProxyLegalIdCardNumber: 第三方平台子客企业法人/负责人证件号
        :type ProxyLegalIdCardNumber: str
        """
        self._Agent = None
        self._ProxyOrganizationName = None
        self._BusinessLicense = None
        self._UniformSocialCreditCode = None
        self._ProxyLegalName = None
        self._Operator = None
        self._ProxyLegalIdCardType = None
        self._ProxyLegalIdCardNumber = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def ProxyOrganizationName(self):
        return self._ProxyOrganizationName

    @ProxyOrganizationName.setter
    def ProxyOrganizationName(self, ProxyOrganizationName):
        self._ProxyOrganizationName = ProxyOrganizationName

    @property
    def BusinessLicense(self):
        return self._BusinessLicense

    @BusinessLicense.setter
    def BusinessLicense(self, BusinessLicense):
        self._BusinessLicense = BusinessLicense

    @property
    def UniformSocialCreditCode(self):
        return self._UniformSocialCreditCode

    @UniformSocialCreditCode.setter
    def UniformSocialCreditCode(self, UniformSocialCreditCode):
        self._UniformSocialCreditCode = UniformSocialCreditCode

    @property
    def ProxyLegalName(self):
        return self._ProxyLegalName

    @ProxyLegalName.setter
    def ProxyLegalName(self, ProxyLegalName):
        self._ProxyLegalName = ProxyLegalName

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator

    @property
    def ProxyLegalIdCardType(self):
        return self._ProxyLegalIdCardType

    @ProxyLegalIdCardType.setter
    def ProxyLegalIdCardType(self, ProxyLegalIdCardType):
        self._ProxyLegalIdCardType = ProxyLegalIdCardType

    @property
    def ProxyLegalIdCardNumber(self):
        return self._ProxyLegalIdCardNumber

    @ProxyLegalIdCardNumber.setter
    def ProxyLegalIdCardNumber(self, ProxyLegalIdCardNumber):
        self._ProxyLegalIdCardNumber = ProxyLegalIdCardNumber


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._ProxyOrganizationName = params.get("ProxyOrganizationName")
        self._BusinessLicense = params.get("BusinessLicense")
        self._UniformSocialCreditCode = params.get("UniformSocialCreditCode")
        self._ProxyLegalName = params.get("ProxyLegalName")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._ProxyLegalIdCardType = params.get("ProxyLegalIdCardType")
        self._ProxyLegalIdCardNumber = params.get("ProxyLegalIdCardNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncProxyOrganizationResponse(AbstractModel):
    """SyncProxyOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TaskInfo(AbstractModel):
    """复杂文档合成任务的任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 合成任务Id，可以通过 ChannelGetTaskResultApi 接口获取任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskStatus: 任务状态：READY - 任务已完成；NOTREADY - 任务未完成；
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskStatus: str
        """
        self._TaskId = None
        self._TaskStatus = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateInfo(AbstractModel):
    """此结构体 (TemplateInfo) 用于描述模板的信息。

    > **模板组成**
    >
    >  一个模板通常会包含以下结构信息
    >- 模板基本信息
    >- 签署参与方 Recipients，在模板发起合同时用于指定参与方
    >- 填写控件 Components
    >- 签署控件 SignComponents

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID，模板的唯一标识
        :type TemplateId: str
        :param _TemplateName: 模板名
        :type TemplateName: str
        :param _Description: 模板描述信息
        :type Description: str
        :param _Components: 模板的填充控件列表
        :type Components: list of Component
        :param _Recipients: 模板中的签署参与方列表
        :type Recipients: list of Recipient
        :param _SignComponents: 模板中的签署控件列表
        :type SignComponents: list of Component
        :param _TemplateType: 模板类型：1-静默签；3-普通模板
        :type TemplateType: int
        :param _IsPromoter: 是否是发起人 ,已弃用
        :type IsPromoter: bool
        :param _Creator: 模板的创建者信息，电子签系统用户ID
        :type Creator: str
        :param _CreatedOn: 模板创建的时间戳，格式为Unix标准时间戳（秒）
        :type CreatedOn: int
        :param _PreviewUrl: 模板的H5预览链接,有效期5分钟。
可以通过浏览器打开此链接预览模板，或者嵌入到iframe中预览模板。
（此功能开放需要联系客户经理）
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewUrl: str
        :param _PdfUrl: 第三方应用集成-模板PDF文件链接，有效期5分钟。
请求参数WithPdfUrl=true时返回
（此功能开放需要联系客户经理）。
注意：此字段可能返回 null，表示取不到有效值。
        :type PdfUrl: str
        :param _ChannelTemplateId: 本模板关联的第三方应用平台企业模板ID
        :type ChannelTemplateId: str
        :param _ChannelTemplateName: 本模板关联的三方应用平台平台企业模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelTemplateName: str
        :param _ChannelAutoSave: 0-需要子客企业手动领取平台企业的模板(默认); 
1-平台自动设置子客模板
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelAutoSave: int
        :param _TemplateVersion: 模板版本，全数字字符。
默认为空，初始版本为yyyyMMdd001。
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateVersion: str
        :param _Available: 模板可用状态：
1启用（默认）
2停用
注意：此字段可能返回 null，表示取不到有效值。
        :type Available: int
        """
        self._TemplateId = None
        self._TemplateName = None
        self._Description = None
        self._Components = None
        self._Recipients = None
        self._SignComponents = None
        self._TemplateType = None
        self._IsPromoter = None
        self._Creator = None
        self._CreatedOn = None
        self._PreviewUrl = None
        self._PdfUrl = None
        self._ChannelTemplateId = None
        self._ChannelTemplateName = None
        self._ChannelAutoSave = None
        self._TemplateVersion = None
        self._Available = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Components(self):
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def Recipients(self):
        return self._Recipients

    @Recipients.setter
    def Recipients(self, Recipients):
        self._Recipients = Recipients

    @property
    def SignComponents(self):
        return self._SignComponents

    @SignComponents.setter
    def SignComponents(self, SignComponents):
        self._SignComponents = SignComponents

    @property
    def TemplateType(self):
        return self._TemplateType

    @TemplateType.setter
    def TemplateType(self, TemplateType):
        self._TemplateType = TemplateType

    @property
    def IsPromoter(self):
        warnings.warn("parameter `IsPromoter` is deprecated", DeprecationWarning) 

        return self._IsPromoter

    @IsPromoter.setter
    def IsPromoter(self, IsPromoter):
        warnings.warn("parameter `IsPromoter` is deprecated", DeprecationWarning) 

        self._IsPromoter = IsPromoter

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def PreviewUrl(self):
        return self._PreviewUrl

    @PreviewUrl.setter
    def PreviewUrl(self, PreviewUrl):
        self._PreviewUrl = PreviewUrl

    @property
    def PdfUrl(self):
        return self._PdfUrl

    @PdfUrl.setter
    def PdfUrl(self, PdfUrl):
        self._PdfUrl = PdfUrl

    @property
    def ChannelTemplateId(self):
        return self._ChannelTemplateId

    @ChannelTemplateId.setter
    def ChannelTemplateId(self, ChannelTemplateId):
        self._ChannelTemplateId = ChannelTemplateId

    @property
    def ChannelTemplateName(self):
        return self._ChannelTemplateName

    @ChannelTemplateName.setter
    def ChannelTemplateName(self, ChannelTemplateName):
        self._ChannelTemplateName = ChannelTemplateName

    @property
    def ChannelAutoSave(self):
        return self._ChannelAutoSave

    @ChannelAutoSave.setter
    def ChannelAutoSave(self, ChannelAutoSave):
        self._ChannelAutoSave = ChannelAutoSave

    @property
    def TemplateVersion(self):
        return self._TemplateVersion

    @TemplateVersion.setter
    def TemplateVersion(self, TemplateVersion):
        self._TemplateVersion = TemplateVersion

    @property
    def Available(self):
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._Description = params.get("Description")
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self._Components.append(obj)
        if params.get("Recipients") is not None:
            self._Recipients = []
            for item in params.get("Recipients"):
                obj = Recipient()
                obj._deserialize(item)
                self._Recipients.append(obj)
        if params.get("SignComponents") is not None:
            self._SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self._SignComponents.append(obj)
        self._TemplateType = params.get("TemplateType")
        self._IsPromoter = params.get("IsPromoter")
        self._Creator = params.get("Creator")
        self._CreatedOn = params.get("CreatedOn")
        self._PreviewUrl = params.get("PreviewUrl")
        self._PdfUrl = params.get("PdfUrl")
        self._ChannelTemplateId = params.get("ChannelTemplateId")
        self._ChannelTemplateName = params.get("ChannelTemplateName")
        self._ChannelAutoSave = params.get("ChannelAutoSave")
        self._TemplateVersion = params.get("TemplateVersion")
        self._Available = params.get("Available")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFile(AbstractModel):
    """此结构体 (UploadFile) 用于描述多文件上传的文件信息。

    """

    def __init__(self):
        r"""
        :param _FileBody: Base64编码后的文件内容
        :type FileBody: str
        :param _FileName: 文件名
        :type FileName: str
        """
        self._FileBody = None
        self._FileName = None

    @property
    def FileBody(self):
        return self._FileBody

    @FileBody.setter
    def FileBody(self, FileBody):
        self._FileBody = FileBody

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName


    def _deserialize(self, params):
        self._FileBody = params.get("FileBody")
        self._FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFilesRequest(AbstractModel):
    """UploadFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 应用相关信息，若是第三方应用集成调用 若是第三方应用集成调用,Agent.AppId 和 Agent.ProxyOrganizationOpenId 必填
        :type Agent: :class:`tencentcloud.essbasic.v20210526.models.Agent`
        :param _BusinessType: 文件对应业务类型
1. TEMPLATE - 模板； 文件类型：.pdf/.doc/.docx/.html
2. DOCUMENT - 签署过程及签署后的合同文档/图片控件 文件类型：.pdf/.doc/.docx/.jpg/.png/.xls.xlsx/.html
        :type BusinessType: str
        :param _FileInfos: 上传文件内容数组，最多支持20个文件
        :type FileInfos: list of UploadFile
        :param _Operator: 操作者的信息
        :type Operator: :class:`tencentcloud.essbasic.v20210526.models.UserInfo`
        """
        self._Agent = None
        self._BusinessType = None
        self._FileInfos = None
        self._Operator = None

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def BusinessType(self):
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def FileInfos(self):
        return self._FileInfos

    @FileInfos.setter
    def FileInfos(self, FileInfos):
        self._FileInfos = FileInfos

    @property
    def Operator(self):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        warnings.warn("parameter `Operator` is deprecated", DeprecationWarning) 

        self._Operator = Operator


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._BusinessType = params.get("BusinessType")
        if params.get("FileInfos") is not None:
            self._FileInfos = []
            for item in params.get("FileInfos"):
                obj = UploadFile()
                obj._deserialize(item)
                self._FileInfos.append(obj)
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFilesResponse(AbstractModel):
    """UploadFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 上传成功文件数量
        :type TotalCount: int
        :param _FileIds: 文件id数组，有效期一个小时；有效期内此文件id可以反复使用
        :type FileIds: list of str
        :param _FileUrls: 文件Url
        :type FileUrls: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._FileIds = None
        self._FileUrls = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def FileIds(self):
        return self._FileIds

    @FileIds.setter
    def FileIds(self, FileIds):
        self._FileIds = FileIds

    @property
    def FileUrls(self):
        return self._FileUrls

    @FileUrls.setter
    def FileUrls(self, FileUrls):
        self._FileUrls = FileUrls

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._FileIds = params.get("FileIds")
        self._FileUrls = params.get("FileUrls")
        self._RequestId = params.get("RequestId")


class UsageDetail(AbstractModel):
    """用量明细

    """

    def __init__(self):
        r"""
        :param _ProxyOrganizationOpenId: 子客企业唯一标识
        :type ProxyOrganizationOpenId: str
        :param _ProxyOrganizationName: 子客企业名
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyOrganizationName: str
        :param _Date: 日期，当需要汇总数据时日期为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Date: str
        :param _Usage: 消耗数量
        :type Usage: int
        :param _Cancel: 撤回数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Cancel: int
        :param _FlowChannel: 消耗渠道
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowChannel: str
        """
        self._ProxyOrganizationOpenId = None
        self._ProxyOrganizationName = None
        self._Date = None
        self._Usage = None
        self._Cancel = None
        self._FlowChannel = None

    @property
    def ProxyOrganizationOpenId(self):
        return self._ProxyOrganizationOpenId

    @ProxyOrganizationOpenId.setter
    def ProxyOrganizationOpenId(self, ProxyOrganizationOpenId):
        self._ProxyOrganizationOpenId = ProxyOrganizationOpenId

    @property
    def ProxyOrganizationName(self):
        return self._ProxyOrganizationName

    @ProxyOrganizationName.setter
    def ProxyOrganizationName(self, ProxyOrganizationName):
        self._ProxyOrganizationName = ProxyOrganizationName

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Usage(self):
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Cancel(self):
        return self._Cancel

    @Cancel.setter
    def Cancel(self, Cancel):
        self._Cancel = Cancel

    @property
    def FlowChannel(self):
        return self._FlowChannel

    @FlowChannel.setter
    def FlowChannel(self, FlowChannel):
        self._FlowChannel = FlowChannel


    def _deserialize(self, params):
        self._ProxyOrganizationOpenId = params.get("ProxyOrganizationOpenId")
        self._ProxyOrganizationName = params.get("ProxyOrganizationName")
        self._Date = params.get("Date")
        self._Usage = params.get("Usage")
        self._Cancel = params.get("Cancel")
        self._FlowChannel = params.get("FlowChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    """接口调用者信息

    """

    def __init__(self):
        r"""
        :param _OpenId: 第三方应用平台自定义，对应第三方平台子客企业员的唯一标识。一个OpenId在一个子客企业内唯一对应一个真实员工，不可在其他子客企业内重复使用。（例如，可以使用经办人企业名+员工身份证的hash值，需要第三方应用平台保存），最大64位字符串
        :type OpenId: str
        :param _Channel: 内部参数，暂未开放使用
        :type Channel: str
        :param _CustomUserId: 内部参数，暂未开放使用
        :type CustomUserId: str
        :param _ClientIp: 内部参数，暂未开放使用
        :type ClientIp: str
        :param _ProxyIp: 内部参数，暂未开放使用
        :type ProxyIp: str
        """
        self._OpenId = None
        self._Channel = None
        self._CustomUserId = None
        self._ClientIp = None
        self._ProxyIp = None

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def Channel(self):
        warnings.warn("parameter `Channel` is deprecated", DeprecationWarning) 

        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        warnings.warn("parameter `Channel` is deprecated", DeprecationWarning) 

        self._Channel = Channel

    @property
    def CustomUserId(self):
        warnings.warn("parameter `CustomUserId` is deprecated", DeprecationWarning) 

        return self._CustomUserId

    @CustomUserId.setter
    def CustomUserId(self, CustomUserId):
        warnings.warn("parameter `CustomUserId` is deprecated", DeprecationWarning) 

        self._CustomUserId = CustomUserId

    @property
    def ClientIp(self):
        warnings.warn("parameter `ClientIp` is deprecated", DeprecationWarning) 

        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        warnings.warn("parameter `ClientIp` is deprecated", DeprecationWarning) 

        self._ClientIp = ClientIp

    @property
    def ProxyIp(self):
        warnings.warn("parameter `ProxyIp` is deprecated", DeprecationWarning) 

        return self._ProxyIp

    @ProxyIp.setter
    def ProxyIp(self, ProxyIp):
        warnings.warn("parameter `ProxyIp` is deprecated", DeprecationWarning) 

        self._ProxyIp = ProxyIp


    def _deserialize(self, params):
        self._OpenId = params.get("OpenId")
        self._Channel = params.get("Channel")
        self._CustomUserId = params.get("CustomUserId")
        self._ClientIp = params.get("ClientIp")
        self._ProxyIp = params.get("ProxyIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserThreeFactor(AbstractModel):
    """用户的三要素：姓名，证件号，证件类型

    """

    def __init__(self):
        r"""
        :param _Name: 姓名
        :type Name: str
        :param _IdCardType: 证件类型: 
ID_CARD 身份证
HONGKONG_AND_MACAO 港澳居民来往内地通行证
HONGKONG_MACAO_AND_TAIWAN 港澳台居民居住证(格式同居民身份证)
        :type IdCardType: str
        :param _IdCardNumber: 证件号，如果有 X 请大写
        :type IdCardNumber: str
        """
        self._Name = None
        self._IdCardType = None
        self._IdCardNumber = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCardType(self):
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def IdCardNumber(self):
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebThemeConfig(AbstractModel):
    """主题配置

    """

    def __init__(self):
        r"""
        :param _DisplaySignBrandLogo: 是否显示页面底部电子签logo，取值如下：
<ul><li> **true**：页面底部显示电子签logo</li>
<li> **false**：页面底部不显示电子签logo（默认）</li></ul>
        :type DisplaySignBrandLogo: bool
        :param _WebEmbedThemeColor: 主题颜色：
支持十六进制颜色值以及RGB格式颜色值，例如：#D54941，rgb(213, 73, 65)
<br/>
        :type WebEmbedThemeColor: str
        """
        self._DisplaySignBrandLogo = None
        self._WebEmbedThemeColor = None

    @property
    def DisplaySignBrandLogo(self):
        return self._DisplaySignBrandLogo

    @DisplaySignBrandLogo.setter
    def DisplaySignBrandLogo(self, DisplaySignBrandLogo):
        self._DisplaySignBrandLogo = DisplaySignBrandLogo

    @property
    def WebEmbedThemeColor(self):
        return self._WebEmbedThemeColor

    @WebEmbedThemeColor.setter
    def WebEmbedThemeColor(self, WebEmbedThemeColor):
        self._WebEmbedThemeColor = WebEmbedThemeColor


    def _deserialize(self, params):
        self._DisplaySignBrandLogo = params.get("DisplaySignBrandLogo")
        self._WebEmbedThemeColor = params.get("WebEmbedThemeColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        