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


class AdaptiveDynamicStreamingTaskInput(AbstractModel):
    """对视频转自适应码流的输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 转自适应码流模板 ID。
        :type Definition: int
        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。
注意：此字段可能返回 null，表示取不到有效值。
        :type WatermarkSet: list of WatermarkInput
        :param OutputStorage: 转自适应码流后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 转自适应码流后，manifest 文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_adaptiveDynamicStreaming_{definition}.{format}`。
        :type OutputObjectPath: str
        :param SubStreamManifestObjectName: 转自适应码流（HLS）后，二级 index 文件的输出路径，只能为相对路径。如果不填，则默认为相对路径：`{inputName}_adaptiveDynamicStreaming_{definition}_{trackType}_{trackDefinition}.{format}`。
        :type SubStreamManifestObjectName: str
        :param SegmentObjectName: 转自适应码流后，分片文件的输出路径，只能为相对路径。如果不填，则默认为相对路径：`{inputName}_adaptiveDynamicStreaming_{definition}_{trackType}_{trackDefinition}_{number}.{format}`。
        :type SegmentObjectName: str
        :param ObjectNumberFormat: 转自适应码流后输出路径中的`{number}`变量的规则。
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectNumberFormat: :class:`tencentcloud.mps.v20190612.models.NumberFormat`
        """
        self.Definition = None
        self.WatermarkSet = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.SubStreamManifestObjectName = None
        self.SegmentObjectName = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        self.SubStreamManifestObjectName = params.get("SubStreamManifestObjectName")
        self.SegmentObjectName = params.get("SegmentObjectName")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))


class AiAnalysisTaskInput(AbstractModel):
    """AI 视频智能分析输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 视频内容分析模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiContentReviewTaskInput(AbstractModel):
    """智能内容审核任务类型

    """

    def __init__(self):
        """
        :param Definition: 视频内容审核模板 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskInput(AbstractModel):
    """视频内容识别输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 视频智能识别模板 ID 。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AnimatedGraphicTaskInput(AbstractModel):
    """转动图任务类型。

    """

    def __init__(self):
        """
        :param Definition: 视频转动图模板 ID。
        :type Definition: int
        :param StartTimeOffset: 动图在视频中的开始时间，单位为秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 动图在视频中的结束时间，单位为秒。
        :type EndTimeOffset: float
        :param OutputStorage: 转动图后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 转动图后文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_animatedGraphic_{definition}.{format}`。
        :type OutputObjectPath: str
        """
        self.Definition = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.OutputStorage = None
        self.OutputObjectPath = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")


class AnimatedGraphicsTemplate(AbstractModel):
    """转动图模板详情。

    """

    def __init__(self):
        """
        :param Definition: 转动图模板唯一标识。
        :type Definition: int
        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param Name: 转动图模板名称。
        :type Name: str
        :param Comment: 转动图模板描述。
        :type Comment: str
        :param Width: 动图宽度（或长边）的最大值。
        :type Width: int
        :param Height: 动图高度（或短边）的最大值。
        :type Height: int
        :param Format: 动图格式。
        :type Format: str
        :param Fps: 帧率。
        :type Fps: int
        :param Quality: 图片质量。
        :type Quality: float
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.Format = None
        self.Fps = None
        self.Quality = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Format = params.get("Format")
        self.Fps = params.get("Fps")
        self.Quality = params.get("Quality")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class AudioTemplateInfo(AbstractModel):
    """音频流配置参数

    """

    def __init__(self):
        """
        :param Codec: 音频流的编码格式。
当外层参数 Container 为 mp3 时，可选值为：
<li>libmp3lame。</li>
当外层参数 Container 为 ogg 或 flac 时，可选值为：
<li>flac。</li>
当外层参数 Container 为 m4a 时，可选值为：
<li>libfdk_aac；</li>
<li>libmp3lame；</li>
<li>ac3。</li>
当外层参数 Container 为 mp4 或 flv 时，可选值为：
<li>libfdk_aac：更适合 mp4；</li>
<li>libmp3lame：更适合 flv；</li>
<li>mp2。</li>
当外层参数 Container 为 hls 时，可选值为：
<li>libfdk_aac；</li>
<li>libmp3lame。</li>
        :type Codec: str
        :param Bitrate: 音频流的码率，取值范围：0 和 [26, 256]，单位：kbps。
当取值为 0，表示音频码率和原始音频保持一致。
        :type Bitrate: int
        :param SampleRate: 音频流的采样率，可选值：
<li>32000</li>
<li>44100</li>
<li>48000</li>
单位：Hz。
        :type SampleRate: int
        :param AudioChannel: 音频通道方式，可选值：
<li>1：单通道</li>
<li>2：双通道</li>
<li>6：立体声</li>
默认值：2。
        :type AudioChannel: int
        """
        self.Codec = None
        self.Bitrate = None
        self.SampleRate = None
        self.AudioChannel = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Bitrate = params.get("Bitrate")
        self.SampleRate = params.get("SampleRate")
        self.AudioChannel = params.get("AudioChannel")


class AudioTemplateInfoForUpdate(AbstractModel):
    """音频流配置参数

    """

    def __init__(self):
        """
        :param Codec: 音频流的编码格式。
当外层参数 Container 为 mp3 时，可选值为：
<li>libmp3lame。</li>
当外层参数 Container 为 ogg 或 flac 时，可选值为：
<li>flac。</li>
当外层参数 Container 为 m4a 时，可选值为：
<li>libfdk_aac；</li>
<li>libmp3lame；</li>
<li>ac3。</li>
当外层参数 Container 为 mp4 或 flv 时，可选值为：
<li>libfdk_aac：更适合 mp4；</li>
<li>libmp3lame：更适合 flv；</li>
<li>mp2。</li>
当外层参数 Container 为 hls 时，可选值为：
<li>libfdk_aac；</li>
<li>libmp3lame。</li>
        :type Codec: str
        :param Bitrate: 音频流的码率，取值范围：0 和 [26, 256]，单位：kbps。 当取值为 0，表示音频码率和原始音频保持一致。
        :type Bitrate: int
        :param SampleRate: 音频流的采样率，可选值：
<li>32000</li>
<li>44100</li>
<li>48000</li>
单位：Hz。
        :type SampleRate: int
        :param AudioChannel: 音频通道方式，可选值：
<li>1：单通道</li>
<li>2：双通道</li>
<li>6：立体声</li>
        :type AudioChannel: int
        """
        self.Codec = None
        self.Bitrate = None
        self.SampleRate = None
        self.AudioChannel = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Bitrate = params.get("Bitrate")
        self.SampleRate = params.get("SampleRate")
        self.AudioChannel = params.get("AudioChannel")


class CosFileUploadTrigger(AbstractModel):
    """绑定到 COS 的输入规则。

    """

    def __init__(self):
        """
        :param Bucket: 工作流绑定的 COS Bucket 名，如 TopRankVideo-125xxx88。
        :type Bucket: str
        :param Region: 工作流绑定的 COS Bucket 所属园区，如 ap-chongiqng。
        :type Region: str
        :param Dir: 工作流绑定的输入路径目录，如`/movie/201907/`，不填代表根目录`/`。
        :type Dir: str
        :param Formats: 工作流允许触发的文件格式列表，如 ["mp4", "flv", "mov"]。不填代表所有格式的文件都可以触发工作流。
        :type Formats: list of str
        """
        self.Bucket = None
        self.Region = None
        self.Dir = None
        self.Formats = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Dir = params.get("Dir")
        self.Formats = params.get("Formats")


class CosInputInfo(AbstractModel):
    """视频处理 COS 对象信息。

    """

    def __init__(self):
        """
        :param Bucket: 视频处理对象文件所在的 COS Bucket 名，如 TopRankVideo-125xxx88。
        :type Bucket: str
        :param Region: 视频处理对象文件所在的 COS Bucket 所属园区，如 ap-chongqing。
        :type Region: str
        :param Object: 视频处理对象文件的输入路径，如`/movie/201907/WildAnimal.mov`。
        :type Object: str
        """
        self.Bucket = None
        self.Region = None
        self.Object = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Object = params.get("Object")


class CosOutputStorage(AbstractModel):
    """视频处理 COS 输出对象信息。

    """

    def __init__(self):
        """
        :param Bucket: 视频处理生成的文件输出的目标 Bucket 名，如 TopRankVideo-125xxx88。如果不填，表示继承上层。
        :type Bucket: str
        :param Region: 视频处理生成的文件输出的目标 Bucket 的园区，如 ap-chongqing。如果不填，表示继承上层。
        :type Region: str
        """
        self.Bucket = None
        self.Region = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")


class CreateAnimatedGraphicsTemplateRequest(AbstractModel):
    """CreateAnimatedGraphicsTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Width: 动图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 视频流高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param Fps: 帧率，取值范围：[1, 30]，单位：Hz。
        :type Fps: int
        :param Format: 动图格式，取值为 gif 和 webp。默认为 gif。
        :type Format: str
        :param Quality: 图片质量，取值范围：[1, 100]，默认值为 75。
        :type Quality: float
        :param Name: 转动图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        """
        self.Width = None
        self.Height = None
        self.Fps = None
        self.Format = None
        self.Quality = None
        self.Name = None
        self.Comment = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.Format = params.get("Format")
        self.Quality = params.get("Quality")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")


class CreateAnimatedGraphicsTemplateResponse(AbstractModel):
    """CreateAnimatedGraphicsTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转动图模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateImageSpriteTemplateRequest(AbstractModel):
    """CreateImageSpriteTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Width: 雪碧图中小图的宽度，取值范围： [128, 4096]，单位：px。
        :type Width: int
        :param Height: 雪碧图中小图的高度，取值范围： [128, 4096]，单位：px。
        :type Height: int
        :param SampleType: 采样类型，取值：
<li>Percent：按百分比。</li>
<li>Time：按时间间隔。</li>
        :type SampleType: str
        :param SampleInterval: 采样间隔。
<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>
<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>
        :type SampleInterval: int
        :param RowCount: 雪碧图中小图的行数。
        :type RowCount: int
        :param ColumnCount: 雪碧图中小图的列数。
        :type ColumnCount: int
        :param Name: 雪碧图模板名称，长度限制：64 个字符。
        :type Name: str
        """
        self.Width = None
        self.Height = None
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.Name = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.Name = params.get("Name")


class CreateImageSpriteTemplateResponse(AbstractModel):
    """CreateImageSpriteTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 雪碧图模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateSampleSnapshotTemplateRequest(AbstractModel):
    """CreateSampleSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Width: 图片宽度，取值范围： [128, 4096]，单位：px。
        :type Width: int
        :param Height: 图片高度，取值范围： [128, 4096]，单位：px。
        :type Height: int
        :param SampleType: 采样截图类型，取值：
<li>Percent：按百分比。</li>
<li>Time：按时间间隔。</li>
        :type SampleType: str
        :param SampleInterval: 采样间隔。
<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>
<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>
        :type SampleInterval: int
        :param Name: 采样截图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Format: 图片格式，取值为 jpg 和 png。默认为 jpg。
        :type Format: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        """
        self.Width = None
        self.Height = None
        self.SampleType = None
        self.SampleInterval = None
        self.Name = None
        self.Format = None
        self.Comment = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.Name = params.get("Name")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")


class CreateSampleSnapshotTemplateResponse(AbstractModel):
    """CreateSampleSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 采样截图模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateSnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """CreateSnapshotByTimeOffsetTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Width: 图片宽度，取值范围： [128, 4096]，单位：px。
        :type Width: int
        :param Height: 图片高度，取值范围： [128, 4096]，单位：px。
        :type Height: int
        :param Name: 指定时间点截图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Format: 图片格式，取值可以为 jpg 和 png。默认为 jpg。
        :type Format: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        """
        self.Width = None
        self.Height = None
        self.Name = None
        self.Format = None
        self.Comment = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Name = params.get("Name")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")


class CreateSnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """CreateSnapshotByTimeOffsetTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 时间点截图模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateTranscodeTemplateRequest(AbstractModel):
    """CreateTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Container: 封装格式，可选值：mp4、flv、hls、mp3、flac、ogg、m4a。其中，mp3、flac、ogg、m4a 为纯音频文件。
        :type Container: str
        :param Name: 转码模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param RemoveVideo: 是否去除视频数据，可选值：
<li>0：保留</li>
<li>1：去除</li>
默认值：0。
        :type RemoveVideo: int
        :param RemoveAudio: 是否去除音频数据，可选值：
<li>0：保留</li>
<li>1：去除</li>
默认值：0。
        :type RemoveAudio: int
        :param VideoTemplate: 视频流配置参数，当 RemoveVideo 为 0，该字段必填。
        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfo`
        :param AudioTemplate: 音频流配置参数，当 RemoveAudio 为 0，该字段必填。
        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfo`
        :param TEHDConfig: 极速高清转码参数，需联系商务架构师开通后才能使用。
        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfig`
        """
        self.Container = None
        self.Name = None
        self.Comment = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None


    def _deserialize(self, params):
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))


class CreateTranscodeTemplateResponse(AbstractModel):
    """CreateTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转码模板唯一标识。
        :type Definition: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateWatermarkTemplateRequest(AbstractModel):
    """CreateWatermarkTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Type: 水印类型，可选值：
<li>image：图片水印；</li>
<li>text：文字水印。</li>
        :type Type: str
        :param Name: 水印模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param CoordinateOrigin: 原点位置，可选值：
<li>TopLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角；</li>
<li>TopRight：表示坐标原点位于视频图像的右上角，水印原点为图片或文字的右上角；</li>
<li>BottomLeft：表示坐标原点位于视频图像的左下角，水印原点为图片或文字的左下角；</li>
<li>BottomRight：表示坐标原点位于视频图像的右下角，水印原点为图片或文字的右下角。</li>
默认值：TopLeft。目前，当 Type 为 image，该字段仅支持 TopLeft。
        :type CoordinateOrigin: str
        :param XPos: 水印原点距离视频图像坐标原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 XPos 为视频宽度指定百分比，如 10% 表示 XPos 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 XPos 为指定像素，如 100px 表示 XPos 为 100 像素。</li>
默认值：0px。
        :type XPos: str
        :param YPos: 水印原点距离视频图像坐标原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 YPos 为视频高度指定百分比，如 10% 表示 YPos 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 YPos 为指定像素，如 100px 表示 YPos 为 100 像素。</li>
默认值：0px。
        :type YPos: str
        :param ImageTemplate: 图片水印模板，仅当 Type 为 image，该字段必填且有效。
        :type ImageTemplate: :class:`tencentcloud.mps.v20190612.models.ImageWatermarkInput`
        :param TextTemplate: 文字水印模板，仅当 Type 为 text，该字段必填且有效。
        :type TextTemplate: :class:`tencentcloud.mps.v20190612.models.TextWatermarkTemplateInput`
        :param SvgTemplate: SVG 水印模板，仅当 Type 为 svg，该字段必填且有效。
        :type SvgTemplate: :class:`tencentcloud.mps.v20190612.models.SvgWatermarkInput`
        """
        self.Type = None
        self.Name = None
        self.Comment = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkInput()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInput()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInput()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))


