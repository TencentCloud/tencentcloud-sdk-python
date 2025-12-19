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


class AddChunkRequest(AbstractModel):
    r"""AddChunk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _FileId: 文件ID
        :type FileId: str
        :param _BeforeChunkId: 新增chunk的后面一个ChunkID。如果是空就是插到队尾。插入位置的下一个 chunkId。如果插到最前面，传入原切片的第一个。
        :type BeforeChunkId: str
        :param _InsertPos: 显式指定的位置,实际的位置。从 0 开始计算。0 代表插到最前面，chunk total 代表插到最后面。
        :type InsertPos: int
        :param _Content: chunk内容
        :type Content: str
        :param _AfterChunkId: 新 Chunk 插入到目标 Chunk ​之后的位置。插入位置的上一个 chunkId
        :type AfterChunkId: str
        """
        self._InstanceId = None
        self._FileId = None
        self._BeforeChunkId = None
        self._InsertPos = None
        self._Content = None
        self._AfterChunkId = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FileId(self):
        r"""文件ID
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def BeforeChunkId(self):
        r"""新增chunk的后面一个ChunkID。如果是空就是插到队尾。插入位置的下一个 chunkId。如果插到最前面，传入原切片的第一个。
        :rtype: str
        """
        return self._BeforeChunkId

    @BeforeChunkId.setter
    def BeforeChunkId(self, BeforeChunkId):
        self._BeforeChunkId = BeforeChunkId

    @property
    def InsertPos(self):
        r"""显式指定的位置,实际的位置。从 0 开始计算。0 代表插到最前面，chunk total 代表插到最后面。
        :rtype: int
        """
        return self._InsertPos

    @InsertPos.setter
    def InsertPos(self, InsertPos):
        self._InsertPos = InsertPos

    @property
    def Content(self):
        r"""chunk内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def AfterChunkId(self):
        r"""新 Chunk 插入到目标 Chunk ​之后的位置。插入位置的上一个 chunkId
        :rtype: str
        """
        return self._AfterChunkId

    @AfterChunkId.setter
    def AfterChunkId(self, AfterChunkId):
        self._AfterChunkId = AfterChunkId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FileId = params.get("FileId")
        self._BeforeChunkId = params.get("BeforeChunkId")
        self._InsertPos = params.get("InsertPos")
        self._Content = params.get("Content")
        self._AfterChunkId = params.get("AfterChunkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddChunkResponse(AbstractModel):
    r"""AddChunk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ChunkId: 新增的ChunkId
        :type ChunkId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ChunkId = None
        self._RequestId = None

    @property
    def ChunkId(self):
        r"""新增的ChunkId
        :rtype: str
        """
        return self._ChunkId

    @ChunkId.setter
    def ChunkId(self, ChunkId):
        self._ChunkId = ChunkId

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
        self._ChunkId = params.get("ChunkId")
        self._RequestId = params.get("RequestId")


class ChatAIRequest(AbstractModel):
    r"""ChatAI请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话ID
        :type SessionId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Question: 问题内容
        :type Question: str
        :param _Context: 上下文
        :type Context: str
        :param _Model: 模型
        :type Model: str
        :param _DeepThinking: 是否深度思考
        :type DeepThinking: bool
        :param _DataSourceIds: 数据源id
        :type DataSourceIds: list of str
        :param _AgentType: agent类型
        :type AgentType: str
        :param _OldRecordId: 需要重新生成答案的记录ID
        :type OldRecordId: str
        :param _KnowledgeBaseIds: 知识库id列表
        :type KnowledgeBaseIds: list of str
        """
        self._SessionId = None
        self._InstanceId = None
        self._Question = None
        self._Context = None
        self._Model = None
        self._DeepThinking = None
        self._DataSourceIds = None
        self._AgentType = None
        self._OldRecordId = None
        self._KnowledgeBaseIds = None

    @property
    def SessionId(self):
        r"""会话ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Question(self):
        r"""问题内容
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Context(self):
        r"""上下文
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Model(self):
        r"""模型
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def DeepThinking(self):
        r"""是否深度思考
        :rtype: bool
        """
        return self._DeepThinking

    @DeepThinking.setter
    def DeepThinking(self, DeepThinking):
        self._DeepThinking = DeepThinking

    @property
    def DataSourceIds(self):
        r"""数据源id
        :rtype: list of str
        """
        return self._DataSourceIds

    @DataSourceIds.setter
    def DataSourceIds(self, DataSourceIds):
        self._DataSourceIds = DataSourceIds

    @property
    def AgentType(self):
        r"""agent类型
        :rtype: str
        """
        return self._AgentType

    @AgentType.setter
    def AgentType(self, AgentType):
        self._AgentType = AgentType

    @property
    def OldRecordId(self):
        r"""需要重新生成答案的记录ID
        :rtype: str
        """
        return self._OldRecordId

    @OldRecordId.setter
    def OldRecordId(self, OldRecordId):
        self._OldRecordId = OldRecordId

    @property
    def KnowledgeBaseIds(self):
        r"""知识库id列表
        :rtype: list of str
        """
        return self._KnowledgeBaseIds

    @KnowledgeBaseIds.setter
    def KnowledgeBaseIds(self, KnowledgeBaseIds):
        self._KnowledgeBaseIds = KnowledgeBaseIds


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._InstanceId = params.get("InstanceId")
        self._Question = params.get("Question")
        self._Context = params.get("Context")
        self._Model = params.get("Model")
        self._DeepThinking = params.get("DeepThinking")
        self._DataSourceIds = params.get("DataSourceIds")
        self._AgentType = params.get("AgentType")
        self._OldRecordId = params.get("OldRecordId")
        self._KnowledgeBaseIds = params.get("KnowledgeBaseIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatAIResponse(AbstractModel):
    r"""ChatAI返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Chunk(AbstractModel):
    r"""文件分片

    """

    def __init__(self):
        r"""
        :param _Id: 切片ID
        :type Id: str
        :param _Content: 切片内容
        :type Content: str
        :param _Size: 切片的字数
        :type Size: int
        :param _Summary: 切片概要
        :type Summary: str
        """
        self._Id = None
        self._Content = None
        self._Size = None
        self._Summary = None

    @property
    def Id(self):
        r"""切片ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Content(self):
        r"""切片内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Size(self):
        r"""切片的字数
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Summary(self):
        r"""切片概要
        :rtype: str
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Content = params.get("Content")
        self._Size = params.get("Size")
        self._Summary = params.get("Summary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ColumnInfo(AbstractModel):
    r"""知识库文档表列信息

    """

    def __init__(self):
        r"""
        :param _Name: 列名称
        :type Name: str
        :param _Type: 列类型：int, bigint, double, date, datetime, string，decimal
        :type Type: str
        :param _Description: 列名称描述
        :type Description: str
        :param _Index: 列索引
        :type Index: int
        :param _OriginalName: 原始字段名称
        :type OriginalName: str
        """
        self._Name = None
        self._Type = None
        self._Description = None
        self._Index = None
        self._OriginalName = None

    @property
    def Name(self):
        r"""列名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""列类型：int, bigint, double, date, datetime, string，decimal
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Description(self):
        r"""列名称描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Index(self):
        r"""列索引
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def OriginalName(self):
        r"""原始字段名称
        :rtype: str
        """
        return self._OriginalName

    @OriginalName.setter
    def OriginalName(self, OriginalName):
        self._OriginalName = OriginalName


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Description = params.get("Description")
        self._Index = params.get("Index")
        self._OriginalName = params.get("OriginalName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosFileInfo(AbstractModel):
    r"""cos 文件信息

    """

    def __init__(self):
        r"""
        :param _FileName: 文件名称，包含后缀
        :type FileName: str
        :param _FileType: 文件类型，"PDF", "DOC", "DOCX", "XLS", "XLSX", "PPT", "PPTX", "MD", "TXT", "PNG", "JPG", "JPEG", "CSV"
        :type FileType: str
        :param _UserCosUrl: 用户文件的cosurl
        :type UserCosUrl: str
        """
        self._FileName = None
        self._FileType = None
        self._UserCosUrl = None

    @property
    def FileName(self):
        r"""文件名称，包含后缀
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        r"""文件类型，"PDF", "DOC", "DOCX", "XLS", "XLSX", "PPT", "PPTX", "MD", "TXT", "PNG", "JPG", "JPEG", "CSV"
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def UserCosUrl(self):
        r"""用户文件的cosurl
        :rtype: str
        """
        return self._UserCosUrl

    @UserCosUrl.setter
    def UserCosUrl(self, UserCosUrl):
        self._UserCosUrl = UserCosUrl


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._UserCosUrl = params.get("UserCosUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataAgentSessionRequest(AbstractModel):
    r"""CreateDataAgentSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataAgentSessionResponse(AbstractModel):
    r"""CreateDataAgentSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话
        :type SessionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionId = None
        self._RequestId = None

    @property
    def SessionId(self):
        r"""会话
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

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
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class DeleteChunkRequest(AbstractModel):
    r"""DeleteChunk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _FileId: 文件ID
        :type FileId: str
        :param _ChunkIds: 切片ID
        :type ChunkIds: list of str
        """
        self._InstanceId = None
        self._FileId = None
        self._ChunkIds = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FileId(self):
        r"""文件ID
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def ChunkIds(self):
        r"""切片ID
        :rtype: list of str
        """
        return self._ChunkIds

    @ChunkIds.setter
    def ChunkIds(self, ChunkIds):
        self._ChunkIds = ChunkIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FileId = params.get("FileId")
        self._ChunkIds = params.get("ChunkIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteChunkResponse(AbstractModel):
    r"""DeleteChunk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteDataAgentSessionRequest(AbstractModel):
    r"""DeleteDataAgentSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _SessionId: 会话ID
        :type SessionId: str
        """
        self._InstanceId = None
        self._SessionId = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SessionId(self):
        r"""会话ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDataAgentSessionResponse(AbstractModel):
    r"""DeleteDataAgentSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 删除的会话ID
        :type SessionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionId = None
        self._RequestId = None

    @property
    def SessionId(self):
        r"""删除的会话ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

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
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class FileInfo(AbstractModel):
    r"""知识库文件信息

    """

    def __init__(self):
        r"""
        :param _FileName: 文件名称
        :type FileName: str
        :param _FileSize: 文件大小，字节
        :type FileSize: float
        :param _Type: 文件类型,0=文本,1=表格，默认0

        :type Type: int
        :param _FileId: 文件ID
        :type FileId: str
        :param _Status: 状态，0：数据处理中  1：可用 -1：错误
        :type Status: int
        :param _CreateUser: 操作者

        :type CreateUser: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ChunkConfig: 分片策略
        :type ChunkConfig: :class:`tencentcloud.dataagent.v20250513.models.KnowledgeTaskConfig`
        :param _Source: 文件来源0=unknow,1=user_cos,2=local
        :type Source: int
        :param _FileUrl: 文件url
        :type FileUrl: str
        :param _IsShowCase: 是否官方示例，0=否，1=是
        :type IsShowCase: int
        :param _DocumentSummary: 文档摘要
        :type DocumentSummary: str
        """
        self._FileName = None
        self._FileSize = None
        self._Type = None
        self._FileId = None
        self._Status = None
        self._CreateUser = None
        self._CreateTime = None
        self._ChunkConfig = None
        self._Source = None
        self._FileUrl = None
        self._IsShowCase = None
        self._DocumentSummary = None

    @property
    def FileName(self):
        r"""文件名称
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        r"""文件大小，字节
        :rtype: float
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def Type(self):
        r"""文件类型,0=文本,1=表格，默认0

        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def FileId(self):
        r"""文件ID
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def Status(self):
        r"""状态，0：数据处理中  1：可用 -1：错误
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateUser(self):
        r"""操作者

        :rtype: str
        """
        return self._CreateUser

    @CreateUser.setter
    def CreateUser(self, CreateUser):
        self._CreateUser = CreateUser

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ChunkConfig(self):
        r"""分片策略
        :rtype: :class:`tencentcloud.dataagent.v20250513.models.KnowledgeTaskConfig`
        """
        return self._ChunkConfig

    @ChunkConfig.setter
    def ChunkConfig(self, ChunkConfig):
        self._ChunkConfig = ChunkConfig

    @property
    def Source(self):
        r"""文件来源0=unknow,1=user_cos,2=local
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def FileUrl(self):
        r"""文件url
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def IsShowCase(self):
        r"""是否官方示例，0=否，1=是
        :rtype: int
        """
        return self._IsShowCase

    @IsShowCase.setter
    def IsShowCase(self, IsShowCase):
        self._IsShowCase = IsShowCase

    @property
    def DocumentSummary(self):
        r"""文档摘要
        :rtype: str
        """
        return self._DocumentSummary

    @DocumentSummary.setter
    def DocumentSummary(self, DocumentSummary):
        self._DocumentSummary = DocumentSummary


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._Type = params.get("Type")
        self._FileId = params.get("FileId")
        self._Status = params.get("Status")
        self._CreateUser = params.get("CreateUser")
        self._CreateTime = params.get("CreateTime")
        if params.get("ChunkConfig") is not None:
            self._ChunkConfig = KnowledgeTaskConfig()
            self._ChunkConfig._deserialize(params.get("ChunkConfig"))
        self._Source = params.get("Source")
        self._FileUrl = params.get("FileUrl")
        self._IsShowCase = params.get("IsShowCase")
        self._DocumentSummary = params.get("DocumentSummary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetJobsByKnowledgeBaseIdRequest(AbstractModel):
    r"""GetJobsByKnowledgeBaseId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _KnowledgeBaseId: 知识库id
        :type KnowledgeBaseId: str
        """
        self._InstanceId = None
        self._KnowledgeBaseId = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def KnowledgeBaseId(self):
        r"""知识库id
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetJobsByKnowledgeBaseIdResponse(AbstractModel):
    r"""GetJobsByKnowledgeBaseId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Jobs: 任务列表详情
        :type Jobs: list of UploadJob
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Jobs = None
        self._RequestId = None

    @property
    def Jobs(self):
        r"""任务列表详情
        :rtype: list of UploadJob
        """
        return self._Jobs

    @Jobs.setter
    def Jobs(self, Jobs):
        self._Jobs = Jobs

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
        if params.get("Jobs") is not None:
            self._Jobs = []
            for item in params.get("Jobs"):
                obj = UploadJob()
                obj._deserialize(item)
                self._Jobs.append(obj)
        self._RequestId = params.get("RequestId")


class GetKnowledgeBaseFileListRequest(AbstractModel):
    r"""GetKnowledgeBaseFileList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Page: 默认 1 表示第一页，可以不填
        :type Page: int
        :param _PageSize: 默认 10 一页展示 10 条，可以不填
        :type PageSize: int
        :param _KnowledgeBaseId: 知识库id
        :type KnowledgeBaseId: str
        """
        self._InstanceId = None
        self._Page = None
        self._PageSize = None
        self._KnowledgeBaseId = None

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Page(self):
        r"""默认 1 表示第一页，可以不填
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        r"""默认 10 一页展示 10 条，可以不填
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def KnowledgeBaseId(self):
        r"""知识库id
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetKnowledgeBaseFileListResponse(AbstractModel):
    r"""GetKnowledgeBaseFileList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileList: 文件信息列表
        :type FileList: list of FileInfo
        :param _Total: 文件信息总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileList = None
        self._Total = None
        self._RequestId = None

    @property
    def FileList(self):
        r"""文件信息列表
        :rtype: list of FileInfo
        """
        return self._FileList

    @FileList.setter
    def FileList(self, FileList):
        self._FileList = FileList

    @property
    def Total(self):
        r"""文件信息总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("FileList") is not None:
            self._FileList = []
            for item in params.get("FileList"):
                obj = FileInfo()
                obj._deserialize(item)
                self._FileList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetKnowledgeBaseListRequest(AbstractModel):
    r"""GetKnowledgeBaseList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetKnowledgeBaseListResponse(AbstractModel):
    r"""GetKnowledgeBaseList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseList: 用户实例所有知识库列表
        :type KnowledgeBaseList: list of KnowledgeBase
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KnowledgeBaseList = None
        self._RequestId = None

    @property
    def KnowledgeBaseList(self):
        r"""用户实例所有知识库列表
        :rtype: list of KnowledgeBase
        """
        return self._KnowledgeBaseList

    @KnowledgeBaseList.setter
    def KnowledgeBaseList(self, KnowledgeBaseList):
        self._KnowledgeBaseList = KnowledgeBaseList

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
        if params.get("KnowledgeBaseList") is not None:
            self._KnowledgeBaseList = []
            for item in params.get("KnowledgeBaseList"):
                obj = KnowledgeBase()
                obj._deserialize(item)
                self._KnowledgeBaseList.append(obj)
        self._RequestId = params.get("RequestId")


class GetSessionDetailsRequest(AbstractModel):
    r"""GetSessionDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _SessionId: 会话ID
        :type SessionId: str
        """
        self._InstanceId = None
        self._SessionId = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SessionId(self):
        r"""会话ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSessionDetailsResponse(AbstractModel):
    r"""GetSessionDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordList: 会话记录详情
        :type RecordList: list of Record
        :param _RecordCount: 记录总数
        :type RecordCount: int
        :param _RunRecord: 当前在运行的record信息
        :type RunRecord: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordList = None
        self._RecordCount = None
        self._RunRecord = None
        self._RequestId = None

    @property
    def RecordList(self):
        r"""会话记录详情
        :rtype: list of Record
        """
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

    @property
    def RecordCount(self):
        r"""记录总数
        :rtype: int
        """
        return self._RecordCount

    @RecordCount.setter
    def RecordCount(self, RecordCount):
        self._RecordCount = RecordCount

    @property
    def RunRecord(self):
        r"""当前在运行的record信息
        :rtype: str
        """
        return self._RunRecord

    @RunRecord.setter
    def RunRecord(self, RunRecord):
        self._RunRecord = RunRecord

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
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = Record()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._RecordCount = params.get("RecordCount")
        self._RunRecord = params.get("RunRecord")
        self._RequestId = params.get("RequestId")


class GetUploadJobDetailsRequest(AbstractModel):
    r"""GetUploadJobDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _JobId: 任务id
        :type JobId: str
        """
        self._InstanceId = None
        self._JobId = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def JobId(self):
        r"""任务id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUploadJobDetailsResponse(AbstractModel):
    r"""GetUploadJobDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Job: 任务详情
        :type Job: :class:`tencentcloud.dataagent.v20250513.models.UploadJob`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Job = None
        self._RequestId = None

    @property
    def Job(self):
        r"""任务详情
        :rtype: :class:`tencentcloud.dataagent.v20250513.models.UploadJob`
        """
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

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
        if params.get("Job") is not None:
            self._Job = UploadJob()
            self._Job._deserialize(params.get("Job"))
        self._RequestId = params.get("RequestId")


class KnowledgeBase(AbstractModel):
    r"""知识库信息

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库id
        :type KnowledgeBaseId: str
        :param _KnowledgeBaseName: 知识库名称

        :type KnowledgeBaseName: str
        :param _KnowledgeBaseDesc: 知识库描述
        :type KnowledgeBaseDesc: str
        :param _Creator: 创建者subuin
        :type Creator: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _FileNum: 文件数量
        :type FileNum: int
        :param _DatasourceIds: 知识库关联的数据库列表，目前是只绑定一个数据源，数组预留拓展
        :type DatasourceIds: list of str
        """
        self._KnowledgeBaseId = None
        self._KnowledgeBaseName = None
        self._KnowledgeBaseDesc = None
        self._Creator = None
        self._CreateTime = None
        self._FileNum = None
        self._DatasourceIds = None

    @property
    def KnowledgeBaseId(self):
        r"""知识库id
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def KnowledgeBaseName(self):
        r"""知识库名称

        :rtype: str
        """
        return self._KnowledgeBaseName

    @KnowledgeBaseName.setter
    def KnowledgeBaseName(self, KnowledgeBaseName):
        self._KnowledgeBaseName = KnowledgeBaseName

    @property
    def KnowledgeBaseDesc(self):
        r"""知识库描述
        :rtype: str
        """
        return self._KnowledgeBaseDesc

    @KnowledgeBaseDesc.setter
    def KnowledgeBaseDesc(self, KnowledgeBaseDesc):
        self._KnowledgeBaseDesc = KnowledgeBaseDesc

    @property
    def Creator(self):
        r"""创建者subuin
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def FileNum(self):
        r"""文件数量
        :rtype: int
        """
        return self._FileNum

    @FileNum.setter
    def FileNum(self, FileNum):
        self._FileNum = FileNum

    @property
    def DatasourceIds(self):
        r"""知识库关联的数据库列表，目前是只绑定一个数据源，数组预留拓展
        :rtype: list of str
        """
        return self._DatasourceIds

    @DatasourceIds.setter
    def DatasourceIds(self, DatasourceIds):
        self._DatasourceIds = DatasourceIds


    def _deserialize(self, params):
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._KnowledgeBaseName = params.get("KnowledgeBaseName")
        self._KnowledgeBaseDesc = params.get("KnowledgeBaseDesc")
        self._Creator = params.get("Creator")
        self._CreateTime = params.get("CreateTime")
        self._FileNum = params.get("FileNum")
        self._DatasourceIds = params.get("DatasourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeTaskConfig(AbstractModel):
    r"""任务配置

    """

    def __init__(self):
        r"""
        :param _ChunkType: 切片类型  0:自定义切片，1：智能切片
        :type ChunkType: int
        :param _MaxChunkSize: /智能切片：最小值 1000，默认 4800 自定义切片：正整数即可,默认值 1000
        :type MaxChunkSize: int
        :param _Delimiters:  切片分隔符,自定义切片使用：默认值为：["\n\n", "\n", "。", "！", "？", "，", ""]
注意：此字段可能返回 null，表示取不到有效值。
        :type Delimiters: list of str
        :param _ChunkOverlap: 自定义切片使用:默认0 可重叠字符长度
        :type ChunkOverlap: int
        :param _Columns: 表格类文档解析
        :type Columns: list of ColumnInfo
        :param _Indexes: 带检索的索引列表
        :type Indexes: list of int
        :param _GenDocSummary: 0：不生成文档摘要，1：生成文档概要。默认0，当取1时，GenParaSummary必须也为1
        :type GenDocSummary: int
        :param _GenParaSummary: 0：不生成段落摘要，1：生成段落概要。默认0
        :type GenParaSummary: int
        """
        self._ChunkType = None
        self._MaxChunkSize = None
        self._Delimiters = None
        self._ChunkOverlap = None
        self._Columns = None
        self._Indexes = None
        self._GenDocSummary = None
        self._GenParaSummary = None

    @property
    def ChunkType(self):
        r"""切片类型  0:自定义切片，1：智能切片
        :rtype: int
        """
        return self._ChunkType

    @ChunkType.setter
    def ChunkType(self, ChunkType):
        self._ChunkType = ChunkType

    @property
    def MaxChunkSize(self):
        r"""/智能切片：最小值 1000，默认 4800 自定义切片：正整数即可,默认值 1000
        :rtype: int
        """
        return self._MaxChunkSize

    @MaxChunkSize.setter
    def MaxChunkSize(self, MaxChunkSize):
        self._MaxChunkSize = MaxChunkSize

    @property
    def Delimiters(self):
        r""" 切片分隔符,自定义切片使用：默认值为：["\n\n", "\n", "。", "！", "？", "，", ""]
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Delimiters

    @Delimiters.setter
    def Delimiters(self, Delimiters):
        self._Delimiters = Delimiters

    @property
    def ChunkOverlap(self):
        r"""自定义切片使用:默认0 可重叠字符长度
        :rtype: int
        """
        return self._ChunkOverlap

    @ChunkOverlap.setter
    def ChunkOverlap(self, ChunkOverlap):
        self._ChunkOverlap = ChunkOverlap

    @property
    def Columns(self):
        r"""表格类文档解析
        :rtype: list of ColumnInfo
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Indexes(self):
        r"""带检索的索引列表
        :rtype: list of int
        """
        return self._Indexes

    @Indexes.setter
    def Indexes(self, Indexes):
        self._Indexes = Indexes

    @property
    def GenDocSummary(self):
        r"""0：不生成文档摘要，1：生成文档概要。默认0，当取1时，GenParaSummary必须也为1
        :rtype: int
        """
        return self._GenDocSummary

    @GenDocSummary.setter
    def GenDocSummary(self, GenDocSummary):
        self._GenDocSummary = GenDocSummary

    @property
    def GenParaSummary(self):
        r"""0：不生成段落摘要，1：生成段落概要。默认0
        :rtype: int
        """
        return self._GenParaSummary

    @GenParaSummary.setter
    def GenParaSummary(self, GenParaSummary):
        self._GenParaSummary = GenParaSummary


    def _deserialize(self, params):
        self._ChunkType = params.get("ChunkType")
        self._MaxChunkSize = params.get("MaxChunkSize")
        self._Delimiters = params.get("Delimiters")
        self._ChunkOverlap = params.get("ChunkOverlap")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = ColumnInfo()
                obj._deserialize(item)
                self._Columns.append(obj)
        self._Indexes = params.get("Indexes")
        self._GenDocSummary = params.get("GenDocSummary")
        self._GenParaSummary = params.get("GenParaSummary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyChunkRequest(AbstractModel):
    r"""ModifyChunk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _FileId: 文件ID
        :type FileId: str
        :param _ChunkId: 切片ID
        :type ChunkId: str
        :param _Content: 编辑后的文本
        :type Content: str
        """
        self._InstanceId = None
        self._FileId = None
        self._ChunkId = None
        self._Content = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FileId(self):
        r"""文件ID
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def ChunkId(self):
        r"""切片ID
        :rtype: str
        """
        return self._ChunkId

    @ChunkId.setter
    def ChunkId(self, ChunkId):
        self._ChunkId = ChunkId

    @property
    def Content(self):
        r"""编辑后的文本
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FileId = params.get("FileId")
        self._ChunkId = params.get("ChunkId")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyChunkResponse(AbstractModel):
    r"""ModifyChunk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyKnowledgeBaseRequest(AbstractModel):
    r"""ModifyKnowledgeBase请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _OperateType: 操作类型：Create，Update，Delete
        :type OperateType: str
        :param _KnowledgeBaseId: 知识库id，update和delete时必填
        :type KnowledgeBaseId: str
        :param _KnowledgeBaseName: 知识库名称，create和update时必填。只允许字母、数字、汉字、下划线
        :type KnowledgeBaseName: str
        :param _KnowledgeBaseDesc: 知识库描述，create和update时必填
        :type KnowledgeBaseDesc: str
        """
        self._InstanceId = None
        self._OperateType = None
        self._KnowledgeBaseId = None
        self._KnowledgeBaseName = None
        self._KnowledgeBaseDesc = None

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OperateType(self):
        r"""操作类型：Create，Update，Delete
        :rtype: str
        """
        return self._OperateType

    @OperateType.setter
    def OperateType(self, OperateType):
        self._OperateType = OperateType

    @property
    def KnowledgeBaseId(self):
        r"""知识库id，update和delete时必填
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def KnowledgeBaseName(self):
        r"""知识库名称，create和update时必填。只允许字母、数字、汉字、下划线
        :rtype: str
        """
        return self._KnowledgeBaseName

    @KnowledgeBaseName.setter
    def KnowledgeBaseName(self, KnowledgeBaseName):
        self._KnowledgeBaseName = KnowledgeBaseName

    @property
    def KnowledgeBaseDesc(self):
        r"""知识库描述，create和update时必填
        :rtype: str
        """
        return self._KnowledgeBaseDesc

    @KnowledgeBaseDesc.setter
    def KnowledgeBaseDesc(self, KnowledgeBaseDesc):
        self._KnowledgeBaseDesc = KnowledgeBaseDesc


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OperateType = params.get("OperateType")
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._KnowledgeBaseName = params.get("KnowledgeBaseName")
        self._KnowledgeBaseDesc = params.get("KnowledgeBaseDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyKnowledgeBaseResponse(AbstractModel):
    r"""ModifyKnowledgeBase返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库id
        :type KnowledgeBaseId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KnowledgeBaseId = None
        self._RequestId = None

    @property
    def KnowledgeBaseId(self):
        r"""知识库id
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

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
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._RequestId = params.get("RequestId")


class QueryChunkListRequest(AbstractModel):
    r"""QueryChunkList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Page: 表示第一页
        :type Page: int
        :param _PageSize: 默认一页展示 10 条
        :type PageSize: int
        """
        self._Page = None
        self._PageSize = None

    @property
    def Page(self):
        r"""表示第一页
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        r"""默认一页展示 10 条
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryChunkListResponse(AbstractModel):
    r"""QueryChunkList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Chunks: 分片信息
        :type Chunks: list of Chunk
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Chunks = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Chunks(self):
        r"""分片信息
        :rtype: list of Chunk
        """
        return self._Chunks

    @Chunks.setter
    def Chunks(self, Chunks):
        self._Chunks = Chunks

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
        self._Total = params.get("Total")
        if params.get("Chunks") is not None:
            self._Chunks = []
            for item in params.get("Chunks"):
                obj = Chunk()
                obj._deserialize(item)
                self._Chunks.append(obj)
        self._RequestId = params.get("RequestId")


class Record(AbstractModel):
    r"""问答结构

    """

    def __init__(self):
        r"""
        :param _Question: 问题内容
        :type Question: str
        :param _Answer: 回答内容
        :type Answer: str
        :param _Think: 思考内容
        :type Think: str
        :param _TaskList: 任务列表
        :type TaskList: list of Task
        :param _CreateTime: 记录创建时间
        :type CreateTime: str
        :param _UpdateTime: 记录更新时间
        :type UpdateTime: str
        :param _RecordId: 记录id
        :type RecordId: str
        :param _FinalSummary: 总结内容
        :type FinalSummary: str
        :param _SessionId: 会话ID
        :type SessionId: str
        :param _Feedback: 1=赞，2=踩，0=无反馈
        :type Feedback: int
        :param _DbInfo: 数据库信息
        :type DbInfo: str
        :param _ErrorContext: 错误信息
        :type ErrorContext: str
        :param _TaskListStr: TaskList的string字符串
        :type TaskListStr: str
        :param _KnowledgeBaseIds: 知识库id列表
        :type KnowledgeBaseIds: list of str
        :param _Context: 上下文
        :type Context: str
        """
        self._Question = None
        self._Answer = None
        self._Think = None
        self._TaskList = None
        self._CreateTime = None
        self._UpdateTime = None
        self._RecordId = None
        self._FinalSummary = None
        self._SessionId = None
        self._Feedback = None
        self._DbInfo = None
        self._ErrorContext = None
        self._TaskListStr = None
        self._KnowledgeBaseIds = None
        self._Context = None

    @property
    def Question(self):
        r"""问题内容
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        r"""回答内容
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def Think(self):
        r"""思考内容
        :rtype: str
        """
        return self._Think

    @Think.setter
    def Think(self, Think):
        self._Think = Think

    @property
    def TaskList(self):
        r"""任务列表
        :rtype: list of Task
        """
        return self._TaskList

    @TaskList.setter
    def TaskList(self, TaskList):
        self._TaskList = TaskList

    @property
    def CreateTime(self):
        r"""记录创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""记录更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def RecordId(self):
        r"""记录id
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def FinalSummary(self):
        r"""总结内容
        :rtype: str
        """
        return self._FinalSummary

    @FinalSummary.setter
    def FinalSummary(self, FinalSummary):
        self._FinalSummary = FinalSummary

    @property
    def SessionId(self):
        r"""会话ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Feedback(self):
        r"""1=赞，2=踩，0=无反馈
        :rtype: int
        """
        return self._Feedback

    @Feedback.setter
    def Feedback(self, Feedback):
        self._Feedback = Feedback

    @property
    def DbInfo(self):
        r"""数据库信息
        :rtype: str
        """
        return self._DbInfo

    @DbInfo.setter
    def DbInfo(self, DbInfo):
        self._DbInfo = DbInfo

    @property
    def ErrorContext(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrorContext

    @ErrorContext.setter
    def ErrorContext(self, ErrorContext):
        self._ErrorContext = ErrorContext

    @property
    def TaskListStr(self):
        r"""TaskList的string字符串
        :rtype: str
        """
        return self._TaskListStr

    @TaskListStr.setter
    def TaskListStr(self, TaskListStr):
        self._TaskListStr = TaskListStr

    @property
    def KnowledgeBaseIds(self):
        r"""知识库id列表
        :rtype: list of str
        """
        return self._KnowledgeBaseIds

    @KnowledgeBaseIds.setter
    def KnowledgeBaseIds(self, KnowledgeBaseIds):
        self._KnowledgeBaseIds = KnowledgeBaseIds

    @property
    def Context(self):
        r"""上下文
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context


    def _deserialize(self, params):
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._Think = params.get("Think")
        if params.get("TaskList") is not None:
            self._TaskList = []
            for item in params.get("TaskList"):
                obj = Task()
                obj._deserialize(item)
                self._TaskList.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._RecordId = params.get("RecordId")
        self._FinalSummary = params.get("FinalSummary")
        self._SessionId = params.get("SessionId")
        self._Feedback = params.get("Feedback")
        self._DbInfo = params.get("DbInfo")
        self._ErrorContext = params.get("ErrorContext")
        self._TaskListStr = params.get("TaskListStr")
        self._KnowledgeBaseIds = params.get("KnowledgeBaseIds")
        self._Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StepExpand(AbstractModel):
    r"""步骤扩展结构

    """

    def __init__(self):
        r"""
        :param _Title: 标题
        :type Title: str
        :param _Status: 状态
        :type Status: str
        :param _CellIds: cellid数组
        :type CellIds: list of str
        """
        self._Title = None
        self._Status = None
        self._CellIds = None

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
    def Status(self):
        r"""状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CellIds(self):
        r"""cellid数组
        :rtype: list of str
        """
        return self._CellIds

    @CellIds.setter
    def CellIds(self, CellIds):
        self._CellIds = CellIds


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Status = params.get("Status")
        self._CellIds = params.get("CellIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StepInfo(AbstractModel):
    r"""任务步骤

    """

    def __init__(self):
        r"""
        :param _Id: 步骤id
        :type Id: int
        :param _Name: 步骤名称
        :type Name: str
        :param _Status: 步骤状态
        :type Status: str
        :param _Type: 类型(text/expand)
        :type Type: str
        :param _Summary: 总结
        :type Summary: str
        :param _Expand: 步骤扩展结构
        :type Expand: :class:`tencentcloud.dataagent.v20250513.models.StepExpand`
        :param _Desc: 描述
        :type Desc: str
        """
        self._Id = None
        self._Name = None
        self._Status = None
        self._Type = None
        self._Summary = None
        self._Expand = None
        self._Desc = None

    @property
    def Id(self):
        r"""步骤id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""步骤名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""步骤状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        r"""类型(text/expand)
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Summary(self):
        r"""总结
        :rtype: str
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def Expand(self):
        r"""步骤扩展结构
        :rtype: :class:`tencentcloud.dataagent.v20250513.models.StepExpand`
        """
        return self._Expand

    @Expand.setter
    def Expand(self, Expand):
        self._Expand = Expand

    @property
    def Desc(self):
        r"""描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._Summary = params.get("Summary")
        if params.get("Expand") is not None:
            self._Expand = StepExpand()
            self._Expand._deserialize(params.get("Expand"))
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopChatAIRequest(AbstractModel):
    r"""StopChatAI请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话ID
        :type SessionId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._SessionId = None
        self._InstanceId = None

    @property
    def SessionId(self):
        r"""会话ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopChatAIResponse(AbstractModel):
    r"""StopChatAI返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话
        :type SessionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionId = None
        self._RequestId = None

    @property
    def SessionId(self):
        r"""会话
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

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
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class Task(AbstractModel):
    r"""任务信息

    """

    def __init__(self):
        r"""
        :param _Id: 任务ID
        :type Id: int
        :param _Name: 任务名称
        :type Name: str
        :param _Status: 任务状态
        :type Status: str
        :param _StepInfoList: 任务步骤列表
        :type StepInfoList: list of StepInfo
        """
        self._Id = None
        self._Name = None
        self._Status = None
        self._StepInfoList = None

    @property
    def Id(self):
        r"""任务ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""任务状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StepInfoList(self):
        r"""任务步骤列表
        :rtype: list of StepInfo
        """
        return self._StepInfoList

    @StepInfoList.setter
    def StepInfoList(self, StepInfoList):
        self._StepInfoList = StepInfoList


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        if params.get("StepInfoList") is not None:
            self._StepInfoList = []
            for item in params.get("StepInfoList"):
                obj = StepInfo()
                obj._deserialize(item)
                self._StepInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadAndCommitFileRequest(AbstractModel):
    r"""UploadAndCommitFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _CosFiles: 上传文件列表
        :type CosFiles: list of CosFileInfo
        :param _KnowledgeBaseId: 知识库id
        :type KnowledgeBaseId: str
        """
        self._InstanceId = None
        self._CosFiles = None
        self._KnowledgeBaseId = None

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CosFiles(self):
        r"""上传文件列表
        :rtype: list of CosFileInfo
        """
        return self._CosFiles

    @CosFiles.setter
    def CosFiles(self, CosFiles):
        self._CosFiles = CosFiles

    @property
    def KnowledgeBaseId(self):
        r"""知识库id
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("CosFiles") is not None:
            self._CosFiles = []
            for item in params.get("CosFiles"):
                obj = CosFileInfo()
                obj._deserialize(item)
                self._CosFiles.append(obj)
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadAndCommitFileResponse(AbstractModel):
    r"""UploadAndCommitFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 上传任务
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""上传任务
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

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
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class UploadJob(AbstractModel):
    r"""上传任务

    """

    def __init__(self):
        r"""
        :param _Id: id
        :type Id: int
        :param _JobId: 任务id
        :type JobId: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _KnowledgeBaseId: 知识库id
        :type KnowledgeBaseId: str
        :param _Uin: uin
        :type Uin: str
        :param _SubUin: subuin
        :type SubUin: str
        :param _Status: Pending、FileUploading、
FileParsing、
Success、
Failed 
	
        :type Status: str
        :param _CreateTime: 任务创建时间
        :type CreateTime: str
        :param _UpdateTime: 任务更新时间
        :type UpdateTime: str
        :param _Message: 错误信息
        :type Message: str
        """
        self._Id = None
        self._JobId = None
        self._InstanceId = None
        self._KnowledgeBaseId = None
        self._Uin = None
        self._SubUin = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Message = None

    @property
    def Id(self):
        r"""id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def JobId(self):
        r"""任务id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def KnowledgeBaseId(self):
        r"""知识库id
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def Uin(self):
        r"""uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubUin(self):
        r"""subuin
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def Status(self):
        r"""Pending、FileUploading、
FileParsing、
Success、
Failed 
	
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""任务创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""任务更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Message(self):
        r"""错误信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._JobId = params.get("JobId")
        self._InstanceId = params.get("InstanceId")
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._Uin = params.get("Uin")
        self._SubUin = params.get("SubUin")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        