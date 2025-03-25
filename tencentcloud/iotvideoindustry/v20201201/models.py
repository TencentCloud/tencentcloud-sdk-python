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


class AbnormalEvents(AbstractModel):
    """异动事件走势列表

    """

    def __init__(self):
        r"""
        :param _Date: 对应查询日期
        :type Date: str
        :param _Info: 列表信息
        :type Info: list of AbnormalEventsInfo
        """
        self._Date = None
        self._Info = None

    @property
    def Date(self):
        """对应查询日期
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Info(self):
        """列表信息
        :rtype: list of AbnormalEventsInfo
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info


    def _deserialize(self, params):
        self._Date = params.get("Date")
        if params.get("Info") is not None:
            self._Info = []
            for item in params.get("Info"):
                obj = AbnormalEventsInfo()
                obj._deserialize(item)
                self._Info.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbnormalEventsInfo(AbstractModel):
    """异动事件走势元素

    """

    def __init__(self):
        r"""
        :param _Key: 类型值
        :type Key: int
        :param _Count: 类型总数
        :type Count: int
        """
        self._Key = None
        self._Count = None

    @property
    def Key(self):
        """类型值
        :rtype: int
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Count(self):
        """类型总数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllDeviceInfo(AbstractModel):
    """查询全部设备出参

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        :param _DeviceType: 设备类型；2：IPC
        :type DeviceType: int
        :param _Status: 设备状态；0：设备不在线；1：设备在线；2：设备隔离中；3：设备未注册
        :type Status: int
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _ExtraInformation: 设备扩展属性
        :type ExtraInformation: str
        :param _NickName: 设备名称
        :type NickName: str
        :param _GroupPath: 设备绑定分组路径
        :type GroupPath: str
        :param _DeviceCode: 设备编码
        :type DeviceCode: str
        :param _IsRecord: 是否存在录像,，0:不存在；1：存在
        :type IsRecord: int
        :param _Recordable: 该设备是否可录制
        :type Recordable: int
        :param _Protocol: 设备接入协议
        :type Protocol: str
        :param _GroupId: 组Id
        :type GroupId: str
        :param _GroupName: 组名
        :type GroupName: str
        """
        self._DeviceId = None
        self._DeviceType = None
        self._Status = None
        self._CreateTime = None
        self._ExtraInformation = None
        self._NickName = None
        self._GroupPath = None
        self._DeviceCode = None
        self._IsRecord = None
        self._Recordable = None
        self._Protocol = None
        self._GroupId = None
        self._GroupName = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceType(self):
        """设备类型；2：IPC
        :rtype: int
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Status(self):
        """设备状态；0：设备不在线；1：设备在线；2：设备隔离中；3：设备未注册
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExtraInformation(self):
        """设备扩展属性
        :rtype: str
        """
        return self._ExtraInformation

    @ExtraInformation.setter
    def ExtraInformation(self, ExtraInformation):
        self._ExtraInformation = ExtraInformation

    @property
    def NickName(self):
        """设备名称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def GroupPath(self):
        """设备绑定分组路径
        :rtype: str
        """
        return self._GroupPath

    @GroupPath.setter
    def GroupPath(self, GroupPath):
        self._GroupPath = GroupPath

    @property
    def DeviceCode(self):
        """设备编码
        :rtype: str
        """
        return self._DeviceCode

    @DeviceCode.setter
    def DeviceCode(self, DeviceCode):
        self._DeviceCode = DeviceCode

    @property
    def IsRecord(self):
        """是否存在录像,，0:不存在；1：存在
        :rtype: int
        """
        return self._IsRecord

    @IsRecord.setter
    def IsRecord(self, IsRecord):
        self._IsRecord = IsRecord

    @property
    def Recordable(self):
        """该设备是否可录制
        :rtype: int
        """
        return self._Recordable

    @Recordable.setter
    def Recordable(self, Recordable):
        self._Recordable = Recordable

    @property
    def Protocol(self):
        """设备接入协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def GroupId(self):
        """组Id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """组名
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceType = params.get("DeviceType")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._ExtraInformation = params.get("ExtraInformation")
        self._NickName = params.get("NickName")
        self._GroupPath = params.get("GroupPath")
        self._DeviceCode = params.get("DeviceCode")
        self._IsRecord = params.get("IsRecord")
        self._Recordable = params.get("Recordable")
        self._Protocol = params.get("Protocol")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindGroupDevicesRequest(AbstractModel):
    """BindGroupDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组ID
        :type GroupId: str
        :param _DeviceList: 设备唯一标识列表
        :type DeviceList: list of str
        """
        self._GroupId = None
        self._DeviceList = None

    @property
    def GroupId(self):
        """分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def DeviceList(self):
        """设备唯一标识列表
        :rtype: list of str
        """
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._DeviceList = params.get("DeviceList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindGroupDevicesResponse(AbstractModel):
    """BindGroupDevices返回参数结构体

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


