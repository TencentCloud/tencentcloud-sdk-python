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


class ChatCompletionsRequest(AbstractModel):
    r"""ChatCompletions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Messages: 会话内容，按对话时间从旧到新在数组中排列，长度受模型窗口大小限制。
        :type Messages: list of Message
        :param _ModelName: 模型名称，可选模型列表：hunyuan-turbo，hunyuan-large，hunyuan-large-longcontext，hunyuan-standard，hunyuan-standard-256K，deepseek-r1，deepseek-v3，deepseek-r1-distill-qwen-32b。
        :type ModelName: str
        :param _Stream: 是否以流式接口的形式返回数据，默认true。
        :type Stream: bool
        :param _TopP: 取值区间为[0.0, 1.0], 非必要不建议使用, 不合理的取值会影响效果 。
        :type TopP: float
        :param _Temperature: 取值区间为[0.0, 2.0], 非必要不建议使用, 不合理的取值会影响效果 。
        :type Temperature: float
        :param _OnlineSearch: 是否开启联网搜索。默认为 false。
        :type OnlineSearch: bool
        :param _OnlineSearchOptions: 当 OnlineSearch 为 true 时，指定的搜索引擎，默认为 bing。
        :type OnlineSearchOptions: :class:`tencentcloud.es.v20250101.models.OnlineSearchOptions`
        :param _Tools: 可调用的工具列表，当前支持模型：hunyuan-turbo, deepseek-v3。
        :type Tools: list of Tool
        :param _ToolChoice: 工具使用选项，可选值包括 none、auto、custom。说明：1. 仅对 hunyuan-turbo、deepseek-v3 模型生效。2. none：不调用工具；auto：模型自行选择生成回复或调用工具；custom：强制模型调用指定的工具。3. 未设置时，默认值为auto
        :type ToolChoice: str
        :param _CustomTool: 强制模型调用指定的工具，当参数ToolChoice为custom时，此参数为必填
        :type CustomTool: :class:`tencentcloud.es.v20250101.models.Tool`
        """
        self._Messages = None
        self._ModelName = None
        self._Stream = None
        self._TopP = None
        self._Temperature = None
        self._OnlineSearch = None
        self._OnlineSearchOptions = None
        self._Tools = None
        self._ToolChoice = None
        self._CustomTool = None

    @property
    def Messages(self):
        r"""会话内容，按对话时间从旧到新在数组中排列，长度受模型窗口大小限制。
        :rtype: list of Message
        """
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def ModelName(self):
        r"""模型名称，可选模型列表：hunyuan-turbo，hunyuan-large，hunyuan-large-longcontext，hunyuan-standard，hunyuan-standard-256K，deepseek-r1，deepseek-v3，deepseek-r1-distill-qwen-32b。
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def Stream(self):
        r"""是否以流式接口的形式返回数据，默认true。
        :rtype: bool
        """
        return self._Stream

    @Stream.setter
    def Stream(self, Stream):
        self._Stream = Stream

    @property
    def TopP(self):
        r"""取值区间为[0.0, 1.0], 非必要不建议使用, 不合理的取值会影响效果 。
        :rtype: float
        """
        return self._TopP

    @TopP.setter
    def TopP(self, TopP):
        self._TopP = TopP

    @property
    def Temperature(self):
        r"""取值区间为[0.0, 2.0], 非必要不建议使用, 不合理的取值会影响效果 。
        :rtype: float
        """
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def OnlineSearch(self):
        r"""是否开启联网搜索。默认为 false。
        :rtype: bool
        """
        return self._OnlineSearch

    @OnlineSearch.setter
    def OnlineSearch(self, OnlineSearch):
        self._OnlineSearch = OnlineSearch

    @property
    def OnlineSearchOptions(self):
        r"""当 OnlineSearch 为 true 时，指定的搜索引擎，默认为 bing。
        :rtype: :class:`tencentcloud.es.v20250101.models.OnlineSearchOptions`
        """
        return self._OnlineSearchOptions

    @OnlineSearchOptions.setter
    def OnlineSearchOptions(self, OnlineSearchOptions):
        self._OnlineSearchOptions = OnlineSearchOptions

    @property
    def Tools(self):
        r"""可调用的工具列表，当前支持模型：hunyuan-turbo, deepseek-v3。
        :rtype: list of Tool
        """
        return self._Tools

    @Tools.setter
    def Tools(self, Tools):
        self._Tools = Tools

    @property
    def ToolChoice(self):
        r"""工具使用选项，可选值包括 none、auto、custom。说明：1. 仅对 hunyuan-turbo、deepseek-v3 模型生效。2. none：不调用工具；auto：模型自行选择生成回复或调用工具；custom：强制模型调用指定的工具。3. 未设置时，默认值为auto
        :rtype: str
        """
        return self._ToolChoice

    @ToolChoice.setter
    def ToolChoice(self, ToolChoice):
        self._ToolChoice = ToolChoice

    @property
    def CustomTool(self):
        r"""强制模型调用指定的工具，当参数ToolChoice为custom时，此参数为必填
        :rtype: :class:`tencentcloud.es.v20250101.models.Tool`
        """
        return self._CustomTool

    @CustomTool.setter
    def CustomTool(self, CustomTool):
        self._CustomTool = CustomTool


    def _deserialize(self, params):
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = Message()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._ModelName = params.get("ModelName")
        self._Stream = params.get("Stream")
        self._TopP = params.get("TopP")
        self._Temperature = params.get("Temperature")
        self._OnlineSearch = params.get("OnlineSearch")
        if params.get("OnlineSearchOptions") is not None:
            self._OnlineSearchOptions = OnlineSearchOptions()
            self._OnlineSearchOptions._deserialize(params.get("OnlineSearchOptions"))
        if params.get("Tools") is not None:
            self._Tools = []
            for item in params.get("Tools"):
                obj = Tool()
                obj._deserialize(item)
                self._Tools.append(obj)
        self._ToolChoice = params.get("ToolChoice")
        if params.get("CustomTool") is not None:
            self._CustomTool = Tool()
            self._CustomTool._deserialize(params.get("CustomTool"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatCompletionsResponse(AbstractModel):
    r"""ChatCompletions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 此次请求的id
        :type Id: str
        :param _Choices: 回复内容
        :type Choices: list of Choice
        :param _Usage: token使用量
        :type Usage: :class:`tencentcloud.es.v20250101.models.TokenUsage`
        :param _OnlineSearchContent: 联网搜索结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type OnlineSearchContent: list of WebContent
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._Id = None
        self._Choices = None
        self._Usage = None
        self._OnlineSearchContent = None
        self._RequestId = None

    @property
    def Id(self):
        r"""此次请求的id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Choices(self):
        r"""回复内容
        :rtype: list of Choice
        """
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices

    @property
    def Usage(self):
        r"""token使用量
        :rtype: :class:`tencentcloud.es.v20250101.models.TokenUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def OnlineSearchContent(self):
        r"""联网搜索结果。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WebContent
        """
        return self._OnlineSearchContent

    @OnlineSearchContent.setter
    def OnlineSearchContent(self, OnlineSearchContent):
        self._OnlineSearchContent = OnlineSearchContent

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
        self._Id = params.get("Id")
        if params.get("Choices") is not None:
            self._Choices = []
            for item in params.get("Choices"):
                obj = Choice()
                obj._deserialize(item)
                self._Choices.append(obj)
        if params.get("Usage") is not None:
            self._Usage = TokenUsage()
            self._Usage._deserialize(params.get("Usage"))
        if params.get("OnlineSearchContent") is not None:
            self._OnlineSearchContent = []
            for item in params.get("OnlineSearchContent"):
                obj = WebContent()
                obj._deserialize(item)
                self._OnlineSearchContent.append(obj)
        self._RequestId = params.get("RequestId")


class Choice(AbstractModel):
    r"""返回的回复, 支持多个。

    """

    def __init__(self):
        r"""
        :param _Message: 返回的回复。
        :type Message: :class:`tencentcloud.es.v20250101.models.OutputMessage`
        """
        self._Message = None

    @property
    def Message(self):
        r"""返回的回复。
        :rtype: :class:`tencentcloud.es.v20250101.models.OutputMessage`
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        if params.get("Message") is not None:
            self._Message = OutputMessage()
            self._Message._deserialize(params.get("Message"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Chunk(AbstractModel):
    r"""切片对象信息

    """

    def __init__(self):
        r"""
        :param _Index: chunk索引。切片顺序 id。
        :type Index: int
        :param _Content: chunk内容。
        :type Content: str
        """
        self._Index = None
        self._Content = None

    @property
    def Index(self):
        r"""chunk索引。切片顺序 id。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Content(self):
        r"""chunk内容。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChunkConfig(AbstractModel):
    r"""文档分片配置

    """

    def __init__(self):
        r"""
        :param _MaxChunkSize: 最大分片长度
        :type MaxChunkSize: int
        :param _Delimiters: 分隔符列表
        :type Delimiters: list of str
        :param _ChunkOverlap: 相邻切片重合字符数，需要小于分片长度
        :type ChunkOverlap: int
        """
        self._MaxChunkSize = None
        self._Delimiters = None
        self._ChunkOverlap = None

    @property
    def MaxChunkSize(self):
        r"""最大分片长度
        :rtype: int
        """
        return self._MaxChunkSize

    @MaxChunkSize.setter
    def MaxChunkSize(self, MaxChunkSize):
        self._MaxChunkSize = MaxChunkSize

    @property
    def Delimiters(self):
        r"""分隔符列表
        :rtype: list of str
        """
        return self._Delimiters

    @Delimiters.setter
    def Delimiters(self, Delimiters):
        self._Delimiters = Delimiters

    @property
    def ChunkOverlap(self):
        r"""相邻切片重合字符数，需要小于分片长度
        :rtype: int
        """
        return self._ChunkOverlap

    @ChunkOverlap.setter
    def ChunkOverlap(self, ChunkOverlap):
        self._ChunkOverlap = ChunkOverlap


    def _deserialize(self, params):
        self._MaxChunkSize = params.get("MaxChunkSize")
        self._Delimiters = params.get("Delimiters")
        self._ChunkOverlap = params.get("ChunkOverlap")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChunkConfigAsync(AbstractModel):
    r"""文档切片异步任务

    """

    def __init__(self):
        r"""
        :param _MaxChunkSize: 最大分片长度
        :type MaxChunkSize: int
        """
        self._MaxChunkSize = None

    @property
    def MaxChunkSize(self):
        r"""最大分片长度
        :rtype: int
        """
        return self._MaxChunkSize

    @MaxChunkSize.setter
    def MaxChunkSize(self, MaxChunkSize):
        self._MaxChunkSize = MaxChunkSize


    def _deserialize(self, params):
        self._MaxChunkSize = params.get("MaxChunkSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChunkDocument(AbstractModel):
    r"""切片文档信息

    """

    def __init__(self):
        r"""
        :param _FileType: 文件类型，支持 MD，TXT 格式。
        :type FileType: str
        :param _FileContent: 文本原文，使用字符串格式输入。
        :type FileContent: str
        """
        self._FileType = None
        self._FileContent = None

    @property
    def FileType(self):
        r"""文件类型，支持 MD，TXT 格式。
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileContent(self):
        r"""文本原文，使用字符串格式输入。
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileContent = params.get("FileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChunkDocumentAsyncRequest(AbstractModel):
    r"""ChunkDocumentAsync请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Document: 文件信息。
        :type Document: :class:`tencentcloud.es.v20250101.models.Document`
        :param _ModelName: 模型名称，可选模型列表：doc-tree-chunk。
        :type ModelName: str
        :param _Config: 文件切片配置。
        :type Config: :class:`tencentcloud.es.v20250101.models.ChunkConfigAsync`
        """
        self._Document = None
        self._ModelName = None
        self._Config = None

    @property
    def Document(self):
        r"""文件信息。
        :rtype: :class:`tencentcloud.es.v20250101.models.Document`
        """
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document

    @property
    def ModelName(self):
        r"""模型名称，可选模型列表：doc-tree-chunk。
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def Config(self):
        r"""文件切片配置。
        :rtype: :class:`tencentcloud.es.v20250101.models.ChunkConfigAsync`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        if params.get("Document") is not None:
            self._Document = Document()
            self._Document._deserialize(params.get("Document"))
        self._ModelName = params.get("ModelName")
        if params.get("Config") is not None:
            self._Config = ChunkConfigAsync()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChunkDocumentAsyncResponse(AbstractModel):
    r"""ChunkDocumentAsync返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ChunkDocumentRequest(AbstractModel):
    r"""ChunkDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Document: 切片文件信息。
        :type Document: :class:`tencentcloud.es.v20250101.models.ChunkDocument`
        :param _ModelName: 模型名称，可选模型列表：doc-chunk。
        :type ModelName: str
        :param _Config: 文件切片配置。
        :type Config: :class:`tencentcloud.es.v20250101.models.ChunkConfig`
        """
        self._Document = None
        self._ModelName = None
        self._Config = None

    @property
    def Document(self):
        r"""切片文件信息。
        :rtype: :class:`tencentcloud.es.v20250101.models.ChunkDocument`
        """
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document

    @property
    def ModelName(self):
        r"""模型名称，可选模型列表：doc-chunk。
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def Config(self):
        r"""文件切片配置。
        :rtype: :class:`tencentcloud.es.v20250101.models.ChunkConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        if params.get("Document") is not None:
            self._Document = ChunkDocument()
            self._Document._deserialize(params.get("Document"))
        self._ModelName = params.get("ModelName")
        if params.get("Config") is not None:
            self._Config = ChunkConfig()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChunkDocumentResponse(AbstractModel):
    r"""ChunkDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Chunks: 无
        :type Chunks: list of Chunk
        :param _Usage: token消耗量
        :type Usage: :class:`tencentcloud.es.v20250101.models.Usage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Chunks = None
        self._Usage = None
        self._RequestId = None

    @property
    def Chunks(self):
        r"""无
        :rtype: list of Chunk
        """
        return self._Chunks

    @Chunks.setter
    def Chunks(self, Chunks):
        self._Chunks = Chunks

    @property
    def Usage(self):
        r"""token消耗量
        :rtype: :class:`tencentcloud.es.v20250101.models.Usage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
        if params.get("Chunks") is not None:
            self._Chunks = []
            for item in params.get("Chunks"):
                obj = Chunk()
                obj._deserialize(item)
                self._Chunks.append(obj)
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class Document(AbstractModel):
    r"""文档信息

    """

    def __init__(self):
        r"""
        :param _FileType: 支持的文件类型：PDF、DOC、DOCX、PPT、PPTX、MD、TXT、XLS、
XLSX、CSV、PNG、JPG、JPEG、BMP、GIF、WEBP、HEIC、EPS、ICNS、
IM、PCX、PPM、TIFF、XBM、HEIF、JP2

文档解析支持的文件大小：
-PDF、DOC、DOCX、PPT、PPTX支持100M
-MD、TXT、XLS、XLSX、CSV支特10M
-其他支持20M

文本切片支持的文件大小：
-PDF最大300M
-D0CX、D0C、PPT、PPTX最大200M
-TXT、MD最大10M
-其他最大20M
        :type FileType: str
        :param _FileUrl: 文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，使用腾讯云COS 文件地址。
        :type FileUrl: str
        :param _FileContent: 文件的 base64 值，携带 MineType前缀信息。编码后的后的文件不超过 10M。
支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过3秒。
支持的图片像素：单边介于20-10000px之间。
        :type FileContent: str
        :param _FileName: 文件名称，当使用 base64上传的时候使用。
        :type FileName: str
        :param _FileStartPageNumber: 文档的起始页码
        :type FileStartPageNumber: int
        :param _FileEndPageNumber: 文档的结束页码
        :type FileEndPageNumber: int
        """
        self._FileType = None
        self._FileUrl = None
        self._FileContent = None
        self._FileName = None
        self._FileStartPageNumber = None
        self._FileEndPageNumber = None

    @property
    def FileType(self):
        r"""支持的文件类型：PDF、DOC、DOCX、PPT、PPTX、MD、TXT、XLS、
XLSX、CSV、PNG、JPG、JPEG、BMP、GIF、WEBP、HEIC、EPS、ICNS、
IM、PCX、PPM、TIFF、XBM、HEIF、JP2

文档解析支持的文件大小：
-PDF、DOC、DOCX、PPT、PPTX支持100M
-MD、TXT、XLS、XLSX、CSV支特10M
-其他支持20M

文本切片支持的文件大小：
-PDF最大300M
-D0CX、D0C、PPT、PPTX最大200M
-TXT、MD最大10M
-其他最大20M
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileUrl(self):
        r"""文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，使用腾讯云COS 文件地址。
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileContent(self):
        r"""文件的 base64 值，携带 MineType前缀信息。编码后的后的文件不超过 10M。
支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过3秒。
支持的图片像素：单边介于20-10000px之间。
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileName(self):
        r"""文件名称，当使用 base64上传的时候使用。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileStartPageNumber(self):
        r"""文档的起始页码
        :rtype: int
        """
        return self._FileStartPageNumber

    @FileStartPageNumber.setter
    def FileStartPageNumber(self, FileStartPageNumber):
        self._FileStartPageNumber = FileStartPageNumber

    @property
    def FileEndPageNumber(self):
        r"""文档的结束页码
        :rtype: int
        """
        return self._FileEndPageNumber

    @FileEndPageNumber.setter
    def FileEndPageNumber(self, FileEndPageNumber):
        self._FileEndPageNumber = FileEndPageNumber


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileUrl = params.get("FileUrl")
        self._FileContent = params.get("FileContent")
        self._FileName = params.get("FileName")
        self._FileStartPageNumber = params.get("FileStartPageNumber")
        self._FileEndPageNumber = params.get("FileEndPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DocumentChunkUsage(AbstractModel):
    r"""文档切片用量

    """

    def __init__(self):
        r"""
        :param _PageNumber:  解析页面数量
        :type PageNumber: int
        :param _TotalTokens: 消耗 token数量
        :type TotalTokens: int
        """
        self._PageNumber = None
        self._TotalTokens = None

    @property
    def PageNumber(self):
        r""" 解析页面数量
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def TotalTokens(self):
        r"""消耗 token数量
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DocumentParseConfig(AbstractModel):
    r"""文档解析配置

    """

    def __init__(self):
        r"""
        :param _ImageResponseType: 0:图片以链接形式返回
1:返回图片中提取的文本内容
        :type ImageResponseType: int
        """
        self._ImageResponseType = None

    @property
    def ImageResponseType(self):
        r"""0:图片以链接形式返回
1:返回图片中提取的文本内容
        :rtype: int
        """
        return self._ImageResponseType

    @ImageResponseType.setter
    def ImageResponseType(self, ImageResponseType):
        self._ImageResponseType = ImageResponseType


    def _deserialize(self, params):
        self._ImageResponseType = params.get("ImageResponseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmbeddingData(AbstractModel):
    r"""向量内容

    """

    def __init__(self):
        r"""
        :param _Embedding: embedding 内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Embedding: list of float
        :param _Index: 索引序号
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: int
        """
        self._Embedding = None
        self._Index = None

    @property
    def Embedding(self):
        r"""embedding 内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of float
        """
        return self._Embedding

    @Embedding.setter
    def Embedding(self, Embedding):
        self._Embedding = Embedding

    @property
    def Index(self):
        r"""索引序号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._Embedding = params.get("Embedding")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDocumentChunkResultRequest(AbstractModel):
    r"""GetDocumentChunkResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId:  任务 ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r""" 任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDocumentChunkResultResponse(AbstractModel):
    r"""GetDocumentChunkResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态，-1：失败，0：运行中，1：成功。
        :type Status: int
        :param _DocumentChunkResultUrl: 切片结果文件。
        :type DocumentChunkResultUrl: str
        :param _Usage: Token用量。
        :type Usage: :class:`tencentcloud.es.v20250101.models.DocumentChunkUsage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._DocumentChunkResultUrl = None
        self._Usage = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态，-1：失败，0：运行中，1：成功。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DocumentChunkResultUrl(self):
        r"""切片结果文件。
        :rtype: str
        """
        return self._DocumentChunkResultUrl

    @DocumentChunkResultUrl.setter
    def DocumentChunkResultUrl(self, DocumentChunkResultUrl):
        self._DocumentChunkResultUrl = DocumentChunkResultUrl

    @property
    def Usage(self):
        r"""Token用量。
        :rtype: :class:`tencentcloud.es.v20250101.models.DocumentChunkUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
        self._Status = params.get("Status")
        self._DocumentChunkResultUrl = params.get("DocumentChunkResultUrl")
        if params.get("Usage") is not None:
            self._Usage = DocumentChunkUsage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class GetDocumentParseResultRequest(AbstractModel):
    r"""GetDocumentParseResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 Id
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""任务 Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDocumentParseResultResponse(AbstractModel):
    r"""GetDocumentParseResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态，-1：失败，0：运行中，1：成功。
        :type Status: int
        :param _DocumentParseResultUrl: 结果文件。
        :type DocumentParseResultUrl: str
        :param _FailedPages: 失败的页码。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedPages: list of int
        :param _Usage: 消耗页数
        :type Usage: :class:`tencentcloud.es.v20250101.models.PageUsage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._DocumentParseResultUrl = None
        self._FailedPages = None
        self._Usage = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态，-1：失败，0：运行中，1：成功。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DocumentParseResultUrl(self):
        r"""结果文件。
        :rtype: str
        """
        return self._DocumentParseResultUrl

    @DocumentParseResultUrl.setter
    def DocumentParseResultUrl(self, DocumentParseResultUrl):
        self._DocumentParseResultUrl = DocumentParseResultUrl

    @property
    def FailedPages(self):
        r"""失败的页码。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._FailedPages

    @FailedPages.setter
    def FailedPages(self, FailedPages):
        self._FailedPages = FailedPages

    @property
    def Usage(self):
        r"""消耗页数
        :rtype: :class:`tencentcloud.es.v20250101.models.PageUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
        self._Status = params.get("Status")
        self._DocumentParseResultUrl = params.get("DocumentParseResultUrl")
        self._FailedPages = params.get("FailedPages")
        if params.get("Usage") is not None:
            self._Usage = PageUsage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class GetMultiModalEmbeddingRequest(AbstractModel):
    r"""GetMultiModalEmbedding请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelName: 模型名称，支持WeCLIPv2-Base和WeCLIPv2-Large
        :type ModelName: str
        :param _Texts: 需进行向量化的文本集，一次输入限10条，单条文本长度限72
        :type Texts: list of str
        :param _ImageData: 输入图片，base64编码格式，一次输入限制8个，单张图片限制1M
        :type ImageData: list of str
        :param _ImageUrl: 输入图片url，一次输入限8个，推荐cos地址，速度更快
        :type ImageUrl: list of str
        """
        self._ModelName = None
        self._Texts = None
        self._ImageData = None
        self._ImageUrl = None

    @property
    def ModelName(self):
        r"""模型名称，支持WeCLIPv2-Base和WeCLIPv2-Large
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def Texts(self):
        r"""需进行向量化的文本集，一次输入限10条，单条文本长度限72
        :rtype: list of str
        """
        return self._Texts

    @Texts.setter
    def Texts(self, Texts):
        self._Texts = Texts

    @property
    def ImageData(self):
        r"""输入图片，base64编码格式，一次输入限制8个，单张图片限制1M
        :rtype: list of str
        """
        return self._ImageData

    @ImageData.setter
    def ImageData(self, ImageData):
        self._ImageData = ImageData

    @property
    def ImageUrl(self):
        r"""输入图片url，一次输入限8个，推荐cos地址，速度更快
        :rtype: list of str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._Texts = params.get("Texts")
        self._ImageData = params.get("ImageData")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMultiModalEmbeddingResponse(AbstractModel):
    r"""GetMultiModalEmbedding返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 多模态特征向量输出
        :type Data: :class:`tencentcloud.es.v20250101.models.MultiModalEmbeddingData`
        :param _Usage: 消耗的tokens和输入图片数量
        :type Usage: :class:`tencentcloud.es.v20250101.models.MultiModalUsage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Usage = None
        self._RequestId = None

    @property
    def Data(self):
        r"""多模态特征向量输出
        :rtype: :class:`tencentcloud.es.v20250101.models.MultiModalEmbeddingData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Usage(self):
        r"""消耗的tokens和输入图片数量
        :rtype: :class:`tencentcloud.es.v20250101.models.MultiModalUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
        if params.get("Data") is not None:
            self._Data = MultiModalEmbeddingData()
            self._Data._deserialize(params.get("Data"))
        if params.get("Usage") is not None:
            self._Usage = MultiModalUsage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class GetTextEmbeddingRequest(AbstractModel):
    r"""GetTextEmbedding请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelName: 模型名称，可选模型列表：bge-base-zh-v1.5,Conan-embedding-v1,bge-m3,KaLM-embedding-multilingual-mini-v1,Qwen3-Embedding-0.6B。
        :type ModelName: str
        :param _Texts: 需进行向量化的文本集。
        :type Texts: list of str
        """
        self._ModelName = None
        self._Texts = None

    @property
    def ModelName(self):
        r"""模型名称，可选模型列表：bge-base-zh-v1.5,Conan-embedding-v1,bge-m3,KaLM-embedding-multilingual-mini-v1,Qwen3-Embedding-0.6B。
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def Texts(self):
        r"""需进行向量化的文本集。
        :rtype: list of str
        """
        return self._Texts

    @Texts.setter
    def Texts(self, Texts):
        self._Texts = Texts


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._Texts = params.get("Texts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTextEmbeddingResponse(AbstractModel):
    r"""GetTextEmbedding返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果集
        :type Data: list of EmbeddingData
        :param _Usage: 向量化消耗的token数量。
        :type Usage: :class:`tencentcloud.es.v20250101.models.Usage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Usage = None
        self._RequestId = None

    @property
    def Data(self):
        r"""结果集
        :rtype: list of EmbeddingData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Usage(self):
        r"""向量化消耗的token数量。
        :rtype: :class:`tencentcloud.es.v20250101.models.Usage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = EmbeddingData()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class Message(AbstractModel):
    r"""会话内容，按对话时间从旧到新在数组中排列，长度受模型窗口大小限制。

    """

    def __init__(self):
        r"""
        :param _Role: 角色，可选值包括 system、user、assistant、 tool。
        :type Role: str
        :param _Content: 具体文本内容
        :type Content: str
        :param _ToolCallId: 当role为tool时传入，标识具体的函数调用
        :type ToolCallId: str
        :param _ToolCalls: 模型生成的工具调用
        :type ToolCalls: list of ToolCall
        """
        self._Role = None
        self._Content = None
        self._ToolCallId = None
        self._ToolCalls = None

    @property
    def Role(self):
        r"""角色，可选值包括 system、user、assistant、 tool。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        r"""具体文本内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ToolCallId(self):
        r"""当role为tool时传入，标识具体的函数调用
        :rtype: str
        """
        return self._ToolCallId

    @ToolCallId.setter
    def ToolCallId(self, ToolCallId):
        self._ToolCallId = ToolCallId

    @property
    def ToolCalls(self):
        r"""模型生成的工具调用
        :rtype: list of ToolCall
        """
        return self._ToolCalls

    @ToolCalls.setter
    def ToolCalls(self, ToolCalls):
        self._ToolCalls = ToolCalls


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        self._ToolCallId = params.get("ToolCallId")
        if params.get("ToolCalls") is not None:
            self._ToolCalls = []
            for item in params.get("ToolCalls"):
                obj = ToolCall()
                obj._deserialize(item)
                self._ToolCalls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiModalEmbeddingData(AbstractModel):
    r"""多模态特征向量

    """

    def __init__(self):
        r"""
        :param _TextEmbeddings: 文本特征向量
注意：此字段可能返回 null，表示取不到有效值。
        :type TextEmbeddings: list of EmbeddingData
        :param _ImageEmbeddings: 图片特征向量
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageEmbeddings: list of EmbeddingData
        """
        self._TextEmbeddings = None
        self._ImageEmbeddings = None

    @property
    def TextEmbeddings(self):
        r"""文本特征向量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of EmbeddingData
        """
        return self._TextEmbeddings

    @TextEmbeddings.setter
    def TextEmbeddings(self, TextEmbeddings):
        self._TextEmbeddings = TextEmbeddings

    @property
    def ImageEmbeddings(self):
        r"""图片特征向量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of EmbeddingData
        """
        return self._ImageEmbeddings

    @ImageEmbeddings.setter
    def ImageEmbeddings(self, ImageEmbeddings):
        self._ImageEmbeddings = ImageEmbeddings


    def _deserialize(self, params):
        if params.get("TextEmbeddings") is not None:
            self._TextEmbeddings = []
            for item in params.get("TextEmbeddings"):
                obj = EmbeddingData()
                obj._deserialize(item)
                self._TextEmbeddings.append(obj)
        if params.get("ImageEmbeddings") is not None:
            self._ImageEmbeddings = []
            for item in params.get("ImageEmbeddings"):
                obj = EmbeddingData()
                obj._deserialize(item)
                self._ImageEmbeddings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiModalUsage(AbstractModel):
    r"""多模态向量化消耗tokens和images数量

    """

    def __init__(self):
        r"""
        :param _TotalTokens: 消耗tokens
        :type TotalTokens: int
        :param _TotalImages: 输入图片数量
        :type TotalImages: int
        """
        self._TotalTokens = None
        self._TotalImages = None

    @property
    def TotalTokens(self):
        r"""消耗tokens
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens

    @property
    def TotalImages(self):
        r"""输入图片数量
        :rtype: int
        """
        return self._TotalImages

    @TotalImages.setter
    def TotalImages(self, TotalImages):
        self._TotalImages = TotalImages


    def _deserialize(self, params):
        self._TotalTokens = params.get("TotalTokens")
        self._TotalImages = params.get("TotalImages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OnlineSearchOptions(AbstractModel):
    r"""联网搜索选项。

    """

    def __init__(self):
        r"""
        :param _Engine: 搜索引擎。支持 bing 和 sogou。
        :type Engine: str
        """
        self._Engine = None

    @property
    def Engine(self):
        r"""搜索引擎。支持 bing 和 sogou。
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine


    def _deserialize(self, params):
        self._Engine = params.get("Engine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputMessage(AbstractModel):
    r"""会话内容，按对话时间从旧到新在数组中排列，长度受模型窗口大小限制。

    """

    def __init__(self):
        r"""
        :param _Role: 角色
        :type Role: str
        :param _Content: 文本内容	
        :type Content: str
        :param _ReasoningContent: 推理内容	
        :type ReasoningContent: str
        :param _ToolCalls: 模型生成的工具调用
        :type ToolCalls: list of ToolCall
        """
        self._Role = None
        self._Content = None
        self._ReasoningContent = None
        self._ToolCalls = None

    @property
    def Role(self):
        r"""角色
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        r"""文本内容	
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ReasoningContent(self):
        r"""推理内容	
        :rtype: str
        """
        return self._ReasoningContent

    @ReasoningContent.setter
    def ReasoningContent(self, ReasoningContent):
        self._ReasoningContent = ReasoningContent

    @property
    def ToolCalls(self):
        r"""模型生成的工具调用
        :rtype: list of ToolCall
        """
        return self._ToolCalls

    @ToolCalls.setter
    def ToolCalls(self, ToolCalls):
        self._ToolCalls = ToolCalls


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        self._ReasoningContent = params.get("ReasoningContent")
        if params.get("ToolCalls") is not None:
            self._ToolCalls = []
            for item in params.get("ToolCalls"):
                obj = ToolCall()
                obj._deserialize(item)
                self._ToolCalls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PageUsage(AbstractModel):
    r"""消耗页数

    """

    def __init__(self):
        r"""
        :param _TotalPages: 消耗总页数
        :type TotalPages: int
        """
        self._TotalPages = None

    @property
    def TotalPages(self):
        r"""消耗总页数
        :rtype: int
        """
        return self._TotalPages

    @TotalPages.setter
    def TotalPages(self, TotalPages):
        self._TotalPages = TotalPages


    def _deserialize(self, params):
        self._TotalPages = params.get("TotalPages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseDocument(AbstractModel):
    r"""文档信息

    """

    def __init__(self):
        r"""
        :param _FileType: 支持的文件类型：PDF、DOC、DOCX、PPT、PPTX、MD、TXT、XLS、
XLSX、CSV、PNG、JPG、JPEG、BMP、GIF、WEBP、HEIC、EPS、ICNS、
IM、PCX、PPM、TIFF、XBM、HEIF、JP2

文档解析支持的文件大小：
-PDF、DOC、DOCX、PPT、PPTX支持100M
-MD、TXT、XLS、XLSX、CSV支特10M
-其他支持20M

文本切片支持的文件大小：
-PDF最大300M
-D0CX、D0C、PPT、PPTX最大200M
-TXT、MD最大10M
-其他最大20M
        :type FileType: str
        :param _FileUrl: 文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，使用腾讯云COS 文件地址。
        :type FileUrl: str
        :param _FileContent: 文件的 base64 值，携带 MineType前缀信息。编码后的后的文件不超过 10M。
支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过3秒。
支持的图片像素：单边介于20-10000px之间。
文件的 FileUrl、FileContent必须提供一个，如果都提供只使用 FileUrl。
        :type FileContent: str
        :param _DocumentParseConfig: 文档解析配置
        :type DocumentParseConfig: :class:`tencentcloud.es.v20250101.models.DocumentParseConfig`
        :param _FileStartPageNumber: 文档的起始页码
        :type FileStartPageNumber: int
        :param _FileEndPageNumber: 文档的结束页码
        :type FileEndPageNumber: int
        """
        self._FileType = None
        self._FileUrl = None
        self._FileContent = None
        self._DocumentParseConfig = None
        self._FileStartPageNumber = None
        self._FileEndPageNumber = None

    @property
    def FileType(self):
        r"""支持的文件类型：PDF、DOC、DOCX、PPT、PPTX、MD、TXT、XLS、
XLSX、CSV、PNG、JPG、JPEG、BMP、GIF、WEBP、HEIC、EPS、ICNS、
IM、PCX、PPM、TIFF、XBM、HEIF、JP2

文档解析支持的文件大小：
-PDF、DOC、DOCX、PPT、PPTX支持100M
-MD、TXT、XLS、XLSX、CSV支特10M
-其他支持20M

文本切片支持的文件大小：
-PDF最大300M
-D0CX、D0C、PPT、PPTX最大200M
-TXT、MD最大10M
-其他最大20M
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileUrl(self):
        r"""文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，使用腾讯云COS 文件地址。
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileContent(self):
        r"""文件的 base64 值，携带 MineType前缀信息。编码后的后的文件不超过 10M。
支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过3秒。
支持的图片像素：单边介于20-10000px之间。
文件的 FileUrl、FileContent必须提供一个，如果都提供只使用 FileUrl。
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def DocumentParseConfig(self):
        r"""文档解析配置
        :rtype: :class:`tencentcloud.es.v20250101.models.DocumentParseConfig`
        """
        return self._DocumentParseConfig

    @DocumentParseConfig.setter
    def DocumentParseConfig(self, DocumentParseConfig):
        self._DocumentParseConfig = DocumentParseConfig

    @property
    def FileStartPageNumber(self):
        r"""文档的起始页码
        :rtype: int
        """
        return self._FileStartPageNumber

    @FileStartPageNumber.setter
    def FileStartPageNumber(self, FileStartPageNumber):
        self._FileStartPageNumber = FileStartPageNumber

    @property
    def FileEndPageNumber(self):
        r"""文档的结束页码
        :rtype: int
        """
        return self._FileEndPageNumber

    @FileEndPageNumber.setter
    def FileEndPageNumber(self, FileEndPageNumber):
        self._FileEndPageNumber = FileEndPageNumber


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileUrl = params.get("FileUrl")
        self._FileContent = params.get("FileContent")
        if params.get("DocumentParseConfig") is not None:
            self._DocumentParseConfig = DocumentParseConfig()
            self._DocumentParseConfig._deserialize(params.get("DocumentParseConfig"))
        self._FileStartPageNumber = params.get("FileStartPageNumber")
        self._FileEndPageNumber = params.get("FileEndPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseDocumentAsyncRequest(AbstractModel):
    r"""ParseDocumentAsync请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Document: 文件信息。
        :type Document: :class:`tencentcloud.es.v20250101.models.Document`
        :param _ModelName: 模型名称，可选模型列表：doc-llm。
        :type ModelName: str
        """
        self._Document = None
        self._ModelName = None

    @property
    def Document(self):
        r"""文件信息。
        :rtype: :class:`tencentcloud.es.v20250101.models.Document`
        """
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document

    @property
    def ModelName(self):
        r"""模型名称，可选模型列表：doc-llm。
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName


    def _deserialize(self, params):
        if params.get("Document") is not None:
            self._Document = Document()
            self._Document._deserialize(params.get("Document"))
        self._ModelName = params.get("ModelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseDocumentAsyncResponse(AbstractModel):
    r"""ParseDocumentAsync返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 id
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务 id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ParseDocumentRequest(AbstractModel):
    r"""ParseDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Document: 文件信息
        :type Document: :class:`tencentcloud.es.v20250101.models.ParseDocument`
        :param _ModelName: 模型名称，doc-llm。
        :type ModelName: str
        """
        self._Document = None
        self._ModelName = None

    @property
    def Document(self):
        r"""文件信息
        :rtype: :class:`tencentcloud.es.v20250101.models.ParseDocument`
        """
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document

    @property
    def ModelName(self):
        r"""模型名称，doc-llm。
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName


    def _deserialize(self, params):
        if params.get("Document") is not None:
            self._Document = ParseDocument()
            self._Document._deserialize(params.get("Document"))
        self._ModelName = params.get("ModelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseDocumentResponse(AbstractModel):
    r"""ParseDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Progress: 进度：0-100。
        :type Progress: str
        :param _DocumentParseResultUrl:  解析文件结果。
        :type DocumentParseResultUrl: str
        :param _FailedPages: 失败页码。
        :type FailedPages: list of int
        :param _Usage: 消耗页数
        :type Usage: :class:`tencentcloud.es.v20250101.models.PageUsage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._Progress = None
        self._DocumentParseResultUrl = None
        self._FailedPages = None
        self._Usage = None
        self._RequestId = None

    @property
    def Progress(self):
        r"""进度：0-100。
        :rtype: str
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def DocumentParseResultUrl(self):
        r""" 解析文件结果。
        :rtype: str
        """
        return self._DocumentParseResultUrl

    @DocumentParseResultUrl.setter
    def DocumentParseResultUrl(self, DocumentParseResultUrl):
        self._DocumentParseResultUrl = DocumentParseResultUrl

    @property
    def FailedPages(self):
        r"""失败页码。
        :rtype: list of int
        """
        return self._FailedPages

    @FailedPages.setter
    def FailedPages(self, FailedPages):
        self._FailedPages = FailedPages

    @property
    def Usage(self):
        r"""消耗页数
        :rtype: :class:`tencentcloud.es.v20250101.models.PageUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
        self._Progress = params.get("Progress")
        self._DocumentParseResultUrl = params.get("DocumentParseResultUrl")
        self._FailedPages = params.get("FailedPages")
        if params.get("Usage") is not None:
            self._Usage = PageUsage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class RerankResult(AbstractModel):
    r"""输出结果

    """

    def __init__(self):
        r"""
        :param _Index: 对应的doc在输入候选doc数组中的位置索引值
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: int
        :param _RelevanceScore: 相似度分数
注意：此字段可能返回 null，表示取不到有效值。
        :type RelevanceScore: float
        :param _Document: doc原文内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Document: str
        """
        self._Index = None
        self._RelevanceScore = None
        self._Document = None

    @property
    def Index(self):
        r"""对应的doc在输入候选doc数组中的位置索引值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def RelevanceScore(self):
        r"""相似度分数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._RelevanceScore

    @RelevanceScore.setter
    def RelevanceScore(self, RelevanceScore):
        self._RelevanceScore = RelevanceScore

    @property
    def Document(self):
        r"""doc原文内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._RelevanceScore = params.get("RelevanceScore")
        self._Document = params.get("Document")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunRerankRequest(AbstractModel):
    r"""RunRerank请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelName: 模型名称，可选模型列表：bge-reranker-large，bge-reranker-v2-m3。
        :type ModelName: str
        :param _Query: 查询文本。
        :type Query: str
        :param _Documents: 待排序的候选doc列表。
        :type Documents: list of str
        :param _TopN: 排序返回的top文档数量, 如果没有指定则返回全部候选doc，如果指定的top_n值大于输入的候选doc数量，返回全部doc。
        :type TopN: int
        :param _ReturnDocuments: 返回的排序结果列表里面是否返回每一条document原文，默认值False。
        :type ReturnDocuments: bool
        """
        self._ModelName = None
        self._Query = None
        self._Documents = None
        self._TopN = None
        self._ReturnDocuments = None

    @property
    def ModelName(self):
        r"""模型名称，可选模型列表：bge-reranker-large，bge-reranker-v2-m3。
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def Query(self):
        r"""查询文本。
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Documents(self):
        r"""待排序的候选doc列表。
        :rtype: list of str
        """
        return self._Documents

    @Documents.setter
    def Documents(self, Documents):
        self._Documents = Documents

    @property
    def TopN(self):
        r"""排序返回的top文档数量, 如果没有指定则返回全部候选doc，如果指定的top_n值大于输入的候选doc数量，返回全部doc。
        :rtype: int
        """
        return self._TopN

    @TopN.setter
    def TopN(self, TopN):
        self._TopN = TopN

    @property
    def ReturnDocuments(self):
        r"""返回的排序结果列表里面是否返回每一条document原文，默认值False。
        :rtype: bool
        """
        return self._ReturnDocuments

    @ReturnDocuments.setter
    def ReturnDocuments(self, ReturnDocuments):
        self._ReturnDocuments = ReturnDocuments


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._Query = params.get("Query")
        self._Documents = params.get("Documents")
        self._TopN = params.get("TopN")
        self._ReturnDocuments = params.get("ReturnDocuments")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunRerankResponse(AbstractModel):
    r"""RunRerank返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 输出结果集。
        :type Data: list of RerankResult
        :param _Usage: 消耗token数量。
        :type Usage: :class:`tencentcloud.es.v20250101.models.Usage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Usage = None
        self._RequestId = None

    @property
    def Data(self):
        r"""输出结果集。
        :rtype: list of RerankResult
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Usage(self):
        r"""消耗token数量。
        :rtype: :class:`tencentcloud.es.v20250101.models.Usage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RerankResult()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class TokenUsage(AbstractModel):
    r"""token使用量

    """

    def __init__(self):
        r"""
        :param _PromptTokens: 表示prompt的tokens数，多次返回中保持不变
        :type PromptTokens: int
        :param _CompletionTokens: 回答的token总数，在流式返回中，表示到目前为止所有completion的tokens总数，多次返回中持续累加        
        :type CompletionTokens: int
        :param _TotalTokens: 表示prompt_tokens和completion_tokens之和 
        :type TotalTokens: int
        """
        self._PromptTokens = None
        self._CompletionTokens = None
        self._TotalTokens = None

    @property
    def PromptTokens(self):
        r"""表示prompt的tokens数，多次返回中保持不变
        :rtype: int
        """
        return self._PromptTokens

    @PromptTokens.setter
    def PromptTokens(self, PromptTokens):
        self._PromptTokens = PromptTokens

    @property
    def CompletionTokens(self):
        r"""回答的token总数，在流式返回中，表示到目前为止所有completion的tokens总数，多次返回中持续累加        
        :rtype: int
        """
        return self._CompletionTokens

    @CompletionTokens.setter
    def CompletionTokens(self, CompletionTokens):
        self._CompletionTokens = CompletionTokens

    @property
    def TotalTokens(self):
        r"""表示prompt_tokens和completion_tokens之和 
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._PromptTokens = params.get("PromptTokens")
        self._CompletionTokens = params.get("CompletionTokens")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tool(AbstractModel):
    r"""用户指定模型使用的工具

    """

    def __init__(self):
        r"""
        :param _Type: 工具类型，当前只支持function
        :type Type: str
        :param _Function: 具体要调用的function
        :type Function: :class:`tencentcloud.es.v20250101.models.ToolFunction`
        """
        self._Type = None
        self._Function = None

    @property
    def Type(self):
        r"""工具类型，当前只支持function
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Function(self):
        r"""具体要调用的function
        :rtype: :class:`tencentcloud.es.v20250101.models.ToolFunction`
        """
        return self._Function

    @Function.setter
    def Function(self, Function):
        self._Function = Function


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("Function") is not None:
            self._Function = ToolFunction()
            self._Function._deserialize(params.get("Function"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ToolCall(AbstractModel):
    r"""模型生成的工具调用

    """

    def __init__(self):
        r"""
        :param _Id: 工具调用id
        :type Id: str
        :param _Type: 工具调用类型，当前只支持function
        :type Type: str
        :param _Function: 具体的function调用
        :type Function: :class:`tencentcloud.es.v20250101.models.ToolCallFunction`
        :param _Index: 索引值
        :type Index: int
        """
        self._Id = None
        self._Type = None
        self._Function = None
        self._Index = None

    @property
    def Id(self):
        r"""工具调用id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        r"""工具调用类型，当前只支持function
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Function(self):
        r"""具体的function调用
        :rtype: :class:`tencentcloud.es.v20250101.models.ToolCallFunction`
        """
        return self._Function

    @Function.setter
    def Function(self, Function):
        self._Function = Function

    @property
    def Index(self):
        r"""索引值
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        if params.get("Function") is not None:
            self._Function = ToolCallFunction()
            self._Function._deserialize(params.get("Function"))
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ToolCallFunction(AbstractModel):
    r"""具体的function调用

    """

    def __init__(self):
        r"""
        :param _Name: function名称
        :type Name: str
        :param _Arguments: function参数，一般为json字符串
        :type Arguments: str
        """
        self._Name = None
        self._Arguments = None

    @property
    def Name(self):
        r"""function名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Arguments(self):
        r"""function参数，一般为json字符串
        :rtype: str
        """
        return self._Arguments

    @Arguments.setter
    def Arguments(self, Arguments):
        self._Arguments = Arguments


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Arguments = params.get("Arguments")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ToolFunction(AbstractModel):
    r"""function定义

    """

    def __init__(self):
        r"""
        :param _Name: function名称，只能包含a-z，A-Z，0-9，_或-
        :type Name: str
        :param _Parameters: function参数，一般为json字符串
        :type Parameters: str
        :param _Description: function的简单描述
        :type Description: str
        """
        self._Name = None
        self._Parameters = None
        self._Description = None

    @property
    def Name(self):
        r"""function名称，只能包含a-z，A-Z，0-9，_或-
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Parameters(self):
        r"""function参数，一般为json字符串
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def Description(self):
        r"""function的简单描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Parameters = params.get("Parameters")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Usage(AbstractModel):
    r"""token消耗总数

    """

    def __init__(self):
        r"""
        :param _TotalTokens: tokens总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalTokens: int
        """
        self._TotalTokens = None

    @property
    def TotalTokens(self):
        r"""tokens总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebContent(AbstractModel):
    r"""搜索结果网页信息。

    """

    def __init__(self):
        r"""
        :param _Query: 搜素问题	
        :type Query: str
        :param _Title: 标题
        :type Title: str
        :param _Url: 链接
        :type Url: str
        :param _Time: 时间
        :type Time: str
        :param _Content: 网页内容	
        :type Content: str
        :param _ChunkIndex: 切片索引
        :type ChunkIndex: str
        :param _Score: 分数
        :type Score: str
        """
        self._Query = None
        self._Title = None
        self._Url = None
        self._Time = None
        self._Content = None
        self._ChunkIndex = None
        self._Score = None

    @property
    def Query(self):
        r"""搜素问题	
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

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
    def Url(self):
        r"""链接
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Time(self):
        r"""时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Content(self):
        r"""网页内容	
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ChunkIndex(self):
        r"""切片索引
        :rtype: str
        """
        return self._ChunkIndex

    @ChunkIndex.setter
    def ChunkIndex(self, ChunkIndex):
        self._ChunkIndex = ChunkIndex

    @property
    def Score(self):
        r"""分数
        :rtype: str
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._Title = params.get("Title")
        self._Url = params.get("Url")
        self._Time = params.get("Time")
        self._Content = params.get("Content")
        self._ChunkIndex = params.get("ChunkIndex")
        self._Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        