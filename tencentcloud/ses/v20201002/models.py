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
        :param FileName: 附件名称，最大支持255个字符长度，不支持部分附件类型，详情请参考[附件类型](https://cloud.tencent.com/document/product/1288/51951)。
        :type FileName: str
        :param Content: base64之后的附件内容，您可以发送的附件大小上限为5 MB。 注意：腾讯云api目前要求请求包大小不得超过10 MB。如果您要发送多个附件，那么这些附件的总大小不能超过10 MB。
        :type Content: str
        """
        self.FileName = None
        self.Content = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchSendEmailRequest(AbstractModel):
    """BatchSendEmail请求参数结构体

    """

    def __init__(self):
        r"""
        :param FromEmailAddress: 发信邮件地址。请填写发件人邮箱地址，例如：noreply@mail.qcloud.com。如需填写发件人说明，请按照
发信人 <邮件地址> 的方式填写，例如：
腾讯云团队 <noreply@mail.qcloud.com>
        :type FromEmailAddress: str
        :param ReceiverId: 收件人列表ID
        :type ReceiverId: int
        :param Subject: 邮件主题
        :type Subject: str
        :param TaskType: 任务类型 1: 立即发送 2: 定时发送 3: 周期（频率）发送
        :type TaskType: int
        :param ReplyToAddresses: 邮件的“回复”电子邮件地址。可以填写您能收到邮件的邮箱地址，可以是个人邮箱。如果不填，收件人将会回复到腾讯云。
        :type ReplyToAddresses: str
        :param Template: 使用模板发送时，填写的模板相关参数
        :type Template: :class:`tencentcloud.ses.v20201002.models.Template`
        :param Simple: 使用API直接发送内容时，填写的邮件内容
        :type Simple: :class:`tencentcloud.ses.v20201002.models.Simple`
        :param Attachments: 需要发送附件时，填写附件相关参数。
        :type Attachments: list of Attachment
        :param CycleParam: 周期发送任务的必要参数
        :type CycleParam: :class:`tencentcloud.ses.v20201002.models.CycleEmailParam`
        :param TimedParam: 定时发送任务的必要参数
        :type TimedParam: :class:`tencentcloud.ses.v20201002.models.TimedEmailParam`
        """
        self.FromEmailAddress = None
        self.ReceiverId = None
        self.Subject = None
        self.TaskType = None
        self.ReplyToAddresses = None
        self.Template = None
        self.Simple = None
        self.Attachments = None
        self.CycleParam = None
        self.TimedParam = None


    def _deserialize(self, params):
        self.FromEmailAddress = params.get("FromEmailAddress")
        self.ReceiverId = params.get("ReceiverId")
        self.Subject = params.get("Subject")
        self.TaskType = params.get("TaskType")
        self.ReplyToAddresses = params.get("ReplyToAddresses")
        if params.get("Template") is not None:
            self.Template = Template()
            self.Template._deserialize(params.get("Template"))
        if params.get("Simple") is not None:
            self.Simple = Simple()
            self.Simple._deserialize(params.get("Simple"))
        if params.get("Attachments") is not None:
            self.Attachments = []
            for item in params.get("Attachments"):
                obj = Attachment()
                obj._deserialize(item)
                self.Attachments.append(obj)
        if params.get("CycleParam") is not None:
            self.CycleParam = CycleEmailParam()
            self.CycleParam._deserialize(params.get("CycleParam"))
        if params.get("TimedParam") is not None:
            self.TimedParam = TimedEmailParam()
            self.TimedParam._deserialize(params.get("TimedParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchSendEmailResponse(AbstractModel):
    """BatchSendEmail返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 发送任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BlackEmailAddress(AbstractModel):
    """邮箱黑名单结构，包含被拉黑的邮箱地址和被拉黑时间

    """

    def __init__(self):
        r"""
        :param BounceTime: 邮箱被拉黑时间
        :type BounceTime: str
        :param EmailAddress: 被拉黑的邮箱地址
        :type EmailAddress: str
        """
        self.BounceTime = None
        self.EmailAddress = None


    def _deserialize(self, params):
        self.BounceTime = params.get("BounceTime")
        self.EmailAddress = params.get("EmailAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmailAddressRequest(AbstractModel):
    """CreateEmailAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param EmailAddress: 您的发信地址（发信地址总数上限为10个）
        :type EmailAddress: str
        :param EmailSenderName: 发件人别名
        :type EmailSenderName: str
        """
        self.EmailAddress = None
        self.EmailSenderName = None


    def _deserialize(self, params):
        self.EmailAddress = params.get("EmailAddress")
        self.EmailSenderName = params.get("EmailSenderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmailAddressResponse(AbstractModel):
    """CreateEmailAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateEmailIdentityRequest(AbstractModel):
    """CreateEmailIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param EmailIdentity: 您的发信域名，建议使用三级以上域名。例如：mail.qcloud.com。
        :type EmailIdentity: str
        """
        self.EmailIdentity = None


    def _deserialize(self, params):
        self.EmailIdentity = params.get("EmailIdentity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmailIdentityResponse(AbstractModel):
    """CreateEmailIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param IdentityType: 验证类型。固定值：DOMAIN
        :type IdentityType: str
        :param VerifiedForSendingStatus: 是否已通过验证
        :type VerifiedForSendingStatus: bool
        :param Attributes: 需要配置的DNS信息
        :type Attributes: list of DNSAttributes
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IdentityType = None
        self.VerifiedForSendingStatus = None
        self.Attributes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IdentityType = params.get("IdentityType")
        self.VerifiedForSendingStatus = params.get("VerifiedForSendingStatus")
        if params.get("Attributes") is not None:
            self.Attributes = []
            for item in params.get("Attributes"):
                obj = DNSAttributes()
                obj._deserialize(item)
                self.Attributes.append(obj)
        self.RequestId = params.get("RequestId")


class CreateEmailTemplateRequest(AbstractModel):
    """CreateEmailTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateName: 模板名称
        :type TemplateName: str
        :param TemplateContent: 模板内容
        :type TemplateContent: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        """
        self.TemplateName = None
        self.TemplateContent = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        if params.get("TemplateContent") is not None:
            self.TemplateContent = TemplateContent()
            self.TemplateContent._deserialize(params.get("TemplateContent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmailTemplateResponse(AbstractModel):
    """CreateEmailTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CycleEmailParam(AbstractModel):
    """创建重复周期发送邮件任务的参数

    """

    def __init__(self):
        r"""
        :param BeginTime: 任务开始时间
        :type BeginTime: str
        :param IntervalTime: 任务周期 小时维度
        :type IntervalTime: int
        """
        self.BeginTime = None
        self.IntervalTime = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.IntervalTime = params.get("IntervalTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DNSAttributes(AbstractModel):
    """用于描述DNS记录的域名、记录类型、期望得到的值、目前配置的值

    """

    def __init__(self):
        r"""
        :param Type: 记录类型 CNAME | A | TXT | MX
        :type Type: str
        :param SendDomain: 域名
        :type SendDomain: str
        :param ExpectedValue: 需要配置的值
        :type ExpectedValue: str
        :param CurrentValue: 腾讯云目前检测到的值
        :type CurrentValue: str
        :param Status: 检测是否通过，创建时默认为false
        :type Status: bool
        """
        self.Type = None
        self.SendDomain = None
        self.ExpectedValue = None
        self.CurrentValue = None
        self.Status = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.SendDomain = params.get("SendDomain")
        self.ExpectedValue = params.get("ExpectedValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBlackListRequest(AbstractModel):
    """DeleteBlackList请求参数结构体

    """

    def __init__(self):
        r"""
        :param EmailAddressList: 需要清除的黑名单邮箱列表，数组长度至少为1
        :type EmailAddressList: list of str
        """
        self.EmailAddressList = None


    def _deserialize(self, params):
        self.EmailAddressList = params.get("EmailAddressList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBlackListResponse(AbstractModel):
    """DeleteBlackList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEmailAddressRequest(AbstractModel):
    """DeleteEmailAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param EmailAddress: 发信地址
        :type EmailAddress: str
        """
        self.EmailAddress = None


    def _deserialize(self, params):
        self.EmailAddress = params.get("EmailAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEmailAddressResponse(AbstractModel):
    """DeleteEmailAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEmailIdentityRequest(AbstractModel):
    """DeleteEmailIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param EmailIdentity: 发信域名
        :type EmailIdentity: str
        """
        self.EmailIdentity = None


    def _deserialize(self, params):
        self.EmailIdentity = params.get("EmailIdentity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEmailIdentityResponse(AbstractModel):
    """DeleteEmailIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEmailTemplateRequest(AbstractModel):
    """DeleteEmailTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateID: 模板ID
        :type TemplateID: int
        """
        self.TemplateID = None


    def _deserialize(self, params):
        self.TemplateID = params.get("TemplateID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEmailTemplateResponse(AbstractModel):
    """DeleteEmailTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EmailIdentity(AbstractModel):
    """发信域名验证列表结构体

    """

    def __init__(self):
        r"""
        :param IdentityName: 发信域名
        :type IdentityName: str
        :param IdentityType: 验证类型，固定为DOMAIN
        :type IdentityType: str
        :param SendingEnabled: 是否已通过验证
        :type SendingEnabled: bool
        """
        self.IdentityName = None
        self.IdentityType = None
        self.SendingEnabled = None


    def _deserialize(self, params):
        self.IdentityName = params.get("IdentityName")
        self.IdentityType = params.get("IdentityType")
        self.SendingEnabled = params.get("SendingEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmailSender(AbstractModel):
    """用于描述发件人相关信息

    """

    def __init__(self):
        r"""
        :param EmailAddress: 发信地址
        :type EmailAddress: str
        :param EmailSenderName: 发信人别名
注意：此字段可能返回 null，表示取不到有效值。
        :type EmailSenderName: str
        :param CreatedTimestamp: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTimestamp: int
        """
        self.EmailAddress = None
        self.EmailSenderName = None
        self.CreatedTimestamp = None


    def _deserialize(self, params):
        self.EmailAddress = params.get("EmailAddress")
        self.EmailSenderName = params.get("EmailSenderName")
        self.CreatedTimestamp = params.get("CreatedTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEmailIdentityRequest(AbstractModel):
    """GetEmailIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param EmailIdentity: 发信域名
        :type EmailIdentity: str
        """
        self.EmailIdentity = None


    def _deserialize(self, params):
        self.EmailIdentity = params.get("EmailIdentity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEmailIdentityResponse(AbstractModel):
    """GetEmailIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param IdentityType: 验证类型。固定值：DOMAIN
        :type IdentityType: str
        :param VerifiedForSendingStatus: 是否已通过验证
        :type VerifiedForSendingStatus: bool
        :param Attributes: DNS配置详情
        :type Attributes: list of DNSAttributes
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IdentityType = None
        self.VerifiedForSendingStatus = None
        self.Attributes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IdentityType = params.get("IdentityType")
        self.VerifiedForSendingStatus = params.get("VerifiedForSendingStatus")
        if params.get("Attributes") is not None:
            self.Attributes = []
            for item in params.get("Attributes"):
                obj = DNSAttributes()
                obj._deserialize(item)
                self.Attributes.append(obj)
        self.RequestId = params.get("RequestId")


class GetEmailTemplateRequest(AbstractModel):
    """GetEmailTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateID: 模板ID
        :type TemplateID: int
        """
        self.TemplateID = None


    def _deserialize(self, params):
        self.TemplateID = params.get("TemplateID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEmailTemplateResponse(AbstractModel):
    """GetEmailTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateContent: 模板内容数据
        :type TemplateContent: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TemplateContent = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TemplateContent") is not None:
            self.TemplateContent = TemplateContent()
            self.TemplateContent._deserialize(params.get("TemplateContent"))
        self.RequestId = params.get("RequestId")


class GetSendEmailStatusRequest(AbstractModel):
    """GetSendEmailStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param RequestDate: 发送的日期，必填。仅支持查询某个日期，不支持范围查询。
        :type RequestDate: str
        :param Offset: 偏移量。默认为0
        :type Offset: int
        :param Limit: 拉取最大条数，最多 100。
        :type Limit: int
        :param MessageId: SendMail接口返回的MessageId字段。
        :type MessageId: str
        :param ToEmailAddress: 收件人邮箱。
        :type ToEmailAddress: str
        """
        self.RequestDate = None
        self.Offset = None
        self.Limit = None
        self.MessageId = None
        self.ToEmailAddress = None


    def _deserialize(self, params):
        self.RequestDate = params.get("RequestDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.MessageId = params.get("MessageId")
        self.ToEmailAddress = params.get("ToEmailAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSendEmailStatusResponse(AbstractModel):
    """GetSendEmailStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param EmailStatusList: 邮件发送状态列表
        :type EmailStatusList: list of SendEmailStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EmailStatusList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EmailStatusList") is not None:
            self.EmailStatusList = []
            for item in params.get("EmailStatusList"):
                obj = SendEmailStatus()
                obj._deserialize(item)
                self.EmailStatusList.append(obj)
        self.RequestId = params.get("RequestId")


class GetStatisticsReportRequest(AbstractModel):
    """GetStatisticsReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartDate: 开始日期
        :type StartDate: str
        :param EndDate: 结束日期
        :type EndDate: str
        :param Domain: 发信域名
        :type Domain: str
        :param ReceivingMailboxType: 收件方邮箱类型，例如gmail.com
        :type ReceivingMailboxType: str
        """
        self.StartDate = None
        self.EndDate = None
        self.Domain = None
        self.ReceivingMailboxType = None


    def _deserialize(self, params):
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Domain = params.get("Domain")
        self.ReceivingMailboxType = params.get("ReceivingMailboxType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetStatisticsReportResponse(AbstractModel):
    """GetStatisticsReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param DailyVolumes: 发信统计报告，按天
        :type DailyVolumes: list of Volume
        :param OverallVolume: 发信统计报告，总览
        :type OverallVolume: :class:`tencentcloud.ses.v20201002.models.Volume`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DailyVolumes = None
        self.OverallVolume = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DailyVolumes") is not None:
            self.DailyVolumes = []
            for item in params.get("DailyVolumes"):
                obj = Volume()
                obj._deserialize(item)
                self.DailyVolumes.append(obj)
        if params.get("OverallVolume") is not None:
            self.OverallVolume = Volume()
            self.OverallVolume._deserialize(params.get("OverallVolume"))
        self.RequestId = params.get("RequestId")


class ListBlackEmailAddressRequest(AbstractModel):
    """ListBlackEmailAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartDate: 开始日期，格式为YYYY-MM-DD
        :type StartDate: str
        :param EndDate: 结束日期，格式为YYYY-MM-DD
        :type EndDate: str
        :param Limit: 规范，配合Offset使用
        :type Limit: int
        :param Offset: 规范，配合Limit使用，Limit最大取值为100
        :type Offset: int
        :param EmailAddress: 可以指定邮箱进行查询
        :type EmailAddress: str
        :param TaskID: 可以指定任务ID进行查询
        :type TaskID: str
        """
        self.StartDate = None
        self.EndDate = None
        self.Limit = None
        self.Offset = None
        self.EmailAddress = None
        self.TaskID = None


    def _deserialize(self, params):
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.EmailAddress = params.get("EmailAddress")
        self.TaskID = params.get("TaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListBlackEmailAddressResponse(AbstractModel):
    """ListBlackEmailAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param BlackList: 黑名单列表
        :type BlackList: list of BlackEmailAddress
        :param TotalCount: 黑名单总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BlackList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BlackList") is not None:
            self.BlackList = []
            for item in params.get("BlackList"):
                obj = BlackEmailAddress()
                obj._deserialize(item)
                self.BlackList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListEmailAddressRequest(AbstractModel):
    """ListEmailAddress请求参数结构体

    """


class ListEmailAddressResponse(AbstractModel):
    """ListEmailAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param EmailSenders: 发信地址列表详情
注意：此字段可能返回 null，表示取不到有效值。
        :type EmailSenders: list of EmailSender
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EmailSenders = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EmailSenders") is not None:
            self.EmailSenders = []
            for item in params.get("EmailSenders"):
                obj = EmailSender()
                obj._deserialize(item)
                self.EmailSenders.append(obj)
        self.RequestId = params.get("RequestId")


class ListEmailIdentitiesRequest(AbstractModel):
    """ListEmailIdentities请求参数结构体

    """


class ListEmailIdentitiesResponse(AbstractModel):
    """ListEmailIdentities返回参数结构体

    """

    def __init__(self):
        r"""
        :param EmailIdentities: 发信域名列表
        :type EmailIdentities: list of EmailIdentity
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EmailIdentities = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EmailIdentities") is not None:
            self.EmailIdentities = []
            for item in params.get("EmailIdentities"):
                obj = EmailIdentity()
                obj._deserialize(item)
                self.EmailIdentities.append(obj)
        self.RequestId = params.get("RequestId")


class ListEmailTemplatesRequest(AbstractModel):
    """ListEmailTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 获取模版数据量，用于分页
        :type Limit: int
        :param Offset: 获取模版偏移值，用于分页
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEmailTemplatesResponse(AbstractModel):
    """ListEmailTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TemplatesMetadata: 邮件模板列表
        :type TemplatesMetadata: list of TemplatesMetadata
        :param TotalCount: 模版总数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TemplatesMetadata = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TemplatesMetadata") is not None:
            self.TemplatesMetadata = []
            for item in params.get("TemplatesMetadata"):
                obj = TemplatesMetadata()
                obj._deserialize(item)
                self.TemplatesMetadata.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class SendEmailRequest(AbstractModel):
    """SendEmail请求参数结构体

    """

    def __init__(self):
        r"""
        :param FromEmailAddress: 发信邮件地址。请填写发件人邮箱地址，例如：noreply@mail.qcloud.com
如需填写发件人说明，请按照如下方式： 
别名 <邮箱地址>
        :type FromEmailAddress: str
        :param Destination: 收信人邮箱地址，最多支持群发50人。注意：邮件内容会显示所有收件人地址，非群发邮件请多次调用API发送。
        :type Destination: list of str
        :param Subject: 邮件主题
        :type Subject: str
        :param ReplyToAddresses: 邮件的“回复”电子邮件地址。可以填写您能收到邮件的邮箱地址，可以是个人邮箱。如果不填，收件人将会回复到腾讯云。
        :type ReplyToAddresses: str
        :param Template: 使用模板发送时，填写的模板相关参数
        :type Template: :class:`tencentcloud.ses.v20201002.models.Template`
        :param Simple: 使用API直接发送内容时，填写的邮件内容
        :type Simple: :class:`tencentcloud.ses.v20201002.models.Simple`
        :param Attachments: 需要发送附件时，填写附件相关参数。
        :type Attachments: list of Attachment
        :param Unsubscribe: 是否加入退订链接
        :type Unsubscribe: str
        """
        self.FromEmailAddress = None
        self.Destination = None
        self.Subject = None
        self.ReplyToAddresses = None
        self.Template = None
        self.Simple = None
        self.Attachments = None
        self.Unsubscribe = None


    def _deserialize(self, params):
        self.FromEmailAddress = params.get("FromEmailAddress")
        self.Destination = params.get("Destination")
        self.Subject = params.get("Subject")
        self.ReplyToAddresses = params.get("ReplyToAddresses")
        if params.get("Template") is not None:
            self.Template = Template()
            self.Template._deserialize(params.get("Template"))
        if params.get("Simple") is not None:
            self.Simple = Simple()
            self.Simple._deserialize(params.get("Simple"))
        if params.get("Attachments") is not None:
            self.Attachments = []
            for item in params.get("Attachments"):
                obj = Attachment()
                obj._deserialize(item)
                self.Attachments.append(obj)
        self.Unsubscribe = params.get("Unsubscribe")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendEmailResponse(AbstractModel):
    """SendEmail返回参数结构体

    """

    def __init__(self):
        r"""
        :param MessageId: 接受消息生成的唯一消息标识符。
        :type MessageId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MessageId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MessageId = params.get("MessageId")
        self.RequestId = params.get("RequestId")


class SendEmailStatus(AbstractModel):
    """描述邮件发送状态

    """

    def __init__(self):
        r"""
        :param MessageId: SendEmail返回的MessageId
        :type MessageId: str
        :param ToEmailAddress: 收件人邮箱
        :type ToEmailAddress: str
        :param FromEmailAddress: 发件人邮箱
        :type FromEmailAddress: str
        :param SendStatus: 腾讯云处理状态
0: 处理成功
1001: 内部系统异常
1002: 内部系统异常
1003: 内部系统异常
1003: 内部系统异常
1004: 发信超时
1005: 内部系统异常
1006: 触发频率控制，短时间内对同一地址发送过多邮件
1007: 邮件地址在黑名单中
1009: 内部系统异常
1010: 超出了每日发送限制
1011: 无发送自定义内容权限，必须使用模板
2001: 找不到相关记录
3007: 模板ID无效或者不可用
3008: 模板状态异常
3009: 无权限使用该模板
3010: TemplateData字段格式不正确 
3014: 发件域名没有经过认证，无法发送
3020: 收件方邮箱类型在黑名单
3024: 邮箱地址格式预检查失败
3030: 退信率过高，临时限制发送
3033: 余额不足，账号欠费等
        :type SendStatus: int
        :param DeliverStatus: 收件方处理状态
0: 请求成功被腾讯云接受，进入发送队列
1: 邮件递送成功，DeliverTime表示递送成功的时间
2: 邮件因某种原因被丢弃，DeliverMessage表示丢弃原因
3: 收件方ESP拒信，一般原因为邮箱地址不存在，或其它原因
8: 邮件被ESP因某些原因延迟递送，DeliverMessage表示延迟原因
        :type DeliverStatus: int
        :param DeliverMessage: 收件方处理状态描述
        :type DeliverMessage: str
        :param RequestTime: 请求到达腾讯云时间戳
        :type RequestTime: int
        :param DeliverTime: 腾讯云执行递送时间戳
        :type DeliverTime: int
        :param UserOpened: 用户是否打开该邮件
        :type UserOpened: bool
        :param UserClicked: 用户是否点击该邮件中的链接
        :type UserClicked: bool
        :param UserUnsubscribed: 用户是否取消该发送者的订阅
        :type UserUnsubscribed: bool
        :param UserComplainted: 用户是否举报该发送者
        :type UserComplainted: bool
        """
        self.MessageId = None
        self.ToEmailAddress = None
        self.FromEmailAddress = None
        self.SendStatus = None
        self.DeliverStatus = None
        self.DeliverMessage = None
        self.RequestTime = None
        self.DeliverTime = None
        self.UserOpened = None
        self.UserClicked = None
        self.UserUnsubscribed = None
        self.UserComplainted = None


    def _deserialize(self, params):
        self.MessageId = params.get("MessageId")
        self.ToEmailAddress = params.get("ToEmailAddress")
        self.FromEmailAddress = params.get("FromEmailAddress")
        self.SendStatus = params.get("SendStatus")
        self.DeliverStatus = params.get("DeliverStatus")
        self.DeliverMessage = params.get("DeliverMessage")
        self.RequestTime = params.get("RequestTime")
        self.DeliverTime = params.get("DeliverTime")
        self.UserOpened = params.get("UserOpened")
        self.UserClicked = params.get("UserClicked")
        self.UserUnsubscribed = params.get("UserUnsubscribed")
        self.UserComplainted = params.get("UserComplainted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Simple(AbstractModel):
    """邮件发送的内容，可以是纯文本(TEXT)，也可以是纯代码(HTML)，或者纯文本+HTML的组合(建议方式)

    """

    def __init__(self):
        r"""
        :param Html: base64之后的Html代码。需要包含所有的代码信息，不要包含外部css，否则会导致显示格式错乱
        :type Html: str
        :param Text: base64之后的纯文本信息，如果没有Html，邮件中会直接显示纯文本；如果有Html，它代表邮件的纯文本样式
        :type Text: str
        """
        self.Html = None
        self.Text = None


    def _deserialize(self, params):
        self.Html = params.get("Html")
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Template(AbstractModel):
    """模板发送相关信息，包含模板ID，模板变量参数等信息

    """

    def __init__(self):
        r"""
        :param TemplateID: 模板ID。如果没有模板，请先新建一个
        :type TemplateID: int
        :param TemplateData: 模板中的变量参数，请使用json.dump将json对象格式化为string类型。该对象是一组键值对，每个Key代表模板中的一个变量，模板中的变量使用{{键}}表示，相应的值在发送时会被替换为{{值}}。
注意：参数值不能是html等复杂类型的数据。
示例：{"name":"xxx","age":"xx"}
        :type TemplateData: str
        """
        self.TemplateID = None
        self.TemplateData = None


    def _deserialize(self, params):
        self.TemplateID = params.get("TemplateID")
        self.TemplateData = params.get("TemplateData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateContent(AbstractModel):
    """模板内容，TEXT和HTML必须至少存在一项，建议使用TEXT和HTML的组合

    """

    def __init__(self):
        r"""
        :param Html: base64之后的Html代码
        :type Html: str
        :param Text: base64之后的文本内容
        :type Text: str
        """
        self.Html = None
        self.Text = None


    def _deserialize(self, params):
        self.Html = params.get("Html")
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplatesMetadata(AbstractModel):
    """模板列表结构

    """

    def __init__(self):
        r"""
        :param CreatedTimestamp: 创建时间
        :type CreatedTimestamp: int
        :param TemplateName: 模板名称
        :type TemplateName: str
        :param TemplateStatus: 模板状态。1-审核中|0-已通过|2-拒绝|其它-不可用
        :type TemplateStatus: int
        :param TemplateID: 模板ID
        :type TemplateID: int
        :param ReviewReason: 审核原因
        :type ReviewReason: str
        """
        self.CreatedTimestamp = None
        self.TemplateName = None
        self.TemplateStatus = None
        self.TemplateID = None
        self.ReviewReason = None


    def _deserialize(self, params):
        self.CreatedTimestamp = params.get("CreatedTimestamp")
        self.TemplateName = params.get("TemplateName")
        self.TemplateStatus = params.get("TemplateStatus")
        self.TemplateID = params.get("TemplateID")
        self.ReviewReason = params.get("ReviewReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimedEmailParam(AbstractModel):
    """创建定时发送邮件任务时，设置的定时参数，比如开始时间之类

    """

    def __init__(self):
        r"""
        :param BeginTime: 定时发送邮件的开始时间
        :type BeginTime: str
        """
        self.BeginTime = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEmailIdentityRequest(AbstractModel):
    """UpdateEmailIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param EmailIdentity: 请求验证的域名
        :type EmailIdentity: str
        """
        self.EmailIdentity = None


    def _deserialize(self, params):
        self.EmailIdentity = params.get("EmailIdentity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEmailIdentityResponse(AbstractModel):
    """UpdateEmailIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param IdentityType: 验证类型。固定值：DOMAIN
        :type IdentityType: str
        :param VerifiedForSendingStatus: 是否已通过验证
        :type VerifiedForSendingStatus: bool
        :param Attributes: 需要配置的DNS信息
        :type Attributes: list of DNSAttributes
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IdentityType = None
        self.VerifiedForSendingStatus = None
        self.Attributes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IdentityType = params.get("IdentityType")
        self.VerifiedForSendingStatus = params.get("VerifiedForSendingStatus")
        if params.get("Attributes") is not None:
            self.Attributes = []
            for item in params.get("Attributes"):
                obj = DNSAttributes()
                obj._deserialize(item)
                self.Attributes.append(obj)
        self.RequestId = params.get("RequestId")


class UpdateEmailTemplateRequest(AbstractModel):
    """UpdateEmailTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateContent: 模板内容
        :type TemplateContent: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        :param TemplateID: 模板ID
        :type TemplateID: int
        :param TemplateName: 模版名字
        :type TemplateName: str
        """
        self.TemplateContent = None
        self.TemplateID = None
        self.TemplateName = None


    def _deserialize(self, params):
        if params.get("TemplateContent") is not None:
            self.TemplateContent = TemplateContent()
            self.TemplateContent._deserialize(params.get("TemplateContent"))
        self.TemplateID = params.get("TemplateID")
        self.TemplateName = params.get("TemplateName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEmailTemplateResponse(AbstractModel):
    """UpdateEmailTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Volume(AbstractModel):
    """统计数据的结构体

    """

    def __init__(self):
        r"""
        :param SendDate: 日期
注意：此字段可能返回 null，表示取不到有效值。
        :type SendDate: str
        :param RequestCount: 邮件请求数量
        :type RequestCount: int
        :param AcceptedCount: 腾讯云通过数量
        :type AcceptedCount: int
        :param DeliveredCount: 送达数量
        :type DeliveredCount: int
        :param OpenedCount: 打开邮件的用户数量，根据收件人去重
        :type OpenedCount: int
        :param ClickedCount: 点击了邮件中的链接数量用户数量
        :type ClickedCount: int
        :param BounceCount: 退信数量
        :type BounceCount: int
        :param UnsubscribeCount: 取消订阅的用户数量
注意：此字段可能返回 null，表示取不到有效值。
        :type UnsubscribeCount: int
        """
        self.SendDate = None
        self.RequestCount = None
        self.AcceptedCount = None
        self.DeliveredCount = None
        self.OpenedCount = None
        self.ClickedCount = None
        self.BounceCount = None
        self.UnsubscribeCount = None


    def _deserialize(self, params):
        self.SendDate = params.get("SendDate")
        self.RequestCount = params.get("RequestCount")
        self.AcceptedCount = params.get("AcceptedCount")
        self.DeliveredCount = params.get("DeliveredCount")
        self.OpenedCount = params.get("OpenedCount")
        self.ClickedCount = params.get("ClickedCount")
        self.BounceCount = params.get("BounceCount")
        self.UnsubscribeCount = params.get("UnsubscribeCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        