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


class Advice(AbstractModel):
    """建议

    """

    def __init__(self):
        """
        :param Text: 文本
注意：此字段可能返回 null，表示取不到有效值。\n        :type Text: str\n        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AspectRatio(AbstractModel):
    """纵横比

    """

    def __init__(self):
        """
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: list of int\n        :param Number: 数值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Number: str\n        :param Relation: 关系
注意：此字段可能返回 null，表示取不到有效值。\n        :type Relation: str\n        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type Src: str\n        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        """
        self.Index = None
        self.Number = None
        self.Relation = None
        self.Src = None
        self.Value = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.Number = params.get("Number")
        self.Relation = params.get("Relation")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Attribute(AbstractModel):
    """提取属性内容

    """

    def __init__(self):
        """
        :param Text: 原文文本内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Text: str\n        :param Value: 标准化提取值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        :param Index: 对应上级文本位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: int\n        """
        self.Text = None
        self.Value = None
        self.Index = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Value = params.get("Value")
        self.Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BasicInfo(AbstractModel):
    """报告基本信息

    """

    def __init__(self):
        """
        :param HospitalName: 医院名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type HospitalName: str\n        :param DepartmentName: 科室名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type DepartmentName: str\n        :param ReportName: 报告名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReportName: str\n        :param ReportTime: 报告时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReportTime: str\n        :param OutpatientNum: 门诊号
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutpatientNum: str\n        :param InHospitalNum: 住院号
注意：此字段可能返回 null，表示取不到有效值。\n        :type InHospitalNum: str\n        :param InspectionNum: 检查号
注意：此字段可能返回 null，表示取不到有效值。\n        :type InspectionNum: str\n        :param ImageNum: 影像号
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageNum: str\n        :param RadiationNum: 放射号
注意：此字段可能返回 null，表示取不到有效值。\n        :type RadiationNum: str\n        :param PathologyNum: 病理号
注意：此字段可能返回 null，表示取不到有效值。\n        :type PathologyNum: str\n        :param BedNum: 床位号
注意：此字段可能返回 null，表示取不到有效值。\n        :type BedNum: str\n        :param InHospitalTime: 入院时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type InHospitalTime: str\n        :param OutHospitalTime: 出院时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutHospitalTime: str\n        :param CureDuration: 住院治疗时长
注意：此字段可能返回 null，表示取不到有效值。\n        :type CureDuration: str\n        :param HospitalizationTimes: 住院次数
注意：此字段可能返回 null，表示取不到有效值。\n        :type HospitalizationTimes: str\n        :param InspectionTime: 送检检查时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type InspectionTime: str\n        """
        self.HospitalName = None
        self.DepartmentName = None
        self.ReportName = None
        self.ReportTime = None
        self.OutpatientNum = None
        self.InHospitalNum = None
        self.InspectionNum = None
        self.ImageNum = None
        self.RadiationNum = None
        self.PathologyNum = None
        self.BedNum = None
        self.InHospitalTime = None
        self.OutHospitalTime = None
        self.CureDuration = None
        self.HospitalizationTimes = None
        self.InspectionTime = None


    def _deserialize(self, params):
        self.HospitalName = params.get("HospitalName")
        self.DepartmentName = params.get("DepartmentName")
        self.ReportName = params.get("ReportName")
        self.ReportTime = params.get("ReportTime")
        self.OutpatientNum = params.get("OutpatientNum")
        self.InHospitalNum = params.get("InHospitalNum")
        self.InspectionNum = params.get("InspectionNum")
        self.ImageNum = params.get("ImageNum")
        self.RadiationNum = params.get("RadiationNum")
        self.PathologyNum = params.get("PathologyNum")
        self.BedNum = params.get("BedNum")
        self.InHospitalTime = params.get("InHospitalTime")
        self.OutHospitalTime = params.get("OutHospitalTime")
        self.CureDuration = params.get("CureDuration")
        self.HospitalizationTimes = params.get("HospitalizationTimes")
        self.InspectionTime = params.get("InspectionTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlockInfo(AbstractModel):
    """块信息

    """

    def __init__(self):
        """
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: list of int\n        :param Positive: 阳性
注意：此字段可能返回 null，表示取不到有效值。\n        :type Positive: str\n        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type Src: str\n        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        """
        self.Index = None
        self.Positive = None
        self.Src = None
        self.Value = None
        self.Type = None
        self.Name = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.Positive = params.get("Positive")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Case(AbstractModel):
    """医疗事例

    """

    def __init__(self):
        """
        :param Time: 时间发生时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type Time: str\n        :param Value: 事件提取值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        :param Type: 事件类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        :param Desc: 类型描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Desc: str\n        :param Text: 对应原文内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Text: str\n        """
        self.Time = None
        self.Value = None
        self.Type = None
        self.Desc = None
        self.Text = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        self.Type = params.get("Type")
        self.Desc = params.get("Desc")
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaseHistory(AbstractModel):
    """病历资料

    """

    def __init__(self):
        """
        :param Treatment: 诊治信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Treatment: :class:`tencentcloud.mrs.v20200910.models.Treatment`\n        :param HealthHistory: 健康史信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type HealthHistory: :class:`tencentcloud.mrs.v20200910.models.HealthHistory`\n        :param CaseHistoryList: 病例时间轴\n        :type CaseHistoryList: list of Case\n        """
        self.Treatment = None
        self.HealthHistory = None
        self.CaseHistoryList = None


    def _deserialize(self, params):
        if params.get("Treatment") is not None:
            self.Treatment = Treatment()
            self.Treatment._deserialize(params.get("Treatment"))
        if params.get("HealthHistory") is not None:
            self.HealthHistory = HealthHistory()
            self.HealthHistory._deserialize(params.get("HealthHistory"))
        if params.get("CaseHistoryList") is not None:
            self.CaseHistoryList = []
            for item in params.get("CaseHistoryList"):
                obj = Case()
                obj._deserialize(item)
                self.CaseHistoryList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Check(AbstractModel):
    """检查报告单

    """

    def __init__(self):
        """
        :param Desc: 描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Desc: :class:`tencentcloud.mrs.v20200910.models.Desc`\n        :param Summary: 结论
注意：此字段可能返回 null，表示取不到有效值。\n        :type Summary: :class:`tencentcloud.mrs.v20200910.models.Summary`\n        """
        self.Desc = None
        self.Summary = None


    def _deserialize(self, params):
        if params.get("Desc") is not None:
            self.Desc = Desc()
            self.Desc._deserialize(params.get("Desc"))
        if params.get("Summary") is not None:
            self.Summary = Summary()
            self.Summary._deserialize(params.get("Summary"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Conclusion(AbstractModel):
    """检查报告结论，常见于病理检查报告

    """

    def __init__(self):
        """
        :param Text: 原文文本内容\n        :type Text: str\n        :param SymptomList: 病症列表\n        :type SymptomList: list of Symptom\n        """
        self.Text = None
        self.SymptomList = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        if params.get("SymptomList") is not None:
            self.SymptomList = []
            for item in params.get("SymptomList"):
                obj = Symptom()
                obj._deserialize(item)
                self.SymptomList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Desc(AbstractModel):
    """描述

    """

    def __init__(self):
        """
        :param Text: 描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Text: str\n        :param Organ: 器官
注意：此字段可能返回 null，表示取不到有效值。\n        :type Organ: list of Organ\n        :param Tuber: 结节
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tuber: list of TuberInfo\n        """
        self.Text = None
        self.Organ = None
        self.Tuber = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        if params.get("Organ") is not None:
            self.Organ = []
            for item in params.get("Organ"):
                obj = Organ()
                obj._deserialize(item)
                self.Organ.append(obj)
        if params.get("Tuber") is not None:
            self.Tuber = []
            for item in params.get("Tuber"):
                obj = TuberInfo()
                obj._deserialize(item)
                self.Tuber.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagCert(AbstractModel):
    """诊断证明

    """

    def __init__(self):
        """
        :param Advice: 建议
注意：此字段可能返回 null，表示取不到有效值。\n        :type Advice: :class:`tencentcloud.mrs.v20200910.models.Advice`\n        :param Diagnosis: 诊断
注意：此字段可能返回 null，表示取不到有效值。\n        :type Diagnosis: list of DiagCertItem\n        """
        self.Advice = None
        self.Diagnosis = None


    def _deserialize(self, params):
        if params.get("Advice") is not None:
            self.Advice = Advice()
            self.Advice._deserialize(params.get("Advice"))
        if params.get("Diagnosis") is not None:
            self.Diagnosis = []
            for item in params.get("Diagnosis"):
                obj = DiagCertItem()
                obj._deserialize(item)
                self.Diagnosis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagCertItem(AbstractModel):
    """诊断证明项

    """

    def __init__(self):
        """
        :param Text: 文本
注意：此字段可能返回 null，表示取不到有效值。\n        :type Text: str\n        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: list of str\n        """
        self.Text = None
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DischargeDiagnosis(AbstractModel):
    """出入院诊断

    """

    def __init__(self):
        """
        :param TableIndex: 表格位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type TableIndex: int\n        :param OutDiagnosis: 出院诊断
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutDiagnosis: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param DiseaseCode: 疾病编码
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiseaseCode: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param InStatus: 入院情况
注意：此字段可能返回 null，表示取不到有效值。\n        :type InStatus: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param OutStatus: 出院情况
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutStatus: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        """
        self.TableIndex = None
        self.OutDiagnosis = None
        self.DiseaseCode = None
        self.InStatus = None
        self.OutStatus = None


    def _deserialize(self, params):
        self.TableIndex = params.get("TableIndex")
        if params.get("OutDiagnosis") is not None:
            self.OutDiagnosis = BlockInfo()
            self.OutDiagnosis._deserialize(params.get("OutDiagnosis"))
        if params.get("DiseaseCode") is not None:
            self.DiseaseCode = BlockInfo()
            self.DiseaseCode._deserialize(params.get("DiseaseCode"))
        if params.get("InStatus") is not None:
            self.InStatus = BlockInfo()
            self.InStatus._deserialize(params.get("InStatus"))
        if params.get("OutStatus") is not None:
            self.OutStatus = BlockInfo()
            self.OutStatus._deserialize(params.get("OutStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiseaseHistory(AbstractModel):
    """病史

    """

    def __init__(self):
        """
        :param Allergy: 过敏史
注意：此字段可能返回 null，表示取不到有效值。\n        :type Allergy: str\n        :param Infect: 传染疾病史
注意：此字段可能返回 null，表示取不到有效值。\n        :type Infect: str\n        :param MainDisease: 主要病史
注意：此字段可能返回 null，表示取不到有效值。\n        :type MainDisease: str\n        :param Operation: 手术外伤史
注意：此字段可能返回 null，表示取不到有效值。\n        :type Operation: str\n        :param Transfusion: 输血史
注意：此字段可能返回 null，表示取不到有效值。\n        :type Transfusion: str\n        :param Disease: 疾病史
注意：此字段可能返回 null，表示取不到有效值。\n        :type Disease: str\n        """
        self.Allergy = None
        self.Infect = None
        self.MainDisease = None
        self.Operation = None
        self.Transfusion = None
        self.Disease = None


    def _deserialize(self, params):
        self.Allergy = params.get("Allergy")
        self.Infect = params.get("Infect")
        self.MainDisease = params.get("MainDisease")
        self.Operation = params.get("Operation")
        self.Transfusion = params.get("Transfusion")
        self.Disease = params.get("Disease")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiseaseMedicalHistory(AbstractModel):
    """疾病史

    """

    def __init__(self):
        """
        :param MainDiseaseHistory: 主病史
注意：此字段可能返回 null，表示取不到有效值。\n        :type MainDiseaseHistory: str\n        :param AllergyHistory: 过敏史
注意：此字段可能返回 null，表示取不到有效值。\n        :type AllergyHistory: str\n        :param InfectHistory: 传染疾病史
注意：此字段可能返回 null，表示取不到有效值。\n        :type InfectHistory: str\n        :param OperationHistory: 手术史
注意：此字段可能返回 null，表示取不到有效值。\n        :type OperationHistory: str\n        :param TransfusionHistory: 输血史
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransfusionHistory: str\n        """
        self.MainDiseaseHistory = None
        self.AllergyHistory = None
        self.InfectHistory = None
        self.OperationHistory = None
        self.TransfusionHistory = None


    def _deserialize(self, params):
        self.MainDiseaseHistory = params.get("MainDiseaseHistory")
        self.AllergyHistory = params.get("AllergyHistory")
        self.InfectHistory = params.get("InfectHistory")
        self.OperationHistory = params.get("OperationHistory")
        self.TransfusionHistory = params.get("TransfusionHistory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Elastic(AbstractModel):
    """弹性质地

    """

    def __init__(self):
        """
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: list of int\n        :param Score: 分数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Score: str\n        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type Src: str\n        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        """
        self.Index = None
        self.Score = None
        self.Src = None
        self.Value = None
        self.Name = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.Score = params.get("Score")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FamilyHistory(AbstractModel):
    """家族史

    """

    def __init__(self):
        """
        :param RelativeMember: 家族成员
注意：此字段可能返回 null，表示取不到有效值。\n        :type RelativeMember: str\n        :param RelativeCancer: 家族肿瘤史
注意：此字段可能返回 null，表示取不到有效值。\n        :type RelativeCancer: str\n        :param Genetic: 家族遗传史
注意：此字段可能返回 null，表示取不到有效值。\n        :type Genetic: str\n        """
        self.RelativeMember = None
        self.RelativeCancer = None
        self.Genetic = None


    def _deserialize(self, params):
        self.RelativeMember = params.get("RelativeMember")
        self.RelativeCancer = params.get("RelativeCancer")
        self.Genetic = params.get("Genetic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FamilyMedicalHistory(AbstractModel):
    """家族疾病史

    """

    def __init__(self):
        """
        :param RelativeHistory: 家族成员史
