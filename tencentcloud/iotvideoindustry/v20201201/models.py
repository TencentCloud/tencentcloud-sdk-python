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


class AllDeviceInfo(AbstractModel):
    """查询全部设备出参

    """

    def __init__(self):
        """
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


class BindGroupDevicesRequest(AbstractModel):
    """BindGroupDevices请求参数结构体

    """

    def __init__(self):
        """
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


class BindGroupDevicesResponse(AbstractModel):
    """BindGroupDevices返回参数结构体

    """

    def __init__(self):
        """
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
        """
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
        """
        self.DeviceId = None
        self.Command = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.Command = params.get("Command")


class ControlDevicePTZResponse(AbstractModel):
    """ControlDevicePTZ返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class CreateDeviceGroupResponse(AbstractModel):
    """CreateDeviceGroup返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param NickName: 设备名称
        :type NickName: str
        :param PassWord: 设备密码
        :type PassWord: str
        :param GroupId: 设备需要绑定的分组ID，参数为空则默认绑定到根分组
        :type GroupId: str
        """
        self.NickName = None
        self.PassWord = None
        self.GroupId = None


    def _deserialize(self, params):
        self.NickName = params.get("NickName")
        self.PassWord = params.get("PassWord")
        self.GroupId = params.get("GroupId")


class CreateDeviceResponse(AbstractModel):
    """CreateDevice返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceCode: 设备编码
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceCode: str
        :param DeviceId: 设备唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param VirtualGroupId: 设备虚拟组信息，仅在创建NVR/VMS时返回该值
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


class CreateRecordPlanRequest(AbstractModel):
    """CreateRecordPlan请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 计划名称
        :type Name: str
        :param TimeTemplateId: 时间模板ID
        :type TimeTemplateId: str
        :param EventId: 触发录制的事件类别 1:全部
        :type EventId: int
        :param Devices: 该录制计划绑定的设备列表
        :type Devices: list of DeviceItem
        """
        self.Name = None
        self.TimeTemplateId = None
        self.EventId = None
        self.Devices = None


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


class CreateRecordPlanResponse(AbstractModel):
    """CreateRecordPlan返回参数结构体

    """

    def __init__(self):
        """
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


class CreateTimeTemplateRequest(AbstractModel):
    """CreateTimeTemplate请求参数结构体

    """

    def __init__(self):
        """
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


class CreateTimeTemplateResponse(AbstractModel):
    """CreateTimeTemplate返回参数结构体

    """

    def __init__(self):
        """
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


class DeleteDeviceGroupRequest(AbstractModel):
    """DeleteDeviceGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 分组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DeleteDeviceGroupResponse(AbstractModel):
    """DeleteDeviceGroup返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        """
        self.DeviceId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 操作结果
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


class DeleteRecordPlanRequest(AbstractModel):
    """DeleteRecordPlan请求参数结构体

    """

    def __init__(self):
        """
        :param PlanId: 录制计划ID
        :type PlanId: str
        """
        self.PlanId = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")


class DeleteRecordPlanResponse(AbstractModel):
    """DeleteRecordPlan返回参数结构体

    """

    def __init__(self):
        """
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


class DeleteTimeTemplateRequest(AbstractModel):
    """DeleteTimeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 时间模板ID
        :type TemplateId: str
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DeleteTimeTemplateResponse(AbstractModel):
    """DeleteTimeTemplate返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeAllDeviceListRequest(AbstractModel):
    """DescribeAllDeviceList请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，默认0
        :type Offset: int
        :param Limit: 限制，默认200
        :type Limit: int
        :param NickName: 设备名称，需要模糊匹配设备名称时为必填
        :type NickName: str
        :param DeviceIds: DeviceId列表，需要精确查找设备时为必填
        :type DeviceIds: list of str
        """
        self.Offset = None
        self.Limit = None
        self.NickName = None
        self.DeviceIds = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NickName = params.get("NickName")
        self.DeviceIds = params.get("DeviceIds")


class DescribeAllDeviceListResponse(AbstractModel):
    """DescribeAllDeviceList返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeDeviceGroupRequest(AbstractModel):
    """DescribeDeviceGroup请求参数结构体

    """

    def __init__(self):
        """
        :param DeviceIds: 设备唯一标识列表
        :type DeviceIds: list of str
        """
        self.DeviceIds = None


    def _deserialize(self, params):
        self.DeviceIds = params.get("DeviceIds")


class DescribeDeviceGroupResponse(AbstractModel):
    """DescribeDeviceGroup返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeDevicePassWordRequest(AbstractModel):
    """DescribeDevicePassWord请求参数结构体

    """

    def __init__(self):
        """
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        """
        self.DeviceId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")


class DescribeDevicePassWordResponse(AbstractModel):
    """DescribeDevicePassWord返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeDeviceStreamsData(AbstractModel):
    """DescribeDeviceStreams的出参复杂类型

    """

    def __init__(self):
        """
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


