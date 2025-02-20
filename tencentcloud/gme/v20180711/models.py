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
        :param _DataId: 数据唯一ID
        :type DataId: str
        :param _Url: 数据文件的url，为 urlencode 编码,音频文件格式支持的类型：.wav、.m4a、.amr、.mp3、.aac、.wma、.ogg
        :type Url: str
        """
        self._DataId = None
        self._Url = None

    @property
    def DataId(self):
        """数据唯一ID
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def Url(self):
        """数据文件的url，为 urlencode 编码,音频文件格式支持的类型：.wav、.m4a、.amr、.mp3、.aac、.wma、.ogg
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._DataId = params.get("DataId")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgeDetectTaskResult(AbstractModel):
    """年龄语音任务结果

    """

    def __init__(self):
        r"""
        :param _DataId: 数据唯一ID
        :type DataId: str
        :param _Url: 数据文件的url
        :type Url: str
        :param _Status: 任务状态，0: 已创建，1:运行中，2:正常结束，3:异常结束，4:运行超时
        :type Status: int
        :param _Age: 任务结果：0: 成年，1:未成年，100:未知
        :type Age: int
        """
        self._DataId = None
        self._Url = None
        self._Status = None
        self._Age = None

    @property
    def DataId(self):
        """数据唯一ID
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def Url(self):
        """数据文件的url
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Status(self):
        """任务状态，0: 已创建，1:运行中，2:正常结束，3:异常结束，4:运行超时
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Age(self):
        """任务结果：0: 成年，1:未成年，100:未知
        :rtype: int
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age


    def _deserialize(self, params):
        self._DataId = params.get("DataId")
        self._Url = params.get("Url")
        self._Status = params.get("Status")
        self._Age = params.get("Age")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppStatisticsItem(AbstractModel):
    """应用用量统计数据

    """

    def __init__(self):
        r"""
        :param _RealtimeSpeechStatisticsItem: 实时语音统计数据
        :type RealtimeSpeechStatisticsItem: :class:`tencentcloud.gme.v20180711.models.RealTimeSpeechStatisticsItem`
        :param _VoiceMessageStatisticsItem: 语音消息统计数据
        :type VoiceMessageStatisticsItem: :class:`tencentcloud.gme.v20180711.models.VoiceMessageStatisticsItem`
        :param _VoiceFilterStatisticsItem: 语音过滤统计数据
        :type VoiceFilterStatisticsItem: :class:`tencentcloud.gme.v20180711.models.VoiceFilterStatisticsItem`
        :param _Date: 统计时间
        :type Date: str
        :param _AudioTextStatisticsItem: 录音转文本用量统计数据
        :type AudioTextStatisticsItem: :class:`tencentcloud.gme.v20180711.models.AudioTextStatisticsItem`
        :param _StreamTextStatisticsItem: 流式转文本用量数据
        :type StreamTextStatisticsItem: :class:`tencentcloud.gme.v20180711.models.StreamTextStatisticsItem`
        :param _OverseaTextStatisticsItem: 海外转文本用量数据
        :type OverseaTextStatisticsItem: :class:`tencentcloud.gme.v20180711.models.OverseaTextStatisticsItem`
        :param _RealtimeTextStatisticsItem: 实时语音转文本用量数据
        :type RealtimeTextStatisticsItem: :class:`tencentcloud.gme.v20180711.models.RealtimeTextStatisticsItem`
        """
        self._RealtimeSpeechStatisticsItem = None
        self._VoiceMessageStatisticsItem = None
        self._VoiceFilterStatisticsItem = None
        self._Date = None
        self._AudioTextStatisticsItem = None
        self._StreamTextStatisticsItem = None
        self._OverseaTextStatisticsItem = None
        self._RealtimeTextStatisticsItem = None

    @property
    def RealtimeSpeechStatisticsItem(self):
        """实时语音统计数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.RealTimeSpeechStatisticsItem`
        """
        return self._RealtimeSpeechStatisticsItem

    @RealtimeSpeechStatisticsItem.setter
    def RealtimeSpeechStatisticsItem(self, RealtimeSpeechStatisticsItem):
        self._RealtimeSpeechStatisticsItem = RealtimeSpeechStatisticsItem

    @property
    def VoiceMessageStatisticsItem(self):
        """语音消息统计数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.VoiceMessageStatisticsItem`
        """
        return self._VoiceMessageStatisticsItem

    @VoiceMessageStatisticsItem.setter
    def VoiceMessageStatisticsItem(self, VoiceMessageStatisticsItem):
        self._VoiceMessageStatisticsItem = VoiceMessageStatisticsItem

    @property
    def VoiceFilterStatisticsItem(self):
        """语音过滤统计数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.VoiceFilterStatisticsItem`
        """
        return self._VoiceFilterStatisticsItem

    @VoiceFilterStatisticsItem.setter
    def VoiceFilterStatisticsItem(self, VoiceFilterStatisticsItem):
        self._VoiceFilterStatisticsItem = VoiceFilterStatisticsItem

    @property
    def Date(self):
        """统计时间
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def AudioTextStatisticsItem(self):
        """录音转文本用量统计数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.AudioTextStatisticsItem`
        """
        return self._AudioTextStatisticsItem

    @AudioTextStatisticsItem.setter
    def AudioTextStatisticsItem(self, AudioTextStatisticsItem):
        self._AudioTextStatisticsItem = AudioTextStatisticsItem

    @property
    def StreamTextStatisticsItem(self):
        """流式转文本用量数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.StreamTextStatisticsItem`
        """
        return self._StreamTextStatisticsItem

    @StreamTextStatisticsItem.setter
    def StreamTextStatisticsItem(self, StreamTextStatisticsItem):
        self._StreamTextStatisticsItem = StreamTextStatisticsItem

    @property
    def OverseaTextStatisticsItem(self):
        """海外转文本用量数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.OverseaTextStatisticsItem`
        """
        return self._OverseaTextStatisticsItem

    @OverseaTextStatisticsItem.setter
    def OverseaTextStatisticsItem(self, OverseaTextStatisticsItem):
        self._OverseaTextStatisticsItem = OverseaTextStatisticsItem

    @property
    def RealtimeTextStatisticsItem(self):
        """实时语音转文本用量数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.RealtimeTextStatisticsItem`
        """
        return self._RealtimeTextStatisticsItem

    @RealtimeTextStatisticsItem.setter
    def RealtimeTextStatisticsItem(self, RealtimeTextStatisticsItem):
        self._RealtimeTextStatisticsItem = RealtimeTextStatisticsItem


    def _deserialize(self, params):
        if params.get("RealtimeSpeechStatisticsItem") is not None:
            self._RealtimeSpeechStatisticsItem = RealTimeSpeechStatisticsItem()
            self._RealtimeSpeechStatisticsItem._deserialize(params.get("RealtimeSpeechStatisticsItem"))
        if params.get("VoiceMessageStatisticsItem") is not None:
            self._VoiceMessageStatisticsItem = VoiceMessageStatisticsItem()
            self._VoiceMessageStatisticsItem._deserialize(params.get("VoiceMessageStatisticsItem"))
        if params.get("VoiceFilterStatisticsItem") is not None:
            self._VoiceFilterStatisticsItem = VoiceFilterStatisticsItem()
            self._VoiceFilterStatisticsItem._deserialize(params.get("VoiceFilterStatisticsItem"))
        self._Date = params.get("Date")
        if params.get("AudioTextStatisticsItem") is not None:
            self._AudioTextStatisticsItem = AudioTextStatisticsItem()
            self._AudioTextStatisticsItem._deserialize(params.get("AudioTextStatisticsItem"))
        if params.get("StreamTextStatisticsItem") is not None:
            self._StreamTextStatisticsItem = StreamTextStatisticsItem()
            self._StreamTextStatisticsItem._deserialize(params.get("StreamTextStatisticsItem"))
        if params.get("OverseaTextStatisticsItem") is not None:
            self._OverseaTextStatisticsItem = OverseaTextStatisticsItem()
            self._OverseaTextStatisticsItem._deserialize(params.get("OverseaTextStatisticsItem"))
        if params.get("RealtimeTextStatisticsItem") is not None:
            self._RealtimeTextStatisticsItem = RealtimeTextStatisticsItem()
            self._RealtimeTextStatisticsItem._deserialize(params.get("RealtimeTextStatisticsItem"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationDataStatistics(AbstractModel):
    """应用统计数据

    """

    def __init__(self):
        r"""
        :param _BizId: 应用ID
        :type BizId: int
        :param _DauDataNum: Dau统计项数目
        :type DauDataNum: int
        :param _DauDataMainland: 大陆地区Dau统计数据，单位人
        :type DauDataMainland: list of StatisticsItem
        :param _DauDataOversea: 海外地区Dau统计数据，单位人
        :type DauDataOversea: list of StatisticsItem
        :param _DauDataSum: 大陆和海外地区Dau统计数据汇总，单位人
        :type DauDataSum: list of StatisticsItem
        :param _DurationDataNum: 实时语音时长统计项数目
        :type DurationDataNum: int
        :param _DurationDataMainland: 大陆地区实时语音时长统计数据，单位分钟
        :type DurationDataMainland: list of StatisticsItem
        :param _DurationDataOversea: 海外地区实时语音时长统计数据，单位分钟
        :type DurationDataOversea: list of StatisticsItem
        :param _DurationDataSum: 大陆和海外地区实时语音时长统计数据汇总，单位分钟
        :type DurationDataSum: list of StatisticsItem
        :param _PcuDataNum: Pcu统计项数目
        :type PcuDataNum: int
        :param _PcuDataMainland: 大陆地区Pcu统计数据，单位人
        :type PcuDataMainland: list of StatisticsItem
        :param _PcuDataOversea: 海外地区Pcu统计数据，单位人
        :type PcuDataOversea: list of StatisticsItem
        :param _PcuDataSum: 大陆和海外地区Pcu统计数据汇总，单位人
        :type PcuDataSum: list of StatisticsItem
        """
        self._BizId = None
        self._DauDataNum = None
        self._DauDataMainland = None
        self._DauDataOversea = None
        self._DauDataSum = None
        self._DurationDataNum = None
        self._DurationDataMainland = None
        self._DurationDataOversea = None
        self._DurationDataSum = None
        self._PcuDataNum = None
        self._PcuDataMainland = None
        self._PcuDataOversea = None
        self._PcuDataSum = None

    @property
    def BizId(self):
        """应用ID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def DauDataNum(self):
        """Dau统计项数目
        :rtype: int
        """
        return self._DauDataNum

    @DauDataNum.setter
    def DauDataNum(self, DauDataNum):
        self._DauDataNum = DauDataNum

    @property
    def DauDataMainland(self):
        """大陆地区Dau统计数据，单位人
        :rtype: list of StatisticsItem
        """
        return self._DauDataMainland

    @DauDataMainland.setter
    def DauDataMainland(self, DauDataMainland):
        self._DauDataMainland = DauDataMainland

    @property
    def DauDataOversea(self):
        """海外地区Dau统计数据，单位人
        :rtype: list of StatisticsItem
        """
        return self._DauDataOversea

    @DauDataOversea.setter
    def DauDataOversea(self, DauDataOversea):
        self._DauDataOversea = DauDataOversea

    @property
    def DauDataSum(self):
        """大陆和海外地区Dau统计数据汇总，单位人
        :rtype: list of StatisticsItem
        """
        return self._DauDataSum

    @DauDataSum.setter
    def DauDataSum(self, DauDataSum):
        self._DauDataSum = DauDataSum

    @property
    def DurationDataNum(self):
        """实时语音时长统计项数目
        :rtype: int
        """
        return self._DurationDataNum

    @DurationDataNum.setter
    def DurationDataNum(self, DurationDataNum):
        self._DurationDataNum = DurationDataNum

    @property
    def DurationDataMainland(self):
        """大陆地区实时语音时长统计数据，单位分钟
        :rtype: list of StatisticsItem
        """
        return self._DurationDataMainland

    @DurationDataMainland.setter
    def DurationDataMainland(self, DurationDataMainland):
        self._DurationDataMainland = DurationDataMainland

    @property
    def DurationDataOversea(self):
        """海外地区实时语音时长统计数据，单位分钟
        :rtype: list of StatisticsItem
        """
        return self._DurationDataOversea

    @DurationDataOversea.setter
    def DurationDataOversea(self, DurationDataOversea):
        self._DurationDataOversea = DurationDataOversea

    @property
    def DurationDataSum(self):
        """大陆和海外地区实时语音时长统计数据汇总，单位分钟
        :rtype: list of StatisticsItem
        """
        return self._DurationDataSum

    @DurationDataSum.setter
    def DurationDataSum(self, DurationDataSum):
        self._DurationDataSum = DurationDataSum

    @property
    def PcuDataNum(self):
        """Pcu统计项数目
        :rtype: int
        """
        return self._PcuDataNum

    @PcuDataNum.setter
    def PcuDataNum(self, PcuDataNum):
        self._PcuDataNum = PcuDataNum

    @property
    def PcuDataMainland(self):
        """大陆地区Pcu统计数据，单位人
        :rtype: list of StatisticsItem
        """
        return self._PcuDataMainland

    @PcuDataMainland.setter
    def PcuDataMainland(self, PcuDataMainland):
        self._PcuDataMainland = PcuDataMainland

    @property
    def PcuDataOversea(self):
        """海外地区Pcu统计数据，单位人
        :rtype: list of StatisticsItem
        """
        return self._PcuDataOversea

    @PcuDataOversea.setter
    def PcuDataOversea(self, PcuDataOversea):
        self._PcuDataOversea = PcuDataOversea

    @property
    def PcuDataSum(self):
        """大陆和海外地区Pcu统计数据汇总，单位人
        :rtype: list of StatisticsItem
        """
        return self._PcuDataSum

    @PcuDataSum.setter
    def PcuDataSum(self, PcuDataSum):
        self._PcuDataSum = PcuDataSum


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._DauDataNum = params.get("DauDataNum")
        if params.get("DauDataMainland") is not None:
            self._DauDataMainland = []
            for item in params.get("DauDataMainland"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._DauDataMainland.append(obj)
        if params.get("DauDataOversea") is not None:
            self._DauDataOversea = []
            for item in params.get("DauDataOversea"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._DauDataOversea.append(obj)
        if params.get("DauDataSum") is not None:
            self._DauDataSum = []
            for item in params.get("DauDataSum"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._DauDataSum.append(obj)
        self._DurationDataNum = params.get("DurationDataNum")
        if params.get("DurationDataMainland") is not None:
            self._DurationDataMainland = []
            for item in params.get("DurationDataMainland"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._DurationDataMainland.append(obj)
        if params.get("DurationDataOversea") is not None:
            self._DurationDataOversea = []
            for item in params.get("DurationDataOversea"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._DurationDataOversea.append(obj)
        if params.get("DurationDataSum") is not None:
            self._DurationDataSum = []
            for item in params.get("DurationDataSum"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._DurationDataSum.append(obj)
        self._PcuDataNum = params.get("PcuDataNum")
        if params.get("PcuDataMainland") is not None:
            self._PcuDataMainland = []
            for item in params.get("PcuDataMainland"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._PcuDataMainland.append(obj)
        if params.get("PcuDataOversea") is not None:
            self._PcuDataOversea = []
            for item in params.get("PcuDataOversea"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._PcuDataOversea.append(obj)
        if params.get("PcuDataSum") is not None:
            self._PcuDataSum = []
            for item in params.get("PcuDataSum"):
                obj = StatisticsItem()
                obj._deserialize(item)
                self._PcuDataSum.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationList(AbstractModel):
    """获取应用列表返回

    """

    def __init__(self):
        r"""
        :param _ServiceConf: 服务开关状态
        :type ServiceConf: :class:`tencentcloud.gme.v20180711.models.ServiceStatus`
        :param _BizId: 应用ID(AppID)
        :type BizId: int
        :param _AppName: 应用名称
        :type AppName: str
        :param _ProjectId: 项目ID，默认为0
        :type ProjectId: int
        :param _AppStatus: 应用状态，返回0表示正常，1表示关闭，2表示欠费停服，3表示欠费回收
        :type AppStatus: int
        :param _CreateTime: 创建时间，Unix时间戳格式
        :type CreateTime: int
        :param _AppType: 应用类型，无需关注此数值
        :type AppType: int
        """
        self._ServiceConf = None
        self._BizId = None
        self._AppName = None
        self._ProjectId = None
        self._AppStatus = None
        self._CreateTime = None
        self._AppType = None

    @property
    def ServiceConf(self):
        """服务开关状态
        :rtype: :class:`tencentcloud.gme.v20180711.models.ServiceStatus`
        """
        return self._ServiceConf

    @ServiceConf.setter
    def ServiceConf(self, ServiceConf):
        self._ServiceConf = ServiceConf

    @property
    def BizId(self):
        """应用ID(AppID)
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def AppName(self):
        """应用名称
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def ProjectId(self):
        """项目ID，默认为0
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AppStatus(self):
        """应用状态，返回0表示正常，1表示关闭，2表示欠费停服，3表示欠费回收
        :rtype: int
        """
        return self._AppStatus

    @AppStatus.setter
    def AppStatus(self, AppStatus):
        self._AppStatus = AppStatus

    @property
    def CreateTime(self):
        """创建时间，Unix时间戳格式
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AppType(self):
        """应用类型，无需关注此数值
        :rtype: int
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType


    def _deserialize(self, params):
        if params.get("ServiceConf") is not None:
            self._ServiceConf = ServiceStatus()
            self._ServiceConf._deserialize(params.get("ServiceConf"))
        self._BizId = params.get("BizId")
        self._AppName = params.get("AppName")
        self._ProjectId = params.get("ProjectId")
        self._AppStatus = params.get("AppStatus")
        self._CreateTime = params.get("CreateTime")
        self._AppType = params.get("AppType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrConf(AbstractModel):
    """语音转文本配置数据

    """

    def __init__(self):
        r"""
        :param _Status: 语音转文本服务开关，取值：open/close
        :type Status: str
        """
        self._Status = None

    @property
    def Status(self):
        """语音转文本服务开关，取值：open/close
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTextStatisticsItem(AbstractModel):
    """录音转文本用量统计数据

    """

    def __init__(self):
        r"""
        :param _Data: 统计值，单位：秒
        :type Data: float
        """
        self._Data = None

    @property
    def Data(self):
        """统计值，单位：秒
        :rtype: float
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgeDetectTaskRequest(AbstractModel):
    """CreateAgeDetectTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 应用id
        :type BizId: int
        :param _Tasks: 语音检测子任务列表，列表最多支持100个检测子任务。结构体中包含：
<li>DataId：数据的唯一ID</li>
<li>Url：数据文件的url，为 urlencode 编码，流式则为拉流地址</li>
        :type Tasks: list of AgeDetectTask
        :param _Callback: 任务结束时gme后台会自动触发回调
        :type Callback: str
        """
        self._BizId = None
        self._Tasks = None
        self._Callback = None

    @property
    def BizId(self):
        """应用id
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def Tasks(self):
        """语音检测子任务列表，列表最多支持100个检测子任务。结构体中包含：
<li>DataId：数据的唯一ID</li>
<li>Url：数据文件的url，为 urlencode 编码，流式则为拉流地址</li>
        :rtype: list of AgeDetectTask
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def Callback(self):
        """任务结束时gme后台会自动触发回调
        :rtype: str
        """
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = AgeDetectTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgeDetectTaskResponse(AbstractModel):
    """CreateAgeDetectTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 本次任务提交后唯一id，用于获取任务运行结果
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """本次任务提交后唯一id，用于获取任务运行结果
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateAppRequest(AbstractModel):
    """CreateApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称
        :type AppName: str
        :param _ProjectId: 腾讯云项目ID，默认为0，表示默认项目
        :type ProjectId: int
        :param _EngineList: 需要支持的引擎列表，默认全选。
取值：android/ios/unity/cocos/unreal/windows
        :type EngineList: list of str
        :param _RegionList: 服务区域列表，默认全选。
取值：mainland-大陆地区，hmt-港澳台，sea-东南亚，na-北美，eu-欧洲，jpkr-日韩亚太，sa-南美，oc-澳洲，me-中东
        :type RegionList: list of str
        :param _RealtimeSpeechConf: 实时语音服务配置数据
        :type RealtimeSpeechConf: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`
        :param _VoiceMessageConf: 语音消息服务配置数据
        :type VoiceMessageConf: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`
        :param _VoiceFilterConf: 语音分析服务配置数据
        :type VoiceFilterConf: :class:`tencentcloud.gme.v20180711.models.VoiceFilterConf`
        :param _AsrConf: 语音转文本配置数据
        :type AsrConf: :class:`tencentcloud.gme.v20180711.models.AsrConf`
        :param _Tags: 需要添加的标签列表
        :type Tags: list of Tag
        """
        self._AppName = None
        self._ProjectId = None
        self._EngineList = None
        self._RegionList = None
        self._RealtimeSpeechConf = None
        self._VoiceMessageConf = None
        self._VoiceFilterConf = None
        self._AsrConf = None
        self._Tags = None

    @property
    def AppName(self):
        """应用名称
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def ProjectId(self):
        """腾讯云项目ID，默认为0，表示默认项目
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def EngineList(self):
        """需要支持的引擎列表，默认全选。
取值：android/ios/unity/cocos/unreal/windows
        :rtype: list of str
        """
        return self._EngineList

    @EngineList.setter
    def EngineList(self, EngineList):
        self._EngineList = EngineList

    @property
    def RegionList(self):
        """服务区域列表，默认全选。
取值：mainland-大陆地区，hmt-港澳台，sea-东南亚，na-北美，eu-欧洲，jpkr-日韩亚太，sa-南美，oc-澳洲，me-中东
        :rtype: list of str
        """
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def RealtimeSpeechConf(self):
        """实时语音服务配置数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`
        """
        return self._RealtimeSpeechConf

    @RealtimeSpeechConf.setter
    def RealtimeSpeechConf(self, RealtimeSpeechConf):
        self._RealtimeSpeechConf = RealtimeSpeechConf

    @property
    def VoiceMessageConf(self):
        """语音消息服务配置数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`
        """
        return self._VoiceMessageConf

    @VoiceMessageConf.setter
    def VoiceMessageConf(self, VoiceMessageConf):
        self._VoiceMessageConf = VoiceMessageConf

    @property
    def VoiceFilterConf(self):
        """语音分析服务配置数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.VoiceFilterConf`
        """
        return self._VoiceFilterConf

    @VoiceFilterConf.setter
    def VoiceFilterConf(self, VoiceFilterConf):
        self._VoiceFilterConf = VoiceFilterConf

    @property
    def AsrConf(self):
        """语音转文本配置数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.AsrConf`
        """
        return self._AsrConf

    @AsrConf.setter
    def AsrConf(self, AsrConf):
        self._AsrConf = AsrConf

    @property
    def Tags(self):
        """需要添加的标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._ProjectId = params.get("ProjectId")
        self._EngineList = params.get("EngineList")
        self._RegionList = params.get("RegionList")
        if params.get("RealtimeSpeechConf") is not None:
            self._RealtimeSpeechConf = RealtimeSpeechConf()
            self._RealtimeSpeechConf._deserialize(params.get("RealtimeSpeechConf"))
        if params.get("VoiceMessageConf") is not None:
            self._VoiceMessageConf = VoiceMessageConf()
            self._VoiceMessageConf._deserialize(params.get("VoiceMessageConf"))
        if params.get("VoiceFilterConf") is not None:
            self._VoiceFilterConf = VoiceFilterConf()
            self._VoiceFilterConf._deserialize(params.get("VoiceFilterConf"))
        if params.get("AsrConf") is not None:
            self._AsrConf = AsrConf()
            self._AsrConf._deserialize(params.get("AsrConf"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppResp(AbstractModel):
    """CreateApp的输出参数

    """

    def __init__(self):
        r"""
        :param _BizId: 应用ID，由后台自动生成。
        :type BizId: int
        :param _AppName: 应用名称，透传输入参数的AppName
        :type AppName: str
        :param _ProjectId: 项目ID，透传输入的ProjectId
        :type ProjectId: int
        :param _SecretKey: 应用密钥，GME SDK初始化时使用
        :type SecretKey: str
        :param _CreateTime: 服务创建时间戳
        :type CreateTime: int
        :param _RealtimeSpeechConf: 实时语音服务配置数据
        :type RealtimeSpeechConf: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`
        :param _VoiceMessageConf: 语音消息服务配置数据
        :type VoiceMessageConf: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`
        :param _VoiceFilterConf: 语音分析服务配置数据
        :type VoiceFilterConf: :class:`tencentcloud.gme.v20180711.models.VoiceFilterConf`
        :param _AsrConf: 语音转文本服务配置数据
        :type AsrConf: :class:`tencentcloud.gme.v20180711.models.AsrConf`
        """
        self._BizId = None
        self._AppName = None
        self._ProjectId = None
        self._SecretKey = None
        self._CreateTime = None
        self._RealtimeSpeechConf = None
        self._VoiceMessageConf = None
        self._VoiceFilterConf = None
        self._AsrConf = None

    @property
    def BizId(self):
        """应用ID，由后台自动生成。
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def AppName(self):
        """应用名称，透传输入参数的AppName
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def ProjectId(self):
        """项目ID，透传输入的ProjectId
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SecretKey(self):
        """应用密钥，GME SDK初始化时使用
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def CreateTime(self):
        """服务创建时间戳
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RealtimeSpeechConf(self):
        """实时语音服务配置数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.RealtimeSpeechConf`
        """
        return self._RealtimeSpeechConf

    @RealtimeSpeechConf.setter
    def RealtimeSpeechConf(self, RealtimeSpeechConf):
        self._RealtimeSpeechConf = RealtimeSpeechConf

    @property
    def VoiceMessageConf(self):
        """语音消息服务配置数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.VoiceMessageConf`
        """
        return self._VoiceMessageConf

    @VoiceMessageConf.setter
    def VoiceMessageConf(self, VoiceMessageConf):
        self._VoiceMessageConf = VoiceMessageConf

    @property
    def VoiceFilterConf(self):
        """语音分析服务配置数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.VoiceFilterConf`
        """
        return self._VoiceFilterConf

    @VoiceFilterConf.setter
    def VoiceFilterConf(self, VoiceFilterConf):
        self._VoiceFilterConf = VoiceFilterConf

    @property
    def AsrConf(self):
        """语音转文本服务配置数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.AsrConf`
        """
        return self._AsrConf

    @AsrConf.setter
    def AsrConf(self, AsrConf):
        self._AsrConf = AsrConf


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._AppName = params.get("AppName")
        self._ProjectId = params.get("ProjectId")
        self._SecretKey = params.get("SecretKey")
        self._CreateTime = params.get("CreateTime")
        if params.get("RealtimeSpeechConf") is not None:
            self._RealtimeSpeechConf = RealtimeSpeechConf()
            self._RealtimeSpeechConf._deserialize(params.get("RealtimeSpeechConf"))
        if params.get("VoiceMessageConf") is not None:
            self._VoiceMessageConf = VoiceMessageConf()
            self._VoiceMessageConf._deserialize(params.get("VoiceMessageConf"))
        if params.get("VoiceFilterConf") is not None:
            self._VoiceFilterConf = VoiceFilterConf()
            self._VoiceFilterConf._deserialize(params.get("VoiceFilterConf"))
        if params.get("AsrConf") is not None:
            self._AsrConf = AsrConf()
            self._AsrConf._deserialize(params.get("AsrConf"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppResponse(AbstractModel):
    """CreateApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 创建应用返回数据
        :type Data: :class:`tencentcloud.gme.v20180711.models.CreateAppResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """创建应用返回数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.CreateAppResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CreateAppResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateCustomizationRequest(AbstractModel):
    """CreateCustomization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 应用 ID，登录控制台创建应用得到的AppID
        :type BizId: int
        :param _TextUrl: 文本文件的下载地址，服务会从该地址下载文件，目前仅支持腾讯云cos
        :type TextUrl: str
        :param _ModelName: 模型名称，名称长度不超过36，默认为BizId。
        :type ModelName: str
        """
        self._BizId = None
        self._TextUrl = None
        self._ModelName = None

    @property
    def BizId(self):
        """应用 ID，登录控制台创建应用得到的AppID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def TextUrl(self):
        """文本文件的下载地址，服务会从该地址下载文件，目前仅支持腾讯云cos
        :rtype: str
        """
        return self._TextUrl

    @TextUrl.setter
    def TextUrl(self, TextUrl):
        self._TextUrl = TextUrl

    @property
    def ModelName(self):
        """模型名称，名称长度不超过36，默认为BizId。
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._TextUrl = params.get("TextUrl")
        self._ModelName = params.get("ModelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomizationResponse(AbstractModel):
    """CreateCustomization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型ID
        :type ModelId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelId = None
        self._RequestId = None

    @property
    def ModelId(self):
        """模型ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._RequestId = params.get("RequestId")


class CreateScanUserRequest(AbstractModel):
    """CreateScanUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 应用ID，登录控制台 - 服务管理创建应用得到的AppID
        :type BizId: int
        :param _UserId: 需要新增送检的用户号。示例：1234
