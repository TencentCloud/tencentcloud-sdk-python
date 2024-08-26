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
        :param _Mobile: 超管手机号，打码显示
示例值：138****1569

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
        


class ApproverComponentLimitType(AbstractModel):
    """签署方在使用个人印章签署控件（SIGN_SIGNATURE） 时可使用的签署方式

    """

    def __init__(self):
        r"""
        :param _RecipientId: 签署方经办人在模板中配置的参与方ID，与控件绑定，是控件的归属方，ID为32位字符串。
        :type RecipientId: str
        :param _Values: 签署方经办人控件类型是个人印章签署控件（SIGN_SIGNATURE） 时，可选的签名方式，可多选

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
        


class ApproverInfo(AbstractModel):
    """合同参与者信息。

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
<ul><li>ID_CARD 中国大陆居民身份证  (默认值)</li>
<li>HONGKONG_AND_MACAO 港澳居民来往内地通行证</li>
<li>HONGKONG_MACAO_AND_TAIWAN 港澳台居民居住证(格式同居民身份证)</li>
<li>OTHER_CARD_TYPE 其他证件</li></ul>

注: `其他证件类型为白名单功能，使用前请联系对接的客户经理沟通。`
        :type ApproverIdCardType: str
        :param _ApproverIdCardNumber: 签署方经办人的证件号码，应符合以下规则
<ul><li>居民身份证号码应为18位字符串，由数字和大写字母X组成（如存在X，请大写）。</li>
<li>港澳居民来往内地通行证号码共11位。第1位为字母，“H”字头签发给香港居民，“M”字头签发给澳门居民；第2位至第11位为数字。</li>
<li>港澳台居民居住证号码编码规则与中国大陆身份证相同，应为18位字符串。</li></ul>
        :type ApproverIdCardNumber: str
        :param _NotifyType: 通知签署方经办人的方式,  有以下途径:
<ul><li>  **sms**  :  (默认)短信</li>
<li>   **none**   : 不通知</li></ul>

注意：
`如果使用的是通过文件发起合同（CreateFlowByFiles），NotifyType必须 是 sms 才会发送短信`
        :type NotifyType: str
        :param _ApproverRole: 收据场景设置签署人角色类型, 可以设置如下****类型****:
<ul><li> **1**  :收款人</li>
<li>   **2**   :开具人</li>
<li>   **3** :见证人</li></ul>
注: `收据场景为白名单功能，使用前请联系对接的客户经理沟通。`
        :type ApproverRole: int
        :param _ApproverRoleName: 可以自定义签署人角色名：收款人、开具人、见证人等，长度不能超过20，只能由中文、字母、数字和下划线组成。

注: `如果是用模板发起, 优先使用此处上传的, 如果不传则用模板的配置的`
        :type ApproverRoleName: str
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

注： 
如果传进来的<font color="red">UserId已经实名， 则忽略ApproverName，ApproverIdCardType，ApproverIdCardNumber，ApproverMobile这四个入参</font>（会用此UserId实名的身份证和登录的手机号覆盖）
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
<li>此字段可传多个校验方式</li></ul>
        :type ApproverVerifyTypes: list of int
        :param _ApproverSignTypes: 您可以指定签署方签署合同的认证校验方式，可传递以下值：
<ul><li>**1**：人脸认证，需进行人脸识别成功后才能签署合同；</li>
<li>**2**：签署密码，需输入与用户在腾讯电子签设置的密码一致才能校验成功进行合同签署；</li>
<li>**3**：运营商三要素，需到运营商处比对手机号实名信息（名字、手机号、证件号）校验一致才能成功进行合同签署。（如果是港澳台客户，建议不要选择这个）</li>
<li>**5**：设备指纹识别，需要对比手机机主预留的指纹信息，校验一致才能成功进行合同签署。（iOS系统暂不支持该校验方式）</li>
<li>**6**：设备面容识别，需要对比手机机主预留的人脸信息，校验一致才能成功进行合同签署。（Android系统暂不支持该校验方式）</li></ul>


默认为1(人脸认证 ),2(签署密码),3(运营商三要素),5(设备指纹识别),6(设备面容识别)

