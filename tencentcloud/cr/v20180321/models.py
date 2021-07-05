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


class ApplyBlackListDataRequest(AbstractModel):
    """ApplyBlackListData请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，AiApi
        :type Module: str
        :param Operation: 操作名，ApplyBlackListData
        :type Operation: str
        :param BlackList: 黑名单列表
        :type BlackList: list of BlackListData
        """
        self.Module = None
        self.Operation = None
        self.BlackList = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        if params.get("BlackList") is not None:
            self.BlackList = []
            for item in params.get("BlackList"):
                obj = BlackListData()
                obj._deserialize(item)
                self.BlackList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyBlackListDataResponse(AbstractModel):
    """ApplyBlackListData返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ApplyBlackListRequest(AbstractModel):
    """ApplyBlackList请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，本接口取值：account
        :type Module: str
        :param Operation: 操作名，本接口取值：ApplyBlackList
        :type Operation: str
        :param BlackList: 黑名单列表
        :type BlackList: list of SingleBlackApply
        :param InstId: 实例ID，不传默认为系统分配的初始实例
        :type InstId: str
        """
        self.Module = None
        self.Operation = None
        self.BlackList = None
        self.InstId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        if params.get("BlackList") is not None:
            self.BlackList = []
            for item in params.get("BlackList"):
                obj = SingleBlackApply()
                obj._deserialize(item)
                self.BlackList.append(obj)
        self.InstId = params.get("InstId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyBlackListResponse(AbstractModel):
    """ApplyBlackList返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ApplyCreditAuditRequest(AbstractModel):
    """ApplyCreditAudit请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，本接口取值：Credit
        :type Module: str
        :param Operation: 操作名，本接口取值：Apply
        :type Operation: str
        :param InstId: 实例ID
        :type InstId: str
        :param ProductId: 产品ID，形如P******。
        :type ProductId: str
        :param CaseId: 信审任务ID，同一天内，同一InstId下，同一CaseId只能调用一次。
        :type CaseId: str
        :param CallbackUrl: 回调地址
        :type CallbackUrl: str
        :param Data: JSON格式的业务字段。
        :type Data: str
        """
        self.Module = None
        self.Operation = None
        self.InstId = None
        self.ProductId = None
        self.CaseId = None
        self.CallbackUrl = None
        self.Data = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.InstId = params.get("InstId")
        self.ProductId = params.get("ProductId")
        self.CaseId = params.get("CaseId")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyCreditAuditResponse(AbstractModel):
    """ApplyCreditAudit返回参数结构体

    """

    def __init__(self):
        """
        :param RequestDate: 请求日期
        :type RequestDate: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestDate = params.get("RequestDate")
        self.RequestId = params.get("RequestId")


class BlackListData(AbstractModel):
    """黑名单申请信息

    """

    def __init__(self):
        """
        :param BlackType: 黑名单类型，01代表手机号码。
        :type BlackType: str
        :param OperType: 操作类型，A为新增，D为删除。
注意：此字段可能返回 null，表示取不到有效值。
        :type OperType: str
        :param BlackValue: 黑名单值，BlackType为01时，填写11位手机号码。
        :type BlackValue: str
        :param BlackDescription: 备注。
注意：此字段可能返回 null，表示取不到有效值。
        :type BlackDescription: str
        :param BlackValidDate: 黑名单生效截止日期，格式为YYYY-MM-DD，不填默认为永久。
注意：此字段可能返回 null，表示取不到有效值。
        :type BlackValidDate: str
        :param BlackAddDate: 黑名单加入日期
