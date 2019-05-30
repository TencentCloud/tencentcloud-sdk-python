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


class ApplyBlackListRequest(AbstractModel):
    """ApplyBlackList请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块
        :type Module: str
        :param Operation: 操作
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
        :param Module: 模块
        :type Module: str
        :param Operation: 操作
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


class DescribeCreditResultRequest(AbstractModel):
    """DescribeCreditResult请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块
        :type Module: str
        :param Operation: 操作
        :type Operation: str
        :param InstId: 实例ID
        :type InstId: str
        :param ProductId: 产品ID，形如P******。
        :type ProductId: str
        :param CaseId: 信审任务ID
        :type CaseId: str
        :param RequestDate: 请求日期
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


class DescribeRecordsRequest(AbstractModel):
    """DescribeRecords请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块
        :type Module: str
        :param Operation: 操作
        :type Operation: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param AccountNum: 案件编号
        :type AccountNum: str
        :param CalledPhone: 被叫号码
        :type CalledPhone: str
        :param StartBizDate: 查询起始日期
        :type StartBizDate: str
        :param EndBizDate: 查询结束日期
        :type EndBizDate: str
        :param Offset: 分页参数，索引，从0开始
        :type Offset: str
        :param Limit: 分页参数，页长
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
        :param Module: 模块名
        :type Module: str
        :param Operation: 操作名
        :type Operation: str
        :param TaskId: 任务ID，形如abc-a0b1c2xyz
        :type TaskId: str
        """
        self.Module = None
        self.Operation = None
        self.TaskId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.TaskId = params.get("TaskId")


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回参数结构体

    """

    def __init__(self):
        """
        :param TaskResult: 任务结果，例如上传成功时返回“File Uploading Task Success.”
        :type TaskResult: str
        :param TaskType: <p>任务类型：</p><ul style="margin-bottom:0px;"><li>报告下载：001</li><li>催收数据上传：002</li><li>还款数据上传：003</li><li>回访数据上传：004</li><li>停拨数据上传：005</li></ul>
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


class DownloadReportRequest(AbstractModel):
    """DownloadReport请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名
        :type Module: str
        :param Operation: 操作名
        :type Operation: str
        :param ReportDate: 报告日期
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


class DownloadReportResponse(AbstractModel):
    """DownloadReport返回参数结构体

    """

    def __init__(self):
        """
        :param DailyReportUrl: 催收日报下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DailyReportUrl: str
        :param ResultReportUrl: 催收结果下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultReportUrl: str
        :param DetailReportUrl: 催收明细下载地址
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


class UploadDataFileRequest(AbstractModel):
    """UploadDataFile请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名
        :type Module: str
        :param Operation: 操作名
        :type Operation: str
        :param FileName: 文件名
        :type FileName: str
        :param UploadModel: <p>上传类型，不填默认催收文件，取值范围：</p><ul style="margin-bottom:0px;"><li>data：催收文件</li><li>repay：还款文件</li><li>callback：回访文件</li></ul>
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