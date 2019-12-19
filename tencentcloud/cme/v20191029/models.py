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


class AudioStreamInfo(AbstractModel):
    """音频流信息。

    """

    def __init__(self):
        """
        :param Bitrate: 码率，单位：bps。
        :type Bitrate: int
        :param SamplingRate: 采样率，单位：hz。
        :type SamplingRate: int
        :param Codec: 编码格式。
        :type Codec: str
        """
        self.Bitrate = None
        self.SamplingRate = None
        self.Codec = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.SamplingRate = params.get("SamplingRate")
        self.Codec = params.get("Codec")


class CMEExportInfo(AbstractModel):
    """云剪导出信息。

    """

    def __init__(self):
        """
        :param Owner: 导出的归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Name: 导出的素材名称，不得超过30个字符。
        :type Name: str
        :param Description: 导出的素材信息，不得超过50个字符。
        :type Description: str
        :param ClassPath: 导出的素材分类路径，长度不能超过15字符。
        :type ClassPath: str
        :param TagSet: 导出的素材标签，单个标签不得超过10个字符。
        :type TagSet: list of str
        """
        self.Owner = None
        self.Name = None
        self.Description = None
        self.ClassPath = None
        self.TagSet = None


    def _deserialize(self, params):
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.ClassPath = params.get("ClassPath")
        self.TagSet = params.get("TagSet")


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param Category: 项目类别，取值有：
<li>VIDEO_EDIT：视频编辑。</li>
        :type Category: str
        :param Name: 项目名称，不可超过30个字符。
        :type Name: str
        :param AspectRatio: 画布宽高比，取值有：
<li>16:9；</li>
<li>9:16。</li>
        :type AspectRatio: str
        :param Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        self.Platform = None
        self.Category = None
        self.Name = None
        self.AspectRatio = None
        self.Owner = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.Category = params.get("Category")
        self.Name = params.get("Name")
        self.AspectRatio = params.get("AspectRatio")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))


class CreateProjectResponse(AbstractModel):
    """CreateProject返回参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目 Id。
        :type ProjectId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProjectId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RequestId = params.get("RequestId")


class DeleteLoginStatusRequest(AbstractModel):
    """DeleteLoginStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param UserIds: 用户 Id 列表，N 从 0 开始取值，最大 19。
        :type UserIds: list of str
        """
        self.Platform = None
        self.UserIds = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.UserIds = params.get("UserIds")


class DeleteLoginStatusResponse(AbstractModel):
    """DeleteLoginStatus返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProjectRequest(AbstractModel):
    """DeleteProject请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ProjectId: 项目 Id。
        :type ProjectId: str
        """
        self.Platform = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")


class DeleteProjectResponse(AbstractModel):
    """DeleteProject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeLoginStatusRequest(AbstractModel):
    """DescribeLoginStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param UserIds: 用户 Id 列表，N 从 0 开始取值，最大 19。
        :type UserIds: list of str
        """
        self.Platform = None
        self.UserIds = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.UserIds = params.get("UserIds")


class DescribeLoginStatusResponse(AbstractModel):
    """DescribeLoginStatus返回参数结构体

    """

    def __init__(self):
        """
        :param LoginStatusInfoSet: 用户登录状态列表。
        :type LoginStatusInfoSet: list of LoginStatusInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoginStatusInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoginStatusInfoSet") is not None:
            self.LoginStatusInfoSet = []
            for item in params.get("LoginStatusInfoSet"):
                obj = LoginStatusInfo()
                obj._deserialize(item)
                self.LoginStatusInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ProjectIds: 项目 Id 列表，N 从 0 开始取值，最大 19。
        :type ProjectIds: list of str
        :param AspectRatioSet: 画布宽高比集合。
        :type AspectRatioSet: list of str
        :param CategorySet: 项目类别集合。
        :type CategorySet: list of str
        :param Owner: 项目归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param Offset: 分页返回的起始偏移量，默认值：0。
        :type Offset: int
        :param Limit: 分页返回的记录条数，默认值：10。
        :type Limit: int
        """
        self.Platform = None
        self.ProjectIds = None
        self.AspectRatioSet = None
        self.CategorySet = None
        self.Owner = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectIds = params.get("ProjectIds")
        self.AspectRatioSet = params.get("AspectRatioSet")
        self.CategorySet = params.get("CategorySet")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param ProjectInfoSet: 项目信息列表。
        :type ProjectInfoSet: list of ProjectInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ProjectInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ProjectInfoSet") is not None:
            self.ProjectInfoSet = []
            for item in params.get("ProjectInfoSet"):
                obj = ProjectInfo()
                obj._deserialize(item)
                self.ProjectInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param TaskId: 任务 Id。
        :type TaskId: str
        """
        self.Platform = None
        self.TaskId = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TaskId = params.get("TaskId")


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务状态，取值有：
<li>PROCESSING：处理中：</li>
<li>SUCCESS：成功；</li>
<li>FAIL：失败。</li>
        :type Status: str
        :param Progress: 任务进度，取值为：0~100。
        :type Progress: int
        :param ErrCode: 错误码。
