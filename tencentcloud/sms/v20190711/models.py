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


class AddSignStatus(AbstractModel):
    """添加签名响应

    """

    def __init__(self):
        r"""
        :param _SignId: 签名Id。
        :type SignId: int
        :param _SignApplyId: 签名申请Id。
        :type SignApplyId: int
        """
        self._SignId = None
        self._SignApplyId = None

    @property
    def SignId(self):
        """签名Id。
        :rtype: int
        """
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def SignApplyId(self):
        """签名申请Id。
        :rtype: int
        """
        return self._SignApplyId

    @SignApplyId.setter
    def SignApplyId(self, SignApplyId):
        self._SignApplyId = SignApplyId


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        self._SignApplyId = params.get("SignApplyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSmsSignRequest(AbstractModel):
    """AddSmsSign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SignName: 签名名称。
注：不能重复申请已通过或待审核的签名。
        :type SignName: str
        :param _SignType: 签名类型。其中每种类型后面标注了其可选的 DocumentType（证明类型）：
0：公司，可选 DocumentType 有（0，1）。
1：APP，可选 DocumentType 有（0，1，2，3，4） 。
4：商标，可选 DocumentType 有（7）。
5：政府/机关事业单位/其他机构，可选 DocumentType 有（2，3）。
注1：必须按照对应关系选择证明类型，否则会审核失败。
注2：签名类型2（网站）、3（公众号）、6（小程序）已不再支持，具体可参考 [关于腾讯云短信签名申请规则更新的公告](https://cloud.tencent.com/document/product/382/116397)。
        :type SignType: int
        :param _DocumentType: 证明类型：
0：三证合一。
1：企业营业执照。
2：组织机构代码证书。
3：社会信用代码证书。
4：应用后台管理截图（个人开发APP）。
7：商标注册书。
注：证明类型5（网站备案后台截图）、6（小程序设置页面截图）、8（公众号设置页面截图）已不再支持，具体可参考 [关于腾讯云短信签名申请规则更新的公告](https://cloud.tencent.com/document/product/382/116397)。
        :type DocumentType: int
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param _UsedMethod: 签名用途：
0：自用。
1：他用。
        :type UsedMethod: int
        :param _ProofImage: 签名对应的资质证明图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。
        :type ProofImage: str
        :param _CommissionImage: 委托授权证明。选择 UsedMethod 为他用之后需要提交委托的授权证明。
图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。
注：只有 UsedMethod 在选择为 1（他用）时，这个字段才会生效。
        :type CommissionImage: str
        :param _Remark: 签名的申请备注。
        :type Remark: str
        :param _QualificationId: 已审核通过的国内短信的资质 ID。资质 ID 信息可前往国内短信的 [实名资质管理](https://console.cloud.tencent.com/smsv2/enterprise) 页查看。<dx-alert infotype="notice" title="说明"><ul><li>国内短信需填写资质ID，国际短信无需填写。</li></ul></dx-alert>
        :type QualificationId: int
        """
        self._SignName = None
        self._SignType = None
        self._DocumentType = None
        self._International = None
        self._UsedMethod = None
        self._ProofImage = None
        self._CommissionImage = None
        self._Remark = None
        self._QualificationId = None

    @property
    def SignName(self):
        """签名名称。
注：不能重复申请已通过或待审核的签名。
        :rtype: str
        """
        return self._SignName

    @SignName.setter
    def SignName(self, SignName):
        self._SignName = SignName

    @property
    def SignType(self):
        """签名类型。其中每种类型后面标注了其可选的 DocumentType（证明类型）：
0：公司，可选 DocumentType 有（0，1）。
1：APP，可选 DocumentType 有（0，1，2，3，4） 。
4：商标，可选 DocumentType 有（7）。
5：政府/机关事业单位/其他机构，可选 DocumentType 有（2，3）。
注1：必须按照对应关系选择证明类型，否则会审核失败。
注2：签名类型2（网站）、3（公众号）、6（小程序）已不再支持，具体可参考 [关于腾讯云短信签名申请规则更新的公告](https://cloud.tencent.com/document/product/382/116397)。
        :rtype: int
        """
        return self._SignType

    @SignType.setter
    def SignType(self, SignType):
        self._SignType = SignType

    @property
    def DocumentType(self):
        """证明类型：
0：三证合一。
1：企业营业执照。
2：组织机构代码证书。
3：社会信用代码证书。
4：应用后台管理截图（个人开发APP）。
7：商标注册书。
注：证明类型5（网站备案后台截图）、6（小程序设置页面截图）、8（公众号设置页面截图）已不再支持，具体可参考 [关于腾讯云短信签名申请规则更新的公告](https://cloud.tencent.com/document/product/382/116397)。
        :rtype: int
        """
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def International(self):
        """是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :rtype: int
        """
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def UsedMethod(self):
        """签名用途：
0：自用。
1：他用。
        :rtype: int
        """
        return self._UsedMethod

    @UsedMethod.setter
    def UsedMethod(self, UsedMethod):
        self._UsedMethod = UsedMethod

    @property
    def ProofImage(self):
        """签名对应的资质证明图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。
        :rtype: str
        """
        return self._ProofImage

    @ProofImage.setter
    def ProofImage(self, ProofImage):
        self._ProofImage = ProofImage

    @property
    def CommissionImage(self):
        """委托授权证明。选择 UsedMethod 为他用之后需要提交委托的授权证明。
图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。
注：只有 UsedMethod 在选择为 1（他用）时，这个字段才会生效。
        :rtype: str
        """
        return self._CommissionImage

    @CommissionImage.setter
    def CommissionImage(self, CommissionImage):
        self._CommissionImage = CommissionImage

    @property
    def Remark(self):
        """签名的申请备注。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def QualificationId(self):
        """已审核通过的国内短信的资质 ID。资质 ID 信息可前往国内短信的 [实名资质管理](https://console.cloud.tencent.com/smsv2/enterprise) 页查看。<dx-alert infotype="notice" title="说明"><ul><li>国内短信需填写资质ID，国际短信无需填写。</li></ul></dx-alert>
        :rtype: int
        """
        return self._QualificationId

    @QualificationId.setter
    def QualificationId(self, QualificationId):
        self._QualificationId = QualificationId


    def _deserialize(self, params):
        self._SignName = params.get("SignName")
        self._SignType = params.get("SignType")
        self._DocumentType = params.get("DocumentType")
        self._International = params.get("International")
        self._UsedMethod = params.get("UsedMethod")
        self._ProofImage = params.get("ProofImage")
        self._CommissionImage = params.get("CommissionImage")
        self._Remark = params.get("Remark")
        self._QualificationId = params.get("QualificationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSmsSignResponse(AbstractModel):
    """AddSmsSign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AddSignStatus: 添加签名响应
        :type AddSignStatus: :class:`tencentcloud.sms.v20190711.models.AddSignStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AddSignStatus = None
        self._RequestId = None

    @property
    def AddSignStatus(self):
        """添加签名响应
        :rtype: :class:`tencentcloud.sms.v20190711.models.AddSignStatus`
        """
        return self._AddSignStatus

    @AddSignStatus.setter
    def AddSignStatus(self, AddSignStatus):
        self._AddSignStatus = AddSignStatus

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AddSignStatus") is not None:
            self._AddSignStatus = AddSignStatus()
            self._AddSignStatus._deserialize(params.get("AddSignStatus"))
        self._RequestId = params.get("RequestId")


class AddSmsTemplateRequest(AbstractModel):
    """AddSmsTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateName: 模板名称。
        :type TemplateName: str
        :param _TemplateContent: 模板内容。
        :type TemplateContent: str
        :param _SmsType: 短信类型，1表示营销短信，2表示通知短信，3表示验证码短信。
注：为进一步提升短信发送质量、提高短信模板审核通过率，从2024年5月16日起，腾讯云短信模板类型优化为“验证码短信”、“通知短信”、“营销短信”，可参考[关于腾讯云短信模板类型优化公告](https://cloud.tencent.com/document/product/382/106171)。新开通短信服务的客户需严格参考新的短信类型申请短信模板。
        :type SmsType: int
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param _Remark: 模板备注，例如申请原因，使用场景等。
        :type Remark: str
        """
        self._TemplateName = None
        self._TemplateContent = None
        self._SmsType = None
        self._International = None
        self._Remark = None

    @property
    def TemplateName(self):
        """模板名称。
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateContent(self):
        """模板内容。
        :rtype: str
        """
        return self._TemplateContent

    @TemplateContent.setter
    def TemplateContent(self, TemplateContent):
        self._TemplateContent = TemplateContent

    @property
    def SmsType(self):
        """短信类型，1表示营销短信，2表示通知短信，3表示验证码短信。
注：为进一步提升短信发送质量、提高短信模板审核通过率，从2024年5月16日起，腾讯云短信模板类型优化为“验证码短信”、“通知短信”、“营销短信”，可参考[关于腾讯云短信模板类型优化公告](https://cloud.tencent.com/document/product/382/106171)。新开通短信服务的客户需严格参考新的短信类型申请短信模板。
        :rtype: int
        """
        return self._SmsType

    @SmsType.setter
    def SmsType(self, SmsType):
        self._SmsType = SmsType

    @property
    def International(self):
        """是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :rtype: int
        """
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def Remark(self):
        """模板备注，例如申请原因，使用场景等。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        self._TemplateContent = params.get("TemplateContent")
        self._SmsType = params.get("SmsType")
        self._International = params.get("International")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSmsTemplateResponse(AbstractModel):
    """AddSmsTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AddTemplateStatus: 添加短信模板响应包体
        :type AddTemplateStatus: :class:`tencentcloud.sms.v20190711.models.AddTemplateStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AddTemplateStatus = None
        self._RequestId = None

    @property
    def AddTemplateStatus(self):
        """添加短信模板响应包体
        :rtype: :class:`tencentcloud.sms.v20190711.models.AddTemplateStatus`
        """
        return self._AddTemplateStatus

    @AddTemplateStatus.setter
    def AddTemplateStatus(self, AddTemplateStatus):
        self._AddTemplateStatus = AddTemplateStatus

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AddTemplateStatus") is not None:
            self._AddTemplateStatus = AddTemplateStatus()
            self._AddTemplateStatus._deserialize(params.get("AddTemplateStatus"))
        self._RequestId = params.get("RequestId")


class AddTemplateStatus(AbstractModel):
    """添加模板参数响应

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板参数
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        """模板参数
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallbackStatusStatistics(AbstractModel):
    """回执数据统计响应包体

    """

    def __init__(self):
        r"""
        :param _CallbackCount: 短信回执量统计。
        :type CallbackCount: int
        :param _RequestSuccessCount: 短信提交成功量统计。
        :type RequestSuccessCount: int
        :param _CallbackFailCount: 短信回执失败量统计。
        :type CallbackFailCount: int
        :param _CallbackSuccessCount: 短信回执成功量统计。
        :type CallbackSuccessCount: int
        :param _InternalErrorCount: 运营商内部错误统计。
        :type InternalErrorCount: int
        :param _InvalidNumberCount: 号码无效或空号统计。
        :type InvalidNumberCount: int
        :param _ShutdownErrorCount: 停机、关机等错误统计。
        :type ShutdownErrorCount: int
        :param _BlackListCount: 号码拉入黑名单统计。
        :type BlackListCount: int
        :param _FrequencyLimitCount: 运营商频率限制统计。
        :type FrequencyLimitCount: int
        """
        self._CallbackCount = None
        self._RequestSuccessCount = None
        self._CallbackFailCount = None
        self._CallbackSuccessCount = None
        self._InternalErrorCount = None
        self._InvalidNumberCount = None
        self._ShutdownErrorCount = None
        self._BlackListCount = None
        self._FrequencyLimitCount = None

    @property
    def CallbackCount(self):
        """短信回执量统计。
        :rtype: int
        """
        return self._CallbackCount

    @CallbackCount.setter
    def CallbackCount(self, CallbackCount):
        self._CallbackCount = CallbackCount

    @property
    def RequestSuccessCount(self):
        """短信提交成功量统计。
        :rtype: int
        """
        return self._RequestSuccessCount

    @RequestSuccessCount.setter
    def RequestSuccessCount(self, RequestSuccessCount):
        self._RequestSuccessCount = RequestSuccessCount

    @property
    def CallbackFailCount(self):
        """短信回执失败量统计。
        :rtype: int
        """
        return self._CallbackFailCount

    @CallbackFailCount.setter
    def CallbackFailCount(self, CallbackFailCount):
        self._CallbackFailCount = CallbackFailCount

    @property
    def CallbackSuccessCount(self):
        """短信回执成功量统计。
        :rtype: int
        """
        return self._CallbackSuccessCount

    @CallbackSuccessCount.setter
    def CallbackSuccessCount(self, CallbackSuccessCount):
        self._CallbackSuccessCount = CallbackSuccessCount

    @property
    def InternalErrorCount(self):
        """运营商内部错误统计。
        :rtype: int
        """
        return self._InternalErrorCount

    @InternalErrorCount.setter
    def InternalErrorCount(self, InternalErrorCount):
        self._InternalErrorCount = InternalErrorCount

    @property
    def InvalidNumberCount(self):
        """号码无效或空号统计。
        :rtype: int
        """
        return self._InvalidNumberCount

    @InvalidNumberCount.setter
    def InvalidNumberCount(self, InvalidNumberCount):
        self._InvalidNumberCount = InvalidNumberCount

    @property
    def ShutdownErrorCount(self):
        """停机、关机等错误统计。
        :rtype: int
        """
        return self._ShutdownErrorCount

    @ShutdownErrorCount.setter
    def ShutdownErrorCount(self, ShutdownErrorCount):
        self._ShutdownErrorCount = ShutdownErrorCount

    @property
    def BlackListCount(self):
        """号码拉入黑名单统计。
        :rtype: int
        """
        return self._BlackListCount

    @BlackListCount.setter
    def BlackListCount(self, BlackListCount):
        self._BlackListCount = BlackListCount

    @property
    def FrequencyLimitCount(self):
        """运营商频率限制统计。
        :rtype: int
        """
        return self._FrequencyLimitCount

    @FrequencyLimitCount.setter
    def FrequencyLimitCount(self, FrequencyLimitCount):
        self._FrequencyLimitCount = FrequencyLimitCount


    def _deserialize(self, params):
        self._CallbackCount = params.get("CallbackCount")
        self._RequestSuccessCount = params.get("RequestSuccessCount")
        self._CallbackFailCount = params.get("CallbackFailCount")
        self._CallbackSuccessCount = params.get("CallbackSuccessCount")
        self._InternalErrorCount = params.get("InternalErrorCount")
        self._InvalidNumberCount = params.get("InvalidNumberCount")
        self._ShutdownErrorCount = params.get("ShutdownErrorCount")
        self._BlackListCount = params.get("BlackListCount")
        self._FrequencyLimitCount = params.get("FrequencyLimitCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallbackStatusStatisticsRequest(AbstractModel):
    """CallbackStatusStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartDateTime: 开始时间，yyyymmddhh 需要拉取的起始时间，精确到小时。
        :type StartDateTime: int
        :param _EndDataTime: 结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时。
注：EndDataTime 必须大于等于 StartDateTime。
        :type EndDataTime: int
        :param _SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，示例如1400006666。
        :type SmsSdkAppid: str
        :param _Limit: 最大上限。
注：目前固定设置为0。
        :type Limit: int
        :param _Offset: 偏移量。
注：目前固定设置为0。
        :type Offset: int
        """
        self._StartDateTime = None
        self._EndDataTime = None
        self._SmsSdkAppid = None
        self._Limit = None
        self._Offset = None

    @property
    def StartDateTime(self):
        """开始时间，yyyymmddhh 需要拉取的起始时间，精确到小时。
        :rtype: int
        """
        return self._StartDateTime

    @StartDateTime.setter
    def StartDateTime(self, StartDateTime):
        self._StartDateTime = StartDateTime

    @property
    def EndDataTime(self):
        """结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时。
注：EndDataTime 必须大于等于 StartDateTime。
        :rtype: int
        """
        return self._EndDataTime

    @EndDataTime.setter
    def EndDataTime(self, EndDataTime):
        self._EndDataTime = EndDataTime

    @property
    def SmsSdkAppid(self):
        """短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，示例如1400006666。
        :rtype: str
        """
        return self._SmsSdkAppid

    @SmsSdkAppid.setter
    def SmsSdkAppid(self, SmsSdkAppid):
        self._SmsSdkAppid = SmsSdkAppid

    @property
    def Limit(self):
        """最大上限。
注：目前固定设置为0。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量。
注：目前固定设置为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._StartDateTime = params.get("StartDateTime")
        self._EndDataTime = params.get("EndDataTime")
        self._SmsSdkAppid = params.get("SmsSdkAppid")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallbackStatusStatisticsResponse(AbstractModel):
    """CallbackStatusStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CallbackStatusStatistics: 回执数据统计响应包体。
        :type CallbackStatusStatistics: :class:`tencentcloud.sms.v20190711.models.CallbackStatusStatistics`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CallbackStatusStatistics = None
        self._RequestId = None

    @property
    def CallbackStatusStatistics(self):
        """回执数据统计响应包体。
        :rtype: :class:`tencentcloud.sms.v20190711.models.CallbackStatusStatistics`
        """
        return self._CallbackStatusStatistics

    @CallbackStatusStatistics.setter
    def CallbackStatusStatistics(self, CallbackStatusStatistics):
        self._CallbackStatusStatistics = CallbackStatusStatistics

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CallbackStatusStatistics") is not None:
            self._CallbackStatusStatistics = CallbackStatusStatistics()
            self._CallbackStatusStatistics._deserialize(params.get("CallbackStatusStatistics"))
        self._RequestId = params.get("RequestId")


class DeleteSignStatus(AbstractModel):
    """删除签名响应

    """

    def __init__(self):
        r"""
        :param _DeleteStatus: 删除状态信息。
        :type DeleteStatus: str
        :param _DeleteTime: 删除时间，UNIX 时间戳（单位：秒）。
        :type DeleteTime: int
        """
        self._DeleteStatus = None
        self._DeleteTime = None

    @property
    def DeleteStatus(self):
        """删除状态信息。
        :rtype: str
        """
        return self._DeleteStatus

    @DeleteStatus.setter
    def DeleteStatus(self, DeleteStatus):
        self._DeleteStatus = DeleteStatus

    @property
    def DeleteTime(self):
        """删除时间，UNIX 时间戳（单位：秒）。
        :rtype: int
        """
        return self._DeleteTime

    @DeleteTime.setter
    def DeleteTime(self, DeleteTime):
        self._DeleteTime = DeleteTime


    def _deserialize(self, params):
        self._DeleteStatus = params.get("DeleteStatus")
        self._DeleteTime = params.get("DeleteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSmsSignRequest(AbstractModel):
    """DeleteSmsSign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SignId: 待删除的签名 ID。
        :type SignId: int
        """
        self._SignId = None

    @property
    def SignId(self):
        """待删除的签名 ID。
        :rtype: int
        """
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSmsSignResponse(AbstractModel):
    """DeleteSmsSign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeleteSignStatus: 删除签名响应
        :type DeleteSignStatus: :class:`tencentcloud.sms.v20190711.models.DeleteSignStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeleteSignStatus = None
        self._RequestId = None

    @property
    def DeleteSignStatus(self):
        """删除签名响应
        :rtype: :class:`tencentcloud.sms.v20190711.models.DeleteSignStatus`
        """
        return self._DeleteSignStatus

    @DeleteSignStatus.setter
    def DeleteSignStatus(self, DeleteSignStatus):
        self._DeleteSignStatus = DeleteSignStatus

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeleteSignStatus") is not None:
            self._DeleteSignStatus = DeleteSignStatus()
            self._DeleteSignStatus._deserialize(params.get("DeleteSignStatus"))
        self._RequestId = params.get("RequestId")


class DeleteSmsTemplateRequest(AbstractModel):
    """DeleteSmsTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 待删除的模板 ID。
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        """待删除的模板 ID。
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSmsTemplateResponse(AbstractModel):
    """DeleteSmsTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeleteTemplateStatus: 删除模板响应
        :type DeleteTemplateStatus: :class:`tencentcloud.sms.v20190711.models.DeleteTemplateStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeleteTemplateStatus = None
        self._RequestId = None

    @property
    def DeleteTemplateStatus(self):
        """删除模板响应
        :rtype: :class:`tencentcloud.sms.v20190711.models.DeleteTemplateStatus`
        """
        return self._DeleteTemplateStatus

    @DeleteTemplateStatus.setter
    def DeleteTemplateStatus(self, DeleteTemplateStatus):
        self._DeleteTemplateStatus = DeleteTemplateStatus

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeleteTemplateStatus") is not None:
            self._DeleteTemplateStatus = DeleteTemplateStatus()
            self._DeleteTemplateStatus._deserialize(params.get("DeleteTemplateStatus"))
        self._RequestId = params.get("RequestId")


class DeleteTemplateStatus(AbstractModel):
    """删除模板响应

    """

    def __init__(self):
        r"""
        :param _DeleteStatus: 删除状态信息。
        :type DeleteStatus: str
        :param _DeleteTime: 删除时间，UNIX 时间戳（单位：秒）。
        :type DeleteTime: int
        """
        self._DeleteStatus = None
        self._DeleteTime = None

    @property
    def DeleteStatus(self):
        """删除状态信息。
        :rtype: str
        """
        return self._DeleteStatus

    @DeleteStatus.setter
    def DeleteStatus(self, DeleteStatus):
        self._DeleteStatus = DeleteStatus

    @property
    def DeleteTime(self):
        """删除时间，UNIX 时间戳（单位：秒）。
        :rtype: int
        """
        return self._DeleteTime

    @DeleteTime.setter
    def DeleteTime(self, DeleteTime):
        self._DeleteTime = DeleteTime


    def _deserialize(self, params):
        self._DeleteStatus = params.get("DeleteStatus")
        self._DeleteTime = params.get("DeleteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSignListStatus(AbstractModel):
    """获取短信签名信息响应

    """

    def __init__(self):
        r"""
        :param _SignId: 签名Id
        :type SignId: int
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param _StatusCode: 申请签名状态。其中0表示审核通过且已生效，1表示审核中，2表示审核通过待生效，-1表示审核未通过或审核失败。
        :type StatusCode: int
        :param _ReviewReply: 审核回复，审核人员审核后给出的回复，通常是审核未通过的原因。
        :type ReviewReply: str
        :param _SignName: 签名名称。
        :type SignName: str
        :param _CreateTime: 提交审核时间，UNIX 时间戳（单位：秒）。
        :type CreateTime: int
        :param _QualificationId: 国内短信的资质 ID。资质 ID 信息可前往国内短信的 [实名资质管理](https://console.cloud.tencent.com/smsv2/enterprise) 页查看。
注：国际短信不涉及，默认为0。
        :type QualificationId: int
        :param _QualificationName: 国内短信的资质名称。
注：国际短信不涉及，默认为空。
        :type QualificationName: str
        :param _QualificationStatusCode: 国内短信的资质状态。其中0表示待审核，1表示已通过，2表示已拒绝，3表示待补充后提交，4表示变更后待审核，5表示变更后被驳回。可参考 [实名资质审核状态说明](https://cloud.tencent.com/document/product/382/13444#.E5.AE.A1.E6.A0.B8.E7.8A.B6.E6.80.81.E8.AF.B4.E6.98.8E) 。
注：国际短信不涉及，默认为0。
        :type QualificationStatusCode: int
        """
        self._SignId = None
        self._International = None
        self._StatusCode = None
        self._ReviewReply = None
        self._SignName = None
        self._CreateTime = None
        self._QualificationId = None
        self._QualificationName = None
        self._QualificationStatusCode = None

    @property
    def SignId(self):
        """签名Id
        :rtype: int
        """
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def International(self):
        """是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :rtype: int
        """
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def StatusCode(self):
        """申请签名状态。其中0表示审核通过且已生效，1表示审核中，2表示审核通过待生效，-1表示审核未通过或审核失败。
        :rtype: int
        """
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def ReviewReply(self):
        """审核回复，审核人员审核后给出的回复，通常是审核未通过的原因。
        :rtype: str
        """
        return self._ReviewReply

    @ReviewReply.setter
    def ReviewReply(self, ReviewReply):
        self._ReviewReply = ReviewReply

    @property
    def SignName(self):
        """签名名称。
        :rtype: str
        """
        return self._SignName

    @SignName.setter
    def SignName(self, SignName):
        self._SignName = SignName

    @property
    def CreateTime(self):
        """提交审核时间，UNIX 时间戳（单位：秒）。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def QualificationId(self):
        """国内短信的资质 ID。资质 ID 信息可前往国内短信的 [实名资质管理](https://console.cloud.tencent.com/smsv2/enterprise) 页查看。
注：国际短信不涉及，默认为0。
        :rtype: int
        """
        return self._QualificationId

    @QualificationId.setter
    def QualificationId(self, QualificationId):
        self._QualificationId = QualificationId

    @property
    def QualificationName(self):
        """国内短信的资质名称。
注：国际短信不涉及，默认为空。
        :rtype: str
        """
        return self._QualificationName

    @QualificationName.setter
    def QualificationName(self, QualificationName):
        self._QualificationName = QualificationName

    @property
    def QualificationStatusCode(self):
        """国内短信的资质状态。其中0表示待审核，1表示已通过，2表示已拒绝，3表示待补充后提交，4表示变更后待审核，5表示变更后被驳回。可参考 [实名资质审核状态说明](https://cloud.tencent.com/document/product/382/13444#.E5.AE.A1.E6.A0.B8.E7.8A.B6.E6.80.81.E8.AF.B4.E6.98.8E) 。
注：国际短信不涉及，默认为0。
        :rtype: int
        """
        return self._QualificationStatusCode

    @QualificationStatusCode.setter
    def QualificationStatusCode(self, QualificationStatusCode):
        self._QualificationStatusCode = QualificationStatusCode


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        self._International = params.get("International")
        self._StatusCode = params.get("StatusCode")
        self._ReviewReply = params.get("ReviewReply")
        self._SignName = params.get("SignName")
        self._CreateTime = params.get("CreateTime")
        self._QualificationId = params.get("QualificationId")
        self._QualificationName = params.get("QualificationName")
        self._QualificationStatusCode = params.get("QualificationStatusCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsSignListRequest(AbstractModel):
    """DescribeSmsSignList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SignIdSet: 签名 ID 数组。
        :type SignIdSet: list of int non-negative
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        """
        self._SignIdSet = None
        self._International = None

    @property
    def SignIdSet(self):
        """签名 ID 数组。
        :rtype: list of int non-negative
        """
        return self._SignIdSet

    @SignIdSet.setter
    def SignIdSet(self, SignIdSet):
        self._SignIdSet = SignIdSet

    @property
    def International(self):
        """是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :rtype: int
        """
        return self._International

    @International.setter
    def International(self, International):
        self._International = International


    def _deserialize(self, params):
        self._SignIdSet = params.get("SignIdSet")
        self._International = params.get("International")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsSignListResponse(AbstractModel):
    """DescribeSmsSignList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DescribeSignListStatusSet: 获取签名信息响应
        :type DescribeSignListStatusSet: list of DescribeSignListStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DescribeSignListStatusSet = None
        self._RequestId = None

    @property
    def DescribeSignListStatusSet(self):
        """获取签名信息响应
        :rtype: list of DescribeSignListStatus
        """
        return self._DescribeSignListStatusSet

    @DescribeSignListStatusSet.setter
    def DescribeSignListStatusSet(self, DescribeSignListStatusSet):
        self._DescribeSignListStatusSet = DescribeSignListStatusSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DescribeSignListStatusSet") is not None:
            self._DescribeSignListStatusSet = []
            for item in params.get("DescribeSignListStatusSet"):
                obj = DescribeSignListStatus()
                obj._deserialize(item)
                self._DescribeSignListStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSmsTemplateListRequest(AbstractModel):
    """DescribeSmsTemplateList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateIdSet: 模板 ID 数组。
        :type TemplateIdSet: list of int non-negative
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        """
        self._TemplateIdSet = None
        self._International = None

    @property
    def TemplateIdSet(self):
        """模板 ID 数组。
        :rtype: list of int non-negative
        """
        return self._TemplateIdSet

    @TemplateIdSet.setter
    def TemplateIdSet(self, TemplateIdSet):
        self._TemplateIdSet = TemplateIdSet

    @property
    def International(self):
        """是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :rtype: int
        """
        return self._International

    @International.setter
    def International(self, International):
        self._International = International


    def _deserialize(self, params):
        self._TemplateIdSet = params.get("TemplateIdSet")
        self._International = params.get("International")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsTemplateListResponse(AbstractModel):
    """DescribeSmsTemplateList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DescribeTemplateStatusSet: 获取短信模板信息响应
        :type DescribeTemplateStatusSet: list of DescribeTemplateListStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DescribeTemplateStatusSet = None
        self._RequestId = None

    @property
    def DescribeTemplateStatusSet(self):
        """获取短信模板信息响应
        :rtype: list of DescribeTemplateListStatus
        """
        return self._DescribeTemplateStatusSet

    @DescribeTemplateStatusSet.setter
    def DescribeTemplateStatusSet(self, DescribeTemplateStatusSet):
        self._DescribeTemplateStatusSet = DescribeTemplateStatusSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DescribeTemplateStatusSet") is not None:
            self._DescribeTemplateStatusSet = []
            for item in params.get("DescribeTemplateStatusSet"):
                obj = DescribeTemplateListStatus()
                obj._deserialize(item)
                self._DescribeTemplateStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTemplateListStatus(AbstractModel):
    """获取短信模板信息响应

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板Id
        :type TemplateId: int
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param _StatusCode: 申请模板状态，其中0表示审核通过且已生效，1表示审核中，2表示审核通过待生效，-1表示审核未通过或审核失败。
        :type StatusCode: int
        :param _ReviewReply: 审核回复，审核人员审核后给出的回复，通常是审核未通过的原因。
        :type ReviewReply: str
        :param _TemplateName: 模板名称。
        :type TemplateName: str
        :param _CreateTime: 提交审核时间，UNIX 时间戳（单位：秒）。
        :type CreateTime: int
        """
        self._TemplateId = None
        self._International = None
        self._StatusCode = None
        self._ReviewReply = None
        self._TemplateName = None
        self._CreateTime = None

    @property
    def TemplateId(self):
        """模板Id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def International(self):
        """是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :rtype: int
        """
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def StatusCode(self):
        """申请模板状态，其中0表示审核通过且已生效，1表示审核中，2表示审核通过待生效，-1表示审核未通过或审核失败。
        :rtype: int
        """
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def ReviewReply(self):
        """审核回复，审核人员审核后给出的回复，通常是审核未通过的原因。
        :rtype: str
        """
        return self._ReviewReply

    @ReviewReply.setter
    def ReviewReply(self, ReviewReply):
        self._ReviewReply = ReviewReply

    @property
    def TemplateName(self):
        """模板名称。
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def CreateTime(self):
        """提交审核时间，UNIX 时间戳（单位：秒）。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._International = params.get("International")
        self._StatusCode = params.get("StatusCode")
        self._ReviewReply = params.get("ReviewReply")
        self._TemplateName = params.get("TemplateName")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySignStatus(AbstractModel):
    """修改签名响应

    """

    def __init__(self):
        r"""
        :param _SignId: 签名Id
        :type SignId: int
        :param _SignApplyId: 签名修改申请Id
        :type SignApplyId: str
        """
        self._SignId = None
        self._SignApplyId = None

    @property
    def SignId(self):
        """签名Id
        :rtype: int
        """
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def SignApplyId(self):
        """签名修改申请Id
        :rtype: str
        """
        return self._SignApplyId

    @SignApplyId.setter
    def SignApplyId(self, SignApplyId):
        self._SignApplyId = SignApplyId


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        self._SignApplyId = params.get("SignApplyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySmsSignRequest(AbstractModel):
    """ModifySmsSign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SignId: 待修改的签名 ID。
        :type SignId: int
        :param _SignName: 签名名称。
        :type SignName: str
        :param _SignType: 签名类型。其中每种类型后面标注了其可选的 DocumentType（证明类型）：
0：公司，可选 DocumentType 有（0，1）。
1：APP，可选 DocumentType 有（0，1，2，3，4） 。
4：商标，可选 DocumentType 有（7）。
5：政府/机关事业单位/其他机构，可选 DocumentType 有（2，3）。
注1：必须按照对应关系选择证明类型，否则会审核失败。
注2：签名类型2（网站）、3（公众号）、6（小程序）已不再支持，具体可参考 [关于腾讯云短信签名申请规则更新的公告](https://cloud.tencent.com/document/product/382/116397)。
        :type SignType: int
        :param _DocumentType: 证明类型：
0：三证合一。
1：企业营业执照。
2：组织机构代码证书。
3：社会信用代码证书。
4：应用后台管理截图（个人开发APP）。
7：商标注册书。
注：证明类型5（网站备案后台截图）、6（小程序设置页面截图）、8（公众号设置页面截图）已不再支持，具体可参考 [关于腾讯云短信签名申请规则更新的公告](https://cloud.tencent.com/document/product/382/116397)。
        :type DocumentType: int
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
注：需要和待修改签名International值保持一致，该参数不能直接修改国内签名到国际签名。
        :type International: int
        :param _UsedMethod: 签名用途：
0：自用。
1：他用。
        :type UsedMethod: int
        :param _ProofImage: 签名对应的资质证明图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。
        :type ProofImage: str
        :param _CommissionImage: 委托授权证明。选择 UsedMethod 为他用之后需要提交委托的授权证明。
图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。
注：只有 UsedMethod 在选择为 1（他用）时，这个字段才会生效。
        :type CommissionImage: str
        :param _Remark: 签名的申请备注。
        :type Remark: str
        :param _QualificationId: 已审核通过的国内短信的资质 ID。资质 ID 信息可前往国内短信的 [实名资质管理](https://console.cloud.tencent.com/smsv2/enterprise) 页查看。<dx-alert infotype="notice" title="说明"><ul><li>国内短信需填写资质ID，国际短信无需填写。</li></ul></dx-alert>
        :type QualificationId: int
        """
        self._SignId = None
        self._SignName = None
        self._SignType = None
        self._DocumentType = None
        self._International = None
        self._UsedMethod = None
        self._ProofImage = None
        self._CommissionImage = None
        self._Remark = None
        self._QualificationId = None

    @property
    def SignId(self):
        """待修改的签名 ID。
        :rtype: int
        """
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def SignName(self):
        """签名名称。
        :rtype: str
        """
        return self._SignName

    @SignName.setter
    def SignName(self, SignName):
        self._SignName = SignName

    @property
    def SignType(self):
        """签名类型。其中每种类型后面标注了其可选的 DocumentType（证明类型）：
0：公司，可选 DocumentType 有（0，1）。
1：APP，可选 DocumentType 有（0，1，2，3，4） 。
4：商标，可选 DocumentType 有（7）。
5：政府/机关事业单位/其他机构，可选 DocumentType 有（2，3）。
注1：必须按照对应关系选择证明类型，否则会审核失败。
注2：签名类型2（网站）、3（公众号）、6（小程序）已不再支持，具体可参考 [关于腾讯云短信签名申请规则更新的公告](https://cloud.tencent.com/document/product/382/116397)。
        :rtype: int
        """
        return self._SignType

    @SignType.setter
    def SignType(self, SignType):
        self._SignType = SignType

    @property
    def DocumentType(self):
        """证明类型：
0：三证合一。
1：企业营业执照。
2：组织机构代码证书。
3：社会信用代码证书。
4：应用后台管理截图（个人开发APP）。
7：商标注册书。
注：证明类型5（网站备案后台截图）、6（小程序设置页面截图）、8（公众号设置页面截图）已不再支持，具体可参考 [关于腾讯云短信签名申请规则更新的公告](https://cloud.tencent.com/document/product/382/116397)。
        :rtype: int
        """
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def International(self):
        """是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
注：需要和待修改签名International值保持一致，该参数不能直接修改国内签名到国际签名。
        :rtype: int
        """
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def UsedMethod(self):
        """签名用途：
0：自用。
1：他用。
        :rtype: int
        """
        return self._UsedMethod

    @UsedMethod.setter
    def UsedMethod(self, UsedMethod):
        self._UsedMethod = UsedMethod

    @property
    def ProofImage(self):
        """签名对应的资质证明图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。
        :rtype: str
        """
        return self._ProofImage

    @ProofImage.setter
    def ProofImage(self, ProofImage):
        self._ProofImage = ProofImage

    @property
    def CommissionImage(self):
        """委托授权证明。选择 UsedMethod 为他用之后需要提交委托的授权证明。
图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。
注：只有 UsedMethod 在选择为 1（他用）时，这个字段才会生效。
        :rtype: str
        """
        return self._CommissionImage

    @CommissionImage.setter
    def CommissionImage(self, CommissionImage):
        self._CommissionImage = CommissionImage

    @property
    def Remark(self):
        """签名的申请备注。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def QualificationId(self):
        """已审核通过的国内短信的资质 ID。资质 ID 信息可前往国内短信的 [实名资质管理](https://console.cloud.tencent.com/smsv2/enterprise) 页查看。<dx-alert infotype="notice" title="说明"><ul><li>国内短信需填写资质ID，国际短信无需填写。</li></ul></dx-alert>
        :rtype: int
        """
        return self._QualificationId

    @QualificationId.setter
    def QualificationId(self, QualificationId):
        self._QualificationId = QualificationId


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        self._SignName = params.get("SignName")
        self._SignType = params.get("SignType")
        self._DocumentType = params.get("DocumentType")
        self._International = params.get("International")
        self._UsedMethod = params.get("UsedMethod")
        self._ProofImage = params.get("ProofImage")
        self._CommissionImage = params.get("CommissionImage")
        self._Remark = params.get("Remark")
        self._QualificationId = params.get("QualificationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySmsSignResponse(AbstractModel):
    """ModifySmsSign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModifySignStatus: 修改签名响应
        :type ModifySignStatus: :class:`tencentcloud.sms.v20190711.models.ModifySignStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModifySignStatus = None
        self._RequestId = None

    @property
    def ModifySignStatus(self):
        """修改签名响应
        :rtype: :class:`tencentcloud.sms.v20190711.models.ModifySignStatus`
        """
        return self._ModifySignStatus

    @ModifySignStatus.setter
    def ModifySignStatus(self, ModifySignStatus):
        self._ModifySignStatus = ModifySignStatus

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ModifySignStatus") is not None:
            self._ModifySignStatus = ModifySignStatus()
            self._ModifySignStatus._deserialize(params.get("ModifySignStatus"))
        self._RequestId = params.get("RequestId")


class ModifySmsTemplateRequest(AbstractModel):
    """ModifySmsTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 待修改的模板的模板 ID。
        :type TemplateId: int
        :param _TemplateName: 新的模板名称。
        :type TemplateName: str
        :param _TemplateContent: 新的模板内容。
        :type TemplateContent: str
        :param _SmsType: 短信类型，1表示营销短信，2表示通知短信，3表示验证码短信。
注：为进一步提升短信发送质量、提高短信模板审核通过率，从2024年5月16日起，腾讯云短信模板类型优化为“验证码短信”、“通知短信”、“营销短信”，可参考[关于腾讯云短信模板类型优化公告](https://cloud.tencent.com/document/product/382/106171)。新开通短信服务的客户需严格参考新的短信类型申请短信模板。
        :type SmsType: int
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param _Remark: 模板备注，例如申请原因，使用场景等。
        :type Remark: str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TemplateContent = None
        self._SmsType = None
        self._International = None
        self._Remark = None

    @property
    def TemplateId(self):
        """待修改的模板的模板 ID。
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        """新的模板名称。
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateContent(self):
        """新的模板内容。
        :rtype: str
        """
        return self._TemplateContent

    @TemplateContent.setter
    def TemplateContent(self, TemplateContent):
        self._TemplateContent = TemplateContent

    @property
    def SmsType(self):
        """短信类型，1表示营销短信，2表示通知短信，3表示验证码短信。
注：为进一步提升短信发送质量、提高短信模板审核通过率，从2024年5月16日起，腾讯云短信模板类型优化为“验证码短信”、“通知短信”、“营销短信”，可参考[关于腾讯云短信模板类型优化公告](https://cloud.tencent.com/document/product/382/106171)。新开通短信服务的客户需严格参考新的短信类型申请短信模板。
        :rtype: int
        """
        return self._SmsType

    @SmsType.setter
    def SmsType(self, SmsType):
        self._SmsType = SmsType

    @property
    def International(self):
        """是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :rtype: int
        """
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def Remark(self):
        """模板备注，例如申请原因，使用场景等。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._TemplateContent = params.get("TemplateContent")
        self._SmsType = params.get("SmsType")
        self._International = params.get("International")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySmsTemplateResponse(AbstractModel):
    """ModifySmsTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModifyTemplateStatus: 修改模板参数响应
        :type ModifyTemplateStatus: :class:`tencentcloud.sms.v20190711.models.ModifyTemplateStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModifyTemplateStatus = None
        self._RequestId = None

    @property
    def ModifyTemplateStatus(self):
        """修改模板参数响应
        :rtype: :class:`tencentcloud.sms.v20190711.models.ModifyTemplateStatus`
        """
        return self._ModifyTemplateStatus

    @ModifyTemplateStatus.setter
    def ModifyTemplateStatus(self, ModifyTemplateStatus):
        self._ModifyTemplateStatus = ModifyTemplateStatus

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ModifyTemplateStatus") is not None:
            self._ModifyTemplateStatus = ModifyTemplateStatus()
            self._ModifyTemplateStatus._deserialize(params.get("ModifyTemplateStatus"))
        self._RequestId = params.get("RequestId")


class ModifyTemplateStatus(AbstractModel):
    """修改模板参数响应

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板参数
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        """模板参数
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsReplyStatus(AbstractModel):
    """短信回复状态

    """

    def __init__(self):
        r"""
        :param _ExtendCode: 短信码号扩展号，默认未开通，如需开通请联系 [sms helper](https://cloud.tencent.com/document/product/382/3773)。
        :type ExtendCode: str
        :param _NationCode: 国家（或地区）码。
        :type NationCode: str
        :param _PhoneNumber: 手机号码，E.164标准，+[国家或地区码][手机号] ，示例如：+8618501234444， 其中前面有一个+号 ，86为国家码，18501234444为手机号。
        :type PhoneNumber: str
        :param _Sign: 短信签名。
        :type Sign: str
        :param _ReplyContent: 用户回复的内容。
        :type ReplyContent: str
        :param _ReplyTime: 回复时间（例如：2019-10-08 17:18:37）。
        :type ReplyTime: str
        :param _ReplyUnixTime: 回复时间，UNIX 时间戳（单位：秒）。
        :type ReplyUnixTime: int
        """
        self._ExtendCode = None
        self._NationCode = None
        self._PhoneNumber = None
        self._Sign = None
        self._ReplyContent = None
        self._ReplyTime = None
        self._ReplyUnixTime = None

    @property
    def ExtendCode(self):
        """短信码号扩展号，默认未开通，如需开通请联系 [sms helper](https://cloud.tencent.com/document/product/382/3773)。
        :rtype: str
        """
        return self._ExtendCode

    @ExtendCode.setter
    def ExtendCode(self, ExtendCode):
        self._ExtendCode = ExtendCode

    @property
    def NationCode(self):
        """国家（或地区）码。
        :rtype: str
        """
        return self._NationCode

    @NationCode.setter
    def NationCode(self, NationCode):
        self._NationCode = NationCode

    @property
    def PhoneNumber(self):
        """手机号码，E.164标准，+[国家或地区码][手机号] ，示例如：+8618501234444， 其中前面有一个+号 ，86为国家码，18501234444为手机号。
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Sign(self):
        """短信签名。
        :rtype: str
        """
        return self._Sign

    @Sign.setter
    def Sign(self, Sign):
        self._Sign = Sign

    @property
    def ReplyContent(self):
        """用户回复的内容。
        :rtype: str
        """
        return self._ReplyContent

    @ReplyContent.setter
    def ReplyContent(self, ReplyContent):
        self._ReplyContent = ReplyContent

    @property
    def ReplyTime(self):
        """回复时间（例如：2019-10-08 17:18:37）。
        :rtype: str
        """
        return self._ReplyTime

    @ReplyTime.setter
    def ReplyTime(self, ReplyTime):
        self._ReplyTime = ReplyTime

    @property
    def ReplyUnixTime(self):
        """回复时间，UNIX 时间戳（单位：秒）。
        :rtype: int
        """
        return self._ReplyUnixTime

    @ReplyUnixTime.setter
    def ReplyUnixTime(self, ReplyUnixTime):
        self._ReplyUnixTime = ReplyUnixTime


    def _deserialize(self, params):
        self._ExtendCode = params.get("ExtendCode")
        self._NationCode = params.get("NationCode")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Sign = params.get("Sign")
        self._ReplyContent = params.get("ReplyContent")
        self._ReplyTime = params.get("ReplyTime")
        self._ReplyUnixTime = params.get("ReplyUnixTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsReplyStatusByPhoneNumberRequest(AbstractModel):
    """PullSmsReplyStatusByPhoneNumber请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SendDateTime: 拉取起始时间，UNIX 时间戳（时间：秒）。
注：最大可拉取当前时期7天前的数据。
        :type SendDateTime: int
        :param _Offset: 偏移量。
注：目前固定设置为0。
        :type Offset: int
        :param _Limit: 拉取最大条数，最多 100。
        :type Limit: int
        :param _PhoneNumber: 下发目的手机号码，依据 E.164 标准为：+[国家（或地区）码][手机号] ，示例如：+8618501234444， 其中前面有一个+号 ，86为国家码，18501234444为手机号。
        :type PhoneNumber: str
        :param _SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，例如1400006666。
        :type SmsSdkAppid: str
        :param _EndDateTime: 拉取截止时间，UNIX 时间戳（时间：秒）。
        :type EndDateTime: int
        """
        self._SendDateTime = None
        self._Offset = None
        self._Limit = None
        self._PhoneNumber = None
        self._SmsSdkAppid = None
        self._EndDateTime = None

    @property
    def SendDateTime(self):
        """拉取起始时间，UNIX 时间戳（时间：秒）。
注：最大可拉取当前时期7天前的数据。
        :rtype: int
        """
        return self._SendDateTime

    @SendDateTime.setter
    def SendDateTime(self, SendDateTime):
        self._SendDateTime = SendDateTime

    @property
    def Offset(self):
        """偏移量。
注：目前固定设置为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """拉取最大条数，最多 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PhoneNumber(self):
        """下发目的手机号码，依据 E.164 标准为：+[国家（或地区）码][手机号] ，示例如：+8618501234444， 其中前面有一个+号 ，86为国家码，18501234444为手机号。
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def SmsSdkAppid(self):
        """短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，例如1400006666。
        :rtype: str
        """
        return self._SmsSdkAppid

    @SmsSdkAppid.setter
    def SmsSdkAppid(self, SmsSdkAppid):
        self._SmsSdkAppid = SmsSdkAppid

    @property
    def EndDateTime(self):
        """拉取截止时间，UNIX 时间戳（时间：秒）。
        :rtype: int
        """
        return self._EndDateTime

    @EndDateTime.setter
    def EndDateTime(self, EndDateTime):
        self._EndDateTime = EndDateTime


    def _deserialize(self, params):
        self._SendDateTime = params.get("SendDateTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PhoneNumber = params.get("PhoneNumber")
        self._SmsSdkAppid = params.get("SmsSdkAppid")
        self._EndDateTime = params.get("EndDateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsReplyStatusByPhoneNumberResponse(AbstractModel):
    """PullSmsReplyStatusByPhoneNumber返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PullSmsReplyStatusSet: 回复状态响应集合。
        :type PullSmsReplyStatusSet: list of PullSmsReplyStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PullSmsReplyStatusSet = None
        self._RequestId = None

    @property
    def PullSmsReplyStatusSet(self):
        """回复状态响应集合。
        :rtype: list of PullSmsReplyStatus
        """
        return self._PullSmsReplyStatusSet

    @PullSmsReplyStatusSet.setter
    def PullSmsReplyStatusSet(self, PullSmsReplyStatusSet):
        self._PullSmsReplyStatusSet = PullSmsReplyStatusSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PullSmsReplyStatusSet") is not None:
            self._PullSmsReplyStatusSet = []
            for item in params.get("PullSmsReplyStatusSet"):
                obj = PullSmsReplyStatus()
                obj._deserialize(item)
                self._PullSmsReplyStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class PullSmsReplyStatusRequest(AbstractModel):
    """PullSmsReplyStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 拉取最大条数，最多100条。
        :type Limit: int
        :param _SmsSdkAppid: 短信 SdkAppid 在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际 SdkAppid，例如1400006666。
        :type SmsSdkAppid: str
        """
        self._Limit = None
        self._SmsSdkAppid = None

    @property
    def Limit(self):
        """拉取最大条数，最多100条。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SmsSdkAppid(self):
        """短信 SdkAppid 在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际 SdkAppid，例如1400006666。
        :rtype: str
        """
        return self._SmsSdkAppid

    @SmsSdkAppid.setter
    def SmsSdkAppid(self, SmsSdkAppid):
        self._SmsSdkAppid = SmsSdkAppid


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._SmsSdkAppid = params.get("SmsSdkAppid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsReplyStatusResponse(AbstractModel):
    """PullSmsReplyStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PullSmsReplyStatusSet: 回复状态响应集合。
        :type PullSmsReplyStatusSet: list of PullSmsReplyStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PullSmsReplyStatusSet = None
        self._RequestId = None

    @property
    def PullSmsReplyStatusSet(self):
        """回复状态响应集合。
        :rtype: list of PullSmsReplyStatus
        """
        return self._PullSmsReplyStatusSet

    @PullSmsReplyStatusSet.setter
    def PullSmsReplyStatusSet(self, PullSmsReplyStatusSet):
        self._PullSmsReplyStatusSet = PullSmsReplyStatusSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PullSmsReplyStatusSet") is not None:
            self._PullSmsReplyStatusSet = []
            for item in params.get("PullSmsReplyStatusSet"):
                obj = PullSmsReplyStatus()
                obj._deserialize(item)
                self._PullSmsReplyStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class PullSmsSendStatus(AbstractModel):
    """短信的下发状态详细信息

    """

    def __init__(self):
        r"""
        :param _UserReceiveTime: 用户实际接收到短信的时间。
        :type UserReceiveTime: str
        :param _UserReceiveUnixTime: 用户实际接收到短信的时间，UNIX 时间戳（单位：秒）。
        :type UserReceiveUnixTime: int
        :param _NationCode: 国家（或地区）码。
        :type NationCode: str
        :param _PurePhoneNumber: 手机号码,e.164标准，+[国家或地区码][手机号] ，示例如：+8618501234444， 其中前面有一个+号 ，86为国家码，18501234444为手机号。
        :type PurePhoneNumber: str
        :param _PhoneNumber: 手机号码，普通格式，示例如：18501234444。
        :type PhoneNumber: str
        :param _SerialNo: 本次发送标识 ID。
        :type SerialNo: str
        :param _ReportStatus: 实际是否收到短信接收状态，SUCCESS（成功）、FAIL（失败）。
        :type ReportStatus: str
        :param _Description: 用户接收短信状态描述。
        :type Description: str
        """
        self._UserReceiveTime = None
        self._UserReceiveUnixTime = None
        self._NationCode = None
        self._PurePhoneNumber = None
        self._PhoneNumber = None
        self._SerialNo = None
        self._ReportStatus = None
        self._Description = None

    @property
    def UserReceiveTime(self):
        """用户实际接收到短信的时间。
        :rtype: str
        """
        return self._UserReceiveTime

    @UserReceiveTime.setter
    def UserReceiveTime(self, UserReceiveTime):
        self._UserReceiveTime = UserReceiveTime

    @property
    def UserReceiveUnixTime(self):
        """用户实际接收到短信的时间，UNIX 时间戳（单位：秒）。
        :rtype: int
        """
        return self._UserReceiveUnixTime

    @UserReceiveUnixTime.setter
    def UserReceiveUnixTime(self, UserReceiveUnixTime):
        self._UserReceiveUnixTime = UserReceiveUnixTime

    @property
    def NationCode(self):
        """国家（或地区）码。
        :rtype: str
        """
        return self._NationCode

    @NationCode.setter
    def NationCode(self, NationCode):
        self._NationCode = NationCode

    @property
    def PurePhoneNumber(self):
        """手机号码,e.164标准，+[国家或地区码][手机号] ，示例如：+8618501234444， 其中前面有一个+号 ，86为国家码，18501234444为手机号。
        :rtype: str
        """
        return self._PurePhoneNumber

    @PurePhoneNumber.setter
    def PurePhoneNumber(self, PurePhoneNumber):
        self._PurePhoneNumber = PurePhoneNumber

    @property
    def PhoneNumber(self):
        """手机号码，普通格式，示例如：18501234444。
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def SerialNo(self):
        """本次发送标识 ID。
        :rtype: str
        """
        return self._SerialNo

    @SerialNo.setter
    def SerialNo(self, SerialNo):
        self._SerialNo = SerialNo

    @property
    def ReportStatus(self):
        """实际是否收到短信接收状态，SUCCESS（成功）、FAIL（失败）。
        :rtype: str
        """
        return self._ReportStatus

    @ReportStatus.setter
    def ReportStatus(self, ReportStatus):
        self._ReportStatus = ReportStatus

    @property
    def Description(self):
        """用户接收短信状态描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._UserReceiveTime = params.get("UserReceiveTime")
        self._UserReceiveUnixTime = params.get("UserReceiveUnixTime")
        self._NationCode = params.get("NationCode")
        self._PurePhoneNumber = params.get("PurePhoneNumber")
        self._PhoneNumber = params.get("PhoneNumber")
        self._SerialNo = params.get("SerialNo")
        self._ReportStatus = params.get("ReportStatus")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsSendStatusByPhoneNumberRequest(AbstractModel):
    """PullSmsSendStatusByPhoneNumber请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SendDateTime: 拉取起始时间，UNIX 时间戳（时间：秒）。
注：最大可拉取当前时期7天前的数据。
        :type SendDateTime: int
        :param _Offset: 偏移量。
注：目前固定设置为0。
        :type Offset: int
        :param _Limit: 拉取最大条数，最多 100。
        :type Limit: int
        :param _PhoneNumber: 下发目的手机号码，依据 E.164 标准为：+[国家（或地区）码][手机号] ，示例如：+8618501234444， 其中前面有一个+号 ，86为国家码，18501234444为手机号。
        :type PhoneNumber: str
        :param _SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，例如1400006666。
        :type SmsSdkAppid: str
        :param _EndDateTime: 拉取截止时间，UNIX 时间戳（时间：秒）。
        :type EndDateTime: int
        """
        self._SendDateTime = None
        self._Offset = None
        self._Limit = None
        self._PhoneNumber = None
        self._SmsSdkAppid = None
        self._EndDateTime = None

    @property
    def SendDateTime(self):
        """拉取起始时间，UNIX 时间戳（时间：秒）。
注：最大可拉取当前时期7天前的数据。
        :rtype: int
        """
        return self._SendDateTime

    @SendDateTime.setter
    def SendDateTime(self, SendDateTime):
        self._SendDateTime = SendDateTime

    @property
    def Offset(self):
        """偏移量。
注：目前固定设置为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """拉取最大条数，最多 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PhoneNumber(self):
        """下发目的手机号码，依据 E.164 标准为：+[国家（或地区）码][手机号] ，示例如：+8618501234444， 其中前面有一个+号 ，86为国家码，18501234444为手机号。
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def SmsSdkAppid(self):
        """短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，例如1400006666。
        :rtype: str
        """
        return self._SmsSdkAppid

    @SmsSdkAppid.setter
    def SmsSdkAppid(self, SmsSdkAppid):
        self._SmsSdkAppid = SmsSdkAppid

    @property
    def EndDateTime(self):
        """拉取截止时间，UNIX 时间戳（时间：秒）。
        :rtype: int
        """
        return self._EndDateTime

    @EndDateTime.setter
    def EndDateTime(self, EndDateTime):
        self._EndDateTime = EndDateTime


    def _deserialize(self, params):
        self._SendDateTime = params.get("SendDateTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PhoneNumber = params.get("PhoneNumber")
        self._SmsSdkAppid = params.get("SmsSdkAppid")
        self._EndDateTime = params.get("EndDateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsSendStatusByPhoneNumberResponse(AbstractModel):
    """PullSmsSendStatusByPhoneNumber返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PullSmsSendStatusSet: 下发状态响应集合。
        :type PullSmsSendStatusSet: list of PullSmsSendStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PullSmsSendStatusSet = None
        self._RequestId = None

    @property
    def PullSmsSendStatusSet(self):
        """下发状态响应集合。
        :rtype: list of PullSmsSendStatus
        """
        return self._PullSmsSendStatusSet

    @PullSmsSendStatusSet.setter
    def PullSmsSendStatusSet(self, PullSmsSendStatusSet):
        self._PullSmsSendStatusSet = PullSmsSendStatusSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PullSmsSendStatusSet") is not None:
            self._PullSmsSendStatusSet = []
            for item in params.get("PullSmsSendStatusSet"):
                obj = PullSmsSendStatus()
                obj._deserialize(item)
                self._PullSmsSendStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class PullSmsSendStatusRequest(AbstractModel):
    """PullSmsSendStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 拉取最大条数，最多100条。
        :type Limit: int
        :param _SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，例如1400006666。
        :type SmsSdkAppid: str
        """
        self._Limit = None
        self._SmsSdkAppid = None

    @property
    def Limit(self):
        """拉取最大条数，最多100条。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SmsSdkAppid(self):
        """短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，例如1400006666。
        :rtype: str
        """
        return self._SmsSdkAppid

    @SmsSdkAppid.setter
    def SmsSdkAppid(self, SmsSdkAppid):
        self._SmsSdkAppid = SmsSdkAppid


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._SmsSdkAppid = params.get("SmsSdkAppid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsSendStatusResponse(AbstractModel):
    """PullSmsSendStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PullSmsSendStatusSet: 下发状态响应集合。
        :type PullSmsSendStatusSet: list of PullSmsSendStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PullSmsSendStatusSet = None
        self._RequestId = None

    @property
    def PullSmsSendStatusSet(self):
        """下发状态响应集合。
        :rtype: list of PullSmsSendStatus
        """
        return self._PullSmsSendStatusSet

    @PullSmsSendStatusSet.setter
    def PullSmsSendStatusSet(self, PullSmsSendStatusSet):
        self._PullSmsSendStatusSet = PullSmsSendStatusSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PullSmsSendStatusSet") is not None:
            self._PullSmsSendStatusSet = []
            for item in params.get("PullSmsSendStatusSet"):
                obj = PullSmsSendStatus()
                obj._deserialize(item)
                self._PullSmsSendStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class SendSmsRequest(AbstractModel):
    """SendSms请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PhoneNumberSet: 下发手机号码，采用 E.164 标准，格式为+[国家或地区码][手机号]，单次请求最多支持200个手机号且要求全为境内手机号或全为境外手机号。
例如：+8618501234444， 其中前面有一个+号 ，86为国家码，18501234444为手机号。
        :type PhoneNumberSet: list of str
        :param _TemplateID: 模板 ID，必须填写已审核通过的模板 ID。模板ID可登录 [短信控制台](https://console.cloud.tencent.com/smsv2) 查看，若向境外手机号发送短信，仅支持使用国际/港澳台短信模板。
        :type TemplateID: str
        :param _SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2)  添加应用后生成的实际SdkAppid，示例如1400006666。
        :type SmsSdkAppid: str
        :param _Sign: 短信签名内容，使用 UTF-8 编码，必须填写已审核通过的签名，签名信息可登录 [短信控制台](https://console.cloud.tencent.com/smsv2)  查看。注：国内短信为必填参数。
        :type Sign: str
        :param _TemplateParamSet: 模板参数，若无模板参数，则设置为空。
        :type TemplateParamSet: list of str
        :param _ExtendCode: 短信码号扩展号，默认未开通，如需开通请联系 [sms helper](https://cloud.tencent.com/document/product/382/3773)。
        :type ExtendCode: str
        :param _SessionContext: 用户的 session 内容，可以携带用户侧 ID 等上下文信息，server 会原样返回。注意长度需小于512字节。
        :type SessionContext: str
        :param _SenderId: 国内短信无senderid，无需填写该项；若需开通国际/港澳台短信senderid，请联系smshelper。
        :type SenderId: str
        """
        self._PhoneNumberSet = None
        self._TemplateID = None
        self._SmsSdkAppid = None
        self._Sign = None
        self._TemplateParamSet = None
        self._ExtendCode = None
        self._SessionContext = None
        self._SenderId = None

    @property
    def PhoneNumberSet(self):
        """下发手机号码，采用 E.164 标准，格式为+[国家或地区码][手机号]，单次请求最多支持200个手机号且要求全为境内手机号或全为境外手机号。
例如：+8618501234444， 其中前面有一个+号 ，86为国家码，18501234444为手机号。
        :rtype: list of str
        """
        return self._PhoneNumberSet

    @PhoneNumberSet.setter
    def PhoneNumberSet(self, PhoneNumberSet):
        self._PhoneNumberSet = PhoneNumberSet

    @property
    def TemplateID(self):
        """模板 ID，必须填写已审核通过的模板 ID。模板ID可登录 [短信控制台](https://console.cloud.tencent.com/smsv2) 查看，若向境外手机号发送短信，仅支持使用国际/港澳台短信模板。
        :rtype: str
        """
        return self._TemplateID

    @TemplateID.setter
    def TemplateID(self, TemplateID):
        self._TemplateID = TemplateID

    @property
    def SmsSdkAppid(self):
        """短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2)  添加应用后生成的实际SdkAppid，示例如1400006666。
        :rtype: str
        """
        return self._SmsSdkAppid

    @SmsSdkAppid.setter
    def SmsSdkAppid(self, SmsSdkAppid):
        self._SmsSdkAppid = SmsSdkAppid

    @property
    def Sign(self):
        """短信签名内容，使用 UTF-8 编码，必须填写已审核通过的签名，签名信息可登录 [短信控制台](https://console.cloud.tencent.com/smsv2)  查看。注：国内短信为必填参数。
        :rtype: str
        """
        return self._Sign

    @Sign.setter
    def Sign(self, Sign):
        self._Sign = Sign

    @property
    def TemplateParamSet(self):
        """模板参数，若无模板参数，则设置为空。
        :rtype: list of str
        """
        return self._TemplateParamSet

    @TemplateParamSet.setter
    def TemplateParamSet(self, TemplateParamSet):
        self._TemplateParamSet = TemplateParamSet

    @property
    def ExtendCode(self):
        """短信码号扩展号，默认未开通，如需开通请联系 [sms helper](https://cloud.tencent.com/document/product/382/3773)。
        :rtype: str
        """
        return self._ExtendCode

    @ExtendCode.setter
    def ExtendCode(self, ExtendCode):
        self._ExtendCode = ExtendCode

    @property
    def SessionContext(self):
        """用户的 session 内容，可以携带用户侧 ID 等上下文信息，server 会原样返回。注意长度需小于512字节。
        :rtype: str
        """
        return self._SessionContext

    @SessionContext.setter
    def SessionContext(self, SessionContext):
        self._SessionContext = SessionContext

    @property
    def SenderId(self):
        """国内短信无senderid，无需填写该项；若需开通国际/港澳台短信senderid，请联系smshelper。
        :rtype: str
        """
        return self._SenderId

    @SenderId.setter
    def SenderId(self, SenderId):
        self._SenderId = SenderId


    def _deserialize(self, params):
        self._PhoneNumberSet = params.get("PhoneNumberSet")
        self._TemplateID = params.get("TemplateID")
        self._SmsSdkAppid = params.get("SmsSdkAppid")
        self._Sign = params.get("Sign")
        self._TemplateParamSet = params.get("TemplateParamSet")
        self._ExtendCode = params.get("ExtendCode")
        self._SessionContext = params.get("SessionContext")
        self._SenderId = params.get("SenderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendSmsResponse(AbstractModel):
    """SendSms返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SendStatusSet: 短信发送状态。
        :type SendStatusSet: list of SendStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SendStatusSet = None
        self._RequestId = None

    @property
    def SendStatusSet(self):
        """短信发送状态。
        :rtype: list of SendStatus
        """
        return self._SendStatusSet

    @SendStatusSet.setter
    def SendStatusSet(self, SendStatusSet):
        self._SendStatusSet = SendStatusSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SendStatusSet") is not None:
            self._SendStatusSet = []
            for item in params.get("SendStatusSet"):
                obj = SendStatus()
                obj._deserialize(item)
                self._SendStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class SendStatus(AbstractModel):
    """发送短信状态

    """

    def __init__(self):
        r"""
        :param _SerialNo: 发送流水号。
        :type SerialNo: str
        :param _PhoneNumber: 手机号码，E.164标准，+[国家或地区码][手机号] ，示例如：+8618501234444， 其中前面有一个+号 ，86为国家码，18501234444为手机号。
        :type PhoneNumber: str
        :param _Fee: 计费条数，计费规则请查询 [计费策略](https://cloud.tencent.com/document/product/382/36135)。
        :type Fee: int
        :param _SessionContext: 用户Session内容。
        :type SessionContext: str
        :param _Code: 短信请求错误码，具体含义请参考错误码。
        :type Code: str
        :param _Message: 短信请求错误码描述。
        :type Message: str
        :param _IsoCode: 国家码或地区码，例如CN,US等，对于未识别出国家码或者地区码，默认返回DEF,具体支持列表请参考国际/港澳台计费总览。
        :type IsoCode: str
        """
        self._SerialNo = None
        self._PhoneNumber = None
        self._Fee = None
        self._SessionContext = None
        self._Code = None
        self._Message = None
        self._IsoCode = None

    @property
    def SerialNo(self):
        """发送流水号。
        :rtype: str
        """
        return self._SerialNo

    @SerialNo.setter
    def SerialNo(self, SerialNo):
        self._SerialNo = SerialNo

    @property
    def PhoneNumber(self):
        """手机号码，E.164标准，+[国家或地区码][手机号] ，示例如：+8618501234444， 其中前面有一个+号 ，86为国家码，18501234444为手机号。
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Fee(self):
        """计费条数，计费规则请查询 [计费策略](https://cloud.tencent.com/document/product/382/36135)。
        :rtype: int
        """
        return self._Fee

    @Fee.setter
    def Fee(self, Fee):
        self._Fee = Fee

    @property
    def SessionContext(self):
        """用户Session内容。
        :rtype: str
        """
        return self._SessionContext

    @SessionContext.setter
    def SessionContext(self, SessionContext):
        self._SessionContext = SessionContext

    @property
    def Code(self):
        """短信请求错误码，具体含义请参考错误码。
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        """短信请求错误码描述。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def IsoCode(self):
        """国家码或地区码，例如CN,US等，对于未识别出国家码或者地区码，默认返回DEF,具体支持列表请参考国际/港澳台计费总览。
        :rtype: str
        """
        return self._IsoCode

    @IsoCode.setter
    def IsoCode(self, IsoCode):
        self._IsoCode = IsoCode


    def _deserialize(self, params):
        self._SerialNo = params.get("SerialNo")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Fee = params.get("Fee")
        self._SessionContext = params.get("SessionContext")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._IsoCode = params.get("IsoCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendStatusStatistics(AbstractModel):
    """发送数据统计响应包体

    """

    def __init__(self):
        r"""
        :param _FeeCount: 短信计费条数统计，例如提交成功量为100条，其中有20条是长短信（长度为80字）被拆分成2条，则计费条数为： ```80 * 1 + 20 * 2 = 120``` 条。
        :type FeeCount: int
        :param _RequestCount: 短信提交量统计。
        :type RequestCount: int
        :param _RequestSuccessCount: 短信提交成功量统计。
        :type RequestSuccessCount: int
        """
        self._FeeCount = None
        self._RequestCount = None
        self._RequestSuccessCount = None

    @property
    def FeeCount(self):
        """短信计费条数统计，例如提交成功量为100条，其中有20条是长短信（长度为80字）被拆分成2条，则计费条数为： ```80 * 1 + 20 * 2 = 120``` 条。
        :rtype: int
        """
        return self._FeeCount

    @FeeCount.setter
    def FeeCount(self, FeeCount):
        self._FeeCount = FeeCount

    @property
    def RequestCount(self):
        """短信提交量统计。
        :rtype: int
        """
        return self._RequestCount

    @RequestCount.setter
    def RequestCount(self, RequestCount):
        self._RequestCount = RequestCount

    @property
    def RequestSuccessCount(self):
        """短信提交成功量统计。
        :rtype: int
        """
        return self._RequestSuccessCount

    @RequestSuccessCount.setter
    def RequestSuccessCount(self, RequestSuccessCount):
        self._RequestSuccessCount = RequestSuccessCount


    def _deserialize(self, params):
        self._FeeCount = params.get("FeeCount")
        self._RequestCount = params.get("RequestCount")
        self._RequestSuccessCount = params.get("RequestSuccessCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendStatusStatisticsRequest(AbstractModel):
    """SendStatusStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartDateTime: 拉取起始时间，yyyymmddhh 需要拉取的起始时间，精确到小时。
        :type StartDateTime: int
        :param _EndDataTime: 结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时
注：EndDataTime 必须大于等于 StartDateTime。
        :type EndDataTime: int
        :param _SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，示例如1400006666。
        :type SmsSdkAppid: str
        :param _Limit: 最大上限。
注：目前固定设置为0。
        :type Limit: int
        :param _Offset: 偏移量。
注：目前固定设置为0。
        :type Offset: int
        """
        self._StartDateTime = None
        self._EndDataTime = None
        self._SmsSdkAppid = None
        self._Limit = None
        self._Offset = None

    @property
    def StartDateTime(self):
        """拉取起始时间，yyyymmddhh 需要拉取的起始时间，精确到小时。
        :rtype: int
        """
        return self._StartDateTime

    @StartDateTime.setter
    def StartDateTime(self, StartDateTime):
        self._StartDateTime = StartDateTime

    @property
    def EndDataTime(self):
        """结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时
注：EndDataTime 必须大于等于 StartDateTime。
        :rtype: int
        """
        return self._EndDataTime

    @EndDataTime.setter
    def EndDataTime(self, EndDataTime):
        self._EndDataTime = EndDataTime

    @property
    def SmsSdkAppid(self):
        """短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，示例如1400006666。
        :rtype: str
        """
        return self._SmsSdkAppid

    @SmsSdkAppid.setter
    def SmsSdkAppid(self, SmsSdkAppid):
        self._SmsSdkAppid = SmsSdkAppid

    @property
    def Limit(self):
        """最大上限。
注：目前固定设置为0。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量。
注：目前固定设置为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._StartDateTime = params.get("StartDateTime")
        self._EndDataTime = params.get("EndDataTime")
        self._SmsSdkAppid = params.get("SmsSdkAppid")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendStatusStatisticsResponse(AbstractModel):
    """SendStatusStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SendStatusStatistics: 发送数据统计响应包体。
        :type SendStatusStatistics: :class:`tencentcloud.sms.v20190711.models.SendStatusStatistics`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SendStatusStatistics = None
        self._RequestId = None

    @property
    def SendStatusStatistics(self):
        """发送数据统计响应包体。
        :rtype: :class:`tencentcloud.sms.v20190711.models.SendStatusStatistics`
        """
        return self._SendStatusStatistics

    @SendStatusStatistics.setter
    def SendStatusStatistics(self, SendStatusStatistics):
        self._SendStatusStatistics = SendStatusStatistics

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SendStatusStatistics") is not None:
            self._SendStatusStatistics = SendStatusStatistics()
            self._SendStatusStatistics._deserialize(params.get("SendStatusStatistics"))
        self._RequestId = params.get("RequestId")


class SmsPackagesStatistics(AbstractModel):
    """套餐包信息统计响应包体

    """

    def __init__(self):
        r"""
        :param _PackageCreateTime: 套餐包创建时间，标准时间，例如：2019-10-08 17:18:37。
        :type PackageCreateTime: str
        :param _PackageCreateUnixTime: 套餐包创建时间，UNIX 时间戳（单位：秒）。
        :type PackageCreateUnixTime: int
        :param _PackageEffectiveTime: 套餐包生效时间，标准时间，例如：2019-10-08 17:18:37。
        :type PackageEffectiveTime: str
        :param _PackageEffectiveUnixTime: 套餐包生效时间，UNIX 时间戳（单位：秒）。
        :type PackageEffectiveUnixTime: int
        :param _PackageExpiredTime: 套餐包过期时间，标准时间，例如：2019-10-08 17:18:37。
        :type PackageExpiredTime: str
        :param _PackageExpiredUnixTime: 套餐包过期时间，UNIX 时间戳（单位：秒）。
        :type PackageExpiredUnixTime: int
        :param _AmountOfPackage: 套餐包条数。
        :type AmountOfPackage: int
        :param _TypeOfPackage: 0表示赠送套餐包，1表示购买套餐包。
        :type TypeOfPackage: int
        :param _PackageId: 套餐包 ID。
        :type PackageId: int
        :param _CurrentUsage: 当前使用量。
        :type CurrentUsage: int
        """
        self._PackageCreateTime = None
        self._PackageCreateUnixTime = None
        self._PackageEffectiveTime = None
        self._PackageEffectiveUnixTime = None
        self._PackageExpiredTime = None
        self._PackageExpiredUnixTime = None
        self._AmountOfPackage = None
        self._TypeOfPackage = None
        self._PackageId = None
        self._CurrentUsage = None

    @property
    def PackageCreateTime(self):
        """套餐包创建时间，标准时间，例如：2019-10-08 17:18:37。
        :rtype: str
        """
        return self._PackageCreateTime

    @PackageCreateTime.setter
    def PackageCreateTime(self, PackageCreateTime):
        self._PackageCreateTime = PackageCreateTime

    @property
    def PackageCreateUnixTime(self):
        """套餐包创建时间，UNIX 时间戳（单位：秒）。
        :rtype: int
        """
        return self._PackageCreateUnixTime

    @PackageCreateUnixTime.setter
    def PackageCreateUnixTime(self, PackageCreateUnixTime):
        self._PackageCreateUnixTime = PackageCreateUnixTime

    @property
    def PackageEffectiveTime(self):
        """套餐包生效时间，标准时间，例如：2019-10-08 17:18:37。
        :rtype: str
        """
        return self._PackageEffectiveTime

    @PackageEffectiveTime.setter
    def PackageEffectiveTime(self, PackageEffectiveTime):
        self._PackageEffectiveTime = PackageEffectiveTime

    @property
    def PackageEffectiveUnixTime(self):
        """套餐包生效时间，UNIX 时间戳（单位：秒）。
        :rtype: int
        """
        return self._PackageEffectiveUnixTime

    @PackageEffectiveUnixTime.setter
    def PackageEffectiveUnixTime(self, PackageEffectiveUnixTime):
        self._PackageEffectiveUnixTime = PackageEffectiveUnixTime

    @property
    def PackageExpiredTime(self):
        """套餐包过期时间，标准时间，例如：2019-10-08 17:18:37。
        :rtype: str
        """
        return self._PackageExpiredTime

    @PackageExpiredTime.setter
    def PackageExpiredTime(self, PackageExpiredTime):
        self._PackageExpiredTime = PackageExpiredTime

    @property
    def PackageExpiredUnixTime(self):
        """套餐包过期时间，UNIX 时间戳（单位：秒）。
        :rtype: int
        """
        return self._PackageExpiredUnixTime

    @PackageExpiredUnixTime.setter
    def PackageExpiredUnixTime(self, PackageExpiredUnixTime):
        self._PackageExpiredUnixTime = PackageExpiredUnixTime

    @property
    def AmountOfPackage(self):
        """套餐包条数。
        :rtype: int
        """
        return self._AmountOfPackage

    @AmountOfPackage.setter
    def AmountOfPackage(self, AmountOfPackage):
        self._AmountOfPackage = AmountOfPackage

    @property
    def TypeOfPackage(self):
        """0表示赠送套餐包，1表示购买套餐包。
        :rtype: int
        """
        return self._TypeOfPackage

    @TypeOfPackage.setter
    def TypeOfPackage(self, TypeOfPackage):
        self._TypeOfPackage = TypeOfPackage

    @property
    def PackageId(self):
        """套餐包 ID。
        :rtype: int
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def CurrentUsage(self):
        """当前使用量。
        :rtype: int
        """
        return self._CurrentUsage

    @CurrentUsage.setter
    def CurrentUsage(self, CurrentUsage):
        self._CurrentUsage = CurrentUsage


    def _deserialize(self, params):
        self._PackageCreateTime = params.get("PackageCreateTime")
        self._PackageCreateUnixTime = params.get("PackageCreateUnixTime")
        self._PackageEffectiveTime = params.get("PackageEffectiveTime")
        self._PackageEffectiveUnixTime = params.get("PackageEffectiveUnixTime")
        self._PackageExpiredTime = params.get("PackageExpiredTime")
        self._PackageExpiredUnixTime = params.get("PackageExpiredUnixTime")
        self._AmountOfPackage = params.get("AmountOfPackage")
        self._TypeOfPackage = params.get("TypeOfPackage")
        self._PackageId = params.get("PackageId")
        self._CurrentUsage = params.get("CurrentUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsPackagesStatisticsRequest(AbstractModel):
    """SmsPackagesStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，示例如1400006666。
        :type SmsSdkAppid: str
        :param _Limit: 最大上限(需要拉取的套餐包个数)。
注：Limit默认最大值为500，可结合Offset实现分页查询。
        :type Limit: int
        :param _Offset: 偏移量。
        :type Offset: int
        """
        self._SmsSdkAppid = None
        self._Limit = None
        self._Offset = None

    @property
    def SmsSdkAppid(self):
        """短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，示例如1400006666。
        :rtype: str
        """
        return self._SmsSdkAppid

    @SmsSdkAppid.setter
    def SmsSdkAppid(self, SmsSdkAppid):
        self._SmsSdkAppid = SmsSdkAppid

    @property
    def Limit(self):
        """最大上限(需要拉取的套餐包个数)。
注：Limit默认最大值为500，可结合Offset实现分页查询。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._SmsSdkAppid = params.get("SmsSdkAppid")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsPackagesStatisticsResponse(AbstractModel):
    """SmsPackagesStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SmsPackagesStatisticsSet: 发送数据统计响应包体。
        :type SmsPackagesStatisticsSet: list of SmsPackagesStatistics
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SmsPackagesStatisticsSet = None
        self._RequestId = None

    @property
    def SmsPackagesStatisticsSet(self):
        """发送数据统计响应包体。
        :rtype: list of SmsPackagesStatistics
        """
        return self._SmsPackagesStatisticsSet

    @SmsPackagesStatisticsSet.setter
    def SmsPackagesStatisticsSet(self, SmsPackagesStatisticsSet):
        self._SmsPackagesStatisticsSet = SmsPackagesStatisticsSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SmsPackagesStatisticsSet") is not None:
            self._SmsPackagesStatisticsSet = []
            for item in params.get("SmsPackagesStatisticsSet"):
                obj = SmsPackagesStatistics()
                obj._deserialize(item)
                self._SmsPackagesStatisticsSet.append(obj)
        self._RequestId = params.get("RequestId")