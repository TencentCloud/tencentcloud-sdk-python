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


class AddDelayLiveStreamRequest(AbstractModel):
    """AddDelayLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 应用名称。
        :type AppName: str
        :param DomainName: 您的加速域名。
        :type DomainName: str
        :param StreamName: 流名称。
        :type StreamName: str
        :param DelayTime: 延播时间，单位：秒，上限：600秒。
        :type DelayTime: int
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.DelayTime = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.DelayTime = params.get("DelayTime")


class AddDelayLiveStreamResponse(AbstractModel):
    """AddDelayLiveStream返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddLiveWatermarkRequest(AbstractModel):
    """AddLiveWatermark请求参数结构体

    """

    def __init__(self):
        """
        :param PictureUrl: 水印图片url。
        :type PictureUrl: str
        :param WatermarkName: 水印名称。
        :type WatermarkName: str
        :param XPosition: 显示位置,X轴偏移。
        :type XPosition: int
        :param YPosition: 显示位置,Y轴偏移。
        :type YPosition: int
        """
        self.PictureUrl = None
        self.WatermarkName = None
        self.XPosition = None
        self.YPosition = None


    def _deserialize(self, params):
        self.PictureUrl = params.get("PictureUrl")
        self.WatermarkName = params.get("WatermarkName")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")


class AddLiveWatermarkResponse(AbstractModel):
    """AddLiveWatermark返回参数结构体

    """

    def __init__(self):
        """
        :param WatermarkId: 水印ID。
        :type WatermarkId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WatermarkId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.RequestId = params.get("RequestId")


class CreateLiveRecordRequest(AbstractModel):
    """CreateLiveRecord请求参数结构体

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param AppName: 直播流所属应用名称。
        :type AppName: str
        :param DomainName: 推流域名。多域名推流必须设置。
        :type DomainName: str
        :param StartTime: 任务起始时间，中国标准时间，需要URLEncode。如 2017-01-01 10:10:01，编码为：2017-01-01+10%3a10%3a01。录制视频为精彩视频时，忽略此字段。
        :type StartTime: str
        :param EndTime: 任务结束时间，中国标准时间，需要URLEncode。如 2017-01-01 10:30:01，编码为：2017-01-01+10%3a30%3a01。若指定精彩视频录制，结束时间不超过当前时间+30分钟，如果超过或小于起始时间，则实际结束时间为当前时间+30分钟。
        :type EndTime: str
        :param RecordType: 录制类型。不区分大小写。
“video” : 音视频录制【默认】。
“audio” : 纯音频录制。
        :type RecordType: str
        :param FileFormat: 录制文件格式。不区分大小写。其值为：
“flv”,“hls”,”mp4”,“aac”,”mp3”，默认“flv”。
        :type FileFormat: str
        :param Highlight: 精彩视频标志。0：普通视频【默认】；1：精彩视频。
        :type Highlight: int
        :param MixStream: A+B=C混流标志。0：非A+B=C混流录制【默认】；1：标示为A+B=C混流录制。
        :type MixStream: int
        :param StreamParam: 录制流参数，当前支持以下参数： 
