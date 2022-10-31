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


class AddCustomPersonImageRequest(AbstractModel):
    """AddCustomPersonImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param PersonId: 自定义人物Id
        :type PersonId: str
        :param ImageURL: 自定义人物图片地址
        :type ImageURL: str
        :param Image: 图片数据base64之后的结果
        :type Image: str
        """
        self.PersonId = None
        self.ImageURL = None
        self.Image = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.ImageURL = params.get("ImageURL")
        self.Image = params.get("Image")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCustomPersonImageResponse(AbstractModel):
    """AddCustomPersonImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param PersonId: 自定义人物Id
        :type PersonId: str
        :param ImageInfo: 自定义人脸图片信息
        :type ImageInfo: :class:`tencentcloud.ivld.v20210903.models.PersonImageInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PersonId = None
        self.ImageInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        if params.get("ImageInfo") is not None:
            self.ImageInfo = PersonImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        self.RequestId = params.get("RequestId")


class AppearIndexPair(AbstractModel):
    """出现信息索引对

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
        :param AppearIndex: 出现信息，取值范围为[1，3]
        :type AppearIndex: int
        :param Index: AppearInfo中AppearIndex对应元素的第Index元素，从0开始技术
        :type Index: int
        """
        self.AppearIndex = None
        self.Index = None


    def _deserialize(self, params):
        self.AppearIndex = params.get("AppearIndex")
        self.Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppearInfo(AbstractModel):
    """出现信息结构

    包含关键词在音频转文字(ASR)，图片转文字(OCR)以及视频结果中的出现信息

    """

    def __init__(self):
        r"""
        :param AudioAppearSet: 关键词在音频文本结果中的出现位置数组
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioAppearSet: list of TextAppearInfo
        :param TextAppearSet: 关键词在可视文本结果中的出现位置数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TextAppearSet: list of TextAppearInfo
        :param VideoAppearSet: 关键词在视频信息中的出现位置数组
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoAppearSet: list of VideoAppearInfo
        """
        self.AudioAppearSet = None
        self.TextAppearSet = None
        self.VideoAppearSet = None


    def _deserialize(self, params):
        if params.get("AudioAppearSet") is not None:
            self.AudioAppearSet = []
            for item in params.get("AudioAppearSet"):
                obj = TextAppearInfo()
                obj._deserialize(item)
                self.AudioAppearSet.append(obj)
        if params.get("TextAppearSet") is not None:
            self.TextAppearSet = []
            for item in params.get("TextAppearSet"):
                obj = TextAppearInfo()
                obj._deserialize(item)
                self.TextAppearSet.append(obj)
        if params.get("VideoAppearSet") is not None:
            self.VideoAppearSet = []
            for item in params.get("VideoAppearSet"):
                obj = VideoAppearInfo()
                obj._deserialize(item)
                self.VideoAppearSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioData(AbstractModel):
    """音频文件分析结果数据

    """

    def __init__(self):
        r"""
        :param AudioInfoSet: 音频识别文本结果
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioInfoSet: list of AudioInfo
        :param TextTagSet: 音频识别标签数据
        :type TextTagSet: :class:`tencentcloud.ivld.v20210903.models.MultiLevelTag`
        """
        self.AudioInfoSet = None
        self.TextTagSet = None


    def _deserialize(self, params):
        if params.get("AudioInfoSet") is not None:
            self.AudioInfoSet = []
            for item in params.get("AudioInfoSet"):
                obj = AudioInfo()
                obj._deserialize(item)
                self.AudioInfoSet.append(obj)
        if params.get("TextTagSet") is not None:
            self.TextTagSet = MultiLevelTag()
            self.TextTagSet._deserialize(params.get("TextTagSet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioInfo(AbstractModel):
    """音频识别结果信息

    """

    def __init__(self):
        r"""
        :param Content: ASR提取的文字信息
        :type Content: str
        :param StartTimeStamp: ASR起始时间戳，从0开始
        :type StartTimeStamp: float
        :param EndTimeStamp: ASR结束时间戳，从0开始
        :type EndTimeStamp: float
        :param Tag: ASR提取的音频标签
        :type Tag: str
        """
        self.Content = None
        self.StartTimeStamp = None
        self.EndTimeStamp = None
        self.Tag = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.StartTimeStamp = params.get("StartTimeStamp")
        self.EndTimeStamp = params.get("EndTimeStamp")
        self.Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioMetadata(AbstractModel):
    """音频文件元信息

    """

    def __init__(self):
        r"""
        :param FileSize: 媒资音频文件大小，单位为Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param MD5: 媒资音频文件MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type MD5: str
        :param Duration: 媒资音频时长，单位为秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: float
        :param SampleRate: 媒资音频采样率，单位为khz
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleRate: float
        :param BitRate: 媒资音频码率，单位为kbps
注意：此字段可能返回 null，表示取不到有效值。
        :type BitRate: int
        :param Format: 媒资音频文件格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Format: str
        """
        self.FileSize = None
        self.MD5 = None
        self.Duration = None
        self.SampleRate = None
        self.BitRate = None
        self.Format = None


    def _deserialize(self, params):
        self.FileSize = params.get("FileSize")
        self.MD5 = params.get("MD5")
        self.Duration = params.get("Duration")
        self.SampleRate = params.get("SampleRate")
        self.BitRate = params.get("BitRate")
        self.Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifiedPersonInfo(AbstractModel):
    """已分类的人物信息

    """

    def __init__(self):
        r"""
        :param ClassifyName: 人物分类名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassifyName: str
        :param PersonInfoSet: 符合特定分类的人物信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonInfoSet: list of PersonInfo
        """
        self.ClassifyName = None
        self.PersonInfoSet = None


    def _deserialize(self, params):
        self.ClassifyName = params.get("ClassifyName")
        if params.get("PersonInfoSet") is not None:
            self.PersonInfoSet = []
            for item in params.get("PersonInfoSet"):
                obj = PersonInfo()
                obj._deserialize(item)
                self.PersonInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomCategoryRequest(AbstractModel):
    """CreateCustomCategory请求参数结构体

    """

    def __init__(self):
        r"""
        :param L1Category: 自定义一级类型
        :type L1Category: str
        :param L2Category: 自定义二级类型
        :type L2Category: str
        """
        self.L1Category = None
        self.L2Category = None


    def _deserialize(self, params):
        self.L1Category = params.get("L1Category")
        self.L2Category = params.get("L2Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomCategoryResponse(AbstractModel):
    """CreateCustomCategory返回参数结构体

    """

    def __init__(self):
        r"""
        :param CategoryId: 自定义分类信息ID
        :type CategoryId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CategoryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CategoryId = params.get("CategoryId")
        self.RequestId = params.get("RequestId")


