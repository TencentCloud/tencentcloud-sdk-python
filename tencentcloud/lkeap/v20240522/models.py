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


class CancelTaskRequest(AbstractModel):
    r"""CancelTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 取消任务的任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""取消任务的任务ID
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
        


class CancelTaskResponse(AbstractModel):
    r"""CancelTask返回参数结构体

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


class ChatCompletionsRequest(AbstractModel):
    r"""ChatCompletions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Model: 模型名称
        :type Model: str
        :param _Messages: 聊天上下文信息。
说明：
1. 长度最多为 40，按对话时间从旧到新在数组中排列。
2. Message.Role 可选值：system、user、assistant。
其中，system 角色可选，如存在则必须位于列表的最开始。user 和 assistant 需交替出现，以 user 提问开始，user 提问结束，Content 不能为空。Role 的顺序示例：[system（可选） user assistant user assistant user ...]。

        :type Messages: list of Message
        :param _Stream: 是否流式输出
        :type Stream: bool
        :param _Temperature: 控制生成的随机性，较高的值会产生更多样化的输出。
        :type Temperature: float
        :param _MaxTokens: 模型最大输出长度（单位 token），不包含思维链内容。
默认为4096，取值范围：各个模型不同，参考各个模型最大输出长度（示例：4k，即4096）。
输出 token 的总长度受模型的上下文长度限制。
        :type MaxTokens: int
        :param _EnableSearch: 是否启用联网搜索
        :type EnableSearch: bool
        :param _Thinking: 思维链开关，本参数仅在deepseek v3.1时生效
        :type Thinking: :class:`tencentcloud.lkeap.v20240522.models.Thinking`
        """
        self._Model = None
        self._Messages = None
        self._Stream = None
        self._Temperature = None
        self._MaxTokens = None
        self._EnableSearch = None
        self._Thinking = None

    @property
    def Model(self):
        r"""模型名称
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Messages(self):
        r"""聊天上下文信息。
说明：
1. 长度最多为 40，按对话时间从旧到新在数组中排列。
2. Message.Role 可选值：system、user、assistant。
其中，system 角色可选，如存在则必须位于列表的最开始。user 和 assistant 需交替出现，以 user 提问开始，user 提问结束，Content 不能为空。Role 的顺序示例：[system（可选） user assistant user assistant user ...]。

        :rtype: list of Message
        """
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def Stream(self):
        r"""是否流式输出
        :rtype: bool
        """
        return self._Stream

    @Stream.setter
    def Stream(self, Stream):
        self._Stream = Stream

    @property
    def Temperature(self):
        r"""控制生成的随机性，较高的值会产生更多样化的输出。
        :rtype: float
        """
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def MaxTokens(self):
        r"""模型最大输出长度（单位 token），不包含思维链内容。
