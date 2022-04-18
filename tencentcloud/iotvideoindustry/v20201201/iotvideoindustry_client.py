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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.iotvideoindustry.v20201201 import models


class IotvideoindustryClient(AbstractClient):
    _apiVersion = '2020-12-01'
    _endpoint = 'iotvideoindustry.tencentcloudapi.com'
    _service = 'iotvideoindustry'


    def BindGroupDevices(self, request):
        """本接口(BindGroupDevices) 用于绑定设备到分组。

        :param request: Request instance for BindGroupDevices.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.BindGroupDevicesRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.BindGroupDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindGroupDevices", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindGroupDevicesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ControlChannelLocalRecord(self, request):
        """本接口（ControlChannelLocalRecord）用于对通道本地回放流进行控制，包括暂停、播放、拉动、结束等

        :param request: Request instance for ControlChannelLocalRecord.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ControlChannelLocalRecordRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ControlChannelLocalRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlChannelLocalRecord", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ControlChannelLocalRecordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ControlChannelPTZ(self, request):
        """本接口(ControlChannelPTZ) 用于对支持GB28181 PTZ信令的设备进行指定通道的远程控制。

        :param request: Request instance for ControlChannelPTZ.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ControlChannelPTZRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ControlChannelPTZResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlChannelPTZ", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ControlChannelPTZResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ControlDevicePTZ(self, request):
        """本接口(ControlDevicePTZ) 用于对支持GB28181 PTZ信令的设备进行远程控制。
        请使用ControlChannelPTZ接口

        :param request: Request instance for ControlDevicePTZ.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ControlDevicePTZRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ControlDevicePTZResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlDevicePTZ", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ControlDevicePTZResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ControlHomePosition(self, request):
        """看守位控制

        :param request: Request instance for ControlHomePosition.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ControlHomePositionRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ControlHomePositionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlHomePosition", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ControlHomePositionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ControlPreset(self, request):
        """预置位控制

        :param request: Request instance for ControlPreset.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ControlPresetRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ControlPresetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlPreset", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ControlPresetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ControlRecordStream(self, request):
        """对回放流进行控制，包括暂停、播放、拉动、结束等
        请使用ControlChannelLocalRecord接口

        :param request: Request instance for ControlRecordStream.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ControlRecordStreamRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ControlRecordStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlRecordStream", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ControlRecordStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDevice(self, request):
        """本接口(CreateDevice) 用于创建设备。

        :param request: Request instance for CreateDevice.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDevice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDeviceGroup(self, request):
        """本接口(CreateDeviceGroup) 用于创建设备管理分组。

        :param request: Request instance for CreateDeviceGroup.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateDeviceGroupRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateDeviceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDeviceGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDeviceGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveChannel(self, request):
        """创建直播频道

        :param request: Request instance for CreateLiveChannel.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateLiveChannelRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateLiveChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveChannel", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveChannelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLiveRecordPlan(self, request):
        """创建直播录制计划

        :param request: Request instance for CreateLiveRecordPlan.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateLiveRecordPlanRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateLiveRecordPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLiveRecordPlan", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveRecordPlanResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateMessageForward(self, request):
        """创建消息转发配置

        :param request: Request instance for CreateMessageForward.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateMessageForwardRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateMessageForwardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMessageForward", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMessageForwardResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRecordPlan(self, request):
        """本接口(CreateRecordPlan) 用于创建录制计划，使设备与时间模板绑定，以便及时启动录制
        请使用CreateRecordingPlan代替

        :param request: Request instance for CreateRecordPlan.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateRecordPlanRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateRecordPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRecordPlan", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRecordPlanResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRecordingPlan(self, request):
        """本接口(CreateRecordingPlan) 用于创建录制计划，使通道与时间模板绑定，以便及时启动录制

        :param request: Request instance for CreateRecordingPlan.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateRecordingPlanRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateRecordingPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRecordingPlan", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRecordingPlanResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateScene(self, request):
        """创建场景

        :param request: Request instance for CreateScene.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateSceneRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateSceneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScene", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSceneResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTimeTemplate(self, request):
        """本接口(CreateTimeTemplate) 用于根据模板描述的具体录制时间片段，创建定制化的时间模板。

        :param request: Request instance for CreateTimeTemplate.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateTimeTemplateRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.CreateTimeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTimeTemplate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTimeTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteChannel(self, request):
        """本接口用于删除设备下的通道
        注意： 在线状态的设备不允许删除

        :param request: Request instance for DeleteChannel.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteChannelRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteChannel", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteChannelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDevice(self, request):
        """本接口(DeleteDevice)用于删除设备。

        :param request: Request instance for DeleteDevice.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDevice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDeviceGroup(self, request):
        """本接口(DeleteDeviceGroup)用于删除分组。

        :param request: Request instance for DeleteDeviceGroup.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteDeviceGroupRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteDeviceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDeviceGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDeviceGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveChannel(self, request):
        """删除直播接口

        :param request: Request instance for DeleteLiveChannel.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteLiveChannelRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteLiveChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveChannel", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveChannelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveRecordPlan(self, request):
        """删除直播录制计划

        :param request: Request instance for DeleteLiveRecordPlan.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteLiveRecordPlanRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteLiveRecordPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveRecordPlan", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveRecordPlanResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLiveVideoList(self, request):
        """直播录像删除

        :param request: Request instance for DeleteLiveVideoList.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteLiveVideoListRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteLiveVideoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLiveVideoList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveVideoListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteMessageForward(self, request):
        """删除消息转发配置

        :param request: Request instance for DeleteMessageForward.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteMessageForwardRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteMessageForwardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMessageForward", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMessageForwardResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRecordPlan(self, request):
        """本接口(DeleteRecordPlan)用于删除录制计划
        录制计划删除的同时，会停止该录制计划下的全部录制任务。
        请使用DeleteRecordingPlan接口

        :param request: Request instance for DeleteRecordPlan.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteRecordPlanRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteRecordPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordPlan", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRecordPlanResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRecordingPlan(self, request):
        """本接口(DeleteRecordingPlan)用于删除录制计划
        录制计划删除的同时，会停止该录制计划下的全部录制任务。

        :param request: Request instance for DeleteRecordingPlan.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteRecordingPlanRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteRecordingPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordingPlan", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRecordingPlanResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteScene(self, request):
        """删除场景

        :param request: Request instance for DeleteScene.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteSceneRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteSceneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteScene", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSceneResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTimeTemplate(self, request):
        """本接口(DeleteTimeTemplate) 用于删除时间模板。

        :param request: Request instance for DeleteTimeTemplate.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteTimeTemplateRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteTimeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTimeTemplate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTimeTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteVideoList(self, request):
        """删除录像存储列表

        :param request: Request instance for DeleteVideoList.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteVideoListRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteVideoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVideoList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVideoListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteWarning(self, request):
        """设备告警-删除告警

        :param request: Request instance for DeleteWarning.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteWarningRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DeleteWarningResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWarning", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWarningResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAbnormalEvents(self, request):
        """获取异常事件统计

        :param request: Request instance for DescribeAbnormalEvents.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeAbnormalEventsRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeAbnormalEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalEvents", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAbnormalEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAllDeviceList(self, request):
        """本接口(DescribeAllDeviceList) 用于获取设备列表。
        请使用DescribeDevicesList接口

        :param request: Request instance for DescribeAllDeviceList.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeAllDeviceListRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeAllDeviceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllDeviceList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAllDeviceListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBindSceneChannels(self, request):
        """获取场景绑定通道列表

        :param request: Request instance for DescribeBindSceneChannels.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeBindSceneChannelsRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeBindSceneChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBindSceneChannels", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBindSceneChannelsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBindSceneDevices(self, request):
        """获取场景绑定设备列表

        :param request: Request instance for DescribeBindSceneDevices.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeBindSceneDevicesRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeBindSceneDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBindSceneDevices", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBindSceneDevicesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeChannelLiveStreamURL(self, request):
        """本接口(DescribeChannelLiveStreamURL)用于获取设备指定通道实时流地址，地址是动态生成，如重新播放需要调用此接口重新获取最新播放地址。
        正常推流，如未设置对应录制计划，且180s无人观看此流，将会被自动掐断。

        :param request: Request instance for DescribeChannelLiveStreamURL.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeChannelLiveStreamURLRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeChannelLiveStreamURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChannelLiveStreamURL", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeChannelLiveStreamURLResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeChannelLocalRecordURL(self, request):
        """本接口（DescribeChannelLocalRecordURL）用于将NVR等设备对应通道本地回放文件，通过GB28181信令推送至云端，并生成对应的实时视频流URL，流地址URL是动态生成，如需重新播放请重新调用此接口获取最新地址。
        正常推流，如未设置对应录制计划，且180s无人观看此流，将会被自动掐断。

        :param request: Request instance for DescribeChannelLocalRecordURL.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeChannelLocalRecordURLRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeChannelLocalRecordURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChannelLocalRecordURL", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeChannelLocalRecordURLResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeChannelStreamURL(self, request):
        """本接口(DescribeChannelStreamURL)用于获取设备指定通道实时流地址，地址是动态生成，如重新播放需要调用此接口重新获取最新播放地址。
        正常推流，如未设置对应录制计划，且180s无人观看此流，将会被自动掐断。

        :param request: Request instance for DescribeChannelStreamURL.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeChannelStreamURLRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeChannelStreamURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChannelStreamURL", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeChannelStreamURLResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeChannels(self, request):
        """本接口（DescribeChannels）用于获取设备下属通道列表

        :param request: Request instance for DescribeChannels.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeChannelsRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChannels", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeChannelsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeChannelsByLiveRecordPlan(self, request):
        """根据直播录制计划获取频道列表

        :param request: Request instance for DescribeChannelsByLiveRecordPlan.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeChannelsByLiveRecordPlanRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeChannelsByLiveRecordPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChannelsByLiveRecordPlan", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeChannelsByLiveRecordPlanResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCurrentDeviceData(self, request):
        """查询设备统计当前信息

        :param request: Request instance for DescribeCurrentDeviceData.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeCurrentDeviceDataRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeCurrentDeviceDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCurrentDeviceData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCurrentDeviceDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDevice(self, request):
        """获取指定设备详细信息

        :param request: Request instance for DescribeDevice.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeviceEvent(self, request):
        """获取设备事件

        :param request: Request instance for DescribeDeviceEvent.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceEventRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceEvent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceEventResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeviceGroup(self, request):
        """本接口(DescribeDeviceGroup)用于根据设备ID查询设备所在分组信息，可批量查询。

        :param request: Request instance for DescribeDeviceGroup.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceGroupRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeviceList(self, request):
        """本接口(DescribeDevicesList) 用于获取设备列表，支持模糊搜索

        :param request: Request instance for DescribeDeviceList.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceListRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeviceMonitorData(self, request):
        """查询设备统计monitor信息

        :param request: Request instance for DescribeDeviceMonitorData.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceMonitorDataRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceMonitorDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceMonitorData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceMonitorDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDevicePassWord(self, request):
        """本接口(DescribeDevicePassWord)用于查询设备密码。

        :param request: Request instance for DescribeDevicePassWord.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDevicePassWordRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDevicePassWordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevicePassWord", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDevicePassWordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeviceStreams(self, request):
        """本接口(DescribeDeviceStreams)用于获取设备实时流地址。
        请使用DescribeChannelStreamURL接口

        :param request: Request instance for DescribeDeviceStreams.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceStreamsRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeDeviceStreamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceStreams", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceStreamsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGroupById(self, request):
        """本接口(DescribeGroupById)用于根据分组ID查询分组。

        :param request: Request instance for DescribeGroupById.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeGroupByIdRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeGroupByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupById", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupByIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGroupByPath(self, request):
        """根据分组路径查询分组

        :param request: Request instance for DescribeGroupByPath.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeGroupByPathRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeGroupByPathResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupByPath", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupByPathResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGroupDevices(self, request):
        """本接口(DescribeGroupDevices)用于查询分组下的设备列表。

        :param request: Request instance for DescribeGroupDevices.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeGroupDevicesRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeGroupDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupDevices", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupDevicesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGroups(self, request):
        """本接口(DescribeGroups)用于批量查询分组信息。

        :param request: Request instance for DescribeGroups.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeGroupsRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIPCChannels(self, request):
        """获取IPC设备下属通道
        请使用DescribeChannels接口

        :param request: Request instance for DescribeIPCChannels.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeIPCChannelsRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeIPCChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIPCChannels", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIPCChannelsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveChannel(self, request):
        """直播详情接口

        :param request: Request instance for DescribeLiveChannel.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeLiveChannelRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeLiveChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveChannel", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveChannelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveChannelList(self, request):
        """直播列表接口

        :param request: Request instance for DescribeLiveChannelList.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeLiveChannelListRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeLiveChannelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveChannelList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveChannelListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveRecordPlanById(self, request):
        """获取直播录制计划详情

        :param request: Request instance for DescribeLiveRecordPlanById.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeLiveRecordPlanByIdRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeLiveRecordPlanByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveRecordPlanById", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveRecordPlanByIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveRecordPlanIds(self, request):
        """获取直播录制计划列表

        :param request: Request instance for DescribeLiveRecordPlanIds.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeLiveRecordPlanIdsRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeLiveRecordPlanIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveRecordPlanIds", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveRecordPlanIdsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveStream(self, request):
        """直播拉流接口

        :param request: Request instance for DescribeLiveStream.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeLiveStreamRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeLiveStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveStream", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLiveVideoList(self, request):
        """直播录像回放列表

        :param request: Request instance for DescribeLiveVideoList.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeLiveVideoListRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeLiveVideoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLiveVideoList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveVideoListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMessageForward(self, request):
        """查看消息转发配置详情

        :param request: Request instance for DescribeMessageForward.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeMessageForwardRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeMessageForwardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessageForward", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMessageForwardResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMessageForwards(self, request):
        """查看消息转发配置列表

        :param request: Request instance for DescribeMessageForwards.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeMessageForwardsRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeMessageForwardsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMessageForwards", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMessageForwardsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMonitorDataByDate(self, request):
        """运营中心-设备录像存储统计

        :param request: Request instance for DescribeMonitorDataByDate.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeMonitorDataByDateRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeMonitorDataByDateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMonitorDataByDate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMonitorDataByDateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePresetList(self, request):
        """获取预置位列表

        :param request: Request instance for DescribePresetList.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribePresetListRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribePresetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePresetList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePresetListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRecordDatesByChannel(self, request):
        """本接口(DescribeRecordDatesByChannel)用于查询设备含有录像文件的日期列表。

        :param request: Request instance for DescribeRecordDatesByChannel.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeRecordDatesByChannelRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeRecordDatesByChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordDatesByChannel", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRecordDatesByChannelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRecordDatesByLive(self, request):
        """直播录像存储日期列表

        :param request: Request instance for DescribeRecordDatesByLive.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeRecordDatesByLiveRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeRecordDatesByLiveResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordDatesByLive", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRecordDatesByLiveResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRecordStream(self, request):
        """获取回放视频流地址
        请使用DescribeChannelLocalRecordURL接口

        RecordId和StartTime/EndTime互斥
        当存在RecordId时，StartTime和EndTime无效
        当RecordId为空，StartTime和EndTime生效

        :param request: Request instance for DescribeRecordStream.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeRecordStreamRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeRecordStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordStream", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRecordStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRecordingPlanById(self, request):
        """本接口(DescribeRecordingPlanById)用于根据录制计划ID获取录制计划。

        :param request: Request instance for DescribeRecordingPlanById.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeRecordingPlanByIdRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeRecordingPlanByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordingPlanById", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRecordingPlanByIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRecordingPlans(self, request):
        """本接口(DescribeRecordingPlans)用于获取用户的全部录制计划。

        :param request: Request instance for DescribeRecordingPlans.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeRecordingPlansRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeRecordingPlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordingPlans", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRecordingPlansResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSIPServer(self, request):
        """本接口用于获取SIP服务器相关配置，用户可以通过这些配置项，将设备通过GB28181协议注册到本服务。

        :param request: Request instance for DescribeSIPServer.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeSIPServerRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeSIPServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSIPServer", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSIPServerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeScene(self, request):
        """场景详情

        :param request: Request instance for DescribeScene.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeSceneRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeSceneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScene", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSceneResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeScenes(self, request):
        """获取场景列表

        :param request: Request instance for DescribeScenes.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeScenesRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeScenesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScenes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScenesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStatisticDetails(self, request):
        """本接口(DescribeStatisticDetails)用于查询指定统计项详情，返回结果按天为单位聚合，支持的最大时间查询范围为31天。

        :param request: Request instance for DescribeStatisticDetails.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeStatisticDetailsRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeStatisticDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStatisticDetails", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStatisticDetailsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStatisticSummary(self, request):
        """本接口(DescribeStatisticSummary)用于查询用户昨日的概览数据。

        :param request: Request instance for DescribeStatisticSummary.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeStatisticSummaryRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeStatisticSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStatisticSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStatisticSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSubGroups(self, request):
        """本接口(DescribeSubGroups)用于查询分组下的子分组列表。

        :param request: Request instance for DescribeSubGroups.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeSubGroupsRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeSubGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSubscriptionStatus(self, request):
        """查询主设备订阅状态

        :param request: Request instance for DescribeSubscriptionStatus.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeSubscriptionStatusRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeSubscriptionStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubscriptionStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubscriptionStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVideoList(self, request):
        """根据时间获取云端录制文件列表

        :param request: Request instance for DescribeVideoList.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeVideoListRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeVideoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVideoListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVideoListByChannel(self, request):
        """本接口(DescribeVideoListByChannel)用于查询指定通道的录制文件列表

        :param request: Request instance for DescribeVideoListByChannel.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeVideoListByChannelRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeVideoListByChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoListByChannel", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVideoListByChannelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWarnMod(self, request):
        """告警等级列表

        :param request: Request instance for DescribeWarnMod.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeWarnModRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeWarnModResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWarnMod", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWarnModResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWarnings(self, request):
        """获取告警列表

        :param request: Request instance for DescribeWarnings.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeWarningsRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeWarningsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWarnings", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWarningsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeXP2PData(self, request):
        """获取X-P2P的统计数据

        :param request: Request instance for DescribeXP2PData.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeXP2PDataRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.DescribeXP2PDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeXP2PData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeXP2PDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRecordDatesByDev(self, request):
        """本接口(GetRecordDatesByDev)用于查询设备含有录像文件的日期列表。
        请使用DescribeRecordDatesByChannel接口

        :param request: Request instance for GetRecordDatesByDev.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.GetRecordDatesByDevRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.GetRecordDatesByDevResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRecordDatesByDev", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRecordDatesByDevResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRecordPlanByDev(self, request):
        """本接口(GetRecordPlanByDev)用于根据设备ID查询其绑定的录制计划.

        :param request: Request instance for GetRecordPlanByDev.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.GetRecordPlanByDevRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.GetRecordPlanByDevResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRecordPlanByDev", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRecordPlanByDevResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRecordPlanById(self, request):
        """本接口(GetRecordPlanById)用于根据录制计划ID获取录制计划。
        请使用DescribeRecordingPlanById接口

        :param request: Request instance for GetRecordPlanById.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.GetRecordPlanByIdRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.GetRecordPlanByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRecordPlanById", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRecordPlanByIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRecordPlans(self, request):
        """本接口(GetRecordPlans)用于获取用户的全部录制计划。
        请使用DescribeRecordingPlans接口

        :param request: Request instance for GetRecordPlans.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.GetRecordPlansRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.GetRecordPlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRecordPlans", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRecordPlansResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetTimeTemplateById(self, request):
        """本接口(GetTimeTemplateById)用于根据模板ID获取时间模板详情。

        :param request: Request instance for GetTimeTemplateById.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.GetTimeTemplateByIdRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.GetTimeTemplateByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTimeTemplateById", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTimeTemplateByIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetTimeTemplates(self, request):
        """本接口(GetTimeTemplates)用于获取时间模板列表。

        :param request: Request instance for GetTimeTemplates.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.GetTimeTemplatesRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.GetTimeTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTimeTemplates", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTimeTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetVideoListByCon(self, request):
        """本接口(GetVideoListByCon)用于查询设备的录制文件列表
        请使用DescribeVideoListByChannel接口

        :param request: Request instance for GetVideoListByCon.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.GetVideoListByConRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.GetVideoListByConResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetVideoListByCon", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetVideoListByConResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyBindPlanLiveChannel(self, request):
        """直播录制计划绑定解绑直播频道

        :param request: Request instance for ModifyBindPlanLiveChannel.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyBindPlanLiveChannelRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyBindPlanLiveChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBindPlanLiveChannel", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBindPlanLiveChannelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyBindRecordingPlan(self, request):
        """本接口(ModifyBindRecordingPlan)用于更新录制计划绑定的通道

        :param request: Request instance for ModifyBindRecordingPlan.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyBindRecordingPlanRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyBindRecordingPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBindRecordingPlan", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBindRecordingPlanResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyBindSceneChannels(self, request):
        """场景绑定解绑通道接口

        :param request: Request instance for ModifyBindSceneChannels.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyBindSceneChannelsRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyBindSceneChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBindSceneChannels", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBindSceneChannelsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyBindSceneDevice(self, request):
        """场景绑定/解绑通道接口

        :param request: Request instance for ModifyBindSceneDevice.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyBindSceneDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyBindSceneDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBindSceneDevice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBindSceneDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDeviceData(self, request):
        """本接口(ModifyDeviceData)用于编辑设备信息。

        :param request: Request instance for ModifyDeviceData.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyDeviceDataRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyDeviceDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDeviceData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDeviceDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLiveChannel(self, request):
        """编辑直播接口

        :param request: Request instance for ModifyLiveChannel.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyLiveChannelRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyLiveChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveChannel", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveChannelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLiveRecordPlan(self, request):
        """编辑直播录制计划

        :param request: Request instance for ModifyLiveRecordPlan.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyLiveRecordPlanRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyLiveRecordPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveRecordPlan", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveRecordPlanResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLiveVideo(self, request):
        """直播录像编辑

        :param request: Request instance for ModifyLiveVideo.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyLiveVideoRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyLiveVideoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLiveVideo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveVideoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyMessageForward(self, request):
        """修改消息转发配置

        :param request: Request instance for ModifyMessageForward.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyMessageForwardRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyMessageForwardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMessageForward", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMessageForwardResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPreset(self, request):
        """编辑预置位信息

        :param request: Request instance for ModifyPreset.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyPresetRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyPresetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPreset", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPresetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRecordingPlan(self, request):
        """本接口(ModifyRecordingPlan)用于更新录制计划。

        :param request: Request instance for ModifyRecordingPlan.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyRecordingPlanRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyRecordingPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordingPlan", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRecordingPlanResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyScene(self, request):
        """修改场景

        :param request: Request instance for ModifyScene.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifySceneRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifySceneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyScene", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySceneResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySubscriptionStatus(self, request):
        """编辑设备订阅状态

        :param request: Request instance for ModifySubscriptionStatus.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifySubscriptionStatusRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifySubscriptionStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubscriptionStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubscriptionStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVideoInfo(self, request):
        """修改录像存储列表

        :param request: Request instance for ModifyVideoInfo.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyVideoInfoRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ModifyVideoInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVideoInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVideoInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetWarning(self, request):
        """重置设备告警

        :param request: Request instance for ResetWarning.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.ResetWarningRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.ResetWarningResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetWarning", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetWarningResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateDeviceGroup(self, request):
        """本接口(UpdateDeviceGroup)用于修改分组信息。

        :param request: Request instance for UpdateDeviceGroup.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.UpdateDeviceGroupRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.UpdateDeviceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDeviceGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDeviceGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateDevicePassWord(self, request):
        """本接口(UpdateDevicePassWord)用于修改设备密码。

        :param request: Request instance for UpdateDevicePassWord.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.UpdateDevicePassWordRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.UpdateDevicePassWordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDevicePassWord", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDevicePassWordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateRecordPlan(self, request):
        """本接口(UpdateRecordPlan)用于更新录制计划。
        请使用 ModifyRecordingPlan接口和ModifyBindRecordingPlan接口

        :param request: Request instance for UpdateRecordPlan.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.UpdateRecordPlanRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.UpdateRecordPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRecordPlan", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateRecordPlanResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateTimeTemplate(self, request):
        """本接口(UpdateTimeTemplate)用于更新时间模板。

        :param request: Request instance for UpdateTimeTemplate.
        :type request: :class:`tencentcloud.iotvideoindustry.v20201201.models.UpdateTimeTemplateRequest`
        :rtype: :class:`tencentcloud.iotvideoindustry.v20201201.models.UpdateTimeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTimeTemplate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateTimeTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)