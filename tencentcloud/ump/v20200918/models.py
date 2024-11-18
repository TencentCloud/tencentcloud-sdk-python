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
        r"""
        :param _ZoneId: 点位ID
        :type ZoneId: int
        :param _ZoneName: 点位名称
        :type ZoneName: str
        :param _BunkCodes: 铺位编码
        :type BunkCodes: str
        """
        self._ZoneId = None
        self._ZoneName = None
        self._BunkCodes = None

    @property
    def ZoneId(self):
        """点位ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """点位名称
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def BunkCodes(self):
        """铺位编码
        :rtype: str
        """
        return self._BunkCodes

    @BunkCodes.setter
    def BunkCodes(self, BunkCodes):
        self._BunkCodes = BunkCodes


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._BunkCodes = params.get("BunkCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CameraConfig(AbstractModel):
    """摄像头配置信息

    """

    def __init__(self):
        r"""
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _MallId: 广场ID
        :type MallId: int
        :param _FloorId: 楼层ID
        :type FloorId: int
        :param _CameraId: 摄像头ID
        :type CameraId: int
        :param _CameraIp: 摄像头IP
        :type CameraIp: str
        :param _CameraMac: 摄像头Mac
        :type CameraMac: str
        :param _CameraType: 摄像头类型:
1: 码流机
2: AI相机
        :type CameraType: int
        :param _CameraFeature: 摄像头功能:
1: 人脸
2: 人体
        :type CameraFeature: int
        :param _CameraState: 摄像头是否启用:
0: 下线
1: 启用
        :type CameraState: int
        :param _ZoneId: 点位ID
        :type ZoneId: int
        :param _ZoneType: 点位类型:
1: 场门
3: 层门
5: 特殊区域
7: 门店
8: 补位
10: 开放式门店
11: 品类区
12: 公共区
        :type ZoneType: int
        :param _Config: 配置
        :type Config: :class:`tencentcloud.ump.v20200918.models.Config`
        :param _Width: 宽
        :type Width: int
        :param _Height: 高
        :type Height: int
        """
        self._GroupCode = None
        self._MallId = None
        self._FloorId = None
        self._CameraId = None
        self._CameraIp = None
        self._CameraMac = None
        self._CameraType = None
        self._CameraFeature = None
        self._CameraState = None
        self._ZoneId = None
        self._ZoneType = None
        self._Config = None
        self._Width = None
        self._Height = None

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def MallId(self):
        """广场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def FloorId(self):
        """楼层ID
        :rtype: int
        """
        return self._FloorId

    @FloorId.setter
    def FloorId(self, FloorId):
        self._FloorId = FloorId

    @property
    def CameraId(self):
        """摄像头ID
        :rtype: int
        """
        return self._CameraId

    @CameraId.setter
    def CameraId(self, CameraId):
        self._CameraId = CameraId

    @property
    def CameraIp(self):
        """摄像头IP
        :rtype: str
        """
        return self._CameraIp

    @CameraIp.setter
    def CameraIp(self, CameraIp):
        self._CameraIp = CameraIp

    @property
    def CameraMac(self):
        """摄像头Mac
        :rtype: str
        """
        return self._CameraMac

    @CameraMac.setter
    def CameraMac(self, CameraMac):
        self._CameraMac = CameraMac

    @property
    def CameraType(self):
        """摄像头类型:
1: 码流机
2: AI相机
        :rtype: int
        """
        return self._CameraType

    @CameraType.setter
    def CameraType(self, CameraType):
        self._CameraType = CameraType

    @property
    def CameraFeature(self):
        """摄像头功能:
1: 人脸
2: 人体
        :rtype: int
        """
        return self._CameraFeature

    @CameraFeature.setter
    def CameraFeature(self, CameraFeature):
        self._CameraFeature = CameraFeature

    @property
    def CameraState(self):
        """摄像头是否启用:
0: 下线
1: 启用
        :rtype: int
        """
        return self._CameraState

    @CameraState.setter
    def CameraState(self, CameraState):
        self._CameraState = CameraState

    @property
    def ZoneId(self):
        """点位ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneType(self):
        """点位类型:
1: 场门
3: 层门
5: 特殊区域
7: 门店
8: 补位
10: 开放式门店
11: 品类区
12: 公共区
        :rtype: int
        """
        return self._ZoneType

    @ZoneType.setter
    def ZoneType(self, ZoneType):
        self._ZoneType = ZoneType

    @property
    def Config(self):
        """配置
        :rtype: :class:`tencentcloud.ump.v20200918.models.Config`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Width(self):
        """宽
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """高
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._GroupCode = params.get("GroupCode")
        self._MallId = params.get("MallId")
        self._FloorId = params.get("FloorId")
        self._CameraId = params.get("CameraId")
        self._CameraIp = params.get("CameraIp")
        self._CameraMac = params.get("CameraMac")
        self._CameraType = params.get("CameraType")
        self._CameraFeature = params.get("CameraFeature")
        self._CameraState = params.get("CameraState")
        self._ZoneId = params.get("ZoneId")
        self._ZoneType = params.get("ZoneType")
        if params.get("Config") is not None:
            self._Config = Config()
            self._Config._deserialize(params.get("Config"))
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CameraState(AbstractModel):
    """用于场内上报当前相机的状态

    """

    def __init__(self):
        r"""
        :param _CameraId: 相机ID
        :type CameraId: int
        :param _State: 相机状态:
10: 初始化
11: 未知状态
12: 网络异常
13: 未授权
14: 相机App异常
15: 相机取流异常
16: 状态正常
        :type State: int
        """
        self._CameraId = None
        self._State = None

    @property
    def CameraId(self):
        """相机ID
        :rtype: int
        """
        return self._CameraId

    @CameraId.setter
    def CameraId(self, CameraId):
        self._CameraId = CameraId

    @property
    def State(self):
        """相机状态:
10: 初始化
11: 未知状态
12: 网络异常
13: 未授权
14: 相机App异常
15: 相机取流异常
16: 状态正常
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._CameraId = params.get("CameraId")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CameraZones(AbstractModel):
    """摄像头包含简单的点位信息

    """

    def __init__(self):
        r"""
        :param _CameraId: 摄像头ID
        :type CameraId: int
        :param _CameraName: 摄像头名称
        :type CameraName: str
        :param _CameraFeature: 摄像头功能:
1: 人脸
2: 人体
        :type CameraFeature: int
        :param _CameraIp: 摄像头IP
        :type CameraIp: str
        :param _CameraState: 摄像头状态:
0: 异常 (不再使用)
1: 正常 (不再使用)
10: 初始化
11: 未知状态 (因服务内部错误产生)
12: 网络异常
13: 未授权
14: 相机App异常
15: 相机取流异常
16: 正常
        :type CameraState: int
        :param _Zones: 点位列表
        :type Zones: list of BunkZone
        :param _Pixel: 像素:
130W(1280*960)
200W(1920*1080)
400W(2560*1440)
        :type Pixel: str
        :param _RTSP: 相机Rtsp地址
注意：此字段可能返回 null，表示取不到有效值。
        :type RTSP: str
        """
        self._CameraId = None
        self._CameraName = None
        self._CameraFeature = None
        self._CameraIp = None
        self._CameraState = None
        self._Zones = None
        self._Pixel = None
        self._RTSP = None

    @property
    def CameraId(self):
        """摄像头ID
        :rtype: int
        """
        return self._CameraId

    @CameraId.setter
    def CameraId(self, CameraId):
        self._CameraId = CameraId

    @property
    def CameraName(self):
        """摄像头名称
        :rtype: str
        """
        return self._CameraName

    @CameraName.setter
    def CameraName(self, CameraName):
        self._CameraName = CameraName

    @property
    def CameraFeature(self):
        """摄像头功能:
1: 人脸
2: 人体
        :rtype: int
        """
        return self._CameraFeature

    @CameraFeature.setter
    def CameraFeature(self, CameraFeature):
        self._CameraFeature = CameraFeature

    @property
    def CameraIp(self):
        """摄像头IP
        :rtype: str
        """
        return self._CameraIp

    @CameraIp.setter
    def CameraIp(self, CameraIp):
        self._CameraIp = CameraIp

    @property
    def CameraState(self):
        """摄像头状态:
0: 异常 (不再使用)
1: 正常 (不再使用)
10: 初始化
11: 未知状态 (因服务内部错误产生)
12: 网络异常
13: 未授权
14: 相机App异常
15: 相机取流异常
16: 正常
        :rtype: int
        """
        return self._CameraState

    @CameraState.setter
    def CameraState(self, CameraState):
        self._CameraState = CameraState

    @property
    def Zones(self):
        """点位列表
        :rtype: list of BunkZone
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def Pixel(self):
        """像素:
130W(1280*960)
200W(1920*1080)
400W(2560*1440)
        :rtype: str
        """
        return self._Pixel

    @Pixel.setter
    def Pixel(self, Pixel):
        self._Pixel = Pixel

    @property
    def RTSP(self):
        """相机Rtsp地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RTSP

    @RTSP.setter
    def RTSP(self, RTSP):
        self._RTSP = RTSP


    def _deserialize(self, params):
        self._CameraId = params.get("CameraId")
        self._CameraName = params.get("CameraName")
        self._CameraFeature = params.get("CameraFeature")
        self._CameraIp = params.get("CameraIp")
        self._CameraState = params.get("CameraState")
        if params.get("Zones") is not None:
            self._Zones = []
            for item in params.get("Zones"):
                obj = BunkZone()
                obj._deserialize(item)
                self._Zones.append(obj)
        self._Pixel = params.get("Pixel")
        self._RTSP = params.get("RTSP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Config(AbstractModel):
    """摄像头配置

    """

    def __init__(self):
        r"""
        :param _CameraProducer: 摄像头厂商:
H: 海康
D: 大华
Y: 英飞拓
L: 联纵
        :type CameraProducer: str
        :param _RTSP: rtsp 地址
        :type RTSP: str
        :param _Fps: 摄像头帧率
        :type Fps: int
        :param _DecodeFps: 解码帧率
        :type DecodeFps: int
        :param _PassengerFlow: 是否做客流计算:
0: 否
1: 是
        :type PassengerFlow: int
        :param _FaceExpose: 是否打开人脸曝光:
0: 关闭
1: 开启
        :type FaceExpose: int
        :param _MallArea: 门线标注
        :type MallArea: list of Point
        :param _ShopArea: 店门标注
        :type ShopArea: list of Point
        :param _TrackAreas: 检测区标注
        :type TrackAreas: list of Polygon
        :param _Zones: 点位列表（品类区）
        :type Zones: list of ZoneArea
        """
        self._CameraProducer = None
        self._RTSP = None
        self._Fps = None
        self._DecodeFps = None
        self._PassengerFlow = None
        self._FaceExpose = None
        self._MallArea = None
        self._ShopArea = None
        self._TrackAreas = None
        self._Zones = None

    @property
    def CameraProducer(self):
        """摄像头厂商:
H: 海康
D: 大华
Y: 英飞拓
L: 联纵
        :rtype: str
        """
        return self._CameraProducer

    @CameraProducer.setter
    def CameraProducer(self, CameraProducer):
        self._CameraProducer = CameraProducer

    @property
    def RTSP(self):
        """rtsp 地址
        :rtype: str
        """
        return self._RTSP

    @RTSP.setter
    def RTSP(self, RTSP):
        self._RTSP = RTSP

    @property
    def Fps(self):
        """摄像头帧率
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def DecodeFps(self):
        """解码帧率
        :rtype: int
        """
        return self._DecodeFps

    @DecodeFps.setter
    def DecodeFps(self, DecodeFps):
        self._DecodeFps = DecodeFps

    @property
    def PassengerFlow(self):
        """是否做客流计算:
0: 否
1: 是
        :rtype: int
        """
        return self._PassengerFlow

    @PassengerFlow.setter
    def PassengerFlow(self, PassengerFlow):
        self._PassengerFlow = PassengerFlow

    @property
    def FaceExpose(self):
        """是否打开人脸曝光:
0: 关闭
1: 开启
        :rtype: int
        """
        return self._FaceExpose

    @FaceExpose.setter
    def FaceExpose(self, FaceExpose):
        self._FaceExpose = FaceExpose

    @property
    def MallArea(self):
        """门线标注
        :rtype: list of Point
        """
        return self._MallArea

    @MallArea.setter
    def MallArea(self, MallArea):
        self._MallArea = MallArea

    @property
    def ShopArea(self):
        """店门标注
        :rtype: list of Point
        """
        return self._ShopArea

    @ShopArea.setter
    def ShopArea(self, ShopArea):
        self._ShopArea = ShopArea

    @property
    def TrackAreas(self):
        """检测区标注
        :rtype: list of Polygon
        """
        return self._TrackAreas

    @TrackAreas.setter
    def TrackAreas(self, TrackAreas):
        self._TrackAreas = TrackAreas

    @property
    def Zones(self):
        """点位列表（品类区）
        :rtype: list of ZoneArea
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones


    def _deserialize(self, params):
        self._CameraProducer = params.get("CameraProducer")
        self._RTSP = params.get("RTSP")
        self._Fps = params.get("Fps")
        self._DecodeFps = params.get("DecodeFps")
        self._PassengerFlow = params.get("PassengerFlow")
        self._FaceExpose = params.get("FaceExpose")
        if params.get("MallArea") is not None:
            self._MallArea = []
            for item in params.get("MallArea"):
                obj = Point()
                obj._deserialize(item)
                self._MallArea.append(obj)
        if params.get("ShopArea") is not None:
            self._ShopArea = []
            for item in params.get("ShopArea"):
                obj = Point()
                obj._deserialize(item)
                self._ShopArea.append(obj)
        if params.get("TrackAreas") is not None:
            self._TrackAreas = []
            for item in params.get("TrackAreas"):
                obj = Polygon()
                obj._deserialize(item)
                self._TrackAreas.append(obj)
        if params.get("Zones") is not None:
            self._Zones = []
            for item in params.get("Zones"):
                obj = ZoneArea()
                obj._deserialize(item)
                self._Zones.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCameraAlertAlert(AbstractModel):
    """告警信息

    """

    def __init__(self):
        r"""
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _MallId: 广场ID
        :type MallId: int
        :param _CameraId: 相机ID
        :type CameraId: int
        :param _CaptureTime: 时间戳,ms,默认为告警请求到达时间
        :type CaptureTime: int
        :param _Image: 图片base64编码
        :type Image: str
        :param _MoveAlert: 移动告警
        :type MoveAlert: :class:`tencentcloud.ump.v20200918.models.CreateCameraAlertsMoveAlert`
        :param _CoverAlert: 遮挡告警
        :type CoverAlert: :class:`tencentcloud.ump.v20200918.models.CreateCameraAlertsCoverAlert`
        """
        self._GroupCode = None
        self._MallId = None
        self._CameraId = None
        self._CaptureTime = None
        self._Image = None
        self._MoveAlert = None
        self._CoverAlert = None

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def MallId(self):
        """广场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def CameraId(self):
        """相机ID
        :rtype: int
        """
        return self._CameraId

    @CameraId.setter
    def CameraId(self, CameraId):
        self._CameraId = CameraId

    @property
    def CaptureTime(self):
        """时间戳,ms,默认为告警请求到达时间
        :rtype: int
        """
        return self._CaptureTime

    @CaptureTime.setter
    def CaptureTime(self, CaptureTime):
        self._CaptureTime = CaptureTime

    @property
    def Image(self):
        """图片base64编码
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def MoveAlert(self):
        """移动告警
        :rtype: :class:`tencentcloud.ump.v20200918.models.CreateCameraAlertsMoveAlert`
        """
        return self._MoveAlert

    @MoveAlert.setter
    def MoveAlert(self, MoveAlert):
        self._MoveAlert = MoveAlert

    @property
    def CoverAlert(self):
        """遮挡告警
        :rtype: :class:`tencentcloud.ump.v20200918.models.CreateCameraAlertsCoverAlert`
        """
        return self._CoverAlert

    @CoverAlert.setter
    def CoverAlert(self, CoverAlert):
        self._CoverAlert = CoverAlert


    def _deserialize(self, params):
        self._GroupCode = params.get("GroupCode")
        self._MallId = params.get("MallId")
        self._CameraId = params.get("CameraId")
        self._CaptureTime = params.get("CaptureTime")
        self._Image = params.get("Image")
        if params.get("MoveAlert") is not None:
            self._MoveAlert = CreateCameraAlertsMoveAlert()
            self._MoveAlert._deserialize(params.get("MoveAlert"))
        if params.get("CoverAlert") is not None:
            self._CoverAlert = CreateCameraAlertsCoverAlert()
            self._CoverAlert._deserialize(params.get("CoverAlert"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCameraAlertsCoverAlert(AbstractModel):
    """遮挡告警

    """

    def __init__(self):
        r"""
        :param _Cover: 是否遮挡
        :type Cover: bool
        :param _CoverConfidence: 是否移动置信度
        :type CoverConfidence: float
        """
        self._Cover = None
        self._CoverConfidence = None

    @property
    def Cover(self):
        """是否遮挡
        :rtype: bool
        """
        return self._Cover

    @Cover.setter
    def Cover(self, Cover):
        self._Cover = Cover

    @property
    def CoverConfidence(self):
        """是否移动置信度
        :rtype: float
        """
        return self._CoverConfidence

    @CoverConfidence.setter
    def CoverConfidence(self, CoverConfidence):
        self._CoverConfidence = CoverConfidence


    def _deserialize(self, params):
        self._Cover = params.get("Cover")
        self._CoverConfidence = params.get("CoverConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCameraAlertsMoveAlert(AbstractModel):
    """移动告警

    """

    def __init__(self):
        r"""
        :param _Move: 是否移动
        :type Move: bool
        :param _MoveConfidence: 是否移动置信度
        :type MoveConfidence: float
        """
        self._Move = None
        self._MoveConfidence = None

    @property
    def Move(self):
        """是否移动
        :rtype: bool
        """
        return self._Move

    @Move.setter
    def Move(self, Move):
        self._Move = Move

    @property
    def MoveConfidence(self):
        """是否移动置信度
        :rtype: float
        """
        return self._MoveConfidence

    @MoveConfidence.setter
    def MoveConfidence(self, MoveConfidence):
        self._MoveConfidence = MoveConfidence


    def _deserialize(self, params):
        self._Move = params.get("Move")
        self._MoveConfidence = params.get("MoveConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCameraAlertsRequest(AbstractModel):
    """CreateCameraAlerts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Alerts: 告警信息列表
        :type Alerts: list of CreateCameraAlertAlert
        """
        self._Alerts = None

    @property
    def Alerts(self):
        """告警信息列表
        :rtype: list of CreateCameraAlertAlert
        """
        return self._Alerts

    @Alerts.setter
    def Alerts(self, Alerts):
        self._Alerts = Alerts


    def _deserialize(self, params):
        if params.get("Alerts") is not None:
            self._Alerts = []
            for item in params.get("Alerts"):
                obj = CreateCameraAlertAlert()
                obj._deserialize(item)
                self._Alerts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCameraAlertsResponse(AbstractModel):
    """CreateCameraAlerts返回参数结构体

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


class CreateCameraStateRequest(AbstractModel):
    """CreateCameraState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _MallId: 广场ID
        :type MallId: int
        :param _CameraStates: 场内所有相机的状态值
        :type CameraStates: list of CameraState
        """
        self._GroupCode = None
        self._MallId = None
        self._CameraStates = None

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def MallId(self):
        """广场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def CameraStates(self):
        """场内所有相机的状态值
        :rtype: list of CameraState
        """
        return self._CameraStates

    @CameraStates.setter
    def CameraStates(self, CameraStates):
        self._CameraStates = CameraStates


    def _deserialize(self, params):
        self._GroupCode = params.get("GroupCode")
        self._MallId = params.get("MallId")
        if params.get("CameraStates") is not None:
            self._CameraStates = []
            for item in params.get("CameraStates"):
                obj = CameraState()
                obj._deserialize(item)
                self._CameraStates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCameraStateResponse(AbstractModel):
    """CreateCameraState返回参数结构体

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


class CreateCaptureRequest(AbstractModel):
    """CreateCapture请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 原始抓拍报文
        :type Data: str
        """
        self._Data = None

    @property
    def Data(self):
        """原始抓拍报文
        :rtype: str
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
        


class CreateCaptureResponse(AbstractModel):
    """CreateCapture返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RspData: 原始应答报文
注意：此字段可能返回 null，表示取不到有效值。
        :type RspData: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RspData = None
        self._RequestId = None

    @property
    def RspData(self):
        """原始应答报文
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RspData

    @RspData.setter
    def RspData(self, RspData):
        self._RspData = RspData

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
        self._RspData = params.get("RspData")
        self._RequestId = params.get("RequestId")


class CreateMultiBizAlertRequest(AbstractModel):
    """CreateMultiBizAlert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _MallId: 广场ID
        :type MallId: int
        :param _ZoneId: 点位ID
        :type ZoneId: int
        :param _CameraId: 摄像头ID
        :type CameraId: int
        :param _CaptureTime: 时间戳，毫秒
        :type CaptureTime: int
        :param _State: 状态: 
1: 侵占
2: 消失
3: 即侵占又消失
        :type State: int
        :param _Image: 图片base64字符串
        :type Image: str
        :param _Warnings: 告警列表
        :type Warnings: list of MultiBizWarning
        """
        self._GroupCode = None
        self._MallId = None
        self._ZoneId = None
        self._CameraId = None
        self._CaptureTime = None
        self._State = None
        self._Image = None
        self._Warnings = None

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def MallId(self):
        """广场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def ZoneId(self):
        """点位ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def CameraId(self):
        """摄像头ID
        :rtype: int
        """
        return self._CameraId

    @CameraId.setter
    def CameraId(self, CameraId):
        self._CameraId = CameraId

    @property
    def CaptureTime(self):
        """时间戳，毫秒
        :rtype: int
        """
        return self._CaptureTime

    @CaptureTime.setter
    def CaptureTime(self, CaptureTime):
        self._CaptureTime = CaptureTime

    @property
    def State(self):
        """状态: 
1: 侵占
2: 消失
3: 即侵占又消失
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Image(self):
        """图片base64字符串
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Warnings(self):
        """告警列表
        :rtype: list of MultiBizWarning
        """
        return self._Warnings

    @Warnings.setter
    def Warnings(self, Warnings):
        self._Warnings = Warnings


    def _deserialize(self, params):
        self._GroupCode = params.get("GroupCode")
        self._MallId = params.get("MallId")
        self._ZoneId = params.get("ZoneId")
        self._CameraId = params.get("CameraId")
        self._CaptureTime = params.get("CaptureTime")
        self._State = params.get("State")
        self._Image = params.get("Image")
        if params.get("Warnings") is not None:
            self._Warnings = []
            for item in params.get("Warnings"):
                obj = MultiBizWarning()
                obj._deserialize(item)
                self._Warnings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMultiBizAlertResponse(AbstractModel):
    """CreateMultiBizAlert返回参数结构体

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


class CreateProgramStateRequest(AbstractModel):
    """CreateProgramState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _ProgramStateItems: 进程监控信息列表
        :type ProgramStateItems: list of ProgramStateItem
        :param _MallId: 商场ID
        :type MallId: int
        """
        self._GroupCode = None
        self._ProgramStateItems = None
        self._MallId = None

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def ProgramStateItems(self):
        """进程监控信息列表
        :rtype: list of ProgramStateItem
        """
        return self._ProgramStateItems

    @ProgramStateItems.setter
    def ProgramStateItems(self, ProgramStateItems):
        self._ProgramStateItems = ProgramStateItems

    @property
    def MallId(self):
        """商场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId


    def _deserialize(self, params):
        self._GroupCode = params.get("GroupCode")
        if params.get("ProgramStateItems") is not None:
            self._ProgramStateItems = []
            for item in params.get("ProgramStateItems"):
                obj = ProgramStateItem()
                obj._deserialize(item)
                self._ProgramStateItems.append(obj)
        self._MallId = params.get("MallId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProgramStateResponse(AbstractModel):
    """CreateProgramState返回参数结构体

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


class CreateServerStateRequest(AbstractModel):
    """CreateServerState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _ServerStateItems: 服务器监控信息列表
        :type ServerStateItems: list of ServerStateItem
        :param _MallId: 商场ID
        :type MallId: int
        :param _ReportTime: 服务器监控信息上报时间戳，单位毫秒
        :type ReportTime: int
        """
        self._GroupCode = None
        self._ServerStateItems = None
        self._MallId = None
        self._ReportTime = None

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def ServerStateItems(self):
        """服务器监控信息列表
        :rtype: list of ServerStateItem
        """
        return self._ServerStateItems

    @ServerStateItems.setter
    def ServerStateItems(self, ServerStateItems):
        self._ServerStateItems = ServerStateItems

    @property
    def MallId(self):
        """商场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def ReportTime(self):
        """服务器监控信息上报时间戳，单位毫秒
        :rtype: int
        """
        return self._ReportTime

    @ReportTime.setter
    def ReportTime(self, ReportTime):
        self._ReportTime = ReportTime


    def _deserialize(self, params):
        self._GroupCode = params.get("GroupCode")
        if params.get("ServerStateItems") is not None:
            self._ServerStateItems = []
            for item in params.get("ServerStateItems"):
                obj = ServerStateItem()
                obj._deserialize(item)
                self._ServerStateItems.append(obj)
        self._MallId = params.get("MallId")
        self._ReportTime = params.get("ReportTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServerStateResponse(AbstractModel):
    """CreateServerState返回参数结构体

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


class DeleteMultiBizAlertRequest(AbstractModel):
    """DeleteMultiBizAlert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _MallId: 广场ID
        :type MallId: int
        :param _ZoneId: 点位ID
        :type ZoneId: int
        :param _CameraId: 摄像头ID
        :type CameraId: int
        :param _ActionType: 消警动作:
1: 误报
2: 正报合规
3: 正报不合规，整改完成
        :type ActionType: int
        :param _Image: 图片base64字符串
        :type Image: str
        """
        self._GroupCode = None
        self._MallId = None
        self._ZoneId = None
        self._CameraId = None
        self._ActionType = None
        self._Image = None

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def MallId(self):
        """广场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def ZoneId(self):
        """点位ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def CameraId(self):
        """摄像头ID
        :rtype: int
        """
        return self._CameraId

    @CameraId.setter
    def CameraId(self, CameraId):
        self._CameraId = CameraId

    @property
    def ActionType(self):
        """消警动作:
1: 误报
2: 正报合规
3: 正报不合规，整改完成
        :rtype: int
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def Image(self):
        """图片base64字符串
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image


    def _deserialize(self, params):
        self._GroupCode = params.get("GroupCode")
        self._MallId = params.get("MallId")
        self._ZoneId = params.get("ZoneId")
        self._CameraId = params.get("CameraId")
        self._ActionType = params.get("ActionType")
        self._Image = params.get("Image")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMultiBizAlertResponse(AbstractModel):
    """DeleteMultiBizAlert返回参数结构体

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


class DeleteTaskRequest(AbstractModel):
    """DeleteTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _MallId: 广场ID
        :type MallId: int
        :param _TaskId: 任务ID
        :type TaskId: int
        """
        self._GroupCode = None
        self._MallId = None
        self._TaskId = None

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def MallId(self):
        """广场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._GroupCode = params.get("GroupCode")
        self._MallId = params.get("MallId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTaskResponse(AbstractModel):
    """DeleteTask返回参数结构体

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


class DescribeCamerasRequest(AbstractModel):
    """DescribeCameras请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _MallId: 广场ID
        :type MallId: int
        """
        self._GroupCode = None
        self._MallId = None

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def MallId(self):
        """广场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId


    def _deserialize(self, params):
        self._GroupCode = params.get("GroupCode")
        self._MallId = params.get("MallId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCamerasResponse(AbstractModel):
    """DescribeCameras返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Cameras: 摄像头列表
        :type Cameras: list of CameraZones
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Cameras = None
        self._RequestId = None

    @property
    def Cameras(self):
        """摄像头列表
        :rtype: list of CameraZones
        """
        return self._Cameras

    @Cameras.setter
    def Cameras(self, Cameras):
        self._Cameras = Cameras

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
        if params.get("Cameras") is not None:
            self._Cameras = []
            for item in params.get("Cameras"):
                obj = CameraZones()
                obj._deserialize(item)
                self._Cameras.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigRequest(AbstractModel):
    """DescribeConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话ID
        :type SessionId: str
        :param _CameraSign: 摄像头签名
        :type CameraSign: str
        :param _CameraAppId: 摄像头app id
        :type CameraAppId: str
        :param _CameraTimestamp: 摄像头时间戳，毫秒
        :type CameraTimestamp: int
        :param _ServerMac: MAC地址，字母大写
        :type ServerMac: str
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _MallId: 广场ID
        :type MallId: int
        """
        self._SessionId = None
        self._CameraSign = None
        self._CameraAppId = None
        self._CameraTimestamp = None
        self._ServerMac = None
        self._GroupCode = None
        self._MallId = None

    @property
    def SessionId(self):
        """会话ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def CameraSign(self):
        """摄像头签名
        :rtype: str
        """
        return self._CameraSign

    @CameraSign.setter
    def CameraSign(self, CameraSign):
        self._CameraSign = CameraSign

    @property
    def CameraAppId(self):
        """摄像头app id
        :rtype: str
        """
        return self._CameraAppId

    @CameraAppId.setter
    def CameraAppId(self, CameraAppId):
        self._CameraAppId = CameraAppId

    @property
    def CameraTimestamp(self):
        """摄像头时间戳，毫秒
        :rtype: int
        """
        return self._CameraTimestamp

    @CameraTimestamp.setter
    def CameraTimestamp(self, CameraTimestamp):
        self._CameraTimestamp = CameraTimestamp

    @property
    def ServerMac(self):
        """MAC地址，字母大写
        :rtype: str
        """
        return self._ServerMac

    @ServerMac.setter
    def ServerMac(self, ServerMac):
        self._ServerMac = ServerMac

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def MallId(self):
        """广场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._CameraSign = params.get("CameraSign")
        self._CameraAppId = params.get("CameraAppId")
        self._CameraTimestamp = params.get("CameraTimestamp")
        self._ServerMac = params.get("ServerMac")
        self._GroupCode = params.get("GroupCode")
        self._MallId = params.get("MallId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigResponse(AbstractModel):
    """DescribeConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话ID
        :type SessionId: str
        :param _Version: 配置版本号
        :type Version: int
        :param _Cameras: 摄像头列表
        :type Cameras: list of CameraConfig
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionId = None
        self._Version = None
        self._Cameras = None
        self._RequestId = None

    @property
    def SessionId(self):
        """会话ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Version(self):
        """配置版本号
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Cameras(self):
        """摄像头列表
        :rtype: list of CameraConfig
        """
        return self._Cameras

    @Cameras.setter
    def Cameras(self, Cameras):
        self._Cameras = Cameras

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
        self._SessionId = params.get("SessionId")
        self._Version = params.get("Version")
        if params.get("Cameras") is not None:
            self._Cameras = []
            for item in params.get("Cameras"):
                obj = CameraConfig()
                obj._deserialize(item)
                self._Cameras.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeImageRequest(AbstractModel):
    """DescribeImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _MallId: 广场ID
        :type MallId: int
        :param _CameraId: 摄像头ID
        :type CameraId: int
        """
        self._GroupCode = None
        self._MallId = None
        self._CameraId = None

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def MallId(self):
        """广场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def CameraId(self):
        """摄像头ID
        :rtype: int
        """
        return self._CameraId

    @CameraId.setter
    def CameraId(self, CameraId):
        self._CameraId = CameraId


    def _deserialize(self, params):
        self._GroupCode = params.get("GroupCode")
        self._MallId = params.get("MallId")
        self._CameraId = params.get("CameraId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageResponse(AbstractModel):
    """DescribeImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: cos 临时 url，异步上传图片，client需要轮询
        :type ImageUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageUrl = None
        self._RequestId = None

    @property
    def ImageUrl(self):
        """cos 临时 url，异步上传图片，client需要轮询
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

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
        self._ImageUrl = params.get("ImageUrl")
        self._RequestId = params.get("RequestId")


class DescribeMultiBizBaseImageRequest(AbstractModel):
    """DescribeMultiBizBaseImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _MallId: 广场ID
        :type MallId: int
        :param _CameraId: 摄像头ID
        :type CameraId: int
        :param _ZoneId: 点位ID
        :type ZoneId: int
        """
        self._GroupCode = None
        self._MallId = None
        self._CameraId = None
        self._ZoneId = None

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def MallId(self):
        """广场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def CameraId(self):
        """摄像头ID
        :rtype: int
        """
        return self._CameraId

    @CameraId.setter
    def CameraId(self, CameraId):
        self._CameraId = CameraId

    @property
    def ZoneId(self):
        """点位ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._GroupCode = params.get("GroupCode")
        self._MallId = params.get("MallId")
        self._CameraId = params.get("CameraId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMultiBizBaseImageResponse(AbstractModel):
    """DescribeMultiBizBaseImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: cos 临时 url
        :type ImageUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageUrl = None
        self._RequestId = None

    @property
    def ImageUrl(self):
        """cos 临时 url
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

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
        self._ImageUrl = params.get("ImageUrl")
        self._RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _MallId: 广场ID
        :type MallId: int
        :param _TaskType: 任务类型:
1: 底图拉取
        :type TaskType: int
        """
        self._GroupCode = None
        self._MallId = None
        self._TaskType = None

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def MallId(self):
        """广场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def TaskType(self):
        """任务类型:
1: 底图拉取
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType


    def _deserialize(self, params):
        self._GroupCode = params.get("GroupCode")
        self._MallId = params.get("MallId")
        self._TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tasks: 任务列表
        :type Tasks: list of Task
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tasks = None
        self._RequestId = None

    @property
    def Tasks(self):
        """任务列表
        :rtype: list of Task
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

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
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _MallId: 广场ID
        :type MallId: int
        """
        self._GroupCode = None
        self._MallId = None

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def MallId(self):
        """广场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId


    def _deserialize(self, params):
        self._GroupCode = params.get("GroupCode")
        self._MallId = params.get("MallId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Zones: 点位列表
        :type Zones: list of ZoneConfig
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Zones = None
        self._RequestId = None

    @property
    def Zones(self):
        """点位列表
        :rtype: list of ZoneConfig
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

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
        if params.get("Zones") is not None:
            self._Zones = []
            for item in params.get("Zones"):
                obj = ZoneConfig()
                obj._deserialize(item)
                self._Zones.append(obj)
        self._RequestId = params.get("RequestId")


class DiskInfo(AbstractModel):
    """硬盘监控信息

    """

    def __init__(self):
        r"""
        :param _DiskName: 硬盘名字
        :type DiskName: str
        :param _Usage: 硬盘使用率
        :type Usage: float
        """
        self._DiskName = None
        self._Usage = None

    @property
    def DiskName(self):
        """硬盘名字
        :rtype: str
        """
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName

    @property
    def Usage(self):
        """硬盘使用率
        :rtype: float
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage


    def _deserialize(self, params):
        self._DiskName = params.get("DiskName")
        self._Usage = params.get("Usage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMultiBizConfigRequest(AbstractModel):
    """ModifyMultiBizConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _MallId: 广场ID
        :type MallId: int
        :param _ZoneId: 点位ID
        :type ZoneId: int
        :param _CameraId: 摄像头ID
        :type CameraId: int
        :param _MonitoringAreas: 监控区域
        :type MonitoringAreas: list of Polygon
        """
        self._GroupCode = None
        self._MallId = None
        self._ZoneId = None
        self._CameraId = None
        self._MonitoringAreas = None

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def MallId(self):
        """广场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def ZoneId(self):
        """点位ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def CameraId(self):
        """摄像头ID
        :rtype: int
        """
        return self._CameraId

    @CameraId.setter
    def CameraId(self, CameraId):
        self._CameraId = CameraId

    @property
    def MonitoringAreas(self):
        """监控区域
        :rtype: list of Polygon
        """
        return self._MonitoringAreas

    @MonitoringAreas.setter
    def MonitoringAreas(self, MonitoringAreas):
        self._MonitoringAreas = MonitoringAreas


    def _deserialize(self, params):
        self._GroupCode = params.get("GroupCode")
        self._MallId = params.get("MallId")
        self._ZoneId = params.get("ZoneId")
        self._CameraId = params.get("CameraId")
        if params.get("MonitoringAreas") is not None:
            self._MonitoringAreas = []
            for item in params.get("MonitoringAreas"):
                obj = Polygon()
                obj._deserialize(item)
                self._MonitoringAreas.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMultiBizConfigResponse(AbstractModel):
    """ModifyMultiBizConfig返回参数结构体

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


class MultiBizWarning(AbstractModel):
    """多经点位告警

    """

    def __init__(self):
        r"""
        :param _Id: 编号
        :type Id: int
        :param _MonitoringArea: 监控区域
        :type MonitoringArea: list of Point
        :param _WarningInfos: 告警列表
        :type WarningInfos: list of MultiBizWarningInfo
        """
        self._Id = None
        self._MonitoringArea = None
        self._WarningInfos = None

    @property
    def Id(self):
        """编号
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MonitoringArea(self):
        """监控区域
        :rtype: list of Point
        """
        return self._MonitoringArea

    @MonitoringArea.setter
    def MonitoringArea(self, MonitoringArea):
        self._MonitoringArea = MonitoringArea

    @property
    def WarningInfos(self):
        """告警列表
        :rtype: list of MultiBizWarningInfo
        """
        return self._WarningInfos

    @WarningInfos.setter
    def WarningInfos(self, WarningInfos):
        self._WarningInfos = WarningInfos


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("MonitoringArea") is not None:
            self._MonitoringArea = []
            for item in params.get("MonitoringArea"):
                obj = Point()
                obj._deserialize(item)
                self._MonitoringArea.append(obj)
        if params.get("WarningInfos") is not None:
            self._WarningInfos = []
            for item in params.get("WarningInfos"):
                obj = MultiBizWarningInfo()
                obj._deserialize(item)
                self._WarningInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiBizWarningInfo(AbstractModel):
    """多经点位告警信息

    """

    def __init__(self):
        r"""
        :param _WarningType: 告警类型：
0: 无变化
1: 侵占
2: 消失
        :type WarningType: int
        :param _WarningAreaSize: 告警侵占或消失面积
        :type WarningAreaSize: float
        :param _WarningLocation: 告警侵占或消失坐标
        :type WarningLocation: :class:`tencentcloud.ump.v20200918.models.Point`
        :param _WarningAreaContour: 告警侵占或消失轮廓
        :type WarningAreaContour: list of Point
        """
        self._WarningType = None
        self._WarningAreaSize = None
        self._WarningLocation = None
        self._WarningAreaContour = None

    @property
    def WarningType(self):
        """告警类型：
0: 无变化
1: 侵占
2: 消失
        :rtype: int
        """
        return self._WarningType

    @WarningType.setter
    def WarningType(self, WarningType):
        self._WarningType = WarningType

    @property
    def WarningAreaSize(self):
        """告警侵占或消失面积
        :rtype: float
        """
        return self._WarningAreaSize

    @WarningAreaSize.setter
    def WarningAreaSize(self, WarningAreaSize):
        self._WarningAreaSize = WarningAreaSize

    @property
    def WarningLocation(self):
        """告警侵占或消失坐标
        :rtype: :class:`tencentcloud.ump.v20200918.models.Point`
        """
        return self._WarningLocation

    @WarningLocation.setter
    def WarningLocation(self, WarningLocation):
        self._WarningLocation = WarningLocation

    @property
    def WarningAreaContour(self):
        """告警侵占或消失轮廓
        :rtype: list of Point
        """
        return self._WarningAreaContour

    @WarningAreaContour.setter
    def WarningAreaContour(self, WarningAreaContour):
        self._WarningAreaContour = WarningAreaContour


    def _deserialize(self, params):
        self._WarningType = params.get("WarningType")
        self._WarningAreaSize = params.get("WarningAreaSize")
        if params.get("WarningLocation") is not None:
            self._WarningLocation = Point()
            self._WarningLocation._deserialize(params.get("WarningLocation"))
        if params.get("WarningAreaContour") is not None:
            self._WarningAreaContour = []
            for item in params.get("WarningAreaContour"):
                obj = Point()
                obj._deserialize(item)
                self._WarningAreaContour.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Point(AbstractModel):
    """点

    """

    def __init__(self):
        r"""
        :param _X: X坐标
        :type X: int
        :param _Y: Y坐标
        :type Y: int
        """
        self._X = None
        self._Y = None

    @property
    def X(self):
        """X坐标
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        """Y坐标
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Polygon(AbstractModel):
    """多边形

    """

    def __init__(self):
        r"""
        :param _Points: 标注列表
        :type Points: list of Point
        """
        self._Points = None

    @property
    def Points(self):
        """标注列表
        :rtype: list of Point
        """
        return self._Points

    @Points.setter
    def Points(self, Points):
        self._Points = Points


    def _deserialize(self, params):
        if params.get("Points") is not None:
            self._Points = []
            for item in params.get("Points"):
                obj = Point()
                obj._deserialize(item)
                self._Points.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProgramStateItem(AbstractModel):
    """进程状态监控项

    """

    def __init__(self):
        r"""
        :param _ServerIp: 服务器IP
        :type ServerIp: str
        :param _ProgramName: 进程名字
        :type ProgramName: str
        :param _OnlineCount: 在线个数
        :type OnlineCount: int
        :param _OfflineCount: 离线个数
        :type OfflineCount: int
        :param _State: 上报状态:
1: 正常上报
2: 异常上报
注：此处异常上报是指本次上报由于场内服务内部原因导致上报数据不可信等。此时离线个数重置为1，在线个数重置为0
        :type State: int
        """
        self._ServerIp = None
        self._ProgramName = None
        self._OnlineCount = None
        self._OfflineCount = None
        self._State = None

    @property
    def ServerIp(self):
        """服务器IP
        :rtype: str
        """
        return self._ServerIp

    @ServerIp.setter
    def ServerIp(self, ServerIp):
        self._ServerIp = ServerIp

    @property
    def ProgramName(self):
        """进程名字
        :rtype: str
        """
        return self._ProgramName

    @ProgramName.setter
    def ProgramName(self, ProgramName):
        self._ProgramName = ProgramName

    @property
    def OnlineCount(self):
        """在线个数
        :rtype: int
        """
        return self._OnlineCount

    @OnlineCount.setter
    def OnlineCount(self, OnlineCount):
        self._OnlineCount = OnlineCount

    @property
    def OfflineCount(self):
        """离线个数
        :rtype: int
        """
        return self._OfflineCount

    @OfflineCount.setter
    def OfflineCount(self, OfflineCount):
        self._OfflineCount = OfflineCount

    @property
    def State(self):
        """上报状态:
1: 正常上报
2: 异常上报
注：此处异常上报是指本次上报由于场内服务内部原因导致上报数据不可信等。此时离线个数重置为1，在线个数重置为0
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._ServerIp = params.get("ServerIp")
        self._ProgramName = params.get("ProgramName")
        self._OnlineCount = params.get("OnlineCount")
        self._OfflineCount = params.get("OfflineCount")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportServiceRegisterRequest(AbstractModel):
    """ReportServiceRegister请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _MallId: 广场ID
        :type MallId: int
        :param _ServiceRegisterInfos: 服务上报当前的服务能力信息
        :type ServiceRegisterInfos: list of ServiceRegisterInfo
        :param _ServerIp: 服务内网Ip
        :type ServerIp: str
        :param _ServerNodeId: 上报服务所在服务器的唯一ID
        :type ServerNodeId: str
        :param _ReportTime: 上报时间戳, 单位毫秒
        :type ReportTime: int
        """
        self._GroupCode = None
        self._MallId = None
        self._ServiceRegisterInfos = None
        self._ServerIp = None
        self._ServerNodeId = None
        self._ReportTime = None

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def MallId(self):
        """广场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def ServiceRegisterInfos(self):
        """服务上报当前的服务能力信息
        :rtype: list of ServiceRegisterInfo
        """
        return self._ServiceRegisterInfos

    @ServiceRegisterInfos.setter
    def ServiceRegisterInfos(self, ServiceRegisterInfos):
        self._ServiceRegisterInfos = ServiceRegisterInfos

    @property
    def ServerIp(self):
        """服务内网Ip
        :rtype: str
        """
        return self._ServerIp

    @ServerIp.setter
    def ServerIp(self, ServerIp):
        self._ServerIp = ServerIp

    @property
    def ServerNodeId(self):
        """上报服务所在服务器的唯一ID
        :rtype: str
        """
        return self._ServerNodeId

    @ServerNodeId.setter
    def ServerNodeId(self, ServerNodeId):
        self._ServerNodeId = ServerNodeId

    @property
    def ReportTime(self):
        """上报时间戳, 单位毫秒
        :rtype: int
        """
        return self._ReportTime

    @ReportTime.setter
    def ReportTime(self, ReportTime):
        self._ReportTime = ReportTime


    def _deserialize(self, params):
        self._GroupCode = params.get("GroupCode")
        self._MallId = params.get("MallId")
        if params.get("ServiceRegisterInfos") is not None:
            self._ServiceRegisterInfos = []
            for item in params.get("ServiceRegisterInfos"):
                obj = ServiceRegisterInfo()
                obj._deserialize(item)
                self._ServiceRegisterInfos.append(obj)
        self._ServerIp = params.get("ServerIp")
        self._ServerNodeId = params.get("ServerNodeId")
        self._ReportTime = params.get("ReportTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportServiceRegisterResponse(AbstractModel):
    """ReportServiceRegister返回参数结构体

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


class SearchImageRequest(AbstractModel):
    """SearchImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _MallId: 广场ID
        :type MallId: int
        :param _Image: 图片base64字符串
        :type Image: str
        :param _ImageTime: 时间戳，毫秒
        :type ImageTime: int
        """
        self._GroupCode = None
        self._MallId = None
        self._Image = None
        self._ImageTime = None

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def MallId(self):
        """广场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def Image(self):
        """图片base64字符串
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def ImageTime(self):
        """时间戳，毫秒
        :rtype: int
        """
        return self._ImageTime

    @ImageTime.setter
    def ImageTime(self, ImageTime):
        self._ImageTime = ImageTime


    def _deserialize(self, params):
        self._GroupCode = params.get("GroupCode")
        self._MallId = params.get("MallId")
        self._Image = params.get("Image")
        self._ImageTime = params.get("ImageTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchImageResponse(AbstractModel):
    """SearchImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FaceId: face id
        :type FaceId: str
        :param _Results: 搜索结果列表
        :type Results: list of SearchResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FaceId = None
        self._Results = None
        self._RequestId = None

    @property
    def FaceId(self):
        """face id
        :rtype: str
        """
        return self._FaceId

    @FaceId.setter
    def FaceId(self, FaceId):
        self._FaceId = FaceId

    @property
    def Results(self):
        """搜索结果列表
        :rtype: list of SearchResult
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
        self._FaceId = params.get("FaceId")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = SearchResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class SearchResult(AbstractModel):
    """以图搜图检索结果

    """

    def __init__(self):
        r"""
        :param _Image: 图片base64数据
        :type Image: str
        :param _PersonId: 身份ID
        :type PersonId: str
        :param _Similarity: 相似度
        :type Similarity: float
        """
        self._Image = None
        self._PersonId = None
        self._Similarity = None

    @property
    def Image(self):
        """图片base64数据
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def PersonId(self):
        """身份ID
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Similarity(self):
        """相似度
        :rtype: float
        """
        return self._Similarity

    @Similarity.setter
    def Similarity(self, Similarity):
        self._Similarity = Similarity


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._PersonId = params.get("PersonId")
        self._Similarity = params.get("Similarity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerStateItem(AbstractModel):
    """服务器监控状态上报项

    """

    def __init__(self):
        r"""
        :param _ServerState: 服务器状态
1: 在线
2: 离线
3: 重启
        :type ServerState: int
        :param _ServerIp: 服务器IP
        :type ServerIp: str
        :param _DiskInfos: 硬盘监控信息列表
        :type DiskInfos: list of DiskInfo
        """
        self._ServerState = None
        self._ServerIp = None
        self._DiskInfos = None

    @property
    def ServerState(self):
        """服务器状态
1: 在线
2: 离线
3: 重启
        :rtype: int
        """
        return self._ServerState

    @ServerState.setter
    def ServerState(self, ServerState):
        self._ServerState = ServerState

    @property
    def ServerIp(self):
        """服务器IP
        :rtype: str
        """
        return self._ServerIp

    @ServerIp.setter
    def ServerIp(self, ServerIp):
        self._ServerIp = ServerIp

    @property
    def DiskInfos(self):
        """硬盘监控信息列表
        :rtype: list of DiskInfo
        """
        return self._DiskInfos

    @DiskInfos.setter
    def DiskInfos(self, DiskInfos):
        self._DiskInfos = DiskInfos


    def _deserialize(self, params):
        self._ServerState = params.get("ServerState")
        self._ServerIp = params.get("ServerIp")
        if params.get("DiskInfos") is not None:
            self._DiskInfos = []
            for item in params.get("DiskInfos"):
                obj = DiskInfo()
                obj._deserialize(item)
                self._DiskInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceRegisterInfo(AbstractModel):
    """用于服务注册时表示当前服务的具体信息

    """

    def __init__(self):
        r"""
        :param _CgiUrl: 当前服务的回调地址
        :type CgiUrl: str
        :param _ServiceType: 当前服务类型:
1: 多经服务
2: 相机误报警确认
3: 底图更新
        :type ServiceType: int
        """
        self._CgiUrl = None
        self._ServiceType = None

    @property
    def CgiUrl(self):
        """当前服务的回调地址
        :rtype: str
        """
        return self._CgiUrl

    @CgiUrl.setter
    def CgiUrl(self, CgiUrl):
        self._CgiUrl = CgiUrl

    @property
    def ServiceType(self):
        """当前服务类型:
1: 多经服务
2: 相机误报警确认
3: 底图更新
        :rtype: int
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType


    def _deserialize(self, params):
        self._CgiUrl = params.get("CgiUrl")
        self._ServiceType = params.get("ServiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _GroupCode: 集团编码
        :type GroupCode: str
        :param _MallId: 广场ID
        :type MallId: int
        :param _TaskContent: 任务内容
        :type TaskContent: :class:`tencentcloud.ump.v20200918.models.TaskContent`
        :param _TaskType: 任务类型:
1: 底图拉取
        :type TaskType: int
        """
        self._TaskId = None
        self._GroupCode = None
        self._MallId = None
        self._TaskContent = None
        self._TaskType = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def GroupCode(self):
        """集团编码
        :rtype: str
        """
        return self._GroupCode

    @GroupCode.setter
    def GroupCode(self, GroupCode):
        self._GroupCode = GroupCode

    @property
    def MallId(self):
        """广场ID
        :rtype: int
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def TaskContent(self):
        """任务内容
        :rtype: :class:`tencentcloud.ump.v20200918.models.TaskContent`
        """
        return self._TaskContent

    @TaskContent.setter
    def TaskContent(self, TaskContent):
        self._TaskContent = TaskContent

    @property
    def TaskType(self):
        """任务类型:
1: 底图拉取
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._GroupCode = params.get("GroupCode")
        self._MallId = params.get("MallId")
        if params.get("TaskContent") is not None:
            self._TaskContent = TaskContent()
            self._TaskContent._deserialize(params.get("TaskContent"))
        self._TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskContent(AbstractModel):
    """任务内容

    """

    def __init__(self):
        r"""
        :param _CameraId: 摄像头ID
        :type CameraId: int
        :param _RTSP: rtsp 地址
        :type RTSP: str
        :param _Url: 图片上传地址
        :type Url: str
        """
        self._CameraId = None
        self._RTSP = None
        self._Url = None

    @property
    def CameraId(self):
        """摄像头ID
        :rtype: int
        """
        return self._CameraId

    @CameraId.setter
    def CameraId(self, CameraId):
        self._CameraId = CameraId

    @property
    def RTSP(self):
        """rtsp 地址
        :rtype: str
        """
        return self._RTSP

    @RTSP.setter
    def RTSP(self, RTSP):
        self._RTSP = RTSP

    @property
    def Url(self):
        """图片上传地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._CameraId = params.get("CameraId")
        self._RTSP = params.get("RTSP")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneArea(AbstractModel):
    """点位包含店门标注

    """

    def __init__(self):
        r"""
        :param _ZoneId: 点位ID
        :type ZoneId: int
        :param _ShopArea: 店门标注
        :type ShopArea: list of Point
        """
        self._ZoneId = None
        self._ShopArea = None

    @property
    def ZoneId(self):
        """点位ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ShopArea(self):
        """店门标注
        :rtype: list of Point
        """
        return self._ShopArea

    @ShopArea.setter
    def ShopArea(self, ShopArea):
        self._ShopArea = ShopArea


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("ShopArea") is not None:
            self._ShopArea = []
            for item in params.get("ShopArea"):
                obj = Point()
                obj._deserialize(item)
                self._ShopArea.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneConfig(AbstractModel):
    """点位包含绑定、调试信息

    """

    def __init__(self):
        r"""
        :param _ZoneId: 点位ID
        :type ZoneId: int
        :param _ZoneName: 点位名称
        :type ZoneName: str
        :param _ZoneType: 点位类型:
1: 场门
3: 层门
5: 特殊区域
7: 门店
8: 补位
10: 开放式门店
11: 品类区
12: 公共区
        :type ZoneType: int
        :param _BunkCodes: 铺位编码
        :type BunkCodes: str
        :param _FloorName: 楼层名称
        :type FloorName: str
        :param _FloorId: 楼层ID
        :type FloorId: int
        :param _BindNum: 绑定数
        :type BindNum: int
        :param _DebugNum: 调试数
        :type DebugNum: int
        :param _State: 下发状态:
1: 不可下发
2: 可下发
3: 已下发
        :type State: int
        """
        self._ZoneId = None
        self._ZoneName = None
        self._ZoneType = None
        self._BunkCodes = None
        self._FloorName = None
        self._FloorId = None
        self._BindNum = None
        self._DebugNum = None
        self._State = None

    @property
    def ZoneId(self):
        """点位ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """点位名称
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneType(self):
        """点位类型:
1: 场门
3: 层门
5: 特殊区域
7: 门店
8: 补位
10: 开放式门店
11: 品类区
12: 公共区
        :rtype: int
        """
        return self._ZoneType

    @ZoneType.setter
    def ZoneType(self, ZoneType):
        self._ZoneType = ZoneType

    @property
    def BunkCodes(self):
        """铺位编码
        :rtype: str
        """
        return self._BunkCodes

    @BunkCodes.setter
    def BunkCodes(self, BunkCodes):
        self._BunkCodes = BunkCodes

    @property
    def FloorName(self):
        """楼层名称
        :rtype: str
        """
        return self._FloorName

    @FloorName.setter
    def FloorName(self, FloorName):
        self._FloorName = FloorName

    @property
    def FloorId(self):
        """楼层ID
        :rtype: int
        """
        return self._FloorId

    @FloorId.setter
    def FloorId(self, FloorId):
        self._FloorId = FloorId

    @property
    def BindNum(self):
        """绑定数
        :rtype: int
        """
        return self._BindNum

    @BindNum.setter
    def BindNum(self, BindNum):
        self._BindNum = BindNum

    @property
    def DebugNum(self):
        """调试数
        :rtype: int
        """
        return self._DebugNum

    @DebugNum.setter
    def DebugNum(self, DebugNum):
        self._DebugNum = DebugNum

    @property
    def State(self):
        """下发状态:
1: 不可下发
2: 可下发
3: 已下发
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._ZoneType = params.get("ZoneType")
        self._BunkCodes = params.get("BunkCodes")
        self._FloorName = params.get("FloorName")
        self._FloorId = params.get("FloorId")
        self._BindNum = params.get("BindNum")
        self._DebugNum = params.get("DebugNum")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        