默认为4096，取值范围：各个模型不同，参考各个模型最大输出长度（示例：4k，即4096）。
输出 token 的总长度受模型的上下文长度限制。
        :rtype: int
        """
        return self._MaxTokens

    @MaxTokens.setter
    def MaxTokens(self, MaxTokens):
        self._MaxTokens = MaxTokens

    @property
    def EnableSearch(self):
        r"""是否启用联网搜索
        :rtype: bool
        """
        return self._EnableSearch

    @EnableSearch.setter
    def EnableSearch(self, EnableSearch):
        self._EnableSearch = EnableSearch

    @property
    def Thinking(self):
        r"""思维链开关，本参数仅在deepseek v3.1时生效
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.Thinking`
        """
        return self._Thinking

    @Thinking.setter
    def Thinking(self, Thinking):
        self._Thinking = Thinking


    def _deserialize(self, params):
        self._Model = params.get("Model")
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = Message()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._Stream = params.get("Stream")
        self._Temperature = params.get("Temperature")
        self._MaxTokens = params.get("MaxTokens")
        self._EnableSearch = params.get("EnableSearch")
        if params.get("Thinking") is not None:
            self._Thinking = Thinking()
            self._Thinking._deserialize(params.get("Thinking"))
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
        :param _Created: Unix 时间戳，单位为秒。
        :type Created: int
        :param _Usage: Token 统计信息。
按照总 Token 数量计费。
        :type Usage: :class:`tencentcloud.lkeap.v20240522.models.ChatUsage`
        :param _Id: 本次请求的 RequestId。
        :type Id: str
        :param _Choices: 回复内容。
        :type Choices: list of Choice
        :param _Model: 模型名称。
        :type Model: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._Created = None
        self._Usage = None
        self._Id = None
        self._Choices = None
        self._Model = None
        self._RequestId = None

    @property
    def Created(self):
        r"""Unix 时间戳，单位为秒。
        :rtype: int
        """
        return self._Created

    @Created.setter
    def Created(self, Created):
        self._Created = Created

    @property
    def Usage(self):
        r"""Token 统计信息。
按照总 Token 数量计费。
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.ChatUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Id(self):
        r"""本次请求的 RequestId。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Choices(self):
        r"""回复内容。
        :rtype: list of Choice
        """
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices

    @property
    def Model(self):
        r"""模型名称。
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

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
        self._Created = params.get("Created")
        if params.get("Usage") is not None:
            self._Usage = ChatUsage()
            self._Usage._deserialize(params.get("Usage"))
        self._Id = params.get("Id")
        if params.get("Choices") is not None:
            self._Choices = []
            for item in params.get("Choices"):
                obj = Choice()
                obj._deserialize(item)
                self._Choices.append(obj)
        self._Model = params.get("Model")
        self._RequestId = params.get("RequestId")


class ChatUsage(AbstractModel):
    r"""消耗量

    """

    def __init__(self):
        r"""
        :param _PromptTokens: 输入token数
        :type PromptTokens: int
        :param _CompletionTokens: 输出token数
        :type CompletionTokens: int
        :param _TotalTokens: 总token数
        :type TotalTokens: int
        """
        self._PromptTokens = None
        self._CompletionTokens = None
        self._TotalTokens = None

    @property
    def PromptTokens(self):
        r"""输入token数
        :rtype: int
        """
        return self._PromptTokens

    @PromptTokens.setter
    def PromptTokens(self, PromptTokens):
        self._PromptTokens = PromptTokens

    @property
    def CompletionTokens(self):
        r"""输出token数
        :rtype: int
        """
        return self._CompletionTokens

    @CompletionTokens.setter
    def CompletionTokens(self, CompletionTokens):
        self._CompletionTokens = CompletionTokens

    @property
    def TotalTokens(self):
        r"""总token数
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
        


class Choice(AbstractModel):
    r"""返回的回复, 支持多个

    """

    def __init__(self):
        r"""
        :param _FinishReason: 结束标志位，可能为 stop、 content_filter。
stop 表示输出正常结束。
content_filter 只在开启流式输出审核时会出现，表示安全审核未通过。
        :type FinishReason: str
        :param _Delta: 增量返回值，流式调用时使用该字段。
        :type Delta: :class:`tencentcloud.lkeap.v20240522.models.Delta`
        :param _Message: 返回值，非流式调用时使用该字段。
        :type Message: :class:`tencentcloud.lkeap.v20240522.models.Message`
        :param _Index: 索引值，流式调用时使用该字段。
        :type Index: int
        """
        self._FinishReason = None
        self._Delta = None
        self._Message = None
        self._Index = None

    @property
    def FinishReason(self):
        r"""结束标志位，可能为 stop、 content_filter。
stop 表示输出正常结束。
content_filter 只在开启流式输出审核时会出现，表示安全审核未通过。
        :rtype: str
        """
        return self._FinishReason

    @FinishReason.setter
    def FinishReason(self, FinishReason):
        self._FinishReason = FinishReason

    @property
    def Delta(self):
        r"""增量返回值，流式调用时使用该字段。
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.Delta`
        """
        return self._Delta

    @Delta.setter
    def Delta(self, Delta):
        self._Delta = Delta

    @property
    def Message(self):
        r"""返回值，非流式调用时使用该字段。
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.Message`
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Index(self):
        r"""索引值，流式调用时使用该字段。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._FinishReason = params.get("FinishReason")
        if params.get("Delta") is not None:
            self._Delta = Delta()
            self._Delta._deserialize(params.get("Delta"))
        if params.get("Message") is not None:
            self._Message = Message()
            self._Message._deserialize(params.get("Message"))
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReconstructDocumentFlowConfig(AbstractModel):
    r"""创建智能文档解析任务的配置信息

    """

    def __init__(self):
        r"""
        :param _TableResultType: <p>Markdown文件中表格返回的形式<br>0，表格以MD形式返回<br>1，表格以HTML形式返回<br>默认为0</p>
        :type TableResultType: str
        :param _ResultType: <p>智能文档解析返回结果的格式<br>0：只返回全文MD；<br>1：只返回每一页的OCR原始Json；<br>2：只返回每一页的MD，<br>3：返回全文MD + 每一页的OCR原始Json；<br>4：返回全文MD + 每一页的MD<br>5: 返回全文md，每一页ocr原始json，每一页md<br>默认值为0</p>
        :type ResultType: str
        :param _IgnoreFailedPage: <p>是否忽略失败页，返回已成功的页数据。默认为true。</p>
        :type IgnoreFailedPage: bool
        :param _ReturnPageFormat: <p>Markdown文件中是否包含页码信息</p>
        :type ReturnPageFormat: bool
        :param _PageFormat: <p>自定义输出页码样式,{{p}}为页码占位符，开启ReturnPageFormat生效。未填默认样式:<page_num>page {{p}}</page_num></p>
        :type PageFormat: str
        """
        self._TableResultType = None
        self._ResultType = None
        self._IgnoreFailedPage = None
        self._ReturnPageFormat = None
        self._PageFormat = None

    @property
    def TableResultType(self):
        r"""<p>Markdown文件中表格返回的形式<br>0，表格以MD形式返回<br>1，表格以HTML形式返回<br>默认为0</p>
        :rtype: str
        """
        return self._TableResultType

    @TableResultType.setter
    def TableResultType(self, TableResultType):
        self._TableResultType = TableResultType

    @property
    def ResultType(self):
        r"""<p>智能文档解析返回结果的格式<br>0：只返回全文MD；<br>1：只返回每一页的OCR原始Json；<br>2：只返回每一页的MD，<br>3：返回全文MD + 每一页的OCR原始Json；<br>4：返回全文MD + 每一页的MD<br>5: 返回全文md，每一页ocr原始json，每一页md<br>默认值为0</p>
        :rtype: str
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        self._ResultType = ResultType

    @property
    def IgnoreFailedPage(self):
        r"""<p>是否忽略失败页，返回已成功的页数据。默认为true。</p>
        :rtype: bool
        """
        return self._IgnoreFailedPage

    @IgnoreFailedPage.setter
    def IgnoreFailedPage(self, IgnoreFailedPage):
        self._IgnoreFailedPage = IgnoreFailedPage

    @property
    def ReturnPageFormat(self):
        r"""<p>Markdown文件中是否包含页码信息</p>
        :rtype: bool
        """
        return self._ReturnPageFormat

    @ReturnPageFormat.setter
    def ReturnPageFormat(self, ReturnPageFormat):
        self._ReturnPageFormat = ReturnPageFormat

    @property
    def PageFormat(self):
        r"""<p>自定义输出页码样式,{{p}}为页码占位符，开启ReturnPageFormat生效。未填默认样式:<page_num>page {{p}}</page_num></p>
        :rtype: str
        """
        return self._PageFormat

    @PageFormat.setter
    def PageFormat(self, PageFormat):
        self._PageFormat = PageFormat


    def _deserialize(self, params):
        self._TableResultType = params.get("TableResultType")
        self._ResultType = params.get("ResultType")
        self._IgnoreFailedPage = params.get("IgnoreFailedPage")
        self._ReturnPageFormat = params.get("ReturnPageFormat")
        self._PageFormat = params.get("PageFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReconstructDocumentFlowRequest(AbstractModel):
    r"""CreateReconstructDocumentFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileType: 文件类型。**支持的文件类型：**- `WPS、PDF`、`DOC`、`DOCX`、`XLS`、`XLSX`、`PPT`、`PPTX`、`MD`、`TXT`、`PNG`、`JPG`、`JPEG`、`CSV`、`HTML`、`EPUB`、`BMP`、`GIF`、`WEBP`、`HEIC`、`EPS`、`ICNS`、`IM`、`PCX`、`PPM`、`TIFF`、`XBM`、`HEIF`、`JP2`**支持的文件大小：** - `PDF` 最大300M - `WPS`、`DOCX`、`DOC`、`PPT`、`PPTX` 最大 200M - `TXT`、`MD` 最大10M - 其他 最大20M
        :type FileType: str
        :param _FileUrl: 说明：文件的 URL 地址。
备注：文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 URL 速度和稳定性可能受一定影响。
参考：[腾讯云COS文档](https://cloud.tencent.com/document/product/436/7749)
        :type FileUrl: str
        :param _FileBase64: 文件的 Base64 值。
支持的文件类型： PNG、JPG、JPEG、PDF、GIF、BMP、TIFF
支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过 3 秒。
支持的图片像素：单边介于20-10000px之间。
文件的 FileUrl、FileBase64 必须提供一个，如果都提供，只使用 FileUrl。
        :type FileBase64: str
        :param _FileStartPageNumber: 说明：文档的起始页码。
备注：当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的起始页码，识别的页码包含当前值。
默认值：无
        :type FileStartPageNumber: int
        :param _FileEndPageNumber: 说明：文档的结束页码。
备注：当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的结束页码，识别的页码包含当前值。
默认值：无
        :type FileEndPageNumber: int
        :param _Config: 说明：创建文档解析任务配置信息。
备注：可设置结果的返回格式
默认值：无
        :type Config: :class:`tencentcloud.lkeap.v20240522.models.CreateReconstructDocumentFlowConfig`
        """
        self._FileType = None
        self._FileUrl = None
        self._FileBase64 = None
        self._FileStartPageNumber = None
        self._FileEndPageNumber = None
        self._Config = None

    @property
    def FileType(self):
        r"""文件类型。**支持的文件类型：**- `WPS、PDF`、`DOC`、`DOCX`、`XLS`、`XLSX`、`PPT`、`PPTX`、`MD`、`TXT`、`PNG`、`JPG`、`JPEG`、`CSV`、`HTML`、`EPUB`、`BMP`、`GIF`、`WEBP`、`HEIC`、`EPS`、`ICNS`、`IM`、`PCX`、`PPM`、`TIFF`、`XBM`、`HEIF`、`JP2`**支持的文件大小：** - `PDF` 最大300M - `WPS`、`DOCX`、`DOC`、`PPT`、`PPTX` 最大 200M - `TXT`、`MD` 最大10M - 其他 最大20M
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileUrl(self):
        r"""说明：文件的 URL 地址。
备注：文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 URL 速度和稳定性可能受一定影响。
参考：[腾讯云COS文档](https://cloud.tencent.com/document/product/436/7749)
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileBase64(self):
        r"""文件的 Base64 值。
支持的文件类型： PNG、JPG、JPEG、PDF、GIF、BMP、TIFF
支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过 3 秒。
支持的图片像素：单边介于20-10000px之间。
文件的 FileUrl、FileBase64 必须提供一个，如果都提供，只使用 FileUrl。
        :rtype: str
        """
        return self._FileBase64

    @FileBase64.setter
    def FileBase64(self, FileBase64):
        self._FileBase64 = FileBase64

    @property
    def FileStartPageNumber(self):
        r"""说明：文档的起始页码。
备注：当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的起始页码，识别的页码包含当前值。
默认值：无
        :rtype: int
        """
        return self._FileStartPageNumber

    @FileStartPageNumber.setter
    def FileStartPageNumber(self, FileStartPageNumber):
        self._FileStartPageNumber = FileStartPageNumber

    @property
    def FileEndPageNumber(self):
        r"""说明：文档的结束页码。
备注：当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的结束页码，识别的页码包含当前值。
默认值：无
        :rtype: int
        """
        return self._FileEndPageNumber

    @FileEndPageNumber.setter
    def FileEndPageNumber(self, FileEndPageNumber):
        self._FileEndPageNumber = FileEndPageNumber

    @property
    def Config(self):
        r"""说明：创建文档解析任务配置信息。
备注：可设置结果的返回格式
默认值：无
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.CreateReconstructDocumentFlowConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileUrl = params.get("FileUrl")
        self._FileBase64 = params.get("FileBase64")
        self._FileStartPageNumber = params.get("FileStartPageNumber")
        self._FileEndPageNumber = params.get("FileEndPageNumber")
        if params.get("Config") is not None:
            self._Config = CreateReconstructDocumentFlowConfig()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReconstructDocumentFlowResponse(AbstractModel):
    r"""CreateReconstructDocumentFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务唯一id。30天内可以通过GetReconstructDocumentResult接口查询TaskId对应的处理结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务唯一id。30天内可以通过GetReconstructDocumentResult接口查询TaskId对应的处理结果。
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


class CreateSplitDocumentFlowConfig(AbstractModel):
    r"""创建智能文档拆分任务的配置信息

    """

    def __init__(self):
        r"""
        :param _TableResultType: <p>Markdown文件中表格返回的形式<br>0，表格以MD形式返回<br>1，表格以HTML形式返回<br>默认为</p>
        :type TableResultType: str
        :param _ResultType: <p>智能文档解析返回结果的格式<br>0：只返回全文MD；<br>1：只返回每一页的OCR原始Json；<br>2：只返回每一页的MD；<br>3：返回全文MD + 每一页的OCR原始Json；<br>4：返回全文MD + 每一页的MD；<br>5：返回全文md，每一页ocr原始json，每一页md。</p>
        :type ResultType: str
        :param _EnableMllm: <p>是否开启mllm</p>
        :type EnableMllm: bool
        :param _MaxChunkSize: <p>最大分片长度</p>
        :type MaxChunkSize: int
        :param _IgnoreFailedPage: <p>是否忽略返回失败页码</p>
        :type IgnoreFailedPage: bool
        :param _SplitResultType: <p>智能文档解析返回结果的格式<br>0：只返回全文MD；<br>1：只返回每一页的OCR原始Json；<br>2：只返回每一页的MD；<br>3：返回全文MD + 每一页的OCR原始Json；<br>4：返回全文MD + 每一页的MD；<br>5：返回全文md，每一页ocr原始json，每一页md。</p>
        :type SplitResultType: str
        :param _SplitTableResultType: <p>Markdown文件中表格返回的形式<br>0，表格以MD形式返回<br>1，表格以HTML形式返回<br>默认为</p>
        :type SplitTableResultType: str
        :param _ReturnPageFormat: <p>Markdown文件中是否包含页码信息</p>
        :type ReturnPageFormat: bool
        :param _PageFormat: <p>自定义输出页码样式,{{p}}为页码占位符，开启ReturnPageFormat生效。未填默认样式:<page_num>page {{p}}</page_num></p>
        :type PageFormat: str
        """
        self._TableResultType = None
        self._ResultType = None
        self._EnableMllm = None
        self._MaxChunkSize = None
        self._IgnoreFailedPage = None
        self._SplitResultType = None
        self._SplitTableResultType = None
        self._ReturnPageFormat = None
        self._PageFormat = None

    @property
    def TableResultType(self):
        warnings.warn("parameter `TableResultType` is deprecated", DeprecationWarning) 

        r"""<p>Markdown文件中表格返回的形式<br>0，表格以MD形式返回<br>1，表格以HTML形式返回<br>默认为</p>
        :rtype: str
        """
        return self._TableResultType

    @TableResultType.setter
    def TableResultType(self, TableResultType):
        warnings.warn("parameter `TableResultType` is deprecated", DeprecationWarning) 

        self._TableResultType = TableResultType

    @property
    def ResultType(self):
        warnings.warn("parameter `ResultType` is deprecated", DeprecationWarning) 

        r"""<p>智能文档解析返回结果的格式<br>0：只返回全文MD；<br>1：只返回每一页的OCR原始Json；<br>2：只返回每一页的MD；<br>3：返回全文MD + 每一页的OCR原始Json；<br>4：返回全文MD + 每一页的MD；<br>5：返回全文md，每一页ocr原始json，每一页md。</p>
        :rtype: str
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        warnings.warn("parameter `ResultType` is deprecated", DeprecationWarning) 

        self._ResultType = ResultType

    @property
    def EnableMllm(self):
        r"""<p>是否开启mllm</p>
        :rtype: bool
        """
        return self._EnableMllm

    @EnableMllm.setter
    def EnableMllm(self, EnableMllm):
        self._EnableMllm = EnableMllm

    @property
    def MaxChunkSize(self):
        r"""<p>最大分片长度</p>
        :rtype: int
        """
        return self._MaxChunkSize

    @MaxChunkSize.setter
    def MaxChunkSize(self, MaxChunkSize):
        self._MaxChunkSize = MaxChunkSize

    @property
    def IgnoreFailedPage(self):
        r"""<p>是否忽略返回失败页码</p>
        :rtype: bool
        """
        return self._IgnoreFailedPage

    @IgnoreFailedPage.setter
    def IgnoreFailedPage(self, IgnoreFailedPage):
        self._IgnoreFailedPage = IgnoreFailedPage

    @property
    def SplitResultType(self):
        r"""<p>智能文档解析返回结果的格式<br>0：只返回全文MD；<br>1：只返回每一页的OCR原始Json；<br>2：只返回每一页的MD；<br>3：返回全文MD + 每一页的OCR原始Json；<br>4：返回全文MD + 每一页的MD；<br>5：返回全文md，每一页ocr原始json，每一页md。</p>
        :rtype: str
        """
        return self._SplitResultType

    @SplitResultType.setter
    def SplitResultType(self, SplitResultType):
        self._SplitResultType = SplitResultType

    @property
    def SplitTableResultType(self):
        r"""<p>Markdown文件中表格返回的形式<br>0，表格以MD形式返回<br>1，表格以HTML形式返回<br>默认为</p>
        :rtype: str
        """
        return self._SplitTableResultType

    @SplitTableResultType.setter
    def SplitTableResultType(self, SplitTableResultType):
        self._SplitTableResultType = SplitTableResultType

    @property
    def ReturnPageFormat(self):
        r"""<p>Markdown文件中是否包含页码信息</p>
        :rtype: bool
        """
        return self._ReturnPageFormat

    @ReturnPageFormat.setter
    def ReturnPageFormat(self, ReturnPageFormat):
        self._ReturnPageFormat = ReturnPageFormat

    @property
    def PageFormat(self):
        r"""<p>自定义输出页码样式,{{p}}为页码占位符，开启ReturnPageFormat生效。未填默认样式:<page_num>page {{p}}</page_num></p>
        :rtype: str
        """
        return self._PageFormat

    @PageFormat.setter
    def PageFormat(self, PageFormat):
        self._PageFormat = PageFormat


    def _deserialize(self, params):
        self._TableResultType = params.get("TableResultType")
        self._ResultType = params.get("ResultType")
        self._EnableMllm = params.get("EnableMllm")
        self._MaxChunkSize = params.get("MaxChunkSize")
        self._IgnoreFailedPage = params.get("IgnoreFailedPage")
        self._SplitResultType = params.get("SplitResultType")
        self._SplitTableResultType = params.get("SplitTableResultType")
        self._ReturnPageFormat = params.get("ReturnPageFormat")
        self._PageFormat = params.get("PageFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSplitDocumentFlowRequest(AbstractModel):
    r"""CreateSplitDocumentFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileType: 文件类型。**支持的文件类型：**- `WPS`、`PDF`、`DOC`、`DOCX`、`XLS`、`XLSX`、`PPT`、`PPTX`、`MD`、`TXT`、`PNG`、`JPG`、`JPEG`、`CSV`、`HTML`、`EPUB`**支持的文件大小：** - `PDF` 最大300M - `WPS`、`DOCX`、`DOC`、`PPT`、`PPTX` 最大 200M - `TXT`、`MD` 最大10M - 其他 最大20M
        :type FileType: str
        :param _FileUrl: 文件的 URL 地址。
文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 URL 速度和稳定性可能受一定影响。
参考：[腾讯云COS文档](https://cloud.tencent.com/document/product/436/7749)
        :type FileUrl: str
        :param _FileName: 文件名，可选。
**需带文件类型后缀**，当文件名无法从传入的`FileUrl`获取时需要通过该字段来明确。
        :type FileName: str
        :param _FileBase64: 文件的 Base64 值。
支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过 3 秒。
支持的图片像素：单边介于20-10000px之间。
文件的 FileUrl、FileBase64 必须提供一个，如果都提供，只使用 FileUrl。
        :type FileBase64: str
        :param _FileStartPageNumber: 文档的起始页码。
当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的起始页码，识别的页码包含当前值。
        :type FileStartPageNumber: int
        :param _FileEndPageNumber: 文档的结束页码。
当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的结束页码，识别的页码包含当前值。
        :type FileEndPageNumber: int
        :param _Config: 文档拆分任务的配置信息。

        :type Config: :class:`tencentcloud.lkeap.v20240522.models.CreateSplitDocumentFlowConfig`
        """
        self._FileType = None
        self._FileUrl = None
        self._FileName = None
        self._FileBase64 = None
        self._FileStartPageNumber = None
        self._FileEndPageNumber = None
        self._Config = None

    @property
    def FileType(self):
        r"""文件类型。**支持的文件类型：**- `WPS`、`PDF`、`DOC`、`DOCX`、`XLS`、`XLSX`、`PPT`、`PPTX`、`MD`、`TXT`、`PNG`、`JPG`、`JPEG`、`CSV`、`HTML`、`EPUB`**支持的文件大小：** - `PDF` 最大300M - `WPS`、`DOCX`、`DOC`、`PPT`、`PPTX` 最大 200M - `TXT`、`MD` 最大10M - 其他 最大20M
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileUrl(self):
        r"""文件的 URL 地址。
文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 URL 速度和稳定性可能受一定影响。
参考：[腾讯云COS文档](https://cloud.tencent.com/document/product/436/7749)
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileName(self):
        r"""文件名，可选。
**需带文件类型后缀**，当文件名无法从传入的`FileUrl`获取时需要通过该字段来明确。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileBase64(self):
        warnings.warn("parameter `FileBase64` is deprecated", DeprecationWarning) 

        r"""文件的 Base64 值。
支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过 3 秒。
支持的图片像素：单边介于20-10000px之间。
文件的 FileUrl、FileBase64 必须提供一个，如果都提供，只使用 FileUrl。
        :rtype: str
        """
        return self._FileBase64

    @FileBase64.setter
    def FileBase64(self, FileBase64):
        warnings.warn("parameter `FileBase64` is deprecated", DeprecationWarning) 

        self._FileBase64 = FileBase64

    @property
    def FileStartPageNumber(self):
        r"""文档的起始页码。
当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的起始页码，识别的页码包含当前值。
        :rtype: int
        """
        return self._FileStartPageNumber

    @FileStartPageNumber.setter
    def FileStartPageNumber(self, FileStartPageNumber):
        self._FileStartPageNumber = FileStartPageNumber

    @property
    def FileEndPageNumber(self):
        r"""文档的结束页码。
当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的结束页码，识别的页码包含当前值。
        :rtype: int
        """
        return self._FileEndPageNumber

    @FileEndPageNumber.setter
    def FileEndPageNumber(self, FileEndPageNumber):
        self._FileEndPageNumber = FileEndPageNumber

    @property
    def Config(self):
        r"""文档拆分任务的配置信息。

        :rtype: :class:`tencentcloud.lkeap.v20240522.models.CreateSplitDocumentFlowConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileUrl = params.get("FileUrl")
        self._FileName = params.get("FileName")
        self._FileBase64 = params.get("FileBase64")
        self._FileStartPageNumber = params.get("FileStartPageNumber")
        self._FileEndPageNumber = params.get("FileEndPageNumber")
        if params.get("Config") is not None:
            self._Config = CreateSplitDocumentFlowConfig()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSplitDocumentFlowResponse(AbstractModel):
    r"""CreateSplitDocumentFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 拆分任务唯一ID。
30天内可以通过`GetSplitDocumentResult`接口查询TaskId对应的拆分结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""拆分任务唯一ID。
30天内可以通过`GetSplitDocumentResult`接口查询TaskId对应的拆分结果。
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


class Delta(AbstractModel):
    r"""返回的内容

    """

    def __init__(self):
        r"""
        :param _Role: 角色名称。
        :type Role: str
        :param _Content: 内容详情。
        :type Content: str
        :param _ReasoningContent: 思维链内容。 ReasoningConent参数仅支持出参，且只有deepseek-r1模型会返回。
        :type ReasoningContent: str
        """
        self._Role = None
        self._Content = None
        self._ReasoningContent = None

    @property
    def Role(self):
        r"""角色名称。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        r"""内容详情。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ReasoningContent(self):
        r"""思维链内容。 ReasoningConent参数仅支持出参，且只有deepseek-r1模型会返回。
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
        


