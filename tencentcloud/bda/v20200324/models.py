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


class Age(AbstractModel):
    """人体年龄信息。
    AttributesType 不含 Age 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。

    """

    def __init__(self):
        r"""
        :param _Type: 人体年龄信息，返回值为以下集合中的一个{小孩,青年,中年,老年}。
        :type Type: str
        :param _Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self._Type = None
        self._Probability = None

    @property
    def Type(self):
        """人体年龄信息，返回值为以下集合中的一个{小孩,青年,中年,老年}。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Probability(self):
        """Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :rtype: float
        """
        return self._Probability

    @Probability.setter
    def Probability(self, Probability):
        self._Probability = Probability


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttributesOptions(AbstractModel):
    """返回人体属性选项，此值不填则为不需要返回，可以选择的值为以下六个。
    Age、Bag、Gender、Orientation、UpperBodyCloth、LowerBodyCloth，详细的解释请看对象描述
    需注意本接口最多返回面积最大的 5 个人体属性信息，超过 5 个人体（第 6 个及以后的人体）的人体属性不具备参考意义。

    """

    def __init__(self):
        r"""
        :param _Age: 返回年龄信息
        :type Age: bool
        :param _Bag: 返回随身挎包信息
        :type Bag: bool
        :param _Gender: 返回性别信息
        :type Gender: bool
        :param _Orientation: 返回朝向信息
        :type Orientation: bool
        :param _UpperBodyCloth: 返回上装信息
        :type UpperBodyCloth: bool
        :param _LowerBodyCloth: 返回下装信息
        :type LowerBodyCloth: bool
        """
        self._Age = None
        self._Bag = None
        self._Gender = None
        self._Orientation = None
        self._UpperBodyCloth = None
        self._LowerBodyCloth = None

    @property
    def Age(self):
        """返回年龄信息
        :rtype: bool
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Bag(self):
        """返回随身挎包信息
        :rtype: bool
        """
        return self._Bag

    @Bag.setter
    def Bag(self, Bag):
        self._Bag = Bag

    @property
    def Gender(self):
        """返回性别信息
        :rtype: bool
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Orientation(self):
        """返回朝向信息
        :rtype: bool
        """
        return self._Orientation

    @Orientation.setter
    def Orientation(self, Orientation):
        self._Orientation = Orientation

    @property
    def UpperBodyCloth(self):
        """返回上装信息
        :rtype: bool
        """
        return self._UpperBodyCloth

    @UpperBodyCloth.setter
    def UpperBodyCloth(self, UpperBodyCloth):
        self._UpperBodyCloth = UpperBodyCloth

    @property
    def LowerBodyCloth(self):
        """返回下装信息
        :rtype: bool
        """
        return self._LowerBodyCloth

    @LowerBodyCloth.setter
    def LowerBodyCloth(self, LowerBodyCloth):
        self._LowerBodyCloth = LowerBodyCloth


    def _deserialize(self, params):
        self._Age = params.get("Age")
        self._Bag = params.get("Bag")
        self._Gender = params.get("Gender")
        self._Orientation = params.get("Orientation")
        self._UpperBodyCloth = params.get("UpperBodyCloth")
        self._LowerBodyCloth = params.get("LowerBodyCloth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Bag(AbstractModel):
    """人体是否挎包。
    AttributesType 不含 Bag 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。

    """

    def __init__(self):
        r"""
        :param _Type: 挎包信息，返回值为以下集合中的一个{双肩包, 斜挎包, 手拎包, 无包}。
        :type Type: str
        :param _Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self._Type = None
        self._Probability = None

    @property
    def Type(self):
        """挎包信息，返回值为以下集合中的一个{双肩包, 斜挎包, 手拎包, 无包}。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Probability(self):
        """Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :rtype: float
        """
        return self._Probability

    @Probability.setter
    def Probability(self, Probability):
        self._Probability = Probability


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BodyAttributeInfo(AbstractModel):
    """图中检测出的人体属性信息。

    """

    def __init__(self):
        r"""
        :param _Age: 人体年龄信息。 
AttributesType 不含 Age 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type Age: :class:`tencentcloud.bda.v20200324.models.Age`
        :param _Bag: 人体是否挎包。 
AttributesType 不含 Bag 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bag: :class:`tencentcloud.bda.v20200324.models.Bag`
        :param _Gender: 人体性别信息。 
AttributesType 不含 Gender 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type Gender: :class:`tencentcloud.bda.v20200324.models.Gender`
        :param _Orientation: 人体朝向信息。   
AttributesType 不含 UpperBodyCloth 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type Orientation: :class:`tencentcloud.bda.v20200324.models.Orientation`
        :param _UpperBodyCloth: 人体上衣属性信息。
AttributesType 不含 Orientation 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpperBodyCloth: :class:`tencentcloud.bda.v20200324.models.UpperBodyCloth`
        :param _LowerBodyCloth: 人体下衣属性信息。  
AttributesType 不含 LowerBodyCloth 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type LowerBodyCloth: :class:`tencentcloud.bda.v20200324.models.LowerBodyCloth`
        """
        self._Age = None
        self._Bag = None
        self._Gender = None
        self._Orientation = None
        self._UpperBodyCloth = None
        self._LowerBodyCloth = None

    @property
    def Age(self):
        """人体年龄信息。 
AttributesType 不含 Age 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.bda.v20200324.models.Age`
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Bag(self):
        """人体是否挎包。 
AttributesType 不含 Bag 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.bda.v20200324.models.Bag`
        """
        return self._Bag

    @Bag.setter
    def Bag(self, Bag):
        self._Bag = Bag

    @property
    def Gender(self):
        """人体性别信息。 
AttributesType 不含 Gender 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.bda.v20200324.models.Gender`
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Orientation(self):
        """人体朝向信息。   
AttributesType 不含 UpperBodyCloth 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.bda.v20200324.models.Orientation`
        """
        return self._Orientation

    @Orientation.setter
    def Orientation(self, Orientation):
        self._Orientation = Orientation

    @property
    def UpperBodyCloth(self):
        """人体上衣属性信息。
AttributesType 不含 Orientation 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.bda.v20200324.models.UpperBodyCloth`
        """
        return self._UpperBodyCloth

    @UpperBodyCloth.setter
    def UpperBodyCloth(self, UpperBodyCloth):
        self._UpperBodyCloth = UpperBodyCloth

    @property
    def LowerBodyCloth(self):
        """人体下衣属性信息。  
AttributesType 不含 LowerBodyCloth 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.bda.v20200324.models.LowerBodyCloth`
        """
        return self._LowerBodyCloth

    @LowerBodyCloth.setter
    def LowerBodyCloth(self, LowerBodyCloth):
        self._LowerBodyCloth = LowerBodyCloth


    def _deserialize(self, params):
        if params.get("Age") is not None:
            self._Age = Age()
            self._Age._deserialize(params.get("Age"))
        if params.get("Bag") is not None:
            self._Bag = Bag()
            self._Bag._deserialize(params.get("Bag"))
        if params.get("Gender") is not None:
            self._Gender = Gender()
            self._Gender._deserialize(params.get("Gender"))
        if params.get("Orientation") is not None:
            self._Orientation = Orientation()
            self._Orientation._deserialize(params.get("Orientation"))
        if params.get("UpperBodyCloth") is not None:
            self._UpperBodyCloth = UpperBodyCloth()
            self._UpperBodyCloth._deserialize(params.get("UpperBodyCloth"))
        if params.get("LowerBodyCloth") is not None:
            self._LowerBodyCloth = LowerBodyCloth()
            self._LowerBodyCloth._deserialize(params.get("LowerBodyCloth"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BodyDetectResult(AbstractModel):
    """图中检测出来的人体框。

    """

    def __init__(self):
        r"""
        :param _Confidence: 检测出的人体置信度。 
误识率百分之十对应的阈值是0.14；误识率百分之五对应的阈值是0.32；误识率百分之二对应的阈值是0.62；误识率百分之一对应的阈值是0.81。 
通常情况建议使用阈值0.32，可适用大多数情况。
        :type Confidence: float
        :param _BodyRect: 图中检测出来的人体框
        :type BodyRect: :class:`tencentcloud.bda.v20200324.models.BodyRect`
        :param _BodyAttributeInfo: 图中检测出的人体属性信息。
        :type BodyAttributeInfo: :class:`tencentcloud.bda.v20200324.models.BodyAttributeInfo`
        """
        self._Confidence = None
        self._BodyRect = None
        self._BodyAttributeInfo = None

    @property
    def Confidence(self):
        """检测出的人体置信度。 
误识率百分之十对应的阈值是0.14；误识率百分之五对应的阈值是0.32；误识率百分之二对应的阈值是0.62；误识率百分之一对应的阈值是0.81。 
通常情况建议使用阈值0.32，可适用大多数情况。
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def BodyRect(self):
        """图中检测出来的人体框
        :rtype: :class:`tencentcloud.bda.v20200324.models.BodyRect`
        """
        return self._BodyRect

    @BodyRect.setter
    def BodyRect(self, BodyRect):
        self._BodyRect = BodyRect

    @property
    def BodyAttributeInfo(self):
        """图中检测出的人体属性信息。
        :rtype: :class:`tencentcloud.bda.v20200324.models.BodyAttributeInfo`
        """
        return self._BodyAttributeInfo

    @BodyAttributeInfo.setter
    def BodyAttributeInfo(self, BodyAttributeInfo):
        self._BodyAttributeInfo = BodyAttributeInfo


    def _deserialize(self, params):
        self._Confidence = params.get("Confidence")
        if params.get("BodyRect") is not None:
            self._BodyRect = BodyRect()
            self._BodyRect._deserialize(params.get("BodyRect"))
        if params.get("BodyAttributeInfo") is not None:
            self._BodyAttributeInfo = BodyAttributeInfo()
            self._BodyAttributeInfo._deserialize(params.get("BodyAttributeInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BodyJointsResult(AbstractModel):
    """人体框和人体关键点信息。

    """

    def __init__(self):
        r"""
        :param _BoundBox: 图中检测出来的人体框。
        :type BoundBox: :class:`tencentcloud.bda.v20200324.models.BoundRect`
        :param _BodyJoints: 14个人体关键点的坐标，人体关键点详见KeyPointInfo。
        :type BodyJoints: list of KeyPointInfo
        :param _Confidence: 检测出的人体置信度，0-1之间，数值越高越准确。
        :type Confidence: float
        """
        self._BoundBox = None
        self._BodyJoints = None
        self._Confidence = None

    @property
    def BoundBox(self):
        """图中检测出来的人体框。
        :rtype: :class:`tencentcloud.bda.v20200324.models.BoundRect`
        """
        return self._BoundBox

    @BoundBox.setter
    def BoundBox(self, BoundBox):
        self._BoundBox = BoundBox

    @property
    def BodyJoints(self):
        """14个人体关键点的坐标，人体关键点详见KeyPointInfo。
        :rtype: list of KeyPointInfo
        """
        return self._BodyJoints

    @BodyJoints.setter
    def BodyJoints(self, BodyJoints):
        self._BodyJoints = BodyJoints

    @property
    def Confidence(self):
        """检测出的人体置信度，0-1之间，数值越高越准确。
        :rtype: float
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence


    def _deserialize(self, params):
        if params.get("BoundBox") is not None:
            self._BoundBox = BoundRect()
            self._BoundBox._deserialize(params.get("BoundBox"))
        if params.get("BodyJoints") is not None:
            self._BodyJoints = []
            for item in params.get("BodyJoints"):
                obj = KeyPointInfo()
                obj._deserialize(item)
                self._BodyJoints.append(obj)
        self._Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BodyRect(AbstractModel):
    """人体框

    """

    def __init__(self):
        r"""
        :param _X: 人体框左上角横坐标。
        :type X: int
        :param _Y: 人体框左上角纵坐标。
        :type Y: int
        :param _Width: 人体宽度。
        :type Width: int
        :param _Height: 人体高度。
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        """人体框左上角横坐标。
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        """人体框左上角纵坐标。
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        """人体宽度。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """人体高度。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BoundRect(AbstractModel):
    """人体框

    """

    def __init__(self):
        r"""
        :param _X: 人体框左上角横坐标。
        :type X: int
        :param _Y: 人体框左上角纵坐标。
        :type Y: int
        :param _Width: 人体宽度。
        :type Width: int
        :param _Height: 人体高度。
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        """人体框左上角横坐标。
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        """人体框左上角纵坐标。
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        """人体宽度。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """人体高度。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Candidate(AbstractModel):
    """识别出的最相似候选人。

    """

    def __init__(self):
        r"""
        :param _PersonId: 人员ID。
        :type PersonId: str
        :param _TraceId: 人体动作轨迹ID。
        :type TraceId: str
        :param _Score: 候选者的匹配得分。 
十万人体库下，误识率百分之五对应的分数为70分；误识率百分之二对应的分数为80分；误识率百分之一对应的分数为90分。
 
二十万人体库下，误识率百分之五对应的分数为80分；误识率百分之二对应的分数为90分；误识率百分之一对应的分数为95分。
 
通常情况建议使用分数80分（保召回）。若希望获得较高精度，建议使用分数90分（保准确）。
        :type Score: float
        """
        self._PersonId = None
        self._TraceId = None
        self._Score = None

    @property
    def PersonId(self):
        """人员ID。
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def TraceId(self):
        """人体动作轨迹ID。
        :rtype: str
        """
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def Score(self):
        """候选者的匹配得分。 
十万人体库下，误识率百分之五对应的分数为70分；误识率百分之二对应的分数为80分；误识率百分之一对应的分数为90分。
 
二十万人体库下，误识率百分之五对应的分数为80分；误识率百分之二对应的分数为90分；误识率百分之一对应的分数为95分。
 
通常情况建议使用分数80分（保召回）。若希望获得较高精度，建议使用分数90分（保准确）。
        :rtype: float
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._TraceId = params.get("TraceId")
        self._Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupRequest(AbstractModel):
    """CreateGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 人体库名称，[1,60]个字符，可修改，不可重复。
        :type GroupName: str
        :param _GroupId: 人体库 ID，不可修改，不可重复。支持英文、数字、-%@#&_，长度限制64B。
        :type GroupId: str
        :param _Tag: 人体库信息备注，[0，40]个字符。
        :type Tag: str
        :param _BodyModelVersion: 人体识别所用的算法模型版本。 
目前入参仅支持 “1.0”1个输入。 默认为"1.0"。  
不同算法模型版本对应的人体识别算法不同，新版本的整体效果会优于旧版本，后续我们将推出更新版本。
        :type BodyModelVersion: str
        """
        self._GroupName = None
        self._GroupId = None
        self._Tag = None
        self._BodyModelVersion = None

    @property
    def GroupName(self):
        """人体库名称，[1,60]个字符，可修改，不可重复。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupId(self):
        """人体库 ID，不可修改，不可重复。支持英文、数字、-%@#&_，长度限制64B。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Tag(self):
        """人体库信息备注，[0，40]个字符。
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def BodyModelVersion(self):
        """人体识别所用的算法模型版本。 
目前入参仅支持 “1.0”1个输入。 默认为"1.0"。  
不同算法模型版本对应的人体识别算法不同，新版本的整体效果会优于旧版本，后续我们将推出更新版本。
        :rtype: str
        """
        return self._BodyModelVersion

    @BodyModelVersion.setter
    def BodyModelVersion(self, BodyModelVersion):
        self._BodyModelVersion = BodyModelVersion


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._GroupId = params.get("GroupId")
        self._Tag = params.get("Tag")
        self._BodyModelVersion = params.get("BodyModelVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupResponse(AbstractModel):
    """CreateGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreatePersonRequest(AbstractModel):
    """CreatePerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 待加入的人员库ID。
        :type GroupId: str
        :param _PersonName: 人员名称。[1，60]个字符，可修改，可重复。
        :type PersonName: str
        :param _PersonId: 人员ID，单个腾讯云账号下不可修改，不可重复。 
支持英文、数字、-%@#&_，，长度限制64B。
        :type PersonId: str
        :param _Trace: 人体动作轨迹信息。
        :type Trace: :class:`tencentcloud.bda.v20200324.models.Trace`
        """
        self._GroupId = None
        self._PersonName = None
        self._PersonId = None
        self._Trace = None

    @property
    def GroupId(self):
        """待加入的人员库ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PersonName(self):
        """人员名称。[1，60]个字符，可修改，可重复。
        :rtype: str
        """
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def PersonId(self):
        """人员ID，单个腾讯云账号下不可修改，不可重复。 
支持英文、数字、-%@#&_，，长度限制64B。
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Trace(self):
        """人体动作轨迹信息。
        :rtype: :class:`tencentcloud.bda.v20200324.models.Trace`
        """
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._PersonName = params.get("PersonName")
        self._PersonId = params.get("PersonId")
        if params.get("Trace") is not None:
            self._Trace = Trace()
            self._Trace._deserialize(params.get("Trace"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePersonResponse(AbstractModel):
    """CreatePerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TraceId: 人员动作轨迹唯一标识。
        :type TraceId: str
        :param _BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param _InputRetCode: 输入的人体动作轨迹图片中的合法性校验结果。
只有为0时结果才有意义。
-1001: 输入图片不合法。-1002: 输入图片不能构成动作轨迹。
        :type InputRetCode: int
        :param _InputRetCodeDetails: 输入的人体动作轨迹图片中的合法性校验结果详情。 
-1101:图片无效，-1102:url不合法。-1103:图片过大。-1104:图片下载失败。-1105:图片解码失败。-1109:图片分辨率过高。-2023:动作轨迹中有非同人图片。-2024: 动作轨迹提取失败。-2025: 人体检测失败。
RetCode 的顺序和入参中Images 或 Urls 的顺序一致。
        :type InputRetCodeDetails: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TraceId = None
        self._BodyModelVersion = None
        self._InputRetCode = None
        self._InputRetCodeDetails = None
        self._RequestId = None

    @property
    def TraceId(self):
        """人员动作轨迹唯一标识。
        :rtype: str
        """
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def BodyModelVersion(self):
        """人体识别所用的算法模型版本。
        :rtype: str
        """
        return self._BodyModelVersion

    @BodyModelVersion.setter
    def BodyModelVersion(self, BodyModelVersion):
        self._BodyModelVersion = BodyModelVersion

    @property
    def InputRetCode(self):
        """输入的人体动作轨迹图片中的合法性校验结果。
只有为0时结果才有意义。
-1001: 输入图片不合法。-1002: 输入图片不能构成动作轨迹。
        :rtype: int
        """
        return self._InputRetCode

    @InputRetCode.setter
    def InputRetCode(self, InputRetCode):
        self._InputRetCode = InputRetCode

    @property
    def InputRetCodeDetails(self):
        """输入的人体动作轨迹图片中的合法性校验结果详情。 
-1101:图片无效，-1102:url不合法。-1103:图片过大。-1104:图片下载失败。-1105:图片解码失败。-1109:图片分辨率过高。-2023:动作轨迹中有非同人图片。-2024: 动作轨迹提取失败。-2025: 人体检测失败。
RetCode 的顺序和入参中Images 或 Urls 的顺序一致。
        :rtype: list of int
        """
        return self._InputRetCodeDetails

    @InputRetCodeDetails.setter
    def InputRetCodeDetails(self, InputRetCodeDetails):
        self._InputRetCodeDetails = InputRetCodeDetails

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TraceId = params.get("TraceId")
        self._BodyModelVersion = params.get("BodyModelVersion")
        self._InputRetCode = params.get("InputRetCode")
        self._InputRetCodeDetails = params.get("InputRetCodeDetails")
        self._RequestId = params.get("RequestId")


class CreateSegmentationTaskRequest(AbstractModel):
    """CreateSegmentationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoUrl: 需要分割的视频URL，可外网访问。
        :type VideoUrl: str
        :param _BackgroundImageUrl: 背景图片URL。 
可以将视频背景替换为输入的图片。 
如果不输入背景图片，则输出人像区域mask。
        :type BackgroundImageUrl: str
        :param _Config: 预留字段，后期用于展示更多识别信息。
        :type Config: str
        """
        self._VideoUrl = None
        self._BackgroundImageUrl = None
        self._Config = None

    @property
    def VideoUrl(self):
        """需要分割的视频URL，可外网访问。
        :rtype: str
        """
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def BackgroundImageUrl(self):
        """背景图片URL。 
可以将视频背景替换为输入的图片。 
如果不输入背景图片，则输出人像区域mask。
        :rtype: str
        """
        return self._BackgroundImageUrl

    @BackgroundImageUrl.setter
    def BackgroundImageUrl(self, BackgroundImageUrl):
        self._BackgroundImageUrl = BackgroundImageUrl

    @property
    def Config(self):
        """预留字段，后期用于展示更多识别信息。
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._VideoUrl = params.get("VideoUrl")
        self._BackgroundImageUrl = params.get("BackgroundImageUrl")
        self._Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSegmentationTaskResponse(AbstractModel):
    """CreateSegmentationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskID: 任务标识ID,可以用与追溯任务状态，查看任务结果
        :type TaskID: str
        :param _EstimatedProcessingTime: 预估处理时间，单位为秒
        :type EstimatedProcessingTime: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskID = None
        self._EstimatedProcessingTime = None
        self._RequestId = None

    @property
    def TaskID(self):
        """任务标识ID,可以用与追溯任务状态，查看任务结果
        :rtype: str
        """
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def EstimatedProcessingTime(self):
        """预估处理时间，单位为秒
        :rtype: float
        """
        return self._EstimatedProcessingTime

    @EstimatedProcessingTime.setter
    def EstimatedProcessingTime(self, EstimatedProcessingTime):
        self._EstimatedProcessingTime = EstimatedProcessingTime

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        self._EstimatedProcessingTime = params.get("EstimatedProcessingTime")
        self._RequestId = params.get("RequestId")


class CreateTraceRequest(AbstractModel):
    """CreateTrace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 人员ID。
        :type PersonId: str
        :param _Trace: 人体动作轨迹信息。
        :type Trace: :class:`tencentcloud.bda.v20200324.models.Trace`
        """
        self._PersonId = None
        self._Trace = None

    @property
    def PersonId(self):
        """人员ID。
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Trace(self):
        """人体动作轨迹信息。
        :rtype: :class:`tencentcloud.bda.v20200324.models.Trace`
        """
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        if params.get("Trace") is not None:
            self._Trace = Trace()
            self._Trace._deserialize(params.get("Trace"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTraceResponse(AbstractModel):
    """CreateTrace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TraceId: 人员动作轨迹唯一标识。
        :type TraceId: str
        :param _BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param _InputRetCode: 输入的人体动作轨迹图片中的合法性校验结果。
只有为0时结果才有意义。
-1001: 输入图片不合法。-1002: 输入图片不能构成轨迹。
        :type InputRetCode: int
        :param _InputRetCodeDetails: 输入的人体动作轨迹图片中的合法性校验结果详情。 
-1101:图片无效，-1102:url不合法。-1103:图片过大。-1104:图片下载失败。-1105:图片解码失败。-1109:图片分辨率过高。-2023:动作轨迹中有非同人图片。-2024: 动作轨迹提取失败。-2025: 人体检测失败。
        :type InputRetCodeDetails: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TraceId = None
        self._BodyModelVersion = None
        self._InputRetCode = None
        self._InputRetCodeDetails = None
        self._RequestId = None

    @property
    def TraceId(self):
        """人员动作轨迹唯一标识。
        :rtype: str
        """
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def BodyModelVersion(self):
        """人体识别所用的算法模型版本。
        :rtype: str
        """
        return self._BodyModelVersion

    @BodyModelVersion.setter
    def BodyModelVersion(self, BodyModelVersion):
        self._BodyModelVersion = BodyModelVersion

    @property
    def InputRetCode(self):
        """输入的人体动作轨迹图片中的合法性校验结果。
只有为0时结果才有意义。
-1001: 输入图片不合法。-1002: 输入图片不能构成轨迹。
        :rtype: int
        """
        return self._InputRetCode

    @InputRetCode.setter
    def InputRetCode(self, InputRetCode):
        self._InputRetCode = InputRetCode

    @property
    def InputRetCodeDetails(self):
        """输入的人体动作轨迹图片中的合法性校验结果详情。 
-1101:图片无效，-1102:url不合法。-1103:图片过大。-1104:图片下载失败。-1105:图片解码失败。-1109:图片分辨率过高。-2023:动作轨迹中有非同人图片。-2024: 动作轨迹提取失败。-2025: 人体检测失败。
        :rtype: list of int
        """
        return self._InputRetCodeDetails

    @InputRetCodeDetails.setter
    def InputRetCodeDetails(self, InputRetCodeDetails):
        self._InputRetCodeDetails = InputRetCodeDetails

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TraceId = params.get("TraceId")
        self._BodyModelVersion = params.get("BodyModelVersion")
        self._InputRetCode = params.get("InputRetCode")
        self._InputRetCodeDetails = params.get("InputRetCodeDetails")
        self._RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 人体库ID。
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        """人体库ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeletePersonRequest(AbstractModel):
    """DeletePerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 人员ID。
        :type PersonId: str
        """
        self._PersonId = None

    @property
    def PersonId(self):
        """人员ID。
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePersonResponse(AbstractModel):
    """DeletePerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeSegmentationTaskRequest(AbstractModel):
    """DescribeSegmentationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskID: 在提交分割任务成功时返回的任务标识ID。
        :type TaskID: str
        """
        self._TaskID = None

    @property
    def TaskID(self):
        """在提交分割任务成功时返回的任务标识ID。
        :rtype: str
        """
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
        


class DescribeSegmentationTaskResponse(AbstractModel):
    """DescribeSegmentationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskStatus: 当前任务状态：
QUEUING 排队中
PROCESSING 处理中
FINISHED 处理完成
        :type TaskStatus: str
        :param _ResultVideoUrl: 分割后视频URL, 存储于腾讯云COS
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultVideoUrl: str
        :param _ResultVideoMD5: 分割后视频MD5，用于校验
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultVideoMD5: str
        :param _VideoBasicInformation: 视频基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoBasicInformation: :class:`tencentcloud.bda.v20200324.models.VideoBasicInformation`
        :param _ErrorMsg: 分割任务错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskStatus = None
        self._ResultVideoUrl = None
        self._ResultVideoMD5 = None
        self._VideoBasicInformation = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def TaskStatus(self):
        """当前任务状态：
QUEUING 排队中
PROCESSING 处理中
FINISHED 处理完成
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def ResultVideoUrl(self):
        """分割后视频URL, 存储于腾讯云COS
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def ResultVideoMD5(self):
        """分割后视频MD5，用于校验
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultVideoMD5

    @ResultVideoMD5.setter
    def ResultVideoMD5(self, ResultVideoMD5):
        self._ResultVideoMD5 = ResultVideoMD5

    @property
    def VideoBasicInformation(self):
        """视频基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.bda.v20200324.models.VideoBasicInformation`
        """
        return self._VideoBasicInformation

    @VideoBasicInformation.setter
    def VideoBasicInformation(self, VideoBasicInformation):
        self._VideoBasicInformation = VideoBasicInformation

    @property
    def ErrorMsg(self):
        """分割任务错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskStatus = params.get("TaskStatus")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._ResultVideoMD5 = params.get("ResultVideoMD5")
        if params.get("VideoBasicInformation") is not None:
            self._VideoBasicInformation = VideoBasicInformation()
            self._VideoBasicInformation._deserialize(params.get("VideoBasicInformation"))
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DetectBodyJointsRequest(AbstractModel):
    """DetectBodyJoints请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。  
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。 
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。  
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _LocalBodySwitch: 人体局部关键点识别，开启后对人体局部图（例如部分身体部位）进行关键点识别，输出人体关键点坐标，默认不开启

注意：若开启人体局部图片关键点识别，则BoundBox、Confidence返回为空。
        :type LocalBodySwitch: bool
        """
        self._Image = None
        self._Url = None
        self._LocalBodySwitch = None

    @property
    def Image(self):
        """图片 base64 数据，base64 编码后大小不可超过5M。  
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Url(self):
        """图片的 Url 。对应图片 base64 编码后大小不可超过5M。 
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。  
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def LocalBodySwitch(self):
        """人体局部关键点识别，开启后对人体局部图（例如部分身体部位）进行关键点识别，输出人体关键点坐标，默认不开启

注意：若开启人体局部图片关键点识别，则BoundBox、Confidence返回为空。
        :rtype: bool
        """
        return self._LocalBodySwitch

    @LocalBodySwitch.setter
    def LocalBodySwitch(self, LocalBodySwitch):
        self._LocalBodySwitch = LocalBodySwitch


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._LocalBodySwitch = params.get("LocalBodySwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectBodyJointsResponse(AbstractModel):
    """DetectBodyJoints返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BodyJointsResults: 图中检测出的人体框和人体关键点， 包含14个人体关键点的坐标，建议根据人体框置信度筛选出合格的人体；
        :type BodyJointsResults: list of BodyJointsResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BodyJointsResults = None
        self._RequestId = None

    @property
    def BodyJointsResults(self):
        """图中检测出的人体框和人体关键点， 包含14个人体关键点的坐标，建议根据人体框置信度筛选出合格的人体；
        :rtype: list of BodyJointsResult
        """
        return self._BodyJointsResults

    @BodyJointsResults.setter
    def BodyJointsResults(self, BodyJointsResults):
        self._BodyJointsResults = BodyJointsResults

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BodyJointsResults") is not None:
            self._BodyJointsResults = []
            for item in params.get("BodyJointsResults"):
                obj = BodyJointsResult()
                obj._deserialize(item)
                self._BodyJointsResults.append(obj)
        self._RequestId = params.get("RequestId")


class DetectBodyRequest(AbstractModel):
    """DetectBody请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Image: 人体图片 Base64 数据。
图片 base64 编码后大小不可超过5M。
图片分辨率不得超过 1920 * 1080 。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _MaxBodyNum: 最多检测的人体数目，默认值为1（仅检测图片中面积最大的那个人体）； 最大值10 ，检测图片中面积最大的10个人体。
        :type MaxBodyNum: int
        :param _Url: 人体图片 Url 。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片 base64 编码后大小不可超过5M。 
图片分辨率不得超过 1920 * 1080 。
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _AttributesOptions: 是否返回年龄、性别、朝向等属性。 
可选项有 Age、Bag、Gender、UpperBodyCloth、LowerBodyCloth、Orientation。  
如果此参数为空则为不需要返回。 
需要将属性组成一个用逗号分隔的字符串，属性之间的顺序没有要求。 
关于各属性的详细描述，参见下文出参。 
最多返回面积最大的 5 个人体属性信息，超过 5 个人体（第 6 个及以后的人体）的 BodyAttributesInfo 不具备参考意义。
        :type AttributesOptions: :class:`tencentcloud.bda.v20200324.models.AttributesOptions`
        """
        self._Image = None
        self._MaxBodyNum = None
        self._Url = None
        self._AttributesOptions = None

    @property
    def Image(self):
        """人体图片 Base64 数据。
图片 base64 编码后大小不可超过5M。
图片分辨率不得超过 1920 * 1080 。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def MaxBodyNum(self):
        """最多检测的人体数目，默认值为1（仅检测图片中面积最大的那个人体）； 最大值10 ，检测图片中面积最大的10个人体。
        :rtype: int
        """
        return self._MaxBodyNum

    @MaxBodyNum.setter
    def MaxBodyNum(self, MaxBodyNum):
        self._MaxBodyNum = MaxBodyNum

    @property
    def Url(self):
        """人体图片 Url 。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片 base64 编码后大小不可超过5M。 
图片分辨率不得超过 1920 * 1080 。
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def AttributesOptions(self):
        """是否返回年龄、性别、朝向等属性。 
可选项有 Age、Bag、Gender、UpperBodyCloth、LowerBodyCloth、Orientation。  
如果此参数为空则为不需要返回。 
需要将属性组成一个用逗号分隔的字符串，属性之间的顺序没有要求。 
关于各属性的详细描述，参见下文出参。 
最多返回面积最大的 5 个人体属性信息，超过 5 个人体（第 6 个及以后的人体）的 BodyAttributesInfo 不具备参考意义。
        :rtype: :class:`tencentcloud.bda.v20200324.models.AttributesOptions`
        """
        return self._AttributesOptions

    @AttributesOptions.setter
    def AttributesOptions(self, AttributesOptions):
        self._AttributesOptions = AttributesOptions


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._MaxBodyNum = params.get("MaxBodyNum")
        self._Url = params.get("Url")
        if params.get("AttributesOptions") is not None:
            self._AttributesOptions = AttributesOptions()
            self._AttributesOptions._deserialize(params.get("AttributesOptions"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectBodyResponse(AbstractModel):
    """DetectBody返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BodyDetectResults: 图中检测出来的人体框。
        :type BodyDetectResults: list of BodyDetectResult
        :param _BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BodyDetectResults = None
        self._BodyModelVersion = None
        self._RequestId = None

    @property
    def BodyDetectResults(self):
        """图中检测出来的人体框。
        :rtype: list of BodyDetectResult
        """
        return self._BodyDetectResults

    @BodyDetectResults.setter
    def BodyDetectResults(self, BodyDetectResults):
        self._BodyDetectResults = BodyDetectResults

    @property
    def BodyModelVersion(self):
        """人体识别所用的算法模型版本。
        :rtype: str
        """
        return self._BodyModelVersion

    @BodyModelVersion.setter
    def BodyModelVersion(self, BodyModelVersion):
        self._BodyModelVersion = BodyModelVersion

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BodyDetectResults") is not None:
            self._BodyDetectResults = []
            for item in params.get("BodyDetectResults"):
                obj = BodyDetectResult()
                obj._deserialize(item)
                self._BodyDetectResults.append(obj)
        self._BodyModelVersion = params.get("BodyModelVersion")
        self._RequestId = params.get("RequestId")


class Gender(AbstractModel):
    """人体性别信息。
    AttributesType 不含 Gender 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。

    """

    def __init__(self):
        r"""
        :param _Type: 性别信息，返回值为以下集合中的一个 {男性, 女性}
        :type Type: str
        :param _Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self._Type = None
        self._Probability = None

    @property
    def Type(self):
        """性别信息，返回值为以下集合中的一个 {男性, 女性}
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Probability(self):
        """Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :rtype: float
        """
        return self._Probability

    @Probability.setter
    def Probability(self, Probability):
        self._Probability = Probability


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupListRequest(AbstractModel):
    """GetGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 起始序号，默认值为0。
        :type Offset: int
        :param _Limit: 返回数量，默认值为10，最大值为1000。
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        """起始序号，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认值为10，最大值为1000。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupListResponse(AbstractModel):
    """GetGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupInfos: 返回的人体库信息。
        :type GroupInfos: list of GroupInfo
        :param _GroupNum: 人体库总数量。
        :type GroupNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupInfos = None
        self._GroupNum = None
        self._RequestId = None

    @property
    def GroupInfos(self):
        """返回的人体库信息。
        :rtype: list of GroupInfo
        """
        return self._GroupInfos

    @GroupInfos.setter
    def GroupInfos(self, GroupInfos):
        self._GroupInfos = GroupInfos

    @property
    def GroupNum(self):
        """人体库总数量。
        :rtype: int
        """
        return self._GroupNum

    @GroupNum.setter
    def GroupNum(self, GroupNum):
        self._GroupNum = GroupNum

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GroupInfos") is not None:
            self._GroupInfos = []
            for item in params.get("GroupInfos"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._GroupInfos.append(obj)
        self._GroupNum = params.get("GroupNum")
        self._RequestId = params.get("RequestId")


class GetPersonListRequest(AbstractModel):
    """GetPersonList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 人体库ID。
        :type GroupId: str
        :param _Offset: 起始序号，默认值为0。
        :type Offset: int
        :param _Limit: 返回数量，默认值为10，最大值为1000。
        :type Limit: int
        """
        self._GroupId = None
        self._Offset = None
        self._Limit = None

    @property
    def GroupId(self):
        """人体库ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Offset(self):
        """起始序号，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认值为10，最大值为1000。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPersonListResponse(AbstractModel):
    """GetPersonList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonInfos: 返回的人员信息。
        :type PersonInfos: list of PersonInfo
        :param _PersonNum: 该人体库的人员数量。
        :type PersonNum: int
        :param _BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PersonInfos = None
        self._PersonNum = None
        self._BodyModelVersion = None
        self._RequestId = None

    @property
    def PersonInfos(self):
        """返回的人员信息。
        :rtype: list of PersonInfo
        """
        return self._PersonInfos

    @PersonInfos.setter
    def PersonInfos(self, PersonInfos):
        self._PersonInfos = PersonInfos

    @property
    def PersonNum(self):
        """该人体库的人员数量。
        :rtype: int
        """
        return self._PersonNum

    @PersonNum.setter
    def PersonNum(self, PersonNum):
        self._PersonNum = PersonNum

    @property
    def BodyModelVersion(self):
        """人体识别所用的算法模型版本。
        :rtype: str
        """
        return self._BodyModelVersion

    @BodyModelVersion.setter
    def BodyModelVersion(self, BodyModelVersion):
        self._BodyModelVersion = BodyModelVersion

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PersonInfos") is not None:
            self._PersonInfos = []
            for item in params.get("PersonInfos"):
                obj = PersonInfo()
                obj._deserialize(item)
                self._PersonInfos.append(obj)
        self._PersonNum = params.get("PersonNum")
        self._BodyModelVersion = params.get("BodyModelVersion")
        self._RequestId = params.get("RequestId")


class GetSummaryInfoRequest(AbstractModel):
    """GetSummaryInfo请求参数结构体

    """


class GetSummaryInfoResponse(AbstractModel):
    """GetSummaryInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupCount: 人体库总数量。
        :type GroupCount: int
        :param _PersonCount: 人员总数量
        :type PersonCount: int
        :param _TraceCount: 人员轨迹总数量
        :type TraceCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupCount = None
        self._PersonCount = None
        self._TraceCount = None
        self._RequestId = None

    @property
    def GroupCount(self):
        """人体库总数量。
        :rtype: int
        """
        return self._GroupCount

    @GroupCount.setter
    def GroupCount(self, GroupCount):
        self._GroupCount = GroupCount

    @property
    def PersonCount(self):
        """人员总数量
        :rtype: int
        """
        return self._PersonCount

    @PersonCount.setter
    def PersonCount(self, PersonCount):
        self._PersonCount = PersonCount

    @property
    def TraceCount(self):
        """人员轨迹总数量
        :rtype: int
        """
        return self._TraceCount

    @TraceCount.setter
    def TraceCount(self, TraceCount):
        self._TraceCount = TraceCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupCount = params.get("GroupCount")
        self._PersonCount = params.get("PersonCount")
        self._TraceCount = params.get("TraceCount")
        self._RequestId = params.get("RequestId")


class GroupInfo(AbstractModel):
    """返回的人员库信息。

    """

    def __init__(self):
        r"""
        :param _GroupName: 人体库名称。
        :type GroupName: str
        :param _GroupId: 人体库ID。
        :type GroupId: str
        :param _Tag: 人体库信息备注。
        :type Tag: str
        :param _BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param _CreationTimestamp: Group的创建时间和日期 CreationTimestamp。CreationTimestamp 的值是自 Unix 纪元时间到Group创建时间的毫秒数。  
Unix 纪元时间是 1970 年 1 月 1 日星期四，协调世界时 (UTC) 。
        :type CreationTimestamp: int
        """
        self._GroupName = None
        self._GroupId = None
        self._Tag = None
        self._BodyModelVersion = None
        self._CreationTimestamp = None

    @property
    def GroupName(self):
        """人体库名称。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupId(self):
        """人体库ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Tag(self):
        """人体库信息备注。
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def BodyModelVersion(self):
        """人体识别所用的算法模型版本。
        :rtype: str
        """
        return self._BodyModelVersion

    @BodyModelVersion.setter
    def BodyModelVersion(self, BodyModelVersion):
        self._BodyModelVersion = BodyModelVersion

    @property
    def CreationTimestamp(self):
        """Group的创建时间和日期 CreationTimestamp。CreationTimestamp 的值是自 Unix 纪元时间到Group创建时间的毫秒数。  
Unix 纪元时间是 1970 年 1 月 1 日星期四，协调世界时 (UTC) 。
        :rtype: int
        """
        return self._CreationTimestamp

    @CreationTimestamp.setter
    def CreationTimestamp(self, CreationTimestamp):
        self._CreationTimestamp = CreationTimestamp


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._GroupId = params.get("GroupId")
        self._Tag = params.get("Tag")
        self._BodyModelVersion = params.get("BodyModelVersion")
        self._CreationTimestamp = params.get("CreationTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageRect(AbstractModel):
    """图像坐标信息。

    """

    def __init__(self):
        r"""
        :param _X: 左上角横坐标。
        :type X: int
        :param _Y: 左上角纵坐标。
        :type Y: int
        :param _Width: 人体宽度。
        :type Width: int
        :param _Height: 人体高度。
        :type Height: int
        :param _Label: 分割选项名称。
        :type Label: str
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None
        self._Label = None

    @property
    def X(self):
        """左上角横坐标。
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        """左上角纵坐标。
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        """人体宽度。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """人体高度。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Label(self):
        """分割选项名称。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyPointInfo(AbstractModel):
    """人体关键点信息

    """

    def __init__(self):
        r"""
        :param _KeyPointType: 代表不同位置的人体关键点信息，返回值为以下集合中的一个 [头部,颈部,右肩,右肘,右腕,左肩,左肘,左腕,右髋,右膝,右踝,左髋,左膝,左踝]
        :type KeyPointType: str
        :param _X: 人体关键点横坐标
        :type X: float
        :param _Y: 人体关键点纵坐标
        :type Y: float
        :param _BodyScore: 关键点坐标置信度，分数取值在0-1之间，阈值建议为0.25，小于0.25认为在图中无人体关键点。
        :type BodyScore: float
        """
        self._KeyPointType = None
        self._X = None
        self._Y = None
        self._BodyScore = None

    @property
    def KeyPointType(self):
        """代表不同位置的人体关键点信息，返回值为以下集合中的一个 [头部,颈部,右肩,右肘,右腕,左肩,左肘,左腕,右髋,右膝,右踝,左髋,左膝,左踝]
        :rtype: str
        """
        return self._KeyPointType

    @KeyPointType.setter
    def KeyPointType(self, KeyPointType):
        self._KeyPointType = KeyPointType

    @property
    def X(self):
        """人体关键点横坐标
        :rtype: float
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        """人体关键点纵坐标
        :rtype: float
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def BodyScore(self):
        """关键点坐标置信度，分数取值在0-1之间，阈值建议为0.25，小于0.25认为在图中无人体关键点。
        :rtype: float
        """
        return self._BodyScore

    @BodyScore.setter
    def BodyScore(self, BodyScore):
        self._BodyScore = BodyScore


    def _deserialize(self, params):
        self._KeyPointType = params.get("KeyPointType")
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._BodyScore = params.get("BodyScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LowerBodyCloth(AbstractModel):
    """下衣属性信息

    """

    def __init__(self):
        r"""
        :param _Color: 下衣颜色信息。
        :type Color: :class:`tencentcloud.bda.v20200324.models.LowerBodyClothColor`
        :param _Length: 下衣长度信息 。
        :type Length: :class:`tencentcloud.bda.v20200324.models.LowerBodyClothLength`
        :param _Type: 下衣类型信息。
        :type Type: :class:`tencentcloud.bda.v20200324.models.LowerBodyClothType`
        """
        self._Color = None
        self._Length = None
        self._Type = None

    @property
    def Color(self):
        """下衣颜色信息。
        :rtype: :class:`tencentcloud.bda.v20200324.models.LowerBodyClothColor`
        """
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color

    @property
    def Length(self):
        """下衣长度信息 。
        :rtype: :class:`tencentcloud.bda.v20200324.models.LowerBodyClothLength`
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Type(self):
        """下衣类型信息。
        :rtype: :class:`tencentcloud.bda.v20200324.models.LowerBodyClothType`
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        if params.get("Color") is not None:
            self._Color = LowerBodyClothColor()
            self._Color._deserialize(params.get("Color"))
        if params.get("Length") is not None:
            self._Length = LowerBodyClothLength()
            self._Length._deserialize(params.get("Length"))
        if params.get("Type") is not None:
            self._Type = LowerBodyClothType()
            self._Type._deserialize(params.get("Type"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LowerBodyClothColor(AbstractModel):
    """下衣颜色信息

    """

    def __init__(self):
        r"""
        :param _Type: 下衣颜色信息，返回值为以下集合中的一个{ 黑色系, 灰白色系, 彩色} 。
        :type Type: str
        :param _Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self._Type = None
        self._Probability = None

    @property
    def Type(self):
        """下衣颜色信息，返回值为以下集合中的一个{ 黑色系, 灰白色系, 彩色} 。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Probability(self):
        """Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :rtype: float
        """
        return self._Probability

    @Probability.setter
    def Probability(self, Probability):
        self._Probability = Probability


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LowerBodyClothLength(AbstractModel):
    """下衣长度信息

    """

    def __init__(self):
        r"""
        :param _Type: 下衣长度信息，返回值为以下集合中的一个，{长, 短} 。
        :type Type: str
        :param _Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self._Type = None
        self._Probability = None

    @property
    def Type(self):
        """下衣长度信息，返回值为以下集合中的一个，{长, 短} 。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Probability(self):
        """Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :rtype: float
        """
        return self._Probability

    @Probability.setter
    def Probability(self, Probability):
        self._Probability = Probability


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LowerBodyClothType(AbstractModel):
    """下衣类型信息

    """

    def __init__(self):
        r"""
        :param _Type: 下衣类型，返回值为以下集合中的一个 {裤子,裙子} 。
        :type Type: str
        :param _Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self._Type = None
        self._Probability = None

    @property
    def Type(self):
        """下衣类型，返回值为以下集合中的一个 {裤子,裙子} 。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Probability(self):
        """Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :rtype: float
        """
        return self._Probability

    @Probability.setter
    def Probability(self, Probability):
        self._Probability = Probability


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupRequest(AbstractModel):
    """ModifyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 人体库ID。
        :type GroupId: str
        :param _GroupName: 人体库名称。
        :type GroupName: str
        :param _Tag: 人体库信息备注。
        :type Tag: str
        """
        self._GroupId = None
        self._GroupName = None
        self._Tag = None

    @property
    def GroupId(self):
        """人体库ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """人体库名称。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Tag(self):
        """人体库信息备注。
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupResponse(AbstractModel):
    """ModifyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPersonInfoRequest(AbstractModel):
    """ModifyPersonInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 人员ID。
        :type PersonId: str
        :param _PersonName: 人员名称。
        :type PersonName: str
        """
        self._PersonId = None
        self._PersonName = None

    @property
    def PersonId(self):
        """人员ID。
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def PersonName(self):
        """人员名称。
        :rtype: str
        """
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._PersonName = params.get("PersonName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonInfoResponse(AbstractModel):
    """ModifyPersonInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Orientation(AbstractModel):
    """人体朝向信息。
    AttributesType 不含 Orientation 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。

    """

    def __init__(self):
        r"""
        :param _Type: 人体朝向信息，返回值为以下集合中的一个 {正向, 背向, 左, 右}。
        :type Type: str
        :param _Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self._Type = None
        self._Probability = None

    @property
    def Type(self):
        """人体朝向信息，返回值为以下集合中的一个 {正向, 背向, 左, 右}。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Probability(self):
        """Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :rtype: float
        """
        return self._Probability

    @Probability.setter
    def Probability(self, Probability):
        self._Probability = Probability


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonInfo(AbstractModel):
    """人员信息。

    """

    def __init__(self):
        r"""
        :param _PersonName: 人员名称。
        :type PersonName: str
        :param _PersonId: 人员ID。
        :type PersonId: str
        :param _TraceInfos: 包含的人体动作轨迹图片信息列表。
        :type TraceInfos: list of TraceInfo
        """
        self._PersonName = None
        self._PersonId = None
        self._TraceInfos = None

    @property
    def PersonName(self):
        """人员名称。
        :rtype: str
        """
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def PersonId(self):
        """人员ID。
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def TraceInfos(self):
        """包含的人体动作轨迹图片信息列表。
        :rtype: list of TraceInfo
        """
        return self._TraceInfos

    @TraceInfos.setter
    def TraceInfos(self, TraceInfos):
        self._TraceInfos = TraceInfos


    def _deserialize(self, params):
        self._PersonName = params.get("PersonName")
        self._PersonId = params.get("PersonId")
        if params.get("TraceInfos") is not None:
            self._TraceInfos = []
            for item in params.get("TraceInfos"):
                obj = TraceInfo()
                obj._deserialize(item)
                self._TraceInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchTraceRequest(AbstractModel):
    """SearchTrace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 希望搜索的人体库ID。
        :type GroupId: str
        :param _Trace: 人体动作轨迹信息。
        :type Trace: :class:`tencentcloud.bda.v20200324.models.Trace`
        :param _MaxPersonNum: 单张被识别的人体动作轨迹返回的最相似人员数量。
默认值为5，最大值为100。
 例，设MaxPersonNum为8，则返回Top8相似的人员信息。 值越大，需要处理的时间越长。建议不要超过10。
        :type MaxPersonNum: int
        :param _TraceMatchThreshold: 出参Score中，只有超过TraceMatchThreshold值的结果才会返回。
默认为0。范围[0, 100.0]。
        :type TraceMatchThreshold: float
        """
        self._GroupId = None
        self._Trace = None
        self._MaxPersonNum = None
        self._TraceMatchThreshold = None

    @property
    def GroupId(self):
        """希望搜索的人体库ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Trace(self):
        """人体动作轨迹信息。
        :rtype: :class:`tencentcloud.bda.v20200324.models.Trace`
        """
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace

    @property
    def MaxPersonNum(self):
        """单张被识别的人体动作轨迹返回的最相似人员数量。
默认值为5，最大值为100。
 例，设MaxPersonNum为8，则返回Top8相似的人员信息。 值越大，需要处理的时间越长。建议不要超过10。
        :rtype: int
        """
        return self._MaxPersonNum

    @MaxPersonNum.setter
    def MaxPersonNum(self, MaxPersonNum):
        self._MaxPersonNum = MaxPersonNum

    @property
    def TraceMatchThreshold(self):
        """出参Score中，只有超过TraceMatchThreshold值的结果才会返回。
默认为0。范围[0, 100.0]。
        :rtype: float
        """
        return self._TraceMatchThreshold

    @TraceMatchThreshold.setter
    def TraceMatchThreshold(self, TraceMatchThreshold):
        self._TraceMatchThreshold = TraceMatchThreshold


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("Trace") is not None:
            self._Trace = Trace()
            self._Trace._deserialize(params.get("Trace"))
        self._MaxPersonNum = params.get("MaxPersonNum")
        self._TraceMatchThreshold = params.get("TraceMatchThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchTraceResponse(AbstractModel):
    """SearchTrace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Candidates: 识别出的最相似候选人。
        :type Candidates: list of Candidate
        :param _InputRetCode: 输入的人体动作轨迹图片中的合法性校验结果。
只有为0时结果才有意义。
-1001: 输入图片不合法。-1002: 输入图片不能构成动作轨迹。
        :type InputRetCode: int
        :param _InputRetCodeDetails: 输入的人体动作轨迹图片中的合法性校验结果详情。 
-1101:图片无效，-1102:url不合法。-1103:图片过大。-1104:图片下载失败。-1105:图片解码失败。-1109:图片分辨率过高。-2023:动作轨迹中有非同人图片。-2024: 动作轨迹提取失败。-2025: 人体检测失败。
        :type InputRetCodeDetails: list of int
        :param _BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Candidates = None
        self._InputRetCode = None
        self._InputRetCodeDetails = None
        self._BodyModelVersion = None
        self._RequestId = None

    @property
    def Candidates(self):
        """识别出的最相似候选人。
        :rtype: list of Candidate
        """
        return self._Candidates

    @Candidates.setter
    def Candidates(self, Candidates):
        self._Candidates = Candidates

    @property
    def InputRetCode(self):
        """输入的人体动作轨迹图片中的合法性校验结果。
只有为0时结果才有意义。
-1001: 输入图片不合法。-1002: 输入图片不能构成动作轨迹。
        :rtype: int
        """
        return self._InputRetCode

    @InputRetCode.setter
    def InputRetCode(self, InputRetCode):
        self._InputRetCode = InputRetCode

    @property
    def InputRetCodeDetails(self):
        """输入的人体动作轨迹图片中的合法性校验结果详情。 
-1101:图片无效，-1102:url不合法。-1103:图片过大。-1104:图片下载失败。-1105:图片解码失败。-1109:图片分辨率过高。-2023:动作轨迹中有非同人图片。-2024: 动作轨迹提取失败。-2025: 人体检测失败。
        :rtype: list of int
        """
        return self._InputRetCodeDetails

    @InputRetCodeDetails.setter
    def InputRetCodeDetails(self, InputRetCodeDetails):
        self._InputRetCodeDetails = InputRetCodeDetails

    @property
    def BodyModelVersion(self):
        """人体识别所用的算法模型版本。
        :rtype: str
        """
        return self._BodyModelVersion

    @BodyModelVersion.setter
    def BodyModelVersion(self, BodyModelVersion):
        self._BodyModelVersion = BodyModelVersion

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Candidates") is not None:
            self._Candidates = []
            for item in params.get("Candidates"):
                obj = Candidate()
                obj._deserialize(item)
                self._Candidates.append(obj)
        self._InputRetCode = params.get("InputRetCode")
        self._InputRetCodeDetails = params.get("InputRetCodeDetails")
        self._BodyModelVersion = params.get("BodyModelVersion")
        self._RequestId = params.get("RequestId")


class SegmentCustomizedPortraitPicRequest(AbstractModel):
    """SegmentCustomizedPortraitPic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SegmentationOptions: 此参数为分割选项，请根据需要选择自己所想从图片中分割的部分。注意所有选项均为非必选，如未选择则值默认为false, 但是必须要保证多于一个选项的描述为true。
        :type SegmentationOptions: :class:`tencentcloud.bda.v20200324.models.SegmentationOptions`
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。
图片分辨率须小于2000*2000。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url 。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片分辨率须小于2000*2000 ，图片 base64 编码后大小不可超过5M。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        """
        self._SegmentationOptions = None
        self._Image = None
        self._Url = None

    @property
    def SegmentationOptions(self):
        """此参数为分割选项，请根据需要选择自己所想从图片中分割的部分。注意所有选项均为非必选，如未选择则值默认为false, 但是必须要保证多于一个选项的描述为true。
        :rtype: :class:`tencentcloud.bda.v20200324.models.SegmentationOptions`
        """
        return self._SegmentationOptions

    @SegmentationOptions.setter
    def SegmentationOptions(self, SegmentationOptions):
        self._SegmentationOptions = SegmentationOptions

    @property
    def Image(self):
        """图片 base64 数据，base64 编码后大小不可超过5M。
图片分辨率须小于2000*2000。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Url(self):
        """图片的 Url 。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片分辨率须小于2000*2000 ，图片 base64 编码后大小不可超过5M。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        if params.get("SegmentationOptions") is not None:
            self._SegmentationOptions = SegmentationOptions()
            self._SegmentationOptions._deserialize(params.get("SegmentationOptions"))
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SegmentCustomizedPortraitPicResponse(AbstractModel):
    """SegmentCustomizedPortraitPic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PortraitImage: 根据指定标签分割输出的透明背景人像图片的 base64 数据。
        :type PortraitImage: str
        :param _MaskImage: 指定标签处理后的Mask。一个通过 Base64 编码的文件，解码后文件由 Float 型浮点数组成。这些浮点数代表原图从左上角开始的每一行的每一个像素点，每一个浮点数的值是原图相应像素点位于人体轮廓内的置信度（0-1）转化的灰度值（0-255）
        :type MaskImage: str
        :param _ImageRects: 坐标信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageRects: list of ImageRect
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PortraitImage = None
        self._MaskImage = None
        self._ImageRects = None
        self._RequestId = None

    @property
    def PortraitImage(self):
        """根据指定标签分割输出的透明背景人像图片的 base64 数据。
        :rtype: str
        """
        return self._PortraitImage

    @PortraitImage.setter
    def PortraitImage(self, PortraitImage):
        self._PortraitImage = PortraitImage

    @property
    def MaskImage(self):
        """指定标签处理后的Mask。一个通过 Base64 编码的文件，解码后文件由 Float 型浮点数组成。这些浮点数代表原图从左上角开始的每一行的每一个像素点，每一个浮点数的值是原图相应像素点位于人体轮廓内的置信度（0-1）转化的灰度值（0-255）
        :rtype: str
        """
        return self._MaskImage

    @MaskImage.setter
    def MaskImage(self, MaskImage):
        self._MaskImage = MaskImage

    @property
    def ImageRects(self):
        """坐标信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ImageRect
        """
        return self._ImageRects

    @ImageRects.setter
    def ImageRects(self, ImageRects):
        self._ImageRects = ImageRects

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PortraitImage = params.get("PortraitImage")
        self._MaskImage = params.get("MaskImage")
        if params.get("ImageRects") is not None:
            self._ImageRects = []
            for item in params.get("ImageRects"):
                obj = ImageRect()
                obj._deserialize(item)
                self._ImageRects.append(obj)
        self._RequestId = params.get("RequestId")


class SegmentPortraitPicRequest(AbstractModel):
    """SegmentPortraitPic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。
图片分辨率须小于2000*2000。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url 。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片分辨率须小于2000*2000 ，图片 base64 编码后大小不可超过5M。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _RspImgType: 返回图像方式（base64 或 Url ) ，二选一。url有效期为30分钟。
        :type RspImgType: str
        :param _Scene: 适用场景类型。

取值：GEN/GS。GEN为通用场景模式；GS为绿幕场景模式，针对绿幕场景下的人像分割效果更好。
两种模式选择一种传入，默认为GEN。
        :type Scene: str
        """
        self._Image = None
        self._Url = None
        self._RspImgType = None
        self._Scene = None

    @property
    def Image(self):
        """图片 base64 数据，base64 编码后大小不可超过5M。
图片分辨率须小于2000*2000。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Url(self):
        """图片的 Url 。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片分辨率须小于2000*2000 ，图片 base64 编码后大小不可超过5M。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RspImgType(self):
        """返回图像方式（base64 或 Url ) ，二选一。url有效期为30分钟。
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType

    @property
    def Scene(self):
        """适用场景类型。

取值：GEN/GS。GEN为通用场景模式；GS为绿幕场景模式，针对绿幕场景下的人像分割效果更好。
两种模式选择一种传入，默认为GEN。
        :rtype: str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._RspImgType = params.get("RspImgType")
        self._Scene = params.get("Scene")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SegmentPortraitPicResponse(AbstractModel):
    """SegmentPortraitPic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: 处理后的图片 base64 数据，透明背景图。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultImage: str
        :param _ResultMask: 一个通过 base64 编码的文件，解码后文件由 Float 型浮点数组成。这些浮点数代表原图从左上角开始的每一行的每一个像素点，每一个浮点数的值是原图相应像素点位于人体轮廓内的置信度（0-1）转化的灰度值（0-255）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultMask: str
        :param _HasForeground: 图片是否存在前景。
注意：此字段可能返回 null，表示取不到有效值。
        :type HasForeground: bool
        :param _ResultImageUrl: 支持将处理过的图片 base64 数据，透明背景图以Url的形式返回值，Url有效期为30分钟。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultImageUrl: str
        :param _ResultMaskUrl: 一个通过 base64 编码的文件，解码后文件由 Float 型浮点数组成。支持以Url形式的返回值；Url有效期为30分钟。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultMaskUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._ResultMask = None
        self._HasForeground = None
        self._ResultImageUrl = None
        self._ResultMaskUrl = None
        self._RequestId = None

    @property
    def ResultImage(self):
        """处理后的图片 base64 数据，透明背景图。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def ResultMask(self):
        """一个通过 base64 编码的文件，解码后文件由 Float 型浮点数组成。这些浮点数代表原图从左上角开始的每一行的每一个像素点，每一个浮点数的值是原图相应像素点位于人体轮廓内的置信度（0-1）转化的灰度值（0-255）。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultMask

    @ResultMask.setter
    def ResultMask(self, ResultMask):
        self._ResultMask = ResultMask

    @property
    def HasForeground(self):
        """图片是否存在前景。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._HasForeground

    @HasForeground.setter
    def HasForeground(self, HasForeground):
        self._HasForeground = HasForeground

    @property
    def ResultImageUrl(self):
        """支持将处理过的图片 base64 数据，透明背景图以Url的形式返回值，Url有效期为30分钟。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultImageUrl

    @ResultImageUrl.setter
    def ResultImageUrl(self, ResultImageUrl):
        self._ResultImageUrl = ResultImageUrl

    @property
    def ResultMaskUrl(self):
        """一个通过 base64 编码的文件，解码后文件由 Float 型浮点数组成。支持以Url形式的返回值；Url有效期为30分钟。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultMaskUrl

    @ResultMaskUrl.setter
    def ResultMaskUrl(self, ResultMaskUrl):
        self._ResultMaskUrl = ResultMaskUrl

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultImage = params.get("ResultImage")
        self._ResultMask = params.get("ResultMask")
        self._HasForeground = params.get("HasForeground")
        self._ResultImageUrl = params.get("ResultImageUrl")
        self._ResultMaskUrl = params.get("ResultMaskUrl")
        self._RequestId = params.get("RequestId")


class SegmentationOptions(AbstractModel):
    """此参数为分割选项，请根据需要选择自己所想从图片中分割的部分。注意所有选项均为非必选，如未选择则值默认为false, 但是必须要保证多于一个选项的描述为true。

    """

    def __init__(self):
        r"""
        :param _Background: 分割选项-背景
        :type Background: bool
        :param _Hair: 分割选项-头发
        :type Hair: bool
        :param _LeftEyebrow: 分割选项-左眉
        :type LeftEyebrow: bool
        :param _RightEyebrow: 分割选项-右眉
        :type RightEyebrow: bool
        :param _LeftEye: 分割选项-左眼
        :type LeftEye: bool
        :param _RightEye: 分割选项-右眼
        :type RightEye: bool
        :param _Nose: 分割选项-鼻子
        :type Nose: bool
        :param _UpperLip: 分割选项-上唇
        :type UpperLip: bool
        :param _LowerLip: 分割选项-下唇
        :type LowerLip: bool
        :param _Tooth: 分割选项-牙齿
        :type Tooth: bool
        :param _Mouth: 分割选项-口腔（不包含牙齿）
        :type Mouth: bool
        :param _LeftEar: 分割选项-左耳
        :type LeftEar: bool
        :param _RightEar: 分割选项-右耳
        :type RightEar: bool
        :param _Face: 分割选项-面部(不包含眼、耳、口、鼻等五官及头发。)
        :type Face: bool
        :param _Head: 复合分割选项-头部(包含所有的头部元素，相关装饰除外)
        :type Head: bool
        :param _Body: 分割选项-身体（包含脖子）
        :type Body: bool
        :param _Hat: 分割选项-帽子
        :type Hat: bool
        :param _Headdress: 分割选项-头饰
        :type Headdress: bool
        :param _Earrings: 分割选项-耳环
        :type Earrings: bool
        :param _Necklace: 分割选项-项链
        :type Necklace: bool
        :param _Belongings: 分割选项-随身物品（ 例如伞、包、手机等。 ）
        :type Belongings: bool
        """
        self._Background = None
        self._Hair = None
        self._LeftEyebrow = None
        self._RightEyebrow = None
        self._LeftEye = None
        self._RightEye = None
        self._Nose = None
        self._UpperLip = None
        self._LowerLip = None
        self._Tooth = None
        self._Mouth = None
        self._LeftEar = None
        self._RightEar = None
        self._Face = None
        self._Head = None
        self._Body = None
        self._Hat = None
        self._Headdress = None
        self._Earrings = None
        self._Necklace = None
        self._Belongings = None

    @property
    def Background(self):
        """分割选项-背景
        :rtype: bool
        """
        return self._Background

    @Background.setter
    def Background(self, Background):
        self._Background = Background

    @property
    def Hair(self):
        """分割选项-头发
        :rtype: bool
        """
        return self._Hair

    @Hair.setter
    def Hair(self, Hair):
        self._Hair = Hair

    @property
    def LeftEyebrow(self):
        """分割选项-左眉
        :rtype: bool
        """
        return self._LeftEyebrow

    @LeftEyebrow.setter
    def LeftEyebrow(self, LeftEyebrow):
        self._LeftEyebrow = LeftEyebrow

    @property
    def RightEyebrow(self):
        """分割选项-右眉
        :rtype: bool
        """
        return self._RightEyebrow

    @RightEyebrow.setter
    def RightEyebrow(self, RightEyebrow):
        self._RightEyebrow = RightEyebrow

    @property
    def LeftEye(self):
        """分割选项-左眼
        :rtype: bool
        """
        return self._LeftEye

    @LeftEye.setter
    def LeftEye(self, LeftEye):
        self._LeftEye = LeftEye

    @property
    def RightEye(self):
        """分割选项-右眼
        :rtype: bool
        """
        return self._RightEye

    @RightEye.setter
    def RightEye(self, RightEye):
        self._RightEye = RightEye

    @property
    def Nose(self):
        """分割选项-鼻子
        :rtype: bool
        """
        return self._Nose

    @Nose.setter
    def Nose(self, Nose):
        self._Nose = Nose

    @property
    def UpperLip(self):
        """分割选项-上唇
        :rtype: bool
        """
        return self._UpperLip

    @UpperLip.setter
    def UpperLip(self, UpperLip):
        self._UpperLip = UpperLip

    @property
    def LowerLip(self):
        """分割选项-下唇
        :rtype: bool
        """
        return self._LowerLip

    @LowerLip.setter
    def LowerLip(self, LowerLip):
        self._LowerLip = LowerLip

    @property
    def Tooth(self):
        """分割选项-牙齿
        :rtype: bool
        """
        return self._Tooth

    @Tooth.setter
    def Tooth(self, Tooth):
        self._Tooth = Tooth

    @property
    def Mouth(self):
        """分割选项-口腔（不包含牙齿）
        :rtype: bool
        """
        return self._Mouth

    @Mouth.setter
    def Mouth(self, Mouth):
        self._Mouth = Mouth

    @property
    def LeftEar(self):
        """分割选项-左耳
        :rtype: bool
        """
        return self._LeftEar

    @LeftEar.setter
    def LeftEar(self, LeftEar):
        self._LeftEar = LeftEar

    @property
    def RightEar(self):
        """分割选项-右耳
        :rtype: bool
        """
        return self._RightEar

    @RightEar.setter
    def RightEar(self, RightEar):
        self._RightEar = RightEar

    @property
    def Face(self):
        """分割选项-面部(不包含眼、耳、口、鼻等五官及头发。)
        :rtype: bool
        """
        return self._Face

    @Face.setter
    def Face(self, Face):
        self._Face = Face

    @property
    def Head(self):
        """复合分割选项-头部(包含所有的头部元素，相关装饰除外)
        :rtype: bool
        """
        return self._Head

    @Head.setter
    def Head(self, Head):
        self._Head = Head

    @property
    def Body(self):
        """分割选项-身体（包含脖子）
        :rtype: bool
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Hat(self):
        """分割选项-帽子
        :rtype: bool
        """
        return self._Hat

    @Hat.setter
    def Hat(self, Hat):
        self._Hat = Hat

    @property
    def Headdress(self):
        """分割选项-头饰
        :rtype: bool
        """
        return self._Headdress

    @Headdress.setter
    def Headdress(self, Headdress):
        self._Headdress = Headdress

    @property
    def Earrings(self):
        """分割选项-耳环
        :rtype: bool
        """
        return self._Earrings

    @Earrings.setter
    def Earrings(self, Earrings):
        self._Earrings = Earrings

    @property
    def Necklace(self):
        """分割选项-项链
        :rtype: bool
        """
        return self._Necklace

    @Necklace.setter
    def Necklace(self, Necklace):
        self._Necklace = Necklace

    @property
    def Belongings(self):
        """分割选项-随身物品（ 例如伞、包、手机等。 ）
        :rtype: bool
        """
        return self._Belongings

    @Belongings.setter
    def Belongings(self, Belongings):
        self._Belongings = Belongings


    def _deserialize(self, params):
        self._Background = params.get("Background")
        self._Hair = params.get("Hair")
        self._LeftEyebrow = params.get("LeftEyebrow")
        self._RightEyebrow = params.get("RightEyebrow")
        self._LeftEye = params.get("LeftEye")
        self._RightEye = params.get("RightEye")
        self._Nose = params.get("Nose")
        self._UpperLip = params.get("UpperLip")
        self._LowerLip = params.get("LowerLip")
        self._Tooth = params.get("Tooth")
        self._Mouth = params.get("Mouth")
        self._LeftEar = params.get("LeftEar")
        self._RightEar = params.get("RightEar")
        self._Face = params.get("Face")
        self._Head = params.get("Head")
        self._Body = params.get("Body")
        self._Hat = params.get("Hat")
        self._Headdress = params.get("Headdress")
        self._Earrings = params.get("Earrings")
        self._Necklace = params.get("Necklace")
        self._Belongings = params.get("Belongings")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateSegmentationTaskRequest(AbstractModel):
    """TerminateSegmentationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskID: 在提交分割任务成功时返回的任务标识ID。
        :type TaskID: str
        """
        self._TaskID = None

    @property
    def TaskID(self):
        """在提交分割任务成功时返回的任务标识ID。
        :rtype: str
        """
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
        


class TerminateSegmentationTaskResponse(AbstractModel):
    """TerminateSegmentationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Trace(AbstractModel):
    """人体动作轨迹信息

    """

    def __init__(self):
        r"""
        :param _Images: 人体动作轨迹图片 Base64 数组。 
数组长度最小为1最大为5。 
单个图片 base64 编码后大小不可超过2M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Images: list of str
        :param _Urls: 人体动作轨迹图片 Url 数组。 
数组长度最小为1最大为5。 
单个图片 base64 编码后大小不可超过2M。 
Urls、Images必须提供一个，如果都提供，只使用 Urls。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Urls: list of str
        :param _BodyRects: 若输入的Images 和 Urls 是已经裁剪后的人体小图，则可以忽略本参数。 
若否，或图片中包含多个人体，则需要通过本参数来指定图片中的人体框。 
顺序对应 Images 或 Urls 中的顺序。  
当不输入本参数时，我们将认为输入图片已是经过裁剪后的人体小图，不会进行人体检测而直接进行特征提取处理。
        :type BodyRects: list of BodyRect
        """
        self._Images = None
        self._Urls = None
        self._BodyRects = None

    @property
    def Images(self):
        """人体动作轨迹图片 Base64 数组。 
数组长度最小为1最大为5。 
单个图片 base64 编码后大小不可超过2M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :rtype: list of str
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def Urls(self):
        """人体动作轨迹图片 Url 数组。 
数组长度最小为1最大为5。 
单个图片 base64 编码后大小不可超过2M。 
Urls、Images必须提供一个，如果都提供，只使用 Urls。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :rtype: list of str
        """
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def BodyRects(self):
        """若输入的Images 和 Urls 是已经裁剪后的人体小图，则可以忽略本参数。 
若否，或图片中包含多个人体，则需要通过本参数来指定图片中的人体框。 
顺序对应 Images 或 Urls 中的顺序。  
当不输入本参数时，我们将认为输入图片已是经过裁剪后的人体小图，不会进行人体检测而直接进行特征提取处理。
        :rtype: list of BodyRect
        """
        return self._BodyRects

    @BodyRects.setter
    def BodyRects(self, BodyRects):
        self._BodyRects = BodyRects


    def _deserialize(self, params):
        self._Images = params.get("Images")
        self._Urls = params.get("Urls")
        if params.get("BodyRects") is not None:
            self._BodyRects = []
            for item in params.get("BodyRects"):
                obj = BodyRect()
                obj._deserialize(item)
                self._BodyRects.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TraceInfo(AbstractModel):
    """人体动作轨迹信息。

    """

    def __init__(self):
        r"""
        :param _TraceId: 人体动作轨迹ID。
        :type TraceId: str
        :param _BodyIds: 包含的人体动作轨迹图片Id列表。
        :type BodyIds: list of str
        """
        self._TraceId = None
        self._BodyIds = None

    @property
    def TraceId(self):
        """人体动作轨迹ID。
        :rtype: str
        """
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def BodyIds(self):
        """包含的人体动作轨迹图片Id列表。
        :rtype: list of str
        """
        return self._BodyIds

    @BodyIds.setter
    def BodyIds(self, BodyIds):
        self._BodyIds = BodyIds


    def _deserialize(self, params):
        self._TraceId = params.get("TraceId")
        self._BodyIds = params.get("BodyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpperBodyCloth(AbstractModel):
    """上衣属性信息

    """

    def __init__(self):
        r"""
        :param _Texture: 上衣纹理信息。
        :type Texture: :class:`tencentcloud.bda.v20200324.models.UpperBodyClothTexture`
        :param _Color: 上衣颜色信息。
        :type Color: :class:`tencentcloud.bda.v20200324.models.UpperBodyClothColor`
        :param _Sleeve: 上衣衣袖信息。
        :type Sleeve: :class:`tencentcloud.bda.v20200324.models.UpperBodyClothSleeve`
        """
        self._Texture = None
        self._Color = None
        self._Sleeve = None

    @property
    def Texture(self):
        """上衣纹理信息。
        :rtype: :class:`tencentcloud.bda.v20200324.models.UpperBodyClothTexture`
        """
        return self._Texture

    @Texture.setter
    def Texture(self, Texture):
        self._Texture = Texture

    @property
    def Color(self):
        """上衣颜色信息。
        :rtype: :class:`tencentcloud.bda.v20200324.models.UpperBodyClothColor`
        """
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color

    @property
    def Sleeve(self):
        """上衣衣袖信息。
        :rtype: :class:`tencentcloud.bda.v20200324.models.UpperBodyClothSleeve`
        """
        return self._Sleeve

    @Sleeve.setter
    def Sleeve(self, Sleeve):
        self._Sleeve = Sleeve


    def _deserialize(self, params):
        if params.get("Texture") is not None:
            self._Texture = UpperBodyClothTexture()
            self._Texture._deserialize(params.get("Texture"))
        if params.get("Color") is not None:
            self._Color = UpperBodyClothColor()
            self._Color._deserialize(params.get("Color"))
        if params.get("Sleeve") is not None:
            self._Sleeve = UpperBodyClothSleeve()
            self._Sleeve._deserialize(params.get("Sleeve"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpperBodyClothColor(AbstractModel):
    """上衣颜色信息。

    """

    def __init__(self):
        r"""
        :param _Type: 上衣颜色信息，返回值为以下集合中的一个 {红色系, 黄色系, 绿色系, 蓝色系, 黑色系, 灰白色系。
        :type Type: str
        :param _Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self._Type = None
        self._Probability = None

    @property
    def Type(self):
        """上衣颜色信息，返回值为以下集合中的一个 {红色系, 黄色系, 绿色系, 蓝色系, 黑色系, 灰白色系。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Probability(self):
        """Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :rtype: float
        """
        return self._Probability

    @Probability.setter
    def Probability(self, Probability):
        self._Probability = Probability


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpperBodyClothSleeve(AbstractModel):
    """上衣衣袖信息。

    """

    def __init__(self):
        r"""
        :param _Type: 上衣衣袖信息, 返回值为以下集合中的一个 {长袖, 短袖}。
        :type Type: str
        :param _Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self._Type = None
        self._Probability = None

    @property
    def Type(self):
        """上衣衣袖信息, 返回值为以下集合中的一个 {长袖, 短袖}。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Probability(self):
        """Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :rtype: float
        """
        return self._Probability

    @Probability.setter
    def Probability(self, Probability):
        self._Probability = Probability


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpperBodyClothTexture(AbstractModel):
    """上衣纹理信息。

    """

    def __init__(self):
        r"""
        :param _Type: 上衣纹理信息，返回值为以下集合中的一个, {纯色, 格子, 大色块}。
        :type Type: str
        :param _Probability: Type识别概率值，[0.0,1.0], 代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self._Type = None
        self._Probability = None

    @property
    def Type(self):
        """上衣纹理信息，返回值为以下集合中的一个, {纯色, 格子, 大色块}。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Probability(self):
        """Type识别概率值，[0.0,1.0], 代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :rtype: float
        """
        return self._Probability

    @Probability.setter
    def Probability(self, Probability):
        self._Probability = Probability


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoBasicInformation(AbstractModel):
    """视频基础信息

    """

    def __init__(self):
        r"""
        :param _FrameWidth: 视频宽度
        :type FrameWidth: int
        :param _FrameHeight: 视频高度
        :type FrameHeight: int
        :param _FramesPerSecond: 视频帧速率(FPS)
        :type FramesPerSecond: int
        :param _Duration: 视频时长
        :type Duration: float
        :param _TotalFrames: 视频帧数
        :type TotalFrames: int
        """
        self._FrameWidth = None
        self._FrameHeight = None
        self._FramesPerSecond = None
        self._Duration = None
        self._TotalFrames = None

    @property
    def FrameWidth(self):
        """视频宽度
        :rtype: int
        """
        return self._FrameWidth

    @FrameWidth.setter
    def FrameWidth(self, FrameWidth):
        self._FrameWidth = FrameWidth

    @property
    def FrameHeight(self):
        """视频高度
        :rtype: int
        """
        return self._FrameHeight

    @FrameHeight.setter
    def FrameHeight(self, FrameHeight):
        self._FrameHeight = FrameHeight

    @property
    def FramesPerSecond(self):
        """视频帧速率(FPS)
        :rtype: int
        """
        return self._FramesPerSecond

    @FramesPerSecond.setter
    def FramesPerSecond(self, FramesPerSecond):
        self._FramesPerSecond = FramesPerSecond

    @property
    def Duration(self):
        """视频时长
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def TotalFrames(self):
        """视频帧数
        :rtype: int
        """
        return self._TotalFrames

    @TotalFrames.setter
    def TotalFrames(self, TotalFrames):
        self._TotalFrames = TotalFrames


    def _deserialize(self, params):
        self._FrameWidth = params.get("FrameWidth")
        self._FrameHeight = params.get("FrameHeight")
        self._FramesPerSecond = params.get("FramesPerSecond")
        self._Duration = params.get("Duration")
        self._TotalFrames = params.get("TotalFrames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        