class CreateCustomGroupRequest(AbstractModel):
    """CreateCustomGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param Bucket: 人脸图片COS存储桶Host地址
        :type Bucket: str
        """
        self.Bucket = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomGroupResponse(AbstractModel):
    """CreateCustomGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateCustomPersonRequest(AbstractModel):
    """CreateCustomPerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 自定义人物姓名
        :type Name: str
        :param BasicInfo: 自定义人物简要信息(仅用于标记，不支持检索)
        :type BasicInfo: str
        :param CategoryId: 自定义分类ID，如不存在接口会报错
        :type CategoryId: str
        :param ImageURL: 自定义人物图片URL，可支持任意地址，推荐使用COS
        :type ImageURL: str
        :param Image: 原始图片base64编码后的数据
        :type Image: str
        """
        self.Name = None
        self.BasicInfo = None
        self.CategoryId = None
        self.ImageURL = None
        self.Image = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.BasicInfo = params.get("BasicInfo")
        self.CategoryId = params.get("CategoryId")
        self.ImageURL = params.get("ImageURL")
        self.Image = params.get("Image")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomPersonResponse(AbstractModel):
    """CreateCustomPerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param PersonId: 自定义人物Id
        :type PersonId: str
        :param ImageInfo: 自定义人脸信息
        :type ImageInfo: :class:`tencentcloud.ivld.v20210903.models.PersonImageInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PersonId = None
        self.ImageInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        if params.get("ImageInfo") is not None:
            self.ImageInfo = PersonImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        self.RequestId = params.get("RequestId")


class CreateDefaultCategoriesRequest(AbstractModel):
    """CreateDefaultCategories请求参数结构体

    """


class CreateDefaultCategoriesResponse(AbstractModel):
    """CreateDefaultCategories返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTaskRequest(AbstractModel):
    """CreateTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param MediaId: 媒资文件ID，最长32B
        :type MediaId: str
        :param MediaPreknownInfo: 媒资素材先验知识，相关限制参考MediaPreknownInfo
        :type MediaPreknownInfo: :class:`tencentcloud.ivld.v20210903.models.MediaPreknownInfo`
        :param TaskName: 任务名称，最长100个中文字符
        :type TaskName: str
        :param UploadVideo: 是否上传转码后的视频，仅设置true时上传，默认为false
        :type UploadVideo: bool
        :param Label: 自定义标签，可用于查询
        :type Label: str
        :param CallbackURL: 任务分析完成的回调地址，该设置优先级高于控制台全局的设置；
        :type CallbackURL: str
        """
        self.MediaId = None
        self.MediaPreknownInfo = None
        self.TaskName = None
        self.UploadVideo = None
        self.Label = None
        self.CallbackURL = None


    def _deserialize(self, params):
        self.MediaId = params.get("MediaId")
        if params.get("MediaPreknownInfo") is not None:
            self.MediaPreknownInfo = MediaPreknownInfo()
            self.MediaPreknownInfo._deserialize(params.get("MediaPreknownInfo"))
        self.TaskName = params.get("TaskName")
        self.UploadVideo = params.get("UploadVideo")
        self.Label = params.get("Label")
        self.CallbackURL = params.get("CallbackURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskResponse(AbstractModel):
    """CreateTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 智能标签视频分析任务ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CustomCategory(AbstractModel):
    """自定义分类信息

    """

    def __init__(self):
        r"""
        :param CategoryId: 自定义分类ID
        :type CategoryId: str
        :param L1Category: 一级自定义类型
        :type L1Category: str
        :param L2Category: 二级自定义类型
        :type L2Category: str
        """
        self.CategoryId = None
        self.L1Category = None
        self.L2Category = None


    def _deserialize(self, params):
        self.CategoryId = params.get("CategoryId")
        self.L1Category = params.get("L1Category")
        self.L2Category = params.get("L2Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomPersonFilter(AbstractModel):
    """自定义人物批量查询过滤条件

    """

    def __init__(self):
        r"""
        :param Name: 待查询的人物姓名
        :type Name: str
        :param CategoryIdSet: 待过滤的自定义类型Id数组
        :type CategoryIdSet: list of str
        :param PersonIdSet: 待过滤的自定义人物Id数组
        :type PersonIdSet: list of str
        :param L1CategorySet: 一级自定义人物类型数组
        :type L1CategorySet: list of str
        """
        self.Name = None
        self.CategoryIdSet = None
        self.PersonIdSet = None
        self.L1CategorySet = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CategoryIdSet = params.get("CategoryIdSet")
        self.PersonIdSet = params.get("PersonIdSet")
        self.L1CategorySet = params.get("L1CategorySet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomPersonInfo(AbstractModel):
    """自定义人物信息

    """

    def __init__(self):
        r"""
        :param PersonId: 自定义人物Id
        :type PersonId: str
        :param Name: 自定义人物姓名
        :type Name: str
        :param BasicInfo: 自定义人物简介信息
        :type BasicInfo: str
        :param L1Category: 一级自定义人物类型
        :type L1Category: str
        :param L2Category: 二级自定义人物类型
        :type L2Category: str
        :param ImageInfoSet: 自定义人物图片信息
        :type ImageInfoSet: list of PersonImageInfo
        :param CreateTime: 自定义人物创建时间
        :type CreateTime: str
        """
        self.PersonId = None
        self.Name = None
        self.BasicInfo = None
        self.L1Category = None
        self.L2Category = None
        self.ImageInfoSet = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Name = params.get("Name")
        self.BasicInfo = params.get("BasicInfo")
        self.L1Category = params.get("L1Category")
        self.L2Category = params.get("L2Category")
        if params.get("ImageInfoSet") is not None:
            self.ImageInfoSet = []
            for item in params.get("ImageInfoSet"):
                obj = PersonImageInfo()
                obj._deserialize(item)
                self.ImageInfoSet.append(obj)
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Data(AbstractModel):
    """任务结果数据

    """

    def __init__(self):
        r"""
        :param ShowInfo: 节目粒度结构化结果
注意：此字段可能返回 null，表示取不到有效值。
        :type ShowInfo: :class:`tencentcloud.ivld.v20210903.models.ShowInfo`
        """
        self.ShowInfo = None


    def _deserialize(self, params):
        if params.get("ShowInfo") is not None:
            self.ShowInfo = ShowInfo()
            self.ShowInfo._deserialize(params.get("ShowInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomCategoryRequest(AbstractModel):
    """DeleteCustomCategory请求参数结构体

    """

    def __init__(self):
        r"""
        :param CategoryId: 自定义分类ID
        :type CategoryId: str
        """
        self.CategoryId = None


    def _deserialize(self, params):
        self.CategoryId = params.get("CategoryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomCategoryResponse(AbstractModel):
    """DeleteCustomCategory返回参数结构体

    """

    def __init__(self):
        r"""
        :param CategoryId: 123
        :type CategoryId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CategoryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CategoryId = params.get("CategoryId")
        self.RequestId = params.get("RequestId")


class DeleteCustomPersonImageRequest(AbstractModel):
    """DeleteCustomPersonImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param PersonId: 自定义人物Id
        :type PersonId: str
        :param ImageId: 自定义人脸图片Id
        :type ImageId: str
        """
        self.PersonId = None
        self.ImageId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomPersonImageResponse(AbstractModel):
    """DeleteCustomPersonImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param PersonId: 自定义人物Id
        :type PersonId: str
        :param ImageId: 已删除的人物图片Id
        :type ImageId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PersonId = None
        self.ImageId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.ImageId = params.get("ImageId")
        self.RequestId = params.get("RequestId")


class DeleteCustomPersonRequest(AbstractModel):
    """DeleteCustomPerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param PersonId: 待删除的自定义人物ID
        :type PersonId: str
        """
        self.PersonId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomPersonResponse(AbstractModel):
    """DeleteCustomPerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param PersonId: 已删除的自定义人物Id
        :type PersonId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PersonId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.RequestId = params.get("RequestId")


class DeleteMediaRequest(AbstractModel):
    """DeleteMedia请求参数结构体

    """

    def __init__(self):
        r"""
        :param MediaId: 媒资文件在系统中的ID
        :type MediaId: str
        """
        self.MediaId = None


    def _deserialize(self, params):
        self.MediaId = params.get("MediaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMediaResponse(AbstractModel):
    """DeleteMedia返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTaskRequest(AbstractModel):
    """DeleteTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务Id
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTaskResponse(AbstractModel):
    """DeleteTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCustomCategoriesRequest(AbstractModel):
    """DescribeCustomCategories请求参数结构体

    """


class DescribeCustomCategoriesResponse(AbstractModel):
    """DescribeCustomCategories返回参数结构体

    """

    def __init__(self):
        r"""
        :param CategorySet: 自定义人物类型数组
        :type CategorySet: list of CustomCategory
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CategorySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CategorySet") is not None:
            self.CategorySet = []
            for item in params.get("CategorySet"):
                obj = CustomCategory()
                obj._deserialize(item)
                self.CategorySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCustomGroupRequest(AbstractModel):
    """DescribeCustomGroup请求参数结构体

    """


class DescribeCustomGroupResponse(AbstractModel):
    """DescribeCustomGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupSize: 自定义人物库所包含的人物个数
        :type GroupSize: int
        :param Bucket: 自定义人物库图片后续所在的存储桶
        :type Bucket: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupSize = None
        self.Bucket = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupSize = params.get("GroupSize")
        self.Bucket = params.get("Bucket")
        self.RequestId = params.get("RequestId")


class DescribeCustomPersonDetailRequest(AbstractModel):
    """DescribeCustomPersonDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param PersonId: 自定义人物Id
        :type PersonId: str
        """
        self.PersonId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomPersonDetailResponse(AbstractModel):
    """DescribeCustomPersonDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param PersonInfo: 自定义人物信息
        :type PersonInfo: :class:`tencentcloud.ivld.v20210903.models.CustomPersonInfo`
        :param TaskIdSet: 出现该自定义人物的所有分析人物Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PersonInfo = None
        self.TaskIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PersonInfo") is not None:
            self.PersonInfo = CustomPersonInfo()
            self.PersonInfo._deserialize(params.get("PersonInfo"))
        self.TaskIdSet = params.get("TaskIdSet")
        self.RequestId = params.get("RequestId")


class DescribeCustomPersonsRequest(AbstractModel):
    """DescribeCustomPersons请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNumber: 分页序号，从1开始
        :type PageNumber: int
        :param PageSize: 分页数据行数，最多50
        :type PageSize: int
        :param SortBy: 排序信息，默认倒序
        :type SortBy: :class:`tencentcloud.ivld.v20210903.models.SortBy`
        :param Filter: 自定义人物过滤条件
        :type Filter: :class:`tencentcloud.ivld.v20210903.models.CustomPersonFilter`
        """
        self.PageNumber = None
        self.PageSize = None
        self.SortBy = None
        self.Filter = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        if params.get("SortBy") is not None:
            self.SortBy = SortBy()
            self.SortBy._deserialize(params.get("SortBy"))
        if params.get("Filter") is not None:
            self.Filter = CustomPersonFilter()
            self.Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomPersonsResponse(AbstractModel):
    """DescribeCustomPersons返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 满足过滤条件的自定义人物数量
        :type TotalCount: int
        :param PersonInfoSet: 自定义人物信息
        :type PersonInfoSet: list of CustomPersonInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.PersonInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PersonInfoSet") is not None:
            self.PersonInfoSet = []
            for item in params.get("PersonInfoSet"):
                obj = CustomPersonInfo()
                obj._deserialize(item)
                self.PersonInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMediaRequest(AbstractModel):
    """DescribeMedia请求参数结构体

    """

    def __init__(self):
        r"""
        :param MediaId: 导入媒资返回的媒资ID，最长32B
        :type MediaId: str
        """
        self.MediaId = None


    def _deserialize(self, params):
        self.MediaId = params.get("MediaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaResponse(AbstractModel):
    """DescribeMedia返回参数结构体

    """

    def __init__(self):
        r"""
        :param MediaInfo: 媒资信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaInfo: :class:`tencentcloud.ivld.v20210903.models.MediaInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MediaInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MediaInfo") is not None:
            self.MediaInfo = MediaInfo()
            self.MediaInfo._deserialize(params.get("MediaInfo"))
        self.RequestId = params.get("RequestId")


