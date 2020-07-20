# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class Age(AbstractModel):
    """人体年龄信息。
    AttributesType 不含 Age 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。

    """

    def __init__(self):
        """
        :param Type: 人体年龄信息，返回值为以下集合中的一个{小孩,青年,中年,老年}。
        :type Type: str
        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")


class AttributesOptions(AbstractModel):
    """返回人体属性选项，此值不填则为不需要返回，可以选择的值为以下六个。
    Age、Bag、Gender、Orientation、UpperBodyCloth、LowerBodyCloth，详细的解释请看对象描述
    需注意本接口最多返回面积最大的 5 个人体属性信息，超过 5 个人体（第 6 个及以后的人体）的人体属性不具备参考意义。

    """

    def __init__(self):
        """
        :param Age: 返回年龄信息
        :type Age: bool
        :param Bag: 返回随身挎包信息
        :type Bag: bool
        :param Gender: 返回性别信息
        :type Gender: bool
        :param Orientation: 返回朝向信息
        :type Orientation: bool
        :param UpperBodyCloth: 返回上装信息
        :type UpperBodyCloth: bool
        :param LowerBodyCloth: 返回下装信息
        :type LowerBodyCloth: bool
        """
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


class Bag(AbstractModel):
    """人体是否挎包。
    AttributesType 不含 Bag 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。

    """

    def __init__(self):
        """
        :param Type: 挎包信息，返回值为以下集合中的一个{双肩包, 斜挎包, 手拎包, 无包}。
        :type Type: str
        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")


class BodyAttributeInfo(AbstractModel):
    """图中检测出的人体属性信息。

    """

    def __init__(self):
        """
        :param Age: 人体年龄信息。 
AttributesType 不含 Age 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type Age: :class:`tencentcloud.bda.v20200324.models.Age`
        :param Bag: 人体是否挎包。 
AttributesType 不含 Bag 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bag: :class:`tencentcloud.bda.v20200324.models.Bag`
        :param Gender: 人体性别信息。 
AttributesType 不含 Gender 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type Gender: :class:`tencentcloud.bda.v20200324.models.Gender`
        :param Orientation: 人体朝向信息。   
AttributesType 不含 UpperBodyCloth 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type Orientation: :class:`tencentcloud.bda.v20200324.models.Orientation`
        :param UpperBodyCloth: 人体上衣属性信息。
AttributesType 不含 Orientation 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpperBodyCloth: :class:`tencentcloud.bda.v20200324.models.UpperBodyCloth`
        :param LowerBodyCloth: 人体下衣属性信息。  
AttributesType 不含 LowerBodyCloth 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type LowerBodyCloth: :class:`tencentcloud.bda.v20200324.models.LowerBodyCloth`
        """
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


class BodyDetectResult(AbstractModel):
    """图中检测出来的人体框。

    """

    def __init__(self):
        """
        :param Confidence: 检测出的人体置信度。 
误识率百分之十对应的阈值是0.14；误识率百分之五对应的阈值是0.32；误识率百分之二对应的阈值是0.62；误识率百分之一对应的阈值是0.81。 
通常情况建议使用阈值0.32，可适用大多数情况。
        :type Confidence: float
        :param BodyRect: 图中检测出来的人体框
        :type BodyRect: :class:`tencentcloud.bda.v20200324.models.BodyRect`
        :param BodyAttributeInfo: 图中检测出的人体属性信息。
        :type BodyAttributeInfo: :class:`tencentcloud.bda.v20200324.models.BodyAttributeInfo`
        """
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


class BodyJointsResult(AbstractModel):
    """人体框和人体关键点信息。

    """

    def __init__(self):
        """
        :param BoundBox: 图中检测出来的人体框。
        :type BoundBox: :class:`tencentcloud.bda.v20200324.models.BoundRect`
        :param BodyJoints: 14个人体关键点的坐标，人体关键点详见KeyPointInfo。
        :type BodyJoints: list of KeyPointInfo
        :param Confidence: 检测出的人体置信度，0-1之间，数值越高越准确。
        :type Confidence: float
        """
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


class BodyRect(AbstractModel):
    """人体框

    """

    def __init__(self):
        """
        :param X: 人体框左上角横坐标。
        :type X: int
        :param Y: 人体框左上角纵坐标。
        :type Y: int
        :param Width: 人体宽度。
        :type Width: int
        :param Height: 人体高度。
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


class BoundRect(AbstractModel):
    """人体框

    """

    def __init__(self):
        """
        :param X: 人体框左上角横坐标。
        :type X: int
        :param Y: 人体框左上角纵坐标。
        :type Y: int
        :param Width: 人体宽度。
        :type Width: int
        :param Height: 人体高度。
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