class DocumentUsage(AbstractModel):
    r"""文档拆分任务的用量

    """

    def __init__(self):
        r"""
        :param _PageNumber: 文档拆分任务的页数
        :type PageNumber: int
        :param _TotalToken: 文档拆分任务消耗的总token数
        :type TotalToken: int
        :param _TotalTokens: 文档拆分任务消耗的总token数
        :type TotalTokens: int
        :param _SplitTokens: 拆分消耗的token数
        :type SplitTokens: int
        :param _MllmTokens: mllm消耗的token数
        :type MllmTokens: int
        :param _SuccessPageNum: 解析成功页数
        :type SuccessPageNum: int
        :param _FailPageNum: 解析失败页数
        :type FailPageNum: int
        :param _FileSize: 文件大小，单位：字节
        :type FileSize: int
        """
        self._PageNumber = None
        self._TotalToken = None
        self._TotalTokens = None
        self._SplitTokens = None
        self._MllmTokens = None
        self._SuccessPageNum = None
        self._FailPageNum = None
        self._FileSize = None

    @property
    def PageNumber(self):
        r"""文档拆分任务的页数
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def TotalToken(self):
        warnings.warn("parameter `TotalToken` is deprecated", DeprecationWarning) 

        r"""文档拆分任务消耗的总token数
        :rtype: int
        """
        return self._TotalToken

    @TotalToken.setter
    def TotalToken(self, TotalToken):
        warnings.warn("parameter `TotalToken` is deprecated", DeprecationWarning) 

        self._TotalToken = TotalToken

    @property
    def TotalTokens(self):
        r"""文档拆分任务消耗的总token数
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens

    @property
    def SplitTokens(self):
        r"""拆分消耗的token数
        :rtype: int
        """
        return self._SplitTokens

    @SplitTokens.setter
    def SplitTokens(self, SplitTokens):
        self._SplitTokens = SplitTokens

    @property
    def MllmTokens(self):
        r"""mllm消耗的token数
        :rtype: int
        """
        return self._MllmTokens

    @MllmTokens.setter
    def MllmTokens(self, MllmTokens):
        self._MllmTokens = MllmTokens

    @property
    def SuccessPageNum(self):
        r"""解析成功页数
        :rtype: int
        """
        return self._SuccessPageNum

    @SuccessPageNum.setter
    def SuccessPageNum(self, SuccessPageNum):
        self._SuccessPageNum = SuccessPageNum

    @property
    def FailPageNum(self):
        r"""解析失败页数
        :rtype: int
        """
        return self._FailPageNum

    @FailPageNum.setter
    def FailPageNum(self, FailPageNum):
        self._FailPageNum = FailPageNum

    @property
    def FileSize(self):
        r"""文件大小，单位：字节
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._TotalToken = params.get("TotalToken")
        self._TotalTokens = params.get("TotalTokens")
        self._SplitTokens = params.get("SplitTokens")
        self._MllmTokens = params.get("MllmTokens")
        self._SuccessPageNum = params.get("SuccessPageNum")
        self._FailPageNum = params.get("FailPageNum")
        self._FileSize = params.get("FileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmbeddingObject(AbstractModel):
    r"""向量

    """

    def __init__(self):
        r"""
        :param _Embedding: 向量
        :type Embedding: list of float
        """
        self._Embedding = None

    @property
    def Embedding(self):
        r"""向量
        :rtype: list of float
        """
        return self._Embedding

    @Embedding.setter
    def Embedding(self, Embedding):
        self._Embedding = Embedding


    def _deserialize(self, params):
        self._Embedding = params.get("Embedding")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorInfo(AbstractModel):
    r"""错误信息

    """

    def __init__(self):
        r"""
        :param _Code: 错误码
        :type Code: str
        :param _Message: 错误信息
        :type Message: str
        """
        self._Code = None
        self._Message = None

    @property
    def Code(self):
        r"""错误码
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

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
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCharacterUsageRequest(AbstractModel):
    r"""GetCharacterUsage请求参数结构体

    """


