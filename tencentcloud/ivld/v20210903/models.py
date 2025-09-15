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


class AddCustomPersonImageRequest(AbstractModel):
    r"""AddCustomPersonImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 自定义人物Id
        :type PersonId: str
        :param _ImageURL: 自定义人物图片地址
        :type ImageURL: str
        :param _Image: 图片数据base64之后的结果
        :type Image: str
        """
        self._PersonId = None
        self._ImageURL = None
        self._Image = None

    @property
    def PersonId(self):
        r"""自定义人物Id
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def ImageURL(self):
        r"""自定义人物图片地址
        :rtype: str
        """
        return self._ImageURL

    @ImageURL.setter
    def ImageURL(self, ImageURL):
        self._ImageURL = ImageURL

    @property
    def Image(self):
        r"""图片数据base64之后的结果
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._ImageURL = params.get("ImageURL")
        self._Image = params.get("Image")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCustomPersonImageResponse(AbstractModel):
    r"""AddCustomPersonImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 自定义人物Id
        :type PersonId: str
        :param _ImageInfo: 自定义人脸图片信息
        :type ImageInfo: :class:`tencentcloud.ivld.v20210903.models.PersonImageInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PersonId = None
        self._ImageInfo = None
        self._RequestId = None

    @property
    def PersonId(self):
        r"""自定义人物Id
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def ImageInfo(self):
        r"""自定义人脸图片信息
        :rtype: :class:`tencentcloud.ivld.v20210903.models.PersonImageInfo`
        """
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

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
        self._PersonId = params.get("PersonId")
        if params.get("ImageInfo") is not None:
            self._ImageInfo = PersonImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        self._RequestId = params.get("RequestId")


