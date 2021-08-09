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
        """
        :param SignId: 签名Id。\n        :type SignId: int\n        :param SignApplyId: 签名申请Id。\n        :type SignApplyId: int\n        """
        self.SignId = None
        self.SignApplyId = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.SignApplyId = params.get("SignApplyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSmsSignRequest(AbstractModel):
    """AddSmsSign请求参数结构体

    """

    def __init__(self):
        """
        :param SignName: 签名名称。
注：不能重复申请已通过或待审核的签名。\n        :type SignName: str\n        :param SignType: 签名类型。其中每种类型后面标注了其可选的 DocumentType（证明类型）：
0：公司（0，1，2，3）。
1：APP（0，1，2，3，4） 。
2：网站（0，1，2，3，5）。
3：公众号或者小程序（0，1，2，3，6）。
4：商标（7）。
5：政府/机关事业单位/其他机构（2，3）。
注：必须按照对应关系选择证明类型，否则会审核失败。\n        :type SignType: int\n        :param DocumentType: 证明类型：
0：三证合一。
1：企业营业执照。
2：组织机构代码证书。
3：社会信用代码证书。
4：应用后台管理截图（个人开发APP）。
5：网站备案后台截图（个人开发网站）。
6：小程序设置页面截图（个人认证小程序）。
7：商标注册书。\n        :type DocumentType: int\n        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。\n        :type International: int\n        :param UsedMethod: 签名用途：
0：自用。
1：他用。\n        :type UsedMethod: int\n        :param ProofImage: 签名对应的资质证明图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。\n        :type ProofImage: str\n        :param CommissionImage: 委托授权证明。选择 UsedMethod 为他用之后需要提交委托的授权证明。
图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。
注：只有 UsedMethod 在选择为 1（他用）时，这个字段才会生效。\n        :type CommissionImage: str\n        :param Remark: 签名的申请备注。\n        :type Remark: str\n        """
        self.SignName = None
        self.SignType = None
        self.DocumentType = None
        self.International = None
        self.UsedMethod = None
        self.ProofImage = None
        self.CommissionImage = None
        self.Remark = None


    def _deserialize(self, params):
        self.SignName = params.get("SignName")
        self.SignType = params.get("SignType")
        self.DocumentType = params.get("DocumentType")
        self.International = params.get("International")
        self.UsedMethod = params.get("UsedMethod")
        self.ProofImage = params.get("ProofImage")
        self.CommissionImage = params.get("CommissionImage")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSmsSignResponse(AbstractModel):
    """AddSmsSign返回参数结构体

    """

    def __init__(self):
        """
        :param AddSignStatus: 添加签名响应\n        :type AddSignStatus: :class:`tencentcloud.sms.v20190711.models.AddSignStatus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AddSignStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AddSignStatus") is not None:
            self.AddSignStatus = AddSignStatus()
            self.AddSignStatus._deserialize(params.get("AddSignStatus"))
        self.RequestId = params.get("RequestId")


class AddSmsTemplateRequest(AbstractModel):
    """AddSmsTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateName: 模板名称。\n        :type TemplateName: str\n        :param TemplateContent: 模板内容。\n        :type TemplateContent: str\n        :param SmsType: 短信类型，0表示普通短信, 1表示营销短信。\n        :type SmsType: int\n        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。\n        :type International: int\n        :param Remark: 模板备注，例如申请原因，使用场景等。\n        :type Remark: str\n        """
        self.TemplateName = None
        self.TemplateContent = None
        self.SmsType = None
        self.International = None
        self.Remark = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.TemplateContent = params.get("TemplateContent")
        self.SmsType = params.get("SmsType")
        self.International = params.get("International")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSmsTemplateResponse(AbstractModel):
    """AddSmsTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param AddTemplateStatus: 添加短信模板响应包体\n        :type AddTemplateStatus: :class:`tencentcloud.sms.v20190711.models.AddTemplateStatus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AddTemplateStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AddTemplateStatus") is not None:
            self.AddTemplateStatus = AddTemplateStatus()
            self.AddTemplateStatus._deserialize(params.get("AddTemplateStatus"))
        self.RequestId = params.get("RequestId")


class AddTemplateStatus(AbstractModel):
    """添加模板参数响应

    """

    def __init__(self):
        """
        :param TemplateId: 模板参数\n        :type TemplateId: str\n        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallbackStatusStatistics(AbstractModel):
    """回执数据统计响应包体

    """

    def __init__(self):
        """
        :param CallbackCount: 短信回执量统计。\n        :type CallbackCount: int\n        :param RequestSuccessCount: 短信提交成功量统计。\n        :type RequestSuccessCount: int\n        :param CallbackFailCount: 短信回执失败量统计。\n        :type CallbackFailCount: int\n        :param CallbackSuccessCount: 短信回执成功量统计。\n        :type CallbackSuccessCount: int\n        :param InternalErrorCount: 运营商内部错误统计。\n        :type InternalErrorCount: int\n        :param InvalidNumberCount: 号码无效或空号统计。\n        :type InvalidNumberCount: int\n        :param ShutdownErrorCount: 停机、关机等错误统计。\n        :type ShutdownErrorCount: int\n        :param BlackListCount: 号码拉入黑名单统计。\n        :type BlackListCount: int\n        :param FrequencyLimitCount: 运营商频率限制统计。\n        :type FrequencyLimitCount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallbackStatusStatisticsRequest(AbstractModel):
    """CallbackStatusStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param StartDateTime: 开始时间，yyyymmddhh 需要拉取的起始时间，精确到小时。\n        :type StartDateTime: int\n        :param EndDataTime: 结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时。
注：EndDataTime 必须大于 StartDateTime。\n        :type EndDataTime: int\n        :param SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，示例如1400006666。\n        :type SmsSdkAppid: str\n        :param Limit: 最大上限。
注：目前固定设置为0。\n        :type Limit: int\n        :param Offset: 偏移量。
注：目前固定设置为0。\n        :type Offset: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallbackStatusStatisticsResponse(AbstractModel):
    """CallbackStatusStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param CallbackStatusStatistics: 回执数据统计响应包体。\n        :type CallbackStatusStatistics: :class:`tencentcloud.sms.v20190711.models.CallbackStatusStatistics`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CallbackStatusStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CallbackStatusStatistics") is not None:
            self.CallbackStatusStatistics = CallbackStatusStatistics()
            self.CallbackStatusStatistics._deserialize(params.get("CallbackStatusStatistics"))
        self.RequestId = params.get("RequestId")


class DeleteSignStatus(AbstractModel):
    """删除签名响应

    """

    def __init__(self):
        """
        :param DeleteStatus: 删除状态信息。\n        :type DeleteStatus: str\n        :param DeleteTime: 删除时间，UNIX 时间戳（单位：秒）。\n        :type DeleteTime: int\n        """
        self.DeleteStatus = None
        self.DeleteTime = None


    def _deserialize(self, params):
        self.DeleteStatus = params.get("DeleteStatus")
        self.DeleteTime = params.get("DeleteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSmsSignRequest(AbstractModel):
    """DeleteSmsSign请求参数结构体

    """

    def __init__(self):
        """
        :param SignId: 待删除的签名 ID。\n        :type SignId: int\n        """
        self.SignId = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSmsSignResponse(AbstractModel):
    """DeleteSmsSign返回参数结构体

    """

    def __init__(self):
        """
        :param DeleteSignStatus: 删除签名响应\n        :type DeleteSignStatus: :class:`tencentcloud.sms.v20190711.models.DeleteSignStatus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DeleteSignStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeleteSignStatus") is not None:
            self.DeleteSignStatus = DeleteSignStatus()
            self.DeleteSignStatus._deserialize(params.get("DeleteSignStatus"))
        self.RequestId = params.get("RequestId")


class DeleteSmsTemplateRequest(AbstractModel):
    """DeleteSmsTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 待删除的模板 ID。\n        :type TemplateId: int\n        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSmsTemplateResponse(AbstractModel):
    """DeleteSmsTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param DeleteTemplateStatus: 删除模板响应\n        :type DeleteTemplateStatus: :class:`tencentcloud.sms.v20190711.models.DeleteTemplateStatus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DeleteTemplateStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeleteTemplateStatus") is not None:
            self.DeleteTemplateStatus = DeleteTemplateStatus()
            self.DeleteTemplateStatus._deserialize(params.get("DeleteTemplateStatus"))
        self.RequestId = params.get("RequestId")


class DeleteTemplateStatus(AbstractModel):
    """删除模板响应

    """

    def __init__(self):
        """
        :param DeleteStatus: 删除状态信息。\n        :type DeleteStatus: str\n        :param DeleteTime: 删除时间，UNIX 时间戳（单位：秒）。\n        :type DeleteTime: int\n        """
        self.DeleteStatus = None
        self.DeleteTime = None


    def _deserialize(self, params):
        self.DeleteStatus = params.get("DeleteStatus")
        self.DeleteTime = params.get("DeleteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSignListStatus(AbstractModel):
    """获取短信签名信息响应

    """

    def __init__(self):
        """
        :param SignId: 签名Id\n        :type SignId: int\n        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。\n        :type International: int\n        :param StatusCode: 申请签名状态。其中：
0：表示审核通过。
1：表示审核中。
-1：表示审核未通过或审核失败。\n        :type StatusCode: int\n        :param ReviewReply: 审核回复，审核人员审核后给出的回复，通常是审核未通过的原因。\n        :type ReviewReply: str\n        :param SignName: 签名名称。\n        :type SignName: str\n        :param CreateTime: 提交审核时间，UNIX 时间戳（单位：秒）。\n        :type CreateTime: int\n        """
        self.SignId = None
        self.International = None
        self.StatusCode = None
        self.ReviewReply = None
        self.SignName = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.International = params.get("International")
        self.StatusCode = params.get("StatusCode")
        self.ReviewReply = params.get("ReviewReply")
        self.SignName = params.get("SignName")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsSignListRequest(AbstractModel):
    """DescribeSmsSignList请求参数结构体

    """

    def __init__(self):
        """
        :param SignIdSet: 签名 ID 数组。\n        :type SignIdSet: list of int non-negative\n        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。\n        :type International: int\n        """
        self.SignIdSet = None
        self.International = None


    def _deserialize(self, params):
        self.SignIdSet = params.get("SignIdSet")
        self.International = params.get("International")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsSignListResponse(AbstractModel):
    """DescribeSmsSignList返回参数结构体

    """

    def __init__(self):
        """
        :param DescribeSignListStatusSet: 获取签名信息响应\n        :type DescribeSignListStatusSet: list of DescribeSignListStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DescribeSignListStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DescribeSignListStatusSet") is not None:
            self.DescribeSignListStatusSet = []
            for item in params.get("DescribeSignListStatusSet"):
                obj = DescribeSignListStatus()
                obj._deserialize(item)
                self.DescribeSignListStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSmsTemplateListRequest(AbstractModel):
    """DescribeSmsTemplateList请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateIdSet: 模板 ID 数组。\n        :type TemplateIdSet: list of int non-negative\n        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。\n        :type International: int\n        """
        self.TemplateIdSet = None
        self.International = None


    def _deserialize(self, params):
        self.TemplateIdSet = params.get("TemplateIdSet")
        self.International = params.get("International")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsTemplateListResponse(AbstractModel):
    """DescribeSmsTemplateList返回参数结构体

    """

    def __init__(self):
        """
        :param DescribeTemplateStatusSet: 获取短信模板信息响应\n        :type DescribeTemplateStatusSet: list of DescribeTemplateListStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DescribeTemplateStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DescribeTemplateStatusSet") is not None:
            self.DescribeTemplateStatusSet = []
            for item in params.get("DescribeTemplateStatusSet"):
                obj = DescribeTemplateListStatus()
                obj._deserialize(item)
                self.DescribeTemplateStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTemplateListStatus(AbstractModel):
    """获取短信模板信息响应

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id\n        :type TemplateId: int\n        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。\n        :type International: int\n        :param StatusCode: 申请签名状态。其中：
0：表示审核通过。
1：表示审核中。
-1：表示审核未通过或审核失败。\n        :type StatusCode: int\n        :param ReviewReply: 审核回复，审核人员审核后给出的回复，通常是审核未通过的原因。\n        :type ReviewReply: str\n        :param TemplateName: 模板名称。\n        :type TemplateName: str\n        :param CreateTime: 提交审核时间，UNIX 时间戳（单位：秒）。\n        :type CreateTime: int\n        """
        self.TemplateId = None
        self.International = None
        self.StatusCode = None
        self.ReviewReply = None
        self.TemplateName = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.International = params.get("International")
        self.StatusCode = params.get("StatusCode")
        self.ReviewReply = params.get("ReviewReply")
        self.TemplateName = params.get("TemplateName")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySignStatus(AbstractModel):
    """修改签名响应

    """

    def __init__(self):
        """
        :param SignId: 签名Id\n        :type SignId: int\n        :param SignApplyId: 签名修改申请Id\n        :type SignApplyId: str\n        """
        self.SignId = None
        self.SignApplyId = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.SignApplyId = params.get("SignApplyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySmsSignRequest(AbstractModel):
    """ModifySmsSign请求参数结构体

    """

    def __init__(self):
        """
        :param SignId: 待修改的签名 ID。\n        :type SignId: int\n        :param SignName: 签名名称。\n        :type SignName: str\n        :param SignType: 签名类型。其中每种类型后面标注了其可选的 DocumentType（证明类型）：
0：公司（0，1，2，3）。
1：APP（0，1，2，3，4） 。
2：网站（0，1，2，3，5）。
3：公众号或者小程序（0，1，2，3，6）。
4：商标（7）。
5：政府/机关事业单位/其他机构（2，3）。
注：必须按照对应关系选择证明类型，否则会审核失败。\n        :type SignType: int\n        :param DocumentType: 证明类型：
0：三证合一。
1：企业营业执照。
2：组织机构代码证书。
3：社会信用代码证书。
4：应用后台管理截图(个人开发APP)。
5：网站备案后台截图(个人开发网站)。
6：小程序设置页面截图(个人认证小程序)。
7：商标注册书。\n        :type DocumentType: int\n        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
注：需要和待修改签名International值保持一致，该参数不能直接修改国内签名到国际签名。\n        :type International: int\n        :param UsedMethod: 签名用途：
0：自用。
1：他用。\n        :type UsedMethod: int\n        :param ProofImage: 签名对应的资质证明图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。\n        :type ProofImage: str\n        :param CommissionImage: 委托授权证明。选择 UsedMethod 为他用之后需要提交委托的授权证明。
图片需先进行 base64 编码格式转换，将转换后的字符串去掉前缀`data:image/jpeg;base64,`再赋值给该参数。
注：只有 UsedMethod 在选择为 1（他用）时，这个字段才会生效。\n        :type CommissionImage: str\n        :param Remark: 签名的申请备注。\n        :type Remark: str\n        """
        self.SignId = None
        self.SignName = None
        self.SignType = None
        self.DocumentType = None
        self.International = None
        self.UsedMethod = None
        self.ProofImage = None
        self.CommissionImage = None
        self.Remark = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.SignName = params.get("SignName")
        self.SignType = params.get("SignType")
        self.DocumentType = params.get("DocumentType")
        self.International = params.get("International")
        self.UsedMethod = params.get("UsedMethod")
        self.ProofImage = params.get("ProofImage")
        self.CommissionImage = params.get("CommissionImage")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySmsSignResponse(AbstractModel):
    """ModifySmsSign返回参数结构体

    """

    def __init__(self):
        """
        :param ModifySignStatus: 修改签名响应\n        :type ModifySignStatus: :class:`tencentcloud.sms.v20190711.models.ModifySignStatus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ModifySignStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ModifySignStatus") is not None:
            self.ModifySignStatus = ModifySignStatus()
            self.ModifySignStatus._deserialize(params.get("ModifySignStatus"))
        self.RequestId = params.get("RequestId")


class ModifySmsTemplateRequest(AbstractModel):
    """ModifySmsTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 待修改的模板的模板 ID。\n        :type TemplateId: int\n        :param TemplateName: 新的模板名称。\n        :type TemplateName: str\n        :param TemplateContent: 新的模板内容。\n        :type TemplateContent: str\n        :param SmsType: 短信类型，0表示普通短信, 1表示营销短信。\n        :type SmsType: int\n        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。\n        :type International: int\n        :param Remark: 模板备注，例如申请原因，使用场景等。\n        :type Remark: str\n        """
        self.TemplateId = None
        self.TemplateName = None
        self.TemplateContent = None
        self.SmsType = None
        self.International = None
        self.Remark = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.TemplateContent = params.get("TemplateContent")
        self.SmsType = params.get("SmsType")
        self.International = params.get("International")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySmsTemplateResponse(AbstractModel):
    """ModifySmsTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param ModifyTemplateStatus: 修改模板参数响应\n        :type ModifyTemplateStatus: :class:`tencentcloud.sms.v20190711.models.ModifyTemplateStatus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ModifyTemplateStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ModifyTemplateStatus") is not None:
            self.ModifyTemplateStatus = ModifyTemplateStatus()
            self.ModifyTemplateStatus._deserialize(params.get("ModifyTemplateStatus"))
        self.RequestId = params.get("RequestId")


class ModifyTemplateStatus(AbstractModel):
    """修改模板参数响应

    """

    def __init__(self):
        """
        :param TemplateId: 模板参数\n        :type TemplateId: int\n        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsReplyStatus(AbstractModel):
    """短信回复状态

    """

    def __init__(self):
        """
        :param ExtendCode: 短信码号扩展号，默认未开通，如需开通请联系 [sms helper](https://cloud.tencent.com/document/product/382/3773)。\n        :type ExtendCode: str\n        :param NationCode: 国家（或地区）码。\n        :type NationCode: str\n        :param PhoneNumber: 手机号码,e.164标准，+[国家或地区码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。\n        :type PhoneNumber: str\n        :param Sign: 短信签名。\n        :type Sign: str\n        :param ReplyContent: 用户回复的内容。\n        :type ReplyContent: str\n        :param ReplyTime: 回复时间（例如：2019-10-08 17:18:37）。\n        :type ReplyTime: str\n        :param ReplyUnixTime: 回复时间，UNIX 时间戳（单位：秒）。\n        :type ReplyUnixTime: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsReplyStatusByPhoneNumberRequest(AbstractModel):
    """PullSmsReplyStatusByPhoneNumber请求参数结构体

    """

    def __init__(self):
        """
        :param SendDateTime: 拉取起始时间，UNIX 时间戳（时间：秒）。
注：最大可拉取当前时期7天前的数据。\n        :type SendDateTime: int\n        :param Offset: 偏移量。
注：目前固定设置为0。\n        :type Offset: int\n        :param Limit: 拉取最大条数，最多 100。\n        :type Limit: int\n        :param PhoneNumber: 下发目的手机号码，依据 e.164 标准为：+[国家（或地区）码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。\n        :type PhoneNumber: str\n        :param SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，例如1400006666。\n        :type SmsSdkAppid: str\n        :param EndDateTime: 拉取截止时间，UNIX 时间戳（时间：秒）。\n        :type EndDateTime: int\n        """
        self.SendDateTime = None
        self.Offset = None
        self.Limit = None
        self.PhoneNumber = None
        self.SmsSdkAppid = None
        self.EndDateTime = None


    def _deserialize(self, params):
        self.SendDateTime = params.get("SendDateTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PhoneNumber = params.get("PhoneNumber")
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.EndDateTime = params.get("EndDateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsReplyStatusByPhoneNumberResponse(AbstractModel):
    """PullSmsReplyStatusByPhoneNumber返回参数结构体

    """

    def __init__(self):
        """
        :param PullSmsReplyStatusSet: 回复状态响应集合。\n        :type PullSmsReplyStatusSet: list of PullSmsReplyStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Limit: 拉取最大条数，最多100条。\n        :type Limit: int\n        :param SmsSdkAppid: 短信 SdkAppid 在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际 SdkAppid，例如1400006666。\n        :type SmsSdkAppid: str\n        """
        self.Limit = None
        self.SmsSdkAppid = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsReplyStatusResponse(AbstractModel):
    """PullSmsReplyStatus返回参数结构体

    """

    def __init__(self):
        """
        :param PullSmsReplyStatusSet: 回复状态响应集合。\n        :type PullSmsReplyStatusSet: list of PullSmsReplyStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param UserReceiveTime: 用户实际接收到短信的时间。\n        :type UserReceiveTime: str\n        :param UserReceiveUnixTime: 用户实际接收到短信的时间，UNIX 时间戳（单位：秒）。\n        :type UserReceiveUnixTime: int\n        :param NationCode: 国家（或地区）码。\n        :type NationCode: str\n        :param PurePhoneNumber: 手机号码,e.164标准，+[国家或地区码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。\n        :type PurePhoneNumber: str\n        :param PhoneNumber: 手机号码，普通格式，示例如：13711112222。\n        :type PhoneNumber: str\n        :param SerialNo: 本次发送标识 ID。\n        :type SerialNo: str\n        :param ReportStatus: 实际是否收到短信接收状态，SUCCESS（成功）、FAIL（失败）。\n        :type ReportStatus: str\n        :param Description: 用户接收短信状态描述。\n        :type Description: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsSendStatusByPhoneNumberRequest(AbstractModel):
    """PullSmsSendStatusByPhoneNumber请求参数结构体

    """

    def __init__(self):
        """
        :param SendDateTime: 拉取起始时间，UNIX 时间戳（时间：秒）。
注：最大可拉取当前时期7天前的数据。\n        :type SendDateTime: int\n        :param Offset: 偏移量。
注：目前固定设置为0。\n        :type Offset: int\n        :param Limit: 拉取最大条数，最多 100。\n        :type Limit: int\n        :param PhoneNumber: 下发目的手机号码，依据 e.164 标准为：+[国家（或地区）码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。\n        :type PhoneNumber: str\n        :param SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，例如1400006666。\n        :type SmsSdkAppid: str\n        :param EndDateTime: 拉取截止时间，UNIX 时间戳（时间：秒）。\n        :type EndDateTime: int\n        """
        self.SendDateTime = None
        self.Offset = None
        self.Limit = None
        self.PhoneNumber = None
        self.SmsSdkAppid = None
        self.EndDateTime = None


    def _deserialize(self, params):
        self.SendDateTime = params.get("SendDateTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PhoneNumber = params.get("PhoneNumber")
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.EndDateTime = params.get("EndDateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsSendStatusByPhoneNumberResponse(AbstractModel):
    """PullSmsSendStatusByPhoneNumber返回参数结构体

    """

    def __init__(self):
        """
        :param PullSmsSendStatusSet: 下发状态响应集合。\n        :type PullSmsSendStatusSet: list of PullSmsSendStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Limit: 拉取最大条数，最多100条。\n        :type Limit: int\n        :param SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，例如1400006666。\n        :type SmsSdkAppid: str\n        """
        self.Limit = None
        self.SmsSdkAppid = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullSmsSendStatusResponse(AbstractModel):
    """PullSmsSendStatus返回参数结构体

    """

    def __init__(self):
        """
        :param PullSmsSendStatusSet: 下发状态响应集合。\n        :type PullSmsSendStatusSet: list of PullSmsSendStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param PhoneNumberSet: 下发手机号码，采用 e.164 标准，格式为+[国家或地区码][手机号]，单次请求最多支持200个手机号且要求全为境内手机号或全为境外手机号。
例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。\n        :type PhoneNumberSet: list of str\n        :param TemplateID: 模板 ID，必须填写已审核通过的模板 ID。模板ID可登录 [短信控制台](https://console.cloud.tencent.com/smsv2) 查看，若向境外手机号发送短信，仅支持使用国际/港澳台短信模板。\n        :type TemplateID: str\n        :param SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2)  添加应用后生成的实际SdkAppid，示例如1400006666。\n        :type SmsSdkAppid: str\n        :param Sign: 短信签名内容，使用 UTF-8 编码，必须填写已审核通过的签名，签名信息可登录 [短信控制台](https://console.cloud.tencent.com/smsv2)  查看。注：国内短信为必填参数。\n        :type Sign: str\n        :param TemplateParamSet: 模板参数，若无模板参数，则设置为空。\n        :type TemplateParamSet: list of str\n        :param ExtendCode: 短信码号扩展号，默认未开通，如需开通请联系 [sms helper](https://cloud.tencent.com/document/product/382/3773)。\n        :type ExtendCode: str\n        :param SessionContext: 用户的 session 内容，可以携带用户侧 ID 等上下文信息，server 会原样返回。\n        :type SessionContext: str\n        :param SenderId: 国内短信无senderid，无需填写该项；若需开通国际/港澳台短信senderid，请联系smshelper。\n        :type SenderId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendSmsResponse(AbstractModel):
    """SendSms返回参数结构体

    """

    def __init__(self):
        """
        :param SendStatusSet: 短信发送状态。\n        :type SendStatusSet: list of SendStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param SerialNo: 发送流水号。\n        :type SerialNo: str\n        :param PhoneNumber: 手机号码,e.164标准，+[国家或地区码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。\n        :type PhoneNumber: str\n        :param Fee: 计费条数，计费规则请查询 [计费策略](https://cloud.tencent.com/document/product/382/36135)。\n        :type Fee: int\n        :param SessionContext: 用户Session内容。\n        :type SessionContext: str\n        :param Code: 短信请求错误码，具体含义请参考错误码。\n        :type Code: str\n        :param Message: 短信请求错误码描述。\n        :type Message: str\n        :param IsoCode: 国家码或地区码，例如CN,US等，对于未识别出国家码或者地区码，默认返回DEF,具体支持列表请参考国际/港澳台计费总览。\n        :type IsoCode: str\n        """
        self.SerialNo = None
        self.PhoneNumber = None
        self.Fee = None
        self.SessionContext = None
        self.Code = None
        self.Message = None
        self.IsoCode = None


    def _deserialize(self, params):
        self.SerialNo = params.get("SerialNo")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Fee = params.get("Fee")
        self.SessionContext = params.get("SessionContext")
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.IsoCode = params.get("IsoCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendStatusStatistics(AbstractModel):
    """发送数据统计响应包体

    """

    def __init__(self):
        """
        :param FeeCount: 短信计费条数统计，例如提交成功量为100条，其中有20条是长短信（长度为80字）被拆分成2条，则计费条数为： ```80 * 1 + 20 * 2 = 120``` 条。\n        :type FeeCount: int\n        :param RequestCount: 短信提交量统计。\n        :type RequestCount: int\n        :param RequestSuccessCount: 短信提交成功量统计。\n        :type RequestSuccessCount: int\n        """
        self.FeeCount = None
        self.RequestCount = None
        self.RequestSuccessCount = None


    def _deserialize(self, params):
        self.FeeCount = params.get("FeeCount")
        self.RequestCount = params.get("RequestCount")
        self.RequestSuccessCount = params.get("RequestSuccessCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendStatusStatisticsRequest(AbstractModel):
    """SendStatusStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param StartDateTime: 拉取起始时间，yyyymmddhh 需要拉取的起始时间，精确到小时。\n        :type StartDateTime: int\n        :param EndDataTime: 结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时
注：EndDataTime 必须大于 StartDateTime。\n        :type EndDataTime: int\n        :param SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，示例如1400006666。\n        :type SmsSdkAppid: str\n        :param Limit: 最大上限。
注：目前固定设置为0。\n        :type Limit: int\n        :param Offset: 偏移量。
注：目前固定设置为0。\n        :type Offset: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendStatusStatisticsResponse(AbstractModel):
    """SendStatusStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param SendStatusStatistics: 发送数据统计响应包体。\n        :type SendStatusStatistics: :class:`tencentcloud.sms.v20190711.models.SendStatusStatistics`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param PackageCreateTime: 套餐包创建时间，标准时间，例如：2019-10-08 17:18:37。\n        :type PackageCreateTime: str\n        :param PackageCreateUnixTime: 套餐包创建时间，UNIX 时间戳（单位：秒）。\n        :type PackageCreateUnixTime: int\n        :param PackageEffectiveTime: 套餐包生效时间，标准时间，例如：2019-10-08 17:18:37。\n        :type PackageEffectiveTime: str\n        :param PackageEffectiveUnixTime: 套餐包生效时间，UNIX 时间戳（单位：秒）。\n        :type PackageEffectiveUnixTime: int\n        :param PackageExpiredTime: 套餐包过期时间，标准时间，例如：2019-10-08 17:18:37。\n        :type PackageExpiredTime: str\n        :param PackageExpiredUnixTime: 套餐包过期时间，UNIX 时间戳（单位：秒）。\n        :type PackageExpiredUnixTime: int\n        :param AmountOfPackage: 套餐包条数。\n        :type AmountOfPackage: int\n        :param TypeOfPackage: 0表示赠送套餐包，1表示购买套餐包。\n        :type TypeOfPackage: int\n        :param PackageId: 套餐包 ID。\n        :type PackageId: int\n        :param CurrentUsage: 当前使用量。\n        :type CurrentUsage: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsPackagesStatisticsRequest(AbstractModel):
    """SmsPackagesStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param SmsSdkAppid: 短信SdkAppid在 [短信控制台](https://console.cloud.tencent.com/smsv2) 添加应用后生成的实际SdkAppid，示例如1400006666。\n        :type SmsSdkAppid: str\n        :param Limit: 最大上限(需要拉取的套餐包个数)。\n        :type Limit: int\n        :param Offset: 偏移量。
注：目前固定设置为0。\n        :type Offset: int\n        """
        self.SmsSdkAppid = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsPackagesStatisticsResponse(AbstractModel):
    """SmsPackagesStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param SmsPackagesStatisticsSet: 发送数据统计响应包体。\n        :type SmsPackagesStatisticsSet: list of SmsPackagesStatistics\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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