class GetCharacterUsageResponse(AbstractModel):
    r"""GetCharacterUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Used: 已用字符数
        :type Used: int
        :param _Total: 可用字符数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Used = None
        self._Total = None
        self._RequestId = None

    @property
    def Used(self):
        r"""已用字符数
        :rtype: int
        """
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used

    @property
    def Total(self):
        r"""可用字符数
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
        self._Used = params.get("Used")
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetEmbeddingRequest(AbstractModel):
    r"""GetEmbedding请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Model: <p>说明：选择生成向量的模型</p><p>枚举值：</p><ul><li>lke-text-embedding-v1： 文本embedding v1</li><li>lke-text-embedding-v2： 文本embedding v2</li></ul>
        :type Model: str
        :param _Inputs: <p>说明：需要 embedding 的文本<br>备注：单条query最多2000个字符，总条数最多7条</p>
        :type Inputs: list of str
        :param _TextType: <p>说明：文本向量化的类型，为使得检索任务有更好的检索效果，建议区分查询文本（query）和文档文本（document）类型, 聚类、分类等对称任务可以不用特殊指定，采用系统默认值document即可。</p>
        :type TextType: str
        :param _Instruction: <p>说明：自定义任务指令词，当且仅当TextType=query且Model为lke-text-embedding-v1时，生效</p>
        :type Instruction: str
        """
        self._Model = None
        self._Inputs = None
        self._TextType = None
        self._Instruction = None

    @property
    def Model(self):
        r"""<p>说明：选择生成向量的模型</p><p>枚举值：</p><ul><li>lke-text-embedding-v1： 文本embedding v1</li><li>lke-text-embedding-v2： 文本embedding v2</li></ul>
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Inputs(self):
        r"""<p>说明：需要 embedding 的文本<br>备注：单条query最多2000个字符，总条数最多7条</p>
        :rtype: list of str
        """
        return self._Inputs

    @Inputs.setter
    def Inputs(self, Inputs):
        self._Inputs = Inputs

    @property
    def TextType(self):
        r"""<p>说明：文本向量化的类型，为使得检索任务有更好的检索效果，建议区分查询文本（query）和文档文本（document）类型, 聚类、分类等对称任务可以不用特殊指定，采用系统默认值document即可。</p>
        :rtype: str
        """
        return self._TextType

    @TextType.setter
    def TextType(self, TextType):
        self._TextType = TextType

    @property
    def Instruction(self):
        r"""<p>说明：自定义任务指令词，当且仅当TextType=query且Model为lke-text-embedding-v1时，生效</p>
        :rtype: str
        """
        return self._Instruction

    @Instruction.setter
    def Instruction(self, Instruction):
        self._Instruction = Instruction


    def _deserialize(self, params):
        self._Model = params.get("Model")
        self._Inputs = params.get("Inputs")
        self._TextType = params.get("TextType")
        self._Instruction = params.get("Instruction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEmbeddingResponse(AbstractModel):
    r"""GetEmbedding返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>特征</p>
        :type Data: list of EmbeddingObject
        :param _Usage: <p>消耗量，返回TotalToken</p>
        :type Usage: :class:`tencentcloud.lkeap.v20240522.models.Usage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Usage = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>特征</p>
        :rtype: list of EmbeddingObject
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Usage(self):
        r"""<p>消耗量，返回TotalToken</p>
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.Usage`
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
                obj = EmbeddingObject()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class GetReconstructDocumentResultRequest(AbstractModel):
    r"""GetReconstructDocumentResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 说明：解析任务ID
备注：仅支持单个任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""说明：解析任务ID
备注：仅支持单个任务ID
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
        


class GetReconstructDocumentResultResponse(AbstractModel):
    r"""GetReconstructDocumentResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。
