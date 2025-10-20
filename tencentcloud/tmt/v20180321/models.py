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


class BoundingBox(AbstractModel):
    r"""段落文本框位置：x，y代表左上顶点，width和height代表宽高

    """

    def __init__(self):
        r"""
        :param _X: 左上顶点x坐标
        :type X: int
        :param _Y: 左上顶点y坐标
        :type Y: int
        :param _Width: 宽
        :type Width: int
        :param _Height: 高
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        r"""左上顶点x坐标
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""左上顶点y坐标
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        r"""宽
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""高
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coord(AbstractModel):
    r"""坐标详细信息

    """

    def __init__(self):
        r"""
        :param _X: X坐标
        :type X: int
        :param _Y: Y坐标
        :type Y: int
        """
        self._X = None
        self._Y = None

    @property
    def X(self):
        r"""X坐标
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""Y坐标
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileTranslateRequest(AbstractModel):
    r"""FileTranslate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Source: 源语言，支持
zh：简体中文
zh-HK：繁体中文
zh-TW：繁体中文
zh-TR：繁体中文
en：英语
ar：阿拉伯语
de：德语
es：西班牙语
fr：法语
it：意大利语
ja：日语
pt：葡萄牙语
ru：俄语
ko：韩语
tr：土耳其语
vi：越南语
th：泰语
        :type Source: str
        :param _Target: 目标语言，各源语言的目标语言支持列表如下
zh（简体中文）：en（英语）、ar（阿拉伯语）、de（德语）、es（西班牙语）、fr（法语）、it（意大利语）、ja（日语）、pt（葡萄牙语）、ru（俄语）、ko（韩语）、tr（土耳其语）、vi（越南语）、th（泰语）
zh-HK（繁体中文）：en（英语）、ar（阿拉伯语）、de（德语）、es（西班牙语）、fr（法语）、it（意大利语）、ja（日语）、pt（葡萄牙语）、ru（俄语）、ko（韩语）、tr（土耳其语）、vi（越南语）、th（泰语）
zh-TW（繁体中文）：en（英语）、ar（阿拉伯语）、de（德语）、es（西班牙语）、fr（法语）、it（意大利语）、ja（日语）、pt（葡萄牙语）、ru（俄语）、ko（韩语）、tr（土耳其语）、vi（越南语）、th（泰语）
zh-TR（繁体中文）:en（英语）、ar（阿拉伯语）、de（德语）、es（西班牙语）、fr（法语）、it（意大利语）、ja（日语）、pt（葡萄牙语）、ru（俄语）、ko（韩语）、tr（土耳其语）、vi（越南语）、th（泰语）
en（英语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、ar（阿拉伯语）、de（德语）、es（西班牙语）、fr（法语）、it（意大利语）、ja（日语）、pt（葡萄牙语）、ru（俄语）、ko（韩语）、tr（土耳其语）、vi（越南语）、th（泰语）
ar（阿拉伯语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
de（德语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
es（西班牙语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）、fr（法语）
fr（法语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）、es（西班牙语）
it（意大利语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
ja（日语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
pt（葡萄牙语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
ru（俄语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
ko（韩语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
tr（土耳其语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
vi（越南语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
th（泰语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
        :type Target: str
        :param _DocumentType: 文档类型：可支持以下几种(pdf,docx,pptx,xlsx,txt,xml,html,markdown,properties)
        :type DocumentType: str
        :param _SourceType: 数据来源，0：url，1：直接传文件编码后数据
        :type SourceType: int
        :param _Url: 需要翻译文件url，URL长度不能超过1000字符。文件限制如下：docx/xIsx/html/markdown文件不超过800万字符，doc/pdf/pptx文件不超过300页，txt/po文件不超过10MB，pdf/docx/pptx/xlsx不超过40MB
        :type Url: str
        :param _BasicDocumentType: 原始文档类型。该参数为高级参数，请留空，如需使用，请与工作人员确认后再使用。
        :type BasicDocumentType: str
        :param _CallbackUrl: 回调url，URL长度不能超过256字符。文件大于10MB或字符较多时，建议采用回调方式；回调时，所有内容会放入 Body 中，具体请参见[文件翻译回调说明](https://cloud.tencent.com/document/product/551/91138)。
        :type CallbackUrl: str
        :param _Data: 文件数据，当SourceType 值为1时必须填写，为0可不写。要base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。数据要小于5MB。
        :type Data: str
        """
        self._Source = None
        self._Target = None
        self._DocumentType = None
        self._SourceType = None
        self._Url = None
        self._BasicDocumentType = None
        self._CallbackUrl = None
        self._Data = None

    @property
    def Source(self):
        r"""源语言，支持
zh：简体中文
zh-HK：繁体中文
zh-TW：繁体中文
zh-TR：繁体中文
en：英语
ar：阿拉伯语
de：德语
es：西班牙语
fr：法语
it：意大利语
ja：日语
pt：葡萄牙语
ru：俄语
ko：韩语
tr：土耳其语
vi：越南语
th：泰语
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""目标语言，各源语言的目标语言支持列表如下
zh（简体中文）：en（英语）、ar（阿拉伯语）、de（德语）、es（西班牙语）、fr（法语）、it（意大利语）、ja（日语）、pt（葡萄牙语）、ru（俄语）、ko（韩语）、tr（土耳其语）、vi（越南语）、th（泰语）
zh-HK（繁体中文）：en（英语）、ar（阿拉伯语）、de（德语）、es（西班牙语）、fr（法语）、it（意大利语）、ja（日语）、pt（葡萄牙语）、ru（俄语）、ko（韩语）、tr（土耳其语）、vi（越南语）、th（泰语）
zh-TW（繁体中文）：en（英语）、ar（阿拉伯语）、de（德语）、es（西班牙语）、fr（法语）、it（意大利语）、ja（日语）、pt（葡萄牙语）、ru（俄语）、ko（韩语）、tr（土耳其语）、vi（越南语）、th（泰语）
zh-TR（繁体中文）:en（英语）、ar（阿拉伯语）、de（德语）、es（西班牙语）、fr（法语）、it（意大利语）、ja（日语）、pt（葡萄牙语）、ru（俄语）、ko（韩语）、tr（土耳其语）、vi（越南语）、th（泰语）
en（英语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、ar（阿拉伯语）、de（德语）、es（西班牙语）、fr（法语）、it（意大利语）、ja（日语）、pt（葡萄牙语）、ru（俄语）、ko（韩语）、tr（土耳其语）、vi（越南语）、th（泰语）
ar（阿拉伯语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
de（德语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
es（西班牙语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）、fr（法语）
fr（法语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）、es（西班牙语）
it（意大利语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
ja（日语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
pt（葡萄牙语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
ru（俄语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
ko（韩语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
tr（土耳其语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
vi（越南语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
th（泰语）：zh（简体中文）、zh-HK（繁体中文）、zh-TW（繁体中文）、zh-TR（繁体中文）、en（英语）
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def DocumentType(self):
        r"""文档类型：可支持以下几种(pdf,docx,pptx,xlsx,txt,xml,html,markdown,properties)
        :rtype: str
        """
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def SourceType(self):
        r"""数据来源，0：url，1：直接传文件编码后数据
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def Url(self):
        r"""需要翻译文件url，URL长度不能超过1000字符。文件限制如下：docx/xIsx/html/markdown文件不超过800万字符，doc/pdf/pptx文件不超过300页，txt/po文件不超过10MB，pdf/docx/pptx/xlsx不超过40MB
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def BasicDocumentType(self):
        r"""原始文档类型。该参数为高级参数，请留空，如需使用，请与工作人员确认后再使用。
        :rtype: str
        """
        return self._BasicDocumentType

    @BasicDocumentType.setter
    def BasicDocumentType(self, BasicDocumentType):
        self._BasicDocumentType = BasicDocumentType

    @property
    def CallbackUrl(self):
        r"""回调url，URL长度不能超过256字符。文件大于10MB或字符较多时，建议采用回调方式；回调时，所有内容会放入 Body 中，具体请参见[文件翻译回调说明](https://cloud.tencent.com/document/product/551/91138)。
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def Data(self):
        r"""文件数据，当SourceType 值为1时必须填写，为0可不写。要base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。数据要小于5MB。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._DocumentType = params.get("DocumentType")
        self._SourceType = params.get("SourceType")
        self._Url = params.get("Url")
        self._BasicDocumentType = params.get("BasicDocumentType")
        self._CallbackUrl = params.get("CallbackUrl")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileTranslateResponse(AbstractModel):
    r"""FileTranslate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 文件翻译的请求返回结果，包含结果查询需要的TaskId
        :type Data: :class:`tencentcloud.tmt.v20180321.models.Task`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""文件翻译的请求返回结果，包含结果查询需要的TaskId
        :rtype: :class:`tencentcloud.tmt.v20180321.models.Task`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
            self._Data = Task()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetFileTranslateData(AbstractModel):
    r"""文件翻译任务结果

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _Status: 任务状态

- init：任务已初始化
- wait：任务等待执行
- success：任务执行成功
- fail：任务执行失败
        :type Status: str
        :param _FileData: 文件数据，目标文件必须小于50M，否则请通过回调方式请求文件翻译接口
注意：此字段可能返回 null，表示取不到有效值。
        :type FileData: str
        :param _Message: 错误提示
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Progress: 任务进度
        :type Progress: int
        :param _UsedAmount: 本次翻译消耗的字符数	
        :type UsedAmount: int
        """
        self._TaskId = None
        self._Status = None
        self._FileData = None
        self._Message = None
        self._Progress = None
        self._UsedAmount = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""任务状态

- init：任务已初始化
- wait：任务等待执行
- success：任务执行成功
- fail：任务执行失败
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FileData(self):
        r"""文件数据，目标文件必须小于50M，否则请通过回调方式请求文件翻译接口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileData

    @FileData.setter
    def FileData(self, FileData):
        self._FileData = FileData

    @property
    def Message(self):
        r"""错误提示
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Progress(self):
        r"""任务进度
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def UsedAmount(self):
        r"""本次翻译消耗的字符数	
        :rtype: int
        """
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._FileData = params.get("FileData")
        self._Message = params.get("Message")
        self._Progress = params.get("Progress")
        self._UsedAmount = params.get("UsedAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFileTranslateRequest(AbstractModel):
    r"""GetFileTranslate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""任务ID
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
        


class GetFileTranslateResponse(AbstractModel):
    r"""GetFileTranslate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 任务id
        :type Data: :class:`tencentcloud.tmt.v20180321.models.GetFileTranslateData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""任务id
        :rtype: :class:`tencentcloud.tmt.v20180321.models.GetFileTranslateData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
            self._Data = GetFileTranslateData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ImageRecord(AbstractModel):
    r"""图片翻译结果

    """

    def __init__(self):
        r"""
        :param _Value: 图片翻译结果
        :type Value: list of ItemValue
        """
        self._Value = None

    @property
    def Value(self):
        r"""图片翻译结果
        :rtype: list of ItemValue
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        if params.get("Value") is not None:
            self._Value = []
            for item in params.get("Value"):
                obj = ItemValue()
                obj._deserialize(item)
                self._Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTranslateLLMRequest(AbstractModel):
    r"""ImageTranslateLLM请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 图片数据的Base64字符串，经Base64编码后不超过 9M，分辨率建议600*800以上，支持PNG、JPG、JPEG格式。
        :type Data: str
        :param _Target: 目标语言，支持语言列表：

- 中文：zh
- 繁体（中国台湾）：zh-TW
- 繁体（中国香港）：zh-HK
- 英文：en
- 日语：ja
- 韩语：ko
- 泰语：th
- 越南语：vi
- 俄语：ru
- 德语：de
- 法语：fr
- 阿拉伯语：ar
- 西班牙语：es
- 意大利语：it
- 印度尼西亚语：id
- 马来西亚语：ms
- 葡萄牙语：pt
- 土耳其语：tr
- 
        :type Target: str
        :param _Url: 输入图 Url。 使用Url的时候，Data参数需要传入""。 图片限制：小于 10MB，分辨率建议600*800以上，格式支持 jpg、jpeg、png。

        :type Url: str
        """
        self._Data = None
        self._Target = None
        self._Url = None

    @property
    def Data(self):
        r"""图片数据的Base64字符串，经Base64编码后不超过 9M，分辨率建议600*800以上，支持PNG、JPG、JPEG格式。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Target(self):
        r"""目标语言，支持语言列表：

- 中文：zh
- 繁体（中国台湾）：zh-TW
- 繁体（中国香港）：zh-HK
- 英文：en
- 日语：ja
- 韩语：ko
- 泰语：th
- 越南语：vi
- 俄语：ru
- 德语：de
- 法语：fr
- 阿拉伯语：ar
- 西班牙语：es
- 意大利语：it
- 印度尼西亚语：id
- 马来西亚语：ms
- 葡萄牙语：pt
- 土耳其语：tr
- 
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def Url(self):
        r"""输入图 Url。 使用Url的时候，Data参数需要传入""。 图片限制：小于 10MB，分辨率建议600*800以上，格式支持 jpg、jpeg、png。

        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._Target = params.get("Target")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTranslateLLMResponse(AbstractModel):
    r"""ImageTranslateLLM返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 图片数据的Base64字符串，输出格式为JPG。

        :type Data: str
        :param _Source: 原文本主要源语言。
        :type Source: str
        :param _Target: 目标翻译语言。
        :type Target: str
        :param _SourceText: 图片中的全部原文本。
        :type SourceText: str
        :param _TargetText: 图片中全部译文。
        :type TargetText: str
        :param _Angle: 逆时针图片角度，取值范围为0-359
        :type Angle: float
        :param _TransDetails: 翻译详情信息
        :type TransDetails: list of TransDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Source = None
        self._Target = None
        self._SourceText = None
        self._TargetText = None
        self._Angle = None
        self._TransDetails = None
        self._RequestId = None

    @property
    def Data(self):
        r"""图片数据的Base64字符串，输出格式为JPG。

        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Source(self):
        r"""原文本主要源语言。
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""目标翻译语言。
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def SourceText(self):
        r"""图片中的全部原文本。
        :rtype: str
        """
        return self._SourceText

    @SourceText.setter
    def SourceText(self, SourceText):
        self._SourceText = SourceText

    @property
    def TargetText(self):
        r"""图片中全部译文。
        :rtype: str
        """
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText

    @property
    def Angle(self):
        r"""逆时针图片角度，取值范围为0-359
        :rtype: float
        """
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def TransDetails(self):
        r"""翻译详情信息
        :rtype: list of TransDetail
        """
        return self._TransDetails

    @TransDetails.setter
    def TransDetails(self, TransDetails):
        self._TransDetails = TransDetails

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
        self._Data = params.get("Data")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._SourceText = params.get("SourceText")
        self._TargetText = params.get("TargetText")
        self._Angle = params.get("Angle")
        if params.get("TransDetails") is not None:
            self._TransDetails = []
            for item in params.get("TransDetails"):
                obj = TransDetail()
                obj._deserialize(item)
                self._TransDetails.append(obj)
        self._RequestId = params.get("RequestId")


class ImageTranslateRequest(AbstractModel):
    r"""ImageTranslate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionUuid: 唯一id，返回时原样返回
        :type SessionUuid: str
        :param _Scene: doc:文档扫描
        :type Scene: str
        :param _Data: 图片数据的Base64字符串，经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。图片中包含文字需要少于6000字符。
        :type Data: str
        :param _Source: 源语言，支持语言列表：<li> auto：自动识别（识别为一种语言）</li> <li>zh：简体中文</li> <li>zh-TW：繁体中文</li> <li>en：英语</li> <li>ja：日语</li> <li>ko：韩语</li> <li>ru：俄语</li> <li>fr：法语</li> <li>de：德语</li> <li>it：意大利语</li> <li>es：西班牙语</li> <li>pt：葡萄牙语</li> <li>ms：马来西亚语</li> <li>th：泰语</li><li>vi：越南语</li>
        :type Source: str
        :param _Target: 目标语言，各源语言的目标语言支持列表如下：
<li>zh（简体中文）：en（英语）、ja（日语）、ko（韩语）、ru（俄语）、fr（法语）、de（德语）、it（意大利语）、es（西班牙语）、pt（葡萄牙语）、ms（马来语）、th（泰语）、vi（越南语）</li>
<li>zh-TW（繁体中文）：en（英语）、ja（日语）、ko（韩语）、ru（俄语）、fr（法语）、de（德语）、it（意大利语）、es（西班牙语）、pt（葡萄牙语）、ms（马来语）、th（泰语）、vi（越南语）</li>
<li>en（英语）：zh（中文）、ja（日语）、ko（韩语）、ru（俄语）、fr（法语）、de（德语）、it（意大利语）、es（西班牙语）、pt（葡萄牙语）、ms（马来语）、th（泰语）、vi（越南语）</li>
<li>ja（日语）：zh（中文）、en（英语）、ko（韩语）</li>
<li>ko（韩语）：zh（中文）、en（英语）、ja（日语）</li>
<li>ru：俄语：zh（中文）、en（英语）</li>
<li>fr：法语：zh（中文）、en（英语）</li>
<li>de：德语：zh（中文）、en（英语）</li>
<li>it：意大利语：zh（中文）、en（英语）</li>
<li>es：西班牙语：zh（中文）、en（英语）</li>
<li>pt：葡萄牙语：zh（中文）、en（英语）</li>
<li>ms：马来西亚语：zh（中文）、en（英语）</li>
<li>th：泰语：zh（中文）、en（英语）</li>
<li>vi：越南语：zh（中文）、en（英语）</li>
        :type Target: str
        :param _ProjectId: 项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0
        :type ProjectId: int
        """
        self._SessionUuid = None
        self._Scene = None
        self._Data = None
        self._Source = None
        self._Target = None
        self._ProjectId = None

    @property
    def SessionUuid(self):
        r"""唯一id，返回时原样返回
        :rtype: str
        """
        return self._SessionUuid

    @SessionUuid.setter
    def SessionUuid(self, SessionUuid):
        self._SessionUuid = SessionUuid

    @property
    def Scene(self):
        r"""doc:文档扫描
        :rtype: str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def Data(self):
        r"""图片数据的Base64字符串，经Base64编码后不超过 7M，分辨率建议600*800以上，支持PNG、JPG、JPEG、BMP、PDF格式。图片中包含文字需要少于6000字符。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Source(self):
        r"""源语言，支持语言列表：<li> auto：自动识别（识别为一种语言）</li> <li>zh：简体中文</li> <li>zh-TW：繁体中文</li> <li>en：英语</li> <li>ja：日语</li> <li>ko：韩语</li> <li>ru：俄语</li> <li>fr：法语</li> <li>de：德语</li> <li>it：意大利语</li> <li>es：西班牙语</li> <li>pt：葡萄牙语</li> <li>ms：马来西亚语</li> <li>th：泰语</li><li>vi：越南语</li>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""目标语言，各源语言的目标语言支持列表如下：
<li>zh（简体中文）：en（英语）、ja（日语）、ko（韩语）、ru（俄语）、fr（法语）、de（德语）、it（意大利语）、es（西班牙语）、pt（葡萄牙语）、ms（马来语）、th（泰语）、vi（越南语）</li>
<li>zh-TW（繁体中文）：en（英语）、ja（日语）、ko（韩语）、ru（俄语）、fr（法语）、de（德语）、it（意大利语）、es（西班牙语）、pt（葡萄牙语）、ms（马来语）、th（泰语）、vi（越南语）</li>
<li>en（英语）：zh（中文）、ja（日语）、ko（韩语）、ru（俄语）、fr（法语）、de（德语）、it（意大利语）、es（西班牙语）、pt（葡萄牙语）、ms（马来语）、th（泰语）、vi（越南语）</li>
<li>ja（日语）：zh（中文）、en（英语）、ko（韩语）</li>
<li>ko（韩语）：zh（中文）、en（英语）、ja（日语）</li>
<li>ru：俄语：zh（中文）、en（英语）</li>
<li>fr：法语：zh（中文）、en（英语）</li>
<li>de：德语：zh（中文）、en（英语）</li>
<li>it：意大利语：zh（中文）、en（英语）</li>
<li>es：西班牙语：zh（中文）、en（英语）</li>
<li>pt：葡萄牙语：zh（中文）、en（英语）</li>
<li>ms：马来西亚语：zh（中文）、en（英语）</li>
<li>th：泰语：zh（中文）、en（英语）</li>
<li>vi：越南语：zh（中文）、en（英语）</li>
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def ProjectId(self):
        r"""项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._SessionUuid = params.get("SessionUuid")
        self._Scene = params.get("Scene")
        self._Data = params.get("Data")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTranslateResponse(AbstractModel):
    r"""ImageTranslate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionUuid: 请求的SessionUuid返回
        :type SessionUuid: str
        :param _Source: 源语言
        :type Source: str
        :param _Target: 目标语言
        :type Target: str
        :param _ImageRecord: 图片翻译结果，翻译结果按识别的文本每一行独立翻译，后续会推出按段落划分并翻译的版本
        :type ImageRecord: :class:`tencentcloud.tmt.v20180321.models.ImageRecord`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionUuid = None
        self._Source = None
        self._Target = None
        self._ImageRecord = None
        self._RequestId = None

    @property
    def SessionUuid(self):
        r"""请求的SessionUuid返回
        :rtype: str
        """
        return self._SessionUuid

    @SessionUuid.setter
    def SessionUuid(self, SessionUuid):
        self._SessionUuid = SessionUuid

    @property
    def Source(self):
        r"""源语言
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""目标语言
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def ImageRecord(self):
        r"""图片翻译结果，翻译结果按识别的文本每一行独立翻译，后续会推出按段落划分并翻译的版本
        :rtype: :class:`tencentcloud.tmt.v20180321.models.ImageRecord`
        """
        return self._ImageRecord

    @ImageRecord.setter
    def ImageRecord(self, ImageRecord):
        self._ImageRecord = ImageRecord

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
        self._SessionUuid = params.get("SessionUuid")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        if params.get("ImageRecord") is not None:
            self._ImageRecord = ImageRecord()
            self._ImageRecord._deserialize(params.get("ImageRecord"))
        self._RequestId = params.get("RequestId")


class ItemValue(AbstractModel):
    r"""翻译结果

    """

    def __init__(self):
        r"""
        :param _SourceText: 识别出的源文
        :type SourceText: str
        :param _TargetText: 翻译后的译文
        :type TargetText: str
        :param _X: X坐标
        :type X: int
        :param _Y: Y坐标
        :type Y: int
        :param _W: 宽度
        :type W: int
        :param _H: 高度
        :type H: int
        """
        self._SourceText = None
        self._TargetText = None
        self._X = None
        self._Y = None
        self._W = None
        self._H = None

    @property
    def SourceText(self):
        r"""识别出的源文
        :rtype: str
        """
        return self._SourceText

    @SourceText.setter
    def SourceText(self, SourceText):
        self._SourceText = SourceText

    @property
    def TargetText(self):
        r"""翻译后的译文
        :rtype: str
        """
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText

    @property
    def X(self):
        r"""X坐标
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""Y坐标
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def W(self):
        r"""宽度
        :rtype: int
        """
        return self._W

    @W.setter
    def W(self, W):
        self._W = W

    @property
    def H(self):
        r"""高度
        :rtype: int
        """
        return self._H

    @H.setter
    def H(self, H):
        self._H = H


    def _deserialize(self, params):
        self._SourceText = params.get("SourceText")
        self._TargetText = params.get("TargetText")
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._W = params.get("W")
        self._H = params.get("H")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LanguageDetectRequest(AbstractModel):
    r"""LanguageDetect请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待识别的文本，文本统一使用utf-8格式编码，非utf-8格式编码字符会翻译失败。单次请求的文本长度需要低于2000。
        :type Text: str
        :param _ProjectId: 项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0
        :type ProjectId: int
        """
        self._Text = None
        self._ProjectId = None

    @property
    def Text(self):
        r"""待识别的文本，文本统一使用utf-8格式编码，非utf-8格式编码字符会翻译失败。单次请求的文本长度需要低于2000。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def ProjectId(self):
        r"""项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LanguageDetectResponse(AbstractModel):
    r"""LanguageDetect返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Lang: 识别出的语言种类，参考语言列表
<li> zh : 中文 </li> <li> en : 英文 </li><li> jp : 日语 </li> <li> kr : 韩语 </li><li> de : 德语 </li><li> fr : 法语 </li><li> es : 西班牙文 </li> <li> it : 意大利文 </li><li> tr : 土耳其文 </li><li> ru : 俄文 </li><li> pt : 葡萄牙文 </li><li> vi : 越南文 </li><li> id : 印度尼西亚文 </li><li> ms : 马来西亚文 </li><li> th : 泰文 </li>
        :type Lang: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Lang = None
        self._RequestId = None

    @property
    def Lang(self):
        r"""识别出的语言种类，参考语言列表
<li> zh : 中文 </li> <li> en : 英文 </li><li> jp : 日语 </li> <li> kr : 韩语 </li><li> de : 德语 </li><li> fr : 法语 </li><li> es : 西班牙文 </li> <li> it : 意大利文 </li><li> tr : 土耳其文 </li><li> ru : 俄文 </li><li> pt : 葡萄牙文 </li><li> vi : 越南文 </li><li> id : 印度尼西亚文 </li><li> ms : 马来西亚文 </li><li> th : 泰文 </li>
        :rtype: str
        """
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang

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
        self._Lang = params.get("Lang")
        self._RequestId = params.get("RequestId")


class RotateParagraphRect(AbstractModel):
    r"""段落文本旋转信息

    """

    def __init__(self):
        r"""
        :param _Coord: 段落文本坐标
        :type Coord: list of Coord
        :param _TiltAngle: 旋转角度
        :type TiltAngle: float
        :param _Valid: 段落文本信息是否有效
        :type Valid: bool
        """
        self._Coord = None
        self._TiltAngle = None
        self._Valid = None

    @property
    def Coord(self):
        r"""段落文本坐标
        :rtype: list of Coord
        """
        return self._Coord

    @Coord.setter
    def Coord(self, Coord):
        self._Coord = Coord

    @property
    def TiltAngle(self):
        r"""旋转角度
        :rtype: float
        """
        return self._TiltAngle

    @TiltAngle.setter
    def TiltAngle(self, TiltAngle):
        self._TiltAngle = TiltAngle

    @property
    def Valid(self):
        r"""段落文本信息是否有效
        :rtype: bool
        """
        return self._Valid

    @Valid.setter
    def Valid(self, Valid):
        self._Valid = Valid


    def _deserialize(self, params):
        if params.get("Coord") is not None:
            self._Coord = []
            for item in params.get("Coord"):
                obj = Coord()
                obj._deserialize(item)
                self._Coord.append(obj)
        self._TiltAngle = params.get("TiltAngle")
        self._Valid = params.get("Valid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeechTranslateRequest(AbstractModel):
    r"""SpeechTranslate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionUuid: 一段完整的语音对应一个SessionUuid
        :type SessionUuid: str
        :param _Source: 音频中的语言类型，支持语言列表<li> zh : 中文 </li> <li> en : 英文 </li>
        :type Source: str
        :param _Target: 翻译目标语言类型，支持的语言列表<li> zh : 中文 </li> <li> en : 英文 </li>
        :type Target: str
        :param _AudioFormat: pcm : 146   speex : 16779154   mp3 : 83886080
        :type AudioFormat: int
        :param _Seq: 语音分片的序号，从0开始
        :type Seq: int
        :param _IsEnd: 是否最后一片语音分片，0-否，1-是
        :type IsEnd: int
        :param _Data: 语音分片内容进行 Base64 编码后的字符串。音频内容需包含有效并可识别的文本信息。
        :type Data: str
        :param _ProjectId: 项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0
        :type ProjectId: int
        :param _Mode: 识别模式，该参数已废弃
        :type Mode: str
        :param _TransType: 该参数已废弃
        :type TransType: int
        """
        self._SessionUuid = None
        self._Source = None
        self._Target = None
        self._AudioFormat = None
        self._Seq = None
        self._IsEnd = None
        self._Data = None
        self._ProjectId = None
        self._Mode = None
        self._TransType = None

    @property
    def SessionUuid(self):
        r"""一段完整的语音对应一个SessionUuid
        :rtype: str
        """
        return self._SessionUuid

    @SessionUuid.setter
    def SessionUuid(self, SessionUuid):
        self._SessionUuid = SessionUuid

    @property
    def Source(self):
        r"""音频中的语言类型，支持语言列表<li> zh : 中文 </li> <li> en : 英文 </li>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""翻译目标语言类型，支持的语言列表<li> zh : 中文 </li> <li> en : 英文 </li>
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def AudioFormat(self):
        r"""pcm : 146   speex : 16779154   mp3 : 83886080
        :rtype: int
        """
        return self._AudioFormat

    @AudioFormat.setter
    def AudioFormat(self, AudioFormat):
        self._AudioFormat = AudioFormat

    @property
    def Seq(self):
        r"""语音分片的序号，从0开始
        :rtype: int
        """
        return self._Seq

    @Seq.setter
    def Seq(self, Seq):
        self._Seq = Seq

    @property
    def IsEnd(self):
        r"""是否最后一片语音分片，0-否，1-是
        :rtype: int
        """
        return self._IsEnd

    @IsEnd.setter
    def IsEnd(self, IsEnd):
        self._IsEnd = IsEnd

    @property
    def Data(self):
        r"""语音分片内容进行 Base64 编码后的字符串。音频内容需包含有效并可识别的文本信息。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def ProjectId(self):
        r"""项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Mode(self):
        warnings.warn("parameter `Mode` is deprecated", DeprecationWarning) 

        r"""识别模式，该参数已废弃
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        warnings.warn("parameter `Mode` is deprecated", DeprecationWarning) 

        self._Mode = Mode

    @property
    def TransType(self):
        warnings.warn("parameter `TransType` is deprecated", DeprecationWarning) 

        r"""该参数已废弃
        :rtype: int
        """
        return self._TransType

    @TransType.setter
    def TransType(self, TransType):
        warnings.warn("parameter `TransType` is deprecated", DeprecationWarning) 

        self._TransType = TransType


    def _deserialize(self, params):
        self._SessionUuid = params.get("SessionUuid")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._AudioFormat = params.get("AudioFormat")
        self._Seq = params.get("Seq")
        self._IsEnd = params.get("IsEnd")
        self._Data = params.get("Data")
        self._ProjectId = params.get("ProjectId")
        self._Mode = params.get("Mode")
        self._TransType = params.get("TransType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeechTranslateResponse(AbstractModel):
    r"""SpeechTranslate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionUuid: 请求的SessionUuid直接返回
        :type SessionUuid: str
        :param _RecognizeStatus: 语音识别状态 1-进行中 0-完成
        :type RecognizeStatus: int
        :param _SourceText: 识别出的原文
        :type SourceText: str
        :param _TargetText: 翻译出的译文
        :type TargetText: str
        :param _Seq: 第几个语音分片
        :type Seq: int
        :param _Source: 原语言
        :type Source: str
        :param _Target: 目标语言
        :type Target: str
        :param _VadSeq: 当请求的Mode参数填写bvad是，启动VadSeq。此时Seq会被设置为后台vad（静音检测）后的新序号，而VadSeq代表客户端原始Seq值
        :type VadSeq: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionUuid = None
        self._RecognizeStatus = None
        self._SourceText = None
        self._TargetText = None
        self._Seq = None
        self._Source = None
        self._Target = None
        self._VadSeq = None
        self._RequestId = None

    @property
    def SessionUuid(self):
        r"""请求的SessionUuid直接返回
        :rtype: str
        """
        return self._SessionUuid

    @SessionUuid.setter
    def SessionUuid(self, SessionUuid):
        self._SessionUuid = SessionUuid

    @property
    def RecognizeStatus(self):
        r"""语音识别状态 1-进行中 0-完成
        :rtype: int
        """
        return self._RecognizeStatus

    @RecognizeStatus.setter
    def RecognizeStatus(self, RecognizeStatus):
        self._RecognizeStatus = RecognizeStatus

    @property
    def SourceText(self):
        r"""识别出的原文
        :rtype: str
        """
        return self._SourceText

    @SourceText.setter
    def SourceText(self, SourceText):
        self._SourceText = SourceText

    @property
    def TargetText(self):
        r"""翻译出的译文
        :rtype: str
        """
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText

    @property
    def Seq(self):
        r"""第几个语音分片
        :rtype: int
        """
        return self._Seq

    @Seq.setter
    def Seq(self, Seq):
        self._Seq = Seq

    @property
    def Source(self):
        r"""原语言
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""目标语言
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def VadSeq(self):
        r"""当请求的Mode参数填写bvad是，启动VadSeq。此时Seq会被设置为后台vad（静音检测）后的新序号，而VadSeq代表客户端原始Seq值
        :rtype: int
        """
        return self._VadSeq

    @VadSeq.setter
    def VadSeq(self, VadSeq):
        self._VadSeq = VadSeq

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
        self._SessionUuid = params.get("SessionUuid")
        self._RecognizeStatus = params.get("RecognizeStatus")
        self._SourceText = params.get("SourceText")
        self._TargetText = params.get("TargetText")
        self._Seq = params.get("Seq")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._VadSeq = params.get("VadSeq")
        self._RequestId = params.get("RequestId")


class Task(AbstractModel):
    r"""文件翻译请求的返回数据

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可通过此ID在轮询接口获取识别状态与结果。注意：TaskId数据类型为字符串类型
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""任务ID，可通过此ID在轮询接口获取识别状态与结果。注意：TaskId数据类型为字符串类型
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
        


class TextTranslateBatchRequest(AbstractModel):
    r"""TextTranslateBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Source: 源语言，支持： 
auto：自动识别（识别为一种语言）
zh：简体中文
zh-TW：繁体中文
en：英语
ja：日语
ko：韩语
fr：法语
es：西班牙语
it：意大利语
de：德语
tr：土耳其语
ru：俄语
pt：葡萄牙语
vi：越南语
id：印尼语
th：泰语
ms：马来西亚语
ar：阿拉伯语
hi：印地语
        :type Source: str
        :param _Target: 目标语言，各源语言的目标语言支持列表如下

<li> zh（简体中文）：en（英语）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）</li>
<li>zh-TW（繁体中文）：en（英语）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）</li>
<li>en（英语）：zh（中文）、zh-TW（繁体中文）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）、hi（印地语）</li>
<li>ja（日语）：zh（中文）、zh-TW（繁体中文）、en（英语）、ko（韩语）</li>
<li>ko（韩语）：zh（中文）、zh-TW（繁体中文）、en（英语）、ja（日语）</li>
<li>fr（法语）：zh（中文）、zh-TW（繁体中文）、en（英语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>es（西班牙语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>it（意大利语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>de（德语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>tr（土耳其语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、ru（俄语）、pt（葡萄牙语）</li>
<li>ru（俄语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、pt（葡萄牙语）</li>
<li>pt（葡萄牙语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）</li>
<li>vi（越南语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>id（印尼语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>th（泰语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>ms（马来语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>ar（阿拉伯语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>hi（印地语）：en（英语）</li>
        :type Target: str
        :param _ProjectId: 项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0
        :type ProjectId: int
        :param _SourceTextList: 待翻译的文本列表，批量接口可以以数组方式在一次请求中填写多个待翻译文本。文本统一使用utf-8格式编码，非utf-8格式编码字符会翻译失败，请传入有效文本，html标记等非常规翻译文本可能会翻译失败。单次请求的文本长度总和需要低于6000字符。
        :type SourceTextList: list of str
        :param _TermRepoIDList: 需要使用的术语库列表，通过 [术语库操作指南](https://cloud.tencent.com/document/product/551/107926) 自行创建术语库获取。
        :type TermRepoIDList: list of str
        :param _SentRepoIDList: 需要使用的例句库列表，通过 [例句库操作指南](https://cloud.tencent.com/document/product/551/107927) 自行创建例句库获取。
        :type SentRepoIDList: list of str
        """
        self._Source = None
        self._Target = None
        self._ProjectId = None
        self._SourceTextList = None
        self._TermRepoIDList = None
        self._SentRepoIDList = None

    @property
    def Source(self):
        r"""源语言，支持： 
auto：自动识别（识别为一种语言）
zh：简体中文
zh-TW：繁体中文
en：英语
ja：日语
ko：韩语
fr：法语
es：西班牙语
it：意大利语
de：德语
tr：土耳其语
ru：俄语
pt：葡萄牙语
vi：越南语
id：印尼语
th：泰语
ms：马来西亚语
ar：阿拉伯语
hi：印地语
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""目标语言，各源语言的目标语言支持列表如下

<li> zh（简体中文）：en（英语）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）</li>
<li>zh-TW（繁体中文）：en（英语）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）</li>
<li>en（英语）：zh（中文）、zh-TW（繁体中文）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）、hi（印地语）</li>
<li>ja（日语）：zh（中文）、zh-TW（繁体中文）、en（英语）、ko（韩语）</li>
<li>ko（韩语）：zh（中文）、zh-TW（繁体中文）、en（英语）、ja（日语）</li>
<li>fr（法语）：zh（中文）、zh-TW（繁体中文）、en（英语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>es（西班牙语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>it（意大利语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>de（德语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>tr（土耳其语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、ru（俄语）、pt（葡萄牙语）</li>
<li>ru（俄语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、pt（葡萄牙语）</li>
<li>pt（葡萄牙语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）</li>
<li>vi（越南语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>id（印尼语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>th（泰语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>ms（马来语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>ar（阿拉伯语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>hi（印地语）：en（英语）</li>
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def ProjectId(self):
        r"""项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SourceTextList(self):
        r"""待翻译的文本列表，批量接口可以以数组方式在一次请求中填写多个待翻译文本。文本统一使用utf-8格式编码，非utf-8格式编码字符会翻译失败，请传入有效文本，html标记等非常规翻译文本可能会翻译失败。单次请求的文本长度总和需要低于6000字符。
        :rtype: list of str
        """
        return self._SourceTextList

    @SourceTextList.setter
    def SourceTextList(self, SourceTextList):
        self._SourceTextList = SourceTextList

    @property
    def TermRepoIDList(self):
        r"""需要使用的术语库列表，通过 [术语库操作指南](https://cloud.tencent.com/document/product/551/107926) 自行创建术语库获取。
        :rtype: list of str
        """
        return self._TermRepoIDList

    @TermRepoIDList.setter
    def TermRepoIDList(self, TermRepoIDList):
        self._TermRepoIDList = TermRepoIDList

    @property
    def SentRepoIDList(self):
        r"""需要使用的例句库列表，通过 [例句库操作指南](https://cloud.tencent.com/document/product/551/107927) 自行创建例句库获取。
        :rtype: list of str
        """
        return self._SentRepoIDList

    @SentRepoIDList.setter
    def SentRepoIDList(self, SentRepoIDList):
        self._SentRepoIDList = SentRepoIDList


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._ProjectId = params.get("ProjectId")
        self._SourceTextList = params.get("SourceTextList")
        self._TermRepoIDList = params.get("TermRepoIDList")
        self._SentRepoIDList = params.get("SentRepoIDList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextTranslateBatchResponse(AbstractModel):
    r"""TextTranslateBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Source: 源语言，详见入参Source
        :type Source: str
        :param _Target: 目标语言，详见入参Target
        :type Target: str
        :param _TargetTextList: 翻译后的文本列表
        :type TargetTextList: list of str
        :param _UsedAmount: 本次翻译消耗的字符数
        :type UsedAmount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Source = None
        self._Target = None
        self._TargetTextList = None
        self._UsedAmount = None
        self._RequestId = None

    @property
    def Source(self):
        r"""源语言，详见入参Source
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""目标语言，详见入参Target
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def TargetTextList(self):
        r"""翻译后的文本列表
        :rtype: list of str
        """
        return self._TargetTextList

    @TargetTextList.setter
    def TargetTextList(self, TargetTextList):
        self._TargetTextList = TargetTextList

    @property
    def UsedAmount(self):
        r"""本次翻译消耗的字符数
        :rtype: int
        """
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

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
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._TargetTextList = params.get("TargetTextList")
        self._UsedAmount = params.get("UsedAmount")
        self._RequestId = params.get("RequestId")


class TextTranslateRequest(AbstractModel):
    r"""TextTranslate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SourceText: 待翻译的文本，文本统一使用utf-8格式编码，非utf-8格式编码字符会翻译失败，请传入有效文本，html标记等非常规翻译文本可能会翻译失败。单次请求的文本长度需要低于6000字符。
        :type SourceText: str
        :param _Source: 源语言，支持：
auto：自动识别（识别为一种语言）
zh：简体中文
zh-TW：繁体中文
en：英语
ja：日语
ko：韩语
fr：法语
es：西班牙语
it：意大利语
de：德语
tr：土耳其语
ru：俄语
pt：葡萄牙语
vi：越南语
id：印尼语
th：泰语
ms：马来西亚语
ar：阿拉伯语
hi：印地语
        :type Source: str
        :param _Target: 目标语言，各源语言的目标语言支持列表如下

<li> zh（简体中文）：zh-TW（繁体中文）、en（英语）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）</li>
<li>zh-TW（繁体中文）：zh（简体中文）、en（英语）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）</li>
<li>en（英语）：zh（中文）、zh-TW（繁体中文）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）、hi（印地语）</li>
<li>ja（日语）：zh（中文）、zh-TW（繁体中文）、en（英语）、ko（韩语）</li>
<li>ko（韩语）：zh（中文）、zh-TW（繁体中文）、en（英语）、ja（日语）</li>
<li>fr（法语）：zh（中文）、zh-TW（繁体中文）、en（英语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>es（西班牙语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>it（意大利语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>de（德语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>tr（土耳其语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、ru（俄语）、pt（葡萄牙语）</li>
<li>ru（俄语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、pt（葡萄牙语）</li>
<li>pt（葡萄牙语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）</li>
<li>vi（越南语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>id（印尼语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>th（泰语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>ms（马来语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>ar（阿拉伯语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>hi（印地语）：en（英语）</li>
        :type Target: str
        :param _ProjectId: 项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0
        :type ProjectId: int
        :param _UntranslatedText: 用来标记不希望被翻译的文本内容，如句子中的特殊符号、人名、地名等；每次请求只支持配置一个不被翻译的单词；仅支持配置人名、地名等名词，不要配置动词或短语，否则会影响翻译结果。
        :type UntranslatedText: str
        :param _TermRepoIDList: 需要使用的术语库列表，通过 [术语库操作指南](https://cloud.tencent.com/document/product/551/107926) 自行创建术语库获取。
        :type TermRepoIDList: list of str
        :param _SentRepoIDList: 需要使用的例句库列表，通过 [例句库操作指南](https://cloud.tencent.com/document/product/551/107927) 自行创建例句库获取。
        :type SentRepoIDList: list of str
        """
        self._SourceText = None
        self._Source = None
        self._Target = None
        self._ProjectId = None
        self._UntranslatedText = None
        self._TermRepoIDList = None
        self._SentRepoIDList = None

    @property
    def SourceText(self):
        r"""待翻译的文本，文本统一使用utf-8格式编码，非utf-8格式编码字符会翻译失败，请传入有效文本，html标记等非常规翻译文本可能会翻译失败。单次请求的文本长度需要低于6000字符。
        :rtype: str
        """
        return self._SourceText

    @SourceText.setter
    def SourceText(self, SourceText):
        self._SourceText = SourceText

    @property
    def Source(self):
        r"""源语言，支持：
auto：自动识别（识别为一种语言）
zh：简体中文
zh-TW：繁体中文
en：英语
ja：日语
ko：韩语
fr：法语
es：西班牙语
it：意大利语
de：德语
tr：土耳其语
ru：俄语
pt：葡萄牙语
vi：越南语
id：印尼语
th：泰语
ms：马来西亚语
ar：阿拉伯语
hi：印地语
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""目标语言，各源语言的目标语言支持列表如下

<li> zh（简体中文）：zh-TW（繁体中文）、en（英语）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）</li>
<li>zh-TW（繁体中文）：zh（简体中文）、en（英语）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）</li>
<li>en（英语）：zh（中文）、zh-TW（繁体中文）、ja（日语）、ko（韩语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）、vi（越南语）、id（印尼语）、th（泰语）、ms（马来语）、ar（阿拉伯语）、hi（印地语）</li>
<li>ja（日语）：zh（中文）、zh-TW（繁体中文）、en（英语）、ko（韩语）</li>
<li>ko（韩语）：zh（中文）、zh-TW（繁体中文）、en（英语）、ja（日语）</li>
<li>fr（法语）：zh（中文）、zh-TW（繁体中文）、en（英语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>es（西班牙语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>it（意大利语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、de（德语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>de（德语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、tr（土耳其语）、ru（俄语）、pt（葡萄牙语）</li>
<li>tr（土耳其语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、ru（俄语）、pt（葡萄牙语）</li>
<li>ru（俄语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、pt（葡萄牙语）</li>
<li>pt（葡萄牙语）：zh（中文）、zh-TW（繁体中文）、en（英语）、fr（法语）、es（西班牙语）、it（意大利语）、de（德语）、tr（土耳其语）、ru（俄语）</li>
<li>vi（越南语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>id（印尼语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>th（泰语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>ms（马来语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>ar（阿拉伯语）：zh（中文）、zh-TW（繁体中文）、en（英语）</li>
<li>hi（印地语）：en（英语）</li>
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def ProjectId(self):
        r"""项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def UntranslatedText(self):
        r"""用来标记不希望被翻译的文本内容，如句子中的特殊符号、人名、地名等；每次请求只支持配置一个不被翻译的单词；仅支持配置人名、地名等名词，不要配置动词或短语，否则会影响翻译结果。
        :rtype: str
        """
        return self._UntranslatedText

    @UntranslatedText.setter
    def UntranslatedText(self, UntranslatedText):
        self._UntranslatedText = UntranslatedText

    @property
    def TermRepoIDList(self):
        r"""需要使用的术语库列表，通过 [术语库操作指南](https://cloud.tencent.com/document/product/551/107926) 自行创建术语库获取。
        :rtype: list of str
        """
        return self._TermRepoIDList

    @TermRepoIDList.setter
    def TermRepoIDList(self, TermRepoIDList):
        self._TermRepoIDList = TermRepoIDList

    @property
    def SentRepoIDList(self):
        r"""需要使用的例句库列表，通过 [例句库操作指南](https://cloud.tencent.com/document/product/551/107927) 自行创建例句库获取。
        :rtype: list of str
        """
        return self._SentRepoIDList

    @SentRepoIDList.setter
    def SentRepoIDList(self, SentRepoIDList):
        self._SentRepoIDList = SentRepoIDList


    def _deserialize(self, params):
        self._SourceText = params.get("SourceText")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._ProjectId = params.get("ProjectId")
        self._UntranslatedText = params.get("UntranslatedText")
        self._TermRepoIDList = params.get("TermRepoIDList")
        self._SentRepoIDList = params.get("SentRepoIDList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextTranslateResponse(AbstractModel):
    r"""TextTranslate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetText: 翻译后的文本
        :type TargetText: str
        :param _Source: 源语言，详见入参Source
        :type Source: str
        :param _Target: 目标语言，详见入参Target
        :type Target: str
        :param _UsedAmount: 本次翻译消耗的字符数
        :type UsedAmount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TargetText = None
        self._Source = None
        self._Target = None
        self._UsedAmount = None
        self._RequestId = None

    @property
    def TargetText(self):
        r"""翻译后的文本
        :rtype: str
        """
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText

    @property
    def Source(self):
        r"""源语言，详见入参Source
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""目标语言，详见入参Target
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def UsedAmount(self):
        r"""本次翻译消耗的字符数
        :rtype: int
        """
        return self._UsedAmount

    @UsedAmount.setter
    def UsedAmount(self, UsedAmount):
        self._UsedAmount = UsedAmount

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
        self._TargetText = params.get("TargetText")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._UsedAmount = params.get("UsedAmount")
        self._RequestId = params.get("RequestId")


class TransDetail(AbstractModel):
    r"""大模型图片翻译详情信息

    """

    def __init__(self):
        r"""
        :param _SourceLineText: 当前行的原文本
        :type SourceLineText: str
        :param _TargetLineText: 当前行的译文
        :type TargetLineText: str
        :param _BoundingBox: 段落文本框位置
        :type BoundingBox: :class:`tencentcloud.tmt.v20180321.models.BoundingBox`
        :param _LinesCount: 行数
        :type LinesCount: int
        :param _LineHeight: 行高
        :type LineHeight: int
        :param _SpamCode: 正常段落spam_code字段为0；如果存在spam_code字段且值大于0（1: 命中垃圾检查；2: 命中安全策略；3: 其他。），则命中安全检查被过滤。
        :type SpamCode: int
        :param _RotateParagraphRect: 段落文本旋转信息，只在valid为true时表示坐标有效
        :type RotateParagraphRect: :class:`tencentcloud.tmt.v20180321.models.RotateParagraphRect`
        """
        self._SourceLineText = None
        self._TargetLineText = None
        self._BoundingBox = None
        self._LinesCount = None
        self._LineHeight = None
        self._SpamCode = None
        self._RotateParagraphRect = None

    @property
    def SourceLineText(self):
        r"""当前行的原文本
        :rtype: str
        """
        return self._SourceLineText

    @SourceLineText.setter
    def SourceLineText(self, SourceLineText):
        self._SourceLineText = SourceLineText

    @property
    def TargetLineText(self):
        r"""当前行的译文
        :rtype: str
        """
        return self._TargetLineText

    @TargetLineText.setter
    def TargetLineText(self, TargetLineText):
        self._TargetLineText = TargetLineText

    @property
    def BoundingBox(self):
        r"""段落文本框位置
        :rtype: :class:`tencentcloud.tmt.v20180321.models.BoundingBox`
        """
        return self._BoundingBox

    @BoundingBox.setter
    def BoundingBox(self, BoundingBox):
        self._BoundingBox = BoundingBox

    @property
    def LinesCount(self):
        r"""行数
        :rtype: int
        """
        return self._LinesCount

    @LinesCount.setter
    def LinesCount(self, LinesCount):
        self._LinesCount = LinesCount

    @property
    def LineHeight(self):
        r"""行高
        :rtype: int
        """
        return self._LineHeight

    @LineHeight.setter
    def LineHeight(self, LineHeight):
        self._LineHeight = LineHeight

    @property
    def SpamCode(self):
        r"""正常段落spam_code字段为0；如果存在spam_code字段且值大于0（1: 命中垃圾检查；2: 命中安全策略；3: 其他。），则命中安全检查被过滤。
        :rtype: int
        """
        return self._SpamCode

    @SpamCode.setter
    def SpamCode(self, SpamCode):
        self._SpamCode = SpamCode

    @property
    def RotateParagraphRect(self):
        r"""段落文本旋转信息，只在valid为true时表示坐标有效
        :rtype: :class:`tencentcloud.tmt.v20180321.models.RotateParagraphRect`
        """
        return self._RotateParagraphRect

    @RotateParagraphRect.setter
    def RotateParagraphRect(self, RotateParagraphRect):
        self._RotateParagraphRect = RotateParagraphRect


    def _deserialize(self, params):
        self._SourceLineText = params.get("SourceLineText")
        self._TargetLineText = params.get("TargetLineText")
        if params.get("BoundingBox") is not None:
            self._BoundingBox = BoundingBox()
            self._BoundingBox._deserialize(params.get("BoundingBox"))
        self._LinesCount = params.get("LinesCount")
        self._LineHeight = params.get("LineHeight")
        self._SpamCode = params.get("SpamCode")
        if params.get("RotateParagraphRect") is not None:
            self._RotateParagraphRect = RotateParagraphRect()
            self._RotateParagraphRect._deserialize(params.get("RotateParagraphRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        