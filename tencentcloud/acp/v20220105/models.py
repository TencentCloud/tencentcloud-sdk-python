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
        :param _AppPackage: App包名
        :type AppPackage: str
        :param _AppName: App名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AppName: str
        :param _AppVersion: App版本
注意：此字段可能返回 null，表示取不到有效值。
        :type AppVersion: str
        :param _Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param _ReportUrl: App隐私诊断报告下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportUrl: str
        :param _ReportTitle: App隐私诊断报告名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportTitle: str
        :param _BehaviorUrl: App诊断堆栈报告下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type BehaviorUrl: str
        :param _BehaviorTitle: App诊断堆栈报告名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BehaviorTitle: str
        :param _HighRiskCount: 诊断高风险项数量
注意：此字段可能返回 null，表示取不到有效值。
        :type HighRiskCount: int
        :param _PrivacyTextName: 隐私申明文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivacyTextName: str
        :param _SoftwareMD5: 软件MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type SoftwareMD5: str
        :param _PrivacyTextMD5: 隐私文本MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivacyTextMD5: str
        """
        self._AppPackage = None
        self._AppName = None
        self._AppVersion = None
        self._Platform = None
        self._ReportUrl = None
        self._ReportTitle = None
        self._BehaviorUrl = None
        self._BehaviorTitle = None
        self._HighRiskCount = None
        self._PrivacyTextName = None
        self._SoftwareMD5 = None
        self._PrivacyTextMD5 = None

    @property
    def AppPackage(self):
        return self._AppPackage

    @AppPackage.setter
    def AppPackage(self, AppPackage):
        self._AppPackage = AppPackage

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ReportUrl(self):
        return self._ReportUrl

    @ReportUrl.setter
    def ReportUrl(self, ReportUrl):
        self._ReportUrl = ReportUrl

    @property
    def ReportTitle(self):
        return self._ReportTitle

    @ReportTitle.setter
    def ReportTitle(self, ReportTitle):
        self._ReportTitle = ReportTitle

    @property
    def BehaviorUrl(self):
        return self._BehaviorUrl

    @BehaviorUrl.setter
    def BehaviorUrl(self, BehaviorUrl):
        self._BehaviorUrl = BehaviorUrl

    @property
    def BehaviorTitle(self):
        return self._BehaviorTitle

    @BehaviorTitle.setter
    def BehaviorTitle(self, BehaviorTitle):
        self._BehaviorTitle = BehaviorTitle

    @property
    def HighRiskCount(self):
        return self._HighRiskCount

    @HighRiskCount.setter
    def HighRiskCount(self, HighRiskCount):
        self._HighRiskCount = HighRiskCount

    @property
    def PrivacyTextName(self):
        return self._PrivacyTextName

    @PrivacyTextName.setter
    def PrivacyTextName(self, PrivacyTextName):
        self._PrivacyTextName = PrivacyTextName

    @property
    def SoftwareMD5(self):
        return self._SoftwareMD5

    @SoftwareMD5.setter
    def SoftwareMD5(self, SoftwareMD5):
        self._SoftwareMD5 = SoftwareMD5

    @property
    def PrivacyTextMD5(self):
        return self._PrivacyTextMD5

    @PrivacyTextMD5.setter
    def PrivacyTextMD5(self, PrivacyTextMD5):
        self._PrivacyTextMD5 = PrivacyTextMD5


    def _deserialize(self, params):
        self._AppPackage = params.get("AppPackage")
        self._AppName = params.get("AppName")
        self._AppVersion = params.get("AppVersion")
        self._Platform = params.get("Platform")
        self._ReportUrl = params.get("ReportUrl")
        self._ReportTitle = params.get("ReportTitle")
        self._BehaviorUrl = params.get("BehaviorUrl")
        self._BehaviorTitle = params.get("BehaviorTitle")
        self._HighRiskCount = params.get("HighRiskCount")
        self._PrivacyTextName = params.get("PrivacyTextName")
        self._SoftwareMD5 = params.get("SoftwareMD5")
        self._PrivacyTextMD5 = params.get("PrivacyTextMD5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTaskData(AbstractModel):
    """应用合规隐私诊断任务数据

    """

    def __init__(self):
        r"""
        :param _TaskID: 任务ID
        :type TaskID: str
        :param _TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        :param _TaskStatus: 0:默认值(待检测/待咨询), 1.检测中, 2:待评估, 3:评估中, 4:任务完成/咨询完成, 5:任务失败, 6:咨询中;
        :type TaskStatus: int
        :param _TaskErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskErrMsg: str
        :param _Source: 任务来源,0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android)
        :type Source: int
        :param _AppInfo: 应用信息
        :type AppInfo: :class:`tencentcloud.acp.v20220105.models.AppInfoItem`
        :param _StartTime: 任务启动时间
        :type StartTime: str
        :param _EndTime: 任务完成时间(更新时间)
        :type EndTime: str
        :param _ContactName: 联系人信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactName: str
        """
        self._TaskID = None
        self._TaskType = None
        self._TaskStatus = None
        self._TaskErrMsg = None
        self._Source = None
        self._AppInfo = None
        self._StartTime = None
        self._EndTime = None
        self._ContactName = None

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskErrMsg(self):
        return self._TaskErrMsg

    @TaskErrMsg.setter
    def TaskErrMsg(self, TaskErrMsg):
        self._TaskErrMsg = TaskErrMsg

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def AppInfo(self):
        return self._AppInfo

    @AppInfo.setter
    def AppInfo(self, AppInfo):
        self._AppInfo = AppInfo

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

    @property
    def ContactName(self):
        return self._ContactName

    @ContactName.setter
    def ContactName(self, ContactName):
        self._ContactName = ContactName


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        self._TaskType = params.get("TaskType")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskErrMsg = params.get("TaskErrMsg")
        self._Source = params.get("Source")
        if params.get("AppInfo") is not None:
            self._AppInfo = AppInfoItem()
            self._AppInfo._deserialize(params.get("AppInfo"))
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ContactName = params.get("ContactName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppScanTaskRepeatRequest(AbstractModel):
    """CreateAppScanTaskRepeat请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Source: 任务来源, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android), 3:app漏洞扫描;
        :type Source: int
        :param _Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param _TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        :param _OrgTaskID: 原诊断任务ID
        :type OrgTaskID: str
        :param _AppPackage: App包名
        :type AppPackage: str
        :param _FileID: 上传的文件ID(任务来源为1时必填)
        :type FileID: str
        :param _AppDownloadUrl: 软件下载链接地址(任务来源为2时必填)
        :type AppDownloadUrl: str
        :param _PrivacyTextUrl: 隐私文本下载地址(任务来源为2时必填)
        :type PrivacyTextUrl: str
        :param _AppName: 应用名称
        :type AppName: str
        :param _PrivacyTextName: 隐私申明文件名称
        :type PrivacyTextName: str
        :param _AppSha1: 软件Sha1值(PrivacyTextMD5不为空时必填)
        :type AppSha1: str
        :param _PrivacyTextMD5: 隐私申明文本md5(AppSha1不为空时必填)
        :type PrivacyTextMD5: str
        """
        self._Source = None
        self._Platform = None
        self._TaskType = None
        self._OrgTaskID = None
        self._AppPackage = None
        self._FileID = None
        self._AppDownloadUrl = None
        self._PrivacyTextUrl = None
        self._AppName = None
        self._PrivacyTextName = None
        self._AppSha1 = None
        self._PrivacyTextMD5 = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def OrgTaskID(self):
        return self._OrgTaskID

    @OrgTaskID.setter
    def OrgTaskID(self, OrgTaskID):
        self._OrgTaskID = OrgTaskID

    @property
    def AppPackage(self):
        return self._AppPackage

    @AppPackage.setter
    def AppPackage(self, AppPackage):
        self._AppPackage = AppPackage

    @property
    def FileID(self):
        return self._FileID

    @FileID.setter
    def FileID(self, FileID):
        self._FileID = FileID

    @property
    def AppDownloadUrl(self):
        return self._AppDownloadUrl

    @AppDownloadUrl.setter
    def AppDownloadUrl(self, AppDownloadUrl):
        self._AppDownloadUrl = AppDownloadUrl

    @property
    def PrivacyTextUrl(self):
        return self._PrivacyTextUrl

    @PrivacyTextUrl.setter
    def PrivacyTextUrl(self, PrivacyTextUrl):
        self._PrivacyTextUrl = PrivacyTextUrl

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def PrivacyTextName(self):
        return self._PrivacyTextName

    @PrivacyTextName.setter
    def PrivacyTextName(self, PrivacyTextName):
        self._PrivacyTextName = PrivacyTextName

    @property
    def AppSha1(self):
        return self._AppSha1

    @AppSha1.setter
    def AppSha1(self, AppSha1):
        self._AppSha1 = AppSha1

    @property
    def PrivacyTextMD5(self):
        return self._PrivacyTextMD5

    @PrivacyTextMD5.setter
    def PrivacyTextMD5(self, PrivacyTextMD5):
        self._PrivacyTextMD5 = PrivacyTextMD5


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Platform = params.get("Platform")
        self._TaskType = params.get("TaskType")
        self._OrgTaskID = params.get("OrgTaskID")
        self._AppPackage = params.get("AppPackage")
        self._FileID = params.get("FileID")
        self._AppDownloadUrl = params.get("AppDownloadUrl")
        self._PrivacyTextUrl = params.get("PrivacyTextUrl")
        self._AppName = params.get("AppName")
        self._PrivacyTextName = params.get("PrivacyTextName")
        self._AppSha1 = params.get("AppSha1")
        self._PrivacyTextMD5 = params.get("PrivacyTextMD5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppScanTaskRepeatResponse(AbstractModel):
    """CreateAppScanTaskRepeat返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Result: int
        :param _TaskID: 任务id
        :type TaskID: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._TaskID = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._TaskID = params.get("TaskID")
        self._RequestId = params.get("RequestId")


