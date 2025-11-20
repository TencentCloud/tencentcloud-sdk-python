# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.iotvideoindustry.v20201201 import models
from typing import Dict


class IotvideoindustryClient(AbstractClient):
    _apiVersion = '2020-12-01'
    _endpoint = 'iotvideoindustry.tencentcloudapi.com'
    _service = 'iotvideoindustry'

    async def BindGroupDevices(
            self,
            request: models.BindGroupDevicesRequest,
            opts: Dict = None,
    ) -> models.BindGroupDevicesResponse:
        """
        本接口(BindGroupDevices) 用于绑定设备到分组。
        """
        
        kwargs = {}
        kwargs["action"] = "BindGroupDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindGroupDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlChannelLocalRecord(
            self,
            request: models.ControlChannelLocalRecordRequest,
            opts: Dict = None,
    ) -> models.ControlChannelLocalRecordResponse:
        """
        本接口（ControlChannelLocalRecord）用于对通道本地回放流进行控制，包括暂停、播放、拉动、结束等
        """
        
        kwargs = {}
        kwargs["action"] = "ControlChannelLocalRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlChannelLocalRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlChannelPTZ(
            self,
            request: models.ControlChannelPTZRequest,
            opts: Dict = None,
    ) -> models.ControlChannelPTZResponse:
        """
        本接口(ControlChannelPTZ) 用于对支持GB28181 PTZ信令的设备进行指定通道的远程控制。
        """
        
        kwargs = {}
        kwargs["action"] = "ControlChannelPTZ"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlChannelPTZResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlDevicePTZ(
            self,
            request: models.ControlDevicePTZRequest,
            opts: Dict = None,
    ) -> models.ControlDevicePTZResponse:
        """
        本接口(ControlDevicePTZ) 用于对支持GB28181 PTZ信令的设备进行远程控制。
        请使用ControlChannelPTZ接口
        """
        
        kwargs = {}
        kwargs["action"] = "ControlDevicePTZ"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlDevicePTZResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlHomePosition(
            self,
            request: models.ControlHomePositionRequest,
            opts: Dict = None,
    ) -> models.ControlHomePositionResponse:
        """
        看守位控制
        """
        
        kwargs = {}
        kwargs["action"] = "ControlHomePosition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlHomePositionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlPreset(
            self,
            request: models.ControlPresetRequest,
            opts: Dict = None,
    ) -> models.ControlPresetResponse:
        """
        预置位控制
        """
        
        kwargs = {}
        kwargs["action"] = "ControlPreset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlPresetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlRecordStream(
            self,
            request: models.ControlRecordStreamRequest,
            opts: Dict = None,
    ) -> models.ControlRecordStreamResponse:
        """
        对回放流进行控制，包括暂停、播放、拉动、结束等
        请使用ControlChannelLocalRecord接口
        """
        
        kwargs = {}
        kwargs["action"] = "ControlRecordStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlRecordStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDevice(
            self,
            request: models.CreateDeviceRequest,
            opts: Dict = None,
    ) -> models.CreateDeviceResponse:
        """
        本接口(CreateDevice) 用于创建设备。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDeviceGroup(
            self,
            request: models.CreateDeviceGroupRequest,
            opts: Dict = None,
    ) -> models.CreateDeviceGroupResponse:
        """
        本接口(CreateDeviceGroup) 用于创建设备管理分组。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDeviceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeviceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveChannel(
            self,
            request: models.CreateLiveChannelRequest,
            opts: Dict = None,
    ) -> models.CreateLiveChannelResponse:
        """
        创建直播频道
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLiveRecordPlan(
            self,
            request: models.CreateLiveRecordPlanRequest,
            opts: Dict = None,
    ) -> models.CreateLiveRecordPlanResponse:
        """
        创建直播录制计划，直播录制接口，暂时下线中，只有国标接口支持云端录制
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLiveRecordPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLiveRecordPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMessageForward(
            self,
            request: models.CreateMessageForwardRequest,
            opts: Dict = None,
    ) -> models.CreateMessageForwardResponse:
        """
        创建消息转发配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMessageForward"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMessageForwardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRecordPlan(
            self,
            request: models.CreateRecordPlanRequest,
            opts: Dict = None,
    ) -> models.CreateRecordPlanResponse:
        """
        本接口(CreateRecordPlan) 用于创建录制计划，使设备与时间模板绑定，以便及时启动录制
        请使用CreateRecordingPlan代替
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRecordPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRecordPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRecordingPlan(
            self,
            request: models.CreateRecordingPlanRequest,
            opts: Dict = None,
    ) -> models.CreateRecordingPlanResponse:
        """
        本接口(CreateRecordingPlan) 用于创建录制计划，使通道与时间模板绑定，以便及时启动录制
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRecordingPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRecordingPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScene(
            self,
            request: models.CreateSceneRequest,
            opts: Dict = None,
    ) -> models.CreateSceneResponse:
        """
        创建场景
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScene"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSceneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTimeTemplate(
            self,
            request: models.CreateTimeTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateTimeTemplateResponse:
        """
        本接口(CreateTimeTemplate) 用于根据模板描述的具体录制时间片段，创建定制化的时间模板。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTimeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTimeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteChannel(
            self,
            request: models.DeleteChannelRequest,
            opts: Dict = None,
    ) -> models.DeleteChannelResponse:
        """
        本接口用于删除设备下的通道
        注意： 在线状态的设备不允许删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDevice(
            self,
            request: models.DeleteDeviceRequest,
            opts: Dict = None,
    ) -> models.DeleteDeviceResponse:
        """
        本接口(DeleteDevice)用于删除设备。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDeviceGroup(
            self,
            request: models.DeleteDeviceGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteDeviceGroupResponse:
        """
        本接口(DeleteDeviceGroup)用于删除分组。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDeviceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeviceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveChannel(
            self,
            request: models.DeleteLiveChannelRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveChannelResponse:
        """
        删除直播接口
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveRecordPlan(
            self,
            request: models.DeleteLiveRecordPlanRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveRecordPlanResponse:
        """
        删除直播录制计划
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveRecordPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveRecordPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLiveVideoList(
            self,
            request: models.DeleteLiveVideoListRequest,
            opts: Dict = None,
    ) -> models.DeleteLiveVideoListResponse:
        """
        直播录像删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLiveVideoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLiveVideoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMessageForward(
            self,
            request: models.DeleteMessageForwardRequest,
            opts: Dict = None,
    ) -> models.DeleteMessageForwardResponse:
        """
        删除消息转发配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMessageForward"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMessageForwardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordPlan(
            self,
            request: models.DeleteRecordPlanRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordPlanResponse:
        """
        本接口(DeleteRecordPlan)用于删除录制计划
        录制计划删除的同时，会停止该录制计划下的全部录制任务。
        请使用DeleteRecordingPlan接口
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordingPlan(
            self,
            request: models.DeleteRecordingPlanRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordingPlanResponse:
        """
        本接口(DeleteRecordingPlan)用于删除录制计划
        录制计划删除的同时，会停止该录制计划下的全部录制任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordingPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordingPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteScene(
            self,
            request: models.DeleteSceneRequest,
            opts: Dict = None,
    ) -> models.DeleteSceneResponse:
        """
        删除场景
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteScene"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSceneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTimeTemplate(
            self,
            request: models.DeleteTimeTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteTimeTemplateResponse:
        """
        本接口(DeleteTimeTemplate) 用于删除时间模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTimeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTimeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVideoList(
            self,
            request: models.DeleteVideoListRequest,
            opts: Dict = None,
    ) -> models.DeleteVideoListResponse:
        """
        删除录像存储列表
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVideoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVideoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWarning(
            self,
            request: models.DeleteWarningRequest,
            opts: Dict = None,
    ) -> models.DeleteWarningResponse:
        """
        设备告警-删除告警
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWarning"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWarningResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalEvents(
            self,
            request: models.DescribeAbnormalEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalEventsResponse:
        """
        获取异常事件统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbnormalEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbnormalEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllDeviceList(
            self,
            request: models.DescribeAllDeviceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAllDeviceListResponse:
        """
        本接口(DescribeAllDeviceList) 用于获取设备列表。
        请使用DescribeDevicesList接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllDeviceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllDeviceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBindSceneChannels(
            self,
            request: models.DescribeBindSceneChannelsRequest,
            opts: Dict = None,
    ) -> models.DescribeBindSceneChannelsResponse:
        """
        获取场景绑定通道列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBindSceneChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBindSceneChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBindSceneDevices(
            self,
            request: models.DescribeBindSceneDevicesRequest,
            opts: Dict = None,
    ) -> models.DescribeBindSceneDevicesResponse:
        """
        获取场景绑定设备列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBindSceneDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBindSceneDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChannelLiveStreamURL(
            self,
            request: models.DescribeChannelLiveStreamURLRequest,
            opts: Dict = None,
    ) -> models.DescribeChannelLiveStreamURLResponse:
        """
        本接口(DescribeChannelLiveStreamURL)用于获取设备指定通道实时流地址，地址是动态生成，如重新播放需要调用此接口重新获取最新播放地址。
        正常推流，如未设置对应录制计划，且180s无人观看此流，将会被自动掐断。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChannelLiveStreamURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChannelLiveStreamURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChannelLocalRecordURL(
            self,
            request: models.DescribeChannelLocalRecordURLRequest,
            opts: Dict = None,
    ) -> models.DescribeChannelLocalRecordURLResponse:
        """
        本接口（DescribeChannelLocalRecordURL）用于将NVR等设备对应通道本地回放文件，通过GB28181信令推送至云端，并生成对应的实时视频流URL，流地址URL是动态生成，如需重新播放请重新调用此接口获取最新地址。
        正常推流，如未设置对应录制计划，且180s无人观看此流，将会被自动掐断。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChannelLocalRecordURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChannelLocalRecordURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChannelStreamURL(
            self,
            request: models.DescribeChannelStreamURLRequest,
            opts: Dict = None,
    ) -> models.DescribeChannelStreamURLResponse:
        """
        本接口(DescribeChannelStreamURL)用于获取设备指定通道实时流地址，地址是动态生成，如重新播放需要调用此接口重新获取最新播放地址。
        正常推流，如未设置对应录制计划，且180s无人观看此流，将会被自动掐断。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChannelStreamURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChannelStreamURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChannels(
            self,
            request: models.DescribeChannelsRequest,
            opts: Dict = None,
    ) -> models.DescribeChannelsResponse:
        """
        本接口（DescribeChannels）用于获取设备下属通道列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChannelsByLiveRecordPlan(
            self,
            request: models.DescribeChannelsByLiveRecordPlanRequest,
            opts: Dict = None,
    ) -> models.DescribeChannelsByLiveRecordPlanResponse:
        """
        根据直播录制计划获取频道列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChannelsByLiveRecordPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChannelsByLiveRecordPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCurrentDeviceData(
            self,
            request: models.DescribeCurrentDeviceDataRequest,
            opts: Dict = None,
    ) -> models.DescribeCurrentDeviceDataResponse:
        """
        查询设备统计当前信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCurrentDeviceData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCurrentDeviceDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevice(
            self,
            request: models.DescribeDeviceRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceResponse:
        """
        获取指定设备详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceEvent(
            self,
            request: models.DescribeDeviceEventRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceEventResponse:
        """
        获取设备事件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceGroup(
            self,
            request: models.DescribeDeviceGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceGroupResponse:
        """
        本接口(DescribeDeviceGroup)用于根据设备ID查询设备所在分组信息，可批量查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceList(
            self,
            request: models.DescribeDeviceListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceListResponse:
        """
        本接口(DescribeDeviceList) 用于获取设备列表，支持模糊搜索
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceMonitorData(
            self,
            request: models.DescribeDeviceMonitorDataRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceMonitorDataResponse:
        """
        查询设备统计monitor信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceMonitorData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceMonitorDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevicePassWord(
            self,
            request: models.DescribeDevicePassWordRequest,
            opts: Dict = None,
    ) -> models.DescribeDevicePassWordResponse:
        """
        本接口(DescribeDevicePassWord)用于查询设备密码。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevicePassWord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDevicePassWordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceStreams(
            self,
            request: models.DescribeDeviceStreamsRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceStreamsResponse:
        """
        本接口(DescribeDeviceStreams)用于获取设备实时流地址。
        请使用DescribeChannelStreamURL接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceStreams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceStreamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupById(
            self,
            request: models.DescribeGroupByIdRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupByIdResponse:
        """
        本接口(DescribeGroupById)用于根据分组ID查询分组。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupByPath(
            self,
            request: models.DescribeGroupByPathRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupByPathResponse:
        """
        根据分组路径查询分组
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupByPath"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupByPathResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupDevices(
            self,
            request: models.DescribeGroupDevicesRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupDevicesResponse:
        """
        本接口(DescribeGroupDevices)用于查询分组下的设备列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroups(
            self,
            request: models.DescribeGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupsResponse:
        """
        本接口(DescribeGroups)用于批量查询分组信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPCChannels(
            self,
            request: models.DescribeIPCChannelsRequest,
            opts: Dict = None,
    ) -> models.DescribeIPCChannelsResponse:
        """
        获取IPC设备下属通道
        请使用DescribeChannels接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPCChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPCChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveChannel(
            self,
            request: models.DescribeLiveChannelRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveChannelResponse:
        """
        直播详情接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveChannelList(
            self,
            request: models.DescribeLiveChannelListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveChannelListResponse:
        """
        直播列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveChannelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveChannelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveRecordPlanById(
            self,
            request: models.DescribeLiveRecordPlanByIdRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveRecordPlanByIdResponse:
        """
        获取直播录制计划详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveRecordPlanById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveRecordPlanByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveRecordPlanIds(
            self,
            request: models.DescribeLiveRecordPlanIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveRecordPlanIdsResponse:
        """
        获取直播录制计划列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveRecordPlanIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveRecordPlanIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveStream(
            self,
            request: models.DescribeLiveStreamRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveStreamResponse:
        """
        直播拉流接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLiveVideoList(
            self,
            request: models.DescribeLiveVideoListRequest,
            opts: Dict = None,
    ) -> models.DescribeLiveVideoListResponse:
        """
        直播录像回放列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLiveVideoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLiveVideoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMessageForward(
            self,
            request: models.DescribeMessageForwardRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageForwardResponse:
        """
        查看消息转发配置详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessageForward"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageForwardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMessageForwards(
            self,
            request: models.DescribeMessageForwardsRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageForwardsResponse:
        """
        查看消息转发配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessageForwards"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageForwardsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMonitorDataByDate(
            self,
            request: models.DescribeMonitorDataByDateRequest,
            opts: Dict = None,
    ) -> models.DescribeMonitorDataByDateResponse:
        """
        运营中心-设备录像存储统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMonitorDataByDate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMonitorDataByDateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePresetList(
            self,
            request: models.DescribePresetListRequest,
            opts: Dict = None,
    ) -> models.DescribePresetListResponse:
        """
        获取预置位列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePresetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePresetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordDatesByChannel(
            self,
            request: models.DescribeRecordDatesByChannelRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordDatesByChannelResponse:
        """
        本接口(DescribeRecordDatesByChannel)用于查询设备含有录像文件的日期列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordDatesByChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordDatesByChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordDatesByLive(
            self,
            request: models.DescribeRecordDatesByLiveRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordDatesByLiveResponse:
        """
        直播录像存储日期列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordDatesByLive"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordDatesByLiveResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordStream(
            self,
            request: models.DescribeRecordStreamRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordStreamResponse:
        """
        获取回放视频流地址
        请使用DescribeChannelLocalRecordURL接口

        RecordId和StartTime/EndTime互斥
        当存在RecordId时，StartTime和EndTime无效
        当RecordId为空，StartTime和EndTime生效
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordingPlanById(
            self,
            request: models.DescribeRecordingPlanByIdRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordingPlanByIdResponse:
        """
        本接口(DescribeRecordingPlanById)用于根据录制计划ID获取录制计划。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordingPlanById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordingPlanByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordingPlans(
            self,
            request: models.DescribeRecordingPlansRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordingPlansResponse:
        """
        本接口(DescribeRecordingPlans)用于获取用户的全部录制计划。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordingPlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordingPlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSIPServer(
            self,
            request: models.DescribeSIPServerRequest,
            opts: Dict = None,
    ) -> models.DescribeSIPServerResponse:
        """
        本接口用于获取SIP服务器相关配置，用户可以通过这些配置项，将设备通过GB28181协议注册到本服务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSIPServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSIPServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScene(
            self,
            request: models.DescribeSceneRequest,
            opts: Dict = None,
    ) -> models.DescribeSceneResponse:
        """
        场景详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScene"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSceneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScenes(
            self,
            request: models.DescribeScenesRequest,
            opts: Dict = None,
    ) -> models.DescribeScenesResponse:
        """
        获取场景列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScenes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScenesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStatisticDetails(
            self,
            request: models.DescribeStatisticDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeStatisticDetailsResponse:
        """
        本接口(DescribeStatisticDetails)用于查询指定统计项详情，返回结果按天为单位聚合，支持的最大时间查询范围为31天。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStatisticDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStatisticDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStatisticSummary(
            self,
            request: models.DescribeStatisticSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeStatisticSummaryResponse:
        """
        本接口(DescribeStatisticSummary)用于查询用户昨日的概览数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStatisticSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStatisticSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubGroups(
            self,
            request: models.DescribeSubGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubGroupsResponse:
        """
        本接口(DescribeSubGroups)用于查询分组下的子分组列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubscriptionStatus(
            self,
            request: models.DescribeSubscriptionStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeSubscriptionStatusResponse:
        """
        查询主设备订阅状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubscriptionStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubscriptionStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoList(
            self,
            request: models.DescribeVideoListRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoListResponse:
        """
        根据时间获取云端录制文件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoListByChannel(
            self,
            request: models.DescribeVideoListByChannelRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoListByChannelResponse:
        """
        本接口(DescribeVideoListByChannel)用于查询指定通道的录制文件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoListByChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoListByChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWarnMod(
            self,
            request: models.DescribeWarnModRequest,
            opts: Dict = None,
    ) -> models.DescribeWarnModResponse:
        """
        告警等级列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWarnMod"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWarnModResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWarnings(
            self,
            request: models.DescribeWarningsRequest,
            opts: Dict = None,
    ) -> models.DescribeWarningsResponse:
        """
        获取告警列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWarnings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWarningsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeXP2PData(
            self,
            request: models.DescribeXP2PDataRequest,
            opts: Dict = None,
    ) -> models.DescribeXP2PDataResponse:
        """
        获取X-P2P的统计数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeXP2PData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeXP2PDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRecordDatesByDev(
            self,
            request: models.GetRecordDatesByDevRequest,
            opts: Dict = None,
    ) -> models.GetRecordDatesByDevResponse:
        """
        本接口(GetRecordDatesByDev)用于查询设备含有录像文件的日期列表。
        请使用DescribeRecordDatesByChannel接口
        """
        
        kwargs = {}
        kwargs["action"] = "GetRecordDatesByDev"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRecordDatesByDevResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRecordPlanByDev(
            self,
            request: models.GetRecordPlanByDevRequest,
            opts: Dict = None,
    ) -> models.GetRecordPlanByDevResponse:
        """
        本接口(GetRecordPlanByDev)用于根据设备ID查询其绑定的录制计划. 这个接口没有业务逻辑用到, 已废弃，统一用DescribeDevice
        """
        
        kwargs = {}
        kwargs["action"] = "GetRecordPlanByDev"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRecordPlanByDevResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRecordPlanById(
            self,
            request: models.GetRecordPlanByIdRequest,
            opts: Dict = None,
    ) -> models.GetRecordPlanByIdResponse:
        """
        本接口(GetRecordPlanById)用于根据录制计划ID获取录制计划。
        请使用DescribeRecordingPlanById接口
        """
        
        kwargs = {}
        kwargs["action"] = "GetRecordPlanById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRecordPlanByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRecordPlans(
            self,
            request: models.GetRecordPlansRequest,
            opts: Dict = None,
    ) -> models.GetRecordPlansResponse:
        """
        本接口(GetRecordPlans)用于获取用户的全部录制计划。
        请使用DescribeRecordingPlans接口
        """
        
        kwargs = {}
        kwargs["action"] = "GetRecordPlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRecordPlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTimeTemplateById(
            self,
            request: models.GetTimeTemplateByIdRequest,
            opts: Dict = None,
    ) -> models.GetTimeTemplateByIdResponse:
        """
        本接口(GetTimeTemplateById)用于根据模板ID获取时间模板详情。
        """
        
        kwargs = {}
        kwargs["action"] = "GetTimeTemplateById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTimeTemplateByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTimeTemplates(
            self,
            request: models.GetTimeTemplatesRequest,
            opts: Dict = None,
    ) -> models.GetTimeTemplatesResponse:
        """
        本接口(GetTimeTemplates)用于获取时间模板列表。
        """
        
        kwargs = {}
        kwargs["action"] = "GetTimeTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTimeTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetVideoListByCon(
            self,
            request: models.GetVideoListByConRequest,
            opts: Dict = None,
    ) -> models.GetVideoListByConResponse:
        """
        本接口(GetVideoListByCon)用于查询设备的录制文件列表
        请使用DescribeVideoListByChannel接口
        """
        
        kwargs = {}
        kwargs["action"] = "GetVideoListByCon"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetVideoListByConResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBindPlanLiveChannel(
            self,
            request: models.ModifyBindPlanLiveChannelRequest,
            opts: Dict = None,
    ) -> models.ModifyBindPlanLiveChannelResponse:
        """
        直播录制计划绑定解绑直播频道
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBindPlanLiveChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBindPlanLiveChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBindRecordingPlan(
            self,
            request: models.ModifyBindRecordingPlanRequest,
            opts: Dict = None,
    ) -> models.ModifyBindRecordingPlanResponse:
        """
        本接口(ModifyBindRecordingPlan)用于更新录制计划绑定的通道
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBindRecordingPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBindRecordingPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBindSceneChannels(
            self,
            request: models.ModifyBindSceneChannelsRequest,
            opts: Dict = None,
    ) -> models.ModifyBindSceneChannelsResponse:
        """
        场景绑定解绑通道接口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBindSceneChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBindSceneChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBindSceneDevice(
            self,
            request: models.ModifyBindSceneDeviceRequest,
            opts: Dict = None,
    ) -> models.ModifyBindSceneDeviceResponse:
        """
        场景绑定/解绑通道接口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBindSceneDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBindSceneDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDeviceData(
            self,
            request: models.ModifyDeviceDataRequest,
            opts: Dict = None,
    ) -> models.ModifyDeviceDataResponse:
        """
        本接口(ModifyDeviceData)用于编辑设备信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDeviceData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDeviceDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveChannel(
            self,
            request: models.ModifyLiveChannelRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveChannelResponse:
        """
        编辑直播接口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveRecordPlan(
            self,
            request: models.ModifyLiveRecordPlanRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveRecordPlanResponse:
        """
        编辑直播录制计划
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveRecordPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveRecordPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLiveVideo(
            self,
            request: models.ModifyLiveVideoRequest,
            opts: Dict = None,
    ) -> models.ModifyLiveVideoResponse:
        """
        直播录像编辑
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLiveVideo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLiveVideoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMessageForward(
            self,
            request: models.ModifyMessageForwardRequest,
            opts: Dict = None,
    ) -> models.ModifyMessageForwardResponse:
        """
        修改消息转发配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMessageForward"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMessageForwardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPreset(
            self,
            request: models.ModifyPresetRequest,
            opts: Dict = None,
    ) -> models.ModifyPresetResponse:
        """
        编辑预置位信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPreset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPresetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordingPlan(
            self,
            request: models.ModifyRecordingPlanRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordingPlanResponse:
        """
        本接口(ModifyRecordingPlan)用于更新录制计划。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordingPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordingPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyScene(
            self,
            request: models.ModifySceneRequest,
            opts: Dict = None,
    ) -> models.ModifySceneResponse:
        """
        修改场景
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyScene"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySceneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubscriptionStatus(
            self,
            request: models.ModifySubscriptionStatusRequest,
            opts: Dict = None,
    ) -> models.ModifySubscriptionStatusResponse:
        """
        编辑设备订阅状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubscriptionStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubscriptionStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVideoInfo(
            self,
            request: models.ModifyVideoInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyVideoInfoResponse:
        """
        修改录像存储列表
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVideoInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVideoInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetWarning(
            self,
            request: models.ResetWarningRequest,
            opts: Dict = None,
    ) -> models.ResetWarningResponse:
        """
        重置设备告警
        """
        
        kwargs = {}
        kwargs["action"] = "ResetWarning"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetWarningResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDeviceGroup(
            self,
            request: models.UpdateDeviceGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateDeviceGroupResponse:
        """
        本接口(UpdateDeviceGroup)用于修改分组信息。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDeviceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDeviceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDevicePassWord(
            self,
            request: models.UpdateDevicePassWordRequest,
            opts: Dict = None,
    ) -> models.UpdateDevicePassWordResponse:
        """
        本接口(UpdateDevicePassWord)用于修改设备密码。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDevicePassWord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDevicePassWordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRecordPlan(
            self,
            request: models.UpdateRecordPlanRequest,
            opts: Dict = None,
    ) -> models.UpdateRecordPlanResponse:
        """
        本接口(UpdateRecordPlan)用于更新录制计划。
        请使用 ModifyRecordingPlan接口和ModifyBindRecordingPlan接口
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRecordPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRecordPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTimeTemplate(
            self,
            request: models.UpdateTimeTemplateRequest,
            opts: Dict = None,
    ) -> models.UpdateTimeTemplateResponse:
        """
        本接口(UpdateTimeTemplate)用于更新时间模板。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTimeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTimeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)