class CreateWatermarkTemplateResponse(AbstractModel):
    """CreateWatermarkTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 水印模板唯一标识。
        :type Definition: int
        :param ImageUrl: 水印图片地址，仅当 Type 为 image，该字段有效。
        :type ImageUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.ImageUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.ImageUrl = params.get("ImageUrl")
        self.RequestId = params.get("RequestId")


class CreateWorkflowRequest(AbstractModel):
    """CreateWorkflow请求参数结构体

    """

    def __init__(self):
        """
        :param WorkflowName: 工作流名称，最多128字符。同一个用户该名称唯一。
        :type WorkflowName: str
        :param Trigger: 工作流绑定的触发规则，当上传视频命中该规则到该对象时即触发工作流。
        :type Trigger: :class:`tencentcloud.mps.v20190612.models.WorkflowTrigger`
        :param OutputStorage: 视频处理的文件输出存储位置。不填则继承 Trigger 中的存储位置。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputDir: 视频处理生成的文件输出的目标目录，如`/movie/201907/`。如果不填，表示与触发文件所在的目录一致。
        :type OutputDir: str
        :param MediaProcessTask: 视频处理类型任务参数。
        :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`
        :param TaskNotifyConfig: 任务的事件通知配置，不填代表不获取事件通知。
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TaskPriority: 工作流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。
        :type TaskPriority: int
        """
        self.WorkflowName = None
        self.Trigger = None
        self.OutputStorage = None
        self.OutputDir = None
        self.MediaProcessTask = None
        self.TaskNotifyConfig = None
        self.TaskPriority = None


    def _deserialize(self, params):
        self.WorkflowName = params.get("WorkflowName")
        if params.get("Trigger") is not None:
            self.Trigger = WorkflowTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TaskPriority = params.get("TaskPriority")


class CreateWorkflowResponse(AbstractModel):
    """CreateWorkflow返回参数结构体

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WorkflowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        self.RequestId = params.get("RequestId")


class DeleteAnimatedGraphicsTemplateRequest(AbstractModel):
    """DeleteAnimatedGraphicsTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转动图模板唯一标识。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class DeleteAnimatedGraphicsTemplateResponse(AbstractModel):
    """DeleteAnimatedGraphicsTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageSpriteTemplateRequest(AbstractModel):
    """DeleteImageSpriteTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 雪碧图模板唯一标识。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class DeleteImageSpriteTemplateResponse(AbstractModel):
    """DeleteImageSpriteTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSampleSnapshotTemplateRequest(AbstractModel):
    """DeleteSampleSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 采样截图模板唯一标识。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class DeleteSampleSnapshotTemplateResponse(AbstractModel):
    """DeleteSampleSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """DeleteSnapshotByTimeOffsetTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 指定时间点截图模板唯一标识。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class DeleteSnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """DeleteSnapshotByTimeOffsetTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTranscodeTemplateRequest(AbstractModel):
    """DeleteTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转码模板唯一标识。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class DeleteTranscodeTemplateResponse(AbstractModel):
    """DeleteTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWatermarkTemplateRequest(AbstractModel):
    """DeleteWatermarkTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 水印模板唯一标识。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class DeleteWatermarkTemplateResponse(AbstractModel):
    """DeleteWatermarkTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWorkflowRequest(AbstractModel):
    """DeleteWorkflow请求参数结构体

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        """
        self.WorkflowId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")


class DeleteWorkflowResponse(AbstractModel):
    """DeleteWorkflow返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAnimatedGraphicsTemplatesRequest(AbstractModel):
    """DescribeAnimatedGraphicsTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 转动图模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")


class DescribeAnimatedGraphicsTemplatesResponse(AbstractModel):
    """DescribeAnimatedGraphicsTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param AnimatedGraphicsTemplateSet: 转动图模板详情列表。
        :type AnimatedGraphicsTemplateSet: list of AnimatedGraphicsTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AnimatedGraphicsTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AnimatedGraphicsTemplateSet") is not None:
            self.AnimatedGraphicsTemplateSet = []
            for item in params.get("AnimatedGraphicsTemplateSet"):
                obj = AnimatedGraphicsTemplate()
                obj._deserialize(item)
                self.AnimatedGraphicsTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImageSpriteTemplatesRequest(AbstractModel):
    """DescribeImageSpriteTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 雪碧图模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")


class DescribeImageSpriteTemplatesResponse(AbstractModel):
    """DescribeImageSpriteTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param ImageSpriteTemplateSet: 雪碧图模板详情列表。
        :type ImageSpriteTemplateSet: list of ImageSpriteTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ImageSpriteTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImageSpriteTemplateSet") is not None:
            self.ImageSpriteTemplateSet = []
            for item in params.get("ImageSpriteTemplateSet"):
                obj = ImageSpriteTemplate()
                obj._deserialize(item)
                self.ImageSpriteTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSampleSnapshotTemplatesRequest(AbstractModel):
    """DescribeSampleSnapshotTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 采样截图模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")


class DescribeSampleSnapshotTemplatesResponse(AbstractModel):
    """DescribeSampleSnapshotTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param SampleSnapshotTemplateSet: 采样截图模板详情列表。
        :type SampleSnapshotTemplateSet: list of SampleSnapshotTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SampleSnapshotTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SampleSnapshotTemplateSet") is not None:
            self.SampleSnapshotTemplateSet = []
            for item in params.get("SampleSnapshotTemplateSet"):
                obj = SampleSnapshotTemplate()
                obj._deserialize(item)
                self.SampleSnapshotTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotByTimeOffsetTemplatesRequest(AbstractModel):
    """DescribeSnapshotByTimeOffsetTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 指定时间点截图模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")


class DescribeSnapshotByTimeOffsetTemplatesResponse(AbstractModel):
    """DescribeSnapshotByTimeOffsetTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param SnapshotByTimeOffsetTemplateSet: 指定时间点截图模板详情列表。
        :type SnapshotByTimeOffsetTemplateSet: list of SnapshotByTimeOffsetTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SnapshotByTimeOffsetTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SnapshotByTimeOffsetTemplateSet") is not None:
            self.SnapshotByTimeOffsetTemplateSet = []
            for item in params.get("SnapshotByTimeOffsetTemplateSet"):
                obj = SnapshotByTimeOffsetTemplate()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 视频处理任务的任务 ID。
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TaskType: 任务类型，目前仅有取值 WorkflowTask。
        :type TaskType: str
        :param Status: 任务状态，取值：
<li>WAITING：等待中；</li>
<li>PROCESSING：处理中；</li>
<li>FINISH：已完成。</li>
        :type Status: str
        :param CreateTime: 任务的创建时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param BeginProcessTime: 任务开始执行的时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type BeginProcessTime: str
        :param FinishTime: 任务执行完毕的时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type FinishTime: str
        :param WorkflowTask: 视频处理任务信息，仅当 TaskType 为 WorkflowTask，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowTask: :class:`tencentcloud.mps.v20190612.models.WorkflowTask`
        :param TaskNotifyConfig: 任务的事件通知信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TasksPriority: 任务流的优先级，取值范围为 [-10, 10]。
        :type TasksPriority: int
        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长50个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长1000个字符。
        :type SessionContext: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskType = None
        self.Status = None
        self.CreateTime = None
        self.BeginProcessTime = None
        self.FinishTime = None
        self.WorkflowTask = None
        self.TaskNotifyConfig = None
        self.TasksPriority = None
        self.SessionId = None
        self.SessionContext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")
        if params.get("WorkflowTask") is not None:
            self.WorkflowTask = WorkflowTask()
            self.WorkflowTask._deserialize(params.get("WorkflowTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TasksPriority = params.get("TasksPriority")
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        """
        :param Status: 过滤条件：任务状态，可选值：WAITING（等待中）、PROCESSING（处理中）、FINISH（已完成）。
        :type Status: str
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        :param ScrollToken: 翻页标识，分批拉取时使用：当单次请求无法拉取所有数据，接口将会返回 ScrollToken，下一次请求携带该 Token，将会从下一条记录开始获取。
        :type ScrollToken: str
        """
        self.Status = None
        self.Limit = None
        self.ScrollToken = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Limit = params.get("Limit")
        self.ScrollToken = params.get("ScrollToken")


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TaskSet: 任务概要列表。
        :type TaskSet: list of TaskSimpleInfo
        :param ScrollToken: 翻页标识，当请求未返回所有数据，该字段表示下一条记录的 ID。当该字段为空字符串，说明已无更多数据。
        :type ScrollToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskSet = None
        self.ScrollToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self.TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskSimpleInfo()
                obj._deserialize(item)
                self.TaskSet.append(obj)
        self.ScrollToken = params.get("ScrollToken")
        self.RequestId = params.get("RequestId")


class DescribeTranscodeTemplatesRequest(AbstractModel):
    """DescribeTranscodeTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 转码模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int
        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param ContainerType: 封装格式过滤条件，可选值：
<li>Video：视频格式，可以同时包含视频流和音频流的封装格式板；</li>
<li>PureAudio：纯音频格式，只能包含音频流的封装格式。</li>
        :type ContainerType: str
        :param TEHDType: 极速高清过滤条件，用于过滤普通转码或极速高清转码模板，可选值：
<li>Common：普通转码模板；</li>
<li>TEHD：极速高清模板。</li>
        :type TEHDType: str
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        """
        self.Definitions = None
        self.Type = None
        self.ContainerType = None
        self.TEHDType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Type = params.get("Type")
        self.ContainerType = params.get("ContainerType")
        self.TEHDType = params.get("TEHDType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTranscodeTemplatesResponse(AbstractModel):
    """DescribeTranscodeTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param TranscodeTemplateSet: 转码模板详情列表。
        :type TranscodeTemplateSet: list of TranscodeTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TranscodeTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TranscodeTemplateSet") is not None:
            self.TranscodeTemplateSet = []
            for item in params.get("TranscodeTemplateSet"):
                obj = TranscodeTemplate()
                obj._deserialize(item)
                self.TranscodeTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserInfoRequest(AbstractModel):
    """DescribeUserInfo请求参数结构体

    """


class DescribeUserInfoResponse(AbstractModel):
    """DescribeUserInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 用户状态，取值：
<li>Normal：正常 ；</li>
<li> Closed：下线；</li>
<li> Arrearage：欠费停服。</li>
        :type Status: str
        :param PaymentType: 用户付费类型，取值：
<li>DailyPayment：日结付费 ；</li>
<li>MonthlyPayment：月结付费。</li>
        :type PaymentType: str
        :param OldMpsUser: 是否是旧版视频处理用户，取值：
<li>0：否 ；</li>
<li>1：是。</li>
        :type OldMpsUser: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.PaymentType = None
        self.OldMpsUser = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.PaymentType = params.get("PaymentType")
        self.OldMpsUser = params.get("OldMpsUser")
        self.RequestId = params.get("RequestId")


class DescribeWatermarkTemplatesRequest(AbstractModel):
    """DescribeWatermarkTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 水印模板唯一标识过滤条件，数组长度限制：100。
        :type Definitions: list of int
        :param Type: 水印类型过滤条件，可选值：
<li>image：图片水印；</li>
<li>text：文字水印。</li>
        :type Type: str
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数
<li>默认值：10；</li>
<li>最大值：100。</li>
        :type Limit: int
        """
        self.Definitions = None
        self.Type = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Type = params.get("Type")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeWatermarkTemplatesResponse(AbstractModel):
    """DescribeWatermarkTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param WatermarkTemplateSet: 水印模板详情列表。
        :type WatermarkTemplateSet: list of WatermarkTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.WatermarkTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WatermarkTemplateSet") is not None:
            self.WatermarkTemplateSet = []
            for item in params.get("WatermarkTemplateSet"):
                obj = WatermarkTemplate()
                obj._deserialize(item)
                self.WatermarkTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWorkflowsRequest(AbstractModel):
    """DescribeWorkflows请求参数结构体

    """

    def __init__(self):
        """
        :param WorkflowIds: 工作流 ID 过滤条件，数组长度限制：100。
        :type WorkflowIds: list of int
        :param Status: 工作流状态，取值范围：
<li>Enabled：已启用，</li>
<li>Disabled：已禁用。</li>
不填此参数，则不区分工作流状态。
        :type Status: str
        :param Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param Limit: 返回记录条数，默认值：10，最大值：100。
        :type Limit: int
        """
        self.WorkflowIds = None
        self.Status = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.WorkflowIds = params.get("WorkflowIds")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeWorkflowsResponse(AbstractModel):
    """DescribeWorkflows返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。
        :type TotalCount: int
        :param WorkflowInfoSet: 工作流信息数组。
        :type WorkflowInfoSet: list of WorkflowInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.WorkflowInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WorkflowInfoSet") is not None:
            self.WorkflowInfoSet = []
            for item in params.get("WorkflowInfoSet"):
                obj = WorkflowInfo()
                obj._deserialize(item)
                self.WorkflowInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DisableWorkflowRequest(AbstractModel):
    """DisableWorkflow请求参数结构体

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        """
        self.WorkflowId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")


class DisableWorkflowResponse(AbstractModel):
    """DisableWorkflow返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableWorkflowRequest(AbstractModel):
    """EnableWorkflow请求参数结构体

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        """
        self.WorkflowId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")


class EnableWorkflowResponse(AbstractModel):
    """EnableWorkflow返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ImageSpriteTaskInput(AbstractModel):
    """对视频截雪碧图任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 雪碧图模板 ID。
        :type Definition: int
        :param OutputStorage: 截取雪碧图后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 截取雪碧图后，雪碧图图片文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_imageSprite_{definition}_{number}.{format}`。
        :type OutputObjectPath: str
        :param WebVttObjectName: 截取雪碧图后，Web VTT 文件的输出路径，只能为相对路径。如果不填，则默认为相对路径：`{inputName}_imageSprite_{definition}.{format}`。
        :type WebVttObjectName: str
        :param ObjectNumberFormat: 截取雪碧图后输出路径中的`{number}`变量的规则。
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectNumberFormat: :class:`tencentcloud.mps.v20190612.models.NumberFormat`
        """
        self.Definition = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.WebVttObjectName = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        self.WebVttObjectName = params.get("WebVttObjectName")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))


class ImageSpriteTemplate(AbstractModel):
    """雪碧图模板详情

    """

    def __init__(self):
        """
        :param Definition: 雪碧图模板唯一标识。
        :type Definition: int
        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param Name: 雪碧图模板名称。
        :type Name: str
        :param Width: 雪碧图中小图的宽度。
        :type Width: int
        :param Height: 雪碧图中小图的高度。
        :type Height: int
        :param SampleType: 采样类型。
        :type SampleType: str
        :param SampleInterval: 采样间隔。
        :type SampleInterval: int
        :param RowCount: 雪碧图中小图的行数。
        :type RowCount: int
        :param ColumnCount: 雪碧图中小图的列数。
        :type ColumnCount: int
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class ImageWatermarkInput(AbstractModel):
    """图片水印模板输入参数

    """

    def __init__(self):
        """
        :param ImageContent: 水印图片 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串。支持 jpeg、png 图片格式。
        :type ImageContent: str
        :param Width: 水印的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>
默认值：10%。
        :type Width: str
        :param Height: 水印的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>
默认值：0px，表示 Height 按照原始水印图片的宽高比缩放。
        :type Height: str
        """
        self.ImageContent = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.ImageContent = params.get("ImageContent")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class ImageWatermarkInputForUpdate(AbstractModel):
    """图片水印模板输入参数

    """

    def __init__(self):
        """
        :param ImageContent: 水印图片 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串。支持 jpeg、png 图片格式。
        :type ImageContent: str
        :param Width: 水印的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>
        :type Width: str
        :param Height: 水印的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>
0px 表示 Height 按照 Width 对视频宽度的比例缩放。
        :type Height: str
        """
        self.ImageContent = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.ImageContent = params.get("ImageContent")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class ImageWatermarkTemplate(AbstractModel):
    """图片水印模板

    """

    def __init__(self):
        """
        :param ImageUrl: 水印图片地址。
        :type ImageUrl: str
        :param Width: 水印的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>
        :type Width: str
        :param Height: 水印的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素；</li>
0px：表示 Height 按照 Width 对视频宽度的比例缩放。
        :type Height: str
        """
        self.ImageUrl = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class MediaAnimatedGraphicsItem(AbstractModel):
    """视频转动图结果信息

    """

    def __init__(self):
        """
        :param Storage: 转动图文件的存储位置。
        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param Path: 转动图的文件路径。
        :type Path: str
        :param Definition: 转动图模板 ID，参见[转动图参数模板](https://cloud.tencent.com/document/product/266/33481#.E8.BD.AC.E5.8A.A8.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param Container: 动图格式，如 gif。
        :type Container: str
        :param Height: 动图的高度，单位：px。
        :type Height: int
        :param Width: 动图的宽度，单位：px。
        :type Width: int
        :param Bitrate: 动图码率，单位：bps。
        :type Bitrate: int
        :param Size: 动图大小，单位：字节。
        :type Size: int
        :param Md5: 动图的md5值。
        :type Md5: str
        :param StartTimeOffset: 动图在视频中的起始时间偏移，单位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 动图在视频中的结束时间偏移，单位：秒。
        :type EndTimeOffset: float
        """
        self.Storage = None
        self.Path = None
        self.Definition = None
        self.Container = None
        self.Height = None
        self.Width = None
        self.Bitrate = None
        self.Size = None
        self.Md5 = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        self.Path = params.get("Path")
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Bitrate = params.get("Bitrate")
        self.Size = params.get("Size")
        self.Md5 = params.get("Md5")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class MediaAudioStreamItem(AbstractModel):
    """点播文件音频流信息

    """

    def __init__(self):
        """
        :param Bitrate: 音频流的码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param SamplingRate: 音频流的采样率，单位：hz。
注意：此字段可能返回 null，表示取不到有效值。
        :type SamplingRate: int
        :param Codec: 音频流的编码格式，例如 aac。
注意：此字段可能返回 null，表示取不到有效值。
        :type Codec: str
        """
        self.Bitrate = None
        self.SamplingRate = None
        self.Codec = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.SamplingRate = params.get("SamplingRate")
        self.Codec = params.get("Codec")


