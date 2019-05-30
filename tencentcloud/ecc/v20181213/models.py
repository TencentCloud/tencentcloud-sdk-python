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
        :param Name: 项目 名字
        :type Name: str
        :param Score: 该项得分
        :type Score: float
        """
        self.Name = None
        self.Score = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Score = params.get("Score")


class CompostionContext(AbstractModel):
    """ocr返回的作文文本信息

    """

    def __init__(self):
        """
        :param Content: 作文内容
        :type Content: str
        """
        self.Content = None


    def _deserialize(self, params):
        self.Content = params.get("Content")


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
        :param Outline: 作文提纲，可选参数，作文的写作要求。
        :type Outline: str
        :param ModelSubject: 范文标题，可选参数，本接口可以依据提供的范文对作文进行评分。
        :type ModelSubject: str
        :param ModelContent: 范文内容，可选参数，同上，范文的正文部分。
        :type ModelContent: str
        """
        self.Content = None
        self.Title = None
        self.Grade = None
        self.Outline = None
        self.ModelSubject = None
        self.ModelContent = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.Title = params.get("Title")
        self.Grade = params.get("Grade")
        self.Outline = params.get("Outline")
        self.ModelSubject = params.get("ModelSubject")
        self.ModelContent = params.get("ModelContent")


class ECCResponse(AbstractModel):
    """ECC返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 整体的批改结果
        :type Data: :class:`tencentcloud.ecc.v20181213.models.CorrectData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CorrectData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class EHOCRRequest(AbstractModel):
    """EHOCR请求参数结构体

    """

    def __init__(self):
        """
        :param Image: 图片所在的url或base64编码后的图像数据，依据InputType而定
        :type Image: str
        :param InputType: 输出图片类型，0表示Image字段是图片所在的url，1表示Image字段是base64编码后的图像数据
        :type InputType: int
        """
        self.Image = None
        self.InputType = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.InputType = params.get("InputType")


class EHOCRResponse(AbstractModel):
    """EHOCR返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 识别后的作文内容
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


class ScoreCategory(AbstractModel):
    """四个维度的得分

    """

    def __init__(self):
        """
        :param Words: 词汇项
        :type Words: :class:`tencentcloud.ecc.v20181213.models.Aspect`
        :param Sentences: 句子项
        :type Sentences: :class:`tencentcloud.ecc.v20181213.models.Aspect`
        :param Structure: 篇章结构
        :type Structure: :class:`tencentcloud.ecc.v20181213.models.Aspect`
        :param Content: 内容
        :type Content: :class:`tencentcloud.ecc.v20181213.models.Aspect`
        """
        self.Words = None
        self.Sentences = None
        self.Structure = None
        self.Content = None


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


class SentenceCom(AbstractModel):
    """句子点评

    """

    def __init__(self):
        """
        :param Suggestions: 点评内容
        :type Suggestions: list of SentenceSuggest
        :param Sentence: 点评的句子信息
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
        """
        self.Type = None
        self.ErrorType = None
        self.Origin = None
        self.Replace = None
        self.Message = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.ErrorType = params.get("ErrorType")
        self.Origin = params.get("Origin")
        self.Replace = params.get("Replace")
        self.Message = params.get("Message")