注意：此字段可能返回 null，表示取不到有效值。
        :type BlackAddDate: str
        :param BlackStatus: 0-生效 1-失效
        :type BlackStatus: str
        """
        self.BlackType = None
        self.OperType = None
        self.BlackValue = None
        self.BlackDescription = None
        self.BlackValidDate = None
        self.BlackAddDate = None
        self.BlackStatus = None


    def _deserialize(self, params):
        self.BlackType = params.get("BlackType")
        self.OperType = params.get("OperType")
        self.BlackValue = params.get("BlackValue")
        self.BlackDescription = params.get("BlackDescription")
        self.BlackValidDate = params.get("BlackValidDate")
        self.BlackAddDate = params.get("BlackAddDate")
        self.BlackStatus = params.get("BlackStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotFileData(AbstractModel):
    """机器人文件结构

    """

    def __init__(self):
        """
        :param FileType: 文件类型 A 拨打结果 T 记录详情
        :type FileType: str
        :param CosUrl: 文件地址
        :type CosUrl: str
        """
        self.FileType = None
        self.CosUrl = None


    def _deserialize(self, params):
        self.FileType = params.get("FileType")
        self.CosUrl = params.get("CosUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotFlow(AbstractModel):
    """机器人对话流信息

    """

    def __init__(self):
        """
        :param BotFlowId: 对话流ID
        :type BotFlowId: str
        :param BotFlowName: 对话流名称
        :type BotFlowName: str
        :param PhonePoolList: 号码组信息列表
        :type PhonePoolList: list of PhonePool
        """
        self.BotFlowId = None
        self.BotFlowName = None
        self.PhonePoolList = None


    def _deserialize(self, params):
        self.BotFlowId = params.get("BotFlowId")
        self.BotFlowName = params.get("BotFlowName")
        if params.get("PhonePoolList") is not None:
            self.PhonePoolList = []
            for item in params.get("PhonePoolList"):
                obj = PhonePool()
                obj._deserialize(item)
                self.PhonePoolList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotInfo(AbstractModel):
    """机器人列表

    """

    def __init__(self):
        """
        :param BotId: 机器人ID
        :type BotId: str
        :param BotName: 机器人名称
        :type BotName: str
        :param BotStatus: 机器人状态。0-停用 1-启用 2-待审核
        :type BotStatus: str
        """
        self.BotId = None
        self.BotName = None
        self.BotStatus = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.BotName = params.get("BotName")
        self.BotStatus = params.get("BotStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallInfo(AbstractModel):
    """作业信息

    """

    def __init__(self):
        """
        :param BizDate: 业务日期
        :type BizDate: str
        :param Status: 状态 WAIT：待执行；DOING：执行中；ERROR：执行错误；DONE：已完成；
        :type Status: str
        :param TotalCount: 成功总数
        :type TotalCount: int
        :param FileName: 文件名称
        :type FileName: str
        :param FileType: 文件类型 I：呼叫文件 R：停拨文件
        :type FileType: str
        :param CallId: 作业唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type CallId: str
        """
        self.BizDate = None
        self.Status = None
        self.TotalCount = None
        self.FileName = None
        self.FileType = None
        self.CallId = None


    def _deserialize(self, params):
        self.BizDate = params.get("BizDate")
        self.Status = params.get("Status")
        self.TotalCount = params.get("TotalCount")
        self.FileName = params.get("FileName")
        self.FileType = params.get("FileType")
        self.CallId = params.get("CallId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallTimeDict(AbstractModel):
    """产品拨打时间集合

    """

    def __init__(self):
        """
        :param Monday: 周一
        :type Monday: :class:`tencentcloud.cr.v20180321.models.CallTimeInfo`
        :param Tuesday: 周二
        :type Tuesday: :class:`tencentcloud.cr.v20180321.models.CallTimeInfo`
        :param Wednesday: 周三
        :type Wednesday: :class:`tencentcloud.cr.v20180321.models.CallTimeInfo`
        :param Thursday: 周四
        :type Thursday: :class:`tencentcloud.cr.v20180321.models.CallTimeInfo`
        :param Friday: 周五
        :type Friday: :class:`tencentcloud.cr.v20180321.models.CallTimeInfo`
        :param Saturday: 周六
        :type Saturday: :class:`tencentcloud.cr.v20180321.models.CallTimeInfo`
        :param Sunday: 周日
        :type Sunday: :class:`tencentcloud.cr.v20180321.models.CallTimeInfo`
        """
        self.Monday = None
        self.Tuesday = None
        self.Wednesday = None
        self.Thursday = None
        self.Friday = None
        self.Saturday = None
        self.Sunday = None


    def _deserialize(self, params):
        if params.get("Monday") is not None:
            self.Monday = CallTimeInfo()
            self.Monday._deserialize(params.get("Monday"))
        if params.get("Tuesday") is not None:
            self.Tuesday = CallTimeInfo()
            self.Tuesday._deserialize(params.get("Tuesday"))
        if params.get("Wednesday") is not None:
            self.Wednesday = CallTimeInfo()
            self.Wednesday._deserialize(params.get("Wednesday"))
        if params.get("Thursday") is not None:
            self.Thursday = CallTimeInfo()
            self.Thursday._deserialize(params.get("Thursday"))
        if params.get("Friday") is not None:
            self.Friday = CallTimeInfo()
            self.Friday._deserialize(params.get("Friday"))
        if params.get("Saturday") is not None:
            self.Saturday = CallTimeInfo()
            self.Saturday._deserialize(params.get("Saturday"))
        if params.get("Sunday") is not None:
            self.Sunday = CallTimeInfo()
            self.Sunday._deserialize(params.get("Sunday"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallTimeInfo(AbstractModel):
    """产品拨打时间信息

    """

    def __init__(self):
        """
        :param StartTime: 产品开始拨打时间，HHmmss格式,默认090000
        :type StartTime: str
        :param EndTime: 产品结束拨打时间，HHmmss格式.默认200000
        :type EndTime: str
        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeBotCallStatusRequest(AbstractModel):
    """ChangeBotCallStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param Operation: 操作名。默认值（固定）：ChangeBotCallStatus
        :type Operation: str
        :param Status: 作业变更状态
SUSPEND：暂停；EXECUTE：恢复；
        :type Status: str
        :param CallId: 作业唯一标识
        :type CallId: str
        :param BizDate: 业务日期
        :type BizDate: str
        :param BotId: 任务ID，二者必填一个
        :type BotId: str
        :param BotName: 任务名称，二者必填一个
        :type BotName: str
        """
        self.Module = None
        self.Operation = None
        self.Status = None
        self.CallId = None
        self.BizDate = None
        self.BotId = None
        self.BotName = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.Status = params.get("Status")
        self.CallId = params.get("CallId")
        self.BizDate = params.get("BizDate")
        self.BotId = params.get("BotId")
        self.BotName = params.get("BotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeBotCallStatusResponse(AbstractModel):
    """ChangeBotCallStatus返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ChangeBotTaskStatusRequest(AbstractModel):
    """ChangeBotTaskStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param Operation: 操作名。默认值（固定）：ChangeBotTaskStatus
        :type Operation: str
        :param Status: 作业变更状态
SUSPEND：暂停；EXECUTE：恢复；
        :type Status: str
        :param BotId: 任务ID，二者必填一个
        :type BotId: str
        :param BotName: 任务名称，二者必填一个
        :type BotName: str
        """
        self.Module = None
        self.Operation = None
        self.Status = None
        self.BotId = None
        self.BotName = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.Status = params.get("Status")
        self.BotId = params.get("BotId")
        self.BotName = params.get("BotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeBotTaskStatusResponse(AbstractModel):
    """ChangeBotTaskStatus返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateBotTaskRequest(AbstractModel):
    """CreateBotTask请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param Operation: 操作名。默认值（固定）：CreateTask
        :type Operation: str
        :param BotName: 任务名称
        :type BotName: str
        :param FlowId: 对话流ID
        :type FlowId: str
        :param BanCall: 是否禁止拨打，默认Y
        :type BanCall: str
        :param PhoneCollection: 拨打线路集合
        :type PhoneCollection: str
        :param CallTimeCollection: 产品拨打时间集合
        :type CallTimeCollection: :class:`tencentcloud.cr.v20180321.models.CallTimeDict`
        :param StartTimeBan: 禁止拨打起始时间。默认130000
        :type StartTimeBan: str
        :param EndTimeBan: 禁止拨打结束时间。默认140000
        :type EndTimeBan: str
        :param CodeType: 重播方式，NON：未接通、LABEL：意向分级，可多选，用竖线分隔：NON|LABEL
        :type CodeType: str
        :param CodeCollection: 重播值集合，A：强意向、B：中意向、C：低意向、D：无意向、E：在忙、F：未接通、G：无效号码，可多选，用竖线分隔：A|B|C|D|E|F|G
        :type CodeCollection: str
        :param CallCount: 继续拨打次数
        :type CallCount: int
        :param CallInterval: 拨打间隔
        :type CallInterval: int
        :param SmsSignId: 未接通引用短信签名ID
        :type SmsSignId: str
        :param SmsTemplateId: 未接通引用短信模板ID
        :type SmsTemplateId: str
        :param CallType: 拨打方式。NORMAL - 正常拨打；TIMER - 定时拨打
        :type CallType: str
        :param CallStartDate: 拨打开始日期。CallType=TIMER时有值，yyyy-MM-dd
        :type CallStartDate: str
        :param CallEndDate: 拨打结束日期。CallType=PERIOD 时有值，yyyy-MM-dd
        :type CallEndDate: str
        """
        self.Module = None
        self.Operation = None
        self.BotName = None
        self.FlowId = None
        self.BanCall = None
        self.PhoneCollection = None
        self.CallTimeCollection = None
        self.StartTimeBan = None
        self.EndTimeBan = None
        self.CodeType = None
        self.CodeCollection = None
        self.CallCount = None
        self.CallInterval = None
        self.SmsSignId = None
        self.SmsTemplateId = None
        self.CallType = None
        self.CallStartDate = None
        self.CallEndDate = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.BotName = params.get("BotName")
        self.FlowId = params.get("FlowId")
        self.BanCall = params.get("BanCall")
        self.PhoneCollection = params.get("PhoneCollection")
        if params.get("CallTimeCollection") is not None:
            self.CallTimeCollection = CallTimeDict()
            self.CallTimeCollection._deserialize(params.get("CallTimeCollection"))
        self.StartTimeBan = params.get("StartTimeBan")
        self.EndTimeBan = params.get("EndTimeBan")
        self.CodeType = params.get("CodeType")
        self.CodeCollection = params.get("CodeCollection")
        self.CallCount = params.get("CallCount")
        self.CallInterval = params.get("CallInterval")
        self.SmsSignId = params.get("SmsSignId")
        self.SmsTemplateId = params.get("SmsTemplateId")
        self.CallType = params.get("CallType")
        self.CallStartDate = params.get("CallStartDate")
        self.CallEndDate = params.get("CallEndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBotTaskResponse(AbstractModel):
    """CreateBotTask返回参数结构体

    """

    def __init__(self):
        """
        :param BotId: 机器人任务Id
        :type BotId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BotId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.RequestId = params.get("RequestId")


class DescribeBotFlowRequest(AbstractModel):
    """DescribeBotFlow请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param Operation: 操作名。默认值（固定）：GetFlow
        :type Operation: str
        """
        self.Module = None
        self.Operation = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBotFlowResponse(AbstractModel):
    """DescribeBotFlow返回参数结构体

    """

    def __init__(self):
        """
        :param BotFlowList: 机器人对话流列表
注意：此字段可能返回 null，表示取不到有效值。
        :type BotFlowList: list of BotFlow
        :param SmsSignList: 短信签名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SmsSignList: list of SmsSign
        :param SmsTemplateList: 短信模板列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SmsTemplateList: list of SmsTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BotFlowList = None
        self.SmsSignList = None
        self.SmsTemplateList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BotFlowList") is not None:
            self.BotFlowList = []
            for item in params.get("BotFlowList"):
                obj = BotFlow()
                obj._deserialize(item)
                self.BotFlowList.append(obj)
        if params.get("SmsSignList") is not None:
            self.SmsSignList = []
            for item in params.get("SmsSignList"):
                obj = SmsSign()
                obj._deserialize(item)
                self.SmsSignList.append(obj)
        if params.get("SmsTemplateList") is not None:
            self.SmsTemplateList = []
            for item in params.get("SmsTemplateList"):
                obj = SmsTemplate()
                obj._deserialize(item)
                self.SmsTemplateList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCreditResultRequest(AbstractModel):
    """DescribeCreditResult请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，本接口取值：Credit
        :type Module: str
        :param Operation: 操作名，本接口取值：Get
        :type Operation: str
        :param InstId: 实例ID
        :type InstId: str
        :param ProductId: 产品ID，形如P******。
        :type ProductId: str
        :param CaseId: 信审任务ID
        :type CaseId: str
        :param RequestDate: 请求日期，格式为YYYY-MM-DD
        :type RequestDate: str
        """
        self.Module = None
        self.Operation = None
        self.InstId = None
        self.ProductId = None
        self.CaseId = None
        self.RequestDate = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.InstId = params.get("InstId")
        self.ProductId = params.get("ProductId")
        self.CaseId = params.get("CaseId")
        self.RequestDate = params.get("RequestDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCreditResultResponse(AbstractModel):
    """DescribeCreditResult返回参数结构体

    """

    def __init__(self):
        """
        :param ResultCode: <p>呼叫结果，取值范围：</p><ul style="margin-bottom:0px;"><li>NON：接通</li><li>DBU：号码忙</li><li>DRF：不在服务区</li><li>ANA：欠费未接听</li><li>REJ：拒接</li><li>SHU：关机</li><li>NAN：空号</li><li>HAL：停机</li><li>DAD：未接听</li><li>EXE：其他异常</li></ul>
        :type ResultCode: str
        :param ClientCode: 客户标识代码，多个标识码以英文逗号分隔，ResultCode为NON时才有。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientCode: str
        :param RingStartTime: 开始振铃时间，ResultCode为NON或DAD时才有此字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type RingStartTime: str
        :param RingDuration: 振铃时长
        :type RingDuration: int
        :param AnswerDuration: 接通时长
        :type AnswerDuration: int
        :param ContextValue: JSON格式的扩展信息字段，ResultCode为NON时才有。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContextValue: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultCode = None
        self.ClientCode = None
        self.RingStartTime = None
        self.RingDuration = None
        self.AnswerDuration = None
        self.ContextValue = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultCode = params.get("ResultCode")
        self.ClientCode = params.get("ClientCode")
        self.RingStartTime = params.get("RingStartTime")
        self.RingDuration = params.get("RingDuration")
        self.AnswerDuration = params.get("AnswerDuration")
        self.ContextValue = params.get("ContextValue")
        self.RequestId = params.get("RequestId")


class DescribeFileModelRequest(AbstractModel):
    """DescribeFileModel请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param Operation: 操作名。默认值（固定）：DescribeFileModel
        :type Operation: str
        :param FileType: 模板文件类型，输入input，停拨stop
        :type FileType: str
        :param BotId: 任务ID，二者必填一个
        :type BotId: str
        :param BotName: 任务名称，二者必填一个
        :type BotName: str
        """
        self.Module = None
        self.Operation = None
        self.FileType = None
        self.BotId = None
        self.BotName = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.FileType = params.get("FileType")
        self.BotId = params.get("BotId")
        self.BotName = params.get("BotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileModelResponse(AbstractModel):
    """DescribeFileModel返回参数结构体

    """

    def __init__(self):
        """
        :param CosUrl: 模板下载链接
        :type CosUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CosUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CosUrl = params.get("CosUrl")
        self.RequestId = params.get("RequestId")


class DescribeRecordsRequest(AbstractModel):
    """DescribeRecords请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，本接口取值：Record
        :type Module: str
        :param Operation: 操作名，本接口取值：List
        :type Operation: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param AccountNum: 案件编号
        :type AccountNum: str
        :param CalledPhone: 被叫号码
        :type CalledPhone: str
        :param StartBizDate: 查询起始日期，格式为YYYY-MM-DD
        :type StartBizDate: str
        :param EndBizDate: 查询结束日期，格式为YYYY-MM-DD
        :type EndBizDate: str
        :param Offset: 分页参数，索引，默认为0
        :type Offset: str
        :param Limit: 分页参数，页长，默认为20
        :type Limit: str
        :param InstId: 实例ID，不传默认为系统分配的初始实例
        :type InstId: str
        """
        self.Module = None
        self.Operation = None
        self.ProductId = None
        self.AccountNum = None
        self.CalledPhone = None
        self.StartBizDate = None
        self.EndBizDate = None
        self.Offset = None
        self.Limit = None
        self.InstId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ProductId = params.get("ProductId")
        self.AccountNum = params.get("AccountNum")
        self.CalledPhone = params.get("CalledPhone")
        self.StartBizDate = params.get("StartBizDate")
        self.EndBizDate = params.get("EndBizDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstId = params.get("InstId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordsResponse(AbstractModel):
    """DescribeRecords返回参数结构体

    """

    def __init__(self):
        """
        :param RecordList: 录音列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordList: list of SingleRecord
        :param TotalCount: 录音总量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecordList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = SingleRecord()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，本接口取值：Task
        :type Module: str
        :param Operation: 操作名，本接口取值：DescribeTaskStatus
        :type Operation: str
        :param TaskId: 任务ID，"上传文件"接口返回的DataResId，形如abc-xyz123
        :type TaskId: str
        :param InstId: 实例ID，不传默认为系统分配的初始实例。
        :type InstId: str
        """
        self.Module = None
        self.Operation = None
        self.TaskId = None
        self.InstId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.TaskId = params.get("TaskId")
        self.InstId = params.get("InstId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回参数结构体

    """

    def __init__(self):
        """
        :param TaskResult: <p>任务结果：</p><ul style="margin-bottom:0px;"><li>处理中："Uploading Data."</li><li>上传成功："File Uploading Task Success."</li><li>上传失败：具体失败原因</li></ul>
        :type TaskResult: str
        :param TaskType: <p>任务类型：</p><ul style="margin-bottom:0px;"><li>到期/逾期提醒数据上传：002</li><li>到期/逾期提醒停拨数据上传：003</li><li>回访数据上传：004</li><li>回访停拨数据上传：005</li></ul>
        :type TaskType: str
        :param TaskFileUrl: 过滤文件下载链接，有过滤数据时才存在。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskFileUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskResult = None
        self.TaskType = None
        self.TaskFileUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskResult = params.get("TaskResult")
        self.TaskType = params.get("TaskType")
        self.TaskFileUrl = params.get("TaskFileUrl")
        self.RequestId = params.get("RequestId")


class DownloadBotRecordRequest(AbstractModel):
    """DownloadBotRecord请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块：AiApi
        :type Module: str
        :param Operation: 操作：DownloadRecord
        :type Operation: str
        :param BizDate: 业务日期
        :type BizDate: str
        """
        self.Module = None
        self.Operation = None
        self.BizDate = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.BizDate = params.get("BizDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadBotRecordResponse(AbstractModel):
    """DownloadBotRecord返回参数结构体

    """

    def __init__(self):
        """
        :param RecordCosUrl: 录音地址。请求后30分钟内有效
        :type RecordCosUrl: str
        :param TextCosUrl: 文本地址。请求后30分钟内有效
        :type TextCosUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecordCosUrl = None
        self.TextCosUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordCosUrl = params.get("RecordCosUrl")
        self.TextCosUrl = params.get("TextCosUrl")
        self.RequestId = params.get("RequestId")


class DownloadDialogueTextRequest(AbstractModel):
    """DownloadDialogueText请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，本接口取值：Report
        :type Module: str
        :param Operation: 操作名，本接口取值：DownloadTextReport
        :type Operation: str
        :param ReportDate: 报告日期，格式为YYYY-MM-DD
        :type ReportDate: str
        :param InstId: 实例ID
        :type InstId: str
        """
        self.Module = None
        self.Operation = None
        self.ReportDate = None
        self.InstId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ReportDate = params.get("ReportDate")
        self.InstId = params.get("InstId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadDialogueTextResponse(AbstractModel):
    """DownloadDialogueText返回参数结构体

    """

    def __init__(self):
        """
        :param TextReportUrl: 对话文本下载地址
        :type TextReportUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextReportUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TextReportUrl = params.get("TextReportUrl")
        self.RequestId = params.get("RequestId")


class DownloadRecordListRequest(AbstractModel):
    """DownloadRecordList请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，本接口取值：Record
        :type Module: str
        :param Operation: 操作名，本接口取值：DownloadList
        :type Operation: str
        :param BizDate: 录音日期，格式为YYYY-MM-DD
        :type BizDate: str
        :param InstId: 实例ID
        :type InstId: str
        """
        self.Module = None
        self.Operation = None
        self.BizDate = None
        self.InstId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.BizDate = params.get("BizDate")
        self.InstId = params.get("InstId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadRecordListResponse(AbstractModel):
    """DownloadRecordList返回参数结构体

    """

    def __init__(self):
        """
        :param RecordListUrl: 录音列表下载地址
        :type RecordListUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecordListUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordListUrl = params.get("RecordListUrl")
        self.RequestId = params.get("RequestId")


class DownloadReportRequest(AbstractModel):
    """DownloadReport请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，本接口取值：Report
        :type Module: str
        :param Operation: 操作名，本接口取值：DownloadReport
        :type Operation: str
        :param ReportDate: 报告日期，格式为YYYY-MM-DD
        :type ReportDate: str
        :param InstId: 实例ID，不传默认为系统分配的初始实例。
        :type InstId: str
        """
        self.Module = None
        self.Operation = None
        self.ReportDate = None
        self.InstId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ReportDate = params.get("ReportDate")
        self.InstId = params.get("InstId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadReportResponse(AbstractModel):
    """DownloadReport返回参数结构体

    """

    def __init__(self):
        """
        :param DailyReportUrl: 到期/逾期提醒日报下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DailyReportUrl: str
        :param ResultReportUrl: 到期/逾期提醒结果下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultReportUrl: str
        :param DetailReportUrl: 到期/逾期提醒明细下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailReportUrl: str
        :param CallbackDailyReportUrl: 回访日报下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackDailyReportUrl: str
        :param CallbackResultReportUrl: 回访结果下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackResultReportUrl: str
        :param CallbackDetailReportUrl: 回访明细下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackDetailReportUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DailyReportUrl = None
        self.ResultReportUrl = None
        self.DetailReportUrl = None
        self.CallbackDailyReportUrl = None
        self.CallbackResultReportUrl = None
        self.CallbackDetailReportUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DailyReportUrl = params.get("DailyReportUrl")
        self.ResultReportUrl = params.get("ResultReportUrl")
        self.DetailReportUrl = params.get("DetailReportUrl")
        self.CallbackDailyReportUrl = params.get("CallbackDailyReportUrl")
        self.CallbackResultReportUrl = params.get("CallbackResultReportUrl")
        self.CallbackDetailReportUrl = params.get("CallbackDetailReportUrl")
        self.RequestId = params.get("RequestId")


class ExportBotDataRequest(AbstractModel):
    """ExportBotData请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param Operation: 操作名。默认值（固定）：ExportBotData
        :type Operation: str
        :param BizDate: 业务日期。YYYY-MM-DD
        :type BizDate: str
        :param BotId: 任务ID，二者必填一个
        :type BotId: str
        :param BotName: 任务名称，二者必填一个
        :type BotName: str
        """
        self.Module = None
        self.Operation = None
        self.BizDate = None
        self.BotId = None
        self.BotName = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.BizDate = params.get("BizDate")
        self.BotId = params.get("BotId")
        self.BotName = params.get("BotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportBotDataResponse(AbstractModel):
    """ExportBotData返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 导出文件列表
        :type Data: list of BotFileData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = BotFileData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class PhonePool(AbstractModel):
    """号码组信息

    """

    def __init__(self):
        """
        :param PoolId: 号码组ID
        :type PoolId: str
        :param PoolName: 号码组名称
        :type PoolName: str
        """
        self.PoolId = None
        self.PoolName = None


    def _deserialize(self, params):
        self.PoolId = params.get("PoolId")
        self.PoolName = params.get("PoolName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductQueryInfo(AbstractModel):
    """QueryProducts接口对应数据结构。产品对应的相关信息。

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param ProductName: 产品名称
        :type ProductName: str
        :param ProductCode: 产品编码
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCode: str
        :param ProductStatus: 产品状态 0 禁用 1 启用
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductStatus: int
        :param SceneType: 场景类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneType: str
        """
        self.ProductId = None
        self.ProductName = None
        self.ProductCode = None
        self.ProductStatus = None
        self.SceneType = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.ProductCode = params.get("ProductCode")
        self.ProductStatus = params.get("ProductStatus")
        self.SceneType = params.get("SceneType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBlackListDataRequest(AbstractModel):
    """QueryBlackListData请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块:AiApi
        :type Module: str
        :param Operation: 操作:QueryBlackListData
        :type Operation: str
        :param Offset: 页码
        :type Offset: int
        :param Limit: 每页数量
        :type Limit: int
        :param StartBizDate: 开始日期
        :type StartBizDate: str
        :param EndBizDate: 结束日期
        :type EndBizDate: str
        :param BlackValue: 电话号码、手机
        :type BlackValue: str
        """
        self.Module = None
        self.Operation = None
        self.Offset = None
        self.Limit = None
        self.StartBizDate = None
        self.EndBizDate = None
        self.BlackValue = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.StartBizDate = params.get("StartBizDate")
        self.EndBizDate = params.get("EndBizDate")
        self.BlackValue = params.get("BlackValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBlackListDataResponse(AbstractModel):
    """QueryBlackListData返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数。
        :type TotalCount: int
        :param Data: 黑名单列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of BlackListData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = BlackListData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class QueryBotListRequest(AbstractModel):
    """QueryBotList请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名：AiApi
        :type Module: str
        :param Operation: 操作名：QueryBotList
        :type Operation: str
        """
        self.Module = None
        self.Operation = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBotListResponse(AbstractModel):
    """QueryBotList返回参数结构体

    """

    def __init__(self):
        """
        :param BotList: 任务列表。
        :type BotList: list of BotInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BotList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BotList") is not None:
            self.BotList = []
            for item in params.get("BotList"):
                obj = BotInfo()
                obj._deserialize(item)
                self.BotList.append(obj)
        self.RequestId = params.get("RequestId")


class QueryCallListRequest(AbstractModel):
    """QueryCallList请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param Operation: 操作名。默认值（固定）：QueryCallList
        :type Operation: str
        :param BizDate: 业务日期
        :type BizDate: str
        :param BotId: 任务ID，二者必填一个
        :type BotId: str
        :param BotName: 任务名称，二者必填一个
        :type BotName: str
        :param FileName: 通过API或平台上传的文件完整名称
        :type FileName: str
        """
        self.Module = None
        self.Operation = None
        self.BizDate = None
        self.BotId = None
        self.BotName = None
        self.FileName = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.BizDate = params.get("BizDate")
        self.BotId = params.get("BotId")
        self.BotName = params.get("BotName")
        self.FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCallListResponse(AbstractModel):
    """QueryCallList返回参数结构体

    """

    def __init__(self):
        """
        :param CallList: 任务作业状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CallList: list of CallInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CallList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CallList") is not None:
            self.CallList = []
            for item in params.get("CallList"):
                obj = CallInfo()
                obj._deserialize(item)
                self.CallList.append(obj)
        self.RequestId = params.get("RequestId")


class QueryInstantDataRequest(AbstractModel):
    """QueryInstantData请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，本接口取值：Data
        :type Module: str
        :param Operation: 操作名，本接口取值：Query
        :type Operation: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param InstanceId: 实例ID，不传默认为系统分配的初始实例
        :type InstanceId: str
        :param QueryModel: 查询类型：callRecord 通话记录
        :type QueryModel: str
        :param Data: 查询参数
        :type Data: str
        """
        self.Module = None
        self.Operation = None
        self.ProductId = None
        self.InstanceId = None
        self.QueryModel = None
        self.Data = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ProductId = params.get("ProductId")
        self.InstanceId = params.get("InstanceId")
        self.QueryModel = params.get("QueryModel")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryInstantDataResponse(AbstractModel):
    """QueryInstantData返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Data: 返回内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class QueryProductsRequest(AbstractModel):
    """QueryProducts请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名。默认值（固定）：Product
        :type Module: str
        :param Operation: 操作名。默认值（固定）：QueryProducts
        :type Operation: str
        :param InstanceId: 实例Id。
        :type InstanceId: str
        """
        self.Module = None
        self.Operation = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryProductsResponse(AbstractModel):
    """QueryProducts返回参数结构体

    """

    def __init__(self):
        """
        :param ProductList: 产品信息。
        :type ProductList: list of ProductQueryInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProductList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProductList") is not None:
            self.ProductList = []
            for item in params.get("ProductList"):
                obj = ProductQueryInfo()
                obj._deserialize(item)
                self.ProductList.append(obj)
        self.RequestId = params.get("RequestId")


class QueryRecordListRequest(AbstractModel):
    """QueryRecordList请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名。AiApi
        :type Module: str
        :param Operation: 操作名。QueryRecordList
        :type Operation: str
        :param Offset: 偏移值
        :type Offset: int
        :param Limit: 偏移位移，最大20
        :type Limit: int
        :param BotId: 任务ID，二者必填一个
        :type BotId: str
        :param BotName: 任务名称，二者必填一个
        :type BotName: str
        :param CalledPhone: 被叫号码
        :type CalledPhone: str
        :param StartBizDate: 开始日期
        :type StartBizDate: str
        :param EndBizDate: 结束日期
        :type EndBizDate: str
        """
        self.Module = None
        self.Operation = None
        self.Offset = None
        self.Limit = None
        self.BotId = None
        self.BotName = None
        self.CalledPhone = None
        self.StartBizDate = None
        self.EndBizDate = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.BotId = params.get("BotId")
        self.BotName = params.get("BotName")
        self.CalledPhone = params.get("CalledPhone")
        self.StartBizDate = params.get("StartBizDate")
        self.EndBizDate = params.get("EndBizDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryRecordListResponse(AbstractModel):
    """QueryRecordList返回参数结构体

    """

    def __init__(self):
        """
        :param RecordList: 录音列表。
        :type RecordList: list of RecordInfo
        :param TotalCount: 总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecordList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = RecordInfo()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class RecordInfo(AbstractModel):
    """录音文件详情

    """

    def __init__(self):
        """
        :param BotId: 任务Id
        :type BotId: str
        :param BotName: 任务名称
        :type BotName: str
        :param BizDate: 任务日期
        :type BizDate: str
        :param CalledPhone: 被叫号码
        :type CalledPhone: str
        :param CallStartTime: 开始通话时间
        :type CallStartTime: str
        :param Duration: 通话时长
        :type Duration: int
        :param CosUrl: 录音文件地址
        :type CosUrl: str
        :param DialogueLog: 对话日志。JSON格式
        :type DialogueLog: str
        :param CosFileName: 录音文件名
        :type CosFileName: str
        """
        self.BotId = None
        self.BotName = None
        self.BizDate = None
        self.CalledPhone = None
        self.CallStartTime = None
        self.Duration = None
        self.CosUrl = None
        self.DialogueLog = None
        self.CosFileName = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.BotName = params.get("BotName")
        self.BizDate = params.get("BizDate")
        self.CalledPhone = params.get("CalledPhone")
        self.CallStartTime = params.get("CallStartTime")
        self.Duration = params.get("Duration")
        self.CosUrl = params.get("CosUrl")
        self.DialogueLog = params.get("DialogueLog")
        self.CosFileName = params.get("CosFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SingleBlackApply(AbstractModel):
    """黑名单申请信息

    """

    def __init__(self):
        """
        :param BlackType: 黑名单类型，01代表手机号码。
        :type BlackType: str
        :param OperationType: 操作类型，A为新增，D为删除。
        :type OperationType: str
        :param BlackValue: 黑名单值，BlackType为01时，填写11位手机号码。
        :type BlackValue: str
        :param BlackDescription: 备注。
        :type BlackDescription: str
        :param BlackValidDate: 黑名单生效截止日期，格式为YYYY-MM-DD，不填默认为永久。
        :type BlackValidDate: str
        """
        self.BlackType = None
        self.OperationType = None
        self.BlackValue = None
        self.BlackDescription = None
        self.BlackValidDate = None


    def _deserialize(self, params):
        self.BlackType = params.get("BlackType")
        self.OperationType = params.get("OperationType")
        self.BlackValue = params.get("BlackValue")
        self.BlackDescription = params.get("BlackDescription")
        self.BlackValidDate = params.get("BlackValidDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SingleRecord(AbstractModel):
    """录音信息

    """

    def __init__(self):
        """
        :param AccountNum: 案件编号。
        :type AccountNum: str
        :param BizDate: 外呼日期。
        :type BizDate: str
        :param CallStartTime: 开始呼叫时间。
        :type CallStartTime: str
        :param CallerPhone: 主叫号码。
        :type CallerPhone: str
        :param Direction: 呼叫方向，O为呼出，I为呼入。
        :type Direction: str
        :param Duration: 通话时长。
        :type Duration: int
        :param ProductId: 产品ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param RecordCosUrl: 录音下载链接。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordCosUrl: str
        """
        self.AccountNum = None
        self.BizDate = None
        self.CallStartTime = None
        self.CallerPhone = None
        self.Direction = None
        self.Duration = None
        self.ProductId = None
        self.RecordCosUrl = None


    def _deserialize(self, params):
        self.AccountNum = params.get("AccountNum")
        self.BizDate = params.get("BizDate")
        self.CallStartTime = params.get("CallStartTime")
        self.CallerPhone = params.get("CallerPhone")
        self.Direction = params.get("Direction")
        self.Duration = params.get("Duration")
        self.ProductId = params.get("ProductId")
        self.RecordCosUrl = params.get("RecordCosUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsSign(AbstractModel):
    """短信签名信息

    """

    def __init__(self):
        """
        :param SignId: 短信签名ID
        :type SignId: str
        :param SignName: 短信签名名称
        :type SignName: str
        """
        self.SignId = None
        self.SignName = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.SignName = params.get("SignName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsTemplate(AbstractModel):
    """短信模板信息

    """

    def __init__(self):
        """
        :param TemplateId: 短信模板ID
        :type TemplateId: str
        :param TemplateName: 短信模板名称
        :type TemplateName: str
        """
        self.TemplateId = None
        self.TemplateName = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateBotTaskRequest(AbstractModel):
    """UpdateBotTask请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param Operation: 操作名。默认值（固定）：UpdateTask
        :type Operation: str
        :param BotName: 任务名称
        :type BotName: str
        :param BotId: 任务ID
        :type BotId: str
        :param CallTimeCollection: 产品拨打时间集合
        :type CallTimeCollection: :class:`tencentcloud.cr.v20180321.models.CallTimeDict`
        :param BanCall: 是否禁止拨打，默认Y
        :type BanCall: str
        :param StartTimeBan: 禁止拨打起始时间。默认130000
        :type StartTimeBan: str
        :param EndTimeBan: 禁止拨打结束时间。默认140000
        :type EndTimeBan: str
        :param PhoneCollection: 拨打线路集合
        :type PhoneCollection: str
        :param CodeType: 重播方式，NON：未接通、LABEL：意向分级，可多选，用竖线分隔：NON|LABEL
        :type CodeType: str
        :param CodeCollection: 重播值集合，A：强意向、B：中意向、C：低意向、D：无意向、E：在忙、F：未接通、G：无效号码，可多选，用竖线分隔：A|B|C|D|E|F|G
        :type CodeCollection: str
        :param CallCount: 继续拨打次数
        :type CallCount: int
        :param CallInterval: 拨打间隔
        :type CallInterval: int
        :param SmsSignId: 未接通引用短信签名ID
        :type SmsSignId: str
        :param SmsTemplateId: 未接通引用短信模板ID
        :type SmsTemplateId: str
        """
        self.Module = None
        self.Operation = None
        self.BotName = None
        self.BotId = None
        self.CallTimeCollection = None
        self.BanCall = None
        self.StartTimeBan = None
        self.EndTimeBan = None
        self.PhoneCollection = None
        self.CodeType = None
        self.CodeCollection = None
        self.CallCount = None
        self.CallInterval = None
        self.SmsSignId = None
        self.SmsTemplateId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.BotName = params.get("BotName")
        self.BotId = params.get("BotId")
        if params.get("CallTimeCollection") is not None:
            self.CallTimeCollection = CallTimeDict()
            self.CallTimeCollection._deserialize(params.get("CallTimeCollection"))
        self.BanCall = params.get("BanCall")
        self.StartTimeBan = params.get("StartTimeBan")
        self.EndTimeBan = params.get("EndTimeBan")
        self.PhoneCollection = params.get("PhoneCollection")
        self.CodeType = params.get("CodeType")
        self.CodeCollection = params.get("CodeCollection")
        self.CallCount = params.get("CallCount")
        self.CallInterval = params.get("CallInterval")
        self.SmsSignId = params.get("SmsSignId")
        self.SmsTemplateId = params.get("SmsTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateBotTaskResponse(AbstractModel):
    """UpdateBotTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UploadBotDataRequest(AbstractModel):
    """UploadBotData请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param Operation: 操作名。默认值（固定）：UploadData
        :type Operation: str
        :param Data: 任务数据。JSON格式
        :type Data: str
        :param BotId: 任务ID，二者必填一个
        :type BotId: str
        :param BotName: 任务名称，二者必填一个
        :type BotName: str
        """
        self.Module = None
        self.Operation = None
        self.Data = None
        self.BotId = None
        self.BotName = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.Data = params.get("Data")
        self.BotId = params.get("BotId")
        self.BotName = params.get("BotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadBotDataResponse(AbstractModel):
    """UploadBotData返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UploadBotFileRequest(AbstractModel):
    """UploadBotFile请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param Operation: 操作名。默认值（固定）：Upload
        :type Operation: str
        :param FileType: 文件类型，输入input，停拨stop
        :type FileType: str
        :param FileUrl: 文件链接
        :type FileUrl: str
        :param FileName: 文件名
        :type FileName: str
        :param BotId: 任务ID，二者必填一个
        :type BotId: str
        :param BotName: 任务名称，二者必填一个
        :type BotName: str
        """
        self.Module = None
        self.Operation = None
        self.FileType = None
        self.FileUrl = None
        self.FileName = None
        self.BotId = None
        self.BotName = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.FileType = params.get("FileType")
        self.FileUrl = params.get("FileUrl")
        self.FileName = params.get("FileName")
        self.BotId = params.get("BotId")
        self.BotName = params.get("BotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadBotFileResponse(AbstractModel):
    """UploadBotFile返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UploadDataFileRequest(AbstractModel):
    """UploadDataFile请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，本接口取值：Data
        :type Module: str
        :param Operation: 操作名，本接口取值：Upload
        :type Operation: str
        :param FileName: 文件名
        :type FileName: str
        :param UploadModel: <p>上传类型，不填默认到期/逾期提醒文件，取值范围：</p><ul style="margin-bottom:0px;"><li>data：到期/逾期提醒文件</li><li>repay：到期/逾期提醒停拨文件</li><li>callback：回访文件</li><li>callstop：回访停拨文件</li><li>blacklist：黑名单文件</li></ul>
        :type UploadModel: str
        :param File: 文件，文件与文件地址上传只可选用一种，必须使用multipart/form-data协议来上传二进制流文件，建议使用xlsx格式，大小不超过5MB。
        :type File: binary
        :param FileUrl: 文件上传地址，文件与文件地址上传只可选用一种，大小不超过50MB。
        :type FileUrl: str
        :param InstId: 实例ID，不传默认为系统分配的初始实例。
        :type InstId: str
        """
        self.Module = None
        self.Operation = None
        self.FileName = None
        self.UploadModel = None
        self.File = None
        self.FileUrl = None
        self.InstId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.FileName = params.get("FileName")
        self.UploadModel = params.get("UploadModel")
        self.File = params.get("File")
        self.FileUrl = params.get("FileUrl")
        self.InstId = params.get("InstId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadDataFileResponse(AbstractModel):
    """UploadDataFile返回参数结构体

    """

    def __init__(self):
        """
        :param DataResId: 数据ID
        :type DataResId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataResId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DataResId = params.get("DataResId")
        self.RequestId = params.get("RequestId")


class UploadDataJsonRequest(AbstractModel):
    """UploadDataJson请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名，本接口取值：Data
        :type Module: str
        :param Operation: 操作名，本接口取值：UploadJson
        :type Operation: str
        :param Data: 报文信息
        :type Data: str
        :param UploadModel: <p>上传类型，不填默认到期/逾期提醒数据，取值范围：</p><ul style="margin-bottom:0px;"><li>data：到期/逾期提醒数据</li><li>repay：到期/逾期提醒停拨数据</li></ul>
        :type UploadModel: str
        :param InstanceId: 实例ID，不传默认为系统分配的初始实例。
        :type InstanceId: str
        """
        self.Module = None
        self.Operation = None
        self.Data = None
        self.UploadModel = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.Data = params.get("Data")
        self.UploadModel = params.get("UploadModel")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadDataJsonResponse(AbstractModel):
    """UploadDataJson返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 响应报文信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class UploadFileRequest(AbstractModel):
    """UploadFile请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名
        :type Module: str
        :param Operation: 操作名
        :type Operation: str
        :param FileUrl: 文件上传地址，要求地址协议为HTTPS，且URL端口必须为443
        :type FileUrl: str
        :param FileName: 文件名
        :type FileName: str
        :param FileDate: 文件日期
        :type FileDate: str
        """
        self.Module = None
        self.Operation = None
        self.FileUrl = None
        self.FileName = None
        self.FileDate = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.FileUrl = params.get("FileUrl")
        self.FileName = params.get("FileName")
        self.FileDate = params.get("FileDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFileResponse(AbstractModel):
    """UploadFile返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")