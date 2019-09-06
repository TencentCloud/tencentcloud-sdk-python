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


class Aspect(AbstractModel):
    """作文批改每个维度名字与得分

    """

    def __init__(self):
        """
        :param Name: 维度名字
        :type Name: str
        :param Score: 维度得分
        :type Score: float
        :param Percentage: 维度分数占比
        :type Percentage: float
        """
        self.Name = None
        self.Score = None
        self.Percentage = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Score = params.get("Score")
        self.Percentage = params.get("Percentage")


class CompostionContext(AbstractModel):
    """图像识别批改接口返回的作文文本信息或批改信息

    """

    def __init__(self):
        """
        :param Content: 作文内容
        :type Content: str
        :param CorrectData: 批改结果
注意：此字段可能返回 null，表示取不到有效值。
        :type CorrectData: :class:`tencentcloud.ecc.v20181213.models.CorrectData`
        :param TaskId: 任务 id，用于查询接口
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param SessionId: 图像识别唯一标识，一次识别一个 SessionId
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        """
        self.Content = None
        self.CorrectData = None
        self.TaskId = None
        self.SessionId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        if params.get("CorrectData") is not None:
            self.CorrectData = CorrectData()
            self.CorrectData._deserialize(params.get("CorrectData"))
        self.TaskId = params.get("TaskId")
        self.SessionId = params.get("SessionId")


class CorrectData(AbstractModel):
    """批改的结果

    """

    def __init__(self):
        """
        :param Score: 总得分
        :type Score: float
        :param ScoreCat: 各项得分详情
        :type ScoreCat: :class:`tencentcloud.ecc.v20181213.models.ScoreCategory`
        :param Comment: 综合评价
        :type Comment: str
        :param SentenceComments: 句子点评
        :type SentenceComments: list of SentenceCom
        """
        self.Score = None
        self.ScoreCat = None
        self.Comment = None
        self.SentenceComments = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        if params.get("ScoreCat") is not None:
            self.ScoreCat = ScoreCategory()
            self.ScoreCat._deserialize(params.get("ScoreCat"))
        self.Comment = params.get("Comment")
        if params.get("SentenceComments") is not None:
            self.SentenceComments = []
            for item in params.get("SentenceComments"):
                obj = SentenceCom()
                obj._deserialize(item)
                self.SentenceComments.append(obj)


class DescribeTaskRequest(AbstractModel):
    """DescribeTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID
        :type TaskId: str
        :param EccAppid: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数（暂时无需传入）。
        :type EccAppid: str
        """
        self.TaskId = None
        self.EccAppid = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.EccAppid = params.get("EccAppid")