注意：此字段可能返回 null，表示取不到有效值。\n        :type RelativeHistory: str\n        :param RelativeCancerHistory: 家族肿瘤史
注意：此字段可能返回 null，表示取不到有效值。\n        :type RelativeCancerHistory: str\n        :param GeneticHistory: 家族遗传史
注意：此字段可能返回 null，表示取不到有效值。\n        :type GeneticHistory: str\n        """
        self.RelativeHistory = None
        self.RelativeCancerHistory = None
        self.GeneticHistory = None


    def _deserialize(self, params):
        self.RelativeHistory = params.get("RelativeHistory")
        self.RelativeCancerHistory = params.get("RelativeCancerHistory")
        self.GeneticHistory = params.get("GeneticHistory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Finding(AbstractModel):
    """检查所见内容，常见于病理，检查报告

    """

    def __init__(self):
        """
        :param Text: 原文文本内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Text: str\n        :param TuberList: 肿瘤结节列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type TuberList: list of Tuber\n        """
        self.Text = None
        self.TuberList = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        if params.get("TuberList") is not None:
            self.TuberList = []
            for item in params.get("TuberList"):
                obj = Tuber()
                obj._deserialize(item)
                self.TuberList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirstPage(AbstractModel):
    """病案首页

    """

    def __init__(self):
        """
        :param DischargeDiagnosis: 出入院诊断
注意：此字段可能返回 null，表示取不到有效值。\n        :type DischargeDiagnosis: list of DischargeDiagnosis\n        :param PathologicalDiagnosis: 病理诊断
注意：此字段可能返回 null，表示取不到有效值。\n        :type PathologicalDiagnosis: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param ClinicalDiagnosis: 临床诊断
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClinicalDiagnosis: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        """
        self.DischargeDiagnosis = None
        self.PathologicalDiagnosis = None
        self.ClinicalDiagnosis = None


    def _deserialize(self, params):
        if params.get("DischargeDiagnosis") is not None:
            self.DischargeDiagnosis = []
            for item in params.get("DischargeDiagnosis"):
                obj = DischargeDiagnosis()
                obj._deserialize(item)
                self.DischargeDiagnosis.append(obj)
        if params.get("PathologicalDiagnosis") is not None:
            self.PathologicalDiagnosis = BlockInfo()
            self.PathologicalDiagnosis._deserialize(params.get("PathologicalDiagnosis"))
        if params.get("ClinicalDiagnosis") is not None:
            self.ClinicalDiagnosis = BlockInfo()
            self.ClinicalDiagnosis._deserialize(params.get("ClinicalDiagnosis"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HandleParam(AbstractModel):
    """图片处理参数

    """

    def __init__(self):
        """
        :param OcrEngineType: ocr引擎\n        :type OcrEngineType: int\n        :param IsReturnText: 是否返回分行文本内容\n        :type IsReturnText: bool\n        :param RotateTheAngle: 顺时针旋转角度\n        :type RotateTheAngle: float\n        :param AutoFitDirection: 自动适配方向,仅支持优图引擎\n        :type AutoFitDirection: bool\n        :param AutoOptimizeCoordinate: 坐标优化\n        :type AutoOptimizeCoordinate: bool\n        :param IsScale: 是否开启图片压缩，开启时imageOriginalSize必须正确填写\n        :type IsScale: bool\n        :param ImageOriginalSize: 原始图片大小(单位byes),用来判断该图片是否需要压缩\n        :type ImageOriginalSize: int\n        :param ScaleTargetSize: 采用后台默认值(2048Kb)\n        :type ScaleTargetSize: int\n        """
        self.OcrEngineType = None
        self.IsReturnText = None
        self.RotateTheAngle = None
        self.AutoFitDirection = None
        self.AutoOptimizeCoordinate = None
        self.IsScale = None
        self.ImageOriginalSize = None
        self.ScaleTargetSize = None


    def _deserialize(self, params):
        self.OcrEngineType = params.get("OcrEngineType")
        self.IsReturnText = params.get("IsReturnText")
        self.RotateTheAngle = params.get("RotateTheAngle")
        self.AutoFitDirection = params.get("AutoFitDirection")
        self.AutoOptimizeCoordinate = params.get("AutoOptimizeCoordinate")
        self.IsScale = params.get("IsScale")
        self.ImageOriginalSize = params.get("ImageOriginalSize")
        self.ScaleTargetSize = params.get("ScaleTargetSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthHistory(AbstractModel):
    """健康史信息

    """

    def __init__(self):
        """
        :param DiseaseHistory: 疾病史
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiseaseHistory: :class:`tencentcloud.mrs.v20200910.models.DiseaseHistory`\n        :param FamilyHistory: 家族史
注意：此字段可能返回 null，表示取不到有效值。\n        :type FamilyHistory: :class:`tencentcloud.mrs.v20200910.models.FamilyHistory`\n        :param MarryHistory: 婚育史
注意：此字段可能返回 null，表示取不到有效值。\n        :type MarryHistory: :class:`tencentcloud.mrs.v20200910.models.MarryHistory`\n        :param PersonalHistory: 个人史
注意：此字段可能返回 null，表示取不到有效值。\n        :type PersonalHistory: :class:`tencentcloud.mrs.v20200910.models.PersonalHistory`\n        :param MenstrualHistory: 月经史
注意：此字段可能返回 null，表示取不到有效值。\n        :type MenstrualHistory: :class:`tencentcloud.mrs.v20200910.models.MenstrualHistory`\n        """
        self.DiseaseHistory = None
        self.FamilyHistory = None
        self.MarryHistory = None
        self.PersonalHistory = None
        self.MenstrualHistory = None


    def _deserialize(self, params):
        if params.get("DiseaseHistory") is not None:
            self.DiseaseHistory = DiseaseHistory()
            self.DiseaseHistory._deserialize(params.get("DiseaseHistory"))
        if params.get("FamilyHistory") is not None:
            self.FamilyHistory = FamilyHistory()
            self.FamilyHistory._deserialize(params.get("FamilyHistory"))
        if params.get("MarryHistory") is not None:
            self.MarryHistory = MarryHistory()
            self.MarryHistory._deserialize(params.get("MarryHistory"))
        if params.get("PersonalHistory") is not None:
            self.PersonalHistory = PersonalHistory()
            self.PersonalHistory._deserialize(params.get("PersonalHistory"))
        if params.get("MenstrualHistory") is not None:
            self.MenstrualHistory = MenstrualHistory()
            self.MenstrualHistory._deserialize(params.get("MenstrualHistory"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HistologyLevel(AbstractModel):
    """组织学等级

    """

    def __init__(self):
        """
        :param Grade: 等级
注意：此字段可能返回 null，表示取不到有效值。\n        :type Grade: str\n        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: list of int\n        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type Src: str\n        """
        self.Grade = None
        self.Index = None
        self.Src = None


    def _deserialize(self, params):
        self.Grade = params.get("Grade")
        self.Index = params.get("Index")
        self.Src = params.get("Src")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HistologyType(AbstractModel):
    """组织学类型

    """

    def __init__(self):
        """
        :param Infiltration: 浸润
注意：此字段可能返回 null，表示取不到有效值。\n        :type Infiltration: str\n        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: list of int\n        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type Src: str\n        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        """
        self.Infiltration = None
        self.Index = None
        self.Src = None
        self.Type = None


    def _deserialize(self, params):
        self.Infiltration = params.get("Infiltration")
        self.Index = params.get("Index")
        self.Src = params.get("Src")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hospitalization(AbstractModel):
    """出入院信息

    """

    def __init__(self):
        """
        :param AdmissionTime: 入院时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type AdmissionTime: str\n        :param DischargeTime: 出院时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type DischargeTime: str\n        :param AdmissionDays: 住院天数
注意：此字段可能返回 null，表示取不到有效值。\n        :type AdmissionDays: str\n        :param AdmissionDignosis: 入院诊断
注意：此字段可能返回 null，表示取不到有效值。\n        :type AdmissionDignosis: str\n        :param AdmissionCondition: 入院情况
注意：此字段可能返回 null，表示取不到有效值。\n        :type AdmissionCondition: str\n        :param DiagnosisTreatment: 诊疗经过
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiagnosisTreatment: str\n        :param DischargeDiagnosis: 出院诊断
注意：此字段可能返回 null，表示取不到有效值。\n        :type DischargeDiagnosis: str\n        :param DischargeInstruction: 出院医嘱
注意：此字段可能返回 null，表示取不到有效值。\n        :type DischargeInstruction: str\n        """
        self.AdmissionTime = None
        self.DischargeTime = None
        self.AdmissionDays = None
        self.AdmissionDignosis = None
        self.AdmissionCondition = None
        self.DiagnosisTreatment = None
        self.DischargeDiagnosis = None
        self.DischargeInstruction = None


    def _deserialize(self, params):
        self.AdmissionTime = params.get("AdmissionTime")
        self.DischargeTime = params.get("DischargeTime")
        self.AdmissionDays = params.get("AdmissionDays")
        self.AdmissionDignosis = params.get("AdmissionDignosis")
        self.AdmissionCondition = params.get("AdmissionCondition")
        self.DiagnosisTreatment = params.get("DiagnosisTreatment")
        self.DischargeDiagnosis = params.get("DischargeDiagnosis")
        self.DischargeInstruction = params.get("DischargeInstruction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IHC(AbstractModel):
    """免疫组化项目

    """

    def __init__(self):
        """
        :param Index: 索引位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: list of int\n        :param Text: 原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type Text: str\n        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Grade: 等级
注意：此字段可能返回 null，表示取不到有效值。\n        :type Grade: str\n        :param Percent: 百分比
注意：此字段可能返回 null，表示取不到有效值。\n        :type Percent: str\n        :param Positive: 阴阳性
注意：此字段可能返回 null，表示取不到有效值。\n        :type Positive: str\n        """
        self.Index = None
        self.Text = None
        self.Name = None
        self.Grade = None
        self.Percent = None
        self.Positive = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.Text = params.get("Text")
        self.Name = params.get("Name")
        self.Grade = params.get("Grade")
        self.Percent = params.get("Percent")
        self.Positive = params.get("Positive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IHCInfo(AbstractModel):
    """Ihc信息

    """

    def __init__(self):
        """
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: list of int\n        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type Src: str\n        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Value: 值\n        :type Value: :class:`tencentcloud.mrs.v20200910.models.Value`\n        """
        self.Index = None
        self.Src = None
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.Src = params.get("Src")
        self.Name = params.get("Name")
        if params.get("Value") is not None:
            self.Value = Value()
            self.Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageInfo(AbstractModel):
    """图片信息

    """

    def __init__(self):
        """
        :param Id: 图片id\n        :type Id: int\n        :param Url: 图片url\n        :type Url: str\n        :param Base64: 图片base64编码\n        :type Base64: str\n        """
        self.Id = None
        self.Url = None
        self.Base64 = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Url = params.get("Url")
        self.Base64 = params.get("Base64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageReport(AbstractModel):
    """报告内容

    """

    def __init__(self):
        """
        :param ImageText: 报告文本信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageText: :class:`tencentcloud.mrs.v20200910.models.ImageText`\n        :param KindSet: 报告类别信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type KindSet: list of KindItem\n        :param BasicInfo: 基本信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type BasicInfo: :class:`tencentcloud.mrs.v20200910.models.BasicInfo`\n        :param PersonalInfo: 个人隐私信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type PersonalInfo: :class:`tencentcloud.mrs.v20200910.models.PersonalInfo`\n        :param TestList: 检验指标内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type TestList: list of TestItem\n        :param Inspection: 检查报告内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Inspection: :class:`tencentcloud.mrs.v20200910.models.Inspection`\n        :param CaseHistory: 病历资料内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type CaseHistory: :class:`tencentcloud.mrs.v20200910.models.CaseHistory`\n        :param Pathology: 病理报告内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Pathology: :class:`tencentcloud.mrs.v20200910.models.Pathology`\n        """
        self.ImageText = None
        self.KindSet = None
        self.BasicInfo = None
        self.PersonalInfo = None
        self.TestList = None
        self.Inspection = None
        self.CaseHistory = None
        self.Pathology = None


    def _deserialize(self, params):
        if params.get("ImageText") is not None:
            self.ImageText = ImageText()
            self.ImageText._deserialize(params.get("ImageText"))
        if params.get("KindSet") is not None:
            self.KindSet = []
            for item in params.get("KindSet"):
                obj = KindItem()
                obj._deserialize(item)
                self.KindSet.append(obj)
        if params.get("BasicInfo") is not None:
            self.BasicInfo = BasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("PersonalInfo") is not None:
            self.PersonalInfo = PersonalInfo()
            self.PersonalInfo._deserialize(params.get("PersonalInfo"))
        if params.get("TestList") is not None:
            self.TestList = []
            for item in params.get("TestList"):
                obj = TestItem()
                obj._deserialize(item)
                self.TestList.append(obj)
        if params.get("Inspection") is not None:
            self.Inspection = Inspection()
            self.Inspection._deserialize(params.get("Inspection"))
        if params.get("CaseHistory") is not None:
            self.CaseHistory = CaseHistory()
            self.CaseHistory._deserialize(params.get("CaseHistory"))
        if params.get("Pathology") is not None:
            self.Pathology = Pathology()
            self.Pathology._deserialize(params.get("Pathology"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageText(AbstractModel):
    """报告图片信息

    """

    def __init__(self):
        """
        :param Confidence: 文字内容可信度，0-100评分
