# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class CallbackStatusStatistics(AbstractModel):
    """回执数据统计响应包体

    """

    def __init__(self):
        """
        :param CallbackCount: 短信回执量统计。
        :type CallbackCount: int
        :param RequestSuccessCount: 短信提交成功量统计。
        :type RequestSuccessCount: int
        :param CallbackFailCount: 短信回执失败量统计。
        :type CallbackFailCount: int
        :param CallbackSuccessCount: 短信回执成功量统计。
        :type CallbackSuccessCount: int
        :param InternalErrorCount: 运营商内部错误统计。
        :type InternalErrorCount: int
        :param InvalidNumberCount: 号码无效或空号统计。
        :type InvalidNumberCount: int
        :param ShutdownErrorCount: 停机、关机等错误统计。
        :type ShutdownErrorCount: int
        :param BlackListCount: 号码拉入黑名单统计。
        :type BlackListCount: int
        :param FrequencyLimitCount: 运营商频率限制统计。
        :type FrequencyLimitCount: int
        """
        self.CallbackCount = None
        self.RequestSuccessCount = None
        self.CallbackFailCount = None
        self.CallbackSuccessCount = None
        self.InternalErrorCount = None
        self.InvalidNumberCount = None
        self.ShutdownErrorCount = None
        self.BlackListCount = None
        self.FrequencyLimitCount = None


    def _deserialize(self, params):
        self.CallbackCount = params.get("CallbackCount")
        self.RequestSuccessCount = params.get("RequestSuccessCount")
        self.CallbackFailCount = params.get("CallbackFailCount")
        self.CallbackSuccessCount = params.get("CallbackSuccessCount")
        self.InternalErrorCount = params.get("InternalErrorCount")
        self.InvalidNumberCount = params.get("InvalidNumberCount")
        self.ShutdownErrorCount = params.get("ShutdownErrorCount")
        self.BlackListCount = params.get("BlackListCount")
        self.FrequencyLimitCount = params.get("FrequencyLimitCount")