class MediaImageSpriteItem(AbstractModel):
    """雪碧图信息

    """

    def __init__(self):
        """
        :param Definition: 雪碧图规格，参见[雪碧图参数模板](https://cloud.tencent.com/document/product/266/33480#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param Height: 雪碧图小图的高度。
        :type Height: int
        :param Width: 雪碧图小图的宽度。
        :type Width: int
        :param TotalCount: 每一张雪碧图大图里小图的数量。
        :type TotalCount: int
        :param ImagePathSet: 每一张雪碧图大图的路径。
        :type ImagePathSet: list of str
        :param WebVttPath: 雪碧图子图位置与时间关系的 WebVtt 文件路径。WebVtt 文件表明了各个雪碧图小图对应的时间点，以及在在雪碧大图里的坐标位置，一般被播放器用于实现预览。
        :type WebVttPath: str
        :param Storage: 雪碧图文件的存储位置。
        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        """
        self.Definition = None
        self.Height = None
        self.Width = None
        self.TotalCount = None
        self.ImagePathSet = None
        self.WebVttPath = None
        self.Storage = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.TotalCount = params.get("TotalCount")
        self.ImagePathSet = params.get("ImagePathSet")
        self.WebVttPath = params.get("WebVttPath")
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))


class MediaInputInfo(AbstractModel):
    """视频处理输入对象信息。

    """

    def __init__(self):
        """
        :param Type: 视频处理对象的类型，现在仅支持 COS。
        :type Type: str
        :param CosInputInfo: 当 Type 为 COS 时有效，则该项为必填，表示视频处理 COS 对象信息。
        :type CosInputInfo: :class:`tencentcloud.mps.v20190612.models.CosInputInfo`
        """
        self.Type = None
        self.CosInputInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosInputInfo") is not None:
            self.CosInputInfo = CosInputInfo()
            self.CosInputInfo._deserialize(params.get("CosInputInfo"))


