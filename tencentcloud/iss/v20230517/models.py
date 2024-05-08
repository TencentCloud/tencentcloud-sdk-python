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


class AIConfig(AbstractModel):
    """AI分析配置

    """

    def __init__(self):
        r"""
        :param _DetectType: AI 分析类型。可选值为 Facemask(口罩识别)、Chefhat(厨师帽识别)、Smoking(抽烟检测)、Chefcloth(厨师服识别)、PhoneCall(接打电话识别)、Pet(宠物识别)、Body(人体识别)和Car(车辆车牌识别)等
        :type DetectType: str
        :param _TimeInterval: 截图频率。可选值1～20秒
        :type TimeInterval: int
        :param _OperTimeSlot: 模板生效的时间段。最多包含5组时间段
        :type OperTimeSlot: list of OperTimeSlot
        """
        self._DetectType = None
        self._TimeInterval = None
        self._OperTimeSlot = None

    @property
    def DetectType(self):
        return self._DetectType

    @DetectType.setter
    def DetectType(self, DetectType):
        self._DetectType = DetectType

    @property
    def TimeInterval(self):
        return self._TimeInterval

    @TimeInterval.setter
    def TimeInterval(self, TimeInterval):
        self._TimeInterval = TimeInterval

    @property
    def OperTimeSlot(self):
        return self._OperTimeSlot

    @OperTimeSlot.setter
    def OperTimeSlot(self, OperTimeSlot):
        self._OperTimeSlot = OperTimeSlot


    def _deserialize(self, params):
        self._DetectType = params.get("DetectType")
        self._TimeInterval = params.get("TimeInterval")
        if params.get("OperTimeSlot") is not None:
            self._OperTimeSlot = []
            for item in params.get("OperTimeSlot"):
                obj = OperTimeSlot()
                obj._deserialize(item)
                self._OperTimeSlot.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AITaskInfo(AbstractModel):
    """AI任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: AI 任务 ID
        :type TaskId: str
        :param _Name: AI 任务名称
        :type Name: str
        :param _Desc: AI 任务描述
        :type Desc: str
        :param _Status: AI 任务状态。"on"代表开启了 AI 分析任务，"off"代表停止 AI 分析任务
        :type Status: str
        :param _ChannelList: 通道 ID 列表
        :type ChannelList: list of str
        :param _CallbackUrl: AI 结果回调地址
        :type CallbackUrl: str
        :param _Templates: AI 配置列表
        :type Templates: list of AITemplates
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _UpdatedTime: 更新时间
        :type UpdatedTime: str
        """
        self._TaskId = None
        self._Name = None
        self._Desc = None
        self._Status = None
        self._ChannelList = None
        self._CallbackUrl = None
        self._Templates = None
        self._CreatedTime = None
        self._UpdatedTime = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ChannelList(self):
        return self._ChannelList

    @ChannelList.setter
    def ChannelList(self, ChannelList):
        self._ChannelList = ChannelList

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def Templates(self):
        return self._Templates

    @Templates.setter
    def Templates(self, Templates):
        self._Templates = Templates

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._Status = params.get("Status")
        self._ChannelList = params.get("ChannelList")
        self._CallbackUrl = params.get("CallbackUrl")
        if params.get("Templates") is not None:
            self._Templates = []
            for item in params.get("Templates"):
                obj = AITemplates()
                obj._deserialize(item)
                self._Templates.append(obj)
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AITaskResultData(AbstractModel):
    """AI识别结果

    """

    def __init__(self):
        r"""
        :param _TaskId: AI 任务 ID
        :type TaskId: str
        :param _AIResultCount: 在 BeginTime 和 EndTime 时间之内，有识别结果的 AI 调用次数（分页依据此数值）
        :type AIResultCount: int
        :param _AIResults: AI 任务执行结果详情
注意：此字段可能返回 null，表示取不到有效值。
        :type AIResults: :class:`tencentcloud.iss.v20230517.models.AITaskResultInfo`
        """
        self._TaskId = None
        self._AIResultCount = None
        self._AIResults = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def AIResultCount(self):
        return self._AIResultCount

    @AIResultCount.setter
    def AIResultCount(self, AIResultCount):
        self._AIResultCount = AIResultCount

    @property
    def AIResults(self):
        return self._AIResults

    @AIResults.setter
    def AIResults(self, AIResults):
        self._AIResults = AIResults


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._AIResultCount = params.get("AIResultCount")
        if params.get("AIResults") is not None:
            self._AIResults = AITaskResultInfo()
            self._AIResults._deserialize(params.get("AIResults"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AITaskResultInfo(AbstractModel):
    """AI分析结果详情

    """

    def __init__(self):
        r"""
        :param _Body: 人体识别结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Body: list of BodyAIResultInfo
        :param _Pet: 宠物识别结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Pet: list of PetAIResultInfo
        :param _Car: 车辆车牌识别结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Car: list of CarAIResultInfo
        :param _ChefHat: 厨师帽结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ChefHat: list of ChefHatAIResultInfo
        :param _ChefCloth: 厨师服结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ChefCloth: list of ChefClothAIResultInfo
        :param _FaceMask: 口罩识别结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceMask: list of FaceMaskAIResultInfo
        :param _Smoking: 抽烟检测结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Smoking: list of SmokingAIResultInfo
        :param _PhoneCall: 接打电话识别结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneCall: list of PhoneCallAIResultInfo
        """
        self._Body = None
        self._Pet = None
        self._Car = None
        self._ChefHat = None
        self._ChefCloth = None
        self._FaceMask = None
        self._Smoking = None
        self._PhoneCall = None

    @property
    def Body(self):
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Pet(self):
        return self._Pet

    @Pet.setter
    def Pet(self, Pet):
        self._Pet = Pet

    @property
    def Car(self):
        return self._Car

    @Car.setter
    def Car(self, Car):
        self._Car = Car

    @property
    def ChefHat(self):
        return self._ChefHat

    @ChefHat.setter
    def ChefHat(self, ChefHat):
        self._ChefHat = ChefHat

    @property
    def ChefCloth(self):
        return self._ChefCloth

    @ChefCloth.setter
    def ChefCloth(self, ChefCloth):
        self._ChefCloth = ChefCloth

    @property
    def FaceMask(self):
        return self._FaceMask

    @FaceMask.setter
    def FaceMask(self, FaceMask):
        self._FaceMask = FaceMask

    @property
    def Smoking(self):
        return self._Smoking

    @Smoking.setter
    def Smoking(self, Smoking):
        self._Smoking = Smoking

    @property
    def PhoneCall(self):
        return self._PhoneCall

    @PhoneCall.setter
    def PhoneCall(self, PhoneCall):
        self._PhoneCall = PhoneCall


    def _deserialize(self, params):
        if params.get("Body") is not None:
            self._Body = []
            for item in params.get("Body"):
                obj = BodyAIResultInfo()
                obj._deserialize(item)
                self._Body.append(obj)
        if params.get("Pet") is not None:
            self._Pet = []
            for item in params.get("Pet"):
                obj = PetAIResultInfo()
                obj._deserialize(item)
                self._Pet.append(obj)
        if params.get("Car") is not None:
            self._Car = []
            for item in params.get("Car"):
                obj = CarAIResultInfo()
                obj._deserialize(item)
                self._Car.append(obj)
        if params.get("ChefHat") is not None:
            self._ChefHat = []
            for item in params.get("ChefHat"):
                obj = ChefHatAIResultInfo()
                obj._deserialize(item)
                self._ChefHat.append(obj)
        if params.get("ChefCloth") is not None:
            self._ChefCloth = []
            for item in params.get("ChefCloth"):
                obj = ChefClothAIResultInfo()
                obj._deserialize(item)
                self._ChefCloth.append(obj)
        if params.get("FaceMask") is not None:
            self._FaceMask = []
            for item in params.get("FaceMask"):
                obj = FaceMaskAIResultInfo()
                obj._deserialize(item)
                self._FaceMask.append(obj)
        if params.get("Smoking") is not None:
            self._Smoking = []
            for item in params.get("Smoking"):
                obj = SmokingAIResultInfo()
                obj._deserialize(item)
                self._Smoking.append(obj)
        if params.get("PhoneCall") is not None:
            self._PhoneCall = []
            for item in params.get("PhoneCall"):
                obj = PhoneCallAIResultInfo()
                obj._deserialize(item)
                self._PhoneCall.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AITemplates(AbstractModel):
    """AI模板信息

    """

    def __init__(self):
        r"""
        :param _Tag: AI 类别。可选值 AI(AI 分析)和 Snapshot(截图)，Templates 列表中只能出现一种类型。
        :type Tag: str
        :param _AIConfig: AI 分析配置。和"SnapshotConfig"二选一。
        :type AIConfig: :class:`tencentcloud.iss.v20230517.models.AIConfig`
        :param _SnapshotConfig: 截图配置。和"AIConfig"二选一。
        :type SnapshotConfig: :class:`tencentcloud.iss.v20230517.models.SnapshotConfig`
        """
        self._Tag = None
        self._AIConfig = None
        self._SnapshotConfig = None

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def AIConfig(self):
        return self._AIConfig

    @AIConfig.setter
    def AIConfig(self, AIConfig):
        self._AIConfig = AIConfig

    @property
    def SnapshotConfig(self):
        return self._SnapshotConfig

    @SnapshotConfig.setter
    def SnapshotConfig(self, SnapshotConfig):
        self._SnapshotConfig = SnapshotConfig


    def _deserialize(self, params):
        self._Tag = params.get("Tag")
        if params.get("AIConfig") is not None:
            self._AIConfig = AIConfig()
            self._AIConfig._deserialize(params.get("AIConfig"))
        if params.get("SnapshotConfig") is not None:
            self._SnapshotConfig = SnapshotConfig()
            self._SnapshotConfig._deserialize(params.get("SnapshotConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAITaskRequest(AbstractModel):
    """AddAITask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: AI 任务名称。仅支持中文、英文、数字、_、-，长度不超过32个字符
        :type Name: str
        :param _ChannelList: 通道 ID 列表。不能添加存在于其他 AI 任务的通道，限制1000个通道。
        :type ChannelList: list of str
        :param _Templates: AI 配置列表
        :type Templates: list of AITemplates
        :param _Desc: AI 任务描述。仅支持中文、英文、数字、_、-，长度不超过128个字符
        :type Desc: str
        :param _CallbackUrl: AI 结果回调地址。类似 "http://ip:port/***或者https://domain/***
        :type CallbackUrl: str
        :param _IsStartTheTask: 是否立即开启 AI 任务。"true"代表立即开启 AI 任务，"false"代表暂不开启 AI 任务，默认为 false。
        :type IsStartTheTask: bool
        """
        self._Name = None
        self._ChannelList = None
        self._Templates = None
        self._Desc = None
        self._CallbackUrl = None
        self._IsStartTheTask = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ChannelList(self):
        return self._ChannelList

    @ChannelList.setter
    def ChannelList(self, ChannelList):
        self._ChannelList = ChannelList

    @property
    def Templates(self):
        return self._Templates

    @Templates.setter
    def Templates(self, Templates):
        self._Templates = Templates

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def IsStartTheTask(self):
        return self._IsStartTheTask

    @IsStartTheTask.setter
    def IsStartTheTask(self, IsStartTheTask):
        self._IsStartTheTask = IsStartTheTask


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ChannelList = params.get("ChannelList")
        if params.get("Templates") is not None:
            self._Templates = []
            for item in params.get("Templates"):
                obj = AITemplates()
                obj._deserialize(item)
                self._Templates.append(obj)
        self._Desc = params.get("Desc")
        self._CallbackUrl = params.get("CallbackUrl")
        self._IsStartTheTask = params.get("IsStartTheTask")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAITaskResponse(AbstractModel):
    """AddAITask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: AI任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iss.v20230517.models.AITaskInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AITaskInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddDeviceData(AbstractModel):
    """增加设备接口返回数据

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备iD
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param _Code: 设备编码（国标设备即我们为设备生成的20位国标编码，rtmp 设备为10 位设备编码）
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param _Name: 设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _AccessProtocol: 设备接入协议，1:RTMP,2:GB,3:GW 
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessProtocol: int
        :param _Type: 设备类型，1:IPC,2:NVR
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _ClusterId: 设备接入服务节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ClusterName: 设备接入服务节点名称

注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param _TransportProtocol: 设备流传输协议，1:UDP,2:TCP 
注意：此字段可能返回 null，表示取不到有效值。
        :type TransportProtocol: int
        :param _Password: 设备密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Description: 设备描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Status: 设备状态，0:未注册,1:在线,2:离线,3:禁用
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _OrganizationId: 设备所属组织ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationId: int
        :param _GatewayId: 设备接入网关ID，从查询网关列表接口中获取（仅网关接入需要）
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayId: str
        :param _ProtocolType: 网关接入协议类型，1.海康SDK，2.大华SDK，3.宇视SDK，4.Onvif（仅网关接入需要）
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtocolType: int
        :param _Ip: 设备接入IP（仅网关接入需要）
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Port: 设备Port（仅网关接入需要）
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Username: 设备用户名（仅网关接入需要）
注意：此字段可能返回 null，表示取不到有效值。
        :type Username: str
        :param _AppId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        """
        self._DeviceId = None
        self._Code = None
        self._Name = None
        self._AccessProtocol = None
        self._Type = None
        self._ClusterId = None
        self._ClusterName = None
        self._TransportProtocol = None
        self._Password = None
        self._Description = None
        self._Status = None
        self._OrganizationId = None
        self._GatewayId = None
        self._ProtocolType = None
        self._Ip = None
        self._Port = None
        self._Username = None
        self._AppId = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AccessProtocol(self):
        return self._AccessProtocol

    @AccessProtocol.setter
    def AccessProtocol(self, AccessProtocol):
        self._AccessProtocol = AccessProtocol

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def TransportProtocol(self):
        return self._TransportProtocol

    @TransportProtocol.setter
    def TransportProtocol(self, TransportProtocol):
        self._TransportProtocol = TransportProtocol

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ProtocolType(self):
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Code = params.get("Code")
        self._Name = params.get("Name")
        self._AccessProtocol = params.get("AccessProtocol")
        self._Type = params.get("Type")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._TransportProtocol = params.get("TransportProtocol")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._OrganizationId = params.get("OrganizationId")
        self._GatewayId = params.get("GatewayId")
        self._ProtocolType = params.get("ProtocolType")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Username = params.get("Username")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddOrgData(AbstractModel):
    """增加组织接口返回数据

    """

    def __init__(self):
        r"""
        :param _OrganizationId: 组织 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationId: str
        :param _Name: 组织名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _ParentId: 组织父节点 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentId: str
        :param _Level: 组织层级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param _AppId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _ParentIds: 组织结构
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentIds: str
        :param _Total: 设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Online: 设备在线数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Online: int
        """
        self._OrganizationId = None
        self._Name = None
        self._ParentId = None
        self._Level = None
        self._AppId = None
        self._ParentIds = None
        self._Total = None
        self._Online = None

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParentId(self):
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ParentIds(self):
        return self._ParentIds

    @ParentIds.setter
    def ParentIds(self, ParentIds):
        self._ParentIds = ParentIds

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Online(self):
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        self._Name = params.get("Name")
        self._ParentId = params.get("ParentId")
        self._Level = params.get("Level")
        self._AppId = params.get("AppId")
        self._ParentIds = params.get("ParentIds")
        self._Total = params.get("Total")
        self._Online = params.get("Online")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddOrganizationRequest(AbstractModel):
    """AddOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 组织名称（仅支持中文、英文、数字、_、-的组合，长度不超过16个字符，且组织名称不能重复）
        :type Name: str
        :param _ParentId: 组织父节点 ID（从查询组织接口DescribeOrganization中获取，填0代表根组织）
        :type ParentId: str
        """
        self._Name = None
        self._ParentId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParentId(self):
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ParentId = params.get("ParentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddOrganizationResponse(AbstractModel):
    """AddOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 增加组织接口返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.AddOrgData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AddOrgData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddRecordBackupPlanData(AbstractModel):
    """新增录像上云计划返回数据

    """

    def __init__(self):
        r"""
        :param _PlanId: 录像上云计划ID
        :type PlanId: str
        :param _PlanName: 录像上云计划名称
        :type PlanName: str
        :param _TemplateId: 录像上云模板ID
        :type TemplateId: str
        :param _Describe: 录像上云计划描述
        :type Describe: str
        :param _LifeCycle: 云文件生命周期
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Status: 录像上云计划状态，1:正常使用中，0:删除中，无法使用
        :type Status: int
        :param _ChannelCount: 通道数量
        :type ChannelCount: int
        :param _CreateAt: 创建时间
        :type CreateAt: str
        :param _UpdateAt: 修改时间
        :type UpdateAt: str
        """
        self._PlanId = None
        self._PlanName = None
        self._TemplateId = None
        self._Describe = None
        self._LifeCycle = None
        self._Status = None
        self._ChannelCount = None
        self._CreateAt = None
        self._UpdateAt = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanName(self):
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def LifeCycle(self):
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ChannelCount(self):
        return self._ChannelCount

    @ChannelCount.setter
    def ChannelCount(self, ChannelCount):
        self._ChannelCount = ChannelCount

    @property
    def CreateAt(self):
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        self._Describe = params.get("Describe")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        self._Status = params.get("Status")
        self._ChannelCount = params.get("ChannelCount")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRecordBackupPlanRequest(AbstractModel):
    """AddRecordBackupPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 录制模板ID（录像计划关联的模板ID，从查询录像上云模板列表接口ListRecordBackupTemplates中获取）
        :type TemplateId: str
        :param _PlanName: 录像计划名称（仅支持中文、英文、数字、_、-，长度不超过32个字符，计划名称全局唯一，不能为空，不能重复）
        :type PlanName: str
        :param _Describe: 录像计划描述（仅支持中文、英文、数字、_、-，长度不超过128个字符）
        :type Describe: str
        :param _LifeCycle: 生命周期（录像文件生命周期设置，管理文件冷、热存储的时间）
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Channels: 通道及通道所属设备（添加录像的设备的通道信息，一次添加通道总数不超过5000个，包括组织目录下的通道数量）
        :type Channels: list of ChannelInfo
        :param _OrganizationId: 添加组织目录下所有设备通道（Json数组，可以为空，通道总数量不超过5000个（包括Channel字段的数量））
        :type OrganizationId: list of str
        """
        self._TemplateId = None
        self._PlanName = None
        self._Describe = None
        self._LifeCycle = None
        self._Channels = None
        self._OrganizationId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def PlanName(self):
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def LifeCycle(self):
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Channels(self):
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._PlanName = params.get("PlanName")
        self._Describe = params.get("Describe")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        if params.get("Channels") is not None:
            self._Channels = []
            for item in params.get("Channels"):
                obj = ChannelInfo()
                obj._deserialize(item)
                self._Channels.append(obj)
        self._OrganizationId = params.get("OrganizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRecordBackupPlanResponse(AbstractModel):
    """AddRecordBackupPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.AddRecordBackupPlanData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AddRecordBackupPlanData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddRecordBackupTemplateData(AbstractModel):
    """新增录像上云模板返回数据

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param _TemplateName: 模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateName: str
        :param _TimeSections: 上云时间段（按周进行设置，支持一天设置多个时间段，每个时间段不小于10分钟）
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSections: list of RecordTemplateTimeSections
        :param _DevTimeSections: 录像时间段（按周进行设置，支持一天设置多个时间段，每个时间段不小于10分钟）
注意：此字段可能返回 null，表示取不到有效值。
        :type DevTimeSections: list of RecordTemplateTimeSections
        :param _Scale: 上云倍速（支持1，2，4倍速）
注意：此字段可能返回 null，表示取不到有效值。
        :type Scale: int
        :param _CreateAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateAt: str
        :param _UpdateAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateAt: str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TimeSections = None
        self._DevTimeSections = None
        self._Scale = None
        self._CreateAt = None
        self._UpdateAt = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections

    @property
    def DevTimeSections(self):
        return self._DevTimeSections

    @DevTimeSections.setter
    def DevTimeSections(self, DevTimeSections):
        self._DevTimeSections = DevTimeSections

    @property
    def Scale(self):
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale

    @property
    def CreateAt(self):
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        if params.get("DevTimeSections") is not None:
            self._DevTimeSections = []
            for item in params.get("DevTimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._DevTimeSections.append(obj)
        self._Scale = params.get("Scale")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRecordBackupTemplateRequest(AbstractModel):
    """AddRecordBackupTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateName: 模板名称（仅支持中文、英文、数字、_、-，长度不超过32个字符，模板名称全局唯一，不能为空，不能重复）
        :type TemplateName: str
        :param _TimeSections: 上云时间段（按周进行设置，支持一天设置多个时间段，每个时间段不小于10分钟）
        :type TimeSections: list of RecordTemplateTimeSections
        :param _DevTimeSections: 录像时间段（按周进行设置，支持一天设置多个时间段，每个时间段不小于10分钟）
        :type DevTimeSections: list of RecordTemplateTimeSections
        :param _Scale: 上云倍速（支持1，2，4倍速）
        :type Scale: int
        """
        self._TemplateName = None
        self._TimeSections = None
        self._DevTimeSections = None
        self._Scale = None

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections

    @property
    def DevTimeSections(self):
        return self._DevTimeSections

    @DevTimeSections.setter
    def DevTimeSections(self, DevTimeSections):
        self._DevTimeSections = DevTimeSections

    @property
    def Scale(self):
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        if params.get("DevTimeSections") is not None:
            self._DevTimeSections = []
            for item in params.get("DevTimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._DevTimeSections.append(obj)
        self._Scale = params.get("Scale")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRecordBackupTemplateResponse(AbstractModel):
    """AddRecordBackupTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.AddRecordBackupTemplateData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AddRecordBackupTemplateData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddRecordPlanRequest(AbstractModel):
    """AddRecordPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanName: 实时上云计划名称，仅支持中文、英文、数字、_、-，长度不超过32个字符，计划名称全局唯一，不能为空，不能重复
        :type PlanName: str
        :param _TemplateId: 实时上云模板ID
        :type TemplateId: str
        :param _LifeCycle: 生命周期
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Describe: 上云计划描述，仅支持中文、英文、数字、_、-，长度不超过128个字符 
        :type Describe: str
        :param _StreamType: 码流类型，default:不指定码流类型，以设备默认推送类型为主， main:主码流，sub:子码流，其他根据设备能力集自定义，不填按默认类型处理，长度不能超过32个字节
        :type StreamType: str
        :param _Channels: 添加录像的设备的通道信息，一次添加通道总数不超过5000个，包括组织目录下的通道数量
        :type Channels: list of ChannelInfo
        :param _OrganizationId: 添加组织目录下所有设备通道，Json数组，可以为空，通道总数量不超过5000个（包括Channel字段的数量）
        :type OrganizationId: list of str
        """
        self._PlanName = None
        self._TemplateId = None
        self._LifeCycle = None
        self._Describe = None
        self._StreamType = None
        self._Channels = None
        self._OrganizationId = None

    @property
    def PlanName(self):
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def LifeCycle(self):
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def StreamType(self):
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def Channels(self):
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId


    def _deserialize(self, params):
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        self._Describe = params.get("Describe")
        self._StreamType = params.get("StreamType")
        if params.get("Channels") is not None:
            self._Channels = []
            for item in params.get("Channels"):
                obj = ChannelInfo()
                obj._deserialize(item)
                self._Channels.append(obj)
        self._OrganizationId = params.get("OrganizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRecordPlanResponse(AbstractModel):
    """AddRecordPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.RecordPlanOptData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = RecordPlanOptData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddRecordRetrieveTaskData(AbstractModel):
    """查询取回任务详情返回数据

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _StartTime: 取回录像的开始时间
        :type StartTime: int
        :param _EndTime: 取回录像的结束时间
        :type EndTime: int
        :param _Mode: 取回模式，1:极速模式，其他暂不支持
        :type Mode: int
        :param _Expiration: 副本有效期
        :type Expiration: int
        :param _Status: 任务状态，0:已取回，1:取回中，2:待取回
        :type Status: int
        :param _Capacity: 取回容量，单位MB
        :type Capacity: float
        :param _Describe: 任务描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
        """
        self._TaskId = None
        self._TaskName = None
        self._StartTime = None
        self._EndTime = None
        self._Mode = None
        self._Expiration = None
        self._Status = None
        self._Capacity = None
        self._Describe = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Expiration(self):
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Capacity(self):
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Mode = params.get("Mode")
        self._Expiration = params.get("Expiration")
        self._Status = params.get("Status")
        self._Capacity = params.get("Capacity")
        self._Describe = params.get("Describe")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRecordRetrieveTaskRequest(AbstractModel):
    """AddRecordRetrieveTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务名称，仅支持中文、英文、数字、_、-，长度不超过32个字符，模板名称全局唯一，不能为空，不能重复
        :type TaskName: str
        :param _StartTime: 取回录像的开始时间，UTC秒数，例如：1662114146，开始和结束时间段最长为一天，且不能跨天
        :type StartTime: int
        :param _EndTime: 取回录像的结束时间，UTC秒数，例如：1662114146，开始和结束时间段最长为一天，且不能跨天
        :type EndTime: int
        :param _Mode: 取回模式， 1:极速模式，其他暂不支持
        :type Mode: int
        :param _Expiration: 取回录像副本有效期，最小为1天，最大为365天
        :type Expiration: int
        :param _Channels: 设备通道，一个任务最多32个设备通道
        :type Channels: list of ChannelInfo
        :param _Describe: 取回任务描述
        :type Describe: str
        """
        self._TaskName = None
        self._StartTime = None
        self._EndTime = None
        self._Mode = None
        self._Expiration = None
        self._Channels = None
        self._Describe = None

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Expiration(self):
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def Channels(self):
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Mode = params.get("Mode")
        self._Expiration = params.get("Expiration")
        if params.get("Channels") is not None:
            self._Channels = []
            for item in params.get("Channels"):
                obj = ChannelInfo()
                obj._deserialize(item)
                self._Channels.append(obj)
        self._Describe = params.get("Describe")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRecordRetrieveTaskResponse(AbstractModel):
    """AddRecordRetrieveTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.AddRecordRetrieveTaskData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AddRecordRetrieveTaskData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddRecordTemplateRequest(AbstractModel):
    """AddRecordTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateName: 模板名称， 仅支持中文、英文、数字、_、-，长度不超过32个字符，模板名称全局唯一，不能为空，不能重复
        :type TemplateName: str
        :param _TimeSections: 上云时间段，按周进行设置，支持一天设置多个时间段，每个时间段不小于10分钟
        :type TimeSections: list of RecordTemplateTimeSections
        """
        self._TemplateName = None
        self._TimeSections = None

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRecordTemplateResponse(AbstractModel):
    """AddRecordTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.RecordTemplateInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = RecordTemplateInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddStreamAuthData(AbstractModel):
    """设置推拉流鉴权返回数据结构

    """

    def __init__(self):
        r"""
        :param _Id: 鉴权配置ID（uuid）
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _PullState: 是否开播放鉴权（1:开启,0:关闭）
注意：此字段可能返回 null，表示取不到有效值。
        :type PullState: int
        :param _PullSecret: 播放密钥（仅支持字母数字，长度0-10位）
注意：此字段可能返回 null，表示取不到有效值。
        :type PullSecret: str
        :param _PullExpired: 播放过期时间（单位：分钟）
注意：此字段可能返回 null，表示取不到有效值。
        :type PullExpired: int
        :param _PushState: 是否开启推流鉴权（1:开启,0:关闭）
注意：此字段可能返回 null，表示取不到有效值。
        :type PushState: int
        :param _PushSecret: 推流密钥（仅支持字母数字，长度0-10位）
注意：此字段可能返回 null，表示取不到有效值。
        :type PushSecret: str
        :param _PushExpired: 推流过期时间（单位：分钟）
注意：此字段可能返回 null，表示取不到有效值。
        :type PushExpired: int
        :param _AppId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        """
        self._Id = None
        self._PullState = None
        self._PullSecret = None
        self._PullExpired = None
        self._PushState = None
        self._PushSecret = None
        self._PushExpired = None
        self._AppId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PullState(self):
        return self._PullState

    @PullState.setter
    def PullState(self, PullState):
        self._PullState = PullState

    @property
    def PullSecret(self):
        return self._PullSecret

    @PullSecret.setter
    def PullSecret(self, PullSecret):
        self._PullSecret = PullSecret

    @property
    def PullExpired(self):
        return self._PullExpired

    @PullExpired.setter
    def PullExpired(self, PullExpired):
        self._PullExpired = PullExpired

    @property
    def PushState(self):
        return self._PushState

    @PushState.setter
    def PushState(self, PushState):
        self._PushState = PushState

    @property
    def PushSecret(self):
        return self._PushSecret

    @PushSecret.setter
    def PushSecret(self, PushSecret):
        self._PushSecret = PushSecret

    @property
    def PushExpired(self):
        return self._PushExpired

    @PushExpired.setter
    def PushExpired(self, PushExpired):
        self._PushExpired = PushExpired

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PullState = params.get("PullState")
        self._PullSecret = params.get("PullSecret")
        self._PullExpired = params.get("PullExpired")
        self._PushState = params.get("PushState")
        self._PushSecret = params.get("PushSecret")
        self._PushExpired = params.get("PushExpired")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddStreamAuthRequest(AbstractModel):
    """AddStreamAuth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 鉴权配置ID（uuid）
        :type Id: str
        :param _PullState: 是否开播放鉴权（1:开启,0:关闭）
        :type PullState: int
        :param _PullSecret: 播放密钥（仅支持字母数字，长度0-10位）
        :type PullSecret: str
        :param _PullExpired: 播放过期时间（单位：分钟）
        :type PullExpired: int
        :param _PushState: 是否开启推流鉴权（1:开启,0:关闭）
        :type PushState: int
        :param _PushSecret: 推流密钥（仅支持字母数字，长度0-10位）
        :type PushSecret: str
        :param _PushExpired: 推流过期时间（单位：分钟）
        :type PushExpired: int
        """
        self._Id = None
        self._PullState = None
        self._PullSecret = None
        self._PullExpired = None
        self._PushState = None
        self._PushSecret = None
        self._PushExpired = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PullState(self):
        return self._PullState

    @PullState.setter
    def PullState(self, PullState):
        self._PullState = PullState

    @property
    def PullSecret(self):
        return self._PullSecret

    @PullSecret.setter
    def PullSecret(self, PullSecret):
        self._PullSecret = PullSecret

    @property
    def PullExpired(self):
        return self._PullExpired

    @PullExpired.setter
    def PullExpired(self, PullExpired):
        self._PullExpired = PullExpired

    @property
    def PushState(self):
        return self._PushState

    @PushState.setter
    def PushState(self, PushState):
        self._PushState = PushState

    @property
    def PushSecret(self):
        return self._PushSecret

    @PushSecret.setter
    def PushSecret(self, PushSecret):
        self._PushSecret = PushSecret

    @property
    def PushExpired(self):
        return self._PushExpired

    @PushExpired.setter
    def PushExpired(self, PushExpired):
        self._PushExpired = PushExpired


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PullState = params.get("PullState")
        self._PullSecret = params.get("PullSecret")
        self._PullExpired = params.get("PullExpired")
        self._PushState = params.get("PushState")
        self._PushSecret = params.get("PushSecret")
        self._PushExpired = params.get("PushExpired")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddStreamAuthResponse(AbstractModel):
    """AddStreamAuth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设置推拉流鉴权返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.AddStreamAuthData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AddStreamAuthData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddUserDeviceRequest(AbstractModel):
    """AddUserDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 设备名称，仅支持中文、英文、数字、_、-，长度不超过32个字符；（设备名称无需全局唯一，可以重复）
        :type Name: str
        :param _AccessProtocol: 设备接入协议（1:RTMP,2:GB,3:GW,4:IVCP）
        :type AccessProtocol: int
        :param _Type: 设备类型，1:IPC,2:NVR；（若设备接入协议选择RTMP,IVCP，则设备类型只能选择IPC）
        :type Type: int
        :param _OrganizationId: 设备所属组织ID，从查询组织接口DescribeOrganization中获取
        :type OrganizationId: str
        :param _ClusterId: 设备接入服务节点ID（从查询设备可用服务节点接口DescribeDeviceRegion中获取的Value字段）
        :type ClusterId: str
        :param _TransportProtocol: 设备流传输协议，1:UDP,2:TCP；(国标设备有效，不填写则默认UDP协议)
        :type TransportProtocol: int
        :param _Password: 设备密码（国标，网关设备必填，仅支持数字组合，长度为1-64个字符）
        :type Password: str
        :param _Description: 设备描述，仅支持中文、英文、数字、_、-，长度不超过128个字符
        :type Description: str
        :param _GatewayId: 设备接入网关ID，从查询网关列表接口中ListGateways获取（仅网关接入需要）
        :type GatewayId: str
        :param _ProtocolType: 网关接入协议类型（从查询网关接入协议接口DescribeGatewayProtocol中获取）1.海康SDK，2.大华SDK，3.宇视SDK，4.Onvif（仅网关接入需要）
        :type ProtocolType: int
        :param _Ip: 设备接入IP（仅网关接入需要）
        :type Ip: str
        :param _Port: 设备端口（仅网关接入需要）
        :type Port: int
        :param _Username: 设备用户名（仅网关接入需要）
        :type Username: str
        :param _SNCode: 设备 SN，仅IVCP 协议设备需要
        :type SNCode: str
        """
        self._Name = None
        self._AccessProtocol = None
        self._Type = None
        self._OrganizationId = None
        self._ClusterId = None
        self._TransportProtocol = None
        self._Password = None
        self._Description = None
        self._GatewayId = None
        self._ProtocolType = None
        self._Ip = None
        self._Port = None
        self._Username = None
        self._SNCode = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AccessProtocol(self):
        return self._AccessProtocol

    @AccessProtocol.setter
    def AccessProtocol(self, AccessProtocol):
        self._AccessProtocol = AccessProtocol

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TransportProtocol(self):
        return self._TransportProtocol

    @TransportProtocol.setter
    def TransportProtocol(self, TransportProtocol):
        self._TransportProtocol = TransportProtocol

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ProtocolType(self):
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def SNCode(self):
        return self._SNCode

    @SNCode.setter
    def SNCode(self, SNCode):
        self._SNCode = SNCode


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AccessProtocol = params.get("AccessProtocol")
        self._Type = params.get("Type")
        self._OrganizationId = params.get("OrganizationId")
        self._ClusterId = params.get("ClusterId")
        self._TransportProtocol = params.get("TransportProtocol")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._GatewayId = params.get("GatewayId")
        self._ProtocolType = params.get("ProtocolType")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Username = params.get("Username")
        self._SNCode = params.get("SNCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserDeviceResponse(AbstractModel):
    """AddUserDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 增加设备返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.AddDeviceData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AddDeviceData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class BaseAIResultInfo(AbstractModel):
    """通用AI识别结果信息

    """

    def __init__(self):
        r"""
        :param _Name: 名称。返回值有人体识别结果名称(person)、宠物识别结果名称(cat和dog) 、车辆车牌识别结果名称(vehicle)
        :type Name: str
        :param _Score: 置信度
        :type Score: int
        :param _Location: 截图中坐标信息
        :type Location: :class:`tencentcloud.iss.v20230517.models.Location`
        """
        self._Name = None
        self._Score = None
        self._Location = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Score = params.get("Score")
        if params.get("Location") is not None:
            self._Location = Location()
            self._Location._deserialize(params.get("Location"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchOperateDeviceData(AbstractModel):
    """批量操作设备返回结果

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID（用于在查询任务的子任务列表接口ListSubTasks中查询任务进度）
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchOperateDeviceRequest(AbstractModel):
    """BatchOperateDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceIds: 设备 ID 数组（从获取设备列表接口ListDevices中获取）
        :type DeviceIds: list of str
        :param _Cmd: 操作命令（enable：启用；disable：禁用；delete：删除；upgrade：固件升级；reset：恢复出厂设置；reboot：重启）
        :type Cmd: str
        """
        self._DeviceIds = None
        self._Cmd = None

    @property
    def DeviceIds(self):
        return self._DeviceIds

    @DeviceIds.setter
    def DeviceIds(self, DeviceIds):
        self._DeviceIds = DeviceIds

    @property
    def Cmd(self):
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd


    def _deserialize(self, params):
        self._DeviceIds = params.get("DeviceIds")
        self._Cmd = params.get("Cmd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchOperateDeviceResponse(AbstractModel):
    """BatchOperateDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.BatchOperateDeviceData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = BatchOperateDeviceData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class BitRateInfo(AbstractModel):
    """视频通道码率返回结果

    """

    def __init__(self):
        r"""
        :param _ChannelId: 通道Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelId: str
        :param _Bitrate: 码率,单位:kbps
注意：此字段可能返回 null，表示取不到有效值。
        :type Bitrate: float
        """
        self._ChannelId = None
        self._Bitrate = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Bitrate(self):
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._Bitrate = params.get("Bitrate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BodyAIResultInfo(AbstractModel):
    """人体识别结果详情

    """

    def __init__(self):
        r"""
        :param _Time: 时间字符串
        :type Time: str
        :param _Url: 截图 URL
        :type Url: str
        :param _BodyInfo: 人体信息
        :type BodyInfo: list of BaseAIResultInfo
        """
        self._Time = None
        self._Url = None
        self._BodyInfo = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def BodyInfo(self):
        return self._BodyInfo

    @BodyInfo.setter
    def BodyInfo(self, BodyInfo):
        self._BodyInfo = BodyInfo


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Url = params.get("Url")
        if params.get("BodyInfo") is not None:
            self._BodyInfo = []
            for item in params.get("BodyInfo"):
                obj = BaseAIResultInfo()
                obj._deserialize(item)
                self._BodyInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CarAIResultInfo(AbstractModel):
    """车辆车牌识别结果信息

    """

    def __init__(self):
        r"""
        :param _Serial: 车系
        :type Serial: str
        :param _Brand: 车辆品牌
        :type Brand: str
        :param _Type: 车辆类型
        :type Type: str
        :param _Color: 车辆颜色
        :type Color: str
        :param _Confidence: 置信度，0 - 100
        :type Confidence: int
        :param _Year: 年份，识别不出年份时返回0
        :type Year: int
        :param _PlateContent: 车牌信息
        :type PlateContent: :class:`tencentcloud.iss.v20230517.models.PlateContent`
        :param _Location: 截图中坐标信息
        :type Location: :class:`tencentcloud.iss.v20230517.models.Location`
        """
        self._Serial = None
        self._Brand = None
        self._Type = None
        self._Color = None
        self._Confidence = None
        self._Year = None
        self._PlateContent = None
        self._Location = None

    @property
    def Serial(self):
        return self._Serial

    @Serial.setter
    def Serial(self, Serial):
        self._Serial = Serial

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Year(self):
        return self._Year

    @Year.setter
    def Year(self, Year):
        self._Year = Year

    @property
    def PlateContent(self):
        return self._PlateContent

    @PlateContent.setter
    def PlateContent(self, PlateContent):
        self._PlateContent = PlateContent

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location


    def _deserialize(self, params):
        self._Serial = params.get("Serial")
        self._Brand = params.get("Brand")
        self._Type = params.get("Type")
        self._Color = params.get("Color")
        self._Confidence = params.get("Confidence")
        self._Year = params.get("Year")
        if params.get("PlateContent") is not None:
            self._PlateContent = PlateContent()
            self._PlateContent._deserialize(params.get("PlateContent"))
        if params.get("Location") is not None:
            self._Location = Location()
            self._Location._deserialize(params.get("Location"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelInfo(AbstractModel):
    """通道及通道所属设备信息

    """

    def __init__(self):
        r"""
        :param _DeviceId: 通道所属的设备ID
        :type DeviceId: str
        :param _ChannelId: 设备通道ID，一个设备通道只允许被一个上云计划添加
        :type ChannelId: str
        """
        self._DeviceId = None
        self._ChannelId = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ChannelId(self):
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
        


class CheckDomainRequest(AbstractModel):
    """CheckDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlayDomain: 播放域名
        :type PlayDomain: str
        :param _InternalDomain: CNAME 记录值
        :type InternalDomain: str
        """
        self._PlayDomain = None
        self._InternalDomain = None

    @property
    def PlayDomain(self):
        return self._PlayDomain

    @PlayDomain.setter
    def PlayDomain(self, PlayDomain):
        self._PlayDomain = PlayDomain

    @property
    def InternalDomain(self):
        return self._InternalDomain

    @InternalDomain.setter
    def InternalDomain(self, InternalDomain):
        self._InternalDomain = InternalDomain


    def _deserialize(self, params):
        self._PlayDomain = params.get("PlayDomain")
        self._InternalDomain = params.get("InternalDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckDomainResponse(AbstractModel):
    """CheckDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 是否备案
        :type Data: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class ChefClothAIResultInfo(AbstractModel):
    """厨师服识别结果详情

    """

    def __init__(self):
        r"""
        :param _Time: 时间字符串
        :type Time: str
        :param _Url: 截图 URL
        :type Url: str
        :param _ChefClothInfoInfo: 厨师服信息
        :type ChefClothInfoInfo: list of BaseAIResultInfo
        """
        self._Time = None
        self._Url = None
        self._ChefClothInfoInfo = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def ChefClothInfoInfo(self):
        return self._ChefClothInfoInfo

    @ChefClothInfoInfo.setter
    def ChefClothInfoInfo(self, ChefClothInfoInfo):
        self._ChefClothInfoInfo = ChefClothInfoInfo


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Url = params.get("Url")
        if params.get("ChefClothInfoInfo") is not None:
            self._ChefClothInfoInfo = []
            for item in params.get("ChefClothInfoInfo"):
                obj = BaseAIResultInfo()
                obj._deserialize(item)
                self._ChefClothInfoInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChefHatAIResultInfo(AbstractModel):
    """厨师帽识别结果详情

    """

    def __init__(self):
        r"""
        :param _Time: 时间字符串
        :type Time: str
        :param _Url: 截图 URL
        :type Url: str
        :param _ChefHatInfo: 厨师帽信息
        :type ChefHatInfo: list of BaseAIResultInfo
        """
        self._Time = None
        self._Url = None
        self._ChefHatInfo = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def ChefHatInfo(self):
        return self._ChefHatInfo

    @ChefHatInfo.setter
    def ChefHatInfo(self, ChefHatInfo):
        self._ChefHatInfo = ChefHatInfo


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Url = params.get("Url")
        if params.get("ChefHatInfo") is not None:
            self._ChefHatInfo = []
            for item in params.get("ChefHatInfo"):
                obj = BaseAIResultInfo()
                obj._deserialize(item)
                self._ChefHatInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDevicePTZRequest(AbstractModel):
    """ControlDevicePTZ请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelId: 通道 ID（从通道查询接口DescribeDeviceChannel中获取）
        :type ChannelId: str
        :param _Type: 命令类型（上:up,下:down,左:left,右:right
上左:leftup,上右:rightup,下左:leftdown,下右:rightdown
放大:zoomin,缩小:zoomout
聚焦远:focusfar,聚焦近:focusnear
光圈放大:irisin,光圈缩小:irisout）
        :type Type: str
        :param _Speed: 命令描述（速度值范围1-8）
        :type Speed: int
        """
        self._ChannelId = None
        self._Type = None
        self._Speed = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Speed(self):
        return self._Speed

    @Speed.setter
    def Speed(self, Speed):
        self._Speed = Speed


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._Type = params.get("Type")
        self._Speed = params.get("Speed")
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
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ControlDevicePresetRequest(AbstractModel):
    """ControlDevicePreset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelId: 通道 ID（从通道查询接口DescribeDeviceChannel中获取）
        :type ChannelId: str
        :param _Cmd: 命令（goto:预置位调用；
set:预置位设置；
del:预置位删除）
        :type Cmd: str
        :param _Index: 预置位索引（只支持1-10的索引位置，超出报错）
        :type Index: int
        """
        self._ChannelId = None
        self._Cmd = None
        self._Index = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Cmd(self):
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._Cmd = params.get("Cmd")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDevicePresetResponse(AbstractModel):
    """ControlDevicePreset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ControlDeviceStreamData(AbstractModel):
    """获取开流地址返回数据

    """

    def __init__(self):
        r"""
        :param _Flv: flv 流地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Flv: str
        :param _Hls: hls 流地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Hls: str
        :param _Rtmp: rtmp 流地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Rtmp: str
        """
        self._Flv = None
        self._Hls = None
        self._Rtmp = None

    @property
    def Flv(self):
        return self._Flv

    @Flv.setter
    def Flv(self, Flv):
        self._Flv = Flv

    @property
    def Hls(self):
        return self._Hls

    @Hls.setter
    def Hls(self, Hls):
        self._Hls = Hls

    @property
    def Rtmp(self):
        return self._Rtmp

    @Rtmp.setter
    def Rtmp(self, Rtmp):
        self._Rtmp = Rtmp


    def _deserialize(self, params):
        self._Flv = params.get("Flv")
        self._Hls = params.get("Hls")
        self._Rtmp = params.get("Rtmp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDeviceStreamRequest(AbstractModel):
    """ControlDeviceStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelId: 通道 ID（从通道查询接口DescribeDeviceChannel中获取）
        :type ChannelId: str
        :param _StreamType: 流类型（1:主码流；
2:子码流（不可以和 Resolution 同时下发））
        :type StreamType: str
        :param _Resolution: 分辨率（1:QCIF；
2:CIF；
3:4CIF；
4:D1；
5:720P；
6:1080P/I；
自定义的19201080等等（需设备支持）（不可以和 StreamType 同时下发））
        :type Resolution: str
        :param _IsInternal: 是否内网
        :type IsInternal: bool
        """
        self._ChannelId = None
        self._StreamType = None
        self._Resolution = None
        self._IsInternal = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def StreamType(self):
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def IsInternal(self):
        return self._IsInternal

    @IsInternal.setter
    def IsInternal(self, IsInternal):
        self._IsInternal = IsInternal


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._StreamType = params.get("StreamType")
        self._Resolution = params.get("Resolution")
        self._IsInternal = params.get("IsInternal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDeviceStreamResponse(AbstractModel):
    """ControlDeviceStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.ControlDeviceStreamData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ControlDeviceStreamData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ControlRecordRequest(AbstractModel):
    """ControlRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelId: 通道ID（录像播放地址格式 https://${domain}/live/${ChannelId}@${Session}）
        :type ChannelId: str
        :param _Session: 录像会话 ID （ 录像播放地址格式 https://${domain}/live/${ChannelId}@${Session}）
        :type Session: str
        :param _ControlAction: 录像操作类型 （play:播放；pause:暂停 ；stop:关闭）
        :type ControlAction: str
        :param _Position: 跳转进度 （ 参数应大于等于0，跳转到录像开始时间的相对时间（单位秒），例如0就是跳转到录像开始的时间,不可以和 Scale 参数同时出现）
        :type Position: int
        :param _Scale: 速度 （ 范围（0.25,0.5,1,2,4,8），不可以和 Pos 参数同时出现）
        :type Scale: float
        """
        self._ChannelId = None
        self._Session = None
        self._ControlAction = None
        self._Position = None
        self._Scale = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Session(self):
        return self._Session

    @Session.setter
    def Session(self, Session):
        self._Session = Session

    @property
    def ControlAction(self):
        return self._ControlAction

    @ControlAction.setter
    def ControlAction(self, ControlAction):
        self._ControlAction = ControlAction

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def Scale(self):
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._Session = params.get("Session")
        self._ControlAction = params.get("ControlAction")
        self._Position = params.get("Position")
        self._Scale = params.get("Scale")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlRecordResponse(AbstractModel):
    """ControlRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ControlRecordTimelineRequest(AbstractModel):
    """ControlRecordTimeline请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelId: 通道 ID（从通道查询接口DescribeDeviceChannel中获取）
        :type ChannelId: str
        :param _Start: 起始时间
        :type Start: int
        :param _End: 结束时间
        :type End: int
        """
        self._ChannelId = None
        self._Start = None
        self._End = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Start(self):
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._Start = params.get("Start")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlRecordTimelineResponse(AbstractModel):
    """ControlRecordTimeline返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of Timeline
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = Timeline()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteAITaskRequest(AbstractModel):
    """DeleteAITask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: AI任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAITaskResponse(AbstractModel):
    """DeleteAITask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteDomainRequest(AbstractModel):
    """DeleteDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 域名 ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainResponse(AbstractModel):
    """DeleteDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteGatewayRequest(AbstractModel):
    """DeleteGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关索引ID（从获取网关列表接口ListGateways中获取）
        :type GatewayId: str
        """
        self._GatewayId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGatewayResponse(AbstractModel):
    """DeleteGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteOrganizationRequest(AbstractModel):
    """DeleteOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrganizationId: 组织ID（从查询组织接口DescribeOrganization中获取）
        :type OrganizationId: str
        """
        self._OrganizationId = None

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationResponse(AbstractModel):
    """DeleteOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRecordBackupPlanRequest(AbstractModel):
    """DeleteRecordBackupPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 录像上云计划ID（从查询录像上云计划列表接口ListRecordBackupPlans中获取）
        :type PlanId: str
        """
        self._PlanId = None

    @property
    def PlanId(self):
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
        


class DeleteRecordBackupPlanResponse(AbstractModel):
    """DeleteRecordBackupPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRecordBackupTemplateRequest(AbstractModel):
    """DeleteRecordBackupTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID（从查询录像上云模板列表接口ListRecordBackupTemplates中获取）
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
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
        


class DeleteRecordBackupTemplateResponse(AbstractModel):
    """DeleteRecordBackupTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
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
        :param _PlanId: 上云计划ID
        :type PlanId: str
        """
        self._PlanId = None

    @property
    def PlanId(self):
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRecordRetrieveTaskRequest(AbstractModel):
    """DeleteRecordRetrieveTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 取回任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordRetrieveTaskResponse(AbstractModel):
    """DeleteRecordRetrieveTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRecordTemplateRequest(AbstractModel):
    """DeleteRecordTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
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
        


class DeleteRecordTemplateResponse(AbstractModel):
    """DeleteRecordTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteUserDeviceRequest(AbstractModel):
    """DeleteUserDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID（从获取设备列表ListDevices接口中获取）
        :type DeviceId: str
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
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
        


class DeleteUserDeviceResponse(AbstractModel):
    """DeleteUserDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAITaskRequest(AbstractModel):
    """DescribeAITask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: AI任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAITaskResponse(AbstractModel):
    """DescribeAITask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: AI任务详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iss.v20230517.models.AITaskInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AITaskInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeAITaskResultRequest(AbstractModel):
    """DescribeAITaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: AI 任务 ID
        :type TaskId: str
        :param _ChannelId: 通道ID
        :type ChannelId: str
        :param _Object: 桶内文件的路径。
        :type Object: str
        :param _DetectType: AI 任务识别类型。可选值为 Facemask(口罩识别)、Chefhat(厨师帽识别)、Smoking(抽烟检测)、Chefcloth(厨师服识别)、PhoneCall(接打电话识别)、Pet(宠物识别)、Body(人体识别)和 Car(车辆车牌识别)
        :type DetectType: str
        :param _BeginTime: 开始时间时间。秒级时间戳。开始时间和结束时间跨度小于等于30天
        :type BeginTime: str
        :param _EndTime: 结束时间时间。秒级时间戳。开始时间和结束时间跨度小于等于30天
        :type EndTime: str
        :param _PageNumber: 页码。默认为1
        :type PageNumber: int
        :param _PageSize: 每页 AI 识别结果数量。可选值1～100，默认为10（按时间倒序显示识别结果）
        :type PageSize: int
        """
        self._TaskId = None
        self._ChannelId = None
        self._Object = None
        self._DetectType = None
        self._BeginTime = None
        self._EndTime = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Object(self):
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def DetectType(self):
        return self._DetectType

    @DetectType.setter
    def DetectType(self, DetectType):
        self._DetectType = DetectType

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ChannelId = params.get("ChannelId")
        self._Object = params.get("Object")
        self._DetectType = params.get("DetectType")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAITaskResultResponse(AbstractModel):
    """DescribeAITaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: AI识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iss.v20230517.models.AITaskResultData`
        :param _TotalCount: AI识别结果数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AITaskResultData()
            self._Data._deserialize(params.get("Data"))
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCNAMERequest(AbstractModel):
    """DescribeCNAME请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 服务节点 ID（从查询域名可绑定服务节点接口DescribeDomainRegion中获取）
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCNAMEResponse(AbstractModel):
    """DescribeCNAME返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: CNAME 记录值
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeDeviceChannelData(AbstractModel):
    """查询设备通道信息返回结果

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param _ChannelId: 通道 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelId: str
        :param _ChannelCode: 通道编码
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelCode: str
        :param _Name: 通道名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Status: 流状态（0:未传输,1:传输中）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _PTZType: 是否可控 Ptz（0:不可控,1:可控）
注意：此字段可能返回 null，表示取不到有效值。
        :type PTZType: int
        :param _Manufacturer: 通道厂商
注意：此字段可能返回 null，表示取不到有效值。
        :type Manufacturer: str
        :param _Resolution: 通道支持分辨率（分辨率列表由‘/’隔开，国标协议样例（6/3），自定义样例（12800960/640480））
注意：此字段可能返回 null，表示取不到有效值。
        :type Resolution: str
        :param _State: 通道在离线状态（0:离线,1:在线）
注意：此字段可能返回 null，表示取不到有效值。
        :type State: int
        :param _Region: 所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self._DeviceId = None
        self._ChannelId = None
        self._ChannelCode = None
        self._Name = None
        self._Status = None
        self._PTZType = None
        self._Manufacturer = None
        self._Resolution = None
        self._State = None
        self._Region = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelCode(self):
        return self._ChannelCode

    @ChannelCode.setter
    def ChannelCode(self, ChannelCode):
        self._ChannelCode = ChannelCode

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PTZType(self):
        return self._PTZType

    @PTZType.setter
    def PTZType(self, PTZType):
        self._PTZType = PTZType

    @property
    def Manufacturer(self):
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ChannelId = params.get("ChannelId")
        self._ChannelCode = params.get("ChannelCode")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._PTZType = params.get("PTZType")
        self._Manufacturer = params.get("Manufacturer")
        self._Resolution = params.get("Resolution")
        self._State = params.get("State")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceChannelRequest(AbstractModel):
    """DescribeDeviceChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID（从获取设备列表接口ListDevices中获取）
        :type DeviceId: str
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
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
        


class DescribeDeviceChannelResponse(AbstractModel):
    """DescribeDeviceChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: list of DescribeDeviceChannelData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeDeviceChannelData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceData(AbstractModel):
    """查询设备接口返回数据

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param _Code: 设备编码（国标设备即我们为设备生成的20位国标编码，rtmp 设备为10 位设备编码）
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param _Name: 设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _AccessProtocol: 设备接入协议，1:RTMP,2:GB,3:GW 
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessProtocol: int
        :param _Type: 设备类型，1:IPC,2:NVR
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _ClusterId: 设备接入服务节点id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ClusterName: 设备接入服务节点名称

注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param _TransportProtocol: 设备流传输协议，1:UDP,2:TCP 
注意：此字段可能返回 null，表示取不到有效值。
        :type TransportProtocol: int
        :param _Password: 设备密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Description: 设备描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _SipId: sip服务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SipId: str
        :param _SipDomain: sip服务域
注意：此字段可能返回 null，表示取不到有效值。
        :type SipDomain: str
        :param _SipIp: sip服务IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type SipIp: str
        :param _SipPort: sip服务端口
注意：此字段可能返回 null，表示取不到有效值。
        :type SipPort: int
        :param _PushStreamUrl: Rtmp设备推流地址(仅rtmp设备有效)
注意：此字段可能返回 null，表示取不到有效值。
        :type PushStreamUrl: str
        :param _Status: 设备状态，0:未注册,1:在线,2:离线,3:禁用
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _OrganizationId: 设备所属组织ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationId: str
        :param _GatewayId: 设备接入网关ID，从查询网关列表接口中获取（仅网关接入需要）
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayId: str
        :param _GatewayName: 设备所属网关名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayName: str
        :param _ProtocolTypeName: 设备网关协议名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtocolTypeName: str
        :param _ProtocolType: 网关接入协议类型，1.海康SDK，2.大华SDK，3.宇视SDK，4.Onvif（仅网关接入需要）
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtocolType: int
        :param _Ip: 设备接入IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Port: 设备Port
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Username: 设备用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type Username: str
        :param _Region: 设备地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Manufacturer: 设备厂商
注意：此字段可能返回 null，表示取不到有效值。
        :type Manufacturer: str
        :param _AudioSwitch: 音频关开（0：关闭；1：开启）关闭时丢弃音频	
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioSwitch: int
        :param _SubscribeSwitch: 订阅开关（0：关闭；1：开启）默认开启，开启状态下会订阅设备通道变化，仅国标NVR设备有效	
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscribeSwitch: int
        """
        self._DeviceId = None
        self._Code = None
        self._Name = None
        self._AccessProtocol = None
        self._Type = None
        self._ClusterId = None
        self._ClusterName = None
        self._TransportProtocol = None
        self._Password = None
        self._Description = None
        self._SipId = None
        self._SipDomain = None
        self._SipIp = None
        self._SipPort = None
        self._PushStreamUrl = None
        self._Status = None
        self._OrganizationId = None
        self._GatewayId = None
        self._GatewayName = None
        self._ProtocolTypeName = None
        self._ProtocolType = None
        self._Ip = None
        self._Port = None
        self._Username = None
        self._Region = None
        self._Manufacturer = None
        self._AudioSwitch = None
        self._SubscribeSwitch = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AccessProtocol(self):
        return self._AccessProtocol

    @AccessProtocol.setter
    def AccessProtocol(self, AccessProtocol):
        self._AccessProtocol = AccessProtocol

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def TransportProtocol(self):
        return self._TransportProtocol

    @TransportProtocol.setter
    def TransportProtocol(self, TransportProtocol):
        self._TransportProtocol = TransportProtocol

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SipId(self):
        return self._SipId

    @SipId.setter
    def SipId(self, SipId):
        self._SipId = SipId

    @property
    def SipDomain(self):
        return self._SipDomain

    @SipDomain.setter
    def SipDomain(self, SipDomain):
        self._SipDomain = SipDomain

    @property
    def SipIp(self):
        return self._SipIp

    @SipIp.setter
    def SipIp(self, SipIp):
        self._SipIp = SipIp

    @property
    def SipPort(self):
        return self._SipPort

    @SipPort.setter
    def SipPort(self, SipPort):
        self._SipPort = SipPort

    @property
    def PushStreamUrl(self):
        return self._PushStreamUrl

    @PushStreamUrl.setter
    def PushStreamUrl(self, PushStreamUrl):
        self._PushStreamUrl = PushStreamUrl

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GatewayName(self):
        return self._GatewayName

    @GatewayName.setter
    def GatewayName(self, GatewayName):
        self._GatewayName = GatewayName

    @property
    def ProtocolTypeName(self):
        return self._ProtocolTypeName

    @ProtocolTypeName.setter
    def ProtocolTypeName(self, ProtocolTypeName):
        self._ProtocolTypeName = ProtocolTypeName

    @property
    def ProtocolType(self):
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Manufacturer(self):
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def AudioSwitch(self):
        return self._AudioSwitch

    @AudioSwitch.setter
    def AudioSwitch(self, AudioSwitch):
        self._AudioSwitch = AudioSwitch

    @property
    def SubscribeSwitch(self):
        return self._SubscribeSwitch

    @SubscribeSwitch.setter
    def SubscribeSwitch(self, SubscribeSwitch):
        self._SubscribeSwitch = SubscribeSwitch


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Code = params.get("Code")
        self._Name = params.get("Name")
        self._AccessProtocol = params.get("AccessProtocol")
        self._Type = params.get("Type")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._TransportProtocol = params.get("TransportProtocol")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._SipId = params.get("SipId")
        self._SipDomain = params.get("SipDomain")
        self._SipIp = params.get("SipIp")
        self._SipPort = params.get("SipPort")
        self._PushStreamUrl = params.get("PushStreamUrl")
        self._Status = params.get("Status")
        self._OrganizationId = params.get("OrganizationId")
        self._GatewayId = params.get("GatewayId")
        self._GatewayName = params.get("GatewayName")
        self._ProtocolTypeName = params.get("ProtocolTypeName")
        self._ProtocolType = params.get("ProtocolType")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Username = params.get("Username")
        self._Region = params.get("Region")
        self._Manufacturer = params.get("Manufacturer")
        self._AudioSwitch = params.get("AudioSwitch")
        self._SubscribeSwitch = params.get("SubscribeSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicePresetData(AbstractModel):
    """查询设备预置位返回数据

    """

    def __init__(self):
        r"""
        :param _Index: 预置位索引    只支持1-10的索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: int
        :param _Name: 预置位名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._Index = None
        self._Name = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicePresetRequest(AbstractModel):
    """DescribeDevicePreset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelId: 通道ID（从通道查询接口DescribeDeviceChannel中获取）
        :type ChannelId: str
        """
        self._ChannelId = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicePresetResponse(AbstractModel):
    """DescribeDevicePreset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: list of DescribeDevicePresetData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeDevicePresetData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceRegion(AbstractModel):
    """查询设备可接入集群信息

    """

    def __init__(self):
        r"""
        :param _Label: 服务节点描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Value: 服务节点 ID（对应为其他接口中所需的 ClusterId）
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Region: 地域信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self._Label = None
        self._Value = None
        self._Region = None

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Value = params.get("Value")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceRegionRequest(AbstractModel):
    """DescribeDeviceRegion请求参数结构体

    """


class DescribeDeviceRegionResponse(AbstractModel):
    """DescribeDeviceRegion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: list of DescribeDeviceRegion
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeDeviceRegion()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainData(AbstractModel):
    """查询域名详情数据

    """

    def __init__(self):
        r"""
        :param _Id: 域名ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _PlayDomain: 播放域名
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayDomain: str
        :param _InternalDomain: CNAME 记录值
注意：此字段可能返回 null，表示取不到有效值。
        :type InternalDomain: str
        :param _HaveCert: 是否上传证书（0：否，1：是）
注意：此字段可能返回 null，表示取不到有效值。
        :type HaveCert: int
        :param _ClusterId: 服务节点 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ClusterName: 服务节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param _AppId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _CertId: 证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        """
        self._Id = None
        self._PlayDomain = None
        self._InternalDomain = None
        self._HaveCert = None
        self._ClusterId = None
        self._ClusterName = None
        self._AppId = None
        self._CertId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PlayDomain(self):
        return self._PlayDomain

    @PlayDomain.setter
    def PlayDomain(self, PlayDomain):
        self._PlayDomain = PlayDomain

    @property
    def InternalDomain(self):
        return self._InternalDomain

    @InternalDomain.setter
    def InternalDomain(self, InternalDomain):
        self._InternalDomain = InternalDomain

    @property
    def HaveCert(self):
        return self._HaveCert

    @HaveCert.setter
    def HaveCert(self, HaveCert):
        self._HaveCert = HaveCert

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PlayDomain = params.get("PlayDomain")
        self._InternalDomain = params.get("InternalDomain")
        self._HaveCert = params.get("HaveCert")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._AppId = params.get("AppId")
        self._CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainRegionData(AbstractModel):
    """查询域名可绑定集群数据

    """

    def __init__(self):
        r"""
        :param _Label: 服务节点描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Value: 服务节点 ID（对应为其他接口中所需的 ClusterId）
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Region: 地域信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self._Label = None
        self._Value = None
        self._Region = None

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Value = params.get("Value")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainRegionRequest(AbstractModel):
    """DescribeDomainRegion请求参数结构体

    """


class DescribeDomainRegionResponse(AbstractModel):
    """DescribeDomainRegion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: list of DescribeDomainRegionData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeDomainRegionData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainRequest(AbstractModel):
    """DescribeDomain请求参数结构体

    """


class DescribeDomainResponse(AbstractModel):
    """DescribeDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: list of DescribeDomainData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeDomainData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGatewayData(AbstractModel):
    """查询网关信息返回结果

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关索引ID，用于网关查询，更新，删除操作
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayId: str
        :param _GwId: 网关编码，由网关设备生成的唯一编码
注意：此字段可能返回 null，表示取不到有效值。
        :type GwId: str
        :param _Name: 网关名称，仅支持中文、英文、数字、_、-，长度不超过32个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: 网关描述，仅支持中文、英文、数字、_、-，长度不超过128个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _ClusterId: 服务节点id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ClusterName: 服务节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param _Status: 网关状态，0：离线，1:在线
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Version: 网关版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: list of GatewayVersion
        :param _DeviceNum: 网关下挂设备数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceNum: int
        :param _CreatedAt: 激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _Region: 所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self._GatewayId = None
        self._GwId = None
        self._Name = None
        self._Description = None
        self._ClusterId = None
        self._ClusterName = None
        self._Status = None
        self._Version = None
        self._DeviceNum = None
        self._CreatedAt = None
        self._Region = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GwId(self):
        return self._GwId

    @GwId.setter
    def GwId(self, GwId):
        self._GwId = GwId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def DeviceNum(self):
        return self._DeviceNum

    @DeviceNum.setter
    def DeviceNum(self, DeviceNum):
        self._DeviceNum = DeviceNum

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GwId = params.get("GwId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Status = params.get("Status")
        if params.get("Version") is not None:
            self._Version = []
            for item in params.get("Version"):
                obj = GatewayVersion()
                obj._deserialize(item)
                self._Version.append(obj)
        self._DeviceNum = params.get("DeviceNum")
        self._CreatedAt = params.get("CreatedAt")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayMonitor(AbstractModel):
    """查询网关监控信息返回结果

    """

    def __init__(self):
        r"""
        :param _DeviceTotal: 设备接入总数
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceTotal: int
        :param _DeviceOnline: 设备在线数
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceOnline: int
        :param _DeviceOffline: 设备离线数
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceOffline: int
        :param _ChannelTotal: 视频通道总数
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelTotal: int
        :param _ChannelOnline: 视频通道在线数
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelOnline: int
        :param _ChannelOffline: 视频通道离线数
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelOffline: int
        :param _UpFlow: 网关上行流量,单位kbps
注意：此字段可能返回 null，表示取不到有效值。
        :type UpFlow: int
        :param _ChannelPull: 流在传输中的通道数
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelPull: int
        :param _ChannelUnPull: 流未传输中的通道数
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelUnPull: int
        """
        self._DeviceTotal = None
        self._DeviceOnline = None
        self._DeviceOffline = None
        self._ChannelTotal = None
        self._ChannelOnline = None
        self._ChannelOffline = None
        self._UpFlow = None
        self._ChannelPull = None
        self._ChannelUnPull = None

    @property
    def DeviceTotal(self):
        return self._DeviceTotal

    @DeviceTotal.setter
    def DeviceTotal(self, DeviceTotal):
        self._DeviceTotal = DeviceTotal

    @property
    def DeviceOnline(self):
        return self._DeviceOnline

    @DeviceOnline.setter
    def DeviceOnline(self, DeviceOnline):
        self._DeviceOnline = DeviceOnline

    @property
    def DeviceOffline(self):
        return self._DeviceOffline

    @DeviceOffline.setter
    def DeviceOffline(self, DeviceOffline):
        self._DeviceOffline = DeviceOffline

    @property
    def ChannelTotal(self):
        return self._ChannelTotal

    @ChannelTotal.setter
    def ChannelTotal(self, ChannelTotal):
        self._ChannelTotal = ChannelTotal

    @property
    def ChannelOnline(self):
        return self._ChannelOnline

    @ChannelOnline.setter
    def ChannelOnline(self, ChannelOnline):
        self._ChannelOnline = ChannelOnline

    @property
    def ChannelOffline(self):
        return self._ChannelOffline

    @ChannelOffline.setter
    def ChannelOffline(self, ChannelOffline):
        self._ChannelOffline = ChannelOffline

    @property
    def UpFlow(self):
        return self._UpFlow

    @UpFlow.setter
    def UpFlow(self, UpFlow):
        self._UpFlow = UpFlow

    @property
    def ChannelPull(self):
        return self._ChannelPull

    @ChannelPull.setter
    def ChannelPull(self, ChannelPull):
        self._ChannelPull = ChannelPull

    @property
    def ChannelUnPull(self):
        return self._ChannelUnPull

    @ChannelUnPull.setter
    def ChannelUnPull(self, ChannelUnPull):
        self._ChannelUnPull = ChannelUnPull


    def _deserialize(self, params):
        self._DeviceTotal = params.get("DeviceTotal")
        self._DeviceOnline = params.get("DeviceOnline")
        self._DeviceOffline = params.get("DeviceOffline")
        self._ChannelTotal = params.get("ChannelTotal")
        self._ChannelOnline = params.get("ChannelOnline")
        self._ChannelOffline = params.get("ChannelOffline")
        self._UpFlow = params.get("UpFlow")
        self._ChannelPull = params.get("ChannelPull")
        self._ChannelUnPull = params.get("ChannelUnPull")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayMonitorRequest(AbstractModel):
    """DescribeGatewayMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关索引ID（从获取网关列表接口ListGateways中获取）
        :type GatewayId: str
        """
        self._GatewayId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayMonitorResponse(AbstractModel):
    """DescribeGatewayMonitor返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeGatewayMonitor`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeGatewayMonitor()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeGatewayProtocolData(AbstractModel):
    """查询网关所支持的接入协议

    """

    def __init__(self):
        r"""
        :param _TypeCode: 接入协议的字典码
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeCode: str
        :param _Value: 接入协议类型值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: int
        :param _Label: 接入协议的类型描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        """
        self._TypeCode = None
        self._Value = None
        self._Label = None

    @property
    def TypeCode(self):
        return self._TypeCode

    @TypeCode.setter
    def TypeCode(self, TypeCode):
        self._TypeCode = TypeCode

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label


    def _deserialize(self, params):
        self._TypeCode = params.get("TypeCode")
        self._Value = params.get("Value")
        self._Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayProtocolRequest(AbstractModel):
    """DescribeGatewayProtocol请求参数结构体

    """


class DescribeGatewayProtocolResponse(AbstractModel):
    """DescribeGatewayProtocol返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: list of DescribeGatewayProtocolData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeGatewayProtocolData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGatewayRequest(AbstractModel):
    """DescribeGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关索引ID（从获取网关列表接口ListGateways中获取）
        :type GatewayId: str
        """
        self._GatewayId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayResponse(AbstractModel):
    """DescribeGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeGatewayData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeGatewayData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeGatewayVersion(AbstractModel):
    """查询网关服务版本信息返回数据

    """

    def __init__(self):
        r"""
        :param _Name: 服务名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Version: 服务版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _LatestVersion: 服务最新版本
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestVersion: str
        :param _IsUpdate: 是否需要更新
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUpdate: bool
        :param _UpgradeInfo: 升级信息
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradeInfo: list of str
        """
        self._Name = None
        self._Version = None
        self._LatestVersion = None
        self._IsUpdate = None
        self._UpgradeInfo = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def LatestVersion(self):
        return self._LatestVersion

    @LatestVersion.setter
    def LatestVersion(self, LatestVersion):
        self._LatestVersion = LatestVersion

    @property
    def IsUpdate(self):
        return self._IsUpdate

    @IsUpdate.setter
    def IsUpdate(self, IsUpdate):
        self._IsUpdate = IsUpdate

    @property
    def UpgradeInfo(self):
        return self._UpgradeInfo

    @UpgradeInfo.setter
    def UpgradeInfo(self, UpgradeInfo):
        self._UpgradeInfo = UpgradeInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Version = params.get("Version")
        self._LatestVersion = params.get("LatestVersion")
        self._IsUpdate = params.get("IsUpdate")
        self._UpgradeInfo = params.get("UpgradeInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayVersionData(AbstractModel):
    """查询网关服务版本信息返回数据

    """

    def __init__(self):
        r"""
        :param _Services: 网关服务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Services: list of DescribeGatewayVersion
        """
        self._Services = None

    @property
    def Services(self):
        return self._Services

    @Services.setter
    def Services(self, Services):
        self._Services = Services


    def _deserialize(self, params):
        if params.get("Services") is not None:
            self._Services = []
            for item in params.get("Services"):
                obj = DescribeGatewayVersion()
                obj._deserialize(item)
                self._Services.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayVersionRequest(AbstractModel):
    """DescribeGatewayVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关索引ID（从获取网关列表接口ListGateways中获取）
        :type GatewayId: str
        """
        self._GatewayId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayVersionResponse(AbstractModel):
    """DescribeGatewayVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeGatewayVersionData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeGatewayVersionData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeOrganizationData(AbstractModel):
    """查询组织数据返回结果

    """

    def __init__(self):
        r"""
        :param _OrganizationId: 组织 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationId: str
        :param _Name: 组织名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _ParentId: 组织父节点 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentId: str
        :param _Level: 组织层级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param _AppId: 用户id
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _ParentIds: 组织结构
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentIds: str
        :param _Total: 设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Online: 设备在线数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Online: int
        """
        self._OrganizationId = None
        self._Name = None
        self._ParentId = None
        self._Level = None
        self._AppId = None
        self._ParentIds = None
        self._Total = None
        self._Online = None

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParentId(self):
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ParentIds(self):
        return self._ParentIds

    @ParentIds.setter
    def ParentIds(self, ParentIds):
        self._ParentIds = ParentIds

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Online(self):
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        self._Name = params.get("Name")
        self._ParentId = params.get("ParentId")
        self._Level = params.get("Level")
        self._AppId = params.get("AppId")
        self._ParentIds = params.get("ParentIds")
        self._Total = params.get("Total")
        self._Online = params.get("Online")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationRequest(AbstractModel):
    """DescribeOrganization请求参数结构体

    """


class DescribeOrganizationResponse(AbstractModel):
    """DescribeOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: list of DescribeOrganizationData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeOrganizationData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordBackupPlanData(AbstractModel):
    """查询录像上云计划返回数据

    """

    def __init__(self):
        r"""
        :param _PlanId: 录像上云计划ID
        :type PlanId: str
        :param _PlanName: 录像上云计划名称
        :type PlanName: str
        :param _TemplateId: 录像上云模板ID
        :type TemplateId: str
        :param _Describe: 录像上云计划描述
        :type Describe: str
        :param _LifeCycle: 云文件生命周期
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Status: 录像上云计划状态，1:正常使用中，0:删除中，无法使用
        :type Status: int
        :param _ChannelCount: 通道数量
        :type ChannelCount: int
        :param _CreateAt: 创建时间
        :type CreateAt: str
        :param _UpdateAt: 修改时间
        :type UpdateAt: str
        """
        self._PlanId = None
        self._PlanName = None
        self._TemplateId = None
        self._Describe = None
        self._LifeCycle = None
        self._Status = None
        self._ChannelCount = None
        self._CreateAt = None
        self._UpdateAt = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanName(self):
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def LifeCycle(self):
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ChannelCount(self):
        return self._ChannelCount

    @ChannelCount.setter
    def ChannelCount(self, ChannelCount):
        self._ChannelCount = ChannelCount

    @property
    def CreateAt(self):
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        self._Describe = params.get("Describe")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        self._Status = params.get("Status")
        self._ChannelCount = params.get("ChannelCount")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordBackupPlanRequest(AbstractModel):
    """DescribeRecordBackupPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 录像上云计划ID（从查询录像上云计划列表接口ListRecordBackupPlans中获取）
        :type PlanId: str
        """
        self._PlanId = None

    @property
    def PlanId(self):
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
        


class DescribeRecordBackupPlanResponse(AbstractModel):
    """DescribeRecordBackupPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeRecordBackupPlanData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeRecordBackupPlanData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRecordBackupTemplateData(AbstractModel):
    """查询录像上云模板返回数据

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param _TemplateName: 模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateName: str
        :param _TimeSections: 上云时间段（按周进行设置，支持一天设置多个时间段，每个时间段不小于10分钟）
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSections: list of RecordTemplateTimeSections
        :param _DevTimeSections: 录像时间段（按周进行设置，支持一天设置多个时间段，每个时间段不小于10分钟）
注意：此字段可能返回 null，表示取不到有效值。
        :type DevTimeSections: list of RecordTemplateTimeSections
        :param _Scale: 上云倍速（支持1，2，4倍速）
注意：此字段可能返回 null，表示取不到有效值。
        :type Scale: int
        :param _CreateAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateAt: str
        :param _UpdateAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateAt: str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TimeSections = None
        self._DevTimeSections = None
        self._Scale = None
        self._CreateAt = None
        self._UpdateAt = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections

    @property
    def DevTimeSections(self):
        return self._DevTimeSections

    @DevTimeSections.setter
    def DevTimeSections(self, DevTimeSections):
        self._DevTimeSections = DevTimeSections

    @property
    def Scale(self):
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale

    @property
    def CreateAt(self):
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        if params.get("DevTimeSections") is not None:
            self._DevTimeSections = []
            for item in params.get("DevTimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._DevTimeSections.append(obj)
        self._Scale = params.get("Scale")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordBackupTemplateRequest(AbstractModel):
    """DescribeRecordBackupTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID（从查询录像上云模板列表接口ListRecordBackupTemplates中获取）
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
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
        


class DescribeRecordBackupTemplateResponse(AbstractModel):
    """DescribeRecordBackupTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeRecordBackupTemplateData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeRecordBackupTemplateData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRecordFileData(AbstractModel):
    """用于查询设备云端录像时间轴信息返回数据

    """

    def __init__(self):
        r"""
        :param _Tips: 提示类型，0:时间段内无归档录像，1:时间段内有归档录像
        :type Tips: int
        :param _List: 存在为数组格式，不存在字段内容为空
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of RecordTimeLine
        """
        self._Tips = None
        self._List = None

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._Tips = params.get("Tips")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = RecordTimeLine()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordFileRequest(AbstractModel):
    """DescribeRecordFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 通道所属设备ID
        :type DeviceId: str
        :param _ChannelId: 通道ID
        :type ChannelId: str
        :param _StartTime: 检索开始时间，UTC秒数，例如：1662114146，开始和结束时间段最长为一天，且不能跨天
        :type StartTime: int
        :param _EndTime: 检索结束时间，UTC秒数，例如：1662114246，开始和结束时间段最长为一天，且不能跨天
        :type EndTime: int
        """
        self._DeviceId = None
        self._ChannelId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ChannelId = params.get("ChannelId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordFileResponse(AbstractModel):
    """DescribeRecordFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeRecordFileData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeRecordFileData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRecordPlanRequest(AbstractModel):
    """DescribeRecordPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 实时上云计划ID
        :type PlanId: str
        """
        self._PlanId = None

    @property
    def PlanId(self):
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
        


class DescribeRecordPlanResponse(AbstractModel):
    """DescribeRecordPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.RecordPlanBaseInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = RecordPlanBaseInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRecordPlaybackUrlRequest(AbstractModel):
    """DescribeRecordPlaybackUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelId: 设备通道ID
        :type ChannelId: str
        :param _StartTime: 回放开始时间，UTC秒数，例如：1662114146，开始和结束时间段最长为一天，且不能跨天
        :type StartTime: int
        :param _EndTime: 回放结束时间，UTC秒数，例如：1662114246，开始和结束时间段最长为一天，且不能跨天
        :type EndTime: int
        :param _IsInternal: 是否获取内网地址
        :type IsInternal: bool
        """
        self._ChannelId = None
        self._StartTime = None
        self._EndTime = None
        self._IsInternal = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IsInternal(self):
        return self._IsInternal

    @IsInternal.setter
    def IsInternal(self, IsInternal):
        self._IsInternal = IsInternal


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IsInternal = params.get("IsInternal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordPlaybackUrlResponse(AbstractModel):
    """DescribeRecordPlaybackUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.RecordPlaybackUrl`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = RecordPlaybackUrl()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRecordRetrieveTaskData(AbstractModel):
    """查询云录像取回任务详情返回数据

    """

    def __init__(self):
        r"""
        :param _TaskId: 取回任务ID
        :type TaskId: str
        :param _TaskName: 取回任务名称
        :type TaskName: str
        :param _StartTime: 取回录像的开始时间
        :type StartTime: int
        :param _EndTime: 取回录像的结束时间
        :type EndTime: int
        :param _Mode: 取回模式，1:极速模式，其他暂不支持
        :type Mode: int
        :param _Expiration: 副本有效期
        :type Expiration: int
        :param _Status: 任务状态，0:已取回，1:取回中，2:待取回
        :type Status: int
        :param _Capacity: 取回容量，单位MB
        :type Capacity: float
        :param _Channels: 任务的设备通道id
        :type Channels: list of RecordRetrieveTaskChannelInfo
        :param _Describe: 任务描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
        :param _ChannelCount: 任务通道数量
        :type ChannelCount: int
        """
        self._TaskId = None
        self._TaskName = None
        self._StartTime = None
        self._EndTime = None
        self._Mode = None
        self._Expiration = None
        self._Status = None
        self._Capacity = None
        self._Channels = None
        self._Describe = None
        self._ChannelCount = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Expiration(self):
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Capacity(self):
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity

    @property
    def Channels(self):
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def ChannelCount(self):
        return self._ChannelCount

    @ChannelCount.setter
    def ChannelCount(self, ChannelCount):
        self._ChannelCount = ChannelCount


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Mode = params.get("Mode")
        self._Expiration = params.get("Expiration")
        self._Status = params.get("Status")
        self._Capacity = params.get("Capacity")
        if params.get("Channels") is not None:
            self._Channels = []
            for item in params.get("Channels"):
                obj = RecordRetrieveTaskChannelInfo()
                obj._deserialize(item)
                self._Channels.append(obj)
        self._Describe = params.get("Describe")
        self._ChannelCount = params.get("ChannelCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordRetrieveTaskRequest(AbstractModel):
    """DescribeRecordRetrieveTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 云录像取回任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordRetrieveTaskResponse(AbstractModel):
    """DescribeRecordRetrieveTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeRecordRetrieveTaskData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeRecordRetrieveTaskData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRecordSliceRequest(AbstractModel):
    """DescribeRecordSlice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelId: 通道ID
        :type ChannelId: str
        :param _StartTime: 检索开始时间，UTC秒数，例如：1662114146，开始和结束时间段最长为一天，且不能跨天
        :type StartTime: int
        :param _EndTime: 检索结束时间，UTC秒数，例如：1662114246，开始和结束时间段最长为一天，且不能跨天
        :type EndTime: int
        """
        self._ChannelId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordSliceResponse(AbstractModel):
    """DescribeRecordSlice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 云录像切片信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of RecordSliceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RecordSliceInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordTemplateRequest(AbstractModel):
    """DescribeRecordTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
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
        


class DescribeRecordTemplateResponse(AbstractModel):
    """DescribeRecordTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.RecordTemplateInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = RecordTemplateInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeStreamAuthData(AbstractModel):
    """查询推拉流鉴权返回数据结构

    """

    def __init__(self):
        r"""
        :param _Id: 鉴权配置ID（uuid）
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _PullState: 是否开播放鉴权（1:开启,0:关闭）
注意：此字段可能返回 null，表示取不到有效值。
        :type PullState: int
        :param _PullSecret: 播放密钥（仅支持字母数字，长度0-10位）
注意：此字段可能返回 null，表示取不到有效值。
        :type PullSecret: str
        :param _PullExpired: 播放过期时间（单位：分钟）
注意：此字段可能返回 null，表示取不到有效值。
        :type PullExpired: int
        :param _PushState: 是否开启推流鉴权（1:开启,0:关闭）
注意：此字段可能返回 null，表示取不到有效值。
        :type PushState: int
        :param _PushSecret: 推流密钥（仅支持字母数字，长度0-10位）
注意：此字段可能返回 null，表示取不到有效值。
        :type PushSecret: str
        :param _PushExpired: 推流过期时间（单位：分钟）
注意：此字段可能返回 null，表示取不到有效值。
        :type PushExpired: int
        :param _AppId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        """
        self._Id = None
        self._PullState = None
        self._PullSecret = None
        self._PullExpired = None
        self._PushState = None
        self._PushSecret = None
        self._PushExpired = None
        self._AppId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PullState(self):
        return self._PullState

    @PullState.setter
    def PullState(self, PullState):
        self._PullState = PullState

    @property
    def PullSecret(self):
        return self._PullSecret

    @PullSecret.setter
    def PullSecret(self, PullSecret):
        self._PullSecret = PullSecret

    @property
    def PullExpired(self):
        return self._PullExpired

    @PullExpired.setter
    def PullExpired(self, PullExpired):
        self._PullExpired = PullExpired

    @property
    def PushState(self):
        return self._PushState

    @PushState.setter
    def PushState(self, PushState):
        self._PushState = PushState

    @property
    def PushSecret(self):
        return self._PushSecret

    @PushSecret.setter
    def PushSecret(self, PushSecret):
        self._PushSecret = PushSecret

    @property
    def PushExpired(self):
        return self._PushExpired

    @PushExpired.setter
    def PushExpired(self, PushExpired):
        self._PushExpired = PushExpired

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PullState = params.get("PullState")
        self._PullSecret = params.get("PullSecret")
        self._PullExpired = params.get("PullExpired")
        self._PushState = params.get("PushState")
        self._PushSecret = params.get("PushSecret")
        self._PushExpired = params.get("PushExpired")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamAuthRequest(AbstractModel):
    """DescribeStreamAuth请求参数结构体

    """


class DescribeStreamAuthResponse(AbstractModel):
    """DescribeStreamAuth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeStreamAuthData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeStreamAuthData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTaskRequest(AbstractModel):
    """DescribeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 简单任务或复杂任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskResponse(AbstractModel):
    """DescribeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 任务详情
        :type Data: :class:`tencentcloud.iss.v20230517.models.TaskData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = TaskData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeUserDeviceRequest(AbstractModel):
    """DescribeUserDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID（从获取设备列表接口ListDevices中获取）
        :type DeviceId: str
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
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
        


class DescribeUserDeviceResponse(AbstractModel):
    """DescribeUserDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeDeviceData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeDeviceData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeVideoBitRateList(AbstractModel):
    """查询视频通道码率的返回结果列表

    """

    def __init__(self):
        r"""
        :param _BitRates: 通道码率列表
注意：此字段可能返回 null，表示取不到有效值。
        :type BitRates: list of BitRateInfo
        """
        self._BitRates = None

    @property
    def BitRates(self):
        return self._BitRates

    @BitRates.setter
    def BitRates(self, BitRates):
        self._BitRates = BitRates


    def _deserialize(self, params):
        if params.get("BitRates") is not None:
            self._BitRates = []
            for item in params.get("BitRates"):
                obj = BitRateInfo()
                obj._deserialize(item)
                self._BitRates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoBitRateRequest(AbstractModel):
    """DescribeVideoBitRate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelIds: 通道ID列表
        :type ChannelIds: list of str
        """
        self._ChannelIds = None

    @property
    def ChannelIds(self):
        return self._ChannelIds

    @ChannelIds.setter
    def ChannelIds(self, ChannelIds):
        self._ChannelIds = ChannelIds


    def _deserialize(self, params):
        self._ChannelIds = params.get("ChannelIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoBitRateResponse(AbstractModel):
    """DescribeVideoBitRate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 无
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeVideoBitRateList`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeVideoBitRateList()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeVideoDownloadUrlData(AbstractModel):
    """获取云录像下载URL返回的数据

    """

    def __init__(self):
        r"""
        :param _Url: 录像文件下载 URL
注意：
URL 有效期是10分钟，过期后将拒绝访问，若需再用请重新获取 
录像文件下载采用分块传输编码，响应头Transfer-Encoding:chunked 
下载文件命名格式为{ChannelId}-{BeginTime}-{EndTime}.{FileType} 
        :type Url: str
        :param _ActualBeginTime: 实际下载录像的开始时间
注意：当请求中指定IsRespActualTime参数为true时，才有该字段
        :type ActualBeginTime: str
        :param _ActualEndTime: 实际下载录像的结束时间
注意：当请求中指定IsRespActualTime参数为true时，才有该字段
        :type ActualEndTime: str
        """
        self._Url = None
        self._ActualBeginTime = None
        self._ActualEndTime = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def ActualBeginTime(self):
        return self._ActualBeginTime

    @ActualBeginTime.setter
    def ActualBeginTime(self, ActualBeginTime):
        self._ActualBeginTime = ActualBeginTime

    @property
    def ActualEndTime(self):
        return self._ActualEndTime

    @ActualEndTime.setter
    def ActualEndTime(self, ActualEndTime):
        self._ActualEndTime = ActualEndTime


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._ActualBeginTime = params.get("ActualBeginTime")
        self._ActualEndTime = params.get("ActualEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoDownloadUrlRequest(AbstractModel):
    """DescribeVideoDownloadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelId: 通道 ID
        :type ChannelId: str
        :param _BeginTime: 下载的开始时间，UTC 秒数，开始和结束时间段最长为60分钟，且不能跨天。
注意：实际下载的文件时长可能会大于该时段时长，通过指定IsRespActualTime参数可以获取实际下载的开始时间和结束时间。 原因是下载是TS切片对齐的，其目的也是为了保证用户下载数据的完整性，完全包含其指定的时间段。
        :type BeginTime: str
        :param _EndTime: 下载的结束时间，UTC 秒数，开始和结束时间段最长为60分钟，且不能跨天。
注意：实际下载的文件时长可能会大于该时段时长，通过指定IsRespActualTime参数可以获取实际下载的开始时间和结束时间。 原因是下载是TS切片对齐的，其目的也是为了保证用户下载数据的完整性，完全包含其指定的时间段。
        :type EndTime: str
        :param _FileType: 文件格式，"mp4"：mp4格式，"ts"：ts文件格式
        :type FileType: str
        :param _IsRespActualTime: 响应data中是否携带实际下载录像的开始时间与结束时间
        :type IsRespActualTime: bool
        :param _IsInternal: 是否返回内网下载URL，默认是false，返回公网下载URL，true则返回内网下载URL
        :type IsInternal: bool
        """
        self._ChannelId = None
        self._BeginTime = None
        self._EndTime = None
        self._FileType = None
        self._IsRespActualTime = None
        self._IsInternal = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def IsRespActualTime(self):
        return self._IsRespActualTime

    @IsRespActualTime.setter
    def IsRespActualTime(self, IsRespActualTime):
        self._IsRespActualTime = IsRespActualTime

    @property
    def IsInternal(self):
        return self._IsInternal

    @IsInternal.setter
    def IsInternal(self, IsInternal):
        self._IsInternal = IsInternal


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._FileType = params.get("FileType")
        self._IsRespActualTime = params.get("IsRespActualTime")
        self._IsInternal = params.get("IsInternal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoDownloadUrlResponse(AbstractModel):
    """DescribeVideoDownloadUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回的数据结构
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeVideoDownloadUrlData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeVideoDownloadUrlData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class FaceMaskAIResultInfo(AbstractModel):
    """口罩识别结果详情

    """

    def __init__(self):
        r"""
        :param _Time: 时间字符串
        :type Time: str
        :param _Url: 截图 URL
        :type Url: str
        :param _FaceMaskInfo: 口罩信息
        :type FaceMaskInfo: list of BaseAIResultInfo
        """
        self._Time = None
        self._Url = None
        self._FaceMaskInfo = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def FaceMaskInfo(self):
        return self._FaceMaskInfo

    @FaceMaskInfo.setter
    def FaceMaskInfo(self, FaceMaskInfo):
        self._FaceMaskInfo = FaceMaskInfo


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Url = params.get("Url")
        if params.get("FaceMaskInfo") is not None:
            self._FaceMaskInfo = []
            for item in params.get("FaceMaskInfo"):
                obj = BaseAIResultInfo()
                obj._deserialize(item)
                self._FaceMaskInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayDevice(AbstractModel):
    """网关设备数据

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param _ProtocolType: 网关接入协议类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtocolType: int
        :param _ProtocolTypeName: 网关接入协议名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtocolTypeName: str
        :param _Name: 设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Type: 设备类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _Ip: 设备内网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Port: 设备端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _ChannelNum: 设备下通道数
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelNum: int
        :param _Status: 设备状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self._DeviceId = None
        self._ProtocolType = None
        self._ProtocolTypeName = None
        self._Name = None
        self._Type = None
        self._Ip = None
        self._Port = None
        self._ChannelNum = None
        self._Status = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ProtocolType(self):
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def ProtocolTypeName(self):
        return self._ProtocolTypeName

    @ProtocolTypeName.setter
    def ProtocolTypeName(self, ProtocolTypeName):
        self._ProtocolTypeName = ProtocolTypeName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ChannelNum(self):
        return self._ChannelNum

    @ChannelNum.setter
    def ChannelNum(self, ChannelNum):
        self._ChannelNum = ChannelNum

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ProtocolType = params.get("ProtocolType")
        self._ProtocolTypeName = params.get("ProtocolTypeName")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._ChannelNum = params.get("ChannelNum")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayVersion(AbstractModel):
    """网关详情版本信息

    """

    def __init__(self):
        r"""
        :param _Name: 服务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Version: 服务版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        """
        self._Name = None
        self._Version = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewaysData(AbstractModel):
    """查询网关列表返回结果

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关索引ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayId: str
        :param _GwId: 网关编码
注意：此字段可能返回 null，表示取不到有效值。
        :type GwId: str
        :param _Name: 网关名称，仅支持中文、英文、数字、_、-，长度不超过32个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: 网关描述，仅支持中文、英文、数字、_、-，长度不超过128个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _ClusterId: 网关所属服务节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ClusterName: 网关所属服务节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param _Region: 网关所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Status: 网关状态，0：离线，1:在线
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreatedAt: 网关激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _DeviceNum: 所属网关设备数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceNum: int
        """
        self._GatewayId = None
        self._GwId = None
        self._Name = None
        self._Description = None
        self._ClusterId = None
        self._ClusterName = None
        self._Region = None
        self._Status = None
        self._CreatedAt = None
        self._DeviceNum = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GwId(self):
        return self._GwId

    @GwId.setter
    def GwId(self, GwId):
        self._GwId = GwId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def DeviceNum(self):
        return self._DeviceNum

    @DeviceNum.setter
    def DeviceNum(self, DeviceNum):
        self._DeviceNum = DeviceNum


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GwId = params.get("GwId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        self._CreatedAt = params.get("CreatedAt")
        self._DeviceNum = params.get("DeviceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifeCycleData(AbstractModel):
    """生命周期，云文件生命周期设置，管理文件冷、热存储的时间

    """

    def __init__(self):
        r"""
        :param _Transition: 云文件热存储时长，单位天，最小1天，最大3650天
        :type Transition: int
        :param _Expiration: 云文件冷存储时长， 单位天，0表示不设置，设置时最小60天，Expiration字段加Transition字段不超过3650天
        :type Expiration: int
        """
        self._Transition = None
        self._Expiration = None

    @property
    def Transition(self):
        return self._Transition

    @Transition.setter
    def Transition(self, Transition):
        self._Transition = Transition

    @property
    def Expiration(self):
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration


    def _deserialize(self, params):
        self._Transition = params.get("Transition")
        self._Expiration = params.get("Expiration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAITaskData(AbstractModel):
    """获取AI任务列表的数据

    """

    def __init__(self):
        r"""
        :param _List: AI任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of AITaskInfo
        """
        self._List = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AITaskInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAITasksRequest(AbstractModel):
    """ListAITasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IsContainChannelList: 是否包含通道列表。"true"代表包含通道列表，"false"代表不包含通道列表，默认为 false
        :type IsContainChannelList: bool
        :param _IsContainTemplate: 是否包含AI配置。"true"代表包含任务配置，"false"代表不包含任务配置，默认为 false。
        :type IsContainTemplate: bool
        :param _PageNumber: 页码。默认为1
        :type PageNumber: int
        :param _PageSize: 每页数量。可选值1～200，默认为20
        :type PageSize: int
        """
        self._IsContainChannelList = None
        self._IsContainTemplate = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def IsContainChannelList(self):
        return self._IsContainChannelList

    @IsContainChannelList.setter
    def IsContainChannelList(self, IsContainChannelList):
        self._IsContainChannelList = IsContainChannelList

    @property
    def IsContainTemplate(self):
        return self._IsContainTemplate

    @IsContainTemplate.setter
    def IsContainTemplate(self, IsContainTemplate):
        self._IsContainTemplate = IsContainTemplate

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._IsContainChannelList = params.get("IsContainChannelList")
        self._IsContainTemplate = params.get("IsContainTemplate")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAITasksResponse(AbstractModel):
    """ListAITasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: AI 任务数量
        :type TotalCount: int
        :param _Data: AI任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListAITaskData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = ListAITaskData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListDeviceInfo(AbstractModel):
    """获取设备列表的响应

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备 ID
        :type DeviceId: str
        :param _Code: 设备编码
        :type Code: str
        :param _Status: 设备状态。0:未注册，1:在线，2:离线，3:禁用
        :type Status: int
        :param _TransportProtocol: 设备流传输协议。1:UDP,2:TCP
        :type TransportProtocol: int
        :param _Name: 设备名称
        :type Name: str
        :param _Type: 设备类型。1:IPC,2:NVR
        :type Type: int
        :param _Password: 设备密码
        :type Password: str
        :param _Description: 描述
        :type Description: str
        :param _ClusterId: 设备接入服务节点 ID
        :type ClusterId: str
        :param _ClusterName: 服务节点名称
        :type ClusterName: str
        :param _AccessProtocol: 接入协议。1:RTMP,2:GB,3:GW
        :type AccessProtocol: int
        :param _OrganizationId: 设备所属组织 ID
        :type OrganizationId: str
        :param _ChannelNum: 通道数量
        :type ChannelNum: int
        """
        self._DeviceId = None
        self._Code = None
        self._Status = None
        self._TransportProtocol = None
        self._Name = None
        self._Type = None
        self._Password = None
        self._Description = None
        self._ClusterId = None
        self._ClusterName = None
        self._AccessProtocol = None
        self._OrganizationId = None
        self._ChannelNum = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TransportProtocol(self):
        return self._TransportProtocol

    @TransportProtocol.setter
    def TransportProtocol(self, TransportProtocol):
        self._TransportProtocol = TransportProtocol

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def AccessProtocol(self):
        return self._AccessProtocol

    @AccessProtocol.setter
    def AccessProtocol(self, AccessProtocol):
        self._AccessProtocol = AccessProtocol

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def ChannelNum(self):
        return self._ChannelNum

    @ChannelNum.setter
    def ChannelNum(self, ChannelNum):
        self._ChannelNum = ChannelNum


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Code = params.get("Code")
        self._Status = params.get("Status")
        self._TransportProtocol = params.get("TransportProtocol")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._AccessProtocol = params.get("AccessProtocol")
        self._OrganizationId = params.get("OrganizationId")
        self._ChannelNum = params.get("ChannelNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDevicesRequest(AbstractModel):
    """ListDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrganizationId: 组织ID
        :type OrganizationId: str
        :param _IsContainSubLevel: 是否获取当前层级及子层级的设备列表，默认false
        :type IsContainSubLevel: bool
        :param _IsContainUser: 是否包含当前用户已关联的设备，默认false
        :type IsContainUser: bool
        :param _AccessProtocol: 设备接入协议。1:RTMP，2:GB，3:GW，4:IVCP(私有协议)
        :type AccessProtocol: int
        :param _Type: 设备类型。1:IPC，2:NVR
        :type Type: int
        :param _Status: 设备状态。0:未注册，1:在线，2:离线，3:禁用	
        :type Status: int
        :param _ClusterId: 服务节点ID
        :type ClusterId: str
        :param _Keyword: 模糊搜索设备的关键字
        :type Keyword: str
        :param _CurrentUin: 当前用户Uin
        :type CurrentUin: int
        :param _PageNumber: 页码，默认为1。
        :type PageNumber: int
        :param _PageSize: 每页数量，默认为20。
        :type PageSize: int
        """
        self._OrganizationId = None
        self._IsContainSubLevel = None
        self._IsContainUser = None
        self._AccessProtocol = None
        self._Type = None
        self._Status = None
        self._ClusterId = None
        self._Keyword = None
        self._CurrentUin = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def IsContainSubLevel(self):
        return self._IsContainSubLevel

    @IsContainSubLevel.setter
    def IsContainSubLevel(self, IsContainSubLevel):
        self._IsContainSubLevel = IsContainSubLevel

    @property
    def IsContainUser(self):
        return self._IsContainUser

    @IsContainUser.setter
    def IsContainUser(self, IsContainUser):
        self._IsContainUser = IsContainUser

    @property
    def AccessProtocol(self):
        return self._AccessProtocol

    @AccessProtocol.setter
    def AccessProtocol(self, AccessProtocol):
        self._AccessProtocol = AccessProtocol

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def CurrentUin(self):
        return self._CurrentUin

    @CurrentUin.setter
    def CurrentUin(self, CurrentUin):
        self._CurrentUin = CurrentUin

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        self._IsContainSubLevel = params.get("IsContainSubLevel")
        self._IsContainUser = params.get("IsContainUser")
        self._AccessProtocol = params.get("AccessProtocol")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._ClusterId = params.get("ClusterId")
        self._Keyword = params.get("Keyword")
        self._CurrentUin = params.get("CurrentUin")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDevicesResponse(AbstractModel):
    """ListDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备列表详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ListDeviceInfo
        :param _TotalCount: 设备总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ListDeviceInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListGatewayDevicesData(AbstractModel):
    """查询网关设备列表返回数据

    """

    def __init__(self):
        r"""
        :param _List: 网关下设备列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of GatewayDevice
        :param _TotalCount: 网关下设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self._List = None
        self._TotalCount = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = GatewayDevice()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGatewayDevicesRequest(AbstractModel):
    """ListGatewayDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关索引ID（从获取网关列表接口ListGateways中获取）
        :type GatewayId: str
        :param _PageNumber: 分页页数
        :type PageNumber: int
        :param _PageSize: 分页大小
        :type PageSize: int
        """
        self._GatewayId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGatewayDevicesResponse(AbstractModel):
    """ListGatewayDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListGatewayDevicesData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListGatewayDevicesData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListGatewaysData(AbstractModel):
    """查询网关列表返回结果

    """

    def __init__(self):
        r"""
        :param _List: 网关列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of GatewaysData
        :param _TotalCount: 网关数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self._List = None
        self._TotalCount = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = GatewaysData()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGatewaysRequest(AbstractModel):
    """ListGateways请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 页码，默认为1
        :type PageNumber: int
        :param _PageSize: 每页数量，默认为20
        :type PageSize: int
        :param _Name: 网关名称
        :type Name: str
        :param _ClusterId: 服务节点ID
        :type ClusterId: str
        :param _Status: 网关状态（0：离线，1 ：在线）
        :type Status: int
        """
        self._PageNumber = None
        self._PageSize = None
        self._Name = None
        self._ClusterId = None
        self._Status = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Name = params.get("Name")
        self._ClusterId = params.get("ClusterId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGatewaysResponse(AbstractModel):
    """ListGateways返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListGatewaysData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListGatewaysData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListOrganizationChannelNumbersData(AbstractModel):
    """组织目录下的未添加到实时上云计划中的通道数量返回数据

    """

    def __init__(self):
        r"""
        :param _TotalCount: 组织下通道总数
        :type TotalCount: int
        :param _NotInPlanCount: 组织下未添加到计划的通道总数
        :type NotInPlanCount: int
        """
        self._TotalCount = None
        self._NotInPlanCount = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NotInPlanCount(self):
        return self._NotInPlanCount

    @NotInPlanCount.setter
    def NotInPlanCount(self, NotInPlanCount):
        self._NotInPlanCount = NotInPlanCount


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._NotInPlanCount = params.get("NotInPlanCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationChannelNumbersRequest(AbstractModel):
    """ListOrganizationChannelNumbers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrganizationId: 组织ID，json数组格式，最多一次支持10个组织
        :type OrganizationId: list of str
        """
        self._OrganizationId = None

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationChannelNumbersResponse(AbstractModel):
    """ListOrganizationChannelNumbers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListOrganizationChannelNumbersData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListOrganizationChannelNumbersData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListOrganizationChannelsData(AbstractModel):
    """查询组织目录下的通道列表返回数据

    """

    def __init__(self):
        r"""
        :param _PageNumber: 第几页
        :type PageNumber: int
        :param _PageSize: 当前页的设备数量
        :type PageSize: int
        :param _TotalCount: 本次查询的设备通道总数
        :type TotalCount: int
        :param _List: 设备通道信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of OrganizationChannelInfo
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._List = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = OrganizationChannelInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationChannelsRequest(AbstractModel):
    """ListOrganizationChannels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrganizationId: 组织ID
        :type OrganizationId: str
        :param _PageSize: 每页最大数量
        :type PageSize: int
        :param _PageNumber: 第几页 
        :type PageNumber: int
        :param _DeviceName: 查询条件，则按照设备名称查询
查询条件同时只有一个生效。长度不超过32字节
        :type DeviceName: str
        :param _ChannelName: 查询条件，则按照通道名称查询
查询条件同时只有一个生效。长度不超过32字节
        :type ChannelName: str
        """
        self._OrganizationId = None
        self._PageSize = None
        self._PageNumber = None
        self._DeviceName = None
        self._ChannelName = None

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._DeviceName = params.get("DeviceName")
        self._ChannelName = params.get("ChannelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationChannelsResponse(AbstractModel):
    """ListOrganizationChannels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListOrganizationChannelsData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListOrganizationChannelsData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListRecordBackupPlanData(AbstractModel):
    """查询录像上云计划列表返回数据

    """

    def __init__(self):
        r"""
        :param _PlanId: 录像上云计划ID
        :type PlanId: str
        :param _PlanName: 录像上云计划名称
        :type PlanName: str
        :param _TemplateId: 录像上云模板ID
        :type TemplateId: str
        :param _Describe: 录像上云计划描述
        :type Describe: str
        :param _LifeCycle: 云文件生命周期
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Status: 录像上云计划状态，1:正常使用中，0:删除中，无法使用
        :type Status: int
        :param _ChannelCount: 通道数量
        :type ChannelCount: int
        :param _CreateAt: 创建时间
        :type CreateAt: str
        :param _UpdateAt: 修改时间
        :type UpdateAt: str
        """
        self._PlanId = None
        self._PlanName = None
        self._TemplateId = None
        self._Describe = None
        self._LifeCycle = None
        self._Status = None
        self._ChannelCount = None
        self._CreateAt = None
        self._UpdateAt = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanName(self):
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def LifeCycle(self):
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ChannelCount(self):
        return self._ChannelCount

    @ChannelCount.setter
    def ChannelCount(self, ChannelCount):
        self._ChannelCount = ChannelCount

    @property
    def CreateAt(self):
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        self._Describe = params.get("Describe")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        self._Status = params.get("Status")
        self._ChannelCount = params.get("ChannelCount")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRecordBackupPlanDevicesData(AbstractModel):
    """查询录像上云计划关联通道的返回数据

    """

    def __init__(self):
        r"""
        :param _PageNumber: 第几页
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _PageSize: 当前页的设备数量
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _TotalCount: 本次查询的设备通道总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _List: 设备通道信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of RecordPlanChannelInfo
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._List = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = RecordPlanChannelInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRecordBackupPlanDevicesRequest(AbstractModel):
    """ListRecordBackupPlanDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 录像计划ID（从查询录像上云计划列表接口ListRecordBackupPlans中获取）
        :type PlanId: str
        :param _DeviceName: 按照设备名称查询（为空时，不参考该参数）
        :type DeviceName: str
        :param _ChannelName: 按照通道名称查询（为空时，不参考该参数）
        :type ChannelName: str
        :param _OrganizationName: 按照组织名称查询（为空时，不参考该参数）
        :type OrganizationName: str
        :param _PageSize: 每页最大数量
        :type PageSize: int
        :param _PageNumber: 分页页数
        :type PageNumber: int
        """
        self._PlanId = None
        self._DeviceName = None
        self._ChannelName = None
        self._OrganizationName = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelName = params.get("ChannelName")
        self._OrganizationName = params.get("OrganizationName")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRecordBackupPlanDevicesResponse(AbstractModel):
    """ListRecordBackupPlanDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListRecordBackupPlanDevicesData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListRecordBackupPlanDevicesData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListRecordBackupPlansRequest(AbstractModel):
    """ListRecordBackupPlans请求参数结构体

    """


class ListRecordBackupPlansResponse(AbstractModel):
    """ListRecordBackupPlans返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: list of ListRecordBackupPlanData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ListRecordBackupPlanData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListRecordBackupTemplatesData(AbstractModel):
    """查询录像上云模板列表返回数据

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param _TemplateName: 模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateName: str
        :param _TimeSections: 上云时间段（按周进行设置，支持一天设置多个时间段，每个时间段不小于10分钟）
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSections: list of RecordTemplateTimeSections
        :param _DevTimeSections: 录像时间段（按周进行设置，支持一天设置多个时间段，每个时间段不小于10分钟）
注意：此字段可能返回 null，表示取不到有效值。
        :type DevTimeSections: list of RecordTemplateTimeSections
        :param _Scale: 上云倍速（支持1，2，4倍速）
注意：此字段可能返回 null，表示取不到有效值。
        :type Scale: int
        :param _CreateAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateAt: str
        :param _UpdateAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateAt: str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TimeSections = None
        self._DevTimeSections = None
        self._Scale = None
        self._CreateAt = None
        self._UpdateAt = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections

    @property
    def DevTimeSections(self):
        return self._DevTimeSections

    @DevTimeSections.setter
    def DevTimeSections(self, DevTimeSections):
        self._DevTimeSections = DevTimeSections

    @property
    def Scale(self):
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale

    @property
    def CreateAt(self):
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        if params.get("DevTimeSections") is not None:
            self._DevTimeSections = []
            for item in params.get("DevTimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._DevTimeSections.append(obj)
        self._Scale = params.get("Scale")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRecordBackupTemplatesRequest(AbstractModel):
    """ListRecordBackupTemplates请求参数结构体

    """


class ListRecordBackupTemplatesResponse(AbstractModel):
    """ListRecordBackupTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: list of ListRecordBackupTemplatesData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ListRecordBackupTemplatesData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListRecordPlanChannelsData(AbstractModel):
    """用户下所有实时上云计划中的通道id列表返回数据

    """

    def __init__(self):
        r"""
        :param _List: 用户所有计划下通道id，存在通道是为数组格式，不存在时，字段数据为空 
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of str
        """
        self._List = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._List = params.get("List")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRecordPlanChannelsRequest(AbstractModel):
    """ListRecordPlanChannels请求参数结构体

    """


class ListRecordPlanChannelsResponse(AbstractModel):
    """ListRecordPlanChannels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListRecordPlanChannelsData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListRecordPlanChannelsData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListRecordPlanDevicesData(AbstractModel):
    """云计划下的设备通道列表返回数据

    """

    def __init__(self):
        r"""
        :param _PageNumber: 第几页
        :type PageNumber: int
        :param _PageSize: 当前页的设备数量
        :type PageSize: int
        :param _TotalCount: 本次查询的设备通道总数
        :type TotalCount: int
        :param _List: 设备通道信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of RecordPlanChannelInfo
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._List = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = RecordPlanChannelInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRecordPlanDevicesRequest(AbstractModel):
    """ListRecordPlanDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 上云计划ID
        :type PlanId: str
        :param _PageSize: 每页最大数量
        :type PageSize: int
        :param _PageNumber: 第几页
        :type PageNumber: int
        :param _DeviceName: 按照设备名称查询，为空时，不参考该参数
通道名称、设备名称、组织名称同时只有一个有效，如果同时多个字段有值，按照通道名称、设备名称、组织名称的优先级顺序查询，如果都为空，则全量查询。长度不超过32字节
        :type DeviceName: str
        :param _ChannelName: 按照通道名称查询，为空时，不参考该参数
通道名称、设备名称、组织名称同时只有一个有效，如果同时多个字段有值，按照通道名称、设备名称、组织名称的优先级顺序查询，如果都为空，则全量查询。长度不超过32字节
        :type ChannelName: str
        :param _OrganizationName: 按照组织名称查询|，为空时，不参考该参数
通道名称、设备名称、组织名称同时只有一个有效，如果同时多个字段有值，按照通道名称、设备名称、组织名称的优先级顺序查询，如果都为空，则全量查询。长度不超过32字节
        :type OrganizationName: str
        """
        self._PlanId = None
        self._PageSize = None
        self._PageNumber = None
        self._DeviceName = None
        self._ChannelName = None
        self._OrganizationName = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._DeviceName = params.get("DeviceName")
        self._ChannelName = params.get("ChannelName")
        self._OrganizationName = params.get("OrganizationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRecordPlanDevicesResponse(AbstractModel):
    """ListRecordPlanDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListRecordPlanDevicesData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListRecordPlanDevicesData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListRecordPlansRequest(AbstractModel):
    """ListRecordPlans请求参数结构体

    """


class ListRecordPlansResponse(AbstractModel):
    """ListRecordPlans返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果，存在计划时，为Json数组格式，不存在计划时，字段数据为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of RecordPlanBaseInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RecordPlanBaseInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListRecordRetrieveTasksRequest(AbstractModel):
    """ListRecordRetrieveTasks请求参数结构体

    """


class ListRecordRetrieveTasksResponse(AbstractModel):
    """ListRecordRetrieveTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of RecordRetrieveTaskDetailsInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RecordRetrieveTaskDetailsInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListRecordTemplatesRequest(AbstractModel):
    """ListRecordTemplates请求参数结构体

    """


class ListRecordTemplatesResponse(AbstractModel):
    """ListRecordTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果，存在模板时，为Json数组格式，不存在模板时，字段数据为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of RecordTemplateInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RecordTemplateInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListSubTasksData(AbstractModel):
    """列举子任务列表

    """

    def __init__(self):
        r"""
        :param _List: 子任务列表
        :type List: list of SubTaskData
        :param _TotalCount: 子任务数量
        :type TotalCount: int
        """
        self._List = None
        self._TotalCount = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = SubTaskData()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSubTasksRequest(AbstractModel):
    """ListSubTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 复杂任务ID
        :type TaskId: str
        :param _PageNumber: 页码，默认为1
        :type PageNumber: int
        :param _PageSize: 每页数量，默认为10
        :type PageSize: int
        :param _Status: 默认不对该字段进行筛选，否则根据任务状态进行筛选。状态码：1-NEW，2-RUNNING，3-COMPLETED，4-FAILED
        :type Status: int
        """
        self._TaskId = None
        self._PageNumber = None
        self._PageSize = None
        self._Status = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSubTasksResponse(AbstractModel):
    """ListSubTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListSubTasksData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListSubTasksData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListTasksData(AbstractModel):
    """查询任务列表

    """

    def __init__(self):
        r"""
        :param _List: 任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of TaskData
        :param _TotalCount: 任务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self._List = None
        self._TotalCount = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = TaskData()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTasksRequest(AbstractModel):
    """ListTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 页码，默认为1
        :type PageNumber: int
        :param _PageSize: 每页数量，默认为20
        :type PageSize: int
        :param _Operation: 默认不根据该字段进行筛选，否则根据设备操作类型进行筛选，目前值有：BatchDeleteUserDevice，BatchDisableDevice，BatchEnableDevice，
BatchUpgradeDevice，
BatchResetDevice,
BatchRebootDevice
        :type Operation: str
        :param _Status: 默认不根据该字段进行筛选，否则根据任务状态进行筛选。状态码：1-未执行，2-执行中，3-完成，4-取消
        :type Status: int
        :param _BeginTime: 开始时间
        :type BeginTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        """
        self._PageNumber = None
        self._PageSize = None
        self._Operation = None
        self._Status = None
        self._BeginTime = None
        self._EndTime = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Operation = params.get("Operation")
        self._Status = params.get("Status")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTasksResponse(AbstractModel):
    """ListTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListTasksData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ListTasksData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class Location(AbstractModel):
    """AI识别结果在画面中坐标

    """

    def __init__(self):
        r"""
        :param _X: 左上角 X 坐标轴
        :type X: int
        :param _Y: 左上角 Y 坐标轴
        :type Y: int
        :param _Width: 方框宽
        :type Width: int
        :param _Height: 方框高
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperTimeSlot(AbstractModel):
    """AI分析的时间段配置

    """

    def __init__(self):
        r"""
        :param _Start: 开始时间。格式为"hh:mm:ss"，且 Start 必须小于 End
        :type Start: str
        :param _End: 结束时间。格式为"hh:mm:ss"，且 Start 必须小于 End
        :type End: str
        """
        self._Start = None
        self._End = None

    @property
    def Start(self):
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._Start = params.get("Start")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrganizationChannelInfo(AbstractModel):
    """组织目录下的通道信息

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备通道所属的设备ID
        :type DeviceId: str
        :param _DeviceName: 设备通道所属的设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param _ChannelId: 设备通道ID
        :type ChannelId: str
        :param _ChannelName: 设备通道名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelName: str
        :param _InPlan: 该通道是否在上云计划中，如果是，则不能在添加到其他上云计划|true：在上云计划中，false：不在上云计划中
        :type InPlan: bool
        """
        self._DeviceId = None
        self._DeviceName = None
        self._ChannelId = None
        self._ChannelName = None
        self._InPlan = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def InPlan(self):
        return self._InPlan

    @InPlan.setter
    def InPlan(self, InPlan):
        self._InPlan = InPlan


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        self._InPlan = params.get("InPlan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PetAIResultInfo(AbstractModel):
    """宠物识别结果详情

    """

    def __init__(self):
        r"""
        :param _Time: 时间字符串
        :type Time: str
        :param _Url: 截图 URL
        :type Url: str
        :param _PetInfo: 宠物信息
        :type PetInfo: list of BaseAIResultInfo
        """
        self._Time = None
        self._Url = None
        self._PetInfo = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def PetInfo(self):
        return self._PetInfo

    @PetInfo.setter
    def PetInfo(self, PetInfo):
        self._PetInfo = PetInfo


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Url = params.get("Url")
        if params.get("PetInfo") is not None:
            self._PetInfo = []
            for item in params.get("PetInfo"):
                obj = BaseAIResultInfo()
                obj._deserialize(item)
                self._PetInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhoneCallAIResultInfo(AbstractModel):
    """打电话识别结果详情

    """

    def __init__(self):
        r"""
        :param _Time: 时间字符串
        :type Time: str
        :param _Url: 截图 URL
        :type Url: str
        :param _PhoneCallInfo: 打电话信息
        :type PhoneCallInfo: list of BaseAIResultInfo
        """
        self._Time = None
        self._Url = None
        self._PhoneCallInfo = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def PhoneCallInfo(self):
        return self._PhoneCallInfo

    @PhoneCallInfo.setter
    def PhoneCallInfo(self, PhoneCallInfo):
        self._PhoneCallInfo = PhoneCallInfo


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Url = params.get("Url")
        if params.get("PhoneCallInfo") is not None:
            self._PhoneCallInfo = []
            for item in params.get("PhoneCallInfo"):
                obj = BaseAIResultInfo()
                obj._deserialize(item)
                self._PhoneCallInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlateContent(AbstractModel):
    """AI车牌信息

    """

    def __init__(self):
        r"""
        :param _Plate: 车牌号信息
        :type Plate: str
        :param _Color: 车牌的颜色
        :type Color: str
        :param _Type: 车牌的种类，例如普通蓝牌
        :type Type: str
        :param _Location: 截图中坐标信息
        :type Location: :class:`tencentcloud.iss.v20230517.models.Location`
        """
        self._Plate = None
        self._Color = None
        self._Type = None
        self._Location = None

    @property
    def Plate(self):
        return self._Plate

    @Plate.setter
    def Plate(self, Plate):
        self._Plate = Plate

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location


    def _deserialize(self, params):
        self._Plate = params.get("Plate")
        self._Color = params.get("Color")
        self._Type = params.get("Type")
        if params.get("Location") is not None:
            self._Location = Location()
            self._Location._deserialize(params.get("Location"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayRecordData(AbstractModel):
    """本地录像播放url数据结构

    """

    def __init__(self):
        r"""
        :param _Flv: 录像播放地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Flv: str
        """
        self._Flv = None

    @property
    def Flv(self):
        return self._Flv

    @Flv.setter
    def Flv(self, Flv):
        self._Flv = Flv


    def _deserialize(self, params):
        self._Flv = params.get("Flv")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayRecordRequest(AbstractModel):
    """PlayRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelId: 通道 ID（从查询通道DescribeDeviceChannel接口中获取）
        :type ChannelId: str
        :param _Start: 起始时间
        :type Start: int
        :param _End:  结束时间
        :type End: int
        :param _StreamType: 流类型（1:主码流；2:子码流（不可以和 Resolution 同时下发））
        :type StreamType: int
        :param _Resolution: 分辨率（1:QCIF；2:CIF； 3:4CIF； 4:D1； 5:720P； 6:1080P/I； 自定义的19201080等等（需设备支持）（不可以和 StreamType 同时下发））
        :type Resolution: str
        :param _IsInternal: 是否内网
        :type IsInternal: bool
        """
        self._ChannelId = None
        self._Start = None
        self._End = None
        self._StreamType = None
        self._Resolution = None
        self._IsInternal = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Start(self):
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End

    @property
    def StreamType(self):
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def IsInternal(self):
        return self._IsInternal

    @IsInternal.setter
    def IsInternal(self, IsInternal):
        self._IsInternal = IsInternal


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._Start = params.get("Start")
        self._End = params.get("End")
        self._StreamType = params.get("StreamType")
        self._Resolution = params.get("Resolution")
        self._IsInternal = params.get("IsInternal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayRecordResponse(AbstractModel):
    """PlayRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.PlayRecordData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = PlayRecordData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class RecordPlanBaseInfo(AbstractModel):
    """实时上云计划基础信息

    """

    def __init__(self):
        r"""
        :param _PlanId: 上云计划ID
        :type PlanId: str
        :param _PlanName: 上云计划名称
        :type PlanName: str
        :param _TemplateId: 上云模板ID
        :type TemplateId: str
        :param _Describe: 上云计划描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
        :param _StreamType: 码流类型，default:设备默认码流类型，main:主码流，sub:子码流，其他根据设备能力集自定义
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamType: str
        :param _LifeCycle: 云文件生命周期
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Status: 录像计划状态，1:正常使用中，0:删除中，无法使用
        :type Status: int
        :param _ChannelCount: 通道总数
        :type ChannelCount: int
        """
        self._PlanId = None
        self._PlanName = None
        self._TemplateId = None
        self._Describe = None
        self._StreamType = None
        self._LifeCycle = None
        self._Status = None
        self._ChannelCount = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanName(self):
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def StreamType(self):
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def LifeCycle(self):
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ChannelCount(self):
        return self._ChannelCount

    @ChannelCount.setter
    def ChannelCount(self, ChannelCount):
        self._ChannelCount = ChannelCount


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        self._Describe = params.get("Describe")
        self._StreamType = params.get("StreamType")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        self._Status = params.get("Status")
        self._ChannelCount = params.get("ChannelCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordPlanChannelInfo(AbstractModel):
    """计划下的设备通道信息

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备通道所属的设备ID
        :type DeviceId: str
        :param _DeviceName: 设备通道所属的设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param _ChannelId: 设备通道ID
        :type ChannelId: str
        :param _ChannelName: 设备通道名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelName: str
        :param _OrganizationName: 所属组织名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationName: str
        """
        self._DeviceId = None
        self._DeviceName = None
        self._ChannelId = None
        self._ChannelName = None
        self._OrganizationName = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        self._OrganizationName = params.get("OrganizationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordPlanOptData(AbstractModel):
    """实时上云计划添加和修改的返回数据

    """

    def __init__(self):
        r"""
        :param _PlanId: 上云计划ID
        :type PlanId: str
        :param _PlanName: 上云计划名称
        :type PlanName: str
        :param _TemplateId: 上云模板ID
        :type TemplateId: str
        :param _Describe: 上云计划描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
        :param _LifeCycle: 云文件生命周期
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _StreamType: 码流类型，default:设备默认码流类型，main:主码流，sub:子码流，其他根据设备能力集自定义
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamType: str
        """
        self._PlanId = None
        self._PlanName = None
        self._TemplateId = None
        self._Describe = None
        self._LifeCycle = None
        self._StreamType = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanName(self):
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def LifeCycle(self):
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def StreamType(self):
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        self._Describe = params.get("Describe")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        self._StreamType = params.get("StreamType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordPlaybackUrl(AbstractModel):
    """云录像回放url

    """

    def __init__(self):
        r"""
        :param _Hls: hls回放url
        :type Hls: str
        """
        self._Hls = None

    @property
    def Hls(self):
        return self._Hls

    @Hls.setter
    def Hls(self, Hls):
        self._Hls = Hls


    def _deserialize(self, params):
        self._Hls = params.get("Hls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordRetrieveTaskChannelInfo(AbstractModel):
    """取回任务通道信息

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备通道所属的设备ID
        :type DeviceId: str
        :param _DeviceName: 设备通道所属的设备名称
        :type DeviceName: str
        :param _ChannelId: 设备通道ID
        :type ChannelId: str
        :param _ChannelName: 设备通道名称 
        :type ChannelName: str
        :param _Status: 任务状态，0:已取回，1:取回中，2:待取回, 3:无归档录像
        :type Status: int
        """
        self._DeviceId = None
        self._DeviceName = None
        self._ChannelId = None
        self._ChannelName = None
        self._Status = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordRetrieveTaskDetailsInfo(AbstractModel):
    """录像取回任务详情基础信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _StartTime: 取回录像的开始时间 
        :type StartTime: int
        :param _EndTime: 取回录像的结束时间
        :type EndTime: int
        :param _Mode: 取回模式，1:极速模式，其他暂不支持
        :type Mode: int
        :param _Expiration: 副本有效期
        :type Expiration: int
        :param _Status: 任务状态， 0:已取回，1:取回中，2:待取回
        :type Status: int
        :param _Capacity: 取回容量，单位MB
        :type Capacity: int
        :param _Describe: 任务描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
        :param _ChannelCount: 任务通道数量
        :type ChannelCount: int
        """
        self._TaskId = None
        self._TaskName = None
        self._StartTime = None
        self._EndTime = None
        self._Mode = None
        self._Expiration = None
        self._Status = None
        self._Capacity = None
        self._Describe = None
        self._ChannelCount = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Expiration(self):
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Capacity(self):
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def ChannelCount(self):
        return self._ChannelCount

    @ChannelCount.setter
    def ChannelCount(self, ChannelCount):
        self._ChannelCount = ChannelCount


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Mode = params.get("Mode")
        self._Expiration = params.get("Expiration")
        self._Status = params.get("Status")
        self._Capacity = params.get("Capacity")
        self._Describe = params.get("Describe")
        self._ChannelCount = params.get("ChannelCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordSliceInfo(AbstractModel):
    """录像切片信息

    """

    def __init__(self):
        r"""
        :param _PlanId: 计划ID
        :type PlanId: str
        :param _List: 录像切片开始和结束时间列表
        :type List: list of RecordTimeLine
        """
        self._PlanId = None
        self._List = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = RecordTimeLine()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTemplateInfo(AbstractModel):
    """实时上云模板信息数据

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID
        :type TemplateId: str
        :param _TemplateName: 模板名称
        :type TemplateName: str
        :param _TimeSections: 上云时间段，按周进行设置，支持一天设置多个时间段，每个时间段不小于10分钟
        :type TimeSections: list of RecordTemplateTimeSections
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TimeSections = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTemplateTimeSections(AbstractModel):
    """上云模板的时间片段数据格式

    """

    def __init__(self):
        r"""
        :param _DayOfWeek: 周日期，取值范围1～7（对应周一～周日
        :type DayOfWeek: int
        :param _StartTime: 开始时间，格式：HH:MM:SS，范围：[00:00:00～23:59:59]
        :type StartTime: str
        :param _EndTime: 结束时间，格式：HH:MM:SS，范围：[00:00:00～23:59:59] 
        :type EndTime: str
        """
        self._DayOfWeek = None
        self._StartTime = None
        self._EndTime = None

    @property
    def DayOfWeek(self):
        return self._DayOfWeek

    @DayOfWeek.setter
    def DayOfWeek(self, DayOfWeek):
        self._DayOfWeek = DayOfWeek

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._DayOfWeek = params.get("DayOfWeek")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTimeLine(AbstractModel):
    """云录像时间片段

    """

    def __init__(self):
        r"""
        :param _Begin: 时间片段开始时间，UTC秒数，例如：1662114146
        :type Begin: int
        :param _End: 时间片段结束时间，UTC秒数，例如：1662114146
        :type End: int
        """
        self._Begin = None
        self._End = None

    @property
    def Begin(self):
        return self._Begin

    @Begin.setter
    def Begin(self, Begin):
        self._Begin = Begin

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._Begin = params.get("Begin")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefreshDeviceChannelRequest(AbstractModel):
    """RefreshDeviceChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备 ID（从获取设备列表ListDevices接口中获取）
        :type DeviceId: str
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
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
        


class RefreshDeviceChannelResponse(AbstractModel):
    """RefreshDeviceChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SmokingAIResultInfo(AbstractModel):
    """抽烟识别结果详情

    """

    def __init__(self):
        r"""
        :param _Time: 时间字符串
        :type Time: str
        :param _Url: 截图 URL
        :type Url: str
        :param _SmokingInfo: 抽烟信息
        :type SmokingInfo: list of BaseAIResultInfo
        """
        self._Time = None
        self._Url = None
        self._SmokingInfo = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def SmokingInfo(self):
        return self._SmokingInfo

    @SmokingInfo.setter
    def SmokingInfo(self, SmokingInfo):
        self._SmokingInfo = SmokingInfo


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Url = params.get("Url")
        if params.get("SmokingInfo") is not None:
            self._SmokingInfo = []
            for item in params.get("SmokingInfo"):
                obj = BaseAIResultInfo()
                obj._deserialize(item)
                self._SmokingInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotConfig(AbstractModel):
    """截图配置

    """

    def __init__(self):
        r"""
        :param _TimeInterval: 截图频率。可选值1～20秒
        :type TimeInterval: int
        :param _OperTimeSlot: 模板生效的时间段。最多包含5组时间段
        :type OperTimeSlot: list of OperTimeSlot
        """
        self._TimeInterval = None
        self._OperTimeSlot = None

    @property
    def TimeInterval(self):
        return self._TimeInterval

    @TimeInterval.setter
    def TimeInterval(self, TimeInterval):
        self._TimeInterval = TimeInterval

    @property
    def OperTimeSlot(self):
        return self._OperTimeSlot

    @OperTimeSlot.setter
    def OperTimeSlot(self, OperTimeSlot):
        self._OperTimeSlot = OperTimeSlot


    def _deserialize(self, params):
        self._TimeInterval = params.get("TimeInterval")
        if params.get("OperTimeSlot") is not None:
            self._OperTimeSlot = []
            for item in params.get("OperTimeSlot"):
                obj = OperTimeSlot()
                obj._deserialize(item)
                self._OperTimeSlot.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubTaskData(AbstractModel):
    """子任务详情

    """

    def __init__(self):
        r"""
        :param _SubTaskId: 子任务ID
        :type SubTaskId: str
        :param _Status: 任务状态1:NEW,2:RUNNING,3:COMPLETED ,4:FAILED
        :type Status: int
        :param _FailReason: 任务失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param _Progress: 任务进度
        :type Progress: float
        :param _Action: 操作类型
        :type Action: str
        :param _ActionZhDesc: 操作类型中文描述
        :type ActionZhDesc: str
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _StartedAt: 启动任务时间
        :type StartedAt: str
        :param _CreatedAt: 创建任务时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新任务时间
        :type UpdatedAt: str
        :param _Runtime: 任务运行时间，单位ms
        :type Runtime: int
        :param _DeviceId: 设备ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param _DeviceName: 设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param _ChannelId: 通道ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelId: str
        :param _ChannelName: 通道名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelName: str
        """
        self._SubTaskId = None
        self._Status = None
        self._FailReason = None
        self._Progress = None
        self._Action = None
        self._ActionZhDesc = None
        self._ResourceId = None
        self._StartedAt = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._Runtime = None
        self._DeviceId = None
        self._DeviceName = None
        self._ChannelId = None
        self._ChannelName = None

    @property
    def SubTaskId(self):
        return self._SubTaskId

    @SubTaskId.setter
    def SubTaskId(self, SubTaskId):
        self._SubTaskId = SubTaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailReason(self):
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ActionZhDesc(self):
        return self._ActionZhDesc

    @ActionZhDesc.setter
    def ActionZhDesc(self, ActionZhDesc):
        self._ActionZhDesc = ActionZhDesc

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def StartedAt(self):
        return self._StartedAt

    @StartedAt.setter
    def StartedAt(self, StartedAt):
        self._StartedAt = StartedAt

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Runtime(self):
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName


    def _deserialize(self, params):
        self._SubTaskId = params.get("SubTaskId")
        self._Status = params.get("Status")
        self._FailReason = params.get("FailReason")
        self._Progress = params.get("Progress")
        self._Action = params.get("Action")
        self._ActionZhDesc = params.get("ActionZhDesc")
        self._ResourceId = params.get("ResourceId")
        self._StartedAt = params.get("StartedAt")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._Runtime = params.get("Runtime")
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskData(AbstractModel):
    """查询复杂任务详情返回结果

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _Status: 任务状态1:NEW,2:RUNNING,3:COMPLETED ,4:FAILED
        :type Status: int
        :param _FailReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param _Progress: 进度（0-1）
        :type Progress: float
        :param _Action: 任务操作类型，批量任务类型以Batch开头
        :type Action: str
        :param _ActionZhDesc: 操作类型中文描述
        :type ActionZhDesc: str
        :param _TaskType: 任务类型 1.简单 2.复杂 3.子任务
        :type TaskType: int
        :param _ResourceId: 任务资源id（复杂任务该字段无效）
        :type ResourceId: str
        :param _Total: 总任务数（仅复杂任务有效）
        :type Total: int
        :param _SuccessCount: 成功任务数（仅复杂任务有效）
        :type SuccessCount: int
        :param _FailCount: 失败任务数（仅复杂任务有效）
        :type FailCount: int
        :param _RunningCount: 运行任务数（仅复杂任务有效）
        :type RunningCount: int
        :param _StartedAt: 启动任务时间
        :type StartedAt: str
        :param _CreatedAt: 创建任务时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新任务时间
        :type UpdatedAt: str
        :param _Runtime: 任务运行时间，单位ms
        :type Runtime: int
        :param _DeviceId: 设备ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param _DeviceName: 设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param _ChannelId: 通道ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelId: str
        :param _ChannelName:  通道名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelName: str
        """
        self._TaskId = None
        self._Status = None
        self._FailReason = None
        self._Progress = None
        self._Action = None
        self._ActionZhDesc = None
        self._TaskType = None
        self._ResourceId = None
        self._Total = None
        self._SuccessCount = None
        self._FailCount = None
        self._RunningCount = None
        self._StartedAt = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._Runtime = None
        self._DeviceId = None
        self._DeviceName = None
        self._ChannelId = None
        self._ChannelName = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailReason(self):
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ActionZhDesc(self):
        return self._ActionZhDesc

    @ActionZhDesc.setter
    def ActionZhDesc(self, ActionZhDesc):
        self._ActionZhDesc = ActionZhDesc

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def SuccessCount(self):
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def FailCount(self):
        return self._FailCount

    @FailCount.setter
    def FailCount(self, FailCount):
        self._FailCount = FailCount

    @property
    def RunningCount(self):
        return self._RunningCount

    @RunningCount.setter
    def RunningCount(self, RunningCount):
        self._RunningCount = RunningCount

    @property
    def StartedAt(self):
        return self._StartedAt

    @StartedAt.setter
    def StartedAt(self, StartedAt):
        self._StartedAt = StartedAt

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Runtime(self):
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._FailReason = params.get("FailReason")
        self._Progress = params.get("Progress")
        self._Action = params.get("Action")
        self._ActionZhDesc = params.get("ActionZhDesc")
        self._TaskType = params.get("TaskType")
        self._ResourceId = params.get("ResourceId")
        self._Total = params.get("Total")
        self._SuccessCount = params.get("SuccessCount")
        self._FailCount = params.get("FailCount")
        self._RunningCount = params.get("RunningCount")
        self._StartedAt = params.get("StartedAt")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._Runtime = params.get("Runtime")
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Timeline(AbstractModel):
    """时间片段结构体

    """

    def __init__(self):
        r"""
        :param _Begin: 分片起始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Begin: int
        :param _End: 分片结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type End: int
        """
        self._Begin = None
        self._End = None

    @property
    def Begin(self):
        return self._Begin

    @Begin.setter
    def Begin(self, Begin):
        self._Begin = Begin

    @property
    def End(self):
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._Begin = params.get("Begin")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAITaskRequest(AbstractModel):
    """UpdateAITask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: AI 任务 ID
        :type TaskId: str
        :param _Name: AI 任务名称。仅支持中文、英文、数字、_、-，长度不超过32个字符
        :type Name: str
        :param _Desc: AI 任务描述。仅支持中文、英文、数字、_、-，长度不超过128个字符
        :type Desc: str
        :param _ChannelList: 通道 ID 列表。不能添加存在于其他 AI 任务的通道，限制1000个通道。
        :type ChannelList: list of str
        :param _CallbackUrl: AI 结果回调地址。类似 "http://ip:port/***或者https://domain/***
        :type CallbackUrl: str
        :param _IsStartTheTask: 是否立即开启 AI 任务。"true"代表立即开启 AI 任务，"false"代表暂不开启 AI 任务，默认为 false。
        :type IsStartTheTask: bool
        :param _Templates: AI 配置列表
        :type Templates: list of AITemplates
        """
        self._TaskId = None
        self._Name = None
        self._Desc = None
        self._ChannelList = None
        self._CallbackUrl = None
        self._IsStartTheTask = None
        self._Templates = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ChannelList(self):
        return self._ChannelList

    @ChannelList.setter
    def ChannelList(self, ChannelList):
        self._ChannelList = ChannelList

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def IsStartTheTask(self):
        return self._IsStartTheTask

    @IsStartTheTask.setter
    def IsStartTheTask(self, IsStartTheTask):
        self._IsStartTheTask = IsStartTheTask

    @property
    def Templates(self):
        return self._Templates

    @Templates.setter
    def Templates(self, Templates):
        self._Templates = Templates


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._ChannelList = params.get("ChannelList")
        self._CallbackUrl = params.get("CallbackUrl")
        self._IsStartTheTask = params.get("IsStartTheTask")
        if params.get("Templates") is not None:
            self._Templates = []
            for item in params.get("Templates"):
                obj = AITemplates()
                obj._deserialize(item)
                self._Templates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAITaskResponse(AbstractModel):
    """UpdateAITask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: AI任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iss.v20230517.models.AITaskInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AITaskInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateAITaskStatusRequest(AbstractModel):
    """UpdateAITaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: AI 任务 ID
        :type TaskId: str
        :param _Status: AI 任务状态。"on"代表开启了 AI 分析任务，"off"代表停止AI分析任务
        :type Status: str
        """
        self._TaskId = None
        self._Status = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAITaskStatusResponse(AbstractModel):
    """UpdateAITaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateDeviceData(AbstractModel):
    """修改设备接口返回数据

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param _Code: 设备编码（国标设备即我们为设备生成的20位国标编码，rtmp 设备为10 位设备编码）
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param _Name: 设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _AccessProtocol: 设备接入协议，1:RTMP,2:GB,3:GW 
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessProtocol: int
        :param _Type: 设备类型，1:IPC,2:NVR
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _ClusterId: 设备接入服务节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ClusterName: 设备接入服务节点名称

注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param _TransportProtocol: 设备流传输协议，1:UDP,2:TCP 
注意：此字段可能返回 null，表示取不到有效值。
        :type TransportProtocol: int
        :param _Password: 设备密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param _Description: 设备描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Status: 设备状态，0:未注册,1:在线,2:离线,3:禁用
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _OrganizationId: 设备所属组织ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationId: int
        :param _GatewayId: 设备接入网关ID，从查询网关列表接口中获取（仅网关接入需要）
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayId: str
        :param _ProtocolType: 网关接入协议类型，1.海康SDK，2.大华SDK，3.宇视SDK，4.Onvif（仅网关接入需要）
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtocolType: int
        :param _Ip: 设备接入IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Port: 设备Port
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Username: 设备用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type Username: str
        :param _AppId: 用户Id
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        """
        self._DeviceId = None
        self._Code = None
        self._Name = None
        self._AccessProtocol = None
        self._Type = None
        self._ClusterId = None
        self._ClusterName = None
        self._TransportProtocol = None
        self._Password = None
        self._Description = None
        self._Status = None
        self._OrganizationId = None
        self._GatewayId = None
        self._ProtocolType = None
        self._Ip = None
        self._Port = None
        self._Username = None
        self._AppId = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AccessProtocol(self):
        return self._AccessProtocol

    @AccessProtocol.setter
    def AccessProtocol(self, AccessProtocol):
        self._AccessProtocol = AccessProtocol

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def TransportProtocol(self):
        return self._TransportProtocol

    @TransportProtocol.setter
    def TransportProtocol(self, TransportProtocol):
        self._TransportProtocol = TransportProtocol

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ProtocolType(self):
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Code = params.get("Code")
        self._Name = params.get("Name")
        self._AccessProtocol = params.get("AccessProtocol")
        self._Type = params.get("Type")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._TransportProtocol = params.get("TransportProtocol")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._OrganizationId = params.get("OrganizationId")
        self._GatewayId = params.get("GatewayId")
        self._ProtocolType = params.get("ProtocolType")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Username = params.get("Username")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceOrganizationRequest(AbstractModel):
    """UpdateDeviceOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceIds: 设备 ID 数组（从获取设备列表接口ListDevices中获取）
        :type DeviceIds: list of str
        :param _OrganizationId: 组织 ID（从查询组织接口DescribeOrganization中获取）
        :type OrganizationId: str
        """
        self._DeviceIds = None
        self._OrganizationId = None

    @property
    def DeviceIds(self):
        return self._DeviceIds

    @DeviceIds.setter
    def DeviceIds(self, DeviceIds):
        self._DeviceIds = DeviceIds

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId


    def _deserialize(self, params):
        self._DeviceIds = params.get("DeviceIds")
        self._OrganizationId = params.get("OrganizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceOrganizationResponse(AbstractModel):
    """UpdateDeviceOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateDeviceStatusRequest(AbstractModel):
    """UpdateDeviceStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备 ID（从获取设备列表接口ListDevices中获取）
        :type DeviceId: str
        :param _Status: 禁用启用状态码（2：启用，3:禁用）
        :type Status: int
        """
        self._DeviceId = None
        self._Status = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceStatusResponse(AbstractModel):
    """UpdateDeviceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateGatewayData(AbstractModel):
    """修改网关信息返回结果

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关索引ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayId: str
        :param _GwId: 网关编码
注意：此字段可能返回 null，表示取不到有效值。
        :type GwId: str
        :param _Name: 网关名称，仅支持中文、英文、数字、_、-，长度不超过32个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: 网关描述，仅支持中文、英文、数字、_、-，长度不超过128个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _ClusterId: 服务节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ClusterName: 服务节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param _Status: 网关状态，0：离线，1:在线
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreatedAt: 激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: int
        :param _Secret: 网关密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type Secret: str
        :param _Version: 网关版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        """
        self._GatewayId = None
        self._GwId = None
        self._Name = None
        self._Description = None
        self._ClusterId = None
        self._ClusterName = None
        self._Status = None
        self._CreatedAt = None
        self._Secret = None
        self._Version = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GwId(self):
        return self._GwId

    @GwId.setter
    def GwId(self, GwId):
        self._GwId = GwId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def Secret(self):
        return self._Secret

    @Secret.setter
    def Secret(self, Secret):
        self._Secret = Secret

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GwId = params.get("GwId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Status = params.get("Status")
        self._CreatedAt = params.get("CreatedAt")
        self._Secret = params.get("Secret")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGatewayRequest(AbstractModel):
    """UpdateGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关索引ID（从获取网关列表ListGateways接口中获取）	
        :type GatewayId: str
        :param _Name: 仅支持中文、英文、数网关名称，字、_、-，长度不超过32个字符
        :type Name: str
        :param _Description: 网关描述，仅支持中文、英文、数字、_、-，长度不超过128个字符
        :type Description: str
        """
        self._GatewayId = None
        self._Name = None
        self._Description = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGatewayResponse(AbstractModel):
    """UpdateGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.UpdateGatewayData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = UpdateGatewayData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateOrgData(AbstractModel):
    """修改组织接口返回数据

    """

    def __init__(self):
        r"""
        :param _OrganizationId: 组织 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationId: str
        :param _Name: 组织名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _ParentId: 组织父节点 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentId: str
        :param _Level: 组织层级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param _AppId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _ParentIds: 组织结构
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentIds: str
        :param _Total: 设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Online: 设备在线数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Online: int
        """
        self._OrganizationId = None
        self._Name = None
        self._ParentId = None
        self._Level = None
        self._AppId = None
        self._ParentIds = None
        self._Total = None
        self._Online = None

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParentId(self):
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ParentIds(self):
        return self._ParentIds

    @ParentIds.setter
    def ParentIds(self, ParentIds):
        self._ParentIds = ParentIds

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Online(self):
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        self._Name = params.get("Name")
        self._ParentId = params.get("ParentId")
        self._Level = params.get("Level")
        self._AppId = params.get("AppId")
        self._ParentIds = params.get("ParentIds")
        self._Total = params.get("Total")
        self._Online = params.get("Online")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationRequest(AbstractModel):
    """UpdateOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrganizationId: 组织ID（从查询组织接口DescribeOrganization中获取）
        :type OrganizationId: str
        :param _Name: 组织名称
        :type Name: str
        """
        self._OrganizationId = None
        self._Name = None

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationResponse(AbstractModel):
    """UpdateOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.UpdateOrgData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = UpdateOrgData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateRecordBackupPlanData(AbstractModel):
    """修改录像上云计划返回数据

    """

    def __init__(self):
        r"""
        :param _PlanId: 录像上云计划ID
        :type PlanId: str
        :param _PlanName: 录像上云计划名称
        :type PlanName: str
        :param _TemplateId: 录像上云模板ID
        :type TemplateId: str
        :param _Describe: 录像上云计划描述
        :type Describe: str
        :param _LifeCycle: 云文件生命周期
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Status: 录像上云计划状态，1:正常使用中，0:删除中，无法使用
        :type Status: int
        :param _ChannelCount: 通道数量
        :type ChannelCount: int
        :param _CreateAt: 创建时间
        :type CreateAt: str
        :param _UpdateAt: 修改时间
        :type UpdateAt: str
        """
        self._PlanId = None
        self._PlanName = None
        self._TemplateId = None
        self._Describe = None
        self._LifeCycle = None
        self._Status = None
        self._ChannelCount = None
        self._CreateAt = None
        self._UpdateAt = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanName(self):
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def LifeCycle(self):
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ChannelCount(self):
        return self._ChannelCount

    @ChannelCount.setter
    def ChannelCount(self, ChannelCount):
        self._ChannelCount = ChannelCount

    @property
    def CreateAt(self):
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        self._Describe = params.get("Describe")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        self._Status = params.get("Status")
        self._ChannelCount = params.get("ChannelCount")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordBackupPlanModify(AbstractModel):
    """修改录像上云计划数据结构

    """

    def __init__(self):
        r"""
        :param _PlanName: 录像上云计划名称（仅支持中文、英文、数字、_、-，长度不超过32个字符，计划名称全局唯一，不能为空，不能重复，不修改名称时，不需要该字段）
        :type PlanName: str
        :param _TemplateId: 录制模板ID（从查询录像上云模板列表接口ListRecordBackupTemplates中获取，不修改模板ID时，不需要该字段）
        :type TemplateId: str
        :param _Describe: 录像上云计划描述（仅支持中文、英文、数字、_、-，长度不超过128个字符， 不修改描述时，不需要该字段）
        :type Describe: str
        :param _LifeCycle: 生命周期（录像文件生命周期设置，管理文件冷、热存储的时间，不修改生命周期时，不需要该字段）
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Add: 要新增的设备通道（Json数组，没有新增时，不需要该字段，一次添加通道总数不超过5000个，包括组织目录下的通道数量）
        :type Add: list of ChannelInfo
        :param _Del: 要删除的设备通道（Json数组，内容为要删除的设备通道id，没有删除设备通道时，不需要该字段）
        :type Del: list of str
        :param _OrganizationId: 添加组织目录下所有设备通道（Json数组，可以为空，并且通道总数量不超过5000个（包括Add字段通道数量））
        :type OrganizationId: list of str
        """
        self._PlanName = None
        self._TemplateId = None
        self._Describe = None
        self._LifeCycle = None
        self._Add = None
        self._Del = None
        self._OrganizationId = None

    @property
    def PlanName(self):
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def LifeCycle(self):
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Add(self):
        return self._Add

    @Add.setter
    def Add(self, Add):
        self._Add = Add

    @property
    def Del(self):
        return self._Del

    @Del.setter
    def Del(self, Del):
        self._Del = Del

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId


    def _deserialize(self, params):
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        self._Describe = params.get("Describe")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        if params.get("Add") is not None:
            self._Add = []
            for item in params.get("Add"):
                obj = ChannelInfo()
                obj._deserialize(item)
                self._Add.append(obj)
        self._Del = params.get("Del")
        self._OrganizationId = params.get("OrganizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordBackupPlanRequest(AbstractModel):
    """UpdateRecordBackupPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 计划ID
        :type PlanId: str
        :param _Mod: 修改的内容
        :type Mod: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupPlanModify`
        """
        self._PlanId = None
        self._Mod = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def Mod(self):
        return self._Mod

    @Mod.setter
    def Mod(self, Mod):
        self._Mod = Mod


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        if params.get("Mod") is not None:
            self._Mod = UpdateRecordBackupPlanModify()
            self._Mod._deserialize(params.get("Mod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordBackupPlanResponse(AbstractModel):
    """UpdateRecordBackupPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupPlanData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = UpdateRecordBackupPlanData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateRecordBackupTemplateData(AbstractModel):
    """修改录像上云模板返回数据

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param _TemplateName: 模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateName: str
        :param _TimeSections: 上云时间段（按周进行设置，支持一天设置多个时间段，每个时间段不小于10分钟）
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSections: list of RecordTemplateTimeSections
        :param _DevTimeSections: 录像时间段（按周进行设置，支持一天设置多个时间段，每个时间段不小于10分钟）
注意：此字段可能返回 null，表示取不到有效值。
        :type DevTimeSections: list of RecordTemplateTimeSections
        :param _Scale: 上云倍速（支持1，2，4倍速）
注意：此字段可能返回 null，表示取不到有效值。
        :type Scale: int
        :param _CreateAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateAt: str
        :param _UpdateAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateAt: str
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TimeSections = None
        self._DevTimeSections = None
        self._Scale = None
        self._CreateAt = None
        self._UpdateAt = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections

    @property
    def DevTimeSections(self):
        return self._DevTimeSections

    @DevTimeSections.setter
    def DevTimeSections(self, DevTimeSections):
        self._DevTimeSections = DevTimeSections

    @property
    def Scale(self):
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale

    @property
    def CreateAt(self):
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        if params.get("DevTimeSections") is not None:
            self._DevTimeSections = []
            for item in params.get("DevTimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._DevTimeSections.append(obj)
        self._Scale = params.get("Scale")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordBackupTemplateModify(AbstractModel):
    """修改录像上云模板数据结构

    """

    def __init__(self):
        r"""
        :param _TemplateName: 模板名称（不修改名称时，不需要带该字段）
        :type TemplateName: str
        :param _TimeSections: 上云时间段（按周进行设置，支持一天设置多个时间段，每个时间段不小于10分钟）
        :type TimeSections: list of RecordTemplateTimeSections
        :param _DevTimeSections: 录像时间段（按周进行设置，支持一天设置多个时间段，每个时间段不小于10分钟）
        :type DevTimeSections: list of RecordTemplateTimeSections
        :param _Scale: 上云倍速（支持1，2，4倍速）
        :type Scale: int
        """
        self._TemplateName = None
        self._TimeSections = None
        self._DevTimeSections = None
        self._Scale = None

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections

    @property
    def DevTimeSections(self):
        return self._DevTimeSections

    @DevTimeSections.setter
    def DevTimeSections(self, DevTimeSections):
        self._DevTimeSections = DevTimeSections

    @property
    def Scale(self):
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        if params.get("DevTimeSections") is not None:
            self._DevTimeSections = []
            for item in params.get("DevTimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._DevTimeSections.append(obj)
        self._Scale = params.get("Scale")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordBackupTemplateRequest(AbstractModel):
    """UpdateRecordBackupTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID（从查询录像上云模板列表接口ListRecordBackupTemplates中获取）
        :type TemplateId: str
        :param _Mod: 修改录像上云模板数据
        :type Mod: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupTemplateModify`
        """
        self._TemplateId = None
        self._Mod = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Mod(self):
        return self._Mod

    @Mod.setter
    def Mod(self, Mod):
        self._Mod = Mod


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        if params.get("Mod") is not None:
            self._Mod = UpdateRecordBackupTemplateModify()
            self._Mod._deserialize(params.get("Mod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordBackupTemplateResponse(AbstractModel):
    """UpdateRecordBackupTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupTemplateData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = UpdateRecordBackupTemplateData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateRecordPlanData(AbstractModel):
    """修改实时上云录像计划的数据

    """

    def __init__(self):
        r"""
        :param _PlanName: 上云计划名称，仅支持中文、英文、数字、_、-，长度不超过32个字符，计划名称全局唯一，不能为空，不能重复，不修改名称时，不需要该字段
        :type PlanName: str
        :param _TemplateId: 上云模板ID，不修改模板ID时，不需要该字段
        :type TemplateId: str
        :param _Describe: 上云计划描述，仅支持中文、英文、数字、_、-，长度不超过128个字符， 不修改描述时，不需要该字段
        :type Describe: str
        :param _StreamType: 码流类型，default:不指定码流类型，以设备默认推送类型为主， main:主码流，sub:子码流，其他根据设备能力集自定义，长度不能超过32个字节
        :type StreamType: str
        :param _LifeCycle: 生命周期，文件生命周期设置，管理文件冷、热存储的时间，不修改生命周期时，不需要该字段
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Add: 要新增的设备通道,Json数组，没有新增时，不需要该字段，一次添加通道总数不超过5000个，包括组织目录下的通道数量
        :type Add: list of ChannelInfo
        :param _Del: 要删除的设备通道，Json数组，内容为要删除的设备通道id，没有删除设备通道时，不需要该字段
        :type Del: list of str
        :param _OrganizationId: 组织目录ID，添加组织目录下所有设备通道，Json数组，可以为空，并且通道总数量不超过5000个（包括Add字段通道数量）
        :type OrganizationId: list of str
        """
        self._PlanName = None
        self._TemplateId = None
        self._Describe = None
        self._StreamType = None
        self._LifeCycle = None
        self._Add = None
        self._Del = None
        self._OrganizationId = None

    @property
    def PlanName(self):
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def StreamType(self):
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def LifeCycle(self):
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Add(self):
        return self._Add

    @Add.setter
    def Add(self, Add):
        self._Add = Add

    @property
    def Del(self):
        return self._Del

    @Del.setter
    def Del(self, Del):
        self._Del = Del

    @property
    def OrganizationId(self):
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId


    def _deserialize(self, params):
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        self._Describe = params.get("Describe")
        self._StreamType = params.get("StreamType")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        if params.get("Add") is not None:
            self._Add = []
            for item in params.get("Add"):
                obj = ChannelInfo()
                obj._deserialize(item)
                self._Add.append(obj)
        self._Del = params.get("Del")
        self._OrganizationId = params.get("OrganizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordPlanRequest(AbstractModel):
    """UpdateRecordPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 计划ID
        :type PlanId: str
        :param _Mod: 修改计划的内容
        :type Mod: :class:`tencentcloud.iss.v20230517.models.UpdateRecordPlanData`
        """
        self._PlanId = None
        self._Mod = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def Mod(self):
        return self._Mod

    @Mod.setter
    def Mod(self, Mod):
        self._Mod = Mod


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        if params.get("Mod") is not None:
            self._Mod = UpdateRecordPlanData()
            self._Mod._deserialize(params.get("Mod"))
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
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.RecordPlanOptData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = RecordPlanOptData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateRecordTemplateData(AbstractModel):
    """修改实时上云模板的请求数据结构

    """

    def __init__(self):
        r"""
        :param _TemplateName: 模板名称， 不修改名称时，不需要带该字段
        :type TemplateName: str
        :param _TimeSections: 上云时间段，不修改名称时，不需要带该字段
        :type TimeSections: list of RecordTemplateTimeSections
        """
        self._TemplateName = None
        self._TimeSections = None

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordTemplateRequest(AbstractModel):
    """UpdateRecordTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID
        :type TemplateId: str
        :param _Mod: 修改内容
        :type Mod: :class:`tencentcloud.iss.v20230517.models.UpdateRecordTemplateData`
        """
        self._TemplateId = None
        self._Mod = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Mod(self):
        return self._Mod

    @Mod.setter
    def Mod(self, Mod):
        self._Mod = Mod


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        if params.get("Mod") is not None:
            self._Mod = UpdateRecordTemplateData()
            self._Mod._deserialize(params.get("Mod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordTemplateResponse(AbstractModel):
    """UpdateRecordTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
        :type Data: :class:`tencentcloud.iss.v20230517.models.RecordTemplateInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = RecordTemplateInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateUserDeviceRequest(AbstractModel):
    """UpdateUserDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID（从获取设备列表接口ListDevices中获取）
        :type DeviceId: str
        :param _Name: 设备名称（仅支持中文、英文、数字、_、-，长度不超过32个字符）
        :type Name: str
        :param _TransportProtocol: 设备流传输协议，仅国标设备有效，填0则不做更改（1:UDP,2:TCP）
        :type TransportProtocol: int
        :param _Password: 设备密码（仅国标，网关设备支持）
        :type Password: str
        :param _Description: 设备描述（仅支持中文、英文、数字、_、-，长度不超过128位）
        :type Description: str
        :param _Ip: 设备接入Ip（仅网关接入支持）
        :type Ip: str
        :param _Port: 设备Port（仅网关接入支持）
        :type Port: int
        :param _Username: 设备用户名（仅网关接入支持）
        :type Username: str
        :param _ProtocolType: 网关设备接入协议（仅网关接入支持）
        :type ProtocolType: int
        :param _AudioSwitch: 音频关开（0：关闭；1：开启）默认开启，关闭时丢弃音频
        :type AudioSwitch: int
        :param _SubscribeSwitch: 订阅开关（0：关闭；1：开启）默认开启，开启状态下会订阅设备通道变化，仅国标NVR设备有效
        :type SubscribeSwitch: int
        """
        self._DeviceId = None
        self._Name = None
        self._TransportProtocol = None
        self._Password = None
        self._Description = None
        self._Ip = None
        self._Port = None
        self._Username = None
        self._ProtocolType = None
        self._AudioSwitch = None
        self._SubscribeSwitch = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TransportProtocol(self):
        return self._TransportProtocol

    @TransportProtocol.setter
    def TransportProtocol(self, TransportProtocol):
        self._TransportProtocol = TransportProtocol

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def ProtocolType(self):
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def AudioSwitch(self):
        return self._AudioSwitch

    @AudioSwitch.setter
    def AudioSwitch(self, AudioSwitch):
        self._AudioSwitch = AudioSwitch

    @property
    def SubscribeSwitch(self):
        return self._SubscribeSwitch

    @SubscribeSwitch.setter
    def SubscribeSwitch(self, SubscribeSwitch):
        self._SubscribeSwitch = SubscribeSwitch


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Name = params.get("Name")
        self._TransportProtocol = params.get("TransportProtocol")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Username = params.get("Username")
        self._ProtocolType = params.get("ProtocolType")
        self._AudioSwitch = params.get("AudioSwitch")
        self._SubscribeSwitch = params.get("SubscribeSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserDeviceResponse(AbstractModel):
    """UpdateUserDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: :class:`tencentcloud.iss.v20230517.models.UpdateDeviceData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = UpdateDeviceData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpgradeGatewayRequest(AbstractModel):
    """UpgradeGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关索引ID（从获取网关列表ListGateways接口中获取）
        :type GatewayId: str
        """
        self._GatewayId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeGatewayResponse(AbstractModel):
    """UpgradeGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")