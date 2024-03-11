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
        :param _AppPackage: 小程序apiiid
        :type AppPackage: str
        :param _AppName: 小程序应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AppName: str
        :param _AppVersion: 小程序应用版本
注意：此字段可能返回 null，表示取不到有效值。
        :type AppVersion: str
        :param _Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param _ReportUrl: 小程序隐私诊断报告下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportUrl: str
        :param _ReportTitle: 小程序隐私诊断报告名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportTitle: str
        :param _BehaviorUrl: 小程序隐私诊断堆栈报告下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type BehaviorUrl: str
        :param _BehaviorTitle: 小程序隐私诊断堆栈报告名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BehaviorTitle: str
        :param _HighRiskCount: 诊断风险项数量
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
    """应用隐私合规诊断任务数据

    """

    def __init__(self):
        r"""
        :param _TaskID: 任务id
        :type TaskID: str
        :param _TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        :param _TaskStatus: 0:默认值(待检测/待咨询), 1.检测中, 2:待评估, 3:评估中, 4:任务完成/咨询完成, 5:任务失败, 6:咨询中;
        :type TaskStatus: int
        :param _TaskErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskErrMsg: str
        :param _Source: 任务来源,0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android);
        :type Source: int
        :param _AppInfo: 应用信息
        :type AppInfo: :class:`tencentcloud.mmps.v20200710.models.AppInfoItem`
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
        :param _TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        :param _Source: 任务来源, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android);
        :type Source: int
        :param _AppPackage: 小程序AppID
        :type AppPackage: str
        :param _Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param _OrgTaskID: 原诊断任务ID
        :type OrgTaskID: str
        """
        self._TaskType = None
        self._Source = None
        self._AppPackage = None
        self._Platform = None
        self._OrgTaskID = None

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
    def AppPackage(self):
        return self._AppPackage

    @AppPackage.setter
    def AppPackage(self, AppPackage):
        self._AppPackage = AppPackage

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def OrgTaskID(self):
        return self._OrgTaskID

    @OrgTaskID.setter
    def OrgTaskID(self, OrgTaskID):
        self._OrgTaskID = OrgTaskID


    def _deserialize(self, params):
        self._TaskType = params.get("TaskType")
        self._Source = params.get("Source")
        self._AppPackage = params.get("AppPackage")
        self._Platform = params.get("Platform")
        self._OrgTaskID = params.get("OrgTaskID")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _Source: 任务来源, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android);
        :type Source: int
        :param _AppPackage: 小程序AppID
        :type AppPackage: str
        :param _Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param _AppName: 小程序名称
        :type AppName: str
        :param _AppVersion: 小程序版本
        :type AppVersion: str
        :param _ContactName: 联系人信息
        :type ContactName: str
        :param _TelNumber: 联系电话
        :type TelNumber: str
        :param _CorpName: 公司名称
        :type CorpName: str
        :param _SalesPerson: 商务对接人员
        :type SalesPerson: str
        :param _Email: 公司邮箱
        :type Email: str
        """
        self._TaskType = None
        self._Source = None
        self._AppPackage = None
        self._Platform = None
        self._AppName = None
        self._AppVersion = None
        self._ContactName = None
        self._TelNumber = None
        self._CorpName = None
        self._SalesPerson = None
        self._Email = None

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
    def AppPackage(self):
        return self._AppPackage

    @AppPackage.setter
    def AppPackage(self, AppPackage):
        self._AppPackage = AppPackage

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

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
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email


    def _deserialize(self, params):
        self._TaskType = params.get("TaskType")
        self._Source = params.get("Source")
        self._AppPackage = params.get("AppPackage")
        self._Platform = params.get("Platform")
        self._AppName = params.get("AppName")
        self._AppVersion = params.get("AppVersion")
        self._ContactName = params.get("ContactName")
        self._TelNumber = params.get("TelNumber")
        self._CorpName = params.get("CorpName")
        self._SalesPerson = params.get("SalesPerson")
        self._Email = params.get("Email")
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
        :param _TaskID: 任务id
        :type TaskID: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateFlySecMiniAppProfessionalScanTaskRequest(AbstractModel):
    """CreateFlySecMiniAppProfessionalScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MiniAppID: 小程序AppID
        :type MiniAppID: str
        :param _MiniAppName: 小程序名称
        :type MiniAppName: str
        :param _Mode: 诊断模式 2:深度诊断
        :type Mode: int
        :param _CorpName: 公司名称
        :type CorpName: str
        :param _Mobile: 手机号码
        :type Mobile: str
        :param _Email: 电子邮箱
        :type Email: str
        :param _Remark: 备注信息
        :type Remark: str
        """
        self._MiniAppID = None
        self._MiniAppName = None
        self._Mode = None
        self._CorpName = None
        self._Mobile = None
        self._Email = None
        self._Remark = None

    @property
    def MiniAppID(self):
        return self._MiniAppID

    @MiniAppID.setter
    def MiniAppID(self, MiniAppID):
        self._MiniAppID = MiniAppID

    @property
    def MiniAppName(self):
        return self._MiniAppName

    @MiniAppName.setter
    def MiniAppName(self, MiniAppName):
        self._MiniAppName = MiniAppName

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def CorpName(self):
        return self._CorpName

    @CorpName.setter
    def CorpName(self, CorpName):
        self._CorpName = CorpName

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._MiniAppID = params.get("MiniAppID")
        self._MiniAppName = params.get("MiniAppName")
        self._Mode = params.get("Mode")
        self._CorpName = params.get("CorpName")
        self._Mobile = params.get("Mobile")
        self._Email = params.get("Email")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlySecMiniAppProfessionalScanTaskResponse(AbstractModel):
    """CreateFlySecMiniAppProfessionalScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ret = None
        self._RequestId = None

    @property
    def Ret(self):
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ret = params.get("Ret")
        self._RequestId = params.get("RequestId")


