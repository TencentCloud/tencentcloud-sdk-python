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
    """隐私合规应用信息

    """

    def __init__(self):
        r"""
        :param AppPackage: 小程序apiiid
        :type AppPackage: str
        :param AppName: 小程序应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AppName: str
        :param AppVersion: 小程序应用版本
注意：此字段可能返回 null，表示取不到有效值。
        :type AppVersion: str
        :param Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param ReportUrl: 小程序隐私诊断报告下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportUrl: str
        :param ReportTitle: 小程序隐私诊断报告名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportTitle: str
        :param BehaviorUrl: 小程序隐私诊断堆栈报告下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type BehaviorUrl: str
        :param BehaviorTitle: 小程序隐私诊断堆栈报告名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BehaviorTitle: str
        :param HighRiskCount: 诊断风险项数量
注意：此字段可能返回 null，表示取不到有效值。
        :type HighRiskCount: int
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTaskData(AbstractModel):
    """应用隐私合规诊断任务数据

    """

    def __init__(self):
        r"""
        :param TaskID: 任务id
        :type TaskID: str
        :param TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        :param TaskStatus: 0:默认值(待检测/待咨询), 1.检测中, 2:待评估, 3:评估中, 4:任务完成/咨询完成, 5:任务失败, 6:咨询中;
        :type TaskStatus: int
        :param TaskErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskErrMsg: str
        :param Source: 来源,0:默认值(私域), 1:灵犀, 2:灵鲲
        :type Source: int
        :param AppInfo: 应用信息
        :type AppInfo: :class:`tencentcloud.mmps.v20200710.models.AppInfoItem`
        :param StartTime: 任务启动时间
        :type StartTime: str
        :param EndTime: 任务完成时间(更新时间)
        :type EndTime: str
        """
        self.TaskID = None
        self.TaskType = None
        self.TaskStatus = None
        self.TaskErrMsg = None
        self.Source = None
        self.AppInfo = None
        self.StartTime = None
        self.EndTime = None


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
        :param TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        :param Source: 任务来源, 0:默认值(私域), 1:灵犀, 2:灵鲲;
        :type Source: int
        :param AppPackage: 小程序AppID
        :type AppPackage: str
        :param Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param OrgTaskID: 原诊断任务ID
        :type OrgTaskID: str
        """
        self.TaskType = None
        self.Source = None
        self.AppPackage = None
        self.Platform = None
        self.OrgTaskID = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.Source = params.get("Source")
        self.AppPackage = params.get("AppPackage")
        self.Platform = params.get("Platform")
        self.OrgTaskID = params.get("OrgTaskID")
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
        :param Source: 任务来源, 0:默认值(私域), 1:灵犀, 2:灵鲲;
        :type Source: int
        :param AppPackage: 小程序AppID
        :type AppPackage: str
        :param Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param AppName: 小程序名称
        :type AppName: str
        :param AppVersion: 小程序版本
        :type AppVersion: str
        :param ContactName: 联系人信息
        :type ContactName: str
        :param TelNumber: 联系电话
        :type TelNumber: str
        :param CorpName: 公司名称
        :type CorpName: str
        :param SalesPerson: 商务对接人员
        :type SalesPerson: str
        :param Email: 公司邮箱
        :type Email: str
        """
        self.TaskType = None
        self.Source = None
        self.AppPackage = None
        self.Platform = None
        self.AppName = None
        self.AppVersion = None
        self.ContactName = None
        self.TelNumber = None
        self.CorpName = None
        self.SalesPerson = None
        self.Email = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.Source = params.get("Source")
        self.AppPackage = params.get("AppPackage")
        self.Platform = params.get("Platform")
        self.AppName = params.get("AppName")
        self.AppVersion = params.get("AppVersion")
        self.ContactName = params.get("ContactName")
        self.TelNumber = params.get("TelNumber")
        self.CorpName = params.get("CorpName")
        self.SalesPerson = params.get("SalesPerson")
        self.Email = params.get("Email")
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


class CreateFlySecMiniAppScanTaskRepeatRequest(AbstractModel):
    """CreateFlySecMiniAppScanTaskRepeat请求参数结构体

    """

    def __init__(self):
        r"""
        :param MiniAppID: 小程序AppID
        :type MiniAppID: str
        :param Mode: 诊断模式 1:基础诊断，2:深度诊断
        :type Mode: int
        :param OrgTaskID: 原任务id
        :type OrgTaskID: str
        :param MiniAppTestAccount: 小程序测试账号(自有账号体系需提供,其他情况不需要)
        :type MiniAppTestAccount: str
        :param MiniAppTestPwd: 小程序测试密码(自有账号体系需提供,其他情况不需要)
        :type MiniAppTestPwd: str
        :param ScanVersion: 诊断扫描版本 0:正式版 1:体验版
        :type ScanVersion: int
        """
        self.MiniAppID = None
        self.Mode = None
        self.OrgTaskID = None
        self.MiniAppTestAccount = None
        self.MiniAppTestPwd = None
        self.ScanVersion = None


    def _deserialize(self, params):
        self.MiniAppID = params.get("MiniAppID")
        self.Mode = params.get("Mode")
        self.OrgTaskID = params.get("OrgTaskID")
        self.MiniAppTestAccount = params.get("MiniAppTestAccount")
        self.MiniAppTestPwd = params.get("MiniAppTestPwd")
        self.ScanVersion = params.get("ScanVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlySecMiniAppScanTaskRepeatResponse(AbstractModel):
    """CreateFlySecMiniAppScanTaskRepeat返回参数结构体

    """

    def __init__(self):
        r"""
        :param Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param TaskID: 任务id
        :type TaskID: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ret = None
        self.TaskID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ret = params.get("Ret")
        self.TaskID = params.get("TaskID")
        self.RequestId = params.get("RequestId")


