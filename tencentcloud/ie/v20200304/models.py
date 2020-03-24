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


class CallbackInfo(AbstractModel):
    """任务结果回调地址信息

    """

    def __init__(self):
        """
        :param Url: 回调URL。
        :type Url: str
        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")


class ClassificationEditingInfo(AbstractModel):
    """视频分类识别任务参数信息

    """

    def __init__(self):
        """
        :param Switch: 是否开启视频分类识别。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")


class ClassificationTaskResult(AbstractModel):
    """视频分类识别结果信息

    """

    def __init__(self):
        """
        :param Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param ItemSet: 视频分类识别结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemSet: list of ClassificationTaskResultItem
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.ItemSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self.ItemSet = []
            for item in params.get("ItemSet"):
                obj = ClassificationTaskResultItem()
                obj._deserialize(item)
                self.ItemSet.append(obj)


class ClassificationTaskResultItem(AbstractModel):
    """视频分类识别结果项

    """

    def __init__(self):
        """
        :param Classification: 分类名称。
        :type Classification: str
        :param Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self.Classification = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Classification = params.get("Classification")
        self.Confidence = params.get("Confidence")


class CosAuthMode(AbstractModel):
    """任务视频cos授权信息

    """

    def __init__(self):
        """
        :param Type: 授权类型，可选值： 
0：bucket授权，需要将对应bucket授权给本服务帐号（3020447271），否则会读写cos失败； 
1：key托管，把cos的账号id和key托管于本服务，本服务会提供一个托管id； 
3：临时key授权。
注意：目前智能编辑还不支持临时key授权。
        :type Type: int
        :param HostedId: cos账号托管id，Type等于1时必选。
        :type HostedId: str
        :param SecretId: cos身份识别id，Type等于3时必选。
        :type SecretId: str
        :param SecretKey: cos身份秘钥，Type等于3时必选。
        :type SecretKey: str
        :param Token: 临时授权 token，Type等于3时必选。
        :type Token: str
        """
        self.Type = None
        self.HostedId = None
        self.SecretId = None
        self.SecretKey = None
        self.Token = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.HostedId = params.get("HostedId")
        self.SecretId = params.get("SecretId")
        self.SecretKey = params.get("SecretKey")
        self.Token = params.get("Token")


class CosInfo(AbstractModel):
    """任务视频cos信息

    """

    def __init__(self):
        """
        :param Region: cos 区域值。例如：ap-beijing。
        :type Region: str
        :param Bucket: cos 存储桶，格式为BuketName-AppId。例如：test-123456。
        :type Bucket: str
        :param Path: cos 路径。 
对于写表示目录，例如：/test； 
对于读表示文件路径，例如：/test/test.mp4。
        :type Path: str
        :param CosAuthMode: cos 授权信息，不填默认为公有权限。
        :type CosAuthMode: :class:`tencentcloud.ie.v20200304.models.CosAuthMode`
        """
        self.Region = None
        self.Bucket = None
        self.Path = None
        self.CosAuthMode = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        self.Path = params.get("Path")
        if params.get("CosAuthMode") is not None:
            self.CosAuthMode = CosAuthMode()
            self.CosAuthMode._deserialize(params.get("CosAuthMode"))


class CoverEditingInfo(AbstractModel):
    """智能封面任务参数信息

    """

    def __init__(self):
        """
        :param Switch: 是否开启智能封面。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")


class CoverTaskResult(AbstractModel):
    """智能封面结果信息

    """

    def __init__(self):
        """
        :param Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param ItemSet: 智能封面结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemSet: list of CoverTaskResultItem
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.ItemSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self.ItemSet = []
            for item in params.get("ItemSet"):
                obj = CoverTaskResultItem()
                obj._deserialize(item)
                self.ItemSet.append(obj)