class MediaMetaData(AbstractModel):
    """点播媒体文件元信息

    """

    def __init__(self):
        """
        :param Size: 上传的媒体文件大小（视频为 HLS 时，大小是 m3u8 和 ts 文件大小的总和），单位：字节。
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param Container: 容器类型，例如 m4a，mp4 等。
注意：此字段可能返回 null，表示取不到有效值。
        :type Container: str
        :param Bitrate: 视频流码率平均值与音频流码率平均值之和，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param Height: 视频流高度的最大值，单位：px。
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param Width: 视频流宽度的最大值，单位：px。
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param Duration: 视频时长，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: float
        :param Rotate: 视频拍摄时的选择角度，单位：度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Rotate: int
        :param VideoStreamSet: 视频流信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoStreamSet: list of MediaVideoStreamItem
        :param AudioStreamSet: 音频流信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioStreamSet: list of MediaAudioStreamItem
        :param VideoDuration: 视频时长，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoDuration: float
        :param AudioDuration: 音频时长，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioDuration: float
        """
        self.Size = None
        self.Container = None
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Duration = None
        self.Rotate = None
        self.VideoStreamSet = None
        self.AudioStreamSet = None
        self.VideoDuration = None
        self.AudioDuration = None


    def _deserialize(self, params):
        self.Size = params.get("Size")
        self.Container = params.get("Container")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Duration = params.get("Duration")
        self.Rotate = params.get("Rotate")
        if params.get("VideoStreamSet") is not None:
            self.VideoStreamSet = []
            for item in params.get("VideoStreamSet"):
                obj = MediaVideoStreamItem()
                obj._deserialize(item)
                self.VideoStreamSet.append(obj)
        if params.get("AudioStreamSet") is not None:
            self.AudioStreamSet = []
            for item in params.get("AudioStreamSet"):
                obj = MediaAudioStreamItem()
                obj._deserialize(item)
                self.AudioStreamSet.append(obj)
        self.VideoDuration = params.get("VideoDuration")
        self.AudioDuration = params.get("AudioDuration")


class MediaProcessTaskAnimatedGraphicResult(AbstractModel):
    """转动图任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败：
<li>40000：输入参数不合法，请检查输入参数；</li>
<li>60000：源文件错误（如视频数据损坏），请确认源文件是否正常；</li>
<li>70000：内部服务错误，建议重试。</li>
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 转动图任务的输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.AnimatedGraphicTaskInput`
        :param Output: 转动图任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaAnimatedGraphicsItem`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AnimatedGraphicTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaAnimatedGraphicsItem()
            self.Output._deserialize(params.get("Output"))


class MediaProcessTaskImageSpriteResult(AbstractModel):
    """对视频截雪碧图任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败：
<li>40000：输入参数不合法，请检查输入参数；</li>
<li>60000：源文件错误（如视频数据损坏），请确认源文件是否正常；</li>
<li>70000：内部服务错误，建议重试。</li>
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 对视频截雪碧图任务的输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.ImageSpriteTaskInput`
        :param Output: 对视频截雪碧图任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaImageSpriteItem`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = ImageSpriteTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaImageSpriteItem()
            self.Output._deserialize(params.get("Output"))


class MediaProcessTaskInput(AbstractModel):
    """视频处理任务类型

    """

    def __init__(self):
        """
        :param TranscodeTaskSet: 视频转码任务列表。
        :type TranscodeTaskSet: list of TranscodeTaskInput
        :param AnimatedGraphicTaskSet: 视频转动图任务列表。
        :type AnimatedGraphicTaskSet: list of AnimatedGraphicTaskInput
        :param SnapshotByTimeOffsetTaskSet: 对视频按时间点截图任务列表。
        :type SnapshotByTimeOffsetTaskSet: list of SnapshotByTimeOffsetTaskInput
        :param SampleSnapshotTaskSet: 对视频采样截图任务列表。
        :type SampleSnapshotTaskSet: list of SampleSnapshotTaskInput
        :param ImageSpriteTaskSet: 对视频截雪碧图任务列表。
        :type ImageSpriteTaskSet: list of ImageSpriteTaskInput
        :param AdaptiveDynamicStreamingTaskSet: 对视频转自适应码流任务列表。
        :type AdaptiveDynamicStreamingTaskSet: list of AdaptiveDynamicStreamingTaskInput
        """
        self.TranscodeTaskSet = None
        self.AnimatedGraphicTaskSet = None
        self.SnapshotByTimeOffsetTaskSet = None
        self.SampleSnapshotTaskSet = None
        self.ImageSpriteTaskSet = None
        self.AdaptiveDynamicStreamingTaskSet = None


    def _deserialize(self, params):
        if params.get("TranscodeTaskSet") is not None:
            self.TranscodeTaskSet = []
            for item in params.get("TranscodeTaskSet"):
                obj = TranscodeTaskInput()
                obj._deserialize(item)
                self.TranscodeTaskSet.append(obj)
        if params.get("AnimatedGraphicTaskSet") is not None:
            self.AnimatedGraphicTaskSet = []
            for item in params.get("AnimatedGraphicTaskSet"):
                obj = AnimatedGraphicTaskInput()
                obj._deserialize(item)
                self.AnimatedGraphicTaskSet.append(obj)
        if params.get("SnapshotByTimeOffsetTaskSet") is not None:
            self.SnapshotByTimeOffsetTaskSet = []
            for item in params.get("SnapshotByTimeOffsetTaskSet"):
                obj = SnapshotByTimeOffsetTaskInput()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetTaskSet.append(obj)
        if params.get("SampleSnapshotTaskSet") is not None:
            self.SampleSnapshotTaskSet = []
            for item in params.get("SampleSnapshotTaskSet"):
                obj = SampleSnapshotTaskInput()
                obj._deserialize(item)
                self.SampleSnapshotTaskSet.append(obj)
        if params.get("ImageSpriteTaskSet") is not None:
            self.ImageSpriteTaskSet = []
            for item in params.get("ImageSpriteTaskSet"):
                obj = ImageSpriteTaskInput()
                obj._deserialize(item)
                self.ImageSpriteTaskSet.append(obj)
        if params.get("AdaptiveDynamicStreamingTaskSet") is not None:
            self.AdaptiveDynamicStreamingTaskSet = []
            for item in params.get("AdaptiveDynamicStreamingTaskSet"):
                obj = AdaptiveDynamicStreamingTaskInput()
                obj._deserialize(item)
                self.AdaptiveDynamicStreamingTaskSet.append(obj)


class MediaProcessTaskResult(AbstractModel):
    """任务查询结果类型

    """

    def __init__(self):
        """
        :param Type: 任务的类型，可以取的值有：
<li>Transcode：转码</li>
<li>AnimatedGraphics：转动图</li>
<li>SnapshotByTimeOffset：时间点截图</li>
<li>SampleSnapshot：采样截图</li>
<li>ImageSprites：雪碧图</li>
<li>CoverBySnapshot：截图做封面</li>
<li>AdaptiveDynamicStreaming：自适应码流</li>
        :type Type: str
        :param TranscodeTask: 视频转码任务的查询结果，当任务类型为 Transcode 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskTranscodeResult`
        :param AnimatedGraphicTask: 视频转动图任务的查询结果，当任务类型为 AnimatedGraphics 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AnimatedGraphicTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskAnimatedGraphicResult`
        :param SnapshotByTimeOffsetTask: 对视频按时间点截图任务的查询结果，当任务类型为 SnapshotByTimeOffset 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskSnapshotByTimeOffsetResult`
        :param SampleSnapshotTask: 对视频采样截图任务的查询结果，当任务类型为 SampleSnapshot 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleSnapshotTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskSampleSnapshotResult`
        :param ImageSpriteTask: 对视频截雪碧图任务的查询结果，当任务类型为 ImageSprite 时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageSpriteTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskImageSpriteResult`
        """
        self.Type = None
        self.TranscodeTask = None
        self.AnimatedGraphicTask = None
        self.SnapshotByTimeOffsetTask = None
        self.SampleSnapshotTask = None
        self.ImageSpriteTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("TranscodeTask") is not None:
            self.TranscodeTask = MediaProcessTaskTranscodeResult()
            self.TranscodeTask._deserialize(params.get("TranscodeTask"))
        if params.get("AnimatedGraphicTask") is not None:
            self.AnimatedGraphicTask = MediaProcessTaskAnimatedGraphicResult()
            self.AnimatedGraphicTask._deserialize(params.get("AnimatedGraphicTask"))
        if params.get("SnapshotByTimeOffsetTask") is not None:
            self.SnapshotByTimeOffsetTask = MediaProcessTaskSnapshotByTimeOffsetResult()
            self.SnapshotByTimeOffsetTask._deserialize(params.get("SnapshotByTimeOffsetTask"))
        if params.get("SampleSnapshotTask") is not None:
            self.SampleSnapshotTask = MediaProcessTaskSampleSnapshotResult()
            self.SampleSnapshotTask._deserialize(params.get("SampleSnapshotTask"))
        if params.get("ImageSpriteTask") is not None:
            self.ImageSpriteTask = MediaProcessTaskImageSpriteResult()
            self.ImageSpriteTask._deserialize(params.get("ImageSpriteTask"))


