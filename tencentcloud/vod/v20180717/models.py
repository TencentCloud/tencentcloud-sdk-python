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


class ApplyUploadRequest(AbstractModel):
    """ApplyUpload请求参数结构体

    """

    def __init__(self):
        """
        :param MediaType: 媒体类型，可选值请参考[上传能力综述](https://cloud.tencent.com/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)。
        :type MediaType: str
        :param MediaName: 媒体名称。
        :type MediaName: str
        :param CoverType: 封面类型，可选值请参考[上传能力综述](https://cloud.tencent.com/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)。
        :type CoverType: str
        :param Procedure: 媒体后续任务操作，详见[上传指定任务流](https://cloud.tencent.com/document/product/266/9759)。
        :type Procedure: str
        :param ExpireTime: 媒体文件过期时间，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type ExpireTime: str
        :param StorageRegion: 指定上传园区，仅适用于对上传地域有特殊需求的用户。
        :type StorageRegion: str
        :param ClassId: 分类ID，用于对媒体进行分类管理，可通过[创建分类](https://cloud.tencent.com/document/product/266/7812)接口，创建分类，获得分类 ID。
<li>默认值：0，表示其他分类。</li>
        :type ClassId: int
        :param SourceContext: 来源上下文，用于透传用户请求信息，上传回调接口将返回该字段值，最长 250 个字符。
        :type SourceContext: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.MediaType = None
        self.MediaName = None
        self.CoverType = None
        self.Procedure = None
        self.ExpireTime = None
        self.StorageRegion = None
        self.ClassId = None
        self.SourceContext = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.MediaType = params.get("MediaType")
        self.MediaName = params.get("MediaName")
        self.CoverType = params.get("CoverType")
        self.Procedure = params.get("Procedure")
        self.ExpireTime = params.get("ExpireTime")
        self.StorageRegion = params.get("StorageRegion")
        self.ClassId = params.get("ClassId")
        self.SourceContext = params.get("SourceContext")
        self.SubAppId = params.get("SubAppId")


class ApplyUploadResponse(AbstractModel):
    """ApplyUpload返回参数结构体

    """

    def __init__(self):
        """
        :param StorageBucket: 存储桶，用于上传接口 URL 的 bucket_name。
        :type StorageBucket: str
        :param StorageRegion: 存储园区，用于上传接口 Host 的 Region。
        :type StorageRegion: str
        :param VodSessionKey: 点播会话，用于确认上传接口的参数 VodSessionKey。
        :type VodSessionKey: str
        :param MediaStoragePath: 媒体存储路径，用于上传接口存储媒体的对象键（Key）。
        :type MediaStoragePath: str
        :param CoverStoragePath: 封面存储路径，用于上传接口存储封面的对象键（Key）。
        :type CoverStoragePath: str
        :param TempCertificate: 临时凭证，用于上传接口的权限验证。
        :type TempCertificate: :class:`tencentcloud.vod.v20180717.models.TempCertificate`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StorageBucket = None
        self.StorageRegion = None
        self.VodSessionKey = None
        self.MediaStoragePath = None
        self.CoverStoragePath = None
        self.TempCertificate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StorageBucket = params.get("StorageBucket")
        self.StorageRegion = params.get("StorageRegion")
        self.VodSessionKey = params.get("VodSessionKey")
        self.MediaStoragePath = params.get("MediaStoragePath")
        self.CoverStoragePath = params.get("CoverStoragePath")
        if params.get("TempCertificate") is not None:
            self.TempCertificate = TempCertificate()
            self.TempCertificate._deserialize(params.get("TempCertificate"))
        self.RequestId = params.get("RequestId")


class CommitUploadRequest(AbstractModel):
    """CommitUpload请求参数结构体

    """

    def __init__(self):
        """
        :param VodSessionKey: 点播会话，取申请上传接口的返回值 VodSessionKey。
        :type VodSessionKey: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.VodSessionKey = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.VodSessionKey = params.get("VodSessionKey")
        self.SubAppId = params.get("SubAppId")


class CommitUploadResponse(AbstractModel):
    """CommitUpload返回参数结构体

    """

    def __init__(self):
        """
        :param FileId: 媒体文件的唯一标识。
        :type FileId: str
        :param MediaUrl: 媒体播放地址。
        :type MediaUrl: str
        :param CoverUrl: 媒体封面地址。
        :type CoverUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileId = None
        self.MediaUrl = None
        self.CoverUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.MediaUrl = params.get("MediaUrl")
        self.CoverUrl = params.get("CoverUrl")
        self.RequestId = params.get("RequestId")