class AppearIndexPair(AbstractModel):
    r"""出现信息索引对

    AppearIndex可选值定义如下：

    | AppearIndex名称 | AppearIndex取值 | AppearIndex描述 |
    |---|---|---|
    | APPEAR_INDEX_INVALID | 0 | 非法的任务状态 |
    | APPEAR_INDEX_AUDIO | 1 | 音频出现信息|
    | APPEAR_INDEX_TEXT | 2 | 可视文本出现信息|
    | APPEAR_INDEX_VIDEO | 3 | 视频出现信息|

    例如，当AppearIndex=1，Index=15，则意味着目标关键词出现在第16个(Index计数从0开始)音频文字识别结果之中

    """

    def __init__(self):
        r"""
        :param _AppearIndex: 出现信息，取值范围为[1，3]
        :type AppearIndex: int
        :param _Index: AppearInfo中AppearIndex对应元素的第Index元素，从0开始计数
        :type Index: int
        """
        self._AppearIndex = None
        self._Index = None

    @property
    def AppearIndex(self):
        r"""出现信息，取值范围为[1，3]
        :rtype: int
        """
        return self._AppearIndex

    @AppearIndex.setter
    def AppearIndex(self, AppearIndex):
        self._AppearIndex = AppearIndex

    @property
    def Index(self):
        r"""AppearInfo中AppearIndex对应元素的第Index元素，从0开始计数
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._AppearIndex = params.get("AppearIndex")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppearInfo(AbstractModel):
    r"""出现信息结构

    包含关键词在音频转文字(ASR)，图片转文字(OCR)以及视频结果中的出现信息

    """

    def __init__(self):
        r"""
        :param _AudioAppearSet: 关键词在音频文本结果中的出现位置数组
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioAppearSet: list of TextAppearInfo
        :param _TextAppearSet: 关键词在可视文本结果中的出现位置数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TextAppearSet: list of TextAppearInfo
        :param _VideoAppearSet: 关键词在视频信息中的出现位置数组
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoAppearSet: list of VideoAppearInfo
        """
        self._AudioAppearSet = None
        self._TextAppearSet = None
        self._VideoAppearSet = None

    @property
    def AudioAppearSet(self):
        r"""关键词在音频文本结果中的出现位置数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TextAppearInfo
        """
        return self._AudioAppearSet

    @AudioAppearSet.setter
    def AudioAppearSet(self, AudioAppearSet):
        self._AudioAppearSet = AudioAppearSet

    @property
    def TextAppearSet(self):
        r"""关键词在可视文本结果中的出现位置数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TextAppearInfo
        """
        return self._TextAppearSet

    @TextAppearSet.setter
    def TextAppearSet(self, TextAppearSet):
        self._TextAppearSet = TextAppearSet

    @property
    def VideoAppearSet(self):
        r"""关键词在视频信息中的出现位置数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of VideoAppearInfo
        """
        return self._VideoAppearSet

    @VideoAppearSet.setter
    def VideoAppearSet(self, VideoAppearSet):
        self._VideoAppearSet = VideoAppearSet


    def _deserialize(self, params):
        if params.get("AudioAppearSet") is not None:
            self._AudioAppearSet = []
            for item in params.get("AudioAppearSet"):
                obj = TextAppearInfo()
                obj._deserialize(item)
                self._AudioAppearSet.append(obj)
        if params.get("TextAppearSet") is not None:
            self._TextAppearSet = []
            for item in params.get("TextAppearSet"):
                obj = TextAppearInfo()
                obj._deserialize(item)
                self._TextAppearSet.append(obj)
        if params.get("VideoAppearSet") is not None:
            self._VideoAppearSet = []
            for item in params.get("VideoAppearSet"):
                obj = VideoAppearInfo()
                obj._deserialize(item)
                self._VideoAppearSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrResult(AbstractModel):
    r"""一条 asr 语音结果的结构

    """

    def __init__(self):
        r"""
        :param _Content: ASR提取的文字信息
        :type Content: str
        :param _StartTimeStamp: ASR起始时间戳，从0开始
        :type StartTimeStamp: float
        :param _EndTimeStamp: ASR结束时间戳，从0开始
        :type EndTimeStamp: float
        """
        self._Content = None
        self._StartTimeStamp = None
        self._EndTimeStamp = None

    @property
    def Content(self):
        r"""ASR提取的文字信息
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def StartTimeStamp(self):
        r"""ASR起始时间戳，从0开始
        :rtype: float
        """
        return self._StartTimeStamp

    @StartTimeStamp.setter
    def StartTimeStamp(self, StartTimeStamp):
        self._StartTimeStamp = StartTimeStamp

    @property
    def EndTimeStamp(self):
        r"""ASR结束时间戳，从0开始
        :rtype: float
        """
        return self._EndTimeStamp

    @EndTimeStamp.setter
    def EndTimeStamp(self, EndTimeStamp):
        self._EndTimeStamp = EndTimeStamp


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._StartTimeStamp = params.get("StartTimeStamp")
        self._EndTimeStamp = params.get("EndTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioData(AbstractModel):
    r"""音频文件分析结果数据

    """

    def __init__(self):
        r"""
        :param _AudioInfoSet: 音频识别文本结果
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioInfoSet: list of AudioInfo
        :param _TextTagSet: 音频识别标签数据
        :type TextTagSet: :class:`tencentcloud.ivld.v20210903.models.MultiLevelTag`
        :param _WebMediaURL: 音频下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type WebMediaURL: str
        """
        self._AudioInfoSet = None
        self._TextTagSet = None
        self._WebMediaURL = None

    @property
    def AudioInfoSet(self):
        r"""音频识别文本结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AudioInfo
        """
        return self._AudioInfoSet

    @AudioInfoSet.setter
    def AudioInfoSet(self, AudioInfoSet):
        self._AudioInfoSet = AudioInfoSet

    @property
    def TextTagSet(self):
        r"""音频识别标签数据
        :rtype: :class:`tencentcloud.ivld.v20210903.models.MultiLevelTag`
        """
        return self._TextTagSet

    @TextTagSet.setter
    def TextTagSet(self, TextTagSet):
        self._TextTagSet = TextTagSet

    @property
    def WebMediaURL(self):
        r"""音频下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WebMediaURL

    @WebMediaURL.setter
    def WebMediaURL(self, WebMediaURL):
        self._WebMediaURL = WebMediaURL


    def _deserialize(self, params):
        if params.get("AudioInfoSet") is not None:
            self._AudioInfoSet = []
            for item in params.get("AudioInfoSet"):
                obj = AudioInfo()
                obj._deserialize(item)
                self._AudioInfoSet.append(obj)
        if params.get("TextTagSet") is not None:
            self._TextTagSet = MultiLevelTag()
            self._TextTagSet._deserialize(params.get("TextTagSet"))
        self._WebMediaURL = params.get("WebMediaURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioInfo(AbstractModel):
    r"""音频识别结果信息

    """

    def __init__(self):
        r"""
        :param _Content: ASR提取的文字信息
        :type Content: str
        :param _StartTimeStamp: ASR起始时间戳，从0开始
        :type StartTimeStamp: float
        :param _EndTimeStamp: ASR结束时间戳，从0开始
        :type EndTimeStamp: float
        :param _Tag: ASR提取的音频标签
        :type Tag: str
        """
        self._Content = None
        self._StartTimeStamp = None
        self._EndTimeStamp = None
        self._Tag = None

    @property
    def Content(self):
        r"""ASR提取的文字信息
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def StartTimeStamp(self):
        r"""ASR起始时间戳，从0开始
        :rtype: float
        """
        return self._StartTimeStamp

    @StartTimeStamp.setter
    def StartTimeStamp(self, StartTimeStamp):
        self._StartTimeStamp = StartTimeStamp

    @property
    def EndTimeStamp(self):
        r"""ASR结束时间戳，从0开始
        :rtype: float
        """
        return self._EndTimeStamp

    @EndTimeStamp.setter
    def EndTimeStamp(self, EndTimeStamp):
        self._EndTimeStamp = EndTimeStamp

    @property
    def Tag(self):
        r"""ASR提取的音频标签
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._StartTimeStamp = params.get("StartTimeStamp")
        self._EndTimeStamp = params.get("EndTimeStamp")
        self._Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioMetadata(AbstractModel):
    r"""音频文件元信息

    """

    def __init__(self):
        r"""
        :param _FileSize: 媒资音频文件大小，单位为Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param _MD5: 媒资音频文件MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type MD5: str
        :param _Duration: 媒资音频时长，单位为秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: float
        :param _SampleRate: 媒资音频采样率，单位为khz
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleRate: float
        :param _BitRate: 媒资音频码率，单位为kbps
注意：此字段可能返回 null，表示取不到有效值。
        :type BitRate: int
        :param _Format: 媒资音频文件格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Format: str
        :param _BitDepth: Audio Bit Depth: 16/24 bit .etc
注意：此字段可能返回 null，表示取不到有效值。
        :type BitDepth: int
        :param _ShortFormat: 封装格式短后缀
注意：此字段可能返回 null，表示取不到有效值。
        :type ShortFormat: str
        """
        self._FileSize = None
        self._MD5 = None
        self._Duration = None
        self._SampleRate = None
        self._BitRate = None
        self._Format = None
        self._BitDepth = None
        self._ShortFormat = None

    @property
    def FileSize(self):
        r"""媒资音频文件大小，单位为Byte
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def MD5(self):
        r"""媒资音频文件MD5
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MD5

    @MD5.setter
    def MD5(self, MD5):
        self._MD5 = MD5

    @property
    def Duration(self):
        r"""媒资音频时长，单位为秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def SampleRate(self):
        r"""媒资音频采样率，单位为khz
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def BitRate(self):
        r"""媒资音频码率，单位为kbps
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Format(self):
        r"""媒资音频文件格式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def BitDepth(self):
        r"""Audio Bit Depth: 16/24 bit .etc
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BitDepth

    @BitDepth.setter
    def BitDepth(self, BitDepth):
        self._BitDepth = BitDepth

    @property
    def ShortFormat(self):
        r"""封装格式短后缀
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ShortFormat

    @ShortFormat.setter
    def ShortFormat(self, ShortFormat):
        self._ShortFormat = ShortFormat


    def _deserialize(self, params):
        self._FileSize = params.get("FileSize")
        self._MD5 = params.get("MD5")
        self._Duration = params.get("Duration")
        self._SampleRate = params.get("SampleRate")
        self._BitRate = params.get("BitRate")
        self._Format = params.get("Format")
        self._BitDepth = params.get("BitDepth")
        self._ShortFormat = params.get("ShortFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifiedPersonInfo(AbstractModel):
    r"""已分类的人物信息

    """

    def __init__(self):
        r"""
        :param _ClassifyName: 人物分类名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassifyName: str
        :param _PersonInfoSet: 符合特定分类的人物信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonInfoSet: list of PersonInfo
        """
        self._ClassifyName = None
        self._PersonInfoSet = None

    @property
    def ClassifyName(self):
        r"""人物分类名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClassifyName

    @ClassifyName.setter
    def ClassifyName(self, ClassifyName):
        self._ClassifyName = ClassifyName

    @property
    def PersonInfoSet(self):
        r"""符合特定分类的人物信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PersonInfo
        """
        return self._PersonInfoSet

    @PersonInfoSet.setter
    def PersonInfoSet(self, PersonInfoSet):
        self._PersonInfoSet = PersonInfoSet


    def _deserialize(self, params):
        self._ClassifyName = params.get("ClassifyName")
        if params.get("PersonInfoSet") is not None:
            self._PersonInfoSet = []
            for item in params.get("PersonInfoSet"):
                obj = PersonInfo()
                obj._deserialize(item)
                self._PersonInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomCategoryRequest(AbstractModel):
    r"""CreateCustomCategory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _L1Category: 自定义一级类型
        :type L1Category: str
        :param _L2Category: 自定义二级类型
        :type L2Category: str
        """
        self._L1Category = None
        self._L2Category = None

    @property
    def L1Category(self):
        r"""自定义一级类型
        :rtype: str
        """
        return self._L1Category

    @L1Category.setter
    def L1Category(self, L1Category):
        self._L1Category = L1Category

    @property
    def L2Category(self):
        r"""自定义二级类型
        :rtype: str
        """
        return self._L2Category

    @L2Category.setter
    def L2Category(self, L2Category):
        self._L2Category = L2Category


    def _deserialize(self, params):
        self._L1Category = params.get("L1Category")
        self._L2Category = params.get("L2Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomCategoryResponse(AbstractModel):
    r"""CreateCustomCategory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CategoryId: 自定义分类信息ID
        :type CategoryId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CategoryId = None
        self._RequestId = None

    @property
    def CategoryId(self):
        r"""自定义分类信息ID
        :rtype: str
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

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
        self._CategoryId = params.get("CategoryId")
        self._RequestId = params.get("RequestId")


class CreateCustomGroupRequest(AbstractModel):
    r"""CreateCustomGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Bucket: 人脸图片COS存储桶Host地址
        :type Bucket: str
        """
        self._Bucket = None

    @property
    def Bucket(self):
        r"""人脸图片COS存储桶Host地址
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket


    def _deserialize(self, params):
        self._Bucket = params.get("Bucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomGroupResponse(AbstractModel):
    r"""CreateCustomGroup返回参数结构体

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


class CreateCustomPersonRequest(AbstractModel):
    r"""CreateCustomPerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 自定义人物姓名
        :type Name: str
        :param _BasicInfo: 自定义人物简要信息(仅用于标记，不支持检索)
        :type BasicInfo: str
        :param _CategoryId: 自定义分类ID，如不存在接口会报错
        :type CategoryId: str
        :param _ImageURL: 自定义人物图片URL，可支持任意地址，推荐使用COS
        :type ImageURL: str
        :param _Image: 原始图片base64编码后的数据
        :type Image: str
        """
        self._Name = None
        self._BasicInfo = None
        self._CategoryId = None
        self._ImageURL = None
        self._Image = None

    @property
    def Name(self):
        r"""自定义人物姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BasicInfo(self):
        r"""自定义人物简要信息(仅用于标记，不支持检索)
        :rtype: str
        """
        return self._BasicInfo

    @BasicInfo.setter
    def BasicInfo(self, BasicInfo):
        self._BasicInfo = BasicInfo

    @property
    def CategoryId(self):
        r"""自定义分类ID，如不存在接口会报错
        :rtype: str
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def ImageURL(self):
        r"""自定义人物图片URL，可支持任意地址，推荐使用COS
        :rtype: str
        """
        return self._ImageURL

    @ImageURL.setter
    def ImageURL(self, ImageURL):
        self._ImageURL = ImageURL

    @property
    def Image(self):
        r"""原始图片base64编码后的数据
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._BasicInfo = params.get("BasicInfo")
        self._CategoryId = params.get("CategoryId")
        self._ImageURL = params.get("ImageURL")
        self._Image = params.get("Image")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomPersonResponse(AbstractModel):
    r"""CreateCustomPerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 自定义人物Id
        :type PersonId: str
        :param _ImageInfo: 自定义人脸信息
        :type ImageInfo: :class:`tencentcloud.ivld.v20210903.models.PersonImageInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PersonId = None
        self._ImageInfo = None
        self._RequestId = None

    @property
    def PersonId(self):
        r"""自定义人物Id
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def ImageInfo(self):
        r"""自定义人脸信息
        :rtype: :class:`tencentcloud.ivld.v20210903.models.PersonImageInfo`
        """
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

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
        self._PersonId = params.get("PersonId")
        if params.get("ImageInfo") is not None:
            self._ImageInfo = PersonImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        self._RequestId = params.get("RequestId")


class CreateDefaultCategoriesRequest(AbstractModel):
    r"""CreateDefaultCategories请求参数结构体

    """


class CreateDefaultCategoriesResponse(AbstractModel):
    r"""CreateDefaultCategories返回参数结构体

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


class CreateTaskRequest(AbstractModel):
    r"""CreateTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MediaId: 媒资文件ID
        :type MediaId: str
        :param _MediaPreknownInfo: 媒资素材先验知识，相关限制参考MediaPreknownInfo
        :type MediaPreknownInfo: :class:`tencentcloud.ivld.v20210903.models.MediaPreknownInfo`
        :param _TaskName: 任务名称，最长100个中文字符
        :type TaskName: str
        :param _UploadVideo: 是否上传转码后的视频，仅设置true时上传，默认为false
        :type UploadVideo: bool
        :param _Label: 自定义标签，可用于查询
        :type Label: str
        :param _CallbackURL: 任务分析完成的回调地址，该设置优先级高于控制台全局的设置；
        :type CallbackURL: str
        """
        self._MediaId = None
        self._MediaPreknownInfo = None
        self._TaskName = None
        self._UploadVideo = None
        self._Label = None
        self._CallbackURL = None

    @property
    def MediaId(self):
        r"""媒资文件ID
        :rtype: str
        """
        return self._MediaId

    @MediaId.setter
    def MediaId(self, MediaId):
        self._MediaId = MediaId

    @property
    def MediaPreknownInfo(self):
        r"""媒资素材先验知识，相关限制参考MediaPreknownInfo
        :rtype: :class:`tencentcloud.ivld.v20210903.models.MediaPreknownInfo`
        """
        return self._MediaPreknownInfo

    @MediaPreknownInfo.setter
    def MediaPreknownInfo(self, MediaPreknownInfo):
        self._MediaPreknownInfo = MediaPreknownInfo

    @property
    def TaskName(self):
        r"""任务名称，最长100个中文字符
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def UploadVideo(self):
        r"""是否上传转码后的视频，仅设置true时上传，默认为false
        :rtype: bool
        """
        return self._UploadVideo

    @UploadVideo.setter
    def UploadVideo(self, UploadVideo):
        self._UploadVideo = UploadVideo

    @property
    def Label(self):
        r"""自定义标签，可用于查询
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def CallbackURL(self):
        r"""任务分析完成的回调地址，该设置优先级高于控制台全局的设置；
        :rtype: str
        """
        return self._CallbackURL

    @CallbackURL.setter
    def CallbackURL(self, CallbackURL):
        self._CallbackURL = CallbackURL


    def _deserialize(self, params):
        self._MediaId = params.get("MediaId")
        if params.get("MediaPreknownInfo") is not None:
            self._MediaPreknownInfo = MediaPreknownInfo()
            self._MediaPreknownInfo._deserialize(params.get("MediaPreknownInfo"))
        self._TaskName = params.get("TaskName")
        self._UploadVideo = params.get("UploadVideo")
        self._Label = params.get("Label")
        self._CallbackURL = params.get("CallbackURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskResponse(AbstractModel):
    r"""CreateTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 智能标签视频分析任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""智能标签视频分析任务ID
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


class CreateVideoSummaryTaskRequest(AbstractModel):
    r"""CreateVideoSummaryTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SummaryType: 目前只支持 1，表示新闻缩编。
        :type SummaryType: int
        :param _VideoURL: 待处理的视频的URL，目前只支持*不带签名的*COS地址，长度最长1KB
        :type VideoURL: str
        :param _CallbackURL: 任务处理完成的回调地址。
        :type CallbackURL: str
        :param _WriteBackCosPath: 如果需要你输出 TTS 或者视频，该字段为转存的cos桶地址且不可为空; 示例：https://${Bucket}-${AppId}.cos.${Region}.myqcloud.com/${PathPrefix}/  (注意，cos路径需要以/分隔符结尾)。

        :type WriteBackCosPath: str
        :param _ActiveVideoGenerate: 是否开启结果视频生成功能，如果开启，需要指定WriteBackCosPath 参数
        :type ActiveVideoGenerate: bool
        :param _VideoRotationMode: 生成结果视频的时候，控制生成的结果视频的横转竖参数。如果 ActiveVideoGenerate 为 false, 该参数无效。
        :type VideoRotationMode: :class:`tencentcloud.ivld.v20210903.models.VideoRotationMode`
        :param _TTSMode: 语音合成相关的控制参数
        :type TTSMode: :class:`tencentcloud.ivld.v20210903.models.TTSMode`
        :param _ActiveTTSOutput: 是否输出合成好的语音列表。
        :type ActiveTTSOutput: bool
        :param _ExactAsrSet: 用户指定的精确的 asr 结果列表 
        :type ExactAsrSet: list of AsrResult
        :param _ExactTextSummary: 用户指定的精确的文本摘要
        :type ExactTextSummary: str
        :param _ExactTextSegSet: 用户指定的精确的文本摘要分割结果
        :type ExactTextSegSet: list of str
        :param _ExactShotSegSet: 用户指定的精确的镜头分割结果
        :type ExactShotSegSet: list of ShotInfo
        """
        self._SummaryType = None
        self._VideoURL = None
        self._CallbackURL = None
        self._WriteBackCosPath = None
        self._ActiveVideoGenerate = None
        self._VideoRotationMode = None
        self._TTSMode = None
        self._ActiveTTSOutput = None
        self._ExactAsrSet = None
        self._ExactTextSummary = None
        self._ExactTextSegSet = None
        self._ExactShotSegSet = None

    @property
    def SummaryType(self):
        r"""目前只支持 1，表示新闻缩编。
        :rtype: int
        """
        return self._SummaryType

    @SummaryType.setter
    def SummaryType(self, SummaryType):
        self._SummaryType = SummaryType

    @property
    def VideoURL(self):
        r"""待处理的视频的URL，目前只支持*不带签名的*COS地址，长度最长1KB
        :rtype: str
        """
        return self._VideoURL

    @VideoURL.setter
    def VideoURL(self, VideoURL):
        self._VideoURL = VideoURL

    @property
    def CallbackURL(self):
        r"""任务处理完成的回调地址。
        :rtype: str
        """
        return self._CallbackURL

    @CallbackURL.setter
    def CallbackURL(self, CallbackURL):
        self._CallbackURL = CallbackURL

    @property
    def WriteBackCosPath(self):
        r"""如果需要你输出 TTS 或者视频，该字段为转存的cos桶地址且不可为空; 示例：https://${Bucket}-${AppId}.cos.${Region}.myqcloud.com/${PathPrefix}/  (注意，cos路径需要以/分隔符结尾)。

        :rtype: str
        """
        return self._WriteBackCosPath

    @WriteBackCosPath.setter
    def WriteBackCosPath(self, WriteBackCosPath):
        self._WriteBackCosPath = WriteBackCosPath

    @property
    def ActiveVideoGenerate(self):
        r"""是否开启结果视频生成功能，如果开启，需要指定WriteBackCosPath 参数
        :rtype: bool
        """
        return self._ActiveVideoGenerate

    @ActiveVideoGenerate.setter
    def ActiveVideoGenerate(self, ActiveVideoGenerate):
        self._ActiveVideoGenerate = ActiveVideoGenerate

    @property
    def VideoRotationMode(self):
        r"""生成结果视频的时候，控制生成的结果视频的横转竖参数。如果 ActiveVideoGenerate 为 false, 该参数无效。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.VideoRotationMode`
        """
        return self._VideoRotationMode

    @VideoRotationMode.setter
    def VideoRotationMode(self, VideoRotationMode):
        self._VideoRotationMode = VideoRotationMode

    @property
    def TTSMode(self):
        r"""语音合成相关的控制参数
        :rtype: :class:`tencentcloud.ivld.v20210903.models.TTSMode`
        """
        return self._TTSMode

    @TTSMode.setter
    def TTSMode(self, TTSMode):
        self._TTSMode = TTSMode

    @property
    def ActiveTTSOutput(self):
        r"""是否输出合成好的语音列表。
        :rtype: bool
        """
        return self._ActiveTTSOutput

    @ActiveTTSOutput.setter
    def ActiveTTSOutput(self, ActiveTTSOutput):
        self._ActiveTTSOutput = ActiveTTSOutput

    @property
    def ExactAsrSet(self):
        r"""用户指定的精确的 asr 结果列表 
        :rtype: list of AsrResult
        """
        return self._ExactAsrSet

    @ExactAsrSet.setter
    def ExactAsrSet(self, ExactAsrSet):
        self._ExactAsrSet = ExactAsrSet

    @property
    def ExactTextSummary(self):
        r"""用户指定的精确的文本摘要
        :rtype: str
        """
        return self._ExactTextSummary

    @ExactTextSummary.setter
    def ExactTextSummary(self, ExactTextSummary):
        self._ExactTextSummary = ExactTextSummary

    @property
    def ExactTextSegSet(self):
        r"""用户指定的精确的文本摘要分割结果
        :rtype: list of str
        """
        return self._ExactTextSegSet

    @ExactTextSegSet.setter
    def ExactTextSegSet(self, ExactTextSegSet):
        self._ExactTextSegSet = ExactTextSegSet

    @property
    def ExactShotSegSet(self):
        r"""用户指定的精确的镜头分割结果
        :rtype: list of ShotInfo
        """
        return self._ExactShotSegSet

    @ExactShotSegSet.setter
    def ExactShotSegSet(self, ExactShotSegSet):
        self._ExactShotSegSet = ExactShotSegSet


    def _deserialize(self, params):
        self._SummaryType = params.get("SummaryType")
        self._VideoURL = params.get("VideoURL")
        self._CallbackURL = params.get("CallbackURL")
        self._WriteBackCosPath = params.get("WriteBackCosPath")
        self._ActiveVideoGenerate = params.get("ActiveVideoGenerate")
        if params.get("VideoRotationMode") is not None:
            self._VideoRotationMode = VideoRotationMode()
            self._VideoRotationMode._deserialize(params.get("VideoRotationMode"))
        if params.get("TTSMode") is not None:
            self._TTSMode = TTSMode()
            self._TTSMode._deserialize(params.get("TTSMode"))
        self._ActiveTTSOutput = params.get("ActiveTTSOutput")
        if params.get("ExactAsrSet") is not None:
            self._ExactAsrSet = []
            for item in params.get("ExactAsrSet"):
                obj = AsrResult()
                obj._deserialize(item)
                self._ExactAsrSet.append(obj)
        self._ExactTextSummary = params.get("ExactTextSummary")
        self._ExactTextSegSet = params.get("ExactTextSegSet")
        if params.get("ExactShotSegSet") is not None:
            self._ExactShotSegSet = []
            for item in params.get("ExactShotSegSet"):
                obj = ShotInfo()
                obj._deserialize(item)
                self._ExactShotSegSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVideoSummaryTaskResponse(AbstractModel):
    r"""CreateVideoSummaryTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 返回的任务 id
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""返回的任务 id
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


class CustomCategory(AbstractModel):
    r"""自定义分类信息

    """

    def __init__(self):
        r"""
        :param _CategoryId: 自定义分类ID
        :type CategoryId: str
        :param _L1Category: 一级自定义类型
        :type L1Category: str
        :param _L2Category: 二级自定义类型
        :type L2Category: str
        """
        self._CategoryId = None
        self._L1Category = None
        self._L2Category = None

    @property
    def CategoryId(self):
        r"""自定义分类ID
        :rtype: str
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def L1Category(self):
        r"""一级自定义类型
        :rtype: str
        """
        return self._L1Category

    @L1Category.setter
    def L1Category(self, L1Category):
        self._L1Category = L1Category

    @property
    def L2Category(self):
        r"""二级自定义类型
        :rtype: str
        """
        return self._L2Category

    @L2Category.setter
    def L2Category(self, L2Category):
        self._L2Category = L2Category


    def _deserialize(self, params):
        self._CategoryId = params.get("CategoryId")
        self._L1Category = params.get("L1Category")
        self._L2Category = params.get("L2Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomPersonFilter(AbstractModel):
    r"""自定义人物批量查询过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 待查询的人物姓名
        :type Name: str
        :param _CategoryIdSet: 待过滤的自定义类型Id数组
        :type CategoryIdSet: list of str
        :param _PersonIdSet: 待过滤的自定义人物Id数组
        :type PersonIdSet: list of str
        :param _L1CategorySet: 一级自定义人物类型数组
        :type L1CategorySet: list of str
        """
        self._Name = None
        self._CategoryIdSet = None
        self._PersonIdSet = None
        self._L1CategorySet = None

    @property
    def Name(self):
        r"""待查询的人物姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CategoryIdSet(self):
        r"""待过滤的自定义类型Id数组
        :rtype: list of str
        """
        return self._CategoryIdSet

    @CategoryIdSet.setter
    def CategoryIdSet(self, CategoryIdSet):
        self._CategoryIdSet = CategoryIdSet

    @property
    def PersonIdSet(self):
        r"""待过滤的自定义人物Id数组
        :rtype: list of str
        """
        return self._PersonIdSet

    @PersonIdSet.setter
    def PersonIdSet(self, PersonIdSet):
        self._PersonIdSet = PersonIdSet

    @property
    def L1CategorySet(self):
        r"""一级自定义人物类型数组
        :rtype: list of str
        """
        return self._L1CategorySet

    @L1CategorySet.setter
    def L1CategorySet(self, L1CategorySet):
        self._L1CategorySet = L1CategorySet


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CategoryIdSet = params.get("CategoryIdSet")
        self._PersonIdSet = params.get("PersonIdSet")
        self._L1CategorySet = params.get("L1CategorySet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomPersonInfo(AbstractModel):
    r"""自定义人物信息

    """

    def __init__(self):
        r"""
        :param _PersonId: 自定义人物Id
        :type PersonId: str
        :param _Name: 自定义人物姓名
        :type Name: str
        :param _BasicInfo: 自定义人物简介信息
        :type BasicInfo: str
        :param _L1Category: 一级自定义人物类型
        :type L1Category: str
        :param _L2Category: 二级自定义人物类型
        :type L2Category: str
        :param _ImageInfoSet: 自定义人物图片信息
        :type ImageInfoSet: list of PersonImageInfo
        :param _CreateTime: 自定义人物创建时间
        :type CreateTime: str
        """
        self._PersonId = None
        self._Name = None
        self._BasicInfo = None
        self._L1Category = None
        self._L2Category = None
        self._ImageInfoSet = None
        self._CreateTime = None

    @property
    def PersonId(self):
        r"""自定义人物Id
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Name(self):
        r"""自定义人物姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BasicInfo(self):
        r"""自定义人物简介信息
        :rtype: str
        """
        return self._BasicInfo

    @BasicInfo.setter
    def BasicInfo(self, BasicInfo):
        self._BasicInfo = BasicInfo

    @property
    def L1Category(self):
        r"""一级自定义人物类型
        :rtype: str
        """
        return self._L1Category

    @L1Category.setter
    def L1Category(self, L1Category):
        self._L1Category = L1Category

    @property
    def L2Category(self):
        r"""二级自定义人物类型
        :rtype: str
        """
        return self._L2Category

    @L2Category.setter
    def L2Category(self, L2Category):
        self._L2Category = L2Category

    @property
    def ImageInfoSet(self):
        r"""自定义人物图片信息
        :rtype: list of PersonImageInfo
        """
        return self._ImageInfoSet

    @ImageInfoSet.setter
    def ImageInfoSet(self, ImageInfoSet):
        self._ImageInfoSet = ImageInfoSet

    @property
    def CreateTime(self):
        r"""自定义人物创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._Name = params.get("Name")
        self._BasicInfo = params.get("BasicInfo")
        self._L1Category = params.get("L1Category")
        self._L2Category = params.get("L2Category")
        if params.get("ImageInfoSet") is not None:
            self._ImageInfoSet = []
            for item in params.get("ImageInfoSet"):
                obj = PersonImageInfo()
                obj._deserialize(item)
                self._ImageInfoSet.append(obj)
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Data(AbstractModel):
    r"""任务结果数据

    """

    def __init__(self):
        r"""
        :param _ShowInfo: 节目粒度结构化结果
注意：此字段可能返回 null，表示取不到有效值。
        :type ShowInfo: :class:`tencentcloud.ivld.v20210903.models.ShowInfo`
        """
        self._ShowInfo = None

    @property
    def ShowInfo(self):
        r"""节目粒度结构化结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.ShowInfo`
        """
        return self._ShowInfo

    @ShowInfo.setter
    def ShowInfo(self, ShowInfo):
        self._ShowInfo = ShowInfo


    def _deserialize(self, params):
        if params.get("ShowInfo") is not None:
            self._ShowInfo = ShowInfo()
            self._ShowInfo._deserialize(params.get("ShowInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomCategoryRequest(AbstractModel):
    r"""DeleteCustomCategory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CategoryId: 自定义分类ID
        :type CategoryId: str
        """
        self._CategoryId = None

    @property
    def CategoryId(self):
        r"""自定义分类ID
        :rtype: str
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId


    def _deserialize(self, params):
        self._CategoryId = params.get("CategoryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomCategoryResponse(AbstractModel):
    r"""DeleteCustomCategory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CategoryId: 自定义分类ID
        :type CategoryId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CategoryId = None
        self._RequestId = None

    @property
    def CategoryId(self):
        r"""自定义分类ID
        :rtype: str
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

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
        self._CategoryId = params.get("CategoryId")
        self._RequestId = params.get("RequestId")


class DeleteCustomPersonImageRequest(AbstractModel):
    r"""DeleteCustomPersonImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 自定义人物Id
        :type PersonId: str
        :param _ImageId: 自定义人脸图片Id
        :type ImageId: str
        """
        self._PersonId = None
        self._ImageId = None

    @property
    def PersonId(self):
        r"""自定义人物Id
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def ImageId(self):
        r"""自定义人脸图片Id
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomPersonImageResponse(AbstractModel):
    r"""DeleteCustomPersonImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 自定义人物Id
        :type PersonId: str
        :param _ImageId: 已删除的人物图片Id
        :type ImageId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PersonId = None
        self._ImageId = None
        self._RequestId = None

    @property
    def PersonId(self):
        r"""自定义人物Id
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def ImageId(self):
        r"""已删除的人物图片Id
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

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
        self._PersonId = params.get("PersonId")
        self._ImageId = params.get("ImageId")
        self._RequestId = params.get("RequestId")


class DeleteCustomPersonRequest(AbstractModel):
    r"""DeleteCustomPerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 待删除的自定义人物ID
        :type PersonId: str
        """
        self._PersonId = None

    @property
    def PersonId(self):
        r"""待删除的自定义人物ID
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomPersonResponse(AbstractModel):
    r"""DeleteCustomPerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 已删除的自定义人物Id
        :type PersonId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PersonId = None
        self._RequestId = None

    @property
    def PersonId(self):
        r"""已删除的自定义人物Id
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

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
        self._PersonId = params.get("PersonId")
        self._RequestId = params.get("RequestId")


class DeleteMediaRequest(AbstractModel):
    r"""DeleteMedia请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MediaId: 媒资文件在系统中的ID
        :type MediaId: str
        """
        self._MediaId = None

    @property
    def MediaId(self):
        r"""媒资文件在系统中的ID
        :rtype: str
        """
        return self._MediaId

    @MediaId.setter
    def MediaId(self, MediaId):
        self._MediaId = MediaId


    def _deserialize(self, params):
        self._MediaId = params.get("MediaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMediaResponse(AbstractModel):
    r"""DeleteMedia返回参数结构体

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


class DeleteTaskRequest(AbstractModel):
    r"""DeleteTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""任务Id
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
        


class DeleteTaskResponse(AbstractModel):
    r"""DeleteTask返回参数结构体

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


class DescribeCustomCategoriesRequest(AbstractModel):
    r"""DescribeCustomCategories请求参数结构体

    """


class DescribeCustomCategoriesResponse(AbstractModel):
    r"""DescribeCustomCategories返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CategorySet: 自定义人物类型数组
        :type CategorySet: list of CustomCategory
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CategorySet = None
        self._RequestId = None

    @property
    def CategorySet(self):
        r"""自定义人物类型数组
        :rtype: list of CustomCategory
        """
        return self._CategorySet

    @CategorySet.setter
    def CategorySet(self, CategorySet):
        self._CategorySet = CategorySet

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
        if params.get("CategorySet") is not None:
            self._CategorySet = []
            for item in params.get("CategorySet"):
                obj = CustomCategory()
                obj._deserialize(item)
                self._CategorySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCustomGroupRequest(AbstractModel):
    r"""DescribeCustomGroup请求参数结构体

    """


class DescribeCustomGroupResponse(AbstractModel):
    r"""DescribeCustomGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupSize: 自定义人物库所包含的人物个数
        :type GroupSize: int
        :param _Bucket: 自定义人物库图片后续所在的存储桶
        :type Bucket: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupSize = None
        self._Bucket = None
        self._RequestId = None

    @property
    def GroupSize(self):
        r"""自定义人物库所包含的人物个数
        :rtype: int
        """
        return self._GroupSize

    @GroupSize.setter
    def GroupSize(self, GroupSize):
        self._GroupSize = GroupSize

    @property
    def Bucket(self):
        r"""自定义人物库图片后续所在的存储桶
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

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
        self._GroupSize = params.get("GroupSize")
        self._Bucket = params.get("Bucket")
        self._RequestId = params.get("RequestId")


class DescribeCustomPersonDetailRequest(AbstractModel):
    r"""DescribeCustomPersonDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 自定义人物Id
        :type PersonId: str
        """
        self._PersonId = None

    @property
    def PersonId(self):
        r"""自定义人物Id
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomPersonDetailResponse(AbstractModel):
    r"""DescribeCustomPersonDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonInfo: 自定义人物信息
        :type PersonInfo: :class:`tencentcloud.ivld.v20210903.models.CustomPersonInfo`
        :param _TaskIdSet: 出现该自定义人物的所有分析人物Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PersonInfo = None
        self._TaskIdSet = None
        self._RequestId = None

    @property
    def PersonInfo(self):
        r"""自定义人物信息
        :rtype: :class:`tencentcloud.ivld.v20210903.models.CustomPersonInfo`
        """
        return self._PersonInfo

    @PersonInfo.setter
    def PersonInfo(self, PersonInfo):
        self._PersonInfo = PersonInfo

    @property
    def TaskIdSet(self):
        r"""出现该自定义人物的所有分析人物Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._TaskIdSet

    @TaskIdSet.setter
    def TaskIdSet(self, TaskIdSet):
        self._TaskIdSet = TaskIdSet

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
        if params.get("PersonInfo") is not None:
            self._PersonInfo = CustomPersonInfo()
            self._PersonInfo._deserialize(params.get("PersonInfo"))
        self._TaskIdSet = params.get("TaskIdSet")
        self._RequestId = params.get("RequestId")


class DescribeCustomPersonsRequest(AbstractModel):
    r"""DescribeCustomPersons请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 分页序号，从1开始
        :type PageNumber: int
        :param _PageSize: 分页数据行数，最多50
        :type PageSize: int
        :param _SortBy: 排序信息，默认倒序
        :type SortBy: :class:`tencentcloud.ivld.v20210903.models.SortBy`
        :param _Filter: 自定义人物过滤条件
        :type Filter: :class:`tencentcloud.ivld.v20210903.models.CustomPersonFilter`
        """
        self._PageNumber = None
        self._PageSize = None
        self._SortBy = None
        self._Filter = None

    @property
    def PageNumber(self):
        r"""分页序号，从1开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""分页数据行数，最多50
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SortBy(self):
        r"""排序信息，默认倒序
        :rtype: :class:`tencentcloud.ivld.v20210903.models.SortBy`
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Filter(self):
        r"""自定义人物过滤条件
        :rtype: :class:`tencentcloud.ivld.v20210903.models.CustomPersonFilter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("SortBy") is not None:
            self._SortBy = SortBy()
            self._SortBy._deserialize(params.get("SortBy"))
        if params.get("Filter") is not None:
            self._Filter = CustomPersonFilter()
            self._Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomPersonsResponse(AbstractModel):
    r"""DescribeCustomPersons返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 满足过滤条件的自定义人物数量
        :type TotalCount: int
        :param _PersonInfoSet: 自定义人物信息
        :type PersonInfoSet: list of CustomPersonInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._PersonInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""满足过滤条件的自定义人物数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PersonInfoSet(self):
        r"""自定义人物信息
        :rtype: list of CustomPersonInfo
        """
        return self._PersonInfoSet

    @PersonInfoSet.setter
    def PersonInfoSet(self, PersonInfoSet):
        self._PersonInfoSet = PersonInfoSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("PersonInfoSet") is not None:
            self._PersonInfoSet = []
            for item in params.get("PersonInfoSet"):
                obj = CustomPersonInfo()
                obj._deserialize(item)
                self._PersonInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMediaRequest(AbstractModel):
    r"""DescribeMedia请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MediaId: 导入媒资返回的媒资ID
        :type MediaId: str
        """
        self._MediaId = None

    @property
    def MediaId(self):
        r"""导入媒资返回的媒资ID
        :rtype: str
        """
        return self._MediaId

    @MediaId.setter
    def MediaId(self, MediaId):
        self._MediaId = MediaId


    def _deserialize(self, params):
        self._MediaId = params.get("MediaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaResponse(AbstractModel):
    r"""DescribeMedia返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MediaInfo: 媒资信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaInfo: :class:`tencentcloud.ivld.v20210903.models.MediaInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MediaInfo = None
        self._RequestId = None

    @property
    def MediaInfo(self):
        r"""媒资信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.MediaInfo`
        """
        return self._MediaInfo

    @MediaInfo.setter
    def MediaInfo(self, MediaInfo):
        self._MediaInfo = MediaInfo

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
        if params.get("MediaInfo") is not None:
            self._MediaInfo = MediaInfo()
            self._MediaInfo._deserialize(params.get("MediaInfo"))
        self._RequestId = params.get("RequestId")


class DescribeMediasRequest(AbstractModel):
    r"""DescribeMedias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 分页序号，从1开始
        :type PageNumber: int
        :param _PageSize: 每个分页所包含的元素数量，最大为50
        :type PageSize: int
        :param _MediaFilter: 列举过滤条件，相关限制相见MediaFilter
        :type MediaFilter: :class:`tencentcloud.ivld.v20210903.models.MediaFilter`
        :param _SortBy: 返回结果排序信息，By字段只支持CreateTime
        :type SortBy: :class:`tencentcloud.ivld.v20210903.models.SortBy`
        """
        self._PageNumber = None
        self._PageSize = None
        self._MediaFilter = None
        self._SortBy = None

    @property
    def PageNumber(self):
        r"""分页序号，从1开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每个分页所包含的元素数量，最大为50
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def MediaFilter(self):
        r"""列举过滤条件，相关限制相见MediaFilter
        :rtype: :class:`tencentcloud.ivld.v20210903.models.MediaFilter`
        """
        return self._MediaFilter

    @MediaFilter.setter
    def MediaFilter(self, MediaFilter):
        self._MediaFilter = MediaFilter

    @property
    def SortBy(self):
        r"""返回结果排序信息，By字段只支持CreateTime
        :rtype: :class:`tencentcloud.ivld.v20210903.models.SortBy`
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("MediaFilter") is not None:
            self._MediaFilter = MediaFilter()
            self._MediaFilter._deserialize(params.get("MediaFilter"))
        if params.get("SortBy") is not None:
            self._SortBy = SortBy()
            self._SortBy._deserialize(params.get("SortBy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediasResponse(AbstractModel):
    r"""DescribeMedias返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 满足过滤条件的媒资视频总数量
        :type TotalCount: int
        :param _MediaInfoSet: 满足过滤条件的媒资信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaInfoSet: list of MediaInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._MediaInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""满足过滤条件的媒资视频总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MediaInfoSet(self):
        r"""满足过滤条件的媒资信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MediaInfo
        """
        return self._MediaInfoSet

    @MediaInfoSet.setter
    def MediaInfoSet(self, MediaInfoSet):
        self._MediaInfoSet = MediaInfoSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("MediaInfoSet") is not None:
            self._MediaInfoSet = []
            for item in params.get("MediaInfoSet"):
                obj = MediaInfo()
                obj._deserialize(item)
                self._MediaInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    r"""DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 创建任务返回的TaskId
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""创建任务返回的TaskId
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
        


class DescribeTaskDetailResponse(AbstractModel):
    r"""DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskInfo: 任务信息，不包含任务结果
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskInfo: :class:`tencentcloud.ivld.v20210903.models.TaskInfo`
        :param _TaskData: 视频任务结果数据，只在视频任务结束时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskData: :class:`tencentcloud.ivld.v20210903.models.Data`
        :param _ImageTaskData: 图片任务结果数据，只在图片任务结束时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageTaskData: :class:`tencentcloud.ivld.v20210903.models.ImageData`
        :param _AudioTaskData: 音频任务结果数据，只在音频任务结束时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioTaskData: :class:`tencentcloud.ivld.v20210903.models.AudioData`
        :param _TextTaskData: 文本任务结果数据，只在文本任务结束时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type TextTaskData: :class:`tencentcloud.ivld.v20210903.models.TextData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskInfo = None
        self._TaskData = None
        self._ImageTaskData = None
        self._AudioTaskData = None
        self._TextTaskData = None
        self._RequestId = None

    @property
    def TaskInfo(self):
        r"""任务信息，不包含任务结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.TaskInfo`
        """
        return self._TaskInfo

    @TaskInfo.setter
    def TaskInfo(self, TaskInfo):
        self._TaskInfo = TaskInfo

    @property
    def TaskData(self):
        r"""视频任务结果数据，只在视频任务结束时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.Data`
        """
        return self._TaskData

    @TaskData.setter
    def TaskData(self, TaskData):
        self._TaskData = TaskData

    @property
    def ImageTaskData(self):
        r"""图片任务结果数据，只在图片任务结束时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.ImageData`
        """
        return self._ImageTaskData

    @ImageTaskData.setter
    def ImageTaskData(self, ImageTaskData):
        self._ImageTaskData = ImageTaskData

    @property
    def AudioTaskData(self):
        r"""音频任务结果数据，只在音频任务结束时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.AudioData`
        """
        return self._AudioTaskData

    @AudioTaskData.setter
    def AudioTaskData(self, AudioTaskData):
        self._AudioTaskData = AudioTaskData

    @property
    def TextTaskData(self):
        r"""文本任务结果数据，只在文本任务结束时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.TextData`
        """
        return self._TextTaskData

    @TextTaskData.setter
    def TextTaskData(self, TextTaskData):
        self._TextTaskData = TextTaskData

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
        if params.get("TaskInfo") is not None:
            self._TaskInfo = TaskInfo()
            self._TaskInfo._deserialize(params.get("TaskInfo"))
        if params.get("TaskData") is not None:
            self._TaskData = Data()
            self._TaskData._deserialize(params.get("TaskData"))
        if params.get("ImageTaskData") is not None:
            self._ImageTaskData = ImageData()
            self._ImageTaskData._deserialize(params.get("ImageTaskData"))
        if params.get("AudioTaskData") is not None:
            self._AudioTaskData = AudioData()
            self._AudioTaskData._deserialize(params.get("AudioTaskData"))
        if params.get("TextTaskData") is not None:
            self._TextTaskData = TextData()
            self._TextTaskData._deserialize(params.get("TextTaskData"))
        self._RequestId = params.get("RequestId")


class DescribeTaskRequest(AbstractModel):
    r"""DescribeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: CreateTask返回的任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""CreateTask返回的任务ID
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
        


class DescribeTaskResponse(AbstractModel):
    r"""DescribeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskInfo: 任务信息，详情参见TaskInfo的定义
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskInfo: :class:`tencentcloud.ivld.v20210903.models.TaskInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskInfo = None
        self._RequestId = None

    @property
    def TaskInfo(self):
        r"""任务信息，详情参见TaskInfo的定义
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.TaskInfo`
        """
        return self._TaskInfo

    @TaskInfo.setter
    def TaskInfo(self, TaskInfo):
        self._TaskInfo = TaskInfo

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
        if params.get("TaskInfo") is not None:
            self._TaskInfo = TaskInfo()
            self._TaskInfo._deserialize(params.get("TaskInfo"))
        self._RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    r"""DescribeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 分页序号，从1开始
        :type PageNumber: int
        :param _PageSize: 每个分页所包含的元素数量，最大为50
        :type PageSize: int
        :param _TaskFilter: 任务过滤条件，相关限制参见TaskFilter
        :type TaskFilter: :class:`tencentcloud.ivld.v20210903.models.TaskFilter`
        :param _SortBy: 返回结果排序信息，By字段只支持CreateTimeStamp
        :type SortBy: :class:`tencentcloud.ivld.v20210903.models.SortBy`
        """
        self._PageNumber = None
        self._PageSize = None
        self._TaskFilter = None
        self._SortBy = None

    @property
    def PageNumber(self):
        r"""分页序号，从1开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每个分页所包含的元素数量，最大为50
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TaskFilter(self):
        r"""任务过滤条件，相关限制参见TaskFilter
        :rtype: :class:`tencentcloud.ivld.v20210903.models.TaskFilter`
        """
        return self._TaskFilter

    @TaskFilter.setter
    def TaskFilter(self, TaskFilter):
        self._TaskFilter = TaskFilter

    @property
    def SortBy(self):
        r"""返回结果排序信息，By字段只支持CreateTimeStamp
        :rtype: :class:`tencentcloud.ivld.v20210903.models.SortBy`
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("TaskFilter") is not None:
            self._TaskFilter = TaskFilter()
            self._TaskFilter._deserialize(params.get("TaskFilter"))
        if params.get("SortBy") is not None:
            self._SortBy = SortBy()
            self._SortBy._deserialize(params.get("SortBy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    r"""DescribeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 满足过滤条件的任务总数量
        :type TotalCount: int
        :param _TaskInfoSet: 满足过滤条件的任务数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskInfoSet: list of TaskInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TaskInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""满足过滤条件的任务总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TaskInfoSet(self):
        r"""满足过滤条件的任务数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TaskInfo
        """
        return self._TaskInfoSet

    @TaskInfoSet.setter
    def TaskInfoSet(self, TaskInfoSet):
        self._TaskInfoSet = TaskInfoSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("TaskInfoSet") is not None:
            self._TaskInfoSet = []
            for item in params.get("TaskInfoSet"):
                obj = TaskInfo()
                obj._deserialize(item)
                self._TaskInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUsageAmountRequest(AbstractModel):
    r"""DescribeUsageAmount请求参数结构体

    """


class DescribeUsageAmountResponse(AbstractModel):
    r"""DescribeUsageAmount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UsedHours: 资源使用小时数
        :type UsedHours: float
        :param _TotalHours: 资源包总量小时数
        :type TotalHours: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UsedHours = None
        self._TotalHours = None
        self._RequestId = None

    @property
    def UsedHours(self):
        r"""资源使用小时数
        :rtype: float
        """
        return self._UsedHours

    @UsedHours.setter
    def UsedHours(self, UsedHours):
        self._UsedHours = UsedHours

    @property
    def TotalHours(self):
        r"""资源包总量小时数
        :rtype: float
        """
        return self._TotalHours

    @TotalHours.setter
    def TotalHours(self, TotalHours):
        self._TotalHours = TotalHours

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
        self._UsedHours = params.get("UsedHours")
        self._TotalHours = params.get("TotalHours")
        self._RequestId = params.get("RequestId")


class DescribeVideoSummaryDetailRequest(AbstractModel):
    r"""DescribeVideoSummaryDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 要查询的任务Id
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""要查询的任务Id
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
        


class DescribeVideoSummaryDetailResponse(AbstractModel):
    r"""DescribeVideoSummaryDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务的状态
1: 等待处理中
2: 处理中
3: 处理成功
4: 处理失败
        :type Status: int
        :param _FailedReason: 如果处理失败，返回失败的原因
        :type FailedReason: str
        :param _AsrSet: 提取出的视频的 Asr 结果
        :type AsrSet: list of AsrResult
        :param _TextSummary: 文本摘要结果
        :type TextSummary: str
        :param _TextSegSet: 文本摘要分割结果
        :type TextSegSet: list of str
        :param _ShotSegSet: 镜头分割结果
        :type ShotSegSet: list of ShotInfo
        :param _TextSegMatchShotScoreSet: 数组第 i 个结构 TextSegMatchShotConfidenceSet[i] 表示第 i 个文本摘要分割结果和所有镜头的匹配度。
        :type TextSegMatchShotScoreSet: list of TextSegMatchShotScore
        :param _TTSResultURLSet: TTS 输出音频下载地址列表
        :type TTSResultURLSet: list of str
        :param _VideoResultURL: 合成视频输出下载地址
        :type VideoResultURL: str
        :param _VideoRotateResultURL: 合成后的视频横竖屏转换后的视频下载地址
        :type VideoRotateResultURL: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._FailedReason = None
        self._AsrSet = None
        self._TextSummary = None
        self._TextSegSet = None
        self._ShotSegSet = None
        self._TextSegMatchShotScoreSet = None
        self._TTSResultURLSet = None
        self._VideoResultURL = None
        self._VideoRotateResultURL = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务的状态
1: 等待处理中
2: 处理中
3: 处理成功
4: 处理失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailedReason(self):
        r"""如果处理失败，返回失败的原因
        :rtype: str
        """
        return self._FailedReason

    @FailedReason.setter
    def FailedReason(self, FailedReason):
        self._FailedReason = FailedReason

    @property
    def AsrSet(self):
        r"""提取出的视频的 Asr 结果
        :rtype: list of AsrResult
        """
        return self._AsrSet

    @AsrSet.setter
    def AsrSet(self, AsrSet):
        self._AsrSet = AsrSet

    @property
    def TextSummary(self):
        r"""文本摘要结果
        :rtype: str
        """
        return self._TextSummary

    @TextSummary.setter
    def TextSummary(self, TextSummary):
        self._TextSummary = TextSummary

    @property
    def TextSegSet(self):
        r"""文本摘要分割结果
        :rtype: list of str
        """
        return self._TextSegSet

    @TextSegSet.setter
    def TextSegSet(self, TextSegSet):
        self._TextSegSet = TextSegSet

    @property
    def ShotSegSet(self):
        r"""镜头分割结果
        :rtype: list of ShotInfo
        """
        return self._ShotSegSet

    @ShotSegSet.setter
    def ShotSegSet(self, ShotSegSet):
        self._ShotSegSet = ShotSegSet

    @property
    def TextSegMatchShotScoreSet(self):
        r"""数组第 i 个结构 TextSegMatchShotConfidenceSet[i] 表示第 i 个文本摘要分割结果和所有镜头的匹配度。
        :rtype: list of TextSegMatchShotScore
        """
        return self._TextSegMatchShotScoreSet

    @TextSegMatchShotScoreSet.setter
    def TextSegMatchShotScoreSet(self, TextSegMatchShotScoreSet):
        self._TextSegMatchShotScoreSet = TextSegMatchShotScoreSet

    @property
    def TTSResultURLSet(self):
        r"""TTS 输出音频下载地址列表
        :rtype: list of str
        """
        return self._TTSResultURLSet

    @TTSResultURLSet.setter
    def TTSResultURLSet(self, TTSResultURLSet):
        self._TTSResultURLSet = TTSResultURLSet

    @property
    def VideoResultURL(self):
        r"""合成视频输出下载地址
        :rtype: str
        """
        return self._VideoResultURL

    @VideoResultURL.setter
    def VideoResultURL(self, VideoResultURL):
        self._VideoResultURL = VideoResultURL

    @property
    def VideoRotateResultURL(self):
        r"""合成后的视频横竖屏转换后的视频下载地址
        :rtype: str
        """
        return self._VideoRotateResultURL

    @VideoRotateResultURL.setter
    def VideoRotateResultURL(self, VideoRotateResultURL):
        self._VideoRotateResultURL = VideoRotateResultURL

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
        self._FailedReason = params.get("FailedReason")
        if params.get("AsrSet") is not None:
            self._AsrSet = []
            for item in params.get("AsrSet"):
                obj = AsrResult()
                obj._deserialize(item)
                self._AsrSet.append(obj)
        self._TextSummary = params.get("TextSummary")
        self._TextSegSet = params.get("TextSegSet")
        if params.get("ShotSegSet") is not None:
            self._ShotSegSet = []
            for item in params.get("ShotSegSet"):
                obj = ShotInfo()
                obj._deserialize(item)
                self._ShotSegSet.append(obj)
        if params.get("TextSegMatchShotScoreSet") is not None:
            self._TextSegMatchShotScoreSet = []
            for item in params.get("TextSegMatchShotScoreSet"):
                obj = TextSegMatchShotScore()
                obj._deserialize(item)
                self._TextSegMatchShotScoreSet.append(obj)
        self._TTSResultURLSet = params.get("TTSResultURLSet")
        self._VideoResultURL = params.get("VideoResultURL")
        self._VideoRotateResultURL = params.get("VideoRotateResultURL")
        self._RequestId = params.get("RequestId")


class ImageData(AbstractModel):
    r"""图片文件标签结果

    """

    def __init__(self):
        r"""
        :param _OcrSet: 图片中出现的可视文本识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrSet: list of ImageOcr
        :param _FrameTagSet: 图片中出现的帧标签识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameTagSet: :class:`tencentcloud.ivld.v20210903.models.MultiLevelTag`
        :param _MultiLevelPersonInfoSet: 图片中出现的层级人物识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiLevelPersonInfoSet: list of MultiLevelPersonInfo
        :param _TvLogo: 图片中出现的台标识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type TvLogo: :class:`tencentcloud.ivld.v20210903.models.ImageLogo`
        :param _SourceLogo: 图片中出现的来源信息识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceLogo: :class:`tencentcloud.ivld.v20210903.models.ImageLogo`
        """
        self._OcrSet = None
        self._FrameTagSet = None
        self._MultiLevelPersonInfoSet = None
        self._TvLogo = None
        self._SourceLogo = None

    @property
    def OcrSet(self):
        r"""图片中出现的可视文本识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ImageOcr
        """
        return self._OcrSet

    @OcrSet.setter
    def OcrSet(self, OcrSet):
        self._OcrSet = OcrSet

    @property
    def FrameTagSet(self):
        r"""图片中出现的帧标签识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.MultiLevelTag`
        """
        return self._FrameTagSet

    @FrameTagSet.setter
    def FrameTagSet(self, FrameTagSet):
        self._FrameTagSet = FrameTagSet

    @property
    def MultiLevelPersonInfoSet(self):
        r"""图片中出现的层级人物识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MultiLevelPersonInfo
        """
        return self._MultiLevelPersonInfoSet

    @MultiLevelPersonInfoSet.setter
    def MultiLevelPersonInfoSet(self, MultiLevelPersonInfoSet):
        self._MultiLevelPersonInfoSet = MultiLevelPersonInfoSet

    @property
    def TvLogo(self):
        r"""图片中出现的台标识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.ImageLogo`
        """
        return self._TvLogo

    @TvLogo.setter
    def TvLogo(self, TvLogo):
        self._TvLogo = TvLogo

    @property
    def SourceLogo(self):
        r"""图片中出现的来源信息识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.ImageLogo`
        """
        return self._SourceLogo

    @SourceLogo.setter
    def SourceLogo(self, SourceLogo):
        self._SourceLogo = SourceLogo


    def _deserialize(self, params):
        if params.get("OcrSet") is not None:
            self._OcrSet = []
            for item in params.get("OcrSet"):
                obj = ImageOcr()
                obj._deserialize(item)
                self._OcrSet.append(obj)
        if params.get("FrameTagSet") is not None:
            self._FrameTagSet = MultiLevelTag()
            self._FrameTagSet._deserialize(params.get("FrameTagSet"))
        if params.get("MultiLevelPersonInfoSet") is not None:
            self._MultiLevelPersonInfoSet = []
            for item in params.get("MultiLevelPersonInfoSet"):
                obj = MultiLevelPersonInfo()
                obj._deserialize(item)
                self._MultiLevelPersonInfoSet.append(obj)
        if params.get("TvLogo") is not None:
            self._TvLogo = ImageLogo()
            self._TvLogo._deserialize(params.get("TvLogo"))
        if params.get("SourceLogo") is not None:
            self._SourceLogo = ImageLogo()
            self._SourceLogo._deserialize(params.get("SourceLogo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageLogo(AbstractModel):
    r"""图片中出现的Logo信息

    """

    def __init__(self):
        r"""
        :param _Logo: 图片中出现的Logo识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Logo: str
        :param _AppearRect: Logo在图片中出现的位置
注意：此字段可能返回 null，表示取不到有效值。
        :type AppearRect: :class:`tencentcloud.ivld.v20210903.models.Rectf`
        """
        self._Logo = None
        self._AppearRect = None

    @property
    def Logo(self):
        r"""图片中出现的Logo识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def AppearRect(self):
        r"""Logo在图片中出现的位置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.Rectf`
        """
        return self._AppearRect

    @AppearRect.setter
    def AppearRect(self, AppearRect):
        self._AppearRect = AppearRect


    def _deserialize(self, params):
        self._Logo = params.get("Logo")
        if params.get("AppearRect") is not None:
            self._AppearRect = Rectf()
            self._AppearRect._deserialize(params.get("AppearRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageMetadata(AbstractModel):
    r"""图片文件元信息

    """

    def __init__(self):
        r"""
        :param _FileSize: 媒资图片文件大小，单位为Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param _MD5: 媒资图片文件MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type MD5: str
        :param _Width: 媒资图片文件宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param _Height: 媒资图片文件高度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param _Format: 媒资图片文件格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Format: str
        """
        self._FileSize = None
        self._MD5 = None
        self._Width = None
        self._Height = None
        self._Format = None

    @property
    def FileSize(self):
        r"""媒资图片文件大小，单位为Byte
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def MD5(self):
        r"""媒资图片文件MD5
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MD5

    @MD5.setter
    def MD5(self, MD5):
        self._MD5 = MD5

    @property
    def Width(self):
        r"""媒资图片文件宽度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""媒资图片文件高度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Format(self):
        r"""媒资图片文件格式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format


    def _deserialize(self, params):
        self._FileSize = params.get("FileSize")
        self._MD5 = params.get("MD5")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageOcr(AbstractModel):
    r"""图片OCR识别结果

    """

    def __init__(self):
        r"""
        :param _Content: 图片中可视文本识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _AppearRect: 可视文本在图片中的位置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AppearRect: :class:`tencentcloud.ivld.v20210903.models.Rectf`
        """
        self._Content = None
        self._AppearRect = None

    @property
    def Content(self):
        r"""图片中可视文本识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def AppearRect(self):
        r"""可视文本在图片中的位置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.Rectf`
        """
        return self._AppearRect

    @AppearRect.setter
    def AppearRect(self, AppearRect):
        self._AppearRect = AppearRect


    def _deserialize(self, params):
        self._Content = params.get("Content")
        if params.get("AppearRect") is not None:
            self._AppearRect = Rectf()
            self._AppearRect._deserialize(params.get("AppearRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportMediaRequest(AbstractModel):
    r"""ImportMedia请求参数结构体

    """

    def __init__(self):
        r"""
        :param _URL: 待分析视频的URL，目前只支持*不带签名的*COS地址，字段输入内容最大为1KB
        :type URL: str
        :param _MD5: 待分析视频的MD5，为空时不做校验，否则会做MD5校验，长度必须为32
        :type MD5: str
        :param _Name: 待分析视频的名称，指定后可支持筛选，视频名称的大小长度不能超过64
        :type Name: str
        :param _WriteBackCosPath: 当非本人外部视频地址导入时，该字段为转存的cos桶地址且不可为空; 示例：https://${Bucket}-${AppId}.cos.${Region}.myqcloud.com/${PathPrefix}/  (注意，cos路径需要以/分隔符结尾)。
推荐采用本主帐号COS桶，如果使用其他帐号COS桶，请确保COS桶可写，否则可导致分析失败
        :type WriteBackCosPath: str
        :param _Label: 自定义标签，可用于查询
        :type Label: str
        :param _CallbackURL: 媒资导入完成的回调地址，该设置优先级高于控制台全局的设置；
        :type CallbackURL: str
        :param _MediaType: 媒资文件类型，详细定义参见[MediaPreknownInfo.MediaType](https://cloud.tencent.com/document/product/1509/65063#MediaPreknownInfo)
默认为2(视频)
        :type MediaType: int
        """
        self._URL = None
        self._MD5 = None
        self._Name = None
        self._WriteBackCosPath = None
        self._Label = None
        self._CallbackURL = None
        self._MediaType = None

    @property
    def URL(self):
        r"""待分析视频的URL，目前只支持*不带签名的*COS地址，字段输入内容最大为1KB
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def MD5(self):
        r"""待分析视频的MD5，为空时不做校验，否则会做MD5校验，长度必须为32
        :rtype: str
        """
        return self._MD5

    @MD5.setter
    def MD5(self, MD5):
        self._MD5 = MD5

    @property
    def Name(self):
        r"""待分析视频的名称，指定后可支持筛选，视频名称的大小长度不能超过64
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def WriteBackCosPath(self):
        r"""当非本人外部视频地址导入时，该字段为转存的cos桶地址且不可为空; 示例：https://${Bucket}-${AppId}.cos.${Region}.myqcloud.com/${PathPrefix}/  (注意，cos路径需要以/分隔符结尾)。
推荐采用本主帐号COS桶，如果使用其他帐号COS桶，请确保COS桶可写，否则可导致分析失败
        :rtype: str
        """
        return self._WriteBackCosPath

    @WriteBackCosPath.setter
    def WriteBackCosPath(self, WriteBackCosPath):
        self._WriteBackCosPath = WriteBackCosPath

    @property
    def Label(self):
        r"""自定义标签，可用于查询
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def CallbackURL(self):
        r"""媒资导入完成的回调地址，该设置优先级高于控制台全局的设置；
        :rtype: str
        """
        return self._CallbackURL

    @CallbackURL.setter
    def CallbackURL(self, CallbackURL):
        self._CallbackURL = CallbackURL

    @property
    def MediaType(self):
        r"""媒资文件类型，详细定义参见[MediaPreknownInfo.MediaType](https://cloud.tencent.com/document/product/1509/65063#MediaPreknownInfo)
默认为2(视频)
        :rtype: int
        """
        return self._MediaType

    @MediaType.setter
    def MediaType(self, MediaType):
        self._MediaType = MediaType


    def _deserialize(self, params):
        self._URL = params.get("URL")
        self._MD5 = params.get("MD5")
        self._Name = params.get("Name")
        self._WriteBackCosPath = params.get("WriteBackCosPath")
        self._Label = params.get("Label")
        self._CallbackURL = params.get("CallbackURL")
        self._MediaType = params.get("MediaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportMediaResponse(AbstractModel):
    r"""ImportMedia返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MediaId: 媒资文件在系统中的ID
        :type MediaId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MediaId = None
        self._RequestId = None

    @property
    def MediaId(self):
        r"""媒资文件在系统中的ID
        :rtype: str
        """
        return self._MediaId

    @MediaId.setter
    def MediaId(self, MediaId):
        self._MediaId = MediaId

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
        self._MediaId = params.get("MediaId")
        self._RequestId = params.get("RequestId")


class L1Tag(AbstractModel):
    r"""一级标签信息

    请注意，一级标签信息可能不包含二级标签(此时L2TagSet为空)。在这种情况下，一级标签可直接包含出现信息。

    """

    def __init__(self):
        r"""
        :param _Name: 一级标签名
        :type Name: str
        :param _L2TagSet: 二级标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :type L2TagSet: list of L2Tag
        :param _AppearIndexPairSet: 一级标签出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AppearIndexPairSet: list of AppearIndexPair
        :param _FirstAppear: 一级标签首次出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstAppear: int
        """
        self._Name = None
        self._L2TagSet = None
        self._AppearIndexPairSet = None
        self._FirstAppear = None

    @property
    def Name(self):
        r"""一级标签名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def L2TagSet(self):
        r"""二级标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of L2Tag
        """
        return self._L2TagSet

    @L2TagSet.setter
    def L2TagSet(self, L2TagSet):
        self._L2TagSet = L2TagSet

    @property
    def AppearIndexPairSet(self):
        r"""一级标签出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AppearIndexPair
        """
        return self._AppearIndexPairSet

    @AppearIndexPairSet.setter
    def AppearIndexPairSet(self, AppearIndexPairSet):
        self._AppearIndexPairSet = AppearIndexPairSet

    @property
    def FirstAppear(self):
        r"""一级标签首次出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FirstAppear

    @FirstAppear.setter
    def FirstAppear(self, FirstAppear):
        self._FirstAppear = FirstAppear


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("L2TagSet") is not None:
            self._L2TagSet = []
            for item in params.get("L2TagSet"):
                obj = L2Tag()
                obj._deserialize(item)
                self._L2TagSet.append(obj)
        if params.get("AppearIndexPairSet") is not None:
            self._AppearIndexPairSet = []
            for item in params.get("AppearIndexPairSet"):
                obj = AppearIndexPair()
                obj._deserialize(item)
                self._AppearIndexPairSet.append(obj)
        self._FirstAppear = params.get("FirstAppear")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L2Tag(AbstractModel):
    r"""二级标签信息

    请注意，二级标签信息可能不包含三级标签(此时L3TagSet为空)。

    """

    def __init__(self):
        r"""
        :param _Name: 二级标签名
        :type Name: str
        :param _L3TagSet: 从属于此二级标签的三级标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :type L3TagSet: list of L3Tag
        :param _AppearIndexPairSet: 二级标签出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AppearIndexPairSet: list of AppearIndexPair
        :param _FirstAppear: 二级标签首次出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstAppear: int
        """
        self._Name = None
        self._L3TagSet = None
        self._AppearIndexPairSet = None
        self._FirstAppear = None

    @property
    def Name(self):
        r"""二级标签名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def L3TagSet(self):
        r"""从属于此二级标签的三级标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of L3Tag
        """
        return self._L3TagSet

    @L3TagSet.setter
    def L3TagSet(self, L3TagSet):
        self._L3TagSet = L3TagSet

    @property
    def AppearIndexPairSet(self):
        r"""二级标签出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AppearIndexPair
        """
        return self._AppearIndexPairSet

    @AppearIndexPairSet.setter
    def AppearIndexPairSet(self, AppearIndexPairSet):
        self._AppearIndexPairSet = AppearIndexPairSet

    @property
    def FirstAppear(self):
        r"""二级标签首次出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FirstAppear

    @FirstAppear.setter
    def FirstAppear(self, FirstAppear):
        self._FirstAppear = FirstAppear


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("L3TagSet") is not None:
            self._L3TagSet = []
            for item in params.get("L3TagSet"):
                obj = L3Tag()
                obj._deserialize(item)
                self._L3TagSet.append(obj)
        if params.get("AppearIndexPairSet") is not None:
            self._AppearIndexPairSet = []
            for item in params.get("AppearIndexPairSet"):
                obj = AppearIndexPair()
                obj._deserialize(item)
                self._AppearIndexPairSet.append(obj)
        self._FirstAppear = params.get("FirstAppear")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L3Tag(AbstractModel):
    r"""三级标签信息。

    三级标签不再包含任何子标签。所有三级标签都对应着识别结果中的出现信息，出现信息使用AppearIndexPairSet定位。

    """

    def __init__(self):
        r"""
        :param _Name: 三级标签名
        :type Name: str
        :param _AppearIndexPairSet: 三级标签出现信息索引数组
注意：此字段可能返回 null，表示取不到有效值。
        :type AppearIndexPairSet: list of AppearIndexPair
        :param _FirstAppear: 三级标签首次出现信息，可选值为[1,3]
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstAppear: int
        """
        self._Name = None
        self._AppearIndexPairSet = None
        self._FirstAppear = None

    @property
    def Name(self):
        r"""三级标签名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AppearIndexPairSet(self):
        r"""三级标签出现信息索引数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AppearIndexPair
        """
        return self._AppearIndexPairSet

    @AppearIndexPairSet.setter
    def AppearIndexPairSet(self, AppearIndexPairSet):
        self._AppearIndexPairSet = AppearIndexPairSet

    @property
    def FirstAppear(self):
        r"""三级标签首次出现信息，可选值为[1,3]
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FirstAppear

    @FirstAppear.setter
    def FirstAppear(self, FirstAppear):
        self._FirstAppear = FirstAppear


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("AppearIndexPairSet") is not None:
            self._AppearIndexPairSet = []
            for item in params.get("AppearIndexPairSet"):
                obj = AppearIndexPair()
                obj._deserialize(item)
                self._AppearIndexPairSet.append(obj)
        self._FirstAppear = params.get("FirstAppear")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaFilter(AbstractModel):
    r"""媒资过滤条件

    """

    def __init__(self):
        r"""
        :param _MediaNameSet: 媒资名称过滤条件
        :type MediaNameSet: list of str
        :param _StatusSet: 媒资状态数组，媒资状态可选值参见MediaInfo
        :type StatusSet: list of int
        :param _MediaIdSet: 媒资ID数组
        :type MediaIdSet: list of str
        :param _LabelSet: 媒资自定义标签数组
        :type LabelSet: list of str
        :param _MediaType: 媒资文件类型，定义参见[MediaPreknownInfo.MediaType](https://cloud.tencent.com/document/product/1509/65063#MediaPreknownInfo)
        :type MediaType: int
        """
        self._MediaNameSet = None
        self._StatusSet = None
        self._MediaIdSet = None
        self._LabelSet = None
        self._MediaType = None

    @property
    def MediaNameSet(self):
        r"""媒资名称过滤条件
        :rtype: list of str
        """
        return self._MediaNameSet

    @MediaNameSet.setter
    def MediaNameSet(self, MediaNameSet):
        self._MediaNameSet = MediaNameSet

    @property
    def StatusSet(self):
        r"""媒资状态数组，媒资状态可选值参见MediaInfo
        :rtype: list of int
        """
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

    @property
    def MediaIdSet(self):
        r"""媒资ID数组
        :rtype: list of str
        """
        return self._MediaIdSet

    @MediaIdSet.setter
    def MediaIdSet(self, MediaIdSet):
        self._MediaIdSet = MediaIdSet

    @property
    def LabelSet(self):
        r"""媒资自定义标签数组
        :rtype: list of str
        """
        return self._LabelSet

    @LabelSet.setter
    def LabelSet(self, LabelSet):
        self._LabelSet = LabelSet

    @property
    def MediaType(self):
        r"""媒资文件类型，定义参见[MediaPreknownInfo.MediaType](https://cloud.tencent.com/document/product/1509/65063#MediaPreknownInfo)
        :rtype: int
        """
        return self._MediaType

    @MediaType.setter
    def MediaType(self, MediaType):
        self._MediaType = MediaType


    def _deserialize(self, params):
        self._MediaNameSet = params.get("MediaNameSet")
        self._StatusSet = params.get("StatusSet")
        self._MediaIdSet = params.get("MediaIdSet")
        self._LabelSet = params.get("LabelSet")
        self._MediaType = params.get("MediaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaInfo(AbstractModel):
    r"""媒资信息结构体

    媒资状态定义如下：

    | 状态名 | 状态值 | 状态描述 |
    |---|---|---|
    | MEDIA_STATUS_INVALID | 0 | 非法状态|
    | MEDIA_STATUS_WAITING| 1 | 等待中 |
    | MEDIA_STATUS_DOWNLOADING | 2 | 下载中 |
    | MEDIA_STATUS_DOWNLOADED | 3 | 下载完成 |
    | MEDIA_STATUS_DOWNLOAD_FAILED | 4 | 下载失败(已废弃) |
    | MEDIA_STATUS_TRANSCODING | 5 | 转码中 |
    | MEDIA_STATUS_TRANSCODED | 6 | 转码完成 |
    | MEDIA_STATUS_TRANCODE_FAILED | 7 | 转码失败(已废弃) |
    | MEDIA_STATUS_SUCCESS | 8 | 媒资文件状态就绪，可发起任务 |
    | MEDIA_STATUS_EXPIRED | 9 | 媒资文件已过期 |
    | MEDIA_STATUS_FAILED | 10 | 媒资导入失败 |

    """

    def __init__(self):
        r"""
        :param _MediaId: 媒资ID
        :type MediaId: str
        :param _Name: 媒资名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _DownLoadURL: 媒资下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DownLoadURL: str
        :param _Status: 媒资状态，取值参看上方表格
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _FailedReason: 若状态为失败，表示失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedReason: str
        :param _Metadata: 媒资视频元信息，仅在MediaType=VIDEO时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Metadata: :class:`tencentcloud.ivld.v20210903.models.MediaMetadata`
        :param _Progress: 导入视频进度，取值范围为[0,100]
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: float
        :param _Label: 媒资自定义标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _CallbackURL: 媒资导入完成后的回调地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackURL: str
        :param _MediaType: 媒资文件类型，具体参看[MediaPreknownInfo](https://cloud.tencent.com/document/product/1509/65063#MediaPreknownInfo)
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaType: int
        :param _AudioMetadata: 媒资音频元信息，仅在MediaType=Audio时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioMetadata: :class:`tencentcloud.ivld.v20210903.models.AudioMetadata`
        :param _ImageMetadata: 媒资图片文件元信息，仅在MediaType=Image时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageMetadata: :class:`tencentcloud.ivld.v20210903.models.ImageMetadata`
        :param _TextMetadata: 媒资文本文件元信息，仅在MediaType=Text时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type TextMetadata: :class:`tencentcloud.ivld.v20210903.models.TextMetadata`
        """
        self._MediaId = None
        self._Name = None
        self._DownLoadURL = None
        self._Status = None
        self._FailedReason = None
        self._Metadata = None
        self._Progress = None
        self._Label = None
        self._CallbackURL = None
        self._MediaType = None
        self._AudioMetadata = None
        self._ImageMetadata = None
        self._TextMetadata = None

    @property
    def MediaId(self):
        r"""媒资ID
        :rtype: str
        """
        return self._MediaId

    @MediaId.setter
    def MediaId(self, MediaId):
        self._MediaId = MediaId

    @property
    def Name(self):
        r"""媒资名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DownLoadURL(self):
        r"""媒资下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DownLoadURL

    @DownLoadURL.setter
    def DownLoadURL(self, DownLoadURL):
        self._DownLoadURL = DownLoadURL

    @property
    def Status(self):
        r"""媒资状态，取值参看上方表格
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailedReason(self):
        r"""若状态为失败，表示失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FailedReason

    @FailedReason.setter
    def FailedReason(self, FailedReason):
        self._FailedReason = FailedReason

    @property
    def Metadata(self):
        r"""媒资视频元信息，仅在MediaType=VIDEO时有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.MediaMetadata`
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def Progress(self):
        r"""导入视频进度，取值范围为[0,100]
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Label(self):
        r"""媒资自定义标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def CallbackURL(self):
        r"""媒资导入完成后的回调地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CallbackURL

    @CallbackURL.setter
    def CallbackURL(self, CallbackURL):
        self._CallbackURL = CallbackURL

    @property
    def MediaType(self):
        r"""媒资文件类型，具体参看[MediaPreknownInfo](https://cloud.tencent.com/document/product/1509/65063#MediaPreknownInfo)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MediaType

    @MediaType.setter
    def MediaType(self, MediaType):
        self._MediaType = MediaType

    @property
    def AudioMetadata(self):
        r"""媒资音频元信息，仅在MediaType=Audio时有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.AudioMetadata`
        """
        return self._AudioMetadata

    @AudioMetadata.setter
    def AudioMetadata(self, AudioMetadata):
        self._AudioMetadata = AudioMetadata

    @property
    def ImageMetadata(self):
        r"""媒资图片文件元信息，仅在MediaType=Image时有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.ImageMetadata`
        """
        return self._ImageMetadata

    @ImageMetadata.setter
    def ImageMetadata(self, ImageMetadata):
        self._ImageMetadata = ImageMetadata

    @property
    def TextMetadata(self):
        r"""媒资文本文件元信息，仅在MediaType=Text时有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.TextMetadata`
        """
        return self._TextMetadata

    @TextMetadata.setter
    def TextMetadata(self, TextMetadata):
        self._TextMetadata = TextMetadata


    def _deserialize(self, params):
        self._MediaId = params.get("MediaId")
        self._Name = params.get("Name")
        self._DownLoadURL = params.get("DownLoadURL")
        self._Status = params.get("Status")
        self._FailedReason = params.get("FailedReason")
        if params.get("Metadata") is not None:
            self._Metadata = MediaMetadata()
            self._Metadata._deserialize(params.get("Metadata"))
        self._Progress = params.get("Progress")
        self._Label = params.get("Label")
        self._CallbackURL = params.get("CallbackURL")
        self._MediaType = params.get("MediaType")
        if params.get("AudioMetadata") is not None:
            self._AudioMetadata = AudioMetadata()
            self._AudioMetadata._deserialize(params.get("AudioMetadata"))
        if params.get("ImageMetadata") is not None:
            self._ImageMetadata = ImageMetadata()
            self._ImageMetadata._deserialize(params.get("ImageMetadata"))
        if params.get("TextMetadata") is not None:
            self._TextMetadata = TextMetadata()
            self._TextMetadata._deserialize(params.get("TextMetadata"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaMetadata(AbstractModel):
    r"""媒资文件视频元信息，包括分辨率，帧率，码率等

    """

    def __init__(self):
        r"""
        :param _FileSize: 媒资视频文件大小，单位为字节
        :type FileSize: int
        :param _MD5: 媒资视频文件MD5
        :type MD5: str
        :param _Duration: 媒资视频时长，单位为秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: float
        :param _NumFrames: 媒资视频总帧数
注意：此字段可能返回 null，表示取不到有效值。
        :type NumFrames: int
        :param _Width: 媒资视频宽度，单位为像素
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param _Height: 媒资视频高度，单位为像素
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param _FPS: 媒资视频帧率，单位为Hz
注意：此字段可能返回 null，表示取不到有效值。
        :type FPS: float
        :param _BitRate: 媒资视频比特率，单位为kbps
注意：此字段可能返回 null，表示取不到有效值。
        :type BitRate: int
        """
        self._FileSize = None
        self._MD5 = None
        self._Duration = None
        self._NumFrames = None
        self._Width = None
        self._Height = None
        self._FPS = None
        self._BitRate = None

    @property
    def FileSize(self):
        r"""媒资视频文件大小，单位为字节
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def MD5(self):
        r"""媒资视频文件MD5
        :rtype: str
        """
        return self._MD5

    @MD5.setter
    def MD5(self, MD5):
        self._MD5 = MD5

    @property
    def Duration(self):
        r"""媒资视频时长，单位为秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def NumFrames(self):
        r"""媒资视频总帧数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NumFrames

    @NumFrames.setter
    def NumFrames(self, NumFrames):
        self._NumFrames = NumFrames

    @property
    def Width(self):
        r"""媒资视频宽度，单位为像素
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""媒资视频高度，单位为像素
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def FPS(self):
        r"""媒资视频帧率，单位为Hz
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._FPS

    @FPS.setter
    def FPS(self, FPS):
        self._FPS = FPS

    @property
    def BitRate(self):
        r"""媒资视频比特率，单位为kbps
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate


    def _deserialize(self, params):
        self._FileSize = params.get("FileSize")
        self._MD5 = params.get("MD5")
        self._Duration = params.get("Duration")
        self._NumFrames = params.get("NumFrames")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._FPS = params.get("FPS")
        self._BitRate = params.get("BitRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaPreknownInfo(AbstractModel):
    r"""描述输入媒资的先验知识，例如文件类型(视频)，媒体类型(新闻/综艺等)

    MediaPreknownInfo.MediaType:

    | MediaType 名称|  MediaType取值 | MediaType描述 |
    |---|---|---|
    | MEDIA_TYPE_INVALID | 0 | 非法的媒资文件类型 |
    | MEDIA_TYPE_IMAGE | 1 | 图片 |
    | MEDIA_TYPE_VIDEO | 2 | 视频 |
    | MEDIA_TYPE_AUDIO | 3 | 音频 |
    | MEDIA_TYPE_VIDEO_STREAM | 4 | 视频流，暂不支持 |
    | MEDIA_TYPE_TEXT | 5 | 文本 |

    MediaPreknownInfo.MediaLabel:

    | MediaLabel名称 | MediaLabel取值 | MediaLabel描述 |
    |---|---|---|
    | MEDIA_LABEL_INVALID | 0 | 非法的一级媒资素材类型 |
    | MEDIA_LABEL_NEWS | 1 | 新闻 |
    | MEDIA_LABEL_ENTERTAINMENT | 2 | 综艺|
    | MEDIA_LABEL_INTERNET_INFO | 3 | 互联网资讯 |
    | MEDIA_LABEL_MOVIE | 4 | 电影 |
    | MEDIA_LABEL_SERIES | 5 | 电视连续剧 |
    | MEDIA_LABEL_SPECIAL | 6 | 专题 |
    | MEDIA_LABEL_SPORT | 7 | 体育 |

    MediaPreknownInfo.MediaSecondLabel
    请注意：**当且仅当MediaLabel=2(综艺)时MediaSecondLabel才有意义**

    | MediaSecondLabel名称 | MediaSecondLabel取值 | MediaSecondLabel 描述|
    |---|---|---|
    | MEDIA_SECOND_LABEL_INVALID |  0  | 非法的MediaSecondLabel |
    | MEDIA_SECOND_LABEL_EVENING | 1 | 综艺晚会 |
    | MEDIA_SECOND_LABEL_OTHERS | 2 | 其他 |

    MediaMeta.MediaLang

    | MediaLang名称 | MediaLang取值 | MediaLang描述 |
    |---|---|---|
    | MEDIA_LANG_INVALID | 0 | 非法的MediaLang |
    | MEDIA_LANG_MANDARIN | 1 | 普通话 |
    | MEDIA_LANG_CANTONESE | 2 | 粤语 |

    """

    def __init__(self):
        r"""
        :param _MediaType: 媒资文件类型，参见MediaPreknownInfo结构体定义
        :type MediaType: int
        :param _MediaLabel: 媒资素材一级类型，参见MediaPreknownInfo结构体定义
        :type MediaLabel: int
        :param _MediaSecondLabel: 媒资素材二级类型，参见MediaPreknownInfo结构体定义
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaSecondLabel: int
        :param _MediaLang: 媒资音频类型，参见MediaPreknownInfo结构体定义
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaLang: int
        """
        self._MediaType = None
        self._MediaLabel = None
        self._MediaSecondLabel = None
        self._MediaLang = None

    @property
    def MediaType(self):
        r"""媒资文件类型，参见MediaPreknownInfo结构体定义
        :rtype: int
        """
        return self._MediaType

    @MediaType.setter
    def MediaType(self, MediaType):
        self._MediaType = MediaType

    @property
    def MediaLabel(self):
        r"""媒资素材一级类型，参见MediaPreknownInfo结构体定义
        :rtype: int
        """
        return self._MediaLabel

    @MediaLabel.setter
    def MediaLabel(self, MediaLabel):
        self._MediaLabel = MediaLabel

    @property
    def MediaSecondLabel(self):
        r"""媒资素材二级类型，参见MediaPreknownInfo结构体定义
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MediaSecondLabel

    @MediaSecondLabel.setter
    def MediaSecondLabel(self, MediaSecondLabel):
        self._MediaSecondLabel = MediaSecondLabel

    @property
    def MediaLang(self):
        r"""媒资音频类型，参见MediaPreknownInfo结构体定义
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MediaLang

    @MediaLang.setter
    def MediaLang(self, MediaLang):
        self._MediaLang = MediaLang


    def _deserialize(self, params):
        self._MediaType = params.get("MediaType")
        self._MediaLabel = params.get("MediaLabel")
        self._MediaSecondLabel = params.get("MediaSecondLabel")
        self._MediaLang = params.get("MediaLang")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCallbackRequest(AbstractModel):
    r"""ModifyCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskFinishNotifyURL: 任务分析完成后回调地址
        :type TaskFinishNotifyURL: str
        :param _MediaFinishNotifyURL: 媒体导入完成后回调地址
        :type MediaFinishNotifyURL: str
        """
        self._TaskFinishNotifyURL = None
        self._MediaFinishNotifyURL = None

    @property
    def TaskFinishNotifyURL(self):
        r"""任务分析完成后回调地址
        :rtype: str
        """
        return self._TaskFinishNotifyURL

    @TaskFinishNotifyURL.setter
    def TaskFinishNotifyURL(self, TaskFinishNotifyURL):
        self._TaskFinishNotifyURL = TaskFinishNotifyURL

    @property
    def MediaFinishNotifyURL(self):
        r"""媒体导入完成后回调地址
        :rtype: str
        """
        return self._MediaFinishNotifyURL

    @MediaFinishNotifyURL.setter
    def MediaFinishNotifyURL(self, MediaFinishNotifyURL):
        self._MediaFinishNotifyURL = MediaFinishNotifyURL


    def _deserialize(self, params):
        self._TaskFinishNotifyURL = params.get("TaskFinishNotifyURL")
        self._MediaFinishNotifyURL = params.get("MediaFinishNotifyURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCallbackResponse(AbstractModel):
    r"""ModifyCallback返回参数结构体

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


class MultiLevelPersonInfo(AbstractModel):
    r"""带类型树的已分类人物信息

    """

    def __init__(self):
        r"""
        :param _L1ClassifyName: 一级分类名称(分类信息参见自定义人物类型)
注意：此字段可能返回 null，表示取不到有效值。
        :type L1ClassifyName: str
        :param _L2ClassifiedPersonInfoSet: 已分类人物信息数组(所有分类类型为二级分类)
注意：此字段可能返回 null，表示取不到有效值。
        :type L2ClassifiedPersonInfoSet: list of ClassifiedPersonInfo
        :param _Source: 检测结果来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: int
        """
        self._L1ClassifyName = None
        self._L2ClassifiedPersonInfoSet = None
        self._Source = None

    @property
    def L1ClassifyName(self):
        r"""一级分类名称(分类信息参见自定义人物类型)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._L1ClassifyName

    @L1ClassifyName.setter
    def L1ClassifyName(self, L1ClassifyName):
        self._L1ClassifyName = L1ClassifyName

    @property
    def L2ClassifiedPersonInfoSet(self):
        r"""已分类人物信息数组(所有分类类型为二级分类)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ClassifiedPersonInfo
        """
        return self._L2ClassifiedPersonInfoSet

    @L2ClassifiedPersonInfoSet.setter
    def L2ClassifiedPersonInfoSet(self, L2ClassifiedPersonInfoSet):
        self._L2ClassifiedPersonInfoSet = L2ClassifiedPersonInfoSet

    @property
    def Source(self):
        r"""检测结果来源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source


    def _deserialize(self, params):
        self._L1ClassifyName = params.get("L1ClassifyName")
        if params.get("L2ClassifiedPersonInfoSet") is not None:
            self._L2ClassifiedPersonInfoSet = []
            for item in params.get("L2ClassifiedPersonInfoSet"):
                obj = ClassifiedPersonInfo()
                obj._deserialize(item)
                self._L2ClassifiedPersonInfoSet.append(obj)
        self._Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiLevelTag(AbstractModel):
    r"""标签信息结构体

    包含多级(最多三级)标签结果，以及这些标签在识别结果中的出现位置

    """

    def __init__(self):
        r"""
        :param _TagSet: 树状标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSet: list of L1Tag
        :param _AppearInfo: 标签在识别结果中的定位信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AppearInfo: :class:`tencentcloud.ivld.v20210903.models.AppearInfo`
        """
        self._TagSet = None
        self._AppearInfo = None

    @property
    def TagSet(self):
        r"""树状标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of L1Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def AppearInfo(self):
        r"""标签在识别结果中的定位信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.AppearInfo`
        """
        return self._AppearInfo

    @AppearInfo.setter
    def AppearInfo(self, AppearInfo):
        self._AppearInfo = AppearInfo


    def _deserialize(self, params):
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = L1Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        if params.get("AppearInfo") is not None:
            self._AppearInfo = AppearInfo()
            self._AppearInfo._deserialize(params.get("AppearInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonImageInfo(AbstractModel):
    r"""自定义人物人脸图片信息

    """

    def __init__(self):
        r"""
        :param _ImageId: 人脸图片ID
        :type ImageId: str
        :param _ImageURL: 自定义人脸图片的URL，存储在IVLDCustomPreson存储桶内
        :type ImageURL: str
        :param _ErrorCode: 自定义人脸图片处理错误码
        :type ErrorCode: str
        :param _ErrorMsg: 自定义人脸图片处理错误信息
        :type ErrorMsg: str
        """
        self._ImageId = None
        self._ImageURL = None
        self._ErrorCode = None
        self._ErrorMsg = None

    @property
    def ImageId(self):
        r"""人脸图片ID
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageURL(self):
        r"""自定义人脸图片的URL，存储在IVLDCustomPreson存储桶内
        :rtype: str
        """
        return self._ImageURL

    @ImageURL.setter
    def ImageURL(self, ImageURL):
        self._ImageURL = ImageURL

    @property
    def ErrorCode(self):
        r"""自定义人脸图片处理错误码
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMsg(self):
        r"""自定义人脸图片处理错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._ImageURL = params.get("ImageURL")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonInfo(AbstractModel):
    r"""人物信息

    """

    def __init__(self):
        r"""
        :param _Name: 公众人物姓名
        :type Name: str
        :param _Job: 公众人物职务
        :type Job: str
        :param _FirstAppear: 首次出现模态，可选值为[1,3]，详细参见AppearIndex定义
        :type FirstAppear: int
        :param _AppearInfo: 人物出现信息
        :type AppearInfo: :class:`tencentcloud.ivld.v20210903.models.AppearInfo`
        :param _AppearRect: 人脸在图片中的位置，仅在图片标签任务有效
注意：此字段可能返回 null，表示取不到有效值。
        :type AppearRect: :class:`tencentcloud.ivld.v20210903.models.Rectf`
        :param _PersonId: 人物的personId
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonId: str
        """
        self._Name = None
        self._Job = None
        self._FirstAppear = None
        self._AppearInfo = None
        self._AppearRect = None
        self._PersonId = None

    @property
    def Name(self):
        r"""公众人物姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Job(self):
        r"""公众人物职务
        :rtype: str
        """
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def FirstAppear(self):
        r"""首次出现模态，可选值为[1,3]，详细参见AppearIndex定义
        :rtype: int
        """
        return self._FirstAppear

    @FirstAppear.setter
    def FirstAppear(self, FirstAppear):
        self._FirstAppear = FirstAppear

    @property
    def AppearInfo(self):
        r"""人物出现信息
        :rtype: :class:`tencentcloud.ivld.v20210903.models.AppearInfo`
        """
        return self._AppearInfo

    @AppearInfo.setter
    def AppearInfo(self, AppearInfo):
        self._AppearInfo = AppearInfo

    @property
    def AppearRect(self):
        r"""人脸在图片中的位置，仅在图片标签任务有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.Rectf`
        """
        return self._AppearRect

    @AppearRect.setter
    def AppearRect(self, AppearRect):
        self._AppearRect = AppearRect

    @property
    def PersonId(self):
        r"""人物的personId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Job = params.get("Job")
        self._FirstAppear = params.get("FirstAppear")
        if params.get("AppearInfo") is not None:
            self._AppearInfo = AppearInfo()
            self._AppearInfo._deserialize(params.get("AppearInfo"))
        if params.get("AppearRect") is not None:
            self._AppearRect = Rectf()
            self._AppearRect._deserialize(params.get("AppearRect"))
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCallbackRequest(AbstractModel):
    r"""QueryCallback请求参数结构体

    """


class QueryCallbackResponse(AbstractModel):
    r"""QueryCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskFinishNotifyURL: 任务分析完成后回调地址
        :type TaskFinishNotifyURL: str
        :param _MediaFinishNotifyURL: 媒体导入完成后回调地址
        :type MediaFinishNotifyURL: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskFinishNotifyURL = None
        self._MediaFinishNotifyURL = None
        self._RequestId = None

    @property
    def TaskFinishNotifyURL(self):
        r"""任务分析完成后回调地址
        :rtype: str
        """
        return self._TaskFinishNotifyURL

    @TaskFinishNotifyURL.setter
    def TaskFinishNotifyURL(self, TaskFinishNotifyURL):
        self._TaskFinishNotifyURL = TaskFinishNotifyURL

    @property
    def MediaFinishNotifyURL(self):
        r"""媒体导入完成后回调地址
        :rtype: str
        """
        return self._MediaFinishNotifyURL

    @MediaFinishNotifyURL.setter
    def MediaFinishNotifyURL(self, MediaFinishNotifyURL):
        self._MediaFinishNotifyURL = MediaFinishNotifyURL

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
        self._TaskFinishNotifyURL = params.get("TaskFinishNotifyURL")
        self._MediaFinishNotifyURL = params.get("MediaFinishNotifyURL")
        self._RequestId = params.get("RequestId")


class Rectf(AbstractModel):
    r"""矩形内容框

    """

    def __init__(self):
        r"""
        :param _X: 矩形框左上角水平座标
注意：此字段可能返回 null，表示取不到有效值。
        :type X: float
        :param _Y: 矩形框左上角竖直座标
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: float
        :param _Width: 矩形框宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: float
        :param _Height: 矩形框长度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: float
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        r"""矩形框左上角水平座标
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""矩形框左上角竖直座标
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        r"""矩形框宽度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""矩形框长度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
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
        


class ShotInfo(AbstractModel):
    r"""输入的镜头信息的描述

    """

    def __init__(self):
        r"""
        :param _StartTimeStamp: 镜头开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimeStamp: float
        :param _EndTimeStamp: 镜头结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTimeStamp: float
        """
        self._StartTimeStamp = None
        self._EndTimeStamp = None

    @property
    def StartTimeStamp(self):
        r"""镜头开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._StartTimeStamp

    @StartTimeStamp.setter
    def StartTimeStamp(self, StartTimeStamp):
        self._StartTimeStamp = StartTimeStamp

    @property
    def EndTimeStamp(self):
        r"""镜头结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._EndTimeStamp

    @EndTimeStamp.setter
    def EndTimeStamp(self, EndTimeStamp):
        self._EndTimeStamp = EndTimeStamp


    def _deserialize(self, params):
        self._StartTimeStamp = params.get("StartTimeStamp")
        self._EndTimeStamp = params.get("EndTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShowInfo(AbstractModel):
    r"""视频结构化结果

    """

    def __init__(self):
        r"""
        :param _Date: 节目日期(只在新闻有效)
注意：此字段可能返回 null，表示取不到有效值。
        :type Date: str
        :param _Logo: 台标
注意：此字段可能返回 null，表示取不到有效值。
        :type Logo: str
        :param _Column: 节目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Column: str
        :param _Source: 来源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _CoverImageURL: 节目封面
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverImageURL: str
        :param _SummarySet: 节目内容概要列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SummarySet: list of str
        :param _TitleSet: 节目片段标题列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TitleSet: list of str
        :param _AudioInfoSet: 音频识别结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioInfoSet: list of AudioInfo
        :param _TextInfoSet: 可视文字识别结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TextInfoSet: list of TextInfo
        :param _ClassifiedPersonInfoSet: 已分类人物信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassifiedPersonInfoSet: list of ClassifiedPersonInfo
        :param _TextTagSet: 文本标签列表，包含标签内容和出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TextTagSet: :class:`tencentcloud.ivld.v20210903.models.MultiLevelTag`
        :param _FrameTagSet: 帧标签列表，包括人物信息，场景信息等
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameTagSet: :class:`tencentcloud.ivld.v20210903.models.MultiLevelTag`
        :param _WebMediaURL: 视频下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type WebMediaURL: str
        :param _MediaClassifierSet: 媒资分类信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaClassifierSet: list of str
        :param _SummaryTagSet: 概要标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryTagSet: list of str
        :param _UnknownPersonSet: 未知人物信息
注意：此字段可能返回 null，表示取不到有效值。
        :type UnknownPersonSet: list of UnknownPerson
        :param _MultiLevelPersonInfoSet: 树状已分类人物信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiLevelPersonInfoSet: list of MultiLevelPersonInfo
        """
        self._Date = None
        self._Logo = None
        self._Column = None
        self._Source = None
        self._CoverImageURL = None
        self._SummarySet = None
        self._TitleSet = None
        self._AudioInfoSet = None
        self._TextInfoSet = None
        self._ClassifiedPersonInfoSet = None
        self._TextTagSet = None
        self._FrameTagSet = None
        self._WebMediaURL = None
        self._MediaClassifierSet = None
        self._SummaryTagSet = None
        self._UnknownPersonSet = None
        self._MultiLevelPersonInfoSet = None

    @property
    def Date(self):
        r"""节目日期(只在新闻有效)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Logo(self):
        r"""台标
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def Column(self):
        r"""节目名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Column

    @Column.setter
    def Column(self, Column):
        self._Column = Column

    @property
    def Source(self):
        r"""来源信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def CoverImageURL(self):
        r"""节目封面
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CoverImageURL

    @CoverImageURL.setter
    def CoverImageURL(self, CoverImageURL):
        self._CoverImageURL = CoverImageURL

    @property
    def SummarySet(self):
        r"""节目内容概要列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SummarySet

    @SummarySet.setter
    def SummarySet(self, SummarySet):
        self._SummarySet = SummarySet

    @property
    def TitleSet(self):
        r"""节目片段标题列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._TitleSet

    @TitleSet.setter
    def TitleSet(self, TitleSet):
        self._TitleSet = TitleSet

    @property
    def AudioInfoSet(self):
        r"""音频识别结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AudioInfo
        """
        return self._AudioInfoSet

    @AudioInfoSet.setter
    def AudioInfoSet(self, AudioInfoSet):
        self._AudioInfoSet = AudioInfoSet

    @property
    def TextInfoSet(self):
        r"""可视文字识别结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TextInfo
        """
        return self._TextInfoSet

    @TextInfoSet.setter
    def TextInfoSet(self, TextInfoSet):
        self._TextInfoSet = TextInfoSet

    @property
    def ClassifiedPersonInfoSet(self):
        r"""已分类人物信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ClassifiedPersonInfo
        """
        return self._ClassifiedPersonInfoSet

    @ClassifiedPersonInfoSet.setter
    def ClassifiedPersonInfoSet(self, ClassifiedPersonInfoSet):
        self._ClassifiedPersonInfoSet = ClassifiedPersonInfoSet

    @property
    def TextTagSet(self):
        r"""文本标签列表，包含标签内容和出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.MultiLevelTag`
        """
        return self._TextTagSet

    @TextTagSet.setter
    def TextTagSet(self, TextTagSet):
        self._TextTagSet = TextTagSet

    @property
    def FrameTagSet(self):
        r"""帧标签列表，包括人物信息，场景信息等
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.MultiLevelTag`
        """
        return self._FrameTagSet

    @FrameTagSet.setter
    def FrameTagSet(self, FrameTagSet):
        self._FrameTagSet = FrameTagSet

    @property
    def WebMediaURL(self):
        r"""视频下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WebMediaURL

    @WebMediaURL.setter
    def WebMediaURL(self, WebMediaURL):
        self._WebMediaURL = WebMediaURL

    @property
    def MediaClassifierSet(self):
        r"""媒资分类信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._MediaClassifierSet

    @MediaClassifierSet.setter
    def MediaClassifierSet(self, MediaClassifierSet):
        self._MediaClassifierSet = MediaClassifierSet

    @property
    def SummaryTagSet(self):
        r"""概要标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SummaryTagSet

    @SummaryTagSet.setter
    def SummaryTagSet(self, SummaryTagSet):
        self._SummaryTagSet = SummaryTagSet

    @property
    def UnknownPersonSet(self):
        r"""未知人物信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of UnknownPerson
        """
        return self._UnknownPersonSet

    @UnknownPersonSet.setter
    def UnknownPersonSet(self, UnknownPersonSet):
        self._UnknownPersonSet = UnknownPersonSet

    @property
    def MultiLevelPersonInfoSet(self):
        r"""树状已分类人物信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MultiLevelPersonInfo
        """
        return self._MultiLevelPersonInfoSet

    @MultiLevelPersonInfoSet.setter
    def MultiLevelPersonInfoSet(self, MultiLevelPersonInfoSet):
        self._MultiLevelPersonInfoSet = MultiLevelPersonInfoSet


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._Logo = params.get("Logo")
        self._Column = params.get("Column")
        self._Source = params.get("Source")
        self._CoverImageURL = params.get("CoverImageURL")
        self._SummarySet = params.get("SummarySet")
        self._TitleSet = params.get("TitleSet")
        if params.get("AudioInfoSet") is not None:
            self._AudioInfoSet = []
            for item in params.get("AudioInfoSet"):
                obj = AudioInfo()
                obj._deserialize(item)
                self._AudioInfoSet.append(obj)
        if params.get("TextInfoSet") is not None:
            self._TextInfoSet = []
            for item in params.get("TextInfoSet"):
                obj = TextInfo()
                obj._deserialize(item)
                self._TextInfoSet.append(obj)
        if params.get("ClassifiedPersonInfoSet") is not None:
            self._ClassifiedPersonInfoSet = []
            for item in params.get("ClassifiedPersonInfoSet"):
                obj = ClassifiedPersonInfo()
                obj._deserialize(item)
                self._ClassifiedPersonInfoSet.append(obj)
        if params.get("TextTagSet") is not None:
            self._TextTagSet = MultiLevelTag()
            self._TextTagSet._deserialize(params.get("TextTagSet"))
        if params.get("FrameTagSet") is not None:
            self._FrameTagSet = MultiLevelTag()
            self._FrameTagSet._deserialize(params.get("FrameTagSet"))
        self._WebMediaURL = params.get("WebMediaURL")
        self._MediaClassifierSet = params.get("MediaClassifierSet")
        self._SummaryTagSet = params.get("SummaryTagSet")
        if params.get("UnknownPersonSet") is not None:
            self._UnknownPersonSet = []
            for item in params.get("UnknownPersonSet"):
                obj = UnknownPerson()
                obj._deserialize(item)
                self._UnknownPersonSet.append(obj)
        if params.get("MultiLevelPersonInfoSet") is not None:
            self._MultiLevelPersonInfoSet = []
            for item in params.get("MultiLevelPersonInfoSet"):
                obj = MultiLevelPersonInfo()
                obj._deserialize(item)
                self._MultiLevelPersonInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SortBy(AbstractModel):
    r"""排序条件

    """

    def __init__(self):
        r"""
        :param _By: 排序字段，默认为CreateTime
        :type By: str
        :param _Descend: true表示降序，false表示升序
        :type Descend: bool
        """
        self._By = None
        self._Descend = None

    @property
    def By(self):
        r"""排序字段，默认为CreateTime
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def Descend(self):
        r"""true表示降序，false表示升序
        :rtype: bool
        """
        return self._Descend

    @Descend.setter
    def Descend(self, Descend):
        self._Descend = Descend


    def _deserialize(self, params):
        self._By = params.get("By")
        self._Descend = params.get("Descend")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TTSMode(AbstractModel):
    r"""TTS 的参数模式

    """

    def __init__(self):
        r"""
        :param _Speed: 语速，范围：[-2，2]，分别对应不同语速：
-2代表0.6倍
-1代表0.8倍
0代表1.0倍（默认）
1代表1.2倍
2代表1.5倍
如果需要更细化的语速，可以保留小数点后 2 位，例如0.5/1.25/2.81等。
        :type Speed: float
        :param _VoiceType: 音色 ID，[音色体验地址](https://cloud.tencent.com/product/tts)。


|音乐ID|音色名称|推荐场景|
|--|--|--|
|1001|智瑜|情感女声|
|1002|智聆|通用女声|
|1003|智美|客服女声|
|1004|智云|通用男声|
|1005|智莉|通用女声|
|1007|智娜|客服女声|
|1008|智琪|客服女声|
|1009|智芸|知性女声|
|1010|智华|通用男声|
|1017|智蓉|情感女声|
|1018|智靖|情感男声|



        :type VoiceType: int
        """
        self._Speed = None
        self._VoiceType = None

    @property
    def Speed(self):
        r"""语速，范围：[-2，2]，分别对应不同语速：
-2代表0.6倍
-1代表0.8倍
0代表1.0倍（默认）
1代表1.2倍
2代表1.5倍
如果需要更细化的语速，可以保留小数点后 2 位，例如0.5/1.25/2.81等。
        :rtype: float
        """
        return self._Speed

    @Speed.setter
    def Speed(self, Speed):
        self._Speed = Speed

    @property
    def VoiceType(self):
        r"""音色 ID，[音色体验地址](https://cloud.tencent.com/product/tts)。


|音乐ID|音色名称|推荐场景|
|--|--|--|
|1001|智瑜|情感女声|
|1002|智聆|通用女声|
|1003|智美|客服女声|
|1004|智云|通用男声|
|1005|智莉|通用女声|
|1007|智娜|客服女声|
|1008|智琪|客服女声|
|1009|智芸|知性女声|
|1010|智华|通用男声|
|1017|智蓉|情感女声|
|1018|智靖|情感男声|



        :rtype: int
        """
        return self._VoiceType

    @VoiceType.setter
    def VoiceType(self, VoiceType):
        self._VoiceType = VoiceType


    def _deserialize(self, params):
        self._Speed = params.get("Speed")
        self._VoiceType = params.get("VoiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskFilter(AbstractModel):
    r"""任务筛选条件结构体

    """

    def __init__(self):
        r"""
        :param _MediaTypeSet: 媒资文件类型
        :type MediaTypeSet: list of int
        :param _TaskStatusSet: 待筛选的任务状态列表
        :type TaskStatusSet: list of int
        :param _TaskNameSet: 待筛选的任务名称数组
        :type TaskNameSet: list of str
        :param _TaskIdSet: TaskId数组
        :type TaskIdSet: list of str
        :param _MediaNameSet: 媒资文件名数组
        :type MediaNameSet: list of str
        :param _MediaLangSet: 媒资语言类型
        :type MediaLangSet: list of int
        :param _MediaLabelSet: 媒资素材一级类型
        :type MediaLabelSet: list of int
        :param _LabelSet: 媒资自定义标签数组
        :type LabelSet: list of str
        """
        self._MediaTypeSet = None
        self._TaskStatusSet = None
        self._TaskNameSet = None
        self._TaskIdSet = None
        self._MediaNameSet = None
        self._MediaLangSet = None
        self._MediaLabelSet = None
        self._LabelSet = None

    @property
    def MediaTypeSet(self):
        r"""媒资文件类型
        :rtype: list of int
        """
        return self._MediaTypeSet

    @MediaTypeSet.setter
    def MediaTypeSet(self, MediaTypeSet):
        self._MediaTypeSet = MediaTypeSet

    @property
    def TaskStatusSet(self):
        r"""待筛选的任务状态列表
        :rtype: list of int
        """
        return self._TaskStatusSet

    @TaskStatusSet.setter
    def TaskStatusSet(self, TaskStatusSet):
        self._TaskStatusSet = TaskStatusSet

    @property
    def TaskNameSet(self):
        r"""待筛选的任务名称数组
        :rtype: list of str
        """
        return self._TaskNameSet

    @TaskNameSet.setter
    def TaskNameSet(self, TaskNameSet):
        self._TaskNameSet = TaskNameSet

    @property
    def TaskIdSet(self):
        r"""TaskId数组
        :rtype: list of str
        """
        return self._TaskIdSet

    @TaskIdSet.setter
    def TaskIdSet(self, TaskIdSet):
        self._TaskIdSet = TaskIdSet

    @property
    def MediaNameSet(self):
        r"""媒资文件名数组
        :rtype: list of str
        """
        return self._MediaNameSet

    @MediaNameSet.setter
    def MediaNameSet(self, MediaNameSet):
        self._MediaNameSet = MediaNameSet

    @property
    def MediaLangSet(self):
        r"""媒资语言类型
        :rtype: list of int
        """
        return self._MediaLangSet

    @MediaLangSet.setter
    def MediaLangSet(self, MediaLangSet):
        self._MediaLangSet = MediaLangSet

    @property
    def MediaLabelSet(self):
        r"""媒资素材一级类型
        :rtype: list of int
        """
        return self._MediaLabelSet

    @MediaLabelSet.setter
    def MediaLabelSet(self, MediaLabelSet):
        self._MediaLabelSet = MediaLabelSet

    @property
    def LabelSet(self):
        r"""媒资自定义标签数组
        :rtype: list of str
        """
        return self._LabelSet

    @LabelSet.setter
    def LabelSet(self, LabelSet):
        self._LabelSet = LabelSet


    def _deserialize(self, params):
        self._MediaTypeSet = params.get("MediaTypeSet")
        self._TaskStatusSet = params.get("TaskStatusSet")
        self._TaskNameSet = params.get("TaskNameSet")
        self._TaskIdSet = params.get("TaskIdSet")
        self._MediaNameSet = params.get("MediaNameSet")
        self._MediaLangSet = params.get("MediaLangSet")
        self._MediaLabelSet = params.get("MediaLabelSet")
        self._LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInfo(AbstractModel):
    r"""任务信息

    TaskStatus定义如下:

    | TaskStatus名称 | TaskStatus取值 | TaskStatus描述 |
    |---|---|---|
    | TASK_STATUS_INVALID | 0 | 非法的任务状态 |
    | TASK_STATUS_WAITING | 1 | 排队中 |
    | TASK_STATUS_ANALYSING | 2 | 任务分析中 |
    | TASK_STATUS_ANALYSED | 3 | 任务分析完成 |
    | TASK_STATUS_SNAPSHOT_CREATING | 4 | 任务结果快照生成中 |
    | TASK_STATUS_SNAPSHOT_CREATED | 5 | 任务结果快照生成完成 |
    | TASK_STATUS_RESULT_UPLOADING | 6 | 任务结果快照上传中 |
    | TASK_STATUS_RESULT_UPLOADED | 7 | 任务结果快照上传完成 |
    | TASK_STATUS_SUCCESS | 8 | 任务执行完成 |
    | TASK_STATUS_FAILED | 9 | 任务执行失败 |

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _TaskName: 描述任务名称，指定后可根据名称筛选
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _MediaId: 媒资文件ID
        :type MediaId: str
        :param _TaskStatus: 任务执行状态
        :type TaskStatus: int
        :param _TaskProgress: 任务进度，范围为[0，100]
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskProgress: float
        :param _TaskTimeCost: 任务执行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTimeCost: int
        :param _TaskCreateTime: 任务创建时间
        :type TaskCreateTime: str
        :param _TaskStartTime: 任务开始执行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskStartTime: str
        :param _FailedReason: 任务失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedReason: str
        :param _MediaPreknownInfo: 任务执行时指定的先验知识
        :type MediaPreknownInfo: :class:`tencentcloud.ivld.v20210903.models.MediaPreknownInfo`
        :param _MediaName: 媒资文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaName: str
        :param _Label: 媒资自定义标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _CallbackURL: 任务分析完成后的后调地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackURL: str
        :param _AudioMetadata: 任务对应的媒资文件元信息，仅在MediaType为Audio时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioMetadata: :class:`tencentcloud.ivld.v20210903.models.AudioMetadata`
        :param _ImageMetadata: 任务对应的媒资文件元信息，仅在MediaType为Audio时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageMetadata: :class:`tencentcloud.ivld.v20210903.models.ImageMetadata`
        :param _TextMetadata: 任务对应的媒资文件元信息，仅在MediaType为Text时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type TextMetadata: :class:`tencentcloud.ivld.v20210903.models.TextMetadata`
        :param _Metadata: 任务对应的媒资文件元信息，仅在MediaType为Video时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Metadata: :class:`tencentcloud.ivld.v20210903.models.MediaMetadata`
        """
        self._TaskId = None
        self._TaskName = None
        self._MediaId = None
        self._TaskStatus = None
        self._TaskProgress = None
        self._TaskTimeCost = None
        self._TaskCreateTime = None
        self._TaskStartTime = None
        self._FailedReason = None
        self._MediaPreknownInfo = None
        self._MediaName = None
        self._Label = None
        self._CallbackURL = None
        self._AudioMetadata = None
        self._ImageMetadata = None
        self._TextMetadata = None
        self._Metadata = None

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
    def TaskName(self):
        r"""描述任务名称，指定后可根据名称筛选
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def MediaId(self):
        r"""媒资文件ID
        :rtype: str
        """
        return self._MediaId

    @MediaId.setter
    def MediaId(self, MediaId):
        self._MediaId = MediaId

    @property
    def TaskStatus(self):
        r"""任务执行状态
        :rtype: int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskProgress(self):
        r"""任务进度，范围为[0，100]
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._TaskProgress

    @TaskProgress.setter
    def TaskProgress(self, TaskProgress):
        self._TaskProgress = TaskProgress

    @property
    def TaskTimeCost(self):
        r"""任务执行时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TaskTimeCost

    @TaskTimeCost.setter
    def TaskTimeCost(self, TaskTimeCost):
        self._TaskTimeCost = TaskTimeCost

    @property
    def TaskCreateTime(self):
        r"""任务创建时间
        :rtype: str
        """
        return self._TaskCreateTime

    @TaskCreateTime.setter
    def TaskCreateTime(self, TaskCreateTime):
        self._TaskCreateTime = TaskCreateTime

    @property
    def TaskStartTime(self):
        r"""任务开始执行时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskStartTime

    @TaskStartTime.setter
    def TaskStartTime(self, TaskStartTime):
        self._TaskStartTime = TaskStartTime

    @property
    def FailedReason(self):
        r"""任务失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FailedReason

    @FailedReason.setter
    def FailedReason(self, FailedReason):
        self._FailedReason = FailedReason

    @property
    def MediaPreknownInfo(self):
        r"""任务执行时指定的先验知识
        :rtype: :class:`tencentcloud.ivld.v20210903.models.MediaPreknownInfo`
        """
        return self._MediaPreknownInfo

    @MediaPreknownInfo.setter
    def MediaPreknownInfo(self, MediaPreknownInfo):
        self._MediaPreknownInfo = MediaPreknownInfo

    @property
    def MediaName(self):
        r"""媒资文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MediaName

    @MediaName.setter
    def MediaName(self, MediaName):
        self._MediaName = MediaName

    @property
    def Label(self):
        r"""媒资自定义标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def CallbackURL(self):
        r"""任务分析完成后的后调地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CallbackURL

    @CallbackURL.setter
    def CallbackURL(self, CallbackURL):
        self._CallbackURL = CallbackURL

    @property
    def AudioMetadata(self):
        r"""任务对应的媒资文件元信息，仅在MediaType为Audio时有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.AudioMetadata`
        """
        return self._AudioMetadata

    @AudioMetadata.setter
    def AudioMetadata(self, AudioMetadata):
        self._AudioMetadata = AudioMetadata

    @property
    def ImageMetadata(self):
        r"""任务对应的媒资文件元信息，仅在MediaType为Audio时有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.ImageMetadata`
        """
        return self._ImageMetadata

    @ImageMetadata.setter
    def ImageMetadata(self, ImageMetadata):
        self._ImageMetadata = ImageMetadata

    @property
    def TextMetadata(self):
        r"""任务对应的媒资文件元信息，仅在MediaType为Text时有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.TextMetadata`
        """
        return self._TextMetadata

    @TextMetadata.setter
    def TextMetadata(self, TextMetadata):
        self._TextMetadata = TextMetadata

    @property
    def Metadata(self):
        r"""任务对应的媒资文件元信息，仅在MediaType为Video时有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.MediaMetadata`
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._MediaId = params.get("MediaId")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskProgress = params.get("TaskProgress")
        self._TaskTimeCost = params.get("TaskTimeCost")
        self._TaskCreateTime = params.get("TaskCreateTime")
        self._TaskStartTime = params.get("TaskStartTime")
        self._FailedReason = params.get("FailedReason")
        if params.get("MediaPreknownInfo") is not None:
            self._MediaPreknownInfo = MediaPreknownInfo()
            self._MediaPreknownInfo._deserialize(params.get("MediaPreknownInfo"))
        self._MediaName = params.get("MediaName")
        self._Label = params.get("Label")
        self._CallbackURL = params.get("CallbackURL")
        if params.get("AudioMetadata") is not None:
            self._AudioMetadata = AudioMetadata()
            self._AudioMetadata._deserialize(params.get("AudioMetadata"))
        if params.get("ImageMetadata") is not None:
            self._ImageMetadata = ImageMetadata()
            self._ImageMetadata._deserialize(params.get("ImageMetadata"))
        if params.get("TextMetadata") is not None:
            self._TextMetadata = TextMetadata()
            self._TextMetadata._deserialize(params.get("TextMetadata"))
        if params.get("Metadata") is not None:
            self._Metadata = MediaMetadata()
            self._Metadata._deserialize(params.get("Metadata"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextAppearInfo(AbstractModel):
    r"""关键词在文本中的定位信息

    Position为关键词在文本中的偏移量，从0开始。例如，给定文本结果"欢迎收看新闻三十分”，以及关键词"新闻三十分"，那么StartPosition的值为4，EndPosition的值为9

    """

    def __init__(self):
        r"""
        :param _Index: 文本结果数组中的下标
        :type Index: int
        :param _StartPosition: 关键词在文本中出现的起始偏移量(包含)
        :type StartPosition: int
        :param _EndPosition: 关键词在文本中出现的结束偏移量(不包含)
        :type EndPosition: int
        """
        self._Index = None
        self._StartPosition = None
        self._EndPosition = None

    @property
    def Index(self):
        r"""文本结果数组中的下标
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def StartPosition(self):
        r"""关键词在文本中出现的起始偏移量(包含)
        :rtype: int
        """
        return self._StartPosition

    @StartPosition.setter
    def StartPosition(self, StartPosition):
        self._StartPosition = StartPosition

    @property
    def EndPosition(self):
        r"""关键词在文本中出现的结束偏移量(不包含)
        :rtype: int
        """
        return self._EndPosition

    @EndPosition.setter
    def EndPosition(self, EndPosition):
        self._EndPosition = EndPosition


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._StartPosition = params.get("StartPosition")
        self._EndPosition = params.get("EndPosition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextData(AbstractModel):
    r"""文本文件标签识别结果

    """

    def __init__(self):
        r"""
        :param _Content: 文本内容信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _Summary: 文本概要信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Summary: str
        :param _TextTagSet: 文本标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TextTagSet: :class:`tencentcloud.ivld.v20210903.models.MultiLevelTag`
        :param _WebMediaURL: 文档下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type WebMediaURL: str
        """
        self._Content = None
        self._Summary = None
        self._TextTagSet = None
        self._WebMediaURL = None

    @property
    def Content(self):
        r"""文本内容信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Summary(self):
        r"""文本概要信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def TextTagSet(self):
        r"""文本标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ivld.v20210903.models.MultiLevelTag`
        """
        return self._TextTagSet

    @TextTagSet.setter
    def TextTagSet(self, TextTagSet):
        self._TextTagSet = TextTagSet

    @property
    def WebMediaURL(self):
        r"""文档下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WebMediaURL

    @WebMediaURL.setter
    def WebMediaURL(self, WebMediaURL):
        self._WebMediaURL = WebMediaURL


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._Summary = params.get("Summary")
        if params.get("TextTagSet") is not None:
            self._TextTagSet = MultiLevelTag()
            self._TextTagSet._deserialize(params.get("TextTagSet"))
        self._WebMediaURL = params.get("WebMediaURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextInfo(AbstractModel):
    r"""可视文本识别结果信息(OCR)

    """

    def __init__(self):
        r"""
        :param _Content: OCR提取的内容
        :type Content: str
        :param _StartTimeStamp: OCR起始时间戳，从0开始
        :type StartTimeStamp: float
        :param _EndTimeStamp: OCR结束时间戳，从0开始
        :type EndTimeStamp: float
        :param _Tag: OCR标签信息
        :type Tag: str
        """
        self._Content = None
        self._StartTimeStamp = None
        self._EndTimeStamp = None
        self._Tag = None

    @property
    def Content(self):
        r"""OCR提取的内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def StartTimeStamp(self):
        r"""OCR起始时间戳，从0开始
        :rtype: float
        """
        return self._StartTimeStamp

    @StartTimeStamp.setter
    def StartTimeStamp(self, StartTimeStamp):
        self._StartTimeStamp = StartTimeStamp

    @property
    def EndTimeStamp(self):
        r"""OCR结束时间戳，从0开始
        :rtype: float
        """
        return self._EndTimeStamp

    @EndTimeStamp.setter
    def EndTimeStamp(self, EndTimeStamp):
        self._EndTimeStamp = EndTimeStamp

    @property
    def Tag(self):
        r"""OCR标签信息
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._StartTimeStamp = params.get("StartTimeStamp")
        self._EndTimeStamp = params.get("EndTimeStamp")
        self._Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextMetadata(AbstractModel):
    r"""文本文件元信息

    """

    def __init__(self):
        r"""
        :param _FileSize: 媒资文本文件大小，单位为字节
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param _MD5: 媒资文本文件MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type MD5: str
        :param _Length: 媒资文本文件字符数
注意：此字段可能返回 null，表示取不到有效值。
        :type Length: int
        :param _Format: 媒资文本文件格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Format: str
        :param _ShortFormat: 封装格式短后缀
注意：此字段可能返回 null，表示取不到有效值。
        :type ShortFormat: str
        """
        self._FileSize = None
        self._MD5 = None
        self._Length = None
        self._Format = None
        self._ShortFormat = None

    @property
    def FileSize(self):
        r"""媒资文本文件大小，单位为字节
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def MD5(self):
        r"""媒资文本文件MD5
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MD5

    @MD5.setter
    def MD5(self, MD5):
        self._MD5 = MD5

    @property
    def Length(self):
        r"""媒资文本文件字符数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Format(self):
        r"""媒资文本文件格式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def ShortFormat(self):
        r"""封装格式短后缀
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ShortFormat

    @ShortFormat.setter
    def ShortFormat(self, ShortFormat):
        self._ShortFormat = ShortFormat


    def _deserialize(self, params):
        self._FileSize = params.get("FileSize")
        self._MD5 = params.get("MD5")
        self._Length = params.get("Length")
        self._Format = params.get("Format")
        self._ShortFormat = params.get("ShortFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextSegMatchShotScore(AbstractModel):
    r"""单个文本摘要分割结果和所有镜头的匹配度信息

    """

    def __init__(self):
        r"""
        :param _ScoreSet: 数组第 i 个值表示该文本摘要和第 i 个镜头的匹配度
注意：此字段可能返回 null，表示取不到有效值。
        :type ScoreSet: list of float
        """
        self._ScoreSet = None

    @property
    def ScoreSet(self):
        r"""数组第 i 个值表示该文本摘要和第 i 个镜头的匹配度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of float
        """
        return self._ScoreSet

    @ScoreSet.setter
    def ScoreSet(self, ScoreSet):
        self._ScoreSet = ScoreSet


    def _deserialize(self, params):
        self._ScoreSet = params.get("ScoreSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnknownPerson(AbstractModel):
    r"""未知人物信息

    """

    def __init__(self):
        r"""
        :param _VideoAppearSet: 视觉出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoAppearSet: list of VideoAppearInfo
        :param _PutLibraryAllowed: 未知人物是否可以入库(只有当未知人物人脸小图质量分符合要求时才可入库)
注意：此字段可能返回 null，表示取不到有效值。
        :type PutLibraryAllowed: bool
        :param _AuditClass: 内容审核结果: 0-正常;1-涉政;其他待确定
注意：此字段可能返回 null，表示取不到有效值。
        :type AuditClass: int
        """
        self._VideoAppearSet = None
        self._PutLibraryAllowed = None
        self._AuditClass = None

    @property
    def VideoAppearSet(self):
        r"""视觉出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of VideoAppearInfo
        """
        return self._VideoAppearSet

    @VideoAppearSet.setter
    def VideoAppearSet(self, VideoAppearSet):
        self._VideoAppearSet = VideoAppearSet

    @property
    def PutLibraryAllowed(self):
        r"""未知人物是否可以入库(只有当未知人物人脸小图质量分符合要求时才可入库)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._PutLibraryAllowed

    @PutLibraryAllowed.setter
    def PutLibraryAllowed(self, PutLibraryAllowed):
        self._PutLibraryAllowed = PutLibraryAllowed

    @property
    def AuditClass(self):
        r"""内容审核结果: 0-正常;1-涉政;其他待确定
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AuditClass

    @AuditClass.setter
    def AuditClass(self, AuditClass):
        self._AuditClass = AuditClass


    def _deserialize(self, params):
        if params.get("VideoAppearSet") is not None:
            self._VideoAppearSet = []
            for item in params.get("VideoAppearSet"):
                obj = VideoAppearInfo()
                obj._deserialize(item)
                self._VideoAppearSet.append(obj)
        self._PutLibraryAllowed = params.get("PutLibraryAllowed")
        self._AuditClass = params.get("AuditClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCustomCategoryRequest(AbstractModel):
    r"""UpdateCustomCategory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CategoryId: 自定义人物类型Id
        :type CategoryId: str
        :param _L1Category: 一级自定义人物类型
        :type L1Category: str
        :param _L2Category: 二级自定义人物类型
        :type L2Category: str
        """
        self._CategoryId = None
        self._L1Category = None
        self._L2Category = None

    @property
    def CategoryId(self):
        r"""自定义人物类型Id
        :rtype: str
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def L1Category(self):
        r"""一级自定义人物类型
        :rtype: str
        """
        return self._L1Category

    @L1Category.setter
    def L1Category(self, L1Category):
        self._L1Category = L1Category

    @property
    def L2Category(self):
        r"""二级自定义人物类型
        :rtype: str
        """
        return self._L2Category

    @L2Category.setter
    def L2Category(self, L2Category):
        self._L2Category = L2Category


    def _deserialize(self, params):
        self._CategoryId = params.get("CategoryId")
        self._L1Category = params.get("L1Category")
        self._L2Category = params.get("L2Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCustomCategoryResponse(AbstractModel):
    r"""UpdateCustomCategory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CategoryId: 成功更新的自定义人物类型Id
        :type CategoryId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CategoryId = None
        self._RequestId = None

    @property
    def CategoryId(self):
        r"""成功更新的自定义人物类型Id
        :rtype: str
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

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
        self._CategoryId = params.get("CategoryId")
        self._RequestId = params.get("RequestId")


class UpdateCustomPersonRequest(AbstractModel):
    r"""UpdateCustomPerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 待更新的自定义人物Id
        :type PersonId: str
        :param _Name: 更新后的自定义人物名称，如为空则不更新
        :type Name: str
        :param _BasicInfo: 更新后的自定义人物简介，如为空则不更新
        :type BasicInfo: str
        :param _CategoryId: 更新后的分类信息，如为空则不更新
        :type CategoryId: str
        """
        self._PersonId = None
        self._Name = None
        self._BasicInfo = None
        self._CategoryId = None

    @property
    def PersonId(self):
        r"""待更新的自定义人物Id
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Name(self):
        r"""更新后的自定义人物名称，如为空则不更新
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BasicInfo(self):
        r"""更新后的自定义人物简介，如为空则不更新
        :rtype: str
        """
        return self._BasicInfo

    @BasicInfo.setter
    def BasicInfo(self, BasicInfo):
        self._BasicInfo = BasicInfo

    @property
    def CategoryId(self):
        r"""更新后的分类信息，如为空则不更新
        :rtype: str
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._Name = params.get("Name")
        self._BasicInfo = params.get("BasicInfo")
        self._CategoryId = params.get("CategoryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCustomPersonResponse(AbstractModel):
    r"""UpdateCustomPerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 成功更新的自定义人物Id
        :type PersonId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PersonId = None
        self._RequestId = None

    @property
    def PersonId(self):
        r"""成功更新的自定义人物Id
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

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
        self._PersonId = params.get("PersonId")
        self._RequestId = params.get("RequestId")


class VideoAppearInfo(AbstractModel):
    r"""关键词在视觉结果中的定位信息

    """

    def __init__(self):
        r"""
        :param _StartTimeStamp: 视觉信息起始时间戳，从0开始
        :type StartTimeStamp: float
        :param _EndTimeStamp: 视觉信息终止时间戳，从0开始
关键词在视觉信息中的区间为[StartTimeStamp, EndTimeStamp)
        :type EndTimeStamp: float
        :param _ImageURL: 关键词在视觉信息中的封面图片
        :type ImageURL: str
        """
        self._StartTimeStamp = None
        self._EndTimeStamp = None
        self._ImageURL = None

    @property
    def StartTimeStamp(self):
        r"""视觉信息起始时间戳，从0开始
        :rtype: float
        """
        return self._StartTimeStamp

    @StartTimeStamp.setter
    def StartTimeStamp(self, StartTimeStamp):
        self._StartTimeStamp = StartTimeStamp

    @property
    def EndTimeStamp(self):
        r"""视觉信息终止时间戳，从0开始
关键词在视觉信息中的区间为[StartTimeStamp, EndTimeStamp)
        :rtype: float
        """
        return self._EndTimeStamp

    @EndTimeStamp.setter
    def EndTimeStamp(self, EndTimeStamp):
        self._EndTimeStamp = EndTimeStamp

    @property
    def ImageURL(self):
        r"""关键词在视觉信息中的封面图片
        :rtype: str
        """
        return self._ImageURL

    @ImageURL.setter
    def ImageURL(self, ImageURL):
        self._ImageURL = ImageURL


    def _deserialize(self, params):
        self._StartTimeStamp = params.get("StartTimeStamp")
        self._EndTimeStamp = params.get("EndTimeStamp")
        self._ImageURL = params.get("ImageURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoRotationMode(AbstractModel):
    r"""视频横转竖的控制参数

    """

    def __init__(self):
        r"""
        :param _ActiveVideoRotation: 生成的视频是否需要横屏转竖屏。
        :type ActiveVideoRotation: bool
        """
        self._ActiveVideoRotation = None

    @property
    def ActiveVideoRotation(self):
        r"""生成的视频是否需要横屏转竖屏。
        :rtype: bool
        """
        return self._ActiveVideoRotation

    @ActiveVideoRotation.setter
    def ActiveVideoRotation(self, ActiveVideoRotation):
        self._ActiveVideoRotation = ActiveVideoRotation


    def _deserialize(self, params):
        self._ActiveVideoRotation = params.get("ActiveVideoRotation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        