注意：此字段可能返回 null，表示取不到有效值。\n        :type Confidence: int\n        :param Text: 图片文本内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Text: str\n        :param RotateAngle: 文本旋转角度
注意：此字段可能返回 null，表示取不到有效值。\n        :type RotateAngle: float\n        """
        self.Confidence = None
        self.Text = None
        self.RotateAngle = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Text = params.get("Text")
        self.RotateAngle = params.get("RotateAngle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageToClassRequest(AbstractModel):
    """ImageToClass请求参数结构体

    """

    def __init__(self):
        """
        :param ImageInfoList: 图片列表，允许传入多张图片，支持传入图片的url或base64编码\n        :type ImageInfoList: list of ImageInfo\n        :param HandleParam: 图片处理参数\n        :type HandleParam: :class:`tencentcloud.mrs.v20200910.models.HandleParam`\n        :param Type: 图片类型，目前支持11（检验报告），12（检查报告），15（病理报告），218（诊断证明）。\n        :type Type: int\n        """
        self.ImageInfoList = None
        self.HandleParam = None
        self.Type = None


    def _deserialize(self, params):
        if params.get("ImageInfoList") is not None:
            self.ImageInfoList = []
            for item in params.get("ImageInfoList"):
                obj = ImageInfo()
                obj._deserialize(item)
                self.ImageInfoList.append(obj)
        if params.get("HandleParam") is not None:
            self.HandleParam = HandleParam()
            self.HandleParam._deserialize(params.get("HandleParam"))
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageToClassResponse(AbstractModel):
    """ImageToClass返回参数结构体

    """

    def __init__(self):
        """
        :param TextTypeList: 分类结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type TextTypeList: list of TextType\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TextTypeList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextTypeList") is not None:
            self.TextTypeList = []
            for item in params.get("TextTypeList"):
                obj = TextType()
                obj._deserialize(item)
                self.TextTypeList.append(obj)
        self.RequestId = params.get("RequestId")


class ImageToObjectRequest(AbstractModel):
    """ImageToObject请求参数结构体

    """

    def __init__(self):
        """
        :param ImageInfoList: 图片列表，允许传入多张图片，支持传入图片的url或base64编码\n        :type ImageInfoList: list of ImageInfo\n        :param HandleParam: 图片处理参数\n        :type HandleParam: :class:`tencentcloud.mrs.v20200910.models.HandleParam`\n        :param Type: 报告类型，目前支持11（检验报告），12（检查报告），15（病理报告），28（出院报告），29（入院报告），210（门诊病历），212（手术记录），218（诊断证明）。如果不清楚报告类型，可以使用分类引擎，该字段传0（同时IsUsedClassify字段必须为True，否则无法输出结果）\n        :type Type: int\n        :param IsUsedClassify: 是否使用分类引擎，当不确定报告类型时，可以使用收费的报告分类引擎服务。若该字段为 False，则 Type 字段不能为 0，否则无法输出结果。
注意：当 IsUsedClassify 为True 时，表示使用收费的报告分类服务，将会产生额外的费用，具体收费标准参见 [购买指南的产品价格](https://cloud.tencent.com/document/product/1314/54264)。\n        :type IsUsedClassify: bool\n        """
        self.ImageInfoList = None
        self.HandleParam = None
        self.Type = None
        self.IsUsedClassify = None


    def _deserialize(self, params):
        if params.get("ImageInfoList") is not None:
            self.ImageInfoList = []
            for item in params.get("ImageInfoList"):
                obj = ImageInfo()
                obj._deserialize(item)
                self.ImageInfoList.append(obj)
        if params.get("HandleParam") is not None:
            self.HandleParam = HandleParam()
            self.HandleParam._deserialize(params.get("HandleParam"))
        self.Type = params.get("Type")
        self.IsUsedClassify = params.get("IsUsedClassify")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageToObjectResponse(AbstractModel):
    """ImageToObject返回参数结构体

    """

    def __init__(self):
        """
        :param Template: 报告结构化结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Template: :class:`tencentcloud.mrs.v20200910.models.Template`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = Template()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class Indicator(AbstractModel):
    """检验报告

    """

    def __init__(self):
        """
        :param Indicators: 检验指标项
注意：此字段可能返回 null，表示取不到有效值。\n        :type Indicators: list of IndicatorItem\n        """
        self.Indicators = None


    def _deserialize(self, params):
        if params.get("Indicators") is not None:
            self.Indicators = []
            for item in params.get("Indicators"):
                obj = IndicatorItem()
                obj._deserialize(item)
                self.Indicators.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndicatorItem(AbstractModel):
    """检验指标项

    """

    def __init__(self):
        """
        :param Code: 英文缩写
注意：此字段可能返回 null，表示取不到有效值。\n        :type Code: str\n        :param Scode: 标准缩写
注意：此字段可能返回 null，表示取不到有效值。\n        :type Scode: str\n        :param Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Sname: 标准名
注意：此字段可能返回 null，表示取不到有效值。\n        :type Sname: str\n        :param Result: 结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。\n        :type Unit: str\n        :param Range: 参考范围
注意：此字段可能返回 null，表示取不到有效值。\n        :type Range: str\n        :param Arrow: 上下箭头
注意：此字段可能返回 null，表示取不到有效值。\n        :type Arrow: str\n        :param Normal: 是否正常
注意：此字段可能返回 null，表示取不到有效值。\n        :type Normal: bool\n        :param ItemString: 项目原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type ItemString: str\n        """
        self.Code = None
        self.Scode = None
        self.Name = None
        self.Sname = None
        self.Result = None
        self.Unit = None
        self.Range = None
        self.Arrow = None
        self.Normal = None
        self.ItemString = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Scode = params.get("Scode")
        self.Name = params.get("Name")
        self.Sname = params.get("Sname")
        self.Result = params.get("Result")
        self.Unit = params.get("Unit")
        self.Range = params.get("Range")
        self.Arrow = params.get("Arrow")
        self.Normal = params.get("Normal")
        self.ItemString = params.get("ItemString")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Inspection(AbstractModel):
    """检查报告内容

    """

    def __init__(self):
        """
        :param Finding: 检查所见
注意：此字段可能返回 null，表示取不到有效值。\n        :type Finding: :class:`tencentcloud.mrs.v20200910.models.Finding`\n        :param Conclusion: 检查结论
注意：此字段可能返回 null，表示取不到有效值。\n        :type Conclusion: :class:`tencentcloud.mrs.v20200910.models.Conclusion`\n        """
        self.Finding = None
        self.Conclusion = None


    def _deserialize(self, params):
        if params.get("Finding") is not None:
            self.Finding = Finding()
            self.Finding._deserialize(params.get("Finding"))
        if params.get("Conclusion") is not None:
            self.Conclusion = Conclusion()
            self.Conclusion._deserialize(params.get("Conclusion"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Invas(AbstractModel):
    """侵犯扩散

    """

    def __init__(self):
        """
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: list of int\n        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。\n        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`\n        :param Positive: 阳性
注意：此字段可能返回 null，表示取不到有效值。\n        :type Positive: str\n        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type Src: str\n        """
        self.Index = None
        self.Part = None
        self.Positive = None
        self.Src = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        if params.get("Part") is not None:
            self.Part = Part()
            self.Part._deserialize(params.get("Part"))
        self.Positive = params.get("Positive")
        self.Src = params.get("Src")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Invasive(AbstractModel):
    """侵犯扩散

    """

    def __init__(self):
        """
        :param Index: 索引
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: list of int\n        :param Text: 原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type Text: str\n        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。\n        :type Part: str\n        :param Positive: 阴阳性\n        :type Positive: str\n        """
        self.Index = None
        self.Text = None
        self.Part = None
        self.Positive = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.Text = params.get("Text")
        self.Part = params.get("Part")
        self.Positive = params.get("Positive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KindItem(AbstractModel):
    """类型描述

    """

    def __init__(self):
        """
        :param Level: 等级，分为1，2，3级别，类型逐级细分\n        :type Level: int\n        :param ID: 类型编号，对应唯一的类型编号\n        :type ID: int\n        :param Name: 类型名称\n        :type Name: str\n        """
        self.Level = None
        self.ID = None
        self.Name = None


    def _deserialize(self, params):
        self.Level = params.get("Level")
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Lymph(AbstractModel):
    """淋巴

    """

    def __init__(self):
        """
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type Src: str\n        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: list of int\n        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。\n        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`\n        :param Total: 总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        :param TransferNum: 转移数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransferNum: int\n        """
        self.Src = None
        self.Index = None
        self.Part = None
        self.Total = None
        self.TransferNum = None


    def _deserialize(self, params):
        self.Src = params.get("Src")
        self.Index = params.get("Index")
        if params.get("Part") is not None:
            self.Part = Part()
            self.Part._deserialize(params.get("Part"))
        self.Total = params.get("Total")
        self.TransferNum = params.get("TransferNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MarryHistory(AbstractModel):
    """婚育史

    """

    def __init__(self):
        """
        :param Marriage: 结婚史
注意：此字段可能返回 null，表示取不到有效值。\n        :type Marriage: str\n        :param Fertility: 生育史
注意：此字段可能返回 null，表示取不到有效值。\n        :type Fertility: str\n        """
        self.Marriage = None
        self.Fertility = None


    def _deserialize(self, params):
        self.Marriage = params.get("Marriage")
        self.Fertility = params.get("Fertility")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MedDoc(AbstractModel):
    """医学资料

    """

    def __init__(self):
        """
        :param Advice: 建议
注意：此字段可能返回 null，表示取不到有效值。\n        :type Advice: :class:`tencentcloud.mrs.v20200910.models.Advice`\n        :param Diagnosis: 诊断结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Diagnosis: list of DiagCertItem\n        :param DiseaseMedicalHistory: 疾病史
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiseaseMedicalHistory: :class:`tencentcloud.mrs.v20200910.models.DiseaseMedicalHistory`\n        :param PersonalMedicalHistory: 个人史\n        :type PersonalMedicalHistory: :class:`tencentcloud.mrs.v20200910.models.PersonalMedicalHistory`\n        :param ObstericalMedicalHistory: 婚孕史\n        :type ObstericalMedicalHistory: :class:`tencentcloud.mrs.v20200910.models.ObstericalMedicalHistory`\n        :param FamilyMedicalHistory: 家族史\n        :type FamilyMedicalHistory: :class:`tencentcloud.mrs.v20200910.models.FamilyMedicalHistory`\n        :param MenstrualMedicalHistory: 月经史\n        :type MenstrualMedicalHistory: :class:`tencentcloud.mrs.v20200910.models.MenstrualMedicalHistory`\n        :param TreatmentRecord: 诊疗记录\n        :type TreatmentRecord: :class:`tencentcloud.mrs.v20200910.models.TreatmentRecord`\n        """
        self.Advice = None
        self.Diagnosis = None
        self.DiseaseMedicalHistory = None
        self.PersonalMedicalHistory = None
        self.ObstericalMedicalHistory = None
        self.FamilyMedicalHistory = None
        self.MenstrualMedicalHistory = None
        self.TreatmentRecord = None


    def _deserialize(self, params):
        if params.get("Advice") is not None:
            self.Advice = Advice()
            self.Advice._deserialize(params.get("Advice"))
        if params.get("Diagnosis") is not None:
            self.Diagnosis = []
            for item in params.get("Diagnosis"):
                obj = DiagCertItem()
                obj._deserialize(item)
                self.Diagnosis.append(obj)
        if params.get("DiseaseMedicalHistory") is not None:
            self.DiseaseMedicalHistory = DiseaseMedicalHistory()
            self.DiseaseMedicalHistory._deserialize(params.get("DiseaseMedicalHistory"))
        if params.get("PersonalMedicalHistory") is not None:
            self.PersonalMedicalHistory = PersonalMedicalHistory()
            self.PersonalMedicalHistory._deserialize(params.get("PersonalMedicalHistory"))
        if params.get("ObstericalMedicalHistory") is not None:
            self.ObstericalMedicalHistory = ObstericalMedicalHistory()
            self.ObstericalMedicalHistory._deserialize(params.get("ObstericalMedicalHistory"))
        if params.get("FamilyMedicalHistory") is not None:
            self.FamilyMedicalHistory = FamilyMedicalHistory()
            self.FamilyMedicalHistory._deserialize(params.get("FamilyMedicalHistory"))
        if params.get("MenstrualMedicalHistory") is not None:
            self.MenstrualMedicalHistory = MenstrualMedicalHistory()
            self.MenstrualMedicalHistory._deserialize(params.get("MenstrualMedicalHistory"))
        if params.get("TreatmentRecord") is not None:
            self.TreatmentRecord = TreatmentRecord()
            self.TreatmentRecord._deserialize(params.get("TreatmentRecord"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MedicalRecordInfo(AbstractModel):
    """门诊病历信息

    """

    def __init__(self):
        """
        :param DiagnosisTime: 就诊日期
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiagnosisTime: str\n        :param DiagnosisDepartmentName: 就诊科室
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiagnosisDepartmentName: str\n        :param DiagnosisDoctorName: 就诊医生
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiagnosisDoctorName: str\n        :param ClinicalDiagnosis: 临床诊断
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClinicalDiagnosis: str\n        :param MainNarration: 主述
注意：此字段可能返回 null，表示取不到有效值。\n        :type MainNarration: str\n        :param PhysicalExamination: 体格检查
注意：此字段可能返回 null，表示取不到有效值。\n        :type PhysicalExamination: str\n        :param InspectionFindings: 检查结论
注意：此字段可能返回 null，表示取不到有效值。\n        :type InspectionFindings: str\n        :param TreatmentOpinion: 治疗意见
注意：此字段可能返回 null，表示取不到有效值。\n        :type TreatmentOpinion: str\n        """
        self.DiagnosisTime = None
        self.DiagnosisDepartmentName = None
        self.DiagnosisDoctorName = None
        self.ClinicalDiagnosis = None
        self.MainNarration = None
        self.PhysicalExamination = None
        self.InspectionFindings = None
        self.TreatmentOpinion = None


    def _deserialize(self, params):
        self.DiagnosisTime = params.get("DiagnosisTime")
        self.DiagnosisDepartmentName = params.get("DiagnosisDepartmentName")
        self.DiagnosisDoctorName = params.get("DiagnosisDoctorName")
        self.ClinicalDiagnosis = params.get("ClinicalDiagnosis")
        self.MainNarration = params.get("MainNarration")
        self.PhysicalExamination = params.get("PhysicalExamination")
        self.InspectionFindings = params.get("InspectionFindings")
        self.TreatmentOpinion = params.get("TreatmentOpinion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MenstrualHistory(AbstractModel):
    """月经史

    """

    def __init__(self):
        """
        :param IsOrNot: 是否来月经
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsOrNot: str\n        :param MenarcheAge: 月经初潮年龄
注意：此字段可能返回 null，表示取不到有效值。\n        :type MenarcheAge: str\n        :param LastTime: 末次月经时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastTime: str\n        :param Flow: 经量
注意：此字段可能返回 null，表示取不到有效值。\n        :type Flow: str\n        :param Cycles: 月经周期
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cycles: str\n        :param Duration: 行经天数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Duration: str\n        """
        self.IsOrNot = None
        self.MenarcheAge = None
        self.LastTime = None
        self.Flow = None
        self.Cycles = None
        self.Duration = None


    def _deserialize(self, params):
        self.IsOrNot = params.get("IsOrNot")
        self.MenarcheAge = params.get("MenarcheAge")
        self.LastTime = params.get("LastTime")
        self.Flow = params.get("Flow")
        self.Cycles = params.get("Cycles")
        self.Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MenstrualMedicalHistory(AbstractModel):
    """月经史

    """

    def __init__(self):
        """
        :param LastMenstrualPeriod: 末次月经时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastMenstrualPeriod: str\n        :param MenstrualFlow: 经量
