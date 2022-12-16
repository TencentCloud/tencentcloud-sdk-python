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


class AgeDetectTask(AbstractModel):
    """年龄语音识别子任务

    """

    def __init__(self):
        r"""
        :param DataId: 数据唯一ID
        :type DataId: str
        :param Url: 数据文件的url，为 urlencode 编码,音频文件格式支持的类型：.wav、.m4a、.amr、.mp3、.aac、.wma、.ogg
        :type Url: str
        """
        self.DataId = None
        self.Url = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgeDetectTaskResult(AbstractModel):
    """年龄语音任务结果

    """

    def __init__(self):
        r"""
        :param DataId: 数据唯一ID
        :type DataId: str
        :param Url: 数据文件的url
        :type Url: str
        :param Status: 任务状态，0: 已创建，1:运行中，2:正常结束，3:异常结束，4:运行超时
        :type Status: int
        :param Age: 任务结果：0: 成年，1:未成年，100:未知
        :type Age: int
        """
        self.DataId = None
        self.Url = None
        self.Status = None
        self.Age = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.Age = params.get("Age")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppStatisticsItem(AbstractModel):
    """应用用量统计数据

    """

    def __init__(self):
        r"""
        :param RealtimeSpeechStatisticsItem: 实时语音统计数据
注意：此字段可能返回 null，表示取不到有效值。
        :type RealtimeSpeechStatisticsItem: :class:`tencentcloud.gme.v20180711.models.RealTimeSpeechStatisticsItem`
        :param VoiceMessageStatisticsItem: 语音消息统计数据
注意：此字段可能返回 null，表示取不到有效值。
        :type VoiceMessageStatisticsItem: :class:`tencentcloud.gme.v20180711.models.VoiceMessageStatisticsItem`
        :param VoiceFilterStatisticsItem: 语音过滤统计数据
注意：此字段可能返回 null，表示取不到有效值。
        :type VoiceFilterStatisticsItem: :class:`tencentcloud.gme.v20180711.models.VoiceFilterStatisticsItem`
        :param Date: 统计时间
        :type Date: str
        :param AudioTextStatisticsItem: 录音转文本用量统计数据
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioTextStatisticsItem: :class:`tencentcloud.gme.v20180711.models.AudioTextStatisticsItem`
        :param StreamTextStatisticsItem: 流式转文本用量数据
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamTextStatisticsItem: :class:`tencentcloud.gme.v20180711.models.StreamTextStatisticsItem`
        :param OverseaTextStatisticsItem: 海外转文本用量数据
注意：此字段可能返回 null，表示取不到有效值。
        :type OverseaTextStatisticsItem: :class:`tencentcloud.gme.v20180711.models.OverseaTextStatisticsItem`
        :param RealtimeTextStatisticsItem: 实时语音转文本用量数据
注意：此字段可能返回 null，表示取不到有效值。
        :type RealtimeTextStatisticsItem: :class:`tencentcloud.gme.v20180711.models.RealtimeTextStatisticsItem`
        """
        self.RealtimeSpeechStatisticsItem = None
        self.VoiceMessageStatisticsItem = None
        self.VoiceFilterStatisticsItem = None
        self.Date = None
        self.AudioTextStatisticsItem = None
        self.StreamTextStatisticsItem = None
        self.OverseaTextStatisticsItem = None
        self.RealtimeTextStatisticsItem = None


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
        if params.get("AudioTextStatisticsItem") is not None:
            self.AudioTextStatisticsItem = AudioTextStatisticsItem()
            self.AudioTextStatisticsItem._deserialize(params.get("AudioTextStatisticsItem"))
        if params.get("StreamTextStatisticsItem") is not None:
            self.StreamTextStatisticsItem = StreamTextStatisticsItem()
            self.StreamTextStatisticsItem._deserialize(params.get("StreamTextStatisticsItem"))
        if params.get("OverseaTextStatisticsItem") is not None:
            self.OverseaTextStatisticsItem = OverseaTextStatisticsItem()
            self.OverseaTextStatisticsItem._deserialize(params.get("OverseaTextStatisticsItem"))
        if params.get("RealtimeTextStatisticsItem") is not None:
            self.RealtimeTextStatisticsItem = RealtimeTextStatisticsItem()
            self.RealtimeTextStatisticsItem._deserialize(params.get("RealtimeTextStatisticsItem"))
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
        r"""
        :param BizId: 应用ID
        :type BizId: int
        :param DauDataNum: Dau统计项数目
        :type DauDataNum: int
        :param DauDataMainland: 大陆地区Dau统计数据，单位人
        :type DauDataMainland: list of StatisticsItem
        :param DauDataOversea: 海外地区Dau统计数据，单位人
        :type DauDataOversea: list of StatisticsItem
        :param DauDataSum: 大陆和海外地区Dau统计数据汇总，单位人
        :type DauDataSum: list of StatisticsItem
        :param DurationDataNum: 实时语音时长统计项数目
        :type DurationDataNum: int
        :param DurationDataMainland: 大陆地区实时语音时长统计数据，单位分钟
        :type DurationDataMainland: list of StatisticsItem
        :param DurationDataOversea: 海外地区实时语音时长统计数据，单位分钟
        :type DurationDataOversea: list of StatisticsItem
        :param DurationDataSum: 大陆和海外地区实时语音时长统计数据汇总，单位分钟
        :type DurationDataSum: list of StatisticsItem
        :param PcuDataNum: Pcu统计项数目
        :type PcuDataNum: int
        :param PcuDataMainland: 大陆地区Pcu统计数据，单位人
        :type PcuDataMainland: list of StatisticsItem
        :param PcuDataOversea: 海外地区Pcu统计数据，单位人
        :type PcuDataOversea: list of StatisticsItem
        :param PcuDataSum: 大陆和海外地区Pcu统计数据汇总，单位人
        :type PcuDataSum: list of StatisticsItem
        """
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
        


