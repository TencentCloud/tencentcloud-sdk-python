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


class DescribeFilterResultListRequest(AbstractModel):
    """DescribeFilterResultList请求参数结构体

    """

    def __init__(self):
        """
        :param BizId: 应用ID
        :type BizId: int
        :param StartDate: 开始时间，格式为 年-月-日，如: 2018-07-11
        :type StartDate: str
        :param EndDate: 结束时间，格式为 年-月-日，如: 2018-07-11
        :type EndDate: str
        :param Offset: 偏移量，默认值为0。
        :type Offset: int
        :param Limit: 返回数量，默认值为10，最大值为100。
        :type Limit: int
        """
        self.BizId = None
        self.StartDate = None
        self.EndDate = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeFilterResultListResponse(AbstractModel):
    """DescribeFilterResultList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 过滤结果总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Data: 当前分页过滤结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of VoiceFilterInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = VoiceFilterInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFilterResultRequest(AbstractModel):
    """DescribeFilterResult请求参数结构体

    """

    def __init__(self):
        """
        :param BizId: 应用ID
        :type BizId: int
        :param FileId: 文件ID
        :type FileId: str
        """
        self.BizId = None
        self.FileId = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.FileId = params.get("FileId")


class DescribeFilterResultResponse(AbstractModel):
    """DescribeFilterResult返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 过滤结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.gme.v20180711.models.VoiceFilterInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = VoiceFilterInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeScanResult(AbstractModel):
    """语音检测结果返回

    """

    def __init__(self):
        """
        :param Code: 业务返回码
        :type Code: int
        :param DataId: 数据唯一 ID
        :type DataId: str
        :param ScanFinishTime: 检测完成的时间戳
        :type ScanFinishTime: int
        :param HitFlag: 是否违规
        :type HitFlag: bool
        :param Live: 是否为流
        :type Live: bool
        :param Msg: 业务返回描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param ScanPiece: 检测结果，Code 为 0 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanPiece: list of ScanPiece
        :param ScanStartTime: 提交检测的时间戳
        :type ScanStartTime: int
        :param Scenes: 语音检测场景，对应请求时的 Scene
        :type Scenes: list of str
        :param TaskId: 语音检测任务 ID，由后台分配
        :type TaskId: str
        :param Url: 文件或接流地址
        :type Url: str
        :param Status: 检测任务执行结果状态，分别为：
<li>Start: 任务开始</li>
<li>Success: 成功结束</li>
<li>Error: 异常</li>
        :type Status: str
        """
        self.Code = None
        self.DataId = None
        self.ScanFinishTime = None
        self.HitFlag = None
        self.Live = None
        self.Msg = None
        self.ScanPiece = None
        self.ScanStartTime = None
        self.Scenes = None
        self.TaskId = None
        self.Url = None
        self.Status = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.DataId = params.get("DataId")
        self.ScanFinishTime = params.get("ScanFinishTime")
        self.HitFlag = params.get("HitFlag")
        self.Live = params.get("Live")
        self.Msg = params.get("Msg")
        if params.get("ScanPiece") is not None:
            self.ScanPiece = []
            for item in params.get("ScanPiece"):
                obj = ScanPiece()
                obj._deserialize(item)
                self.ScanPiece.append(obj)
        self.ScanStartTime = params.get("ScanStartTime")
        self.Scenes = params.get("Scenes")
        self.TaskId = params.get("TaskId")
        self.Url = params.get("Url")
        self.Status = params.get("Status")


class DescribeScanResultListRequest(AbstractModel):
    """DescribeScanResultList请求参数结构体

    """

    def __init__(self):
        """
        :param BizId: 应用 ID，在控制台统一创建。
        :type BizId: int
        :param TaskIdList: 查询的任务 ID 列表，任务 ID 列表最多支持 100 个。
        :type TaskIdList: list of str
        """
        self.BizId = None
        self.TaskIdList = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.TaskIdList = params.get("TaskIdList")


class DescribeScanResultListResponse(AbstractModel):
    """DescribeScanResultList返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 要查询的语音检测任务的结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DescribeScanResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DescribeScanResult()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class ScanDetail(AbstractModel):
    """语音检测详情

    """

    def __init__(self):
        """
        :param Label: 违规场景，参照Label定义
        :type Label: str
        :param Rate: 该场景下概率[0.00,100.00],分值越大违规概率越高
        :type Rate: str
        :param KeyWord: 违规关键字
        :type KeyWord: str
        :param StartTime: 关键字在音频的开始时间，从0开始的偏移量，单位为毫秒
        :type StartTime: int
        :param EndTime: 关键字在音频的结束时间，从0开始的偏移量,，单位为毫秒
        :type EndTime: int
        """
        self.Label = None
        self.Rate = None
        self.KeyWord = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Rate = params.get("Rate")
        self.KeyWord = params.get("KeyWord")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class ScanPiece(AbstractModel):
    """语音检测结果，Code 为 0 时返回

    """

    def __init__(self):
        """
        :param DumpUrl: 流检测时返回，音频转存地址，保留30min
注意：此字段可能返回 null，表示取不到有效值。
        :type DumpUrl: str
        :param HitFlag: 是否违规
        :type HitFlag: bool
        :param MainType: 违规主要类型
注意：此字段可能返回 null，表示取不到有效值。
        :type MainType: str
        :param ScanDetail: 语音检测详情
        :type ScanDetail: list of ScanDetail
        :param RoomId: gme实时语音房间id，透传任务传入时的RoomId