注意：此字段可能返回 null，表示取不到有效值。\n        :type MenstrualFlow: str\n        :param MenarcheAge: 月经初潮年龄
注意：此字段可能返回 null，表示取不到有效值。\n        :type MenarcheAge: str\n        :param MenstruationOrNot: 是否来月经
注意：此字段可能返回 null，表示取不到有效值。\n        :type MenstruationOrNot: str\n        :param MenstrualCycles: 月经周期
注意：此字段可能返回 null，表示取不到有效值。\n        :type MenstrualCycles: str\n        :param MenstrualPeriod: 月经持续天数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MenstrualPeriod: str\n        """
        self.LastMenstrualPeriod = None
        self.MenstrualFlow = None
        self.MenarcheAge = None
        self.MenstruationOrNot = None
        self.MenstrualCycles = None
        self.MenstrualPeriod = None


    def _deserialize(self, params):
        self.LastMenstrualPeriod = params.get("LastMenstrualPeriod")
        self.MenstrualFlow = params.get("MenstrualFlow")
        self.MenarcheAge = params.get("MenarcheAge")
        self.MenstruationOrNot = params.get("MenstruationOrNot")
        self.MenstrualCycles = params.get("MenstrualCycles")
        self.MenstrualPeriod = params.get("MenstrualPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Metastasis(AbstractModel):
    """转移

    """

    def __init__(self):
        """
        :param Index: 索引位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: int\n        :param Text: 原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type Text: str\n        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。\n        :type Part: str\n        :param TotalNum: 局部总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalNum: str\n        :param TransferNum: 转移数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransferNum: str\n        """
        self.Index = None
        self.Text = None
        self.Part = None
        self.TotalNum = None
        self.TransferNum = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.Text = params.get("Text")
        self.Part = params.get("Part")
        self.TotalNum = params.get("TotalNum")
        self.TransferNum = params.get("TransferNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Multiple(AbstractModel):
    """多发

    """

    def __init__(self):
        """
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: list of int\n        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type Src: str\n        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        :param Count: 数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type Count: int\n        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        """
        self.Index = None
        self.Src = None
        self.Value = None
        self.Count = None
        self.Name = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        self.Count = params.get("Count")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormPart(AbstractModel):
    """标准部位

    """

    def __init__(self):
        """
        :param Part: 部位值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Part: str\n        :param PartDirection: 部位方向
注意：此字段可能返回 null，表示取不到有效值。\n        :type PartDirection: str\n        :param Tissue: 组织值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tissue: str\n        :param TissueDirection: 组织方向
注意：此字段可能返回 null，表示取不到有效值。\n        :type TissueDirection: str\n        :param Upper: 上级部位
注意：此字段可能返回 null，表示取不到有效值。\n        :type Upper: str\n        """
        self.Part = None
        self.PartDirection = None
        self.Tissue = None
        self.TissueDirection = None
        self.Upper = None


    def _deserialize(self, params):
        self.Part = params.get("Part")
        self.PartDirection = params.get("PartDirection")
        self.Tissue = params.get("Tissue")
        self.TissueDirection = params.get("TissueDirection")
        self.Upper = params.get("Upper")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormSize(AbstractModel):
    """大小

    """

    def __init__(self):
        """
        :param Number: 数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type Number: list of str\n        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        :param Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。\n        :type Unit: str\n        """
        self.Number = None
        self.Type = None
        self.Unit = None


    def _deserialize(self, params):
        self.Number = params.get("Number")
        self.Type = params.get("Type")
        self.Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObstericalMedicalHistory(AbstractModel):
    """孕产史

    """

    def __init__(self):
        """
        :param MarriageHistory: 婚史