(若UserId不填，则UserIdString必填；两者选其一；两者都填以UserIdString为准)
        :type UserId: int
        :param _UserIdString: 需要新增送检的用户号。示例："1234"
(若UserIdString不填，则UserId必填；两者选其一；两者都填以UserIdString为准)
        :type UserIdString: str
        :param _ExpirationTime: 当前用户送检过期时间，单位：秒。
若参数不为0，则在过期时间之后，用户不会被送检。
若参数为0，则送检配置不会自动失效。 
        :type ExpirationTime: int
        """
        self._BizId = None
        self._UserId = None
        self._UserIdString = None
        self._ExpirationTime = None

    @property
    def BizId(self):
        """应用ID，登录控制台 - 服务管理创建应用得到的AppID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def UserId(self):
        """需要新增送检的用户号。示例：1234
(若UserId不填，则UserIdString必填；两者选其一；两者都填以UserIdString为准)
        :rtype: int
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserIdString(self):
        """需要新增送检的用户号。示例："1234"
(若UserIdString不填，则UserId必填；两者选其一；两者都填以UserIdString为准)
        :rtype: str
        """
        return self._UserIdString

    @UserIdString.setter
    def UserIdString(self, UserIdString):
        self._UserIdString = UserIdString

    @property
    def ExpirationTime(self):
        """当前用户送检过期时间，单位：秒。
