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


class ChatCompletionsRequest(AbstractModel):
    """ChatCompletions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Messages: 会话内容，按对话时间从旧到新在数组中排列，长度受模型窗口大小限制
        :type Messages: list of Message
        :param _ModelName: 模型名称
        :type ModelName: str
        :param _Stream: 是否以流式接口的形式返回数据，默认true
        :type Stream: bool
        :param _TopP: 取值区间为[0.0, 1.0], 非必要不建议使用, 不合理的取值会影响效果 
        :type TopP: float
        :param _Temperature: 取值区间为[0.0, 2.0], 非必要不建议使用, 不合理的取值会影响效果 
        :type Temperature: float
        :param _OnlineSearch: 是否开启联网搜索。默认为 false。
        :type OnlineSearch: bool
        :param _OnlineSearchOptions: 当 OnlineSearch 为 true 时，指定的搜索引擎，默认为 bing。
        :type OnlineSearchOptions: :class:`tencentcloud.es.v20250101.models.OnlineSearchOptions`
        """
        self._Messages = None
        self._ModelName = None
        self._Stream = None
        self._TopP = None
        self._Temperature = None
        self._OnlineSearch = None
        self._OnlineSearchOptions = None

    @property
    def Messages(self):
        """会话内容，按对话时间从旧到新在数组中排列，长度受模型窗口大小限制
        :rtype: list of Message
        """
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def ModelName(self):
        """模型名称
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def Stream(self):
        """是否以流式接口的形式返回数据，默认true
        :rtype: bool
        """
        return self._Stream

    @Stream.setter
    def Stream(self, Stream):
        self._Stream = Stream

    @property
    def TopP(self):
        """取值区间为[0.0, 1.0], 非必要不建议使用, 不合理的取值会影响效果 
        :rtype: float
        """
        return self._TopP

    @TopP.setter
    def TopP(self, TopP):
        self._TopP = TopP

    @property
    def Temperature(self):
        """取值区间为[0.0, 2.0], 非必要不建议使用, 不合理的取值会影响效果 
        :rtype: float
        """
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def OnlineSearch(self):
        """是否开启联网搜索。默认为 false。
        :rtype: bool
        """
        return self._OnlineSearch

    @OnlineSearch.setter
    def OnlineSearch(self, OnlineSearch):
        self._OnlineSearch = OnlineSearch

    @property
    def OnlineSearchOptions(self):
        """当 OnlineSearch 为 true 时，指定的搜索引擎，默认为 bing。
        :rtype: :class:`tencentcloud.es.v20250101.models.OnlineSearchOptions`
        """
        return self._OnlineSearchOptions

    @OnlineSearchOptions.setter
    def OnlineSearchOptions(self, OnlineSearchOptions):
        self._OnlineSearchOptions = OnlineSearchOptions


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatCompletionsResponse(AbstractModel):
    """ChatCompletions返回参数结构体

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
        """此次请求的id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Choices(self):
        """回复内容
        :rtype: list of Choice
        """
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices

    @property
    def Usage(self):
        """token使用量
        :rtype: :class:`tencentcloud.es.v20250101.models.TokenUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def OnlineSearchContent(self):
        """联网搜索结果。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WebContent
        """
        return self._OnlineSearchContent

    @OnlineSearchContent.setter
    def OnlineSearchContent(self, OnlineSearchContent):
        self._OnlineSearchContent = OnlineSearchContent

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
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
    """返回的回复, 支持多个。

    """

    def __init__(self):
        r"""
        :param _Message: 返回的回复。
        :type Message: :class:`tencentcloud.es.v20250101.models.OutputMessage`
        """
        self._Message = None

    @property
    def Message(self):
        """返回的回复。
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
    """切片对象信息

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
        """chunk索引。切片顺序 id。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Content(self):
        """chunk内容。
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
    """文档分片配置

    """

    def __init__(self):
        r"""
        :param _MaxChunkSize: 最大分片长度
        :type MaxChunkSize: int
        :param _Delimiters: 分隔符列表
        :type Delimiters: list of str
        """
        self._MaxChunkSize = None
        self._Delimiters = None

    @property
    def MaxChunkSize(self):
        """最大分片长度
        :rtype: int
        """
        return self._MaxChunkSize

    @MaxChunkSize.setter
    def MaxChunkSize(self, MaxChunkSize):
        self._MaxChunkSize = MaxChunkSize

    @property
    def Delimiters(self):
        """分隔符列表
        :rtype: list of str
        """
        return self._Delimiters

    @Delimiters.setter
    def Delimiters(self, Delimiters):
        self._Delimiters = Delimiters


    def _deserialize(self, params):
        self._MaxChunkSize = params.get("MaxChunkSize")
        self._Delimiters = params.get("Delimiters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChunkConfigAsync(AbstractModel):
    """文档切片异步任务

    """

    def __init__(self):
        r"""
        :param _MaxChunkSize: 最大分片长度
        :type MaxChunkSize: int
        """
        self._MaxChunkSize = None

    @property
    def MaxChunkSize(self):
        """最大分片长度
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
    """切片文档信息

    """

    def __init__(self):
        r"""
        :param _FileType: 文件类型
        :type FileType: str
        :param _FileContent: 文件的 base64值
        :type FileContent: str
        """
        self._FileType = None
        self._FileContent = None

    @property
    def FileType(self):
        """文件类型
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileContent(self):
        """文件的 base64值
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
    """ChunkDocumentAsync请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Document: 文件信息
        :type Document: :class:`tencentcloud.es.v20250101.models.Document`
        :param _ModelName: 模型名称
        :type ModelName: str
        :param _Config: 文件切片配置
        :type Config: :class:`tencentcloud.es.v20250101.models.ChunkConfigAsync`
        """
        self._Document = None
        self._ModelName = None
        self._Config = None

    @property
    def Document(self):
        """文件信息
        :rtype: :class:`tencentcloud.es.v20250101.models.Document`
        """
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document

    @property
    def ModelName(self):
        """模型名称
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def Config(self):
        """文件切片配置
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
    """ChunkDocumentAsync返回参数结构体

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
        """任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ChunkDocumentRequest(AbstractModel):
    """ChunkDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Document: 文件切片文件信息
        :type Document: :class:`tencentcloud.es.v20250101.models.ChunkDocument`
        :param _ModelName: 模型名称
        :type ModelName: str
        :param _Config: 文件切片配置
        :type Config: :class:`tencentcloud.es.v20250101.models.ChunkConfig`
        """
        self._Document = None
        self._ModelName = None
        self._Config = None

    @property
    def Document(self):
        """文件切片文件信息
        :rtype: :class:`tencentcloud.es.v20250101.models.ChunkDocument`
        """
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document

    @property
    def ModelName(self):
        """模型名称
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def Config(self):
        """文件切片配置
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
    """ChunkDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Chunks: 无
        :type Chunks: list of Chunk
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Chunks = None
        self._RequestId = None

    @property
    def Chunks(self):
        """无
        :rtype: list of Chunk
        """
        return self._Chunks

    @Chunks.setter
    def Chunks(self, Chunks):
        self._Chunks = Chunks

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
        if params.get("Chunks") is not None:
            self._Chunks = []
            for item in params.get("Chunks"):
                obj = Chunk()
                obj._deserialize(item)
                self._Chunks.append(obj)
        self._RequestId = params.get("RequestId")


class Document(AbstractModel):
    """文档信息

    """

    def __init__(self):
        r"""
        :param _FileType: 文件类型。
支持的文件类型：PDF、DOC、DOCX、PPT、PPTX、MD、TXT、XLS、XLSX、CSV、PNG、JPG、JPEG、BMP、GIF、WEBP、HEIC、EPS、ICNS、IM、PCX、PPM、TIFF、XBM、HEIF、JP2
支持的文件大小：
- PDF、DOC、DOCX、PPT、PPTX 支持100M
- MD、TXT、XLS、XLSX、CSV 支持10M
- 其他支持20M
        :type FileType: str
        :param _FileUrl: 文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，使用腾讯云COS 文件地址。
        :type FileUrl: str
        :param _FileContent: 文件的 base64 值，携带 MineType前缀信息。编码后的后的文件不超过 10M。
支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过3秒。
支持的图片像素：单边介于20-10000px之间。
        :type FileContent: str
        :param _FileName: 文件名称，当使用 base64上传的时候使用。
        :type FileName: str
        """
        self._FileType = None
        self._FileUrl = None
        self._FileContent = None
        self._FileName = None

    @property
    def FileType(self):
        """文件类型。
支持的文件类型：PDF、DOC、DOCX、PPT、PPTX、MD、TXT、XLS、XLSX、CSV、PNG、JPG、JPEG、BMP、GIF、WEBP、HEIC、EPS、ICNS、IM、PCX、PPM、TIFF、XBM、HEIF、JP2
支持的文件大小：
- PDF、DOC、DOCX、PPT、PPTX 支持100M
- MD、TXT、XLS、XLSX、CSV 支持10M
- 其他支持20M
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileUrl(self):
        """文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，使用腾讯云COS 文件地址。
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileContent(self):
        """文件的 base64 值，携带 MineType前缀信息。编码后的后的文件不超过 10M。
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
        """文件名称，当使用 base64上传的时候使用。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileUrl = params.get("FileUrl")
        self._FileContent = params.get("FileContent")
        self._FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DocumentChunkUsage(AbstractModel):
    """文档切片用量

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
        """ 解析页面数量
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def TotalTokens(self):
        """消耗 token数量
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
        


class EmbeddingData(AbstractModel):
    """向量内容

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
        """embedding 内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of float
        """
        return self._Embedding

    @Embedding.setter
    def Embedding(self, Embedding):
        self._Embedding = Embedding

    @property
    def Index(self):
        """索引序号
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
    """GetDocumentChunkResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId:  任务 ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """ 任务 ID
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
    """GetDocumentChunkResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态
        :type Status: int
        :param _DocumentChunkResultUrl: 切片结果
        :type DocumentChunkResultUrl: str
        :param _Usage: 用量
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
        """任务状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DocumentChunkResultUrl(self):
        """切片结果
        :rtype: str
        """
        return self._DocumentChunkResultUrl

    @DocumentChunkResultUrl.setter
    def DocumentChunkResultUrl(self, DocumentChunkResultUrl):
        self._DocumentChunkResultUrl = DocumentChunkResultUrl

    @property
    def Usage(self):
        """用量
        :rtype: :class:`tencentcloud.es.v20250101.models.DocumentChunkUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
        self._Status = params.get("Status")
        self._DocumentChunkResultUrl = params.get("DocumentChunkResultUrl")
        if params.get("Usage") is not None:
            self._Usage = DocumentChunkUsage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class GetDocumentParseResultRequest(AbstractModel):
    """GetDocumentParseResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 Id
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """任务 Id
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
    """GetDocumentParseResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态
        :type Status: int
        :param _DocumentParseResultUrl: 结果文件
        :type DocumentParseResultUrl: str
        :param _FailedPages: 失败的页码
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedPages: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._DocumentParseResultUrl = None
        self._FailedPages = None
        self._RequestId = None

    @property
    def Status(self):
        """任务状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DocumentParseResultUrl(self):
        """结果文件
        :rtype: str
        """
        return self._DocumentParseResultUrl

    @DocumentParseResultUrl.setter
    def DocumentParseResultUrl(self, DocumentParseResultUrl):
        self._DocumentParseResultUrl = DocumentParseResultUrl

    @property
    def FailedPages(self):
        """失败的页码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._FailedPages

    @FailedPages.setter
    def FailedPages(self, FailedPages):
        self._FailedPages = FailedPages

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
        self._Status = params.get("Status")
        self._DocumentParseResultUrl = params.get("DocumentParseResultUrl")
        self._FailedPages = params.get("FailedPages")
        self._RequestId = params.get("RequestId")


class GetTextEmbeddingRequest(AbstractModel):
    """GetTextEmbedding请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelName: 模型名称
        :type ModelName: str
        :param _Texts: 需进行向量化的文本集
        :type Texts: list of str
        """
        self._ModelName = None
        self._Texts = None

    @property
    def ModelName(self):
        """模型名称
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def Texts(self):
        """需进行向量化的文本集
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
    """GetTextEmbedding返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果集
        :type Data: list of EmbeddingData
        :param _Usage: 消耗token数量
        :type Usage: :class:`tencentcloud.es.v20250101.models.Usage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Usage = None
        self._RequestId = None

    @property
    def Data(self):
        """结果集
        :rtype: list of EmbeddingData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Usage(self):
        """消耗token数量
        :rtype: :class:`tencentcloud.es.v20250101.models.Usage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
    """会话内容，按对话时间从旧到新在数组中排列，长度受模型窗口大小限制。

    """

    def __init__(self):
        r"""
        :param _Role: 角色, ‘system', ‘user'，'assistant'或者'tool', 在message中, 除了system，其他必须是user与assistant交替(一问一答) 
        :type Role: str
        :param _Content: 具体文本内容
        :type Content: str
        """
        self._Role = None
        self._Content = None

    @property
    def Role(self):
        """角色, ‘system', ‘user'，'assistant'或者'tool', 在message中, 除了system，其他必须是user与assistant交替(一问一答) 
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        """具体文本内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OnlineSearchOptions(AbstractModel):
    """联网搜索选项。

    """

    def __init__(self):
        r"""
        :param _Engine: 搜索引擎。支持 bing 和 sogou。
        :type Engine: str
        """
        self._Engine = None

    @property
    def Engine(self):
        """搜索引擎。支持 bing 和 sogou。
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
    """会话内容，按对话时间从旧到新在数组中排列，长度受模型窗口大小限制。

    """

    def __init__(self):
        r"""
        :param _Role: 角色
        :type Role: str
        :param _Content: 文本内容	
        :type Content: str
        :param _ReasoningContent: 推理内容	
        :type ReasoningContent: str
        """
        self._Role = None
        self._Content = None
        self._ReasoningContent = None

    @property
    def Role(self):
        """角色
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        """文本内容	
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ReasoningContent(self):
        """推理内容	
        :rtype: str
        """
        return self._ReasoningContent

    @ReasoningContent.setter
    def ReasoningContent(self, ReasoningContent):
        self._ReasoningContent = ReasoningContent


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        self._ReasoningContent = params.get("ReasoningContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseDocument(AbstractModel):
    """文档信息

    """

    def __init__(self):
        r"""
        :param _FileType: 文件类型。