class Candidate(AbstractModel):
    """识别出的最相似候选人。

    """

    def __init__(self):
        """
        :param PersonId: 人员ID。
        :type PersonId: str
        :param TraceId: 人体轨迹ID。
        :type TraceId: str
        :param Score: 候选者的匹配得分。 
十万人体库下，误识率百分之五对应的分数为70分；误识率百分之二对应的分数为80分；误识率百分之一对应的分数为90分。
 
二十万人体库下，误识率百分之五对应的分数为80分；误识率百分之二对应的分数为90分；误识率百分之一对应的分数为95分。
 
通常情况建议使用分数80分（保召回）。若希望获得较高精度，建议使用分数90分（保准确）。
        :type Score: float
        """
        self.PersonId = None
        self.TraceId = None
        self.Score = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.TraceId = params.get("TraceId")
        self.Score = params.get("Score")


class CreateGroupRequest(AbstractModel):
    """CreateGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupName: 人体库名称，[1,60]个字符，可修改，不可重复。
        :type GroupName: str
        :param GroupId: 人体库 ID，不可修改，不可重复。支持英文、数字、-%@#&_，长度限制64B。
        :type GroupId: str
        :param Tag: 人体库信息备注，[0，40]个字符。
        :type Tag: str
        :param BodyModelVersion: 人体识别所用的算法模型版本。 
目前入参仅支持 “1.0”1个输入。 默认为"1.0"。  
不同算法模型版本对应的人体识别算法不同，新版本的整体效果会优于旧版本，后续我们将推出更新版本。
        :type BodyModelVersion: str
        """
        self.GroupName = None
        self.GroupId = None
        self.Tag = None
        self.BodyModelVersion = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.Tag = params.get("Tag")
        self.BodyModelVersion = params.get("BodyModelVersion")


class CreateGroupResponse(AbstractModel):
    """CreateGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePersonRequest(AbstractModel):
    """CreatePerson请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 待加入的人员库ID。
        :type GroupId: str
        :param PersonName: 人员名称。[1，60]个字符，可修改，可重复。
        :type PersonName: str
        :param PersonId: 人员ID，单个腾讯云账号下不可修改，不可重复。 
支持英文、数字、-%@#&_，，长度限制64B。
        :type PersonId: str
        :param Trace: 人体轨迹信息。
        :type Trace: :class:`tencentcloud.bda.v20200324.models.Trace`
        """
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


class CreatePersonResponse(AbstractModel):
    """CreatePerson返回参数结构体

    """

    def __init__(self):
        """
        :param TraceId: 人员轨迹唯一标识。
        :type TraceId: str
        :param BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param InputRetCode: 输入的人体轨迹图片中的合法性校验结果。
只有为0时结果才有意义。
-1001: 输入图片不合法。-1002: 输入图片不能构成轨迹。
        :type InputRetCode: int
        :param InputRetCodeDetails: 输入的人体轨迹图片中的合法性校验结果详情。 
-1101:图片无效，-1102:url不合法。-1103:图片过大。-1104:图片下载失败。-1105:图片解码失败。-1109:图片分辨率过高。-2023:轨迹中有非同人图片。-2024: 轨迹提取失败。-2025: 人体检测失败。
RetCode 的顺序和入参中Images 或 Urls 的顺序一致。
        :type InputRetCodeDetails: list of int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class CreateTraceRequest(AbstractModel):
    """CreateTrace请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员ID。
        :type PersonId: str
        :param Trace: 人体轨迹信息。
        :type Trace: :class:`tencentcloud.bda.v20200324.models.Trace`
        """
        self.PersonId = None
        self.Trace = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        if params.get("Trace") is not None:
            self.Trace = Trace()
            self.Trace._deserialize(params.get("Trace"))