若参数不为0，则在过期时间之后，用户不会被送检。
若参数为0，则送检配置不会自动失效。 
        :rtype: int
        """
        return self._ExpirationTime

    @ExpirationTime.setter
    def ExpirationTime(self, ExpirationTime):
        self._ExpirationTime = ExpirationTime


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._UserId = params.get("UserId")
        self._UserIdString = params.get("UserIdString")
        self._ExpirationTime = params.get("ExpirationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScanUserResponse(AbstractModel):
    """CreateScanUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorCode: 返回结果码
        :type ErrorCode: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorCode = None
        self._RequestId = None

    @property
    def ErrorCode(self):
        """返回结果码
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._RequestId = params.get("RequestId")


class CustomizationConfigs(AbstractModel):
    """语音消息转文本热句模型配置

    """

    def __init__(self):
        r"""
        :param _BizId: 应用 ID，登录控制台创建应用得到的AppID
        :type BizId: int
        :param _ModelId: 模型ID
        :type ModelId: str
        :param _ModelState: 模型状态，-1下线状态，1上线状态, 0训练中, -2训练失败, 3上线中, 4下线中
        :type ModelState: int
        :param _ModelName: 模型名称
        :type ModelName: str
        :param _TextUrl: 文本文件的下载地址，服务会从该地址下载文件，目前仅支持腾讯云cos
        :type TextUrl: str
        :param _UpdateTime: 更新时间，11位时间戳
        :type UpdateTime: int
        """
        self._BizId = None
        self._ModelId = None
        self._ModelState = None
        self._ModelName = None
        self._TextUrl = None
        self._UpdateTime = None

    @property
    def BizId(self):
        """应用 ID，登录控制台创建应用得到的AppID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def ModelId(self):
        """模型ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelState(self):
        """模型状态，-1下线状态，1上线状态, 0训练中, -2训练失败, 3上线中, 4下线中
        :rtype: int
        """
        return self._ModelState

    @ModelState.setter
    def ModelState(self, ModelState):
        self._ModelState = ModelState

    @property
    def ModelName(self):
        """模型名称
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def TextUrl(self):
        """文本文件的下载地址，服务会从该地址下载文件，目前仅支持腾讯云cos
        :rtype: str
        """
        return self._TextUrl

    @TextUrl.setter
    def TextUrl(self, TextUrl):
        self._TextUrl = TextUrl

    @property
    def UpdateTime(self):
        """更新时间，11位时间戳
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._ModelId = params.get("ModelId")
        self._ModelState = params.get("ModelState")
        self._ModelName = params.get("ModelName")
        self._TextUrl = params.get("TextUrl")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomizationRequest(AbstractModel):
    """DeleteCustomization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 删除的模型ID
        :type ModelId: str
        :param _BizId: 应用 ID，登录控制台创建应用得到的AppID
        :type BizId: int
        """
        self._ModelId = None
        self._BizId = None

    @property
    def ModelId(self):
        """删除的模型ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def BizId(self):
        """应用 ID，登录控制台创建应用得到的AppID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomizationResponse(AbstractModel):
    """DeleteCustomization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorCode: 返回值。0为成功，非0为失败。
        :type ErrorCode: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorCode = None
        self._RequestId = None

    @property
    def ErrorCode(self):
        """返回值。0为成功，非0为失败。
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._RequestId = params.get("RequestId")


class DeleteResult(AbstractModel):
    """剔除房间操作结果

    """

    def __init__(self):
        r"""
        :param _Code: 错误码，0-剔除成功 其他-剔除失败
        :type Code: int
        :param _ErrorMsg: 错误描述
        :type ErrorMsg: str
        """
        self._Code = None
        self._ErrorMsg = None

    @property
    def Code(self):
        """错误码，0-剔除成功 其他-剔除失败
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def ErrorMsg(self):
        """错误描述
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoomMemberRequest(AbstractModel):
    """DeleteRoomMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 要操作的房间id
        :type RoomId: str
        :param _DeleteType: 剔除类型 1-删除房间 2-剔除用户
        :type DeleteType: int
        :param _BizId: 应用id
        :type BizId: int
        :param _Uids: 要剔除的用户列表（整型）
        :type Uids: list of str
        :param _StrUids: 要剔除的用户列表（字符串类型）
        :type StrUids: list of str
        """
        self._RoomId = None
        self._DeleteType = None
        self._BizId = None
        self._Uids = None
        self._StrUids = None

    @property
    def RoomId(self):
        """要操作的房间id
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def DeleteType(self):
        """剔除类型 1-删除房间 2-剔除用户
        :rtype: int
        """
        return self._DeleteType

    @DeleteType.setter
    def DeleteType(self, DeleteType):
        self._DeleteType = DeleteType

    @property
    def BizId(self):
        """应用id
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def Uids(self):
        """要剔除的用户列表（整型）
        :rtype: list of str
        """
        return self._Uids

    @Uids.setter
    def Uids(self, Uids):
        self._Uids = Uids

    @property
    def StrUids(self):
        """要剔除的用户列表（字符串类型）
        :rtype: list of str
        """
        return self._StrUids

    @StrUids.setter
    def StrUids(self, StrUids):
        self._StrUids = StrUids


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._DeleteType = params.get("DeleteType")
        self._BizId = params.get("BizId")
        self._Uids = params.get("Uids")
        self._StrUids = params.get("StrUids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoomMemberResponse(AbstractModel):
    """DeleteRoomMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeleteResult: 剔除房间或成员的操作结果
        :type DeleteResult: :class:`tencentcloud.gme.v20180711.models.DeleteResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeleteResult = None
        self._RequestId = None

    @property
    def DeleteResult(self):
        """剔除房间或成员的操作结果
        :rtype: :class:`tencentcloud.gme.v20180711.models.DeleteResult`
        """
        return self._DeleteResult

    @DeleteResult.setter
    def DeleteResult(self, DeleteResult):
        self._DeleteResult = DeleteResult

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeleteResult") is not None:
            self._DeleteResult = DeleteResult()
            self._DeleteResult._deserialize(params.get("DeleteResult"))
        self._RequestId = params.get("RequestId")


class DeleteScanUserRequest(AbstractModel):
    """DeleteScanUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 应用ID，登录控制台 - 服务管理创建应用得到的AppID
        :type BizId: int
        :param _UserId: 需要删除送检的用户号。示例：1234
(若UserId不填，则UserIdString必填；两者选其一；两者都填以UserIdString为准)
        :type UserId: int
        :param _UserIdString: 需要删除送检的用户号。示例："1234"
(若UserIdString不填，则UserId必填；两者选其一；两者都填以UserIdString为准)
        :type UserIdString: str
        """
        self._BizId = None
        self._UserId = None
        self._UserIdString = None

    @property
    def BizId(self):
        """应用ID，登录控制台 - 服务管理创建应用得到的AppID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def UserId(self):
        """需要删除送检的用户号。示例：1234
(若UserId不填，则UserIdString必填；两者选其一；两者都填以UserIdString为准)
        :rtype: int
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserIdString(self):
        """需要删除送检的用户号。示例："1234"
(若UserIdString不填，则UserId必填；两者选其一；两者都填以UserIdString为准)
        :rtype: str
        """
        return self._UserIdString

    @UserIdString.setter
    def UserIdString(self, UserIdString):
        self._UserIdString = UserIdString


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._UserId = params.get("UserId")
        self._UserIdString = params.get("UserIdString")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteScanUserResponse(AbstractModel):
    """DeleteScanUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorCode: 返回结果码
        :type ErrorCode: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorCode = None
        self._RequestId = None

    @property
    def ErrorCode(self):
        """返回结果码
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._RequestId = params.get("RequestId")


class DescribeAgeDetectTaskRequest(AbstractModel):
    """DescribeAgeDetectTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 应用id
        :type BizId: int
        :param _TaskId: [创建年龄语音识别任务](https://cloud.tencent.com/document/product/607/60620)时返回的taskid
        :type TaskId: str
        """
        self._BizId = None
        self._TaskId = None

    @property
    def BizId(self):
        """应用id
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def TaskId(self):
        """[创建年龄语音识别任务](https://cloud.tencent.com/document/product/607/60620)时返回的taskid
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgeDetectTaskResponse(AbstractModel):
    """DescribeAgeDetectTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _Results: 语音检测返回。Results 字段是 JSON 数组，每一个元素包含：
DataId： 请求中对应的 DataId。
Url ：该请求中对应的 Url。
Status ：子任务状态，0:已创建，1:运行中，2:已完成，3:任务异常，4:任务超时。
Age ：子任务完成后的结果，0:成年人，1:未成年人，100:未知结果。
        :type Results: list of AgeDetectTaskResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Results = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Results(self):
        """语音检测返回。Results 字段是 JSON 数组，每一个元素包含：
DataId： 请求中对应的 DataId。
Url ：该请求中对应的 Url。
Status ：子任务状态，0:已创建，1:运行中，2:已完成，3:任务异常，4:任务超时。
Age ：子任务完成后的结果，0:成年人，1:未成年人，100:未知结果。
        :rtype: list of AgeDetectTaskResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = AgeDetectTaskResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAppStatisticsRequest(AbstractModel):
    """DescribeAppStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: GME应用ID
        :type BizId: int
        :param _StartDate: 数据开始时间，东八区时间，格式: 年-月-日，如: 2018-07-13
        :type StartDate: str
        :param _EndDate: 数据结束时间，东八区时间，格式: 年-月-日，如: 2018-07-13
        :type EndDate: str
        :param _Services: 要查询的服务列表，取值：RealTimeSpeech/VoiceMessage/VoiceFilter/SpeechToText
        :type Services: list of str
        """
        self._BizId = None
        self._StartDate = None
        self._EndDate = None
        self._Services = None

    @property
    def BizId(self):
        """GME应用ID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def StartDate(self):
        """数据开始时间，东八区时间，格式: 年-月-日，如: 2018-07-13
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """数据结束时间，东八区时间，格式: 年-月-日，如: 2018-07-13
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Services(self):
        """要查询的服务列表，取值：RealTimeSpeech/VoiceMessage/VoiceFilter/SpeechToText
        :rtype: list of str
        """
        return self._Services

    @Services.setter
    def Services(self, Services):
        self._Services = Services


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Services = params.get("Services")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppStatisticsResp(AbstractModel):
    """获取应用用量统计数据输出参数

    """

    def __init__(self):
        r"""
        :param _AppStatistics: 应用用量统计数据
        :type AppStatistics: list of AppStatisticsItem
        """
        self._AppStatistics = None

    @property
    def AppStatistics(self):
        """应用用量统计数据
        :rtype: list of AppStatisticsItem
        """
        return self._AppStatistics

    @AppStatistics.setter
    def AppStatistics(self, AppStatistics):
        self._AppStatistics = AppStatistics


    def _deserialize(self, params):
        if params.get("AppStatistics") is not None:
            self._AppStatistics = []
            for item in params.get("AppStatistics"):
                obj = AppStatisticsItem()
                obj._deserialize(item)
                self._AppStatistics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppStatisticsResponse(AbstractModel):
    """DescribeAppStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 应用用量统计数据
        :type Data: :class:`tencentcloud.gme.v20180711.models.DescribeAppStatisticsResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """应用用量统计数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeAppStatisticsResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeAppStatisticsResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationDataRequest(AbstractModel):
    """DescribeApplicationData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 应用ID
        :type BizId: int
        :param _StartDate: 数据开始时间，格式为 年-月-日，如: 2018-07-13
        :type StartDate: str
        :param _EndDate: 数据结束时间，格式为 年-月-日，如: 2018-07-13
        :type EndDate: str
        """
        self._BizId = None
        self._StartDate = None
        self._EndDate = None

    @property
    def BizId(self):
        """应用ID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def StartDate(self):
        """数据开始时间，格式为 年-月-日，如: 2018-07-13
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """数据结束时间，格式为 年-月-日，如: 2018-07-13
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationDataResponse(AbstractModel):
    """DescribeApplicationData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 应用统计数据
        :type Data: :class:`tencentcloud.gme.v20180711.models.ApplicationDataStatistics`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """应用统计数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.ApplicationDataStatistics`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ApplicationDataStatistics()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationListRequest(AbstractModel):
    """DescribeApplicationList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID，0表示默认项目，-1表示所有项目，如果需要查找具体项目下的应用列表，请填入具体项目ID，项目ID在项目管理中查看 https://console.cloud.tencent.com/project
        :type ProjectId: int
        :param _PageNo: 页码ID，0表示第一页，以此后推。默认填0
        :type PageNo: int
        :param _PageSize: 每页展示应用数量。默认填200
        :type PageSize: int
        :param _SearchText: 所查找应用名称的关键字，支持模糊匹配查找。空串表示查询所有应用
        :type SearchText: str
        :param _TagSet: 标签列表
        :type TagSet: list of Tag
        :param _Filters: 查找过滤关键字列表
        :type Filters: list of Filter
        """
        self._ProjectId = None
        self._PageNo = None
        self._PageSize = None
        self._SearchText = None
        self._TagSet = None
        self._Filters = None

    @property
    def ProjectId(self):
        """项目ID，0表示默认项目，-1表示所有项目，如果需要查找具体项目下的应用列表，请填入具体项目ID，项目ID在项目管理中查看 https://console.cloud.tencent.com/project
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNo(self):
        """页码ID，0表示第一页，以此后推。默认填0
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        """每页展示应用数量。默认填200
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SearchText(self):
        """所查找应用名称的关键字，支持模糊匹配查找。空串表示查询所有应用
        :rtype: str
        """
        return self._SearchText

    @SearchText.setter
    def SearchText(self, SearchText):
        self._SearchText = SearchText

    @property
    def TagSet(self):
        """标签列表
        :rtype: list of Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def Filters(self):
        """查找过滤关键字列表
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._SearchText = params.get("SearchText")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationListResponse(AbstractModel):
    """DescribeApplicationList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationList: 获取应用列表返回
        :type ApplicationList: list of ApplicationList
        :param _Total: 应用总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicationList = None
        self._Total = None
        self._RequestId = None

    @property
    def ApplicationList(self):
        """获取应用列表返回
        :rtype: list of ApplicationList
        """
        return self._ApplicationList

    @ApplicationList.setter
    def ApplicationList(self, ApplicationList):
        self._ApplicationList = ApplicationList

    @property
    def Total(self):
        """应用总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ApplicationList") is not None:
            self._ApplicationList = []
            for item in params.get("ApplicationList"):
                obj = ApplicationList()
                obj._deserialize(item)
                self._ApplicationList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeRealtimeScanConfigRequest(AbstractModel):
    """DescribeRealtimeScanConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 应用ID。
        :type BizId: int
        """
        self._BizId = None

    @property
    def BizId(self):
        """应用ID。
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRealtimeScanConfigResponse(AbstractModel):
    """DescribeRealtimeScanConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorCode: 返回结果码，0正常，非0失败
        :type ErrorCode: int
        :param _BizId: 应用ID
        :type BizId: int
        :param _AuditType: 送检类型，0: 全量送审，1: 自定义送审
        :type AuditType: int
        :param _UserIdRegex: 用户号正则表达式。
符合此正则表达式规则的用户号将被送检。示例：^6.*（表示所有以6开头的用户号将被送检）
        :type UserIdRegex: list of str
        :param _RoomIdRegex: 房间号正则表达式。
符合此正则表达式规则的房间号将被送检。示例：^6.*（表示所有以6开头的房间号将被送检）
        :type RoomIdRegex: list of str
        :param _UserIdString: 用户号字符串，逗号分隔，示例："0001,0002,0003"
        :type UserIdString: str
        :param _RoomIdString: 房间号字符串，逗号分隔，示例："0001,0002,0003"
        :type RoomIdString: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorCode = None
        self._BizId = None
        self._AuditType = None
        self._UserIdRegex = None
        self._RoomIdRegex = None
        self._UserIdString = None
        self._RoomIdString = None
        self._RequestId = None

    @property
    def ErrorCode(self):
        """返回结果码，0正常，非0失败
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def BizId(self):
        """应用ID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def AuditType(self):
        """送检类型，0: 全量送审，1: 自定义送审
        :rtype: int
        """
        return self._AuditType

    @AuditType.setter
    def AuditType(self, AuditType):
        self._AuditType = AuditType

    @property
    def UserIdRegex(self):
        """用户号正则表达式。
符合此正则表达式规则的用户号将被送检。示例：^6.*（表示所有以6开头的用户号将被送检）
        :rtype: list of str
        """
        return self._UserIdRegex

    @UserIdRegex.setter
    def UserIdRegex(self, UserIdRegex):
        self._UserIdRegex = UserIdRegex

    @property
    def RoomIdRegex(self):
        """房间号正则表达式。
符合此正则表达式规则的房间号将被送检。示例：^6.*（表示所有以6开头的房间号将被送检）
        :rtype: list of str
        """
        return self._RoomIdRegex

    @RoomIdRegex.setter
    def RoomIdRegex(self, RoomIdRegex):
        self._RoomIdRegex = RoomIdRegex

    @property
    def UserIdString(self):
        """用户号字符串，逗号分隔，示例："0001,0002,0003"
        :rtype: str
        """
        return self._UserIdString

    @UserIdString.setter
    def UserIdString(self, UserIdString):
        self._UserIdString = UserIdString

    @property
    def RoomIdString(self):
        """房间号字符串，逗号分隔，示例："0001,0002,0003"
        :rtype: str
        """
        return self._RoomIdString

    @RoomIdString.setter
    def RoomIdString(self, RoomIdString):
        self._RoomIdString = RoomIdString

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._BizId = params.get("BizId")
        self._AuditType = params.get("AuditType")
        self._UserIdRegex = params.get("UserIdRegex")
        self._RoomIdRegex = params.get("RoomIdRegex")
        self._UserIdString = params.get("UserIdString")
        self._RoomIdString = params.get("RoomIdString")
        self._RequestId = params.get("RequestId")


class DescribeRecordInfoRequest(AbstractModel):
    """DescribeRecordInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 进行中的任务taskid（StartRecord接口返回）。
        :type TaskId: int
        :param _BizId: 应用ID。
        :type BizId: int
        """
        self._TaskId = None
        self._BizId = None

    @property
    def TaskId(self):
        """进行中的任务taskid（StartRecord接口返回）。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def BizId(self):
        """应用ID。
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordInfoResponse(AbstractModel):
    """DescribeRecordInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordInfo: 录制信息。
        :type RecordInfo: list of RecordInfo
        :param _RecordMode: 录制类型：1代表单流 2代表混流 3代表单流和混流。
        :type RecordMode: int
        :param _RoomId: 房间ID。
        :type RoomId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordInfo = None
        self._RecordMode = None
        self._RoomId = None
        self._RequestId = None

    @property
    def RecordInfo(self):
        """录制信息。
        :rtype: list of RecordInfo
        """
        return self._RecordInfo

    @RecordInfo.setter
    def RecordInfo(self, RecordInfo):
        self._RecordInfo = RecordInfo

    @property
    def RecordMode(self):
        """录制类型：1代表单流 2代表混流 3代表单流和混流。
        :rtype: int
        """
        return self._RecordMode

    @RecordMode.setter
    def RecordMode(self, RecordMode):
        self._RecordMode = RecordMode

    @property
    def RoomId(self):
        """房间ID。
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RecordInfo") is not None:
            self._RecordInfo = []
            for item in params.get("RecordInfo"):
                obj = RecordInfo()
                obj._deserialize(item)
                self._RecordInfo.append(obj)
        self._RecordMode = params.get("RecordMode")
        self._RoomId = params.get("RoomId")
        self._RequestId = params.get("RequestId")


class DescribeRoomInfoRequest(AbstractModel):
    """DescribeRoomInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用ID，登录[控制台 - 服务管理](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID
        :type SdkAppId: int
        :param _RoomIds: 房间号列表，最大不能超过10个（RoomIds、StrRoomIds必须填一个）
        :type RoomIds: list of int non-negative
        :param _StrRoomIds: 字符串类型房间号列表，最大不能超过10个（RoomIds、StrRoomIds必须填一个）
        :type StrRoomIds: list of str
        """
        self._SdkAppId = None
        self._RoomIds = None
        self._StrRoomIds = None

    @property
    def SdkAppId(self):
        """应用ID，登录[控制台 - 服务管理](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomIds(self):
        """房间号列表，最大不能超过10个（RoomIds、StrRoomIds必须填一个）
        :rtype: list of int non-negative
        """
        return self._RoomIds

    @RoomIds.setter
    def RoomIds(self, RoomIds):
        self._RoomIds = RoomIds

    @property
    def StrRoomIds(self):
        """字符串类型房间号列表，最大不能超过10个（RoomIds、StrRoomIds必须填一个）
        :rtype: list of str
        """
        return self._StrRoomIds

    @StrRoomIds.setter
    def StrRoomIds(self, StrRoomIds):
        self._StrRoomIds = StrRoomIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomIds = params.get("RoomIds")
        self._StrRoomIds = params.get("StrRoomIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomInfoResponse(AbstractModel):
    """DescribeRoomInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 操作结果, 0成功, 非0失败
        :type Result: int
        :param _RoomUsers: 房间用户信息
        :type RoomUsers: list of RoomUser
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RoomUsers = None
        self._RequestId = None

    @property
    def Result(self):
        """操作结果, 0成功, 非0失败
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RoomUsers(self):
        """房间用户信息
        :rtype: list of RoomUser
        """
        return self._RoomUsers

    @RoomUsers.setter
    def RoomUsers(self, RoomUsers):
        self._RoomUsers = RoomUsers

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        if params.get("RoomUsers") is not None:
            self._RoomUsers = []
            for item in params.get("RoomUsers"):
                obj = RoomUser()
                obj._deserialize(item)
                self._RoomUsers.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScanResult(AbstractModel):
    """语音检测结果返回

    """

    def __init__(self):
        r"""
        :param _Code: 业务返回码
        :type Code: int
        :param _DataId: 数据唯一 ID
        :type DataId: str
        :param _ScanFinishTime: 检测完成的时间戳
        :type ScanFinishTime: int
        :param _HitFlag: 是否违规
        :type HitFlag: bool
        :param _Live: 是否为流
        :type Live: bool
        :param _Msg: 业务返回描述
        :type Msg: str
        :param _ScanPiece: 检测结果，Code 为 0 时返回
        :type ScanPiece: list of ScanPiece
        :param _ScanStartTime: 提交检测的时间戳
        :type ScanStartTime: int
        :param _Scenes: 语音检测场景，对应请求时的 Scene
        :type Scenes: list of str
        :param _TaskId: 语音检测任务 ID，由后台分配
        :type TaskId: str
        :param _Url: 文件或接流地址
        :type Url: str
        :param _Status: 检测任务执行结果状态，分别为：
<li>Start: 任务开始</li>
<li>Success: 成功结束</li>
<li>Error: 异常</li>
        :type Status: str
        :param _BizId: 提交检测的应用 ID
        :type BizId: int
        """
        self._Code = None
        self._DataId = None
        self._ScanFinishTime = None
        self._HitFlag = None
        self._Live = None
        self._Msg = None
        self._ScanPiece = None
        self._ScanStartTime = None
        self._Scenes = None
        self._TaskId = None
        self._Url = None
        self._Status = None
        self._BizId = None

    @property
    def Code(self):
        """业务返回码
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def DataId(self):
        """数据唯一 ID
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def ScanFinishTime(self):
        """检测完成的时间戳
        :rtype: int
        """
        return self._ScanFinishTime

    @ScanFinishTime.setter
    def ScanFinishTime(self, ScanFinishTime):
        self._ScanFinishTime = ScanFinishTime

    @property
    def HitFlag(self):
        """是否违规
        :rtype: bool
        """
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

    @property
    def Live(self):
        """是否为流
        :rtype: bool
        """
        return self._Live

    @Live.setter
    def Live(self, Live):
        self._Live = Live

    @property
    def Msg(self):
        """业务返回描述
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def ScanPiece(self):
        """检测结果，Code 为 0 时返回
        :rtype: list of ScanPiece
        """
        return self._ScanPiece

    @ScanPiece.setter
    def ScanPiece(self, ScanPiece):
        self._ScanPiece = ScanPiece

    @property
    def ScanStartTime(self):
        """提交检测的时间戳
        :rtype: int
        """
        return self._ScanStartTime

    @ScanStartTime.setter
    def ScanStartTime(self, ScanStartTime):
        self._ScanStartTime = ScanStartTime

    @property
    def Scenes(self):
        """语音检测场景，对应请求时的 Scene
        :rtype: list of str
        """
        return self._Scenes

    @Scenes.setter
    def Scenes(self, Scenes):
        self._Scenes = Scenes

    @property
    def TaskId(self):
        """语音检测任务 ID，由后台分配
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Url(self):
        """文件或接流地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Status(self):
        """检测任务执行结果状态，分别为：
<li>Start: 任务开始</li>
<li>Success: 成功结束</li>
<li>Error: 异常</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BizId(self):
        """提交检测的应用 ID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._DataId = params.get("DataId")
        self._ScanFinishTime = params.get("ScanFinishTime")
        self._HitFlag = params.get("HitFlag")
        self._Live = params.get("Live")
        self._Msg = params.get("Msg")
        if params.get("ScanPiece") is not None:
            self._ScanPiece = []
            for item in params.get("ScanPiece"):
                obj = ScanPiece()
                obj._deserialize(item)
                self._ScanPiece.append(obj)
        self._ScanStartTime = params.get("ScanStartTime")
        self._Scenes = params.get("Scenes")
        self._TaskId = params.get("TaskId")
        self._Url = params.get("Url")
        self._Status = params.get("Status")
        self._BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanResultListRequest(AbstractModel):
    """DescribeScanResultList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 应用 ID，登录[控制台](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID
        :type BizId: int
        :param _TaskIdList: 查询的任务 ID 列表，任务 ID 列表最多支持 100 个。
        :type TaskIdList: list of str
        :param _Limit: 任务返回结果数量，默认10，上限500。大文件任务忽略此参数，返回全量结果
        :type Limit: int
        """
        self._BizId = None
        self._TaskIdList = None
        self._Limit = None

    @property
    def BizId(self):
        """应用 ID，登录[控制台](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def TaskIdList(self):
        """查询的任务 ID 列表，任务 ID 列表最多支持 100 个。
        :rtype: list of str
        """
        return self._TaskIdList

    @TaskIdList.setter
    def TaskIdList(self, TaskIdList):
        self._TaskIdList = TaskIdList

    @property
    def Limit(self):
        """任务返回结果数量，默认10，上限500。大文件任务忽略此参数，返回全量结果
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._TaskIdList = params.get("TaskIdList")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanResultListResponse(AbstractModel):
    """DescribeScanResultList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 要查询的语音检测任务的结果
        :type Data: list of DescribeScanResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """要查询的语音检测任务的结果
        :rtype: list of DescribeScanResult
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeScanResult()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskInfoRequest(AbstractModel):
    """DescribeTaskInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 应用ID。
        :type BizId: int
        :param _RoomId: 房间ID。
        :type RoomId: str
        """
        self._BizId = None
        self._RoomId = None

    @property
    def BizId(self):
        """应用ID。
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def RoomId(self):
        """房间ID。
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskInfoResponse(AbstractModel):
    """DescribeTaskInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 进行中的任务taskid（StartRecord接口返回）。
        :type TaskId: int
        :param _RecordMode: 录制类型：1代表单流 2代表混流 3代表单流和混流。
        :type RecordMode: int
        :param _SubscribeRecordUserIds: 指定订阅流白名单或者黑名单。
        :type SubscribeRecordUserIds: :class:`tencentcloud.gme.v20180711.models.SubscribeRecordUserIds`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RecordMode = None
        self._SubscribeRecordUserIds = None
        self._RequestId = None

    @property
    def TaskId(self):
        """进行中的任务taskid（StartRecord接口返回）。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RecordMode(self):
        """录制类型：1代表单流 2代表混流 3代表单流和混流。
        :rtype: int
        """
        return self._RecordMode

    @RecordMode.setter
    def RecordMode(self, RecordMode):
        self._RecordMode = RecordMode

    @property
    def SubscribeRecordUserIds(self):
        """指定订阅流白名单或者黑名单。
        :rtype: :class:`tencentcloud.gme.v20180711.models.SubscribeRecordUserIds`
        """
        return self._SubscribeRecordUserIds

    @SubscribeRecordUserIds.setter
    def SubscribeRecordUserIds(self, SubscribeRecordUserIds):
        self._SubscribeRecordUserIds = SubscribeRecordUserIds

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RecordMode = params.get("RecordMode")
        if params.get("SubscribeRecordUserIds") is not None:
            self._SubscribeRecordUserIds = SubscribeRecordUserIds()
            self._SubscribeRecordUserIds._deserialize(params.get("SubscribeRecordUserIds"))
        self._RequestId = params.get("RequestId")


class DescribeUserInAndOutTimeRequest(AbstractModel):
    """DescribeUserInAndOutTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 应用ID
        :type BizId: int
        :param _RoomId: 房间ID
        :type RoomId: int
        :param _UserId: 用户ID
        :type UserId: int
        :param _UserIdStr: 字符串类型用户ID
        :type UserIdStr: str
        :param _RoomIdStr: 字符串类型房间ID
        :type RoomIdStr: str
        """
        self._BizId = None
        self._RoomId = None
        self._UserId = None
        self._UserIdStr = None
        self._RoomIdStr = None

    @property
    def BizId(self):
        """应用ID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def RoomId(self):
        """房间ID
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        """用户ID
        :rtype: int
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserIdStr(self):
        """字符串类型用户ID
        :rtype: str
        """
        return self._UserIdStr

    @UserIdStr.setter
    def UserIdStr(self, UserIdStr):
        self._UserIdStr = UserIdStr

    @property
    def RoomIdStr(self):
        """字符串类型房间ID
        :rtype: str
        """
        return self._RoomIdStr

    @RoomIdStr.setter
    def RoomIdStr(self, RoomIdStr):
        self._RoomIdStr = RoomIdStr


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._RoomId = params.get("RoomId")
        self._UserId = params.get("UserId")
        self._UserIdStr = params.get("UserIdStr")
        self._RoomIdStr = params.get("RoomIdStr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserInAndOutTimeResponse(AbstractModel):
    """DescribeUserInAndOutTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InOutList: 用户在房间得进出时间列表
        :type InOutList: list of InOutTimeInfo
        :param _Duration: 用户在房间中总时长
        :type Duration: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InOutList = None
        self._Duration = None
        self._RequestId = None

    @property
    def InOutList(self):
        """用户在房间得进出时间列表
        :rtype: list of InOutTimeInfo
        """
        return self._InOutList

    @InOutList.setter
    def InOutList(self, InOutList):
        self._InOutList = InOutList

    @property
    def Duration(self):
        """用户在房间中总时长
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InOutList") is not None:
            self._InOutList = []
            for item in params.get("InOutList"):
                obj = InOutTimeInfo()
                obj._deserialize(item)
                self._InOutList.append(obj)
        self._Duration = params.get("Duration")
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """查找过滤

    """

    def __init__(self):
        r"""
        :param _Name: 要过滤的字段名, 比如"AppName"
        :type Name: str
        :param _Values: 多个关键字
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """要过滤的字段名, 比如"AppName"
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """多个关键字
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCustomizationListRequest(AbstractModel):
    """GetCustomizationList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 应用 ID，登录控制台创建应用得到的AppID
        :type BizId: int
        """
        self._BizId = None

    @property
    def BizId(self):
        """应用 ID，登录控制台创建应用得到的AppID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCustomizationListResponse(AbstractModel):
    """GetCustomizationList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomizationConfigs: 语音消息转文本热句模型配置
        :type CustomizationConfigs: list of CustomizationConfigs
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CustomizationConfigs = None
        self._RequestId = None

    @property
    def CustomizationConfigs(self):
        """语音消息转文本热句模型配置
        :rtype: list of CustomizationConfigs
        """
        return self._CustomizationConfigs

    @CustomizationConfigs.setter
    def CustomizationConfigs(self, CustomizationConfigs):
        self._CustomizationConfigs = CustomizationConfigs

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CustomizationConfigs") is not None:
            self._CustomizationConfigs = []
            for item in params.get("CustomizationConfigs"):
                obj = CustomizationConfigs()
                obj._deserialize(item)
                self._CustomizationConfigs.append(obj)
        self._RequestId = params.get("RequestId")


class InOutTimeInfo(AbstractModel):
    """房间内的事件

    """

    def __init__(self):
        r"""
        :param _StartTime: 进入房间时间
        :type StartTime: int
        :param _EndTime: 退出房间时间
        :type EndTime: int
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        """进入房间时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """退出房间时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppStatusRequest(AbstractModel):
    """ModifyAppStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 应用ID，创建应用后由后台生成并返回。
        :type BizId: int
        :param _Status: 应用状态，取值：open/close
        :type Status: str
        """
        self._BizId = None
        self._Status = None

    @property
    def BizId(self):
        """应用ID，创建应用后由后台生成并返回。
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def Status(self):
        """应用状态，取值：open/close
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppStatusResp(AbstractModel):
    """ModifyAppStatus接口输出参数

    """

    def __init__(self):
        r"""
        :param _BizId: GME应用ID
        :type BizId: int
        :param _Status: 应用状态，取值：open/close
        :type Status: str
        """
        self._BizId = None
        self._Status = None

    @property
    def BizId(self):
        """GME应用ID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def Status(self):
        """应用状态，取值：open/close
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppStatusResponse(AbstractModel):
    """ModifyAppStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 修改应用开关状态返回数据
        :type Data: :class:`tencentcloud.gme.v20180711.models.ModifyAppStatusResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """修改应用开关状态返回数据
        :rtype: :class:`tencentcloud.gme.v20180711.models.ModifyAppStatusResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ModifyAppStatusResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyCustomizationRequest(AbstractModel):
    """ModifyCustomization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 应用 ID，登录控制台创建应用得到的AppID
        :type BizId: int
        :param _TextUrl: 文本文件的下载地址，服务会从该地址下载文件，目前仅支持腾讯云cos
        :type TextUrl: str
        :param _ModelId: 修改的模型ID
        :type ModelId: str
        """
        self._BizId = None
        self._TextUrl = None
        self._ModelId = None

    @property
    def BizId(self):
        """应用 ID，登录控制台创建应用得到的AppID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def TextUrl(self):
        """文本文件的下载地址，服务会从该地址下载文件，目前仅支持腾讯云cos
        :rtype: str
        """
        return self._TextUrl

    @TextUrl.setter
    def TextUrl(self, TextUrl):
        self._TextUrl = TextUrl

    @property
    def ModelId(self):
        """修改的模型ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._TextUrl = params.get("TextUrl")
        self._ModelId = params.get("ModelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomizationResponse(AbstractModel):
    """ModifyCustomization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorCode: 返回值。0为成功，非0为失败。
        :type ErrorCode: int
        :param _ModelId: 模型ID
        :type ModelId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorCode = None
        self._ModelId = None
        self._RequestId = None

    @property
    def ErrorCode(self):
        """返回值。0为成功，非0为失败。
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ModelId(self):
        """模型ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._ModelId = params.get("ModelId")
        self._RequestId = params.get("RequestId")


