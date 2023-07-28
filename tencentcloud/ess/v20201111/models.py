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


class Admin(AbstractModel):
    """企业超管信息

    """

    def __init__(self):
        r"""
        :param _Name: 超管名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Mobile: 超管手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type Mobile: str
        """
        self._Name = None
        self._Mobile = None

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
        self._Name = params.get("Name")
        self._Mobile = params.get("Mobile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Agent(AbstractModel):
    """代理相关应用信息，如集团主企业代子企业操作

    """

    def __init__(self):
        r"""
        :param _AppId: 代理机构的应用编号,32位字符串，一般不用传
        :type AppId: str
        :param _ProxyAppId: 被代理机构的应用号，一般不用传
        :type ProxyAppId: str
        :param _ProxyOrganizationId: 被代理机构在电子签平台的机构编号，集团代理下场景必传
        :type ProxyOrganizationId: str
        :param _ProxyOperator: 被代理机构的经办人，一般不用传
        :type ProxyOperator: str
        """
        self._AppId = None
        self._ProxyAppId = None
        self._ProxyOrganizationId = None
        self._ProxyOperator = None

    @property
    def AppId(self):
        warnings.warn("parameter `AppId` is deprecated", DeprecationWarning) 

        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        warnings.warn("parameter `AppId` is deprecated", DeprecationWarning) 

        self._AppId = AppId

    @property
    def ProxyAppId(self):
        warnings.warn("parameter `ProxyAppId` is deprecated", DeprecationWarning) 

        return self._ProxyAppId

    @ProxyAppId.setter
    def ProxyAppId(self, ProxyAppId):
        warnings.warn("parameter `ProxyAppId` is deprecated", DeprecationWarning) 

        self._ProxyAppId = ProxyAppId

    @property
    def ProxyOrganizationId(self):
        return self._ProxyOrganizationId

    @ProxyOrganizationId.setter
    def ProxyOrganizationId(self, ProxyOrganizationId):
        self._ProxyOrganizationId = ProxyOrganizationId

    @property
    def ProxyOperator(self):
        warnings.warn("parameter `ProxyOperator` is deprecated", DeprecationWarning) 

        return self._ProxyOperator

    @ProxyOperator.setter
    def ProxyOperator(self, ProxyOperator):
        warnings.warn("parameter `ProxyOperator` is deprecated", DeprecationWarning) 

        self._ProxyOperator = ProxyOperator


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ProxyAppId = params.get("ProxyAppId")
        self._ProxyOrganizationId = params.get("ProxyOrganizationId")
        self._ProxyOperator = params.get("ProxyOperator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApproverInfo(AbstractModel):
    """参与者信息

    """

    def __init__(self):
        r"""
        :param _ApproverType: 参与者类型：
0：企业
1：个人
3：企业静默签署
注：类型为3（企业静默签署）时，此接口会默认完成该签署方的签署。静默签署仅进行盖章操作，不能自动签名。
        :type ApproverType: int
        :param _ApproverName: 签署人的姓名
        :type ApproverName: str
        :param _ApproverMobile: 签署人的手机号，11位数字
        :type ApproverMobile: str
        :param _OrganizationName: 如果签署方是企业签署方，则为企业名
        :type OrganizationName: str
        :param _SignComponents: 签署人的签署控件列表
        :type SignComponents: list of Component
        :param _ApproverIdCardNumber: 签署人的身份证号
        :type ApproverIdCardNumber: str
        :param _ApproverIdCardType: 签署人的身份证件类型 
ID_CARD 身份证
HONGKONG_AND_MACAO 港澳居民来往内地通行证
HONGKONG_MACAO_AND_TAIWAN 港澳台居民居住证(格式同居民身份证)
        :type ApproverIdCardType: str
        :param _NotifyType: 签署通知类型：sms--短信，none--不通知
        :type NotifyType: str
        :param _ApproverRole: 签署人角色类型：1--收款人、2--开具人、3--见证人
        :type ApproverRole: int
        :param _VerifyChannel: 签署意愿确认渠道，默认为WEIXINAPP:人脸识别
        :type VerifyChannel: list of str
        :param _PreReadTime: 合同的强制预览时间：3~300s，未指定则按合同页数计算
        :type PreReadTime: int
        :param _UserId: 签署人userId，传此字段则不用传姓名、手机号
        :type UserId: str
        :param _ApproverSource: 签署人用户来源，企微侧用户请传入：WEWORKAPP
        :type ApproverSource: str
        :param _CustomApproverTag: 企业签署方或签标识，客户自定义，64位长度。用于发起含有或签签署人的合同。或签参与人必须有此字段。合同内不同或签参与人CustomApproverTag需要保证唯一。如果或签签署人为本方企微参与人，ApproverSource参数需要指定WEWORKAPP
        :type CustomApproverTag: str
        :param _ApproverOption: 签署人个性化能力值
        :type ApproverOption: :class:`tencentcloud.ess.v20201111.models.ApproverOption`
        :param _ApproverVerifyTypes: 签署人查看合同时认证方式, 
1-实名查看 2-短信验证码查看(企业签署方不支持该方式)
如果不传默认为1
模板发起的时候,认证方式以模板配置为主
        :type ApproverVerifyTypes: list of int
        :param _ApproverSignTypes: 签署人签署合同时的认证方式
1-人脸认证 2-签署密码 3-运营商三要素(默认为1,2)
合同签署认证方式的优先级 verifyChannel>approverSignTypes
模板发起的时候,认证方式以模板配置为主
        :type ApproverSignTypes: list of int
        :param _ApproverNeedSignReview: 当前签署方进行签署操作是否需要企业内部审批，true 则为需要。为个人签署方时则由发起方企业审核。	
        :type ApproverNeedSignReview: bool
        """
        self._ApproverType = None
        self._ApproverName = None
        self._ApproverMobile = None
        self._OrganizationName = None
        self._SignComponents = None
        self._ApproverIdCardNumber = None
        self._ApproverIdCardType = None
        self._NotifyType = None
        self._ApproverRole = None
        self._VerifyChannel = None
        self._PreReadTime = None
        self._UserId = None
        self._ApproverSource = None
        self._CustomApproverTag = None
        self._ApproverOption = None
        self._ApproverVerifyTypes = None
        self._ApproverSignTypes = None
        self._ApproverNeedSignReview = None

    @property
    def ApproverType(self):
        return self._ApproverType

    @ApproverType.setter
    def ApproverType(self, ApproverType):
        self._ApproverType = ApproverType

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
    def SignComponents(self):
        return self._SignComponents

    @SignComponents.setter
    def SignComponents(self, SignComponents):
        self._SignComponents = SignComponents

    @property
    def ApproverIdCardNumber(self):
        return self._ApproverIdCardNumber

    @ApproverIdCardNumber.setter
    def ApproverIdCardNumber(self, ApproverIdCardNumber):
        self._ApproverIdCardNumber = ApproverIdCardNumber

    @property
    def ApproverIdCardType(self):
        return self._ApproverIdCardType

    @ApproverIdCardType.setter
    def ApproverIdCardType(self, ApproverIdCardType):
        self._ApproverIdCardType = ApproverIdCardType

    @property
    def NotifyType(self):
        return self._NotifyType

    @NotifyType.setter
    def NotifyType(self, NotifyType):
        self._NotifyType = NotifyType

    @property
    def ApproverRole(self):
        return self._ApproverRole

    @ApproverRole.setter
    def ApproverRole(self, ApproverRole):
        self._ApproverRole = ApproverRole

    @property
    def VerifyChannel(self):
        return self._VerifyChannel

    @VerifyChannel.setter
    def VerifyChannel(self, VerifyChannel):
        self._VerifyChannel = VerifyChannel

    @property
    def PreReadTime(self):
        return self._PreReadTime

    @PreReadTime.setter
    def PreReadTime(self, PreReadTime):
        self._PreReadTime = PreReadTime

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ApproverSource(self):
        return self._ApproverSource

    @ApproverSource.setter
    def ApproverSource(self, ApproverSource):
        self._ApproverSource = ApproverSource

    @property
    def CustomApproverTag(self):
        return self._CustomApproverTag

    @CustomApproverTag.setter
    def CustomApproverTag(self, CustomApproverTag):
        self._CustomApproverTag = CustomApproverTag

    @property
    def ApproverOption(self):
        return self._ApproverOption

    @ApproverOption.setter
    def ApproverOption(self, ApproverOption):
        self._ApproverOption = ApproverOption

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
    def ApproverNeedSignReview(self):
        return self._ApproverNeedSignReview

    @ApproverNeedSignReview.setter
    def ApproverNeedSignReview(self, ApproverNeedSignReview):
        self._ApproverNeedSignReview = ApproverNeedSignReview


    def _deserialize(self, params):
        self._ApproverType = params.get("ApproverType")
        self._ApproverName = params.get("ApproverName")
        self._ApproverMobile = params.get("ApproverMobile")
        self._OrganizationName = params.get("OrganizationName")
        if params.get("SignComponents") is not None:
            self._SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self._SignComponents.append(obj)
        self._ApproverIdCardNumber = params.get("ApproverIdCardNumber")
        self._ApproverIdCardType = params.get("ApproverIdCardType")
        self._NotifyType = params.get("NotifyType")
        self._ApproverRole = params.get("ApproverRole")
        self._VerifyChannel = params.get("VerifyChannel")
        self._PreReadTime = params.get("PreReadTime")
        self._UserId = params.get("UserId")
        self._ApproverSource = params.get("ApproverSource")
        self._CustomApproverTag = params.get("CustomApproverTag")
        if params.get("ApproverOption") is not None:
            self._ApproverOption = ApproverOption()
            self._ApproverOption._deserialize(params.get("ApproverOption"))
        self._ApproverVerifyTypes = params.get("ApproverVerifyTypes")
        self._ApproverSignTypes = params.get("ApproverSignTypes")
        self._ApproverNeedSignReview = params.get("ApproverNeedSignReview")
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
        :param _NoRefuse: 是否可以拒签 默认false-可以拒签 true-不可以拒签
        :type NoRefuse: bool
        :param _NoTransfer: 是否可以转发 默认false-可以转发 true-不可以转发
        :type NoTransfer: bool
        """
        self._NoRefuse = None
        self._NoTransfer = None

    @property
    def NoRefuse(self):
        return self._NoRefuse

    @NoRefuse.setter
    def NoRefuse(self, NoRefuse):
        self._NoRefuse = NoRefuse

    @property
    def NoTransfer(self):
        return self._NoTransfer

    @NoTransfer.setter
    def NoTransfer(self, NoTransfer):
        self._NoTransfer = NoTransfer


    def _deserialize(self, params):
        self._NoRefuse = params.get("NoRefuse")
        self._NoTransfer = params.get("NoTransfer")
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
        :param _Name: 指定签署人名字
        :type Name: str
        :param _Mobile: 指定签署人手机号，11位数字
        :type Mobile: str
        :param _IdCardType: 指定签署人证件类型，ID_CARD-身份证
        :type IdCardType: str
        :param _IdCardNumber: 指定签署人证件号码，字母大写
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
        


class AuthorizedUser(AbstractModel):
    """授权用户

    """

    def __init__(self):
        r"""
        :param _UserId: 电子签系统中的用户id
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
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
        :type UserInfo: :class:`tencentcloud.ess.v20201111.models.UserThreeFactor`
        :param _CallbackUrl: 接受自动签开启的回调地址。需要保证post返回200
        :type CallbackUrl: str
        :param _CertInfoCallback: 是否回调证书信息，默认false-不需要
        :type CertInfoCallback: bool
        :param _UserDefineSeal: 是否支持用户自定义签名印章，默认false-不需要
        :type UserDefineSeal: bool
        :param _SealImgCallback: 是否需要回调的时候返回印章(签名) 图片的 base64，默认false-不需要
        :type SealImgCallback: bool
        :param _VerifyChannels: 开通时候的验证方式，取值：WEIXINAPP（微信人脸识别），INSIGHT（慧眼人脸认别），TELECOM（运营商三要素验证）。如果是小程序开通链接，支持传 WEIXINAPP / TELECOM。如果是 H5 开通链接，支持传 INSIGHT / TELECOM。默认值 WEIXINAPP / INSIGHT。
        :type VerifyChannels: list of str
        """
        self._UserInfo = None
        self._CallbackUrl = None
        self._CertInfoCallback = None
        self._UserDefineSeal = None
        self._SealImgCallback = None
        self._VerifyChannels = None

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

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
    def VerifyChannels(self):
        return self._VerifyChannels

    @VerifyChannels.setter
    def VerifyChannels(self, VerifyChannels):
        self._VerifyChannels = VerifyChannels


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = UserThreeFactor()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._CallbackUrl = params.get("CallbackUrl")
        self._CertInfoCallback = params.get("CertInfoCallback")
        self._UserDefineSeal = params.get("UserDefineSeal")
        self._SealImgCallback = params.get("SealImgCallback")
        self._VerifyChannels = params.get("VerifyChannels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindEmployeeUserIdWithClientOpenIdRequest(AbstractModel):
    """BindEmployeeUserIdWithClientOpenId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 用户信息，OpenId与UserId二选一必填一个，OpenId是第三方客户ID，userId是用户实名后的电子签生成的ID,当传入客户系统openId，传入的openId需与电子签员工userId绑定，且参数Channel必填，Channel值为INTEGRATE；当传入参数UserId，Channel无需指定。（参数参考示例）
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _UserId: 电子签系统员工UserId
        :type UserId: str
        :param _OpenId: 客户系统OpenId
        :type OpenId: str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._UserId = None
        self._OpenId = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

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
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._UserId = params.get("UserId")
        self._OpenId = params.get("OpenId")
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
        


class BindEmployeeUserIdWithClientOpenIdResponse(AbstractModel):
    """BindEmployeeUserIdWithClientOpenId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 绑定是否成功，1表示成功，0表示失败
        :type Status: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CallbackInfo(AbstractModel):
    """应用回调信息

    """

    def __init__(self):
        r"""
        :param _CallbackUrl: 回调url
        :type CallbackUrl: str
        :param _Token: 回调加密key，已废弃
        :type Token: str
        :param _CallbackKey: 回调加密key
        :type CallbackKey: str
        :param _CallbackToken: 回调验签token
        :type CallbackToken: str
        """
        self._CallbackUrl = None
        self._Token = None
        self._CallbackKey = None
        self._CallbackToken = None

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def Token(self):
        warnings.warn("parameter `Token` is deprecated", DeprecationWarning) 

        return self._Token

    @Token.setter
    def Token(self, Token):
        warnings.warn("parameter `Token` is deprecated", DeprecationWarning) 

        self._Token = Token

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def CallbackToken(self):
        return self._CallbackToken

    @CallbackToken.setter
    def CallbackToken(self, CallbackToken):
        self._CallbackToken = CallbackToken


    def _deserialize(self, params):
        self._CallbackUrl = params.get("CallbackUrl")
        self._Token = params.get("Token")
        self._CallbackKey = params.get("CallbackKey")
        self._CallbackToken = params.get("CallbackToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Caller(AbstractModel):
    """此结构体 (Caller) 用于描述调用方属性。

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用号
        :type ApplicationId: str
        :param _OrganizationId: 主机构ID
        :type OrganizationId: str
        :param _OperatorId: 经办人的用户ID，同UserId
        :type OperatorId: str
        :param _SubOrganizationId: 下属机构ID
        :type SubOrganizationId: str
        """
        self._ApplicationId = None
        self._OrganizationId = None
        self._OperatorId = None
        self._SubOrganizationId = None

    @property
    def ApplicationId(self):
        warnings.warn("parameter `ApplicationId` is deprecated", DeprecationWarning) 

        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        warnings.warn("parameter `ApplicationId` is deprecated", DeprecationWarning) 

        self._ApplicationId = ApplicationId

    @property
    def OrganizationId(self):
        warnings.warn("parameter `OrganizationId` is deprecated", DeprecationWarning) 

        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        warnings.warn("parameter `OrganizationId` is deprecated", DeprecationWarning) 

        self._OrganizationId = OrganizationId

    @property
    def OperatorId(self):
        return self._OperatorId

    @OperatorId.setter
    def OperatorId(self, OperatorId):
        self._OperatorId = OperatorId

    @property
    def SubOrganizationId(self):
        warnings.warn("parameter `SubOrganizationId` is deprecated", DeprecationWarning) 

        return self._SubOrganizationId

    @SubOrganizationId.setter
    def SubOrganizationId(self, SubOrganizationId):
        warnings.warn("parameter `SubOrganizationId` is deprecated", DeprecationWarning) 

        self._SubOrganizationId = SubOrganizationId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._OrganizationId = params.get("OrganizationId")
        self._OperatorId = params.get("OperatorId")
        self._SubOrganizationId = params.get("SubOrganizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelFlowRequest(AbstractModel):
    """CancelFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowId: 签署流程id
        :type FlowId: str
        :param _CancelMessage: 撤销原因，最长200个字符；
        :type CancelMessage: str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._FlowId = None
        self._CancelMessage = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def CancelMessage(self):
        return self._CancelMessage

    @CancelMessage.setter
    def CancelMessage(self, CancelMessage):
        self._CancelMessage = CancelMessage

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowId = params.get("FlowId")
        self._CancelMessage = params.get("CancelMessage")
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
        


class CancelFlowResponse(AbstractModel):
    """CancelFlow返回参数结构体

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


class CancelMultiFlowSignQRCodeRequest(AbstractModel):
    """CancelMultiFlowSignQRCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _QrCodeId: 二维码id
        :type QrCodeId: str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._QrCodeId = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def QrCodeId(self):
        return self._QrCodeId

    @QrCodeId.setter
    def QrCodeId(self, QrCodeId):
        self._QrCodeId = QrCodeId

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._QrCodeId = params.get("QrCodeId")
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
        


class CancelMultiFlowSignQRCodeResponse(AbstractModel):
    """CancelMultiFlowSignQRCode返回参数结构体

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


class CancelUserAutoSignEnableUrlRequest(AbstractModel):
    """CancelUserAutoSignEnableUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息，UseId必填	
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _SceneKey: 自动签场景: E_PRESCRIPTION_AUTO_SIGN 电子处方
        :type SceneKey: str
        :param _UserInfo: 指定撤销链接的用户指定撤销链接的用户信息，包含姓名、证件类型、证件号码。

        :type UserInfo: :class:`tencentcloud.ess.v20201111.models.UserThreeFactor`
        """
        self._Operator = None
        self._SceneKey = None
        self._UserInfo = None

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
        


class CancelUserAutoSignEnableUrlResponse(AbstractModel):
    """CancelUserAutoSignEnableUrl返回参数结构体

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


class CcInfo(AbstractModel):
    """抄送信息

    """

    def __init__(self):
        r"""
        :param _Mobile: 被抄送人手机号，11位数字
        :type Mobile: str
        :param _Name: 被抄送人姓名
        :type Name: str
        :param _CcType: 被抄送人类型,
0--个人
1--员工
        :type CcType: int
        :param _CcPermission: 被抄送人权限
0--可查看
1--可查看也可下载
        :type CcPermission: int
        :param _NotifyType: 关注方通知类型：sms--短信，none--不通知
        :type NotifyType: str
        """
        self._Mobile = None
        self._Name = None
        self._CcType = None
        self._CcPermission = None
        self._NotifyType = None

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

    @property
    def NotifyType(self):
        return self._NotifyType

    @NotifyType.setter
    def NotifyType(self, NotifyType):
        self._NotifyType = NotifyType


    def _deserialize(self, params):
        self._Mobile = params.get("Mobile")
        self._Name = params.get("Name")
        self._CcType = params.get("CcType")
        self._CcPermission = params.get("CcPermission")
        self._NotifyType = params.get("NotifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Component(AbstractModel):
    """模板控件信息

    """

    def __init__(self):
        r"""
        :param _ComponentType: 如果是Component填写控件类型，则可选的字段为：
TEXT - 普通文本控件，输入文本字符串；
MULTI_LINE_TEXT - 多行文本控件，输入文本字符串；
CHECK_BOX - 勾选框控件，若选中填写ComponentValue 填写 true或者 false 字符串；
FILL_IMAGE - 图片控件，ComponentValue 填写图片的资源 ID；
DYNAMIC_TABLE - 动态表格控件；
ATTACHMENT - 附件控件,ComponentValue 填写附件图片的资源 ID列表，以逗号分隔；
SELECTOR - 选择器控件，ComponentValue填写选择的字符串内容；
DATE - 日期控件；默认是格式化为xxxx年xx月xx日字符串；
DISTRICT - 省市区行政区控件，ComponentValue填写省市区行政区字符串内容；

如果是SignComponent签署控件类型，则可选的字段为
SIGN_SEAL - 签署印章控件；
SIGN_DATE - 签署日期控件；
SIGN_SIGNATURE - 用户签名控件；
SIGN_PERSONAL_SEAL - 个人签署印章控件（使用文件发起暂不支持此类型）；
SIGN_PAGING_SEAL - 骑缝章；若文件发起，需要对应填充ComponentPosY、ComponentWidth、ComponentHeight
SIGN_OPINION - 签署意见控件，用户需要根据配置的签署意见内容，完成对意见内容的确认；
SIGN_LEGAL_PERSON_SEAL - 企业法定代表人控件。

表单域的控件不能作为印章和签名控件
        :type ComponentType: str
        :param _FileIndex: 控件所属文件的序号（取值为：0-N）。目前单文件的情况下，值是0
        :type FileIndex: int
        :param _ComponentHeight: 参数控件高度，单位pt
        :type ComponentHeight: float
        :param _ComponentWidth: 参数控件宽度，单位pt
        :type ComponentWidth: float
        :param _ComponentPage: 参数控件所在页码，取值为：1-N
        :type ComponentPage: int
        :param _ComponentPosX: 参数控件X位置，单位pt
        :type ComponentPosX: float
        :param _ComponentPosY: 参数控件Y位置，单位pt
        :type ComponentPosY: float
        :param _ComponentId: 查询时返回控件唯一Id。使用文件发起合同时用于GenerateMode==KEYWORD 指定关键字
        :type ComponentId: str
        :param _ComponentName: 查询时返回控件名。使用文件发起合同时用于GenerateMode==FIELD 指定表单域名称
        :type ComponentName: str
        :param _ComponentRequired: 是否必选，默认为false
        :type ComponentRequired: bool
        :param _ComponentRecipientId: 控件关联的签署人ID
        :type ComponentRecipientId: str
        :param _ComponentExtra: 扩展参数：
为JSON格式。

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
参数样例：    "ComponentExtra": "{\"Format\":“yyyy m d”,\"FontSize\":12,\"Gaps\":\"2,2\", \"FontAlign\":\"Right\"}"

ComponentType为SIGN_SEAL类型时，支持以下参数：
1.PageRanges：PageRange的数组，通过PageRanges属性设置该印章在PDF所有页面上盖章（适用于标书在所有页面盖章的情况）
参数样例："ComponentExtra":"{\"PageRanges\":[{\"BeginPage\":1,\"EndPage\":-1}]}"
        :type ComponentExtra: str
        :param _IsFormType: 是否是表单域类型，默认不false-不是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFormType: bool
        :param _ComponentValue: 控件填充vaule，ComponentType和传入值类型对应关系：
TEXT - 文本内容
MULTI_LINE_TEXT - 文本内容
CHECK_BOX - true/false
FILL_IMAGE、ATTACHMENT - 附件的FileId，需要通过UploadFiles接口上传获取
SELECTOR - 选项值
DYNAMIC_TABLE - 传入json格式的表格内容，具体见数据结构FlowInfo：https://cloud.tencent.com/document/api/1420/61525#FlowInfo
DATE - 默认是格式化为xxxx年xx月xx日
SIGN_SEAL - 印章ID，于控制台查询获取
SIGN_PAGING_SEAL - 可以指定印章ID，于控制台查询获取

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
        :param _GenerateMode: NORMAL 正常模式，使用坐标制定签署控件位置
FIELD 表单域，需使用ComponentName指定表单域名称
KEYWORD 关键字，使用ComponentId指定关键字
        :type GenerateMode: str
        :param _ComponentDateFontSize: 日期签署控件的字号，默认为 12
        :type ComponentDateFontSize: int
        :param _ChannelComponentId: 第三方应用集成平台模板控件 id 标识
        :type ChannelComponentId: str
        :param _OffsetX: 指定关键字时横坐标偏移量，单位pt
注意：此字段可能返回 null，表示取不到有效值。
        :type OffsetX: float
        :param _OffsetY: 指定关键字时纵坐标偏移量，单位pt
注意：此字段可能返回 null，表示取不到有效值。
        :type OffsetY: float
        :param _ChannelComponentSource: 第三方应用集成中子客企业控件来源。0-平台指定；1-用户自定义
        :type ChannelComponentSource: int
        :param _KeywordOrder: 指定关键字排序规则，Positive-正序，Reverse-倒序。传入Positive时会根据关键字在PDF文件内的顺序进行排列。在指定KeywordIndexes时，0代表在PDF内查找内容时，查找到的第一个关键字。
传入Reverse时会根据关键字在PDF文件内的反序进行排列。在指定KeywordIndexes时，0代表在PDF内查找内容时，查找到的最后一个关键字。
        :type KeywordOrder: str
        :param _KeywordPage: 指定关键字页码，可选参数，指定页码后，将只在指定的页码内查找关键字，非该页码的关键字将不会查询出来
        :type KeywordPage: int
        :param _RelativeLocation: 关键字位置模式，Middle-居中，Below-正下方，Right-正右方，LowerRight-右上角，UpperRight-右下角。示例：如果设置Middle的关键字盖章，则印章的中心会和关键字的中心重合，如果设置Below，则印章在关键字的正下方
        :type RelativeLocation: str
        :param _KeywordIndexes: 关键字索引，可选参数，如果一个关键字在PDF文件中存在多个，可以通过关键字索引指定使用第几个关键字作为最后的结果，可指定多个索引。示例：[0,2]，说明使用PDF文件内第1个和第3个关键字位置。
        :type KeywordIndexes: list of int
        """
        self._ComponentType = None
        self._FileIndex = None
        self._ComponentHeight = None
        self._ComponentWidth = None
        self._ComponentPage = None
        self._ComponentPosX = None
        self._ComponentPosY = None
        self._ComponentId = None
        self._ComponentName = None
        self._ComponentRequired = None
        self._ComponentRecipientId = None
        self._ComponentExtra = None
        self._IsFormType = None
        self._ComponentValue = None
        self._GenerateMode = None
        self._ComponentDateFontSize = None
        self._ChannelComponentId = None
        self._OffsetX = None
        self._OffsetY = None
        self._ChannelComponentSource = None
        self._KeywordOrder = None
        self._KeywordPage = None
        self._RelativeLocation = None
        self._KeywordIndexes = None

    @property
    def ComponentType(self):
        return self._ComponentType

    @ComponentType.setter
    def ComponentType(self, ComponentType):
        self._ComponentType = ComponentType

    @property
    def FileIndex(self):
        return self._FileIndex

    @FileIndex.setter
    def FileIndex(self, FileIndex):
        self._FileIndex = FileIndex

    @property
    def ComponentHeight(self):
        return self._ComponentHeight

    @ComponentHeight.setter
    def ComponentHeight(self, ComponentHeight):
        self._ComponentHeight = ComponentHeight

    @property
    def ComponentWidth(self):
        return self._ComponentWidth

    @ComponentWidth.setter
    def ComponentWidth(self, ComponentWidth):
        self._ComponentWidth = ComponentWidth

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
    def ComponentExtra(self):
        return self._ComponentExtra

    @ComponentExtra.setter
    def ComponentExtra(self, ComponentExtra):
        self._ComponentExtra = ComponentExtra

    @property
    def IsFormType(self):
        return self._IsFormType

    @IsFormType.setter
    def IsFormType(self, IsFormType):
        self._IsFormType = IsFormType

    @property
    def ComponentValue(self):
        return self._ComponentValue

    @ComponentValue.setter
    def ComponentValue(self, ComponentValue):
        self._ComponentValue = ComponentValue

    @property
    def GenerateMode(self):
        return self._GenerateMode

    @GenerateMode.setter
    def GenerateMode(self, GenerateMode):
        self._GenerateMode = GenerateMode

    @property
    def ComponentDateFontSize(self):
        return self._ComponentDateFontSize

    @ComponentDateFontSize.setter
    def ComponentDateFontSize(self, ComponentDateFontSize):
        self._ComponentDateFontSize = ComponentDateFontSize

    @property
    def ChannelComponentId(self):
        return self._ChannelComponentId

    @ChannelComponentId.setter
    def ChannelComponentId(self, ChannelComponentId):
        self._ChannelComponentId = ChannelComponentId

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
    def ChannelComponentSource(self):
        return self._ChannelComponentSource

    @ChannelComponentSource.setter
    def ChannelComponentSource(self, ChannelComponentSource):
        self._ChannelComponentSource = ChannelComponentSource

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


    def _deserialize(self, params):
        self._ComponentType = params.get("ComponentType")
        self._FileIndex = params.get("FileIndex")
        self._ComponentHeight = params.get("ComponentHeight")
        self._ComponentWidth = params.get("ComponentWidth")
        self._ComponentPage = params.get("ComponentPage")
        self._ComponentPosX = params.get("ComponentPosX")
        self._ComponentPosY = params.get("ComponentPosY")
        self._ComponentId = params.get("ComponentId")
        self._ComponentName = params.get("ComponentName")
        self._ComponentRequired = params.get("ComponentRequired")
        self._ComponentRecipientId = params.get("ComponentRecipientId")
        self._ComponentExtra = params.get("ComponentExtra")
        self._IsFormType = params.get("IsFormType")
        self._ComponentValue = params.get("ComponentValue")
        self._GenerateMode = params.get("GenerateMode")
        self._ComponentDateFontSize = params.get("ComponentDateFontSize")
        self._ChannelComponentId = params.get("ChannelComponentId")
        self._OffsetX = params.get("OffsetX")
        self._OffsetY = params.get("OffsetY")
        self._ChannelComponentSource = params.get("ChannelComponentSource")
        self._KeywordOrder = params.get("KeywordOrder")
        self._KeywordPage = params.get("KeywordPage")
        self._RelativeLocation = params.get("RelativeLocation")
        self._KeywordIndexes = params.get("KeywordIndexes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchCancelFlowUrlRequest(AbstractModel):
    """CreateBatchCancelFlowUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowIds: 需要执行撤回的签署流程id数组，最多100个
        :type FlowIds: list of str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填

        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._FlowIds = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowIds = params.get("FlowIds")
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
        


class CreateBatchCancelFlowUrlResponse(AbstractModel):
    """CreateBatchCancelFlowUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchCancelFlowUrl: 批量撤回签署流程链接
        :type BatchCancelFlowUrl: str
        :param _FailMessages: 签署流程撤回失败信息
        :type FailMessages: list of str
        :param _UrlExpireOn: 签署连接过期时间字符串：年月日-时分秒
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


class CreateChannelSubOrganizationModifyQrCodeRequest(AbstractModel):
    """CreateChannelSubOrganizationModifyQrCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息，userId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _ApplicationId: 应用编号
        :type ApplicationId: str
        """
        self._Operator = None
        self._ApplicationId = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateChannelSubOrganizationModifyQrCodeResponse(AbstractModel):
    """CreateChannelSubOrganizationModifyQrCode返回参数结构体

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


class CreateConvertTaskApiRequest(AbstractModel):
    """CreateConvertTaskApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceType: 资源类型 支持doc,docx,html,xls,xlsx,jpg,jpeg,png,bmp文件类型
        :type ResourceType: str
        :param _ResourceName: 资源名称，长度限制为256字符
        :type ResourceName: str
        :param _ResourceId: 资源Id，通过UploadFiles获取
        :type ResourceId: str
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Agent: 应用号信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Organization: 暂未开放
        :type Organization: :class:`tencentcloud.ess.v20201111.models.OrganizationInfo`
        """
        self._ResourceType = None
        self._ResourceName = None
        self._ResourceId = None
        self._Operator = None
        self._Agent = None
        self._Organization = None

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
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Agent(self):
        warnings.warn("parameter `Agent` is deprecated", DeprecationWarning) 

        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        warnings.warn("parameter `Agent` is deprecated", DeprecationWarning) 

        self._Agent = Agent

    @property
    def Organization(self):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        self._Organization = Organization


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._ResourceName = params.get("ResourceName")
        self._ResourceId = params.get("ResourceId")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
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
        


class CreateConvertTaskApiResponse(AbstractModel):
    """CreateConvertTaskApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 转换任务Id
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


class CreateDocumentRequest(AbstractModel):
    """CreateDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填。支持填入集团子公司经办人 userId代发合同。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowId: 签署流程编号,由CreateFlow接口返回
        :type FlowId: str
        :param _TemplateId: 用户上传的模板ID
        :type TemplateId: str
        :param _FileNames: 文件名列表，单个文件名最大长度200个字符，暂时仅支持单文件发起。设置后流程对应的文件名称当前设置的值。
        :type FileNames: list of str
        :param _FormFields: 内容控件信息数组
        :type FormFields: list of FormField
        :param _NeedPreview: 是否需要生成预览文件 默认不生成；
预览链接有效期300秒；
        :type NeedPreview: bool
        :param _PreviewType: 预览链接类型 默认:0-文件流, 1- H5链接 注意:此参数在NeedPreview 为true 时有效,
        :type PreviewType: int
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _ClientToken: 客户端Token，保持接口幂等性,最大长度64个字符
        :type ClientToken: str
        """
        self._Operator = None
        self._FlowId = None
        self._TemplateId = None
        self._FileNames = None
        self._FormFields = None
        self._NeedPreview = None
        self._PreviewType = None
        self._Agent = None
        self._ClientToken = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def FileNames(self):
        return self._FileNames

    @FileNames.setter
    def FileNames(self, FileNames):
        self._FileNames = FileNames

    @property
    def FormFields(self):
        return self._FormFields

    @FormFields.setter
    def FormFields(self, FormFields):
        self._FormFields = FormFields

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
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowId = params.get("FlowId")
        self._TemplateId = params.get("TemplateId")
        self._FileNames = params.get("FileNames")
        if params.get("FormFields") is not None:
            self._FormFields = []
            for item in params.get("FormFields"):
                obj = FormField()
                obj._deserialize(item)
                self._FormFields.append(obj)
        self._NeedPreview = params.get("NeedPreview")
        self._PreviewType = params.get("PreviewType")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._ClientToken = params.get("ClientToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDocumentResponse(AbstractModel):
    """CreateDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DocumentId: 签署流程电子文档ID
        :type DocumentId: str
        :param _PreviewFileUrl: 签署流程文件的预览地址, 5分钟内有效。仅当NeedPreview为true 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewFileUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DocumentId = None
        self._PreviewFileUrl = None
        self._RequestId = None

    @property
    def DocumentId(self):
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId

    @property
    def PreviewFileUrl(self):
        return self._PreviewFileUrl

    @PreviewFileUrl.setter
    def PreviewFileUrl(self, PreviewFileUrl):
        self._PreviewFileUrl = PreviewFileUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DocumentId = params.get("DocumentId")
        self._PreviewFileUrl = params.get("PreviewFileUrl")
        self._RequestId = params.get("RequestId")


class CreateEmbedWebUrlRequest(AbstractModel):
    """CreateEmbedWebUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作者信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _EmbedType: WEB嵌入资源类型。
<br/>CREATE_SEAL: 创建印章
<br/>PREVIEW_SEAL_LIST：预览印章列表
<br/>PREVIEW_SEAL_DETAIL：预览印章详情
<br/>EXTEND_SERVICE：拓展服务

        :type EmbedType: str
        :param _BusinessId: WEB嵌入的业务资源ID
<br/>PREVIEW_SEAL_DETAIL，必填，取值为印章id
        :type BusinessId: str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Reviewer: 抄送方信息
        :type Reviewer: :class:`tencentcloud.ess.v20201111.models.ReviewerInfo`
        """
        self._Operator = None
        self._EmbedType = None
        self._BusinessId = None
        self._Agent = None
        self._Reviewer = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

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
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def Reviewer(self):
        return self._Reviewer

    @Reviewer.setter
    def Reviewer(self, Reviewer):
        self._Reviewer = Reviewer


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._EmbedType = params.get("EmbedType")
        self._BusinessId = params.get("BusinessId")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("Reviewer") is not None:
            self._Reviewer = ReviewerInfo()
            self._Reviewer._deserialize(params.get("Reviewer"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmbedWebUrlResponse(AbstractModel):
    """CreateEmbedWebUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WebUrl: 嵌入的web链接，有效期：5分钟
EmbedType=PREVIEW_CC_FLOW，该url为h5链接
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


class CreateFlowApproversRequest(AbstractModel):
    """CreateFlowApprovers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowId: 签署流程编号
        :type FlowId: str
        :param _Approvers: 补充签署人信息
        :type Approvers: list of FillApproverInfo
        :param _Initiator: 企微消息中的发起人
        :type Initiator: str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作


        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._FlowId = None
        self._Approvers = None
        self._Initiator = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

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
    def Initiator(self):
        return self._Initiator

    @Initiator.setter
    def Initiator(self, Initiator):
        self._Initiator = Initiator

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowId = params.get("FlowId")
        if params.get("Approvers") is not None:
            self._Approvers = []
            for item in params.get("Approvers"):
                obj = FillApproverInfo()
                obj._deserialize(item)
                self._Approvers.append(obj)
        self._Initiator = params.get("Initiator")
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
        


class CreateFlowApproversResponse(AbstractModel):
    """CreateFlowApprovers返回参数结构体

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


class CreateFlowByFilesRequest(AbstractModel):
    """CreateFlowByFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填。支持填入集团子公司经办人 userId 代发合同
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowName: 签署流程名称,最大长度200个字符
        :type FlowName: str
        :param _Approvers: 签署参与者信息，最大限制50方
        :type Approvers: list of ApproverInfo
        :param _FileIds: 签署pdf文件的资源编号列表，通过UploadFiles接口获取，暂时仅支持单文件发起
        :type FileIds: list of str
        :param _FlowType: 签署流程的类型(如销售合同/入职合同等)，最大长度200个字符
        :type FlowType: str
        :param _Components: 经办人内容控件配置
        :type Components: list of Component
        :param _CcInfos: 被抄送人的信息列表。
注:此功能为白名单功能，若有需要，请联系电子签客服开白使用
        :type CcInfos: list of CcInfo
        :param _NeedPreview: 是否需要预览，true：预览模式，false：非预览（默认）；
预览链接有效期300秒；

注：如果使用“预览模式”，出参会返回合同预览链接 PreviewUrl，不会正式发起合同，且出参不会返回签署流程编号 FlowId；如果使用“非预览”，则会正常返回签署流程编号 FlowId，不会生成合同预览链接 PreviewUrl。
        :type NeedPreview: bool
        :param _PreviewType: 预览链接类型 默认:0-文件流, 1- H5链接 注意:此参数在NeedPreview 为true 时有效,
        :type PreviewType: int
        :param _Deadline: 签署流程的签署截止时间。
值为unix时间戳,精确到秒,不传默认为当前时间一年后
        :type Deadline: int
        :param _RemindedOn: 合同到期提醒时间戳，单位秒。设定该值后，可以提前进行到期通知，方便客户处理合同到期事务，如合同续签等。该值支持的范围是从发起时间起到往后的10年内。仅合同发起方企业的发起人可以编辑修改。
        :type RemindedOn: int
        :param _Unordered: 发送类型：
true：无序签
false：有序签
注：默认为false（有序签）
        :type Unordered: bool
        :param _CustomShowMap: 合同显示的页卡模板，说明：只支持{合同名称}, {发起方企业}, {发起方姓名}, {签署方N企业}, {签署方N姓名}，且N不能超过签署人的数量，N从1开始
        :type CustomShowMap: str
        :param _NeedSignReview: 发起方企业的签署人进行签署操作是否需要企业内部审批。使用此功能需要发起方企业有参与签署。
若设置为true，审核结果需通过接口 CreateFlowSignReview 通知电子签，审核通过后，发起方企业签署人方可进行签署操作，否则会阻塞其签署操作。

注：企业可以通过此功能与企业内部的审批流程进行关联，支持手动、静默签署合同。
        :type NeedSignReview: bool
        :param _UserData: 用户自定义字段，回调的时候会进行透传，长度需要小于20480
        :type UserData: str
        :param _ApproverVerifyType: 签署人校验方式
VerifyCheck: 人脸识别（默认）
MobileCheck：手机号验证
参数说明：可选人脸识别或手机号验证两种方式，若选择后者，未实名个人签署方在签署合同时，无需经过实名认证和意愿确认两次人脸识别，该能力仅适用于个人签署方。
        :type ApproverVerifyType: str
        :param _FlowDescription: 签署流程描述,最大长度1000个字符
        :type FlowDescription: str
        :param _SignBeanTag: 标识是否允许发起后添加控件。0为不允许1为允许。如果为1，创建的时候不能有签署控件，只能创建后添加。注意发起后添加控件功能不支持添加骑缝章和签批控件
        :type SignBeanTag: int
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _CcNotifyType: 给关注人发送短信通知的类型，0-合同发起时通知 1-签署完成后通知
        :type CcNotifyType: int
        :param _AutoSignScene: 个人自动签场景。发起自动签署时，需设置对应自动签署场景，目前仅支持场景：处方单-E_PRESCRIPTION_AUTO_SIGN
        :type AutoSignScene: str
        """
        self._Operator = None
        self._FlowName = None
        self._Approvers = None
        self._FileIds = None
        self._FlowType = None
        self._Components = None
        self._CcInfos = None
        self._NeedPreview = None
        self._PreviewType = None
        self._Deadline = None
        self._RemindedOn = None
        self._Unordered = None
        self._CustomShowMap = None
        self._NeedSignReview = None
        self._UserData = None
        self._ApproverVerifyType = None
        self._FlowDescription = None
        self._SignBeanTag = None
        self._Agent = None
        self._CcNotifyType = None
        self._AutoSignScene = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def Approvers(self):
        return self._Approvers

    @Approvers.setter
    def Approvers(self, Approvers):
        self._Approvers = Approvers

    @property
    def FileIds(self):
        return self._FileIds

    @FileIds.setter
    def FileIds(self, FileIds):
        self._FileIds = FileIds

    @property
    def FlowType(self):
        return self._FlowType

    @FlowType.setter
    def FlowType(self, FlowType):
        self._FlowType = FlowType

    @property
    def Components(self):
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def CcInfos(self):
        return self._CcInfos

    @CcInfos.setter
    def CcInfos(self, CcInfos):
        self._CcInfos = CcInfos

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
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def RemindedOn(self):
        return self._RemindedOn

    @RemindedOn.setter
    def RemindedOn(self, RemindedOn):
        self._RemindedOn = RemindedOn

    @property
    def Unordered(self):
        return self._Unordered

    @Unordered.setter
    def Unordered(self, Unordered):
        self._Unordered = Unordered

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

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def ApproverVerifyType(self):
        return self._ApproverVerifyType

    @ApproverVerifyType.setter
    def ApproverVerifyType(self, ApproverVerifyType):
        self._ApproverVerifyType = ApproverVerifyType

    @property
    def FlowDescription(self):
        return self._FlowDescription

    @FlowDescription.setter
    def FlowDescription(self, FlowDescription):
        self._FlowDescription = FlowDescription

    @property
    def SignBeanTag(self):
        return self._SignBeanTag

    @SignBeanTag.setter
    def SignBeanTag(self, SignBeanTag):
        self._SignBeanTag = SignBeanTag

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

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
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowName = params.get("FlowName")
        if params.get("Approvers") is not None:
            self._Approvers = []
            for item in params.get("Approvers"):
                obj = ApproverInfo()
                obj._deserialize(item)
                self._Approvers.append(obj)
        self._FileIds = params.get("FileIds")
        self._FlowType = params.get("FlowType")
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self._Components.append(obj)
        if params.get("CcInfos") is not None:
            self._CcInfos = []
            for item in params.get("CcInfos"):
                obj = CcInfo()
                obj._deserialize(item)
                self._CcInfos.append(obj)
        self._NeedPreview = params.get("NeedPreview")
        self._PreviewType = params.get("PreviewType")
        self._Deadline = params.get("Deadline")
        self._RemindedOn = params.get("RemindedOn")
        self._Unordered = params.get("Unordered")
        self._CustomShowMap = params.get("CustomShowMap")
        self._NeedSignReview = params.get("NeedSignReview")
        self._UserData = params.get("UserData")
        self._ApproverVerifyType = params.get("ApproverVerifyType")
        self._FlowDescription = params.get("FlowDescription")
        self._SignBeanTag = params.get("SignBeanTag")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._CcNotifyType = params.get("CcNotifyType")
        self._AutoSignScene = params.get("AutoSignScene")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowByFilesResponse(AbstractModel):
    """CreateFlowByFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 签署流程编号。

注：如入参 是否需要预览 NeedPreview 设置为 true，不会正式发起合同，此处不会有值返回；如入参 是否需要预览 NeedPreview 设置为 false，此处会正常返回签署流程编号 FlowId。
        :type FlowId: str
        :param _PreviewUrl: 合同预览链接。

注：如入参 是否需要预览 NeedPreview 设置为 true，会开启“预览模式”，此处会返回预览链接；如入参 是否需要预览 NeedPreview 设置为 false，此处不会有值返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._PreviewUrl = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def PreviewUrl(self):
        return self._PreviewUrl

    @PreviewUrl.setter
    def PreviewUrl(self, PreviewUrl):
        self._PreviewUrl = PreviewUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._PreviewUrl = params.get("PreviewUrl")
        self._RequestId = params.get("RequestId")


class CreateFlowEvidenceReportRequest(AbstractModel):
    """CreateFlowEvidenceReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowId: 签署流程编号
        :type FlowId: str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填

        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._FlowId = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

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


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowId = params.get("FlowId")
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
        


class CreateFlowEvidenceReportResponse(AbstractModel):
    """CreateFlowEvidenceReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportId: 出证报告 ID，用于查询出证报告DescribeFlowEvidenceReport接口时用到
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportId: str
        :param _Status: 执行中：EvidenceStatusExecuting
成功：EvidenceStatusSuccess
失败：EvidenceStatusFailed
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


class CreateFlowGroupByFilesRequest(AbstractModel):
    """CreateFlowGroupByFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填。支持填入集团子公司经办人 userId 代发合同
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowGroupName: 合同（流程）组名称,最大长度200个字符
        :type FlowGroupName: str
        :param _FlowGroupInfos: 合同（流程）组的子合同信息，支持2-50个子合同
        :type FlowGroupInfos: list of FlowGroupInfo
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _FlowGroupOptions: 合同（流程）组的配置项信息。包括是否通知本企业签署方，是否通知其他签署方
        :type FlowGroupOptions: :class:`tencentcloud.ess.v20201111.models.FlowGroupOptions`
        """
        self._Operator = None
        self._FlowGroupName = None
        self._FlowGroupInfos = None
        self._Agent = None
        self._FlowGroupOptions = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def FlowGroupName(self):
        return self._FlowGroupName

    @FlowGroupName.setter
    def FlowGroupName(self, FlowGroupName):
        self._FlowGroupName = FlowGroupName

    @property
    def FlowGroupInfos(self):
        return self._FlowGroupInfos

    @FlowGroupInfos.setter
    def FlowGroupInfos(self, FlowGroupInfos):
        self._FlowGroupInfos = FlowGroupInfos

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowGroupOptions(self):
        return self._FlowGroupOptions

    @FlowGroupOptions.setter
    def FlowGroupOptions(self, FlowGroupOptions):
        self._FlowGroupOptions = FlowGroupOptions


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowGroupName = params.get("FlowGroupName")
        if params.get("FlowGroupInfos") is not None:
            self._FlowGroupInfos = []
            for item in params.get("FlowGroupInfos"):
                obj = FlowGroupInfo()
                obj._deserialize(item)
                self._FlowGroupInfos.append(obj)
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("FlowGroupOptions") is not None:
            self._FlowGroupOptions = FlowGroupOptions()
            self._FlowGroupOptions._deserialize(params.get("FlowGroupOptions"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowGroupByFilesResponse(AbstractModel):
    """CreateFlowGroupByFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowGroupId: 合同(流程)组的合同组Id
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowGroupId: str
        :param _FlowIds: 合同(流程)组中子合同列表.
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


class CreateFlowGroupByTemplatesRequest(AbstractModel):
    """CreateFlowGroupByTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填。支持填入集团子公司经办人 userId 代发合同
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowGroupName: 合同组名称,最大长度200个字符
        :type FlowGroupName: str
        :param _FlowGroupInfos: 合同组的子合同信息，支持2-50个子合同
        :type FlowGroupInfos: list of FlowGroupInfo
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _FlowGroupOptions: 合同组的配置信息。包括是否通知本企业签署方，是否通知其他签署方
        :type FlowGroupOptions: :class:`tencentcloud.ess.v20201111.models.FlowGroupOptions`
        """
        self._Operator = None
        self._FlowGroupName = None
        self._FlowGroupInfos = None
        self._Agent = None
        self._FlowGroupOptions = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def FlowGroupName(self):
        return self._FlowGroupName

    @FlowGroupName.setter
    def FlowGroupName(self, FlowGroupName):
        self._FlowGroupName = FlowGroupName

    @property
    def FlowGroupInfos(self):
        return self._FlowGroupInfos

    @FlowGroupInfos.setter
    def FlowGroupInfos(self, FlowGroupInfos):
        self._FlowGroupInfos = FlowGroupInfos

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowGroupOptions(self):
        return self._FlowGroupOptions

    @FlowGroupOptions.setter
    def FlowGroupOptions(self, FlowGroupOptions):
        self._FlowGroupOptions = FlowGroupOptions


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowGroupName = params.get("FlowGroupName")
        if params.get("FlowGroupInfos") is not None:
            self._FlowGroupInfos = []
            for item in params.get("FlowGroupInfos"):
                obj = FlowGroupInfo()
                obj._deserialize(item)
                self._FlowGroupInfos.append(obj)
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("FlowGroupOptions") is not None:
            self._FlowGroupOptions = FlowGroupOptions()
            self._FlowGroupOptions._deserialize(params.get("FlowGroupOptions"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowGroupByTemplatesResponse(AbstractModel):
    """CreateFlowGroupByTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowGroupId: 合同(流程)组的合同组Id
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowGroupId: str
        :param _FlowIds: 合同(流程)组中子合同列表.
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


class CreateFlowRemindsRequest(AbstractModel):
    """CreateFlowReminds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowIds: 需要执行催办的签署流程id数组，最多100个
        :type FlowIds: list of str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._FlowIds = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowIds = params.get("FlowIds")
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
        


class CreateFlowRemindsResponse(AbstractModel):
    """CreateFlowReminds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RemindFlowRecords: 催办合同详情列表
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


class CreateFlowRequest(AbstractModel):
    """CreateFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填。支持填入集团子公司经办人 userId代发合同。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowName: 签署流程名称,最大长度200个字符
        :type FlowName: str
        :param _Approvers: 签署流程参与者信息，最大限制50方
        :type Approvers: list of FlowCreateApprover
        :param _FlowType: 签署流程的类型(如销售合同/入职合同等)，最大长度200个字符
        :type FlowType: str
        :param _ClientToken: 客户端Token，保持接口幂等性,最大长度64个字符
        :type ClientToken: str
        :param _DeadLine: 签署流程的签署截止时间。
值为unix时间戳,精确到秒,不传默认为当前时间一年后
        :type DeadLine: int
        :param _RemindedOn: 合同到期提醒时间戳，单位秒。设定该值后，可以提前进行到期通知，方便客户处理合同到期事务，如合同续签等。该值支持的范围是从发起时间起到往后的10年内。仅合同发起方企业的发起人可以编辑修改。
        :type RemindedOn: int
        :param _UserData: 用户自定义字段，回调的时候会进行透传，长度需要小于20480
        :type UserData: str
        :param _FlowDescription: 签署流程描述,最大长度1000个字符
        :type FlowDescription: str
        :param _Unordered: 发送类型：
true：无序签
false：有序签
注：默认为false（有序签），请和模板中的配置保持一致
        :type Unordered: bool
        :param _CustomShowMap: 合同显示的页卡模板，说明：只支持{合同名称}, {发起方企业}, {发起方姓名}, {签署方N企业}, {签署方N姓名}，且N不能超过签署人的数量，N从1开始
        :type CustomShowMap: str
        :param _NeedSignReview: 发起方企业的签署人进行签署操作是否需要企业内部审批。使用此功能需要发起方企业有参与签署。
若设置为true，审核结果需通过接口 CreateFlowSignReview 通知电子签，审核通过后，发起方企业签署人方可进行签署操作，否则会阻塞其签署操作。

注：企业可以通过此功能与企业内部的审批流程进行关联，支持手动、静默签署合同。
        :type NeedSignReview: bool
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _CcInfos: 被抄送人的信息列表。
注: 此功能为白名单功能，若有需要，请联系电子签客服开白使用。
        :type CcInfos: list of CcInfo
        :param _AutoSignScene: 个人自动签场景。发起自动签署时，需设置对应自动签署场景，目前仅支持场景：处方单-E_PRESCRIPTION_AUTO_SIGN
        :type AutoSignScene: str
        :param _RelatedFlowId: 暂未开放
        :type RelatedFlowId: str
        :param _CallbackUrl: 暂未开放
        :type CallbackUrl: str
        """
        self._Operator = None
        self._FlowName = None
        self._Approvers = None
        self._FlowType = None
        self._ClientToken = None
        self._DeadLine = None
        self._RemindedOn = None
        self._UserData = None
        self._FlowDescription = None
        self._Unordered = None
        self._CustomShowMap = None
        self._NeedSignReview = None
        self._Agent = None
        self._CcInfos = None
        self._AutoSignScene = None
        self._RelatedFlowId = None
        self._CallbackUrl = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def Approvers(self):
        return self._Approvers

    @Approvers.setter
    def Approvers(self, Approvers):
        self._Approvers = Approvers

    @property
    def FlowType(self):
        return self._FlowType

    @FlowType.setter
    def FlowType(self, FlowType):
        self._FlowType = FlowType

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DeadLine(self):
        return self._DeadLine

    @DeadLine.setter
    def DeadLine(self, DeadLine):
        self._DeadLine = DeadLine

    @property
    def RemindedOn(self):
        return self._RemindedOn

    @RemindedOn.setter
    def RemindedOn(self, RemindedOn):
        self._RemindedOn = RemindedOn

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def FlowDescription(self):
        return self._FlowDescription

    @FlowDescription.setter
    def FlowDescription(self, FlowDescription):
        self._FlowDescription = FlowDescription

    @property
    def Unordered(self):
        return self._Unordered

    @Unordered.setter
    def Unordered(self, Unordered):
        self._Unordered = Unordered

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

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def CcInfos(self):
        return self._CcInfos

    @CcInfos.setter
    def CcInfos(self, CcInfos):
        self._CcInfos = CcInfos

    @property
    def AutoSignScene(self):
        return self._AutoSignScene

    @AutoSignScene.setter
    def AutoSignScene(self, AutoSignScene):
        self._AutoSignScene = AutoSignScene

    @property
    def RelatedFlowId(self):
        warnings.warn("parameter `RelatedFlowId` is deprecated", DeprecationWarning) 

        return self._RelatedFlowId

    @RelatedFlowId.setter
    def RelatedFlowId(self, RelatedFlowId):
        warnings.warn("parameter `RelatedFlowId` is deprecated", DeprecationWarning) 

        self._RelatedFlowId = RelatedFlowId

    @property
    def CallbackUrl(self):
        warnings.warn("parameter `CallbackUrl` is deprecated", DeprecationWarning) 

        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        warnings.warn("parameter `CallbackUrl` is deprecated", DeprecationWarning) 

        self._CallbackUrl = CallbackUrl


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowName = params.get("FlowName")
        if params.get("Approvers") is not None:
            self._Approvers = []
            for item in params.get("Approvers"):
                obj = FlowCreateApprover()
                obj._deserialize(item)
                self._Approvers.append(obj)
        self._FlowType = params.get("FlowType")
        self._ClientToken = params.get("ClientToken")
        self._DeadLine = params.get("DeadLine")
        self._RemindedOn = params.get("RemindedOn")
        self._UserData = params.get("UserData")
        self._FlowDescription = params.get("FlowDescription")
        self._Unordered = params.get("Unordered")
        self._CustomShowMap = params.get("CustomShowMap")
        self._NeedSignReview = params.get("NeedSignReview")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("CcInfos") is not None:
            self._CcInfos = []
            for item in params.get("CcInfos"):
                obj = CcInfo()
                obj._deserialize(item)
                self._CcInfos.append(obj)
        self._AutoSignScene = params.get("AutoSignScene")
        self._RelatedFlowId = params.get("RelatedFlowId")
        self._CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowResponse(AbstractModel):
    """CreateFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 签署流程编号
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


class CreateFlowSignReviewRequest(AbstractModel):
    """CreateFlowSignReview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowId: 签署流程编号
        :type FlowId: str
        :param _ReviewType: 企业内部审核结果
PASS: 通过 
REJECT: 拒绝
        :type ReviewType: str
        :param _ReviewMessage: 审核原因 
当ReviewType 是REJECT 时此字段必填,字符串长度不超过200
        :type ReviewMessage: str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _RecipientId: 审核签署节点使用 非必填 如果填写则审核该签署节点。给个人审核时必填。
        :type RecipientId: str
        :param _OperateType: 操作类型：（接口通过该字段区分操作类型）

SignReview:签署审核
CreateReview:发起审核

默认：SignReview；SignReview:签署审核

该字段不传或者为空，则默认为SignReview签署审核，走签署审核流程
若发起个人审核，则指定该字段为：SignReview（注意，给个人审核时，需联系客户经理开白使用）
        :type OperateType: str
        """
        self._Operator = None
        self._FlowId = None
        self._ReviewType = None
        self._ReviewMessage = None
        self._Agent = None
        self._RecipientId = None
        self._OperateType = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

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
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

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
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowId = params.get("FlowId")
        self._ReviewType = params.get("ReviewType")
        self._ReviewMessage = params.get("ReviewMessage")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._RecipientId = params.get("RecipientId")
        self._OperateType = params.get("OperateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowSignReviewResponse(AbstractModel):
    """CreateFlowSignReview返回参数结构体

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


class CreateFlowSignUrlRequest(AbstractModel):
    """CreateFlowSignUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程编号
        :type FlowId: str
        :param _FlowApproverInfos: 流程签署人列表，其中结构体的ApproverName，ApproverMobile和ApproverType必传，其他可不传，ApproverType目前只支持个人类型的签署人。

签署人只能有手写签名和时间类型的签署控件，其他类型的填写控件和签署控件暂时都未支持。
        :type FlowApproverInfos: list of FlowCreateApprover
        :param _Operator: 用户信息，此结构体UserId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Organization: 机构信息，暂未开放
        :type Organization: :class:`tencentcloud.ess.v20201111.models.OrganizationInfo`
        :param _JumpUrl: 签署完之后的H5页面的跳转链接，此链接支持http://和https://，最大长度1000个字符。
        :type JumpUrl: str
        """
        self._FlowId = None
        self._FlowApproverInfos = None
        self._Operator = None
        self._Agent = None
        self._Organization = None
        self._JumpUrl = None

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
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

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
        self._FlowId = params.get("FlowId")
        if params.get("FlowApproverInfos") is not None:
            self._FlowApproverInfos = []
            for item in params.get("FlowApproverInfos"):
                obj = FlowCreateApprover()
                obj._deserialize(item)
                self._FlowApproverInfos.append(obj)
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
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
        


class CreateFlowSignUrlResponse(AbstractModel):
    """CreateFlowSignUrl返回参数结构体

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


class CreateIntegrationDepartmentRequest(AbstractModel):
    """CreateIntegrationDepartment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息，UserId必填且需拥有组织架构管理权限
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _DeptName: 部门名称，不超过50个字符
        :type DeptName: str
        :param _ParentDeptId: 电子签父部门ID，与ParentDeptOpenId二选一,优先ParentDeptId,都为空时自动填充至根节点下
        :type ParentDeptId: str
        :param _ParentDeptOpenId: 第三方平台中父部门ID,与ParentDeptId二选一,优先ParentDeptId,都为空时自动填充至根节点下
        :type ParentDeptOpenId: str
        :param _DeptOpenId: 客户系统部门ID，不超过64个字符
        :type DeptOpenId: str
        :param _OrderNo: 排序号,1~30000范围内
        :type OrderNo: int
        """
        self._Operator = None
        self._DeptName = None
        self._ParentDeptId = None
        self._ParentDeptOpenId = None
        self._DeptOpenId = None
        self._OrderNo = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def DeptName(self):
        return self._DeptName

    @DeptName.setter
    def DeptName(self, DeptName):
        self._DeptName = DeptName

    @property
    def ParentDeptId(self):
        return self._ParentDeptId

    @ParentDeptId.setter
    def ParentDeptId(self, ParentDeptId):
        self._ParentDeptId = ParentDeptId

    @property
    def ParentDeptOpenId(self):
        return self._ParentDeptOpenId

    @ParentDeptOpenId.setter
    def ParentDeptOpenId(self, ParentDeptOpenId):
        self._ParentDeptOpenId = ParentDeptOpenId

    @property
    def DeptOpenId(self):
        return self._DeptOpenId

    @DeptOpenId.setter
    def DeptOpenId(self, DeptOpenId):
        self._DeptOpenId = DeptOpenId

    @property
    def OrderNo(self):
        return self._OrderNo

    @OrderNo.setter
    def OrderNo(self, OrderNo):
        self._OrderNo = OrderNo


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._DeptName = params.get("DeptName")
        self._ParentDeptId = params.get("ParentDeptId")
        self._ParentDeptOpenId = params.get("ParentDeptOpenId")
        self._DeptOpenId = params.get("DeptOpenId")
        self._OrderNo = params.get("OrderNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIntegrationDepartmentResponse(AbstractModel):
    """CreateIntegrationDepartment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeptId: 电子签部门ID
        :type DeptId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeptId = None
        self._RequestId = None

    @property
    def DeptId(self):
        return self._DeptId

    @DeptId.setter
    def DeptId(self, DeptId):
        self._DeptId = DeptId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeptId = params.get("DeptId")
        self._RequestId = params.get("RequestId")


class CreateIntegrationEmployeesRequest(AbstractModel):
    """CreateIntegrationEmployees请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息，userId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Employees: 待创建员工的信息，不超过20个。
所有类型的企业支持的入参：Mobile和DisplayName必填,OpenId、Email和Department.DepartmentId选填，其他字段暂不支持。
企微类型的企业特有支持的入参：WeworkOpenId，传入此字段无需在传入其他信息
        :type Employees: list of Staff
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._Employees = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Employees(self):
        return self._Employees

    @Employees.setter
    def Employees(self, Employees):
        self._Employees = Employees

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("Employees") is not None:
            self._Employees = []
            for item in params.get("Employees"):
                obj = Staff()
                obj._deserialize(item)
                self._Employees.append(obj)
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
        


class CreateIntegrationEmployeesResponse(AbstractModel):
    """CreateIntegrationEmployees返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CreateEmployeeResult: 创建员工的结果
        :type CreateEmployeeResult: :class:`tencentcloud.ess.v20201111.models.CreateStaffResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CreateEmployeeResult = None
        self._RequestId = None

    @property
    def CreateEmployeeResult(self):
        return self._CreateEmployeeResult

    @CreateEmployeeResult.setter
    def CreateEmployeeResult(self, CreateEmployeeResult):
        self._CreateEmployeeResult = CreateEmployeeResult

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CreateEmployeeResult") is not None:
            self._CreateEmployeeResult = CreateStaffResult()
            self._CreateEmployeeResult._deserialize(params.get("CreateEmployeeResult"))
        self._RequestId = params.get("RequestId")


class CreateIntegrationUserRolesRequest(AbstractModel):
    """CreateIntegrationUserRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息，UserId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _UserIds: 绑定角色的用户id列表
        :type UserIds: list of str
        :param _RoleIds: 绑定角色的角色id列表
        :type RoleIds: list of str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._UserIds = None
        self._RoleIds = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def RoleIds(self):
        return self._RoleIds

    @RoleIds.setter
    def RoleIds(self, RoleIds):
        self._RoleIds = RoleIds

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._UserIds = params.get("UserIds")
        self._RoleIds = params.get("RoleIds")
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
        


class CreateIntegrationUserRolesResponse(AbstractModel):
    """CreateIntegrationUserRoles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailedCreateRoleData: 绑定角色失败列表信息
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


class CreateMultiFlowSignQRCodeRequest(AbstractModel):
    """CreateMultiFlowSignQRCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 用户信息，其中UserId为必填参数
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _TemplateId: 模板ID
        :type TemplateId: str
        :param _FlowName: 签署流程名称，最大长度不超过200字符
        :type FlowName: str
        :param _MaxFlowNum: 最大可发起签署流程份数，默认5份 
发起流程数量超过此上限后二维码自动失效
        :type MaxFlowNum: int
        :param _FlowEffectiveDay: 签署流程有效天数 默认7天 最高设置不超过30天
        :type FlowEffectiveDay: int
        :param _QrEffectiveDay: 二维码有效天数 默认7天 最高设置不超过90天
        :type QrEffectiveDay: int
        :param _Restrictions: 限制二维码用户条件
        :type Restrictions: list of ApproverRestriction
        :param _UserData: 用户自定义字段，回调的时候会进行透传，长度需要小于20480
        :type UserData: str
        :param _CallbackUrl: 回调地址,最大长度1000字符串
回调时机：
用户通过签署二维码发起签署流程时，企业额度不足导致失败
        :type CallbackUrl: str
        :param _Agent: 应用信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _ApproverRestrictions: 限制二维码用户条件（已弃用）
        :type ApproverRestrictions: :class:`tencentcloud.ess.v20201111.models.ApproverRestriction`
        """
        self._Operator = None
        self._TemplateId = None
        self._FlowName = None
        self._MaxFlowNum = None
        self._FlowEffectiveDay = None
        self._QrEffectiveDay = None
        self._Restrictions = None
        self._UserData = None
        self._CallbackUrl = None
        self._Agent = None
        self._ApproverRestrictions = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

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
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def Agent(self):
        warnings.warn("parameter `Agent` is deprecated", DeprecationWarning) 

        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        warnings.warn("parameter `Agent` is deprecated", DeprecationWarning) 

        self._Agent = Agent

    @property
    def ApproverRestrictions(self):
        warnings.warn("parameter `ApproverRestrictions` is deprecated", DeprecationWarning) 

        return self._ApproverRestrictions

    @ApproverRestrictions.setter
    def ApproverRestrictions(self, ApproverRestrictions):
        warnings.warn("parameter `ApproverRestrictions` is deprecated", DeprecationWarning) 

        self._ApproverRestrictions = ApproverRestrictions


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
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
        self._UserData = params.get("UserData")
        self._CallbackUrl = params.get("CallbackUrl")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("ApproverRestrictions") is not None:
            self._ApproverRestrictions = ApproverRestriction()
            self._ApproverRestrictions._deserialize(params.get("ApproverRestrictions"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMultiFlowSignQRCodeResponse(AbstractModel):
    """CreateMultiFlowSignQRCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QrCode: 签署二维码对象
        :type QrCode: :class:`tencentcloud.ess.v20201111.models.SignQrCode`
        :param _SignUrls: 签署链接对象
        :type SignUrls: :class:`tencentcloud.ess.v20201111.models.SignUrl`
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


class CreateOrganizationBatchSignUrlRequest(AbstractModel):
    """CreateOrganizationBatchSignUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，UserId 必填，支持填入集团子公司经办人UserId。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowIds: 指定需要进行批量签署的流程id，数量1-100，填写后用户将通过链接对这些合同进行批量签署。
        :type FlowIds: list of str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _UserId: 员工的UserId，该UserId对应的员工必须已经加入企业并实名，Name和Mobile为空时该字段不能为空。（优先使用UserId对应的员工）
        :type UserId: str
        :param _Name: 员工姓名，该字段需要与Mobile组合使用，UserId为空时该字段不能为空。（UserId为空时，使用Name和Mbile对应的员工）
        :type Name: str
        :param _Mobile: 员工手机号码，该字段需要与Name组合使用，UserId为空时该字段不能为空。（UserId为空时，使用Name和Mbile对应的员工）
        :type Mobile: str
        """
        self._Operator = None
        self._FlowIds = None
        self._Agent = None
        self._UserId = None
        self._Name = None
        self._Mobile = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

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
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowIds = params.get("FlowIds")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._UserId = params.get("UserId")
        self._Name = params.get("Name")
        self._Mobile = params.get("Mobile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationBatchSignUrlResponse(AbstractModel):
    """CreateOrganizationBatchSignUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SignUrl: 批量签署入口链接
        :type SignUrl: str
        :param _ExpiredTime: 链接过期时间戳
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


class CreatePrepareFlowRequest(AbstractModel):
    """CreatePrepareFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _ResourceId: 资源Id，通过多文件上传（UploadFiles）接口获得
        :type ResourceId: str
        :param _FlowName: 合同名称
        :type FlowName: str
        :param _Unordered: 是否顺序签署(true:无序签,false:顺序签)
        :type Unordered: bool
        :param _Deadline: 签署流程的签署截止时间。
值为unix时间戳,精确到秒,不传默认为当前时间一年后
        :type Deadline: int
        :param _UserFlowTypeId: 用户自定义合同类型
        :type UserFlowTypeId: str
        :param _Approvers: 签署流程参与者信息，最大限制50方
        :type Approvers: list of FlowCreateApprover
        :param _IntelligentStatus: 打开智能添加填写区(默认开启，打开:"OPEN" 关闭："CLOSE")
        :type IntelligentStatus: str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填	
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._ResourceId = None
        self._FlowName = None
        self._Unordered = None
        self._Deadline = None
        self._UserFlowTypeId = None
        self._Approvers = None
        self._IntelligentStatus = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def Unordered(self):
        return self._Unordered

    @Unordered.setter
    def Unordered(self, Unordered):
        self._Unordered = Unordered

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def UserFlowTypeId(self):
        return self._UserFlowTypeId

    @UserFlowTypeId.setter
    def UserFlowTypeId(self, UserFlowTypeId):
        self._UserFlowTypeId = UserFlowTypeId

    @property
    def Approvers(self):
        return self._Approvers

    @Approvers.setter
    def Approvers(self, Approvers):
        self._Approvers = Approvers

    @property
    def IntelligentStatus(self):
        return self._IntelligentStatus

    @IntelligentStatus.setter
    def IntelligentStatus(self, IntelligentStatus):
        self._IntelligentStatus = IntelligentStatus

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._ResourceId = params.get("ResourceId")
        self._FlowName = params.get("FlowName")
        self._Unordered = params.get("Unordered")
        self._Deadline = params.get("Deadline")
        self._UserFlowTypeId = params.get("UserFlowTypeId")
        if params.get("Approvers") is not None:
            self._Approvers = []
            for item in params.get("Approvers"):
                obj = FlowCreateApprover()
                obj._deserialize(item)
                self._Approvers.append(obj)
        self._IntelligentStatus = params.get("IntelligentStatus")
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
        


class CreatePrepareFlowResponse(AbstractModel):
    """CreatePrepareFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 快速发起预览链接，有效期5分钟
        :type Url: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._RequestId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._RequestId = params.get("RequestId")


class CreatePreparedPersonalEsignRequest(AbstractModel):
    """CreatePreparedPersonalEsign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserName: 个人用户姓名
        :type UserName: str
        :param _IdCardNumber: 身份证件号码
        :type IdCardNumber: str
        :param _SealName: 印章名称
        :type SealName: str
        :param _Operator: 调用方用户信息，userId 必填。支持填入集团子公司经办人 userId代发合同。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _IdCardType: 身份证件类型:
ID_CARD 身份证
PASSPORT 护照
HONGKONG_AND_MACAO 中国香港
FOREIGN_ID_CARD 境外身份
HONGKONG_MACAO_AND_TAIWAN 中国台湾
        :type IdCardType: str
        :param _SealImage: 印章图片的base64
注：已废弃
请先通过UploadFiles接口上传文件，获取 FileId
        :type SealImage: str
        :param _SealImageCompress: 是否开启印章图片压缩处理，默认不开启，如需开启请设置为 true。当印章超过 2M 时建议开启，开启后图片的 hash 将发生变化。
        :type SealImageCompress: bool
        :param _Mobile: 手机号码；当需要开通自动签时，该参数必传
        :type Mobile: str
        :param _EnableAutoSign: 是否开通自动签，该功能需联系运营工作人员开通后使用
        :type EnableAutoSign: bool
        :param _SealColor: 印章颜色（参数ProcessSeal=true时生效）
默认值：BLACK黑色
取值: 
BLACK 黑色,
RED 红色,
BLUE 蓝色。
        :type SealColor: str
        :param _ProcessSeal: 是否处理印章
默认不做印章处理。
取值：false：不做任何处理；
true：做透明化处理和颜色增强。
        :type ProcessSeal: bool
        :param _FileId: 印章图片文件 id
取值：
填写的FileId通过UploadFiles接口上传文件获取。
        :type FileId: str
        """
        self._UserName = None
        self._IdCardNumber = None
        self._SealName = None
        self._Operator = None
        self._IdCardType = None
        self._SealImage = None
        self._SealImageCompress = None
        self._Mobile = None
        self._EnableAutoSign = None
        self._SealColor = None
        self._ProcessSeal = None
        self._FileId = None

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
    def SealImage(self):
        warnings.warn("parameter `SealImage` is deprecated", DeprecationWarning) 

        return self._SealImage

    @SealImage.setter
    def SealImage(self, SealImage):
        warnings.warn("parameter `SealImage` is deprecated", DeprecationWarning) 

        self._SealImage = SealImage

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
    def SealColor(self):
        return self._SealColor

    @SealColor.setter
    def SealColor(self, SealColor):
        self._SealColor = SealColor

    @property
    def ProcessSeal(self):
        return self._ProcessSeal

    @ProcessSeal.setter
    def ProcessSeal(self, ProcessSeal):
        self._ProcessSeal = ProcessSeal

    @property
    def FileId(self):
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._IdCardNumber = params.get("IdCardNumber")
        self._SealName = params.get("SealName")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._IdCardType = params.get("IdCardType")
        self._SealImage = params.get("SealImage")
        self._SealImageCompress = params.get("SealImageCompress")
        self._Mobile = params.get("Mobile")
        self._EnableAutoSign = params.get("EnableAutoSign")
        self._SealColor = params.get("SealColor")
        self._ProcessSeal = params.get("ProcessSeal")
        self._FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePreparedPersonalEsignResponse(AbstractModel):
    """CreatePreparedPersonalEsign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SealId: 导入生成的印章ID
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


class CreateReleaseFlowRequest(AbstractModel):
    """CreateReleaseFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _NeedRelievedFlowId: 待解除的签署流程编号（即原签署流程的编号）
        :type NeedRelievedFlowId: str
        :param _ReliveInfo: 解除协议内容
        :type ReliveInfo: :class:`tencentcloud.ess.v20201111.models.RelieveInfo`
        :param _ReleasedApprovers: 非必须，解除协议的本企业签署人列表，
默认使用原流程的签署人列表,当解除协议的签署人与原流程的签署人不能相同时（例如原流程签署人离职了），需要指定本企业其他已实名员工来替换原流程中的原签署人，注意需要指明原签署人的编号(ReceiptId,通过DescribeFlowInfo接口获取)来代表需要替换哪一个签署人
解除协议的签署人数量不能多于原流程的签署人数量
        :type ReleasedApprovers: list of ReleasedApprover
        :param _Deadline: 签署流程的签署截止时间。 值为unix时间戳,精确到秒,不传默认为当前时间七天后
        :type Deadline: int
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._NeedRelievedFlowId = None
        self._ReliveInfo = None
        self._ReleasedApprovers = None
        self._Deadline = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

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
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
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
        self._Deadline = params.get("Deadline")
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
        


class CreateReleaseFlowResponse(AbstractModel):
    """CreateReleaseFlow返回参数结构体

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


class CreateSchemeUrlRequest(AbstractModel):
    """CreateSchemeUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _OrganizationName: 企业名称
        :type OrganizationName: str
        :param _Name: 姓名,最大长度50个字符
        :type Name: str
        :param _Mobile: 手机号，大陆手机号11位
        :type Mobile: str
        :param _EndPoint: 链接类型
HTTP：跳转电子签小程序的http_url，
APP：第三方APP或小程序跳转电子签小程序的path。
默认为HTTP类型
        :type EndPoint: str
        :param _FlowId: 签署流程编号 (PathType=1时必传)
        :type FlowId: str
        :param _FlowGroupId: 合同组ID
        :type FlowGroupId: str
        :param _PathType: 跳转页面 1: 小程序合同详情 2: 小程序合同列表页 0: 不传, 默认主页
        :type PathType: int
        :param _AutoJumpBack: 是否自动回跳 true：是， false：否。该参数只针对"APP" 类型的签署链接有效
        :type AutoJumpBack: bool
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Hides: 生成的签署链接在签署过程隐藏的按钮列表, 可以设置隐藏的按钮列表如下

0:合同签署页面更多操作按钮
1:合同签署页面更多操作的拒绝签署按钮
2:合同签署页面更多操作的转他人处理按钮
3:签署成功页的查看详情按钮
        :type Hides: list of int
        """
        self._Operator = None
        self._OrganizationName = None
        self._Name = None
        self._Mobile = None
        self._EndPoint = None
        self._FlowId = None
        self._FlowGroupId = None
        self._PathType = None
        self._AutoJumpBack = None
        self._Agent = None
        self._Hides = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

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
    def EndPoint(self):
        return self._EndPoint

    @EndPoint.setter
    def EndPoint(self, EndPoint):
        self._EndPoint = EndPoint

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def FlowGroupId(self):
        return self._FlowGroupId

    @FlowGroupId.setter
    def FlowGroupId(self, FlowGroupId):
        self._FlowGroupId = FlowGroupId

    @property
    def PathType(self):
        return self._PathType

    @PathType.setter
    def PathType(self, PathType):
        self._PathType = PathType

    @property
    def AutoJumpBack(self):
        return self._AutoJumpBack

    @AutoJumpBack.setter
    def AutoJumpBack(self, AutoJumpBack):
        self._AutoJumpBack = AutoJumpBack

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def Hides(self):
        return self._Hides

    @Hides.setter
    def Hides(self, Hides):
        self._Hides = Hides


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._OrganizationName = params.get("OrganizationName")
        self._Name = params.get("Name")
        self._Mobile = params.get("Mobile")
        self._EndPoint = params.get("EndPoint")
        self._FlowId = params.get("FlowId")
        self._FlowGroupId = params.get("FlowGroupId")
        self._PathType = params.get("PathType")
        self._AutoJumpBack = params.get("AutoJumpBack")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._Hides = params.get("Hides")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSchemeUrlResponse(AbstractModel):
    """CreateSchemeUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SchemeUrl: 小程序链接地址，有效期5分钟
        :type SchemeUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SchemeUrl = None
        self._RequestId = None

    @property
    def SchemeUrl(self):
        return self._SchemeUrl

    @SchemeUrl.setter
    def SchemeUrl(self, SchemeUrl):
        self._SchemeUrl = SchemeUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SchemeUrl = params.get("SchemeUrl")
        self._RequestId = params.get("RequestId")


class CreateSealPolicyRequest(AbstractModel):
    """CreateSealPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Users: 用户在电子文件签署平台标识信息，具体参考UserInfo结构体。可跟下面的UserIds可叠加起作用
        :type Users: list of UserInfo
        :param _SealId: 印章ID
        :type SealId: str
        :param _Expired: 授权有效期。时间戳秒级
        :type Expired: int
        :param _UserIds: 需要授权的用户UserId集合。跟上面的SealId参数配合使用。选填，跟上面的Users同时起作用
        :type UserIds: list of str
        :param _Policy: 印章授权内容
        :type Policy: str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._Users = None
        self._SealId = None
        self._Expired = None
        self._UserIds = None
        self._Policy = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def SealId(self):
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def Expired(self):
        return self._Expired

    @Expired.setter
    def Expired(self, Expired):
        self._Expired = Expired

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = UserInfo()
                obj._deserialize(item)
                self._Users.append(obj)
        self._SealId = params.get("SealId")
        self._Expired = params.get("Expired")
        self._UserIds = params.get("UserIds")
        self._Policy = params.get("Policy")
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
        


class CreateSealPolicyResponse(AbstractModel):
    """CreateSealPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserIds: 最终授权成功的。其他的跳过的是已经授权了的
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


class CreateSealRequest(AbstractModel):
    """CreateSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _SealName: 电子印章名字
        :type SealName: str
        :param _Agent: 应用相关信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _GenerateSource: 本接口支持上传图片印章及系统直接生成印章；如果要使用系统生成印章，此值传：SealGenerateSourceSystem；如果要使用图片上传请传字段 Image
        :type GenerateSource: str
        :param _SealType: 电子印章类型，OFFICIAL-公章,CONTRACT-合同专用章
        :type SealType: str
        :param _FileName: 电子印章图片文件名称
        :type FileName: str
        :param _Image: 电子印章图片base64编码
参数Image,FileToken或GenerateSource=SealGenerateSourceSystem三选一。
        :type Image: str
        :param _Width: 电子印章宽度,单位px
参数不再启用，系统会设置印章大小为标准尺寸。
        :type Width: int
        :param _Height: 电子印章高度,单位px
参数不再启用，系统会设置印章大小为标准尺寸。
        :type Height: int
        :param _Color: 电子印章印章颜色(默认红色RED),RED-红色

系统目前只支持红色印章创建。
        :type Color: str
        :param _SealHorizontalText: 暂时不支持横向文字设置
        :type SealHorizontalText: str
        :param _SealChordText: 暂时不支持下弦文字设置
        :type SealChordText: str
        :param _SealCentralType: 系统生成的印章只支持STAR
        :type SealCentralType: str
        :param _FileToken: 通过文件上传时，服务端生成的电子印章上传图片的token

        :type FileToken: str
        """
        self._Operator = None
        self._SealName = None
        self._Agent = None
        self._GenerateSource = None
        self._SealType = None
        self._FileName = None
        self._Image = None
        self._Width = None
        self._Height = None
        self._Color = None
        self._SealHorizontalText = None
        self._SealChordText = None
        self._SealCentralType = None
        self._FileToken = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def SealName(self):
        return self._SealName

    @SealName.setter
    def SealName(self, SealName):
        self._SealName = SealName

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

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
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color

    @property
    def SealHorizontalText(self):
        return self._SealHorizontalText

    @SealHorizontalText.setter
    def SealHorizontalText(self, SealHorizontalText):
        self._SealHorizontalText = SealHorizontalText

    @property
    def SealChordText(self):
        return self._SealChordText

    @SealChordText.setter
    def SealChordText(self, SealChordText):
        self._SealChordText = SealChordText

    @property
    def SealCentralType(self):
        return self._SealCentralType

    @SealCentralType.setter
    def SealCentralType(self, SealCentralType):
        self._SealCentralType = SealCentralType

    @property
    def FileToken(self):
        return self._FileToken

    @FileToken.setter
    def FileToken(self, FileToken):
        self._FileToken = FileToken


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._SealName = params.get("SealName")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._GenerateSource = params.get("GenerateSource")
        self._SealType = params.get("SealType")
        self._FileName = params.get("FileName")
        self._Image = params.get("Image")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Color = params.get("Color")
        self._SealHorizontalText = params.get("SealHorizontalText")
        self._SealChordText = params.get("SealChordText")
        self._SealCentralType = params.get("SealCentralType")
        self._FileToken = params.get("FileToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSealResponse(AbstractModel):
    """CreateSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SealId: 电子印章编号
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


class CreateStaffResult(AbstractModel):
    """创建员工的结果

    """

    def __init__(self):
        r"""
        :param _SuccessEmployeeData: 创建员工的成功列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessEmployeeData: list of SuccessCreateStaffData
        :param _FailedEmployeeData: 创建员工的失败列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedEmployeeData: list of FailedCreateStaffData
        """
        self._SuccessEmployeeData = None
        self._FailedEmployeeData = None

    @property
    def SuccessEmployeeData(self):
        return self._SuccessEmployeeData

    @SuccessEmployeeData.setter
    def SuccessEmployeeData(self, SuccessEmployeeData):
        self._SuccessEmployeeData = SuccessEmployeeData

    @property
    def FailedEmployeeData(self):
        return self._FailedEmployeeData

    @FailedEmployeeData.setter
    def FailedEmployeeData(self, FailedEmployeeData):
        self._FailedEmployeeData = FailedEmployeeData


    def _deserialize(self, params):
        if params.get("SuccessEmployeeData") is not None:
            self._SuccessEmployeeData = []
            for item in params.get("SuccessEmployeeData"):
                obj = SuccessCreateStaffData()
                obj._deserialize(item)
                self._SuccessEmployeeData.append(obj)
        if params.get("FailedEmployeeData") is not None:
            self._FailedEmployeeData = []
            for item in params.get("FailedEmployeeData"):
                obj = FailedCreateStaffData()
                obj._deserialize(item)
                self._FailedEmployeeData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserAutoSignEnableUrlRequest(AbstractModel):
    """CreateUserAutoSignEnableUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息,UserId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _SceneKey: 自动签场景:
E_PRESCRIPTION_AUTO_SIGN 电子处方
        :type SceneKey: str
        :param _AutoSignConfig: 自动签开通，签署相关配置
        :type AutoSignConfig: :class:`tencentcloud.ess.v20201111.models.AutoSignConfig`
        :param _UrlType: 链接类型，空-默认小程序端链接，H5SIGN-h5端链接
        :type UrlType: str
        :param _NotifyType: 通知类型，默认不填为不通知开通方，填写 SMS 为短信通知。
        :type NotifyType: str
        :param _NotifyAddress: 若上方填写为 SMS，则此处为手机号
        :type NotifyAddress: str
        :param _ExpiredTime: 链接的过期时间，格式为Unix时间戳，不能早于当前时间，且最大为30天。如果不传，默认有效期为7天。
        :type ExpiredTime: int
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._SceneKey = None
        self._AutoSignConfig = None
        self._UrlType = None
        self._NotifyType = None
        self._NotifyAddress = None
        self._ExpiredTime = None
        self._Agent = None

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

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._SceneKey = params.get("SceneKey")
        if params.get("AutoSignConfig") is not None:
            self._AutoSignConfig = AutoSignConfig()
            self._AutoSignConfig._deserialize(params.get("AutoSignConfig"))
        self._UrlType = params.get("UrlType")
        self._NotifyType = params.get("NotifyType")
        self._NotifyAddress = params.get("NotifyAddress")
        self._ExpiredTime = params.get("ExpiredTime")
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
        


class CreateUserAutoSignEnableUrlResponse(AbstractModel):
    """CreateUserAutoSignEnableUrl返回参数结构体

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


class CreateWebThemeConfigRequest(AbstractModel):
    """CreateWebThemeConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _ThemeType: 主题类型
<br/>EMBED_WEB_THEME：嵌入式主题
<br/>目前只支持EMBED_WEB_THEME，web页面嵌入的主题风格配置
        :type ThemeType: str
        :param _WebThemeConfig: 主题配置
        :type WebThemeConfig: :class:`tencentcloud.ess.v20201111.models.WebThemeConfig`
        """
        self._Operator = None
        self._ThemeType = None
        self._WebThemeConfig = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

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
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
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
        


class CreateWebThemeConfigResponse(AbstractModel):
    """CreateWebThemeConfig返回参数结构体

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


class DeleteIntegrationDepartmentRequest(AbstractModel):
    """DeleteIntegrationDepartment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息，UserId必填且需拥有组织架构管理权限
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _DeptId: 电子签中的部门id
        :type DeptId: str
        :param _ReceiveDeptId: 交接部门ID。待删除部门中的合同、印章和模板数据，交接至该部门ID下，未填写交接至公司根部门。
        :type ReceiveDeptId: str
        """
        self._Operator = None
        self._DeptId = None
        self._ReceiveDeptId = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def DeptId(self):
        return self._DeptId

    @DeptId.setter
    def DeptId(self, DeptId):
        self._DeptId = DeptId

    @property
    def ReceiveDeptId(self):
        return self._ReceiveDeptId

    @ReceiveDeptId.setter
    def ReceiveDeptId(self, ReceiveDeptId):
        self._ReceiveDeptId = ReceiveDeptId


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._DeptId = params.get("DeptId")
        self._ReceiveDeptId = params.get("ReceiveDeptId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIntegrationDepartmentResponse(AbstractModel):
    """DeleteIntegrationDepartment返回参数结构体

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


class DeleteIntegrationEmployeesRequest(AbstractModel):
    """DeleteIntegrationEmployees请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息，userId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Employees: 待移除员工的信息，userId和openId二选一，必填一个
        :type Employees: list of Staff
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId需填充子企业Id
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._Employees = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Employees(self):
        return self._Employees

    @Employees.setter
    def Employees(self, Employees):
        self._Employees = Employees

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("Employees") is not None:
            self._Employees = []
            for item in params.get("Employees"):
                obj = Staff()
                obj._deserialize(item)
                self._Employees.append(obj)
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
        


class DeleteIntegrationEmployeesResponse(AbstractModel):
    """DeleteIntegrationEmployees返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeleteEmployeeResult: 员工删除数据
        :type DeleteEmployeeResult: :class:`tencentcloud.ess.v20201111.models.DeleteStaffsResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeleteEmployeeResult = None
        self._RequestId = None

    @property
    def DeleteEmployeeResult(self):
        return self._DeleteEmployeeResult

    @DeleteEmployeeResult.setter
    def DeleteEmployeeResult(self, DeleteEmployeeResult):
        self._DeleteEmployeeResult = DeleteEmployeeResult

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeleteEmployeeResult") is not None:
            self._DeleteEmployeeResult = DeleteStaffsResult()
            self._DeleteEmployeeResult._deserialize(params.get("DeleteEmployeeResult"))
        self._RequestId = params.get("RequestId")


class DeleteIntegrationRoleUsersRequest(AbstractModel):
    """DeleteIntegrationRoleUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息，userId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _RoleId: 角色id
        :type RoleId: str
        :param _Users: 用户信息
        :type Users: list of UserInfo
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._RoleId = None
        self._Users = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._RoleId = params.get("RoleId")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = UserInfo()
                obj._deserialize(item)
                self._Users.append(obj)
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
        


class DeleteIntegrationRoleUsersResponse(AbstractModel):
    """DeleteIntegrationRoleUsers返回参数结构体

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


class DeleteSealPoliciesRequest(AbstractModel):
    """DeleteSealPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _PolicyIds: 印章授权编码数组。这个参数跟下面的SealId其中一个必填，另外一个可选填
        :type PolicyIds: list of str
        :param _SealId: 印章ID。这个参数跟上面的PolicyIds其中一个必填，另外一个可选填
        :type SealId: str
        :param _UserIds: 待授权的员工ID
        :type UserIds: list of str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._PolicyIds = None
        self._SealId = None
        self._UserIds = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

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
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._PolicyIds = params.get("PolicyIds")
        self._SealId = params.get("SealId")
        self._UserIds = params.get("UserIds")
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
        


class DeleteSealPoliciesResponse(AbstractModel):
    """DeleteSealPolicies返回参数结构体

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


class DeleteStaffsResult(AbstractModel):
    """删除员工结果

    """

    def __init__(self):
        r"""
        :param _SuccessEmployeeData: 删除员工的成功数据
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessEmployeeData: list of SuccessDeleteStaffData
        :param _FailedEmployeeData: 删除员工的失败数据
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedEmployeeData: list of FailedDeleteStaffData
        """
        self._SuccessEmployeeData = None
        self._FailedEmployeeData = None

    @property
    def SuccessEmployeeData(self):
        return self._SuccessEmployeeData

    @SuccessEmployeeData.setter
    def SuccessEmployeeData(self, SuccessEmployeeData):
        self._SuccessEmployeeData = SuccessEmployeeData

    @property
    def FailedEmployeeData(self):
        return self._FailedEmployeeData

    @FailedEmployeeData.setter
    def FailedEmployeeData(self, FailedEmployeeData):
        self._FailedEmployeeData = FailedEmployeeData


    def _deserialize(self, params):
        if params.get("SuccessEmployeeData") is not None:
            self._SuccessEmployeeData = []
            for item in params.get("SuccessEmployeeData"):
                obj = SuccessDeleteStaffData()
                obj._deserialize(item)
                self._SuccessEmployeeData.append(obj)
        if params.get("FailedEmployeeData") is not None:
            self._FailedEmployeeData = []
            for item in params.get("FailedEmployeeData"):
                obj = FailedDeleteStaffData()
                obj._deserialize(item)
                self._FailedEmployeeData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Department(AbstractModel):
    """集成版员工部门信息

    """

    def __init__(self):
        r"""
        :param _DepartmentId: 部门id
        :type DepartmentId: str
        :param _DepartmentName: 部门名称
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
        


class DescribeExtendedServiceAuthInfosRequest(AbstractModel):
    """DescribeExtendedServiceAuthInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _ExtendServiceType: 扩展服务类型，默认为空，查询目前支持的所有扩展服务信息，单个指定则查询单个扩展服务开通信息，取值：
OPEN_SERVER_SIGN：开通企业静默签署
OVERSEA_SIGN：企业与港澳台居民签署合同
MOBILE_CHECK_APPROVER：使用手机号验证签署方身份
PAGING_SEAL：骑缝章
BATCH_SIGN：批量签署
        :type ExtendServiceType: str
        """
        self._Operator = None
        self._Agent = None
        self._ExtendServiceType = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def ExtendServiceType(self):
        return self._ExtendServiceType

    @ExtendServiceType.setter
    def ExtendServiceType(self, ExtendServiceType):
        self._ExtendServiceType = ExtendServiceType


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._ExtendServiceType = params.get("ExtendServiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExtendedServiceAuthInfosResponse(AbstractModel):
    """DescribeExtendedServiceAuthInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AuthInfoList: 授权服务信息列表
        :type AuthInfoList: list of ExtendAuthInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AuthInfoList = None
        self._RequestId = None

    @property
    def AuthInfoList(self):
        return self._AuthInfoList

    @AuthInfoList.setter
    def AuthInfoList(self, AuthInfoList):
        self._AuthInfoList = AuthInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AuthInfoList") is not None:
            self._AuthInfoList = []
            for item in params.get("AuthInfoList"):
                obj = ExtendAuthInfo()
                obj._deserialize(item)
                self._AuthInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFileUrlsRequest(AbstractModel):
    """DescribeFileUrls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，UserId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _BusinessType: 文件对应的业务类型，目前支持：
- 流程 "FLOW"，如需下载合同文件请选择此项
- 模板 "TEMPLATE"
- 文档 "DOCUMENT"
- 印章  “SEAL”
        :type BusinessType: str
        :param _BusinessIds: 业务编号的数组，如流程编号、模板编号、文档编号、印章编号。如需下载合同文件请传入FlowId
最大支持20个资源
        :type BusinessIds: list of str
        :param _FileName: 下载后的文件命名，只有FileType为zip的时候生效
        :type FileName: str
        :param _FileType: 文件类型，"JPG", "PDF","ZIP"等
        :type FileType: str
        :param _Offset: 指定资源起始偏移量，默认0
        :type Offset: int
        :param _Limit: 指定资源数量，查询全部资源则传入-1
        :type Limit: int
        :param _UrlTtl: 下载url过期时间，单位秒。0: 按默认值5分钟，允许范围：1s~24x60x60s(1天)
        :type UrlTtl: int
        :param _CcToken: 暂不开放
        :type CcToken: str
        :param _Scene: 暂不开放
        :type Scene: str
        :param _Agent: 应用相关信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._BusinessType = None
        self._BusinessIds = None
        self._FileName = None
        self._FileType = None
        self._Offset = None
        self._Limit = None
        self._UrlTtl = None
        self._CcToken = None
        self._Scene = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def BusinessType(self):
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def BusinessIds(self):
        return self._BusinessIds

    @BusinessIds.setter
    def BusinessIds(self, BusinessIds):
        self._BusinessIds = BusinessIds

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

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
    def UrlTtl(self):
        return self._UrlTtl

    @UrlTtl.setter
    def UrlTtl(self, UrlTtl):
        self._UrlTtl = UrlTtl

    @property
    def CcToken(self):
        warnings.warn("parameter `CcToken` is deprecated", DeprecationWarning) 

        return self._CcToken

    @CcToken.setter
    def CcToken(self, CcToken):
        warnings.warn("parameter `CcToken` is deprecated", DeprecationWarning) 

        self._CcToken = CcToken

    @property
    def Scene(self):
        warnings.warn("parameter `Scene` is deprecated", DeprecationWarning) 

        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        warnings.warn("parameter `Scene` is deprecated", DeprecationWarning) 

        self._Scene = Scene

    @property
    def Agent(self):
        warnings.warn("parameter `Agent` is deprecated", DeprecationWarning) 

        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        warnings.warn("parameter `Agent` is deprecated", DeprecationWarning) 

        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._BusinessType = params.get("BusinessType")
        self._BusinessIds = params.get("BusinessIds")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._UrlTtl = params.get("UrlTtl")
        self._CcToken = params.get("CcToken")
        self._Scene = params.get("Scene")
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
        


class DescribeFileUrlsResponse(AbstractModel):
    """DescribeFileUrls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileUrls: 文件URL信息；
链接不是永久链接，有效期5分钟后链接失效。
        :type FileUrls: list of FileUrl
        :param _TotalCount: URL数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileUrls = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FileUrls(self):
        return self._FileUrls

    @FileUrls.setter
    def FileUrls(self, FileUrls):
        self._FileUrls = FileUrls

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
        if params.get("FileUrls") is not None:
            self._FileUrls = []
            for item in params.get("FileUrls"):
                obj = FileUrl()
                obj._deserialize(item)
                self._FileUrls.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeFlowBriefsRequest(AbstractModel):
    """DescribeFlowBriefs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowIds: 需要查询的流程ID列表，限制最大100个
        :type FlowIds: list of str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._FlowIds = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowIds = params.get("FlowIds")
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
        


class DescribeFlowBriefsResponse(AbstractModel):
    """DescribeFlowBriefs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowBriefs: 流程列表
        :type FlowBriefs: list of FlowBrief
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowBriefs = None
        self._RequestId = None

    @property
    def FlowBriefs(self):
        return self._FlowBriefs

    @FlowBriefs.setter
    def FlowBriefs(self, FlowBriefs):
        self._FlowBriefs = FlowBriefs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FlowBriefs") is not None:
            self._FlowBriefs = []
            for item in params.get("FlowBriefs"):
                obj = FlowBrief()
                obj._deserialize(item)
                self._FlowBriefs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFlowComponentsRequest(AbstractModel):
    """DescribeFlowComponents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作者信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowId: 电子签流程的Id
        :type FlowId: str
        :param _Agent: 应用相关信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._FlowId = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

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


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowId = params.get("FlowId")
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
        


class DescribeFlowComponentsResponse(AbstractModel):
    """DescribeFlowComponents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecipientComponentInfos: 流程关联的填写控件信息
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


class DescribeFlowEvidenceReportRequest(AbstractModel):
    """DescribeFlowEvidenceReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _ReportId: 出证报告编号
        :type ReportId: str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填

        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._ReportId = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def ReportId(self):
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._ReportId = params.get("ReportId")
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
        


class DescribeFlowEvidenceReportResponse(AbstractModel):
    """DescribeFlowEvidenceReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportUrl: 报告 URL
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportUrl: str
        :param _Status: 执行中：EvidenceStatusExecuting
成功：EvidenceStatusSuccess
失败：EvidenceStatusFailed
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


class DescribeFlowInfoRequest(AbstractModel):
    """DescribeFlowInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowIds: 需要查询的流程ID列表，限制最大100个
        :type FlowIds: list of str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _FlowGroupId: 合同组ID
        :type FlowGroupId: str
        """
        self._Operator = None
        self._FlowIds = None
        self._Agent = None
        self._FlowGroupId = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def FlowIds(self):
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowGroupId(self):
        return self._FlowGroupId

    @FlowGroupId.setter
    def FlowGroupId(self, FlowGroupId):
        self._FlowGroupId = FlowGroupId


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowIds = params.get("FlowIds")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._FlowGroupId = params.get("FlowGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowInfoResponse(AbstractModel):
    """DescribeFlowInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowDetailInfos: 签署流程信息
        :type FlowDetailInfos: list of FlowDetailInfo
        :param _FlowGroupId: 合同组ID
        :type FlowGroupId: str
        :param _FlowGroupName: 合同组名称
        :type FlowGroupName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowDetailInfos = None
        self._FlowGroupId = None
        self._FlowGroupName = None
        self._RequestId = None

    @property
    def FlowDetailInfos(self):
        return self._FlowDetailInfos

    @FlowDetailInfos.setter
    def FlowDetailInfos(self, FlowDetailInfos):
        self._FlowDetailInfos = FlowDetailInfos

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
        if params.get("FlowDetailInfos") is not None:
            self._FlowDetailInfos = []
            for item in params.get("FlowDetailInfos"):
                obj = FlowDetailInfo()
                obj._deserialize(item)
                self._FlowDetailInfos.append(obj)
        self._FlowGroupId = params.get("FlowGroupId")
        self._FlowGroupName = params.get("FlowGroupName")
        self._RequestId = params.get("RequestId")


class DescribeFlowTemplatesRequest(AbstractModel):
    """DescribeFlowTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方员工/经办人信息
UserId 必填，在企业控制台组织架构中可以查到员工的UserId
注：请保证对应
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Agent: 代理相关应用信息
如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _ContentType: 查询内容类型
0-模板列表及详情（默认）
1-仅模板列表
        :type ContentType: int
        :param _Filters: 搜索条件，本字段用于指定模板Id进行查询。
Key：template-id
Values：需要查询的模板Id列表
        :type Filters: list of Filter
        :param _Offset: 查询结果分页返回，此处指定第几页，如果不传默从第一页返回。页码从0开始，即首页为0。
        :type Offset: int
        :param _Limit: 指定每页多少条数据，如果不传默认为20，单页最大200。
        :type Limit: int
        :param _ApplicationId: 用于查询指定应用号下单模板列表。
ApplicationId不为空，查询指定应用下的模板列表
ApplicationId为空，查询所有应用下的模板列表
        :type ApplicationId: str
        :param _IsChannel: 默认为false，查询SaaS模板库列表；
为true，查询第三方应用集成平台企业模板库管理列表
        :type IsChannel: bool
        :param _Organization: 暂未开放
        :type Organization: :class:`tencentcloud.ess.v20201111.models.OrganizationInfo`
        :param _GenerateSource: 暂未开放
        :type GenerateSource: int
        """
        self._Operator = None
        self._Agent = None
        self._ContentType = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._ApplicationId = None
        self._IsChannel = None
        self._Organization = None
        self._GenerateSource = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def ContentType(self):
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

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
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def IsChannel(self):
        warnings.warn("parameter `IsChannel` is deprecated", DeprecationWarning) 

        return self._IsChannel

    @IsChannel.setter
    def IsChannel(self, IsChannel):
        warnings.warn("parameter `IsChannel` is deprecated", DeprecationWarning) 

        self._IsChannel = IsChannel

    @property
    def Organization(self):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        self._Organization = Organization

    @property
    def GenerateSource(self):
        warnings.warn("parameter `GenerateSource` is deprecated", DeprecationWarning) 

        return self._GenerateSource

    @GenerateSource.setter
    def GenerateSource(self, GenerateSource):
        warnings.warn("parameter `GenerateSource` is deprecated", DeprecationWarning) 

        self._GenerateSource = GenerateSource


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._ContentType = params.get("ContentType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ApplicationId = params.get("ApplicationId")
        self._IsChannel = params.get("IsChannel")
        if params.get("Organization") is not None:
            self._Organization = OrganizationInfo()
            self._Organization._deserialize(params.get("Organization"))
        self._GenerateSource = params.get("GenerateSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowTemplatesResponse(AbstractModel):
    """DescribeFlowTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Templates: 模板详情列表
        :type Templates: list of TemplateInfo
        :param _TotalCount: 查询到的总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Templates = None
        self._TotalCount = None
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
        self._RequestId = params.get("RequestId")


class DescribeIntegrationDepartmentsRequest(AbstractModel):
    """DescribeIntegrationDepartments请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息，UserId必填且需拥有组织架构管理权限
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _QueryType: 查询类型 0-查询单个部门节点 1-单个部门节点及一级子节点部门列表
        :type QueryType: int
        :param _DeptId: 部门ID,与DeptOpenId二选一,优先DeptId,都为空时获取根节点数据
        :type DeptId: str
        :param _DeptOpenId: 客户系统部门ID,与DeptId二选一,优先DeptId,都为空时获取根节点数据
        :type DeptOpenId: str
        """
        self._Operator = None
        self._QueryType = None
        self._DeptId = None
        self._DeptOpenId = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def QueryType(self):
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def DeptId(self):
        return self._DeptId

    @DeptId.setter
    def DeptId(self, DeptId):
        self._DeptId = DeptId

    @property
    def DeptOpenId(self):
        return self._DeptOpenId

    @DeptOpenId.setter
    def DeptOpenId(self, DeptOpenId):
        self._DeptOpenId = DeptOpenId


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._QueryType = params.get("QueryType")
        self._DeptId = params.get("DeptId")
        self._DeptOpenId = params.get("DeptOpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntegrationDepartmentsResponse(AbstractModel):
    """DescribeIntegrationDepartments返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Departments: 部门列表
        :type Departments: list of IntegrationDepartment
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Departments = None
        self._RequestId = None

    @property
    def Departments(self):
        return self._Departments

    @Departments.setter
    def Departments(self, Departments):
        self._Departments = Departments

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Departments") is not None:
            self._Departments = []
            for item in params.get("Departments"):
                obj = IntegrationDepartment()
                obj._deserialize(item)
                self._Departments.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIntegrationEmployeesRequest(AbstractModel):
    """DescribeIntegrationEmployees请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息，userId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Limit: 返回最大数量，最大为20
        :type Limit: int
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Filters: 查询过滤实名用户，Key为Status，Values为["IsVerified"]
根据第三方系统openId过滤查询员工时,Key为StaffOpenId,Values为["OpenId","OpenId",...]
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0，最大为20000
        :type Offset: int
        """
        self._Operator = None
        self._Limit = None
        self._Agent = None
        self._Filters = None
        self._Offset = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

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


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._Limit = params.get("Limit")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntegrationEmployeesResponse(AbstractModel):
    """DescribeIntegrationEmployees返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Employees: 员工数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Employees: list of Staff
        :param _Offset: 偏移量，默认为0，最大为20000
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: int
        :param _Limit: 返回最大数量，最大为20
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


class DescribeIntegrationMainOrganizationUserRequest(AbstractModel):
    """DescribeIntegrationMainOrganizationUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息，userId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        """
        self._Operator = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
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
        


class DescribeIntegrationMainOrganizationUserResponse(AbstractModel):
    """DescribeIntegrationMainOrganizationUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IntegrationMainOrganizationUser: 主企业员工账号信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IntegrationMainOrganizationUser: :class:`tencentcloud.ess.v20201111.models.IntegrationMainOrganizationUser`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IntegrationMainOrganizationUser = None
        self._RequestId = None

    @property
    def IntegrationMainOrganizationUser(self):
        return self._IntegrationMainOrganizationUser

    @IntegrationMainOrganizationUser.setter
    def IntegrationMainOrganizationUser(self, IntegrationMainOrganizationUser):
        self._IntegrationMainOrganizationUser = IntegrationMainOrganizationUser

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("IntegrationMainOrganizationUser") is not None:
            self._IntegrationMainOrganizationUser = IntegrationMainOrganizationUser()
            self._IntegrationMainOrganizationUser._deserialize(params.get("IntegrationMainOrganizationUser"))
        self._RequestId = params.get("RequestId")


class DescribeIntegrationRolesRequest(AbstractModel):
    """DescribeIntegrationRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息，UserId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Limit: 返回最大数量，最大为200
        :type Limit: int
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Filters: 查询的关键字段:
Key:"RoleType",Values:["1"]查询系统角色，Values:["2"]查询自定义角色
Key:"RoleStatus",Values:["1"]查询启用角色，Values:["2"]查询禁用角色
Key:"IsGroupRole"，Values:["0"],查询非集团角色，Values:["1"]表示查询集团角色
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0，最大为2000
        :type Offset: int
        """
        self._Operator = None
        self._Limit = None
        self._Agent = None
        self._Filters = None
        self._Offset = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

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


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._Limit = params.get("Limit")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntegrationRolesResponse(AbstractModel):
    """DescribeIntegrationRoles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0，最大为2000
        :type Offset: int
        :param _Limit: 返回最大数量，最大为200
        :type Limit: int
        :param _TotalCount: 符合查询条件的总的角色数
        :type TotalCount: int
        :param _IntegrateRoles: 企业角色信息列表
        :type IntegrateRoles: list of IntegrateRole
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Offset = None
        self._Limit = None
        self._TotalCount = None
        self._IntegrateRoles = None
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
    def IntegrateRoles(self):
        return self._IntegrateRoles

    @IntegrateRoles.setter
    def IntegrateRoles(self, IntegrateRoles):
        self._IntegrateRoles = IntegrateRoles

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
        if params.get("IntegrateRoles") is not None:
            self._IntegrateRoles = []
            for item in params.get("IntegrateRoles"):
                obj = IntegrateRole()
                obj._deserialize(item)
                self._IntegrateRoles.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrganizationGroupOrganizationsRequest(AbstractModel):
    """DescribeOrganizationGroupOrganizations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息，userId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Limit: 单次查询成员企业最大返回数量
        :type Limit: int
        :param _Offset: 页面偏移量
        :type Offset: int
        :param _Name: 查询成员企业的企业名，模糊匹配
        :type Name: str
        :param _Status: 成员企业加入集团的当前状态:1-待授权;2-已授权待激活;3-拒绝授权;4-已解除;5-已加入
        :type Status: int
        :param _Export: 是否导出当前成员企业数据
        :type Export: bool
        :param _Id: 成员企业id
        :type Id: str
        """
        self._Operator = None
        self._Limit = None
        self._Offset = None
        self._Name = None
        self._Status = None
        self._Export = None
        self._Id = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

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
    def Export(self):
        return self._Export

    @Export.setter
    def Export(self, Export):
        self._Export = Export

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._Export = params.get("Export")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationGroupOrganizationsResponse(AbstractModel):
    """DescribeOrganizationGroupOrganizations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 查询到的符合条件的成员企业总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _JoinedTotal: 已授权待激活的企业数量
注意：此字段可能返回 null，表示取不到有效值。
        :type JoinedTotal: int
        :param _ActivedTotal: 已加入的企业数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivedTotal: int
        :param _ExportUrl: 导出文件的url
注意：此字段可能返回 null，表示取不到有效值。
        :type ExportUrl: str
        :param _List: 成员企业信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of GroupOrganization
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._JoinedTotal = None
        self._ActivedTotal = None
        self._ExportUrl = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def JoinedTotal(self):
        return self._JoinedTotal

    @JoinedTotal.setter
    def JoinedTotal(self, JoinedTotal):
        self._JoinedTotal = JoinedTotal

    @property
    def ActivedTotal(self):
        return self._ActivedTotal

    @ActivedTotal.setter
    def ActivedTotal(self, ActivedTotal):
        self._ActivedTotal = ActivedTotal

    @property
    def ExportUrl(self):
        return self._ExportUrl

    @ExportUrl.setter
    def ExportUrl(self, ExportUrl):
        self._ExportUrl = ExportUrl

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._JoinedTotal = params.get("JoinedTotal")
        self._ActivedTotal = params.get("ActivedTotal")
        self._ExportUrl = params.get("ExportUrl")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = GroupOrganization()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrganizationSealsRequest(AbstractModel):
    """DescribeOrganizationSeals请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Limit: 返回最大数量，最大为100
        :type Limit: int
        :param _Offset: 偏移量，默认为0，最大为20000
        :type Offset: int
        :param _InfoType: 查询信息类型，为0时不返回授权用户，为1时返回
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
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._Limit = None
        self._Offset = None
        self._InfoType = None
        self._SealId = None
        self._SealTypes = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

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

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._InfoType = params.get("InfoType")
        self._SealId = params.get("SealId")
        self._SealTypes = params.get("SealTypes")
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
        


class DescribeOrganizationSealsResponse(AbstractModel):
    """DescribeOrganizationSeals返回参数结构体

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


class DescribeThirdPartyAuthCodeRequest(AbstractModel):
    """DescribeThirdPartyAuthCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AuthCode: 电子签小程序跳转客户小程序时携带的授权查看码
        :type AuthCode: str
        :param _Operator: 操作人信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._AuthCode = None
        self._Operator = None
        self._Agent = None

    @property
    def AuthCode(self):
        return self._AuthCode

    @AuthCode.setter
    def AuthCode(self, AuthCode):
        self._AuthCode = AuthCode

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        self._AuthCode = params.get("AuthCode")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
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
        


class DescribeThirdPartyAuthCodeResponse(AbstractModel):
    """DescribeThirdPartyAuthCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VerifyStatus: 用户是否实名，VERIFIED 为实名，UNVERIFIED 未实名
        :type VerifyStatus: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VerifyStatus = None
        self._RequestId = None

    @property
    def VerifyStatus(self):
        return self._VerifyStatus

    @VerifyStatus.setter
    def VerifyStatus(self, VerifyStatus):
        self._VerifyStatus = VerifyStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VerifyStatus = params.get("VerifyStatus")
        self._RequestId = params.get("RequestId")


class DescribeUserAutoSignStatusRequest(AbstractModel):
    """DescribeUserAutoSignStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息，UserId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _SceneKey: 自动签场景:
E_PRESCRIPTION_AUTO_SIGN 电子处方
        :type SceneKey: str
        :param _UserInfo: 查询开启状态的用户信息
        :type UserInfo: :class:`tencentcloud.ess.v20201111.models.UserThreeFactor`
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._SceneKey = None
        self._UserInfo = None
        self._Agent = None

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

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._SceneKey = params.get("SceneKey")
        if params.get("UserInfo") is not None:
            self._UserInfo = UserThreeFactor()
            self._UserInfo._deserialize(params.get("UserInfo"))
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
        


class DescribeUserAutoSignStatusResponse(AbstractModel):
    """DescribeUserAutoSignStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsOpen: 是否已开通自动签
        :type IsOpen: bool
        :param _LicenseFrom: 自动签许可生效时间。当且仅当已开通自动签时有值。
        :type LicenseFrom: int
        :param _LicenseTo: 自动签许可到期时间。当且仅当已开通自动签时有值。
        :type LicenseTo: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsOpen = None
        self._LicenseFrom = None
        self._LicenseTo = None
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
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsOpen = params.get("IsOpen")
        self._LicenseFrom = params.get("LicenseFrom")
        self._LicenseTo = params.get("LicenseTo")
        self._RequestId = params.get("RequestId")


class DisableUserAutoSignRequest(AbstractModel):
    """DisableUserAutoSign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息,UserId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _SceneKey: 自动签场景:
E_PRESCRIPTION_AUTO_SIGN 电子处方
        :type SceneKey: str
        :param _UserInfo: 关闭自动签的个人的三要素
        :type UserInfo: :class:`tencentcloud.ess.v20201111.models.UserThreeFactor`
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._SceneKey = None
        self._UserInfo = None
        self._Agent = None

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

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._SceneKey = params.get("SceneKey")
        if params.get("UserInfo") is not None:
            self._UserInfo = UserThreeFactor()
            self._UserInfo._deserialize(params.get("UserInfo"))
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
        


class DisableUserAutoSignResponse(AbstractModel):
    """DisableUserAutoSign返回参数结构体

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


class ExtendAuthInfo(AbstractModel):
    """授权服务信息

    """

    def __init__(self):
        r"""
        :param _Type: 授权服务类型
OPEN_SERVER_SIGN：开通企业静默签署
OVERSEA_SIGN：企业与港澳台居民签署合同
MOBILE_CHECK_APPROVER：使用手机号验证签署方身份
PAGING_SEAL：骑缝章
BATCH_SIGN：批量签署
        :type Type: str
        :param _Name: 授权服务名称
        :type Name: str
        :param _Status: 授权服务状态，ENABLE：开通
DISABLE：未开通
        :type Status: str
        :param _OperatorUserId: 授权人用户id
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorUserId: str
        :param _OperateOn: 授权时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateOn: int
        :param _HasAuthUserList: 被授权用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type HasAuthUserList: list of HasAuthUser
        """
        self._Type = None
        self._Name = None
        self._Status = None
        self._OperatorUserId = None
        self._OperateOn = None
        self._HasAuthUserList = None

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
    def OperatorUserId(self):
        return self._OperatorUserId

    @OperatorUserId.setter
    def OperatorUserId(self, OperatorUserId):
        self._OperatorUserId = OperatorUserId

    @property
    def OperateOn(self):
        return self._OperateOn

    @OperateOn.setter
    def OperateOn(self, OperateOn):
        self._OperateOn = OperateOn

    @property
    def HasAuthUserList(self):
        return self._HasAuthUserList

    @HasAuthUserList.setter
    def HasAuthUserList(self, HasAuthUserList):
        self._HasAuthUserList = HasAuthUserList


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._OperatorUserId = params.get("OperatorUserId")
        self._OperateOn = params.get("OperateOn")
        if params.get("HasAuthUserList") is not None:
            self._HasAuthUserList = []
            for item in params.get("HasAuthUserList"):
                obj = HasAuthUser()
                obj._deserialize(item)
                self._HasAuthUserList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FailedCreateRoleData(AbstractModel):
    """绑定角色失败信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户userId
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _RoleIds: 角色id列表
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
        


class FailedCreateStaffData(AbstractModel):
    """创建员工的失败数据

    """

    def __init__(self):
        r"""
        :param _DisplayName: 员工名
        :type DisplayName: str
        :param _Mobile: 员工手机号
        :type Mobile: str
        :param _WeworkOpenId: 传入的企微账号id
        :type WeworkOpenId: str
        :param _Reason: 失败原因
        :type Reason: str
        """
        self._DisplayName = None
        self._Mobile = None
        self._WeworkOpenId = None
        self._Reason = None

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
    def WeworkOpenId(self):
        return self._WeworkOpenId

    @WeworkOpenId.setter
    def WeworkOpenId(self, WeworkOpenId):
        self._WeworkOpenId = WeworkOpenId

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._Mobile = params.get("Mobile")
        self._WeworkOpenId = params.get("WeworkOpenId")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FailedDeleteStaffData(AbstractModel):
    """删除员工失败数据

    """

    def __init__(self):
        r"""
        :param _UserId: 员工在电子签的userId
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _OpenId: 员工在第三方平台的openId
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param _Reason: 失败原因
        :type Reason: str
        """
        self._UserId = None
        self._OpenId = None
        self._Reason = None

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
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._OpenId = params.get("OpenId")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FailedUpdateStaffData(AbstractModel):
    """更新员工信息失败返回的数据信息

    """

    def __init__(self):
        r"""
        :param _DisplayName: 用户传入的名称
        :type DisplayName: str
        :param _Mobile: 用户传入的手机号
        :type Mobile: str
        :param _Reason: 失败原因
        :type Reason: str
        :param _UserId: 用户Id
        :type UserId: str
        :param _OpenId: 员工在第三方平台的openId
        :type OpenId: str
        """
        self._DisplayName = None
        self._Mobile = None
        self._Reason = None
        self._UserId = None
        self._OpenId = None

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
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

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


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._Mobile = params.get("Mobile")
        self._Reason = params.get("Reason")
        self._UserId = params.get("UserId")
        self._OpenId = params.get("OpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileInfo(AbstractModel):
    """模板中文件的信息结构

    """

    def __init__(self):
        r"""
        :param _FileId: 文件Id
        :type FileId: str
        :param _FileName: 文件名
        :type FileName: str
        :param _FileSize: 文件大小，单位为Byte
        :type FileSize: int
        :param _CreatedOn: 文件上传时间，10位时间戳（精确到秒）
        :type CreatedOn: int
        """
        self._FileId = None
        self._FileName = None
        self._FileSize = None
        self._CreatedOn = None

    @property
    def FileId(self):
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn


    def _deserialize(self, params):
        self._FileId = params.get("FileId")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._CreatedOn = params.get("CreatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileUrl(AbstractModel):
    """下载文件的URL信息

    """

    def __init__(self):
        r"""
        :param _Url: 下载文件的URL，有效期为输入的UrlTtl，默认5分钟
        :type Url: str
        :param _Option: 下载文件的附加信息。如果是pdf文件，会返回pdf文件每页的有效高宽
注意：此字段可能返回 null，表示取不到有效值。
        :type Option: str
        """
        self._Url = None
        self._Option = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Option(self):
        return self._Option

    @Option.setter
    def Option(self, Option):
        self._Option = Option


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._Option = params.get("Option")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FillApproverInfo(AbstractModel):
    """补充签署人信息
    - RecipientId 必须指定
    -  通过企业自定义账号ID补充签署人时，ApproverSource 和 CustomUserId 必填
    - 通过二要素（姓名/手机号）补充签署人时，ApproverName 和 ApproverMobile 必填

    """

    def __init__(self):
        r"""
        :param _RecipientId: 对应模板中的参与方ID
        :type RecipientId: str
        :param _ApproverSource: 签署人来源
WEWORKAPP: 企业微信
        :type ApproverSource: str
        :param _CustomUserId: 企业自定义账号ID
WEWORKAPP场景下指企业自有应用获取企微明文的userid
        :type CustomUserId: str
        :param _ApproverName: 补充签署人姓名
        :type ApproverName: str
        :param _ApproverMobile: 补充签署人手机号
        :type ApproverMobile: str
        """
        self._RecipientId = None
        self._ApproverSource = None
        self._CustomUserId = None
        self._ApproverName = None
        self._ApproverMobile = None

    @property
    def RecipientId(self):
        return self._RecipientId

    @RecipientId.setter
    def RecipientId(self, RecipientId):
        self._RecipientId = RecipientId

    @property
    def ApproverSource(self):
        return self._ApproverSource

    @ApproverSource.setter
    def ApproverSource(self, ApproverSource):
        self._ApproverSource = ApproverSource

    @property
    def CustomUserId(self):
        return self._CustomUserId

    @CustomUserId.setter
    def CustomUserId(self, CustomUserId):
        self._CustomUserId = CustomUserId

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


    def _deserialize(self, params):
        self._RecipientId = params.get("RecipientId")
        self._ApproverSource = params.get("ApproverSource")
        self._CustomUserId = params.get("CustomUserId")
        self._ApproverName = params.get("ApproverName")
        self._ApproverMobile = params.get("ApproverMobile")
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
        :param _ComponentRecipientId: 控件所属参与方Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ComponentRecipientId: str
        :param _ImageUrl: 图片填充控件下载链接，如果是图片填充控件时，这里返回图片的下载链接。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: str
        """
        self._ComponentId = None
        self._ComponentName = None
        self._ComponentFillStatus = None
        self._ComponentValue = None
        self._ComponentRecipientId = None
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
    def ComponentRecipientId(self):
        return self._ComponentRecipientId

    @ComponentRecipientId.setter
    def ComponentRecipientId(self, ComponentRecipientId):
        self._ComponentRecipientId = ComponentRecipientId

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
        self._ComponentRecipientId = params.get("ComponentRecipientId")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """查询过滤条件

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
    """签署人详情信息

    """

    def __init__(self):
        r"""
        :param _ApproveMessage: 签署时的相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveMessage: str
        :param _ApproveName: 签署方姓名
        :type ApproveName: str
        :param _ApproveStatus: 签署方的签署状态
0：还没有发起
1：流程中 没有开始处理
2：待签署
3：已签署
4：已拒绝
5：已过期
6：已撤销
7：还没有预发起
8：待填写
9：因为各种原因而终止
10：填写完成
15：已解除
19：转他人处理
        :type ApproveStatus: int
        :param _ReceiptId: 模板配置中的参与方ID,与控件绑定
        :type ReceiptId: str
        :param _CustomUserId: 客户自定义的用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomUserId: str
        :param _Mobile: 签署人手机号
        :type Mobile: str
        :param _SignOrder: 签署顺序，如果是有序签署，签署顺序从小到大
        :type SignOrder: int
        :param _ApproveTime: 签署人签署时间，时间戳，单位秒
        :type ApproveTime: int
        :param _ApproveType: 签署方类型，ORGANIZATION-企业员工，PERSON-个人，ENTERPRISESERVER-企业静默签
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveType: str
        :param _ApproverSource: 签署方侧用户来源，如WEWORKAPP-企业微信等
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproverSource: str
        :param _CustomApproverTag: 客户自定义签署方标识
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomApproverTag: str
        :param _OrganizationId: 签署方企业Id
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationId: str
        :param _OrganizationName: 签署方企业名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationName: str
        """
        self._ApproveMessage = None
        self._ApproveName = None
        self._ApproveStatus = None
        self._ReceiptId = None
        self._CustomUserId = None
        self._Mobile = None
        self._SignOrder = None
        self._ApproveTime = None
        self._ApproveType = None
        self._ApproverSource = None
        self._CustomApproverTag = None
        self._OrganizationId = None
        self._OrganizationName = None

    @property
    def ApproveMessage(self):
        return self._ApproveMessage

    @ApproveMessage.setter
    def ApproveMessage(self, ApproveMessage):
        self._ApproveMessage = ApproveMessage

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
    def ReceiptId(self):
        return self._ReceiptId

    @ReceiptId.setter
    def ReceiptId(self, ReceiptId):
        self._ReceiptId = ReceiptId

    @property
    def CustomUserId(self):
        return self._CustomUserId

    @CustomUserId.setter
    def CustomUserId(self, CustomUserId):
        self._CustomUserId = CustomUserId

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
    def ApproverSource(self):
        return self._ApproverSource

    @ApproverSource.setter
    def ApproverSource(self, ApproverSource):
        self._ApproverSource = ApproverSource

    @property
    def CustomApproverTag(self):
        return self._CustomApproverTag

    @CustomApproverTag.setter
    def CustomApproverTag(self, CustomApproverTag):
        self._CustomApproverTag = CustomApproverTag

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName


    def _deserialize(self, params):
        self._ApproveMessage = params.get("ApproveMessage")
        self._ApproveName = params.get("ApproveName")
        self._ApproveStatus = params.get("ApproveStatus")
        self._ReceiptId = params.get("ReceiptId")
        self._CustomUserId = params.get("CustomUserId")
        self._Mobile = params.get("Mobile")
        self._SignOrder = params.get("SignOrder")
        self._ApproveTime = params.get("ApproveTime")
        self._ApproveType = params.get("ApproveType")
        self._ApproverSource = params.get("ApproverSource")
        self._CustomApproverTag = params.get("CustomApproverTag")
        self._OrganizationId = params.get("OrganizationId")
        self._OrganizationName = params.get("OrganizationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowApproverUrlInfo(AbstractModel):
    """签署链接信息

    """

    def __init__(self):
        r"""
        :param _SignUrl: 签署链接。注意该链接有效期为30分钟，同时需要注意保密，不要外泄给无关用户。
注意：此字段可能返回 null，表示取不到有效值。
        :type SignUrl: str
        :param _ApproverType: 签署人类型 1-个人
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproverType: int
        :param _ApproverName: 签署人姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproverName: str
        :param _ApproverMobile: 签署人手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproverMobile: str
        :param _LongUrl: 签署长链接。注意该链接有效期为30分钟，同时需要注意保密，不要外泄给无关用户。
注意：此字段可能返回 null，表示取不到有效值。
        :type LongUrl: str
        """
        self._SignUrl = None
        self._ApproverType = None
        self._ApproverName = None
        self._ApproverMobile = None
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
    def LongUrl(self):
        return self._LongUrl

    @LongUrl.setter
    def LongUrl(self, LongUrl):
        self._LongUrl = LongUrl


    def _deserialize(self, params):
        self._SignUrl = params.get("SignUrl")
        self._ApproverType = params.get("ApproverType")
        self._ApproverName = params.get("ApproverName")
        self._ApproverMobile = params.get("ApproverMobile")
        self._LongUrl = params.get("LongUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowBrief(AbstractModel):
    """流程信息摘要

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程的编号ID
        :type FlowId: str
        :param _FlowName: 流程的名称
        :type FlowName: str
        :param _FlowDescription: 流程的描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowDescription: str
        :param _FlowType: 流程的类型
        :type FlowType: str
        :param _FlowStatus: 流程状态
- 0 还没有发起
- 1 待签署
- 2 部分签署
- 3 已拒签
- 4 已签署
- 5 已过期
- 6 已撤销
- 7 还没有预发起
- 8 等待填写
- 9 部分填写
- 10 拒填
- 21 已解除
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowStatus: int
        :param _CreatedOn: 流程创建的时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedOn: int
        :param _FlowMessage: 拒签或者取消的原因描述
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowMessage: str
        :param _Creator:  合同发起人userId
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        :param _Deadline: 合同过期时间，时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Deadline: int
        """
        self._FlowId = None
        self._FlowName = None
        self._FlowDescription = None
        self._FlowType = None
        self._FlowStatus = None
        self._CreatedOn = None
        self._FlowMessage = None
        self._Creator = None
        self._Deadline = None

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
    def FlowStatus(self):
        return self._FlowStatus

    @FlowStatus.setter
    def FlowStatus(self, FlowStatus):
        self._FlowStatus = FlowStatus

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def FlowMessage(self):
        return self._FlowMessage

    @FlowMessage.setter
    def FlowMessage(self, FlowMessage):
        self._FlowMessage = FlowMessage

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._FlowName = params.get("FlowName")
        self._FlowDescription = params.get("FlowDescription")
        self._FlowType = params.get("FlowType")
        self._FlowStatus = params.get("FlowStatus")
        self._CreatedOn = params.get("CreatedOn")
        self._FlowMessage = params.get("FlowMessage")
        self._Creator = params.get("Creator")
        self._Deadline = params.get("Deadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowCreateApprover(AbstractModel):
    """创建流程的签署方信息

    """

    def __init__(self):
        r"""
        :param _ApproverType: 参与者类型：
0：企业
1：个人
3：企业静默签署
注：类型为3（企业静默签署）时，会默认完成该签署方的签署。静默签署仅进行盖章操作，不能是手写签名。
        :type ApproverType: int
        :param _OrganizationName: 如果签署方为企业，需要填入企业全称
        :type OrganizationName: str
        :param _ApproverName: 签署方经办人姓名
        :type ApproverName: str
        :param _ApproverMobile: 签署方经办人手机号码
        :type ApproverMobile: str
        :param _ApproverIdCardType: 签署方经办人证件类型ID_CARD 身份证
HONGKONG_AND_MACAO 港澳居民来往内地通行证
HONGKONG_MACAO_AND_TAIWAN 港澳台居民居住证(格式同居民身份证)
        :type ApproverIdCardType: str
        :param _ApproverIdCardNumber: 签署方经办人证件号码
        :type ApproverIdCardNumber: str
        :param _RecipientId: 签署方经办人在模板中的参与方ID
        :type RecipientId: str
        :param _VerifyChannel: 签署意愿确认渠道,WEIXINAPP:人脸识别
        :type VerifyChannel: list of str
        :param _NotifyType: 是否发送短信，sms--短信通知，none--不通知，默认为sms；发起方=签署方时不发送短信
        :type NotifyType: str
        :param _IsFullText: 合同强制需要阅读全文，无需传此参数
        :type IsFullText: bool
        :param _PreReadTime: 合同的强制预览时间：3~300s，未指定则按合同页数计算
        :type PreReadTime: int
        :param _UserId: 签署方经办人的用户ID,和签署方经办人姓名+手机号+证件必须有一个。
        :type UserId: str
        :param _Required: 当前只支持true，默认为true
        :type Required: bool
        :param _ApproverSource: 签署人用户来源,企微侧用户请传入：WEWORKAPP
        :type ApproverSource: str
        :param _CustomApproverTag: 企业签署方或签标识，客户自定义，64位长度。用于发起含有或签签署人的合同。或签参与人必须有此字段。合同内不同或签参与人CustomApproverTag需要保证唯一。如果或签签署人为本方企微参与人，ApproverSource参数需要指定WEWORKAPP
        :type CustomApproverTag: str
        :param _RegisterInfo: 快速注册相关信息，目前暂未开放！
        :type RegisterInfo: :class:`tencentcloud.ess.v20201111.models.RegisterInfo`
        :param _ApproverOption: 签署人个性化能力值
        :type ApproverOption: :class:`tencentcloud.ess.v20201111.models.ApproverOption`
        :param _JumpUrl: 签署完前端跳转的url，暂未使用
        :type JumpUrl: str
        :param _SignId: 签署ID
- 发起流程时系统自动补充
- 创建签署链接时，可以通过查询详情接口获得签署人的SignId，然后可传入此值为该签署人创建签署链接，无需再传姓名、手机号、证件号等其他信息
        :type SignId: str
        :param _ApproverNeedSignReview: 当前签署方进行签署操作是否需要企业内部审批，true 则为需要。为个人签署方时则由发起方企业审核。
        :type ApproverNeedSignReview: bool
        :param _SignComponents: 签署人签署控件
        :type SignComponents: list of Component
        :param _Components: 签署人填写控件
        :type Components: list of Component
        :param _ComponentLimitType: 签署方控件类型为 SIGN_SIGNATURE时，可以指定签署方签名方式
	HANDWRITE – 手写签名
	OCR_ESIGN -- AI智能识别手写签名
	ESIGN -- 个人印章类型
	SYSTEM_ESIGN -- 系统签名（该类型可以在用户签署时根据用户姓名一键生成一个签名来进行签署）
        :type ComponentLimitType: list of str
        :param _ApproverVerifyTypes: 合同查看方式<br/>默认1 -实名查看 <br/>2-短信验证码查看(企业签署方暂不支持该方式)
        :type ApproverVerifyTypes: list of int
        :param _ApproverSignTypes: 合同签署方式(默认1,2) <br/>1-人脸认证 <br/>2-签署密码 <br/>3-运营商三要素
        :type ApproverSignTypes: list of int non-negative
        """
        self._ApproverType = None
        self._OrganizationName = None
        self._ApproverName = None
        self._ApproverMobile = None
        self._ApproverIdCardType = None
        self._ApproverIdCardNumber = None
        self._RecipientId = None
        self._VerifyChannel = None
        self._NotifyType = None
        self._IsFullText = None
        self._PreReadTime = None
        self._UserId = None
        self._Required = None
        self._ApproverSource = None
        self._CustomApproverTag = None
        self._RegisterInfo = None
        self._ApproverOption = None
        self._JumpUrl = None
        self._SignId = None
        self._ApproverNeedSignReview = None
        self._SignComponents = None
        self._Components = None
        self._ComponentLimitType = None
        self._ApproverVerifyTypes = None
        self._ApproverSignTypes = None

    @property
    def ApproverType(self):
        return self._ApproverType

    @ApproverType.setter
    def ApproverType(self, ApproverType):
        self._ApproverType = ApproverType

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

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
    def ApproverIdCardType(self):
        return self._ApproverIdCardType

    @ApproverIdCardType.setter
    def ApproverIdCardType(self, ApproverIdCardType):
        self._ApproverIdCardType = ApproverIdCardType

    @property
    def ApproverIdCardNumber(self):
        return self._ApproverIdCardNumber

    @ApproverIdCardNumber.setter
    def ApproverIdCardNumber(self, ApproverIdCardNumber):
        self._ApproverIdCardNumber = ApproverIdCardNumber

    @property
    def RecipientId(self):
        return self._RecipientId

    @RecipientId.setter
    def RecipientId(self, RecipientId):
        self._RecipientId = RecipientId

    @property
    def VerifyChannel(self):
        return self._VerifyChannel

    @VerifyChannel.setter
    def VerifyChannel(self, VerifyChannel):
        self._VerifyChannel = VerifyChannel

    @property
    def NotifyType(self):
        return self._NotifyType

    @NotifyType.setter
    def NotifyType(self, NotifyType):
        self._NotifyType = NotifyType

    @property
    def IsFullText(self):
        return self._IsFullText

    @IsFullText.setter
    def IsFullText(self, IsFullText):
        self._IsFullText = IsFullText

    @property
    def PreReadTime(self):
        return self._PreReadTime

    @PreReadTime.setter
    def PreReadTime(self, PreReadTime):
        self._PreReadTime = PreReadTime

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Required(self):
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required

    @property
    def ApproverSource(self):
        return self._ApproverSource

    @ApproverSource.setter
    def ApproverSource(self, ApproverSource):
        self._ApproverSource = ApproverSource

    @property
    def CustomApproverTag(self):
        return self._CustomApproverTag

    @CustomApproverTag.setter
    def CustomApproverTag(self, CustomApproverTag):
        self._CustomApproverTag = CustomApproverTag

    @property
    def RegisterInfo(self):
        return self._RegisterInfo

    @RegisterInfo.setter
    def RegisterInfo(self, RegisterInfo):
        self._RegisterInfo = RegisterInfo

    @property
    def ApproverOption(self):
        return self._ApproverOption

    @ApproverOption.setter
    def ApproverOption(self, ApproverOption):
        self._ApproverOption = ApproverOption

    @property
    def JumpUrl(self):
        warnings.warn("parameter `JumpUrl` is deprecated", DeprecationWarning) 

        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        warnings.warn("parameter `JumpUrl` is deprecated", DeprecationWarning) 

        self._JumpUrl = JumpUrl

    @property
    def SignId(self):
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def ApproverNeedSignReview(self):
        return self._ApproverNeedSignReview

    @ApproverNeedSignReview.setter
    def ApproverNeedSignReview(self, ApproverNeedSignReview):
        self._ApproverNeedSignReview = ApproverNeedSignReview

    @property
    def SignComponents(self):
        return self._SignComponents

    @SignComponents.setter
    def SignComponents(self, SignComponents):
        self._SignComponents = SignComponents

    @property
    def Components(self):
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def ComponentLimitType(self):
        return self._ComponentLimitType

    @ComponentLimitType.setter
    def ComponentLimitType(self, ComponentLimitType):
        self._ComponentLimitType = ComponentLimitType

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
        self._ApproverType = params.get("ApproverType")
        self._OrganizationName = params.get("OrganizationName")
        self._ApproverName = params.get("ApproverName")
        self._ApproverMobile = params.get("ApproverMobile")
        self._ApproverIdCardType = params.get("ApproverIdCardType")
        self._ApproverIdCardNumber = params.get("ApproverIdCardNumber")
        self._RecipientId = params.get("RecipientId")
        self._VerifyChannel = params.get("VerifyChannel")
        self._NotifyType = params.get("NotifyType")
        self._IsFullText = params.get("IsFullText")
        self._PreReadTime = params.get("PreReadTime")
        self._UserId = params.get("UserId")
        self._Required = params.get("Required")
        self._ApproverSource = params.get("ApproverSource")
        self._CustomApproverTag = params.get("CustomApproverTag")
        if params.get("RegisterInfo") is not None:
            self._RegisterInfo = RegisterInfo()
            self._RegisterInfo._deserialize(params.get("RegisterInfo"))
        if params.get("ApproverOption") is not None:
            self._ApproverOption = ApproverOption()
            self._ApproverOption._deserialize(params.get("ApproverOption"))
        self._JumpUrl = params.get("JumpUrl")
        self._SignId = params.get("SignId")
        self._ApproverNeedSignReview = params.get("ApproverNeedSignReview")
        if params.get("SignComponents") is not None:
            self._SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self._SignComponents.append(obj)
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self._Components.append(obj)
        self._ComponentLimitType = params.get("ComponentLimitType")
        self._ApproverVerifyTypes = params.get("ApproverVerifyTypes")
        self._ApproverSignTypes = params.get("ApproverSignTypes")
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
        :param _FlowId: 合同(流程)的ID
        :type FlowId: str
        :param _FlowName: 合同(流程)的名字
        :type FlowName: str
        :param _FlowType: 合同(流程)的类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowType: str
        :param _FlowStatus: 流程状态
- 0 还没有发起
- 1 待签署
- 2 部分签署
- 3 已拒签
- 4 已签署
- 5 已过期
- 6 已撤销
- 7 还没有预发起
- 8 等待填写
- 9 部分填写
- 10 拒填
- 21 已解除
        :type FlowStatus: int
        :param _FlowMessage: 合同(流程)的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowMessage: str
        :param _FlowDescription: 流程的描述
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowDescription: str
        :param _CreatedOn: 合同(流程)的创建时间戳，单位秒
        :type CreatedOn: int
        :param _FlowApproverInfos: 合同(流程)的签署方数组
        :type FlowApproverInfos: list of FlowApproverDetail
        :param _CcInfos: 合同(流程)的关注方信息列表
        :type CcInfos: list of FlowApproverDetail
        :param _Creator: 合同发起人UserId
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        """
        self._FlowId = None
        self._FlowName = None
        self._FlowType = None
        self._FlowStatus = None
        self._FlowMessage = None
        self._FlowDescription = None
        self._CreatedOn = None
        self._FlowApproverInfos = None
        self._CcInfos = None
        self._Creator = None

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
    def FlowDescription(self):
        return self._FlowDescription

    @FlowDescription.setter
    def FlowDescription(self, FlowDescription):
        self._FlowDescription = FlowDescription

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

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
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._FlowName = params.get("FlowName")
        self._FlowType = params.get("FlowType")
        self._FlowStatus = params.get("FlowStatus")
        self._FlowMessage = params.get("FlowMessage")
        self._FlowDescription = params.get("FlowDescription")
        self._CreatedOn = params.get("CreatedOn")
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
        self._Creator = params.get("Creator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowGroupInfo(AbstractModel):
    """此结构体(FlowGroupInfo)描述的是合同组(流程组)的单个合同(流程)信息

    """

    def __init__(self):
        r"""
        :param _FlowName: 合同（流程）的名称
        :type FlowName: str
        :param _Approvers: 合同（流程）的签署方信息
        :type Approvers: list of ApproverInfo
        :param _FileIds: 发起合同（流程）的资源Id,此资源必须是PDF文件,来自UploadFiles,使用文件发起合同(流程)组时必传
        :type FileIds: list of str
        :param _TemplateId: 发起合同（流程）的模板Id,用模板发起合同（流程）组时必填
        :type TemplateId: str
        :param _FlowType: 合同（流程）的类型
        :type FlowType: str
        :param _FlowDescription: 合同（流程）的描述
        :type FlowDescription: str
        :param _Deadline: 合同（流程）的截止时间戳，单位秒。默认是一年
        :type Deadline: int
        :param _CallbackUrl: 合同（流程）的回调地址
        :type CallbackUrl: str
        :param _UserData: 第三方平台传递过来的信息, 限制1024字符 格式必须是base64的
        :type UserData: str
        :param _Unordered: 合同（流程）的签署是否是无序签, true - 无序。 false - 有序, 默认 
        :type Unordered: bool
        :param _Components: 合同（流程）发起方的填写控件，用户
        :type Components: list of Component
        :param _NeedSignReview: 本企业（发起方）是否需要签署审批，若需要审批则只允许查看不允许签署，需要您调用接口CreateFlowSignReview提交审批结果。
        :type NeedSignReview: bool
        :param _AutoSignScene: 本企业（发起方）自动签署，需要您在发起合同时给印章控件指定自动签的印章。
        :type AutoSignScene: str
        """
        self._FlowName = None
        self._Approvers = None
        self._FileIds = None
        self._TemplateId = None
        self._FlowType = None
        self._FlowDescription = None
        self._Deadline = None
        self._CallbackUrl = None
        self._UserData = None
        self._Unordered = None
        self._Components = None
        self._NeedSignReview = None
        self._AutoSignScene = None

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def Approvers(self):
        return self._Approvers

    @Approvers.setter
    def Approvers(self, Approvers):
        self._Approvers = Approvers

    @property
    def FileIds(self):
        return self._FileIds

    @FileIds.setter
    def FileIds(self, FileIds):
        self._FileIds = FileIds

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

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
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

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
    def NeedSignReview(self):
        return self._NeedSignReview

    @NeedSignReview.setter
    def NeedSignReview(self, NeedSignReview):
        self._NeedSignReview = NeedSignReview

    @property
    def AutoSignScene(self):
        return self._AutoSignScene

    @AutoSignScene.setter
    def AutoSignScene(self, AutoSignScene):
        self._AutoSignScene = AutoSignScene


    def _deserialize(self, params):
        self._FlowName = params.get("FlowName")
        if params.get("Approvers") is not None:
            self._Approvers = []
            for item in params.get("Approvers"):
                obj = ApproverInfo()
                obj._deserialize(item)
                self._Approvers.append(obj)
        self._FileIds = params.get("FileIds")
        self._TemplateId = params.get("TemplateId")
        self._FlowType = params.get("FlowType")
        self._FlowDescription = params.get("FlowDescription")
        self._Deadline = params.get("Deadline")
        self._CallbackUrl = params.get("CallbackUrl")
        self._UserData = params.get("UserData")
        self._Unordered = params.get("Unordered")
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self._Components.append(obj)
        self._NeedSignReview = params.get("NeedSignReview")
        self._AutoSignScene = params.get("AutoSignScene")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowGroupOptions(AbstractModel):
    """此结构体(FlowGroupOptions)描述的是合同组的个性化配置，支持控制是否发送短信、未实名个人签署方查看合同组时是否需要实名认证（仅在合同组文件发起配置时生效）

    """

    def __init__(self):
        r"""
        :param _ApproverVerifyType: 发起合同（流程）组的合同（流程）签署人校验方式
VerifyCheck: 人脸识别（默认）
MobileCheck：手机号验证
参数说明：此参数仅在合同组文件发起有效，可选人脸识别或手机号验证两种方式，若选择后者，未实名个人签署方在签署合同时，无需经过实名认证和意愿确认两次人脸识别，该能力仅适用于个人签署方。
        :type ApproverVerifyType: str
        :param _SelfOrganizationApproverNotifyType: 发起合同（流程）组本方企业经办人通知方式
签署通知类型：sms--短信，none--不通知
        :type SelfOrganizationApproverNotifyType: str
        :param _OtherApproverNotifyType: 发起合同（流程）组他方经办人通知方式
签署通知类型：sms--短信，none--不通知
        :type OtherApproverNotifyType: str
        """
        self._ApproverVerifyType = None
        self._SelfOrganizationApproverNotifyType = None
        self._OtherApproverNotifyType = None

    @property
    def ApproverVerifyType(self):
        return self._ApproverVerifyType

    @ApproverVerifyType.setter
    def ApproverVerifyType(self, ApproverVerifyType):
        self._ApproverVerifyType = ApproverVerifyType

    @property
    def SelfOrganizationApproverNotifyType(self):
        return self._SelfOrganizationApproverNotifyType

    @SelfOrganizationApproverNotifyType.setter
    def SelfOrganizationApproverNotifyType(self, SelfOrganizationApproverNotifyType):
        self._SelfOrganizationApproverNotifyType = SelfOrganizationApproverNotifyType

    @property
    def OtherApproverNotifyType(self):
        return self._OtherApproverNotifyType

    @OtherApproverNotifyType.setter
    def OtherApproverNotifyType(self, OtherApproverNotifyType):
        self._OtherApproverNotifyType = OtherApproverNotifyType


    def _deserialize(self, params):
        self._ApproverVerifyType = params.get("ApproverVerifyType")
        self._SelfOrganizationApproverNotifyType = params.get("SelfOrganizationApproverNotifyType")
        self._OtherApproverNotifyType = params.get("OtherApproverNotifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FormField(AbstractModel):
    """电子文档的控件填充信息。按照控件类型进行相应的填充。

    【数据表格传参说明】
    当模板的 ComponentType='DYNAMIC_TABLE'时，FormField.ComponentValue需要传递json格式的字符串参数，用于确定表头&填充数据表格（支持内容的单元格合并）
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
        :param _ComponentValue: 控件填充vaule，ComponentType和传入值类型对应关系：
TEXT - 文本内容
MULTI_LINE_TEXT - 文本内容
CHECK_BOX - true/false
FILL_IMAGE、ATTACHMENT - 附件的FileId，需要通过UploadFiles接口上传获取
SELECTOR - 选项值
DYNAMIC_TABLE - 传入json格式的表格内容，具体见数据结构FlowInfo：https://cloud.tencent.com/document/api/1420/61525#FlowInfo
        :type ComponentValue: str
        :param _ComponentId: 控件id，和ComponentName选择一项传入即可
        :type ComponentId: str
        :param _ComponentName: 控件名字，最大长度不超过30字符，和ComponentId选择一项传入即可
        :type ComponentName: str
        """
        self._ComponentValue = None
        self._ComponentId = None
        self._ComponentName = None

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


    def _deserialize(self, params):
        self._ComponentValue = params.get("ComponentValue")
        self._ComponentId = params.get("ComponentId")
        self._ComponentName = params.get("ComponentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskResultApiRequest(AbstractModel):
    """GetTaskResultApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id，通过CreateConvertTaskApi得到
        :type TaskId: str
        :param _Operator: 操作人信息,UserId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Agent: 应用号信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Organization: 暂未开放
        :type Organization: :class:`tencentcloud.ess.v20201111.models.OrganizationInfo`
        """
        self._TaskId = None
        self._Operator = None
        self._Agent = None
        self._Organization = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Agent(self):
        warnings.warn("parameter `Agent` is deprecated", DeprecationWarning) 

        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        warnings.warn("parameter `Agent` is deprecated", DeprecationWarning) 

        self._Agent = Agent

    @property
    def Organization(self):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        warnings.warn("parameter `Organization` is deprecated", DeprecationWarning) 

        self._Organization = Organization


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
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
        


class GetTaskResultApiResponse(AbstractModel):
    """GetTaskResultApi返回参数结构体

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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._TaskStatus = None
        self._TaskMessage = None
        self._ResourceId = None
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
        self._RequestId = params.get("RequestId")


class GroupOrganization(AbstractModel):
    """成员企业信息

    """

    def __init__(self):
        r"""
        :param _Name: 成员企业名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Alias: 成员企业别名
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param _OrganizationId: 成员企业id
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationId: str
        :param _UpdateTime: 更新时间，时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param _Status: 成员企业加入集团的当前状态:1-待授权;2-已授权待激活;3-拒绝授权;4-已解除;5-已加入
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _IsMainOrganization: 是否为集团主企业
注意：此字段可能返回 null，表示取不到有效值。
        :type IsMainOrganization: bool
        :param _IdCardNumber: 企业社会信用代码
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardNumber: str
        :param _AdminInfo: 企业超管信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminInfo: :class:`tencentcloud.ess.v20201111.models.Admin`
        :param _License: 企业许可证
注意：此字段可能返回 null，表示取不到有效值。
        :type License: str
        :param _LicenseExpireTime: 企业许可证过期时间，时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseExpireTime: int
        :param _JoinTime: 成员企业加入集团时间，时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type JoinTime: int
        :param _FlowEngineEnable: 是否使用审批流引擎，true-是，false-否
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowEngineEnable: bool
        """
        self._Name = None
        self._Alias = None
        self._OrganizationId = None
        self._UpdateTime = None
        self._Status = None
        self._IsMainOrganization = None
        self._IdCardNumber = None
        self._AdminInfo = None
        self._License = None
        self._LicenseExpireTime = None
        self._JoinTime = None
        self._FlowEngineEnable = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsMainOrganization(self):
        return self._IsMainOrganization

    @IsMainOrganization.setter
    def IsMainOrganization(self, IsMainOrganization):
        self._IsMainOrganization = IsMainOrganization

    @property
    def IdCardNumber(self):
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def AdminInfo(self):
        return self._AdminInfo

    @AdminInfo.setter
    def AdminInfo(self, AdminInfo):
        self._AdminInfo = AdminInfo

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def LicenseExpireTime(self):
        return self._LicenseExpireTime

    @LicenseExpireTime.setter
    def LicenseExpireTime(self, LicenseExpireTime):
        self._LicenseExpireTime = LicenseExpireTime

    @property
    def JoinTime(self):
        return self._JoinTime

    @JoinTime.setter
    def JoinTime(self, JoinTime):
        self._JoinTime = JoinTime

    @property
    def FlowEngineEnable(self):
        return self._FlowEngineEnable

    @FlowEngineEnable.setter
    def FlowEngineEnable(self, FlowEngineEnable):
        self._FlowEngineEnable = FlowEngineEnable


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Alias = params.get("Alias")
        self._OrganizationId = params.get("OrganizationId")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._IsMainOrganization = params.get("IsMainOrganization")
        self._IdCardNumber = params.get("IdCardNumber")
        if params.get("AdminInfo") is not None:
            self._AdminInfo = Admin()
            self._AdminInfo._deserialize(params.get("AdminInfo"))
        self._License = params.get("License")
        self._LicenseExpireTime = params.get("LicenseExpireTime")
        self._JoinTime = params.get("JoinTime")
        self._FlowEngineEnable = params.get("FlowEngineEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HasAuthUser(AbstractModel):
    """被授权用户信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户id
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _BelongTo: 用户归属
MainOrg：主企业
CurrentOrg：当前企业
注意：此字段可能返回 null，表示取不到有效值。
        :type BelongTo: str
        """
        self._UserId = None
        self._BelongTo = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def BelongTo(self):
        return self._BelongTo

    @BelongTo.setter
    def BelongTo(self, BelongTo):
        self._BelongTo = BelongTo


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._BelongTo = params.get("BelongTo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntegrateRole(AbstractModel):
    """企业角色数据信息

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色id
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleId: str
        :param _RoleName: 角色名
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleName: str
        :param _RoleStatus: 角色状态，1-启用，2-禁用
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleStatus: int
        :param _IsGroupRole: 是否是集团角色，true-是，false-否
注意：此字段可能返回 null，表示取不到有效值。
        :type IsGroupRole: bool
        :param _SubOrgIdList: 管辖的子企业列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SubOrgIdList: list of str
        """
        self._RoleId = None
        self._RoleName = None
        self._RoleStatus = None
        self._IsGroupRole = None
        self._SubOrgIdList = None

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
    def IsGroupRole(self):
        return self._IsGroupRole

    @IsGroupRole.setter
    def IsGroupRole(self, IsGroupRole):
        self._IsGroupRole = IsGroupRole

    @property
    def SubOrgIdList(self):
        return self._SubOrgIdList

    @SubOrgIdList.setter
    def SubOrgIdList(self, SubOrgIdList):
        self._SubOrgIdList = SubOrgIdList


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        self._RoleStatus = params.get("RoleStatus")
        self._IsGroupRole = params.get("IsGroupRole")
        self._SubOrgIdList = params.get("SubOrgIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntegrationDepartment(AbstractModel):
    """部门信息

    """

    def __init__(self):
        r"""
        :param _DeptId: 部门ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeptId: str
        :param _DeptName: 部门名
注意：此字段可能返回 null，表示取不到有效值。
        :type DeptName: str
        :param _ParentDeptId: 父部门ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentDeptId: str
        :param _DeptOpenId: 客户系统部门ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeptOpenId: str
        :param _OrderNo: 序列号
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderNo: int
        """
        self._DeptId = None
        self._DeptName = None
        self._ParentDeptId = None
        self._DeptOpenId = None
        self._OrderNo = None

    @property
    def DeptId(self):
        return self._DeptId

    @DeptId.setter
    def DeptId(self, DeptId):
        self._DeptId = DeptId

    @property
    def DeptName(self):
        return self._DeptName

    @DeptName.setter
    def DeptName(self, DeptName):
        self._DeptName = DeptName

    @property
    def ParentDeptId(self):
        return self._ParentDeptId

    @ParentDeptId.setter
    def ParentDeptId(self, ParentDeptId):
        self._ParentDeptId = ParentDeptId

    @property
    def DeptOpenId(self):
        return self._DeptOpenId

    @DeptOpenId.setter
    def DeptOpenId(self, DeptOpenId):
        self._DeptOpenId = DeptOpenId

    @property
    def OrderNo(self):
        return self._OrderNo

    @OrderNo.setter
    def OrderNo(self, OrderNo):
        self._OrderNo = OrderNo


    def _deserialize(self, params):
        self._DeptId = params.get("DeptId")
        self._DeptName = params.get("DeptName")
        self._ParentDeptId = params.get("ParentDeptId")
        self._DeptOpenId = params.get("DeptOpenId")
        self._OrderNo = params.get("OrderNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntegrationMainOrganizationUser(AbstractModel):
    """主企业员工账号信息

    """

    def __init__(self):
        r"""
        :param _MainOrganizationId: 主企业id
注意：此字段可能返回 null，表示取不到有效值。
        :type MainOrganizationId: str
        :param _MainUserId: 主企业员工UserId
注意：此字段可能返回 null，表示取不到有效值。
        :type MainUserId: str
        :param _UserName: 主企业员工名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        """
        self._MainOrganizationId = None
        self._MainUserId = None
        self._UserName = None

    @property
    def MainOrganizationId(self):
        return self._MainOrganizationId

    @MainOrganizationId.setter
    def MainOrganizationId(self, MainOrganizationId):
        self._MainOrganizationId = MainOrganizationId

    @property
    def MainUserId(self):
        return self._MainUserId

    @MainUserId.setter
    def MainUserId(self, MainUserId):
        self._MainUserId = MainUserId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._MainOrganizationId = params.get("MainOrganizationId")
        self._MainUserId = params.get("MainUserId")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationCallbackInfoRequest(AbstractModel):
    """ModifyApplicationCallbackInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _OperateType: 操作类型：1-新增，2-删除
        :type OperateType: int
        :param _CallbackInfo: 回调信息
        :type CallbackInfo: :class:`tencentcloud.ess.v20201111.models.CallbackInfo`
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._OperateType = None
        self._CallbackInfo = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def OperateType(self):
        return self._OperateType

    @OperateType.setter
    def OperateType(self, OperateType):
        self._OperateType = OperateType

    @property
    def CallbackInfo(self):
        return self._CallbackInfo

    @CallbackInfo.setter
    def CallbackInfo(self, CallbackInfo):
        self._CallbackInfo = CallbackInfo

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._OperateType = params.get("OperateType")
        if params.get("CallbackInfo") is not None:
            self._CallbackInfo = CallbackInfo()
            self._CallbackInfo._deserialize(params.get("CallbackInfo"))
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
        


class ModifyApplicationCallbackInfoResponse(AbstractModel):
    """ModifyApplicationCallbackInfo返回参数结构体

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


class ModifyIntegrationDepartmentRequest(AbstractModel):
    """ModifyIntegrationDepartment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息，UserId必填且需拥有组织架构管理权限
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _DeptId: 电子签部门ID
        :type DeptId: str
        :param _ParentDeptId: 电子签父部门ID
        :type ParentDeptId: str
        :param _DeptName: 部门名称，不超过50个字符
        :type DeptName: str
        :param _DeptOpenId: 客户系统部门ID，不超过64个字符
        :type DeptOpenId: str
        :param _OrderNo: 排序号,1~30000范围内
        :type OrderNo: int
        """
        self._Operator = None
        self._DeptId = None
        self._ParentDeptId = None
        self._DeptName = None
        self._DeptOpenId = None
        self._OrderNo = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def DeptId(self):
        return self._DeptId

    @DeptId.setter
    def DeptId(self, DeptId):
        self._DeptId = DeptId

    @property
    def ParentDeptId(self):
        return self._ParentDeptId

    @ParentDeptId.setter
    def ParentDeptId(self, ParentDeptId):
        self._ParentDeptId = ParentDeptId

    @property
    def DeptName(self):
        return self._DeptName

    @DeptName.setter
    def DeptName(self, DeptName):
        self._DeptName = DeptName

    @property
    def DeptOpenId(self):
        return self._DeptOpenId

    @DeptOpenId.setter
    def DeptOpenId(self, DeptOpenId):
        self._DeptOpenId = DeptOpenId

    @property
    def OrderNo(self):
        return self._OrderNo

    @OrderNo.setter
    def OrderNo(self, OrderNo):
        self._OrderNo = OrderNo


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._DeptId = params.get("DeptId")
        self._ParentDeptId = params.get("ParentDeptId")
        self._DeptName = params.get("DeptName")
        self._DeptOpenId = params.get("DeptOpenId")
        self._OrderNo = params.get("OrderNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIntegrationDepartmentResponse(AbstractModel):
    """ModifyIntegrationDepartment返回参数结构体

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
        :param _Creator: 电子印章授权人的UserId
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
        :param _SealType: 印章类型,OFFICIAL-企业公章, CONTRACT-合同专用章,ORGANIZATIONSEAL-企业印章(本地上传印章类型),LEGAL_PERSON_SEAL-法人印章
        :type SealType: str
        :param _IsAllTime: 用印申请是否为永久授权，true-是，false-否
        :type IsAllTime: bool
        :param _AuthorizedUsers: 授权人列表
注意：此字段可能返回 null，表示取不到有效值。
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
        


class OrganizationInfo(AbstractModel):
    """机构信息

    """

    def __init__(self):
        r"""
        :param _OrganizationId: 机构在平台的编号，内部字段，暂未开放
        :type OrganizationId: str
        :param _Channel: 用户渠道，内部字段，暂未开放
        :type Channel: str
        :param _OrganizationOpenId: 用户在渠道的机构编号，内部字段，暂未开放
        :type OrganizationOpenId: str
        :param _ClientIp: 用户真实的IP，内部字段，暂未开放
        :type ClientIp: str
        :param _ProxyIp: 机构的代理IP，内部字段，暂未开放
        :type ProxyIp: str
        """
        self._OrganizationId = None
        self._Channel = None
        self._OrganizationOpenId = None
        self._ClientIp = None
        self._ProxyIp = None

    @property
    def OrganizationId(self):
        warnings.warn("parameter `OrganizationId` is deprecated", DeprecationWarning) 

        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        warnings.warn("parameter `OrganizationId` is deprecated", DeprecationWarning) 

        self._OrganizationId = OrganizationId

    @property
    def Channel(self):
        warnings.warn("parameter `Channel` is deprecated", DeprecationWarning) 

        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        warnings.warn("parameter `Channel` is deprecated", DeprecationWarning) 

        self._Channel = Channel

    @property
    def OrganizationOpenId(self):
        warnings.warn("parameter `OrganizationOpenId` is deprecated", DeprecationWarning) 

        return self._OrganizationOpenId

    @OrganizationOpenId.setter
    def OrganizationOpenId(self, OrganizationOpenId):
        warnings.warn("parameter `OrganizationOpenId` is deprecated", DeprecationWarning) 

        self._OrganizationOpenId = OrganizationOpenId

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
        self._OrganizationId = params.get("OrganizationId")
        self._Channel = params.get("Channel")
        self._OrganizationOpenId = params.get("OrganizationOpenId")
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
        :param _ComponentPosX: 签名域横坐标，单位pt
        :type ComponentPosX: float
        :param _ComponentPosY: 签名域纵坐标，单位pt
        :type ComponentPosY: float
        :param _ComponentWidth: 签名域宽度，单位pt
        :type ComponentWidth: float
        :param _ComponentHeight: 签名域高度，单位pt
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
        


class Recipient(AbstractModel):
    """签署参与者信息

    """

    def __init__(self):
        r"""
        :param _RecipientId: 签署参与者ID
        :type RecipientId: str
        :param _RecipientType: 参与者类型。默认为空。ENTERPRISE-企业；INDIVIDUAL-个人；PROMOTER-发起方
        :type RecipientType: str
        :param _Description: 描述信息
        :type Description: str
        :param _RoleName: 角色名称
        :type RoleName: str
        :param _RequireValidation: 是否需要验证，默认为false
        :type RequireValidation: bool
        :param _RequireSign: 是否需要签署，默认为true
        :type RequireSign: bool
        :param _RoutingOrder: 添加序列，0～N
        :type RoutingOrder: int
        :param _RequireDelivery: 是否需要发送，默认为true
        :type RequireDelivery: bool
        :param _Email: 邮箱地址
        :type Email: str
        :param _Mobile: 电话号码
        :type Mobile: str
        :param _UserId: 关联的用户ID
        :type UserId: str
        :param _DeliveryMethod: 发送方式。默认为EMAIL。EMAIL-邮件；MOBILE-手机短信；WECHAT-微信通知
        :type DeliveryMethod: str
        :param _RecipientExtra: 附属信息
        :type RecipientExtra: str
        """
        self._RecipientId = None
        self._RecipientType = None
        self._Description = None
        self._RoleName = None
        self._RequireValidation = None
        self._RequireSign = None
        self._RoutingOrder = None
        self._RequireDelivery = None
        self._Email = None
        self._Mobile = None
        self._UserId = None
        self._DeliveryMethod = None
        self._RecipientExtra = None

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
    def RoutingOrder(self):
        return self._RoutingOrder

    @RoutingOrder.setter
    def RoutingOrder(self, RoutingOrder):
        self._RoutingOrder = RoutingOrder

    @property
    def RequireDelivery(self):
        return self._RequireDelivery

    @RequireDelivery.setter
    def RequireDelivery(self, RequireDelivery):
        self._RequireDelivery = RequireDelivery

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def DeliveryMethod(self):
        return self._DeliveryMethod

    @DeliveryMethod.setter
    def DeliveryMethod(self, DeliveryMethod):
        self._DeliveryMethod = DeliveryMethod

    @property
    def RecipientExtra(self):
        return self._RecipientExtra

    @RecipientExtra.setter
    def RecipientExtra(self, RecipientExtra):
        self._RecipientExtra = RecipientExtra


    def _deserialize(self, params):
        self._RecipientId = params.get("RecipientId")
        self._RecipientType = params.get("RecipientType")
        self._Description = params.get("Description")
        self._RoleName = params.get("RoleName")
        self._RequireValidation = params.get("RequireValidation")
        self._RequireSign = params.get("RequireSign")
        self._RoutingOrder = params.get("RoutingOrder")
        self._RequireDelivery = params.get("RequireDelivery")
        self._Email = params.get("Email")
        self._Mobile = params.get("Mobile")
        self._UserId = params.get("UserId")
        self._DeliveryMethod = params.get("DeliveryMethod")
        self._RecipientExtra = params.get("RecipientExtra")
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
        


class RegisterInfo(AbstractModel):
    """发起流程快速注册相关信息

    """

    def __init__(self):
        r"""
        :param _LegalName: 法人姓名
        :type LegalName: str
        :param _Uscc: 社会统一信用代码
        :type Uscc: str
        :param _UnifiedSocialCreditCode: 社会统一信用代码
        :type UnifiedSocialCreditCode: str
        """
        self._LegalName = None
        self._Uscc = None
        self._UnifiedSocialCreditCode = None

    @property
    def LegalName(self):
        return self._LegalName

    @LegalName.setter
    def LegalName(self, LegalName):
        self._LegalName = LegalName

    @property
    def Uscc(self):
        warnings.warn("parameter `Uscc` is deprecated", DeprecationWarning) 

        return self._Uscc

    @Uscc.setter
    def Uscc(self, Uscc):
        warnings.warn("parameter `Uscc` is deprecated", DeprecationWarning) 

        self._Uscc = Uscc

    @property
    def UnifiedSocialCreditCode(self):
        return self._UnifiedSocialCreditCode

    @UnifiedSocialCreditCode.setter
    def UnifiedSocialCreditCode(self, UnifiedSocialCreditCode):
        self._UnifiedSocialCreditCode = UnifiedSocialCreditCode


    def _deserialize(self, params):
        self._LegalName = params.get("LegalName")
        self._Uscc = params.get("Uscc")
        self._UnifiedSocialCreditCode = params.get("UnifiedSocialCreditCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleasedApprover(AbstractModel):
    """解除协议的签署人，如不指定，默认使用待解除流程（即原流程）中的签署人。
    注意：不支持更换C端（个人身份类型）签署人，如果原流程中含有C端签署人，默认使用原流程中的该C端签署人。
    注意：目前不支持替换C端（个人身份类型）签署人，但是可以指定C端签署人的签署方自定义控件别名，具体见参数ApproverSignRole描述。
    注意：当指定C端签署人的签署方自定义控件别名不空时，除RelievedApproverReceiptId参数外，可以只参数ApproverSignRole。

    """

    def __init__(self):
        r"""
        :param _Name: 签署人姓名，最大长度50个字符

        :type Name: str
        :param _Mobile: 签署人手机号
        :type Mobile: str
        :param _RelievedApproverReceiptId: 要替换的参与人在原合同参与人列表中的签署人编号,通过DescribeFlowInfo 接口获取（即FlowDetailInfos. FlowApproverInfos 结构中的ReceiptId ）
        :type RelievedApproverReceiptId: str
        :param _ApproverType: 指定签署人类型，目前仅支持
ORGANIZATION-企业
ENTERPRISESERVER-企业静默签
        :type ApproverType: str
        :param _ApproverSignComponentType: 签署控件类型，支持自定义企业签署方的签署控件为“印章”或“签名”
- SIGN_SEAL-默认为印章控件类型
- SIGN_SIGNATURE-手写签名控件类型
        :type ApproverSignComponentType: str
        :param _ApproverSignRole: 签署方自定义控件别名，最大长度20个字符
        :type ApproverSignRole: str
        """
        self._Name = None
        self._Mobile = None
        self._RelievedApproverReceiptId = None
        self._ApproverType = None
        self._ApproverSignComponentType = None
        self._ApproverSignRole = None

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
    def RelievedApproverReceiptId(self):
        return self._RelievedApproverReceiptId

    @RelievedApproverReceiptId.setter
    def RelievedApproverReceiptId(self, RelievedApproverReceiptId):
        self._RelievedApproverReceiptId = RelievedApproverReceiptId

    @property
    def ApproverType(self):
        return self._ApproverType

    @ApproverType.setter
    def ApproverType(self, ApproverType):
        self._ApproverType = ApproverType

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
        self._Name = params.get("Name")
        self._Mobile = params.get("Mobile")
        self._RelievedApproverReceiptId = params.get("RelievedApproverReceiptId")
        self._ApproverType = params.get("ApproverType")
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
        


class ReviewerInfo(AbstractModel):
    """关注方信息

    """

    def __init__(self):
        r"""
        :param _Name: 姓名
        :type Name: str
        :param _Mobile: 手机号
        :type Mobile: str
        """
        self._Name = None
        self._Mobile = None

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
        self._Name = params.get("Name")
        self._Mobile = params.get("Mobile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SealInfo(AbstractModel):
    """模板结构体中的印章信息

    """


class SignQrCode(AbstractModel):
    """一码多扫签署二维码对象

    """

    def __init__(self):
        r"""
        :param _QrCodeId: 二维码id
        :type QrCodeId: str
        :param _QrCodeUrl: 二维码url
        :type QrCodeUrl: str
        :param _ExpiredTime: 二维码过期时间戳，单位秒
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
        


class Staff(AbstractModel):
    """企业员工信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户在电子签平台的id
注：创建和更新场景无需填写
        :type UserId: str
        :param _DisplayName: 显示的用户名/昵称
        :type DisplayName: str
        :param _Mobile: 用户手机号
        :type Mobile: str
        :param _Email: 用户邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _OpenId: 用户在第三方平台id，如需在此接口提醒员工实名，该参数不传
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param _Roles: 员工角色
注：创建和更新场景无需填写
注意：此字段可能返回 null，表示取不到有效值。
        :type Roles: list of StaffRole
        :param _Department: 员工部门
注意：此字段可能返回 null，表示取不到有效值。
        :type Department: :class:`tencentcloud.ess.v20201111.models.Department`
        :param _Verified: 员工是否实名
注：创建和更新场景无需填写
        :type Verified: bool
        :param _CreatedOn: 员工创建时间戳，单位秒
注：创建和更新场景无需填写
        :type CreatedOn: int
        :param _VerifiedOn: 员工实名时间戳，单位秒
注：创建和更新场景无需填写
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifiedOn: int
        :param _QuiteJob: 员工是否离职：0-未离职，1-离职
注：创建和更新场景无需填写
注意：此字段可能返回 null，表示取不到有效值。
        :type QuiteJob: int
        :param _ReceiveUserId: 员工离职交接人用户id
注：创建和更新场景无需填写
        :type ReceiveUserId: str
        :param _ReceiveOpenId: 员工离职交接人用户OpenId
注：创建和更新场景无需填写
        :type ReceiveOpenId: str
        :param _WeworkOpenId: 企业微信用户账号ID
注：仅企微类型的企业创建员工接口支持该字段
注意：此字段可能返回 null，表示取不到有效值。
        :type WeworkOpenId: str
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
        self._ReceiveUserId = None
        self._ReceiveOpenId = None
        self._WeworkOpenId = None

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

    @property
    def ReceiveUserId(self):
        return self._ReceiveUserId

    @ReceiveUserId.setter
    def ReceiveUserId(self, ReceiveUserId):
        self._ReceiveUserId = ReceiveUserId

    @property
    def ReceiveOpenId(self):
        return self._ReceiveOpenId

    @ReceiveOpenId.setter
    def ReceiveOpenId(self, ReceiveOpenId):
        self._ReceiveOpenId = ReceiveOpenId

    @property
    def WeworkOpenId(self):
        return self._WeworkOpenId

    @WeworkOpenId.setter
    def WeworkOpenId(self, WeworkOpenId):
        self._WeworkOpenId = WeworkOpenId


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
        self._ReceiveUserId = params.get("ReceiveUserId")
        self._ReceiveOpenId = params.get("ReceiveOpenId")
        self._WeworkOpenId = params.get("WeworkOpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffRole(AbstractModel):
    """集成版企业角色信息

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
        


class StartFlowRequest(AbstractModel):
    """StartFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填。支持填入集团子公司经办人 userId代发合同。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowId: 签署流程编号，由CreateFlow接口返回
        :type FlowId: str
        :param _ClientToken: 客户端Token，保持接口幂等性,最大长度64个字符
        :type ClientToken: str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _CcNotifyType: 给关注人发送短信通知的类型，0-合同发起时通知 1-签署完成后通知
        :type CcNotifyType: int
        """
        self._Operator = None
        self._FlowId = None
        self._ClientToken = None
        self._Agent = None
        self._CcNotifyType = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def CcNotifyType(self):
        return self._CcNotifyType

    @CcNotifyType.setter
    def CcNotifyType(self, CcNotifyType):
        self._CcNotifyType = CcNotifyType


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowId = params.get("FlowId")
        self._ClientToken = params.get("ClientToken")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._CcNotifyType = params.get("CcNotifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartFlowResponse(AbstractModel):
    """StartFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 返回描述，START-发起成功， REVIEW-提交审核成功，EXECUTING-已提交发起任务
        :type Status: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class SuccessCreateStaffData(AbstractModel):
    """创建员工的成功数据

    """

    def __init__(self):
        r"""
        :param _DisplayName: 员工名
        :type DisplayName: str
        :param _Mobile: 员工手机号
        :type Mobile: str
        :param _UserId: 员工在电子签平台的id
        :type UserId: str
        :param _Note: 提示，当创建已存在未实名用户时，该字段有值
注意：此字段可能返回 null，表示取不到有效值。
        :type Note: str
        :param _WeworkOpenId: 传入的企微账号id
        :type WeworkOpenId: str
        """
        self._DisplayName = None
        self._Mobile = None
        self._UserId = None
        self._Note = None
        self._WeworkOpenId = None

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
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def WeworkOpenId(self):
        return self._WeworkOpenId

    @WeworkOpenId.setter
    def WeworkOpenId(self, WeworkOpenId):
        self._WeworkOpenId = WeworkOpenId


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._Mobile = params.get("Mobile")
        self._UserId = params.get("UserId")
        self._Note = params.get("Note")
        self._WeworkOpenId = params.get("WeworkOpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuccessDeleteStaffData(AbstractModel):
    """删除员工的成功数据

    """

    def __init__(self):
        r"""
        :param _DisplayName: 员工名
        :type DisplayName: str
        :param _Mobile: 员工手机号
        :type Mobile: str
        :param _UserId: 员工在电子签平台的id
        :type UserId: str
        """
        self._DisplayName = None
        self._Mobile = None
        self._UserId = None

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
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._Mobile = params.get("Mobile")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuccessUpdateStaffData(AbstractModel):
    """更新员工信息成功返回的数据信息

    """

    def __init__(self):
        r"""
        :param _DisplayName: 传入的用户名称
        :type DisplayName: str
        :param _Mobile: 传入的手机号
        :type Mobile: str
        :param _UserId: 用户Id
        :type UserId: str
        """
        self._DisplayName = None
        self._Mobile = None
        self._UserId = None

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
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._Mobile = params.get("Mobile")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateInfo(AbstractModel):
    """企业模板的信息结构

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID
        :type TemplateId: str
        :param _TemplateName: 模板名字
        :type TemplateName: str
        :param _Description: 模板描述信息
        :type Description: str
        :param _DocumentResourceIds: 模板关联的资源ID列表
        :type DocumentResourceIds: list of str
        :param _FileInfos: 返回的文件信息结构
        :type FileInfos: list of FileInfo
        :param _AttachmentResourceIds: 附件关联的资源ID
        :type AttachmentResourceIds: list of str
        :param _SignOrder: 签署顺序
        :type SignOrder: list of int
        :param _Recipients: 签署参与者的信息
        :type Recipients: list of Recipient
        :param _Components: 模板信息结构
        :type Components: list of Component
        :param _SignComponents: 签署区模板信息结构
        :type SignComponents: list of Component
        :param _Status: 模板状态(-1:不可用；0:草稿态；1:正式态)
        :type Status: int
        :param _Creator: 模板的创建人UserId
        :type Creator: str
        :param _CreatedOn: 模板创建的时间戳，单位秒
        :type CreatedOn: int
        :param _Promoter: 发起人角色信息
        :type Promoter: :class:`tencentcloud.ess.v20201111.models.Recipient`
        :param _TemplateType: 模板类型
取值：
1  静默签,
3  普通模板
        :type TemplateType: int
        :param _Available: 模板可用状态，取值：1启用（默认），2停用
        :type Available: int
        :param _OrganizationId: 创建模板的机构id
        :type OrganizationId: str
        :param _PreviewUrl: 模板预览链接，有效时间5分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewUrl: str
        :param _TemplateVersion: 模板版本。默认为空时，全数字字符，初始版本为yyyyMMdd001。
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateVersion: str
        :param _Published: 模板是否已发布。true-已发布；false-未发布
注意：此字段可能返回 null，表示取不到有效值。
        :type Published: bool
        :param _TemplateSeals: 模板内部指定的印章列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateSeals: list of SealInfo
        :param _Seals: 模板内部指定的印章列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Seals: list of SealInfo
        """
        self._TemplateId = None
        self._TemplateName = None
        self._Description = None
        self._DocumentResourceIds = None
        self._FileInfos = None
        self._AttachmentResourceIds = None
        self._SignOrder = None
        self._Recipients = None
        self._Components = None
        self._SignComponents = None
        self._Status = None
        self._Creator = None
        self._CreatedOn = None
        self._Promoter = None
        self._TemplateType = None
        self._Available = None
        self._OrganizationId = None
        self._PreviewUrl = None
        self._TemplateVersion = None
        self._Published = None
        self._TemplateSeals = None
        self._Seals = None

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
    def DocumentResourceIds(self):
        return self._DocumentResourceIds

    @DocumentResourceIds.setter
    def DocumentResourceIds(self, DocumentResourceIds):
        self._DocumentResourceIds = DocumentResourceIds

    @property
    def FileInfos(self):
        return self._FileInfos

    @FileInfos.setter
    def FileInfos(self, FileInfos):
        self._FileInfos = FileInfos

    @property
    def AttachmentResourceIds(self):
        return self._AttachmentResourceIds

    @AttachmentResourceIds.setter
    def AttachmentResourceIds(self, AttachmentResourceIds):
        self._AttachmentResourceIds = AttachmentResourceIds

    @property
    def SignOrder(self):
        return self._SignOrder

    @SignOrder.setter
    def SignOrder(self, SignOrder):
        self._SignOrder = SignOrder

    @property
    def Recipients(self):
        return self._Recipients

    @Recipients.setter
    def Recipients(self, Recipients):
        self._Recipients = Recipients

    @property
    def Components(self):
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def SignComponents(self):
        return self._SignComponents

    @SignComponents.setter
    def SignComponents(self, SignComponents):
        self._SignComponents = SignComponents

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
    def Promoter(self):
        return self._Promoter

    @Promoter.setter
    def Promoter(self, Promoter):
        self._Promoter = Promoter

    @property
    def TemplateType(self):
        return self._TemplateType

    @TemplateType.setter
    def TemplateType(self, TemplateType):
        self._TemplateType = TemplateType

    @property
    def Available(self):
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def PreviewUrl(self):
        return self._PreviewUrl

    @PreviewUrl.setter
    def PreviewUrl(self, PreviewUrl):
        self._PreviewUrl = PreviewUrl

    @property
    def TemplateVersion(self):
        return self._TemplateVersion

    @TemplateVersion.setter
    def TemplateVersion(self, TemplateVersion):
        self._TemplateVersion = TemplateVersion

    @property
    def Published(self):
        return self._Published

    @Published.setter
    def Published(self, Published):
        self._Published = Published

    @property
    def TemplateSeals(self):
        return self._TemplateSeals

    @TemplateSeals.setter
    def TemplateSeals(self, TemplateSeals):
        self._TemplateSeals = TemplateSeals

    @property
    def Seals(self):
        warnings.warn("parameter `Seals` is deprecated", DeprecationWarning) 

        return self._Seals

    @Seals.setter
    def Seals(self, Seals):
        warnings.warn("parameter `Seals` is deprecated", DeprecationWarning) 

        self._Seals = Seals


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._Description = params.get("Description")
        self._DocumentResourceIds = params.get("DocumentResourceIds")
        if params.get("FileInfos") is not None:
            self._FileInfos = []
            for item in params.get("FileInfos"):
                obj = FileInfo()
                obj._deserialize(item)
                self._FileInfos.append(obj)
        self._AttachmentResourceIds = params.get("AttachmentResourceIds")
        self._SignOrder = params.get("SignOrder")
        if params.get("Recipients") is not None:
            self._Recipients = []
            for item in params.get("Recipients"):
                obj = Recipient()
                obj._deserialize(item)
                self._Recipients.append(obj)
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self._Components.append(obj)
        if params.get("SignComponents") is not None:
            self._SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self._SignComponents.append(obj)
        self._Status = params.get("Status")
        self._Creator = params.get("Creator")
        self._CreatedOn = params.get("CreatedOn")
        if params.get("Promoter") is not None:
            self._Promoter = Recipient()
            self._Promoter._deserialize(params.get("Promoter"))
        self._TemplateType = params.get("TemplateType")
        self._Available = params.get("Available")
        self._OrganizationId = params.get("OrganizationId")
        self._PreviewUrl = params.get("PreviewUrl")
        self._TemplateVersion = params.get("TemplateVersion")
        self._Published = params.get("Published")
        if params.get("TemplateSeals") is not None:
            self._TemplateSeals = []
            for item in params.get("TemplateSeals"):
                obj = SealInfo()
                obj._deserialize(item)
                self._TemplateSeals.append(obj)
        if params.get("Seals") is not None:
            self._Seals = []
            for item in params.get("Seals"):
                obj = SealInfo()
                obj._deserialize(item)
                self._Seals.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindEmployeeUserIdWithClientOpenIdRequest(AbstractModel):
    """UnbindEmployeeUserIdWithClientOpenId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 用户信息，OpenId与UserId二选一必填一个，OpenId是第三方客户ID，userId是用户实名后的电子签生成的ID,当传入客户系统openId，传入的openId需与电子签员工userId绑定，且参数Channel必填，Channel值为INTEGRATE；当传入参数UserId，Channel无需指定(参数用法参考示例)
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _UserId: 电子签系统员工UserId
        :type UserId: str
        :param _OpenId: 客户系统OpenId
        :type OpenId: str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._UserId = None
        self._OpenId = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

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
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._UserId = params.get("UserId")
        self._OpenId = params.get("OpenId")
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
        


class UnbindEmployeeUserIdWithClientOpenIdResponse(AbstractModel):
    """UnbindEmployeeUserIdWithClientOpenId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 解绑是否成功，1表示成功，0表示失败
        :type Status: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class UpdateIntegrationEmployeesRequest(AbstractModel):
    """UpdateIntegrationEmployees请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息，userId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Employees: 员工信息，不超过100个。
根据UserId或OpenId更新员工，必填一个，优先UserId。
可更新Mobile、DisplayName、Email和Department.DepartmentId字段，其他字段暂不支持
        :type Employees: list of Staff
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId需填充子企业Id
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._Employees = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Employees(self):
        return self._Employees

    @Employees.setter
    def Employees(self, Employees):
        self._Employees = Employees

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("Employees") is not None:
            self._Employees = []
            for item in params.get("Employees"):
                obj = Staff()
                obj._deserialize(item)
                self._Employees.append(obj)
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
        


class UpdateIntegrationEmployeesResponse(AbstractModel):
    """UpdateIntegrationEmployees返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessEmployeeData: 更新成功的用户列表
        :type SuccessEmployeeData: list of SuccessUpdateStaffData
        :param _FailedEmployeeData: 更新失败的用户列表
        :type FailedEmployeeData: list of FailedUpdateStaffData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessEmployeeData = None
        self._FailedEmployeeData = None
        self._RequestId = None

    @property
    def SuccessEmployeeData(self):
        return self._SuccessEmployeeData

    @SuccessEmployeeData.setter
    def SuccessEmployeeData(self, SuccessEmployeeData):
        self._SuccessEmployeeData = SuccessEmployeeData

    @property
    def FailedEmployeeData(self):
        return self._FailedEmployeeData

    @FailedEmployeeData.setter
    def FailedEmployeeData(self, FailedEmployeeData):
        self._FailedEmployeeData = FailedEmployeeData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SuccessEmployeeData") is not None:
            self._SuccessEmployeeData = []
            for item in params.get("SuccessEmployeeData"):
                obj = SuccessUpdateStaffData()
                obj._deserialize(item)
                self._SuccessEmployeeData.append(obj)
        if params.get("FailedEmployeeData") is not None:
            self._FailedEmployeeData = []
            for item in params.get("FailedEmployeeData"):
                obj = FailedUpdateStaffData()
                obj._deserialize(item)
                self._FailedEmployeeData.append(obj)
        self._RequestId = params.get("RequestId")


class UploadFile(AbstractModel):
    """此结构体 (UploadFile) 用于描述多文件上传的文件信息。

    """

    def __init__(self):
        r"""
        :param _FileBody: Base64编码后的文件内容
        :type FileBody: str
        :param _FileName: 文件名，最大长度不超过200字符
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
        :param _BusinessType: 文件对应业务类型
1. TEMPLATE - 模板； 文件类型：.pdf/.doc/.docx/.html
2. DOCUMENT - 签署过程及签署后的合同文档/图片控件 文件类型：.pdf/.doc/.docx/.jpg/.png/.xls.xlsx/.html
3. SEAL - 印章； 文件类型：.jpg/.jpeg/.png
        :type BusinessType: str
        :param _Caller: 调用方信息，其中OperatorId为必填字段，即用户的UserId
        :type Caller: :class:`tencentcloud.ess.v20201111.models.Caller`
        :param _FileInfos: 上传文件内容数组，最多支持20个文件
        :type FileInfos: list of UploadFile
        :param _FileType: 文件类型， 默认通过文件内容解析得到文件类型，客户可以显示的说明上传文件的类型。
如：PDF 表示上传的文件 xxx.pdf的文件类型是 PDF
        :type FileType: str
        :param _CoverRect: 此参数只对 PDF 文件有效。是否将pdf灰色矩阵置白
true--是，处理置白
默认为false--否，不处理
        :type CoverRect: bool
        :param _CustomIds: 用户自定义ID数组，与上传文件一一对应
        :type CustomIds: list of str
        :param _FileUrls: 不再使用，上传文件链接数组，最多支持20个URL
        :type FileUrls: str
        """
        self._BusinessType = None
        self._Caller = None
        self._FileInfos = None
        self._FileType = None
        self._CoverRect = None
        self._CustomIds = None
        self._FileUrls = None

    @property
    def BusinessType(self):
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def Caller(self):
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def FileInfos(self):
        return self._FileInfos

    @FileInfos.setter
    def FileInfos(self, FileInfos):
        self._FileInfos = FileInfos

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CoverRect(self):
        return self._CoverRect

    @CoverRect.setter
    def CoverRect(self, CoverRect):
        self._CoverRect = CoverRect

    @property
    def CustomIds(self):
        return self._CustomIds

    @CustomIds.setter
    def CustomIds(self, CustomIds):
        self._CustomIds = CustomIds

    @property
    def FileUrls(self):
        warnings.warn("parameter `FileUrls` is deprecated", DeprecationWarning) 

        return self._FileUrls

    @FileUrls.setter
    def FileUrls(self, FileUrls):
        warnings.warn("parameter `FileUrls` is deprecated", DeprecationWarning) 

        self._FileUrls = FileUrls


    def _deserialize(self, params):
        self._BusinessType = params.get("BusinessType")
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        if params.get("FileInfos") is not None:
            self._FileInfos = []
            for item in params.get("FileInfos"):
                obj = UploadFile()
                obj._deserialize(item)
                self._FileInfos.append(obj)
        self._FileType = params.get("FileType")
        self._CoverRect = params.get("CoverRect")
        self._CustomIds = params.get("CustomIds")
        self._FileUrls = params.get("FileUrls")
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
        :param _FileIds: 文件id数组
        :type FileIds: list of str
        :param _TotalCount: 上传成功文件数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileIds = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FileIds(self):
        return self._FileIds

    @FileIds.setter
    def FileIds(self, FileIds):
        self._FileIds = FileIds

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
        self._FileIds = params.get("FileIds")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class UserInfo(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户在平台的编号
        :type UserId: str
        :param _Channel: 用户的来源渠道，一般不用传，特定场景根据接口说明传值
        :type Channel: str
        :param _OpenId: 用户在渠道的编号，一般不用传，特定场景根据接口说明传值
        :type OpenId: str
        :param _ClientIp: 用户真实IP，内部字段，暂未开放
        :type ClientIp: str
        :param _ProxyIp: 用户代理IP，内部字段，暂未开放
        :type ProxyIp: str
        """
        self._UserId = None
        self._Channel = None
        self._OpenId = None
        self._ClientIp = None
        self._ProxyIp = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Channel(self):
        warnings.warn("parameter `Channel` is deprecated", DeprecationWarning) 

        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        warnings.warn("parameter `Channel` is deprecated", DeprecationWarning) 

        self._Channel = Channel

    @property
    def OpenId(self):
        warnings.warn("parameter `OpenId` is deprecated", DeprecationWarning) 

        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        warnings.warn("parameter `OpenId` is deprecated", DeprecationWarning) 

        self._OpenId = OpenId

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
        self._UserId = params.get("UserId")
        self._Channel = params.get("Channel")
        self._OpenId = params.get("OpenId")
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
        


class VerifyPdfRequest(AbstractModel):
    """VerifyPdf请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: str
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        """
        self._FlowId = None
        self._Operator = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
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
        


class VerifyPdfResponse(AbstractModel):
    """VerifyPdf返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VerifyResult: 验签结果，1-文件未被篡改，全部签名在腾讯电子签完成； 2-文件未被篡改，部分签名在腾讯电子签完成；3-文件被篡改；4-异常：文件内没有签名域；5-异常：文件签名格式错误
        :type VerifyResult: int
        :param _PdfVerifyResults: 验签结果详情,内部状态1-验签成功，在电子签签署；2-验签成功，在其他平台签署；3-验签失败；4-pdf文件没有签名域；5-文件签名格式错误
        :type PdfVerifyResults: list of PdfVerifyResult
        :param _VerifySerialNo: 验签序列号
        :type VerifySerialNo: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VerifyResult = None
        self._PdfVerifyResults = None
        self._VerifySerialNo = None
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
    def VerifySerialNo(self):
        return self._VerifySerialNo

    @VerifySerialNo.setter
    def VerifySerialNo(self, VerifySerialNo):
        self._VerifySerialNo = VerifySerialNo

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
        self._VerifySerialNo = params.get("VerifySerialNo")
        self._RequestId = params.get("RequestId")


class WebThemeConfig(AbstractModel):
    """页面主题配置

    """

    def __init__(self):
        r"""
        :param _DisplaySignBrandLogo: 是否页面底部显示电子签logo
<br/>true：允许在页面底部隐藏电子签logo
<br/>false：不允许允许在页面底部隐藏电子签logo
<br/>默认false，不隐藏logo
        :type DisplaySignBrandLogo: bool
        :param _WebEmbedThemeColor: 主题颜色
<br/>支持十六进制颜色值以及RGB格式颜色值，例如：#D54941，rgb(213, 73, 65)
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
        