class CreateTraceResponse(AbstractModel):
    """CreateTrace返回参数结构体

    """

    def __init__(self):
        """
        :param TraceId: 人员轨迹唯一标识。
        :type TraceId: str
        :param BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param InputRetCode: 输入的人体轨迹图片中的合法性校验结果。
只有为0时结果才有意义。
-1001: 输入图片不合法。-1002: 输入图片不能构成轨迹。
        :type InputRetCode: int
        :param InputRetCodeDetails: 输入的人体轨迹图片中的合法性校验结果详情。 
-1101:图片无效，-1102:url不合法。-1103:图片过大。-1104:图片下载失败。-1105:图片解码失败。-1109:图片分辨率过高。-2023:轨迹中有非同人图片。-2024: 轨迹提取失败。-2025: 人体检测失败。
        :type InputRetCodeDetails: list of int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param GroupId: 人体库ID。
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePersonRequest(AbstractModel):
    """DeletePerson请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员ID。
        :type PersonId: str
        """
        self.PersonId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")


class DeletePersonResponse(AbstractModel):
    """DeletePerson返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetectBodyJointsRequest(AbstractModel):
    """DetectBodyJoints请求参数结构体

    """

    def __init__(self):
        """
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。  
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。 
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。  
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        """
        self.Image = None
        self.Url = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")


class DetectBodyJointsResponse(AbstractModel):
    """DetectBodyJoints返回参数结构体

    """

    def __init__(self):
        """
        :param BodyJointsResults: 图中检测出的人体框和人体关键点， 包含14个人体关键点的坐标，建议根据人体框置信度筛选出合格的人体；
        :type BodyJointsResults: list of BodyJointsResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
图片分辨率不得超过 2048*2048。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 人体图片 Url 。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片 base64 编码后大小不可超过5M。 
图片分辨率不得超过 2048*2048。
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param MaxBodyNum: 最多检测的人体数目，默认值为1（仅检测图片中面积最大的那个人体）； 最大值10 ，检测图片中面积最大的10个人体。
        :type MaxBodyNum: int
        :param AttributesOptions: 是否返回年龄、性别、朝向等属性。 
可选项有 Age、Bag、Gender、UpperBodyCloth、LowerBodyCloth、Orientation。  
如果此参数为空则为不需要返回。 
需要将属性组成一个用逗号分隔的字符串，属性之间的顺序没有要求。 
关于各属性的详细描述，参见下文出参。 
最多返回面积最大的 5 个人体属性信息，超过 5 个人体（第 6 个及以后的人体）的 BodyAttributesInfo 不具备参考意义。
        :type AttributesOptions: :class:`tencentcloud.bda.v20200324.models.AttributesOptions`
        """
        self.Image = None
        self.Url = None
        self.MaxBodyNum = None
        self.AttributesOptions = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.MaxBodyNum = params.get("MaxBodyNum")
        if params.get("AttributesOptions") is not None:
            self.AttributesOptions = AttributesOptions()
            self.AttributesOptions._deserialize(params.get("AttributesOptions"))


class DetectBodyResponse(AbstractModel):
    """DetectBody返回参数结构体

    """

    def __init__(self):
        """
        :param BodyDetectResults: 图中检测出来的人体框。
        :type BodyDetectResults: list of BodyDetectResult
        :param BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Type: 性别信息，返回值为以下集合中的一个 {男性, 女性}
        :type Type: str
        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")


class GetGroupListRequest(AbstractModel):
    """GetGroupList请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 起始序号，默认值为0。
        :type Offset: int
        :param Limit: 返回数量，默认值为10，最大值为1000。
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetGroupListResponse(AbstractModel):
    """GetGroupList返回参数结构体

    """

    def __init__(self):
        """
        :param GroupInfos: 返回的人体库信息。
        :type GroupInfos: list of GroupInfo
        :param GroupNum: 人体库总数量。
        :type GroupNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param GroupId: 人体库ID。
        :type GroupId: str
        :param Offset: 起始序号，默认值为0。
        :type Offset: int
        :param Limit: 返回数量，默认值为10，最大值为1000。
        :type Limit: int
        """
        self.GroupId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetPersonListResponse(AbstractModel):
    """GetPersonList返回参数结构体

    """

    def __init__(self):
        """
        :param PersonInfos: 返回的人员信息。
        :type PersonInfos: list of PersonInfo
        :param PersonNum: 该人体库的人员数量。
        :type PersonNum: int
        :param BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param GroupName: 人体库名称。
        :type GroupName: str
        :param GroupId: 人体库ID。
        :type GroupId: str
        :param Tag: 人体库信息备注。
        :type Tag: str
        :param BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param CreationTimestamp: Group的创建时间和日期 CreationTimestamp。CreationTimestamp 的值是自 Unix 纪元时间到Group创建时间的毫秒数。  
Unix 纪元时间是 1970 年 1 月 1 日星期四，协调世界时 (UTC) 。
        :type CreationTimestamp: int
        """
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