class ModifyCustomizationStateRequest(AbstractModel):
    """ModifyCustomizationState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型ID
        :type ModelId: str
        :param _ToState: 想要变换的模型状态，-1代表下线，1代表上线
        :type ToState: int
        :param _BizId: 应用 ID，登录控制台创建应用得到的AppID
        :type BizId: int
        """
        self._ModelId = None
        self._ToState = None
        self._BizId = None

    @property
    def ModelId(self):
        """模型ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ToState(self):
        """想要变换的模型状态，-1代表下线，1代表上线
        :rtype: int
        """
        return self._ToState

    @ToState.setter
    def ToState(self, ToState):
        self._ToState = ToState

    @property
    def BizId(self):
        """应用 ID，登录控制台创建应用得到的AppID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._ToState = params.get("ToState")
        self._BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomizationStateResponse(AbstractModel):
    """ModifyCustomizationState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型ID
        :type ModelId: str
        :param _ErrorCode: 返回值。0为成功，非0为失败。
        :type ErrorCode: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelId = None
        self._ErrorCode = None
        self._RequestId = None

    @property
    def ModelId(self):
        """模型ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ErrorCode(self):
        """返回值。0为成功，非0为失败。
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._ErrorCode = params.get("ErrorCode")
        self._RequestId = params.get("RequestId")


class ModifyRecordInfoRequest(AbstractModel):
    """ModifyRecordInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 进行中的任务taskid（StartRecord接口返回）。
        :type TaskId: int
        :param _RecordMode: 录制类型：1代表单流 2代表混流 3代表单流和混流。
        :type RecordMode: int
        :param _BizId: 应用ID。
        :type BizId: int
        :param _SubscribeRecordUserIds: 指定订阅流白名单或者黑名单。
        :type SubscribeRecordUserIds: :class:`tencentcloud.gme.v20180711.models.SubscribeRecordUserIds`
        """
        self._TaskId = None
        self._RecordMode = None
        self._BizId = None
        self._SubscribeRecordUserIds = None

    @property
    def TaskId(self):
        """进行中的任务taskid（StartRecord接口返回）。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RecordMode(self):
        """录制类型：1代表单流 2代表混流 3代表单流和混流。
        :rtype: int
        """
        return self._RecordMode

    @RecordMode.setter
    def RecordMode(self, RecordMode):
        self._RecordMode = RecordMode

    @property
    def BizId(self):
        """应用ID。
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def SubscribeRecordUserIds(self):
        """指定订阅流白名单或者黑名单。
        :rtype: :class:`tencentcloud.gme.v20180711.models.SubscribeRecordUserIds`
        """
        return self._SubscribeRecordUserIds

    @SubscribeRecordUserIds.setter
    def SubscribeRecordUserIds(self, SubscribeRecordUserIds):
        self._SubscribeRecordUserIds = SubscribeRecordUserIds


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RecordMode = params.get("RecordMode")
        self._BizId = params.get("BizId")
        if params.get("SubscribeRecordUserIds") is not None:
            self._SubscribeRecordUserIds = SubscribeRecordUserIds()
            self._SubscribeRecordUserIds._deserialize(params.get("SubscribeRecordUserIds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordInfoResponse(AbstractModel):
    """ModifyRecordInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyUserMicStatusRequest(AbstractModel):
    """ModifyUserMicStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 来自 [腾讯云控制台](https://console.cloud.tencent.com/gamegme) 的 GME 服务提供的 AppID，获取请参考 [语音服务开通指引](https://cloud.tencent.com/document/product/607/10782#.E9.87.8D.E7.82.B9.E5.8F.82.E6.95.B0)。
        :type BizId: int
        :param _RoomId: 实时语音房间号。
        :type RoomId: str
        :param _Users: 需要操作的房间内用户以及该用户的目标麦克风状态。
        :type Users: list of UserMicStatus
        """
        self._BizId = None
        self._RoomId = None
        self._Users = None

    @property
    def BizId(self):
        """来自 [腾讯云控制台](https://console.cloud.tencent.com/gamegme) 的 GME 服务提供的 AppID，获取请参考 [语音服务开通指引](https://cloud.tencent.com/document/product/607/10782#.E9.87.8D.E7.82.B9.E5.8F.82.E6.95.B0)。
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def RoomId(self):
        """实时语音房间号。
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Users(self):
        """需要操作的房间内用户以及该用户的目标麦克风状态。
        :rtype: list of UserMicStatus
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._RoomId = params.get("RoomId")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = UserMicStatus()
                obj._deserialize(item)
                self._Users.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserMicStatusResponse(AbstractModel):
    """ModifyUserMicStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果：0为成功，非0为失败。
        :type Result: int
        :param _ErrMsg: 错误信息。
        :type ErrMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._ErrMsg = None
        self._RequestId = None

    @property
    def Result(self):
        """返回结果：0为成功，非0为失败。
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ErrMsg(self):
        """错误信息。
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._ErrMsg = params.get("ErrMsg")
        self._RequestId = params.get("RequestId")