class CreateClassRequest(AbstractModel):
    """CreateClass请求参数结构体

    """

    def __init__(self):
        """
        :param ParentId: 父类 ID，一级分类填写 -1。
        :type ParentId: int
        :param ClassName: 分类名称，长度限制：1-64 个字符。
        :type ClassName: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.ParentId = None
        self.ClassName = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.ParentId = params.get("ParentId")
        self.ClassName = params.get("ClassName")
        self.SubAppId = params.get("SubAppId")


class CreateClassResponse(AbstractModel):
    """CreateClass返回参数结构体

    """

    def __init__(self):
        """
        :param ClassId: 分类 ID
        :type ClassId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClassId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClassId = params.get("ClassId")
        self.RequestId = params.get("RequestId")


class DeleteClassRequest(AbstractModel):
    """DeleteClass请求参数结构体

    """

    def __init__(self):
        """
        :param ClassId: 分类 ID
        :type ClassId: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.ClassId = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.ClassId = params.get("ClassId")
        self.SubAppId = params.get("SubAppId")


class DeleteClassResponse(AbstractModel):
    """DeleteClass返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMediaRequest(AbstractModel):
    """DeleteMedia请求参数结构体

    """

    def __init__(self):
        """
        :param FileId: 媒体文件的唯一标识。
        :type FileId: str
        :param DeleteParts: 指定本次需要删除的部分。默认值为 "[]", 表示删除媒体及其对应的全部视频处理文件。
        :type DeleteParts: list of MediaDeleteItem
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID 。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.FileId = None
        self.DeleteParts = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        if params.get("DeleteParts") is not None:
            self.DeleteParts = []
            for item in params.get("DeleteParts"):
                obj = MediaDeleteItem()
                obj._deserialize(item)
                self.DeleteParts.append(obj)
        self.SubAppId = params.get("SubAppId")


class DeleteMediaResponse(AbstractModel):
    """DeleteMedia返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAllClassRequest(AbstractModel):
    """DescribeAllClass请求参数结构体

    """

    def __init__(self):
        """
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.SubAppId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")


class DescribeAllClassResponse(AbstractModel):
    """DescribeAllClass返回参数结构体

    """

    def __init__(self):
        """
        :param ClassInfoSet: 分类信息集合
        :type ClassInfoSet: list of MediaClassInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClassInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClassInfoSet") is not None:
            self.ClassInfoSet = []
            for item in params.get("ClassInfoSet"):
                obj = MediaClassInfo()
                obj._deserialize(item)
                self.ClassInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMediaInfosRequest(AbstractModel):
    """DescribeMediaInfos请求参数结构体

    """

    def __init__(self):
        """
        :param FileIds: 媒体文件 ID 列表，N 从 0 开始取值，最大 19。
        :type FileIds: list of str
        :param Filters: 指定所有媒体文件需要返回的信息，可同时指定多个信息，N 从 0 开始递增。如果未填写该字段，默认返回所有信息。选项有：
<li>basicInfo（视频基础信息）。</li>
<li>metaData（视频元信息）。</li>
<li>transcodeInfo（视频转码结果信息）。</li>
<li>animatedGraphicsInfo（视频转动图结果信息）。</li>
<li>imageSpriteInfo（视频雪碧图信息）。</li>
<li>snapshotByTimeOffsetInfo（视频指定时间点截图信息）。</li>
<li>sampleSnapshotInfo（采样截图信息）。</li>
<li>keyFrameDescInfo（打点信息）。</li>
        :type Filters: list of str
        """
        self.FileIds = None
        self.Filters = None


    def _deserialize(self, params):
        self.FileIds = params.get("FileIds")
        self.Filters = params.get("Filters")