class ChannelDetail(AbstractModel):
    """国标通道详细信息

    """

    def __init__(self):
        r"""
        :param _ChannelName: 通道名称
        :type ChannelName: str
        :param _ChannelId: 通道唯一标识
        :type ChannelId: str
        :param _ChannelType: 通道类型 0：未知；1：视频通道；2：音频通道；3：告警通道
        :type ChannelType: int
        :param _ChannelCode: 20位国标通道编码
        :type ChannelCode: str
        :param _ExtraInformation: 通道扩展信息
        :type ExtraInformation: str
        :param _Status: 通道在线状态
        :type Status: int
        :param _IsRecord: 通道是否存在录像标识 0：无录像；1：有录像
        :type IsRecord: int
        :param _DeviceId: 通道所属设备唯一标识
        :type DeviceId: str
        :param _BusinessGroupId: 通道所属虚拟组织的ID
        :type BusinessGroupId: str
        """
        self._ChannelName = None
        self._ChannelId = None
        self._ChannelType = None
        self._ChannelCode = None
        self._ExtraInformation = None
        self._Status = None
        self._IsRecord = None
        self._DeviceId = None
        self._BusinessGroupId = None

    @property
    def ChannelName(self):
        """通道名称
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def ChannelId(self):
        """通道唯一标识
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelType(self):
        """通道类型 0：未知；1：视频通道；2：音频通道；3：告警通道
        :rtype: int
        """
        return self._ChannelType

    @ChannelType.setter
    def ChannelType(self, ChannelType):
        self._ChannelType = ChannelType

    @property
    def ChannelCode(self):
        """20位国标通道编码
        :rtype: str
        """
        return self._ChannelCode

    @ChannelCode.setter
    def ChannelCode(self, ChannelCode):
        self._ChannelCode = ChannelCode

    @property
    def ExtraInformation(self):
        """通道扩展信息
        :rtype: str
        """
        return self._ExtraInformation

    @ExtraInformation.setter
    def ExtraInformation(self, ExtraInformation):
        self._ExtraInformation = ExtraInformation

    @property
    def Status(self):
        """通道在线状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsRecord(self):
        """通道是否存在录像标识 0：无录像；1：有录像
        :rtype: int
        """
        return self._IsRecord

    @IsRecord.setter
    def IsRecord(self, IsRecord):
        self._IsRecord = IsRecord

    @property
    def DeviceId(self):
        """通道所属设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def BusinessGroupId(self):
        """通道所属虚拟组织的ID
        :rtype: str
        """
        return self._BusinessGroupId

    @BusinessGroupId.setter
    def BusinessGroupId(self, BusinessGroupId):
        self._BusinessGroupId = BusinessGroupId


    def _deserialize(self, params):
        self._ChannelName = params.get("ChannelName")
        self._ChannelId = params.get("ChannelId")
        self._ChannelType = params.get("ChannelType")
        self._ChannelCode = params.get("ChannelCode")
        self._ExtraInformation = params.get("ExtraInformation")
        self._Status = params.get("Status")
        self._IsRecord = params.get("IsRecord")
        self._DeviceId = params.get("DeviceId")
        self._BusinessGroupId = params.get("BusinessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelItem(AbstractModel):
    """GB28181通道

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        :param _ChannelId: 通道唯一标识
        :type ChannelId: str
        """
        self._DeviceId = None
        self._ChannelId = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ChannelId(self):
        """通道唯一标识
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlChannelLocalRecordRequest(AbstractModel):
    """ControlChannelLocalRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        :param _ChannelId: 通道唯一标识
        :type ChannelId: str
        :param _StreamId: 流Id，流的唯一标识
        :type StreamId: str
        :param _Command: 控制参数，转义的json字符串

目前支持的command：
"Command": "{"Action":"PAUSE"}" 暂停
"Command": "{"Action":"PLAY"}" 暂停恢复
"Command": "{"Action":"PLAY","Offset":"15"}" 基于文件起始时间点的位置偏移，单位秒
        :type Command: str
        """
        self._DeviceId = None
        self._ChannelId = None
        self._StreamId = None
        self._Command = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ChannelId(self):
        """通道唯一标识
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def StreamId(self):
        """流Id，流的唯一标识
        :rtype: str
        """
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def Command(self):
        """控制参数，转义的json字符串

目前支持的command：
"Command": "{"Action":"PAUSE"}" 暂停
"Command": "{"Action":"PLAY"}" 暂停恢复
"Command": "{"Action":"PLAY","Offset":"15"}" 基于文件起始时间点的位置偏移，单位秒
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ChannelId = params.get("ChannelId")
        self._StreamId = params.get("StreamId")
        self._Command = params.get("Command")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlChannelLocalRecordResponse(AbstractModel):
    """ControlChannelLocalRecord返回参数结构体

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


class ControlChannelPTZRequest(AbstractModel):
    """ControlChannelPTZ请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        :param _ChannelId: 通道唯一标识
        :type ChannelId: str
        :param _Command: PTZ控制命令类型：
stop - 停止当前PTZ信令
left - 向左移动
right - 向右移动
up - 向上移动
down - 向下移动
leftUp - 左上移动
leftDown - 左下移动
rightUp - 右上移动
rightDown - 右下移动
zoomOut - 镜头缩小
zoomIn - 镜头放大
irisIn - 光圈缩小
irisOut - 光圈放大
focusIn - 焦距变近
focusOut - 焦距变远
        :type Command: str
        """
        self._DeviceId = None
        self._ChannelId = None
        self._Command = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ChannelId(self):
        """通道唯一标识
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Command(self):
        """PTZ控制命令类型：
stop - 停止当前PTZ信令
left - 向左移动
right - 向右移动
up - 向上移动
down - 向下移动
leftUp - 左上移动
leftDown - 左下移动
rightUp - 右上移动
rightDown - 右下移动
zoomOut - 镜头缩小
zoomIn - 镜头放大
irisIn - 光圈缩小
irisOut - 光圈放大
focusIn - 焦距变近
focusOut - 焦距变远
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ChannelId = params.get("ChannelId")
        self._Command = params.get("Command")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlChannelPTZResponse(AbstractModel):
    """ControlChannelPTZ返回参数结构体

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


class ControlDevicePTZRequest(AbstractModel):
    """ControlDevicePTZ请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        :param _Command: PTZ控制命令类型：
stop - 停止当前PTZ信令
left - 向左移动
right - 向右移动
up - 向上移动
down - 向下移动
leftUp - 左上移动
leftDown - 左下移动
rightUp - 右上移动
rightDown - 右下移动
zoomOut - 镜头缩小
zoomIn - 镜头放大
irisIn - 光圈缩小
irisOut - 光圈放大
focusIn - 焦距变近
focusOut - 焦距变远
        :type Command: str
        :param _ChannelId: 通道唯一标识
        :type ChannelId: str
        """
        self._DeviceId = None
        self._Command = None
        self._ChannelId = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Command(self):
        """PTZ控制命令类型：
stop - 停止当前PTZ信令
left - 向左移动
right - 向右移动
up - 向上移动
down - 向下移动
leftUp - 左上移动
leftDown - 左下移动
rightUp - 右上移动
rightDown - 右下移动
zoomOut - 镜头缩小
zoomIn - 镜头放大
irisIn - 光圈缩小
irisOut - 光圈放大
focusIn - 焦距变近
focusOut - 焦距变远
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def ChannelId(self):
        """通道唯一标识
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Command = params.get("Command")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDevicePTZResponse(AbstractModel):
    """ControlDevicePTZ返回参数结构体

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


class ControlHomePositionRequest(AbstractModel):
    """ControlHomePosition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelId: 通道ID
        :type ChannelId: str
        :param _DeviceId: 设备Id
        :type DeviceId: str
        :param _Enable: 看守位使能 0-停用看守位 1-启用看守位
        :type Enable: int
        :param _PresetId: 预置位编码 范围1-8，启用看守位时必填
        :type PresetId: int
        :param _ResetTime: 看守位自动归位时间， 启用看守位时必填
        :type ResetTime: int
        """
        self._ChannelId = None
        self._DeviceId = None
        self._Enable = None
        self._PresetId = None
        self._ResetTime = None

    @property
    def ChannelId(self):
        """通道ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def DeviceId(self):
        """设备Id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Enable(self):
        """看守位使能 0-停用看守位 1-启用看守位
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def PresetId(self):
        """预置位编码 范围1-8，启用看守位时必填
        :rtype: int
        """
        return self._PresetId

    @PresetId.setter
    def PresetId(self, PresetId):
        self._PresetId = PresetId

    @property
    def ResetTime(self):
        """看守位自动归位时间， 启用看守位时必填
        :rtype: int
        """
        return self._ResetTime

    @ResetTime.setter
    def ResetTime(self, ResetTime):
        self._ResetTime = ResetTime


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._DeviceId = params.get("DeviceId")
        self._Enable = params.get("Enable")
        self._PresetId = params.get("PresetId")
        self._ResetTime = params.get("ResetTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlHomePositionResponse(AbstractModel):
    """ControlHomePosition返回参数结构体

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


class ControlPresetRequest(AbstractModel):
    """ControlPreset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelId: 通道ID
        :type ChannelId: str
        :param _Command: 控制命令：
Set-设置当前位置为预置位
Del-删除指定的预置位
Call-调用指定的预置位
        :type Command: str
        :param _PresetId: 预置位编码 范围1-8
        :type PresetId: int
        :param _DeviceId: 设备Id
        :type DeviceId: str
        """
        self._ChannelId = None
        self._Command = None
        self._PresetId = None
        self._DeviceId = None

    @property
    def ChannelId(self):
        """通道ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Command(self):
        """控制命令：
Set-设置当前位置为预置位
Del-删除指定的预置位
Call-调用指定的预置位
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def PresetId(self):
        """预置位编码 范围1-8
        :rtype: int
        """
        return self._PresetId

    @PresetId.setter
    def PresetId(self, PresetId):
        self._PresetId = PresetId

    @property
    def DeviceId(self):
        """设备Id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._Command = params.get("Command")
        self._PresetId = params.get("PresetId")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlPresetResponse(AbstractModel):
    """ControlPreset返回参数结构体

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


class ControlRecordStreamRequest(AbstractModel):
    """ControlRecordStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备Id，设备的唯一标识
        :type DeviceId: str
        :param _StreamId: 流Id，流的唯一标识
        :type StreamId: str
        :param _Command: |控制参数，CmdJson结构转义的json字符串。| Action  | string  |是|控制动作，play(用于暂停后恢复播放)、pause（暂停）、teardown(停止)、jump(拖动播放)
| Offset  | uint  |否|拖动播放时的时间偏移量（相对于起始时间）,单位：秒
目前支持的command：
"Command": "{"Action":"PAUSE"}" 暂停
"Command": "{"Action":"PLAY"}" 暂停恢复
"Command": "{"Action":"PLAY","Offset":"15"}" 位置偏移，可以替代jump操作
        :type Command: str
        :param _ChannelId: 通道唯一标识
        :type ChannelId: str
        """
        self._DeviceId = None
        self._StreamId = None
        self._Command = None
        self._ChannelId = None

    @property
    def DeviceId(self):
        """设备Id，设备的唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def StreamId(self):
        """流Id，流的唯一标识
        :rtype: str
        """
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def Command(self):
        """|控制参数，CmdJson结构转义的json字符串。| Action  | string  |是|控制动作，play(用于暂停后恢复播放)、pause（暂停）、teardown(停止)、jump(拖动播放)
| Offset  | uint  |否|拖动播放时的时间偏移量（相对于起始时间）,单位：秒
目前支持的command：
"Command": "{"Action":"PAUSE"}" 暂停
"Command": "{"Action":"PLAY"}" 暂停恢复
"Command": "{"Action":"PLAY","Offset":"15"}" 位置偏移，可以替代jump操作
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def ChannelId(self):
        """通道唯一标识
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._StreamId = params.get("StreamId")
        self._Command = params.get("Command")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlRecordStreamResponse(AbstractModel):
    """ControlRecordStream返回参数结构体

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


class CreateDeviceGroupRequest(AbstractModel):
    """CreateDeviceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 分组名称
        :type GroupName: str
        :param _ParentId: 父分组ID
        :type ParentId: str
        :param _GroupDescribe: 分组描述
        :type GroupDescribe: str
        """
        self._GroupName = None
        self._ParentId = None
        self._GroupDescribe = None

    @property
    def GroupName(self):
        """分组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ParentId(self):
        """父分组ID
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def GroupDescribe(self):
        """分组描述
        :rtype: str
        """
        return self._GroupDescribe

    @GroupDescribe.setter
    def GroupDescribe(self, GroupDescribe):
        self._GroupDescribe = GroupDescribe


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._ParentId = params.get("ParentId")
        self._GroupDescribe = params.get("GroupDescribe")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceGroupResponse(AbstractModel):
    """CreateDeviceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 响应结果，“OK”为成功，其他为失败
        :type Status: str
        :param _GroupId: 分组ID
        :type GroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._GroupId = None
        self._RequestId = None

    @property
    def Status(self):
        """响应结果，“OK”为成功，其他为失败
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def GroupId(self):
        """分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

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
        self._Status = params.get("Status")
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateDeviceRequest(AbstractModel):
    """CreateDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NickName: 设备名称
        :type NickName: str
        :param _PassWord: 设备密码
        :type PassWord: str
        :param _DeviceType: 设备类型，1：国标VMS设备(公有云不支持此类型)，2：国标IPC设备，3：国标NVR设备，9：智能告警设备(公有云不支持此类型)
        :type DeviceType: int
        :param _GroupId: 设备需要绑定的分组ID，参数为空则默认绑定到根分组
        :type GroupId: str
        """
        self._NickName = None
        self._PassWord = None
        self._DeviceType = None
        self._GroupId = None

    @property
    def NickName(self):
        """设备名称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def PassWord(self):
        """设备密码
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def DeviceType(self):
        """设备类型，1：国标VMS设备(公有云不支持此类型)，2：国标IPC设备，3：国标NVR设备，9：智能告警设备(公有云不支持此类型)
        :rtype: int
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def GroupId(self):
        """设备需要绑定的分组ID，参数为空则默认绑定到根分组
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._NickName = params.get("NickName")
        self._PassWord = params.get("PassWord")
        self._DeviceType = params.get("DeviceType")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceResponse(AbstractModel):
    """CreateDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceCode: 设备编码
        :type DeviceCode: str
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        :param _VirtualGroupId: 设备虚拟组信息，仅在创建NVR时返回该值
        :type VirtualGroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceCode = None
        self._DeviceId = None
        self._VirtualGroupId = None
        self._RequestId = None

    @property
    def DeviceCode(self):
        """设备编码
        :rtype: str
        """
        return self._DeviceCode

    @DeviceCode.setter
    def DeviceCode(self, DeviceCode):
        self._DeviceCode = DeviceCode

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def VirtualGroupId(self):
        """设备虚拟组信息，仅在创建NVR时返回该值
        :rtype: str
        """
        return self._VirtualGroupId

    @VirtualGroupId.setter
    def VirtualGroupId(self, VirtualGroupId):
        self._VirtualGroupId = VirtualGroupId

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
        self._DeviceCode = params.get("DeviceCode")
        self._DeviceId = params.get("DeviceId")
        self._VirtualGroupId = params.get("VirtualGroupId")
        self._RequestId = params.get("RequestId")


class CreateLiveChannelRequest(AbstractModel):
    """CreateLiveChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LiveChannelName: 直播频道名称
        :type LiveChannelName: str
        :param _LiveChannelType: 直播频道类型 1：固定直播；2：移动直播
        :type LiveChannelType: int
        """
        self._LiveChannelName = None
        self._LiveChannelType = None

    @property
    def LiveChannelName(self):
        """直播频道名称
        :rtype: str
        """
        return self._LiveChannelName

    @LiveChannelName.setter
    def LiveChannelName(self, LiveChannelName):
        self._LiveChannelName = LiveChannelName

    @property
    def LiveChannelType(self):
        """直播频道类型 1：固定直播；2：移动直播
        :rtype: int
        """
        return self._LiveChannelType

    @LiveChannelType.setter
    def LiveChannelType(self, LiveChannelType):
        self._LiveChannelType = LiveChannelType


    def _deserialize(self, params):
        self._LiveChannelName = params.get("LiveChannelName")
        self._LiveChannelType = params.get("LiveChannelType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveChannelResponse(AbstractModel):
    """CreateLiveChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LiveChannelId: 直播频道ID
        :type LiveChannelId: str
        :param _PushStreamAddress: 直播频道推流地址
        :type PushStreamAddress: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LiveChannelId = None
        self._PushStreamAddress = None
        self._RequestId = None

    @property
    def LiveChannelId(self):
        """直播频道ID
        :rtype: str
        """
        return self._LiveChannelId

    @LiveChannelId.setter
    def LiveChannelId(self, LiveChannelId):
        self._LiveChannelId = LiveChannelId

    @property
    def PushStreamAddress(self):
        """直播频道推流地址
        :rtype: str
        """
        return self._PushStreamAddress

    @PushStreamAddress.setter
    def PushStreamAddress(self, PushStreamAddress):
        self._PushStreamAddress = PushStreamAddress

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
        self._LiveChannelId = params.get("LiveChannelId")
        self._PushStreamAddress = params.get("PushStreamAddress")
        self._RequestId = params.get("RequestId")


class CreateLiveRecordPlanRequest(AbstractModel):
    """CreateLiveRecordPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanName: 录制计划名
        :type PlanName: str
        :param _PlanType: 计划类型 1：固定直播 2：移动直播
        :type PlanType: int
        :param _TemplateId: 时间模板ID,固定直播时为必填
        :type TemplateId: str
        :param _RecordStorageTime: 录制文件存储时长，单位天，默认30天
        :type RecordStorageTime: int
        :param _LiveChannelIds: 绑定的直播频道ID列表
        :type LiveChannelIds: list of str
        """
        self._PlanName = None
        self._PlanType = None
        self._TemplateId = None
        self._RecordStorageTime = None
        self._LiveChannelIds = None

    @property
    def PlanName(self):
        """录制计划名
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def PlanType(self):
        """计划类型 1：固定直播 2：移动直播
        :rtype: int
        """
        return self._PlanType

    @PlanType.setter
    def PlanType(self, PlanType):
        self._PlanType = PlanType

    @property
    def TemplateId(self):
        """时间模板ID,固定直播时为必填
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RecordStorageTime(self):
        """录制文件存储时长，单位天，默认30天
        :rtype: int
        """
        return self._RecordStorageTime

    @RecordStorageTime.setter
    def RecordStorageTime(self, RecordStorageTime):
        self._RecordStorageTime = RecordStorageTime

    @property
    def LiveChannelIds(self):
        """绑定的直播频道ID列表
        :rtype: list of str
        """
        return self._LiveChannelIds

    @LiveChannelIds.setter
    def LiveChannelIds(self, LiveChannelIds):
        self._LiveChannelIds = LiveChannelIds


    def _deserialize(self, params):
        self._PlanName = params.get("PlanName")
        self._PlanType = params.get("PlanType")
        self._TemplateId = params.get("TemplateId")
        self._RecordStorageTime = params.get("RecordStorageTime")
        self._LiveChannelIds = params.get("LiveChannelIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveRecordPlanResponse(AbstractModel):
    """CreateLiveRecordPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 录制计划名称
        :type PlanId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PlanId = None
        self._RequestId = None

    @property
    def PlanId(self):
        """录制计划名称
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

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
        self._PlanId = params.get("PlanId")
        self._RequestId = params.get("RequestId")


class CreateMessageForwardRequest(AbstractModel):
    """CreateMessageForward请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionId: 区域ID
        :type RegionId: str
        :param _RegionName: 区域名称
        :type RegionName: str
        :param _Instance: 实例ID
        :type Instance: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _MessageType: json数组， 转发类型 1: 告警 2:GPS
        :type MessageType: str
        :param _TopicId: kafka topic id
        :type TopicId: str
        :param _TopicName: kafka topic 名称
        :type TopicName: str
        """
        self._RegionId = None
        self._RegionName = None
        self._Instance = None
        self._InstanceName = None
        self._MessageType = None
        self._TopicId = None
        self._TopicName = None

    @property
    def RegionId(self):
        """区域ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """区域名称
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def Instance(self):
        """实例ID
        :rtype: str
        """
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def MessageType(self):
        """json数组， 转发类型 1: 告警 2:GPS
        :rtype: str
        """
        return self._MessageType

    @MessageType.setter
    def MessageType(self, MessageType):
        self._MessageType = MessageType

    @property
    def TopicId(self):
        """kafka topic id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        """kafka topic 名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._Instance = params.get("Instance")
        self._InstanceName = params.get("InstanceName")
        self._MessageType = params.get("MessageType")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMessageForwardResponse(AbstractModel):
    """CreateMessageForward返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IntId: 配置ID
        :type IntId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IntId = None
        self._RequestId = None

    @property
    def IntId(self):
        """配置ID
        :rtype: int
        """
        return self._IntId

    @IntId.setter
    def IntId(self, IntId):
        self._IntId = IntId

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
        self._IntId = params.get("IntId")
        self._RequestId = params.get("RequestId")


class CreateRecordPlanRequest(AbstractModel):
    """CreateRecordPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 计划名称
        :type Name: str
        :param _TimeTemplateId: 时间模板ID
        :type TimeTemplateId: str
        :param _EventId: 触发录制的事件类别 1:全部
        :type EventId: int
        :param _Devices: 该录制计划绑定的设备列表
        :type Devices: list of DeviceItem
        :param _RecordStorageTime: 存储周期
        :type RecordStorageTime: int
        """
        self._Name = None
        self._TimeTemplateId = None
        self._EventId = None
        self._Devices = None
        self._RecordStorageTime = None

    @property
    def Name(self):
        """计划名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TimeTemplateId(self):
        """时间模板ID
        :rtype: str
        """
        return self._TimeTemplateId

    @TimeTemplateId.setter
    def TimeTemplateId(self, TimeTemplateId):
        self._TimeTemplateId = TimeTemplateId

    @property
    def EventId(self):
        """触发录制的事件类别 1:全部
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Devices(self):
        """该录制计划绑定的设备列表
        :rtype: list of DeviceItem
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def RecordStorageTime(self):
        """存储周期
        :rtype: int
        """
        return self._RecordStorageTime

    @RecordStorageTime.setter
    def RecordStorageTime(self, RecordStorageTime):
        self._RecordStorageTime = RecordStorageTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TimeTemplateId = params.get("TimeTemplateId")
        self._EventId = params.get("EventId")
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeviceItem()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._RecordStorageTime = params.get("RecordStorageTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordPlanResponse(AbstractModel):
    """CreateRecordPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 录制计划ID
        :type PlanId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PlanId = None
        self._RequestId = None

    @property
    def PlanId(self):
        """录制计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

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
        self._PlanId = params.get("PlanId")
        self._RequestId = params.get("RequestId")


class CreateRecordingPlanRequest(AbstractModel):
    """CreateRecordingPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 计划名称
        :type Name: str
        :param _TimeTemplateId: 时间模板ID
        :type TimeTemplateId: str
        :param _Channels: 该录制计划绑定的通道列表
        :type Channels: list of ChannelItem
        :param _RecordStorageTime: 存储周期(天)；默认存储30天
        :type RecordStorageTime: int
        """
        self._Name = None
        self._TimeTemplateId = None
        self._Channels = None
        self._RecordStorageTime = None

    @property
    def Name(self):
        """计划名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TimeTemplateId(self):
        """时间模板ID
        :rtype: str
        """
        return self._TimeTemplateId

    @TimeTemplateId.setter
    def TimeTemplateId(self, TimeTemplateId):
        self._TimeTemplateId = TimeTemplateId

    @property
    def Channels(self):
        """该录制计划绑定的通道列表
        :rtype: list of ChannelItem
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels

    @property
    def RecordStorageTime(self):
        """存储周期(天)；默认存储30天
        :rtype: int
        """
        return self._RecordStorageTime

    @RecordStorageTime.setter
    def RecordStorageTime(self, RecordStorageTime):
        self._RecordStorageTime = RecordStorageTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TimeTemplateId = params.get("TimeTemplateId")
        if params.get("Channels") is not None:
            self._Channels = []
            for item in params.get("Channels"):
                obj = ChannelItem()
                obj._deserialize(item)
                self._Channels.append(obj)
        self._RecordStorageTime = params.get("RecordStorageTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordingPlanResponse(AbstractModel):
    """CreateRecordingPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 录制计划ID
        :type PlanId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PlanId = None
        self._RequestId = None

    @property
    def PlanId(self):
        """录制计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

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
        self._PlanId = params.get("PlanId")
        self._RequestId = params.get("RequestId")


class CreateSceneRequest(AbstractModel):
    """CreateScene请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SceneName: 场景名称
        :type SceneName: str
        :param _SceneTrigger: 场景触发规则
        :type SceneTrigger: str
        :param _RecordDuration: 录制时长 (秒)
        :type RecordDuration: int
        :param _StoreDuration: 录像存储时长(天)
        :type StoreDuration: int
        :param _Devices: 设备列表(不推荐使用)
        :type Devices: list of DeviceItem
        :param _Channels: 通道列表
        :type Channels: list of ChannelItem
        """
        self._SceneName = None
        self._SceneTrigger = None
        self._RecordDuration = None
        self._StoreDuration = None
        self._Devices = None
        self._Channels = None

    @property
    def SceneName(self):
        """场景名称
        :rtype: str
        """
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName

    @property
    def SceneTrigger(self):
        """场景触发规则
        :rtype: str
        """
        return self._SceneTrigger

    @SceneTrigger.setter
    def SceneTrigger(self, SceneTrigger):
        self._SceneTrigger = SceneTrigger

    @property
    def RecordDuration(self):
        """录制时长 (秒)
        :rtype: int
        """
        return self._RecordDuration

    @RecordDuration.setter
    def RecordDuration(self, RecordDuration):
        self._RecordDuration = RecordDuration

    @property
    def StoreDuration(self):
        """录像存储时长(天)
        :rtype: int
        """
        return self._StoreDuration

    @StoreDuration.setter
    def StoreDuration(self, StoreDuration):
        self._StoreDuration = StoreDuration

    @property
    def Devices(self):
        """设备列表(不推荐使用)
        :rtype: list of DeviceItem
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def Channels(self):
        """通道列表
        :rtype: list of ChannelItem
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels


    def _deserialize(self, params):
        self._SceneName = params.get("SceneName")
        self._SceneTrigger = params.get("SceneTrigger")
        self._RecordDuration = params.get("RecordDuration")
        self._StoreDuration = params.get("StoreDuration")
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeviceItem()
                obj._deserialize(item)
                self._Devices.append(obj)
        if params.get("Channels") is not None:
            self._Channels = []
            for item in params.get("Channels"):
                obj = ChannelItem()
                obj._deserialize(item)
                self._Channels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSceneResponse(AbstractModel):
    """CreateScene返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IntId: 场景ID
        :type IntId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IntId = None
        self._RequestId = None

    @property
    def IntId(self):
        """场景ID
        :rtype: int
        """
        return self._IntId

    @IntId.setter
    def IntId(self, IntId):
        self._IntId = IntId

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
        self._IntId = params.get("IntId")
        self._RequestId = params.get("RequestId")


class CreateTimeTemplateRequest(AbstractModel):
    """CreateTimeTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 时间模板名称
        :type Name: str
        :param _IsAllWeek: 是否为每周全时录制（即7*24h录制），0：非全时录制，1；全时录制，默认0
        :type IsAllWeek: int
        :param _TimeTemplateSpecs: 当IsAllWeek为0时必选，用于描述模板的各个时间片段
        :type TimeTemplateSpecs: list of TimeTemplateSpec
        """
        self._Name = None
        self._IsAllWeek = None
        self._TimeTemplateSpecs = None

    @property
    def Name(self):
        """时间模板名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IsAllWeek(self):
        """是否为每周全时录制（即7*24h录制），0：非全时录制，1；全时录制，默认0
        :rtype: int
        """
        return self._IsAllWeek

    @IsAllWeek.setter
    def IsAllWeek(self, IsAllWeek):
        self._IsAllWeek = IsAllWeek

    @property
    def TimeTemplateSpecs(self):
        """当IsAllWeek为0时必选，用于描述模板的各个时间片段
        :rtype: list of TimeTemplateSpec
        """
        return self._TimeTemplateSpecs

    @TimeTemplateSpecs.setter
    def TimeTemplateSpecs(self, TimeTemplateSpecs):
        self._TimeTemplateSpecs = TimeTemplateSpecs


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._IsAllWeek = params.get("IsAllWeek")
        if params.get("TimeTemplateSpecs") is not None:
            self._TimeTemplateSpecs = []
            for item in params.get("TimeTemplateSpecs"):
                obj = TimeTemplateSpec()
                obj._deserialize(item)
                self._TimeTemplateSpecs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTimeTemplateResponse(AbstractModel):
    """CreateTimeTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 时间模板ID
        :type TemplateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        """时间模板ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

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
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class DeleteChannelRequest(AbstractModel):
    """DeleteChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _ChannelId: 通道ID
        :type ChannelId: str
        """
        self._DeviceId = None
        self._ChannelId = None

    @property
    def DeviceId(self):
        """设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ChannelId(self):
        """通道ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteChannelResponse(AbstractModel):
    """DeleteChannel返回参数结构体

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


class DeleteDeviceGroupRequest(AbstractModel):
    """DeleteDeviceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组ID
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        """分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceGroupResponse(AbstractModel):
    """DeleteDeviceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 响应结果
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """响应结果
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 操作结果 OK-成功； 其他-失败
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """操作结果 OK-成功； 其他-失败
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DeleteLiveChannelRequest(AbstractModel):
    """DeleteLiveChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LiveChannelId: 直播频道ID
        :type LiveChannelId: str
        """
        self._LiveChannelId = None

    @property
    def LiveChannelId(self):
        """直播频道ID
        :rtype: str
        """
        return self._LiveChannelId

    @LiveChannelId.setter
    def LiveChannelId(self, LiveChannelId):
        self._LiveChannelId = LiveChannelId


    def _deserialize(self, params):
        self._LiveChannelId = params.get("LiveChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveChannelResponse(AbstractModel):
    """DeleteLiveChannel返回参数结构体

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


class DeleteLiveRecordPlanRequest(AbstractModel):
    """DeleteLiveRecordPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 录制计划ID
        :type PlanId: str
        """
        self._PlanId = None

    @property
    def PlanId(self):
        """录制计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveRecordPlanResponse(AbstractModel):
    """DeleteLiveRecordPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 删除状态描述
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """删除状态描述
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DeleteLiveVideoListRequest(AbstractModel):
    """DeleteLiveVideoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IntIDs: 视频ID 列表, 大小限制(100)
        :type IntIDs: list of int non-negative
        """
        self._IntIDs = None

    @property
    def IntIDs(self):
        """视频ID 列表, 大小限制(100)
        :rtype: list of int non-negative
        """
        return self._IntIDs

    @IntIDs.setter
    def IntIDs(self, IntIDs):
        self._IntIDs = IntIDs


    def _deserialize(self, params):
        self._IntIDs = params.get("IntIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveVideoListResponse(AbstractModel):
    """DeleteLiveVideoList返回参数结构体

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


class DeleteMessageForwardRequest(AbstractModel):
    """DeleteMessageForward请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IntId: 配置ID
        :type IntId: int
        """
        self._IntId = None

    @property
    def IntId(self):
        """配置ID
        :rtype: int
        """
        return self._IntId

    @IntId.setter
    def IntId(self, IntId):
        self._IntId = IntId


    def _deserialize(self, params):
        self._IntId = params.get("IntId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMessageForwardResponse(AbstractModel):
    """DeleteMessageForward返回参数结构体

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


class DeleteRecordPlanRequest(AbstractModel):
    """DeleteRecordPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 录制计划ID
        :type PlanId: str
        """
        self._PlanId = None

    @property
    def PlanId(self):
        """录制计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordPlanResponse(AbstractModel):
    """DeleteRecordPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 操作结果，OK：成功，其他：失败
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """操作结果，OK：成功，其他：失败
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DeleteRecordingPlanRequest(AbstractModel):
    """DeleteRecordingPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 录制计划ID
        :type PlanId: str
        """
        self._PlanId = None

    @property
    def PlanId(self):
        """录制计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordingPlanResponse(AbstractModel):
    """DeleteRecordingPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 操作结果，OK：成功，其他：失败
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """操作结果，OK：成功，其他：失败
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DeleteSceneRequest(AbstractModel):
    """DeleteScene请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IntId: 场景ID
        :type IntId: int
        """
        self._IntId = None

    @property
    def IntId(self):
        """场景ID
        :rtype: int
        """
        return self._IntId

    @IntId.setter
    def IntId(self, IntId):
        self._IntId = IntId


    def _deserialize(self, params):
        self._IntId = params.get("IntId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSceneResponse(AbstractModel):
    """DeleteScene返回参数结构体

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


class DeleteTimeTemplateRequest(AbstractModel):
    """DeleteTimeTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 时间模板ID
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        """时间模板ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTimeTemplateResponse(AbstractModel):
    """DeleteTimeTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 操作结果，OK：成功，其他：失败
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """操作结果，OK：成功，其他：失败
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DeleteVideoListRequest(AbstractModel):
    """DeleteVideoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InitIDs: 视频ID列表长度限制100内
        :type InitIDs: list of int
        """
        self._InitIDs = None

    @property
    def InitIDs(self):
        """视频ID列表长度限制100内
        :rtype: list of int
        """
        return self._InitIDs

    @InitIDs.setter
    def InitIDs(self, InitIDs):
        self._InitIDs = InitIDs


    def _deserialize(self, params):
        self._InitIDs = params.get("InitIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVideoListResponse(AbstractModel):
    """DeleteVideoList返回参数结构体

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


class DeleteWarningRequest(AbstractModel):
    """DeleteWarning请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 告警ID
        :type Id: int
        :param _Index: 告警索引
        :type Index: str
        """
        self._Id = None
        self._Index = None

    @property
    def Id(self):
        """告警ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Index(self):
        """告警索引
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWarningResponse(AbstractModel):
    """DeleteWarning返回参数结构体

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


class DescribeAbnormalEventsRequest(AbstractModel):
    """DescribeAbnormalEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        """开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
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
        


class DescribeAbnormalEventsResponse(AbstractModel):
    """DescribeAbnormalEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 异动事件走势列表
        :type Data: list of AbnormalEvents
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """异动事件走势列表
        :rtype: list of AbnormalEvents
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
                obj = AbnormalEvents()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAllDeviceListRequest(AbstractModel):
    """DescribeAllDeviceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 限制，默认200
        :type Limit: int
        :param _NickName: 设备名称，需要模糊匹配设备名称时为必填
        :type NickName: str
        :param _DeviceIds: DeviceId列表，需要精确查找设备时为必填
        :type DeviceIds: list of str
        :param _DeviceTypes: 设备类型过滤，设备类型，1：国标VMS设备(公有云不支持此类型)，2：国标IPC设备，3：国标NVR设备，9：智能告警设备(公有云不支持此类型)
        :type DeviceTypes: list of int
        """
        self._Offset = None
        self._Limit = None
        self._NickName = None
        self._DeviceIds = None
        self._DeviceTypes = None

    @property
    def Offset(self):
        """偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制，默认200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def NickName(self):
        """设备名称，需要模糊匹配设备名称时为必填
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def DeviceIds(self):
        """DeviceId列表，需要精确查找设备时为必填
        :rtype: list of str
        """
        return self._DeviceIds

    @DeviceIds.setter
    def DeviceIds(self, DeviceIds):
        self._DeviceIds = DeviceIds

    @property
    def DeviceTypes(self):
        """设备类型过滤，设备类型，1：国标VMS设备(公有云不支持此类型)，2：国标IPC设备，3：国标NVR设备，9：智能告警设备(公有云不支持此类型)
        :rtype: list of int
        """
        return self._DeviceTypes

    @DeviceTypes.setter
    def DeviceTypes(self, DeviceTypes):
        self._DeviceTypes = DeviceTypes


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._NickName = params.get("NickName")
        self._DeviceIds = params.get("DeviceIds")
        self._DeviceTypes = params.get("DeviceTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllDeviceListResponse(AbstractModel):
    """DescribeAllDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 设备总数
        :type TotalCount: int
        :param _Devices: 设备详细信息列表
        :type Devices: list of AllDeviceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Devices = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """设备总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Devices(self):
        """设备详细信息列表
        :rtype: list of AllDeviceInfo
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = AllDeviceInfo()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBindSceneChannelsRequest(AbstractModel):
    """DescribeBindSceneChannels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 条数限制最大不能超过1000
        :type Limit: int
        :param _SceneId: 场景ID
        :type SceneId: int
        :param _Offset: 偏移值
        :type Offset: int
        """
        self._Limit = None
        self._SceneId = None
        self._Offset = None

    @property
    def Limit(self):
        """条数限制最大不能超过1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SceneId(self):
        """场景ID
        :rtype: int
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def Offset(self):
        """偏移值
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._SceneId = params.get("SceneId")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindSceneChannelsResponse(AbstractModel):
    """DescribeBindSceneChannels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 通道列表
        :type List: list of ChannelItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """通道列表
        :rtype: list of ChannelItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ChannelItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBindSceneDevicesRequest(AbstractModel):
    """DescribeBindSceneDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SceneId: 场景ID
        :type SceneId: int
        :param _Offset: 偏移值
        :type Offset: int
        :param _Limit: 条数限制最大不能超过1000
        :type Limit: int
        """
        self._SceneId = None
        self._Offset = None
        self._Limit = None

    @property
    def SceneId(self):
        """场景ID
        :rtype: int
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def Offset(self):
        """偏移值
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """条数限制最大不能超过1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SceneId = params.get("SceneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindSceneDevicesResponse(AbstractModel):
    """DescribeBindSceneDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 设备列表
        :type List: list of DeviceItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """设备列表
        :rtype: list of DeviceItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DeviceItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeChannelLiveStreamURLRequest(AbstractModel):
    """DescribeChannelLiveStreamURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识，必填参数
        :type DeviceId: str
        :param _ChannelId: 通道唯一标识（接口升级字段为必填），必填参数
        :type ChannelId: str
        """
        self._DeviceId = None
        self._ChannelId = None

    @property
    def DeviceId(self):
        """设备唯一标识，必填参数
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ChannelId(self):
        """通道唯一标识（接口升级字段为必填），必填参数
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChannelLiveStreamURLResponse(AbstractModel):
    """DescribeChannelLiveStreamURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备实时流地址列表
        :type Data: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceStreamsData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """设备实时流地址列表
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceStreamsData`
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
            self._Data = DescribeDeviceStreamsData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeChannelLocalRecordURLRequest(AbstractModel):
    """DescribeChannelLocalRecordURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        :param _ChannelId: 通道唯一标识
        :type ChannelId: str
        :param _RecordId: 录像文件Id，通过获取本地录像返回
        :type RecordId: str
        :param _ExpireTime: UNIX 时间戳，30天内，URL失效时间，如180s无人观看此流则URL提前失效
        :type ExpireTime: int
        :param _StartTime: 录像文件推送的开始时间，需要在RecordId参数起始时间内，可以通过此参数控制回放流起始点
        :type StartTime: int
        :param _EndTime: 录像文件推送的结束时间，需要在RecordId参数起始时间内，可以通过此参数控制回放流起始点
        :type EndTime: int
        """
        self._DeviceId = None
        self._ChannelId = None
        self._RecordId = None
        self._ExpireTime = None
        self._StartTime = None
        self._EndTime = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ChannelId(self):
        """通道唯一标识
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def RecordId(self):
        """录像文件Id，通过获取本地录像返回
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def ExpireTime(self):
        """UNIX 时间戳，30天内，URL失效时间，如180s无人观看此流则URL提前失效
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def StartTime(self):
        """录像文件推送的开始时间，需要在RecordId参数起始时间内，可以通过此参数控制回放流起始点
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """录像文件推送的结束时间，需要在RecordId参数起始时间内，可以通过此参数控制回放流起始点
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ChannelId = params.get("ChannelId")
        self._RecordId = params.get("RecordId")
        self._ExpireTime = params.get("ExpireTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChannelLocalRecordURLResponse(AbstractModel):
    """DescribeChannelLocalRecordURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果
        :type Data: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeRecordStreamData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """结果
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeRecordStreamData`
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
            self._Data = DescribeRecordStreamData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeChannelStreamURLRequest(AbstractModel):
    """DescribeChannelStreamURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识，必填参数
        :type DeviceId: str
        :param _ExpireTime: 流地址失效时间，固定值填写0，其他参数无效，必填参数
        :type ExpireTime: int
        :param _ChannelId: 通道唯一标识（接口升级字段为必填），必填参数
        :type ChannelId: str
        """
        self._DeviceId = None
        self._ExpireTime = None
        self._ChannelId = None

    @property
    def DeviceId(self):
        """设备唯一标识，必填参数
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ExpireTime(self):
        """流地址失效时间，固定值填写0，其他参数无效，必填参数
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ChannelId(self):
        """通道唯一标识（接口升级字段为必填），必填参数
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ExpireTime = params.get("ExpireTime")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChannelStreamURLResponse(AbstractModel):
    """DescribeChannelStreamURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备实时流地址列表
        :type Data: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceStreamsData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """设备实时流地址列表
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceStreamsData`
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
            self._Data = DescribeDeviceStreamsData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeChannelsByLiveRecordPlanRequest(AbstractModel):
    """DescribeChannelsByLiveRecordPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 录制计划ID
        :type PlanId: str
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Limit: 分页大小
        :type Limit: int
        """
        self._PlanId = None
        self._Offset = None
        self._Limit = None

    @property
    def PlanId(self):
        """录制计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def Offset(self):
        """分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChannelsByLiveRecordPlanResponse(AbstractModel):
    """DescribeChannelsByLiveRecordPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总个数
        :type TotalCount: int
        :param _LiveChannels: 通道详情数组
        :type LiveChannels: list of LiveChannelItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._LiveChannels = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LiveChannels(self):
        """通道详情数组
        :rtype: list of LiveChannelItem
        """
        return self._LiveChannels

    @LiveChannels.setter
    def LiveChannels(self, LiveChannels):
        self._LiveChannels = LiveChannels

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
        self._TotalCount = params.get("TotalCount")
        if params.get("LiveChannels") is not None:
            self._LiveChannels = []
            for item in params.get("LiveChannels"):
                obj = LiveChannelItem()
                obj._deserialize(item)
                self._LiveChannels.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeChannelsRequest(AbstractModel):
    """DescribeChannels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备Id
        :type DeviceId: str
        :param _Limit: 限制，默认0
        :type Limit: int
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _ChannelTypes: 通道类型  0: 未知类型 1: 视频通道 2:  音频通道 3: 告警通道
        :type ChannelTypes: list of int non-negative
        :param _PlanId: 录制计划ID， 当为"null"值时未绑定录制计划
        :type PlanId: str
        :param _SceneId: 告警联动场景ID， 当为 -1 值时未绑定场景
        :type SceneId: int
        """
        self._DeviceId = None
        self._Limit = None
        self._Offset = None
        self._ChannelTypes = None
        self._PlanId = None
        self._SceneId = None

    @property
    def DeviceId(self):
        """设备Id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Limit(self):
        """限制，默认0
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ChannelTypes(self):
        """通道类型  0: 未知类型 1: 视频通道 2:  音频通道 3: 告警通道
        :rtype: list of int non-negative
        """
        return self._ChannelTypes

    @ChannelTypes.setter
    def ChannelTypes(self, ChannelTypes):
        self._ChannelTypes = ChannelTypes

    @property
    def PlanId(self):
        """录制计划ID， 当为"null"值时未绑定录制计划
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def SceneId(self):
        """告警联动场景ID， 当为 -1 值时未绑定场景
        :rtype: int
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ChannelTypes = params.get("ChannelTypes")
        self._PlanId = params.get("PlanId")
        self._SceneId = params.get("SceneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChannelsResponse(AbstractModel):
    """DescribeChannels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 通道总数
        :type TotalCount: int
        :param _Channels: 通道详情列表
        :type Channels: list of ChannelDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Channels = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """通道总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Channels(self):
        """通道详情列表
        :rtype: list of ChannelDetail
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Channels") is not None:
            self._Channels = []
            for item in params.get("Channels"):
                obj = ChannelDetail()
                obj._deserialize(item)
                self._Channels.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCurrentDeviceDataRequest(AbstractModel):
    """DescribeCurrentDeviceData请求参数结构体

    """


class DescribeCurrentDeviceDataResponse(AbstractModel):
    """DescribeCurrentDeviceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Channels: 通道数
        :type Channels: int
        :param _Devices: 设备数
        :type Devices: int
        :param _OnlineChannels: 在线通道数
        :type OnlineChannels: int
        :param _OnlineDevices: 在线设备数
        :type OnlineDevices: int
        :param _RecordingChannels: 正在录制通道数
        :type RecordingChannels: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Channels = None
        self._Devices = None
        self._OnlineChannels = None
        self._OnlineDevices = None
        self._RecordingChannels = None
        self._RequestId = None

    @property
    def Channels(self):
        """通道数
        :rtype: int
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels

    @property
    def Devices(self):
        """设备数
        :rtype: int
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def OnlineChannels(self):
        """在线通道数
        :rtype: int
        """
        return self._OnlineChannels

    @OnlineChannels.setter
    def OnlineChannels(self, OnlineChannels):
        self._OnlineChannels = OnlineChannels

    @property
    def OnlineDevices(self):
        """在线设备数
        :rtype: int
        """
        return self._OnlineDevices

    @OnlineDevices.setter
    def OnlineDevices(self, OnlineDevices):
        self._OnlineDevices = OnlineDevices

    @property
    def RecordingChannels(self):
        """正在录制通道数
        :rtype: int
        """
        return self._RecordingChannels

    @RecordingChannels.setter
    def RecordingChannels(self, RecordingChannels):
        self._RecordingChannels = RecordingChannels

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
        self._Channels = params.get("Channels")
        self._Devices = params.get("Devices")
        self._OnlineChannels = params.get("OnlineChannels")
        self._OnlineDevices = params.get("OnlineDevices")
        self._RecordingChannels = params.get("RecordingChannels")
        self._RequestId = params.get("RequestId")


class DescribeDeviceEventRequest(AbstractModel):
    """DescribeDeviceEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间，秒级时间戳
        :type StartTime: int
        :param _EndTime: 结束时间，秒级时间戳
        :type EndTime: int
        :param _DeviceId: 设备Id
        :type DeviceId: str
        :param _EventTypes: 默认为全部 事件类型 1:注册 2:心跳 4:录制异常 5:播放异常 6:流中断
        :type EventTypes: list of int
        :param _Offset: 偏移值
        :type Offset: int
        :param _Limit: limit限制值
        :type Limit: int
        """
        self._StartTime = None
        self._EndTime = None
        self._DeviceId = None
        self._EventTypes = None
        self._Offset = None
        self._Limit = None

    @property
    def StartTime(self):
        """开始时间，秒级时间戳
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，秒级时间戳
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DeviceId(self):
        """设备Id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def EventTypes(self):
        """默认为全部 事件类型 1:注册 2:心跳 4:录制异常 5:播放异常 6:流中断
        :rtype: list of int
        """
        return self._EventTypes

    @EventTypes.setter
    def EventTypes(self, EventTypes):
        self._EventTypes = EventTypes

    @property
    def Offset(self):
        """偏移值
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """limit限制值
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DeviceId = params.get("DeviceId")
        self._EventTypes = params.get("EventTypes")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceEventResponse(AbstractModel):
    """DescribeDeviceEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Events: 事件列表
        :type Events: list of Events
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Events = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Events(self):
        """事件列表
        :rtype: list of Events
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = Events()
                obj._deserialize(item)
                self._Events.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceGroupRequest(AbstractModel):
    """DescribeDeviceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceIds: 设备唯一标识列表
        :type DeviceIds: list of str
        """
        self._DeviceIds = None

    @property
    def DeviceIds(self):
        """设备唯一标识列表
        :rtype: list of str
        """
        return self._DeviceIds

    @DeviceIds.setter
    def DeviceIds(self, DeviceIds):
        self._DeviceIds = DeviceIds


    def _deserialize(self, params):
        self._DeviceIds = params.get("DeviceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceGroupResponse(AbstractModel):
    """DescribeDeviceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DevGroups: 设备所在分组信息
        :type DevGroups: list of DevGroupInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DevGroups = None
        self._RequestId = None

    @property
    def DevGroups(self):
        """设备所在分组信息
        :rtype: list of DevGroupInfo
        """
        return self._DevGroups

    @DevGroups.setter
    def DevGroups(self, DevGroups):
        self._DevGroups = DevGroups

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
        if params.get("DevGroups") is not None:
            self._DevGroups = []
            for item in params.get("DevGroups"):
                obj = DevGroupInfo()
                obj._deserialize(item)
                self._DevGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceListRequest(AbstractModel):
    """DescribeDeviceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 限制，默认200
        :type Limit: int
        :param _NickName: 设备名前缀
        :type NickName: str
        :param _DeviceTypes: 设备类型，1：国标VMS设备(公有云不支持此类型)，2：国标IPC设备，3：国标NVR设备，9：智能告警设备(公有云不支持此类型)
        :type DeviceTypes: list of int
        """
        self._Offset = None
        self._Limit = None
        self._NickName = None
        self._DeviceTypes = None

    @property
    def Offset(self):
        """偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制，默认200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def NickName(self):
        """设备名前缀
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def DeviceTypes(self):
        """设备类型，1：国标VMS设备(公有云不支持此类型)，2：国标IPC设备，3：国标NVR设备，9：智能告警设备(公有云不支持此类型)
        :rtype: list of int
        """
        return self._DeviceTypes

    @DeviceTypes.setter
    def DeviceTypes(self, DeviceTypes):
        self._DeviceTypes = DeviceTypes


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._NickName = params.get("NickName")
        self._DeviceTypes = params.get("DeviceTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceListResponse(AbstractModel):
    """DescribeDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 设备总数
        :type TotalCount: int
        :param _Devices: 设备详细信息列表
        :type Devices: list of AllDeviceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Devices = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """设备总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Devices(self):
        """设备详细信息列表
        :rtype: list of AllDeviceInfo
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = AllDeviceInfo()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceMonitorDataRequest(AbstractModel):
    """DescribeDeviceMonitorData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间戳
        :type StartTime: int
        :param _EndTime: 结束时间戳
        :type EndTime: int
        :param _Type: 类型 支持 OnlineChannels/OnlineDevices/RecordingChannels
        :type Type: str
        :param _TimesSpec: 时间粒度 目前只支持 1h
        :type TimesSpec: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Type = None
        self._TimesSpec = None

    @property
    def StartTime(self):
        """开始时间戳
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间戳
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        """类型 支持 OnlineChannels/OnlineDevices/RecordingChannels
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TimesSpec(self):
        """时间粒度 目前只支持 1h
        :rtype: str
        """
        return self._TimesSpec

    @TimesSpec.setter
    def TimesSpec(self, TimesSpec):
        self._TimesSpec = TimesSpec


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._TimesSpec = params.get("TimesSpec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceMonitorDataResponse(AbstractModel):
    """DescribeDeviceMonitorData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询设备统计monitor信息列表
        :type Data: list of DeviceMonitorValue
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """查询设备统计monitor信息列表
        :rtype: list of DeviceMonitorValue
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
                obj = DeviceMonitorValue()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDevicePassWordRequest(AbstractModel):
    """DescribeDevicePassWord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicePassWordResponse(AbstractModel):
    """DescribeDevicePassWord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PassWord: 设备密码
        :type PassWord: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PassWord = None
        self._RequestId = None

    @property
    def PassWord(self):
        """设备密码
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

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
        self._PassWord = params.get("PassWord")
        self._RequestId = params.get("RequestId")


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
        :type DeviceId: str
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
        """设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Device: 设备详情信息
        :type Device: :class:`tencentcloud.iotvideoindustry.v20201201.models.AllDeviceInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Device = None
        self._RequestId = None

    @property
    def Device(self):
        """设备详情信息
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.AllDeviceInfo`
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

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
        if params.get("Device") is not None:
            self._Device = AllDeviceInfo()
            self._Device._deserialize(params.get("Device"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceStreamsData(AbstractModel):
    """DescribeDeviceStreams的出参复杂类型

    """

    def __init__(self):
        r"""
        :param _RtspAddr: rtsp地址
        :type RtspAddr: str
        :param _RtmpAddr: rtmp地址
        :type RtmpAddr: str
        :param _HlsAddr: hls地址
        :type HlsAddr: str
        :param _FlvAddr: flv地址
        :type FlvAddr: str
        """
        self._RtspAddr = None
        self._RtmpAddr = None
        self._HlsAddr = None
        self._FlvAddr = None

    @property
    def RtspAddr(self):
        """rtsp地址
        :rtype: str
        """
        return self._RtspAddr

    @RtspAddr.setter
    def RtspAddr(self, RtspAddr):
        self._RtspAddr = RtspAddr

    @property
    def RtmpAddr(self):
        """rtmp地址
        :rtype: str
        """
        return self._RtmpAddr

    @RtmpAddr.setter
    def RtmpAddr(self, RtmpAddr):
        self._RtmpAddr = RtmpAddr

    @property
    def HlsAddr(self):
        """hls地址
        :rtype: str
        """
        return self._HlsAddr

    @HlsAddr.setter
    def HlsAddr(self, HlsAddr):
        self._HlsAddr = HlsAddr

    @property
    def FlvAddr(self):
        """flv地址
        :rtype: str
        """
        return self._FlvAddr

    @FlvAddr.setter
    def FlvAddr(self, FlvAddr):
        self._FlvAddr = FlvAddr


    def _deserialize(self, params):
        self._RtspAddr = params.get("RtspAddr")
        self._RtmpAddr = params.get("RtmpAddr")
        self._HlsAddr = params.get("HlsAddr")
        self._FlvAddr = params.get("FlvAddr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceStreamsRequest(AbstractModel):
    """DescribeDeviceStreams请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        :param _ExpireTime: 流地址失效时间
        :type ExpireTime: int
        :param _ChannelId: 通道唯一标识（接口升级字段为必填）
        :type ChannelId: str
        """
        self._DeviceId = None
        self._ExpireTime = None
        self._ChannelId = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ExpireTime(self):
        """流地址失效时间
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ChannelId(self):
        """通道唯一标识（接口升级字段为必填）
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ExpireTime = params.get("ExpireTime")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceStreamsResponse(AbstractModel):
    """DescribeDeviceStreams返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备实时流地址列表
        :type Data: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceStreamsData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """设备实时流地址列表
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceStreamsData`
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
            self._Data = DescribeDeviceStreamsData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeGroupByIdRequest(AbstractModel):
    """DescribeGroupById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组ID
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        """分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupByIdResponse(AbstractModel):
    """DescribeGroupById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Group: 分组信息详情
        :type Group: :class:`tencentcloud.iotvideoindustry.v20201201.models.GroupItem`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Group = None
        self._RequestId = None

    @property
    def Group(self):
        """分组信息详情
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.GroupItem`
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

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
        if params.get("Group") is not None:
            self._Group = GroupItem()
            self._Group._deserialize(params.get("Group"))
        self._RequestId = params.get("RequestId")


class DescribeGroupByPathRequest(AbstractModel):
    """DescribeGroupByPath请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupPath: 分组路径，格式为/aaa(/bbb/ccc)
        :type GroupPath: str
        """
        self._GroupPath = None

    @property
    def GroupPath(self):
        """分组路径，格式为/aaa(/bbb/ccc)
        :rtype: str
        """
        return self._GroupPath

    @GroupPath.setter
    def GroupPath(self, GroupPath):
        self._GroupPath = GroupPath


    def _deserialize(self, params):
        self._GroupPath = params.get("GroupPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupByPathResponse(AbstractModel):
    """DescribeGroupByPath返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Group: 分组信息详情
        :type Group: :class:`tencentcloud.iotvideoindustry.v20201201.models.GroupItem`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Group = None
        self._RequestId = None

    @property
    def Group(self):
        """分组信息详情
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.GroupItem`
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

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
        if params.get("Group") is not None:
            self._Group = GroupItem()
            self._Group._deserialize(params.get("Group"))
        self._RequestId = params.get("RequestId")


class DescribeGroupDevicesRequest(AbstractModel):
    """DescribeGroupDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组ID
        :type GroupId: str
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 限制值，默认200
        :type Limit: int
        :param _NickName: 设备名称，根据设备名称模糊匹配时必填
        :type NickName: str
        :param _Recordable: 过滤不可录制设备
        :type Recordable: int
        :param _DeviceTypes: 当Group是普通组的时候，支持根据DeviceTypes筛选类型，
 设备类型，1：国标VMS设备(公有云不支持此类型)，2：国标IPC设备，3：国标NVR设备，9：智能告警设备(公有云不支持此类型)
        :type DeviceTypes: list of int
        """
        self._GroupId = None
        self._Offset = None
        self._Limit = None
        self._NickName = None
        self._Recordable = None
        self._DeviceTypes = None

    @property
    def GroupId(self):
        """分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Offset(self):
        """偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制值，默认200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def NickName(self):
        """设备名称，根据设备名称模糊匹配时必填
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Recordable(self):
        """过滤不可录制设备
        :rtype: int
        """
        return self._Recordable

    @Recordable.setter
    def Recordable(self, Recordable):
        self._Recordable = Recordable

    @property
    def DeviceTypes(self):
        """当Group是普通组的时候，支持根据DeviceTypes筛选类型，
 设备类型，1：国标VMS设备(公有云不支持此类型)，2：国标IPC设备，3：国标NVR设备，9：智能告警设备(公有云不支持此类型)
        :rtype: list of int
        """
        return self._DeviceTypes

    @DeviceTypes.setter
    def DeviceTypes(self, DeviceTypes):
        self._DeviceTypes = DeviceTypes


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._NickName = params.get("NickName")
        self._Recordable = params.get("Recordable")
        self._DeviceTypes = params.get("DeviceTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupDevicesResponse(AbstractModel):
    """DescribeGroupDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 分组绑定的设备数
        :type TotalCount: int
        :param _DeviceList: 设备详情列表
        :type DeviceList: list of GroupDeviceItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DeviceList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """分组绑定的设备数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeviceList(self):
        """设备详情列表
        :rtype: list of GroupDeviceItem
        """
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList

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
        self._TotalCount = params.get("TotalCount")
        if params.get("DeviceList") is not None:
            self._DeviceList = []
            for item in params.get("DeviceList"):
                obj = GroupDeviceItem()
                obj._deserialize(item)
                self._DeviceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGroupsRequest(AbstractModel):
    """DescribeGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupIds: 分组ID列表
        :type GroupIds: list of str
        """
        self._GroupIds = None

    @property
    def GroupIds(self):
        """分组ID列表
        :rtype: list of str
        """
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupsResponse(AbstractModel):
    """DescribeGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: 分组详细信息列表
        :type Groups: list of GroupInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Groups = None
        self._RequestId = None

    @property
    def Groups(self):
        """分组详细信息列表
        :rtype: list of GroupInfo
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

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
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIPCChannelsRequest(AbstractModel):
    """DescribeIPCChannels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 限制，默认0
        :type Limit: int
        :param _DeviceId: 设备Id
        :type DeviceId: str
        :param _ChannelTypes: 通道类型  0: 未知类型 1: 视频通道 2:  音频通道 3: 告警通道
        :type ChannelTypes: list of int non-negative
        """
        self._Offset = None
        self._Limit = None
        self._DeviceId = None
        self._ChannelTypes = None

    @property
    def Offset(self):
        """偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制，默认0
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DeviceId(self):
        """设备Id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ChannelTypes(self):
        """通道类型  0: 未知类型 1: 视频通道 2:  音频通道 3: 告警通道
        :rtype: list of int non-negative
        """
        return self._ChannelTypes

    @ChannelTypes.setter
    def ChannelTypes(self, ChannelTypes):
        self._ChannelTypes = ChannelTypes


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DeviceId = params.get("DeviceId")
        self._ChannelTypes = params.get("ChannelTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPCChannelsResponse(AbstractModel):
    """DescribeIPCChannels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 通道总数
        :type TotalCount: int
        :param _DeviceList: 通道详情列表
        :type DeviceList: list of GroupDeviceItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DeviceList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """通道总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeviceList(self):
        """通道详情列表
        :rtype: list of GroupDeviceItem
        """
        return self._DeviceList

    @DeviceList.setter
    def DeviceList(self, DeviceList):
        self._DeviceList = DeviceList

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
        self._TotalCount = params.get("TotalCount")
        if params.get("DeviceList") is not None:
            self._DeviceList = []
            for item in params.get("DeviceList"):
                obj = GroupDeviceItem()
                obj._deserialize(item)
                self._DeviceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveChannelListRequest(AbstractModel):
    """DescribeLiveChannelList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 最大数
        :type Limit: int
        :param _LiveChannelType: 直播频道类型，1：固定直播；2：移动直播
        :type LiveChannelType: int
        :param _RecordPlanId: 直播录制计划ID, null: 直播录制计划为空
        :type RecordPlanId: str
        :param _LiveChannelName: 频道名称 (支持模糊搜索)
        :type LiveChannelName: str
        """
        self._Offset = None
        self._Limit = None
        self._LiveChannelType = None
        self._RecordPlanId = None
        self._LiveChannelName = None

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """最大数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def LiveChannelType(self):
        """直播频道类型，1：固定直播；2：移动直播
        :rtype: int
        """
        return self._LiveChannelType

    @LiveChannelType.setter
    def LiveChannelType(self, LiveChannelType):
        self._LiveChannelType = LiveChannelType

    @property
    def RecordPlanId(self):
        """直播录制计划ID, null: 直播录制计划为空
        :rtype: str
        """
        return self._RecordPlanId

    @RecordPlanId.setter
    def RecordPlanId(self, RecordPlanId):
        self._RecordPlanId = RecordPlanId

    @property
    def LiveChannelName(self):
        """频道名称 (支持模糊搜索)
        :rtype: str
        """
        return self._LiveChannelName

    @LiveChannelName.setter
    def LiveChannelName(self, LiveChannelName):
        self._LiveChannelName = LiveChannelName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._LiveChannelType = params.get("LiveChannelType")
        self._RecordPlanId = params.get("RecordPlanId")
        self._LiveChannelName = params.get("LiveChannelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveChannelListResponse(AbstractModel):
    """DescribeLiveChannelList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 频道总数
        :type Total: int
        :param _LiveChannels: 频道信息数组
        :type LiveChannels: list of LiveChannelInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._LiveChannels = None
        self._RequestId = None

    @property
    def Total(self):
        """频道总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def LiveChannels(self):
        """频道信息数组
        :rtype: list of LiveChannelInfo
        """
        return self._LiveChannels

    @LiveChannels.setter
    def LiveChannels(self, LiveChannels):
        self._LiveChannels = LiveChannels

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
        self._Total = params.get("Total")
        if params.get("LiveChannels") is not None:
            self._LiveChannels = []
            for item in params.get("LiveChannels"):
                obj = LiveChannelInfo()
                obj._deserialize(item)
                self._LiveChannels.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveChannelRequest(AbstractModel):
    """DescribeLiveChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LiveChannelId: 频道ID
        :type LiveChannelId: str
        """
        self._LiveChannelId = None

    @property
    def LiveChannelId(self):
        """频道ID
        :rtype: str
        """
        return self._LiveChannelId

    @LiveChannelId.setter
    def LiveChannelId(self, LiveChannelId):
        self._LiveChannelId = LiveChannelId


    def _deserialize(self, params):
        self._LiveChannelId = params.get("LiveChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveChannelResponse(AbstractModel):
    """DescribeLiveChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LiveChannelId: 频道ID
        :type LiveChannelId: str
        :param _LiveChannelName: 频道名称
        :type LiveChannelName: str
        :param _LiveChannelType: 直播频道类型 1：固定直播；2：移动直播
        :type LiveChannelType: int
        :param _LiveStatus: 通道直播状态：1: 未推流，2: 推流中
        :type LiveStatus: int
        :param _PushStreamAddress: 推流地址
        :type PushStreamAddress: str
        :param _CreateTime: 创建时间
        :type CreateTime: list of str
        :param _UpdateTime: 修改时间
        :type UpdateTime: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LiveChannelId = None
        self._LiveChannelName = None
        self._LiveChannelType = None
        self._LiveStatus = None
        self._PushStreamAddress = None
        self._CreateTime = None
        self._UpdateTime = None
        self._RequestId = None

    @property
    def LiveChannelId(self):
        """频道ID
        :rtype: str
        """
        return self._LiveChannelId

    @LiveChannelId.setter
    def LiveChannelId(self, LiveChannelId):
        self._LiveChannelId = LiveChannelId

    @property
    def LiveChannelName(self):
        """频道名称
        :rtype: str
        """
        return self._LiveChannelName

    @LiveChannelName.setter
    def LiveChannelName(self, LiveChannelName):
        self._LiveChannelName = LiveChannelName

    @property
    def LiveChannelType(self):
        """直播频道类型 1：固定直播；2：移动直播
        :rtype: int
        """
        return self._LiveChannelType

    @LiveChannelType.setter
    def LiveChannelType(self, LiveChannelType):
        self._LiveChannelType = LiveChannelType

    @property
    def LiveStatus(self):
        """通道直播状态：1: 未推流，2: 推流中
        :rtype: int
        """
        return self._LiveStatus

    @LiveStatus.setter
    def LiveStatus(self, LiveStatus):
        self._LiveStatus = LiveStatus

    @property
    def PushStreamAddress(self):
        """推流地址
        :rtype: str
        """
        return self._PushStreamAddress

    @PushStreamAddress.setter
    def PushStreamAddress(self, PushStreamAddress):
        self._PushStreamAddress = PushStreamAddress

    @property
    def CreateTime(self):
        """创建时间
        :rtype: list of str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """修改时间
        :rtype: list of str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

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
        self._LiveChannelId = params.get("LiveChannelId")
        self._LiveChannelName = params.get("LiveChannelName")
        self._LiveChannelType = params.get("LiveChannelType")
        self._LiveStatus = params.get("LiveStatus")
        self._PushStreamAddress = params.get("PushStreamAddress")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._RequestId = params.get("RequestId")


class DescribeLiveRecordPlanByIdRequest(AbstractModel):
    """DescribeLiveRecordPlanById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 录制计划ID
        :type PlanId: str
        """
        self._PlanId = None

    @property
    def PlanId(self):
        """录制计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveRecordPlanByIdResponse(AbstractModel):
    """DescribeLiveRecordPlanById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanName: 计划名称
        :type PlanName: str
        :param _TemplateId: 模板ID
        :type TemplateId: str
        :param _TemplateName: 模板名称
        :type TemplateName: str
        :param _RecordStorageTime: 存储时间
        :type RecordStorageTime: int
        :param _PlanType: 计划类型
        :type PlanType: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PlanName = None
        self._TemplateId = None
        self._TemplateName = None
        self._RecordStorageTime = None
        self._PlanType = None
        self._RequestId = None

    @property
    def PlanName(self):
        """计划名称
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        """模板ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        """模板名称
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def RecordStorageTime(self):
        """存储时间
        :rtype: int
        """
        return self._RecordStorageTime

    @RecordStorageTime.setter
    def RecordStorageTime(self, RecordStorageTime):
        self._RecordStorageTime = RecordStorageTime

    @property
    def PlanType(self):
        """计划类型
        :rtype: int
        """
        return self._PlanType

    @PlanType.setter
    def PlanType(self, PlanType):
        self._PlanType = PlanType

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
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        self._RecordStorageTime = params.get("RecordStorageTime")
        self._PlanType = params.get("PlanType")
        self._RequestId = params.get("RequestId")


class DescribeLiveRecordPlanIdsRequest(AbstractModel):
    """DescribeLiveRecordPlanIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 时间模板ID
        :type TemplateId: str
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Limit: 分页大小
        :type Limit: int
        """
        self._TemplateId = None
        self._Offset = None
        self._Limit = None

    @property
    def TemplateId(self):
        """时间模板ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Offset(self):
        """分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveRecordPlanIdsResponse(AbstractModel):
    """DescribeLiveRecordPlanIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总个数
        :type TotalCount: int
        :param _Plans: 计划数组
        :type Plans: list of LiveRecordPlanItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Plans = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Plans(self):
        """计划数组
        :rtype: list of LiveRecordPlanItem
        """
        return self._Plans

    @Plans.setter
    def Plans(self, Plans):
        self._Plans = Plans

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Plans") is not None:
            self._Plans = []
            for item in params.get("Plans"):
                obj = LiveRecordPlanItem()
                obj._deserialize(item)
                self._Plans.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLiveStreamRequest(AbstractModel):
    """DescribeLiveStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LiveChannelId: 频道ID
        :type LiveChannelId: str
        :param _ExpireTime: 过期时间 秒级unix时间戳
        :type ExpireTime: int
        """
        self._LiveChannelId = None
        self._ExpireTime = None

    @property
    def LiveChannelId(self):
        """频道ID
        :rtype: str
        """
        return self._LiveChannelId

    @LiveChannelId.setter
    def LiveChannelId(self, LiveChannelId):
        self._LiveChannelId = LiveChannelId

    @property
    def ExpireTime(self):
        """过期时间 秒级unix时间戳
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._LiveChannelId = params.get("LiveChannelId")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveStreamResponse(AbstractModel):
    """DescribeLiveStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 拉流地址，只有在推流情况下才有
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotvideoindustry.v20201201.models.StreamAddress`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """拉流地址，只有在推流情况下才有
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.StreamAddress`
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
            self._Data = StreamAddress()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeLiveVideoListRequest(AbstractModel):
    """DescribeLiveVideoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 分页的每页数量
        :type Limit: int
        :param _LiveChannelId: 直播频道ID
        :type LiveChannelId: str
        :param _StartRecordTime: 开始录制开始时间
        :type StartRecordTime: int
        :param _EndRecordTime: 开始录制结束时间
        :type EndRecordTime: int
        :param _StartExpireTime: 过期开始时间
        :type StartExpireTime: int
        :param _EndExpireTime: 过期结束时间
        :type EndExpireTime: int
        :param _StartFileSize: 文件大小范围 Byte
        :type StartFileSize: int
        :param _EndFileSize: 文件大小范围 Byte
        :type EndFileSize: int
        :param _IsRecording: 录制状态，5: 录制回写完
        :type IsRecording: int
        """
        self._Offset = None
        self._Limit = None
        self._LiveChannelId = None
        self._StartRecordTime = None
        self._EndRecordTime = None
        self._StartExpireTime = None
        self._EndExpireTime = None
        self._StartFileSize = None
        self._EndFileSize = None
        self._IsRecording = None

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页的每页数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def LiveChannelId(self):
        """直播频道ID
        :rtype: str
        """
        return self._LiveChannelId

    @LiveChannelId.setter
    def LiveChannelId(self, LiveChannelId):
        self._LiveChannelId = LiveChannelId

    @property
    def StartRecordTime(self):
        """开始录制开始时间
        :rtype: int
        """
        return self._StartRecordTime

    @StartRecordTime.setter
    def StartRecordTime(self, StartRecordTime):
        self._StartRecordTime = StartRecordTime

    @property
    def EndRecordTime(self):
        """开始录制结束时间
        :rtype: int
        """
        return self._EndRecordTime

    @EndRecordTime.setter
    def EndRecordTime(self, EndRecordTime):
        self._EndRecordTime = EndRecordTime

    @property
    def StartExpireTime(self):
        """过期开始时间
        :rtype: int
        """
        return self._StartExpireTime

    @StartExpireTime.setter
    def StartExpireTime(self, StartExpireTime):
        self._StartExpireTime = StartExpireTime

    @property
    def EndExpireTime(self):
        """过期结束时间
        :rtype: int
        """
        return self._EndExpireTime

    @EndExpireTime.setter
    def EndExpireTime(self, EndExpireTime):
        self._EndExpireTime = EndExpireTime

    @property
    def StartFileSize(self):
        """文件大小范围 Byte
        :rtype: int
        """
        return self._StartFileSize

    @StartFileSize.setter
    def StartFileSize(self, StartFileSize):
        self._StartFileSize = StartFileSize

    @property
    def EndFileSize(self):
        """文件大小范围 Byte
        :rtype: int
        """
        return self._EndFileSize

    @EndFileSize.setter
    def EndFileSize(self, EndFileSize):
        self._EndFileSize = EndFileSize

    @property
    def IsRecording(self):
        """录制状态，5: 录制回写完
        :rtype: int
        """
        return self._IsRecording

    @IsRecording.setter
    def IsRecording(self, IsRecording):
        self._IsRecording = IsRecording


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._LiveChannelId = params.get("LiveChannelId")
        self._StartRecordTime = params.get("StartRecordTime")
        self._EndRecordTime = params.get("EndRecordTime")
        self._StartExpireTime = params.get("StartExpireTime")
        self._EndExpireTime = params.get("EndExpireTime")
        self._StartFileSize = params.get("StartFileSize")
        self._EndFileSize = params.get("EndFileSize")
        self._IsRecording = params.get("IsRecording")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveVideoListResponse(AbstractModel):
    """DescribeLiveVideoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总的条数
        :type Total: int
        :param _RecordList: 录制任务详情数组
        :type RecordList: list of LiveRecordItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._RecordList = None
        self._RequestId = None

    @property
    def Total(self):
        """总的条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RecordList(self):
        """录制任务详情数组
        :rtype: list of LiveRecordItem
        """
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

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
        self._Total = params.get("Total")
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = LiveRecordItem()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMessageForwardRequest(AbstractModel):
    """DescribeMessageForward请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IntId: 配置ID
        :type IntId: int
        """
        self._IntId = None

    @property
    def IntId(self):
        """配置ID
        :rtype: int
        """
        return self._IntId

    @IntId.setter
    def IntId(self, IntId):
        self._IntId = IntId


    def _deserialize(self, params):
        self._IntId = params.get("IntId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMessageForwardResponse(AbstractModel):
    """DescribeMessageForward返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionId: 区域ID
        :type RegionId: str
        :param _RegionName: 区域名称
        :type RegionName: str
        :param _Instance: 实例ID
        :type Instance: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _IntId: 配置ID
        :type IntId: int
        :param _MessageType: json数组， 转发类型 1: 告警 2:GPS
        :type MessageType: str
        :param _TopicId: kafka topic id
        :type TopicId: str
        :param _CreateTime: 配置创建时间
        :type CreateTime: str
        :param _Uin: 用户Uin信息
        :type Uin: str
        :param _TopicName: kafka topic 名称
        :type TopicName: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionId = None
        self._RegionName = None
        self._Instance = None
        self._InstanceName = None
        self._IntId = None
        self._MessageType = None
        self._TopicId = None
        self._CreateTime = None
        self._Uin = None
        self._TopicName = None
        self._UpdateTime = None
        self._RequestId = None

    @property
    def RegionId(self):
        """区域ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """区域名称
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def Instance(self):
        """实例ID
        :rtype: str
        """
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def IntId(self):
        """配置ID
        :rtype: int
        """
        return self._IntId

    @IntId.setter
    def IntId(self, IntId):
        self._IntId = IntId

    @property
    def MessageType(self):
        """json数组， 转发类型 1: 告警 2:GPS
        :rtype: str
        """
        return self._MessageType

    @MessageType.setter
    def MessageType(self, MessageType):
        self._MessageType = MessageType

    @property
    def TopicId(self):
        """kafka topic id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def CreateTime(self):
        """配置创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Uin(self):
        """用户Uin信息
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def TopicName(self):
        """kafka topic 名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

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
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._Instance = params.get("Instance")
        self._InstanceName = params.get("InstanceName")
        self._IntId = params.get("IntId")
        self._MessageType = params.get("MessageType")
        self._TopicId = params.get("TopicId")
        self._CreateTime = params.get("CreateTime")
        self._Uin = params.get("Uin")
        self._TopicName = params.get("TopicName")
        self._UpdateTime = params.get("UpdateTime")
        self._RequestId = params.get("RequestId")


class DescribeMessageForwardsRequest(AbstractModel):
    """DescribeMessageForwards请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 数量限制
        :type Limit: int
        :param _Offset: 偏移
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        """数量限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMessageForwardsResponse(AbstractModel):
    """DescribeMessageForwards返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 配置总数
        :type Total: int
        :param _List: 配置列表
        :type List: list of MessageForward
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """配置总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """配置列表
        :rtype: list of MessageForward
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = MessageForward()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMonitorDataByDateRequest(AbstractModel):
    """DescribeMonitorDataByDate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间戳
        :type StartTime: int
        :param _EndTime: 结束时间戳 最多显示30天数据
        :type EndTime: int
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        """开始时间戳
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间戳 最多显示30天数据
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
        


class DescribeMonitorDataByDateResponse(AbstractModel):
    """DescribeMonitorDataByDate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 统计数据列表
        :type Data: list of RecordStatistic
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """统计数据列表
        :rtype: list of RecordStatistic
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
                obj = RecordStatistic()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePresetListRequest(AbstractModel):
    """DescribePresetList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelId: 视频通道唯一标识
        :type ChannelId: str
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        """
        self._ChannelId = None
        self._DeviceId = None

    @property
    def ChannelId(self):
        """视频通道唯一标识
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePresetListResponse(AbstractModel):
    """DescribePresetList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 预置列表
        :type Data: list of PresetItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """预置列表
        :rtype: list of PresetItem
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
                obj = PresetItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordDatesByChannelRequest(AbstractModel):
    """DescribeRecordDatesByChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        :param _ChannelId: 通道唯一标识
        :type ChannelId: str
        :param _Type: 1: 云端录制 2: 本地录制
        :type Type: int
        :param _Limit: 限制量，默认200
        :type Limit: int
        :param _Offset: 偏移量，默认0
        :type Offset: int
        """
        self._DeviceId = None
        self._ChannelId = None
        self._Type = None
        self._Limit = None
        self._Offset = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ChannelId(self):
        """通道唯一标识
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Type(self):
        """1: 云端录制 2: 本地录制
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Limit(self):
        """限制量，默认200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ChannelId = params.get("ChannelId")
        self._Type = params.get("Type")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordDatesByChannelResponse(AbstractModel):
    """DescribeRecordDatesByChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Dates: 含有录像文件的日期列表
        :type Dates: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Dates = None
        self._RequestId = None

    @property
    def Dates(self):
        """含有录像文件的日期列表
        :rtype: list of str
        """
        return self._Dates

    @Dates.setter
    def Dates(self, Dates):
        self._Dates = Dates

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
        self._Dates = params.get("Dates")
        self._RequestId = params.get("RequestId")


class DescribeRecordDatesByLiveRequest(AbstractModel):
    """DescribeRecordDatesByLive请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LiveChannelId: 直播频道ID
        :type LiveChannelId: str
        :param _Offset: 分页值，本地录制时参数无效
        :type Offset: int
        :param _Limit: 限制值，本地录制时参数无效
        :type Limit: int
        """
        self._LiveChannelId = None
        self._Offset = None
        self._Limit = None

    @property
    def LiveChannelId(self):
        """直播频道ID
        :rtype: str
        """
        return self._LiveChannelId

    @LiveChannelId.setter
    def LiveChannelId(self, LiveChannelId):
        self._LiveChannelId = LiveChannelId

    @property
    def Offset(self):
        """分页值，本地录制时参数无效
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制值，本地录制时参数无效
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._LiveChannelId = params.get("LiveChannelId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordDatesByLiveResponse(AbstractModel):
    """DescribeRecordDatesByLive返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Dates: 录制日期数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Dates: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Dates = None
        self._RequestId = None

    @property
    def Dates(self):
        """录制日期数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Dates

    @Dates.setter
    def Dates(self, Dates):
        self._Dates = Dates

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
        self._Dates = params.get("Dates")
        self._RequestId = params.get("RequestId")


class DescribeRecordStreamData(AbstractModel):
    """DescribeRecordStreamData 复杂类型

    """

    def __init__(self):
        r"""
        :param _RtspAddr: Rtsp地址
        :type RtspAddr: str
        :param _RtmpAddr: Rtmp地址
        :type RtmpAddr: str
        :param _HlsAddr: Hls地址
        :type HlsAddr: str
        :param _FlvAddr: Flv地址
        :type FlvAddr: str
        :param _StreamId: 流Id
        :type StreamId: str
        """
        self._RtspAddr = None
        self._RtmpAddr = None
        self._HlsAddr = None
        self._FlvAddr = None
        self._StreamId = None

    @property
    def RtspAddr(self):
        """Rtsp地址
        :rtype: str
        """
        return self._RtspAddr

    @RtspAddr.setter
    def RtspAddr(self, RtspAddr):
        self._RtspAddr = RtspAddr

    @property
    def RtmpAddr(self):
        """Rtmp地址
        :rtype: str
        """
        return self._RtmpAddr

    @RtmpAddr.setter
    def RtmpAddr(self, RtmpAddr):
        self._RtmpAddr = RtmpAddr

    @property
    def HlsAddr(self):
        """Hls地址
        :rtype: str
        """
        return self._HlsAddr

    @HlsAddr.setter
    def HlsAddr(self, HlsAddr):
        self._HlsAddr = HlsAddr

    @property
    def FlvAddr(self):
        """Flv地址
        :rtype: str
        """
        return self._FlvAddr

    @FlvAddr.setter
    def FlvAddr(self, FlvAddr):
        self._FlvAddr = FlvAddr

    @property
    def StreamId(self):
        """流Id
        :rtype: str
        """
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId


    def _deserialize(self, params):
        self._RtspAddr = params.get("RtspAddr")
        self._RtmpAddr = params.get("RtmpAddr")
        self._HlsAddr = params.get("HlsAddr")
        self._FlvAddr = params.get("FlvAddr")
        self._StreamId = params.get("StreamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordStreamRequest(AbstractModel):
    """DescribeRecordStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备Id
        :type DeviceId: str
        :param _ExpireTime: 流失效时间，UNIX时间戳，30天内
        :type ExpireTime: int
        :param _RecordId: 录像文件ID
        :type RecordId: str
        :param _StartTime: 录像流开始时间，当录像文件ID为空时有效，UNIX时间戳
        :type StartTime: int
        :param _EndTime: 录像流结束时间，当录像文件iD为空时有效，UNIX时间戳
        :type EndTime: int
        :param _ChannelId: 通道唯一标识（此接口升级为必填字段）
        :type ChannelId: str
        """
        self._DeviceId = None
        self._ExpireTime = None
        self._RecordId = None
        self._StartTime = None
        self._EndTime = None
        self._ChannelId = None

    @property
    def DeviceId(self):
        """设备Id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ExpireTime(self):
        """流失效时间，UNIX时间戳，30天内
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def RecordId(self):
        """录像文件ID
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def StartTime(self):
        """录像流开始时间，当录像文件ID为空时有效，UNIX时间戳
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """录像流结束时间，当录像文件iD为空时有效，UNIX时间戳
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ChannelId(self):
        """通道唯一标识（此接口升级为必填字段）
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ExpireTime = params.get("ExpireTime")
        self._RecordId = params.get("RecordId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordStreamResponse(AbstractModel):
    """DescribeRecordStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果
        :type Data: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeRecordStreamData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """结果
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeRecordStreamData`
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
            self._Data = DescribeRecordStreamData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRecordingPlanByIdRequest(AbstractModel):
    """DescribeRecordingPlanById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 录制计划ID
        :type PlanId: str
        """
        self._PlanId = None

    @property
    def PlanId(self):
        """录制计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordingPlanByIdResponse(AbstractModel):
    """DescribeRecordingPlanById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Plan: 录制计划详情
        :type Plan: :class:`tencentcloud.iotvideoindustry.v20201201.models.RecordPlanDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Plan = None
        self._RequestId = None

    @property
    def Plan(self):
        """录制计划详情
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.RecordPlanDetail`
        """
        return self._Plan

    @Plan.setter
    def Plan(self, Plan):
        self._Plan = Plan

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
        if params.get("Plan") is not None:
            self._Plan = RecordPlanDetail()
            self._Plan._deserialize(params.get("Plan"))
        self._RequestId = params.get("RequestId")


class DescribeRecordingPlansRequest(AbstractModel):
    """DescribeRecordingPlans请求参数结构体

    """


class DescribeRecordingPlansResponse(AbstractModel):
    """DescribeRecordingPlans返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Plans: 录制计划详情·列表
        :type Plans: list of RecordPlanDetail
        :param _TotalCount: 录制计划总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Plans = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Plans(self):
        """录制计划详情·列表
        :rtype: list of RecordPlanDetail
        """
        return self._Plans

    @Plans.setter
    def Plans(self, Plans):
        self._Plans = Plans

    @property
    def TotalCount(self):
        """录制计划总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Plans") is not None:
            self._Plans = []
            for item in params.get("Plans"):
                obj = RecordPlanDetail()
                obj._deserialize(item)
                self._Plans.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSIPServerRequest(AbstractModel):
    """DescribeSIPServer请求参数结构体

    """


class DescribeSIPServerResponse(AbstractModel):
    """DescribeSIPServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: SIP服务器相关配置项
        :type Data: :class:`tencentcloud.iotvideoindustry.v20201201.models.ServerConfiguration`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """SIP服务器相关配置项
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ServerConfiguration`
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
            self._Data = ServerConfiguration()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeSceneRequest(AbstractModel):
    """DescribeScene请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IntId: 场景ID
        :type IntId: int
        """
        self._IntId = None

    @property
    def IntId(self):
        """场景ID
        :rtype: int
        """
        return self._IntId

    @IntId.setter
    def IntId(self, IntId):
        self._IntId = IntId


    def _deserialize(self, params):
        self._IntId = params.get("IntId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSceneResponse(AbstractModel):
    """DescribeScene返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IntId: 场景ID
        :type IntId: int
        :param _RecordDuration: 录制时长(秒)
        :type RecordDuration: int
        :param _SceneName: 场景名称
        :type SceneName: str
        :param _SceneTrigger: 场景触发规则
        :type SceneTrigger: str
        :param _StoreDuration: 存储时长 (天)
        :type StoreDuration: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Uin: 用户Uin
        :type Uin: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IntId = None
        self._RecordDuration = None
        self._SceneName = None
        self._SceneTrigger = None
        self._StoreDuration = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Uin = None
        self._RequestId = None

    @property
    def IntId(self):
        """场景ID
        :rtype: int
        """
        return self._IntId

    @IntId.setter
    def IntId(self, IntId):
        self._IntId = IntId

    @property
    def RecordDuration(self):
        """录制时长(秒)
        :rtype: int
        """
        return self._RecordDuration

    @RecordDuration.setter
    def RecordDuration(self, RecordDuration):
        self._RecordDuration = RecordDuration

    @property
    def SceneName(self):
        """场景名称
        :rtype: str
        """
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName

    @property
    def SceneTrigger(self):
        """场景触发规则
        :rtype: str
        """
        return self._SceneTrigger

    @SceneTrigger.setter
    def SceneTrigger(self, SceneTrigger):
        self._SceneTrigger = SceneTrigger

    @property
    def StoreDuration(self):
        """存储时长 (天)
        :rtype: int
        """
        return self._StoreDuration

    @StoreDuration.setter
    def StoreDuration(self, StoreDuration):
        self._StoreDuration = StoreDuration

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Uin(self):
        """用户Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

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
        self._IntId = params.get("IntId")
        self._RecordDuration = params.get("RecordDuration")
        self._SceneName = params.get("SceneName")
        self._SceneTrigger = params.get("SceneTrigger")
        self._StoreDuration = params.get("StoreDuration")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Uin = params.get("Uin")
        self._RequestId = params.get("RequestId")


class DescribeScenesRequest(AbstractModel):
    """DescribeScenes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 条数限制
        :type Limit: int
        :param _Offset: 偏移
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        """条数限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScenesResponse(AbstractModel):
    """DescribeScenes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 场景总数
        :type Total: int
        :param _List: 场景列表
        :type List: list of SceneItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        """场景总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        """场景列表
        :rtype: list of SceneItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = SceneItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStatisticDetailsRequest(AbstractModel):
    """DescribeStatisticDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartDate: 开始日期，格式【YYYY-MM-DD】
        :type StartDate: str
        :param _EndDate: 结束日期，格式【YYYY-MM-DD】
        :type EndDate: str
        :param _StatisticField: 统计项。取值范围：
1.录制设备数：RecordingDevice
2.非录制设备数：NonRecordingDevice
3.观看流量总数：WatchFlux
4.已用存储容量总数：StorageUsage
5. X-P2P分享流量: P2PFluxTotal
6. X-P2P峰值带宽: P2PPeakValue
7. RTMP推流路数(直播推流): LivePushTotal
        :type StatisticField: str
        """
        self._StartDate = None
        self._EndDate = None
        self._StatisticField = None

    @property
    def StartDate(self):
        """开始日期，格式【YYYY-MM-DD】
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """结束日期，格式【YYYY-MM-DD】
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def StatisticField(self):
        """统计项。取值范围：
1.录制设备数：RecordingDevice
2.非录制设备数：NonRecordingDevice
3.观看流量总数：WatchFlux
4.已用存储容量总数：StorageUsage
5. X-P2P分享流量: P2PFluxTotal
6. X-P2P峰值带宽: P2PPeakValue
7. RTMP推流路数(直播推流): LivePushTotal
        :rtype: str
        """
        return self._StatisticField

    @StatisticField.setter
    def StatisticField(self, StatisticField):
        self._StatisticField = StatisticField


    def _deserialize(self, params):
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._StatisticField = params.get("StatisticField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStatisticDetailsResponse(AbstractModel):
    """DescribeStatisticDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 统计详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of StatisticItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """统计详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StatisticItem
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
                obj = StatisticItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStatisticSummaryRequest(AbstractModel):
    """DescribeStatisticSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Date: 指定日期。格式【YYYY-MM-DD】
        :type Date: str
        """
        self._Date = None

    @property
    def Date(self):
        """指定日期。格式【YYYY-MM-DD】
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStatisticSummaryResponse(AbstractModel):
    """DescribeStatisticSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordingDevice: 录制设备总数
        :type RecordingDevice: int
        :param _NonRecordingDevice: 非录制设备总数
        :type NonRecordingDevice: int
        :param _WatchFlux: 观看流量总数。为直播观看流量与点播观看流量之和。单位：GB
        :type WatchFlux: float
        :param _StorageUsage: 累计有效存储容量总数。单位：GB
        :type StorageUsage: float
        :param _P2PFluxTotal: X-P2P分享流量。单位 Byte
        :type P2PFluxTotal: float
        :param _P2PPeakValue: X-P2P峰值带宽。 单位bps
        :type P2PPeakValue: float
        :param _LivePushTotal: RTMP推流路数 ( 直播推流)
        :type LivePushTotal: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordingDevice = None
        self._NonRecordingDevice = None
        self._WatchFlux = None
        self._StorageUsage = None
        self._P2PFluxTotal = None
        self._P2PPeakValue = None
        self._LivePushTotal = None
        self._RequestId = None

    @property
    def RecordingDevice(self):
        """录制设备总数
        :rtype: int
        """
        return self._RecordingDevice

    @RecordingDevice.setter
    def RecordingDevice(self, RecordingDevice):
        self._RecordingDevice = RecordingDevice

    @property
    def NonRecordingDevice(self):
        """非录制设备总数
        :rtype: int
        """
        return self._NonRecordingDevice

    @NonRecordingDevice.setter
    def NonRecordingDevice(self, NonRecordingDevice):
        self._NonRecordingDevice = NonRecordingDevice

    @property
    def WatchFlux(self):
        """观看流量总数。为直播观看流量与点播观看流量之和。单位：GB
        :rtype: float
        """
        return self._WatchFlux

    @WatchFlux.setter
    def WatchFlux(self, WatchFlux):
        self._WatchFlux = WatchFlux

    @property
    def StorageUsage(self):
        """累计有效存储容量总数。单位：GB
        :rtype: float
        """
        return self._StorageUsage

    @StorageUsage.setter
    def StorageUsage(self, StorageUsage):
        self._StorageUsage = StorageUsage

    @property
    def P2PFluxTotal(self):
        """X-P2P分享流量。单位 Byte
        :rtype: float
        """
        return self._P2PFluxTotal

    @P2PFluxTotal.setter
    def P2PFluxTotal(self, P2PFluxTotal):
        self._P2PFluxTotal = P2PFluxTotal

    @property
    def P2PPeakValue(self):
        """X-P2P峰值带宽。 单位bps
        :rtype: float
        """
        return self._P2PPeakValue

    @P2PPeakValue.setter
    def P2PPeakValue(self, P2PPeakValue):
        self._P2PPeakValue = P2PPeakValue

    @property
    def LivePushTotal(self):
        """RTMP推流路数 ( 直播推流)
        :rtype: int
        """
        return self._LivePushTotal

    @LivePushTotal.setter
    def LivePushTotal(self, LivePushTotal):
        self._LivePushTotal = LivePushTotal

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
        self._RecordingDevice = params.get("RecordingDevice")
        self._NonRecordingDevice = params.get("NonRecordingDevice")
        self._WatchFlux = params.get("WatchFlux")
        self._StorageUsage = params.get("StorageUsage")
        self._P2PFluxTotal = params.get("P2PFluxTotal")
        self._P2PPeakValue = params.get("P2PPeakValue")
        self._LivePushTotal = params.get("LivePushTotal")
        self._RequestId = params.get("RequestId")


class DescribeSubGroupsRequest(AbstractModel):
    """DescribeSubGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组ID
        :type GroupId: str
        :param _GroupName: 分组名称，根据名称模糊匹配子分组时为必填
        :type GroupName: str
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 限制数，默认200
        :type Limit: int
        :param _OnlyGroup: 是否统计子分组下的设备数，0：统计，1：不统计
        :type OnlyGroup: int
        """
        self._GroupId = None
        self._GroupName = None
        self._Offset = None
        self._Limit = None
        self._OnlyGroup = None

    @property
    def GroupId(self):
        """分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """分组名称，根据名称模糊匹配子分组时为必填
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Offset(self):
        """偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制数，默认200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OnlyGroup(self):
        """是否统计子分组下的设备数，0：统计，1：不统计
        :rtype: int
        """
        return self._OnlyGroup

    @OnlyGroup.setter
    def OnlyGroup(self, OnlyGroup):
        self._OnlyGroup = OnlyGroup


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OnlyGroup = params.get("OnlyGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubGroupsResponse(AbstractModel):
    """DescribeSubGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupList: 子分组详情列表
        :type GroupList: list of GroupItem
        :param _TotalCount: 子分组总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def GroupList(self):
        """子分组详情列表
        :rtype: list of GroupItem
        """
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList

    @property
    def TotalCount(self):
        """子分组总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("GroupList") is not None:
            self._GroupList = []
            for item in params.get("GroupList"):
                obj = GroupItem()
                obj._deserialize(item)
                self._GroupList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSubscriptionStatusRequest(AbstractModel):
    """DescribeSubscriptionStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
        :type DeviceId: str
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
        """设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscriptionStatusResponse(AbstractModel):
    """DescribeSubscriptionStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmStatus: 设备GB28181报警订阅状态 1：未开启订阅；2：已开启订阅
        :type AlarmStatus: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlarmStatus = None
        self._RequestId = None

    @property
    def AlarmStatus(self):
        """设备GB28181报警订阅状态 1：未开启订阅；2：已开启订阅
        :rtype: int
        """
        return self._AlarmStatus

    @AlarmStatus.setter
    def AlarmStatus(self, AlarmStatus):
        self._AlarmStatus = AlarmStatus

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
        self._AlarmStatus = params.get("AlarmStatus")
        self._RequestId = params.get("RequestId")


class DescribeVideoListByChannelRequest(AbstractModel):
    """DescribeVideoListByChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        :param _ChannelId: 通道唯一标识
        :type ChannelId: str
        :param _Type: 1: 云端录制 2: 本地录制
        :type Type: int
        :param _Date: 指定某天。取值【YYYY-MM-DD】
为空时默认查询最近一天的记录
        :type Date: str
        :param _Limit: 限制量，默认2000
        :type Limit: int
        :param _Offset: 偏移量，默认0
        :type Offset: int
        """
        self._DeviceId = None
        self._ChannelId = None
        self._Type = None
        self._Date = None
        self._Limit = None
        self._Offset = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ChannelId(self):
        """通道唯一标识
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Type(self):
        """1: 云端录制 2: 本地录制
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Date(self):
        """指定某天。取值【YYYY-MM-DD】
为空时默认查询最近一天的记录
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Limit(self):
        """限制量，默认2000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ChannelId = params.get("ChannelId")
        self._Type = params.get("Type")
        self._Date = params.get("Date")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoListByChannelResponse(AbstractModel):
    """DescribeVideoListByChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoList: 录像详情列表
        :type VideoList: list of RecordTaskItem
        :param _TotalCount: 录像总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VideoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def VideoList(self):
        """录像详情列表
        :rtype: list of RecordTaskItem
        """
        return self._VideoList

    @VideoList.setter
    def VideoList(self, VideoList):
        self._VideoList = VideoList

    @property
    def TotalCount(self):
        """录像总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("VideoList") is not None:
            self._VideoList = []
            for item in params.get("VideoList"):
                obj = RecordTaskItem()
                obj._deserialize(item)
                self._VideoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeVideoListRequest(AbstractModel):
    """DescribeVideoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移
        :type Offset: int
        :param _Limit: 限制
        :type Limit: int
        :param _StartTime: 开始时间戳，秒级
        :type StartTime: int
        :param _EndTime: 结束时间戳，秒级
        :type EndTime: int
        :param _DeviceId: 设备Id
        :type DeviceId: str
        :param _StartRecordTime: 开始录制范围 开始
        :type StartRecordTime: int
        :param _EndRecordTime: 开始录制范围 结束
        :type EndRecordTime: int
        :param _StartExpireTime: 过期时间范围 开始
        :type StartExpireTime: int
        :param _EndExpireTime: 过期时间范围 结束
        :type EndExpireTime: int
        :param _StartFileSize: 文件大小范围 开始 单位byte
        :type StartFileSize: int
        :param _EndFileSize: 文件大小范围 结束 单位byte
        :type EndFileSize: int
        :param _IsRecording: 录制状态 99: 录制方已经回写状态 1: 开始录制了，等待回写 2: 已经到了时间模板的停止时间，在等待录制方回写
        :type IsRecording: int
        :param _ChannelId: 通道ID默认必传
        :type ChannelId: str
        :param _PlanId: 录制计划ID
        :type PlanId: str
        :param _SceneId: 场景ID
        :type SceneId: int
        :param _WarnId: 告警ID
        :type WarnId: int
        :param _RecordType: 录制类型 1: 联动计划录制 2: 告警录制
        :type RecordType: list of int
        """
        self._Offset = None
        self._Limit = None
        self._StartTime = None
        self._EndTime = None
        self._DeviceId = None
        self._StartRecordTime = None
        self._EndRecordTime = None
        self._StartExpireTime = None
        self._EndExpireTime = None
        self._StartFileSize = None
        self._EndFileSize = None
        self._IsRecording = None
        self._ChannelId = None
        self._PlanId = None
        self._SceneId = None
        self._WarnId = None
        self._RecordType = None

    @property
    def Offset(self):
        """偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def StartTime(self):
        """开始时间戳，秒级
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间戳，秒级
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DeviceId(self):
        """设备Id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def StartRecordTime(self):
        """开始录制范围 开始
        :rtype: int
        """
        return self._StartRecordTime

    @StartRecordTime.setter
    def StartRecordTime(self, StartRecordTime):
        self._StartRecordTime = StartRecordTime

    @property
    def EndRecordTime(self):
        """开始录制范围 结束
        :rtype: int
        """
        return self._EndRecordTime

    @EndRecordTime.setter
    def EndRecordTime(self, EndRecordTime):
        self._EndRecordTime = EndRecordTime

    @property
    def StartExpireTime(self):
        """过期时间范围 开始
        :rtype: int
        """
        return self._StartExpireTime

    @StartExpireTime.setter
    def StartExpireTime(self, StartExpireTime):
        self._StartExpireTime = StartExpireTime

    @property
    def EndExpireTime(self):
        """过期时间范围 结束
        :rtype: int
        """
        return self._EndExpireTime

    @EndExpireTime.setter
    def EndExpireTime(self, EndExpireTime):
        self._EndExpireTime = EndExpireTime

    @property
    def StartFileSize(self):
        """文件大小范围 开始 单位byte
        :rtype: int
        """
        return self._StartFileSize

    @StartFileSize.setter
    def StartFileSize(self, StartFileSize):
        self._StartFileSize = StartFileSize

    @property
    def EndFileSize(self):
        """文件大小范围 结束 单位byte
        :rtype: int
        """
        return self._EndFileSize

    @EndFileSize.setter
    def EndFileSize(self, EndFileSize):
        self._EndFileSize = EndFileSize

    @property
    def IsRecording(self):
        """录制状态 99: 录制方已经回写状态 1: 开始录制了，等待回写 2: 已经到了时间模板的停止时间，在等待录制方回写
        :rtype: int
        """
        return self._IsRecording

    @IsRecording.setter
    def IsRecording(self, IsRecording):
        self._IsRecording = IsRecording

    @property
    def ChannelId(self):
        """通道ID默认必传
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def PlanId(self):
        """录制计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def SceneId(self):
        """场景ID
        :rtype: int
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def WarnId(self):
        """告警ID
        :rtype: int
        """
        return self._WarnId

    @WarnId.setter
    def WarnId(self, WarnId):
        self._WarnId = WarnId

    @property
    def RecordType(self):
        """录制类型 1: 联动计划录制 2: 告警录制
        :rtype: list of int
        """
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._DeviceId = params.get("DeviceId")
        self._StartRecordTime = params.get("StartRecordTime")
        self._EndRecordTime = params.get("EndRecordTime")
        self._StartExpireTime = params.get("StartExpireTime")
        self._EndExpireTime = params.get("EndExpireTime")
        self._StartFileSize = params.get("StartFileSize")
        self._EndFileSize = params.get("EndFileSize")
        self._IsRecording = params.get("IsRecording")
        self._ChannelId = params.get("ChannelId")
        self._PlanId = params.get("PlanId")
        self._SceneId = params.get("SceneId")
        self._WarnId = params.get("WarnId")
        self._RecordType = params.get("RecordType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoListResponse(AbstractModel):
    """DescribeVideoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _VideoList: 已废弃
        :type VideoList: :class:`tencentcloud.iotvideoindustry.v20201201.models.RecordTaskItem`
        :param _RecordList: 录像详情列表
        :type RecordList: list of RecordTaskItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VideoList = None
        self._RecordList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VideoList(self):
        """已废弃
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.RecordTaskItem`
        """
        return self._VideoList

    @VideoList.setter
    def VideoList(self, VideoList):
        self._VideoList = VideoList

    @property
    def RecordList(self):
        """录像详情列表
        :rtype: list of RecordTaskItem
        """
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

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
        self._TotalCount = params.get("TotalCount")
        if params.get("VideoList") is not None:
            self._VideoList = RecordTaskItem()
            self._VideoList._deserialize(params.get("VideoList"))
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = RecordTaskItem()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWarnModRequest(AbstractModel):
    """DescribeWarnMod请求参数结构体

    """


class DescribeWarnModResponse(AbstractModel):
    """DescribeWarnMod返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 告警类型
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """告警类型
        :rtype: str
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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeWarningsRequest(AbstractModel):
    """DescribeWarnings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderType: 1:创建时间倒序 2：创建时间升序 3：level倒序 4：leve升序
        :type OrderType: int
        :param _DeviceId: 可选设备id
        :type DeviceId: str
        :param _WarnLevelArray: 如果不传则查询所有，取值参见配置
        :type WarnLevelArray: list of int
        :param _WarnModeArray: 如果不传则查询所有，取值参见配置
        :type WarnModeArray: list of int
        :param _Offset: 不传认为是0
        :type Offset: int
        :param _Limit: 不传认为是20
        :type Limit: int
        :param _DateBegin: 形似：2021-05-21 00:00:00 .取值在当前日前30天内，不传默认是当前日前30天日期
        :type DateBegin: str
        :param _DateEnd: 形似：2021-05-21 23:59:59 .取值在当前日前30天内，不传默认是当前日前30天日期
        :type DateEnd: str
        """
        self._OrderType = None
        self._DeviceId = None
        self._WarnLevelArray = None
        self._WarnModeArray = None
        self._Offset = None
        self._Limit = None
        self._DateBegin = None
        self._DateEnd = None

    @property
    def OrderType(self):
        """1:创建时间倒序 2：创建时间升序 3：level倒序 4：leve升序
        :rtype: int
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def DeviceId(self):
        """可选设备id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def WarnLevelArray(self):
        """如果不传则查询所有，取值参见配置
        :rtype: list of int
        """
        return self._WarnLevelArray

    @WarnLevelArray.setter
    def WarnLevelArray(self, WarnLevelArray):
        self._WarnLevelArray = WarnLevelArray

    @property
    def WarnModeArray(self):
        """如果不传则查询所有，取值参见配置
        :rtype: list of int
        """
        return self._WarnModeArray

    @WarnModeArray.setter
    def WarnModeArray(self, WarnModeArray):
        self._WarnModeArray = WarnModeArray

    @property
    def Offset(self):
        """不传认为是0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """不传认为是20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DateBegin(self):
        """形似：2021-05-21 00:00:00 .取值在当前日前30天内，不传默认是当前日前30天日期
        :rtype: str
        """
        return self._DateBegin

    @DateBegin.setter
    def DateBegin(self, DateBegin):
        self._DateBegin = DateBegin

    @property
    def DateEnd(self):
        """形似：2021-05-21 23:59:59 .取值在当前日前30天内，不传默认是当前日前30天日期
        :rtype: str
        """
        return self._DateEnd

    @DateEnd.setter
    def DateEnd(self, DateEnd):
        self._DateEnd = DateEnd


    def _deserialize(self, params):
        self._OrderType = params.get("OrderType")
        self._DeviceId = params.get("DeviceId")
        self._WarnLevelArray = params.get("WarnLevelArray")
        self._WarnModeArray = params.get("WarnModeArray")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DateBegin = params.get("DateBegin")
        self._DateEnd = params.get("DateEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWarningsResponse(AbstractModel):
    """DescribeWarnings返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Data: 告警列表
        :type Data: list of WarningsData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """告警列表
        :rtype: list of WarningsData
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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = WarningsData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeXP2PDataRequest(AbstractModel):
    """DescribeXP2PData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _P2PAppId: P2P应用ID
        :type P2PAppId: str
        :param _From: 查询开始时间，时间戳秒
        :type From: int
        :param _To: 查询结束时间，时间戳秒
        :type To: int
        :param _P2PChannelId: P2P通路ID
        :type P2PChannelId: str
        """
        self._P2PAppId = None
        self._From = None
        self._To = None
        self._P2PChannelId = None

    @property
    def P2PAppId(self):
        """P2P应用ID
        :rtype: str
        """
        return self._P2PAppId

    @P2PAppId.setter
    def P2PAppId(self, P2PAppId):
        self._P2PAppId = P2PAppId

    @property
    def From(self):
        """查询开始时间，时间戳秒
        :rtype: int
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        """查询结束时间，时间戳秒
        :rtype: int
        """
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def P2PChannelId(self):
        """P2P通路ID
        :rtype: str
        """
        return self._P2PChannelId

    @P2PChannelId.setter
    def P2PChannelId(self, P2PChannelId):
        self._P2PChannelId = P2PChannelId


    def _deserialize(self, params):
        self._P2PAppId = params.get("P2PAppId")
        self._From = params.get("From")
        self._To = params.get("To")
        self._P2PChannelId = params.get("P2PChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeXP2PDataResponse(AbstractModel):
    """DescribeXP2PData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: [log_time,cdn_bytes , p2p_bytes, online_people, stuck_times, stuck_people,request,request_success,request_fail,play_fail]
[时间戳,cdn流量(字节) , p2p流量(字节), 在线人数, 卡播次数, 卡播人数,起播请求次数,起播成功次数,起播失败次数,播放失败次数, pcdn cdn流量（字节), pcdn路由流量(字节), 上传流量(字节)]
[1481016480, 46118502414, 75144943171, 61691, 3853, 0,0,0,0,0, 0, 0, 0]
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """[log_time,cdn_bytes , p2p_bytes, online_people, stuck_times, stuck_people,request,request_success,request_fail,play_fail]
[时间戳,cdn流量(字节) , p2p流量(字节), 在线人数, 卡播次数, 卡播人数,起播请求次数,起播成功次数,起播失败次数,播放失败次数, pcdn cdn流量（字节), pcdn路由流量(字节), 上传流量(字节)]
[1481016480, 46118502414, 75144943171, 61691, 3853, 0,0,0,0,0, 0, 0, 0]
        :rtype: str
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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DevGroupInfo(AbstractModel):
    """设备所在分组信息

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        :param _GroupId: 分组ID
        :type GroupId: str
        :param _GroupPath: 分组路径
        :type GroupPath: str
        :param _ParentId: 父分组ID
        :type ParentId: str
        :param _Error: 设备错误，仅在用户没权限或者设备已删除时返回具体结果
        :type Error: str
        """
        self._DeviceId = None
        self._GroupId = None
        self._GroupPath = None
        self._ParentId = None
        self._Error = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def GroupId(self):
        """分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupPath(self):
        """分组路径
        :rtype: str
        """
        return self._GroupPath

    @GroupPath.setter
    def GroupPath(self, GroupPath):
        self._GroupPath = GroupPath

    @property
    def ParentId(self):
        """父分组ID
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def Error(self):
        """设备错误，仅在用户没权限或者设备已删除时返回具体结果
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._GroupId = params.get("GroupId")
        self._GroupPath = params.get("GroupPath")
        self._ParentId = params.get("ParentId")
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceItem(AbstractModel):
    """用于描述唯一一个设备

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        :param _ChannelId: 通道唯一标识
        :type ChannelId: str
        """
        self._DeviceId = None
        self._ChannelId = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ChannelId(self):
        """通道唯一标识
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceMonitorValue(AbstractModel):
    """查询设备统计返回值

    """

    def __init__(self):
        r"""
        :param _Value: 统计值
        :type Value: float
        :param _Time: 统计时间
        :type Time: int
        """
        self._Value = None
        self._Time = None

    @property
    def Value(self):
        """统计值
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Time(self):
        """统计时间
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time


    def _deserialize(self, params):
        self._Value = params.get("Value")
        self._Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Events(AbstractModel):
    """设备事件列表

    """

    def __init__(self):
        r"""
        :param _EventTime: 开始时间，秒级时间戳
        :type EventTime: int
        :param _EventType: 事件类型 1:注册 2:心跳 4:录制异常 5:播放异常 6:流中断
        :type EventType: int
        :param _EventDesc: 事件描述
        :type EventDesc: str
        :param _DeviceType: 设备类型
        :type DeviceType: int
        :param _DeviceAddress: 设备地址
        :type DeviceAddress: str
        :param _DeviceId: 设备Id
        :type DeviceId: str
        :param _ChannelId: 通道Id
        :type ChannelId: str
        :param _EventLog: 事件日志
        :type EventLog: str
        :param _DeviceName: 设备备注名称
        :type DeviceName: str
        """
        self._EventTime = None
        self._EventType = None
        self._EventDesc = None
        self._DeviceType = None
        self._DeviceAddress = None
        self._DeviceId = None
        self._ChannelId = None
        self._EventLog = None
        self._DeviceName = None

    @property
    def EventTime(self):
        """开始时间，秒级时间戳
        :rtype: int
        """
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime

    @property
    def EventType(self):
        """事件类型 1:注册 2:心跳 4:录制异常 5:播放异常 6:流中断
        :rtype: int
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def EventDesc(self):
        """事件描述
        :rtype: str
        """
        return self._EventDesc

    @EventDesc.setter
    def EventDesc(self, EventDesc):
        self._EventDesc = EventDesc

    @property
    def DeviceType(self):
        """设备类型
        :rtype: int
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def DeviceAddress(self):
        """设备地址
        :rtype: str
        """
        return self._DeviceAddress

    @DeviceAddress.setter
    def DeviceAddress(self, DeviceAddress):
        self._DeviceAddress = DeviceAddress

    @property
    def DeviceId(self):
        """设备Id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ChannelId(self):
        """通道Id
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def EventLog(self):
        """事件日志
        :rtype: str
        """
        return self._EventLog

    @EventLog.setter
    def EventLog(self, EventLog):
        self._EventLog = EventLog

    @property
    def DeviceName(self):
        """设备备注名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._EventTime = params.get("EventTime")
        self._EventType = params.get("EventType")
        self._EventDesc = params.get("EventDesc")
        self._DeviceType = params.get("DeviceType")
        self._DeviceAddress = params.get("DeviceAddress")
        self._DeviceId = params.get("DeviceId")
        self._ChannelId = params.get("ChannelId")
        self._EventLog = params.get("EventLog")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRecordDatesByDevRequest(AbstractModel):
    """GetRecordDatesByDev请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        :param _Limit: 限制量，默认200
        :type Limit: int
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _ChannelId: 通道唯一标识，对于NVR设备，多通道IPC设备，设备编码与通道编码不一致的IPC设备，此字段为必填
        :type ChannelId: str
        :param _Type: 1: 云端录制 2: 本地录制
        :type Type: int
        """
        self._DeviceId = None
        self._Limit = None
        self._Offset = None
        self._ChannelId = None
        self._Type = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Limit(self):
        """限制量，默认200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ChannelId(self):
        """通道唯一标识，对于NVR设备，多通道IPC设备，设备编码与通道编码不一致的IPC设备，此字段为必填
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Type(self):
        """1: 云端录制 2: 本地录制
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ChannelId = params.get("ChannelId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRecordDatesByDevResponse(AbstractModel):
    """GetRecordDatesByDev返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Dates: 含有录像文件的日期列表
        :type Dates: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Dates = None
        self._RequestId = None

    @property
    def Dates(self):
        """含有录像文件的日期列表
        :rtype: list of str
        """
        return self._Dates

    @Dates.setter
    def Dates(self, Dates):
        self._Dates = Dates

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
        self._Dates = params.get("Dates")
        self._RequestId = params.get("RequestId")


class GetRecordPlanByDevRequest(AbstractModel):
    """GetRecordPlanByDev请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRecordPlanByDevResponse(AbstractModel):
    """GetRecordPlanByDev返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Plan: 录制计划详情
        :type Plan: :class:`tencentcloud.iotvideoindustry.v20201201.models.RecordPlanItem`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Plan = None
        self._RequestId = None

    @property
    def Plan(self):
        """录制计划详情
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.RecordPlanItem`
        """
        return self._Plan

    @Plan.setter
    def Plan(self, Plan):
        self._Plan = Plan

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
        if params.get("Plan") is not None:
            self._Plan = RecordPlanItem()
            self._Plan._deserialize(params.get("Plan"))
        self._RequestId = params.get("RequestId")


class GetRecordPlanByIdRequest(AbstractModel):
    """GetRecordPlanById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 录制计划ID
        :type PlanId: str
        """
        self._PlanId = None

    @property
    def PlanId(self):
        """录制计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRecordPlanByIdResponse(AbstractModel):
    """GetRecordPlanById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Plan: 录制计划详情
        :type Plan: :class:`tencentcloud.iotvideoindustry.v20201201.models.RecordPlanItem`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Plan = None
        self._RequestId = None

    @property
    def Plan(self):
        """录制计划详情
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.RecordPlanItem`
        """
        return self._Plan

    @Plan.setter
    def Plan(self, Plan):
        self._Plan = Plan

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
        if params.get("Plan") is not None:
            self._Plan = RecordPlanItem()
            self._Plan._deserialize(params.get("Plan"))
        self._RequestId = params.get("RequestId")


class GetRecordPlansRequest(AbstractModel):
    """GetRecordPlans请求参数结构体

    """


class GetRecordPlansResponse(AbstractModel):
    """GetRecordPlans返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Plans: 录制计划详情·列表
        :type Plans: list of RecordPlanItem
        :param _TotalCount: 录制计划总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Plans = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Plans(self):
        """录制计划详情·列表
        :rtype: list of RecordPlanItem
        """
        return self._Plans

    @Plans.setter
    def Plans(self, Plans):
        self._Plans = Plans

    @property
    def TotalCount(self):
        """录制计划总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Plans") is not None:
            self._Plans = []
            for item in params.get("Plans"):
                obj = RecordPlanItem()
                obj._deserialize(item)
                self._Plans.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class GetTimeTemplateByIdRequest(AbstractModel):
    """GetTimeTemplateById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 时间模板ID
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        """时间模板ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTimeTemplateByIdResponse(AbstractModel):
    """GetTimeTemplateById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Template: 时间模板详情
        :type Template: :class:`tencentcloud.iotvideoindustry.v20201201.models.TimeTemplateItem`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Template = None
        self._RequestId = None

    @property
    def Template(self):
        """时间模板详情
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.TimeTemplateItem`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

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
        if params.get("Template") is not None:
            self._Template = TimeTemplateItem()
            self._Template._deserialize(params.get("Template"))
        self._RequestId = params.get("RequestId")


class GetTimeTemplatesRequest(AbstractModel):
    """GetTimeTemplates请求参数结构体

    """


class GetTimeTemplatesResponse(AbstractModel):
    """GetTimeTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Templates: 时间模板列表
        :type Templates: list of TimeTemplateItem
        :param _TotalCount: 时间模板总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Templates = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Templates(self):
        """时间模板列表
        :rtype: list of TimeTemplateItem
        """
        return self._Templates

    @Templates.setter
    def Templates(self, Templates):
        self._Templates = Templates

    @property
    def TotalCount(self):
        """时间模板总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Templates") is not None:
            self._Templates = []
            for item in params.get("Templates"):
                obj = TimeTemplateItem()
                obj._deserialize(item)
                self._Templates.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class GetVideoListByConRequest(AbstractModel):
    """GetVideoListByCon请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制量
        :type Limit: int
        :param _ChannelId: 通道唯一标识，对于NVR设备，多通道IPC设备，设备编码与通道编码不一致的IPC设备，此字段为必填
        :type ChannelId: str
        :param _LatestDay: 0：查询指定日期的录像；1：查询最近一天的录像；默认0
        :type LatestDay: int
        :param _Date: 指定某天。取值【YYYY-MM-DD】
为空时默认查询最近一天的记录
        :type Date: str
        :param _Type: 1: 云端录制 2: 本地录制
        :type Type: int
        """
        self._DeviceId = None
        self._Offset = None
        self._Limit = None
        self._ChannelId = None
        self._LatestDay = None
        self._Date = None
        self._Type = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ChannelId(self):
        """通道唯一标识，对于NVR设备，多通道IPC设备，设备编码与通道编码不一致的IPC设备，此字段为必填
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def LatestDay(self):
        """0：查询指定日期的录像；1：查询最近一天的录像；默认0
        :rtype: int
        """
        return self._LatestDay

    @LatestDay.setter
    def LatestDay(self, LatestDay):
        self._LatestDay = LatestDay

    @property
    def Date(self):
        """指定某天。取值【YYYY-MM-DD】
为空时默认查询最近一天的记录
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Type(self):
        """1: 云端录制 2: 本地录制
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ChannelId = params.get("ChannelId")
        self._LatestDay = params.get("LatestDay")
        self._Date = params.get("Date")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetVideoListByConResponse(AbstractModel):
    """GetVideoListByCon返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoList: 录像详情列表
        :type VideoList: list of RecordTaskItem
        :param _TotalCount: 录像总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VideoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def VideoList(self):
        """录像详情列表
        :rtype: list of RecordTaskItem
        """
        return self._VideoList

    @VideoList.setter
    def VideoList(self, VideoList):
        self._VideoList = VideoList

    @property
    def TotalCount(self):
        """录像总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("VideoList") is not None:
            self._VideoList = []
            for item in params.get("VideoList"):
                obj = RecordTaskItem()
                obj._deserialize(item)
                self._VideoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class GroupDeviceItem(AbstractModel):
    """分组下设备信息

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        :param _NickName: 设备名称
        :type NickName: str
        :param _Status: 设备状态
        :type Status: int
        :param _ExtraInformation: 扩展信息
        :type ExtraInformation: str
        :param _DeviceType: 设备类型
        :type DeviceType: int
        :param _RTSPUrl: rtsp地址
        :type RTSPUrl: str
        :param _DeviceCode: 设备编码
        :type DeviceCode: str
        :param _IsRecord: 是否存在录像
        :type IsRecord: int
        :param _Recordable: 该设备是否可录制
        :type Recordable: int
        :param _Protocol: 设备接入协议
        :type Protocol: str
        :param _CreateTime: 设备创建时间
        :type CreateTime: int
        :param _ChannelNum: 设备通道总数
        :type ChannelNum: int
        :param _VideoChannelNum: 设备视频通道总数
        :type VideoChannelNum: int
        """
        self._DeviceId = None
        self._NickName = None
        self._Status = None
        self._ExtraInformation = None
        self._DeviceType = None
        self._RTSPUrl = None
        self._DeviceCode = None
        self._IsRecord = None
        self._Recordable = None
        self._Protocol = None
        self._CreateTime = None
        self._ChannelNum = None
        self._VideoChannelNum = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def NickName(self):
        """设备名称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Status(self):
        """设备状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExtraInformation(self):
        """扩展信息
        :rtype: str
        """
        return self._ExtraInformation

    @ExtraInformation.setter
    def ExtraInformation(self, ExtraInformation):
        self._ExtraInformation = ExtraInformation

    @property
    def DeviceType(self):
        """设备类型
        :rtype: int
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def RTSPUrl(self):
        """rtsp地址
        :rtype: str
        """
        return self._RTSPUrl

    @RTSPUrl.setter
    def RTSPUrl(self, RTSPUrl):
        self._RTSPUrl = RTSPUrl

    @property
    def DeviceCode(self):
        """设备编码
        :rtype: str
        """
        return self._DeviceCode

    @DeviceCode.setter
    def DeviceCode(self, DeviceCode):
        self._DeviceCode = DeviceCode

    @property
    def IsRecord(self):
        """是否存在录像
        :rtype: int
        """
        return self._IsRecord

    @IsRecord.setter
    def IsRecord(self, IsRecord):
        self._IsRecord = IsRecord

    @property
    def Recordable(self):
        """该设备是否可录制
        :rtype: int
        """
        return self._Recordable

    @Recordable.setter
    def Recordable(self, Recordable):
        self._Recordable = Recordable

    @property
    def Protocol(self):
        """设备接入协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CreateTime(self):
        """设备创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ChannelNum(self):
        """设备通道总数
        :rtype: int
        """
        return self._ChannelNum

    @ChannelNum.setter
    def ChannelNum(self, ChannelNum):
        self._ChannelNum = ChannelNum

    @property
    def VideoChannelNum(self):
        """设备视频通道总数
        :rtype: int
        """
        return self._VideoChannelNum

    @VideoChannelNum.setter
    def VideoChannelNum(self, VideoChannelNum):
        self._VideoChannelNum = VideoChannelNum


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._NickName = params.get("NickName")
        self._Status = params.get("Status")
        self._ExtraInformation = params.get("ExtraInformation")
        self._DeviceType = params.get("DeviceType")
        self._RTSPUrl = params.get("RTSPUrl")
        self._DeviceCode = params.get("DeviceCode")
        self._IsRecord = params.get("IsRecord")
        self._Recordable = params.get("Recordable")
        self._Protocol = params.get("Protocol")
        self._CreateTime = params.get("CreateTime")
        self._ChannelNum = params.get("ChannelNum")
        self._VideoChannelNum = params.get("VideoChannelNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfo(AbstractModel):
    """分组信息详情

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组ID
        :type GroupId: str
        :param _GroupName: 分组名称
        :type GroupName: str
        :param _GroupType: 分组类型
        :type GroupType: str
        :param _GroupPath: 分组路径
        :type GroupPath: str
        :param _ParentId: 父分组ID
        :type ParentId: str
        :param _GroupDescribe: 分组描述
        :type GroupDescribe: str
        :param _ExtraInformation: 扩展信息
        :type ExtraInformation: str
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _GroupStatus: 分组状态
        :type GroupStatus: int
        :param _Error: 设备不存在时产生的错误
        :type Error: str
        """
        self._GroupId = None
        self._GroupName = None
        self._GroupType = None
        self._GroupPath = None
        self._ParentId = None
        self._GroupDescribe = None
        self._ExtraInformation = None
        self._CreateTime = None
        self._GroupStatus = None
        self._Error = None

    @property
    def GroupId(self):
        """分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """分组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupType(self):
        """分组类型
        :rtype: str
        """
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def GroupPath(self):
        """分组路径
        :rtype: str
        """
        return self._GroupPath

    @GroupPath.setter
    def GroupPath(self, GroupPath):
        self._GroupPath = GroupPath

    @property
    def ParentId(self):
        """父分组ID
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def GroupDescribe(self):
        """分组描述
        :rtype: str
        """
        return self._GroupDescribe

    @GroupDescribe.setter
    def GroupDescribe(self, GroupDescribe):
        self._GroupDescribe = GroupDescribe

    @property
    def ExtraInformation(self):
        """扩展信息
        :rtype: str
        """
        return self._ExtraInformation

    @ExtraInformation.setter
    def ExtraInformation(self, ExtraInformation):
        self._ExtraInformation = ExtraInformation

    @property
    def CreateTime(self):
        """创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def GroupStatus(self):
        """分组状态
        :rtype: int
        """
        return self._GroupStatus

    @GroupStatus.setter
    def GroupStatus(self, GroupStatus):
        self._GroupStatus = GroupStatus

    @property
    def Error(self):
        """设备不存在时产生的错误
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._GroupType = params.get("GroupType")
        self._GroupPath = params.get("GroupPath")
        self._ParentId = params.get("ParentId")
        self._GroupDescribe = params.get("GroupDescribe")
        self._ExtraInformation = params.get("ExtraInformation")
        self._CreateTime = params.get("CreateTime")
        self._GroupStatus = params.get("GroupStatus")
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupItem(AbstractModel):
    """分组信息

    """

    def __init__(self):
        r"""
        :param _GroupName: 分组名称
        :type GroupName: str
        :param _ParentId: 父分组ID
        :type ParentId: str
        :param _GroupId: 分组ID
        :type GroupId: str
        :param _GroupPath: 分组路径
        :type GroupPath: str
        :param _GroupDescribe: 分组描述
        :type GroupDescribe: str
        :param _DeviceNum: 分组绑定设备数
        :type DeviceNum: int
        :param _SubGroupNum: 子分组数量
        :type SubGroupNum: int
        :param _ExtraInformation: 分组附加信息
        :type ExtraInformation: str
        :param _GroupType: 分组类型
        :type GroupType: str
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _GroupStatus: 分组状态
        :type GroupStatus: int
        """
        self._GroupName = None
        self._ParentId = None
        self._GroupId = None
        self._GroupPath = None
        self._GroupDescribe = None
        self._DeviceNum = None
        self._SubGroupNum = None
        self._ExtraInformation = None
        self._GroupType = None
        self._CreateTime = None
        self._GroupStatus = None

    @property
    def GroupName(self):
        """分组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ParentId(self):
        """父分组ID
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def GroupId(self):
        """分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupPath(self):
        """分组路径
        :rtype: str
        """
        return self._GroupPath

    @GroupPath.setter
    def GroupPath(self, GroupPath):
        self._GroupPath = GroupPath

    @property
    def GroupDescribe(self):
        """分组描述
        :rtype: str
        """
        return self._GroupDescribe

    @GroupDescribe.setter
    def GroupDescribe(self, GroupDescribe):
        self._GroupDescribe = GroupDescribe

    @property
    def DeviceNum(self):
        """分组绑定设备数
        :rtype: int
        """
        return self._DeviceNum

    @DeviceNum.setter
    def DeviceNum(self, DeviceNum):
        self._DeviceNum = DeviceNum

    @property
    def SubGroupNum(self):
        """子分组数量
        :rtype: int
        """
        return self._SubGroupNum

    @SubGroupNum.setter
    def SubGroupNum(self, SubGroupNum):
        self._SubGroupNum = SubGroupNum

    @property
    def ExtraInformation(self):
        """分组附加信息
        :rtype: str
        """
        return self._ExtraInformation

    @ExtraInformation.setter
    def ExtraInformation(self, ExtraInformation):
        self._ExtraInformation = ExtraInformation

    @property
    def GroupType(self):
        """分组类型
        :rtype: str
        """
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def CreateTime(self):
        """创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def GroupStatus(self):
        """分组状态
        :rtype: int
        """
        return self._GroupStatus

    @GroupStatus.setter
    def GroupStatus(self, GroupStatus):
        self._GroupStatus = GroupStatus


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._ParentId = params.get("ParentId")
        self._GroupId = params.get("GroupId")
        self._GroupPath = params.get("GroupPath")
        self._GroupDescribe = params.get("GroupDescribe")
        self._DeviceNum = params.get("DeviceNum")
        self._SubGroupNum = params.get("SubGroupNum")
        self._ExtraInformation = params.get("ExtraInformation")
        self._GroupType = params.get("GroupType")
        self._CreateTime = params.get("CreateTime")
        self._GroupStatus = params.get("GroupStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveChannelInfo(AbstractModel):
    """频道信息

    """

    def __init__(self):
        r"""
        :param _LiveChannelId: 频道ID
        :type LiveChannelId: str
        :param _LiveChannelName: 频道名称
        :type LiveChannelName: str
        :param _LiveChannelType: 频道类型
        :type LiveChannelType: int
        :param _LiveStatus: 通道直播状态：1: 未推流，2: 推流中
        :type LiveStatus: int
        :param _PushStreamAddress: 推流地址
        :type PushStreamAddress: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 修改时间
        :type UpdateTime: str
        """
        self._LiveChannelId = None
        self._LiveChannelName = None
        self._LiveChannelType = None
        self._LiveStatus = None
        self._PushStreamAddress = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def LiveChannelId(self):
        """频道ID
        :rtype: str
        """
        return self._LiveChannelId

    @LiveChannelId.setter
    def LiveChannelId(self, LiveChannelId):
        self._LiveChannelId = LiveChannelId

    @property
    def LiveChannelName(self):
        """频道名称
        :rtype: str
        """
        return self._LiveChannelName

    @LiveChannelName.setter
    def LiveChannelName(self, LiveChannelName):
        self._LiveChannelName = LiveChannelName

    @property
    def LiveChannelType(self):
        """频道类型
        :rtype: int
        """
        return self._LiveChannelType

    @LiveChannelType.setter
    def LiveChannelType(self, LiveChannelType):
        self._LiveChannelType = LiveChannelType

    @property
    def LiveStatus(self):
        """通道直播状态：1: 未推流，2: 推流中
        :rtype: int
        """
        return self._LiveStatus

    @LiveStatus.setter
    def LiveStatus(self, LiveStatus):
        self._LiveStatus = LiveStatus

    @property
    def PushStreamAddress(self):
        """推流地址
        :rtype: str
        """
        return self._PushStreamAddress

    @PushStreamAddress.setter
    def PushStreamAddress(self, PushStreamAddress):
        self._PushStreamAddress = PushStreamAddress

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """修改时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._LiveChannelId = params.get("LiveChannelId")
        self._LiveChannelName = params.get("LiveChannelName")
        self._LiveChannelType = params.get("LiveChannelType")
        self._LiveStatus = params.get("LiveStatus")
        self._PushStreamAddress = params.get("PushStreamAddress")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveChannelItem(AbstractModel):
    """直播频道详情

    """

    def __init__(self):
        r"""
        :param _ChannelId: 频道ID
        :type ChannelId: str
        :param _ChannelName: 频道名称
        :type ChannelName: str
        """
        self._ChannelId = None
        self._ChannelName = None

    @property
    def ChannelId(self):
        """频道ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        """频道名称
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveRecordItem(AbstractModel):
    """直播录制详情item

    """

    def __init__(self):
        r"""
        :param _IntID: 录制文件自增ID
        :type IntID: int
        :param _LiveChannelId: 直播频道ID
        :type LiveChannelId: str
        :param _ExpectDeleteTime: 过期时间
        :type ExpectDeleteTime: int
        :param _RecordTimeLen: 录制时长
        :type RecordTimeLen: int
        :param _FileSize: 文件大小
        :type FileSize: int
        :param _VideoUrl: 录制文件url
        :type VideoUrl: str
        :param _RecordPlanId: 录制计划ID
        :type RecordPlanId: str
        :param _StartTime: 录制开始时间
        :type StartTime: int
        :param _EndTime: 录制结束时间
        :type EndTime: int
        """
        self._IntID = None
        self._LiveChannelId = None
        self._ExpectDeleteTime = None
        self._RecordTimeLen = None
        self._FileSize = None
        self._VideoUrl = None
        self._RecordPlanId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def IntID(self):
        """录制文件自增ID
        :rtype: int
        """
        return self._IntID

    @IntID.setter
    def IntID(self, IntID):
        self._IntID = IntID

    @property
    def LiveChannelId(self):
        """直播频道ID
        :rtype: str
        """
        return self._LiveChannelId

    @LiveChannelId.setter
    def LiveChannelId(self, LiveChannelId):
        self._LiveChannelId = LiveChannelId

    @property
    def ExpectDeleteTime(self):
        """过期时间
        :rtype: int
        """
        return self._ExpectDeleteTime

    @ExpectDeleteTime.setter
    def ExpectDeleteTime(self, ExpectDeleteTime):
        self._ExpectDeleteTime = ExpectDeleteTime

    @property
    def RecordTimeLen(self):
        """录制时长
        :rtype: int
        """
        return self._RecordTimeLen

    @RecordTimeLen.setter
    def RecordTimeLen(self, RecordTimeLen):
        self._RecordTimeLen = RecordTimeLen

    @property
    def FileSize(self):
        """文件大小
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def VideoUrl(self):
        """录制文件url
        :rtype: str
        """
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def RecordPlanId(self):
        """录制计划ID
        :rtype: str
        """
        return self._RecordPlanId

    @RecordPlanId.setter
    def RecordPlanId(self, RecordPlanId):
        self._RecordPlanId = RecordPlanId

    @property
    def StartTime(self):
        """录制开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """录制结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._IntID = params.get("IntID")
        self._LiveChannelId = params.get("LiveChannelId")
        self._ExpectDeleteTime = params.get("ExpectDeleteTime")
        self._RecordTimeLen = params.get("RecordTimeLen")
        self._FileSize = params.get("FileSize")
        self._VideoUrl = params.get("VideoUrl")
        self._RecordPlanId = params.get("RecordPlanId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveRecordPlanItem(AbstractModel):
    """直播录制计划详情

    """

    def __init__(self):
        r"""
        :param _PlanId: 计划ID
        :type PlanId: str
        :param _PlanName: 计划名称
        :type PlanName: str
        """
        self._PlanId = None
        self._PlanName = None

    @property
    def PlanId(self):
        """计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanName(self):
        """计划名称
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PlanName = params.get("PlanName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MessageForward(AbstractModel):
    """消息转发配置信息

    """

    def __init__(self):
        r"""
        :param _IntId: 配置ID
        :type IntId: int
        :param _Uin: 用户Uin
        :type Uin: str
        :param _MessageType: json数组， 转发类型 1: 告警 2:GPS
        :type MessageType: str
        :param _RegionId: 区域ID
        :type RegionId: str
        :param _RegionName: 区域名称
        :type RegionName: str
        :param _Instance: 实例ID
        :type Instance: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _TopicId: kafka topic id
        :type TopicId: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _TopicName: topic 名称
        :type TopicName: str
        """
        self._IntId = None
        self._Uin = None
        self._MessageType = None
        self._RegionId = None
        self._RegionName = None
        self._Instance = None
        self._InstanceName = None
        self._TopicId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._TopicName = None

    @property
    def IntId(self):
        """配置ID
        :rtype: int
        """
        return self._IntId

    @IntId.setter
    def IntId(self, IntId):
        self._IntId = IntId

    @property
    def Uin(self):
        """用户Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def MessageType(self):
        """json数组， 转发类型 1: 告警 2:GPS
        :rtype: str
        """
        return self._MessageType

    @MessageType.setter
    def MessageType(self, MessageType):
        self._MessageType = MessageType

    @property
    def RegionId(self):
        """区域ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """区域名称
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def Instance(self):
        """实例ID
        :rtype: str
        """
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def TopicId(self):
        """kafka topic id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def TopicName(self):
        """topic 名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._IntId = params.get("IntId")
        self._Uin = params.get("Uin")
        self._MessageType = params.get("MessageType")
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._Instance = params.get("Instance")
        self._InstanceName = params.get("InstanceName")
        self._TopicId = params.get("TopicId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBindPlanLiveChannelRequest(AbstractModel):
    """ModifyBindPlanLiveChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 直播录制计划ID
        :type PlanId: str
        :param _Type: 1: 绑定 2: 解绑
        :type Type: int
        :param _LiveChannelIds: 直播频道ID列表
        :type LiveChannelIds: list of str
        """
        self._PlanId = None
        self._Type = None
        self._LiveChannelIds = None

    @property
    def PlanId(self):
        """直播录制计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def Type(self):
        """1: 绑定 2: 解绑
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def LiveChannelIds(self):
        """直播频道ID列表
        :rtype: list of str
        """
        return self._LiveChannelIds

    @LiveChannelIds.setter
    def LiveChannelIds(self, LiveChannelIds):
        self._LiveChannelIds = LiveChannelIds


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._Type = params.get("Type")
        self._LiveChannelIds = params.get("LiveChannelIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBindPlanLiveChannelResponse(AbstractModel):
    """ModifyBindPlanLiveChannel返回参数结构体

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


class ModifyBindRecordingPlanRequest(AbstractModel):
    """ModifyBindRecordingPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 操作类型： 1-绑定设备 ；2-解绑设备
        :type Type: int
        :param _PlanId: 录制计划ID
        :type PlanId: str
        :param _Channels: 录制通道列表
        :type Channels: list of ChannelItem
        """
        self._Type = None
        self._PlanId = None
        self._Channels = None

    @property
    def Type(self):
        """操作类型： 1-绑定设备 ；2-解绑设备
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PlanId(self):
        """录制计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def Channels(self):
        """录制通道列表
        :rtype: list of ChannelItem
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._PlanId = params.get("PlanId")
        if params.get("Channels") is not None:
            self._Channels = []
            for item in params.get("Channels"):
                obj = ChannelItem()
                obj._deserialize(item)
                self._Channels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBindRecordingPlanResponse(AbstractModel):
    """ModifyBindRecordingPlan返回参数结构体

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


class ModifyBindSceneChannelsRequest(AbstractModel):
    """ModifyBindSceneChannels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SceneId: 场景ID
        :type SceneId: int
        :param _Type: 1: 绑定 2: 解绑
        :type Type: int
        :param _Channels: 通道列表
        :type Channels: list of ChannelItem
        """
        self._SceneId = None
        self._Type = None
        self._Channels = None

    @property
    def SceneId(self):
        """场景ID
        :rtype: int
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def Type(self):
        """1: 绑定 2: 解绑
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Channels(self):
        """通道列表
        :rtype: list of ChannelItem
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels


    def _deserialize(self, params):
        self._SceneId = params.get("SceneId")
        self._Type = params.get("Type")
        if params.get("Channels") is not None:
            self._Channels = []
            for item in params.get("Channels"):
                obj = ChannelItem()
                obj._deserialize(item)
                self._Channels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBindSceneChannelsResponse(AbstractModel):
    """ModifyBindSceneChannels返回参数结构体

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


class ModifyBindSceneDeviceRequest(AbstractModel):
    """ModifyBindSceneDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SceneId: 场景ID
        :type SceneId: int
        :param _Type: 1: 绑定 2: 解绑
        :type Type: int
        :param _Devices: 设备列表
        :type Devices: list of DeviceItem
        """
        self._SceneId = None
        self._Type = None
        self._Devices = None

    @property
    def SceneId(self):
        """场景ID
        :rtype: int
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def Type(self):
        """1: 绑定 2: 解绑
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Devices(self):
        """设备列表
        :rtype: list of DeviceItem
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices


    def _deserialize(self, params):
        self._SceneId = params.get("SceneId")
        self._Type = params.get("Type")
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeviceItem()
                obj._deserialize(item)
                self._Devices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBindSceneDeviceResponse(AbstractModel):
    """ModifyBindSceneDevice返回参数结构体

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


class ModifyDeviceDataRequest(AbstractModel):
    """ModifyDeviceData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        :param _NickName: 设备名称
        :type NickName: str
        """
        self._DeviceId = None
        self._NickName = None

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def NickName(self):
        """设备名称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._NickName = params.get("NickName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceDataResponse(AbstractModel):
    """ModifyDeviceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 操作结果,“OK”表示成功，其他表示失败。
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """操作结果,“OK”表示成功，其他表示失败。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyLiveChannelRequest(AbstractModel):
    """ModifyLiveChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LiveChannelId: 直播频道ID
        :type LiveChannelId: str
        :param _LiveChannelName: 直播频道名
        :type LiveChannelName: str
        """
        self._LiveChannelId = None
        self._LiveChannelName = None

    @property
    def LiveChannelId(self):
        """直播频道ID
        :rtype: str
        """
        return self._LiveChannelId

    @LiveChannelId.setter
    def LiveChannelId(self, LiveChannelId):
        self._LiveChannelId = LiveChannelId

    @property
    def LiveChannelName(self):
        """直播频道名
        :rtype: str
        """
        return self._LiveChannelName

    @LiveChannelName.setter
    def LiveChannelName(self, LiveChannelName):
        self._LiveChannelName = LiveChannelName


    def _deserialize(self, params):
        self._LiveChannelId = params.get("LiveChannelId")
        self._LiveChannelName = params.get("LiveChannelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveChannelResponse(AbstractModel):
    """ModifyLiveChannel返回参数结构体

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


class ModifyLiveRecordPlanRequest(AbstractModel):
    """ModifyLiveRecordPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 录制计划ID
        :type PlanId: str
        :param _PlanName: 录制计划名
        :type PlanName: str
        :param _TemplateId: 时间模板ID，固定直播时为必填
        :type TemplateId: str
        """
        self._PlanId = None
        self._PlanName = None
        self._TemplateId = None

    @property
    def PlanId(self):
        """录制计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanName(self):
        """录制计划名
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        """时间模板ID，固定直播时为必填
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveRecordPlanResponse(AbstractModel):
    """ModifyLiveRecordPlan返回参数结构体

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


class ModifyLiveVideoRequest(AbstractModel):
    """ModifyLiveVideo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IntIDs: 视频ID 列表, 大小限制(100)
        :type IntIDs: list of int
        :param _ExpireTime: 过期时间 秒 (-1: 为永不过期)
        :type ExpireTime: int
        """
        self._IntIDs = None
        self._ExpireTime = None

    @property
    def IntIDs(self):
        """视频ID 列表, 大小限制(100)
        :rtype: list of int
        """
        return self._IntIDs

    @IntIDs.setter
    def IntIDs(self, IntIDs):
        self._IntIDs = IntIDs

    @property
    def ExpireTime(self):
        """过期时间 秒 (-1: 为永不过期)
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._IntIDs = params.get("IntIDs")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveVideoResponse(AbstractModel):
    """ModifyLiveVideo返回参数结构体

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


class ModifyMessageForwardRequest(AbstractModel):
    """ModifyMessageForward请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IntId: 配置ID
        :type IntId: int
        :param _MessageType: json数组， 转发类型 1: 告警 2:GPS
        :type MessageType: str
        """
        self._IntId = None
        self._MessageType = None

    @property
    def IntId(self):
        """配置ID
        :rtype: int
        """
        return self._IntId

    @IntId.setter
    def IntId(self, IntId):
        self._IntId = IntId

    @property
    def MessageType(self):
        """json数组， 转发类型 1: 告警 2:GPS
        :rtype: str
        """
        return self._MessageType

    @MessageType.setter
    def MessageType(self, MessageType):
        self._MessageType = MessageType


    def _deserialize(self, params):
        self._IntId = params.get("IntId")
        self._MessageType = params.get("MessageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMessageForwardResponse(AbstractModel):
    """ModifyMessageForward返回参数结构体

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


class ModifyPresetRequest(AbstractModel):
    """ModifyPreset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelId: 通道ID
        :type ChannelId: str
        :param _PresetId: 预置位编码 范围1-8
        :type PresetId: int
        :param _PresetName: 预制位名称
        :type PresetName: str
        :param _DeviceId: 设备Id
        :type DeviceId: str
        """
        self._ChannelId = None
        self._PresetId = None
        self._PresetName = None
        self._DeviceId = None

    @property
    def ChannelId(self):
        """通道ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def PresetId(self):
        """预置位编码 范围1-8
        :rtype: int
        """
        return self._PresetId

    @PresetId.setter
    def PresetId(self, PresetId):
        self._PresetId = PresetId

    @property
    def PresetName(self):
        """预制位名称
        :rtype: str
        """
        return self._PresetName

    @PresetName.setter
    def PresetName(self, PresetName):
        self._PresetName = PresetName

    @property
    def DeviceId(self):
        """设备Id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._PresetId = params.get("PresetId")
        self._PresetName = params.get("PresetName")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPresetResponse(AbstractModel):
    """ModifyPreset返回参数结构体

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


class ModifyRecordingPlanRequest(AbstractModel):
    """ModifyRecordingPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 录制计划ID
        :type PlanId: str
        :param _Name: 计划名称
        :type Name: str
        :param _TimeTemplateId: 时间模板ID
        :type TimeTemplateId: str
        """
        self._PlanId = None
        self._Name = None
        self._TimeTemplateId = None

    @property
    def PlanId(self):
        """录制计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def Name(self):
        """计划名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TimeTemplateId(self):
        """时间模板ID
        :rtype: str
        """
        return self._TimeTemplateId

    @TimeTemplateId.setter
    def TimeTemplateId(self, TimeTemplateId):
        self._TimeTemplateId = TimeTemplateId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._Name = params.get("Name")
        self._TimeTemplateId = params.get("TimeTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordingPlanResponse(AbstractModel):
    """ModifyRecordingPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 操作结果
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """操作结果
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifySceneRequest(AbstractModel):
    """ModifyScene请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IntId: 场景ID
        :type IntId: int
        :param _SceneName: 场景名称
        :type SceneName: str
        :param _SceneTrigger: 触发条件
        :type SceneTrigger: str
        :param _RecordDuration: 录制时长(秒)
        :type RecordDuration: int
        """
        self._IntId = None
        self._SceneName = None
        self._SceneTrigger = None
        self._RecordDuration = None

    @property
    def IntId(self):
        """场景ID
        :rtype: int
        """
        return self._IntId

    @IntId.setter
    def IntId(self, IntId):
        self._IntId = IntId

    @property
    def SceneName(self):
        """场景名称
        :rtype: str
        """
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName

    @property
    def SceneTrigger(self):
        """触发条件
        :rtype: str
        """
        return self._SceneTrigger

    @SceneTrigger.setter
    def SceneTrigger(self, SceneTrigger):
        self._SceneTrigger = SceneTrigger

    @property
    def RecordDuration(self):
        """录制时长(秒)
        :rtype: int
        """
        return self._RecordDuration

    @RecordDuration.setter
    def RecordDuration(self, RecordDuration):
        self._RecordDuration = RecordDuration


    def _deserialize(self, params):
        self._IntId = params.get("IntId")
        self._SceneName = params.get("SceneName")
        self._SceneTrigger = params.get("SceneTrigger")
        self._RecordDuration = params.get("RecordDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySceneResponse(AbstractModel):
    """ModifyScene返回参数结构体

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


class ModifySubscriptionStatusRequest(AbstractModel):
    """ModifySubscriptionStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _Status: 订阅状态 1：关闭订阅 2：开启订阅
        :type Status: int
        :param _SubscriptionItem: 订阅类型 Alarm:告警订阅 Catalog:目录订阅 MobilePosition:移动位置订阅
        :type SubscriptionItem: str
        """
        self._DeviceId = None
        self._Status = None
        self._SubscriptionItem = None

    @property
    def DeviceId(self):
        """设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Status(self):
        """订阅状态 1：关闭订阅 2：开启订阅
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubscriptionItem(self):
        """订阅类型 Alarm:告警订阅 Catalog:目录订阅 MobilePosition:移动位置订阅
        :rtype: str
        """
        return self._SubscriptionItem

    @SubscriptionItem.setter
    def SubscriptionItem(self, SubscriptionItem):
        self._SubscriptionItem = SubscriptionItem


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Status = params.get("Status")
        self._SubscriptionItem = params.get("SubscriptionItem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscriptionStatusResponse(AbstractModel):
    """ModifySubscriptionStatus返回参数结构体

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


class ModifyVideoInfoRequest(AbstractModel):
    """ModifyVideoInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InitIDs: 视频ID列表长度限制100内
        :type InitIDs: list of int
        :param _ExpireTime: 过期时间 时间戳 -1: 永不过期 0: 无效值
        :type ExpireTime: int
        """
        self._InitIDs = None
        self._ExpireTime = None

    @property
    def InitIDs(self):
        """视频ID列表长度限制100内
        :rtype: list of int
        """
        return self._InitIDs

    @InitIDs.setter
    def InitIDs(self, InitIDs):
        self._InitIDs = InitIDs

    @property
    def ExpireTime(self):
        """过期时间 时间戳 -1: 永不过期 0: 无效值
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._InitIDs = params.get("InitIDs")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVideoInfoResponse(AbstractModel):
    """ModifyVideoInfo返回参数结构体

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


class PresetItem(AbstractModel):
    """预置位结构出参

    """

    def __init__(self):
        r"""
        :param _PresetId: 预置位ID
        :type PresetId: int
        :param _PresetName: 预置位名称
        :type PresetName: str
        :param _Status: 预置位状态 0:未设置预置位 1:已设置预置位 2:已设置预置位&看守位
        :type Status: int
        :param _ResetTime: 预置位启用时的自动归位时间
        :type ResetTime: int
        """
        self._PresetId = None
        self._PresetName = None
        self._Status = None
        self._ResetTime = None

    @property
    def PresetId(self):
        """预置位ID
        :rtype: int
        """
        return self._PresetId

    @PresetId.setter
    def PresetId(self, PresetId):
        self._PresetId = PresetId

    @property
    def PresetName(self):
        """预置位名称
        :rtype: str
        """
        return self._PresetName

    @PresetName.setter
    def PresetName(self, PresetName):
        self._PresetName = PresetName

    @property
    def Status(self):
        """预置位状态 0:未设置预置位 1:已设置预置位 2:已设置预置位&看守位
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ResetTime(self):
        """预置位启用时的自动归位时间
        :rtype: int
        """
        return self._ResetTime

    @ResetTime.setter
    def ResetTime(self, ResetTime):
        self._ResetTime = ResetTime


    def _deserialize(self, params):
        self._PresetId = params.get("PresetId")
        self._PresetName = params.get("PresetName")
        self._Status = params.get("Status")
        self._ResetTime = params.get("ResetTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordPlanDetail(AbstractModel):
    """录制计划详情

    """

    def __init__(self):
        r"""
        :param _PlanId: 计划ID
        :type PlanId: str
        :param _Name: 计划名称
        :type Name: str
        :param _TimeTemplateId: 时间模板ID
        :type TimeTemplateId: str
        :param _TimeTemplateName: 时间模板名称
        :type TimeTemplateName: str
        :param _Channels: 绑定的通道列表
        :type Channels: list of ChannelItem
        :param _RecordStorageTime: 存储周期（天）
        :type RecordStorageTime: int
        """
        self._PlanId = None
        self._Name = None
        self._TimeTemplateId = None
        self._TimeTemplateName = None
        self._Channels = None
        self._RecordStorageTime = None

    @property
    def PlanId(self):
        """计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def Name(self):
        """计划名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TimeTemplateId(self):
        """时间模板ID
        :rtype: str
        """
        return self._TimeTemplateId

    @TimeTemplateId.setter
    def TimeTemplateId(self, TimeTemplateId):
        self._TimeTemplateId = TimeTemplateId

    @property
    def TimeTemplateName(self):
        """时间模板名称
        :rtype: str
        """
        return self._TimeTemplateName

    @TimeTemplateName.setter
    def TimeTemplateName(self, TimeTemplateName):
        self._TimeTemplateName = TimeTemplateName

    @property
    def Channels(self):
        """绑定的通道列表
        :rtype: list of ChannelItem
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels

    @property
    def RecordStorageTime(self):
        """存储周期（天）
        :rtype: int
        """
        return self._RecordStorageTime

    @RecordStorageTime.setter
    def RecordStorageTime(self, RecordStorageTime):
        self._RecordStorageTime = RecordStorageTime


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._Name = params.get("Name")
        self._TimeTemplateId = params.get("TimeTemplateId")
        self._TimeTemplateName = params.get("TimeTemplateName")
        if params.get("Channels") is not None:
            self._Channels = []
            for item in params.get("Channels"):
                obj = ChannelItem()
                obj._deserialize(item)
                self._Channels.append(obj)
        self._RecordStorageTime = params.get("RecordStorageTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordPlanItem(AbstractModel):
    """录制计划详情

    """

    def __init__(self):
        r"""
        :param _PlanId: 计划ID
        :type PlanId: str
        :param _Name: 计划名称
        :type Name: str
        :param _TimeTemplateId: 时间模板ID
        :type TimeTemplateId: str
        :param _TimeTemplateName: 时间模板名称
        :type TimeTemplateName: str
        :param _EventId: 录制类型
        :type EventId: int
        :param _Devices: 绑定的设备列表
        :type Devices: list of DeviceItem
        :param _RecordStorageTime: 录像存储天数
        :type RecordStorageTime: int
        """
        self._PlanId = None
        self._Name = None
        self._TimeTemplateId = None
        self._TimeTemplateName = None
        self._EventId = None
        self._Devices = None
        self._RecordStorageTime = None

    @property
    def PlanId(self):
        """计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def Name(self):
        """计划名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TimeTemplateId(self):
        """时间模板ID
        :rtype: str
        """
        return self._TimeTemplateId

    @TimeTemplateId.setter
    def TimeTemplateId(self, TimeTemplateId):
        self._TimeTemplateId = TimeTemplateId

    @property
    def TimeTemplateName(self):
        """时间模板名称
        :rtype: str
        """
        return self._TimeTemplateName

    @TimeTemplateName.setter
    def TimeTemplateName(self, TimeTemplateName):
        self._TimeTemplateName = TimeTemplateName

    @property
    def EventId(self):
        """录制类型
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Devices(self):
        """绑定的设备列表
        :rtype: list of DeviceItem
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def RecordStorageTime(self):
        """录像存储天数
        :rtype: int
        """
        return self._RecordStorageTime

    @RecordStorageTime.setter
    def RecordStorageTime(self, RecordStorageTime):
        self._RecordStorageTime = RecordStorageTime


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._Name = params.get("Name")
        self._TimeTemplateId = params.get("TimeTemplateId")
        self._TimeTemplateName = params.get("TimeTemplateName")
        self._EventId = params.get("EventId")
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeviceItem()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._RecordStorageTime = params.get("RecordStorageTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordStatistic(AbstractModel):
    """大盘统计-录像存储统计 出参RecordStatistic

    """

    def __init__(self):
        r"""
        :param _Time: 时间戳
        :type Time: int
        :param _Value: 统计结果
        :type Value: :class:`tencentcloud.iotvideoindustry.v20201201.models.RecordStatisticValue`
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        """时间戳
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        """统计结果
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.RecordStatisticValue`
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        if params.get("Value") is not None:
            self._Value = RecordStatisticValue()
            self._Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordStatisticValue(AbstractModel):
    """大盘统计-录像存储统计 出参Value

    """

    def __init__(self):
        r"""
        :param _ExpectTimeLen: 期望执行时间 秒
        :type ExpectTimeLen: int
        :param _RecordTimeLen: 实际执行时间 秒
        :type RecordTimeLen: int
        :param _FileSize: 存储大小 G
        :type FileSize: float
        """
        self._ExpectTimeLen = None
        self._RecordTimeLen = None
        self._FileSize = None

    @property
    def ExpectTimeLen(self):
        """期望执行时间 秒
        :rtype: int
        """
        return self._ExpectTimeLen

    @ExpectTimeLen.setter
    def ExpectTimeLen(self, ExpectTimeLen):
        self._ExpectTimeLen = ExpectTimeLen

    @property
    def RecordTimeLen(self):
        """实际执行时间 秒
        :rtype: int
        """
        return self._RecordTimeLen

    @RecordTimeLen.setter
    def RecordTimeLen(self, RecordTimeLen):
        self._RecordTimeLen = RecordTimeLen

    @property
    def FileSize(self):
        """存储大小 G
        :rtype: float
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize


    def _deserialize(self, params):
        self._ExpectTimeLen = params.get("ExpectTimeLen")
        self._RecordTimeLen = params.get("RecordTimeLen")
        self._FileSize = params.get("FileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTaskItem(AbstractModel):
    """普通设备的录像详情

    """

    def __init__(self):
        r"""
        :param _RecordTaskId: 录像任务ID
        :type RecordTaskId: str
        :param _RecordPlanId: 录制计划ID
        :type RecordPlanId: str
        :param _StartTime: 本录制片段开始时间
        :type StartTime: int
        :param _EndTime: 本录制片段结束时间
        :type EndTime: int
        :param _EventId: 录制模式
        :type EventId: int
        :param _VideoUrl: 本录制片段对应的录制文件URL
        :type VideoUrl: str
        :param _RecordStatus: 本录制片段当前的录制状态
        :type RecordStatus: int
        :param _SceneId: 场景ID
        :type SceneId: int
        :param _WarnId: 告警ID
        :type WarnId: int
        :param _RecordId: 录制id，NVR下属设备有效
        :type RecordId: str
        """
        self._RecordTaskId = None
        self._RecordPlanId = None
        self._StartTime = None
        self._EndTime = None
        self._EventId = None
        self._VideoUrl = None
        self._RecordStatus = None
        self._SceneId = None
        self._WarnId = None
        self._RecordId = None

    @property
    def RecordTaskId(self):
        """录像任务ID
        :rtype: str
        """
        return self._RecordTaskId

    @RecordTaskId.setter
    def RecordTaskId(self, RecordTaskId):
        self._RecordTaskId = RecordTaskId

    @property
    def RecordPlanId(self):
        """录制计划ID
        :rtype: str
        """
        return self._RecordPlanId

    @RecordPlanId.setter
    def RecordPlanId(self, RecordPlanId):
        self._RecordPlanId = RecordPlanId

    @property
    def StartTime(self):
        """本录制片段开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """本录制片段结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def EventId(self):
        """录制模式
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def VideoUrl(self):
        """本录制片段对应的录制文件URL
        :rtype: str
        """
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def RecordStatus(self):
        """本录制片段当前的录制状态
        :rtype: int
        """
        return self._RecordStatus

    @RecordStatus.setter
    def RecordStatus(self, RecordStatus):
        self._RecordStatus = RecordStatus

    @property
    def SceneId(self):
        """场景ID
        :rtype: int
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def WarnId(self):
        """告警ID
        :rtype: int
        """
        return self._WarnId

    @WarnId.setter
    def WarnId(self, WarnId):
        self._WarnId = WarnId

    @property
    def RecordId(self):
        """录制id，NVR下属设备有效
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId


    def _deserialize(self, params):
        self._RecordTaskId = params.get("RecordTaskId")
        self._RecordPlanId = params.get("RecordPlanId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._EventId = params.get("EventId")
        self._VideoUrl = params.get("VideoUrl")
        self._RecordStatus = params.get("RecordStatus")
        self._SceneId = params.get("SceneId")
        self._WarnId = params.get("WarnId")
        self._RecordId = params.get("RecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetWarningRequest(AbstractModel):
    """ResetWarning请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 告警ID
        :type Id: int
        :param _Index: Es中告警ID
        :type Index: str
        """
        self._Id = None
        self._Index = None

    @property
    def Id(self):
        """告警ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Index(self):
        """Es中告警ID
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetWarningResponse(AbstractModel):
    """ResetWarning返回参数结构体

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


class SceneItem(AbstractModel):
    """场景列表元素

    """

    def __init__(self):
        r"""
        :param _IntId: 场景ID
        :type IntId: int
        :param _Uin: 用户UIN
        :type Uin: str
        :param _SceneName: 场景名称
        :type SceneName: str
        :param _SceneTrigger: 触发规则
        :type SceneTrigger: str
        :param _RecordDuration: 录制时长 秒
        :type RecordDuration: int
        :param _StoreDuration: 存储时长 天
        :type StoreDuration: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 修改时间
        :type UpdateTime: str
        """
        self._IntId = None
        self._Uin = None
        self._SceneName = None
        self._SceneTrigger = None
        self._RecordDuration = None
        self._StoreDuration = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def IntId(self):
        """场景ID
        :rtype: int
        """
        return self._IntId

    @IntId.setter
    def IntId(self, IntId):
        self._IntId = IntId

    @property
    def Uin(self):
        """用户UIN
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SceneName(self):
        """场景名称
        :rtype: str
        """
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName

    @property
    def SceneTrigger(self):
        """触发规则
        :rtype: str
        """
        return self._SceneTrigger

    @SceneTrigger.setter
    def SceneTrigger(self, SceneTrigger):
        self._SceneTrigger = SceneTrigger

    @property
    def RecordDuration(self):
        """录制时长 秒
        :rtype: int
        """
        return self._RecordDuration

    @RecordDuration.setter
    def RecordDuration(self, RecordDuration):
        self._RecordDuration = RecordDuration

    @property
    def StoreDuration(self):
        """存储时长 天
        :rtype: int
        """
        return self._StoreDuration

    @StoreDuration.setter
    def StoreDuration(self, StoreDuration):
        self._StoreDuration = StoreDuration

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """修改时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._IntId = params.get("IntId")
        self._Uin = params.get("Uin")
        self._SceneName = params.get("SceneName")
        self._SceneTrigger = params.get("SceneTrigger")
        self._RecordDuration = params.get("RecordDuration")
        self._StoreDuration = params.get("StoreDuration")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerConfiguration(AbstractModel):
    """SIIP服务器相关配置项

    """

    def __init__(self):
        r"""
        :param _Host: SIP服务器地址
        :type Host: str
        :param _Port: SIP服务器端口
        :type Port: int
        :param _Serial: SIP服务器编码
        :type Serial: str
        :param _Realm: SIP服务器域
        :type Realm: str
        """
        self._Host = None
        self._Port = None
        self._Serial = None
        self._Realm = None

    @property
    def Host(self):
        """SIP服务器地址
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        """SIP服务器端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Serial(self):
        """SIP服务器编码
        :rtype: str
        """
        return self._Serial

    @Serial.setter
    def Serial(self, Serial):
        self._Serial = Serial

    @property
    def Realm(self):
        """SIP服务器域
        :rtype: str
        """
        return self._Realm

    @Realm.setter
    def Realm(self, Realm):
        self._Realm = Realm


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._Serial = params.get("Serial")
        self._Realm = params.get("Realm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatisticItem(AbstractModel):
    """某天的统计数额

    """

    def __init__(self):
        r"""
        :param _Date: 日期。格式【YYYY-MM-DD】
        :type Date: str
        :param _Sum: 统计数额
        :type Sum: float
        """
        self._Date = None
        self._Sum = None

    @property
    def Date(self):
        """日期。格式【YYYY-MM-DD】
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Sum(self):
        """统计数额
        :rtype: float
        """
        return self._Sum

    @Sum.setter
    def Sum(self, Sum):
        self._Sum = Sum


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._Sum = params.get("Sum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamAddress(AbstractModel):
    """拉流地址，只有在推流情况下才有

    """

    def __init__(self):
        r"""
        :param _StreamId: 流ID
        :type StreamId: str
        :param _RtspAddr: rtsp流地址
        :type RtspAddr: str
        :param _RtmpAddr: rtmp流地址
        :type RtmpAddr: str
        :param _HlsAddr: hls流地址
        :type HlsAddr: str
        :param _FlvAddr: flv流地址
        :type FlvAddr: str
        """
        self._StreamId = None
        self._RtspAddr = None
        self._RtmpAddr = None
        self._HlsAddr = None
        self._FlvAddr = None

    @property
    def StreamId(self):
        """流ID
        :rtype: str
        """
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def RtspAddr(self):
        """rtsp流地址
        :rtype: str
        """
        return self._RtspAddr

    @RtspAddr.setter
    def RtspAddr(self, RtspAddr):
        self._RtspAddr = RtspAddr

    @property
    def RtmpAddr(self):
        """rtmp流地址
        :rtype: str
        """
        return self._RtmpAddr

    @RtmpAddr.setter
    def RtmpAddr(self, RtmpAddr):
        self._RtmpAddr = RtmpAddr

    @property
    def HlsAddr(self):
        """hls流地址
        :rtype: str
        """
        return self._HlsAddr

    @HlsAddr.setter
    def HlsAddr(self, HlsAddr):
        self._HlsAddr = HlsAddr

    @property
    def FlvAddr(self):
        """flv流地址
        :rtype: str
        """
        return self._FlvAddr

    @FlvAddr.setter
    def FlvAddr(self, FlvAddr):
        self._FlvAddr = FlvAddr


    def _deserialize(self, params):
        self._StreamId = params.get("StreamId")
        self._RtspAddr = params.get("RtspAddr")
        self._RtmpAddr = params.get("RtmpAddr")
        self._HlsAddr = params.get("HlsAddr")
        self._FlvAddr = params.get("FlvAddr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeTemplateItem(AbstractModel):
    """时间模板详情

    """

    def __init__(self):
        r"""
        :param _TemplateId: 时间模板ID
        :type TemplateId: str
        :param _Name: 模板名称
        :type Name: str
        :param _IsAllWeek: 是否全时录制，即7*24小时录制 0-否 1-是
        :type IsAllWeek: int
        :param _Type: 是否为自定义模板 0-否 1-是
        :type Type: int
        :param _TimeTemplateSpecs: 时间片段详情
        :type TimeTemplateSpecs: list of TimeTemplateSpec
        """
        self._TemplateId = None
        self._Name = None
        self._IsAllWeek = None
        self._Type = None
        self._TimeTemplateSpecs = None

    @property
    def TemplateId(self):
        """时间模板ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        """模板名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IsAllWeek(self):
        """是否全时录制，即7*24小时录制 0-否 1-是
        :rtype: int
        """
        return self._IsAllWeek

    @IsAllWeek.setter
    def IsAllWeek(self, IsAllWeek):
        self._IsAllWeek = IsAllWeek

    @property
    def Type(self):
        """是否为自定义模板 0-否 1-是
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TimeTemplateSpecs(self):
        """时间片段详情
        :rtype: list of TimeTemplateSpec
        """
        return self._TimeTemplateSpecs

    @TimeTemplateSpecs.setter
    def TimeTemplateSpecs(self, TimeTemplateSpecs):
        self._TimeTemplateSpecs = TimeTemplateSpecs


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Name = params.get("Name")
        self._IsAllWeek = params.get("IsAllWeek")
        self._Type = params.get("Type")
        if params.get("TimeTemplateSpecs") is not None:
            self._TimeTemplateSpecs = []
            for item in params.get("TimeTemplateSpecs"):
                obj = TimeTemplateSpec()
                obj._deserialize(item)
                self._TimeTemplateSpecs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeTemplateSpec(AbstractModel):
    """在操作时间模板时，用于描述各个时间片段

    """

    def __init__(self):
        r"""
        :param _DayofWeek: 一周中的周几
        :type DayofWeek: int
        :param _BeginTime: 时间片段的开始时分。格式【HH:MM】
        :type BeginTime: str
        :param _EndTime: 时间片段的结束时分。格式【HH:MM】
        :type EndTime: str
        """
        self._DayofWeek = None
        self._BeginTime = None
        self._EndTime = None

    @property
    def DayofWeek(self):
        """一周中的周几
        :rtype: int
        """
        return self._DayofWeek

    @DayofWeek.setter
    def DayofWeek(self, DayofWeek):
        self._DayofWeek = DayofWeek

    @property
    def BeginTime(self):
        """时间片段的开始时分。格式【HH:MM】
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """时间片段的结束时分。格式【HH:MM】
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._DayofWeek = params.get("DayofWeek")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceGroupRequest(AbstractModel):
    """UpdateDeviceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 分组名称
        :type GroupName: str
        :param _GroupId: 分组ID
        :type GroupId: str
        :param _GroupDescribe: 分组描述
        :type GroupDescribe: str
        :param _NewParentId: 新父分组ID，用于修改分组路径
        :type NewParentId: str
        """
        self._GroupName = None
        self._GroupId = None
        self._GroupDescribe = None
        self._NewParentId = None

    @property
    def GroupName(self):
        """分组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupId(self):
        """分组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupDescribe(self):
        """分组描述
        :rtype: str
        """
        return self._GroupDescribe

    @GroupDescribe.setter
    def GroupDescribe(self, GroupDescribe):
        self._GroupDescribe = GroupDescribe

    @property
    def NewParentId(self):
        """新父分组ID，用于修改分组路径
        :rtype: str
        """
        return self._NewParentId

    @NewParentId.setter
    def NewParentId(self, NewParentId):
        self._NewParentId = NewParentId


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._GroupId = params.get("GroupId")
        self._GroupDescribe = params.get("GroupDescribe")
        self._NewParentId = params.get("NewParentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceGroupResponse(AbstractModel):
    """UpdateDeviceGroup返回参数结构体

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


class UpdateDevicePassWordRequest(AbstractModel):
    """UpdateDevicePassWord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PassWord: 设备密码
        :type PassWord: str
        :param _DeviceId: 设备唯一标识
        :type DeviceId: str
        """
        self._PassWord = None
        self._DeviceId = None

    @property
    def PassWord(self):
        """设备密码
        :rtype: str
        """
        return self._PassWord

    @PassWord.setter
    def PassWord(self, PassWord):
        self._PassWord = PassWord

    @property
    def DeviceId(self):
        """设备唯一标识
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._PassWord = params.get("PassWord")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDevicePassWordResponse(AbstractModel):
    """UpdateDevicePassWord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 操作结果，“OK”表示成功，其他表示失败。
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """操作结果，“OK”表示成功，其他表示失败。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class UpdateRecordPlanRequest(AbstractModel):
    """UpdateRecordPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 录制计划ID
        :type PlanId: str
        :param _Name: 计划名称
        :type Name: str
        :param _TimeTemplateId: 时间模板ID
        :type TimeTemplateId: str
        :param _EventId: 触发录制的事件 1：全部
        :type EventId: int
        :param _Devices: 录制设备列表
        :type Devices: list of DeviceItem
        :param _IsModifyDevices: 是否更新绑定此录制计划的设备列表
0 - 不更新
1 - 更新，如果Devices参数为空则清空设备列表，Devices不为空则全量更新设备列表
        :type IsModifyDevices: int
        """
        self._PlanId = None
        self._Name = None
        self._TimeTemplateId = None
        self._EventId = None
        self._Devices = None
        self._IsModifyDevices = None

    @property
    def PlanId(self):
        """录制计划ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def Name(self):
        """计划名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TimeTemplateId(self):
        """时间模板ID
        :rtype: str
        """
        return self._TimeTemplateId

    @TimeTemplateId.setter
    def TimeTemplateId(self, TimeTemplateId):
        self._TimeTemplateId = TimeTemplateId

    @property
    def EventId(self):
        """触发录制的事件 1：全部
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Devices(self):
        """录制设备列表
        :rtype: list of DeviceItem
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def IsModifyDevices(self):
        """是否更新绑定此录制计划的设备列表
0 - 不更新
1 - 更新，如果Devices参数为空则清空设备列表，Devices不为空则全量更新设备列表
        :rtype: int
        """
        return self._IsModifyDevices

    @IsModifyDevices.setter
    def IsModifyDevices(self, IsModifyDevices):
        self._IsModifyDevices = IsModifyDevices


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._Name = params.get("Name")
        self._TimeTemplateId = params.get("TimeTemplateId")
        self._EventId = params.get("EventId")
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeviceItem()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._IsModifyDevices = params.get("IsModifyDevices")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordPlanResponse(AbstractModel):
    """UpdateRecordPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 操作结果
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """操作结果
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class UpdateTimeTemplateRequest(AbstractModel):
    """UpdateTimeTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 时间模板ID
        :type TemplateId: str
        :param _Name: 时间模板名称
        :type Name: str
        :param _IsAllWeek: 是否全时录制，即7*24小时录制。
0：非全时录制；1：全时录制。默认1
        :type IsAllWeek: int
        :param _TimeTemplateSpecs: 录制时间片段
        :type TimeTemplateSpecs: list of TimeTemplateSpec
        """
        self._TemplateId = None
        self._Name = None
        self._IsAllWeek = None
        self._TimeTemplateSpecs = None

    @property
    def TemplateId(self):
        """时间模板ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        """时间模板名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IsAllWeek(self):
        """是否全时录制，即7*24小时录制。
0：非全时录制；1：全时录制。默认1
        :rtype: int
        """
        return self._IsAllWeek

    @IsAllWeek.setter
    def IsAllWeek(self, IsAllWeek):
        self._IsAllWeek = IsAllWeek

    @property
    def TimeTemplateSpecs(self):
        """录制时间片段
        :rtype: list of TimeTemplateSpec
        """
        return self._TimeTemplateSpecs

    @TimeTemplateSpecs.setter
    def TimeTemplateSpecs(self, TimeTemplateSpecs):
        self._TimeTemplateSpecs = TimeTemplateSpecs


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Name = params.get("Name")
        self._IsAllWeek = params.get("IsAllWeek")
        if params.get("TimeTemplateSpecs") is not None:
            self._TimeTemplateSpecs = []
            for item in params.get("TimeTemplateSpecs"):
                obj = TimeTemplateSpec()
                obj._deserialize(item)
                self._TimeTemplateSpecs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTimeTemplateResponse(AbstractModel):
    """UpdateTimeTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 操作结果，“OK”表示成功，其他表示失败。
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """操作结果，“OK”表示成功，其他表示失败。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class WarningsData(AbstractModel):
    """告警列表出参

    """

    def __init__(self):
        r"""
        :param _Id: 唯一ID
        :type Id: int
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _WarnChannel: 告警通道
        :type WarnChannel: str
        :param _WarnLevel: 告警级别 1: "一级警情", 2: "二级警情", 3: "三级警情", 4: "四级警情",
        :type WarnLevel: int
        :param _WarnLevelName: 告警级别名称
        :type WarnLevelName: str
        :param _WarnMode: 告警方式 2 设备报警 5 视频报警 6 设备故障报警
        :type WarnMode: int
        :param _WarnModeName: 告警方式名称
        :type WarnModeName: str
        :param _WarnType: 告警类型  2: {
			Name: "设备报警",
			WarnType: map[int]string{
				1: "视频丢失报警",
				2: "设备防拆报警",
				3: "存储设备磁盘满报警",
				4: "设备高温报警",
				5: "设备低温报警",
			},
		},
		5: {
			Name: "视频报警",
			WarnType: map[int]string{
				1:  "人工视频报警",
				2:  "运动目标检测报警",
				3:  "遗留物检测报警",
				4:  "物体移除检测报警",
				5:  "绊线检测报警",
				6:  "入侵检测报警",
				7:  "逆行检测报警",
				8:  "徘徊检测报警",
				9:  "流量统计报警",
				10: "密度检测报警",
				11: "视频异常检测报警",
				12: "快速移动报警",
			},
		},
		6: {
			Name: "设备故障报警",
			WarnType: map[int]string{
				1: "存储设备磁盘故障报警",
				2: "存储设备风扇故障报警",
			},
		}
        :type WarnType: int
        :param _Del: 是否删除
        :type Del: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self._Id = None
        self._DeviceId = None
        self._DeviceName = None
        self._WarnChannel = None
        self._WarnLevel = None
        self._WarnLevelName = None
        self._WarnMode = None
        self._WarnModeName = None
        self._WarnType = None
        self._Del = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Id(self):
        """唯一ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DeviceId(self):
        """设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def WarnChannel(self):
        """告警通道
        :rtype: str
        """
        return self._WarnChannel

    @WarnChannel.setter
    def WarnChannel(self, WarnChannel):
        self._WarnChannel = WarnChannel

    @property
    def WarnLevel(self):
        """告警级别 1: "一级警情", 2: "二级警情", 3: "三级警情", 4: "四级警情",
        :rtype: int
        """
        return self._WarnLevel

    @WarnLevel.setter
    def WarnLevel(self, WarnLevel):
        self._WarnLevel = WarnLevel

    @property
    def WarnLevelName(self):
        """告警级别名称
        :rtype: str
        """
        return self._WarnLevelName

    @WarnLevelName.setter
    def WarnLevelName(self, WarnLevelName):
        self._WarnLevelName = WarnLevelName

    @property
    def WarnMode(self):
        """告警方式 2 设备报警 5 视频报警 6 设备故障报警
        :rtype: int
        """
        return self._WarnMode

    @WarnMode.setter
    def WarnMode(self, WarnMode):
        self._WarnMode = WarnMode

    @property
    def WarnModeName(self):
        """告警方式名称
        :rtype: str
        """
        return self._WarnModeName

    @WarnModeName.setter
    def WarnModeName(self, WarnModeName):
        self._WarnModeName = WarnModeName

    @property
    def WarnType(self):
        """告警类型  2: {
			Name: "设备报警",
			WarnType: map[int]string{
				1: "视频丢失报警",
				2: "设备防拆报警",
				3: "存储设备磁盘满报警",
				4: "设备高温报警",
				5: "设备低温报警",
			},
		},
		5: {
			Name: "视频报警",
			WarnType: map[int]string{
				1:  "人工视频报警",
				2:  "运动目标检测报警",
				3:  "遗留物检测报警",
				4:  "物体移除检测报警",
				5:  "绊线检测报警",
				6:  "入侵检测报警",
				7:  "逆行检测报警",
				8:  "徘徊检测报警",
				9:  "流量统计报警",
				10: "密度检测报警",
				11: "视频异常检测报警",
				12: "快速移动报警",
			},
		},
		6: {
			Name: "设备故障报警",
			WarnType: map[int]string{
				1: "存储设备磁盘故障报警",
				2: "存储设备风扇故障报警",
			},
		}
        :rtype: int
        """
        return self._WarnType

    @WarnType.setter
    def WarnType(self, WarnType):
        self._WarnType = WarnType

    @property
    def Del(self):
        """是否删除
        :rtype: int
        """
        return self._Del

    @Del.setter
    def Del(self, Del):
        self._Del = Del

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._WarnChannel = params.get("WarnChannel")
        self._WarnLevel = params.get("WarnLevel")
        self._WarnLevelName = params.get("WarnLevelName")
        self._WarnMode = params.get("WarnMode")
        self._WarnModeName = params.get("WarnModeName")
        self._WarnType = params.get("WarnType")
        self._Del = params.get("Del")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        