class CoverTaskResultItem(AbstractModel):
    """智能封面结果项

    """

    def __init__(self):
        """
        :param CoverUrl: 智能封面地址。
        :type CoverUrl: str
        :param Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self.CoverUrl = None
        self.Confidence = None


    def _deserialize(self, params):
        self.CoverUrl = params.get("CoverUrl")
        self.Confidence = params.get("Confidence")


class CreateEditingTaskRequest(AbstractModel):
    """CreateEditingTask请求参数结构体

    """

    def __init__(self):
        """
        :param EditingInfo: 智能编辑任务参数。
        :type EditingInfo: :class:`tencentcloud.ie.v20200304.models.EditingInfo`
        :param DownInfo: 视频源信息。
        :type DownInfo: :class:`tencentcloud.ie.v20200304.models.DownInfo`
        :param SaveInfo: 结果存储信息。对于包含智能拆条、智能集锦或者智能封面的任务必选。
        :type SaveInfo: :class:`tencentcloud.ie.v20200304.models.SaveInfo`
        :param CallbackInfo: 任务结果回调地址信息。
        :type CallbackInfo: :class:`tencentcloud.ie.v20200304.models.CallbackInfo`
        """
        self.EditingInfo = None
        self.DownInfo = None
        self.SaveInfo = None
        self.CallbackInfo = None


    def _deserialize(self, params):
        if params.get("EditingInfo") is not None:
            self.EditingInfo = EditingInfo()
            self.EditingInfo._deserialize(params.get("EditingInfo"))
        if params.get("DownInfo") is not None:
            self.DownInfo = DownInfo()
            self.DownInfo._deserialize(params.get("DownInfo"))
        if params.get("SaveInfo") is not None:
            self.SaveInfo = SaveInfo()
            self.SaveInfo._deserialize(params.get("SaveInfo"))
        if params.get("CallbackInfo") is not None:
            self.CallbackInfo = CallbackInfo()
            self.CallbackInfo._deserialize(params.get("CallbackInfo"))


class CreateEditingTaskResponse(AbstractModel):
    """CreateEditingTask返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 编辑任务 ID，可以通过该 ID 查询任务状态。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DescribeEditingTaskResultRequest(AbstractModel):
    """DescribeEditingTaskResult请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 编辑任务 ID。
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeEditingTaskResultResponse(AbstractModel):
    """DescribeEditingTaskResult返回参数结构体

    """

    def __init__(self):
        """
        :param TaskResult: 编辑任务结果信息。
        :type TaskResult: :class:`tencentcloud.ie.v20200304.models.EditingTaskResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskResult") is not None:
            self.TaskResult = EditingTaskResult()
            self.TaskResult._deserialize(params.get("TaskResult"))
        self.RequestId = params.get("RequestId")


class DownInfo(AbstractModel):
    """视频源信息

    """

    def __init__(self):
        """
        :param Type: 下载类型，可选值： 
0：UrlInfo； 
1：CosInfo。
        :type Type: int
        :param UrlInfo: Url形式下载信息，当Type等于0时必选。
        :type UrlInfo: :class:`tencentcloud.ie.v20200304.models.UrlInfo`
        :param CosInfo: Cos形式下载信息，当Type等于1时必选。
        :type CosInfo: :class:`tencentcloud.ie.v20200304.models.CosInfo`
        """
        self.Type = None
        self.UrlInfo = None
        self.CosInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("UrlInfo") is not None:
            self.UrlInfo = UrlInfo()
            self.UrlInfo._deserialize(params.get("UrlInfo"))
        if params.get("CosInfo") is not None:
            self.CosInfo = CosInfo()
            self.CosInfo._deserialize(params.get("CosInfo"))


class EditingInfo(AbstractModel):
    """智能编辑任务参数信息

    """

    def __init__(self):
        """
        :param TagEditingInfo: 视频标签识别任务参数，不填则不开启。
        :type TagEditingInfo: :class:`tencentcloud.ie.v20200304.models.TagEditingInfo`
        :param ClassificationEditingInfo: 视频分类识别任务参数，不填则不开启。
        :type ClassificationEditingInfo: :class:`tencentcloud.ie.v20200304.models.ClassificationEditingInfo`
        :param StripEditingInfo: 智能拆条任务参数，不填则不开启。
        :type StripEditingInfo: :class:`tencentcloud.ie.v20200304.models.StripEditingInfo`
        :param HighlightsEditingInfo: 智能集锦任务参数，不填则不开启。
        :type HighlightsEditingInfo: :class:`tencentcloud.ie.v20200304.models.HighlightsEditingInfo`
        :param CoverEditingInfo: 智能封面任务参数，不填则不开启。
        :type CoverEditingInfo: :class:`tencentcloud.ie.v20200304.models.CoverEditingInfo`
        :param OpeningEndingEditingInfo: 片头片尾识别任务参数，不填则不开启。
        :type OpeningEndingEditingInfo: :class:`tencentcloud.ie.v20200304.models.OpeningEndingEditingInfo`
        """
        self.TagEditingInfo = None
        self.ClassificationEditingInfo = None
        self.StripEditingInfo = None
        self.HighlightsEditingInfo = None
        self.CoverEditingInfo = None
        self.OpeningEndingEditingInfo = None


    def _deserialize(self, params):
        if params.get("TagEditingInfo") is not None:
            self.TagEditingInfo = TagEditingInfo()
            self.TagEditingInfo._deserialize(params.get("TagEditingInfo"))
        if params.get("ClassificationEditingInfo") is not None:
            self.ClassificationEditingInfo = ClassificationEditingInfo()
            self.ClassificationEditingInfo._deserialize(params.get("ClassificationEditingInfo"))
        if params.get("StripEditingInfo") is not None:
            self.StripEditingInfo = StripEditingInfo()
            self.StripEditingInfo._deserialize(params.get("StripEditingInfo"))
        if params.get("HighlightsEditingInfo") is not None:
            self.HighlightsEditingInfo = HighlightsEditingInfo()
            self.HighlightsEditingInfo._deserialize(params.get("HighlightsEditingInfo"))
        if params.get("CoverEditingInfo") is not None:
            self.CoverEditingInfo = CoverEditingInfo()
            self.CoverEditingInfo._deserialize(params.get("CoverEditingInfo"))
        if params.get("OpeningEndingEditingInfo") is not None:
            self.OpeningEndingEditingInfo = OpeningEndingEditingInfo()
            self.OpeningEndingEditingInfo._deserialize(params.get("OpeningEndingEditingInfo"))


class EditingTaskResult(AbstractModel):
    """智能识别任务结果信息

    """

    def __init__(self):
        """
        :param TaskId: 编辑任务 ID。
        :type TaskId: str
        :param Status: 编辑任务状态。 
1：执行中；2：已完成。
        :type Status: int
        :param TagTaskResult: 视频标签识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagTaskResult: :class:`tencentcloud.ie.v20200304.models.TagTaskResult`
        :param ClassificationTaskResult: 视频分类识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassificationTaskResult: :class:`tencentcloud.ie.v20200304.models.ClassificationTaskResult`
        :param StripTaskResult: 智能拆条结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type StripTaskResult: :class:`tencentcloud.ie.v20200304.models.StripTaskResult`
        :param HighlightsTaskResult: 智能集锦结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type HighlightsTaskResult: :class:`tencentcloud.ie.v20200304.models.HighlightsTaskResult`
        :param CoverTaskResult: 智能封面结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type CoverTaskResult: :class:`tencentcloud.ie.v20200304.models.CoverTaskResult`
        :param OpeningEndingTaskResult: 片头片尾识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type OpeningEndingTaskResult: :class:`tencentcloud.ie.v20200304.models.OpeningEndingTaskResult`
        """
        self.TaskId = None
        self.Status = None
        self.TagTaskResult = None
        self.ClassificationTaskResult = None
        self.StripTaskResult = None
        self.HighlightsTaskResult = None
        self.CoverTaskResult = None
        self.OpeningEndingTaskResult = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        if params.get("TagTaskResult") is not None:
            self.TagTaskResult = TagTaskResult()
            self.TagTaskResult._deserialize(params.get("TagTaskResult"))
        if params.get("ClassificationTaskResult") is not None:
            self.ClassificationTaskResult = ClassificationTaskResult()
            self.ClassificationTaskResult._deserialize(params.get("ClassificationTaskResult"))
        if params.get("StripTaskResult") is not None:
            self.StripTaskResult = StripTaskResult()
            self.StripTaskResult._deserialize(params.get("StripTaskResult"))
        if params.get("HighlightsTaskResult") is not None:
            self.HighlightsTaskResult = HighlightsTaskResult()
            self.HighlightsTaskResult._deserialize(params.get("HighlightsTaskResult"))
        if params.get("CoverTaskResult") is not None:
            self.CoverTaskResult = CoverTaskResult()
            self.CoverTaskResult._deserialize(params.get("CoverTaskResult"))
        if params.get("OpeningEndingTaskResult") is not None:
            self.OpeningEndingTaskResult = OpeningEndingTaskResult()
            self.OpeningEndingTaskResult._deserialize(params.get("OpeningEndingTaskResult"))


class HighlightsEditingInfo(AbstractModel):
    """智能集锦任务参数信息

    """

    def __init__(self):
        """
        :param Switch: 是否开启智能集锦。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")


class HighlightsTaskResult(AbstractModel):
    """智能集锦结果信息

    """

    def __init__(self):
        """
        :param Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param ItemSet: 智能集锦结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemSet: list of HighlightsTaskResultItem
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.ItemSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self.ItemSet = []
            for item in params.get("ItemSet"):
                obj = HighlightsTaskResultItem()
                obj._deserialize(item)
                self.ItemSet.append(obj)


class HighlightsTaskResultItem(AbstractModel):
    """智能集锦结果项

    """

    def __init__(self):
        """
        :param HighlightUrl: 智能集锦地址。
        :type HighlightUrl: str
        :param CovImgUrl: 智能集锦封面地址。
        :type CovImgUrl: str
        :param Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        :param Duration: 智能集锦持续时间，单位：秒。
        :type Duration: float
        :param SegmentSet: 智能集锦子片段结果集，集锦片段由这些子片段拼接生成。
        :type SegmentSet: list of HighlightsTaskResultItemSegment
        """
        self.HighlightUrl = None
        self.CovImgUrl = None
        self.Confidence = None
        self.Duration = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.HighlightUrl = params.get("HighlightUrl")
        self.CovImgUrl = params.get("CovImgUrl")
        self.Confidence = params.get("Confidence")
        self.Duration = params.get("Duration")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = HighlightsTaskResultItemSegment()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class HighlightsTaskResultItemSegment(AbstractModel):
    """智能集锦结果片段

    """

    def __init__(self):
        """
        :param Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        :param StartTimeOffset: 集锦片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 集锦片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        """
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class OpeningEndingEditingInfo(AbstractModel):
    """片头片尾识别任务参数信息

    """

    def __init__(self):
        """
        :param Switch: 是否开启片头片尾识别。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")


class OpeningEndingTaskResult(AbstractModel):
    """片头片尾识别结果信息

    """

    def __init__(self):
        """
        :param Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param Item: 片头片尾识别结果项。
注意：此字段可能返回 null，表示取不到有效值。
        :type Item: :class:`tencentcloud.ie.v20200304.models.OpeningEndingTaskResultItem`
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.Item = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("Item") is not None:
            self.Item = OpeningEndingTaskResultItem()
            self.Item._deserialize(params.get("Item"))


class OpeningEndingTaskResultItem(AbstractModel):
    """片头片尾识别结果项

    """

    def __init__(self):
        """
        :param OpeningTimeOffset: 视频片头的结束时间点，单位：秒。
        :type OpeningTimeOffset: float
        :param OpeningConfidence: 片头识别置信度，取值范围是 0 到 100。
        :type OpeningConfidence: float
        :param EndingTimeOffset: 视频片尾的开始时间点，单位：秒。
        :type EndingTimeOffset: float
        :param EndingConfidence: 片尾识别置信度，取值范围是 0 到 100。
        :type EndingConfidence: float
        """
        self.OpeningTimeOffset = None
        self.OpeningConfidence = None
        self.EndingTimeOffset = None
        self.EndingConfidence = None


    def _deserialize(self, params):
        self.OpeningTimeOffset = params.get("OpeningTimeOffset")
        self.OpeningConfidence = params.get("OpeningConfidence")
        self.EndingTimeOffset = params.get("EndingTimeOffset")
        self.EndingConfidence = params.get("EndingConfidence")


class SaveInfo(AbstractModel):
    """任务存储信息

    """

    def __init__(self):
        """
        :param Type: 存储类型，可选值： 
1：CosInfo。
        :type Type: int
        :param CosInfo: Cos形式存储信息，当Type等于1时必选。
        :type CosInfo: :class:`tencentcloud.ie.v20200304.models.CosInfo`
        """
        self.Type = None
        self.CosInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosInfo") is not None:
            self.CosInfo = CosInfo()
            self.CosInfo._deserialize(params.get("CosInfo"))


class StripEditingInfo(AbstractModel):
    """智能拆条任务参数信息

    """

    def __init__(self):
        """
        :param Switch: 是否开启智能拆条。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")


class StripTaskResult(AbstractModel):
    """智能拆条结果信息

    """

    def __init__(self):
        """
        :param Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param ItemSet: 智能拆条结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemSet: list of StripTaskResultItem
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.ItemSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self.ItemSet = []
            for item in params.get("ItemSet"):
                obj = StripTaskResultItem()
                obj._deserialize(item)
                self.ItemSet.append(obj)


class StripTaskResultItem(AbstractModel):
    """智能拆条结果项

    """

    def __init__(self):
        """
        :param SegmentUrl: 视频拆条片段地址。
        :type SegmentUrl: str
        :param CovImgUrl: 拆条封面图片地址。
        :type CovImgUrl: str
        :param Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        :param StartTimeOffset: 拆条片段起始的偏移时间，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 拆条片段终止的偏移时间，单位：秒。
        :type EndTimeOffset: float
        """
        self.SegmentUrl = None
        self.CovImgUrl = None
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.SegmentUrl = params.get("SegmentUrl")
        self.CovImgUrl = params.get("CovImgUrl")
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class TagEditingInfo(AbstractModel):
    """视频标签识别任务参数信息

    """

    def __init__(self):
        """
        :param Switch: 是否开启视频标签识别。0为关闭，1为开启。其他非0非1值默认为0。
        :type Switch: int
        :param CustomInfo: 额外定制化服务参数。参数为序列化的Json字符串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")


class TagTaskResult(AbstractModel):
    """视频标签识别结果信息

    """

    def __init__(self):
        """
        :param Status: 编辑任务状态。 
1：执行中；2：成功；3：失败。
        :type Status: int
        :param ErrCode: 编辑任务失败错误码。 
0：成功；其他值：失败。
        :type ErrCode: int
        :param ErrMsg: 编辑任务失败错误描述。
        :type ErrMsg: str
        :param ItemSet: 视频标签识别结果集。
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemSet: list of TagTaskResultItem
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.ItemSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self.ItemSet = []
            for item in params.get("ItemSet"):
                obj = TagTaskResultItem()
                obj._deserialize(item)
                self.ItemSet.append(obj)


class TagTaskResultItem(AbstractModel):
    """视频标签识别结果项

    """

    def __init__(self):
        """
        :param Tag: 标签名称。
        :type Tag: str
        :param Confidence: 置信度，取值范围是 0 到 100。
        :type Confidence: float
        """
        self.Tag = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Confidence = params.get("Confidence")


class UrlInfo(AbstractModel):
    """任务视频Url形式下载信息。

    """

    def __init__(self):
        """
        :param Url: 视频 URL。音视频支持mp4、ts等格式；直播流支持flv、rtmp格式。
注意：目前智能编辑还不支持直播流场景。
        :type Url: str
        :param Format: 视频地址格式，可选值： 
0：音视频 ;
1：直播流。 
默认为0。其他非0非1值默认为0。
        :type Format: int
        :param Host: 指定请求资源时，HTTP头部host的值。
        :type Host: str
        """
        self.Url = None
        self.Format = None
        self.Host = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Format = params.get("Format")
        self.Host = params.get("Host")