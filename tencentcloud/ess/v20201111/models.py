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
    """参与者信息。

    """

    def __init__(self):
        r"""
        :param _ApproverType: 在指定签署方时，可选择企业B端或个人C端等不同的参与者类型，可选类型如下:
**0**：企业
**1**：个人
**3**：企业静默签署
注：`类型为3（企业静默签署）时，此接口会默认完成该签署方的签署。静默签署仅进行盖章操作，不能自动签名。`
**7**: 个人自动签署，适用于个人自动签场景。
注: `个人自动签场景为白名单功能，使用前请联系对接的客户经理沟通。`
        :type ApproverType: int
        :param _ApproverName: 签署方经办人的姓名。
经办人的姓名将用于身份认证和电子签名，请确保填写的姓名为签署方的真实姓名，而非昵称等代名。
        :type ApproverName: str
        :param _ApproverMobile: 签署方经办人手机号码， 支持国内手机号11位数字(无需加+86前缀或其他字符)。
请确认手机号所有方为此合同签署方。
        :type ApproverMobile: str
        :param _OrganizationName: 组织机构名称。
请确认该名称与企业营业执照中注册的名称一致。
如果名称中包含英文括号()，请使用中文括号（）代替。
如果签署方是企业签署方(approverType = 0 或者 approverType = 3)， 则企业名称必填。

        :type OrganizationName: str
        :param _SignComponents: 合同中的签署控件列表，列表中可支持下列多种签署控件,控件的详细定义参考开发者中心的Component结构体
<ul><li> 个人签名/印章</li>
<li> 企业印章</li>
<li> 骑缝章等签署控件</li></ul>
        :type SignComponents: list of Component
        :param _ApproverIdCardType: 签署方经办人的证件类型，支持以下类型
<ul><li>ID_CARD 居民身份证  (默认值)</li>
<li>HONGKONG_AND_MACAO 港澳居民来往内地通行证</li>
<li>HONGKONG_MACAO_AND_TAIWAN 港澳台居民居住证(格式同居民身份证)</li>
<li>OTHER_CARD_TYPE 其他证件</li></ul>

注: `其他证件类型为白名单功能，使用前请联系对接的客户经理沟通。`
        :type ApproverIdCardType: str
        :param _ApproverIdCardNumber: 签署方经办人的证件号码，应符合以下规则
<ul><li>居民身份证号码应为18位字符串，由数字和大写字母X组成（如存在X，请大写）。</li>
<li>港澳居民来往内地通行证号码应为9位字符串，第1位为“C”，第2位为英文字母（但“I”、“O”除外），后7位为阿拉伯数字。</li>
<li>港澳台居民居住证号码编码规则与中国大陆身份证相同，应为18位字符串。</li></ul>
        :type ApproverIdCardNumber: str
        :param _NotifyType: 通知签署方经办人的方式,  有以下途径:
<ul><li>  **sms**  :  (默认)短信</li>
<li>   **none**   : 不通知</li></ul>
        :type NotifyType: str
        :param _ApproverRole: 收据场景设置签署人角色类型, 可以设置如下****类型****:
<ul><li> **1**  :收款人</li>
<li>   **2**   :开具人</li>
<li>   **3** :见证人</li></ul>
注: `收据场景为白名单功能，使用前请联系对接的客户经理沟通。`
        :type ApproverRole: int
        :param _VerifyChannel: 签署意愿确认渠道，默认为WEIXINAPP:人脸识别

注: 将要废弃, 用ApproverSignTypes签署人签署合同时的认证方式代替, 新客户可请用ApproverSignTypes来设置
        :type VerifyChannel: list of str
        :param _PreReadTime: 签署方在签署合同之前，需要强制阅读合同的时长，可指定为3秒至300秒之间的任意值。

若未指定阅读时间，则会按照合同页数大小计算阅读时间，计算规则如下：
<ul><li>合同页数少于等于2页，阅读时间为3秒；</li>
<li>合同页数为3到5页，阅读时间为5秒；</li>
<li>合同页数大于等于6页，阅读时间为10秒。</li></ul>
        :type PreReadTime: int
        :param _UserId: 签署人userId，仅支持本企业的员工userid， 可在控制台组织管理处获得

注: `若传此字段 则以userid的信息为主，会覆盖传递过来的签署人基本信息， 包括姓名，手机号，证件类型等信息`
        :type UserId: str
        :param _ApproverSource: 在企微场景下使用，需设置参数为**WEWORKAPP**，以表明合同来源于企微。
        :type ApproverSource: str
        :param _CustomApproverTag: 在企业微信场景下，表明该合同流程为或签，其最大长度为64位字符串。
所有参与或签的人员均需具备该标识。
注意，在合同中，不同的或签参与人必须保证其CustomApproverTag唯一。
如果或签签署人为本方企业微信参与人，则需要指定ApproverSource参数为WEWORKAPP。
        :type CustomApproverTag: str
        :param _ApproverOption: 可以控制签署方在签署合同时能否进行某些操作，例如拒签、转交他人等。
详细操作可以参考开发者中心的ApproverOption结构体。
        :type ApproverOption: :class:`tencentcloud.ess.v20201111.models.ApproverOption`
        :param _ApproverVerifyTypes: 指定个人签署方查看合同的校验方式,可以传值如下:
<ul><li>  **1**   : （默认）人脸识别,人脸识别后才能合同内容</li>
<li>  **2**  : 手机号验证, 用户手机号和参与方手机号(ApproverMobile)相同即可查看合同内容（当手写签名方式为OCR_ESIGN时，该校验方式无效，因为这种签名方式依赖实名认证）
</li></ul>
注: 
<ul><li>如果合同流程设置ApproverVerifyType查看合同的校验方式,    则忽略此签署人的查看合同的校验方式</li>
<li>此字段不可传多个校验方式</li></ul>
        :type ApproverVerifyTypes: list of int
        :param _ApproverSignTypes: 您可以指定签署方签署合同的认证校验方式，可传递以下值：
<ul><li>**1**：人脸认证，需进行人脸识别成功后才能签署合同；</li>
<li>**2**：签署密码，需输入与用户在腾讯电子签设置的密码一致才能校验成功进行合同签署；</li>
<li>**3**：运营商三要素，需到运营商处比对手机号实名信息（名字、手机号、证件号）校验一致才能成功进行合同签署。</li></ul>
注：
<ul><li>默认情况下，认证校验方式为人脸认证和签署密码两种形式；</li>
<li>您可以传递多种值，表示可用多种认证校验方式。</li></ul>
        :type ApproverSignTypes: list of int
        :param _ApproverNeedSignReview: 发起方企业的签署人进行签署操作前，是否需要企业内部走审批流程，取值如下：
<ul><li>**false**：（默认）不需要审批，直接签署。</li>
<li>**true**：需要走审批流程。当到对应参与人签署时，会阻塞其签署操作，等待企业内部审批完成。</li></ul>
企业可以通过CreateFlowSignReview审批接口通知腾讯电子签平台企业内部审批结果
<ul><li>如果企业通知腾讯电子签平台审核通过，签署方可继续签署动作。</li>
<li>如果企业通知腾讯电子签平台审核未通过，平台将继续阻塞签署方的签署动作，直到企业通知平台审核通过。</li></ul>

注：`此功能可用于与企业内部的审批流程进行关联，支持手动、静默签署合同`
        :type ApproverNeedSignReview: bool
        :param _AddSignComponentsLimits: [用PDF文件创建签署流程](https://qian.tencent.com/developers/companyApis/startFlows/CreateFlowByFiles)时,如果设置了外层参数SignBeanTag=1(允许签署过程中添加签署控件),则可通过此参数明确规定合同所使用的签署控件类型（骑缝章、普通章法人章等）和具体的印章（印章ID）或签名方式。

注：`限制印章控件或骑缝章控件情况下,仅本企业签署方可以指定具体印章（通过传递ComponentValue,支持多个），他方企业或个人只支持限制控件类型。`
        :type AddSignComponentsLimits: list of ComponentLimit
        """
        self._ApproverType = None
        self._ApproverName = None
        self._ApproverMobile = None
        self._OrganizationName = None
        self._SignComponents = None
        self._ApproverIdCardType = None
        self._ApproverIdCardNumber = None
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
        self._AddSignComponentsLimits = None

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

    @property
    def AddSignComponentsLimits(self):
        return self._AddSignComponentsLimits

    @AddSignComponentsLimits.setter
    def AddSignComponentsLimits(self, AddSignComponentsLimits):
        self._AddSignComponentsLimits = AddSignComponentsLimits


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
        self._ApproverIdCardType = params.get("ApproverIdCardType")
        self._ApproverIdCardNumber = params.get("ApproverIdCardNumber")
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
        if params.get("AddSignComponentsLimits") is not None:
            self._AddSignComponentsLimits = []
            for item in params.get("AddSignComponentsLimits"):
                obj = ComponentLimit()
                obj._deserialize(item)
                self._AddSignComponentsLimits.append(obj)
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
        :param _NoRefuse: 签署方是否可以拒签

<ul><li> **false** : ( 默认)可以拒签</li>
<li> **true** :不可以拒签</li></ul>
        :type NoRefuse: bool
        :param _NoTransfer: 签署方是否可以转他人处理

<ul><li> **false** : ( 默认)可以转他人处理</li>
<li> **true** :不可以转他人处理</li></ul>
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
        :param _UserInfo: 自动签开通个人用户信息, 包括名字,身份证等
        :type UserInfo: :class:`tencentcloud.ess.v20201111.models.UserThreeFactor`
        :param _CertInfoCallback: 是否回调证书信息:
<ul><li>**false**: 不需要(默认)</li>
<li>**true**:需要</li></ul>
        :type CertInfoCallback: bool
        :param _UserDefineSeal: 是否支持用户自定义签名印章:
<ul><li>**false**: 不能自己定义(默认)</li>
<li>**true**: 可以自己定义</li></ul>
        :type UserDefineSeal: bool
        :param _SealImgCallback: 回调中是否需要自动签将要使用的印章(签名) 图片的 base64:
<ul><li>**false**: 不需要(默认)</li>
<li>**true**: 需要</li></ul>
        :type SealImgCallback: bool
        :param _CallbackUrl: 执行结果的回调URL，该URL仅支持HTTP或HTTPS协议，建议采用HTTPS协议以保证数据传输的安全性。
腾讯电子签服务器将通过POST方式，application/json格式通知执行结果，请确保外网可以正常访问该URL。
回调的相关说明可参考开发者中心的<a href="https://qian.tencent.com/developers/company/callback_types_v2" target="_blank">回调通知</a>模块。
        :type CallbackUrl: str
        :param _VerifyChannels: 开通时候的身份验证方式, 取值为：
<ul><li>**WEIXINAPP** : 微信人脸识别</li>
<li>**INSIGHT** : 慧眼人脸认别</li>
<li>**TELECOM** : 运营商三要素验证</li></ul>
注：
<ul><li>如果是小程序开通链接，支持传 WEIXINAPP / TELECOM。为空默认 WEIXINAPP</li>
<li>如果是 H5 开通链接，支持传 INSIGHT / TELECOM。为空默认 INSIGHT </li></ul>
        :type VerifyChannels: list of str
        :param _LicenseType: 设置用户开通自动签时是否绑定个人自动签账号许可。

<ul><li>**0**: (默认) 使用个人自动签账号许可进行开通，个人自动签账号许可有效期1年，注: `不可解绑释放更换他人`</li>
</ul>
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
        warnings.warn("parameter `CallbackUrl` is deprecated", DeprecationWarning) 

        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        warnings.warn("parameter `CallbackUrl` is deprecated", DeprecationWarning) 

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
    """企业应用回调信息

    """

    def __init__(self):
        r"""
        :param _CallbackUrl: 回调url,。请确保回调地址能够接收并处理 HTTP POST 请求，并返回状态码 200 以表示处理正常。
        :type CallbackUrl: str
        :param _Token: 回调加密key，已废弃
        :type Token: str
        :param _CallbackKey: 回调加密key，用于回调消息加解密。
        :type CallbackKey: str
        :param _CallbackToken: 回调验签token，用于回调通知校验。
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowId: 合同流程ID, 为32位字符串。
建议开发者保存此流程ID方便后续其他操作。
        :type FlowId: str
        :param _CancelMessage: 撤销此合同(流程)的原因，最长200个字。
        :type CancelMessage: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _QrCodeId: 二维码ID，为32位字符串。
        :type QrCodeId: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _SceneKey: 自动签使用的场景值, 可以选择的场景值如下:
<ul><li> **E_PRESCRIPTION_AUTO_SIGN** :  电子处方场景</li></ul>

注: `现在仅支持电子处方场景`
        :type SceneKey: str
        :param _UserInfo: 预撤销链接的用户信息，包含姓名、证件类型、证件号码等信息。

        :type UserInfo: :class:`tencentcloud.ess.v20201111.models.UserThreeFactor`
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _Mobile: 被抄送方手机号码， 支持国内手机号11位数字(无需加+86前缀或其他字符)。
请确认手机号所有方为此业务通知方。
        :type Mobile: str
        :param _Name: 被抄送方姓名。
抄送方的姓名将用于身份认证，请确保填写的姓名为抄送方的真实姓名，而非昵称等代名。
        :type Name: str
        :param _CcType: 被抄送方类型, 可设置以下类型:
<ul><li> **0** :个人抄送方</li>
<li> **1** :企业员工抄送方</li></ul>
        :type CcType: int
        :param _CcPermission: 被抄送方权限, 可设置如下权限:
<ul><li> **0** :可查看合同内容</li>
<li> **1** :可查看合同内容也可下载原文</li></ul>
        :type CcPermission: int
        :param _NotifyType: 通知签署方经办人的方式,  有以下途径:
<ul><li> **sms** :  (默认)短信</li>
<li> **none** : 不通知</li></ul>
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
    """模板/流程中控件信息，可以是填充控件或签署控件

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
        :param _FileIndex: 控件所属文件的序号（取值为：0-N）。
目前单文件的情况下，值是0
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
        :param _ComponentId: 控件唯一ID。
或使用文件发起合同时用于GenerateMode==KEYWORD 指定关键字
        :type ComponentId: str
        :param _ComponentName: 控件名。
或使用文件发起合同时用于GenerateMode==FIELD 指定表单域名称
        :type ComponentName: str
        :param _ComponentRequired: 是否必选，默认为false-非必选
        :type ComponentRequired: bool
        :param _ComponentRecipientId: 控件关联的参与方ID，对应Recipient结构体中的RecipientId
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
        :param _IsFormType: 是否是表单域类型，默认false-不是
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
        :param _ChannelComponentId: 第三方应用集成平台模板控件 ID 标识
        :type ChannelComponentId: str
        :param _OffsetX: 指定关键字时横坐标偏移量，单位pt
注意：此字段可能返回 null，表示取不到有效值。
        :type OffsetX: float
        :param _OffsetY: 指定关键字时纵坐标偏移量，单位pt
注意：此字段可能返回 null，表示取不到有效值。
        :type OffsetY: float
        :param _ChannelComponentSource: 第三方应用集成中子客企业控件来源。
0-平台指定；
1-用户自定义
        :type ChannelComponentSource: int
        :param _KeywordOrder: 指定关键字排序规则，Positive-正序，Reverse-倒序。
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
        :param _KeywordIndexes: 关键字索引。
