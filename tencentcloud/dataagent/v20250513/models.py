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
        :param _AfterChunkId: 	 新 Chunk 插入到目标 Chunk ​之后的位置。插入位置的上一个 chunkId
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
        r"""	 新 Chunk 插入到目标 Chunk ​之后的位置。插入位置的上一个 chunkId
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
        :param _ChunkId: 新增的chunkid
        :type ChunkId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ChunkId = None
        self._RequestId = None

    @property
    def ChunkId(self):
        r"""新增的chunkid
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


class CreateDataAgentSessionRequest(AbstractModel):
    r"""CreateDataAgentSession请求参数结构体

    """


class CreateDataAgentSessionResponse(AbstractModel):
    r"""CreateDataAgentSession返回参数结构体

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


class DeleteDataAgentSessionResponse(AbstractModel):
    r"""DeleteDataAgentSession返回参数结构体

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


class GetSessionDetailsResponse(AbstractModel):
    r"""GetSessionDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordCount: 记录总数
        :type RecordCount: int
        :param _RunRecord: 当前在运行的record信息
        :type RunRecord: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordCount = None
        self._RunRecord = None
        self._RequestId = None

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
        self._RecordCount = params.get("RecordCount")
        self._RunRecord = params.get("RunRecord")
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
        :param _Page: 默认 1 表示第一页
        :type Page: int
        :param _PageSize: 	 默认 10 一页展示 10 条
        :type PageSize: int
        """
        self._Page = None
        self._PageSize = None

    @property
    def Page(self):
        r"""默认 1 表示第一页
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        r"""	 默认 10 一页展示 10 条
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


class StopChatAIRequest(AbstractModel):
    r"""StopChatAI请求参数结构体

    """


class StopChatAIResponse(AbstractModel):
    r"""StopChatAI返回参数结构体

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