注意：此字段可能返回 null，表示取不到有效值。\n        :type MarriageHistory: str\n        :param FertilityHistory: 孕史
注意：此字段可能返回 null，表示取不到有效值。\n        :type FertilityHistory: str\n        """
        self.MarriageHistory = None
        self.FertilityHistory = None


    def _deserialize(self, params):
        self.MarriageHistory = params.get("MarriageHistory")
        self.FertilityHistory = params.get("FertilityHistory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Organ(AbstractModel):
    """器官

    """

    def __init__(self):
        """
        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。\n        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`\n        :param Size: 大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type Size: list of Size\n        :param Envelope: 包膜
注意：此字段可能返回 null，表示取不到有效值。\n        :type Envelope: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Edge: 边缘
注意：此字段可能返回 null，表示取不到有效值。\n        :type Edge: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param InnerEcho: 内部回声
注意：此字段可能返回 null，表示取不到有效值。\n        :type InnerEcho: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Gland: 腺体
注意：此字段可能返回 null，表示取不到有效值。\n        :type Gland: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Shape: 形状
注意：此字段可能返回 null，表示取不到有效值。\n        :type Shape: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Thickness: 厚度
注意：此字段可能返回 null，表示取不到有效值。\n        :type Thickness: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param ShapeAttr: 形态
注意：此字段可能返回 null，表示取不到有效值。\n        :type ShapeAttr: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param CDFI: 血液cdfi
注意：此字段可能返回 null，表示取不到有效值。\n        :type CDFI: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param SymDesc: 描述信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type SymDesc: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param SizeStatus: 大小状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type SizeStatus: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Outline: 轮廓
注意：此字段可能返回 null，表示取不到有效值。\n        :type Outline: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Structure: 结构
注意：此字段可能返回 null，表示取不到有效值。\n        :type Structure: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Density: 密度
注意：此字段可能返回 null，表示取不到有效值。\n        :type Density: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Vas: 血管
注意：此字段可能返回 null，表示取不到有效值。\n        :type Vas: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Cysticwall: 囊壁
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cysticwall: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Capsule: 被膜
注意：此字段可能返回 null，表示取不到有效值。\n        :type Capsule: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param IsthmusThicknese: 峡部厚度
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsthmusThicknese: :class:`tencentcloud.mrs.v20200910.models.Size`\n        :param InnerEchoDistribution: 内部回声分布
注意：此字段可能返回 null，表示取不到有效值。\n        :type InnerEchoDistribution: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type Src: str\n        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: list of int\n        """
        self.Part = None
        self.Size = None
        self.Envelope = None
        self.Edge = None
        self.InnerEcho = None
        self.Gland = None
        self.Shape = None
        self.Thickness = None
        self.ShapeAttr = None
        self.CDFI = None
        self.SymDesc = None
        self.SizeStatus = None
        self.Outline = None
        self.Structure = None
        self.Density = None
        self.Vas = None
        self.Cysticwall = None
        self.Capsule = None
        self.IsthmusThicknese = None
        self.InnerEchoDistribution = None
        self.Src = None
        self.Index = None


    def _deserialize(self, params):
        if params.get("Part") is not None:
            self.Part = Part()
            self.Part._deserialize(params.get("Part"))
        if params.get("Size") is not None:
            self.Size = []
            for item in params.get("Size"):
                obj = Size()
                obj._deserialize(item)
                self.Size.append(obj)
        if params.get("Envelope") is not None:
            self.Envelope = BlockInfo()
            self.Envelope._deserialize(params.get("Envelope"))
        if params.get("Edge") is not None:
            self.Edge = BlockInfo()
            self.Edge._deserialize(params.get("Edge"))
        if params.get("InnerEcho") is not None:
            self.InnerEcho = BlockInfo()
            self.InnerEcho._deserialize(params.get("InnerEcho"))
        if params.get("Gland") is not None:
            self.Gland = BlockInfo()
            self.Gland._deserialize(params.get("Gland"))
        if params.get("Shape") is not None:
            self.Shape = BlockInfo()
            self.Shape._deserialize(params.get("Shape"))
        if params.get("Thickness") is not None:
            self.Thickness = BlockInfo()
            self.Thickness._deserialize(params.get("Thickness"))
        if params.get("ShapeAttr") is not None:
            self.ShapeAttr = BlockInfo()
            self.ShapeAttr._deserialize(params.get("ShapeAttr"))
        if params.get("CDFI") is not None:
            self.CDFI = BlockInfo()
            self.CDFI._deserialize(params.get("CDFI"))
        if params.get("SymDesc") is not None:
            self.SymDesc = BlockInfo()
            self.SymDesc._deserialize(params.get("SymDesc"))
        if params.get("SizeStatus") is not None:
            self.SizeStatus = BlockInfo()
            self.SizeStatus._deserialize(params.get("SizeStatus"))
        if params.get("Outline") is not None:
            self.Outline = BlockInfo()
            self.Outline._deserialize(params.get("Outline"))
        if params.get("Structure") is not None:
            self.Structure = BlockInfo()
            self.Structure._deserialize(params.get("Structure"))
        if params.get("Density") is not None:
            self.Density = BlockInfo()
            self.Density._deserialize(params.get("Density"))
        if params.get("Vas") is not None:
            self.Vas = BlockInfo()
            self.Vas._deserialize(params.get("Vas"))
        if params.get("Cysticwall") is not None:
            self.Cysticwall = BlockInfo()
            self.Cysticwall._deserialize(params.get("Cysticwall"))
        if params.get("Capsule") is not None:
            self.Capsule = BlockInfo()
            self.Capsule._deserialize(params.get("Capsule"))
        if params.get("IsthmusThicknese") is not None:
            self.IsthmusThicknese = Size()
            self.IsthmusThicknese._deserialize(params.get("IsthmusThicknese"))
        if params.get("InnerEchoDistribution") is not None:
            self.InnerEchoDistribution = BlockInfo()
            self.InnerEchoDistribution._deserialize(params.get("InnerEchoDistribution"))
        self.Src = params.get("Src")
        self.Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Part(AbstractModel):
    """部位信息

    """

    def __init__(self):
        """
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: list of int\n        :param NormPart: 部位
注意：此字段可能返回 null，表示取不到有效值。\n        :type NormPart: :class:`tencentcloud.mrs.v20200910.models.NormPart`\n        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type Src: str\n        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        """
        self.Index = None
        self.NormPart = None
        self.Src = None
        self.Value = None
        self.Name = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        if params.get("NormPart") is not None:
            self.NormPart = NormPart()
            self.NormPart._deserialize(params.get("NormPart"))
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Pathology(AbstractModel):
    """病理内容

    """

    def __init__(self):
        """
        :param PathologicalType: 病理类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type PathologicalType: str\n        :param InfiltrationDepth: 侵润深度
注意：此字段可能返回 null，表示取不到有效值。\n        :type InfiltrationDepth: str\n        :param PTNM: PTNM分期
注意：此字段可能返回 null，表示取不到有效值。\n        :type PTNM: str\n        :param DistanceMetastasis: 远处转移
注意：此字段可能返回 null，表示取不到有效值。\n        :type DistanceMetastasis: str\n        :param SummaryText: 影像诊断
注意：此字段可能返回 null，表示取不到有效值。\n        :type SummaryText: str\n        :param DescText: 影像所见
注意：此字段可能返回 null，表示取不到有效值。\n        :type DescText: str\n        :param HistologyType: 组织学类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type HistologyType: str\n        :param HistologyLevel: 组织学等级
注意：此字段可能返回 null，表示取不到有效值。\n        :type HistologyLevel: str\n        :param SampleType: 标本类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type SampleType: str\n        :param SamplePart: 标本部位
注意：此字段可能返回 null，表示取不到有效值。\n        :type SamplePart: str\n        :param SampleSize: 标本大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type SampleSize: str\n        :param InvasiveList: 肿瘤扩散
注意：此字段可能返回 null，表示取不到有效值。\n        :type InvasiveList: list of Invasive\n        :param MetastasisList: 肿瘤转移
注意：此字段可能返回 null，表示取不到有效值。\n        :type MetastasisList: list of Metastasis\n        :param IHCList: 免疫组化信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type IHCList: list of IHC\n        """
        self.PathologicalType = None
        self.InfiltrationDepth = None
        self.PTNM = None
        self.DistanceMetastasis = None
        self.SummaryText = None
        self.DescText = None
        self.HistologyType = None
        self.HistologyLevel = None
        self.SampleType = None
        self.SamplePart = None
        self.SampleSize = None
        self.InvasiveList = None
        self.MetastasisList = None
        self.IHCList = None


    def _deserialize(self, params):
        self.PathologicalType = params.get("PathologicalType")
        self.InfiltrationDepth = params.get("InfiltrationDepth")
        self.PTNM = params.get("PTNM")
        self.DistanceMetastasis = params.get("DistanceMetastasis")
        self.SummaryText = params.get("SummaryText")
        self.DescText = params.get("DescText")
        self.HistologyType = params.get("HistologyType")
        self.HistologyLevel = params.get("HistologyLevel")
        self.SampleType = params.get("SampleType")
        self.SamplePart = params.get("SamplePart")
        self.SampleSize = params.get("SampleSize")
        if params.get("InvasiveList") is not None:
            self.InvasiveList = []
            for item in params.get("InvasiveList"):
                obj = Invasive()
                obj._deserialize(item)
                self.InvasiveList.append(obj)
        if params.get("MetastasisList") is not None:
            self.MetastasisList = []
            for item in params.get("MetastasisList"):
                obj = Metastasis()
                obj._deserialize(item)
                self.MetastasisList.append(obj)
        if params.get("IHCList") is not None:
            self.IHCList = []
            for item in params.get("IHCList"):
                obj = IHC()
                obj._deserialize(item)
                self.IHCList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathologyReport(AbstractModel):
    """病理报告

    """

    def __init__(self):
        """
        :param CancerPart: 癌症部位
注意：此字段可能返回 null，表示取不到有效值。\n        :type CancerPart: :class:`tencentcloud.mrs.v20200910.models.Part`\n        :param CancerSize: 癌症部位大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type CancerSize: list of Size\n        :param DescText: 描述文本
注意：此字段可能返回 null，表示取不到有效值。\n        :type DescText: str\n        :param HistologyLevel: 组织学等级
注意：此字段可能返回 null，表示取不到有效值。\n        :type HistologyLevel: :class:`tencentcloud.mrs.v20200910.models.HistologyLevel`\n        :param HistologyType: 组织学类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type HistologyType: :class:`tencentcloud.mrs.v20200910.models.HistologyType`\n        :param IHC: IHC信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type IHC: list of IHCInfo\n        :param InfiltrationDepth: 浸润深度
注意：此字段可能返回 null，表示取不到有效值。\n        :type InfiltrationDepth: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Invasive: 肿瘤扩散
注意：此字段可能返回 null，表示取不到有效值。\n        :type Invasive: list of Invas\n        :param LymphNodes: 淋巴结
注意：此字段可能返回 null，表示取不到有效值。\n        :type LymphNodes: list of Lymph\n        :param PTNM: PTNM信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type PTNM: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param PathologicalReportType: 病理报告类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type PathologicalReportType: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param ReportText: 报告原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReportText: str\n        :param SampleType: 标本类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type SampleType: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param SummaryText: 结论文本
注意：此字段可能返回 null，表示取不到有效值。\n        :type SummaryText: str\n        """
        self.CancerPart = None
        self.CancerSize = None
        self.DescText = None
        self.HistologyLevel = None
        self.HistologyType = None
        self.IHC = None
        self.InfiltrationDepth = None
        self.Invasive = None
        self.LymphNodes = None
        self.PTNM = None
        self.PathologicalReportType = None
        self.ReportText = None
        self.SampleType = None
        self.SummaryText = None


    def _deserialize(self, params):
        if params.get("CancerPart") is not None:
            self.CancerPart = Part()
            self.CancerPart._deserialize(params.get("CancerPart"))
        if params.get("CancerSize") is not None:
            self.CancerSize = []
            for item in params.get("CancerSize"):
                obj = Size()
                obj._deserialize(item)
                self.CancerSize.append(obj)
        self.DescText = params.get("DescText")
        if params.get("HistologyLevel") is not None:
            self.HistologyLevel = HistologyLevel()
            self.HistologyLevel._deserialize(params.get("HistologyLevel"))
        if params.get("HistologyType") is not None:
            self.HistologyType = HistologyType()
            self.HistologyType._deserialize(params.get("HistologyType"))
        if params.get("IHC") is not None:
            self.IHC = []
            for item in params.get("IHC"):
                obj = IHCInfo()
                obj._deserialize(item)
                self.IHC.append(obj)
        if params.get("InfiltrationDepth") is not None:
            self.InfiltrationDepth = BlockInfo()
            self.InfiltrationDepth._deserialize(params.get("InfiltrationDepth"))
        if params.get("Invasive") is not None:
            self.Invasive = []
            for item in params.get("Invasive"):
                obj = Invas()
                obj._deserialize(item)
                self.Invasive.append(obj)
        if params.get("LymphNodes") is not None:
            self.LymphNodes = []
            for item in params.get("LymphNodes"):
                obj = Lymph()
                obj._deserialize(item)
                self.LymphNodes.append(obj)
        if params.get("PTNM") is not None:
            self.PTNM = BlockInfo()
            self.PTNM._deserialize(params.get("PTNM"))
        if params.get("PathologicalReportType") is not None:
            self.PathologicalReportType = BlockInfo()
            self.PathologicalReportType._deserialize(params.get("PathologicalReportType"))
        self.ReportText = params.get("ReportText")
        if params.get("SampleType") is not None:
            self.SampleType = BlockInfo()
            self.SampleType._deserialize(params.get("SampleType"))
        self.SummaryText = params.get("SummaryText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PatientInfo(AbstractModel):
    """患者信息

    """

    def __init__(self):
        """
        :param Name: 患者姓名
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Sex: 患者性别
注意：此字段可能返回 null，表示取不到有效值。\n        :type Sex: str\n        :param Age: 患者年龄
注意：此字段可能返回 null，表示取不到有效值。\n        :type Age: str\n        :param Phone: 患者手机号码
注意：此字段可能返回 null，表示取不到有效值。\n        :type Phone: str\n        :param Address: 患者地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type Address: str\n        :param IdCard: 患者身份证
注意：此字段可能返回 null，表示取不到有效值。\n        :type IdCard: str\n        :param HealthCardNo: 健康卡号
注意：此字段可能返回 null，表示取不到有效值。\n        :type HealthCardNo: str\n        :param SocialSecurityCardNo: 社保卡号
注意：此字段可能返回 null，表示取不到有效值。\n        :type SocialSecurityCardNo: str\n        :param Birthday: 出生日期
注意：此字段可能返回 null，表示取不到有效值。\n        :type Birthday: str\n        :param Ethnicity: 民族
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ethnicity: str\n        :param Married: 婚姻状况
注意：此字段可能返回 null，表示取不到有效值。\n        :type Married: str\n        :param Profession: 职业
注意：此字段可能返回 null，表示取不到有效值。\n        :type Profession: str\n        :param EducationBackground: 教育程度
注意：此字段可能返回 null，表示取不到有效值。\n        :type EducationBackground: str\n        :param Nationality: 国籍
注意：此字段可能返回 null，表示取不到有效值。\n        :type Nationality: str\n        :param BirthPlace: 籍贯
注意：此字段可能返回 null，表示取不到有效值。\n        :type BirthPlace: str\n        :param MedicalInsuranceType: 医保类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type MedicalInsuranceType: str\n        """
        self.Name = None
        self.Sex = None
        self.Age = None
        self.Phone = None
        self.Address = None
        self.IdCard = None
        self.HealthCardNo = None
        self.SocialSecurityCardNo = None
        self.Birthday = None
        self.Ethnicity = None
        self.Married = None
        self.Profession = None
        self.EducationBackground = None
        self.Nationality = None
        self.BirthPlace = None
        self.MedicalInsuranceType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Sex = params.get("Sex")
        self.Age = params.get("Age")
        self.Phone = params.get("Phone")
        self.Address = params.get("Address")
        self.IdCard = params.get("IdCard")
        self.HealthCardNo = params.get("HealthCardNo")
        self.SocialSecurityCardNo = params.get("SocialSecurityCardNo")
        self.Birthday = params.get("Birthday")
        self.Ethnicity = params.get("Ethnicity")
        self.Married = params.get("Married")
        self.Profession = params.get("Profession")
        self.EducationBackground = params.get("EducationBackground")
        self.Nationality = params.get("Nationality")
        self.BirthPlace = params.get("BirthPlace")
        self.MedicalInsuranceType = params.get("MedicalInsuranceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonalHistory(AbstractModel):
    """个人史

    """

    def __init__(self):
        """
        :param BirthPlace: 出生地
注意：此字段可能返回 null，表示取不到有效值。\n        :type BirthPlace: str\n        :param Job: 工作史
注意：此字段可能返回 null，表示取不到有效值。\n        :type Job: str\n        :param LivePlace: 旅居史
注意：此字段可能返回 null，表示取不到有效值。\n        :type LivePlace: str\n        :param Personal: 个人史
注意：此字段可能返回 null，表示取不到有效值。\n        :type Personal: str\n        :param Smoke: 吸烟史
注意：此字段可能返回 null，表示取不到有效值。\n        :type Smoke: str\n        :param Alcoholic: 饮酒史
注意：此字段可能返回 null，表示取不到有效值。\n        :type Alcoholic: str\n        """
        self.BirthPlace = None
        self.Job = None
        self.LivePlace = None
        self.Personal = None
        self.Smoke = None
        self.Alcoholic = None


    def _deserialize(self, params):
        self.BirthPlace = params.get("BirthPlace")
        self.Job = params.get("Job")
        self.LivePlace = params.get("LivePlace")
        self.Personal = params.get("Personal")
        self.Smoke = params.get("Smoke")
        self.Alcoholic = params.get("Alcoholic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonalInfo(AbstractModel):
    """个人信息

    """

    def __init__(self):
        """
        :param Name: 姓名
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Gender: 性别
注意：此字段可能返回 null，表示取不到有效值。\n        :type Gender: str\n        :param Age: 年龄
注意：此字段可能返回 null，表示取不到有效值。\n        :type Age: str\n        :param IDCard: 身份证号码
注意：此字段可能返回 null，表示取不到有效值。\n        :type IDCard: str\n        :param HealthCardNum: 健康卡号
注意：此字段可能返回 null，表示取不到有效值。\n        :type HealthCardNum: str\n        :param SocialSecurityCardNum: 社保号
注意：此字段可能返回 null，表示取不到有效值。\n        :type SocialSecurityCardNum: str\n        :param Birthday: 出生日期
注意：此字段可能返回 null，表示取不到有效值。\n        :type Birthday: str\n        :param Ethnicity: 民族
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ethnicity: str\n        :param Nationality: 国籍
注意：此字段可能返回 null，表示取不到有效值。\n        :type Nationality: str\n        :param Married: 婚姻状况
注意：此字段可能返回 null，表示取不到有效值。\n        :type Married: str\n        :param Profession: 职业
注意：此字段可能返回 null，表示取不到有效值。\n        :type Profession: str\n        :param EducationBackground: 教育程度
注意：此字段可能返回 null，表示取不到有效值。\n        :type EducationBackground: str\n        :param BirthPlace: 籍贯
注意：此字段可能返回 null，表示取不到有效值。\n        :type BirthPlace: str\n        :param MedicalInsuranceType: 医保卡类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type MedicalInsuranceType: str\n        :param LinkPhone: 联系电话
注意：此字段可能返回 null，表示取不到有效值。\n        :type LinkPhone: str\n        :param LinkAddress: 联系地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type LinkAddress: str\n        :param KinsfolkName: 家属姓名
注意：此字段可能返回 null，表示取不到有效值。\n        :type KinsfolkName: str\n        :param KinsfolkRelation: 家属关系
注意：此字段可能返回 null，表示取不到有效值。\n        :type KinsfolkRelation: str\n        :param KinsfolkPhone: 家属联系电话
注意：此字段可能返回 null，表示取不到有效值。\n        :type KinsfolkPhone: str\n        """
        self.Name = None
        self.Gender = None
        self.Age = None
        self.IDCard = None
        self.HealthCardNum = None
        self.SocialSecurityCardNum = None
        self.Birthday = None
        self.Ethnicity = None
        self.Nationality = None
        self.Married = None
        self.Profession = None
        self.EducationBackground = None
        self.BirthPlace = None
        self.MedicalInsuranceType = None
        self.LinkPhone = None
        self.LinkAddress = None
        self.KinsfolkName = None
        self.KinsfolkRelation = None
        self.KinsfolkPhone = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Gender = params.get("Gender")
        self.Age = params.get("Age")
        self.IDCard = params.get("IDCard")
        self.HealthCardNum = params.get("HealthCardNum")
        self.SocialSecurityCardNum = params.get("SocialSecurityCardNum")
        self.Birthday = params.get("Birthday")
        self.Ethnicity = params.get("Ethnicity")
        self.Nationality = params.get("Nationality")
        self.Married = params.get("Married")
        self.Profession = params.get("Profession")
        self.EducationBackground = params.get("EducationBackground")
        self.BirthPlace = params.get("BirthPlace")
        self.MedicalInsuranceType = params.get("MedicalInsuranceType")
        self.LinkPhone = params.get("LinkPhone")
        self.LinkAddress = params.get("LinkAddress")
        self.KinsfolkName = params.get("KinsfolkName")
        self.KinsfolkRelation = params.get("KinsfolkRelation")
        self.KinsfolkPhone = params.get("KinsfolkPhone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonalMedicalHistory(AbstractModel):
    """个人史

    """

    def __init__(self):
        """
        :param BirthPlace: 出生史
注意：此字段可能返回 null，表示取不到有效值。\n        :type BirthPlace: str\n        :param LivePlace: 居住史
注意：此字段可能返回 null，表示取不到有效值。\n        :type LivePlace: str\n        :param Job: 工作史
注意：此字段可能返回 null，表示取不到有效值。\n        :type Job: str\n        :param SmokeHistory: 吸烟史
注意：此字段可能返回 null，表示取不到有效值。\n        :type SmokeHistory: str\n        :param AlcoholicHistory: 饮酒史
注意：此字段可能返回 null，表示取不到有效值。\n        :type AlcoholicHistory: str\n        """
        self.BirthPlace = None
        self.LivePlace = None
        self.Job = None
        self.SmokeHistory = None
        self.AlcoholicHistory = None


    def _deserialize(self, params):
        self.BirthPlace = params.get("BirthPlace")
        self.LivePlace = params.get("LivePlace")
        self.Job = params.get("Job")
        self.SmokeHistory = params.get("SmokeHistory")
        self.AlcoholicHistory = params.get("AlcoholicHistory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportImageStructuredRequest(AbstractModel):
    """ReportImageStructured请求参数结构体

    """

    def __init__(self):
        """
        :param ImageURL: 医疗报告图片URL\n        :type ImageURL: str\n        :param ImageBase64: 医疗报告图片base64编码后内容\n        :type ImageBase64: str\n        """
        self.ImageURL = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageURL = params.get("ImageURL")
        self.ImageBase64 = params.get("ImageBase64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportImageStructuredResponse(AbstractModel):
    """ReportImageStructured返回参数结构体

    """

    def __init__(self):
        """
        :param Report: 报告内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Report: :class:`tencentcloud.mrs.v20200910.models.ImageReport`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Report = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Report") is not None:
            self.Report = ImageReport()
            self.Report._deserialize(params.get("Report"))
        self.RequestId = params.get("RequestId")


class ReportInfo(AbstractModel):
    """报告基本信息

    """

    def __init__(self):
        """
        :param Hospital: 医院名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Hospital: str\n        :param DepartmentName: 科室名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type DepartmentName: str\n        :param BillingTime: 申请时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type BillingTime: str\n        :param ReportTime: 报告时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReportTime: str\n        :param InspectTime: 检查时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type InspectTime: str\n        :param CheckNum: 检查号
注意：此字段可能返回 null，表示取不到有效值。\n        :type CheckNum: str\n        :param ImageNum: 影像号
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageNum: str\n        :param RadiationNum: 放射号
注意：此字段可能返回 null，表示取不到有效值。\n        :type RadiationNum: str\n        :param TestNum: 检验号
注意：此字段可能返回 null，表示取不到有效值。\n        :type TestNum: str\n        :param OutpatientNum: 门诊号
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutpatientNum: str\n        :param PathologyNum: 病理号
注意：此字段可能返回 null，表示取不到有效值。\n        :type PathologyNum: str\n        :param InHospitalNum: 住院号
注意：此字段可能返回 null，表示取不到有效值。\n        :type InHospitalNum: str\n        :param SampleNum: 样本号
注意：此字段可能返回 null，表示取不到有效值。\n        :type SampleNum: str\n        :param SampleType: 标本种类
注意：此字段可能返回 null，表示取不到有效值。\n        :type SampleType: str\n        :param MedicalRecordNum: 病历号
注意：此字段可能返回 null，表示取不到有效值。\n        :type MedicalRecordNum: str\n        :param ReportName: 报告名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReportName: str\n        :param UltraNum: 超声号
注意：此字段可能返回 null，表示取不到有效值。\n        :type UltraNum: str\n        :param Diagnose: 临床诊断
注意：此字段可能返回 null，表示取不到有效值。\n        :type Diagnose: str\n        """
        self.Hospital = None
        self.DepartmentName = None
        self.BillingTime = None
        self.ReportTime = None
        self.InspectTime = None
        self.CheckNum = None
        self.ImageNum = None
        self.RadiationNum = None
        self.TestNum = None
        self.OutpatientNum = None
        self.PathologyNum = None
        self.InHospitalNum = None
        self.SampleNum = None
        self.SampleType = None
        self.MedicalRecordNum = None
        self.ReportName = None
        self.UltraNum = None
        self.Diagnose = None


    def _deserialize(self, params):
        self.Hospital = params.get("Hospital")
        self.DepartmentName = params.get("DepartmentName")
        self.BillingTime = params.get("BillingTime")
        self.ReportTime = params.get("ReportTime")
        self.InspectTime = params.get("InspectTime")
        self.CheckNum = params.get("CheckNum")
        self.ImageNum = params.get("ImageNum")
        self.RadiationNum = params.get("RadiationNum")
        self.TestNum = params.get("TestNum")
        self.OutpatientNum = params.get("OutpatientNum")
        self.PathologyNum = params.get("PathologyNum")
        self.InHospitalNum = params.get("InHospitalNum")
        self.SampleNum = params.get("SampleNum")
        self.SampleType = params.get("SampleType")
        self.MedicalRecordNum = params.get("MedicalRecordNum")
        self.ReportName = params.get("ReportName")
        self.UltraNum = params.get("UltraNum")
        self.Diagnose = params.get("Diagnose")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportTextStructuredRequest(AbstractModel):
    """ReportTextStructured请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 报告文本内容\n        :type Text: str\n        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportTextStructuredResponse(AbstractModel):
    """ReportTextStructured返回参数结构体

    """

    def __init__(self):
        """
        :param Report: 报告内容\n        :type Report: :class:`tencentcloud.mrs.v20200910.models.TextReport`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Report = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Report") is not None:
            self.Report = TextReport()
            self.Report._deserialize(params.get("Report"))
        self.RequestId = params.get("RequestId")


class Size(AbstractModel):
    """大小

    """

    def __init__(self):
        """
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: list of int\n        :param NormSize: 标准大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type NormSize: :class:`tencentcloud.mrs.v20200910.models.NormSize`\n        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type Src: str\n        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        """
        self.Index = None
        self.NormSize = None
        self.Src = None
        self.Value = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        if params.get("NormSize") is not None:
            self.NormSize = NormSize()
            self.NormSize._deserialize(params.get("NormSize"))
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Summary(AbstractModel):
    """结论

    """

    def __init__(self):
        """
        :param Symptom: 症状
注意：此字段可能返回 null，表示取不到有效值。\n        :type Symptom: list of SymptomInfo\n        :param Text: 文本
注意：此字段可能返回 null，表示取不到有效值。\n        :type Text: str\n        """
        self.Symptom = None
        self.Text = None


    def _deserialize(self, params):
        if params.get("Symptom") is not None:
            self.Symptom = []
            for item in params.get("Symptom"):
                obj = SymptomInfo()
                obj._deserialize(item)
                self.Symptom.append(obj)
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Surgery(AbstractModel):
    """手术记录

    """

    def __init__(self):
        """
        :param SurgeryHistory: 手术史
注意：此字段可能返回 null，表示取不到有效值。\n        :type SurgeryHistory: :class:`tencentcloud.mrs.v20200910.models.SurgeryHistory`\n        """
        self.SurgeryHistory = None


    def _deserialize(self, params):
        if params.get("SurgeryHistory") is not None:
            self.SurgeryHistory = SurgeryHistory()
            self.SurgeryHistory._deserialize(params.get("SurgeryHistory"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SurgeryAttr(AbstractModel):
    """手术记录属性

    """

    def __init__(self):
        """
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SurgeryHistory(AbstractModel):
    """手术史

    """

    def __init__(self):
        """
        :param SurgeryName: 手术名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type SurgeryName: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`\n        :param SurgeryDate: 手术日期