class DescribeDeviceStreamsRequest(AbstractModel):
    """DescribeDeviceStreams请求参数结构体

    """

    def __init__(self):
        """
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        :param ExpireTime: 流地址失效时间
        :type ExpireTime: int
        """
        self.DeviceId = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ExpireTime = params.get("ExpireTime")


class DescribeDeviceStreamsResponse(AbstractModel):
    """DescribeDeviceStreams返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param GroupId: 分组ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DescribeGroupByIdResponse(AbstractModel):
    """DescribeGroupById返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param GroupPath: 分组路径，格式为/aaa(/bbb/ccc)
        :type GroupPath: str
        """
        self.GroupPath = None


    def _deserialize(self, params):
        self.GroupPath = params.get("GroupPath")


class DescribeGroupByPathResponse(AbstractModel):
    """DescribeGroupByPath返回参数结构体

    """

    def __init__(self):
        """
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
        """
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
        """
        self.GroupId = None
        self.Offset = None
        self.Limit = None
        self.NickName = None
        self.Recordable = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NickName = params.get("NickName")
        self.Recordable = params.get("Recordable")


class DescribeGroupDevicesResponse(AbstractModel):
    """DescribeGroupDevices返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param GroupIds: 分组ID列表
        :type GroupIds: list of str
        """
        self.GroupIds = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")


class DescribeGroupsResponse(AbstractModel):
    """DescribeGroups返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeRecordStreamData(AbstractModel):
    """DescribeRecordStreamData 复杂类型

    """

    def __init__(self):
        """
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


