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


class AdmissionConditionBlock(AbstractModel):
    """入院情况

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文

注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdmissionDiagnosisBlock(AbstractModel):
    """入院诊断

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.Norm = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Norm = params.get("Norm")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class BaseInfo(AbstractModel):
    """标准信息类

    """

    def __init__(self):
        r"""
        :param Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 标准值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Name = None
        self.Index = None
        self.Src = None
        self.Value = None
        self.Coords = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Index = params.get("Index")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaseItem(AbstractModel):
    """基础类型

    """

    def __init__(self):
        r"""
        :param Name: 类型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原始文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 归一化后值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Alias: 别名
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Coords: 四点坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Name = None
        self.Src = None
        self.Value = None
        self.Alias = None
        self.Coords = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        self.Alias = params.get("Alias")
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaseItem2(AbstractModel):
    """基础类型

    """

    def __init__(self):
        r"""
        :param Name: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原始文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 归一化后值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Coords: 四点坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Name = None
        self.Src = None
        self.Value = None
        self.Coords = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaseItem3(AbstractModel):
    """基础类型

    """

    def __init__(self):
        r"""
        :param Name: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原始文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 归一化后值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Coords: 四点坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        :param Order: 第几次
注意：此字段可能返回 null，表示取不到有效值。
        :type Order: int
        """
        self.Name = None
        self.Src = None
        self.Value = None
        self.Coords = None
        self.Order = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
        self.Order = params.get("Order")
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
        :param Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Value = None
        self.Src = None
        self.Coords = None


    def _deserialize(self, params):
        self.Value = params.get("Value")
        self.Src = params.get("Src")
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BirthCert(AbstractModel):
    """出生证明结构化信息

    """

    def __init__(self):
        r"""
        :param NeonatalInfo: 新生儿信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NeonatalInfo: :class:`tencentcloud.mrs.v20200910.models.NeonatalInfo`
        :param MotherInfo: 母亲信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MotherInfo: :class:`tencentcloud.mrs.v20200910.models.ParentInfo`
        :param FatherInfo: 父亲信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FatherInfo: :class:`tencentcloud.mrs.v20200910.models.ParentInfo`
        :param IssueInfo: 签发信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IssueInfo: :class:`tencentcloud.mrs.v20200910.models.IssueInfo`
        """
        self.NeonatalInfo = None
        self.MotherInfo = None
        self.FatherInfo = None
        self.IssueInfo = None


    def _deserialize(self, params):
        if params.get("NeonatalInfo") is not None:
            self.NeonatalInfo = NeonatalInfo()
            self.NeonatalInfo._deserialize(params.get("NeonatalInfo"))
        if params.get("MotherInfo") is not None:
            self.MotherInfo = ParentInfo()
            self.MotherInfo._deserialize(params.get("MotherInfo"))
        if params.get("FatherInfo") is not None:
            self.FatherInfo = ParentInfo()
            self.FatherInfo._deserialize(params.get("FatherInfo"))
        if params.get("IssueInfo") is not None:
            self.IssueInfo = IssueInfo()
            self.IssueInfo._deserialize(params.get("IssueInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BirthPlaceBlock(AbstractModel):
    """出生地

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
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
        :param Size: 大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: list of Size
        """
        self.Index = None
        self.Positive = None
        self.Src = None
        self.Value = None
        self.Type = None
        self.Name = None
        self.Size = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.Positive = params.get("Positive")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        if params.get("Size") is not None:
            self.Size = []
            for item in params.get("Size"):
                obj = Size()
                obj._deserialize(item)
                self.Size.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlockInfoV2(AbstractModel):
    """块信息

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
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Code: 疾病编码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        """
        self.Index = None
        self.Src = None
        self.Value = None
        self.Name = None
        self.Code = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        self.Name = params.get("Name")
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BloodPressureBlock(AbstractModel):
    """血压

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param NormDiastolic: 舒张压
注意：此字段可能返回 null，表示取不到有效值。
        :type NormDiastolic: str
        :param NormSystolic: 收缩压
注意：此字段可能返回 null，表示取不到有效值。
        :type NormSystolic: str
        """
        self.Name = None
        self.Src = None
        self.Norm = None
        self.Unit = None
        self.Value = None
        self.NormDiastolic = None
        self.NormSystolic = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Norm = params.get("Norm")
        self.Unit = params.get("Unit")
        self.Value = params.get("Value")
        self.NormDiastolic = params.get("NormDiastolic")
        self.NormSystolic = params.get("NormSystolic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BodyExaminationBlock(AbstractModel):
    """查体

    """

    def __init__(self):
        r"""
        :param BodyTemperature: 体温
注意：此字段可能返回 null，表示取不到有效值。
        :type BodyTemperature: :class:`tencentcloud.mrs.v20200910.models.BodyTemperatureBlock`
        :param Pulse: 脉搏
注意：此字段可能返回 null，表示取不到有效值。
        :type Pulse: :class:`tencentcloud.mrs.v20200910.models.BodyTemperatureBlock`
        :param Breathe: 呼吸
注意：此字段可能返回 null，表示取不到有效值。
        :type Breathe: :class:`tencentcloud.mrs.v20200910.models.BodyTemperatureBlock`
        :param BloodPressure: 血压
注意：此字段可能返回 null，表示取不到有效值。
        :type BloodPressure: :class:`tencentcloud.mrs.v20200910.models.BloodPressureBlock`
        """
        self.BodyTemperature = None
        self.Pulse = None
        self.Breathe = None
        self.BloodPressure = None


    def _deserialize(self, params):
        if params.get("BodyTemperature") is not None:
            self.BodyTemperature = BodyTemperatureBlock()
            self.BodyTemperature._deserialize(params.get("BodyTemperature"))
        if params.get("Pulse") is not None:
            self.Pulse = BodyTemperatureBlock()
            self.Pulse._deserialize(params.get("Pulse"))
        if params.get("Breathe") is not None:
            self.Breathe = BodyTemperatureBlock()
            self.Breathe._deserialize(params.get("Breathe"))
        if params.get("BloodPressure") is not None:
            self.BloodPressure = BloodPressureBlock()
            self.BloodPressure._deserialize(params.get("BloodPressure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BodyTemperatureBlock(AbstractModel):
    """体温名称

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.Norm = None
        self.Unit = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Norm = params.get("Norm")
        self.Unit = params.get("Unit")
        self.Value = params.get("Value")
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
        