interval 录制分片时长，单位 秒，0 - 7200
storage_time 录制文件存储时长，单位 秒
eg. interval=3600&storage_time=7200
注：参数需要url encode。
        :type StreamParam: str
        """
        self.StreamName = None
        self.AppName = None
        self.DomainName = None
        self.StartTime = None
        self.EndTime = None
        self.RecordType = None
        self.FileFormat = None
        self.Highlight = None
        self.MixStream = None
        self.StreamParam = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RecordType = params.get("RecordType")
        self.FileFormat = params.get("FileFormat")
        self.Highlight = params.get("Highlight")
        self.MixStream = params.get("MixStream")
        self.StreamParam = params.get("StreamParam")


class CreateLiveRecordResponse(AbstractModel):
    """CreateLiveRecord返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID，全局唯一标识录制任务。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreatePullStreamConfigRequest(AbstractModel):
    """CreatePullStreamConfig请求参数结构体

    """

    def __init__(self):
        """
        :param FromUrl: 源Url。
        :type FromUrl: str
        :param ToUrl: 目的Url，目前限制该目标地址为腾讯域名。
        :type ToUrl: str
        :param AreaId: 区域id,1-深圳,2-上海，3-天津,4-香港。
        :type AreaId: int
        :param IspId: 运营商id,1-电信,2-移动,3-联通,4-其他,AreaId为4的时候,IspId只能为其他。
        :type IspId: int
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间，注意：
1. 结束时间必须大于开始时间；
2. 结束时间和开始时间必须大于当前时间；
3. 结束时间 和 开始时间 间隔必须小于七天。
        :type EndTime: str
        """
        self.FromUrl = None
        self.ToUrl = None
        self.AreaId = None
        self.IspId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.FromUrl = params.get("FromUrl")
        self.ToUrl = params.get("ToUrl")
        self.AreaId = params.get("AreaId")
        self.IspId = params.get("IspId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class CreatePullStreamConfigResponse(AbstractModel):
    """CreatePullStreamConfig返回参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置成功后的id。
        :type ConfigId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ConfigId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.RequestId = params.get("RequestId")


class DeleteLiveRecordRequest(AbstractModel):
    """DeleteLiveRecord请求参数结构体

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param TaskId: 任务ID，全局唯一标识录制任务。
        :type TaskId: int
        """
        self.StreamName = None
        self.TaskId = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TaskId = params.get("TaskId")


class DeleteLiveRecordResponse(AbstractModel):
    """DeleteLiveRecord返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveWatermarkRequest(AbstractModel):
    """DeleteLiveWatermark请求参数结构体

    """

    def __init__(self):
        """
        :param WatermarkId: 水印ID。
        :type WatermarkId: int
        """
        self.WatermarkId = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")


class DeleteLiveWatermarkResponse(AbstractModel):
    """DeleteLiveWatermark返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeLivePlayAuthKeyRequest(AbstractModel):
    """DescribeLivePlayAuthKey请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


class DescribeLivePlayAuthKeyResponse(AbstractModel):
    """DescribeLivePlayAuthKey返回参数结构体

    """

    def __init__(self):
        """
        :param PlayAuthKeyInfo: 播放鉴权key信息。
        :type PlayAuthKeyInfo: :class:`tencentcloud.live.v20180801.models.PlayAuthKeyInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PlayAuthKeyInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayAuthKeyInfo") is not None:
            self.PlayAuthKeyInfo = PlayAuthKeyInfo()
            self.PlayAuthKeyInfo._deserialize(params.get("PlayAuthKeyInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLivePushAuthKeyRequest(AbstractModel):
    """DescribeLivePushAuthKey请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


class DescribeLivePushAuthKeyResponse(AbstractModel):
    """DescribeLivePushAuthKey返回参数结构体

    """

    def __init__(self):
        """
        :param PushAuthKeyInfo: 推流鉴权key信息。
        :type PushAuthKeyInfo: :class:`tencentcloud.live.v20180801.models.PushAuthKeyInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PushAuthKeyInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PushAuthKeyInfo") is not None:
            self.PushAuthKeyInfo = PushAuthKeyInfo()
            self.PushAuthKeyInfo._deserialize(params.get("PushAuthKeyInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamOnlineInfoRequest(AbstractModel):
    """DescribeLiveStreamOnlineInfo请求参数结构体

    """

    def __init__(self):
        """
        :param PageNum: 取得第几页。
默认值：1
        :type PageNum: int
        :param PageSize: 分页大小。

最大值：100。
取值范围：1~100 之前的任意整数。
默认值：10
        :type PageSize: int
        :param Status: 0:未开始推流 1:正在推流 2:服务出错 3:已关闭。
        :type Status: int
        :param StreamName: 流名称。
        :type StreamName: str
        """
        self.PageNum = None
        self.PageSize = None
        self.Status = None
        self.StreamName = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.Status = params.get("Status")
        self.StreamName = params.get("StreamName")


class DescribeLiveStreamOnlineInfoResponse(AbstractModel):
    """DescribeLiveStreamOnlineInfo返回参数结构体

    """

    def __init__(self):
        """
        :param PageNum: 分页的页码。
        :type PageNum: int
        :param PageSize: 每页大小
        :type PageSize: int
        :param TotalNum: 符合条件的总个数。
        :type TotalNum: int
        :param TotalPage: 总页数。
        :type TotalPage: int
        :param StreamInfoList: 流信息列表
        :type StreamInfoList: list of StreamInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.StreamInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        if params.get("StreamInfoList") is not None:
            self.StreamInfoList = []
            for item in params.get("StreamInfoList"):
                obj = StreamInfo()
                obj._deserialize(item)
                self.StreamInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamOnlineListRequest(AbstractModel):
    """DescribeLiveStreamOnlineList请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 您的加速域名。
        :type DomainName: str
        :param AppName: 应用名称。
        :type AppName: str
        :param PageNum: 取得第几页，默认1。
        :type PageNum: int
        :param PageSize: 每页大小，最大100。 
取值：1~100之前的任意整数。
默认值：10
        :type PageSize: int
        """
        self.DomainName = None
        self.AppName = None
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")


class DescribeLiveStreamOnlineListResponse(AbstractModel):
    """DescribeLiveStreamOnlineList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalNum: 符合条件的总个数。
        :type TotalNum: int
        :param TotalPage: 总页数。
        :type TotalPage: int
        :param PageNum: 分页的页码。
        :type PageNum: int
        :param PageSize: 每页显示的条数。
        :type PageSize: int
        :param OnlineInfo: 正在推送流的信息列表
        :type OnlineInfo: list of StreamOnlineInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.TotalPage = None
        self.PageNum = None
        self.PageSize = None
        self.OnlineInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        if params.get("OnlineInfo") is not None:
            self.OnlineInfo = []
            for item in params.get("OnlineInfo"):
                obj = StreamOnlineInfo()
                obj._deserialize(item)
                self.OnlineInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamPublishedListRequest(AbstractModel):
    """DescribeLiveStreamPublishedList请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 您的域名。
        :type DomainName: str
        :param EndTime: 结束时间。
UTC 格式，例如：2016-06-30T19:00:00Z。
不超过当前时间。
        :type EndTime: str
        :param StartTime: 起始时间。 
UTC 格式，例如：2016-06-29T19:00:00Z。
和当前时间相隔不超过7天。
        :type StartTime: str
        :param AppName: 直播流所属应用名称。
        :type AppName: str
        :param PageNum: 取得第几页。
默认值：1
        :type PageNum: int
        :param PageSize: 分页大小。

最大值：100。
取值范围：1~100 之前的任意整数。
默认值：10
        :type PageSize: int
        """
        self.DomainName = None
        self.EndTime = None
        self.StartTime = None
        self.AppName = None
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.AppName = params.get("AppName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")


class DescribeLiveStreamPublishedListResponse(AbstractModel):
    """DescribeLiveStreamPublishedList返回参数结构体

    """

    def __init__(self):
        """
        :param PublishInfo: 推流记录信息。
        :type PublishInfo: list of StreamName
        :param PageNum: 分页的页码。
        :type PageNum: int
        :param PageSize: 每页大小
        :type PageSize: int
        :param TotalNum: 符合条件的总个数。
        :type TotalNum: int
        :param TotalPage: 总页数。
        :type TotalPage: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PublishInfo = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PublishInfo") is not None:
            self.PublishInfo = []
            for item in params.get("PublishInfo"):
                obj = StreamName()
                obj._deserialize(item)
                self.PublishInfo.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamStateRequest(AbstractModel):
    """DescribeLiveStreamState请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 应用名称。
        :type AppName: str
        :param DomainName: 您的加速域名。
        :type DomainName: str
        :param StreamName: 流名称。
        :type StreamName: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")


class DescribeLiveStreamStateResponse(AbstractModel):
    """DescribeLiveStreamState返回参数结构体

    """

    def __init__(self):
        """
        :param StreamState: 流状态
        :type StreamState: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StreamState = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StreamState = params.get("StreamState")
        self.RequestId = params.get("RequestId")


class DescribeLiveWatermarksRequest(AbstractModel):
    """DescribeLiveWatermarks请求参数结构体

    """


class DescribeLiveWatermarksResponse(AbstractModel):
    """DescribeLiveWatermarks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalNum: 水印总个数。
        :type TotalNum: int
        :param WatermarkList: 水印信息列表。
        :type WatermarkList: list of WatermarkInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.WatermarkList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("WatermarkList") is not None:
            self.WatermarkList = []
            for item in params.get("WatermarkList"):
                obj = WatermarkInfo()
                obj._deserialize(item)
                self.WatermarkList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePullStreamConfigsRequest(AbstractModel):
    """DescribePullStreamConfigs请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置id。
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")


class DescribePullStreamConfigsResponse(AbstractModel):
    """DescribePullStreamConfigs返回参数结构体

    """

    def __init__(self):
        """
        :param PullStreamConfigs: 拉流配置。
        :type PullStreamConfigs: list of PullStreamConfig
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PullStreamConfigs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PullStreamConfigs") is not None:
            self.PullStreamConfigs = []
            for item in params.get("PullStreamConfigs"):
                obj = PullStreamConfig()
                obj._deserialize(item)
                self.PullStreamConfigs.append(obj)
        self.RequestId = params.get("RequestId")


class DropLiveStreamRequest(AbstractModel):
    """DropLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param DomainName: 您的加速域名。
        :type DomainName: str
        :param AppName: 应用名称。
        :type AppName: str
        """
        self.StreamName = None
        self.DomainName = None
        self.AppName = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")


class DropLiveStreamResponse(AbstractModel):
    """DropLiveStream返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ForbidLiveStreamRequest(AbstractModel):
    """ForbidLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 应用名称。
        :type AppName: str
        :param DomainName: 您的加速域名。
        :type DomainName: str
        :param StreamName: 流名称。
        :type StreamName: str
        :param ResumeTime: 恢复流的时间。UTC 格式，例如：2018-11-29T19:00:00Z。
注意：默认禁播90天，且最长支持禁播90天。
        :type ResumeTime: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.ResumeTime = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.ResumeTime = params.get("ResumeTime")


class ForbidLiveStreamResponse(AbstractModel):
    """ForbidLiveStream返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLivePlayAuthKeyRequest(AbstractModel):
    """ModifyLivePlayAuthKey请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        :param Enable: 是否启用，0：关闭，1：启用。
        :type Enable: int
        :param AuthKey: 鉴权key。
        :type AuthKey: str
        :param AuthDelta: 有效时间，单位：秒。
        :type AuthDelta: int
        """
        self.DomainName = None
        self.Enable = None
        self.AuthKey = None
        self.AuthDelta = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.AuthKey = params.get("AuthKey")
        self.AuthDelta = params.get("AuthDelta")


class ModifyLivePlayAuthKeyResponse(AbstractModel):
    """ModifyLivePlayAuthKey返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLivePushAuthKeyRequest(AbstractModel):
    """ModifyLivePushAuthKey请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param Enable: 是否启用，0：关闭，1：启用。
        :type Enable: int
        :param MasterAuthKey: 主鉴权key。
        :type MasterAuthKey: str
        :param BackupAuthKey: 备鉴权key。
        :type BackupAuthKey: str
        :param AuthDelta: 有效时间，单位：秒。
        :type AuthDelta: int
        """
        self.DomainName = None
        self.Enable = None
        self.MasterAuthKey = None
        self.BackupAuthKey = None
        self.AuthDelta = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.MasterAuthKey = params.get("MasterAuthKey")
        self.BackupAuthKey = params.get("BackupAuthKey")
        self.AuthDelta = params.get("AuthDelta")


class ModifyLivePushAuthKeyResponse(AbstractModel):
    """ModifyLivePushAuthKey返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPullStreamConfigRequest(AbstractModel):
    """ModifyPullStreamConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置id。
        :type ConfigId: str
        :param FromUrl: 源Url。
        :type FromUrl: str
        :param ToUrl: 目的Url。
        :type ToUrl: str
        :param AreaId: 区域id,1-深圳,2-上海，3-天津,4-香港。如有改动，需同时传入IspId。
        :type AreaId: int
        :param IspId: 运营商id,1-电信,2-移动,3-联通,4-其他,AreaId为4的时候,IspId只能为其他。如有改动，需同时传入AreaId。
        :type IspId: int
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间，注意：
1. 结束时间必须大于开始时间；
2. 结束时间和开始时间必须大于当前时间；
3. 结束时间 和 开始时间 间隔必须小于七天。
        :type EndTime: str
        """
        self.ConfigId = None
        self.FromUrl = None
        self.ToUrl = None
        self.AreaId = None
        self.IspId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.FromUrl = params.get("FromUrl")
        self.ToUrl = params.get("ToUrl")
        self.AreaId = params.get("AreaId")
        self.IspId = params.get("IspId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class ModifyPullStreamConfigResponse(AbstractModel):
    """ModifyPullStreamConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPullStreamStatusRequest(AbstractModel):
    """ModifyPullStreamStatus请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigIds: 配置id列表。
        :type ConfigIds: list of str
        :param Status: 目标状态。0无效，2正在运行，4暂停。
        :type Status: str
        """
        self.ConfigIds = None
        self.Status = None


    def _deserialize(self, params):
        self.ConfigIds = params.get("ConfigIds")
        self.Status = params.get("Status")


class ModifyPullStreamStatusResponse(AbstractModel):
    """ModifyPullStreamStatus返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PlayAuthKeyInfo(AbstractModel):
    """播放鉴权key信息

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        :param Enable: 是否启用，0：关闭，1：启用。
        :type Enable: int
        :param AuthKey: 鉴权key。
        :type AuthKey: str
        :param AuthDelta: 有效时间，单位：秒。
        :type AuthDelta: int
        """
        self.DomainName = None
        self.Enable = None
        self.AuthKey = None
        self.AuthDelta = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.AuthKey = params.get("AuthKey")
        self.AuthDelta = params.get("AuthDelta")


class PublishTime(AbstractModel):
    """推流时间

    """

    def __init__(self):
        """
        :param PublishTime: 推流时间
UTC 格式，例如：2018-06-29T19:00:00Z。
        :type PublishTime: str
        """
        self.PublishTime = None


    def _deserialize(self, params):
        self.PublishTime = params.get("PublishTime")


class PullStreamConfig(AbstractModel):
    """拉流配置

    """

    def __init__(self):
        """
        :param ConfigId: 拉流配置Id。
        :type ConfigId: str
        :param FromUrl: 源Url。
        :type FromUrl: str
        :param ToUrl: 目的Url。
        :type ToUrl: str
        :param AreaName: 区域名。
        :type AreaName: str
        :param IspName: 运营商名。
        :type IspName: str
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param Status: 0无效，1初始状态，2正在运行，3拉起失败，4暂停。
        :type Status: str
        """
        self.ConfigId = None
        self.FromUrl = None
        self.ToUrl = None
        self.AreaName = None
        self.IspName = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.FromUrl = params.get("FromUrl")
        self.ToUrl = params.get("ToUrl")
        self.AreaName = params.get("AreaName")
        self.IspName = params.get("IspName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")


class PushAuthKeyInfo(AbstractModel):
    """推流鉴权key信息

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        :param Enable: 是否启用，0：关闭，1：启用。
        :type Enable: int
        :param MasterAuthKey: 主鉴权key。
        :type MasterAuthKey: str
        :param BackupAuthKey: 备鉴权key。
        :type BackupAuthKey: str
        :param AuthDelta: 有效时间，单位：秒。
        :type AuthDelta: int
        """
        self.DomainName = None
        self.Enable = None
        self.MasterAuthKey = None
        self.BackupAuthKey = None
        self.AuthDelta = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.MasterAuthKey = params.get("MasterAuthKey")
        self.BackupAuthKey = params.get("BackupAuthKey")
        self.AuthDelta = params.get("AuthDelta")


class ResumeDelayLiveStreamRequest(AbstractModel):
    """ResumeDelayLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 应用名称。
        :type AppName: str
        :param DomainName: 您的加速域名。
        :type DomainName: str
        :param StreamName: 流名称。
        :type StreamName: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")


class ResumeDelayLiveStreamResponse(AbstractModel):
    """ResumeDelayLiveStream返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResumeLiveStreamRequest(AbstractModel):
    """ResumeLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 应用名称。
        :type AppName: str
        :param DomainName: 您的加速域名。
        :type DomainName: str
        :param StreamName: 流名称。
        :type StreamName: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")


class ResumeLiveStreamResponse(AbstractModel):
    """ResumeLiveStream返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetLiveWatermarkStatusRequest(AbstractModel):
    """SetLiveWatermarkStatus请求参数结构体

    """

    def __init__(self):
        """
        :param WatermarkId: 水印ID。
        :type WatermarkId: int
        :param Status: 状态。0：停用，1:启用
        :type Status: int
        """
        self.WatermarkId = None
        self.Status = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.Status = params.get("Status")


class SetLiveWatermarkStatusResponse(AbstractModel):
    """SetLiveWatermarkStatus返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopLiveRecordRequest(AbstractModel):
    """StopLiveRecord请求参数结构体

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param TaskId: 任务ID，全局唯一标识录制任务。
        :type TaskId: int
        """
        self.StreamName = None
        self.TaskId = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TaskId = params.get("TaskId")


class StopLiveRecordResponse(AbstractModel):
    """StopLiveRecord返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StreamInfo(AbstractModel):
    """推流信息

    """

    def __init__(self):
        """
        :param AppName: 直播流所属应用名称
        :type AppName: str
        :param CreateMode: 创建模式
        :type CreateMode: str
        :param CreateTime: 创建时间，如: 2018-07-13 14:48:23
        :type CreateTime: str
        :param Status: 流状态
        :type Status: int
        :param StreamId: 流id
        :type StreamId: str
        :param StreamName: 流名称
        :type StreamName: str
        :param WaterMarkId: 水印id
        :type WaterMarkId: str
        """
        self.AppName = None
        self.CreateMode = None
        self.CreateTime = None
        self.Status = None
        self.StreamId = None
        self.StreamName = None
        self.WaterMarkId = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.CreateMode = params.get("CreateMode")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.StreamId = params.get("StreamId")
        self.StreamName = params.get("StreamName")
        self.WaterMarkId = params.get("WaterMarkId")


class StreamName(AbstractModel):
    """流名称列表

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        """
        self.StreamName = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")


class StreamOnlineInfo(AbstractModel):
    """查询当前正在推流的信息

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param PublishTimeList: 推流时间列表
        :type PublishTimeList: list of PublishTime
        """
        self.StreamName = None
        self.PublishTimeList = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        if params.get("PublishTimeList") is not None:
            self.PublishTimeList = []
            for item in params.get("PublishTimeList"):
                obj = PublishTime()
                obj._deserialize(item)
                self.PublishTimeList.append(obj)


class UpdateLiveWatermarkRequest(AbstractModel):
    """UpdateLiveWatermark请求参数结构体

    """

    def __init__(self):
        """
        :param WatermarkId: 水印ID。
        :type WatermarkId: int
        :param PictureUrl: 水印图片url。
        :type PictureUrl: str
        :param XPosition: 显示位置，X轴偏移。
        :type XPosition: int
        :param YPosition: 显示位置，Y轴偏移。
        :type YPosition: int
        :param WatermarkName: 水印名称。
        :type WatermarkName: str
        """
        self.WatermarkId = None
        self.PictureUrl = None
        self.XPosition = None
        self.YPosition = None
        self.WatermarkName = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.PictureUrl = params.get("PictureUrl")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.WatermarkName = params.get("WatermarkName")


class UpdateLiveWatermarkResponse(AbstractModel):
    """UpdateLiveWatermark返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class WatermarkInfo(AbstractModel):
    """水印信息

    """

    def __init__(self):
        """
        :param WatermarkId: 水印ID。
        :type WatermarkId: int
        :param PictureUrl: 水印图片url。
        :type PictureUrl: str
        :param XPosition: 显示位置，X轴偏移。
        :type XPosition: int
        :param YPosition: 显示位置，Y轴偏移。
        :type YPosition: int
        :param WatermarkName: 水印名称。
        :type WatermarkName: str
        :param Status: 当前状态。0：未使用，1:使用中。
        :type Status: int
        :param CreateTime: 添加时间。
        :type CreateTime: str
        """
        self.WatermarkId = None
        self.PictureUrl = None
        self.XPosition = None
        self.YPosition = None
        self.WatermarkName = None
        self.Status = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.PictureUrl = params.get("PictureUrl")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.WatermarkName = params.get("WatermarkName")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")