class OverseaTextStatisticsItem(AbstractModel):
    """海外转文本用量数据

    """

    def __init__(self):
        r"""
        :param _Data: 统计值，单位：秒
        :type Data: float
        """
        self._Data = None

    @property
    def Data(self):
        """统计值，单位：秒
        :rtype: float
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealTimeSpeechStatisticsItem(AbstractModel):
    """实时语音用量统计数据

    """

    def __init__(self):
        r"""
        :param _MainLandDau: 大陆地区DAU
        :type MainLandDau: int
        :param _MainLandPcu: 大陆地区PCU
        :type MainLandPcu: int
        :param _MainLandDuration: 大陆地区总使用时长，单位为min
        :type MainLandDuration: int
        :param _OverseaDau: 海外地区DAU
        :type OverseaDau: int
        :param _OverseaPcu: 海外地区PCU
        :type OverseaPcu: int
        :param _OverseaDuration: 海外地区总使用时长，单位为min
        :type OverseaDuration: int
        """
        self._MainLandDau = None
        self._MainLandPcu = None
        self._MainLandDuration = None
        self._OverseaDau = None
        self._OverseaPcu = None
        self._OverseaDuration = None

    @property
    def MainLandDau(self):
        """大陆地区DAU
        :rtype: int
        """
        return self._MainLandDau

    @MainLandDau.setter
    def MainLandDau(self, MainLandDau):
        self._MainLandDau = MainLandDau

    @property
    def MainLandPcu(self):
        """大陆地区PCU
        :rtype: int
        """
        return self._MainLandPcu

    @MainLandPcu.setter
    def MainLandPcu(self, MainLandPcu):
        self._MainLandPcu = MainLandPcu

    @property
    def MainLandDuration(self):
        """大陆地区总使用时长，单位为min
        :rtype: int
        """
        return self._MainLandDuration

    @MainLandDuration.setter
    def MainLandDuration(self, MainLandDuration):
        self._MainLandDuration = MainLandDuration

    @property
    def OverseaDau(self):
        """海外地区DAU
        :rtype: int
        """
        return self._OverseaDau

    @OverseaDau.setter
    def OverseaDau(self, OverseaDau):
        self._OverseaDau = OverseaDau

    @property
    def OverseaPcu(self):
        """海外地区PCU
        :rtype: int
        """
        return self._OverseaPcu

    @OverseaPcu.setter
    def OverseaPcu(self, OverseaPcu):
        self._OverseaPcu = OverseaPcu

    @property
    def OverseaDuration(self):
        """海外地区总使用时长，单位为min
        :rtype: int
        """
        return self._OverseaDuration

    @OverseaDuration.setter
    def OverseaDuration(self, OverseaDuration):
        self._OverseaDuration = OverseaDuration


    def _deserialize(self, params):
        self._MainLandDau = params.get("MainLandDau")
        self._MainLandPcu = params.get("MainLandPcu")
        self._MainLandDuration = params.get("MainLandDuration")
        self._OverseaDau = params.get("OverseaDau")
        self._OverseaPcu = params.get("OverseaPcu")
        self._OverseaDuration = params.get("OverseaDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealtimeSpeechConf(AbstractModel):
    """实时语音配置数据

    """

    def __init__(self):
        r"""
        :param _Status: 实时语音服务开关，取值：open/close
        :type Status: str
        :param _Quality: 实时语音音质类型，取值：high-高音质 ordinary-普通音质
        :type Quality: str
        """
        self._Status = None
        self._Quality = None

    @property
    def Status(self):
        """实时语音服务开关，取值：open/close
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Quality(self):
        """实时语音音质类型，取值：high-高音质 ordinary-普通音质
        :rtype: str
        """
        return self._Quality

    @Quality.setter
    def Quality(self, Quality):
        self._Quality = Quality


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Quality = params.get("Quality")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealtimeTextStatisticsItem(AbstractModel):
    """实时语音转文本用量数据

    """

    def __init__(self):
        r"""
        :param _Data: 统计值，单位：秒
        :type Data: float
        """
        self._Data = None

    @property
    def Data(self):
        """统计值，单位：秒
        :rtype: float
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordInfo(AbstractModel):
    """房间内录制信息。
    注意：此字段可能返回 null，表示取不到有效值。

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID（当混流模式时，取值为0）。
        :type UserId: str
        :param _FileName: 录制文件名。
        :type FileName: str
        :param _RecordBeginTime: 录制开始时间（unix时间戳如：1234567868）。
        :type RecordBeginTime: int
        :param _RecordStatus: 录制状态：2代表正在录制  10代表等待转码  11代表正在转码  12正在上传  13代表上传完成  14代表通知用户完成。
        :type RecordStatus: int
        """
        self._UserId = None
        self._FileName = None
        self._RecordBeginTime = None
        self._RecordStatus = None

    @property
    def UserId(self):
        """用户ID（当混流模式时，取值为0）。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def FileName(self):
        """录制文件名。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def RecordBeginTime(self):
        """录制开始时间（unix时间戳如：1234567868）。
        :rtype: int
        """
        return self._RecordBeginTime

    @RecordBeginTime.setter
    def RecordBeginTime(self, RecordBeginTime):
        self._RecordBeginTime = RecordBeginTime

    @property
    def RecordStatus(self):
        """录制状态：2代表正在录制  10代表等待转码  11代表正在转码  12正在上传  13代表上传完成  14代表通知用户完成。
        :rtype: int
        """
        return self._RecordStatus

    @RecordStatus.setter
    def RecordStatus(self, RecordStatus):
        self._RecordStatus = RecordStatus


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._FileName = params.get("FileName")
        self._RecordBeginTime = params.get("RecordBeginTime")
        self._RecordStatus = params.get("RecordStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoomUser(AbstractModel):
    """房间内用户信息

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间id
        :type RoomId: int
        :param _Uins: 房间里用户uin列表
        :type Uins: list of int non-negative
        :param _StrRoomId: 字符串房间id
        :type StrRoomId: str
        :param _StrUins: 房间里用户字符串uin列表
        :type StrUins: list of str
        """
        self._RoomId = None
        self._Uins = None
        self._StrRoomId = None
        self._StrUins = None

    @property
    def RoomId(self):
        """房间id
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Uins(self):
        """房间里用户uin列表
        :rtype: list of int non-negative
        """
        return self._Uins

    @Uins.setter
    def Uins(self, Uins):
        self._Uins = Uins

    @property
    def StrRoomId(self):
        """字符串房间id
        :rtype: str
        """
        return self._StrRoomId

    @StrRoomId.setter
    def StrRoomId(self, StrRoomId):
        self._StrRoomId = StrRoomId

    @property
    def StrUins(self):
        """房间里用户字符串uin列表
        :rtype: list of str
        """
        return self._StrUins

    @StrUins.setter
    def StrUins(self, StrUins):
        self._StrUins = StrUins


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._Uins = params.get("Uins")
        self._StrRoomId = params.get("StrRoomId")
        self._StrUins = params.get("StrUins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanDetail(AbstractModel):
    """语音检测详情

    """

    def __init__(self):
        r"""
        :param _Label: 违规场景，参照<a href="https://cloud.tencent.com/document/product/607/37622#Label_Value">Label</a>定义
        :type Label: str
        :param _Rate: 该场景下概率[0.00,100.00],分值越大违规概率越高
        :type Rate: str
        :param _KeyWord: 违规关键字
        :type KeyWord: str
        :param _StartTime: 关键字在音频的开始时间，从0开始的偏移量，单位为毫秒，Label=moan时有效
        :type StartTime: int
        :param _EndTime: 关键字在音频的结束时间，从0开始的偏移量,，单位为毫秒，Label=moan时有效
        :type EndTime: int
        """
        self._Label = None
        self._Rate = None
        self._KeyWord = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Label(self):
        """违规场景，参照<a href="https://cloud.tencent.com/document/product/607/37622#Label_Value">Label</a>定义
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Rate(self):
        """该场景下概率[0.00,100.00],分值越大违规概率越高
        :rtype: str
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def KeyWord(self):
        """违规关键字
        :rtype: str
        """
        return self._KeyWord

    @KeyWord.setter
    def KeyWord(self, KeyWord):
        self._KeyWord = KeyWord

    @property
    def StartTime(self):
        """关键字在音频的开始时间，从0开始的偏移量，单位为毫秒，Label=moan时有效
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """关键字在音频的结束时间，从0开始的偏移量,，单位为毫秒，Label=moan时有效
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Rate = params.get("Rate")
        self._KeyWord = params.get("KeyWord")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanPiece(AbstractModel):
    """语音检测结果，Code 为 0 时返回

    """

    def __init__(self):
        r"""
        :param _DumpUrl: 流检测时返回，音频转存地址，保留30min
        :type DumpUrl: str
        :param _HitFlag: 是否违规
        :type HitFlag: bool
        :param _MainType: 违规主要类型
        :type MainType: str
        :param _ScanDetail: 语音检测详情
        :type ScanDetail: list of ScanDetail
        :param _RoomId: gme实时语音房间ID，透传任务传入时的RoomId
        :type RoomId: str
        :param _OpenId: gme实时语音用户ID，透传任务传入时的OpenId
        :type OpenId: str
        :param _Info: 备注
        :type Info: str
        :param _Offset: 流检测时分片在流中的偏移时间，单位毫秒
        :type Offset: int
        :param _Duration: 流检测时分片时长
        :type Duration: int
        :param _PieceStartTime: 分片开始检测时间
        :type PieceStartTime: int
        """
        self._DumpUrl = None
        self._HitFlag = None
        self._MainType = None
        self._ScanDetail = None
        self._RoomId = None
        self._OpenId = None
        self._Info = None
        self._Offset = None
        self._Duration = None
        self._PieceStartTime = None

    @property
    def DumpUrl(self):
        """流检测时返回，音频转存地址，保留30min
        :rtype: str
        """
        return self._DumpUrl

    @DumpUrl.setter
    def DumpUrl(self, DumpUrl):
        self._DumpUrl = DumpUrl

    @property
    def HitFlag(self):
        """是否违规
        :rtype: bool
        """
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

    @property
    def MainType(self):
        """违规主要类型
        :rtype: str
        """
        return self._MainType

    @MainType.setter
    def MainType(self, MainType):
        self._MainType = MainType

    @property
    def ScanDetail(self):
        """语音检测详情
        :rtype: list of ScanDetail
        """
        return self._ScanDetail

    @ScanDetail.setter
    def ScanDetail(self, ScanDetail):
        self._ScanDetail = ScanDetail

    @property
    def RoomId(self):
        """gme实时语音房间ID，透传任务传入时的RoomId
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def OpenId(self):
        """gme实时语音用户ID，透传任务传入时的OpenId
        :rtype: str
        """
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def Info(self):
        """备注
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Offset(self):
        """流检测时分片在流中的偏移时间，单位毫秒
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Duration(self):
        """流检测时分片时长
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def PieceStartTime(self):
        """分片开始检测时间
        :rtype: int
        """
        return self._PieceStartTime

    @PieceStartTime.setter
    def PieceStartTime(self, PieceStartTime):
        self._PieceStartTime = PieceStartTime


    def _deserialize(self, params):
        self._DumpUrl = params.get("DumpUrl")
        self._HitFlag = params.get("HitFlag")
        self._MainType = params.get("MainType")
        if params.get("ScanDetail") is not None:
            self._ScanDetail = []
            for item in params.get("ScanDetail"):
                obj = ScanDetail()
                obj._deserialize(item)
                self._ScanDetail.append(obj)
        self._RoomId = params.get("RoomId")
        self._OpenId = params.get("OpenId")
        self._Info = params.get("Info")
        self._Offset = params.get("Offset")
        self._Duration = params.get("Duration")
        self._PieceStartTime = params.get("PieceStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanVoiceRequest(AbstractModel):
    """ScanVoice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 应用ID，登录[控制台 - 服务管理](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID
        :type BizId: int
        :param _Scenes: 语音检测场景，参数值目前要求为 default。 预留场景设置： 谩骂、色情、广告、违禁等场景，<a href="#Label_Value">具体取值见上述 Label 说明。</a>
        :type Scenes: list of str
        :param _Live: 是否为直播流。值为 false 时表示普通语音文件检测；为 true 时表示语音流检测。
        :type Live: bool
        :param _Tasks: 语音检测任务列表，列表最多支持100个检测任务。结构体中包含：
<li>DataId：数据的唯一ID</li>
<li>Url：数据文件的url，为 urlencode 编码，流式则为拉流地址</li>
        :type Tasks: list of Task
        :param _Callback: 异步检测结果回调地址，具体见上述<a href="#Callback_Declare">回调相关说明</a>。（说明：该字段为空时，必须通过接口(查询语音检测结果)获取检测结果）。
        :type Callback: str
        :param _Lang: 语种，不传默认中文
        :type Lang: str
        """
        self._BizId = None
        self._Scenes = None
        self._Live = None
        self._Tasks = None
        self._Callback = None
        self._Lang = None

    @property
    def BizId(self):
        """应用ID，登录[控制台 - 服务管理](https://console.cloud.tencent.com/gamegme)创建应用得到的AppID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def Scenes(self):
        """语音检测场景，参数值目前要求为 default。 预留场景设置： 谩骂、色情、广告、违禁等场景，<a href="#Label_Value">具体取值见上述 Label 说明。</a>
        :rtype: list of str
        """
        return self._Scenes

    @Scenes.setter
    def Scenes(self, Scenes):
        self._Scenes = Scenes

    @property
    def Live(self):
        """是否为直播流。值为 false 时表示普通语音文件检测；为 true 时表示语音流检测。
        :rtype: bool
        """
        return self._Live

    @Live.setter
    def Live(self, Live):
        self._Live = Live

    @property
    def Tasks(self):
        """语音检测任务列表，列表最多支持100个检测任务。结构体中包含：
<li>DataId：数据的唯一ID</li>
<li>Url：数据文件的url，为 urlencode 编码，流式则为拉流地址</li>
        :rtype: list of Task
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def Callback(self):
        """异步检测结果回调地址，具体见上述<a href="#Callback_Declare">回调相关说明</a>。（说明：该字段为空时，必须通过接口(查询语音检测结果)获取检测结果）。
        :rtype: str
        """
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def Lang(self):
        """语种，不传默认中文
        :rtype: str
        """
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._Scenes = params.get("Scenes")
        self._Live = params.get("Live")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._Callback = params.get("Callback")
        self._Lang = params.get("Lang")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanVoiceResponse(AbstractModel):
    """ScanVoice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 语音检测返回。Data 字段是 JSON 数组，每一个元素包含：<li>DataId： 请求中对应的 DataId。</li>
<li>TaskID ：该检测任务的 ID，用于轮询语音检测结果。</li>
        :type Data: list of ScanVoiceResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """语音检测返回。Data 字段是 JSON 数组，每一个元素包含：<li>DataId： 请求中对应的 DataId。</li>
<li>TaskID ：该检测任务的 ID，用于轮询语音检测结果。</li>
        :rtype: list of ScanVoiceResult
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ScanVoiceResult()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ScanVoiceResult(AbstractModel):
    """语音检测返回结果

    """

    def __init__(self):
        r"""
        :param _DataId: 数据ID
        :type DataId: str
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._DataId = None
        self._TaskId = None

    @property
    def DataId(self):
        """数据ID
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def TaskId(self):
        """任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._DataId = params.get("DataId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SceneInfo(AbstractModel):
    """SceneInfo场景信息
    'RealTime','实时语音分析',
    'VoiceMessage','语音消息',
    'GMECloudApi':'GME云API接口'

    """

    def __init__(self):
        r"""
        :param _SceneId: 'RealTime','实时语音分析',
'VoiceMessage','语音消息',
'GMECloudApi':'GME云API接口'
        :type SceneId: str
        :param _Status: 开关状态，true开启/false关闭
        :type Status: bool
        :param _CallbackUrl: 用户回调地址
        :type CallbackUrl: str
        """
        self._SceneId = None
        self._Status = None
        self._CallbackUrl = None

    @property
    def SceneId(self):
        """'RealTime','实时语音分析',
'VoiceMessage','语音消息',
'GMECloudApi':'GME云API接口'
        :rtype: str
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def Status(self):
        """开关状态，true开启/false关闭
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CallbackUrl(self):
        """用户回调地址
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl


    def _deserialize(self, params):
        self._SceneId = params.get("SceneId")
        self._Status = params.get("Status")
        self._CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceStatus(AbstractModel):
    """服务开关状态

    """

    def __init__(self):
        r"""
        :param _RealTimeSpeech: 实时语音服务开关状态
        :type RealTimeSpeech: :class:`tencentcloud.gme.v20180711.models.StatusInfo`
        :param _VoiceMessage: 语音消息服务开关状态
        :type VoiceMessage: :class:`tencentcloud.gme.v20180711.models.StatusInfo`
        :param _Porn: 语音内容安全服务开关状态
        :type Porn: :class:`tencentcloud.gme.v20180711.models.StatusInfo`
        :param _Live: 语音录制服务开关状态
        :type Live: :class:`tencentcloud.gme.v20180711.models.StatusInfo`
        :param _RealTimeAsr: 语音转文本服务开关状态
        :type RealTimeAsr: :class:`tencentcloud.gme.v20180711.models.StatusInfo`
        :param _TextTranslate: 文本翻译服务开关状态
        :type TextTranslate: :class:`tencentcloud.gme.v20180711.models.StatusInfo`
        """
        self._RealTimeSpeech = None
        self._VoiceMessage = None
        self._Porn = None
        self._Live = None
        self._RealTimeAsr = None
        self._TextTranslate = None

    @property
    def RealTimeSpeech(self):
        """实时语音服务开关状态
        :rtype: :class:`tencentcloud.gme.v20180711.models.StatusInfo`
        """
        return self._RealTimeSpeech

    @RealTimeSpeech.setter
    def RealTimeSpeech(self, RealTimeSpeech):
        self._RealTimeSpeech = RealTimeSpeech

    @property
    def VoiceMessage(self):
        """语音消息服务开关状态
        :rtype: :class:`tencentcloud.gme.v20180711.models.StatusInfo`
        """
        return self._VoiceMessage

    @VoiceMessage.setter
    def VoiceMessage(self, VoiceMessage):
        self._VoiceMessage = VoiceMessage

    @property
    def Porn(self):
        """语音内容安全服务开关状态
        :rtype: :class:`tencentcloud.gme.v20180711.models.StatusInfo`
        """
        return self._Porn

    @Porn.setter
    def Porn(self, Porn):
        self._Porn = Porn

    @property
    def Live(self):
        """语音录制服务开关状态
        :rtype: :class:`tencentcloud.gme.v20180711.models.StatusInfo`
        """
        return self._Live

    @Live.setter
    def Live(self, Live):
        self._Live = Live

    @property
    def RealTimeAsr(self):
        """语音转文本服务开关状态
        :rtype: :class:`tencentcloud.gme.v20180711.models.StatusInfo`
        """
        return self._RealTimeAsr

    @RealTimeAsr.setter
    def RealTimeAsr(self, RealTimeAsr):
        self._RealTimeAsr = RealTimeAsr

    @property
    def TextTranslate(self):
        """文本翻译服务开关状态
        :rtype: :class:`tencentcloud.gme.v20180711.models.StatusInfo`
        """
        return self._TextTranslate

    @TextTranslate.setter
    def TextTranslate(self, TextTranslate):
        self._TextTranslate = TextTranslate


    def _deserialize(self, params):
        if params.get("RealTimeSpeech") is not None:
            self._RealTimeSpeech = StatusInfo()
            self._RealTimeSpeech._deserialize(params.get("RealTimeSpeech"))
        if params.get("VoiceMessage") is not None:
            self._VoiceMessage = StatusInfo()
            self._VoiceMessage._deserialize(params.get("VoiceMessage"))
        if params.get("Porn") is not None:
            self._Porn = StatusInfo()
            self._Porn._deserialize(params.get("Porn"))
        if params.get("Live") is not None:
            self._Live = StatusInfo()
            self._Live._deserialize(params.get("Live"))
        if params.get("RealTimeAsr") is not None:
            self._RealTimeAsr = StatusInfo()
            self._RealTimeAsr._deserialize(params.get("RealTimeAsr"))
        if params.get("TextTranslate") is not None:
            self._TextTranslate = StatusInfo()
            self._TextTranslate._deserialize(params.get("TextTranslate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartRecordRequest(AbstractModel):
    """StartRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 应用ID。
        :type BizId: int
        :param _RoomId: 房间ID。
        :type RoomId: str
        :param _RecordMode: 录制类型：1代表单流 2代表混流 3代表单流和混流。
        :type RecordMode: int
        :param _SubscribeRecordUserIds: 指定订阅流白名单或者黑名单（不传默认订阅房间内所有音频流）。
        :type SubscribeRecordUserIds: :class:`tencentcloud.gme.v20180711.models.SubscribeRecordUserIds`
        """
        self._BizId = None
        self._RoomId = None
        self._RecordMode = None
        self._SubscribeRecordUserIds = None

    @property
    def BizId(self):
        """应用ID。
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def RoomId(self):
        """房间ID。
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RecordMode(self):
        """录制类型：1代表单流 2代表混流 3代表单流和混流。
        :rtype: int
        """
        return self._RecordMode

    @RecordMode.setter
    def RecordMode(self, RecordMode):
        self._RecordMode = RecordMode

    @property
    def SubscribeRecordUserIds(self):
        """指定订阅流白名单或者黑名单（不传默认订阅房间内所有音频流）。
        :rtype: :class:`tencentcloud.gme.v20180711.models.SubscribeRecordUserIds`
        """
        return self._SubscribeRecordUserIds

    @SubscribeRecordUserIds.setter
    def SubscribeRecordUserIds(self, SubscribeRecordUserIds):
        self._SubscribeRecordUserIds = SubscribeRecordUserIds


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._RoomId = params.get("RoomId")
        self._RecordMode = params.get("RecordMode")
        if params.get("SubscribeRecordUserIds") is not None:
            self._SubscribeRecordUserIds = SubscribeRecordUserIds()
            self._SubscribeRecordUserIds._deserialize(params.get("SubscribeRecordUserIds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartRecordResponse(AbstractModel):
    """StartRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务taskid。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务taskid。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StatisticsItem(AbstractModel):
    """用量数据单元

    """

    def __init__(self):
        r"""
        :param _StatDate: 日期，格式为年-月-日，如2018-07-13
        :type StatDate: str
        :param _Data: 统计值
        :type Data: int
        """
        self._StatDate = None
        self._Data = None

    @property
    def StatDate(self):
        """日期，格式为年-月-日，如2018-07-13
        :rtype: str
        """
        return self._StatDate

    @StatDate.setter
    def StatDate(self, StatDate):
        self._StatDate = StatDate

    @property
    def Data(self):
        """统计值
        :rtype: int
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._StatDate = params.get("StatDate")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatusInfo(AbstractModel):
    """服务开关状态

    """

    def __init__(self):
        r"""
        :param _Status: 服务开关状态， 0-正常，1-关闭
        :type Status: int
        """
        self._Status = None

    @property
    def Status(self):
        """服务开关状态， 0-正常，1-关闭
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRecordRequest(AbstractModel):
    """StopRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: int
        :param _BizId: 应用ID。
        :type BizId: int
        """
        self._TaskId = None
        self._BizId = None

    @property
    def TaskId(self):
        """任务ID。
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def BizId(self):
        """应用ID。
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRecordResponse(AbstractModel):
    """StopRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StreamTextStatisticsItem(AbstractModel):
    """流式转文本用量数据

    """

    def __init__(self):
        r"""
        :param _Data: 统计值，单位：秒
        :type Data: float
        """
        self._Data = None

    @property
    def Data(self):
        """统计值，单位：秒
        :rtype: float
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeRecordUserIds(AbstractModel):
    """指定订阅流白名单或者黑名单。

    """

    def __init__(self):
        r"""
        :param _UnSubscribeUserIds: 订阅音频流黑名单，指定不订阅哪几个UserId的音频流，例如["1", "2", "3"], 代表不订阅UserId 1，2，3的音频流。默认不填订阅房间内所有音频流，订阅列表用户数不超过20。
注意：只能同时设置UnSubscribeAudioUserIds、SubscribeAudioUserIds 其中1个参数
        :type UnSubscribeUserIds: list of str
        :param _SubscribeUserIds: 订阅音频流白名单，指定订阅哪几个UserId的音频流，例如["1", "2", "3"], 代表订阅UserId 1，2，3的音频流。默认不填订阅房间内所有音频流，订阅列表用户数不超过20。
注意：只能同时设置UnSubscribeAudioUserIds、SubscribeAudioUserIds 其中1个参数。
        :type SubscribeUserIds: list of str
        """
        self._UnSubscribeUserIds = None
        self._SubscribeUserIds = None

    @property
    def UnSubscribeUserIds(self):
        """订阅音频流黑名单，指定不订阅哪几个UserId的音频流，例如["1", "2", "3"], 代表不订阅UserId 1，2，3的音频流。默认不填订阅房间内所有音频流，订阅列表用户数不超过20。
注意：只能同时设置UnSubscribeAudioUserIds、SubscribeAudioUserIds 其中1个参数
        :rtype: list of str
        """
        return self._UnSubscribeUserIds

    @UnSubscribeUserIds.setter
    def UnSubscribeUserIds(self, UnSubscribeUserIds):
        self._UnSubscribeUserIds = UnSubscribeUserIds

    @property
    def SubscribeUserIds(self):
        """订阅音频流白名单，指定订阅哪几个UserId的音频流，例如["1", "2", "3"], 代表订阅UserId 1，2，3的音频流。默认不填订阅房间内所有音频流，订阅列表用户数不超过20。
注意：只能同时设置UnSubscribeAudioUserIds、SubscribeAudioUserIds 其中1个参数。
        :rtype: list of str
        """
        return self._SubscribeUserIds

    @SubscribeUserIds.setter
    def SubscribeUserIds(self, SubscribeUserIds):
        self._SubscribeUserIds = SubscribeUserIds


    def _deserialize(self, params):
        self._UnSubscribeUserIds = params.get("UnSubscribeUserIds")
        self._SubscribeUserIds = params.get("SubscribeUserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签列表

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """语音检测任务列表

    """

    def __init__(self):
        r"""
        :param _DataId: 数据的唯一ID
        :type DataId: str
        :param _Url: 数据文件的url，为 urlencode 编码，流式则为拉流地址
        :type Url: str
        :param _RoomId: gme实时语音房间ID，通过gme实时语音进行语音分析时输入
        :type RoomId: str
        :param _OpenId: gme实时语音用户ID，通过gme实时语音进行语音分析时输入
        :type OpenId: str
        """
        self._DataId = None
        self._Url = None
        self._RoomId = None
        self._OpenId = None

    @property
    def DataId(self):
        """数据的唯一ID
        :rtype: str
        """
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def Url(self):
        """数据文件的url，为 urlencode 编码，流式则为拉流地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RoomId(self):
        """gme实时语音房间ID，通过gme实时语音进行语音分析时输入
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def OpenId(self):
        """gme实时语音用户ID，通过gme实时语音进行语音分析时输入
        :rtype: str
        """
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId


    def _deserialize(self, params):
        self._DataId = params.get("DataId")
        self._Url = params.get("Url")
        self._RoomId = params.get("RoomId")
        self._OpenId = params.get("OpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateScanRoomsRequest(AbstractModel):
    """UpdateScanRooms请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 应用ID
        :type BizId: int
        :param _RoomIdString: 需要送检的所有房间号。多个房间号之间用","分隔。示例："0001,0002,0003"
        :type RoomIdString: str
        :param _RoomIdRegex: 符合此正则表达式规则的房间号将被送检。示例：^6.*（表示所有以6开头的房间号将被送检）
        :type RoomIdRegex: list of str
        """
        self._BizId = None
        self._RoomIdString = None
        self._RoomIdRegex = None

    @property
    def BizId(self):
        """应用ID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def RoomIdString(self):
        """需要送检的所有房间号。多个房间号之间用","分隔。示例："0001,0002,0003"
        :rtype: str
        """
        return self._RoomIdString

    @RoomIdString.setter
    def RoomIdString(self, RoomIdString):
        self._RoomIdString = RoomIdString

    @property
    def RoomIdRegex(self):
        """符合此正则表达式规则的房间号将被送检。示例：^6.*（表示所有以6开头的房间号将被送检）
        :rtype: list of str
        """
        return self._RoomIdRegex

    @RoomIdRegex.setter
    def RoomIdRegex(self, RoomIdRegex):
        self._RoomIdRegex = RoomIdRegex


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._RoomIdString = params.get("RoomIdString")
        self._RoomIdRegex = params.get("RoomIdRegex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateScanRoomsResponse(AbstractModel):
    """UpdateScanRooms返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorCode: 返回结果码
        :type ErrorCode: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorCode = None
        self._RequestId = None

    @property
    def ErrorCode(self):
        """返回结果码
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._RequestId = params.get("RequestId")


class UpdateScanUsersRequest(AbstractModel):
    """UpdateScanUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizId: 应用ID
        :type BizId: int
        :param _UserIdString: 需要送检的所有用户号。多个用户号之间用","分隔。示例："0001,0002,0003"
        :type UserIdString: str
        :param _UserIdRegex: 符合此正则表达式规则的用户号将被送检。示例：["^6.*"] 表示所有以6开头的用户号将被送检
        :type UserIdRegex: list of str
        """
        self._BizId = None
        self._UserIdString = None
        self._UserIdRegex = None

    @property
    def BizId(self):
        """应用ID
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def UserIdString(self):
        """需要送检的所有用户号。多个用户号之间用","分隔。示例："0001,0002,0003"
        :rtype: str
        """
        return self._UserIdString

    @UserIdString.setter
    def UserIdString(self, UserIdString):
        self._UserIdString = UserIdString

    @property
    def UserIdRegex(self):
        """符合此正则表达式规则的用户号将被送检。示例：["^6.*"] 表示所有以6开头的用户号将被送检
        :rtype: list of str
        """
        return self._UserIdRegex

    @UserIdRegex.setter
    def UserIdRegex(self, UserIdRegex):
        self._UserIdRegex = UserIdRegex


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._UserIdString = params.get("UserIdString")
        self._UserIdRegex = params.get("UserIdRegex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateScanUsersResponse(AbstractModel):
    """UpdateScanUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorCode: 返回结果码
        :type ErrorCode: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorCode = None
        self._RequestId = None

    @property
    def ErrorCode(self):
        """返回结果码
        :rtype: int
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._RequestId = params.get("RequestId")


class UserMicStatus(AbstractModel):
    """用户麦克风状态

    """

    def __init__(self):
        r"""
        :param _EnableMic: 开麦状态。1表示关闭麦克风，2表示打开麦克风。
        :type EnableMic: int
        :param _Uid: 客户端用于标识用户的Openid。（Uid、StrUid必须填一个，优先处理StrUid。）
        :type Uid: int
        :param _StrUid: 客户端用于标识字符串型用户的Openid。（Uid、StrUid必须填一个，优先处理StrUid。）
        :type StrUid: str
        """
        self._EnableMic = None
        self._Uid = None
        self._StrUid = None

    @property
    def EnableMic(self):
        """开麦状态。1表示关闭麦克风，2表示打开麦克风。
        :rtype: int
        """
        return self._EnableMic

    @EnableMic.setter
    def EnableMic(self, EnableMic):
        self._EnableMic = EnableMic

    @property
    def Uid(self):
        """客户端用于标识用户的Openid。（Uid、StrUid必须填一个，优先处理StrUid。）
        :rtype: int
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def StrUid(self):
        """客户端用于标识字符串型用户的Openid。（Uid、StrUid必须填一个，优先处理StrUid。）
        :rtype: str
        """
        return self._StrUid

    @StrUid.setter
    def StrUid(self, StrUid):
        self._StrUid = StrUid


    def _deserialize(self, params):
        self._EnableMic = params.get("EnableMic")
        self._Uid = params.get("Uid")
        self._StrUid = params.get("StrUid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceFilterConf(AbstractModel):
    """语音过滤服务配置数据

    """

    def __init__(self):
        r"""
        :param _Status: 语音过滤服务开关，取值：open/close
        :type Status: str
        :param _SceneInfos: 场景配置信息，如开关状态，回调地址。
        :type SceneInfos: list of SceneInfo
        """
        self._Status = None
        self._SceneInfos = None

    @property
    def Status(self):
        """语音过滤服务开关，取值：open/close
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SceneInfos(self):
        """场景配置信息，如开关状态，回调地址。
        :rtype: list of SceneInfo
        """
        return self._SceneInfos

    @SceneInfos.setter
    def SceneInfos(self, SceneInfos):
        self._SceneInfos = SceneInfos


    def _deserialize(self, params):
        self._Status = params.get("Status")
        if params.get("SceneInfos") is not None:
            self._SceneInfos = []
            for item in params.get("SceneInfos"):
                obj = SceneInfo()
                obj._deserialize(item)
                self._SceneInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceFilterStatisticsItem(AbstractModel):
    """语音过滤用量统计数据

    """

    def __init__(self):
        r"""
        :param _Duration: 语音过滤总时长，单位为min
        :type Duration: int
        """
        self._Duration = None

    @property
    def Duration(self):
        """语音过滤总时长，单位为min
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceMessageConf(AbstractModel):
    """离线语音服务配置数据

    """

    def __init__(self):
        r"""
        :param _Status: 离线语音服务开关，取值：open/close
        :type Status: str
        :param _Language: 离线语音支持语种，取值： all-全部，cnen-中英文。默认为中英文
        :type Language: str
        """
        self._Status = None
        self._Language = None

    @property
    def Status(self):
        """离线语音服务开关，取值：open/close
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Language(self):
        """离线语音支持语种，取值： all-全部，cnen-中英文。默认为中英文
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Language = params.get("Language")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceMessageStatisticsItem(AbstractModel):
    """语音消息用量统计信息

    """

    def __init__(self):
        r"""
        :param _Dau: 离线语音DAU
        :type Dau: int
        """
        self._Dau = None

    @property
    def Dau(self):
        """离线语音DAU
        :rtype: int
        """
        return self._Dau

    @Dau.setter
    def Dau(self, Dau):
        self._Dau = Dau


    def _deserialize(self, params):
        self._Dau = params.get("Dau")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        