注：
1. 用<font color='red'>模板创建合同场景</font>, 签署人的认证方式需要在配置模板的时候指定, <font color='red'>在创建合同重新指定无效</font>
2. 运营商三要素认证方式对手机号运营商及前缀有限制,可以参考[运营商支持列表类](https://qian.tencent.com/developers/company/mobile_support)得到具体的支持说明
3. 校验方式不允许只包含<font color='red'>设备指纹识别</font>和<font color='red'>设备面容识别</font>，至少需要再增加一种其他校验方式。
4. <font color='red'>设备指纹识别</font>和<font color='red'>设备面容识别</font>只支持小程序使用，其他端暂不支持。
        :type ApproverSignTypes: list of int
        :param _ApproverNeedSignReview: 发起方企业的签署人进行签署操作前，是否需要企业内部走审批流程，取值如下：
<ul><li>**false**：（默认）不需要审批，直接签署。</li>
<li>**true**：需要走审批流程。当到对应参与人签署时，会阻塞其签署操作，等待企业内部审批完成。</li></ul>
企业可以通过CreateFlowSignReview审批接口通知腾讯电子签平台企业内部审批结果
<ul><li>如果企业通知腾讯电子签平台审核通过，签署方可继续签署动作。</li>
<li>如果企业通知腾讯电子签平台审核未通过，平台将继续阻塞签署方的签署动作，直到企业通知平台审核通过。</li></ul>

注：`此功能可用于与企业内部的审批流程进行关联，支持手动、静默签署合同`
        :type ApproverNeedSignReview: bool
        :param _AddSignComponentsLimits: [用PDF文件创建签署流程](https://qian.tencent.com/developers/companyApis/startFlows/CreateFlowByFiles)时,如果设置了外层参数SignBeanTag=1(允许签署过程中添加签署控件),则可通过此参数明确规定合同所使用的签署控件类型（骑缝章、普通章法人章等）和具体的印章（印章ID或者印章类型）或签名方式。

注：`限制印章控件或骑缝章控件情况下,仅本企业签署方可以指定具体印章（通过传递ComponentValue,支持多个），他方企业或个人只支持限制控件类型。`
        :type AddSignComponentsLimits: list of ComponentLimit
        :param _SignInstructionContent: 签署须知：支持传入富文本，最长字数：500个中文字符
        :type SignInstructionContent: str
        :param _Deadline: 签署人的签署截止时间，格式为Unix标准时间戳（秒）

注: `若不设置此参数，则默认使用合同的截止时间，此参数暂不支持合同组子合同`
        :type Deadline: int
        :param _Components: 签署人在合同中的填写控件列表，列表中可支持下列多种填写控件，控件的详细定义参考开发者中心的Component结构体
<ul><li>单行文本控件</li>
<li>多行文本控件</li>
<li>勾选框控件</li>
<li>数字控件</li>
<li>图片控件</li>
<li>数据表格等填写控件</li></ul>

具体使用说明可参考[为签署方指定填写控件](https://qian.tencent.cn/developers/company/createFlowByFiles/#指定签署方填写控件)

注：`此参数仅在通过文件发起合同或者合同组时生效`
        :type Components: list of Component
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
        self._ApproverRoleName = None
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
        self._SignInstructionContent = None
        self._Deadline = None
        self._Components = None

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
    def ApproverRoleName(self):
        return self._ApproverRoleName

    @ApproverRoleName.setter
    def ApproverRoleName(self, ApproverRoleName):
        self._ApproverRoleName = ApproverRoleName

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

    @property
    def SignInstructionContent(self):
        return self._SignInstructionContent

    @SignInstructionContent.setter
    def SignInstructionContent(self, SignInstructionContent):
        self._SignInstructionContent = SignInstructionContent

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def Components(self):
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components


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
        self._ApproverRoleName = params.get("ApproverRoleName")
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
        self._SignInstructionContent = params.get("SignInstructionContent")
        self._Deadline = params.get("Deadline")
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
        


class ApproverItem(AbstractModel):
    """签署方信息，发起合同后可获取到对应的签署方信息，如角色ID，角色名称

    """

    def __init__(self):
        r"""
        :param _SignId: 签署方唯一编号
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
        :param _NoRefuse: 签署方是否可以拒签

<ul><li> **false** : ( 默认)可以拒签</li>
<li> **true** :不可以拒签</li></ul>
        :type NoRefuse: bool
        :param _NoTransfer: 签署方是否可以转他人处理

<ul><li> **false** : ( 默认)可以转他人处理</li>
<li> **true** :不可以转他人处理</li></ul>
        :type NoTransfer: bool
        :param _CanEditApprover: 允许编辑签署人信息（嵌入式使用） 默认true-可以编辑 false-不可以编辑
        :type CanEditApprover: bool
        :param _FillType: 签署人信息补充类型，默认无需补充。

<ul><li> **1** : ( 动态签署人（可发起合同后再补充签署人信息）注：`企业自动签不支持动态补充`</li></ul>

注：
`使用动态签署人能力前，需登陆腾讯电子签控制台打开服务开关`
        :type FillType: int
        :param _FlowReadLimit: 签署人阅读合同限制参数
 <br/>取值：
<ul>
<li> LimitReadTimeAndBottom，阅读合同必须限制阅读时长并且必须阅读到底</li>
<li> LimitReadTime，阅读合同仅限制阅读时长</li>
<li> LimitBottom，阅读合同仅限制必须阅读到底</li>
<li> NoReadTimeAndBottom，阅读合同不限制阅读时长且不限制阅读到底（白名单功能，请联系客户经理开白使用）</li>
</ul>
        :type FlowReadLimit: str
        """
        self._NoRefuse = None
        self._NoTransfer = None
        self._CanEditApprover = None
        self._FillType = None
        self._FlowReadLimit = None

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

    @property
    def CanEditApprover(self):
        return self._CanEditApprover

    @CanEditApprover.setter
    def CanEditApprover(self, CanEditApprover):
        self._CanEditApprover = CanEditApprover

    @property
    def FillType(self):
        return self._FillType

    @FillType.setter
    def FillType(self, FillType):
        self._FillType = FillType

    @property
    def FlowReadLimit(self):
        return self._FlowReadLimit

    @FlowReadLimit.setter
    def FlowReadLimit(self, FlowReadLimit):
        self._FlowReadLimit = FlowReadLimit


    def _deserialize(self, params):
        self._NoRefuse = params.get("NoRefuse")
        self._NoTransfer = params.get("NoTransfer")
        self._CanEditApprover = params.get("CanEditApprover")
        self._FillType = params.get("FillType")
        self._FlowReadLimit = params.get("FlowReadLimit")
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
        


class AuthInfoDetail(AbstractModel):
    """企业扩展服务授权列表详情

    """

    def __init__(self):
        r"""
        :param _Type: 扩展服务类型，和入参一致
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Name: 扩展服务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _HasAuthUserList: 授权员工列表
注意：此字段可能返回 null，表示取不到有效值。
        :type HasAuthUserList: list of HasAuthUser
        :param _HasAuthOrganizationList: 授权企业列表（企业自动签时，该字段有值）
注意：此字段可能返回 null，表示取不到有效值。
        :type HasAuthOrganizationList: list of HasAuthOrganization
        :param _AuthUserTotal: 授权员工列表总数
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthUserTotal: int
        :param _AuthOrganizationTotal: 授权企业列表总数
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthOrganizationTotal: int
        """
        self._Type = None
        self._Name = None
        self._HasAuthUserList = None
        self._HasAuthOrganizationList = None
        self._AuthUserTotal = None
        self._AuthOrganizationTotal = None

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
    def HasAuthUserList(self):
        return self._HasAuthUserList

    @HasAuthUserList.setter
    def HasAuthUserList(self, HasAuthUserList):
        self._HasAuthUserList = HasAuthUserList

    @property
    def HasAuthOrganizationList(self):
        return self._HasAuthOrganizationList

    @HasAuthOrganizationList.setter
    def HasAuthOrganizationList(self, HasAuthOrganizationList):
        self._HasAuthOrganizationList = HasAuthOrganizationList

    @property
    def AuthUserTotal(self):
        return self._AuthUserTotal

    @AuthUserTotal.setter
    def AuthUserTotal(self, AuthUserTotal):
        self._AuthUserTotal = AuthUserTotal

    @property
    def AuthOrganizationTotal(self):
        return self._AuthOrganizationTotal

    @AuthOrganizationTotal.setter
    def AuthOrganizationTotal(self, AuthOrganizationTotal):
        self._AuthOrganizationTotal = AuthOrganizationTotal


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        if params.get("HasAuthUserList") is not None:
            self._HasAuthUserList = []
            for item in params.get("HasAuthUserList"):
                obj = HasAuthUser()
                obj._deserialize(item)
                self._HasAuthUserList.append(obj)
        if params.get("HasAuthOrganizationList") is not None:
            self._HasAuthOrganizationList = []
            for item in params.get("HasAuthOrganizationList"):
                obj = HasAuthOrganization()
                obj._deserialize(item)
                self._HasAuthOrganizationList.append(obj)
        self._AuthUserTotal = params.get("AuthUserTotal")
        self._AuthOrganizationTotal = params.get("AuthOrganizationTotal")
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
<li>**1**: 不绑定自动签账号许可开通，后续使用合同份额进行合同发起</li></ul>
        :type LicenseType: int
        :param _JumpUrl: 开通成功后前端页面跳转的url，此字段的用法场景请联系客户经理确认。

注：`仅支持H5开通场景`, `跳转链接仅支持 https:// , qianapp:// 开头`

跳转场景：
<ul><li>**贵方H5 -> 腾讯电子签H5 -> 贵方H5** : JumpUrl格式: https://YOUR_CUSTOM_URL/xxxx，只需满足 https:// 开头的正确且合规的网址即可。</li>
<li>**贵方原生App -> 腾讯电子签H5 -> 贵方原生App** : JumpUrl格式: qianapp://YOUR_CUSTOM_URL，只需满足 qianapp:// 开头的URL即可。`APP实现方，需要拦截Webview地址跳转，发现url是qianapp:// 开头时跳转到原生页面。`APP拦截地址跳转可参考：<a href='https://stackoverflow.com/questions/41693263/android-webview-err-unknown-url-scheme'>Android</a>，<a href='https://razorpay.com/docs/payments/payment-gateway/web-integration/standard/webview/upi-intent-ios/'>IOS</a> </li></ul>

成功结果返回：
若贵方需要在跳转回时通过链接query参数提示开通成功，JumpUrl中的query应携带如下参数：`appendResult=qian`。这样腾讯电子签H5会在跳转回的url后面会添加query参数提示贵方签署成功，例如： qianapp://YOUR_CUSTOM_URL?action=sign&result=success&from=tencent_ess
        :type JumpUrl: str
        """
        self._UserInfo = None
        self._CertInfoCallback = None
        self._UserDefineSeal = None
        self._SealImgCallback = None
        self._CallbackUrl = None
        self._VerifyChannels = None
        self._LicenseType = None
        self._JumpUrl = None

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

    @property
    def JumpUrl(self):
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl


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
        self._JumpUrl = params.get("JumpUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillUsageDetail(AbstractModel):
    """用户计费使用情况详情

    """

    def __init__(self):
        r"""
        :param _FlowId: 合同流程ID，为32位字符串。
可登录腾讯电子签控制台，在 "合同"->"合同中心" 中查看某个合同的FlowId(在页面中展示为合同ID)。
        :type FlowId: str
        :param _OperatorName: 合同经办人名称
如果有多个经办人用分号隔开。
        :type OperatorName: str
        :param _CreateOrganizationName: 发起方组织机构名称
        :type CreateOrganizationName: str
        :param _FlowName: 合同流程的名称。
        :type FlowName: str
        :param _Status: 当前合同状态,如下是状态码对应的状态。
<ul>
<li>**0**: 还没有发起</li>
<li>**1**: 等待签署</li>
<li>**2**: 部分签署 </li>
<li>**3**: 拒签</li>
<li>**4**: 已签署 </li>
<li>**5**: 已过期 </li>
<li>**6**: 已撤销 </li>
<li>**7**: 还没有预发起</li>
<li>**8**: 等待填写</li>
<li>**9**: 部分填写 </li>
<li>**10**: 拒填</li>
<li>**11**: 已解除</li>
</ul>
        :type Status: int
        :param _QuotaType: 查询的套餐类型
对应关系如下:
<ul>
<li>**CloudEnterprise**: 企业版合同</li>
<li>**SingleSignature**: 单方签章</li>
<li>**CloudProve**: 签署报告</li>
<li>**CloudOnlineSign**: 腾讯会议在线签约</li>
<li>**ChannelWeCard**: 微工卡</li>
<li>**SignFlow**: 合同套餐</li>
<li>**SignFace**: 签署意愿（人脸识别）</li>
<li>**SignPassword**: 签署意愿（密码）</li>
<li>**SignSMS**: 签署意愿（短信）</li>
<li>**PersonalEssAuth**: 签署人实名（腾讯电子签认证）</li>
<li>**PersonalThirdAuth**: 签署人实名（信任第三方认证）</li>
<li>**OrgEssAuth**: 签署企业实名</li>
<li>**FlowNotify**: 短信通知</li>
<li>**AuthService**: 企业工商信息查询</li>
</ul>
        :type QuotaType: str
        :param _UseCount: 合同使用量
注: `如果消耗类型是撤销返还，此值为负值代表返还的合同数量`
        :type UseCount: int
        :param _CostTime: 消耗的时间戳，格式为Unix标准时间戳（秒）。
        :type CostTime: int
        :param _QuotaName: 消耗的套餐名称
        :type QuotaName: str
        :param _CostType: 消耗类型
**1**.扣费
**2**.撤销返还
        :type CostType: int
        :param _Remark: 备注
        :type Remark: str
        """
        self._FlowId = None
        self._OperatorName = None
        self._CreateOrganizationName = None
        self._FlowName = None
        self._Status = None
        self._QuotaType = None
        self._UseCount = None
        self._CostTime = None
        self._QuotaName = None
        self._CostType = None
        self._Remark = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def OperatorName(self):
        return self._OperatorName

    @OperatorName.setter
    def OperatorName(self, OperatorName):
        self._OperatorName = OperatorName

    @property
    def CreateOrganizationName(self):
        return self._CreateOrganizationName

    @CreateOrganizationName.setter
    def CreateOrganizationName(self, CreateOrganizationName):
        self._CreateOrganizationName = CreateOrganizationName

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def QuotaType(self):
        return self._QuotaType

    @QuotaType.setter
    def QuotaType(self, QuotaType):
        self._QuotaType = QuotaType

    @property
    def UseCount(self):
        return self._UseCount

    @UseCount.setter
    def UseCount(self, UseCount):
        self._UseCount = UseCount

    @property
    def CostTime(self):
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def QuotaName(self):
        return self._QuotaName

    @QuotaName.setter
    def QuotaName(self, QuotaName):
        self._QuotaName = QuotaName

    @property
    def CostType(self):
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._OperatorName = params.get("OperatorName")
        self._CreateOrganizationName = params.get("CreateOrganizationName")
        self._FlowName = params.get("FlowName")
        self._Status = params.get("Status")
        self._QuotaType = params.get("QuotaType")
        self._UseCount = params.get("UseCount")
        self._CostTime = params.get("CostTime")
        self._QuotaName = params.get("QuotaName")
        self._CostType = params.get("CostType")
        self._Remark = params.get("Remark")
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
        :param _Operator: 执行本接口操作的员工信息。使用此接口时，必须填写UserId。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _UserId: 员工在腾讯电子签平台的唯一身份标识，为32位字符串。

通过<a href="https://qian.tencent.com/developers/companyApis/staffs/DescribeIntegrationEmployees" target="_blank">DescribeIntegrationEmployees</a>接口获取，也可登录腾讯电子签控制台查看
![image](https://qcloudimg.tencent-cloud.cn/raw/97cfffabb0caa61df16999cd395d7850.png)
        :type UserId: str
        :param _OpenId: 员工在贵司业务系统中的唯一身份标识，用于与腾讯电子签账号进行映射，确保在同一企业内不会出现重复。 该标识最大长度为64位字符串，仅支持包含26个英文字母和数字0-9的字符。
        :type OpenId: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _Status: 绑定是否成功。
<ul><li>**0**：失败</li><li>**1**：成功</li></ul>
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        


class CancelFailureFlow(AbstractModel):
    """撤销失败的流程信息

    """

    def __init__(self):
        r"""
        :param _FlowId: 合同流程ID，为32位字符串。
        :type FlowId: str
        :param _Reason: 撤销失败原因
        :type Reason: str
        """
        self._FlowId = None
        self._Reason = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._Reason = params.get("Reason")
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

可登录腾讯电子签控制台，[点击查看FlowId在控制台中的位置](https://qcloudimg.tencent-cloud.cn/raw/0a83015166cfe1cb043d14f9ec4bd75e.png)
        :type FlowId: str
        :param _CancelMessage: 撤销此合同流程的**撤销理由**，最多支持200个字符长度。只能由中文、字母、数字、中文标点和英文标点组成（不支持表情）。

![image](https://qcloudimg.tencent-cloud.cn/raw/f16cf37dbb3a09d6569877f093b92204/channel_ChannelCancelFlow.png)
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _QrCodeId: 需要取消的签署码ID，为32位字符串。由[创建一码多签签署码](https://qian.tencent.com/developers/companyApis/startFlows/CreateMultiFlowSignQRCode/)返回
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
<ul><li> **E_PRESCRIPTION_AUTO_SIGN** :  电子处方场景</li><li> **OTHER** :  通用场景</li></ul>
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """此结构体 (Component) 用于描述控件属性。

    在通过文件发起合同时，对应的component有三种定位方式
    1. 绝对定位方式 （可以通过 [PDF坐标计算助手](https://qian.tencent.com/developers/tools/template-editor)计算控件的坐标）
    2. 表单域(FIELD)定位方式
    3. 关键字(KEYWORD)定位方式，使用关键字定位时，请确保PDF原始文件内是关键字以文字形式保存在PDF文件中，不支持对图片内文字进行关键字查找

    """

    def __init__(self):
        r"""
        :param _ComponentType: **如果是Component填写控件类型，则可选的字段为**：

<ul><li> <b>TEXT</b> : 普通文本控件，输入文本字符串；</li>
<li> <b>MULTI_LINE_TEXT</b> : 多行文本控件，输入文本字符串；</li>
<li> <b>CHECK_BOX</b> : 勾选框控件，若选中填写ComponentValue 填写 true或者 false 字符串；</li>
<li> <b>FILL_IMAGE</b> : 图片控件，ComponentValue 填写图片的资源 ID；</li>
<li> <b>DYNAMIC_TABLE</b> : 动态表格控件；</li>
<li> <b>ATTACHMENT</b> : 附件控件,ComponentValue 填写附件图片的资源 ID列表，以逗号分隔；</li>
<li> <b>SELECTOR</b> : 选择器控件，ComponentValue填写选择的字符串内容；</li>
<li> <b>DATE</b> : 日期控件；默认是格式化为xxxx年xx月xx日字符串；</li>
<li> <b>WATERMARK</b> : 水印控件；只能分配给发起方，必须设置ComponentExtra；</li>
<li> <b>DISTRICT</b> : 省市区行政区控件，ComponentValue填写省市区行政区字符串内容；</li></ul>

**如果是SignComponent签署控件类型，
需要根据签署人的类型可选的字段为**
* 企业方
<ul><li> <b>SIGN_SEAL</b> : 签署印章控件；</li>
<li> <b>SIGN_DATE</b> : 签署日期控件；</li>
<li> <b>SIGN_SIGNATURE</b> : 用户签名控件；</li>
<li> <b>SIGN_PAGING_SEAL</b> : 骑缝章；若文件发起，需要对应填充ComponentPosY、ComponentWidth、ComponentHeight</li>
<li> <b>SIGN_OPINION</b> : 签署意见控件，用户需要根据配置的签署意见内容，完成对意见内容的确认；</li>
<li> <b>SIGN_LEGAL_PERSON_SEAL</b> : 企业法定代表人控件。</li></ul>

* 个人方
<ul><li> <b>SIGN_DATE</b> : 签署日期控件；</li>
<li> <b>SIGN_SIGNATURE</b> : 用户签名控件；</li></ul>
 
注：` 表单域的控件不能作为印章和签名控件`
        :type ComponentType: str
        :param _ComponentHeight: **在绝对定位方式和关键字定位方式下**，指定控件的高度， 控件高度是指控件在PDF文件中的高度，单位为pt（点）。

        :type ComponentHeight: float
        :param _ComponentWidth: **在绝对定位方式和关键字定位方式下**，指定控件宽度，控件宽度是指控件在PDF文件中的宽度，单位为pt（点）。

        :type ComponentWidth: float
        :param _ComponentPage: **在绝对定位方式方式下**，指定控件所在PDF文件上的页码
**在使用文件发起的情况下**，绝对定位方式的填写控件和签署控件支持使用负数来指定控件在PDF文件上的页码，使用负数时，页码从最后一页开始。例如：ComponentPage设置为-1，即代表在PDF文件的最后一页，以此类推。

注：
1. 页码编号是从<font color="red">1</font>开始编号的。
2.  <font color="red">页面编号不能超过PDF文件的页码总数</font>。如果指定的页码超过了PDF文件的页码总数，在填写和签署时会出现错误，导致无法正常进行操作。
        :type ComponentPage: int
        :param _ComponentPosX: **在绝对定位方式和关键字定位方式下**，可以指定控件横向位置的位置，单位为pt（点）。
        :type ComponentPosX: float
        :param _ComponentPosY: **在绝对定位方式和关键字定位方式下**，可以指定控件纵向位置的位置，单位为pt（点）。
        :type ComponentPosY: float
        :param _FileIndex: <font color="red">【暂未使用】</font>控件所属文件的序号（取值为：0-N）。 目前单文件的情况下，值一直为0
        :type FileIndex: int
        :param _GenerateMode: 控件生成的方式：
<ul><li> <b>NORMAL</b> : 绝对定位控件</li>
<li> <b>FIELD</b> : 表单域</li>
<li> <b>KEYWORD</b> : 关键字（设置关键字时，请确保PDF原始文件内是关键字以文字形式保存在PDF文件中，不支持对图片内文字进行关键字查找）</li></ul>
        :type GenerateMode: str
        :param _ComponentId: 控件唯一ID。

**在绝对定位方式方式下**，ComponentId为控件的ID，长度不能超过30，只能由中文、字母、数字和下划线组成，可以在后续的操作中使用该名称来引用控件。

**在关键字定位方式下**，ComponentId不仅为控件的ID，也是关键字整词。此方式下可以通过"^"来决定是否使用关键字整词匹配能力。

例：

- 如传入的关键字<font color="red">"^甲方签署^"</font >，则会在PDF文件中有且仅有"甲方签署"关键字的地方（<font color="red">前后不能有其他字符</font >）进行对应操作。
- 如传入的关键字为<font color="red">"甲方签署</font >"，则PDF文件中每个出现关键字的位置（<font color="red">前后可以有其他字符</font >）都会执行相应操作。


注：`控件ID可以在一个PDF中不可重复`

<a href="https://qcloudimg.tencent-cloud.cn/raw/93178569d07b4d7dbbe0967ae679e35c.png" target="_blank">点击查看ComponentId在模板编辑页面的位置</a>

        :type ComponentId: str
        :param _ComponentName: **在绝对定位方式方式下**，ComponentName为控件名，长度不能超过20，只能由中文、字母、数字和下划线组成，可以在后续的操作中使用该名称来引用控件。

**在表单域定位方式下**，ComponentName不仅为控件名，也是表单域名称。

注：`控件名可以在一个PDF中可以重复`

<a href="https://qcloudimg.tencent-cloud.cn/raw/93178569d07b4d7dbbe0967ae679e35c.png" target="_blank">点击查看ComponentName在模板页面的位置</a>
        :type ComponentName: str
        :param _ComponentRequired: 如果是<b>填写控件</b>，ComponentRequired表示在填写页面此控件是否必填
<ul><li>false（默认）：可以不填写</li>
<li>true ：必须填写此填写控件</li></ul>
如果是<b>签署控件</b>，签批控件中签署意见等可以不填写， 其他签署控件不受此字段影响
        :type ComponentRequired: bool
        :param _ComponentRecipientId: **在通过接口拉取控件信息场景下**，为出参参数，此控件归属的参与方的角色ID角色（即RecipientId），**发起合同时候不要填写此字段留空即可**
        :type ComponentRecipientId: str
        :param _ComponentExtra: **在所有的定位方式下**，控件的扩展参数，为<font color="red">JSON格式</font>，不同类型的控件会有部分非通用参数。

<font color="red">ComponentType为TEXT、MULTI_LINE_TEXT时</font>，支持以下参数：
<ul><li> <b>Font</b>：目前只支持黑体、宋体</li>
<li> <b>FontSize</b>： 范围12 :72</li>
<li> <b>FontAlign</b>： Left/Right/Center，左对齐/居中/右对齐</li>
<li> <b>FontColor</b>：字符串类型，格式为RGB颜色数字</li></ul>
<b>参数样例</b>：`{"FontColor":"255,0,0","FontSize":12}`

<font color="red">ComponentType为DATE时</font>，支持以下参数：
<ul><li> <b>Font</b>：目前只支持黑体、宋体</li>
<li> <b>FontSize</b>： 范围12 :72</li></ul>
<b>参数样例</b>：`{"FontColor":"255,0,0","FontSize":12}`

<font color="red">ComponentType为WATERMARK时</font>，支持以下参数：
<ul><li> <b>Font</b>：目前只支持黑体、宋体</li>
<li> <b>FontSize</b>： 范围6 :24</li>
<li> <b>Opacity</b>： 透明度，范围0 :1</li>
<li> <b>Density</b>： 水印样式，1-宽松，2-标准（默认值），3-密集，</li>
<li> <b>SubType</b>： 水印类型：CUSTOM_WATERMARK-自定义内容，PERSON_INFO_WATERMARK-访问者信息</li></ul>
<b>参数样例</b>：`"{\"Font\":\"黑体\",\"FontSize\":20,\"Opacity\":0.1,\"Density\":2,\"SubType\":\"PERSON_INFO_WATERMARK\"}"`

<font color="red">ComponentType为FILL_IMAGE时</font>，支持以下参数：
<ul><li> <b>NotMakeImageCenter</b>：bool。是否设置图片居中。false：居中（默认）。 true : 不居中</li>
<li> <b>FillMethod</b> : int. 填充方式。0-铺满（默认）；1-等比例缩放</li></ul>

<font color="red">ComponentType为SIGN_SIGNATURE类型时</font>，可以通过**ComponentTypeLimit**参数控制签名方式
<ul><li> <b>HANDWRITE</b> :  需要实时手写的手写签名</li>
<li> <b>HANDWRITTEN_ESIGN</b> : 长效手写签名， 是使用保存到个人中心的印章列表的手写签名(并且包含HANDWRITE)</li>
<li> <b>OCR_ESIGN</b> : AI智能识别手写签名</li>
<li> <b>ESIGN</b> : 个人印章类型</li>
<li> <b>SYSTEM_ESIGN</b> : 系统签名（该类型可以在用户签署时根据用户姓名一键生成一个签名来进行签署）</li>
<li> <b>IMG_ESIGN</b> : 图片印章(该类型支持用户在签署将上传的PNG格式的图片作为签名)</li></ul>
<b>参考样例</b>：`{"ComponentTypeLimit": ["SYSTEM_ESIGN"]}`
印章的对应关系参考下图
![image](https://qcloudimg.tencent-cloud.cn/raw/ee0498856c060c065628a0c5ba780d6b.jpg)<br><br>

<font color="red">ComponentType为SIGN_SEAL 或者 SIGN_PAGING_SEAL类型时</font>，可以通过**ComponentTypeLimit**参数控制签署方签署时要使用的印章类型，支持指定以下印章类型
<ul><li> <b>OFFICIAL</b> :  企业公章</li>
<li> <b>CONTRACT</b> : 合同专用章</li>
<li> <b>FINANCE</b> : 财务专用章</li>
<li> <b>PERSONNEL</b> : 人事专用章</li></ul>
<b>参考样例</b>：`{\"ComponentTypeLimit\":[\"PERSONNEL\",\"FINANCE\"]}` 表示改印章签署区,客户需使用人事专用章或财务专用章盖章签署。<br><br>

<font color="red">ComponentType为SIGN_DATE时</font>，支持以下参数：
<ul><li> <b>Font</b> :字符串类型目前只支持"黑体"、"宋体"，如果不填默认为"黑体"</li>
<li> <b>FontSize</b> : 数字类型，范围6-72，默认值为12</li>
<li> <b>FontAlign</b> : 字符串类型，可取Left/Right/Center，对应左对齐/居中/右对齐</li>
<li> <b>Format</b> : 字符串类型，日期格式，必须是以下五种之一 “yyyy m d”，”yyyy年m月d日”，”yyyy/m/d”，”yyyy-m-d”，”yyyy.m.d”。</li>
<li> <b>Gaps</b> : 字符串类型，仅在Format为“yyyy m d”时起作用，格式为用逗号分开的两个整数，例如”2,2”，两个数字分别是日期格式的前后两个空隙中的空格个数</li></ul>
如果extra参数为空，默认为”yyyy年m月d日”格式的居中日期
特别地，如果extra中Format字段为空或无法被识别，则extra参数会被当作默认值处理（Font，FontSize，Gaps和FontAlign都不会起效）
<b>参数样例</b>： ` "{"Format":"yyyy m d","FontSize":12,"Gaps":"2,2", "FontAlign":"Right"}"`

<font color="red">ComponentType为SIGN_SEAL类型时</font>，支持以下参数：
<ul><li> <b>PageRanges</b> :PageRange的数组，通过PageRanges属性设置该印章在PDF所有页面上盖章（适用于标书在所有页面盖章的情况）</li></ul>
<b>参数样例</b>：` "{"PageRanges":[{"BeginPage":1,"EndPage":-1}]}"`


<font color="red">关键字模式下支持关键字找不到的情况下不进行报错的设置</font>
<ul><li> <b>IgnoreKeywordError</b> :1-关键字查找不到时不进行报错</li></ul>
场景说明：如果使用关键字进行定位，但是指定的PDF文件中又没有设置的关键字时，发起合同会进行关键字是否存在的校验，如果关键字不存在，会进行报错返回。如果不希望进行报错，可以设置"IgnoreKeywordError"来忽略错误。请注意，如果关键字签署控件对应的签署方在整个PDF文件中一个签署控件都没有，还是会触发报错逻辑。
<b>参数样例</b>：` "{"IgnoreKeywordError":1}"`
        :type ComponentExtra: str
        :param _IsFormType: **在通过接口拉取控件信息场景下**，为出参参数，此控件是否通过表单域定位方式生成，默认false-不是，**发起合同时候不要填写此字段留空即可**
        :type IsFormType: bool
        :param _ComponentValue: 控件填充vaule，ComponentType和传入值类型对应关系：
<ul><li> <b>TEXT</b> : 文本内容</li>
<li> <b>MULTI_LINE_TEXT</b> : 文本内容，可以用  \n 来控制换行位置 </li>
<li> <b>CHECK_BOX</b> : true/false</li>
<li> <b>FILL_IMAGE、ATTACHMENT</b> : 附件的FileId，需要通过UploadFiles接口上传获取</li>
<li> <b>SELECTOR</b> : 选项值</li>
<li> <b>DYNAMIC_TABLE</b>  - 传入json格式的表格内容，详见说明：[数据表格](https://qian.tencent.com/developers/company/dynamic_table)</li>
<li> <b>DATE</b> : 格式化为：xxxx年xx月xx日（例如2024年05年28日）</li>
<li> <b>SIGN_SEAL</b> : 印章ID，于控制台查询获取， [点击查看在控制台上位置](https://qcloudimg.tencent-cloud.cn/raw/f7b0f2ea4a534aada4b893dbf9671eae.png)</li>
<li> <b>SIGN_PAGING_SEAL</b> : 可以指定印章ID，于控制台查询获取， [点击查看在控制台上位置](https://qcloudimg.tencent-cloud.cn/raw/f7b0f2ea4a534aada4b893dbf9671eae.png)</li></ul>


<b>控件值约束说明</b>：
<table> <thead> <tr> <th>特殊控件</th> <th>填写约束</th> </tr> </thead> <tbody> <tr> <td>企业全称控件</td> <td>企业名称中文字符中文括号</td> </tr> <tr> <td>统一社会信用代码控件</td> <td>企业注册的统一社会信用代码</td> </tr> <tr> <td>法人名称控件</td> <td>最大50个字符，2到25个汉字或者1到50个字母</td> </tr> <tr> <td>签署意见控件</td> <td>签署意见最大长度为50字符</td> </tr> <tr> <td>签署人手机号控件</td> <td>国内手机号 13,14,15,16,17,18,19号段长度11位</td> </tr> <tr> <td>签署人身份证控件</td> <td>合法的身份证号码检查</td> </tr> <tr> <td>控件名称</td> <td>控件名称最大长度为20字符，不支持表情</td> </tr> <tr> <td>单行文本控件</td> <td>只允许输入中文，英文，数字，中英文标点符号，不支持表情</td> </tr> <tr> <td>多行文本控件</td> <td>只允许输入中文，英文，数字，中英文标点符号，不支持表情</td> </tr> <tr> <td>勾选框控件</td> <td>选择填字符串true，不选填字符串false</td> </tr> <tr> <td>选择器控件</td> <td>同单行文本控件约束，填写选择值中的字符串</td> </tr> <tr> <td>数字控件</td> <td>请输入有效的数字(可带小数点)</td> </tr> <tr> <td>日期控件</td> <td>格式：yyyy年mm月dd日</td> </tr> <tr> <td>附件控件</td> <td>JPG或PNG图片，上传数量限制，1到6个，最大6个附件，填写上传的资源ID</td> </tr> <tr> <td>图片控件</td> <td>JPG或PNG图片，填写上传的图片资源ID</td> </tr> <tr> <td>邮箱控件</td> <td>有效的邮箱地址, w3c标准</td> </tr> <tr> <td>地址控件</td> <td>只允许输入中文，英文，数字，中英文标点符号，不支持表情</td> </tr> <tr> <td>省市区控件</td> <td>只允许输入中文，英文，数字，中英文标点符号，不支持表情</td> </tr> <tr> <td>性别控件</td> <td>选择值中的字符串</td> </tr> <tr> <td>学历控件</td> <td>选择值中的字符串</td> </tr> <tr> <td>水印控件</td> <td>水印控件设置为CUSTOM_WATERMARK类型时的水印内容</td> </tr> </tbody> </table>
注：   `部分特殊控件需要在控制台配置模板形式创建`
        :type ComponentValue: str
        :param _OffsetX: **如果控件是关键字定位方式**，可以对关键字定位出来的区域进行横坐标方向的调整，单位为pt（点）。例如，如果关键字定位出来的区域偏左或偏右，可以通过调整横坐标方向的参数来使控件位置更加准确。
注意： `向左调整设置为负数， 向右调整设置成正数`
注意：此字段可能返回 null，表示取不到有效值。
        :type OffsetX: float
        :param _OffsetY: **如果控件是关键字定位方式**，可以对关键字定位出来的区域进行纵坐标方向的调整，单位为pt（点）。例如，如果关键字定位出来的区域偏上或偏下，可以通过调整纵坐标方向的参数来使控件位置更加准确。
注意： `向上调整设置为负数， 向下调整设置成正数`
注意：此字段可能返回 null，表示取不到有效值。
        :type OffsetY: float
        :param _KeywordOrder: **如果控件是关键字定位方式**，指定关键字排序规则时，可以选择Positive或Reverse两种排序方式。
<ul><li> <b>Positive</b> :表示正序，即根据关键字在PDF文件内的顺序进行排列</li>
<li> <b>Reverse</b> :表示倒序，即根据关键字在PDF文件内的反序进行排列</li></ul>

在指定KeywordIndexes时，如果使用Positive排序方式，0代表在PDF内查找内容时，查找到的第一个关键字；如果使用Reverse排序方式，0代表在PDF内查找内容时，查找到的最后一个关键字。
        :type KeywordOrder: str
        :param _KeywordPage: **如果控件是关键字定位方式**，在KeywordPage中指定关键字页码时，将只会在该页码中查找关键字，非该页码的关键字将不会查询出来。如果不设置查找所有页面中的关键字。
        :type KeywordPage: int
        :param _RelativeLocation: **如果控件是关键字定位方式**，关键字生成的区域的对齐方式， 可以设置下面的值
<ul><li> <b>Middle</b> :居中</li>
<li> <b>Below</b> :正下方</li>
<li> <b>Right</b> :正右方</li>
<li> <b>LowerRight</b> :右下角</li>
<li> <b>UpperRight</b> :右上角。</li></ul>
示例：如果设置Middle的关键字盖章，则印章的中心会和关键字的中心重合，如果设置Below，则印章在关键字的正下方
        :type RelativeLocation: str
        :param _KeywordIndexes: **如果控件是关键字定位方式**，关键字索引是指在PDF文件中存在多个相同的关键字时，通过索引指定使用哪一个关键字作为最后的结果。可以通过指定多个索引来同时使用多个关键字。例如，[0,2]表示使用PDF文件内第1个和第3个关键字位置作为最后的结果。

注意：关键字索引是从0开始计数的
        :type KeywordIndexes: list of int
        :param _LockComponentValue: **web嵌入发起合同场景下**， 是否锁定填写和签署控件值不允许嵌入页面进行编辑
<ul><li>false（默认）：不锁定控件值，允许在页面编辑控件值</li>
<li>true：锁定控件值，在页面编辑控件值</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type LockComponentValue: bool
        :param _ForbidMoveAndDelete: **web嵌入发起合同场景下**，是否禁止移动和删除填写和签署控件
<ul><li> <b>false（默认）</b> :不禁止移动和删除控件</li>
<li> <b>true</b> : 可以移动和删除控件</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type ForbidMoveAndDelete: bool
        :param _ComponentDateFontSize: <font color="red">【暂未使用】</font>日期签署控件的字号，默认为 12
        :type ComponentDateFontSize: int
        :param _ChannelComponentId: <font color="red">【暂未使用】</font>第三方应用集成平台模板控件 ID 标识
        :type ChannelComponentId: str
        :param _ChannelComponentSource: <font color="red">【暂未使用】</font>第三方应用集成中子客企业控件来源。
<ul><li> <b>0</b> :平台指定；</li>
<li> <b>1</b> :用户自定义</li></ul>
        :type ChannelComponentSource: int
        """
        self._ComponentType = None
        self._ComponentHeight = None
        self._ComponentWidth = None
        self._ComponentPage = None
        self._ComponentPosX = None
        self._ComponentPosY = None
        self._FileIndex = None
        self._GenerateMode = None
        self._ComponentId = None
        self._ComponentName = None
        self._ComponentRequired = None
        self._ComponentRecipientId = None
        self._ComponentExtra = None
        self._IsFormType = None
        self._ComponentValue = None
        self._OffsetX = None
        self._OffsetY = None
        self._KeywordOrder = None
        self._KeywordPage = None
        self._RelativeLocation = None
        self._KeywordIndexes = None
        self._LockComponentValue = None
        self._ForbidMoveAndDelete = None
        self._ComponentDateFontSize = None
        self._ChannelComponentId = None
        self._ChannelComponentSource = None

    @property
    def ComponentType(self):
        return self._ComponentType

    @ComponentType.setter
    def ComponentType(self, ComponentType):
        self._ComponentType = ComponentType

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
    def ChannelComponentSource(self):
        return self._ChannelComponentSource

    @ChannelComponentSource.setter
    def ChannelComponentSource(self, ChannelComponentSource):
        self._ChannelComponentSource = ChannelComponentSource


    def _deserialize(self, params):
        self._ComponentType = params.get("ComponentType")
        self._ComponentHeight = params.get("ComponentHeight")
        self._ComponentWidth = params.get("ComponentWidth")
        self._ComponentPage = params.get("ComponentPage")
        self._ComponentPosX = params.get("ComponentPosX")
        self._ComponentPosY = params.get("ComponentPosY")
        self._FileIndex = params.get("FileIndex")
        self._GenerateMode = params.get("GenerateMode")
        self._ComponentId = params.get("ComponentId")
        self._ComponentName = params.get("ComponentName")
        self._ComponentRequired = params.get("ComponentRequired")
        self._ComponentRecipientId = params.get("ComponentRecipientId")
        self._ComponentExtra = params.get("ComponentExtra")
        self._IsFormType = params.get("IsFormType")
        self._ComponentValue = params.get("ComponentValue")
        self._OffsetX = params.get("OffsetX")
        self._OffsetY = params.get("OffsetY")
        self._KeywordOrder = params.get("KeywordOrder")
        self._KeywordPage = params.get("KeywordPage")
        self._RelativeLocation = params.get("RelativeLocation")
        self._KeywordIndexes = params.get("KeywordIndexes")
        self._LockComponentValue = params.get("LockComponentValue")
        self._ForbidMoveAndDelete = params.get("ForbidMoveAndDelete")
        self._ComponentDateFontSize = params.get("ComponentDateFontSize")
        self._ChannelComponentId = params.get("ChannelComponentId")
        self._ChannelComponentSource = params.get("ChannelComponentSource")
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

1.当ComponentType 是 SIGN_SEAL 或者 SIGN_PAGING_SEAL 时可传入企业印章Id（支持多个）或者以下印章类型

<ul><li> <b>OFFICIAL</b> :  企业公章</li>
<li> <b>CONTRACT</b> : 合同专用章</li>
<li> <b>FINANCE</b> : 财务专用章</li>
<li> <b>PERSONNEL</b> : 人事专用章</li></ul>

**注：`限制印章控件或骑缝章控件情况下,仅本企业签署方可以指定具体印章（通过传递ComponentValue,支持多个),他方企业签署人只能限制类型.若同时指定了印章类型和印章Id,以印章Id为主,印章类型会被忽略`**


2.当ComponentType 是 SIGN_SIGNATURE 时可传入以下类型（支持多个）

<ul><li>HANDWRITE : 需要实时手写的手写签名</li>
<li>HANDWRITTEN_ESIGN : 长效手写签名， 是使用保存到个人中心的印章列表的手写签名(并且包含HANDWRITE)</li>
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
列表中的流程(合同)编号不要重复.
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
        :param _TaskId: 批量撤销任务编号，为32位字符串，可用于[查询批量撤销签署流程任务结果](https://qian.tencent.com/developers/companyApis/operateFlows/CreateBatchCancelFlowUrl) 或关联[批量撤销任务结果回调](https://qian.tencent.com/developers/company/callback_types_contracts_sign#%E4%B9%9D-%E6%89%B9%E9%87%8F%E6%92%A4%E9%94%80%E7%BB%93%E6%9E%9C%E5%9B%9E%E8%B0%83)
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchCancelFlowUrl = None
        self._FailMessages = None
        self._UrlExpireOn = None
        self._TaskId = None
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
        self._BatchCancelFlowUrl = params.get("BatchCancelFlowUrl")
        self._FailMessages = params.get("FailMessages")
        self._UrlExpireOn = params.get("UrlExpireOn")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateBatchInitOrganizationUrlRequest(AbstractModel):
    """CreateBatchInitOrganizationUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _OperateTypes: 初始化操作类型
<ul><li>CREATE_SEAL : 创建印章</li>
<li>AUTH_JOIN_ORGANIZATION_GROUP : 加入集团企业</li>
<li>OPEN_AUTO_SIGN :开通企业自动签署</li></ul>
        :type OperateTypes: list of str
        :param _OrganizationIds: 批量操作的企业Id列表，最大支持50个
        :type OrganizationIds: list of str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._OperateTypes = None
        self._OrganizationIds = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def OperateTypes(self):
        return self._OperateTypes

    @OperateTypes.setter
    def OperateTypes(self, OperateTypes):
        self._OperateTypes = OperateTypes

    @property
    def OrganizationIds(self):
        return self._OrganizationIds

    @OrganizationIds.setter
    def OrganizationIds(self, OrganizationIds):
        self._OrganizationIds = OrganizationIds

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
        self._OperateTypes = params.get("OperateTypes")
        self._OrganizationIds = params.get("OrganizationIds")
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
        


class CreateBatchInitOrganizationUrlResponse(AbstractModel):
    """CreateBatchInitOrganizationUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MiniAppPath: 小程序路径
        :type MiniAppPath: str
        :param _OperateLongUrl: 操作长链
        :type OperateLongUrl: str
        :param _OperateShortUrl: 操作短链
        :type OperateShortUrl: str
        :param _QRCodeUrl: 操作二维码
        :type QRCodeUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MiniAppPath = None
        self._OperateLongUrl = None
        self._OperateShortUrl = None
        self._QRCodeUrl = None
        self._RequestId = None

    @property
    def MiniAppPath(self):
        return self._MiniAppPath

    @MiniAppPath.setter
    def MiniAppPath(self, MiniAppPath):
        self._MiniAppPath = MiniAppPath

    @property
    def OperateLongUrl(self):
        return self._OperateLongUrl

    @OperateLongUrl.setter
    def OperateLongUrl(self, OperateLongUrl):
        self._OperateLongUrl = OperateLongUrl

    @property
    def OperateShortUrl(self):
        return self._OperateShortUrl

    @OperateShortUrl.setter
    def OperateShortUrl(self, OperateShortUrl):
        self._OperateShortUrl = OperateShortUrl

    @property
    def QRCodeUrl(self):
        return self._QRCodeUrl

    @QRCodeUrl.setter
    def QRCodeUrl(self, QRCodeUrl):
        self._QRCodeUrl = QRCodeUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MiniAppPath = params.get("MiniAppPath")
        self._OperateLongUrl = params.get("OperateLongUrl")
        self._OperateShortUrl = params.get("OperateShortUrl")
        self._QRCodeUrl = params.get("QRCodeUrl")
        self._RequestId = params.get("RequestId")


class CreateBatchOrganizationAuthorizationUrlRequest(AbstractModel):
    """CreateBatchOrganizationAuthorizationUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _AdminName: 组织机构超管姓名。 在注册流程中，必须是超管本人进行操作。
此参数需要跟[创建企业批量认证链接](https://qian.tencent.com/developers/companyApis/organizations/CreateBatchOrganizationRegistrationTasks)中 AdminName 保持一致。
        :type AdminName: str
        :param _AdminMobile: 组织机构超管手机号。 在注册流程中，必须是超管本人进行操作。此参数需要跟[创建企业批量认证链接](https://qian.tencent.com/developers/companyApis/organizations/CreateBatchOrganizationRegistrationTasks)中 Admin Mobile保持一致。
        :type AdminMobile: str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _SubTaskIds: 企业批量认证链接的子任务 SubTaskId，该 SubTaskId 是通过接口 查询企业批量认证链接 DescribeBatchOrganizationRegistrationUrls 获得。此参数需与超管个人三要素（AdminName，AdminMobile，AdminIdCardNumber）配合使用。若 SubTaskId 不属于传入的超级管理员，将进行筛选。
        :type SubTaskIds: list of str
        :param _AdminIdCardType: 组织机构超管证件类型支持以下类型
- ID_CARD : 居民身份证 (默认值)
-  HONGKONG_AND_MACAO : 港澳居民来往内地通行证
- HONGKONG_MACAO_AND_TAIWAN : 港澳台居民居住证(格式同居民身份证)
此参数需要跟[创建企业批量认证链接](https://qian.tencent.com/developers/companyApis/organizations/CreateBatchOrganizationRegistrationTasks)中 AdminIdCardType保持一致。
        :type AdminIdCardType: str
        :param _AdminIdCardNumber: 组织机构超管证件号。 在注册流程中，必须是超管本人进行操作。此参数需要跟[创建企业批量认证链接](https://qian.tencent.com/developers/companyApis/organizations/CreateBatchOrganizationRegistrationTasks)中 AdminIdCardNumber保持一致。
        :type AdminIdCardNumber: str
        :param _Endpoint: 要跳转的链接类型<ul><li> **HTTP**：跳转电子签小程序的http_url, 短信通知或者H5跳转适合此类型  ，此时返回长链 (默认类型)</li><li>**HTTP_SHORT_URL**：跳转电子签小程序的http_url, 短信通知或者H5跳转适合此类型，此时返回短链</li><li>**APP**： 第三方APP或小程序跳转电子签小程序的path,  APP或者小程序跳转适合此类型</li><li>**QR_CODE**： 跳转电子签小程序的http_url的二维码形式,  可以在页面展示适合此类型</li></ul>
        :type Endpoint: str
        """
        self._Operator = None
        self._AdminName = None
        self._AdminMobile = None
        self._Agent = None
        self._SubTaskIds = None
        self._AdminIdCardType = None
        self._AdminIdCardNumber = None
        self._Endpoint = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def AdminName(self):
        return self._AdminName

    @AdminName.setter
    def AdminName(self, AdminName):
        self._AdminName = AdminName

    @property
    def AdminMobile(self):
        return self._AdminMobile

    @AdminMobile.setter
    def AdminMobile(self, AdminMobile):
        self._AdminMobile = AdminMobile

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def SubTaskIds(self):
        return self._SubTaskIds

    @SubTaskIds.setter
    def SubTaskIds(self, SubTaskIds):
        self._SubTaskIds = SubTaskIds

    @property
    def AdminIdCardType(self):
        return self._AdminIdCardType

    @AdminIdCardType.setter
    def AdminIdCardType(self, AdminIdCardType):
        self._AdminIdCardType = AdminIdCardType

    @property
    def AdminIdCardNumber(self):
        return self._AdminIdCardNumber

    @AdminIdCardNumber.setter
    def AdminIdCardNumber(self, AdminIdCardNumber):
        self._AdminIdCardNumber = AdminIdCardNumber

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._AdminName = params.get("AdminName")
        self._AdminMobile = params.get("AdminMobile")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._SubTaskIds = params.get("SubTaskIds")
        self._AdminIdCardType = params.get("AdminIdCardType")
        self._AdminIdCardNumber = params.get("AdminIdCardNumber")
        self._Endpoint = params.get("Endpoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchOrganizationAuthorizationUrlResponse(AbstractModel):
    """CreateBatchOrganizationAuthorizationUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AuthUrl: 批量企业注册链接-单链接包含多条认证流，根据Endpoint的不同设置，返回不同的链接地址。失效时间：7天
跳转链接, 链接的有效期根据企业,员工状态和终端等有区别, 可以参考下表
<table> <thead> <tr> <th>Endpoint</th> <th>示例</th> <th>链接有效期限</th> </tr> </thead>  <tbody>
 <tr> <td>HTTP</td> <td>https://res.ess.tencent.cn/cdn/h5-activity-dev/jump-mp.html?to=AUTHORIZATION_ENTERPRISE_FOR_BATCH_SUBMIT&shortKey=yDCHHURDfBxSB2rj2Bfa</td> <td>7天</td> </tr> 
<tr> <td>HTTP_SHORT_URL</td> <td>https://test.essurl.cn/8gDKUBAWK8</td> <td>7天</td> </tr> 
<tr> <td>APP</td> <td>pages/guide/index?to=AUTHORIZATION_ENTERPRISE_FOR_BATCH_SUBMIT&shortKey=yDCHpURDfR6iEkdpsDde</td> <td>7天</td> </tr><tr> <td>QR_CODE</td> <td>https://dyn.test.ess.tencent.cn/imgs/qrcode_urls/authorization_enterprise_for_batch_submit/yDCHHUUckpbdauq9UEjnoFDCCumAMmv1.png</td> <td>7天</td> </tr> </tbody> </table>
注： 
`1.创建的链接应避免被转义，如：&被转义为\u0026；如使用Postman请求后，请选择响应类型为 JSON，否则链接将被转义`

        :type AuthUrl: str
        :param _ErrorMessages: 认证流认证失败信息
        :type ErrorMessages: list of str
        :param _ExpireTime: 链接过期时间，为 7 天后，创建时间，格式为Unix标准时间戳（秒）。
        :type ExpireTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AuthUrl = None
        self._ErrorMessages = None
        self._ExpireTime = None
        self._RequestId = None

    @property
    def AuthUrl(self):
        return self._AuthUrl

    @AuthUrl.setter
    def AuthUrl(self, AuthUrl):
        self._AuthUrl = AuthUrl

    @property
    def ErrorMessages(self):
        return self._ErrorMessages

    @ErrorMessages.setter
    def ErrorMessages(self, ErrorMessages):
        self._ErrorMessages = ErrorMessages

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AuthUrl = params.get("AuthUrl")
        self._ErrorMessages = params.get("ErrorMessages")
        self._ExpireTime = params.get("ExpireTime")
        self._RequestId = params.get("RequestId")


class CreateBatchOrganizationRegistrationTasksRequest(AbstractModel):
    """CreateBatchOrganizationRegistrationTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _RegistrationOrganizations: 组织机构注册信息。
一次最多支持10条认证流
        :type RegistrationOrganizations: list of RegistrationOrganizationInfo
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Endpoint: 要生成链接的类型, 可以选择的值如下: 

<ul>
<li>(默认)PC: 生成PC端的链接</li>
<li>SHORT_URL: H5跳转到电子签小程序链接的短链形式, 一般用于发送短信中带的链接, 打开后进入腾讯电子签小程序</li>
<li>APP：生成小程序跳转链接</li>
<li>H5：生成H5跳转长链接</li>
<li>SHORT_H5：生成H5跳转短链</li>
</ul>
        :type Endpoint: str
        """
        self._Operator = None
        self._RegistrationOrganizations = None
        self._Agent = None
        self._Endpoint = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def RegistrationOrganizations(self):
        return self._RegistrationOrganizations

    @RegistrationOrganizations.setter
    def RegistrationOrganizations(self, RegistrationOrganizations):
        self._RegistrationOrganizations = RegistrationOrganizations

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("RegistrationOrganizations") is not None:
            self._RegistrationOrganizations = []
            for item in params.get("RegistrationOrganizations"):
                obj = RegistrationOrganizationInfo()
                obj._deserialize(item)
                self._RegistrationOrganizations.append(obj)
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._Endpoint = params.get("Endpoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchOrganizationRegistrationTasksResponse(AbstractModel):
    """CreateBatchOrganizationRegistrationTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 生成注册链接的任务Id，
根据这个id， 调用DescribeBatchOrganizationRegistrationUrls 获取生成的链接，进入认证流程
        :type TaskId: str
        :param _ErrorMessages: 批量生成企业认证链接的详细错误信息，
顺序与输入参数保持一致。
若企业认证均成功生成，则不返回错误信息；
若存在任何错误，则返回具体的错误描述。
        :type ErrorMessages: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._ErrorMessages = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._ErrorMessages = params.get("ErrorMessages")
        self._RequestId = params.get("RequestId")


class CreateBatchQuickSignUrlRequest(AbstractModel):
    """CreateBatchQuickSignUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowApproverInfo: 批量签署的流程签署人，其中姓名(ApproverName)、参与人类型(ApproverType)必传，手机号(ApproverMobile)和证件信息(ApproverIdCardType、ApproverIdCardNumber)可任选一种或全部传入。
注:
`1. ApproverType目前只支持个人类型的签署人。`
`2. 签署人只能有手写签名和时间类型的签署控件，其他类型的填写控件和签署控件暂时都未支持。`
`3. 当需要通过短信验证码签署时，手机号ApproverMobile需要与发起合同时填写的用户手机号一致。`
        :type FlowApproverInfo: :class:`tencentcloud.ess.v20201111.models.FlowCreateApprover`
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId(子企业的组织ID)为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowIds: 批量签署的合同流程ID数组。
注: `在调用此接口时，请确保合同流程均为本企业发起，且合同数量不超过100个。`
        :type FlowIds: list of str
        :param _FlowGroupId: 合同组编号
注：`该参数和合同流程ID数组必须二选一`
        :type FlowGroupId: str
        :param _JumpUrl: 签署完之后的H5页面的跳转链接，此链接及支持http://和https://，最大长度1000个字符。(建议https协议)
        :type JumpUrl: str
        :param _SignatureTypes: 指定批量签署合同的签名类型，可传递以下值：
<ul><li>**0**：手写签名(默认)</li>
<li>**1**：OCR楷体</li>
<li>**2**：姓名印章</li>
<li>**3**：图片印章</li>
<li>**4**：系统签名</li></ul>
注：
<ul><li>默认情况下，签名类型为手写签名</li>
<li>您可以传递多种值，表示可用多种签名类型。</li>
<li>该参数会覆盖您合同中的签名类型，若您在发起合同时限定了签名类型(赋值签名类型给ComponentTypeLimit)，请将这些签名类型赋予此参数</li>
</ul>
        :type SignatureTypes: list of int
        :param _ApproverSignTypes: 指定批量签署合同的认证校验方式，可传递以下值：
<ul><li>**1**：人脸认证(默认)，需进行人脸识别成功后才能签署合同</li>
<li>**2**：密码认证(默认)，需输入与用户在腾讯电子签设置的密码一致才能校验成功进行合同签署</li>
<li>**3**：运营商三要素，需到运营商处比对手机号实名信息(名字、手机号、证件号)校验一致才能成功进行合同签署。</li></ul>
注：
<ul><li>默认情况下，认证校验方式为人脸和密码认证</li>
<li>您可以传递多种值，表示可用多种认证校验方式。</li></ul>
        :type ApproverSignTypes: list of int
        :param _SignTypeSelector: 生成H5签署链接时，您可以指定签署方签署合同的认证校验方式的选择模式，可传递一下值：
<ul><li>**0**：签署方自行选择，签署方可以从预先指定的认证方式中自由选择；</li>
<li>**1**：自动按顺序首位推荐，签署方无需选择，系统会优先推荐使用第一种认证方式。</li></ul>
注：
`不指定该值时，默认为签署方自行选择。`
        :type SignTypeSelector: int
        """
        self._FlowApproverInfo = None
        self._Agent = None
        self._Operator = None
        self._FlowIds = None
        self._FlowGroupId = None
        self._JumpUrl = None
        self._SignatureTypes = None
        self._ApproverSignTypes = None
        self._SignTypeSelector = None

    @property
    def FlowApproverInfo(self):
        return self._FlowApproverInfo

    @FlowApproverInfo.setter
    def FlowApproverInfo(self, FlowApproverInfo):
        self._FlowApproverInfo = FlowApproverInfo

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
    def JumpUrl(self):
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl

    @property
    def SignatureTypes(self):
        return self._SignatureTypes

    @SignatureTypes.setter
    def SignatureTypes(self, SignatureTypes):
        self._SignatureTypes = SignatureTypes

    @property
    def ApproverSignTypes(self):
        return self._ApproverSignTypes

    @ApproverSignTypes.setter
    def ApproverSignTypes(self, ApproverSignTypes):
        self._ApproverSignTypes = ApproverSignTypes

    @property
    def SignTypeSelector(self):
        return self._SignTypeSelector

    @SignTypeSelector.setter
    def SignTypeSelector(self, SignTypeSelector):
        self._SignTypeSelector = SignTypeSelector


    def _deserialize(self, params):
        if params.get("FlowApproverInfo") is not None:
            self._FlowApproverInfo = FlowCreateApprover()
            self._FlowApproverInfo._deserialize(params.get("FlowApproverInfo"))
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowIds = params.get("FlowIds")
        self._FlowGroupId = params.get("FlowGroupId")
        self._JumpUrl = params.get("JumpUrl")
        self._SignatureTypes = params.get("SignatureTypes")
        self._ApproverSignTypes = params.get("ApproverSignTypes")
        self._SignTypeSelector = params.get("SignTypeSelector")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchQuickSignUrlResponse(AbstractModel):
    """CreateBatchQuickSignUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowApproverUrlInfo: 签署人签署链接信息
        :type FlowApproverUrlInfo: :class:`tencentcloud.ess.v20201111.models.FlowApproverUrlInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowApproverUrlInfo = None
        self._RequestId = None

    @property
    def FlowApproverUrlInfo(self):
        return self._FlowApproverUrlInfo

    @FlowApproverUrlInfo.setter
    def FlowApproverUrlInfo(self, FlowApproverUrlInfo):
        self._FlowApproverUrlInfo = FlowApproverUrlInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FlowApproverUrlInfo") is not None:
            self._FlowApproverUrlInfo = FlowApproverUrlInfo()
            self._FlowApproverUrlInfo._deserialize(params.get("FlowApproverUrlInfo"))
        self._RequestId = params.get("RequestId")


class CreateBatchSignUrlRequest(AbstractModel):
    """CreateBatchSignUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Name: 签署方经办人的姓名。
经办人的姓名将用于身份认证和电子签名，请确保填写的姓名为签署方的真实姓名，而非昵称等代名。

注：`请确保和合同中填入的一致`, `除动态签署人场景外，此参数必填`
        :type Name: str
        :param _Mobile: 手机号码， 支持国内手机号11位数字(无需加+86前缀或其他字符)。
请确认手机号所有方为此业务通知方。

注：`请确保和合同中填入的一致,  若无法保持一致，请确保在发起和生成批量签署链接时传入相同的参与方证件信息`，`除动态签署人场景外，此参数必填`
        :type Mobile: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _IdCardType: 证件类型，支持以下类型
<ul><li>ID_CARD : 中国大陆居民身份证 (默认值)</li>
<li>HONGKONG_AND_MACAO : 港澳居民来往内地通行证</li>
<li>HONGKONG_MACAO_AND_TAIWAN : 港澳台居民居住证(格式同居民身份证)</li></ul>

注：`请确保和合同中填入的一致`
        :type IdCardType: str
        :param _IdCardNumber: 证件号码，应符合以下规则
<ul><li>居民身份证号码应为18位字符串，由数字和大写字母X组成（如存在X，请大写）。</li>
<li>港澳居民来往内地通行证号码共11位。第1位为字母，“H”字头签发给香港居民，“M”字头签发给澳门居民；第2位至第11位为数字。</li>
<li>港澳台居民居住证号码编码规则与中国大陆身份证相同，应为18位字符串。</li></ul>

注：`请确保和合同中填入的一致`
        :type IdCardNumber: str
        :param _NotifyType: 通知用户方式：
<ul>
<li>**NONE** : 不通知（默认）</li>
<li>**SMS** : 短信通知（发送短信通知到Mobile参数所传的手机号）</li>
</ul>
        :type NotifyType: str
        :param _FlowIds: 批量签署的合同流程ID数组。
注: `在调用此接口时，请确保合同流程均为本企业发起，且合同数量不超过100个。`
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
        :param _FlowBatchUrlInfo: 批量签署合同相关信息，指定合同和签署方的信息，用于补充动态签署人。	
        :type FlowBatchUrlInfo: :class:`tencentcloud.ess.v20201111.models.FlowBatchUrlInfo`
        """
        self._Operator = None
        self._Name = None
        self._Mobile = None
        self._Agent = None
        self._IdCardType = None
        self._IdCardNumber = None
        self._NotifyType = None
        self._FlowIds = None
        self._OrganizationName = None
        self._JumpToDetail = None
        self._FlowBatchUrlInfo = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

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
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

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

    @property
    def FlowBatchUrlInfo(self):
        return self._FlowBatchUrlInfo

    @FlowBatchUrlInfo.setter
    def FlowBatchUrlInfo(self, FlowBatchUrlInfo):
        self._FlowBatchUrlInfo = FlowBatchUrlInfo


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._Name = params.get("Name")
        self._Mobile = params.get("Mobile")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
        self._NotifyType = params.get("NotifyType")
        self._FlowIds = params.get("FlowIds")
        self._OrganizationName = params.get("OrganizationName")
        self._JumpToDetail = params.get("JumpToDetail")
        if params.get("FlowBatchUrlInfo") is not None:
            self._FlowBatchUrlInfo = FlowBatchUrlInfo()
            self._FlowBatchUrlInfo._deserialize(params.get("FlowBatchUrlInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchSignUrlResponse(AbstractModel):
    """CreateBatchSignUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SignUrl: 批量签署链接，以短链形式返回，短链的有效期参考回参中的 ExpiredTime。

注: 
1. 非小程序和APP集成使用
2. <font color="red">生成的链路后面不能再增加参数</font>（会出现覆盖链接中已有参数导致错误）
        :type SignUrl: str
        :param _ExpiredTime: 链接过期时间以 Unix 时间戳格式表示，默认生成链接时间起，往后7天有效期。过期后短链将失效，无法打开。
        :type ExpiredTime: int
        :param _MiniAppPath: 从客户小程序或者客户APP跳转至腾讯电子签小程序进行批量签署的跳转路径

注: 
1. 小程序和APP集成使用
2. <font color="red">生成的链路后面不能再增加参数</font>（会出现覆盖链接中已有参数导致错误）
        :type MiniAppPath: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
<li>html</li>
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
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _TemplateId: 用户配置的合同模板ID，会基于此模板创建合同文档，为32位字符串。

[点击查看模板Id在控制台上的位置](https://qcloudimg.tencent-cloud.cn/raw/253071cc2f7becb063c7cf71b37b7861.png)
        :type TemplateId: str
        :param _FlowId: 合同流程ID，为32位字符串。
此接口的合同流程ID需要由[创建签署流程](https://qian.tencent.com/developers/companyApis/startFlows/CreateFlow)接口创建得到。
        :type FlowId: str
        :param _FileNames: 文件名列表，单个文件名最大长度200个字符，暂时仅支持单文件发起。设置后流程对应的文件名称当前设置的值。
        :type FileNames: list of str
        :param _FormFields: 电子文档的填写控件的填充内容。具体方式可以参考[FormField](https://qian.tencent.com/developers/companyApis/dataTypes/#formfield)结构体的定义。
<ul>
<li>支持自动签传递印章，可通过指定自动签控件id，指定印章id来完成</li>
<li>附件控件支持传入图片、文件资源id，并将内容合成到合同文件中。支持的文件类型有doc、docx、xls、xlsx、html、jpg、jpeg、png、bmp、txt、pdf。需要注意如果传入的资源类型都是图片类型，图片资源会放置在合同文件的末尾，如果传入的资源有非图片类型资源，会将资源放置在附件控件所在页面的下一页。</li>
</ul>
注：只有在控制台编辑模板时，<font color="red">归属给发起方</font>的填写控件（如下图）才能在创建文档的时候进行内容填充。
![image](https://qcloudimg.tencent-cloud.cn/raw/a54a76a58c454593d06d8e9883ecc9b3.png)
        :type FormFields: list of FormField
        :param _NeedPreview: 是否为预览模式，取值如下：
<ul><li> **false**：非预览模式（默认），会产生合同流程并返回合同流程编号FlowId。</li> 
<li> **true**：预览模式，不产生合同流程，不返回合同流程编号FlowId，而是返回预览链接PreviewUrl，有效期为300秒，用于查看真实发起后合同的样子。 <font color="red">注意： 以预览模式创建的合同仅供查看，因此参与方无法进行签署操作</font> </li></ul>
注: `当使用的模板中存在动态表格控件时，预览结果中没有动态表格的填写内容，动态表格合成完后会触发文档合成完成的回调通知`
        :type NeedPreview: bool
        :param _PreviewType: 预览模式下产生的预览链接类型 
<ul><li> **0** :(默认) 文件流 ,点开后下载预览的合同PDF文件 </li>
<li> **1** :H5链接 ,点开后在浏览器中展示合同的样子。</li></ul>
注: `1.此参数在NeedPreview 为true时有效`
`2.动态表格控件不支持H5链接方式预览`
        :type PreviewType: int
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _ClientToken: 已废弃字段，客户端Token，保持接口幂等性,最大长度64个字符
        :type ClientToken: str
        """
        self._Operator = None
        self._TemplateId = None
        self._FlowId = None
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
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

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
        self._TemplateId = params.get("TemplateId")
        self._FlowId = params.get("FlowId")
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
后续需用同样的FlowId再次调用[发起签署流程](https://qian.tencent.com/developers/companyApis/startFlows/StartFlow)，合同才能进入签署环节
        :type DocumentId: str
        :param _PreviewFileUrl: 合同预览链接URL。

注: `1.如果是预览模式(即NeedPreview设置为true)时, 才会有此预览链接URL`
`2.当使用的模板中存在动态表格控件时，预览结果中没有动态表格的填写内容`
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewFileUrl: str
        :param _Approvers: 签署方信息，如角色ID、角色名称等
注意：此字段可能返回 null，表示取不到有效值。
        :type Approvers: list of ApproverItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DocumentId = None
        self._PreviewFileUrl = None
        self._Approvers = None
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
        self._DocumentId = params.get("DocumentId")
        self._PreviewFileUrl = params.get("PreviewFileUrl")
        if params.get("Approvers") is not None:
            self._Approvers = []
            for item in params.get("Approvers"):
                obj = ApproverItem()
                obj._deserialize(item)
                self._Approvers.append(obj)
        self._RequestId = params.get("RequestId")


class CreateEmbedWebUrlRequest(AbstractModel):
    """CreateEmbedWebUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
<br/>注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _EmbedType: WEB嵌入资源类型，支持以下类型
<ul><li>CREATE_SEAL: 生成创建印章的嵌入页面</li>
<li>CREATE_TEMPLATE：生成创建模板的嵌入页面</li>
<li>MODIFY_TEMPLATE：生成编辑模板的嵌入页面</li>
<li>PREVIEW_TEMPLATE：生成预览模板的嵌入页面</li>
<li>PREVIEW_SEAL_LIST：生成预览印章列表的嵌入页面</li>
<li>PREVIEW_SEAL_DETAIL：生成预览印章详情的嵌入页面</li>
<li>EXTEND_SERVICE：生成拓展服务的嵌入页面</li>
<li>PREVIEW_FLOW：生成预览合同的嵌入页面（支持移动端）</li>
<li>PREVIEW_FLOW_DETAIL：生成查看合同详情的嵌入页面（仅支持PC端）</li></ul>
        :type EmbedType: str
        :param _BusinessId: WEB嵌入的业务资源ID
<ul><li>PREVIEW_SEAL_DETAIL，必填，取值为印章id</li>
<li>MODIFY_TEMPLATE，PREVIEW_TEMPLATE，必填，取值为模板id</li>
<li>PREVIEW_FLOW，PREVIEW_FLOW_DETAIL，必填，取值为合同id</li>
</ul>
        :type BusinessId: str
        :param _Agent: 代理企业和员工的信息。
<br/>在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Reviewer: 抄送方信息
        :type Reviewer: :class:`tencentcloud.ess.v20201111.models.ReviewerInfo`
        :param _Option: 个性化参数，用于控制页面展示内容
        :type Option: :class:`tencentcloud.ess.v20201111.models.EmbedUrlOption`
        :param _UserData: <ul> <li>目前仅支持EmbedType=CREATE_TEMPLATE时传入</li> <li>指定后，创建，编辑，删除模板时，回调都会携带该userData</li> <li>支持的格式：json字符串的BASE64编码字符串</li> <li>示例：<ul>                  <li>json字符串：{"ComeFrom":"xxx"}，BASE64编码：eyJDb21lRnJvbSI6Inh4eCJ9</li>                  <li>eyJDb21lRnJvbSI6Inh4eCJ9，为符合要求的userData数据格式</li> </ul> </li> </ul>
        :type UserData: str
        """
        self._Operator = None
        self._EmbedType = None
        self._BusinessId = None
        self._Agent = None
        self._Reviewer = None
        self._Option = None
        self._UserData = None

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
        self._UserData = params.get("UserData")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateEmployeeQualificationSealQrCodeRequest(AbstractModel):
    """CreateEmployeeQualificationSealQrCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。使用此接口时，必须填写userId。 支持填入集团子公司经办人 userId 代发合同。  注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Agent: 代理企业和员工的信息。 在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _HintText: 提示信息，扫码后此信息会展示给扫描用户，用来提示用户授权操作的目的，会在授权界面下面的位置展示。

![image](https://qcloudimg.tencent-cloud.cn/raw/8436ffd78c20605e6b133ff4bc4d2ac7.png)
        :type HintText: str
        """
        self._Operator = None
        self._Agent = None
        self._HintText = None

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
    def HintText(self):
        return self._HintText

    @HintText.setter
    def HintText(self, HintText):
        self._HintText = HintText


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._HintText = params.get("HintText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmployeeQualificationSealQrCodeResponse(AbstractModel):
    """CreateEmployeeQualificationSealQrCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QrcodeBase64: 二维码图片的Base64  注:  `此二维码的有效时间为7天，过期后需要重新生成新的二维码图片`
        :type QrcodeBase64: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QrcodeBase64 = None
        self._RequestId = None

    @property
    def QrcodeBase64(self):
        return self._QrcodeBase64

    @QrcodeBase64.setter
    def QrcodeBase64(self, QrcodeBase64):
        self._QrcodeBase64 = QrcodeBase64

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._QrcodeBase64 = params.get("QrcodeBase64")
        self._RequestId = params.get("RequestId")


class CreateExtendedServiceAuthInfosRequest(AbstractModel):
    """CreateExtendedServiceAuthInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _UserIds: 本企业员工的id，需要已实名，正常在职员工
        :type UserIds: list of str
        :param _ExtendServiceType: 取值
<ul><li>OPEN_SERVER_SIGN：企业自动签</li>
<li>BATCH_SIGN：批量签署</li>
</ul>
        :type ExtendServiceType: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._UserIds = None
        self._ExtendServiceType = None
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
        self._UserIds = params.get("UserIds")
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
        


class CreateExtendedServiceAuthInfosResponse(AbstractModel):
    """CreateExtendedServiceAuthInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateFlowApproversRequest(AbstractModel):
    """CreateFlowApprovers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Approvers: 补充签署环节签署候选人信息。

注：` 如果发起方指定的补充签署人是企业微信签署人（ApproverSource=WEWORKAPP），则需要提供企业微信UserId进行补充； 如果不指定，则使用姓名和手机号进行补充。`
        :type Approvers: list of FillApproverInfo
        :param _FlowId: 合同流程ID，为32位字符串。
建议开发者妥善保存此流程ID，以便于顺利进行后续操作。
可登录腾讯电子签控制台，在 "合同"->"合同中心" 中查看某个合同的FlowId(在页面中展示为合同ID)。
        :type FlowId: str
        :param _FillApproverType: 签署人信息补充方式

<ul><li>**0**: <font color="red">或签合同</font>添加签署候选人，或签支持一个节点传多个签署人，不传值默认或签。
注: `或签只支持企业签署方`</li>
<li>**1**: <font color="red">动态签署人合同</font>的添加签署候选人，支持企业或个人签署方。</li></ul>
        :type FillApproverType: int
        :param _Initiator: 在可定制的企业微信通知中，发起人可以根据具体需求进行自定义设置。
        :type Initiator: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _FlowGroupId: 合同流程组的组ID, 在合同流程组场景下，生成合同流程组的签署链接时需要赋值
        :type FlowGroupId: str
        """
        self._Operator = None
        self._Approvers = None
        self._FlowId = None
        self._FillApproverType = None
        self._Initiator = None
        self._Agent = None
        self._FlowGroupId = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Approvers(self):
        return self._Approvers

    @Approvers.setter
    def Approvers(self, Approvers):
        self._Approvers = Approvers

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def FillApproverType(self):
        return self._FillApproverType

    @FillApproverType.setter
    def FillApproverType(self, FillApproverType):
        self._FillApproverType = FillApproverType

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
        if params.get("Approvers") is not None:
            self._Approvers = []
            for item in params.get("Approvers"):
                obj = FillApproverInfo()
                obj._deserialize(item)
                self._Approvers.append(obj)
        self._FlowId = params.get("FlowId")
        self._FillApproverType = params.get("FillApproverType")
        self._Initiator = params.get("Initiator")
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
        


class CreateFlowApproversResponse(AbstractModel):
    """CreateFlowApprovers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FillError: 批量补充签署人时，补充失败的报错说明

注:`目前仅补充动态签署人时会返回补充失败的原因`
注意：此字段可能返回 null，表示取不到有效值。
        :type FillError: list of FillError
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateFlowBlockchainEvidenceUrlRequest(AbstractModel):
    """CreateFlowBlockchainEvidenceUrl请求参数结构体

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
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _ExpiredOn: 链接/二维码的有效截止时间，格式为unix时间戳。最长不超过 2099年12月31日（4102415999）。
默认值为有效期为当前时间后7天。
        :type ExpiredOn: int
        """
        self._Operator = None
        self._FlowId = None
        self._Agent = None
        self._ExpiredOn = None

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

    @property
    def ExpiredOn(self):
        return self._ExpiredOn

    @ExpiredOn.setter
    def ExpiredOn(self, ExpiredOn):
        self._ExpiredOn = ExpiredOn


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowId = params.get("FlowId")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._ExpiredOn = params.get("ExpiredOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowBlockchainEvidenceUrlResponse(AbstractModel):
    """CreateFlowBlockchainEvidenceUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QrCode: 二维码图片下载链接，下载链接有效时间5分钟，请尽快下载保存。
        :type QrCode: str
        :param _Url: 查看短链，可直接点击短链查看证书。
        :type Url: str
        :param _ExpiredOn: 二维码和短链的过期时间戳，过期时间默认为生成链接后7天。
        :type ExpiredOn: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QrCode = None
        self._Url = None
        self._ExpiredOn = None
        self._RequestId = None

    @property
    def QrCode(self):
        return self._QrCode

    @QrCode.setter
    def QrCode(self, QrCode):
        self._QrCode = QrCode

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def ExpiredOn(self):
        return self._ExpiredOn

    @ExpiredOn.setter
    def ExpiredOn(self, ExpiredOn):
        self._ExpiredOn = ExpiredOn

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._QrCode = params.get("QrCode")
        self._Url = params.get("Url")
        self._ExpiredOn = params.get("ExpiredOn")
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
        :param _FlowName: 自定义的合同流程的名称，长度不能超过200个字符，只能由中文汉字、中文标点、英文字母、阿拉伯数字、空格、小括号、中括号、中划线、下划线以及（,）、（;）、（.）、(&)、（+）组成。

该名称还将用于合同签署完成后文件下载的默认文件名称。
        :type FlowName: str
        :param _Approvers: 合同流程的参与方列表，最多可支持50个参与方，可在列表中指定企业B端签署方和个人C端签署方的联系和认证方式等信息，具体定义可以参考开发者中心的ApproverInfo结构体。

如果合同流程是有序签署，Approvers列表中参与人的顺序就是默认的签署顺序，请确保列表中参与人的顺序符合实际签署顺序。
        :type Approvers: list of ApproverInfo
        :param _FileIds: 本合同流程需包含的PDF文件资源编号列表，通过[UploadFiles](https://qian.tencent.com/developers/companyApis/templatesAndFiles/UploadFiles)接口获取PDF文件资源编号。

注:  `目前，此接口仅支持单个文件发起。`
        :type FileIds: list of str
        :param _FlowDescription: 合同流程描述信息(可自定义此描述)，最大长度1000个字符。
        :type FlowDescription: str
        :param _FlowType: 合同流程的类别分类（可自定义名称，如销售合同/入职合同等），最大长度为200个字符，仅限中文、字母、数字和下划线组成。
如果用户已经在控制台创建了自定义合同类型，可以将这里的类型名称传入。 如果没有创建，我们会自动给发起方公司创建此自定义合同类型。
![image](https://qcloudimg.tencent-cloud.cn/raw/36582cea03ae6a2559894844942b5d5c.png)
        :type FlowType: str
        :param _Components: 模板或者合同中的填写控件列表，列表中可支持下列多种填写控件，控件的详细定义参考开发者中心的Component结构体
<ul><li> 单行文本控件      </li>
<li> 多行文本控件      </li>
<li> 勾选框控件        </li>
<li> 数字控件          </li>
<li> 图片控件          </li>
<li> 水印控件          </li>
<li> 动态表格等填写控件</li></ul>
        :type Components: list of Component
        :param _CcInfos: 合同流程的抄送人列表，最多可支持50个抄送人，抄送人可查看合同内容及签署进度，但无需参与合同签署。

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
<ul><li> **0** :(默认) 文件流 ,点开后下载预览的合同PDF文件 </li>
<li> **1** :H5链接 ,点开后在浏览器中展示合同的样子</li></ul>
注: `此参数在NeedPreview 为true时有效`

        :type PreviewType: int
        :param _Deadline: 合同流程的签署截止时间，格式为Unix标准时间戳（秒），如果未设置签署截止时间，则默认为合同流程创建后的365天时截止。
如果在签署截止时间前未完成签署，则合同状态会变为已过期，导致合同作废。
        :type Deadline: int
        :param _Unordered: 合同流程的签署顺序类型：
<ul><li> **false**：(默认)有序签署, 本合同多个参与人需要依次签署 </li>
<li> **true**：无序签署, 本合同多个参与人没有先后签署限制</li></ul>
        :type Unordered: bool
        :param _UserData: 调用方自定义的个性化字段(可自定义此名称)，并以base64方式编码，支持的最大数据大小为 20480长度。

在合同状态变更的回调信息等场景中，该字段的信息将原封不动地透传给贵方。回调的相关说明可参考开发者中心的[回调通知](https://qian.tencent.com/developers/company/callback_types_v2)模块。
        :type UserData: str
        :param _RemindedOn: 合同到期提醒时间，为Unix标准时间戳（秒）格式，支持的范围是从发起时间开始到后10年内。

到达提醒时间后，腾讯电子签会短信通知发起方企业合同提醒，可用于处理合同到期事务，如合同续签等事宜。
        :type RemindedOn: int
        :param _ApproverVerifyType: 指定个人签署方查看合同的校验方式
<ul><li>   **VerifyCheck**  :（默认）人脸识别,人脸识别后才能合同内容 </li>
<li>   **MobileCheck**  :  手机号验证, 用户手机号和参与方手机号（ApproverMobile）相同即可查看合同内容（当手写签名方式为OCR_ESIGN时，该校验方式无效，因为这种签名方式依赖实名认证）</li></ul>
        :type ApproverVerifyType: str
        :param _SignBeanTag: 签署方签署控件（印章/签名等）的生成方式：
<ul><li> **0**：在合同流程发起时，由发起人指定签署方的签署控件的位置和数量。</li>
<li> **1**：签署方在签署时自行添加签署控件，可以拖动位置和控制数量。</li></ul>
        :type SignBeanTag: int
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


![image](https://qcloudimg.tencent-cloud.cn/raw/628f0928cac15d2e3bfa6088f53f5998.png)


        :type CustomShowMap: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _AutoSignScene: 个人自动签名的使用场景包括以下, 个人自动签署(即ApproverType设置成个人自动签署时)业务此值必传：
<ul><li> **E_PRESCRIPTION_AUTO_SIGN**：电子处方单（医疗自动签）  </li><li> **OTHER** :  通用场景</li></ul>
注: `个人自动签名场景是白名单功能，使用前请与对接的客户经理联系沟通。`
        :type AutoSignScene: str
        :param _NeedSignReview: 发起方企业的签署人进行签署操作前，是否需要企业内部走审批流程，取值如下：
<ul><li> **false**：（默认）不需要审批，直接签署。</li>
<li> **true**：需要走审批流程。当到对应参与人签署时，会阻塞其签署操作，等待企业内部审批完成。</li></ul>
企业可以通过CreateFlowSignReview审批接口通知腾讯电子签平台企业内部审批结果
<ul><li> 如果企业通知腾讯电子签平台审核通过，签署方可继续签署动作。</li>
<li> 如果企业通知腾讯电子签平台审核未通过，平台将继续阻塞签署方的签署动作，直到企业通知平台审核通过。</li></ul>
注：`此功能可用于与企业内部的审批流程进行关联，支持手动、静默签署合同`
        :type NeedSignReview: bool
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
        self._Unordered = None
        self._UserData = None
        self._RemindedOn = None
        self._ApproverVerifyType = None
        self._SignBeanTag = None
        self._CustomShowMap = None
        self._Agent = None
        self._AutoSignScene = None
        self._NeedSignReview = None

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
    def Unordered(self):
        return self._Unordered

    @Unordered.setter
    def Unordered(self, Unordered):
        self._Unordered = Unordered

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def RemindedOn(self):
        return self._RemindedOn

    @RemindedOn.setter
    def RemindedOn(self, RemindedOn):
        self._RemindedOn = RemindedOn

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
    def CustomShowMap(self):
        return self._CustomShowMap

    @CustomShowMap.setter
    def CustomShowMap(self, CustomShowMap):
        self._CustomShowMap = CustomShowMap

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

    @property
    def NeedSignReview(self):
        return self._NeedSignReview

    @NeedSignReview.setter
    def NeedSignReview(self, NeedSignReview):
        self._NeedSignReview = NeedSignReview


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
        self._Unordered = params.get("Unordered")
        self._UserData = params.get("UserData")
        self._RemindedOn = params.get("RemindedOn")
        self._ApproverVerifyType = params.get("ApproverVerifyType")
        self._SignBeanTag = params.get("SignBeanTag")
        self._CustomShowMap = params.get("CustomShowMap")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._AutoSignScene = params.get("AutoSignScene")
        self._NeedSignReview = params.get("NeedSignReview")
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

注: 如果是预览模式(即NeedPreview设置为true)时, 此处不会有值返回。

[点击查看FlowId在控制台中的位置](https://qcloudimg.tencent-cloud.cn/raw/0a83015166cfe1cb043d14f9ec4bd75e.png)
        :type FlowId: str
        :param _PreviewUrl: 合同预览链接URL。

注：如果是预览模式(即NeedPreview设置为true)时, 才会有此预览链接URL
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewUrl: str
        :param _Approvers: 签署方信息，如角色ID、角色名称等
注意：此字段可能返回 null，表示取不到有效值。
        :type Approvers: list of ApproverItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._PreviewUrl = None
        self._Approvers = None
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
        self._PreviewUrl = params.get("PreviewUrl")
        if params.get("Approvers") is not None:
            self._Approvers = []
            for item in params.get("Approvers"):
                obj = ApproverItem()
                obj._deserialize(item)
                self._Approvers.append(obj)
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
        :param _ReportType: 指定申请的报告类型，可选类型如下：
<ul><li> **0** :合同签署报告（默认）</li>
<li> **1** :公证处核验报告</li></ul>
        :type ReportType: int
        """
        self._Operator = None
        self._FlowId = None
        self._Agent = None
        self._ReportType = None

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

    @property
    def ReportType(self):
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowId = params.get("FlowId")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._ReportType = params.get("ReportType")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
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
        :param _Approvers: 合同组签署方信息。
        :type Approvers: list of FlowGroupApprovers
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowGroupId = None
        self._FlowIds = None
        self._Approvers = None
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
        self._FlowGroupId = params.get("FlowGroupId")
        self._FlowIds = params.get("FlowIds")
        if params.get("Approvers") is not None:
            self._Approvers = []
            for item in params.get("Approvers"):
                obj = FlowGroupApprovers()
                obj._deserialize(item)
                self._Approvers.append(obj)
        self._RequestId = params.get("RequestId")


class CreateFlowGroupByTemplatesRequest(AbstractModel):
    """CreateFlowGroupByTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
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
        :param _Approvers: 合同组签署人信息。
        :type Approvers: list of FlowGroupApprovers
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowGroupId = None
        self._FlowIds = None
        self._Approvers = None
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
        self._FlowGroupId = params.get("FlowGroupId")
        self._FlowIds = params.get("FlowIds")
        if params.get("Approvers") is not None:
            self._Approvers = []
            for item in params.get("Approvers"):
                obj = FlowGroupApprovers()
                obj._deserialize(item)
                self._Approvers.append(obj)
        self._RequestId = params.get("RequestId")


class CreateFlowGroupSignReviewRequest(AbstractModel):
    """CreateFlowGroupSignReview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowGroupId: 合同(流程)组的合同组Id，为32位字符串，通过接口[通过多文件创建合同组签署流程](https://qian.tencent.com/developers/companyApis/startFlows/CreateFlowGroupByFiles) 或[通过多模板创建合同组签署流程](https://qian.tencent.com/developers/companyApis/startFlows/CreateFlowGroupByTemplates)创建合同组签署流程时返回。
        :type FlowGroupId: str
        :param _ReviewType: 提交的审核结果，审核结果有下面三种情况
<ul><li><b>PASS</b>: 审核通过，合同流程可以继续执行签署等操作</li>
<li><b>REJECT</b>: 审核拒绝，合同流程不会变动</li>
<li><b>SIGN_REJECT</b>:拒签，合同流程直接结束，合同状态变为**合同拒签**</li></ul>
        :type ReviewType: str
        :param _ApproverInfo: 需要进行签署审核的签署人的个人信息或企业信息，签署方的匹配方式按照以下规则:

个人：二选一（选择其中任意信息组合即可）
<ul><li>姓名+证件类型+证件号</li>
<li>姓名+手机号</li></ul>

企业：二选一  （选择其中任意信息组合即可）
<ul><li>企业名+姓名+证件类型+证件号</li>
<li>企业名+姓名+手机号</li></ul>
        :type ApproverInfo: :class:`tencentcloud.ess.v20201111.models.NeedReviewApproverInfo`
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _ReviewMessage: 审核不通过的原因，该字段的字符串长度不超过200个字符。

注：`当审核类型（ReviewType）为审核拒绝（REJECT）或拒签（SIGN_REJECT）时，审核结果原因字段必须填写`

        :type ReviewMessage: str
        """
        self._Operator = None
        self._FlowGroupId = None
        self._ReviewType = None
        self._ApproverInfo = None
        self._Agent = None
        self._ReviewMessage = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def FlowGroupId(self):
        return self._FlowGroupId

    @FlowGroupId.setter
    def FlowGroupId(self, FlowGroupId):
        self._FlowGroupId = FlowGroupId

    @property
    def ReviewType(self):
        return self._ReviewType

    @ReviewType.setter
    def ReviewType(self, ReviewType):
        self._ReviewType = ReviewType

    @property
    def ApproverInfo(self):
        return self._ApproverInfo

    @ApproverInfo.setter
    def ApproverInfo(self, ApproverInfo):
        self._ApproverInfo = ApproverInfo

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def ReviewMessage(self):
        return self._ReviewMessage

    @ReviewMessage.setter
    def ReviewMessage(self, ReviewMessage):
        self._ReviewMessage = ReviewMessage


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowGroupId = params.get("FlowGroupId")
        self._ReviewType = params.get("ReviewType")
        if params.get("ApproverInfo") is not None:
            self._ApproverInfo = NeedReviewApproverInfo()
            self._ApproverInfo._deserialize(params.get("ApproverInfo"))
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._ReviewMessage = params.get("ReviewMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowGroupSignReviewResponse(AbstractModel):
    """CreateFlowGroupSignReview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateFlowOption(AbstractModel):
    """创建合同个性化参数

    """

    def __init__(self):
        r"""
        :param _CanEditFlow: 是否允许修改发起合同时确认弹窗的合同信息（合同名称、合同类型、签署截止时间），若不允许编辑，则表单字段将被禁止输入。
<br/>true：允许编辑<br/>false：不允许编辑（默认值）<br/>
        :type CanEditFlow: bool
        :param _CanEditFormField: 是否允许编辑模板控件
<br/>true:允许编辑模板控件信息
<br/>false:不允许编辑模板控件信息（默认值）
<br/>
        :type CanEditFormField: bool
        :param _HideShowFlowName: 发起页面隐藏合同名称展示
<br/>true:发起页面隐藏合同名称展示
<br/>false:发起页面不隐藏合同名称展示（默认值）
<br/>
        :type HideShowFlowName: bool
        :param _HideShowFlowType: 发起页面隐藏合同类型展示
<br/>true:发起页面隐藏合同类型展示
<br/>false:发起页面不隐藏合同类型展示（默认值）
<br/>

        :type HideShowFlowType: bool
        :param _HideShowDeadline: 发起页面隐藏合同截止日期展示
<br/>true:发起页面隐藏合同截止日期展示
<br/>false:发起页面不隐藏合同截止日期展示（默认值）
<br/>
        :type HideShowDeadline: bool
        :param _CanSkipAddApprover: 发起页面允许跳过添加签署人环节
<br/>true:发起页面允许跳过添加签署人环节
<br/>false:发起页面不允许跳过添加签署人环节（默认值）
<br/>

        :type CanSkipAddApprover: bool
        :param _SkipUploadFile: 文件发起页面跳过文件上传步骤
<br/>true:文件发起页面跳过文件上传步骤
<br/>false:文件发起页面不跳过文件上传步骤（默认值）
<br/>
        :type SkipUploadFile: bool
        :param _ForbidEditFillComponent: 禁止编辑填写控件
<br/>true:禁止编辑填写控件
<br/>false:允许编辑填写控件（默认值）
<br/>
        :type ForbidEditFillComponent: bool
        :param _CustomCreateFlowDescription: 定制化发起合同弹窗的描述信息，描述信息最长500字符

        :type CustomCreateFlowDescription: str
        :param _ForbidAddApprover:   禁止添加签署方，若为true则在发起流程的可嵌入页面隐藏“添加签署人按钮”

        :type ForbidAddApprover: bool
        :param _ForbidEditFlowProperties:   禁止设置设置签署流程属性 (顺序、合同签署认证方式等)，若为true则在发起流程的可嵌入页面隐藏签署流程设置面板

        :type ForbidEditFlowProperties: bool
        :param _HideComponentTypes: 在发起流程的可嵌入页面要隐藏的控件列表，和 ShowComponentTypes 参数 只能二选一使用，具体的控件类型如下
<ul><li>SIGN_SIGNATURE : 个人签名/印章</li>
<li>SIGN_SEAL : 企业印章</li>
<li>SIGN_PAGING_SEAL : 骑缝章</li>
<li>SIGN_LEGAL_PERSON_SEAL : 法定代表人章</li>
<li>SIGN_APPROVE : 签批</li>
<li>SIGN_OPINION : 签署意见</li>
<li>BUSI-FULL-NAME  : 企业全称</li>
<li>BUSI-CREDIT-CODE : 统一社会信用代码</li>
<li>BUSI-LEGAL-NAME : 法人/经营者姓名</li>
<li>PERSONAL-NAME : 签署人姓名</li>
<li>PERSONAL-MOBILE : 签署人手机号</li>
<li>PERSONAL-IDCARD-TYPE : 签署人证件类型</li>
<li>PERSONAL-IDCARD : 签署人证件号</li>
<li>TEXT : 单行文本</li>
<li>MULTI_LINE_TEXT : 多行文本</li>
<li>CHECK_BOX : 勾选框</li>
<li>SELECTOR : 选择器</li>
<li>DIGIT : 数字</li>
<li>DATE : 日期</li>
<li>FILL_IMAGE : 图片</li>
<li>ATTACHMENT : 附件</li>
<li>EMAIL : 邮箱</li>
<li>LOCATION : 地址</li>
<li>EDUCATION : 学历</li>
<li>GENDER : 性别</li>
<li>DISTRICT : 省市区</li></ul>
        :type HideComponentTypes: list of str
        :param _ShowComponentTypes: 在发起流程的可嵌入页面要显示的控件列表，和 HideComponentTypes 参数 只能二选一使用，具体的控件类型如下
<ul><li>SIGN_SIGNATURE : 个人签名/印章</li>
<li>SIGN_SEAL : 企业印章</li>
<li>SIGN_PAGING_SEAL : 骑缝章</li>
<li>SIGN_LEGAL_PERSON_SEAL : 法定代表人章</li>
<li>SIGN_APPROVE : 签批</li>
<li>SIGN_OPINION : 签署意见</li>
<li>BUSI-FULL-NAME  : 企业全称</li>
<li>BUSI-CREDIT-CODE : 统一社会信用代码</li>
<li>BUSI-LEGAL-NAME : 法人/经营者姓名</li>
<li>PERSONAL-NAME : 签署人姓名</li>
<li>PERSONAL-MOBILE : 签署人手机号</li>
<li>PERSONAL-IDCARD-TYPE : 签署人证件类型</li>
<li>PERSONAL-IDCARD : 签署人证件号</li>
<li>TEXT : 单行文本</li>
<li>MULTI_LINE_TEXT : 多行文本</li>
<li>CHECK_BOX : 勾选框</li>
<li>SELECTOR : 选择器</li>
<li>DIGIT : 数字</li>
<li>DATE : 日期</li>
<li>FILL_IMAGE : 图片</li>
<li>ATTACHMENT : 附件</li>
<li>EMAIL : 邮箱</li>
<li>LOCATION : 地址</li>
<li>EDUCATION : 学历</li>
<li>GENDER : 性别</li>
<li>DISTRICT : 省市区</li></ul>
        :type ShowComponentTypes: list of str
        :param _ResultPageConfig: 发起流程的可嵌入页面结果页配置
        :type ResultPageConfig: list of CreateResultPageConfig
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
        self._ForbidAddApprover = None
        self._ForbidEditFlowProperties = None
        self._HideComponentTypes = None
        self._ShowComponentTypes = None
        self._ResultPageConfig = None

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

    @property
    def ForbidAddApprover(self):
        return self._ForbidAddApprover

    @ForbidAddApprover.setter
    def ForbidAddApprover(self, ForbidAddApprover):
        self._ForbidAddApprover = ForbidAddApprover

    @property
    def ForbidEditFlowProperties(self):
        return self._ForbidEditFlowProperties

    @ForbidEditFlowProperties.setter
    def ForbidEditFlowProperties(self, ForbidEditFlowProperties):
        self._ForbidEditFlowProperties = ForbidEditFlowProperties

    @property
    def HideComponentTypes(self):
        return self._HideComponentTypes

    @HideComponentTypes.setter
    def HideComponentTypes(self, HideComponentTypes):
        self._HideComponentTypes = HideComponentTypes

    @property
    def ShowComponentTypes(self):
        return self._ShowComponentTypes

    @ShowComponentTypes.setter
    def ShowComponentTypes(self, ShowComponentTypes):
        self._ShowComponentTypes = ShowComponentTypes

    @property
    def ResultPageConfig(self):
        return self._ResultPageConfig

    @ResultPageConfig.setter
    def ResultPageConfig(self, ResultPageConfig):
        self._ResultPageConfig = ResultPageConfig


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
        self._ForbidAddApprover = params.get("ForbidAddApprover")
        self._ForbidEditFlowProperties = params.get("ForbidEditFlowProperties")
        self._HideComponentTypes = params.get("HideComponentTypes")
        self._ShowComponentTypes = params.get("ShowComponentTypes")
        if params.get("ResultPageConfig") is not None:
            self._ResultPageConfig = []
            for item in params.get("ResultPageConfig"):
                obj = CreateResultPageConfig()
                obj._deserialize(item)
                self._ResultPageConfig.append(obj)
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _FlowName: 自定义的合同流程的名称，长度不能超过200个字符，只能由中文汉字、中文标点、英文字母、阿拉伯数字、空格、小括号、中括号、中划线、下划线以及（,）、（;）、（.）、(&)、（+）组成。

该名称还将用于合同签署完成后文件下载的默认文件名称。
        :type FlowName: str
        :param _Approvers: 合同流程的参与方列表，最多可支持50个参与方，可在列表中指定企业B端签署方和个人C端签署方的联系和认证方式等信息，具体定义可以参考开发者中心的ApproverInfo结构体。

注:  
<font color="red" > <b> 在发起流程时，需要保证 approver 中的顺序与模板定义顺序一致，否则会发起失败。
例如，如果模板中定义的第一个参与人是个人用户，第二个参与人是企业员工，则在 approver 中传参时，第一个也必须是个人用户，第二个参与人必须是企业员工。</b></font>

[点击查看模板参与人顺序定义位置](https://qcloudimg.tencent-cloud.cn/raw/d14457b48cc66b29262ccb9d7b3ed556.png)
        :type Approvers: list of FlowCreateApprover
        :param _FlowDescription: 合同流程描述信息(可自定义此描述)，最大长度1000个字符。
        :type FlowDescription: str
        :param _FlowType: 合同流程的类别分类（可自定义名称，如销售合同/入职合同等），最大长度为200个字符，仅限中文、字母、数字和下划线组成。
此合同类型需要跟模板配置的合同类型保持一致。
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
        :param _CustomShowMap: 您可以自定义**腾讯电子签小程序合同列表页**展示的合同内容模板，模板中支持以下变量：
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

![image](https://qcloudimg.tencent-cloud.cn/raw/628f0928cac15d2e3bfa6088f53f5998.png)


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
        :type CcInfos: list of CcInfo
        :param _AutoSignScene: 个人自动签名的使用场景包括以下, 个人自动签署(即ApproverType设置成个人自动签署时)业务此值必传：
<ul><li> **E_PRESCRIPTION_AUTO_SIGN**：电子处方单（医疗自动签）  </li><li> **OTHER** :  通用场景</li></ul>
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
此返回的合同流程ID，需再次调用<a href="https://qian.tencent.com/developers/companyApis/startFlows/CreateDocument" target="_blank">创建电子文档</a>和<a href="https://qian.tencent.com/developers/companyApis/startFlows/StartFlow" target="_blank">发起签署流程</a>接口将合同开始后，合同才能进入签署环节，[点击查看FlowId在控制台中的位置（只在进入签署环节后有效）](https://qcloudimg.tencent-cloud.cn/raw/0a83015166cfe1cb043d14f9ec4bd75e.png)


        :type FlowId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowId: 合同流程ID，为32位字符串。
<ul><li>建议开发者妥善保存此流程ID，以便于顺利进行后续操作。</li>
<li>可登录腾讯电子签控制台，在 "合同"->"合同中心" 中查看某个合同的FlowId(在页面中展示为合同ID)。</li></ul>
        :type FlowId: str
        :param _ReviewType: 企业内部审核结果
<ul><li>PASS: 审核通过</li>
<li>REJECT: 审核拒绝</li>
<li>SIGN_REJECT:拒签(流程结束)</li></ul>
        :type ReviewType: str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _RecipientId: 审核节点的签署人标志，用于指定当前审核的签署方
<ul><li>**如果签署审核节点是个人， 此参数必填**。</li></ul>
        :type RecipientId: str
        :param _OperateType: 操作类型：（接口通过该字段区分不同的操作类型）

<ul><li>SignReview: 签署审核（默认）</li>
<li>CreateReview: 创建审核</li></ul>

如果审核节点是个人，则操作类型只能为SignReview。
        :type OperateType: str
        :param _ReviewMessage: 审核结果原因
<ul><li>字符串长度不超过200</li>
<li>当ReviewType 是拒绝（REJECT） 时此字段必填。</li>
<li>当ReviewType 是拒绝（SIGN_REJECT） 时此字段必填。</li></ul>


        :type ReviewMessage: str
        """
        self._Operator = None
        self._FlowId = None
        self._ReviewType = None
        self._Agent = None
        self._RecipientId = None
        self._OperateType = None
        self._ReviewMessage = None

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

    @property
    def ReviewMessage(self):
        return self._ReviewMessage

    @ReviewMessage.setter
    def ReviewMessage(self, ReviewMessage):
        self._ReviewMessage = ReviewMessage


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowId = params.get("FlowId")
        self._ReviewType = params.get("ReviewType")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._RecipientId = params.get("RecipientId")
        self._OperateType = params.get("OperateType")
        self._ReviewMessage = params.get("ReviewMessage")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _FlowApproverInfos: 流程签署人列表，其中结构体的ApproverName，ApproverMobile和ApproverType必传，企业签署人则需传OrganizationName，其他可不传。

注:
`1. 签署人只能有手写签名、时间类型、印章类型的签署控件和内容填写控件，其他类型的签署控件暂时未支持。`
`2. 生成发起方预览链接时，该字段（FlowApproverInfos）传空或者不传`
        :type FlowApproverInfos: list of FlowCreateApprover
        :param _Organization: 机构信息，暂未开放
        :type Organization: :class:`tencentcloud.ess.v20201111.models.OrganizationInfo`
        :param _JumpUrl: 签署完之后的H5页面的跳转链接，最大长度1000个字符。链接类型请参考 <a href="https://qian.tencent.com/developers/company/openqianh5" target="_blank">跳转电子签H5</a>

        :type JumpUrl: str
        :param _UrlType: 链接类型，支持指定以下类型
<ul><li>0 : 签署链接 (默认值)</li>
<li>1 : 预览链接</li></ul>
注:
`1. 当指定链接类型为1时，链接为预览链接，打开链接无法签署仅支持预览以及查看当前合同状态。`
`2. 如需生成发起方预览链接，则签署方信息传空，即FlowApproverInfos传空或者不传。`
        :type UrlType: int
        """
        self._FlowId = None
        self._Operator = None
        self._Agent = None
        self._FlowApproverInfos = None
        self._Organization = None
        self._JumpUrl = None
        self._UrlType = None

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

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def FlowApproverInfos(self):
        return self._FlowApproverInfos

    @FlowApproverInfos.setter
    def FlowApproverInfos(self, FlowApproverInfos):
        self._FlowApproverInfos = FlowApproverInfos

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

    @property
    def UrlType(self):
        return self._UrlType

    @UrlType.setter
    def UrlType(self, UrlType):
        self._UrlType = UrlType


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("FlowApproverInfos") is not None:
            self._FlowApproverInfos = []
            for item in params.get("FlowApproverInfos"):
                obj = FlowCreateApprover()
                obj._deserialize(item)
                self._FlowApproverInfos.append(obj)
        if params.get("Organization") is not None:
            self._Organization = OrganizationInfo()
            self._Organization._deserialize(params.get("Organization"))
        self._JumpUrl = params.get("JumpUrl")
        self._UrlType = params.get("UrlType")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _DeptName: 部门名称，最大长度为50个字符。
        :type DeptName: str
        :param _Agent: 代理企业和员工的信息。 在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _ParentDeptId: 电子签父部门ID。
注：`如果同时指定了ParentDeptId与ParentDeptOpenId参数，系统将优先使用ParentDeptId。当二者都未指定时，创建的新部门将自动填充至根节点部门下。`
        :type ParentDeptId: str
        :param _ParentDeptOpenId: 第三方平台中父部门ID。
注：`如果同时指定了ParentDeptId与ParentDeptOpenId参数，系统将优先使用ParentDeptId。当二者都未指定时，创建的新部门将自动填充至根节点部门下。`
        :type ParentDeptOpenId: str
        :param _DeptOpenId: 客户系统部门ID，最大长度为64个字符。
        :type DeptOpenId: str
        :param _OrderNo: 排序号，支持设置的数值范围为1~30000。同一父部门下，排序号越大，部门顺序越靠前。
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
        :param _DeptId: 电子签部门ID。建议开发者保存此部门ID，方便后续查询或修改部门信息。
        :type DeptId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Operator: 执行本接口操作的员工信息。使用此接口时，必须填写userId。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Employees: 待创建员工的信息最多不超过20个。

**1. 在创建企业微信员工的场景下** :  只需传入下面的参数，其他信息不支持设置。
<table> <thead> <tr> <th>参数</th> <th>是否必填</th> <th>含义</th> </tr> </thead> <tbody> <tr> <td>WeworkOpenId</td> <td>是</td> <td>企业微信用户账号ID</td> </tr> </tbody> </table>

**2. 在其他场景下** :   只需传入下面的参数，其他信息不支持设置。
<table> <thead> <tr> <th>参数</th> <th>是否必填</th> <th>含义</th> </tr> </thead> <tbody> <tr> <td>DisplayName</td> <td>是</td> <td>用户的真实名字</td> </tr> <tr> <td>Mobile</td> <td>是</td> <td>用户手机号码</td> </tr> <tr> <td>OpenId</td> <td>否</td> <td>用户的自定义ID</td> </tr> <tr> <td>Email</td> <td>否</td> <td>用户的邮箱</td> </tr> <tr> <td>Department.DepartmentId</td> <td>否</td> <td>用户加入后的部门ID</td> </tr> </tbody> </table>


注: `每个手机号每天最多使用3次`
        :type Employees: list of Staff
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _InvitationNotifyType: 员工邀请方式
可通过以下途径进行设置：
<ul><li>**SMS（默认）**：邀请将通过短信或企业微信消息发送。若场景非企业微信，则采用企业微信消息；其他情境下则使用短信通知。短信内含链接，点击后将进入微信小程序进行认证并加入企业的流程。</li><li>**H5**：将生成H5链接，用户点击链接后可进入H5页面进行认证并加入企业的流程。</li><li>**NONE**：系统会根据Endpoint生成签署链接，业务方需获取链接并通知客户。</li></ul>
        :type InvitationNotifyType: str
        :param _JumpUrl: 回跳地址，为认证成功后页面进行回跳的URL，请确保回跳地址的可用性。

注：`只有在员工邀请方式（InvitationNotifyType参数）为H5场景下才生效， 其他方式下设置无效。`

        :type JumpUrl: str
        :param _Endpoint: 要跳转的链接类型<ul><li> **HTTP**：跳转电子签小程序的http_url, 短信通知或者H5跳转适合此类型  ，此时返回长链 (默认类型)</li><li>**HTTP_SHORT_URL**：跳转电子签小程序的http_url, 短信通知或者H5跳转适合此类型，此时返回短链</li><li>**APP**： 第三方APP或小程序跳转电子签小程序的path,  APP或者小程序跳转适合此类型</li><li>**H5**： 第三方移动端浏览器进行嵌入，不支持小程序嵌入，过期时间一个月</li></ul>注意：InvitationNotifyType 和 Endpoint 的关系图<table><tbody><tr><td>通知类型（InvitationNotifyType）</td><td>Endpoint</td></tr><tr><td>SMS（默认）</td><td>不需要传递，会将 Endpoint 默认设置为HTTP_SHORT_URL</td></tr><tr><td>H5</td><td>不需要传递，会将 Endpoint 默认设置为 H5</td></tr><tr><td>NONE</td><td>所有 Endpoint 都支持（HTTP_URL/HTTP_SHORT_URL/H5/APP）默认为HTTP_SHORT_URL</td></tr></tbody></table>
        :type Endpoint: str
        """
        self._Operator = None
        self._Employees = None
        self._Agent = None
        self._InvitationNotifyType = None
        self._JumpUrl = None
        self._Endpoint = None

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

    @property
    def InvitationNotifyType(self):
        return self._InvitationNotifyType

    @InvitationNotifyType.setter
    def InvitationNotifyType(self, InvitationNotifyType):
        self._InvitationNotifyType = InvitationNotifyType

    @property
    def JumpUrl(self):
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint


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
        self._InvitationNotifyType = params.get("InvitationNotifyType")
        self._JumpUrl = params.get("JumpUrl")
        self._Endpoint = params.get("Endpoint")
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
        :param _CreateEmployeeResult: 创建员工的结果。包含创建成功的数据与创建失败数据。
        :type CreateEmployeeResult: :class:`tencentcloud.ess.v20201111.models.CreateStaffResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateIntegrationSubOrganizationActiveRecordRequest(AbstractModel):
    """CreateIntegrationSubOrganizationActiveRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。使用此接口时，必须填写userId。 支持填入集团子公司经办人 userId 代发合同。  注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _SubOrganizationIds: 待激活成员企业ID集合
        :type SubOrganizationIds: list of str
        """
        self._Operator = None
        self._SubOrganizationIds = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def SubOrganizationIds(self):
        return self._SubOrganizationIds

    @SubOrganizationIds.setter
    def SubOrganizationIds(self, SubOrganizationIds):
        self._SubOrganizationIds = SubOrganizationIds


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._SubOrganizationIds = params.get("SubOrganizationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIntegrationSubOrganizationActiveRecordResponse(AbstractModel):
    """CreateIntegrationSubOrganizationActiveRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailedSubOrganizationIds: 激活失败的成员企业ID集合
        :type FailedSubOrganizationIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailedSubOrganizationIds = None
        self._RequestId = None

    @property
    def FailedSubOrganizationIds(self):
        return self._FailedSubOrganizationIds

    @FailedSubOrganizationIds.setter
    def FailedSubOrganizationIds(self, FailedSubOrganizationIds):
        self._FailedSubOrganizationIds = FailedSubOrganizationIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailedSubOrganizationIds = params.get("FailedSubOrganizationIds")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateLegalSealQrCodeRequest(AbstractModel):
    """CreateLegalSealQrCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Organization: 机构信息，暂未开放
        :type Organization: :class:`tencentcloud.ess.v20201111.models.OrganizationInfo`
        """
        self._Operator = None
        self._Agent = None
        self._Organization = None

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
        


class CreateLegalSealQrCodeResponse(AbstractModel):
    """CreateLegalSealQrCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QrcodeBase64: 二维码图片base64值，二维码有效期7天（604800秒）

二维码图片的样式如下图：
![image](https://qcloudimg.tencent-cloud.cn/raw/7ec2478761158a35a9c623882839a5df.png)
        :type QrcodeBase64: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QrcodeBase64 = None
        self._RequestId = None

    @property
    def QrcodeBase64(self):
        return self._QrcodeBase64

    @QrcodeBase64.setter
    def QrcodeBase64(self, QrcodeBase64):
        self._QrcodeBase64 = QrcodeBase64

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._QrcodeBase64 = params.get("QrcodeBase64")
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
        :param _ApproverComponentLimitTypes: 指定签署方在使用个人印章签署控件（SIGN_SIGNATURE） 时可使用的签署方式：自由书写、正楷临摹、系统签名、个人印章。
        :type ApproverComponentLimitTypes: list of ApproverComponentLimitType
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
        self._ApproverComponentLimitTypes = None

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

    @property
    def ApproverComponentLimitTypes(self):
        return self._ApproverComponentLimitTypes

    @ApproverComponentLimitTypes.setter
    def ApproverComponentLimitTypes(self, ApproverComponentLimitTypes):
        self._ApproverComponentLimitTypes = ApproverComponentLimitTypes


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
        


class CreateMultiFlowSignQRCodeResponse(AbstractModel):
    """CreateMultiFlowSignQRCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QrCode: 一码多签签署码的基本信息，用户可扫描该二维码进行签署操作。
        :type QrCode: :class:`tencentcloud.ess.v20201111.models.SignQrCode`
        :param _SignUrls: 一码多签签署码的链接信息，适用于客户系统整合二维码功能。通过链接，用户可直接访问电子签名小程序并签署合同。
        :type SignUrls: :class:`tencentcloud.ess.v20201111.models.SignUrl`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateOrganizationAuthUrlRequest(AbstractModel):
    """CreateOrganizationAuthUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _AuthorizationTypes: 指定授权方式 支持多选:
1-上传授权书方式
2- 法人授权方式
3- 法人身份认证方式
        :type AuthorizationTypes: list of int non-negative
        :param _OrganizationName: 企业名称
EndPointType=“H5”或者"SHORT_H5"时，该参数必填

        :type OrganizationName: str
        :param _UniformSocialCreditCode: 企业统一社会信用代码
        :type UniformSocialCreditCode: str
        :param _LegalName: 法人姓名
        :type LegalName: str
        :param _AutoJumpUrl: 认证完成跳转链接
        :type AutoJumpUrl: str
        :param _OrganizationAddress: 营业执照企业地址
示例：xx省xx市xx县/区xx街道
        :type OrganizationAddress: str
        :param _AdminName: 认证人姓名
        :type AdminName: str
        :param _AdminMobile: 认证人手机号
        :type AdminMobile: str
        :param _AdminIdCardNumber: 认证人身份证号
        :type AdminIdCardNumber: str
        :param _AdminIdCardType: 认证人证件类型
支持以下类型
<ul><li>ID_CARD : 中国大陆居民身份证  (默认值)</li>
<li>HONGKONG_AND_MACAO : 港澳居民来往内地通行证</li>
<li>HONGKONG_MACAO_AND_TAIWAN : 港澳台居民居住证(格式同居民身份证)</li></ul>

        :type AdminIdCardType: str
        :param _UniformSocialCreditCodeSame: 营业执照的社会信用代码保持一致
false 关闭-默认
true 开启
        :type UniformSocialCreditCodeSame: bool
        :param _LegalNameSame: 法人姓名保持一致
false 关闭-默认
true 开启
        :type LegalNameSame: bool
        :param _AdminNameSame: 认证人姓名一致
false 关闭-默认
true 开启
注意：
开启后在认证过程前会校验拦截
        :type AdminNameSame: bool
        :param _AdminIdCardNumberSame: 认证人居民身份证件号一致
false 关闭-默认
true 开启
注意：
开启后在认证过程前会校验拦截
        :type AdminIdCardNumberSame: bool
        :param _AdminMobileSame: 认证人手机号一致
false 关闭-默认
true 开启
注意：
开启后在认证过程前会校验拦截
        :type AdminMobileSame: bool
        :param _OrganizationNameSame: 企业名称保持一致
false 关闭-默认
true 开启
        :type OrganizationNameSame: bool
        :param _BusinessLicense: 营业执照正面照(PNG或JPG) base64格式, 大小不超过5M
        :type BusinessLicense: str
        :param _Endpoint: 跳转链接类型：
"PC"-PC端认证链接 
"APP"-全屏或半屏跳转小程序链接
“H5”-H5页面认证链接 "SHORT_H5"- H5认证短链
"SHORT_URL"- 跳转小程序短链	
        :type Endpoint: str
        """
        self._Operator = None
        self._AuthorizationTypes = None
        self._OrganizationName = None
        self._UniformSocialCreditCode = None
        self._LegalName = None
        self._AutoJumpUrl = None
        self._OrganizationAddress = None
        self._AdminName = None
        self._AdminMobile = None
        self._AdminIdCardNumber = None
        self._AdminIdCardType = None
        self._UniformSocialCreditCodeSame = None
        self._LegalNameSame = None
        self._AdminNameSame = None
        self._AdminIdCardNumberSame = None
        self._AdminMobileSame = None
        self._OrganizationNameSame = None
        self._BusinessLicense = None
        self._Endpoint = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def AuthorizationTypes(self):
        return self._AuthorizationTypes

    @AuthorizationTypes.setter
    def AuthorizationTypes(self, AuthorizationTypes):
        self._AuthorizationTypes = AuthorizationTypes

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def UniformSocialCreditCode(self):
        return self._UniformSocialCreditCode

    @UniformSocialCreditCode.setter
    def UniformSocialCreditCode(self, UniformSocialCreditCode):
        self._UniformSocialCreditCode = UniformSocialCreditCode

    @property
    def LegalName(self):
        return self._LegalName

    @LegalName.setter
    def LegalName(self, LegalName):
        self._LegalName = LegalName

    @property
    def AutoJumpUrl(self):
        return self._AutoJumpUrl

    @AutoJumpUrl.setter
    def AutoJumpUrl(self, AutoJumpUrl):
        self._AutoJumpUrl = AutoJumpUrl

    @property
    def OrganizationAddress(self):
        return self._OrganizationAddress

    @OrganizationAddress.setter
    def OrganizationAddress(self, OrganizationAddress):
        self._OrganizationAddress = OrganizationAddress

    @property
    def AdminName(self):
        return self._AdminName

    @AdminName.setter
    def AdminName(self, AdminName):
        self._AdminName = AdminName

    @property
    def AdminMobile(self):
        return self._AdminMobile

    @AdminMobile.setter
    def AdminMobile(self, AdminMobile):
        self._AdminMobile = AdminMobile

    @property
    def AdminIdCardNumber(self):
        return self._AdminIdCardNumber

    @AdminIdCardNumber.setter
    def AdminIdCardNumber(self, AdminIdCardNumber):
        self._AdminIdCardNumber = AdminIdCardNumber

    @property
    def AdminIdCardType(self):
        return self._AdminIdCardType

    @AdminIdCardType.setter
    def AdminIdCardType(self, AdminIdCardType):
        self._AdminIdCardType = AdminIdCardType

    @property
    def UniformSocialCreditCodeSame(self):
        return self._UniformSocialCreditCodeSame

    @UniformSocialCreditCodeSame.setter
    def UniformSocialCreditCodeSame(self, UniformSocialCreditCodeSame):
        self._UniformSocialCreditCodeSame = UniformSocialCreditCodeSame

    @property
    def LegalNameSame(self):
        return self._LegalNameSame

    @LegalNameSame.setter
    def LegalNameSame(self, LegalNameSame):
        self._LegalNameSame = LegalNameSame

    @property
    def AdminNameSame(self):
        return self._AdminNameSame

    @AdminNameSame.setter
    def AdminNameSame(self, AdminNameSame):
        self._AdminNameSame = AdminNameSame

    @property
    def AdminIdCardNumberSame(self):
        return self._AdminIdCardNumberSame

    @AdminIdCardNumberSame.setter
    def AdminIdCardNumberSame(self, AdminIdCardNumberSame):
        self._AdminIdCardNumberSame = AdminIdCardNumberSame

    @property
    def AdminMobileSame(self):
        return self._AdminMobileSame

    @AdminMobileSame.setter
    def AdminMobileSame(self, AdminMobileSame):
        self._AdminMobileSame = AdminMobileSame

    @property
    def OrganizationNameSame(self):
        return self._OrganizationNameSame

    @OrganizationNameSame.setter
    def OrganizationNameSame(self, OrganizationNameSame):
        self._OrganizationNameSame = OrganizationNameSame

    @property
    def BusinessLicense(self):
        return self._BusinessLicense

    @BusinessLicense.setter
    def BusinessLicense(self, BusinessLicense):
        self._BusinessLicense = BusinessLicense

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._AuthorizationTypes = params.get("AuthorizationTypes")
        self._OrganizationName = params.get("OrganizationName")
        self._UniformSocialCreditCode = params.get("UniformSocialCreditCode")
        self._LegalName = params.get("LegalName")
        self._AutoJumpUrl = params.get("AutoJumpUrl")
        self._OrganizationAddress = params.get("OrganizationAddress")
        self._AdminName = params.get("AdminName")
        self._AdminMobile = params.get("AdminMobile")
        self._AdminIdCardNumber = params.get("AdminIdCardNumber")
        self._AdminIdCardType = params.get("AdminIdCardType")
        self._UniformSocialCreditCodeSame = params.get("UniformSocialCreditCodeSame")
        self._LegalNameSame = params.get("LegalNameSame")
        self._AdminNameSame = params.get("AdminNameSame")
        self._AdminIdCardNumberSame = params.get("AdminIdCardNumberSame")
        self._AdminMobileSame = params.get("AdminMobileSame")
        self._OrganizationNameSame = params.get("OrganizationNameSame")
        self._BusinessLicense = params.get("BusinessLicense")
        self._Endpoint = params.get("Endpoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationAuthUrlResponse(AbstractModel):
    """CreateOrganizationAuthUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AuthUrl: “H5”-H5长连接
"SHORT_H5"- H5短链
"APP"-小程序
"PC"-PC浏览器
链接有效期统一30天
        :type AuthUrl: str
        :param _ExpiredTime: 链接过期时间戳
        :type ExpiredTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AuthUrl = None
        self._ExpiredTime = None
        self._RequestId = None

    @property
    def AuthUrl(self):
        return self._AuthUrl

    @AuthUrl.setter
    def AuthUrl(self, AuthUrl):
        self._AuthUrl = AuthUrl

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
        self._AuthUrl = params.get("AuthUrl")
        self._ExpiredTime = params.get("ExpiredTime")
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

<ul>
<li>1. 若UserId为空，Name和Mobile 必须提供。</li>
<li>2. 若UserId 与 Name，Mobile均存在，将优先采用UserId对应的员工。</li>
</ul>
        :type UserId: str
        :param _Name: 员工姓名，必须与手机号码一起使用。
如果UserId为空，则此字段不能为空。同时，姓名和手机号码必须与传入合同（FlowId）中的签署人信息一致。
        :type Name: str
        :param _Mobile: 员工手机号，必须与姓名一起使用。
 如果UserId为空，则此字段不能为空。同时，姓名和手机号码必须与传入合同（FlowId）中的签署人信息一致。
        :type Mobile: str
        :param _RecipientIds: 为签署方经办人在签署合同中的参与方ID，必须与参数FlowIds数组一一对应。
您可以通过查询合同接口（DescribeFlowInfo）查询此参数。
若传了此参数，则可以不传 UserId, Name, Mobile等参数
        :type RecipientIds: list of str
        """
        self._Operator = None
        self._FlowIds = None
        self._Agent = None
        self._UserId = None
        self._Name = None
        self._Mobile = None
        self._RecipientIds = None

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

    @property
    def RecipientIds(self):
        return self._RecipientIds

    @RecipientIds.setter
    def RecipientIds(self, RecipientIds):
        self._RecipientIds = RecipientIds


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
        self._RecipientIds = params.get("RecipientIds")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateOrganizationGroupInvitationLinkRequest(AbstractModel):
    """CreateOrganizationGroupInvitationLink请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。使用此接口时，必须填写userId。 支持填入集团子公司经办人 userId 代发合同。  注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _ExpireTime: 到期时间（以秒为单位的时间戳），其上限为30天的有效期限。
        :type ExpireTime: int
        """
        self._Operator = None
        self._ExpireTime = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationGroupInvitationLinkResponse(AbstractModel):
    """CreateOrganizationGroupInvitationLink返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Link: 加入集团二维码链接，子企业的管理员可以直接扫码进入。
注意:1. 该链接有效期时间为ExpireTime，同时需要注意保密，不要外泄给无关用户。2. 该链接不支持小程序嵌入，仅支持<b>移动端浏览器</b>打开。3. <font color="red">生成的链路后面不能再增加参数</font>（会出现覆盖链接中已有参数导致错误）
        :type Link: str
        :param _ExpireTime: 到期时间（以秒为单位的时间戳）
        :type ExpireTime: int
        :param _JumpUrl: 加入集团短链接。
注意:
1. 该链接有效期时间为ExpireTime，同时需要注意保密，不要外泄给无关用户。
2. 该链接不支持小程序嵌入，仅支持<b>移动端浏览器</b>打开。
3. <font color="red">生成的链路后面不能再增加参数</font>（会出现覆盖链接中已有参数导致错误）
        :type JumpUrl: str
        :param _MiniAppPath: 腾讯电子签小程序加入集团链接。

<li>小程序和APP集成使用</li>
<li>得到的链接类似于`pages/guide?shortKey=yDw***k1xFc5`, 用法可以参考：<a href="https://qian.tencent.com/developers/company/openwxminiprogram" target="_blank">跳转电子签小程序</a></li>


注： <font color="red">生成的链路后面不能再增加参数</font>
        :type MiniAppPath: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Link = None
        self._ExpireTime = None
        self._JumpUrl = None
        self._MiniAppPath = None
        self._RequestId = None

    @property
    def Link(self):
        return self._Link

    @Link.setter
    def Link(self, Link):
        self._Link = Link

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def JumpUrl(self):
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl

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
        self._Link = params.get("Link")
        self._ExpireTime = params.get("ExpireTime")
        self._JumpUrl = params.get("JumpUrl")
        self._MiniAppPath = params.get("MiniAppPath")
        self._RequestId = params.get("RequestId")


class CreateOrganizationInfoChangeUrlRequest(AbstractModel):
    """CreateOrganizationInfoChangeUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _ChangeType: 企业信息变更类型，可选类型如下：
<ul><li>**1**：企业超管变更</li><li>**2**：企业基础信息变更</li></ul>
        :type ChangeType: int
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._ChangeType = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def ChangeType(self):
        return self._ChangeType

    @ChangeType.setter
    def ChangeType(self, ChangeType):
        self._ChangeType = ChangeType

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
        self._ChangeType = params.get("ChangeType")
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
        


class CreateOrganizationInfoChangeUrlResponse(AbstractModel):
    """CreateOrganizationInfoChangeUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 创建的企业信息变更链接。
        :type Url: str
        :param _ExpiredTime: 链接过期时间。链接7天有效。
        :type ExpiredTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreatePartnerAutoSignAuthUrlRequest(AbstractModel):
    """CreatePartnerAutoSignAuthUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: 代理企业和员工的信息。<br/>在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Operator: 执行本接口操作的员工信息。<br/>注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _AuthorizedOrganizationId: 被授企业id/授权方企业id，和AuthorizedOrganizationName二选一传入
        :type AuthorizedOrganizationId: str
        :param _AuthorizedOrganizationName: 被授企业名称/授权方企业名称，和AuthorizedOrganizationId二选一传入
        :type AuthorizedOrganizationName: str
        :param _SealTypes: 指定印章类型，指定后只能选择该类型的印章进行授权支持以下印章类型：- OFFICIAL : 企业公章- CONTRACT : 合同专用章- FINANCE : 财务专用章- PERSONNEL : 人事专用章
        :type SealTypes: list of str
        :param _AuthToMe: 他方授权给我方：
- false：我方授权他方，AuthorizedOrganizationName代表【被授权方】企业名称
- true：他方授权我方，AuthorizedOrganizationName代表【授权方】企业名称
        :type AuthToMe: bool
        """
        self._Agent = None
        self._Operator = None
        self._AuthorizedOrganizationId = None
        self._AuthorizedOrganizationName = None
        self._SealTypes = None
        self._AuthToMe = None

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
    def AuthorizedOrganizationId(self):
        return self._AuthorizedOrganizationId

    @AuthorizedOrganizationId.setter
    def AuthorizedOrganizationId(self, AuthorizedOrganizationId):
        self._AuthorizedOrganizationId = AuthorizedOrganizationId

    @property
    def AuthorizedOrganizationName(self):
        return self._AuthorizedOrganizationName

    @AuthorizedOrganizationName.setter
    def AuthorizedOrganizationName(self, AuthorizedOrganizationName):
        self._AuthorizedOrganizationName = AuthorizedOrganizationName

    @property
    def SealTypes(self):
        return self._SealTypes

    @SealTypes.setter
    def SealTypes(self, SealTypes):
        self._SealTypes = SealTypes

    @property
    def AuthToMe(self):
        return self._AuthToMe

    @AuthToMe.setter
    def AuthToMe(self, AuthToMe):
        self._AuthToMe = AuthToMe


    def _deserialize(self, params):
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._AuthorizedOrganizationId = params.get("AuthorizedOrganizationId")
        self._AuthorizedOrganizationName = params.get("AuthorizedOrganizationName")
        self._SealTypes = params.get("SealTypes")
        self._AuthToMe = params.get("AuthToMe")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePartnerAutoSignAuthUrlResponse(AbstractModel):
    """CreatePartnerAutoSignAuthUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 授权链接，以短链形式返回，短链的有效期参考回参中的 ExpiredTime。
        :type Url: str
        :param _MiniAppPath: 从客户小程序或者客户APP跳转至腾讯电子签小程序进行批量签署的跳转路径
        :type MiniAppPath: str
        :param _ExpireTime: 链接过期时间以 Unix 时间戳格式表示，从生成链接时间起，往后7天有效期。过期后短链将失效，无法打开。
        :type ExpireTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._MiniAppPath = None
        self._ExpireTime = None
        self._RequestId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def MiniAppPath(self):
        return self._MiniAppPath

    @MiniAppPath.setter
    def MiniAppPath(self, MiniAppPath):
        self._MiniAppPath = MiniAppPath

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._MiniAppPath = params.get("MiniAppPath")
        self._ExpireTime = params.get("ExpireTime")
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
<li> HONGKONG_AND_MACAO  : 港澳居民来往内地通行证</li>
<li> HONGKONG_MACAO_AND_TAIWAN  : 港澳台居民居住证(格式同居民身份证)</li></ul>
        :type IdCardType: str
        :param _IdCardNumber: 证件号码，应符合以下规则
<ul><li>居民身份证号码应为18位字符串，由数字和大写字母X组成（如存在X，请大写）。</li>
<li>港澳居民来往内地通行证号码共11位。第1位为字母，“H”字头签发给香港居民，“M”字头签发给澳门居民；第2位至第11位为数字。</li>
<li>港澳台居民居住证号码编码规则与中国大陆身份证相同，应为18位字符串。</li></ul>
        :type IdCardNumber: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _SceneKey: 自动签使用的场景值, 可以选择的场景值如下:
<ul><li> **E_PRESCRIPTION_AUTO_SIGN** :  电子处方场景</li><li> **OTHER** :  通用场景</li></ul>

注: `不传默认为处方单场景，即E_PRESCRIPTION_AUTO_SIGN`
        :type SceneKey: str
        """
        self._Operator = None
        self._UserName = None
        self._IdCardType = None
        self._IdCardNumber = None
        self._Agent = None
        self._SceneKey = None

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

    @property
    def SceneKey(self):
        return self._SceneKey

    @SceneKey.setter
    def SceneKey(self, SceneKey):
        self._SceneKey = SceneKey


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
        self._SceneKey = params.get("SceneKey")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Operator: 执行本接口操作的员工信息。使用此接口时，必须填写userId。
支持填入集团子公司经办人 userId 代发合同。

注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _ResourceId: 资源id，与ResourceType相对应，取值范围：
<ul>
<li>文件Id（通过UploadFiles获取文件资源Id）</li>
<li>模板Id（通过控制台创建模板后获取模板Id）</li>
</ul>
注意：需要同时设置 ResourceType 参数指定资源类型
        :type ResourceId: str
        :param _FlowName: 自定义的合同流程的名称，长度不能超过200个字符，只能由中文汉字、中文标点、英文字母、阿拉伯数字、空格、小括号、中括号、中划线、下划线以及（,）、（;）、（.）、(&)、（+）组成。

该名称还将用于合同签署完成后文件下载的默认文件名称。
        :type FlowName: str
        :param _ResourceType: 资源类型，取值有：
<ul><li> **1**：模板</li>
<li> **2**：文件（默认值）</li></ul>
        :type ResourceType: int
        :param _Unordered: 合同流程的签署顺序类型：
<ul><li> **false**：(默认)有序签署, 本合同多个参与人需要依次签署 </li>
<li> **true**：无序签署, 本合同多个参与人没有先后签署限制</li></ul>
        :type Unordered: bool
        :param _Deadline: 合同流程的签署截止时间，格式为Unix标准时间戳（秒），如果未设置签署截止时间，则默认为合同流程创建后的365天时截止。

        :type Deadline: int
        :param _UserFlowTypeId: 用户自定义合同类型Id

该id为电子签企业内的合同类型id， 可以在控制台-合同-自定义合同类型处获取
注: `该参数如果和FlowType同时传，以该参数优先生效`
        :type UserFlowTypeId: str
        :param _FlowType: 合同流程的类别分类（可自定义名称，如销售合同/入职合同等），最大长度为200个字符，仅限中文、字母、数字和下划线组成。
        :type FlowType: str
        :param _Approvers: 合同流程的参与方列表，最多可支持50个参与方，可在列表中指定企业B端签署方和个人C端签署方的联系和认证方式等信息，具体定义可以参考开发者中心的ApproverInfo结构体。

如果合同流程是有序签署，Approvers列表中参与人的顺序就是默认的签署顺序，请确保列表中参与人的顺序符合实际签署顺序。
        :type Approvers: list of FlowCreateApprover
        :param _IntelligentStatus: 开启或者关闭智能添加填写区：
<ul><li> **OPEN**：开启（默认值）</li>
<li> **CLOSE**：关闭</li></ul>
        :type IntelligentStatus: str
        :param _Components: 该字段已废弃，请使用InitiatorComponents
        :type Components: :class:`tencentcloud.ess.v20201111.models.Component`
        :param _FlowOption: 发起合同个性化参数
用于满足创建及页面操作过程中的个性化要求
具体定制化内容详见数据接口说明
        :type FlowOption: :class:`tencentcloud.ess.v20201111.models.CreateFlowOption`
        :param _NeedSignReview: 发起方企业的签署人进行签署操作前，是否需要企业内部走审批流程，取值如下：
<ul><li> **false**：（默认）不需要审批，直接签署。</li>
<li> **true**：需要走审批流程。当到对应参与人签署时，会阻塞其签署操作，等待企业内部审批完成。</li></ul>
企业可以通过CreateFlowSignReview审批接口通知腾讯电子签平台企业内部审批结果
<ul><li> 如果企业通知腾讯电子签平台审核通过，签署方可继续签署动作。</li>
<li> 如果企业通知腾讯电子签平台审核未通过，平台将继续阻塞签署方的签署动作，直到企业通知平台审核通过。</li></ul>
注：`此功能可用于与企业内部的审批流程进行关联，支持手动、静默签署合同`
        :type NeedSignReview: bool
        :param _NeedCreateReview: 发起方企业的签署人进行发起操作是否需要企业内部审批。使用此功能需要发起方企业有参与签署。

若设置为true，发起审核结果需通过接口 CreateFlowSignReview 通知电子签，审核通过后，发起方企业签署人方可进行发起操作，否则会阻塞其发起操作。


        :type NeedCreateReview: bool
        :param _UserData: 调用方自定义的个性化字段(可自定义此名称)，并以base64方式编码，支持的最大数据大小为 20480长度。

在合同状态变更的回调信息等场景中，该字段的信息将原封不动地透传给贵方。回调的相关说明可参考开发者中心的<a href="https://qian.tencent.com/developers/company/callback_types_v2" target="_blank">回调通知</a>模块。
        :type UserData: str
        :param _CcInfos: 合同流程的抄送人列表，最多可支持50个抄送人，抄送人可查看合同内容及签署进度，但无需参与合同签署。

        :type CcInfos: :class:`tencentcloud.ess.v20201111.models.CcInfo`
        :param _FlowId: 合同Id：用于通过一个已发起的合同快速生成一个发起流程web链接
注: `该参数必须是一个待发起审核的合同id，并且还未审核通过`
        :type FlowId: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _InitiatorComponents: 模板或者合同中的填写控件列表，列表中可支持下列多种填写控件，控件的详细定义参考开发者中心的Component结构体

        :type InitiatorComponents: list of Component
        """
        self._Operator = None
        self._ResourceId = None
        self._FlowName = None
        self._ResourceType = None
        self._Unordered = None
        self._Deadline = None
        self._UserFlowTypeId = None
        self._FlowType = None
        self._Approvers = None
        self._IntelligentStatus = None
        self._Components = None
        self._FlowOption = None
        self._NeedSignReview = None
        self._NeedCreateReview = None
        self._UserData = None
        self._CcInfos = None
        self._FlowId = None
        self._Agent = None
        self._InitiatorComponents = None

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
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

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
    def CcInfos(self):
        return self._CcInfos

    @CcInfos.setter
    def CcInfos(self, CcInfos):
        self._CcInfos = CcInfos

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
    def InitiatorComponents(self):
        return self._InitiatorComponents

    @InitiatorComponents.setter
    def InitiatorComponents(self, InitiatorComponents):
        self._InitiatorComponents = InitiatorComponents


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._ResourceId = params.get("ResourceId")
        self._FlowName = params.get("FlowName")
        self._ResourceType = params.get("ResourceType")
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
        if params.get("Components") is not None:
            self._Components = Component()
            self._Components._deserialize(params.get("Components"))
        if params.get("FlowOption") is not None:
            self._FlowOption = CreateFlowOption()
            self._FlowOption._deserialize(params.get("FlowOption"))
        self._NeedSignReview = params.get("NeedSignReview")
        self._NeedCreateReview = params.get("NeedCreateReview")
        self._UserData = params.get("UserData")
        if params.get("CcInfos") is not None:
            self._CcInfos = CcInfo()
            self._CcInfos._deserialize(params.get("CcInfos"))
        self._FlowId = params.get("FlowId")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("InitiatorComponents") is not None:
            self._InitiatorComponents = []
            for item in params.get("InitiatorComponents"):
                obj = Component()
                obj._deserialize(item)
                self._InitiatorComponents.append(obj)
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
        :param _Url: 发起流程的web页面链接，有效期5分钟
        :type Url: str
        :param _FlowId: 创建的合同id（还未实际发起），每次调用会生成新的id，用户可以记录此字段对应后续页面发起的合同，若在页面上未成功发起，则此字段无效。
        :type FlowId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._FlowId = None
        self._RequestId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

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
        self._Url = params.get("Url")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreatePreparedPersonalEsignRequest(AbstractModel):
    """CreatePreparedPersonalEsign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserName: 个人用户姓名
        :type UserName: str
        :param _IdCardNumber: 证件号码，应符合以下规则
<ul><li>居民身份证号码应为18位字符串，由数字和大写字母X组成（如存在X，请大写）。</li>
<li>港澳居民来往内地通行证号码共11位。第1位为字母，“H”字头签发给香港居民，“M”字头签发给澳门居民；第2位至第11位为数字。。</li>
<li>港澳台居民居住证号码编码规则与中国大陆身份证相同，应为18位字符串。</li></ul>
        :type IdCardNumber: str
        :param _SealName: 印章名称，长度1-50个字。
        :type SealName: str
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _IdCardType: 证件类型，支持以下类型
<ul><li>ID_CARD : 中国大陆居民身份证 (默认值)</li>
<li>HONGKONG_AND_MACAO : 港澳居民来往内地通行证</li>
<li>HONGKONG_MACAO_AND_TAIWAN : 港澳台居民居住证(格式同居民身份证)</li></ul>
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
        :param _ProcessSeal: 是否处理印章，默认不做印章处理。
取值如下：
<ul>
<li>false：不做任何处理；</li>
<li>true：做透明化处理和颜色增强。</li>
</ul>
        :type ProcessSeal: bool
        :param _FileId: 印章图片文件 id
取值：
填写的FileId通过UploadFiles接口上传文件获取。
        :type FileId: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _LicenseType: 设置用户开通自动签时是否绑定个人自动签账号许可。一旦绑定后，将扣减购买的个人自动签账号许可一次（1年有效期），不可解绑释放。不传默认为绑定自动签账号许可。 0-绑定个人自动签账号许可，开通后将扣减购买的个人自动签账号许可一次 1-不绑定，发起合同时将按标准合同套餐进行扣减	
        :type LicenseType: int
        :param _SceneKey: 自动签使用的场景值, 可以选择的场景值如下:
<ul><li> **E_PRESCRIPTION_AUTO_SIGN** :  电子处方场景</li><li> **OTHER** :  通用场景</li></ul>

注: `不传默认为处方单场景，即E_PRESCRIPTION_AUTO_SIGN`
        :type SceneKey: str
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
        self._SceneKey = None

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

    @property
    def SceneKey(self):
        return self._SceneKey

    @SceneKey.setter
    def SceneKey(self, SceneKey):
        self._SceneKey = SceneKey


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
        self._SceneKey = params.get("SceneKey")
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
        :param _SealId: 导入生成的印章ID，为32位字符串。
建议开发者保存此印章ID，开头实名认证后，通过此 ID查询导入的印章。
        :type SealId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateResultPageConfig(AbstractModel):
    """发起流程的可嵌入页面操作结果页配置

    """

    def __init__(self):
        r"""
        :param _Type: <ul>
  <li>0 : 发起审批成功页面（通过接口<a href="https://qian.tencent.com/developers/companyApis/embedPages/CreatePrepareFlow/" target="_blank">创建发起流程web页面</a>发起时设置了NeedCreateReview参数为true）</li>
</ul>
        :type Type: int
        :param _Title: 结果页标题，不超过50字
        :type Title: str
        :param _Description: 结果页描述，不超过200字
        :type Description: str
        """
        self._Type = None
        self._Title = None
        self._Description = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Title = params.get("Title")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param _IdCardType: 证件类型，支持以下类型
<ul><li>ID_CARD : 居民身份证</li>
<li>HONGKONG_AND_MACAO : 港澳居民来往内地通行证</li>
<li>HONGKONG_MACAO_AND_TAIWAN : 港澳台居民居住证(格式同居民身份证)</li></ul>
        :type IdCardType: str
        :param _IdCardNumber: 证件号码，应符合以下规则
<ul><li>居民身份证号码应为18位字符串，由数字和大写字母X组成(如存在X，请大写)。</li>
<li>港澳居民来往内地通行证号码共11位。第1位为字母，“H”字头签发给香港居民，“M”字头签发给澳门居民；第2位至第11位为数字。</li>
<li>港澳台居民居住证号码编码规则与中国大陆身份证相同，应为18位字符串。</li></ul>
        :type IdCardNumber: str
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

<ul><li> **0** : 腾讯电子签小程序个人首页 (默认) <a href="https://qcloudimg.tencent-cloud.cn/raw/a2667ea84ec993cc060321afe3191d65.jpg" target="_blank" >点击查看示例页面</a></li>
<li> **1** : 腾讯电子签小程序流程合同的详情页 (即合同签署页面)<a href="https://qcloudimg.tencent-cloud.cn/raw/446a679f09b1b7f40eb84e67face8acc.jpg" target="_blank" >点击查看示例页面</a></li>
<li> **2** : 腾讯电子签小程序合同列表页 <a href="https://qcloudimg.tencent-cloud.cn/raw/c7b80e44c1d68ae3270a6fc4939c7214.jpg" target="_blank" >点击查看示例页面</a> </li>
<li> **3** : 腾讯电子签小程序合同封面页  （注：`生成动态签署人补充链接时，必须指定为封面页`）<a href="https://qcloudimg.tencent-cloud.cn/raw/0d22cc587be4bf084877c151350c3bf7.jpg" target="_blank" >点击查看示例页面</a></li></ul>
        :type PathType: int
        :param _AutoJumpBack: 签署完成后是否自动回跳
<ul><li>**false**：否, 签署完成不会自动跳转回来(默认)</li><li>**true**：是, 签署完成会自动跳转回来</li></ul>

注: 
1. 该参数<font color="red">只针对APP类型（电子签小程序跳转贵方小程序）场景</font> 的签署链接有效
2. <font color="red">手机应用APP 或 微信小程序需要监控界面的返回走后序逻辑</font>, 微信小程序的文档可以参考[这个](https://developers.weixin.qq.com/miniprogram/dev/reference/api/App.html#onShow-Object-object)
3. <font color="red">电子签小程序跳转贵方APP，不支持自动跳转，必需用户手动点击完成按钮（微信的限制）</font> 
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
        :param _RecipientId: 签署节点ID，用于生成动态签署人链接完成领取。

注：`生成动态签署人补充链接时必传。`
        :type RecipientId: str
        :param _FlowGroupUrlInfo: 合同组相关信息，指定合同组子合同和签署方的信息，用于补充动态签署人。
        :type FlowGroupUrlInfo: :class:`tencentcloud.ess.v20201111.models.FlowGroupUrlInfo`
        """
        self._Operator = None
        self._OrganizationName = None
        self._Name = None
        self._Mobile = None
        self._IdCardType = None
        self._IdCardNumber = None
        self._EndPoint = None
        self._FlowId = None
        self._FlowGroupId = None
        self._PathType = None
        self._AutoJumpBack = None
        self._Agent = None
        self._Hides = None
        self._RecipientId = None
        self._FlowGroupUrlInfo = None

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

    @property
    def RecipientId(self):
        return self._RecipientId

    @RecipientId.setter
    def RecipientId(self, RecipientId):
        self._RecipientId = RecipientId

    @property
    def FlowGroupUrlInfo(self):
        return self._FlowGroupUrlInfo

    @FlowGroupUrlInfo.setter
    def FlowGroupUrlInfo(self, FlowGroupUrlInfo):
        self._FlowGroupUrlInfo = FlowGroupUrlInfo


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._OrganizationName = params.get("OrganizationName")
        self._Name = params.get("Name")
        self._Mobile = params.get("Mobile")
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
        self._EndPoint = params.get("EndPoint")
        self._FlowId = params.get("FlowId")
        self._FlowGroupId = params.get("FlowGroupId")
        self._PathType = params.get("PathType")
        self._AutoJumpBack = params.get("AutoJumpBack")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._Hides = params.get("Hides")
        self._RecipientId = params.get("RecipientId")
        if params.get("FlowGroupUrlInfo") is not None:
            self._FlowGroupUrlInfo = FlowGroupUrlInfo()
            self._FlowGroupUrlInfo._deserialize(params.get("FlowGroupUrlInfo"))
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


注： <font color="red">生成的链路后面不能再增加参数</font>
        :type SchemeUrl: str
        :param _SchemeQrcodeUrl: 二维码，在生成动态签署人跳转封面页链接时返回
        :type SchemeQrcodeUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SchemeUrl = None
        self._SchemeQrcodeUrl = None
        self._RequestId = None

    @property
    def SchemeUrl(self):
        return self._SchemeUrl

    @SchemeUrl.setter
    def SchemeUrl(self, SchemeUrl):
        self._SchemeUrl = SchemeUrl

    @property
    def SchemeQrcodeUrl(self):
        return self._SchemeQrcodeUrl

    @SchemeQrcodeUrl.setter
    def SchemeQrcodeUrl(self, SchemeQrcodeUrl):
        self._SchemeQrcodeUrl = SchemeQrcodeUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SchemeUrl = params.get("SchemeUrl")
        self._SchemeQrcodeUrl = params.get("SchemeQrcodeUrl")
        self._RequestId = params.get("RequestId")


class CreateSealPolicyRequest(AbstractModel):
    """CreateSealPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Users: 用户在电子文件签署平台标识信息，具体参考UserInfo结构体。可跟下面的UserIds可叠加起作用
        :type Users: list of UserInfo
        :param _SealId: 电子印章ID，为32位字符串。
建议开发者保留此印章ID，后续指定签署区印章或者操作印章需此印章ID。
可登录腾讯电子签控制台，在 "印章"->"印章中心"选择查看的印章，在"印章详情" 中查看某个印章的SealId(在页面中展示为印章ID)。
        :type SealId: str
        :param _Expired: 授权有效期，时间戳秒级。可以传0，代表有效期到2099年12月12日23点59分59秒。
        :type Expired: int
        :param _UserIds: 需要授权的用户UserId集合。跟上面的SealId参数配合使用。选填，跟上面的Users同时起作用
        :type UserIds: list of str
        :param _Policy: 印章授权内容
        :type Policy: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _UserIds: 最终授权成功的用户ID，在腾讯电子签平台的唯一身份标识，为32位字符串。
可登录腾讯电子签控制台，在 "更多能力"->"组织管理" 中查看某位员工的UserId(在页面中展示为用户ID)。
        :type UserIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _SealName: 电子印章名字，1-50个中文字符
注:`同一企业下电子印章名字不能相同`
        :type SealName: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _GenerateSource: 电子印章生成方式
<ul>
<li><strong>空值</strong>:(默认)使用上传的图片生成印章, 此时需要上传SealImage图片</li>
<li><strong>SealGenerateSourceSystem</strong>: 系统生成印章, 无需上传SealImage图片</li>
</ul>
        :type GenerateSource: str
        :param _SealType: 电子印章类型 , 可选类型如下: <ul><li>**OFFICIAL**: (默认)公章</li><li>**CONTRACT**: 合同专用章;</li><li>**FINANCE**: 财务专用章;</li><li>**PERSONNEL**: 人事专用章</li><li>**INVOICE**: 发票专用章</li><li>**OTHER**: 其他</li></ul>注: 同企业下只能有<font color="red">一个</font>公章, 重复创建会报错
        :type SealType: str
        :param _FileName: 电子印章图片文件名称，1-50个中文字符。
        :type FileName: str
        :param _Image: 电子印章图片base64编码，大小不超过10M（原始图片不超过5M），只支持PNG或JPG图片格式

注: `通过图片创建的电子印章，需电子签平台人工审核`


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
        :param _SealHorizontalText: 企业印章横向文字，最多可填15个汉字  (若超过印章最大宽度，优先压缩字间距，其次缩小字号)
横向文字的位置如下图中的"印章横向文字在这里"

![image](https://dyn.ess.tencent.cn/guide/capi/CreateSealByImage2.png)

        :type SealHorizontalText: str
        :param _SealChordText: 暂时不支持下弦文字设置
        :type SealChordText: str
        :param _SealCentralType: 系统生成的印章只支持STAR
        :type SealCentralType: str
        :param _FileToken: 通过文件上传时，服务端生成的电子印章上传图片的token

        :type FileToken: str
        :param _SealStyle: 印章样式, 可以选择的样式如下: 
<ul><li>**circle**:(默认)圆形印章</li>
<li>**ellipse**:椭圆印章</li></ul>
        :type SealStyle: str
        :param _SealSize: 印章尺寸取值描述, 可以选择的尺寸如下: 
<ul><li> **42_42**: 圆形企业公章直径42mm, 当SealStyle是圆形的时候才有效</li>
<li> **40_40**: 圆形企业印章直径40mm, 当SealStyle是圆形的时候才有效</li>
<li> **45_30**: 椭圆形印章45mm x 30mm, 当SealStyle是椭圆的时候才有效</li>
<li> **40_30**: 椭圆形印章40mm x 30mm, 当SealStyle是椭圆的时候才有效</li></ul>
        :type SealSize: str
        :param _TaxIdentifyCode: 企业税号
注:
<ul>
<li>1.印章类型SealType是INVOICE类型时，此参数才会生效</li>
<li>2.印章类型SealType是INVOICE类型，且该字段没有传入值或传入空时，会取该企业对应的统一社会信用代码作为默认的企业税号（<font color="red">如果是通过授权书授权方式认证的企业，此参数必传不能为空</font>）</li>
</ul>
        :type TaxIdentifyCode: str
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
        self._TaxIdentifyCode = None

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

    @property
    def TaxIdentifyCode(self):
        return self._TaxIdentifyCode

    @TaxIdentifyCode.setter
    def TaxIdentifyCode(self, TaxIdentifyCode):
        self._TaxIdentifyCode = TaxIdentifyCode


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
        self._TaxIdentifyCode = params.get("TaxIdentifyCode")
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
        :param _SealId: 电子印章ID，为32位字符串。
建议开发者保留此印章ID，后续指定签署区印章或者操作印章需此印章ID。
可登录腾讯电子签控制台，在 "印章"->"印章中心"选择查看的印章，在"印章详情" 中查看某个印章的SealId(在页面中展示为印章ID)。
        :type SealId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
<ul><li> **E_PRESCRIPTION_AUTO_SIGN** :  电子处方场景</li><li> **OTHER** :  通用场景</li></ul>
        :type SceneKey: str
        :param _AutoSignConfig: 自动签开通配置信息, 包括开通的人员的信息等
        :type AutoSignConfig: :class:`tencentcloud.ess.v20201111.models.AutoSignConfig`
        :param _UrlType: 生成的链接类型：
<ul><li> 不传(即为空值) 则会生成小程序端开通链接(默认)</li>
<li> **H5SIGN** : 生成H5端开通链接</li></ul>
        :type UrlType: str
        :param _NotifyType: 是否通知开通方，通知类型:
<ul><li>默认不设置为不通知开通方</li>
<li>**SMS** :  短信通知 ,如果需要短信通知则NotifyAddress填写对方的手机号</li></ul>
        :type NotifyType: str
        :param _NotifyAddress: 如果通知类型NotifyType选择为SMS，则此处为手机号, 其他通知类型不需要设置此项
        :type NotifyAddress: str
        :param _ExpiredTime: 链接的过期时间，格式为Unix时间戳，不能早于当前时间，且最大为当前时间往后30天。`如果不传，默认过期时间为当前时间往后7天。`
        :type ExpiredTime: int
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _UserData: 调用方自定义的个性化字段(可自定义此字段的值)，并以base64方式编码，支持的最大数据大小为 20480长度。 在个人自动签的开通、关闭等回调信息场景中，该字段的信息将原封不动地透传给贵方。 
        :type UserData: str
        """
        self._Operator = None
        self._SceneKey = None
        self._AutoSignConfig = None
        self._UrlType = None
        self._NotifyType = None
        self._NotifyAddress = None
        self._ExpiredTime = None
        self._Agent = None
        self._UserData = None

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
        self._UserData = params.get("UserData")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateUserAutoSignSealUrlRequest(AbstractModel):
    """CreateUserAutoSignSealUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _SceneKey: 自动签使用的场景值, 可以选择的场景值如下:
<ul><li> **E_PRESCRIPTION_AUTO_SIGN** :  电子处方场景</li><li> **OTHER** :  通用场景</li></ul>
        :type SceneKey: str
        :param _UserInfo: 自动签开通个人用户信息, 包括名字,身份证等。
        :type UserInfo: :class:`tencentcloud.ess.v20201111.models.UserThreeFactor`
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _ExpiredTime: 链接的过期时间，格式为Unix时间戳，不能早于当前时间，且最大为当前时间往后30天。`如果不传，默认过期时间为当前时间往后7天。`
        :type ExpiredTime: int
        """
        self._Operator = None
        self._SceneKey = None
        self._UserInfo = None
        self._Agent = None
        self._ExpiredTime = None

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

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime


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
        self._ExpiredTime = params.get("ExpiredTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserAutoSignSealUrlResponse(AbstractModel):
    """CreateUserAutoSignSealUrl返回参数结构体

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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateUserMobileChangeUrlRequest(AbstractModel):
    """CreateUserMobileChangeUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。使用此接口时，必须填写userId。 支持填入集团子公司经办人 userId 代发合同。  注: 在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Agent: 代理企业和员工的信息。 在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _UserId: 如果您要修改企业员工用户ID，传递此用户ID即可，其他参数（Name，UserAccountType，IdCardType，IdCardNumber）将被忽略。如果不传此用户ID，则会使用其他参数来进行链接生成。

[点击查看用户ID的获取方式](https://res.ess.tencent.cn/cdn/tsign-developer-center/assets/images/%E7%BB%84%E7%BB%87%E6%9E%B6%E6%9E%84-47eb7105dd300e6dc0c502fba22688ae.png)
        :type UserId: str
        :param _UserAccountType: 要修改手机号用户的类型。
<ul><li>0：员工 （默认）</li><li>1：个人</li>
</ul>
如果是员工类型，<b>只能修改本方员工，而不能修改其他企业的员工</b>。
如果是个人类型，可<b>不指定用户身份，生成的是固定的链接，当前登录电子签小程序的用户可进行换绑。</b>

        :type UserAccountType: int
        :param _Name: 要修改手机号用户的姓名，请确保填写的姓名为对方的真实姓名，而非昵称等代名。

如果没有传递 userId且 userAccountType 是 0 或者没有传递， 此参数为<b>必填项。</b>
        :type Name: str
        :param _IdCardType: 要修改手机号用户的证件类型，
目前支持的账号类型如下：

<ul><li><b>ID_CARD </b>: （默认）中国大陆居民身份证 </li>
<li><b>HONGKONG_AND_MACAO</b> : 港澳居民来往内地通行证</li>
<li><b>HONGKONG_MACAO_AND_TAIWAN </b>: 港澳台居民居住证(格式同居民身份证)</li></ul>

        :type IdCardType: str
        :param _IdCardNumber: 要修改手机号用户的身份证号码，应符合以下规则
<ul><li>居民身份证号码应为18位字符串，由数字和大写字母X组成（如存在X，请大写）。</li>
<li>港澳居民来往内地通行证号码共11位。第1位为字母，“H”字头签发给香港居民，“M”字头签发给澳门居民；第2位至第11位为数字。</li>
<li>港澳台居民居住证号码编码规则与中国大陆身份证相同，应为18位字符串。</li></ul>
如果没有传递 userId且 userAccountType 是 0 或者没有传递， 此参数为<b>必填项。</b>
        :type IdCardNumber: str
        :param _Endpoint: 要跳转的链接类型

<ul>
<li><b>HTTP</b>：（默认）跳转电子签小程序的http_url,短信通知或者H5跳转适合此类型 ，此时返回长链 (默认类型)</li>
<li><b>HTTP_SHORT_URL</b>：跳转电子签小程序的http_url,短信通知或者H5跳转适合此类型，此时返回短链</li>
<li><b>APP</b>：第三方APP或小程序跳转电子签小程序的path, APP或者小程序跳转适合此类型</li>
</ul>


        :type Endpoint: str
        :param _UserData: 在用户完成实名认证后，其自定义数据将通过[手机号换绑回调](https://qian.tencent.com/developers/company/callback_types_staffs/#%E5%8D%81%E4%B8%89-%E4%B8%AA%E4%BA%BA%E5%91%98%E5%B7%A5%E6%89%8B%E6%9C%BA%E5%8F%B7%E4%BF%AE%E6%94%B9%E5%90%8E%E5%9B%9E%E8%B0%83)返回，以便用户确认其个人数据信息。请注意，自定义数据的字符长度上限为1000，且必须采用base64编码格式。

请注意：
此参数仅支持通过[获取c端用户实名链接](https://qian.tencent.com/developers/companyApis/users/CreateUserVerifyUrl)接口实名的用户生效。
        :type UserData: str
        """
        self._Operator = None
        self._Agent = None
        self._UserId = None
        self._UserAccountType = None
        self._Name = None
        self._IdCardType = None
        self._IdCardNumber = None
        self._Endpoint = None
        self._UserData = None

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
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserAccountType(self):
        return self._UserAccountType

    @UserAccountType.setter
    def UserAccountType(self, UserAccountType):
        self._UserAccountType = UserAccountType

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
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

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
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._UserId = params.get("UserId")
        self._UserAccountType = params.get("UserAccountType")
        self._Name = params.get("Name")
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
        self._Endpoint = params.get("Endpoint")
        self._UserData = params.get("UserData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserMobileChangeUrlResponse(AbstractModel):
    """CreateUserMobileChangeUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 腾讯电子签小程序的实名认证链接。
如果没有传递，默认值是 HTTP。 链接的有效期均是 7 天。

- 如果EndPoint是APP，
得到的链接类似于pages/guide/index?to=MOBILE_CHANGE_INTENTION&shortKey=yDCZHUyOcExAlcOvNod0, 用法可以参考描述中的"跳转到小程序的实现"

- 如果EndPoint是HTTP，
得到的链接类似于https://res.ess.tencent.cn/cdn/h5-activity/jump-mp.html?to=MOBILE_CHANGE_INTENTION&shortKey=yDCZHUyOcChrfpaswT0d，点击后会跳转到腾讯电子签小程序进行签署

- 如果EndPoint是HTTP_SHORT_URL，
得到的链接类似于https://essurl.cn/2n**42Nd，点击后会跳转到腾讯电子签小程序进行签署


注： 生成的链路后面不能再增加参数
示例值：https://essurl.cn/2n**42Nd
        :type Url: str
        :param _ExpireTime: 链接失效期限如下：

<ul>
<li>如果指定更换绑定手机号的用户(指定用户ID或姓名等信息)，则设定的链接失效期限为7天后。</li>
<li>如果没有指定更换绑定手机号的用户，则生成通用跳转到个人换手机号的界面，链接不会过期。</li>
</ul>
        :type ExpireTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._ExpireTime = None
        self._RequestId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._ExpireTime = params.get("ExpireTime")
        self._RequestId = params.get("RequestId")


class CreateUserVerifyUrlRequest(AbstractModel):
    """CreateUserVerifyUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 操作人信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Name: 要实名的姓名
        :type Name: str
        :param _IdCardNumber: 要实名的身份证号码，
身份证号码如果有x的话，统一传大写X
        :type IdCardNumber: str
        :param _IdCardType: 证件类型，目前只支持身份证类型：ID_CARD
        :type IdCardType: str
        :param _Mobile: 要实名的手机号，兼容带+86的格式
        :type Mobile: str
        :param _JumpUrl: 实名完之后的跳转链接，最大长度1000个字符。
链接类型请参考 <a href="https://qian.tencent.com/developers/company/openqianh5" target="_blank">跳转电子签H5</a>。

注：此参数仅支持 Endpoint 为 <font color="red">H5 或 H5_SHORT_URL </font>的时候传递

        :type JumpUrl: str
        :param _Endpoint: 要跳转的链接类型

- HTTP：
跳转电子签小程序的http_url,短信通知或者H5跳转适合此类型 ，此时返回长链 (默认类型)

- HTTP_SHORT_URL：
跳转电子签小程序的http_url,短信通知或者H5跳转适合此类型，此时返回短链

- APP：
第三方APP或小程序跳转电子签小程序的path, APP或者小程序跳转适合此类型

- H5：
跳转电子签H5实名页面的长链

- H5_SHORT_URL：
跳转电子签H5实名页面的短链

注：如果不传递，默认值是 <font color="red"> APP </font>
        :type Endpoint: str
        :param _AutoJumpBack: 签署完成后是否自动回跳
<ul><li>false：否, 实名完成不会自动跳转回来(默认)</li><li>true：是, 实名完成会自动跳转回来</li></ul>

注: 
1. 该参数<font color="red">只针对APP类型（第三方APP或小程序跳转电子签小程序）场景</font> 的实名链接有效
2. <font color="red">手机应用APP 或 微信小程序需要监控界面的返回走后序逻辑</font>, 微信小程序的文档可以参考[这个](https://developers.weixin.qq.com/miniprogram/dev/reference/api/App.html#onShow-Object-object)
3. <font color="red">电子签小程序跳转贵方APP，不支持自动跳转，必需用户手动点击完成按钮（微信的限制）</font> 
        :type AutoJumpBack: bool
        :param _UserData: 在用户完成实名认证后，其自定义数据将通过[企业引导个人实名认证后回调](https://qian.tencent.com/developers/company/callback_types_staffs/#%E5%8D%81%E4%BA%8C-%E4%BC%81%E4%B8%9A%E5%BC%95%E5%AF%BC%E4%B8%AA%E4%BA%BA%E5%AE%9E%E5%90%8D%E8%AE%A4%E8%AF%81%E5%90%8E%E5%9B%9E%E8%B0%83)返回，以便用户确认其个人数据信息。请注意，自定义数据的字符长度上限为1000，且必须采用base64编码格式。
        :type UserData: str
        """
        self._Operator = None
        self._Name = None
        self._IdCardNumber = None
        self._IdCardType = None
        self._Mobile = None
        self._JumpUrl = None
        self._Endpoint = None
        self._AutoJumpBack = None
        self._UserData = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCardNumber(self):
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def IdCardType(self):
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def JumpUrl(self):
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def AutoJumpBack(self):
        return self._AutoJumpBack

    @AutoJumpBack.setter
    def AutoJumpBack(self, AutoJumpBack):
        self._AutoJumpBack = AutoJumpBack

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
        self._Name = params.get("Name")
        self._IdCardNumber = params.get("IdCardNumber")
        self._IdCardType = params.get("IdCardType")
        self._Mobile = params.get("Mobile")
        self._JumpUrl = params.get("JumpUrl")
        self._Endpoint = params.get("Endpoint")
        self._AutoJumpBack = params.get("AutoJumpBack")
        self._UserData = params.get("UserData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserVerifyUrlResponse(AbstractModel):
    """CreateUserVerifyUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserVerifyUrl: 腾讯电子签小程序的实名认证链接。
如果没有传递，默认值是 HTTP。 链接的有效期均是 7 天。

- 如果EndPoint是APP，
得到的链接类似于pages/guide/index?to=MP_PERSONAL_VERIFY&shortKey=yDCZHUyOcExAlcOvNod0, 用法可以参考描述中的"跳转到小程序的实现"

- 如果EndPoint是HTTP，
得到的链接类似于https://res.ess.tencent.cn/cdn/h5-activity/jump-mp.html?to=TAG_VERIFY&shortKey=yDCZHUyOcChrfpaswT0d，点击后会跳转到腾讯电子签小程序进行签署

- 如果EndPoint是HTTP_SHORT_URL，
得到的链接类似于https://essurl.cn/2n**42Nd，点击后会跳转到腾讯电子签小程序进行签署

- 如果EndPoint是H5，
得到的链接类似于 https://quick.test.qian.tencent.cn/guide?Code=yDU****VJhsS5q&CodeType=xxx&shortKey=yD*****frcb，点击后会跳转到腾讯电子签H5页面进行签署

- 如果EndPoint是H5_SHORT_URL，
得到的链接类似于https://essurl.cn/2n**42Nd，点击后会跳转到腾讯电子签H5页面进行签署


`注：` <font color="red">生成的链路后面不能再增加参数</font>
示例值：https://essurl.cn/2n**42Nd
        :type UserVerifyUrl: str
        :param _ExpireTime: 链接过期时间
        :type ExpireTime: int
        :param _MiniAppId: 小程序appid，用于半屏拉起电子签小程序， 仅在 Endpoint 设置为 APP 的时候返回
        :type MiniAppId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserVerifyUrl = None
        self._ExpireTime = None
        self._MiniAppId = None
        self._RequestId = None

    @property
    def UserVerifyUrl(self):
        return self._UserVerifyUrl

    @UserVerifyUrl.setter
    def UserVerifyUrl(self, UserVerifyUrl):
        self._UserVerifyUrl = UserVerifyUrl

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def MiniAppId(self):
        return self._MiniAppId

    @MiniAppId.setter
    def MiniAppId(self, MiniAppId):
        self._MiniAppId = MiniAppId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserVerifyUrl = params.get("UserVerifyUrl")
        self._ExpireTime = params.get("ExpireTime")
        self._MiniAppId = params.get("MiniAppId")
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
        :param _WebThemeConfig: 电子签logo是否展示，主体颜色等配置项
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteExtendedServiceAuthInfosRequest(AbstractModel):
    """DeleteExtendedServiceAuthInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _UserIds: 本企业员工的id，需要已实名，正常在职员工
        :type UserIds: list of str
        :param _ExtendServiceType: 取值如下所示：
<ul><li>OPEN_SERVER_SIGN：企业自动签</li>
<li>BATCH_SIGN：批量签署</li>
</ul>
        :type ExtendServiceType: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._UserIds = None
        self._ExtendServiceType = None
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
        self._UserIds = params.get("UserIds")
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
        


class DeleteExtendedServiceAuthInfosResponse(AbstractModel):
    """DeleteExtendedServiceAuthInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _DeptId: 电子签中的部门ID，通过<a href="https://qian.tencent.com/developers/companyApis/organizations/DescribeIntegrationDepartments" target="_blank">DescribeIntegrationDepartments</a>接口可获得。
        :type DeptId: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _ReceiveDeptId: 交接部门ID。
待删除部门中的合同、印章和模板数据，将会被交接至该部门ID下；若未填写则交接至公司根部门。
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Operator: 执行本接口操作的员工信息。使用此接口时，必须填写UserId。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Employees: 待离职员工的信息最多不超过100个。应符合以下规则：

1. UserId和OpenId不可同时为空，必须填写其中一个，优先使用UserId。

2. **若需要进行离职交接**，交接人信息ReceiveUserId和ReceiveOpenId不可同时为空，必须填写其中一个，优先使用ReceiveUserId。
        :type Employees: list of Staff
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _DeleteEmployeeResult: 员工删除结果。包含成功数据与失败数据。
<ul><li>**成功数据**：展示员工姓名、手机号与电子签平台UserId</li>
<li>**失败数据**：展示员工电子签平台UserId、第三方平台OpenId和失败原因</li></ul>
        :type DeleteEmployeeResult: :class:`tencentcloud.ess.v20201111.models.DeleteStaffsResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _PolicyIds: 印章授权编码数组。这个参数跟下面的SealId其中一个必填，另外一个可选填
        :type PolicyIds: list of str
        :param _SealId: 电子印章ID，为32位字符串。
建议开发者保留此印章ID，后续指定签署区印章或者操作印章需此印章ID。
可登录腾讯电子签控制台，在 "印章"->"印章中心"选择查看的印章，在"印章详情" 中查看某个印章的SealId(在页面中展示为印章ID)。
注：印章ID。这个参数跟上面的PolicyIds其中一个必填，另外一个可选填。
        :type SealId: str
        :param _UserIds: 待授权的员工ID，员工在腾讯电子签平台的唯一身份标识，为32位字符串。
可登录腾讯电子签控制台，在 "更多能力"->"组织管理" 中查看某位员工的UserId(在页面中展示为用户ID)。
        :type UserIds: list of str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
    """集成版员工部门信息。

    """

    def __init__(self):
        r"""
        :param _DepartmentId: 部门ID。
        :type DepartmentId: str
        :param _DepartmentName: 部门名称。
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
        


class DescribeBatchOrganizationRegistrationUrlsRequest(AbstractModel):
    """DescribeBatchOrganizationRegistrationUrls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _TaskId: 通过接口CreateBatchOrganizationRegistrationTasks创建企业批量认证链接任得到的任务Id
        :type TaskId: str
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._TaskId = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
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
        


class DescribeBatchOrganizationRegistrationUrlsResponse(AbstractModel):
    """DescribeBatchOrganizationRegistrationUrls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrganizationAuthUrls: 企业批量注册链接信息
        :type OrganizationAuthUrls: list of OrganizationAuthUrl
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrganizationAuthUrls = None
        self._RequestId = None

    @property
    def OrganizationAuthUrls(self):
        return self._OrganizationAuthUrls

    @OrganizationAuthUrls.setter
    def OrganizationAuthUrls(self, OrganizationAuthUrls):
        self._OrganizationAuthUrls = OrganizationAuthUrls

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("OrganizationAuthUrls") is not None:
            self._OrganizationAuthUrls = []
            for item in params.get("OrganizationAuthUrls"):
                obj = OrganizationAuthUrl()
                obj._deserialize(item)
                self._OrganizationAuthUrls.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillUsageDetailRequest(AbstractModel):
    """DescribeBillUsageDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询开始时间字符串，格式为yyyymmdd,时间跨度不能大于31天
        :type StartTime: str
        :param _EndTime: 查询结束时间字符串，格式为yyyymmdd,时间跨度不能大于31天
        :type EndTime: str
        :param _Offset: 指定分页返回第几页的数据，如果不传默认返回第一页，页码从 0 开始，即首页为 0
        :type Offset: int
        :param _Limit: 指定分页每页返回的数据条数，如果不传默认为 50，单页最大支持 50。
        :type Limit: int
        :param _QuotaType: 查询的套餐类型 （选填 ）不传则查询所有套餐；
目前支持:
<ul>
<li>**CloudEnterprise**: 企业版合同</li>
<li>**SingleSignature**: 单方签章</li>
<li>**CloudProve**: 签署报告</li>
<li>**CloudOnlineSign**: 腾讯会议在线签约</li>
<li>**ChannelWeCard**: 微工卡</li>
<li>**SignFlow**: 合同套餐</li>
<li>**SignFace**: 签署意愿（人脸识别）</li>
<li>**SignPassword**: 签署意愿（密码）</li>
<li>**SignSMS**: 签署意愿（短信）</li>
<li>**PersonalEssAuth**: 签署人实名（腾讯电子签认证）</li>
<li>**PersonalThirdAuth**: 签署人实名（信任第三方认证）</li>
<li>**OrgEssAuth**: 签署企业实名</li>
<li>**FlowNotify**: 短信通知</li>
<li>**AuthService**: 企业工商信息查询</li>
</ul>
        :type QuotaType: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._QuotaType = None
        self._Agent = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

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
    def QuotaType(self):
        return self._QuotaType

    @QuotaType.setter
    def QuotaType(self, QuotaType):
        self._QuotaType = QuotaType

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._QuotaType = params.get("QuotaType")
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
        


class DescribeBillUsageDetailResponse(AbstractModel):
    """DescribeBillUsageDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Details: 消耗详情
        :type Details: list of BillUsageDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
                obj = BillUsageDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillUsageRequest(AbstractModel):
    """DescribeBillUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询开始时间字符串，格式为yyyymmdd,时间跨度不能大于90天
        :type StartTime: str
        :param _EndTime: 查询结束时间字符串，格式为yyyymmdd,时间跨度不能大于90天
        :type EndTime: str
        :param _QuotaType: 查询的套餐类型 （选填 ）不传则查询所有套餐；目前支持:<ul><li>**CloudEnterprise**: 企业版合同</li><li>**SingleSignature**: 单方签章</li><li>**CloudProve**: 签署报告</li><li>**CloudOnlineSign**: 腾讯会议在线签约</li><li>**ChannelWeCard**: 微工卡</li><li>**SignFlow**: 合同套餐</li><li>**SignFace**: 签署意愿（人脸识别）</li><li>**SignPassword**: 签署意愿（密码）</li><li>**SignSMS**: 签署意愿（短信）</li><li>**PersonalEssAuth**: 签署人实名（腾讯电子签认证）</li><li>**PersonalThirdAuth**: 签署人实名（信任第三方认证）</li><li>**OrgEssAuth**: 签署企业实名</li><li>**FlowNotify**: 短信通知</li><li>**AuthService**: 企业工商信息查询</li></ul>
        :type QuotaType: str
        :param _DisplaySubEnterprise: 是否展示集团子企业的明细，默认否
        :type DisplaySubEnterprise: bool
        """
        self._StartTime = None
        self._EndTime = None
        self._QuotaType = None
        self._DisplaySubEnterprise = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def QuotaType(self):
        return self._QuotaType

    @QuotaType.setter
    def QuotaType(self, QuotaType):
        self._QuotaType = QuotaType

    @property
    def DisplaySubEnterprise(self):
        return self._DisplaySubEnterprise

    @DisplaySubEnterprise.setter
    def DisplaySubEnterprise(self, DisplaySubEnterprise):
        self._DisplaySubEnterprise = DisplaySubEnterprise


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._QuotaType = params.get("QuotaType")
        self._DisplaySubEnterprise = params.get("DisplaySubEnterprise")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillUsageResponse(AbstractModel):
    """DescribeBillUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Summary: 企业套餐余额及使用情况
        :type Summary: list of OrgBillSummary
        :param _SubOrgSummary: 集团子企业套餐使用情况
注意：此字段可能返回 null，表示取不到有效值。
        :type SubOrgSummary: list of SubOrgBillSummary
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Summary = None
        self._SubOrgSummary = None
        self._RequestId = None

    @property
    def Summary(self):
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def SubOrgSummary(self):
        return self._SubOrgSummary

    @SubOrgSummary.setter
    def SubOrgSummary(self, SubOrgSummary):
        self._SubOrgSummary = SubOrgSummary

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Summary") is not None:
            self._Summary = []
            for item in params.get("Summary"):
                obj = OrgBillSummary()
                obj._deserialize(item)
                self._Summary.append(obj)
        if params.get("SubOrgSummary") is not None:
            self._SubOrgSummary = []
            for item in params.get("SubOrgSummary"):
                obj = SubOrgBillSummary()
                obj._deserialize(item)
                self._SubOrgSummary.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCancelFlowsTaskRequest(AbstractModel):
    """DescribeCancelFlowsTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
<br/>注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _TaskId: 批量撤销任务编号，为32位字符串，通过接口[获取批量撤销签署流程腾讯电子签小程序链接](https://qian.tencent.com/developers/companyApis/operateFlows/CreateBatchCancelFlowUrl)获得。
        :type TaskId: str
        :param _Agent: 代理企业和员工的信息。
<br/>在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._TaskId = None
        self._Agent = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
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
        


class DescribeCancelFlowsTaskResponse(AbstractModel):
    """DescribeCancelFlowsTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 批量撤销任务编号，为32位字符串，通过接口[获取批量撤销签署流程腾讯电子签小程序链接](https://qian.tencent.com/developers/companyApis/operateFlows/CreateBatchCancelFlowUrl)获得。
        :type TaskId: str
        :param _TaskStatus: 任务状态，需要关注的状态
<ul><li>**PROCESSING**  - 任务执行中</li>
<li>**END** - 任务处理完成</li>
<li>**TIMEOUT** 任务超时未处理完成，用户未在批量撤销链接有效期内操作</li></ul>
        :type TaskStatus: str
        :param _SuccessFlowIds: 批量撤销成功的签署流程编号
        :type SuccessFlowIds: list of str
        :param _FailureFlows: 批量撤销失败的签署流程信息
        :type FailureFlows: list of CancelFailureFlow
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._TaskStatus = None
        self._SuccessFlowIds = None
        self._FailureFlows = None
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
    def SuccessFlowIds(self):
        return self._SuccessFlowIds

    @SuccessFlowIds.setter
    def SuccessFlowIds(self, SuccessFlowIds):
        self._SuccessFlowIds = SuccessFlowIds

    @property
    def FailureFlows(self):
        return self._FailureFlows

    @FailureFlows.setter
    def FailureFlows(self, FailureFlows):
        self._FailureFlows = FailureFlows

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskStatus = params.get("TaskStatus")
        self._SuccessFlowIds = params.get("SuccessFlowIds")
        if params.get("FailureFlows") is not None:
            self._FailureFlows = []
            for item in params.get("FailureFlows"):
                obj = CancelFailureFlow()
                obj._deserialize(item)
                self._FailureFlows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeExtendedServiceAuthDetailRequest(AbstractModel):
    """DescribeExtendedServiceAuthDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _ExtendServiceType: 要查询的扩展服务类型。
如下所示：
<ul><li>OPEN_SERVER_SIGN：企业静默签署</li>
<li>BATCH_SIGN：批量签署</li>
</ul>

        :type ExtendServiceType: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Limit: 指定每页返回的数据条数，和Offset参数配合使用。 注：`1.默认值为20，单页做大值为200。`	
        :type Limit: int
        :param _Offset: 查询结果分页返回，指定从第几页返回数据，和Limit参数配合使用。 注：`1.offset从0开始，即第一页为0。` `2.默认从第一页返回。`	
        :type Offset: int
        """
        self._Operator = None
        self._ExtendServiceType = None
        self._Agent = None
        self._Limit = None
        self._Offset = None

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


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._ExtendServiceType = params.get("ExtendServiceType")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExtendedServiceAuthDetailResponse(AbstractModel):
    """DescribeExtendedServiceAuthDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AuthInfoDetail: 服务授权的信息列表，根据查询类型返回特定扩展服务的授权状况。
        :type AuthInfoDetail: :class:`tencentcloud.ess.v20201111.models.AuthInfoDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AuthInfoDetail = None
        self._RequestId = None

    @property
    def AuthInfoDetail(self):
        return self._AuthInfoDetail

    @AuthInfoDetail.setter
    def AuthInfoDetail(self, AuthInfoDetail):
        self._AuthInfoDetail = AuthInfoDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AuthInfoDetail") is not None:
            self._AuthInfoDetail = AuthInfoDetail()
            self._AuthInfoDetail._deserialize(params.get("AuthInfoDetail"))
        self._RequestId = params.get("RequestId")


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
<ul><li>OPEN_SERVER_SIGN：企业自动签署</li>
<li>AUTO_SIGN_CAN_FILL_IN：本企业自动签合同支持签前内容补充</li>
<li>BATCH_SIGN：批量签署</li>
<li>OVERSEA_SIGN：企业与港澳台居民签署合同</li>
<li>AGE_LIMIT_EXPANSION：拓宽签署方年龄限制</li>
<li>MOBILE_CHECK_APPROVER：个人签署方仅校验手机号</li>
<li>HIDE_OPERATOR_DISPLAY：隐藏合同经办人姓名</li>
<li>ORGANIZATION_OCR_FALLBACK：正楷临摹签名失败后更换其他签名类型</li>
<li>ORGANIZATION_FLOW_NOTIFY_TYPE：短信通知签署方</li>
<li>HIDE_ONE_KEY_SIGN：个人签署方手动签字</li>
<li>ORGANIZATION_FLOW_EMAIL_NOTIFY：邮件通知签署方</li>
<li>FLOW_APPROVAL：合同审批强制开启</li>
<li>ORGANIZATION_FLOW_PASSWD_NOTIFY：签署密码开通引导</li></ul>
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _BusinessType: 文件对应的业务类型，目前支持：
<ul>
<li>**FLOW ** : <font color="red">如需下载合同文件请选择此项</font></li>
<li>**TEMPLATE ** : 如需下载模板文件请选择此项</li>
<li>**DOCUMENT  **: 如需下载文档文件请选择此项</li>
<li>**SEAL  **: 如需下载印章图片请选择此项</li>
</ul>
        :type BusinessType: str
        :param _BusinessIds: 业务编号的数组，取值如下：
<ul>
<li>流程编号</li>
<li>模板编号</li>
<li>文档编号</li>
<li>印章编号</li>
<li>如需下载合同文件请传入FlowId，最大支持20个资源</li>
</ul>
        :type BusinessIds: list of str
        :param _FileName: 下载后的文件命名，只有FileType为zip的时候生效
        :type FileName: str
        :param _FileType: 要下载的文件类型，取值如下：
<ul>
<li>JPG</li>
<li>PDF</li>
<li>ZIP</li>
</ul>
        :type FileType: str
        :param _Offset: 指定分页返回第几页的数据，如果不传默认返回第一页，页码从 0 开始，即首页为 0，最大 1000。
        :type Offset: int
        :param _Limit: 指定分页每页返回的数据条数，如果不传默认为 20，单页最大支持 100。
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
链接不是永久链接,  过期时间受UrlTtl入参的影响,  默认有效期5分钟后,  到期后链接失效。
        :type FileUrls: list of FileUrl
        :param _TotalCount: URL数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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

[点击查看FlowId在控制台中的位置](https://qcloudimg.tencent-cloud.cn/raw/0a83015166cfe1cb043d14f9ec4bd75e.png)
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowId: 合同流程ID，为32位字符串。
建议开发者妥善保存此流程ID，以便于顺利进行后续操作。
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
        


class DescribeFlowComponentsResponse(AbstractModel):
    """DescribeFlowComponents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecipientComponentInfos: 合同流程关联的填写控件信息，按照参与方进行分类返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecipientComponentInfos: list of RecipientComponentInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _ReportType: 指定申请的报告类型，可选类型如下：
<ul><li> **0** :合同签署报告（默认）</li>
<li> **1** :公证处核验报告</li></ul>
        :type ReportType: int
        """
        self._Operator = None
        self._ReportId = None
        self._Agent = None
        self._ReportType = None

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

    @property
    def ReportType(self):
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._ReportId = params.get("ReportId")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._ReportType = params.get("ReportType")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Operator: 执行本接口操作的员工信息。 注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`	
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowIds: 需要查询的流程ID列表，最多可传入100个ID。
如果要查询合同组的信息，则不需要传入此参数，只需传入 FlowGroupId 参数即可。


可登录腾讯电子签控制台，在 "合同"->"合同中心" 中查看某个合同的FlowId(在页面中展示为合同ID)。

[点击查看FlowId在控制台中的位置](https://qcloudimg.tencent-cloud.cn/raw/0a83015166cfe1cb043d14f9ec4bd75e.png)
        :type FlowIds: list of str
        :param _Agent: 代理企业和员工的信息。 在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。	
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _FlowGroupId: 需要查询的流程组ID，如果传入此参数，则会忽略 FlowIds 参数。该合同组由<a href="https://qian.tencent.com/developers/companyApis/startFlows/CreateFlowGroupByFiles" target="_blank">通过多文件创建合同组签署流程</a>等接口创建。
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
        :param _FlowDetailInfos: 合同流程的详细信息。
如果查询的是合同组信息，则返回的是组内所有子合同流程的详细信息。
        :type FlowDetailInfos: list of FlowDetailInfo
        :param _FlowGroupId: 合同组ID，只有在查询合同组信息时才会返回。
        :type FlowGroupId: str
        :param _FlowGroupName: 合同组名称，只有在查询合同组信息时才会返回。
        :type FlowGroupName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _ContentType: 查询内容控制

<ul><li>**0**：模板列表及详情（默认）</li>
<li>**1**：仅模板列表</li></ul>
        :type ContentType: int
        :param _Filters: 搜索条件，本字段用于指定模板Id进行查询。
Key：template-id Values：需要查询的模板Id列表
        :type Filters: list of Filter
        :param _Offset: 查询结果分页返回，指定从第几页返回数据，和Limit参数配合使用。

注：`1.offset从0开始，即第一页为0。`
`2.默认从第一页返回。`
        :type Offset: int
        :param _Limit: 指定每页返回的数据条数，和Offset参数配合使用。

注：`1.默认值为20，单页做大值为200。`
        :type Limit: int
        :param _ApplicationId: 指定查询的应用号，指定后查询该应用号下的模板列表。

注：`1.ApplicationId为空时，查询所有应用下的模板列表。`
        :type ApplicationId: str
        :param _IsChannel: 默认为false，查询SaaS模板库列表；
为true，查询第三方应用集成平台企业模板库管理列表
        :type IsChannel: bool
        :param _Organization: 暂未开放
        :type Organization: :class:`tencentcloud.ess.v20201111.models.OrganizationInfo`
        :param _GenerateSource: 暂未开放
        :type GenerateSource: int
        :param _WithPreviewUrl: 是否获取模板预览链接
        :type WithPreviewUrl: bool
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
        self._WithPreviewUrl = None

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

    @property
    def WithPreviewUrl(self):
        return self._WithPreviewUrl

    @WithPreviewUrl.setter
    def WithPreviewUrl(self, WithPreviewUrl):
        self._WithPreviewUrl = WithPreviewUrl


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
        self._WithPreviewUrl = params.get("WithPreviewUrl")
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
        :param _Templates: 模板详情列表数据
        :type Templates: list of TemplateInfo
        :param _TotalCount: 查询到的模板总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _QueryType: 查询类型，支持以下类型：
<ul><li>**0**：查询单个部门节点列表，不包含子节点部门信息</li>
<li>**1**：查询单个部门节点级一级子节点部门信息列表</li></ul>
        :type QueryType: int
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _DeptId: 查询的部门ID。
注：`如果同时指定了DeptId与DeptOpenId参数，系统将优先使用DeptId参数进行查询。当二者都未指定时，系统将返回根节点部门数据。`
        :type DeptId: str
        :param _DeptOpenId: 查询的客户系统部门ID。
注：`如果同时指定了DeptId与DeptOpenId参数，系统将优先使用DeptId参数进行查询。当二者都未指定时，系统将返回根节点部门数据。`
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
        :param _Departments: 部门信息列表。部门信息根据部门排序号OrderNo降序排列，根据部门创建时间升序排列。
        :type Departments: list of IntegrationDepartment
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Operator: 执行本接口操作的员工信息。使用此接口时，必须填写UserId。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Limit: 指定分页每页返回的数据条数，单页最大支持 20。
        :type Limit: int
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Filters: 查询的关键字段，支持Key-Values查询。可选键值如下：
<ul>
  <li>Key:**"Status"**，根据实名状态查询员工，Values可选：
    <ul><li>**["IsVerified"]**：查询已实名的员工</li><li>**["NotVerified"]**：查询未实名的员工</li></ul></li>
  <li>Key:**"DepartmentId"**，根据部门ID查询部门下的员工，Values为指定的部门ID：**["DepartmentId"]**</li>
  <li>Key:**"UserId"**，根据用户ID查询员工，Values为指定的用户ID：**["UserId"]**</li>
  <li>Key:**"UserWeWorkOpenId"**，根据用户企微账号ID查询员工，Values为指定用户的企微账号ID：**["UserWeWorkOpenId"]**</li>
  <li>Key:**"StaffOpenId"**，根据第三方系统用户OpenId查询员工，Values为第三方系统用户OpenId列表：**["OpenId1","OpenId2",...]**</li>
  <li>Key:**"RoleId"**，根据电子签角色ID查询员工，Values为指定的角色ID，满足其中任意一个角色即可：**["RoleId1","RoleId2",...]**</li>
</ul>
        :type Filters: list of Filter
        :param _Offset: 指定分页返回第几页的数据，如果不传默认返回第一页。页码从 0 开始，即首页为 0，最大20000。
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
        :param _Employees: 员工信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Employees: list of Staff
        :param _Offset: 指定分页返回第几页的数据。页码从 0 开始，即首页为 0，最大20000。
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: int
        :param _Limit: 指定分页每页返回的数据条数，单页最大支持 20。
        :type Limit: int
        :param _TotalCount: 符合条件的员工数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Offset: OFFSET 用于指定查询结果的偏移量，如果不传默认偏移为0,最大2000。
分页参数, 需要limit, offset 配合使用
例如:
您希望得到第三页的数据, 且每页限制最多10条
您可以使用 LIMIT 10 OFFSET 20

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
        :param _Offset: OFFSET 用于指定查询结果的偏移量，如果不传默认偏移为0, 最大为2000
分页参数, 需要limit, offset 配合使用
例如:
您希望得到第三页的数据, 且每页限制最多10条
您可以使用 LIMIT 10 OFFSET 20
        :type Offset: int
        :param _Limit: 指定分页每页返回的数据条数，单页最大支持 200。
        :type Limit: int
        :param _TotalCount: 符合查询条件的总角色数。
        :type TotalCount: int
        :param _IntegrateRoles: 企业角色信息列表。
        :type IntegrateRoles: list of IntegrateRole
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Operator: 执行本接口操作的员工信息,userId必填。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Limit: 指定分页每页返回的数据条数，单页最大1000
        :type Limit: int
        :param _Offset: 指定分页返回第几页的数据，如果不传默认返回第一页，页码从 0 开始，即首页为 0
        :type Offset: int
        :param _Name: 查询成员企业的企业名，模糊匹配
        :type Name: str
        :param _Status: 成员企业加入集团的当前状态
<ul><li> **1**：待授权</li>
<li> **2**：已授权待激活</li>
<li> **3**：拒绝授权</li>
<li> **4**：已解除</li>
<li> **5**：已加入</li>
</ul>
        :type Status: int
        :param _Export: 是否导出当前成员企业数据
<ul><li> **false**：不导出（默认值）</li>
<li> **true**：导出</li></ul>
        :type Export: bool
        :param _Id: 成员企业机构 ID，32 位字符串，在PC控制台 集团管理可获取
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
        :param _Total: 符合查询条件的资源实例总数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _JoinedTotal: 已授权待激活的子企业总数量
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
        :param _ActivatedTotal: 已加入的子企业总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivatedTotal: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Limit: 指定分页每页返回的数据条数，如果不传默认为 20，单页最大支持 200。
        :type Limit: int
        :param _Offset: 指定分页返回第几页的数据，如果不传默认返回第一页，页码从 0 开始，即首页为 0，最大 20000。
        :type Offset: int
        :param _InfoType: 查询授权用户信息类型，取值如下：

<ul> <li><b>0</b>：（默认）不返回授权用户信息</li> <li><b>1</b>：返回授权用户的信息</li> </ul>
        :type InfoType: int
        :param _SealId: 印章id，是否查询特定的印章（没有输入返回所有）
        :type SealId: str
        :param _SealTypes: 印章种类列表（均为组织机构印章）。 若无特定需求，将展示所有类型的印章。 目前支持以下几种：<ul> <li><strong>OFFICIAL</strong>：企业公章；</li> <li><strong>CONTRACT</strong>：合同专用章；</li> <li><strong>ORGANIZATION_SEAL</strong>：企业印章（通过图片上传创建）；</li> <li><strong>LEGAL_PERSON_SEAL</strong>：法定代表人章。</li> <li><strong>EMPLOYEE_QUALIFICATION_SEAL</strong>：员工执业章。</li> </ul>
        :type SealTypes: list of str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _SealStatuses: 需查询的印章状态列表。
<ul>
<li>空：（默认）仅查询启用状态的印章；</li>
<li><strong>ALL</strong>：查询所有状态的印章；</li>
<li><strong>CHECKING</strong>：查询待审核的印章；</li>
<li><strong>SUCCESS</strong>：查询启用状态的印章；</li>
<li><strong>FAIL</strong>：查询印章审核拒绝的印章；</li>
<li><strong>DISABLE</strong>：查询已停用的印章；</li>
<li><strong>STOPPED</strong>：查询已终止的印章；</li>
<li><strong>VOID</strong>：查询已作废的印章；</li>
<li><strong>INVALID</strong>：查询已失效的印章。</li>
</ul>
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
        :param _TotalCount: 在设定了SealId时，返回值为0或1；若未设定SealId，则返回公司的总印章数量
        :type TotalCount: int
        :param _Seals: 查询到的印章结果数组
        :type Seals: list of OccupiedSeal
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribePersonCertificateRequest(AbstractModel):
    """DescribePersonCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _UserInfo: 个人用户的三要素信息：
<ul><li>姓名</li>
<li>证件号</li>
<li>证件类型</li></ul>
        :type UserInfo: :class:`tencentcloud.ess.v20201111.models.UserThreeFactor`
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _SceneKey: 证书使用场景，可以选择的场景值如下:
<ul><li> **E_PRESCRIPTION_AUTO_SIGN** :  电子处方场景</li><li> **OTHER** :  通用场景</li></ul>
        :type SceneKey: str
        """
        self._Operator = None
        self._UserInfo = None
        self._Agent = None
        self._SceneKey = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

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

    @property
    def SceneKey(self):
        return self._SceneKey

    @SceneKey.setter
    def SceneKey(self, SceneKey):
        self._SceneKey = SceneKey


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        if params.get("UserInfo") is not None:
            self._UserInfo = UserThreeFactor()
            self._UserInfo._deserialize(params.get("UserInfo"))
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._SceneKey = params.get("SceneKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonCertificateResponse(AbstractModel):
    """DescribePersonCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Cert: 证书的Base64
        :type Cert: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Cert = None
        self._RequestId = None

    @property
    def Cert(self):
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Cert = params.get("Cert")
        self._RequestId = params.get("RequestId")


class DescribeSignFaceVideoRequest(AbstractModel):
    """DescribeSignFaceVideo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。使用此接口时，必须填写userId。<br/>注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowId: 合同流程ID，为32位字符串。
        :type FlowId: str
        :param _SignId: 签署参与人在本流程中的编号ID(每个流程不同)，可用此ID来定位签署参与人在本流程的签署节点，也可用于后续创建签署链接等操作。
        :type SignId: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._Operator = None
        self._FlowId = None
        self._SignId = None
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
    def SignId(self):
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

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
        self._SignId = params.get("SignId")
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
        


class DescribeSignFaceVideoResponse(AbstractModel):
    """DescribeSignFaceVideo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoData: 核身视频结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoData: :class:`tencentcloud.ess.v20201111.models.DetectInfoVideoData`
        :param _IntentionQuestionResult: 意愿核身问答模式结果。若未使用该意愿核身功能，该字段返回值可以不处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentionQuestionResult: :class:`tencentcloud.ess.v20201111.models.IntentionQuestionResult`
        :param _IntentionActionResult: 意愿核身点头确认模式的结果信息，若未使用该意愿核身功能，该字段返回值可以不处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentionActionResult: :class:`tencentcloud.ess.v20201111.models.IntentionActionResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VideoData = None
        self._IntentionQuestionResult = None
        self._IntentionActionResult = None
        self._RequestId = None

    @property
    def VideoData(self):
        return self._VideoData

    @VideoData.setter
    def VideoData(self, VideoData):
        self._VideoData = VideoData

    @property
    def IntentionQuestionResult(self):
        return self._IntentionQuestionResult

    @IntentionQuestionResult.setter
    def IntentionQuestionResult(self, IntentionQuestionResult):
        self._IntentionQuestionResult = IntentionQuestionResult

    @property
    def IntentionActionResult(self):
        return self._IntentionActionResult

    @IntentionActionResult.setter
    def IntentionActionResult(self, IntentionActionResult):
        self._IntentionActionResult = IntentionActionResult

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("VideoData") is not None:
            self._VideoData = DetectInfoVideoData()
            self._VideoData._deserialize(params.get("VideoData"))
        if params.get("IntentionQuestionResult") is not None:
            self._IntentionQuestionResult = IntentionQuestionResult()
            self._IntentionQuestionResult._deserialize(params.get("IntentionQuestionResult"))
        if params.get("IntentionActionResult") is not None:
            self._IntentionActionResult = IntentionActionResult()
            self._IntentionActionResult._deserialize(params.get("IntentionActionResult"))
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
<ul><li> **E_PRESCRIPTION_AUTO_SIGN** :  电子处方场景</li><li> **OTHER** :  通用场景</li></ul>
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
        :param _LicenseType: 设置用户开通自动签时是否绑定个人自动签账号许可。<ul><li>**0**: 使用个人自动签账号许可进行开通，个人自动签账号许可有效期1年，注: `不可解绑释放更换他人`</li><li>**1**: 不绑定自动签账号许可开通，后续使用合同份额进行合同发起</li></ul>
        :type LicenseType: int
        :param _SealId: 用户开通自动签指定使用的印章，为空则未设置印章，需重新进入开通链接设置印章。
        :type SealId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsOpen = None
        self._LicenseFrom = None
        self._LicenseTo = None
        self._LicenseType = None
        self._SealId = None
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
        self._IsOpen = params.get("IsOpen")
        self._LicenseFrom = params.get("LicenseFrom")
        self._LicenseTo = params.get("LicenseTo")
        self._LicenseType = params.get("LicenseType")
        self._SealId = params.get("SealId")
        self._RequestId = params.get("RequestId")


class DescribeUserVerifyStatusRequest(AbstractModel):
    """DescribeUserVerifyStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 用户信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Name: 姓名
        :type Name: str
        :param _IdCardNumber: 证件号码，应符合以下规则
<ul><li>居民身份证号码应为18位字符串，由数字和大写字母X组成（如存在X，请大写）。</li>
<li>港澳居民来往内地通行证号码共11位。第1位为字母，“H”字头签发给香港居民，“M”字头签发给澳门居民；第2位至第11位为数字。</li>
<li>港澳台居民居住证号码编码规则与中国大陆身份证相同，应为18位字符串。</li></ul>
        :type IdCardNumber: str
        :param _IdCardType: 证件类型，支持以下类型
<ul><li>ID_CARD : 居民身份证 (默认值)</li>
<li>HONGKONG_AND_MACAO : 港澳居民来往内地通行证</li>
<li>HONGKONG_MACAO_AND_TAIWAN : 港澳台居民居住证(格式同居民身份证)</li></ul>
        :type IdCardType: str
        """
        self._Operator = None
        self._Name = None
        self._IdCardNumber = None
        self._IdCardType = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCardNumber(self):
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def IdCardType(self):
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._Name = params.get("Name")
        self._IdCardNumber = params.get("IdCardNumber")
        self._IdCardType = params.get("IdCardType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserVerifyStatusResponse(AbstractModel):
    """DescribeUserVerifyStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VerifyStatus: true:表示已实名
false：表示未实名
        :type VerifyStatus: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DetectInfoVideoData(AbstractModel):
    """视频认证结果

    """

    def __init__(self):
        r"""
        :param _LiveNessVideo: 活体视频的base64编码，mp4格式

注:`需进行base64解码获取活体视频文件`
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveNessVideo: str
        """
        self._LiveNessVideo = None

    @property
    def LiveNessVideo(self):
        return self._LiveNessVideo

    @LiveNessVideo.setter
    def LiveNessVideo(self, LiveNessVideo):
        self._LiveNessVideo = LiveNessVideo


    def _deserialize(self, params):
        self._LiveNessVideo = params.get("LiveNessVideo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableUserAutoSignRequest(AbstractModel):
    """DisableUserAutoSign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _SceneKey: 自动签使用的场景值, 可以选择的场景值如下:
<ul><li> **E_PRESCRIPTION_AUTO_SIGN** :  电子处方场景</li><li> **OTHER** :  通用场景</li></ul>
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
<ul>
<li><b>true</b>：允许在合同详情页展示控件</li>
<li><b>false</b>：（默认）不允许在合同详情页展示控件</li>
</ul>
        :type ShowFlowDetailComponent: bool
        :param _ShowTemplateComponent: 模板预览，允许展示模板控件信息
<ul><li> <b>true</b> :允许在模板预览页展示控件</li>
<li> <b>false</b> :（默认）不允许在模板预览页展示控件</li></ul>
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
<ul><li>OPEN_SERVER_SIGN：企业自动签署</li>
<li>BATCH_SIGN：批量签署</li>
<li>OVERSEA_SIGN：企业与港澳台居民签署合同</li>
<li>AGE_LIMIT_EXPANSION：拓宽签署方年龄限制</li>
<li>MOBILE_CHECK_APPROVER：个人签署方仅校验手机号</li>
<li>HIDE_OPERATOR_DISPLAY：隐藏合同经办人姓名</li>
<li>ORGANIZATION_OCR_FALLBACK：正楷临摹签名失败后更换其他签名类型</li>
<li>ORGANIZATION_FLOW_NOTIFY_TYPE：短信通知签署方</li>
<li>HIDE_ONE_KEY_SIGN：个人签署方手动签字</li>
<li>PAGING_SEAL：骑缝章</li>
<li>ORGANIZATION_FLOW_PASSWD_NOTIFY：签署密码开通引导</li></ul>
        :type Type: str
        :param _Name: 扩展服务的名称
        :type Name: str
        :param _Status: 扩展服务的开通状态：
<ul>
<li>ENABLE : 已开通</li>
<li>DISABLE : 未开通</li>
</ul>
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
        :param _Mobile: 用户传入的手机号，明文展示
        :type Mobile: str
        :param _Reason: 失败原因
        :type Reason: str
        :param _UserId: 员工在腾讯电子签平台的唯一身份标识，为32位字符串。
可登录腾讯电子签控制台，在 "更多能力"->"组织管理" 中查看某位员工的UserId(在页面中展示为用户ID)。
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
    - 补充个人签署方时，若该用户已在电子签完成实名则可通过指定姓名和证件类型、证件号码完成补充

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
        :param _OrganizationName: 补充企业动态签署人时，需要指定对应企业名称
        :type OrganizationName: str
        :param _ApproverIdCardType: 签署方经办人的证件类型，支持以下类型
<ul><li>ID_CARD 中国大陆居民身份证</li>
<li>HONGKONG_AND_MACAO 港澳居民来往内地通行证</li>
<li>HONGKONG_MACAO_AND_TAIWAN 港澳台居民居住证(格式同居民身份证)</li>
<li>OTHER_CARD_TYPE 其他证件</li></ul>

注: `1.其他证件类型为白名单功能，使用前请联系对接的客户经理沟通。`
`2.补充个人签署方时，若该用户已在电子签完成实名则可通过指定姓名和证件类型、证件号码完成补充。`
        :type ApproverIdCardType: str
        :param _ApproverIdCardNumber: 签署方经办人的证件号码，应符合以下规则
<ul><li>居民身份证号码应为18位字符串，由数字和大写字母X组成（如存在X，请大写）。</li>
<li>港澳居民来往内地通行证号码共11位。第1位为字母，“H”字头签发给香港居民，“M”字头签发给澳门居民；第2位至第11位为数字。。</li>
<li>港澳台居民居住证号码编码规则与中国大陆身份证相同，应为18位字符串。</li></ul>

注：`补充个人签署方时，若该用户已在电子签完成实名则可通过指定姓名和证件类型、证件号码完成补充。`
        :type ApproverIdCardNumber: str
        :param _FlowId: 合同流程ID，补充合同组子合同动态签署人时必传。
        :type FlowId: str
        """
        self._RecipientId = None
        self._ApproverSource = None
        self._CustomUserId = None
        self._ApproverName = None
        self._ApproverMobile = None
        self._OrganizationName = None
        self._ApproverIdCardType = None
        self._ApproverIdCardNumber = None
        self._FlowId = None

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

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

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
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._RecipientId = params.get("RecipientId")
        self._ApproverSource = params.get("ApproverSource")
        self._CustomUserId = params.get("CustomUserId")
        self._ApproverName = params.get("ApproverName")
        self._ApproverMobile = params.get("ApproverMobile")
        self._OrganizationName = params.get("OrganizationName")
        self._ApproverIdCardType = params.get("ApproverIdCardType")
        self._ApproverIdCardNumber = params.get("ApproverIdCardNumber")
        self._FlowId = params.get("FlowId")
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
        :param _ApproverRoleName: 自定义签署人角色
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproverRoleName: str
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
        self._ApproverRoleName = None

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

    @property
    def ApproverRoleName(self):
        return self._ApproverRoleName

    @ApproverRoleName.setter
    def ApproverRoleName(self, ApproverRoleName):
        self._ApproverRoleName = ApproverRoleName


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
        self._ApproverRoleName = params.get("ApproverRoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowApproverUrlInfo(AbstractModel):
    """签署链接信息。

    """

    def __init__(self):
        r"""
        :param _SignUrl: 签署短链接。
注意:
1. 该链接有效期为<b>30分钟</b>，同时需要注意保密，不要外泄给无关用户。
2. 该链接不支持小程序嵌入，仅支持<b>移动端浏览器</b>打开。
3. <font color="red">生成的链路后面不能再增加参数</font>（会出现覆盖链接中已有参数导致错误）
        :type SignUrl: str
        :param _ApproverType: 签署人类型。
- **1**: 个人
        :type ApproverType: int
        :param _ApproverName: 签署人姓名。
        :type ApproverName: str
        :param _ApproverMobile: 签署人手机号。
        :type ApproverMobile: str
        :param _LongUrl: 签署长链接。
注意:
1. 该链接有效期为**30分钟**，同时需要注意保密，不要外泄给无关用户。
2. 该链接不支持小程序嵌入，仅支持**移动端浏览器**打开。
3. <font color="red">生成的链路后面不能再增加参数</font>（会出现覆盖链接中已有参数导致错误）
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
        


class FlowBatchApproverInfo(AbstractModel):
    """批量签署合同相关信息，指定批量签署合同和签署方的信息，用于补充动态签署人。

    """

    def __init__(self):
        r"""
        :param _FlowId: 合同流程ID。
        :type FlowId: str
        :param _RecipientId: 签署节点ID，用于生成动态签署人链接完成领取。注：`生成动态签署人补充链接时必传。`
        :type RecipientId: str
        """
        self._FlowId = None
        self._RecipientId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RecipientId(self):
        return self._RecipientId

    @RecipientId.setter
    def RecipientId(self, RecipientId):
        self._RecipientId = RecipientId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RecipientId = params.get("RecipientId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowBatchUrlInfo(AbstractModel):
    """批量签署合同相关信息，指定批量签署合同和签署方的信息，用于补充动态签署人。

    """

    def __init__(self):
        r"""
        :param _FlowBatchApproverInfos: 批量签署合同和签署方的信息，用于补充动态签署人。
        :type FlowBatchApproverInfos: list of FlowBatchApproverInfo
        """
        self._FlowBatchApproverInfos = None

    @property
    def FlowBatchApproverInfos(self):
        return self._FlowBatchApproverInfos

    @FlowBatchApproverInfos.setter
    def FlowBatchApproverInfos(self, FlowBatchApproverInfos):
        self._FlowBatchApproverInfos = FlowBatchApproverInfos


    def _deserialize(self, params):
        if params.get("FlowBatchApproverInfos") is not None:
            self._FlowBatchApproverInfos = []
            for item in params.get("FlowBatchApproverInfos"):
                obj = FlowBatchApproverInfo()
                obj._deserialize(item)
                self._FlowBatchApproverInfos.append(obj)
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
        :param _ApproverType: 在指定签署方时，可以选择企业B端或个人C端等不同的参与者类型，可选类型如下：

<ul><li> <b>0</b> :企业B端。</li>
<li> <b>1</b> :个人C端。</li>
<li> <b>3</b> :企业B端静默（自动）签署，无需签署人参与，自动签署可以参考<a href="https://qian.tencent.com/developers/company/autosign_guide" target="_blank" rel="noopener noreferrer">自动签署使用说明</a>文档。</li>
<li> <b>7</b> :个人C端自动签署，适用于个人自动签场景。注: <b>个人自动签场景为白名单功能，使用前请联系对接的客户经理沟通。</b> </li></ul>
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
        :param _ApproverMobile: 签署方经办人手机号码， 支持国内手机号11位数字(无需加+86前缀或其他字符)。 此手机号用于通知和用户的实名认证等环境，请确认手机号所有方为此合同签署方。

注：`在未指定签署人电子签UserId情况下，为必填参数`

        :type ApproverMobile: str
        :param _ApproverIdCardType: 证件类型，支持以下类型
<ul><li><b>ID_CARD</b>: 居民身份证 (默认值)</li>
<li><b>HONGKONG_AND_MACAO</b> : 港澳居民来往内地通行证</li>
<li><b>HONGKONG_MACAO_AND_TAIWAN</b> : 港澳台居民居住证(格式同居民身份证)</li></ul>
        :type ApproverIdCardType: str
        :param _ApproverIdCardNumber: 证件号码，应符合以下规则
<ul><li>居民身份证号码应为18位字符串，由数字和大写字母X组成（如存在X，请大写）。</li>
<li>港澳居民来往内地通行证号码共11位。第1位为字母，“H”字头签发给香港居民，“M”字头签发给澳门居民；第2位至第11位为数字。</li>
<li>港澳台居民居住证号码编码规则与中国大陆身份证相同，应为18位字符串。</li></ul>
        :type ApproverIdCardNumber: str
        :param _RecipientId: 签署方经办人在模板中配置的参与方ID，与控件绑定，是控件的归属方，ID为32位字符串。

<b>模板发起合同时，该参数为必填项，可以通过[查询模板信息接口](https://qian.tencent.com/developers/companyApis/templatesAndFiles/DescribeFlowTemplates)获得。</b>
<b>文件发起合同时，该参数无需传值。</b>

如果开发者后续用合同模板发起合同，建议保存此值，在用合同模板发起合同中需此值绑定对应的签署经办人 。
        :type RecipientId: str
        :param _VerifyChannel: 签署意愿确认渠道，默认为WEIXINAPP:人脸识别

注: <font color="red">将要废弃</font >, `用ApproverSignTypes签署人签署合同时的认证方式代替, 新客户可请用ApproverSignTypes来设置`
        :type VerifyChannel: list of str
        :param _NotifyType: 通知签署方经办人的方式,  有以下途径:
<ul><li>  **sms**  :  (默认)短信</li>
<li>   **none**   : 不通知</li></ul>

注: `既是发起方又是签署方时，不给此签署方发送短信`
        :type NotifyType: str
        :param _IsFullText: 合同强制需要阅读全文，无需传此参数
        :type IsFullText: bool
        :param _PreReadTime: 签署方在签署合同之前，需要强制阅读合同的时长，可指定为3秒至300秒之间的任意值。

若未指定阅读时间，则会按照合同页数大小计算阅读时间，计算规则如下：
<ul>
<li>合同页数少于等于2页，阅读时间为3秒；</li>
<li>合同页数为3到5页，阅读时间为5秒；</li>
<li>合同页数大于等于6页，阅读时间为10秒。</li>
</ul>
        :type PreReadTime: int
        :param _UserId: 签署人userId，仅支持本企业的员工userid， 可在控制台组织管理处获得

注： 
如果传进来的<font color="red">UserId已经实名， 则忽略ApproverName，ApproverIdCardType，ApproverIdCardNumber，ApproverMobile这四个入参</font>（会用此UserId实名的身份证和登录的手机号覆盖）
        :type UserId: str
        :param _Required: <font color="red">字段已经废弃</font>，当前只支持true，默认为true
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
        :param _ApproverOption: 签署人个性化能力值，如是否可以转发他人处理、是否可以拒签、是否为动态补充签署人等功能开关。
        :type ApproverOption: :class:`tencentcloud.ess.v20201111.models.ApproverOption`
        :param _JumpUrl: 签署完前端跳转的url，暂未使用
        :type JumpUrl: str
        :param _SignId: 签署人的签署ID

<ul>
<li>在CreateFlow、CreatePrepareFlow等发起流程时不需要传入此参数，电子签后台系统会自动生成。</li>
<li>在CreateFlowSignUrl、CreateBatchQuickSignUrl等生成签署链接时，可以通过查询详情接口获取签署人的SignId，然后可以将此值传入，为该签署人创建签署链接。这样可以避免重复传输姓名、手机号、证件号等其他信息。</li>
</ul>
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
        :param _ComponentLimitType: 当签署方控件类型为 <b>SIGN_SIGNATURE</b> 时，可以指定签署方签名方式。如果不指定，签署人可以使用所有的签名类型，可指定的签名类型包括：

<ul><li> <b>HANDWRITE</b> :需要实时手写的手写签名。</li>
<li> <b>HANDWRITTEN_ESIGN</b> :长效手写签名， 是使用保存到个人中心的印章列表的手写签名。(并且包含HANDWRITE)</li>
<li> <b>OCR_ESIGN</b> :AI智能识别手写签名。</li>
<li> <b>ESIGN</b> :个人印章类型。</li>
<li> <b>IMG_ESIGN</b>  : 图片印章。该类型支持用户在签署将上传的PNG格式的图片作为签名。</li>
<li> <b>SYSTEM_ESIGN</b> :系统签名。该类型可以在用户签署时根据用户姓名一键生成一个签名来进行签署。</li></ul>

各种签名的样式可以参考下图：
![image](https://qcloudimg.tencent-cloud.cn/raw/ee0498856c060c065628a0c5ba780d6b.jpg)
        :type ComponentLimitType: list of str
        :param _ApproverVerifyTypes: 指定个人签署方查看合同的校验方式,可以传值如下:
<ul><li>  **1**   : （默认）人脸识别,人脸识别后才能合同内容</li>
<li>  **2**  : 手机号验证, 用户手机号和参与方手机号(ApproverMobile)相同即可查看合同内容（当手写签名方式为OCR_ESIGN时，该校验方式无效，因为这种签名方式依赖实名认证）
</li></ul>
注: 
<ul><li>如果合同流程设置ApproverVerifyType查看合同的校验方式,    则忽略此签署人的查看合同的校验方式</li>
<li>此字段可传多个校验方式</li></ul>

`此参数仅针对文件发起设置生效,模板发起合同签署流程, 请以模板配置为主`

.
        :type ApproverVerifyTypes: list of int
        :param _ApproverSignTypes: 您可以指定签署方签署合同的认证校验方式，可传递以下值：
<ul><li>**1**：人脸认证，需进行人脸识别成功后才能签署合同；</li>
<li>**2**：签署密码，需输入与用户在腾讯电子签设置的密码一致才能校验成功进行合同签署；</li>
<li>**3**：运营商三要素，需到运营商处比对手机号实名信息（名字、手机号、证件号）校验一致才能成功进行合同签署。（如果是港澳台客户，建议不要选择这个）</li>
<li>**5**：设备指纹识别，需要对比手机机主预留的指纹信息，校验一致才能成功进行合同签署。（iOS系统暂不支持该校验方式）</li>
<li>**6**：设备面容识别，需要对比手机机主预留的人脸信息，校验一致才能成功进行合同签署。（Android系统暂不支持该校验方式）</li></ul>

注：
<ul><li>默认情况下，认证校验方式为人脸认证和签署密码两种形式；</li>
<li>您可以传递多种值，表示可用多种认证校验方式。</li>
<li>校验方式不允许只包含设备指纹识别和设备面容识别，至少需要再增加一种其他校验方式。</li>
<li>设备指纹识别和设备面容识别只支持小程序使用，其他端暂不支持。</li></ul>

注:
`此参数仅针对文件发起设置生效,模板发起合同签署流程, 请以模板配置为主`
        :type ApproverSignTypes: list of int non-negative
        :param _SignTypeSelector: 生成H5签署链接时，您可以指定签署方签署合同的认证校验方式的选择模式，可传递一下值：
<ul><li>**0**：签署方自行选择，签署方可以从预先指定的认证方式中自由选择；</li>
<li>**1**：自动按顺序首位推荐，签署方无需选择，系统会优先推荐使用第一种认证方式。</li></ul>
注：
`不指定该值时，默认为签署方自行选择。`
        :type SignTypeSelector: int
        :param _Deadline: 签署人的签署截止时间，格式为Unix标准时间戳（秒）, 超过此时间未签署的合同变成已过期状态，不能在继续签署

注: `若不设置此参数，则默认使用合同的截止时间，此参数暂不支持合同组子合同`
        :type Deadline: int
        :param _Intention: 视频核身意图配置，可指定问答模式或者点头模式的语音文本。

注:
 `1.视频认证为白名单功能，使用前请联系对接的客户经理沟通。`
`2.使用视频认证必须指定签署认证方式为人脸（即ApproverSignTypes）。`
        :type Intention: :class:`tencentcloud.ess.v20201111.models.Intention`
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
        self._SignTypeSelector = None
        self._Deadline = None
        self._Intention = None

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

    @property
    def SignTypeSelector(self):
        return self._SignTypeSelector

    @SignTypeSelector.setter
    def SignTypeSelector(self, SignTypeSelector):
        self._SignTypeSelector = SignTypeSelector

    @property
    def Deadline(self):
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def Intention(self):
        return self._Intention

    @Intention.setter
    def Intention(self, Intention):
        self._Intention = Intention


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
        self._SignTypeSelector = params.get("SignTypeSelector")
        self._Deadline = params.get("Deadline")
        if params.get("Intention") is not None:
            self._Intention = Intention()
            self._Intention._deserialize(params.get("Intention"))
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
        :param _FlowId: 合同流程ID，为32位字符串。
        :type FlowId: str
        :param _FlowName: 合同流程的名称（可自定义此名称），长度不能超过200，只能由中文、字母、数字和下划线组成。
        :type FlowName: str
        :param _FlowType: 合同流程的类别分类（如销售合同/入职合同等）。	
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowType: str
        :param _FlowStatus: 合同流程当前的签署状态, 会存在下列的状态值 <ul><li> **0** : 未开启流程(合同中不存在填写环节)</li> <li> **1** : 待签署</li> <li> **2** : 部分签署</li> <li> **3** : 已拒签</li> <li> **4** : 已签署</li> <li> **5** : 已过期</li> <li> **6** : 已撤销</li> <li> **7** : 未开启流程(合同中存在填写环节)</li> <li> **8** : 等待填写</li> <li> **9** : 部分填写</li> <li> **10** : 已拒填</li> <li> **21** : 已解除</li></ul>	
        :type FlowStatus: int
        :param _FlowMessage: 当合同流程状态为已拒签（即 FlowStatus=3）或已撤销（即 FlowStatus=6）时，此字段 FlowMessage 为拒签或撤销原因。	
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowMessage: str
        :param _FlowDescription: 合同流程描述信息。	
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowDescription: str
        :param _CreatedOn: 合同流程的创建时间戳，格式为Unix标准时间戳（秒）。	
        :type CreatedOn: int
        :param _FlowApproverInfos: 合同流程的签署方数组
        :type FlowApproverInfos: list of FlowApproverDetail
        :param _CcInfos: 合同流程的关注方信息数组
        :type CcInfos: list of FlowApproverDetail
        :param _Creator: 合同流程发起方的员工编号, 即员工在腾讯电子签平台的唯一身份标识。	
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
        


class FlowGroupApproverInfo(AbstractModel):
    """合同组相关信息，指定合同组子合同和签署方的信息，用于补充动态签署人。

    """

    def __init__(self):
        r"""
        :param _FlowId: 合同流程ID。
        :type FlowId: str
        :param _RecipientId: 签署节点ID，用于生成动态签署人链接完成领取。注：`生成动态签署人补充链接时必传。`
        :type RecipientId: str
        """
        self._FlowId = None
        self._RecipientId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RecipientId(self):
        return self._RecipientId

    @RecipientId.setter
    def RecipientId(self, RecipientId):
        self._RecipientId = RecipientId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RecipientId = params.get("RecipientId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowGroupApprovers(AbstractModel):
    """合同组签署方信息

    """

    def __init__(self):
        r"""
        :param _FlowId: 合同流程ID 
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: str
        :param _Approvers: 签署方信息，包含合同ID和角色ID用于定位RecipientId。
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
        


class FlowGroupUrlInfo(AbstractModel):
    """合同组相关信息，指定合同组子合同和签署方的信息，用于补充动态签署人。

    """

    def __init__(self):
        r"""
        :param _FlowGroupApproverInfos: 合同组子合同和签署方的信息，用于补充动态签署人。
        :type FlowGroupApproverInfos: list of FlowGroupApproverInfo
        """
        self._FlowGroupApproverInfos = None

    @property
    def FlowGroupApproverInfos(self):
        return self._FlowGroupApproverInfos

    @FlowGroupApproverInfos.setter
    def FlowGroupApproverInfos(self, FlowGroupApproverInfos):
        self._FlowGroupApproverInfos = FlowGroupApproverInfos


    def _deserialize(self, params):
        if params.get("FlowGroupApproverInfos") is not None:
            self._FlowGroupApproverInfos = []
            for item in params.get("FlowGroupApproverInfos"):
                obj = FlowGroupApproverInfo()
                obj._deserialize(item)
                self._FlowGroupApproverInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FormField(AbstractModel):
    """电子文档的控件填充信息。按照控件类型进行相应的填充。

    当控件的 ComponentType=‘SIGN_SEAL'时，FormField.ComponentValue填入印章id。

    * 可用于指定自动签模板未设置自动签印章时，可由接口传入自动签印章
    * 若指定的控件上已设置ComponentValue，那以已经设置的ComponentValue为准

    ```
    FormField输入示例：
    {
        "ComponentId": "componentId1",
        "ComponentValue": "sealId（印章id）"
    }
    ```

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

    当控件的 ComponentType='ATTACHMENT'时，FormField.ComponentValue支持填入附件图片或者文件的资源ID列表，以逗号分隔，单个附件控件最多支持6个资源ID；
    支持的文件类型包括doc、docx、xls、xlsx、html、jpg、jpeg、png、bmp、txt、pdf

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

    输入示例3（表格设置字体加粗颜色）：

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
                    "content":"123",
                    "style": {"color": "#b50000", "fontSize": 12,"bold": true,"align": "CENTER"}
                },
                {
                    "rowStart":2,
                    "rowEnd":3,
                    "columnStart":1,
                    "columnEnd":2,
                    "content":"456",
                    "style": {"color": "#b50000", "fontSize": 12,"bold": true,"align": "LEFT"}
                },
                {
                    "rowStart":3,
                    "rowEnd":3,
                    "columnStart":3,
                    "columnEnd":3,
                    "content":"789",
                    "style": {"color": "#b500bf", "fontSize": 12,"bold": false,"align": "RIGHT"}
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
    | cells.N.style         | String  | 单元格字体风格配置 ，风格配置的json字符串  如： {"font":"黑体","fontSize":12,"color":"#FFFFFF","bold":true,"align":"CENTER"}      |

    表格参数headers说明
    widthPercent Integer 表头单元格列占总表头的比例，例如1：30表示 此列占表头的30%，不填写时列宽度平均拆分；例如2：总2列，某一列填写40，剩余列可以为空，按照60计算。；例如3：总3列，某一列填写30，剩余2列可以为空，分别为(100-30)/2=35

    content String 表头单元格内容，字数不超过100


    style String 为字体风格设置 风格支持： font : 目前支持 黑体、宋体; fontSize： 6-72; color：000000-FFFFFF  字符串形如：  "#FFFFFF" 或者 "0xFFFFFF"; bold ： 是否加粗， true ： 加粗 false： 不加粗; align: 对其方式， 支持 LEFT / RIGHT / CENTER

    """

    def __init__(self):
        r"""
        :param _ComponentValue: 控件填充vaule，ComponentType和传入值类型对应关系：
<ul><li> <b>TEXT</b> : 文本内容</li>
<li> <b>MULTI_LINE_TEXT</b> : 文本内容， 可以用  \n 来控制换行位置</li>
<li> <b>CHECK_BOX</b> : true/false</li>
<li> <b>FILL_IMAGE、ATTACHMENT</b> : 附件的FileId，需要通过UploadFiles接口上传获取</li>
<li> <b>SELECTOR</b> : 选项值</li>
<li> <b>DYNAMIC_TABLE</b>  - 传入json格式的表格内容，详见说明：[数据表格](https://qian.tencent.com/developers/company/dynamic_table)</li>
<li> <b>DATE</b> : 格式化：xxxx年xx月xx日（例如：2024年05月28日）</li>
</ul>


<b>控件值约束说明</b>：
<table> <thead> <tr> <th>特殊控件</th> <th>填写约束</th> </tr> </thead> <tbody> <tr> <td>企业全称控件</td> <td>企业名称中文字符中文括号</td> </tr> <tr> <td>统一社会信用代码控件</td> <td>企业注册的统一社会信用代码</td> </tr> <tr> <td>法人名称控件</td> <td>最大50个字符，2到25个汉字或者1到50个字母</td> </tr> <tr> <td>签署意见控件</td> <td>签署意见最大长度为50字符</td> </tr> <tr> <td>签署人手机号控件</td> <td>国内手机号 13,14,15,16,17,18,19号段长度11位</td> </tr> <tr> <td>签署人身份证控件</td> <td>合法的身份证号码检查</td> </tr> <tr> <td>控件名称</td> <td>控件名称最大长度为20字符，不支持表情</td> </tr> <tr> <td>单行文本控件</td> <td>只允许输入中文，英文，数字，中英文标点符号，不支持表情</td> </tr> <tr> <td>多行文本控件</td> <td>只允许输入中文，英文，数字，中英文标点符号，不支持表情</td> </tr> <tr> <td>勾选框控件</td> <td>选择填字符串true，不选填字符串false</td> </tr> <tr> <td>选择器控件</td> <td>同单行文本控件约束，填写选择值中的字符串</td> </tr> <tr> <td>数字控件</td> <td>请输入有效的数字(可带小数点)</td> </tr> <tr> <td>日期控件</td> <td>格式：yyyy年mm月dd日</td> </tr> <tr> <td>附件控件</td> <td>JPG或PNG图片，上传数量限制，1到6个，最大6个附件，填写上传的资源ID</td> </tr> <tr> <td>图片控件</td> <td>JPG或PNG图片，填写上传的图片资源ID</td> </tr> <tr> <td>邮箱控件</td> <td>有效的邮箱地址, w3c标准</td> </tr> <tr> <td>地址控件</td> <td>只允许输入中文，英文，数字，中英文标点符号，不支持表情</td> </tr> <tr> <td>省市区控件</td> <td>只允许输入中文，英文，数字，中英文标点符号，不支持表情</td> </tr> <tr> <td>性别控件</td> <td>选择值中的字符串</td> </tr> <tr> <td>学历控件</td> <td>选择值中的字符串</td> </tr> </tbody> </table>

        :type ComponentValue: str
        :param _ComponentId: 控件id，和ComponentName选择一项传入即可

<a href="https://dyn.ess.tencent.cn/guide/apivideo/component_name.mp4" target="_blank">点击查看在模板中找到控件ID的方式</a>
        :type ComponentId: str
        :param _ComponentName: 控件名字，最大长度不超过30字符，和ComponentId选择一项传入即可

<a href="https://dyn.ess.tencent.cn/guide/apivideo/component_name.mp4" target="_blank">点击查看在模板中找到控件名字的方式</a>
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
        :param _TaskId: 转换任务Id，通过接口<a href="https://qian.tencent.com/developers/companyApis/templatesAndFiles/CreateConvertTaskApi" target="_blank">创建文件转换任务接口</a>或<a href="https://qian.tencent.com/developers/companyApis/templatesAndFiles/CreateMergeFileTask" target="_blank">创建多文件转换任务接口</a>
得到的转换任务id
        :type TaskId: str
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
<ul><li>**0**  :NeedTranform   - 任务已提交</li>
<li>**4**  :Processing     - 文档转换中</li>
<li>**8**  :TaskEnd        - 任务处理完成</li>
<li>**-2** :DownloadFailed - 下载失败</li>
<li>**-6** :ProcessFailed  - 转换失败</li>
<li>**-13**:ProcessTimeout - 转换文件超时</li></ul>
        :type TaskStatus: int
        :param _TaskMessage: 状态描述，需要关注的状态
<ul><li> **NeedTranform** : 任务已提交</li>
<li> **Processing** : 文档转换中</li>
<li> **TaskEnd** : 任务处理完成</li>
<li> **DownloadFailed** : 下载失败</li>
<li> **ProcessFailed** : 转换失败</li>
<li> **ProcessTimeout** : 转换文件超时</li></ul>
        :type TaskMessage: str
        :param _ResourceId: 资源Id（即FileId），用于[用PDF文件创建签署流程](https://qian.tencent.com/developers/companyApis/startFlows/CreateFlowByFiles)
        :type ResourceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _OrganizationId: 成员企业id，为 32 位字符串，可在电子签PC 控制台，企业设置->企业电子签账号 获取
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationId: str
        :param _UpdateTime: 记录更新时间， unix时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param _Status: 成员企业加入集团的当前状态
<ul><li> **1**：待授权</li>
<li> **2**：已授权待激活</li>
<li> **3**：拒绝授权</li>
<li> **4**：已解除</li>
<li> **5**：已加入</li>
</ul>

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
        :param _License: 企业许可证Id，此字段暂时不需要关注
注意：此字段可能返回 null，表示取不到有效值。
        :type License: str
        :param _LicenseExpireTime: 企业许可证过期时间，unix时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseExpireTime: int
        :param _JoinTime: 成员企业加入集团时间，unix时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type JoinTime: int
        :param _FlowEngineEnable: 是否使用自建审批流引擎（即不是企微审批流引擎）
<ul><li> **true**：是</li>
<li> **false**：否</li></ul>
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
        


class HasAuthOrganization(AbstractModel):
    """授权企业列表（目前仅用于“企业自动签 -> 合作企业授权”）

    """

    def __init__(self):
        r"""
        :param _OrganizationId: 授权企业id
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationId: str
        :param _OrganizationName: 授权企业名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationName: str
        :param _AuthorizedOrganizationId: 被授权企业id
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizedOrganizationId: str
        :param _AuthorizedOrganizationName: 被授权企业名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizedOrganizationName: str
        :param _TemplateId: 授权模板id（仅当授权方式为模板授权时有值）
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param _TemplateName: 授权模板名称（仅当授权方式为模板授权时有值）
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateName: str
        :param _AuthorizeTime: 授权时间，格式为时间戳，单位s
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizeTime: int
        """
        self._OrganizationId = None
        self._OrganizationName = None
        self._AuthorizedOrganizationId = None
        self._AuthorizedOrganizationName = None
        self._TemplateId = None
        self._TemplateName = None
        self._AuthorizeTime = None

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
    def AuthorizedOrganizationId(self):
        return self._AuthorizedOrganizationId

    @AuthorizedOrganizationId.setter
    def AuthorizedOrganizationId(self, AuthorizedOrganizationId):
        self._AuthorizedOrganizationId = AuthorizedOrganizationId

    @property
    def AuthorizedOrganizationName(self):
        return self._AuthorizedOrganizationName

    @AuthorizedOrganizationName.setter
    def AuthorizedOrganizationName(self, AuthorizedOrganizationName):
        self._AuthorizedOrganizationName = AuthorizedOrganizationName

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
    def AuthorizeTime(self):
        return self._AuthorizeTime

    @AuthorizeTime.setter
    def AuthorizeTime(self, AuthorizeTime):
        self._AuthorizeTime = AuthorizeTime


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        self._OrganizationName = params.get("OrganizationName")
        self._AuthorizedOrganizationId = params.get("AuthorizedOrganizationId")
        self._AuthorizedOrganizationName = params.get("AuthorizedOrganizationName")
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._AuthorizeTime = params.get("AuthorizeTime")
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
        :param _MainOrganizationId: 集团主企业id，当前企业为集团子企业时，该字段有值
注意：此字段可能返回 null，表示取不到有效值。
        :type MainOrganizationId: str
        """
        self._UserId = None
        self._BelongTo = None
        self._MainOrganizationId = None

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

    @property
    def MainOrganizationId(self):
        return self._MainOrganizationId

    @MainOrganizationId.setter
    def MainOrganizationId(self, MainOrganizationId):
        self._MainOrganizationId = MainOrganizationId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._BelongTo = params.get("BelongTo")
        self._MainOrganizationId = params.get("MainOrganizationId")
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
        :param _DeptId: 部门ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeptId: str
        :param _DeptName: 部门名。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeptName: str
        :param _ParentDeptId: 父部门ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentDeptId: str
        :param _DeptOpenId: 客户系统部门ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeptOpenId: str
        :param _OrderNo: 序列号。
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
        


class Intention(AbstractModel):
    """视频核身意图配置，可指定问答模式或者点头模式的语音文本。

    注: `视频认证为白名单功能，使用前请联系对接的客户经理沟通。`

    """

    def __init__(self):
        r"""
        :param _IntentionType: 视频认证类型，支持以下类型
<ul><li>1 : 问答模式</li>
<li>2 : 点头模式</li></ul>

注: `视频认证为白名单功能，使用前请联系对接的客户经理沟通。`
        :type IntentionType: int
        :param _IntentionQuestions: 意愿核身语音问答模式（即语音播报+语音回答）使用的文案，包括：系统语音播报的文本、需要核验的标准文本。当前仅支持1轮问答。

注：`选择问答模式时，此字段可不传，不传则使用默认语音文本：请问，您是否同意签署本协议？可语音回复“同意”或“不同意”。`
        :type IntentionQuestions: list of IntentionQuestion
        :param _IntentionActions: 意愿核身（点头确认模式）使用的文案，若未使用意愿核身（点头确认模式），则该字段无需传入。当前仅支持一个提示文本。

注：`选择点头模式时，此字段可不传，不传则使用默认语音文本：请问，您是否同意签署本协议？可点头同意。`
        :type IntentionActions: list of IntentionAction
        """
        self._IntentionType = None
        self._IntentionQuestions = None
        self._IntentionActions = None

    @property
    def IntentionType(self):
        return self._IntentionType

    @IntentionType.setter
    def IntentionType(self, IntentionType):
        self._IntentionType = IntentionType

    @property
    def IntentionQuestions(self):
        return self._IntentionQuestions

    @IntentionQuestions.setter
    def IntentionQuestions(self, IntentionQuestions):
        self._IntentionQuestions = IntentionQuestions

    @property
    def IntentionActions(self):
        return self._IntentionActions

    @IntentionActions.setter
    def IntentionActions(self, IntentionActions):
        self._IntentionActions = IntentionActions


    def _deserialize(self, params):
        self._IntentionType = params.get("IntentionType")
        if params.get("IntentionQuestions") is not None:
            self._IntentionQuestions = []
            for item in params.get("IntentionQuestions"):
                obj = IntentionQuestion()
                obj._deserialize(item)
                self._IntentionQuestions.append(obj)
        if params.get("IntentionActions") is not None:
            self._IntentionActions = []
            for item in params.get("IntentionActions"):
                obj = IntentionAction()
                obj._deserialize(item)
                self._IntentionActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntentionAction(AbstractModel):
    """意愿核身（点头确认模式）使用的文案，若未使用意愿核身（点头确认模式），则该字段无需传入。当前仅支持一个提示文本。

    """

    def __init__(self):
        r"""
        :param _Text: 点头确认模式下，系统语音播报使用的问题文本，问题最大长度为150个字符。
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntentionActionResult(AbstractModel):
    """意愿核身点头确认模式结果

    """

    def __init__(self):
        r"""
        :param _Details: 意愿核身结果详细数据，与每段点头确认过程一一对应
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of IntentionActionResultDetail
        """
        self._Details = None

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = IntentionActionResultDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntentionActionResultDetail(AbstractModel):
    """意愿核身点头确认模式结果详细数据

    """

    def __init__(self):
        r"""
        :param _Video: 视频base64编码（其中包含全程提示文本和点头音频，mp4格式）
注意：此字段可能返回 null，表示取不到有效值。
        :type Video: str
        """
        self._Video = None

    @property
    def Video(self):
        return self._Video

    @Video.setter
    def Video(self, Video):
        self._Video = Video


    def _deserialize(self, params):
        self._Video = params.get("Video")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntentionQuestion(AbstractModel):
    """意愿核身语音问答模式（即语音播报+语音回答）使用的文案，包括：系统语音播报的文本、需要核验的标准文本。当前仅支持1轮问答。

    """

    def __init__(self):
        r"""
        :param _Question: 当选择语音问答模式时，系统自动播报的问题文本，最大长度为150个字符。
        :type Question: str
        :param _Answers:  当选择语音问答模式时，用于判断用户回答是否通过的标准答案列表，传入后可自动判断用户回答文本是否在标准文本列表中。
        :type Answers: list of str
        """
        self._Question = None
        self._Answers = None

    @property
    def Question(self):
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answers(self):
        return self._Answers

    @Answers.setter
    def Answers(self, Answers):
        self._Answers = Answers


    def _deserialize(self, params):
        self._Question = params.get("Question")
        self._Answers = params.get("Answers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntentionQuestionResult(AbstractModel):
    """意愿核身问答模式结果。若未使用该意愿核身功能，该字段返回值可以不处理。

    """

    def __init__(self):
        r"""
        :param _Video: 视频base64（其中包含全程问题和回答音频，mp4格式）

注：`需进行base64解码获取视频文件`
注意：此字段可能返回 null，表示取不到有效值。
        :type Video: str
        :param _ResultCode:  和答案匹配结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultCode: list of str
        :param _AsrResult: 回答问题语音识别结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrResult: list of str
        """
        self._Video = None
        self._ResultCode = None
        self._AsrResult = None

    @property
    def Video(self):
        return self._Video

    @Video.setter
    def Video(self, Video):
        self._Video = Video

    @property
    def ResultCode(self):
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def AsrResult(self):
        return self._AsrResult

    @AsrResult.setter
    def AsrResult(self, AsrResult):
        self._AsrResult = AsrResult


    def _deserialize(self, params):
        self._Video = params.get("Video")
        self._ResultCode = params.get("ResultCode")
        self._AsrResult = params.get("AsrResult")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyExtendedServiceRequest(AbstractModel):
    """ModifyExtendedService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _ServiceType: 要管理的拓展服务类型。
<ul><li>OPEN_SERVER_SIGN：企业自动签署</li>
<li>AUTO_SIGN_CAN_FILL_IN：本企业自动签合同支持签前内容补充</li>
<li>OVERSEA_SIGN：企业与港澳台居民签署合同</li>
<li>AGE_LIMIT_EXPANSION：拓宽签署方年龄限制</li>
<li>MOBILE_CHECK_APPROVER：个人签署方仅校验手机号</li>
<li>HIDE_OPERATOR_DISPLAY：隐藏合同经办人姓名</li>
<li>ORGANIZATION_OCR_FALLBACK：正楷临摹签名失败后更换其他签名类型</li>
<li>ORGANIZATION_FLOW_NOTIFY_TYPE：短信通知签署方</li>
<li>HIDE_ONE_KEY_SIGN：个人签署方手动签字</li>
<li>ORGANIZATION_FLOW_EMAIL_NOTIFY：邮件通知签署方</li>
<li>FLOW_APPROVAL：合同审批强制开启</li>
<li>ORGANIZATION_FLOW_PASSWD_NOTIFY：签署密码开通引导</li></ul>
        :type ServiceType: str
        :param _Operate: 操作类型
<ul>
<li>OPEN : 开通</li>
<li>CLOSE : 关闭</li>
</ul>
        :type Operate: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _Endpoint: 链接跳转类型，支持以下类型
<ul>
<li>WEIXINAPP : 短链直接跳转到电子签小程序  (默认值)</li>
<li>APP : 第三方APP或小程序跳转电子签小程序</li>
</ul>
        :type Endpoint: str
        """
        self._Operator = None
        self._ServiceType = None
        self._Operate = None
        self._Agent = None
        self._Endpoint = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

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
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._ServiceType = params.get("ServiceType")
        self._Operate = params.get("Operate")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
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

当操作类型是 OPEN 且 扩展服务类型是  OPEN_SERVER_SIGN 或者 OVERSEA_SIGN 时返回操作链接，
返回的链接当前操作人（超管或法人）点击链接完成服务开通操作。
        :type OperateUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyFlowDeadlineRequest(AbstractModel):
    """ModifyFlowDeadline请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _FlowId: 合同流程ID，为32位字符串。
<ul><li>建议开发者妥善保存此流程ID，以便于顺利进行后续操作。</li>
<li>可登录腾讯电子签控制台，在 "合同"->"合同中心" 中查看某个合同的FlowId(在页面中展示为合同ID)。</li></ul>
        :type FlowId: str
        :param _Deadline: 签署流程或签署人新的签署截止时间，格式为Unix标准时间戳（秒）
        :type Deadline: int
        :param _Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _RecipientId: 签署方角色编号，为32位字符串
<ul><li>若指定了此参数，则只调整签署流程中此签署人的签署截止时间，否则调整合同整体的签署截止时间（合同截止时间+发起时未设置签署人截止时间的参与人的签署截止时间）</li>
<li>通过[用PDF文件创建签署流程](https://qian.tencent.com/developers/companyApis/startFlows/CreateFlowByFiles)发起合同，或通过[模板发起合同-创建电子文档](https://qian.tencent.com/developers/companyApis/startFlows/CreateDocument)时，返回参数[Approvers](https://qian.tencent.com/developers/companyApis/dataTypes/#approveritem)会返回此信息，建议开发者妥善保存</li>
<li>也可通过[查询合同流程的详情信息](https://qian.tencent.com/developers/companyApis/queryFlows/DescribeFlowInfo)接口查询签署人的RecipientId编号</li></ul>
        :type RecipientId: str
        """
        self._Operator = None
        self._FlowId = None
        self._Deadline = None
        self._Agent = None
        self._RecipientId = None

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

    @property
    def RecipientId(self):
        return self._RecipientId

    @RecipientId.setter
    def RecipientId(self, RecipientId):
        self._RecipientId = RecipientId


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self._Operator = UserInfo()
            self._Operator._deserialize(params.get("Operator"))
        self._FlowId = params.get("FlowId")
        self._Deadline = params.get("Deadline")
        if params.get("Agent") is not None:
            self._Agent = Agent()
            self._Agent._deserialize(params.get("Agent"))
        self._RecipientId = params.get("RecipientId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFlowDeadlineResponse(AbstractModel):
    """ModifyFlowDeadline返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _DeptId: 电子签部门ID，通过<a href="https://qian.tencent.com/developers/companyApis/organizations/DescribeIntegrationDepartments" target="_blank">DescribeIntegrationDepartments</a>接口获得。
        :type DeptId: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _ParentDeptId: 电子签父部门ID，通过<a href="https://qian.tencent.com/developers/companyApis/organizations/DescribeIntegrationDepartments" target="_blank">DescribeIntegrationDepartments</a>接口获得。
        :type ParentDeptId: str
        :param _DeptName: 部门名称，最大长度为50个字符。
        :type DeptName: str
        :param _DeptOpenId: 客户系统部门ID，最大长度为64个字符。
        :type DeptOpenId: str
        :param _OrderNo: 排序号，支持设置的数值范围为1~30000。同一父部门下，排序号越大，部门顺序越靠前。
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class NeedReviewApproverInfo(AbstractModel):
    """需要进行签署审核的签署人信息

    """

    def __init__(self):
        r"""
        :param _ApproverType: 签署方经办人的类型，支持以下类型
<ul><li> ORGANIZATION 企业（含企业自动签）</li>
<li>PERSON 个人（含个人自动签）</li></ul>
        :type ApproverType: str
        :param _ApproverName: 签署方经办人的姓名。 经办人的姓名将用于身份认证和电子签名，请确保填写的姓名为签署方的真实姓名，而非昵称等代名。
        :type ApproverName: str
        :param _ApproverMobile: 签署方经办人手机号码， 支持国内手机号11位数字(无需加+86前缀或其他字符)。 请确认手机号所有方为此合同签署方。
        :type ApproverMobile: str
        :param _ApproverIdCardType: 签署方经办人的证件类型，支持以下类型
<ul><li>ID_CARD 中国大陆居民身份证  (默认值)</li>
<li>HONGKONG_AND_MACAO 港澳居民来往内地通行证</li>
<li>HONGKONG_MACAO_AND_TAIWAN 港澳台居民居住证(格式同居民身份证)</li>
<li>OTHER_CARD_TYPE 其他证件</li></ul>

注: `其他证件类型为白名单功能，使用前请联系对接的客户经理沟通。`
        :type ApproverIdCardType: str
        :param _ApproverIdCardNumber: 签署方经办人的证件号码，应符合以下规则
<ul><li>居民身份证号码应为18位字符串，由数字和大写字母X组成（如存在X，请大写）。</li>
<li>港澳居民来往内地通行证号码共11位。第1位为字母，“H”字头签发给香港居民，“M”字头签发给澳门居民；第2位至第11位为数字。</li>
<li>港澳台居民居住证号码编码规则与中国大陆身份证相同，应为18位字符串。</li></ul>
        :type ApproverIdCardNumber: str
        :param _OrganizationName: 组织机构名称。
请确认该名称与企业营业执照中注册的名称一致。
如果名称中包含英文括号()，请使用中文括号（）代替。
如果签署方是企业签署方(approverType = 0 或者 approverType = 3)， 则企业名称必填。

        :type OrganizationName: str
        """
        self._ApproverType = None
        self._ApproverName = None
        self._ApproverMobile = None
        self._ApproverIdCardType = None
        self._ApproverIdCardNumber = None
        self._OrganizationName = None

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
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName


    def _deserialize(self, params):
        self._ApproverType = params.get("ApproverType")
        self._ApproverName = params.get("ApproverName")
        self._ApproverMobile = params.get("ApproverMobile")
        self._ApproverIdCardType = params.get("ApproverIdCardType")
        self._ApproverIdCardNumber = params.get("ApproverIdCardNumber")
        self._OrganizationName = params.get("OrganizationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class OrgBillSummary(AbstractModel):
    """企业套餐余额情况

    """

    def __init__(self):
        r"""
        :param _Total: 套餐总数
        :type Total: int
        :param _Used: 套餐使用数
        :type Used: int
        :param _Available: 套餐剩余数
        :type Available: int
        :param _QuotaType: 套餐类型
对应关系如下:
<ul>
<li>**CloudEnterprise**: 企业版合同</li>
<li>**SingleSignature**: 单方签章</li>
<li>**CloudProve**: 签署报告</li>
<li>**CloudOnlineSign**: 腾讯会议在线签约</li>
<li>**ChannelWeCard**: 微工卡</li>
<li>**SignFlow**: 合同套餐</li>
<li>**SignFace**: 签署意愿（人脸识别）</li>
<li>**SignPassword**: 签署意愿（密码）</li>
<li>**SignSMS**: 签署意愿（短信）</li>
<li>**PersonalEssAuth**: 签署人实名（腾讯电子签认证）</li>
<li>**PersonalThirdAuth**: 签署人实名（信任第三方认证）</li>
<li>**OrgEssAuth**: 签署企业实名</li>
<li>**FlowNotify**: 短信通知</li>
<li>**AuthService**: 企业工商信息查询</li>
</ul>
        :type QuotaType: str
        """
        self._Total = None
        self._Used = None
        self._Available = None
        self._QuotaType = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Used(self):
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used

    @property
    def Available(self):
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def QuotaType(self):
        return self._QuotaType

    @QuotaType.setter
    def QuotaType(self, QuotaType):
        self._QuotaType = QuotaType


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Used = params.get("Used")
        self._Available = params.get("Available")
        self._QuotaType = params.get("QuotaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrganizationAuthUrl(AbstractModel):
    """企业批量注册链接信息

    """

    def __init__(self):
        r"""
        :param _AuthUrl: 企业批量注册链接，根据Endpoint的不同设置，返回不同的链接地址。失效时间：7天
跳转链接, 链接的有效期根据企业,员工状态和终端等有区别, 可以参考下表
<table> <thead> <tr> <th>Endpoint</th> <th>示例</th> <th>链接有效期限</th> </tr> </thead>  <tbody>
 <tr> <td>PC</td> <td>https://qian.tencent.com/console/batch-register?token=yDSx0UUgtjuaf4UEfd2MjCnfI1iuXFE6&orgName=批量认证线上测试企业9</td> <td>7天</td> </tr> 
<tr> <td>PC_SHORT_URL</td> <td>https://test.essurl.cn/8gDKUBAWK8</td> <td>7天</td> </tr> 
<tr> <td>APP</td> <td>/pages/guide/index?to=REGISTER_ENTERPRISE_FOR_BATCH&urlAuthToken=yDSx0UUgtjuaf4UEfd2MjCnfI1iuXFE6&orgName=批量认证线上测试企业9</td> <td>7天</td> </tr> </tbody> </table>
注： 
`1.创建的链接应避免被转义，如：&被转义为\u0026；如使用Postman请求后，请选择响应类型为 JSON，否则链接将被转义`

        :type AuthUrl: str
        :param _ErrorMessage: 企业批量注册的错误信息，例如：企业三要素不通过	
        :type ErrorMessage: str
        :param _SubTaskId: 企业批量注册的唯一 Id， 此 Id 可以用在[创建企业批量认证链接-单链接](https://qian.tencent.com/developers/companyApis/organizations/CreateBatchOrganizationAuthorizationUrl)。
        :type SubTaskId: str
        """
        self._AuthUrl = None
        self._ErrorMessage = None
        self._SubTaskId = None

    @property
    def AuthUrl(self):
        return self._AuthUrl

    @AuthUrl.setter
    def AuthUrl(self, AuthUrl):
        self._AuthUrl = AuthUrl

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def SubTaskId(self):
        return self._SubTaskId

    @SubTaskId.setter
    def SubTaskId(self, SubTaskId):
        self._SubTaskId = SubTaskId


    def _deserialize(self, params):
        self._AuthUrl = params.get("AuthUrl")
        self._ErrorMessage = params.get("ErrorMessage")
        self._SubTaskId = params.get("SubTaskId")
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
        :param _SignPlatform: 签署平台
如果文件是在腾讯电子签平台签署，则为**腾讯电子签**，
如果文件不在腾讯电子签平台签署，则为**其他平台**。
        :type SignPlatform: str
        :param _SignerName: 申请证书的主体的名字

如果是在腾讯电子签平台签署, 则对应的主体的名字个数如下
**企业**:  ESS@企业名称@编码
**个人**: ESS@个人姓名@证件号@808854

如果在其他平台签署的, 主体的名字参考其他平台的说明
        :type SignerName: str
        :param _SignTime: 签署时间的Unix时间戳，单位毫秒
        :type SignTime: int
        :param _SignAlgorithm: 证书签名算法,  如SHA1withRSA等算法
        :type SignAlgorithm: str
        :param _CertSn: CA供应商下发给用户的证书编号

注意：`腾讯电子签接入多家CA供应商以提供容灾能力，不同CA下发的证书编号区别较大，但基本都是由数字和字母组成，长度在200以下`。
        :type CertSn: str
        :param _CertNotBefore: 证书起始时间的Unix时间戳，单位毫秒
        :type CertNotBefore: int
        :param _CertNotAfter: 证书过期时间的时间戳，单位毫秒
        :type CertNotAfter: int
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
        :param _ApproverVerifyTypes: 签署人查看合同校验方式, 支持的类型如下:
<ul><li> 1 :实名认证查看</li>
<li> 2 :手机号校验查看</li></ul>
        :type ApproverVerifyTypes: list of int
        :param _ApproverSignTypes: 签署人进行合同签署时的认证方式，支持的类型如下:
<ul><li> 1 :人脸认证</li>
<li> 2 :签署密码</li>
<li> 3 :运营商三要素认证</li>
<li> 4 :UKey认证</li>
<li> 5 :设备指纹识别</li>
<li> 6 :设备面容识别</li></ul>
        :type ApproverSignTypes: list of int
        :param _NoTransfer: 签署方是否可以转他人处理

<ul><li> **false** : ( 默认)可以转他人处理</li>
<li> **true** :不可以转他人处理</li></ul>
        :type NoTransfer: bool
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
        self._ApproverVerifyTypes = None
        self._ApproverSignTypes = None
        self._NoTransfer = None

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
    def NoTransfer(self):
        return self._NoTransfer

    @NoTransfer.setter
    def NoTransfer(self, NoTransfer):
        self._NoTransfer = NoTransfer


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
        self._ApproverVerifyTypes = params.get("ApproverVerifyTypes")
        self._ApproverSignTypes = params.get("ApproverSignTypes")
        self._NoTransfer = params.get("NoTransfer")
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
<ul><li>0-未填写</li>
<li>1-已填写</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type RecipientFillStatus: str
        :param _IsPromoter: 是否为发起方
<ul><li>true-发起方</li>
<li>false-参与方</li></ul>
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
        


class RegistrationOrganizationInfo(AbstractModel):
    """企业认证信息参数， 需要保证这些参数跟营业执照中的信息一致。

    """

    def __init__(self):
        r"""
        :param _OrganizationName: 组织机构名称。
请确认该名称与企业营业执照中注册的名称一致。
如果名称中包含英文括号()，请使用中文括号（）代替。
        :type OrganizationName: str
        :param _UniformSocialCreditCode: 组织机构企业统一社会信用代码。
请确认该企业统一社会信用代码与企业营业执照中注册的统一社会信用代码一致。
        :type UniformSocialCreditCode: str
        :param _LegalName: 组织机构法人的姓名。
请确认该企业统一社会信用代码与企业营业执照中注册的法人姓名一致。
        :type LegalName: str
        :param _Address: 组织机构企业注册地址。
请确认该企业注册地址与企业营业执照中注册的地址一致。
        :type Address: str
        :param _AdminName: 组织机构超管姓名。
在注册流程中，必须是超管本人进行操作。
如果法人做为超管管理组织机构,超管姓名就是法人姓名
如果入参中传递超管授权书PowerOfAttorneys，则此参数为必填参数。
        :type AdminName: str
        :param _AdminMobile: 组织机构超管手机号。
在注册流程中，这个手机号必须跟操作人在电子签注册的个人手机号一致。
如果入参中传递超管授权书PowerOfAttorneys，则此参数为必填参数
        :type AdminMobile: str
        :param _AuthorizationTypes: 可选的此企业允许的授权方式, 可以设置的方式有:
1：上传授权书
2：法人授权超管
5：授权书+对公打款


注:
`1. 当前仅支持一种认证方式`
`2. 如果当前的企业类型是政府/事业单位, 则只支持上传授权书+对公打款`
`3. 如果当前操作人是法人,则是法人认证`
        :type AuthorizationTypes: list of int non-negative
        :param _AdminIdCardNumber: 认证人身份证号，如果入参中传递超管授权书PowerOfAttorneys，则此参数为必填参数

        :type AdminIdCardNumber: str
        :param _AdminIdCardType: 认证人证件类型 
支持以下类型
<ul><li>ID_CARD : 居民身份证  (默认值)</li>
<li>HONGKONG_AND_MACAO : 港澳居民来往内地通行证</li>
<li>HONGKONG_MACAO_AND_TAIWAN : 港澳台居民居住证(格式同居民身份证)</li></ul>

        :type AdminIdCardType: str
        :param _BusinessLicense: 营业执照正面照(PNG或JPG) base64格式, 大小不超过5M
        :type BusinessLicense: str
        :param _PowerOfAttorneys: 授权书(PNG或JPG或PDF) base64格式, 大小不超过8M 。
p.s. 如果上传授权书 ，需遵循以下条件
1. 超管的信息（超管姓名，超管身份证，超管手机号）必须为必填参数。
2. 超管的个人身份必须在电子签已经实名。
2. 认证方式AuthorizationTypes必须只能是上传授权书方式 

        :type PowerOfAttorneys: list of str
        """
        self._OrganizationName = None
        self._UniformSocialCreditCode = None
        self._LegalName = None
        self._Address = None
        self._AdminName = None
        self._AdminMobile = None
        self._AuthorizationTypes = None
        self._AdminIdCardNumber = None
        self._AdminIdCardType = None
        self._BusinessLicense = None
        self._PowerOfAttorneys = None

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def UniformSocialCreditCode(self):
        return self._UniformSocialCreditCode

    @UniformSocialCreditCode.setter
    def UniformSocialCreditCode(self, UniformSocialCreditCode):
        self._UniformSocialCreditCode = UniformSocialCreditCode

    @property
    def LegalName(self):
        return self._LegalName

    @LegalName.setter
    def LegalName(self, LegalName):
        self._LegalName = LegalName

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def AdminName(self):
        return self._AdminName

    @AdminName.setter
    def AdminName(self, AdminName):
        self._AdminName = AdminName

    @property
    def AdminMobile(self):
        return self._AdminMobile

    @AdminMobile.setter
    def AdminMobile(self, AdminMobile):
        self._AdminMobile = AdminMobile

    @property
    def AuthorizationTypes(self):
        return self._AuthorizationTypes

    @AuthorizationTypes.setter
    def AuthorizationTypes(self, AuthorizationTypes):
        self._AuthorizationTypes = AuthorizationTypes

    @property
    def AdminIdCardNumber(self):
        return self._AdminIdCardNumber

    @AdminIdCardNumber.setter
    def AdminIdCardNumber(self, AdminIdCardNumber):
        self._AdminIdCardNumber = AdminIdCardNumber

    @property
    def AdminIdCardType(self):
        return self._AdminIdCardType

    @AdminIdCardType.setter
    def AdminIdCardType(self, AdminIdCardType):
        self._AdminIdCardType = AdminIdCardType

    @property
    def BusinessLicense(self):
        return self._BusinessLicense

    @BusinessLicense.setter
    def BusinessLicense(self, BusinessLicense):
        self._BusinessLicense = BusinessLicense

    @property
    def PowerOfAttorneys(self):
        return self._PowerOfAttorneys

    @PowerOfAttorneys.setter
    def PowerOfAttorneys(self, PowerOfAttorneys):
        self._PowerOfAttorneys = PowerOfAttorneys


    def _deserialize(self, params):
        self._OrganizationName = params.get("OrganizationName")
        self._UniformSocialCreditCode = params.get("UniformSocialCreditCode")
        self._LegalName = params.get("LegalName")
        self._Address = params.get("Address")
        self._AdminName = params.get("AdminName")
        self._AdminMobile = params.get("AdminMobile")
        self._AuthorizationTypes = params.get("AuthorizationTypes")
        self._AdminIdCardNumber = params.get("AdminIdCardNumber")
        self._AdminIdCardType = params.get("AdminIdCardType")
        self._BusinessLicense = params.get("BusinessLicense")
        self._PowerOfAttorneys = params.get("PowerOfAttorneys")
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
        :param _ApproverSignSealId: 印章Id，签署控件类型为印章时，用于指定本企业签署方在解除协议中使用那个印章进行签署
        :type ApproverSignSealId: str
        """
        self._Name = None
        self._Mobile = None
        self._RelievedApproverReceiptId = None
        self._ApproverType = None
        self._ApproverSignComponentType = None
        self._ApproverSignRole = None
        self._ApproverSignSealId = None

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

    @property
    def ApproverSignSealId(self):
        return self._ApproverSignSealId

    @ApproverSignSealId.setter
    def ApproverSignSealId(self, ApproverSignSealId):
        self._ApproverSignSealId = ApproverSignSealId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Mobile = params.get("Mobile")
        self._RelievedApproverReceiptId = params.get("RelievedApproverReceiptId")
        self._ApproverType = params.get("ApproverType")
        self._ApproverSignComponentType = params.get("ApproverSignComponentType")
        self._ApproverSignRole = params.get("ApproverSignRole")
        self._ApproverSignSealId = params.get("ApproverSignSealId")
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
        


class RenewAutoSignLicenseRequest(AbstractModel):
    """RenewAutoSignLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _SceneKey: 自动签使用的场景值, 可以选择的场景值如下:
<ul><li> **E_PRESCRIPTION_AUTO_SIGN** :  电子处方场景</li><li> **OTHER** :  通用场景</li></ul>
        :type SceneKey: str
        :param _UserInfo: 需要续期自动签的个人的信息，如姓名，证件信息等。
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
        


class RenewAutoSignLicenseResponse(AbstractModel):
    """RenewAutoSignLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LicenseTo: 续期成功后新的自动签许可到期时间。当且仅当已通过许可开通自动签时有值。

值为unix时间戳,单位为秒。
        :type LicenseTo: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LicenseTo = None
        self._RequestId = None

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
        self._LicenseTo = params.get("LicenseTo")
        self._RequestId = params.get("RequestId")


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
    """企业员工信息。

    """

    def __init__(self):
        r"""
        :param _UserId: 员工在腾讯电子签平台的唯一身份标识，为32位字符串。
注：`创建和更新场景无需填写。`
        :type UserId: str
        :param _DisplayName: 显示的用户名/昵称。
        :type DisplayName: str
        :param _Mobile: 用户手机号码， 支持国内手机号11位数字(无需加+86前缀或其他字符)。
        :type Mobile: str
        :param _Email: 用户邮箱。
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _OpenId: 用户在第三方平台ID。
注：`如需在此接口提醒员工实名，该参数不传。`
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param _Roles: 员工角色信息。
注：`创建和更新场景无需填写。`
注意：此字段可能返回 null，表示取不到有效值。
        :type Roles: list of StaffRole
        :param _Department: 员工部门信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Department: :class:`tencentcloud.ess.v20201111.models.Department`
        :param _Verified: 员工是否实名。
注：`创建和更新场景无需填写。`
        :type Verified: bool
        :param _CreatedOn: 员工创建时间戳，单位秒。
注：`创建和更新场景无需填写。`
        :type CreatedOn: int
        :param _VerifiedOn: 员工实名时间戳，单位秒。
注：`创建和更新场景无需填写。`
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifiedOn: int
        :param _QuiteJob: 员工是否离职：
<ul><li>**0**：未离职</li><li>**1**：离职</li></ul>
注：`创建和更新场景无需填写。`
注意：此字段可能返回 null，表示取不到有效值。
        :type QuiteJob: int
        :param _ReceiveUserId: 员工离职交接人用户ID。
注：`创建和更新场景无需填写。`
        :type ReceiveUserId: str
        :param _ReceiveOpenId: 员工离职交接人用户OpenId。
注：`创建和更新场景无需填写。`
        :type ReceiveOpenId: str
        :param _WeworkOpenId: 企业微信用户账号ID。
注：`仅企微类型的企业创建员工接口支持该字段。`
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
    """集成版企业角色信息。

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleId: str
        :param _RoleName: 角色名称。
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class SubOrgBillSummary(AbstractModel):
    """子企业套餐使用情况

    """

    def __init__(self):
        r"""
        :param _OrganizationName: 子企业名称
        :type OrganizationName: str
        :param _Usage:  
        :type Usage: list of SubOrgBillUsage
        """
        self._OrganizationName = None
        self._Usage = None

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def Usage(self):
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage


    def _deserialize(self, params):
        self._OrganizationName = params.get("OrganizationName")
        if params.get("Usage") is not None:
            self._Usage = []
            for item in params.get("Usage"):
                obj = SubOrgBillUsage()
                obj._deserialize(item)
                self._Usage.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubOrgBillUsage(AbstractModel):
    """集团子企业使用集团主企业的套餐使用情况

    """

    def __init__(self):
        r"""
        :param _Used: 套餐使用数
        :type Used: int
        :param _QuotaType: 套餐类型
对应关系如下:
<ul>
<li>**CloudEnterprise**: 企业版合同</li>
<li>**SingleSignature**: 单方签章</li>
<li>**CloudProve**: 签署报告</li>
<li>**CloudOnlineSign**: 腾讯会议在线签约</li>
<li>**ChannelWeCard**: 微工卡</li>
<li>**SignFlow**: 合同套餐</li>
<li>**SignFace**: 签署意愿（人脸识别）</li>
<li>**SignPassword**: 签署意愿（密码）</li>
<li>**SignSMS**: 签署意愿（短信）</li>
<li>**PersonalEssAuth**: 签署人实名（腾讯电子签认证）</li>
<li>**PersonalThirdAuth**: 签署人实名（信任第三方认证）</li>
<li>**OrgEssAuth**: 签署企业实名</li>
<li>**FlowNotify**: 短信通知</li>
<li>**AuthService**: 企业工商信息查询</li>
</ul>
        :type QuotaType: str
        """
        self._Used = None
        self._QuotaType = None

    @property
    def Used(self):
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used

    @property
    def QuotaType(self):
        return self._QuotaType

    @QuotaType.setter
    def QuotaType(self, QuotaType):
        self._QuotaType = QuotaType


    def _deserialize(self, params):
        self._Used = params.get("Used")
        self._QuotaType = params.get("QuotaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuccessCreateStaffData(AbstractModel):
    """创建/修改员工成功返回的信息
    现在支持saas/企微/H5端进行加入。

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
        :param _Url: 员工邀请返回链接 根据入参的 InvitationNotifyType 和 Endpoint 返回链接 <table><tbody><tr><td>链接类型</td><td>有效期</td><td>示例</td></tr><tr><td>HTTP_SHORT_URL（短链）</td><td>一天</td><td>https://test.essurl.cn/fvG7UBEd0F</td></tr><tr><td>HTTP（长链）</td><td>一天</td><td>https://res.ess.tencent.cn/cdn/h5-activity-dev/jump-mp.html?where=mini&from=MSG&to=USER_VERIFY&verifyToken=yDCVbUUckpwocmfpUySko7IS83LTV0u0&expireTime=1710840183</td></tr><tr><td>H5</td><td>30 天</td><td>https://quick.test.qian.tencent.cn/guide?Code=yDCVbUUckpwtvxqoUbTw4VBBjLbfAtW7&CodeType=QUICK&shortKey=yDCVbUY7lhqV7mZlCL2d</td></tr><tr><td>APP</td><td>一天</td><td>/pages/guide/index?to=USER_VERIFY&verifyToken=yDCVbUUckpwocm96UySko7ISvEIZH7Yz&expireTime=1710840455 </td></tr></tbody></table>
        :type Url: str
        """
        self._DisplayName = None
        self._Mobile = None
        self._UserId = None
        self._Note = None
        self._WeworkOpenId = None
        self._Url = None

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

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._Mobile = params.get("Mobile")
        self._UserId = params.get("UserId")
        self._Note = params.get("Note")
        self._WeworkOpenId = params.get("WeworkOpenId")
        self._Url = params.get("Url")
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
    """更新员工信息成功返回的数据信息， 仅支持未实名的用户进行更新
    会通过短信、企微消息或者H5Url 链接
    如果是通过H5邀请加入的方式，会返回H5 链接

    """

    def __init__(self):
        r"""
        :param _DisplayName: 传入的用户名称
        :type DisplayName: str
        :param _Mobile: 传入的手机号，没有打码
        :type Mobile: str
        :param _UserId: 员工在腾讯电子签平台的唯一身份标识，为32位字符串。
可登录腾讯电子签控制台，在 "更多能力"->"组织管理" 中查看某位员工的UserId(在页面中展示为用户ID)。
        :type UserId: str
        :param _Url: H5端员工实名链接

只有入参 InvitationNotifyType = H5的时候才会进行返回。
        :type Url: str
        """
        self._DisplayName = None
        self._Mobile = None
        self._UserId = None
        self._Url = None

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
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._Mobile = params.get("Mobile")
        self._UserId = params.get("UserId")
        self._Url = params.get("Url")
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
        :param _TemplateName: 模板的名字
        :type TemplateName: str
        :param _Recipients: 此模块需要签署的各个参与方的角色列表。RecipientId标识每个参与方角色对应的唯一标识符，用于确定此角色的信息。

[点击查看在模板中配置的签署参与方角色列表的样子](https://qcloudimg.tencent-cloud.cn/raw/e082bbcc0d923f8cb723d98382410aa2.png)


        :type Recipients: list of Recipient
        :param _Components: 模板的填充控件列表

[点击查看在模板中配置的填充控件的样子](https://qcloudimg.tencent-cloud.cn/raw/cb2f58529fca8d909258f9d45a56f7f4.png)
        :type Components: list of Component
        :param _SignComponents: 此模板中的签署控件列表

[点击查看在模板中配置的签署控件的样子](https://qcloudimg.tencent-cloud.cn/raw/29bc6ed753a5a0fce4a3ab02e2c0d955.png)
        :type SignComponents: list of Component
        :param _Description: 模板描述信息
        :type Description: str
        :param _DocumentResourceIds: 此模板的资源ID
        :type DocumentResourceIds: list of str
        :param _FileInfos: 生成模板的文件基础信息
        :type FileInfos: list of FileInfo
        :param _AttachmentResourceIds: 此模板里边附件的资源ID
        :type AttachmentResourceIds: list of str
        :param _SignOrder: 签署人参与签署的顺序，可以分为以下两种方式：

<b>无序</b>：不限定签署人的签署顺序，签署人可以在任何时间签署。此种方式值为 ：｛-1｝
<b>有序</b>：通过序列数字标识签署顺序，从0开始编码，数字越大签署顺序越靠后，签署人按照指定的顺序依次签署。此种方式值为： ｛0，1，2，3………｝
        :type SignOrder: list of int
        :param _Status: 此模板的状态可以分为以下几种：

<b>-1</b>：不可用状态。
<b>0</b>：草稿态，即模板正在编辑或未发布状态。
<b>1</b>：正式态，只有正式态的模板才可以发起合同。
        :type Status: int
        :param _Creator: 模板的创建者信息，用户的名字

注： `是创建者的名字，而非创建者的用户ID`
        :type Creator: str
        :param _CreatedOn: 模板创建的时间戳，格式为Unix标准时间戳（秒）
        :type CreatedOn: int
        :param _Promoter: 此模板创建方角色信息。

[点击查看在模板中配置的创建方角色的样子](https://qcloudimg.tencent-cloud.cn/raw/e082bbcc0d923f8cb723d98382410aa2.png)

        :type Promoter: :class:`tencentcloud.ess.v20201111.models.Recipient`
        :param _TemplateType: 模板类型可以分为以下两种：

<b>1</b>：带有本企业自动签署的模板，即签署过程无需签署人手动操作，系统自动完成签署。
<b>3</b>：普通模板，即签署人需要手动进行签署操作。
        :type TemplateType: int
        :param _Available: 模板可用状态可以分为以下两种：

<b>1</b>：（默认）启用状态，即模板可以正常使用。
<b>2</b>：停用状态，即模板暂时无法使用。

可到控制台启停模板
        :type Available: int
        :param _OrganizationId: 创建模板的企业ID，电子签的机构ID
        :type OrganizationId: str
        :param _CreatorId: 模板创建人用户ID
        :type CreatorId: str
        :param _PreviewUrl: 模板的H5预览链接,有效期5分钟。
可以通过浏览器打开此链接预览模板，或者嵌入到iframe中预览模板。
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewUrl: str
        :param _UserFlowType: 用户自定义合同类型。

返回配置模板的时候选择的合同类型。[点击查看配置的位置](https://qcloudimg.tencent-cloud.cn/raw/4a766f0540253bf2a05d50c58bd14990.png)

自定义合同类型配置的地方如链接图所示。[点击查看自定义合同类型管理的位置](https://qcloudimg.tencent-cloud.cn/raw/36582cea03ae6a2559894844942b5d5c.png)

注意：此字段可能返回 null，表示取不到有效值。
        :type UserFlowType: :class:`tencentcloud.ess.v20201111.models.UserFlowType`
        :param _TemplateVersion: 模板版本的编号，旨在标识其独特的版本信息，通常呈现为一串字符串，由日期和递增的数字组成
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateVersion: str
        :param _Published: 模板是否已发布可以分为以下两种状态：

<b>true</b>：已发布状态，表示该模板已经发布并可以正常使用。
<b>false</b>：未发布状态，表示该模板还未发布，无法使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type Published: bool
        :param _ShareTemplateId: <b>集体账号场景下</b>： 集团账号分享给子企业的模板的来源模板ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ShareTemplateId: str
        :param _TemplateSeals: 此模板配置的预填印章列表（包括自动签署指定的印章）
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateSeals: list of SealInfo
        :param _Seals: 模板内部指定的印章列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Seals: list of SealInfo
        """
        self._TemplateId = None
        self._TemplateName = None
        self._Recipients = None
        self._Components = None
        self._SignComponents = None
        self._Description = None
        self._DocumentResourceIds = None
        self._FileInfos = None
        self._AttachmentResourceIds = None
        self._SignOrder = None
        self._Status = None
        self._Creator = None
        self._CreatedOn = None
        self._Promoter = None
        self._TemplateType = None
        self._Available = None
        self._OrganizationId = None
        self._CreatorId = None
        self._PreviewUrl = None
        self._UserFlowType = None
        self._TemplateVersion = None
        self._Published = None
        self._ShareTemplateId = None
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
    def CreatorId(self):
        return self._CreatorId

    @CreatorId.setter
    def CreatorId(self, CreatorId):
        self._CreatorId = CreatorId

    @property
    def PreviewUrl(self):
        return self._PreviewUrl

    @PreviewUrl.setter
    def PreviewUrl(self, PreviewUrl):
        self._PreviewUrl = PreviewUrl

    @property
    def UserFlowType(self):
        return self._UserFlowType

    @UserFlowType.setter
    def UserFlowType(self, UserFlowType):
        self._UserFlowType = UserFlowType

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
    def ShareTemplateId(self):
        return self._ShareTemplateId

    @ShareTemplateId.setter
    def ShareTemplateId(self, ShareTemplateId):
        self._ShareTemplateId = ShareTemplateId

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
        self._Status = params.get("Status")
        self._Creator = params.get("Creator")
        self._CreatedOn = params.get("CreatedOn")
        if params.get("Promoter") is not None:
            self._Promoter = Recipient()
            self._Promoter._deserialize(params.get("Promoter"))
        self._TemplateType = params.get("TemplateType")
        self._Available = params.get("Available")
        self._OrganizationId = params.get("OrganizationId")
        self._CreatorId = params.get("CreatorId")
        self._PreviewUrl = params.get("PreviewUrl")
        if params.get("UserFlowType") is not None:
            self._UserFlowType = UserFlowType()
            self._UserFlowType._deserialize(params.get("UserFlowType"))
        self._TemplateVersion = params.get("TemplateVersion")
        self._Published = params.get("Published")
        self._ShareTemplateId = params.get("ShareTemplateId")
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
        :param _Operator: 执行本接口操作的员工信息。使用此接口时，必须填写UserId。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _UserId: 员工在腾讯电子签平台的唯一身份标识，为32位字符串。

通过<a href="https://qian.tencent.com/developers/companyApis/staffs/DescribeIntegrationEmployees" target="_blank">DescribeIntegrationEmployees</a>接口获取，也可登录腾讯电子签控制台查看
![image](https://qcloudimg.tencent-cloud.cn/raw/97cfffabb0caa61df16999cd395d7850.png)
        :type UserId: str
        :param _OpenId: 员工在贵司业务系统中的唯一身份标识，用于与腾讯电子签账号进行映射，确保在同一企业内不会出现重复。
该标识最大长度为64位字符串，仅支持包含26个英文字母和数字0-9的字符。
        :type OpenId: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
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
        :param _Status: 解绑是否成功。
<ul><li> **0**：失败 </li>
<li> **1**：成功 </li></ul>
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Operator: 执行本接口操作的员工信息,UserId必填。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Employees: 需要更新的员工信息，最多不超过100个。根据UserId或OpenId更新员工信息，必须填写其中一个，优先使用UserId。

可更新以下字段，其他字段暂不支持
<table> <thead> <tr> <th>参数</th> <th>含义</th> </tr> </thead> <tbody> <tr> <td>DisplayName</td> <td>用户的真实名字</td> </tr> <tr> <td>Mobile</td> <td>用户手机号码</td> </tr> <tr> <td>Email</td> <td>用户的邮箱</td> </tr> <tr> <td>Department.DepartmentId</td> <td>用户进入后的部门ID</td> </tr> </tbody> </table>
        :type Employees: list of Staff
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param _InvitationNotifyType: 员工邀请方式可通过以下途径进行设置：<ul><li>**SMS（默认）**：邀请将通过短信或企业微信消息发送。若场景非企业微信，则采用企业微信消息；其他情境下则使用短信通知。短信内含链接，点击后将进入微信小程序进行认证并加入企业的流程。</li><li>**H5**：将生成H5链接，用户点击链接后可进入H5页面进行认证并加入企业的流程。</li><li>**NONE**：系统会根据Endpoint生成签署链接，业务方需获取链接并通知客户。</li></ul>
        :type InvitationNotifyType: str
        :param _JumpUrl: 回跳地址，为认证成功后页面进行回跳的URL，请确保回跳地址的可用性。注：`只有在员工邀请方式（InvitationNotifyType参数）为H5场景下才生效， 其他方式下设置无效。`
        :type JumpUrl: str
        :param _Endpoint: 要跳转的链接类型<ul><li> **HTTP**：跳转电子签小程序的http_url, 短信通知或者H5跳转适合此类型  ，此时返回长链 (默认类型)</li><li>**HTTP_SHORT_URL**：跳转电子签小程序的http_url, 短信通知或者H5跳转适合此类型，此时返回短链</li><li>**APP**： 第三方APP或小程序跳转电子签小程序的path,  APP或者小程序跳转适合此类型</li><li>**H5**： 第三方移动端浏览器进行嵌入，不支持小程序嵌入，过期时间一个月</li></ul>注意：InvitationNotifyType 和 Endpoint 的关系图<table><tbody><tr><td>通知类型（InvitationNotifyType）</td><td>Endpoint</td></tr><tr><td>SMS（默认）</td><td>不需要传递，会将 Endpoint 默认设置为HTTP_SHORT_URL</td></tr><tr><td>H5</td><td>不需要传递，会将 Endpoint 默认设置为 H5</td></tr><tr><td>NONE</td><td>所有 Endpoint 都支持（HTTP_URL/HTTP_SHORT_URL/H5/APP）默认为HTTP_SHORT_URL</td></tr></tbody></table>
        :type Endpoint: str
        """
        self._Operator = None
        self._Employees = None
        self._Agent = None
        self._InvitationNotifyType = None
        self._JumpUrl = None
        self._Endpoint = None

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

    @property
    def InvitationNotifyType(self):
        return self._InvitationNotifyType

    @InvitationNotifyType.setter
    def InvitationNotifyType(self, InvitationNotifyType):
        self._InvitationNotifyType = InvitationNotifyType

    @property
    def JumpUrl(self):
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint


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
        self._InvitationNotifyType = params.get("InvitationNotifyType")
        self._JumpUrl = params.get("JumpUrl")
        self._Endpoint = params.get("Endpoint")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _BusinessType: 文件对应业务类型,可以选择的类型如下
<ul><li> **TEMPLATE** : 此上传的文件用户生成合同模板，文件类型支持.pdf/.doc/.docx/.html格式，如果非pdf文件需要通过<a href="https://qian.tencent.com/developers/companyApis/templatesAndFiles/CreateConvertTaskApi" target="_blank">创建文件转换任务</a>转换后才能使用</li>
<li> **DOCUMENT** : 此文件用来发起合同流程，文件类型支持.pdf/.doc/.docx/.jpg/.png/.xls.xlsx/.html，如果非pdf文件需要通过<a href="https://qian.tencent.com/developers/companyApis/templatesAndFiles/CreateConvertTaskApi" target="_blank">创建文件转换任务</a>转换后才能使用</li>
<li> **SEAL** : 此文件用于印章的生成，文件类型支持.jpg/.jpeg/.png</li></ul>
        :type BusinessType: str
        :param _Caller: 执行本接口操作的员工信息。其中OperatorId为必填字段，即用户的UserId。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。`
        :type Caller: :class:`tencentcloud.ess.v20201111.models.Caller`
        :param _FileInfos: 上传文件内容数组，最多支持上传20个文件。
        :type FileInfos: list of UploadFile
        :param _FileType: 文件类型， 默认通过文件内容和文件后缀一起解析得到文件类型，调用接口时可以显示的指定上传文件的类型。
可支持的指定类型如下:
<ul><li>pdf</li>
<li>doc</li>
<li>docx</li>
<li>xls</li>
<li>xlsx</li>
<li>html</li>
<li>jpg</li>
<li>jpeg</li>
<li>png</li></ul>
如：pdf 表示上传的文件 张三入职合同.pdf的文件类型是 pdf
        :type FileType: str
        :param _CoverRect: 此参数仅对上传的PDF文件有效。其主要作用是确定是否将PDF中的灰色矩阵置为白色。
<ul><li>**true**：将灰色矩阵置为白色。</li>
<li>**false**：无需处理，不会将灰色矩阵置为白色（默认）。</li></ul>

注: `该参数仅在关键字定位时，需要去除关键字所在的灰框场景下使用。`
        :type CoverRect: bool
        :param _CustomIds: 用户自定义ID数组，与上传文件一一对应

注: `历史遗留问题，已经废弃，调用接口时不用赋值`
        :type CustomIds: list of str
        :param _FileUrls: 不再使用，上传文件链接数组，最多支持20个URL
        :type FileUrls: str
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._BusinessType = None
        self._Caller = None
        self._FileInfos = None
        self._FileType = None
        self._CoverRect = None
        self._CustomIds = None
        self._FileUrls = None
        self._Agent = None

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

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


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
        


class UploadFilesResponse(AbstractModel):
    """UploadFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileIds: 文件资源ID数组，每个文件资源ID为32位字符串。
建议开发者保存此资源ID，后续创建合同或创建合同流程需此资源ID。
        :type FileIds: list of str
        :param _TotalCount: 上传成功文件数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class UserFlowType(AbstractModel):
    """用户自定义合同类型， 自定义合同类型的管理可以[点击查看在控制台位置的截图](https://qcloudimg.tencent-cloud.cn/raw/85a9b2ebce07b0cd6d75d5327d538235.png)

    """

    def __init__(self):
        r"""
        :param _UserFlowTypeId: 合同类型ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserFlowTypeId: str
        :param _Name: 合同类型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: 合同类型说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self._UserFlowTypeId = None
        self._Name = None
        self._Description = None

    @property
    def UserFlowTypeId(self):
        return self._UserFlowTypeId

    @UserFlowTypeId.setter
    def UserFlowTypeId(self, UserFlowTypeId):
        self._UserFlowTypeId = UserFlowTypeId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._UserFlowTypeId = params.get("UserFlowTypeId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
<ul><li>ID_CARD : 中国大陆居民身份证 (默认值)</li>
<li>HONGKONG_AND_MACAO : 港澳居民来往内地通行证</li>
<li>HONGKONG_MACAO_AND_TAIWAN : 港澳台居民居住证(格式同居民身份证)</li></ul>
        :type IdCardType: str
        :param _IdCardNumber: 证件号码，应符合以下规则
<ul><li>居民身份证号码应为18位字符串，由数字和大写字母X组成（如存在X，请大写）。</li>
<li>港澳居民来往内地通行证号码共11位。第1位为字母，“H”字头签发给香港居民，“M”字头签发给澳门居民；第2位至第11位为数字。</li>
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
        :param _FlowId: 合同流程ID，为32位字符串。
可登录腾讯电子签控制台，在 "合同"->"合同中心" 中查看某个合同的FlowId(在页面中展示为合同ID)。
        :type FlowId: str
        :param _Operator: 执行本接口操作的员工信息。
注: `在调用此接口时，请确保指定的员工已获得所需的接口调用权限，并具备接口传入的相应资源的数据权限。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param _Agent: 代理企业和员工的信息。
在集团企业代理子企业操作的场景中，需设置此参数。在此情境下，ProxyOrganizationId（子企业的组织ID）为必填项。
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self._FlowId = None
        self._Operator = None
        self._Agent = None

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

    @property
    def Agent(self):
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
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
        


class VerifyPdfResponse(AbstractModel):
    """VerifyPdf返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VerifyResult: 验签结果代码，代码的含义如下：

<ul><li>**1**：文件未被篡改，全部签名在腾讯电子签完成。</li>
<li>**2**：文件未被篡改，部分签名在腾讯电子签完成。</li>
<li>**3**：文件被篡改。</li>
<li>**4**：异常：文件内没有签名域。</li>
<li>**5**：异常：文件签名格式错误。</li></ul>
        :type VerifyResult: int
        :param _PdfVerifyResults: 验签结果详情，每个签名域对应的验签结果。状态值如下
<ul><li> **1** :验签成功，在电子签签署</li>
<li> **2** :验签成功，在其他平台签署</li>
<li> **3** :验签失败</li>
<li> **4** :pdf文件没有签名域</li>
<li> **5** :文件签名格式错误</li></ul>
        :type PdfVerifyResults: list of PdfVerifyResult
        :param _VerifySerialNo: 验签序列号, 为11为数组组成的字符串
        :type VerifySerialNo: str
        :param _PdfResourceMd5: 合同文件MD5哈希值
        :type PdfResourceMd5: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VerifyResult = None
        self._PdfVerifyResults = None
        self._VerifySerialNo = None
        self._PdfResourceMd5 = None
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
    def PdfResourceMd5(self):
        return self._PdfResourceMd5

    @PdfResourceMd5.setter
    def PdfResourceMd5(self, PdfResourceMd5):
        self._PdfResourceMd5 = PdfResourceMd5

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
        self._PdfResourceMd5 = params.get("PdfResourceMd5")
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
        