<li>0：成功；</li>
<li>其他值：失败。</li>
        :type ErrCode: int
        :param ErrMsg: 错误信息。
        :type ErrMsg: str
        :param TaskType: 任务类型，取值有：
<li>VIDEO_EDIT_PROJECT_EXPORT：视频编辑项目导出。</li>
        :type TaskType: str
        :param VideoEditProjectOutput: 导出项目输出信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoEditProjectOutput: :class:`tencentcloud.cme.v20191029.models.VideoEditProjectOutput`
        :param CreateTime: 创建时间，格式按照 ISO 8601 标准表示。
        :type CreateTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Progress = None
        self.ErrCode = None
        self.ErrMsg = None
        self.TaskType = None
        self.VideoEditProjectOutput = None
        self.CreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        self.TaskType = params.get("TaskType")
        if params.get("VideoEditProjectOutput") is not None:
            self.VideoEditProjectOutput = VideoEditProjectOutput()
            self.VideoEditProjectOutput._deserialize(params.get("VideoEditProjectOutput"))
        self.CreateTime = params.get("CreateTime")
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ProjectId: 项目 Id。
        :type ProjectId: str
        :param TaskTypeSet: 任务类型集合，取值有：
<li>VIDEO_EDIT_PROJECT_EXPORT：视频编辑项目导出。</li>
        :type TaskTypeSet: list of str
        :param StatusSet: 任务状态集合，取值有：
<li>PROCESSING：处理中；</li>
<li>SUCCESS：成功；</li>
<li>FAIL：失败。</li>
        :type StatusSet: list of str
        :param Offset: 分页返回的起始偏移量，默认值：0。
        :type Offset: int
        :param Limit: 分页返回的记录条数，默认值：10。
        :type Limit: int
        """
        self.Platform = None
        self.ProjectId = None
        self.TaskTypeSet = None
        self.StatusSet = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.TaskTypeSet = params.get("TaskTypeSet")
        self.StatusSet = params.get("StatusSet")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合搜索条件的记录总数。
        :type TotalCount: int
        :param TaskBaseInfoSet: 任务基础信息列表。
        :type TaskBaseInfoSet: list of TaskBaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TaskBaseInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TaskBaseInfoSet") is not None:
            self.TaskBaseInfoSet = []
            for item in params.get("TaskBaseInfoSet"):
                obj = TaskBaseInfo()
                obj._deserialize(item)
                self.TaskBaseInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class Entity(AbstractModel):
    """用于描述资源的归属实体。

    """

    def __init__(self):
        """
        :param Type: 类型，取值有：
<li>PERSON：个人。</li>
        :type Type: str
        :param Id: Id，当 Type=PERSON，取值为用户 Id。
        :type Id: str
        """
        self.Type = None
        self.Id = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Id = params.get("Id")


class ExportVideoEditProjectRequest(AbstractModel):
    """ExportVideoEditProject请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ProjectId: 项目 Id。
        :type ProjectId: str
        :param Definition: 导出模板 Id，目前不支持自定义创建，只支持下面的预置模板 Id。
<li>10：分辨率为 480P，输出视频格式为 MP4；</li>
<li>11：分辨率为 720P，输出视频格式为 MP4；</li>
<li>12：分辨率为 1080P，输出视频格式为 MP4。</li>
        :type Definition: int
        :param ExportDestination: 导出目标。