class DescribeMediasRequest(AbstractModel):
    """DescribeMedias请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNumber: 分页序号，从1开始
        :type PageNumber: int
        :param PageSize: 每个分页所包含的元素数量，最大为50
        :type PageSize: int
        :param MediaFilter: 列举过滤条件，相关限制相见MediaFilter
        :type MediaFilter: :class:`tencentcloud.ivld.v20210903.models.MediaFilter`
        :param SortBy: 返回结果排序信息，By字段只支持CreateTime
        :type SortBy: :class:`tencentcloud.ivld.v20210903.models.SortBy`
        """
        self.PageNumber = None
        self.PageSize = None
        self.MediaFilter = None
        self.SortBy = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        if params.get("MediaFilter") is not None:
            self.MediaFilter = MediaFilter()
            self.MediaFilter._deserialize(params.get("MediaFilter"))
        if params.get("SortBy") is not None:
            self.SortBy = SortBy()
            self.SortBy._deserialize(params.get("SortBy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediasResponse(AbstractModel):
    """DescribeMedias返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 满足过滤条件的媒资视频总数量
        :type TotalCount: int
        :param MediaInfoSet: 满足过滤条件的媒资信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaInfoSet: list of MediaInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.MediaInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("MediaInfoSet") is not None:
            self.MediaInfoSet = []
            for item in params.get("MediaInfoSet"):
                obj = MediaInfo()
                obj._deserialize(item)
                self.MediaInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 创建任务返回的TaskId
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskInfo: 任务信息，不包含任务结果
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskInfo: :class:`tencentcloud.ivld.v20210903.models.TaskInfo`
        :param TaskData: 视频任务结果数据，只在视频任务结束时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskData: :class:`tencentcloud.ivld.v20210903.models.Data`
        :param ImageTaskData: 图片任务结果数据，只在图片任务结束时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageTaskData: :class:`tencentcloud.ivld.v20210903.models.ImageData`
        :param AudioTaskData: 音频任务结果数据，只在音频任务结束时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioTaskData: :class:`tencentcloud.ivld.v20210903.models.AudioData`
        :param TextTaskData: 文本任务结果数据，只在文本任务结束时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type TextTaskData: :class:`tencentcloud.ivld.v20210903.models.TextData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskInfo = None
        self.TaskData = None
        self.ImageTaskData = None
        self.AudioTaskData = None
        self.TextTaskData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskInfo") is not None:
            self.TaskInfo = TaskInfo()
            self.TaskInfo._deserialize(params.get("TaskInfo"))
        if params.get("TaskData") is not None:
            self.TaskData = Data()
            self.TaskData._deserialize(params.get("TaskData"))
        if params.get("ImageTaskData") is not None:
            self.ImageTaskData = ImageData()
            self.ImageTaskData._deserialize(params.get("ImageTaskData"))
        if params.get("AudioTaskData") is not None:
            self.AudioTaskData = AudioData()
            self.AudioTaskData._deserialize(params.get("AudioTaskData"))
        if params.get("TextTaskData") is not None:
            self.TextTaskData = TextData()
            self.TextTaskData._deserialize(params.get("TextTaskData"))
        self.RequestId = params.get("RequestId")


class DescribeTaskRequest(AbstractModel):
    """DescribeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: CreateTask返回的任务ID，最长32B
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskResponse(AbstractModel):
    """DescribeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskInfo: 任务信息，详情参见TaskInfo的定义
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskInfo: :class:`tencentcloud.ivld.v20210903.models.TaskInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskInfo") is not None:
            self.TaskInfo = TaskInfo()
            self.TaskInfo._deserialize(params.get("TaskInfo"))
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNumber: 分页序号，从1开始
        :type PageNumber: int
        :param PageSize: 每个分页所包含的元素数量，最大为50
        :type PageSize: int
        :param TaskFilter: 任务过滤条件，相关限制参见TaskFilter
        :type TaskFilter: :class:`tencentcloud.ivld.v20210903.models.TaskFilter`
        :param SortBy: 返回结果排序信息，By字段只支持CreateTimeStamp
        :type SortBy: :class:`tencentcloud.ivld.v20210903.models.SortBy`
        """
        self.PageNumber = None
        self.PageSize = None
        self.TaskFilter = None
        self.SortBy = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        if params.get("TaskFilter") is not None:
            self.TaskFilter = TaskFilter()
            self.TaskFilter._deserialize(params.get("TaskFilter"))
        if params.get("SortBy") is not None:
            self.SortBy = SortBy()
            self.SortBy._deserialize(params.get("SortBy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 满足过滤条件的任务总数量
        :type TotalCount: int
        :param TaskInfoSet: 满足过滤条件的任务数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskInfoSet: list of TaskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TaskInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TaskInfoSet") is not None:
            self.TaskInfoSet = []
            for item in params.get("TaskInfoSet"):
                obj = TaskInfo()
                obj._deserialize(item)
                self.TaskInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class ImageData(AbstractModel):
    """图片文件标签结果

    """

    def __init__(self):
        r"""
        :param OcrSet: 图片中出现的可视文本识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrSet: list of ImageOcr
        :param FrameTagSet: 图片中出现的帧标签识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameTagSet: :class:`tencentcloud.ivld.v20210903.models.MultiLevelTag`
        :param MultiLevelPersonInfoSet: 图片中出现的层级人物识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiLevelPersonInfoSet: list of MultiLevelPersonInfo
        :param TvLogo: 图片中出现的台标识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type TvLogo: :class:`tencentcloud.ivld.v20210903.models.ImageLogo`
        :param SourceLogo: 图片中出现的来源信息识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceLogo: :class:`tencentcloud.ivld.v20210903.models.ImageLogo`
        """
        self.OcrSet = None
        self.FrameTagSet = None
        self.MultiLevelPersonInfoSet = None
        self.TvLogo = None
        self.SourceLogo = None


    def _deserialize(self, params):
        if params.get("OcrSet") is not None:
            self.OcrSet = []
            for item in params.get("OcrSet"):
                obj = ImageOcr()
                obj._deserialize(item)
                self.OcrSet.append(obj)
        if params.get("FrameTagSet") is not None:
            self.FrameTagSet = MultiLevelTag()
            self.FrameTagSet._deserialize(params.get("FrameTagSet"))
        if params.get("MultiLevelPersonInfoSet") is not None:
            self.MultiLevelPersonInfoSet = []
            for item in params.get("MultiLevelPersonInfoSet"):
                obj = MultiLevelPersonInfo()
                obj._deserialize(item)
                self.MultiLevelPersonInfoSet.append(obj)
        if params.get("TvLogo") is not None:
            self.TvLogo = ImageLogo()
            self.TvLogo._deserialize(params.get("TvLogo"))
        if params.get("SourceLogo") is not None:
            self.SourceLogo = ImageLogo()
            self.SourceLogo._deserialize(params.get("SourceLogo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageLogo(AbstractModel):
    """图片中出现的Logo信息

    """

    def __init__(self):
        r"""
        :param Logo: 图片中出现的Logo识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Logo: str
        :param AppearRect: Logo在图片中出现的位置
注意：此字段可能返回 null，表示取不到有效值。
        :type AppearRect: :class:`tencentcloud.ivld.v20210903.models.Rectf`
        """
        self.Logo = None
        self.AppearRect = None


    def _deserialize(self, params):
        self.Logo = params.get("Logo")
        if params.get("AppearRect") is not None:
            self.AppearRect = Rectf()
            self.AppearRect._deserialize(params.get("AppearRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageMetadata(AbstractModel):
    """图片文件元信息

    """

    def __init__(self):
        r"""
        :param FileSize: 媒资图片文件大小，单位为Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param MD5: 媒资图片文件MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type MD5: str
        :param Width: 媒资图片文件宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param Height: 媒资图片文件高度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param Format: 媒资图片文件格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Format: str
        """
        self.FileSize = None
        self.MD5 = None
        self.Width = None
        self.Height = None
        self.Format = None


    def _deserialize(self, params):
        self.FileSize = params.get("FileSize")
        self.MD5 = params.get("MD5")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageOcr(AbstractModel):
    """图片OCR识别结果

    """

    def __init__(self):
        r"""
        :param Content: 图片中可视文本识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param AppearRect: 可视文本在图片中的位置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AppearRect: :class:`tencentcloud.ivld.v20210903.models.Rectf`
        """
        self.Content = None
        self.AppearRect = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        if params.get("AppearRect") is not None:
            self.AppearRect = Rectf()
            self.AppearRect._deserialize(params.get("AppearRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportMediaRequest(AbstractModel):
    """ImportMedia请求参数结构体

    """

    def __init__(self):
        r"""
        :param URL: 待分析视频的URL，目前只支持*不带签名的*COS地址，长度最长1KB
        :type URL: str
        :param MD5: 待分析视频的MD5，为空时不做校验，否则会做MD5校验，长度必须为32B
        :type MD5: str
        :param Name: 待分析视频的名称，指定后可支持筛选，最多64B
        :type Name: str
        :param WriteBackCosPath: 当非本人外部视频地址导入时，该字段为转存的cos桶地址且不可为空; 示例：https://${Bucket}-${AppId}.cos.${Region}.myqcloud.com/${PathPrefix}/  (注意，cos路径需要以/分隔符结尾)。
推荐采用本主帐号COS桶，如果使用其他帐号COS桶，请确保COS桶可写，否则可导致分析失败
        :type WriteBackCosPath: str
        :param Label: 自定义标签，可用于查询
        :type Label: str
        :param CallbackURL: 媒资导入完成的回调地址，该设置优先级高于控制台全局的设置；
        :type CallbackURL: str
        :param MediaType: 媒资文件类型，详细定义参见[MediaPreknownInfo.MediaType](https://cloud.tencent.com/document/product/1509/65063#MediaPreknownInfo)
默认为2(视频)
        :type MediaType: int
        """
        self.URL = None
        self.MD5 = None
        self.Name = None
        self.WriteBackCosPath = None
        self.Label = None
        self.CallbackURL = None
        self.MediaType = None


    def _deserialize(self, params):
        self.URL = params.get("URL")
        self.MD5 = params.get("MD5")
        self.Name = params.get("Name")
        self.WriteBackCosPath = params.get("WriteBackCosPath")
        self.Label = params.get("Label")
        self.CallbackURL = params.get("CallbackURL")
        self.MediaType = params.get("MediaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportMediaResponse(AbstractModel):
    """ImportMedia返回参数结构体

    """

    def __init__(self):
        r"""
        :param MediaId: 媒资文件在系统中的ID
        :type MediaId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MediaId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MediaId = params.get("MediaId")
        self.RequestId = params.get("RequestId")


class L1Tag(AbstractModel):
    """一级标签信息

    请注意，一级标签信息可能不包含二级标签(此时L2TagSet为空)。在这种情况下，一级标签可直接包含出现信息。

    """

    def __init__(self):
        r"""
        :param Name: 一级标签名
        :type Name: str
        :param L2TagSet: 二级标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :type L2TagSet: list of L2Tag
        :param AppearIndexPairSet: 一级标签出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AppearIndexPairSet: list of AppearIndexPair
        :param FirstAppear: 一级标签首次出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstAppear: int
        """
        self.Name = None
        self.L2TagSet = None
        self.AppearIndexPairSet = None
        self.FirstAppear = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("L2TagSet") is not None:
            self.L2TagSet = []
            for item in params.get("L2TagSet"):
                obj = L2Tag()
                obj._deserialize(item)
                self.L2TagSet.append(obj)
        if params.get("AppearIndexPairSet") is not None:
            self.AppearIndexPairSet = []
            for item in params.get("AppearIndexPairSet"):
                obj = AppearIndexPair()
                obj._deserialize(item)
                self.AppearIndexPairSet.append(obj)
        self.FirstAppear = params.get("FirstAppear")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L2Tag(AbstractModel):
    """二级标签信息

    请注意，二级标签信息可能不包含三级标签(此时L3TagSet为空)。

    """

    def __init__(self):
        r"""
        :param Name: 二级标签名
        :type Name: str
        :param L3TagSet: 从属于此二级标签的三级标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :type L3TagSet: list of L3Tag
        :param AppearIndexPairSet: 二级标签出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AppearIndexPairSet: list of AppearIndexPair
        :param FirstAppear: 二级标签首次出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstAppear: int
        """
        self.Name = None
        self.L3TagSet = None
        self.AppearIndexPairSet = None
        self.FirstAppear = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("L3TagSet") is not None:
            self.L3TagSet = []
            for item in params.get("L3TagSet"):
                obj = L3Tag()
                obj._deserialize(item)
                self.L3TagSet.append(obj)
        if params.get("AppearIndexPairSet") is not None:
            self.AppearIndexPairSet = []
            for item in params.get("AppearIndexPairSet"):
                obj = AppearIndexPair()
                obj._deserialize(item)
                self.AppearIndexPairSet.append(obj)
        self.FirstAppear = params.get("FirstAppear")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L3Tag(AbstractModel):
    """三级标签信息。

    三级标签不再包含任何子标签。所有三级标签都对应着识别结果中的出现信息，出现信息使用AppearIndexPairSet定位。

    """

    def __init__(self):
        r"""
        :param Name: 三级标签名
        :type Name: str
        :param AppearIndexPairSet: 三级标签出现信息索引数组
注意：此字段可能返回 null，表示取不到有效值。
        :type AppearIndexPairSet: list of AppearIndexPair
        :param FirstAppear: 三级标签首次出现信息，可选值为[1,3]
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstAppear: int
        """
        self.Name = None
        self.AppearIndexPairSet = None
        self.FirstAppear = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("AppearIndexPairSet") is not None:
            self.AppearIndexPairSet = []
            for item in params.get("AppearIndexPairSet"):
                obj = AppearIndexPair()
                obj._deserialize(item)
                self.AppearIndexPairSet.append(obj)
        self.FirstAppear = params.get("FirstAppear")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaFilter(AbstractModel):
    """媒资过滤条件


    """

    def __init__(self):
        r"""
        :param MediaNameSet: 媒资名称过滤条件
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaNameSet: list of str
        :param StatusSet: 媒资状态数组，媒资状态可选值参见MediaInfo
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusSet: list of int
        :param MediaIdSet: 媒资ID数组
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaIdSet: list of str
        :param LabelSet: 媒资自定义标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelSet: list of str
        :param MediaType: 媒资文件类型，定义参见[MediaPreknownInfo.MediaType](https://cloud.tencent.com/document/product/1509/65063#MediaPreknownInfo)
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaType: int
        """
        self.MediaNameSet = None
        self.StatusSet = None
        self.MediaIdSet = None
        self.LabelSet = None
        self.MediaType = None


    def _deserialize(self, params):
        self.MediaNameSet = params.get("MediaNameSet")
        self.StatusSet = params.get("StatusSet")
        self.MediaIdSet = params.get("MediaIdSet")
        self.LabelSet = params.get("LabelSet")
        self.MediaType = params.get("MediaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaInfo(AbstractModel):
    """媒资信息结构体

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
        :param MediaId: 媒资ID
        :type MediaId: str
        :param Name: 媒资名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param DownLoadURL: 媒资下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DownLoadURL: str
        :param Status: 媒资状态，取值参看上方表格
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param FailedReason: 若状态为失败，表示失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedReason: str
        :param Metadata: 媒资视频元信息，仅在MediaType=VIDEO时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Metadata: :class:`tencentcloud.ivld.v20210903.models.MediaMetadata`
        :param Progress: 导入视频进度，取值范围为[0,100]
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: float
        :param Label: 媒资自定义标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param CallbackURL: 媒资导入完成后的回调地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackURL: str
        :param MediaType: 媒资文件类型，具体参看[MediaPreknownInfo](https://cloud.tencent.com/document/product/1509/65063#MediaPreknownInfo)
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaType: int
        :param AudioMetadata: 媒资音频元信息，仅在MediaType=Audio时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioMetadata: :class:`tencentcloud.ivld.v20210903.models.AudioMetadata`
        :param ImageMetadata: 媒资图片文件元信息，仅在MediaType=Image时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageMetadata: :class:`tencentcloud.ivld.v20210903.models.ImageMetadata`
        :param TextMetadata: 媒资文本文件元信息，仅在MediaType=Text时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type TextMetadata: :class:`tencentcloud.ivld.v20210903.models.TextMetadata`
        """
        self.MediaId = None
        self.Name = None
        self.DownLoadURL = None
        self.Status = None
        self.FailedReason = None
        self.Metadata = None
        self.Progress = None
        self.Label = None
        self.CallbackURL = None
        self.MediaType = None
        self.AudioMetadata = None
        self.ImageMetadata = None
        self.TextMetadata = None


    def _deserialize(self, params):
        self.MediaId = params.get("MediaId")
        self.Name = params.get("Name")
        self.DownLoadURL = params.get("DownLoadURL")
        self.Status = params.get("Status")
        self.FailedReason = params.get("FailedReason")
        if params.get("Metadata") is not None:
            self.Metadata = MediaMetadata()
            self.Metadata._deserialize(params.get("Metadata"))
        self.Progress = params.get("Progress")
        self.Label = params.get("Label")
        self.CallbackURL = params.get("CallbackURL")
        self.MediaType = params.get("MediaType")
        if params.get("AudioMetadata") is not None:
            self.AudioMetadata = AudioMetadata()
            self.AudioMetadata._deserialize(params.get("AudioMetadata"))
        if params.get("ImageMetadata") is not None:
            self.ImageMetadata = ImageMetadata()
            self.ImageMetadata._deserialize(params.get("ImageMetadata"))
        if params.get("TextMetadata") is not None:
            self.TextMetadata = TextMetadata()
            self.TextMetadata._deserialize(params.get("TextMetadata"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaMetadata(AbstractModel):
    """媒资文件视频元信息，包括分辨率，帧率，码率等

    """

    def __init__(self):
        r"""
        :param FileSize: 媒资视频文件大小，单位为字节
        :type FileSize: int
        :param MD5: 媒资视频文件MD5
        :type MD5: str
        :param Duration: 媒资视频时长，单位为秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: float
        :param NumFrames: 媒资视频总帧数
注意：此字段可能返回 null，表示取不到有效值。
        :type NumFrames: int
        :param Width: 媒资视频宽度，单位为像素
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param Height: 媒资视频高度，单位为像素
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param FPS: 媒资视频帧率，单位为Hz
注意：此字段可能返回 null，表示取不到有效值。
        :type FPS: float
        :param BitRate: 媒资视频比特率，单位为kbps
注意：此字段可能返回 null，表示取不到有效值。
        :type BitRate: int
        """
        self.FileSize = None
        self.MD5 = None
        self.Duration = None
        self.NumFrames = None
        self.Width = None
        self.Height = None
        self.FPS = None
        self.BitRate = None


    def _deserialize(self, params):
        self.FileSize = params.get("FileSize")
        self.MD5 = params.get("MD5")
        self.Duration = params.get("Duration")
        self.NumFrames = params.get("NumFrames")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.FPS = params.get("FPS")
        self.BitRate = params.get("BitRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaPreknownInfo(AbstractModel):
    """描述输入媒资的先验知识，例如文件类型(视频)，媒体类型(新闻/综艺等)

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
        :param MediaType: 媒资文件类型，参见MediaPreknownInfo结构体定义
        :type MediaType: int
        :param MediaLabel: 媒资素材一级类型，参见MediaPreknownInfo结构体定义
        :type MediaLabel: int
        :param MediaSecondLabel: 媒资素材二级类型，参见MediaPreknownInfo结构体定义
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaSecondLabel: int
        :param MediaLang: 媒资音频类型，参见MediaPreknownInfo结构体定义
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaLang: int
        """
        self.MediaType = None
        self.MediaLabel = None
        self.MediaSecondLabel = None
        self.MediaLang = None


    def _deserialize(self, params):
        self.MediaType = params.get("MediaType")
        self.MediaLabel = params.get("MediaLabel")
        self.MediaSecondLabel = params.get("MediaSecondLabel")
        self.MediaLang = params.get("MediaLang")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCallbackRequest(AbstractModel):
    """ModifyCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskFinishNotifyURL: 任务分析完成后回调地址
        :type TaskFinishNotifyURL: str
        :param MediaFinishNotifyURL: 媒体导入完成后回调地址
        :type MediaFinishNotifyURL: str
        """
        self.TaskFinishNotifyURL = None
        self.MediaFinishNotifyURL = None


    def _deserialize(self, params):
        self.TaskFinishNotifyURL = params.get("TaskFinishNotifyURL")
        self.MediaFinishNotifyURL = params.get("MediaFinishNotifyURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCallbackResponse(AbstractModel):
    """ModifyCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MultiLevelPersonInfo(AbstractModel):
    """带类型树的已分类人物信息

    """

    def __init__(self):
        r"""
        :param L1ClassifyName: 一级分类名称(分类信息参见自定义人物类型)
注意：此字段可能返回 null，表示取不到有效值。
        :type L1ClassifyName: str
        :param L2ClassifiedPersonInfoSet: 已分类人物信息数组(所有分类类型为二级分类)
注意：此字段可能返回 null，表示取不到有效值。
        :type L2ClassifiedPersonInfoSet: list of ClassifiedPersonInfo
        :param Source: 检测结果来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: int
        """
        self.L1ClassifyName = None
        self.L2ClassifiedPersonInfoSet = None
        self.Source = None


    def _deserialize(self, params):
        self.L1ClassifyName = params.get("L1ClassifyName")
        if params.get("L2ClassifiedPersonInfoSet") is not None:
            self.L2ClassifiedPersonInfoSet = []
            for item in params.get("L2ClassifiedPersonInfoSet"):
                obj = ClassifiedPersonInfo()
                obj._deserialize(item)
                self.L2ClassifiedPersonInfoSet.append(obj)
        self.Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiLevelTag(AbstractModel):
    """标签信息结构体

    包含多级(最多三级)标签结果，以及这些标签在识别结果中的出现位置

    """

    def __init__(self):
        r"""
        :param TagSet: 树状标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSet: list of L1Tag
        :param AppearInfo: 标签在识别结果中的定位信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AppearInfo: :class:`tencentcloud.ivld.v20210903.models.AppearInfo`
        """
        self.TagSet = None
        self.AppearInfo = None


    def _deserialize(self, params):
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = L1Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        if params.get("AppearInfo") is not None:
            self.AppearInfo = AppearInfo()
            self.AppearInfo._deserialize(params.get("AppearInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonImageInfo(AbstractModel):
    """自定义人物人脸图片信息

    """

    def __init__(self):
        r"""
        :param ImageId: 人脸图片ID
        :type ImageId: str
        :param ImageURL: 自定义人脸图片的URL，存储在IVLDCustomPreson存储桶内
        :type ImageURL: str
        :param ErrorCode: 自定义人脸图片处理错误码
        :type ErrorCode: str
        :param ErrorMsg: 自定义人脸图片处理错误信息
        :type ErrorMsg: str
        """
        self.ImageId = None
        self.ImageURL = None
        self.ErrorCode = None
        self.ErrorMsg = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageURL = params.get("ImageURL")
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonInfo(AbstractModel):
    """人物信息

    """

    def __init__(self):
        r"""
        :param Name: 公众人物姓名
        :type Name: str
        :param Job: 公众人物职务
        :type Job: str
        :param FirstAppear: 首次出现模态，可选值为[1,3]，详细参见AppearIndex定义
        :type FirstAppear: int
        :param AppearInfo: 人物出现信息
        :type AppearInfo: :class:`tencentcloud.ivld.v20210903.models.AppearInfo`
        :param AppearRect: 人脸在图片中的位置，仅在图片标签任务有效
注意：此字段可能返回 null，表示取不到有效值。
        :type AppearRect: :class:`tencentcloud.ivld.v20210903.models.Rectf`
        """
        self.Name = None
        self.Job = None
        self.FirstAppear = None
        self.AppearInfo = None
        self.AppearRect = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Job = params.get("Job")
        self.FirstAppear = params.get("FirstAppear")
        if params.get("AppearInfo") is not None:
            self.AppearInfo = AppearInfo()
            self.AppearInfo._deserialize(params.get("AppearInfo"))
        if params.get("AppearRect") is not None:
            self.AppearRect = Rectf()
            self.AppearRect._deserialize(params.get("AppearRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCallbackRequest(AbstractModel):
    """QueryCallback请求参数结构体

    """


class QueryCallbackResponse(AbstractModel):
    """QueryCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskFinishNotifyURL: 任务分析完成后回调地址
        :type TaskFinishNotifyURL: str
        :param MediaFinishNotifyURL: 媒体导入完成后回调地址
        :type MediaFinishNotifyURL: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskFinishNotifyURL = None
        self.MediaFinishNotifyURL = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskFinishNotifyURL = params.get("TaskFinishNotifyURL")
        self.MediaFinishNotifyURL = params.get("MediaFinishNotifyURL")
        self.RequestId = params.get("RequestId")


class Rectf(AbstractModel):
    """矩形内容框

    """

    def __init__(self):
        r"""
        :param X: 矩形框左上角水平座标
注意：此字段可能返回 null，表示取不到有效值。
        :type X: float
        :param Y: 矩形框左上角竖直座标
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: float
        :param Width: 矩形框宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: float
        :param Height: 矩形框长度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: float
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShowInfo(AbstractModel):
    """视频结构化结果

    """

    def __init__(self):
        r"""
        :param Date: 节目日期(只在新闻有效)
注意：此字段可能返回 null，表示取不到有效值。
        :type Date: str
        :param Logo: 台标
注意：此字段可能返回 null，表示取不到有效值。
        :type Logo: str
        :param Column: 节目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Column: str
        :param Source: 来源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param CoverImageURL: 节目封面
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverImageURL: str
        :param SummarySet: 节目内容概要列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SummarySet: list of str
        :param TitleSet: 节目片段标题列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TitleSet: list of str
        :param AudioInfoSet: 音频识别结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioInfoSet: list of AudioInfo
        :param TextInfoSet: 可视文字识别结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TextInfoSet: list of TextInfo
        :param ClassifiedPersonInfoSet: 已分类人物信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassifiedPersonInfoSet: list of ClassifiedPersonInfo
        :param TextTagSet: 文本标签列表，包含标签内容和出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TextTagSet: :class:`tencentcloud.ivld.v20210903.models.MultiLevelTag`
        :param FrameTagSet: 帧标签列表，包括人物信息，场景信息等
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameTagSet: :class:`tencentcloud.ivld.v20210903.models.MultiLevelTag`
        :param WebMediaURL: 视频下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type WebMediaURL: str
        :param MediaClassifierSet: 媒资分类信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaClassifierSet: list of str
        :param SummaryTagSet: 概要标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SummaryTagSet: list of str
        :param UnknownPersonSet: 未知人物信息
注意：此字段可能返回 null，表示取不到有效值。
        :type UnknownPersonSet: list of UnknownPerson
        :param MultiLevelPersonInfoSet: 树状已分类人物信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiLevelPersonInfoSet: list of MultiLevelPersonInfo
        """
        self.Date = None
        self.Logo = None
        self.Column = None
        self.Source = None
        self.CoverImageURL = None
        self.SummarySet = None
        self.TitleSet = None
        self.AudioInfoSet = None
        self.TextInfoSet = None
        self.ClassifiedPersonInfoSet = None
        self.TextTagSet = None
        self.FrameTagSet = None
        self.WebMediaURL = None
        self.MediaClassifierSet = None
        self.SummaryTagSet = None
        self.UnknownPersonSet = None
        self.MultiLevelPersonInfoSet = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.Logo = params.get("Logo")
        self.Column = params.get("Column")
        self.Source = params.get("Source")
        self.CoverImageURL = params.get("CoverImageURL")
        self.SummarySet = params.get("SummarySet")
        self.TitleSet = params.get("TitleSet")
        if params.get("AudioInfoSet") is not None:
            self.AudioInfoSet = []
            for item in params.get("AudioInfoSet"):
                obj = AudioInfo()
                obj._deserialize(item)
                self.AudioInfoSet.append(obj)
        if params.get("TextInfoSet") is not None:
            self.TextInfoSet = []
            for item in params.get("TextInfoSet"):
                obj = TextInfo()
                obj._deserialize(item)
                self.TextInfoSet.append(obj)
        if params.get("ClassifiedPersonInfoSet") is not None:
            self.ClassifiedPersonInfoSet = []
            for item in params.get("ClassifiedPersonInfoSet"):
                obj = ClassifiedPersonInfo()
                obj._deserialize(item)
                self.ClassifiedPersonInfoSet.append(obj)
        if params.get("TextTagSet") is not None:
            self.TextTagSet = MultiLevelTag()
            self.TextTagSet._deserialize(params.get("TextTagSet"))
        if params.get("FrameTagSet") is not None:
            self.FrameTagSet = MultiLevelTag()
            self.FrameTagSet._deserialize(params.get("FrameTagSet"))
        self.WebMediaURL = params.get("WebMediaURL")
        self.MediaClassifierSet = params.get("MediaClassifierSet")
        self.SummaryTagSet = params.get("SummaryTagSet")
        if params.get("UnknownPersonSet") is not None:
            self.UnknownPersonSet = []
            for item in params.get("UnknownPersonSet"):
                obj = UnknownPerson()
                obj._deserialize(item)
                self.UnknownPersonSet.append(obj)
        if params.get("MultiLevelPersonInfoSet") is not None:
            self.MultiLevelPersonInfoSet = []
            for item in params.get("MultiLevelPersonInfoSet"):
                obj = MultiLevelPersonInfo()
                obj._deserialize(item)
                self.MultiLevelPersonInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SortBy(AbstractModel):
    """排序条件

    """

    def __init__(self):
        r"""
        :param By: 排序字段，默认为CreateTime
        :type By: str
        :param Descend: true表示降序，false表示升序
        :type Descend: bool
        """
        self.By = None
        self.Descend = None


    def _deserialize(self, params):
        self.By = params.get("By")
        self.Descend = params.get("Descend")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskFilter(AbstractModel):
    """任务筛选条件结构体

    """

    def __init__(self):
        r"""
        :param MediaTypeSet: 媒资文件类型
        :type MediaTypeSet: list of int
        :param TaskStatusSet: 待筛选的任务状态列表
        :type TaskStatusSet: list of int
        :param TaskNameSet: 待筛选的任务名称数组
        :type TaskNameSet: list of str
        :param TaskIdSet: TaskId数组
        :type TaskIdSet: list of str
        :param MediaNameSet: 媒资文件名数组
        :type MediaNameSet: list of str
        :param MediaLangSet: 媒资语言类型
        :type MediaLangSet: list of int
        :param MediaLabelSet: 媒资素材一级类型
        :type MediaLabelSet: list of int
        :param LabelSet: 媒资自定义标签数组
        :type LabelSet: list of str
        """
        self.MediaTypeSet = None
        self.TaskStatusSet = None
        self.TaskNameSet = None
        self.TaskIdSet = None
        self.MediaNameSet = None
        self.MediaLangSet = None
        self.MediaLabelSet = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.MediaTypeSet = params.get("MediaTypeSet")
        self.TaskStatusSet = params.get("TaskStatusSet")
        self.TaskNameSet = params.get("TaskNameSet")
        self.TaskIdSet = params.get("TaskIdSet")
        self.MediaNameSet = params.get("MediaNameSet")
        self.MediaLangSet = params.get("MediaLangSet")
        self.MediaLabelSet = params.get("MediaLabelSet")
        self.LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInfo(AbstractModel):
    """任务信息

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
        :param TaskId: 任务ID
        :type TaskId: str
        :param TaskName: 描述任务名称，指定后可根据名称筛选
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param MediaId: 媒资文件ID
        :type MediaId: str
        :param TaskStatus: 任务执行状态
        :type TaskStatus: int
        :param TaskProgress: 任务进度，范围为[0，100]
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskProgress: float
        :param TaskTimeCost: 任务执行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTimeCost: int
        :param TaskCreateTime: 任务创建时间
        :type TaskCreateTime: str
        :param TaskStartTime: 任务开始执行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskStartTime: str
        :param FailedReason: 任务失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedReason: str
        :param MediaPreknownInfo: 任务执行时指定的先验知识
        :type MediaPreknownInfo: :class:`tencentcloud.ivld.v20210903.models.MediaPreknownInfo`
        :param MediaName: 媒资文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaName: str
        :param Label: 媒资自定义标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param CallbackURL: 任务分析完成后的后调地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackURL: str
        :param AudioMetadata: 任务对应的媒资文件元信息，仅在MediaType为Audio时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioMetadata: :class:`tencentcloud.ivld.v20210903.models.AudioMetadata`
        :param ImageMetadata: 任务对应的媒资文件元信息，仅在MediaType为Audio时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageMetadata: :class:`tencentcloud.ivld.v20210903.models.ImageMetadata`
        :param TextMetadata: 任务对应的媒资文件元信息，仅在MediaType为Text时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type TextMetadata: :class:`tencentcloud.ivld.v20210903.models.TextMetadata`
        :param Metadata: 任务对应的媒资文件元信息，仅在MediaType为Video时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Metadata: :class:`tencentcloud.ivld.v20210903.models.MediaMetadata`
        """
        self.TaskId = None
        self.TaskName = None
        self.MediaId = None
        self.TaskStatus = None
        self.TaskProgress = None
        self.TaskTimeCost = None
        self.TaskCreateTime = None
        self.TaskStartTime = None
        self.FailedReason = None
        self.MediaPreknownInfo = None
        self.MediaName = None
        self.Label = None
        self.CallbackURL = None
        self.AudioMetadata = None
        self.ImageMetadata = None
        self.TextMetadata = None
        self.Metadata = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        self.MediaId = params.get("MediaId")
        self.TaskStatus = params.get("TaskStatus")
        self.TaskProgress = params.get("TaskProgress")
        self.TaskTimeCost = params.get("TaskTimeCost")
        self.TaskCreateTime = params.get("TaskCreateTime")
        self.TaskStartTime = params.get("TaskStartTime")
        self.FailedReason = params.get("FailedReason")
        if params.get("MediaPreknownInfo") is not None:
            self.MediaPreknownInfo = MediaPreknownInfo()
            self.MediaPreknownInfo._deserialize(params.get("MediaPreknownInfo"))
        self.MediaName = params.get("MediaName")
        self.Label = params.get("Label")
        self.CallbackURL = params.get("CallbackURL")
        if params.get("AudioMetadata") is not None:
            self.AudioMetadata = AudioMetadata()
            self.AudioMetadata._deserialize(params.get("AudioMetadata"))
        if params.get("ImageMetadata") is not None:
            self.ImageMetadata = ImageMetadata()
            self.ImageMetadata._deserialize(params.get("ImageMetadata"))
        if params.get("TextMetadata") is not None:
            self.TextMetadata = TextMetadata()
            self.TextMetadata._deserialize(params.get("TextMetadata"))
        if params.get("Metadata") is not None:
            self.Metadata = MediaMetadata()
            self.Metadata._deserialize(params.get("Metadata"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextAppearInfo(AbstractModel):
    """关键词在文本中的定位信息

    Position为关键词在文本中的偏移量，从0开始。例如，给定文本结果"欢迎收看新闻三十分”，以及关键词"新闻三十分"，那么StartPosition的值为4，EndPosition的值为9

    """

    def __init__(self):
        r"""
        :param Index: 文本结果数组中的下标
        :type Index: int
        :param StartPosition: 关键词在文本中出现的起始偏移量(包含)
        :type StartPosition: int
        :param EndPosition: 关键词在文本中出现的结束偏移量(不包含)
        :type EndPosition: int
        """
        self.Index = None
        self.StartPosition = None
        self.EndPosition = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.StartPosition = params.get("StartPosition")
        self.EndPosition = params.get("EndPosition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextData(AbstractModel):
    """文本文件标签识别结果

    """

    def __init__(self):
        r"""
        :param Content: 文本内容信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param Summary: 文本概要信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Summary: str
        :param TextTagSet: 文本标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TextTagSet: :class:`tencentcloud.ivld.v20210903.models.MultiLevelTag`
        """
        self.Content = None
        self.Summary = None
        self.TextTagSet = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.Summary = params.get("Summary")
        if params.get("TextTagSet") is not None:
            self.TextTagSet = MultiLevelTag()
            self.TextTagSet._deserialize(params.get("TextTagSet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextInfo(AbstractModel):
    """可视文本识别结果信息(OCR)

    """

    def __init__(self):
        r"""
        :param Content: OCR提取的内容
        :type Content: str
        :param StartTimeStamp: OCR起始时间戳，从0开始
        :type StartTimeStamp: float
        :param EndTimeStamp: OCR结束时间戳，从0开始
        :type EndTimeStamp: float
        :param Tag: OCR标签信息
        :type Tag: str
        """
        self.Content = None
        self.StartTimeStamp = None
        self.EndTimeStamp = None
        self.Tag = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.StartTimeStamp = params.get("StartTimeStamp")
        self.EndTimeStamp = params.get("EndTimeStamp")
        self.Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextMetadata(AbstractModel):
    """文本文件元信息

    """

    def __init__(self):
        r"""
        :param FileSize: 媒资文本文件大小，单位为字节
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param MD5: 媒资文本文件MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type MD5: str
        :param Length: 媒资文本文件字符数
注意：此字段可能返回 null，表示取不到有效值。
        :type Length: int
        :param Format: 媒资文本文件格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Format: str
        """
        self.FileSize = None
        self.MD5 = None
        self.Length = None
        self.Format = None


    def _deserialize(self, params):
        self.FileSize = params.get("FileSize")
        self.MD5 = params.get("MD5")
        self.Length = params.get("Length")
        self.Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnknownPerson(AbstractModel):
    """未知人物信息

    """

    def __init__(self):
        r"""
        :param VideoAppearSet: 视觉出现信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoAppearSet: list of VideoAppearInfo
        :param PutLibraryAllowed: 未知人物是否可以入库(只有当未知人物人脸小图质量分符合要求时才可入库)
注意：此字段可能返回 null，表示取不到有效值。
        :type PutLibraryAllowed: bool
        """
        self.VideoAppearSet = None
        self.PutLibraryAllowed = None


    def _deserialize(self, params):
        if params.get("VideoAppearSet") is not None:
            self.VideoAppearSet = []
            for item in params.get("VideoAppearSet"):
                obj = VideoAppearInfo()
                obj._deserialize(item)
                self.VideoAppearSet.append(obj)
        self.PutLibraryAllowed = params.get("PutLibraryAllowed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCustomCategoryRequest(AbstractModel):
    """UpdateCustomCategory请求参数结构体

    """

    def __init__(self):
        r"""
        :param CategoryId: 自定义人物类型Id
        :type CategoryId: str
        :param L1Category: 一级自定义人物类型
        :type L1Category: str
        :param L2Category: 二级自定义人物类型
        :type L2Category: str
        """
        self.CategoryId = None
        self.L1Category = None
        self.L2Category = None


    def _deserialize(self, params):
        self.CategoryId = params.get("CategoryId")
        self.L1Category = params.get("L1Category")
        self.L2Category = params.get("L2Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCustomCategoryResponse(AbstractModel):
    """UpdateCustomCategory返回参数结构体

    """

    def __init__(self):
        r"""
        :param CategoryId: 成功更新的自定义人物类型Id
        :type CategoryId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CategoryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CategoryId = params.get("CategoryId")
        self.RequestId = params.get("RequestId")


class UpdateCustomPersonRequest(AbstractModel):
    """UpdateCustomPerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param PersonId: 待更新的自定义人物Id
        :type PersonId: str
        :param Name: 更新后的自定义人物名称，如为空则不更新
        :type Name: str
        :param BasicInfo: 更新后的自定义人物简介，如为空则不更新
        :type BasicInfo: str
        :param CategoryId: 更新后的分类信息，如为空则不更新
        :type CategoryId: str
        """
        self.PersonId = None
        self.Name = None
        self.BasicInfo = None
        self.CategoryId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Name = params.get("Name")
        self.BasicInfo = params.get("BasicInfo")
        self.CategoryId = params.get("CategoryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCustomPersonResponse(AbstractModel):
    """UpdateCustomPerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param PersonId: 成功更新的自定义人物Id
        :type PersonId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PersonId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.RequestId = params.get("RequestId")


class VideoAppearInfo(AbstractModel):
    """关键词在视觉结果中的定位信息

    """

    def __init__(self):
        r"""
        :param StartTimeStamp: 视觉信息起始时间戳，从0开始
        :type StartTimeStamp: float
        :param EndTimeStamp: 视觉信息终止时间戳，从0开始
关键词在视觉信息中的区间为[StartTimeStamp, EndTimeStamp)
        :type EndTimeStamp: float
        :param ImageURL: 关键词在视觉信息中的封面图片
        :type ImageURL: str
        """
        self.StartTimeStamp = None
        self.EndTimeStamp = None
        self.ImageURL = None


    def _deserialize(self, params):
        self.StartTimeStamp = params.get("StartTimeStamp")
        self.EndTimeStamp = params.get("EndTimeStamp")
        self.ImageURL = params.get("ImageURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        