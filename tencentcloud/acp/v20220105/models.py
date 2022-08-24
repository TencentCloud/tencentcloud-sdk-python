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


class AppInfoItem(AbstractModel):
    """应用合规隐私诊断任务应用数据信息

    """

    def __init__(self):
        r"""
        :param AppPackage: App包名
        :type AppPackage: str
        :param AppName: App名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AppName: str
        :param AppVersion: App版本
注意：此字段可能返回 null，表示取不到有效值。
        :type AppVersion: str
        :param Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param ReportUrl: App隐私诊断报告下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportUrl: str
        :param ReportTitle: App隐私诊断报告名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportTitle: str
        :param BehaviorUrl: App诊断堆栈报告下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type BehaviorUrl: str
        :param BehaviorTitle: App诊断堆栈报告名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BehaviorTitle: str
        :param HighRiskCount: 诊断高风险项数量
注意：此字段可能返回 null，表示取不到有效值。
        :type HighRiskCount: int
        :param PrivacyTextName: 隐私申明文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivacyTextName: str
        :param SoftwareMD5: 软件MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type SoftwareMD5: str
        :param PrivacyTextMD5: 隐私文本MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivacyTextMD5: str
        """
        self.AppPackage = None
        self.AppName = None
        self.AppVersion = None
        self.Platform = None
        self.ReportUrl = None
        self.ReportTitle = None
        self.BehaviorUrl = None
        self.BehaviorTitle = None
        self.HighRiskCount = None
        self.PrivacyTextName = None
        self.SoftwareMD5 = None
        self.PrivacyTextMD5 = None


    def _deserialize(self, params):
        self.AppPackage = params.get("AppPackage")
        self.AppName = params.get("AppName")
        self.AppVersion = params.get("AppVersion")
        self.Platform = params.get("Platform")
        self.ReportUrl = params.get("ReportUrl")
        self.ReportTitle = params.get("ReportTitle")
        self.BehaviorUrl = params.get("BehaviorUrl")
        self.BehaviorTitle = params.get("BehaviorTitle")
        self.HighRiskCount = params.get("HighRiskCount")
        self.PrivacyTextName = params.get("PrivacyTextName")
        self.SoftwareMD5 = params.get("SoftwareMD5")
        self.PrivacyTextMD5 = params.get("PrivacyTextMD5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTaskData(AbstractModel):
    """应用合规隐私诊断任务数据

    """

    def __init__(self):
        r"""
        :param TaskID: 任务ID
        :type TaskID: str
        :param TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        :param TaskStatus: 0:默认值(待检测/待咨询), 1.检测中, 2:待评估, 3:评估中, 4:任务完成/咨询完成, 5:任务失败, 6:咨询中;
        :type TaskStatus: int
        :param TaskErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskErrMsg: str
        :param Source: 任务来源,0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android)
        :type Source: int
        :param AppInfo: 应用信息
        :type AppInfo: :class:`tencentcloud.acp.v20220105.models.AppInfoItem`
        :param StartTime: 任务启动时间
        :type StartTime: str
        :param EndTime: 任务完成时间(更新时间)
        :type EndTime: str
        :param ContactName: 联系人信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactName: str
        """
        self.TaskID = None
        self.TaskType = None
        self.TaskStatus = None
        self.TaskErrMsg = None
        self.Source = None
        self.AppInfo = None
        self.StartTime = None
        self.EndTime = None
        self.ContactName = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.TaskType = params.get("TaskType")
        self.TaskStatus = params.get("TaskStatus")
        self.TaskErrMsg = params.get("TaskErrMsg")
        self.Source = params.get("Source")
        if params.get("AppInfo") is not None:
            self.AppInfo = AppInfoItem()
            self.AppInfo._deserialize(params.get("AppInfo"))
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ContactName = params.get("ContactName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppScanTaskRepeatRequest(AbstractModel):
    """CreateAppScanTaskRepeat请求参数结构体

    """

    def __init__(self):
        r"""
        :param Source: 任务来源, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android), 3:app漏洞扫描;
        :type Source: int
        :param Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        :param OrgTaskID: 原诊断任务ID
        :type OrgTaskID: str
        :param AppPackage: App包名
        :type AppPackage: str
        :param FileID: 上传的文件ID(任务来源为1时必填)
        :type FileID: str
        :param AppDownloadUrl: 软件下载链接地址(任务来源为2时必填)
        :type AppDownloadUrl: str
        :param PrivacyTextUrl: 隐私文本下载地址(任务来源为2时必填)
        :type PrivacyTextUrl: str
        :param AppName: 应用名称
        :type AppName: str
        :param PrivacyTextName: 隐私申明文件名称
        :type PrivacyTextName: str
        """
        self.Source = None
        self.Platform = None
        self.TaskType = None
        self.OrgTaskID = None
        self.AppPackage = None
        self.FileID = None
        self.AppDownloadUrl = None
        self.PrivacyTextUrl = None
        self.AppName = None
        self.PrivacyTextName = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Platform = params.get("Platform")
        self.TaskType = params.get("TaskType")
        self.OrgTaskID = params.get("OrgTaskID")
        self.AppPackage = params.get("AppPackage")
        self.FileID = params.get("FileID")
        self.AppDownloadUrl = params.get("AppDownloadUrl")
        self.PrivacyTextUrl = params.get("PrivacyTextUrl")
        self.AppName = params.get("AppName")
        self.PrivacyTextName = params.get("PrivacyTextName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppScanTaskRepeatResponse(AbstractModel):
    """CreateAppScanTaskRepeat返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Result: int
        :param TaskID: 任务id
        :type TaskID: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.TaskID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.TaskID = params.get("TaskID")
        self.RequestId = params.get("RequestId")


class CreateAppScanTaskRequest(AbstractModel):
    """CreateAppScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        :param Source: 任务来源, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android), 3:app漏洞扫描;
        :type Source: int
        :param Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param AppPackage: App包名
        :type AppPackage: str
        :param AppName: App名称
        :type AppName: str
        :param AppVersion: App版本
        :type AppVersion: str
        :param FileID: 上传的软件文件ID(任务来源为1时必填)
        :type FileID: str
        :param AppDownloadUrl: 软件下载链接地址(任务来源为2时必填)
        :type AppDownloadUrl: str
        :param PrivacyTextUrl: 隐私文本下载地址(任务来源为2时必填)
        :type PrivacyTextUrl: str
        :param ContactName: 联系人信息
        :type ContactName: str
        :param TelNumber: 联系电话
        :type TelNumber: str
        :param Email: 公司邮箱
        :type Email: str
        :param CorpName: 公司名称
        :type CorpName: str
        :param SalesPerson: 商务对接人员
        :type SalesPerson: str
        :param Remark: 备注信息
        :type Remark: str
        :param IsAgreePrivacy: 是否同意隐私条款，0:不同意(默认), 1:同意
        :type IsAgreePrivacy: int
        :param PrivacyTextName: 隐私申明文件名称
        :type PrivacyTextName: str
        """
        self.TaskType = None
        self.Source = None
        self.Platform = None
        self.AppPackage = None
        self.AppName = None
        self.AppVersion = None
        self.FileID = None
        self.AppDownloadUrl = None
        self.PrivacyTextUrl = None
        self.ContactName = None
        self.TelNumber = None
        self.Email = None
        self.CorpName = None
        self.SalesPerson = None
        self.Remark = None
        self.IsAgreePrivacy = None
        self.PrivacyTextName = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.Source = params.get("Source")
        self.Platform = params.get("Platform")
        self.AppPackage = params.get("AppPackage")
        self.AppName = params.get("AppName")
        self.AppVersion = params.get("AppVersion")
        self.FileID = params.get("FileID")
        self.AppDownloadUrl = params.get("AppDownloadUrl")
        self.PrivacyTextUrl = params.get("PrivacyTextUrl")
        self.ContactName = params.get("ContactName")
        self.TelNumber = params.get("TelNumber")
        self.Email = params.get("Email")
        self.CorpName = params.get("CorpName")
        self.SalesPerson = params.get("SalesPerson")
        self.Remark = params.get("Remark")
        self.IsAgreePrivacy = params.get("IsAgreePrivacy")
        self.PrivacyTextName = params.get("PrivacyTextName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppScanTaskResponse(AbstractModel):
    """CreateAppScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Result: int
        :param TaskID: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskID: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.TaskID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.TaskID = params.get("TaskID")
        self.RequestId = params.get("RequestId")


class DescribeFileTicketRequest(AbstractModel):
    """DescribeFileTicket请求参数结构体

    """

    def __init__(self):
        r"""
        :param Source: 任务来源, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android), 3:app漏洞扫描;
        :type Source: int
        :param Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        """
        self.Source = None
        self.Platform = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileTicketResponse(AbstractModel):
    """DescribeFileTicket返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Result: int
        :param UploadUrl: 上传url(任务来源为2时:Post方法（100:apk,101:txt）, 任务来源为1时:put方法)
        :type UploadUrl: str
        :param UploadSign: 上传url鉴权信息(任务来源为1时上传需要, Authorization参数值)
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadSign: str
        :param FildID: 上传文件ID(任务来源为1时提交诊断任务需要)
注意：此字段可能返回 null，表示取不到有效值。
        :type FildID: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.UploadUrl = None
        self.UploadSign = None
        self.FildID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.UploadUrl = params.get("UploadUrl")
        self.UploadSign = params.get("UploadSign")
        self.FildID = params.get("FildID")
        self.RequestId = params.get("RequestId")


class DescribeResourceUsageInfoRequest(AbstractModel):
    """DescribeResourceUsageInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param PriceName: 资源计费项名称(为空时，则根据Source，TaskType和Platform进行查询)
        :type PriceName: str
        :param TaskType: 任务类型, 0:基础版, 1:专家版
        :type TaskType: int
        :param Platform: 应用平台, 0:android
        :type Platform: int
        :param Source: 任务来源, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android), 3:app漏洞扫描;
        :type Source: int
        """
        self.PriceName = None
        self.TaskType = None
        self.Platform = None
        self.Source = None


    def _deserialize(self, params):
        self.PriceName = params.get("PriceName")
        self.TaskType = params.get("TaskType")
        self.Platform = params.get("Platform")
        self.Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceUsageInfoResponse(AbstractModel):
    """DescribeResourceUsageInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值, 0:成功, 其他值请查看“返回值”定义，暂时未定
        :type Result: int
        :param Data: 资源使用信息
        :type Data: :class:`tencentcloud.acp.v20220105.models.ResourceUsageInfoData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        if params.get("Data") is not None:
            self.Data = ResourceUsageInfoData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeScanTaskListRequest(AbstractModel):
    """DescribeScanTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Source: 任务来源, -1:所有, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android), 3:app漏洞扫描;
        :type Source: int
        :param Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param TaskStatuses: 任务状态,可多值查询,例如:"1,2,3" 0:默认值(待检测/待咨询), 1.检测中, 2:待评估, 3:评估中, 4:任务完成/咨询完成, 5:任务失败, 6:咨询中;
        :type TaskStatuses: str
        :param TaskTypes: 任务类型,可多值查询,采用逗号分隔,例如:"0,1" 0:基础版, 1:专家版, 2:本地化
        :type TaskTypes: str
        :param PageNo: 页码
        :type PageNo: int
        :param PageSize: 页码大小
        :type PageSize: int
        :param AppName: 应用名称或小程序名称(可选参数)
        :type AppName: str
        :param StartTime: 查询时间范围, 查询开始时间(2021-09-30 或 2021-09-30 10:57:34)
        :type StartTime: str
        :param EndTime: 查询时间范围, 查询结束时间(2021-09-30 或 2021-09-30 10:57:34)
        :type EndTime: str
        """
        self.Source = None
        self.Platform = None
        self.TaskStatuses = None
        self.TaskTypes = None
        self.PageNo = None
        self.PageSize = None
        self.AppName = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Platform = params.get("Platform")
        self.TaskStatuses = params.get("TaskStatuses")
        self.TaskTypes = params.get("TaskTypes")
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.AppName = params.get("AppName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanTaskListResponse(AbstractModel):
    """DescribeScanTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Result: int
        :param Total: 任务总数量
        :type Total: int
        :param Data: 诊断任务数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of AppTaskData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Total = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Total = params.get("Total")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = AppTaskData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeScanTaskReportUrlRequest(AbstractModel):
    """DescribeScanTaskReportUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Source: 任务来源, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android), 3:app漏洞扫描;
        :type Source: int
        :param Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param TaskID: 任务id
        :type TaskID: str
        :param TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        :param ReportType: 报告类型, 0:诊断报告, 1:堆栈报告, 2:视频证据(预留), 3:报告json结果
        :type ReportType: int
        """
        self.Source = None
        self.Platform = None
        self.TaskID = None
        self.TaskType = None
        self.ReportType = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Platform = params.get("Platform")
        self.TaskID = params.get("TaskID")
        self.TaskType = params.get("TaskType")
        self.ReportType = params.get("ReportType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanTaskReportUrlResponse(AbstractModel):
    """DescribeScanTaskReportUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Result: int
        :param ReportUrl: 诊断报告/堆栈信息/报告json结果下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportUrl: str
        :param ReportTitle: 诊断报告/堆栈/报告json结果的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportTitle: str
        :param ReportResult: 诊断json结果内容
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportResult: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.ReportUrl = None
        self.ReportTitle = None
        self.ReportResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.ReportUrl = params.get("ReportUrl")
        self.ReportTitle = params.get("ReportTitle")
        self.ReportResult = params.get("ReportResult")
        self.RequestId = params.get("RequestId")


class DescribeScanTaskStatusRequest(AbstractModel):
    """DescribeScanTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Source: 任务来源, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android), 3:app漏洞扫描;
        :type Source: int
        :param Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param TaskID: 任务id
        :type TaskID: str
        :param TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        """
        self.Source = None
        self.Platform = None
        self.TaskID = None
        self.TaskType = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Platform = params.get("Platform")
        self.TaskID = params.get("TaskID")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanTaskStatusResponse(AbstractModel):
    """DescribeScanTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Result: int
        :param Status: 0:默认值(待检测/待咨询), 1.检测中,  4:任务完成/咨询完成, 5:任务失败, 6:咨询中;
        :type Status: int
        :param ErrMsg: 诊断失败的错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param FlowSteps: 任务流详情
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowSteps: list of TaskFlowStepsInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Status = None
        self.ErrMsg = None
        self.FlowSteps = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Status = params.get("Status")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("FlowSteps") is not None:
            self.FlowSteps = []
            for item in params.get("FlowSteps"):
                obj = TaskFlowStepsInfo()
                obj._deserialize(item)
                self.FlowSteps.append(obj)
        self.RequestId = params.get("RequestId")


class ResourceUsageInfoData(AbstractModel):
    """资源使用情况信息

    """

    def __init__(self):
        r"""
        :param ResourceName: 资源计费项名称
        :type ResourceName: str
        :param Total: 资源总数
        :type Total: int
        :param UnusedCount: 未使用资源数
        :type UnusedCount: int
        """
        self.ResourceName = None
        self.Total = None
        self.UnusedCount = None


    def _deserialize(self, params):
        self.ResourceName = params.get("ResourceName")
        self.Total = params.get("Total")
        self.UnusedCount = params.get("UnusedCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskFlowStepsInfo(AbstractModel):
    """任务流步骤详情

    """

    def __init__(self):
        r"""
        :param FlowNo: 流程编号
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowNo: str
        :param FlowName: 流程名称
        :type FlowName: str
        :param FlowStatus: 流程状态, 其他值:进行中, 2:成功, 3:失败
        :type FlowStatus: int
        :param FlowStateDesc: 流程状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowStateDesc: str
        :param StartTime: 流程启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 流程完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self.FlowNo = None
        self.FlowName = None
        self.FlowStatus = None
        self.FlowStateDesc = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.FlowNo = params.get("FlowNo")
        self.FlowName = params.get("FlowName")
        self.FlowStatus = params.get("FlowStatus")
        self.FlowStateDesc = params.get("FlowStateDesc")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        