注意：此字段可能返回 null，表示取不到有效值。\n        :type SurgeryDate: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`\n        :param PreoperativePathology: 术前诊断
注意：此字段可能返回 null，表示取不到有效值。\n        :type PreoperativePathology: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`\n        :param IntraoperativePathology: 术中诊断
注意：此字段可能返回 null，表示取不到有效值。\n        :type IntraoperativePathology: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`\n        :param PostoperativePathology: 术后诊断
注意：此字段可能返回 null，表示取不到有效值。\n        :type PostoperativePathology: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`\n        :param DischargeDiagnosis: 出院诊断
注意：此字段可能返回 null，表示取不到有效值。\n        :type DischargeDiagnosis: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`\n        """
        self.SurgeryName = None
        self.SurgeryDate = None
        self.PreoperativePathology = None
        self.IntraoperativePathology = None
        self.PostoperativePathology = None
        self.DischargeDiagnosis = None


    def _deserialize(self, params):
        if params.get("SurgeryName") is not None:
            self.SurgeryName = SurgeryAttr()
            self.SurgeryName._deserialize(params.get("SurgeryName"))
        if params.get("SurgeryDate") is not None:
            self.SurgeryDate = SurgeryAttr()
            self.SurgeryDate._deserialize(params.get("SurgeryDate"))
        if params.get("PreoperativePathology") is not None:
            self.PreoperativePathology = SurgeryAttr()
            self.PreoperativePathology._deserialize(params.get("PreoperativePathology"))
        if params.get("IntraoperativePathology") is not None:
            self.IntraoperativePathology = SurgeryAttr()
            self.IntraoperativePathology._deserialize(params.get("IntraoperativePathology"))
        if params.get("PostoperativePathology") is not None:
            self.PostoperativePathology = SurgeryAttr()
            self.PostoperativePathology._deserialize(params.get("PostoperativePathology"))
        if params.get("DischargeDiagnosis") is not None:
            self.DischargeDiagnosis = SurgeryAttr()
            self.DischargeDiagnosis._deserialize(params.get("DischargeDiagnosis"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Symptom(AbstractModel):
    """可见病症内容

    """

    def __init__(self):
        """
        :param Desc: 描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Desc: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。\n        :type Part: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        :param Grade: 等级
注意：此字段可能返回 null，表示取不到有效值。\n        :type Grade: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        :param AttrList: 性质
注意：此字段可能返回 null，表示取不到有效值。\n        :type AttrList: list of Attribute\n        """
        self.Desc = None
        self.Part = None
        self.Grade = None
        self.AttrList = None


    def _deserialize(self, params):
        if params.get("Desc") is not None:
            self.Desc = Attribute()
            self.Desc._deserialize(params.get("Desc"))
        if params.get("Part") is not None:
            self.Part = Attribute()
            self.Part._deserialize(params.get("Part"))
        if params.get("Grade") is not None:
            self.Grade = Attribute()
            self.Grade._deserialize(params.get("Grade"))
        if params.get("AttrList") is not None:
            self.AttrList = []
            for item in params.get("AttrList"):
                obj = Attribute()
                obj._deserialize(item)
                self.AttrList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SymptomInfo(AbstractModel):
    """病症描述信息

    """

    def __init__(self):
        """
        :param Grade: 等级
注意：此字段可能返回 null，表示取不到有效值。\n        :type Grade: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。\n        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`\n        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: list of int\n        :param Symptom: 病变
注意：此字段可能返回 null，表示取不到有效值。\n        :type Symptom: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Attrs: 属性
注意：此字段可能返回 null，表示取不到有效值。\n        :type Attrs: list of BlockInfo\n        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type Src: str\n        """
        self.Grade = None
        self.Part = None
        self.Index = None
        self.Symptom = None
        self.Attrs = None
        self.Src = None


    def _deserialize(self, params):
        if params.get("Grade") is not None:
            self.Grade = BlockInfo()
            self.Grade._deserialize(params.get("Grade"))
        if params.get("Part") is not None:
            self.Part = Part()
            self.Part._deserialize(params.get("Part"))
        self.Index = params.get("Index")
        if params.get("Symptom") is not None:
            self.Symptom = BlockInfo()
            self.Symptom._deserialize(params.get("Symptom"))
        if params.get("Attrs") is not None:
            self.Attrs = []
            for item in params.get("Attrs"):
                obj = BlockInfo()
                obj._deserialize(item)
                self.Attrs.append(obj)
        self.Src = params.get("Src")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Template(AbstractModel):
    """报告模板

    """

    def __init__(self):
        """
        :param PatientInfo: 患者信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type PatientInfo: :class:`tencentcloud.mrs.v20200910.models.PatientInfo`\n        :param ReportInfo: 报告信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReportInfo: :class:`tencentcloud.mrs.v20200910.models.ReportInfo`\n        :param Check: 检查报告