class CallbackStatusStatisticsRequest(AbstractModel):
    """CallbackStatusStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param StartDateTime: 开始时间，yyyymmddhh 需要拉取的起始时间，精确到小时。
        :type StartDateTime: int
        :param EndDataTime: 结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时。
注：EndDataTime 必须大于 StartDateTime。
        :type EndDataTime: int
        :param SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid，示例如1400006666。
        :type SmsSdkAppid: str
        :param Limit: 最大上限。
注：目前固定设置为0。
        :type Limit: int
        :param Offset: 偏移量。
注：目前固定设置为0。
        :type Offset: int
        """
        self.StartDateTime = None
        self.EndDataTime = None
        self.SmsSdkAppid = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartDateTime = params.get("StartDateTime")
        self.EndDataTime = params.get("EndDataTime")
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class CallbackStatusStatisticsResponse(AbstractModel):
    """CallbackStatusStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param CallbackStatusStatistics: 回执数据统计响应包体。
        :type CallbackStatusStatistics: :class:`tencentcloud.sms.v20190711.models.CallbackStatusStatistics`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CallbackStatusStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CallbackStatusStatistics") is not None:
            self.CallbackStatusStatistics = CallbackStatusStatistics()
            self.CallbackStatusStatistics._deserialize(params.get("CallbackStatusStatistics"))
        self.RequestId = params.get("RequestId")


class PullSmsReplyStatus(AbstractModel):
    """短信回复状态

    """

    def __init__(self):
        """
        :param ExtendCode: 短信码号扩展号，默认未开通，如需开通请联系 [sms helper](https://cloud.tencent.com/document/product/382/3773)。
        :type ExtendCode: str
        :param NationCode: 国家（或地区）码。
        :type NationCode: str
        :param PhoneNumber: 手机号码,e.164标准，+[国家或地区码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :type PhoneNumber: str
        :param Sign: 短信签名。
        :type Sign: str
        :param ReplyContent: 用户回复的内容。
        :type ReplyContent: str
        :param ReplyTime: 回复时间（例如：2019-10-08 17:18:37）。
        :type ReplyTime: str
        :param ReplyUnixTime: 回复时间，UNIX 时间戳（单位：秒）。
        :type ReplyUnixTime: int
        """
        self.ExtendCode = None
        self.NationCode = None
        self.PhoneNumber = None
        self.Sign = None
        self.ReplyContent = None
        self.ReplyTime = None
        self.ReplyUnixTime = None


    def _deserialize(self, params):
        self.ExtendCode = params.get("ExtendCode")
        self.NationCode = params.get("NationCode")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Sign = params.get("Sign")
        self.ReplyContent = params.get("ReplyContent")
        self.ReplyTime = params.get("ReplyTime")
        self.ReplyUnixTime = params.get("ReplyUnixTime")


class PullSmsReplyStatusByPhoneNumberRequest(AbstractModel):
    """PullSmsReplyStatusByPhoneNumber请求参数结构体

    """

    def __init__(self):
        """
        :param SendDateTime: 拉取起始时间，UNIX 时间戳（时间：秒）。
        :type SendDateTime: int
        :param Offset: 偏移量。
注：目前固定设置为0。
        :type Offset: int
        :param Limit: 拉取最大条数，最多 100。
        :type Limit: int
        :param PhoneNumber: 下发目的手机号码，依据 e.164 标准为：+[国家（或地区）码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :type PhoneNumber: str
        :param SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid，示例如1400006666。
        :type SmsSdkAppid: str
        """
        self.SendDateTime = None
        self.Offset = None
        self.Limit = None
        self.PhoneNumber = None
        self.SmsSdkAppid = None


    def _deserialize(self, params):
        self.SendDateTime = params.get("SendDateTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PhoneNumber = params.get("PhoneNumber")
        self.SmsSdkAppid = params.get("SmsSdkAppid")


class PullSmsReplyStatusByPhoneNumberResponse(AbstractModel):
    """PullSmsReplyStatusByPhoneNumber返回参数结构体

    """

    def __init__(self):
        """
        :param PullSmsReplyStatusSet: 回复状态响应集合。
        :type PullSmsReplyStatusSet: list of PullSmsReplyStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PullSmsReplyStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PullSmsReplyStatusSet") is not None:
            self.PullSmsReplyStatusSet = []
            for item in params.get("PullSmsReplyStatusSet"):
                obj = PullSmsReplyStatus()
                obj._deserialize(item)
                self.PullSmsReplyStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class PullSmsReplyStatusRequest(AbstractModel):
    """PullSmsReplyStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 拉取最大条数，最多100条。
        :type Limit: int
        :param SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid,示例如1400006666。
        :type SmsSdkAppid: str
        """
        self.Limit = None
        self.SmsSdkAppid = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.SmsSdkAppid = params.get("SmsSdkAppid")


class PullSmsReplyStatusResponse(AbstractModel):
    """PullSmsReplyStatus返回参数结构体

    """

    def __init__(self):
        """
        :param PullSmsReplyStatusSet: 回复状态响应集合。
        :type PullSmsReplyStatusSet: list of PullSmsReplyStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PullSmsReplyStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PullSmsReplyStatusSet") is not None:
            self.PullSmsReplyStatusSet = []
            for item in params.get("PullSmsReplyStatusSet"):
                obj = PullSmsReplyStatus()
                obj._deserialize(item)
                self.PullSmsReplyStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class PullSmsSendStatus(AbstractModel):
    """短信的下发状态详细信息

    """

    def __init__(self):
        """
        :param UserReceiveTime: 用户实际接收到短信的时间。
        :type UserReceiveTime: str
        :param UserReceiveUnixTime: 用户实际接收到短信的时间，UNIX 时间戳（单位：秒）。
        :type UserReceiveUnixTime: int
        :param NationCode: 国家（或地区）码。
        :type NationCode: str
        :param PurePhoneNumber: 手机号码,e.164标准，+[国家或地区码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :type PurePhoneNumber: str
        :param PhoneNumber: 手机号码，普通格式，示例如：13711112222。
        :type PhoneNumber: str
        :param SerialNo: 本次发送标识 ID。
        :type SerialNo: str
        :param ReportStatus: 实际是否收到短信接收状态，SUCCESS（成功）、FAIL（失败）。
        :type ReportStatus: str
        :param Description: 用户接收短信状态描述。
        :type Description: str
        """
        self.UserReceiveTime = None
        self.UserReceiveUnixTime = None
        self.NationCode = None
        self.PurePhoneNumber = None
        self.PhoneNumber = None
        self.SerialNo = None
        self.ReportStatus = None
        self.Description = None


    def _deserialize(self, params):
        self.UserReceiveTime = params.get("UserReceiveTime")
        self.UserReceiveUnixTime = params.get("UserReceiveUnixTime")
        self.NationCode = params.get("NationCode")
        self.PurePhoneNumber = params.get("PurePhoneNumber")
        self.PhoneNumber = params.get("PhoneNumber")
        self.SerialNo = params.get("SerialNo")
        self.ReportStatus = params.get("ReportStatus")
        self.Description = params.get("Description")


class PullSmsSendStatusByPhoneNumberRequest(AbstractModel):
    """PullSmsSendStatusByPhoneNumber请求参数结构体

    """

    def __init__(self):
        """
        :param SendDateTime: 拉取起始时间，UNIX 时间戳（时间：秒）。
        :type SendDateTime: int
        :param Offset: 偏移量。
注：目前固定设置为0。
        :type Offset: int
        :param Limit: 拉取最大条数，最多 100。
        :type Limit: int
        :param PhoneNumber: 下发目的手机号码，依据 e.164 标准为：+[国家（或地区）码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :type PhoneNumber: str
        :param SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid，示例如1400006666。
        :type SmsSdkAppid: str
        """
        self.SendDateTime = None
        self.Offset = None
        self.Limit = None
        self.PhoneNumber = None
        self.SmsSdkAppid = None


    def _deserialize(self, params):
        self.SendDateTime = params.get("SendDateTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PhoneNumber = params.get("PhoneNumber")
        self.SmsSdkAppid = params.get("SmsSdkAppid")


class PullSmsSendStatusByPhoneNumberResponse(AbstractModel):
    """PullSmsSendStatusByPhoneNumber返回参数结构体

    """

    def __init__(self):
        """
        :param PullSmsSendStatusSet: 下发状态响应集合。
        :type PullSmsSendStatusSet: list of PullSmsSendStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PullSmsSendStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PullSmsSendStatusSet") is not None:
            self.PullSmsSendStatusSet = []
            for item in params.get("PullSmsSendStatusSet"):
                obj = PullSmsSendStatus()
                obj._deserialize(item)
                self.PullSmsSendStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class PullSmsSendStatusRequest(AbstractModel):
    """PullSmsSendStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 拉取最大条数，最多100条。
        :type Limit: int
        :param SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid，示例如1400006666。
        :type SmsSdkAppid: str
        """
        self.Limit = None
        self.SmsSdkAppid = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.SmsSdkAppid = params.get("SmsSdkAppid")


class PullSmsSendStatusResponse(AbstractModel):
    """PullSmsSendStatus返回参数结构体

    """

    def __init__(self):
        """
        :param PullSmsSendStatusSet: 下发状态响应集合。
        :type PullSmsSendStatusSet: list of PullSmsSendStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PullSmsSendStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PullSmsSendStatusSet") is not None:
            self.PullSmsSendStatusSet = []
            for item in params.get("PullSmsSendStatusSet"):
                obj = PullSmsSendStatus()
                obj._deserialize(item)
                self.PullSmsSendStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class SendSmsRequest(AbstractModel):
    """SendSms请求参数结构体

    """

    def __init__(self):
        """
        :param PhoneNumberSet: 下发手机号码，采用 e.164 标准，+[国家或地区码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号，最多不要超过200个手机号。
        :type PhoneNumberSet: list of str
        :param TemplateID: 模板 ID，必须填写已审核通过的模板 ID。模板ID可登录 [短信控制台](https://console.cloud.tencent.com/sms/smslist) 查看。
        :type TemplateID: str
        :param SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/sms/smslist)  添加应用后生成的实际SdkAppid，示例如1400006666。
        :type SmsSdkAppid: str
        :param Sign: 短信签名内容，使用 UTF-8 编码，必须填写已审核通过的签名，签名信息可登录 [短信控制台](https://console.cloud.tencent.com/sms/smslist)  查看。
        :type Sign: str
        :param TemplateParamSet: 模板参数，若无模板参数，则设置为空。
        :type TemplateParamSet: list of str
        :param ExtendCode: 短信码号扩展号，默认未开通，如需开通请联系 [sms helper](https://cloud.tencent.com/document/product/382/3773)。
        :type ExtendCode: str
        :param SessionContext: 用户的 session 内容，可以携带用户侧 ID 等上下文信息，server 会原样返回。
        :type SessionContext: str
        :param SenderId: 国际/港澳台短信 senderid，国内短信填空，默认未开通，如需开通请联系 [sms helper](https://cloud.tencent.com/document/product/382/3773)。
        :type SenderId: str
        """
        self.PhoneNumberSet = None
        self.TemplateID = None
        self.SmsSdkAppid = None
        self.Sign = None
        self.TemplateParamSet = None
        self.ExtendCode = None
        self.SessionContext = None
        self.SenderId = None


    def _deserialize(self, params):
        self.PhoneNumberSet = params.get("PhoneNumberSet")
        self.TemplateID = params.get("TemplateID")
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.Sign = params.get("Sign")
        self.TemplateParamSet = params.get("TemplateParamSet")
        self.ExtendCode = params.get("ExtendCode")
        self.SessionContext = params.get("SessionContext")
        self.SenderId = params.get("SenderId")


class SendSmsResponse(AbstractModel):
    """SendSms返回参数结构体

    """

    def __init__(self):
        """
        :param SendStatusSet: 短信发送状态。
        :type SendStatusSet: list of SendStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SendStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SendStatusSet") is not None:
            self.SendStatusSet = []
            for item in params.get("SendStatusSet"):
                obj = SendStatus()
                obj._deserialize(item)
                self.SendStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class SendStatus(AbstractModel):
    """发送短信状态

    """

    def __init__(self):
        """
        :param SerialNo: 发送流水号。
        :type SerialNo: str
        :param PhoneNumber: 手机号码,e.164标准，+[国家或地区码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :type PhoneNumber: str
        :param Fee: 计费条数，计费规则请查询 [计费策略](https://cloud.tencent.com/document/product/382/36135)。
        :type Fee: int
        :param SessionContext: 用户Session内容。
        :type SessionContext: str
        :param Code: 短信请求错误码，具体含义请参考错误码。
        :type Code: str
        :param Message: 短信请求错误码描述。
        :type Message: str
        """
        self.SerialNo = None
        self.PhoneNumber = None
        self.Fee = None
        self.SessionContext = None
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.SerialNo = params.get("SerialNo")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Fee = params.get("Fee")
        self.SessionContext = params.get("SessionContext")
        self.Code = params.get("Code")
        self.Message = params.get("Message")


class SendStatusStatistics(AbstractModel):
    """发送数据统计响应包体

    """

    def __init__(self):
        """
        :param FeeCount: 短信计费条数统计，例如提交成功量为100条，其中有20条是长短信（长度为80字）被拆分成2条，则计费条数为： ```80 * 1 + 20 * 2 = 120``` 条。
        :type FeeCount: int
        :param RequestCount: 短信提交量统计。
        :type RequestCount: int
        :param RequestSuccessCount: 短信提交成功量统计。
        :type RequestSuccessCount: int
        """
        self.FeeCount = None
        self.RequestCount = None
        self.RequestSuccessCount = None


    def _deserialize(self, params):
        self.FeeCount = params.get("FeeCount")
        self.RequestCount = params.get("RequestCount")
        self.RequestSuccessCount = params.get("RequestSuccessCount")


class SendStatusStatisticsRequest(AbstractModel):
    """SendStatusStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param StartDateTime: 拉取起始时间，yyyymmddhh 需要拉取的起始时间，精确到小时。
        :type StartDateTime: int
        :param EndDataTime: 结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时
注：EndDataTime 必须大于 StartDateTime。
        :type EndDataTime: int
        :param SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid，示例如1400006666。
        :type SmsSdkAppid: str
        :param Limit: 最大上限。
注：目前固定设置为0。
        :type Limit: int
        :param Offset: 偏移量。
注：目前固定设置为0。
        :type Offset: int
        """
        self.StartDateTime = None
        self.EndDataTime = None
        self.SmsSdkAppid = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartDateTime = params.get("StartDateTime")
        self.EndDataTime = params.get("EndDataTime")
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class SendStatusStatisticsResponse(AbstractModel):
    """SendStatusStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param SendStatusStatistics: 发送数据统计响应包体。
        :type SendStatusStatistics: :class:`tencentcloud.sms.v20190711.models.SendStatusStatistics`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SendStatusStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SendStatusStatistics") is not None:
            self.SendStatusStatistics = SendStatusStatistics()
            self.SendStatusStatistics._deserialize(params.get("SendStatusStatistics"))
        self.RequestId = params.get("RequestId")


class SmsPackagesStatistics(AbstractModel):
    """套餐包信息统计响应包体

    """

    def __init__(self):
        """
        :param PackageCreateTime: 套餐包创建时间，标准时间，例如：2019-10-08 17:18:37。
        :type PackageCreateTime: str
        :param PackageCreateUnixTime: 套餐包创建时间，UNIX 时间戳（单位：秒）。
        :type PackageCreateUnixTime: int
        :param PackageEffectiveTime: 套餐包生效时间，标准时间，例如：2019-10-08 17:18:37。
        :type PackageEffectiveTime: str
        :param PackageEffectiveUnixTime: 套餐包生效时间，UNIX 时间戳（单位：秒）。
        :type PackageEffectiveUnixTime: int
        :param PackageExpiredTime: 套餐包过期时间，标准时间，例如：2019-10-08 17:18:37。
        :type PackageExpiredTime: str
        :param PackageExpiredUnixTime: 套餐包过期时间，UNIX 时间戳（单位：秒）。
        :type PackageExpiredUnixTime: int
        :param AmountOfPackage: 套餐包条数。
        :type AmountOfPackage: int
        :param TypeOfPackage: 0表示赠送套餐包，1表示购买套餐包。
        :type TypeOfPackage: int
        :param PackageId: 套餐包 ID。
        :type PackageId: int
        :param CurrentUsage: 当前使用量。
        :type CurrentUsage: int
        """
        self.PackageCreateTime = None
        self.PackageCreateUnixTime = None
        self.PackageEffectiveTime = None
        self.PackageEffectiveUnixTime = None
        self.PackageExpiredTime = None
        self.PackageExpiredUnixTime = None
        self.AmountOfPackage = None
        self.TypeOfPackage = None
        self.PackageId = None
        self.CurrentUsage = None


    def _deserialize(self, params):
        self.PackageCreateTime = params.get("PackageCreateTime")
        self.PackageCreateUnixTime = params.get("PackageCreateUnixTime")
        self.PackageEffectiveTime = params.get("PackageEffectiveTime")
        self.PackageEffectiveUnixTime = params.get("PackageEffectiveUnixTime")
        self.PackageExpiredTime = params.get("PackageExpiredTime")
        self.PackageExpiredUnixTime = params.get("PackageExpiredUnixTime")
        self.AmountOfPackage = params.get("AmountOfPackage")
        self.TypeOfPackage = params.get("TypeOfPackage")
        self.PackageId = params.get("PackageId")
        self.CurrentUsage = params.get("CurrentUsage")


class SmsPackagesStatisticsRequest(AbstractModel):
    """SmsPackagesStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/sms/smslist) 添加应用后生成的实际SdkAppid，示例如1400006666。
        :type SmsSdkAppid: str
        :param Limit: 最大上限(需要拉取的套餐包个数)。
        :type Limit: int
        :param Offset: 偏移量。
注：目前固定设置为0。
        :type Offset: int
        """
        self.SmsSdkAppid = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class SmsPackagesStatisticsResponse(AbstractModel):
    """SmsPackagesStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param SmsPackagesStatisticsSet: 发送数据统计响应包体。
        :type SmsPackagesStatisticsSet: list of SmsPackagesStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SmsPackagesStatisticsSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SmsPackagesStatisticsSet") is not None:
            self.SmsPackagesStatisticsSet = []
            for item in params.get("SmsPackagesStatisticsSet"):
                obj = SmsPackagesStatistics()
                obj._deserialize(item)
                self.SmsPackagesStatisticsSet.append(obj)
        self.RequestId = params.get("RequestId")