如果一个关键字在PDF文件中存在多个，可以通过关键字索引指定使用第几个关键字作为最后的结果，可指定多个索引。
示例：[0,2]，说明使用PDF文件内第1个和第3个关键字位置。
        :type KeywordIndexes: list of int
        :param _LockComponentValue: 是否锁定控件值不允许编辑（嵌入式发起使用）
<br/>默认false：不锁定控件值，允许在页面编辑控件值
注意：此字段可能返回 null，表示取不到有效值。
        :type LockComponentValue: bool
        :param _ForbidMoveAndDelete: 是否禁止移动和删除控件
<br/>默认false，不禁止移动和删除控件
注意：此字段可能返回 null，表示取不到有效值。
        :type ForbidMoveAndDelete: bool
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
        self._LockComponentValue = None
        self._ForbidMoveAndDelete = None

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
        


class CreateBatchCancelFlowUrlRequest(AbstractModel):
    """CreateBatchCancelFlowUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
<br/>注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowIds: 需要执行撤回的流程(合同)的编号列表，最多100个.
<br>列表中的流程(合同)编号不要重复.
        :type FlowIds: list of str
        :param _Agent: 代理企业和员工的信息。
<br/>在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
数组里边的错误原因与传进来的FlowIds一一对应,如果是空字符串则标识没有出错
        :type FailMessages: list of str
        :param _UrlExpireOn: 签署连接过期时间字符串：年月日-时分秒

例如:2023-07-28 17:25:59
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


class CreateConvertTaskApiRequest(AbstractModel):
    """CreateConvertTaskApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceType: 需要进行转换的资源文件类型
支持的文件类型如下：
<ul><li>doc</li>
<li>docx</li>
<li>xls</li>
<li>xlsx</li>
<li>jpg</li>
<li>jpeg</li>
<li>png</li>
<li>bmp</li>
<li>txt</li></ul>
        :type ResourceType: str
        :param _ResourceName: 需要进行转换操作的文件资源名称，带资源后缀名。

注:  `资源名称长度限制为256个字符`
        :type ResourceName: str
        :param _ResourceId: 需要进行转换操作的文件资源Id，通过<a href="https://qian.tencent.com/developers/companyApis/templatesAndFiles/UploadFiles" target="_blank">UploadFiles</a>接口获取文件资源Id。

注:  `目前，此接口仅支持单个文件进行转换。`
        :type ResourceId: str
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _TaskId: 接口返回的文件转换任务Id，可以调用接口<a href="https://qian.tencent.com/developers/companyApis/templatesAndFiles/GetTaskResultApi" target="_blank">查询转换任务状态</a>获取转换任务的状态和转换后的文件资源Id。
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
        :param _FlowId: 合同流程ID，为32位字符串。
此接口的合同流程ID需要由<a href="https://qian.tencent.com/developers/companyApis/startFlows/CreateFlow" target="_blank">创建签署流程</a>接口创建得到。
        :type FlowId: str
        :param _TemplateId: 用户配置的合同模板ID，会基于此模板创建合同文档，为32位字符串。
可登录腾讯电子签控制台，在 "模板"->"模板中心"->"列表展示设置"选中模板 ID 中查看某个模板的TemplateId(在页面中展示为模板ID)。
        :type TemplateId: str
        :param _FileNames: 文件名列表，单个文件名最大长度200个字符，暂时仅支持单文件发起。设置后流程对应的文件名称当前设置的值。
        :type FileNames: list of str
        :param _FormFields: 电子文档的填写控件的填充内容。具体方式可以参考<a href="https://qian.tencent.com/developers/companyApis/dataTypes/#formfield" target="_blank">FormField</a>结构体的定义。
        :type FormFields: list of FormField
        :param _NeedPreview: 是否为预览模式，取值如下：
<ul><li> **false**：非预览模式（默认），会产生合同流程并返回合同流程编号FlowId。</li>
<li> **true**：预览模式，不产生合同流程，不返回合同流程编号FlowId，而是返回预览链接PreviewUrl，有效期为300秒，用于查看真实发起后合同的样子。</li></ul>
        :type NeedPreview: bool
        :param _PreviewType: 预览模式下产生的预览链接类型 
<ul><li> **0** :(默认) 文件流 ,点开后后下载预览的合同PDF文件 </li>
<li> **1** :H5链接 ,点开后在浏览器中展示合同的样子</li></ul>
注: `此参数在NeedPreview 为true时有效`

        :type PreviewType: int
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _ClientToken: 已废弃字段，客户端Token，保持接口幂等性,最大长度64个字符
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
        :param _DocumentId: 合同流程的底层电子文档ID，为32位字符串。

注:
后续需用同样的FlowId再次调用<a href="https://qian.tencent.com/developers/companyApis/startFlows/StartFlow" target="_blank">发起签署流程</a>，合同才能进入签署环节
        :type DocumentId: str
        :param _PreviewFileUrl: 合同预览链接URL。

注：如果是预览模式(即NeedPreview设置为true)时, 才会有此预览链接URL
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
        :param _Operator: 执行本接口操作的员工信息。
<br/>注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _EmbedType: WEB嵌入资源类型，支持以下类型
<ul><li>CREATE_SEAL: 生成创建印章的嵌入页面</li>
<li>CREATE_TEMPLATE：生成创建模板的嵌入页面</li>
<li>MODIFY_TEMPLATE：生成编辑模板的嵌入页面</li>
<li>PREVIEW_TEMPLATE：生成预览模板的嵌入页面</li>
<li>PREVIEW_SEAL_LIST：生成预览印章列表的嵌入页面</li>
<li>PREVIEW_SEAL_DETAIL：生成预览印章详情的嵌入页面</li>
<li>EXTEND_SERVICE：生成拓展服务的嵌入页面</li>
<li>PREVIEW_FLOW：生成预览合同的嵌入页面</li>
<li>PREVIEW_FLOW_DETAIL：生成查看合同详情的嵌入页面</li></ul>
        :type EmbedType: str
        :param _BusinessId: WEB嵌入的业务资源ID
<ul><li>PREVIEW_SEAL_DETAIL，必填，取值为印章id</li>
<li>MODIFY_TEMPLATE，PREVIEW_TEMPLATE，必填，取值为模板id</li>
<li>PREVIEW_FLOW，PREVIEW_FLOW_DETAIL，必填，取值为合同id</li><ul>
        :type BusinessId: str
        :param _Agent: 代理企业和员工的信息。
<br/>在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Reviewer: 抄送方信息
        :type Reviewer: :class:`tencentcloud.ess.v20201111.models.ReviewerInfo`
        :param _Option: 个性化参数，用于控制页面展示内容
        :type Option: :class:`tencentcloud.ess.v20201111.models.EmbedUrlOption`
        """
        self._Operator = None
        self._EmbedType = None
        self._BusinessId = None
        self._Agent = None
        self._Reviewer = None
        self._Option = None

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

    @property
    def Option(self):
        return self._Option

    @Option.setter
    def Option(self, Option):
        self._Option = Option


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
        if params.get("Option") is not None:
            self._Option = EmbedUrlOption()
            self._Option._deserialize(params.get("Option"))
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
<br/>EmbedType=PREVIEW_CC_FLOW，该url为h5链接
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowId: 合同流程ID，为32位字符串。
建议开发者妥善保存此流程ID，以便于顺利进行后续操作。
可登录腾讯电子签控制台，在 "合同"->"合同中心" 中查看某个合同的FlowId(在页面中展示为合同ID)。
        :type FlowId: str
        :param _Approvers: 补充企业签署人信息。

- 如果发起方指定的补充签署人是企业微信签署人（ApproverSource=WEWORKAPP），则需要提供企业微信UserId进行补充；

- 如果不指定，则使用姓名和手机号进行补充。
        :type Approvers: list of FillApproverInfo
        :param _Initiator: 在可定制的企业微信通知中，发起人可以根据具体需求进行自定义设置。
        :type Initiator: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _Operator: 执行本接口操作的员工信息。使用此接口时，必须填写userId。
支持填入集团子公司经办人 userId 代发合同。

注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowName: 合同流程的名称（可自定义此名称），长度不能超过200，只能由中文、字母、数字和下划线组成。

该名称还将用于合同签署完成后的下载文件名。
        :type FlowName: str
        :param _Approvers: 合同流程的参与方列表，最多可支持50个参与方，可在列表中指定企业B端签署方和个人C端签署方的联系和认证方式等信息，具体定义可以参考开发者中心的ApproverInfo结构体。

如果合同流程是有序签署，Approvers列表中参与人的顺序就是默认的签署顺序，请确保列表中参与人的顺序符合实际签署顺序。
        :type Approvers: list of ApproverInfo
        :param _FileIds: 本合同流程需包含的PDF文件资源编号列表，通过<a href="https://qian.tencent.com/developers/companyApis/templatesAndFiles/UploadFiles" target="_blank">UploadFiles</a>接口获取PDF文件资源编号。

注:  `目前，此接口仅支持单个文件发起。`
        :type FileIds: list of str
        :param _FlowDescription: 合同流程描述信息(可自定义此描述)，最大长度1000个字符。
        :type FlowDescription: str
        :param _FlowType: 合同流程的类别分类（可自定义名称，如销售合同/入职合同等），最大长度为200个字符，仅限中文、字母、数字和下划线组成。
        :type FlowType: str
        :param _Components: 模板或者合同中的填写控件列表，列表中可支持下列多种填写控件，控件的详细定义参考开发者中心的Component结构体
<ul><li> 单行文本控件      </li>
<li> 多行文本控件      </li>
<li> 勾选框控件        </li>
<li> 数字控件          </li>
<li> 图片控件          </li>
<li> 动态表格等填写控件</li></ul>
        :type Components: list of Component
        :param _CcInfos: 合同流程的抄送人列表，最多可支持50个抄送人，抄送人可查看合同内容及签署进度，但无需参与合同签署。

注:`此功能为白名单功能，使用前请联系对接的客户经理沟通。`
        :type CcInfos: list of CcInfo
        :param _CcNotifyType: 可以设置以下时间节点来给抄送人发送短信通知来查看合同内容：
<ul><li> **0**：合同发起时通知（默认值）</li>
<li> **1**：签署完成后通知</li></ul>
        :type CcNotifyType: int
        :param _NeedPreview: 是否为预览模式，取值如下：
<ul><li> **false**：非预览模式（默认），会产生合同流程并返回合同流程编号FlowId。</li>
<li> **true**：预览模式，不产生合同流程，不返回合同流程编号FlowId，而是返回预览链接PreviewUrl，有效期为300秒，用于查看真实发起后合同的样子。</li></ul>
        :type NeedPreview: bool
        :param _PreviewType: 预览模式下产生的预览链接类型 
<ul><li> **0** :(默认) 文件流 ,点开后后下载预览的合同PDF文件 </li>
<li> **1** :H5链接 ,点开后在浏览器中展示合同的样子</li></ul>
注: `此参数在NeedPreview 为true时有效`

        :type PreviewType: int
        :param _Deadline: 合同流程的签署截止时间，格式为Unix标准时间戳（秒），如果未设置签署截止时间，则默认为合同流程创建后的365天时截止。
如果在签署截止时间前未完成签署，则合同状态会变为已过期，导致合同作废。
        :type Deadline: int
        :param _RemindedOn: 合同到期提醒时间，为Unix标准时间戳（秒）格式，支持的范围是从发起时间开始到后10年内。

到达提醒时间后，腾讯电子签会短信通知发起方企业合同提醒，可用于处理合同到期事务，如合同续签等事宜。
        :type RemindedOn: int
        :param _Unordered: 合同流程的签署顺序类型：
<ul><li> **false**：(默认)有序签署, 本合同多个参与人需要依次签署 </li>
<li> **true**：无序签署, 本合同多个参与人没有先后签署限制</li></ul>
        :type Unordered: bool
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
        :param _NeedSignReview: 发起方企业的签署人进行签署操作前，是否需要企业内部走审批流程，取值如下：
<ul><li> **false**：（默认）不需要审批，直接签署。</li>
<li> **true**：需要走审批流程。当到对应参与人签署时，会阻塞其签署操作，等待企业内部审批完成。</li></ul>
企业可以通过CreateFlowSignReview审批接口通知腾讯电子签平台企业内部审批结果
<ul><li> 如果企业通知腾讯电子签平台审核通过，签署方可继续签署动作。</li>
<li> 如果企业通知腾讯电子签平台审核未通过，平台将继续阻塞签署方的签署动作，直到企业通知平台审核通过。</li></ul>
注：`此功能可用于与企业内部的审批流程进行关联，支持手动、静默签署合同`
        :type NeedSignReview: bool
        :param _UserData: 调用方自定义的个性化字段(可自定义此名称)，并以base64方式编码，支持的最大数据大小为 20480长度。

在合同状态变更的回调信息等场景中，该字段的信息将原封不动地透传给贵方。回调的相关说明可参考开发者中心的<a href="https://qian.tencent.com/developers/company/callback_types_v2" target="_blank">回调通知</a>模块。
        :type UserData: str
        :param _ApproverVerifyType: 指定个人签署方查看合同的校验方式
<ul><li>   **VerifyCheck**  :（默认）人脸识别,人脸识别后才能合同内容 </li>
<li>   **MobileCheck**  :  手机号验证, 用户手机号和参与方手机号（ApproverMobile）相同即可查看合同内容（当手写签名方式为OCR_ESIGN时，该校验方式无效，因为这种签名方式依赖实名认证）</li></ul>
        :type ApproverVerifyType: str
        :param _SignBeanTag: 签署方签署控件（印章/签名等）的生成方式：
<ul><li> **0**：在合同流程发起时，由发起人指定签署方的签署控件的位置和数量。</li>
<li> **1**：签署方在签署时自行添加签署控件，可以拖动位置和控制数量。</li></ul>
        :type SignBeanTag: int
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _AutoSignScene: 个人自动签名的使用场景包括以下, 个人自动签署(即ApproverType设置成个人自动签署时)业务此值必传：
<ul><li> **E_PRESCRIPTION_AUTO_SIGN**：处方单（医疗自动签）  </li></ul>
注: `个人自动签名场景是白名单功能，使用前请与对接的客户经理联系沟通。`
        :type AutoSignScene: str
        """
        self._Operator = None
        self._FlowName = None
        self._Approvers = None
        self._FileIds = None
        self._FlowDescription = None
        self._FlowType = None
        self._Components = None
        self._CcInfos = None
        self._CcNotifyType = None
        self._NeedPreview = None
        self._PreviewType = None
        self._Deadline = None
        self._RemindedOn = None
        self._Unordered = None
        self._CustomShowMap = None
        self._NeedSignReview = None
        self._UserData = None
        self._ApproverVerifyType = None
        self._SignBeanTag = None
        self._Agent = None
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
    def CcNotifyType(self):
        return self._CcNotifyType

    @CcNotifyType.setter
    def CcNotifyType(self, CcNotifyType):
        self._CcNotifyType = CcNotifyType

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
        self._FlowDescription = params.get("FlowDescription")
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
        self._CcNotifyType = params.get("CcNotifyType")
        self._NeedPreview = params.get("NeedPreview")
        self._PreviewType = params.get("PreviewType")
        self._Deadline = params.get("Deadline")
        self._RemindedOn = params.get("RemindedOn")
        self._Unordered = params.get("Unordered")
        self._CustomShowMap = params.get("CustomShowMap")
        self._NeedSignReview = params.get("NeedSignReview")
        self._UserData = params.get("UserData")
        self._ApproverVerifyType = params.get("ApproverVerifyType")
        self._SignBeanTag = params.get("SignBeanTag")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
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
        :param _FlowId: 合同流程ID，为32位字符串。