class CreateAppScanTaskRequest(AbstractModel):
    """CreateAppScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        :param _Source: 任务来源, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android), 3:app漏洞扫描;
        :type Source: int
        :param _Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param _AppPackage: App包名
        :type AppPackage: str
        :param _AppName: App名称(任务来源为2时必填)
        :type AppName: str
        :param _AppVersion: App版本
        :type AppVersion: str
        :param _FileID: 上传的软件文件ID(任务来源为1时必填)
        :type FileID: str
        :param _AppDownloadUrl: 软件下载链接地址(任务来源为2时必填)
        :type AppDownloadUrl: str
        :param _PrivacyTextUrl: 隐私文本下载地址(任务来源为2时必填)
        :type PrivacyTextUrl: str
        :param _ContactName: 联系人信息
        :type ContactName: str
        :param _TelNumber: 联系电话
        :type TelNumber: str
        :param _Email: 公司邮箱
        :type Email: str
        :param _CorpName: 公司名称
        :type CorpName: str
        :param _SalesPerson: 商务对接人员
        :type SalesPerson: str
        :param _Remark: 备注信息
        :type Remark: str
        :param _IsAgreePrivacy: 是否同意隐私条款，0:不同意(默认), 1:同意
        :type IsAgreePrivacy: int
        :param _PrivacyTextName: 隐私申明文件名称
        :type PrivacyTextName: str
        :param _AppSha1: 软件Sha1值(PrivacyTextMD5不为空时必填)
        :type AppSha1: str
        :param _PrivacyTextMD5: 隐私申明文本md5(AppSha1不为空时必填)
        :type PrivacyTextMD5: str
        """
        self._TaskType = None
        self._Source = None
        self._Platform = None
        self._AppPackage = None
        self._AppName = None
        self._AppVersion = None
        self._FileID = None
        self._AppDownloadUrl = None
        self._PrivacyTextUrl = None
        self._ContactName = None
        self._TelNumber = None
        self._Email = None
        self._CorpName = None
        self._SalesPerson = None
        self._Remark = None
        self._IsAgreePrivacy = None
        self._PrivacyTextName = None
        self._AppSha1 = None
        self._PrivacyTextMD5 = None

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def AppPackage(self):
        return self._AppPackage

    @AppPackage.setter
    def AppPackage(self, AppPackage):
        self._AppPackage = AppPackage

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def FileID(self):
        return self._FileID

    @FileID.setter
    def FileID(self, FileID):
        self._FileID = FileID

    @property
    def AppDownloadUrl(self):
        return self._AppDownloadUrl

    @AppDownloadUrl.setter
    def AppDownloadUrl(self, AppDownloadUrl):
        self._AppDownloadUrl = AppDownloadUrl

    @property
    def PrivacyTextUrl(self):
        return self._PrivacyTextUrl

    @PrivacyTextUrl.setter
    def PrivacyTextUrl(self, PrivacyTextUrl):
        self._PrivacyTextUrl = PrivacyTextUrl

    @property
    def ContactName(self):
        return self._ContactName

    @ContactName.setter
    def ContactName(self, ContactName):
        self._ContactName = ContactName

    @property
    def TelNumber(self):
        return self._TelNumber

    @TelNumber.setter
    def TelNumber(self, TelNumber):
        self._TelNumber = TelNumber

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def CorpName(self):
        return self._CorpName

    @CorpName.setter
    def CorpName(self, CorpName):
        self._CorpName = CorpName

    @property
    def SalesPerson(self):
        return self._SalesPerson

    @SalesPerson.setter
    def SalesPerson(self, SalesPerson):
        self._SalesPerson = SalesPerson

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def IsAgreePrivacy(self):
        return self._IsAgreePrivacy

    @IsAgreePrivacy.setter
    def IsAgreePrivacy(self, IsAgreePrivacy):
        self._IsAgreePrivacy = IsAgreePrivacy

    @property
    def PrivacyTextName(self):
        return self._PrivacyTextName

    @PrivacyTextName.setter
    def PrivacyTextName(self, PrivacyTextName):
        self._PrivacyTextName = PrivacyTextName

    @property
    def AppSha1(self):
        return self._AppSha1

    @AppSha1.setter
    def AppSha1(self, AppSha1):
        self._AppSha1 = AppSha1

    @property
    def PrivacyTextMD5(self):
        return self._PrivacyTextMD5

    @PrivacyTextMD5.setter
    def PrivacyTextMD5(self, PrivacyTextMD5):
        self._PrivacyTextMD5 = PrivacyTextMD5


    def _deserialize(self, params):
        self._TaskType = params.get("TaskType")
        self._Source = params.get("Source")
        self._Platform = params.get("Platform")
        self._AppPackage = params.get("AppPackage")
        self._AppName = params.get("AppName")
        self._AppVersion = params.get("AppVersion")
        self._FileID = params.get("FileID")
        self._AppDownloadUrl = params.get("AppDownloadUrl")
        self._PrivacyTextUrl = params.get("PrivacyTextUrl")
        self._ContactName = params.get("ContactName")
        self._TelNumber = params.get("TelNumber")
        self._Email = params.get("Email")
        self._CorpName = params.get("CorpName")
        self._SalesPerson = params.get("SalesPerson")
        self._Remark = params.get("Remark")
        self._IsAgreePrivacy = params.get("IsAgreePrivacy")
        self._PrivacyTextName = params.get("PrivacyTextName")
        self._AppSha1 = params.get("AppSha1")
        self._PrivacyTextMD5 = params.get("PrivacyTextMD5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppScanTaskResponse(AbstractModel):
    """CreateAppScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Result: int
        :param _TaskID: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskID: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._TaskID = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._TaskID = params.get("TaskID")
        self._RequestId = params.get("RequestId")


class DescribeChannelTaskReportUrlRequest(AbstractModel):
    """DescribeChannelTaskReportUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Source: 任务来源, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android), 3:app漏洞扫描;
        :type Source: int
        :param _Platform: 应用平台, 0:android, 1: iOS，2:小程序
        :type Platform: int
        :param _TaskID: 任务id
        :type TaskID: str
        :param _TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        :param _ReportType: 报告类型, 0:诊断报告, 1:堆栈报告, 2:视频证据(预留), 3:报告json结果
        :type ReportType: int
        :param _AppMD5: 子渠道APP MD5值
        :type AppMD5: str
        """
        self._Source = None
        self._Platform = None
        self._TaskID = None
        self._TaskType = None
        self._ReportType = None
        self._AppMD5 = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def ReportType(self):
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def AppMD5(self):
        return self._AppMD5

    @AppMD5.setter
    def AppMD5(self, AppMD5):
        self._AppMD5 = AppMD5


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Platform = params.get("Platform")
        self._TaskID = params.get("TaskID")
        self._TaskType = params.get("TaskType")
        self._ReportType = params.get("ReportType")
        self._AppMD5 = params.get("AppMD5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChannelTaskReportUrlResponse(AbstractModel):
    """DescribeChannelTaskReportUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Result: int
        :param _ReportUrl: 诊断报告/堆栈信息/报告json结果下载链接
        :type ReportUrl: str
        :param _ReportTitle: 诊断报告/堆栈/报告json结果的名称
        :type ReportTitle: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._ReportUrl = None
        self._ReportTitle = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ReportUrl(self):
        return self._ReportUrl

    @ReportUrl.setter
    def ReportUrl(self, ReportUrl):
        self._ReportUrl = ReportUrl

    @property
    def ReportTitle(self):
        return self._ReportTitle

    @ReportTitle.setter
    def ReportTitle(self, ReportTitle):
        self._ReportTitle = ReportTitle

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._ReportUrl = params.get("ReportUrl")
        self._ReportTitle = params.get("ReportTitle")
        self._RequestId = params.get("RequestId")