支持的文件类型：PDF、DOC、DOCX、PPT、PPTX、MD、TXT、XLS、XLSX、CSV、PNG、JPG、JPEG、BMP、GIF、WEBP、HEIC、EPS、ICNS、IM、PCX、PPM、TIFF、XBM、HEIF、JP2
支持的文件大小：
- PDF、DOC、DOCX、PPT、PPTX 支持100M
- MD、TXT、XLS、XLSX、CSV 支持10M
- 其他支持20M
        :type FileType: str
        :param _FileUrl: 文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，使用腾讯云COS 文件地址。
        :type FileUrl: str
        :param _FileContent: 文件的 base64 值，携带 MineType前缀信息。编码后的后的文件不超过 10M。
支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过3秒。
支持的图片像素：单边介于20-10000px之间。
        :type FileContent: str
        """
        self._FileType = None
        self._FileUrl = None
        self._FileContent = None

    @property
    def FileType(self):
        """文件类型。
支持的文件类型：PDF、DOC、DOCX、PPT、PPTX、MD、TXT、XLS、XLSX、CSV、PNG、JPG、JPEG、BMP、GIF、WEBP、HEIC、EPS、ICNS、IM、PCX、PPM、TIFF、XBM、HEIF、JP2
支持的文件大小：
- PDF、DOC、DOCX、PPT、PPTX 支持100M
- MD、TXT、XLS、XLSX、CSV 支持10M
- 其他支持20M
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileUrl(self):
        """文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，使用腾讯云COS 文件地址。
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileContent(self):
        """文件的 base64 值，携带 MineType前缀信息。编码后的后的文件不超过 10M。