注意：此字段可能返回 null，表示取不到有效值。\n        :type Check: :class:`tencentcloud.mrs.v20200910.models.Check`\n        :param Pathology: 病理报告
注意：此字段可能返回 null，表示取不到有效值。\n        :type Pathology: :class:`tencentcloud.mrs.v20200910.models.PathologyReport`\n        :param MedDoc: 出院报告，入院报告，门诊病历
注意：此字段可能返回 null，表示取不到有效值。\n        :type MedDoc: :class:`tencentcloud.mrs.v20200910.models.MedDoc`\n        :param DiagCert: 诊断证明
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiagCert: :class:`tencentcloud.mrs.v20200910.models.DiagCert`\n        :param FirstPage: 病案首页
注意：此字段可能返回 null，表示取不到有效值。\n        :type FirstPage: :class:`tencentcloud.mrs.v20200910.models.FirstPage`\n        :param Indicator: 检验报告
注意：此字段可能返回 null，表示取不到有效值。\n        :type Indicator: :class:`tencentcloud.mrs.v20200910.models.Indicator`\n        :param ReportType: 报告类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReportType: str\n        :param MedicalRecordInfo: 门诊病历信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type MedicalRecordInfo: :class:`tencentcloud.mrs.v20200910.models.MedicalRecordInfo`\n        :param Hospitalization: 出入院信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Hospitalization: :class:`tencentcloud.mrs.v20200910.models.Hospitalization`\n        :param Surgery: 手术记录
注意：此字段可能返回 null，表示取不到有效值。\n        :type Surgery: :class:`tencentcloud.mrs.v20200910.models.Surgery`\n        """
        self.PatientInfo = None
        self.ReportInfo = None
        self.Check = None
        self.Pathology = None
        self.MedDoc = None
        self.DiagCert = None
        self.FirstPage = None
        self.Indicator = None
        self.ReportType = None
        self.MedicalRecordInfo = None
        self.Hospitalization = None
        self.Surgery = None


    def _deserialize(self, params):
        if params.get("PatientInfo") is not None:
            self.PatientInfo = PatientInfo()
            self.PatientInfo._deserialize(params.get("PatientInfo"))
        if params.get("ReportInfo") is not None:
            self.ReportInfo = ReportInfo()
            self.ReportInfo._deserialize(params.get("ReportInfo"))
        if params.get("Check") is not None:
            self.Check = Check()
            self.Check._deserialize(params.get("Check"))
        if params.get("Pathology") is not None:
            self.Pathology = PathologyReport()
            self.Pathology._deserialize(params.get("Pathology"))
        if params.get("MedDoc") is not None:
            self.MedDoc = MedDoc()
            self.MedDoc._deserialize(params.get("MedDoc"))
        if params.get("DiagCert") is not None:
            self.DiagCert = DiagCert()
            self.DiagCert._deserialize(params.get("DiagCert"))
        if params.get("FirstPage") is not None:
            self.FirstPage = FirstPage()
            self.FirstPage._deserialize(params.get("FirstPage"))
        if params.get("Indicator") is not None:
            self.Indicator = Indicator()
            self.Indicator._deserialize(params.get("Indicator"))
        self.ReportType = params.get("ReportType")
        if params.get("MedicalRecordInfo") is not None:
            self.MedicalRecordInfo = MedicalRecordInfo()
            self.MedicalRecordInfo._deserialize(params.get("MedicalRecordInfo"))
        if params.get("Hospitalization") is not None:
            self.Hospitalization = Hospitalization()
            self.Hospitalization._deserialize(params.get("Hospitalization"))
        if params.get("Surgery") is not None:
            self.Surgery = Surgery()
            self.Surgery._deserialize(params.get("Surgery"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TestItem(AbstractModel):
    """检验指标内容

    """

    def __init__(self):
        """
        :param ID: 标准名称编号，利用该编号可以获取详细的指标含义和解释
注意：此字段可能返回 null，表示取不到有效值。\n        :type ID: int\n        :param Code: 英文名称或简称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Code: str\n        :param Name: 项目指标名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Result: 检验结果值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param Range: 正常结果范围
注意：此字段可能返回 null，表示取不到有效值。\n        :type Range: str\n        :param Util: 指标单位
注意：此字段可能返回 null，表示取不到有效值。\n        :type Util: str\n        :param IsNormal: 是否正常
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsNormal: bool\n        :param IsExceed: 是否超标
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsExceed: bool\n        """
        self.ID = None
        self.Code = None
        self.Name = None
        self.Result = None
        self.Range = None
        self.Util = None
        self.IsNormal = None
        self.IsExceed = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Code = params.get("Code")
        self.Name = params.get("Name")
        self.Result = params.get("Result")
        self.Range = params.get("Range")
        self.Util = params.get("Util")
        self.IsNormal = params.get("IsNormal")
        self.IsExceed = params.get("IsExceed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextReport(AbstractModel):
    """文本类型报告返回结果

    """

    def __init__(self):
        """
        :param KindSet: 报告类别信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type KindSet: list of KindItem\n        :param BasicInfo: 基本信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type BasicInfo: :class:`tencentcloud.mrs.v20200910.models.BasicInfo`\n        :param PersonalInfo: 个人隐私信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type PersonalInfo: :class:`tencentcloud.mrs.v20200910.models.PersonalInfo`\n        :param TestList: 检验指标表
注意：此字段可能返回 null，表示取不到有效值。\n        :type TestList: list of TestItem\n        :param Inspection: 检查报告内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Inspection: :class:`tencentcloud.mrs.v20200910.models.Inspection`\n        :param CaseHistory: 病历资料
注意：此字段可能返回 null，表示取不到有效值。\n        :type CaseHistory: :class:`tencentcloud.mrs.v20200910.models.CaseHistory`\n        :param Pathology: 病理检查内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Pathology: :class:`tencentcloud.mrs.v20200910.models.Pathology`\n        """
        self.KindSet = None
        self.BasicInfo = None
        self.PersonalInfo = None
        self.TestList = None
        self.Inspection = None
        self.CaseHistory = None
        self.Pathology = None


    def _deserialize(self, params):
        if params.get("KindSet") is not None:
            self.KindSet = []
            for item in params.get("KindSet"):
                obj = KindItem()
                obj._deserialize(item)
                self.KindSet.append(obj)
        if params.get("BasicInfo") is not None:
            self.BasicInfo = BasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("PersonalInfo") is not None:
            self.PersonalInfo = PersonalInfo()
            self.PersonalInfo._deserialize(params.get("PersonalInfo"))
        if params.get("TestList") is not None:
            self.TestList = []
            for item in params.get("TestList"):
                obj = TestItem()
                obj._deserialize(item)
                self.TestList.append(obj)
        if params.get("Inspection") is not None:
            self.Inspection = Inspection()
            self.Inspection._deserialize(params.get("Inspection"))
        if params.get("CaseHistory") is not None:
            self.CaseHistory = CaseHistory()
            self.CaseHistory._deserialize(params.get("CaseHistory"))
        if params.get("Pathology") is not None:
            self.Pathology = Pathology()
            self.Pathology._deserialize(params.get("Pathology"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToClassRequest(AbstractModel):
    """TextToClass请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 报告文本\n        :type Text: str\n        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToClassResponse(AbstractModel):
    """TextToClass返回参数结构体

    """

    def __init__(self):
        """
        :param TextTypeList: 分类结果\n        :type TextTypeList: list of TextType\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TextTypeList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextTypeList") is not None:
            self.TextTypeList = []
            for item in params.get("TextTypeList"):
                obj = TextType()
                obj._deserialize(item)
                self.TextTypeList.append(obj)
        self.RequestId = params.get("RequestId")


class TextToObjectRequest(AbstractModel):
    """TextToObject请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 报告文本\n        :type Text: str\n        :param Type: 报告类型，目前支持12（检查报告），15（病理报告），28（出院报告），29（入院报告），210（门诊病历），212（手术记录），218（诊断证明）。如果不清楚报告类型，可以使用分类引擎，该字段传0（同时IsUsedClassify字段必须为True，否则无法输出结果）\n        :type Type: int\n        :param IsUsedClassify: 是否使用分类引擎，当不确定报告类型时，可以使用收费的报告分类引擎服务。若该字段为False，则Type字段不能为0，否则无法输出结果。
