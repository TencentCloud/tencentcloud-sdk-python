# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class Abnormals(AbstractModel):
    r"""异常提醒

    """

    def __init__(self):
        r"""
        :param _Type: 类型
        :type Type: str
        :param _Title: 标题
        :type Title: str
        :param _AbnormalReason: 异常原因 PatientInfo 病人信息缺失；OrderInfo 医嘱信息缺失； PrescriptionError 处方异常提醒
        :type AbnormalReason: str
        """
        self._Type = None
        self._Title = None
        self._AbnormalReason = None

    @property
    def Type(self):
        r"""类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Title(self):
        r"""标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def AbnormalReason(self):
        r"""异常原因 PatientInfo 病人信息缺失；OrderInfo 医嘱信息缺失； PrescriptionError 处方异常提醒
        :rtype: str
        """
        return self._AbnormalReason

    @AbnormalReason.setter
    def AbnormalReason(self, AbnormalReason):
        self._AbnormalReason = AbnormalReason


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Title = params.get("Title")
        self._AbnormalReason = params.get("AbnormalReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonHeader(AbstractModel):
    r"""业务接口请求头

    """

    def __init__(self):
        r"""
        :param _HospitalId: 机构ID
        :type HospitalId: str
        :param _Token: token
        :type Token: str
        """
        self._HospitalId = None
        self._Token = None

    @property
    def HospitalId(self):
        r"""机构ID
        :rtype: str
        """
        return self._HospitalId

    @HospitalId.setter
    def HospitalId(self, HospitalId):
        self._HospitalId = HospitalId

    @property
    def Token(self):
        r"""token
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token


    def _deserialize(self, params):
        self._HospitalId = params.get("HospitalId")
        self._Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CriticalInfo(AbstractModel):
    r"""危疾重症

    """

    def __init__(self):
        r"""
        :param _Type: 危急重症类型 0:文字描述类 1:数值检查类
        :type Type: int
        :param _Tips: 提示
        :type Tips: str
        """
        self._Type = None
        self._Tips = None

    @property
    def Type(self):
        r"""危急重症类型 0:文字描述类 1:数值检查类
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Tips(self):
        r"""提示
        :rtype: str
        """
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Tips = params.get("Tips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CurrentDiagnosis(AbstractModel):
    r"""当前诊断

    """

    def __init__(self):
        r"""
        :param _DiagnoseDisease: 诊断疾病
        :type DiagnoseDisease: str
        :param _DiseaseGuideInfo: 疾病指南信息
        :type DiseaseGuideInfo: str
        :param _StandardName: 标准名称
        :type StandardName: str
        """
        self._DiagnoseDisease = None
        self._DiseaseGuideInfo = None
        self._StandardName = None

    @property
    def DiagnoseDisease(self):
        r"""诊断疾病
        :rtype: str
        """
        return self._DiagnoseDisease

    @DiagnoseDisease.setter
    def DiagnoseDisease(self, DiagnoseDisease):
        self._DiagnoseDisease = DiagnoseDisease

    @property
    def DiseaseGuideInfo(self):
        r"""疾病指南信息
        :rtype: str
        """
        return self._DiseaseGuideInfo

    @DiseaseGuideInfo.setter
    def DiseaseGuideInfo(self, DiseaseGuideInfo):
        self._DiseaseGuideInfo = DiseaseGuideInfo

    @property
    def StandardName(self):
        r"""标准名称
        :rtype: str
        """
        return self._StandardName

    @StandardName.setter
    def StandardName(self, StandardName):
        self._StandardName = StandardName


    def _deserialize(self, params):
        self._DiagnoseDisease = params.get("DiagnoseDisease")
        self._DiseaseGuideInfo = params.get("DiseaseGuideInfo")
        self._StandardName = params.get("StandardName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Department(AbstractModel):
    r"""科室信息

    """

    def __init__(self):
        r"""
        :param _Id: 科室ID
        :type Id: str
        :param _Name: 科室名称
        :type Name: str
        :param _Scope: 科室类型 0:门诊  1:住院  2:门诊+住院
        :type Scope: int
        :param _OutpatientOn: 门诊区开关 true:此科室对应的门诊区开启智能审方功能, false:此科室对应的门诊区关闭智能审方功能; 仅对scope为0/2的科室生效
        :type OutpatientOn: bool
        :param _InHospitalOn: 住院区开关 true:此科室对应的住院区开启智能审方功能, false:此科室对应的住院区关闭智能审方功能; 仅对scope为1/2的科室生效
        :type InHospitalOn: bool
        """
        self._Id = None
        self._Name = None
        self._Scope = None
        self._OutpatientOn = None
        self._InHospitalOn = None

    @property
    def Id(self):
        r"""科室ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""科室名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Scope(self):
        r"""科室类型 0:门诊  1:住院  2:门诊+住院
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def OutpatientOn(self):
        r"""门诊区开关 true:此科室对应的门诊区开启智能审方功能, false:此科室对应的门诊区关闭智能审方功能; 仅对scope为0/2的科室生效
        :rtype: bool
        """
        return self._OutpatientOn

    @OutpatientOn.setter
    def OutpatientOn(self, OutpatientOn):
        self._OutpatientOn = OutpatientOn

    @property
    def InHospitalOn(self):
        r"""住院区开关 true:此科室对应的住院区开启智能审方功能, false:此科室对应的住院区关闭智能审方功能; 仅对scope为1/2的科室生效
        :rtype: bool
        """
        return self._InHospitalOn

    @InHospitalOn.setter
    def InHospitalOn(self, InHospitalOn):
        self._InHospitalOn = InHospitalOn


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Scope = params.get("Scope")
        self._OutpatientOn = params.get("OutpatientOn")
        self._InHospitalOn = params.get("InHospitalOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagnosisInfo(AbstractModel):
    r"""诊断、辅助内容

    """

    def __init__(self):
        r"""
        :param _IntentType: 默认0，0:初诊-常规诊疗 1:复诊 2:检验检查/取药/咨询/疫苗 3:信息缺失 4:信息错误
        :type IntentType: int
        :param _RiskInfo: 诊断风险
        :type RiskInfo: str
        :param _SuspectedDiagnosis: 疑似诊断列表
        :type SuspectedDiagnosis: list of SuspectedDiagnosis
        :param _ReferralInfo: 转诊提醒
        :type ReferralInfo: :class:`tencentcloud.aca.v20210323.models.ReferralInfo`
        :param _CriticalInfo: 危急重症
        :type CriticalInfo: list of CriticalInfo
        :param _VitalSignsInfo: 生命体征风险
        :type VitalSignsInfo: :class:`tencentcloud.aca.v20210323.models.VitalSignsInfo`
        :param _DifferDiagnosis: 鉴别诊断
        :type DifferDiagnosis: list of DifferDiagnosis
        :param _RecordQuality: 病历质控
        :type RecordQuality: :class:`tencentcloud.aca.v20210323.models.RecordQuality`
        :param _CurrentDiagnosis: 当前诊断
        :type CurrentDiagnosis: list of CurrentDiagnosis
        :param _TreatmentGuide: 治疗方案
        :type TreatmentGuide: list of TreatmentGuide
        :param _EmrQuality: 病历质控
        :type EmrQuality: :class:`tencentcloud.aca.v20210323.models.EmrQuality`
        :param _HealthPrescriptions: 健康处方
        :type HealthPrescriptions: list of HealthPrescriptions
        """
        self._IntentType = None
        self._RiskInfo = None
        self._SuspectedDiagnosis = None
        self._ReferralInfo = None
        self._CriticalInfo = None
        self._VitalSignsInfo = None
        self._DifferDiagnosis = None
        self._RecordQuality = None
        self._CurrentDiagnosis = None
        self._TreatmentGuide = None
        self._EmrQuality = None
        self._HealthPrescriptions = None

    @property
    def IntentType(self):
        r"""默认0，0:初诊-常规诊疗 1:复诊 2:检验检查/取药/咨询/疫苗 3:信息缺失 4:信息错误
        :rtype: int
        """
        return self._IntentType

    @IntentType.setter
    def IntentType(self, IntentType):
        self._IntentType = IntentType

    @property
    def RiskInfo(self):
        r"""诊断风险
        :rtype: str
        """
        return self._RiskInfo

    @RiskInfo.setter
    def RiskInfo(self, RiskInfo):
        self._RiskInfo = RiskInfo

    @property
    def SuspectedDiagnosis(self):
        r"""疑似诊断列表
        :rtype: list of SuspectedDiagnosis
        """
        return self._SuspectedDiagnosis

    @SuspectedDiagnosis.setter
    def SuspectedDiagnosis(self, SuspectedDiagnosis):
        self._SuspectedDiagnosis = SuspectedDiagnosis

    @property
    def ReferralInfo(self):
        r"""转诊提醒
        :rtype: :class:`tencentcloud.aca.v20210323.models.ReferralInfo`
        """
        return self._ReferralInfo

    @ReferralInfo.setter
    def ReferralInfo(self, ReferralInfo):
        self._ReferralInfo = ReferralInfo

    @property
    def CriticalInfo(self):
        r"""危急重症
        :rtype: list of CriticalInfo
        """
        return self._CriticalInfo

    @CriticalInfo.setter
    def CriticalInfo(self, CriticalInfo):
        self._CriticalInfo = CriticalInfo

    @property
    def VitalSignsInfo(self):
        r"""生命体征风险
        :rtype: :class:`tencentcloud.aca.v20210323.models.VitalSignsInfo`
        """
        return self._VitalSignsInfo

    @VitalSignsInfo.setter
    def VitalSignsInfo(self, VitalSignsInfo):
        self._VitalSignsInfo = VitalSignsInfo

    @property
    def DifferDiagnosis(self):
        r"""鉴别诊断
        :rtype: list of DifferDiagnosis
        """
        return self._DifferDiagnosis

    @DifferDiagnosis.setter
    def DifferDiagnosis(self, DifferDiagnosis):
        self._DifferDiagnosis = DifferDiagnosis

    @property
    def RecordQuality(self):
        r"""病历质控
        :rtype: :class:`tencentcloud.aca.v20210323.models.RecordQuality`
        """
        return self._RecordQuality

    @RecordQuality.setter
    def RecordQuality(self, RecordQuality):
        self._RecordQuality = RecordQuality

    @property
    def CurrentDiagnosis(self):
        r"""当前诊断
        :rtype: list of CurrentDiagnosis
        """
        return self._CurrentDiagnosis

    @CurrentDiagnosis.setter
    def CurrentDiagnosis(self, CurrentDiagnosis):
        self._CurrentDiagnosis = CurrentDiagnosis

    @property
    def TreatmentGuide(self):
        r"""治疗方案
        :rtype: list of TreatmentGuide
        """
        return self._TreatmentGuide

    @TreatmentGuide.setter
    def TreatmentGuide(self, TreatmentGuide):
        self._TreatmentGuide = TreatmentGuide

    @property
    def EmrQuality(self):
        r"""病历质控
        :rtype: :class:`tencentcloud.aca.v20210323.models.EmrQuality`
        """
        return self._EmrQuality

    @EmrQuality.setter
    def EmrQuality(self, EmrQuality):
        self._EmrQuality = EmrQuality

    @property
    def HealthPrescriptions(self):
        r"""健康处方
        :rtype: list of HealthPrescriptions
        """
        return self._HealthPrescriptions

    @HealthPrescriptions.setter
    def HealthPrescriptions(self, HealthPrescriptions):
        self._HealthPrescriptions = HealthPrescriptions


    def _deserialize(self, params):
        self._IntentType = params.get("IntentType")
        self._RiskInfo = params.get("RiskInfo")
        if params.get("SuspectedDiagnosis") is not None:
            self._SuspectedDiagnosis = []
            for item in params.get("SuspectedDiagnosis"):
                obj = SuspectedDiagnosis()
                obj._deserialize(item)
                self._SuspectedDiagnosis.append(obj)
        if params.get("ReferralInfo") is not None:
            self._ReferralInfo = ReferralInfo()
            self._ReferralInfo._deserialize(params.get("ReferralInfo"))
        if params.get("CriticalInfo") is not None:
            self._CriticalInfo = []
            for item in params.get("CriticalInfo"):
                obj = CriticalInfo()
                obj._deserialize(item)
                self._CriticalInfo.append(obj)
        if params.get("VitalSignsInfo") is not None:
            self._VitalSignsInfo = VitalSignsInfo()
            self._VitalSignsInfo._deserialize(params.get("VitalSignsInfo"))
        if params.get("DifferDiagnosis") is not None:
            self._DifferDiagnosis = []
            for item in params.get("DifferDiagnosis"):
                obj = DifferDiagnosis()
                obj._deserialize(item)
                self._DifferDiagnosis.append(obj)
        if params.get("RecordQuality") is not None:
            self._RecordQuality = RecordQuality()
            self._RecordQuality._deserialize(params.get("RecordQuality"))
        if params.get("CurrentDiagnosis") is not None:
            self._CurrentDiagnosis = []
            for item in params.get("CurrentDiagnosis"):
                obj = CurrentDiagnosis()
                obj._deserialize(item)
                self._CurrentDiagnosis.append(obj)
        if params.get("TreatmentGuide") is not None:
            self._TreatmentGuide = []
            for item in params.get("TreatmentGuide"):
                obj = TreatmentGuide()
                obj._deserialize(item)
                self._TreatmentGuide.append(obj)
        if params.get("EmrQuality") is not None:
            self._EmrQuality = EmrQuality()
            self._EmrQuality._deserialize(params.get("EmrQuality"))
        if params.get("HealthPrescriptions") is not None:
            self._HealthPrescriptions = []
            for item in params.get("HealthPrescriptions"):
                obj = HealthPrescriptions()
                obj._deserialize(item)
                self._HealthPrescriptions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Dict(AbstractModel):
    r"""字典信息

    """

    def __init__(self):
        r"""
        :param _FreqCode: 给药频次编码
        :type FreqCode: str
        :param _FreqName: 给药频次名称
        :type FreqName: str
        :param _Disable: 是否禁用 0-启用 1-禁用
        :type Disable: int
        :param _UsageCode: 给药途径编码
        :type UsageCode: str
        :param _UsageName: 给药途径名称
        :type UsageName: str
        :param _DeptId: 科室ID
        :type DeptId: str
        :param _DeptName: 科室名称
        :type DeptName: str
        :param _Scope: 科室区域类型 0:门诊  1:住院  2:门诊+住院
        :type Scope: int
        :param _OutpatientOn: 门诊开关
        :type OutpatientOn: bool
        :param _InHospitalOn: 住院
        :type InHospitalOn: bool
        :param _DiagCode: 诊断编码
        :type DiagCode: str
        :param _DiagName: 诊断名称
        :type DiagName: str
        :param _IcdCode: ICD代码
        :type IcdCode: str
        """
        self._FreqCode = None
        self._FreqName = None
        self._Disable = None
        self._UsageCode = None
        self._UsageName = None
        self._DeptId = None
        self._DeptName = None
        self._Scope = None
        self._OutpatientOn = None
        self._InHospitalOn = None
        self._DiagCode = None
        self._DiagName = None
        self._IcdCode = None

    @property
    def FreqCode(self):
        r"""给药频次编码
        :rtype: str
        """
        return self._FreqCode

    @FreqCode.setter
    def FreqCode(self, FreqCode):
        self._FreqCode = FreqCode

    @property
    def FreqName(self):
        r"""给药频次名称
        :rtype: str
        """
        return self._FreqName

    @FreqName.setter
    def FreqName(self, FreqName):
        self._FreqName = FreqName

    @property
    def Disable(self):
        r"""是否禁用 0-启用 1-禁用
        :rtype: int
        """
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable

    @property
    def UsageCode(self):
        r"""给药途径编码
        :rtype: str
        """
        return self._UsageCode

    @UsageCode.setter
    def UsageCode(self, UsageCode):
        self._UsageCode = UsageCode

    @property
    def UsageName(self):
        r"""给药途径名称
        :rtype: str
        """
        return self._UsageName

    @UsageName.setter
    def UsageName(self, UsageName):
        self._UsageName = UsageName

    @property
    def DeptId(self):
        r"""科室ID
        :rtype: str
        """
        return self._DeptId

    @DeptId.setter
    def DeptId(self, DeptId):
        self._DeptId = DeptId

    @property
    def DeptName(self):
        r"""科室名称
        :rtype: str
        """
        return self._DeptName

    @DeptName.setter
    def DeptName(self, DeptName):
        self._DeptName = DeptName

    @property
    def Scope(self):
        r"""科室区域类型 0:门诊  1:住院  2:门诊+住院
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def OutpatientOn(self):
        r"""门诊开关
        :rtype: bool
        """
        return self._OutpatientOn

    @OutpatientOn.setter
    def OutpatientOn(self, OutpatientOn):
        self._OutpatientOn = OutpatientOn

    @property
    def InHospitalOn(self):
        r"""住院
        :rtype: bool
        """
        return self._InHospitalOn

    @InHospitalOn.setter
    def InHospitalOn(self, InHospitalOn):
        self._InHospitalOn = InHospitalOn

    @property
    def DiagCode(self):
        r"""诊断编码
        :rtype: str
        """
        return self._DiagCode

    @DiagCode.setter
    def DiagCode(self, DiagCode):
        self._DiagCode = DiagCode

    @property
    def DiagName(self):
        r"""诊断名称
        :rtype: str
        """
        return self._DiagName

    @DiagName.setter
    def DiagName(self, DiagName):
        self._DiagName = DiagName

    @property
    def IcdCode(self):
        r"""ICD代码
        :rtype: str
        """
        return self._IcdCode

    @IcdCode.setter
    def IcdCode(self, IcdCode):
        self._IcdCode = IcdCode


    def _deserialize(self, params):
        self._FreqCode = params.get("FreqCode")
        self._FreqName = params.get("FreqName")
        self._Disable = params.get("Disable")
        self._UsageCode = params.get("UsageCode")
        self._UsageName = params.get("UsageName")
        self._DeptId = params.get("DeptId")
        self._DeptName = params.get("DeptName")
        self._Scope = params.get("Scope")
        self._OutpatientOn = params.get("OutpatientOn")
        self._InHospitalOn = params.get("InHospitalOn")
        self._DiagCode = params.get("DiagCode")
        self._DiagName = params.get("DiagName")
        self._IcdCode = params.get("IcdCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DifferDiagnosis(AbstractModel):
    r"""鉴别诊断

    """

    def __init__(self):
        r"""
        :param _DifferName: 鉴别名称
        :type DifferName: str
        :param _DifferTips: 鉴别提示
        :type DifferTips: str
        :param _DiseaseGuideInfo: 疾病指南信息
        :type DiseaseGuideInfo: str
        """
        self._DifferName = None
        self._DifferTips = None
        self._DiseaseGuideInfo = None

    @property
    def DifferName(self):
        r"""鉴别名称
        :rtype: str
        """
        return self._DifferName

    @DifferName.setter
    def DifferName(self, DifferName):
        self._DifferName = DifferName

    @property
    def DifferTips(self):
        r"""鉴别提示
        :rtype: str
        """
        return self._DifferTips

    @DifferTips.setter
    def DifferTips(self, DifferTips):
        self._DifferTips = DifferTips

    @property
    def DiseaseGuideInfo(self):
        r"""疾病指南信息
        :rtype: str
        """
        return self._DiseaseGuideInfo

    @DiseaseGuideInfo.setter
    def DiseaseGuideInfo(self, DiseaseGuideInfo):
        self._DiseaseGuideInfo = DiseaseGuideInfo


    def _deserialize(self, params):
        self._DifferName = params.get("DifferName")
        self._DifferTips = params.get("DifferTips")
        self._DiseaseGuideInfo = params.get("DiseaseGuideInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DocInfo(AbstractModel):
    r"""药品文档信息

    """

    def __init__(self):
        r"""
        :param _DrugId: 药品ID
        :type DrugId: str
        :param _DrugName: 药品名称
        :type DrugName: str
        :param _DocUrl: 说明书地址
        :type DocUrl: str
        """
        self._DrugId = None
        self._DrugName = None
        self._DocUrl = None

    @property
    def DrugId(self):
        r"""药品ID
        :rtype: str
        """
        return self._DrugId

    @DrugId.setter
    def DrugId(self, DrugId):
        self._DrugId = DrugId

    @property
    def DrugName(self):
        r"""药品名称
        :rtype: str
        """
        return self._DrugName

    @DrugName.setter
    def DrugName(self, DrugName):
        self._DrugName = DrugName

    @property
    def DocUrl(self):
        r"""说明书地址
        :rtype: str
        """
        return self._DocUrl

    @DocUrl.setter
    def DocUrl(self, DocUrl):
        self._DocUrl = DocUrl


    def _deserialize(self, params):
        self._DrugId = params.get("DrugId")
        self._DrugName = params.get("DrugName")
        self._DocUrl = params.get("DocUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DoctorInfo(AbstractModel):
    r"""医生信息

    """

    def __init__(self):
        r"""
        :param _DoctorId: 医生ID
        :type DoctorId: str
        :param _DoctorName: 医生姓名
        :type DoctorName: str
        :param _DoctorPhone: 医生电话
        :type DoctorPhone: str
        """
        self._DoctorId = None
        self._DoctorName = None
        self._DoctorPhone = None

    @property
    def DoctorId(self):
        r"""医生ID
        :rtype: str
        """
        return self._DoctorId

    @DoctorId.setter
    def DoctorId(self, DoctorId):
        self._DoctorId = DoctorId

    @property
    def DoctorName(self):
        r"""医生姓名
        :rtype: str
        """
        return self._DoctorName

    @DoctorName.setter
    def DoctorName(self, DoctorName):
        self._DoctorName = DoctorName

    @property
    def DoctorPhone(self):
        r"""医生电话
        :rtype: str
        """
        return self._DoctorPhone

    @DoctorPhone.setter
    def DoctorPhone(self, DoctorPhone):
        self._DoctorPhone = DoctorPhone


    def _deserialize(self, params):
        self._DoctorId = params.get("DoctorId")
        self._DoctorName = params.get("DoctorName")
        self._DoctorPhone = params.get("DoctorPhone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Drug(AbstractModel):
    r"""药品信息

    """

    def __init__(self):
        r"""
        :param _DrugOrgId: 医院药品id
        :type DrugOrgId: str
        :param _DrugName: 医院药品通用名
        :type DrugName: str
        :param _DrugCommodityName: 医院药品商品名
        :type DrugCommodityName: str
        :param _Specifications: 医院药品规格
        :type Specifications: str
        :param _ApprovalNumber: 医院药品批准文号
        :type ApprovalNumber: str
        :param _Manufacturer: 生产厂商
        :type Manufacturer: str
        :param _DosageForm: 剂型
        :type DosageForm: str
        :param _Unuse: 使用状态 0:启用 1:停用
        :type Unuse: int
        :param _DosageFormCode: 剂型编码
        :type DosageFormCode: str
        :param _DefinedDailyDose: 抗菌药DDD值
        :type DefinedDailyDose: str
        :param _Amount: 药品单价
        :type Amount: str
        :param _YbCode: 国家医保编码
        :type YbCode: str
        :param _DrugBasicCode: 药品本位码
        :type DrugBasicCode: str
        :param _PropertyInfo: 药品属性
        :type PropertyInfo: :class:`tencentcloud.aca.v20210323.models.DurgPropertyInfo`
        """
        self._DrugOrgId = None
        self._DrugName = None
        self._DrugCommodityName = None
        self._Specifications = None
        self._ApprovalNumber = None
        self._Manufacturer = None
        self._DosageForm = None
        self._Unuse = None
        self._DosageFormCode = None
        self._DefinedDailyDose = None
        self._Amount = None
        self._YbCode = None
        self._DrugBasicCode = None
        self._PropertyInfo = None

    @property
    def DrugOrgId(self):
        r"""医院药品id
        :rtype: str
        """
        return self._DrugOrgId

    @DrugOrgId.setter
    def DrugOrgId(self, DrugOrgId):
        self._DrugOrgId = DrugOrgId

    @property
    def DrugName(self):
        r"""医院药品通用名
        :rtype: str
        """
        return self._DrugName

    @DrugName.setter
    def DrugName(self, DrugName):
        self._DrugName = DrugName

    @property
    def DrugCommodityName(self):
        r"""医院药品商品名
        :rtype: str
        """
        return self._DrugCommodityName

    @DrugCommodityName.setter
    def DrugCommodityName(self, DrugCommodityName):
        self._DrugCommodityName = DrugCommodityName

    @property
    def Specifications(self):
        r"""医院药品规格
        :rtype: str
        """
        return self._Specifications

    @Specifications.setter
    def Specifications(self, Specifications):
        self._Specifications = Specifications

    @property
    def ApprovalNumber(self):
        r"""医院药品批准文号
        :rtype: str
        """
        return self._ApprovalNumber

    @ApprovalNumber.setter
    def ApprovalNumber(self, ApprovalNumber):
        self._ApprovalNumber = ApprovalNumber

    @property
    def Manufacturer(self):
        r"""生产厂商
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def DosageForm(self):
        r"""剂型
        :rtype: str
        """
        return self._DosageForm

    @DosageForm.setter
    def DosageForm(self, DosageForm):
        self._DosageForm = DosageForm

    @property
    def Unuse(self):
        r"""使用状态 0:启用 1:停用
        :rtype: int
        """
        return self._Unuse

    @Unuse.setter
    def Unuse(self, Unuse):
        self._Unuse = Unuse

    @property
    def DosageFormCode(self):
        r"""剂型编码
        :rtype: str
        """
        return self._DosageFormCode

    @DosageFormCode.setter
    def DosageFormCode(self, DosageFormCode):
        self._DosageFormCode = DosageFormCode

    @property
    def DefinedDailyDose(self):
        r"""抗菌药DDD值
        :rtype: str
        """
        return self._DefinedDailyDose

    @DefinedDailyDose.setter
    def DefinedDailyDose(self, DefinedDailyDose):
        self._DefinedDailyDose = DefinedDailyDose

    @property
    def Amount(self):
        r"""药品单价
        :rtype: str
        """
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def YbCode(self):
        r"""国家医保编码
        :rtype: str
        """
        return self._YbCode

    @YbCode.setter
    def YbCode(self, YbCode):
        self._YbCode = YbCode

    @property
    def DrugBasicCode(self):
        r"""药品本位码
        :rtype: str
        """
        return self._DrugBasicCode

    @DrugBasicCode.setter
    def DrugBasicCode(self, DrugBasicCode):
        self._DrugBasicCode = DrugBasicCode

    @property
    def PropertyInfo(self):
        r"""药品属性
        :rtype: :class:`tencentcloud.aca.v20210323.models.DurgPropertyInfo`
        """
        return self._PropertyInfo

    @PropertyInfo.setter
    def PropertyInfo(self, PropertyInfo):
        self._PropertyInfo = PropertyInfo


    def _deserialize(self, params):
        self._DrugOrgId = params.get("DrugOrgId")
        self._DrugName = params.get("DrugName")
        self._DrugCommodityName = params.get("DrugCommodityName")
        self._Specifications = params.get("Specifications")
        self._ApprovalNumber = params.get("ApprovalNumber")
        self._Manufacturer = params.get("Manufacturer")
        self._DosageForm = params.get("DosageForm")
        self._Unuse = params.get("Unuse")
        self._DosageFormCode = params.get("DosageFormCode")
        self._DefinedDailyDose = params.get("DefinedDailyDose")
        self._Amount = params.get("Amount")
        self._YbCode = params.get("YbCode")
        self._DrugBasicCode = params.get("DrugBasicCode")
        if params.get("PropertyInfo") is not None:
            self._PropertyInfo = DurgPropertyInfo()
            self._PropertyInfo._deserialize(params.get("PropertyInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrugList(AbstractModel):
    r"""药品列表

    """

    def __init__(self):
        r"""
        :param _DrugId: 药品ID
        :type DrugId: str
        :param _DrugName: 药品名称
        :type DrugName: str
        :param _DocUrl: 文档地址
        :type DocUrl: str
        :param _NotFound: 是否找到
        :type NotFound: bool
        """
        self._DrugId = None
        self._DrugName = None
        self._DocUrl = None
        self._NotFound = None

    @property
    def DrugId(self):
        r"""药品ID
        :rtype: str
        """
        return self._DrugId

    @DrugId.setter
    def DrugId(self, DrugId):
        self._DrugId = DrugId

    @property
    def DrugName(self):
        r"""药品名称
        :rtype: str
        """
        return self._DrugName

    @DrugName.setter
    def DrugName(self, DrugName):
        self._DrugName = DrugName

    @property
    def DocUrl(self):
        r"""文档地址
        :rtype: str
        """
        return self._DocUrl

    @DocUrl.setter
    def DocUrl(self, DocUrl):
        self._DocUrl = DocUrl

    @property
    def NotFound(self):
        r"""是否找到
        :rtype: bool
        """
        return self._NotFound

    @NotFound.setter
    def NotFound(self, NotFound):
        self._NotFound = NotFound


    def _deserialize(self, params):
        self._DrugId = params.get("DrugId")
        self._DrugName = params.get("DrugName")
        self._DocUrl = params.get("DocUrl")
        self._NotFound = params.get("NotFound")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrugUsage(AbstractModel):
    r"""处方药品信息

    """

    def __init__(self):
        r"""
        :param _DrugId: 药品ID
        :type DrugId: str
        :param _DrugName: 药品名称
        :type DrugName: str
        :param _TimePerDay: 日服药频次
        :type TimePerDay: str
        :param _Usage: 给药途径
        :type Usage: str
        :param _PrescriptionId: 处方ID，药品不同分组是传不同的处方ID
        :type PrescriptionId: str
        :param _DosagePerTime: 每次剂量
        :type DosagePerTime: str
        :param _DosagePerTimeUnit: 每次剂量单位
        :type DosagePerTimeUnit: str
        :param _Time: 单次服药时间
        :type Time: str
        :param _Cycle: 给药周期
        :type Cycle: str
        :param _DosagePerDay: 单日剂量
        :type DosagePerDay: str
        :param _Course: 疗程
        :type Course: str
        :param _Speed: 给药速度
        :type Speed: str
        :param _BeginTime: 处方生效时间戳，住院医嘱必须传(caseType =1)
        :type BeginTime: int
        :param _EndTime: 处方失效时间戳，住院医嘱必须传(caseType =1)
        :type EndTime: int
        :param _Package: 开具数量
        :type Package: str
        :param _PackageUnit: 开具数量单位
        :type PackageUnit: str
        :param _GroupInj: 相同标志液体间进行配伍禁忌审核，不同标志间液体不进行配伍禁忌审核
        :type GroupInj: str
        :param _PrescriptionCharge: 处方金额
        :type PrescriptionCharge: str
        :param _MedicationDays: 用药天数
        :type MedicationDays: str
        """
        self._DrugId = None
        self._DrugName = None
        self._TimePerDay = None
        self._Usage = None
        self._PrescriptionId = None
        self._DosagePerTime = None
        self._DosagePerTimeUnit = None
        self._Time = None
        self._Cycle = None
        self._DosagePerDay = None
        self._Course = None
        self._Speed = None
        self._BeginTime = None
        self._EndTime = None
        self._Package = None
        self._PackageUnit = None
        self._GroupInj = None
        self._PrescriptionCharge = None
        self._MedicationDays = None

    @property
    def DrugId(self):
        r"""药品ID
        :rtype: str
        """
        return self._DrugId

    @DrugId.setter
    def DrugId(self, DrugId):
        self._DrugId = DrugId

    @property
    def DrugName(self):
        r"""药品名称
        :rtype: str
        """
        return self._DrugName

    @DrugName.setter
    def DrugName(self, DrugName):
        self._DrugName = DrugName

    @property
    def TimePerDay(self):
        r"""日服药频次
        :rtype: str
        """
        return self._TimePerDay

    @TimePerDay.setter
    def TimePerDay(self, TimePerDay):
        self._TimePerDay = TimePerDay

    @property
    def Usage(self):
        r"""给药途径
        :rtype: str
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def PrescriptionId(self):
        r"""处方ID，药品不同分组是传不同的处方ID
        :rtype: str
        """
        return self._PrescriptionId

    @PrescriptionId.setter
    def PrescriptionId(self, PrescriptionId):
        self._PrescriptionId = PrescriptionId

    @property
    def DosagePerTime(self):
        r"""每次剂量
        :rtype: str
        """
        return self._DosagePerTime

    @DosagePerTime.setter
    def DosagePerTime(self, DosagePerTime):
        self._DosagePerTime = DosagePerTime

    @property
    def DosagePerTimeUnit(self):
        r"""每次剂量单位
        :rtype: str
        """
        return self._DosagePerTimeUnit

    @DosagePerTimeUnit.setter
    def DosagePerTimeUnit(self, DosagePerTimeUnit):
        self._DosagePerTimeUnit = DosagePerTimeUnit

    @property
    def Time(self):
        r"""单次服药时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Cycle(self):
        r"""给药周期
        :rtype: str
        """
        return self._Cycle

    @Cycle.setter
    def Cycle(self, Cycle):
        self._Cycle = Cycle

    @property
    def DosagePerDay(self):
        r"""单日剂量
        :rtype: str
        """
        return self._DosagePerDay

    @DosagePerDay.setter
    def DosagePerDay(self, DosagePerDay):
        self._DosagePerDay = DosagePerDay

    @property
    def Course(self):
        r"""疗程
        :rtype: str
        """
        return self._Course

    @Course.setter
    def Course(self, Course):
        self._Course = Course

    @property
    def Speed(self):
        r"""给药速度
        :rtype: str
        """
        return self._Speed

    @Speed.setter
    def Speed(self, Speed):
        self._Speed = Speed

    @property
    def BeginTime(self):
        r"""处方生效时间戳，住院医嘱必须传(caseType =1)
        :rtype: int
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""处方失效时间戳，住院医嘱必须传(caseType =1)
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Package(self):
        r"""开具数量
        :rtype: str
        """
        return self._Package

    @Package.setter
    def Package(self, Package):
        self._Package = Package

    @property
    def PackageUnit(self):
        r"""开具数量单位
        :rtype: str
        """
        return self._PackageUnit

    @PackageUnit.setter
    def PackageUnit(self, PackageUnit):
        self._PackageUnit = PackageUnit

    @property
    def GroupInj(self):
        r"""相同标志液体间进行配伍禁忌审核，不同标志间液体不进行配伍禁忌审核
        :rtype: str
        """
        return self._GroupInj

    @GroupInj.setter
    def GroupInj(self, GroupInj):
        self._GroupInj = GroupInj

    @property
    def PrescriptionCharge(self):
        r"""处方金额
        :rtype: str
        """
        return self._PrescriptionCharge

    @PrescriptionCharge.setter
    def PrescriptionCharge(self, PrescriptionCharge):
        self._PrescriptionCharge = PrescriptionCharge

    @property
    def MedicationDays(self):
        r"""用药天数
        :rtype: str
        """
        return self._MedicationDays

    @MedicationDays.setter
    def MedicationDays(self, MedicationDays):
        self._MedicationDays = MedicationDays


    def _deserialize(self, params):
        self._DrugId = params.get("DrugId")
        self._DrugName = params.get("DrugName")
        self._TimePerDay = params.get("TimePerDay")
        self._Usage = params.get("Usage")
        self._PrescriptionId = params.get("PrescriptionId")
        self._DosagePerTime = params.get("DosagePerTime")
        self._DosagePerTimeUnit = params.get("DosagePerTimeUnit")
        self._Time = params.get("Time")
        self._Cycle = params.get("Cycle")
        self._DosagePerDay = params.get("DosagePerDay")
        self._Course = params.get("Course")
        self._Speed = params.get("Speed")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Package = params.get("Package")
        self._PackageUnit = params.get("PackageUnit")
        self._GroupInj = params.get("GroupInj")
        self._PrescriptionCharge = params.get("PrescriptionCharge")
        self._MedicationDays = params.get("MedicationDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DurgPropertyInfo(AbstractModel):
    r"""药品属性

    """

    def __init__(self):
        r"""
        :param _DrugType: 药品类型 1:西药,2:中成药,3:中药,4:化学药品,5:生物制药
        :type DrugType: int
        :param _AntibacterialType: 抗菌药分类 1:抗真菌药物, 2:抗细菌药物, 3:抗结核药物, 4:其他抗菌药, 0:普通药品
        :type AntibacterialType: int
        :param _AntibacterialClass: 抗菌药级别 1:非限制级, 2:限制级, 3:特殊使用级 
        :type AntibacterialClass: int
        :param _SpeciallyDrugType: 特殊药品类型 1:毒性药品, 2:麻醉药品, 3:放射药品, 4:精神一类药品, 5:精神二类药品, 6:其他特管药品， 7:贵重药品
        :type SpeciallyDrugType: int
        :param _IsBasicDrug: 是否为基本药物 1:是, 2:否, 0:未知
        :type IsBasicDrug: int
        :param _ChargeType: 社保药品 1:甲类药品, 2:乙类药品, 3:双跨药品, 4:自费药品, 0:未知
        :type ChargeType: int
        """
        self._DrugType = None
        self._AntibacterialType = None
        self._AntibacterialClass = None
        self._SpeciallyDrugType = None
        self._IsBasicDrug = None
        self._ChargeType = None

    @property
    def DrugType(self):
        r"""药品类型 1:西药,2:中成药,3:中药,4:化学药品,5:生物制药
        :rtype: int
        """
        return self._DrugType

    @DrugType.setter
    def DrugType(self, DrugType):
        self._DrugType = DrugType

    @property
    def AntibacterialType(self):
        r"""抗菌药分类 1:抗真菌药物, 2:抗细菌药物, 3:抗结核药物, 4:其他抗菌药, 0:普通药品
        :rtype: int
        """
        return self._AntibacterialType

    @AntibacterialType.setter
    def AntibacterialType(self, AntibacterialType):
        self._AntibacterialType = AntibacterialType

    @property
    def AntibacterialClass(self):
        r"""抗菌药级别 1:非限制级, 2:限制级, 3:特殊使用级 
        :rtype: int
        """
        return self._AntibacterialClass

    @AntibacterialClass.setter
    def AntibacterialClass(self, AntibacterialClass):
        self._AntibacterialClass = AntibacterialClass

    @property
    def SpeciallyDrugType(self):
        r"""特殊药品类型 1:毒性药品, 2:麻醉药品, 3:放射药品, 4:精神一类药品, 5:精神二类药品, 6:其他特管药品， 7:贵重药品
        :rtype: int
        """
        return self._SpeciallyDrugType

    @SpeciallyDrugType.setter
    def SpeciallyDrugType(self, SpeciallyDrugType):
        self._SpeciallyDrugType = SpeciallyDrugType

    @property
    def IsBasicDrug(self):
        r"""是否为基本药物 1:是, 2:否, 0:未知
        :rtype: int
        """
        return self._IsBasicDrug

    @IsBasicDrug.setter
    def IsBasicDrug(self, IsBasicDrug):
        self._IsBasicDrug = IsBasicDrug

    @property
    def ChargeType(self):
        r"""社保药品 1:甲类药品, 2:乙类药品, 3:双跨药品, 4:自费药品, 0:未知
        :rtype: int
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType


    def _deserialize(self, params):
        self._DrugType = params.get("DrugType")
        self._AntibacterialType = params.get("AntibacterialType")
        self._AntibacterialClass = params.get("AntibacterialClass")
        self._SpeciallyDrugType = params.get("SpeciallyDrugType")
        self._IsBasicDrug = params.get("IsBasicDrug")
        self._ChargeType = params.get("ChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmrDiagnosises(AbstractModel):
    r"""诊断列表

    """

    def __init__(self):
        r"""
        :param _DiagnosisName: 诊断名称
        :type DiagnosisName: str
        :param _IcdCode: ICD代码
        :type IcdCode: str
        """
        self._DiagnosisName = None
        self._IcdCode = None

    @property
    def DiagnosisName(self):
        r"""诊断名称
        :rtype: str
        """
        return self._DiagnosisName

    @DiagnosisName.setter
    def DiagnosisName(self, DiagnosisName):
        self._DiagnosisName = DiagnosisName

    @property
    def IcdCode(self):
        r"""ICD代码
        :rtype: str
        """
        return self._IcdCode

    @IcdCode.setter
    def IcdCode(self, IcdCode):
        self._IcdCode = IcdCode


    def _deserialize(self, params):
        self._DiagnosisName = params.get("DiagnosisName")
        self._IcdCode = params.get("IcdCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmrQuality(AbstractModel):
    r"""病历质控

    """

    def __init__(self):
        r"""
        :param _MissPhysicalExamination: 缺失体格检查项目
        :type MissPhysicalExamination: list of str
        """
        self._MissPhysicalExamination = None

    @property
    def MissPhysicalExamination(self):
        r"""缺失体格检查项目
        :rtype: list of str
        """
        return self._MissPhysicalExamination

    @MissPhysicalExamination.setter
    def MissPhysicalExamination(self, MissPhysicalExamination):
        self._MissPhysicalExamination = MissPhysicalExamination


    def _deserialize(self, params):
        self._MissPhysicalExamination = params.get("MissPhysicalExamination")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDrugIndicationsReqData(AbstractModel):
    r"""获取适应症请求

    """

    def __init__(self):
        r"""
        :param _Drugs: 查询药品列表
        :type Drugs: list of IndicationsDrug
        """
        self._Drugs = None

    @property
    def Drugs(self):
        r"""查询药品列表
        :rtype: list of IndicationsDrug
        """
        return self._Drugs

    @Drugs.setter
    def Drugs(self, Drugs):
        self._Drugs = Drugs


    def _deserialize(self, params):
        if params.get("Drugs") is not None:
            self._Drugs = []
            for item in params.get("Drugs"):
                obj = IndicationsDrug()
                obj._deserialize(item)
                self._Drugs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDrugIndicationsRequest(AbstractModel):
    r"""GetDrugIndications请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Header: 请求头
        :type Header: :class:`tencentcloud.aca.v20210323.models.CommonHeader`
        :param _Data: 获取适应症请求
        :type Data: :class:`tencentcloud.aca.v20210323.models.GetDrugIndicationsReqData`
        """
        self._Header = None
        self._Data = None

    @property
    def Header(self):
        r"""请求头
        :rtype: :class:`tencentcloud.aca.v20210323.models.CommonHeader`
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def Data(self):
        r"""获取适应症请求
        :rtype: :class:`tencentcloud.aca.v20210323.models.GetDrugIndicationsReqData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Header") is not None:
            self._Header = CommonHeader()
            self._Header._deserialize(params.get("Header"))
        if params.get("Data") is not None:
            self._Data = GetDrugIndicationsReqData()
            self._Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDrugIndicationsResp(AbstractModel):
    r"""药品适应症响应

    """

    def __init__(self):
        r"""
        :param _Indications: 适应症
        :type Indications: list of str
        :param _DocInfos: 药品说明
        :type DocInfos: list of DocInfo
        """
        self._Indications = None
        self._DocInfos = None

    @property
    def Indications(self):
        r"""适应症
        :rtype: list of str
        """
        return self._Indications

    @Indications.setter
    def Indications(self, Indications):
        self._Indications = Indications

    @property
    def DocInfos(self):
        r"""药品说明
        :rtype: list of DocInfo
        """
        return self._DocInfos

    @DocInfos.setter
    def DocInfos(self, DocInfos):
        self._DocInfos = DocInfos


    def _deserialize(self, params):
        self._Indications = params.get("Indications")
        if params.get("DocInfos") is not None:
            self._DocInfos = []
            for item in params.get("DocInfos"):
                obj = DocInfo()
                obj._deserialize(item)
                self._DocInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDrugIndicationsResponse(AbstractModel):
    r"""GetDrugIndications返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: 错误码
        :type Code: int
        :param _Message: 错误信息
        :type Message: str
        :param _Data: 适应症响应
        :type Data: :class:`tencentcloud.aca.v20210323.models.GetDrugIndicationsResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Code = None
        self._Message = None
        self._Data = None
        self._RequestId = None

    @property
    def Code(self):
        r"""错误码
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""错误信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Data(self):
        r"""适应症响应
        :rtype: :class:`tencentcloud.aca.v20210323.models.GetDrugIndicationsResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Data") is not None:
            self._Data = GetDrugIndicationsResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class HealthPrescriptions(AbstractModel):
    r"""健康处方

    """

    def __init__(self):
        r"""
        :param _Title: 标题
        :type Title: str
        :param _Url: 健康处方链接
        :type Url: str
        :param _KeyInformation: 关键信息
        :type KeyInformation: str
        """
        self._Title = None
        self._Url = None
        self._KeyInformation = None

    @property
    def Title(self):
        r"""标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Url(self):
        r"""健康处方链接
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def KeyInformation(self):
        r"""关键信息
        :rtype: str
        """
        return self._KeyInformation

    @KeyInformation.setter
    def KeyInformation(self, KeyInformation):
        self._KeyInformation = KeyInformation


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Url = params.get("Url")
        self._KeyInformation = params.get("KeyInformation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndicationsDrug(AbstractModel):
    r"""适应症药品请求

    """

    def __init__(self):
        r"""
        :param _DrugName: 药品名称
        :type DrugName: str
        :param _Specifications: 规格
        :type Specifications: str
        :param _ApprovalNumber: 批准文号
        :type ApprovalNumber: str
        :param _Manufacturer: 生产厂家
        :type Manufacturer: str
        :param _DrugId: 药品ID
        :type DrugId: str
        :param _TradeName: 商品名
        :type TradeName: str
        :param _Type: 类型 默认0 0-西药 2-中药
        :type Type: int
        """
        self._DrugName = None
        self._Specifications = None
        self._ApprovalNumber = None
        self._Manufacturer = None
        self._DrugId = None
        self._TradeName = None
        self._Type = None

    @property
    def DrugName(self):
        r"""药品名称
        :rtype: str
        """
        return self._DrugName

    @DrugName.setter
    def DrugName(self, DrugName):
        self._DrugName = DrugName

    @property
    def Specifications(self):
        r"""规格
        :rtype: str
        """
        return self._Specifications

    @Specifications.setter
    def Specifications(self, Specifications):
        self._Specifications = Specifications

    @property
    def ApprovalNumber(self):
        r"""批准文号
        :rtype: str
        """
        return self._ApprovalNumber

    @ApprovalNumber.setter
    def ApprovalNumber(self, ApprovalNumber):
        self._ApprovalNumber = ApprovalNumber

    @property
    def Manufacturer(self):
        r"""生产厂家
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def DrugId(self):
        r"""药品ID
        :rtype: str
        """
        return self._DrugId

    @DrugId.setter
    def DrugId(self, DrugId):
        self._DrugId = DrugId

    @property
    def TradeName(self):
        r"""商品名
        :rtype: str
        """
        return self._TradeName

    @TradeName.setter
    def TradeName(self, TradeName):
        self._TradeName = TradeName

    @property
    def Type(self):
        r"""类型 默认0 0-西药 2-中药
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._DrugName = params.get("DrugName")
        self._Specifications = params.get("Specifications")
        self._ApprovalNumber = params.get("ApprovalNumber")
        self._Manufacturer = params.get("Manufacturer")
        self._DrugId = params.get("DrugId")
        self._TradeName = params.get("TradeName")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginData(AbstractModel):
    r"""登录请求对象

    """

    def __init__(self):
        r"""
        :param _DoctorId: 医生ID
        :type DoctorId: str
        :param _DoctorName: 医生名称
        :type DoctorName: str
        :param _DoctorLevel: 医生职级 主治医师、副主任医师、主任医师
        :type DoctorLevel: str
        :param _DoctorDepartment: 医生科室 当前登录科室
        :type DoctorDepartment: str
        :param _DepartmentId: 科室ID
        :type DepartmentId: str
        """
        self._DoctorId = None
        self._DoctorName = None
        self._DoctorLevel = None
        self._DoctorDepartment = None
        self._DepartmentId = None

    @property
    def DoctorId(self):
        r"""医生ID
        :rtype: str
        """
        return self._DoctorId

    @DoctorId.setter
    def DoctorId(self, DoctorId):
        self._DoctorId = DoctorId

    @property
    def DoctorName(self):
        r"""医生名称
        :rtype: str
        """
        return self._DoctorName

    @DoctorName.setter
    def DoctorName(self, DoctorName):
        self._DoctorName = DoctorName

    @property
    def DoctorLevel(self):
        r"""医生职级 主治医师、副主任医师、主任医师
        :rtype: str
        """
        return self._DoctorLevel

    @DoctorLevel.setter
    def DoctorLevel(self, DoctorLevel):
        self._DoctorLevel = DoctorLevel

    @property
    def DoctorDepartment(self):
        r"""医生科室 当前登录科室
        :rtype: str
        """
        return self._DoctorDepartment

    @DoctorDepartment.setter
    def DoctorDepartment(self, DoctorDepartment):
        self._DoctorDepartment = DoctorDepartment

    @property
    def DepartmentId(self):
        r"""科室ID
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId


    def _deserialize(self, params):
        self._DoctorId = params.get("DoctorId")
        self._DoctorName = params.get("DoctorName")
        self._DoctorLevel = params.get("DoctorLevel")
        self._DoctorDepartment = params.get("DoctorDepartment")
        self._DepartmentId = params.get("DepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginDataResp(AbstractModel):
    r"""登录返回数据

    """

    def __init__(self):
        r"""
        :param _Token: token
        :type Token: str
        :param _ExpiresIn: 过期时间
        :type ExpiresIn: int
        :param _Timestamp: 服务端时间戳，时间戳校验失败时返回
        :type Timestamp: int
        """
        self._Token = None
        self._ExpiresIn = None
        self._Timestamp = None

    @property
    def Token(self):
        r"""token
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def ExpiresIn(self):
        r"""过期时间
        :rtype: int
        """
        return self._ExpiresIn

    @ExpiresIn.setter
    def ExpiresIn(self, ExpiresIn):
        self._ExpiresIn = ExpiresIn

    @property
    def Timestamp(self):
        r"""服务端时间戳，时间戳校验失败时返回
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._ExpiresIn = params.get("ExpiresIn")
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginHeader(AbstractModel):
    r"""登录接口请求头

    """

    def __init__(self):
        r"""
        :param _HospitalId: 机构ID
        :type HospitalId: str
        :param _PartnerId: 合作方ID
        :type PartnerId: str
        :param _Timestamp: 加密时间戳毫秒
        :type Timestamp: int
        :param _Signature: 签名数据
        :type Signature: str
        :param _PlatformId: 平台ID，平台版登录时传入
        :type PlatformId: str
        """
        self._HospitalId = None
        self._PartnerId = None
        self._Timestamp = None
        self._Signature = None
        self._PlatformId = None

    @property
    def HospitalId(self):
        r"""机构ID
        :rtype: str
        """
        return self._HospitalId

    @HospitalId.setter
    def HospitalId(self, HospitalId):
        self._HospitalId = HospitalId

    @property
    def PartnerId(self):
        r"""合作方ID
        :rtype: str
        """
        return self._PartnerId

    @PartnerId.setter
    def PartnerId(self, PartnerId):
        self._PartnerId = PartnerId

    @property
    def Timestamp(self):
        r"""加密时间戳毫秒
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Signature(self):
        r"""签名数据
        :rtype: str
        """
        return self._Signature

    @Signature.setter
    def Signature(self, Signature):
        self._Signature = Signature

    @property
    def PlatformId(self):
        r"""平台ID，平台版登录时传入
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._HospitalId = params.get("HospitalId")
        self._PartnerId = params.get("PartnerId")
        self._Timestamp = params.get("Timestamp")
        self._Signature = params.get("Signature")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginHisToolRequest(AbstractModel):
    r"""LoginHisTool请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Header: 请求头
        :type Header: :class:`tencentcloud.aca.v20210323.models.LoginHeader`
        :param _Data: 请求体
        :type Data: :class:`tencentcloud.aca.v20210323.models.LoginData`
        """
        self._Header = None
        self._Data = None

    @property
    def Header(self):
        r"""请求头
        :rtype: :class:`tencentcloud.aca.v20210323.models.LoginHeader`
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def Data(self):
        r"""请求体
        :rtype: :class:`tencentcloud.aca.v20210323.models.LoginData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Header") is not None:
            self._Header = LoginHeader()
            self._Header._deserialize(params.get("Header"))
        if params.get("Data") is not None:
            self._Data = LoginData()
            self._Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginHisToolResponse(AbstractModel):
    r"""LoginHisTool返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: 错误码
        :type Code: int
        :param _Message: 错误信息
        :type Message: str
        :param _Data: 登录返回token信息
        :type Data: :class:`tencentcloud.aca.v20210323.models.LoginDataResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Code = None
        self._Message = None
        self._Data = None
        self._RequestId = None

    @property
    def Code(self):
        r"""错误码
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""错误信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Data(self):
        r"""登录返回token信息
        :rtype: :class:`tencentcloud.aca.v20210323.models.LoginDataResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Data") is not None:
            self._Data = LoginDataResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class LoginOutData(AbstractModel):
    r"""登出

    """

    def __init__(self):
        r"""
        :param _Token: 登录获取的token
        :type Token: str
        """
        self._Token = None

    @property
    def Token(self):
        r"""登录获取的token
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token


    def _deserialize(self, params):
        self._Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginOutHeader(AbstractModel):
    r"""登出header对象

    """

    def __init__(self):
        r"""
        :param _PartnerId: 合作方ID
        :type PartnerId: str
        :param _Timestamp: 时间戳毫秒数
        :type Timestamp: int
        :param _Signature: 签名值
        :type Signature: str
        :param _HospitalId: 医院ID 单院版传这个
        :type HospitalId: str
        :param _PlatformId: 平台ID 平台版传这个
        :type PlatformId: str
        """
        self._PartnerId = None
        self._Timestamp = None
        self._Signature = None
        self._HospitalId = None
        self._PlatformId = None

    @property
    def PartnerId(self):
        r"""合作方ID
        :rtype: str
        """
        return self._PartnerId

    @PartnerId.setter
    def PartnerId(self, PartnerId):
        self._PartnerId = PartnerId

    @property
    def Timestamp(self):
        r"""时间戳毫秒数
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Signature(self):
        r"""签名值
        :rtype: str
        """
        return self._Signature

    @Signature.setter
    def Signature(self, Signature):
        self._Signature = Signature

    @property
    def HospitalId(self):
        r"""医院ID 单院版传这个
        :rtype: str
        """
        return self._HospitalId

    @HospitalId.setter
    def HospitalId(self, HospitalId):
        self._HospitalId = HospitalId

    @property
    def PlatformId(self):
        r"""平台ID 平台版传这个
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._PartnerId = params.get("PartnerId")
        self._Timestamp = params.get("Timestamp")
        self._Signature = params.get("Signature")
        self._HospitalId = params.get("HospitalId")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginOutHisToolRequest(AbstractModel):
    r"""LoginOutHisTool请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Header: 登出请求header
        :type Header: :class:`tencentcloud.aca.v20210323.models.LoginOutHeader`
        :param _Data: 登出请求数据
        :type Data: :class:`tencentcloud.aca.v20210323.models.LoginOutData`
        """
        self._Header = None
        self._Data = None

    @property
    def Header(self):
        r"""登出请求header
        :rtype: :class:`tencentcloud.aca.v20210323.models.LoginOutHeader`
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def Data(self):
        r"""登出请求数据
        :rtype: :class:`tencentcloud.aca.v20210323.models.LoginOutData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Header") is not None:
            self._Header = LoginOutHeader()
            self._Header._deserialize(params.get("Header"))
        if params.get("Data") is not None:
            self._Data = LoginOutData()
            self._Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginOutHisToolResponse(AbstractModel):
    r"""LoginOutHisTool返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: 错误码
        :type Code: int
        :param _Message: 错误信息
        :type Message: str
        :param _Data: 响应数据
        :type Data: :class:`tencentcloud.aca.v20210323.models.LoginOutResponseData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Code = None
        self._Message = None
        self._Data = None
        self._RequestId = None

    @property
    def Code(self):
        r"""错误码
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""错误信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Data(self):
        r"""响应数据
        :rtype: :class:`tencentcloud.aca.v20210323.models.LoginOutResponseData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Data") is not None:
            self._Data = LoginOutResponseData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class LoginOutResponseData(AbstractModel):
    r"""登出数据

    """

    def __init__(self):
        r"""
        :param _Timestamp: 服务器时间戳毫秒
        :type Timestamp: int
        """
        self._Timestamp = None

    @property
    def Timestamp(self):
        r"""服务器时间戳毫秒
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperateResp(AbstractModel):
    r"""操作结果

    """

    def __init__(self):
        r"""
        :param _Dummy: 操作结果
        :type Dummy: bool
        """
        self._Dummy = None

    @property
    def Dummy(self):
        r"""操作结果
        :rtype: bool
        """
        return self._Dummy

    @Dummy.setter
    def Dummy(self, Dummy):
        self._Dummy = Dummy


    def _deserialize(self, params):
        self._Dummy = params.get("Dummy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PatientBaseInfo(AbstractModel):
    r"""患者信息

    """

    def __init__(self):
        r"""
        :param _Sex: 性别
        :type Sex: str
        :param _Height: 身高 单位cm
        :type Height: str
        :param _Weight: 体重 单位kg
        :type Weight: str
        :param _PatientId: 患者ID
        :type PatientId: str
        :param _Name: 名称
        :type Name: str
        :param _Age: 年龄
        :type Age: str
        :param _BirthPlace: 出生地
        :type BirthPlace: str
        :param _LivePlace: 居住地
        :type LivePlace: str
        :param _BirthDay: 出生日期和年龄必须传一个
        :type BirthDay: str
        """
        self._Sex = None
        self._Height = None
        self._Weight = None
        self._PatientId = None
        self._Name = None
        self._Age = None
        self._BirthPlace = None
        self._LivePlace = None
        self._BirthDay = None

    @property
    def Sex(self):
        r"""性别
        :rtype: str
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Height(self):
        r"""身高 单位cm
        :rtype: str
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Weight(self):
        r"""体重 单位kg
        :rtype: str
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def PatientId(self):
        r"""患者ID
        :rtype: str
        """
        return self._PatientId

    @PatientId.setter
    def PatientId(self, PatientId):
        self._PatientId = PatientId

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Age(self):
        r"""年龄
        :rtype: str
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def BirthPlace(self):
        r"""出生地
        :rtype: str
        """
        return self._BirthPlace

    @BirthPlace.setter
    def BirthPlace(self, BirthPlace):
        self._BirthPlace = BirthPlace

    @property
    def LivePlace(self):
        r"""居住地
        :rtype: str
        """
        return self._LivePlace

    @LivePlace.setter
    def LivePlace(self, LivePlace):
        self._LivePlace = LivePlace

    @property
    def BirthDay(self):
        r"""出生日期和年龄必须传一个
        :rtype: str
        """
        return self._BirthDay

    @BirthDay.setter
    def BirthDay(self, BirthDay):
        self._BirthDay = BirthDay


    def _deserialize(self, params):
        self._Sex = params.get("Sex")
        self._Height = params.get("Height")
        self._Weight = params.get("Weight")
        self._PatientId = params.get("PatientId")
        self._Name = params.get("Name")
        self._Age = params.get("Age")
        self._BirthPlace = params.get("BirthPlace")
        self._LivePlace = params.get("LivePlace")
        self._BirthDay = params.get("BirthDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PatientFamilyHistory(AbstractModel):
    r"""患者家族病史

    """

    def __init__(self):
        r"""
        :param _FamilyDiseaseHistory: 家族病史 如家族病史不能分开，可传入此字段
        :type FamilyDiseaseHistory: str
        :param _Relation: 关系
        :type Relation: str
        :param _CurrentSituation: 当前情况
        :type CurrentSituation: str
        """
        self._FamilyDiseaseHistory = None
        self._Relation = None
        self._CurrentSituation = None

    @property
    def FamilyDiseaseHistory(self):
        r"""家族病史 如家族病史不能分开，可传入此字段
        :rtype: str
        """
        return self._FamilyDiseaseHistory

    @FamilyDiseaseHistory.setter
    def FamilyDiseaseHistory(self, FamilyDiseaseHistory):
        self._FamilyDiseaseHistory = FamilyDiseaseHistory

    @property
    def Relation(self):
        r"""关系
        :rtype: str
        """
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation

    @property
    def CurrentSituation(self):
        r"""当前情况
        :rtype: str
        """
        return self._CurrentSituation

    @CurrentSituation.setter
    def CurrentSituation(self, CurrentSituation):
        self._CurrentSituation = CurrentSituation


    def _deserialize(self, params):
        self._FamilyDiseaseHistory = params.get("FamilyDiseaseHistory")
        self._Relation = params.get("Relation")
        self._CurrentSituation = params.get("CurrentSituation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PatientHistory(AbstractModel):
    r"""患者过往病史

    """

    def __init__(self):
        r"""
        :param _DiseaseHistory: 病史
        :type DiseaseHistory: str
        :param _TreatmentHistory: 治疗史
        :type TreatmentHistory: str
        """
        self._DiseaseHistory = None
        self._TreatmentHistory = None

    @property
    def DiseaseHistory(self):
        r"""病史
        :rtype: str
        """
        return self._DiseaseHistory

    @DiseaseHistory.setter
    def DiseaseHistory(self, DiseaseHistory):
        self._DiseaseHistory = DiseaseHistory

    @property
    def TreatmentHistory(self):
        r"""治疗史
        :rtype: str
        """
        return self._TreatmentHistory

    @TreatmentHistory.setter
    def TreatmentHistory(self, TreatmentHistory):
        self._TreatmentHistory = TreatmentHistory


    def _deserialize(self, params):
        self._DiseaseHistory = params.get("DiseaseHistory")
        self._TreatmentHistory = params.get("TreatmentHistory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhysicalExam(AbstractModel):
    r"""体格检查

    """

    def __init__(self):
        r"""
        :param _Pulse: 脉搏，单位：次/分
        :type Pulse: str
        :param _Breathe: 呼吸，单位：次/分
        :type Breathe: str
        :param _Weight: 体重，单位KG
        :type Weight: str
        :param _BodyTemperature: 体温，单位：℃ 
        :type BodyTemperature: str
        :param _DiastolicPressure: 舒张压， 单位：mmHg
        :type DiastolicPressure: str
        :param _SystolicPressure: 收缩压， 单位：mmHg
        :type SystolicPressure: str
        """
        self._Pulse = None
        self._Breathe = None
        self._Weight = None
        self._BodyTemperature = None
        self._DiastolicPressure = None
        self._SystolicPressure = None

    @property
    def Pulse(self):
        r"""脉搏，单位：次/分
        :rtype: str
        """
        return self._Pulse

    @Pulse.setter
    def Pulse(self, Pulse):
        self._Pulse = Pulse

    @property
    def Breathe(self):
        r"""呼吸，单位：次/分
        :rtype: str
        """
        return self._Breathe

    @Breathe.setter
    def Breathe(self, Breathe):
        self._Breathe = Breathe

    @property
    def Weight(self):
        r"""体重，单位KG
        :rtype: str
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def BodyTemperature(self):
        r"""体温，单位：℃ 
        :rtype: str
        """
        return self._BodyTemperature

    @BodyTemperature.setter
    def BodyTemperature(self, BodyTemperature):
        self._BodyTemperature = BodyTemperature

    @property
    def DiastolicPressure(self):
        r"""舒张压， 单位：mmHg
        :rtype: str
        """
        return self._DiastolicPressure

    @DiastolicPressure.setter
    def DiastolicPressure(self, DiastolicPressure):
        self._DiastolicPressure = DiastolicPressure

    @property
    def SystolicPressure(self):
        r"""收缩压， 单位：mmHg
        :rtype: str
        """
        return self._SystolicPressure

    @SystolicPressure.setter
    def SystolicPressure(self, SystolicPressure):
        self._SystolicPressure = SystolicPressure


    def _deserialize(self, params):
        self._Pulse = params.get("Pulse")
        self._Breathe = params.get("Breathe")
        self._Weight = params.get("Weight")
        self._BodyTemperature = params.get("BodyTemperature")
        self._DiastolicPressure = params.get("DiastolicPressure")
        self._SystolicPressure = params.get("SystolicPressure")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RationalDrugInfo(AbstractModel):
    r"""合理用药信息

    """

    def __init__(self):
        r"""
        :param _Hit: 是否有风险
        :type Hit: bool
        :param _DrugUsages: 药品用量风险
        :type DrugUsages: list of RiskInfo
        :param _DrugRepeats: 重复用药风险
        :type DrugRepeats: list of RiskInfo
        :param _DrugRoutes: 用药途径风险
        :type DrugRoutes: list of RiskInfo
        :param _SpecialPopulations: 特殊人群风险
        :type SpecialPopulations: list of RiskInfo
        :param _DrugTaboos: 禁忌症风险
        :type DrugTaboos: list of RiskInfo
        :param _DrugInteractions: 相互作用风险
        :type DrugInteractions: list of RiskInfo
        :param _DrugIncompatibility: 配伍禁忌风险
        :type DrugIncompatibility: list of RiskInfo
        :param _DrugAllergys: 过敏风险
        :type DrugAllergys: list of RiskInfo
        :param _DrugIndications: 适应症风险
        :type DrugIndications: list of RiskInfo
        :param _Abnormals: 异常提醒
        :type Abnormals: list of Abnormals
        :param _DrugList: 药品列表
        :type DrugList: list of DrugList
        """
        self._Hit = None
        self._DrugUsages = None
        self._DrugRepeats = None
        self._DrugRoutes = None
        self._SpecialPopulations = None
        self._DrugTaboos = None
        self._DrugInteractions = None
        self._DrugIncompatibility = None
        self._DrugAllergys = None
        self._DrugIndications = None
        self._Abnormals = None
        self._DrugList = None

    @property
    def Hit(self):
        r"""是否有风险
        :rtype: bool
        """
        return self._Hit

    @Hit.setter
    def Hit(self, Hit):
        self._Hit = Hit

    @property
    def DrugUsages(self):
        r"""药品用量风险
        :rtype: list of RiskInfo
        """
        return self._DrugUsages

    @DrugUsages.setter
    def DrugUsages(self, DrugUsages):
        self._DrugUsages = DrugUsages

    @property
    def DrugRepeats(self):
        r"""重复用药风险
        :rtype: list of RiskInfo
        """
        return self._DrugRepeats

    @DrugRepeats.setter
    def DrugRepeats(self, DrugRepeats):
        self._DrugRepeats = DrugRepeats

    @property
    def DrugRoutes(self):
        r"""用药途径风险
        :rtype: list of RiskInfo
        """
        return self._DrugRoutes

    @DrugRoutes.setter
    def DrugRoutes(self, DrugRoutes):
        self._DrugRoutes = DrugRoutes

    @property
    def SpecialPopulations(self):
        r"""特殊人群风险
        :rtype: list of RiskInfo
        """
        return self._SpecialPopulations

    @SpecialPopulations.setter
    def SpecialPopulations(self, SpecialPopulations):
        self._SpecialPopulations = SpecialPopulations

    @property
    def DrugTaboos(self):
        r"""禁忌症风险
        :rtype: list of RiskInfo
        """
        return self._DrugTaboos

    @DrugTaboos.setter
    def DrugTaboos(self, DrugTaboos):
        self._DrugTaboos = DrugTaboos

    @property
    def DrugInteractions(self):
        r"""相互作用风险
        :rtype: list of RiskInfo
        """
        return self._DrugInteractions

    @DrugInteractions.setter
    def DrugInteractions(self, DrugInteractions):
        self._DrugInteractions = DrugInteractions

    @property
    def DrugIncompatibility(self):
        r"""配伍禁忌风险
        :rtype: list of RiskInfo
        """
        return self._DrugIncompatibility

    @DrugIncompatibility.setter
    def DrugIncompatibility(self, DrugIncompatibility):
        self._DrugIncompatibility = DrugIncompatibility

    @property
    def DrugAllergys(self):
        r"""过敏风险
        :rtype: list of RiskInfo
        """
        return self._DrugAllergys

    @DrugAllergys.setter
    def DrugAllergys(self, DrugAllergys):
        self._DrugAllergys = DrugAllergys

    @property
    def DrugIndications(self):
        r"""适应症风险
        :rtype: list of RiskInfo
        """
        return self._DrugIndications

    @DrugIndications.setter
    def DrugIndications(self, DrugIndications):
        self._DrugIndications = DrugIndications

    @property
    def Abnormals(self):
        r"""异常提醒
        :rtype: list of Abnormals
        """
        return self._Abnormals

    @Abnormals.setter
    def Abnormals(self, Abnormals):
        self._Abnormals = Abnormals

    @property
    def DrugList(self):
        r"""药品列表
        :rtype: list of DrugList
        """
        return self._DrugList

    @DrugList.setter
    def DrugList(self, DrugList):
        self._DrugList = DrugList


    def _deserialize(self, params):
        self._Hit = params.get("Hit")
        if params.get("DrugUsages") is not None:
            self._DrugUsages = []
            for item in params.get("DrugUsages"):
                obj = RiskInfo()
                obj._deserialize(item)
                self._DrugUsages.append(obj)
        if params.get("DrugRepeats") is not None:
            self._DrugRepeats = []
            for item in params.get("DrugRepeats"):
                obj = RiskInfo()
                obj._deserialize(item)
                self._DrugRepeats.append(obj)
        if params.get("DrugRoutes") is not None:
            self._DrugRoutes = []
            for item in params.get("DrugRoutes"):
                obj = RiskInfo()
                obj._deserialize(item)
                self._DrugRoutes.append(obj)
        if params.get("SpecialPopulations") is not None:
            self._SpecialPopulations = []
            for item in params.get("SpecialPopulations"):
                obj = RiskInfo()
                obj._deserialize(item)
                self._SpecialPopulations.append(obj)
        if params.get("DrugTaboos") is not None:
            self._DrugTaboos = []
            for item in params.get("DrugTaboos"):
                obj = RiskInfo()
                obj._deserialize(item)
                self._DrugTaboos.append(obj)
        if params.get("DrugInteractions") is not None:
            self._DrugInteractions = []
            for item in params.get("DrugInteractions"):
                obj = RiskInfo()
                obj._deserialize(item)
                self._DrugInteractions.append(obj)
        if params.get("DrugIncompatibility") is not None:
            self._DrugIncompatibility = []
            for item in params.get("DrugIncompatibility"):
                obj = RiskInfo()
                obj._deserialize(item)
                self._DrugIncompatibility.append(obj)
        if params.get("DrugAllergys") is not None:
            self._DrugAllergys = []
            for item in params.get("DrugAllergys"):
                obj = RiskInfo()
                obj._deserialize(item)
                self._DrugAllergys.append(obj)
        if params.get("DrugIndications") is not None:
            self._DrugIndications = []
            for item in params.get("DrugIndications"):
                obj = RiskInfo()
                obj._deserialize(item)
                self._DrugIndications.append(obj)
        if params.get("Abnormals") is not None:
            self._Abnormals = []
            for item in params.get("Abnormals"):
                obj = Abnormals()
                obj._deserialize(item)
                self._Abnormals.append(obj)
        if params.get("DrugList") is not None:
            self._DrugList = []
            for item in params.get("DrugList"):
                obj = DrugList()
                obj._deserialize(item)
                self._DrugList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecommendedUsage(AbstractModel):
    r"""推荐用法

    """

    def __init__(self):
        r"""
        :param _UsageRoute: 给药途径
        :type UsageRoute: str
        :param _Frequency: 给药频率 格式为“最小频次,最大频次,频次单位,频次周期”，如"1,2,次,2"， 表示2天内最少给药1次，最大给药2次。
        :type Frequency: str
        :param _SingleDose: 给药剂量 格式为"最小剂量,最大剂量,剂量单位"，如"10,10,ml"，<br>表示每次最大给药量为10ml，最小给药量为10ml。
        :type SingleDose: str
        """
        self._UsageRoute = None
        self._Frequency = None
        self._SingleDose = None

    @property
    def UsageRoute(self):
        r"""给药途径
        :rtype: str
        """
        return self._UsageRoute

    @UsageRoute.setter
    def UsageRoute(self, UsageRoute):
        self._UsageRoute = UsageRoute

    @property
    def Frequency(self):
        r"""给药频率 格式为“最小频次,最大频次,频次单位,频次周期”，如"1,2,次,2"， 表示2天内最少给药1次，最大给药2次。
        :rtype: str
        """
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def SingleDose(self):
        r"""给药剂量 格式为"最小剂量,最大剂量,剂量单位"，如"10,10,ml"，<br>表示每次最大给药量为10ml，最小给药量为10ml。
        :rtype: str
        """
        return self._SingleDose

    @SingleDose.setter
    def SingleDose(self, SingleDose):
        self._SingleDose = SingleDose


    def _deserialize(self, params):
        self._UsageRoute = params.get("UsageRoute")
        self._Frequency = params.get("Frequency")
        self._SingleDose = params.get("SingleDose")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordQuality(AbstractModel):
    r"""病历质控

    """

    def __init__(self):
        r"""
        :param _Hit: 病历是否有问题
        :type Hit: bool
        :param _Completeness: 完整性问题
        :type Completeness: str
        :param _Timeliness: 及时性问题
        :type Timeliness: str
        :param _Logical: 逻辑性问题
        :type Logical: str
        """
        self._Hit = None
        self._Completeness = None
        self._Timeliness = None
        self._Logical = None

    @property
    def Hit(self):
        r"""病历是否有问题
        :rtype: bool
        """
        return self._Hit

    @Hit.setter
    def Hit(self, Hit):
        self._Hit = Hit

    @property
    def Completeness(self):
        r"""完整性问题
        :rtype: str
        """
        return self._Completeness

    @Completeness.setter
    def Completeness(self, Completeness):
        self._Completeness = Completeness

    @property
    def Timeliness(self):
        r"""及时性问题
        :rtype: str
        """
        return self._Timeliness

    @Timeliness.setter
    def Timeliness(self, Timeliness):
        self._Timeliness = Timeliness

    @property
    def Logical(self):
        r"""逻辑性问题
        :rtype: str
        """
        return self._Logical

    @Logical.setter
    def Logical(self, Logical):
        self._Logical = Logical


    def _deserialize(self, params):
        self._Hit = params.get("Hit")
        self._Completeness = params.get("Completeness")
        self._Timeliness = params.get("Timeliness")
        self._Logical = params.get("Logical")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReferralInfo(AbstractModel):
    r"""转诊提醒

    """

    def __init__(self):
        r"""
        :param _Hit: 命中
        :type Hit: bool
        :param _Tips: 提示
        :type Tips: str
        """
        self._Hit = None
        self._Tips = None

    @property
    def Hit(self):
        r"""命中
        :rtype: bool
        """
        return self._Hit

    @Hit.setter
    def Hit(self, Hit):
        self._Hit = Hit

    @property
    def Tips(self):
        r"""提示
        :rtype: str
        """
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips


    def _deserialize(self, params):
        self._Hit = params.get("Hit")
        self._Tips = params.get("Tips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestCase(AbstractModel):
    r"""预测数据

    """

    def __init__(self):
        r"""
        :param _CaseType: 处方类型 0:门诊处方；1:住院医嘱；2:急诊处方 
        :type CaseType: int
        :param _ChiefComplaint: 主诉
        :type ChiefComplaint: str
        :param _Department: 科室
        :type Department: str
        :param _CaseId: 病历文书ID
医生每次书写病历文书的ID，文书内容包含主诉，病史，当前诊断等内容<br />门诊场景：门诊病历文书（带有主诉、病史、诊断及药品的）只有一份，这个编号只有一个。<br/>住院场景：假设住院3天，医生每天都会写一份病历文书（带有主诉、病史、诊断及医嘱药品的文书），那么有对应三个病历文书编号，每次调用预测接口都要传入不同的病历文书编号。注意：如两次调用预测接口，传相同的caseid，则在药师端管理平台的上一次审方记录中的诊断会被本次接口传入的诊断更新。
        :type CaseId: str
        :param _CaseTime: 病历更新时间
        :type CaseTime: str
        :param _VisitId: 就诊ID
门诊处方传门诊号，住院医嘱传住院号；备注：门诊场景：用户挂一次号，看一个医生，这时候会有一个代表变成就诊的编号，下一次挂号就诊，这个编号会变。<br/>住院场景：用户本次办理入院，会有一个住院编号，仅代表本次住院，如果下次再住院，这个编号会变。
        :type VisitId: str
        :param _PatientBaseinfo: 患者信息
        :type PatientBaseinfo: :class:`tencentcloud.aca.v20210323.models.PatientBaseInfo`
        :param _DoctorInfo: 医生信息
        :type DoctorInfo: :class:`tencentcloud.aca.v20210323.models.DoctorInfo`
        :param _PresentIllness: 现病史
        :type PresentIllness: str
        :param _PatientOther: 患者其他信息，包含过敏史等
        :type PatientOther: str
        :param _PatientHistory: 患者过往病史
        :type PatientHistory: :class:`tencentcloud.aca.v20210323.models.PatientHistory`
        :param _PatientFamilyHistory: 患者家族病史
        :type PatientFamilyHistory: :class:`tencentcloud.aca.v20210323.models.PatientFamilyHistory`
        :param _PhysicalExam: 体格检查
        :type PhysicalExam: :class:`tencentcloud.aca.v20210323.models.PhysicalExam`
        :param _EmrDiagnosises: 诊断列表，第一个为首要诊断
        :type EmrDiagnosises: list of EmrDiagnosises
        :param _Prescriptions: 处方列表
        :type Prescriptions: list of DrugUsage
        """
        self._CaseType = None
        self._ChiefComplaint = None
        self._Department = None
        self._CaseId = None
        self._CaseTime = None
        self._VisitId = None
        self._PatientBaseinfo = None
        self._DoctorInfo = None
        self._PresentIllness = None
        self._PatientOther = None
        self._PatientHistory = None
        self._PatientFamilyHistory = None
        self._PhysicalExam = None
        self._EmrDiagnosises = None
        self._Prescriptions = None

    @property
    def CaseType(self):
        r"""处方类型 0:门诊处方；1:住院医嘱；2:急诊处方 
        :rtype: int
        """
        return self._CaseType

    @CaseType.setter
    def CaseType(self, CaseType):
        self._CaseType = CaseType

    @property
    def ChiefComplaint(self):
        r"""主诉
        :rtype: str
        """
        return self._ChiefComplaint

    @ChiefComplaint.setter
    def ChiefComplaint(self, ChiefComplaint):
        self._ChiefComplaint = ChiefComplaint

    @property
    def Department(self):
        r"""科室
        :rtype: str
        """
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def CaseId(self):
        r"""病历文书ID
医生每次书写病历文书的ID，文书内容包含主诉，病史，当前诊断等内容<br />门诊场景：门诊病历文书（带有主诉、病史、诊断及药品的）只有一份，这个编号只有一个。<br/>住院场景：假设住院3天，医生每天都会写一份病历文书（带有主诉、病史、诊断及医嘱药品的文书），那么有对应三个病历文书编号，每次调用预测接口都要传入不同的病历文书编号。注意：如两次调用预测接口，传相同的caseid，则在药师端管理平台的上一次审方记录中的诊断会被本次接口传入的诊断更新。
        :rtype: str
        """
        return self._CaseId

    @CaseId.setter
    def CaseId(self, CaseId):
        self._CaseId = CaseId

    @property
    def CaseTime(self):
        r"""病历更新时间
        :rtype: str
        """
        return self._CaseTime

    @CaseTime.setter
    def CaseTime(self, CaseTime):
        self._CaseTime = CaseTime

    @property
    def VisitId(self):
        r"""就诊ID
门诊处方传门诊号，住院医嘱传住院号；备注：门诊场景：用户挂一次号，看一个医生，这时候会有一个代表变成就诊的编号，下一次挂号就诊，这个编号会变。<br/>住院场景：用户本次办理入院，会有一个住院编号，仅代表本次住院，如果下次再住院，这个编号会变。
        :rtype: str
        """
        return self._VisitId

    @VisitId.setter
    def VisitId(self, VisitId):
        self._VisitId = VisitId

    @property
    def PatientBaseinfo(self):
        r"""患者信息
        :rtype: :class:`tencentcloud.aca.v20210323.models.PatientBaseInfo`
        """
        return self._PatientBaseinfo

    @PatientBaseinfo.setter
    def PatientBaseinfo(self, PatientBaseinfo):
        self._PatientBaseinfo = PatientBaseinfo

    @property
    def DoctorInfo(self):
        r"""医生信息
        :rtype: :class:`tencentcloud.aca.v20210323.models.DoctorInfo`
        """
        return self._DoctorInfo

    @DoctorInfo.setter
    def DoctorInfo(self, DoctorInfo):
        self._DoctorInfo = DoctorInfo

    @property
    def PresentIllness(self):
        r"""现病史
        :rtype: str
        """
        return self._PresentIllness

    @PresentIllness.setter
    def PresentIllness(self, PresentIllness):
        self._PresentIllness = PresentIllness

    @property
    def PatientOther(self):
        r"""患者其他信息，包含过敏史等
        :rtype: str
        """
        return self._PatientOther

    @PatientOther.setter
    def PatientOther(self, PatientOther):
        self._PatientOther = PatientOther

    @property
    def PatientHistory(self):
        r"""患者过往病史
        :rtype: :class:`tencentcloud.aca.v20210323.models.PatientHistory`
        """
        return self._PatientHistory

    @PatientHistory.setter
    def PatientHistory(self, PatientHistory):
        self._PatientHistory = PatientHistory

    @property
    def PatientFamilyHistory(self):
        r"""患者家族病史
        :rtype: :class:`tencentcloud.aca.v20210323.models.PatientFamilyHistory`
        """
        return self._PatientFamilyHistory

    @PatientFamilyHistory.setter
    def PatientFamilyHistory(self, PatientFamilyHistory):
        self._PatientFamilyHistory = PatientFamilyHistory

    @property
    def PhysicalExam(self):
        r"""体格检查
        :rtype: :class:`tencentcloud.aca.v20210323.models.PhysicalExam`
        """
        return self._PhysicalExam

    @PhysicalExam.setter
    def PhysicalExam(self, PhysicalExam):
        self._PhysicalExam = PhysicalExam

    @property
    def EmrDiagnosises(self):
        r"""诊断列表，第一个为首要诊断
        :rtype: list of EmrDiagnosises
        """
        return self._EmrDiagnosises

    @EmrDiagnosises.setter
    def EmrDiagnosises(self, EmrDiagnosises):
        self._EmrDiagnosises = EmrDiagnosises

    @property
    def Prescriptions(self):
        r"""处方列表
        :rtype: list of DrugUsage
        """
        return self._Prescriptions

    @Prescriptions.setter
    def Prescriptions(self, Prescriptions):
        self._Prescriptions = Prescriptions


    def _deserialize(self, params):
        self._CaseType = params.get("CaseType")
        self._ChiefComplaint = params.get("ChiefComplaint")
        self._Department = params.get("Department")
        self._CaseId = params.get("CaseId")
        self._CaseTime = params.get("CaseTime")
        self._VisitId = params.get("VisitId")
        if params.get("PatientBaseinfo") is not None:
            self._PatientBaseinfo = PatientBaseInfo()
            self._PatientBaseinfo._deserialize(params.get("PatientBaseinfo"))
        if params.get("DoctorInfo") is not None:
            self._DoctorInfo = DoctorInfo()
            self._DoctorInfo._deserialize(params.get("DoctorInfo"))
        self._PresentIllness = params.get("PresentIllness")
        self._PatientOther = params.get("PatientOther")
        if params.get("PatientHistory") is not None:
            self._PatientHistory = PatientHistory()
            self._PatientHistory._deserialize(params.get("PatientHistory"))
        if params.get("PatientFamilyHistory") is not None:
            self._PatientFamilyHistory = PatientFamilyHistory()
            self._PatientFamilyHistory._deserialize(params.get("PatientFamilyHistory"))
        if params.get("PhysicalExam") is not None:
            self._PhysicalExam = PhysicalExam()
            self._PhysicalExam._deserialize(params.get("PhysicalExam"))
        if params.get("EmrDiagnosises") is not None:
            self._EmrDiagnosises = []
            for item in params.get("EmrDiagnosises"):
                obj = EmrDiagnosises()
                obj._deserialize(item)
                self._EmrDiagnosises.append(obj)
        if params.get("Prescriptions") is not None:
            self._Prescriptions = []
            for item in params.get("Prescriptions"):
                obj = DrugUsage()
                obj._deserialize(item)
                self._Prescriptions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskInfo(AbstractModel):
    r"""风险信息

    """

    def __init__(self):
        r"""
        :param _DrugId: 药品ID
        :type DrugId: str
        :param _DrugName: 药品名称
        :type DrugName: str
        :param _RiskLevel: 风险等级：低级风险、中级风险、高级风险
        :type RiskLevel: str
        :param _RiskTips: 风险提示
        :type RiskTips: str
        :param _FdaLevel: FDA分级
        :type FdaLevel: str
        :param _RelatedDrugName: 关联药品名称
        :type RelatedDrugName: str
        :param _RelatedPrescriptionId: 关联处方ID
        :type RelatedPrescriptionId: str
        """
        self._DrugId = None
        self._DrugName = None
        self._RiskLevel = None
        self._RiskTips = None
        self._FdaLevel = None
        self._RelatedDrugName = None
        self._RelatedPrescriptionId = None

    @property
    def DrugId(self):
        r"""药品ID
        :rtype: str
        """
        return self._DrugId

    @DrugId.setter
    def DrugId(self, DrugId):
        self._DrugId = DrugId

    @property
    def DrugName(self):
        r"""药品名称
        :rtype: str
        """
        return self._DrugName

    @DrugName.setter
    def DrugName(self, DrugName):
        self._DrugName = DrugName

    @property
    def RiskLevel(self):
        r"""风险等级：低级风险、中级风险、高级风险
        :rtype: str
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RiskTips(self):
        r"""风险提示
        :rtype: str
        """
        return self._RiskTips

    @RiskTips.setter
    def RiskTips(self, RiskTips):
        self._RiskTips = RiskTips

    @property
    def FdaLevel(self):
        r"""FDA分级
        :rtype: str
        """
        return self._FdaLevel

    @FdaLevel.setter
    def FdaLevel(self, FdaLevel):
        self._FdaLevel = FdaLevel

    @property
    def RelatedDrugName(self):
        r"""关联药品名称
        :rtype: str
        """
        return self._RelatedDrugName

    @RelatedDrugName.setter
    def RelatedDrugName(self, RelatedDrugName):
        self._RelatedDrugName = RelatedDrugName

    @property
    def RelatedPrescriptionId(self):
        r"""关联处方ID
        :rtype: str
        """
        return self._RelatedPrescriptionId

    @RelatedPrescriptionId.setter
    def RelatedPrescriptionId(self, RelatedPrescriptionId):
        self._RelatedPrescriptionId = RelatedPrescriptionId


    def _deserialize(self, params):
        self._DrugId = params.get("DrugId")
        self._DrugName = params.get("DrugName")
        self._RiskLevel = params.get("RiskLevel")
        self._RiskTips = params.get("RiskTips")
        self._FdaLevel = params.get("FdaLevel")
        self._RelatedDrugName = params.get("RelatedDrugName")
        self._RelatedPrescriptionId = params.get("RelatedPrescriptionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartDrugInfoData(AbstractModel):
    r"""智能用药请求数据

    """

    def __init__(self):
        r"""
        :param _DrugName: 药品名称
        :type DrugName: str
        :param _Specifications: 规格
        :type Specifications: str
        :param _ApprovalNumber: 批准文号
        :type ApprovalNumber: str
        :param _Manufacturer: 生产厂家
        :type Manufacturer: str
        :param _DrugId: 药品ID
        :type DrugId: str
        :param _Diagnosis: 诊断
        :type Diagnosis: str
        :param _Age: 年龄
        :type Age: float
        """
        self._DrugName = None
        self._Specifications = None
        self._ApprovalNumber = None
        self._Manufacturer = None
        self._DrugId = None
        self._Diagnosis = None
        self._Age = None

    @property
    def DrugName(self):
        r"""药品名称
        :rtype: str
        """
        return self._DrugName

    @DrugName.setter
    def DrugName(self, DrugName):
        self._DrugName = DrugName

    @property
    def Specifications(self):
        r"""规格
        :rtype: str
        """
        return self._Specifications

    @Specifications.setter
    def Specifications(self, Specifications):
        self._Specifications = Specifications

    @property
    def ApprovalNumber(self):
        r"""批准文号
        :rtype: str
        """
        return self._ApprovalNumber

    @ApprovalNumber.setter
    def ApprovalNumber(self, ApprovalNumber):
        self._ApprovalNumber = ApprovalNumber

    @property
    def Manufacturer(self):
        r"""生产厂家
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def DrugId(self):
        r"""药品ID
        :rtype: str
        """
        return self._DrugId

    @DrugId.setter
    def DrugId(self, DrugId):
        self._DrugId = DrugId

    @property
    def Diagnosis(self):
        r"""诊断
        :rtype: str
        """
        return self._Diagnosis

    @Diagnosis.setter
    def Diagnosis(self, Diagnosis):
        self._Diagnosis = Diagnosis

    @property
    def Age(self):
        r"""年龄
        :rtype: float
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age


    def _deserialize(self, params):
        self._DrugName = params.get("DrugName")
        self._Specifications = params.get("Specifications")
        self._ApprovalNumber = params.get("ApprovalNumber")
        self._Manufacturer = params.get("Manufacturer")
        self._DrugId = params.get("DrugId")
        self._Diagnosis = params.get("Diagnosis")
        self._Age = params.get("Age")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartDrugInfoRequest(AbstractModel):
    r"""SmartDrugInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Header: 请求头
        :type Header: :class:`tencentcloud.aca.v20210323.models.CommonHeader`
        :param _Data: 药品信息
        :type Data: :class:`tencentcloud.aca.v20210323.models.SmartDrugInfoData`
        """
        self._Header = None
        self._Data = None

    @property
    def Header(self):
        r"""请求头
        :rtype: :class:`tencentcloud.aca.v20210323.models.CommonHeader`
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def Data(self):
        r"""药品信息
        :rtype: :class:`tencentcloud.aca.v20210323.models.SmartDrugInfoData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Header") is not None:
            self._Header = CommonHeader()
            self._Header._deserialize(params.get("Header"))
        if params.get("Data") is not None:
            self._Data = SmartDrugInfoData()
            self._Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartDrugInfoResp(AbstractModel):
    r"""智能用药响应

    """

    def __init__(self):
        r"""
        :param _DrugId: 药品ID
        :type DrugId: str
        :param _SequenceId: 序列ID
        :type SequenceId: int
        :param _DrugHashId: 药品哈希ID
        :type DrugHashId: str
        :param _ImgUrl: 图片URL
        :type ImgUrl: str
        :param _DrugName: 药品名称
        :type DrugName: str
        :param _TradeName: 商品名
        :type TradeName: str
        :param _EnglishName: 英文名称
        :type EnglishName: str
        :param _EnglishTradeName: 英文商品名
        :type EnglishTradeName: str
        :param _Pinyin: 拼音
        :type Pinyin: str
        :param _OtherNames: 其他名称
        :type OtherNames: str
        :param _ChemicalName: 化学名称
        :type ChemicalName: str
        :param _EnglishChemicalName: 英文化学名称
        :type EnglishChemicalName: str
        :param _ApprovalNumber: 批准文号
        :type ApprovalNumber: str
        :param _Property: 药品属性标签 多个标签时 | 分隔，如抗菌药|抗生素|贵重药品
        :type Property: str
        :param _Ingredients: 药品成分
        :type Ingredients: str
        :param _PhenotypicTrait: 药品性状
        :type PhenotypicTrait: str
        :param _Indications: 适应症
        :type Indications: str
        :param _Specifications: 规格
        :type Specifications: str
        :param _UsageAndDosage: 用法用量
        :type UsageAndDosage: str
        :param _RecommendedUsage: 推荐用法
        :type RecommendedUsage: :class:`tencentcloud.aca.v20210323.models.RecommendedUsage`
        :param _AdverseReaction: 不良反应
        :type AdverseReaction: str
        :param _Contraindication: 禁忌
        :type Contraindication: str
        :param _Attentions: 注意事项
        :type Attentions: str
        :param _Overdose: 药物过量
        :type Overdose: str
        :param _PregnantAndLactatingWomen: 孕妇及哺乳期妇女用药
        :type PregnantAndLactatingWomen: str
        :param _ElderlyPatients: 老年患者用药
        :type ElderlyPatients: str
        :param _PediatricDrugs: 儿童用药
        :type PediatricDrugs: str
        :param _Interactions: 药物相互作用
        :type Interactions: str
        :param _ClinicalResearch: 临床研究
        :type ClinicalResearch: str
        :param _PharmacologyToxicology: 药理毒理
        :type PharmacologyToxicology: str
        :param _Pharmacokinetics: 药代动力学
        :type Pharmacokinetics: str
        :param _Warning: 警告
        :type Warning: str
        :param _ExpireDate: 有效期
        :type ExpireDate: str
        :param _Storage: 贮藏
        :type Storage: str
        :param _Pack: 包装
        :type Pack: str
        :param _Manufacturer: 生产企业
        :type Manufacturer: str
        :param _ManufacturerAddress: 生产企业地址
        :type ManufacturerAddress: str
        :param _ManufacturerPhone: 生产企业电话
        :type ManufacturerPhone: str
        :param _ManufacturerEmail: 生产企业邮箱
        :type ManufacturerEmail: str
        :param _ManufacturerWebsite: 生产企业网站
        :type ManufacturerWebsite: str
        :param _DocRevisionTime: 说明书制定和修订时间
        :type DocRevisionTime: str
        :param _References: 参考文献
        :type References: str
        :param _DrugDosageForm: 剂型
        :type DrugDosageForm: str
        :param _DrugRoute: 给药途径
        :type DrugRoute: str
        :param _DrugBasicCode: 药品本位码
        :type DrugBasicCode: str
        :param _OctTag: OTC标签
        :type OctTag: str
        """
        self._DrugId = None
        self._SequenceId = None
        self._DrugHashId = None
        self._ImgUrl = None
        self._DrugName = None
        self._TradeName = None
        self._EnglishName = None
        self._EnglishTradeName = None
        self._Pinyin = None
        self._OtherNames = None
        self._ChemicalName = None
        self._EnglishChemicalName = None
        self._ApprovalNumber = None
        self._Property = None
        self._Ingredients = None
        self._PhenotypicTrait = None
        self._Indications = None
        self._Specifications = None
        self._UsageAndDosage = None
        self._RecommendedUsage = None
        self._AdverseReaction = None
        self._Contraindication = None
        self._Attentions = None
        self._Overdose = None
        self._PregnantAndLactatingWomen = None
        self._ElderlyPatients = None
        self._PediatricDrugs = None
        self._Interactions = None
        self._ClinicalResearch = None
        self._PharmacologyToxicology = None
        self._Pharmacokinetics = None
        self._Warning = None
        self._ExpireDate = None
        self._Storage = None
        self._Pack = None
        self._Manufacturer = None
        self._ManufacturerAddress = None
        self._ManufacturerPhone = None
        self._ManufacturerEmail = None
        self._ManufacturerWebsite = None
        self._DocRevisionTime = None
        self._References = None
        self._DrugDosageForm = None
        self._DrugRoute = None
        self._DrugBasicCode = None
        self._OctTag = None

    @property
    def DrugId(self):
        r"""药品ID
        :rtype: str
        """
        return self._DrugId

    @DrugId.setter
    def DrugId(self, DrugId):
        self._DrugId = DrugId

    @property
    def SequenceId(self):
        r"""序列ID
        :rtype: int
        """
        return self._SequenceId

    @SequenceId.setter
    def SequenceId(self, SequenceId):
        self._SequenceId = SequenceId

    @property
    def DrugHashId(self):
        r"""药品哈希ID
        :rtype: str
        """
        return self._DrugHashId

    @DrugHashId.setter
    def DrugHashId(self, DrugHashId):
        self._DrugHashId = DrugHashId

    @property
    def ImgUrl(self):
        r"""图片URL
        :rtype: str
        """
        return self._ImgUrl

    @ImgUrl.setter
    def ImgUrl(self, ImgUrl):
        self._ImgUrl = ImgUrl

    @property
    def DrugName(self):
        r"""药品名称
        :rtype: str
        """
        return self._DrugName

    @DrugName.setter
    def DrugName(self, DrugName):
        self._DrugName = DrugName

    @property
    def TradeName(self):
        r"""商品名
        :rtype: str
        """
        return self._TradeName

    @TradeName.setter
    def TradeName(self, TradeName):
        self._TradeName = TradeName

    @property
    def EnglishName(self):
        r"""英文名称
        :rtype: str
        """
        return self._EnglishName

    @EnglishName.setter
    def EnglishName(self, EnglishName):
        self._EnglishName = EnglishName

    @property
    def EnglishTradeName(self):
        r"""英文商品名
        :rtype: str
        """
        return self._EnglishTradeName

    @EnglishTradeName.setter
    def EnglishTradeName(self, EnglishTradeName):
        self._EnglishTradeName = EnglishTradeName

    @property
    def Pinyin(self):
        r"""拼音
        :rtype: str
        """
        return self._Pinyin

    @Pinyin.setter
    def Pinyin(self, Pinyin):
        self._Pinyin = Pinyin

    @property
    def OtherNames(self):
        r"""其他名称
        :rtype: str
        """
        return self._OtherNames

    @OtherNames.setter
    def OtherNames(self, OtherNames):
        self._OtherNames = OtherNames

    @property
    def ChemicalName(self):
        r"""化学名称
        :rtype: str
        """
        return self._ChemicalName

    @ChemicalName.setter
    def ChemicalName(self, ChemicalName):
        self._ChemicalName = ChemicalName

    @property
    def EnglishChemicalName(self):
        r"""英文化学名称
        :rtype: str
        """
        return self._EnglishChemicalName

    @EnglishChemicalName.setter
    def EnglishChemicalName(self, EnglishChemicalName):
        self._EnglishChemicalName = EnglishChemicalName

    @property
    def ApprovalNumber(self):
        r"""批准文号
        :rtype: str
        """
        return self._ApprovalNumber

    @ApprovalNumber.setter
    def ApprovalNumber(self, ApprovalNumber):
        self._ApprovalNumber = ApprovalNumber

    @property
    def Property(self):
        r"""药品属性标签 多个标签时 | 分隔，如抗菌药|抗生素|贵重药品
        :rtype: str
        """
        return self._Property

    @Property.setter
    def Property(self, Property):
        self._Property = Property

    @property
    def Ingredients(self):
        r"""药品成分
        :rtype: str
        """
        return self._Ingredients

    @Ingredients.setter
    def Ingredients(self, Ingredients):
        self._Ingredients = Ingredients

    @property
    def PhenotypicTrait(self):
        r"""药品性状
        :rtype: str
        """
        return self._PhenotypicTrait

    @PhenotypicTrait.setter
    def PhenotypicTrait(self, PhenotypicTrait):
        self._PhenotypicTrait = PhenotypicTrait

    @property
    def Indications(self):
        r"""适应症
        :rtype: str
        """
        return self._Indications

    @Indications.setter
    def Indications(self, Indications):
        self._Indications = Indications

    @property
    def Specifications(self):
        r"""规格
        :rtype: str
        """
        return self._Specifications

    @Specifications.setter
    def Specifications(self, Specifications):
        self._Specifications = Specifications

    @property
    def UsageAndDosage(self):
        r"""用法用量
        :rtype: str
        """
        return self._UsageAndDosage

    @UsageAndDosage.setter
    def UsageAndDosage(self, UsageAndDosage):
        self._UsageAndDosage = UsageAndDosage

    @property
    def RecommendedUsage(self):
        r"""推荐用法
        :rtype: :class:`tencentcloud.aca.v20210323.models.RecommendedUsage`
        """
        return self._RecommendedUsage

    @RecommendedUsage.setter
    def RecommendedUsage(self, RecommendedUsage):
        self._RecommendedUsage = RecommendedUsage

    @property
    def AdverseReaction(self):
        r"""不良反应
        :rtype: str
        """
        return self._AdverseReaction

    @AdverseReaction.setter
    def AdverseReaction(self, AdverseReaction):
        self._AdverseReaction = AdverseReaction

    @property
    def Contraindication(self):
        r"""禁忌
        :rtype: str
        """
        return self._Contraindication

    @Contraindication.setter
    def Contraindication(self, Contraindication):
        self._Contraindication = Contraindication

    @property
    def Attentions(self):
        r"""注意事项
        :rtype: str
        """
        return self._Attentions

    @Attentions.setter
    def Attentions(self, Attentions):
        self._Attentions = Attentions

    @property
    def Overdose(self):
        r"""药物过量
        :rtype: str
        """
        return self._Overdose

    @Overdose.setter
    def Overdose(self, Overdose):
        self._Overdose = Overdose

    @property
    def PregnantAndLactatingWomen(self):
        r"""孕妇及哺乳期妇女用药
        :rtype: str
        """
        return self._PregnantAndLactatingWomen

    @PregnantAndLactatingWomen.setter
    def PregnantAndLactatingWomen(self, PregnantAndLactatingWomen):
        self._PregnantAndLactatingWomen = PregnantAndLactatingWomen

    @property
    def ElderlyPatients(self):
        r"""老年患者用药
        :rtype: str
        """
        return self._ElderlyPatients

    @ElderlyPatients.setter
    def ElderlyPatients(self, ElderlyPatients):
        self._ElderlyPatients = ElderlyPatients

    @property
    def PediatricDrugs(self):
        r"""儿童用药
        :rtype: str
        """
        return self._PediatricDrugs

    @PediatricDrugs.setter
    def PediatricDrugs(self, PediatricDrugs):
        self._PediatricDrugs = PediatricDrugs

    @property
    def Interactions(self):
        r"""药物相互作用
        :rtype: str
        """
        return self._Interactions

    @Interactions.setter
    def Interactions(self, Interactions):
        self._Interactions = Interactions

    @property
    def ClinicalResearch(self):
        r"""临床研究
        :rtype: str
        """
        return self._ClinicalResearch

    @ClinicalResearch.setter
    def ClinicalResearch(self, ClinicalResearch):
        self._ClinicalResearch = ClinicalResearch

    @property
    def PharmacologyToxicology(self):
        r"""药理毒理
        :rtype: str
        """
        return self._PharmacologyToxicology

    @PharmacologyToxicology.setter
    def PharmacologyToxicology(self, PharmacologyToxicology):
        self._PharmacologyToxicology = PharmacologyToxicology

    @property
    def Pharmacokinetics(self):
        r"""药代动力学
        :rtype: str
        """
        return self._Pharmacokinetics

    @Pharmacokinetics.setter
    def Pharmacokinetics(self, Pharmacokinetics):
        self._Pharmacokinetics = Pharmacokinetics

    @property
    def Warning(self):
        r"""警告
        :rtype: str
        """
        return self._Warning

    @Warning.setter
    def Warning(self, Warning):
        self._Warning = Warning

    @property
    def ExpireDate(self):
        r"""有效期
        :rtype: str
        """
        return self._ExpireDate

    @ExpireDate.setter
    def ExpireDate(self, ExpireDate):
        self._ExpireDate = ExpireDate

    @property
    def Storage(self):
        r"""贮藏
        :rtype: str
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Pack(self):
        r"""包装
        :rtype: str
        """
        return self._Pack

    @Pack.setter
    def Pack(self, Pack):
        self._Pack = Pack

    @property
    def Manufacturer(self):
        r"""生产企业
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def ManufacturerAddress(self):
        r"""生产企业地址
        :rtype: str
        """
        return self._ManufacturerAddress

    @ManufacturerAddress.setter
    def ManufacturerAddress(self, ManufacturerAddress):
        self._ManufacturerAddress = ManufacturerAddress

    @property
    def ManufacturerPhone(self):
        r"""生产企业电话
        :rtype: str
        """
        return self._ManufacturerPhone

    @ManufacturerPhone.setter
    def ManufacturerPhone(self, ManufacturerPhone):
        self._ManufacturerPhone = ManufacturerPhone

    @property
    def ManufacturerEmail(self):
        r"""生产企业邮箱
        :rtype: str
        """
        return self._ManufacturerEmail

    @ManufacturerEmail.setter
    def ManufacturerEmail(self, ManufacturerEmail):
        self._ManufacturerEmail = ManufacturerEmail

    @property
    def ManufacturerWebsite(self):
        r"""生产企业网站
        :rtype: str
        """
        return self._ManufacturerWebsite

    @ManufacturerWebsite.setter
    def ManufacturerWebsite(self, ManufacturerWebsite):
        self._ManufacturerWebsite = ManufacturerWebsite

    @property
    def DocRevisionTime(self):
        r"""说明书制定和修订时间
        :rtype: str
        """
        return self._DocRevisionTime

    @DocRevisionTime.setter
    def DocRevisionTime(self, DocRevisionTime):
        self._DocRevisionTime = DocRevisionTime

    @property
    def References(self):
        r"""参考文献
        :rtype: str
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def DrugDosageForm(self):
        r"""剂型
        :rtype: str
        """
        return self._DrugDosageForm

    @DrugDosageForm.setter
    def DrugDosageForm(self, DrugDosageForm):
        self._DrugDosageForm = DrugDosageForm

    @property
    def DrugRoute(self):
        r"""给药途径
        :rtype: str
        """
        return self._DrugRoute

    @DrugRoute.setter
    def DrugRoute(self, DrugRoute):
        self._DrugRoute = DrugRoute

    @property
    def DrugBasicCode(self):
        r"""药品本位码
        :rtype: str
        """
        return self._DrugBasicCode

    @DrugBasicCode.setter
    def DrugBasicCode(self, DrugBasicCode):
        self._DrugBasicCode = DrugBasicCode

    @property
    def OctTag(self):
        r"""OTC标签
        :rtype: str
        """
        return self._OctTag

    @OctTag.setter
    def OctTag(self, OctTag):
        self._OctTag = OctTag


    def _deserialize(self, params):
        self._DrugId = params.get("DrugId")
        self._SequenceId = params.get("SequenceId")
        self._DrugHashId = params.get("DrugHashId")
        self._ImgUrl = params.get("ImgUrl")
        self._DrugName = params.get("DrugName")
        self._TradeName = params.get("TradeName")
        self._EnglishName = params.get("EnglishName")
        self._EnglishTradeName = params.get("EnglishTradeName")
        self._Pinyin = params.get("Pinyin")
        self._OtherNames = params.get("OtherNames")
        self._ChemicalName = params.get("ChemicalName")
        self._EnglishChemicalName = params.get("EnglishChemicalName")
        self._ApprovalNumber = params.get("ApprovalNumber")
        self._Property = params.get("Property")
        self._Ingredients = params.get("Ingredients")
        self._PhenotypicTrait = params.get("PhenotypicTrait")
        self._Indications = params.get("Indications")
        self._Specifications = params.get("Specifications")
        self._UsageAndDosage = params.get("UsageAndDosage")
        if params.get("RecommendedUsage") is not None:
            self._RecommendedUsage = RecommendedUsage()
            self._RecommendedUsage._deserialize(params.get("RecommendedUsage"))
        self._AdverseReaction = params.get("AdverseReaction")
        self._Contraindication = params.get("Contraindication")
        self._Attentions = params.get("Attentions")
        self._Overdose = params.get("Overdose")
        self._PregnantAndLactatingWomen = params.get("PregnantAndLactatingWomen")
        self._ElderlyPatients = params.get("ElderlyPatients")
        self._PediatricDrugs = params.get("PediatricDrugs")
        self._Interactions = params.get("Interactions")
        self._ClinicalResearch = params.get("ClinicalResearch")
        self._PharmacologyToxicology = params.get("PharmacologyToxicology")
        self._Pharmacokinetics = params.get("Pharmacokinetics")
        self._Warning = params.get("Warning")
        self._ExpireDate = params.get("ExpireDate")
        self._Storage = params.get("Storage")
        self._Pack = params.get("Pack")
        self._Manufacturer = params.get("Manufacturer")
        self._ManufacturerAddress = params.get("ManufacturerAddress")
        self._ManufacturerPhone = params.get("ManufacturerPhone")
        self._ManufacturerEmail = params.get("ManufacturerEmail")
        self._ManufacturerWebsite = params.get("ManufacturerWebsite")
        self._DocRevisionTime = params.get("DocRevisionTime")
        self._References = params.get("References")
        self._DrugDosageForm = params.get("DrugDosageForm")
        self._DrugRoute = params.get("DrugRoute")
        self._DrugBasicCode = params.get("DrugBasicCode")
        self._OctTag = params.get("OctTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartDrugInfoResponse(AbstractModel):
    r"""SmartDrugInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: 错误码
        :type Code: int
        :param _Message: 错误信息
        :type Message: str
        :param _Data: 智能用药信息
        :type Data: :class:`tencentcloud.aca.v20210323.models.SmartDrugInfoResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Code = None
        self._Message = None
        self._Data = None
        self._RequestId = None

    @property
    def Code(self):
        r"""错误码
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""错误信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Data(self):
        r"""智能用药信息
        :rtype: :class:`tencentcloud.aca.v20210323.models.SmartDrugInfoResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Data") is not None:
            self._Data = SmartDrugInfoResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class SmartPredictReqData(AbstractModel):
    r"""智能预测接口请求对象

    """

    def __init__(self):
        r"""
        :param _RequestCase: 病历和处方信息
        :type RequestCase: :class:`tencentcloud.aca.v20210323.models.RequestCase`
        :param _RequestType: 0--默认值，同时返回**疾病预测**和**用药审查**结果<br>1--仅返回**疾病预测**结果<br>2--仅返回**用药审查**结果<br>已同时激活两个模块时，可按需使用 
        :type RequestType: int
        """
        self._RequestCase = None
        self._RequestType = None

    @property
    def RequestCase(self):
        r"""病历和处方信息
        :rtype: :class:`tencentcloud.aca.v20210323.models.RequestCase`
        """
        return self._RequestCase

    @RequestCase.setter
    def RequestCase(self, RequestCase):
        self._RequestCase = RequestCase

    @property
    def RequestType(self):
        r"""0--默认值，同时返回**疾病预测**和**用药审查**结果<br>1--仅返回**疾病预测**结果<br>2--仅返回**用药审查**结果<br>已同时激活两个模块时，可按需使用 
        :rtype: int
        """
        return self._RequestType

    @RequestType.setter
    def RequestType(self, RequestType):
        self._RequestType = RequestType


    def _deserialize(self, params):
        if params.get("RequestCase") is not None:
            self._RequestCase = RequestCase()
            self._RequestCase._deserialize(params.get("RequestCase"))
        self._RequestType = params.get("RequestType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartPredictRequest(AbstractModel):
    r"""SmartPredict请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Header: 请求头
        :type Header: :class:`tencentcloud.aca.v20210323.models.CommonHeader`
        :param _Data: 请求体
        :type Data: :class:`tencentcloud.aca.v20210323.models.SmartPredictReqData`
        """
        self._Header = None
        self._Data = None

    @property
    def Header(self):
        r"""请求头
        :rtype: :class:`tencentcloud.aca.v20210323.models.CommonHeader`
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def Data(self):
        r"""请求体
        :rtype: :class:`tencentcloud.aca.v20210323.models.SmartPredictReqData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Header") is not None:
            self._Header = CommonHeader()
            self._Header._deserialize(params.get("Header"))
        if params.get("Data") is not None:
            self._Data = SmartPredictReqData()
            self._Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartPredictRespData(AbstractModel):
    r"""智能问诊响应数据

    """

    def __init__(self):
        r"""
        :param _DiagnosisInfo: 诊断辅助内容
        :type DiagnosisInfo: :class:`tencentcloud.aca.v20210323.models.DiagnosisInfo`
        :param _RationalDrugInfo: 用药风险信息
        :type RationalDrugInfo: :class:`tencentcloud.aca.v20210323.models.RationalDrugInfo`
        """
        self._DiagnosisInfo = None
        self._RationalDrugInfo = None

    @property
    def DiagnosisInfo(self):
        r"""诊断辅助内容
        :rtype: :class:`tencentcloud.aca.v20210323.models.DiagnosisInfo`
        """
        return self._DiagnosisInfo

    @DiagnosisInfo.setter
    def DiagnosisInfo(self, DiagnosisInfo):
        self._DiagnosisInfo = DiagnosisInfo

    @property
    def RationalDrugInfo(self):
        r"""用药风险信息
        :rtype: :class:`tencentcloud.aca.v20210323.models.RationalDrugInfo`
        """
        return self._RationalDrugInfo

    @RationalDrugInfo.setter
    def RationalDrugInfo(self, RationalDrugInfo):
        self._RationalDrugInfo = RationalDrugInfo


    def _deserialize(self, params):
        if params.get("DiagnosisInfo") is not None:
            self._DiagnosisInfo = DiagnosisInfo()
            self._DiagnosisInfo._deserialize(params.get("DiagnosisInfo"))
        if params.get("RationalDrugInfo") is not None:
            self._RationalDrugInfo = RationalDrugInfo()
            self._RationalDrugInfo._deserialize(params.get("RationalDrugInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartPredictResponse(AbstractModel):
    r"""SmartPredict返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: 错误码
        :type Code: int
        :param _Message: 错误信息
        :type Message: str
        :param _Data: 智能预测内容
        :type Data: :class:`tencentcloud.aca.v20210323.models.SmartPredictRespData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Code = None
        self._Message = None
        self._Data = None
        self._RequestId = None

    @property
    def Code(self):
        r"""错误码
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""错误信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Data(self):
        r"""智能预测内容
        :rtype: :class:`tencentcloud.aca.v20210323.models.SmartPredictRespData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Data") is not None:
            self._Data = SmartPredictRespData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class SuspectedDiagnosis(AbstractModel):
    r"""疑似诊断

    """

    def __init__(self):
        r"""
        :param _DiseaseName: 疾病名称
        :type DiseaseName: str
        :param _IcdCode: ICD代码
        :type IcdCode: str
        :param _Symptom: 症状
        :type Symptom: str
        :param _Physi: 体征
        :type Physi: str
        :param _Inspection: 检查
        :type Inspection: str
        :param _DiseaseGuideInfo: 疾病指南信息
        :type DiseaseGuideInfo: str
        :param _Probability: 置信度
        :type Probability: float
        """
        self._DiseaseName = None
        self._IcdCode = None
        self._Symptom = None
        self._Physi = None
        self._Inspection = None
        self._DiseaseGuideInfo = None
        self._Probability = None

    @property
    def DiseaseName(self):
        r"""疾病名称
        :rtype: str
        """
        return self._DiseaseName

    @DiseaseName.setter
    def DiseaseName(self, DiseaseName):
        self._DiseaseName = DiseaseName

    @property
    def IcdCode(self):
        r"""ICD代码
        :rtype: str
        """
        return self._IcdCode

    @IcdCode.setter
    def IcdCode(self, IcdCode):
        self._IcdCode = IcdCode

    @property
    def Symptom(self):
        r"""症状
        :rtype: str
        """
        return self._Symptom

    @Symptom.setter
    def Symptom(self, Symptom):
        self._Symptom = Symptom

    @property
    def Physi(self):
        r"""体征
        :rtype: str
        """
        return self._Physi

    @Physi.setter
    def Physi(self, Physi):
        self._Physi = Physi

    @property
    def Inspection(self):
        r"""检查
        :rtype: str
        """
        return self._Inspection

    @Inspection.setter
    def Inspection(self, Inspection):
        self._Inspection = Inspection

    @property
    def DiseaseGuideInfo(self):
        r"""疾病指南信息
        :rtype: str
        """
        return self._DiseaseGuideInfo

    @DiseaseGuideInfo.setter
    def DiseaseGuideInfo(self, DiseaseGuideInfo):
        self._DiseaseGuideInfo = DiseaseGuideInfo

    @property
    def Probability(self):
        r"""置信度
        :rtype: float
        """
        return self._Probability

    @Probability.setter
    def Probability(self, Probability):
        self._Probability = Probability


    def _deserialize(self, params):
        self._DiseaseName = params.get("DiseaseName")
        self._IcdCode = params.get("IcdCode")
        self._Symptom = params.get("Symptom")
        self._Physi = params.get("Physi")
        self._Inspection = params.get("Inspection")
        self._DiseaseGuideInfo = params.get("DiseaseGuideInfo")
        self._Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncDepartmentData(AbstractModel):
    r"""同步科室信息

    """

    def __init__(self):
        r"""
        :param _Cmd: 操作类型 1:获取科室列表  2:同步科室信息（增、改） 3:删除科室
        :type Cmd: int
        :param _List: 科室列表
        :type List: list of Department
        """
        self._Cmd = None
        self._List = None

    @property
    def Cmd(self):
        r"""操作类型 1:获取科室列表  2:同步科室信息（增、改） 3:删除科室
        :rtype: int
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def List(self):
        r"""科室列表
        :rtype: list of Department
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._Cmd = params.get("Cmd")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Department()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncDepartmentRequest(AbstractModel):
    r"""SyncDepartment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Header: 请求头
        :type Header: :class:`tencentcloud.aca.v20210323.models.CommonHeader`
        :param _Data: 同步数据
        :type Data: :class:`tencentcloud.aca.v20210323.models.SyncDepartmentData`
        """
        self._Header = None
        self._Data = None

    @property
    def Header(self):
        r"""请求头
        :rtype: :class:`tencentcloud.aca.v20210323.models.CommonHeader`
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def Data(self):
        r"""同步数据
        :rtype: :class:`tencentcloud.aca.v20210323.models.SyncDepartmentData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Header") is not None:
            self._Header = CommonHeader()
            self._Header._deserialize(params.get("Header"))
        if params.get("Data") is not None:
            self._Data = SyncDepartmentData()
            self._Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncDepartmentRespData(AbstractModel):
    r"""同步科室信息返回

    """

    def __init__(self):
        r"""
        :param _List: 科室列表
        :type List: list of Department
        """
        self._List = None

    @property
    def List(self):
        r"""科室列表
        :rtype: list of Department
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Department()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncDepartmentResponse(AbstractModel):
    r"""SyncDepartment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: 错误码
        :type Code: int
        :param _Message: 错误信息
        :type Message: str
        :param _Data: 响应数据
        :type Data: :class:`tencentcloud.aca.v20210323.models.SyncDepartmentRespData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Code = None
        self._Message = None
        self._Data = None
        self._RequestId = None

    @property
    def Code(self):
        r"""错误码
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""错误信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Data(self):
        r"""响应数据
        :rtype: :class:`tencentcloud.aca.v20210323.models.SyncDepartmentRespData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Data") is not None:
            self._Data = SyncDepartmentRespData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class SyncDictData(AbstractModel):
    r"""同步字典数据

    """

    def __init__(self):
        r"""
        :param _HospitalId: 医院ID
        :type HospitalId: str
        :param _DictType: 字典类型 1-给药频次 2-给药途径 3-科室 4-诊断
        :type DictType: int
        :param _Dicts: 字典数据
        :type Dicts: list of Dict
        """
        self._HospitalId = None
        self._DictType = None
        self._Dicts = None

    @property
    def HospitalId(self):
        r"""医院ID
        :rtype: str
        """
        return self._HospitalId

    @HospitalId.setter
    def HospitalId(self, HospitalId):
        self._HospitalId = HospitalId

    @property
    def DictType(self):
        r"""字典类型 1-给药频次 2-给药途径 3-科室 4-诊断
        :rtype: int
        """
        return self._DictType

    @DictType.setter
    def DictType(self, DictType):
        self._DictType = DictType

    @property
    def Dicts(self):
        r"""字典数据
        :rtype: list of Dict
        """
        return self._Dicts

    @Dicts.setter
    def Dicts(self, Dicts):
        self._Dicts = Dicts


    def _deserialize(self, params):
        self._HospitalId = params.get("HospitalId")
        self._DictType = params.get("DictType")
        if params.get("Dicts") is not None:
            self._Dicts = []
            for item in params.get("Dicts"):
                obj = Dict()
                obj._deserialize(item)
                self._Dicts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncStandardDictRequest(AbstractModel):
    r"""SyncStandardDict请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Header: 请求头
        :type Header: :class:`tencentcloud.aca.v20210323.models.CommonHeader`
        :param _Data: 字典数据
        :type Data: :class:`tencentcloud.aca.v20210323.models.SyncDictData`
        """
        self._Header = None
        self._Data = None

    @property
    def Header(self):
        r"""请求头
        :rtype: :class:`tencentcloud.aca.v20210323.models.CommonHeader`
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def Data(self):
        r"""字典数据
        :rtype: :class:`tencentcloud.aca.v20210323.models.SyncDictData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Header") is not None:
            self._Header = CommonHeader()
            self._Header._deserialize(params.get("Header"))
        if params.get("Data") is not None:
            self._Data = SyncDictData()
            self._Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncStandardDictResponse(AbstractModel):
    r"""SyncStandardDict返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: 错误码
        :type Code: int
        :param _Message: 错误信息
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Code = None
        self._Message = None
        self._RequestId = None

    @property
    def Code(self):
        r"""错误码
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""错误信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class TreatmentGuide(AbstractModel):
    r"""治疗方案

    """

    def __init__(self):
        r"""
        :param _DoctorDiagnosis: 医生诊断
        :type DoctorDiagnosis: str
        :param _DiseaseName: 疾病名称
        :type DiseaseName: str
        :param _TreatDetailUrl: 治疗详情链接
        :type TreatDetailUrl: str
        :param _TreatPlan: 治疗方案
        :type TreatPlan: str
        :param _TreatPrinciple: 治疗原则
        :type TreatPrinciple: str
        """
        self._DoctorDiagnosis = None
        self._DiseaseName = None
        self._TreatDetailUrl = None
        self._TreatPlan = None
        self._TreatPrinciple = None

    @property
    def DoctorDiagnosis(self):
        r"""医生诊断
        :rtype: str
        """
        return self._DoctorDiagnosis

    @DoctorDiagnosis.setter
    def DoctorDiagnosis(self, DoctorDiagnosis):
        self._DoctorDiagnosis = DoctorDiagnosis

    @property
    def DiseaseName(self):
        r"""疾病名称
        :rtype: str
        """
        return self._DiseaseName

    @DiseaseName.setter
    def DiseaseName(self, DiseaseName):
        self._DiseaseName = DiseaseName

    @property
    def TreatDetailUrl(self):
        r"""治疗详情链接
        :rtype: str
        """
        return self._TreatDetailUrl

    @TreatDetailUrl.setter
    def TreatDetailUrl(self, TreatDetailUrl):
        self._TreatDetailUrl = TreatDetailUrl

    @property
    def TreatPlan(self):
        r"""治疗方案
        :rtype: str
        """
        return self._TreatPlan

    @TreatPlan.setter
    def TreatPlan(self, TreatPlan):
        self._TreatPlan = TreatPlan

    @property
    def TreatPrinciple(self):
        r"""治疗原则
        :rtype: str
        """
        return self._TreatPrinciple

    @TreatPrinciple.setter
    def TreatPrinciple(self, TreatPrinciple):
        self._TreatPrinciple = TreatPrinciple


    def _deserialize(self, params):
        self._DoctorDiagnosis = params.get("DoctorDiagnosis")
        self._DiseaseName = params.get("DiseaseName")
        self._TreatDetailUrl = params.get("TreatDetailUrl")
        self._TreatPlan = params.get("TreatPlan")
        self._TreatPrinciple = params.get("TreatPrinciple")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadDrugData(AbstractModel):
    r"""上传药品数据

    """

    def __init__(self):
        r"""
        :param _Drugs: 药品列表
        :type Drugs: list of Drug
        """
        self._Drugs = None

    @property
    def Drugs(self):
        r"""药品列表
        :rtype: list of Drug
        """
        return self._Drugs

    @Drugs.setter
    def Drugs(self, Drugs):
        self._Drugs = Drugs


    def _deserialize(self, params):
        if params.get("Drugs") is not None:
            self._Drugs = []
            for item in params.get("Drugs"):
                obj = Drug()
                obj._deserialize(item)
                self._Drugs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadDrugsRequest(AbstractModel):
    r"""UploadDrugs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Header: 请求头数据
        :type Header: :class:`tencentcloud.aca.v20210323.models.CommonHeader`
        :param _Data: 药品上传数据
        :type Data: :class:`tencentcloud.aca.v20210323.models.UploadDrugData`
        """
        self._Header = None
        self._Data = None

    @property
    def Header(self):
        r"""请求头数据
        :rtype: :class:`tencentcloud.aca.v20210323.models.CommonHeader`
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def Data(self):
        r"""药品上传数据
        :rtype: :class:`tencentcloud.aca.v20210323.models.UploadDrugData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Header") is not None:
            self._Header = CommonHeader()
            self._Header._deserialize(params.get("Header"))
        if params.get("Data") is not None:
            self._Data = UploadDrugData()
            self._Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadDrugsResponse(AbstractModel):
    r"""UploadDrugs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: 错误码
        :type Code: int
        :param _Message: 错误信息
        :type Message: str
        :param _Data: 操作信息
        :type Data: :class:`tencentcloud.aca.v20210323.models.OperateResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Code = None
        self._Message = None
        self._Data = None
        self._RequestId = None

    @property
    def Code(self):
        r"""错误码
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""错误信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Data(self):
        r"""操作信息
        :rtype: :class:`tencentcloud.aca.v20210323.models.OperateResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Data") is not None:
            self._Data = OperateResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class VitalSignsInfo(AbstractModel):
    r"""生命体征风险

    """

    def __init__(self):
        r"""
        :param _Hit: 是否包含风险
        :type Hit: bool
        :param _Tips: 提示
        :type Tips: str
        """
        self._Hit = None
        self._Tips = None

    @property
    def Hit(self):
        r"""是否包含风险
        :rtype: bool
        """
        return self._Hit

    @Hit.setter
    def Hit(self, Hit):
        self._Hit = Hit

    @property
    def Tips(self):
        r"""提示
        :rtype: str
        """
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips


    def _deserialize(self, params):
        self._Hit = params.get("Hit")
        self._Tips = params.get("Tips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        