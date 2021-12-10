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
        r"""
        :param Text: 文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        """
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
        r"""
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Number: 数值
注意：此字段可能返回 null，表示取不到有效值。
        :type Number: str
        :param Relation: 关系
注意：此字段可能返回 null，表示取不到有效值。
        :type Relation: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
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
        


class BiopsyPart(AbstractModel):
    """活检部位

    """

    def __init__(self):
        r"""
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        """
        self.Value = None
        self.Src = None


    def _deserialize(self, params):
        self.Value = params.get("Value")
        self.Src = params.get("Src")
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
        r"""
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Positive: 阳性
注意：此字段可能返回 null，表示取不到有效值。
        :type Positive: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
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
        


class Check(AbstractModel):
    """检查报告单

    """

    def __init__(self):
        r"""
        :param Desc: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: :class:`tencentcloud.mrs.v20200910.models.Desc`
        :param Summary: 结论
注意：此字段可能返回 null，表示取不到有效值。
        :type Summary: :class:`tencentcloud.mrs.v20200910.models.Summary`
        """
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
        


class Desc(AbstractModel):
    """描述

    """

    def __init__(self):
        r"""
        :param Text: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param Organ: 器官
注意：此字段可能返回 null，表示取不到有效值。
        :type Organ: list of Organ
        :param Tuber: 结节
注意：此字段可能返回 null，表示取不到有效值。
        :type Tuber: list of TuberInfo
        """
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
        r"""
        :param Advice: 建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Advice: :class:`tencentcloud.mrs.v20200910.models.Advice`
        :param Diagnosis: 诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type Diagnosis: list of DiagCertItem
        """
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
        r"""
        :param Text: 文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of str
        """
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
        r"""
        :param TableIndex: 表格位置
注意：此字段可能返回 null，表示取不到有效值。
        :type TableIndex: int
        :param OutDiagnosis: 出院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type OutDiagnosis: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param DiseaseCode: 疾病编码
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseaseCode: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param InStatus: 入院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type InStatus: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param OutStatus: 出院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type OutStatus: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        """
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
        


class DiseaseMedicalHistory(AbstractModel):
    """疾病史

    """

    def __init__(self):
        r"""
        :param MainDiseaseHistory: 主病史
注意：此字段可能返回 null，表示取不到有效值。
        :type MainDiseaseHistory: str
        :param AllergyHistory: 过敏史
注意：此字段可能返回 null，表示取不到有效值。
        :type AllergyHistory: str
        :param InfectHistory: 传染疾病史
注意：此字段可能返回 null，表示取不到有效值。
        :type InfectHistory: str
        :param OperationHistory: 手术史
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationHistory: str
        :param TransfusionHistory: 输血史
注意：此字段可能返回 null，表示取不到有效值。
        :type TransfusionHistory: str
        """
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
        