class MediaProcessTaskSampleSnapshotResult(AbstractModel):
    """对视频做采样截图任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败：
<li>40000：输入参数不合法，请检查输入参数；</li>
<li>60000：源文件错误（如视频数据损坏），请确认源文件是否正常；</li>
<li>70000：内部服务错误，建议重试。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 对视频做采样截图任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.SampleSnapshotTaskInput`
        :param Output: 对视频做采样截图任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaSampleSnapshotItem`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = SampleSnapshotTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaSampleSnapshotItem()
            self.Output._deserialize(params.get("Output"))


class MediaProcessTaskSnapshotByTimeOffsetResult(AbstractModel):
    """对视频按指定时间点截图任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败：
<li>40000：输入参数不合法，请检查输入参数；</li>
<li>60000：源文件错误（如视频数据损坏），请确认源文件是否正常；</li>
<li>70000：内部服务错误，建议重试。</li>
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 对视频按指定时间点截图任务输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.SnapshotByTimeOffsetTaskInput`
        :param Output: 对视频按指定时间点截图任务输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaSnapshotByTimeOffsetItem`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = SnapshotByTimeOffsetTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaSnapshotByTimeOffsetItem()
            self.Output._deserialize(params.get("Output"))


class MediaProcessTaskTranscodeResult(AbstractModel):
    """转码任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
        :type Status: str
        :param ErrCode: 错误码，0 表示成功，其他值表示失败：
<li>40000：输入参数不合法，请检查输入参数；</li>
<li>60000：源文件错误（如视频数据损坏），请确认源文件是否正常；</li>
<li>70000：内部服务错误，建议重试。</li>
        :type ErrCode: int
        :param Message: 错误信息。
        :type Message: str
        :param Input: 转码任务的输入。
        :type Input: :class:`tencentcloud.mps.v20190612.models.TranscodeTaskInput`
        :param Output: 转码任务的输出。
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaTranscodeItem`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = TranscodeTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaTranscodeItem()
            self.Output._deserialize(params.get("Output"))


class MediaSampleSnapshotItem(AbstractModel):
    """采样截图信息

    """

    def __init__(self):
        """
        :param Definition: 采样截图规格 ID，参见[采样截图参数模板](https://cloud.tencent.com/document/product/266/33480#.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param SampleType: 采样方式，取值范围：
<li>Percent：根据百分比间隔采样。</li>
<li>Time：根据时间间隔采样。</li>
        :type SampleType: str
        :param Interval: 采样间隔
<li>当 SampleType 为 Percent 时，该值表示多少百分比一张图。</li>
<li>当 SampleType 为 Time 时，该值表示多少时间间隔一张图，单位秒， 第一张图均为视频首帧。</li>
        :type Interval: int
        :param Storage: 截图后文件的存储位置。
        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param ImagePathSet: 生成的截图 path 列表。
        :type ImagePathSet: list of str
        :param WaterMarkDefinition: 截图如果被打上了水印，被打水印的模板 ID 列表。
        :type WaterMarkDefinition: list of int
        """
        self.Definition = None
        self.SampleType = None
        self.Interval = None
        self.Storage = None
        self.ImagePathSet = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SampleType = params.get("SampleType")
        self.Interval = params.get("Interval")
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        self.ImagePathSet = params.get("ImagePathSet")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")


class MediaSnapshotByTimeOffsetItem(AbstractModel):
    """点播文件指定时间点截图信息

    """

    def __init__(self):
        """
        :param Definition: 指定时间点截图规格，参见[指定时间点截图参数模板](https://cloud.tencent.com/document/product/266/33480#.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param PicInfoSet: 同一规格的截图信息集合，每个元素代表一张截图。
        :type PicInfoSet: list of MediaSnapshotByTimePicInfoItem
        :param Storage: 指定时间点截图文件的存储位置。
        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        """
        self.Definition = None
        self.PicInfoSet = None
        self.Storage = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("PicInfoSet") is not None:
            self.PicInfoSet = []
            for item in params.get("PicInfoSet"):
                obj = MediaSnapshotByTimePicInfoItem()
                obj._deserialize(item)
                self.PicInfoSet.append(obj)
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))


class MediaSnapshotByTimePicInfoItem(AbstractModel):
    """指定时间点截图信息

    """

    def __init__(self):
        """
        :param TimeOffset: 该张截图对应视频文件中的时间偏移，单位为<font color=red>毫秒</font>。
        :type TimeOffset: float
        :param Path: 该张截图的路径。
        :type Path: str
        :param WaterMarkDefinition: 截图如果被打上了水印，被打水印的模板 ID 列表。
        :type WaterMarkDefinition: list of int
        """
        self.TimeOffset = None
        self.Path = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.TimeOffset = params.get("TimeOffset")
        self.Path = params.get("Path")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")


class MediaTranscodeItem(AbstractModel):
    """转码信息

    """

    def __init__(self):
        """
        :param OutputStorage: 转码后文件的目标存储。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param Path: 转码后的视频文件路径。
        :type Path: str
        :param Definition: 转码规格 ID，参见[转码参数模板](https://cloud.tencent.com/document/product/266/33478#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param Bitrate: 视频流码率平均值与音频流码率平均值之和， 单位：bps。
        :type Bitrate: int
        :param Height: 视频流高度的最大值，单位：px。
        :type Height: int
        :param Width: 视频流宽度的最大值，单位：px。
        :type Width: int
        :param Size: 媒体文件总大小（视频为 HLS 时，大小是 m3u8 和 ts 文件大小的总和），单位：字节。
        :type Size: int
        :param Duration: 视频时长，单位：秒。
        :type Duration: float
        :param Container: 容器类型，例如 m4a，mp4 等。
        :type Container: str
        :param Md5: 视频的 md5 值。
        :type Md5: str
        :param AudioStreamSet: 音频流信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioStreamSet: list of MediaAudioStreamItem
        :param VideoStreamSet: 视频流信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoStreamSet: list of MediaVideoStreamItem
        """
        self.OutputStorage = None
        self.Path = None
        self.Definition = None
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Size = None
        self.Duration = None
        self.Container = None
        self.Md5 = None
        self.AudioStreamSet = None
        self.VideoStreamSet = None


    def _deserialize(self, params):
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.Path = params.get("Path")
        self.Definition = params.get("Definition")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Size = params.get("Size")
        self.Duration = params.get("Duration")
        self.Container = params.get("Container")
        self.Md5 = params.get("Md5")
        if params.get("AudioStreamSet") is not None:
            self.AudioStreamSet = []
            for item in params.get("AudioStreamSet"):
                obj = MediaAudioStreamItem()
                obj._deserialize(item)
                self.AudioStreamSet.append(obj)
        if params.get("VideoStreamSet") is not None:
            self.VideoStreamSet = []
            for item in params.get("VideoStreamSet"):
                obj = MediaVideoStreamItem()
                obj._deserialize(item)
                self.VideoStreamSet.append(obj)


class MediaVideoStreamItem(AbstractModel):
    """点播文件视频流信息

    """

    def __init__(self):
        """
        :param Bitrate: 视频流的码率，单位：bps。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param Height: 视频流的高度，单位：px。
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param Width: 视频流的宽度，单位：px。
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param Codec: 视频流的编码格式，例如 h264。
注意：此字段可能返回 null，表示取不到有效值。
        :type Codec: str
        :param Fps: 帧率，单位：hz。
注意：此字段可能返回 null，表示取不到有效值。
        :type Fps: int
        """
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Codec = None
        self.Fps = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")


class ModifyAnimatedGraphicsTemplateRequest(AbstractModel):
    """ModifyAnimatedGraphicsTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转动图模板唯一标识。
        :type Definition: int
        :param Name: 转动图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Width: 动图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 视频流高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param Format: 动图格式，取值为 gif 和 webp。
        :type Format: str
        :param Fps: 帧率，取值范围：[1, 30]，单位：Hz。
        :type Fps: int
        :param Quality: 图片质量，取值范围：[1, 100]，默认值为 75。
        :type Quality: float
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.Format = None
        self.Fps = None
        self.Quality = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Format = params.get("Format")
        self.Fps = params.get("Fps")
        self.Quality = params.get("Quality")
        self.Comment = params.get("Comment")


class ModifyAnimatedGraphicsTemplateResponse(AbstractModel):
    """ModifyAnimatedGraphicsTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImageSpriteTemplateRequest(AbstractModel):
    """ModifyImageSpriteTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 雪碧图模板唯一标识。
        :type Definition: int
        :param Name: 雪碧图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Width: 雪碧图中小图的宽度，取值范围： [128, 4096]，单位：px。
        :type Width: int
        :param Height: 雪碧图中小图的高度，取值范围： [128, 4096]，单位：px。
        :type Height: int
        :param SampleType: 采样类型，取值：
<li>Percent：按百分比。</li>
<li>Time：按时间间隔。</li>
        :type SampleType: str
        :param SampleInterval: 采样间隔。
<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>
<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>
        :type SampleInterval: int
        :param RowCount: 雪碧图中小图的行数。
        :type RowCount: int
        :param ColumnCount: 雪碧图中小图的列数。
        :type ColumnCount: int
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")


class ModifyImageSpriteTemplateResponse(AbstractModel):
    """ModifyImageSpriteTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySampleSnapshotTemplateRequest(AbstractModel):
    """ModifySampleSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 采样截图模板唯一标识。
        :type Definition: int
        :param Name: 采样截图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Width: 图片宽度，取值范围： [128, 4096]，单位：px。
        :type Width: int
        :param Height: 图片高度，取值范围： [128, 4096]，单位：px。
        :type Height: int
        :param SampleType: 采样截图类型，取值：
<li>Percent：按百分比。</li>
<li>Time：按时间间隔。</li>
        :type SampleType: str
        :param SampleInterval: 采样间隔。
<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>
<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>
        :type SampleInterval: int
        :param Format: 图片格式，取值为 jpg 和 png。
        :type Format: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.SampleType = None
        self.SampleInterval = None
        self.Format = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")


class ModifySampleSnapshotTemplateResponse(AbstractModel):
    """ModifySampleSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """ModifySnapshotByTimeOffsetTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 指定时间点截图模板唯一标识。
        :type Definition: int
        :param Name: 指定时间点截图模板名称，长度限制：64 个字符。
        :type Name: str
        :param Width: 图片宽度，取值范围： [128, 4096]，单位：px。
        :type Width: int
        :param Height: 图片高度，取值范围： [128, 4096]，单位：px。
        :type Height: int
        :param Format: 图片格式，取值可以为 jpg 和 png。
        :type Format: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.Format = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")


class ModifySnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """ModifySnapshotByTimeOffsetTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTranscodeTemplateRequest(AbstractModel):
    """ModifyTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转码模板唯一标识。
        :type Definition: int
        :param Container: 封装格式，可选值：mp4、flv、hls、mp3、flac、ogg、m4a。其中，mp3、flac、ogg、m4a 为纯音频文件。
        :type Container: str
        :param Name: 转码模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字节。
        :type Comment: str
        :param RemoveVideo: 是否去除视频数据，可选值：
<li>0：保留</li>
<li>1：去除</li>
        :type RemoveVideo: int
        :param RemoveAudio: 是否去除音频数据，可选值：
<li>0：保留</li>
<li>1：去除</li>
        :type RemoveAudio: int
        :param VideoTemplate: 视频流配置参数。
        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfoForUpdate`
        :param AudioTemplate: 音频流配置参数。
        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfoForUpdate`
        :param TEHDConfig: 极速高清转码参数，需联系商务架构师开通后才能使用。
        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfigForUpdate`
        """
        self.Definition = None
        self.Container = None
        self.Name = None
        self.Comment = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfoForUpdate()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfoForUpdate()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfigForUpdate()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))


class ModifyTranscodeTemplateResponse(AbstractModel):
    """ModifyTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWatermarkTemplateRequest(AbstractModel):
    """ModifyWatermarkTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 水印模板唯一标识。
        :type Definition: int
        :param Name: 水印模板名称，长度限制：64 个字符。
        :type Name: str
        :param Comment: 模板描述信息，长度限制：256 个字符。
        :type Comment: str
        :param CoordinateOrigin: 原点位置，可选值：
<li>TopLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角；</li>
<li>TopRight：表示坐标原点位于视频图像的右上角，水印原点为图片或文字的右上角；</li>
<li>BottomLeft：表示坐标原点位于视频图像的左下角，水印原点为图片或文字的左下角；</li>
<li>BottomRight：表示坐标原点位于视频图像的右下角，水印原点为图片或文字的右下角。</li>
目前，当 Type 为 image，该字段仅支持 TopLeft。
        :type CoordinateOrigin: str
        :param XPos: 水印原点距离视频图像坐标原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 XPos 为视频宽度指定百分比，如 10% 表示 XPos 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 XPos 为指定像素，如 100px 表示 XPos 为 100 像素。</li>
        :type XPos: str
        :param YPos: 水印原点距离视频图像坐标原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 YPos 为视频高度指定百分比，如 10% 表示 YPos 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 YPos 为指定像素，如 100px 表示 YPos 为 100 像素。</li>
        :type YPos: str
        :param ImageTemplate: 图片水印模板，该字段仅对图片水印模板有效。
        :type ImageTemplate: :class:`tencentcloud.mps.v20190612.models.ImageWatermarkInputForUpdate`
        :param TextTemplate: 文字水印模板，该字段仅对文字水印模板有效。
        :type TextTemplate: :class:`tencentcloud.mps.v20190612.models.TextWatermarkTemplateInputForUpdate`
        :param SvgTemplate: SVG水印模板，当 Type 为 svg，该字段必填。当 Type 为 image 或 text，该字段无效。
        :type SvgTemplate: :class:`tencentcloud.mps.v20190612.models.SvgWatermarkInputForUpdate`
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkInputForUpdate()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInputForUpdate()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInputForUpdate()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))


class ModifyWatermarkTemplateResponse(AbstractModel):
    """ModifyWatermarkTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param ImageUrl: 图片水印地址，仅当 ImageTemplate.ImageContent 非空，该字段有效。
        :type ImageUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.RequestId = params.get("RequestId")


class NumberFormat(AbstractModel):
    """输出文件名的`{number}`变量的规则。

    """

    def __init__(self):
        """
        :param InitialValue: `{number}`变量的起始值，默认为0。
        :type InitialValue: int
        :param Increment: `{number}`变量的增长步长，默认为1。
        :type Increment: int
        :param MinLength: `{number}`变量的最小长度，不足时补占位符。默认为1。
        :type MinLength: int
        :param PlaceHolder: `{number}`变量的长度不足时，补充的占位符。默认为"0"。
        :type PlaceHolder: str
        """
        self.InitialValue = None
        self.Increment = None
        self.MinLength = None
        self.PlaceHolder = None


    def _deserialize(self, params):
        self.InitialValue = params.get("InitialValue")
        self.Increment = params.get("Increment")
        self.MinLength = params.get("MinLength")
        self.PlaceHolder = params.get("PlaceHolder")


class ProcessLiveMediaRequest(AbstractModel):
    """ProcessLiveMedia请求参数结构体

    """

    def __init__(self):
        """
        :param Url: 直播流 URL。
        :type Url: str
        :param OutputStorage: 直播流处理输出文件的目标存储。如处理有文件输出，该参数为必填项。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputDir: 直播流处理生成的文件输出的目标目录，如`/movie/201909/`，如果不填为 `/` 目录。
        :type OutputDir: str
        :param AiRecognitionTask: 直播流内容识别类型任务参数。
        :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param AiAnalysisTask: 直播流内容分析类型任务参数。
        :type AiAnalysisTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskInput`
        :param TaskNotifyConfig: 任务的事件通知信息，不填代表不获取事件通知。
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。
        :type SessionContext: str
        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param StartTime: 直播开始时间戳（UTC 时间 单位为秒，该参数仅对于直播流分析有效）。
        :type StartTime: int
        """
        self.Url = None
        self.OutputStorage = None
        self.OutputDir = None
        self.AiRecognitionTask = None
        self.AiAnalysisTask = None
        self.TaskNotifyConfig = None
        self.SessionContext = None
        self.SessionId = None
        self.StartTime = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.StartTime = params.get("StartTime")


class ProcessLiveMediaResponse(AbstractModel):
    """ProcessLiveMedia返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ProcessMediaRequest(AbstractModel):
    """ProcessMedia请求参数结构体

    """

    def __init__(self):
        """
        :param InputInfo: 视频处理的文件输入信息。
        :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`
        :param OutputStorage: 视频处理输出文件的目标存储。不填则继承 InputInfo 中的存储位置。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputDir: 视频处理生成的文件输出的目标目录，如`/movie/201907/`。如果不填，表示与 InputInfo 中文件所在的目录一致。
        :type OutputDir: str
        :param MediaProcessTask: 视频处理类型任务参数。
        :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`
        :param TaskNotifyConfig: 任务的事件通知信息，不填代表不获取事件通知。
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TasksPriority: 任务流的优先级，数值越大优先级越高，取值范围是-10到 10，不填代表0。
        :type TasksPriority: int
        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
        :type SessionId: str
        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。
        :type SessionContext: str
        """
        self.InputInfo = None
        self.OutputStorage = None
        self.OutputDir = None
        self.MediaProcessTask = None
        self.TaskNotifyConfig = None
        self.TasksPriority = None
        self.SessionId = None
        self.SessionContext = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TasksPriority = params.get("TasksPriority")
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")


class ProcessMediaResponse(AbstractModel):
    """ProcessMedia返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ResetWorkflowRequest(AbstractModel):
    """ResetWorkflow请求参数结构体

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        :param WorkflowName: 工作流名称，最多128字符。同一个用户该名称唯一。
        :type WorkflowName: str
        :param Trigger: 工作流绑定的触发规则，当上传视频命中该规则到该对象时即触发工作流。
        :type Trigger: :class:`tencentcloud.mps.v20190612.models.WorkflowTrigger`
        :param OutputStorage: 视频处理的文件输出配置。不填则继承 Trigger 中的存储位置。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputDir: 视频处理生成的文件输出的目标目录，如`/movie/201907/`。如果不填，表示与触发文件所在的目录一致，即`{inputDir}`。
        :type OutputDir: str
        :param MediaProcessTask: 视频处理类型任务参数。
        :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`
        :param TaskPriority: 工作流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。
        :type TaskPriority: int
        :param TaskNotifyConfig: 任务的事件通知信息，不填代表不获取事件通知。
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        """
        self.WorkflowId = None
        self.WorkflowName = None
        self.Trigger = None
        self.OutputStorage = None
        self.OutputDir = None
        self.MediaProcessTask = None
        self.TaskPriority = None
        self.TaskNotifyConfig = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        self.WorkflowName = params.get("WorkflowName")
        if params.get("Trigger") is not None:
            self.Trigger = WorkflowTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        self.TaskPriority = params.get("TaskPriority")
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))


class ResetWorkflowResponse(AbstractModel):
    """ResetWorkflow返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SampleSnapshotTaskInput(AbstractModel):
    """对视频做采样截图任务输入参数类型。

    """

    def __init__(self):
        """
        :param Definition: 采样截图模板 ID。
        :type Definition: int
        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。
注意：此字段可能返回 null，表示取不到有效值。
        :type WatermarkSet: list of WatermarkInput
        :param OutputStorage: 采样截图后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 采样截图后图片文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_sampleSnapshot_{definition}_{number}.{format}`。
        :type OutputObjectPath: str
        :param ObjectNumberFormat: 采样截图后输出路径中的`{number}`变量的规则。
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectNumberFormat: :class:`tencentcloud.mps.v20190612.models.NumberFormat`
        """
        self.Definition = None
        self.WatermarkSet = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))


class SampleSnapshotTemplate(AbstractModel):
    """采样截图模板详情

    """

    def __init__(self):
        """
        :param Definition: 采样截图模板唯一标识。
        :type Definition: int
        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param Name: 采样截图模板名称。
        :type Name: str
        :param Comment: 模板描述信息。
        :type Comment: str
        :param Width: 图片宽度。
        :type Width: int
        :param Height: 图片高度。
        :type Height: int
        :param Format: 图片格式。
        :type Format: str
        :param SampleType: 采样截图类型。
        :type SampleType: str
        :param SampleInterval: 采样间隔。
        :type SampleInterval: int
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.Format = None
        self.SampleType = None
        self.SampleInterval = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Format = params.get("Format")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class SnapshotByTimeOffsetTaskInput(AbstractModel):
    """对视频按指定时间点截图任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 指定时间点截图模板 ID。
        :type Definition: int
        :param TimeOffsetSet: 截图时间点列表，单位为<font color=red>毫秒</font>。
        :type TimeOffsetSet: list of float
        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。
注意：此字段可能返回 null，表示取不到有效值。
        :type WatermarkSet: list of WatermarkInput
        :param OutputStorage: 时间点截图后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 时间点截图后图片文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_snapshotByTimeOffset_{definition}_{number}.{format}`。
        :type OutputObjectPath: str
        :param ObjectNumberFormat: 时间点截图后输出路径中的`{number}`变量的规则。
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectNumberFormat: :class:`tencentcloud.mps.v20190612.models.NumberFormat`
        """
        self.Definition = None
        self.TimeOffsetSet = None
        self.WatermarkSet = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.TimeOffsetSet = params.get("TimeOffsetSet")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))


class SnapshotByTimeOffsetTemplate(AbstractModel):
    """时间点截图模板详情

    """

    def __init__(self):
        """
        :param Definition: 时间点截图模板唯一标识。
        :type Definition: int
        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param Name: 时间点截图模板名称。
        :type Name: str
        :param Comment: 模板描述信息。
        :type Comment: str
        :param Width: 图片宽度。
        :type Width: int
        :param Height: 图片高度。
        :type Height: int
        :param Format: 图片格式。
        :type Format: str
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.Format = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Format = params.get("Format")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class SvgWatermarkInput(AbstractModel):
    """SVG水印模板输入参数

    """

    def __init__(self):
        """
        :param Width: 水印的宽度，支持 px，%，W%，H%，S%，L% 六种格式：
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素；当填 0px 且
 Height 不为 0px 时，表示水印的宽度按原始 SVG 图像等比缩放；当 Width、Height 都填 0px 时，表示水印的宽度取原始 SVG 图像的宽度；</li>
<li>当字符串以 W% 结尾，表示水印 Width 为视频宽度的百分比大小，如 10W% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 H% 结尾，表示水印 Width 为视频高度的百分比大小，如 10H% 表示 Width 为视频高度的 10%；</li>
<li>当字符串以 S% 结尾，表示水印 Width 为视频短边的百分比大小，如 10S% 表示 Width 为视频短边的 10%；</li>
<li>当字符串以 L% 结尾，表示水印 Width 为视频长边的百分比大小，如 10L% 表示 Width 为视频长边的 10%；</li>
<li>当字符串以 % 结尾时，含义同 W%。</li>
默认值为 10W%。
        :type Width: str
        :param Height: 水印的高度，支持 px，W%，H%，S%，L% 六种格式：
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素；当填 0px 且
 Width 不为 0px 时，表示水印的高度按原始 SVG 图像等比缩放；当 Width、Height 都填 0px 时，表示水印的高度取原始 SVG 图像的高度；</li>
<li>当字符串以 W% 结尾，表示水印 Height 为视频宽度的百分比大小，如 10W% 表示 Height 为视频宽度的 10%；</li>
<li>当字符串以 H% 结尾，表示水印 Height 为视频高度的百分比大小，如 10H% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 S% 结尾，表示水印 Height 为视频短边的百分比大小，如 10S% 表示 Height 为视频短边的 10%；</li>
<li>当字符串以 L% 结尾，表示水印 Height 为视频长边的百分比大小，如 10L% 表示 Height 为视频长边的 10%；</li>
<li>当字符串以 % 结尾时，含义同 H%。</li>
默认值为 0px。
        :type Height: str
        """
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class SvgWatermarkInputForUpdate(AbstractModel):
    """SVG水印模板输入参数

    """

    def __init__(self):
        """
        :param Width: 水印的宽度，支持 px，%，W%，H%，S%，L% 六种格式：
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素；当填 0px 且
 Height 不为 0px 时，表示水印的宽度按原始 SVG 图像等比缩放；当 Width、Height 都填 0px 时，表示水印的宽度取原始 SVG 图像的宽度；</li>
<li>当字符串以 W% 结尾，表示水印 Width 为视频宽度的百分比大小，如 10W% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 H% 结尾，表示水印 Width 为视频高度的百分比大小，如 10H% 表示 Width 为视频高度的 10%；</li>
<li>当字符串以 S% 结尾，表示水印 Width 为视频短边的百分比大小，如 10S% 表示 Width 为视频短边的 10%；</li>
<li>当字符串以 L% 结尾，表示水印 Width 为视频长边的百分比大小，如 10L% 表示 Width 为视频长边的 10%；</li>
<li>当字符串以 % 结尾时，含义同 W%。</li>
默认值为 10W%。
        :type Width: str
        :param Height: 水印的高度，支持 px，%，W%，H%，S%，L% 六种格式：
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素；当填 0px 且
 Width 不为 0px 时，表示水印的高度按原始 SVG 图像等比缩放；当 Width、Height 都填 0px 时，表示水印的高度取原始 SVG 图像的高度；</li>
<li>当字符串以 W% 结尾，表示水印 Height 为视频宽度的百分比大小，如 10W% 表示 Height 为视频宽度的 10%；</li>
<li>当字符串以 H% 结尾，表示水印 Height 为视频高度的百分比大小，如 10H% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 S% 结尾，表示水印 Height 为视频短边的百分比大小，如 10S% 表示 Height 为视频短边的 10%；</li>
<li>当字符串以 L% 结尾，表示水印 Height 为视频长边的百分比大小，如 10L% 表示 Height 为视频长边的 10%；</li>
<li>当字符串以 % 结尾时，含义同 H%。
默认值为 0px。
        :type Height: str
        """
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class TEHDConfig(AbstractModel):
    """极速高清参数配置。

    """

    def __init__(self):
        """
        :param Type: 极速高清类型，可选值：
<li>TEHD-100：极速高清-100。</li>
不填代表不启用极速高清。
        :type Type: str
        :param MaxVideoBitrate: 视频码率上限，当 Type 指定了极速高清类型时有效。
不填或填0表示不设视频码率上限。
        :type MaxVideoBitrate: int
        """
        self.Type = None
        self.MaxVideoBitrate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MaxVideoBitrate = params.get("MaxVideoBitrate")


class TEHDConfigForUpdate(AbstractModel):
    """极速高清参数配置。

    """

    def __init__(self):
        """
        :param Type: 极速高清类型，可选值：
<li>TEHD-100：极速高清-100。</li>
不填代表不修改。
        :type Type: str
        :param MaxVideoBitrate: 视频码率上限，不填代表不修改。
        :type MaxVideoBitrate: int
        """
        self.Type = None
        self.MaxVideoBitrate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MaxVideoBitrate = params.get("MaxVideoBitrate")


class TaskNotifyConfig(AbstractModel):
    """任务的事件通知配置。

    """

    def __init__(self):
        """
        :param CmqModel: CMQ 的模型，有 Queue 和 Topic 两种，目前仅支持 Queue。
        :type CmqModel: str
        :param CmqRegion: CMQ 的园区，如 sh，bj 等。
        :type CmqRegion: str
        :param QueueName: 当模型为 Queue 时有效，表示接收事件通知的 CMQ 的队列名。
        :type QueueName: str
        :param TopicName: 当模型为 Topic 时有效，表示接收事件通知的 CMQ 的主题名。
        :type TopicName: str
        :param NotifyMode: 工作流通知的模式，可取值有 Finish 和 Change，不填代表 Finish。
        :type NotifyMode: str
        """
        self.CmqModel = None
        self.CmqRegion = None
        self.QueueName = None
        self.TopicName = None
        self.NotifyMode = None


    def _deserialize(self, params):
        self.CmqModel = params.get("CmqModel")
        self.CmqRegion = params.get("CmqRegion")
        self.QueueName = params.get("QueueName")
        self.TopicName = params.get("TopicName")
        self.NotifyMode = params.get("NotifyMode")


class TaskOutputStorage(AbstractModel):
    """视频处理输出对象信息。

    """

    def __init__(self):
        """
        :param Type: 视频处理输出对象存储位置的类型，现在仅支持 COS。
        :type Type: str
        :param CosOutputStorage: 当 Type 为 COS 时有效，则该项为必填，表示视频处理 COS 输出位置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CosOutputStorage: :class:`tencentcloud.mps.v20190612.models.CosOutputStorage`
        """
        self.Type = None
        self.CosOutputStorage = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosOutputStorage") is not None:
            self.CosOutputStorage = CosOutputStorage()
            self.CosOutputStorage._deserialize(params.get("CosOutputStorage"))


class TaskSimpleInfo(AbstractModel):
    """任务概要信息

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID。
        :type TaskId: str
        :param TaskType: 任务类型，目前仅支持 WorkflowTask。
        :type TaskType: str
        :param CreateTime: 任务创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param BeginProcessTime: 任务开始执行时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。若任务尚未开始，该字段为：0000-00-00T00:00:00Z。
        :type BeginProcessTime: str
        :param FinishTime: 任务结束时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。若任务尚未完成，该字段为：0000-00-00T00:00:00Z。
        :type FinishTime: str
        """
        self.TaskId = None
        self.TaskType = None
        self.CreateTime = None
        self.BeginProcessTime = None
        self.FinishTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.CreateTime = params.get("CreateTime")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")


class TextWatermarkTemplateInput(AbstractModel):
    """文字水印模板

    """

    def __init__(self):
        """
        :param FontType: 字体类型，目前可以支持两种：
<li>simkai.ttf：可以支持中文和英文；</li>
<li>arial.ttf：仅支持英文。</li>
        :type FontType: str
        :param FontSize: 字体大小，格式：Npx，N 为数值。
        :type FontSize: str
        :param FontColor: 字体颜色，格式：0xRRGGBB，默认值：0xFFFFFF（白色）。
        :type FontColor: str
        :param FontAlpha: 文字透明度，取值范围：(0, 1]
<li>0：完全透明</li>
<li>1：完全不透明</li>
默认值：1。
        :type FontAlpha: float
        """
        self.FontType = None
        self.FontSize = None
        self.FontColor = None
        self.FontAlpha = None


    def _deserialize(self, params):
        self.FontType = params.get("FontType")
        self.FontSize = params.get("FontSize")
        self.FontColor = params.get("FontColor")
        self.FontAlpha = params.get("FontAlpha")


class TextWatermarkTemplateInputForUpdate(AbstractModel):
    """文字水印模板

    """

    def __init__(self):
        """
        :param FontType: 字体类型，目前可以支持两种：
<li>simkai.ttf：可以支持中文和英文；</li>
<li>arial.ttf：仅支持英文。</li>
        :type FontType: str
        :param FontSize: 字体大小，格式：Npx，N 为数值。
        :type FontSize: str
        :param FontColor: 字体颜色，格式：0xRRGGBB，默认值：0xFFFFFF（白色）。
        :type FontColor: str
        :param FontAlpha: 文字透明度，取值范围：(0, 1]
<li>0：完全透明</li>
<li>1：完全不透明</li>
        :type FontAlpha: float
        """
        self.FontType = None
        self.FontSize = None
        self.FontColor = None
        self.FontAlpha = None


    def _deserialize(self, params):
        self.FontType = params.get("FontType")
        self.FontSize = params.get("FontSize")
        self.FontColor = params.get("FontColor")
        self.FontAlpha = params.get("FontAlpha")


class TranscodeTaskInput(AbstractModel):
    """转码任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 视频转码模板 ID。
        :type Definition: int
        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。
注意：此字段可能返回 null，表示取不到有效值。
        :type WatermarkSet: list of WatermarkInput
        :param OutputStorage: 转码后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 转码后主文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_transcode_{definition}.{format}`。
        :type OutputObjectPath: str
        :param SegmentObjectName: 转码后分片文件的输出路径（转码 HLS 时 ts 的路径），只能为相对路径。如果不填，则默认为：`{inputName}_transcode_{definition}_{number}.{format}`。
        :type SegmentObjectName: str
        :param ObjectNumberFormat: 转码后输出路径中的`{number}`变量的规则。
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectNumberFormat: :class:`tencentcloud.mps.v20190612.models.NumberFormat`
        """
        self.Definition = None
        self.WatermarkSet = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.SegmentObjectName = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        self.SegmentObjectName = params.get("SegmentObjectName")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))


class TranscodeTemplate(AbstractModel):
    """转码模板详情

    """

    def __init__(self):
        """
        :param Definition: 转码模板唯一标识。
        :type Definition: str
        :param Container: 封装格式，取值：mp4、flv、hls、mp3、flac、ogg。
        :type Container: str
        :param Name: 转码模板名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Comment: 模板描述信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param Type: 模板类型，取值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>
        :type Type: str
        :param RemoveVideo: 是否去除视频数据，取值：
<li>0：保留；</li>
<li>1：去除。</li>
        :type RemoveVideo: int
        :param RemoveAudio: 是否去除音频数据，取值：
<li>0：保留；</li>
<li>1：去除。</li>
        :type RemoveAudio: int
        :param VideoTemplate: 视频流配置参数，仅当 RemoveVideo 为 0，该字段有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfo`
        :param AudioTemplate: 音频流配置参数，仅当 RemoveAudio 为 0，该字段有效 。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfo`
        :param TEHDConfig: 极速高清转码参数，需联系商务架构师开通后才能使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfig`
        :param ContainerType: 封装格式过滤条件，可选值：
<li>Video：视频格式，可以同时包含视频流和音频流的封装格式；</li>
<li>PureAudio：纯音频格式，只能包含音频流的封装格式板。</li>
        :type ContainerType: str
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Container = None
        self.Name = None
        self.Comment = None
        self.Type = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None
        self.ContainerType = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Type = params.get("Type")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        self.ContainerType = params.get("ContainerType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class VideoTemplateInfo(AbstractModel):
    """视频流配置参数

    """

    def __init__(self):
        """
        :param Codec: 视频流的编码格式，可选值：
<li>libx264：H.264 编码</li>
<li>libx265：H.265 编码</li>
目前 H.265 编码必须指定分辨率，并且需要在 640*480 以内。
        :type Codec: str
        :param Fps: 视频帧率，取值范围：[0, 60]，单位：Hz。
当取值为 0，表示帧率和原始视频保持一致。
        :type Fps: int
        :param Bitrate: 视频流的码率，取值范围：0 和 [128, 35000]，单位：kbps。
当取值为 0，表示视频码率和原始视频保持一致。
        :type Bitrate: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。
        :type ResolutionAdaptive: str
        :param Width: 视频流宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Width: int
        :param Height: 视频流高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。
        :type Height: int
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
默认值：black 。
        :type FillType: str
        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None
        self.FillType = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.FillType = params.get("FillType")


class VideoTemplateInfoForUpdate(AbstractModel):
    """视频流配置参数

    """

    def __init__(self):
        """
        :param Codec: 视频流的编码格式，可选值：
<li>libx264：H.264 编码</li>
<li>libx265：H.265 编码</li>
目前 H.265 编码必须指定分辨率，并且需要在 640*480 以内。
        :type Codec: str
        :param Fps: 视频帧率，取值范围：[0, 60]，单位：Hz。
当取值为 0，表示帧率和原始视频保持一致。
        :type Fps: int
        :param Bitrate: 视频流的码率，取值范围：0 和 [128, 35000]，单位：kbps。
当取值为 0，表示视频码率和原始视频保持一致。
        :type Bitrate: int
        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
        :type ResolutionAdaptive: str
        :param Width: 视频流宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
        :type Width: int
        :param Height: 视频流高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
        :type Height: int
        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
默认值：black 。
        :type FillType: str
        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None
        self.FillType = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.FillType = params.get("FillType")


class WatermarkInput(AbstractModel):
    """视频处理任务中的水印参数类型

    """

    def __init__(self):
        """
        :param Definition: 水印模板 ID。
        :type Definition: int
        :param TextContent: 文字内容，长度不超过100个字符。仅当水印类型为文字水印时填写。
        :type TextContent: str
        :param SvgContent: SVG 内容。长度不超过 2000000 个字符。仅当水印类型为 SVG 水印时填写。
        :type SvgContent: str
        """
        self.Definition = None
        self.TextContent = None
        self.SvgContent = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.TextContent = params.get("TextContent")
        self.SvgContent = params.get("SvgContent")


class WatermarkTemplate(AbstractModel):
    """水印模板详情

    """

    def __init__(self):
        """
        :param Definition: 水印模板唯一标识。
        :type Definition: int
        :param Type: 水印类型，取值：
<li>image：图片水印；</li>
<li>text：文字水印。</li>
        :type Type: str
        :param Name: 水印模板名称。
        :type Name: str
        :param Comment: 模板描述信息。
        :type Comment: str
        :param XPos: 水印图片原点距离视频图像原点的水平位置。
<li>当字符串以 % 结尾，表示水印 Left 为视频宽度指定百分比的位置，如 10% 表示 Left 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Left 为视频宽度指定像素的位置，如 100px 表示 Left 为 100 像素。</li>
        :type XPos: str
        :param YPos: 水印图片原点距离视频图像原点的垂直位置。
<li>当字符串以 % 结尾，表示水印 Top 为视频高度指定百分比的位置，如 10% 表示 Top 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Top 为视频高度指定像素的位置，如 100px 表示 Top 为 100 像素。</li>
        :type YPos: str
        :param ImageTemplate: 图片水印模板，仅当 Type 为 image，该字段有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageTemplate: :class:`tencentcloud.mps.v20190612.models.ImageWatermarkTemplate`
        :param TextTemplate: 文字水印模板，仅当 Type 为 text，该字段有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TextTemplate: :class:`tencentcloud.mps.v20190612.models.TextWatermarkTemplateInput`
        :param SvgTemplate: SVG 水印模板，当 Type 为 svg，该字段有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type SvgTemplate: :class:`tencentcloud.mps.v20190612.models.SvgWatermarkInput`
        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type UpdateTime: str
        :param CoordinateOrigin: 原点位置，可选值：
<li>topLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角；</li>
<li>topRight：表示坐标原点位于视频图像的右上角，水印原点为图片或文字的右上角；</li>
<li>bottomLeft：表示坐标原点位于视频图像的左下角，水印原点为图片或文字的左下角；</li>
<li>bottomRight：表示坐标原点位于视频图像的右下角，水印原点为图片或文字的右下。；</li>
        :type CoordinateOrigin: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None
        self.CreateTime = None
        self.UpdateTime = None
        self.CoordinateOrigin = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkTemplate()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInput()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInput()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CoordinateOrigin = params.get("CoordinateOrigin")


class WorkflowInfo(AbstractModel):
    """工作流信息详情。

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        :param WorkflowName: 工作流名称。
        :type WorkflowName: str
        :param Status: 工作流状态，取值范围：
<li>Enabled：已启用，</li>
<li>Disabled：已禁用。</li>
        :type Status: str
        :param Trigger: 工作流绑定的输入规则，当上传视频命中该规则到该对象时即触发工作流。
        :type Trigger: :class:`tencentcloud.mps.v20190612.models.WorkflowTrigger`
        :param OutputStorage: 视频处理的文件输出存储位置。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
        :param MediaProcessTask: 视频处理类型任务参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`
        :param AiContentReviewTask: 视频内容审核类型任务参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: 视频内容分析类型任务参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AiAnalysisTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: 视频内容识别类型任务参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param TaskNotifyConfig: 任务的事件通知信息，不填代表不获取事件通知。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TaskPriority: 任务流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。
        :type TaskPriority: int
        :param OutputDir: 视频处理生成的文件输出的目标目录，如`/movie/201907/`。
        :type OutputDir: str
        :param CreateTime: 工作流创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 工作流最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type UpdateTime: str
        """
        self.WorkflowId = None
        self.WorkflowName = None
        self.Status = None
        self.Trigger = None
        self.OutputStorage = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TaskNotifyConfig = None
        self.TaskPriority = None
        self.OutputDir = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        self.WorkflowName = params.get("WorkflowName")
        self.Status = params.get("Status")
        if params.get("Trigger") is not None:
            self.Trigger = WorkflowTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TaskPriority = params.get("TaskPriority")
        self.OutputDir = params.get("OutputDir")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class WorkflowTask(AbstractModel):
    """视频处理任务信息

    """

    def __init__(self):
        """
        :param TaskId: 视频处理任务 ID。
        :type TaskId: str
        :param Status: 任务流状态，取值：
<li>PROCESSING：处理中；</li>
<li>FINISH：已完成。</li>
        :type Status: str
        :param ErrCode: 已弃用，请使用各个具体任务的 ErrCode。
        :type ErrCode: int
        :param Message: 已弃用，请使用各个具体任务的 Message。
        :type Message: str
        :param InputInfo: 视频处理的目标文件信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`
        :param MetaData: 原始视频的元信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaData: :class:`tencentcloud.mps.v20190612.models.MediaMetaData`
        :param MediaProcessResultSet: 视频处理任务的执行状态与结果。
        :type MediaProcessResultSet: list of MediaProcessTaskResult
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.InputInfo = None
        self.MetaData = None
        self.MediaProcessResultSet = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        if params.get("MediaProcessResultSet") is not None:
            self.MediaProcessResultSet = []
            for item in params.get("MediaProcessResultSet"):
                obj = MediaProcessTaskResult()
                obj._deserialize(item)
                self.MediaProcessResultSet.append(obj)


class WorkflowTrigger(AbstractModel):
    """输入规则，当上传视频命中该规则时，即触发工作流。

    """

    def __init__(self):
        """
        :param Type: 触发器的类型，目前仅支持 CosFileUpload。
        :type Type: str
        :param CosFileUploadTrigger: 当 Type 为 CosFileUpload 时必填且有效，为 COS 触发规则。
注意：此字段可能返回 null，表示取不到有效值。
        :type CosFileUploadTrigger: :class:`tencentcloud.mps.v20190612.models.CosFileUploadTrigger`
        """
        self.Type = None
        self.CosFileUploadTrigger = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosFileUploadTrigger") is not None:
            self.CosFileUploadTrigger = CosFileUploadTrigger()
            self.CosFileUploadTrigger._deserialize(params.get("CosFileUploadTrigger"))