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


class Aspect(AbstractModel):
    """作文批改每个维度名字与得分

    """

    def __init__(self):
        r"""
        :param _Name: 维度名字
        :type Name: str
        :param _Score: 维度得分
        :type Score: float
        :param _Percentage: 维度分数占比
        :type Percentage: float
        """
        self._Name = None
        self._Score = None
        self._Percentage = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Percentage(self):
        return self._Percentage

    @Percentage.setter
    def Percentage(self, Percentage):
        self._Percentage = Percentage


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Score = params.get("Score")
        self._Percentage = params.get("Percentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompostionContext(AbstractModel):
    """图像识别批改接口返回的作文文本信息或批改信息

    """

    def __init__(self):
        r"""
        :param _Content: 作文内容
        :type Content: str
        :param _CorrectData: 批改结果
注意：此字段可能返回 null，表示取不到有效值。
        :type CorrectData: :class:`tencentcloud.ecc.v20181213.models.CorrectData`
        :param _TaskId: 任务 id，用于查询接口
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _SessionId: 图像识别唯一标识，一次识别一个 SessionId
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        """
        self._Content = None
        self._CorrectData = None
        self._TaskId = None
        self._SessionId = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CorrectData(self):
        return self._CorrectData

    @CorrectData.setter
    def CorrectData(self, CorrectData):
        self._CorrectData = CorrectData

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._Content = params.get("Content")
        if params.get("CorrectData") is not None:
            self._CorrectData = CorrectData()
            self._CorrectData._deserialize(params.get("CorrectData"))
        self._TaskId = params.get("TaskId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CorrectData(AbstractModel):
    """批改的结果

    """

    def __init__(self):
        r"""
        :param _Score: 总得分
        :type Score: float
        :param _ScoreCat: 各项得分详情
        :type ScoreCat: :class:`tencentcloud.ecc.v20181213.models.ScoreCategory`
        :param _Comment: 综合评价
        :type Comment: str
        :param _SentenceComments: 句子点评
        :type SentenceComments: list of SentenceCom
        """
        self._Score = None
        self._ScoreCat = None
        self._Comment = None
        self._SentenceComments = None

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def ScoreCat(self):
        return self._ScoreCat

    @ScoreCat.setter
    def ScoreCat(self, ScoreCat):
        self._ScoreCat = ScoreCat

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def SentenceComments(self):
        return self._SentenceComments

    @SentenceComments.setter
    def SentenceComments(self, SentenceComments):
        self._SentenceComments = SentenceComments


    def _deserialize(self, params):
        self._Score = params.get("Score")
        if params.get("ScoreCat") is not None:
            self._ScoreCat = ScoreCategory()
            self._ScoreCat._deserialize(params.get("ScoreCat"))
        self._Comment = params.get("Comment")
        if params.get("SentenceComments") is not None:
            self._SentenceComments = []
            for item in params.get("SentenceComments"):
                obj = SentenceCom()
                obj._deserialize(item)
                self._SentenceComments.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CorrectMultiImageRequest(AbstractModel):
    """CorrectMultiImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Image: 图片的url链接或base64数据。每张图片数据作为数组的一个元素，数组个数与图片个数保持一致。存放类别依据InputType而定，url与base64编码不能混合使用。
        :type Image: list of str
        :param _InputType: 输出图片类型，0 表示 Image 字段是图片所在的 url，1 表示 Image 字段是 base64 编码后的图像数据。
        :type InputType: int
        :param _EccAppid: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数。
        :type EccAppid: str
        :param _SessionId: 图像识别唯一标识，一次识别一个 SessionId，使用识别功能时 SessionId 可用于使用文本批改接口，此时按图像批改价格收费；如使用文本批改接口时没有传入 SessionId，则需要收取文本批改的费用。
        :type SessionId: str
        :param _ServerType: 服务类型，0：“多图像识别”，只返回识别结果；1：“多图像批改”，同时返回识别结果与批改结果。默认为 0。
        :type ServerType: int
        :param _Title: 作文题目，可选参数
        :type Title: str
        :param _Grade: 年级标准， 默认以 cet4 为标准，取值与意义如下：elementary 小学，grade7 grade8 grade9分别对应初一，初二，初三。 grade10 grade11 grade12 分别对应高一，高二，高三，以及 cet4 和 cet6 分别表示 英语4级和6级。
        :type Grade: str
        :param _Requirement: 作文提纲，可选参数，作文的写作要求。
        :type Requirement: str
        :param _ModelTitle: 范文标题，可选参数，本接口可以依据提供的范文对作文进行评分。
        :type ModelTitle: str
        :param _ModelContent: 范文内容，可选参数，同上，范文的正文部分。
        :type ModelContent: str
        :param _IsAsync: 异步模式标识，0：同步模式，1：异步模式。默认为同步模式
        :type IsAsync: int
        """
        self._Image = None
        self._InputType = None
        self._EccAppid = None
        self._SessionId = None
        self._ServerType = None
        self._Title = None
        self._Grade = None
        self._Requirement = None
        self._ModelTitle = None
        self._ModelContent = None
        self._IsAsync = None

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def InputType(self):
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def EccAppid(self):
        return self._EccAppid

    @EccAppid.setter
    def EccAppid(self, EccAppid):
        self._EccAppid = EccAppid

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def ServerType(self):
        return self._ServerType

    @ServerType.setter
    def ServerType(self, ServerType):
        self._ServerType = ServerType

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Grade(self):
        return self._Grade

    @Grade.setter
    def Grade(self, Grade):
        self._Grade = Grade

    @property
    def Requirement(self):
        return self._Requirement

    @Requirement.setter
    def Requirement(self, Requirement):
        self._Requirement = Requirement

    @property
    def ModelTitle(self):
        return self._ModelTitle

    @ModelTitle.setter
    def ModelTitle(self, ModelTitle):
        self._ModelTitle = ModelTitle

    @property
    def ModelContent(self):
        return self._ModelContent

    @ModelContent.setter
    def ModelContent(self, ModelContent):
        self._ModelContent = ModelContent

    @property
    def IsAsync(self):
        return self._IsAsync

    @IsAsync.setter
    def IsAsync(self, IsAsync):
        self._IsAsync = IsAsync


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._InputType = params.get("InputType")
        self._EccAppid = params.get("EccAppid")
        self._SessionId = params.get("SessionId")
        self._ServerType = params.get("ServerType")
        self._Title = params.get("Title")
        self._Grade = params.get("Grade")
        self._Requirement = params.get("Requirement")
        self._ModelTitle = params.get("ModelTitle")
        self._ModelContent = params.get("ModelContent")
        self._IsAsync = params.get("IsAsync")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CorrectMultiImageResponse(AbstractModel):
    """CorrectMultiImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 接口返回数据
        :type Data: :class:`tencentcloud.ecc.v20181213.models.CompostionContext`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CompostionContext()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTaskRequest(AbstractModel):
    """DescribeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID
        :type TaskId: str
        :param _EccAppid: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数（暂时无需传入）。
        :type EccAppid: str
        """
        self._TaskId = None
        self._EccAppid = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def EccAppid(self):
        return self._EccAppid

    @EccAppid.setter
    def EccAppid(self, EccAppid):
        self._EccAppid = EccAppid


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._EccAppid = params.get("EccAppid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskResponse(AbstractModel):
    """DescribeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 作文识别文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _CorrectData: 整体的批改结果
注意：此字段可能返回 null，表示取不到有效值。
        :type CorrectData: :class:`tencentcloud.ecc.v20181213.models.CorrectData`
        :param _Status: 任务状态，“Progressing”: 处理中（此时无结果返回）、“Finished”: 处理完成
        :type Status: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Content = None
        self._CorrectData = None
        self._Status = None
        self._RequestId = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CorrectData(self):
        return self._CorrectData

    @CorrectData.setter
    def CorrectData(self, CorrectData):
        self._CorrectData = CorrectData

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Content = params.get("Content")
        if params.get("CorrectData") is not None:
            self._CorrectData = CorrectData()
            self._CorrectData._deserialize(params.get("CorrectData"))
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ECCRequest(AbstractModel):
    """ECC请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 作文文本，必填
        :type Content: str
        :param _Title: 作文题目，可选参数
        :type Title: str
        :param _Grade: 年级标准， 默认以cet4为标准，取值与意义如下：elementary 小学，grade7 grade8 grade9分别对应初一，初二，初三。 grade10 grade11 grade12 分别对应高一，高二，高三，以及cet4和cet6 分别表示 英语4级和6级。
        :type Grade: str
        :param _Requirement: 作文提纲，可选参数，作文的写作要求。
        :type Requirement: str
        :param _ModelTitle: 范文标题，可选参数，本接口可以依据提供的范文对作文进行评分。
        :type ModelTitle: str
        :param _ModelContent: 范文内容，可选参数，同上，范文的正文部分。
        :type ModelContent: str
        :param _EccAppid: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数（暂时无需传入）。
        :type EccAppid: str
        :param _IsAsync: 异步模式标识，0：同步模式，1：异步模式，默认为同步模式
        :type IsAsync: int
        :param _SessionId: 图像识别唯一标识，一次识别一个 SessionId。当传入此前识别接口使用过的 SessionId，则本次批改按图像批改价格收费；如使用了识别接口且本次没有传入 SessionId，则需要加取文本批改的费用；如果直接使用文本批改接口，则只收取文本批改的费用
        :type SessionId: str
        """
        self._Content = None
        self._Title = None
        self._Grade = None
        self._Requirement = None
        self._ModelTitle = None
        self._ModelContent = None
        self._EccAppid = None
        self._IsAsync = None
        self._SessionId = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Grade(self):
        return self._Grade

    @Grade.setter
    def Grade(self, Grade):
        self._Grade = Grade

    @property
    def Requirement(self):
        return self._Requirement

    @Requirement.setter
    def Requirement(self, Requirement):
        self._Requirement = Requirement

    @property
    def ModelTitle(self):
        return self._ModelTitle

    @ModelTitle.setter
    def ModelTitle(self, ModelTitle):
        self._ModelTitle = ModelTitle

    @property
    def ModelContent(self):
        return self._ModelContent

    @ModelContent.setter
    def ModelContent(self, ModelContent):
        self._ModelContent = ModelContent

    @property
    def EccAppid(self):
        return self._EccAppid

    @EccAppid.setter
    def EccAppid(self, EccAppid):
        self._EccAppid = EccAppid

    @property
    def IsAsync(self):
        return self._IsAsync

    @IsAsync.setter
    def IsAsync(self, IsAsync):
        self._IsAsync = IsAsync

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._Title = params.get("Title")
        self._Grade = params.get("Grade")
        self._Requirement = params.get("Requirement")
        self._ModelTitle = params.get("ModelTitle")
        self._ModelContent = params.get("ModelContent")
        self._EccAppid = params.get("EccAppid")
        self._IsAsync = params.get("IsAsync")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ECCResponse(AbstractModel):
    """ECC返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 整体的批改结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ecc.v20181213.models.CorrectData`
        :param _TaskId: 任务 id，用于查询接口
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TaskId = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CorrectData()
            self._Data._deserialize(params.get("Data"))
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class EHOCRRequest(AbstractModel):
    """EHOCR请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Image: 图片所在的url或base64编码后的图像数据，依据InputType而定
        :type Image: str
        :param _InputType: 输出图片类型，0 表示 Image 字段是图片所在的 url，1 表示 Image 字段是 base64 编码后的图像数据
        :type InputType: int
        :param _EccAppid: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数（暂时无需传入）。
        :type EccAppid: str
        :param _SessionId: 图像识别唯一标识，一次识别一个 SessionId，使用识别功能时 SessionId 可用于使用文本批改接口，此时按图像批改价格收费；如使用文本批改接口时没有传入 SessionId，则需要收取文本批改的费用
        :type SessionId: str
        :param _ServerType: 服务类型，0：“图像识别”，只返回识别结果，1：“图像批改”，同时返回识别结果与批改结果。默认为 0
        :type ServerType: int
        :param _Title: 作文题目，可选参数
        :type Title: str
        :param _Grade: 年级标准， 默认以 cet4 为标准，取值与意义如下：elementary 小学，grade7 grade8 grade9分别对应初一，初二，初三。 grade10 grade11 grade12 分别对应高一，高二，高三，以及 cet4 和 cet6 分别表示 英语4级和6级。
        :type Grade: str
        :param _Requirement: 作文提纲，可选参数，作文的写作要求。
        :type Requirement: str
        :param _ModelTitle: 范文标题，可选参数，本接口可以依据提供的范文对作文进行评分。
        :type ModelTitle: str
        :param _ModelContent: 范文内容，可选参数，同上，范文的正文部分。
        :type ModelContent: str
        :param _IsAsync: 异步模式标识，0：同步模式，1：异步模式。默认为同步模式
        :type IsAsync: int
        """
        self._Image = None
        self._InputType = None
        self._EccAppid = None
        self._SessionId = None
        self._ServerType = None
        self._Title = None
        self._Grade = None
        self._Requirement = None
        self._ModelTitle = None
        self._ModelContent = None
        self._IsAsync = None

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def InputType(self):
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def EccAppid(self):
        return self._EccAppid

    @EccAppid.setter
    def EccAppid(self, EccAppid):
        self._EccAppid = EccAppid

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def ServerType(self):
        return self._ServerType

    @ServerType.setter
    def ServerType(self, ServerType):
        self._ServerType = ServerType

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Grade(self):
        return self._Grade

    @Grade.setter
    def Grade(self, Grade):
        self._Grade = Grade

    @property
    def Requirement(self):
        return self._Requirement

    @Requirement.setter
    def Requirement(self, Requirement):
        self._Requirement = Requirement

    @property
    def ModelTitle(self):
        return self._ModelTitle

    @ModelTitle.setter
    def ModelTitle(self, ModelTitle):
        self._ModelTitle = ModelTitle

    @property
    def ModelContent(self):
        return self._ModelContent

    @ModelContent.setter
    def ModelContent(self, ModelContent):
        self._ModelContent = ModelContent

    @property
    def IsAsync(self):
        return self._IsAsync

    @IsAsync.setter
    def IsAsync(self, IsAsync):
        self._IsAsync = IsAsync


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._InputType = params.get("InputType")
        self._EccAppid = params.get("EccAppid")
        self._SessionId = params.get("SessionId")
        self._ServerType = params.get("ServerType")
        self._Title = params.get("Title")
        self._Grade = params.get("Grade")
        self._Requirement = params.get("Requirement")
        self._ModelTitle = params.get("ModelTitle")
        self._ModelContent = params.get("ModelContent")
        self._IsAsync = params.get("IsAsync")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EHOCRResponse(AbstractModel):
    """EHOCR返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 接口返回数据
        :type Data: :class:`tencentcloud.ecc.v20181213.models.CompostionContext`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CompostionContext()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ErrorCoordinate(AbstractModel):
    """维度单词坐标

    """

    def __init__(self):
        r"""
        :param _Coordinate: 维度单词坐标
        :type Coordinate: list of int
        """
        self._Coordinate = None

    @property
    def Coordinate(self):
        return self._Coordinate

    @Coordinate.setter
    def Coordinate(self, Coordinate):
        self._Coordinate = Coordinate


    def _deserialize(self, params):
        self._Coordinate = params.get("Coordinate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreCategory(AbstractModel):
    """四个维度的得分

    """

    def __init__(self):
        r"""
        :param _Words: 词汇维度
        :type Words: :class:`tencentcloud.ecc.v20181213.models.Aspect`
        :param _Sentences: 句子维度
        :type Sentences: :class:`tencentcloud.ecc.v20181213.models.Aspect`
        :param _Structure: 篇章结构维度
        :type Structure: :class:`tencentcloud.ecc.v20181213.models.Aspect`
        :param _Content: 内容维度
        :type Content: :class:`tencentcloud.ecc.v20181213.models.Aspect`
        :param _Score: 维度得分
        :type Score: float
        :param _Percentage: 维度分数占比
        :type Percentage: float
        """
        self._Words = None
        self._Sentences = None
        self._Structure = None
        self._Content = None
        self._Score = None
        self._Percentage = None

    @property
    def Words(self):
        return self._Words

    @Words.setter
    def Words(self, Words):
        self._Words = Words

    @property
    def Sentences(self):
        return self._Sentences

    @Sentences.setter
    def Sentences(self, Sentences):
        self._Sentences = Sentences

    @property
    def Structure(self):
        return self._Structure

    @Structure.setter
    def Structure(self, Structure):
        self._Structure = Structure

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Percentage(self):
        return self._Percentage

    @Percentage.setter
    def Percentage(self, Percentage):
        self._Percentage = Percentage


    def _deserialize(self, params):
        if params.get("Words") is not None:
            self._Words = Aspect()
            self._Words._deserialize(params.get("Words"))
        if params.get("Sentences") is not None:
            self._Sentences = Aspect()
            self._Sentences._deserialize(params.get("Sentences"))
        if params.get("Structure") is not None:
            self._Structure = Aspect()
            self._Structure._deserialize(params.get("Structure"))
        if params.get("Content") is not None:
            self._Content = Aspect()
            self._Content._deserialize(params.get("Content"))
        self._Score = params.get("Score")
        self._Percentage = params.get("Percentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceCom(AbstractModel):
    """批改结果按句点评的详细信息

    """

    def __init__(self):
        r"""
        :param _Suggestions: 句子错误纠正信息
        :type Suggestions: list of SentenceSuggest
        :param _Sentence: 句子信息
        :type Sentence: :class:`tencentcloud.ecc.v20181213.models.SentenceItem`
        """
        self._Suggestions = None
        self._Sentence = None

    @property
    def Suggestions(self):
        return self._Suggestions

    @Suggestions.setter
    def Suggestions(self, Suggestions):
        self._Suggestions = Suggestions

    @property
    def Sentence(self):
        return self._Sentence

    @Sentence.setter
    def Sentence(self, Sentence):
        self._Sentence = Sentence


    def _deserialize(self, params):
        if params.get("Suggestions") is not None:
            self._Suggestions = []
            for item in params.get("Suggestions"):
                obj = SentenceSuggest()
                obj._deserialize(item)
                self._Suggestions.append(obj)
        if params.get("Sentence") is not None:
            self._Sentence = SentenceItem()
            self._Sentence._deserialize(params.get("Sentence"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceItem(AbstractModel):
    """句子的相关信息

    """

    def __init__(self):
        r"""
        :param _Sentence: 英语句子
        :type Sentence: str
        :param _ParaID: 段落id
        :type ParaID: int
        :param _SentenceID: 句子id
        :type SentenceID: int
        """
        self._Sentence = None
        self._ParaID = None
        self._SentenceID = None

    @property
    def Sentence(self):
        return self._Sentence

    @Sentence.setter
    def Sentence(self, Sentence):
        self._Sentence = Sentence

    @property
    def ParaID(self):
        return self._ParaID

    @ParaID.setter
    def ParaID(self, ParaID):
        self._ParaID = ParaID

    @property
    def SentenceID(self):
        return self._SentenceID

    @SentenceID.setter
    def SentenceID(self, SentenceID):
        self._SentenceID = SentenceID


    def _deserialize(self, params):
        self._Sentence = params.get("Sentence")
        self._ParaID = params.get("ParaID")
        self._SentenceID = params.get("SentenceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceSuggest(AbstractModel):
    """句子批阅建议

    """

    def __init__(self):
        r"""
        :param _Type: 类型
        :type Type: str
        :param _ErrorType: 错误类型
        :type ErrorType: str
        :param _Origin: 原始单词
        :type Origin: str
        :param _Replace: 替换成 的单词
        :type Replace: str
        :param _Message: 提示信息
        :type Message: str
        :param _ErrorPosition: 维度单词位置，在句子的第几个到第几个单词之间
        :type ErrorPosition: list of int
        :param _ErrorCoordinates: 维度单词坐标，错误单词在图片中的坐标，只有传图片时正常返回，传文字时返回[ ]
        :type ErrorCoordinates: list of ErrorCoordinate
        """
        self._Type = None
        self._ErrorType = None
        self._Origin = None
        self._Replace = None
        self._Message = None
        self._ErrorPosition = None
        self._ErrorCoordinates = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ErrorType(self):
        return self._ErrorType

    @ErrorType.setter
    def ErrorType(self, ErrorType):
        self._ErrorType = ErrorType

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def Replace(self):
        return self._Replace

    @Replace.setter
    def Replace(self, Replace):
        self._Replace = Replace

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ErrorPosition(self):
        return self._ErrorPosition

    @ErrorPosition.setter
    def ErrorPosition(self, ErrorPosition):
        self._ErrorPosition = ErrorPosition

    @property
    def ErrorCoordinates(self):
        return self._ErrorCoordinates

    @ErrorCoordinates.setter
    def ErrorCoordinates(self, ErrorCoordinates):
        self._ErrorCoordinates = ErrorCoordinates


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._ErrorType = params.get("ErrorType")
        self._Origin = params.get("Origin")
        self._Replace = params.get("Replace")
        self._Message = params.get("Message")
        self._ErrorPosition = params.get("ErrorPosition")
        if params.get("ErrorCoordinates") is not None:
            self._ErrorCoordinates = []
            for item in params.get("ErrorCoordinates"):
                obj = ErrorCoordinate()
                obj._deserialize(item)
                self._ErrorCoordinates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        