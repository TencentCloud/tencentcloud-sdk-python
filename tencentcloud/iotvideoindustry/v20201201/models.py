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
        :param Date: 对应查询日期
注意：此字段可能返回 null，表示取不到有效值。
        :type Date: str
        :param Info: 列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: list of AbnormalEventsInfo
        """
        self.Date = None
        self.Info = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        if params.get("Info") is not None:
            self.Info = []
            for item in params.get("Info"):
                obj = AbnormalEventsInfo()
                obj._deserialize(item)
                self.Info.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbnormalEventsInfo(AbstractModel):
    """异动事件走势元素

    """

    def __init__(self):
        r"""
        :param Key: 类型值
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: int
        :param Count: 类型总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self.Key = None
        self.Count = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllDeviceInfo(AbstractModel):
    """查询全部设备出参

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param DeviceType: 设备类型；2：IPC
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceType: int
        :param Status: 设备状态；0：设备不在线；1：设备在线；2：设备隔离中；3：设备未注册
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param ExtraInformation: 设备扩展属性
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraInformation: str
        :param NickName: 设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param GroupPath: 设备绑定分组路径
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupPath: str
        :param DeviceCode: 设备编码
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceCode: str
        :param IsRecord: 是否存在录像,，0:不存在；1：存在
注意：此字段可能返回 null，表示取不到有效值。
        :type IsRecord: int
        :param Recordable: 该设备是否可录制
注意：此字段可能返回 null，表示取不到有效值。
        :type Recordable: int
        :param Protocol: 设备接入协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param GroupId: 组Id
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 组名
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        """
        self.DeviceId = None
        self.DeviceType = None
        self.Status = None
        self.CreateTime = None
        self.ExtraInformation = None
        self.NickName = None
        self.GroupPath = None
        self.DeviceCode = None
        self.IsRecord = None
        self.Recordable = None
        self.Protocol = None
        self.GroupId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.DeviceType = params.get("DeviceType")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.ExtraInformation = params.get("ExtraInformation")
        self.NickName = params.get("NickName")
        self.GroupPath = params.get("GroupPath")
        self.DeviceCode = params.get("DeviceCode")
        self.IsRecord = params.get("IsRecord")
        self.Recordable = params.get("Recordable")
        self.Protocol = params.get("Protocol")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindGroupDevicesRequest(AbstractModel):
    """BindGroupDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 分组ID
        :type GroupId: str
        :param DeviceList: 设备唯一标识列表
        :type DeviceList: list of str
        """
        self.GroupId = None
        self.DeviceList = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.DeviceList = params.get("DeviceList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindGroupDevicesResponse(AbstractModel):
    """BindGroupDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ChannelDetail(AbstractModel):
    """国标通道详细信息

    """

    def __init__(self):
        r"""
        :param ChannelName: 通道名称
        :type ChannelName: str
        :param ChannelId: 通道唯一标识
        :type ChannelId: str
        :param ChannelType: 通道类型 0：未知；1：视频通道；2：音频通道；3：告警通道
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelType: int
        :param ChannelCode: 20位国标通道编码
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelCode: str
        :param ExtraInformation: 通道扩展信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraInformation: str
        :param Status: 通道在线状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param IsRecord: 通道是否存在录像标识 0：无录像；1：有录像
注意：此字段可能返回 null，表示取不到有效值。
        :type IsRecord: int
        :param DeviceId: 通道所属设备唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param BusinessGroupId: 通道所属虚拟组织的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessGroupId: str
        """
        self.ChannelName = None
        self.ChannelId = None
        self.ChannelType = None
        self.ChannelCode = None
        self.ExtraInformation = None
        self.Status = None
        self.IsRecord = None
        self.DeviceId = None
        self.BusinessGroupId = None


    def _deserialize(self, params):
        self.ChannelName = params.get("ChannelName")
        self.ChannelId = params.get("ChannelId")
        self.ChannelType = params.get("ChannelType")
        self.ChannelCode = params.get("ChannelCode")
        self.ExtraInformation = params.get("ExtraInformation")
        self.Status = params.get("Status")
        self.IsRecord = params.get("IsRecord")
        self.DeviceId = params.get("DeviceId")
        self.BusinessGroupId = params.get("BusinessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelItem(AbstractModel):
    """GB28181通道

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param ChannelId: 通道唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelId: str
        """
        self.DeviceId = None
        self.ChannelId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlChannelLocalRecordRequest(AbstractModel):
    """ControlChannelLocalRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        :param ChannelId: 通道唯一标识
        :type ChannelId: str
        :param StreamId: 流Id，流的唯一标识
        :type StreamId: str
        :param Command: 控制参数，转义的json字符串

目前支持的command：
"Command": "{"Action":"PAUSE"}" 暂停
"Command": "{"Action":"PLAY"}" 暂停恢复
"Command": "{"Action":"PLAY","Offset":"15"}" 基于文件起始时间点的位置偏移，单位秒
        :type Command: str
        """
        self.DeviceId = None
        self.ChannelId = None
        self.StreamId = None
        self.Command = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ChannelId = params.get("ChannelId")
        self.StreamId = params.get("StreamId")
        self.Command = params.get("Command")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlChannelLocalRecordResponse(AbstractModel):
    """ControlChannelLocalRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ControlChannelPTZRequest(AbstractModel):
    """ControlChannelPTZ请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        :param ChannelId: 通道唯一标识
        :type ChannelId: str
        :param Command: PTZ控制命令类型：
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
        self.DeviceId = None
        self.ChannelId = None
        self.Command = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ChannelId = params.get("ChannelId")
        self.Command = params.get("Command")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlChannelPTZResponse(AbstractModel):
    """ControlChannelPTZ返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ControlDevicePTZRequest(AbstractModel):
    """ControlDevicePTZ请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        :param Command: PTZ控制命令类型：
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
        :param ChannelId: 通道唯一标识
        :type ChannelId: str
        """
        self.DeviceId = None
        self.Command = None
        self.ChannelId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.Command = params.get("Command")
        self.ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDevicePTZResponse(AbstractModel):
    """ControlDevicePTZ返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ControlHomePositionRequest(AbstractModel):
    """ControlHomePosition请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelId: 通道ID
        :type ChannelId: str
        :param DeviceId: 设备Id
        :type DeviceId: str
        :param Enable: 看守位使能 0-停用看守位 1-启用看守位
        :type Enable: int
        :param PresetId: 预置位编码 范围1-8，启用看守位时必填
        :type PresetId: int
        :param ResetTime: 看守位自动归位时间， 启用看守位时必填
        :type ResetTime: int
        """
        self.ChannelId = None
        self.DeviceId = None
        self.Enable = None
        self.PresetId = None
        self.ResetTime = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        self.DeviceId = params.get("DeviceId")
        self.Enable = params.get("Enable")
        self.PresetId = params.get("PresetId")
        self.ResetTime = params.get("ResetTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlHomePositionResponse(AbstractModel):
    """ControlHomePosition返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ControlPresetRequest(AbstractModel):
    """ControlPreset请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelId: 通道ID
        :type ChannelId: str
        :param Command: 控制命令：
Set-设置当前位置为预置位
Del-删除指定的预置位
Call-调用指定的预置位
        :type Command: str
        :param PresetId: 预置位编码 范围1-8
        :type PresetId: int
        :param DeviceId: 设备Id
        :type DeviceId: str
        """
        self.ChannelId = None
        self.Command = None
        self.PresetId = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        self.Command = params.get("Command")
        self.PresetId = params.get("PresetId")
        self.DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlPresetResponse(AbstractModel):
    """ControlPreset返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ControlRecordStreamRequest(AbstractModel):
    """ControlRecordStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备Id，设备的唯一标识
        :type DeviceId: str
        :param StreamId: 流Id，流的唯一标识
        :type StreamId: str
        :param Command: |控制参数，CmdJson结构转义的json字符串。| Action  | string  |是|控制动作，play(用于暂停后恢复播放)、pause（暂停）、teardown(停止)、jump(拖动播放)
| Offset  | uint  |否|拖动播放时的时间偏移量（相对于起始时间）,单位：秒
目前支持的command：
"Command": "{"Action":"PAUSE"}" 暂停
"Command": "{"Action":"PLAY"}" 暂停恢复
"Command": "{"Action":"PLAY","Offset":"15"}" 位置偏移，可以替代jump操作
        :type Command: str
        :param ChannelId: 通道唯一标识
        :type ChannelId: str
        """
        self.DeviceId = None
        self.StreamId = None
        self.Command = None
        self.ChannelId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.StreamId = params.get("StreamId")
        self.Command = params.get("Command")
        self.ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlRecordStreamResponse(AbstractModel):
    """ControlRecordStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDeviceGroupRequest(AbstractModel):
    """CreateDeviceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupName: 分组名称
        :type GroupName: str
        :param ParentId: 父分组ID
        :type ParentId: str
        :param GroupDescribe: 分组描述
        :type GroupDescribe: str
        """
        self.GroupName = None
        self.ParentId = None
        self.GroupDescribe = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.ParentId = params.get("ParentId")
        self.GroupDescribe = params.get("GroupDescribe")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceGroupResponse(AbstractModel):
    """CreateDeviceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 响应结果，“OK”为成功，其他为失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param GroupId: 分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreateDeviceRequest(AbstractModel):
    """CreateDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param NickName: 设备名称
        :type NickName: str
        :param PassWord: 设备密码
        :type PassWord: str
        :param DeviceType: 设备类型，1：国标VMS设备(公有云不支持此类型)，2：国标IPC设备，3：国标NVR设备，9：智能告警设备(公有云不支持此类型)
        :type DeviceType: int
        :param GroupId: 设备需要绑定的分组ID，参数为空则默认绑定到根分组
        :type GroupId: str
        """
        self.NickName = None
        self.PassWord = None
        self.DeviceType = None
        self.GroupId = None


    def _deserialize(self, params):
        self.NickName = params.get("NickName")
        self.PassWord = params.get("PassWord")
        self.DeviceType = params.get("DeviceType")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceResponse(AbstractModel):
    """CreateDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceCode: 设备编码
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceCode: str
        :param DeviceId: 设备唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param VirtualGroupId: 设备虚拟组信息，仅在创建NVR时返回该值
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualGroupId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceCode = None
        self.DeviceId = None
        self.VirtualGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceCode = params.get("DeviceCode")
        self.DeviceId = params.get("DeviceId")
        self.VirtualGroupId = params.get("VirtualGroupId")
        self.RequestId = params.get("RequestId")


class CreateLiveChannelRequest(AbstractModel):
    """CreateLiveChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param LiveChannelName: 直播频道名称
        :type LiveChannelName: str
        :param LiveChannelType: 直播频道类型 1：固定直播；2：移动直播
        :type LiveChannelType: int
        """
        self.LiveChannelName = None
        self.LiveChannelType = None


    def _deserialize(self, params):
        self.LiveChannelName = params.get("LiveChannelName")
        self.LiveChannelType = params.get("LiveChannelType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveChannelResponse(AbstractModel):
    """CreateLiveChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param LiveChannelId: 直播频道ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveChannelId: str
        :param PushStreamAddress: 直播频道推流地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PushStreamAddress: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LiveChannelId = None
        self.PushStreamAddress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LiveChannelId = params.get("LiveChannelId")
        self.PushStreamAddress = params.get("PushStreamAddress")
        self.RequestId = params.get("RequestId")


class CreateLiveRecordPlanRequest(AbstractModel):
    """CreateLiveRecordPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param PlanName: 录制计划名
        :type PlanName: str
        :param PlanType: 计划类型 1：固定直播 2：移动直播
        :type PlanType: int
        :param TemplateId: 时间模板ID,固定直播时为必填
        :type TemplateId: str
        :param RecordStorageTime: 录制文件存储时长，单位天，默认30天
        :type RecordStorageTime: int
        :param LiveChannelIds: 绑定的直播频道ID列表
        :type LiveChannelIds: list of str
        """
        self.PlanName = None
        self.PlanType = None
        self.TemplateId = None
        self.RecordStorageTime = None
        self.LiveChannelIds = None


    def _deserialize(self, params):
        self.PlanName = params.get("PlanName")
        self.PlanType = params.get("PlanType")
        self.TemplateId = params.get("TemplateId")
        self.RecordStorageTime = params.get("RecordStorageTime")
        self.LiveChannelIds = params.get("LiveChannelIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveRecordPlanResponse(AbstractModel):
    """CreateLiveRecordPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param PlanId: 录制计划名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PlanId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PlanId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        self.RequestId = params.get("RequestId")


class CreateMessageForwardRequest(AbstractModel):
    """CreateMessageForward请求参数结构体

    """

    def __init__(self):
        r"""
        :param RegionId: 区域ID
        :type RegionId: str
        :param RegionName: 区域名称
        :type RegionName: str
        :param Instance: 实例ID
        :type Instance: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param MessageType: json数组， 转发类型 1: 告警 2:GPS
        :type MessageType: str
        :param TopicId: kafka topic id
        :type TopicId: str
        :param TopicName: kafka topic 名称
        :type TopicName: str
        """
        self.RegionId = None
        self.RegionName = None
        self.Instance = None
        self.InstanceName = None
        self.MessageType = None
        self.TopicId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.Instance = params.get("Instance")
        self.InstanceName = params.get("InstanceName")
        self.MessageType = params.get("MessageType")
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMessageForwardResponse(AbstractModel):
    """CreateMessageForward返回参数结构体

    """

    def __init__(self):
        r"""
        :param IntId: 配置ID
注意：此字段可能返回 null，表示取不到有效值。
        :type IntId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IntId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IntId = params.get("IntId")
        self.RequestId = params.get("RequestId")


class CreateRecordPlanRequest(AbstractModel):
    """CreateRecordPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 计划名称
        :type Name: str
        :param TimeTemplateId: 时间模板ID
        :type TimeTemplateId: str
        :param EventId: 触发录制的事件类别 1:全部
        :type EventId: int
        :param Devices: 该录制计划绑定的设备列表
        :type Devices: list of DeviceItem
        :param RecordStorageTime: 存储周期
        :type RecordStorageTime: int
        """
        self.Name = None
        self.TimeTemplateId = None
        self.EventId = None
        self.Devices = None
        self.RecordStorageTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TimeTemplateId = params.get("TimeTemplateId")
        self.EventId = params.get("EventId")
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceItem()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.RecordStorageTime = params.get("RecordStorageTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordPlanResponse(AbstractModel):
    """CreateRecordPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param PlanId: 录制计划ID
        :type PlanId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PlanId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        self.RequestId = params.get("RequestId")


class CreateRecordingPlanRequest(AbstractModel):
    """CreateRecordingPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 计划名称
        :type Name: str
        :param TimeTemplateId: 时间模板ID
        :type TimeTemplateId: str
        :param Channels: 该录制计划绑定的通道列表
        :type Channels: list of ChannelItem
        :param RecordStorageTime: 存储周期(天)；默认存储30天
        :type RecordStorageTime: int
        """
        self.Name = None
        self.TimeTemplateId = None
        self.Channels = None
        self.RecordStorageTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TimeTemplateId = params.get("TimeTemplateId")
        if params.get("Channels") is not None:
            self.Channels = []
            for item in params.get("Channels"):
                obj = ChannelItem()
                obj._deserialize(item)
                self.Channels.append(obj)
        self.RecordStorageTime = params.get("RecordStorageTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordingPlanResponse(AbstractModel):
    """CreateRecordingPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param PlanId: 录制计划ID
        :type PlanId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PlanId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        self.RequestId = params.get("RequestId")


class CreateSceneRequest(AbstractModel):
    """CreateScene请求参数结构体

    """

    def __init__(self):
        r"""
        :param SceneName: 场景名称
        :type SceneName: str
        :param SceneTrigger: 场景触发规则
        :type SceneTrigger: str
        :param RecordDuration: 录制时长 (秒)
        :type RecordDuration: int
        :param StoreDuration: 录像存储时长(天)
        :type StoreDuration: int
        :param Devices: 设备列表(不推荐使用)
        :type Devices: list of DeviceItem
        :param Channels: 通道列表
        :type Channels: list of ChannelItem
        """
        self.SceneName = None
        self.SceneTrigger = None
        self.RecordDuration = None
        self.StoreDuration = None
        self.Devices = None
        self.Channels = None


    def _deserialize(self, params):
        self.SceneName = params.get("SceneName")
        self.SceneTrigger = params.get("SceneTrigger")
        self.RecordDuration = params.get("RecordDuration")
        self.StoreDuration = params.get("StoreDuration")
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceItem()
                obj._deserialize(item)
                self.Devices.append(obj)
        if params.get("Channels") is not None:
            self.Channels = []
            for item in params.get("Channels"):
                obj = ChannelItem()
                obj._deserialize(item)
                self.Channels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSceneResponse(AbstractModel):
    """CreateScene返回参数结构体

    """

    def __init__(self):
        r"""
        :param IntId: 场景ID
注意：此字段可能返回 null，表示取不到有效值。
        :type IntId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IntId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IntId = params.get("IntId")
        self.RequestId = params.get("RequestId")


class CreateTimeTemplateRequest(AbstractModel):
    """CreateTimeTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 时间模板名称
        :type Name: str
        :param IsAllWeek: 是否为每周全时录制（即7*24h录制），0：非全时录制，1；全时录制，默认0
        :type IsAllWeek: int
        :param TimeTemplateSpecs: 当IsAllWeek为0时必选，用于描述模板的各个时间片段
        :type TimeTemplateSpecs: list of TimeTemplateSpec
        """
        self.Name = None
        self.IsAllWeek = None
        self.TimeTemplateSpecs = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.IsAllWeek = params.get("IsAllWeek")
        if params.get("TimeTemplateSpecs") is not None:
            self.TimeTemplateSpecs = []
            for item in params.get("TimeTemplateSpecs"):
                obj = TimeTemplateSpec()
                obj._deserialize(item)
                self.TimeTemplateSpecs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTimeTemplateResponse(AbstractModel):
    """CreateTimeTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 时间模板ID
        :type TemplateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class DeleteChannelRequest(AbstractModel):
    """DeleteChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备ID
        :type DeviceId: str
        :param ChannelId: 通道ID
        :type ChannelId: str
        """
        self.DeviceId = None
        self.ChannelId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteChannelResponse(AbstractModel):
    """DeleteChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDeviceGroupRequest(AbstractModel):
    """DeleteDeviceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 分组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceGroupResponse(AbstractModel):
    """DeleteDeviceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 响应结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        """
        self.DeviceId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 操作结果 OK-成功； 其他-失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DeleteLiveChannelRequest(AbstractModel):
    """DeleteLiveChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param LiveChannelId: 直播频道ID
        :type LiveChannelId: str
        """
        self.LiveChannelId = None


    def _deserialize(self, params):
        self.LiveChannelId = params.get("LiveChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveChannelResponse(AbstractModel):
    """DeleteLiveChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveRecordPlanRequest(AbstractModel):
    """DeleteLiveRecordPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param PlanId: 录制计划ID
        :type PlanId: str
        """
        self.PlanId = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveRecordPlanResponse(AbstractModel):
    """DeleteLiveRecordPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 删除状态描述
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DeleteLiveVideoListRequest(AbstractModel):
    """DeleteLiveVideoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param IntIDs: 视频ID 列表, 大小限制(100)
        :type IntIDs: list of int non-negative
        """
        self.IntIDs = None


    def _deserialize(self, params):
        self.IntIDs = params.get("IntIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveVideoListResponse(AbstractModel):
    """DeleteLiveVideoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMessageForwardRequest(AbstractModel):
    """DeleteMessageForward请求参数结构体

    """

    def __init__(self):
        r"""
        :param IntId: 配置ID
        :type IntId: int
        """
        self.IntId = None


    def _deserialize(self, params):
        self.IntId = params.get("IntId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMessageForwardResponse(AbstractModel):
    """DeleteMessageForward返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRecordPlanRequest(AbstractModel):
    """DeleteRecordPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param PlanId: 录制计划ID
        :type PlanId: str
        """
        self.PlanId = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordPlanResponse(AbstractModel):
    """DeleteRecordPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 操作结果，OK：成功，其他：失败
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DeleteRecordingPlanRequest(AbstractModel):
    """DeleteRecordingPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param PlanId: 录制计划ID
        :type PlanId: str
        """
        self.PlanId = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordingPlanResponse(AbstractModel):
    """DeleteRecordingPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 操作结果，OK：成功，其他：失败
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DeleteSceneRequest(AbstractModel):
    """DeleteScene请求参数结构体

    """

    def __init__(self):
        r"""
        :param IntId: 场景ID
        :type IntId: int
        """
        self.IntId = None


    def _deserialize(self, params):
        self.IntId = params.get("IntId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSceneResponse(AbstractModel):
    """DeleteScene返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTimeTemplateRequest(AbstractModel):
    """DeleteTimeTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 时间模板ID
        :type TemplateId: str
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTimeTemplateResponse(AbstractModel):
    """DeleteTimeTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 操作结果，OK：成功，其他：失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DeleteVideoListRequest(AbstractModel):
    """DeleteVideoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InitIDs: 视频ID列表长度限制100内
        :type InitIDs: list of int
        """
        self.InitIDs = None


    def _deserialize(self, params):
        self.InitIDs = params.get("InitIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVideoListResponse(AbstractModel):
    """DeleteVideoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWarningRequest(AbstractModel):
    """DeleteWarning请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 告警ID
        :type Id: int
        :param Index: 告警索引
        :type Index: str
        """
        self.Id = None
        self.Index = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWarningResponse(AbstractModel):
    """DeleteWarning返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAbnormalEventsRequest(AbstractModel):
    """DescribeAbnormalEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param EndTime: 结束时间
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
        


class DescribeAbnormalEventsResponse(AbstractModel):
    """DescribeAbnormalEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 异动事件走势列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of AbnormalEvents
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = AbnormalEvents()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAllDeviceListRequest(AbstractModel):
    """DescribeAllDeviceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认0
        :type Offset: int
        :param Limit: 限制，默认200
        :type Limit: int
        :param NickName: 设备名称，需要模糊匹配设备名称时为必填
        :type NickName: str
        :param DeviceIds: DeviceId列表，需要精确查找设备时为必填
        :type DeviceIds: list of str
        :param DeviceTypes: 设备类型过滤，设备类型，1：国标VMS设备(公有云不支持此类型)，2：国标IPC设备，3：国标NVR设备，9：智能告警设备(公有云不支持此类型)
        :type DeviceTypes: list of int
        """
        self.Offset = None
        self.Limit = None
        self.NickName = None
        self.DeviceIds = None
        self.DeviceTypes = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NickName = params.get("NickName")
        self.DeviceIds = params.get("DeviceIds")
        self.DeviceTypes = params.get("DeviceTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllDeviceListResponse(AbstractModel):
    """DescribeAllDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Devices: 设备详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Devices: list of AllDeviceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Devices = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = AllDeviceInfo()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBindSceneChannelsRequest(AbstractModel):
    """DescribeBindSceneChannels请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 条数限制最大不能超过1000
        :type Limit: int
        :param SceneId: 场景ID
        :type SceneId: int
        :param Offset: 偏移值
        :type Offset: int
        """
        self.Limit = None
        self.SceneId = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.SceneId = params.get("SceneId")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindSceneChannelsResponse(AbstractModel):
    """DescribeBindSceneChannels返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param List: 通道列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of ChannelItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ChannelItem()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBindSceneDevicesRequest(AbstractModel):
    """DescribeBindSceneDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param SceneId: 场景ID
        :type SceneId: int
        :param Offset: 偏移值
        :type Offset: int
        :param Limit: 条数限制最大不能超过1000
        :type Limit: int
        """
        self.SceneId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SceneId = params.get("SceneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindSceneDevicesResponse(AbstractModel):
    """DescribeBindSceneDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param List: 设备列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DeviceItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = DeviceItem()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeChannelLiveStreamURLRequest(AbstractModel):
    """DescribeChannelLiveStreamURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识，必填参数
        :type DeviceId: str
        :param ChannelId: 通道唯一标识（接口升级字段为必填），必填参数
        :type ChannelId: str
        """
        self.DeviceId = None
        self.ChannelId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChannelLiveStreamURLResponse(AbstractModel):
    """DescribeChannelLiveStreamURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 设备实时流地址列表
        :type Data: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceStreamsData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeDeviceStreamsData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeChannelLocalRecordURLRequest(AbstractModel):
    """DescribeChannelLocalRecordURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        :param ChannelId: 通道唯一标识
        :type ChannelId: str
        :param RecordId: 录像文件Id，通过获取本地录像返回
        :type RecordId: str
        :param ExpireTime: UNIX 时间戳，30天内，URL失效时间，如180s无人观看此流则URL提前失效
        :type ExpireTime: int
        :param StartTime: 录像文件推送的开始时间，需要在RecordId参数起始时间内，可以通过此参数控制回放流起始点
        :type StartTime: int
        :param EndTime: 录像文件推送的结束时间，需要在RecordId参数起始时间内，可以通过此参数控制回放流起始点
        :type EndTime: int
        """
        self.DeviceId = None
        self.ChannelId = None
        self.RecordId = None
        self.ExpireTime = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ChannelId = params.get("ChannelId")
        self.RecordId = params.get("RecordId")
        self.ExpireTime = params.get("ExpireTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChannelLocalRecordURLResponse(AbstractModel):
    """DescribeChannelLocalRecordURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 结果
        :type Data: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeRecordStreamData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeRecordStreamData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeChannelStreamURLRequest(AbstractModel):
    """DescribeChannelStreamURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识，必填参数
        :type DeviceId: str
        :param ExpireTime: 流地址失效时间，固定值填写0，其他参数无效，必填参数
        :type ExpireTime: int
        :param ChannelId: 通道唯一标识（接口升级字段为必填），必填参数
        :type ChannelId: str
        """
        self.DeviceId = None
        self.ExpireTime = None
        self.ChannelId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ExpireTime = params.get("ExpireTime")
        self.ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChannelStreamURLResponse(AbstractModel):
    """DescribeChannelStreamURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 设备实时流地址列表
        :type Data: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceStreamsData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeDeviceStreamsData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeChannelsByLiveRecordPlanRequest(AbstractModel):
    """DescribeChannelsByLiveRecordPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param PlanId: 录制计划ID
        :type PlanId: str
        :param Offset: 分页偏移量
        :type Offset: int
        :param Limit: 分页大小
        :type Limit: int
        """
        self.PlanId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChannelsByLiveRecordPlanResponse(AbstractModel):
    """DescribeChannelsByLiveRecordPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param LiveChannels: 通道详情数组
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveChannels: list of LiveChannelItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.LiveChannels = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LiveChannels") is not None:
            self.LiveChannels = []
            for item in params.get("LiveChannels"):
                obj = LiveChannelItem()
                obj._deserialize(item)
                self.LiveChannels.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeChannelsRequest(AbstractModel):
    """DescribeChannels请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备Id
        :type DeviceId: str
        :param Limit: 限制，默认0
        :type Limit: int
        :param Offset: 偏移量，默认0
        :type Offset: int
        :param ChannelTypes: 通道类型  0: 未知类型 1: 视频通道 2:  音频通道 3: 告警通道
        :type ChannelTypes: list of int non-negative
        :param PlanId: 录制计划ID， 当为"null"值时未绑定录制计划
        :type PlanId: str
        :param SceneId: 告警联动场景ID， 当为 -1 值时未绑定场景
        :type SceneId: int
        """
        self.DeviceId = None
        self.Limit = None
        self.Offset = None
        self.ChannelTypes = None
        self.PlanId = None
        self.SceneId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ChannelTypes = params.get("ChannelTypes")
        self.PlanId = params.get("PlanId")
        self.SceneId = params.get("SceneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChannelsResponse(AbstractModel):
    """DescribeChannels返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 通道总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Channels: 通道详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Channels: list of ChannelDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Channels = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Channels") is not None:
            self.Channels = []
            for item in params.get("Channels"):
                obj = ChannelDetail()
                obj._deserialize(item)
                self.Channels.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCurrentDeviceDataRequest(AbstractModel):
    """DescribeCurrentDeviceData请求参数结构体

    """


class DescribeCurrentDeviceDataResponse(AbstractModel):
    """DescribeCurrentDeviceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Channels: 通道数
        :type Channels: int
        :param Devices: 设备数
        :type Devices: int
        :param OnlineChannels: 在线通道数
        :type OnlineChannels: int
        :param OnlineDevices: 在线设备数
        :type OnlineDevices: int
        :param RecordingChannels: 正在录制通道数
        :type RecordingChannels: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Channels = None
        self.Devices = None
        self.OnlineChannels = None
        self.OnlineDevices = None
        self.RecordingChannels = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Channels = params.get("Channels")
        self.Devices = params.get("Devices")
        self.OnlineChannels = params.get("OnlineChannels")
        self.OnlineDevices = params.get("OnlineDevices")
        self.RecordingChannels = params.get("RecordingChannels")
        self.RequestId = params.get("RequestId")


class DescribeDeviceEventRequest(AbstractModel):
    """DescribeDeviceEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间，秒级时间戳
        :type StartTime: int
        :param EndTime: 结束时间，秒级时间戳
        :type EndTime: int
        :param DeviceId: 设备Id
        :type DeviceId: str
        :param EventTypes: 事件类型 1:注册 2:心跳 4:录制异常 5:播放异常 6:流中断
        :type EventTypes: list of int
        :param Offset: 偏移值
        :type Offset: int
        :param Limit: limit限制值
        :type Limit: int
        """
        self.StartTime = None
        self.EndTime = None
        self.DeviceId = None
        self.EventTypes = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.DeviceId = params.get("DeviceId")
        self.EventTypes = params.get("EventTypes")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceEventResponse(AbstractModel):
    """DescribeDeviceEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Events: 事件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Events: list of Events
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Events = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = Events()
                obj._deserialize(item)
                self.Events.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceGroupRequest(AbstractModel):
    """DescribeDeviceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceIds: 设备唯一标识列表
        :type DeviceIds: list of str
        """
        self.DeviceIds = None


    def _deserialize(self, params):
        self.DeviceIds = params.get("DeviceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceGroupResponse(AbstractModel):
    """DescribeDeviceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param DevGroups: 设备所在分组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DevGroups: list of DevGroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DevGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DevGroups") is not None:
            self.DevGroups = []
            for item in params.get("DevGroups"):
                obj = DevGroupInfo()
                obj._deserialize(item)
                self.DevGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceListRequest(AbstractModel):
    """DescribeDeviceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认0
        :type Offset: int
        :param Limit: 限制，默认200
        :type Limit: int
        :param NickName: 设备名前缀
        :type NickName: str
        :param DeviceTypes: 设备类型，1：国标VMS设备(公有云不支持此类型)，2：国标IPC设备，3：国标NVR设备，9：智能告警设备(公有云不支持此类型)
        :type DeviceTypes: list of int
        """
        self.Offset = None
        self.Limit = None
        self.NickName = None
        self.DeviceTypes = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NickName = params.get("NickName")
        self.DeviceTypes = params.get("DeviceTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceListResponse(AbstractModel):
    """DescribeDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Devices: 设备详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Devices: list of AllDeviceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Devices = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = AllDeviceInfo()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceMonitorDataRequest(AbstractModel):
    """DescribeDeviceMonitorData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间戳
        :type StartTime: int
        :param EndTime: 结束时间戳
        :type EndTime: int
        :param Type: 类型 支持 OnlineChannels/OnlineDevices/RecordingChannels
        :type Type: str
        :param TimesSpec: 时间粒度 目前只支持 1h
        :type TimesSpec: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Type = None
        self.TimesSpec = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Type = params.get("Type")
        self.TimesSpec = params.get("TimesSpec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceMonitorDataResponse(AbstractModel):
    """DescribeDeviceMonitorData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 查询设备统计monitor信息列表
        :type Data: list of DeviceMonitorValue
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DeviceMonitorValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDevicePassWordRequest(AbstractModel):
    """DescribeDevicePassWord请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        """
        self.DeviceId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicePassWordResponse(AbstractModel):
    """DescribeDevicePassWord返回参数结构体

    """

    def __init__(self):
        r"""
        :param PassWord: 设备密码
        :type PassWord: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PassWord = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PassWord = params.get("PassWord")
        self.RequestId = params.get("RequestId")


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备ID
        :type DeviceId: str
        """
        self.DeviceId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param Device: 设备详情信息
        :type Device: :class:`tencentcloud.iotvideoindustry.v20201201.models.AllDeviceInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Device = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Device") is not None:
            self.Device = AllDeviceInfo()
            self.Device._deserialize(params.get("Device"))
        self.RequestId = params.get("RequestId")


class DescribeDeviceStreamsData(AbstractModel):
    """DescribeDeviceStreams的出参复杂类型

    """

    def __init__(self):
        r"""
        :param RtspAddr: rtsp地址
        :type RtspAddr: str
        :param RtmpAddr: rtmp地址
        :type RtmpAddr: str
        :param HlsAddr: hls地址
        :type HlsAddr: str
        :param FlvAddr: flv地址
        :type FlvAddr: str
        """
        self.RtspAddr = None
        self.RtmpAddr = None
        self.HlsAddr = None
        self.FlvAddr = None


    def _deserialize(self, params):
        self.RtspAddr = params.get("RtspAddr")
        self.RtmpAddr = params.get("RtmpAddr")
        self.HlsAddr = params.get("HlsAddr")
        self.FlvAddr = params.get("FlvAddr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceStreamsRequest(AbstractModel):
    """DescribeDeviceStreams请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        :param ExpireTime: 流地址失效时间
        :type ExpireTime: int
        :param ChannelId: 通道唯一标识（接口升级字段为必填）
        :type ChannelId: str
        """
        self.DeviceId = None
        self.ExpireTime = None
        self.ChannelId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ExpireTime = params.get("ExpireTime")
        self.ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceStreamsResponse(AbstractModel):
    """DescribeDeviceStreams返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 设备实时流地址列表
        :type Data: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceStreamsData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeDeviceStreamsData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeGroupByIdRequest(AbstractModel):
    """DescribeGroupById请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 分组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupByIdResponse(AbstractModel):
    """DescribeGroupById返回参数结构体

    """

    def __init__(self):
        r"""
        :param Group: 分组信息详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Group: :class:`tencentcloud.iotvideoindustry.v20201201.models.GroupItem`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Group = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Group") is not None:
            self.Group = GroupItem()
            self.Group._deserialize(params.get("Group"))
        self.RequestId = params.get("RequestId")


class DescribeGroupByPathRequest(AbstractModel):
    """DescribeGroupByPath请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupPath: 分组路径，格式为/aaa(/bbb/ccc)
        :type GroupPath: str
        """
        self.GroupPath = None


    def _deserialize(self, params):
        self.GroupPath = params.get("GroupPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupByPathResponse(AbstractModel):
    """DescribeGroupByPath返回参数结构体

    """

    def __init__(self):
        r"""
        :param Group: 分组信息详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Group: :class:`tencentcloud.iotvideoindustry.v20201201.models.GroupItem`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Group = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Group") is not None:
            self.Group = GroupItem()
            self.Group._deserialize(params.get("Group"))
        self.RequestId = params.get("RequestId")


class DescribeGroupDevicesRequest(AbstractModel):
    """DescribeGroupDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 分组ID
        :type GroupId: str
        :param Offset: 偏移量，默认0
        :type Offset: int
        :param Limit: 限制值，默认200
        :type Limit: int
        :param NickName: 设备名称，根据设备名称模糊匹配时必填
        :type NickName: str
        :param Recordable: 过滤不可录制设备
        :type Recordable: int
        :param DeviceTypes: 当Group是普通组的时候，支持根据DeviceTypes筛选类型，
 设备类型，1：国标VMS设备(公有云不支持此类型)，2：国标IPC设备，3：国标NVR设备，9：智能告警设备(公有云不支持此类型)
        :type DeviceTypes: list of int
        """
        self.GroupId = None
        self.Offset = None
        self.Limit = None
        self.NickName = None
        self.Recordable = None
        self.DeviceTypes = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NickName = params.get("NickName")
        self.Recordable = params.get("Recordable")
        self.DeviceTypes = params.get("DeviceTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupDevicesResponse(AbstractModel):
    """DescribeGroupDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 分组绑定的设备数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param DeviceList: 设备详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceList: list of GroupDeviceItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DeviceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DeviceList") is not None:
            self.DeviceList = []
            for item in params.get("DeviceList"):
                obj = GroupDeviceItem()
                obj._deserialize(item)
                self.DeviceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGroupsRequest(AbstractModel):
    """DescribeGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupIds: 分组ID列表
        :type GroupIds: list of str
        """
        self.GroupIds = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupsResponse(AbstractModel):
    """DescribeGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param Groups: 分组详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Groups: list of GroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Groups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIPCChannelsRequest(AbstractModel):
    """DescribeIPCChannels请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认0
        :type Offset: int
        :param Limit: 限制，默认0
        :type Limit: int
        :param DeviceId: 设备Id
        :type DeviceId: str
        :param ChannelTypes: 通道类型  0: 未知类型 1: 视频通道 2:  音频通道 3: 告警通道
        :type ChannelTypes: list of int non-negative
        """
        self.Offset = None
        self.Limit = None
        self.DeviceId = None
        self.ChannelTypes = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DeviceId = params.get("DeviceId")
        self.ChannelTypes = params.get("ChannelTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPCChannelsResponse(AbstractModel):
    """DescribeIPCChannels返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 通道总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param DeviceList: 通道详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceList: list of GroupDeviceItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DeviceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DeviceList") is not None:
            self.DeviceList = []
            for item in params.get("DeviceList"):
                obj = GroupDeviceItem()
                obj._deserialize(item)
                self.DeviceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveChannelListRequest(AbstractModel):
    """DescribeLiveChannelList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 最大数
        :type Limit: int
        :param LiveChannelType: 直播频道类型，1：固定直播；2：移动直播
        :type LiveChannelType: int
        :param RecordPlanId: 直播录制计划ID, null: 直播录制计划为空
        :type RecordPlanId: str
        :param LiveChannelName: 频道名称 (支持模糊搜索)
        :type LiveChannelName: str
        """
        self.Offset = None
        self.Limit = None
        self.LiveChannelType = None
        self.RecordPlanId = None
        self.LiveChannelName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.LiveChannelType = params.get("LiveChannelType")
        self.RecordPlanId = params.get("RecordPlanId")
        self.LiveChannelName = params.get("LiveChannelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveChannelListResponse(AbstractModel):
    """DescribeLiveChannelList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 频道总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param LiveChannels: 频道信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveChannels: list of LiveChannelInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.LiveChannels = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("LiveChannels") is not None:
            self.LiveChannels = []
            for item in params.get("LiveChannels"):
                obj = LiveChannelInfo()
                obj._deserialize(item)
                self.LiveChannels.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveChannelRequest(AbstractModel):
    """DescribeLiveChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param LiveChannelId: 频道ID
        :type LiveChannelId: str
        """
        self.LiveChannelId = None


    def _deserialize(self, params):
        self.LiveChannelId = params.get("LiveChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveChannelResponse(AbstractModel):
    """DescribeLiveChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param LiveChannelId: 频道ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveChannelId: str
        :param LiveChannelName: 频道名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveChannelName: str
        :param LiveChannelType: 直播频道类型 1：固定直播；2：移动直播
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveChannelType: int
        :param LiveStatus: 通道直播状态：1: 未推流，2: 推流中
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveStatus: int
        :param PushStreamAddress: 推流地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PushStreamAddress: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: list of str
        :param UpdateTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LiveChannelId = None
        self.LiveChannelName = None
        self.LiveChannelType = None
        self.LiveStatus = None
        self.PushStreamAddress = None
        self.CreateTime = None
        self.UpdateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LiveChannelId = params.get("LiveChannelId")
        self.LiveChannelName = params.get("LiveChannelName")
        self.LiveChannelType = params.get("LiveChannelType")
        self.LiveStatus = params.get("LiveStatus")
        self.PushStreamAddress = params.get("PushStreamAddress")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.RequestId = params.get("RequestId")


class DescribeLiveRecordPlanByIdRequest(AbstractModel):
    """DescribeLiveRecordPlanById请求参数结构体

    """

    def __init__(self):
        r"""
        :param PlanId: 录制计划ID
        :type PlanId: str
        """
        self.PlanId = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveRecordPlanByIdResponse(AbstractModel):
    """DescribeLiveRecordPlanById返回参数结构体

    """

    def __init__(self):
        r"""
        :param PlanName: 计划名称
        :type PlanName: str
        :param TemplateId: 模板ID
        :type TemplateId: str
        :param TemplateName: 模板名称
        :type TemplateName: str
        :param RecordStorageTime: 存储时间
        :type RecordStorageTime: int
        :param PlanType: 计划类型
        :type PlanType: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PlanName = None
        self.TemplateId = None
        self.TemplateName = None
        self.RecordStorageTime = None
        self.PlanType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PlanName = params.get("PlanName")
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.RecordStorageTime = params.get("RecordStorageTime")
        self.PlanType = params.get("PlanType")
        self.RequestId = params.get("RequestId")


class DescribeLiveRecordPlanIdsRequest(AbstractModel):
    """DescribeLiveRecordPlanIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 时间模板ID
        :type TemplateId: str
        :param Offset: 分页偏移量
        :type Offset: int
        :param Limit: 分页大小
        :type Limit: int
        """
        self.TemplateId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveRecordPlanIdsResponse(AbstractModel):
    """DescribeLiveRecordPlanIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总个数
        :type TotalCount: int
        :param Plans: 计划数组
        :type Plans: list of LiveRecordPlanItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Plans = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Plans") is not None:
            self.Plans = []
            for item in params.get("Plans"):
                obj = LiveRecordPlanItem()
                obj._deserialize(item)
                self.Plans.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamRequest(AbstractModel):
    """DescribeLiveStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param LiveChannelId: 频道ID
        :type LiveChannelId: str
        :param ExpireTime: 过期时间
        :type ExpireTime: int
        """
        self.LiveChannelId = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.LiveChannelId = params.get("LiveChannelId")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveStreamResponse(AbstractModel):
    """DescribeLiveStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 拉流地址，只有在推流情况下才有
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotvideoindustry.v20201201.models.StreamAddress`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = StreamAddress()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeLiveVideoListRequest(AbstractModel):
    """DescribeLiveVideoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 分页的每页数量
        :type Limit: int
        :param LiveChannelId: 直播频道ID
        :type LiveChannelId: str
        :param StartRecordTime: 开始录制开始时间
        :type StartRecordTime: int
        :param EndRecordTime: 开始录制结束时间
        :type EndRecordTime: int
        :param StartExpireTime: 过期开始时间
        :type StartExpireTime: int
        :param EndExpireTime: 过期结束时间
        :type EndExpireTime: int
        :param StartFileSize: 文件大小范围 Byte
        :type StartFileSize: int
        :param EndFileSize: 文件大小范围 Byte
        :type EndFileSize: int
        :param IsRecording: 录制状态，5: 录制回写完
        :type IsRecording: int
        """
        self.Offset = None
        self.Limit = None
        self.LiveChannelId = None
        self.StartRecordTime = None
        self.EndRecordTime = None
        self.StartExpireTime = None
        self.EndExpireTime = None
        self.StartFileSize = None
        self.EndFileSize = None
        self.IsRecording = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.LiveChannelId = params.get("LiveChannelId")
        self.StartRecordTime = params.get("StartRecordTime")
        self.EndRecordTime = params.get("EndRecordTime")
        self.StartExpireTime = params.get("StartExpireTime")
        self.EndExpireTime = params.get("EndExpireTime")
        self.StartFileSize = params.get("StartFileSize")
        self.EndFileSize = params.get("EndFileSize")
        self.IsRecording = params.get("IsRecording")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveVideoListResponse(AbstractModel):
    """DescribeLiveVideoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总的条数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RecordList: 录制任务详情数组
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordList: list of LiveRecordItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.RecordList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = LiveRecordItem()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMessageForwardRequest(AbstractModel):
    """DescribeMessageForward请求参数结构体

    """

    def __init__(self):
        r"""
        :param IntId: 配置ID
        :type IntId: int
        """
        self.IntId = None


    def _deserialize(self, params):
        self.IntId = params.get("IntId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMessageForwardResponse(AbstractModel):
    """DescribeMessageForward返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegionId: 区域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: str
        :param RegionName: 区域名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionName: str
        :param Instance: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Instance: str
        :param InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param IntId: 配置ID
注意：此字段可能返回 null，表示取不到有效值。
        :type IntId: int
        :param MessageType: json数组， 转发类型 1: 告警 2:GPS
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageType: str
        :param TopicId: kafka topic id
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param CreateTime: 配置创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Uin: 用户Uin信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param TopicName: kafka topic 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegionId = None
        self.RegionName = None
        self.Instance = None
        self.InstanceName = None
        self.IntId = None
        self.MessageType = None
        self.TopicId = None
        self.CreateTime = None
        self.Uin = None
        self.TopicName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.Instance = params.get("Instance")
        self.InstanceName = params.get("InstanceName")
        self.IntId = params.get("IntId")
        self.MessageType = params.get("MessageType")
        self.TopicId = params.get("TopicId")
        self.CreateTime = params.get("CreateTime")
        self.Uin = params.get("Uin")
        self.TopicName = params.get("TopicName")
        self.RequestId = params.get("RequestId")


class DescribeMessageForwardsRequest(AbstractModel):
    """DescribeMessageForwards请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 数量限制
        :type Limit: int
        :param Offset: 偏移
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMessageForwardsResponse(AbstractModel):
    """DescribeMessageForwards返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 配置总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param List: 配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of MessageForward
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = MessageForward()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMonitorDataByDateRequest(AbstractModel):
    """DescribeMonitorDataByDate请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间戳
        :type StartTime: int
        :param EndTime: 结束时间戳 最多显示30天数据
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
        


class DescribeMonitorDataByDateResponse(AbstractModel):
    """DescribeMonitorDataByDate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 统计数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of RecordStatistic
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RecordStatistic()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePresetListRequest(AbstractModel):
    """DescribePresetList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelId: 视频通道唯一标识
        :type ChannelId: str
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        """
        self.ChannelId = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        self.DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePresetListResponse(AbstractModel):
    """DescribePresetList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 预置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of PresetItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = PresetItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRecordDatesByChannelRequest(AbstractModel):
    """DescribeRecordDatesByChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        :param ChannelId: 通道唯一标识
        :type ChannelId: str
        :param Type: 1: 云端录制 2: 本地录制
        :type Type: int
        :param Limit: 限制量，默认200
        :type Limit: int
        :param Offset: 偏移量，默认0
        :type Offset: int
        """
        self.DeviceId = None
        self.ChannelId = None
        self.Type = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ChannelId = params.get("ChannelId")
        self.Type = params.get("Type")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordDatesByChannelResponse(AbstractModel):
    """DescribeRecordDatesByChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param Dates: 含有录像文件的日期列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Dates: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Dates = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Dates = params.get("Dates")
        self.RequestId = params.get("RequestId")


class DescribeRecordDatesByLiveRequest(AbstractModel):
    """DescribeRecordDatesByLive请求参数结构体

    """

    def __init__(self):
        r"""
        :param LiveChannelId: 直播频道ID
        :type LiveChannelId: str
        :param Offset: 分页值，本地录制时参数无效
        :type Offset: int
        :param Limit: 限制值，本地录制时参数无效
        :type Limit: int
        """
        self.LiveChannelId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.LiveChannelId = params.get("LiveChannelId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordDatesByLiveResponse(AbstractModel):
    """DescribeRecordDatesByLive返回参数结构体

    """

    def __init__(self):
        r"""
        :param Dates: 录制日期数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Dates: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Dates = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Dates = params.get("Dates")
        self.RequestId = params.get("RequestId")


class DescribeRecordStreamData(AbstractModel):
    """DescribeRecordStreamData 复杂类型

    """

    def __init__(self):
        r"""
        :param RtspAddr: Rtsp地址
        :type RtspAddr: str
        :param RtmpAddr: Rtmp地址
        :type RtmpAddr: str
        :param HlsAddr: Hls地址
        :type HlsAddr: str
        :param FlvAddr: Flv地址
        :type FlvAddr: str
        :param StreamId: 流Id
        :type StreamId: str
        """
        self.RtspAddr = None
        self.RtmpAddr = None
        self.HlsAddr = None
        self.FlvAddr = None
        self.StreamId = None


    def _deserialize(self, params):
        self.RtspAddr = params.get("RtspAddr")
        self.RtmpAddr = params.get("RtmpAddr")
        self.HlsAddr = params.get("HlsAddr")
        self.FlvAddr = params.get("FlvAddr")
        self.StreamId = params.get("StreamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordStreamRequest(AbstractModel):
    """DescribeRecordStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备Id
        :type DeviceId: str
        :param ExpireTime: 流失效时间，UNIX时间戳，30天内
        :type ExpireTime: int
        :param RecordId: 录像文件ID
        :type RecordId: str
        :param StartTime: 录像流开始时间，当录像文件ID为空时有效，UNIX时间戳
        :type StartTime: int
        :param EndTime: 录像流结束时间，当录像文件iD为空时有效，UNIX时间戳
        :type EndTime: int
        :param ChannelId: 通道唯一标识（此接口升级为必填字段）
        :type ChannelId: str
        """
        self.DeviceId = None
        self.ExpireTime = None
        self.RecordId = None
        self.StartTime = None
        self.EndTime = None
        self.ChannelId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ExpireTime = params.get("ExpireTime")
        self.RecordId = params.get("RecordId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordStreamResponse(AbstractModel):
    """DescribeRecordStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 结果
        :type Data: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeRecordStreamData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeRecordStreamData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRecordingPlanByIdRequest(AbstractModel):
    """DescribeRecordingPlanById请求参数结构体

    """

    def __init__(self):
        r"""
        :param PlanId: 录制计划ID
        :type PlanId: str
        """
        self.PlanId = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordingPlanByIdResponse(AbstractModel):
    """DescribeRecordingPlanById返回参数结构体

    """

    def __init__(self):
        r"""
        :param Plan: 录制计划详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Plan: :class:`tencentcloud.iotvideoindustry.v20201201.models.RecordPlanDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Plan = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Plan") is not None:
            self.Plan = RecordPlanDetail()
            self.Plan._deserialize(params.get("Plan"))
        self.RequestId = params.get("RequestId")


class DescribeRecordingPlansRequest(AbstractModel):
    """DescribeRecordingPlans请求参数结构体

    """


class DescribeRecordingPlansResponse(AbstractModel):
    """DescribeRecordingPlans返回参数结构体

    """

    def __init__(self):
        r"""
        :param Plans: 录制计划详情·列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Plans: list of RecordPlanDetail
        :param TotalCount: 录制计划总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Plans = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Plans") is not None:
            self.Plans = []
            for item in params.get("Plans"):
                obj = RecordPlanDetail()
                obj._deserialize(item)
                self.Plans.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSIPServerRequest(AbstractModel):
    """DescribeSIPServer请求参数结构体

    """


class DescribeSIPServerResponse(AbstractModel):
    """DescribeSIPServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: SIP服务器相关配置项
        :type Data: :class:`tencentcloud.iotvideoindustry.v20201201.models.ServerConfiguration`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ServerConfiguration()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeSceneRequest(AbstractModel):
    """DescribeScene请求参数结构体

    """

    def __init__(self):
        r"""
        :param IntId: 场景ID
        :type IntId: int
        """
        self.IntId = None


    def _deserialize(self, params):
        self.IntId = params.get("IntId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSceneResponse(AbstractModel):
    """DescribeScene返回参数结构体

    """

    def __init__(self):
        r"""
        :param IntId: 场景ID
注意：此字段可能返回 null，表示取不到有效值。
        :type IntId: int
        :param RecordDuration: 录制时长(秒)
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordDuration: int
        :param SceneName: 场景名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneName: str
        :param SceneTrigger: 场景触发规则
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneTrigger: str
        :param StoreDuration: 存储时长 (天)
注意：此字段可能返回 null，表示取不到有效值。
        :type StoreDuration: int
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param Uin: 用户Uin
        :type Uin: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IntId = None
        self.RecordDuration = None
        self.SceneName = None
        self.SceneTrigger = None
        self.StoreDuration = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Uin = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IntId = params.get("IntId")
        self.RecordDuration = params.get("RecordDuration")
        self.SceneName = params.get("SceneName")
        self.SceneTrigger = params.get("SceneTrigger")
        self.StoreDuration = params.get("StoreDuration")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Uin = params.get("Uin")
        self.RequestId = params.get("RequestId")


class DescribeScenesRequest(AbstractModel):
    """DescribeScenes请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 条数限制
        :type Limit: int
        :param Offset: 偏移
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScenesResponse(AbstractModel):
    """DescribeScenes返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 场景总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param List: 场景列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of SceneItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = SceneItem()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStatisticDetailsRequest(AbstractModel):
    """DescribeStatisticDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartDate: 开始日期，格式【YYYY-MM-DD】
        :type StartDate: str
        :param EndDate: 结束日期，格式【YYYY-MM-DD】
        :type EndDate: str
        :param StatisticField: 统计项。取值范围：
1.录制设备数：RecordingDevice
2.非录制设备数：NonRecordingDevice
3.观看流量总数：WatchFlux
4.已用存储容量总数：StorageUsage
5. X-P2P分享流量: P2PFluxTotal
6. X-P2P峰值带宽: P2PPeakValue
7. RTMP推流路数(直播推流): LivePushTotal
        :type StatisticField: str
        """
        self.StartDate = None
        self.EndDate = None
        self.StatisticField = None


    def _deserialize(self, params):
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.StatisticField = params.get("StatisticField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStatisticDetailsResponse(AbstractModel):
    """DescribeStatisticDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 统计详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of StatisticItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = StatisticItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStatisticSummaryRequest(AbstractModel):
    """DescribeStatisticSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param Date: 指定日期。格式【YYYY-MM-DD】
        :type Date: str
        """
        self.Date = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStatisticSummaryResponse(AbstractModel):
    """DescribeStatisticSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param RecordingDevice: 录制设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordingDevice: int
        :param NonRecordingDevice: 非录制设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type NonRecordingDevice: int
        :param WatchFlux: 观看流量总数。为直播观看流量与点播观看流量之和。单位：GB
注意：此字段可能返回 null，表示取不到有效值。
        :type WatchFlux: float
        :param StorageUsage: 累计有效存储容量总数。单位：GB
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageUsage: float
        :param P2PFluxTotal: X-P2P分享流量。单位 Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type P2PFluxTotal: float
        :param P2PPeakValue: X-P2P峰值带宽。 单位bps
注意：此字段可能返回 null，表示取不到有效值。
        :type P2PPeakValue: float
        :param LivePushTotal: RTMP推流路数 ( 直播推流)
注意：此字段可能返回 null，表示取不到有效值。
        :type LivePushTotal: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecordingDevice = None
        self.NonRecordingDevice = None
        self.WatchFlux = None
        self.StorageUsage = None
        self.P2PFluxTotal = None
        self.P2PPeakValue = None
        self.LivePushTotal = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordingDevice = params.get("RecordingDevice")
        self.NonRecordingDevice = params.get("NonRecordingDevice")
        self.WatchFlux = params.get("WatchFlux")
        self.StorageUsage = params.get("StorageUsage")
        self.P2PFluxTotal = params.get("P2PFluxTotal")
        self.P2PPeakValue = params.get("P2PPeakValue")
        self.LivePushTotal = params.get("LivePushTotal")
        self.RequestId = params.get("RequestId")


class DescribeSubGroupsRequest(AbstractModel):
    """DescribeSubGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 分组ID
        :type GroupId: str
        :param GroupName: 分组名称，根据名称模糊匹配子分组时为必填
        :type GroupName: str
        :param Offset: 偏移量，默认0
        :type Offset: int
        :param Limit: 限制数，默认200
        :type Limit: int
        :param OnlyGroup: 是否统计子分组下的设备数，0：统计，1：不统计
        :type OnlyGroup: int
        """
        self.GroupId = None
        self.GroupName = None
        self.Offset = None
        self.Limit = None
        self.OnlyGroup = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OnlyGroup = params.get("OnlyGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubGroupsResponse(AbstractModel):
    """DescribeSubGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupList: 子分组详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupList: list of GroupItem
        :param TotalCount: 子分组总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = GroupItem()
                obj._deserialize(item)
                self.GroupList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSubscriptionStatusRequest(AbstractModel):
    """DescribeSubscriptionStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备ID
        :type DeviceId: str
        """
        self.DeviceId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscriptionStatusResponse(AbstractModel):
    """DescribeSubscriptionStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param AlarmStatus: 设备GB28181报警订阅状态 1：未开启订阅；2：已开启订阅
        :type AlarmStatus: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AlarmStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AlarmStatus = params.get("AlarmStatus")
        self.RequestId = params.get("RequestId")


class DescribeVideoListByChannelRequest(AbstractModel):
    """DescribeVideoListByChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        :param ChannelId: 通道唯一标识
        :type ChannelId: str
        :param Type: 1: 云端录制 2: 本地录制
        :type Type: int
        :param Date: 指定某天。取值【YYYY-MM-DD】
为空时默认查询最近一天的记录
        :type Date: str
        :param Limit: 限制量，默认2000
        :type Limit: int
        :param Offset: 偏移量，默认0
        :type Offset: int
        """
        self.DeviceId = None
        self.ChannelId = None
        self.Type = None
        self.Date = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ChannelId = params.get("ChannelId")
        self.Type = params.get("Type")
        self.Date = params.get("Date")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoListByChannelResponse(AbstractModel):
    """DescribeVideoListByChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param VideoList: 录像详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoList: list of RecordTaskItem
        :param TotalCount: 录像总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VideoList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VideoList") is not None:
            self.VideoList = []
            for item in params.get("VideoList"):
                obj = RecordTaskItem()
                obj._deserialize(item)
                self.VideoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVideoListRequest(AbstractModel):
    """DescribeVideoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移
        :type Offset: int
        :param Limit: 限制
        :type Limit: int
        :param StartTime: 开始时间戳，秒级
        :type StartTime: int
        :param EndTime: 结束时间戳，秒级
        :type EndTime: int
        :param DeviceId: 设备Id
        :type DeviceId: str
        :param StartRecordTime: 开始录制范围 开始
        :type StartRecordTime: int
        :param EndRecordTime: 开始录制范围 结束
        :type EndRecordTime: int
        :param StartExpireTime: 过期时间范围 开始
        :type StartExpireTime: int
        :param EndExpireTime: 过期时间范围 结束
        :type EndExpireTime: int
        :param StartFileSize: 文件大小范围 开始 单位byte
        :type StartFileSize: int
        :param EndFileSize: 文件大小范围 结束 单位byte
        :type EndFileSize: int
        :param IsRecording: 录制状态 99: 录制方已经回写状态 1: 开始录制了，等待回写 2: 已经到了时间模板的停止时间，在等待录制方回写
        :type IsRecording: int
        :param ChannelId: 通道ID默认必传
        :type ChannelId: str
        :param PlanId: 录制计划ID
        :type PlanId: str
        :param SceneId: 场景ID
        :type SceneId: int
        :param WarnId: 告警ID
        :type WarnId: int
        :param RecordType: 录制类型 1: 联动计划录制 2: 告警录制
        :type RecordType: list of int
        """
        self.Offset = None
        self.Limit = None
        self.StartTime = None
        self.EndTime = None
        self.DeviceId = None
        self.StartRecordTime = None
        self.EndRecordTime = None
        self.StartExpireTime = None
        self.EndExpireTime = None
        self.StartFileSize = None
        self.EndFileSize = None
        self.IsRecording = None
        self.ChannelId = None
        self.PlanId = None
        self.SceneId = None
        self.WarnId = None
        self.RecordType = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.DeviceId = params.get("DeviceId")
        self.StartRecordTime = params.get("StartRecordTime")
        self.EndRecordTime = params.get("EndRecordTime")
        self.StartExpireTime = params.get("StartExpireTime")
        self.EndExpireTime = params.get("EndExpireTime")
        self.StartFileSize = params.get("StartFileSize")
        self.EndFileSize = params.get("EndFileSize")
        self.IsRecording = params.get("IsRecording")
        self.ChannelId = params.get("ChannelId")
        self.PlanId = params.get("PlanId")
        self.SceneId = params.get("SceneId")
        self.WarnId = params.get("WarnId")
        self.RecordType = params.get("RecordType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoListResponse(AbstractModel):
    """DescribeVideoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
        :type TotalCount: int
        :param VideoList: 已废弃
        :type VideoList: :class:`tencentcloud.iotvideoindustry.v20201201.models.RecordTaskItem`
        :param RecordList: 录像详情列表
        :type RecordList: list of RecordTaskItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.VideoList = None
        self.RecordList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VideoList") is not None:
            self.VideoList = RecordTaskItem()
            self.VideoList._deserialize(params.get("VideoList"))
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = RecordTaskItem()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWarnModRequest(AbstractModel):
    """DescribeWarnMod请求参数结构体

    """


class DescribeWarnModResponse(AbstractModel):
    """DescribeWarnMod返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 告警类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeWarningsRequest(AbstractModel):
    """DescribeWarnings请求参数结构体

    """

    def __init__(self):
        r"""
        :param OrderType: 1:创建时间倒序 2：创建时间升序 3：level倒序 4：leve升序
        :type OrderType: int
        :param DeviceId: 可选设备id
        :type DeviceId: str
        :param WarnLevelArray: 如果不传则查询所有，取值参见配置
        :type WarnLevelArray: list of int
        :param WarnModeArray: 如果不传则查询所有，取值参见配置
        :type WarnModeArray: list of int
        :param Offset: 不传认为是0
        :type Offset: int
        :param Limit: 不传认为是20
        :type Limit: int
        :param DateBegin: 形似：2021-05-21 00:00:00 .取值在当前日前30天内，不传默认是当前日前30天日期
        :type DateBegin: str
        :param DateEnd: 形似：2021-05-21 23:59:59 .取值在当前日前30天内，不传默认是当前日前30天日期
        :type DateEnd: str
        """
        self.OrderType = None
        self.DeviceId = None
        self.WarnLevelArray = None
        self.WarnModeArray = None
        self.Offset = None
        self.Limit = None
        self.DateBegin = None
        self.DateEnd = None


    def _deserialize(self, params):
        self.OrderType = params.get("OrderType")
        self.DeviceId = params.get("DeviceId")
        self.WarnLevelArray = params.get("WarnLevelArray")
        self.WarnModeArray = params.get("WarnModeArray")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DateBegin = params.get("DateBegin")
        self.DateEnd = params.get("DateEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWarningsResponse(AbstractModel):
    """DescribeWarnings返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Data: 告警列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of WarningsData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = WarningsData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeXP2PDataRequest(AbstractModel):
    """DescribeXP2PData请求参数结构体

    """

    def __init__(self):
        r"""
        :param P2PAppId: P2P应用ID
        :type P2PAppId: str
        :param From: 查询开始时间
        :type From: int
        :param To: 查询结束时间
        :type To: int
        :param P2PChannelId: P2P通路ID
        :type P2PChannelId: str
        """
        self.P2PAppId = None
        self.From = None
        self.To = None
        self.P2PChannelId = None


    def _deserialize(self, params):
        self.P2PAppId = params.get("P2PAppId")
        self.From = params.get("From")
        self.To = params.get("To")
        self.P2PChannelId = params.get("P2PChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeXP2PDataResponse(AbstractModel):
    """DescribeXP2PData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: [log_time,cdn_bytes , p2p_bytes, online_people, stuck_times, stuck_people,request,request_success,request_fail,play_fail]
[时间戳,cdn流量(字节) , p2p流量(字节), 在线人数, 卡播次数, 卡播人数,起播请求次数,起播成功次数,起播失败次数,播放失败次数, pcdn cdn流量（字节), pcdn路由流量(字节), 上传流量(字节)]
[1481016480, 46118502414, 75144943171, 61691, 3853, 0,0,0,0,0, 0, 0, 0]
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DevGroupInfo(AbstractModel):
    """设备所在分组信息

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        :param GroupId: 分组ID
        :type GroupId: str
        :param GroupPath: 分组路径
        :type GroupPath: str
        :param ParentId: 父分组ID
        :type ParentId: str
        :param Error: 设备错误，仅在用户没权限或者设备已删除时返回具体结果
        :type Error: str
        """
        self.DeviceId = None
        self.GroupId = None
        self.GroupPath = None
        self.ParentId = None
        self.Error = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.GroupId = params.get("GroupId")
        self.GroupPath = params.get("GroupPath")
        self.ParentId = params.get("ParentId")
        self.Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceItem(AbstractModel):
    """用于描述唯一一个设备

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param ChannelId: 通道唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelId: str
        """
        self.DeviceId = None
        self.ChannelId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceMonitorValue(AbstractModel):
    """查询设备统计返回值

    """

    def __init__(self):
        r"""
        :param Value: 统计值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: float
        :param Time: 统计时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: int
        """
        self.Value = None
        self.Time = None


    def _deserialize(self, params):
        self.Value = params.get("Value")
        self.Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Events(AbstractModel):
    """设备事件列表

    """

    def __init__(self):
        r"""
        :param EventTime: 开始时间，秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type EventTime: int
        :param EventType: 事件类型 1:注册 2:心跳 4:录制异常 5:播放异常 6:流中断
注意：此字段可能返回 null，表示取不到有效值。
        :type EventType: int
        :param EventDesc: 事件描述
注意：此字段可能返回 null，表示取不到有效值。
        :type EventDesc: str
        :param DeviceType: 设备类型
        :type DeviceType: int
        :param DeviceAddress: 设备地址
        :type DeviceAddress: str
        :param DeviceId: 设备Id
        :type DeviceId: str
        :param ChannelId: 通道Id
        :type ChannelId: str
        :param EventLog: 事件日志
        :type EventLog: str
        :param DeviceName: 设备备注名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        """
        self.EventTime = None
        self.EventType = None
        self.EventDesc = None
        self.DeviceType = None
        self.DeviceAddress = None
        self.DeviceId = None
        self.ChannelId = None
        self.EventLog = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.EventTime = params.get("EventTime")
        self.EventType = params.get("EventType")
        self.EventDesc = params.get("EventDesc")
        self.DeviceType = params.get("DeviceType")
        self.DeviceAddress = params.get("DeviceAddress")
        self.DeviceId = params.get("DeviceId")
        self.ChannelId = params.get("ChannelId")
        self.EventLog = params.get("EventLog")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRecordDatesByDevRequest(AbstractModel):
    """GetRecordDatesByDev请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        :param Limit: 限制量，默认200
        :type Limit: int
        :param Offset: 偏移量，默认0
        :type Offset: int
        :param ChannelId: 通道唯一标识，对于NVR设备，多通道IPC设备，设备编码与通道编码不一致的IPC设备，此字段为必填
        :type ChannelId: str
        :param Type: 1: 云端录制 2: 本地录制
        :type Type: int
        """
        self.DeviceId = None
        self.Limit = None
        self.Offset = None
        self.ChannelId = None
        self.Type = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ChannelId = params.get("ChannelId")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRecordDatesByDevResponse(AbstractModel):
    """GetRecordDatesByDev返回参数结构体

    """

    def __init__(self):
        r"""
        :param Dates: 含有录像文件的日期列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Dates: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Dates = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Dates = params.get("Dates")
        self.RequestId = params.get("RequestId")


class GetRecordPlanByDevRequest(AbstractModel):
    """GetRecordPlanByDev请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        """
        self.DeviceId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRecordPlanByDevResponse(AbstractModel):
    """GetRecordPlanByDev返回参数结构体

    """

    def __init__(self):
        r"""
        :param Plan: 录制计划详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Plan: :class:`tencentcloud.iotvideoindustry.v20201201.models.RecordPlanItem`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Plan = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Plan") is not None:
            self.Plan = RecordPlanItem()
            self.Plan._deserialize(params.get("Plan"))
        self.RequestId = params.get("RequestId")


class GetRecordPlanByIdRequest(AbstractModel):
    """GetRecordPlanById请求参数结构体

    """

    def __init__(self):
        r"""
        :param PlanId: 录制计划ID
        :type PlanId: str
        """
        self.PlanId = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRecordPlanByIdResponse(AbstractModel):
    """GetRecordPlanById返回参数结构体

    """

    def __init__(self):
        r"""
        :param Plan: 录制计划详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Plan: :class:`tencentcloud.iotvideoindustry.v20201201.models.RecordPlanItem`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Plan = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Plan") is not None:
            self.Plan = RecordPlanItem()
            self.Plan._deserialize(params.get("Plan"))
        self.RequestId = params.get("RequestId")


class GetRecordPlansRequest(AbstractModel):
    """GetRecordPlans请求参数结构体

    """


class GetRecordPlansResponse(AbstractModel):
    """GetRecordPlans返回参数结构体

    """

    def __init__(self):
        r"""
        :param Plans: 录制计划详情·列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Plans: list of RecordPlanItem
        :param TotalCount: 录制计划总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Plans = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Plans") is not None:
            self.Plans = []
            for item in params.get("Plans"):
                obj = RecordPlanItem()
                obj._deserialize(item)
                self.Plans.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class GetTimeTemplateByIdRequest(AbstractModel):
    """GetTimeTemplateById请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 时间模板ID
        :type TemplateId: str
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTimeTemplateByIdResponse(AbstractModel):
    """GetTimeTemplateById返回参数结构体

    """

    def __init__(self):
        r"""
        :param Template: 时间模板详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Template: :class:`tencentcloud.iotvideoindustry.v20201201.models.TimeTemplateItem`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = TimeTemplateItem()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class GetTimeTemplatesRequest(AbstractModel):
    """GetTimeTemplates请求参数结构体

    """


class GetTimeTemplatesResponse(AbstractModel):
    """GetTimeTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param Templates: 时间模板列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Templates: list of TimeTemplateItem
        :param TotalCount: 时间模板总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Templates = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = TimeTemplateItem()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class GetVideoListByConRequest(AbstractModel):
    """GetVideoListByCon请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        :param Offset: 偏移量，默认0
        :type Offset: int
        :param Limit: 限制量，默认200
        :type Limit: int
        :param ChannelId: 通道唯一标识，对于NVR设备，多通道IPC设备，设备编码与通道编码不一致的IPC设备，此字段为必填
        :type ChannelId: str
        :param LatestDay: 0：查询指定日期的录像；1：查询最近一天的录像；默认0
        :type LatestDay: int
        :param Date: 指定某天。取值【YYYY-MM-DD】
为空时默认查询最近一天的记录
        :type Date: str
        :param Type: 1: 云端录制 2: 本地录制
        :type Type: int
        """
        self.DeviceId = None
        self.Offset = None
        self.Limit = None
        self.ChannelId = None
        self.LatestDay = None
        self.Date = None
        self.Type = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ChannelId = params.get("ChannelId")
        self.LatestDay = params.get("LatestDay")
        self.Date = params.get("Date")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetVideoListByConResponse(AbstractModel):
    """GetVideoListByCon返回参数结构体

    """

    def __init__(self):
        r"""
        :param VideoList: 录像详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoList: list of RecordTaskItem
        :param TotalCount: 录像总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VideoList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VideoList") is not None:
            self.VideoList = []
            for item in params.get("VideoList"):
                obj = RecordTaskItem()
                obj._deserialize(item)
                self.VideoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class GroupDeviceItem(AbstractModel):
    """分组下设备信息

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param NickName: 设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param Status: 设备状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param ExtraInformation: 扩展信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraInformation: str
        :param DeviceType: 设备类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceType: int
        :param RTSPUrl: rtsp地址
注意：此字段可能返回 null，表示取不到有效值。
        :type RTSPUrl: str
        :param DeviceCode: 设备编码
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceCode: str
        :param IsRecord: 是否存在录像
注意：此字段可能返回 null，表示取不到有效值。
        :type IsRecord: int
        :param Recordable: 该设备是否可录制
注意：此字段可能返回 null，表示取不到有效值。
        :type Recordable: int
        :param Protocol: 设备接入协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param CreateTime: 设备创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param ChannelNum: 设备通道总数
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelNum: int
        :param VideoChannelNum: 设备视频通道总数
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoChannelNum: int
        """
        self.DeviceId = None
        self.NickName = None
        self.Status = None
        self.ExtraInformation = None
        self.DeviceType = None
        self.RTSPUrl = None
        self.DeviceCode = None
        self.IsRecord = None
        self.Recordable = None
        self.Protocol = None
        self.CreateTime = None
        self.ChannelNum = None
        self.VideoChannelNum = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.NickName = params.get("NickName")
        self.Status = params.get("Status")
        self.ExtraInformation = params.get("ExtraInformation")
        self.DeviceType = params.get("DeviceType")
        self.RTSPUrl = params.get("RTSPUrl")
        self.DeviceCode = params.get("DeviceCode")
        self.IsRecord = params.get("IsRecord")
        self.Recordable = params.get("Recordable")
        self.Protocol = params.get("Protocol")
        self.CreateTime = params.get("CreateTime")
        self.ChannelNum = params.get("ChannelNum")
        self.VideoChannelNum = params.get("VideoChannelNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfo(AbstractModel):
    """分组信息详情

    """

    def __init__(self):
        r"""
        :param GroupId: 分组ID
        :type GroupId: str
        :param GroupName: 分组名称
        :type GroupName: str
        :param GroupType: 分组类型
        :type GroupType: str
        :param GroupPath: 分组路径
        :type GroupPath: str
        :param ParentId: 父分组ID
        :type ParentId: str
        :param GroupDescribe: 分组描述
        :type GroupDescribe: str
        :param ExtraInformation: 扩展信息
        :type ExtraInformation: str
        :param CreateTime: 创建时间
        :type CreateTime: int
        :param GroupStatus: 分组状态
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupStatus: int
        :param Error: 设备不存在时产生的错误
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: str
        """
        self.GroupId = None
        self.GroupName = None
        self.GroupType = None
        self.GroupPath = None
        self.ParentId = None
        self.GroupDescribe = None
        self.ExtraInformation = None
        self.CreateTime = None
        self.GroupStatus = None
        self.Error = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.GroupType = params.get("GroupType")
        self.GroupPath = params.get("GroupPath")
        self.ParentId = params.get("ParentId")
        self.GroupDescribe = params.get("GroupDescribe")
        self.ExtraInformation = params.get("ExtraInformation")
        self.CreateTime = params.get("CreateTime")
        self.GroupStatus = params.get("GroupStatus")
        self.Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupItem(AbstractModel):
    """分组信息

    """

    def __init__(self):
        r"""
        :param GroupName: 分组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param ParentId: 父分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentId: str
        :param GroupId: 分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupPath: 分组路径
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupPath: str
        :param GroupDescribe: 分组描述
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupDescribe: str
        :param DeviceNum: 分组绑定设备数
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceNum: int
        :param SubGroupNum: 子分组数量
注意：此字段可能返回 null，表示取不到有效值。
        :type SubGroupNum: int
        :param ExtraInformation: 分组附加信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraInformation: str
        :param GroupType: 分组类型
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupType: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param GroupStatus: 分组状态
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupStatus: int
        """
        self.GroupName = None
        self.ParentId = None
        self.GroupId = None
        self.GroupPath = None
        self.GroupDescribe = None
        self.DeviceNum = None
        self.SubGroupNum = None
        self.ExtraInformation = None
        self.GroupType = None
        self.CreateTime = None
        self.GroupStatus = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.ParentId = params.get("ParentId")
        self.GroupId = params.get("GroupId")
        self.GroupPath = params.get("GroupPath")
        self.GroupDescribe = params.get("GroupDescribe")
        self.DeviceNum = params.get("DeviceNum")
        self.SubGroupNum = params.get("SubGroupNum")
        self.ExtraInformation = params.get("ExtraInformation")
        self.GroupType = params.get("GroupType")
        self.CreateTime = params.get("CreateTime")
        self.GroupStatus = params.get("GroupStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveChannelInfo(AbstractModel):
    """频道信息

    """

    def __init__(self):
        r"""
        :param LiveChannelId: 频道ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveChannelId: str
        :param LiveChannelName: 频道名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveChannelName: str
        :param LiveChannelType: 频道类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveChannelType: int
        :param LiveStatus: 通道直播状态：1: 未推流，2: 推流中
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveStatus: int
        :param PushStreamAddress: 推流地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PushStreamAddress: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.LiveChannelId = None
        self.LiveChannelName = None
        self.LiveChannelType = None
        self.LiveStatus = None
        self.PushStreamAddress = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.LiveChannelId = params.get("LiveChannelId")
        self.LiveChannelName = params.get("LiveChannelName")
        self.LiveChannelType = params.get("LiveChannelType")
        self.LiveStatus = params.get("LiveStatus")
        self.PushStreamAddress = params.get("PushStreamAddress")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveChannelItem(AbstractModel):
    """直播频道详情

    """

    def __init__(self):
        r"""
        :param ChannelId: 频道ID
        :type ChannelId: str
        :param ChannelName: 频道名称
        :type ChannelName: str
        """
        self.ChannelId = None
        self.ChannelName = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        self.ChannelName = params.get("ChannelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveRecordItem(AbstractModel):
    """直播录制详情item

    """

    def __init__(self):
        r"""
        :param IntID: 录制文件自增ID
        :type IntID: int
        :param LiveChannelId: 直播频道ID
        :type LiveChannelId: str
        :param ExpectDeleteTime: 过期时间
        :type ExpectDeleteTime: int
        :param RecordTimeLen: 录制时长
        :type RecordTimeLen: int
        :param FileSize: 文件大小
        :type FileSize: int
        :param VideoUrl: 录制文件url
        :type VideoUrl: str
        :param RecordPlanId: 录制计划ID
        :type RecordPlanId: str
        :param StartTime: 录制开始时间
        :type StartTime: int
        :param EndTime: 录制结束时间
        :type EndTime: int
        """
        self.IntID = None
        self.LiveChannelId = None
        self.ExpectDeleteTime = None
        self.RecordTimeLen = None
        self.FileSize = None
        self.VideoUrl = None
        self.RecordPlanId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.IntID = params.get("IntID")
        self.LiveChannelId = params.get("LiveChannelId")
        self.ExpectDeleteTime = params.get("ExpectDeleteTime")
        self.RecordTimeLen = params.get("RecordTimeLen")
        self.FileSize = params.get("FileSize")
        self.VideoUrl = params.get("VideoUrl")
        self.RecordPlanId = params.get("RecordPlanId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveRecordPlanItem(AbstractModel):
    """直播录制计划详情

    """

    def __init__(self):
        r"""
        :param PlanId: 计划ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PlanId: str
        :param PlanName: 计划名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PlanName: str
        """
        self.PlanId = None
        self.PlanName = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        self.PlanName = params.get("PlanName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MessageForward(AbstractModel):
    """消息转发配置信息

    """

    def __init__(self):
        r"""
        :param IntId: 配置ID
注意：此字段可能返回 null，表示取不到有效值。
        :type IntId: int
        :param Uin: 用户Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param MessageType: json数组， 转发类型 1: 告警 2:GPS
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageType: str
        :param RegionId: 区域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: str
        :param RegionName: 区域名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionName: str
        :param Instance: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Instance: str
        :param InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param TopicId: kafka topic id
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param TopicName: topic 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        """
        self.IntId = None
        self.Uin = None
        self.MessageType = None
        self.RegionId = None
        self.RegionName = None
        self.Instance = None
        self.InstanceName = None
        self.TopicId = None
        self.CreateTime = None
        self.UpdateTime = None
        self.TopicName = None


    def _deserialize(self, params):
        self.IntId = params.get("IntId")
        self.Uin = params.get("Uin")
        self.MessageType = params.get("MessageType")
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.Instance = params.get("Instance")
        self.InstanceName = params.get("InstanceName")
        self.TopicId = params.get("TopicId")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBindPlanLiveChannelRequest(AbstractModel):
    """ModifyBindPlanLiveChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param PlanId: 直播录制计划ID
        :type PlanId: str
        :param Type: 1: 绑定 2: 解绑
        :type Type: int
        :param LiveChannelIds: 直播频道ID列表
        :type LiveChannelIds: list of str
        """
        self.PlanId = None
        self.Type = None
        self.LiveChannelIds = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        self.Type = params.get("Type")
        self.LiveChannelIds = params.get("LiveChannelIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBindPlanLiveChannelResponse(AbstractModel):
    """ModifyBindPlanLiveChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBindRecordingPlanRequest(AbstractModel):
    """ModifyBindRecordingPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 操作类型： 1-绑定设备 ；2-解绑设备
        :type Type: int
        :param PlanId: 录制计划ID
        :type PlanId: str
        :param Channels: 录制通道列表
        :type Channels: list of ChannelItem
        """
        self.Type = None
        self.PlanId = None
        self.Channels = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.PlanId = params.get("PlanId")
        if params.get("Channels") is not None:
            self.Channels = []
            for item in params.get("Channels"):
                obj = ChannelItem()
                obj._deserialize(item)
                self.Channels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBindRecordingPlanResponse(AbstractModel):
    """ModifyBindRecordingPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBindSceneChannelsRequest(AbstractModel):
    """ModifyBindSceneChannels请求参数结构体

    """

    def __init__(self):
        r"""
        :param SceneId: 场景ID
        :type SceneId: int
        :param Type: 1: 绑定 2: 解绑
        :type Type: int
        :param Channels: 通道列表
        :type Channels: list of ChannelItem
        """
        self.SceneId = None
        self.Type = None
        self.Channels = None


    def _deserialize(self, params):
        self.SceneId = params.get("SceneId")
        self.Type = params.get("Type")
        if params.get("Channels") is not None:
            self.Channels = []
            for item in params.get("Channels"):
                obj = ChannelItem()
                obj._deserialize(item)
                self.Channels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBindSceneChannelsResponse(AbstractModel):
    """ModifyBindSceneChannels返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBindSceneDeviceRequest(AbstractModel):
    """ModifyBindSceneDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param SceneId: 场景ID
        :type SceneId: int
        :param Type: 1: 绑定 2: 解绑
        :type Type: int
        :param Devices: 设备列表
        :type Devices: list of DeviceItem
        """
        self.SceneId = None
        self.Type = None
        self.Devices = None


    def _deserialize(self, params):
        self.SceneId = params.get("SceneId")
        self.Type = params.get("Type")
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceItem()
                obj._deserialize(item)
                self.Devices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBindSceneDeviceResponse(AbstractModel):
    """ModifyBindSceneDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDeviceDataRequest(AbstractModel):
    """ModifyDeviceData请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        :param NickName: 设备名称
        :type NickName: str
        """
        self.DeviceId = None
        self.NickName = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.NickName = params.get("NickName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceDataResponse(AbstractModel):
    """ModifyDeviceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 操作结果,“OK”表示成功，其他表示失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifyLiveChannelRequest(AbstractModel):
    """ModifyLiveChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param LiveChannelId: 直播频道ID
        :type LiveChannelId: str
        :param LiveChannelName: 直播频道名
        :type LiveChannelName: str
        """
        self.LiveChannelId = None
        self.LiveChannelName = None


    def _deserialize(self, params):
        self.LiveChannelId = params.get("LiveChannelId")
        self.LiveChannelName = params.get("LiveChannelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveChannelResponse(AbstractModel):
    """ModifyLiveChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveRecordPlanRequest(AbstractModel):
    """ModifyLiveRecordPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param PlanId: 录制计划ID
        :type PlanId: str
        :param PlanName: 录制计划名
        :type PlanName: str
        :param TemplateId: 时间模板ID，固定直播时为必填
        :type TemplateId: str
        """
        self.PlanId = None
        self.PlanName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        self.PlanName = params.get("PlanName")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveRecordPlanResponse(AbstractModel):
    """ModifyLiveRecordPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveVideoRequest(AbstractModel):
    """ModifyLiveVideo请求参数结构体

    """

    def __init__(self):
        r"""
        :param IntIDs: 视频ID 列表, 大小限制(100)
        :type IntIDs: list of int
        :param ExpireTime: 过期时间 秒 (-1: 为永不过期)
        :type ExpireTime: int
        """
        self.IntIDs = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.IntIDs = params.get("IntIDs")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveVideoResponse(AbstractModel):
    """ModifyLiveVideo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMessageForwardRequest(AbstractModel):
    """ModifyMessageForward请求参数结构体

    """

    def __init__(self):
        r"""
        :param IntId: 配置ID
        :type IntId: int
        :param MessageType: json数组， 转发类型 1: 告警 2:GPS
        :type MessageType: str
        """
        self.IntId = None
        self.MessageType = None


    def _deserialize(self, params):
        self.IntId = params.get("IntId")
        self.MessageType = params.get("MessageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMessageForwardResponse(AbstractModel):
    """ModifyMessageForward返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPresetRequest(AbstractModel):
    """ModifyPreset请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelId: 通道ID
        :type ChannelId: str
        :param PresetId: 预置位编码 范围1-8
        :type PresetId: int
        :param PresetName: 预制位名称
        :type PresetName: str
        :param DeviceId: 设备Id
        :type DeviceId: str
        """
        self.ChannelId = None
        self.PresetId = None
        self.PresetName = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        self.PresetId = params.get("PresetId")
        self.PresetName = params.get("PresetName")
        self.DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPresetResponse(AbstractModel):
    """ModifyPreset返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRecordingPlanRequest(AbstractModel):
    """ModifyRecordingPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param PlanId: 录制计划ID
        :type PlanId: str
        :param Name: 计划名称
        :type Name: str
        :param TimeTemplateId: 时间模板ID
        :type TimeTemplateId: str
        """
        self.PlanId = None
        self.Name = None
        self.TimeTemplateId = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        self.Name = params.get("Name")
        self.TimeTemplateId = params.get("TimeTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordingPlanResponse(AbstractModel):
    """ModifyRecordingPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 操作结果
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifySceneRequest(AbstractModel):
    """ModifyScene请求参数结构体

    """

    def __init__(self):
        r"""
        :param IntId: 场景ID
        :type IntId: int
        :param SceneName: 场景名称
        :type SceneName: str
        :param SceneTrigger: 触发条件
        :type SceneTrigger: str
        :param RecordDuration: 录制时长(秒)
        :type RecordDuration: int
        """
        self.IntId = None
        self.SceneName = None
        self.SceneTrigger = None
        self.RecordDuration = None


    def _deserialize(self, params):
        self.IntId = params.get("IntId")
        self.SceneName = params.get("SceneName")
        self.SceneTrigger = params.get("SceneTrigger")
        self.RecordDuration = params.get("RecordDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySceneResponse(AbstractModel):
    """ModifyScene返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubscriptionStatusRequest(AbstractModel):
    """ModifySubscriptionStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备ID
        :type DeviceId: str
        :param Status: 订阅状态 1：关闭订阅 2：开启订阅
        :type Status: int
        :param SubscriptionItem: 订阅类型 Alarm:告警订阅 Catalog:目录订阅 MobilePosition:移动位置订阅
        :type SubscriptionItem: str
        """
        self.DeviceId = None
        self.Status = None
        self.SubscriptionItem = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.Status = params.get("Status")
        self.SubscriptionItem = params.get("SubscriptionItem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscriptionStatusResponse(AbstractModel):
    """ModifySubscriptionStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVideoInfoRequest(AbstractModel):
    """ModifyVideoInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param InitIDs: 视频ID列表长度限制100内
        :type InitIDs: list of int
        :param ExpireTime: 过期时间 时间戳 -1: 永不过期 0: 无效值
        :type ExpireTime: int
        """
        self.InitIDs = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.InitIDs = params.get("InitIDs")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVideoInfoResponse(AbstractModel):
    """ModifyVideoInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PresetItem(AbstractModel):
    """预置位结构出参

    """

    def __init__(self):
        r"""
        :param PresetId: 预置位ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PresetId: int
        :param PresetName: 预置位名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PresetName: str
        :param Status: 预置位状态 0:未设置预置位 1:已设置预置位 2:已设置预置位&看守位
        :type Status: int
        :param ResetTime: 预置位启用时的自动归位时间
        :type ResetTime: int
        """
        self.PresetId = None
        self.PresetName = None
        self.Status = None
        self.ResetTime = None


    def _deserialize(self, params):
        self.PresetId = params.get("PresetId")
        self.PresetName = params.get("PresetName")
        self.Status = params.get("Status")
        self.ResetTime = params.get("ResetTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordPlanDetail(AbstractModel):
    """录制计划详情

    """

    def __init__(self):
        r"""
        :param PlanId: 计划ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PlanId: str
        :param Name: 计划名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param TimeTemplateId: 时间模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeTemplateId: str
        :param TimeTemplateName: 时间模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeTemplateName: str
        :param Channels: 绑定的通道列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Channels: list of ChannelItem
        :param RecordStorageTime: 存储周期（天）
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordStorageTime: int
        """
        self.PlanId = None
        self.Name = None
        self.TimeTemplateId = None
        self.TimeTemplateName = None
        self.Channels = None
        self.RecordStorageTime = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        self.Name = params.get("Name")
        self.TimeTemplateId = params.get("TimeTemplateId")
        self.TimeTemplateName = params.get("TimeTemplateName")
        if params.get("Channels") is not None:
            self.Channels = []
            for item in params.get("Channels"):
                obj = ChannelItem()
                obj._deserialize(item)
                self.Channels.append(obj)
        self.RecordStorageTime = params.get("RecordStorageTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordPlanItem(AbstractModel):
    """录制计划详情

    """

    def __init__(self):
        r"""
        :param PlanId: 计划ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PlanId: str
        :param Name: 计划名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param TimeTemplateId: 时间模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeTemplateId: str
        :param TimeTemplateName: 时间模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeTemplateName: str
        :param EventId: 录制类型
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: int
        :param Devices: 绑定的设备列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Devices: list of DeviceItem
        """
        self.PlanId = None
        self.Name = None
        self.TimeTemplateId = None
        self.TimeTemplateName = None
        self.EventId = None
        self.Devices = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        self.Name = params.get("Name")
        self.TimeTemplateId = params.get("TimeTemplateId")
        self.TimeTemplateName = params.get("TimeTemplateName")
        self.EventId = params.get("EventId")
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceItem()
                obj._deserialize(item)
                self.Devices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordStatistic(AbstractModel):
    """大盘统计-录像存储统计 出参RecordStatistic

    """

    def __init__(self):
        r"""
        :param Time: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: int
        :param Value: 统计结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.iotvideoindustry.v20201201.models.RecordStatisticValue`
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        if params.get("Value") is not None:
            self.Value = RecordStatisticValue()
            self.Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordStatisticValue(AbstractModel):
    """大盘统计-录像存储统计 出参Value

    """

    def __init__(self):
        r"""
        :param ExpectTimeLen: 期望执行时间 秒
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpectTimeLen: int
        :param RecordTimeLen: 实际执行时间 秒
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordTimeLen: int
        :param FileSize: 存储大小 G
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: float
        """
        self.ExpectTimeLen = None
        self.RecordTimeLen = None
        self.FileSize = None


    def _deserialize(self, params):
        self.ExpectTimeLen = params.get("ExpectTimeLen")
        self.RecordTimeLen = params.get("RecordTimeLen")
        self.FileSize = params.get("FileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTaskItem(AbstractModel):
    """普通设备的录像详情

    """

    def __init__(self):
        r"""
        :param RecordTaskId: 录像任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordTaskId: str
        :param RecordPlanId: 录制计划ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordPlanId: str
        :param StartTime: 本录制片段开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param EndTime: 本录制片段结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param EventId: 录制模式
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: int
        :param VideoUrl: 本录制片段对应的录制文件URL
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoUrl: str
        :param RecordStatus: 本录制片段当前的录制状态
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordStatus: int
        :param SceneId: 场景ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneId: int
        :param WarnId: 告警ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WarnId: int
        :param RecordId: 录制id，NVR下属设备有效
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordId: str
        """
        self.RecordTaskId = None
        self.RecordPlanId = None
        self.StartTime = None
        self.EndTime = None
        self.EventId = None
        self.VideoUrl = None
        self.RecordStatus = None
        self.SceneId = None
        self.WarnId = None
        self.RecordId = None


    def _deserialize(self, params):
        self.RecordTaskId = params.get("RecordTaskId")
        self.RecordPlanId = params.get("RecordPlanId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.EventId = params.get("EventId")
        self.VideoUrl = params.get("VideoUrl")
        self.RecordStatus = params.get("RecordStatus")
        self.SceneId = params.get("SceneId")
        self.WarnId = params.get("WarnId")
        self.RecordId = params.get("RecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetWarningRequest(AbstractModel):
    """ResetWarning请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 告警ID
        :type Id: int
        :param Index: Es中告警ID
        :type Index: str
        """
        self.Id = None
        self.Index = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetWarningResponse(AbstractModel):
    """ResetWarning返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SceneItem(AbstractModel):
    """场景列表元素

    """

    def __init__(self):
        r"""
        :param IntId: 场景ID
注意：此字段可能返回 null，表示取不到有效值。
        :type IntId: int
        :param Uin: 用户UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param SceneName: 场景名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneName: str
        :param SceneTrigger: 触发规则
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneTrigger: str
        :param RecordDuration: 录制时长 秒
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordDuration: int
        :param StoreDuration: 存储时长 天
注意：此字段可能返回 null，表示取不到有效值。
        :type StoreDuration: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 修改时间
        :type UpdateTime: str
        """
        self.IntId = None
        self.Uin = None
        self.SceneName = None
        self.SceneTrigger = None
        self.RecordDuration = None
        self.StoreDuration = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.IntId = params.get("IntId")
        self.Uin = params.get("Uin")
        self.SceneName = params.get("SceneName")
        self.SceneTrigger = params.get("SceneTrigger")
        self.RecordDuration = params.get("RecordDuration")
        self.StoreDuration = params.get("StoreDuration")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerConfiguration(AbstractModel):
    """SIIP服务器相关配置项

    """

    def __init__(self):
        r"""
        :param Host: SIP服务器地址
        :type Host: str
        :param Port: SIP服务器端口
        :type Port: int
        :param Serial: SIP服务器编码
        :type Serial: str
        :param Realm: SIP服务器域
        :type Realm: str
        """
        self.Host = None
        self.Port = None
        self.Serial = None
        self.Realm = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        self.Port = params.get("Port")
        self.Serial = params.get("Serial")
        self.Realm = params.get("Realm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatisticItem(AbstractModel):
    """某天的统计数额

    """

    def __init__(self):
        r"""
        :param Date: 日期。格式【YYYY-MM-DD】
注意：此字段可能返回 null，表示取不到有效值。
        :type Date: str
        :param Sum: 统计数额
注意：此字段可能返回 null，表示取不到有效值。
        :type Sum: float
        """
        self.Date = None
        self.Sum = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.Sum = params.get("Sum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamAddress(AbstractModel):
    """拉流地址，只有在推流情况下才有

    """

    def __init__(self):
        r"""
        :param StreamId: 流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamId: str
        :param RtspAddr: rtsp流地址
注意：此字段可能返回 null，表示取不到有效值。
        :type RtspAddr: str
        :param RtmpAddr: rtmp流地址
注意：此字段可能返回 null，表示取不到有效值。
        :type RtmpAddr: str
        :param HlsAddr: hls流地址
注意：此字段可能返回 null，表示取不到有效值。
        :type HlsAddr: str
        :param FlvAddr: flv流地址
注意：此字段可能返回 null，表示取不到有效值。
        :type FlvAddr: str
        """
        self.StreamId = None
        self.RtspAddr = None
        self.RtmpAddr = None
        self.HlsAddr = None
        self.FlvAddr = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.RtspAddr = params.get("RtspAddr")
        self.RtmpAddr = params.get("RtmpAddr")
        self.HlsAddr = params.get("HlsAddr")
        self.FlvAddr = params.get("FlvAddr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeTemplateItem(AbstractModel):
    """时间模板详情

    """

    def __init__(self):
        r"""
        :param TemplateId: 时间模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param Name: 模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param IsAllWeek: 是否全时录制，即7*24小时录制 0-否 1-是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllWeek: int
        :param Type: 是否为自定义模板 0-否 1-是
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param TimeTemplateSpecs: 时间片段详情
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeTemplateSpecs: list of TimeTemplateSpec
        """
        self.TemplateId = None
        self.Name = None
        self.IsAllWeek = None
        self.Type = None
        self.TimeTemplateSpecs = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Name = params.get("Name")
        self.IsAllWeek = params.get("IsAllWeek")
        self.Type = params.get("Type")
        if params.get("TimeTemplateSpecs") is not None:
            self.TimeTemplateSpecs = []
            for item in params.get("TimeTemplateSpecs"):
                obj = TimeTemplateSpec()
                obj._deserialize(item)
                self.TimeTemplateSpecs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeTemplateSpec(AbstractModel):
    """在操作时间模板时，用于描述各个时间片段

    """

    def __init__(self):
        r"""
        :param DayofWeek: 一周中的周几
注意：此字段可能返回 null，表示取不到有效值。
        :type DayofWeek: int
        :param BeginTime: 时间片段的开始时分。格式【HH:MM】
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: str
        :param EndTime: 时间片段的结束时分。格式【HH:MM】
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self.DayofWeek = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.DayofWeek = params.get("DayofWeek")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceGroupRequest(AbstractModel):
    """UpdateDeviceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupName: 分组名称
        :type GroupName: str
        :param GroupId: 分组ID
        :type GroupId: str
        :param GroupDescribe: 分组描述
        :type GroupDescribe: str
        :param NewParentId: 新父分组ID，用于修改分组路径
        :type NewParentId: str
        """
        self.GroupName = None
        self.GroupId = None
        self.GroupDescribe = None
        self.NewParentId = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.GroupDescribe = params.get("GroupDescribe")
        self.NewParentId = params.get("NewParentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceGroupResponse(AbstractModel):
    """UpdateDeviceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateDevicePassWordRequest(AbstractModel):
    """UpdateDevicePassWord请求参数结构体

    """

    def __init__(self):
        r"""
        :param PassWord: 设备密码
        :type PassWord: str
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        """
        self.PassWord = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.PassWord = params.get("PassWord")
        self.DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDevicePassWordResponse(AbstractModel):
    """UpdateDevicePassWord返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 操作结果，“OK”表示成功，其他表示失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class UpdateRecordPlanRequest(AbstractModel):
    """UpdateRecordPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param PlanId: 录制计划ID
        :type PlanId: str
        :param Name: 计划名称
        :type Name: str
        :param TimeTemplateId: 时间模板ID
        :type TimeTemplateId: str
        :param EventId: 触发录制的事件 1：全部
        :type EventId: int
        :param Devices: 录制设备列表
        :type Devices: list of DeviceItem
        :param IsModifyDevices: 是否更新绑定此录制计划的设备列表
0 - 不更新
1 - 更新，如果Devices参数为空则清空设备列表，Devices不为空则全量更新设备列表
        :type IsModifyDevices: int
        """
        self.PlanId = None
        self.Name = None
        self.TimeTemplateId = None
        self.EventId = None
        self.Devices = None
        self.IsModifyDevices = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        self.Name = params.get("Name")
        self.TimeTemplateId = params.get("TimeTemplateId")
        self.EventId = params.get("EventId")
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceItem()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.IsModifyDevices = params.get("IsModifyDevices")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordPlanResponse(AbstractModel):
    """UpdateRecordPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 操作结果
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class UpdateTimeTemplateRequest(AbstractModel):
    """UpdateTimeTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 时间模板ID
        :type TemplateId: str
        :param Name: 时间模板名称
        :type Name: str
        :param IsAllWeek: 是否全时录制，即7*24小时录制。
0：非全时录制；1：全时录制。默认1
        :type IsAllWeek: int
        :param TimeTemplateSpecs: 录制时间片段
        :type TimeTemplateSpecs: list of TimeTemplateSpec
        """
        self.TemplateId = None
        self.Name = None
        self.IsAllWeek = None
        self.TimeTemplateSpecs = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Name = params.get("Name")
        self.IsAllWeek = params.get("IsAllWeek")
        if params.get("TimeTemplateSpecs") is not None:
            self.TimeTemplateSpecs = []
            for item in params.get("TimeTemplateSpecs"):
                obj = TimeTemplateSpec()
                obj._deserialize(item)
                self.TimeTemplateSpecs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTimeTemplateResponse(AbstractModel):
    """UpdateTimeTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 操作结果，“OK”表示成功，其他表示失败。
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class WarningsData(AbstractModel):
    """告警列表出参

    """

    def __init__(self):
        r"""
        :param Id: 唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param DeviceId: 设备ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param DeviceName: 设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param WarnChannel: 告警通道
注意：此字段可能返回 null，表示取不到有效值。
        :type WarnChannel: str
        :param WarnLevel: 告警级别 1: "一级警情", 2: "二级警情", 3: "三级警情", 4: "四级警情",
注意：此字段可能返回 null，表示取不到有效值。
        :type WarnLevel: int
        :param WarnLevelName: 告警级别名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WarnLevelName: str
        :param WarnMode: 告警方式 2 设备报警 5 视频报警 6 设备故障报警
注意：此字段可能返回 null，表示取不到有效值。
        :type WarnMode: int
        :param WarnModeName: 告警方式名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WarnModeName: str
        :param WarnType: 告警类型  2: {
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
注意：此字段可能返回 null，表示取不到有效值。
        :type WarnType: int
        :param Del: 是否删除
注意：此字段可能返回 null，表示取不到有效值。
        :type Del: int
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.Id = None
        self.DeviceId = None
        self.DeviceName = None
        self.WarnChannel = None
        self.WarnLevel = None
        self.WarnLevelName = None
        self.WarnMode = None
        self.WarnModeName = None
        self.WarnType = None
        self.Del = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.DeviceId = params.get("DeviceId")
        self.DeviceName = params.get("DeviceName")
        self.WarnChannel = params.get("WarnChannel")
        self.WarnLevel = params.get("WarnLevel")
        self.WarnLevelName = params.get("WarnLevelName")
        self.WarnMode = params.get("WarnMode")
        self.WarnModeName = params.get("WarnModeName")
        self.WarnType = params.get("WarnType")
        self.Del = params.get("Del")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        