class KeyPointInfo(AbstractModel):
    """人体关键点信息

    """

    def __init__(self):
        """
        :param KeyPointType: 代表不同位置的人体关键点信息，返回值为以下集合中的一个 [头部,颈部,右肩,右肘,右腕,左肩,左肘,左腕,右髋,右膝,右踝,左髋,左膝,左踝]
        :type KeyPointType: str
        :param X: 人体关键点横坐标
        :type X: float
        :param Y: 人体关键点纵坐标
        :type Y: float
        """
        self.KeyPointType = None
        self.X = None
        self.Y = None


    def _deserialize(self, params):
        self.KeyPointType = params.get("KeyPointType")
        self.X = params.get("X")
        self.Y = params.get("Y")


class LowerBodyCloth(AbstractModel):
    """下衣属性信息

    """

    def __init__(self):
        """
        :param Color: 下衣颜色信息。
        :type Color: :class:`tencentcloud.bda.v20200324.models.LowerBodyClothColor`
        :param Length: 下衣长度信息 。
        :type Length: :class:`tencentcloud.bda.v20200324.models.LowerBodyClothLength`
        :param Type: 下衣类型信息。
        :type Type: :class:`tencentcloud.bda.v20200324.models.LowerBodyClothType`
        """
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


class LowerBodyClothColor(AbstractModel):
    """下衣颜色信息

    """

    def __init__(self):
        """
        :param Type: 下衣颜色信息，返回值为以下集合中的一个{ 黑色系, 灰白色系, 彩色} 。
        :type Type: str
        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")


class LowerBodyClothLength(AbstractModel):
    """下衣长度信息

    """

    def __init__(self):
        """
        :param Type: 下衣长度信息，返回值为以下集合中的一个，{长, 短} 。
        :type Type: str
        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")


class LowerBodyClothType(AbstractModel):
    """下衣类型信息

    """

    def __init__(self):
        """
        :param Type: 下衣类型，返回值为以下集合中的一个 {裤子,裙子} 。
        :type Type: str
        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")


class ModifyGroupRequest(AbstractModel):
    """ModifyGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 人体库ID。
        :type GroupId: str
        :param GroupName: 人体库名称。
        :type GroupName: str
        :param Tag: 人体库信息备注。
        :type Tag: str
        """
        self.GroupId = None
        self.GroupName = None
        self.Tag = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.Tag = params.get("Tag")


class ModifyGroupResponse(AbstractModel):
    """ModifyGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPersonInfoRequest(AbstractModel):
    """ModifyPersonInfo请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员ID。
        :type PersonId: str
        :param PersonName: 人员名称。
        :type PersonName: str
        """
        self.PersonId = None
        self.PersonName = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.PersonName = params.get("PersonName")


class ModifyPersonInfoResponse(AbstractModel):
    """ModifyPersonInfo返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Orientation(AbstractModel):
    """人体朝向信息。
    AttributesType 不含 Orientation 或检测超过 5 个人体时，此参数仍返回，但不具备参考意义。

    """

    def __init__(self):
        """
        :param Type: 人体朝向信息，返回值为以下集合中的一个 {正向, 背向, 左, 右}。
        :type Type: str
        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")


class PersonInfo(AbstractModel):
    """人员信息。

    """

    def __init__(self):
        """
        :param PersonName: 人员名称。
        :type PersonName: str
        :param PersonId: 人员ID。
        :type PersonId: str
        :param TraceInfos: 包含的人体轨迹图片信息列表。
        :type TraceInfos: list of TraceInfo
        """
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


class SearchTraceRequest(AbstractModel):
    """SearchTrace请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 希望搜索的人体库ID。
        :type GroupId: str
        :param Trace: 人体轨迹信息。
        :type Trace: :class:`tencentcloud.bda.v20200324.models.Trace`
        :param MaxPersonNum: 单张被识别的人体轨迹返回的最相似人员数量。
默认值为5，最大值为100。
 例，设MaxPersonNum为8，则返回Top8相似的人员信息。 值越大，需要处理的时间越长。建议不要超过10。
        :type MaxPersonNum: int
        :param TraceMatchThreshold: 出参Score中，只有超过TraceMatchThreshold值的结果才会返回。
默认为0。范围[0, 100.0]。
        :type TraceMatchThreshold: float
        """
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