class ChiefComplaintBlock(AbstractModel):
    """主诉

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 单位输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Detail: 主诉详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: list of ChiefComplaintDetailBlock
        """
        self.Name = None
        self.Src = None
        self.Value = None
        self.Detail = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = ChiefComplaintDetailBlock()
                obj._deserialize(item)
                self.Detail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChiefComplaintDetailBlock(AbstractModel):
    """主诉详情

    """

    def __init__(self):
        r"""
        :param DiseaseName: 疾病名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseaseName: str
        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: str
        :param Time: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: str
        :param TimeType: 时间类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeType: str
        """
        self.DiseaseName = None
        self.Part = None
        self.Time = None
        self.TimeType = None


    def _deserialize(self, params):
        self.DiseaseName = params.get("DiseaseName")
        self.Part = params.get("Part")
        self.Time = params.get("Time")
        self.TimeType = params.get("TimeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClinicalStaging(AbstractModel):
    """临床分期

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coord(AbstractModel):
    """坐标

    """

    def __init__(self):
        r"""
        :param Points: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Points: list of Point
        """
        self.Points = None


    def _deserialize(self, params):
        if params.get("Points") is not None:
            self.Points = []
            for item in params.get("Points"):
                obj = Point()
                obj._deserialize(item)
                self.Points.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coordinate(AbstractModel):
    """坐标

    """

    def __init__(self):
        r"""
        :param X: 左上角x坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type X: int
        :param Y: 左上角y坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: int
        :param Width: 宽度，单位像素
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param Height: 高度，单位像素
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CovidItem(AbstractModel):
    """核酸报告结论结构

    """

    def __init__(self):
        r"""
        :param SampleTime: 采样时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleTime: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param TestTime: 检测时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TestTime: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param TestOrganization: 检测机构
注意：此字段可能返回 null，表示取不到有效值。
        :type TestOrganization: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param TestResult: 检测结果
注意：此字段可能返回 null，表示取不到有效值。
        :type TestResult: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param CodeColor: 健康码颜色
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeColor: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        """
        self.SampleTime = None
        self.TestTime = None
        self.TestOrganization = None
        self.TestResult = None
        self.CodeColor = None


    def _deserialize(self, params):
        if params.get("SampleTime") is not None:
            self.SampleTime = BaseItem()
            self.SampleTime._deserialize(params.get("SampleTime"))
        if params.get("TestTime") is not None:
            self.TestTime = BaseItem()
            self.TestTime._deserialize(params.get("TestTime"))
        if params.get("TestOrganization") is not None:
            self.TestOrganization = BaseItem()
            self.TestOrganization._deserialize(params.get("TestOrganization"))
        if params.get("TestResult") is not None:
            self.TestResult = BaseItem()
            self.TestResult._deserialize(params.get("TestResult"))
        if params.get("CodeColor") is not None:
            self.CodeColor = BaseItem()
            self.CodeColor._deserialize(params.get("CodeColor"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CovidItemsInfo(AbstractModel):
    """核酸报告结论

    """

    def __init__(self):
        r"""
        :param CovidItems: 核酸报告结论
注意：此字段可能返回 null，表示取不到有效值。
        :type CovidItems: list of CovidItem
        :param Version: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        """
        self.CovidItems = None
        self.Version = None


    def _deserialize(self, params):
        if params.get("CovidItems") is not None:
            self.CovidItems = []
            for item in params.get("CovidItems"):
                obj = CovidItem()
                obj._deserialize(item)
                self.CovidItems.append(obj)
        self.Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeathDateBlock(AbstractModel):
    """死亡时间

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param Timestamp: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.Type = None
        self.Norm = None
        self.Unit = None
        self.Timestamp = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Type = params.get("Type")
        self.Norm = params.get("Norm")
        self.Unit = params.get("Unit")
        self.Timestamp = params.get("Timestamp")
        self.Value = params.get("Value")
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
        :param Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Text = None
        self.Organ = None
        self.Tuber = None
        self.Coords = None


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
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescInfo(AbstractModel):
    """描述段落

    """

    def __init__(self):
        r"""
        :param Text: 描述段落文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param Infos: 描述段落详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Infos: list of DetailInformation
        """
        self.Text = None
        self.Infos = None


    def _deserialize(self, params):
        if params.get("Text") is not None:
            self.Text = BaseInfo()
            self.Text._deserialize(params.get("Text"))
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = DetailInformation()
                obj._deserialize(item)
                self.Infos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetailInformation(AbstractModel):
    """详情

    """

    def __init__(self):
        r"""
        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param TissueSizes: 组织大小
注意：此字段可能返回 null，表示取不到有效值。
        :type TissueSizes: list of Size
        :param TuberSizes: 结节大小
注意：此字段可能返回 null，表示取不到有效值。
        :type TuberSizes: list of Size
        :param CancerSizes: 肿瘤大小
注意：此字段可能返回 null，表示取不到有效值。
        :type CancerSizes: list of Size
        :param HistologyLevel: 组织学等级
注意：此字段可能返回 null，表示取不到有效值。
        :type HistologyLevel: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param HistologyType: 组织学类型
注意：此字段可能返回 null，表示取不到有效值。
        :type HistologyType: :class:`tencentcloud.mrs.v20200910.models.HistologyTypeV2`
        :param Invasive: 侵犯
注意：此字段可能返回 null，表示取不到有效值。
        :type Invasive: list of InvasiveV2
        :param PTNM: pTNM
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNM: :class:`tencentcloud.mrs.v20200910.models.PTNM`
        :param InfiltrationDepth: 浸润深度
注意：此字段可能返回 null，表示取不到有效值。
        :type InfiltrationDepth: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param TuberNum: 结节数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TuberNum: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param Calcification: 钙化
注意：此字段可能返回 null，表示取不到有效值。
        :type Calcification: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param Necrosis: 坏死
注意：此字段可能返回 null，表示取不到有效值。
        :type Necrosis: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param Abnormity: 异形
注意：此字段可能返回 null，表示取不到有效值。
        :type Abnormity: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param Breaked: 断链
注意：此字段可能返回 null，表示取不到有效值。
        :type Breaked: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        """
        self.Part = None
        self.TissueSizes = None
        self.TuberSizes = None
        self.CancerSizes = None
        self.HistologyLevel = None
        self.HistologyType = None
        self.Invasive = None
        self.PTNM = None
        self.InfiltrationDepth = None
        self.TuberNum = None
        self.Calcification = None
        self.Necrosis = None
        self.Abnormity = None
        self.Breaked = None


    def _deserialize(self, params):
        if params.get("Part") is not None:
            self.Part = Part()
            self.Part._deserialize(params.get("Part"))
        if params.get("TissueSizes") is not None:
            self.TissueSizes = []
            for item in params.get("TissueSizes"):
                obj = Size()
                obj._deserialize(item)
                self.TissueSizes.append(obj)
        if params.get("TuberSizes") is not None:
            self.TuberSizes = []
            for item in params.get("TuberSizes"):
                obj = Size()
                obj._deserialize(item)
                self.TuberSizes.append(obj)
        if params.get("CancerSizes") is not None:
            self.CancerSizes = []
            for item in params.get("CancerSizes"):
                obj = Size()
                obj._deserialize(item)
                self.CancerSizes.append(obj)
        if params.get("HistologyLevel") is not None:
            self.HistologyLevel = BaseInfo()
            self.HistologyLevel._deserialize(params.get("HistologyLevel"))
        if params.get("HistologyType") is not None:
            self.HistologyType = HistologyTypeV2()
            self.HistologyType._deserialize(params.get("HistologyType"))
        if params.get("Invasive") is not None:
            self.Invasive = []
            for item in params.get("Invasive"):
                obj = InvasiveV2()
                obj._deserialize(item)
                self.Invasive.append(obj)
        if params.get("PTNM") is not None:
            self.PTNM = PTNM()
            self.PTNM._deserialize(params.get("PTNM"))
        if params.get("InfiltrationDepth") is not None:
            self.InfiltrationDepth = BaseInfo()
            self.InfiltrationDepth._deserialize(params.get("InfiltrationDepth"))
        if params.get("TuberNum") is not None:
            self.TuberNum = BaseInfo()
            self.TuberNum._deserialize(params.get("TuberNum"))
        if params.get("Calcification") is not None:
            self.Calcification = BaseInfo()
            self.Calcification._deserialize(params.get("Calcification"))
        if params.get("Necrosis") is not None:
            self.Necrosis = BaseInfo()
            self.Necrosis._deserialize(params.get("Necrosis"))
        if params.get("Abnormity") is not None:
            self.Abnormity = BaseInfo()
            self.Abnormity._deserialize(params.get("Abnormity"))
        if params.get("Breaked") is not None:
            self.Breaked = BaseInfo()
            self.Breaked._deserialize(params.get("Breaked"))
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
        


class DischargeConditionBlock(AbstractModel):
    """出院情况

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        """
        self.Name = None
        self.Src = None
        self.Value = None
        self.Norm = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        self.Norm = params.get("Norm")
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
        


class DischargeDiagnosisBlock(AbstractModel):
    """出院诊断

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.Norm = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Norm = params.get("Norm")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DischargeInfoBlock(AbstractModel):
    """出入院结构体

    """

    def __init__(self):
        r"""
        :param DiseaseHistory: 疾病史
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseaseHistory: :class:`tencentcloud.mrs.v20200910.models.DiseaseHistoryBlock`
        :param PersonalHistory: 个人史
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonalHistory: :class:`tencentcloud.mrs.v20200910.models.PersonalHistoryBlock`
        :param DrugHistory: 药物史
注意：此字段可能返回 null，表示取不到有效值。
        :type DrugHistory: :class:`tencentcloud.mrs.v20200910.models.DrugHistoryBlock`
        :param TreatmentRecord: 治疗相关
注意：此字段可能返回 null，表示取不到有效值。
        :type TreatmentRecord: :class:`tencentcloud.mrs.v20200910.models.TreatmentRecordBlock`
        :param ParagraphBlock: 文本段落
注意：此字段可能返回 null，表示取不到有效值。
        :type ParagraphBlock: :class:`tencentcloud.mrs.v20200910.models.ParagraphBlock`
        """
        self.DiseaseHistory = None
        self.PersonalHistory = None
        self.DrugHistory = None
        self.TreatmentRecord = None
        self.ParagraphBlock = None


    def _deserialize(self, params):
        if params.get("DiseaseHistory") is not None:
            self.DiseaseHistory = DiseaseHistoryBlock()
            self.DiseaseHistory._deserialize(params.get("DiseaseHistory"))
        if params.get("PersonalHistory") is not None:
            self.PersonalHistory = PersonalHistoryBlock()
            self.PersonalHistory._deserialize(params.get("PersonalHistory"))
        if params.get("DrugHistory") is not None:
            self.DrugHistory = DrugHistoryBlock()
            self.DrugHistory._deserialize(params.get("DrugHistory"))
        if params.get("TreatmentRecord") is not None:
            self.TreatmentRecord = TreatmentRecordBlock()
            self.TreatmentRecord._deserialize(params.get("TreatmentRecord"))
        if params.get("ParagraphBlock") is not None:
            self.ParagraphBlock = ParagraphBlock()
            self.ParagraphBlock._deserialize(params.get("ParagraphBlock"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiseaseHistoryBlock(AbstractModel):
    """疾病史

    """

    def __init__(self):
        r"""
        :param MainDiseaseHistory: 主要病史
注意：此字段可能返回 null，表示取不到有效值。
        :type MainDiseaseHistory: :class:`tencentcloud.mrs.v20200910.models.MainDiseaseHistoryBlock`
        :param AllergyHistory: 过敏史
注意：此字段可能返回 null，表示取不到有效值。
        :type AllergyHistory: :class:`tencentcloud.mrs.v20200910.models.MainDiseaseHistoryBlock`
        :param InfectHistory: 注射史
注意：此字段可能返回 null，表示取不到有效值。
        :type InfectHistory: :class:`tencentcloud.mrs.v20200910.models.MainDiseaseHistoryBlock`
        :param SurgeryHistory: 手术史
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryHistory: :class:`tencentcloud.mrs.v20200910.models.SurgeryHistoryBlock`
        :param TransfusionHistory: 输血史
注意：此字段可能返回 null，表示取不到有效值。
        :type TransfusionHistory: :class:`tencentcloud.mrs.v20200910.models.TransfusionHistoryBlock`
        """
        self.MainDiseaseHistory = None
        self.AllergyHistory = None
        self.InfectHistory = None
        self.SurgeryHistory = None
        self.TransfusionHistory = None


    def _deserialize(self, params):
        if params.get("MainDiseaseHistory") is not None:
            self.MainDiseaseHistory = MainDiseaseHistoryBlock()
            self.MainDiseaseHistory._deserialize(params.get("MainDiseaseHistory"))
        if params.get("AllergyHistory") is not None:
            self.AllergyHistory = MainDiseaseHistoryBlock()
            self.AllergyHistory._deserialize(params.get("AllergyHistory"))
        if params.get("InfectHistory") is not None:
            self.InfectHistory = MainDiseaseHistoryBlock()
            self.InfectHistory._deserialize(params.get("InfectHistory"))
        if params.get("SurgeryHistory") is not None:
            self.SurgeryHistory = SurgeryHistoryBlock()
            self.SurgeryHistory._deserialize(params.get("SurgeryHistory"))
        if params.get("TransfusionHistory") is not None:
            self.TransfusionHistory = TransfusionHistoryBlock()
            self.TransfusionHistory._deserialize(params.get("TransfusionHistory"))
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
        


class DiseasePresentBlock(AbstractModel):
    """现病史

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Norm: 归一化
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        """
        self.Name = None
        self.Src = None
        self.Value = None
        self.Norm = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        self.Norm = params.get("Norm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DosageBlock(AbstractModel):
    """药物用法用量

    """

    def __init__(self):
        r"""
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param SingleMeasurement: 单次计量
注意：此字段可能返回 null，表示取不到有效值。
        :type SingleMeasurement: str
        :param Frequency: 频次
注意：此字段可能返回 null，表示取不到有效值。
        :type Frequency: str
        :param DrugDeliveryRoute: 给药途径
注意：此字段可能返回 null，表示取不到有效值。
        :type DrugDeliveryRoute: str
        """
        self.Value = None
        self.SingleMeasurement = None
        self.Frequency = None
        self.DrugDeliveryRoute = None


    def _deserialize(self, params):
        self.Value = params.get("Value")
        self.SingleMeasurement = params.get("SingleMeasurement")
        self.Frequency = params.get("Frequency")
        self.DrugDeliveryRoute = params.get("DrugDeliveryRoute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrugHistoryBlock(AbstractModel):
    """药物史

    """

    def __init__(self):
        r"""
        :param Name: 药品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param DrugList: 药物列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DrugList: list of DrugListBlock
        :param Value: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.DrugList = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        if params.get("DrugList") is not None:
            self.DrugList = []
            for item in params.get("DrugList"):
                obj = DrugListBlock()
                obj._deserialize(item)
                self.DrugList.append(obj)
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrugListBlock(AbstractModel):
    """药物史

    """

    def __init__(self):
        r"""
        :param CommonName: 通用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonName: str
        :param TradeName: 商品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeName: str
        :param Dosage: 用法用量
注意：此字段可能返回 null，表示取不到有效值。
        :type Dosage: :class:`tencentcloud.mrs.v20200910.models.DosageBlock`
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.CommonName = None
        self.TradeName = None
        self.Dosage = None
        self.Value = None


    def _deserialize(self, params):
        self.CommonName = params.get("CommonName")
        self.TradeName = params.get("TradeName")
        if params.get("Dosage") is not None:
            self.Dosage = DosageBlock()
            self.Dosage._deserialize(params.get("Dosage"))
        self.Value = params.get("Value")
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
        :param Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Text = None
        self.Organ = None
        self.Coords = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        if params.get("Organ") is not None:
            self.Organ = []
            for item in params.get("Organ"):
                obj = EndoscopyOrgan()
                obj._deserialize(item)
                self.Organ.append(obj)
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
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
        :param Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Part = None
        self.Index = None
        self.Src = None
        self.PartAlias = None
        self.SymDescList = None
        self.Coords = None


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
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Exame(AbstractModel):
    """体检结论

    """

    def __init__(self):
        r"""
        :param OverView: 结论段落
注意：此字段可能返回 null，表示取不到有效值。
        :type OverView: list of ResultInfo
        :param Abnormality: 异常与建议段落
注意：此字段可能返回 null，表示取不到有效值。
        :type Abnormality: list of ResultInfo
        """
        self.OverView = None
        self.Abnormality = None


    def _deserialize(self, params):
        if params.get("OverView") is not None:
            self.OverView = []
            for item in params.get("OverView"):
                obj = ResultInfo()
                obj._deserialize(item)
                self.OverView.append(obj)
        if params.get("Abnormality") is not None:
            self.Abnormality = []
            for item in params.get("Abnormality"):
                obj = ResultInfo()
                obj._deserialize(item)
                self.Abnormality.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EyeChildItem(AbstractModel):
    """眼科子结构

    """

    def __init__(self):
        r"""
        :param Sph: 球镜
注意：此字段可能返回 null，表示取不到有效值。
        :type Sph: list of BaseItem3
        :param Cyl: 柱镜
注意：此字段可能返回 null，表示取不到有效值。
        :type Cyl: list of BaseItem3
        :param Ax: 轴位
注意：此字段可能返回 null，表示取不到有效值。
        :type Ax: list of BaseItem3
        :param Se: 等效球镜
注意：此字段可能返回 null，表示取不到有效值。
        :type Se: :class:`tencentcloud.mrs.v20200910.models.BaseItem2`
        """
        self.Sph = None
        self.Cyl = None
        self.Ax = None
        self.Se = None


    def _deserialize(self, params):
        if params.get("Sph") is not None:
            self.Sph = []
            for item in params.get("Sph"):
                obj = BaseItem3()
                obj._deserialize(item)
                self.Sph.append(obj)
        if params.get("Cyl") is not None:
            self.Cyl = []
            for item in params.get("Cyl"):
                obj = BaseItem3()
                obj._deserialize(item)
                self.Cyl.append(obj)
        if params.get("Ax") is not None:
            self.Ax = []
            for item in params.get("Ax"):
                obj = BaseItem3()
                obj._deserialize(item)
                self.Ax.append(obj)
        if params.get("Se") is not None:
            self.Se = BaseItem2()
            self.Se._deserialize(params.get("Se"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EyeItem(AbstractModel):
    """眼科结构体

    """

    def __init__(self):
        r"""
        :param Left: 左眼
注意：此字段可能返回 null，表示取不到有效值。
        :type Left: :class:`tencentcloud.mrs.v20200910.models.EyeChildItem`
        :param Right: 右眼
注意：此字段可能返回 null，表示取不到有效值。
        :type Right: :class:`tencentcloud.mrs.v20200910.models.EyeChildItem`
        :param Pd: 瞳距
注意：此字段可能返回 null，表示取不到有效值。
        :type Pd: :class:`tencentcloud.mrs.v20200910.models.BaseItem2`
        """
        self.Left = None
        self.Right = None
        self.Pd = None


    def _deserialize(self, params):
        if params.get("Left") is not None:
            self.Left = EyeChildItem()
            self.Left._deserialize(params.get("Left"))
        if params.get("Right") is not None:
            self.Right = EyeChildItem()
            self.Right._deserialize(params.get("Right"))
        if params.get("Pd") is not None:
            self.Pd = BaseItem2()
            self.Pd._deserialize(params.get("Pd"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EyeItemsInfo(AbstractModel):
    """眼科报告结构体

    """

    def __init__(self):
        r"""
        :param EyeItems: 眼科报告
注意：此字段可能返回 null，表示取不到有效值。
        :type EyeItems: :class:`tencentcloud.mrs.v20200910.models.EyeItem`
        :param Version: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        """
        self.EyeItems = None
        self.Version = None


    def _deserialize(self, params):
        if params.get("EyeItems") is not None:
            self.EyeItems = EyeItem()
            self.EyeItems._deserialize(params.get("EyeItems"))
        self.Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FamilyHistoryBlock(AbstractModel):
    """家族史

    """

    def __init__(self):
        r"""
        :param RelativeHistory: 家庭成员
注意：此字段可能返回 null，表示取不到有效值。
        :type RelativeHistory: :class:`tencentcloud.mrs.v20200910.models.RelativeHistoryBlock`
        :param RelativeCancerHistory: 家族肿瘤史
注意：此字段可能返回 null，表示取不到有效值。
        :type RelativeCancerHistory: :class:`tencentcloud.mrs.v20200910.models.RelativeCancerHistoryBlock`
        :param GeneticHistory: 家族遗传史
注意：此字段可能返回 null，表示取不到有效值。
        :type GeneticHistory: :class:`tencentcloud.mrs.v20200910.models.GeneticHistoryBlock`
        """
        self.RelativeHistory = None
        self.RelativeCancerHistory = None
        self.GeneticHistory = None


    def _deserialize(self, params):
        if params.get("RelativeHistory") is not None:
            self.RelativeHistory = RelativeHistoryBlock()
            self.RelativeHistory._deserialize(params.get("RelativeHistory"))
        if params.get("RelativeCancerHistory") is not None:
            self.RelativeCancerHistory = RelativeCancerHistoryBlock()
            self.RelativeCancerHistory._deserialize(params.get("RelativeCancerHistory"))
        if params.get("GeneticHistory") is not None:
            self.GeneticHistory = GeneticHistoryBlock()
            self.GeneticHistory._deserialize(params.get("GeneticHistory"))
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
        


class FertilityHistoryBlock(AbstractModel):
    """婚育史

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param PregCount: 妊娠次数
注意：此字段可能返回 null，表示取不到有效值。
        :type PregCount: str
        :param ProduCount: 生产次数
注意：此字段可能返回 null，表示取不到有效值。
        :type ProduCount: str
        """
        self.Name = None
        self.Src = None
        self.State = None
        self.Norm = None
        self.Value = None
        self.PregCount = None
        self.ProduCount = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.State = params.get("State")
        self.Norm = params.get("Norm")
        self.Value = params.get("Value")
        self.PregCount = params.get("PregCount")
        self.ProduCount = params.get("ProduCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Fetus(AbstractModel):
    """胎儿数据结构

    """

    def __init__(self):
        r"""
        :param BPD: 双顶径
注意：此字段可能返回 null，表示取不到有效值。
        :type BPD: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param APTD: 腹前后径
注意：此字段可能返回 null，表示取不到有效值。
        :type APTD: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param TTD: 腹左右径
注意：此字段可能返回 null，表示取不到有效值。
        :type TTD: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param CRL: 头臀径
注意：此字段可能返回 null，表示取不到有效值。
        :type CRL: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param HC: 头围
注意：此字段可能返回 null，表示取不到有效值。
        :type HC: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param AC: 腹围
注意：此字段可能返回 null，表示取不到有效值。
        :type AC: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param FL: 股骨长
注意：此字段可能返回 null，表示取不到有效值。
        :type FL: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param HL: 肱骨长
注意：此字段可能返回 null，表示取不到有效值。
        :type HL: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param Weight: 胎儿重量
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param NT: 颈项透明层
注意：此字段可能返回 null，表示取不到有效值。
        :type NT: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param UmbilicalCord: 脐动脉血流
注意：此字段可能返回 null，表示取不到有效值。
        :type UmbilicalCord: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param WaterDeep: 羊水最大深度
注意：此字段可能返回 null，表示取不到有效值。
        :type WaterDeep: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param WaterQuad: 羊水四象限测量
注意：此字段可能返回 null，表示取不到有效值。
        :type WaterQuad: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param AFI: 羊水指数
注意：此字段可能返回 null，表示取不到有效值。
        :type AFI: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param FHR: 胎心
注意：此字段可能返回 null，表示取不到有效值。
        :type FHR: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param Movement: 胎动
注意：此字段可能返回 null，表示取不到有效值。
        :type Movement: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param Num: 胎数
注意：此字段可能返回 null，表示取不到有效值。
        :type Num: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param Position: 胎位
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param Alive: 是否活胎
注意：此字段可能返回 null，表示取不到有效值。
        :type Alive: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param PlacentaLocation: 胎盘位置
注意：此字段可能返回 null，表示取不到有效值。
        :type PlacentaLocation: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param PlacentaThickness: 胎盘厚度
注意：此字段可能返回 null，表示取不到有效值。
        :type PlacentaThickness: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param PlacentaGrade: 胎盘成熟度
注意：此字段可能返回 null，表示取不到有效值。
        :type PlacentaGrade: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param GestationTime: 妊娠时间
注意：此字段可能返回 null，表示取不到有效值。
        :type GestationTime: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param GestationPeriod: 妊娠周期
注意：此字段可能返回 null，表示取不到有效值。
        :type GestationPeriod: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param AroundNeck: 绕颈
注意：此字段可能返回 null，表示取不到有效值。
        :type AroundNeck: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param Sym: 病变
注意：此字段可能返回 null，表示取不到有效值。
        :type Sym: list of FieldInfo
        :param Src: 原文内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        """
        self.BPD = None
        self.APTD = None
        self.TTD = None
        self.CRL = None
        self.HC = None
        self.AC = None
        self.FL = None
        self.HL = None
        self.Weight = None
        self.NT = None
        self.UmbilicalCord = None
        self.WaterDeep = None
        self.WaterQuad = None
        self.AFI = None
        self.FHR = None
        self.Movement = None
        self.Num = None
        self.Position = None
        self.Alive = None
        self.PlacentaLocation = None
        self.PlacentaThickness = None
        self.PlacentaGrade = None
        self.GestationTime = None
        self.GestationPeriod = None
        self.AroundNeck = None
        self.Sym = None
        self.Src = None


    def _deserialize(self, params):
        if params.get("BPD") is not None:
            self.BPD = FieldInfo()
            self.BPD._deserialize(params.get("BPD"))
        if params.get("APTD") is not None:
            self.APTD = FieldInfo()
            self.APTD._deserialize(params.get("APTD"))
        if params.get("TTD") is not None:
            self.TTD = FieldInfo()
            self.TTD._deserialize(params.get("TTD"))
        if params.get("CRL") is not None:
            self.CRL = FieldInfo()
            self.CRL._deserialize(params.get("CRL"))
        if params.get("HC") is not None:
            self.HC = FieldInfo()
            self.HC._deserialize(params.get("HC"))
        if params.get("AC") is not None:
            self.AC = FieldInfo()
            self.AC._deserialize(params.get("AC"))
        if params.get("FL") is not None:
            self.FL = FieldInfo()
            self.FL._deserialize(params.get("FL"))
        if params.get("HL") is not None:
            self.HL = FieldInfo()
            self.HL._deserialize(params.get("HL"))
        if params.get("Weight") is not None:
            self.Weight = FieldInfo()
            self.Weight._deserialize(params.get("Weight"))
        if params.get("NT") is not None:
            self.NT = FieldInfo()
            self.NT._deserialize(params.get("NT"))
        if params.get("UmbilicalCord") is not None:
            self.UmbilicalCord = FieldInfo()
            self.UmbilicalCord._deserialize(params.get("UmbilicalCord"))
        if params.get("WaterDeep") is not None:
            self.WaterDeep = FieldInfo()
            self.WaterDeep._deserialize(params.get("WaterDeep"))
        if params.get("WaterQuad") is not None:
            self.WaterQuad = FieldInfo()
            self.WaterQuad._deserialize(params.get("WaterQuad"))
        if params.get("AFI") is not None:
            self.AFI = FieldInfo()
            self.AFI._deserialize(params.get("AFI"))
        if params.get("FHR") is not None:
            self.FHR = FieldInfo()
            self.FHR._deserialize(params.get("FHR"))
        if params.get("Movement") is not None:
            self.Movement = FieldInfo()
            self.Movement._deserialize(params.get("Movement"))
        if params.get("Num") is not None:
            self.Num = FieldInfo()
            self.Num._deserialize(params.get("Num"))
        if params.get("Position") is not None:
            self.Position = FieldInfo()
            self.Position._deserialize(params.get("Position"))
        if params.get("Alive") is not None:
            self.Alive = FieldInfo()
            self.Alive._deserialize(params.get("Alive"))
        if params.get("PlacentaLocation") is not None:
            self.PlacentaLocation = FieldInfo()
            self.PlacentaLocation._deserialize(params.get("PlacentaLocation"))
        if params.get("PlacentaThickness") is not None:
            self.PlacentaThickness = FieldInfo()
            self.PlacentaThickness._deserialize(params.get("PlacentaThickness"))
        if params.get("PlacentaGrade") is not None:
            self.PlacentaGrade = FieldInfo()
            self.PlacentaGrade._deserialize(params.get("PlacentaGrade"))
        if params.get("GestationTime") is not None:
            self.GestationTime = FieldInfo()
            self.GestationTime._deserialize(params.get("GestationTime"))
        if params.get("GestationPeriod") is not None:
            self.GestationPeriod = FieldInfo()
            self.GestationPeriod._deserialize(params.get("GestationPeriod"))
        if params.get("AroundNeck") is not None:
            self.AroundNeck = FieldInfo()
            self.AroundNeck._deserialize(params.get("AroundNeck"))
        if params.get("Sym") is not None:
            self.Sym = []
            for item in params.get("Sym"):
                obj = FieldInfo()
                obj._deserialize(item)
                self.Sym.append(obj)
        self.Src = params.get("Src")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FieldInfo(AbstractModel):
    """通用块信息

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Nums: 数值
注意：此字段可能返回 null，表示取不到有效值。
        :type Nums: list of NumValue
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        """
        self.Name = None
        self.Value = None
        self.Nums = None
        self.Src = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("Nums") is not None:
            self.Nums = []
            for item in params.get("Nums"):
                obj = NumValue()
                obj._deserialize(item)
                self.Nums.append(obj)
        self.Src = params.get("Src")
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
        :param DamagePoi: 受伤中毒的外部原因
注意：此字段可能返回 null，表示取不到有效值。
        :type DamagePoi: :class:`tencentcloud.mrs.v20200910.models.BlockInfoV2`
        :param Fp2NdItems: 病案首页第二页
注意：此字段可能返回 null，表示取不到有效值。
        :type Fp2NdItems: list of Fp2NdItem
        """
        self.DischargeDiagnosis = None
        self.PathologicalDiagnosis = None
        self.ClinicalDiagnosis = None
        self.DamagePoi = None
        self.Fp2NdItems = None


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
        if params.get("DamagePoi") is not None:
            self.DamagePoi = BlockInfoV2()
            self.DamagePoi._deserialize(params.get("DamagePoi"))
        if params.get("Fp2NdItems") is not None:
            self.Fp2NdItems = []
            for item in params.get("Fp2NdItems"):
                obj = Fp2NdItem()
                obj._deserialize(item)
                self.Fp2NdItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Fp2NdItem(AbstractModel):
    """病案首页第二页

    """

    def __init__(self):
        r"""
        :param Code: 手术编码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param Name: 手术名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param StartTime: 手术开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param EndTime: 手术结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param Level: 手术等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param Type: 手术类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param IncisionHealingGrade: 醉愈合方式
注意：此字段可能返回 null，表示取不到有效值。
        :type IncisionHealingGrade: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param AnesthesiaMethod: 麻醉方法
注意：此字段可能返回 null，表示取不到有效值。
        :type AnesthesiaMethod: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        """
        self.Code = None
        self.Name = None
        self.StartTime = None
        self.EndTime = None
        self.Level = None
        self.Type = None
        self.IncisionHealingGrade = None
        self.AnesthesiaMethod = None


    def _deserialize(self, params):
        if params.get("Code") is not None:
            self.Code = BaseItem()
            self.Code._deserialize(params.get("Code"))
        if params.get("Name") is not None:
            self.Name = BaseItem()
            self.Name._deserialize(params.get("Name"))
        if params.get("StartTime") is not None:
            self.StartTime = BaseItem()
            self.StartTime._deserialize(params.get("StartTime"))
        if params.get("EndTime") is not None:
            self.EndTime = BaseItem()
            self.EndTime._deserialize(params.get("EndTime"))
        if params.get("Level") is not None:
            self.Level = BaseItem()
            self.Level._deserialize(params.get("Level"))
        if params.get("Type") is not None:
            self.Type = BaseItem()
            self.Type._deserialize(params.get("Type"))
        if params.get("IncisionHealingGrade") is not None:
            self.IncisionHealingGrade = BaseItem()
            self.IncisionHealingGrade._deserialize(params.get("IncisionHealingGrade"))
        if params.get("AnesthesiaMethod") is not None:
            self.AnesthesiaMethod = BaseItem()
            self.AnesthesiaMethod._deserialize(params.get("AnesthesiaMethod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneticHistoryBlock(AbstractModel):
    """家族遗传史

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param GeneticList: 遗传列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GeneticList: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.GeneticList = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.GeneticList = params.get("GeneticList")
        self.Value = params.get("Value")
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
        


class HistologyClass(AbstractModel):
    """组织学类

    """

    def __init__(self):
        r"""
        :param Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Name = None
        self.Index = None
        self.Src = None
        self.Value = None
        self.Coords = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Index = params.get("Index")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
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
        


class HistologyTypeV2(AbstractModel):
    """组织学类型

    """

    def __init__(self):
        r"""
        :param Infiltration: 浸润
注意：此字段可能返回 null，表示取不到有效值。
        :type Infiltration: str
        :param Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Type: 归一化后的组织学类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Infiltration = None
        self.Index = None
        self.Src = None
        self.Type = None
        self.Name = None
        self.Coords = None


    def _deserialize(self, params):
        self.Infiltration = params.get("Infiltration")
        self.Index = params.get("Index")
        self.Src = params.get("Src")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
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
        


class IHCBlock(AbstractModel):
    """IHC块

    """

    def __init__(self):
        r"""
        :param Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 具体值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.mrs.v20200910.models.ValueBlock`
        :param Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Index = None
        self.Src = None
        self.Name = None
        self.Value = None
        self.Coords = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.Src = params.get("Src")
        self.Name = params.get("Name")
        if params.get("Value") is not None:
            self.Value = ValueBlock()
            self.Value._deserialize(params.get("Value"))
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
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
        


class IHCV2(AbstractModel):
    """IHC

    """

    def __init__(self):
        r"""
        :param Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Name: ihc归一化
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: ihc详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.mrs.v20200910.models.Value`
        :param Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Index = None
        self.Src = None
        self.Name = None
        self.Value = None
        self.Coords = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.Src = params.get("Src")
        self.Name = params.get("Name")
        if params.get("Value") is not None:
            self.Value = Value()
            self.Value._deserialize(params.get("Value"))
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
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
        :param UserType: 后付费的用户类型，新客户传1，老客户可不传或传 0。2022 年 12 月 15 新增了计费项，在此时间之前已经通过商务指定优惠价格的大客户，请不传这个字段或传 0，如果传 1 会导致以前获得的折扣价格失效。在 2022 年 12 月 15 日之后，通过商务指定优惠价格的大客户请传 1。
        :type UserType: int
        """
        self.ImageInfoList = None
        self.HandleParam = None
        self.Type = None
        self.UserType = None


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
        self.UserType = params.get("UserType")
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
        :param UserType: 后付费的用户类型，新客户传1，老客户可不传或传 0。2022 年 12 月 15 新增了计费项，在此时间之前已经通过商务指定优惠价格的大客户，请不传这个字段或传 0，如果传 1 会导致以前获得的折扣价格失效。在 2022 年 12 月 15 日之后，通过商务指定优惠价格的大客户请传 1。
        :type UserType: int
        :param ReportTypeVersion: 可选。用于指定不同报告使用的结构化引擎版本，不同版本返回的JSON 数据结果不兼容。若不指定版本号，就默认用旧的版本号。
（1）检验报告 11，默认使用 V2，最高支持 V3。
（2）病理报告 15，默认使用 V1，最高支持 V2。
（3）入院记录29、出院记录 28、病历记录 216、病程记录 217、门诊记录 210，默认使用 V1，最高支持 V2。
        :type ReportTypeVersion: list of ReportTypeVersion
        """
        self.ImageInfoList = None
        self.HandleParam = None
        self.Type = None
        self.IsUsedClassify = None
        self.UserType = None
        self.ReportTypeVersion = None


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
        self.UserType = params.get("UserType")
        if params.get("ReportTypeVersion") is not None:
            self.ReportTypeVersion = []
            for item in params.get("ReportTypeVersion"):
                obj = ReportTypeVersion()
                obj._deserialize(item)
                self.ReportTypeVersion.append(obj)
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
        :param TextTypeList: 多级分类结果
注意：此字段可能返回 null，表示取不到有效值。
        :type TextTypeList: list of TextType
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Template = None
        self.TextTypeList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = Template()
            self.Template._deserialize(params.get("Template"))
        if params.get("TextTypeList") is not None:
            self.TextTypeList = []
            for item in params.get("TextTypeList"):
                obj = TextType()
                obj._deserialize(item)
                self.TextTypeList.append(obj)
        self.RequestId = params.get("RequestId")


class ImmunohistochemistryBlock(AbstractModel):
    """免疫组化

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 免疫组化详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of IHCBlock
        """
        self.Name = None
        self.Src = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = IHCBlock()
                obj._deserialize(item)
                self.Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param Id: 指标项ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param Coords: 指标项坐标位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: :class:`tencentcloud.mrs.v20200910.models.Coordinate`
        :param InferNormal: 推测结果是否异常
注意：此字段可能返回 null，表示取不到有效值。
        :type InferNormal: str
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
        self.Id = None
        self.Coords = None
        self.InferNormal = None


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
        self.Id = params.get("Id")
        if params.get("Coords") is not None:
            self.Coords = Coordinate()
            self.Coords._deserialize(params.get("Coords"))
        self.InferNormal = params.get("InferNormal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndicatorItemV2(AbstractModel):
    """检验指标项结构v2

    """

    def __init__(self):
        r"""
        :param Item: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Item: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param Code: 英文编码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param Result: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param Range: 参考范围
注意：此字段可能返回 null，表示取不到有效值。
        :type Range: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param Arrow: 上下箭头
注意：此字段可能返回 null，表示取不到有效值。
        :type Arrow: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param Method: 检测方法
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        :param Normal: 结果是否异常
注意：此字段可能返回 null，表示取不到有效值。
        :type Normal: bool
        :param Id: ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param Order: 序号
注意：此字段可能返回 null，表示取不到有效值。
        :type Order: int
        :param InferNormal: 推测结果是否异常
注意：此字段可能返回 null，表示取不到有效值。
        :type InferNormal: str
        """
        self.Item = None
        self.Code = None
        self.Result = None
        self.Unit = None
        self.Range = None
        self.Arrow = None
        self.Method = None
        self.Normal = None
        self.Id = None
        self.Order = None
        self.InferNormal = None


    def _deserialize(self, params):
        if params.get("Item") is not None:
            self.Item = BaseItem()
            self.Item._deserialize(params.get("Item"))
        if params.get("Code") is not None:
            self.Code = BaseItem()
            self.Code._deserialize(params.get("Code"))
        if params.get("Result") is not None:
            self.Result = BaseItem()
            self.Result._deserialize(params.get("Result"))
        if params.get("Unit") is not None:
            self.Unit = BaseItem()
            self.Unit._deserialize(params.get("Unit"))
        if params.get("Range") is not None:
            self.Range = BaseItem()
            self.Range._deserialize(params.get("Range"))
        if params.get("Arrow") is not None:
            self.Arrow = BaseItem()
            self.Arrow._deserialize(params.get("Arrow"))
        if params.get("Method") is not None:
            self.Method = BaseItem()
            self.Method._deserialize(params.get("Method"))
        self.Normal = params.get("Normal")
        self.Id = params.get("Id")
        self.Order = params.get("Order")
        self.InferNormal = params.get("InferNormal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndicatorV3(AbstractModel):
    """检验报告v3

    """

    def __init__(self):
        r"""
        :param TableIndictors: 检验报告V3结论
注意：此字段可能返回 null，表示取不到有效值。
        :type TableIndictors: list of TableIndicators
        :param Version: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        """
        self.TableIndictors = None
        self.Version = None


    def _deserialize(self, params):
        if params.get("TableIndictors") is not None:
            self.TableIndictors = []
            for item in params.get("TableIndictors"):
                obj = TableIndicators()
                obj._deserialize(item)
                self.TableIndictors.append(obj)
        self.Version = params.get("Version")
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
        


class InvasiveV2(AbstractModel):
    """侵犯

    """

    def __init__(self):
        r"""
        :param Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param Positive: 阴性或阳性
注意：此字段可能返回 null，表示取不到有效值。
        :type Positive: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Index = None
        self.Part = None
        self.Positive = None
        self.Src = None
        self.Coords = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        if params.get("Part") is not None:
            self.Part = Part()
            self.Part._deserialize(params.get("Part"))
        self.Positive = params.get("Positive")
        self.Src = params.get("Src")
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IssueInfo(AbstractModel):
    """签发信息

    """

    def __init__(self):
        r"""
        :param CertNumber: 编号
注意：此字段可能返回 null，表示取不到有效值。
        :type CertNumber: str
        :param IssuedAuthority: 签发机构
注意：此字段可能返回 null，表示取不到有效值。
        :type IssuedAuthority: str
        :param IssuedDate: 签发日期
注意：此字段可能返回 null，表示取不到有效值。
        :type IssuedDate: str
        """
        self.CertNumber = None
        self.IssuedAuthority = None
        self.IssuedDate = None


    def _deserialize(self, params):
        self.CertNumber = params.get("CertNumber")
        self.IssuedAuthority = params.get("IssuedAuthority")
        self.IssuedDate = params.get("IssuedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LastMenstrualPeriodBlock(AbstractModel):
    """末次月经

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Timestamp: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.Norm = None
        self.Type = None
        self.Timestamp = None
        self.Unit = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Norm = params.get("Norm")
        self.Type = params.get("Type")
        self.Timestamp = params.get("Timestamp")
        self.Unit = params.get("Unit")
        self.Value = params.get("Value")
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
        


class LymphNode(AbstractModel):
    """单淋巴结转移信息

    """

    def __init__(self):
        r"""
        :param Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: :class:`tencentcloud.mrs.v20200910.models.Part`
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Total: 总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param TransferNum: 转移数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferNum: int
        :param Sizes: 淋巴结大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Sizes: list of int
        :param Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Name = None
        self.Index = None
        self.Part = None
        self.Src = None
        self.Total = None
        self.TransferNum = None
        self.Sizes = None
        self.Coords = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Index = params.get("Index")
        if params.get("Part") is not None:
            self.Part = Part()
            self.Part._deserialize(params.get("Part"))
        self.Src = params.get("Src")
        self.Total = params.get("Total")
        self.TransferNum = params.get("TransferNum")
        self.Sizes = params.get("Sizes")
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LymphTotal(AbstractModel):
    """淋巴结总计转移信息

    """

    def __init__(self):
        r"""
        :param Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param TransferNum: 转移数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferNum: str
        :param Total: 总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Name = None
        self.TransferNum = None
        self.Total = None
        self.Src = None
        self.Index = None
        self.Coords = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TransferNum = params.get("TransferNum")
        self.Total = params.get("Total")
        self.Src = params.get("Src")
        self.Index = params.get("Index")
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MainDiseaseHistoryBlock(AbstractModel):
    """既往史

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: bool
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Neglist: 否定列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Neglist: :class:`tencentcloud.mrs.v20200910.models.NeglistBlock`
        :param Poslist: 肯定列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Poslist: :class:`tencentcloud.mrs.v20200910.models.PoslistBlock`
        """
        self.Name = None
        self.Src = None
        self.State = None
        self.Value = None
        self.Neglist = None
        self.Poslist = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.State = params.get("State")
        self.Value = params.get("Value")
        if params.get("Neglist") is not None:
            self.Neglist = NeglistBlock()
            self.Neglist._deserialize(params.get("Neglist"))
        if params.get("Poslist") is not None:
            self.Poslist = PoslistBlock()
            self.Poslist._deserialize(params.get("Poslist"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Maternity(AbstractModel):
    """孕产报告

    """

    def __init__(self):
        r"""
        :param Desc: 描述部分
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: :class:`tencentcloud.mrs.v20200910.models.MaternityDesc`
        :param Summary: 结论部分
注意：此字段可能返回 null，表示取不到有效值。
        :type Summary: :class:`tencentcloud.mrs.v20200910.models.MaternitySummary`
        :param OcrText: 报告原文
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrText: str
        """
        self.Desc = None
        self.Summary = None
        self.OcrText = None


    def _deserialize(self, params):
        if params.get("Desc") is not None:
            self.Desc = MaternityDesc()
            self.Desc._deserialize(params.get("Desc"))
        if params.get("Summary") is not None:
            self.Summary = MaternitySummary()
            self.Summary._deserialize(params.get("Summary"))
        self.OcrText = params.get("OcrText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaternityDesc(AbstractModel):
    """孕产描述部分

    """

    def __init__(self):
        r"""
        :param Fetus: 胎儿数据结构
注意：此字段可能返回 null，表示取不到有效值。
        :type Fetus: list of Fetus
        :param FetusNum: 胎儿数量
注意：此字段可能返回 null，表示取不到有效值。
        :type FetusNum: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param Text: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Fetus = None
        self.FetusNum = None
        self.Text = None
        self.Coords = None


    def _deserialize(self, params):
        if params.get("Fetus") is not None:
            self.Fetus = []
            for item in params.get("Fetus"):
                obj = Fetus()
                obj._deserialize(item)
                self.Fetus.append(obj)
        if params.get("FetusNum") is not None:
            self.FetusNum = FieldInfo()
            self.FetusNum._deserialize(params.get("FetusNum"))
        self.Text = params.get("Text")
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaternitySummary(AbstractModel):
    """孕产结论部分

    """

    def __init__(self):
        r"""
        :param Fetus: 胎儿数据结构
注意：此字段可能返回 null，表示取不到有效值。
        :type Fetus: list of Fetus
        :param FetusNum: 胎儿数量
注意：此字段可能返回 null，表示取不到有效值。
        :type FetusNum: :class:`tencentcloud.mrs.v20200910.models.FieldInfo`
        :param Sym: 病变
注意：此字段可能返回 null，表示取不到有效值。
        :type Sym: list of FieldInfo
        :param Text: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Fetus = None
        self.FetusNum = None
        self.Sym = None
        self.Text = None
        self.Coords = None


    def _deserialize(self, params):
        if params.get("Fetus") is not None:
            self.Fetus = []
            for item in params.get("Fetus"):
                obj = Fetus()
                obj._deserialize(item)
                self.Fetus.append(obj)
        if params.get("FetusNum") is not None:
            self.FetusNum = FieldInfo()
            self.FetusNum._deserialize(params.get("FetusNum"))
        if params.get("Sym") is not None:
            self.Sym = []
            for item in params.get("Sym"):
                obj = FieldInfo()
                obj._deserialize(item)
                self.Sym.append(obj)
        self.Text = params.get("Text")
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
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
        


class MenstrualFlowBlock(AbstractModel):
    """月经量

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MenstrualHistoryBlock(AbstractModel):
    """月经史

    """

    def __init__(self):
        r"""
        :param LastMenstrualPeriod: 末次月经
注意：此字段可能返回 null，表示取不到有效值。
        :type LastMenstrualPeriod: :class:`tencentcloud.mrs.v20200910.models.LastMenstrualPeriodBlock`
        :param MenstrualFlow: 月经量
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstrualFlow: :class:`tencentcloud.mrs.v20200910.models.MenstrualFlowBlock`
        :param MenarcheAge: 初潮时间
注意：此字段可能返回 null，表示取不到有效值。
        :type MenarcheAge: :class:`tencentcloud.mrs.v20200910.models.LastMenstrualPeriodBlock`
        :param MenstruationOrNot: 是否绝经
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstruationOrNot: :class:`tencentcloud.mrs.v20200910.models.MenstruationOrNotBlock`
        :param MenstrualCycles: 月经周期
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstrualCycles: :class:`tencentcloud.mrs.v20200910.models.LastMenstrualPeriodBlock`
        :param MenstrualPeriod: 月经经期
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstrualPeriod: :class:`tencentcloud.mrs.v20200910.models.MenstrualPeriodBlock`
        """
        self.LastMenstrualPeriod = None
        self.MenstrualFlow = None
        self.MenarcheAge = None
        self.MenstruationOrNot = None
        self.MenstrualCycles = None
        self.MenstrualPeriod = None


    def _deserialize(self, params):
        if params.get("LastMenstrualPeriod") is not None:
            self.LastMenstrualPeriod = LastMenstrualPeriodBlock()
            self.LastMenstrualPeriod._deserialize(params.get("LastMenstrualPeriod"))
        if params.get("MenstrualFlow") is not None:
            self.MenstrualFlow = MenstrualFlowBlock()
            self.MenstrualFlow._deserialize(params.get("MenstrualFlow"))
        if params.get("MenarcheAge") is not None:
            self.MenarcheAge = LastMenstrualPeriodBlock()
            self.MenarcheAge._deserialize(params.get("MenarcheAge"))
        if params.get("MenstruationOrNot") is not None:
            self.MenstruationOrNot = MenstruationOrNotBlock()
            self.MenstruationOrNot._deserialize(params.get("MenstruationOrNot"))
        if params.get("MenstrualCycles") is not None:
            self.MenstrualCycles = LastMenstrualPeriodBlock()
            self.MenstrualCycles._deserialize(params.get("MenstrualCycles"))
        if params.get("MenstrualPeriod") is not None:
            self.MenstrualPeriod = MenstrualPeriodBlock()
            self.MenstrualPeriod._deserialize(params.get("MenstrualPeriod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MenstrualHistoryDetailBlock(AbstractModel):
    """月经史

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param TimeType: 时间类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeType: str
        :param Timestamp: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.State = None
        self.Norm = None
        self.TimeType = None
        self.Timestamp = None
        self.Unit = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.State = params.get("State")
        self.Norm = params.get("Norm")
        self.TimeType = params.get("TimeType")
        self.Timestamp = params.get("Timestamp")
        self.Unit = params.get("Unit")
        self.Value = params.get("Value")
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
        


class MenstrualPeriodBlock(AbstractModel):
    """月经经期

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Timestamp: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.Norm = None
        self.Type = None
        self.Timestamp = None
        self.Unit = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Norm = params.get("Norm")
        self.Type = params.get("Type")
        self.Timestamp = params.get("Timestamp")
        self.Unit = params.get("Unit")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MenstruationOrNotBlock(AbstractModel):
    """是否绝经

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param TimeType: 时间类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeType: str
        :param Timestamp: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.Norm = None
        self.TimeType = None
        self.Timestamp = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Norm = params.get("Norm")
        self.TimeType = params.get("TimeType")
        self.Timestamp = params.get("Timestamp")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Molecular(AbstractModel):
    """分子病理

    """

    def __init__(self):
        r"""
        :param Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Name: 基因名称标注化
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 分子病理详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.mrs.v20200910.models.MolecularValue`
        :param Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Index = None
        self.Src = None
        self.Name = None
        self.Value = None
        self.Coords = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.Src = params.get("Src")
        self.Name = params.get("Name")
        if params.get("Value") is not None:
            self.Value = MolecularValue()
            self.Value._deserialize(params.get("Value"))
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MolecularValue(AbstractModel):
    """分子病理详细信息

    """

    def __init__(self):
        r"""
        :param Exon: 外显子
注意：此字段可能返回 null，表示取不到有效值。
        :type Exon: str
        :param Position: 点位
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: str
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Positive: 阳性或阴性
注意：此字段可能返回 null，表示取不到有效值。
        :type Positive: str
        :param Src: 基因名称原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        """
        self.Exon = None
        self.Position = None
        self.Type = None
        self.Positive = None
        self.Src = None


    def _deserialize(self, params):
        self.Exon = params.get("Exon")
        self.Position = params.get("Position")
        self.Type = params.get("Type")
        self.Positive = params.get("Positive")
        self.Src = params.get("Src")
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
        


class NeglistBlock(AbstractModel):
    """否定列表

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
        


class NeonatalInfo(AbstractModel):
    """新生儿信息

    """

    def __init__(self):
        r"""
        :param NeonatalName: 新生儿名字
注意：此字段可能返回 null，表示取不到有效值。
        :type NeonatalName: str
        :param NeonatalGender: 新生儿性别
注意：此字段可能返回 null，表示取不到有效值。
        :type NeonatalGender: str
        :param BirthLength: 出生身长
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthLength: str
        :param BirthWeight: 出生体重
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthWeight: str
        :param GestationalAge: 出生孕周
注意：此字段可能返回 null，表示取不到有效值。
        :type GestationalAge: str
        :param BirthTime: 出生时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthTime: str
        :param BirthPlace: 出生地点
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthPlace: str
        :param MedicalInstitutions: 医疗机构
注意：此字段可能返回 null，表示取不到有效值。
        :type MedicalInstitutions: str
        """
        self.NeonatalName = None
        self.NeonatalGender = None
        self.BirthLength = None
        self.BirthWeight = None
        self.GestationalAge = None
        self.BirthTime = None
        self.BirthPlace = None
        self.MedicalInstitutions = None


    def _deserialize(self, params):
        self.NeonatalName = params.get("NeonatalName")
        self.NeonatalGender = params.get("NeonatalGender")
        self.BirthLength = params.get("BirthLength")
        self.BirthWeight = params.get("BirthWeight")
        self.GestationalAge = params.get("GestationalAge")
        self.BirthTime = params.get("BirthTime")
        self.BirthPlace = params.get("BirthPlace")
        self.MedicalInstitutions = params.get("MedicalInstitutions")
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
        :param PartDetail: 部位详情
注意：此字段可能返回 null，表示取不到有效值。
        :type PartDetail: :class:`tencentcloud.mrs.v20200910.models.PartDesc`
        """
        self.Part = None
        self.PartDirection = None
        self.Tissue = None
        self.TissueDirection = None
        self.Upper = None
        self.PartDetail = None


    def _deserialize(self, params):
        self.Part = params.get("Part")
        self.PartDirection = params.get("PartDirection")
        self.Tissue = params.get("Tissue")
        self.TissueDirection = params.get("TissueDirection")
        self.Upper = params.get("Upper")
        if params.get("PartDetail") is not None:
            self.PartDetail = PartDesc()
            self.PartDetail._deserialize(params.get("PartDetail"))
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
        :param Impl: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Impl: str
        """
        self.Number = None
        self.Type = None
        self.Unit = None
        self.Impl = None


    def _deserialize(self, params):
        self.Number = params.get("Number")
        self.Type = params.get("Type")
        self.Unit = params.get("Unit")
        self.Impl = params.get("Impl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NumValue(AbstractModel):
    """数值结构体

    """

    def __init__(self):
        r"""
        :param Num: 数值
注意：此字段可能返回 null，表示取不到有效值。
        :type Num: str
        :param Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        """
        self.Num = None
        self.Unit = None


    def _deserialize(self, params):
        self.Num = params.get("Num")
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
        


class ObstetricalHistoryBlock(AbstractModel):
    """婚姻-生育史

    """

    def __init__(self):
        r"""
        :param MarriageHistory: 婚姻史
注意：此字段可能返回 null，表示取不到有效值。
        :type MarriageHistory: :class:`tencentcloud.mrs.v20200910.models.MenstrualHistoryDetailBlock`
        :param FertilityHistory: 婚育史
注意：此字段可能返回 null，表示取不到有效值。
        :type FertilityHistory: :class:`tencentcloud.mrs.v20200910.models.FertilityHistoryBlock`
        """
        self.MarriageHistory = None
        self.FertilityHistory = None


    def _deserialize(self, params):
        if params.get("MarriageHistory") is not None:
            self.MarriageHistory = MenstrualHistoryDetailBlock()
            self.MarriageHistory._deserialize(params.get("MarriageHistory"))
        if params.get("FertilityHistory") is not None:
            self.FertilityHistory = FertilityHistoryBlock()
            self.FertilityHistory._deserialize(params.get("FertilityHistory"))
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
        :param Transparent: 透声度
注意：此字段可能返回 null，表示取不到有效值。
        :type Transparent: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param MriAdc: MRI ADC
注意：此字段可能返回 null，表示取不到有效值。
        :type MriAdc: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param MriDwi: MRI DWI
注意：此字段可能返回 null，表示取不到有效值。
        :type MriDwi: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param MriT1: MRI T1信号
注意：此字段可能返回 null，表示取不到有效值。
        :type MriT1: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param MriT2: MRI T2信号
注意：此字段可能返回 null，表示取不到有效值。
        :type MriT2: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param CtHu: CT HU值
注意：此字段可能返回 null，表示取不到有效值。
        :type CtHu: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Suvmax: SUmax值
注意：此字段可能返回 null，表示取不到有效值。
        :type Suvmax: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Metabolism: 代谢情况
注意：此字段可能返回 null，表示取不到有效值。
        :type Metabolism: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param RadioactiveUptake: 放射性摄取
注意：此字段可能返回 null，表示取不到有效值。
        :type RadioactiveUptake: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param LymphEnlargement: 淋巴结情况
注意：此字段可能返回 null，表示取不到有效值。
        :type LymphEnlargement: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param ImageFeature: 影像特征
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageFeature: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Duct: 导管
注意：此字段可能返回 null，表示取不到有效值。
        :type Duct: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Trend: 趋势
注意：此字段可能返回 null，表示取不到有效值。
        :type Trend: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Operation: 手术情况
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Coords: 器官在报告图片中的坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
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
        self.Transparent = None
        self.MriAdc = None
        self.MriDwi = None
        self.MriT1 = None
        self.MriT2 = None
        self.CtHu = None
        self.Suvmax = None
        self.Metabolism = None
        self.RadioactiveUptake = None
        self.LymphEnlargement = None
        self.ImageFeature = None
        self.Duct = None
        self.Trend = None
        self.Operation = None
        self.Coords = None


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
        if params.get("Transparent") is not None:
            self.Transparent = BlockInfo()
            self.Transparent._deserialize(params.get("Transparent"))
        if params.get("MriAdc") is not None:
            self.MriAdc = BlockInfo()
            self.MriAdc._deserialize(params.get("MriAdc"))
        if params.get("MriDwi") is not None:
            self.MriDwi = BlockInfo()
            self.MriDwi._deserialize(params.get("MriDwi"))
        if params.get("MriT1") is not None:
            self.MriT1 = BlockInfo()
            self.MriT1._deserialize(params.get("MriT1"))
        if params.get("MriT2") is not None:
            self.MriT2 = BlockInfo()
            self.MriT2._deserialize(params.get("MriT2"))
        if params.get("CtHu") is not None:
            self.CtHu = BlockInfo()
            self.CtHu._deserialize(params.get("CtHu"))
        if params.get("Suvmax") is not None:
            self.Suvmax = BlockInfo()
            self.Suvmax._deserialize(params.get("Suvmax"))
        if params.get("Metabolism") is not None:
            self.Metabolism = BlockInfo()
            self.Metabolism._deserialize(params.get("Metabolism"))
        if params.get("RadioactiveUptake") is not None:
            self.RadioactiveUptake = BlockInfo()
            self.RadioactiveUptake._deserialize(params.get("RadioactiveUptake"))
        if params.get("LymphEnlargement") is not None:
            self.LymphEnlargement = BlockInfo()
            self.LymphEnlargement._deserialize(params.get("LymphEnlargement"))
        if params.get("ImageFeature") is not None:
            self.ImageFeature = BlockInfo()
            self.ImageFeature._deserialize(params.get("ImageFeature"))
        if params.get("Duct") is not None:
            self.Duct = BlockInfo()
            self.Duct._deserialize(params.get("Duct"))
        if params.get("Trend") is not None:
            self.Trend = BlockInfo()
            self.Trend._deserialize(params.get("Trend"))
        if params.get("Operation") is not None:
            self.Operation = BlockInfo()
            self.Operation._deserialize(params.get("Operation"))
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OtherInfo(AbstractModel):
    """其他信息

    """

    def __init__(self):
        r"""
        :param Anesthesia: 麻醉方法
注意：此字段可能返回 null，表示取不到有效值。
        :type Anesthesia: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param BloodLoss: 术中出血
注意：此字段可能返回 null，表示取不到有效值。
        :type BloodLoss: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param BloodTransfusion: 输血
注意：此字段可能返回 null，表示取不到有效值。
        :type BloodTransfusion: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param Duration: 手术用时
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param EndTime: 手术开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        :param StartTime: 手术结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: :class:`tencentcloud.mrs.v20200910.models.SurgeryAttr`
        """
        self.Anesthesia = None
        self.BloodLoss = None
        self.BloodTransfusion = None
        self.Duration = None
        self.EndTime = None
        self.StartTime = None


    def _deserialize(self, params):
        if params.get("Anesthesia") is not None:
            self.Anesthesia = SurgeryAttr()
            self.Anesthesia._deserialize(params.get("Anesthesia"))
        if params.get("BloodLoss") is not None:
            self.BloodLoss = SurgeryAttr()
            self.BloodLoss._deserialize(params.get("BloodLoss"))
        if params.get("BloodTransfusion") is not None:
            self.BloodTransfusion = SurgeryAttr()
            self.BloodTransfusion._deserialize(params.get("BloodTransfusion"))
        if params.get("Duration") is not None:
            self.Duration = SurgeryAttr()
            self.Duration._deserialize(params.get("Duration"))
        if params.get("EndTime") is not None:
            self.EndTime = SurgeryAttr()
            self.EndTime._deserialize(params.get("EndTime"))
        if params.get("StartTime") is not None:
            self.StartTime = SurgeryAttr()
            self.StartTime._deserialize(params.get("StartTime"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PTNM(AbstractModel):
    """pTNM

    """

    def __init__(self):
        r"""
        :param Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param PT: pT
注意：此字段可能返回 null，表示取不到有效值。
        :type PT: str
        :param PN: pN
注意：此字段可能返回 null，表示取不到有效值。
        :type PN: str
        :param PM: pM
注意：此字段可能返回 null，表示取不到有效值。
        :type PM: str
        :param Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Name = None
        self.Index = None
        self.Src = None
        self.Value = None
        self.PT = None
        self.PN = None
        self.PM = None
        self.Coords = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Index = params.get("Index")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        self.PT = params.get("PT")
        self.PN = params.get("PN")
        self.PM = params.get("PM")
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PTNMBlock(AbstractModel):
    """PTNM分期

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param PTNMM: PTNM分期
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNMM: str
        :param PTNMN: PTNM分期
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNMN: str
        :param PTNMT: PTNM分期
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNMT: str
        """
        self.Name = None
        self.Src = None
        self.PTNMM = None
        self.PTNMN = None
        self.PTNMT = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.PTNMM = params.get("PTNMM")
        self.PTNMN = params.get("PTNMN")
        self.PTNMT = params.get("PTNMT")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParagraphBlock(AbstractModel):
    """文本块

    """

    def __init__(self):
        r"""
        :param IncisionHealingText: 切口愈合情况
注意：此字段可能返回 null，表示取不到有效值。
        :type IncisionHealingText: str
        :param AuxiliaryExaminationText: 辅助检查
注意：此字段可能返回 null，表示取不到有效值。
        :type AuxiliaryExaminationText: str
        :param SpecialExamText: 特殊检查
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecialExamText: str
        :param OutpatientDiagnosisText: 门诊诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type OutpatientDiagnosisText: str
        :param AdmissionConditionText: 入院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionConditionText: str
        :param CheckAndTreatmentProcessText: 诊疗经过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckAndTreatmentProcessText: str
        :param SymptomsAndSignsText: 体征
注意：此字段可能返回 null，表示取不到有效值。
        :type SymptomsAndSignsText: str
        :param DischargeInstructionsText: 出院医嘱
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeInstructionsText: str
        :param AdmissionDiagnosisText: 入院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionDiagnosisText: str
        :param SurgeryConditionText: 手术情况
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryConditionText: str
        :param PathologicalDiagnosisText: 病理诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type PathologicalDiagnosisText: str
        :param DischargeConditionText: 出院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeConditionText: str
        :param CheckRecordText: 检查记录

注意：此字段可能返回 null，表示取不到有效值。
        :type CheckRecordText: str
        :param ChiefComplaintText: 主诉
注意：此字段可能返回 null，表示取不到有效值。
        :type ChiefComplaintText: str
        :param DischargeDiagnosisText: 出院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeDiagnosisText: str
        :param MainDiseaseHistoryText: 既往史
注意：此字段可能返回 null，表示取不到有效值。
        :type MainDiseaseHistoryText: str
        :param DiseasePresentText: 现病史
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseasePresentText: str
        :param PersonalHistoryText: 个人史
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonalHistoryText: str
        :param MenstruallHistoryText: 月经史
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstruallHistoryText: str
        :param ObstericalHistoryText: 婚育史
注意：此字段可能返回 null，表示取不到有效值。
        :type ObstericalHistoryText: str
        :param FamilyHistoryText: 家族史
注意：此字段可能返回 null，表示取不到有效值。
        :type FamilyHistoryText: str
        :param AllergyHistoryText: 过敏史
注意：此字段可能返回 null，表示取不到有效值。
        :type AllergyHistoryText: str
        :param DiseaseHistoryText: 病史信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseaseHistoryText: str
        :param OtherDiagnosisText: 其它诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherDiagnosisText: str
        :param BodyExaminationText: 体格检查
注意：此字段可能返回 null，表示取不到有效值。
        :type BodyExaminationText: str
        :param SpecialistExaminationText: 专科检查
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecialistExaminationText: str
        :param TreatmentResultText: 治疗结果
注意：此字段可能返回 null，表示取不到有效值。
        :type TreatmentResultText: str
        """
        self.IncisionHealingText = None
        self.AuxiliaryExaminationText = None
        self.SpecialExamText = None
        self.OutpatientDiagnosisText = None
        self.AdmissionConditionText = None
        self.CheckAndTreatmentProcessText = None
        self.SymptomsAndSignsText = None
        self.DischargeInstructionsText = None
        self.AdmissionDiagnosisText = None
        self.SurgeryConditionText = None
        self.PathologicalDiagnosisText = None
        self.DischargeConditionText = None
        self.CheckRecordText = None
        self.ChiefComplaintText = None
        self.DischargeDiagnosisText = None
        self.MainDiseaseHistoryText = None
        self.DiseasePresentText = None
        self.PersonalHistoryText = None
        self.MenstruallHistoryText = None
        self.ObstericalHistoryText = None
        self.FamilyHistoryText = None
        self.AllergyHistoryText = None
        self.DiseaseHistoryText = None
        self.OtherDiagnosisText = None
        self.BodyExaminationText = None
        self.SpecialistExaminationText = None
        self.TreatmentResultText = None


    def _deserialize(self, params):
        self.IncisionHealingText = params.get("IncisionHealingText")
        self.AuxiliaryExaminationText = params.get("AuxiliaryExaminationText")
        self.SpecialExamText = params.get("SpecialExamText")
        self.OutpatientDiagnosisText = params.get("OutpatientDiagnosisText")
        self.AdmissionConditionText = params.get("AdmissionConditionText")
        self.CheckAndTreatmentProcessText = params.get("CheckAndTreatmentProcessText")
        self.SymptomsAndSignsText = params.get("SymptomsAndSignsText")
        self.DischargeInstructionsText = params.get("DischargeInstructionsText")
        self.AdmissionDiagnosisText = params.get("AdmissionDiagnosisText")
        self.SurgeryConditionText = params.get("SurgeryConditionText")
        self.PathologicalDiagnosisText = params.get("PathologicalDiagnosisText")
        self.DischargeConditionText = params.get("DischargeConditionText")
        self.CheckRecordText = params.get("CheckRecordText")
        self.ChiefComplaintText = params.get("ChiefComplaintText")
        self.DischargeDiagnosisText = params.get("DischargeDiagnosisText")
        self.MainDiseaseHistoryText = params.get("MainDiseaseHistoryText")
        self.DiseasePresentText = params.get("DiseasePresentText")
        self.PersonalHistoryText = params.get("PersonalHistoryText")
        self.MenstruallHistoryText = params.get("MenstruallHistoryText")
        self.ObstericalHistoryText = params.get("ObstericalHistoryText")
        self.FamilyHistoryText = params.get("FamilyHistoryText")
        self.AllergyHistoryText = params.get("AllergyHistoryText")
        self.DiseaseHistoryText = params.get("DiseaseHistoryText")
        self.OtherDiagnosisText = params.get("OtherDiagnosisText")
        self.BodyExaminationText = params.get("BodyExaminationText")
        self.SpecialistExaminationText = params.get("SpecialistExaminationText")
        self.TreatmentResultText = params.get("TreatmentResultText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParentInfo(AbstractModel):
    """母亲或父亲信息

    """

    def __init__(self):
        r"""
        :param Name: 名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Age: 年龄
注意：此字段可能返回 null，表示取不到有效值。
        :type Age: str
        :param IdCard: 证件号
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCard: str
        :param Ethnicity: 民族
注意：此字段可能返回 null，表示取不到有效值。
        :type Ethnicity: str
        :param Nationality: 国籍
注意：此字段可能返回 null，表示取不到有效值。
        :type Nationality: str
        :param Address: 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        """
        self.Name = None
        self.Age = None
        self.IdCard = None
        self.Ethnicity = None
        self.Nationality = None
        self.Address = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Age = params.get("Age")
        self.IdCard = params.get("IdCard")
        self.Ethnicity = params.get("Ethnicity")
        self.Nationality = params.get("Nationality")
        self.Address = params.get("Address")
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
        :param ValueBrief: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueBrief: str
        """
        self.Index = None
        self.NormPart = None
        self.Src = None
        self.Value = None
        self.Name = None
        self.ValueBrief = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        if params.get("NormPart") is not None:
            self.NormPart = NormPart()
            self.NormPart._deserialize(params.get("NormPart"))
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        self.Name = params.get("Name")
        self.ValueBrief = params.get("ValueBrief")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartDesc(AbstractModel):
    """部位描述

    """

    def __init__(self):
        r"""
        :param MainDir: 主要部位
注意：此字段可能返回 null，表示取不到有效值。
        :type MainDir: str
        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: str
        :param SecondaryDir: 次要部位
注意：此字段可能返回 null，表示取不到有效值。
        :type SecondaryDir: str
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.MainDir = None
        self.Part = None
        self.SecondaryDir = None
        self.Type = None


    def _deserialize(self, params):
        self.MainDir = params.get("MainDir")
        self.Part = params.get("Part")
        self.SecondaryDir = params.get("SecondaryDir")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathologicalDiagnosisBlock(AbstractModel):
    """病理诊断

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Detail: 病理详细
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: list of PathologicalDiagnosisDetailBlock
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.Detail = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = PathologicalDiagnosisDetailBlock()
                obj._deserialize(item)
                self.Detail.append(obj)
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathologicalDiagnosisDetailBlock(AbstractModel):
    """病理详细

    """

    def __init__(self):
        r"""
        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: str
        :param HistologicalType: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type HistologicalType: str
        :param HistologicalGrade: 等级
注意：此字段可能返回 null，表示取不到有效值。
        :type HistologicalGrade: str
        """
        self.Part = None
        self.HistologicalType = None
        self.HistologicalGrade = None


    def _deserialize(self, params):
        self.Part = params.get("Part")
        self.HistologicalType = params.get("HistologicalType")
        self.HistologicalGrade = params.get("HistologicalGrade")
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
        


class PathologyV2(AbstractModel):
    """病理报告v2

    """

    def __init__(self):
        r"""
        :param PathologicalReportType: 报告类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PathologicalReportType: :class:`tencentcloud.mrs.v20200910.models.Report`
        :param Desc: 描述段落
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: :class:`tencentcloud.mrs.v20200910.models.DescInfo`
        :param Summary: 诊断结论
注意：此字段可能返回 null，表示取不到有效值。
        :type Summary: :class:`tencentcloud.mrs.v20200910.models.SummaryInfo`
        :param ReportText: 报告全文
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportText: str
        :param LymphTotal: 淋巴结总计转移信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LymphTotal: list of LymphTotal
        :param LymphNodes: 单淋巴结转移信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LymphNodes: list of LymphNode
        :param Ihc: ihc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Ihc: list of IHCV2
        :param Clinical: 临床诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type Clinical: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param Precancer: 是否癌前病变
注意：此字段可能返回 null，表示取不到有效值。
        :type Precancer: :class:`tencentcloud.mrs.v20200910.models.HistologyClass`
        :param Malignant: 是否恶性肿瘤
注意：此字段可能返回 null，表示取不到有效值。
        :type Malignant: :class:`tencentcloud.mrs.v20200910.models.HistologyClass`
        :param Benigntumor: 是否良性肿瘤
注意：此字段可能返回 null，表示取不到有效值。
        :type Benigntumor: :class:`tencentcloud.mrs.v20200910.models.HistologyClass`
        :param SampleType: 送检材料
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleType: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param LymphSize: 淋巴结大小
注意：此字段可能返回 null，表示取不到有效值。
        :type LymphSize: list of Size
        :param Molecular: 分子病理
注意：此字段可能返回 null，表示取不到有效值。
        :type Molecular: list of Molecular
        """
        self.PathologicalReportType = None
        self.Desc = None
        self.Summary = None
        self.ReportText = None
        self.LymphTotal = None
        self.LymphNodes = None
        self.Ihc = None
        self.Clinical = None
        self.Precancer = None
        self.Malignant = None
        self.Benigntumor = None
        self.SampleType = None
        self.LymphSize = None
        self.Molecular = None


    def _deserialize(self, params):
        if params.get("PathologicalReportType") is not None:
            self.PathologicalReportType = Report()
            self.PathologicalReportType._deserialize(params.get("PathologicalReportType"))
        if params.get("Desc") is not None:
            self.Desc = DescInfo()
            self.Desc._deserialize(params.get("Desc"))
        if params.get("Summary") is not None:
            self.Summary = SummaryInfo()
            self.Summary._deserialize(params.get("Summary"))
        self.ReportText = params.get("ReportText")
        if params.get("LymphTotal") is not None:
            self.LymphTotal = []
            for item in params.get("LymphTotal"):
                obj = LymphTotal()
                obj._deserialize(item)
                self.LymphTotal.append(obj)
        if params.get("LymphNodes") is not None:
            self.LymphNodes = []
            for item in params.get("LymphNodes"):
                obj = LymphNode()
                obj._deserialize(item)
                self.LymphNodes.append(obj)
        if params.get("Ihc") is not None:
            self.Ihc = []
            for item in params.get("Ihc"):
                obj = IHCV2()
                obj._deserialize(item)
                self.Ihc.append(obj)
        if params.get("Clinical") is not None:
            self.Clinical = BaseInfo()
            self.Clinical._deserialize(params.get("Clinical"))
        if params.get("Precancer") is not None:
            self.Precancer = HistologyClass()
            self.Precancer._deserialize(params.get("Precancer"))
        if params.get("Malignant") is not None:
            self.Malignant = HistologyClass()
            self.Malignant._deserialize(params.get("Malignant"))
        if params.get("Benigntumor") is not None:
            self.Benigntumor = HistologyClass()
            self.Benigntumor._deserialize(params.get("Benigntumor"))
        if params.get("SampleType") is not None:
            self.SampleType = BaseInfo()
            self.SampleType._deserialize(params.get("SampleType"))
        if params.get("LymphSize") is not None:
            self.LymphSize = []
            for item in params.get("LymphSize"):
                obj = Size()
                obj._deserialize(item)
                self.LymphSize.append(obj)
        if params.get("Molecular") is not None:
            self.Molecular = []
            for item in params.get("Molecular"):
                obj = Molecular()
                obj._deserialize(item)
                self.Molecular.append(obj)
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
        :param BedNo: 床号
注意：此字段可能返回 null，表示取不到有效值。
        :type BedNo: str
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
        self.BedNo = None


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
        self.BedNo = params.get("BedNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonalHistoryBlock(AbstractModel):
    """个人史

    """

    def __init__(self):
        r"""
        :param BirthPlace: 出生地
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthPlace: :class:`tencentcloud.mrs.v20200910.models.BirthPlaceBlock`
        :param LivePlace: 居住地
注意：此字段可能返回 null，表示取不到有效值。
        :type LivePlace: :class:`tencentcloud.mrs.v20200910.models.BirthPlaceBlock`
        :param Job: 职业
注意：此字段可能返回 null，表示取不到有效值。
        :type Job: :class:`tencentcloud.mrs.v20200910.models.BirthPlaceBlock`
        :param SmokeHistory: 吸烟
注意：此字段可能返回 null，表示取不到有效值。
        :type SmokeHistory: :class:`tencentcloud.mrs.v20200910.models.SmokeHistoryBlock`
        :param AlcoholicHistory: 喝酒
注意：此字段可能返回 null，表示取不到有效值。
        :type AlcoholicHistory: :class:`tencentcloud.mrs.v20200910.models.SmokeHistoryBlock`
        :param MenstrualHistory: 月经史
注意：此字段可能返回 null，表示取不到有效值。
        :type MenstrualHistory: :class:`tencentcloud.mrs.v20200910.models.MenstrualHistoryBlock`
        :param ObstericalHistory: 婚姻-生育史
注意：此字段可能返回 null，表示取不到有效值。
        :type ObstericalHistory: :class:`tencentcloud.mrs.v20200910.models.ObstetricalHistoryBlock`
        :param FamilyHistory: 家族史
注意：此字段可能返回 null，表示取不到有效值。
        :type FamilyHistory: :class:`tencentcloud.mrs.v20200910.models.FamilyHistoryBlock`
        """
        self.BirthPlace = None
        self.LivePlace = None
        self.Job = None
        self.SmokeHistory = None
        self.AlcoholicHistory = None
        self.MenstrualHistory = None
        self.ObstericalHistory = None
        self.FamilyHistory = None


    def _deserialize(self, params):
        if params.get("BirthPlace") is not None:
            self.BirthPlace = BirthPlaceBlock()
            self.BirthPlace._deserialize(params.get("BirthPlace"))
        if params.get("LivePlace") is not None:
            self.LivePlace = BirthPlaceBlock()
            self.LivePlace._deserialize(params.get("LivePlace"))
        if params.get("Job") is not None:
            self.Job = BirthPlaceBlock()
            self.Job._deserialize(params.get("Job"))
        if params.get("SmokeHistory") is not None:
            self.SmokeHistory = SmokeHistoryBlock()
            self.SmokeHistory._deserialize(params.get("SmokeHistory"))
        if params.get("AlcoholicHistory") is not None:
            self.AlcoholicHistory = SmokeHistoryBlock()
            self.AlcoholicHistory._deserialize(params.get("AlcoholicHistory"))
        if params.get("MenstrualHistory") is not None:
            self.MenstrualHistory = MenstrualHistoryBlock()
            self.MenstrualHistory._deserialize(params.get("MenstrualHistory"))
        if params.get("ObstericalHistory") is not None:
            self.ObstericalHistory = ObstetricalHistoryBlock()
            self.ObstericalHistory._deserialize(params.get("ObstericalHistory"))
        if params.get("FamilyHistory") is not None:
            self.FamilyHistory = FamilyHistoryBlock()
            self.FamilyHistory._deserialize(params.get("FamilyHistory"))
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
        


class Point(AbstractModel):
    """点坐标

    """

    def __init__(self):
        r"""
        :param X: x坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type X: int
        :param Y: y坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: int
        """
        self.X = None
        self.Y = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoslistBlock(AbstractModel):
    """肯定列表

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
        


class Rectangle(AbstractModel):
    """位置坐标

    """

    def __init__(self):
        r"""
        :param X: x坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type X: int
        :param Y: y坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: int
        :param W: 宽
注意：此字段可能返回 null，表示取不到有效值。
        :type W: int
        :param H: 高
注意：此字段可能返回 null，表示取不到有效值。
        :type H: int
        """
        self.X = None
        self.Y = None
        self.W = None
        self.H = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.W = params.get("W")
        self.H = params.get("H")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelapseDateBlock(AbstractModel):
    """复发时间

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param DiseaseName: 疾病名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseaseName: str
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Norm: 归一化值
注意：此字段可能返回 null，表示取不到有效值。
        :type Norm: str
        :param Unit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param Timestamp: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.DiseaseName = None
        self.Type = None
        self.Norm = None
        self.Unit = None
        self.Timestamp = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.DiseaseName = params.get("DiseaseName")
        self.Type = params.get("Type")
        self.Norm = params.get("Norm")
        self.Unit = params.get("Unit")
        self.Timestamp = params.get("Timestamp")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelativeCancerHistoryBlock(AbstractModel):
    """家族肿瘤史

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param RelativeCancerList: 肿瘤史列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RelativeCancerList: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.RelativeCancerList = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.RelativeCancerList = params.get("RelativeCancerList")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelativeHistoryBlock(AbstractModel):
    """家庭成员

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Detail: 成员列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: list of RelativeHistoryDetailBlock
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Detail = None
        self.Src = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = RelativeHistoryDetailBlock()
                obj._deserialize(item)
                self.Detail.append(obj)
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelativeHistoryDetailBlock(AbstractModel):
    """家庭成员详情

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Relation: 关系
注意：此字段可能返回 null，表示取不到有效值。
        :type Relation: str
        :param TimeOfDeath: 死亡时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeOfDeath: str
        :param TimeType: 时间类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeType: str
        """
        self.Name = None
        self.Relation = None
        self.TimeOfDeath = None
        self.TimeType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Relation = params.get("Relation")
        self.TimeOfDeath = params.get("TimeOfDeath")
        self.TimeType = params.get("TimeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Report(AbstractModel):
    """报告类型

    """

    def __init__(self):
        r"""
        :param Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Index: 索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: list of int
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 报告类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Coords: 原文对应坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Name = None
        self.Index = None
        self.Src = None
        self.Value = None
        self.Coords = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Index = params.get("Index")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
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
        :param CheckItem: 检查项目
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckItem: str
        :param CheckMethod: 检查方法
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckMethod: str
        :param DiagnoseTime: 诊断时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagnoseTime: str
        :param HealthCheckupNum: 体检号
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheckupNum: str
        :param OtherTime: 其它时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherTime: str
        :param PrintTime: 打印时间
注意：此字段可能返回 null，表示取不到有效值。
        :type PrintTime: str
        :param Times: 未归类时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Times: list of Time
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
        self.CheckItem = None
        self.CheckMethod = None
        self.DiagnoseTime = None
        self.HealthCheckupNum = None
        self.OtherTime = None
        self.PrintTime = None
        self.Times = None


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
        self.CheckItem = params.get("CheckItem")
        self.CheckMethod = params.get("CheckMethod")
        self.DiagnoseTime = params.get("DiagnoseTime")
        self.HealthCheckupNum = params.get("HealthCheckupNum")
        self.OtherTime = params.get("OtherTime")
        self.PrintTime = params.get("PrintTime")
        if params.get("Times") is not None:
            self.Times = []
            for item in params.get("Times"):
                obj = Time()
                obj._deserialize(item)
                self.Times.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportTypeVersion(AbstractModel):
    """指定报告类型选用其结构化版本

    """

    def __init__(self):
        r"""
        :param ReportType: 检验报告
        :type ReportType: int
        :param Version: 版本2
        :type Version: int
        """
        self.ReportType = None
        self.Version = None


    def _deserialize(self, params):
        self.ReportType = params.get("ReportType")
        self.Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultInfo(AbstractModel):
    """结论信息

    """

    def __init__(self):
        r"""
        :param Text: 段落文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param Items: 结论详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of BaseInfo
        """
        self.Text = None
        self.Items = None


    def _deserialize(self, params):
        if params.get("Text") is not None:
            self.Text = BaseInfo()
            self.Text._deserialize(params.get("Text"))
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = BaseInfo()
                obj._deserialize(item)
                self.Items.append(obj)
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
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self.Index = None
        self.NormSize = None
        self.Src = None
        self.Value = None
        self.Name = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        if params.get("NormSize") is not None:
            self.NormSize = NormSize()
            self.NormSize._deserialize(params.get("NormSize"))
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmokeHistoryBlock(AbstractModel):
    """吸烟史

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param TimeUnit: 时间单位
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param TimeNorm: 时间归一化
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeNorm: str
        :param Amount: 吸烟量
注意：此字段可能返回 null，表示取不到有效值。
        :type Amount: str
        :param QuitState: 戒烟状态
注意：此字段可能返回 null，表示取不到有效值。
        :type QuitState: bool
        :param State: 是否吸烟
注意：此字段可能返回 null，表示取不到有效值。
        :type State: bool
        :param Value: 对外输出值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.TimeUnit = None
        self.TimeNorm = None
        self.Amount = None
        self.QuitState = None
        self.State = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeNorm = params.get("TimeNorm")
        self.Amount = params.get("Amount")
        self.QuitState = params.get("QuitState")
        self.State = params.get("State")
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
        :param Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Symptom = None
        self.Text = None
        self.Coords = None


    def _deserialize(self, params):
        if params.get("Symptom") is not None:
            self.Symptom = []
            for item in params.get("Symptom"):
                obj = SymptomInfo()
                obj._deserialize(item)
                self.Symptom.append(obj)
        self.Text = params.get("Text")
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SummaryInfo(AbstractModel):
    """诊断结论

    """

    def __init__(self):
        r"""
        :param Text: 诊断结论文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: :class:`tencentcloud.mrs.v20200910.models.BaseInfo`
        :param Infos: 诊断结论详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Infos: list of DetailInformation
        """
        self.Text = None
        self.Infos = None


    def _deserialize(self, params):
        if params.get("Text") is not None:
            self.Text = BaseInfo()
            self.Text._deserialize(params.get("Text"))
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = DetailInformation()
                obj._deserialize(item)
                self.Infos.append(obj)
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
        :param OtherInfo: 其他信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherInfo: :class:`tencentcloud.mrs.v20200910.models.OtherInfo`
        """
        self.SurgeryHistory = None
        self.OtherInfo = None


    def _deserialize(self, params):
        if params.get("SurgeryHistory") is not None:
            self.SurgeryHistory = SurgeryHistory()
            self.SurgeryHistory._deserialize(params.get("SurgeryHistory"))
        if params.get("OtherInfo") is not None:
            self.OtherInfo = OtherInfo()
            self.OtherInfo._deserialize(params.get("OtherInfo"))
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
        


class SurgeryConditionBlock(AbstractModel):
    """手术经过

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param SurgeryList: 手术历史
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryList: list of SurgeryListBlock
        :param Value: 对外输出值

注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.SurgeryList = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        if params.get("SurgeryList") is not None:
            self.SurgeryList = []
            for item in params.get("SurgeryList"):
                obj = SurgeryListBlock()
                obj._deserialize(item)
                self.SurgeryList.append(obj)
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
        


class SurgeryHistoryBlock(AbstractModel):
    """手术史

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Surgerylist: 手术列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Surgerylist: list of SurgeryListBlock
        """
        self.Name = None
        self.Src = None
        self.Value = None
        self.Surgerylist = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.Value = params.get("Value")
        if params.get("Surgerylist") is not None:
            self.Surgerylist = []
            for item in params.get("Surgerylist"):
                obj = SurgeryListBlock()
                obj._deserialize(item)
                self.Surgerylist.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SurgeryListBlock(AbstractModel):
    """手术列表

    """

    def __init__(self):
        r"""
        :param Time: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: str
        :param TimeType: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeType: str
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: list of str
        :param Part: 部位
注意：此字段可能返回 null，表示取不到有效值。
        :type Part: str
        """
        self.Time = None
        self.TimeType = None
        self.Name = None
        self.Part = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.TimeType = params.get("TimeType")
        self.Name = params.get("Name")
        self.Part = params.get("Part")
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
        :param Coords: 坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
        """
        self.Grade = None
        self.Part = None
        self.Index = None
        self.Symptom = None
        self.Attrs = None
        self.Src = None
        self.Coords = None


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
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableIndicators(AbstractModel):
    """检验报告结构

    """

    def __init__(self):
        r"""
        :param Indicators: 项目列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Indicators: list of IndicatorItemV2
        :param Sample: 采样标本
注意：此字段可能返回 null，表示取不到有效值。
        :type Sample: :class:`tencentcloud.mrs.v20200910.models.BaseItem`
        """
        self.Indicators = None
        self.Sample = None


    def _deserialize(self, params):
        if params.get("Indicators") is not None:
            self.Indicators = []
            for item in params.get("Indicators"):
                obj = IndicatorItemV2()
                obj._deserialize(item)
                self.Indicators.append(obj)
        if params.get("Sample") is not None:
            self.Sample = BaseItem()
            self.Sample._deserialize(params.get("Sample"))
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
        :param VaccineCertificate: 疫苗接种凭证
注意：此字段可能返回 null，表示取不到有效值。
        :type VaccineCertificate: :class:`tencentcloud.mrs.v20200910.models.VaccineCertificate`
        :param OcrText: OCR文本
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrText: str
        :param OcrResult: OCR拼接后文本
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrResult: str
        :param ReportTypeDesc: 报告类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportTypeDesc: str
        :param PathologyV2: 病理报告v2
注意：此字段可能返回 null，表示取不到有效值。
        :type PathologyV2: :class:`tencentcloud.mrs.v20200910.models.PathologyV2`
        :param C14: 碳14尿素呼气试验
注意：此字段可能返回 null，表示取不到有效值。
        :type C14: :class:`tencentcloud.mrs.v20200910.models.Indicator`
        :param Exame: 体检结论
注意：此字段可能返回 null，表示取不到有效值。
        :type Exame: :class:`tencentcloud.mrs.v20200910.models.Exame`
        :param MedDocV2: 出院报告v2，入院报告v2，门诊病历v2
注意：此字段可能返回 null，表示取不到有效值。
        :type MedDocV2: :class:`tencentcloud.mrs.v20200910.models.DischargeInfoBlock`
        :param IndicatorV3: 检验报告v3
注意：此字段可能返回 null，表示取不到有效值。
        :type IndicatorV3: :class:`tencentcloud.mrs.v20200910.models.IndicatorV3`
        :param Covid: 核酸报告
注意：此字段可能返回 null，表示取不到有效值。
        :type Covid: :class:`tencentcloud.mrs.v20200910.models.CovidItemsInfo`
        :param Maternity: 孕产报告
注意：此字段可能返回 null，表示取不到有效值。
        :type Maternity: :class:`tencentcloud.mrs.v20200910.models.Maternity`
        :param Eye: 眼科报告
注意：此字段可能返回 null，表示取不到有效值。
        :type Eye: :class:`tencentcloud.mrs.v20200910.models.EyeItemsInfo`
        :param BirthCert: 出生证明
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthCert: :class:`tencentcloud.mrs.v20200910.models.BirthCert`
        :param Timeline: 时间轴
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeline: :class:`tencentcloud.mrs.v20200910.models.TimelineInformation`
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
        self.OcrResult = None
        self.ReportTypeDesc = None
        self.PathologyV2 = None
        self.C14 = None
        self.Exame = None
        self.MedDocV2 = None
        self.IndicatorV3 = None
        self.Covid = None
        self.Maternity = None
        self.Eye = None
        self.BirthCert = None
        self.Timeline = None


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
        self.OcrResult = params.get("OcrResult")
        self.ReportTypeDesc = params.get("ReportTypeDesc")
        if params.get("PathologyV2") is not None:
            self.PathologyV2 = PathologyV2()
            self.PathologyV2._deserialize(params.get("PathologyV2"))
        if params.get("C14") is not None:
            self.C14 = Indicator()
            self.C14._deserialize(params.get("C14"))
        if params.get("Exame") is not None:
            self.Exame = Exame()
            self.Exame._deserialize(params.get("Exame"))
        if params.get("MedDocV2") is not None:
            self.MedDocV2 = DischargeInfoBlock()
            self.MedDocV2._deserialize(params.get("MedDocV2"))
        if params.get("IndicatorV3") is not None:
            self.IndicatorV3 = IndicatorV3()
            self.IndicatorV3._deserialize(params.get("IndicatorV3"))
        if params.get("Covid") is not None:
            self.Covid = CovidItemsInfo()
            self.Covid._deserialize(params.get("Covid"))
        if params.get("Maternity") is not None:
            self.Maternity = Maternity()
            self.Maternity._deserialize(params.get("Maternity"))
        if params.get("Eye") is not None:
            self.Eye = EyeItemsInfo()
            self.Eye._deserialize(params.get("Eye"))
        if params.get("BirthCert") is not None:
            self.BirthCert = BirthCert()
            self.BirthCert._deserialize(params.get("BirthCert"))
        if params.get("Timeline") is not None:
            self.Timeline = TimelineInformation()
            self.Timeline._deserialize(params.get("Timeline"))
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
        :param UserType: 后付费的用户类型，新客户传1，老客户可不传或传 0。2022 年 12 月 15 新增了计费项，在此时间之前已经通过商务指定优惠价格的大客户，请不传这个字段或传 0，如果传 1 会导致以前获得的折扣价格失效。在 2022 年 12 月 15 日之后，通过商务指定优惠价格的大客户请传 1。
        :type UserType: int
        """
        self.Text = None
        self.UserType = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.UserType = params.get("UserType")
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
        :param UserType: 后付费的用户类型，新客户传1，老客户可不传或传 0。2022 年 12 月 15 新增了计费项，在此时间之前已经通过商务指定优惠价格的大客户，请不传这个字段或传 0，如果传 1 会导致以前获得的折扣价格失效。在 2022 年 12 月 15 日之后，通过商务指定优惠价格的大客户请传 1。
        :type UserType: int
        :param ReportTypeVersion: 可选。用于指定不同报告使用的结构化引擎版本，不同版本返回的JSON 数据结果不兼容。若不指定版本号，就默认用旧的版本号。
（1）检验报告 11，默认使用 V2，最高支持 V3。
（2）病理报告 15，默认使用 V1，最高支持 V2。
（3）入院记录29、出院记录 28、病历记录 216、病程记录 217、门诊记录 210，默认使用 V1，最高支持 V2。
        :type ReportTypeVersion: list of ReportTypeVersion
        """
        self.Text = None
        self.Type = None
        self.IsUsedClassify = None
        self.UserType = None
        self.ReportTypeVersion = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Type = params.get("Type")
        self.IsUsedClassify = params.get("IsUsedClassify")
        self.UserType = params.get("UserType")
        if params.get("ReportTypeVersion") is not None:
            self.ReportTypeVersion = []
            for item in params.get("ReportTypeVersion"):
                obj = ReportTypeVersion()
                obj._deserialize(item)
                self.ReportTypeVersion.append(obj)
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
        


class Time(AbstractModel):
    """时间

    """

    def __init__(self):
        r"""
        :param Name: 具体时间类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 时间值
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
        


class TimelineEvent(AbstractModel):
    """时间轴事件

    """

    def __init__(self):
        r"""
        :param Type: 事件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Src: 原文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param SubType: 事件子类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SubType: str
        :param Time: 事件发生时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: str
        :param Value: 事件值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Rectangle: 位置坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Rectangle: :class:`tencentcloud.mrs.v20200910.models.Rectangle`
        :param Place: 事件发生地点
注意：此字段可能返回 null，表示取不到有效值。
        :type Place: str
        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self.Type = None
        self.Src = None
        self.SubType = None
        self.Time = None
        self.Value = None
        self.Rectangle = None
        self.Place = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Src = params.get("Src")
        self.SubType = params.get("SubType")
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        if params.get("Rectangle") is not None:
            self.Rectangle = Rectangle()
            self.Rectangle._deserialize(params.get("Rectangle"))
        self.Place = params.get("Place")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimelineInformation(AbstractModel):
    """时间轴

    """

    def __init__(self):
        r"""
        :param Timeline: 时间轴
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeline: list of TimelineEvent
        """
        self.Timeline = None


    def _deserialize(self, params):
        if params.get("Timeline") is not None:
            self.Timeline = []
            for item in params.get("Timeline"):
                obj = TimelineEvent()
                obj._deserialize(item)
                self.Timeline.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransfusionHistoryBlock(AbstractModel):
    """输血史

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Src: 原文
注意：此字段可能返回 null，表示取不到有效值。
        :type Src: str
        :param State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: bool
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Src = None
        self.State = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Src = params.get("Src")
        self.State = params.get("State")
        self.Value = params.get("Value")
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
        


class TreatmentRecordBlock(AbstractModel):
    """治疗记录

    """

    def __init__(self):
        r"""
        :param Immunohistochemistry: 免疫组化
注意：此字段可能返回 null，表示取不到有效值。
        :type Immunohistochemistry: :class:`tencentcloud.mrs.v20200910.models.ImmunohistochemistryBlock`
        :param ChiefComplaint: 主诉
注意：此字段可能返回 null，表示取不到有效值。
        :type ChiefComplaint: :class:`tencentcloud.mrs.v20200910.models.ChiefComplaintBlock`
        :param AdmissionCondition: 入院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionCondition: :class:`tencentcloud.mrs.v20200910.models.AdmissionConditionBlock`
        :param BodyExamination: 查体
注意：此字段可能返回 null，表示取不到有效值。
        :type BodyExamination: :class:`tencentcloud.mrs.v20200910.models.BodyExaminationBlock`
        :param AdmissionDiagnosis: 入院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionDiagnosis: :class:`tencentcloud.mrs.v20200910.models.AdmissionDiagnosisBlock`
        :param AdmissionTraditionalDiagnosis: 入院中医诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionTraditionalDiagnosis: :class:`tencentcloud.mrs.v20200910.models.AdmissionDiagnosisBlock`
        :param AdmissionModernDiagnosis: 入院西医诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionModernDiagnosis: :class:`tencentcloud.mrs.v20200910.models.AdmissionDiagnosisBlock`
        :param PathologicalDiagnosis: 病理诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type PathologicalDiagnosis: :class:`tencentcloud.mrs.v20200910.models.PathologicalDiagnosisBlock`
        :param DiseasePresent: 现病史
注意：此字段可能返回 null，表示取不到有效值。
        :type DiseasePresent: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param SymptomsAndSigns: 体征
注意：此字段可能返回 null，表示取不到有效值。
        :type SymptomsAndSigns: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param AuxiliaryExamination: 辅助检查
注意：此字段可能返回 null，表示取不到有效值。
        :type AuxiliaryExamination: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param SpecialistExamination: 特殊检查
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecialistExamination: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param MentalExamination: 精神检查
注意：此字段可能返回 null，表示取不到有效值。
        :type MentalExamination: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param CheckRecord: 检查记录
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckRecord: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param InspectResult: 检查结果
注意：此字段可能返回 null，表示取不到有效值。
        :type InspectResult: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param CheckAndTreatmentProcess: 治疗经过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckAndTreatmentProcess: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param SurgeryCondition: 手术经过
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryCondition: :class:`tencentcloud.mrs.v20200910.models.SurgeryConditionBlock`
        :param IncisionHealing: 切口愈合
注意：此字段可能返回 null，表示取不到有效值。
        :type IncisionHealing: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param DischargeDiagnosis: 出院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeDiagnosis: :class:`tencentcloud.mrs.v20200910.models.DischargeDiagnosisBlock`
        :param DischargeTraditionalDiagnosis: 出院中医诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeTraditionalDiagnosis: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param DischargeModernDiagnosis: 出院西医诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeModernDiagnosis: :class:`tencentcloud.mrs.v20200910.models.DischargeDiagnosisBlock`
        :param DischargeCondition: 出院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeCondition: :class:`tencentcloud.mrs.v20200910.models.DischargeConditionBlock`
        :param DischargeInstructions: 出院医嘱
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeInstructions: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param TreatmentSuggestion: 治疗建议
注意：此字段可能返回 null，表示取不到有效值。
        :type TreatmentSuggestion: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param FollowUpRequirements: 随访
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowUpRequirements: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param ConditionChanges: 治疗情况变化
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionChanges: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param PulmonaryArterySystolicPressure: 收缩压
注意：此字段可能返回 null，表示取不到有效值。
        :type PulmonaryArterySystolicPressure: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param BCLC: bclc分期
注意：此字段可能返回 null，表示取不到有效值。
        :type BCLC: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param PTNM: PTNM分期
注意：此字段可能返回 null，表示取不到有效值。
        :type PTNM: :class:`tencentcloud.mrs.v20200910.models.PTNMBlock`
        :param ECOG: ECOG评分
注意：此字段可能返回 null，表示取不到有效值。
        :type ECOG: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param NRS: NRS评分
注意：此字段可能返回 null，表示取不到有效值。
        :type NRS: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param KPS: kps评分
注意：此字段可能返回 null，表示取不到有效值。
        :type KPS: :class:`tencentcloud.mrs.v20200910.models.DiseasePresentBlock`
        :param Cancerstaging: 癌症分期
注意：此字段可能返回 null，表示取不到有效值。
        :type Cancerstaging: :class:`tencentcloud.mrs.v20200910.models.ClinicalStaging`
        :param DeathDate: 死亡时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DeathDate: :class:`tencentcloud.mrs.v20200910.models.DeathDateBlock`
        :param RelapseDate: 复发日期
注意：此字段可能返回 null，表示取不到有效值。
        :type RelapseDate: :class:`tencentcloud.mrs.v20200910.models.RelapseDateBlock`
        :param ObservationDays: 观察日期
注意：此字段可能返回 null，表示取不到有效值。
        :type ObservationDays: :class:`tencentcloud.mrs.v20200910.models.DeathDateBlock`
        :param IncisionHealingText: 切口愈合情况
注意：此字段可能返回 null，表示取不到有效值。
        :type IncisionHealingText: str
        :param AuxiliaryExaminationText: 辅助检查
注意：此字段可能返回 null，表示取不到有效值。
        :type AuxiliaryExaminationText: str
        :param SpecialExamText: 特殊检查
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecialExamText: str
        :param OutpatientDiagnosisText: 门诊诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type OutpatientDiagnosisText: str
        :param AdmissionConditionText: 入院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionConditionText: str
        :param CheckAndTreatmentProcessText: 诊疗经过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckAndTreatmentProcessText: str
        :param SymptomsAndSignsText: 体征
注意：此字段可能返回 null，表示取不到有效值。
        :type SymptomsAndSignsText: str
        :param DischargeInstructionsText: 出院医嘱
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeInstructionsText: str
        :param AdmissionDiagnosisText: 入院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type AdmissionDiagnosisText: str
        :param SurgeryConditionText: 手术情况
注意：此字段可能返回 null，表示取不到有效值。
        :type SurgeryConditionText: str
        :param PathologicalDiagnosisText: 病理诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type PathologicalDiagnosisText: str
        :param DischargeConditionText: 出院情况
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeConditionText: str
        :param CheckRecordText: 检查记录
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckRecordText: str
        :param ChiefComplaintText: 主诉
注意：此字段可能返回 null，表示取不到有效值。
        :type ChiefComplaintText: str
        :param DischargeDiagnosisText: 出院诊断
注意：此字段可能返回 null，表示取不到有效值。
        :type DischargeDiagnosisText: str
        """
        self.Immunohistochemistry = None
        self.ChiefComplaint = None
        self.AdmissionCondition = None
        self.BodyExamination = None
        self.AdmissionDiagnosis = None
        self.AdmissionTraditionalDiagnosis = None
        self.AdmissionModernDiagnosis = None
        self.PathologicalDiagnosis = None
        self.DiseasePresent = None
        self.SymptomsAndSigns = None
        self.AuxiliaryExamination = None
        self.SpecialistExamination = None
        self.MentalExamination = None
        self.CheckRecord = None
        self.InspectResult = None
        self.CheckAndTreatmentProcess = None
        self.SurgeryCondition = None
        self.IncisionHealing = None
        self.DischargeDiagnosis = None
        self.DischargeTraditionalDiagnosis = None
        self.DischargeModernDiagnosis = None
        self.DischargeCondition = None
        self.DischargeInstructions = None
        self.TreatmentSuggestion = None
        self.FollowUpRequirements = None
        self.ConditionChanges = None
        self.PulmonaryArterySystolicPressure = None
        self.BCLC = None
        self.PTNM = None
        self.ECOG = None
        self.NRS = None
        self.KPS = None
        self.Cancerstaging = None
        self.DeathDate = None
        self.RelapseDate = None
        self.ObservationDays = None
        self.IncisionHealingText = None
        self.AuxiliaryExaminationText = None
        self.SpecialExamText = None
        self.OutpatientDiagnosisText = None
        self.AdmissionConditionText = None
        self.CheckAndTreatmentProcessText = None
        self.SymptomsAndSignsText = None
        self.DischargeInstructionsText = None
        self.AdmissionDiagnosisText = None
        self.SurgeryConditionText = None
        self.PathologicalDiagnosisText = None
        self.DischargeConditionText = None
        self.CheckRecordText = None
        self.ChiefComplaintText = None
        self.DischargeDiagnosisText = None


    def _deserialize(self, params):
        if params.get("Immunohistochemistry") is not None:
            self.Immunohistochemistry = ImmunohistochemistryBlock()
            self.Immunohistochemistry._deserialize(params.get("Immunohistochemistry"))
        if params.get("ChiefComplaint") is not None:
            self.ChiefComplaint = ChiefComplaintBlock()
            self.ChiefComplaint._deserialize(params.get("ChiefComplaint"))
        if params.get("AdmissionCondition") is not None:
            self.AdmissionCondition = AdmissionConditionBlock()
            self.AdmissionCondition._deserialize(params.get("AdmissionCondition"))
        if params.get("BodyExamination") is not None:
            self.BodyExamination = BodyExaminationBlock()
            self.BodyExamination._deserialize(params.get("BodyExamination"))
        if params.get("AdmissionDiagnosis") is not None:
            self.AdmissionDiagnosis = AdmissionDiagnosisBlock()
            self.AdmissionDiagnosis._deserialize(params.get("AdmissionDiagnosis"))
        if params.get("AdmissionTraditionalDiagnosis") is not None:
            self.AdmissionTraditionalDiagnosis = AdmissionDiagnosisBlock()
            self.AdmissionTraditionalDiagnosis._deserialize(params.get("AdmissionTraditionalDiagnosis"))
        if params.get("AdmissionModernDiagnosis") is not None:
            self.AdmissionModernDiagnosis = AdmissionDiagnosisBlock()
            self.AdmissionModernDiagnosis._deserialize(params.get("AdmissionModernDiagnosis"))
        if params.get("PathologicalDiagnosis") is not None:
            self.PathologicalDiagnosis = PathologicalDiagnosisBlock()
            self.PathologicalDiagnosis._deserialize(params.get("PathologicalDiagnosis"))
        if params.get("DiseasePresent") is not None:
            self.DiseasePresent = DiseasePresentBlock()
            self.DiseasePresent._deserialize(params.get("DiseasePresent"))
        if params.get("SymptomsAndSigns") is not None:
            self.SymptomsAndSigns = DiseasePresentBlock()
            self.SymptomsAndSigns._deserialize(params.get("SymptomsAndSigns"))
        if params.get("AuxiliaryExamination") is not None:
            self.AuxiliaryExamination = DiseasePresentBlock()
            self.AuxiliaryExamination._deserialize(params.get("AuxiliaryExamination"))
        if params.get("SpecialistExamination") is not None:
            self.SpecialistExamination = DiseasePresentBlock()
            self.SpecialistExamination._deserialize(params.get("SpecialistExamination"))
        if params.get("MentalExamination") is not None:
            self.MentalExamination = DiseasePresentBlock()
            self.MentalExamination._deserialize(params.get("MentalExamination"))
        if params.get("CheckRecord") is not None:
            self.CheckRecord = DiseasePresentBlock()
            self.CheckRecord._deserialize(params.get("CheckRecord"))
        if params.get("InspectResult") is not None:
            self.InspectResult = DiseasePresentBlock()
            self.InspectResult._deserialize(params.get("InspectResult"))
        if params.get("CheckAndTreatmentProcess") is not None:
            self.CheckAndTreatmentProcess = DiseasePresentBlock()
            self.CheckAndTreatmentProcess._deserialize(params.get("CheckAndTreatmentProcess"))
        if params.get("SurgeryCondition") is not None:
            self.SurgeryCondition = SurgeryConditionBlock()
            self.SurgeryCondition._deserialize(params.get("SurgeryCondition"))
        if params.get("IncisionHealing") is not None:
            self.IncisionHealing = DiseasePresentBlock()
            self.IncisionHealing._deserialize(params.get("IncisionHealing"))
        if params.get("DischargeDiagnosis") is not None:
            self.DischargeDiagnosis = DischargeDiagnosisBlock()
            self.DischargeDiagnosis._deserialize(params.get("DischargeDiagnosis"))
        if params.get("DischargeTraditionalDiagnosis") is not None:
            self.DischargeTraditionalDiagnosis = DiseasePresentBlock()
            self.DischargeTraditionalDiagnosis._deserialize(params.get("DischargeTraditionalDiagnosis"))
        if params.get("DischargeModernDiagnosis") is not None:
            self.DischargeModernDiagnosis = DischargeDiagnosisBlock()
            self.DischargeModernDiagnosis._deserialize(params.get("DischargeModernDiagnosis"))
        if params.get("DischargeCondition") is not None:
            self.DischargeCondition = DischargeConditionBlock()
            self.DischargeCondition._deserialize(params.get("DischargeCondition"))
        if params.get("DischargeInstructions") is not None:
            self.DischargeInstructions = DiseasePresentBlock()
            self.DischargeInstructions._deserialize(params.get("DischargeInstructions"))
        if params.get("TreatmentSuggestion") is not None:
            self.TreatmentSuggestion = DiseasePresentBlock()
            self.TreatmentSuggestion._deserialize(params.get("TreatmentSuggestion"))
        if params.get("FollowUpRequirements") is not None:
            self.FollowUpRequirements = DiseasePresentBlock()
            self.FollowUpRequirements._deserialize(params.get("FollowUpRequirements"))
        if params.get("ConditionChanges") is not None:
            self.ConditionChanges = DiseasePresentBlock()
            self.ConditionChanges._deserialize(params.get("ConditionChanges"))
        if params.get("PulmonaryArterySystolicPressure") is not None:
            self.PulmonaryArterySystolicPressure = DiseasePresentBlock()
            self.PulmonaryArterySystolicPressure._deserialize(params.get("PulmonaryArterySystolicPressure"))
        if params.get("BCLC") is not None:
            self.BCLC = DiseasePresentBlock()
            self.BCLC._deserialize(params.get("BCLC"))
        if params.get("PTNM") is not None:
            self.PTNM = PTNMBlock()
            self.PTNM._deserialize(params.get("PTNM"))
        if params.get("ECOG") is not None:
            self.ECOG = DiseasePresentBlock()
            self.ECOG._deserialize(params.get("ECOG"))
        if params.get("NRS") is not None:
            self.NRS = DiseasePresentBlock()
            self.NRS._deserialize(params.get("NRS"))
        if params.get("KPS") is not None:
            self.KPS = DiseasePresentBlock()
            self.KPS._deserialize(params.get("KPS"))
        if params.get("Cancerstaging") is not None:
            self.Cancerstaging = ClinicalStaging()
            self.Cancerstaging._deserialize(params.get("Cancerstaging"))
        if params.get("DeathDate") is not None:
            self.DeathDate = DeathDateBlock()
            self.DeathDate._deserialize(params.get("DeathDate"))
        if params.get("RelapseDate") is not None:
            self.RelapseDate = RelapseDateBlock()
            self.RelapseDate._deserialize(params.get("RelapseDate"))
        if params.get("ObservationDays") is not None:
            self.ObservationDays = DeathDateBlock()
            self.ObservationDays._deserialize(params.get("ObservationDays"))
        self.IncisionHealingText = params.get("IncisionHealingText")
        self.AuxiliaryExaminationText = params.get("AuxiliaryExaminationText")
        self.SpecialExamText = params.get("SpecialExamText")
        self.OutpatientDiagnosisText = params.get("OutpatientDiagnosisText")
        self.AdmissionConditionText = params.get("AdmissionConditionText")
        self.CheckAndTreatmentProcessText = params.get("CheckAndTreatmentProcessText")
        self.SymptomsAndSignsText = params.get("SymptomsAndSignsText")
        self.DischargeInstructionsText = params.get("DischargeInstructionsText")
        self.AdmissionDiagnosisText = params.get("AdmissionDiagnosisText")
        self.SurgeryConditionText = params.get("SurgeryConditionText")
        self.PathologicalDiagnosisText = params.get("PathologicalDiagnosisText")
        self.DischargeConditionText = params.get("DischargeConditionText")
        self.CheckRecordText = params.get("CheckRecordText")
        self.ChiefComplaintText = params.get("ChiefComplaintText")
        self.DischargeDiagnosisText = params.get("DischargeDiagnosisText")
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
        :param Transparent: 透声度
注意：此字段可能返回 null，表示取不到有效值。
        :type Transparent: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param MriAdc: MRI ADC
注意：此字段可能返回 null，表示取不到有效值。
        :type MriAdc: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param MriDwi: MRI DWI
注意：此字段可能返回 null，表示取不到有效值。
        :type MriDwi: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param MriT1: MRI T1信号
注意：此字段可能返回 null，表示取不到有效值。
        :type MriT1: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param MriT2: MRI T2信号
注意：此字段可能返回 null，表示取不到有效值。
        :type MriT2: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param CtHu: CT HU值
注意：此字段可能返回 null，表示取不到有效值。
        :type CtHu: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Suvmax: SUmax值
注意：此字段可能返回 null，表示取不到有效值。
        :type Suvmax: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Metabolism: 代谢情况
注意：此字段可能返回 null，表示取不到有效值。
        :type Metabolism: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param RadioactiveUptake: 放射性摄取
注意：此字段可能返回 null，表示取不到有效值。
        :type RadioactiveUptake: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param SymDesc: 病变
注意：此字段可能返回 null，表示取不到有效值。
        :type SymDesc: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param ImageFeature: 影像特征
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageFeature: :class:`tencentcloud.mrs.v20200910.models.BlockInfo`
        :param Coords: 在报告图片中的坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Coords: list of Coord
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
        self.Transparent = None
        self.MriAdc = None
        self.MriDwi = None
        self.MriT1 = None
        self.MriT2 = None
        self.CtHu = None
        self.Suvmax = None
        self.Metabolism = None
        self.RadioactiveUptake = None
        self.SymDesc = None
        self.ImageFeature = None
        self.Coords = None


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
        if params.get("Transparent") is not None:
            self.Transparent = BlockInfo()
            self.Transparent._deserialize(params.get("Transparent"))
        if params.get("MriAdc") is not None:
            self.MriAdc = BlockInfo()
            self.MriAdc._deserialize(params.get("MriAdc"))
        if params.get("MriDwi") is not None:
            self.MriDwi = BlockInfo()
            self.MriDwi._deserialize(params.get("MriDwi"))
        if params.get("MriT1") is not None:
            self.MriT1 = BlockInfo()
            self.MriT1._deserialize(params.get("MriT1"))
        if params.get("MriT2") is not None:
            self.MriT2 = BlockInfo()
            self.MriT2._deserialize(params.get("MriT2"))
        if params.get("CtHu") is not None:
            self.CtHu = BlockInfo()
            self.CtHu._deserialize(params.get("CtHu"))
        if params.get("Suvmax") is not None:
            self.Suvmax = BlockInfo()
            self.Suvmax._deserialize(params.get("Suvmax"))
        if params.get("Metabolism") is not None:
            self.Metabolism = BlockInfo()
            self.Metabolism._deserialize(params.get("Metabolism"))
        if params.get("RadioactiveUptake") is not None:
            self.RadioactiveUptake = BlockInfo()
            self.RadioactiveUptake._deserialize(params.get("RadioactiveUptake"))
        if params.get("SymDesc") is not None:
            self.SymDesc = BlockInfo()
            self.SymDesc._deserialize(params.get("SymDesc"))
        if params.get("ImageFeature") is not None:
            self.ImageFeature = BlockInfo()
            self.ImageFeature._deserialize(params.get("ImageFeature"))
        if params.get("Coords") is not None:
            self.Coords = []
            for item in params.get("Coords"):
                obj = Coord()
                obj._deserialize(item)
                self.Coords.append(obj)
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
        :param Lot: 疫苗批号
注意：此字段可能返回 null，表示取不到有效值。
        :type Lot: str
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
        self.Lot = None


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
        self.Lot = params.get("Lot")
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
        


class ValueBlock(AbstractModel):
    """值块

    """

    def __init__(self):
        r"""
        :param Grade: 等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Grade: str
        :param Percent: 百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: list of float
        :param Positive: 阳性阴性
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
        