- `Success`：执行完成
- `Processing`：执行中
-  `Pause`: 暂停
-  `Failed`：执行失败
-  `WaitExecute`：等待执行
        :type Status: str
        :param _DocumentRecognizeResultUrl: 解析结果的临时下载地址。文件类型为zip压缩包，下载链接有效期30分钟
        :type DocumentRecognizeResultUrl: str
        :param _FailedPages: 文档解析失败的页码
        :type FailedPages: list of ReconstructDocumentFailedPage
        :param _Usage: 文档拆分任务的用量	
        :type Usage: :class:`tencentcloud.lkeap.v20240522.models.DocumentUsage`
        :param _Error: 文档解析任务失败错误信息，当文档解析任务失败会返回具体的错误信息
        :type Error: :class:`tencentcloud.lkeap.v20240522.models.ErrorInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._DocumentRecognizeResultUrl = None
        self._FailedPages = None
        self._Usage = None
        self._Error = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。
- `Success`：执行完成
- `Processing`：执行中
-  `Pause`: 暂停
-  `Failed`：执行失败
-  `WaitExecute`：等待执行
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DocumentRecognizeResultUrl(self):
        r"""解析结果的临时下载地址。文件类型为zip压缩包，下载链接有效期30分钟
        :rtype: str
        """
        return self._DocumentRecognizeResultUrl

    @DocumentRecognizeResultUrl.setter
    def DocumentRecognizeResultUrl(self, DocumentRecognizeResultUrl):
        self._DocumentRecognizeResultUrl = DocumentRecognizeResultUrl

    @property
    def FailedPages(self):
        r"""文档解析失败的页码
        :rtype: list of ReconstructDocumentFailedPage
        """
        return self._FailedPages

    @FailedPages.setter
    def FailedPages(self, FailedPages):
        self._FailedPages = FailedPages

    @property
    def Usage(self):
        r"""文档拆分任务的用量	
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.DocumentUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Error(self):
        r"""文档解析任务失败错误信息，当文档解析任务失败会返回具体的错误信息
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.ErrorInfo`
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

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
        self._DocumentRecognizeResultUrl = params.get("DocumentRecognizeResultUrl")
        if params.get("FailedPages") is not None:
            self._FailedPages = []
            for item in params.get("FailedPages"):
                obj = ReconstructDocumentFailedPage()
                obj._deserialize(item)
                self._FailedPages.append(obj)
        if params.get("Usage") is not None:
            self._Usage = DocumentUsage()
            self._Usage._deserialize(params.get("Usage"))
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        self._RequestId = params.get("RequestId")


class GetSplitDocumentResultRequest(AbstractModel):
    r"""GetSplitDocumentResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 拆分任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""拆分任务ID
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
        


class GetSplitDocumentResultResponse(AbstractModel):
    r"""GetSplitDocumentResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。