class CreateFlySecMiniAppScanTaskRequest(AbstractModel):
    """CreateFlySecMiniAppScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param MiniAppID: 小程序AppID
        :type MiniAppID: str
        :param Mode: 诊断模式 1:基础诊断，2:深度诊断
        :type Mode: int
        :param MiniAppTestAccount: 小程序测试账号(自有账号体系需提供,其他情况不需要)
        :type MiniAppTestAccount: str
        :param MiniAppTestPwd: 小程序测试密码(自有账号体系需提供,其他情况不需要)
        :type MiniAppTestPwd: str
        :param Industry: 小程序所属行业
        :type Industry: str
        :param SurveyContent: 小程序调查问卷json字符串
        :type SurveyContent: str
        :param Mobile: 手机号码
        :type Mobile: str
        :param Email: 邮箱地址
        :type Email: str
        :param SalesPerson: 商务合作接口人
        :type SalesPerson: str
        :param ScanVersion: 诊断扫描版本 0:正式版 1:体验版
        :type ScanVersion: int
        """
        self.MiniAppID = None
        self.Mode = None
        self.MiniAppTestAccount = None
        self.MiniAppTestPwd = None
        self.Industry = None
        self.SurveyContent = None
        self.Mobile = None
        self.Email = None
        self.SalesPerson = None
        self.ScanVersion = None


    def _deserialize(self, params):
        self.MiniAppID = params.get("MiniAppID")
        self.Mode = params.get("Mode")
        self.MiniAppTestAccount = params.get("MiniAppTestAccount")
        self.MiniAppTestPwd = params.get("MiniAppTestPwd")
        self.Industry = params.get("Industry")
        self.SurveyContent = params.get("SurveyContent")
        self.Mobile = params.get("Mobile")
        self.Email = params.get("Email")
        self.SalesPerson = params.get("SalesPerson")
        self.ScanVersion = params.get("ScanVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlySecMiniAppScanTaskResponse(AbstractModel):
    """CreateFlySecMiniAppScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param TaskID: 任务id
        :type TaskID: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ret = None
        self.TaskID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ret = params.get("Ret")
        self.TaskID = params.get("TaskID")
        self.RequestId = params.get("RequestId")


class DescribeBasicDiagnosisResourceUsageInfoRequest(AbstractModel):
    """DescribeBasicDiagnosisResourceUsageInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Mode: 诊断模式 1:基础诊断，2:深度诊断
        :type Mode: int
        """
        self.Mode = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicDiagnosisResourceUsageInfoResponse(AbstractModel):
    """DescribeBasicDiagnosisResourceUsageInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param ResourceName: 资源类型
        :type ResourceName: str
        :param Total: 资源总数
        :type Total: int
        :param UnusedCount: 资源未使用次数
        :type UnusedCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ret = None
        self.ResourceName = None
        self.Total = None
        self.UnusedCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ret = params.get("Ret")
        self.ResourceName = params.get("ResourceName")
        self.Total = params.get("Total")
        self.UnusedCount = params.get("UnusedCount")
        self.RequestId = params.get("RequestId")


class DescribeFlySecMiniAppReportUrlRequest(AbstractModel):
    """DescribeFlySecMiniAppReportUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskID: 任务id
        :type TaskID: str
        :param MiniAppID: 小程序appid
        :type MiniAppID: str
        :param Mode: 诊断方式 1:基础诊断，2:深度诊断
        :type Mode: int
        :param ReportType: 诊断报告类型 0:基础诊断报告, 1:总裁版诊断报告
        :type ReportType: int
        """
        self.TaskID = None
        self.MiniAppID = None
        self.Mode = None
        self.ReportType = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.MiniAppID = params.get("MiniAppID")
        self.Mode = params.get("Mode")
        self.ReportType = params.get("ReportType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlySecMiniAppReportUrlResponse(AbstractModel):
    """DescribeFlySecMiniAppReportUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param Url: 诊断报告下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ret = None
        self.Url = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ret = params.get("Ret")
        self.Url = params.get("Url")
        self.RequestId = params.get("RequestId")


class DescribeFlySecMiniAppScanReportListRequest(AbstractModel):
    """DescribeFlySecMiniAppScanReportList请求参数结构体

    """

    def __init__(self):
        r"""
        :param MiniAppID: 任务id
        :type MiniAppID: str
        :param Mode: 诊断方式 1:基础诊断，2:深度诊断
        :type Mode: int
        :param Status: 诊断状态 -1:查询全部, 0:排队中, 1:成功, 2:失败, 3:进行中
        :type Status: int
        :param Size: 查询数量, 0:查询所有, 其他值:最近几次的诊断数量
        :type Size: int
        :param MiniAppVersion: 小程序版本
        :type MiniAppVersion: str
        """
        self.MiniAppID = None
        self.Mode = None
        self.Status = None
        self.Size = None
        self.MiniAppVersion = None


    def _deserialize(self, params):
        self.MiniAppID = params.get("MiniAppID")
        self.Mode = params.get("Mode")
        self.Status = params.get("Status")
        self.Size = params.get("Size")
        self.MiniAppVersion = params.get("MiniAppVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlySecMiniAppScanReportListResponse(AbstractModel):
    """DescribeFlySecMiniAppScanReportList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param Data: 诊断报告数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of FlySecMiniAppReportData
        :param Total: 诊断任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ret = None
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ret = params.get("Ret")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = FlySecMiniAppReportData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeFlySecMiniAppScanTaskListRequest(AbstractModel):
    """DescribeFlySecMiniAppScanTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Mode: 诊断方式 1:基础诊断，2:深度诊断
        :type Mode: int
        :param Status: 诊断状态 -1:查询全部, 0:排队中, 1:成功, 2:失败, 3:进行中
        :type Status: int
        :param Size: 查询数量, 0:查询所有, 其他值:最近几次的诊断数量
        :type Size: int
        :param MiniAppID: 小程序appid(为空的时候,则查询当前用户诊断的所有小程序)
        :type MiniAppID: str
        """
        self.Mode = None
        self.Status = None
        self.Size = None
        self.MiniAppID = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.Status = params.get("Status")
        self.Size = params.get("Size")
        self.MiniAppID = params.get("MiniAppID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlySecMiniAppScanTaskListResponse(AbstractModel):
    """DescribeFlySecMiniAppScanTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param Data: 诊断任务数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of FlySecMiniAppTaskData
        :param Total: 诊断任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ret = None
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ret = params.get("Ret")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = FlySecMiniAppTaskData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeFlySecMiniAppScanTaskParamRequest(AbstractModel):
    """DescribeFlySecMiniAppScanTaskParam请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskID: 任务id
        :type TaskID: str
        """
        self.TaskID = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlySecMiniAppScanTaskParamResponse(AbstractModel):
    """DescribeFlySecMiniAppScanTaskParam返回参数结构体

    """

    def __init__(self):
        r"""
        :param Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param MiniAppID: 小程序AppID
        :type MiniAppID: str
        :param Mode: 诊断模式 1:基础诊断，2:深度诊断
        :type Mode: int
        :param MiniAppTestAccount: 小程序测试账号(自有账号体系需提供,其他情况不需要)
注意：此字段可能返回 null，表示取不到有效值。
        :type MiniAppTestAccount: str
        :param MiniAppTestPwd: 小程序测试密码(自有账号体系需提供,其他情况不需要)
注意：此字段可能返回 null，表示取不到有效值。
        :type MiniAppTestPwd: str
        :param ScanVersion: 诊断扫描版本 0:正式版 1:体验版
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanVersion: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ret = None
        self.MiniAppID = None
        self.Mode = None
        self.MiniAppTestAccount = None
        self.MiniAppTestPwd = None
        self.ScanVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ret = params.get("Ret")
        self.MiniAppID = params.get("MiniAppID")
        self.Mode = params.get("Mode")
        self.MiniAppTestAccount = params.get("MiniAppTestAccount")
        self.MiniAppTestPwd = params.get("MiniAppTestPwd")
        self.ScanVersion = params.get("ScanVersion")
        self.RequestId = params.get("RequestId")


class DescribeFlySecMiniAppScanTaskStatusRequest(AbstractModel):
    """DescribeFlySecMiniAppScanTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskID: 任务id
        :type TaskID: str
        """
        self.TaskID = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlySecMiniAppScanTaskStatusResponse(AbstractModel):
    """DescribeFlySecMiniAppScanTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param Status: 诊断状态, 0:排队中, 1:成功, 2:失败, 3:进行中
        :type Status: int
        :param Errno: 诊断失败错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type Errno: int
        :param MiniAppName: 小程序名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MiniAppName: str
        :param MiniAppVersion: 小程序版本
注意：此字段可能返回 null，表示取不到有效值。
        :type MiniAppVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ret = None
        self.Status = None
        self.Errno = None
        self.MiniAppName = None
        self.MiniAppVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ret = params.get("Ret")
        self.Status = params.get("Status")
        self.Errno = params.get("Errno")
        self.MiniAppName = params.get("MiniAppName")
        self.MiniAppVersion = params.get("MiniAppVersion")
        self.RequestId = params.get("RequestId")


class DescribeResourceUsageInfoRequest(AbstractModel):
    """DescribeResourceUsageInfo请求参数结构体

    """


class DescribeResourceUsageInfoResponse(AbstractModel):
    """DescribeResourceUsageInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param Data: 安全资源数据列表
        :type Data: list of ResourceUsageInfoData
        :param Total: 安全资源数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ret = None
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ret = params.get("Ret")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceUsageInfoData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeScanTaskListRequest(AbstractModel):
    """DescribeScanTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Source: 任务来源, -1:所有, 0:默认值(私域), 1:灵犀, 2:灵鲲;
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
        :param Data: 诊断任务数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of AppTaskData
        :param Total: 任务总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = AppTaskData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeScanTaskReportUrlRequest(AbstractModel):
    """DescribeScanTaskReportUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Source: 任务来源, 0:默认值(私域), 1:灵犀, 2:灵鲲;
        :type Source: int
        :param TaskID: 任务id
        :type TaskID: str
        :param Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param ReportType: 报告类型, 0:诊断报告, 1:堆栈报告
        :type ReportType: int
        :param TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        """
        self.Source = None
        self.TaskID = None
        self.Platform = None
        self.ReportType = None
        self.TaskType = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.TaskID = params.get("TaskID")
        self.Platform = params.get("Platform")
        self.ReportType = params.get("ReportType")
        self.TaskType = params.get("TaskType")
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
        :param ReportUrl: 诊断报告/堆栈信息下载链接
        :type ReportUrl: str
        :param ReportTitle: 诊断报告/堆栈名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportTitle: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.ReportUrl = None
        self.ReportTitle = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.ReportUrl = params.get("ReportUrl")
        self.ReportTitle = params.get("ReportTitle")
        self.RequestId = params.get("RequestId")


class DescribeScanTaskStatusRequest(AbstractModel):
    """DescribeScanTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        :param Source: 任务来源, 0:默认值(私域), 1:灵犀, 2:灵鲲;
        :type Source: int
        :param TaskID: 任务id
        :type TaskID: str
        :param Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        """
        self.TaskType = None
        self.Source = None
        self.TaskID = None
        self.Platform = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.Source = params.get("Source")
        self.TaskID = params.get("TaskID")
        self.Platform = params.get("Platform")
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


class FlySecMiniAppReportData(AbstractModel):
    """翼扬诊断小程序报告数据

    """

    def __init__(self):
        r"""
        :param TaskID: 任务id
        :type TaskID: str
        :param MiniAppID: 小程序appid
        :type MiniAppID: str
        :param MiniAppName: 小程序名称
        :type MiniAppName: str
        :param MiniAppVersion: 小程序版本
        :type MiniAppVersion: str
        :param Mode: 诊断模式 1:基础诊断，2:深度诊断
        :type Mode: int
        :param Status: 诊断状态, 0:排队中, 1:成功, 2:失败, 3:进行中
        :type Status: int
        :param CreateTime: 诊断时间
        :type CreateTime: int
        :param RiskScore: 诊断得分
        :type RiskScore: str
        :param RiskLevel: 诊断风险等级 1:高风险 2:中风险 3:低风险
        :type RiskLevel: int
        :param RiskItems: 诊断8大维度得分情况(每项总分100分)
        :type RiskItems: :class:`tencentcloud.mmps.v20200710.models.FlySecMiniAppRiskItems`
        """
        self.TaskID = None
        self.MiniAppID = None
        self.MiniAppName = None
        self.MiniAppVersion = None
        self.Mode = None
        self.Status = None
        self.CreateTime = None
        self.RiskScore = None
        self.RiskLevel = None
        self.RiskItems = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.MiniAppID = params.get("MiniAppID")
        self.MiniAppName = params.get("MiniAppName")
        self.MiniAppVersion = params.get("MiniAppVersion")
        self.Mode = params.get("Mode")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.RiskScore = params.get("RiskScore")
        self.RiskLevel = params.get("RiskLevel")
        if params.get("RiskItems") is not None:
            self.RiskItems = FlySecMiniAppRiskItems()
            self.RiskItems._deserialize(params.get("RiskItems"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlySecMiniAppRiskItems(AbstractModel):
    """翼扬诊断小程序的诊断报告风险数据

    """

    def __init__(self):
        r"""
        :param RiskItem1Score: 代码防护(基础诊断)
        :type RiskItem1Score: int
        :param RiskItem2Score: 开发测试信息泄露(基础诊断)
        :type RiskItem2Score: int
        :param RiskItem3Score: 编码规范(基础诊断)
        :type RiskItem3Score: int
        :param RiskItem4Score: 配置风险(基础诊断)
        :type RiskItem4Score: int
        :param RiskItem5Score: 账号安全(基础诊断)
        :type RiskItem5Score: int
        :param RiskItem6Score: 用户信息安全(基础诊断)
        :type RiskItem6Score: int
        :param RiskItem7Score: 内部信息泄露(基础诊断)
        :type RiskItem7Score: int
        :param RiskItem8Score: 其他安全(基础诊断)
        :type RiskItem8Score: int
        """
        self.RiskItem1Score = None
        self.RiskItem2Score = None
        self.RiskItem3Score = None
        self.RiskItem4Score = None
        self.RiskItem5Score = None
        self.RiskItem6Score = None
        self.RiskItem7Score = None
        self.RiskItem8Score = None


    def _deserialize(self, params):
        self.RiskItem1Score = params.get("RiskItem1Score")
        self.RiskItem2Score = params.get("RiskItem2Score")
        self.RiskItem3Score = params.get("RiskItem3Score")
        self.RiskItem4Score = params.get("RiskItem4Score")
        self.RiskItem5Score = params.get("RiskItem5Score")
        self.RiskItem6Score = params.get("RiskItem6Score")
        self.RiskItem7Score = params.get("RiskItem7Score")
        self.RiskItem8Score = params.get("RiskItem8Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlySecMiniAppTaskData(AbstractModel):
    """翼扬诊断小程序任务数据

    """

    def __init__(self):
        r"""
        :param TaskID: 任务id
        :type TaskID: str
        :param MiniAppID: 小程序appid
        :type MiniAppID: str
        :param MiniAppName: 小程序名称
        :type MiniAppName: str
        :param MiniAppVersion: 小程序版本
        :type MiniAppVersion: str
        :param Mode: 诊断模式 1:基础诊断，2:深度诊断
        :type Mode: int
        :param CreateTime: 诊断时间
        :type CreateTime: int
        :param Status: 诊断状态, 0:排队中, 1:成功, 2:失败, 3:进行中
        :type Status: int
        :param Error: 诊断失败错误码
        :type Error: int
        """
        self.TaskID = None
        self.MiniAppID = None
        self.MiniAppName = None
        self.MiniAppVersion = None
        self.Mode = None
        self.CreateTime = None
        self.Status = None
        self.Error = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.MiniAppID = params.get("MiniAppID")
        self.MiniAppName = params.get("MiniAppName")
        self.MiniAppVersion = params.get("MiniAppVersion")
        self.Mode = params.get("Mode")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceUsageInfoData(AbstractModel):
    """翼扬安全资源使用情况

    """

    def __init__(self):
        r"""
        :param ResourceName: 资源名称, 具体名称请查看产品配置
        :type ResourceName: str
        :param Total: 资源总数
        :type Total: int
        :param UnusedCount: 资源未使用次数
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
        