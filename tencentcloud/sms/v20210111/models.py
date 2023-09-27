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
        :param _SignId: 签名ID。
        :type SignId: int
        """
        self._SignId = None

    @property
    def SignId(self):
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
2：网站，可选 DocumentType 有（0，1，2，3，5）。
3：公众号，可选 DocumentType 有（0，1，2，3，8）。
4：商标，可选 DocumentType 有（7）。
5：政府/机关事业单位/其他机构，可选 DocumentType 有（2，3）。
6：小程序，可选 DocumentType 有（0，1，2，3，6）。
注：必须按照对应关系选择证明类型，否则会审核失败。
        :type SignType: int
        :param _DocumentType: 证明类型：
0：三证合一。
1：企业营业执照。
2：组织机构代码证书。
3：社会信用代码证书。
4：应用后台管理截图（个人开发APP）。
5：网站备案后台截图（个人开发网站）。
6：小程序设置页面截图（个人认证小程序）。
7：商标注册书。
8：公众号设置页面截图（个人认证公众号）。
        :type DocumentType: int
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param _SignPurpose: 签名用途：
0：自用。
1：他用。
        :type SignPurpose: int
        :param _ProofImage: 签名对应的资质证明图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。
        :type ProofImage: str
        :param _CommissionImage: 委托授权证明。选择 SignPurpose 为他用之后需要提交委托的授权证明。
图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。
注：只有 SignPurpose 在选择为 1（他用）时，这个字段才会生效。
        :type CommissionImage: str
        :param _Remark: 签名的申请备注。
        :type Remark: str
        """
        self._SignName = None
        self._SignType = None
        self._DocumentType = None
        self._International = None
        self._SignPurpose = None
        self._ProofImage = None
        self._CommissionImage = None
        self._Remark = None

    @property
    def SignName(self):
        return self._SignName

    @SignName.setter
    def SignName(self, SignName):
        self._SignName = SignName

    @property
    def SignType(self):
        return self._SignType

    @SignType.setter
    def SignType(self, SignType):
        self._SignType = SignType

    @property
    def DocumentType(self):
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def SignPurpose(self):
        return self._SignPurpose

    @SignPurpose.setter
    def SignPurpose(self, SignPurpose):
        self._SignPurpose = SignPurpose

    @property
    def ProofImage(self):
        return self._ProofImage

    @ProofImage.setter
    def ProofImage(self, ProofImage):
        self._ProofImage = ProofImage

    @property
    def CommissionImage(self):
        return self._CommissionImage

    @CommissionImage.setter
    def CommissionImage(self, CommissionImage):
        self._CommissionImage = CommissionImage

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._SignName = params.get("SignName")
        self._SignType = params.get("SignType")
        self._DocumentType = params.get("DocumentType")
        self._International = params.get("International")
        self._SignPurpose = params.get("SignPurpose")
        self._ProofImage = params.get("ProofImage")
        self._CommissionImage = params.get("CommissionImage")
        self._Remark = params.get("Remark")
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
        :type AddSignStatus: :class:`tencentcloud.sms.v20210111.models.AddSignStatus`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AddSignStatus = None
        self._RequestId = None

    @property
    def AddSignStatus(self):
        return self._AddSignStatus

    @AddSignStatus.setter
    def AddSignStatus(self, AddSignStatus):
        self._AddSignStatus = AddSignStatus

    @property
    def RequestId(self):
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
        :param _SmsType: 短信类型，0表示普通短信, 1表示营销短信。
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
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateContent(self):
        return self._TemplateContent

    @TemplateContent.setter
    def TemplateContent(self, TemplateContent):
        self._TemplateContent = TemplateContent

    @property
    def SmsType(self):
        return self._SmsType

    @SmsType.setter
    def SmsType(self, SmsType):
        self._SmsType = SmsType

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def Remark(self):
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
        :type AddTemplateStatus: :class:`tencentcloud.sms.v20210111.models.AddTemplateStatus`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AddTemplateStatus = None
        self._RequestId = None

    @property
    def AddTemplateStatus(self):
        return self._AddTemplateStatus

    @AddTemplateStatus.setter
    def AddTemplateStatus(self, AddTemplateStatus):
        self._AddTemplateStatus = AddTemplateStatus

    @property
    def RequestId(self):
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
        :param _TemplateId: 模板ID。
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
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
        return self._CallbackCount

    @CallbackCount.setter
    def CallbackCount(self, CallbackCount):
        self._CallbackCount = CallbackCount

    @property
    def RequestSuccessCount(self):
        return self._RequestSuccessCount

    @RequestSuccessCount.setter
    def RequestSuccessCount(self, RequestSuccessCount):
        self._RequestSuccessCount = RequestSuccessCount

    @property
    def CallbackFailCount(self):
        return self._CallbackFailCount

    @CallbackFailCount.setter
    def CallbackFailCount(self, CallbackFailCount):
        self._CallbackFailCount = CallbackFailCount

    @property
    def CallbackSuccessCount(self):
        return self._CallbackSuccessCount

    @CallbackSuccessCount.setter
    def CallbackSuccessCount(self, CallbackSuccessCount):
        self._CallbackSuccessCount = CallbackSuccessCount

    @property
    def InternalErrorCount(self):
        return self._InternalErrorCount

    @InternalErrorCount.setter
    def InternalErrorCount(self, InternalErrorCount):
        self._InternalErrorCount = InternalErrorCount

    @property
    def InvalidNumberCount(self):
        return self._InvalidNumberCount

    @InvalidNumberCount.setter
    def InvalidNumberCount(self, InvalidNumberCount):
        self._InvalidNumberCount = InvalidNumberCount

    @property
    def ShutdownErrorCount(self):
        return self._ShutdownErrorCount

    @ShutdownErrorCount.setter
    def ShutdownErrorCount(self, ShutdownErrorCount):
        self._ShutdownErrorCount = ShutdownErrorCount

    @property
    def BlackListCount(self):
        return self._BlackListCount

    @BlackListCount.setter
    def BlackListCount(self, BlackListCount):
        self._BlackListCount = BlackListCount

    @property
    def FrequencyLimitCount(self):
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
        :param _BeginTime: 起始时间，格式为yyyymmddhh，精确到小时，例如2021050113，表示2021年5月1号13时。
        :type BeginTime: str
        :param _EndTime: 结束时间，格式为yyyymmddhh，精确到小时，例如2021050118，表示2021年5月1号18时。