- `Success`：执行完成
- `Processing`：执行中
- `Pause`: 暂停
- `Failed`：执行失败
- `WaitExecute`：等待执行
        :type Status: str
        :param _DocumentRecognizeResultUrl: 拆分结果的临时下载地址。
文件类型为zip压缩包，下载链接有效期30分钟。
压缩包内包含\*.md、\*.jsonl、\*mllm.json以及images文件夹。

> **jsonl** 结构说明：
- `page_content`:
 用于生成嵌入（embedding）库，以便于检索使用。该字段中的图片将使用占位符替换。
- `org_data`:
 表示与 page_content 对应的最小语义完整性块，用于问答模型的处理。
- `big_data`:
 表示与 page_content 对应的最大语义完整性块，也用于问答模型的处理。
        :type DocumentRecognizeResultUrl: str
        :param _FailedPages: 文档拆分失败的页码
        :type FailedPages: list of SplitDocumentFailedPage
        :param _Usage: 文档拆分任务的用量
        :type Usage: :class:`tencentcloud.lkeap.v20240522.models.DocumentUsage`
        :param _Error: 文档拆分失败的错误信息，当拆分任务失败时返回该错误信息
        :type Error: :class:`tencentcloud.lkeap.v20240522.models.ErrorInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._DocumentRecognizeResultUrl = None
        self._FailedPages = None
        self._Usage = None
        self._Error = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。

- `Success`：执行完成
- `Processing`：执行中
- `Pause`: 暂停
- `Failed`：执行失败
- `WaitExecute`：等待执行
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DocumentRecognizeResultUrl(self):
        r"""拆分结果的临时下载地址。
文件类型为zip压缩包，下载链接有效期30分钟。
压缩包内包含\*.md、\*.jsonl、\*mllm.json以及images文件夹。

> **jsonl** 结构说明：
- `page_content`:
 用于生成嵌入（embedding）库，以便于检索使用。该字段中的图片将使用占位符替换。
- `org_data`:
 表示与 page_content 对应的最小语义完整性块，用于问答模型的处理。
- `big_data`:
 表示与 page_content 对应的最大语义完整性块，也用于问答模型的处理。
        :rtype: str
        """
        return self._DocumentRecognizeResultUrl

    @DocumentRecognizeResultUrl.setter
    def DocumentRecognizeResultUrl(self, DocumentRecognizeResultUrl):
        self._DocumentRecognizeResultUrl = DocumentRecognizeResultUrl

    @property
    def FailedPages(self):
        warnings.warn("parameter `FailedPages` is deprecated", DeprecationWarning) 

        r"""文档拆分失败的页码
        :rtype: list of SplitDocumentFailedPage
        """
        return self._FailedPages

    @FailedPages.setter
    def FailedPages(self, FailedPages):
        warnings.warn("parameter `FailedPages` is deprecated", DeprecationWarning) 

        self._FailedPages = FailedPages

    @property
    def Usage(self):
        r"""文档拆分任务的用量
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.DocumentUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Error(self):
        r"""文档拆分失败的错误信息，当拆分任务失败时返回该错误信息
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.ErrorInfo`
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

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
        self._DocumentRecognizeResultUrl = params.get("DocumentRecognizeResultUrl")
        if params.get("FailedPages") is not None:
            self._FailedPages = []
            for item in params.get("FailedPages"):
                obj = SplitDocumentFailedPage()
                obj._deserialize(item)
                self._FailedPages.append(obj)
        if params.get("Usage") is not None:
            self._Usage = DocumentUsage()
            self._Usage._deserialize(params.get("Usage"))
        if params.get("Error") is not None:
            self._Error = ErrorInfo()
            self._Error._deserialize(params.get("Error"))
        self._RequestId = params.get("RequestId")


class Message(AbstractModel):
    r"""会话内容

    """

    def __init__(self):
        r"""
        :param _Role: 角色
        :type Role: str
        :param _Content: 内容
        :type Content: str
        :param _ReasoningContent: 思维链内容。
ReasoningConent参数仅支持出参，且只有deepseek-r1模型会返回。
        :type ReasoningContent: str
        :param _SearchResults: 搜索结果
        :type SearchResults: list of SearchResult
        """
        self._Role = None
        self._Content = None
        self._ReasoningContent = None
        self._SearchResults = None

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
        r"""内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ReasoningContent(self):
        r"""思维链内容。
ReasoningConent参数仅支持出参，且只有deepseek-r1模型会返回。
        :rtype: str
        """
        return self._ReasoningContent

    @ReasoningContent.setter
    def ReasoningContent(self, ReasoningContent):
        self._ReasoningContent = ReasoningContent

    @property
    def SearchResults(self):
        r"""搜索结果
        :rtype: list of SearchResult
        """
        return self._SearchResults

    @SearchResults.setter
    def SearchResults(self, SearchResults):
        self._SearchResults = SearchResults


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        self._ReasoningContent = params.get("ReasoningContent")
        if params.get("SearchResults") is not None:
            self._SearchResults = []
            for item in params.get("SearchResults"):
                obj = SearchResult()
                obj._deserialize(item)
                self._SearchResults.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryRewriteRequest(AbstractModel):
    r"""QueryRewrite请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Messages: 说明：需要改写的多轮历史会话，每轮历史对话需要包含user（问）和assistant（答）成对输入
备注：由于模型字符限制，最多提供4轮对话。针对最后一轮对话进行改写。四轮对话最多包含3600个字符。
        :type Messages: list of Message
        :param _Model: 说明：模型名称
备注：仅一个模型可选
默认值：lke-query-rewrite-base
        :type Model: str
        """
        self._Messages = None
        self._Model = None

    @property
    def Messages(self):
        r"""说明：需要改写的多轮历史会话，每轮历史对话需要包含user（问）和assistant（答）成对输入
备注：由于模型字符限制，最多提供4轮对话。针对最后一轮对话进行改写。四轮对话最多包含3600个字符。
        :rtype: list of Message
        """
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def Model(self):
        r"""说明：模型名称