class DescribeRecordStreamRequest(AbstractModel):
    """DescribeRecordStream请求参数结构体

    """

    def __init__(self):
        """
        :param DeviceId: 设备Id
        :type DeviceId: str
        :param ExpireTime: 流失效时间
        :type ExpireTime: int
        :param RecordId: 录像文件Id
        :type RecordId: str
        :param StartTime: 录像流开始时间，当录像文件Id为空时有效
        :type StartTime: int
        :param EndTime: 录像流结束时间，当录像文件Id为空时有效
        :type EndTime: int
        """
        self.DeviceId = None
        self.ExpireTime = None
        self.RecordId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ExpireTime = params.get("ExpireTime")
        self.RecordId = params.get("RecordId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeRecordStreamResponse(AbstractModel):
    """DescribeRecordStream返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeSIPServerRequest(AbstractModel):
    """DescribeSIPServer请求参数结构体

    """


class DescribeSIPServerResponse(AbstractModel):
    """DescribeSIPServer返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeStatisticDetailsRequest(AbstractModel):
    """DescribeStatisticDetails请求参数结构体

    """

    def __init__(self):
        """
        :param StartDate: 开始日期，格式【YYYY-MM-DD】
        :type StartDate: str
        :param EndDate: 结束日期，格式【YYYY-MM-DD】
        :type EndDate: str
        :param StatisticField: 统计项。取值范围：
1.录制设备数：RecordingDevice
2.非录制设备数：NonRecordingDevice
3.观看流量总数：WatchFlux
4.已用存储容量总数：StorageUsage
        :type StatisticField: str
        """
        self.StartDate = None
        self.EndDate = None
        self.StatisticField = None


    def _deserialize(self, params):
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.StatisticField = params.get("StatisticField")


class DescribeStatisticDetailsResponse(AbstractModel):
    """DescribeStatisticDetails返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param Date: 指定日期。格式【YYYY-MM-DD】
        :type Date: str
        """
        self.Date = None


    def _deserialize(self, params):
        self.Date = params.get("Date")


class DescribeStatisticSummaryResponse(AbstractModel):
    """DescribeStatisticSummary返回参数结构体

    """

    def __init__(self):
        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecordingDevice = None
        self.NonRecordingDevice = None
        self.WatchFlux = None
        self.StorageUsage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordingDevice = params.get("RecordingDevice")
        self.NonRecordingDevice = params.get("NonRecordingDevice")
        self.WatchFlux = params.get("WatchFlux")
        self.StorageUsage = params.get("StorageUsage")
        self.RequestId = params.get("RequestId")


class DescribeSubGroupsRequest(AbstractModel):
    """DescribeSubGroups请求参数结构体

    """

    def __init__(self):
        """
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


class DescribeSubGroupsResponse(AbstractModel):
    """DescribeSubGroups返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeVideoListRequest(AbstractModel):
    """DescribeVideoList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间戳，秒级
        :type StartTime: int
        :param EndTime: 结束时间戳，秒级
        :type EndTime: int
        :param Offset: 偏移
        :type Offset: int
        :param Limit: 限制
        :type Limit: int
        :param DeviceId: 设备Id
        :type DeviceId: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DeviceId = params.get("DeviceId")


class DescribeVideoListResponse(AbstractModel):
    """DescribeVideoList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数
        :type TotalCount: int
        :param VideoList: 录像详情列表
        :type VideoList: :class:`tencentcloud.iotvideoindustry.v20201201.models.RecordTaskItem`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.VideoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VideoList") is not None:
            self.VideoList = RecordTaskItem()
            self.VideoList._deserialize(params.get("VideoList"))
        self.RequestId = params.get("RequestId")


class DevGroupInfo(AbstractModel):
    """设备所在分组信息

    """

    def __init__(self):
        """
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


class DeviceItem(AbstractModel):
    """用于描述唯一一个设备

    """

    def __init__(self):
        """
        :param DeviceId: 设备唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        """
        self.DeviceId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")


class GetRecordDatesByDevRequest(AbstractModel):
    """GetRecordDatesByDev请求参数结构体

    """

    def __init__(self):
        """
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        :param Offset: 偏移量，默认0
        :type Offset: int
        :param Limit: 限制量，默认200
        :type Limit: int
        """
        self.DeviceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetRecordDatesByDevResponse(AbstractModel):
    """GetRecordDatesByDev返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        """
        self.DeviceId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")


class GetRecordPlanByDevResponse(AbstractModel):
    """GetRecordPlanByDev返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param PlanId: 录制计划ID
        :type PlanId: str
        """
        self.PlanId = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")


class GetRecordPlanByIdResponse(AbstractModel):
    """GetRecordPlanById返回参数结构体

    """

    def __init__(self):
        """
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
        """
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
        """
        :param TemplateId: 时间模板ID
        :type TemplateId: str
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class GetTimeTemplateByIdResponse(AbstractModel):
    """GetTimeTemplateById返回参数结构体

    """

    def __init__(self):
        """
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
        """
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
        """
        :param DeviceId: 设备唯一标识
        :type DeviceId: str
        :param Offset: 偏移量，默认0
        :type Offset: int
        :param Limit: 限制量，默认200
        :type Limit: int
        :param LatestDay: 0：查询指定日期的录像；1：查询最近一天的录像；默认0
        :type LatestDay: int
        :param Date: 指定某天。取值【YYYY-MM-DD】
当LatestDay为空或为0时，本参数不允许为空。
        :type Date: str
        """
        self.DeviceId = None
        self.Offset = None
        self.Limit = None
        self.LatestDay = None
        self.Date = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.LatestDay = params.get("LatestDay")
        self.Date = params.get("Date")


class GetVideoListByConResponse(AbstractModel):
    """GetVideoListByCon返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class GroupInfo(AbstractModel):
    """分组信息详情

    """

    def __init__(self):
        """
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


class GroupItem(AbstractModel):
    """分组信息

    """

    def __init__(self):
        """
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


class ModifyDeviceDataRequest(AbstractModel):
    """ModifyDeviceData请求参数结构体

    """

    def __init__(self):
        """
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


class ModifyDeviceDataResponse(AbstractModel):
    """ModifyDeviceData返回参数结构体

    """

    def __init__(self):
        """
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


class RecordPlanItem(AbstractModel):
    """录制计划详情

    """

    def __init__(self):
        """
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


class RecordTaskItem(AbstractModel):
    """普通设备的录像详情

    """

    def __init__(self):
        """
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
        """
        self.RecordTaskId = None
        self.RecordPlanId = None
        self.StartTime = None
        self.EndTime = None
        self.EventId = None
        self.VideoUrl = None
        self.RecordStatus = None


    def _deserialize(self, params):
        self.RecordTaskId = params.get("RecordTaskId")
        self.RecordPlanId = params.get("RecordPlanId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.EventId = params.get("EventId")
        self.VideoUrl = params.get("VideoUrl")
        self.RecordStatus = params.get("RecordStatus")


class ServerConfiguration(AbstractModel):
    """SIIP服务器相关配置项

    """

    def __init__(self):
        """
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


class StatisticItem(AbstractModel):
    """某天的统计数额

    """

    def __init__(self):
        """
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


class TimeTemplateItem(AbstractModel):
    """时间模板详情

    """

    def __init__(self):
        """
        :param TemplateId: 时间模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param Name: 模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param IsAllWeek: 是否全时录制，即7*24小时录制
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllWeek: int
        :param Type: 是否为自定义模板
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


class TimeTemplateSpec(AbstractModel):
    """在操作时间模板时，用于描述各个时间片段

    """

    def __init__(self):
        """
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


class UpdateDeviceGroupRequest(AbstractModel):
    """UpdateDeviceGroup请求参数结构体

    """

    def __init__(self):
        """
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


class UpdateDeviceGroupResponse(AbstractModel):
    """UpdateDeviceGroup返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class UpdateDevicePassWordResponse(AbstractModel):
    """UpdateDevicePassWord返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class UpdateRecordPlanResponse(AbstractModel):
    """UpdateRecordPlan返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class UpdateTimeTemplateResponse(AbstractModel):
    """UpdateTimeTemplate返回参数结构体

    """

    def __init__(self):
        """
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