class DescribeMediaInfosResponse(AbstractModel):
    """DescribeMediaInfos返回参数结构体

    """

    def __init__(self):
        """
        :param MediaInfoSet: 媒体文件信息列表。
        :type MediaInfoSet: list of MediaInfo
        :param NotExistFileIdSet: 不存在的文件 ID 列表。
        :type NotExistFileIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MediaInfoSet = None
        self.NotExistFileIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MediaInfoSet") is not None:
            self.MediaInfoSet = []
            for item in params.get("MediaInfoSet"):
                obj = MediaInfo()
                obj._deserialize(item)
                self.MediaInfoSet.append(obj)
        self.NotExistFileIdSet = params.get("NotExistFileIdSet")
        self.RequestId = params.get("RequestId")


class MediaAnimatedGraphicsInfo(AbstractModel):
    """点播文件视频转动图结果信息

    """

    def __init__(self):
        """
        :param AnimatedGraphicsSet: 视频转动图结果信息
        :type AnimatedGraphicsSet: list of MediaAnimatedGraphicsItem
        """
        self.AnimatedGraphicsSet = None


    def _deserialize(self, params):
        if params.get("AnimatedGraphicsSet") is not None:
            self.AnimatedGraphicsSet = []
            for item in params.get("AnimatedGraphicsSet"):
                obj = MediaAnimatedGraphicsItem()
                obj._deserialize(item)
                self.AnimatedGraphicsSet.append(obj)


class MediaAnimatedGraphicsItem(AbstractModel):
    """视频转动图结果信息

    """

    def __init__(self):
        """
        :param Url: 转动图的文件地址。
        :type Url: str
        :param Definition: 转动图模板 ID，参见[转动图参数模板](https://cloud.tencent.com/document/product/266/11701#.E9.A2.84.E7.BD.AE.E8.BD.AC.E5.8A.A8.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
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
        self.Url = None
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
        self.Url = params.get("Url")
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
        :type Bitrate: int
        :param SamplingRate: 音频流的采样率，单位：hz。
        :type SamplingRate: int
        :param Codec: 音频流的编码格式，例如 aac。
        :type Codec: str
        """
        self.Bitrate = None
        self.SamplingRate = None
        self.Codec = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.SamplingRate = params.get("SamplingRate")
        self.Codec = params.get("Codec")


class MediaBasicInfo(AbstractModel):
    """点播媒体文件基础信息

    """

    def __init__(self):
        """
        :param Name: 媒体文件名称。
        :type Name: str
        :param Description: 媒体文件描述。
        :type Description: str
        :param CreateTime: 媒体文件的创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 媒体文件的最近更新时间（如修改视频属性、发起视频处理等会触发更新媒体文件信息的操作），使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type UpdateTime: str
        :param ExpireTime: 媒体文件的过期时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。过期后该媒体文件及其相关资源（转码结果、雪碧图等）将被永久删除。“9999-12-31T23:59:59Z”表示永不过期。
        :type ExpireTime: str
        :param ClassId: 媒体文件的分类 ID。
        :type ClassId: int
        :param ClassName: 媒体文件的分类名称。
        :type ClassName: str
        :param ClassPath: 媒体文件的分类路径，分类间以“-”分隔，如“新的一级分类 - 新的二级分类”。
        :type ClassPath: str
        :param CoverUrl: 媒体文件的封面图片地址。
        :type CoverUrl: str
        :param Type: 媒体文件的封装格式，例如 mp4、flv 等。
        :type Type: str
        :param MediaUrl: 原始媒体文件的 URL 地址。
        :type MediaUrl: str
        :param SourceInfo: 该媒体文件的来源信息。
        :type SourceInfo: :class:`tencentcloud.vod.v20180717.models.MediaSourceData`
        :param StorageRegion: 媒体文件存储地区，如 ap-guangzhou，参见[地域列表](https://cloud.tencent.com/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。
        :type StorageRegion: str
        :param TagSet: 媒体文件的标签信息。
        :type TagSet: list of str
        :param Vid: 直播录制文件的唯一标识
        :type Vid: str
        """
        self.Name = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ExpireTime = None
        self.ClassId = None
        self.ClassName = None
        self.ClassPath = None
        self.CoverUrl = None
        self.Type = None
        self.MediaUrl = None
        self.SourceInfo = None
        self.StorageRegion = None
        self.TagSet = None
        self.Vid = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ClassId = params.get("ClassId")
        self.ClassName = params.get("ClassName")
        self.ClassPath = params.get("ClassPath")
        self.CoverUrl = params.get("CoverUrl")
        self.Type = params.get("Type")
        self.MediaUrl = params.get("MediaUrl")
        if params.get("SourceInfo") is not None:
            self.SourceInfo = MediaSourceData()
            self.SourceInfo._deserialize(params.get("SourceInfo"))
        self.StorageRegion = params.get("StorageRegion")
        self.TagSet = params.get("TagSet")
        self.Vid = params.get("Vid")


class MediaClassInfo(AbstractModel):
    """分类信息描述

    """

    def __init__(self):
        """
        :param ClassId: 分类 ID
        :type ClassId: int
        :param ParentId: 父类 ID，一级分类的父类 ID 为 -1。
        :type ParentId: int
        :param ClassName: 分类名称
        :type ClassName: str
        :param Level: 分类级别，一级分类为 0，最大值为 3，即最多允许 4 级分类层次。
        :type Level: int
        :param SubClassIdSet: 当前分类的第一级子类 ID 集合
        :type SubClassIdSet: list of int
        """
        self.ClassId = None
        self.ParentId = None
        self.ClassName = None
        self.Level = None
        self.SubClassIdSet = None


    def _deserialize(self, params):
        self.ClassId = params.get("ClassId")
        self.ParentId = params.get("ParentId")
        self.ClassName = params.get("ClassName")
        self.Level = params.get("Level")
        self.SubClassIdSet = params.get("SubClassIdSet")


class MediaDeleteItem(AbstractModel):
    """指定删除点播视频时的删除内容

    """

    def __init__(self):
        """
        :param Type: 所指定的删除部分。如果未填写该字段则参数无效。可选值有：
<li>TranscodeFiles（删除转码文件）。</li>
<li>WechatPublishFiles（删除微信发布文件）。</li>
        :type Type: str
        :param Definition: 删除由Type参数指定的种类下的视频模板号，模板定义参见[转码模板](https://cloud.tencent.com/document/product/266/11701#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。
默认值为0，表示删除参数Type指定种类下所有的视频。
        :type Definition: int
        """
        self.Type = None
        self.Definition = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Definition = params.get("Definition")


class MediaImageSpriteInfo(AbstractModel):
    """点播文件雪碧图信息

    """

    def __init__(self):
        """
        :param ImageSpriteSet: 特定规格的雪碧图信息集合，每个元素代表一套相同规格的雪碧图。
        :type ImageSpriteSet: list of MediaImageSpriteItem
        """
        self.ImageSpriteSet = None


    def _deserialize(self, params):
        if params.get("ImageSpriteSet") is not None:
            self.ImageSpriteSet = []
            for item in params.get("ImageSpriteSet"):
                obj = MediaImageSpriteItem()
                obj._deserialize(item)
                self.ImageSpriteSet.append(obj)


class MediaImageSpriteItem(AbstractModel):
    """雪碧图信息

    """

    def __init__(self):
        """
        :param Definition: 雪碧图规格，参见[雪碧图参数模板](https://cloud.tencent.com/document/product/266/11702#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param Height: 雪碧图小图的高度。
        :type Height: int
        :param Width: 雪碧图小图的宽度。
        :type Width: int
        :param TotalCount: 每一张雪碧图大图里小图的数量。
        :type TotalCount: int
        :param ImageUrlSet: 每一张雪碧图大图的地址。
        :type ImageUrlSet: list of str
        :param WebVttUrl: 雪碧图子图位置与时间关系的 WebVtt 文件地址。WebVtt 文件表明了各个雪碧图小图对应的时间点，以及在在雪碧大图里的坐标位置，一般被播放器用于实现预览。
        :type WebVttUrl: str
        """
        self.Definition = None
        self.Height = None
        self.Width = None
        self.TotalCount = None
        self.ImageUrlSet = None
        self.WebVttUrl = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.TotalCount = params.get("TotalCount")
        self.ImageUrlSet = params.get("ImageUrlSet")
        self.WebVttUrl = params.get("WebVttUrl")


class MediaInfo(AbstractModel):
    """点播文件信息

    """

    def __init__(self):
        """
        :param BasicInfo: 基础信息。包括视频名称、大小、时长、封面图片等。
        :type BasicInfo: :class:`tencentcloud.vod.v20180717.models.MediaBasicInfo`
        :param MetaData: 元信息。包括视频流信息、音频流信息等。
        :type MetaData: :class:`tencentcloud.vod.v20180717.models.MediaMetaData`
        :param TranscodeInfo: 转码结果信息。包括该视频转码生成的各种码率的视频的地址、规格、码率、分辨率等。
        :type TranscodeInfo: :class:`tencentcloud.vod.v20180717.models.MediaTranscodeInfo`
        :param AnimatedGraphicsInfo: 转动图结果信息。对视频转动图（如 gif）后，动图相关信息。
        :type AnimatedGraphicsInfo: :class:`tencentcloud.vod.v20180717.models.MediaAnimatedGraphicsInfo`
        :param SampleSnapshotInfo: 采样截图信息。对视频采样截图后，相关截图信息。
        :type SampleSnapshotInfo: :class:`tencentcloud.vod.v20180717.models.MediaSampleSnapshotInfo`
        :param ImageSpriteInfo: 雪碧图信息。对视频截取雪碧图之后，雪碧的相关信息。
        :type ImageSpriteInfo: :class:`tencentcloud.vod.v20180717.models.MediaImageSpriteInfo`
        :param SnapshotByTimeOffsetInfo: 指定时间点截图信息。对视频依照指定时间点截图后，各个截图的信息。
        :type SnapshotByTimeOffsetInfo: :class:`tencentcloud.vod.v20180717.models.MediaSnapshotByTimeOffsetInfo`
        :param KeyFrameDescInfo: 视频打点信息。对视频设置的各个打点信息。
        :type KeyFrameDescInfo: :class:`tencentcloud.vod.v20180717.models.MediaKeyFrameDescInfo`
        :param FileId: 媒体文件唯一标识 ID。
        :type FileId: str
        """
        self.BasicInfo = None
        self.MetaData = None
        self.TranscodeInfo = None
        self.AnimatedGraphicsInfo = None
        self.SampleSnapshotInfo = None
        self.ImageSpriteInfo = None
        self.SnapshotByTimeOffsetInfo = None
        self.KeyFrameDescInfo = None
        self.FileId = None


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self.BasicInfo = MediaBasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        if params.get("TranscodeInfo") is not None:
            self.TranscodeInfo = MediaTranscodeInfo()
            self.TranscodeInfo._deserialize(params.get("TranscodeInfo"))
        if params.get("AnimatedGraphicsInfo") is not None:
            self.AnimatedGraphicsInfo = MediaAnimatedGraphicsInfo()
            self.AnimatedGraphicsInfo._deserialize(params.get("AnimatedGraphicsInfo"))
        if params.get("SampleSnapshotInfo") is not None:
            self.SampleSnapshotInfo = MediaSampleSnapshotInfo()
            self.SampleSnapshotInfo._deserialize(params.get("SampleSnapshotInfo"))
        if params.get("ImageSpriteInfo") is not None:
            self.ImageSpriteInfo = MediaImageSpriteInfo()
            self.ImageSpriteInfo._deserialize(params.get("ImageSpriteInfo"))
        if params.get("SnapshotByTimeOffsetInfo") is not None:
            self.SnapshotByTimeOffsetInfo = MediaSnapshotByTimeOffsetInfo()
            self.SnapshotByTimeOffsetInfo._deserialize(params.get("SnapshotByTimeOffsetInfo"))
        if params.get("KeyFrameDescInfo") is not None:
            self.KeyFrameDescInfo = MediaKeyFrameDescInfo()
            self.KeyFrameDescInfo._deserialize(params.get("KeyFrameDescInfo"))
        self.FileId = params.get("FileId")


class MediaKeyFrameDescInfo(AbstractModel):
    """视频打点信息

    """

    def __init__(self):
        """
        :param KeyFrameDescSet: 视频打点信息数组。
        :type KeyFrameDescSet: list of MediaKeyFrameDescItem
        """
        self.KeyFrameDescSet = None


    def _deserialize(self, params):
        if params.get("KeyFrameDescSet") is not None:
            self.KeyFrameDescSet = []
            for item in params.get("KeyFrameDescSet"):
                obj = MediaKeyFrameDescItem()
                obj._deserialize(item)
                self.KeyFrameDescSet.append(obj)


class MediaKeyFrameDescItem(AbstractModel):
    """视频打点信息

    """

    def __init__(self):
        """
        :param TimeOffset: 打点的视频偏移时间，单位：秒。
        :type TimeOffset: float
        :param Content: 打点的内容字符串，限制 1-128 个字符。
        :type Content: str
        """
        self.TimeOffset = None
        self.Content = None


    def _deserialize(self, params):
        self.TimeOffset = params.get("TimeOffset")
        self.Content = params.get("Content")


class MediaMetaData(AbstractModel):
    """点播媒体文件元信息

    """

    def __init__(self):
        """
        :param Size: 上传的媒体文件大小（视频为 HLS 时，大小是 m3u8 和 ts 文件大小的总和），单位：字节。
        :type Size: int
        :param Container: 容器类型，例如 m4a，mp4 等。
        :type Container: str
        :param Bitrate: 视频流码率平均值与音频流码率平均值之和，单位：bps。
        :type Bitrate: int
        :param Height: 视频流高度的最大值，单位：px。
        :type Height: int
        :param Width: 视频流宽度的最大值，单位：px。
        :type Width: int
        :param Duration: 视频时长，单位：秒。
        :type Duration: float
        :param Rotate: 视频拍摄时的选择角度，单位：度。
        :type Rotate: int
        :param VideoStreamSet: 视频流信息。
        :type VideoStreamSet: list of MediaVideoStreamItem
        :param AudioStreamSet: 音频流信息。
        :type AudioStreamSet: list of MediaAudioStreamItem
        :param VideoDuration: 视频时长，单位：秒。
        :type VideoDuration: float
        :param AudioDuration: 音频时长，单位：秒。
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


class MediaSampleSnapshotInfo(AbstractModel):
    """点播文件采样截图信息

    """

    def __init__(self):
        """
        :param SampleSnapshotSet: 特定规格的采样截图信息集合，每个元素代表一套相同规格的采样截图。
        :type SampleSnapshotSet: list of MediaSampleSnapshotItem
        """
        self.SampleSnapshotSet = None


    def _deserialize(self, params):
        if params.get("SampleSnapshotSet") is not None:
            self.SampleSnapshotSet = []
            for item in params.get("SampleSnapshotSet"):
                obj = MediaSampleSnapshotItem()
                obj._deserialize(item)
                self.SampleSnapshotSet.append(obj)


class MediaSampleSnapshotItem(AbstractModel):
    """采样截图信息

    """

    def __init__(self):
        """
        :param Definition: 采样截图规格 ID，参见[采样截图参数模板](https://cloud.tencent.com/document/product/266/11702#.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param SampleType: 采样方式，取值范围：
<li>Percent：根据百分比间隔采样。</li>
<li>Time：根据时间间隔采样。</li>
        :type SampleType: str
        :param Interval: 采样间隔
<li>当 SampleType 为 Percent 时，该值表示多少百分比一张图。</li>
<li>当 SampleType 为 Time 时，该值表示多少时间间隔一张图，单位秒， 第一张图均为视频首帧。</li>
        :type Interval: int
        :param ImageUrlSet: 生成的截图 url 列表。
        :type ImageUrlSet: list of str
        :param WaterMarkDefinition: 截图如果被打上了水印，被打水印的模板 ID 列表。
        :type WaterMarkDefinition: list of int
        """
        self.Definition = None
        self.SampleType = None
        self.Interval = None
        self.ImageUrlSet = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SampleType = params.get("SampleType")
        self.Interval = params.get("Interval")
        self.ImageUrlSet = params.get("ImageUrlSet")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")


class MediaSnapshotByTimeOffsetInfo(AbstractModel):
    """点播文件指定时间点截图信息

    """

    def __init__(self):
        """
        :param SnapshotByTimeOffsetSet: 特定规格的指定时间点截图信息集合。目前每种规格只能有一套截图。
        :type SnapshotByTimeOffsetSet: list of MediaSnapshotByTimeOffsetItem
        """
        self.SnapshotByTimeOffsetSet = None


    def _deserialize(self, params):
        if params.get("SnapshotByTimeOffsetSet") is not None:
            self.SnapshotByTimeOffsetSet = []
            for item in params.get("SnapshotByTimeOffsetSet"):
                obj = MediaSnapshotByTimeOffsetItem()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetSet.append(obj)


class MediaSnapshotByTimeOffsetItem(AbstractModel):
    """点播文件指定时间点截图信息

    """

    def __init__(self):
        """
        :param Definition: 指定时间点截图规格，参见[指定时间点截图参数模板](https://cloud.tencent.com/document/product/266/11702#.E6.8C.87.E5.AE.9A.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param PicInfoSet: 同一规格的截图信息集合，每个元素代表一张截图。
        :type PicInfoSet: list of MediaSnapshotByTimePicInfoItem
        """
        self.Definition = None
        self.PicInfoSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("PicInfoSet") is not None:
            self.PicInfoSet = []
            for item in params.get("PicInfoSet"):
                obj = MediaSnapshotByTimePicInfoItem()
                obj._deserialize(item)
                self.PicInfoSet.append(obj)


class MediaSnapshotByTimePicInfoItem(AbstractModel):
    """指定时间点截图信息

    """

    def __init__(self):
        """
        :param TimeOffset: 该张截图对应视频文件中的时间偏移，单位：秒。
        :type TimeOffset: float
        :param Url: 该张截图的 URL 地址。
        :type Url: str
        :param WaterMarkDefinition: 截图如果被打上了水印，被打水印的模板 ID 列表。
        :type WaterMarkDefinition: list of int
        """
        self.TimeOffset = None
        self.Url = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.TimeOffset = params.get("TimeOffset")
        self.Url = params.get("Url")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")


class MediaSourceData(AbstractModel):
    """来源文件信息

    """

    def __init__(self):
        """
        :param SourceType: 媒体文件的来源类别：
<li>Record：来自录制。如直播录制、直播时移录制等。</li>
<li>Upload：来自上传。如拉取上传、服务端上传、客户端 UGC 上传等。</li>
<li>VideoProcessing：来自视频处理。如视频拼接、视频剪辑等。</li>
<li>Unknown：未知来源。</li>
        :type SourceType: str
        :param SourceContext: 用户创建文件时透传的字段
        :type SourceContext: str
        """
        self.SourceType = None
        self.SourceContext = None


    def _deserialize(self, params):
        self.SourceType = params.get("SourceType")
        self.SourceContext = params.get("SourceContext")


class MediaTranscodeInfo(AbstractModel):
    """点播文件转码信息

    """

    def __init__(self):
        """
        :param TranscodeSet: 各规格的转码信息集合，每个元素代表一个规格的转码结果。
        :type TranscodeSet: list of MediaTranscodeItem
        """
        self.TranscodeSet = None


    def _deserialize(self, params):
        if params.get("TranscodeSet") is not None:
            self.TranscodeSet = []
            for item in params.get("TranscodeSet"):
                obj = MediaTranscodeItem()
                obj._deserialize(item)
                self.TranscodeSet.append(obj)


class MediaTranscodeItem(AbstractModel):
    """转码信息

    """

    def __init__(self):
        """
        :param Url: 转码后的视频文件地址。
        :type Url: str
        :param Definition: 转码规格 ID，参见[转码参数模板](https://cloud.tencent.com/document/product/266/11701#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。
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
        :type AudioStreamSet: list of MediaAudioStreamItem
        :param VideoStreamSet: 视频流信息。
        :type VideoStreamSet: list of MediaVideoStreamItem
        """
        self.Url = None
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
        self.Url = params.get("Url")
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
        :type Bitrate: int
        :param Height: 视频流的高度，单位：px。
        :type Height: int
        :param Width: 视频流的宽度，单位：px。
        :type Width: int
        :param Codec: 视频流的编码格式，例如 h264。
        :type Codec: str
        :param Fps: 帧率，单位：hz。
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


class ModifyClassRequest(AbstractModel):
    """ModifyClass请求参数结构体

    """

    def __init__(self):
        """
        :param ClassId: 分类 ID
        :type ClassId: int
        :param ClassName: 分类名称。长度限制：1-64 个字符。
        :type ClassName: str
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.ClassId = None
        self.ClassName = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.ClassId = params.get("ClassId")
        self.ClassName = params.get("ClassName")
        self.SubAppId = params.get("SubAppId")


class ModifyClassResponse(AbstractModel):
    """ModifyClass返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMediaInfoRequest(AbstractModel):
    """ModifyMediaInfo请求参数结构体

    """

    def __init__(self):
        """
        :param FileId: 媒体文件唯一标识。
        :type FileId: str
        :param Name: 媒体文件名称，最长 64 个字符。
        :type Name: str
        :param Description: 媒体文件描述，最长 128 个字符。
        :type Description: str
        :param ClassId: 媒体文件分类 ID。
        :type ClassId: int
        :param ExpireTime: 媒体文件过期时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。填“9999-12-31T23:59:59Z”表示永不过期。过期后该媒体文件及其相关资源（转码结果、雪碧图等）将被永久删除。
        :type ExpireTime: str
        :param CoverData: 视频封面图片文件（如 jpeg, png 等）进行 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串，仅支持 gif、jpeg、png 三种图片格式。
        :type CoverData: str
        :param AddKeyFrameDescs: 新增的一组视频打点信息，如果某个偏移时间已存在打点，则会进行覆盖操作，单个媒体文件最多 100 个打点信息。同一个请求里，AddKeyFrameDescs 的时间偏移参数必须与 DeleteKeyFrameDescs 都不同。
        :type AddKeyFrameDescs: list of MediaKeyFrameDescItem
        :param DeleteKeyFrameDescs: 要删除的一组视频打点信息的时间偏移，单位：秒。同一个请求里，AddKeyFrameDescs 的时间偏移参数必须与 DeleteKeyFrameDescs 都不同。
        :type DeleteKeyFrameDescs: list of float
        :param ClearKeyFrameDescs: 取值 1 表示清空视频打点信息，其他值无意义。
同一个请求里，ClearKeyFrameDescs 与 AddKeyFrameDescs 不能同时出现。
        :type ClearKeyFrameDescs: int
        :param AddTags: 新增的一组标签，单个媒体文件最多 16 个标签，单个标签最多 16 个字符。同一个请求里，AddTags 参数必须与 DeleteTags 都不同。
        :type AddTags: list of str
        :param DeleteTags: 要删除的一组标签。同一个请求里，AddTags 参数必须与 DeleteTags 都不同。
        :type DeleteTags: list of str
        :param ClearTags: 取值 1 表示清空媒体文件所有标签，其他值无意义。
同一个请求里，ClearTags 与 AddTags 不能同时出现。
        :type ClearTags: int
        :param SubAppId: 点播[子应用](/document/product/266/14574) ID 。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        """
        self.FileId = None
        self.Name = None
        self.Description = None
        self.ClassId = None
        self.ExpireTime = None
        self.CoverData = None
        self.AddKeyFrameDescs = None
        self.DeleteKeyFrameDescs = None
        self.ClearKeyFrameDescs = None
        self.AddTags = None
        self.DeleteTags = None
        self.ClearTags = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.ClassId = params.get("ClassId")
        self.ExpireTime = params.get("ExpireTime")
        self.CoverData = params.get("CoverData")
        if params.get("AddKeyFrameDescs") is not None:
            self.AddKeyFrameDescs = []
            for item in params.get("AddKeyFrameDescs"):
                obj = MediaKeyFrameDescItem()
                obj._deserialize(item)
                self.AddKeyFrameDescs.append(obj)
        self.DeleteKeyFrameDescs = params.get("DeleteKeyFrameDescs")
        self.ClearKeyFrameDescs = params.get("ClearKeyFrameDescs")
        self.AddTags = params.get("AddTags")
        self.DeleteTags = params.get("DeleteTags")
        self.ClearTags = params.get("ClearTags")
        self.SubAppId = params.get("SubAppId")


class ModifyMediaInfoResponse(AbstractModel):
    """ModifyMediaInfo返回参数结构体

    """

    def __init__(self):
        """
        :param CoverUrl: 新的视频封面 URL。
* 注意：仅当请求携带 CoverData 时此返回值有效。 *
        :type CoverUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CoverUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CoverUrl = params.get("CoverUrl")
        self.RequestId = params.get("RequestId")


class TempCertificate(AbstractModel):
    """临时凭证

    """

    def __init__(self):
        """
        :param SecretId: 临时安全证书 Id。
        :type SecretId: str
        :param SecretKey: 临时安全证书 Key。
        :type SecretKey: str
        :param Token: Token 值。
        :type Token: str
        :param ExpiredTime: 证书无效的时间，返回 Unix 时间戳，精确到秒。
        :type ExpiredTime: int
        """
        self.SecretId = None
        self.SecretKey = None
        self.Token = None
        self.ExpiredTime = None


    def _deserialize(self, params):
        self.SecretId = params.get("SecretId")
        self.SecretKey = params.get("SecretKey")
        self.Token = params.get("Token")
        self.ExpiredTime = params.get("ExpiredTime")