<li>CME：云剪，即导出为云剪素材；</li>
<li>VOD：云点播，即导出为云点播媒资。</li>
        :type ExportDestination: str
        :param CMEExportInfo: 导出的云剪素材信息。指定 ExportDestination = CME 时有效。
        :type CMEExportInfo: :class:`tencentcloud.cme.v20191029.models.CMEExportInfo`
        :param VODExportInfo: 导出的云点播媒资信息。指定 ExportDestination = VOD 时有效。
        :type VODExportInfo: :class:`tencentcloud.cme.v20191029.models.VODExportInfo`
        """
        self.Platform = None
        self.ProjectId = None
        self.Definition = None
        self.ExportDestination = None
        self.CMEExportInfo = None
        self.VODExportInfo = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.Definition = params.get("Definition")
        self.ExportDestination = params.get("ExportDestination")
        if params.get("CMEExportInfo") is not None:
            self.CMEExportInfo = CMEExportInfo()
            self.CMEExportInfo._deserialize(params.get("CMEExportInfo"))
        if params.get("VODExportInfo") is not None:
            self.VODExportInfo = VODExportInfo()
            self.VODExportInfo._deserialize(params.get("VODExportInfo"))


class ExportVideoEditProjectResponse(AbstractModel):
    """ExportVideoEditProject返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 Id。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ImportMediaToProjectRequest(AbstractModel):
    """ImportMediaToProject请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ProjectId: 项目 Id。
        :type ProjectId: str
        :param VodFileId: 云点播媒资 FileId。
        :type VodFileId: str
        :param Name: 素材名称，不能超过30个字符。
        :type Name: str
        :param PreProcessDefinition: 素材预处理任务模板 ID，取值：
<li>10：进行编辑预处理。</li>
注意：如果填0则不进行处理。
        :type PreProcessDefinition: int
        """
        self.Platform = None
        self.ProjectId = None
        self.VodFileId = None
        self.Name = None
        self.PreProcessDefinition = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.VodFileId = params.get("VodFileId")
        self.Name = params.get("Name")
        self.PreProcessDefinition = params.get("PreProcessDefinition")


class ImportMediaToProjectResponse(AbstractModel):
    """ImportMediaToProject返回参数结构体

    """

    def __init__(self):
        """
        :param MaterialId: 素材 Id。
        :type MaterialId: str
        :param TaskId: 素材预处理任务 ID，如果未指定发起预处理任务则为空。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaterialId = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaterialId = params.get("MaterialId")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class LoginStatusInfo(AbstractModel):
    """登录态信息

    """

    def __init__(self):
        """
        :param UserId: 用户 Id。
        :type UserId: str
        :param Status: 用户登录状态。
<li>Online：在线；</li>
<li>Offline：离线。</li>
        :type Status: str
        """
        self.UserId = None
        self.Status = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Status = params.get("Status")


class MaterialBaseInfo(AbstractModel):
    """素材基础信息。

    """

    def __init__(self):
        """
        :param Name: 素材名称。
        :type Name: str
        :param Description: 描述信息。
        :type Description: str
        :param ClassPath: 分类路径。
        :type ClassPath: str
        :param TagSet: 标签集合。
        :type TagSet: list of str
        :param Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        :param MaterialType: 素材类型。
        :type MaterialType: str
        :param MaterialUrl: 素材 URL。
        :type MaterialUrl: str
        :param VodFileId: 云点播媒资 FileId。
        :type VodFileId: str
        :param CreateTime: 创建时间，格式按照 ISO 8601 标准表示。
        :type CreateTime: str
        """
        self.Name = None
        self.Description = None
        self.ClassPath = None
        self.TagSet = None
        self.Owner = None
        self.MaterialType = None
        self.MaterialUrl = None
        self.VodFileId = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.ClassPath = params.get("ClassPath")
        self.TagSet = params.get("TagSet")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.MaterialType = params.get("MaterialType")
        self.MaterialUrl = params.get("MaterialUrl")
        self.VodFileId = params.get("VodFileId")
        self.CreateTime = params.get("CreateTime")


class MediaMetaData(AbstractModel):
    """文件元信息。

    """

    def __init__(self):
        """
        :param Size: 大小。
        :type Size: int
        :param Container: 容器类型。
        :type Container: str
        :param Bitrate: 视频流码率平均值与音频流码率平均值之和，单位：bps。
        :type Bitrate: int
        :param Height: 视频流高度的最大值，单位：px。
        :type Height: int
        :param Width: 视频流宽度的最大值，单位：px。
        :type Width: int
        :param Duration: 时长，单位：秒。
        :type Duration: float
        :param VideoStreamInfoSet: 视频流信息。
        :type VideoStreamInfoSet: list of VideoStreamInfo
        :param AudioStreamInfoSet: 音频流信息。
        :type AudioStreamInfoSet: list of AudioStreamInfo
        """
        self.Size = None
        self.Container = None
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Duration = None
        self.VideoStreamInfoSet = None
        self.AudioStreamInfoSet = None


    def _deserialize(self, params):
        self.Size = params.get("Size")
        self.Container = params.get("Container")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Duration = params.get("Duration")
        if params.get("VideoStreamInfoSet") is not None:
            self.VideoStreamInfoSet = []
            for item in params.get("VideoStreamInfoSet"):
                obj = VideoStreamInfo()
                obj._deserialize(item)
                self.VideoStreamInfoSet.append(obj)
        if params.get("AudioStreamInfoSet") is not None:
            self.AudioStreamInfoSet = []
            for item in params.get("AudioStreamInfoSet"):
                obj = AudioStreamInfo()
                obj._deserialize(item)
                self.AudioStreamInfoSet.append(obj)


class ModifyProjectRequest(AbstractModel):
    """ModifyProject请求参数结构体

    """

    def __init__(self):
        """
        :param Platform: 平台名称，指定访问的平台。
        :type Platform: str
        :param ProjectId: 项目 Id。
        :type ProjectId: str
        :param Name: 项目名称，不可超过30个字符。
        :type Name: str
        :param Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        self.Platform = None
        self.ProjectId = None
        self.Name = None
        self.Owner = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.Name = params.get("Name")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))