备注：仅一个模型可选
默认值：lke-query-rewrite-base
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model


    def _deserialize(self, params):
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = Message()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._Model = params.get("Model")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryRewriteResponse(AbstractModel):
    r"""QueryRewrite返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 改写结果
        :type Content: str
        :param _Usage: 消耗量，返回输入token数，输出token数以及总token数
        :type Usage: :class:`tencentcloud.lkeap.v20240522.models.Usage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Content = None
        self._Usage = None
        self._RequestId = None

    @property
    def Content(self):
        r"""改写结果
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Usage(self):
        r"""消耗量，返回输入token数，输出token数以及总token数
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.Usage`
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
        self._Content = params.get("Content")
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class ReconstructDocumentFailedPage(AbstractModel):
    r"""文档解析失败记录

    """

    def __init__(self):
        r"""
        :param _PageNumber: 失败页码	
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        """
        self._PageNumber = None

    @property
    def PageNumber(self):
        r"""失败页码	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReconstructDocumentSSEConfig(AbstractModel):
    r"""ReconstructDocumentSSE 功能配置参数

    """

    def __init__(self):
        r"""
        :param _TableResultType: Markdown文件中表格返回的形式
0，表格以MD形式返回
1，表格以HTML形式返回
默认为0
        :type TableResultType: str
        :param _MarkdownImageResponseType: Markdown文件中图片返回的形式
0:markdown中图片以链接形式返回
1:markdown中图片只返回图片中提取的文本内容
默认是0
        :type MarkdownImageResponseType: str
        :param _ReturnPageFormat: Markdown文件中是否包含页码信息
        :type ReturnPageFormat: bool
        :param _PageFormat: 自定义输出页码样式,{{p}}为页码占位符，开启ReturnPageFormat生效。未填默认样式:<page_num>page {{p}}</page_num>
        :type PageFormat: str
        :param _IgnoreFailedPage: 是否忽略失败页，返回已成功的页数据
        :type IgnoreFailedPage: bool
        """
        self._TableResultType = None
        self._MarkdownImageResponseType = None
        self._ReturnPageFormat = None
        self._PageFormat = None
        self._IgnoreFailedPage = None

    @property
    def TableResultType(self):
        r"""Markdown文件中表格返回的形式
0，表格以MD形式返回
1，表格以HTML形式返回
默认为0
        :rtype: str
        """
        return self._TableResultType

    @TableResultType.setter
    def TableResultType(self, TableResultType):
        self._TableResultType = TableResultType

    @property
    def MarkdownImageResponseType(self):
        r"""Markdown文件中图片返回的形式
0:markdown中图片以链接形式返回
1:markdown中图片只返回图片中提取的文本内容
默认是0
        :rtype: str
        """
        return self._MarkdownImageResponseType

    @MarkdownImageResponseType.setter
    def MarkdownImageResponseType(self, MarkdownImageResponseType):
        self._MarkdownImageResponseType = MarkdownImageResponseType

    @property
    def ReturnPageFormat(self):
        r"""Markdown文件中是否包含页码信息
        :rtype: bool
        """
        return self._ReturnPageFormat

    @ReturnPageFormat.setter
    def ReturnPageFormat(self, ReturnPageFormat):
        self._ReturnPageFormat = ReturnPageFormat

    @property
    def PageFormat(self):
        r"""自定义输出页码样式,{{p}}为页码占位符，开启ReturnPageFormat生效。未填默认样式:<page_num>page {{p}}</page_num>
        :rtype: str
        """
        return self._PageFormat

    @PageFormat.setter
    def PageFormat(self, PageFormat):
        self._PageFormat = PageFormat

    @property
    def IgnoreFailedPage(self):
        r"""是否忽略失败页，返回已成功的页数据
        :rtype: bool
        """
        return self._IgnoreFailedPage

    @IgnoreFailedPage.setter
    def IgnoreFailedPage(self, IgnoreFailedPage):
        self._IgnoreFailedPage = IgnoreFailedPage


    def _deserialize(self, params):
        self._TableResultType = params.get("TableResultType")
        self._MarkdownImageResponseType = params.get("MarkdownImageResponseType")
        self._ReturnPageFormat = params.get("ReturnPageFormat")
        self._PageFormat = params.get("PageFormat")
        self._IgnoreFailedPage = params.get("IgnoreFailedPage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReconstructDocumentSSERequest(AbstractModel):
    r"""ReconstructDocumentSSE请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileType: 支持解析的文件类型。**支持的文件类型**：WPS、PDF、DOC、DOCX、PPT、PPTX、MD、TXT、XLS、XLSX、CSV、PNG、JPG、JPEG、BMP、GIF、WEBP、HEIC、EPS、ICNS、IM、PCX、PPM、TIFF、XBM、HEIF、JP2**支持的文件大小**：- WPS、PDF、DOC、DOCX、PPT、PPTX 支持100M- MD、TXT、XLS、XLSX、CSV 支持10M- 其他支持20M
        :type FileType: str
        :param _FileUrl: 文件的 URL 地址。文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 URL 速度和稳定性可能受一定影响。文件的 FileUrl、FileBase64 必须提供一个，如果都提供，只使用 FileUrl。
参考：[腾讯云COS文档](https://cloud.tencent.com/document/product/436/7749)

默认值：无
        :type FileUrl: str
        :param _FileBase64: 说明：文件的 Base64 值。
备注：支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过 3 秒。
支持的图片像素：单边介于20-10000px之间。文件的 FileUrl、FileBase64 必须提供一个，如果都提供，只使用 FileUrl。

默认值：无
        :type FileBase64: str
        :param _FileStartPageNumber: 说明：文档的起始页码。
备注：当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的起始页码，识别的页码包含当前值。
默认值：无
        :type FileStartPageNumber: int
        :param _FileEndPageNumber: 说明：文档的结束页码。备注：当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的结束页码，识别的页码包含当前值，文档页码大于100页建议使用异步解析接入。默认值：无
        :type FileEndPageNumber: int
        :param _Config: 说明：文档解析配置信息	
备注：可设置返回markdown结果的格式
默认值：无

        :type Config: :class:`tencentcloud.lkeap.v20240522.models.ReconstructDocumentSSEConfig`
        """
        self._FileType = None
        self._FileUrl = None
        self._FileBase64 = None
        self._FileStartPageNumber = None
        self._FileEndPageNumber = None
        self._Config = None

    @property
    def FileType(self):
        r"""支持解析的文件类型。**支持的文件类型**：WPS、PDF、DOC、DOCX、PPT、PPTX、MD、TXT、XLS、XLSX、CSV、PNG、JPG、JPEG、BMP、GIF、WEBP、HEIC、EPS、ICNS、IM、PCX、PPM、TIFF、XBM、HEIF、JP2**支持的文件大小**：- WPS、PDF、DOC、DOCX、PPT、PPTX 支持100M- MD、TXT、XLS、XLSX、CSV 支持10M- 其他支持20M
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileUrl(self):
        r"""文件的 URL 地址。文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 URL 速度和稳定性可能受一定影响。文件的 FileUrl、FileBase64 必须提供一个，如果都提供，只使用 FileUrl。
参考：[腾讯云COS文档](https://cloud.tencent.com/document/product/436/7749)

默认值：无
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileBase64(self):
        r"""说明：文件的 Base64 值。
备注：支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过 3 秒。
支持的图片像素：单边介于20-10000px之间。文件的 FileUrl、FileBase64 必须提供一个，如果都提供，只使用 FileUrl。

默认值：无
        :rtype: str
        """
        return self._FileBase64

    @FileBase64.setter
    def FileBase64(self, FileBase64):
        self._FileBase64 = FileBase64

    @property
    def FileStartPageNumber(self):
        r"""说明：文档的起始页码。
备注：当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的起始页码，识别的页码包含当前值。
默认值：无
        :rtype: int
        """
        return self._FileStartPageNumber

    @FileStartPageNumber.setter
    def FileStartPageNumber(self, FileStartPageNumber):
        self._FileStartPageNumber = FileStartPageNumber

    @property
    def FileEndPageNumber(self):
        r"""说明：文档的结束页码。备注：当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的结束页码，识别的页码包含当前值，文档页码大于100页建议使用异步解析接入。默认值：无
        :rtype: int
        """
        return self._FileEndPageNumber

    @FileEndPageNumber.setter
    def FileEndPageNumber(self, FileEndPageNumber):
        self._FileEndPageNumber = FileEndPageNumber

    @property
    def Config(self):
        r"""说明：文档解析配置信息	
备注：可设置返回markdown结果的格式
默认值：无

        :rtype: :class:`tencentcloud.lkeap.v20240522.models.ReconstructDocumentSSEConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileUrl = params.get("FileUrl")
        self._FileBase64 = params.get("FileBase64")
        self._FileStartPageNumber = params.get("FileStartPageNumber")
        self._FileEndPageNumber = params.get("FileEndPageNumber")
        if params.get("Config") is not None:
            self._Config = ReconstructDocumentSSEConfig()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReconstructDocumentSSEResponse(AbstractModel):
    r"""ReconstructDocumentSSE返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。本次请求的唯一标识
        :type TaskId: str
        :param _ResponseType: 响应类型。1：返回进度信息， 2：返回解析结果
        :type ResponseType: str
        :param _Progress: 进度。0~100
        :type Progress: str
        :param _ProgressMessage: 进度信息。
        :type ProgressMessage: str
        :param _DocumentRecognizeResultUrl: 文档解析结果的临时下载地址。文件类型为zip压缩包，下载链接有效期30分钟。压缩包内包含*.md、*.json以及images文件夹。

        :type DocumentRecognizeResultUrl: str
        :param _FailedPages: 文档解析失败的页码。
        :type FailedPages: list of ReconstructDocumentFailedPage
        :param _FailPageNum: 文档解析失败页数
        :type FailPageNum: int
        :param _SuccessPageNum: 文档解析成功页数
        :type SuccessPageNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._TaskId = None
        self._ResponseType = None
        self._Progress = None
        self._ProgressMessage = None
        self._DocumentRecognizeResultUrl = None
        self._FailedPages = None
        self._FailPageNum = None
        self._SuccessPageNum = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。本次请求的唯一标识
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ResponseType(self):
        r"""响应类型。1：返回进度信息， 2：返回解析结果
        :rtype: str
        """
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def Progress(self):
        r"""进度。0~100
        :rtype: str
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def ProgressMessage(self):
        r"""进度信息。
        :rtype: str
        """
        return self._ProgressMessage

    @ProgressMessage.setter
    def ProgressMessage(self, ProgressMessage):
        self._ProgressMessage = ProgressMessage

    @property
    def DocumentRecognizeResultUrl(self):
        r"""文档解析结果的临时下载地址。文件类型为zip压缩包，下载链接有效期30分钟。压缩包内包含*.md、*.json以及images文件夹。

        :rtype: str
        """
        return self._DocumentRecognizeResultUrl

    @DocumentRecognizeResultUrl.setter
    def DocumentRecognizeResultUrl(self, DocumentRecognizeResultUrl):
        self._DocumentRecognizeResultUrl = DocumentRecognizeResultUrl

    @property
    def FailedPages(self):
        r"""文档解析失败的页码。
        :rtype: list of ReconstructDocumentFailedPage
        """
        return self._FailedPages

    @FailedPages.setter
    def FailedPages(self, FailedPages):
        self._FailedPages = FailedPages

    @property
    def FailPageNum(self):
        r"""文档解析失败页数
        :rtype: int
        """
        return self._FailPageNum

    @FailPageNum.setter
    def FailPageNum(self, FailPageNum):
        self._FailPageNum = FailPageNum

    @property
    def SuccessPageNum(self):
        r"""文档解析成功页数
        :rtype: int
        """
        return self._SuccessPageNum

    @SuccessPageNum.setter
    def SuccessPageNum(self, SuccessPageNum):
        self._SuccessPageNum = SuccessPageNum

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
        self._TaskId = params.get("TaskId")
        self._ResponseType = params.get("ResponseType")
        self._Progress = params.get("Progress")
        self._ProgressMessage = params.get("ProgressMessage")
        self._DocumentRecognizeResultUrl = params.get("DocumentRecognizeResultUrl")
        if params.get("FailedPages") is not None:
            self._FailedPages = []
            for item in params.get("FailedPages"):
                obj = ReconstructDocumentFailedPage()
                obj._deserialize(item)
                self._FailedPages.append(obj)
        self._FailPageNum = params.get("FailPageNum")
        self._SuccessPageNum = params.get("SuccessPageNum")
        self._RequestId = params.get("RequestId")


class RunRerankRequest(AbstractModel):
    r"""RunRerank请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Query: 说明：查询内容
备注：用于匹配的query
        :type Query: str
        :param _Docs: 说明：文档列表
备注：最多60个，Query字段和Docs字段的总长度上限为2000字符
        :type Docs: list of str
        :param _Model: 说明：模型名称
备注：仅一个模型可选
默认值：lke-reranker-base
        :type Model: str
        """
        self._Query = None
        self._Docs = None
        self._Model = None

    @property
    def Query(self):
        r"""说明：查询内容
备注：用于匹配的query
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Docs(self):
        r"""说明：文档列表
备注：最多60个，Query字段和Docs字段的总长度上限为2000字符
        :rtype: list of str
        """
        return self._Docs

    @Docs.setter
    def Docs(self, Docs):
        self._Docs = Docs

    @property
    def Model(self):
        r"""说明：模型名称
备注：仅一个模型可选
默认值：lke-reranker-base
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._Docs = params.get("Docs")
        self._Model = params.get("Model")
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
        :param _ScoreList: 相关性, 数值越大越相关
        :type ScoreList: list of float
        :param _Usage: 消耗量，仅返回TotalToken
        :type Usage: :class:`tencentcloud.lkeap.v20240522.models.Usage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScoreList = None
        self._Usage = None
        self._RequestId = None

    @property
    def ScoreList(self):
        r"""相关性, 数值越大越相关
        :rtype: list of float
        """
        return self._ScoreList

    @ScoreList.setter
    def ScoreList(self, ScoreList):
        self._ScoreList = ScoreList

    @property
    def Usage(self):
        r"""消耗量，仅返回TotalToken
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.Usage`
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
        self._ScoreList = params.get("ScoreList")
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class SearchResult(AbstractModel):
    r"""搜索结果

    """

    def __init__(self):
        r"""
        :param _Index: 索引
        :type Index: int
        :param _Url: 链接地址
        :type Url: str
        :param _Name: 标题
        :type Name: str
        :param _Snippet: 摘要
        :type Snippet: str
        :param _Icon: 图标
        :type Icon: str
        :param _Site: 站点
        :type Site: str
        :param _PublishedTime: 1740412800
        :type PublishedTime: int
        """
        self._Index = None
        self._Url = None
        self._Name = None
        self._Snippet = None
        self._Icon = None
        self._Site = None
        self._PublishedTime = None

    @property
    def Index(self):
        r"""索引
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Url(self):
        r"""链接地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Name(self):
        r"""标题
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Snippet(self):
        r"""摘要
        :rtype: str
        """
        return self._Snippet

    @Snippet.setter
    def Snippet(self, Snippet):
        self._Snippet = Snippet

    @property
    def Icon(self):
        r"""图标
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def Site(self):
        r"""站点
        :rtype: str
        """
        return self._Site

    @Site.setter
    def Site(self, Site):
        self._Site = Site

    @property
    def PublishedTime(self):
        r"""1740412800
        :rtype: int
        """
        return self._PublishedTime

    @PublishedTime.setter
    def PublishedTime(self, PublishedTime):
        self._PublishedTime = PublishedTime


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Url = params.get("Url")
        self._Name = params.get("Name")
        self._Snippet = params.get("Snippet")
        self._Icon = params.get("Icon")
        self._Site = params.get("Site")
        self._PublishedTime = params.get("PublishedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitDocumentFailedPage(AbstractModel):
    r"""文档解析失败记录

    """

    def __init__(self):
        r"""
        :param _PageNumber: 失败页码	
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        """
        self._PageNumber = None

    @property
    def PageNumber(self):
        r"""失败页码	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Thinking(AbstractModel):
    r"""思维链开关类型

    """

    def __init__(self):
        r"""
        :param _Type: 控制开启思维链，默认disabled

enabled：开启思维链
disabled：关闭思维链
        :type Type: str
        """
        self._Type = None

    @property
    def Type(self):
        r"""控制开启思维链，默认disabled

enabled：开启思维链
disabled：关闭思维链
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Usage(AbstractModel):
    r"""消耗量

    """

    def __init__(self):
        r"""
        :param _TotalPages: 文档页数
        :type TotalPages: int
        :param _InputTokens: 输入token数
        :type InputTokens: int
        :param _OutputTokens: 输出token数
        :type OutputTokens: int
        :param _TotalTokens: 总token数
        :type TotalTokens: int
        """
        self._TotalPages = None
        self._InputTokens = None
        self._OutputTokens = None
        self._TotalTokens = None

    @property
    def TotalPages(self):
        r"""文档页数
        :rtype: int
        """
        return self._TotalPages

    @TotalPages.setter
    def TotalPages(self, TotalPages):
        self._TotalPages = TotalPages

    @property
    def InputTokens(self):
        r"""输入token数
        :rtype: int
        """
        return self._InputTokens

    @InputTokens.setter
    def InputTokens(self, InputTokens):
        self._InputTokens = InputTokens

    @property
    def OutputTokens(self):
        r"""输出token数
        :rtype: int
        """
        return self._OutputTokens

    @OutputTokens.setter
    def OutputTokens(self, OutputTokens):
        self._OutputTokens = OutputTokens

    @property
    def TotalTokens(self):
        r"""总token数
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._TotalPages = params.get("TotalPages")
        self._InputTokens = params.get("InputTokens")
        self._OutputTokens = params.get("OutputTokens")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        