建议开发者妥善保存此流程ID，以便于顺利进行后续操作。
可登录腾讯电子签控制台，在 "合同"->"合同中心" 中查看某个合同的FlowId(在页面中展示为合同ID)。

注: 如果是预览模式(即NeedPreview设置为true)时, 此处不会有值返回。
        :type FlowId: str
        :param _PreviewUrl: 合同预览链接URL。

注：如果是预览模式(即NeedPreview设置为true)时, 才会有此预览链接URL
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowId: 合同流程ID，为32位字符串。
可登录腾讯电子签控制台，在 "合同"->"合同中心" 中查看某个合同的FlowId(在页面中展示为合同ID)。
        :type FlowId: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _ReportId: 出证报告 ID，可用于<a href="https://qian.tencent.com/developers/companyApis/certificate/DescribeFlowEvidenceReport" target="_blank">获取出证报告任务执行结果</a>查询出证任务结果和出证PDF的下载URL
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportId: str
        :param _Status: 出证任务执行的状态, 状态含义如下：

<ul><li>**EvidenceStatusExecuting**：  出证任务在执行中</li>
<li>**EvidenceStatusSuccess**：  出证任务执行成功</li>
<li>**EvidenceStatusFailed** ： 出征任务执行失败</li></ul>
        :type Status: str
        :param _ReportUrl: 此字段已经废除,不再使用.
出证的PDF下载地址请调用DescribeChannelFlowEvidenceReport接口获取
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
        warnings.warn("parameter `ReportUrl` is deprecated", DeprecationWarning) 

        return self._ReportUrl

    @ReportUrl.setter
    def ReportUrl(self, ReportUrl):
        warnings.warn("parameter `ReportUrl` is deprecated", DeprecationWarning) 

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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowGroupName: 合同（流程）组名称（可自定义此名称），长度不能超过200，只能由中文、字母、数字和下划线组成。
        :type FlowGroupName: str
        :param _FlowGroupInfos: 合同（流程）组的子合同信息，支持2-50个子合同
        :type FlowGroupInfos: list of FlowGroupInfo
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _FlowGroupOptions: 合同（流程）组的配置项信息。
其中包括：
<ul>
<li>是否通知本企业签署方</li>
<li>是否通知其他签署方</li>
</ul>
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowGroupName: 合同（流程）组名称（可自定义此名称），长度不能超过200，只能由中文、字母、数字和下划线组成。
        :type FlowGroupName: str
        :param _FlowGroupInfos: 合同（流程）组的子合同信息，支持2-50个子合同
        :type FlowGroupInfos: list of FlowGroupInfo
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _FlowGroupOptions: 合同（流程）组的配置项信息。
其中包括：
<ul>
<li>是否通知本企业签署方</li>
<li>是否通知其他签署方</li>
</ul>
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


