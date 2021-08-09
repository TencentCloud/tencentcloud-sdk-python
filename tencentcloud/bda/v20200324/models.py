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
        """
        :param Type: 人体年龄信息，返回值为以下集合中的一个{小孩,青年,中年,老年}。\n        :type Type: str\n        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。\n        :type Probability: float\n        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttributesOptions(AbstractModel):
    """返回人体属性选项，此值不填则为不需要返回，可以选择的值为以下六个。
    Age、Bag、Gender、Orientation、UpperBodyCloth、LowerBodyCloth，详细的解释请看对象描述
    需注意本接口最多返回面积最大的 5 个人体属性信息，超过 5 个人体（第 6 个及以后的人体）的人体属性不具备参考意义。

    """

    def __init__(self):
        """
        :param Age: 返回年龄信息\n        :type Age: bool\n        :param Bag: 返回随身挎包信息\n        :type Bag: bool\n        :param Gender: 返回性别信息\n        :type Gender: bool\n        :param Orientation: 返回朝向信息\n        :type Orientation: bool\n        :param UpperBodyCloth: 返回上装信息\n        :type UpperBodyCloth: bool\n        :param LowerBodyCloth: 返回下装信息\n        :type LowerBodyCloth: bool\n        """
        self.Age = None
        self.Bag = None
        self.Gender = None
        self.Orientation = None
        self.UpperBodyCloth = None
        self.LowerBodyCloth = None


    def _deserialize(self, params):
        self.Age = params.get("Age")
        self.Bag = params.get("Bag")
        self.Gender = params.get("Gender")
        self.Orientation = params.get("Orientation")
        self.UpperBodyCloth = params.get("UpperBodyCloth")
        self.LowerBodyCloth = params.get("LowerBodyCloth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Bag(AbstractModel):
    """人体是否挎包。
    AttributesType 不含 Bag 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。

    """

    def __init__(self):
        """
        :param Type: 挎包信息，返回值为以下集合中的一个{双肩包, 斜挎包, 手拎包, 无包}。\n        :type Type: str\n        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。\n        :type Probability: float\n        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BodyAttributeInfo(AbstractModel):
    """图中检测出的人体属性信息。

    """

    def __init__(self):
        """
        :param Age: 人体年龄信息。 
AttributesType 不含 Age 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Age: :class:`tencentcloud.bda.v20200324.models.Age`\n        :param Bag: 人体是否挎包。 
AttributesType 不含 Bag 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Bag: :class:`tencentcloud.bda.v20200324.models.Bag`\n        :param Gender: 人体性别信息。 
AttributesType 不含 Gender 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Gender: :class:`tencentcloud.bda.v20200324.models.Gender`\n        :param Orientation: 人体朝向信息。   
AttributesType 不含 UpperBodyCloth 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Orientation: :class:`tencentcloud.bda.v20200324.models.Orientation`\n        :param UpperBodyCloth: 人体上衣属性信息。
AttributesType 不含 Orientation 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpperBodyCloth: :class:`tencentcloud.bda.v20200324.models.UpperBodyCloth`\n        :param LowerBodyCloth: 人体下衣属性信息。  
AttributesType 不含 LowerBodyCloth 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LowerBodyCloth: :class:`tencentcloud.bda.v20200324.models.LowerBodyCloth`\n        """
        self.Age = None
        self.Bag = None
        self.Gender = None
        self.Orientation = None
        self.UpperBodyCloth = None
        self.LowerBodyCloth = None


    def _deserialize(self, params):
        if params.get("Age") is not None:
            self.Age = Age()
            self.Age._deserialize(params.get("Age"))
        if params.get("Bag") is not None:
            self.Bag = Bag()
            self.Bag._deserialize(params.get("Bag"))
        if params.get("Gender") is not None:
            self.Gender = Gender()
            self.Gender._deserialize(params.get("Gender"))
        if params.get("Orientation") is not None:
            self.Orientation = Orientation()
            self.Orientation._deserialize(params.get("Orientation"))
        if params.get("UpperBodyCloth") is not None:
            self.UpperBodyCloth = UpperBodyCloth()
            self.UpperBodyCloth._deserialize(params.get("UpperBodyCloth"))
        if params.get("LowerBodyCloth") is not None:
            self.LowerBodyCloth = LowerBodyCloth()
            self.LowerBodyCloth._deserialize(params.get("LowerBodyCloth"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BodyDetectResult(AbstractModel):
    """图中检测出来的人体框。

    """

    def __init__(self):
        """
        :param Confidence: 检测出的人体置信度。 
误识率百分之十对应的阈值是0.14；误识率百分之五对应的阈值是0.32；误识率百分之二对应的阈值是0.62；误识率百分之一对应的阈值是0.81。 
通常情况建议使用阈值0.32，可适用大多数情况。\n        :type Confidence: float\n        :param BodyRect: 图中检测出来的人体框\n        :type BodyRect: :class:`tencentcloud.bda.v20200324.models.BodyRect`\n        :param BodyAttributeInfo: 图中检测出的人体属性信息。\n        :type BodyAttributeInfo: :class:`tencentcloud.bda.v20200324.models.BodyAttributeInfo`\n        """
        self.Confidence = None
        self.BodyRect = None
        self.BodyAttributeInfo = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        if params.get("BodyRect") is not None:
            self.BodyRect = BodyRect()
            self.BodyRect._deserialize(params.get("BodyRect"))
        if params.get("BodyAttributeInfo") is not None:
            self.BodyAttributeInfo = BodyAttributeInfo()
            self.BodyAttributeInfo._deserialize(params.get("BodyAttributeInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BodyJointsResult(AbstractModel):
    """人体框和人体关键点信息。

    """

    def __init__(self):
        """
        :param BoundBox: 图中检测出来的人体框。\n        :type BoundBox: :class:`tencentcloud.bda.v20200324.models.BoundRect`\n        :param BodyJoints: 14个人体关键点的坐标，人体关键点详见KeyPointInfo。\n        :type BodyJoints: list of KeyPointInfo\n        :param Confidence: 检测出的人体置信度，0-1之间，数值越高越准确。\n        :type Confidence: float\n        """
        self.BoundBox = None
        self.BodyJoints = None
        self.Confidence = None


    def _deserialize(self, params):
        if params.get("BoundBox") is not None:
            self.BoundBox = BoundRect()
            self.BoundBox._deserialize(params.get("BoundBox"))
        if params.get("BodyJoints") is not None:
            self.BodyJoints = []
            for item in params.get("BodyJoints"):
                obj = KeyPointInfo()
                obj._deserialize(item)
                self.BodyJoints.append(obj)
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BodyRect(AbstractModel):
    """人体框

    """

    def __init__(self):
        """
        :param X: 人体框左上角横坐标。\n        :type X: int\n        :param Y: 人体框左上角纵坐标。\n        :type Y: int\n        :param Width: 人体宽度。\n        :type Width: int\n        :param Height: 人体高度。\n        :type Height: int\n        """
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
        


class BoundRect(AbstractModel):
    """人体框

    """

    def __init__(self):
        """
        :param X: 人体框左上角横坐标。\n        :type X: int\n        :param Y: 人体框左上角纵坐标。\n        :type Y: int\n        :param Width: 人体宽度。\n        :type Width: int\n        :param Height: 人体高度。\n        :type Height: int\n        """
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
        


class Candidate(AbstractModel):
    """识别出的最相似候选人。

    """

    def __init__(self):
        """
        :param PersonId: 人员ID。\n        :type PersonId: str\n        :param TraceId: 人体轨迹ID。\n        :type TraceId: str\n        :param Score: 候选者的匹配得分。 
十万人体库下，误识率百分之五对应的分数为70分；误识率百分之二对应的分数为80分；误识率百分之一对应的分数为90分。
 
二十万人体库下，误识率百分之五对应的分数为80分；误识率百分之二对应的分数为90分；误识率百分之一对应的分数为95分。
 
通常情况建议使用分数80分（保召回）。若希望获得较高精度，建议使用分数90分（保准确）。\n        :type Score: float\n        """
        self.PersonId = None
        self.TraceId = None
        self.Score = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.TraceId = params.get("TraceId")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupRequest(AbstractModel):
    """CreateGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupName: 人体库名称，[1,60]个字符，可修改，不可重复。\n        :type GroupName: str\n        :param GroupId: 人体库 ID，不可修改，不可重复。支持英文、数字、-%@#&_，长度限制64B。\n        :type GroupId: str\n        :param Tag: 人体库信息备注，[0，40]个字符。\n        :type Tag: str\n        :param BodyModelVersion: 人体识别所用的算法模型版本。 
目前入参仅支持 “1.0”1个输入。 默认为"1.0"。  
不同算法模型版本对应的人体识别算法不同，新版本的整体效果会优于旧版本，后续我们将推出更新版本。\n        :type BodyModelVersion: str\n        """
        self.GroupName = None
        self.GroupId = None
        self.Tag = None
        self.BodyModelVersion = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.Tag = params.get("Tag")
        self.BodyModelVersion = params.get("BodyModelVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupResponse(AbstractModel):
    """CreateGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePersonRequest(AbstractModel):
    """CreatePerson请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 待加入的人员库ID。\n        :type GroupId: str\n        :param PersonName: 人员名称。[1，60]个字符，可修改，可重复。\n        :type PersonName: str\n        :param PersonId: 人员ID，单个腾讯云账号下不可修改，不可重复。 
支持英文、数字、-%@#&_，，长度限制64B。\n        :type PersonId: str\n        :param Trace: 人体轨迹信息。\n        :type Trace: :class:`tencentcloud.bda.v20200324.models.Trace`\n        """
        self.GroupId = None
        self.PersonName = None
        self.PersonId = None
        self.Trace = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PersonName = params.get("PersonName")
        self.PersonId = params.get("PersonId")
        if params.get("Trace") is not None:
            self.Trace = Trace()
            self.Trace._deserialize(params.get("Trace"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePersonResponse(AbstractModel):
    """CreatePerson返回参数结构体

    """

    def __init__(self):
        """
        :param TraceId: 人员轨迹唯一标识。\n        :type TraceId: str\n        :param BodyModelVersion: 人体识别所用的算法模型版本。\n        :type BodyModelVersion: str\n        :param InputRetCode: 输入的人体轨迹图片中的合法性校验结果。
只有为0时结果才有意义。
-1001: 输入图片不合法。-1002: 输入图片不能构成轨迹。\n        :type InputRetCode: int\n        :param InputRetCodeDetails: 输入的人体轨迹图片中的合法性校验结果详情。 
-1101:图片无效，-1102:url不合法。-1103:图片过大。-1104:图片下载失败。-1105:图片解码失败。-1109:图片分辨率过高。-2023:轨迹中有非同人图片。-2024: 轨迹提取失败。-2025: 人体检测失败。
RetCode 的顺序和入参中Images 或 Urls 的顺序一致。\n        :type InputRetCodeDetails: list of int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TraceId = None
        self.BodyModelVersion = None
        self.InputRetCode = None
        self.InputRetCodeDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.InputRetCode = params.get("InputRetCode")
        self.InputRetCodeDetails = params.get("InputRetCodeDetails")
        self.RequestId = params.get("RequestId")


class CreateSegmentationTaskRequest(AbstractModel):
    """CreateSegmentationTask请求参数结构体

    """

    def __init__(self):
        """
        :param VideoUrl: 需要分割的视频URL，可外网访问。\n        :type VideoUrl: str\n        :param BackgroundImageUrl: 背景图片URL。 
可以将视频背景替换为输入的图片。 
如果不输入背景图片，则输出人像区域mask。\n        :type BackgroundImageUrl: str\n        :param Config: 预留字段，后期用于展示更多识别信息。\n        :type Config: str\n        """
        self.VideoUrl = None
        self.BackgroundImageUrl = None
        self.Config = None


    def _deserialize(self, params):
        self.VideoUrl = params.get("VideoUrl")
        self.BackgroundImageUrl = params.get("BackgroundImageUrl")
        self.Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSegmentationTaskResponse(AbstractModel):
    """CreateSegmentationTask返回参数结构体

    """

    def __init__(self):
        """
        :param TaskID: 任务标识ID,可以用与追溯任务状态，查看任务结果\n        :type TaskID: str\n        :param EstimatedProcessingTime: 预估处理时间，单位为秒\n        :type EstimatedProcessingTime: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskID = None
        self.EstimatedProcessingTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        self.EstimatedProcessingTime = params.get("EstimatedProcessingTime")
        self.RequestId = params.get("RequestId")


class CreateTraceRequest(AbstractModel):
    """CreateTrace请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员ID。\n        :type PersonId: str\n        :param Trace: 人体轨迹信息。\n        :type Trace: :class:`tencentcloud.bda.v20200324.models.Trace`\n        """
        self.PersonId = None
        self.Trace = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        if params.get("Trace") is not None:
            self.Trace = Trace()
            self.Trace._deserialize(params.get("Trace"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTraceResponse(AbstractModel):
    """CreateTrace返回参数结构体

    """

    def __init__(self):
        """
        :param TraceId: 人员轨迹唯一标识。\n        :type TraceId: str\n        :param BodyModelVersion: 人体识别所用的算法模型版本。\n        :type BodyModelVersion: str\n        :param InputRetCode: 输入的人体轨迹图片中的合法性校验结果。
只有为0时结果才有意义。
-1001: 输入图片不合法。-1002: 输入图片不能构成轨迹。\n        :type InputRetCode: int\n        :param InputRetCodeDetails: 输入的人体轨迹图片中的合法性校验结果详情。 
-1101:图片无效，-1102:url不合法。-1103:图片过大。-1104:图片下载失败。-1105:图片解码失败。-1109:图片分辨率过高。-2023:轨迹中有非同人图片。-2024: 轨迹提取失败。-2025: 人体检测失败。\n        :type InputRetCodeDetails: list of int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TraceId = None
        self.BodyModelVersion = None
        self.InputRetCode = None
        self.InputRetCodeDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.InputRetCode = params.get("InputRetCode")
        self.InputRetCodeDetails = params.get("InputRetCodeDetails")
        self.RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 人体库ID。\n        :type GroupId: str\n        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePersonRequest(AbstractModel):
    """DeletePerson请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员ID。\n        :type PersonId: str\n        """
        self.PersonId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePersonResponse(AbstractModel):
    """DeletePerson返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeSegmentationTaskRequest(AbstractModel):
    """DescribeSegmentationTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskID: 在提交分割任务成功时返回的任务标识ID。\n        :type TaskID: str\n        """
        self.TaskID = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSegmentationTaskResponse(AbstractModel):
    """DescribeSegmentationTask返回参数结构体

    """

    def __init__(self):
        """
        :param TaskStatus: 当前任务状态：
QUEUING 排队中
PROCESSING 处理中
FINISHED 处理完成\n        :type TaskStatus: str\n        :param ResultVideoUrl: 分割后视频URL, 存储于腾讯云COS
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResultVideoUrl: str\n        :param ResultVideoMD5: 分割后视频MD5，用于校验
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResultVideoMD5: str\n        :param VideoBasicInformation: 视频基本信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type VideoBasicInformation: :class:`tencentcloud.bda.v20200324.models.VideoBasicInformation`\n        :param ErrorMsg: 分割任务错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskStatus = None
        self.ResultVideoUrl = None
        self.ResultVideoMD5 = None
        self.VideoBasicInformation = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskStatus = params.get("TaskStatus")
        self.ResultVideoUrl = params.get("ResultVideoUrl")
        self.ResultVideoMD5 = params.get("ResultVideoMD5")
        if params.get("VideoBasicInformation") is not None:
            self.VideoBasicInformation = VideoBasicInformation()
            self.VideoBasicInformation._deserialize(params.get("VideoBasicInformation"))
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class DetectBodyJointsRequest(AbstractModel):
    """DetectBodyJoints请求参数结构体

    """

    def __init__(self):
        """
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。  
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。\n        :type Image: str\n        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。 
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。  
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。\n        :type Url: str\n        """
        self.Image = None
        self.Url = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectBodyJointsResponse(AbstractModel):
    """DetectBodyJoints返回参数结构体

    """

    def __init__(self):
        """
        :param BodyJointsResults: 图中检测出的人体框和人体关键点， 包含14个人体关键点的坐标，建议根据人体框置信度筛选出合格的人体；\n        :type BodyJointsResults: list of BodyJointsResult\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BodyJointsResults = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BodyJointsResults") is not None:
            self.BodyJointsResults = []
            for item in params.get("BodyJointsResults"):
                obj = BodyJointsResult()
                obj._deserialize(item)
                self.BodyJointsResults.append(obj)
        self.RequestId = params.get("RequestId")


class DetectBodyRequest(AbstractModel):
    """DetectBody请求参数结构体

    """

    def __init__(self):
        """
        :param Image: 人体图片 Base64 数据。
图片 base64 编码后大小不可超过5M。
图片分辨率不得超过 1920 * 1080 。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。\n        :type Image: str\n        :param MaxBodyNum: 最多检测的人体数目，默认值为1（仅检测图片中面积最大的那个人体）； 最大值10 ，检测图片中面积最大的10个人体。\n        :type MaxBodyNum: int\n        :param Url: 人体图片 Url 。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片 base64 编码后大小不可超过5M。 
图片分辨率不得超过 1920 * 1080 。
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。\n        :type Url: str\n        :param AttributesOptions: 是否返回年龄、性别、朝向等属性。 
可选项有 Age、Bag、Gender、UpperBodyCloth、LowerBodyCloth、Orientation。  
如果此参数为空则为不需要返回。 
需要将属性组成一个用逗号分隔的字符串，属性之间的顺序没有要求。 
关于各属性的详细描述，参见下文出参。 
最多返回面积最大的 5 个人体属性信息，超过 5 个人体（第 6 个及以后的人体）的 BodyAttributesInfo 不具备参考意义。\n        :type AttributesOptions: :class:`tencentcloud.bda.v20200324.models.AttributesOptions`\n        """
        self.Image = None
        self.MaxBodyNum = None
        self.Url = None
        self.AttributesOptions = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.MaxBodyNum = params.get("MaxBodyNum")
        self.Url = params.get("Url")
        if params.get("AttributesOptions") is not None:
            self.AttributesOptions = AttributesOptions()
            self.AttributesOptions._deserialize(params.get("AttributesOptions"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectBodyResponse(AbstractModel):
    """DetectBody返回参数结构体

    """

    def __init__(self):
        """
        :param BodyDetectResults: 图中检测出来的人体框。\n        :type BodyDetectResults: list of BodyDetectResult\n        :param BodyModelVersion: 人体识别所用的算法模型版本。\n        :type BodyModelVersion: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BodyDetectResults = None
        self.BodyModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BodyDetectResults") is not None:
            self.BodyDetectResults = []
            for item in params.get("BodyDetectResults"):
                obj = BodyDetectResult()
                obj._deserialize(item)
                self.BodyDetectResults.append(obj)
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.RequestId = params.get("RequestId")


class Gender(AbstractModel):
    """人体性别信息。
    AttributesType 不含 Gender 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。

    """

    def __init__(self):
        """
        :param Type: 性别信息，返回值为以下集合中的一个 {男性, 女性}\n        :type Type: str\n        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。\n        :type Probability: float\n        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupListRequest(AbstractModel):
    """GetGroupList请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 起始序号，默认值为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认值为10，最大值为1000。\n        :type Limit: int\n        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupListResponse(AbstractModel):
    """GetGroupList返回参数结构体

    """

    def __init__(self):
        """
        :param GroupInfos: 返回的人体库信息。\n        :type GroupInfos: list of GroupInfo\n        :param GroupNum: 人体库总数量。\n        :type GroupNum: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.GroupInfos = None
        self.GroupNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GroupInfos") is not None:
            self.GroupInfos = []
            for item in params.get("GroupInfos"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.GroupInfos.append(obj)
        self.GroupNum = params.get("GroupNum")
        self.RequestId = params.get("RequestId")


class GetPersonListRequest(AbstractModel):
    """GetPersonList请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 人体库ID。\n        :type GroupId: str\n        :param Offset: 起始序号，默认值为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认值为10，最大值为1000。\n        :type Limit: int\n        """
        self.GroupId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPersonListResponse(AbstractModel):
    """GetPersonList返回参数结构体

    """

    def __init__(self):
        """
        :param PersonInfos: 返回的人员信息。\n        :type PersonInfos: list of PersonInfo\n        :param PersonNum: 该人体库的人员数量。\n        :type PersonNum: int\n        :param BodyModelVersion: 人体识别所用的算法模型版本。\n        :type BodyModelVersion: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PersonInfos = None
        self.PersonNum = None
        self.BodyModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PersonInfos") is not None:
            self.PersonInfos = []
            for item in params.get("PersonInfos"):
                obj = PersonInfo()
                obj._deserialize(item)
                self.PersonInfos.append(obj)
        self.PersonNum = params.get("PersonNum")
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.RequestId = params.get("RequestId")


class GroupInfo(AbstractModel):
    """返回的人员库信息。

    """

    def __init__(self):
        """
        :param GroupName: 人体库名称。\n        :type GroupName: str\n        :param GroupId: 人体库ID。\n        :type GroupId: str\n        :param Tag: 人体库信息备注。\n        :type Tag: str\n        :param BodyModelVersion: 人体识别所用的算法模型版本。\n        :type BodyModelVersion: str\n        :param CreationTimestamp: Group的创建时间和日期 CreationTimestamp。CreationTimestamp 的值是自 Unix 纪元时间到Group创建时间的毫秒数。  
Unix 纪元时间是 1970 年 1 月 1 日星期四，协调世界时 (UTC) 。\n        :type CreationTimestamp: int\n        """
        self.GroupName = None
        self.GroupId = None
        self.Tag = None
        self.BodyModelVersion = None
        self.CreationTimestamp = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.Tag = params.get("Tag")
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.CreationTimestamp = params.get("CreationTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageRect(AbstractModel):
    """图像坐标信息。

    """

    def __init__(self):
        """
        :param X: 左上角横坐标。\n        :type X: int\n        :param Y: 左上角纵坐标。\n        :type Y: int\n        :param Width: 人体宽度。\n        :type Width: int\n        :param Height: 人体高度。\n        :type Height: int\n        :param Label: 分割选项名称。\n        :type Label: str\n        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None
        self.Label = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyPointInfo(AbstractModel):
    """人体关键点信息

    """

    def __init__(self):
        """
        :param KeyPointType: 代表不同位置的人体关键点信息，返回值为以下集合中的一个 [头部,颈部,右肩,右肘,右腕,左肩,左肘,左腕,右髋,右膝,右踝,左髋,左膝,左踝]\n        :type KeyPointType: str\n        :param X: 人体关键点横坐标\n        :type X: float\n        :param Y: 人体关键点纵坐标\n        :type Y: float\n        """
        self.KeyPointType = None
        self.X = None
        self.Y = None


    def _deserialize(self, params):
        self.KeyPointType = params.get("KeyPointType")
        self.X = params.get("X")
        self.Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LowerBodyCloth(AbstractModel):
    """下衣属性信息

    """

    def __init__(self):
        """
        :param Color: 下衣颜色信息。\n        :type Color: :class:`tencentcloud.bda.v20200324.models.LowerBodyClothColor`\n        :param Length: 下衣长度信息 。\n        :type Length: :class:`tencentcloud.bda.v20200324.models.LowerBodyClothLength`\n        :param Type: 下衣类型信息。\n        :type Type: :class:`tencentcloud.bda.v20200324.models.LowerBodyClothType`\n        """
        self.Color = None
        self.Length = None
        self.Type = None


    def _deserialize(self, params):
        if params.get("Color") is not None:
            self.Color = LowerBodyClothColor()
            self.Color._deserialize(params.get("Color"))
        if params.get("Length") is not None:
            self.Length = LowerBodyClothLength()
            self.Length._deserialize(params.get("Length"))
        if params.get("Type") is not None:
            self.Type = LowerBodyClothType()
            self.Type._deserialize(params.get("Type"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LowerBodyClothColor(AbstractModel):
    """下衣颜色信息

    """

    def __init__(self):
        """
        :param Type: 下衣颜色信息，返回值为以下集合中的一个{ 黑色系, 灰白色系, 彩色} 。\n        :type Type: str\n        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。\n        :type Probability: float\n        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LowerBodyClothLength(AbstractModel):
    """下衣长度信息

    """

    def __init__(self):
        """
        :param Type: 下衣长度信息，返回值为以下集合中的一个，{长, 短} 。\n        :type Type: str\n        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。\n        :type Probability: float\n        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LowerBodyClothType(AbstractModel):
    """下衣类型信息

    """

    def __init__(self):
        """
        :param Type: 下衣类型，返回值为以下集合中的一个 {裤子,裙子} 。\n        :type Type: str\n        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。\n        :type Probability: float\n        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupRequest(AbstractModel):
    """ModifyGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 人体库ID。\n        :type GroupId: str\n        :param GroupName: 人体库名称。\n        :type GroupName: str\n        :param Tag: 人体库信息备注。\n        :type Tag: str\n        """
        self.GroupId = None
        self.GroupName = None
        self.Tag = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupResponse(AbstractModel):
    """ModifyGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPersonInfoRequest(AbstractModel):
    """ModifyPersonInfo请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员ID。\n        :type PersonId: str\n        :param PersonName: 人员名称。\n        :type PersonName: str\n        """
        self.PersonId = None
        self.PersonName = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.PersonName = params.get("PersonName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonInfoResponse(AbstractModel):
    """ModifyPersonInfo返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Orientation(AbstractModel):
    """人体朝向信息。
    AttributesType 不含 Orientation 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。

    """

    def __init__(self):
        """
        :param Type: 人体朝向信息，返回值为以下集合中的一个 {正向, 背向, 左, 右}。\n        :type Type: str\n        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。\n        :type Probability: float\n        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonInfo(AbstractModel):
    """人员信息。

    """

    def __init__(self):
        """
        :param PersonName: 人员名称。\n        :type PersonName: str\n        :param PersonId: 人员ID。\n        :type PersonId: str\n        :param TraceInfos: 包含的人体轨迹图片信息列表。\n        :type TraceInfos: list of TraceInfo\n        """
        self.PersonName = None
        self.PersonId = None
        self.TraceInfos = None


    def _deserialize(self, params):
        self.PersonName = params.get("PersonName")
        self.PersonId = params.get("PersonId")
        if params.get("TraceInfos") is not None:
            self.TraceInfos = []
            for item in params.get("TraceInfos"):
                obj = TraceInfo()
                obj._deserialize(item)
                self.TraceInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchTraceRequest(AbstractModel):
    """SearchTrace请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 希望搜索的人体库ID。\n        :type GroupId: str\n        :param Trace: 人体轨迹信息。\n        :type Trace: :class:`tencentcloud.bda.v20200324.models.Trace`\n        :param MaxPersonNum: 单张被识别的人体轨迹返回的最相似人员数量。
默认值为5，最大值为100。
 例，设MaxPersonNum为8，则返回Top8相似的人员信息。 值越大，需要处理的时间越长。建议不要超过10。\n        :type MaxPersonNum: int\n        :param TraceMatchThreshold: 出参Score中，只有超过TraceMatchThreshold值的结果才会返回。
默认为0。范围[0, 100.0]。\n        :type TraceMatchThreshold: float\n        """
        self.GroupId = None
        self.Trace = None
        self.MaxPersonNum = None
        self.TraceMatchThreshold = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        if params.get("Trace") is not None:
            self.Trace = Trace()
            self.Trace._deserialize(params.get("Trace"))
        self.MaxPersonNum = params.get("MaxPersonNum")
        self.TraceMatchThreshold = params.get("TraceMatchThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchTraceResponse(AbstractModel):
    """SearchTrace返回参数结构体

    """

    def __init__(self):
        """
        :param Candidates: 识别出的最相似候选人。\n        :type Candidates: list of Candidate\n        :param InputRetCode: 输入的人体轨迹图片中的合法性校验结果。
只有为0时结果才有意义。
-1001: 输入图片不合法。-1002: 输入图片不能构成轨迹。\n        :type InputRetCode: int\n        :param InputRetCodeDetails: 输入的人体轨迹图片中的合法性校验结果详情。 
-1101:图片无效，-1102:url不合法。-1103:图片过大。-1104:图片下载失败。-1105:图片解码失败。-1109:图片分辨率过高。-2023:轨迹中有非同人图片。-2024: 轨迹提取失败。-2025: 人体检测失败。\n        :type InputRetCodeDetails: list of int\n        :param BodyModelVersion: 人体识别所用的算法模型版本。\n        :type BodyModelVersion: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Candidates = None
        self.InputRetCode = None
        self.InputRetCodeDetails = None
        self.BodyModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Candidates") is not None:
            self.Candidates = []
            for item in params.get("Candidates"):
                obj = Candidate()
                obj._deserialize(item)
                self.Candidates.append(obj)
        self.InputRetCode = params.get("InputRetCode")
        self.InputRetCodeDetails = params.get("InputRetCodeDetails")
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.RequestId = params.get("RequestId")


class SegmentCustomizedPortraitPicRequest(AbstractModel):
    """SegmentCustomizedPortraitPic请求参数结构体

    """

    def __init__(self):
        """
        :param SegmentationOptions: 此参数为分割选项，请根据需要选择自己所想从图片中分割的部分。注意所有选项均为非必选，如未选择则值默认为false, 但是必须要保证多于一个选项的描述为true。\n        :type SegmentationOptions: :class:`tencentcloud.bda.v20200324.models.SegmentationOptions`\n        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
图片分辨率须小于2000*2000。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。\n        :type Image: str\n        :param Url: 图片的 Url 。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片分辨率须小于2000*2000 ，图片 base64 编码后大小不可超过5M。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。\n        :type Url: str\n        """
        self.SegmentationOptions = None
        self.Image = None
        self.Url = None


    def _deserialize(self, params):
        if params.get("SegmentationOptions") is not None:
            self.SegmentationOptions = SegmentationOptions()
            self.SegmentationOptions._deserialize(params.get("SegmentationOptions"))
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SegmentCustomizedPortraitPicResponse(AbstractModel):
    """SegmentCustomizedPortraitPic返回参数结构体

    """

    def __init__(self):
        """
        :param PortraitImage: 根据指定标签分割输出的透明背景人像图片的 base64 数据。\n        :type PortraitImage: str\n        :param MaskImage: 指定标签处理后的Mask。一个通过 Base64 编码的文件，解码后文件由 Float 型浮点数组成。这些浮点数代表原图从左上角开始的每一行的每一个像素点，每一个浮点数的值是原图相应像素点位于人体轮廓内的置信度（0-1）转化的灰度值（0-255）\n        :type MaskImage: str\n        :param ImageRects: 坐标信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageRects: list of ImageRect\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PortraitImage = None
        self.MaskImage = None
        self.ImageRects = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PortraitImage = params.get("PortraitImage")
        self.MaskImage = params.get("MaskImage")
        if params.get("ImageRects") is not None:
            self.ImageRects = []
            for item in params.get("ImageRects"):
                obj = ImageRect()
                obj._deserialize(item)
                self.ImageRects.append(obj)
        self.RequestId = params.get("RequestId")


class SegmentPortraitPicRequest(AbstractModel):
    """SegmentPortraitPic请求参数结构体

    """

    def __init__(self):
        """
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
图片分辨率须小于2000*2000。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。\n        :type Image: str\n        :param Url: 图片的 Url 。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片分辨率须小于2000*2000 ，图片 base64 编码后大小不可超过5M。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。\n        :type Url: str\n        """
        self.Image = None
        self.Url = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SegmentPortraitPicResponse(AbstractModel):
    """SegmentPortraitPic返回参数结构体

    """

    def __init__(self):
        """
        :param ResultImage: 处理后的图片 base64 数据，透明背景图\n        :type ResultImage: str\n        :param ResultMask: 一个通过 Base64 编码的文件，解码后文件由 Float 型浮点数组成。这些浮点数代表原图从左上角开始的每一行的每一个像素点，每一个浮点数的值是原图相应像素点位于人体轮廓内的置信度（0-1）转化的灰度值（0-255）\n        :type ResultMask: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ResultImage = None
        self.ResultMask = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultImage = params.get("ResultImage")
        self.ResultMask = params.get("ResultMask")
        self.RequestId = params.get("RequestId")


class SegmentationOptions(AbstractModel):
    """此参数为分割选项，请根据需要选择自己所想从图片中分割的部分。注意所有选项均为非必选，如未选择则值默认为false, 但是必须要保证多于一个选项的描述为true。

    """

    def __init__(self):
        """
        :param Background: 分割选项-背景\n        :type Background: bool\n        :param Hair: 分割选项-头发\n        :type Hair: bool\n        :param LeftEyebrow: 分割选项-左眉\n        :type LeftEyebrow: bool\n        :param RightEyebrow: 分割选项-右眉\n        :type RightEyebrow: bool\n        :param LeftEye: 分割选项-左眼\n        :type LeftEye: bool\n        :param RightEye: 分割选项-右眼\n        :type RightEye: bool\n        :param Nose: 分割选项-鼻子\n        :type Nose: bool\n        :param UpperLip: 分割选项-上唇\n        :type UpperLip: bool\n        :param LowerLip: 分割选项-下唇\n        :type LowerLip: bool\n        :param Tooth: 分割选项-牙齿\n        :type Tooth: bool\n        :param Mouth: 分割选项-口腔（不包含牙齿）\n        :type Mouth: bool\n        :param LeftEar: 分割选项-左耳\n        :type LeftEar: bool\n        :param RightEar: 分割选项-右耳\n        :type RightEar: bool\n        :param Face: 分割选项-面部(不包含眼、耳、口、鼻等五官及头发。)\n        :type Face: bool\n        :param Head: 复合分割选项-头部(包含所有的头部元素，相关装饰除外)\n        :type Head: bool\n        :param Body: 分割选项-身体（包含脖子）\n        :type Body: bool\n        :param Hat: 分割选项-帽子\n        :type Hat: bool\n        :param Headdress: 分割选项-头饰\n        :type Headdress: bool\n        :param Earrings: 分割选项-耳环\n        :type Earrings: bool\n        :param Necklace: 分割选项-项链\n        :type Necklace: bool\n        :param Belongings: 分割选项-随身物品（ 例如伞、包、手机等。 ）\n        :type Belongings: bool\n        """
        self.Background = None
        self.Hair = None
        self.LeftEyebrow = None
        self.RightEyebrow = None
        self.LeftEye = None
        self.RightEye = None
        self.Nose = None
        self.UpperLip = None
        self.LowerLip = None
        self.Tooth = None
        self.Mouth = None
        self.LeftEar = None
        self.RightEar = None
        self.Face = None
        self.Head = None
        self.Body = None
        self.Hat = None
        self.Headdress = None
        self.Earrings = None
        self.Necklace = None
        self.Belongings = None


    def _deserialize(self, params):
        self.Background = params.get("Background")
        self.Hair = params.get("Hair")
        self.LeftEyebrow = params.get("LeftEyebrow")
        self.RightEyebrow = params.get("RightEyebrow")
        self.LeftEye = params.get("LeftEye")
        self.RightEye = params.get("RightEye")
        self.Nose = params.get("Nose")
        self.UpperLip = params.get("UpperLip")
        self.LowerLip = params.get("LowerLip")
        self.Tooth = params.get("Tooth")
        self.Mouth = params.get("Mouth")
        self.LeftEar = params.get("LeftEar")
        self.RightEar = params.get("RightEar")
        self.Face = params.get("Face")
        self.Head = params.get("Head")
        self.Body = params.get("Body")
        self.Hat = params.get("Hat")
        self.Headdress = params.get("Headdress")
        self.Earrings = params.get("Earrings")
        self.Necklace = params.get("Necklace")
        self.Belongings = params.get("Belongings")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateSegmentationTaskRequest(AbstractModel):
    """TerminateSegmentationTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskID: 在提交分割任务成功时返回的任务标识ID。\n        :type TaskID: str\n        """
        self.TaskID = None


    def _deserialize(self, params):
        self.TaskID = params.get("TaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateSegmentationTaskResponse(AbstractModel):
    """TerminateSegmentationTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Trace(AbstractModel):
    """人体轨迹信息

    """

    def __init__(self):
        """
        :param Images: 人体轨迹图片 Base64 数组。 
数组长度最小为1最大为5。 
单个图片 base64 编码后大小不可超过2M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。\n        :type Images: list of str\n        :param Urls: 人体轨迹图片 Url 数组。 
数组长度最小为1最大为5。 
单个图片 base64 编码后大小不可超过2M。 
Urls、Images必须提供一个，如果都提供，只使用 Urls。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。\n        :type Urls: list of str\n        :param BodyRects: 若输入的Images 和 Urls 是已经裁剪后的人体小图，则可以忽略本参数。 
若否，或图片中包含多个人体，则需要通过本参数来指定图片中的人体框。 
顺序对应 Images 或 Urls 中的顺序。  
当不输入本参数时，我们将认为输入图片已是经过裁剪后的人体小图，不会进行人体检测而直接进行特征提取处理。\n        :type BodyRects: list of BodyRect\n        """
        self.Images = None
        self.Urls = None
        self.BodyRects = None


    def _deserialize(self, params):
        self.Images = params.get("Images")
        self.Urls = params.get("Urls")
        if params.get("BodyRects") is not None:
            self.BodyRects = []
            for item in params.get("BodyRects"):
                obj = BodyRect()
                obj._deserialize(item)
                self.BodyRects.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TraceInfo(AbstractModel):
    """人体轨迹信息。

    """

    def __init__(self):
        """
        :param TraceId: 人体轨迹ID。\n        :type TraceId: str\n        :param BodyIds: 包含的人体轨迹图片Id列表。\n        :type BodyIds: list of str\n        """
        self.TraceId = None
        self.BodyIds = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        self.BodyIds = params.get("BodyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpperBodyCloth(AbstractModel):
    """上衣属性信息

    """

    def __init__(self):
        """
        :param Texture: 上衣纹理信息。\n        :type Texture: :class:`tencentcloud.bda.v20200324.models.UpperBodyClothTexture`\n        :param Color: 上衣颜色信息。\n        :type Color: :class:`tencentcloud.bda.v20200324.models.UpperBodyClothColor`\n        :param Sleeve: 上衣衣袖信息。\n        :type Sleeve: :class:`tencentcloud.bda.v20200324.models.UpperBodyClothSleeve`\n        """
        self.Texture = None
        self.Color = None
        self.Sleeve = None


    def _deserialize(self, params):
        if params.get("Texture") is not None:
            self.Texture = UpperBodyClothTexture()
            self.Texture._deserialize(params.get("Texture"))
        if params.get("Color") is not None:
            self.Color = UpperBodyClothColor()
            self.Color._deserialize(params.get("Color"))
        if params.get("Sleeve") is not None:
            self.Sleeve = UpperBodyClothSleeve()
            self.Sleeve._deserialize(params.get("Sleeve"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpperBodyClothColor(AbstractModel):
    """上衣颜色信息。

    """

    def __init__(self):
        """
        :param Type: 上衣颜色信息，返回值为以下集合中的一个 {红色系, 黄色系, 绿色系, 蓝色系, 黑色系, 灰白色系。\n        :type Type: str\n        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。\n        :type Probability: float\n        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpperBodyClothSleeve(AbstractModel):
    """上衣衣袖信息。

    """

    def __init__(self):
        """
        :param Type: 上衣衣袖信息, 返回值为以下集合中的一个 {长袖, 短袖}。\n        :type Type: str\n        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。\n        :type Probability: float\n        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpperBodyClothTexture(AbstractModel):
    """上衣纹理信息。

    """

    def __init__(self):
        """
        :param Type: 上衣纹理信息，返回值为以下集合中的一个, {纯色, 格子, 大色块}。\n        :type Type: str\n        :param Probability: Type识别概率值，[0.0,1.0], 代表判断正确的概率。如0.8则代表有Type值有80%概率正确。\n        :type Probability: float\n        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoBasicInformation(AbstractModel):
    """视频基础信息

    """

    def __init__(self):
        """
        :param FrameWidth: 视频宽度\n        :type FrameWidth: int\n        :param FrameHeight: 视频高度\n        :type FrameHeight: int\n        :param FramesPerSecond: 视频帧速率(FPS)\n        :type FramesPerSecond: int\n        :param Duration: 视频时长\n        :type Duration: float\n        :param TotalFrames: 视频帧数\n        :type TotalFrames: int\n        """
        self.FrameWidth = None
        self.FrameHeight = None
        self.FramesPerSecond = None
        self.Duration = None
        self.TotalFrames = None


    def _deserialize(self, params):
        self.FrameWidth = params.get("FrameWidth")
        self.FrameHeight = params.get("FrameHeight")
        self.FramesPerSecond = params.get("FramesPerSecond")
        self.Duration = params.get("Duration")
        self.TotalFrames = params.get("TotalFrames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        