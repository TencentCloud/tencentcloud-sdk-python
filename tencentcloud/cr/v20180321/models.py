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
        r"""
        :param _Module: 模块名，AiApi
        :type Module: str
        :param _Operation: 操作名，ApplyBlackListData
        :type Operation: str
        :param _BlackList: 黑名单列表
        :type BlackList: list of BlackListData
        """
        self._Module = None
        self._Operation = None
        self._BlackList = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def BlackList(self):
        return self._BlackList

    @BlackList.setter
    def BlackList(self, BlackList):
        self._BlackList = BlackList


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        if params.get("BlackList") is not None:
            self._BlackList = []
            for item in params.get("BlackList"):
                obj = BlackListData()
                obj._deserialize(item)
                self._BlackList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyBlackListDataResponse(AbstractModel):
    """ApplyBlackListData返回参数结构体

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


class ApplyBlackListRequest(AbstractModel):
    """ApplyBlackList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：account
        :type Module: str
        :param _Operation: 操作名，本接口取值：ApplyBlackList
        :type Operation: str
        :param _BlackList: 黑名单列表
        :type BlackList: list of SingleBlackApply
        :param _InstId: 实例ID，不传默认为系统分配的初始实例
        :type InstId: str
        """
        self._Module = None
        self._Operation = None
        self._BlackList = None
        self._InstId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def BlackList(self):
        return self._BlackList

    @BlackList.setter
    def BlackList(self, BlackList):
        self._BlackList = BlackList

    @property
    def InstId(self):
        return self._InstId

    @InstId.setter
    def InstId(self, InstId):
        self._InstId = InstId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        if params.get("BlackList") is not None:
            self._BlackList = []
            for item in params.get("BlackList"):
                obj = SingleBlackApply()
                obj._deserialize(item)
                self._BlackList.append(obj)
        self._InstId = params.get("InstId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyBlackListResponse(AbstractModel):
    """ApplyBlackList返回参数结构体

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


class ApplyCreditAuditRequest(AbstractModel):
    """ApplyCreditAudit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：Credit
        :type Module: str
        :param _Operation: 操作名，本接口取值：Apply
        :type Operation: str
        :param _InstId: 实例ID
        :type InstId: str
        :param _ProductId: 产品ID，形如P******。
        :type ProductId: str
        :param _CaseId: 信审任务ID，同一天内，同一InstId下，同一CaseId只能调用一次。
        :type CaseId: str
        :param _CallbackUrl: 回调地址
        :type CallbackUrl: str
        :param _Data: JSON格式的业务字段。
        :type Data: str
        """
        self._Module = None
        self._Operation = None
        self._InstId = None
        self._ProductId = None
        self._CaseId = None
        self._CallbackUrl = None
        self._Data = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def InstId(self):
        return self._InstId

    @InstId.setter
    def InstId(self, InstId):
        self._InstId = InstId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def CaseId(self):
        return self._CaseId

    @CaseId.setter
    def CaseId(self, CaseId):
        self._CaseId = CaseId

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._InstId = params.get("InstId")
        self._ProductId = params.get("ProductId")
        self._CaseId = params.get("CaseId")
        self._CallbackUrl = params.get("CallbackUrl")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyCreditAuditResponse(AbstractModel):
    """ApplyCreditAudit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestDate: 请求日期
        :type RequestDate: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestDate = None
        self._RequestId = None

    @property
    def RequestDate(self):
        return self._RequestDate

    @RequestDate.setter
    def RequestDate(self, RequestDate):
        self._RequestDate = RequestDate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestDate = params.get("RequestDate")
        self._RequestId = params.get("RequestId")


class BlackListData(AbstractModel):
    """黑名单申请信息

    """

    def __init__(self):
        r"""
        :param _BlackType: 黑名单类型，01代表手机号码。
        :type BlackType: str
        :param _OperType: 操作类型，A为新增，D为删除。
注意：此字段可能返回 null，表示取不到有效值。
        :type OperType: str
        :param _BlackValue: 黑名单值，BlackType为01时，填写11位手机号码。
        :type BlackValue: str
        :param _BlackDescription: 备注。
注意：此字段可能返回 null，表示取不到有效值。
        :type BlackDescription: str
        :param _BlackValidDate: 黑名单生效截止日期，格式为YYYY-MM-DD，不填默认为永久。
注意：此字段可能返回 null，表示取不到有效值。
        :type BlackValidDate: str
        :param _BlackAddDate: 黑名单加入日期