class SearchTraceResponse(AbstractModel):
    """SearchTrace返回参数结构体

    """

    def __init__(self):
        """
        :param Candidates: 识别出的最相似候选人。
        :type Candidates: list of Candidate
        :param InputRetCode: 输入的人体轨迹图片中的合法性校验结果。
只有为0时结果才有意义。
-1001: 输入图片不合法。-1002: 输入图片不能构成轨迹。
        :type InputRetCode: int
        :param InputRetCodeDetails: 输入的人体轨迹图片中的合法性校验结果详情。 
-1101:图片无效，-1102:url不合法。-1103:图片过大。-1104:图片下载失败。-1105:图片解码失败。-1109:图片分辨率过高。-2023:轨迹中有非同人图片。-2024: 轨迹提取失败。-2025: 人体检测失败。
        :type InputRetCodeDetails: list of int
        :param BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class SegmentPortraitPicRequest(AbstractModel):
    """SegmentPortraitPic请求参数结构体

    """

    def __init__(self):
        """
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
图片分辨率须小于2000*2000。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片分辨率须小于2000*2000 ，图片 base64 编码后大小不可超过5M。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        """
        self.Image = None
        self.Url = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")


class SegmentPortraitPicResponse(AbstractModel):
    """SegmentPortraitPic返回参数结构体

    """

    def __init__(self):
        """
        :param ResultImage: 处理后的图片 base64 数据，透明背景图
        :type ResultImage: str
        :param ResultMask: 一个通过 Base64 编码的文件，解码后文件由 Float 型浮点数组成。这些浮点数代表原图从左上角开始的每一行的每一个像素点，每一个浮点数的值是原图相应像素点位于人体轮廓内的置信度（0-1）转化的灰度值（0-255）
        :type ResultMask: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultImage = None
        self.ResultMask = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultImage = params.get("ResultImage")
        self.ResultMask = params.get("ResultMask")
        self.RequestId = params.get("RequestId")


class Trace(AbstractModel):
    """人体轨迹信息

    """

    def __init__(self):
        """
        :param Images: 人体轨迹图片 Base64 数组。 
数组长度最小为1最大为5。 
单个图片 base64 编码后大小不可超过2M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Images: list of str
        :param Urls: 人体轨迹图片 Url 数组。 
数组长度最小为1最大为5。 
单个图片 base64 编码后大小不可超过2M。 
Urls、Images必须提供一个，如果都提供，只使用 Urls。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Urls: list of str
        :param BodyRects: 若输入的Images 和 Urls 是已经裁剪后的人体小图，则可以忽略本参数。 
若否，或图片中包含多个人体，则需要通过本参数来指定图片中的人体框。 
顺序对应 Images 或 Urls 中的顺序。  
当不输入本参数时，我们将认为输入图片已是经过裁剪后的人体小图，不会进行人体检测而直接进行特征提取处理。
        :type BodyRects: list of BodyRect
        """
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


class TraceInfo(AbstractModel):
    """人体轨迹信息。

    """

    def __init__(self):
        """
        :param TraceId: 人体轨迹ID。
        :type TraceId: str
        :param BodyIds: 包含的人体轨迹图片Id列表。
        :type BodyIds: list of str
        """
        self.TraceId = None
        self.BodyIds = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        self.BodyIds = params.get("BodyIds")


class UpperBodyCloth(AbstractModel):
    """上衣属性信息

    """

    def __init__(self):
        """
        :param Texture: 上衣纹理信息。
        :type Texture: :class:`tencentcloud.bda.v20200324.models.UpperBodyClothTexture`
        :param Color: 上衣颜色信息。
        :type Color: :class:`tencentcloud.bda.v20200324.models.UpperBodyClothColor`
        :param Sleeve: 上衣衣袖信息。
        :type Sleeve: :class:`tencentcloud.bda.v20200324.models.UpperBodyClothSleeve`
        """
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


class UpperBodyClothColor(AbstractModel):
    """上衣颜色信息。

    """

    def __init__(self):
        """
        :param Type: 上衣颜色信息，返回值为以下集合中的一个 {红色系, 黄色系, 绿色系, 蓝色系, 黑色系, 灰白色系。
        :type Type: str
        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")


class UpperBodyClothSleeve(AbstractModel):
    """上衣衣袖信息。

    """

    def __init__(self):
        """
        :param Type: 上衣衣袖信息, 返回值为以下集合中的一个 {长袖, 短袖}。
        :type Type: str
        :param Probability: Type识别概率值，[0.0,1.0],代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")


class UpperBodyClothTexture(AbstractModel):
    """上衣纹理信息。

    """

    def __init__(self):
        """
        :param Type: 上衣纹理信息，返回值为以下集合中的一个, {纯色, 格子, 大色块}。
        :type Type: str
        :param Probability: Type识别概率值，[0.0,1.0], 代表判断正确的概率。如0.8则代表有Type值有80%概率正确。
        :type Probability: float
        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")