注意：此字段可能返回 null，表示取不到有效值。
        :type RoomId: str
        :param OpenId: gme实时语音用户id，透传任务传入时的OpenId
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        """
        self.DumpUrl = None
        self.HitFlag = None
        self.MainType = None
        self.ScanDetail = None
        self.RoomId = None
        self.OpenId = None


    def _deserialize(self, params):
        self.DumpUrl = params.get("DumpUrl")
        self.HitFlag = params.get("HitFlag")
        self.MainType = params.get("MainType")
        if params.get("ScanDetail") is not None:
            self.ScanDetail = []
            for item in params.get("ScanDetail"):
                obj = ScanDetail()
                obj._deserialize(item)
                self.ScanDetail.append(obj)
        self.RoomId = params.get("RoomId")
        self.OpenId = params.get("OpenId")


class ScanVoiceRequest(AbstractModel):
    """ScanVoice请求参数结构体

    """

    def __init__(self):
        """
        :param BizId: 应用ID，登录控制台创建应用得到的AppID。
        :type BizId: int
        :param Scenes: 语音检测场景，参数值目前要求为 default。 预留场景设置： 谩骂、色情、涉政、广告、暴恐、违禁等场景，<a href="#Label_Value">具体取值见上述 Label 说明。</a>
        :type Scenes: list of str
        :param Live: 是否为直播流。值为 false 时表示普通语音文件检测；为 true 时表示语音流检测。
        :type Live: bool
        :param Tasks: 语音检测任务列表，列表最多支持100个检测任务。结构体中包含：
<li>DataId：数据的唯一ID</li>
<li>Url：数据文件的url，为 urlencode 编码，流式则为拉流地址</li>
        :type Tasks: list of Task
        :param Callback: 异步检测结果回调地址，具体见上述<a href="#Callback_Declare">回调相关说明</a>。（说明：该字段为空时，必须通过接口(查询语音检测结果)获取检测结果）。
        :type Callback: str
        """
        self.BizId = None
        self.Scenes = None
        self.Live = None
        self.Tasks = None
        self.Callback = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.Scenes = params.get("Scenes")
        self.Live = params.get("Live")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.Callback = params.get("Callback")


class ScanVoiceResponse(AbstractModel):
    """ScanVoice返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 语音检测返回。Data 字段是 JSON 数组，每一个元素包含：<li>DataId： 请求中对应的 DataId。</li>
<li>TaskID ：该检测任务的 ID，用于轮询语音检测结果。</li>
        :type Data: list of ScanVoiceResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ScanVoiceResult()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class ScanVoiceResult(AbstractModel):
    """语音检测返回结果

    """

    def __init__(self):
        """
        :param DataId: 数据ID
        :type DataId: str
        :param TaskId: 任务ID
        :type TaskId: str
        """
        self.DataId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.TaskId = params.get("TaskId")


class Task(AbstractModel):
    """语音检测任务列表

    """

    def __init__(self):
        """
        :param DataId: 数据的唯一ID
        :type DataId: str
        :param Url: 数据文件的url，为 urlencode 编码，流式则为拉流地址
        :type Url: str
        :param RoomId: gme实时语音房间id，通过gme实时语音进行语音分析时输入
        :type RoomId: str
        :param OpenId: gme实时语音用户id，通过gme实时语音进行语音分析时输入
        :type OpenId: str
        """
        self.DataId = None
        self.Url = None
        self.RoomId = None
        self.OpenId = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.Url = params.get("Url")
        self.RoomId = params.get("RoomId")
        self.OpenId = params.get("OpenId")


class VoiceFilter(AbstractModel):
    """过滤结果

    """

    def __init__(self):
        """
        :param Type: 过滤类型，1：政治，2：色情，3：涉毒，4：谩骂
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param Word: 过滤命中关键词
注意：此字段可能返回 null，表示取不到有效值。
        :type Word: str
        """
        self.Type = None
        self.Word = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Word = params.get("Word")


class VoiceFilterInfo(AbstractModel):
    """语音文件过滤详情

    """

    def __init__(self):
        """
        :param BizId: 应用id
注意：此字段可能返回 null，表示取不到有效值。
        :type BizId: int
        :param FileId: 文件id，表示文件唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        :param FileName: 文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param OpenId: 用户id
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param Timestamp: 数据创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param Data: 过滤结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of VoiceFilter
        """
        self.BizId = None
        self.FileId = None
        self.FileName = None
        self.OpenId = None
        self.Timestamp = None
        self.Data = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.FileId = params.get("FileId")
        self.FileName = params.get("FileName")
        self.OpenId = params.get("OpenId")
        self.Timestamp = params.get("Timestamp")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = VoiceFilter()
                obj._deserialize(item)
                self.Data.append(obj)


class VoiceFilterRequest(AbstractModel):
    """VoiceFilter请求参数结构体

    """

    def __init__(self):
        """
        :param BizId: 应用ID，登录[控制台](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID
        :type BizId: int
        :param FileId: 文件ID，表示文件唯一ID
        :type FileId: str
        :param FileName: 文件名
        :type FileName: str
        :param FileUrl: 文件url，urlencode编码，FileUrl和FileContent二选一
        :type FileUrl: str
        :param FileContent: 文件内容，base64编码，FileUrl和FileContent二选一
        :type FileContent: str
        :param OpenId: 用户ID
        :type OpenId: str
        """
        self.BizId = None
        self.FileId = None
        self.FileName = None
        self.FileUrl = None
        self.FileContent = None
        self.OpenId = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.FileId = params.get("FileId")
        self.FileName = params.get("FileName")
        self.FileUrl = params.get("FileUrl")
        self.FileContent = params.get("FileContent")
        self.OpenId = params.get("OpenId")


class VoiceFilterResponse(AbstractModel):
    """VoiceFilter返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")