注意：此字段可能返回 null，表示取不到有效值。
        :type BlackAddDate: str
        :param _BlackStatus: 0-生效 1-失效
        :type BlackStatus: str
        """
        self._BlackType = None
        self._OperType = None
        self._BlackValue = None
        self._BlackDescription = None
        self._BlackValidDate = None
        self._BlackAddDate = None
        self._BlackStatus = None

    @property
    def BlackType(self):
        return self._BlackType

    @BlackType.setter
    def BlackType(self, BlackType):
        self._BlackType = BlackType

    @property
    def OperType(self):
        return self._OperType

    @OperType.setter
    def OperType(self, OperType):
        self._OperType = OperType

    @property
    def BlackValue(self):
        return self._BlackValue

    @BlackValue.setter
    def BlackValue(self, BlackValue):
        self._BlackValue = BlackValue

    @property
    def BlackDescription(self):
        return self._BlackDescription

    @BlackDescription.setter
    def BlackDescription(self, BlackDescription):
        self._BlackDescription = BlackDescription

    @property
    def BlackValidDate(self):
        return self._BlackValidDate

    @BlackValidDate.setter
    def BlackValidDate(self, BlackValidDate):
        self._BlackValidDate = BlackValidDate

    @property
    def BlackAddDate(self):
        return self._BlackAddDate

    @BlackAddDate.setter
    def BlackAddDate(self, BlackAddDate):
        self._BlackAddDate = BlackAddDate

    @property
    def BlackStatus(self):
        return self._BlackStatus

    @BlackStatus.setter
    def BlackStatus(self, BlackStatus):
        self._BlackStatus = BlackStatus


    def _deserialize(self, params):
        self._BlackType = params.get("BlackType")
        self._OperType = params.get("OperType")
        self._BlackValue = params.get("BlackValue")
        self._BlackDescription = params.get("BlackDescription")
        self._BlackValidDate = params.get("BlackValidDate")
        self._BlackAddDate = params.get("BlackAddDate")
        self._BlackStatus = params.get("BlackStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotFileData(AbstractModel):
    """机器人文件结构

    """

    def __init__(self):
        r"""
        :param _FileType: 文件类型 A 拨打结果 T 记录详情
        :type FileType: str
        :param _CosUrl: 文件地址
        :type CosUrl: str
        """
        self._FileType = None
        self._CosUrl = None

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CosUrl(self):
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._CosUrl = params.get("CosUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotFlow(AbstractModel):
    """机器人对话流信息

    """

    def __init__(self):
        r"""
        :param _BotFlowId: 对话流ID
        :type BotFlowId: str
        :param _BotFlowName: 对话流名称
        :type BotFlowName: str
        :param _PhonePoolList: 号码组信息列表
        :type PhonePoolList: list of PhonePool
        """
        self._BotFlowId = None
        self._BotFlowName = None
        self._PhonePoolList = None

    @property
    def BotFlowId(self):
        return self._BotFlowId

    @BotFlowId.setter
    def BotFlowId(self, BotFlowId):
        self._BotFlowId = BotFlowId

    @property
    def BotFlowName(self):
        return self._BotFlowName

    @BotFlowName.setter
    def BotFlowName(self, BotFlowName):
        self._BotFlowName = BotFlowName

    @property
    def PhonePoolList(self):
        return self._PhonePoolList

    @PhonePoolList.setter
    def PhonePoolList(self, PhonePoolList):
        self._PhonePoolList = PhonePoolList


    def _deserialize(self, params):
        self._BotFlowId = params.get("BotFlowId")
        self._BotFlowName = params.get("BotFlowName")
        if params.get("PhonePoolList") is not None:
            self._PhonePoolList = []
            for item in params.get("PhonePoolList"):
                obj = PhonePool()
                obj._deserialize(item)
                self._PhonePoolList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotInfo(AbstractModel):
    """机器人列表

    """

    def __init__(self):
        r"""
        :param _BotId: 机器人ID
        :type BotId: str
        :param _BotName: 机器人名称
        :type BotName: str
        :param _BotStatus: 机器人状态。0-停用 1-启用 2-待审核
        :type BotStatus: str
        """
        self._BotId = None
        self._BotName = None
        self._BotStatus = None

    @property
    def BotId(self):
        return self._BotId

    @BotId.setter
    def BotId(self, BotId):
        self._BotId = BotId

    @property
    def BotName(self):
        return self._BotName

    @BotName.setter
    def BotName(self, BotName):
        self._BotName = BotName

    @property
    def BotStatus(self):
        return self._BotStatus

    @BotStatus.setter
    def BotStatus(self, BotStatus):
        self._BotStatus = BotStatus


    def _deserialize(self, params):
        self._BotId = params.get("BotId")
        self._BotName = params.get("BotName")
        self._BotStatus = params.get("BotStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallInfo(AbstractModel):
    """作业信息

    """

    def __init__(self):
        r"""
        :param _BizDate: 业务日期
        :type BizDate: str
        :param _Status: 状态 WAIT：待执行；DOING：执行中；ERROR：执行错误；DONE：已完成；
        :type Status: str
        :param _TotalCount: 成功总数
        :type TotalCount: int
        :param _FileName: 文件名称
        :type FileName: str
        :param _FileType: 文件类型 I：呼叫文件 R：停拨文件
        :type FileType: str
        :param _CallId: 作业唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type CallId: str
        """
        self._BizDate = None
        self._Status = None
        self._TotalCount = None
        self._FileName = None
        self._FileType = None
        self._CallId = None

    @property
    def BizDate(self):
        return self._BizDate

    @BizDate.setter
    def BizDate(self, BizDate):
        self._BizDate = BizDate

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
    def CallId(self):
        return self._CallId

    @CallId.setter
    def CallId(self, CallId):
        self._CallId = CallId


    def _deserialize(self, params):
        self._BizDate = params.get("BizDate")
        self._Status = params.get("Status")
        self._TotalCount = params.get("TotalCount")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._CallId = params.get("CallId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallTimeDict(AbstractModel):
    """产品拨打时间集合

    """

    def __init__(self):
        r"""
        :param _Monday: 周一
        :type Monday: :class:`tencentcloud.cr.v20180321.models.CallTimeInfo`
        :param _Tuesday: 周二
        :type Tuesday: :class:`tencentcloud.cr.v20180321.models.CallTimeInfo`
        :param _Wednesday: 周三
        :type Wednesday: :class:`tencentcloud.cr.v20180321.models.CallTimeInfo`
        :param _Thursday: 周四
        :type Thursday: :class:`tencentcloud.cr.v20180321.models.CallTimeInfo`
        :param _Friday: 周五
        :type Friday: :class:`tencentcloud.cr.v20180321.models.CallTimeInfo`
        :param _Saturday: 周六
        :type Saturday: :class:`tencentcloud.cr.v20180321.models.CallTimeInfo`
        :param _Sunday: 周日
        :type Sunday: :class:`tencentcloud.cr.v20180321.models.CallTimeInfo`
        """
        self._Monday = None
        self._Tuesday = None
        self._Wednesday = None
        self._Thursday = None
        self._Friday = None
        self._Saturday = None
        self._Sunday = None

    @property
    def Monday(self):
        return self._Monday

    @Monday.setter
    def Monday(self, Monday):
        self._Monday = Monday

    @property
    def Tuesday(self):
        return self._Tuesday

    @Tuesday.setter
    def Tuesday(self, Tuesday):
        self._Tuesday = Tuesday

    @property
    def Wednesday(self):
        return self._Wednesday

    @Wednesday.setter
    def Wednesday(self, Wednesday):
        self._Wednesday = Wednesday

    @property
    def Thursday(self):
        return self._Thursday

    @Thursday.setter
    def Thursday(self, Thursday):
        self._Thursday = Thursday

    @property
    def Friday(self):
        return self._Friday

    @Friday.setter
    def Friday(self, Friday):
        self._Friday = Friday

    @property
    def Saturday(self):
        return self._Saturday

    @Saturday.setter
    def Saturday(self, Saturday):
        self._Saturday = Saturday

    @property
    def Sunday(self):
        return self._Sunday

    @Sunday.setter
    def Sunday(self, Sunday):
        self._Sunday = Sunday


    def _deserialize(self, params):
        if params.get("Monday") is not None:
            self._Monday = CallTimeInfo()
            self._Monday._deserialize(params.get("Monday"))
        if params.get("Tuesday") is not None:
            self._Tuesday = CallTimeInfo()
            self._Tuesday._deserialize(params.get("Tuesday"))
        if params.get("Wednesday") is not None:
            self._Wednesday = CallTimeInfo()
            self._Wednesday._deserialize(params.get("Wednesday"))
        if params.get("Thursday") is not None:
            self._Thursday = CallTimeInfo()
            self._Thursday._deserialize(params.get("Thursday"))
        if params.get("Friday") is not None:
            self._Friday = CallTimeInfo()
            self._Friday._deserialize(params.get("Friday"))
        if params.get("Saturday") is not None:
            self._Saturday = CallTimeInfo()
            self._Saturday._deserialize(params.get("Saturday"))
        if params.get("Sunday") is not None:
            self._Sunday = CallTimeInfo()
            self._Sunday._deserialize(params.get("Sunday"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallTimeInfo(AbstractModel):
    """产品拨打时间信息

    """

    def __init__(self):
        r"""
        :param _StartTime: 产品开始拨打时间，HHmmss格式,默认090000
        :type StartTime: str
        :param _EndTime: 产品结束拨打时间，HHmmss格式.默认200000
        :type EndTime: str
        """
        self._StartTime = None
        self._EndTime = None

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


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeBotCallStatusRequest(AbstractModel):
    """ChangeBotCallStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param _Operation: 操作名。默认值（固定）：ChangeBotCallStatus
        :type Operation: str
        :param _Status: 作业变更状态
SUSPEND：暂停；EXECUTE：恢复；
        :type Status: str
        :param _CallId: 作业唯一标识
        :type CallId: str
        :param _BizDate: 业务日期
        :type BizDate: str
        :param _BotId: 任务ID，二者必填一个
        :type BotId: str
        :param _BotName: 任务名称，二者必填一个
        :type BotName: str
        """
        self._Module = None
        self._Operation = None
        self._Status = None
        self._CallId = None
        self._BizDate = None
        self._BotId = None
        self._BotName = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CallId(self):
        return self._CallId

    @CallId.setter
    def CallId(self, CallId):
        self._CallId = CallId

    @property
    def BizDate(self):
        return self._BizDate

    @BizDate.setter
    def BizDate(self, BizDate):
        self._BizDate = BizDate

    @property
    def BotId(self):
        return self._BotId

    @BotId.setter
    def BotId(self, BotId):
        self._BotId = BotId

    @property
    def BotName(self):
        return self._BotName

    @BotName.setter
    def BotName(self, BotName):
        self._BotName = BotName


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._Status = params.get("Status")
        self._CallId = params.get("CallId")
        self._BizDate = params.get("BizDate")
        self._BotId = params.get("BotId")
        self._BotName = params.get("BotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeBotCallStatusResponse(AbstractModel):
    """ChangeBotCallStatus返回参数结构体

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