class ModifyProjectResponse(AbstractModel):
    """ModifyProject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ProjectInfo(AbstractModel):
    """项目信息。

    """

    def __init__(self):
        """
        :param ProjectId: 项目 Id。
        :type ProjectId: str
        :param Name: 项目名称。
        :type Name: str
        :param AspectRatio: 画布宽高比。
        :type AspectRatio: str
        :param Category: 项目类别。
        :type Category: str
        :param Owner: 归属者。
        :type Owner: :class:`tencentcloud.cme.v20191029.models.Entity`
        """
        self.ProjectId = None
        self.Name = None
        self.AspectRatio = None
        self.Category = None
        self.Owner = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Name = params.get("Name")
        self.AspectRatio = params.get("AspectRatio")
        self.Category = params.get("Category")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))


class TaskBaseInfo(AbstractModel):
    """任务基础信息。

    """

    def __init__(self):
        """
        :param TaskId: 任务 Id。
        :type TaskId: str
        :param TaskType: 任务类型，取值有：
<li>VIDEO_EDIT_PROJECT_EXPORT：项目导出。</li>
        :type TaskType: str
        :param Status: 任务状态，取值有：
<li>PROCESSING：处理中：</li>
<li>SUCCESS：成功；</li>
<li>FAIL：失败。</li>
        :type Status: str
        :param Progress: 任务进度，取值为：0~100。
        :type Progress: int
        :param ErrCode: 错误码。
<li>0：成功；</li>
<li>其他值：失败。</li>
        :type ErrCode: int
        :param ErrMsg: 错误信息。
        :type ErrMsg: str
        :param CreateTime: 创建时间，格式按照 ISO 8601 标准表示。
        :type CreateTime: str
        """
        self.TaskId = None
        self.TaskType = None
        self.Status = None
        self.Progress = None
        self.ErrCode = None
        self.ErrMsg = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        self.CreateTime = params.get("CreateTime")


class VODExportInfo(AbstractModel):
    """云点播导出信息。

    """

    def __init__(self):
        """
        :param Name: 导出的媒资名称。
        :type Name: str
        :param ClassId: 导出的媒资分类 Id。
        :type ClassId: int
        """
        self.Name = None
        self.ClassId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ClassId = params.get("ClassId")


class VideoEditProjectOutput(AbstractModel):
    """项目导出信息。

    """

    def __init__(self):
        """
        :param VodFileId: 云点播媒资 FileId。
        :type VodFileId: str
        :param URL: 导出的媒资 URL。
        :type URL: str
        :param MetaData: 元信息。
        :type MetaData: :class:`tencentcloud.cme.v20191029.models.MediaMetaData`
        :param MaterialBaseInfo: 素材基础信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaterialBaseInfo: :class:`tencentcloud.cme.v20191029.models.MaterialBaseInfo`
        """
        self.VodFileId = None
        self.URL = None
        self.MetaData = None
        self.MaterialBaseInfo = None


    def _deserialize(self, params):
        self.VodFileId = params.get("VodFileId")
        self.URL = params.get("URL")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        if params.get("MaterialBaseInfo") is not None:
            self.MaterialBaseInfo = MaterialBaseInfo()
            self.MaterialBaseInfo._deserialize(params.get("MaterialBaseInfo"))


class VideoStreamInfo(AbstractModel):
    """视频流信息。

    """

    def __init__(self):
        """
        :param Bitrate: 码率，单位：bps。
        :type Bitrate: int
        :param Height: 高度，单位：px。
        :type Height: int
        :param Width: 宽度，单位：px。
        :type Width: int
        :param Codec: 编码格式。
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