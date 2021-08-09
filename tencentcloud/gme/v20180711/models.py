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


class AppStatisticsItem(AbstractModel):
    """应用用量统计数据

    """

    def __init__(self):
        """
        :param RealtimeSpeechStatisticsItem: 实时语音统计数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type RealtimeSpeechStatisticsItem: :class:`tencentcloud.gme.v20180711.models.RealTimeSpeechStatisticsItem`\n        :param VoiceMessageStatisticsItem: 语音消息统计数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type VoiceMessageStatisticsItem: :class:`tencentcloud.gme.v20180711.models.VoiceMessageStatisticsItem`\n        :param VoiceFilterStatisticsItem: 语音过滤统计数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type VoiceFilterStatisticsItem: :class:`tencentcloud.gme.v20180711.models.VoiceFilterStatisticsItem`\n        :param Date: 统计时间\n        :type Date: str\n        """
        self.RealtimeSpeechStatisticsItem = None
        self.VoiceMessageStatisticsItem = None
        self.VoiceFilterStatisticsItem = None
        self.Date = None


    def _deserialize(self, params):
        if params.get("RealtimeSpeechStatisticsItem") is not None:
            self.RealtimeSpeechStatisticsItem = RealTimeSpeechStatisticsItem()
            self.RealtimeSpeechStatisticsItem._deserialize(params.get("RealtimeSpeechStatisticsItem"))
        if params.get("VoiceMessageStatisticsItem") is not None:
            self.VoiceMessageStatisticsItem = VoiceMessageStatisticsItem()
            self.VoiceMessageStatisticsItem._deserialize(params.get("VoiceMessageStatisticsItem"))
        if params.get("VoiceFilterStatisticsItem") is not None:
            self.VoiceFilterStatisticsItem = VoiceFilterStatisticsItem()
            self.VoiceFilterStatisticsItem._deserialize(params.get("VoiceFilterStatisticsItem"))
        self.Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationDataStatistics(AbstractModel):
    """应用统计数据

    """

    def __init__(self):
        """
        :param BizId: 应用ID\n        :type BizId: int\n        :param DauDataNum: Dau统计项数目\n        :type DauDataNum: int\n        :param DauDataMainland: 大陆地区Dau统计数据，单位人\n        :type DauDataMainland: list of StatisticsItem\n        :param DauDataOversea: 海外地区Dau统计数据，单位人\n        :type DauDataOversea: list of StatisticsItem\n        :param DauDataSum: 大陆和海外地区Dau统计数据汇总，单位人\n        :type DauDataSum: list of StatisticsItem\n        :param DurationDataNum: 实时语音时长统计项数目\n        :type DurationDataNum: int\n        :param DurationDataMainland: 大陆地区实时语音时长统计数据，单位分钟\n        :type DurationDataMainland: list of StatisticsItem\n        :param DurationDataOversea: 海外地区实时语音时长统计数据，单位分钟\n        :type DurationDataOversea: list of StatisticsItem\n        :param DurationDataSum: 大陆和海外地区实时语音时长统计数据汇总，单位分钟\n        :type DurationDataSum: list of StatisticsItem\n        :param PcuDataNum: Pcu统计项数目\n        :type PcuDataNum: int\n        :param PcuDataMainland: 大陆地区Pcu统计数据，单位人\n        :type PcuDataMainland: list of StatisticsItem\n        :param PcuDataOversea: 海外地区Pcu统计数据，单位人\n        :type PcuDataOversea: list of StatisticsItem\n        :param PcuDataSum: 大陆和海外地区Pcu统计数据汇总，单位人\n        :type PcuDataSum: list of StatisticsItem\n        """
        self.BizId = None
        self.DauDataNum = None
        self.DauDataMainland = None
        self.DauDataOversea = None
        self.DauDataSum = None
        self.DurationDataNum = None
        self.DurationDataMainland = None
        self.DurationDataOversea = None
        self.DurationDataSum = None
        self.PcuDataNum = None
        self.PcuDataMainland = None
        self.PcuDataOversea = None
        self.PcuDataSum = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.DauDataNum = params.get("DauDataNum")
        if params.get("DauDataMainland") is not None:
            self.DauDataMainland = []
            for item in params.get("DauDataMainland"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DauDataMainland.append(obj)
        if params.get("DauDataOversea") is not None:
            self.DauDataOversea = []
            for item in params.get("DauDataOversea"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DauDataOversea.append(obj)
        if params.get("DauDataSum") is not None:
            self.DauDataSum = []
            for item in params.get("DauDataSum"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DauDataSum.append(obj)
        self.DurationDataNum = params.get("DurationDataNum")
        if params.get("DurationDataMainland") is not None:
            self.DurationDataMainland = []
            for item in params.get("DurationDataMainland"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DurationDataMainland.append(obj)
        if params.get("DurationDataOversea") is not None:
            self.DurationDataOversea = []
            for item in params.get("DurationDataOversea"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DurationDataOversea.append(obj)
        if params.get("DurationDataSum") is not None:
            self.DurationDataSum = []
            for item in params.get("DurationDataSum"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.DurationDataSum.append(obj)
        self.PcuDataNum = params.get("PcuDataNum")
        if params.get("PcuDataMainland") is not None:
            self.PcuDataMainland = []
            for item in params.get("PcuDataMainland"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.PcuDataMainland.append(obj)
        if params.get("PcuDataOversea") is not None:
            self.PcuDataOversea = []
            for item in params.get("PcuDataOversea"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.PcuDataOversea.append(obj)
        if params.get("PcuDataSum") is not None:
            self.PcuDataSum = []
            for item in params.get("PcuDataSum"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self.PcuDataSum.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppRequest(AbstractModel):
    """CreateApp请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 应用名称\n        :type AppName: str\n        :param ProjectId: 腾讯云项目ID，默认为0，表示默认项目\n        :type ProjectId: int\n        :param EngineList: 需要支持的引擎列表，默认全选。\n        :type EngineList: list of str\n        :param RegionList: 服务区域列表，默认全选。\n        :type RegionList: list of str\n        :param RealtimeSpeechConf: 实时语音服务配置数据\n        :type RealtimeSpeechConf: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`\n        :param VoiceMessageConf: 语音消息及转文本服务配置数据\n        :type VoiceMessageConf: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`\n        :param VoiceFilterConf: 语音分析服务配置数据\n        :type VoiceFilterConf: :class:`tencentcloud.gme.v20180711.models.VoiceFilterConf`\n        :param Tags: 需要添加的标签列表\n        :type Tags: list of Tag\n        """
        self.AppName = None
        self.ProjectId = None
        self.EngineList = None
        self.RegionList = None
        self.RealtimeSpeechConf = None
        self.VoiceMessageConf = None
        self.VoiceFilterConf = None
        self.Tags = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.ProjectId = params.get("ProjectId")
        self.EngineList = params.get("EngineList")
        self.RegionList = params.get("RegionList")
        if params.get("RealtimeSpeechConf") is not None:
            self.RealtimeSpeechConf = RealtimeSpeechConf()
            self.RealtimeSpeechConf._deserialize(params.get("RealtimeSpeechConf"))
        if params.get("VoiceMessageConf") is not None:
            self.VoiceMessageConf = VoiceMessageConf()
            self.VoiceMessageConf._deserialize(params.get("VoiceMessageConf"))
        if params.get("VoiceFilterConf") is not None:
            self.VoiceFilterConf = VoiceFilterConf()
            self.VoiceFilterConf._deserialize(params.get("VoiceFilterConf"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppResponse(AbstractModel):
    """CreateApp的输出参数

    """

    def __init__(self):
        """
        :param BizId: 应用ID，由后台自动生成。\n        :type BizId: int\n        :param AppName: 应用名称，透传输入参数的AppName\n        :type AppName: str\n        :param ProjectId: 项目ID，透传输入的ProjectId\n        :type ProjectId: int\n        :param SecretKey: 应用密钥，GME SDK初始化时使用\n        :type SecretKey: str\n        :param CreateTime: 服务创建时间戳\n        :type CreateTime: int\n        :param RealtimeSpeechConf: 实时语音服务配置数据\n        :type RealtimeSpeechConf: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`\n        :param VoiceMessageConf: 语音消息及转文本服务配置数据\n        :type VoiceMessageConf: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`\n        :param VoiceFilterConf: 语音分析服务配置数据\n        :type VoiceFilterConf: :class:`tencentcloud.gme.v20180711.models.VoiceFilterConf`\n        """
        self.BizId = None
        self.AppName = None
        self.ProjectId = None
        self.SecretKey = None
        self.CreateTime = None
        self.RealtimeSpeechConf = None
        self.VoiceMessageConf = None
        self.VoiceFilterConf = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.AppName = params.get("AppName")
        self.ProjectId = params.get("ProjectId")
        self.SecretKey = params.get("SecretKey")
        self.CreateTime = params.get("CreateTime")
        if params.get("RealtimeSpeechConf") is not None:
            self.RealtimeSpeechConf = RealtimeSpeechConf()
            self.RealtimeSpeechConf._deserialize(params.get("RealtimeSpeechConf"))
        if params.get("VoiceMessageConf") is not None:
            self.VoiceMessageConf = VoiceMessageConf()
            self.VoiceMessageConf._deserialize(params.get("VoiceMessageConf"))
        if params.get("VoiceFilterConf") is not None:
            self.VoiceFilterConf = VoiceFilterConf()
            self.VoiceFilterConf._deserialize(params.get("VoiceFilterConf"))


class DescribeAppStatisticsRequest(AbstractModel):
    """DescribeAppStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param BizId: GME应用ID\n        :type BizId: int\n        :param StartDate: 数据开始时间，东八区时间，格式: 年-月-日，如: 2018-07-13\n        :type StartDate: str\n        :param EndDate: 数据结束时间，东八区时间，格式: 年-月-日，如: 2018-07-13\n        :type EndDate: str\n        :param Services: 要查询的服务列表，取值：RealTimeSpeech/VoiceMessage/VoiceFilter\n        :type Services: list of str\n        """
        self.BizId = None
        self.StartDate = None
        self.EndDate = None
        self.Services = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Services = params.get("Services")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppStatisticsResponse(AbstractModel):
    """获取应用用量统计数据输出参数

    """

    def __init__(self):
        """
        :param AppStatistics: 应用用量统计数据\n        :type AppStatistics: list of AppStatisticsItem\n        """
        self.AppStatistics = None


    def _deserialize(self, params):
        if params.get("AppStatistics") is not None:
            self.AppStatistics = []
            for item in params.get("AppStatistics"):
                obj = AppStatisticsItem()
                obj._deserialize(item)
                self.AppStatistics.append(obj)


class DescribeApplicationDataRequest(AbstractModel):
    """DescribeApplicationData请求参数结构体

    """

    def __init__(self):
        """
        :param BizId: 应用ID\n        :type BizId: int\n        :param StartDate: 数据开始时间，格式为 年-月-日，如: 2018-07-13\n        :type StartDate: str\n        :param EndDate: 数据结束时间，格式为 年-月-日，如: 2018-07-13\n        :type EndDate: str\n        """
        self.BizId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationDataResponse(AbstractModel):
    """DescribeApplicationData返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 应用统计数据\n        :type Data: :class:`tencentcloud.gme.v20180711.models.ApplicationDataStatistics`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ApplicationDataStatistics()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeFilterResultListRequest(AbstractModel):
    """DescribeFilterResultList请求参数结构体

    """

    def __init__(self):
        """
        :param BizId: 应用ID\n        :type BizId: int\n        :param StartDate: 开始时间，格式为 年-月-日，如: 2018-07-11\n        :type StartDate: str\n        :param EndDate: 结束时间，格式为 年-月-日，如: 2018-07-11\n        :type EndDate: str\n        :param Offset: 偏移量，默认值为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认值为10，最大值为100。\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFilterResultListResponse(AbstractModel):
    """DescribeFilterResultList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 过滤结果总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Data: 当前分页过滤结果列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: list of VoiceFilterInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param BizId: 应用ID\n        :type BizId: int\n        :param FileId: 文件ID\n        :type FileId: str\n        """
        self.BizId = None
        self.FileId = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFilterResultResponse(AbstractModel):
    """DescribeFilterResult返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 过滤结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: :class:`tencentcloud.gme.v20180711.models.VoiceFilterInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = VoiceFilterInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRoomInfoRequest(AbstractModel):
    """DescribeRoomInfo请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: 应用ID，登录[控制台 - 服务管理](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID\n        :type SdkAppId: int\n        :param RoomIds: 房间号列表，最大不能超过10个\n        :type RoomIds: list of int non-negative\n        """
        self.SdkAppId = None
        self.RoomIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomIds = params.get("RoomIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomInfoResponse(AbstractModel):
    """DescribeRoomInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 操作结果, 0成功, 非0失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: int\n        :param RoomUsers: 房间用户信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type RoomUsers: list of RoomUser\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RoomUsers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        if params.get("RoomUsers") is not None:
            self.RoomUsers = []
            for item in params.get("RoomUsers"):
                obj = RoomUser()
                obj._deserialize(item)
                self.RoomUsers.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeScanResult(AbstractModel):
    """语音检测结果返回

    """

    def __init__(self):
        """
        :param Code: 业务返回码\n        :type Code: int\n        :param DataId: 数据唯一 ID\n        :type DataId: str\n        :param ScanFinishTime: 检测完成的时间戳\n        :type ScanFinishTime: int\n        :param HitFlag: 是否违规\n        :type HitFlag: bool\n        :param Live: 是否为流\n        :type Live: bool\n        :param Msg: 业务返回描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Msg: str\n        :param ScanPiece: 检测结果，Code 为 0 时返回
注意：此字段可能返回 null，表示取不到有效值。\n        :type ScanPiece: list of ScanPiece\n        :param ScanStartTime: 提交检测的时间戳\n        :type ScanStartTime: int\n        :param Scenes: 语音检测场景，对应请求时的 Scene\n        :type Scenes: list of str\n        :param TaskId: 语音检测任务 ID，由后台分配\n        :type TaskId: str\n        :param Url: 文件或接流地址\n        :type Url: str\n        :param Status: 检测任务执行结果状态，分别为：
<li>Start: 任务开始</li>
<li>Success: 成功结束</li>
<li>Error: 异常</li>\n        :type Status: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanResultListRequest(AbstractModel):
    """DescribeScanResultList请求参数结构体

    """

    def __init__(self):
        """
        :param BizId: 应用 ID，登录[控制台](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID\n        :type BizId: int\n        :param TaskIdList: 查询的任务 ID 列表，任务 ID 列表最多支持 100 个。\n        :type TaskIdList: list of str\n        :param Limit: 任务返回结果数量，默认10，上限500。大文件任务忽略此参数，返回全量结果\n        :type Limit: int\n        """
        self.BizId = None
        self.TaskIdList = None
        self.Limit = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.TaskIdList = params.get("TaskIdList")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanResultListResponse(AbstractModel):
    """DescribeScanResultList返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 要查询的语音检测任务的结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: list of DescribeScanResult\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeUserInAndOutTimeRequest(AbstractModel):
    """DescribeUserInAndOutTime请求参数结构体

    """

    def __init__(self):
        """
        :param BizId: 应用ID\n        :type BizId: int\n        :param RoomId: 房间ID\n        :type RoomId: int\n        :param UserId: 用户ID\n        :type UserId: int\n        """
        self.BizId = None
        self.RoomId = None
        self.UserId = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.RoomId = params.get("RoomId")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserInAndOutTimeResponse(AbstractModel):
    """DescribeUserInAndOutTime返回参数结构体

    """

    def __init__(self):
        """
        :param InOutList: 用户在房间得进出时间列表\n        :type InOutList: list of InOutTimeInfo\n        :param Duration: 用户在房间中总时长\n        :type Duration: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InOutList = None
        self.Duration = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InOutList") is not None:
            self.InOutList = []
            for item in params.get("InOutList"):
                obj = InOutTimeInfo()
                obj._deserialize(item)
                self.InOutList.append(obj)
        self.Duration = params.get("Duration")
        self.RequestId = params.get("RequestId")


class InOutTimeInfo(AbstractModel):
    """用户进出房间信息

    """

    def __init__(self):
        """
        :param StartTime: 进入房间时间\n        :type StartTime: int\n        :param EndTime: 退出房间时间\n        :type EndTime: int\n        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppStatusRequest(AbstractModel):
    """ModifyAppStatus请求参数结构体

    """

    def __init__(self):
        """
        :param BizId: 应用ID，创建应用后由后台生成并返回。\n        :type BizId: int\n        :param Status: 应用状态，取值：open/close\n        :type Status: str\n        """
        self.BizId = None
        self.Status = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppStatusResponse(AbstractModel):
    """ModifyAppStatus接口输出参数

    """

    def __init__(self):
        """
        :param BizId: GME应用ID\n        :type BizId: int\n        :param Status: 应用状态，取值：open/close\n        :type Status: str\n        """
        self.BizId = None
        self.Status = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.Status = params.get("Status")


class ModifyRoomInfoRequest(AbstractModel):
    """ModifyRoomInfo请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: 应用ID，登录[控制台 - 服务管理](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID\n        :type SdkAppId: int\n        :param RoomId: 房间id\n        :type RoomId: int\n        :param OperationType: 301 启动推流
302 停止推流
303 重置RTMP连接\n        :type OperationType: int\n        """
        self.SdkAppId = None
        self.RoomId = None
        self.OperationType = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.OperationType = params.get("OperationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoomInfoResponse(AbstractModel):
    """ModifyRoomInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 操作结果, 0成功, 非0失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: int\n        :param ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.ErrMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.ErrMsg = params.get("ErrMsg")
        self.RequestId = params.get("RequestId")


class RealTimeSpeechStatisticsItem(AbstractModel):
    """实时语音用量统计数据

    """

    def __init__(self):
        """
        :param MainLandDau: 大陆地区DAU\n        :type MainLandDau: int\n        :param MainLandPcu: 大陆地区PCU\n        :type MainLandPcu: int\n        :param MainLandDuration: 大陆地区总使用时长，单位为min\n        :type MainLandDuration: int\n        :param OverseaDau: 海外地区DAU\n        :type OverseaDau: int\n        :param OverseaPcu: 海外地区PCU\n        :type OverseaPcu: int\n        :param OverseaDuration: 海外地区总使用时长，单位为min\n        :type OverseaDuration: int\n        """
        self.MainLandDau = None
        self.MainLandPcu = None
        self.MainLandDuration = None
        self.OverseaDau = None
        self.OverseaPcu = None
        self.OverseaDuration = None


    def _deserialize(self, params):
        self.MainLandDau = params.get("MainLandDau")
        self.MainLandPcu = params.get("MainLandPcu")
        self.MainLandDuration = params.get("MainLandDuration")
        self.OverseaDau = params.get("OverseaDau")
        self.OverseaPcu = params.get("OverseaPcu")
        self.OverseaDuration = params.get("OverseaDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealtimeSpeechConf(AbstractModel):
    """实时语音配置数据

    """

    def __init__(self):
        """
        :param Status: 实时语音服务开关，取值：open/close\n        :type Status: str\n        :param Quality: 实时语音音质类型，取值：high-高音质，ordinary-普通音质。默认高音质。普通音质仅白名单开放，如需要普通音质，请联系腾讯云商务。\n        :type Quality: str\n        """
        self.Status = None
        self.Quality = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Quality = params.get("Quality")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoomUser(AbstractModel):
    """房间内用户信息

    """

    def __init__(self):
        """
        :param RoomId: 房间id\n        :type RoomId: int\n        :param Uins: 房间里用户uin列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Uins: list of int non-negative\n        """
        self.RoomId = None
        self.Uins = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.Uins = params.get("Uins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanDetail(AbstractModel):
    """语音检测详情

    """

    def __init__(self):
        """
        :param Label: 违规场景，参照<a href="https://cloud.tencent.com/document/product/607/37622#Label_Value">Label</a>定义\n        :type Label: str\n        :param Rate: 该场景下概率[0.00,100.00],分值越大违规概率越高\n        :type Rate: str\n        :param KeyWord: 违规关键字\n        :type KeyWord: str\n        :param StartTime: 关键字在音频的开始时间，从0开始的偏移量，单位为毫秒\n        :type StartTime: int\n        :param EndTime: 关键字在音频的结束时间，从0开始的偏移量,，单位为毫秒\n        :type EndTime: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanPiece(AbstractModel):
    """语音检测结果，Code 为 0 时返回

    """

    def __init__(self):
        """
        :param DumpUrl: 流检测时返回，音频转存地址，保留30min
注意：此字段可能返回 null，表示取不到有效值。\n        :type DumpUrl: str\n        :param HitFlag: 是否违规\n        :type HitFlag: bool\n        :param MainType: 违规主要类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type MainType: str\n        :param ScanDetail: 语音检测详情\n        :type ScanDetail: list of ScanDetail\n        :param RoomId: gme实时语音房间ID，透传任务传入时的RoomId
注意：此字段可能返回 null，表示取不到有效值。\n        :type RoomId: str\n        :param OpenId: gme实时语音用户ID，透传任务传入时的OpenId
注意：此字段可能返回 null，表示取不到有效值。\n        :type OpenId: str\n        :param Info: 备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Info: str\n        :param Offset: 流检测时分片在流中的偏移时间，单位毫秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type Offset: int\n        :param Duration: 流检测时分片时长
注意：此字段可能返回 null，表示取不到有效值。\n        :type Duration: int\n        :param PieceStartTime: 分片开始检测时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type PieceStartTime: int\n        """
        self.DumpUrl = None
        self.HitFlag = None
        self.MainType = None
        self.ScanDetail = None
        self.RoomId = None
        self.OpenId = None
        self.Info = None
        self.Offset = None
        self.Duration = None
        self.PieceStartTime = None


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
        self.Info = params.get("Info")
        self.Offset = params.get("Offset")
        self.Duration = params.get("Duration")
        self.PieceStartTime = params.get("PieceStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanVoiceRequest(AbstractModel):
    """ScanVoice请求参数结构体

    """

    def __init__(self):
        """
        :param BizId: 应用ID，登录[控制台 - 服务管理](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID\n        :type BizId: int\n        :param Scenes: 语音检测场景，参数值目前要求为 default。 预留场景设置： 谩骂、色情、涉政、广告、暴恐、违禁等场景，<a href="#Label_Value">具体取值见上述 Label 说明。</a>\n        :type Scenes: list of str\n        :param Live: 是否为直播流。值为 false 时表示普通语音文件检测；为 true 时表示语音流检测。\n        :type Live: bool\n        :param Tasks: 语音检测任务列表，列表最多支持100个检测任务。结构体中包含：
<li>DataId：数据的唯一ID</li>
<li>Url：数据文件的url，为 urlencode 编码，流式则为拉流地址</li>\n        :type Tasks: list of Task\n        :param Callback: 异步检测结果回调地址，具体见上述<a href="#Callback_Declare">回调相关说明</a>。（说明：该字段为空时，必须通过接口(查询语音检测结果)获取检测结果）。\n        :type Callback: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanVoiceResponse(AbstractModel):
    """ScanVoice返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 语音检测返回。Data 字段是 JSON 数组，每一个元素包含：<li>DataId： 请求中对应的 DataId。</li>
<li>TaskID ：该检测任务的 ID，用于轮询语音检测结果。</li>\n        :type Data: list of ScanVoiceResult\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param DataId: 数据ID\n        :type DataId: str\n        :param TaskId: 任务ID\n        :type TaskId: str\n        """
        self.DataId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatisticsItem(AbstractModel):
    """用量数据单元

    """

    def __init__(self):
        """
        :param StatDate: 日期，格式为年-月-日，如2018-07-13\n        :type StatDate: str\n        :param Data: 统计值\n        :type Data: int\n        """
        self.StatDate = None
        self.Data = None


    def _deserialize(self, params):
        self.StatDate = params.get("StatDate")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签列表

    """

    def __init__(self):
        """
        :param TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagKey: str\n        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagValue: str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """语音检测任务列表

    """

    def __init__(self):
        """
        :param DataId: 数据的唯一ID\n        :type DataId: str\n        :param Url: 数据文件的url，为 urlencode 编码，流式则为拉流地址\n        :type Url: str\n        :param RoomId: gme实时语音房间ID，通过gme实时语音进行语音分析时输入\n        :type RoomId: str\n        :param OpenId: gme实时语音用户ID，通过gme实时语音进行语音分析时输入\n        :type OpenId: str\n        """
        self.DataId = None
        self.Url = None
        self.RoomId = None
        self.OpenId = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.Url = params.get("Url")
        self.RoomId = params.get("RoomId")
        self.OpenId = params.get("OpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceFilter(AbstractModel):
    """过滤结果

    """

    def __init__(self):
        """
        :param Type: 过滤类型，1：政治，2：色情，3：涉毒，4：谩骂
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: int\n        :param Word: 过滤命中关键词
注意：此字段可能返回 null，表示取不到有效值。\n        :type Word: str\n        """
        self.Type = None
        self.Word = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Word = params.get("Word")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceFilterConf(AbstractModel):
    """语音过滤服务配置数据

    """

    def __init__(self):
        """
        :param Status: 语音过滤服务开关，取值：open/close\n        :type Status: str\n        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceFilterInfo(AbstractModel):
    """语音文件过滤详情

    """

    def __init__(self):
        """
        :param BizId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type BizId: int\n        :param FileId: 文件ID，表示文件唯一ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileId: str\n        :param FileName: 文件名
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileName: str\n        :param OpenId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type OpenId: str\n        :param Timestamp: 数据创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type Timestamp: str\n        :param Data: 过滤结果列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: list of VoiceFilter\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceFilterRequest(AbstractModel):
    """VoiceFilter请求参数结构体

    """

    def __init__(self):
        """
        :param BizId: 应用ID，登录[控制台](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID\n        :type BizId: int\n        :param FileId: 文件ID，表示文件唯一ID\n        :type FileId: str\n        :param FileName: 文件名\n        :type FileName: str\n        :param FileUrl: 文件url，urlencode编码，FileUrl和FileContent二选一\n        :type FileUrl: str\n        :param FileContent: 文件内容，base64编码，FileUrl和FileContent二选一\n        :type FileContent: str\n        :param OpenId: 用户ID\n        :type OpenId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceFilterResponse(AbstractModel):
    """VoiceFilter返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VoiceFilterStatisticsItem(AbstractModel):
    """语音过滤用量统计数据

    """

    def __init__(self):
        """
        :param Duration: 语音过滤总时长\n        :type Duration: int\n        """
        self.Duration = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceMessageConf(AbstractModel):
    """离线语音服务配置数据

    """

    def __init__(self):
        """
        :param Status: 离线语音服务开关，取值：open/close\n        :type Status: str\n        :param Language: 离线语音支持语种，取值： all-全部，cnen-中英文。默认为中英文\n        :type Language: str\n        """
        self.Status = None
        self.Language = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Language = params.get("Language")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceMessageStatisticsItem(AbstractModel):
    """语音消息用量统计信息

    """

    def __init__(self):
        """
        :param Dau: 离线语音DAU\n        :type Dau: int\n        """
        self.Dau = None


    def _deserialize(self, params):
        self.Dau = params.get("Dau")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        