class CreateFlowOption(AbstractModel):
    """创建合同个性化参数

    """

    def __init__(self):
        r"""
        :param _CanEditFlow: 是否允许修改发起合同时确认弹窗的合同信息（合同名称、合同类型、签署截止时间），若不允许编辑，则表单字段将被禁止输入。
<br/>true：允许编辑（默认），<br/>false：不允许编辑<br/>默认：false：不允许编辑
        :type CanEditFlow: bool
        :param _CanEditFormField: 是否允许编辑模板控件
<br/>true:允许编辑模板控件信息
<br/>false:不允许编辑模板控件信息
<br/>默认false:不允许编辑模板控件信息
        :type CanEditFormField: bool
        :param _HideShowFlowName: 发起页面隐藏合同名称展示
<br/>true:发起页面隐藏合同名称展示
<br/>false:发起页面不隐藏合同名称展示
<br/>默认false:发起页面不隐藏合同名称展示
        :type HideShowFlowName: bool
        :param _HideShowFlowType: 发起页面隐藏合同类型展示
<br/>true:发起页面隐藏合同类型展示
<br/>false:发起页面不隐藏合同类型展示
<br/>默认false:发起页面不隐藏合同类型展示

        :type HideShowFlowType: bool
        :param _HideShowDeadline: 发起页面隐藏合同截止日期展示
<br/>true:发起页面隐藏合同截止日期展示
<br/>false:发起页面不隐藏合同截止日期展示
<br/>默认false:发起页面不隐藏合同截止日期展示
        :type HideShowDeadline: bool
        :param _CanSkipAddApprover: 发起页面允许跳过添加签署人环节
<br/>true:发起页面允许跳过添加签署人环节
<br/>false:发起页面不允许跳过添加签署人环节
<br/>默认false:发起页面不允许跳过添加签署人环节

        :type CanSkipAddApprover: bool
        :param _SkipUploadFile: 文件发起页面跳过文件上传步骤
<br/>true:文件发起页面跳过文件上传步骤
<br/>false:文件发起页面不跳过文件上传步骤
<br/>默认false:文件发起页面不跳过文件上传步骤
        :type SkipUploadFile: bool
        :param _ForbidEditFillComponent: 禁止编辑填写控件
<br/>true:禁止编辑填写控件
<br/>false:允许编辑填写控件
<br/>默认false:允许编辑填写控件
        :type ForbidEditFillComponent: bool
        :param _CustomCreateFlowDescription: 定制化发起合同弹窗的描述信息，描述信息最长500

        :type CustomCreateFlowDescription: str
        """
        self._CanEditFlow = None
        self._CanEditFormField = None
        self._HideShowFlowName = None
        self._HideShowFlowType = None
        self._HideShowDeadline = None
        self._CanSkipAddApprover = None
        self._SkipUploadFile = None
        self._ForbidEditFillComponent = None
        self._CustomCreateFlowDescription = None

    @property
    def CanEditFlow(self):
        return self._CanEditFlow

    @CanEditFlow.setter
    def CanEditFlow(self, CanEditFlow):
        self._CanEditFlow = CanEditFlow

    @property
    def CanEditFormField(self):
        return self._CanEditFormField

    @CanEditFormField.setter
    def CanEditFormField(self, CanEditFormField):
        self._CanEditFormField = CanEditFormField

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
    def SkipUploadFile(self):
        return self._SkipUploadFile

    @SkipUploadFile.setter
    def SkipUploadFile(self, SkipUploadFile):
        self._SkipUploadFile = SkipUploadFile

    @property
    def ForbidEditFillComponent(self):
        return self._ForbidEditFillComponent

    @ForbidEditFillComponent.setter
    def ForbidEditFillComponent(self, ForbidEditFillComponent):
        self._ForbidEditFillComponent = ForbidEditFillComponent

    @property
    def CustomCreateFlowDescription(self):
        return self._CustomCreateFlowDescription

    @CustomCreateFlowDescription.setter
    def CustomCreateFlowDescription(self, CustomCreateFlowDescription):
        self._CustomCreateFlowDescription = CustomCreateFlowDescription


    def _deserialize(self, params):
        self._CanEditFlow = params.get("CanEditFlow")
        self._CanEditFormField = params.get("CanEditFormField")
        self._HideShowFlowName = params.get("HideShowFlowName")
        self._HideShowFlowType = params.get("HideShowFlowType")
        self._HideShowDeadline = params.get("HideShowDeadline")
        self._CanSkipAddApprover = params.get("CanSkipAddApprover")
        self._SkipUploadFile = params.get("SkipUploadFile")
        self._ForbidEditFillComponent = params.get("ForbidEditFillComponent")
        self._CustomCreateFlowDescription = params.get("CustomCreateFlowDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowRemindsRequest(AbstractModel):
    """CreateFlowReminds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowIds: 需执行催办的签署流程ID数组，最多包含100个。
        :type FlowIds: list of str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _RemindFlowRecords: 合同催办结果的详细信息列表。
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
        :param _Operator: 执行本接口操作的员工信息。使用此接口时，必须填写userId。
支持填入集团子公司经办人 userId 代发合同。

注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowName: 合同流程的名称（可自定义此名称），长度不能超过200，只能由中文、字母、数字和下划线组成。

该名称还将用于合同签署完成后的下载文件名。
        :type FlowName: str
        :param _Approvers: 合同流程的参与方列表，最多可支持50个参与方，可在列表中指定企业B端签署方和个人C端签署方的联系和认证方式等信息，具体定义可以参考开发者中心的ApproverInfo结构体。

注:  `approver中的顺序需要和模板中的顺序保持一致， 否则会导致模板中配置的信息无效`
        :type Approvers: list of FlowCreateApprover
        :param _FlowDescription: 合同流程描述信息(可自定义此描述)，最大长度1000个字符。
        :type FlowDescription: str
        :param _FlowType: 合同流程的类别分类（可自定义名称，如销售合同/入职合同等），最大长度为200个字符，仅限中文、字母、数字和下划线组成。
        :type FlowType: str
        :param _ClientToken: 已经废弃字段，客户端Token，保持接口幂等性,最大长度64个字符
        :type ClientToken: str
        :param _DeadLine: 合同流程的签署截止时间，格式为Unix标准时间戳（秒），如果未设置签署截止时间，则默认为合同流程创建后的365天时截止。
如果在签署截止时间前未完成签署，则合同状态会变为已过期，导致合同作废。
        :type DeadLine: int
        :param _RemindedOn: 合同到期提醒时间，为Unix标准时间戳（秒）格式，支持的范围是从发起时间开始到后10年内。

到达提醒时间后，腾讯电子签会短信通知发起方企业合同提醒，可用于处理合同到期事务，如合同续签等事宜。
        :type RemindedOn: int
        :param _UserData: 调用方自定义的个性化字段(可自定义此名称)，并以base64方式编码，支持的最大数据大小为 20480长度。

在合同状态变更的回调信息等场景中，该字段的信息将原封不动地透传给贵方。回调的相关说明可参考开发者中心的<a href="https://qian.tencent.com/developers/company/callback_types_v2" target="_blank">回调通知</a>模块。
        :type UserData: str
        :param _Unordered: 合同流程的签署顺序类型：
<ul><li> **false**：(默认)有序签署, 本合同多个参与人需要依次签署 </li>
<li> **true**：无序签署, 本合同多个参与人没有先后签署限制</li></ul>
注：`请和模板中的配置保持一致`
        :type Unordered: bool
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
        :param _NeedSignReview: 发起方企业的签署人进行签署操作前，是否需要企业内部走审批流程，取值如下：
<ul><li> **false**：（默认）不需要审批，直接签署。</li>
<li> **true**：需要走审批流程。当到对应参与人签署时，会阻塞其签署操作，等待企业内部审批完成。</li></ul>
企业可以通过CreateFlowSignReview审批接口通知腾讯电子签平台企业内部审批结果
<ul><li> 如果企业通知腾讯电子签平台审核通过，签署方可继续签署动作。</li>
<li> 如果企业通知腾讯电子签平台审核未通过，平台将继续阻塞签署方的签署动作，直到企业通知平台审核通过。</li></ul>
注：`此功能可用于与企业内部的审批流程进行关联，支持手动、静默签署合同`
        :type NeedSignReview: bool
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _CcInfos: 合同流程的抄送人列表，最多可支持50个抄送人，抄送人可查看合同内容及签署进度，但无需参与合同签署。

注:`此功能为白名单功能，使用前请联系对接的客户经理沟通。`
        :type CcInfos: list of CcInfo
        :param _AutoSignScene: 个人自动签名的使用场景包括以下, 个人自动签署(即ApproverType设置成个人自动签署时)业务此值必传：
<ul><li> **E_PRESCRIPTION_AUTO_SIGN**：处方单（医疗自动签）  </li></ul>
注: `个人自动签名场景是白名单功能，使用前请与对接的客户经理联系沟通。`
        :type AutoSignScene: str
        :param _RelatedFlowId: 暂未开放
        :type RelatedFlowId: str
        :param _CallbackUrl: 暂未开放
        :type CallbackUrl: str
        """
        self._Operator = None
        self._FlowName = None
        self._Approvers = None
        self._FlowDescription = None
        self._FlowType = None
        self._ClientToken = None
        self._DeadLine = None
        self._RemindedOn = None
        self._UserData = None
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
        self._FlowDescription = params.get("FlowDescription")
        self._FlowType = params.get("FlowType")
        self._ClientToken = params.get("ClientToken")
        self._DeadLine = params.get("DeadLine")
        self._RemindedOn = params.get("RemindedOn")
        self._UserData = params.get("UserData")
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
        :param _FlowId: 合同流程ID，为32位字符串。
建议开发者妥善保存此流程ID，以便于顺利进行后续操作。

注:
此返回的合同流程ID，需再次调用<a href="https://qian.tencent.com/developers/companyApis/startFlows/CreateDocument" target="_blank">创建电子文档</a>和<a href="https://qian.tencent.com/developers/companyApis/startFlows/StartFlow" target="_blank">发起签署流程</a>接口将合同开始后，合同才能进入签署环节


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
若发起个人审核，则指定该字段为：SignReview
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
        :param _FlowId: 合同流程ID，为32位字符串。
建议开发者妥善保存此流程ID，以便于顺利进行后续操作。
可登录腾讯电子签控制台，在 "合同"->"合同中心" 中查看某个合同的FlowId(在页面中展示为合同ID)。
        :type FlowId: str
        :param _FlowApproverInfos: 流程签署人列表，其中结构体的ApproverName，ApproverMobile和ApproverType必传，其他可不传，

注:
`1. ApproverType目前只支持个人类型的签署人。`
`2. 签署人只能有手写签名和时间类型的签署控件，其他类型的填写控件和签署控件暂时都未支持。`
        :type FlowApproverInfos: list of FlowCreateApprover
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Organization: 机构信息，暂未开放
        :type Organization: :class:`tencentcloud.ess.v20201111.models.OrganizationInfo`
        :param _JumpUrl: 签署完之后的H5页面的跳转链接，此链接及支持http://和https://，最大长度1000个字符。(建议https协议)
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得组织架构管理权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _DeptName: 部门名称，不超过50个字符
        :type DeptName: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
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
        self._Agent = None
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
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

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
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
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


class CreateIntegrationRoleRequest(AbstractModel):
    """CreateIntegrationRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 角色名称，最大长度为20个字符，仅限中文、字母、数字和下划线组成。
        :type Name: str
        :param _Operator: 执行本接口操作的员工信息。使用此接口时，必须填写userId。
支持填入集团子公司经办人 userId 代发合同。

注: 在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Description: 角色描述，最大长度为50个字符
        :type Description: str
        :param _IsGroupRole: 角色类型，0:saas角色，1:集团角色
默认0，saas角色
        :type IsGroupRole: int
        :param _PermissionGroups: 权限树
        :type PermissionGroups: list of PermissionGroup
        :param _SubOrganizationIds: 集团角色的话，需要传递集团子企业列表，如果是全选，则传1
        :type SubOrganizationIds: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Name = None
        self._Operator = None
        self._Description = None
        self._IsGroupRole = None
        self._PermissionGroups = None
        self._SubOrganizationIds = None
        self._Agent = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IsGroupRole(self):
        return self._IsGroupRole

    @IsGroupRole.setter
    def IsGroupRole(self, IsGroupRole):
        self._IsGroupRole = IsGroupRole

    @property
    def PermissionGroups(self):
        return self._PermissionGroups

    @PermissionGroups.setter
    def PermissionGroups(self, PermissionGroups):
        self._PermissionGroups = PermissionGroups

    @property
    def SubOrganizationIds(self):
        return self._SubOrganizationIds

    @SubOrganizationIds.setter
    def SubOrganizationIds(self, SubOrganizationIds):
        self._SubOrganizationIds = SubOrganizationIds

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._Description = params.get("Description")
        self._IsGroupRole = params.get("IsGroupRole")
        if params.get("PermissionGroups") is not None:
            self._PermissionGroups = []
            for item in params.get("PermissionGroups"):
                obj = PermissionGroup()
                obj._deserialize(item)
                self._PermissionGroups.append(obj)
        self._SubOrganizationIds = params.get("SubOrganizationIds")
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
        


class CreateIntegrationRoleResponse(AbstractModel):
    """CreateIntegrationRole返回参数结构体

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


class CreateIntegrationUserRolesRequest(AbstractModel):
    """CreateIntegrationUserRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。 注: 在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _UserIds: 绑定角色的用户id列表，不能重复，不能大于 100 个
        :type UserIds: list of str
        :param _RoleIds: 绑定角色的角色id列表，不能重复，不能大于 100，可以通过DescribeIntegrationRoles接口获取角色信息
        :type RoleIds: list of str
        :param _Agent: 代理企业和员工的信息。 在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _TemplateId: 合同模板ID，为32位字符串。
可登录腾讯电子签控制台，在 "模板"->"模板中心"->"列表展示设置"选中模板 ID 中查看某个模板的TemplateId(在页面中展示为模板ID)。
        :type TemplateId: str
        :param _FlowName: 合同流程的名称（可自定义此名称），长度不能超过200，只能由中文、字母、数字和下划线组成。
该名称还将用于合同签署完成后的下载文件名。
        :type FlowName: str
        :param _MaxFlowNum: 通过此二维码可发起的流程最大限额，如未明确指定，默认为5份。
一旦发起流程数超越该限制，该二维码将自动失效。
        :type MaxFlowNum: int
        :param _QrEffectiveDay: 二维码的有效期限，默认为7天，最高设定不得超过90天。
一旦超过二维码的有效期限，该二维码将自动失效。
        :type QrEffectiveDay: int
        :param _FlowEffectiveDay: 合同流程的签署有效期限，若未设定签署截止日期，则默认为自合同流程创建起的7天内截止。
若在签署截止日期前未完成签署，合同状态将变更为已过期，从而导致合同无效。
最长设定期限不得超过30天。
        :type FlowEffectiveDay: int
        :param _Restrictions: 指定签署人信息。
在指定签署人后，仅允许特定签署人通过扫描二维码进行签署。
        :type Restrictions: list of ApproverRestriction
        :param _UserData: 调用方自定义的个性化字段(可自定义此字段的值)，并以base64方式编码，支持的最大数据大小为 20480长度。
在合同状态变更的回调信息等场景中，该字段的信息将原封不动地透传给贵方。
回调的相关说明可参考开发者中心的<a href="https://qian.tencent.com/developers/company/callback_types_v2" target="_blank">回调通知</a>模块。
        :type UserData: str
        :param _CallbackUrl: 已废弃，回调配置统一使用企业应用管理-应用集成-企业版应用中的配置 
<br/> 通过一码多扫二维码发起的合同，回调消息可参考文档 https://qian.tencent.com/developers/company/callback_types_contracts_sign
<br/> 用户通过签署二维码发起合同时，因企业额度不足导致失败 会触发签署二维码相关回调,具体参考文档 https://qian.tencent.com/developers/company/callback_types_commons#%E7%AD%BE%E7%BD%B2%E4%BA%8C%E7%BB%B4%E7%A0%81%E7%9B%B8%E5%85%B3%E5%9B%9E%E8%B0%83

        :type CallbackUrl: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _ApproverRestrictions: 限制二维码用户条件（已弃用）
        :type ApproverRestrictions: :class:`tencentcloud.ess.v20201111.models.ApproverRestriction`
        """
        self._Operator = None
        self._TemplateId = None
        self._FlowName = None
        self._MaxFlowNum = None
        self._QrEffectiveDay = None
        self._FlowEffectiveDay = None
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
    def QrEffectiveDay(self):
        return self._QrEffectiveDay

    @QrEffectiveDay.setter
    def QrEffectiveDay(self, QrEffectiveDay):
        self._QrEffectiveDay = QrEffectiveDay

    @property
    def FlowEffectiveDay(self):
        return self._FlowEffectiveDay

    @FlowEffectiveDay.setter
    def FlowEffectiveDay(self, FlowEffectiveDay):
        self._FlowEffectiveDay = FlowEffectiveDay

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
        warnings.warn("parameter `CallbackUrl` is deprecated", DeprecationWarning) 

        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        warnings.warn("parameter `CallbackUrl` is deprecated", DeprecationWarning) 

        self._CallbackUrl = CallbackUrl

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
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
        self._QrEffectiveDay = params.get("QrEffectiveDay")
        self._FlowEffectiveDay = params.get("FlowEffectiveDay")
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
        :param _QrCode: 签署二维码的基本信息，用于创建二维码，用户可扫描该二维码进行签署操作。
        :type QrCode: :class:`tencentcloud.ess.v20201111.models.SignQrCode`
        :param _SignUrls: 流程签署二维码的签署信息，适用于客户系统整合二维码功能。通过链接，用户可直接访问电子签名小程序并签署合同。
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
        :param _Operator: 执行本接口操作的员工信息。使用此接口时，必须填写userId。
支持填入集团子公司经办人 userId 代发合同。

注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowIds: 请指定需执行批量签署的流程ID，数量范围为1-100。
您可登录腾讯电子签控制台，浏览 "合同"->"合同中心" 以查阅某一合同的FlowId（在页面中显示为合同ID）。
用户将利用链接对这些合同实施批量操作。
        :type FlowIds: list of str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _UserId: 员工在腾讯电子签平台的独特身份标识，为32位字符串。
您可登录腾讯电子签控制台，在 "更多能力"->"组织管理" 中查阅某位员工的UserId（在页面中显示为用户ID）。
UserId必须是传入合同（FlowId）中的签署人。
- 1. 若UserId为空，Name和Mobile 必须提供。
- 2. 若UserId 与 Name，Mobile均存在，将优先采用UserId对应的员工。
        :type UserId: str
        :param _Name: 员工姓名，必须与手机号码一起使用。
如果UserId为空，则此字段不能为空。同时，姓名和手机号码必须与传入合同（FlowId）中的签署人信息一致。
        :type Name: str
        :param _Mobile: 员工手机号，必须与姓名一起使用。
 如果UserId为空，则此字段不能为空。同时，姓名和手机号码必须与传入合同（FlowId）中的签署人信息一致。
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
        :param _SignUrl: 批量签署入口链接，用户可使用这个链接跳转到控制台页面对合同进行签署操作。
        :type SignUrl: str
        :param _ExpiredTime: 链接过期截止时间，格式为Unix标准时间戳（秒），默认为7天后截止。
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


class CreatePersonAuthCertificateImageRequest(AbstractModel):
    """CreatePersonAuthCertificateImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _UserName: 个人用户名称
        :type UserName: str
        :param _IdCardType: 证件类型，支持以下类型
<ul><li> ID_CARD  : 居民身份证 (默认值)</li>
<li> PASSPORT  : 护照</li>
<li> FOREIGN_ID_CARD  : 外国人永久居留身份证</li>
<li> HONGKONG_AND_MACAO  : 港澳居民来往内地通行证</li>
<li> HONGKONG_MACAO_AND_TAIWAN  : 港澳台居民居住证(格式同居民身份证)</li></ul>
        :type IdCardType: str
        :param _IdCardNumber: 证件号码，应符合以下规则
<ul><li>居民身份证号码应为18位字符串，由数字和大写字母X组成（如存在X，请大写）。</li>
<li>港澳居民来往内地通行证号码应为9位字符串，第1位为“C”，第2位为英文字母（但“I”、“O”除外），后7位为阿拉伯数字。</li>
<li>港澳台居民居住证号码编码规则与中国大陆身份证相同，应为18位字符串。</li></ul>
        :type IdCardNumber: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._UserName = None
        self._IdCardType = None
        self._IdCardNumber = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

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
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._UserName = params.get("UserName")
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
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
        


class CreatePersonAuthCertificateImageResponse(AbstractModel):
    """CreatePersonAuthCertificateImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AuthCertUrl: 个人用户认证证书图片下载URL，`有效期为5分钟`，超过有效期后将无法再下载。
        :type AuthCertUrl: str
        :param _ImageCertId: 个人用户认证证书的编号, 为20位数字组成的字符串,  由腾讯电子签下发此编号 。
该编号会合成到个人用户证书证明图片。

注: `个人用户认证证书的编号和证明图片绑定, 获取新的证明图片编号会变动`
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageCertId: str
        :param _SerialNumber: CA供应商下发给用户的证书编号，在证书到期后自动续期后此证书编号会发生变动，且不会合成到个人用户证书证明图片中。

注意：`腾讯电子签接入多家CA供应商以提供容灾能力，不同CA下发的证书编号区别较大，但基本都是由数字和字母组成，长度在200以下。`
注意：此字段可能返回 null，表示取不到有效值。
        :type SerialNumber: str
        :param _ValidFrom: CA证书颁发时间，格式为Unix标准时间戳（秒）   
该时间格式化后会合成到个人用户证书证明图片
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidFrom: int
        :param _ValidTo: CA证书有效截止时间，格式为Unix标准时间戳（秒）
该时间格式化后会合成到个人用户证书证明图片
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidTo: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AuthCertUrl = None
        self._ImageCertId = None
        self._SerialNumber = None
        self._ValidFrom = None
        self._ValidTo = None
        self._RequestId = None

    @property
    def AuthCertUrl(self):
        return self._AuthCertUrl

    @AuthCertUrl.setter
    def AuthCertUrl(self, AuthCertUrl):
        self._AuthCertUrl = AuthCertUrl

    @property
    def ImageCertId(self):
        return self._ImageCertId

    @ImageCertId.setter
    def ImageCertId(self, ImageCertId):
        self._ImageCertId = ImageCertId

    @property
    def SerialNumber(self):
        return self._SerialNumber

    @SerialNumber.setter
    def SerialNumber(self, SerialNumber):
        self._SerialNumber = SerialNumber

    @property
    def ValidFrom(self):
        return self._ValidFrom

    @ValidFrom.setter
    def ValidFrom(self, ValidFrom):
        self._ValidFrom = ValidFrom

    @property
    def ValidTo(self):
        return self._ValidTo

    @ValidTo.setter
    def ValidTo(self, ValidTo):
        self._ValidTo = ValidTo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AuthCertUrl = params.get("AuthCertUrl")
        self._ImageCertId = params.get("ImageCertId")
        self._SerialNumber = params.get("SerialNumber")
        self._ValidFrom = params.get("ValidFrom")
        self._ValidTo = params.get("ValidTo")
        self._RequestId = params.get("RequestId")


class CreatePrepareFlowRequest(AbstractModel):
    """CreatePrepareFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _ResourceId: 资源id，与ResourceType对应
        :type ResourceId: str
        :param _FlowName: 合同名称
        :type FlowName: str
        :param _Unordered: 是否顺序签署
true:无序签
false:顺序签
        :type Unordered: bool
        :param _Deadline: 签署流程的签署截止时间。
值为unix时间戳,精确到秒
不传默认为当前时间一年后
        :type Deadline: int
        :param _UserFlowTypeId: 用户自定义合同类型Id

该id为电子签企业内的合同类型id， 可以在自定义合同类型处获取
        :type UserFlowTypeId: str
        :param _FlowType: 合同类型名称
该字段用于客户自定义合同类型
建议使用时指定合同类型，便于之后合同分类以及查看
如果合同类型与自定义的合同类型描述一致，会自动归类到自定义的合同类型处，如果不一致，则会创建一个新的自定义合同类型
        :type FlowType: str
        :param _Approvers: 签署流程参与者信息，最大限制50方
        :type Approvers: list of FlowCreateApprover
        :param _IntelligentStatus: 打开智能添加填写区
默认开启，打开:"OPEN"
 关闭："CLOSE"
        :type IntelligentStatus: str
        :param _ResourceType: 资源类型，
1：模板
2：文件，
不传默认为2：文件
        :type ResourceType: int
        :param _Components: 发起方填写控件
该类型控件由发起方完成填写
        :type Components: :class:`tencentcloud.ess.v20201111.models.Component`
        :param _FlowOption: 发起合同个性化参数
用于满足创建及页面操作过程中的个性化要求
具体定制化内容详见数据接口说明
        :type FlowOption: :class:`tencentcloud.ess.v20201111.models.CreateFlowOption`
        :param _NeedSignReview: 是否开启发起方签署审核
true:开启发起方签署审核
false:不开启发起方签署审核
默认false:不开启发起方签署审核
        :type NeedSignReview: bool
        :param _NeedCreateReview: 开启发起方发起合同审核
true:开启发起方发起合同审核
false:不开启发起方发起合同审核
默认false:不开启发起方发起合同审核
        :type NeedCreateReview: bool
        :param _UserData: 用户自定义参数
        :type UserData: str
        :param _FlowId: 合同id,用于通过已web页面发起的合同id快速生成一个web发起合同链接
        :type FlowId: str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填	
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._ResourceId = None
        self._FlowName = None
        self._Unordered = None
        self._Deadline = None
        self._UserFlowTypeId = None
        self._FlowType = None
        self._Approvers = None
        self._IntelligentStatus = None
        self._ResourceType = None
        self._Components = None
        self._FlowOption = None
        self._NeedSignReview = None
        self._NeedCreateReview = None
        self._UserData = None
        self._FlowId = None
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
    def FlowType(self):
        return self._FlowType

    @FlowType.setter
    def FlowType(self, FlowType):
        self._FlowType = FlowType

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
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Components(self):
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def FlowOption(self):
        return self._FlowOption

    @FlowOption.setter
    def FlowOption(self, FlowOption):
        self._FlowOption = FlowOption

    @property
    def NeedSignReview(self):
        return self._NeedSignReview

    @NeedSignReview.setter
    def NeedSignReview(self, NeedSignReview):
        self._NeedSignReview = NeedSignReview

    @property
    def NeedCreateReview(self):
        return self._NeedCreateReview

    @NeedCreateReview.setter
    def NeedCreateReview(self, NeedCreateReview):
        self._NeedCreateReview = NeedCreateReview

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

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
        self._ResourceId = params.get("ResourceId")
        self._FlowName = params.get("FlowName")
        self._Unordered = params.get("Unordered")
        self._Deadline = params.get("Deadline")
        self._UserFlowTypeId = params.get("UserFlowTypeId")
        self._FlowType = params.get("FlowType")
        if params.get("Approvers") is not None:
            self._Approvers = []
            for item in params.get("Approvers"):
                obj = FlowCreateApprover()
                obj._deserialize(item)
                self._Approvers.append(obj)
        self._IntelligentStatus = params.get("IntelligentStatus")
        self._ResourceType = params.get("ResourceType")
        if params.get("Components") is not None:
            self._Components = Component()
            self._Components._deserialize(params.get("Components"))
        if params.get("FlowOption") is not None:
            self._FlowOption = CreateFlowOption()
            self._FlowOption._deserialize(params.get("FlowOption"))
        self._NeedSignReview = params.get("NeedSignReview")
        self._NeedCreateReview = params.get("NeedCreateReview")
        self._UserData = params.get("UserData")
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
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _LicenseType: 设置用户开通自动签时是否绑定个人自动签账号许可。一旦绑定后，将扣减购买的个人自动签账号许可一次（1年有效期），不可解绑释放。不传默认为绑定自动签账号许可。 0-绑定个人自动签账号许可，开通后将扣减购买的个人自动签账号许可一次 1-不绑定，发起合同时将按标准合同套餐进行扣减	
        :type LicenseType: int
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
        self._Agent = None
        self._LicenseType = None

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

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def LicenseType(self):
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType


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
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._LicenseType = params.get("LicenseType")
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _NeedRelievedFlowId: 待解除的签署流程编号（即原签署流程的编号）。
        :type NeedRelievedFlowId: str
        :param _ReliveInfo: 解除协议内容, 包括解除理由等信息。
        :type ReliveInfo: :class:`tencentcloud.ess.v20201111.models.RelieveInfo`
        :param _Agent: 关于渠道应用的相关信息，包括子客企业及应用编、号等详细内容，您可以参阅开发者中心所提供的 Agent 结构体以获取详细定义。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _ReleasedApprovers: 替换解除协议的签署人， 如不指定替换签署人,  则使用原流程的签署人。 <br/>
如需更换原合同中的企业端签署人，可通过指定该签署人的RecipientId编号更换此企业端签署人。(可通过接口<a href="https://qian.tencent.com/developers/companyApis/queryFlows/DescribeFlowInfo/">DescribeFlowInfo</a>查询签署人的RecipientId编号)<br/>

注意：
`只能更换自己企业的签署人,  不支持更换个人类型或者其他企业的签署人。`
`可以不指定替换签署人, 使用原流程的签署人 `
        :type ReleasedApprovers: list of ReleasedApprover
        :param _Deadline: 合同流程的签署截止时间，格式为Unix标准时间戳（秒），如果未设置签署截止时间，则默认为合同流程创建后的7天时截止。
如果在签署截止时间前未完成签署，则合同状态会变为已过期，导致合同作废。
        :type Deadline: int
        :param _UserData: 调用方自定义的个性化字段，该字段的值可以是字符串JSON或其他字符串形式，客户可以根据自身需求自定义数据格式并在需要时进行解析。该字段的信息将以Base64编码的形式传输，支持的最大数据大小为20480长度。

在合同状态变更的回调信息等场景中，该字段的信息将原封不动地透传给贵方。

回调的相关说明可参考开发者中心的<a href="https://qian.tencent.com/developers/company/callback_types_v2" target="_blank">回调通知</a>模块。
        :type UserData: str
        """
        self._Operator = None
        self._NeedRelievedFlowId = None
        self._ReliveInfo = None
        self._Agent = None
        self._ReleasedApprovers = None
        self._Deadline = None
        self._UserData = None

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
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

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
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._NeedRelievedFlowId = params.get("NeedRelievedFlowId")
        if params.get("ReliveInfo") is not None:
            self._ReliveInfo = RelieveInfo()
            self._ReliveInfo._deserialize(params.get("ReliveInfo"))
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("ReleasedApprovers") is not None:
            self._ReleasedApprovers = []
            for item in params.get("ReleasedApprovers"):
                obj = ReleasedApprover()
                obj._deserialize(item)
                self._ReleasedApprovers.append(obj)
        self._Deadline = params.get("Deadline")
        self._UserData = params.get("UserData")
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
`注意：这里的流程编号对应的合同是本次发起的解除协议。`

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
        :param _Operator: 执行本接口操作的员工信息, userId 必填。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _OrganizationName: 合同流程签署方的组织机构名称。
如果名称中包含英文括号()，请使用中文括号（）代替。
        :type OrganizationName: str
        :param _Name: 合同流程里边签署方经办人的姓名。

        :type Name: str
        :param _Mobile: 合同流程里边签署方经办人手机号码， 支持国内手机号11位数字(无需加+86前缀或其他字符)。
        :type Mobile: str
        :param _EndPoint: 要跳转的链接类型

<ul><li> **HTTP**：跳转电子签小程序的http_url, 短信通知或者H5跳转适合此类型  ，此时返回长链 (默认类型)</li>
<li>**HTTP_SHORT_URL**：跳转电子签小程序的http_url, 短信通知或者H5跳转适合此类型，此时返回短链</li>
<li>**APP**： 第三方APP或小程序跳转电子签小程序的path,  APP或者小程序跳转适合此类型</li></ul>
        :type EndPoint: str
        :param _FlowId: 合同流程ID 
注: `如果准备跳转到合同流程签署的详情页面(即PathType=1时)必传,   跳转其他页面可不传`
        :type FlowId: str
        :param _FlowGroupId: 合同流程组的组ID, 在合同流程组场景下，生成合同流程组的签署链接时需要赋值
        :type FlowGroupId: str
        :param _PathType: 要跳转到的页面类型 

<ul><li> **0** : 腾讯电子签小程序个人首页 (默认)</li>
<li> **1** : 腾讯电子签小程序流程合同的详情页 (即合同签署页面)</li>
<li> **2** : 腾讯电子签小程序合同列表页</li></ul>
        :type PathType: int
        :param _AutoJumpBack: 签署完成后是否自动回跳
<ul><li>**false**：否, 签署完成不会自动跳转回来(默认)</li><li>**true**：是, 签署完成会自动跳转回来</li></ul>
注:  ` 该参数只针对"APP" 类型的签署链接有效`
        :type AutoJumpBack: bool
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Hides: 生成的签署链接在签署页面隐藏的按钮列表，可设置如下：

<ul><li> **0** :合同签署页面更多操作按钮</li>
<li> **1** :合同签署页面更多操作的拒绝签署按钮</li>
<li> **2** :合同签署页面更多操作的转他人处理按钮</li>
<li> **3** :签署成功页的查看详情按钮</li></ul>

注:  `字段为数组, 可以传值隐藏多个按钮`
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
        :param _SchemeUrl: 腾讯电子签小程序的签署链接。

<ul><li>如果EndPoint是**APP**，得到的链接类似于`pages/guide?from=default&where=mini&id=yDwJSUUirqauh***7jNSxwdirTSGuH&to=CONTRACT_DETAIL&name=&phone=&shortKey=yDw***k1xFc5`, 用法可以参加接口描述中的"跳转到小程序的实现"</li>
<li>如果EndPoint是**HTTP**，得到的链接类似于 `https://res.ess.tencent.cn/cdn/h5-activity/jump-mp.html?where=mini&from=SFY&id=yDwfEUUw**4rV6Avz&to=MVP_CONTRACT_COVER&name=%E9%83%**5%86%9B`，点击后会跳转到腾讯电子签小程序进行签署</li>
<li>如果EndPoint是**HTTP_SHORT_URL**，得到的链接类似于 `https://essurl.cn/2n**42Nd`，点击后会跳转到腾讯电子签小程序进行签署</li></ul>
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _SealName: 电子印章名字，1-50个中文字符。
        :type SealName: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _GenerateSource: 本接口支持上传图片印章及系统直接生成印章；
如果要使用系统生成印章，此值传：SealGenerateSourceSystem；
如果要使用图片上传请传字段 Image
        :type GenerateSource: str
        :param _SealType: 电子印章类型：
OFFICIAL-公章；
CONTRACT-合同专用章;
FINANCE-合财务专用章;
PERSONNEL-人事专用章.
        :type SealType: str
        :param _FileName: 电子印章图片文件名称，1-50个中文字符。
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
        :param _SealHorizontalText: 企业印章横向文字，最多可填15个汉字（若超过印章最大宽度，优先压缩字间距，其次缩小字号）
        :type SealHorizontalText: str
        :param _SealChordText: 暂时不支持下弦文字设置
        :type SealChordText: str
        :param _SealCentralType: 系统生成的印章只支持STAR
        :type SealCentralType: str
        :param _FileToken: 通过文件上传时，服务端生成的电子印章上传图片的token

        :type FileToken: str
        :param _SealStyle: 印章样式:

cycle:圆形印章;
ellipse:椭圆印章;
注：默认圆形印章
        :type SealStyle: str
        :param _SealSize: 印章尺寸取值描述：
42_42 圆形企业公章直径42mm；
40_40 圆形企业印章直径40mm；
45_30 椭圆形印章45mm x 30mm;
        :type SealSize: str
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
        self._SealStyle = None
        self._SealSize = None

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
        self._SealStyle = params.get("SealStyle")
        self._SealSize = params.get("SealSize")
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _SceneKey: 自动签使用的场景值, 可以选择的场景值如下:
<ul><li> **E_PRESCRIPTION_AUTO_SIGN** :  电子处方场景</li></ul>

注: `现在仅支持电子处方场景`
        :type SceneKey: str
        :param _AutoSignConfig: 自动签开通配置信息, 包括开通的人员的信息等
        :type AutoSignConfig: :class:`tencentcloud.ess.v20201111.models.AutoSignConfig`
        :param _UrlType: 生成的链接类型：
<ul><li> 不传(即为空值) 则会生成小程序端开通链接(默认)</li>
<li> **H5SIGN** : 生成H5端开通链接</li></ul>
        :type UrlType: str
        :param _NotifyType: 是否通知开通方，通知类型:
<ul><li>默认不设置为不通知开通方</li>
<li>**SMS** :  短信通知 ,如果需要短信通知则NotifyAddress填写对方的手机号</li><ul>
        :type NotifyType: str
        :param _NotifyAddress: 如果通知类型NotifyType选择为SMS，则此处为手机号, 其他通知类型不需要设置此项
        :type NotifyAddress: str
        :param _ExpiredTime: 链接的过期时间，格式为Unix时间戳，不能早于当前时间，且最大为当前时间往后30天。`如果不传，默认过期时间为当前时间往后7天。`
        :type ExpiredTime: int
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _Url: 个人用户自动签的开通链接, 短链形式。过期时间受 `ExpiredTime` 参数控制。
        :type Url: str
        :param _AppId: 腾讯电子签小程序的 AppID，用于其他小程序/APP等应用跳转至腾讯电子签小程序使用

注: `如果获取的是H5链接, 则不会返回此值`
        :type AppId: str
        :param _AppOriginalId: 腾讯电子签小程序的原始 Id,  ，用于其他小程序/APP等应用跳转至腾讯电子签小程序使用

注: `如果获取的是H5链接, 则不会返回此值`
        :type AppOriginalId: str
        :param _Path: 腾讯电子签小程序的跳转路径，用于其他小程序/APP等应用跳转至腾讯电子签小程序使用

注: `如果获取的是H5链接, 则不会返回此值`
        :type Path: str
        :param _QrCode: base64 格式的跳转二维码图片，可通过微信扫描后跳转到腾讯电子签小程序的开通界面。

注: `如果获取的是H5链接, 则不会返回此二维码图片`
        :type QrCode: str
        :param _UrlType: 返回的链接类型
<ul><li> 空: 默认小程序端链接</li>
<li> **H5SIGN** : h5端链接</li></ul>
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
        :param _Operator: 注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _ThemeType: 主题类型，取值如下：
<ul><li> **EMBED_WEB_THEME**：嵌入式主题（默认），web页面嵌入的主题风格配置</li>
</ul>
        :type ThemeType: str
        :param _WebThemeConfig: 主题配置
        :type WebThemeConfig: :class:`tencentcloud.ess.v20201111.models.WebThemeConfig`
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._ThemeType = None
        self._WebThemeConfig = None
        self._Agent = None

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
        self._ThemeType = params.get("ThemeType")
        if params.get("WebThemeConfig") is not None:
            self._WebThemeConfig = WebThemeConfig()
            self._WebThemeConfig._deserialize(params.get("WebThemeConfig"))
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得组织架构管理权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _DeptId: 电子签中的部门id,通过DescribeIntegrationDepartments接口可获得
        :type DeptId: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _ReceiveDeptId: 交接部门ID。待删除部门中的合同、印章和模板数据，交接至该部门ID下，未填写交接至公司根部门。
        :type ReceiveDeptId: str
        """
        self._Operator = None
        self._DeptId = None
        self._Agent = None
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
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

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
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
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
        :param _Employees: 待移除员工的信息，userId和openId二选一，必填一个，如果需要指定交接人的话，ReceiveUserId或者ReceiveOpenId字段二选一
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
        :param _Operator: 执行本接口操作的员工信息。 注: 在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _RoleId: 角色id，可以通过DescribeIntegrationRoles接口获取角色信息
        :type RoleId: str
        :param _Users: 用户信息,最多 200 个用户，并且 UserId 和 OpenId 二选一，其他字段不需要传
        :type Users: list of UserInfo
        :param _Agent: 代理企业和员工的信息。 在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _ExtendServiceType: 要查询的扩展服务类型。
默认为空，即查询当前支持的所有扩展服务信息。
若需查询单个扩展服务的开通情况，请传递相应的值，如下所示：
<ul><li>OPEN_SERVER_SIGN：企业静默签署</li>
<li>OVERSEA_SIGN：企业与港澳台居民签署合同</li>
<li>MOBILE_CHECK_APPROVER：使用手机号验证签署方身份</li>
<li>PAGING_SEAL：骑缝章</li>
<li>BATCH_SIGN：批量签署</li></ul>
        :type ExtendServiceType: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._ExtendServiceType = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def ExtendServiceType(self):
        return self._ExtendServiceType

    @ExtendServiceType.setter
    def ExtendServiceType(self, ExtendServiceType):
        self._ExtendServiceType = ExtendServiceType

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
        self._ExtendServiceType = params.get("ExtendServiceType")
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
        


class DescribeExtendedServiceAuthInfosResponse(AbstractModel):
    """DescribeExtendedServiceAuthInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AuthInfoList: 服务开通和授权的信息列表，根据查询类型返回所有支持的扩展服务开通和授权状况，或者返回特定扩展服务的开通和授权状况。
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
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowIds: 查询的合同流程ID列表最多支持100个流程ID。 
如果某个合同流程ID不存在，系统会跳过此ID的查询，继续查询剩余存在的合同流程。

可登录腾讯电子签控制台，在 "合同"->"合同中心" 中查看某个合同的FlowId(在页面中展示为合同ID)。
        :type FlowIds: list of str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _FlowBriefs: 合同流程基础信息列表，包含流程的名称、状态、创建日期等基本信息。 
注：`与入参 FlowIds 的顺序可能存在不一致的情况。`
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
        :param _FlowId: 流程(合同)的编号
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
        


class DescribeFlowComponentsResponse(AbstractModel):
    """DescribeFlowComponents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecipientComponentInfos: 流程关联的填写控件信息，按照参与方进行分类返回。
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _ReportId: 签署报告编号, 由<a href="https://qian.tencent.com/developers/companyApis/certificate/CreateFlowEvidenceReport" target="_blank">提交申请出证报告任务</a>产生
        :type ReportId: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _ReportUrl: 出证报告PDF的下载 URL，`有效期为5分钟`，超过有效期后将无法再下载。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportUrl: str
        :param _Status: 出证任务执行的状态, 状态含义如下：

<ul><li>**EvidenceStatusExecuting**：  出证任务在执行中</li>
<li>**EvidenceStatusSuccess**：  出证任务执行成功</li>
<li>**EvidenceStatusFailed** ： 出征任务执行失败</li></ul>
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

如果查询合同组的信息,不要传此参数
        :type FlowIds: list of str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _FlowGroupId: 合同组ID, 如果传此参数会忽略FlowIds入参
 所以如传此参数不要传FlowIds参数

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
注：请保证员工有相关的角色权限
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得组织架构管理权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _QueryType: 查询类型 0-查询单个部门节点 1-单个部门节点及一级子节点部门列表
        :type QueryType: int
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _DeptId: 部门ID,与DeptOpenId二选一,优先DeptId,都为空时获取根节点数据
        :type DeptId: str
        :param _DeptOpenId: 客户系统部门ID,与DeptId二选一,优先DeptId,都为空时获取根节点数据
        :type DeptOpenId: str
        """
        self._Operator = None
        self._QueryType = None
        self._Agent = None
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
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

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
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
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
        :param _Limit: 指定每页多少条数据，单页最大20
        :type Limit: int
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Filters: 查询过滤实名用户，Key为Status，Values为["IsVerified"]，查询过滤未实名用户，Key为Status，Values为["NotVerified"]
查询某个部门的用户，Key为DepartmentId，Values为["DepartmentId"]
根据用户Id查询员工时，Key为UserId，Values为["UserId"]
根据第三方系统openId过滤查询员工时,Key为StaffOpenId,Values为["OpenId","OpenId",...]
        :type Filters: list of Filter
        :param _Offset: 查询结果分页返回，此处指定第几页，如果不传默认从第一页返回。页码从 0 开始，即首页为 0，最大20000
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


class DescribeIntegrationRolesRequest(AbstractModel):
    """DescribeIntegrationRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。使用此接口时，必须填写UserId。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Limit: 指定分页每页返回的数据条数，单页最大支持 200。
        :type Limit: int
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Filters: 查询的关键字段，支持Key-Value单值查询。可选键值对如下：
<ul>
  <li>Key:"RoleType"，查询角色类型，Values可选：
    <ul><li>**"1"**：查询系统角色</li><li>**"2"**：查询自定义角色</li></ul>
  </li><li>Key:"RoleStatus"，查询角色状态，Values可选：
    <ul><li>**"1"**：查询启用角色</li><li>**"2"**：查询禁用角色</li></ul>
  </li><li>Key:"IsGroupRole"，是否查询集团角色，Values可选：
    <ul><li>**"0"**：查询非集团角色</li><li>**"1"**：查询集团角色</li></ul>
  </li><li>Key:"IsReturnPermissionGroup"，是否返回角色对应权限树，Values可选：
    <ul><li>**"0"**：接口不返回角色对应的权限树字段</li><li>**"1"**：接口返回角色对应的权限树字段</li></ul>
  </li>
</ul>
        :type Filters: list of Filter
        :param _Offset: 指定分页返回第几页的数据，如果不传默认返回第一页。页码从 0 开始，即首页为 0，最大2000。
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
        :param _Offset: 指定分页返回的页码。页码从0开始，最大为2000。
        :type Offset: int
        :param _Limit: 指定分页每页返回的数据条数，单页最大支持 200。
        :type Limit: int
        :param _TotalCount: 符合查询条件的总角色数。
        :type TotalCount: int
        :param _IntegrateRoles: 企业角色信息列表。
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
        :param _Limit: 指定每页多少条数据，单页最大1000
        :type Limit: int
        :param _Offset: 查询结果分页返回，此处指定第几页，如果不传默认从第一页返回。页码从 0 开始，即首页为 0
        :type Offset: int
        :param _Name: 查询成员企业的企业名，模糊匹配
        :type Name: str
        :param _Status: 成员企业加入集团的当前状态:1-待授权;2-已授权待激活;3-拒绝授权;4-已解除;5-已加入
        :type Status: int
        :param _Export: 是否导出当前成员企业数据
        :type Export: bool
        :param _Id: 成员企业机构 ID，在PC控制台 集团管理可获取
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
        :param _ActivedTotal: 已加入的企业数量(废弃,请使用ActivatedTotal)
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivedTotal: int
        :param _ExportUrl: 如果入参Export为 true 时使用，表示导出Excel的url
注意：此字段可能返回 null，表示取不到有效值。
        :type ExportUrl: str
        :param _List: 成员企业信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of GroupOrganization
        :param _ActivatedTotal: 已加入的企业数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivatedTotal: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._JoinedTotal = None
        self._ActivedTotal = None
        self._ExportUrl = None
        self._List = None
        self._ActivatedTotal = None
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
        warnings.warn("parameter `ActivedTotal` is deprecated", DeprecationWarning) 

        return self._ActivedTotal

    @ActivedTotal.setter
    def ActivedTotal(self, ActivedTotal):
        warnings.warn("parameter `ActivedTotal` is deprecated", DeprecationWarning) 

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
    def ActivatedTotal(self):
        return self._ActivatedTotal

    @ActivatedTotal.setter
    def ActivatedTotal(self, ActivatedTotal):
        self._ActivatedTotal = ActivatedTotal

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
        self._ActivatedTotal = params.get("ActivatedTotal")
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
        :param _SealStatuses: 查询的印章状态列表。
取值为空，只查询启用状态的印章；
取值ALL，查询所有状态的印章；
取值CHECKING，查询待审核的印章；
取值SUCCESS，查询启用状态的印章；
取值FAIL，查询印章审核拒绝的印章；
取值DISABLE，查询已停用的印章；
取值STOPPED，查询已终止的印章；
取值VOID，查询已作废的印章；
取值INVALID，查询已失效的印章；

        :type SealStatuses: list of str
        """
        self._Operator = None
        self._Limit = None
        self._Offset = None
        self._InfoType = None
        self._SealId = None
        self._SealTypes = None
        self._Agent = None
        self._SealStatuses = None

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

    @property
    def SealStatuses(self):
        return self._SealStatuses

    @SealStatuses.setter
    def SealStatuses(self, SealStatuses):
        self._SealStatuses = SealStatuses


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
        self._SealStatuses = params.get("SealStatuses")
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
        :param _AuthCode: 腾讯电子签小程序跳转客户企业小程序时携带的授权查看码，AuthCode由腾讯电子签小程序生成。
        :type AuthCode: str
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _VerifyStatus: AuthCode 中对应个人用户是否实名
<ul>
<li> **VERIFIED** : 此个人已实名</li>
<li> **UNVERIFIED**: 此个人未实名</li></ul>
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _SceneKey: 自动签使用的场景值, 可以选择的场景值如下:
<ul><li> **E_PRESCRIPTION_AUTO_SIGN** : 电子处方场景</li></ul>

注: `现在仅支持电子处方场景`
        :type SceneKey: str
        :param _UserInfo: 要查询状态的用户信息, 包括名字,身份证等
        :type UserInfo: :class:`tencentcloud.ess.v20201111.models.UserThreeFactor`
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _IsOpen: 查询用户是否已开通自动签
        :type IsOpen: bool
        :param _LicenseFrom: 自动签许可生效时间。当且仅当已通过许可开通自动签时有值。

值为unix时间戳,单位为秒。
        :type LicenseFrom: int
        :param _LicenseTo: 自动签许可到期时间。当且仅当已通过许可开通自动签时有值。

值为unix时间戳,单位为秒。
        :type LicenseTo: int
        :param _LicenseType: 设置用户开通自动签时是否绑定个人自动签账号许可。

<ul><li>**0**: 使用个人自动签账号许可进行开通，个人自动签账号许可有效期1年，注: `不可解绑释放更换他人`</li></ul>
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


class DisableUserAutoSignRequest(AbstractModel):
    """DisableUserAutoSign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _SceneKey: 自动签使用的场景值, 可以选择的场景值如下:
<ul><li> **E_PRESCRIPTION_AUTO_SIGN** 电子处方</li></ul>
        :type SceneKey: str
        :param _UserInfo: 需要关闭自动签的个人的信息，如姓名，证件信息等。
        :type UserInfo: :class:`tencentcloud.ess.v20201111.models.UserThreeFactor`
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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


class EmbedUrlOption(AbstractModel):
    """个性化参数

    """

    def __init__(self):
        r"""
        :param _ShowFlowDetailComponent: 合同详情预览，允许展示控件信息
<br/>true：允许在合同详情页展示控件
<br/>false：不允许在合同详情页展示控件
<br/>默认false，合同详情页不展示控件
        :type ShowFlowDetailComponent: bool
        :param _ShowTemplateComponent: 模板预览，允许展示模板控件信息
<br/>true：允许在模板预览页展示控件
<br/>false：不允许在模板预览页展示控件
<br/>默认false，模板预览页不展示控件
        :type ShowTemplateComponent: bool
        """
        self._ShowFlowDetailComponent = None
        self._ShowTemplateComponent = None

    @property
    def ShowFlowDetailComponent(self):
        return self._ShowFlowDetailComponent

    @ShowFlowDetailComponent.setter
    def ShowFlowDetailComponent(self, ShowFlowDetailComponent):
        self._ShowFlowDetailComponent = ShowFlowDetailComponent

    @property
    def ShowTemplateComponent(self):
        return self._ShowTemplateComponent

    @ShowTemplateComponent.setter
    def ShowTemplateComponent(self, ShowTemplateComponent):
        self._ShowTemplateComponent = ShowTemplateComponent


    def _deserialize(self, params):
        self._ShowFlowDetailComponent = params.get("ShowFlowDetailComponent")
        self._ShowTemplateComponent = params.get("ShowTemplateComponent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtendAuthInfo(AbstractModel):
    """扩展服务开通和授权的详细信息

    """

    def __init__(self):
        r"""
        :param _Type: 扩展服务的类型，可能是以下值：
<ul><li>OPEN_SERVER_SIGN：企业静默签署</li>
<li>OVERSEA_SIGN：企业与港澳台居民签署合同</li>
<li>MOBILE_CHECK_APPROVER：使用手机号验证签署方身份</li>
<li>PAGING_SEAL：骑缝章</li>
<li>BATCH_SIGN：批量签署</li></ul>
        :type Type: str
        :param _Name: 扩展服务的名称
        :type Name: str
        :param _Status: 扩展服务的开通状态：
ENABLE：开通
DISABLE：未开通
        :type Status: str
        :param _OperatorUserId: 操作扩展服务的操作人UserId，员工在腾讯电子签平台的唯一身份标识，为32位字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorUserId: str
        :param _OperateOn: 扩展服务的操作时间，格式为Unix标准时间戳（秒）。
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateOn: int
        :param _HasAuthUserList: 该扩展服务若可以授权，此参数对应授权人员的列表
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
        :param _FileId: 文件ID
        :type FileId: str
        :param _FileName: 文件名
        :type FileName: str
        :param _FileSize: 文件大小，单位为Byte
        :type FileSize: int
        :param _CreatedOn: 文件上传时间，格式为Unix标准时间戳（秒）
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
    -  通过企业微信自定义账号ID补充签署人时，ApproverSource 和 CustomUserId 必填，ApproverSource取值：WEWORKAPP
    - 通过二要素（姓名/手机号）补充签署人时，ApproverName 和 ApproverMobile 必填，ApproverSource设置为空

    """

    def __init__(self):
        r"""
        :param _RecipientId: 签署方经办人在模板中配置的参与方ID，与控件绑定，是控件的归属方，ID为32位字符串。
模板发起合同时，该参数为必填项。
文件发起合同是，该参数无需传值。
如果开发者后序用合同模板发起合同，建议保存此值，在用合同模板发起合同中需此值绑定对应的签署经办人 。
        :type RecipientId: str
        :param _ApproverSource: 签署人来源
WEWORKAPP: 企业微信
<br/>仅【企微或签】时指定WEWORKAPP
        :type ApproverSource: str
        :param _CustomUserId: 企业微信UserId
<br/>当ApproverSource为WEWORKAPP的企微或签场景下，必须指企业自有应用获取企业微信的UserId
        :type CustomUserId: str
        :param _ApproverName: 补充企业签署人员工姓名
        :type ApproverName: str
        :param _ApproverMobile: 补充企业签署人员工手机号
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
        :param _SignId: 签署参与人在本流程中的编号ID（每个流程不同），可用此ID来定位签署参与人在本流程的签署节点，也可用于后续创建签署链接等操作。
注意：此字段可能返回 null，表示取不到有效值。
        :type SignId: str
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
        self._SignId = None

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

    @property
    def SignId(self):
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId


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
        self._SignId = params.get("SignId")
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
        :param _SignUrl: 签署链接(短链形式呈现)。请注意保密，不要将其外泄给无关用户。
注: `注意该链接有效期为30分钟`
注意：此字段可能返回 null，表示取不到有效值。
        :type SignUrl: str
        :param _ApproverType: 签署参与人类型 
<ul><li> **1** :个人参与方</li></ul>

注: `现在仅支持个人参与方`
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproverType: int
        :param _ApproverName: 签署人姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproverName: str
        :param _ApproverMobile: 签署人手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproverMobile: str
        :param _LongUrl: 签署链接(长链形式呈现)。请注意保密，不要将其外泄给无关用户。
注: `注意该链接有效期为30分钟`
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
    """合同流程的基础信息

    """

    def __init__(self):
        r"""
        :param _FlowId: 合同流程ID，为32位字符串。
        :type FlowId: str
        :param _FlowName: 合同流程的名称。
        :type FlowName: str
        :param _FlowDescription: 合同流程描述信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowDescription: str
        :param _FlowType: 合同流程的类别分类（如销售合同/入职合同等）。
        :type FlowType: str
        :param _FlowStatus: 合同流程当前的签署状态, 会存在下列的状态值
<ul><li> **0** : 未开启流程(合同中不存在填写环节)</li>
<li> **1** : 待签署</li>
<li> **2** : 部分签署</li>
<li> **3** : 已拒签</li>
<li> **4** : 已签署</li>
<li> **5** : 已过期</li>
<li> **6** : 已撤销</li>
<li> **7** : 未开启流程(合同中存在填写环节)</li>
<li> **8** : 等待填写</li>
<li> **9** : 部分填写</li>
<li> **10** : 已拒填</li>
<li> **21** : 已解除</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowStatus: int
        :param _CreatedOn: 合同流程创建时间，格式为Unix标准时间戳（秒）。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedOn: int
        :param _FlowMessage: 当合同流程状态为已拒签（即 FlowStatus=3）或已撤销（即 FlowStatus=6）时，此字段 FlowMessage 为拒签或撤销原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowMessage: str
        :param _Creator:  合同流程发起方的员工编号, 即员工在腾讯电子签平台的唯一身份标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        :param _Deadline: 合同流程的签署截止时间，格式为Unix标准时间戳（秒）。
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
        :param _ApproverType: 在指定签署方时，可选择企业B端或个人C端等不同的参与者类型，可选类型如下:
0：企业
1：个人
3：企业静默签署
注：类型为3（企业静默签署）时，此接口会默认完成该签署方的签署。静默签署仅进行盖章操作，不能自动签名。
7: 个人自动签署，适用于个人自动签场景。
注: 个人自动签场景为白名单功能，使用前请联系对接的客户经理沟通。
        :type ApproverType: int
        :param _OrganizationName: 组织机构名称。
请确认该名称与企业营业执照中注册的名称一致。
如果名称中包含英文括号()，请使用中文括号（）代替。

注: `当approverType=0(企业签署方) 或 approverType=3(企业静默签署)时，必须指定`


        :type OrganizationName: str
        :param _ApproverName: 签署方经办人的姓名。
经办人的姓名将用于身份认证和电子签名，请确保填写的姓名为签署方的真实姓名，而非昵称等代名。

在未指定签署人电子签UserId情况下，为必填参数
        :type ApproverName: str
        :param _ApproverMobile: 签署方经办人手机号码， 支持国内手机号11位数字(无需加+86前缀或其他字符)。
请确认手机号所有方为此合同签署方。

在未指定签署人电子签UserId情况下，为必填参数

        :type ApproverMobile: str
        :param _ApproverIdCardType: 证件类型，支持以下类型
<ul><li>ID_CARD : 居民身份证 (默认值)</li>
<li>HONGKONG_AND_MACAO : 港澳居民来往内地通行证</li>
<li>HONGKONG_MACAO_AND_TAIWAN : 港澳台居民居住证(格式同居民身份证)</li></ul>
        :type ApproverIdCardType: str
        :param _ApproverIdCardNumber: 证件号码，应符合以下规则
<ul><li>居民身份证号码应为18位字符串，由数字和大写字母X组成（如存在X，请大写）。</li>
<li>港澳居民来往内地通行证号码应为9位字符串，第1位为“C”，第2位为英文字母（但“I”、“O”除外），后7位为阿拉伯数字。</li>
<li>港澳台居民居住证号码编码规则与中国大陆身份证相同，应为18位字符串。</li></ul>
        :type ApproverIdCardNumber: str
        :param _RecipientId: 签署方经办人在模板中配置的参与方ID，与控件绑定，是控件的归属方，ID为32位字符串。
模板发起合同时，该参数为必填项。
文件发起合同是，该参数无需传值。
如果开发者后续用合同模板发起合同，建议保存此值，在用合同模板发起合同中需此值绑定对应的签署经办人 。
        :type RecipientId: str
        :param _VerifyChannel: 签署意愿确认渠道，默认为WEIXINAPP:人脸识别

注: 将要废弃, 用ApproverSignTypes签署人签署合同时的认证方式代替, 新客户可请用ApproverSignTypes来设置
        :type VerifyChannel: list of str
        :param _NotifyType: 通知签署方经办人的方式,  有以下途径:
<ul><li>  **sms**  :  (默认)短信</li>
<li>   **none**   : 不通知</li></ul>

注: `发起方也是签署方时不给此签署方发送短信`
        :type NotifyType: str
        :param _IsFullText: 合同强制需要阅读全文，无需传此参数
        :type IsFullText: bool
        :param _PreReadTime: 合同的强制预览时间：3~300s，未指定则按合同页数计算
        :type PreReadTime: int
        :param _UserId: 签署人userId，仅支持本企业的员工userid， 可在控制台组织管理处获得

注: `若传此字段 则以userid的信息为主，会覆盖传递过来的签署人基本信息， 包括姓名，手机号，证件类型等信息`
        :type UserId: str
        :param _Required: 字段已经废弃，当前只支持true，默认为true
        :type Required: bool
        :param _ApproverSource: 在企微场景下使用，需设置参数为**WEWORKAPP**，以表明合同来源于企微。
        :type ApproverSource: str
        :param _CustomApproverTag: 在企业微信场景下，表明该合同流程为或签，其最大长度为64位字符串。
所有参与或签的人员均需具备该标识。
注意，在合同中，不同的或签参与人必须保证其CustomApproverTag唯一。
如果或签签署人为本方企业微信参与人，则需要指定ApproverSource参数为WEWORKAPP。
        :type CustomApproverTag: str
        :param _RegisterInfo: 已经废弃, 快速注册相关信息
        :type RegisterInfo: :class:`tencentcloud.ess.v20201111.models.RegisterInfo`
        :param _ApproverOption: 签署人个性化能力值，如是否可以转发他人处理、是否可以拒签等功能开关。
        :type ApproverOption: :class:`tencentcloud.ess.v20201111.models.ApproverOption`
        :param _JumpUrl: 签署完前端跳转的url，暂未使用
        :type JumpUrl: str
        :param _SignId: 签署ID
- 发起流程时系统自动补充
- 创建签署链接时，可以通过查询详情接口获得签署人的SignId，然后可传入此值为该签署人创建签署链接，无需再传姓名、手机号、证件号等其他信息
        :type SignId: str
        :param _ApproverNeedSignReview: 发起方企业的签署人进行签署操作前，是否需要企业内部走审批流程，取值如下：
<ul><li>**false**：（默认）不需要审批，直接签署。</li>
<li>**true**：需要走审批流程。当到对应参与人签署时，会阻塞其签署操作，等待企业内部审批完成。</li></ul>
企业可以通过CreateFlowSignReview审批接口通知腾讯电子签平台企业内部审批结果
<ul><li>如果企业通知腾讯电子签平台审核通过，签署方可继续签署动作。</li>
<li>如果企业通知腾讯电子签平台审核未通过，平台将继续阻塞签署方的签署动作，直到企业通知平台审核通过。</li></ul>

注：`此功能可用于与企业内部的审批流程进行关联，支持手动、静默签署合同`
        :type ApproverNeedSignReview: bool
        :param _SignComponents: 签署人签署控件， 此参数仅针对文件发起（CreateFlowByFiles）生效

合同中的签署控件列表，列表中可支持下列多种签署控件,控件的详细定义参考开发者中心的Component结构体
<ul><li> 个人签名/印章</li>
<li> 企业印章</li>
<li> 骑缝章等签署控件</li></ul>

`此参数仅针对文件发起设置生效,模板发起合同签署流程, 请以模板配置为主`
        :type SignComponents: list of Component
        :param _Components: 签署人填写控件 此参数仅针对文件发起（CreateFlowByFiles）生效

合同中的填写控件列表，列表中可支持下列多种填写控件，控件的详细定义参考开发者中心的Component结构体
<ul><li>单行文本控件</li>
<li>多行文本控件</li>
<li>勾选框控件</li>
<li>数字控件</li>
<li>图片控件</li>
<li>动态表格等填写控件</li></ul>

`此参数仅针对文件发起设置生效,模板发起合同签署流程, 请以模板配置为主`
        :type Components: list of Component
        :param _ComponentLimitType: 签署方控件类型为 SIGN_SIGNATURE时，可以指定签署方签名方式
	HANDWRITE – 手写签名
	OCR_ESIGN -- AI智能识别手写签名
	ESIGN -- 个人印章类型
	SYSTEM_ESIGN -- 系统签名（该类型可以在用户签署时根据用户姓名一键生成一个签名来进行签署）
        :type ComponentLimitType: list of str
        :param _ApproverVerifyTypes: 指定个人签署方查看合同的校验方式,可以传值如下:
<ul><li>  **1**   : （默认）人脸识别,人脸识别后才能合同内容</li>
<li>  **2**  : 手机号验证, 用户手机号和参与方手机号(ApproverMobile)相同即可查看合同内容（当手写签名方式为OCR_ESIGN时，该校验方式无效，因为这种签名方式依赖实名认证）
</li></ul>
注: 
<ul><li>如果合同流程设置ApproverVerifyType查看合同的校验方式,    则忽略此签署人的查看合同的校验方式</li>
<li>此字段不可传多个校验方式</li></ul>

`此参数仅针对文件发起设置生效,模板发起合同签署流程, 请以模板配置为主`

.
        :type ApproverVerifyTypes: list of int
        :param _ApproverSignTypes: 您可以指定签署方签署合同的认证校验方式，可传递以下值：
<ul><li>**1**：人脸认证，需进行人脸识别成功后才能签署合同；</li>
<li>**2**：签署密码，需输入与用户在腾讯电子签设置的密码一致才能校验成功进行合同签署；</li>
<li>**3**：运营商三要素，需到运营商处比对手机号实名信息（名字、手机号、证件号）校验一致才能成功进行合同签署。</li></ul>
注：
<ul><li>默认情况下，认证校验方式为人脸认证和签署密码两种形式；</li>
<li>您可以传递多种值，表示可用多种认证校验方式。</li></ul>

注:
`此参数仅针对文件发起设置生效,模板发起合同签署流程, 请以模板配置为主`
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
        :param _FlowName: 合同流程的名称（可自定义此名称），长度不能超过200，只能由中文、字母、数字和下划线组成。
该名称还将用于合同签署完成后的下载文件名。
        :type FlowName: str
        :param _Approvers: 签署流程参与者信息，最大限制50方
注意 approver中的顺序需要和模板中的顺序保持一致， 否则会导致模板中配置的信息无效。
        :type Approvers: list of ApproverInfo
        :param _FileIds: 文件资源ID，通过多文件上传[UploadFiles](https://qian.tencent.com/developers/companyApis/templatesAndFiles/UploadFiles)接口获得，为32位字符串。
建议开发者保存此资源ID，后续创建合同或创建合同流程需此资源ID。
        :type FileIds: list of str
        :param _TemplateId: 合同模板ID，为32位字符串。
建议开发者保存此模板ID，后续用此模板发起合同流程需要此参数。
可登录腾讯电子签控制台，在 "模板"->"模板中心"->"列表展示设置"选中模板 ID 中查看某个模板的TemplateId(在页面中展示为模板ID)。
        :type TemplateId: str
        :param _FlowType: 签署流程的类型(如销售合同/入职合同等)，最大长度200个字符
示例值：劳务合同
        :type FlowType: str
        :param _FlowDescription: 签署流程描述,最大长度1000个字符
        :type FlowDescription: str
        :param _Deadline: 签署流程的签署截止时间。

值为unix时间戳,精确到秒,不传默认为当前时间一年后
示例值：1604912664
        :type Deadline: int
        :param _CallbackUrl: 合同（流程）的回调地址
        :type CallbackUrl: str
        :param _UserData: 调用方自定义的个性化字段(可自定义此字段的值)，并以base64方式编码，支持的最大数据大小为 20480长度。
在合同状态变更的回调信息等场景中，该字段的信息将原封不动地透传给贵方。
回调的相关说明可参考开发者中心的<a href="https://qian.tencent.com/developers/company/callback_types_v2" target="_blank">回调通知</a>模块。
        :type UserData: str
        :param _Unordered: 发送类型：
true：无序签
false：有序签
注：默认为false（有序签），请和模板中的配置保持一致
示例值：true
        :type Unordered: bool
        :param _Components: 模板或者合同中的填写控件列表，列表中可支持下列多种填写控件，控件的详细定义参考开发者中心的Component结构体
<ul><li>单行文本控件</li>
<li>多行文本控件</li>
<li>勾选框控件</li>
<li>数字控件</li>
<li>图片控件</li>
<li>动态表格等填写控件</li></ul>
        :type Components: list of Component
        :param _NeedSignReview: 发起方企业的签署人进行签署操作是否需要企业内部审批。使用此功能需要发起方企业有参与签署。
若设置为true，审核结果需通过接口 [CreateFlowSignReview](https://qian.tencent.com/developers/companyApis/operateFlows/CreateFlowSignReview) 通知电子签，审核通过后，发起方企业签署人方可进行签署操作，否则会阻塞其签署操作。

注：企业可以通过此功能与企业内部的审批流程进行关联，支持手动、静默签署合同。
示例值：true
        :type NeedSignReview: bool
        :param _AutoSignScene: 个人自动签场景。发起自动签署时，需设置对应自动签署场景，目前仅支持场景：处方单-E_PRESCRIPTION_AUTO_SIGN
示例值：E_PRESCRIPTION_AUTO_SIGN
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
        warnings.warn("parameter `CallbackUrl` is deprecated", DeprecationWarning) 

        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        warnings.warn("parameter `CallbackUrl` is deprecated", DeprecationWarning) 

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
        :param _ApproverVerifyType: 签署人校验方式,支持以下类型
<ul><li>VerifyCheck : 人脸识别 (默认值)</li>
<li>MobileCheck : 手机号验证</li></ul>
参数说明：此参数仅在合同组文件发起有效，可选人脸识别或手机号验证两种方式，若选择后者，未实名个人签署方在签署合同时，无需经过实名认证和意愿确认两次人脸识别，该能力仅适用于个人签署方。
        :type ApproverVerifyType: str
        :param _SelfOrganizationApproverNotifyType: 发起合同（流程）组本方企业经办人通知方式
签署通知类型，支持以下类型
<ul><li>sms : 短信 (默认值)</li><li>none : 不通知</li></ul>
        :type SelfOrganizationApproverNotifyType: str
        :param _OtherApproverNotifyType: 发起合同（流程）组他方经办人通知方式
签署通知类型，支持以下类型
<ul><li>sms : 短信 (默认值)</li><li>none : 不通知</li></ul>
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

    当控件的 ComponentType='TEXT'时，FormField.ComponentValue填入文本内容
    ```
    FormFiled输入示例：
    {
        "ComponentId": "componentId1",
        "ComponentValue": "文本内容"
    }
    ```
    当控件的 ComponentType='MULTI_LINE_TEXT'时，FormField.ComponentValue填入文本内容，支持自动换行。
    ```
    FormFiled输入示例：
    {
        "ComponentId": "componentId1",
        "ComponentValue": "多行文本内容"
    }
    ```
    当控件的 ComponentType='CHECK_BOX'时，FormField.ComponentValue填入true或false文本
    ```
    FormFiled输入示例：
    {
        "ComponentId": "componentId1",
        "ComponentValue": "true"
    }
    ```
    当控件的 ComponentType='FILL_IMAGE'时，FormField.ComponentValue填入图片的资源ID
    ```
    FormFiled输入示例：
    {
        "ComponentId": "componentId1",
        "ComponentValue": "yDwhsxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
    ```
    当控件的 ComponentType='ATTACHMENT'时，FormField.ComponentValue填入附件图片的资源ID列表，以逗号分隔，单个附件控件最多支持6个资源ID；
    ```
    FormFiled输入示例：
    {
        "ComponentId": "componentId1",
        "ComponentValue": "yDwhsxxxxxxxxxxxxxxxxxxxxxxxxxx1,yDwhsxxxxxxxxxxxxxxxxxxxxxxxxxx2,yDwhsxxxxxxxxxxxxxxxxxxxxxxxxxx3"
    }
    ```
    当控件的 ComponentType='SELECTOR'时，FormField.ComponentValue填入选择的选项内容；
    ```
    FormFiled输入示例：
    {
        "ComponentId": "componentId1",
        "ComponentValue": "选择的内容"
    }
    ```
    当控件的 ComponentType='DATE'时，FormField.ComponentValue填入日期内容；
    ```
    FormFiled输入示例：
    {
        "ComponentId": "componentId1",
        "ComponentValue": "2023年01月01日"
    }
    ```
    当控件的 ComponentType='DISTRICT'时，FormField.ComponentValue填入省市区内容；
    ```
    FormFiled输入示例：
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
        :param _TaskId: 任务Id，通过接口CreateConvertTaskApi或CreateMergeFileTask得到的返回任务id
        :type TaskId: str
        :param _Operator: 操作人信息,UserId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Agent: 代理企业和员工的信息。 在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _ResourceId: 资源Id，也是FileId，用于文件发起时使用
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
        :param _FlowEngineEnable: 是否使用自建审批流引擎（即不是企微审批流引擎），true-是，false-否
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
    """被授权的用户信息

    """

    def __init__(self):
        r"""
        :param _UserId: 员工在腾讯电子签平台的唯一身份标识，为32位字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _BelongTo: 当前员工的归属情况，可能值是：
MainOrg：在集团企业的场景下，返回此值代表是归属主企业
CurrentOrg：在普通企业场景下返回此值；或者在集团企业的场景下，返回此值代表归属子企业
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
        :param _PermissionGroups: 权限树
注意：此字段可能返回 null，表示取不到有效值。
        :type PermissionGroups: list of PermissionGroup
        """
        self._RoleId = None
        self._RoleName = None
        self._RoleStatus = None
        self._IsGroupRole = None
        self._SubOrgIdList = None
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
        self._IsGroupRole = params.get("IsGroupRole")
        self._SubOrgIdList = params.get("SubOrgIdList")
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
        


class ModifyApplicationCallbackInfoRequest(AbstractModel):
    """ModifyApplicationCallbackInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _OperateType: 操作类型：
1-新增
2-删除
        :type OperateType: int
        :param _CallbackInfo: 企业应用回调信息
        :type CallbackInfo: :class:`tencentcloud.ess.v20201111.models.CallbackInfo`
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得组织架构管理权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _DeptId: 电子签部门ID,通过DescribeIntegrationDepartments接口可以获取
        :type DeptId: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _ParentDeptId: 电子签父部门ID，通过DescribeIntegrationDepartments接口可以获取
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
        self._Agent = None
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
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

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
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
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


class ModifyIntegrationRoleRequest(AbstractModel):
    """ModifyIntegrationRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色Id，可通过接口 DescribeIntegrationRoles 查询获取
        :type RoleId: str
        :param _Name: 角色名称，最大长度为20个字符，仅限中文、字母、数字和下划线组成。
        :type Name: str
        :param _Operator: 执行本接口操作的员工信息。使用此接口时，必须填写userId。
支持填入集团子公司经办人 userId 代发合同。

注: 在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Description: 角色描述，最大长度为50个字符
        :type Description: str
        :param _PermissionGroups: 权限树
        :type PermissionGroups: list of PermissionGroup
        :param _SubOrganizationIds: 集团角色的话，需要传递集团子企业列表，如果是全选，则传1
        :type SubOrganizationIds: list of str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._RoleId = None
        self._Name = None
        self._Operator = None
        self._Description = None
        self._PermissionGroups = None
        self._SubOrganizationIds = None
        self._Agent = None

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

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

    @property
    def SubOrganizationIds(self):
        return self._SubOrganizationIds

    @SubOrganizationIds.setter
    def SubOrganizationIds(self, SubOrganizationIds):
        self._SubOrganizationIds = SubOrganizationIds

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._Name = params.get("Name")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._Description = params.get("Description")
        if params.get("PermissionGroups") is not None:
            self._PermissionGroups = []
            for item in params.get("PermissionGroups"):
                obj = PermissionGroup()
                obj._deserialize(item)
                self._PermissionGroups.append(obj)
        self._SubOrganizationIds = params.get("SubOrganizationIds")
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
        


class ModifyIntegrationRoleResponse(AbstractModel):
    """ModifyIntegrationRole返回参数结构体

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
        :param _CertNotBefore: 证书起始时间戳，单位毫秒
        :type CertNotBefore: int
        :param _CertNotAfter: 证书过期时间戳，单位毫秒
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
        


class Recipient(AbstractModel):
    """流程中参与方的信息结构

    """

    def __init__(self):
        r"""
        :param _RecipientId: 签署参与者ID，唯一标识
        :type RecipientId: str
        :param _RecipientType: 参与者类型。
默认为空。
ENTERPRISE-企业；
INDIVIDUAL-个人；
PROMOTER-发起方
        :type RecipientType: str
        :param _Description: 描述信息
        :type Description: str
        :param _RoleName: 角色名称
        :type RoleName: str
        :param _RequireValidation: 是否需要验证，
默认为false-不需要验证
        :type RequireValidation: bool
        :param _RequireSign: 是否需要签署，
默认为true-需要签署
        :type RequireSign: bool
        :param _RoutingOrder: 此参与方添加的顺序，从0～N
        :type RoutingOrder: int
        :param _RequireDelivery: 是否需要发送，
默认为true-需要发送
        :type RequireDelivery: bool
        :param _Email: 邮箱地址
        :type Email: str
        :param _Mobile: 电话号码
        :type Mobile: str
        :param _UserId: 关联的用户ID，电子签系统的用户ID
        :type UserId: str
        :param _DeliveryMethod: 发送方式，默认为EMAIL。
EMAIL-邮件；
MOBILE-手机短信；
WECHAT-微信通知
        :type DeliveryMethod: str
        :param _RecipientExtra: 参与方的一些附属信息，json格式
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
0-未填写
1-已填写
注意：此字段可能返回 null，表示取不到有效值。
        :type RecipientFillStatus: str
        :param _IsPromoter: 是否为发起方
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPromoter: bool
        :param _Components: 填写控件列表
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
    """解除协议的签署人，如不指定，默认使用原流程中的签署人。<br/>
    `注意：不支持更换C端（个人身份类型）签署人，如果原流程中含有C端签署人，默认使用原流程中的该C端签署人。`<br/>
    `注意：目前不支持替换C端（个人身份类型）签署人，但是可以指定C端签署人的签署方自定义控件别名，具体见参数ApproverSignRole描述。`<br/>
    `注意：当指定C端签署人的签署方自定义控件别名不空时，除RelievedApproverReceiptId参数外，可以只参数ApproverSignRole。`<br/>

    """

    def __init__(self):
        r"""
        :param _Name: 签署人姓名，最大长度50个字。

        :type Name: str
        :param _Mobile: 签署人手机号。
        :type Mobile: str
        :param _RelievedApproverReceiptId: 要更换的原合同参与人RecipientId编号。(可通过接口<a href="https://qian.tencent.com/developers/companyApis/queryFlows/DescribeFlowInfo/">DescribeFlowInfo</a>查询签署人的RecipientId编号)<br/>
        :type RelievedApproverReceiptId: str
        :param _ApproverType: 指定签署人类型，目前仅支持
<ul><li> **ORGANIZATION**：企业（默认值）</li>
<li> **ENTERPRISESERVER**：企业静默签</li></ul>
        :type ApproverType: str
        :param _ApproverSignComponentType: 签署控件类型，支持自定义企业签署方的签署控件类型
<ul><li> **SIGN_SEAL**：默认为印章控件类型（默认值）</li>
<li> **SIGN_SIGNATURE**：手写签名控件类型</li></ul>
        :type ApproverSignComponentType: str
        :param _ApproverSignRole: 参与方在合同中的角色是按照创建合同的时候来排序的，解除协议默认会将第一个参与人叫`甲方`,第二个叫`乙方`,  第三个叫`丙方`，以此类推。

如果需改动此参与人的角色名字，可用此字段指定，由汉字,英文字符,数字组成，最大20个字。

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
        :param _Reason: 解除理由，长度不能超过200，只能由中文、字母、数字、中文标点和英文标点组成(不支持表情)。
        :type Reason: str
        :param _RemainInForceItem: 解除后仍然有效的条款，保留条款，长度不能超过200，只能由中文、字母、数字、中文标点和英文标点组成(不支持表情)。

        :type RemainInForceItem: str
        :param _OriginalExpenseSettlement: 原合同事项处理-费用结算，长度不能超过200，只能由中文、字母、数字、中文标点和英文标点组成(不支持表情)。
        :type OriginalExpenseSettlement: str
        :param _OriginalOtherSettlement: 原合同事项处理-其他事项，长度不能超过200，只能由中文、字母、数字、中文标点和英文标点组成(不支持表情)。
        :type OriginalOtherSettlement: str
        :param _OtherDeals: 其他约定，长度不能超过200，只能由中文、字母、数字、中文标点和英文标点组成(不支持表情)。
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
    """催办接口返回的详细信息。

    """

    def __init__(self):
        r"""
        :param _CanRemind: 合同流程是否可以催办：
true - 可以，false - 不可以。
若无法催办，将返回RemindMessage以解释原因。
        :type CanRemind: bool
        :param _FlowId: 合同流程ID，为32位字符串。
        :type FlowId: str
        :param _RemindMessage: 在合同流程无法催办的情况下，系统将返回RemindMessage以阐述原因。
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
    """模板中指定的印章信息

    """

    def __init__(self):
        r"""
        :param _SealId: 印章ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SealId: str
        :param _SealType: 印章类型。LEGAL_PERSON_SEAL: 法定代表人章；
ORGANIZATIONSEAL：企业印章；
OFFICIAL：企业公章；
CONTRACT：合同专用章
注意：此字段可能返回 null，表示取不到有效值。
        :type SealType: str
        :param _SealName: 印章名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SealName: str
        """
        self._SealId = None
        self._SealType = None
        self._SealName = None

    @property
    def SealId(self):
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def SealType(self):
        return self._SealType

    @SealType.setter
    def SealType(self, SealType):
        self._SealType = SealType

    @property
    def SealName(self):
        return self._SealName

    @SealName.setter
    def SealName(self, SealName):
        self._SealName = SealName


    def _deserialize(self, params):
        self._SealId = params.get("SealId")
        self._SealType = params.get("SealType")
        self._SealName = params.get("SealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignQrCode(AbstractModel):
    """签署二维码的基本信息，用于创建二维码，用户可扫描该二维码进行签署操作。

    """

    def __init__(self):
        r"""
        :param _QrCodeId: 二维码ID，为32位字符串。
        :type QrCodeId: str
        :param _QrCodeUrl: 二维码URL，可通过转换二维码的工具或代码组件将此URL转化为二维码，以便用户扫描进行流程签署。
        :type QrCodeUrl: str
        :param _ExpiredTime: 二维码的有截止时间，格式为Unix标准时间戳（秒）。
一旦超过二维码的有效期限，该二维码将自动失效。
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
    """流程签署二维码的签署信息，适用于客户系统整合二维码功能。
    通过链接，用户可直接访问电子签名小程序并签署合同。

    """

    def __init__(self):
        r"""
        :param _AppSignUrl: 跳转至电子签名小程序签署的链接地址。
适用于客户端APP及小程序直接唤起电子签名小程序。
        :type AppSignUrl: str
        :param _EffectiveTime: 签署链接有效时间，格式类似"2022-08-05 15:55:01"
        :type EffectiveTime: str
        :param _HttpSignUrl: 跳转至电子签名小程序签署的链接地址，格式类似于https://essurl.cn/xxx。
打开此链接将会展示H5中间页面，随后唤起电子签名小程序以进行合同签署。
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowId: 合同流程ID，为32位字符串。
此处需要传入[创建签署流程接口](https://qian.tencent.com/developers/companyApis/startFlows/CreateFlow)得到的FlowId。
        :type FlowId: str
        :param _ClientToken: 客户端Token，保持接口幂等性,最大长度64个字符
        :type ClientToken: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _CcNotifyType: 若在创建签署流程时指定了关注人CcInfos，此参数可设定向关注人发送短信通知的类型：
<ul><li> **0** :合同发起时通知通知对方来查看合同（默认）</li>
<li> **1** : 签署完成后通知对方来查看合同</li></ul>
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
        warnings.warn("parameter `ClientToken` is deprecated", DeprecationWarning) 

        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        warnings.warn("parameter `ClientToken` is deprecated", DeprecationWarning) 

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
        :param _Status: 发起成功后返回的状态，根据合同流程的不同，返回不同状态：
<ul><li> **START** : 发起成功, 合同进入签署环节</li>
<li> **REVIEW** : 提交审核成功, 合同需要发起审核, 发起方企业通过接口审核通过后合同才进入签署环境  `白名单功能，使用前请联系对接的客户经理沟通。`</li>
<li> **EXECUTING** : 已提交发起任务且PDF合同正在合成中, 等PDF合同合成成功后进入签署环节</li></ul>
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
    """此结构体 (TemplateInfo) 用于描述模板的信息。

    > **模板组成**
    >
    >  一个模板通常会包含以下结构信息
    >- 模板基本信息
    >- 发起方参与信息Promoter、签署参与方 Recipients，后者会在模板发起合同时用于指定参与方
    >- 填写控件 Components
    >- 签署控件 SignComponents
    >- 生成模板的文件基础信息 FileInfos

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID，模板的唯一标识
        :type TemplateId: str
        :param _TemplateName: 模板名
        :type TemplateName: str
        :param _Description: 模板描述信息
        :type Description: str
        :param _DocumentResourceIds: 模板关联的资源ID列表
        :type DocumentResourceIds: list of str
        :param _FileInfos: 生成模板的文件基础信息
        :type FileInfos: list of FileInfo
        :param _AttachmentResourceIds: 附件关联的资源ID
        :type AttachmentResourceIds: list of str
        :param _SignOrder: 签署顺序
无序 -1
有序为序列数字 0,1,2
        :type SignOrder: list of int
        :param _Recipients: 模板中的签署参与方列表
        :type Recipients: list of Recipient
        :param _Components: 模板的填充控件列表
        :type Components: list of Component
        :param _SignComponents: 模板中的签署控件列表
        :type SignComponents: list of Component
        :param _Status: 模板状态
-1:不可用
0:草稿态
1:正式态，可以正常使用
        :type Status: int
        :param _Creator: 模板的创建者信息，电子签系统用户ID
        :type Creator: str
        :param _CreatedOn: 模板创建的时间戳，格式为Unix标准时间戳（秒）
        :type CreatedOn: int
        :param _Promoter: 发起方参与信息Promoter
        :type Promoter: :class:`tencentcloud.ess.v20201111.models.Recipient`
        :param _TemplateType: 模板类型：
1  静默签,
3  普通模板
        :type TemplateType: int
        :param _Available: 模板可用状态：
1 启用（默认）
2 停用
        :type Available: int
        :param _OrganizationId: 创建模板的企业ID，电子签的机构ID
        :type OrganizationId: str
        :param _PreviewUrl: 模板预览链接，有效时间5分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewUrl: str
        :param _TemplateVersion: 模板版本。默认为空时，全数字字符，初始版本为yyyyMMdd001。
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateVersion: str
        :param _Published: 模板是否已发布：
true-已发布
false-未发布
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
        :param _Operator: 当前用户信息，UserId必填
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
        :param _Name: 签署方经办人的姓名。
经办人的姓名将用于身份认证和电子签名，请确保填写的姓名为签署方的真实姓名，而非昵称等代名。
        :type Name: str
        :param _IdCardType: 证件类型，支持以下类型
<ul><li>ID_CARD : 居民身份证 (默认值)</li>
<li>HONGKONG_AND_MACAO : 港澳居民来往内地通行证</li>
<li>HONGKONG_MACAO_AND_TAIWAN : 港澳台居民居住证(格式同居民身份证)</li></ul>
        :type IdCardType: str
        :param _IdCardNumber: 证件号码，应符合以下规则
<ul><li>居民身份证号码应为18位字符串，由数字和大写字母X组成（如存在X，请大写）。</li>
<li>港澳居民来往内地通行证号码应为9位字符串，第1位为“C”，第2位为英文字母（但“I”、“O”除外），后7位为阿拉伯数字。</li>
<li>港澳台居民居住证号码编码规则与中国大陆身份证相同，应为18位字符串。</li></ul>
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
        :param _PdfVerifyResults: 验签结果详情，每个签名域对应的验签结果。状态值：1-验签成功，在电子签签署；2-验签成功，在其他平台签署；3-验签失败；4-pdf文件没有签名域；5-文件签名格式错误
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
        