支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过3秒。
支持的图片像素：单边介于20-10000px之间。
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileUrl = params.get("FileUrl")
        self._FileContent = params.get("FileContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseDocumentAsyncRequest(AbstractModel):
    """ParseDocumentAsync请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Document: 文件信息
        :type Document: :class:`tencentcloud.es.v20250101.models.Document`
        :param _ModelName: 模型名称
        :type ModelName: str
        """
        self._Document = None
        self._ModelName = None

    @property
    def Document(self):
        """文件信息
        :rtype: :class:`tencentcloud.es.v20250101.models.Document`
        """
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document

    @property
    def ModelName(self):
        """模型名称
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
    """ParseDocumentAsync返回参数结构体

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
        """任务 id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ParseDocumentRequest(AbstractModel):
    """ParseDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Document: 文件信息
        :type Document: :class:`tencentcloud.es.v20250101.models.ParseDocument`
        :param _ModelName: 模型名称
        :type ModelName: str
        """
        self._Document = None
        self._ModelName = None

    @property
    def Document(self):
        """文件信息
        :rtype: :class:`tencentcloud.es.v20250101.models.ParseDocument`
        """
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document

    @property
    def ModelName(self):
        """模型名称
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
    """ParseDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Progress: 进度
        :type Progress: str
        :param _DocumentParseResultUrl:  解析文件结果
        :type DocumentParseResultUrl: str
        :param _FailedPages: 失败页码
        :type FailedPages: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._Progress = None
        self._DocumentParseResultUrl = None
        self._FailedPages = None
        self._RequestId = None

    @property
    def Progress(self):
        """进度
        :rtype: str
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def DocumentParseResultUrl(self):
        """ 解析文件结果
        :rtype: str
        """
        return self._DocumentParseResultUrl

    @DocumentParseResultUrl.setter
    def DocumentParseResultUrl(self, DocumentParseResultUrl):
        self._DocumentParseResultUrl = DocumentParseResultUrl

    @property
    def FailedPages(self):
        """失败页码
        :rtype: list of int
        """
        return self._FailedPages

    @FailedPages.setter
    def FailedPages(self, FailedPages):
        self._FailedPages = FailedPages

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
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
        self._RequestId = params.get("RequestId")


class RerankResult(AbstractModel):
    """输出结果

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
        """对应的doc在输入候选doc数组中的位置索引值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def RelevanceScore(self):
        """相似度分数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._RelevanceScore

    @RelevanceScore.setter
    def RelevanceScore(self, RelevanceScore):
        self._RelevanceScore = RelevanceScore

    @property
    def Document(self):
        """doc原文内容
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
    """RunRerank请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelName: 模型名称
        :type ModelName: str
        :param _Query: 查询文本
        :type Query: str
        :param _Documents: 待排序的候选doc列表
        :type Documents: list of str
        :param _TopN: 排序返回的top文档数量, 如果没有指定则返回全部候选doc，如果指定的top_n值大于输入的候选doc数量，返回全部doc
        :type TopN: int
        :param _ReturnDocuments: 返回的排序结果列表里面是否返回每一条document原文，默认值False
        :type ReturnDocuments: bool
        """
        self._ModelName = None
        self._Query = None
        self._Documents = None
        self._TopN = None
        self._ReturnDocuments = None

    @property
    def ModelName(self):
        """模型名称
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def Query(self):
        """查询文本
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Documents(self):
        """待排序的候选doc列表
        :rtype: list of str
        """
        return self._Documents

    @Documents.setter
    def Documents(self, Documents):
        self._Documents = Documents

    @property
    def TopN(self):
        """排序返回的top文档数量, 如果没有指定则返回全部候选doc，如果指定的top_n值大于输入的候选doc数量，返回全部doc
        :rtype: int
        """
        return self._TopN

    @TopN.setter
    def TopN(self, TopN):
        self._TopN = TopN

    @property
    def ReturnDocuments(self):
        """返回的排序结果列表里面是否返回每一条document原文，默认值False
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
    """RunRerank返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 输出结果集
        :type Data: list of RerankResult
        :param _Usage: 消耗token数量
        :type Usage: :class:`tencentcloud.es.v20250101.models.Usage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Usage = None
        self._RequestId = None

    @property
    def Data(self):
        """输出结果集
        :rtype: list of RerankResult
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Usage(self):
        """消耗token数量
        :rtype: :class:`tencentcloud.es.v20250101.models.Usage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
    """token使用量

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
        """表示prompt的tokens数，多次返回中保持不变
        :rtype: int
        """
        return self._PromptTokens

    @PromptTokens.setter
    def PromptTokens(self, PromptTokens):
        self._PromptTokens = PromptTokens

    @property
    def CompletionTokens(self):
        """回答的token总数，在流式返回中，表示到目前为止所有completion的tokens总数，多次返回中持续累加        
        :rtype: int
        """
        return self._CompletionTokens

    @CompletionTokens.setter
    def CompletionTokens(self, CompletionTokens):
        self._CompletionTokens = CompletionTokens

    @property
    def TotalTokens(self):
        """表示prompt_tokens和completion_tokens之和 
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
        


class Usage(AbstractModel):
    """token消耗总数

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
        """tokens总数
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
    """搜索结果网页信息。

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
        """搜素问题	
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Title(self):
        """标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Url(self):
        """链接
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Time(self):
        """时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Content(self):
        """网页内容	
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ChunkIndex(self):
        """切片索引
        :rtype: str
        """
        return self._ChunkIndex

    @ChunkIndex.setter
    def ChunkIndex(self, ChunkIndex):
        self._ChunkIndex = ChunkIndex

    @property
    def Score(self):
        """分数
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
        