class ApplicationList(AbstractModel):
    """获取应用列表返回

    """

    def __init__(self):
        r"""
        :param ServiceConf: 服务开关状态
        :type ServiceConf: :class:`tencentcloud.gme.v20180711.models.ServiceStatus`
        :param BizId: 应用ID(AppID)
        :type BizId: int
        :param AppName: 应用名称
        :type AppName: str
        :param ProjectId: 项目ID，默认为0
        :type ProjectId: int
        :param AppStatus: 应用状态，返回0表示正常，1表示关闭，2表示欠费停服，3表示欠费回收
        :type AppStatus: int
        :param CreateTime: 创建时间，Unix时间戳格式
        :type CreateTime: int
        :param AppType: 应用类型，无需关注此数值
        :type AppType: int
        """
        self.ServiceConf = None
        self.BizId = None
        self.AppName = None
        self.ProjectId = None
        self.AppStatus = None
        self.CreateTime = None
        self.AppType = None


    def _deserialize(self, params):
        if params.get("ServiceConf") is not None:
            self.ServiceConf = ServiceStatus()
            self.ServiceConf._deserialize(params.get("ServiceConf"))
        self.BizId = params.get("BizId")
        self.AppName = params.get("AppName")
        self.ProjectId = params.get("ProjectId")
        self.AppStatus = params.get("AppStatus")
        self.CreateTime = params.get("CreateTime")
        self.AppType = params.get("AppType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTextStatisticsItem(AbstractModel):
    """录音转文本用量统计数据

    """

    def __init__(self):
        r"""
        :param Data: 统计值，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: float
        """
        self.Data = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgeDetectTaskRequest(AbstractModel):
    """CreateAgeDetectTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizId: 应用id
        :type BizId: int
        :param Tasks: 语音检测子任务列表，列表最多支持100个检测子任务。结构体中包含：
<li>DataId：数据的唯一ID</li>
<li>Url：数据文件的url，为 urlencode 编码，流式则为拉流地址</li>
        :type Tasks: list of AgeDetectTask
        :param Callback: 任务结束时gme后台会自动触发回调
        :type Callback: str
        """
        self.BizId = None
        self.Tasks = None
        self.Callback = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = AgeDetectTask()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgeDetectTaskResponse(AbstractModel):
    """CreateAgeDetectTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 本次任务提交后唯一id，用于获取任务运行结果
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateAppRequest(AbstractModel):
    """CreateApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param AppName: 应用名称
        :type AppName: str
        :param ProjectId: 腾讯云项目ID，默认为0，表示默认项目
        :type ProjectId: int
        :param EngineList: 需要支持的引擎列表，默认全选。
        :type EngineList: list of str
        :param RegionList: 服务区域列表，默认全选。
        :type RegionList: list of str
        :param RealtimeSpeechConf: 实时语音服务配置数据
        :type RealtimeSpeechConf: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`
        :param VoiceMessageConf: 语音消息及转文本服务配置数据
        :type VoiceMessageConf: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`
        :param VoiceFilterConf: 语音分析服务配置数据
        :type VoiceFilterConf: :class:`tencentcloud.gme.v20180711.models.VoiceFilterConf`
        :param Tags: 需要添加的标签列表
        :type Tags: list of Tag
        """
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
        


class CreateAppResp(AbstractModel):
    """CreateApp的输出参数

    """

    def __init__(self):
        r"""
        :param BizId: 应用ID，由后台自动生成。
        :type BizId: int
        :param AppName: 应用名称，透传输入参数的AppName
        :type AppName: str
        :param ProjectId: 项目ID，透传输入的ProjectId
        :type ProjectId: int
        :param SecretKey: 应用密钥，GME SDK初始化时使用
        :type SecretKey: str
        :param CreateTime: 服务创建时间戳
        :type CreateTime: int
        :param RealtimeSpeechConf: 实时语音服务配置数据
        :type RealtimeSpeechConf: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`
        :param VoiceMessageConf: 语音消息及转文本服务配置数据
        :type VoiceMessageConf: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`
        :param VoiceFilterConf: 语音分析服务配置数据
        :type VoiceFilterConf: :class:`tencentcloud.gme.v20180711.models.VoiceFilterConf`
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppResponse(AbstractModel):
    """CreateApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 创建应用返回数据
        :type Data: :class:`tencentcloud.gme.v20180711.models.CreateAppResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CreateAppResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class CreateCustomizationRequest(AbstractModel):
    """CreateCustomization请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizId: 应用 ID，登录控制台创建应用得到的AppID
        :type BizId: int
        :param TextUrl: 文本文件的下载地址，服务会从该地址下载文件，目前仅支持腾讯云cos
        :type TextUrl: str
        :param ModelName: 模型名称，名称长度不超过36，默认为BizId。
        :type ModelName: str
        """
        self.BizId = None
        self.TextUrl = None
        self.ModelName = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.TextUrl = params.get("TextUrl")
        self.ModelName = params.get("ModelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomizationResponse(AbstractModel):
    """CreateCustomization返回参数结构体

    """

    def __init__(self):
        r"""
        :param ModelId: 模型ID
        :type ModelId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ModelId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.RequestId = params.get("RequestId")


class CreateScanUserRequest(AbstractModel):
    """CreateScanUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizId: 应用ID，登录控制台 - 服务管理创建应用得到的AppID
        :type BizId: int
        :param UserId: 需要新增送检的用户号。示例：1234
        :type UserId: int
        """
        self.BizId = None
        self.UserId = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScanUserResponse(AbstractModel):
    """CreateScanUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrorCode: 返回结果码
        :type ErrorCode: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.RequestId = params.get("RequestId")


class CustomizationConfigs(AbstractModel):
    """语音消息转文本热句模型配置

    """

    def __init__(self):
        r"""
        :param BizId: 应用 ID，登录控制台创建应用得到的AppID
        :type BizId: int
        :param ModelId: 模型ID
        :type ModelId: str
        :param ModelState: 模型状态，-1下线状态，1上线状态, 0训练中, -2训练失败, 3上线中, 4下线中
        :type ModelState: int
        :param ModelName: 模型名称
        :type ModelName: str
        :param TextUrl: 文本文件的下载地址，服务会从该地址下载文件，目前仅支持腾讯云cos
        :type TextUrl: str
        :param UpdateTime: 更新时间，11位时间戳
        :type UpdateTime: int
        """
        self.BizId = None
        self.ModelId = None
        self.ModelState = None
        self.ModelName = None
        self.TextUrl = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.ModelId = params.get("ModelId")
        self.ModelState = params.get("ModelState")
        self.ModelName = params.get("ModelName")
        self.TextUrl = params.get("TextUrl")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomizationRequest(AbstractModel):
    """DeleteCustomization请求参数结构体

    """

    def __init__(self):
        r"""
        :param ModelId: 删除的模型ID
        :type ModelId: str
        :param BizId: 应用 ID，登录控制台创建应用得到的AppID
        :type BizId: int
        """
        self.ModelId = None
        self.BizId = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomizationResponse(AbstractModel):
    """DeleteCustomization返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrorCode: 返回值。0为成功，非0为失败。
        :type ErrorCode: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.RequestId = params.get("RequestId")


class DeleteResult(AbstractModel):
    """剔除房间操作结果

    """

    def __init__(self):
        r"""
        :param Code: 错误码，0-剔除成功 其他-剔除失败
        :type Code: int
        :param ErrorMsg: 错误描述
        :type ErrorMsg: str
        """
        self.Code = None
        self.ErrorMsg = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoomMemberRequest(AbstractModel):
    """DeleteRoomMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoomId: 要操作的房间id
        :type RoomId: str
        :param Uids: 要剔除的用户列表
        :type Uids: list of str
        :param DeleteType: 剔除类型 1-删除房间 2-剔除用户
        :type DeleteType: int
        :param BizId: 应用id
        :type BizId: int
        """
        self.RoomId = None
        self.Uids = None
        self.DeleteType = None
        self.BizId = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.Uids = params.get("Uids")
        self.DeleteType = params.get("DeleteType")
        self.BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoomMemberResponse(AbstractModel):
    """DeleteRoomMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param DeleteResult: 剔除房间或成员的操作结果
        :type DeleteResult: :class:`tencentcloud.gme.v20180711.models.DeleteResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeleteResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeleteResult") is not None:
            self.DeleteResult = DeleteResult()
            self.DeleteResult._deserialize(params.get("DeleteResult"))
        self.RequestId = params.get("RequestId")


class DeleteScanUserRequest(AbstractModel):
    """DeleteScanUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizId: 应用ID，登录控制台 - 服务管理创建应用得到的AppID
        :type BizId: int
        :param UserId: 需要删除送检的用户号。示例：1234
        :type UserId: int
        """
        self.BizId = None
        self.UserId = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteScanUserResponse(AbstractModel):
    """DeleteScanUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrorCode: 返回结果码
        :type ErrorCode: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.RequestId = params.get("RequestId")


class DescribeAgeDetectTaskRequest(AbstractModel):
    """DescribeAgeDetectTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizId: 应用id
        :type BizId: int
        :param TaskId: 创建年龄语音识别任务时返回的taskid
        :type TaskId: str
        """
        self.BizId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgeDetectTaskResponse(AbstractModel):
    """DescribeAgeDetectTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        :param Results: 语音检测返回。Results 字段是 JSON 数组，每一个元素包含：
DataId： 请求中对应的 DataId。
Url ：该请求中对应的 Url。
Status ：子任务状态，0:已创建，1:运行中，2:已完成，3:任务异常，4:任务超时。
Age ：子任务完成后的结果，0:成年人，1:未成年人，100:未知结果。
        :type Results: list of AgeDetectTaskResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = AgeDetectTaskResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAppStatisticsRequest(AbstractModel):
    """DescribeAppStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizId: GME应用ID
        :type BizId: int
        :param StartDate: 数据开始时间，东八区时间，格式: 年-月-日，如: 2018-07-13
        :type StartDate: str
        :param EndDate: 数据结束时间，东八区时间，格式: 年-月-日，如: 2018-07-13
        :type EndDate: str
        :param Services: 要查询的服务列表，取值：RealTimeSpeech/VoiceMessage/VoiceFilter/SpeechToText
        :type Services: list of str
        """
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
        


class DescribeAppStatisticsResp(AbstractModel):
    """获取应用用量统计数据输出参数

    """

    def __init__(self):
        r"""
        :param AppStatistics: 应用用量统计数据
        :type AppStatistics: list of AppStatisticsItem
        """
        self.AppStatistics = None


    def _deserialize(self, params):
        if params.get("AppStatistics") is not None:
            self.AppStatistics = []
            for item in params.get("AppStatistics"):
                obj = AppStatisticsItem()
                obj._deserialize(item)
                self.AppStatistics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppStatisticsResponse(AbstractModel):
    """DescribeAppStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 应用用量统计数据
        :type Data: :class:`tencentcloud.gme.v20180711.models.DescribeAppStatisticsResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeAppStatisticsResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeApplicationDataRequest(AbstractModel):
    """DescribeApplicationData请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizId: 应用ID
        :type BizId: int
        :param StartDate: 数据开始时间，格式为 年-月-日，如: 2018-07-13
        :type StartDate: str
        :param EndDate: 数据结束时间，格式为 年-月-日，如: 2018-07-13
        :type EndDate: str
        """
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
        r"""
        :param Data: 应用统计数据
        :type Data: :class:`tencentcloud.gme.v20180711.models.ApplicationDataStatistics`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ApplicationDataStatistics()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeApplicationListRequest(AbstractModel):
    """DescribeApplicationList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID，0表示默认项目，-1表示所有项目，如果需要查找具体项目下的应用列表，请填入具体项目ID，项目ID在项目管理中查看 https://console.cloud.tencent.com/project
        :type ProjectId: int
        :param PageNo: 页码ID，0表示第一页，以此后推。默认填0
        :type PageNo: int
        :param PageSize: 每页展示应用数量。默认填200
        :type PageSize: int
        :param SearchText: 所查找应用名称的关键字，支持模糊匹配查找。空串表示查询所有应用
        :type SearchText: str
        :param TagSet: 标签列表
        :type TagSet: list of Tag
        :param Filters: 查找过滤关键字列表
        :type Filters: list of Filter
        """
        self.ProjectId = None
        self.PageNo = None
        self.PageSize = None
        self.SearchText = None
        self.TagSet = None
        self.Filters = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.SearchText = params.get("SearchText")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationListResponse(AbstractModel):
    """DescribeApplicationList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationList: 获取应用列表返回
        :type ApplicationList: list of ApplicationList
        :param Total: 应用总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ApplicationList = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ApplicationList") is not None:
            self.ApplicationList = []
            for item in params.get("ApplicationList"):
                obj = ApplicationList()
                obj._deserialize(item)
                self.ApplicationList.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeRealtimeScanConfigRequest(AbstractModel):
    """DescribeRealtimeScanConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizId: 应用ID
        :type BizId: int
        """
        self.BizId = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRealtimeScanConfigResponse(AbstractModel):
    """DescribeRealtimeScanConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrorCode: 返回结果码，0正常，非0失败
        :type ErrorCode: int
        :param BizId: 应用ID
        :type BizId: int
        :param AuditType: 送检类型，0: 全量送审，1: 自定义送审
        :type AuditType: int
        :param UserIdRegex: 用户号正则表达式
        :type UserIdRegex: list of str
        :param RoomIdRegex: 房间号正则表达式
        :type RoomIdRegex: list of str
        :param UserIdString: 用户号字符串，逗号分隔，示例："0001,0002,0003"
        :type UserIdString: str
        :param RoomIdString: 房间号字符串，逗号分隔，示例："0001,0002,0003"
        :type RoomIdString: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.BizId = None
        self.AuditType = None
        self.UserIdRegex = None
        self.RoomIdRegex = None
        self.UserIdString = None
        self.RoomIdString = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.BizId = params.get("BizId")
        self.AuditType = params.get("AuditType")
        self.UserIdRegex = params.get("UserIdRegex")
        self.RoomIdRegex = params.get("RoomIdRegex")
        self.UserIdString = params.get("UserIdString")
        self.RoomIdString = params.get("RoomIdString")
        self.RequestId = params.get("RequestId")


class DescribeRoomInfoRequest(AbstractModel):
    """DescribeRoomInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用ID，登录[控制台 - 服务管理](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID
        :type SdkAppId: int
        :param RoomIds: 房间号列表，最大不能超过10个（RoomIds、StrRoomIds必须填一个）
        :type RoomIds: list of int non-negative
        :param StrRoomIds: 字符串类型房间号列表，最大不能超过10个（RoomIds、StrRoomIds必须填一个）
        :type StrRoomIds: list of str
        """
        self.SdkAppId = None
        self.RoomIds = None
        self.StrRoomIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomIds = params.get("RoomIds")
        self.StrRoomIds = params.get("StrRoomIds")
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
        r"""
        :param Result: 操作结果, 0成功, 非0失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: int
        :param RoomUsers: 房间用户信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RoomUsers: list of RoomUser
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
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
        :param BizId: 提交检测的应用 ID
        :type BizId: int
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
        self.BizId = None


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
        self.BizId = params.get("BizId")
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
        r"""
        :param BizId: 应用 ID，登录[控制台](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID
        :type BizId: int
        :param TaskIdList: 查询的任务 ID 列表，任务 ID 列表最多支持 100 个。
        :type TaskIdList: list of str
        :param Limit: 任务返回结果数量，默认10，上限500。大文件任务忽略此参数，返回全量结果
        :type Limit: int
        """
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
        r"""
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


class DescribeUserInAndOutTimeRequest(AbstractModel):
    """DescribeUserInAndOutTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizId: 应用ID
        :type BizId: int
        :param RoomId: 房间ID
        :type RoomId: int
        :param UserId: 用户ID
        :type UserId: int
        :param UserIdStr: 字符串类型用户ID
        :type UserIdStr: str
        :param RoomIdStr: 字符串类型房间ID
        :type RoomIdStr: str
        """
        self.BizId = None
        self.RoomId = None
        self.UserId = None
        self.UserIdStr = None
        self.RoomIdStr = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.RoomId = params.get("RoomId")
        self.UserId = params.get("UserId")
        self.UserIdStr = params.get("UserIdStr")
        self.RoomIdStr = params.get("RoomIdStr")
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
        r"""
        :param InOutList: 用户在房间得进出时间列表
        :type InOutList: list of InOutTimeInfo
        :param Duration: 用户在房间中总时长
        :type Duration: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class Filter(AbstractModel):
    """查找过滤

    """

    def __init__(self):
        r"""
        :param Name: 要过滤的字段名, 比如"AppName"
        :type Name: str
        :param Values: 多个关键字
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCustomizationListRequest(AbstractModel):
    """GetCustomizationList请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizId: 应用 ID，登录控制台创建应用得到的AppID
        :type BizId: int
        """
        self.BizId = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCustomizationListResponse(AbstractModel):
    """GetCustomizationList返回参数结构体

    """

    def __init__(self):
        r"""
        :param CustomizationConfigs: 语音消息转文本热句模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomizationConfigs: list of CustomizationConfigs
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CustomizationConfigs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomizationConfigs") is not None:
            self.CustomizationConfigs = []
            for item in params.get("CustomizationConfigs"):
                obj = CustomizationConfigs()
                obj._deserialize(item)
                self.CustomizationConfigs.append(obj)
        self.RequestId = params.get("RequestId")


class InOutTimeInfo(AbstractModel):
    """用户进出房间信息

    """

    def __init__(self):
        r"""
        :param StartTime: 进入房间时间
        :type StartTime: int
        :param EndTime: 退出房间时间
        :type EndTime: int
        """
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
        r"""
        :param BizId: 应用ID，创建应用后由后台生成并返回。
        :type BizId: int
        :param Status: 应用状态，取值：open/close
        :type Status: str
        """
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
        


class ModifyAppStatusResp(AbstractModel):
    """ModifyAppStatus接口输出参数

    """

    def __init__(self):
        r"""
        :param BizId: GME应用ID
        :type BizId: int
        :param Status: 应用状态，取值：open/close
        :type Status: str
        """
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
    """ModifyAppStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 修改应用开关状态返回数据
        :type Data: :class:`tencentcloud.gme.v20180711.models.ModifyAppStatusResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ModifyAppStatusResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class ModifyCustomizationRequest(AbstractModel):
    """ModifyCustomization请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizId: 应用 ID，登录控制台创建应用得到的AppID
        :type BizId: int
        :param TextUrl: 文本文件的下载地址，服务会从该地址下载文件，目前仅支持腾讯云cos
        :type TextUrl: str
        :param ModelId: 修改的模型ID
        :type ModelId: str
        """
        self.BizId = None
        self.TextUrl = None
        self.ModelId = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.TextUrl = params.get("TextUrl")
        self.ModelId = params.get("ModelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomizationResponse(AbstractModel):
    """ModifyCustomization返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrorCode: 返回值。0为成功，非0为失败。
        :type ErrorCode: int
        :param ModelId: 模型ID
        :type ModelId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.ModelId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.ModelId = params.get("ModelId")
        self.RequestId = params.get("RequestId")


class ModifyCustomizationStateRequest(AbstractModel):
    """ModifyCustomizationState请求参数结构体

    """

    def __init__(self):
        r"""
        :param ModelId: 模型ID
        :type ModelId: str
        :param ToState: 想要变换的模型状态，-1代表下线，1代表上线
        :type ToState: int
        :param BizId: 应用 ID，登录控制台创建应用得到的AppID
        :type BizId: int
        """
        self.ModelId = None
        self.ToState = None
        self.BizId = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.ToState = params.get("ToState")
        self.BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomizationStateResponse(AbstractModel):
    """ModifyCustomizationState返回参数结构体

    """

    def __init__(self):
        r"""
        :param ModelId: 模型ID
        :type ModelId: str
        :param ErrorCode: 返回值。0为成功，非0为失败。
        :type ErrorCode: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ModelId = None
        self.ErrorCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.ErrorCode = params.get("ErrorCode")
        self.RequestId = params.get("RequestId")


class ModifyUserMicStatusRequest(AbstractModel):
    """ModifyUserMicStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizId: 来自 [腾讯云控制台](https://console.cloud.tencent.com/gamegme) 的 GME 服务提供的 AppID，获取请参考 [语音服务开通指引](https://cloud.tencent.com/document/product/607/10782#.E9.87.8D.E7.82.B9.E5.8F.82.E6.95.B0)。
        :type BizId: int
        :param RoomId: 实时语音房间号。
        :type RoomId: str
        :param Users: 需要操作的房间内用户以及该用户的目标麦克风状态。
        :type Users: list of UserMicStatus
        """
        self.BizId = None
        self.RoomId = None
        self.Users = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.RoomId = params.get("RoomId")
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = UserMicStatus()
                obj._deserialize(item)
                self.Users.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserMicStatusResponse(AbstractModel):
    """ModifyUserMicStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果：0为成功，非0为失败。
        :type Result: int
        :param ErrMsg: 错误信息。
        :type ErrMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.ErrMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.ErrMsg = params.get("ErrMsg")
        self.RequestId = params.get("RequestId")


class OverseaTextStatisticsItem(AbstractModel):
    """海外转文本用量数据

    """

    def __init__(self):
        r"""
        :param Data: 统计值，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: float
        """
        self.Data = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealTimeSpeechStatisticsItem(AbstractModel):
    """实时语音用量统计数据

    """

    def __init__(self):
        r"""
        :param MainLandDau: 大陆地区DAU
        :type MainLandDau: int
        :param MainLandPcu: 大陆地区PCU
        :type MainLandPcu: int
        :param MainLandDuration: 大陆地区总使用时长，单位为min
        :type MainLandDuration: int
        :param OverseaDau: 海外地区DAU
        :type OverseaDau: int
        :param OverseaPcu: 海外地区PCU
        :type OverseaPcu: int
        :param OverseaDuration: 海外地区总使用时长，单位为min
        :type OverseaDuration: int
        """
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
        r"""
        :param Status: 实时语音服务开关，取值：open/close
        :type Status: str
        :param Quality: 实时语音音质类型，取值：high-高音质
        :type Quality: str
        """
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
        


class RealtimeTextStatisticsItem(AbstractModel):
    """实时语音转文本用量数据

    """

    def __init__(self):
        r"""
        :param Data: 统计值，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: float
        """
        self.Data = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
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
        r"""
        :param RoomId: 房间id
        :type RoomId: int
        :param Uins: 房间里用户uin列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Uins: list of int non-negative
        :param StrRoomId: 字符串房间id
注意：此字段可能返回 null，表示取不到有效值。
        :type StrRoomId: str
        """
        self.RoomId = None
        self.Uins = None
        self.StrRoomId = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.Uins = params.get("Uins")
        self.StrRoomId = params.get("StrRoomId")
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
        r"""
        :param Label: 违规场景，参照<a href="https://cloud.tencent.com/document/product/607/37622#Label_Value">Label</a>定义
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
        r"""
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
        :param RoomId: gme实时语音房间ID，透传任务传入时的RoomId
注意：此字段可能返回 null，表示取不到有效值。
        :type RoomId: str
        :param OpenId: gme实时语音用户ID，透传任务传入时的OpenId
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param Info: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: str
        :param Offset: 流检测时分片在流中的偏移时间，单位毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: int
        :param Duration: 流检测时分片时长
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param PieceStartTime: 分片开始检测时间
注意：此字段可能返回 null，表示取不到有效值。
        :type PieceStartTime: int
        """
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
        r"""
        :param BizId: 应用ID，登录[控制台 - 服务管理](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID
        :type BizId: int
        :param Scenes: 语音检测场景，参数值目前要求为 default。 预留场景设置： 谩骂、色情、广告、违禁等场景，<a href="#Label_Value">具体取值见上述 Label 说明。</a>
        :type Scenes: list of str
        :param Live: 是否为直播流。值为 false 时表示普通语音文件检测；为 true 时表示语音流检测。
        :type Live: bool
        :param Tasks: 语音检测任务列表，列表最多支持100个检测任务。结构体中包含：
<li>DataId：数据的唯一ID</li>
<li>Url：数据文件的url，为 urlencode 编码，流式则为拉流地址</li>
        :type Tasks: list of Task
        :param Callback: 异步检测结果回调地址，具体见上述<a href="#Callback_Declare">回调相关说明</a>。（说明：该字段为空时，必须通过接口(查询语音检测结果)获取检测结果）。
        :type Callback: str
        :param Lang: 语种，不传默认中文
        :type Lang: str
        """
        self.BizId = None
        self.Scenes = None
        self.Live = None
        self.Tasks = None
        self.Callback = None
        self.Lang = None


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
        self.Lang = params.get("Lang")
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
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceStatus(AbstractModel):
    """服务开关状态

    """

    def __init__(self):
        r"""
        :param RealTimeSpeech: 实时语音服务开关状态
注意：此字段可能返回 null，表示取不到有效值。
        :type RealTimeSpeech: :class:`tencentcloud.gme.v20180711.models.StatusInfo`
        :param VoiceMessage: 语音消息服务开关状态
注意：此字段可能返回 null，表示取不到有效值。
        :type VoiceMessage: :class:`tencentcloud.gme.v20180711.models.StatusInfo`
        :param Porn: 语音内容安全服务开关状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Porn: :class:`tencentcloud.gme.v20180711.models.StatusInfo`
        :param Live: 语音录制服务开关状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Live: :class:`tencentcloud.gme.v20180711.models.StatusInfo`
        :param RealTimeAsr: 语音转文本服务开关状态
注意：此字段可能返回 null，表示取不到有效值。
        :type RealTimeAsr: :class:`tencentcloud.gme.v20180711.models.StatusInfo`
        """
        self.RealTimeSpeech = None
        self.VoiceMessage = None
        self.Porn = None
        self.Live = None
        self.RealTimeAsr = None


    def _deserialize(self, params):
        if params.get("RealTimeSpeech") is not None:
            self.RealTimeSpeech = StatusInfo()
            self.RealTimeSpeech._deserialize(params.get("RealTimeSpeech"))
        if params.get("VoiceMessage") is not None:
            self.VoiceMessage = StatusInfo()
            self.VoiceMessage._deserialize(params.get("VoiceMessage"))
        if params.get("Porn") is not None:
            self.Porn = StatusInfo()
            self.Porn._deserialize(params.get("Porn"))
        if params.get("Live") is not None:
            self.Live = StatusInfo()
            self.Live._deserialize(params.get("Live"))
        if params.get("RealTimeAsr") is not None:
            self.RealTimeAsr = StatusInfo()
            self.RealTimeAsr._deserialize(params.get("RealTimeAsr"))
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
        r"""
        :param StatDate: 日期，格式为年-月-日，如2018-07-13
        :type StatDate: str
        :param Data: 统计值
        :type Data: int
        """
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
        


class StatusInfo(AbstractModel):
    """服务开关状态

    """

    def __init__(self):
        r"""
        :param Status: 服务开关状态， 0-正常，1-关闭
        :type Status: int
        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamTextStatisticsItem(AbstractModel):
    """流式转文本用量数据

    """

    def __init__(self):
        r"""
        :param Data: 统计值，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: float
        """
        self.Data = None


    def _deserialize(self, params):
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
        r"""
        :param TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
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
        r"""
        :param DataId: 数据的唯一ID
        :type DataId: str
        :param Url: 数据文件的url，为 urlencode 编码，流式则为拉流地址
        :type Url: str
        :param RoomId: gme实时语音房间ID，通过gme实时语音进行语音分析时输入
        :type RoomId: str
        :param OpenId: gme实时语音用户ID，通过gme实时语音进行语音分析时输入
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateScanRoomsRequest(AbstractModel):
    """UpdateScanRooms请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizId: 应用ID
        :type BizId: int
        :param RoomIdString: 需要送检的所有房间号。多个房间号之间用","分隔。示例："0001,0002,0003"
        :type RoomIdString: str
        :param RoomIdRegex: 符合此正则表达式规则的房间号将被送检。示例：["^6.*"] 表示所有以6开头的房间号将被送检
        :type RoomIdRegex: list of str
        """
        self.BizId = None
        self.RoomIdString = None
        self.RoomIdRegex = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.RoomIdString = params.get("RoomIdString")
        self.RoomIdRegex = params.get("RoomIdRegex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateScanRoomsResponse(AbstractModel):
    """UpdateScanRooms返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrorCode: 返回结果码
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCode: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.RequestId = params.get("RequestId")


class UpdateScanUsersRequest(AbstractModel):
    """UpdateScanUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizId: 应用ID
        :type BizId: int
        :param UserIdString: 需要送检的所有用户号。多个用户号之间用","分隔。示例："0001,0002,0003"
        :type UserIdString: str
        :param UserIdRegex: 符合此正则表达式规则的用户号将被送检。示例：["^6.*"] 表示所有以6开头的用户号将被送检
        :type UserIdRegex: list of str
        """
        self.BizId = None
        self.UserIdString = None
        self.UserIdRegex = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.UserIdString = params.get("UserIdString")
        self.UserIdRegex = params.get("UserIdRegex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateScanUsersResponse(AbstractModel):
    """UpdateScanUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrorCode: 返回结果码
        :type ErrorCode: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.RequestId = params.get("RequestId")


class UserMicStatus(AbstractModel):
    """用户麦克风状态

    """

    def __init__(self):
        r"""
        :param Uid: 客户端用于标识用户的Openid。
        :type Uid: int
        :param EnableMic: 开麦状态。1表示关闭麦克风，2表示打开麦克风。
        :type EnableMic: int
        """
        self.Uid = None
        self.EnableMic = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.EnableMic = params.get("EnableMic")
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
        r"""
        :param Status: 语音过滤服务开关，取值：open/close
        :type Status: str
        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceFilterStatisticsItem(AbstractModel):
    """语音过滤用量统计数据

    """

    def __init__(self):
        r"""
        :param Duration: 语音过滤总时长，单位为min
        :type Duration: int
        """
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
        r"""
        :param Status: 离线语音服务开关，取值：open/close
        :type Status: str
        :param Language: 离线语音支持语种，取值： all-全部，cnen-中英文。默认为中英文
        :type Language: str
        """
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
        r"""
        :param Dau: 离线语音DAU
        :type Dau: int
        """
        self.Dau = None


    def _deserialize(self, params):
        self.Dau = params.get("Dau")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        