class CreateFlySecMiniAppScanTaskRepeatRequest(AbstractModel):
    """CreateFlySecMiniAppScanTaskRepeat请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MiniAppID: 小程序AppID
        :type MiniAppID: str
        :param _Mode: 诊断模式 1:基础诊断
        :type Mode: int
        :param _OrgTaskID: 原任务id
        :type OrgTaskID: str
        :param _MiniAppTestAccount: 小程序测试账号(自有账号体系需提供,其他情况不需要)
        :type MiniAppTestAccount: str
        :param _MiniAppTestPwd: 小程序测试密码(自有账号体系需提供,其他情况不需要)
        :type MiniAppTestPwd: str
        :param _ScanVersion: 诊断扫描版本 0:正式版 1:体验版
        :type ScanVersion: int
        """
        self._MiniAppID = None
        self._Mode = None
        self._OrgTaskID = None
        self._MiniAppTestAccount = None
        self._MiniAppTestPwd = None
        self._ScanVersion = None

    @property
    def MiniAppID(self):
        return self._MiniAppID

    @MiniAppID.setter
    def MiniAppID(self, MiniAppID):
        self._MiniAppID = MiniAppID

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def OrgTaskID(self):
        return self._OrgTaskID

    @OrgTaskID.setter
    def OrgTaskID(self, OrgTaskID):
        self._OrgTaskID = OrgTaskID

    @property
    def MiniAppTestAccount(self):
        return self._MiniAppTestAccount

    @MiniAppTestAccount.setter
    def MiniAppTestAccount(self, MiniAppTestAccount):
        self._MiniAppTestAccount = MiniAppTestAccount

    @property
    def MiniAppTestPwd(self):
        return self._MiniAppTestPwd

    @MiniAppTestPwd.setter
    def MiniAppTestPwd(self, MiniAppTestPwd):
        self._MiniAppTestPwd = MiniAppTestPwd

    @property
    def ScanVersion(self):
        return self._ScanVersion

    @ScanVersion.setter
    def ScanVersion(self, ScanVersion):
        self._ScanVersion = ScanVersion


    def _deserialize(self, params):
        self._MiniAppID = params.get("MiniAppID")
        self._Mode = params.get("Mode")
        self._OrgTaskID = params.get("OrgTaskID")
        self._MiniAppTestAccount = params.get("MiniAppTestAccount")
        self._MiniAppTestPwd = params.get("MiniAppTestPwd")
        self._ScanVersion = params.get("ScanVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlySecMiniAppScanTaskRepeatResponse(AbstractModel):
    """CreateFlySecMiniAppScanTaskRepeat返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param _TaskID: 任务id
        :type TaskID: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ret = None
        self._TaskID = None
        self._RequestId = None

    @property
    def Ret(self):
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret

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
        self._Ret = params.get("Ret")
        self._TaskID = params.get("TaskID")
        self._RequestId = params.get("RequestId")


class CreateFlySecMiniAppScanTaskRequest(AbstractModel):
    """CreateFlySecMiniAppScanTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MiniAppID: 小程序AppID
        :type MiniAppID: str
        :param _Mode: 诊断模式 1:基础诊断
        :type Mode: int
        :param _MiniAppTestAccount: 小程序测试账号(自有账号体系需提供,其他情况不需要)
        :type MiniAppTestAccount: str
        :param _MiniAppTestPwd: 小程序测试密码(自有账号体系需提供,其他情况不需要)
        :type MiniAppTestPwd: str
        :param _Industry: 小程序所属行业
        :type Industry: str
        :param _SurveyContent: 小程序调查问卷json字符串
        :type SurveyContent: str
        :param _Mobile: 手机号码
        :type Mobile: str
        :param _Email: 邮箱地址
        :type Email: str
        :param _SalesPerson: 商务合作接口人
        :type SalesPerson: str
        :param _ScanVersion: 诊断扫描版本 0:正式版 1:体验版
        :type ScanVersion: int
        """
        self._MiniAppID = None
        self._Mode = None
        self._MiniAppTestAccount = None
        self._MiniAppTestPwd = None
        self._Industry = None
        self._SurveyContent = None
        self._Mobile = None
        self._Email = None
        self._SalesPerson = None
        self._ScanVersion = None

    @property
    def MiniAppID(self):
        return self._MiniAppID

    @MiniAppID.setter
    def MiniAppID(self, MiniAppID):
        self._MiniAppID = MiniAppID

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def MiniAppTestAccount(self):
        return self._MiniAppTestAccount

    @MiniAppTestAccount.setter
    def MiniAppTestAccount(self, MiniAppTestAccount):
        self._MiniAppTestAccount = MiniAppTestAccount

    @property
    def MiniAppTestPwd(self):
        return self._MiniAppTestPwd

    @MiniAppTestPwd.setter
    def MiniAppTestPwd(self, MiniAppTestPwd):
        self._MiniAppTestPwd = MiniAppTestPwd

    @property
    def Industry(self):
        return self._Industry

    @Industry.setter
    def Industry(self, Industry):
        self._Industry = Industry

    @property
    def SurveyContent(self):
        return self._SurveyContent

    @SurveyContent.setter
    def SurveyContent(self, SurveyContent):
        self._SurveyContent = SurveyContent

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def SalesPerson(self):
        return self._SalesPerson

    @SalesPerson.setter
    def SalesPerson(self, SalesPerson):
        self._SalesPerson = SalesPerson

    @property
    def ScanVersion(self):
        return self._ScanVersion

    @ScanVersion.setter
    def ScanVersion(self, ScanVersion):
        self._ScanVersion = ScanVersion


    def _deserialize(self, params):
        self._MiniAppID = params.get("MiniAppID")
        self._Mode = params.get("Mode")
        self._MiniAppTestAccount = params.get("MiniAppTestAccount")
        self._MiniAppTestPwd = params.get("MiniAppTestPwd")
        self._Industry = params.get("Industry")
        self._SurveyContent = params.get("SurveyContent")
        self._Mobile = params.get("Mobile")
        self._Email = params.get("Email")
        self._SalesPerson = params.get("SalesPerson")
        self._ScanVersion = params.get("ScanVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlySecMiniAppScanTaskResponse(AbstractModel):
    """CreateFlySecMiniAppScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param _TaskID: 任务id
        :type TaskID: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ret = None
        self._TaskID = None
        self._RequestId = None

    @property
    def Ret(self):
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret

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
        self._Ret = params.get("Ret")
        self._TaskID = params.get("TaskID")
        self._RequestId = params.get("RequestId")


class DescribeBasicDiagnosisResourceUsageInfoRequest(AbstractModel):
    """DescribeBasicDiagnosisResourceUsageInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Mode: 诊断模式 1:基础诊断，2:深度诊断
        :type Mode: int
        """
        self._Mode = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicDiagnosisResourceUsageInfoResponse(AbstractModel):
    """DescribeBasicDiagnosisResourceUsageInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param _ResourceName: 资源类型
        :type ResourceName: str
        :param _Total: 资源总数
        :type Total: int
        :param _UnusedCount: 资源未使用次数
        :type UnusedCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ret = None
        self._ResourceName = None
        self._Total = None
        self._UnusedCount = None
        self._RequestId = None

    @property
    def Ret(self):
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret

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

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ret = params.get("Ret")
        self._ResourceName = params.get("ResourceName")
        self._Total = params.get("Total")
        self._UnusedCount = params.get("UnusedCount")
        self._RequestId = params.get("RequestId")


class DescribeFlySecMiniAppReportUrlRequest(AbstractModel):
    """DescribeFlySecMiniAppReportUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskID: 任务id
        :type TaskID: str
        :param _MiniAppID: 小程序appid
        :type MiniAppID: str
        :param _Mode: 诊断方式 1:基础诊断，2:深度诊断
        :type Mode: int
        :param _ReportType: 诊断报告类型 0:基础诊断报告，1:总裁版诊断报告，2:诊断报告json结果
        :type ReportType: int
        """
        self._TaskID = None
        self._MiniAppID = None
        self._Mode = None
        self._ReportType = None

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def MiniAppID(self):
        return self._MiniAppID

    @MiniAppID.setter
    def MiniAppID(self, MiniAppID):
        self._MiniAppID = MiniAppID

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def ReportType(self):
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        self._MiniAppID = params.get("MiniAppID")
        self._Mode = params.get("Mode")
        self._ReportType = params.get("ReportType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlySecMiniAppReportUrlResponse(AbstractModel):
    """DescribeFlySecMiniAppReportUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param _Url: 诊断报告下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ret = None
        self._Url = None
        self._RequestId = None

    @property
    def Ret(self):
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ret = params.get("Ret")
        self._Url = params.get("Url")
        self._RequestId = params.get("RequestId")


class DescribeFlySecMiniAppScanReportListRequest(AbstractModel):
    """DescribeFlySecMiniAppScanReportList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MiniAppID: 小程序AppID
        :type MiniAppID: str
        :param _Mode: 诊断方式 1:基础诊断，2:深度诊断
        :type Mode: int
        :param _Status: 诊断状态 -1:查询全部, 0:排队中, 1:成功, 2:失败, 3:进行中
        :type Status: int
        :param _Size: 查询数量, 0:查询所有, 其他值:最近几次的诊断数量
        :type Size: int
        :param _MiniAppVersion: 小程序版本
        :type MiniAppVersion: str
        """
        self._MiniAppID = None
        self._Mode = None
        self._Status = None
        self._Size = None
        self._MiniAppVersion = None

    @property
    def MiniAppID(self):
        return self._MiniAppID

    @MiniAppID.setter
    def MiniAppID(self, MiniAppID):
        self._MiniAppID = MiniAppID

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def MiniAppVersion(self):
        return self._MiniAppVersion

    @MiniAppVersion.setter
    def MiniAppVersion(self, MiniAppVersion):
        self._MiniAppVersion = MiniAppVersion


    def _deserialize(self, params):
        self._MiniAppID = params.get("MiniAppID")
        self._Mode = params.get("Mode")
        self._Status = params.get("Status")
        self._Size = params.get("Size")
        self._MiniAppVersion = params.get("MiniAppVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlySecMiniAppScanReportListResponse(AbstractModel):
    """DescribeFlySecMiniAppScanReportList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param _Data: 诊断报告数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of FlySecMiniAppReportData
        :param _Total: 诊断任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ret = None
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Ret(self):
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ret = params.get("Ret")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = FlySecMiniAppReportData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeFlySecMiniAppScanTaskListRequest(AbstractModel):
    """DescribeFlySecMiniAppScanTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Mode: 诊断方式 1:基础诊断，2:深度诊断
        :type Mode: int
        :param _Status: 诊断状态 -1:查询全部, 0:排队中, 1:成功, 2:失败, 3:进行中
        :type Status: int
        :param _Size: 查询数量, 0:查询所有, 其他值:最近几次的诊断数量
        :type Size: int
        :param _MiniAppID: 小程序appid(为空的时候,则查询当前用户诊断的所有小程序)
        :type MiniAppID: str
        """
        self._Mode = None
        self._Status = None
        self._Size = None
        self._MiniAppID = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def MiniAppID(self):
        return self._MiniAppID

    @MiniAppID.setter
    def MiniAppID(self, MiniAppID):
        self._MiniAppID = MiniAppID


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._Status = params.get("Status")
        self._Size = params.get("Size")
        self._MiniAppID = params.get("MiniAppID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlySecMiniAppScanTaskListResponse(AbstractModel):
    """DescribeFlySecMiniAppScanTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param _Data: 诊断任务数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of FlySecMiniAppTaskData
        :param _Total: 诊断任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ret = None
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Ret(self):
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ret = params.get("Ret")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = FlySecMiniAppTaskData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeFlySecMiniAppScanTaskParamRequest(AbstractModel):
    """DescribeFlySecMiniAppScanTaskParam请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskID: 任务id
        :type TaskID: str
        """
        self._TaskID = None

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlySecMiniAppScanTaskParamResponse(AbstractModel):
    """DescribeFlySecMiniAppScanTaskParam返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param _MiniAppID: 小程序AppID
        :type MiniAppID: str
        :param _Mode: 诊断模式 1:基础诊断，2:深度诊断
        :type Mode: int
        :param _MiniAppTestAccount: 小程序测试账号(自有账号体系需提供,其他情况不需要)
注意：此字段可能返回 null，表示取不到有效值。
        :type MiniAppTestAccount: str
        :param _MiniAppTestPwd: 小程序测试密码(自有账号体系需提供,其他情况不需要)
注意：此字段可能返回 null，表示取不到有效值。
        :type MiniAppTestPwd: str
        :param _ScanVersion: 诊断扫描版本 0:正式版 1:体验版
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanVersion: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ret = None
        self._MiniAppID = None
        self._Mode = None
        self._MiniAppTestAccount = None
        self._MiniAppTestPwd = None
        self._ScanVersion = None
        self._RequestId = None

    @property
    def Ret(self):
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret

    @property
    def MiniAppID(self):
        return self._MiniAppID

    @MiniAppID.setter
    def MiniAppID(self, MiniAppID):
        self._MiniAppID = MiniAppID

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def MiniAppTestAccount(self):
        return self._MiniAppTestAccount

    @MiniAppTestAccount.setter
    def MiniAppTestAccount(self, MiniAppTestAccount):
        self._MiniAppTestAccount = MiniAppTestAccount

    @property
    def MiniAppTestPwd(self):
        return self._MiniAppTestPwd

    @MiniAppTestPwd.setter
    def MiniAppTestPwd(self, MiniAppTestPwd):
        self._MiniAppTestPwd = MiniAppTestPwd

    @property
    def ScanVersion(self):
        return self._ScanVersion

    @ScanVersion.setter
    def ScanVersion(self, ScanVersion):
        self._ScanVersion = ScanVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ret = params.get("Ret")
        self._MiniAppID = params.get("MiniAppID")
        self._Mode = params.get("Mode")
        self._MiniAppTestAccount = params.get("MiniAppTestAccount")
        self._MiniAppTestPwd = params.get("MiniAppTestPwd")
        self._ScanVersion = params.get("ScanVersion")
        self._RequestId = params.get("RequestId")


class DescribeFlySecMiniAppScanTaskStatusRequest(AbstractModel):
    """DescribeFlySecMiniAppScanTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskID: 任务id
        :type TaskID: str
        """
        self._TaskID = None

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlySecMiniAppScanTaskStatusResponse(AbstractModel):
    """DescribeFlySecMiniAppScanTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param _Status: 诊断状态, 0:排队中, 1:成功, 2:失败, 3:进行中
        :type Status: int
        :param _Errno: 诊断失败错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type Errno: int
        :param _MiniAppName: 小程序名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MiniAppName: str
        :param _MiniAppVersion: 小程序版本
注意：此字段可能返回 null，表示取不到有效值。
        :type MiniAppVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ret = None
        self._Status = None
        self._Errno = None
        self._MiniAppName = None
        self._MiniAppVersion = None
        self._RequestId = None

    @property
    def Ret(self):
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Errno(self):
        return self._Errno

    @Errno.setter
    def Errno(self, Errno):
        self._Errno = Errno

    @property
    def MiniAppName(self):
        return self._MiniAppName

    @MiniAppName.setter
    def MiniAppName(self, MiniAppName):
        self._MiniAppName = MiniAppName

    @property
    def MiniAppVersion(self):
        return self._MiniAppVersion

    @MiniAppVersion.setter
    def MiniAppVersion(self, MiniAppVersion):
        self._MiniAppVersion = MiniAppVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ret = params.get("Ret")
        self._Status = params.get("Status")
        self._Errno = params.get("Errno")
        self._MiniAppName = params.get("MiniAppName")
        self._MiniAppVersion = params.get("MiniAppVersion")
        self._RequestId = params.get("RequestId")


class DescribeResourceUsageInfoRequest(AbstractModel):
    """DescribeResourceUsageInfo请求参数结构体

    """


class DescribeResourceUsageInfoResponse(AbstractModel):
    """DescribeResourceUsageInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ret: 返回值, 0:成功, 其他值请查看“返回值”定义
        :type Ret: int
        :param _Data: 安全资源数据列表
        :type Data: list of ResourceUsageInfoData
        :param _Total: 安全资源数量
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ret = None
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Ret(self):
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ret = params.get("Ret")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ResourceUsageInfoData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeScanTaskListRequest(AbstractModel):
    """DescribeScanTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Source: 任务来源, -1:所有, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android);
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
        :param _Data: 诊断任务数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of AppTaskData
        :param _Total: 任务总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Data = None
        self._Total = None
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
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AppTaskData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeScanTaskReportUrlRequest(AbstractModel):
    """DescribeScanTaskReportUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Source: 任务来源, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android);
        :type Source: int
        :param _TaskID: 任务id
        :type TaskID: str
        :param _Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        :param _ReportType: 报告类型, 0:诊断报告, 1:堆栈报告(预留), 2:视频证据(预留), 3:报告json结果
        :type ReportType: int
        :param _TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        """
        self._Source = None
        self._TaskID = None
        self._Platform = None
        self._ReportType = None
        self._TaskType = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ReportType(self):
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._TaskID = params.get("TaskID")
        self._Platform = params.get("Platform")
        self._ReportType = params.get("ReportType")
        self._TaskType = params.get("TaskType")
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
        :param _ReportUrl: 诊断报告/堆栈信息下载链接
        :type ReportUrl: str
        :param _ReportTitle: 诊断报告/堆栈名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportTitle: str
        :param _ReportResult: 诊断json结果内容
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportResult: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :param _TaskType: 任务类型, 0:基础版, 1:专家版, 2:本地化
        :type TaskType: int
        :param _Source: 任务来源, 0:小程序诊断, 1:预留字段(暂未使用), 2:app诊断(android);
        :type Source: int
        :param _TaskID: 任务id
        :type TaskID: str
        :param _Platform: 应用平台, 0:android, 1:ios, 2:小程序
        :type Platform: int
        """
        self._TaskType = None
        self._Source = None
        self._TaskID = None
        self._Platform = None

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
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        self._TaskType = params.get("TaskType")
        self._Source = params.get("Source")
        self._TaskID = params.get("TaskID")
        self._Platform = params.get("Platform")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class FlySecMiniAppReportData(AbstractModel):
    """翼扬诊断小程序报告数据

    """

    def __init__(self):
        r"""
        :param _TaskID: 任务id
        :type TaskID: str
        :param _MiniAppID: 小程序appid
        :type MiniAppID: str
        :param _MiniAppName: 小程序名称
        :type MiniAppName: str
        :param _MiniAppVersion: 小程序版本
        :type MiniAppVersion: str
        :param _Mode: 诊断模式 1:基础诊断，2:深度诊断
        :type Mode: int
        :param _Status: 诊断状态, 0:排队中, 1:成功, 2:失败, 3:进行中
        :type Status: int
        :param _CreateTime: 诊断时间
        :type CreateTime: int
        :param _RiskScore: 诊断得分
        :type RiskScore: str
        :param _RiskLevel: 诊断风险等级 1:高风险 2:中风险 3:低风险
        :type RiskLevel: int
        :param _RiskItems: 诊断8大维度得分情况(每项总分100分)
        :type RiskItems: :class:`tencentcloud.mmps.v20200710.models.FlySecMiniAppRiskItems`
        """
        self._TaskID = None
        self._MiniAppID = None
        self._MiniAppName = None
        self._MiniAppVersion = None
        self._Mode = None
        self._Status = None
        self._CreateTime = None
        self._RiskScore = None
        self._RiskLevel = None
        self._RiskItems = None

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def MiniAppID(self):
        return self._MiniAppID

    @MiniAppID.setter
    def MiniAppID(self, MiniAppID):
        self._MiniAppID = MiniAppID

    @property
    def MiniAppName(self):
        return self._MiniAppName

    @MiniAppName.setter
    def MiniAppName(self, MiniAppName):
        self._MiniAppName = MiniAppName

    @property
    def MiniAppVersion(self):
        return self._MiniAppVersion

    @MiniAppVersion.setter
    def MiniAppVersion(self, MiniAppVersion):
        self._MiniAppVersion = MiniAppVersion

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RiskScore(self):
        return self._RiskScore

    @RiskScore.setter
    def RiskScore(self, RiskScore):
        self._RiskScore = RiskScore

    @property
    def RiskLevel(self):
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RiskItems(self):
        return self._RiskItems

    @RiskItems.setter
    def RiskItems(self, RiskItems):
        self._RiskItems = RiskItems


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        self._MiniAppID = params.get("MiniAppID")
        self._MiniAppName = params.get("MiniAppName")
        self._MiniAppVersion = params.get("MiniAppVersion")
        self._Mode = params.get("Mode")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._RiskScore = params.get("RiskScore")
        self._RiskLevel = params.get("RiskLevel")
        if params.get("RiskItems") is not None:
            self._RiskItems = FlySecMiniAppRiskItems()
            self._RiskItems._deserialize(params.get("RiskItems"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlySecMiniAppRiskItems(AbstractModel):
    """翼扬诊断小程序的诊断报告风险数据

    """

    def __init__(self):
        r"""
        :param _RiskItem1Score: 代码防护(基础诊断)
        :type RiskItem1Score: int
        :param _RiskItem2Score: 开发测试信息泄露(基础诊断)
        :type RiskItem2Score: int
        :param _RiskItem3Score: 编码规范(基础诊断)
        :type RiskItem3Score: int
        :param _RiskItem4Score: 配置风险(基础诊断)
        :type RiskItem4Score: int
        :param _RiskItem5Score: 账号安全(基础诊断)
        :type RiskItem5Score: int
        :param _RiskItem6Score: 用户信息安全(基础诊断)
        :type RiskItem6Score: int
        :param _RiskItem7Score: 内部信息泄露(基础诊断)
        :type RiskItem7Score: int
        :param _RiskItem8Score: 其他安全(基础诊断)
        :type RiskItem8Score: int
        """
        self._RiskItem1Score = None
        self._RiskItem2Score = None
        self._RiskItem3Score = None
        self._RiskItem4Score = None
        self._RiskItem5Score = None
        self._RiskItem6Score = None
        self._RiskItem7Score = None
        self._RiskItem8Score = None

    @property
    def RiskItem1Score(self):
        return self._RiskItem1Score

    @RiskItem1Score.setter
    def RiskItem1Score(self, RiskItem1Score):
        self._RiskItem1Score = RiskItem1Score

    @property
    def RiskItem2Score(self):
        return self._RiskItem2Score

    @RiskItem2Score.setter
    def RiskItem2Score(self, RiskItem2Score):
        self._RiskItem2Score = RiskItem2Score

    @property
    def RiskItem3Score(self):
        return self._RiskItem3Score

    @RiskItem3Score.setter
    def RiskItem3Score(self, RiskItem3Score):
        self._RiskItem3Score = RiskItem3Score

    @property
    def RiskItem4Score(self):
        return self._RiskItem4Score

    @RiskItem4Score.setter
    def RiskItem4Score(self, RiskItem4Score):
        self._RiskItem4Score = RiskItem4Score

    @property
    def RiskItem5Score(self):
        return self._RiskItem5Score

    @RiskItem5Score.setter
    def RiskItem5Score(self, RiskItem5Score):
        self._RiskItem5Score = RiskItem5Score

    @property
    def RiskItem6Score(self):
        return self._RiskItem6Score

    @RiskItem6Score.setter
    def RiskItem6Score(self, RiskItem6Score):
        self._RiskItem6Score = RiskItem6Score

    @property
    def RiskItem7Score(self):
        return self._RiskItem7Score

    @RiskItem7Score.setter
    def RiskItem7Score(self, RiskItem7Score):
        self._RiskItem7Score = RiskItem7Score

    @property
    def RiskItem8Score(self):
        return self._RiskItem8Score

    @RiskItem8Score.setter
    def RiskItem8Score(self, RiskItem8Score):
        self._RiskItem8Score = RiskItem8Score


    def _deserialize(self, params):
        self._RiskItem1Score = params.get("RiskItem1Score")
        self._RiskItem2Score = params.get("RiskItem2Score")
        self._RiskItem3Score = params.get("RiskItem3Score")
        self._RiskItem4Score = params.get("RiskItem4Score")
        self._RiskItem5Score = params.get("RiskItem5Score")
        self._RiskItem6Score = params.get("RiskItem6Score")
        self._RiskItem7Score = params.get("RiskItem7Score")
        self._RiskItem8Score = params.get("RiskItem8Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlySecMiniAppTaskData(AbstractModel):
    """翼扬诊断小程序任务数据

    """

    def __init__(self):
        r"""
        :param _TaskID: 任务id
        :type TaskID: str
        :param _MiniAppID: 小程序appid
        :type MiniAppID: str
        :param _MiniAppName: 小程序名称
        :type MiniAppName: str
        :param _MiniAppVersion: 小程序版本
        :type MiniAppVersion: str
        :param _Mode: 诊断模式 1:基础诊断，2:深度诊断
        :type Mode: int
        :param _CreateTime: 诊断时间
        :type CreateTime: int
        :param _Status: 诊断状态, 0:排队中, 1:成功, 2:失败, 3:进行中
        :type Status: int
        :param _Error: 诊断失败错误码
        :type Error: int
        """
        self._TaskID = None
        self._MiniAppID = None
        self._MiniAppName = None
        self._MiniAppVersion = None
        self._Mode = None
        self._CreateTime = None
        self._Status = None
        self._Error = None

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def MiniAppID(self):
        return self._MiniAppID

    @MiniAppID.setter
    def MiniAppID(self, MiniAppID):
        self._MiniAppID = MiniAppID

    @property
    def MiniAppName(self):
        return self._MiniAppName

    @MiniAppName.setter
    def MiniAppName(self, MiniAppName):
        self._MiniAppName = MiniAppName

    @property
    def MiniAppVersion(self):
        return self._MiniAppVersion

    @MiniAppVersion.setter
    def MiniAppVersion(self, MiniAppVersion):
        self._MiniAppVersion = MiniAppVersion

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        self._MiniAppID = params.get("MiniAppID")
        self._MiniAppName = params.get("MiniAppName")
        self._MiniAppVersion = params.get("MiniAppVersion")
        self._Mode = params.get("Mode")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceUsageInfoData(AbstractModel):
    """翼扬安全资源使用情况

    """

    def __init__(self):
        r"""
        :param _ResourceName: 资源名称, 具体名称请查看产品配置
        :type ResourceName: str
        :param _Total: 资源总数
        :type Total: int
        :param _UnusedCount: 资源未使用次数
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
        