class EcgDescription(AbstractModel):
    """心电图详情

    """

    def __init__(self):
        r"""
        :param HeartRate: 心率
注意：此字段可能返回 null，表示取不到有效值。
        :type HeartRate: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param AuricularRate: 心房率
注意：此字段可能返回 null，表示取不到有效值。
        :type AuricularRate: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param VentricularRate: 心室率
注意：此字段可能返回 null，表示取不到有效值。
        :type VentricularRate: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param Rhythm: 节律
注意：此字段可能返回 null，表示取不到有效值。
        :type Rhythm: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param PDuration: P波时间
注意：此字段可能返回 null，表示取不到有效值。
        :type PDuration: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param QrsDuration: QRS时间
注意：此字段可能返回 null，表示取不到有效值。
        :type QrsDuration: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param QrsAxis: QRS电轴
注意：此字段可能返回 null，表示取不到有效值。
        :type QrsAxis: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param PRInterval: P-R间期
注意：此字段可能返回 null，表示取不到有效值。
        :type PRInterval: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param PPInterval: P-P间期
注意：此字段可能返回 null，表示取不到有效值。
        :type PPInterval: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param RRInterval: R-R间期
注意：此字段可能返回 null，表示取不到有效值。
        :type RRInterval: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param PJInterval: P-J间期
注意：此字段可能返回 null，表示取不到有效值。
        :type PJInterval: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param QTInterval: Q-T间期
注意：此字段可能返回 null，表示取不到有效值。
        :type QTInterval: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param QTCInterval: qt/qtc间期
注意：此字段可能返回 null，表示取不到有效值。
        :type QTCInterval: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param Rv5SV1Amplitude: RV5/SV1振幅
注意：此字段可能返回 null，表示取不到有效值。
        :type Rv5SV1Amplitude: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param Rv5AddSV1Amplitude: RV5+SV1振幅
注意：此字段可能返回 null，表示取不到有效值。
        :type Rv5AddSV1Amplitude: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param PRTAxis: PRT电轴
注意：此字段可能返回 null，表示取不到有效值。
        :type PRTAxis: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param Rv5Amplitude: RV5振幅
注意：此字段可能返回 null，表示取不到有效值。
        :type Rv5Amplitude: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param SV1Amplitude: SV1振幅
注意：此字段可能返回 null，表示取不到有效值。
        :type SV1Amplitude: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param RV6SV2: RV6/SV2
注意：此字段可能返回 null，表示取不到有效值。
        :type RV6SV2: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        :param PQRSTAxis: P/QRS/T电轴
注意：此字段可能返回 null，表示取不到有效值。
        :type PQRSTAxis: :class:`tencentcloud.mrs.v20200910.models.EcgItem`
        """
        self.HeartRate = None
        self.AuricularRate = None
        self.VentricularRate = None
        self.Rhythm = None
        self.PDuration = None
        self.QrsDuration = None
        self.QrsAxis = None
        self.PRInterval = None
        self.PPInterval = None
        self.RRInterval = None
        self.PJInterval = None
        self.QTInterval = None
        self.QTCInterval = None
        self.Rv5SV1Amplitude = None
        self.Rv5AddSV1Amplitude = None
        self.PRTAxis = None
        self.Rv5Amplitude = None
        self.SV1Amplitude = None
        self.RV6SV2 = None
        self.PQRSTAxis = None


    def _deserialize(self, params):
        if params.get("HeartRate") is not None:
            self.HeartRate = EcgItem()
            self.HeartRate._deserialize(params.get("HeartRate"))
        if params.get("AuricularRate") is not None:
            self.AuricularRate = EcgItem()
            self.AuricularRate._deserialize(params.get("AuricularRate"))
        if params.get("VentricularRate") is not None:
            self.VentricularRate = EcgItem()
            self.VentricularRate._deserialize(params.get("VentricularRate"))
        if params.get("Rhythm") is not None:
            self.Rhythm = EcgItem()
            self.Rhythm._deserialize(params.get("Rhythm"))
        if params.get("PDuration") is not None:
            self.PDuration = EcgItem()
            self.PDuration._deserialize(params.get("PDuration"))
        if params.get("QrsDuration") is not None:
            self.QrsDuration = EcgItem()
            self.QrsDuration._deserialize(params.get("QrsDuration"))
        if params.get("QrsAxis") is not None:
            self.QrsAxis = EcgItem()
            self.QrsAxis._deserialize(params.get("QrsAxis"))
        if params.get("PRInterval") is not None:
            self.PRInterval = EcgItem()
            self.PRInterval._deserialize(params.get("PRInterval"))
        if params.get("PPInterval") is not None:
            self.PPInterval = EcgItem()
            self.PPInterval._deserialize(params.get("PPInterval"))
        if params.get("RRInterval") is not None:
            self.RRInterval = EcgItem()
            self.RRInterval._deserialize(params.get("RRInterval"))
        if params.get("PJInterval") is not None:
            self.PJInterval = EcgItem()
            self.PJInterval._deserialize(params.get("PJInterval"))
        if params.get("QTInterval") is not None:
            self.QTInterval = EcgItem()
            self.QTInterval._deserialize(params.get("QTInterval"))
        if params.get("QTCInterval") is not None:
            self.QTCInterval = EcgItem()
            self.QTCInterval._deserialize(params.get("QTCInterval"))
        if params.get("Rv5SV1Amplitude") is not None:
            self.Rv5SV1Amplitude = EcgItem()
            self.Rv5SV1Amplitude._deserialize(params.get("Rv5SV1Amplitude"))
        if params.get("Rv5AddSV1Amplitude") is not None:
            self.Rv5AddSV1Amplitude = EcgItem()
            self.Rv5AddSV1Amplitude._deserialize(params.get("Rv5AddSV1Amplitude"))
        if params.get("PRTAxis") is not None:
            self.PRTAxis = EcgItem()
            self.PRTAxis._deserialize(params.get("PRTAxis"))
        if params.get("Rv5Amplitude") is not None:
            self.Rv5Amplitude = EcgItem()
            self.Rv5Amplitude._deserialize(params.get("Rv5Amplitude"))
        if params.get("SV1Amplitude") is not None:
            self.SV1Amplitude = EcgItem()
            self.SV1Amplitude._deserialize(params.get("SV1Amplitude"))
        if params.get("RV6SV2") is not None:
            self.RV6SV2 = EcgItem()
            self.RV6SV2._deserialize(params.get("RV6SV2"))
        if params.get("PQRSTAxis") is not None:
            self.PQRSTAxis = EcgItem()
            self.PQRSTAxis._deserialize(params.get("PQRSTAxis"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EcgDiagnosis(AbstractModel):
    """心电图诊断

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of str
        """
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
        


class EcgItem(AbstractModel):
    """心电图指标项

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        """
        self.Name = None
        self.Value = None
        self.Unit = None
        self.Src = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Unit = params.get("Unit")
        self.Src = params.get("Src")
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
        r"""
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Score: 分数
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
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
        


class Electrocardiogram(AbstractModel):
    """心电图

    """

    def __init__(self):
        r"""
        :param EcgDescription: 心电图详情
注意：此字段可能返回 null，表示取不到有效值。
        :type EcgDescription: :class:`tencentcloud.mrs.v20200910.models.EcgDescription`
        :param EcgDiagnosis: 心电图诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type EcgDiagnosis: :class:`tencentcloud.mrs.v20200910.models.EcgDiagnosis`
        """
        self.EcgDescription = None
        self.EcgDiagnosis = None


    def _deserialize(self, params):
        if params.get("EcgDescription") is not None:
            self.EcgDescription = EcgDescription()
            self.EcgDescription._deserialize(params.get("EcgDescription"))
        if params.get("EcgDiagnosis") is not None:
            self.EcgDiagnosis = EcgDiagnosis()
            self.EcgDiagnosis._deserialize(params.get("EcgDiagnosis"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Endoscopy(AbstractModel):
    """内窥镜报告

    """

    def __init__(self):
        r"""
        :param BiopsyPart: 活检部位
注意：此字段可能返回 null，表示取不到有效值。
        :type BiopsyPart: :class:`tencentcloud.mrs.v20200910.models.BiopsyPart`
        :param Desc: 可见描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: :class:`tencentcloud.mrs.v20200910.models.EndoscopyDesc`
        :param Summary: 结论
注意：此字段可能返回 null，表示取不到有效值。
        :type Summary: :class:`tencentcloud.mrs.v20200910.models.Summary`
        """
        self.BiopsyPart = None
        self.Desc = None
        self.Summary = None


    def _deserialize(self, params):
        if params.get("BiopsyPart") is not None:
            self.BiopsyPart = BiopsyPart()
            self.BiopsyPart._deserialize(params.get("BiopsyPart"))
        if params.get("Desc") is not None:
            self.Desc = EndoscopyDesc()
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
        


class EndoscopyDesc(AbstractModel):
    """内窥镜描述

    """

    def __init__(self):
        r"""
        :param Text: 描述内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param Organ: 器官
注意：此字段可能返回 null，表示取不到有效值。
        :type Organ: list of EndoscopyOrgan
        """
        self.Text = None
        self.Organ = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        if params.get("Organ") is not None:
            self.Organ = []
            for item in params.get("Organ"):
                obj = EndoscopyOrgan()
                obj._deserialize(item)
                self.Organ.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndoscopyOrgan(AbstractModel):
    """内窥部位

    """

    def __init__(self):
        r"""
        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param PartAlias: 部位别名
注意：此字段可能返回 null，表示取不到有效值。
        :type PartAlias: str
        :param SymDescList: 症状描述
注意：此字段可能返回 null，表示取不到有效值。
        :type SymDescList: list of BlockInfo
        """
        self.Part = None
        self.Index = None
        self.Src = None
        self.PartAlias = None
        self.SymDescList = None


    def _deserialize(self, params):
        if params.get("Part") is not None:
            self.Part = Part()
            self.Part._deserialize(params.get("Part"))
        self.Index = params.get("Index")
        self.Src = params.get("Src")
        self.PartAlias = params.get("PartAlias")
        if params.get("SymDescList") is not None:
            self.SymDescList = []
            for item in params.get("SymDescList"):
                obj = BlockInfo()
                obj._deserialize(item)
                self.SymDescList.append(obj)
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
        r"""
        :param RelativeHistory: 家族成员史
注意：此字段可能返回 null，表示取不到有效值。
        :type RelativeHistory: str
        :param RelativeCancerHistory: 家族肿瘤史
注意：此字段可能返回 null，表示取不到有效值。
        :type RelativeCancerHistory: str
        :param GeneticHistory: 家族遗传史
注意：此字段可能返回 null，表示取不到有效值。
        :type GeneticHistory: str
        """
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
        


class FirstPage(AbstractModel):
    """病案首页

    """

    def __init__(self):
        r"""
        :param DischargeDiagnosis: 出入院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeDiagnosis: list of DischargeDiagnosis
        :param PathologicalDiagnosis: 病理诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type PathologicalDiagnosis: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param ClinicalDiagnosis: 临床诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type ClinicalDiagnosis: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        """
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
        r"""
        :param OcrEngineType: ocr引擎
        :type OcrEngineType: int
        :param IsReturnText: 是否返回分行文本内容
        :type IsReturnText: bool
        :param RotateTheAngle: 顺时针旋转角度
        :type RotateTheAngle: float
        :param AutoFitDirection: 自动适配方向,仅支持优图引擎
        :type AutoFitDirection: bool
        :param AutoOptimizeCoordinate: 坐标优化
        :type AutoOptimizeCoordinate: bool
        :param IsScale: 是否开启图片压缩，开启时imageOriginalSize必须正确填写
        :type IsScale: bool
        :param ImageOriginalSize: 原始图片大小(单位byes),用来判断该图片是否需要压缩
        :type ImageOriginalSize: int
        :param ScaleTargetSize: 采用后台默认值(2048Kb)
        :type ScaleTargetSize: int
        """
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
        


class HistologyLevel(AbstractModel):
    """组织学等级

    """

    def __init__(self):
        r"""
        :param Grade: 等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Grade: str
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        """
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
        r"""
        :param Infiltration: 浸润
注意：此字段可能返回 null，表示取不到有效值。
        :type Infiltration: str
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
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
        r"""
        :param AdmissionTime: 入院时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionTime: str
        :param DischargeTime: 出院时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeTime: str
        :param AdmissionDays: 住院天数
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionDays: str
        :param AdmissionDignosis: 入院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionDignosis: str
        :param AdmissionCondition: 入院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionCondition: str
        :param DiagnosisTreatment: 诊疗经过
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagnosisTreatment: str
        :param DischargeDiagnosis: 出院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeDiagnosis: str
        :param DischargeInstruction: 出院医嘱
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeInstruction: str
        """
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
        


class IHCInfo(AbstractModel):
    """Ihc信息

    """

    def __init__(self):
        r"""
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 值
        :type Value: :class:`tencentcloud.mrs.v20200910.models.Value`
        """
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
        r"""
        :param Id: 图片id
        :type Id: int
        :param Url: 图片url
        :type Url: str
        :param Base64: 图片base64编码
        :type Base64: str
        """
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
        


class ImageToClassRequest(AbstractModel):
    """ImageToClass请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageInfoList: 图片列表，允许传入多张图片，支持传入图片的base64编码，暂不支持图片url
        :type ImageInfoList: list of ImageInfo
        :param HandleParam: 图片处理参数
        :type HandleParam: :class:`tencentcloud.mrs.v20200910.models.HandleParam`
        :param Type: 不填，默认为0
        :type Type: int
        """
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
        r"""
        :param TextTypeList: 分类结果
注意：此字段可能返回 null，表示取不到有效值。
        :type TextTypeList: list of TextType
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param ImageInfoList: 图片列表，允许传入多张图片，目前只支持传入图片base64编码，图片url暂不支持
        :type ImageInfoList: list of ImageInfo
        :param HandleParam: 图片处理参数
        :type HandleParam: :class:`tencentcloud.mrs.v20200910.models.HandleParam`
        :param Type: 报告类型，目前支持11（检验报告），12（检查报告），15（病理报告），28（出院报告），29（入院报告），210（门诊病历），212（手术记录），218（诊断证明），363（心电图），27（内窥镜检查），215（处方单），219（免疫接种证明），301（C14呼气试验）。如果不清楚报告类型，可以使用分类引擎，该字段传0（同时IsUsedClassify字段必须为True，否则无法输出结果）
        :type Type: int
        :param IsUsedClassify: 是否使用分类引擎，当不确定报告类型时，可以使用收费的报告分类引擎服务。若该字段为 False，则 Type 字段不能为 0，否则无法输出结果。
注意：当 IsUsedClassify 为True 时，表示使用收费的报告分类服务，将会产生额外的费用，具体收费标准参见 [购买指南的产品价格](https://cloud.tencent.com/document/product/1314/54264)。
        :type IsUsedClassify: bool
        """
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
        r"""
        :param Template: 报告结构化结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Template: :class:`tencentcloud.mrs.v20200910.models.Template`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Indicators: 检验指标项
注意：此字段可能返回 null，表示取不到有效值。
        :type Indicators: list of IndicatorItem
        """
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
        r"""
        :param Code: 英文缩写
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param Scode: 标准缩写
注意：此字段可能返回 null，表示取不到有效值。
        :type Scode: str
        :param Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Sname: 标准名
注意：此字段可能返回 null，表示取不到有效值。
        :type Sname: str
        :param Result: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param Range: 参考范围
注意：此字段可能返回 null，表示取不到有效值。
        :type Range: str
        :param Arrow: 上下箭头
注意：此字段可能返回 null，表示取不到有效值。
        :type Arrow: str
        :param Normal: 是否正常
注意：此字段可能返回 null，表示取不到有效值。
        :type Normal: bool
        :param ItemString: 项目原文
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemString: str
        """
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
        


class Invas(AbstractModel):
    """侵犯扩散

    """

    def __init__(self):
        r"""
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param Positive: 阳性
注意：此字段可能返回 null，表示取不到有效值。
        :type Positive: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        """
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
        


class Lymph(AbstractModel):
    """淋巴

    """

    def __init__(self):
        r"""
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param TransferNum: 转移数
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferNum: int
        """
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
        


class MedDoc(AbstractModel):
    """医学资料

    """

    def __init__(self):
        r"""
        :param Advice: 建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Advice: :class:`tencentcloud.mrs.v20200910.models.Advice`
        :param Diagnosis: 诊断结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Diagnosis: list of DiagCertItem
        :param DiseaseMedicalHistory: 疾病史
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseaseMedicalHistory: :class:`tencentcloud.mrs.v20200910.models.DiseaseMedicalHistory`
        :param PersonalMedicalHistory: 个人史
        :type PersonalMedicalHistory: :class:`tencentcloud.mrs.v20200910.models.PersonalMedicalHistory`
        :param ObstericalMedicalHistory: 婚孕史
        :type ObstericalMedicalHistory: :class:`tencentcloud.mrs.v20200910.models.ObstericalMedicalHistory`
        :param FamilyMedicalHistory: 家族史
        :type FamilyMedicalHistory: :class:`tencentcloud.mrs.v20200910.models.FamilyMedicalHistory`
        :param MenstrualMedicalHistory: 月经史
        :type MenstrualMedicalHistory: :class:`tencentcloud.mrs.v20200910.models.MenstrualMedicalHistory`
        :param TreatmentRecord: 诊疗记录
        :type TreatmentRecord: :class:`tencentcloud.mrs.v20200910.models.TreatmentRecord`
        """
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
        r"""
        :param DiagnosisTime: 就诊日期
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagnosisTime: str
        :param DiagnosisDepartmentName: 就诊科室
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagnosisDepartmentName: str
        :param DiagnosisDoctorName: 就诊医生
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagnosisDoctorName: str
        :param ClinicalDiagnosis: 临床诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type ClinicalDiagnosis: str
        :param MainNarration: 主述
注意：此字段可能返回 null，表示取不到有效值。
        :type MainNarration: str
        :param PhysicalExamination: 体格检查
注意：此字段可能返回 null，表示取不到有效值。
        :type PhysicalExamination: str
        :param InspectionFindings: 检查结论
注意：此字段可能返回 null，表示取不到有效值。
        :type InspectionFindings: str
        :param TreatmentOpinion: 治疗意见
注意：此字段可能返回 null，表示取不到有效值。
        :type TreatmentOpinion: str
        """
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
        


class Medicine(AbstractModel):
    """药品

    """

    def __init__(self):
        r"""
        :param Name: 药品名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param TradeName: 商品名
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeName: str
        :param Firm: 厂商
注意：此字段可能返回 null，表示取不到有效值。
        :type Firm: str
        :param Category: 医保类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Category: str
        :param Specification: 规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Specification: str
        :param MinQuantity: 最小包装数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MinQuantity: str
        :param DosageUnit: 最小制剂单位
注意：此字段可能返回 null，表示取不到有效值。
        :type DosageUnit: str
        :param PackingUnit: 最小包装单位
注意：此字段可能返回 null，表示取不到有效值。
        :type PackingUnit: str
        """
        self.Name = None
        self.TradeName = None
        self.Firm = None
        self.Category = None
        self.Specification = None
        self.MinQuantity = None
        self.DosageUnit = None
        self.PackingUnit = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TradeName = params.get("TradeName")
        self.Firm = params.get("Firm")
        self.Category = params.get("Category")
        self.Specification = params.get("Specification")
        self.MinQuantity = params.get("MinQuantity")
        self.DosageUnit = params.get("DosageUnit")
        self.PackingUnit = params.get("PackingUnit")
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
        r"""
        :param LastMenstrualPeriod: 末次月经时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastMenstrualPeriod: str
        :param MenstrualFlow: 经量
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstrualFlow: str
        :param MenarcheAge: 月经初潮年龄
注意：此字段可能返回 null，表示取不到有效值。
        :type MenarcheAge: str
        :param MenstruationOrNot: 是否来月经
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstruationOrNot: str
        :param MenstrualCycles: 月经周期
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstrualCycles: str
        :param MenstrualPeriod: 月经持续天数
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstrualPeriod: str
        """
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
        


class Multiple(AbstractModel):
    """多发

    """

    def __init__(self):
        r"""
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Count: 数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
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
        r"""
        :param Part: 部位值
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: str
        :param PartDirection: 部位方向
注意：此字段可能返回 null，表示取不到有效值。
        :type PartDirection: str
        :param Tissue: 组织值
注意：此字段可能返回 null，表示取不到有效值。
        :type Tissue: str
        :param TissueDirection: 组织方向
注意：此字段可能返回 null，表示取不到有效值。
        :type TissueDirection: str
        :param Upper: 上级部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Upper: str
        """
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
        r"""
        :param Number: 数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Number: list of str
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        """
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
        r"""
        :param MarriageHistory: 婚史
注意：此字段可能返回 null，表示取不到有效值。
        :type MarriageHistory: str
        :param FertilityHistory: 孕史
注意：此字段可能返回 null，表示取不到有效值。
        :type FertilityHistory: str
        """
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
        r"""
        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param Size: 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: list of Size
        :param Envelope: 包膜
注意：此字段可能返回 null，表示取不到有效值。
        :type Envelope: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Edge: 边缘
注意：此字段可能返回 null，表示取不到有效值。
        :type Edge: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param InnerEcho: 内部回声
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerEcho: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Gland: 腺体
注意：此字段可能返回 null，表示取不到有效值。
        :type Gland: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Shape: 形状
注意：此字段可能返回 null，表示取不到有效值。
        :type Shape: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Thickness: 厚度
注意：此字段可能返回 null，表示取不到有效值。
        :type Thickness: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param ShapeAttr: 形态
注意：此字段可能返回 null，表示取不到有效值。
        :type ShapeAttr: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param CDFI: 血液cdfi
注意：此字段可能返回 null，表示取不到有效值。
        :type CDFI: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param SymDesc: 描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SymDesc: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param SizeStatus: 大小状态
注意：此字段可能返回 null，表示取不到有效值。
        :type SizeStatus: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Outline: 轮廓
注意：此字段可能返回 null，表示取不到有效值。
        :type Outline: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Structure: 结构
注意：此字段可能返回 null，表示取不到有效值。
        :type Structure: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Density: 密度
注意：此字段可能返回 null，表示取不到有效值。
        :type Density: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Vas: 血管
注意：此字段可能返回 null，表示取不到有效值。
        :type Vas: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Cysticwall: 囊壁
注意：此字段可能返回 null，表示取不到有效值。
        :type Cysticwall: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Capsule: 被膜
注意：此字段可能返回 null，表示取不到有效值。
        :type Capsule: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param IsthmusThicknese: 峡部厚度
注意：此字段可能返回 null，表示取不到有效值。
        :type IsthmusThicknese: :class:`tencentcloud.mrs.v20200910.models.Size`
        :param InnerEchoDistribution: 内部回声分布
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerEchoDistribution: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        """
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
        r"""
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param NormPart: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type NormPart: :class:`tencentcloud.mrs.v20200910.models.NormPart`
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
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
        


class PathologyReport(AbstractModel):
    """病理报告

    """

    def __init__(self):
        r"""
        :param CancerPart: 癌症部位
注意：此字段可能返回 null，表示取不到有效值。
        :type CancerPart: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param CancerSize: 癌症部位大小
注意：此字段可能返回 null，表示取不到有效值。
        :type CancerSize: list of Size
        :param DescText: 描述文本
注意：此字段可能返回 null，表示取不到有效值。
        :type DescText: str
        :param HistologyLevel: 组织学等级
注意：此字段可能返回 null，表示取不到有效值。
        :type HistologyLevel: :class:`tencentcloud.mrs.v20200910.models.HistologyLevel`
        :param HistologyType: 组织学类型
注意：此字段可能返回 null，表示取不到有效值。
        :type HistologyType: :class:`tencentcloud.mrs.v20200910.models.HistologyType`
        :param IHC: IHC信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IHC: list of IHCInfo
        :param InfiltrationDepth: 浸润深度
注意：此字段可能返回 null，表示取不到有效值。
        :type InfiltrationDepth: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Invasive: 肿瘤扩散
注意：此字段可能返回 null，表示取不到有效值。
        :type Invasive: list of Invas
        :param LymphNodes: 淋巴结
注意：此字段可能返回 null，表示取不到有效值。
        :type LymphNodes: list of Lymph
        :param PTNM: PTNM信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNM: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param PathologicalReportType: 病理报告类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PathologicalReportType: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param ReportText: 报告原文
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportText: str
        :param SampleType: 标本类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleType: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param SummaryText: 结论文本
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryText: str
        """
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
        r"""
        :param Name: 患者姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Sex: 患者性别
注意：此字段可能返回 null，表示取不到有效值。
        :type Sex: str
        :param Age: 患者年龄
注意：此字段可能返回 null，表示取不到有效值。
        :type Age: str
        :param Phone: 患者手机号码
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param Address: 患者地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param IdCard: 患者身份证
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCard: str
        :param HealthCardNo: 健康卡号
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCardNo: str
        :param SocialSecurityCardNo: 社保卡号
注意：此字段可能返回 null，表示取不到有效值。
        :type SocialSecurityCardNo: str
        :param Birthday: 出生日期
注意：此字段可能返回 null，表示取不到有效值。
        :type Birthday: str
        :param Ethnicity: 民族
注意：此字段可能返回 null，表示取不到有效值。
        :type Ethnicity: str
        :param Married: 婚姻状况
注意：此字段可能返回 null，表示取不到有效值。
        :type Married: str
        :param Profession: 职业
注意：此字段可能返回 null，表示取不到有效值。
        :type Profession: str
        :param EducationBackground: 教育程度
注意：此字段可能返回 null，表示取不到有效值。
        :type EducationBackground: str
        :param Nationality: 国籍
注意：此字段可能返回 null，表示取不到有效值。
        :type Nationality: str
        :param BirthPlace: 籍贯
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthPlace: str
        :param MedicalInsuranceType: 医保类型
注意：此字段可能返回 null，表示取不到有效值。
        :type MedicalInsuranceType: str
        :param AgeNorm: 标准化年龄
注意：此字段可能返回 null，表示取不到有效值。
        :type AgeNorm: str
        :param Nation: 民族
注意：此字段可能返回 null，表示取不到有效值。
        :type Nation: str
        :param MarriedCode: 婚姻代码
注意：此字段可能返回 null，表示取不到有效值。
        :type MarriedCode: str
        :param ProfessionCode: 职业代码
注意：此字段可能返回 null，表示取不到有效值。
        :type ProfessionCode: str
        :param MedicalInsuranceTypeCode: 居民医保代码
注意：此字段可能返回 null，表示取不到有效值。
        :type MedicalInsuranceTypeCode: str
        """
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
        self.AgeNorm = None
        self.Nation = None
        self.MarriedCode = None
        self.ProfessionCode = None
        self.MedicalInsuranceTypeCode = None


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
        self.AgeNorm = params.get("AgeNorm")
        self.Nation = params.get("Nation")
        self.MarriedCode = params.get("MarriedCode")
        self.ProfessionCode = params.get("ProfessionCode")
        self.MedicalInsuranceTypeCode = params.get("MedicalInsuranceTypeCode")
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
        r"""
        :param BirthPlace: 出生史
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthPlace: str
        :param LivePlace: 居住史
注意：此字段可能返回 null，表示取不到有效值。
        :type LivePlace: str
        :param Job: 工作史
注意：此字段可能返回 null，表示取不到有效值。
        :type Job: str
        :param SmokeHistory: 吸烟史
注意：此字段可能返回 null，表示取不到有效值。
        :type SmokeHistory: str
        :param AlcoholicHistory: 饮酒史
注意：此字段可能返回 null，表示取不到有效值。
        :type AlcoholicHistory: str
        """
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
        


class Prescription(AbstractModel):
    """处方单

    """

    def __init__(self):
        r"""
        :param MedicineList: 药品列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MedicineList: list of Medicine
        """
        self.MedicineList = None


    def _deserialize(self, params):
        if params.get("MedicineList") is not None:
            self.MedicineList = []
            for item in params.get("MedicineList"):
                obj = Medicine()
                obj._deserialize(item)
                self.MedicineList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportInfo(AbstractModel):
    """报告基本信息

    """

    def __init__(self):
        r"""
        :param Hospital: 医院名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Hospital: str
        :param DepartmentName: 科室名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DepartmentName: str
        :param BillingTime: 申请时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingTime: str
        :param ReportTime: 报告时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportTime: str
        :param InspectTime: 检查时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InspectTime: str
        :param CheckNum: 检查号
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckNum: str
        :param ImageNum: 影像号
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageNum: str
        :param RadiationNum: 放射号
注意：此字段可能返回 null，表示取不到有效值。
        :type RadiationNum: str
        :param TestNum: 检验号
注意：此字段可能返回 null，表示取不到有效值。
        :type TestNum: str
        :param OutpatientNum: 门诊号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutpatientNum: str
        :param PathologyNum: 病理号
注意：此字段可能返回 null，表示取不到有效值。
        :type PathologyNum: str
        :param InHospitalNum: 住院号
注意：此字段可能返回 null，表示取不到有效值。
        :type InHospitalNum: str
        :param SampleNum: 样本号
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleNum: str
        :param SampleType: 标本种类
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleType: str
        :param MedicalRecordNum: 病历号
注意：此字段可能返回 null，表示取不到有效值。
        :type MedicalRecordNum: str
        :param ReportName: 报告名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportName: str
        :param UltraNum: 超声号
注意：此字段可能返回 null，表示取不到有效值。
        :type UltraNum: str
        :param Diagnose: 临床诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type Diagnose: str
        """
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
        


class Size(AbstractModel):
    """大小

    """

    def __init__(self):
        r"""
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param NormSize: 标准大小
注意：此字段可能返回 null，表示取不到有效值。
        :type NormSize: :class:`tencentcloud.mrs.v20200910.models.NormSize`
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
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
        r"""
        :param Symptom: 症状
注意：此字段可能返回 null，表示取不到有效值。
        :type Symptom: list of SymptomInfo
        :param Text: 文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        """
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
        r"""
        :param SurgeryHistory: 手术史
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryHistory: :class:`tencentcloud.mrs.v20200910.models.SurgeryHistory`
        """
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
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
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
        r"""
        :param SurgeryName: 手术名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryName: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param SurgeryDate: 手术日期
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryDate: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param PreoperativePathology: 术前诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type PreoperativePathology: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param IntraoperativePathology: 术中诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type IntraoperativePathology: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param PostoperativePathology: 术后诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type PostoperativePathology: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param DischargeDiagnosis: 出院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeDiagnosis: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        """
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
        


class SymptomInfo(AbstractModel):
    """病症描述信息

    """

    def __init__(self):
        r"""
        :param Grade: 等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Grade: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Symptom: 病变
注意：此字段可能返回 null，表示取不到有效值。
        :type Symptom: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Attrs: 属性
注意：此字段可能返回 null，表示取不到有效值。
        :type Attrs: list of BlockInfo
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        """
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
        r"""
        :param PatientInfo: 患者信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PatientInfo: :class:`tencentcloud.mrs.v20200910.models.PatientInfo`
        :param ReportInfo: 报告信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportInfo: :class:`tencentcloud.mrs.v20200910.models.ReportInfo`
        :param Check: 检查报告
注意：此字段可能返回 null，表示取不到有效值。
        :type Check: :class:`tencentcloud.mrs.v20200910.models.Check`
        :param Pathology: 病理报告
注意：此字段可能返回 null，表示取不到有效值。
        :type Pathology: :class:`tencentcloud.mrs.v20200910.models.PathologyReport`
        :param MedDoc: 出院报告，入院报告，门诊病历
注意：此字段可能返回 null，表示取不到有效值。
        :type MedDoc: :class:`tencentcloud.mrs.v20200910.models.MedDoc`
        :param DiagCert: 诊断证明
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagCert: :class:`tencentcloud.mrs.v20200910.models.DiagCert`
        :param FirstPage: 病案首页
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstPage: :class:`tencentcloud.mrs.v20200910.models.FirstPage`
        :param Indicator: 检验报告
注意：此字段可能返回 null，表示取不到有效值。
        :type Indicator: :class:`tencentcloud.mrs.v20200910.models.Indicator`
        :param ReportType: 报告类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportType: str
        :param MedicalRecordInfo: 门诊病历信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MedicalRecordInfo: :class:`tencentcloud.mrs.v20200910.models.MedicalRecordInfo`
        :param Hospitalization: 出入院信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Hospitalization: :class:`tencentcloud.mrs.v20200910.models.Hospitalization`
        :param Surgery: 手术记录
注意：此字段可能返回 null，表示取不到有效值。
        :type Surgery: :class:`tencentcloud.mrs.v20200910.models.Surgery`
        :param Electrocardiogram: 心电图报告
注意：此字段可能返回 null，表示取不到有效值。
        :type Electrocardiogram: :class:`tencentcloud.mrs.v20200910.models.Electrocardiogram`
        :param Endoscopy: 内窥镜报告
注意：此字段可能返回 null，表示取不到有效值。
        :type Endoscopy: :class:`tencentcloud.mrs.v20200910.models.Endoscopy`
        :param Prescription: 处方单
注意：此字段可能返回 null，表示取不到有效值。
        :type Prescription: :class:`tencentcloud.mrs.v20200910.models.Prescription`
        :param VaccineCertificate: 免疫接种证明
注意：此字段可能返回 null，表示取不到有效值。
        :type VaccineCertificate: :class:`tencentcloud.mrs.v20200910.models.VaccineCertificate`
        :param OcrText: OCR文本
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrText: str
        """
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
        self.Electrocardiogram = None
        self.Endoscopy = None
        self.Prescription = None
        self.VaccineCertificate = None
        self.OcrText = None


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
        if params.get("Electrocardiogram") is not None:
            self.Electrocardiogram = Electrocardiogram()
            self.Electrocardiogram._deserialize(params.get("Electrocardiogram"))
        if params.get("Endoscopy") is not None:
            self.Endoscopy = Endoscopy()
            self.Endoscopy._deserialize(params.get("Endoscopy"))
        if params.get("Prescription") is not None:
            self.Prescription = Prescription()
            self.Prescription._deserialize(params.get("Prescription"))
        if params.get("VaccineCertificate") is not None:
            self.VaccineCertificate = VaccineCertificate()
            self.VaccineCertificate._deserialize(params.get("VaccineCertificate"))
        self.OcrText = params.get("OcrText")
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
        r"""
        :param Text: 报告文本
        :type Text: str
        """
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
        r"""
        :param TextTypeList: 分类结果
        :type TextTypeList: list of TextType
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Text: 报告文本
        :type Text: str
        :param Type: 报告类型，目前支持12（检查报告），15（病理报告），28（出院报告），29（入院报告），210（门诊病历），212（手术记录），218（诊断证明），363（心电图），27（内窥镜检查），215（处方单），219（免疫接种证明），301（C14呼气试验）。如果不清楚报告类型，可以使用分类引擎，该字段传0（同时IsUsedClassify字段必须为True，否则无法输出结果）
        :type Type: int
        :param IsUsedClassify: 是否使用分类引擎，当不确定报告类型时，可以使用收费的报告分类引擎服务。若该字段为False，则Type字段不能为0，否则无法输出结果。
注意：当 IsUsedClassify 为True 时，表示使用收费的报告分类服务，将会产生额外的费用，具体收费标准参见 [购买指南的产品价格](https://cloud.tencent.com/document/product/1314/54264)。
        :type IsUsedClassify: bool
        """
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
        r"""
        :param Template: 报告结构化结果
        :type Template: :class:`tencentcloud.mrs.v20200910.models.Template`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Id: 类别Id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param Level: 类别层级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param Name: 类别名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
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
        


class TreatmentRecord(AbstractModel):
    """病历

    """

    def __init__(self):
        r"""
        :param DmissionCondition: 入院
注意：此字段可能返回 null，表示取不到有效值。
        :type DmissionCondition: str
        :param ChiefComplaint: 主诉
注意：此字段可能返回 null，表示取不到有效值。
        :type ChiefComplaint: str
        :param DiseasePresent: 现病史
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseasePresent: str
        :param SymptomsAndSigns: 主要症状体征
注意：此字段可能返回 null，表示取不到有效值。
        :type SymptomsAndSigns: str
        :param AuxiliaryExamination: 辅助检查
注意：此字段可能返回 null，表示取不到有效值。
        :type AuxiliaryExamination: str
        :param BodyExamination: 体格检查
注意：此字段可能返回 null，表示取不到有效值。
        :type BodyExamination: str
        :param SpecialistExamination: 专科检查
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecialistExamination: str
        :param MentalExamination: 精神检查
注意：此字段可能返回 null，表示取不到有效值。
        :type MentalExamination: str
        :param CheckRecord: 检查记录
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckRecord: str
        :param InspectResult: 化验结果
注意：此字段可能返回 null，表示取不到有效值。
        :type InspectResult: str
        :param IncisionHealing: 切口愈合情况
注意：此字段可能返回 null，表示取不到有效值。
        :type IncisionHealing: str
        :param TreatmentSuggestion: 处理意见
注意：此字段可能返回 null，表示取不到有效值。
        :type TreatmentSuggestion: str
        :param FollowUpRequirements: 门诊随访要求
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowUpRequirements: str
        :param CheckAndTreatmentProcess: 诊疗经过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckAndTreatmentProcess: str
        :param SurgeryCondition: 手术经过
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryCondition: str
        :param ConditionChanges: 入院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionChanges: str
        :param DischargeCondition: 出院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeCondition: str
        :param PTNM: pTNM信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNM: str
        :param PTNMM: pTNMM信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNMM: str
        :param PTNMN: pTNMN信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNMN: str
        :param PTNMT: pTNMT信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNMT: str
        :param ECOG: ECOG信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ECOG: str
        :param NRS: NRS信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NRS: str
        :param KPS: KPS信息
注意：此字段可能返回 null，表示取不到有效值。
        :type KPS: str
        :param DeathDate: 死亡日期
注意：此字段可能返回 null，表示取不到有效值。
        :type DeathDate: str
        :param RelapseDate: 复发日期
注意：此字段可能返回 null，表示取不到有效值。
        :type RelapseDate: str
        :param ObservationDays: 观测天数
注意：此字段可能返回 null，表示取不到有效值。
        :type ObservationDays: str
        """
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
        


class TuberInfo(AbstractModel):
    """结节

    """

    def __init__(self):
        r"""
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param Size: 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: list of Size
        :param Multiple: 多发
注意：此字段可能返回 null，表示取不到有效值。
        :type Multiple: :class:`tencentcloud.mrs.v20200910.models.Multiple`
        :param AspectRatio: 纵横比
注意：此字段可能返回 null，表示取不到有效值。
        :type AspectRatio: :class:`tencentcloud.mrs.v20200910.models.AspectRatio`
        :param Edge: 边缘
注意：此字段可能返回 null，表示取不到有效值。
        :type Edge: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param InnerEcho: 内部回声
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerEcho: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param RearEcho: 外部回声
注意：此字段可能返回 null，表示取不到有效值。
        :type RearEcho: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Elastic: 弹性质地
注意：此字段可能返回 null，表示取不到有效值。
        :type Elastic: :class:`tencentcloud.mrs.v20200910.models.Elastic`
        :param Shape: 形状
注意：此字段可能返回 null，表示取不到有效值。
        :type Shape: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param ShapeAttr: 形态
注意：此字段可能返回 null，表示取不到有效值。
        :type ShapeAttr: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param SkinMedulla: 皮髓质信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SkinMedulla: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Trend: 变化趋势
注意：此字段可能返回 null，表示取不到有效值。
        :type Trend: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Calcification: 钙化
注意：此字段可能返回 null，表示取不到有效值。
        :type Calcification: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Envelope: 包膜
注意：此字段可能返回 null，表示取不到有效值。
        :type Envelope: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Enhancement: 强化
注意：此字段可能返回 null，表示取不到有效值。
        :type Enhancement: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param LymphEnlargement: 淋巴结
注意：此字段可能返回 null，表示取不到有效值。
        :type LymphEnlargement: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param LymphDoor: 淋巴门
注意：此字段可能返回 null，表示取不到有效值。
        :type LymphDoor: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Activity: 活动度
注意：此字段可能返回 null，表示取不到有效值。
        :type Activity: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Operation: 手术情况
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param CDFI: 血液cdfi
注意：此字段可能返回 null，表示取不到有效值。
        :type CDFI: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Index: 原文位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param SizeStatus: 大小状态
注意：此字段可能返回 null，表示取不到有效值。
        :type SizeStatus: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param InnerEchoDistribution: 内部回声分布
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerEchoDistribution: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param InnerEchoType: 内部回声类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerEchoType: list of BlockInfo
        :param Outline: 轮廓
注意：此字段可能返回 null，表示取不到有效值。
        :type Outline: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Structure: 结构
注意：此字段可能返回 null，表示取不到有效值。
        :type Structure: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Density: 密度
注意：此字段可能返回 null，表示取不到有效值。
        :type Density: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Vas: 血管
注意：此字段可能返回 null，表示取不到有效值。
        :type Vas: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Cysticwall: 囊壁
注意：此字段可能返回 null，表示取不到有效值。
        :type Cysticwall: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Capsule: 被膜
注意：此字段可能返回 null，表示取不到有效值。
        :type Capsule: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param IsthmusThicknese: 峡部厚度
注意：此字段可能返回 null，表示取不到有效值。
        :type IsthmusThicknese: :class:`tencentcloud.mrs.v20200910.models.Size`
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        """
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
        


class Vaccination(AbstractModel):
    """免疫接种记录

    """

    def __init__(self):
        r"""
        :param Id: 序号
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param Vaccine: 疫苗名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Vaccine: str
        :param Dose: 剂次
注意：此字段可能返回 null，表示取不到有效值。
        :type Dose: str
        :param Date: 接种日期
注意：此字段可能返回 null，表示取不到有效值。
        :type Date: str
        :param LotNumber: 疫苗批号
注意：此字段可能返回 null，表示取不到有效值。
        :type LotNumber: str
        :param Manufacturer: 生产企业
注意：此字段可能返回 null，表示取不到有效值。
        :type Manufacturer: str
        :param Clinic: 接种单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Clinic: str
        :param Site: 接种部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Site: str
        :param Provider: 接种者
注意：此字段可能返回 null，表示取不到有效值。
        :type Provider: str
        """
        self.Id = None
        self.Vaccine = None
        self.Dose = None
        self.Date = None
        self.LotNumber = None
        self.Manufacturer = None
        self.Clinic = None
        self.Site = None
        self.Provider = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Vaccine = params.get("Vaccine")
        self.Dose = params.get("Dose")
        self.Date = params.get("Date")
        self.LotNumber = params.get("LotNumber")
        self.Manufacturer = params.get("Manufacturer")
        self.Clinic = params.get("Clinic")
        self.Site = params.get("Site")
        self.Provider = params.get("Provider")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VaccineCertificate(AbstractModel):
    """免疫接种证明

    """

    def __init__(self):
        r"""
        :param VaccineList: 免疫接种列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VaccineList: list of Vaccination
        """
        self.VaccineList = None


    def _deserialize(self, params):
        if params.get("VaccineList") is not None:
            self.VaccineList = []
            for item in params.get("VaccineList"):
                obj = Vaccination()
                obj._deserialize(item)
                self.VaccineList.append(obj)
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
        r"""
        :param Grade: 等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Grade: str
        :param Percent: 百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: list of float
        :param Positive: 阳性
注意：此字段可能返回 null，表示取不到有效值。
        :type Positive: str
        """
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
        