注：EndTime 必须大于 BeginTime，且相差不超过32天。
        :type EndTime: str
        :param _SmsSdkAppId: 短信 SdkAppId 在 [短信控制台](https://console.cloud.tencent.com/smsv2/app-manage)  添加应用后生成的实际 SdkAppId，示例如1400006666。
        :type SmsSdkAppId: str
        :param _Limit: 最大上限。
注：目前固定设置为0。
        :type Limit: int
        :param _Offset: 偏移量。
注：目前固定设置为0。
        :type Offset: int
        """
        self._BeginTime = None
        self._EndTime = None
        self._SmsSdkAppId = None
        self._Limit = None
        self._Offset = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SmsSdkAppId(self):
        return self._SmsSdkAppId

    @SmsSdkAppId.setter
    def SmsSdkAppId(self, SmsSdkAppId):
        self._SmsSdkAppId = SmsSdkAppId

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
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._SmsSdkAppId = params.get("SmsSdkAppId")
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
        :type CallbackStatusStatistics: :class:`tencentcloud.sms.v20210111.models.CallbackStatusStatistics`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CallbackStatusStatistics = None
        self._RequestId = None

    @property
    def CallbackStatusStatistics(self):
        return self._CallbackStatusStatistics

    @CallbackStatusStatistics.setter
    def CallbackStatusStatistics(self, CallbackStatusStatistics):
        self._CallbackStatusStatistics = CallbackStatusStatistics

    @property
    def RequestId(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteStatus: str
        :param _DeleteTime: 删除时间，UNIX 时间戳（单位：秒）。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteTime: int
        """
        self._DeleteStatus = None
        self._DeleteTime = None

    @property
    def DeleteStatus(self):
        return self._DeleteStatus

    @DeleteStatus.setter
    def DeleteStatus(self, DeleteStatus):
        self._DeleteStatus = DeleteStatus

    @property
    def DeleteTime(self):
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
        :type DeleteSignStatus: :class:`tencentcloud.sms.v20210111.models.DeleteSignStatus`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeleteSignStatus = None
        self._RequestId = None

    @property
    def DeleteSignStatus(self):
        return self._DeleteSignStatus

    @DeleteSignStatus.setter
    def DeleteSignStatus(self, DeleteSignStatus):
        self._DeleteSignStatus = DeleteSignStatus

    @property
    def RequestId(self):
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
        :type DeleteTemplateStatus: :class:`tencentcloud.sms.v20210111.models.DeleteTemplateStatus`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeleteTemplateStatus = None
        self._RequestId = None

    @property
    def DeleteTemplateStatus(self):
        return self._DeleteTemplateStatus

    @DeleteTemplateStatus.setter
    def DeleteTemplateStatus(self, DeleteTemplateStatus):
        self._DeleteTemplateStatus = DeleteTemplateStatus

    @property
    def RequestId(self):
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
        return self._DeleteStatus

    @DeleteStatus.setter
    def DeleteStatus(self, DeleteStatus):
        self._DeleteStatus = DeleteStatus

    @property
    def DeleteTime(self):
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
        


class DescribePhoneNumberInfoRequest(AbstractModel):
    """DescribePhoneNumberInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PhoneNumberSet: 查询手机号码，采用 E.164 标准，格式为+[国家或地区码][手机号]，单次请求最多支持200个手机号。
例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :type PhoneNumberSet: list of str
        """
        self._PhoneNumberSet = None

    @property
    def PhoneNumberSet(self):
        return self._PhoneNumberSet

    @PhoneNumberSet.setter
    def PhoneNumberSet(self, PhoneNumberSet):
        self._PhoneNumberSet = PhoneNumberSet


    def _deserialize(self, params):
        self._PhoneNumberSet = params.get("PhoneNumberSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePhoneNumberInfoResponse(AbstractModel):
    """DescribePhoneNumberInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PhoneNumberInfoSet: 获取号码信息。
        :type PhoneNumberInfoSet: list of PhoneNumberInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PhoneNumberInfoSet = None
        self._RequestId = None

    @property
    def PhoneNumberInfoSet(self):
        return self._PhoneNumberInfoSet

    @PhoneNumberInfoSet.setter
    def PhoneNumberInfoSet(self, PhoneNumberInfoSet):
        self._PhoneNumberInfoSet = PhoneNumberInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PhoneNumberInfoSet") is not None:
            self._PhoneNumberInfoSet = []
            for item in params.get("PhoneNumberInfoSet"):
                obj = PhoneNumberInfo()
                obj._deserialize(item)
                self._PhoneNumberInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSignListStatus(AbstractModel):
    """获取短信签名信息响应

    """

    def __init__(self):
        r"""
        :param _SignId: 签名ID。
        :type SignId: int
        :param _International: 是否国际/港澳台短信，其中0表示国内短信，1表示国际/港澳台短信。
        :type International: int
        :param _StatusCode: 申请签名状态，其中0表示审核通过，1表示审核中。
-1：表示审核未通过或审核失败。
        :type StatusCode: int
        :param _ReviewReply: 审核回复，审核人员审核后给出的回复，通常是审核未通过的原因。
        :type ReviewReply: str
        :param _SignName: 签名名称。
        :type SignName: str
        :param _CreateTime: 提交审核时间，UNIX 时间戳（单位：秒）。
        :type CreateTime: int
        """
        self._SignId = None
        self._International = None
        self._StatusCode = None
        self._ReviewReply = None
        self._SignName = None
        self._CreateTime = None

    @property
    def SignId(self):
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def ReviewReply(self):
        return self._ReviewReply

    @ReviewReply.setter
    def ReviewReply(self, ReviewReply):
        self._ReviewReply = ReviewReply

    @property
    def SignName(self):
        return self._SignName

    @SignName.setter
    def SignName(self, SignName):
        self._SignName = SignName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        self._International = params.get("International")
        self._StatusCode = params.get("StatusCode")
        self._ReviewReply = params.get("ReviewReply")
        self._SignName = params.get("SignName")
        self._CreateTime = params.get("CreateTime")
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
注：默认数组最大长度100。
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
        return self._SignIdSet

    @SignIdSet.setter
    def SignIdSet(self, SignIdSet):
        self._SignIdSet = SignIdSet

    @property
    def International(self):
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DescribeSignListStatusSet = None
        self._RequestId = None

    @property
    def DescribeSignListStatusSet(self):
        return self._DescribeSignListStatusSet

    @DescribeSignListStatusSet.setter
    def DescribeSignListStatusSet(self, DescribeSignListStatusSet):
        self._DescribeSignListStatusSet = DescribeSignListStatusSet

    @property
    def RequestId(self):
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
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param _TemplateIdSet: 模板 ID 数组。数组为空时默认查询模板列表信息，请使用 Limit 和 Offset 字段设置查询范围。
<dx-alert infotype="notice" title="注意">默认数组长度最大100</dx-alert>
        :type TemplateIdSet: list of int non-negative
        :param _Limit: 最大上限，最多100。
注：默认为0，TemplateIdSet 为空时启用。
        :type Limit: int
        :param _Offset: 偏移量。
注：默认为0，TemplateIdSet 为空时启用。
        :type Offset: int
        """
        self._International = None
        self._TemplateIdSet = None
        self._Limit = None
        self._Offset = None

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def TemplateIdSet(self):
        return self._TemplateIdSet

    @TemplateIdSet.setter
    def TemplateIdSet(self, TemplateIdSet):
        self._TemplateIdSet = TemplateIdSet

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
        self._International = params.get("International")
        self._TemplateIdSet = params.get("TemplateIdSet")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DescribeTemplateStatusSet = None
        self._RequestId = None

    @property
    def DescribeTemplateStatusSet(self):
        return self._DescribeTemplateStatusSet

    @DescribeTemplateStatusSet.setter
    def DescribeTemplateStatusSet(self, DescribeTemplateStatusSet):
        self._DescribeTemplateStatusSet = DescribeTemplateStatusSet

    @property
    def RequestId(self):
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
        :param _TemplateId: 模板ID。
        :type TemplateId: int
        :param _International: 是否国际/港澳台短信，其中0表示国内短信，1表示国际/港澳台短信，3表示该模板既支持国内短信也支持国际/港澳台短信。
        :type International: int
        :param _StatusCode: 申请模板状态，其中0表示审核通过且已生效，1表示审核中，2表示审核通过待生效，-1表示审核未通过或审核失败。注：只有状态值为0时该模板才能使用。
        :type StatusCode: int
        :param _ReviewReply: 审核回复，审核人员审核后给出的回复，通常是审核未通过的原因。
        :type ReviewReply: str
        :param _TemplateName: 模板名称。
        :type TemplateName: str
        :param _CreateTime: 提交审核时间，UNIX 时间戳（单位：秒）。
        :type CreateTime: int
        :param _TemplateContent: 模板内容。
        :type TemplateContent: str
        """
        self._TemplateId = None
        self._International = None
        self._StatusCode = None
        self._ReviewReply = None
        self._TemplateName = None
        self._CreateTime = None
        self._TemplateContent = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def ReviewReply(self):
        return self._ReviewReply

    @ReviewReply.setter
    def ReviewReply(self, ReviewReply):
        self._ReviewReply = ReviewReply

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TemplateContent(self):
        return self._TemplateContent

    @TemplateContent.setter
    def TemplateContent(self, TemplateContent):
        self._TemplateContent = TemplateContent


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._International = params.get("International")
        self._StatusCode = params.get("StatusCode")
        self._ReviewReply = params.get("ReviewReply")
        self._TemplateName = params.get("TemplateName")
        self._CreateTime = params.get("CreateTime")
        self._TemplateContent = params.get("TemplateContent")
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
        :param _SignId: 签名ID。
        :type SignId: int
        """
        self._SignId = None

    @property
    def SignId(self):
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
2：网站，可选 DocumentType 有（0，1，2，3，5）。
3：公众号，可选 DocumentType 有（0，1，2，3，8）。
4：商标，可选 DocumentType 有（7）。
5：政府/机关事业单位/其他机构，可选 DocumentType 有（2，3）。
6：小程序，可选 DocumentType 有（0，1，2，3，6）。
注：必须按照对应关系选择证明类型，否则会审核失败。
        :type SignType: int
        :param _DocumentType: 证明类型：
0：三证合一。
1：企业营业执照。
2：组织机构代码证书。
3：社会信用代码证书。
4：应用后台管理截图（个人开发APP）。
5：网站备案后台截图（个人开发网站）。
6：小程序设置页面截图（个人认证小程序）。
7：商标注册书。
8：公众号设置页面截图（个人认证公众号）。
        :type DocumentType: int
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
注：需要和待修改签名International值保持一致，该参数不能直接修改国内签名到国际签名。
        :type International: int
        :param _SignPurpose: 签名用途：
0：自用。
1：他用。
        :type SignPurpose: int
        :param _ProofImage: 签名对应的资质证明图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。
        :type ProofImage: str
        :param _CommissionImage: 委托授权证明。选择 SignPurpose 为他用之后需要提交委托的授权证明。
图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。
注：只有 SignPurpose 在选择为 1（他用）时，这个字段才会生效。
        :type CommissionImage: str
        :param _Remark: 签名的申请备注。
        :type Remark: str
        """
        self._SignId = None
        self._SignName = None
        self._SignType = None
        self._DocumentType = None
        self._International = None
        self._SignPurpose = None
        self._ProofImage = None
        self._CommissionImage = None
        self._Remark = None

    @property
    def SignId(self):
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def SignName(self):
        return self._SignName

    @SignName.setter
    def SignName(self, SignName):
        self._SignName = SignName

    @property
    def SignType(self):
        return self._SignType

    @SignType.setter
    def SignType(self, SignType):
        self._SignType = SignType

    @property
    def DocumentType(self):
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def SignPurpose(self):
        return self._SignPurpose

    @SignPurpose.setter
    def SignPurpose(self, SignPurpose):
        self._SignPurpose = SignPurpose

    @property
    def ProofImage(self):
        return self._ProofImage

    @ProofImage.setter
    def ProofImage(self, ProofImage):
        self._ProofImage = ProofImage

    @property
    def CommissionImage(self):
        return self._CommissionImage

    @CommissionImage.setter
    def CommissionImage(self, CommissionImage):
        self._CommissionImage = CommissionImage

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        self._SignName = params.get("SignName")
        self._SignType = params.get("SignType")
        self._DocumentType = params.get("DocumentType")
        self._International = params.get("International")
        self._SignPurpose = params.get("SignPurpose")
        self._ProofImage = params.get("ProofImage")
        self._CommissionImage = params.get("CommissionImage")
        self._Remark = params.get("Remark")
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
        :type ModifySignStatus: :class:`tencentcloud.sms.v20210111.models.ModifySignStatus`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModifySignStatus = None
        self._RequestId = None

    @property
    def ModifySignStatus(self):
        return self._ModifySignStatus

    @ModifySignStatus.setter
    def ModifySignStatus(self, ModifySignStatus):
        self._ModifySignStatus = ModifySignStatus

    @property
    def RequestId(self):
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
        :param _TemplateId: 待修改模板的ID。
        :type TemplateId: int
        :param _TemplateName: 新的模板名称。
        :type TemplateName: str
        :param _TemplateContent: 新的模板内容。
        :type TemplateContent: str
        :param _SmsType: 短信类型，0表示普通短信, 1表示营销短信。
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
    def TemplateContent(self):
        return self._TemplateContent

    @TemplateContent.setter
    def TemplateContent(self, TemplateContent):
        self._TemplateContent = TemplateContent

    @property
    def SmsType(self):
        return self._SmsType

    @SmsType.setter
    def SmsType(self, SmsType):
        self._SmsType = SmsType

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def Remark(self):
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
        :type ModifyTemplateStatus: :class:`tencentcloud.sms.v20210111.models.ModifyTemplateStatus`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModifyTemplateStatus = None
        self._RequestId = None

    @property
    def ModifyTemplateStatus(self):
        return self._ModifyTemplateStatus

    @ModifyTemplateStatus.setter
    def ModifyTemplateStatus(self, ModifyTemplateStatus):
        self._ModifyTemplateStatus = ModifyTemplateStatus

    @property
    def RequestId(self):
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
        :param _TemplateId: 模板ID。
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
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
        


class PhoneNumberInfo(AbstractModel):
    """号码信息。

    """

    def __init__(self):
        r"""
        :param _Code: 号码信息查询错误码，查询成功返回 "Ok"。
        :type Code: str
        :param _Message: 号码信息查询错误码描述。
        :type Message: str
        :param _NationCode: 国家（或地区）码。
        :type NationCode: str
        :param _SubscriberNumber: 用户号码，去除国家或地区码前缀的普通格式，示例如：13711112222。
        :type SubscriberNumber: str
        :param _PhoneNumber: 解析后的规范的 E.164 号码，与下发短信的号码解析结果一致。解析失败时会原样返回。
        :type PhoneNumber: str
        :param _IsoCode: 国家码或地区码，例如 CN、US 等，对于未识别出国家码或者地区码，默认返回 DEF。
        :type IsoCode: str
        :param _IsoName: 国家码或地区名，例如 China，可参考 [国际/港澳台短信价格总览](https://cloud.tencent.com/document/product/382/18051#.E6.97.A5.E7.BB.93.E5.90.8E.E4.BB.98.E8.B4.B9.3Ca-id.3D.22post-payment.22.3E.3C.2Fa.3E)
        :type IsoName: str
        """
        self._Code = None
        self._Message = None
        self._NationCode = None
        self._SubscriberNumber = None
        self._PhoneNumber = None
        self._IsoCode = None
        self._IsoName = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def NationCode(self):
        return self._NationCode

    @NationCode.setter
    def NationCode(self, NationCode):
        self._NationCode = NationCode

    @property
    def SubscriberNumber(self):
        return self._SubscriberNumber

    @SubscriberNumber.setter
    def SubscriberNumber(self, SubscriberNumber):
        self._SubscriberNumber = SubscriberNumber

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def IsoCode(self):
        return self._IsoCode

    @IsoCode.setter
    def IsoCode(self, IsoCode):
        self._IsoCode = IsoCode

    @property
    def IsoName(self):
        return self._IsoName

    @IsoName.setter
    def IsoName(self, IsoName):
        self._IsoName = IsoName


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._NationCode = params.get("NationCode")
        self._SubscriberNumber = params.get("SubscriberNumber")
        self._PhoneNumber = params.get("PhoneNumber")
        self._IsoCode = params.get("IsoCode")
        self._IsoName = params.get("IsoName")
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
        :param _ExtendCode: 短信码号扩展号，默认未开通，如需开通请联系 [sms helper](https://cloud.tencent.com/document/product/382/3773#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81)。
        :type ExtendCode: str
        :param _CountryCode: 国家（或地区）码。
        :type CountryCode: str
        :param _PhoneNumber: 手机号码，E.164标准，+[国家或地区码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :type PhoneNumber: str
        :param _SignName: 短信签名名称。
        :type SignName: str
        :param _ReplyContent: 用户回复的内容。
        :type ReplyContent: str
        :param _ReplyTime: 回复时间，UNIX 时间戳（单位：秒）。
        :type ReplyTime: int
        :param _SubscriberNumber: 用户号码，普通格式，示例如：13711112222。
        :type SubscriberNumber: str
        """
        self._ExtendCode = None
        self._CountryCode = None
        self._PhoneNumber = None
        self._SignName = None
        self._ReplyContent = None
        self._ReplyTime = None
        self._SubscriberNumber = None

    @property
    def ExtendCode(self):
        return self._ExtendCode

    @ExtendCode.setter
    def ExtendCode(self, ExtendCode):
        self._ExtendCode = ExtendCode

    @property
    def CountryCode(self):
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def SignName(self):
        return self._SignName

    @SignName.setter
    def SignName(self, SignName):
        self._SignName = SignName

    @property
    def ReplyContent(self):
        return self._ReplyContent

    @ReplyContent.setter
    def ReplyContent(self, ReplyContent):
        self._ReplyContent = ReplyContent

    @property
    def ReplyTime(self):
        return self._ReplyTime

    @ReplyTime.setter
    def ReplyTime(self, ReplyTime):
        self._ReplyTime = ReplyTime

    @property
    def SubscriberNumber(self):
        return self._SubscriberNumber

    @SubscriberNumber.setter
    def SubscriberNumber(self, SubscriberNumber):
        self._SubscriberNumber = SubscriberNumber


    def _deserialize(self, params):
        self._ExtendCode = params.get("ExtendCode")
        self._CountryCode = params.get("CountryCode")
        self._PhoneNumber = params.get("PhoneNumber")
        self._SignName = params.get("SignName")
        self._ReplyContent = params.get("ReplyContent")
        self._ReplyTime = params.get("ReplyTime")
        self._SubscriberNumber = params.get("SubscriberNumber")
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
        :param _BeginTime: 拉取起始时间，UNIX 时间戳（时间：秒）。
注：最大可拉取当前时期前7天的数据。
        :type BeginTime: int
        :param _Offset: 偏移量。
注：目前固定设置为0。
        :type Offset: int
        :param _Limit: 拉取最大条数，最多 100。
        :type Limit: int
        :param _PhoneNumber: 下发目的手机号码，依据 E.164 标准为：+[国家（或地区）码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :type PhoneNumber: str
        :param _SmsSdkAppId: 短信 SdkAppId 在 [短信控制台](https://console.cloud.tencent.com/smsv2/app-manage)  添加应用后生成的实际 SdkAppId，示例如1400006666。
        :type SmsSdkAppId: str
        :param _EndTime: 拉取截止时间，UNIX 时间戳（时间：秒）。
        :type EndTime: int
        """
        self._BeginTime = None
        self._Offset = None
        self._Limit = None
        self._PhoneNumber = None
        self._SmsSdkAppId = None
        self._EndTime = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

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
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def SmsSdkAppId(self):
        return self._SmsSdkAppId

    @SmsSdkAppId.setter
    def SmsSdkAppId(self, SmsSdkAppId):
        self._SmsSdkAppId = SmsSdkAppId

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PhoneNumber = params.get("PhoneNumber")
        self._SmsSdkAppId = params.get("SmsSdkAppId")
        self._EndTime = params.get("EndTime")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PullSmsReplyStatusSet = None
        self._RequestId = None

    @property
    def PullSmsReplyStatusSet(self):
        return self._PullSmsReplyStatusSet

    @PullSmsReplyStatusSet.setter
    def PullSmsReplyStatusSet(self, PullSmsReplyStatusSet):
        self._PullSmsReplyStatusSet = PullSmsReplyStatusSet

    @property
    def RequestId(self):
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
        :param _SmsSdkAppId: 短信 SdkAppId 在 [短信控制台](https://console.cloud.tencent.com/smsv2/app-manage) 添加应用后生成的实际 SdkAppId，例如1400006666。
        :type SmsSdkAppId: str
        """
        self._Limit = None
        self._SmsSdkAppId = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SmsSdkAppId(self):
        return self._SmsSdkAppId

    @SmsSdkAppId.setter
    def SmsSdkAppId(self, SmsSdkAppId):
        self._SmsSdkAppId = SmsSdkAppId


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._SmsSdkAppId = params.get("SmsSdkAppId")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PullSmsReplyStatusSet = None
        self._RequestId = None

    @property
    def PullSmsReplyStatusSet(self):
        return self._PullSmsReplyStatusSet

    @PullSmsReplyStatusSet.setter
    def PullSmsReplyStatusSet(self, PullSmsReplyStatusSet):
        self._PullSmsReplyStatusSet = PullSmsReplyStatusSet

    @property
    def RequestId(self):
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
        :param _UserReceiveTime: 用户实际接收到短信的时间，UNIX 时间戳（单位：秒）。
        :type UserReceiveTime: int
        :param _CountryCode: 国家（或地区）码。
        :type CountryCode: str
        :param _SubscriberNumber: 用户号码，普通格式，示例如：13711112222。
        :type SubscriberNumber: str
        :param _PhoneNumber: 手机号码，E.164标准，+[国家或地区码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :type PhoneNumber: str
        :param _SerialNo: 本次发送标识 ID。
        :type SerialNo: str
        :param _ReportStatus: 实际是否收到短信接收状态，SUCCESS（成功）、FAIL（失败）。
        :type ReportStatus: str
        :param _Description: 用户接收短信状态描述。
        :type Description: str
        :param _SessionContext: 用户的 session 内容。与请求中的 SessionContext 一致，默认为空，如需开通请联系 [腾讯云短信小助手](https://cloud.tencent.com/document/product/382/3773#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81)。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionContext: str
        """
        self._UserReceiveTime = None
        self._CountryCode = None
        self._SubscriberNumber = None
        self._PhoneNumber = None
        self._SerialNo = None
        self._ReportStatus = None
        self._Description = None
        self._SessionContext = None

    @property
    def UserReceiveTime(self):
        return self._UserReceiveTime

    @UserReceiveTime.setter
    def UserReceiveTime(self, UserReceiveTime):
        self._UserReceiveTime = UserReceiveTime

    @property
    def CountryCode(self):
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def SubscriberNumber(self):
        return self._SubscriberNumber

    @SubscriberNumber.setter
    def SubscriberNumber(self, SubscriberNumber):
        self._SubscriberNumber = SubscriberNumber

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def SerialNo(self):
        return self._SerialNo

    @SerialNo.setter
    def SerialNo(self, SerialNo):
        self._SerialNo = SerialNo

    @property
    def ReportStatus(self):
        return self._ReportStatus

    @ReportStatus.setter
    def ReportStatus(self, ReportStatus):
        self._ReportStatus = ReportStatus

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SessionContext(self):
        return self._SessionContext

    @SessionContext.setter
    def SessionContext(self, SessionContext):
        self._SessionContext = SessionContext


    def _deserialize(self, params):
        self._UserReceiveTime = params.get("UserReceiveTime")
        self._CountryCode = params.get("CountryCode")
        self._SubscriberNumber = params.get("SubscriberNumber")
        self._PhoneNumber = params.get("PhoneNumber")
        self._SerialNo = params.get("SerialNo")
        self._ReportStatus = params.get("ReportStatus")
        self._Description = params.get("Description")
        self._SessionContext = params.get("SessionContext")
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
        :param _BeginTime: 拉取起始时间，UNIX 时间戳（时间：秒）。
注：最大可拉取当前时期前7天的数据。
        :type BeginTime: int
        :param _Offset: 偏移量。
注：目前固定设置为0。
        :type Offset: int
        :param _Limit: 拉取最大条数，最多 100。
        :type Limit: int
        :param _PhoneNumber: 下发目的手机号码，依据 E.164 标准为：+[国家（或地区）码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :type PhoneNumber: str
        :param _SmsSdkAppId: 短信 SdkAppId 在 [短信控制台](https://console.cloud.tencent.com/smsv2/app-manage)  添加应用后生成的实际 SdkAppId，示例如1400006666。
        :type SmsSdkAppId: str
        :param _EndTime: 拉取截止时间，UNIX 时间戳（时间：秒）。
        :type EndTime: int
        """
        self._BeginTime = None
        self._Offset = None
        self._Limit = None
        self._PhoneNumber = None
        self._SmsSdkAppId = None
        self._EndTime = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

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
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def SmsSdkAppId(self):
        return self._SmsSdkAppId

    @SmsSdkAppId.setter
    def SmsSdkAppId(self, SmsSdkAppId):
        self._SmsSdkAppId = SmsSdkAppId

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PhoneNumber = params.get("PhoneNumber")
        self._SmsSdkAppId = params.get("SmsSdkAppId")
        self._EndTime = params.get("EndTime")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PullSmsSendStatusSet = None
        self._RequestId = None

    @property
    def PullSmsSendStatusSet(self):
        return self._PullSmsSendStatusSet

    @PullSmsSendStatusSet.setter
    def PullSmsSendStatusSet(self, PullSmsSendStatusSet):
        self._PullSmsSendStatusSet = PullSmsSendStatusSet

    @property
    def RequestId(self):
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
        :param _SmsSdkAppId: 短信 SdkAppId 在 [短信控制台](https://console.cloud.tencent.com/smsv2/app-manage) 添加应用后生成的实际 SdkAppId，例如1400006666。
        :type SmsSdkAppId: str
        """
        self._Limit = None
        self._SmsSdkAppId = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SmsSdkAppId(self):
        return self._SmsSdkAppId

    @SmsSdkAppId.setter
    def SmsSdkAppId(self, SmsSdkAppId):
        self._SmsSdkAppId = SmsSdkAppId


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._SmsSdkAppId = params.get("SmsSdkAppId")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PullSmsSendStatusSet = None
        self._RequestId = None

    @property
    def PullSmsSendStatusSet(self):
        return self._PullSmsSendStatusSet

    @PullSmsSendStatusSet.setter
    def PullSmsSendStatusSet(self, PullSmsSendStatusSet):
        self._PullSmsSendStatusSet = PullSmsSendStatusSet

    @property
    def RequestId(self):
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


class ReportConversionRequest(AbstractModel):
    """ReportConversion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SmsSdkAppId: 短信应用ID。在 [短信控制台](https://console.cloud.tencent.com/smsv2/app-manage)  添加应用后生成的实际 SdkAppId，示例如1400006666。
        :type SmsSdkAppId: str
        :param _SerialNo: 发送短信返回的流水号。
        :type SerialNo: str
        :param _ConversionTime: 用户回填时间，UNIX 时间戳（单位：秒）。
        :type ConversionTime: int
        """
        self._SmsSdkAppId = None
        self._SerialNo = None
        self._ConversionTime = None

    @property
    def SmsSdkAppId(self):
        return self._SmsSdkAppId

    @SmsSdkAppId.setter
    def SmsSdkAppId(self, SmsSdkAppId):
        self._SmsSdkAppId = SmsSdkAppId

    @property
    def SerialNo(self):
        return self._SerialNo

    @SerialNo.setter
    def SerialNo(self, SerialNo):
        self._SerialNo = SerialNo

    @property
    def ConversionTime(self):
        return self._ConversionTime

    @ConversionTime.setter
    def ConversionTime(self, ConversionTime):
        self._ConversionTime = ConversionTime


    def _deserialize(self, params):
        self._SmsSdkAppId = params.get("SmsSdkAppId")
        self._SerialNo = params.get("SerialNo")
        self._ConversionTime = params.get("ConversionTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportConversionResponse(AbstractModel):
    """ReportConversion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportConversionStatus: 转化率上报响应包体。
        :type ReportConversionStatus: :class:`tencentcloud.sms.v20210111.models.ReportConversionStatus`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReportConversionStatus = None
        self._RequestId = None

    @property
    def ReportConversionStatus(self):
        return self._ReportConversionStatus

    @ReportConversionStatus.setter
    def ReportConversionStatus(self, ReportConversionStatus):
        self._ReportConversionStatus = ReportConversionStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ReportConversionStatus") is not None:
            self._ReportConversionStatus = ReportConversionStatus()
            self._ReportConversionStatus._deserialize(params.get("ReportConversionStatus"))
        self._RequestId = params.get("RequestId")


class ReportConversionStatus(AbstractModel):
    """转化率上报响应。

    """

    def __init__(self):
        r"""
        :param _Code: 错误码。上报成功返回 ok。
        :type Code: str
        :param _Message: 错误码描述。
        :type Message: str
        """
        self._Code = None
        self._Message = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendSmsRequest(AbstractModel):
    """SendSms请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PhoneNumberSet: 下发手机号码，采用 E.164 标准，格式为+[国家或地区码][手机号]，单次请求最多支持200个手机号且要求全为境内手机号或全为境外手机号。
例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
注：发送国内短信格式还支持0086、86或无任何国家或地区码的11位手机号码，前缀默认为+86。
        :type PhoneNumberSet: list of str
        :param _SmsSdkAppId: 短信 SdkAppId，在 [短信控制台](https://console.cloud.tencent.com/smsv2/app-manage)  添加应用后生成的实际 SdkAppId，示例如1400006666。
        :type SmsSdkAppId: str
        :param _TemplateId: 模板 ID，必须填写已审核通过的模板 ID。模板 ID 可前往 [国内短信](https://console.cloud.tencent.com/smsv2/csms-template) 或 [国际/港澳台短信](https://console.cloud.tencent.com/smsv2/isms-template) 的正文模板管理查看，若向境外手机号发送短信，仅支持使用国际/港澳台短信模板。
        :type TemplateId: str
        :param _SignName: 短信签名内容，使用 UTF-8 编码，必须填写已审核通过的签名，例如：腾讯云，签名信息可前往 [国内短信](https://console.cloud.tencent.com/smsv2/csms-sign) 或 [国际/港澳台短信](https://console.cloud.tencent.com/smsv2/isms-sign) 的签名管理查看。
<dx-alert infotype="notice" title="注意">发送国内短信该参数必填，且需填写签名内容而非签名ID。</dx-alert>
        :type SignName: str
        :param _TemplateParamSet: 模板参数，若无模板参数，则设置为空。
<dx-alert infotype="notice" title="注意">模板参数的个数需要与 TemplateId 对应模板的变量个数保持一致。</dx-alert>
        :type TemplateParamSet: list of str
        :param _ExtendCode: 短信码号扩展号，默认未开通，如需开通请联系 [腾讯云短信小助手](https://cloud.tencent.com/document/product/382/3773#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81)。
        :type ExtendCode: str
        :param _SessionContext: 用户的 session 内容，可以携带用户侧 ID 等上下文信息，server 会原样返回。注意长度需小于512字节。
        :type SessionContext: str
        :param _SenderId: 国内短信无需填写该项；国际/港澳台短信已申请独立 SenderId 需要填写该字段，默认使用公共 SenderId，无需填写该字段。
注：月度使用量达到指定量级可申请独立 SenderId 使用，详情请联系 [腾讯云短信小助手](https://cloud.tencent.com/document/product/382/3773#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81)。
        :type SenderId: str
        """
        self._PhoneNumberSet = None
        self._SmsSdkAppId = None
        self._TemplateId = None
        self._SignName = None
        self._TemplateParamSet = None
        self._ExtendCode = None
        self._SessionContext = None
        self._SenderId = None

    @property
    def PhoneNumberSet(self):
        return self._PhoneNumberSet

    @PhoneNumberSet.setter
    def PhoneNumberSet(self, PhoneNumberSet):
        self._PhoneNumberSet = PhoneNumberSet

    @property
    def SmsSdkAppId(self):
        return self._SmsSdkAppId

    @SmsSdkAppId.setter
    def SmsSdkAppId(self, SmsSdkAppId):
        self._SmsSdkAppId = SmsSdkAppId

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def SignName(self):
        return self._SignName

    @SignName.setter
    def SignName(self, SignName):
        self._SignName = SignName

    @property
    def TemplateParamSet(self):
        return self._TemplateParamSet

    @TemplateParamSet.setter
    def TemplateParamSet(self, TemplateParamSet):
        self._TemplateParamSet = TemplateParamSet

    @property
    def ExtendCode(self):
        return self._ExtendCode

    @ExtendCode.setter
    def ExtendCode(self, ExtendCode):
        self._ExtendCode = ExtendCode

    @property
    def SessionContext(self):
        return self._SessionContext

    @SessionContext.setter
    def SessionContext(self, SessionContext):
        self._SessionContext = SessionContext

    @property
    def SenderId(self):
        return self._SenderId

    @SenderId.setter
    def SenderId(self, SenderId):
        self._SenderId = SenderId


    def _deserialize(self, params):
        self._PhoneNumberSet = params.get("PhoneNumberSet")
        self._SmsSdkAppId = params.get("SmsSdkAppId")
        self._TemplateId = params.get("TemplateId")
        self._SignName = params.get("SignName")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SendStatusSet = None
        self._RequestId = None

    @property
    def SendStatusSet(self):
        return self._SendStatusSet

    @SendStatusSet.setter
    def SendStatusSet(self, SendStatusSet):
        self._SendStatusSet = SendStatusSet

    @property
    def RequestId(self):
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
        :param _PhoneNumber: 手机号码，E.164标准，+[国家或地区码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :type PhoneNumber: str
        :param _Fee: 计费条数，计费规则请查询 [计费策略](https://cloud.tencent.com/document/product/382/36135)。
        :type Fee: int
        :param _SessionContext: 用户 session 内容。
        :type SessionContext: str
        :param _Code: 短信请求错误码，具体含义请参考 [错误码](https://cloud.tencent.com/document/api/382/55981#6.-.E9.94.99.E8.AF.AF.E7.A0.81)，发送成功返回 "Ok"。
        :type Code: str
        :param _Message: 短信请求错误码描述。
        :type Message: str
        :param _IsoCode: 国家码或地区码，例如 CN、US 等，对于未识别出国家码或者地区码，默认返回 DEF，具体支持列表请参考 [国际/港澳台短信价格总览](https://cloud.tencent.com/document/product/382/18051)。
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
        return self._SerialNo

    @SerialNo.setter
    def SerialNo(self, SerialNo):
        self._SerialNo = SerialNo

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Fee(self):
        return self._Fee

    @Fee.setter
    def Fee(self, Fee):
        self._Fee = Fee

    @property
    def SessionContext(self):
        return self._SessionContext

    @SessionContext.setter
    def SessionContext(self, SessionContext):
        self._SessionContext = SessionContext

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def IsoCode(self):
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
        return self._FeeCount

    @FeeCount.setter
    def FeeCount(self, FeeCount):
        self._FeeCount = FeeCount

    @property
    def RequestCount(self):
        return self._RequestCount

    @RequestCount.setter
    def RequestCount(self, RequestCount):
        self._RequestCount = RequestCount

    @property
    def RequestSuccessCount(self):
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
        :param _BeginTime: 起始时间，格式为yyyymmddhh，精确到小时，例如2021050113，表示2021年5月1号13时。
        :type BeginTime: str
        :param _EndTime: 结束时间，格式为yyyymmddhh，精确到小时，例如2021050118，表示2021年5月1号18时。
注：EndTime 必须大于 BeginTime。
        :type EndTime: str
        :param _SmsSdkAppId: 短信 SdkAppId 在 [短信控制台](https://console.cloud.tencent.com/smsv2/app-manage)  添加应用后生成的实际 SdkAppId，示例如1400006666。
        :type SmsSdkAppId: str
        :param _Limit: 最大上限。
注：目前固定设置为0。
        :type Limit: int
        :param _Offset: 偏移量。
注：目前固定设置为0。
        :type Offset: int
        """
        self._BeginTime = None
        self._EndTime = None
        self._SmsSdkAppId = None
        self._Limit = None
        self._Offset = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SmsSdkAppId(self):
        return self._SmsSdkAppId

    @SmsSdkAppId.setter
    def SmsSdkAppId(self, SmsSdkAppId):
        self._SmsSdkAppId = SmsSdkAppId

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
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._SmsSdkAppId = params.get("SmsSdkAppId")
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
        :type SendStatusStatistics: :class:`tencentcloud.sms.v20210111.models.SendStatusStatistics`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SendStatusStatistics = None
        self._RequestId = None

    @property
    def SendStatusStatistics(self):
        return self._SendStatusStatistics

    @SendStatusStatistics.setter
    def SendStatusStatistics(self, SendStatusStatistics):
        self._SendStatusStatistics = SendStatusStatistics

    @property
    def RequestId(self):
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
        :param _PackageCreateTime: 套餐包创建时间，UNIX 时间戳（单位：秒）。
        :type PackageCreateTime: int
        :param _PackageEffectiveTime: 套餐包生效时间，UNIX 时间戳（单位：秒）。
        :type PackageEffectiveTime: int
        :param _PackageExpiredTime: 套餐包过期时间，UNIX 时间戳（单位：秒）。
        :type PackageExpiredTime: int
        :param _PackageAmount: 套餐包条数。
        :type PackageAmount: int
        :param _PackageType: 套餐包类别，0表示赠送套餐包，1表示购买套餐包。
        :type PackageType: int
        :param _PackageId: 套餐包 ID。
        :type PackageId: int
        :param _CurrentUsage: 当前使用套餐包条数。
        :type CurrentUsage: int
        """
        self._PackageCreateTime = None
        self._PackageEffectiveTime = None
        self._PackageExpiredTime = None
        self._PackageAmount = None
        self._PackageType = None
        self._PackageId = None
        self._CurrentUsage = None

    @property
    def PackageCreateTime(self):
        return self._PackageCreateTime

    @PackageCreateTime.setter
    def PackageCreateTime(self, PackageCreateTime):
        self._PackageCreateTime = PackageCreateTime

    @property
    def PackageEffectiveTime(self):
        return self._PackageEffectiveTime

    @PackageEffectiveTime.setter
    def PackageEffectiveTime(self, PackageEffectiveTime):
        self._PackageEffectiveTime = PackageEffectiveTime

    @property
    def PackageExpiredTime(self):
        return self._PackageExpiredTime

    @PackageExpiredTime.setter
    def PackageExpiredTime(self, PackageExpiredTime):
        self._PackageExpiredTime = PackageExpiredTime

    @property
    def PackageAmount(self):
        return self._PackageAmount

    @PackageAmount.setter
    def PackageAmount(self, PackageAmount):
        self._PackageAmount = PackageAmount

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def CurrentUsage(self):
        return self._CurrentUsage

    @CurrentUsage.setter
    def CurrentUsage(self, CurrentUsage):
        self._CurrentUsage = CurrentUsage


    def _deserialize(self, params):
        self._PackageCreateTime = params.get("PackageCreateTime")
        self._PackageEffectiveTime = params.get("PackageEffectiveTime")
        self._PackageExpiredTime = params.get("PackageExpiredTime")
        self._PackageAmount = params.get("PackageAmount")
        self._PackageType = params.get("PackageType")
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
        :param _SmsSdkAppId: 短信 SdkAppId 在 [短信控制台](https://console.cloud.tencent.com/smsv2/app-manage)  添加应用后生成的实际 SdkAppId，示例如1400006666。
        :type SmsSdkAppId: str
        :param _Limit: 最大上限(需要拉取的套餐包个数)。
        :type Limit: int
        :param _Offset: 偏移量。
        :type Offset: int
        :param _BeginTime: 起始时间，格式为yyyymmddhh，精确到小时，例如2021050113，表示2021年5月1号13时。
注：接口会返回 BeginTime 到 EndTime 之间创建的套餐包的统计信息。
        :type BeginTime: str
        :param _EndTime: 结束时间，格式为yyyymmddhh，精确到小时，例如2021050118，表示2021年5月1号18时。
注：EndTime 必须大于 BeginTime 且小于当前时间。
        :type EndTime: str
        """
        self._SmsSdkAppId = None
        self._Limit = None
        self._Offset = None
        self._BeginTime = None
        self._EndTime = None

    @property
    def SmsSdkAppId(self):
        return self._SmsSdkAppId

    @SmsSdkAppId.setter
    def SmsSdkAppId(self, SmsSdkAppId):
        self._SmsSdkAppId = SmsSdkAppId

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
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._SmsSdkAppId = params.get("SmsSdkAppId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SmsPackagesStatisticsSet = None
        self._RequestId = None

    @property
    def SmsPackagesStatisticsSet(self):
        return self._SmsPackagesStatisticsSet

    @SmsPackagesStatisticsSet.setter
    def SmsPackagesStatisticsSet(self, SmsPackagesStatisticsSet):
        self._SmsPackagesStatisticsSet = SmsPackagesStatisticsSet

    @property
    def RequestId(self):
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