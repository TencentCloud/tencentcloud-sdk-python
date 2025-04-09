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


class Attachment(AbstractModel):
    """附件结构，包含附件名和base64之后的附件内容。

    """

    def __init__(self):
        r"""
        :param _FileName: 附件名称，最大支持255个字符长度，不支持部分附件类型，详情请参考[附件类型](https://cloud.tencent.com/document/product/1288/51951)。
        :type FileName: str
        :param _Content: Base64之后的附件内容，您可以发送的附件大小上限为4M。注意：腾讯云接口请求最大支持 8M 的请求包，附件内容经过 Base64 预期扩大1.5倍。应该控制所有附件的总大小最大在 4M 以内，整体请求超出 8M 接口会返回错误。
        :type Content: str
        :param _FileURL: 附件URL。未开放功能，请勿使用。
        :type FileURL: str
        """
        self._FileName = None
        self._Content = None
        self._FileURL = None

    @property
    def FileName(self):
        """附件名称，最大支持255个字符长度，不支持部分附件类型，详情请参考[附件类型](https://cloud.tencent.com/document/product/1288/51951)。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Content(self):
        """Base64之后的附件内容，您可以发送的附件大小上限为4M。注意：腾讯云接口请求最大支持 8M 的请求包，附件内容经过 Base64 预期扩大1.5倍。应该控制所有附件的总大小最大在 4M 以内，整体请求超出 8M 接口会返回错误。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FileURL(self):
        """附件URL。未开放功能，请勿使用。
        :rtype: str
        """
        return self._FileURL

    @FileURL.setter
    def FileURL(self, FileURL):
        self._FileURL = FileURL


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._Content = params.get("Content")
        self._FileURL = params.get("FileURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchSendEmailRequest(AbstractModel):
    """BatchSendEmail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FromEmailAddress: 发信邮件地址。请填写发件人邮箱地址，例如：noreply@mail.qcloud.com。如需填写发件人说明，请按照
发信人 &lt;邮件地址&gt; 的方式填写，例如：
腾讯云团队 &lt;noreply@mail.qcloud.com&gt;
        :type FromEmailAddress: str
        :param _ReceiverId: 收件人列表ID
        :type ReceiverId: int
        :param _Subject: 邮件主题
        :type Subject: str
        :param _TaskType: 任务类型 1: 立即发送 2: 定时发送 3: 周期（频率）发送
        :type TaskType: int
        :param _ReplyToAddresses: 邮件的“回复”电子邮件地址。可以填写您能收到邮件的邮箱地址，可以是个人邮箱。如果不填，收件人的回复邮件将会发送失败。
        :type ReplyToAddresses: str
        :param _Template: 使用模板发送时，填写的模板相关参数
<dx-alert infotype="notice" title="注意"> 如您未申请过特殊配置，则该字段为必填 </dx-alert>
        :type Template: :class:`tencentcloud.ses.v20201002.models.Template`
        :param _Simple: 已废弃<dx-alert infotype="notice" title="说明"> 仅部分历史上申请了特殊配置的客户需要使用。如您未申请过特殊配置，则不存在该字段。</dx-alert>
        :type Simple: :class:`tencentcloud.ses.v20201002.models.Simple`
        :param _Attachments: 需要发送附件时，填写附件相关参数（暂未支持）
        :type Attachments: list of Attachment
        :param _CycleParam: 周期发送任务的必要参数
        :type CycleParam: :class:`tencentcloud.ses.v20201002.models.CycleEmailParam`
        :param _TimedParam: 定时发送任务的必要参数
        :type TimedParam: :class:`tencentcloud.ses.v20201002.models.TimedEmailParam`
        :param _Unsubscribe: 退订链接选项 0: 不加入退订链接 1: 简体中文 2: 英文 3: 繁体中文 4: 西班牙语 5: 法语 6: 德语 7: 日语 8: 韩语 9: 阿拉伯语 10: 泰语
        :type Unsubscribe: str
        :param _ADLocation: 是否添加广告标识 0:不添加 1:添加到subject前面，2:添加到subject后面
        :type ADLocation: int
        """
        self._FromEmailAddress = None
        self._ReceiverId = None
        self._Subject = None
        self._TaskType = None
        self._ReplyToAddresses = None
        self._Template = None
        self._Simple = None
        self._Attachments = None
        self._CycleParam = None
        self._TimedParam = None
        self._Unsubscribe = None
        self._ADLocation = None

    @property
    def FromEmailAddress(self):
        """发信邮件地址。请填写发件人邮箱地址，例如：noreply@mail.qcloud.com。如需填写发件人说明，请按照
发信人 &lt;邮件地址&gt; 的方式填写，例如：
腾讯云团队 &lt;noreply@mail.qcloud.com&gt;
        :rtype: str
        """
        return self._FromEmailAddress

    @FromEmailAddress.setter
    def FromEmailAddress(self, FromEmailAddress):
        self._FromEmailAddress = FromEmailAddress

    @property
    def ReceiverId(self):
        """收件人列表ID
        :rtype: int
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

    @property
    def Subject(self):
        """邮件主题
        :rtype: str
        """
        return self._Subject

    @Subject.setter
    def Subject(self, Subject):
        self._Subject = Subject

    @property
    def TaskType(self):
        """任务类型 1: 立即发送 2: 定时发送 3: 周期（频率）发送
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def ReplyToAddresses(self):
        """邮件的“回复”电子邮件地址。可以填写您能收到邮件的邮箱地址，可以是个人邮箱。如果不填，收件人的回复邮件将会发送失败。
        :rtype: str
        """
        return self._ReplyToAddresses

    @ReplyToAddresses.setter
    def ReplyToAddresses(self, ReplyToAddresses):
        self._ReplyToAddresses = ReplyToAddresses

    @property
    def Template(self):
        """使用模板发送时，填写的模板相关参数
<dx-alert infotype="notice" title="注意"> 如您未申请过特殊配置，则该字段为必填 </dx-alert>
        :rtype: :class:`tencentcloud.ses.v20201002.models.Template`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def Simple(self):
        """已废弃<dx-alert infotype="notice" title="说明"> 仅部分历史上申请了特殊配置的客户需要使用。如您未申请过特殊配置，则不存在该字段。</dx-alert>
        :rtype: :class:`tencentcloud.ses.v20201002.models.Simple`
        """
        return self._Simple

    @Simple.setter
    def Simple(self, Simple):
        self._Simple = Simple

    @property
    def Attachments(self):
        """需要发送附件时，填写附件相关参数（暂未支持）
        :rtype: list of Attachment
        """
        return self._Attachments

    @Attachments.setter
    def Attachments(self, Attachments):
        self._Attachments = Attachments

    @property
    def CycleParam(self):
        """周期发送任务的必要参数
        :rtype: :class:`tencentcloud.ses.v20201002.models.CycleEmailParam`
        """
        return self._CycleParam

    @CycleParam.setter
    def CycleParam(self, CycleParam):
        self._CycleParam = CycleParam

    @property
    def TimedParam(self):
        """定时发送任务的必要参数
        :rtype: :class:`tencentcloud.ses.v20201002.models.TimedEmailParam`
        """
        return self._TimedParam

    @TimedParam.setter
    def TimedParam(self, TimedParam):
        self._TimedParam = TimedParam

    @property
    def Unsubscribe(self):
        """退订链接选项 0: 不加入退订链接 1: 简体中文 2: 英文 3: 繁体中文 4: 西班牙语 5: 法语 6: 德语 7: 日语 8: 韩语 9: 阿拉伯语 10: 泰语
        :rtype: str
        """
        return self._Unsubscribe

    @Unsubscribe.setter
    def Unsubscribe(self, Unsubscribe):
        self._Unsubscribe = Unsubscribe

    @property
    def ADLocation(self):
        """是否添加广告标识 0:不添加 1:添加到subject前面，2:添加到subject后面
        :rtype: int
        """
        return self._ADLocation

    @ADLocation.setter
    def ADLocation(self, ADLocation):
        self._ADLocation = ADLocation


    def _deserialize(self, params):
        self._FromEmailAddress = params.get("FromEmailAddress")
        self._ReceiverId = params.get("ReceiverId")
        self._Subject = params.get("Subject")
        self._TaskType = params.get("TaskType")
        self._ReplyToAddresses = params.get("ReplyToAddresses")
        if params.get("Template") is not None:
            self._Template = Template()
            self._Template._deserialize(params.get("Template"))
        if params.get("Simple") is not None:
            self._Simple = Simple()
            self._Simple._deserialize(params.get("Simple"))
        if params.get("Attachments") is not None:
            self._Attachments = []
            for item in params.get("Attachments"):
                obj = Attachment()
                obj._deserialize(item)
                self._Attachments.append(obj)
        if params.get("CycleParam") is not None:
            self._CycleParam = CycleEmailParam()
            self._CycleParam._deserialize(params.get("CycleParam"))
        if params.get("TimedParam") is not None:
            self._TimedParam = TimedEmailParam()
            self._TimedParam._deserialize(params.get("TimedParam"))
        self._Unsubscribe = params.get("Unsubscribe")
        self._ADLocation = params.get("ADLocation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchSendEmailResponse(AbstractModel):
    """BatchSendEmail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 发送任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """发送任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class BlackAddressDetail(AbstractModel):
    """黑名单详情

    """

    def __init__(self):
        r"""
        :param _Id: 黑名单地址id
        :type Id: int
        :param _Email: 邮箱地址
        :type Email: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ExpireDate: 过期时间
        :type ExpireDate: str
        :param _Status: 黑名单状态，0:已过期，1:生效中
        :type Status: int
        """
        self._Id = None
        self._Email = None
        self._CreateTime = None
        self._ExpireDate = None
        self._Status = None

    @property
    def Id(self):
        """黑名单地址id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Email(self):
        """邮箱地址
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireDate(self):
        """过期时间
        :rtype: str
        """
        return self._ExpireDate

    @ExpireDate.setter
    def ExpireDate(self, ExpireDate):
        self._ExpireDate = ExpireDate

    @property
    def Status(self):
        """黑名单状态，0:已过期，1:生效中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Email = params.get("Email")
        self._CreateTime = params.get("CreateTime")
        self._ExpireDate = params.get("ExpireDate")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlackEmailAddress(AbstractModel):
    """邮箱黑名单结构，包含被拉黑的邮箱地址和被拉黑时间，以及被拉黑的理由

    """

    def __init__(self):
        r"""
        :param _BounceTime: 邮箱被拉黑时间
        :type BounceTime: str
        :param _EmailAddress: 被拉黑的邮箱地址
        :type EmailAddress: str
        :param _IspDesc: 被拉黑的理由
        :type IspDesc: str
        """
        self._BounceTime = None
        self._EmailAddress = None
        self._IspDesc = None

    @property
    def BounceTime(self):
        """邮箱被拉黑时间
        :rtype: str
        """
        return self._BounceTime

    @BounceTime.setter
    def BounceTime(self, BounceTime):
        self._BounceTime = BounceTime

    @property
    def EmailAddress(self):
        """被拉黑的邮箱地址
        :rtype: str
        """
        return self._EmailAddress

    @EmailAddress.setter
    def EmailAddress(self, EmailAddress):
        self._EmailAddress = EmailAddress

    @property
    def IspDesc(self):
        """被拉黑的理由
        :rtype: str
        """
        return self._IspDesc

    @IspDesc.setter
    def IspDesc(self, IspDesc):
        self._IspDesc = IspDesc


    def _deserialize(self, params):
        self._BounceTime = params.get("BounceTime")
        self._EmailAddress = params.get("EmailAddress")
        self._IspDesc = params.get("IspDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomBlacklistRequest(AbstractModel):
    """CreateCustomBlacklist请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Emails: 添加到黑名单的邮件地址
        :type Emails: list of str
        :param _ExpireDate: 过期日期
        :type ExpireDate: str
        """
        self._Emails = None
        self._ExpireDate = None

    @property
    def Emails(self):
        """添加到黑名单的邮件地址
        :rtype: list of str
        """
        return self._Emails

    @Emails.setter
    def Emails(self, Emails):
        self._Emails = Emails

    @property
    def ExpireDate(self):
        """过期日期
        :rtype: str
        """
        return self._ExpireDate

    @ExpireDate.setter
    def ExpireDate(self, ExpireDate):
        self._ExpireDate = ExpireDate


    def _deserialize(self, params):
        self._Emails = params.get("Emails")
        self._ExpireDate = params.get("ExpireDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomBlacklistResponse(AbstractModel):
    """CreateCustomBlacklist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 收件人总数
        :type TotalCount: int
        :param _ValidCount: 实际上传数量
        :type ValidCount: int
        :param _TooLongCount: 数据过长数量
        :type TooLongCount: int
        :param _RepeatCount: 重复数量
        :type RepeatCount: int
        :param _InvalidCount: 格式不正确数量
        :type InvalidCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ValidCount = None
        self._TooLongCount = None
        self._RepeatCount = None
        self._InvalidCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """收件人总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ValidCount(self):
        """实际上传数量
        :rtype: int
        """
        return self._ValidCount

    @ValidCount.setter
    def ValidCount(self, ValidCount):
        self._ValidCount = ValidCount

    @property
    def TooLongCount(self):
        """数据过长数量
        :rtype: int
        """
        return self._TooLongCount

    @TooLongCount.setter
    def TooLongCount(self, TooLongCount):
        self._TooLongCount = TooLongCount

    @property
    def RepeatCount(self):
        """重复数量
        :rtype: int
        """
        return self._RepeatCount

    @RepeatCount.setter
    def RepeatCount(self, RepeatCount):
        self._RepeatCount = RepeatCount

    @property
    def InvalidCount(self):
        """格式不正确数量
        :rtype: int
        """
        return self._InvalidCount

    @InvalidCount.setter
    def InvalidCount(self, InvalidCount):
        self._InvalidCount = InvalidCount

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
        self._TotalCount = params.get("TotalCount")
        self._ValidCount = params.get("ValidCount")
        self._TooLongCount = params.get("TooLongCount")
        self._RepeatCount = params.get("RepeatCount")
        self._InvalidCount = params.get("InvalidCount")
        self._RequestId = params.get("RequestId")


class CreateEmailAddressRequest(AbstractModel):
    """CreateEmailAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EmailAddress: 您的发信地址（发信地址总数上限为10个）
        :type EmailAddress: str
        :param _EmailSenderName: 发件人别名
        :type EmailSenderName: str
        """
        self._EmailAddress = None
        self._EmailSenderName = None

    @property
    def EmailAddress(self):
        """您的发信地址（发信地址总数上限为10个）
        :rtype: str
        """
        return self._EmailAddress

    @EmailAddress.setter
    def EmailAddress(self, EmailAddress):
        self._EmailAddress = EmailAddress

    @property
    def EmailSenderName(self):
        """发件人别名
        :rtype: str
        """
        return self._EmailSenderName

    @EmailSenderName.setter
    def EmailSenderName(self, EmailSenderName):
        self._EmailSenderName = EmailSenderName


    def _deserialize(self, params):
        self._EmailAddress = params.get("EmailAddress")
        self._EmailSenderName = params.get("EmailSenderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmailAddressResponse(AbstractModel):
    """CreateEmailAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateEmailIdentityRequest(AbstractModel):
    """CreateEmailIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EmailIdentity: 您的发信域名，建议使用三级以上域名。例如：mail.qcloud.com。
        :type EmailIdentity: str
        """
        self._EmailIdentity = None

    @property
    def EmailIdentity(self):
        """您的发信域名，建议使用三级以上域名。例如：mail.qcloud.com。
        :rtype: str
        """
        return self._EmailIdentity

    @EmailIdentity.setter
    def EmailIdentity(self, EmailIdentity):
        self._EmailIdentity = EmailIdentity


    def _deserialize(self, params):
        self._EmailIdentity = params.get("EmailIdentity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmailIdentityResponse(AbstractModel):
    """CreateEmailIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IdentityType: 验证类型。固定值：DOMAIN
        :type IdentityType: str
        :param _VerifiedForSendingStatus: 是否已通过验证
        :type VerifiedForSendingStatus: bool
        :param _Attributes: 需要配置的DNS信息
        :type Attributes: list of DNSAttributes
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IdentityType = None
        self._VerifiedForSendingStatus = None
        self._Attributes = None
        self._RequestId = None

    @property
    def IdentityType(self):
        """验证类型。固定值：DOMAIN
        :rtype: str
        """
        return self._IdentityType

    @IdentityType.setter
    def IdentityType(self, IdentityType):
        self._IdentityType = IdentityType

    @property
    def VerifiedForSendingStatus(self):
        """是否已通过验证
        :rtype: bool
        """
        return self._VerifiedForSendingStatus

    @VerifiedForSendingStatus.setter
    def VerifiedForSendingStatus(self, VerifiedForSendingStatus):
        self._VerifiedForSendingStatus = VerifiedForSendingStatus

    @property
    def Attributes(self):
        """需要配置的DNS信息
        :rtype: list of DNSAttributes
        """
        return self._Attributes

    @Attributes.setter
    def Attributes(self, Attributes):
        self._Attributes = Attributes

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
        self._IdentityType = params.get("IdentityType")
        self._VerifiedForSendingStatus = params.get("VerifiedForSendingStatus")
        if params.get("Attributes") is not None:
            self._Attributes = []
            for item in params.get("Attributes"):
                obj = DNSAttributes()
                obj._deserialize(item)
                self._Attributes.append(obj)
        self._RequestId = params.get("RequestId")


class CreateEmailTemplateRequest(AbstractModel):
    """CreateEmailTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateName: 模板名称
        :type TemplateName: str
        :param _TemplateContent: 模板内容
        :type TemplateContent: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        """
        self._TemplateName = None
        self._TemplateContent = None

    @property
    def TemplateName(self):
        """模板名称
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateContent(self):
        """模板内容
        :rtype: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        """
        return self._TemplateContent

    @TemplateContent.setter
    def TemplateContent(self, TemplateContent):
        self._TemplateContent = TemplateContent


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        if params.get("TemplateContent") is not None:
            self._TemplateContent = TemplateContent()
            self._TemplateContent._deserialize(params.get("TemplateContent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmailTemplateResponse(AbstractModel):
    """CreateEmailTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateID: 模板id
        :type TemplateID: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateID = None
        self._RequestId = None

    @property
    def TemplateID(self):
        """模板id
        :rtype: int
        """
        return self._TemplateID

    @TemplateID.setter
    def TemplateID(self, TemplateID):
        self._TemplateID = TemplateID

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
        self._TemplateID = params.get("TemplateID")
        self._RequestId = params.get("RequestId")


class CreateReceiverDetailRequest(AbstractModel):
    """CreateReceiverDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReceiverId: 收件人列表ID
        :type ReceiverId: int
        :param _Emails: 邮箱
        :type Emails: list of str
        """
        self._ReceiverId = None
        self._Emails = None

    @property
    def ReceiverId(self):
        """收件人列表ID
        :rtype: int
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

    @property
    def Emails(self):
        """邮箱
        :rtype: list of str
        """
        return self._Emails

    @Emails.setter
    def Emails(self, Emails):
        self._Emails = Emails


    def _deserialize(self, params):
        self._ReceiverId = params.get("ReceiverId")
        self._Emails = params.get("Emails")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReceiverDetailResponse(AbstractModel):
    """CreateReceiverDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 收件人总数
        :type TotalCount: int
        :param _ValidCount: 实际上传数量
        :type ValidCount: int
        :param _TooLongCount: 数据过长数量
        :type TooLongCount: int
        :param _EmptyEmailCount: 邮件地址为空数量
        :type EmptyEmailCount: int
        :param _RepeatCount: 重复数量
        :type RepeatCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ValidCount = None
        self._TooLongCount = None
        self._EmptyEmailCount = None
        self._RepeatCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """收件人总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ValidCount(self):
        """实际上传数量
        :rtype: int
        """
        return self._ValidCount

    @ValidCount.setter
    def ValidCount(self, ValidCount):
        self._ValidCount = ValidCount

    @property
    def TooLongCount(self):
        """数据过长数量
        :rtype: int
        """
        return self._TooLongCount

    @TooLongCount.setter
    def TooLongCount(self, TooLongCount):
        self._TooLongCount = TooLongCount

    @property
    def EmptyEmailCount(self):
        """邮件地址为空数量
        :rtype: int
        """
        return self._EmptyEmailCount

    @EmptyEmailCount.setter
    def EmptyEmailCount(self, EmptyEmailCount):
        self._EmptyEmailCount = EmptyEmailCount

    @property
    def RepeatCount(self):
        """重复数量
        :rtype: int
        """
        return self._RepeatCount

    @RepeatCount.setter
    def RepeatCount(self, RepeatCount):
        self._RepeatCount = RepeatCount

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
        self._TotalCount = params.get("TotalCount")
        self._ValidCount = params.get("ValidCount")
        self._TooLongCount = params.get("TooLongCount")
        self._EmptyEmailCount = params.get("EmptyEmailCount")
        self._RepeatCount = params.get("RepeatCount")
        self._RequestId = params.get("RequestId")


class CreateReceiverDetailWithDataRequest(AbstractModel):
    """CreateReceiverDetailWithData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReceiverId: 收件人列表ID
        :type ReceiverId: int
        :param _Datas: 收信人邮箱以及模板参数，数组形式。收件人个数限制20000个以内。
        :type Datas: list of ReceiverInputData
        """
        self._ReceiverId = None
        self._Datas = None

    @property
    def ReceiverId(self):
        """收件人列表ID
        :rtype: int
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

    @property
    def Datas(self):
        """收信人邮箱以及模板参数，数组形式。收件人个数限制20000个以内。
        :rtype: list of ReceiverInputData
        """
        return self._Datas

    @Datas.setter
    def Datas(self, Datas):
        self._Datas = Datas


    def _deserialize(self, params):
        self._ReceiverId = params.get("ReceiverId")
        if params.get("Datas") is not None:
            self._Datas = []
            for item in params.get("Datas"):
                obj = ReceiverInputData()
                obj._deserialize(item)
                self._Datas.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReceiverDetailWithDataResponse(AbstractModel):
    """CreateReceiverDetailWithData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 收件人总数
        :type TotalCount: int
        :param _ValidCount: 实际上传数量
        :type ValidCount: int
        :param _TooLongCount: 数据过长数量
        :type TooLongCount: int
        :param _EmptyEmailCount: 邮件地址为空数量
        :type EmptyEmailCount: int
        :param _RepeatCount: 重复数量
        :type RepeatCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ValidCount = None
        self._TooLongCount = None
        self._EmptyEmailCount = None
        self._RepeatCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """收件人总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ValidCount(self):
        """实际上传数量
        :rtype: int
        """
        return self._ValidCount

    @ValidCount.setter
    def ValidCount(self, ValidCount):
        self._ValidCount = ValidCount

    @property
    def TooLongCount(self):
        """数据过长数量
        :rtype: int
        """
        return self._TooLongCount

    @TooLongCount.setter
    def TooLongCount(self, TooLongCount):
        self._TooLongCount = TooLongCount

    @property
    def EmptyEmailCount(self):
        """邮件地址为空数量
        :rtype: int
        """
        return self._EmptyEmailCount

    @EmptyEmailCount.setter
    def EmptyEmailCount(self, EmptyEmailCount):
        self._EmptyEmailCount = EmptyEmailCount

    @property
    def RepeatCount(self):
        """重复数量
        :rtype: int
        """
        return self._RepeatCount

    @RepeatCount.setter
    def RepeatCount(self, RepeatCount):
        self._RepeatCount = RepeatCount

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
        self._TotalCount = params.get("TotalCount")
        self._ValidCount = params.get("ValidCount")
        self._TooLongCount = params.get("TooLongCount")
        self._EmptyEmailCount = params.get("EmptyEmailCount")
        self._RepeatCount = params.get("RepeatCount")
        self._RequestId = params.get("RequestId")


class CreateReceiverRequest(AbstractModel):
    """CreateReceiver请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReceiversName: 收件人列表名称
        :type ReceiversName: str
        :param _Desc: 收件人列表描述
        :type Desc: str
        """
        self._ReceiversName = None
        self._Desc = None

    @property
    def ReceiversName(self):
        """收件人列表名称
        :rtype: str
        """
        return self._ReceiversName

    @ReceiversName.setter
    def ReceiversName(self, ReceiversName):
        self._ReceiversName = ReceiversName

    @property
    def Desc(self):
        """收件人列表描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._ReceiversName = params.get("ReceiversName")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReceiverResponse(AbstractModel):
    """CreateReceiver返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReceiverId: 收件人列表id，后续根据收件人列表id上传收件人地址
        :type ReceiverId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReceiverId = None
        self._RequestId = None

    @property
    def ReceiverId(self):
        """收件人列表id，后续根据收件人列表id上传收件人地址
        :rtype: int
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

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
        self._ReceiverId = params.get("ReceiverId")
        self._RequestId = params.get("RequestId")


class CycleEmailParam(AbstractModel):
    """创建重复周期发送邮件任务的参数

    """

    def __init__(self):
        r"""
        :param _BeginTime: 任务开始时间
        :type BeginTime: str
        :param _IntervalTime: 任务周期 小时维度
        :type IntervalTime: int
        :param _TermCycle: 是否终止周期，用于任务更新 0否1是
        :type TermCycle: int
        """
        self._BeginTime = None
        self._IntervalTime = None
        self._TermCycle = None

    @property
    def BeginTime(self):
        """任务开始时间
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def IntervalTime(self):
        """任务周期 小时维度
        :rtype: int
        """
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def TermCycle(self):
        """是否终止周期，用于任务更新 0否1是
        :rtype: int
        """
        return self._TermCycle

    @TermCycle.setter
    def TermCycle(self, TermCycle):
        self._TermCycle = TermCycle


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._IntervalTime = params.get("IntervalTime")
        self._TermCycle = params.get("TermCycle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DNSAttributes(AbstractModel):
    """用于描述DNS记录的域名、记录类型、期望得到的值、目前配置的值

    """

    def __init__(self):
        r"""
        :param _Type: 记录类型 CNAME | A | TXT | MX
        :type Type: str
        :param _SendDomain: 域名
        :type SendDomain: str
        :param _ExpectedValue: 需要配置的值
        :type ExpectedValue: str
        :param _CurrentValue: 腾讯云目前检测到的值
        :type CurrentValue: str
        :param _Status: 检测是否通过，创建时默认为false
        :type Status: bool
        """
        self._Type = None
        self._SendDomain = None
        self._ExpectedValue = None
        self._CurrentValue = None
        self._Status = None

    @property
    def Type(self):
        """记录类型 CNAME | A | TXT | MX
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SendDomain(self):
        """域名
        :rtype: str
        """
        return self._SendDomain

    @SendDomain.setter
    def SendDomain(self, SendDomain):
        self._SendDomain = SendDomain

    @property
    def ExpectedValue(self):
        """需要配置的值
        :rtype: str
        """
        return self._ExpectedValue

    @ExpectedValue.setter
    def ExpectedValue(self, ExpectedValue):
        self._ExpectedValue = ExpectedValue

    @property
    def CurrentValue(self):
        """腾讯云目前检测到的值
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Status(self):
        """检测是否通过，创建时默认为false
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._SendDomain = params.get("SendDomain")
        self._ExpectedValue = params.get("ExpectedValue")
        self._CurrentValue = params.get("CurrentValue")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBlackListRequest(AbstractModel):
    """DeleteBlackList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EmailAddressList: 需要清除的黑名单邮箱列表，数组长度至少为1
        :type EmailAddressList: list of str
        """
        self._EmailAddressList = None

    @property
    def EmailAddressList(self):
        """需要清除的黑名单邮箱列表，数组长度至少为1
        :rtype: list of str
        """
        return self._EmailAddressList

    @EmailAddressList.setter
    def EmailAddressList(self, EmailAddressList):
        self._EmailAddressList = EmailAddressList


    def _deserialize(self, params):
        self._EmailAddressList = params.get("EmailAddressList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBlackListResponse(AbstractModel):
    """DeleteBlackList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteCustomBlackListRequest(AbstractModel):
    """DeleteCustomBlackList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Emails: 需要删除的邮箱地址
        :type Emails: list of str
        """
        self._Emails = None

    @property
    def Emails(self):
        """需要删除的邮箱地址
        :rtype: list of str
        """
        return self._Emails

    @Emails.setter
    def Emails(self, Emails):
        self._Emails = Emails


    def _deserialize(self, params):
        self._Emails = params.get("Emails")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomBlackListResponse(AbstractModel):
    """DeleteCustomBlackList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteEmailAddressRequest(AbstractModel):
    """DeleteEmailAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EmailAddress: 发信地址
        :type EmailAddress: str
        """
        self._EmailAddress = None

    @property
    def EmailAddress(self):
        """发信地址
        :rtype: str
        """
        return self._EmailAddress

    @EmailAddress.setter
    def EmailAddress(self, EmailAddress):
        self._EmailAddress = EmailAddress


    def _deserialize(self, params):
        self._EmailAddress = params.get("EmailAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEmailAddressResponse(AbstractModel):
    """DeleteEmailAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteEmailIdentityRequest(AbstractModel):
    """DeleteEmailIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EmailIdentity: 发信域名
        :type EmailIdentity: str
        """
        self._EmailIdentity = None

    @property
    def EmailIdentity(self):
        """发信域名
        :rtype: str
        """
        return self._EmailIdentity

    @EmailIdentity.setter
    def EmailIdentity(self, EmailIdentity):
        self._EmailIdentity = EmailIdentity


    def _deserialize(self, params):
        self._EmailIdentity = params.get("EmailIdentity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEmailIdentityResponse(AbstractModel):
    """DeleteEmailIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteEmailTemplateRequest(AbstractModel):
    """DeleteEmailTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateID: 模板ID
        :type TemplateID: int
        """
        self._TemplateID = None

    @property
    def TemplateID(self):
        """模板ID
        :rtype: int
        """
        return self._TemplateID

    @TemplateID.setter
    def TemplateID(self, TemplateID):
        self._TemplateID = TemplateID


    def _deserialize(self, params):
        self._TemplateID = params.get("TemplateID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEmailTemplateResponse(AbstractModel):
    """DeleteEmailTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteReceiverRequest(AbstractModel):
    """DeleteReceiver请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReceiverId: 收件人列表id，创建收件人列表时会返回
        :type ReceiverId: int
        """
        self._ReceiverId = None

    @property
    def ReceiverId(self):
        """收件人列表id，创建收件人列表时会返回
        :rtype: int
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId


    def _deserialize(self, params):
        self._ReceiverId = params.get("ReceiverId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReceiverResponse(AbstractModel):
    """DeleteReceiver返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class EmailIdentity(AbstractModel):
    """发信域名验证列表结构体

    """

    def __init__(self):
        r"""
        :param _IdentityName: 发信域名
        :type IdentityName: str
        :param _IdentityType: 验证类型，固定为DOMAIN
        :type IdentityType: str
        :param _SendingEnabled: 是否已通过验证
        :type SendingEnabled: bool
        :param _CurrentReputationLevel: 当前信誉等级
        :type CurrentReputationLevel: int
        :param _DailyQuota: 当日最高发信量
        :type DailyQuota: int
        :param _SendIp: 域名配置的独立ip
        :type SendIp: list of str
        """
        self._IdentityName = None
        self._IdentityType = None
        self._SendingEnabled = None
        self._CurrentReputationLevel = None
        self._DailyQuota = None
        self._SendIp = None

    @property
    def IdentityName(self):
        """发信域名
        :rtype: str
        """
        return self._IdentityName

    @IdentityName.setter
    def IdentityName(self, IdentityName):
        self._IdentityName = IdentityName

    @property
    def IdentityType(self):
        """验证类型，固定为DOMAIN
        :rtype: str
        """
        return self._IdentityType

    @IdentityType.setter
    def IdentityType(self, IdentityType):
        self._IdentityType = IdentityType

    @property
    def SendingEnabled(self):
        """是否已通过验证
        :rtype: bool
        """
        return self._SendingEnabled

    @SendingEnabled.setter
    def SendingEnabled(self, SendingEnabled):
        self._SendingEnabled = SendingEnabled

    @property
    def CurrentReputationLevel(self):
        """当前信誉等级
        :rtype: int
        """
        return self._CurrentReputationLevel

    @CurrentReputationLevel.setter
    def CurrentReputationLevel(self, CurrentReputationLevel):
        self._CurrentReputationLevel = CurrentReputationLevel

    @property
    def DailyQuota(self):
        """当日最高发信量
        :rtype: int
        """
        return self._DailyQuota

    @DailyQuota.setter
    def DailyQuota(self, DailyQuota):
        self._DailyQuota = DailyQuota

    @property
    def SendIp(self):
        """域名配置的独立ip
        :rtype: list of str
        """
        return self._SendIp

    @SendIp.setter
    def SendIp(self, SendIp):
        self._SendIp = SendIp


    def _deserialize(self, params):
        self._IdentityName = params.get("IdentityName")
        self._IdentityType = params.get("IdentityType")
        self._SendingEnabled = params.get("SendingEnabled")
        self._CurrentReputationLevel = params.get("CurrentReputationLevel")
        self._DailyQuota = params.get("DailyQuota")
        self._SendIp = params.get("SendIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmailSender(AbstractModel):
    """用于描述发件人相关信息

    """

    def __init__(self):
        r"""
        :param _EmailAddress: 发信地址
        :type EmailAddress: str
        :param _EmailSenderName: 发信人别名
        :type EmailSenderName: str
        :param _CreatedTimestamp: 创建时间
        :type CreatedTimestamp: int
        :param _SmtpPwdType: smtp密码类型,0=没有设置密码,1=已经设置了密码
        :type SmtpPwdType: int
        """
        self._EmailAddress = None
        self._EmailSenderName = None
        self._CreatedTimestamp = None
        self._SmtpPwdType = None

    @property
    def EmailAddress(self):
        """发信地址
        :rtype: str
        """
        return self._EmailAddress

    @EmailAddress.setter
    def EmailAddress(self, EmailAddress):
        self._EmailAddress = EmailAddress

    @property
    def EmailSenderName(self):
        """发信人别名
        :rtype: str
        """
        return self._EmailSenderName

    @EmailSenderName.setter
    def EmailSenderName(self, EmailSenderName):
        self._EmailSenderName = EmailSenderName

    @property
    def CreatedTimestamp(self):
        """创建时间
        :rtype: int
        """
        return self._CreatedTimestamp

    @CreatedTimestamp.setter
    def CreatedTimestamp(self, CreatedTimestamp):
        self._CreatedTimestamp = CreatedTimestamp

    @property
    def SmtpPwdType(self):
        """smtp密码类型,0=没有设置密码,1=已经设置了密码
        :rtype: int
        """
        return self._SmtpPwdType

    @SmtpPwdType.setter
    def SmtpPwdType(self, SmtpPwdType):
        self._SmtpPwdType = SmtpPwdType


    def _deserialize(self, params):
        self._EmailAddress = params.get("EmailAddress")
        self._EmailSenderName = params.get("EmailSenderName")
        self._CreatedTimestamp = params.get("CreatedTimestamp")
        self._SmtpPwdType = params.get("SmtpPwdType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEmailIdentityRequest(AbstractModel):
    """GetEmailIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EmailIdentity: 发信域名
        :type EmailIdentity: str
        """
        self._EmailIdentity = None

    @property
    def EmailIdentity(self):
        """发信域名
        :rtype: str
        """
        return self._EmailIdentity

    @EmailIdentity.setter
    def EmailIdentity(self, EmailIdentity):
        self._EmailIdentity = EmailIdentity


    def _deserialize(self, params):
        self._EmailIdentity = params.get("EmailIdentity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEmailIdentityResponse(AbstractModel):
    """GetEmailIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IdentityType: 验证类型。固定值：DOMAIN
        :type IdentityType: str
        :param _VerifiedForSendingStatus: 是否已通过验证
        :type VerifiedForSendingStatus: bool
        :param _Attributes: DNS配置详情
        :type Attributes: list of DNSAttributes
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IdentityType = None
        self._VerifiedForSendingStatus = None
        self._Attributes = None
        self._RequestId = None

    @property
    def IdentityType(self):
        """验证类型。固定值：DOMAIN
        :rtype: str
        """
        return self._IdentityType

    @IdentityType.setter
    def IdentityType(self, IdentityType):
        self._IdentityType = IdentityType

    @property
    def VerifiedForSendingStatus(self):
        """是否已通过验证
        :rtype: bool
        """
        return self._VerifiedForSendingStatus

    @VerifiedForSendingStatus.setter
    def VerifiedForSendingStatus(self, VerifiedForSendingStatus):
        self._VerifiedForSendingStatus = VerifiedForSendingStatus

    @property
    def Attributes(self):
        """DNS配置详情
        :rtype: list of DNSAttributes
        """
        return self._Attributes

    @Attributes.setter
    def Attributes(self, Attributes):
        self._Attributes = Attributes

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
        self._IdentityType = params.get("IdentityType")
        self._VerifiedForSendingStatus = params.get("VerifiedForSendingStatus")
        if params.get("Attributes") is not None:
            self._Attributes = []
            for item in params.get("Attributes"):
                obj = DNSAttributes()
                obj._deserialize(item)
                self._Attributes.append(obj)
        self._RequestId = params.get("RequestId")


class GetEmailTemplateRequest(AbstractModel):
    """GetEmailTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateID: 模板ID
        :type TemplateID: int
        """
        self._TemplateID = None

    @property
    def TemplateID(self):
        """模板ID
        :rtype: int
        """
        return self._TemplateID

    @TemplateID.setter
    def TemplateID(self, TemplateID):
        self._TemplateID = TemplateID


    def _deserialize(self, params):
        self._TemplateID = params.get("TemplateID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEmailTemplateResponse(AbstractModel):
    """GetEmailTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateContent: 模板内容数据
        :type TemplateContent: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        :param _TemplateStatus: 模板状态 0-审核通过 1-待审核 2-审核拒绝
        :type TemplateStatus: int
        :param _TemplateName: 模板名称
        :type TemplateName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateContent = None
        self._TemplateStatus = None
        self._TemplateName = None
        self._RequestId = None

    @property
    def TemplateContent(self):
        """模板内容数据
        :rtype: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        """
        return self._TemplateContent

    @TemplateContent.setter
    def TemplateContent(self, TemplateContent):
        self._TemplateContent = TemplateContent

    @property
    def TemplateStatus(self):
        """模板状态 0-审核通过 1-待审核 2-审核拒绝
        :rtype: int
        """
        return self._TemplateStatus

    @TemplateStatus.setter
    def TemplateStatus(self, TemplateStatus):
        self._TemplateStatus = TemplateStatus

    @property
    def TemplateName(self):
        """模板名称
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

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
        if params.get("TemplateContent") is not None:
            self._TemplateContent = TemplateContent()
            self._TemplateContent._deserialize(params.get("TemplateContent"))
        self._TemplateStatus = params.get("TemplateStatus")
        self._TemplateName = params.get("TemplateName")
        self._RequestId = params.get("RequestId")


class GetSendEmailStatusRequest(AbstractModel):
    """GetSendEmailStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestDate: 发送的日期，必填。仅支持查询某个日期，不支持范围查询。
        :type RequestDate: str
        :param _Offset: 偏移量。默认为0
        :type Offset: int
        :param _Limit: 拉取最大条数，最多 100。
        :type Limit: int
        :param _MessageId: SendMail接口返回的MessageId字段。
        :type MessageId: str
        :param _ToEmailAddress: 收件人邮箱。
        :type ToEmailAddress: str
        """
        self._RequestDate = None
        self._Offset = None
        self._Limit = None
        self._MessageId = None
        self._ToEmailAddress = None

    @property
    def RequestDate(self):
        """发送的日期，必填。仅支持查询某个日期，不支持范围查询。
        :rtype: str
        """
        return self._RequestDate

    @RequestDate.setter
    def RequestDate(self, RequestDate):
        self._RequestDate = RequestDate

    @property
    def Offset(self):
        """偏移量。默认为0
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
    def MessageId(self):
        """SendMail接口返回的MessageId字段。
        :rtype: str
        """
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def ToEmailAddress(self):
        """收件人邮箱。
        :rtype: str
        """
        return self._ToEmailAddress

    @ToEmailAddress.setter
    def ToEmailAddress(self, ToEmailAddress):
        self._ToEmailAddress = ToEmailAddress


    def _deserialize(self, params):
        self._RequestDate = params.get("RequestDate")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MessageId = params.get("MessageId")
        self._ToEmailAddress = params.get("ToEmailAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSendEmailStatusResponse(AbstractModel):
    """GetSendEmailStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EmailStatusList: 邮件发送状态列表
        :type EmailStatusList: list of SendEmailStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EmailStatusList = None
        self._RequestId = None

    @property
    def EmailStatusList(self):
        """邮件发送状态列表
        :rtype: list of SendEmailStatus
        """
        return self._EmailStatusList

    @EmailStatusList.setter
    def EmailStatusList(self, EmailStatusList):
        self._EmailStatusList = EmailStatusList

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
        if params.get("EmailStatusList") is not None:
            self._EmailStatusList = []
            for item in params.get("EmailStatusList"):
                obj = SendEmailStatus()
                obj._deserialize(item)
                self._EmailStatusList.append(obj)
        self._RequestId = params.get("RequestId")


class GetStatisticsReportRequest(AbstractModel):
    """GetStatisticsReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartDate: 开始日期
        :type StartDate: str
        :param _EndDate: 结束日期
        :type EndDate: str
        :param _Domain: 发信域名
        :type Domain: str
        :param _ReceivingMailboxType: 收件方邮箱类型，例如gmail.com
        :type ReceivingMailboxType: str
        """
        self._StartDate = None
        self._EndDate = None
        self._Domain = None
        self._ReceivingMailboxType = None

    @property
    def StartDate(self):
        """开始日期
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """结束日期
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Domain(self):
        """发信域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ReceivingMailboxType(self):
        """收件方邮箱类型，例如gmail.com
        :rtype: str
        """
        return self._ReceivingMailboxType

    @ReceivingMailboxType.setter
    def ReceivingMailboxType(self, ReceivingMailboxType):
        self._ReceivingMailboxType = ReceivingMailboxType


    def _deserialize(self, params):
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Domain = params.get("Domain")
        self._ReceivingMailboxType = params.get("ReceivingMailboxType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetStatisticsReportResponse(AbstractModel):
    """GetStatisticsReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DailyVolumes: 发信统计报告，按天
        :type DailyVolumes: list of Volume
        :param _OverallVolume: 发信统计报告，总览
        :type OverallVolume: :class:`tencentcloud.ses.v20201002.models.Volume`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DailyVolumes = None
        self._OverallVolume = None
        self._RequestId = None

    @property
    def DailyVolumes(self):
        """发信统计报告，按天
        :rtype: list of Volume
        """
        return self._DailyVolumes

    @DailyVolumes.setter
    def DailyVolumes(self, DailyVolumes):
        self._DailyVolumes = DailyVolumes

    @property
    def OverallVolume(self):
        """发信统计报告，总览
        :rtype: :class:`tencentcloud.ses.v20201002.models.Volume`
        """
        return self._OverallVolume

    @OverallVolume.setter
    def OverallVolume(self, OverallVolume):
        self._OverallVolume = OverallVolume

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
        if params.get("DailyVolumes") is not None:
            self._DailyVolumes = []
            for item in params.get("DailyVolumes"):
                obj = Volume()
                obj._deserialize(item)
                self._DailyVolumes.append(obj)
        if params.get("OverallVolume") is not None:
            self._OverallVolume = Volume()
            self._OverallVolume._deserialize(params.get("OverallVolume"))
        self._RequestId = params.get("RequestId")


class ListBlackEmailAddressRequest(AbstractModel):
    """ListBlackEmailAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartDate: 开始日期，格式为YYYY-MM-DD
        :type StartDate: str
        :param _EndDate: 结束日期，格式为YYYY-MM-DD
        :type EndDate: str
        :param _Limit: 规范，配合Offset使用
        :type Limit: int
        :param _Offset: 规范，配合Limit使用，Limit最大取值为100
        :type Offset: int
        :param _EmailAddress: 可以指定邮箱进行查询
        :type EmailAddress: str
        :param _TaskID: 已废弃
        :type TaskID: str
        """
        self._StartDate = None
        self._EndDate = None
        self._Limit = None
        self._Offset = None
        self._EmailAddress = None
        self._TaskID = None

    @property
    def StartDate(self):
        """开始日期，格式为YYYY-MM-DD
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """结束日期，格式为YYYY-MM-DD
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Limit(self):
        """规范，配合Offset使用
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """规范，配合Limit使用，Limit最大取值为100
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EmailAddress(self):
        """可以指定邮箱进行查询
        :rtype: str
        """
        return self._EmailAddress

    @EmailAddress.setter
    def EmailAddress(self, EmailAddress):
        self._EmailAddress = EmailAddress

    @property
    def TaskID(self):
        """已废弃
        :rtype: str
        """
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID


    def _deserialize(self, params):
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EmailAddress = params.get("EmailAddress")
        self._TaskID = params.get("TaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListBlackEmailAddressResponse(AbstractModel):
    """ListBlackEmailAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BlackList: 黑名单列表
        :type BlackList: list of BlackEmailAddress
        :param _TotalCount: 黑名单总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BlackList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def BlackList(self):
        """黑名单列表
        :rtype: list of BlackEmailAddress
        """
        return self._BlackList

    @BlackList.setter
    def BlackList(self, BlackList):
        self._BlackList = BlackList

    @property
    def TotalCount(self):
        """黑名单总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("BlackList") is not None:
            self._BlackList = []
            for item in params.get("BlackList"):
                obj = BlackEmailAddress()
                obj._deserialize(item)
                self._BlackList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListCustomBlacklistRequest(AbstractModel):
    """ListCustomBlacklist请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，整型，从0开始
        :type Offset: int
        :param _Limit: 限制数目，整型,不超过100
        :type Limit: int
        :param _Status: 筛选黑名单的状态，0:已过期，1:生效中, 2:全部
        :type Status: int
        :param _Email: 黑名单中的邮箱地址
        :type Email: str
        """
        self._Offset = None
        self._Limit = None
        self._Status = None
        self._Email = None

    @property
    def Offset(self):
        """偏移量，整型，从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制数目，整型,不超过100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Status(self):
        """筛选黑名单的状态，0:已过期，1:生效中, 2:全部
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Email(self):
        """黑名单中的邮箱地址
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Status = params.get("Status")
        self._Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCustomBlacklistResponse(AbstractModel):
    """ListCustomBlacklist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 列表总数
        :type TotalCount: int
        :param _Data: 黑名单列表详情
        :type Data: list of BlackAddressDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """列表总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        """黑名单列表详情
        :rtype: list of BlackAddressDetail
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = BlackAddressDetail()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListEmailAddressRequest(AbstractModel):
    """ListEmailAddress请求参数结构体

    """


class ListEmailAddressResponse(AbstractModel):
    """ListEmailAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EmailSenders: 发信地址列表详情
        :type EmailSenders: list of EmailSender
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EmailSenders = None
        self._RequestId = None

    @property
    def EmailSenders(self):
        """发信地址列表详情
        :rtype: list of EmailSender
        """
        return self._EmailSenders

    @EmailSenders.setter
    def EmailSenders(self, EmailSenders):
        self._EmailSenders = EmailSenders

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
        if params.get("EmailSenders") is not None:
            self._EmailSenders = []
            for item in params.get("EmailSenders"):
                obj = EmailSender()
                obj._deserialize(item)
                self._EmailSenders.append(obj)
        self._RequestId = params.get("RequestId")


class ListEmailIdentitiesRequest(AbstractModel):
    """ListEmailIdentities请求参数结构体

    """


class ListEmailIdentitiesResponse(AbstractModel):
    """ListEmailIdentities返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EmailIdentities: 发信域名列表
        :type EmailIdentities: list of EmailIdentity
        :param _MaxReputationLevel: 最大信誉等级
        :type MaxReputationLevel: int
        :param _MaxDailyQuota: 单域名最高日发送量
        :type MaxDailyQuota: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EmailIdentities = None
        self._MaxReputationLevel = None
        self._MaxDailyQuota = None
        self._RequestId = None

    @property
    def EmailIdentities(self):
        """发信域名列表
        :rtype: list of EmailIdentity
        """
        return self._EmailIdentities

    @EmailIdentities.setter
    def EmailIdentities(self, EmailIdentities):
        self._EmailIdentities = EmailIdentities

    @property
    def MaxReputationLevel(self):
        """最大信誉等级
        :rtype: int
        """
        return self._MaxReputationLevel

    @MaxReputationLevel.setter
    def MaxReputationLevel(self, MaxReputationLevel):
        self._MaxReputationLevel = MaxReputationLevel

    @property
    def MaxDailyQuota(self):
        """单域名最高日发送量
        :rtype: int
        """
        return self._MaxDailyQuota

    @MaxDailyQuota.setter
    def MaxDailyQuota(self, MaxDailyQuota):
        self._MaxDailyQuota = MaxDailyQuota

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
        if params.get("EmailIdentities") is not None:
            self._EmailIdentities = []
            for item in params.get("EmailIdentities"):
                obj = EmailIdentity()
                obj._deserialize(item)
                self._EmailIdentities.append(obj)
        self._MaxReputationLevel = params.get("MaxReputationLevel")
        self._MaxDailyQuota = params.get("MaxDailyQuota")
        self._RequestId = params.get("RequestId")


class ListEmailTemplatesRequest(AbstractModel):
    """ListEmailTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 获取模板数据量，用于分页
        :type Limit: int
        :param _Offset: 获取模板偏移值，用于分页
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        """获取模板数据量，用于分页
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """获取模板偏移值，用于分页
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEmailTemplatesResponse(AbstractModel):
    """ListEmailTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplatesMetadata: 邮件模板列表
        :type TemplatesMetadata: list of TemplatesMetadata
        :param _TotalCount: 模板总数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplatesMetadata = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TemplatesMetadata(self):
        """邮件模板列表
        :rtype: list of TemplatesMetadata
        """
        return self._TemplatesMetadata

    @TemplatesMetadata.setter
    def TemplatesMetadata(self, TemplatesMetadata):
        self._TemplatesMetadata = TemplatesMetadata

    @property
    def TotalCount(self):
        """模板总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("TemplatesMetadata") is not None:
            self._TemplatesMetadata = []
            for item in params.get("TemplatesMetadata"):
                obj = TemplatesMetadata()
                obj._deserialize(item)
                self._TemplatesMetadata.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListReceiverDetailsRequest(AbstractModel):
    """ListReceiverDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReceiverId: 收件人列表ID,CreateReceiver接口创建收件人列表时会返回该值
        :type ReceiverId: int
        :param _Offset: 偏移量，整型，从0开始
        :type Offset: int
        :param _Limit: 限制数目，整型,不超过100
        :type Limit: int
        :param _Email: 收件人地址，长度0-50，示例：xxx@te.com，支持模糊查询
        :type Email: str
        :param _CreateTimeBegin: 搜索开始时间
        :type CreateTimeBegin: str
        :param _CreateTimeEnd: 搜索结束时间
        :type CreateTimeEnd: str
        :param _Status: 1:有效，2:无效
        :type Status: int
        """
        self._ReceiverId = None
        self._Offset = None
        self._Limit = None
        self._Email = None
        self._CreateTimeBegin = None
        self._CreateTimeEnd = None
        self._Status = None

    @property
    def ReceiverId(self):
        """收件人列表ID,CreateReceiver接口创建收件人列表时会返回该值
        :rtype: int
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

    @property
    def Offset(self):
        """偏移量，整型，从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制数目，整型,不超过100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Email(self):
        """收件人地址，长度0-50，示例：xxx@te.com，支持模糊查询
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def CreateTimeBegin(self):
        """搜索开始时间
        :rtype: str
        """
        return self._CreateTimeBegin

    @CreateTimeBegin.setter
    def CreateTimeBegin(self, CreateTimeBegin):
        self._CreateTimeBegin = CreateTimeBegin

    @property
    def CreateTimeEnd(self):
        """搜索结束时间
        :rtype: str
        """
        return self._CreateTimeEnd

    @CreateTimeEnd.setter
    def CreateTimeEnd(self, CreateTimeEnd):
        self._CreateTimeEnd = CreateTimeEnd

    @property
    def Status(self):
        """1:有效，2:无效
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ReceiverId = params.get("ReceiverId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Email = params.get("Email")
        self._CreateTimeBegin = params.get("CreateTimeBegin")
        self._CreateTimeEnd = params.get("CreateTimeEnd")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReceiverDetailsResponse(AbstractModel):
    """ListReceiverDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Data: 数据记录
        :type Data: list of ReceiverDetail
        :param _ValidCount: 有效邮件地址数
        :type ValidCount: int
        :param _InvalidCount: 无效邮件地址数
        :type InvalidCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._ValidCount = None
        self._InvalidCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        """数据记录
        :rtype: list of ReceiverDetail
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def ValidCount(self):
        """有效邮件地址数
        :rtype: int
        """
        return self._ValidCount

    @ValidCount.setter
    def ValidCount(self, ValidCount):
        self._ValidCount = ValidCount

    @property
    def InvalidCount(self):
        """无效邮件地址数
        :rtype: int
        """
        return self._InvalidCount

    @InvalidCount.setter
    def InvalidCount(self, InvalidCount):
        self._InvalidCount = InvalidCount

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ReceiverDetail()
                obj._deserialize(item)
                self._Data.append(obj)
        self._ValidCount = params.get("ValidCount")
        self._InvalidCount = params.get("InvalidCount")
        self._RequestId = params.get("RequestId")


class ListReceiversRequest(AbstractModel):
    """ListReceivers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，整型，从0开始
        :type Offset: int
        :param _Limit: 限制数目，整型，不超过100
        :type Limit: int
        :param _Status: 列表状态(1 待上传 2 上传中  3传完成)，若查询所有就不传这个字段
        :type Status: int
        :param _KeyWord: 列表名称的关键字，模糊查询
        :type KeyWord: str
        """
        self._Offset = None
        self._Limit = None
        self._Status = None
        self._KeyWord = None

    @property
    def Offset(self):
        """偏移量，整型，从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制数目，整型，不超过100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Status(self):
        """列表状态(1 待上传 2 上传中  3传完成)，若查询所有就不传这个字段
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def KeyWord(self):
        """列表名称的关键字，模糊查询
        :rtype: str
        """
        return self._KeyWord

    @KeyWord.setter
    def KeyWord(self, KeyWord):
        self._KeyWord = KeyWord


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Status = params.get("Status")
        self._KeyWord = params.get("KeyWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReceiversResponse(AbstractModel):
    """ListReceivers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Data: 数据记录
        :type Data: list of ReceiverData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        """数据记录
        :rtype: list of ReceiverData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ReceiverData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListSendTasksRequest(AbstractModel):
    """ListSendTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，整型，从0开始，0代表跳过0行
        :type Offset: int
        :param _Limit: 限制数目，整型,不超过100
        :type Limit: int
        :param _Status: 任务状态 1 待开始 5 发送中 6 今日暂停发送  7 发信异常 10 发送完成。查询所有状态，则不传这个字段
        :type Status: int
        :param _ReceiverId: 收件人列表ID
        :type ReceiverId: int
        :param _TaskType: 任务类型 1即时 2定时 3周期，查询所有类型则不传这个字段
        :type TaskType: int
        """
        self._Offset = None
        self._Limit = None
        self._Status = None
        self._ReceiverId = None
        self._TaskType = None

    @property
    def Offset(self):
        """偏移量，整型，从0开始，0代表跳过0行
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制数目，整型,不超过100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Status(self):
        """任务状态 1 待开始 5 发送中 6 今日暂停发送  7 发信异常 10 发送完成。查询所有状态，则不传这个字段
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ReceiverId(self):
        """收件人列表ID
        :rtype: int
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

    @property
    def TaskType(self):
        """任务类型 1即时 2定时 3周期，查询所有类型则不传这个字段
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Status = params.get("Status")
        self._ReceiverId = params.get("ReceiverId")
        self._TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSendTasksResponse(AbstractModel):
    """ListSendTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Data: 数据记录
        :type Data: list of SendTaskData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        """数据记录
        :rtype: list of SendTaskData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SendTaskData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ReceiverData(AbstractModel):
    """收件人列表数据类型

    """

    def __init__(self):
        r"""
        :param _ReceiverId: 收件人列表ID
        :type ReceiverId: int
        :param _ReceiversName: 收件人列表名称
        :type ReceiversName: str
        :param _Count: 收件人地址总数
        :type Count: int
        :param _Desc: 收件人列表描述
        :type Desc: str
        :param _ReceiversStatus: 列表状态(1 待上传 2 上传中 3 上传完成)
        :type ReceiversStatus: int
        :param _CreateTime: 创建时间,如:2021-09-28 16:40:35
        :type CreateTime: str
        :param _InvalidCount: 无效收件人数量
        :type InvalidCount: int
        """
        self._ReceiverId = None
        self._ReceiversName = None
        self._Count = None
        self._Desc = None
        self._ReceiversStatus = None
        self._CreateTime = None
        self._InvalidCount = None

    @property
    def ReceiverId(self):
        """收件人列表ID
        :rtype: int
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

    @property
    def ReceiversName(self):
        """收件人列表名称
        :rtype: str
        """
        return self._ReceiversName

    @ReceiversName.setter
    def ReceiversName(self, ReceiversName):
        self._ReceiversName = ReceiversName

    @property
    def Count(self):
        """收件人地址总数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Desc(self):
        """收件人列表描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ReceiversStatus(self):
        """列表状态(1 待上传 2 上传中 3 上传完成)
        :rtype: int
        """
        return self._ReceiversStatus

    @ReceiversStatus.setter
    def ReceiversStatus(self, ReceiversStatus):
        self._ReceiversStatus = ReceiversStatus

    @property
    def CreateTime(self):
        """创建时间,如:2021-09-28 16:40:35
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def InvalidCount(self):
        """无效收件人数量
        :rtype: int
        """
        return self._InvalidCount

    @InvalidCount.setter
    def InvalidCount(self, InvalidCount):
        self._InvalidCount = InvalidCount


    def _deserialize(self, params):
        self._ReceiverId = params.get("ReceiverId")
        self._ReceiversName = params.get("ReceiversName")
        self._Count = params.get("Count")
        self._Desc = params.get("Desc")
        self._ReceiversStatus = params.get("ReceiversStatus")
        self._CreateTime = params.get("CreateTime")
        self._InvalidCount = params.get("InvalidCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReceiverDetail(AbstractModel):
    """收件人列表详情

    """

    def __init__(self):
        r"""
        :param _Email: 收件人地址
        :type Email: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _TemplateData: 模板参数
        :type TemplateData: str
        :param _Reason: 无效原因
        :type Reason: str
        :param _Status: 1:有效，2:无效
        :type Status: int
        :param _EmailId: 收件人地址id
        :type EmailId: int
        """
        self._Email = None
        self._CreateTime = None
        self._TemplateData = None
        self._Reason = None
        self._Status = None
        self._EmailId = None

    @property
    def Email(self):
        """收件人地址
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TemplateData(self):
        """模板参数
        :rtype: str
        """
        return self._TemplateData

    @TemplateData.setter
    def TemplateData(self, TemplateData):
        self._TemplateData = TemplateData

    @property
    def Reason(self):
        """无效原因
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Status(self):
        """1:有效，2:无效
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EmailId(self):
        """收件人地址id
        :rtype: int
        """
        return self._EmailId

    @EmailId.setter
    def EmailId(self, EmailId):
        self._EmailId = EmailId


    def _deserialize(self, params):
        self._Email = params.get("Email")
        self._CreateTime = params.get("CreateTime")
        self._TemplateData = params.get("TemplateData")
        self._Reason = params.get("Reason")
        self._Status = params.get("Status")
        self._EmailId = params.get("EmailId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReceiverInputData(AbstractModel):
    """收件人明细输入参数，包含收件人邮箱，以及模板参数

    """

    def __init__(self):
        r"""
        :param _Email: 收件人邮箱
        :type Email: str
        :param _TemplateData: 模板中的变量参数，请使用json.dump将json对象格式化为string类型。该对象是一组键值对，每个Key代表模板中的一个变量，模板中的变量使用{{键}}表示，相应的值在发送时会被替换为{{值}}。
注意：参数值不能是html等复杂类型的数据。TemplateData (整个 JSON 结构) 总长度限制为 800 bytes。
        :type TemplateData: str
        """
        self._Email = None
        self._TemplateData = None

    @property
    def Email(self):
        """收件人邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def TemplateData(self):
        """模板中的变量参数，请使用json.dump将json对象格式化为string类型。该对象是一组键值对，每个Key代表模板中的一个变量，模板中的变量使用{{键}}表示，相应的值在发送时会被替换为{{值}}。
注意：参数值不能是html等复杂类型的数据。TemplateData (整个 JSON 结构) 总长度限制为 800 bytes。
        :rtype: str
        """
        return self._TemplateData

    @TemplateData.setter
    def TemplateData(self, TemplateData):
        self._TemplateData = TemplateData


    def _deserialize(self, params):
        self._Email = params.get("Email")
        self._TemplateData = params.get("TemplateData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendEmailRequest(AbstractModel):
    """SendEmail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FromEmailAddress: 发件人邮箱地址。不使用别名时请直接填写发件人邮箱地址，例如：noreply@mail.qcloud.com如需填写发件人别名时，请按照如下方式（注意别名与邮箱地址之间必须使用一个空格隔开）：别名+一个空格+<邮箱地址>，别名中不能带有冒号(:)。
        :type FromEmailAddress: str
        :param _Destination: 收信人邮箱地址，最多支持群发50人。注意：邮件内容会显示所有收件人地址，非群发邮件请多次调用API发送。
        :type Destination: list of str
        :param _Subject: 邮件主题
        :type Subject: str
        :param _ReplyToAddresses: 邮件的“回复”电子邮件地址。可以填写您能收到邮件的邮箱地址，可以是个人邮箱。如果不填，收件人的回复邮件将会发送失败。
        :type ReplyToAddresses: str
        :param _Cc: 抄送人邮箱地址，最多支持抄送20人。
        :type Cc: list of str
        :param _Bcc: 密送人邮箱地址，最多支持抄送20人,Bcc和Destination不能重复。
        :type Bcc: list of str
        :param _Template: 使用模板发送时，填写模板相关参数。
<dx-alert infotype="notice" title="注意"> 如您未申请过特殊配置，则该字段为必填 </dx-alert>
        :type Template: :class:`tencentcloud.ses.v20201002.models.Template`
        :param _Simple: 已废弃
<dx-alert infotype="notice" title="说明"> 仅部分历史上申请了特殊配置的客户需要使用。如您未申请过特殊配置，则不存在该字段。</dx-alert>
        :type Simple: :class:`tencentcloud.ses.v20201002.models.Simple`
        :param _Attachments: 需要发送附件时，填写附件相关参数。腾讯云接口请求最大支持 8M 的请求包，附件内容经过 Base64 预期扩大1.5倍，应该控制所有附件的总大小最大在 4M 以内，整体请求超出 8M 时接口会返回错误
        :type Attachments: list of Attachment
        :param _Unsubscribe: 退订链接选项 0: 不加入退订链接 1: 简体中文 2: 英文 3: 繁体中文 4: 西班牙语 5: 法语 6: 德语 7: 日语 8: 韩语 9: 阿拉伯语 10: 泰语
        :type Unsubscribe: str
        :param _TriggerType: 邮件触发类型 0:非触发类，默认类型，营销类邮件、非即时类邮件等选择此类型  1:触发类，验证码等即时发送类邮件，若邮件超过一定大小，系统会自动选择非触发类型通道
        :type TriggerType: int
        :param _SmtpMessageId: smtp头中的Message-Id字段
        :type SmtpMessageId: str
        :param _SmtpHeaders: smtp头中可以设置的其它字段
        :type SmtpHeaders: str
        """
        self._FromEmailAddress = None
        self._Destination = None
        self._Subject = None
        self._ReplyToAddresses = None
        self._Cc = None
        self._Bcc = None
        self._Template = None
        self._Simple = None
        self._Attachments = None
        self._Unsubscribe = None
        self._TriggerType = None
        self._SmtpMessageId = None
        self._SmtpHeaders = None

    @property
    def FromEmailAddress(self):
        """发件人邮箱地址。不使用别名时请直接填写发件人邮箱地址，例如：noreply@mail.qcloud.com如需填写发件人别名时，请按照如下方式（注意别名与邮箱地址之间必须使用一个空格隔开）：别名+一个空格+<邮箱地址>，别名中不能带有冒号(:)。
        :rtype: str
        """
        return self._FromEmailAddress

    @FromEmailAddress.setter
    def FromEmailAddress(self, FromEmailAddress):
        self._FromEmailAddress = FromEmailAddress

    @property
    def Destination(self):
        """收信人邮箱地址，最多支持群发50人。注意：邮件内容会显示所有收件人地址，非群发邮件请多次调用API发送。
        :rtype: list of str
        """
        return self._Destination

    @Destination.setter
    def Destination(self, Destination):
        self._Destination = Destination

    @property
    def Subject(self):
        """邮件主题
        :rtype: str
        """
        return self._Subject

    @Subject.setter
    def Subject(self, Subject):
        self._Subject = Subject

    @property
    def ReplyToAddresses(self):
        """邮件的“回复”电子邮件地址。可以填写您能收到邮件的邮箱地址，可以是个人邮箱。如果不填，收件人的回复邮件将会发送失败。
        :rtype: str
        """
        return self._ReplyToAddresses

    @ReplyToAddresses.setter
    def ReplyToAddresses(self, ReplyToAddresses):
        self._ReplyToAddresses = ReplyToAddresses

    @property
    def Cc(self):
        """抄送人邮箱地址，最多支持抄送20人。
        :rtype: list of str
        """
        return self._Cc

    @Cc.setter
    def Cc(self, Cc):
        self._Cc = Cc

    @property
    def Bcc(self):
        """密送人邮箱地址，最多支持抄送20人,Bcc和Destination不能重复。
        :rtype: list of str
        """
        return self._Bcc

    @Bcc.setter
    def Bcc(self, Bcc):
        self._Bcc = Bcc

    @property
    def Template(self):
        """使用模板发送时，填写模板相关参数。
<dx-alert infotype="notice" title="注意"> 如您未申请过特殊配置，则该字段为必填 </dx-alert>
        :rtype: :class:`tencentcloud.ses.v20201002.models.Template`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def Simple(self):
        """已废弃
<dx-alert infotype="notice" title="说明"> 仅部分历史上申请了特殊配置的客户需要使用。如您未申请过特殊配置，则不存在该字段。</dx-alert>
        :rtype: :class:`tencentcloud.ses.v20201002.models.Simple`
        """
        return self._Simple

    @Simple.setter
    def Simple(self, Simple):
        self._Simple = Simple

    @property
    def Attachments(self):
        """需要发送附件时，填写附件相关参数。腾讯云接口请求最大支持 8M 的请求包，附件内容经过 Base64 预期扩大1.5倍，应该控制所有附件的总大小最大在 4M 以内，整体请求超出 8M 时接口会返回错误
        :rtype: list of Attachment
        """
        return self._Attachments

    @Attachments.setter
    def Attachments(self, Attachments):
        self._Attachments = Attachments

    @property
    def Unsubscribe(self):
        """退订链接选项 0: 不加入退订链接 1: 简体中文 2: 英文 3: 繁体中文 4: 西班牙语 5: 法语 6: 德语 7: 日语 8: 韩语 9: 阿拉伯语 10: 泰语
        :rtype: str
        """
        return self._Unsubscribe

    @Unsubscribe.setter
    def Unsubscribe(self, Unsubscribe):
        self._Unsubscribe = Unsubscribe

    @property
    def TriggerType(self):
        """邮件触发类型 0:非触发类，默认类型，营销类邮件、非即时类邮件等选择此类型  1:触发类，验证码等即时发送类邮件，若邮件超过一定大小，系统会自动选择非触发类型通道
        :rtype: int
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def SmtpMessageId(self):
        """smtp头中的Message-Id字段
        :rtype: str
        """
        return self._SmtpMessageId

    @SmtpMessageId.setter
    def SmtpMessageId(self, SmtpMessageId):
        self._SmtpMessageId = SmtpMessageId

    @property
    def SmtpHeaders(self):
        """smtp头中可以设置的其它字段
        :rtype: str
        """
        return self._SmtpHeaders

    @SmtpHeaders.setter
    def SmtpHeaders(self, SmtpHeaders):
        self._SmtpHeaders = SmtpHeaders


    def _deserialize(self, params):
        self._FromEmailAddress = params.get("FromEmailAddress")
        self._Destination = params.get("Destination")
        self._Subject = params.get("Subject")
        self._ReplyToAddresses = params.get("ReplyToAddresses")
        self._Cc = params.get("Cc")
        self._Bcc = params.get("Bcc")
        if params.get("Template") is not None:
            self._Template = Template()
            self._Template._deserialize(params.get("Template"))
        if params.get("Simple") is not None:
            self._Simple = Simple()
            self._Simple._deserialize(params.get("Simple"))
        if params.get("Attachments") is not None:
            self._Attachments = []
            for item in params.get("Attachments"):
                obj = Attachment()
                obj._deserialize(item)
                self._Attachments.append(obj)
        self._Unsubscribe = params.get("Unsubscribe")
        self._TriggerType = params.get("TriggerType")
        self._SmtpMessageId = params.get("SmtpMessageId")
        self._SmtpHeaders = params.get("SmtpHeaders")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendEmailResponse(AbstractModel):
    """SendEmail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MessageId: 接受消息生成的唯一消息标识符。
        :type MessageId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MessageId = None
        self._RequestId = None

    @property
    def MessageId(self):
        """接受消息生成的唯一消息标识符。
        :rtype: str
        """
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

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
        self._MessageId = params.get("MessageId")
        self._RequestId = params.get("RequestId")


class SendEmailStatus(AbstractModel):
    """描述邮件发送状态

    """

    def __init__(self):
        r"""
        :param _MessageId: SendEmail返回的MessageId
        :type MessageId: str
        :param _ToEmailAddress: 收件人邮箱
        :type ToEmailAddress: str
        :param _FromEmailAddress: 发件人邮箱
        :type FromEmailAddress: str
        :param _SendStatus: 腾讯云处理状态
0: 处理成功
1001: 内部系统异常
1002: 内部系统异常
1003: 内部系统异常
1003: 内部系统异常
1004: 发信超时
1005: 内部系统异常
1006: 触发频率控制，短时间内对同一地址发送过多邮件
1007: 邮件地址在黑名单中
1008: 域名被收件人拒收
1009: 内部系统异常
1010: 超出了每日发送限制
1011: 无发送自定义内容权限，必须使用模板
1013: 域名被收件人取消订阅
2001: 找不到相关记录
3007: 模板ID无效或者不可用
3008: 被收信域名临时封禁
3009: 无权限使用该模板
3010: TemplateData字段格式不正确 
3014: 发件域名没有经过认证，无法发送
3020: 收件方邮箱类型在黑名单
3024: 邮箱地址格式预检查失败
3030: 退信率过高，临时限制发送
3033: 余额不足，账号欠费等
        :type SendStatus: int
        :param _DeliverStatus: 收件方处理状态
0: 请求成功被腾讯云接受，进入发送队列
1: 邮件递送成功，DeliverTime表示递送成功的时间
2: 邮件因某种原因被丢弃，DeliverMessage表示丢弃原因
3: 收件方ESP拒信，一般原因为邮箱地址不存在，或其它原因
8: 邮件被ESP因某些原因延迟递送，DeliverMessage表示延迟原因
        :type DeliverStatus: int
        :param _DeliverMessage: 收件方处理状态描述
        :type DeliverMessage: str
        :param _RequestTime: 请求到达腾讯云时间戳
        :type RequestTime: int
        :param _DeliverTime: 腾讯云执行递送时间戳
        :type DeliverTime: int
        :param _UserOpened: 用户是否打开该邮件
        :type UserOpened: bool
        :param _UserClicked: 用户是否点击该邮件中的链接
        :type UserClicked: bool
        :param _UserUnsubscribed: 用户是否取消该发送者的订阅
        :type UserUnsubscribed: bool
        :param _UserComplainted: 用户是否举报该发送者
        :type UserComplainted: bool
        """
        self._MessageId = None
        self._ToEmailAddress = None
        self._FromEmailAddress = None
        self._SendStatus = None
        self._DeliverStatus = None
        self._DeliverMessage = None
        self._RequestTime = None
        self._DeliverTime = None
        self._UserOpened = None
        self._UserClicked = None
        self._UserUnsubscribed = None
        self._UserComplainted = None

    @property
    def MessageId(self):
        """SendEmail返回的MessageId
        :rtype: str
        """
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def ToEmailAddress(self):
        """收件人邮箱
        :rtype: str
        """
        return self._ToEmailAddress

    @ToEmailAddress.setter
    def ToEmailAddress(self, ToEmailAddress):
        self._ToEmailAddress = ToEmailAddress

    @property
    def FromEmailAddress(self):
        """发件人邮箱
        :rtype: str
        """
        return self._FromEmailAddress

    @FromEmailAddress.setter
    def FromEmailAddress(self, FromEmailAddress):
        self._FromEmailAddress = FromEmailAddress

    @property
    def SendStatus(self):
        """腾讯云处理状态
0: 处理成功
1001: 内部系统异常
1002: 内部系统异常
1003: 内部系统异常
1003: 内部系统异常
1004: 发信超时
1005: 内部系统异常
1006: 触发频率控制，短时间内对同一地址发送过多邮件
1007: 邮件地址在黑名单中
1008: 域名被收件人拒收
1009: 内部系统异常
1010: 超出了每日发送限制
1011: 无发送自定义内容权限，必须使用模板
1013: 域名被收件人取消订阅
2001: 找不到相关记录
3007: 模板ID无效或者不可用
3008: 被收信域名临时封禁
3009: 无权限使用该模板
3010: TemplateData字段格式不正确 
3014: 发件域名没有经过认证，无法发送
3020: 收件方邮箱类型在黑名单
3024: 邮箱地址格式预检查失败
3030: 退信率过高，临时限制发送
3033: 余额不足，账号欠费等
        :rtype: int
        """
        return self._SendStatus

    @SendStatus.setter
    def SendStatus(self, SendStatus):
        self._SendStatus = SendStatus

    @property
    def DeliverStatus(self):
        """收件方处理状态
0: 请求成功被腾讯云接受，进入发送队列
1: 邮件递送成功，DeliverTime表示递送成功的时间
2: 邮件因某种原因被丢弃，DeliverMessage表示丢弃原因
3: 收件方ESP拒信，一般原因为邮箱地址不存在，或其它原因
8: 邮件被ESP因某些原因延迟递送，DeliverMessage表示延迟原因
        :rtype: int
        """
        return self._DeliverStatus

    @DeliverStatus.setter
    def DeliverStatus(self, DeliverStatus):
        self._DeliverStatus = DeliverStatus

    @property
    def DeliverMessage(self):
        """收件方处理状态描述
        :rtype: str
        """
        return self._DeliverMessage

    @DeliverMessage.setter
    def DeliverMessage(self, DeliverMessage):
        self._DeliverMessage = DeliverMessage

    @property
    def RequestTime(self):
        """请求到达腾讯云时间戳
        :rtype: int
        """
        return self._RequestTime

    @RequestTime.setter
    def RequestTime(self, RequestTime):
        self._RequestTime = RequestTime

    @property
    def DeliverTime(self):
        """腾讯云执行递送时间戳
        :rtype: int
        """
        return self._DeliverTime

    @DeliverTime.setter
    def DeliverTime(self, DeliverTime):
        self._DeliverTime = DeliverTime

    @property
    def UserOpened(self):
        """用户是否打开该邮件
        :rtype: bool
        """
        return self._UserOpened

    @UserOpened.setter
    def UserOpened(self, UserOpened):
        self._UserOpened = UserOpened

    @property
    def UserClicked(self):
        """用户是否点击该邮件中的链接
        :rtype: bool
        """
        return self._UserClicked

    @UserClicked.setter
    def UserClicked(self, UserClicked):
        self._UserClicked = UserClicked

    @property
    def UserUnsubscribed(self):
        """用户是否取消该发送者的订阅
        :rtype: bool
        """
        return self._UserUnsubscribed

    @UserUnsubscribed.setter
    def UserUnsubscribed(self, UserUnsubscribed):
        self._UserUnsubscribed = UserUnsubscribed

    @property
    def UserComplainted(self):
        """用户是否举报该发送者
        :rtype: bool
        """
        return self._UserComplainted

    @UserComplainted.setter
    def UserComplainted(self, UserComplainted):
        self._UserComplainted = UserComplainted


    def _deserialize(self, params):
        self._MessageId = params.get("MessageId")
        self._ToEmailAddress = params.get("ToEmailAddress")
        self._FromEmailAddress = params.get("FromEmailAddress")
        self._SendStatus = params.get("SendStatus")
        self._DeliverStatus = params.get("DeliverStatus")
        self._DeliverMessage = params.get("DeliverMessage")
        self._RequestTime = params.get("RequestTime")
        self._DeliverTime = params.get("DeliverTime")
        self._UserOpened = params.get("UserOpened")
        self._UserClicked = params.get("UserClicked")
        self._UserUnsubscribed = params.get("UserUnsubscribed")
        self._UserComplainted = params.get("UserComplainted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendTaskData(AbstractModel):
    """发送任务数据

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: int
        :param _FromEmailAddress: 发信地址
        :type FromEmailAddress: str
        :param _ReceiverId: 收件人列表Id
        :type ReceiverId: int
        :param _TaskStatus: 任务状态 1 待开始 5 发送中 6 今日暂停发送  7 发信异常 10 发送完成
        :type TaskStatus: int
        :param _TaskType: 任务类型 1 即时 2 定时 3 周期
        :type TaskType: int
        :param _RequestCount: 任务请求发信数量
        :type RequestCount: int
        :param _SendCount: 已经发送数量
        :type SendCount: int
        :param _CacheCount: 缓存数量
        :type CacheCount: int
        :param _CreateTime: 任务创建时间
        :type CreateTime: str
        :param _UpdateTime: 任务更新时间
        :type UpdateTime: str
        :param _Subject: 邮件主题
        :type Subject: str
        :param _Template: 模板和模板数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Template: :class:`tencentcloud.ses.v20201002.models.Template`
        :param _CycleParam: 周期任务参数
注意：此字段可能返回 null，表示取不到有效值。
        :type CycleParam: :class:`tencentcloud.ses.v20201002.models.CycleEmailParam`
        :param _TimedParam: 定时任务参数
注意：此字段可能返回 null，表示取不到有效值。
        :type TimedParam: :class:`tencentcloud.ses.v20201002.models.TimedEmailParam`
        :param _ErrMsg: 任务异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param _ReceiversName: 收件人列表名称
        :type ReceiversName: str
        """
        self._TaskId = None
        self._FromEmailAddress = None
        self._ReceiverId = None
        self._TaskStatus = None
        self._TaskType = None
        self._RequestCount = None
        self._SendCount = None
        self._CacheCount = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Subject = None
        self._Template = None
        self._CycleParam = None
        self._TimedParam = None
        self._ErrMsg = None
        self._ReceiversName = None

    @property
    def TaskId(self):
        """任务id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def FromEmailAddress(self):
        """发信地址
        :rtype: str
        """
        return self._FromEmailAddress

    @FromEmailAddress.setter
    def FromEmailAddress(self, FromEmailAddress):
        self._FromEmailAddress = FromEmailAddress

    @property
    def ReceiverId(self):
        """收件人列表Id
        :rtype: int
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

    @property
    def TaskStatus(self):
        """任务状态 1 待开始 5 发送中 6 今日暂停发送  7 发信异常 10 发送完成
        :rtype: int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskType(self):
        """任务类型 1 即时 2 定时 3 周期
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def RequestCount(self):
        """任务请求发信数量
        :rtype: int
        """
        return self._RequestCount

    @RequestCount.setter
    def RequestCount(self, RequestCount):
        self._RequestCount = RequestCount

    @property
    def SendCount(self):
        """已经发送数量
        :rtype: int
        """
        return self._SendCount

    @SendCount.setter
    def SendCount(self, SendCount):
        self._SendCount = SendCount

    @property
    def CacheCount(self):
        """缓存数量
        :rtype: int
        """
        return self._CacheCount

    @CacheCount.setter
    def CacheCount(self, CacheCount):
        self._CacheCount = CacheCount

    @property
    def CreateTime(self):
        """任务创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """任务更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Subject(self):
        """邮件主题
        :rtype: str
        """
        return self._Subject

    @Subject.setter
    def Subject(self, Subject):
        self._Subject = Subject

    @property
    def Template(self):
        """模板和模板数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ses.v20201002.models.Template`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def CycleParam(self):
        """周期任务参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ses.v20201002.models.CycleEmailParam`
        """
        return self._CycleParam

    @CycleParam.setter
    def CycleParam(self, CycleParam):
        self._CycleParam = CycleParam

    @property
    def TimedParam(self):
        """定时任务参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ses.v20201002.models.TimedEmailParam`
        """
        return self._TimedParam

    @TimedParam.setter
    def TimedParam(self, TimedParam):
        self._TimedParam = TimedParam

    @property
    def ErrMsg(self):
        """任务异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def ReceiversName(self):
        """收件人列表名称
        :rtype: str
        """
        return self._ReceiversName

    @ReceiversName.setter
    def ReceiversName(self, ReceiversName):
        self._ReceiversName = ReceiversName


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._FromEmailAddress = params.get("FromEmailAddress")
        self._ReceiverId = params.get("ReceiverId")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskType = params.get("TaskType")
        self._RequestCount = params.get("RequestCount")
        self._SendCount = params.get("SendCount")
        self._CacheCount = params.get("CacheCount")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Subject = params.get("Subject")
        if params.get("Template") is not None:
            self._Template = Template()
            self._Template._deserialize(params.get("Template"))
        if params.get("CycleParam") is not None:
            self._CycleParam = CycleEmailParam()
            self._CycleParam._deserialize(params.get("CycleParam"))
        if params.get("TimedParam") is not None:
            self._TimedParam = TimedEmailParam()
            self._TimedParam._deserialize(params.get("TimedParam"))
        self._ErrMsg = params.get("ErrMsg")
        self._ReceiversName = params.get("ReceiversName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Simple(AbstractModel):
    """邮件发送的内容，可以是纯文本(TEXT)，也可以是纯代码(HTML)，或者纯文本+HTML的组合(建议方式)

    """

    def __init__(self):
        r"""
        :param _Html: base64之后的Html代码。需要包含所有的代码信息，不要包含外部css，否则会导致显示格式错乱
        :type Html: str
        :param _Text: base64之后的纯文本信息，如果没有Html，邮件中会直接显示纯文本；如果有Html，它代表邮件的纯文本样式
        :type Text: str
        """
        self._Html = None
        self._Text = None

    @property
    def Html(self):
        """base64之后的Html代码。需要包含所有的代码信息，不要包含外部css，否则会导致显示格式错乱
        :rtype: str
        """
        return self._Html

    @Html.setter
    def Html(self, Html):
        self._Html = Html

    @property
    def Text(self):
        """base64之后的纯文本信息，如果没有Html，邮件中会直接显示纯文本；如果有Html，它代表邮件的纯文本样式
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Html = params.get("Html")
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Template(AbstractModel):
    """模板发送相关信息，包含模板ID，模板变量参数等信息

    """

    def __init__(self):
        r"""
        :param _TemplateID: 模板ID。如果没有模板，请先新建一个
        :type TemplateID: int
        :param _TemplateData: 模板中的变量参数，请使用json.dump将json对象格式化为string类型。该对象是一组键值对，每个Key代表模板中的一个变量，模板中的变量使用{{键}}表示，相应的值在发送时会被替换为{{值}}。
注意：参数值不能是html等复杂类型的数据。
示例：{"name":"xxx","age":"xx"}
        :type TemplateData: str
        """
        self._TemplateID = None
        self._TemplateData = None

    @property
    def TemplateID(self):
        """模板ID。如果没有模板，请先新建一个
        :rtype: int
        """
        return self._TemplateID

    @TemplateID.setter
    def TemplateID(self, TemplateID):
        self._TemplateID = TemplateID

    @property
    def TemplateData(self):
        """模板中的变量参数，请使用json.dump将json对象格式化为string类型。该对象是一组键值对，每个Key代表模板中的一个变量，模板中的变量使用{{键}}表示，相应的值在发送时会被替换为{{值}}。
注意：参数值不能是html等复杂类型的数据。
示例：{"name":"xxx","age":"xx"}
        :rtype: str
        """
        return self._TemplateData

    @TemplateData.setter
    def TemplateData(self, TemplateData):
        self._TemplateData = TemplateData


    def _deserialize(self, params):
        self._TemplateID = params.get("TemplateID")
        self._TemplateData = params.get("TemplateData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateContent(AbstractModel):
    """模板内容，TEXT和HTML必须至少存在一项，建议使用TEXT和HTML的组合

    """

    def __init__(self):
        r"""
        :param _Html: base64之后的Html代码
        :type Html: str
        :param _Text: base64之后的文本内容
        :type Text: str
        """
        self._Html = None
        self._Text = None

    @property
    def Html(self):
        """base64之后的Html代码
        :rtype: str
        """
        return self._Html

    @Html.setter
    def Html(self, Html):
        self._Html = Html

    @property
    def Text(self):
        """base64之后的文本内容
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Html = params.get("Html")
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplatesMetadata(AbstractModel):
    """模板列表结构

    """

    def __init__(self):
        r"""
        :param _CreatedTimestamp: 创建时间
        :type CreatedTimestamp: int
        :param _TemplateName: 模板名称
        :type TemplateName: str
        :param _TemplateStatus: 模板状态。1-审核中|0-已通过|2-拒绝|其它-不可用
        :type TemplateStatus: int
        :param _TemplateID: 模板ID
        :type TemplateID: int
        :param _ReviewReason: 审核原因
        :type ReviewReason: str
        """
        self._CreatedTimestamp = None
        self._TemplateName = None
        self._TemplateStatus = None
        self._TemplateID = None
        self._ReviewReason = None

    @property
    def CreatedTimestamp(self):
        """创建时间
        :rtype: int
        """
        return self._CreatedTimestamp

    @CreatedTimestamp.setter
    def CreatedTimestamp(self, CreatedTimestamp):
        self._CreatedTimestamp = CreatedTimestamp

    @property
    def TemplateName(self):
        """模板名称
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateStatus(self):
        """模板状态。1-审核中|0-已通过|2-拒绝|其它-不可用
        :rtype: int
        """
        return self._TemplateStatus

    @TemplateStatus.setter
    def TemplateStatus(self, TemplateStatus):
        self._TemplateStatus = TemplateStatus

    @property
    def TemplateID(self):
        """模板ID
        :rtype: int
        """
        return self._TemplateID

    @TemplateID.setter
    def TemplateID(self, TemplateID):
        self._TemplateID = TemplateID

    @property
    def ReviewReason(self):
        """审核原因
        :rtype: str
        """
        return self._ReviewReason

    @ReviewReason.setter
    def ReviewReason(self, ReviewReason):
        self._ReviewReason = ReviewReason


    def _deserialize(self, params):
        self._CreatedTimestamp = params.get("CreatedTimestamp")
        self._TemplateName = params.get("TemplateName")
        self._TemplateStatus = params.get("TemplateStatus")
        self._TemplateID = params.get("TemplateID")
        self._ReviewReason = params.get("ReviewReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimedEmailParam(AbstractModel):
    """创建定时发送邮件任务时，设置的定时参数，比如开始时间之类

    """

    def __init__(self):
        r"""
        :param _BeginTime: 定时发送邮件的开始时间
        :type BeginTime: str
        """
        self._BeginTime = None

    @property
    def BeginTime(self):
        """定时发送邮件的开始时间
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCustomBlackListRequest(AbstractModel):
    """UpdateCustomBlackList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 需要更改的黑名单id
        :type Id: int
        :param _Email: 修改后的邮件地址
        :type Email: str
        :param _ExpireDate: 过期时间，为空则表示永久有效
        :type ExpireDate: str
        """
        self._Id = None
        self._Email = None
        self._ExpireDate = None

    @property
    def Id(self):
        """需要更改的黑名单id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Email(self):
        """修改后的邮件地址
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def ExpireDate(self):
        """过期时间，为空则表示永久有效
        :rtype: str
        """
        return self._ExpireDate

    @ExpireDate.setter
    def ExpireDate(self, ExpireDate):
        self._ExpireDate = ExpireDate


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Email = params.get("Email")
        self._ExpireDate = params.get("ExpireDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCustomBlackListResponse(AbstractModel):
    """UpdateCustomBlackList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdateEmailIdentityRequest(AbstractModel):
    """UpdateEmailIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EmailIdentity: 请求验证的域名
        :type EmailIdentity: str
        """
        self._EmailIdentity = None

    @property
    def EmailIdentity(self):
        """请求验证的域名
        :rtype: str
        """
        return self._EmailIdentity

    @EmailIdentity.setter
    def EmailIdentity(self, EmailIdentity):
        self._EmailIdentity = EmailIdentity


    def _deserialize(self, params):
        self._EmailIdentity = params.get("EmailIdentity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEmailIdentityResponse(AbstractModel):
    """UpdateEmailIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IdentityType: 验证类型。固定值：DOMAIN
        :type IdentityType: str
        :param _VerifiedForSendingStatus: 是否已通过验证
        :type VerifiedForSendingStatus: bool
        :param _Attributes: 需要配置的DNS信息
        :type Attributes: list of DNSAttributes
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IdentityType = None
        self._VerifiedForSendingStatus = None
        self._Attributes = None
        self._RequestId = None

    @property
    def IdentityType(self):
        """验证类型。固定值：DOMAIN
        :rtype: str
        """
        return self._IdentityType

    @IdentityType.setter
    def IdentityType(self, IdentityType):
        self._IdentityType = IdentityType

    @property
    def VerifiedForSendingStatus(self):
        """是否已通过验证
        :rtype: bool
        """
        return self._VerifiedForSendingStatus

    @VerifiedForSendingStatus.setter
    def VerifiedForSendingStatus(self, VerifiedForSendingStatus):
        self._VerifiedForSendingStatus = VerifiedForSendingStatus

    @property
    def Attributes(self):
        """需要配置的DNS信息
        :rtype: list of DNSAttributes
        """
        return self._Attributes

    @Attributes.setter
    def Attributes(self, Attributes):
        self._Attributes = Attributes

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
        self._IdentityType = params.get("IdentityType")
        self._VerifiedForSendingStatus = params.get("VerifiedForSendingStatus")
        if params.get("Attributes") is not None:
            self._Attributes = []
            for item in params.get("Attributes"):
                obj = DNSAttributes()
                obj._deserialize(item)
                self._Attributes.append(obj)
        self._RequestId = params.get("RequestId")


class UpdateEmailSmtpPassWordRequest(AbstractModel):
    """UpdateEmailSmtpPassWord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Password: smtp密码，长度限制64
        :type Password: str
        :param _EmailAddress: 发信邮箱,长度限制128
        :type EmailAddress: str
        """
        self._Password = None
        self._EmailAddress = None

    @property
    def Password(self):
        """smtp密码，长度限制64
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def EmailAddress(self):
        """发信邮箱,长度限制128
        :rtype: str
        """
        return self._EmailAddress

    @EmailAddress.setter
    def EmailAddress(self, EmailAddress):
        self._EmailAddress = EmailAddress


    def _deserialize(self, params):
        self._Password = params.get("Password")
        self._EmailAddress = params.get("EmailAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEmailSmtpPassWordResponse(AbstractModel):
    """UpdateEmailSmtpPassWord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdateEmailTemplateRequest(AbstractModel):
    """UpdateEmailTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateContent: 模板内容
        :type TemplateContent: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        :param _TemplateID: 模板ID
        :type TemplateID: int
        :param _TemplateName: 模板名字
        :type TemplateName: str
        """
        self._TemplateContent = None
        self._TemplateID = None
        self._TemplateName = None

    @property
    def TemplateContent(self):
        """模板内容
        :rtype: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        """
        return self._TemplateContent

    @TemplateContent.setter
    def TemplateContent(self, TemplateContent):
        self._TemplateContent = TemplateContent

    @property
    def TemplateID(self):
        """模板ID
        :rtype: int
        """
        return self._TemplateID

    @TemplateID.setter
    def TemplateID(self, TemplateID):
        self._TemplateID = TemplateID

    @property
    def TemplateName(self):
        """模板名字
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName


    def _deserialize(self, params):
        if params.get("TemplateContent") is not None:
            self._TemplateContent = TemplateContent()
            self._TemplateContent._deserialize(params.get("TemplateContent"))
        self._TemplateID = params.get("TemplateID")
        self._TemplateName = params.get("TemplateName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEmailTemplateResponse(AbstractModel):
    """UpdateEmailTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class Volume(AbstractModel):
    """统计数据的结构体

    """

    def __init__(self):
        r"""
        :param _SendDate: 日期
注意：此字段可能返回 null，表示取不到有效值。
        :type SendDate: str
        :param _RequestCount: 邮件请求数量
        :type RequestCount: int
        :param _AcceptedCount: 腾讯云通过数量
        :type AcceptedCount: int
        :param _DeliveredCount: 送达数量
        :type DeliveredCount: int
        :param _OpenedCount: 打开邮件的用户数量，根据收件人去重
        :type OpenedCount: int
        :param _ClickedCount: 点击了邮件中的链接数量用户数量
        :type ClickedCount: int
        :param _BounceCount: 退信数量
        :type BounceCount: int
        :param _UnsubscribeCount: 取消订阅的用户数量
注意：此字段可能返回 null，表示取不到有效值。
        :type UnsubscribeCount: int
        """
        self._SendDate = None
        self._RequestCount = None
        self._AcceptedCount = None
        self._DeliveredCount = None
        self._OpenedCount = None
        self._ClickedCount = None
        self._BounceCount = None
        self._UnsubscribeCount = None

    @property
    def SendDate(self):
        """日期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SendDate

    @SendDate.setter
    def SendDate(self, SendDate):
        self._SendDate = SendDate

    @property
    def RequestCount(self):
        """邮件请求数量
        :rtype: int
        """
        return self._RequestCount

    @RequestCount.setter
    def RequestCount(self, RequestCount):
        self._RequestCount = RequestCount

    @property
    def AcceptedCount(self):
        """腾讯云通过数量
        :rtype: int
        """
        return self._AcceptedCount

    @AcceptedCount.setter
    def AcceptedCount(self, AcceptedCount):
        self._AcceptedCount = AcceptedCount

    @property
    def DeliveredCount(self):
        """送达数量
        :rtype: int
        """
        return self._DeliveredCount

    @DeliveredCount.setter
    def DeliveredCount(self, DeliveredCount):
        self._DeliveredCount = DeliveredCount

    @property
    def OpenedCount(self):
        """打开邮件的用户数量，根据收件人去重
        :rtype: int
        """
        return self._OpenedCount

    @OpenedCount.setter
    def OpenedCount(self, OpenedCount):
        self._OpenedCount = OpenedCount

    @property
    def ClickedCount(self):
        """点击了邮件中的链接数量用户数量
        :rtype: int
        """
        return self._ClickedCount

    @ClickedCount.setter
    def ClickedCount(self, ClickedCount):
        self._ClickedCount = ClickedCount

    @property
    def BounceCount(self):
        """退信数量
        :rtype: int
        """
        return self._BounceCount

    @BounceCount.setter
    def BounceCount(self, BounceCount):
        self._BounceCount = BounceCount

    @property
    def UnsubscribeCount(self):
        """取消订阅的用户数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UnsubscribeCount

    @UnsubscribeCount.setter
    def UnsubscribeCount(self, UnsubscribeCount):
        self._UnsubscribeCount = UnsubscribeCount


    def _deserialize(self, params):
        self._SendDate = params.get("SendDate")
        self._RequestCount = params.get("RequestCount")
        self._AcceptedCount = params.get("AcceptedCount")
        self._DeliveredCount = params.get("DeliveredCount")
        self._OpenedCount = params.get("OpenedCount")
        self._ClickedCount = params.get("ClickedCount")
        self._BounceCount = params.get("BounceCount")
        self._UnsubscribeCount = params.get("UnsubscribeCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        