class DescribeTaskResponse(AbstractModel):
    """DescribeTask返回参数结构体

    """

    def __init__(self):
        """
        :param Content: 作文识别文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param CorrectData: 整体的批改结果
注意：此字段可能返回 null，表示取不到有效值。
        :type CorrectData: :class:`tencentcloud.ecc.v20181213.models.CorrectData`
        :param Status: 任务状态，“Progressing”: 处理中（此时无结果返回）、“Finished”: 处理完成
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Content = None
        self.CorrectData = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        if params.get("CorrectData") is not None:
            self.CorrectData = CorrectData()
            self.CorrectData._deserialize(params.get("CorrectData"))
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ECCRequest(AbstractModel):
    """ECC请求参数结构体

    """

    def __init__(self):
        """
        :param Content: 作文文本，必填
        :type Content: str
        :param Title: 作文题目，可选参数
        :type Title: str
        :param Grade: 年级标准， 默认以cet4为标准，取值与意义如下：elementary 小学，grade7 grade8 grade9分别对应初一，初二，初三。 grade10 grade11 grade12 分别对应高一，高二，高三，以及cet4和cet6 分别表示 英语4级和6级。
        :type Grade: str
        :param Requirement: 作文提纲，可选参数，作文的写作要求。
        :type Requirement: str
        :param ModelTitle: 范文标题，可选参数，本接口可以依据提供的范文对作文进行评分。
        :type ModelTitle: str
        :param ModelContent: 范文内容，可选参数，同上，范文的正文部分。
        :type ModelContent: str
        :param EccAppid: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数（暂时无需传入）。
        :type EccAppid: str
        :param IsAsync: 异步模式标识，0：同步模式，1：异步模式，默认为同步模式
        :type IsAsync: int
        :param SessionId: 图像识别唯一标识，一次识别一个 SessionId。当传入此前识别接口使用过的 SessionId，则本次批改按图像批改价格收费；如使用了识别接口且本次没有传入 SessionId，则需要加取文本批改的费用；如果直接使用文本批改接口，则只收取文本批改的费用
        :type SessionId: str
        """
        self.Content = None
        self.Title = None
        self.Grade = None
        self.Requirement = None
        self.ModelTitle = None
        self.ModelContent = None
        self.EccAppid = None
        self.IsAsync = None
        self.SessionId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.Title = params.get("Title")
        self.Grade = params.get("Grade")
        self.Requirement = params.get("Requirement")
        self.ModelTitle = params.get("ModelTitle")
        self.ModelContent = params.get("ModelContent")
        self.EccAppid = params.get("EccAppid")
        self.IsAsync = params.get("IsAsync")
        self.SessionId = params.get("SessionId")


class ECCResponse(AbstractModel):
    """ECC返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 整体的批改结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ecc.v20181213.models.CorrectData`
        :param TaskId: 任务 id，用于查询接口
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CorrectData()
            self.Data._deserialize(params.get("Data"))
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class EHOCRRequest(AbstractModel):
    """EHOCR请求参数结构体

    """

    def __init__(self):
        """
        :param Image: 图片所在的url或base64编码后的图像数据，依据InputType而定
        :type Image: str
        :param InputType: 输出图片类型，0 表示 Image 字段是图片所在的 url，1 表示 Image 字段是 base64 编码后的图像数据
        :type InputType: int
        :param EccAppid: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数（暂时无需传入）。
        :type EccAppid: str
        :param SessionId: 图像识别唯一标识，一次识别一个 SessionId，使用识别功能时 SessionId 可用于使用文本批改接口，此时按图像批改价格收费；如使用文本批改接口时没有传入 SessionId，则需要收取文本批改的费用
        :type SessionId: str
        :param ServerType: 服务类型，0：“图像识别”，只返回识别结果，1：“图像批改”，同时返回识别结果与批改结果。默认为 0
        :type ServerType: int
        :param Title: 作文题目，可选参数
        :type Title: str
        :param Grade: 年级标准， 默认以 cet4 为标准，取值与意义如下：elementary 小学，grade7 grade8 grade9分别对应初一，初二，初三。 grade10 grade11 grade12 分别对应高一，高二，高三，以及 cet4 和 cet6 分别表示 英语4级和6级。
        :type Grade: str
        :param Requirement: 作文提纲，可选参数，作文的写作要求。
        :type Requirement: str
        :param ModelTitle: 范文标题，可选参数，本接口可以依据提供的范文对作文进行评分。
        :type ModelTitle: str
        :param ModelContent: 范文内容，可选参数，同上，范文的正文部分。
        :type ModelContent: str
        :param IsAsync: 异步模式标识，0：同步模式，1：异步模式。默认为同步模式
        :type IsAsync: int
        """
        self.Image = None
        self.InputType = None
        self.EccAppid = None
        self.SessionId = None
        self.ServerType = None
        self.Title = None
        self.Grade = None
        self.Requirement = None
        self.ModelTitle = None
        self.ModelContent = None
        self.IsAsync = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.InputType = params.get("InputType")
        self.EccAppid = params.get("EccAppid")
        self.SessionId = params.get("SessionId")
        self.ServerType = params.get("ServerType")
        self.Title = params.get("Title")
        self.Grade = params.get("Grade")
        self.Requirement = params.get("Requirement")
        self.ModelTitle = params.get("ModelTitle")
        self.ModelContent = params.get("ModelContent")
        self.IsAsync = params.get("IsAsync")


class EHOCRResponse(AbstractModel):
    """EHOCR返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 接口返回数据
        :type Data: :class:`tencentcloud.ecc.v20181213.models.CompostionContext`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CompostionContext()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class ErrorCoordinate(AbstractModel):
    """维度单词坐标

    """

    def __init__(self):
        """
        :param Coordinate: 维度单词坐标
        :type Coordinate: list of int
        """
        self.Coordinate = None


    def _deserialize(self, params):
        self.Coordinate = params.get("Coordinate")


class ScoreCategory(AbstractModel):
    """四个维度的得分

    """

    def __init__(self):
        """
        :param Words: 词汇维度
        :type Words: :class:`tencentcloud.ecc.v20181213.models.Aspect`
        :param Sentences: 句子维度
        :type Sentences: :class:`tencentcloud.ecc.v20181213.models.Aspect`
        :param Structure: 篇章结构维度
        :type Structure: :class:`tencentcloud.ecc.v20181213.models.Aspect`
        :param Content: 内容维度
        :type Content: :class:`tencentcloud.ecc.v20181213.models.Aspect`
        :param Score: 维度得分
        :type Score: float
        :param Percentage: 维度分数占比
        :type Percentage: float
        """
        self.Words = None
        self.Sentences = None
        self.Structure = None
        self.Content = None
        self.Score = None
        self.Percentage = None


    def _deserialize(self, params):
        if params.get("Words") is not None:
            self.Words = Aspect()
            self.Words._deserialize(params.get("Words"))
        if params.get("Sentences") is not None:
            self.Sentences = Aspect()
            self.Sentences._deserialize(params.get("Sentences"))
        if params.get("Structure") is not None:
            self.Structure = Aspect()
            self.Structure._deserialize(params.get("Structure"))
        if params.get("Content") is not None:
            self.Content = Aspect()
            self.Content._deserialize(params.get("Content"))
        self.Score = params.get("Score")
        self.Percentage = params.get("Percentage")


class SentenceCom(AbstractModel):
    """批改结果按句点评的详细信息

    """

    def __init__(self):
        """
        :param Suggestions: 句子错误纠正信息
        :type Suggestions: list of SentenceSuggest
        :param Sentence: 句子信息
        :type Sentence: :class:`tencentcloud.ecc.v20181213.models.SentenceItem`
        """
        self.Suggestions = None
        self.Sentence = None


    def _deserialize(self, params):
        if params.get("Suggestions") is not None:
            self.Suggestions = []
            for item in params.get("Suggestions"):
                obj = SentenceSuggest()
                obj._deserialize(item)
                self.Suggestions.append(obj)
        if params.get("Sentence") is not None:
            self.Sentence = SentenceItem()
            self.Sentence._deserialize(params.get("Sentence"))


class SentenceItem(AbstractModel):
    """句子的相关信息

    """

    def __init__(self):
        """
        :param Sentence: 英语句子
        :type Sentence: str
        :param ParaID: 段落id
        :type ParaID: int
        :param SentenceID: 句子id
        :type SentenceID: int
        """
        self.Sentence = None
        self.ParaID = None
        self.SentenceID = None


    def _deserialize(self, params):
        self.Sentence = params.get("Sentence")
        self.ParaID = params.get("ParaID")
        self.SentenceID = params.get("SentenceID")


class SentenceSuggest(AbstractModel):
    """句子批阅建议

    """

    def __init__(self):
        """
        :param Type: 类型
        :type Type: str
        :param ErrorType: 错误类型
        :type ErrorType: str
        :param Origin: 原始单词
        :type Origin: str
        :param Replace: 替换成 的单词
        :type Replace: str
        :param Message: 提示信息
        :type Message: str
        :param ErrorPosition: 维度单词位置，在句子的第几个到第几个单词之间
        :type ErrorPosition: list of int
        :param ErrorCoordinates: 维度单词坐标，错误单词在图片中的坐标，只有传图片时正常返回，传文字时返回[ ]
        :type ErrorCoordinates: list of ErrorCoordinate
        """
        self.Type = None
        self.ErrorType = None
        self.Origin = None
        self.Replace = None
        self.Message = None
        self.ErrorPosition = None
        self.ErrorCoordinates = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.ErrorType = params.get("ErrorType")
        self.Origin = params.get("Origin")
        self.Replace = params.get("Replace")
        self.Message = params.get("Message")
        self.ErrorPosition = params.get("ErrorPosition")
        if params.get("ErrorCoordinates") is not None:
            self.ErrorCoordinates = []
            for item in params.get("ErrorCoordinates"):
                obj = ErrorCoordinate()
                obj._deserialize(item)
                self.ErrorCoordinates.append(obj)