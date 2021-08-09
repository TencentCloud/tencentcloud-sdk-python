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


class BunkZone(AbstractModel):
    """点位包含铺位信息

    """

    def __init__(self):
        """
        :param ZoneId: 点位ID\n        :type ZoneId: int\n        :param ZoneName: 点位名称\n        :type ZoneName: str\n        :param BunkCodes: 铺位编码\n        :type BunkCodes: str\n        """
        self.ZoneId = None
        self.ZoneName = None
        self.BunkCodes = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.BunkCodes = params.get("BunkCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CameraConfig(AbstractModel):
    """摄像头配置信息

    """

    def __init__(self):
        """
        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param MallId: 广场ID\n        :type MallId: int\n        :param FloorId: 楼层ID\n        :type FloorId: int\n        :param CameraId: 摄像头ID\n        :type CameraId: int\n        :param CameraIp: 摄像头IP\n        :type CameraIp: str\n        :param CameraMac: 摄像头Mac\n        :type CameraMac: str\n        :param CameraType: 摄像头类型:
1: 码流机
2: AI相机\n        :type CameraType: int\n        :param CameraFeature: 摄像头功能:
1: 人脸
2: 人体\n        :type CameraFeature: int\n        :param CameraState: 摄像头是否启用:
0: 下线
1: 启用\n        :type CameraState: int\n        :param ZoneId: 点位ID\n        :type ZoneId: int\n        :param ZoneType: 点位类型:
1: 场门
3: 层门
5: 特殊区域
7: 门店
8: 补位
10: 开放式门店
11: 品类区
12: 公共区\n        :type ZoneType: int\n        :param Config: 配置\n        :type Config: :class:`tencentcloud.ump.v20200918.models.Config`\n        :param Width: 宽\n        :type Width: int\n        :param Height: 高\n        :type Height: int\n        """
        self.GroupCode = None
        self.MallId = None
        self.FloorId = None
        self.CameraId = None
        self.CameraIp = None
        self.CameraMac = None
        self.CameraType = None
        self.CameraFeature = None
        self.CameraState = None
        self.ZoneId = None
        self.ZoneType = None
        self.Config = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.GroupCode = params.get("GroupCode")
        self.MallId = params.get("MallId")
        self.FloorId = params.get("FloorId")
        self.CameraId = params.get("CameraId")
        self.CameraIp = params.get("CameraIp")
        self.CameraMac = params.get("CameraMac")
        self.CameraType = params.get("CameraType")
        self.CameraFeature = params.get("CameraFeature")
        self.CameraState = params.get("CameraState")
        self.ZoneId = params.get("ZoneId")
        self.ZoneType = params.get("ZoneType")
        if params.get("Config") is not None:
            self.Config = Config()
            self.Config._deserialize(params.get("Config"))
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CameraState(AbstractModel):
    """用于场内上报当前相机的状态

    """

    def __init__(self):
        """
        :param CameraId: 相机ID\n        :type CameraId: int\n        :param State: 相机状态:
10: 初始化
11: 未知状态
12: 网络异常
13: 未授权
14: 相机App异常
15: 相机取流异常
16: 状态正常\n        :type State: int\n        """
        self.CameraId = None
        self.State = None


    def _deserialize(self, params):
        self.CameraId = params.get("CameraId")
        self.State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CameraZones(AbstractModel):
    """摄像头包含简单的点位信息

    """

    def __init__(self):
        """
        :param CameraId: 摄像头ID\n        :type CameraId: int\n        :param CameraName: 摄像头名称\n        :type CameraName: str\n        :param CameraFeature: 摄像头功能:
1: 人脸
2: 人体\n        :type CameraFeature: int\n        :param CameraIp: 摄像头IP\n        :type CameraIp: str\n        :param CameraState: 摄像头状态:
0: 异常 (不再使用)
1: 正常 (不再使用)
10: 初始化
11: 未知状态 (因服务内部错误产生)
12: 网络异常
13: 未授权
14: 相机App异常
15: 相机取流异常
16: 正常\n        :type CameraState: int\n        :param Zones: 点位列表\n        :type Zones: list of BunkZone\n        :param Pixel: 像素:
130W(1280*960)
200W(1920*1080)
400W(2560*1440)\n        :type Pixel: str\n        :param RTSP: 相机Rtsp地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type RTSP: str\n        """
        self.CameraId = None
        self.CameraName = None
        self.CameraFeature = None
        self.CameraIp = None
        self.CameraState = None
        self.Zones = None
        self.Pixel = None
        self.RTSP = None


    def _deserialize(self, params):
        self.CameraId = params.get("CameraId")
        self.CameraName = params.get("CameraName")
        self.CameraFeature = params.get("CameraFeature")
        self.CameraIp = params.get("CameraIp")
        self.CameraState = params.get("CameraState")
        if params.get("Zones") is not None:
            self.Zones = []
            for item in params.get("Zones"):
                obj = BunkZone()
                obj._deserialize(item)
                self.Zones.append(obj)
        self.Pixel = params.get("Pixel")
        self.RTSP = params.get("RTSP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Config(AbstractModel):
    """摄像头配置

    """

    def __init__(self):
        """
        :param CameraProducer: 摄像头厂商:
H: 海康
D: 大华
Y: 英飞拓
L: 联纵\n        :type CameraProducer: str\n        :param RTSP: rtsp 地址\n        :type RTSP: str\n        :param Fps: 摄像头帧率\n        :type Fps: int\n        :param DecodeFps: 解码帧率\n        :type DecodeFps: int\n        :param PassengerFlow: 是否做客流计算:
0: 否
1: 是\n        :type PassengerFlow: int\n        :param FaceExpose: 是否打开人脸曝光:
0: 关闭
1: 开启\n        :type FaceExpose: int\n        :param MallArea: 门线标注\n        :type MallArea: list of Point\n        :param ShopArea: 店门标注\n        :type ShopArea: list of Point\n        :param TrackAreas: 检测区标注\n        :type TrackAreas: list of Polygon\n        :param Zones: 点位列表（品类区）\n        :type Zones: list of ZoneArea\n        """
        self.CameraProducer = None
        self.RTSP = None
        self.Fps = None
        self.DecodeFps = None
        self.PassengerFlow = None
        self.FaceExpose = None
        self.MallArea = None
        self.ShopArea = None
        self.TrackAreas = None
        self.Zones = None


    def _deserialize(self, params):
        self.CameraProducer = params.get("CameraProducer")
        self.RTSP = params.get("RTSP")
        self.Fps = params.get("Fps")
        self.DecodeFps = params.get("DecodeFps")
        self.PassengerFlow = params.get("PassengerFlow")
        self.FaceExpose = params.get("FaceExpose")
        if params.get("MallArea") is not None:
            self.MallArea = []
            for item in params.get("MallArea"):
                obj = Point()
                obj._deserialize(item)
                self.MallArea.append(obj)
        if params.get("ShopArea") is not None:
            self.ShopArea = []
            for item in params.get("ShopArea"):
                obj = Point()
                obj._deserialize(item)
                self.ShopArea.append(obj)
        if params.get("TrackAreas") is not None:
            self.TrackAreas = []
            for item in params.get("TrackAreas"):
                obj = Polygon()
                obj._deserialize(item)
                self.TrackAreas.append(obj)
        if params.get("Zones") is not None:
            self.Zones = []
            for item in params.get("Zones"):
                obj = ZoneArea()
                obj._deserialize(item)
                self.Zones.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCameraAlertAlert(AbstractModel):
    """告警信息

    """

    def __init__(self):
        """
        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param MallId: 广场ID\n        :type MallId: int\n        :param CameraId: 相机ID\n        :type CameraId: int\n        :param CaptureTime: 时间戳,ms,默认为告警请求到达时间\n        :type CaptureTime: int\n        :param Image: 图片base64编码\n        :type Image: str\n        :param MoveAlert: 移动告警\n        :type MoveAlert: :class:`tencentcloud.ump.v20200918.models.CreateCameraAlertsMoveAlert`\n        :param CoverAlert: 遮挡告警\n        :type CoverAlert: :class:`tencentcloud.ump.v20200918.models.CreateCameraAlertsCoverAlert`\n        """
        self.GroupCode = None
        self.MallId = None
        self.CameraId = None
        self.CaptureTime = None
        self.Image = None
        self.MoveAlert = None
        self.CoverAlert = None


    def _deserialize(self, params):
        self.GroupCode = params.get("GroupCode")
        self.MallId = params.get("MallId")
        self.CameraId = params.get("CameraId")
        self.CaptureTime = params.get("CaptureTime")
        self.Image = params.get("Image")
        if params.get("MoveAlert") is not None:
            self.MoveAlert = CreateCameraAlertsMoveAlert()
            self.MoveAlert._deserialize(params.get("MoveAlert"))
        if params.get("CoverAlert") is not None:
            self.CoverAlert = CreateCameraAlertsCoverAlert()
            self.CoverAlert._deserialize(params.get("CoverAlert"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCameraAlertsCoverAlert(AbstractModel):
    """遮挡告警

    """

    def __init__(self):
        """
        :param Cover: 是否遮挡\n        :type Cover: bool\n        :param CoverConfidence: 是否移动置信度\n        :type CoverConfidence: float\n        """
        self.Cover = None
        self.CoverConfidence = None


    def _deserialize(self, params):
        self.Cover = params.get("Cover")
        self.CoverConfidence = params.get("CoverConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCameraAlertsMoveAlert(AbstractModel):
    """移动告警

    """

    def __init__(self):
        """
        :param Move: 是否移动\n        :type Move: bool\n        :param MoveConfidence: 是否移动置信度\n        :type MoveConfidence: float\n        """
        self.Move = None
        self.MoveConfidence = None


    def _deserialize(self, params):
        self.Move = params.get("Move")
        self.MoveConfidence = params.get("MoveConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCameraAlertsRequest(AbstractModel):
    """CreateCameraAlerts请求参数结构体

    """

    def __init__(self):
        """
        :param Alerts: 告警信息列表\n        :type Alerts: list of CreateCameraAlertAlert\n        """
        self.Alerts = None


    def _deserialize(self, params):
        if params.get("Alerts") is not None:
            self.Alerts = []
            for item in params.get("Alerts"):
                obj = CreateCameraAlertAlert()
                obj._deserialize(item)
                self.Alerts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCameraAlertsResponse(AbstractModel):
    """CreateCameraAlerts返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateCameraStateRequest(AbstractModel):
    """CreateCameraState请求参数结构体

    """

    def __init__(self):
        """
        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param MallId: 广场ID\n        :type MallId: int\n        :param CameraStates: 场内所有相机的状态值\n        :type CameraStates: list of CameraState\n        """
        self.GroupCode = None
        self.MallId = None
        self.CameraStates = None


    def _deserialize(self, params):
        self.GroupCode = params.get("GroupCode")
        self.MallId = params.get("MallId")
        if params.get("CameraStates") is not None:
            self.CameraStates = []
            for item in params.get("CameraStates"):
                obj = CameraState()
                obj._deserialize(item)
                self.CameraStates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCameraStateResponse(AbstractModel):
    """CreateCameraState返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateCaptureRequest(AbstractModel):
    """CreateCapture请求参数结构体

    """

    def __init__(self):
        """
        :param Data: 原始抓拍报文\n        :type Data: str\n        """
        self.Data = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCaptureResponse(AbstractModel):
    """CreateCapture返回参数结构体

    """

    def __init__(self):
        """
        :param RspData: 原始应答报文
注意：此字段可能返回 null，表示取不到有效值。\n        :type RspData: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RspData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RspData = params.get("RspData")
        self.RequestId = params.get("RequestId")


class CreateMultiBizAlertRequest(AbstractModel):
    """CreateMultiBizAlert请求参数结构体

    """

    def __init__(self):
        """
        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param MallId: 广场ID\n        :type MallId: int\n        :param ZoneId: 点位ID\n        :type ZoneId: int\n        :param CameraId: 摄像头ID\n        :type CameraId: int\n        :param CaptureTime: 时间戳，毫秒\n        :type CaptureTime: int\n        :param State: 状态: 
1: 侵占
2: 消失
3: 即侵占又消失\n        :type State: int\n        :param Image: 图片base64字符串\n        :type Image: str\n        :param Warnings: 告警列表\n        :type Warnings: list of MultiBizWarning\n        """
        self.GroupCode = None
        self.MallId = None
        self.ZoneId = None
        self.CameraId = None
        self.CaptureTime = None
        self.State = None
        self.Image = None
        self.Warnings = None


    def _deserialize(self, params):
        self.GroupCode = params.get("GroupCode")
        self.MallId = params.get("MallId")
        self.ZoneId = params.get("ZoneId")
        self.CameraId = params.get("CameraId")
        self.CaptureTime = params.get("CaptureTime")
        self.State = params.get("State")
        self.Image = params.get("Image")
        if params.get("Warnings") is not None:
            self.Warnings = []
            for item in params.get("Warnings"):
                obj = MultiBizWarning()
                obj._deserialize(item)
                self.Warnings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMultiBizAlertResponse(AbstractModel):
    """CreateMultiBizAlert返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateProgramStateRequest(AbstractModel):
    """CreateProgramState请求参数结构体

    """

    def __init__(self):
        """
        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param ProgramStateItems: 进程监控信息列表\n        :type ProgramStateItems: list of ProgramStateItem\n        :param MallId: 商场ID\n        :type MallId: int\n        """
        self.GroupCode = None
        self.ProgramStateItems = None
        self.MallId = None


    def _deserialize(self, params):
        self.GroupCode = params.get("GroupCode")
        if params.get("ProgramStateItems") is not None:
            self.ProgramStateItems = []
            for item in params.get("ProgramStateItems"):
                obj = ProgramStateItem()
                obj._deserialize(item)
                self.ProgramStateItems.append(obj)
        self.MallId = params.get("MallId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProgramStateResponse(AbstractModel):
    """CreateProgramState返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateServerStateRequest(AbstractModel):
    """CreateServerState请求参数结构体

    """

    def __init__(self):
        """
        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param ServerStateItems: 服务器监控信息列表\n        :type ServerStateItems: list of ServerStateItem\n        :param MallId: 商场ID\n        :type MallId: int\n        :param ReportTime: 服务器监控信息上报时间戳，单位毫秒\n        :type ReportTime: int\n        """
        self.GroupCode = None
        self.ServerStateItems = None
        self.MallId = None
        self.ReportTime = None


    def _deserialize(self, params):
        self.GroupCode = params.get("GroupCode")
        if params.get("ServerStateItems") is not None:
            self.ServerStateItems = []
            for item in params.get("ServerStateItems"):
                obj = ServerStateItem()
                obj._deserialize(item)
                self.ServerStateItems.append(obj)
        self.MallId = params.get("MallId")
        self.ReportTime = params.get("ReportTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServerStateResponse(AbstractModel):
    """CreateServerState返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMultiBizAlertRequest(AbstractModel):
    """DeleteMultiBizAlert请求参数结构体

    """

    def __init__(self):
        """
        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param MallId: 广场ID\n        :type MallId: int\n        :param ZoneId: 点位ID\n        :type ZoneId: int\n        :param CameraId: 摄像头ID\n        :type CameraId: int\n        :param ActionType: 消警动作:
1: 误报
2: 正报合规
3: 正报不合规，整改完成\n        :type ActionType: int\n        :param Image: 图片base64字符串\n        :type Image: str\n        """
        self.GroupCode = None
        self.MallId = None
        self.ZoneId = None
        self.CameraId = None
        self.ActionType = None
        self.Image = None


    def _deserialize(self, params):
        self.GroupCode = params.get("GroupCode")
        self.MallId = params.get("MallId")
        self.ZoneId = params.get("ZoneId")
        self.CameraId = params.get("CameraId")
        self.ActionType = params.get("ActionType")
        self.Image = params.get("Image")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMultiBizAlertResponse(AbstractModel):
    """DeleteMultiBizAlert返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTaskRequest(AbstractModel):
    """DeleteTask请求参数结构体

    """

    def __init__(self):
        """
        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param MallId: 广场ID\n        :type MallId: int\n        :param TaskId: 任务ID\n        :type TaskId: int\n        """
        self.GroupCode = None
        self.MallId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.GroupCode = params.get("GroupCode")
        self.MallId = params.get("MallId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTaskResponse(AbstractModel):
    """DeleteTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCamerasRequest(AbstractModel):
    """DescribeCameras请求参数结构体

    """

    def __init__(self):
        """
        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param MallId: 广场ID\n        :type MallId: int\n        """
        self.GroupCode = None
        self.MallId = None


    def _deserialize(self, params):
        self.GroupCode = params.get("GroupCode")
        self.MallId = params.get("MallId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCamerasResponse(AbstractModel):
    """DescribeCameras返回参数结构体

    """

    def __init__(self):
        """
        :param Cameras: 摄像头列表\n        :type Cameras: list of CameraZones\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Cameras = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Cameras") is not None:
            self.Cameras = []
            for item in params.get("Cameras"):
                obj = CameraZones()
                obj._deserialize(item)
                self.Cameras.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeConfigRequest(AbstractModel):
    """DescribeConfig请求参数结构体

    """

    def __init__(self):
        """
        :param SessionId: 会话ID\n        :type SessionId: str\n        :param CameraSign: 摄像头签名\n        :type CameraSign: str\n        :param CameraAppId: 摄像头app id\n        :type CameraAppId: str\n        :param CameraTimestamp: 摄像头时间戳，毫秒\n        :type CameraTimestamp: int\n        :param ServerMac: MAC地址，字母大写\n        :type ServerMac: str\n        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param MallId: 广场ID\n        :type MallId: int\n        """
        self.SessionId = None
        self.CameraSign = None
        self.CameraAppId = None
        self.CameraTimestamp = None
        self.ServerMac = None
        self.GroupCode = None
        self.MallId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.CameraSign = params.get("CameraSign")
        self.CameraAppId = params.get("CameraAppId")
        self.CameraTimestamp = params.get("CameraTimestamp")
        self.ServerMac = params.get("ServerMac")
        self.GroupCode = params.get("GroupCode")
        self.MallId = params.get("MallId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigResponse(AbstractModel):
    """DescribeConfig返回参数结构体

    """

    def __init__(self):
        """
        :param SessionId: 会话ID\n        :type SessionId: str\n        :param Version: 配置版本号\n        :type Version: int\n        :param Cameras: 摄像头列表\n        :type Cameras: list of CameraConfig\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SessionId = None
        self.Version = None
        self.Cameras = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.Version = params.get("Version")
        if params.get("Cameras") is not None:
            self.Cameras = []
            for item in params.get("Cameras"):
                obj = CameraConfig()
                obj._deserialize(item)
                self.Cameras.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImageRequest(AbstractModel):
    """DescribeImage请求参数结构体

    """

    def __init__(self):
        """
        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param MallId: 广场ID\n        :type MallId: int\n        :param CameraId: 摄像头ID\n        :type CameraId: int\n        """
        self.GroupCode = None
        self.MallId = None
        self.CameraId = None


    def _deserialize(self, params):
        self.GroupCode = params.get("GroupCode")
        self.MallId = params.get("MallId")
        self.CameraId = params.get("CameraId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageResponse(AbstractModel):
    """DescribeImage返回参数结构体

    """

    def __init__(self):
        """
        :param ImageUrl: cos 临时 url，异步上传图片，client需要轮询\n        :type ImageUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ImageUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.RequestId = params.get("RequestId")


class DescribeMultiBizBaseImageRequest(AbstractModel):
    """DescribeMultiBizBaseImage请求参数结构体

    """

    def __init__(self):
        """
        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param MallId: 广场ID\n        :type MallId: int\n        :param CameraId: 摄像头ID\n        :type CameraId: int\n        :param ZoneId: 点位ID\n        :type ZoneId: int\n        """
        self.GroupCode = None
        self.MallId = None
        self.CameraId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.GroupCode = params.get("GroupCode")
        self.MallId = params.get("MallId")
        self.CameraId = params.get("CameraId")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMultiBizBaseImageResponse(AbstractModel):
    """DescribeMultiBizBaseImage返回参数结构体

    """

    def __init__(self):
        """
        :param ImageUrl: cos 临时 url\n        :type ImageUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ImageUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        """
        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param MallId: 广场ID\n        :type MallId: int\n        :param TaskType: 任务类型:
1: 底图拉取\n        :type TaskType: int\n        """
        self.GroupCode = None
        self.MallId = None
        self.TaskType = None


    def _deserialize(self, params):
        self.GroupCode = params.get("GroupCode")
        self.MallId = params.get("MallId")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        """
        :param Tasks: 任务列表\n        :type Tasks: list of Task\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """

    def __init__(self):
        """
        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param MallId: 广场ID\n        :type MallId: int\n        """
        self.GroupCode = None
        self.MallId = None


    def _deserialize(self, params):
        self.GroupCode = params.get("GroupCode")
        self.MallId = params.get("MallId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        """
        :param Zones: 点位列表\n        :type Zones: list of ZoneConfig\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Zones = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Zones") is not None:
            self.Zones = []
            for item in params.get("Zones"):
                obj = ZoneConfig()
                obj._deserialize(item)
                self.Zones.append(obj)
        self.RequestId = params.get("RequestId")


class DiskInfo(AbstractModel):
    """硬盘监控信息

    """

    def __init__(self):
        """
        :param DiskName: 硬盘名字\n        :type DiskName: str\n        :param Usage: 硬盘使用率\n        :type Usage: float\n        """
        self.DiskName = None
        self.Usage = None


    def _deserialize(self, params):
        self.DiskName = params.get("DiskName")
        self.Usage = params.get("Usage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMultiBizConfigRequest(AbstractModel):
    """ModifyMultiBizConfig请求参数结构体

    """

    def __init__(self):
        """
        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param MallId: 广场ID\n        :type MallId: int\n        :param ZoneId: 点位ID\n        :type ZoneId: int\n        :param CameraId: 摄像头ID\n        :type CameraId: int\n        :param MonitoringAreas: 监控区域\n        :type MonitoringAreas: list of Polygon\n        """
        self.GroupCode = None
        self.MallId = None
        self.ZoneId = None
        self.CameraId = None
        self.MonitoringAreas = None


    def _deserialize(self, params):
        self.GroupCode = params.get("GroupCode")
        self.MallId = params.get("MallId")
        self.ZoneId = params.get("ZoneId")
        self.CameraId = params.get("CameraId")
        if params.get("MonitoringAreas") is not None:
            self.MonitoringAreas = []
            for item in params.get("MonitoringAreas"):
                obj = Polygon()
                obj._deserialize(item)
                self.MonitoringAreas.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMultiBizConfigResponse(AbstractModel):
    """ModifyMultiBizConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MultiBizWarning(AbstractModel):
    """多经点位告警

    """

    def __init__(self):
        """
        :param Id: 编号\n        :type Id: int\n        :param MonitoringArea: 监控区域\n        :type MonitoringArea: list of Point\n        :param WarningInfos: 告警列表\n        :type WarningInfos: list of MultiBizWarningInfo\n        """
        self.Id = None
        self.MonitoringArea = None
        self.WarningInfos = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        if params.get("MonitoringArea") is not None:
            self.MonitoringArea = []
            for item in params.get("MonitoringArea"):
                obj = Point()
                obj._deserialize(item)
                self.MonitoringArea.append(obj)
        if params.get("WarningInfos") is not None:
            self.WarningInfos = []
            for item in params.get("WarningInfos"):
                obj = MultiBizWarningInfo()
                obj._deserialize(item)
                self.WarningInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiBizWarningInfo(AbstractModel):
    """多经点位告警信息

    """

    def __init__(self):
        """
        :param WarningType: 告警类型：
0: 无变化
1: 侵占
2: 消失\n        :type WarningType: int\n        :param WarningAreaSize: 告警侵占或消失面积\n        :type WarningAreaSize: float\n        :param WarningLocation: 告警侵占或消失坐标\n        :type WarningLocation: :class:`tencentcloud.ump.v20200918.models.Point`\n        :param WarningAreaContour: 告警侵占或消失轮廓\n        :type WarningAreaContour: list of Point\n        """
        self.WarningType = None
        self.WarningAreaSize = None
        self.WarningLocation = None
        self.WarningAreaContour = None


    def _deserialize(self, params):
        self.WarningType = params.get("WarningType")
        self.WarningAreaSize = params.get("WarningAreaSize")
        if params.get("WarningLocation") is not None:
            self.WarningLocation = Point()
            self.WarningLocation._deserialize(params.get("WarningLocation"))
        if params.get("WarningAreaContour") is not None:
            self.WarningAreaContour = []
            for item in params.get("WarningAreaContour"):
                obj = Point()
                obj._deserialize(item)
                self.WarningAreaContour.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Point(AbstractModel):
    """点

    """

    def __init__(self):
        """
        :param X: X坐标\n        :type X: int\n        :param Y: Y坐标\n        :type Y: int\n        """
        self.X = None
        self.Y = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Polygon(AbstractModel):
    """多边形

    """

    def __init__(self):
        """
        :param Points: 标注列表\n        :type Points: list of Point\n        """
        self.Points = None


    def _deserialize(self, params):
        if params.get("Points") is not None:
            self.Points = []
            for item in params.get("Points"):
                obj = Point()
                obj._deserialize(item)
                self.Points.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProgramStateItem(AbstractModel):
    """进程状态监控项

    """

    def __init__(self):
        """
        :param ServerIp: 服务器IP\n        :type ServerIp: str\n        :param ProgramName: 进程名字\n        :type ProgramName: str\n        :param OnlineCount: 在线个数\n        :type OnlineCount: int\n        :param OfflineCount: 离线个数\n        :type OfflineCount: int\n        :param State: 上报状态:
1: 正常上报
2: 异常上报
注：此处异常上报是指本次上报由于场内服务内部原因导致上报数据不可信等。此时离线个数重置为1，在线个数重置为0\n        :type State: int\n        """
        self.ServerIp = None
        self.ProgramName = None
        self.OnlineCount = None
        self.OfflineCount = None
        self.State = None


    def _deserialize(self, params):
        self.ServerIp = params.get("ServerIp")
        self.ProgramName = params.get("ProgramName")
        self.OnlineCount = params.get("OnlineCount")
        self.OfflineCount = params.get("OfflineCount")
        self.State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportServiceRegisterRequest(AbstractModel):
    """ReportServiceRegister请求参数结构体

    """

    def __init__(self):
        """
        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param MallId: 广场ID\n        :type MallId: int\n        :param ServiceRegisterInfos: 服务上报当前的服务能力信息\n        :type ServiceRegisterInfos: list of ServiceRegisterInfo\n        :param ServerIp: 服务内网Ip\n        :type ServerIp: str\n        :param ServerNodeId: 上报服务所在服务器的唯一ID\n        :type ServerNodeId: str\n        :param ReportTime: 上报时间戳, 单位毫秒\n        :type ReportTime: int\n        """
        self.GroupCode = None
        self.MallId = None
        self.ServiceRegisterInfos = None
        self.ServerIp = None
        self.ServerNodeId = None
        self.ReportTime = None


    def _deserialize(self, params):
        self.GroupCode = params.get("GroupCode")
        self.MallId = params.get("MallId")
        if params.get("ServiceRegisterInfos") is not None:
            self.ServiceRegisterInfos = []
            for item in params.get("ServiceRegisterInfos"):
                obj = ServiceRegisterInfo()
                obj._deserialize(item)
                self.ServiceRegisterInfos.append(obj)
        self.ServerIp = params.get("ServerIp")
        self.ServerNodeId = params.get("ServerNodeId")
        self.ReportTime = params.get("ReportTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportServiceRegisterResponse(AbstractModel):
    """ReportServiceRegister返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SearchImageRequest(AbstractModel):
    """SearchImage请求参数结构体

    """

    def __init__(self):
        """
        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param MallId: 广场ID\n        :type MallId: int\n        :param Image: 图片base64字符串\n        :type Image: str\n        :param ImageTime: 时间戳，毫秒\n        :type ImageTime: int\n        """
        self.GroupCode = None
        self.MallId = None
        self.Image = None
        self.ImageTime = None


    def _deserialize(self, params):
        self.GroupCode = params.get("GroupCode")
        self.MallId = params.get("MallId")
        self.Image = params.get("Image")
        self.ImageTime = params.get("ImageTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchImageResponse(AbstractModel):
    """SearchImage返回参数结构体

    """

    def __init__(self):
        """
        :param FaceId: face id\n        :type FaceId: str\n        :param Results: 搜索结果列表\n        :type Results: list of SearchResult\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FaceId = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FaceId = params.get("FaceId")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = SearchResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class SearchResult(AbstractModel):
    """以图搜图检索结果

    """

    def __init__(self):
        """
        :param Image: 图片base64数据\n        :type Image: str\n        :param PersonId: 身份ID\n        :type PersonId: str\n        :param Similarity: 相似度\n        :type Similarity: float\n        """
        self.Image = None
        self.PersonId = None
        self.Similarity = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.PersonId = params.get("PersonId")
        self.Similarity = params.get("Similarity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerStateItem(AbstractModel):
    """服务器监控状态上报项

    """

    def __init__(self):
        """
        :param ServerState: 服务器状态
1: 在线
2: 离线
3: 重启\n        :type ServerState: int\n        :param ServerIp: 服务器IP\n        :type ServerIp: str\n        :param DiskInfos: 硬盘监控信息列表\n        :type DiskInfos: list of DiskInfo\n        """
        self.ServerState = None
        self.ServerIp = None
        self.DiskInfos = None


    def _deserialize(self, params):
        self.ServerState = params.get("ServerState")
        self.ServerIp = params.get("ServerIp")
        if params.get("DiskInfos") is not None:
            self.DiskInfos = []
            for item in params.get("DiskInfos"):
                obj = DiskInfo()
                obj._deserialize(item)
                self.DiskInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceRegisterInfo(AbstractModel):
    """用于服务注册时表示当前服务的具体信息

    """

    def __init__(self):
        """
        :param CgiUrl: 当前服务的回调地址\n        :type CgiUrl: str\n        :param ServiceType: 当前服务类型:
1: 多经服务
2: 相机误报警确认
3: 底图更新\n        :type ServiceType: int\n        """
        self.CgiUrl = None
        self.ServiceType = None


    def _deserialize(self, params):
        self.CgiUrl = params.get("CgiUrl")
        self.ServiceType = params.get("ServiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """任务信息

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param GroupCode: 集团编码\n        :type GroupCode: str\n        :param MallId: 广场ID\n        :type MallId: int\n        :param TaskContent: 任务内容\n        :type TaskContent: :class:`tencentcloud.ump.v20200918.models.TaskContent`\n        :param TaskType: 任务类型:
1: 底图拉取\n        :type TaskType: int\n        """
        self.TaskId = None
        self.GroupCode = None
        self.MallId = None
        self.TaskContent = None
        self.TaskType = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.GroupCode = params.get("GroupCode")
        self.MallId = params.get("MallId")
        if params.get("TaskContent") is not None:
            self.TaskContent = TaskContent()
            self.TaskContent._deserialize(params.get("TaskContent"))
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskContent(AbstractModel):
    """任务内容

    """

    def __init__(self):
        """
        :param CameraId: 摄像头ID\n        :type CameraId: int\n        :param RTSP: rtsp 地址\n        :type RTSP: str\n        :param Url: 图片上传地址\n        :type Url: str\n        """
        self.CameraId = None
        self.RTSP = None
        self.Url = None


    def _deserialize(self, params):
        self.CameraId = params.get("CameraId")
        self.RTSP = params.get("RTSP")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneArea(AbstractModel):
    """点位包含店门标注

    """

    def __init__(self):
        """
        :param ZoneId: 点位ID\n        :type ZoneId: int\n        :param ShopArea: 店门标注\n        :type ShopArea: list of Point\n        """
        self.ZoneId = None
        self.ShopArea = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("ShopArea") is not None:
            self.ShopArea = []
            for item in params.get("ShopArea"):
                obj = Point()
                obj._deserialize(item)
                self.ShopArea.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneConfig(AbstractModel):
    """点位包含绑定、调试信息

    """

    def __init__(self):
        """
        :param ZoneId: 点位ID\n        :type ZoneId: int\n        :param ZoneName: 点位名称\n        :type ZoneName: str\n        :param ZoneType: 点位类型:
1: 场门
3: 层门
5: 特殊区域
7: 门店
8: 补位
10: 开放式门店
11: 品类区
12: 公共区\n        :type ZoneType: int\n        :param BunkCodes: 铺位编码\n        :type BunkCodes: str\n        :param FloorName: 楼层名称\n        :type FloorName: str\n        :param FloorId: 楼层ID\n        :type FloorId: int\n        :param BindNum: 绑定数\n        :type BindNum: int\n        :param DebugNum: 调试数\n        :type DebugNum: int\n        :param State: 下发状态:
1: 不可下发
2: 可下发
3: 已下发\n        :type State: int\n        """
        self.ZoneId = None
        self.ZoneName = None
        self.ZoneType = None
        self.BunkCodes = None
        self.FloorName = None
        self.FloorId = None
        self.BindNum = None
        self.DebugNum = None
        self.State = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.ZoneType = params.get("ZoneType")
        self.BunkCodes = params.get("BunkCodes")
        self.FloorName = params.get("FloorName")
        self.FloorId = params.get("FloorId")
        self.BindNum = params.get("BindNum")
        self.DebugNum = params.get("DebugNum")
        self.State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        