class DescribeFileTicketRequest(AbstractModel):
    """DescribeFileTicket请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Source: 任务来源, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android), 3:app漏洞扫描;
        :type Source: int
        :param _Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        """
        self._Source = None
        self._Platform = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileTicketResponse(AbstractModel):
    """DescribeFileTicket返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Result: int
        :param _UploadUrl: 上传url(任务来源为2时:Post方法（100:apk,101:txt）, 任务来源为1时:put方法)
        :type UploadUrl: str
        :param _UploadSign: 上传url鉴权信息(任务来源为1时上传需要, Authorization参数值)
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadSign: str
        :param _FildID: 上传文件ID(任务来源为1时提交诊断任务需要)
注意：此字段可能返回 null，表示取不到有效值。
        :type FildID: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._UploadUrl = None
        self._UploadSign = None
        self._FildID = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def UploadUrl(self):
        return self._UploadUrl

    @UploadUrl.setter
    def UploadUrl(self, UploadUrl):
        self._UploadUrl = UploadUrl

    @property
    def UploadSign(self):
        return self._UploadSign

    @UploadSign.setter
    def UploadSign(self, UploadSign):
        self._UploadSign = UploadSign

    @property
    def FildID(self):
        return self._FildID

    @FildID.setter
    def FildID(self, FildID):
        self._FildID = FildID

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._UploadUrl = params.get("UploadUrl")
        self._UploadSign = params.get("UploadSign")
        self._FildID = params.get("FildID")
        self._RequestId = params.get("RequestId")


class DescribeResourceUsageInfoRequest(AbstractModel):
    """DescribeResourceUsageInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PriceName: 资源计费项名称(为空时，则根据Source，TaskType和Platform进行查询)
        :type PriceName: str
        :param _TaskType: 任务类型, 0:基础版, 1:专家版
        :type TaskType: int
        :param _Platform: 应用平台, 0:android
        :type Platform: int
        :param _Source: 任务来源, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android), 3:app漏洞扫描;
        :type Source: int
        """
        self._PriceName = None
        self._TaskType = None
        self._Platform = None
        self._Source = None

    @property
    def PriceName(self):
        return self._PriceName

    @PriceName.setter
    def PriceName(self, PriceName):
        self._PriceName = PriceName

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source


    def _deserialize(self, params):
        self._PriceName = params.get("PriceName")
        self._TaskType = params.get("TaskType")
        self._Platform = params.get("Platform")
        self._Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceUsageInfoResponse(AbstractModel):
    """DescribeResourceUsageInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值, 0:成功, 其他值请查看“返回值”定义，暂时未定
        :type Result: int
        :param _Data: 资源使用信息
        :type Data: :class:`tencentcloud.acp.v20220105.models.ResourceUsageInfoData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Data = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        if params.get("Data") is not None:
            self._Data = ResourceUsageInfoData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeScanTaskListRequest(AbstractModel):
    """DescribeScanTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Source: 任务来源, -1:所有, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android), 3:app漏洞扫描;
        :type Source: int
        :param _Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param _TaskStatuses: 任务状态,可多值查询,例如:"1,2,3" 0:默认值(待检测/待咨询), 1.检测中, 2:待评估, 3:评估中, 4:任务完成/咨询完成, 5:任务失败, 6:咨询中;
        :type TaskStatuses: str
        :param _TaskTypes: 任务类型,可多值查询,采用逗号分隔,例如:"0,1" 0:基础版, 1:专家版, 2:本地化
        :type TaskTypes: str
        :param _PageNo: 页码
        :type PageNo: int
        :param _PageSize: 页码大小
        :type PageSize: int
        :param _AppName: 应用名称或小程序名称(可选参数)
        :type AppName: str
        :param _StartTime: 查询时间范围, 查询开始时间(2021-09-30 或 2021-09-30 10:57:34)
        :type StartTime: str
        :param _EndTime: 查询时间范围, 查询结束时间(2021-09-30 或 2021-09-30 10:57:34)
        :type EndTime: str
        """
        self._Source = None
        self._Platform = None
        self._TaskStatuses = None
        self._TaskTypes = None
        self._PageNo = None
        self._PageSize = None
        self._AppName = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def TaskStatuses(self):
        return self._TaskStatuses

    @TaskStatuses.setter
    def TaskStatuses(self, TaskStatuses):
        self._TaskStatuses = TaskStatuses

    @property
    def TaskTypes(self):
        return self._TaskTypes

    @TaskTypes.setter
    def TaskTypes(self, TaskTypes):
        self._TaskTypes = TaskTypes

    @property
    def PageNo(self):
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

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
        self._Source = params.get("Source")
        self._Platform = params.get("Platform")
        self._TaskStatuses = params.get("TaskStatuses")
        self._TaskTypes = params.get("TaskTypes")
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._AppName = params.get("AppName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanTaskListResponse(AbstractModel):
    """DescribeScanTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Result: int
        :param _Total: 任务总数量
        :type Total: int
        :param _Data: 诊断任务数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of AppTaskData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Total = None
        self._Data = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        self._Result = params.get("Result")
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AppTaskData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScanTaskReportUrlRequest(AbstractModel):
    """DescribeScanTaskReportUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Source: 任务来源, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android), 3:app漏洞扫描;
        :type Source: int
        :param _Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param _TaskID: 任务id
        :type TaskID: str
        :param _TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        :param _ReportType: 报告类型, 0:诊断报告, 1:堆栈报告, 2:视频证据(预留), 3:报告json结果
        :type ReportType: int
        """
        self._Source = None
        self._Platform = None
        self._TaskID = None
        self._TaskType = None
        self._ReportType = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def ReportType(self):
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Platform = params.get("Platform")
        self._TaskID = params.get("TaskID")
        self._TaskType = params.get("TaskType")
        self._ReportType = params.get("ReportType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanTaskReportUrlResponse(AbstractModel):
    """DescribeScanTaskReportUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Result: int
        :param _ReportUrl: 诊断报告/堆栈信息/报告json结果下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportUrl: str
        :param _ReportTitle: 诊断报告/堆栈/报告json结果的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportTitle: str
        :param _ReportResult: 诊断json结果内容
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportResult: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._ReportUrl = None
        self._ReportTitle = None
        self._ReportResult = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ReportUrl(self):
        return self._ReportUrl

    @ReportUrl.setter
    def ReportUrl(self, ReportUrl):
        self._ReportUrl = ReportUrl

    @property
    def ReportTitle(self):
        return self._ReportTitle

    @ReportTitle.setter
    def ReportTitle(self, ReportTitle):
        self._ReportTitle = ReportTitle

    @property
    def ReportResult(self):
        return self._ReportResult

    @ReportResult.setter
    def ReportResult(self, ReportResult):
        self._ReportResult = ReportResult

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._ReportUrl = params.get("ReportUrl")
        self._ReportTitle = params.get("ReportTitle")
        self._ReportResult = params.get("ReportResult")
        self._RequestId = params.get("RequestId")


class DescribeScanTaskStatusRequest(AbstractModel):
    """DescribeScanTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Source: 任务来源, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android), 3:app漏洞扫描;
        :type Source: int
        :param _Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param _TaskID: 任务id
        :type TaskID: str
        :param _TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        """
        self._Source = None
        self._Platform = None
        self._TaskID = None
        self._TaskType = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Platform = params.get("Platform")
        self._TaskID = params.get("TaskID")
        self._TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanTaskStatusResponse(AbstractModel):
    """DescribeScanTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Result: int
        :param _Status: 0:默认值(待检测/待咨询), 1.检测中,  4:任务完成/咨询完成, 5:任务失败, 6:咨询中;
        :type Status: int
        :param _ErrMsg: 诊断失败的错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param _FlowSteps: 任务流详情
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowSteps: list of TaskFlowStepsInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Status = None
        self._ErrMsg = None
        self._FlowSteps = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def FlowSteps(self):
        return self._FlowSteps

    @FlowSteps.setter
    def FlowSteps(self, FlowSteps):
        self._FlowSteps = FlowSteps

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Status = params.get("Status")
        self._ErrMsg = params.get("ErrMsg")
        if params.get("FlowSteps") is not None:
            self._FlowSteps = []
            for item in params.get("FlowSteps"):
                obj = TaskFlowStepsInfo()
                obj._deserialize(item)
                self._FlowSteps.append(obj)
        self._RequestId = params.get("RequestId")


class ResourceUsageInfoData(AbstractModel):
    """资源使用情况信息

    """

    def __init__(self):
        r"""
        :param _ResourceName: 资源计费项名称
        :type ResourceName: str
        :param _Total: 资源总数
        :type Total: int
        :param _UnusedCount: 未使用资源数
        :type UnusedCount: int
        """
        self._ResourceName = None
        self._Total = None
        self._UnusedCount = None

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def UnusedCount(self):
        return self._UnusedCount

    @UnusedCount.setter
    def UnusedCount(self, UnusedCount):
        self._UnusedCount = UnusedCount


    def _deserialize(self, params):
        self._ResourceName = params.get("ResourceName")
        self._Total = params.get("Total")
        self._UnusedCount = params.get("UnusedCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskFlowStepsInfo(AbstractModel):
    """任务流步骤详情

    """

    def __init__(self):
        r"""
        :param _FlowNo: 流程编号
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowNo: str
        :param _FlowName: 流程名称
        :type FlowName: str
        :param _FlowStatus: 流程状态, 其他值:进行中, 2:成功, 3:失败
        :type FlowStatus: int
        :param _FlowStateDesc: 流程状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowStateDesc: str
        :param _StartTime: 流程启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 流程完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self._FlowNo = None
        self._FlowName = None
        self._FlowStatus = None
        self._FlowStateDesc = None
        self._StartTime = None
        self._EndTime = None

    @property
    def FlowNo(self):
        return self._FlowNo

    @FlowNo.setter
    def FlowNo(self, FlowNo):
        self._FlowNo = FlowNo

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowStatus(self):
        return self._FlowStatus

    @FlowStatus.setter
    def FlowStatus(self, FlowStatus):
        self._FlowStatus = FlowStatus

    @property
    def FlowStateDesc(self):
        return self._FlowStateDesc

    @FlowStateDesc.setter
    def FlowStateDesc(self, FlowStateDesc):
        self._FlowStateDesc = FlowStateDesc

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
        self._FlowNo = params.get("FlowNo")
        self._FlowName = params.get("FlowName")
        self._FlowStatus = params.get("FlowStatus")
        self._FlowStateDesc = params.get("FlowStateDesc")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        