class ChangeBotTaskStatusRequest(AbstractModel):
    """ChangeBotTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param _Operation: 操作名。默认值（固定）：ChangeBotTaskStatus
        :type Operation: str
        :param _Status: 作业变更状态
SUSPEND：暂停；EXECUTE：恢复；
        :type Status: str
        :param _BotId: 任务ID，二者必填一个
        :type BotId: str
        :param _BotName: 任务名称，二者必填一个
        :type BotName: str
        """
        self._Module = None
        self._Operation = None
        self._Status = None
        self._BotId = None
        self._BotName = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BotId(self):
        return self._BotId

    @BotId.setter
    def BotId(self, BotId):
        self._BotId = BotId

    @property
    def BotName(self):
        return self._BotName

    @BotName.setter
    def BotName(self, BotName):
        self._BotName = BotName


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._Status = params.get("Status")
        self._BotId = params.get("BotId")
        self._BotName = params.get("BotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeBotTaskStatusResponse(AbstractModel):
    """ChangeBotTaskStatus返回参数结构体

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


class CreateBotTaskRequest(AbstractModel):
    """CreateBotTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param _Operation: 操作名。默认值（固定）：CreateTask
        :type Operation: str
        :param _BotName: 任务名称
        :type BotName: str
        :param _FlowId: 对话流ID
        :type FlowId: str
        :param _BanCall: 是否禁止拨打，默认Y
        :type BanCall: str
        :param _PhoneCollection: 拨打线路集合
        :type PhoneCollection: str
        :param _CallTimeCollection: 产品拨打时间集合
        :type CallTimeCollection: :class:`tencentcloud.cr.v20180321.models.CallTimeDict`
        :param _StartTimeBan: 禁止拨打起始时间。默认130000
        :type StartTimeBan: str
        :param _EndTimeBan: 禁止拨打结束时间。默认140000
        :type EndTimeBan: str
        :param _CodeType: 重播方式，NON：未接通、LABEL：意向分级，可多选，用竖线分隔：NON|LABEL
        :type CodeType: str
        :param _CodeCollection: 重播值集合，A：强意向、B：中意向、C：低意向、D：无意向、E：在忙、F：未接通、G：无效号码，可多选，用竖线分隔：A|B|C|D|E|F|G
        :type CodeCollection: str
        :param _CallCount: 继续拨打次数
        :type CallCount: int
        :param _CallInterval: 拨打间隔
        :type CallInterval: int
        :param _SmsSignId: 未接通引用短信签名ID
        :type SmsSignId: str
        :param _SmsTemplateId: 未接通引用短信模板ID
        :type SmsTemplateId: str
        :param _CallType: 拨打方式。NORMAL - 正常拨打；TIMER - 定时拨打
        :type CallType: str
        :param _CallStartDate: 拨打开始日期。CallType=TIMER时有值，yyyy-MM-dd
        :type CallStartDate: str
        :param _CallEndDate: 拨打结束日期。CallType=PERIOD 时有值，yyyy-MM-dd
        :type CallEndDate: str
        """
        self._Module = None
        self._Operation = None
        self._BotName = None
        self._FlowId = None
        self._BanCall = None
        self._PhoneCollection = None
        self._CallTimeCollection = None
        self._StartTimeBan = None
        self._EndTimeBan = None
        self._CodeType = None
        self._CodeCollection = None
        self._CallCount = None
        self._CallInterval = None
        self._SmsSignId = None
        self._SmsTemplateId = None
        self._CallType = None
        self._CallStartDate = None
        self._CallEndDate = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def BotName(self):
        return self._BotName

    @BotName.setter
    def BotName(self, BotName):
        self._BotName = BotName

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def BanCall(self):
        return self._BanCall

    @BanCall.setter
    def BanCall(self, BanCall):
        self._BanCall = BanCall

    @property
    def PhoneCollection(self):
        return self._PhoneCollection

    @PhoneCollection.setter
    def PhoneCollection(self, PhoneCollection):
        self._PhoneCollection = PhoneCollection

    @property
    def CallTimeCollection(self):
        return self._CallTimeCollection

    @CallTimeCollection.setter
    def CallTimeCollection(self, CallTimeCollection):
        self._CallTimeCollection = CallTimeCollection

    @property
    def StartTimeBan(self):
        return self._StartTimeBan

    @StartTimeBan.setter
    def StartTimeBan(self, StartTimeBan):
        self._StartTimeBan = StartTimeBan

    @property
    def EndTimeBan(self):
        return self._EndTimeBan

    @EndTimeBan.setter
    def EndTimeBan(self, EndTimeBan):
        self._EndTimeBan = EndTimeBan

    @property
    def CodeType(self):
        return self._CodeType

    @CodeType.setter
    def CodeType(self, CodeType):
        self._CodeType = CodeType

    @property
    def CodeCollection(self):
        return self._CodeCollection

    @CodeCollection.setter
    def CodeCollection(self, CodeCollection):
        self._CodeCollection = CodeCollection

    @property
    def CallCount(self):
        return self._CallCount

    @CallCount.setter
    def CallCount(self, CallCount):
        self._CallCount = CallCount

    @property
    def CallInterval(self):
        return self._CallInterval

    @CallInterval.setter
    def CallInterval(self, CallInterval):
        self._CallInterval = CallInterval

    @property
    def SmsSignId(self):
        return self._SmsSignId

    @SmsSignId.setter
    def SmsSignId(self, SmsSignId):
        self._SmsSignId = SmsSignId

    @property
    def SmsTemplateId(self):
        return self._SmsTemplateId

    @SmsTemplateId.setter
    def SmsTemplateId(self, SmsTemplateId):
        self._SmsTemplateId = SmsTemplateId

    @property
    def CallType(self):
        return self._CallType

    @CallType.setter
    def CallType(self, CallType):
        self._CallType = CallType

    @property
    def CallStartDate(self):
        return self._CallStartDate

    @CallStartDate.setter
    def CallStartDate(self, CallStartDate):
        self._CallStartDate = CallStartDate

    @property
    def CallEndDate(self):
        return self._CallEndDate

    @CallEndDate.setter
    def CallEndDate(self, CallEndDate):
        self._CallEndDate = CallEndDate


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._BotName = params.get("BotName")
        self._FlowId = params.get("FlowId")
        self._BanCall = params.get("BanCall")
        self._PhoneCollection = params.get("PhoneCollection")
        if params.get("CallTimeCollection") is not None:
            self._CallTimeCollection = CallTimeDict()
            self._CallTimeCollection._deserialize(params.get("CallTimeCollection"))
        self._StartTimeBan = params.get("StartTimeBan")
        self._EndTimeBan = params.get("EndTimeBan")
        self._CodeType = params.get("CodeType")
        self._CodeCollection = params.get("CodeCollection")
        self._CallCount = params.get("CallCount")
        self._CallInterval = params.get("CallInterval")
        self._SmsSignId = params.get("SmsSignId")
        self._SmsTemplateId = params.get("SmsTemplateId")
        self._CallType = params.get("CallType")
        self._CallStartDate = params.get("CallStartDate")
        self._CallEndDate = params.get("CallEndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBotTaskResponse(AbstractModel):
    """CreateBotTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BotId: 机器人任务Id
        :type BotId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BotId = None
        self._RequestId = None

    @property
    def BotId(self):
        return self._BotId

    @BotId.setter
    def BotId(self, BotId):
        self._BotId = BotId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BotId = params.get("BotId")
        self._RequestId = params.get("RequestId")


class DescribeBotFlowRequest(AbstractModel):
    """DescribeBotFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param _Operation: 操作名。默认值（固定）：GetFlow
        :type Operation: str
        """
        self._Module = None
        self._Operation = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBotFlowResponse(AbstractModel):
    """DescribeBotFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BotFlowList: 机器人对话流列表
注意：此字段可能返回 null，表示取不到有效值。
        :type BotFlowList: list of BotFlow
        :param _SmsSignList: 短信签名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SmsSignList: list of SmsSign
        :param _SmsTemplateList: 短信模板列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SmsTemplateList: list of SmsTemplate
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BotFlowList = None
        self._SmsSignList = None
        self._SmsTemplateList = None
        self._RequestId = None

    @property
    def BotFlowList(self):
        return self._BotFlowList

    @BotFlowList.setter
    def BotFlowList(self, BotFlowList):
        self._BotFlowList = BotFlowList

    @property
    def SmsSignList(self):
        return self._SmsSignList

    @SmsSignList.setter
    def SmsSignList(self, SmsSignList):
        self._SmsSignList = SmsSignList

    @property
    def SmsTemplateList(self):
        return self._SmsTemplateList

    @SmsTemplateList.setter
    def SmsTemplateList(self, SmsTemplateList):
        self._SmsTemplateList = SmsTemplateList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BotFlowList") is not None:
            self._BotFlowList = []
            for item in params.get("BotFlowList"):
                obj = BotFlow()
                obj._deserialize(item)
                self._BotFlowList.append(obj)
        if params.get("SmsSignList") is not None:
            self._SmsSignList = []
            for item in params.get("SmsSignList"):
                obj = SmsSign()
                obj._deserialize(item)
                self._SmsSignList.append(obj)
        if params.get("SmsTemplateList") is not None:
            self._SmsTemplateList = []
            for item in params.get("SmsTemplateList"):
                obj = SmsTemplate()
                obj._deserialize(item)
                self._SmsTemplateList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCreditResultRequest(AbstractModel):
    """DescribeCreditResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：Credit
        :type Module: str
        :param _Operation: 操作名，本接口取值：Get
        :type Operation: str
        :param _InstId: 实例ID
        :type InstId: str
        :param _ProductId: 产品ID，形如P******。
        :type ProductId: str
        :param _CaseId: 信审任务ID
        :type CaseId: str
        :param _RequestDate: 请求日期，格式为YYYY-MM-DD
        :type RequestDate: str
        """
        self._Module = None
        self._Operation = None
        self._InstId = None
        self._ProductId = None
        self._CaseId = None
        self._RequestDate = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def InstId(self):
        return self._InstId

    @InstId.setter
    def InstId(self, InstId):
        self._InstId = InstId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def CaseId(self):
        return self._CaseId

    @CaseId.setter
    def CaseId(self, CaseId):
        self._CaseId = CaseId

    @property
    def RequestDate(self):
        return self._RequestDate

    @RequestDate.setter
    def RequestDate(self, RequestDate):
        self._RequestDate = RequestDate


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._InstId = params.get("InstId")
        self._ProductId = params.get("ProductId")
        self._CaseId = params.get("CaseId")
        self._RequestDate = params.get("RequestDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCreditResultResponse(AbstractModel):
    """DescribeCreditResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultCode: <p>呼叫结果，取值范围：</p><ul style="margin-bottom:0px;"><li>NON：接通</li><li>DBU：号码忙</li><li>DRF：不在服务区</li><li>ANA：欠费未接听</li><li>REJ：拒接</li><li>SHU：关机</li><li>NAN：空号</li><li>HAL：停机</li><li>DAD：未接听</li><li>EXE：其他异常</li></ul>
        :type ResultCode: str
        :param _ClientCode: 客户标识代码，多个标识码以英文逗号分隔，ResultCode为NON时才有。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientCode: str
        :param _RingStartTime: 开始振铃时间，ResultCode为NON或DAD时才有此字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type RingStartTime: str
        :param _RingDuration: 振铃时长
        :type RingDuration: int
        :param _AnswerDuration: 接通时长
        :type AnswerDuration: int
        :param _ContextValue: JSON格式的扩展信息字段，ResultCode为NON时才有。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContextValue: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultCode = None
        self._ClientCode = None
        self._RingStartTime = None
        self._RingDuration = None
        self._AnswerDuration = None
        self._ContextValue = None
        self._RequestId = None

    @property
    def ResultCode(self):
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def ClientCode(self):
        return self._ClientCode

    @ClientCode.setter
    def ClientCode(self, ClientCode):
        self._ClientCode = ClientCode

    @property
    def RingStartTime(self):
        return self._RingStartTime

    @RingStartTime.setter
    def RingStartTime(self, RingStartTime):
        self._RingStartTime = RingStartTime

    @property
    def RingDuration(self):
        return self._RingDuration

    @RingDuration.setter
    def RingDuration(self, RingDuration):
        self._RingDuration = RingDuration

    @property
    def AnswerDuration(self):
        return self._AnswerDuration

    @AnswerDuration.setter
    def AnswerDuration(self, AnswerDuration):
        self._AnswerDuration = AnswerDuration

    @property
    def ContextValue(self):
        return self._ContextValue

    @ContextValue.setter
    def ContextValue(self, ContextValue):
        self._ContextValue = ContextValue

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultCode = params.get("ResultCode")
        self._ClientCode = params.get("ClientCode")
        self._RingStartTime = params.get("RingStartTime")
        self._RingDuration = params.get("RingDuration")
        self._AnswerDuration = params.get("AnswerDuration")
        self._ContextValue = params.get("ContextValue")
        self._RequestId = params.get("RequestId")


class DescribeFileModelRequest(AbstractModel):
    """DescribeFileModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param _Operation: 操作名。默认值（固定）：DescribeFileModel
        :type Operation: str
        :param _FileType: 模板文件类型，输入input，停拨stop
        :type FileType: str
        :param _BotId: 任务ID，二者必填一个
        :type BotId: str
        :param _BotName: 任务名称，二者必填一个
        :type BotName: str
        """
        self._Module = None
        self._Operation = None
        self._FileType = None
        self._BotId = None
        self._BotName = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def BotId(self):
        return self._BotId

    @BotId.setter
    def BotId(self, BotId):
        self._BotId = BotId

    @property
    def BotName(self):
        return self._BotName

    @BotName.setter
    def BotName(self, BotName):
        self._BotName = BotName


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._FileType = params.get("FileType")
        self._BotId = params.get("BotId")
        self._BotName = params.get("BotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileModelResponse(AbstractModel):
    """DescribeFileModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CosUrl: 模板下载链接
        :type CosUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CosUrl = None
        self._RequestId = None

    @property
    def CosUrl(self):
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CosUrl = params.get("CosUrl")
        self._RequestId = params.get("RequestId")


class DescribeRecordsRequest(AbstractModel):
    """DescribeRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：Record
        :type Module: str
        :param _Operation: 操作名，本接口取值：List
        :type Operation: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _AccountNum: 案件编号
        :type AccountNum: str
        :param _CalledPhone: 被叫号码
        :type CalledPhone: str
        :param _StartBizDate: 查询起始日期，格式为YYYY-MM-DD
        :type StartBizDate: str
        :param _EndBizDate: 查询结束日期，格式为YYYY-MM-DD
        :type EndBizDate: str
        :param _Offset: 分页参数，索引，默认为0
        :type Offset: str
        :param _Limit: 分页参数，页长，默认为20
        :type Limit: str
        :param _InstId: 实例ID，不传默认为系统分配的初始实例
        :type InstId: str
        """
        self._Module = None
        self._Operation = None
        self._ProductId = None
        self._AccountNum = None
        self._CalledPhone = None
        self._StartBizDate = None
        self._EndBizDate = None
        self._Offset = None
        self._Limit = None
        self._InstId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def AccountNum(self):
        return self._AccountNum

    @AccountNum.setter
    def AccountNum(self, AccountNum):
        self._AccountNum = AccountNum

    @property
    def CalledPhone(self):
        return self._CalledPhone

    @CalledPhone.setter
    def CalledPhone(self, CalledPhone):
        self._CalledPhone = CalledPhone

    @property
    def StartBizDate(self):
        return self._StartBizDate

    @StartBizDate.setter
    def StartBizDate(self, StartBizDate):
        self._StartBizDate = StartBizDate

    @property
    def EndBizDate(self):
        return self._EndBizDate

    @EndBizDate.setter
    def EndBizDate(self, EndBizDate):
        self._EndBizDate = EndBizDate

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
    def InstId(self):
        return self._InstId

    @InstId.setter
    def InstId(self, InstId):
        self._InstId = InstId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ProductId = params.get("ProductId")
        self._AccountNum = params.get("AccountNum")
        self._CalledPhone = params.get("CalledPhone")
        self._StartBizDate = params.get("StartBizDate")
        self._EndBizDate = params.get("EndBizDate")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstId = params.get("InstId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordsResponse(AbstractModel):
    """DescribeRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordList: 录音列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordList: list of SingleRecord
        :param _TotalCount: 录音总量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

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
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = SingleRecord()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：Task
        :type Module: str
        :param _Operation: 操作名，本接口取值：DescribeTaskStatus
        :type Operation: str
        :param _TaskId: 任务ID，"上传文件"接口返回的DataResId，形如abc-xyz123
        :type TaskId: str
        :param _InstId: 实例ID，不传默认为系统分配的初始实例。
        :type InstId: str
        """
        self._Module = None
        self._Operation = None
        self._TaskId = None
        self._InstId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def InstId(self):
        return self._InstId

    @InstId.setter
    def InstId(self, InstId):
        self._InstId = InstId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._TaskId = params.get("TaskId")
        self._InstId = params.get("InstId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskResult: <p>任务结果：</p><ul style="margin-bottom:0px;"><li>处理中："Uploading Data."</li><li>上传成功："File Uploading Task Success."</li><li>上传失败：具体失败原因</li></ul>
        :type TaskResult: str
        :param _TaskType: <p>任务类型：</p><ul style="margin-bottom:0px;"><li>到期/逾期提醒数据上传：002</li><li>到期/逾期提醒停拨数据上传：003</li><li>回访数据上传：004</li><li>回访停拨数据上传：005</li></ul>
        :type TaskType: str
        :param _TaskFileUrl: 过滤文件下载链接，有过滤数据时才存在。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskFileUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskResult = None
        self._TaskType = None
        self._TaskFileUrl = None
        self._RequestId = None

    @property
    def TaskResult(self):
        return self._TaskResult

    @TaskResult.setter
    def TaskResult(self, TaskResult):
        self._TaskResult = TaskResult

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TaskFileUrl(self):
        return self._TaskFileUrl

    @TaskFileUrl.setter
    def TaskFileUrl(self, TaskFileUrl):
        self._TaskFileUrl = TaskFileUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskResult = params.get("TaskResult")
        self._TaskType = params.get("TaskType")
        self._TaskFileUrl = params.get("TaskFileUrl")
        self._RequestId = params.get("RequestId")


class DownloadBotRecordRequest(AbstractModel):
    """DownloadBotRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块：AiApi
        :type Module: str
        :param _Operation: 操作：DownloadRecord
        :type Operation: str
        :param _BizDate: 业务日期
        :type BizDate: str
        """
        self._Module = None
        self._Operation = None
        self._BizDate = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def BizDate(self):
        return self._BizDate

    @BizDate.setter
    def BizDate(self, BizDate):
        self._BizDate = BizDate


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._BizDate = params.get("BizDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadBotRecordResponse(AbstractModel):
    """DownloadBotRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordCosUrl: 录音地址。请求后30分钟内有效
        :type RecordCosUrl: str
        :param _TextCosUrl: 文本地址。请求后30分钟内有效
        :type TextCosUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordCosUrl = None
        self._TextCosUrl = None
        self._RequestId = None

    @property
    def RecordCosUrl(self):
        return self._RecordCosUrl

    @RecordCosUrl.setter
    def RecordCosUrl(self, RecordCosUrl):
        self._RecordCosUrl = RecordCosUrl

    @property
    def TextCosUrl(self):
        return self._TextCosUrl

    @TextCosUrl.setter
    def TextCosUrl(self, TextCosUrl):
        self._TextCosUrl = TextCosUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RecordCosUrl = params.get("RecordCosUrl")
        self._TextCosUrl = params.get("TextCosUrl")
        self._RequestId = params.get("RequestId")


class DownloadDialogueTextRequest(AbstractModel):
    """DownloadDialogueText请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：Report
        :type Module: str
        :param _Operation: 操作名，本接口取值：DownloadTextReport
        :type Operation: str
        :param _ReportDate: 报告日期，格式为YYYY-MM-DD
        :type ReportDate: str
        :param _InstId: 实例ID
        :type InstId: str
        """
        self._Module = None
        self._Operation = None
        self._ReportDate = None
        self._InstId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ReportDate(self):
        return self._ReportDate

    @ReportDate.setter
    def ReportDate(self, ReportDate):
        self._ReportDate = ReportDate

    @property
    def InstId(self):
        return self._InstId

    @InstId.setter
    def InstId(self, InstId):
        self._InstId = InstId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ReportDate = params.get("ReportDate")
        self._InstId = params.get("InstId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadDialogueTextResponse(AbstractModel):
    """DownloadDialogueText返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TextReportUrl: 对话文本下载地址
        :type TextReportUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TextReportUrl = None
        self._RequestId = None

    @property
    def TextReportUrl(self):
        return self._TextReportUrl

    @TextReportUrl.setter
    def TextReportUrl(self, TextReportUrl):
        self._TextReportUrl = TextReportUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TextReportUrl = params.get("TextReportUrl")
        self._RequestId = params.get("RequestId")


class DownloadRecordListRequest(AbstractModel):
    """DownloadRecordList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：Record
        :type Module: str
        :param _Operation: 操作名，本接口取值：DownloadList
        :type Operation: str
        :param _BizDate: 录音日期，格式为YYYY-MM-DD
        :type BizDate: str
        :param _InstId: 实例ID
        :type InstId: str
        """
        self._Module = None
        self._Operation = None
        self._BizDate = None
        self._InstId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def BizDate(self):
        return self._BizDate

    @BizDate.setter
    def BizDate(self, BizDate):
        self._BizDate = BizDate

    @property
    def InstId(self):
        return self._InstId

    @InstId.setter
    def InstId(self, InstId):
        self._InstId = InstId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._BizDate = params.get("BizDate")
        self._InstId = params.get("InstId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadRecordListResponse(AbstractModel):
    """DownloadRecordList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordListUrl: 录音列表下载地址
        :type RecordListUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordListUrl = None
        self._RequestId = None

    @property
    def RecordListUrl(self):
        return self._RecordListUrl

    @RecordListUrl.setter
    def RecordListUrl(self, RecordListUrl):
        self._RecordListUrl = RecordListUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RecordListUrl = params.get("RecordListUrl")
        self._RequestId = params.get("RequestId")


class DownloadReportRequest(AbstractModel):
    """DownloadReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：Report
        :type Module: str
        :param _Operation: 操作名，本接口取值：DownloadReport
        :type Operation: str
        :param _ReportDate: 报告日期，格式为YYYY-MM-DD
        :type ReportDate: str
        :param _InstId: 实例ID，不传默认为系统分配的初始实例。
        :type InstId: str
        """
        self._Module = None
        self._Operation = None
        self._ReportDate = None
        self._InstId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ReportDate(self):
        return self._ReportDate

    @ReportDate.setter
    def ReportDate(self, ReportDate):
        self._ReportDate = ReportDate

    @property
    def InstId(self):
        return self._InstId

    @InstId.setter
    def InstId(self, InstId):
        self._InstId = InstId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ReportDate = params.get("ReportDate")
        self._InstId = params.get("InstId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadReportResponse(AbstractModel):
    """DownloadReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DailyReportUrl: 到期/逾期提醒日报下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DailyReportUrl: str
        :param _ResultReportUrl: 到期/逾期提醒结果下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultReportUrl: str
        :param _DetailReportUrl: 到期/逾期提醒明细下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailReportUrl: str
        :param _CallbackDailyReportUrl: 回访日报下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackDailyReportUrl: str
        :param _CallbackResultReportUrl: 回访结果下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackResultReportUrl: str
        :param _CallbackDetailReportUrl: 回访明细下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackDetailReportUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DailyReportUrl = None
        self._ResultReportUrl = None
        self._DetailReportUrl = None
        self._CallbackDailyReportUrl = None
        self._CallbackResultReportUrl = None
        self._CallbackDetailReportUrl = None
        self._RequestId = None

    @property
    def DailyReportUrl(self):
        return self._DailyReportUrl

    @DailyReportUrl.setter
    def DailyReportUrl(self, DailyReportUrl):
        self._DailyReportUrl = DailyReportUrl

    @property
    def ResultReportUrl(self):
        return self._ResultReportUrl

    @ResultReportUrl.setter
    def ResultReportUrl(self, ResultReportUrl):
        self._ResultReportUrl = ResultReportUrl

    @property
    def DetailReportUrl(self):
        return self._DetailReportUrl

    @DetailReportUrl.setter
    def DetailReportUrl(self, DetailReportUrl):
        self._DetailReportUrl = DetailReportUrl

    @property
    def CallbackDailyReportUrl(self):
        return self._CallbackDailyReportUrl

    @CallbackDailyReportUrl.setter
    def CallbackDailyReportUrl(self, CallbackDailyReportUrl):
        self._CallbackDailyReportUrl = CallbackDailyReportUrl

    @property
    def CallbackResultReportUrl(self):
        return self._CallbackResultReportUrl

    @CallbackResultReportUrl.setter
    def CallbackResultReportUrl(self, CallbackResultReportUrl):
        self._CallbackResultReportUrl = CallbackResultReportUrl

    @property
    def CallbackDetailReportUrl(self):
        return self._CallbackDetailReportUrl

    @CallbackDetailReportUrl.setter
    def CallbackDetailReportUrl(self, CallbackDetailReportUrl):
        self._CallbackDetailReportUrl = CallbackDetailReportUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DailyReportUrl = params.get("DailyReportUrl")
        self._ResultReportUrl = params.get("ResultReportUrl")
        self._DetailReportUrl = params.get("DetailReportUrl")
        self._CallbackDailyReportUrl = params.get("CallbackDailyReportUrl")
        self._CallbackResultReportUrl = params.get("CallbackResultReportUrl")
        self._CallbackDetailReportUrl = params.get("CallbackDetailReportUrl")
        self._RequestId = params.get("RequestId")


class ExportBotDataRequest(AbstractModel):
    """ExportBotData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param _Operation: 操作名。默认值（固定）：ExportBotData
        :type Operation: str
        :param _BizDate: 业务日期。YYYY-MM-DD
        :type BizDate: str
        :param _BotId: 任务ID，二者必填一个
        :type BotId: str
        :param _BotName: 任务名称，二者必填一个
        :type BotName: str
        """
        self._Module = None
        self._Operation = None
        self._BizDate = None
        self._BotId = None
        self._BotName = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def BizDate(self):
        return self._BizDate

    @BizDate.setter
    def BizDate(self, BizDate):
        self._BizDate = BizDate

    @property
    def BotId(self):
        return self._BotId

    @BotId.setter
    def BotId(self, BotId):
        self._BotId = BotId

    @property
    def BotName(self):
        return self._BotName

    @BotName.setter
    def BotName(self, BotName):
        self._BotName = BotName


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._BizDate = params.get("BizDate")
        self._BotId = params.get("BotId")
        self._BotName = params.get("BotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportBotDataResponse(AbstractModel):
    """ExportBotData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 导出文件列表
        :type Data: list of BotFileData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = BotFileData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class PhonePool(AbstractModel):
    """号码组信息

    """

    def __init__(self):
        r"""
        :param _PoolId: 号码组ID
        :type PoolId: str
        :param _PoolName: 号码组名称
        :type PoolName: str
        """
        self._PoolId = None
        self._PoolName = None

    @property
    def PoolId(self):
        return self._PoolId

    @PoolId.setter
    def PoolId(self, PoolId):
        self._PoolId = PoolId

    @property
    def PoolName(self):
        return self._PoolName

    @PoolName.setter
    def PoolName(self, PoolName):
        self._PoolName = PoolName


    def _deserialize(self, params):
        self._PoolId = params.get("PoolId")
        self._PoolName = params.get("PoolName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductQueryInfo(AbstractModel):
    """QueryProducts接口对应数据结构。产品对应的相关信息。

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _ProductCode: 产品编码
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCode: str
        :param _ProductStatus: 产品状态 0 禁用 1 启用
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductStatus: int
        :param _SceneType: 场景类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneType: str
        """
        self._ProductId = None
        self._ProductName = None
        self._ProductCode = None
        self._ProductStatus = None
        self._SceneType = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def ProductStatus(self):
        return self._ProductStatus

    @ProductStatus.setter
    def ProductStatus(self, ProductStatus):
        self._ProductStatus = ProductStatus

    @property
    def SceneType(self):
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        self._ProductCode = params.get("ProductCode")
        self._ProductStatus = params.get("ProductStatus")
        self._SceneType = params.get("SceneType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBlackListDataRequest(AbstractModel):
    """QueryBlackListData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块:AiApi
        :type Module: str
        :param _Operation: 操作:QueryBlackListData
        :type Operation: str
        :param _Offset: 页码
        :type Offset: int
        :param _Limit: 每页数量
        :type Limit: int
        :param _StartBizDate: 开始日期
        :type StartBizDate: str
        :param _EndBizDate: 结束日期
        :type EndBizDate: str
        :param _BlackValue: 电话号码、手机
        :type BlackValue: str
        """
        self._Module = None
        self._Operation = None
        self._Offset = None
        self._Limit = None
        self._StartBizDate = None
        self._EndBizDate = None
        self._BlackValue = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

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
    def StartBizDate(self):
        return self._StartBizDate

    @StartBizDate.setter
    def StartBizDate(self, StartBizDate):
        self._StartBizDate = StartBizDate

    @property
    def EndBizDate(self):
        return self._EndBizDate

    @EndBizDate.setter
    def EndBizDate(self, EndBizDate):
        self._EndBizDate = EndBizDate

    @property
    def BlackValue(self):
        return self._BlackValue

    @BlackValue.setter
    def BlackValue(self, BlackValue):
        self._BlackValue = BlackValue


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartBizDate = params.get("StartBizDate")
        self._EndBizDate = params.get("EndBizDate")
        self._BlackValue = params.get("BlackValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBlackListDataResponse(AbstractModel):
    """QueryBlackListData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数。
        :type TotalCount: int
        :param _Data: 黑名单列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of BlackListData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = BlackListData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class QueryBotListRequest(AbstractModel):
    """QueryBotList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名：AiApi
        :type Module: str
        :param _Operation: 操作名：QueryBotList
        :type Operation: str
        """
        self._Module = None
        self._Operation = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBotListResponse(AbstractModel):
    """QueryBotList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BotList: 任务列表。
        :type BotList: list of BotInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BotList = None
        self._RequestId = None

    @property
    def BotList(self):
        return self._BotList

    @BotList.setter
    def BotList(self, BotList):
        self._BotList = BotList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BotList") is not None:
            self._BotList = []
            for item in params.get("BotList"):
                obj = BotInfo()
                obj._deserialize(item)
                self._BotList.append(obj)
        self._RequestId = params.get("RequestId")


class QueryCallListRequest(AbstractModel):
    """QueryCallList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param _Operation: 操作名。默认值（固定）：QueryCallList
        :type Operation: str
        :param _BizDate: 业务日期
        :type BizDate: str
        :param _BotId: 任务ID，二者必填一个
        :type BotId: str
        :param _BotName: 任务名称，二者必填一个
        :type BotName: str
        :param _FileName: 通过API或平台上传的文件完整名称
        :type FileName: str
        """
        self._Module = None
        self._Operation = None
        self._BizDate = None
        self._BotId = None
        self._BotName = None
        self._FileName = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def BizDate(self):
        return self._BizDate

    @BizDate.setter
    def BizDate(self, BizDate):
        self._BizDate = BizDate

    @property
    def BotId(self):
        return self._BotId

    @BotId.setter
    def BotId(self, BotId):
        self._BotId = BotId

    @property
    def BotName(self):
        return self._BotName

    @BotName.setter
    def BotName(self, BotName):
        self._BotName = BotName

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._BizDate = params.get("BizDate")
        self._BotId = params.get("BotId")
        self._BotName = params.get("BotName")
        self._FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCallListResponse(AbstractModel):
    """QueryCallList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CallList: 任务作业状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CallList: list of CallInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CallList = None
        self._RequestId = None

    @property
    def CallList(self):
        return self._CallList

    @CallList.setter
    def CallList(self, CallList):
        self._CallList = CallList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CallList") is not None:
            self._CallList = []
            for item in params.get("CallList"):
                obj = CallInfo()
                obj._deserialize(item)
                self._CallList.append(obj)
        self._RequestId = params.get("RequestId")


class QueryInstantDataRequest(AbstractModel):
    """QueryInstantData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：Data
        :type Module: str
        :param _Operation: 操作名，本接口取值：Query
        :type Operation: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _InstanceId: 实例ID，不传默认为系统分配的初始实例
        :type InstanceId: str
        :param _QueryModel: 查询类型：callRecord 通话记录
        :type QueryModel: str
        :param _Data: 查询参数
        :type Data: str
        """
        self._Module = None
        self._Operation = None
        self._ProductId = None
        self._InstanceId = None
        self._QueryModel = None
        self._Data = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def QueryModel(self):
        return self._QueryModel

    @QueryModel.setter
    def QueryModel(self, QueryModel):
        self._QueryModel = QueryModel

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ProductId = params.get("ProductId")
        self._InstanceId = params.get("InstanceId")
        self._QueryModel = params.get("QueryModel")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryInstantDataResponse(AbstractModel):
    """QueryInstantData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Data: 返回内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class QueryProductsRequest(AbstractModel):
    """QueryProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名。默认值（固定）：Product
        :type Module: str
        :param _Operation: 操作名。默认值（固定）：QueryProducts
        :type Operation: str
        :param _InstanceId: 实例Id。
        :type InstanceId: str
        """
        self._Module = None
        self._Operation = None
        self._InstanceId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryProductsResponse(AbstractModel):
    """QueryProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductList: 产品信息。
        :type ProductList: list of ProductQueryInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProductList = None
        self._RequestId = None

    @property
    def ProductList(self):
        return self._ProductList

    @ProductList.setter
    def ProductList(self, ProductList):
        self._ProductList = ProductList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ProductList") is not None:
            self._ProductList = []
            for item in params.get("ProductList"):
                obj = ProductQueryInfo()
                obj._deserialize(item)
                self._ProductList.append(obj)
        self._RequestId = params.get("RequestId")


class QueryRecordListRequest(AbstractModel):
    """QueryRecordList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名。AiApi
        :type Module: str
        :param _Operation: 操作名。QueryRecordList
        :type Operation: str
        :param _Offset: 偏移值
        :type Offset: int
        :param _Limit: 偏移位移，最大20
        :type Limit: int
        :param _BotId: 任务ID，二者必填一个
        :type BotId: str
        :param _BotName: 任务名称，二者必填一个
        :type BotName: str
        :param _CalledPhone: 被叫号码
        :type CalledPhone: str
        :param _StartBizDate: 开始日期
        :type StartBizDate: str
        :param _EndBizDate: 结束日期
        :type EndBizDate: str
        """
        self._Module = None
        self._Operation = None
        self._Offset = None
        self._Limit = None
        self._BotId = None
        self._BotName = None
        self._CalledPhone = None
        self._StartBizDate = None
        self._EndBizDate = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

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
    def BotId(self):
        return self._BotId

    @BotId.setter
    def BotId(self, BotId):
        self._BotId = BotId

    @property
    def BotName(self):
        return self._BotName

    @BotName.setter
    def BotName(self, BotName):
        self._BotName = BotName

    @property
    def CalledPhone(self):
        return self._CalledPhone

    @CalledPhone.setter
    def CalledPhone(self, CalledPhone):
        self._CalledPhone = CalledPhone

    @property
    def StartBizDate(self):
        return self._StartBizDate

    @StartBizDate.setter
    def StartBizDate(self, StartBizDate):
        self._StartBizDate = StartBizDate

    @property
    def EndBizDate(self):
        return self._EndBizDate

    @EndBizDate.setter
    def EndBizDate(self, EndBizDate):
        self._EndBizDate = EndBizDate


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._BotId = params.get("BotId")
        self._BotName = params.get("BotName")
        self._CalledPhone = params.get("CalledPhone")
        self._StartBizDate = params.get("StartBizDate")
        self._EndBizDate = params.get("EndBizDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryRecordListResponse(AbstractModel):
    """QueryRecordList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordList: 录音列表。
        :type RecordList: list of RecordInfo
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

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
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = RecordInfo()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class RecordInfo(AbstractModel):
    """录音文件详情

    """

    def __init__(self):
        r"""
        :param _BotId: 任务Id
        :type BotId: str
        :param _BotName: 任务名称
        :type BotName: str
        :param _BizDate: 任务日期
        :type BizDate: str
        :param _CalledPhone: 被叫号码
        :type CalledPhone: str
        :param _CallStartTime: 开始通话时间
        :type CallStartTime: str
        :param _Duration: 通话时长
        :type Duration: int
        :param _CosUrl: 录音文件地址
        :type CosUrl: str
        :param _DialogueLog: 对话日志。JSON格式
        :type DialogueLog: str
        :param _CosFileName: 录音文件名
        :type CosFileName: str
        """
        self._BotId = None
        self._BotName = None
        self._BizDate = None
        self._CalledPhone = None
        self._CallStartTime = None
        self._Duration = None
        self._CosUrl = None
        self._DialogueLog = None
        self._CosFileName = None

    @property
    def BotId(self):
        return self._BotId

    @BotId.setter
    def BotId(self, BotId):
        self._BotId = BotId

    @property
    def BotName(self):
        return self._BotName

    @BotName.setter
    def BotName(self, BotName):
        self._BotName = BotName

    @property
    def BizDate(self):
        return self._BizDate

    @BizDate.setter
    def BizDate(self, BizDate):
        self._BizDate = BizDate

    @property
    def CalledPhone(self):
        return self._CalledPhone

    @CalledPhone.setter
    def CalledPhone(self, CalledPhone):
        self._CalledPhone = CalledPhone

    @property
    def CallStartTime(self):
        return self._CallStartTime

    @CallStartTime.setter
    def CallStartTime(self, CallStartTime):
        self._CallStartTime = CallStartTime

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def CosUrl(self):
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def DialogueLog(self):
        return self._DialogueLog

    @DialogueLog.setter
    def DialogueLog(self, DialogueLog):
        self._DialogueLog = DialogueLog

    @property
    def CosFileName(self):
        return self._CosFileName

    @CosFileName.setter
    def CosFileName(self, CosFileName):
        self._CosFileName = CosFileName


    def _deserialize(self, params):
        self._BotId = params.get("BotId")
        self._BotName = params.get("BotName")
        self._BizDate = params.get("BizDate")
        self._CalledPhone = params.get("CalledPhone")
        self._CallStartTime = params.get("CallStartTime")
        self._Duration = params.get("Duration")
        self._CosUrl = params.get("CosUrl")
        self._DialogueLog = params.get("DialogueLog")
        self._CosFileName = params.get("CosFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SingleBlackApply(AbstractModel):
    """黑名单申请信息

    """

    def __init__(self):
        r"""
        :param _BlackType: 黑名单类型，01代表手机号码。
        :type BlackType: str
        :param _OperationType: 操作类型，A为新增，D为删除。
        :type OperationType: str
        :param _BlackValue: 黑名单值，BlackType为01时，填写11位手机号码。
        :type BlackValue: str
        :param _BlackDescription: 备注。
        :type BlackDescription: str
        :param _BlackValidDate: 黑名单生效截止日期，格式为YYYY-MM-DD，不填默认为永久。
        :type BlackValidDate: str
        """
        self._BlackType = None
        self._OperationType = None
        self._BlackValue = None
        self._BlackDescription = None
        self._BlackValidDate = None

    @property
    def BlackType(self):
        return self._BlackType

    @BlackType.setter
    def BlackType(self, BlackType):
        self._BlackType = BlackType

    @property
    def OperationType(self):
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def BlackValue(self):
        return self._BlackValue

    @BlackValue.setter
    def BlackValue(self, BlackValue):
        self._BlackValue = BlackValue

    @property
    def BlackDescription(self):
        return self._BlackDescription

    @BlackDescription.setter
    def BlackDescription(self, BlackDescription):
        self._BlackDescription = BlackDescription

    @property
    def BlackValidDate(self):
        return self._BlackValidDate

    @BlackValidDate.setter
    def BlackValidDate(self, BlackValidDate):
        self._BlackValidDate = BlackValidDate


    def _deserialize(self, params):
        self._BlackType = params.get("BlackType")
        self._OperationType = params.get("OperationType")
        self._BlackValue = params.get("BlackValue")
        self._BlackDescription = params.get("BlackDescription")
        self._BlackValidDate = params.get("BlackValidDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SingleRecord(AbstractModel):
    """录音信息

    """

    def __init__(self):
        r"""
        :param _AccountNum: 案件编号。
        :type AccountNum: str
        :param _BizDate: 外呼日期。
        :type BizDate: str
        :param _CallStartTime: 开始呼叫时间。
        :type CallStartTime: str
        :param _CallerPhone: 主叫号码。
        :type CallerPhone: str
        :param _Direction: 呼叫方向，O为呼出，I为呼入。
        :type Direction: str
        :param _Duration: 通话时长。
        :type Duration: int
        :param _ProductId: 产品ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _RecordCosUrl: 录音下载链接。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordCosUrl: str
        """
        self._AccountNum = None
        self._BizDate = None
        self._CallStartTime = None
        self._CallerPhone = None
        self._Direction = None
        self._Duration = None
        self._ProductId = None
        self._RecordCosUrl = None

    @property
    def AccountNum(self):
        return self._AccountNum

    @AccountNum.setter
    def AccountNum(self, AccountNum):
        self._AccountNum = AccountNum

    @property
    def BizDate(self):
        return self._BizDate

    @BizDate.setter
    def BizDate(self, BizDate):
        self._BizDate = BizDate

    @property
    def CallStartTime(self):
        return self._CallStartTime

    @CallStartTime.setter
    def CallStartTime(self, CallStartTime):
        self._CallStartTime = CallStartTime

    @property
    def CallerPhone(self):
        return self._CallerPhone

    @CallerPhone.setter
    def CallerPhone(self, CallerPhone):
        self._CallerPhone = CallerPhone

    @property
    def Direction(self):
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def RecordCosUrl(self):
        return self._RecordCosUrl

    @RecordCosUrl.setter
    def RecordCosUrl(self, RecordCosUrl):
        self._RecordCosUrl = RecordCosUrl


    def _deserialize(self, params):
        self._AccountNum = params.get("AccountNum")
        self._BizDate = params.get("BizDate")
        self._CallStartTime = params.get("CallStartTime")
        self._CallerPhone = params.get("CallerPhone")
        self._Direction = params.get("Direction")
        self._Duration = params.get("Duration")
        self._ProductId = params.get("ProductId")
        self._RecordCosUrl = params.get("RecordCosUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsSign(AbstractModel):
    """短信签名信息

    """

    def __init__(self):
        r"""
        :param _SignId: 短信签名ID
        :type SignId: str
        :param _SignName: 短信签名名称
        :type SignName: str
        """
        self._SignId = None
        self._SignName = None

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


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        self._SignName = params.get("SignName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsTemplate(AbstractModel):
    """短信模板信息

    """

    def __init__(self):
        r"""
        :param _TemplateId: 短信模板ID
        :type TemplateId: str
        :param _TemplateName: 短信模板名称
        :type TemplateName: str
        """
        self._TemplateId = None
        self._TemplateName = None

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


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateBotTaskRequest(AbstractModel):
    """UpdateBotTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param _Operation: 操作名。默认值（固定）：UpdateTask
        :type Operation: str
        :param _BotName: 任务名称
        :type BotName: str
        :param _BotId: 任务ID
        :type BotId: str
        :param _CallTimeCollection: 产品拨打时间集合
        :type CallTimeCollection: :class:`tencentcloud.cr.v20180321.models.CallTimeDict`
        :param _BanCall: 是否禁止拨打，默认Y
        :type BanCall: str
        :param _StartTimeBan: 禁止拨打起始时间。默认130000
        :type StartTimeBan: str
        :param _EndTimeBan: 禁止拨打结束时间。默认140000
        :type EndTimeBan: str
        :param _PhoneCollection: 拨打线路集合
        :type PhoneCollection: str
        :param _CodeType: 重播方式，NON：未接通、LABEL：意向分级，可多选，用竖线分隔：NON|LABEL
        :type CodeType: str
        :param _CodeCollection: 重播值集合，A：强意向、B：中意向、C：低意向、D：无意向、E：在忙、F：未接通、G：无效号码，可多选，用竖线分隔：A|B|C|D|E|F|G
        :type CodeCollection: str
        :param _CallCount: 继续拨打次数
        :type CallCount: int
        :param _CallInterval: 拨打间隔
        :type CallInterval: int
        :param _SmsSignId: 未接通引用短信签名ID
        :type SmsSignId: str
        :param _SmsTemplateId: 未接通引用短信模板ID
        :type SmsTemplateId: str
        """
        self._Module = None
        self._Operation = None
        self._BotName = None
        self._BotId = None
        self._CallTimeCollection = None
        self._BanCall = None
        self._StartTimeBan = None
        self._EndTimeBan = None
        self._PhoneCollection = None
        self._CodeType = None
        self._CodeCollection = None
        self._CallCount = None
        self._CallInterval = None
        self._SmsSignId = None
        self._SmsTemplateId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def BotName(self):
        return self._BotName

    @BotName.setter
    def BotName(self, BotName):
        self._BotName = BotName

    @property
    def BotId(self):
        return self._BotId

    @BotId.setter
    def BotId(self, BotId):
        self._BotId = BotId

    @property
    def CallTimeCollection(self):
        return self._CallTimeCollection

    @CallTimeCollection.setter
    def CallTimeCollection(self, CallTimeCollection):
        self._CallTimeCollection = CallTimeCollection

    @property
    def BanCall(self):
        return self._BanCall

    @BanCall.setter
    def BanCall(self, BanCall):
        self._BanCall = BanCall

    @property
    def StartTimeBan(self):
        return self._StartTimeBan

    @StartTimeBan.setter
    def StartTimeBan(self, StartTimeBan):
        self._StartTimeBan = StartTimeBan

    @property
    def EndTimeBan(self):
        return self._EndTimeBan

    @EndTimeBan.setter
    def EndTimeBan(self, EndTimeBan):
        self._EndTimeBan = EndTimeBan

    @property
    def PhoneCollection(self):
        return self._PhoneCollection

    @PhoneCollection.setter
    def PhoneCollection(self, PhoneCollection):
        self._PhoneCollection = PhoneCollection

    @property
    def CodeType(self):
        return self._CodeType

    @CodeType.setter
    def CodeType(self, CodeType):
        self._CodeType = CodeType

    @property
    def CodeCollection(self):
        return self._CodeCollection

    @CodeCollection.setter
    def CodeCollection(self, CodeCollection):
        self._CodeCollection = CodeCollection

    @property
    def CallCount(self):
        return self._CallCount

    @CallCount.setter
    def CallCount(self, CallCount):
        self._CallCount = CallCount

    @property
    def CallInterval(self):
        return self._CallInterval

    @CallInterval.setter
    def CallInterval(self, CallInterval):
        self._CallInterval = CallInterval

    @property
    def SmsSignId(self):
        return self._SmsSignId

    @SmsSignId.setter
    def SmsSignId(self, SmsSignId):
        self._SmsSignId = SmsSignId

    @property
    def SmsTemplateId(self):
        return self._SmsTemplateId

    @SmsTemplateId.setter
    def SmsTemplateId(self, SmsTemplateId):
        self._SmsTemplateId = SmsTemplateId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._BotName = params.get("BotName")
        self._BotId = params.get("BotId")
        if params.get("CallTimeCollection") is not None:
            self._CallTimeCollection = CallTimeDict()
            self._CallTimeCollection._deserialize(params.get("CallTimeCollection"))
        self._BanCall = params.get("BanCall")
        self._StartTimeBan = params.get("StartTimeBan")
        self._EndTimeBan = params.get("EndTimeBan")
        self._PhoneCollection = params.get("PhoneCollection")
        self._CodeType = params.get("CodeType")
        self._CodeCollection = params.get("CodeCollection")
        self._CallCount = params.get("CallCount")
        self._CallInterval = params.get("CallInterval")
        self._SmsSignId = params.get("SmsSignId")
        self._SmsTemplateId = params.get("SmsTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateBotTaskResponse(AbstractModel):
    """UpdateBotTask返回参数结构体

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


class UploadBotDataRequest(AbstractModel):
    """UploadBotData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param _Operation: 操作名。默认值（固定）：UploadData
        :type Operation: str
        :param _Data: 任务数据。JSON格式
        :type Data: str
        :param _BotId: 任务ID，二者必填一个
        :type BotId: str
        :param _BotName: 任务名称，二者必填一个
        :type BotName: str
        """
        self._Module = None
        self._Operation = None
        self._Data = None
        self._BotId = None
        self._BotName = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def BotId(self):
        return self._BotId

    @BotId.setter
    def BotId(self, BotId):
        self._BotId = BotId

    @property
    def BotName(self):
        return self._BotName

    @BotName.setter
    def BotName(self, BotName):
        self._BotName = BotName


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._Data = params.get("Data")
        self._BotId = params.get("BotId")
        self._BotName = params.get("BotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadBotDataResponse(AbstractModel):
    """UploadBotData返回参数结构体

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


class UploadBotFileRequest(AbstractModel):
    """UploadBotFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名。默认值（固定）：AiApi
        :type Module: str
        :param _Operation: 操作名。默认值（固定）：Upload
        :type Operation: str
        :param _FileType: 文件类型，输入input，停拨stop
        :type FileType: str
        :param _FileUrl: 文件链接
        :type FileUrl: str
        :param _FileName: 文件名
        :type FileName: str
        :param _BotId: 任务ID，二者必填一个
        :type BotId: str
        :param _BotName: 任务名称，二者必填一个
        :type BotName: str
        """
        self._Module = None
        self._Operation = None
        self._FileType = None
        self._FileUrl = None
        self._FileName = None
        self._BotId = None
        self._BotName = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def BotId(self):
        return self._BotId

    @BotId.setter
    def BotId(self, BotId):
        self._BotId = BotId

    @property
    def BotName(self):
        return self._BotName

    @BotName.setter
    def BotName(self, BotName):
        self._BotName = BotName


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._FileType = params.get("FileType")
        self._FileUrl = params.get("FileUrl")
        self._FileName = params.get("FileName")
        self._BotId = params.get("BotId")
        self._BotName = params.get("BotName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadBotFileResponse(AbstractModel):
    """UploadBotFile返回参数结构体

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


class UploadDataFileRequest(AbstractModel):
    """UploadDataFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：Data
        :type Module: str
        :param _Operation: 操作名，本接口取值：Upload
        :type Operation: str
        :param _FileName: 文件名
        :type FileName: str
        :param _UploadModel: <p>上传类型，不填默认到期/逾期提醒文件，取值范围：</p><ul style="margin-bottom:0px;"><li>data：到期/逾期提醒文件</li><li>repay：到期/逾期提醒停拨文件</li><li>callback：回访文件</li><li>callstop：回访停拨文件</li><li>blacklist：黑名单文件</li></ul>
        :type UploadModel: str
        :param _File: 文件，文件与文件地址上传只可选用一种，必须使用multipart/form-data协议来上传二进制流文件，建议使用xlsx格式，大小不超过5MB。
        :type File: binary
        :param _FileUrl: 文件上传地址，文件与文件地址上传只可选用一种，大小不超过50MB。
        :type FileUrl: str
        :param _InstId: 实例ID，不传默认为系统分配的初始实例。
        :type InstId: str
        """
        self._Module = None
        self._Operation = None
        self._FileName = None
        self._UploadModel = None
        self._File = None
        self._FileUrl = None
        self._InstId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def UploadModel(self):
        return self._UploadModel

    @UploadModel.setter
    def UploadModel(self, UploadModel):
        self._UploadModel = UploadModel

    @property
    def File(self):
        return self._File

    @File.setter
    def File(self, File):
        self._File = File

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def InstId(self):
        return self._InstId

    @InstId.setter
    def InstId(self, InstId):
        self._InstId = InstId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._FileName = params.get("FileName")
        self._UploadModel = params.get("UploadModel")
        self._File = params.get("File")
        self._FileUrl = params.get("FileUrl")
        self._InstId = params.get("InstId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadDataFileResponse(AbstractModel):
    """UploadDataFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataResId: 数据ID
        :type DataResId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataResId = None
        self._RequestId = None

    @property
    def DataResId(self):
        return self._DataResId

    @DataResId.setter
    def DataResId(self, DataResId):
        self._DataResId = DataResId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DataResId = params.get("DataResId")
        self._RequestId = params.get("RequestId")


class UploadDataJsonRequest(AbstractModel):
    """UploadDataJson请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名，本接口取值：Data
        :type Module: str
        :param _Operation: 操作名，本接口取值：UploadJson
        :type Operation: str
        :param _Data: 报文信息
        :type Data: str
        :param _UploadModel: <p>上传类型，不填默认到期/逾期提醒数据，取值范围：</p><ul style="margin-bottom:0px;"><li>data：到期/逾期提醒数据</li><li>repay：到期/逾期提醒停拨数据</li></ul>
        :type UploadModel: str
        :param _InstanceId: 实例ID，不传默认为系统分配的初始实例。
        :type InstanceId: str
        """
        self._Module = None
        self._Operation = None
        self._Data = None
        self._UploadModel = None
        self._InstanceId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def UploadModel(self):
        return self._UploadModel

    @UploadModel.setter
    def UploadModel(self, UploadModel):
        self._UploadModel = UploadModel

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._Data = params.get("Data")
        self._UploadModel = params.get("UploadModel")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadDataJsonResponse(AbstractModel):
    """UploadDataJson返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 响应报文信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class UploadFileRequest(AbstractModel):
    """UploadFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名
        :type Module: str
        :param _Operation: 操作名
        :type Operation: str
        :param _FileUrl: 文件上传地址，要求地址协议为HTTPS，且URL端口必须为443
        :type FileUrl: str
        :param _FileName: 文件名
        :type FileName: str
        :param _FileDate: 文件日期
        :type FileDate: str
        """
        self._Module = None
        self._Operation = None
        self._FileUrl = None
        self._FileName = None
        self._FileDate = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileDate(self):
        return self._FileDate

    @FileDate.setter
    def FileDate(self, FileDate):
        self._FileDate = FileDate


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._FileUrl = params.get("FileUrl")
        self._FileName = params.get("FileName")
        self._FileDate = params.get("FileDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFileResponse(AbstractModel):
    """UploadFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
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