注意：当 IsUsedClassify 为True 时，表示使用收费的报告分类服务，将会产生额外的费用，具体收费标准参见 [购买指南的产品价格](https://cloud.tencent.com/document/product/1314/54264)。\n        :type IsUsedClassify: bool\n        """
        self.Text = None
        self.Type = None
        self.IsUsedClassify = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Type = params.get("Type")
        self.IsUsedClassify = params.get("IsUsedClassify")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToObjectResponse(AbstractModel):
    """TextToObject返回参数结构体

    """

    def __init__(self):
        """
        :param Template: 报告结构化结果\n        :type Template: :class:`tencentcloud.mrs.v20200910.models.Template`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = Template()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class TextType(AbstractModel):
    """文本类型

    """

    def __init__(self):
        """
        :param Id: 类别Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type Id: int\n        :param Level: 类别层级
注意：此字段可能返回 null，表示取不到有效值。\n        :type Level: int\n        :param Name: 类别名
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        """
        self.Id = None
        self.Level = None
        self.Name = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Level = params.get("Level")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Treatment(AbstractModel):
    """诊治信息

    """

    def __init__(self):
        """
        :param ChiefComplaint: 主诉
注意：此字段可能返回 null，表示取不到有效值。\n        :type ChiefComplaint: str\n        :param AdmissionDiagnosis: 入院诊断
注意：此字段可能返回 null，表示取不到有效值。\n        :type AdmissionDiagnosis: str\n        """
        self.ChiefComplaint = None
        self.AdmissionDiagnosis = None


    def _deserialize(self, params):
        self.ChiefComplaint = params.get("ChiefComplaint")
        self.AdmissionDiagnosis = params.get("AdmissionDiagnosis")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TreatmentRecord(AbstractModel):
    """病历

    """

    def __init__(self):
        """
        :param DmissionCondition: 入院
注意：此字段可能返回 null，表示取不到有效值。\n        :type DmissionCondition: str\n        :param ChiefComplaint: 主诉
注意：此字段可能返回 null，表示取不到有效值。\n        :type ChiefComplaint: str\n        :param DiseasePresent: 现病史
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiseasePresent: str\n        :param SymptomsAndSigns: 主要症状体征
注意：此字段可能返回 null，表示取不到有效值。\n        :type SymptomsAndSigns: str\n        :param AuxiliaryExamination: 辅助检查
注意：此字段可能返回 null，表示取不到有效值。\n        :type AuxiliaryExamination: str\n        :param BodyExamination: 体格检查
注意：此字段可能返回 null，表示取不到有效值。\n        :type BodyExamination: str\n        :param SpecialistExamination: 专科检查
注意：此字段可能返回 null，表示取不到有效值。\n        :type SpecialistExamination: str\n        :param MentalExamination: 精神检查
注意：此字段可能返回 null，表示取不到有效值。\n        :type MentalExamination: str\n        :param CheckRecord: 检查记录
注意：此字段可能返回 null，表示取不到有效值。\n        :type CheckRecord: str\n        :param InspectResult: 化验结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type InspectResult: str\n        :param IncisionHealing: 切口愈合情况
注意：此字段可能返回 null，表示取不到有效值。\n        :type IncisionHealing: str\n        :param TreatmentSuggestion: 处理意见
注意：此字段可能返回 null，表示取不到有效值。\n        :type TreatmentSuggestion: str\n        :param FollowUpRequirements: 门诊随访要求
注意：此字段可能返回 null，表示取不到有效值。\n        :type FollowUpRequirements: str\n        :param CheckAndTreatmentProcess: 诊疗经过
注意：此字段可能返回 null，表示取不到有效值。\n        :type CheckAndTreatmentProcess: str\n        :param SurgeryCondition: 手术经过
注意：此字段可能返回 null，表示取不到有效值。\n        :type SurgeryCondition: str\n        :param ConditionChanges: 入院情况
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConditionChanges: str\n        :param DischargeCondition: 出院情况
注意：此字段可能返回 null，表示取不到有效值。\n        :type DischargeCondition: str\n        :param PTNM: pTNM信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type PTNM: str\n        :param PTNMM: pTNMM信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type PTNMM: str\n        :param PTNMN: pTNMN信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type PTNMN: str\n        :param PTNMT: pTNMT信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type PTNMT: str\n        :param ECOG: ECOG信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ECOG: str\n        :param NRS: NRS信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type NRS: str\n        :param KPS: KPS信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type KPS: str\n        :param DeathDate: 死亡日期
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeathDate: str\n        :param RelapseDate: 复发日期
注意：此字段可能返回 null，表示取不到有效值。\n        :type RelapseDate: str\n        :param ObservationDays: 观测天数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ObservationDays: str\n        """
        self.DmissionCondition = None
        self.ChiefComplaint = None
        self.DiseasePresent = None
        self.SymptomsAndSigns = None
        self.AuxiliaryExamination = None
        self.BodyExamination = None
        self.SpecialistExamination = None
        self.MentalExamination = None
        self.CheckRecord = None
        self.InspectResult = None
        self.IncisionHealing = None
        self.TreatmentSuggestion = None
        self.FollowUpRequirements = None
        self.CheckAndTreatmentProcess = None
        self.SurgeryCondition = None
        self.ConditionChanges = None
        self.DischargeCondition = None
        self.PTNM = None
        self.PTNMM = None
        self.PTNMN = None
        self.PTNMT = None
        self.ECOG = None
        self.NRS = None
        self.KPS = None
        self.DeathDate = None
        self.RelapseDate = None
        self.ObservationDays = None


    def _deserialize(self, params):
        self.DmissionCondition = params.get("DmissionCondition")
        self.ChiefComplaint = params.get("ChiefComplaint")
        self.DiseasePresent = params.get("DiseasePresent")
        self.SymptomsAndSigns = params.get("SymptomsAndSigns")
        self.AuxiliaryExamination = params.get("AuxiliaryExamination")
        self.BodyExamination = params.get("BodyExamination")
        self.SpecialistExamination = params.get("SpecialistExamination")
        self.MentalExamination = params.get("MentalExamination")
        self.CheckRecord = params.get("CheckRecord")
        self.InspectResult = params.get("InspectResult")
        self.IncisionHealing = params.get("IncisionHealing")
        self.TreatmentSuggestion = params.get("TreatmentSuggestion")
        self.FollowUpRequirements = params.get("FollowUpRequirements")
        self.CheckAndTreatmentProcess = params.get("CheckAndTreatmentProcess")
        self.SurgeryCondition = params.get("SurgeryCondition")
        self.ConditionChanges = params.get("ConditionChanges")
        self.DischargeCondition = params.get("DischargeCondition")
        self.PTNM = params.get("PTNM")
        self.PTNMM = params.get("PTNMM")
        self.PTNMN = params.get("PTNMN")
        self.PTNMT = params.get("PTNMT")
        self.ECOG = params.get("ECOG")
        self.NRS = params.get("NRS")
        self.KPS = params.get("KPS")
        self.DeathDate = params.get("DeathDate")
        self.RelapseDate = params.get("RelapseDate")
        self.ObservationDays = params.get("ObservationDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tuber(AbstractModel):
    """肿瘤结节

    """

    def __init__(self):
        """
        :param Part: 部位信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Part: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        :param Type: 类型信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        :param SizeList: 大小信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type SizeList: list of Attribute\n        :param Shape: 形态信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Shape: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        :param Edge: 边缘信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Edge: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        :param CDFI: CDFI信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type CDFI: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        :param Metabolism: 代谢信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Metabolism: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        :param LymphGland: 淋巴结信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type LymphGland: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        :param LymphDoor: 淋巴门信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type LymphDoor: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        :param SkinMedulla: 皮髓质信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type SkinMedulla: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        :param InnerEcho: 内部回声信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type InnerEcho: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        :param RearEcho: 外部回声信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type RearEcho: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        :param Envelope: 包膜信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Envelope: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        :param Calcification: 钙化信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Calcification: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        :param Enhancement: 强化信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Enhancement: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        :param AspectRatio: 纵横比信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type AspectRatio: :class:`tencentcloud.mrs.v20200910.models.Attribute`\n        """
        self.Part = None
        self.Type = None
        self.SizeList = None
        self.Shape = None
        self.Edge = None
        self.CDFI = None
        self.Metabolism = None
        self.LymphGland = None
        self.LymphDoor = None
        self.SkinMedulla = None
        self.InnerEcho = None
        self.RearEcho = None
        self.Envelope = None
        self.Calcification = None
        self.Enhancement = None
        self.AspectRatio = None


    def _deserialize(self, params):
        if params.get("Part") is not None:
            self.Part = Attribute()
            self.Part._deserialize(params.get("Part"))
        if params.get("Type") is not None:
            self.Type = Attribute()
            self.Type._deserialize(params.get("Type"))
        if params.get("SizeList") is not None:
            self.SizeList = []
            for item in params.get("SizeList"):
                obj = Attribute()
                obj._deserialize(item)
                self.SizeList.append(obj)
        if params.get("Shape") is not None:
            self.Shape = Attribute()
            self.Shape._deserialize(params.get("Shape"))
        if params.get("Edge") is not None:
            self.Edge = Attribute()
            self.Edge._deserialize(params.get("Edge"))
        if params.get("CDFI") is not None:
            self.CDFI = Attribute()
            self.CDFI._deserialize(params.get("CDFI"))
        if params.get("Metabolism") is not None:
            self.Metabolism = Attribute()
            self.Metabolism._deserialize(params.get("Metabolism"))
        if params.get("LymphGland") is not None:
            self.LymphGland = Attribute()
            self.LymphGland._deserialize(params.get("LymphGland"))
        if params.get("LymphDoor") is not None:
            self.LymphDoor = Attribute()
            self.LymphDoor._deserialize(params.get("LymphDoor"))
        if params.get("SkinMedulla") is not None:
            self.SkinMedulla = Attribute()
            self.SkinMedulla._deserialize(params.get("SkinMedulla"))
        if params.get("InnerEcho") is not None:
            self.InnerEcho = Attribute()
            self.InnerEcho._deserialize(params.get("InnerEcho"))
        if params.get("RearEcho") is not None:
            self.RearEcho = Attribute()
            self.RearEcho._deserialize(params.get("RearEcho"))
        if params.get("Envelope") is not None:
            self.Envelope = Attribute()
            self.Envelope._deserialize(params.get("Envelope"))
        if params.get("Calcification") is not None:
            self.Calcification = Attribute()
            self.Calcification._deserialize(params.get("Calcification"))
        if params.get("Enhancement") is not None:
            self.Enhancement = Attribute()
            self.Enhancement._deserialize(params.get("Enhancement"))
        if params.get("AspectRatio") is not None:
            self.AspectRatio = Attribute()
            self.AspectRatio._deserialize(params.get("AspectRatio"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TuberInfo(AbstractModel):
    """结节

    """

    def __init__(self):
        """
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。\n        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`\n        :param Size: 大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type Size: list of Size\n        :param Multiple: 多发
注意：此字段可能返回 null，表示取不到有效值。\n        :type Multiple: :class:`tencentcloud.mrs.v20200910.models.Multiple`\n        :param AspectRatio: 纵横比
注意：此字段可能返回 null，表示取不到有效值。\n        :type AspectRatio: :class:`tencentcloud.mrs.v20200910.models.AspectRatio`\n        :param Edge: 边缘
注意：此字段可能返回 null，表示取不到有效值。\n        :type Edge: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param InnerEcho: 内部回声
注意：此字段可能返回 null，表示取不到有效值。\n        :type InnerEcho: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param RearEcho: 外部回声
注意：此字段可能返回 null，表示取不到有效值。\n        :type RearEcho: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Elastic: 弹性质地
注意：此字段可能返回 null，表示取不到有效值。\n        :type Elastic: :class:`tencentcloud.mrs.v20200910.models.Elastic`\n        :param Shape: 形状
注意：此字段可能返回 null，表示取不到有效值。\n        :type Shape: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param ShapeAttr: 形态
注意：此字段可能返回 null，表示取不到有效值。\n        :type ShapeAttr: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param SkinMedulla: 皮髓质信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type SkinMedulla: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Trend: 变化趋势
注意：此字段可能返回 null，表示取不到有效值。\n        :type Trend: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Calcification: 钙化
注意：此字段可能返回 null，表示取不到有效值。\n        :type Calcification: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Envelope: 包膜
注意：此字段可能返回 null，表示取不到有效值。\n        :type Envelope: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Enhancement: 强化
注意：此字段可能返回 null，表示取不到有效值。\n        :type Enhancement: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param LymphEnlargement: 淋巴结
注意：此字段可能返回 null，表示取不到有效值。\n        :type LymphEnlargement: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param LymphDoor: 淋巴门
注意：此字段可能返回 null，表示取不到有效值。\n        :type LymphDoor: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Activity: 活动度
注意：此字段可能返回 null，表示取不到有效值。\n        :type Activity: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Operation: 手术情况
注意：此字段可能返回 null，表示取不到有效值。\n        :type Operation: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param CDFI: 血液cdfi
注意：此字段可能返回 null，表示取不到有效值。\n        :type CDFI: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Index: list of int\n        :param SizeStatus: 大小状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type SizeStatus: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param InnerEchoDistribution: 内部回声分布
注意：此字段可能返回 null，表示取不到有效值。\n        :type InnerEchoDistribution: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param InnerEchoType: 内部回声类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type InnerEchoType: list of BlockInfo\n        :param Outline: 轮廓
注意：此字段可能返回 null，表示取不到有效值。\n        :type Outline: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Structure: 结构
注意：此字段可能返回 null，表示取不到有效值。\n        :type Structure: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Density: 密度
注意：此字段可能返回 null，表示取不到有效值。\n        :type Density: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Vas: 血管
注意：此字段可能返回 null，表示取不到有效值。\n        :type Vas: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Cysticwall: 囊壁
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cysticwall: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param Capsule: 被膜
注意：此字段可能返回 null，表示取不到有效值。\n        :type Capsule: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`\n        :param IsthmusThicknese: 峡部厚度
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsthmusThicknese: :class:`tencentcloud.mrs.v20200910.models.Size`\n        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。\n        :type Src: str\n        """
        self.Type = None
        self.Part = None
        self.Size = None
        self.Multiple = None
        self.AspectRatio = None
        self.Edge = None
        self.InnerEcho = None
        self.RearEcho = None
        self.Elastic = None
        self.Shape = None
        self.ShapeAttr = None
        self.SkinMedulla = None
        self.Trend = None
        self.Calcification = None
        self.Envelope = None
        self.Enhancement = None
        self.LymphEnlargement = None
        self.LymphDoor = None
        self.Activity = None
        self.Operation = None
        self.CDFI = None
        self.Index = None
        self.SizeStatus = None
        self.InnerEchoDistribution = None
        self.InnerEchoType = None
        self.Outline = None
        self.Structure = None
        self.Density = None
        self.Vas = None
        self.Cysticwall = None
        self.Capsule = None
        self.IsthmusThicknese = None
        self.Src = None


    def _deserialize(self, params):
        if params.get("Type") is not None:
            self.Type = BlockInfo()
            self.Type._deserialize(params.get("Type"))
        if params.get("Part") is not None:
            self.Part = Part()
            self.Part._deserialize(params.get("Part"))
        if params.get("Size") is not None:
            self.Size = []
            for item in params.get("Size"):
                obj = Size()
                obj._deserialize(item)
                self.Size.append(obj)
        if params.get("Multiple") is not None:
            self.Multiple = Multiple()
            self.Multiple._deserialize(params.get("Multiple"))
        if params.get("AspectRatio") is not None:
            self.AspectRatio = AspectRatio()
            self.AspectRatio._deserialize(params.get("AspectRatio"))
        if params.get("Edge") is not None:
            self.Edge = BlockInfo()
            self.Edge._deserialize(params.get("Edge"))
        if params.get("InnerEcho") is not None:
            self.InnerEcho = BlockInfo()
            self.InnerEcho._deserialize(params.get("InnerEcho"))
        if params.get("RearEcho") is not None:
            self.RearEcho = BlockInfo()
            self.RearEcho._deserialize(params.get("RearEcho"))
        if params.get("Elastic") is not None:
            self.Elastic = Elastic()
            self.Elastic._deserialize(params.get("Elastic"))
        if params.get("Shape") is not None:
            self.Shape = BlockInfo()
            self.Shape._deserialize(params.get("Shape"))
        if params.get("ShapeAttr") is not None:
            self.ShapeAttr = BlockInfo()
            self.ShapeAttr._deserialize(params.get("ShapeAttr"))
        if params.get("SkinMedulla") is not None:
            self.SkinMedulla = BlockInfo()
            self.SkinMedulla._deserialize(params.get("SkinMedulla"))
        if params.get("Trend") is not None:
            self.Trend = BlockInfo()
            self.Trend._deserialize(params.get("Trend"))
        if params.get("Calcification") is not None:
            self.Calcification = BlockInfo()
            self.Calcification._deserialize(params.get("Calcification"))
        if params.get("Envelope") is not None:
            self.Envelope = BlockInfo()
            self.Envelope._deserialize(params.get("Envelope"))
        if params.get("Enhancement") is not None:
            self.Enhancement = BlockInfo()
            self.Enhancement._deserialize(params.get("Enhancement"))
        if params.get("LymphEnlargement") is not None:
            self.LymphEnlargement = BlockInfo()
            self.LymphEnlargement._deserialize(params.get("LymphEnlargement"))
        if params.get("LymphDoor") is not None:
            self.LymphDoor = BlockInfo()
            self.LymphDoor._deserialize(params.get("LymphDoor"))
        if params.get("Activity") is not None:
            self.Activity = BlockInfo()
            self.Activity._deserialize(params.get("Activity"))
        if params.get("Operation") is not None:
            self.Operation = BlockInfo()
            self.Operation._deserialize(params.get("Operation"))
        if params.get("CDFI") is not None:
            self.CDFI = BlockInfo()
            self.CDFI._deserialize(params.get("CDFI"))
        self.Index = params.get("Index")
        if params.get("SizeStatus") is not None:
            self.SizeStatus = BlockInfo()
            self.SizeStatus._deserialize(params.get("SizeStatus"))
        if params.get("InnerEchoDistribution") is not None:
            self.InnerEchoDistribution = BlockInfo()
            self.InnerEchoDistribution._deserialize(params.get("InnerEchoDistribution"))
        if params.get("InnerEchoType") is not None:
            self.InnerEchoType = []
            for item in params.get("InnerEchoType"):
                obj = BlockInfo()
                obj._deserialize(item)
                self.InnerEchoType.append(obj)
        if params.get("Outline") is not None:
            self.Outline = BlockInfo()
            self.Outline._deserialize(params.get("Outline"))
        if params.get("Structure") is not None:
            self.Structure = BlockInfo()
            self.Structure._deserialize(params.get("Structure"))
        if params.get("Density") is not None:
            self.Density = BlockInfo()
            self.Density._deserialize(params.get("Density"))
        if params.get("Vas") is not None:
            self.Vas = BlockInfo()
            self.Vas._deserialize(params.get("Vas"))
        if params.get("Cysticwall") is not None:
            self.Cysticwall = BlockInfo()
            self.Cysticwall._deserialize(params.get("Cysticwall"))
        if params.get("Capsule") is not None:
            self.Capsule = BlockInfo()
            self.Capsule._deserialize(params.get("Capsule"))
        if params.get("IsthmusThicknese") is not None:
            self.IsthmusThicknese = Size()
            self.IsthmusThicknese._deserialize(params.get("IsthmusThicknese"))
        self.Src = params.get("Src")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Value(AbstractModel):
    """值

    """

    def __init__(self):
        """
        :param Grade: 等级
注意：此字段可能返回 null，表示取不到有效值。\n        :type Grade: str\n        :param Percent: 百分比
注意：此字段可能返回 null，表示取不到有效值。\n        :type Percent: list of float\n        :param Positive: 阳性
注意：此字段可能返回 null，表示取不到有效值。\n        :type Positive: str\n        """
        self.Grade = None
        self.Percent = None
        self.Positive = None


    def _deserialize(self, params):
        self.Grade = params.get("Grade")
        self.Percent = params.get("Percent")
        self.Positive = params.get("Positive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        