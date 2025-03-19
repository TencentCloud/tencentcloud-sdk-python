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


class Action(AbstractModel):
    """动作信息

    """

    def __init__(self):
        r"""
        :param _Id: 动作id
        :type Id: int
        :param _Name: 动作名
        :type Name: str
        """
        self._Id = None
        self._Name = None

    @property
    def Id(self):
        """动作id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """动作名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionDetail(AbstractModel):
    """详细动作信息

    """

    def __init__(self):
        r"""
        :param _Id: 动作id
        :type Id: int
        :param _Name: 动作名称
        :type Name: str
        :param _ActionType: 动作类型
        :type ActionType: str
        :param _ActionDesc: 动作说明
        :type ActionDesc: str
        :param _MsgType: 消息类型，orgin/custom/model
        :type MsgType: str
        :param _MsgContent: 消息内容,有效值为x-json:后的字段
        :type MsgContent: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _WID: 设备唯一标识
        :type WID: str
        :param _LinkRuleSet: 关联故障列表
        :type LinkRuleSet: list of LinkRule
        :param _SinkConfig: 动作下沉配置,有效值为x-json:后的字段
        :type SinkConfig: str
        """
        self._Id = None
        self._Name = None
        self._ActionType = None
        self._ActionDesc = None
        self._MsgType = None
        self._MsgContent = None
        self._CreateTime = None
        self._WID = None
        self._LinkRuleSet = None
        self._SinkConfig = None

    @property
    def Id(self):
        """动作id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """动作名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ActionType(self):
        """动作类型
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActionDesc(self):
        """动作说明
        :rtype: str
        """
        return self._ActionDesc

    @ActionDesc.setter
    def ActionDesc(self, ActionDesc):
        self._ActionDesc = ActionDesc

    @property
    def MsgType(self):
        """消息类型，orgin/custom/model
        :rtype: str
        """
        return self._MsgType

    @MsgType.setter
    def MsgType(self, MsgType):
        self._MsgType = MsgType

    @property
    def MsgContent(self):
        """消息内容,有效值为x-json:后的字段
        :rtype: str
        """
        return self._MsgContent

    @MsgContent.setter
    def MsgContent(self, MsgContent):
        self._MsgContent = MsgContent

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
    def WID(self):
        """设备唯一标识
        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID

    @property
    def LinkRuleSet(self):
        """关联故障列表
        :rtype: list of LinkRule
        """
        return self._LinkRuleSet

    @LinkRuleSet.setter
    def LinkRuleSet(self, LinkRuleSet):
        self._LinkRuleSet = LinkRuleSet

    @property
    def SinkConfig(self):
        """动作下沉配置,有效值为x-json:后的字段
        :rtype: str
        """
        return self._SinkConfig

    @SinkConfig.setter
    def SinkConfig(self, SinkConfig):
        self._SinkConfig = SinkConfig


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._ActionType = params.get("ActionType")
        self._ActionDesc = params.get("ActionDesc")
        self._MsgType = params.get("MsgType")
        self._MsgContent = params.get("MsgContent")
        self._CreateTime = params.get("CreateTime")
        self._WID = params.get("WID")
        if params.get("LinkRuleSet") is not None:
            self._LinkRuleSet = []
            for item in params.get("LinkRuleSet"):
                obj = LinkRule()
                obj._deserialize(item)
                self._LinkRuleSet.append(obj)
        self._SinkConfig = params.get("SinkConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionObj(AbstractModel):
    """动作对象

    """

    def __init__(self):
        r"""
        :param _Id: 动作id
        :type Id: int
        :param _Name: 动作名称
        :type Name: str
        :param _Type: 动作类型。（app/推送消息至应用-携带空间设备：无,appWithNearbyDevices/推送至应用-携带空间设备：携带,device/推送消息至设备-指定设备,nearbyDevices/推送消息至设备-事件所在范围内的设备,toAlarm/转换为告警,toNotification/转换为通知）
        :type Type: str
        :param _Desc: 动作说明
        :type Desc: str
        :param _MsgType: 消息类型，orgin/custom/model
        :type MsgType: str
        :param _MsgContent: 消息内容
        :type MsgContent: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _SinkConfig: 动作下沉配置
        :type SinkConfig: str
        :param _ApplyDevice:  具体应用（appid）/具体设备（DIN/subID）
        :type ApplyDevice: str
        """
        self._Id = None
        self._Name = None
        self._Type = None
        self._Desc = None
        self._MsgType = None
        self._MsgContent = None
        self._CreateTime = None
        self._SinkConfig = None
        self._ApplyDevice = None

    @property
    def Id(self):
        """动作id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """动作名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """动作类型。（app/推送消息至应用-携带空间设备：无,appWithNearbyDevices/推送至应用-携带空间设备：携带,device/推送消息至设备-指定设备,nearbyDevices/推送消息至设备-事件所在范围内的设备,toAlarm/转换为告警,toNotification/转换为通知）
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Desc(self):
        """动作说明
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def MsgType(self):
        """消息类型，orgin/custom/model
        :rtype: str
        """
        return self._MsgType

    @MsgType.setter
    def MsgType(self, MsgType):
        self._MsgType = MsgType

    @property
    def MsgContent(self):
        """消息内容
        :rtype: str
        """
        return self._MsgContent

    @MsgContent.setter
    def MsgContent(self, MsgContent):
        self._MsgContent = MsgContent

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
    def SinkConfig(self):
        """动作下沉配置
        :rtype: str
        """
        return self._SinkConfig

    @SinkConfig.setter
    def SinkConfig(self, SinkConfig):
        self._SinkConfig = SinkConfig

    @property
    def ApplyDevice(self):
        """ 具体应用（appid）/具体设备（DIN/subID）
        :rtype: str
        """
        return self._ApplyDevice

    @ApplyDevice.setter
    def ApplyDevice(self, ApplyDevice):
        self._ApplyDevice = ApplyDevice


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Desc = params.get("Desc")
        self._MsgType = params.get("MsgType")
        self._MsgContent = params.get("MsgContent")
        self._CreateTime = params.get("CreateTime")
        self._SinkConfig = params.get("SinkConfig")
        self._ApplyDevice = params.get("ApplyDevice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAlarmProcessRecordRequest(AbstractModel):
    """AddAlarmProcessRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordSet: 处理记录项
        :type RecordSet: list of ProcessRecordInfo
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _ApplicationId: 非孪生平台外部应用appid
        :type ApplicationId: int
        :param _ExtendOne: 此字段填写的是非孪生中台的用户id（多个用逗号分隔），如果是非孪生中台用户必填该字段

        :type ExtendOne: str
        """
        self._RecordSet = None
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._ApplicationId = None
        self._ExtendOne = None

    @property
    def RecordSet(self):
        """处理记录项
        :rtype: list of ProcessRecordInfo
        """
        return self._RecordSet

    @RecordSet.setter
    def RecordSet(self, RecordSet):
        self._RecordSet = RecordSet

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def ApplicationId(self):
        """非孪生平台外部应用appid
        :rtype: int
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ExtendOne(self):
        """此字段填写的是非孪生中台的用户id（多个用逗号分隔），如果是非孪生中台用户必填该字段

        :rtype: str
        """
        return self._ExtendOne

    @ExtendOne.setter
    def ExtendOne(self, ExtendOne):
        self._ExtendOne = ExtendOne


    def _deserialize(self, params):
        if params.get("RecordSet") is not None:
            self._RecordSet = []
            for item in params.get("RecordSet"):
                obj = ProcessRecordInfo()
                obj._deserialize(item)
                self._RecordSet.append(obj)
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        self._ApplicationId = params.get("ApplicationId")
        self._ExtendOne = params.get("ExtendOne")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAlarmProcessRecordResponse(AbstractModel):
    """AddAlarmProcessRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 添加告警处理记录结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """添加告警处理记录结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = EmptyRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class AddDeviceInfo(AbstractModel):
    """添加设备信息

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品id
        :type ProductId: int
        :param _SN: 设备sn序列号
        :type SN: str
        :param _ParentWID: 父设备wid，不为空表示导入子设备
        :type ParentWID: str
        :param _KeySource: 密钥来源：0-使用产品密钥 1-使用设备特有的密钥
        :type KeySource: int
        """
        self._ProductId = None
        self._SN = None
        self._ParentWID = None
        self._KeySource = None

    @property
    def ProductId(self):
        """产品id
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def SN(self):
        """设备sn序列号
        :rtype: str
        """
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN

    @property
    def ParentWID(self):
        """父设备wid，不为空表示导入子设备
        :rtype: str
        """
        return self._ParentWID

    @ParentWID.setter
    def ParentWID(self, ParentWID):
        self._ParentWID = ParentWID

    @property
    def KeySource(self):
        """密钥来源：0-使用产品密钥 1-使用设备特有的密钥
        :rtype: int
        """
        return self._KeySource

    @KeySource.setter
    def KeySource(self, KeySource):
        self._KeySource = KeySource


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._SN = params.get("SN")
        self._ParentWID = params.get("ParentWID")
        self._KeySource = params.get("KeySource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdministrationData(AbstractModel):
    """行政区划数据结构

    """

    def __init__(self):
        r"""
        :param _AdministrationCode: 行政区划编码
        :type AdministrationCode: str
        :param _AdministrationName: 行政区划名称
        :type AdministrationName: str
        """
        self._AdministrationCode = None
        self._AdministrationName = None

    @property
    def AdministrationCode(self):
        """行政区划编码
        :rtype: str
        """
        return self._AdministrationCode

    @AdministrationCode.setter
    def AdministrationCode(self, AdministrationCode):
        self._AdministrationCode = AdministrationCode

    @property
    def AdministrationName(self):
        """行政区划名称
        :rtype: str
        """
        return self._AdministrationName

    @AdministrationName.setter
    def AdministrationName(self, AdministrationName):
        self._AdministrationName = AdministrationName


    def _deserialize(self, params):
        self._AdministrationCode = params.get("AdministrationCode")
        self._AdministrationName = params.get("AdministrationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdministrativeDetail(AbstractModel):
    """行政区划详情

    """

    def __init__(self):
        r"""
        :param _AdministrativeTypeCode: 行政区域类型编码
        :type AdministrativeTypeCode: str
        :param _AdministrativeCode: 行政区域编码
        :type AdministrativeCode: str
        :param _AdministrativeName: 行政区域名称
        :type AdministrativeName: str
        """
        self._AdministrativeTypeCode = None
        self._AdministrativeCode = None
        self._AdministrativeName = None

    @property
    def AdministrativeTypeCode(self):
        """行政区域类型编码
        :rtype: str
        """
        return self._AdministrativeTypeCode

    @AdministrativeTypeCode.setter
    def AdministrativeTypeCode(self, AdministrativeTypeCode):
        self._AdministrativeTypeCode = AdministrativeTypeCode

    @property
    def AdministrativeCode(self):
        """行政区域编码
        :rtype: str
        """
        return self._AdministrativeCode

    @AdministrativeCode.setter
    def AdministrativeCode(self, AdministrativeCode):
        self._AdministrativeCode = AdministrativeCode

    @property
    def AdministrativeName(self):
        """行政区域名称
        :rtype: str
        """
        return self._AdministrativeName

    @AdministrativeName.setter
    def AdministrativeName(self, AdministrativeName):
        self._AdministrativeName = AdministrativeName


    def _deserialize(self, params):
        self._AdministrativeTypeCode = params.get("AdministrativeTypeCode")
        self._AdministrativeCode = params.get("AdministrativeCode")
        self._AdministrativeName = params.get("AdministrativeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmInfo(AbstractModel):
    """告警信息

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _Id: 告警ID
        :type Id: str
        :param _Status: 告警状态
        :type Status: str
        :param _Time: 告警时间
        :type Time: int
        :param _Type: 告警业务类型
        :type Type: str
        :param _TypeName: 告警业务类型名称
        :type TypeName: str
        :param _SubType: 子告警类型
        :type SubType: str
        :param _SubTypeName: 子告警类型名称
        :type SubTypeName: str
        :param _Level: 告警级别id
        :type Level: int
        :param _LevelName: 告警级别名称
        :type LevelName: str
        :param _AppId: 上报应用appid
        :type AppId: int
        :param _WID: 设备wid
        :type WID: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Position: 空间位置
        :type Position: str
        :param _ReportImg: 上报图片
        :type ReportImg: :class:`tencentcloud.weilingwith.v20230427.models.ReportImg`
        :param _Desc: 告警描述
        :type Desc: str
        :param _HandlePersonSet: 处理人
        :type HandlePersonSet: list of HandlerPersonInfo
        :param _HandleRecordSet: 处理记录
        :type HandleRecordSet: list of HandleRecordInfo
        :param _Extend: 扩展信息
        :type Extend: str
        :param _ExtendOne: 应用扩展字段1
        :type ExtendOne: str
        :param _ExtendTwo: 应用扩展字段2
        :type ExtendTwo: str
        :param _Echo: 应用透传字段,有效字段为x-json后的字段
        :type Echo: str
        """
        self._WorkspaceId = None
        self._Id = None
        self._Status = None
        self._Time = None
        self._Type = None
        self._TypeName = None
        self._SubType = None
        self._SubTypeName = None
        self._Level = None
        self._LevelName = None
        self._AppId = None
        self._WID = None
        self._DeviceName = None
        self._Position = None
        self._ReportImg = None
        self._Desc = None
        self._HandlePersonSet = None
        self._HandleRecordSet = None
        self._Extend = None
        self._ExtendOne = None
        self._ExtendTwo = None
        self._Echo = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Id(self):
        """告警ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        """告警状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Time(self):
        """告警时间
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Type(self):
        """告警业务类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TypeName(self):
        """告警业务类型名称
        :rtype: str
        """
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def SubType(self):
        """子告警类型
        :rtype: str
        """
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def SubTypeName(self):
        """子告警类型名称
        :rtype: str
        """
        return self._SubTypeName

    @SubTypeName.setter
    def SubTypeName(self, SubTypeName):
        self._SubTypeName = SubTypeName

    @property
    def Level(self):
        """告警级别id
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def LevelName(self):
        """告警级别名称
        :rtype: str
        """
        return self._LevelName

    @LevelName.setter
    def LevelName(self, LevelName):
        self._LevelName = LevelName

    @property
    def AppId(self):
        """上报应用appid
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def WID(self):
        """设备wid
        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID

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
    def Position(self):
        """空间位置
        :rtype: str
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def ReportImg(self):
        """上报图片
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ReportImg`
        """
        return self._ReportImg

    @ReportImg.setter
    def ReportImg(self, ReportImg):
        self._ReportImg = ReportImg

    @property
    def Desc(self):
        """告警描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def HandlePersonSet(self):
        """处理人
        :rtype: list of HandlerPersonInfo
        """
        return self._HandlePersonSet

    @HandlePersonSet.setter
    def HandlePersonSet(self, HandlePersonSet):
        self._HandlePersonSet = HandlePersonSet

    @property
    def HandleRecordSet(self):
        """处理记录
        :rtype: list of HandleRecordInfo
        """
        return self._HandleRecordSet

    @HandleRecordSet.setter
    def HandleRecordSet(self, HandleRecordSet):
        self._HandleRecordSet = HandleRecordSet

    @property
    def Extend(self):
        """扩展信息
        :rtype: str
        """
        return self._Extend

    @Extend.setter
    def Extend(self, Extend):
        self._Extend = Extend

    @property
    def ExtendOne(self):
        """应用扩展字段1
        :rtype: str
        """
        return self._ExtendOne

    @ExtendOne.setter
    def ExtendOne(self, ExtendOne):
        self._ExtendOne = ExtendOne

    @property
    def ExtendTwo(self):
        """应用扩展字段2
        :rtype: str
        """
        return self._ExtendTwo

    @ExtendTwo.setter
    def ExtendTwo(self, ExtendTwo):
        self._ExtendTwo = ExtendTwo

    @property
    def Echo(self):
        """应用透传字段,有效字段为x-json后的字段
        :rtype: str
        """
        return self._Echo

    @Echo.setter
    def Echo(self, Echo):
        self._Echo = Echo


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        self._Time = params.get("Time")
        self._Type = params.get("Type")
        self._TypeName = params.get("TypeName")
        self._SubType = params.get("SubType")
        self._SubTypeName = params.get("SubTypeName")
        self._Level = params.get("Level")
        self._LevelName = params.get("LevelName")
        self._AppId = params.get("AppId")
        self._WID = params.get("WID")
        self._DeviceName = params.get("DeviceName")
        self._Position = params.get("Position")
        if params.get("ReportImg") is not None:
            self._ReportImg = ReportImg()
            self._ReportImg._deserialize(params.get("ReportImg"))
        self._Desc = params.get("Desc")
        if params.get("HandlePersonSet") is not None:
            self._HandlePersonSet = []
            for item in params.get("HandlePersonSet"):
                obj = HandlerPersonInfo()
                obj._deserialize(item)
                self._HandlePersonSet.append(obj)
        if params.get("HandleRecordSet") is not None:
            self._HandleRecordSet = []
            for item in params.get("HandleRecordSet"):
                obj = HandleRecordInfo()
                obj._deserialize(item)
                self._HandleRecordSet.append(obj)
        self._Extend = params.get("Extend")
        self._ExtendOne = params.get("ExtendOne")
        self._ExtendTwo = params.get("ExtendTwo")
        self._Echo = params.get("Echo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmLevelInfo(AbstractModel):
    """告警级别详情

    """

    def __init__(self):
        r"""
        :param _LevelId: 级别id
        :type LevelId: int
        :param _LevelName: 级别名称
        :type LevelName: str
        """
        self._LevelId = None
        self._LevelName = None

    @property
    def LevelId(self):
        """级别id
        :rtype: int
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId

    @property
    def LevelName(self):
        """级别名称
        :rtype: str
        """
        return self._LevelName

    @LevelName.setter
    def LevelName(self, LevelName):
        self._LevelName = LevelName


    def _deserialize(self, params):
        self._LevelId = params.get("LevelId")
        self._LevelName = params.get("LevelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmStatusData(AbstractModel):
    """告警状态返回结构体

    """

    def __init__(self):
        r"""
        :param _StatusID: 告警状态ID
        :type StatusID: str
        :param _StatusName: 告警状态名称
        :type StatusName: str
        :param _StatusType: 告警状态类型
        :type StatusType: str
        """
        self._StatusID = None
        self._StatusName = None
        self._StatusType = None

    @property
    def StatusID(self):
        """告警状态ID
        :rtype: str
        """
        return self._StatusID

    @StatusID.setter
    def StatusID(self, StatusID):
        self._StatusID = StatusID

    @property
    def StatusName(self):
        """告警状态名称
        :rtype: str
        """
        return self._StatusName

    @StatusName.setter
    def StatusName(self, StatusName):
        self._StatusName = StatusName

    @property
    def StatusType(self):
        """告警状态类型
        :rtype: str
        """
        return self._StatusType

    @StatusType.setter
    def StatusType(self, StatusType):
        self._StatusType = StatusType


    def _deserialize(self, params):
        self._StatusID = params.get("StatusID")
        self._StatusName = params.get("StatusName")
        self._StatusType = params.get("StatusType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmTypeDetailInfo(AbstractModel):
    """告警类型详情信息

    """

    def __init__(self):
        r"""
        :param _Id: 告警类型id
        :type Id: int
        :param _ParentId: 父节点id
        :type ParentId: int
        :param _Type: 0-标准告警类型，1-自定义告警类型
        :type Type: int
        :param _Name: 告警名称类型
        :type Name: str
        :param _EnglishName: 告警类型英文名称
        :type EnglishName: str
        """
        self._Id = None
        self._ParentId = None
        self._Type = None
        self._Name = None
        self._EnglishName = None

    @property
    def Id(self):
        """告警类型id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ParentId(self):
        """父节点id
        :rtype: int
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def Type(self):
        """0-标准告警类型，1-自定义告警类型
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        """告警名称类型
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EnglishName(self):
        """告警类型英文名称
        :rtype: str
        """
        return self._EnglishName

    @EnglishName.setter
    def EnglishName(self, EnglishName):
        self._EnglishName = EnglishName


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ParentId = params.get("ParentId")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._EnglishName = params.get("EnglishName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmTypeInfo(AbstractModel):
    """告警类型

    """

    def __init__(self):
        r"""
        :param _Type: 告警父类型
        :type Type: str
        :param _SubType: 告警子类型(如果传告警子类型，则必传父类型)
        :type SubType: str
        """
        self._Type = None
        self._SubType = None

    @property
    def Type(self):
        """告警父类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SubType(self):
        """告警子类型(如果传告警子类型，则必传父类型)
        :rtype: str
        """
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._SubType = params.get("SubType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiContent(AbstractModel):
    """API参数信息

    """

    def __init__(self):
        r"""
        :param _Id: 所属API的id
        :type Id: str
        :param _Name: 参数名称
        :type Name: str
        :param _Type: 参数类型
        :type Type: str
        :param _Dynamic: 是否为动态值
        :type Dynamic: bool
        :param _Required: 是否必填
        :type Required: bool
        :param _Value: 参数值
        :type Value: str
        :param _DefaultValue: 默认值
        :type DefaultValue: str
        """
        self._Id = None
        self._Name = None
        self._Type = None
        self._Dynamic = None
        self._Required = None
        self._Value = None
        self._DefaultValue = None

    @property
    def Id(self):
        """所属API的id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """参数名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """参数类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Dynamic(self):
        """是否为动态值
        :rtype: bool
        """
        return self._Dynamic

    @Dynamic.setter
    def Dynamic(self, Dynamic):
        self._Dynamic = Dynamic

    @property
    def Required(self):
        """是否必填
        :rtype: bool
        """
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required

    @property
    def Value(self):
        """参数值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def DefaultValue(self):
        """默认值
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Dynamic = params.get("Dynamic")
        self._Required = params.get("Required")
        self._Value = params.get("Value")
        self._DefaultValue = params.get("DefaultValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiInfo(AbstractModel):
    """API描述

    """

    def __init__(self):
        r"""
        :param _ApiId: API的id
        :type ApiId: str
        :param _Name: API名称
        :type Name: str
        :param _AppId: API所属应用的id
        :type AppId: str
        :param _WorkspaceId: API所属的项目空间的id
        :type WorkspaceId: str
        :param _PoiCode: API所属目录的编码
        :type PoiCode: str
        :param _Type:  接口分类0. 其他服务 1. IOT服务 2. 空间服务 3.微应用服务 4.场景服务 5.AI算法服务 6.任务算法服务 7.第三方服务
        :type Type: int
        :param _DataAudit: 数据授权 0:否 1:是
        :type DataAudit: int
        :param _ApplyAudit: 是否需要申请 0:否 1:是
        :type ApplyAudit: int
        :param _Description: API详情
        :type Description: str
        :param _Address: API地址
        :type Address: str
        :param _Method: 请求方法类型
        :type Method: str
        :param _Status: API状态
        :type Status: int
        :param _PreviewUrl: API预览地址
        :type PreviewUrl: str
        :param _QueryParams: query参数
        :type QueryParams: list of ApiContent
        :param _PathParams: 路径参数
        :type PathParams: list of ApiContent
        :param _RequestHeaders: 请求头
        :type RequestHeaders: list of ApiContent
        :param _ResponseHeaders: 响应头
        :type ResponseHeaders: list of ApiContent
        :param _IsCommonSpace: 是否为公共空间接口
        :type IsCommonSpace: bool
        :param _Body: 请求体（base64编码）
        :type Body: str
        :param _ResponseBody: 响应体（base64编码）
        :type ResponseBody: str
        :param _Style: 接口方式 1.http 2消息通知服务
        :type Style: int
        """
        self._ApiId = None
        self._Name = None
        self._AppId = None
        self._WorkspaceId = None
        self._PoiCode = None
        self._Type = None
        self._DataAudit = None
        self._ApplyAudit = None
        self._Description = None
        self._Address = None
        self._Method = None
        self._Status = None
        self._PreviewUrl = None
        self._QueryParams = None
        self._PathParams = None
        self._RequestHeaders = None
        self._ResponseHeaders = None
        self._IsCommonSpace = None
        self._Body = None
        self._ResponseBody = None
        self._Style = None

    @property
    def ApiId(self):
        """API的id
        :rtype: str
        """
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def Name(self):
        """API名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AppId(self):
        """API所属应用的id
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def WorkspaceId(self):
        """API所属的项目空间的id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def PoiCode(self):
        """API所属目录的编码
        :rtype: str
        """
        return self._PoiCode

    @PoiCode.setter
    def PoiCode(self, PoiCode):
        self._PoiCode = PoiCode

    @property
    def Type(self):
        """ 接口分类0. 其他服务 1. IOT服务 2. 空间服务 3.微应用服务 4.场景服务 5.AI算法服务 6.任务算法服务 7.第三方服务
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DataAudit(self):
        """数据授权 0:否 1:是
        :rtype: int
        """
        return self._DataAudit

    @DataAudit.setter
    def DataAudit(self, DataAudit):
        self._DataAudit = DataAudit

    @property
    def ApplyAudit(self):
        """是否需要申请 0:否 1:是
        :rtype: int
        """
        return self._ApplyAudit

    @ApplyAudit.setter
    def ApplyAudit(self, ApplyAudit):
        self._ApplyAudit = ApplyAudit

    @property
    def Description(self):
        """API详情
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Address(self):
        """API地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Method(self):
        """请求方法类型
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Status(self):
        """API状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PreviewUrl(self):
        """API预览地址
        :rtype: str
        """
        return self._PreviewUrl

    @PreviewUrl.setter
    def PreviewUrl(self, PreviewUrl):
        self._PreviewUrl = PreviewUrl

    @property
    def QueryParams(self):
        """query参数
        :rtype: list of ApiContent
        """
        return self._QueryParams

    @QueryParams.setter
    def QueryParams(self, QueryParams):
        self._QueryParams = QueryParams

    @property
    def PathParams(self):
        """路径参数
        :rtype: list of ApiContent
        """
        return self._PathParams

    @PathParams.setter
    def PathParams(self, PathParams):
        self._PathParams = PathParams

    @property
    def RequestHeaders(self):
        """请求头
        :rtype: list of ApiContent
        """
        return self._RequestHeaders

    @RequestHeaders.setter
    def RequestHeaders(self, RequestHeaders):
        self._RequestHeaders = RequestHeaders

    @property
    def ResponseHeaders(self):
        """响应头
        :rtype: list of ApiContent
        """
        return self._ResponseHeaders

    @ResponseHeaders.setter
    def ResponseHeaders(self, ResponseHeaders):
        self._ResponseHeaders = ResponseHeaders

    @property
    def IsCommonSpace(self):
        """是否为公共空间接口
        :rtype: bool
        """
        return self._IsCommonSpace

    @IsCommonSpace.setter
    def IsCommonSpace(self, IsCommonSpace):
        self._IsCommonSpace = IsCommonSpace

    @property
    def Body(self):
        """请求体（base64编码）
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def ResponseBody(self):
        """响应体（base64编码）
        :rtype: str
        """
        return self._ResponseBody

    @ResponseBody.setter
    def ResponseBody(self, ResponseBody):
        self._ResponseBody = ResponseBody

    @property
    def Style(self):
        """接口方式 1.http 2消息通知服务
        :rtype: int
        """
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style


    def _deserialize(self, params):
        self._ApiId = params.get("ApiId")
        self._Name = params.get("Name")
        self._AppId = params.get("AppId")
        self._WorkspaceId = params.get("WorkspaceId")
        self._PoiCode = params.get("PoiCode")
        self._Type = params.get("Type")
        self._DataAudit = params.get("DataAudit")
        self._ApplyAudit = params.get("ApplyAudit")
        self._Description = params.get("Description")
        self._Address = params.get("Address")
        self._Method = params.get("Method")
        self._Status = params.get("Status")
        self._PreviewUrl = params.get("PreviewUrl")
        if params.get("QueryParams") is not None:
            self._QueryParams = []
            for item in params.get("QueryParams"):
                obj = ApiContent()
                obj._deserialize(item)
                self._QueryParams.append(obj)
        if params.get("PathParams") is not None:
            self._PathParams = []
            for item in params.get("PathParams"):
                obj = ApiContent()
                obj._deserialize(item)
                self._PathParams.append(obj)
        if params.get("RequestHeaders") is not None:
            self._RequestHeaders = []
            for item in params.get("RequestHeaders"):
                obj = ApiContent()
                obj._deserialize(item)
                self._RequestHeaders.append(obj)
        if params.get("ResponseHeaders") is not None:
            self._ResponseHeaders = []
            for item in params.get("ResponseHeaders"):
                obj = ApiContent()
                obj._deserialize(item)
                self._ResponseHeaders.append(obj)
        self._IsCommonSpace = params.get("IsCommonSpace")
        self._Body = params.get("Body")
        self._ResponseBody = params.get("ResponseBody")
        self._Style = params.get("Style")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiInfoList(AbstractModel):
    """API列表

    """

    def __init__(self):
        r"""
        :param _ApiInfo: API列表
        :type ApiInfo: list of ApiInfo
        :param _TotalCount: 数据总条数
        :type TotalCount: int
        """
        self._ApiInfo = None
        self._TotalCount = None

    @property
    def ApiInfo(self):
        """API列表
        :rtype: list of ApiInfo
        """
        return self._ApiInfo

    @ApiInfo.setter
    def ApiInfo(self, ApiInfo):
        self._ApiInfo = ApiInfo

    @property
    def TotalCount(self):
        """数据总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("ApiInfo") is not None:
            self._ApiInfo = []
            for item in params.get("ApiInfo"):
                obj = ApiInfo()
                obj._deserialize(item)
                self._ApiInfo.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationInfo(AbstractModel):
    """应用描述

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用分配的appId
        :type ApplicationId: str
        :param _Name: 应用中文名
        :type Name: str
        :param _Address: 应用地址
        :type Address: str
        :param _ApplicationLogo: 应用logo
        :type ApplicationLogo: :class:`tencentcloud.weilingwith.v20230427.models.ApplicationLogo`
        :param _Type: 应用类型，0:saas应用 1:平台应用
        :type Type: int
        :param _EnglishName: engine
        :type EnglishName: str
        :param _Description: 能源管理应用
        :type Description: str
        """
        self._ApplicationId = None
        self._Name = None
        self._Address = None
        self._ApplicationLogo = None
        self._Type = None
        self._EnglishName = None
        self._Description = None

    @property
    def ApplicationId(self):
        """应用分配的appId
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def Name(self):
        """应用中文名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Address(self):
        """应用地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def ApplicationLogo(self):
        """应用logo
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ApplicationLogo`
        """
        return self._ApplicationLogo

    @ApplicationLogo.setter
    def ApplicationLogo(self, ApplicationLogo):
        self._ApplicationLogo = ApplicationLogo

    @property
    def Type(self):
        """应用类型，0:saas应用 1:平台应用
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EnglishName(self):
        """engine
        :rtype: str
        """
        return self._EnglishName

    @EnglishName.setter
    def EnglishName(self, EnglishName):
        self._EnglishName = EnglishName

    @property
    def Description(self):
        """能源管理应用
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._Name = params.get("Name")
        self._Address = params.get("Address")
        if params.get("ApplicationLogo") is not None:
            self._ApplicationLogo = ApplicationLogo()
            self._ApplicationLogo._deserialize(params.get("ApplicationLogo"))
        self._Type = params.get("Type")
        self._EnglishName = params.get("EnglishName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationList(AbstractModel):
    """应用列表

    """

    def __init__(self):
        r"""
        :param _ApplicationInfoList: 应用列表
        :type ApplicationInfoList: list of ApplicationInfo
        :param _TotalCount: 当前查询条件命中的数据总条数
        :type TotalCount: str
        """
        self._ApplicationInfoList = None
        self._TotalCount = None

    @property
    def ApplicationInfoList(self):
        """应用列表
        :rtype: list of ApplicationInfo
        """
        return self._ApplicationInfoList

    @ApplicationInfoList.setter
    def ApplicationInfoList(self, ApplicationInfoList):
        self._ApplicationInfoList = ApplicationInfoList

    @property
    def TotalCount(self):
        """当前查询条件命中的数据总条数
        :rtype: str
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("ApplicationInfoList") is not None:
            self._ApplicationInfoList = []
            for item in params.get("ApplicationInfoList"):
                obj = ApplicationInfo()
                obj._deserialize(item)
                self._ApplicationInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationLogo(AbstractModel):
    """应用logo

    """

    def __init__(self):
        r"""
        :param _FileId: logo图片对应的fileId
        :type FileId: str
        :param _Url: logo图片地址
        :type Url: str
        """
        self._FileId = None
        self._Url = None

    @property
    def FileId(self):
        """logo图片对应的fileId
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def Url(self):
        """logo图片地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._FileId = params.get("FileId")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationTokenInfo(AbstractModel):
    """应用Token令牌信息

    """

    def __init__(self):
        r"""
        :param _Token: 应用申请调用API的令牌
        :type Token: str
        """
        self._Token = None

    @property
    def Token(self):
        """应用申请调用API的令牌
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token


    def _deserialize(self, params):
        self._Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateDeviceRequest(AbstractModel):
    """BatchCreateDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间Id
        :type WorkspaceId: int
        :param _AddDeviceSet: 设备信息项

        :type AddDeviceSet: list of AddDeviceInfo
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._WorkspaceId = None
        self._AddDeviceSet = None
        self._ApplicationToken = None

    @property
    def WorkspaceId(self):
        """工作空间Id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def AddDeviceSet(self):
        """设备信息项

        :rtype: list of AddDeviceInfo
        """
        return self._AddDeviceSet

    @AddDeviceSet.setter
    def AddDeviceSet(self, AddDeviceSet):
        self._AddDeviceSet = AddDeviceSet

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        if params.get("AddDeviceSet") is not None:
            self._AddDeviceSet = []
            for item in params.get("AddDeviceSet"):
                obj = AddDeviceInfo()
                obj._deserialize(item)
                self._AddDeviceSet.append(obj)
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateDeviceRes(AbstractModel):
    """批量新增设备接口返回结果

    """

    def __init__(self):
        r"""
        :param _SuccessSet: 新增成功的设备列表
        :type SuccessSet: list of CreateDeviceSucceeded
        :param _FailSet: 新增失败的设备列表
        :type FailSet: list of CreateDeviceFailed
        """
        self._SuccessSet = None
        self._FailSet = None

    @property
    def SuccessSet(self):
        """新增成功的设备列表
        :rtype: list of CreateDeviceSucceeded
        """
        return self._SuccessSet

    @SuccessSet.setter
    def SuccessSet(self, SuccessSet):
        self._SuccessSet = SuccessSet

    @property
    def FailSet(self):
        """新增失败的设备列表
        :rtype: list of CreateDeviceFailed
        """
        return self._FailSet

    @FailSet.setter
    def FailSet(self, FailSet):
        self._FailSet = FailSet


    def _deserialize(self, params):
        if params.get("SuccessSet") is not None:
            self._SuccessSet = []
            for item in params.get("SuccessSet"):
                obj = CreateDeviceSucceeded()
                obj._deserialize(item)
                self._SuccessSet.append(obj)
        if params.get("FailSet") is not None:
            self._FailSet = []
            for item in params.get("FailSet"):
                obj = CreateDeviceFailed()
                obj._deserialize(item)
                self._FailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateDeviceResponse(AbstractModel):
    """BatchCreateDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 批量新增设备返回结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.BatchCreateDeviceRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """批量新增设备返回结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.BatchCreateDeviceRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = BatchCreateDeviceRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class BatchDeleteDeviceRequest(AbstractModel):
    """BatchDeleteDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _WIDSet: 设备wid数组列表
        :type WIDSet: list of str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._WorkspaceId = None
        self._WIDSet = None
        self._ApplicationToken = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WIDSet(self):
        """设备wid数组列表
        :rtype: list of str
        """
        return self._WIDSet

    @WIDSet.setter
    def WIDSet(self, WIDSet):
        self._WIDSet = WIDSet

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._WIDSet = params.get("WIDSet")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteDeviceResponse(AbstractModel):
    """BatchDeleteDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回请求结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回请求结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = EmptyRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class BatchKillAlarmRequest(AbstractModel):
    """BatchKillAlarm请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 告警开始时间，必填,时间戳秒
        :type BeginTime: int
        :param _EndTime: 告警结束时间，必填，时间戳秒
        :type EndTime: int
        :param _StatusSet: 告警状态: unprocessed processing

        :type StatusSet: list of str
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _UserId: 当前操作用户id
        :type UserId: str
        :param _UserName: 当前操作用户名称
        :type UserName: str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _ProcessorId: 当前告警处理人，填孪生中台用户id,多个用逗号分隔

        :type ProcessorId: str
        :param _AlarmTypeSet: 告警子类型(如果传告警子类型，则必传父类型)

        :type AlarmTypeSet: list of AlarmTypeInfo
        :param _LevelSet: 告警级别,包括1~5
        :type LevelSet: list of int
        :param _WIDSet: 设备id
        :type WIDSet: list of str
        :param _IdSet: 告警id
        :type IdSet: list of str
        :param _Desc: 告警处理的说明
        :type Desc: str
        """
        self._BeginTime = None
        self._EndTime = None
        self._StatusSet = None
        self._WorkspaceId = None
        self._UserId = None
        self._UserName = None
        self._ApplicationToken = None
        self._ProcessorId = None
        self._AlarmTypeSet = None
        self._LevelSet = None
        self._WIDSet = None
        self._IdSet = None
        self._Desc = None

    @property
    def BeginTime(self):
        """告警开始时间，必填,时间戳秒
        :rtype: int
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """告警结束时间，必填，时间戳秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StatusSet(self):
        """告警状态: unprocessed processing

        :rtype: list of str
        """
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def UserId(self):
        """当前操作用户id
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        """当前操作用户名称
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def ProcessorId(self):
        """当前告警处理人，填孪生中台用户id,多个用逗号分隔

        :rtype: str
        """
        return self._ProcessorId

    @ProcessorId.setter
    def ProcessorId(self, ProcessorId):
        self._ProcessorId = ProcessorId

    @property
    def AlarmTypeSet(self):
        """告警子类型(如果传告警子类型，则必传父类型)

        :rtype: list of AlarmTypeInfo
        """
        return self._AlarmTypeSet

    @AlarmTypeSet.setter
    def AlarmTypeSet(self, AlarmTypeSet):
        self._AlarmTypeSet = AlarmTypeSet

    @property
    def LevelSet(self):
        """告警级别,包括1~5
        :rtype: list of int
        """
        return self._LevelSet

    @LevelSet.setter
    def LevelSet(self, LevelSet):
        self._LevelSet = LevelSet

    @property
    def WIDSet(self):
        """设备id
        :rtype: list of str
        """
        return self._WIDSet

    @WIDSet.setter
    def WIDSet(self, WIDSet):
        self._WIDSet = WIDSet

    @property
    def IdSet(self):
        """告警id
        :rtype: list of str
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def Desc(self):
        """告警处理的说明
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._StatusSet = params.get("StatusSet")
        self._WorkspaceId = params.get("WorkspaceId")
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._ApplicationToken = params.get("ApplicationToken")
        self._ProcessorId = params.get("ProcessorId")
        if params.get("AlarmTypeSet") is not None:
            self._AlarmTypeSet = []
            for item in params.get("AlarmTypeSet"):
                obj = AlarmTypeInfo()
                obj._deserialize(item)
                self._AlarmTypeSet.append(obj)
        self._LevelSet = params.get("LevelSet")
        self._WIDSet = params.get("WIDSet")
        self._IdSet = params.get("IdSet")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchKillAlarmResponse(AbstractModel):
    """BatchKillAlarm返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 批量消警结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """批量消警结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = EmptyRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class BatchReportAppMessageRequest(AbstractModel):
    """BatchReportAppMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间Id
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _ReportSet: 消息上报请求列表
        :type ReportSet: list of ReportAppMessage
        """
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._ReportSet = None

    @property
    def WorkspaceId(self):
        """工作空间Id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def ReportSet(self):
        """消息上报请求列表
        :rtype: list of ReportAppMessage
        """
        return self._ReportSet

    @ReportSet.setter
    def ReportSet(self, ReportSet):
        self._ReportSet = ReportSet


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        if params.get("ReportSet") is not None:
            self._ReportSet = []
            for item in params.get("ReportSet"):
                obj = ReportAppMessage()
                obj._deserialize(item)
                self._ReportSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchReportAppMessageRes(AbstractModel):
    """批量消息上报结果

    """

    def __init__(self):
        r"""
        :param _TotalElements: 上报数量

        :type TotalElements: int
        :param _Commit: 提交数量（推送成功）
        :type Commit: int
        :param _SpanMap: 消息推送结果列表
        :type SpanMap: list of ReportMsgRes
        """
        self._TotalElements = None
        self._Commit = None
        self._SpanMap = None

    @property
    def TotalElements(self):
        """上报数量

        :rtype: int
        """
        return self._TotalElements

    @TotalElements.setter
    def TotalElements(self, TotalElements):
        self._TotalElements = TotalElements

    @property
    def Commit(self):
        """提交数量（推送成功）
        :rtype: int
        """
        return self._Commit

    @Commit.setter
    def Commit(self, Commit):
        self._Commit = Commit

    @property
    def SpanMap(self):
        """消息推送结果列表
        :rtype: list of ReportMsgRes
        """
        return self._SpanMap

    @SpanMap.setter
    def SpanMap(self, SpanMap):
        self._SpanMap = SpanMap


    def _deserialize(self, params):
        self._TotalElements = params.get("TotalElements")
        self._Commit = params.get("Commit")
        if params.get("SpanMap") is not None:
            self._SpanMap = []
            for item in params.get("SpanMap"):
                obj = ReportMsgRes()
                obj._deserialize(item)
                self._SpanMap.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchReportAppMessageResponse(AbstractModel):
    """BatchReportAppMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 批量消息上报结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.BatchReportAppMessageRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """批量消息上报结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.BatchReportAppMessageRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = BatchReportAppMessageRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class BuildingListRes(AbstractModel):
    """建筑列表响应体

    """

    def __init__(self):
        r"""
        :param _BuildingProfileList: 建筑列表
        :type BuildingProfileList: list of BuildingProfile
        """
        self._BuildingProfileList = None

    @property
    def BuildingProfileList(self):
        """建筑列表
        :rtype: list of BuildingProfile
        """
        return self._BuildingProfileList

    @BuildingProfileList.setter
    def BuildingProfileList(self, BuildingProfileList):
        self._BuildingProfileList = BuildingProfileList


    def _deserialize(self, params):
        if params.get("BuildingProfileList") is not None:
            self._BuildingProfileList = []
            for item in params.get("BuildingProfileList"):
                obj = BuildingProfile()
                obj._deserialize(item)
                self._BuildingProfileList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BuildingModel(AbstractModel):
    """建筑模型信息

    """

    def __init__(self):
        r"""
        :param _ElementId: 构件ID
        :type ElementId: str
        :param _ElementName: 构件名称
        :type ElementName: str
        :param _ModelType: 模型类型
        :type ModelType: str
        :param _ModelUrl: 模型URL
        :type ModelUrl: str
        """
        self._ElementId = None
        self._ElementName = None
        self._ModelType = None
        self._ModelUrl = None

    @property
    def ElementId(self):
        """构件ID
        :rtype: str
        """
        return self._ElementId

    @ElementId.setter
    def ElementId(self, ElementId):
        self._ElementId = ElementId

    @property
    def ElementName(self):
        """构件名称
        :rtype: str
        """
        return self._ElementName

    @ElementName.setter
    def ElementName(self, ElementName):
        self._ElementName = ElementName

    @property
    def ModelType(self):
        """模型类型
        :rtype: str
        """
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType

    @property
    def ModelUrl(self):
        """模型URL
        :rtype: str
        """
        return self._ModelUrl

    @ModelUrl.setter
    def ModelUrl(self, ModelUrl):
        self._ModelUrl = ModelUrl


    def _deserialize(self, params):
        self._ElementId = params.get("ElementId")
        self._ElementName = params.get("ElementName")
        self._ModelType = params.get("ModelType")
        self._ModelUrl = params.get("ModelUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BuildingModelRes(AbstractModel):
    """建模模型信息响应体

    """

    def __init__(self):
        r"""
        :param _Models: 建模模型信息出参
        :type Models: list of BuildingModel
        """
        self._Models = None

    @property
    def Models(self):
        """建模模型信息出参
        :rtype: list of BuildingModel
        """
        return self._Models

    @Models.setter
    def Models(self, Models):
        self._Models = Models


    def _deserialize(self, params):
        if params.get("Models") is not None:
            self._Models = []
            for item in params.get("Models"):
                obj = BuildingModel()
                obj._deserialize(item)
                self._Models.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BuildingProfile(AbstractModel):
    """建筑概要信息

    """

    def __init__(self):
        r"""
        :param _BuildingId: 建筑id
        :type BuildingId: str
        :param _BuildingName: 建筑名称
        :type BuildingName: str
        :param _SpaceCode: 空间编码
        :type SpaceCode: str
        :param _Longitude: 经度
        :type Longitude: float
        :param _Latitude: 纬度
        :type Latitude: float
        :param _Address: 地址
        :type Address: str
        """
        self._BuildingId = None
        self._BuildingName = None
        self._SpaceCode = None
        self._Longitude = None
        self._Latitude = None
        self._Address = None

    @property
    def BuildingId(self):
        """建筑id
        :rtype: str
        """
        return self._BuildingId

    @BuildingId.setter
    def BuildingId(self, BuildingId):
        self._BuildingId = BuildingId

    @property
    def BuildingName(self):
        """建筑名称
        :rtype: str
        """
        return self._BuildingName

    @BuildingName.setter
    def BuildingName(self, BuildingName):
        self._BuildingName = BuildingName

    @property
    def SpaceCode(self):
        """空间编码
        :rtype: str
        """
        return self._SpaceCode

    @SpaceCode.setter
    def SpaceCode(self, SpaceCode):
        self._SpaceCode = SpaceCode

    @property
    def Longitude(self):
        """经度
        :rtype: float
        """
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Latitude(self):
        """纬度
        :rtype: float
        """
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude

    @property
    def Address(self):
        """地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address


    def _deserialize(self, params):
        self._BuildingId = params.get("BuildingId")
        self._BuildingName = params.get("BuildingName")
        self._SpaceCode = params.get("SpaceCode")
        self._Longitude = params.get("Longitude")
        self._Latitude = params.get("Latitude")
        self._Address = params.get("Address")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BuildingProfileRes(AbstractModel):
    """查询建筑信息响应体

    """

    def __init__(self):
        r"""
        :param _BuildingProfile: 建筑概要信息
        :type BuildingProfile: :class:`tencentcloud.weilingwith.v20230427.models.BuildingProfile`
        """
        self._BuildingProfile = None

    @property
    def BuildingProfile(self):
        """建筑概要信息
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.BuildingProfile`
        """
        return self._BuildingProfile

    @BuildingProfile.setter
    def BuildingProfile(self, BuildingProfile):
        self._BuildingProfile = BuildingProfile


    def _deserialize(self, params):
        if params.get("BuildingProfile") is not None:
            self._BuildingProfile = BuildingProfile()
            self._BuildingProfile._deserialize(params.get("BuildingProfile"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CameraExtendInfoRes(AbstractModel):
    """视频扩展信息结果

    """

    def __init__(self):
        r"""
        :param _SaveType: 存储方式 (nvr或cosmtav)
        :type SaveType: str
        :param _SaveDay: 云存储天数（save_type是cosmtav时这个参数才有效）

        :type SaveDay: int
        :param _LiveResolution: 实时分辨率
        :type LiveResolution: int
        :param _HistoryResolution: 历史分辨率
        :type HistoryResolution: int
        """
        self._SaveType = None
        self._SaveDay = None
        self._LiveResolution = None
        self._HistoryResolution = None

    @property
    def SaveType(self):
        """存储方式 (nvr或cosmtav)
        :rtype: str
        """
        return self._SaveType

    @SaveType.setter
    def SaveType(self, SaveType):
        self._SaveType = SaveType

    @property
    def SaveDay(self):
        """云存储天数（save_type是cosmtav时这个参数才有效）

        :rtype: int
        """
        return self._SaveDay

    @SaveDay.setter
    def SaveDay(self, SaveDay):
        self._SaveDay = SaveDay

    @property
    def LiveResolution(self):
        """实时分辨率
        :rtype: int
        """
        return self._LiveResolution

    @LiveResolution.setter
    def LiveResolution(self, LiveResolution):
        self._LiveResolution = LiveResolution

    @property
    def HistoryResolution(self):
        """历史分辨率
        :rtype: int
        """
        return self._HistoryResolution

    @HistoryResolution.setter
    def HistoryResolution(self, HistoryResolution):
        self._HistoryResolution = HistoryResolution


    def _deserialize(self, params):
        self._SaveType = params.get("SaveType")
        self._SaveDay = params.get("SaveDay")
        self._LiveResolution = params.get("LiveResolution")
        self._HistoryResolution = params.get("HistoryResolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeAlarmStatusRequest(AbstractModel):
    """ChangeAlarmStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 告警的id，返回的列表中的id
        :type Id: str
        :param _Status: 告警状态 processed unprocessed processing misreport shield
        :type Status: str
        :param _ProcessTime: 告警处理时间
        :type ProcessTime: int
        :param _ProcessType: 处理类型
        :type ProcessType: str
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _UserId: 当前操作用户id
        :type UserId: str
        :param _UserName: 当前操作用户名称
        :type UserName: str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _Processor: 平台告警处理人
        :type Processor: str
        :param _ProcessDescription: 告警处理的描述信息
        :type ProcessDescription: str
        :param _ProcessExtend: 告警处理的扩展信息，可以为JSON字符串
        :type ProcessExtend: str
        :param _ExtendOne: 扩展字段1，目前存的应用告警处理人
        :type ExtendOne: str
        :param _ApplicationId: 应用id
        :type ApplicationId: int
        """
        self._Id = None
        self._Status = None
        self._ProcessTime = None
        self._ProcessType = None
        self._WorkspaceId = None
        self._UserId = None
        self._UserName = None
        self._ApplicationToken = None
        self._Processor = None
        self._ProcessDescription = None
        self._ProcessExtend = None
        self._ExtendOne = None
        self._ApplicationId = None

    @property
    def Id(self):
        """告警的id，返回的列表中的id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        """告警状态 processed unprocessed processing misreport shield
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProcessTime(self):
        """告警处理时间
        :rtype: int
        """
        return self._ProcessTime

    @ProcessTime.setter
    def ProcessTime(self, ProcessTime):
        self._ProcessTime = ProcessTime

    @property
    def ProcessType(self):
        """处理类型
        :rtype: str
        """
        return self._ProcessType

    @ProcessType.setter
    def ProcessType(self, ProcessType):
        self._ProcessType = ProcessType

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def UserId(self):
        """当前操作用户id
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        """当前操作用户名称
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def Processor(self):
        """平台告警处理人
        :rtype: str
        """
        return self._Processor

    @Processor.setter
    def Processor(self, Processor):
        self._Processor = Processor

    @property
    def ProcessDescription(self):
        """告警处理的描述信息
        :rtype: str
        """
        return self._ProcessDescription

    @ProcessDescription.setter
    def ProcessDescription(self, ProcessDescription):
        self._ProcessDescription = ProcessDescription

    @property
    def ProcessExtend(self):
        """告警处理的扩展信息，可以为JSON字符串
        :rtype: str
        """
        return self._ProcessExtend

    @ProcessExtend.setter
    def ProcessExtend(self, ProcessExtend):
        self._ProcessExtend = ProcessExtend

    @property
    def ExtendOne(self):
        """扩展字段1，目前存的应用告警处理人
        :rtype: str
        """
        return self._ExtendOne

    @ExtendOne.setter
    def ExtendOne(self, ExtendOne):
        self._ExtendOne = ExtendOne

    @property
    def ApplicationId(self):
        """应用id
        :rtype: int
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        self._ProcessTime = params.get("ProcessTime")
        self._ProcessType = params.get("ProcessType")
        self._WorkspaceId = params.get("WorkspaceId")
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._ApplicationToken = params.get("ApplicationToken")
        self._Processor = params.get("Processor")
        self._ProcessDescription = params.get("ProcessDescription")
        self._ProcessExtend = params.get("ProcessExtend")
        self._ExtendOne = params.get("ExtendOne")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeAlarmStatusResponse(AbstractModel):
    """ChangeAlarmStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回空结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回空结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = EmptyRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ControlCameraPTZRequest(AbstractModel):
    """ControlCameraPTZ请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WID: 设备的唯一标识
        :type WID: str
        :param _CMD: ptz指令
left - 向左移动
right - 向右移动
up - 向上移动
down - 向下
zoomOut - 镜头缩小
zoomIn - 镜头放大
irisIn - 光圈缩小
irisOut - 光圈放大
focusIn - 焦距变近
focusOut - 焦距变远

        :type CMD: str
        :param _WorkspaceId: 工作空间Id
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._WID = None
        self._CMD = None
        self._WorkspaceId = None
        self._ApplicationToken = None

    @property
    def WID(self):
        """设备的唯一标识
        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID

    @property
    def CMD(self):
        """ptz指令
left - 向左移动
right - 向右移动
up - 向上移动
down - 向下
zoomOut - 镜头缩小
zoomIn - 镜头放大
irisIn - 光圈缩小
irisOut - 光圈放大
focusIn - 焦距变近
focusOut - 焦距变远

        :rtype: str
        """
        return self._CMD

    @CMD.setter
    def CMD(self, CMD):
        self._CMD = CMD

    @property
    def WorkspaceId(self):
        """工作空间Id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._WID = params.get("WID")
        self._CMD = params.get("CMD")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlCameraPTZResponse(AbstractModel):
    """ControlCameraPTZ返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 控制摄像头结果返回
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """控制摄像头结果返回
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = EmptyRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ControlDeviceRequest(AbstractModel):
    """ControlDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _WIDSet: 设备wid，最大100个
        :type WIDSet: list of str
        :param _ControlData: 控制内容
        :type ControlData: str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _IsSynchronized: 是否同步返回设备下控ack结果
        :type IsSynchronized: bool
        """
        self._WorkspaceId = None
        self._WIDSet = None
        self._ControlData = None
        self._ApplicationToken = None
        self._IsSynchronized = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WIDSet(self):
        """设备wid，最大100个
        :rtype: list of str
        """
        return self._WIDSet

    @WIDSet.setter
    def WIDSet(self, WIDSet):
        self._WIDSet = WIDSet

    @property
    def ControlData(self):
        """控制内容
        :rtype: str
        """
        return self._ControlData

    @ControlData.setter
    def ControlData(self, ControlData):
        self._ControlData = ControlData

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def IsSynchronized(self):
        """是否同步返回设备下控ack结果
        :rtype: bool
        """
        return self._IsSynchronized

    @IsSynchronized.setter
    def IsSynchronized(self, IsSynchronized):
        self._IsSynchronized = IsSynchronized


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._WIDSet = params.get("WIDSet")
        self._ControlData = params.get("ControlData")
        self._ApplicationToken = params.get("ApplicationToken")
        self._IsSynchronized = params.get("IsSynchronized")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDeviceRes(AbstractModel):
    """设备控制结果

    """

    def __init__(self):
        r"""
        :param _WID: 设备Id
        :type WID: str
        :param _Code: 指令接受, 0表示成功
        :type Code: int
        :param _Result: 控制结果
        :type Result: str
        :param _Seq: 批量大于1时，可用此seq进行链路追踪
        :type Seq: str
        """
        self._WID = None
        self._Code = None
        self._Result = None
        self._Seq = None

    @property
    def WID(self):
        """设备Id
        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID

    @property
    def Code(self):
        """指令接受, 0表示成功
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Result(self):
        """控制结果
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Seq(self):
        """批量大于1时，可用此seq进行链路追踪
        :rtype: str
        """
        return self._Seq

    @Seq.setter
    def Seq(self, Seq):
        self._Seq = Seq


    def _deserialize(self, params):
        self._WID = params.get("WID")
        self._Code = params.get("Code")
        self._Result = params.get("Result")
        self._Seq = params.get("Seq")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDeviceResponse(AbstractModel):
    """ControlDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 设备控制后结果集
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.ControlDeviceSet`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """设备控制后结果集
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ControlDeviceSet`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ControlDeviceSet()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ControlDeviceSet(AbstractModel):
    """设备控制后返回结果集合

    """

    def __init__(self):
        r"""
        :param _Set: 设备控制后返回结果集合
        :type Set: list of ControlDeviceRes
        """
        self._Set = None

    @property
    def Set(self):
        """设备控制后返回结果集合
        :rtype: list of ControlDeviceRes
        """
        return self._Set

    @Set.setter
    def Set(self, Set):
        self._Set = Set


    def _deserialize(self, params):
        if params.get("Set") is not None:
            self._Set = []
            for item in params.get("Set"):
                obj = ControlDeviceRes()
                obj._deserialize(item)
                self._Set.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationTokenRequest(AbstractModel):
    """CreateApplicationToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用id
        :type ApplicationId: int
        :param _Nonce: 一个随机数或者时间戳，用于防止重放攻击，每个请求唯一，建议用uuid
        :type Nonce: str
        :param _TenantId: 租户id
        :type TenantId: int
        :param _RequestTime: 请求时间，当前时间的unix毫秒时间戳
        :type RequestTime: int
        :param _Signature: 签名方法见用户使用文档
        :type Signature: str
        """
        self._ApplicationId = None
        self._Nonce = None
        self._TenantId = None
        self._RequestTime = None
        self._Signature = None

    @property
    def ApplicationId(self):
        """应用id
        :rtype: int
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def Nonce(self):
        """一个随机数或者时间戳，用于防止重放攻击，每个请求唯一，建议用uuid
        :rtype: str
        """
        return self._Nonce

    @Nonce.setter
    def Nonce(self, Nonce):
        self._Nonce = Nonce

    @property
    def TenantId(self):
        """租户id
        :rtype: int
        """
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def RequestTime(self):
        """请求时间，当前时间的unix毫秒时间戳
        :rtype: int
        """
        return self._RequestTime

    @RequestTime.setter
    def RequestTime(self, RequestTime):
        self._RequestTime = RequestTime

    @property
    def Signature(self):
        """签名方法见用户使用文档
        :rtype: str
        """
        return self._Signature

    @Signature.setter
    def Signature(self, Signature):
        self._Signature = Signature


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._Nonce = params.get("Nonce")
        self._TenantId = params.get("TenantId")
        self._RequestTime = params.get("RequestTime")
        self._Signature = params.get("Signature")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationTokenResponse(AbstractModel):
    """CreateApplicationToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 应用令牌信息
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.ApplicationTokenInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """应用令牌信息
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ApplicationTokenInfo`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ApplicationTokenInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateDeviceFailed(AbstractModel):
    """导入失败设备信息

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品id
        :type ProductId: int
        :param _ParentWID: 父设备wid，不为空表示导入自设备
        :type ParentWID: str
        :param _Reason: 失败原因
        :type Reason: str
        :param _SN: 设备sn序列号
        :type SN: str
        """
        self._ProductId = None
        self._ParentWID = None
        self._Reason = None
        self._SN = None

    @property
    def ProductId(self):
        """产品id
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ParentWID(self):
        """父设备wid，不为空表示导入自设备
        :rtype: str
        """
        return self._ParentWID

    @ParentWID.setter
    def ParentWID(self, ParentWID):
        self._ParentWID = ParentWID

    @property
    def Reason(self):
        """失败原因
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def SN(self):
        """设备sn序列号
        :rtype: str
        """
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ParentWID = params.get("ParentWID")
        self._Reason = params.get("Reason")
        self._SN = params.get("SN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceSucceeded(AbstractModel):
    """导入成功设备信息

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品id
        :type ProductId: int
        :param _ParentWID: 父设备wid，不为空表示导入自设备
        :type ParentWID: str
        :param _WID: 设备编码
        :type WID: str
        :param _SN: 设备sn序列号
        :type SN: str
        """
        self._ProductId = None
        self._ParentWID = None
        self._WID = None
        self._SN = None

    @property
    def ProductId(self):
        """产品id
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ParentWID(self):
        """父设备wid，不为空表示导入自设备
        :rtype: str
        """
        return self._ParentWID

    @ParentWID.setter
    def ParentWID(self, ParentWID):
        self._ParentWID = ParentWID

    @property
    def WID(self):
        """设备编码
        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID

    @property
    def SN(self):
        """设备sn序列号
        :rtype: str
        """
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ParentWID = params.get("ParentWID")
        self._WID = params.get("WID")
        self._SN = params.get("SN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomField(AbstractModel):
    """自定义字段

    """

    def __init__(self):
        r"""
        :param _Id: 字段id
        :type Id: int
        :param _Val: 字段内容
        :type Val: str
        """
        self._Id = None
        self._Val = None

    @property
    def Id(self):
        """字段id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Val(self):
        """字段内容
        :rtype: str
        """
        return self._Val

    @Val.setter
    def Val(self, Val):
        self._Val = Val


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Val = params.get("Val")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomFieldInfo(AbstractModel):
    """自定义字段

    """

    def __init__(self):
        r"""
        :param _Id: 字段id
        :type Id: int
        :param _Key: 字段key
        :type Key: str
        :param _Name: 字段名
        :type Name: str
        :param _Val: 字段值
        :type Val: str
        """
        self._Id = None
        self._Key = None
        self._Name = None
        self._Val = None

    @property
    def Id(self):
        """字段id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Key(self):
        """字段key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Name(self):
        """字段名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Val(self):
        """字段值
        :rtype: str
        """
        return self._Val

    @Val.setter
    def Val(self, Val):
        self._Val = Val


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Key = params.get("Key")
        self._Name = params.get("Name")
        self._Val = params.get("Val")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceGroupRequest(AbstractModel):
    """DeleteDeviceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 设备分组的id
        :type Id: int
        :param _WorkspaceId: 工作空间的id
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._Id = None
        self._WorkspaceId = None
        self._ApplicationToken = None

    @property
    def Id(self):
        """设备分组的id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def WorkspaceId(self):
        """工作空间的id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
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
        :param _Result: 无返回信息
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """无返回信息
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = EmptyRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeActionListRequest(AbstractModel):
    """DescribeActionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _PageNumber: 分页查询，第几页，必传，大于0
        :type PageNumber: int
        :param _PageSize: 每页条数，必传大于0
        :type PageSize: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _ActionType: 动作类型，（app,device,toAlarm,toNotification）
        :type ActionType: str
        :param _IdSet: 事件id详情
        :type IdSet: list of int
        """
        self._WorkspaceId = None
        self._PageNumber = None
        self._PageSize = None
        self._ApplicationToken = None
        self._ActionType = None
        self._IdSet = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def PageNumber(self):
        """分页查询，第几页，必传，大于0
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数，必传大于0
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def ActionType(self):
        """动作类型，（app,device,toAlarm,toNotification）
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def IdSet(self):
        """事件id详情
        :rtype: list of int
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._ApplicationToken = params.get("ApplicationToken")
        self._ActionType = params.get("ActionType")
        self._IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeActionListRes(AbstractModel):
    """动作列表查询结果

    """

    def __init__(self):
        r"""
        :param _PageNumber: 第几页
        :type PageNumber: int
        :param _PageSize: 每页条数
        :type PageSize: int
        :param _TotalPage: 总页数
        :type TotalPage: int
        :param _TotalRow: 总条数
        :type TotalRow: int
        :param _ActionDetailSet: 动作列表查询集合
        :type ActionDetailSet: list of ActionDetail
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalPage = None
        self._TotalRow = None
        self._ActionDetailSet = None

    @property
    def PageNumber(self):
        """第几页
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalPage(self):
        """总页数
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def TotalRow(self):
        """总条数
        :rtype: int
        """
        return self._TotalRow

    @TotalRow.setter
    def TotalRow(self, TotalRow):
        self._TotalRow = TotalRow

    @property
    def ActionDetailSet(self):
        """动作列表查询集合
        :rtype: list of ActionDetail
        """
        return self._ActionDetailSet

    @ActionDetailSet.setter
    def ActionDetailSet(self, ActionDetailSet):
        self._ActionDetailSet = ActionDetailSet


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalPage = params.get("TotalPage")
        self._TotalRow = params.get("TotalRow")
        if params.get("ActionDetailSet") is not None:
            self._ActionDetailSet = []
            for item in params.get("ActionDetailSet"):
                obj = ActionDetail()
                obj._deserialize(item)
                self._ActionDetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeActionListResponse(AbstractModel):
    """DescribeActionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 动作列表查询结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.DescribeActionListRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """动作列表查询结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeActionListRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeActionListRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeAdministrationByTagRequest(AbstractModel):
    """DescribeAdministrationByTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _WorkspaceId: 工作空间ID
        :type WorkspaceId: int
        :param _Tag: 标签值
        :type Tag: str
        """
        self._ApplicationToken = None
        self._WorkspaceId = None
        self._Tag = None

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def WorkspaceId(self):
        """工作空间ID
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Tag(self):
        """标签值
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._ApplicationToken = params.get("ApplicationToken")
        self._WorkspaceId = params.get("WorkspaceId")
        self._Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAdministrationByTagRes(AbstractModel):
    """根据Tag获取行政区划列表返回结构

    """

    def __init__(self):
        r"""
        :param _List: 行政区划列表
        :type List: list of AdministrationData
        """
        self._List = None

    @property
    def List(self):
        """行政区划列表
        :rtype: list of AdministrationData
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AdministrationData()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAdministrationByTagResponse(AbstractModel):
    """DescribeAdministrationByTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 行政区划返回结构
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAdministrationByTagRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """行政区划返回结构
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAdministrationByTagRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeAdministrationByTagRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeAlarmLevelListRequest(AbstractModel):
    """DescribeAlarmLevelList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._WorkspaceId = None
        self._ApplicationToken = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmLevelListRes(AbstractModel):
    """告警级别枚举获取

    """

    def __init__(self):
        r"""
        :param _AlarmLevelSet: 告警级别枚举获取数组
        :type AlarmLevelSet: list of AlarmLevelInfo
        """
        self._AlarmLevelSet = None

    @property
    def AlarmLevelSet(self):
        """告警级别枚举获取数组
        :rtype: list of AlarmLevelInfo
        """
        return self._AlarmLevelSet

    @AlarmLevelSet.setter
    def AlarmLevelSet(self, AlarmLevelSet):
        self._AlarmLevelSet = AlarmLevelSet


    def _deserialize(self, params):
        if params.get("AlarmLevelSet") is not None:
            self._AlarmLevelSet = []
            for item in params.get("AlarmLevelSet"):
                obj = AlarmLevelInfo()
                obj._deserialize(item)
                self._AlarmLevelSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmLevelListResponse(AbstractModel):
    """DescribeAlarmLevelList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 告警级别列表查询结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAlarmLevelListRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """告警级别列表查询结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAlarmLevelListRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeAlarmLevelListRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeAlarmListRequest(AbstractModel):
    """DescribeAlarmList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 告警开始时间，必填,时间戳秒
        :type BeginTime: int
        :param _EndTime: 告警结束时间，必填，时间戳秒
        :type EndTime: int
        :param _PageNumber: 分页查询，第几页
        :type PageNumber: int
        :param _PageSize: 每页条数
        :type PageSize: int
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _Statuses: 告警状态
        :type Statuses: list of str
        :param _AlarmTypeSet: 告警类型
        :type AlarmTypeSet: list of AlarmTypeInfo
        :param _LevelSet: 告警级别id
        :type LevelSet: list of int
        :param _IdSet: 告警id
        :type IdSet: list of str
        :param _AppIdSet: 应用id
        :type AppIdSet: list of int
        :param _WIDSet: 设备id
        :type WIDSet: list of str
        :param _SpaceCodeSet: 空间层级
        :type SpaceCodeSet: list of str
        :param _ExtendOne: 应用扩展字段1
        :type ExtendOne: list of str
        :param _ExtendTwo: 应用扩展字段2
        :type ExtendTwo: list of str
        :param _ProcessorSet: 当前告警处理人，填孪生中台的用户id
        :type ProcessorSet: list of str
        :param _GroupIdSet: 分组id
        :type GroupIdSet: list of int
        """
        self._BeginTime = None
        self._EndTime = None
        self._PageNumber = None
        self._PageSize = None
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._Statuses = None
        self._AlarmTypeSet = None
        self._LevelSet = None
        self._IdSet = None
        self._AppIdSet = None
        self._WIDSet = None
        self._SpaceCodeSet = None
        self._ExtendOne = None
        self._ExtendTwo = None
        self._ProcessorSet = None
        self._GroupIdSet = None

    @property
    def BeginTime(self):
        """告警开始时间，必填,时间戳秒
        :rtype: int
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """告警结束时间，必填，时间戳秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageNumber(self):
        """分页查询，第几页
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def Statuses(self):
        """告警状态
        :rtype: list of str
        """
        return self._Statuses

    @Statuses.setter
    def Statuses(self, Statuses):
        self._Statuses = Statuses

    @property
    def AlarmTypeSet(self):
        """告警类型
        :rtype: list of AlarmTypeInfo
        """
        return self._AlarmTypeSet

    @AlarmTypeSet.setter
    def AlarmTypeSet(self, AlarmTypeSet):
        self._AlarmTypeSet = AlarmTypeSet

    @property
    def LevelSet(self):
        """告警级别id
        :rtype: list of int
        """
        return self._LevelSet

    @LevelSet.setter
    def LevelSet(self, LevelSet):
        self._LevelSet = LevelSet

    @property
    def IdSet(self):
        """告警id
        :rtype: list of str
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet

    @property
    def AppIdSet(self):
        """应用id
        :rtype: list of int
        """
        return self._AppIdSet

    @AppIdSet.setter
    def AppIdSet(self, AppIdSet):
        self._AppIdSet = AppIdSet

    @property
    def WIDSet(self):
        """设备id
        :rtype: list of str
        """
        return self._WIDSet

    @WIDSet.setter
    def WIDSet(self, WIDSet):
        self._WIDSet = WIDSet

    @property
    def SpaceCodeSet(self):
        """空间层级
        :rtype: list of str
        """
        return self._SpaceCodeSet

    @SpaceCodeSet.setter
    def SpaceCodeSet(self, SpaceCodeSet):
        self._SpaceCodeSet = SpaceCodeSet

    @property
    def ExtendOne(self):
        """应用扩展字段1
        :rtype: list of str
        """
        return self._ExtendOne

    @ExtendOne.setter
    def ExtendOne(self, ExtendOne):
        self._ExtendOne = ExtendOne

    @property
    def ExtendTwo(self):
        """应用扩展字段2
        :rtype: list of str
        """
        return self._ExtendTwo

    @ExtendTwo.setter
    def ExtendTwo(self, ExtendTwo):
        self._ExtendTwo = ExtendTwo

    @property
    def ProcessorSet(self):
        """当前告警处理人，填孪生中台的用户id
        :rtype: list of str
        """
        return self._ProcessorSet

    @ProcessorSet.setter
    def ProcessorSet(self, ProcessorSet):
        self._ProcessorSet = ProcessorSet

    @property
    def GroupIdSet(self):
        """分组id
        :rtype: list of int
        """
        return self._GroupIdSet

    @GroupIdSet.setter
    def GroupIdSet(self, GroupIdSet):
        self._GroupIdSet = GroupIdSet


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        self._Statuses = params.get("Statuses")
        if params.get("AlarmTypeSet") is not None:
            self._AlarmTypeSet = []
            for item in params.get("AlarmTypeSet"):
                obj = AlarmTypeInfo()
                obj._deserialize(item)
                self._AlarmTypeSet.append(obj)
        self._LevelSet = params.get("LevelSet")
        self._IdSet = params.get("IdSet")
        self._AppIdSet = params.get("AppIdSet")
        self._WIDSet = params.get("WIDSet")
        self._SpaceCodeSet = params.get("SpaceCodeSet")
        self._ExtendOne = params.get("ExtendOne")
        self._ExtendTwo = params.get("ExtendTwo")
        self._ProcessorSet = params.get("ProcessorSet")
        self._GroupIdSet = params.get("GroupIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmListRes(AbstractModel):
    """告警列表回包

    """

    def __init__(self):
        r"""
        :param _PageNumber: 第几页
        :type PageNumber: int
        :param _PageSize: 每页条数
        :type PageSize: int
        :param _TotalPage: 总页数
        :type TotalPage: int
        :param _TotalRow: 总条数
        :type TotalRow: int
        :param _AlarmInfoSet: 告警列表集合
        :type AlarmInfoSet: list of AlarmInfo
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalPage = None
        self._TotalRow = None
        self._AlarmInfoSet = None

    @property
    def PageNumber(self):
        """第几页
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalPage(self):
        """总页数
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def TotalRow(self):
        """总条数
        :rtype: int
        """
        return self._TotalRow

    @TotalRow.setter
    def TotalRow(self, TotalRow):
        self._TotalRow = TotalRow

    @property
    def AlarmInfoSet(self):
        """告警列表集合
        :rtype: list of AlarmInfo
        """
        return self._AlarmInfoSet

    @AlarmInfoSet.setter
    def AlarmInfoSet(self, AlarmInfoSet):
        self._AlarmInfoSet = AlarmInfoSet


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalPage = params.get("TotalPage")
        self._TotalRow = params.get("TotalRow")
        if params.get("AlarmInfoSet") is not None:
            self._AlarmInfoSet = []
            for item in params.get("AlarmInfoSet"):
                obj = AlarmInfo()
                obj._deserialize(item)
                self._AlarmInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmListResponse(AbstractModel):
    """DescribeAlarmList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 告警列表查询结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAlarmListRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """告警列表查询结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAlarmListRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeAlarmListRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeAlarmStatusListRequest(AbstractModel):
    """DescribeAlarmStatusList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _WorkspaceId: 工作空间ID
        :type WorkspaceId: str
        """
        self._ApplicationToken = None
        self._WorkspaceId = None

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def WorkspaceId(self):
        """工作空间ID
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId


    def _deserialize(self, params):
        self._ApplicationToken = params.get("ApplicationToken")
        self._WorkspaceId = params.get("WorkspaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmStatusListRes(AbstractModel):
    """告警状态列表返回

    """

    def __init__(self):
        r"""
        :param _List: 告警状态返回结构
        :type List: list of AlarmStatusData
        """
        self._List = None

    @property
    def List(self):
        """告警状态返回结构
        :rtype: list of AlarmStatusData
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AlarmStatusData()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmStatusListResponse(AbstractModel):
    """DescribeAlarmStatusList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 告警状态返回结构
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAlarmStatusListRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """告警状态返回结构
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAlarmStatusListRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeAlarmStatusListRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeAlarmTypeListRequest(AbstractModel):
    """DescribeAlarmTypeList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _ParentType: 一级类型
        :type ParentType: str
        """
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._ParentType = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def ParentType(self):
        """一级类型
        :rtype: str
        """
        return self._ParentType

    @ParentType.setter
    def ParentType(self, ParentType):
        self._ParentType = ParentType


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        self._ParentType = params.get("ParentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmTypeListRes(AbstractModel):
    """告警类型列表回包

    """

    def __init__(self):
        r"""
        :param _AlarmTypeSet: 告警类型查询列表
        :type AlarmTypeSet: list of AlarmTypeDetailInfo
        """
        self._AlarmTypeSet = None

    @property
    def AlarmTypeSet(self):
        """告警类型查询列表
        :rtype: list of AlarmTypeDetailInfo
        """
        return self._AlarmTypeSet

    @AlarmTypeSet.setter
    def AlarmTypeSet(self, AlarmTypeSet):
        self._AlarmTypeSet = AlarmTypeSet


    def _deserialize(self, params):
        if params.get("AlarmTypeSet") is not None:
            self._AlarmTypeSet = []
            for item in params.get("AlarmTypeSet"):
                obj = AlarmTypeDetailInfo()
                obj._deserialize(item)
                self._AlarmTypeSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmTypeListResponse(AbstractModel):
    """DescribeAlarmTypeList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 告警类型列表查询
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAlarmTypeListRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """告警类型列表查询
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAlarmTypeListRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeAlarmTypeListRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationListRequest(AbstractModel):
    """DescribeApplicationList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 项目空间id，本次查询返回的应用均关联至该空间
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _ApplicationId: 应用id数组，可选，填了则表示根据id批量查询
        :type ApplicationId: list of int non-negative
        :param _PageNumber: 请求页号
        :type PageNumber: int
        :param _PageSize: 页容量，默认为10
        :type PageSize: int
        """
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._ApplicationId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def WorkspaceId(self):
        """项目空间id，本次查询返回的应用均关联至该空间
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def ApplicationId(self):
        """应用id数组，可选，填了则表示根据id批量查询
        :rtype: list of int non-negative
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def PageNumber(self):
        """请求页号
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """页容量，默认为10
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        self._ApplicationId = params.get("ApplicationId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
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
        :param _Result: 应用列表
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.ApplicationList`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """应用列表
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ApplicationList`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ApplicationList()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeBuildingListRequest(AbstractModel):
    """DescribeBuildingList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 项目空间id
        :type WorkspaceId: str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _HasModel: 是否有模型文件
        :type HasModel: bool
        :param _SpaceCodes: 空间编码
        :type SpaceCodes: list of str
        """
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._HasModel = None
        self._SpaceCodes = None

    @property
    def WorkspaceId(self):
        """项目空间id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def HasModel(self):
        """是否有模型文件
        :rtype: bool
        """
        return self._HasModel

    @HasModel.setter
    def HasModel(self, HasModel):
        self._HasModel = HasModel

    @property
    def SpaceCodes(self):
        """空间编码
        :rtype: list of str
        """
        return self._SpaceCodes

    @SpaceCodes.setter
    def SpaceCodes(self, SpaceCodes):
        self._SpaceCodes = SpaceCodes


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        self._HasModel = params.get("HasModel")
        self._SpaceCodes = params.get("SpaceCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBuildingListResponse(AbstractModel):
    """DescribeBuildingList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 查询建筑列表出参
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.BuildingListRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """查询建筑列表出参
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.BuildingListRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = BuildingListRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeBuildingModelRequest(AbstractModel):
    """DescribeBuildingModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BuildingId: 建筑id
        :type BuildingId: str
        :param _WorkspaceId: 项目空间id
        :type WorkspaceId: str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._BuildingId = None
        self._WorkspaceId = None
        self._ApplicationToken = None

    @property
    def BuildingId(self):
        """建筑id
        :rtype: str
        """
        return self._BuildingId

    @BuildingId.setter
    def BuildingId(self, BuildingId):
        self._BuildingId = BuildingId

    @property
    def WorkspaceId(self):
        """项目空间id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._BuildingId = params.get("BuildingId")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBuildingModelResponse(AbstractModel):
    """DescribeBuildingModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 建模模型信息出参
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.BuildingModelRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """建模模型信息出参
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.BuildingModelRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = BuildingModelRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeBuildingProfileRequest(AbstractModel):
    """DescribeBuildingProfile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BuildingId: 建筑id
        :type BuildingId: str
        :param _WorkspaceId: 项目空间id
        :type WorkspaceId: str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._BuildingId = None
        self._WorkspaceId = None
        self._ApplicationToken = None

    @property
    def BuildingId(self):
        """建筑id
        :rtype: str
        """
        return self._BuildingId

    @BuildingId.setter
    def BuildingId(self, BuildingId):
        self._BuildingId = BuildingId

    @property
    def WorkspaceId(self):
        """项目空间id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._BuildingId = params.get("BuildingId")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBuildingProfileResponse(AbstractModel):
    """DescribeBuildingProfile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 查询建筑信息出参
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.BuildingProfileRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """查询建筑信息出参
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.BuildingProfileRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = BuildingProfileRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCameraExtendInfoRequest(AbstractModel):
    """DescribeCameraExtendInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WID: 设备的唯一标识

        :type WID: str
        :param _WorkspaceId: 工作空间Id
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._WID = None
        self._WorkspaceId = None
        self._ApplicationToken = None

    @property
    def WID(self):
        """设备的唯一标识

        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID

    @property
    def WorkspaceId(self):
        """工作空间Id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._WID = params.get("WID")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCameraExtendInfoResponse(AbstractModel):
    """DescribeCameraExtendInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 获取视频扩展信息结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.CameraExtendInfoRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """获取视频扩展信息结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.CameraExtendInfoRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CameraExtendInfoRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCityWorkspaceListRequest(AbstractModel):
    """DescribeCityWorkspaceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AdministrativeCodeSet: 行政区编码集合
        :type AdministrativeCodeSet: list of str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._AdministrativeCodeSet = None
        self._ApplicationToken = None

    @property
    def AdministrativeCodeSet(self):
        """行政区编码集合
        :rtype: list of str
        """
        return self._AdministrativeCodeSet

    @AdministrativeCodeSet.setter
    def AdministrativeCodeSet(self, AdministrativeCodeSet):
        self._AdministrativeCodeSet = AdministrativeCodeSet

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._AdministrativeCodeSet = params.get("AdministrativeCodeSet")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCityWorkspaceListRes(AbstractModel):
    """通过城市id查询工作空间列表

    """

    def __init__(self):
        r"""
        :param _WorkspaceSet: 通过城市id查询工作空间列表结果
        :type WorkspaceSet: list of WorkspaceInfo
        """
        self._WorkspaceSet = None

    @property
    def WorkspaceSet(self):
        """通过城市id查询工作空间列表结果
        :rtype: list of WorkspaceInfo
        """
        return self._WorkspaceSet

    @WorkspaceSet.setter
    def WorkspaceSet(self, WorkspaceSet):
        self._WorkspaceSet = WorkspaceSet


    def _deserialize(self, params):
        if params.get("WorkspaceSet") is not None:
            self._WorkspaceSet = []
            for item in params.get("WorkspaceSet"):
                obj = WorkspaceInfo()
                obj._deserialize(item)
                self._WorkspaceSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCityWorkspaceListResponse(AbstractModel):
    """DescribeCityWorkspaceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 工作空间信息集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.DescribeCityWorkspaceListRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """工作空间信息集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeCityWorkspaceListRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeCityWorkspaceListRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceGroupListRequest(AbstractModel):
    """DescribeDeviceGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _WorkspaceId: 工作空间ID
        :type WorkspaceId: int
        :param _GroupId: 分组id, 不传默认全部
        :type GroupId: int
        """
        self._ApplicationToken = None
        self._WorkspaceId = None
        self._GroupId = None

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def WorkspaceId(self):
        """工作空间ID
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def GroupId(self):
        """分组id, 不传默认全部
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ApplicationToken = params.get("ApplicationToken")
        self._WorkspaceId = params.get("WorkspaceId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceGroupListRes(AbstractModel):
    """设备分组信息

    """

    def __init__(self):
        r"""
        :param _List: 设备分组list
        :type List: list of DescribeGroupInfo
        """
        self._List = None

    @property
    def List(self):
        """设备分组list
        :rtype: list of DescribeGroupInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DescribeGroupInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceGroupListResponse(AbstractModel):
    """DescribeDeviceGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 分组信息
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceGroupListRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """分组信息
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceGroupListRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeDeviceGroupListRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceListRequest(AbstractModel):
    """DescribeDeviceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _PageNumber: 分页查询，第几页，必传，大于0
        :type PageNumber: int
        :param _PageSize: 每页条数，必传大于0
        :type PageSize: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _DeviceTypeSet: 设备类型，非必填
        :type DeviceTypeSet: list of str
        :param _ProductIdSet: 产品 pid，非必填
        :type ProductIdSet: list of int
        :param _TagIdSet: 设备标签，非必填
        :type TagIdSet: list of int
        :param _SpaceCodeSet: 空间层级
        :type SpaceCodeSet: list of str
        :param _DeviceTagSet: 设备标签名，非必填
        :type DeviceTagSet: list of str
        :param _WIDSet: 设备wid,非必填
        :type WIDSet: list of str
        :param _Field: 自定义字段
        :type Field: :class:`tencentcloud.weilingwith.v20230427.models.CustomField`
        :param _GroupIdSet: 分组id列表，非必填
        :type GroupIdSet: list of int
        :param _IsActive: 是否激活，默认全部，"1"激活，"0"未激活
        :type IsActive: str
        :param _IsCamera: 是否为摄像头，默认全部，"true"摄像头，"false"非摄像头
        :type IsCamera: str
        """
        self._WorkspaceId = None
        self._PageNumber = None
        self._PageSize = None
        self._ApplicationToken = None
        self._DeviceTypeSet = None
        self._ProductIdSet = None
        self._TagIdSet = None
        self._SpaceCodeSet = None
        self._DeviceTagSet = None
        self._WIDSet = None
        self._Field = None
        self._GroupIdSet = None
        self._IsActive = None
        self._IsCamera = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def PageNumber(self):
        """分页查询，第几页，必传，大于0
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数，必传大于0
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def DeviceTypeSet(self):
        """设备类型，非必填
        :rtype: list of str
        """
        return self._DeviceTypeSet

    @DeviceTypeSet.setter
    def DeviceTypeSet(self, DeviceTypeSet):
        self._DeviceTypeSet = DeviceTypeSet

    @property
    def ProductIdSet(self):
        """产品 pid，非必填
        :rtype: list of int
        """
        return self._ProductIdSet

    @ProductIdSet.setter
    def ProductIdSet(self, ProductIdSet):
        self._ProductIdSet = ProductIdSet

    @property
    def TagIdSet(self):
        """设备标签，非必填
        :rtype: list of int
        """
        return self._TagIdSet

    @TagIdSet.setter
    def TagIdSet(self, TagIdSet):
        self._TagIdSet = TagIdSet

    @property
    def SpaceCodeSet(self):
        """空间层级
        :rtype: list of str
        """
        return self._SpaceCodeSet

    @SpaceCodeSet.setter
    def SpaceCodeSet(self, SpaceCodeSet):
        self._SpaceCodeSet = SpaceCodeSet

    @property
    def DeviceTagSet(self):
        """设备标签名，非必填
        :rtype: list of str
        """
        return self._DeviceTagSet

    @DeviceTagSet.setter
    def DeviceTagSet(self, DeviceTagSet):
        self._DeviceTagSet = DeviceTagSet

    @property
    def WIDSet(self):
        """设备wid,非必填
        :rtype: list of str
        """
        return self._WIDSet

    @WIDSet.setter
    def WIDSet(self, WIDSet):
        self._WIDSet = WIDSet

    @property
    def Field(self):
        """自定义字段
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.CustomField`
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def GroupIdSet(self):
        """分组id列表，非必填
        :rtype: list of int
        """
        return self._GroupIdSet

    @GroupIdSet.setter
    def GroupIdSet(self, GroupIdSet):
        self._GroupIdSet = GroupIdSet

    @property
    def IsActive(self):
        """是否激活，默认全部，"1"激活，"0"未激活
        :rtype: str
        """
        return self._IsActive

    @IsActive.setter
    def IsActive(self, IsActive):
        self._IsActive = IsActive

    @property
    def IsCamera(self):
        """是否为摄像头，默认全部，"true"摄像头，"false"非摄像头
        :rtype: str
        """
        return self._IsCamera

    @IsCamera.setter
    def IsCamera(self, IsCamera):
        self._IsCamera = IsCamera


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._ApplicationToken = params.get("ApplicationToken")
        self._DeviceTypeSet = params.get("DeviceTypeSet")
        self._ProductIdSet = params.get("ProductIdSet")
        self._TagIdSet = params.get("TagIdSet")
        self._SpaceCodeSet = params.get("SpaceCodeSet")
        self._DeviceTagSet = params.get("DeviceTagSet")
        self._WIDSet = params.get("WIDSet")
        if params.get("Field") is not None:
            self._Field = CustomField()
            self._Field._deserialize(params.get("Field"))
        self._GroupIdSet = params.get("GroupIdSet")
        self._IsActive = params.get("IsActive")
        self._IsCamera = params.get("IsCamera")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceListRes(AbstractModel):
    """设备列表查询结果

    """

    def __init__(self):
        r"""
        :param _PageNumber: 第几页
        :type PageNumber: int
        :param _PageSize: 每页条数
        :type PageSize: int
        :param _TotalPage: 总页数
        :type TotalPage: int
        :param _TotalRow: 总条数
        :type TotalRow: int
        :param _DeviceDataSet: 设备信息集合
        :type DeviceDataSet: list of DeviceDataInfo
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalPage = None
        self._TotalRow = None
        self._DeviceDataSet = None

    @property
    def PageNumber(self):
        """第几页
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalPage(self):
        """总页数
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def TotalRow(self):
        """总条数
        :rtype: int
        """
        return self._TotalRow

    @TotalRow.setter
    def TotalRow(self, TotalRow):
        self._TotalRow = TotalRow

    @property
    def DeviceDataSet(self):
        """设备信息集合
        :rtype: list of DeviceDataInfo
        """
        return self._DeviceDataSet

    @DeviceDataSet.setter
    def DeviceDataSet(self, DeviceDataSet):
        self._DeviceDataSet = DeviceDataSet


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalPage = params.get("TotalPage")
        self._TotalRow = params.get("TotalRow")
        if params.get("DeviceDataSet") is not None:
            self._DeviceDataSet = []
            for item in params.get("DeviceDataSet"):
                obj = DeviceDataInfo()
                obj._deserialize(item)
                self._DeviceDataSet.append(obj)
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
        :param _Result: 查询设备列表结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceListRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """查询设备列表结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceListRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeDeviceListRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceShadowListRequest(AbstractModel):
    """DescribeDeviceShadowList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _WIDSet: WID
        :type WIDSet: list of str
        :param _PageNumber: 分页查询，第几页
        :type PageNumber: int
        :param _PageSize: 每页条数
        :type PageSize: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _DeviceTypeSet: 设备类型code
        :type DeviceTypeSet: list of str
        :param _ProductIdSet: 产品 pid
        :type ProductIdSet: list of int
        :param _TagIdSet: 设备标签id
        :type TagIdSet: list of int
        :param _SpaceCodeSet: 空间层级，（支持空间多层，比如具体建筑、具体楼层）
        :type SpaceCodeSet: list of str
        :param _DeviceTagSet: 设备标签名
        :type DeviceTagSet: list of str
        """
        self._WorkspaceId = None
        self._WIDSet = None
        self._PageNumber = None
        self._PageSize = None
        self._ApplicationToken = None
        self._DeviceTypeSet = None
        self._ProductIdSet = None
        self._TagIdSet = None
        self._SpaceCodeSet = None
        self._DeviceTagSet = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WIDSet(self):
        """WID
        :rtype: list of str
        """
        return self._WIDSet

    @WIDSet.setter
    def WIDSet(self, WIDSet):
        self._WIDSet = WIDSet

    @property
    def PageNumber(self):
        """分页查询，第几页
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def DeviceTypeSet(self):
        """设备类型code
        :rtype: list of str
        """
        return self._DeviceTypeSet

    @DeviceTypeSet.setter
    def DeviceTypeSet(self, DeviceTypeSet):
        self._DeviceTypeSet = DeviceTypeSet

    @property
    def ProductIdSet(self):
        """产品 pid
        :rtype: list of int
        """
        return self._ProductIdSet

    @ProductIdSet.setter
    def ProductIdSet(self, ProductIdSet):
        self._ProductIdSet = ProductIdSet

    @property
    def TagIdSet(self):
        """设备标签id
        :rtype: list of int
        """
        return self._TagIdSet

    @TagIdSet.setter
    def TagIdSet(self, TagIdSet):
        self._TagIdSet = TagIdSet

    @property
    def SpaceCodeSet(self):
        """空间层级，（支持空间多层，比如具体建筑、具体楼层）
        :rtype: list of str
        """
        return self._SpaceCodeSet

    @SpaceCodeSet.setter
    def SpaceCodeSet(self, SpaceCodeSet):
        self._SpaceCodeSet = SpaceCodeSet

    @property
    def DeviceTagSet(self):
        """设备标签名
        :rtype: list of str
        """
        return self._DeviceTagSet

    @DeviceTagSet.setter
    def DeviceTagSet(self, DeviceTagSet):
        self._DeviceTagSet = DeviceTagSet


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._WIDSet = params.get("WIDSet")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._ApplicationToken = params.get("ApplicationToken")
        self._DeviceTypeSet = params.get("DeviceTypeSet")
        self._ProductIdSet = params.get("ProductIdSet")
        self._TagIdSet = params.get("TagIdSet")
        self._SpaceCodeSet = params.get("SpaceCodeSet")
        self._DeviceTagSet = params.get("DeviceTagSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceShadowListResponse(AbstractModel):
    """DescribeDeviceShadowList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 获取设备影子结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.DeviceShadowRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """获取设备影子结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DeviceShadowRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DeviceShadowRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceStatusListRequest(AbstractModel):
    """DescribeDeviceStatusList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _PageNumber: 分页查询，第几页，必传，大于0
        :type PageNumber: int
        :param _PageSize: 每页条数，必传大于0
        :type PageSize: int
        :param _DeviceTypeSet: 设备类型
        :type DeviceTypeSet: list of str
        :param _ProductIdSet: 产品 pid
        :type ProductIdSet: list of int
        :param _TagIdSet: 设备标签id

        :type TagIdSet: list of int
        :param _SpaceCodeSet: 空间位置（支持空间多层，比如具体建筑、具体楼层）
        :type SpaceCodeSet: list of str
        :param _WIDSet: 设备编号列表

        :type WIDSet: list of str
        :param _DeviceTagSet: 设备标签名，非必填
        :type DeviceTagSet: list of str
        :param _DeviceStatusSet: 通信在/离线状态（online=normal+fault、offline）
        :type DeviceStatusSet: list of str
        :param _StatusSet: 设备业务状态
（正常-normal、故障-fault、离线-offline）

        :type StatusSet: list of str
        :param _IsAlive: 推流状态，推流中-true，未推流-false 仅摄像头有的状态
        :type IsAlive: list of bool
        """
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._PageNumber = None
        self._PageSize = None
        self._DeviceTypeSet = None
        self._ProductIdSet = None
        self._TagIdSet = None
        self._SpaceCodeSet = None
        self._WIDSet = None
        self._DeviceTagSet = None
        self._DeviceStatusSet = None
        self._StatusSet = None
        self._IsAlive = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def PageNumber(self):
        """分页查询，第几页，必传，大于0
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数，必传大于0
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def DeviceTypeSet(self):
        """设备类型
        :rtype: list of str
        """
        return self._DeviceTypeSet

    @DeviceTypeSet.setter
    def DeviceTypeSet(self, DeviceTypeSet):
        self._DeviceTypeSet = DeviceTypeSet

    @property
    def ProductIdSet(self):
        """产品 pid
        :rtype: list of int
        """
        return self._ProductIdSet

    @ProductIdSet.setter
    def ProductIdSet(self, ProductIdSet):
        self._ProductIdSet = ProductIdSet

    @property
    def TagIdSet(self):
        """设备标签id

        :rtype: list of int
        """
        return self._TagIdSet

    @TagIdSet.setter
    def TagIdSet(self, TagIdSet):
        self._TagIdSet = TagIdSet

    @property
    def SpaceCodeSet(self):
        """空间位置（支持空间多层，比如具体建筑、具体楼层）
        :rtype: list of str
        """
        return self._SpaceCodeSet

    @SpaceCodeSet.setter
    def SpaceCodeSet(self, SpaceCodeSet):
        self._SpaceCodeSet = SpaceCodeSet

    @property
    def WIDSet(self):
        """设备编号列表

        :rtype: list of str
        """
        return self._WIDSet

    @WIDSet.setter
    def WIDSet(self, WIDSet):
        self._WIDSet = WIDSet

    @property
    def DeviceTagSet(self):
        """设备标签名，非必填
        :rtype: list of str
        """
        return self._DeviceTagSet

    @DeviceTagSet.setter
    def DeviceTagSet(self, DeviceTagSet):
        self._DeviceTagSet = DeviceTagSet

    @property
    def DeviceStatusSet(self):
        """通信在/离线状态（online=normal+fault、offline）
        :rtype: list of str
        """
        return self._DeviceStatusSet

    @DeviceStatusSet.setter
    def DeviceStatusSet(self, DeviceStatusSet):
        self._DeviceStatusSet = DeviceStatusSet

    @property
    def StatusSet(self):
        """设备业务状态
（正常-normal、故障-fault、离线-offline）

        :rtype: list of str
        """
        return self._StatusSet

    @StatusSet.setter
    def StatusSet(self, StatusSet):
        self._StatusSet = StatusSet

    @property
    def IsAlive(self):
        """推流状态，推流中-true，未推流-false 仅摄像头有的状态
        :rtype: list of bool
        """
        return self._IsAlive

    @IsAlive.setter
    def IsAlive(self, IsAlive):
        self._IsAlive = IsAlive


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._DeviceTypeSet = params.get("DeviceTypeSet")
        self._ProductIdSet = params.get("ProductIdSet")
        self._TagIdSet = params.get("TagIdSet")
        self._SpaceCodeSet = params.get("SpaceCodeSet")
        self._WIDSet = params.get("WIDSet")
        self._DeviceTagSet = params.get("DeviceTagSet")
        self._DeviceStatusSet = params.get("DeviceStatusSet")
        self._StatusSet = params.get("StatusSet")
        self._IsAlive = params.get("IsAlive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceStatusListResponse(AbstractModel):
    """DescribeDeviceStatusList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 查询设备状态结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.DeviceStatusRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """查询设备状态结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DeviceStatusRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DeviceStatusRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceStatusStatRequest(AbstractModel):
    """DescribeDeviceStatusStat请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Level: 所属空间地理层级，必填。0表示查询所有层级（1、2）的设备状态，1表示楼栋，2表示楼层
        :type Level: int
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _SpaceCodeSet: 空间位置，非必填。为空表示查询所有（1，2）层级
        :type SpaceCodeSet: list of str
        :param _DeviceTypeSet: 设备类型，非必填。为空表示查询所有设备类型
        :type DeviceTypeSet: list of str
        """
        self._Level = None
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._SpaceCodeSet = None
        self._DeviceTypeSet = None

    @property
    def Level(self):
        """所属空间地理层级，必填。0表示查询所有层级（1、2）的设备状态，1表示楼栋，2表示楼层
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def SpaceCodeSet(self):
        """空间位置，非必填。为空表示查询所有（1，2）层级
        :rtype: list of str
        """
        return self._SpaceCodeSet

    @SpaceCodeSet.setter
    def SpaceCodeSet(self, SpaceCodeSet):
        self._SpaceCodeSet = SpaceCodeSet

    @property
    def DeviceTypeSet(self):
        """设备类型，非必填。为空表示查询所有设备类型
        :rtype: list of str
        """
        return self._DeviceTypeSet

    @DeviceTypeSet.setter
    def DeviceTypeSet(self, DeviceTypeSet):
        self._DeviceTypeSet = DeviceTypeSet


    def _deserialize(self, params):
        self._Level = params.get("Level")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        self._SpaceCodeSet = params.get("SpaceCodeSet")
        self._DeviceTypeSet = params.get("DeviceTypeSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceStatusStatResponse(AbstractModel):
    """DescribeDeviceStatusStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 设备状态统计结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.DeviceStatusStatRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """设备状态统计结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DeviceStatusStatRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DeviceStatusStatRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceTagListRequest(AbstractModel):
    """DescribeDeviceTagList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _PageNumber: 分页查询，第几页，必传，大于0
        :type PageNumber: int
        :param _PageSize: 每页条数，必传大于0
        :type PageSize: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._WorkspaceId = None
        self._PageNumber = None
        self._PageSize = None
        self._ApplicationToken = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def PageNumber(self):
        """分页查询，第几页，必传，大于0
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数，必传大于0
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceTagListResponse(AbstractModel):
    """DescribeDeviceTagList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 设备标签查询结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.DeviceTagRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """设备标签查询结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DeviceTagRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DeviceTagRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceTypeListRequest(AbstractModel):
    """DescribeDeviceTypeList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _Flag: 默认0只拉取设备列表关联的设备类型列表；1拉取空间下所有的设备类型列表
        :type Flag: int
        """
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._Flag = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def Flag(self):
        """默认0只拉取设备列表关联的设备类型列表；1拉取空间下所有的设备类型列表
        :rtype: int
        """
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        self._Flag = params.get("Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceTypeListResponse(AbstractModel):
    """DescribeDeviceTypeList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 设备的设备类型列表
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.DeviceTypeSet`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """设备的设备类型列表
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DeviceTypeSet`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DeviceTypeSet()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeEdgeApplicationTokenRequest(AbstractModel):
    """DescribeEdgeApplicationToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _Refresh: 是否刷新token，默认为false
        :type Refresh: bool
        """
        self._ApplicationToken = None
        self._Refresh = None

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def Refresh(self):
        """是否刷新token，默认为false
        :rtype: bool
        """
        return self._Refresh

    @Refresh.setter
    def Refresh(self, Refresh):
        self._Refresh = Refresh


    def _deserialize(self, params):
        self._ApplicationToken = params.get("ApplicationToken")
        self._Refresh = params.get("Refresh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeApplicationTokenResponse(AbstractModel):
    """DescribeEdgeApplicationToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 边缘应用令牌信息	
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.ApplicationTokenInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """边缘应用令牌信息	
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ApplicationTokenInfo`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ApplicationTokenInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeElementProfilePageRequest(AbstractModel):
    """DescribeElementProfilePage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BuildingId: 建筑id
        :type BuildingId: str
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 页容量
        :type PageSize: int
        :param _WorkspaceId: 项目空间id
        :type WorkspaceId: str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _ParentElementIds: 父级构件id
        :type ParentElementIds: list of str
        :param _Level: 空间层级
        :type Level: int
        :param _SpaceTypeCode: 空间分类代码
        :type SpaceTypeCode: str
        :param _EntityTypes: 构件类型
        :type EntityTypes: list of str
        :param _IncludeDelete: 是否包含已删除构件
        :type IncludeDelete: bool
        :param _StartTime: 时间范围-开始
        :type StartTime: int
        :param _EndTime: 时间范围-结束
        :type EndTime: int
        """
        self._BuildingId = None
        self._PageNumber = None
        self._PageSize = None
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._ParentElementIds = None
        self._Level = None
        self._SpaceTypeCode = None
        self._EntityTypes = None
        self._IncludeDelete = None
        self._StartTime = None
        self._EndTime = None

    @property
    def BuildingId(self):
        """建筑id
        :rtype: str
        """
        return self._BuildingId

    @BuildingId.setter
    def BuildingId(self, BuildingId):
        self._BuildingId = BuildingId

    @property
    def PageNumber(self):
        """页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """页容量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def WorkspaceId(self):
        """项目空间id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def ParentElementIds(self):
        """父级构件id
        :rtype: list of str
        """
        return self._ParentElementIds

    @ParentElementIds.setter
    def ParentElementIds(self, ParentElementIds):
        self._ParentElementIds = ParentElementIds

    @property
    def Level(self):
        """空间层级
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def SpaceTypeCode(self):
        """空间分类代码
        :rtype: str
        """
        return self._SpaceTypeCode

    @SpaceTypeCode.setter
    def SpaceTypeCode(self, SpaceTypeCode):
        self._SpaceTypeCode = SpaceTypeCode

    @property
    def EntityTypes(self):
        """构件类型
        :rtype: list of str
        """
        return self._EntityTypes

    @EntityTypes.setter
    def EntityTypes(self, EntityTypes):
        self._EntityTypes = EntityTypes

    @property
    def IncludeDelete(self):
        """是否包含已删除构件
        :rtype: bool
        """
        return self._IncludeDelete

    @IncludeDelete.setter
    def IncludeDelete(self, IncludeDelete):
        self._IncludeDelete = IncludeDelete

    @property
    def StartTime(self):
        """时间范围-开始
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """时间范围-结束
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._BuildingId = params.get("BuildingId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        self._ParentElementIds = params.get("ParentElementIds")
        self._Level = params.get("Level")
        self._SpaceTypeCode = params.get("SpaceTypeCode")
        self._EntityTypes = params.get("EntityTypes")
        self._IncludeDelete = params.get("IncludeDelete")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeElementProfilePageResponse(AbstractModel):
    """DescribeElementProfilePage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 分页查询构件出参
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.ElementProfilePageRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """分页查询构件出参
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ElementProfilePageRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ElementProfilePageRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeElementProfileTreeRequest(AbstractModel):
    """DescribeElementProfileTree请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BuildingId: 建筑id
        :type BuildingId: str
        :param _WorkspaceId: 项目空间id
        :type WorkspaceId: str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _ElementId: 父级构件id
        :type ElementId: str
        :param _Level: 构件级别
        :type Level: int
        :param _SpaceTypeCode: 空间分类代码
        :type SpaceTypeCode: str
        """
        self._BuildingId = None
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._ElementId = None
        self._Level = None
        self._SpaceTypeCode = None

    @property
    def BuildingId(self):
        """建筑id
        :rtype: str
        """
        return self._BuildingId

    @BuildingId.setter
    def BuildingId(self, BuildingId):
        self._BuildingId = BuildingId

    @property
    def WorkspaceId(self):
        """项目空间id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def ElementId(self):
        """父级构件id
        :rtype: str
        """
        return self._ElementId

    @ElementId.setter
    def ElementId(self, ElementId):
        self._ElementId = ElementId

    @property
    def Level(self):
        """构件级别
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def SpaceTypeCode(self):
        """空间分类代码
        :rtype: str
        """
        return self._SpaceTypeCode

    @SpaceTypeCode.setter
    def SpaceTypeCode(self, SpaceTypeCode):
        self._SpaceTypeCode = SpaceTypeCode


    def _deserialize(self, params):
        self._BuildingId = params.get("BuildingId")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        self._ElementId = params.get("ElementId")
        self._Level = params.get("Level")
        self._SpaceTypeCode = params.get("SpaceTypeCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeElementProfileTreeResponse(AbstractModel):
    """DescribeElementProfileTree返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 构件树出参
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.ElementProfileTreeRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """构件树出参
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ElementProfileTreeRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ElementProfileTreeRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeEventListRequest(AbstractModel):
    """DescribeEventList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _PageNumber: 分页查询，第几页，必传，大于0
        :type PageNumber: int
        :param _PageSize: 每页条数，必传大于0
        :type PageSize: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _TriggerType: 事件触发类型，(app, device, timer)
        :type TriggerType: str
        :param _IdSet: 事件id详情
        :type IdSet: list of int
        """
        self._WorkspaceId = None
        self._PageNumber = None
        self._PageSize = None
        self._ApplicationToken = None
        self._TriggerType = None
        self._IdSet = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def PageNumber(self):
        """分页查询，第几页，必传，大于0
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数，必传大于0
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def TriggerType(self):
        """事件触发类型，(app, device, timer)
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def IdSet(self):
        """事件id详情
        :rtype: list of int
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._ApplicationToken = params.get("ApplicationToken")
        self._TriggerType = params.get("TriggerType")
        self._IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEventListRes(AbstractModel):
    """事件列表查询结果

    """

    def __init__(self):
        r"""
        :param _PageNumber: 第几页
        :type PageNumber: int
        :param _PageSize: 每页条数
        :type PageSize: int
        :param _TotalPage: 总页数
        :type TotalPage: int
        :param _TotalRow: 总条数
        :type TotalRow: int
        :param _EventDetailSet: 事件信息列表
        :type EventDetailSet: list of EventDetail
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalPage = None
        self._TotalRow = None
        self._EventDetailSet = None

    @property
    def PageNumber(self):
        """第几页
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalPage(self):
        """总页数
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def TotalRow(self):
        """总条数
        :rtype: int
        """
        return self._TotalRow

    @TotalRow.setter
    def TotalRow(self, TotalRow):
        self._TotalRow = TotalRow

    @property
    def EventDetailSet(self):
        """事件信息列表
        :rtype: list of EventDetail
        """
        return self._EventDetailSet

    @EventDetailSet.setter
    def EventDetailSet(self, EventDetailSet):
        self._EventDetailSet = EventDetailSet


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalPage = params.get("TotalPage")
        self._TotalRow = params.get("TotalRow")
        if params.get("EventDetailSet") is not None:
            self._EventDetailSet = []
            for item in params.get("EventDetailSet"):
                obj = EventDetail()
                obj._deserialize(item)
                self._EventDetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEventListResponse(AbstractModel):
    """DescribeEventList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 事件列表查询结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.DescribeEventListRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """事件列表查询结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeEventListRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeEventListRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeFileDownloadURLRequest(AbstractModel):
    """DescribeFileDownloadURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间Id
        :type WorkspaceId: int
        :param _FileId: 文件Id
        :type FileId: str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._WorkspaceId = None
        self._FileId = None
        self._ApplicationToken = None

    @property
    def WorkspaceId(self):
        """工作空间Id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def FileId(self):
        """文件Id
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._FileId = params.get("FileId")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileDownloadURLResponse(AbstractModel):
    """DescribeFileDownloadURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 文件下载URL地址
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.FileDownloadURL`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """文件下载URL地址
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.FileDownloadURL`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = FileDownloadURL()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeFileUploadURLRequest(AbstractModel):
    """DescribeFileUploadURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间Id
        :type WorkspaceId: int
        :param _FileName: 文件名称
        :type FileName: str
        :param _FileSize: 文件大小
        :type FileSize: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _FileMD5: 文件MD5
        :type FileMD5: str
        :param _SaveType: 存储类型
        :type SaveType: str
        :param _FileExpireTime: 过期时间，过期时间戳，精确到秒的时间戳，noExpireFlag为false时必填

        :type FileExpireTime: int
        :param _NoExpireFlag: 永不过期标记
        :type NoExpireFlag: bool
        """
        self._WorkspaceId = None
        self._FileName = None
        self._FileSize = None
        self._ApplicationToken = None
        self._FileMD5 = None
        self._SaveType = None
        self._FileExpireTime = None
        self._NoExpireFlag = None

    @property
    def WorkspaceId(self):
        """工作空间Id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def FileName(self):
        """文件名称
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

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
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def FileMD5(self):
        """文件MD5
        :rtype: str
        """
        return self._FileMD5

    @FileMD5.setter
    def FileMD5(self, FileMD5):
        self._FileMD5 = FileMD5

    @property
    def SaveType(self):
        """存储类型
        :rtype: str
        """
        return self._SaveType

    @SaveType.setter
    def SaveType(self, SaveType):
        self._SaveType = SaveType

    @property
    def FileExpireTime(self):
        """过期时间，过期时间戳，精确到秒的时间戳，noExpireFlag为false时必填

        :rtype: int
        """
        return self._FileExpireTime

    @FileExpireTime.setter
    def FileExpireTime(self, FileExpireTime):
        self._FileExpireTime = FileExpireTime

    @property
    def NoExpireFlag(self):
        """永不过期标记
        :rtype: bool
        """
        return self._NoExpireFlag

    @NoExpireFlag.setter
    def NoExpireFlag(self, NoExpireFlag):
        self._NoExpireFlag = NoExpireFlag


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._ApplicationToken = params.get("ApplicationToken")
        self._FileMD5 = params.get("FileMD5")
        self._SaveType = params.get("SaveType")
        self._FileExpireTime = params.get("FileExpireTime")
        self._NoExpireFlag = params.get("NoExpireFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileUploadURLResponse(AbstractModel):
    """DescribeFileUploadURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 获取文件上传地址结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.FileUploadURL`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """获取文件上传地址结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.FileUploadURL`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = FileUploadURL()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeGroupInfo(AbstractModel):
    """分组信息实体类

    """

    def __init__(self):
        r"""
        :param _Id: 分组
        :type Id: int
        :param _Name: 设备分组名称
        :type Name: str
        :param _Description: 分组描述
        :type Description: str
        :param _ParentId: 分组父级ID
        :type ParentId: int
        """
        self._Id = None
        self._Name = None
        self._Description = None
        self._ParentId = None

    @property
    def Id(self):
        """分组
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """设备分组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """分组描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ParentId(self):
        """分组父级ID
        :rtype: int
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ParentId = params.get("ParentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInterfaceListRequest(AbstractModel):
    """DescribeInterfaceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _PageNumber: 请求页号
        :type PageNumber: int
        :param _PageSize: 请求页容量，默认全量返回
        :type PageSize: int
        :param _Keyword: 查询关键字
        :type Keyword: str
        :param _Style: 接口方式 1.http 2消息通知服务
        :type Style: list of int non-negative
        :param _Type: 接口分类0. 其他服务 1. IOT服务 2. 空间服务 3.微应用服务 4.场景服务 5.AI算法服务 6.任务算法服务 7.第三方服务 8.3DTiles服务
        :type Type: list of int non-negative
        """
        self._ApplicationToken = None
        self._PageNumber = None
        self._PageSize = None
        self._Keyword = None
        self._Style = None
        self._Type = None

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def PageNumber(self):
        """请求页号
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """请求页容量，默认全量返回
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Keyword(self):
        """查询关键字
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Style(self):
        """接口方式 1.http 2消息通知服务
        :rtype: list of int non-negative
        """
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style

    @property
    def Type(self):
        """接口分类0. 其他服务 1. IOT服务 2. 空间服务 3.微应用服务 4.场景服务 5.AI算法服务 6.任务算法服务 7.第三方服务 8.3DTiles服务
        :rtype: list of int non-negative
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._ApplicationToken = params.get("ApplicationToken")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Keyword = params.get("Keyword")
        self._Style = params.get("Style")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInterfaceListResponse(AbstractModel):
    """DescribeInterfaceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: API列表
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.ApiInfoList`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """API列表
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ApiInfoList`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ApiInfoList()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeLinkRuleListRequest(AbstractModel):
    """DescribeLinkRuleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _PageNumber: 分页查询，第几页，必传，大于0
        :type PageNumber: int
        :param _PageSize: 每页条数，必传大于0
        :type PageSize: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _TriggerType: 事件触发类型
        :type TriggerType: str
        :param _IdSet: 联动id
        :type IdSet: list of int
        """
        self._WorkspaceId = None
        self._PageNumber = None
        self._PageSize = None
        self._ApplicationToken = None
        self._TriggerType = None
        self._IdSet = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def PageNumber(self):
        """分页查询，第几页，必传，大于0
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数，必传大于0
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def TriggerType(self):
        """事件触发类型
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def IdSet(self):
        """联动id
        :rtype: list of int
        """
        return self._IdSet

    @IdSet.setter
    def IdSet(self, IdSet):
        self._IdSet = IdSet


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._ApplicationToken = params.get("ApplicationToken")
        self._TriggerType = params.get("TriggerType")
        self._IdSet = params.get("IdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLinkRuleListRes(AbstractModel):
    """联动规则列表查询结果

    """

    def __init__(self):
        r"""
        :param _PageNumber: 第几页
        :type PageNumber: int
        :param _PageSize: 每页条数
        :type PageSize: int
        :param _TotalPage: 总页数
        :type TotalPage: int
        :param _TotalRow: 总条数
        :type TotalRow: int
        :param _LinkRuleSet: 联动规则列表
        :type LinkRuleSet: list of LinkRuleInfo
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalPage = None
        self._TotalRow = None
        self._LinkRuleSet = None

    @property
    def PageNumber(self):
        """第几页
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalPage(self):
        """总页数
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def TotalRow(self):
        """总条数
        :rtype: int
        """
        return self._TotalRow

    @TotalRow.setter
    def TotalRow(self, TotalRow):
        self._TotalRow = TotalRow

    @property
    def LinkRuleSet(self):
        """联动规则列表
        :rtype: list of LinkRuleInfo
        """
        return self._LinkRuleSet

    @LinkRuleSet.setter
    def LinkRuleSet(self, LinkRuleSet):
        self._LinkRuleSet = LinkRuleSet


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalPage = params.get("TotalPage")
        self._TotalRow = params.get("TotalRow")
        if params.get("LinkRuleSet") is not None:
            self._LinkRuleSet = []
            for item in params.get("LinkRuleSet"):
                obj = LinkRuleInfo()
                obj._deserialize(item)
                self._LinkRuleSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLinkRuleListResponse(AbstractModel):
    """DescribeLinkRuleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 联动规则列表查询结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.DescribeLinkRuleListRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """联动规则列表查询结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeLinkRuleListRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeLinkRuleListRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeModelListRequest(AbstractModel):
    """DescribeModelList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _PageNumber: 分页查询，第几页，大于0
        :type PageNumber: int
        :param _PageSize: 每页条数，大于0
        :type PageSize: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _DeviceTypeSet: 设备类型
        :type DeviceTypeSet: list of str
        :param _ProductIdSet: 产品 pid
        :type ProductIdSet: list of int
        :param _ModelIdSet: 模型id
        :type ModelIdSet: list of str
        """
        self._WorkspaceId = None
        self._PageNumber = None
        self._PageSize = None
        self._ApplicationToken = None
        self._DeviceTypeSet = None
        self._ProductIdSet = None
        self._ModelIdSet = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def PageNumber(self):
        """分页查询，第几页，大于0
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数，大于0
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def DeviceTypeSet(self):
        """设备类型
        :rtype: list of str
        """
        return self._DeviceTypeSet

    @DeviceTypeSet.setter
    def DeviceTypeSet(self, DeviceTypeSet):
        self._DeviceTypeSet = DeviceTypeSet

    @property
    def ProductIdSet(self):
        """产品 pid
        :rtype: list of int
        """
        return self._ProductIdSet

    @ProductIdSet.setter
    def ProductIdSet(self, ProductIdSet):
        self._ProductIdSet = ProductIdSet

    @property
    def ModelIdSet(self):
        """模型id
        :rtype: list of str
        """
        return self._ModelIdSet

    @ModelIdSet.setter
    def ModelIdSet(self, ModelIdSet):
        self._ModelIdSet = ModelIdSet


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._ApplicationToken = params.get("ApplicationToken")
        self._DeviceTypeSet = params.get("DeviceTypeSet")
        self._ProductIdSet = params.get("ProductIdSet")
        self._ModelIdSet = params.get("ModelIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelListResponse(AbstractModel):
    """DescribeModelList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 模型列表查询结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.ModelSet`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """模型列表查询结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ModelSet`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ModelSet()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeProductListRequest(AbstractModel):
    """DescribeProductList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _PageNumber: 分页查询，第几页
        :type PageNumber: int
        :param _PageSize: 每页条数，大于0
        :type PageSize: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _DeviceTypeSet: 设备类型
        :type DeviceTypeSet: list of str
        :param _ProductIdSet: 产品 pid
        :type ProductIdSet: list of int
        :param _ModelIdSet: 模型id
        :type ModelIdSet: list of str
        """
        self._WorkspaceId = None
        self._PageNumber = None
        self._PageSize = None
        self._ApplicationToken = None
        self._DeviceTypeSet = None
        self._ProductIdSet = None
        self._ModelIdSet = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def PageNumber(self):
        """分页查询，第几页
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数，大于0
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def DeviceTypeSet(self):
        """设备类型
        :rtype: list of str
        """
        return self._DeviceTypeSet

    @DeviceTypeSet.setter
    def DeviceTypeSet(self, DeviceTypeSet):
        self._DeviceTypeSet = DeviceTypeSet

    @property
    def ProductIdSet(self):
        """产品 pid
        :rtype: list of int
        """
        return self._ProductIdSet

    @ProductIdSet.setter
    def ProductIdSet(self, ProductIdSet):
        self._ProductIdSet = ProductIdSet

    @property
    def ModelIdSet(self):
        """模型id
        :rtype: list of str
        """
        return self._ModelIdSet

    @ModelIdSet.setter
    def ModelIdSet(self, ModelIdSet):
        self._ModelIdSet = ModelIdSet


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._ApplicationToken = params.get("ApplicationToken")
        self._DeviceTypeSet = params.get("DeviceTypeSet")
        self._ProductIdSet = params.get("ProductIdSet")
        self._ModelIdSet = params.get("ModelIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductListResponse(AbstractModel):
    """DescribeProductList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 产品列表查询结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.ProductSet`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """产品列表查询结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ProductSet`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ProductSet()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribePropertyListRequest(AbstractModel):
    """DescribePropertyList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BuildingId: 建筑id
        :type BuildingId: str
        :param _ElementId: 构件id
        :type ElementId: str
        :param _WorkspaceId: 项目空间id
        :type WorkspaceId: str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._BuildingId = None
        self._ElementId = None
        self._WorkspaceId = None
        self._ApplicationToken = None

    @property
    def BuildingId(self):
        """建筑id
        :rtype: str
        """
        return self._BuildingId

    @BuildingId.setter
    def BuildingId(self, BuildingId):
        self._BuildingId = BuildingId

    @property
    def ElementId(self):
        """构件id
        :rtype: str
        """
        return self._ElementId

    @ElementId.setter
    def ElementId(self, ElementId):
        self._ElementId = ElementId

    @property
    def WorkspaceId(self):
        """项目空间id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._BuildingId = params.get("BuildingId")
        self._ElementId = params.get("ElementId")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePropertyListResponse(AbstractModel):
    """DescribePropertyList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 构件属性信息出参
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.ElementPropertyRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """构件属性信息出参
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ElementPropertyRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = ElementPropertyRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeRuleDetailRequest(AbstractModel):
    """DescribeRuleDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: str
        :param _Id: 联动id
        :type Id: str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._WorkspaceId = None
        self._Id = None
        self._ApplicationToken = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Id(self):
        """联动id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._Id = params.get("Id")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleDetailResponse(AbstractModel):
    """DescribeRuleDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 规则详情查询结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.RuleDetailRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """规则详情查询结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.RuleDetailRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = RuleDetailRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeSceneListRequest(AbstractModel):
    """DescribeSceneList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 项目空间id
        :type WorkspaceId: str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._WorkspaceId = None
        self._ApplicationToken = None

    @property
    def WorkspaceId(self):
        """项目空间id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSceneListResponse(AbstractModel):
    """DescribeSceneList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 场景列表出参
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.SceneListRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """场景列表出参
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.SceneListRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = SceneListRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeSpaceDeviceIdListRequest(AbstractModel):
    """DescribeSpaceDeviceIdList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ElementIds: 构件id列表
        :type ElementIds: list of str
        :param _IsCascade: 是否级联
        :type IsCascade: bool
        :param _WorkspaceId: 项目空间id
        :type WorkspaceId: str
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 页容量
        :type PageSize: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._ElementIds = None
        self._IsCascade = None
        self._WorkspaceId = None
        self._PageNumber = None
        self._PageSize = None
        self._ApplicationToken = None

    @property
    def ElementIds(self):
        """构件id列表
        :rtype: list of str
        """
        return self._ElementIds

    @ElementIds.setter
    def ElementIds(self, ElementIds):
        self._ElementIds = ElementIds

    @property
    def IsCascade(self):
        """是否级联
        :rtype: bool
        """
        return self._IsCascade

    @IsCascade.setter
    def IsCascade(self, IsCascade):
        self._IsCascade = IsCascade

    @property
    def WorkspaceId(self):
        """项目空间id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def PageNumber(self):
        """页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """页容量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._ElementIds = params.get("ElementIds")
        self._IsCascade = params.get("IsCascade")
        self._WorkspaceId = params.get("WorkspaceId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpaceDeviceIdListResponse(AbstractModel):
    """DescribeSpaceDeviceIdList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 设备ID列表
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.SpaceDeviceIdListRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """设备ID列表
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.SpaceDeviceIdListRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = SpaceDeviceIdListRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeSpaceDeviceRelationListRequest(AbstractModel):
    """DescribeSpaceDeviceRelationList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ElementIds: 构件id列表
        :type ElementIds: list of str
        :param _IsCascade: 是否级联
        :type IsCascade: bool
        :param _WorkspaceId: 项目空间id
        :type WorkspaceId: str
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 页容量
        :type PageSize: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._ElementIds = None
        self._IsCascade = None
        self._WorkspaceId = None
        self._PageNumber = None
        self._PageSize = None
        self._ApplicationToken = None

    @property
    def ElementIds(self):
        """构件id列表
        :rtype: list of str
        """
        return self._ElementIds

    @ElementIds.setter
    def ElementIds(self, ElementIds):
        self._ElementIds = ElementIds

    @property
    def IsCascade(self):
        """是否级联
        :rtype: bool
        """
        return self._IsCascade

    @IsCascade.setter
    def IsCascade(self, IsCascade):
        self._IsCascade = IsCascade

    @property
    def WorkspaceId(self):
        """项目空间id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def PageNumber(self):
        """页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """页容量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._ElementIds = params.get("ElementIds")
        self._IsCascade = params.get("IsCascade")
        self._WorkspaceId = params.get("WorkspaceId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpaceDeviceRelationListResponse(AbstractModel):
    """DescribeSpaceDeviceRelationList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 查询指定空间下设备与构件绑定关系列表出参
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.SpaceDeviceRelationRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """查询指定空间下设备与构件绑定关系列表出参
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.SpaceDeviceRelationRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = SpaceDeviceRelationRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeSpaceInfoByDeviceIdRequest(AbstractModel):
    """DescribeSpaceInfoByDeviceId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备id
        :type DeviceId: str
        :param _WorkspaceId: 项目空间id
        :type WorkspaceId: str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._DeviceId = None
        self._WorkspaceId = None
        self._ApplicationToken = None

    @property
    def DeviceId(self):
        """设备id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def WorkspaceId(self):
        """项目空间id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpaceInfoByDeviceIdResponse(AbstractModel):
    """DescribeSpaceInfoByDeviceId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 设备绑定的空间信息出参
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.DeviceSpaceInfoRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """设备绑定的空间信息出参
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DeviceSpaceInfoRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DeviceSpaceInfoRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeSpaceRelationByDeviceIdRequest(AbstractModel):
    """DescribeSpaceRelationByDeviceId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备id
        :type DeviceId: str
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._DeviceId = None
        self._WorkspaceId = None
        self._ApplicationToken = None

    @property
    def DeviceId(self):
        """设备id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpaceRelationByDeviceIdResponse(AbstractModel):
    """DescribeSpaceRelationByDeviceId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 空间层级关系出参
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.SpaceRelationRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """空间层级关系出参
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.SpaceRelationRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = SpaceRelationRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeSpaceTypeListRequest(AbstractModel):
    """DescribeSpaceTypeList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 项目空间ID
        :type WorkspaceId: str
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 页容量
        :type PageSize: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._WorkspaceId = None
        self._PageNumber = None
        self._PageSize = None
        self._ApplicationToken = None

    @property
    def WorkspaceId(self):
        """项目空间ID
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def PageNumber(self):
        """页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """页容量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpaceTypeListResponse(AbstractModel):
    """DescribeSpaceTypeList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 空间分类列表出参
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.SpaceTypeListRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """空间分类列表出参
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.SpaceTypeListRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = SpaceTypeListRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTenantBuildingCountAndAreaRequest(AbstractModel):
    """DescribeTenantBuildingCountAndArea请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceIdList: 租户所有工作空间ID列表
        :type WorkspaceIdList: list of str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._WorkspaceIdList = None
        self._ApplicationToken = None

    @property
    def WorkspaceIdList(self):
        """租户所有工作空间ID列表
        :rtype: list of str
        """
        return self._WorkspaceIdList

    @WorkspaceIdList.setter
    def WorkspaceIdList(self, WorkspaceIdList):
        self._WorkspaceIdList = WorkspaceIdList

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._WorkspaceIdList = params.get("WorkspaceIdList")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTenantBuildingCountAndAreaResponse(AbstractModel):
    """DescribeTenantBuildingCountAndArea返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 租户所有项目空间楼栋数量与建筑面积统计结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.SpaceDataTotalStatsRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """租户所有项目空间楼栋数量与建筑面积统计结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.SpaceDataTotalStatsRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = SpaceDataTotalStatsRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTenantDepartmentListRequest(AbstractModel):
    """DescribeTenantDepartmentList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 翻页页码
        :type Offset: int
        :param _Limit: 翻页大小
        :type Limit: int
        :param _ApplicationToken: token
        :type ApplicationToken: str
        :param _TenantId: 租户ID
        :type TenantId: str
        :param _UpdateAt: 更新时间戳，单位秒
        :type UpdateAt: int
        :param _DepartmentId: 部门ID
        :type DepartmentId: str
        :param _Cursor: 用户id
        :type Cursor: str
        """
        self._Offset = None
        self._Limit = None
        self._ApplicationToken = None
        self._TenantId = None
        self._UpdateAt = None
        self._DepartmentId = None
        self._Cursor = None

    @property
    def Offset(self):
        """翻页页码
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """翻页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ApplicationToken(self):
        """token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def TenantId(self):
        """租户ID
        :rtype: str
        """
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def UpdateAt(self):
        """更新时间戳，单位秒
        :rtype: int
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt

    @property
    def DepartmentId(self):
        """部门ID
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def Cursor(self):
        """用户id
        :rtype: str
        """
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ApplicationToken = params.get("ApplicationToken")
        self._TenantId = params.get("TenantId")
        self._UpdateAt = params.get("UpdateAt")
        self._DepartmentId = params.get("DepartmentId")
        self._Cursor = params.get("Cursor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTenantDepartmentListResponse(AbstractModel):
    """DescribeTenantDepartmentList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回数据
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.SsoDepartmentsResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回数据
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.SsoDepartmentsResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = SsoDepartmentsResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTenantUserListRequest(AbstractModel):
    """DescribeTenantUserList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 翻页页码
        :type Offset: int
        :param _Limit: 翻页大小
        :type Limit: int
        :param _ApplicationToken: token
        :type ApplicationToken: str
        :param _TenantId: 租户ID
        :type TenantId: str
        :param _UpdateAt: 更新时间戳，单位秒
        :type UpdateAt: int
        :param _DepartmentId: 部门ID
        :type DepartmentId: str
        :param _Cursor: 用户id
        :type Cursor: str
        :param _Status: 状态，0，获取所有数据，1正常启用，2禁用
        :type Status: int
        :param _WorkspaceId: 项目空间id
        :type WorkspaceId: str
        :param _Keyword: 关键词
        :type Keyword: str
        :param _NoRecursive: 是否递归获取子级数据，0需要，1不需要，默认为0
        :type NoRecursive: str
        """
        self._Offset = None
        self._Limit = None
        self._ApplicationToken = None
        self._TenantId = None
        self._UpdateAt = None
        self._DepartmentId = None
        self._Cursor = None
        self._Status = None
        self._WorkspaceId = None
        self._Keyword = None
        self._NoRecursive = None

    @property
    def Offset(self):
        """翻页页码
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """翻页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ApplicationToken(self):
        """token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def TenantId(self):
        """租户ID
        :rtype: str
        """
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def UpdateAt(self):
        """更新时间戳，单位秒
        :rtype: int
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt

    @property
    def DepartmentId(self):
        """部门ID
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def Cursor(self):
        """用户id
        :rtype: str
        """
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Status(self):
        """状态，0，获取所有数据，1正常启用，2禁用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def WorkspaceId(self):
        """项目空间id
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Keyword(self):
        """关键词
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def NoRecursive(self):
        """是否递归获取子级数据，0需要，1不需要，默认为0
        :rtype: str
        """
        return self._NoRecursive

    @NoRecursive.setter
    def NoRecursive(self, NoRecursive):
        self._NoRecursive = NoRecursive


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ApplicationToken = params.get("ApplicationToken")
        self._TenantId = params.get("TenantId")
        self._UpdateAt = params.get("UpdateAt")
        self._DepartmentId = params.get("DepartmentId")
        self._Cursor = params.get("Cursor")
        self._Status = params.get("Status")
        self._WorkspaceId = params.get("WorkspaceId")
        self._Keyword = params.get("Keyword")
        self._NoRecursive = params.get("NoRecursive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTenantUserListResponse(AbstractModel):
    """DescribeTenantUserList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回数据
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.SsoUserResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回数据
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.SsoUserResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = SsoUserResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeVideoCloudRecordRequest(AbstractModel):
    """DescribeVideoCloudRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WID: 设备的唯一标识
        :type WID: str
        :param _StartTime: 录像开始时间（s）
        :type StartTime: int
        :param _EndTime: 录像结束时间（s）

        :type EndTime: int
        :param _WorkspaceId: 工作空间Id
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._WID = None
        self._StartTime = None
        self._EndTime = None
        self._WorkspaceId = None
        self._ApplicationToken = None

    @property
    def WID(self):
        """设备的唯一标识
        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID

    @property
    def StartTime(self):
        """录像开始时间（s）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """录像结束时间（s）

        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def WorkspaceId(self):
        """工作空间Id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._WID = params.get("WID")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoCloudRecordResponse(AbstractModel):
    """DescribeVideoCloudRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 获取云录像结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.VideoCloudRecordRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """获取云录像结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.VideoCloudRecordRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = VideoCloudRecordRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeVideoLiveStreamRequest(AbstractModel):
    """DescribeVideoLiveStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WID: 设备的唯一标识

        :type WID: str
        :param _Protocol: 枚举如下：
flv
rtmp
hls
webrtc
raw (视频原始帧)
        :type Protocol: str
        :param _WorkspaceId: 工作空间Id
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _StreamId: 主码流传0，子码流传1，默认主码流

        :type StreamId: int
        :param _Env: 设备所在环境，公有云私有化项目传0或者不传，混合云项目一般传空间id
        :type Env: str
        """
        self._WID = None
        self._Protocol = None
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._StreamId = None
        self._Env = None

    @property
    def WID(self):
        """设备的唯一标识

        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID

    @property
    def Protocol(self):
        """枚举如下：
flv
rtmp
hls
webrtc
raw (视频原始帧)
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def WorkspaceId(self):
        """工作空间Id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def StreamId(self):
        """主码流传0，子码流传1，默认主码流

        :rtype: int
        """
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def Env(self):
        """设备所在环境，公有云私有化项目传0或者不传，混合云项目一般传空间id
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._WID = params.get("WID")
        self._Protocol = params.get("Protocol")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        self._StreamId = params.get("StreamId")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoLiveStreamResponse(AbstractModel):
    """DescribeVideoLiveStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 视频实时流获取结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.VideoRecordStreamRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """视频实时流获取结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.VideoRecordStreamRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = VideoRecordStreamRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeVideoRecordStreamRequest(AbstractModel):
    """DescribeVideoRecordStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WID: 设备唯一标识
        :type WID: str
        :param _Protocol: 枚举如下：
flvsh
rtmp
hls
webrtc
raw (视频原始帧)
        :type Protocol: str
        :param _StartTime: 开始时间（精确到毫秒）
        :type StartTime: int
        :param _EndTime: 结束时间（精确到毫秒）
        :type EndTime: int
        :param _PlayBackRate: 倍速 0.5、1、2、4
        :type PlayBackRate: float
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _Stream: 流的唯一标识，播放链接尾缀
        :type Stream: str
        :param _Env: 公有云私有化项目传0或者不传；混合云项目一般传空间id
        :type Env: str
        """
        self._WID = None
        self._Protocol = None
        self._StartTime = None
        self._EndTime = None
        self._PlayBackRate = None
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._Stream = None
        self._Env = None

    @property
    def WID(self):
        """设备唯一标识
        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID

    @property
    def Protocol(self):
        """枚举如下：
flvsh
rtmp
hls
webrtc
raw (视频原始帧)
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def StartTime(self):
        """开始时间（精确到毫秒）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间（精确到毫秒）
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PlayBackRate(self):
        """倍速 0.5、1、2、4
        :rtype: float
        """
        return self._PlayBackRate

    @PlayBackRate.setter
    def PlayBackRate(self, PlayBackRate):
        self._PlayBackRate = PlayBackRate

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def Stream(self):
        """流的唯一标识，播放链接尾缀
        :rtype: str
        """
        return self._Stream

    @Stream.setter
    def Stream(self, Stream):
        self._Stream = Stream

    @property
    def Env(self):
        """公有云私有化项目传0或者不传；混合云项目一般传空间id
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._WID = params.get("WID")
        self._Protocol = params.get("Protocol")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PlayBackRate = params.get("PlayBackRate")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        self._Stream = params.get("Stream")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoRecordStreamResponse(AbstractModel):
    """DescribeVideoRecordStream返回参数结构体

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


class DescribeWorkSpaceBuildingCountAndAreaRequest(AbstractModel):
    """DescribeWorkSpaceBuildingCountAndArea请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceIdList: 工作空间ID列表
        :type WorkspaceIdList: list of str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._WorkspaceIdList = None
        self._ApplicationToken = None

    @property
    def WorkspaceIdList(self):
        """工作空间ID列表
        :rtype: list of str
        """
        return self._WorkspaceIdList

    @WorkspaceIdList.setter
    def WorkspaceIdList(self, WorkspaceIdList):
        self._WorkspaceIdList = WorkspaceIdList

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._WorkspaceIdList = params.get("WorkspaceIdList")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkSpaceBuildingCountAndAreaResponse(AbstractModel):
    """DescribeWorkSpaceBuildingCountAndArea返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 查询项目空间楼栋数量与建筑面积出参
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.SpaceDataListStatsRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """查询项目空间楼栋数量与建筑面积出参
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.SpaceDataListStatsRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = SpaceDataListStatsRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeWorkspaceListRequest(AbstractModel):
    """DescribeWorkspaceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _WorkspaceId: 工作空间id，非必填，填了则表示根据id进行批量查询
        :type WorkspaceId: int
        """
        self._ApplicationToken = None
        self._WorkspaceId = None

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def WorkspaceId(self):
        """工作空间id，非必填，填了则表示根据id进行批量查询
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId


    def _deserialize(self, params):
        self._ApplicationToken = params.get("ApplicationToken")
        self._WorkspaceId = params.get("WorkspaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkspaceListResponse(AbstractModel):
    """DescribeWorkspaceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 项目空间列表
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.WorkspaceInfoList`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """项目空间列表
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.WorkspaceInfoList`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = WorkspaceInfoList()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeWorkspaceUserListRequest(AbstractModel):
    """DescribeWorkspaceUserList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 翻页页码
        :type Offset: int
        :param _Limit: 翻页大小
        :type Limit: int
        :param _WorkspaceId: 工作空间ID
        :type WorkspaceId: str
        :param _ApplicationToken: token
        :type ApplicationToken: str
        :param _TenantId: 租户ID
        :type TenantId: str
        :param _UpdateAt: 更新时间戳，单位秒
        :type UpdateAt: int
        """
        self._Offset = None
        self._Limit = None
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._TenantId = None
        self._UpdateAt = None

    @property
    def Offset(self):
        """翻页页码
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """翻页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def WorkspaceId(self):
        """工作空间ID
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def TenantId(self):
        """租户ID
        :rtype: str
        """
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def UpdateAt(self):
        """更新时间戳，单位秒
        :rtype: int
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        self._TenantId = params.get("TenantId")
        self._UpdateAt = params.get("UpdateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkspaceUserListResponse(AbstractModel):
    """DescribeWorkspaceUserList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回数据
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.SsoTeamUserResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回数据
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.SsoTeamUserResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = SsoTeamUserResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeviceDataInfo(AbstractModel):
    """设备数据信息

    """

    def __init__(self):
        r"""
        :param _WID: 设备ID， wid
        :type WID: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _DeviceTypeCode: 设备类型Id
        :type DeviceTypeCode: str
        :param _DeviceTypeName: 设备类型名称
        :type DeviceTypeName: str
        :param _ProductId: 产品Id
        :type ProductId: int
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _ProductAbility: 产品能力:信令数据、音视频。二进制数值中第0位表示信令数据、第1位表示音视频 。1（信令数据），3（具有信令数据以及音视频能力）。
        :type ProductAbility: int
        :param _SpaceInfoSet: 设备位置信息
        :type SpaceInfoSet: list of DeviceSpaceInfo
        :param _ModelId: 模型id
        :type ModelId: str
        :param _ModelName: 模型名称
        :type ModelName: str
        :param _DeviceTagSet: 设备标签名，非必填
        :type DeviceTagSet: list of str
        :param _IsActive: 激活状态（1激活、0未激活）
        :type IsActive: int
        :param _ActiveTime:  激活时间
        :type ActiveTime: str
        :param _IsLive: 推流状态（推流中、未推流） 仅摄像机有的状态
        :type IsLive: bool
        :param _ParentWID: 设备所属父设备id（子设备才有）
        :type ParentWID: str
        :param _ParentWIDName: 设备所有父设备名称（子设备才有）
        :type ParentWIDName: str
        :param _SN: 序列号
        :type SN: str
        :param _Location: 设备点位坐标值
        :type Location: :class:`tencentcloud.weilingwith.v20230427.models.DeviceLocation`
        :param _FieldList: 自定义字段
        :type FieldList: list of CustomFieldInfo
        :param _GroupInfo: 分组信息
        :type GroupInfo: str
        :param _DeviceStatus: 通信在/离线状态（online=normal+fault，offline）
        :type DeviceStatus: str
        :param _Status: 设备业务状态（normal、fault、offline）
        :type Status: str
        """
        self._WID = None
        self._DeviceName = None
        self._DeviceTypeCode = None
        self._DeviceTypeName = None
        self._ProductId = None
        self._ProductName = None
        self._ProductAbility = None
        self._SpaceInfoSet = None
        self._ModelId = None
        self._ModelName = None
        self._DeviceTagSet = None
        self._IsActive = None
        self._ActiveTime = None
        self._IsLive = None
        self._ParentWID = None
        self._ParentWIDName = None
        self._SN = None
        self._Location = None
        self._FieldList = None
        self._GroupInfo = None
        self._DeviceStatus = None
        self._Status = None

    @property
    def WID(self):
        """设备ID， wid
        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID

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
    def DeviceTypeCode(self):
        """设备类型Id
        :rtype: str
        """
        return self._DeviceTypeCode

    @DeviceTypeCode.setter
    def DeviceTypeCode(self, DeviceTypeCode):
        self._DeviceTypeCode = DeviceTypeCode

    @property
    def DeviceTypeName(self):
        """设备类型名称
        :rtype: str
        """
        return self._DeviceTypeName

    @DeviceTypeName.setter
    def DeviceTypeName(self, DeviceTypeName):
        self._DeviceTypeName = DeviceTypeName

    @property
    def ProductId(self):
        """产品Id
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        """产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductAbility(self):
        """产品能力:信令数据、音视频。二进制数值中第0位表示信令数据、第1位表示音视频 。1（信令数据），3（具有信令数据以及音视频能力）。
        :rtype: int
        """
        return self._ProductAbility

    @ProductAbility.setter
    def ProductAbility(self, ProductAbility):
        self._ProductAbility = ProductAbility

    @property
    def SpaceInfoSet(self):
        """设备位置信息
        :rtype: list of DeviceSpaceInfo
        """
        return self._SpaceInfoSet

    @SpaceInfoSet.setter
    def SpaceInfoSet(self, SpaceInfoSet):
        self._SpaceInfoSet = SpaceInfoSet

    @property
    def ModelId(self):
        """模型id
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

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
    def DeviceTagSet(self):
        """设备标签名，非必填
        :rtype: list of str
        """
        return self._DeviceTagSet

    @DeviceTagSet.setter
    def DeviceTagSet(self, DeviceTagSet):
        self._DeviceTagSet = DeviceTagSet

    @property
    def IsActive(self):
        """激活状态（1激活、0未激活）
        :rtype: int
        """
        return self._IsActive

    @IsActive.setter
    def IsActive(self, IsActive):
        self._IsActive = IsActive

    @property
    def ActiveTime(self):
        """ 激活时间
        :rtype: str
        """
        return self._ActiveTime

    @ActiveTime.setter
    def ActiveTime(self, ActiveTime):
        self._ActiveTime = ActiveTime

    @property
    def IsLive(self):
        """推流状态（推流中、未推流） 仅摄像机有的状态
        :rtype: bool
        """
        return self._IsLive

    @IsLive.setter
    def IsLive(self, IsLive):
        self._IsLive = IsLive

    @property
    def ParentWID(self):
        """设备所属父设备id（子设备才有）
        :rtype: str
        """
        return self._ParentWID

    @ParentWID.setter
    def ParentWID(self, ParentWID):
        self._ParentWID = ParentWID

    @property
    def ParentWIDName(self):
        """设备所有父设备名称（子设备才有）
        :rtype: str
        """
        return self._ParentWIDName

    @ParentWIDName.setter
    def ParentWIDName(self, ParentWIDName):
        self._ParentWIDName = ParentWIDName

    @property
    def SN(self):
        """序列号
        :rtype: str
        """
        return self._SN

    @SN.setter
    def SN(self, SN):
        self._SN = SN

    @property
    def Location(self):
        """设备点位坐标值
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DeviceLocation`
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def FieldList(self):
        """自定义字段
        :rtype: list of CustomFieldInfo
        """
        return self._FieldList

    @FieldList.setter
    def FieldList(self, FieldList):
        self._FieldList = FieldList

    @property
    def GroupInfo(self):
        """分组信息
        :rtype: str
        """
        return self._GroupInfo

    @GroupInfo.setter
    def GroupInfo(self, GroupInfo):
        self._GroupInfo = GroupInfo

    @property
    def DeviceStatus(self):
        """通信在/离线状态（online=normal+fault，offline）
        :rtype: str
        """
        return self._DeviceStatus

    @DeviceStatus.setter
    def DeviceStatus(self, DeviceStatus):
        self._DeviceStatus = DeviceStatus

    @property
    def Status(self):
        """设备业务状态（normal、fault、offline）
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._WID = params.get("WID")
        self._DeviceName = params.get("DeviceName")
        self._DeviceTypeCode = params.get("DeviceTypeCode")
        self._DeviceTypeName = params.get("DeviceTypeName")
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        self._ProductAbility = params.get("ProductAbility")
        if params.get("SpaceInfoSet") is not None:
            self._SpaceInfoSet = []
            for item in params.get("SpaceInfoSet"):
                obj = DeviceSpaceInfo()
                obj._deserialize(item)
                self._SpaceInfoSet.append(obj)
        self._ModelId = params.get("ModelId")
        self._ModelName = params.get("ModelName")
        self._DeviceTagSet = params.get("DeviceTagSet")
        self._IsActive = params.get("IsActive")
        self._ActiveTime = params.get("ActiveTime")
        self._IsLive = params.get("IsLive")
        self._ParentWID = params.get("ParentWID")
        self._ParentWIDName = params.get("ParentWIDName")
        self._SN = params.get("SN")
        if params.get("Location") is not None:
            self._Location = DeviceLocation()
            self._Location._deserialize(params.get("Location"))
        if params.get("FieldList") is not None:
            self._FieldList = []
            for item in params.get("FieldList"):
                obj = CustomFieldInfo()
                obj._deserialize(item)
                self._FieldList.append(obj)
        self._GroupInfo = params.get("GroupInfo")
        self._DeviceStatus = params.get("DeviceStatus")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceLocation(AbstractModel):
    """设备点位坐标值

    """

    def __init__(self):
        r"""
        :param _X: 点位X坐标值
        :type X: float
        :param _Y: 点位Y坐标值
        :type Y: float
        :param _Z: 点位Z坐标值
        :type Z: float
        """
        self._X = None
        self._Y = None
        self._Z = None

    @property
    def X(self):
        """点位X坐标值
        :rtype: float
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        """点位Y坐标值
        :rtype: float
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Z(self):
        """点位Z坐标值
        :rtype: float
        """
        return self._Z

    @Z.setter
    def Z(self, Z):
        self._Z = Z


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Z = params.get("Z")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceModifyInfo(AbstractModel):
    """设备修改信息入参

    """

    def __init__(self):
        r"""
        :param _WID: 设备id
        :type WID: str
        :param _DeviceName: 修改后的设备名字
        :type DeviceName: str
        """
        self._WID = None
        self._DeviceName = None

    @property
    def WID(self):
        """设备id
        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID

    @property
    def DeviceName(self):
        """修改后的设备名字
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._WID = params.get("WID")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceShadowInfo(AbstractModel):
    """设备影子信息

    """

    def __init__(self):
        r"""
        :param _WID: 设备ID
        :type WID: str
        :param _DeviceShadow: 设备影子数据,返回有效数据为"x-json:"后字段
        :type DeviceShadow: str
        :param _DeviceShadowUpdateTime: 设备影子更新时间
        :type DeviceShadowUpdateTime: str
        """
        self._WID = None
        self._DeviceShadow = None
        self._DeviceShadowUpdateTime = None

    @property
    def WID(self):
        """设备ID
        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID

    @property
    def DeviceShadow(self):
        """设备影子数据,返回有效数据为"x-json:"后字段
        :rtype: str
        """
        return self._DeviceShadow

    @DeviceShadow.setter
    def DeviceShadow(self, DeviceShadow):
        self._DeviceShadow = DeviceShadow

    @property
    def DeviceShadowUpdateTime(self):
        """设备影子更新时间
        :rtype: str
        """
        return self._DeviceShadowUpdateTime

    @DeviceShadowUpdateTime.setter
    def DeviceShadowUpdateTime(self, DeviceShadowUpdateTime):
        self._DeviceShadowUpdateTime = DeviceShadowUpdateTime


    def _deserialize(self, params):
        self._WID = params.get("WID")
        self._DeviceShadow = params.get("DeviceShadow")
        self._DeviceShadowUpdateTime = params.get("DeviceShadowUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceShadowRes(AbstractModel):
    """设备影子查询列表

    """

    def __init__(self):
        r"""
        :param _PageNumber: 第几页
        :type PageNumber: int
        :param _PageSize: 每页条数
        :type PageSize: int
        :param _TotalPage: 总页数
        :type TotalPage: int
        :param _TotalRow: 总条数
        :type TotalRow: int
        :param _Set: 设备影子列表
        :type Set: list of DeviceShadowInfo
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalPage = None
        self._TotalRow = None
        self._Set = None

    @property
    def PageNumber(self):
        """第几页
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalPage(self):
        """总页数
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def TotalRow(self):
        """总条数
        :rtype: int
        """
        return self._TotalRow

    @TotalRow.setter
    def TotalRow(self, TotalRow):
        self._TotalRow = TotalRow

    @property
    def Set(self):
        """设备影子列表
        :rtype: list of DeviceShadowInfo
        """
        return self._Set

    @Set.setter
    def Set(self, Set):
        self._Set = Set


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalPage = params.get("TotalPage")
        self._TotalRow = params.get("TotalRow")
        if params.get("Set") is not None:
            self._Set = []
            for item in params.get("Set"):
                obj = DeviceShadowInfo()
                obj._deserialize(item)
                self._Set.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceSpaceInfo(AbstractModel):
    """设备位置信息

    """

    def __init__(self):
        r"""
        :param _Id: 空间Id
        :type Id: str
        :param _Name: 空间名字
        :type Name: str
        :param _Level: 空间级别
        :type Level: int
        :param _Code: 空间编码
        :type Code: str
        """
        self._Id = None
        self._Name = None
        self._Level = None
        self._Code = None

    @property
    def Id(self):
        """空间Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """空间名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Level(self):
        """空间级别
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Code(self):
        """空间编码
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Level = params.get("Level")
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceSpaceInfoRes(AbstractModel):
    """设备挂接的空间信息

    """

    def __init__(self):
        r"""
        :param _BuildingId: 建筑id
        :type BuildingId: str
        :param _ElementId: 构件id
        :type ElementId: str
        :param _EntityType: 构件类型
        :type EntityType: str
        :param _ElementName: 构件名称
        :type ElementName: str
        :param _Level: 构件级别
        :type Level: int
        :param _BottomHeight: 底部标高（单位mm）
        :type BottomHeight: int
        :param _SpaceCode: 空间编码
        :type SpaceCode: str
        """
        self._BuildingId = None
        self._ElementId = None
        self._EntityType = None
        self._ElementName = None
        self._Level = None
        self._BottomHeight = None
        self._SpaceCode = None

    @property
    def BuildingId(self):
        """建筑id
        :rtype: str
        """
        return self._BuildingId

    @BuildingId.setter
    def BuildingId(self, BuildingId):
        self._BuildingId = BuildingId

    @property
    def ElementId(self):
        """构件id
        :rtype: str
        """
        return self._ElementId

    @ElementId.setter
    def ElementId(self, ElementId):
        self._ElementId = ElementId

    @property
    def EntityType(self):
        """构件类型
        :rtype: str
        """
        return self._EntityType

    @EntityType.setter
    def EntityType(self, EntityType):
        self._EntityType = EntityType

    @property
    def ElementName(self):
        """构件名称
        :rtype: str
        """
        return self._ElementName

    @ElementName.setter
    def ElementName(self, ElementName):
        self._ElementName = ElementName

    @property
    def Level(self):
        """构件级别
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def BottomHeight(self):
        """底部标高（单位mm）
        :rtype: int
        """
        return self._BottomHeight

    @BottomHeight.setter
    def BottomHeight(self, BottomHeight):
        self._BottomHeight = BottomHeight

    @property
    def SpaceCode(self):
        """空间编码
        :rtype: str
        """
        return self._SpaceCode

    @SpaceCode.setter
    def SpaceCode(self, SpaceCode):
        self._SpaceCode = SpaceCode


    def _deserialize(self, params):
        self._BuildingId = params.get("BuildingId")
        self._ElementId = params.get("ElementId")
        self._EntityType = params.get("EntityType")
        self._ElementName = params.get("ElementName")
        self._Level = params.get("Level")
        self._BottomHeight = params.get("BottomHeight")
        self._SpaceCode = params.get("SpaceCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceStatusInfo(AbstractModel):
    """设备状态信息

    """

    def __init__(self):
        r"""
        :param _WID: 设备ID
        :type WID: str
        :param _DeviceStatus: 设备状态（online=normal+fault、offline）
        :type DeviceStatus: str
        :param _DeviceStatusUpdateTime: 设备状态更新时间
        :type DeviceStatusUpdateTime: str
        :param _Status: 设备业务状态（normal、fault、offline）
        :type Status: str
        :param _IsAlive: 推流状态。推流中-true，未推流-false
        :type IsAlive: bool
        """
        self._WID = None
        self._DeviceStatus = None
        self._DeviceStatusUpdateTime = None
        self._Status = None
        self._IsAlive = None

    @property
    def WID(self):
        """设备ID
        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID

    @property
    def DeviceStatus(self):
        """设备状态（online=normal+fault、offline）
        :rtype: str
        """
        return self._DeviceStatus

    @DeviceStatus.setter
    def DeviceStatus(self, DeviceStatus):
        self._DeviceStatus = DeviceStatus

    @property
    def DeviceStatusUpdateTime(self):
        """设备状态更新时间
        :rtype: str
        """
        return self._DeviceStatusUpdateTime

    @DeviceStatusUpdateTime.setter
    def DeviceStatusUpdateTime(self, DeviceStatusUpdateTime):
        self._DeviceStatusUpdateTime = DeviceStatusUpdateTime

    @property
    def Status(self):
        """设备业务状态（normal、fault、offline）
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsAlive(self):
        """推流状态。推流中-true，未推流-false
        :rtype: bool
        """
        return self._IsAlive

    @IsAlive.setter
    def IsAlive(self, IsAlive):
        self._IsAlive = IsAlive


    def _deserialize(self, params):
        self._WID = params.get("WID")
        self._DeviceStatus = params.get("DeviceStatus")
        self._DeviceStatusUpdateTime = params.get("DeviceStatusUpdateTime")
        self._Status = params.get("Status")
        self._IsAlive = params.get("IsAlive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceStatusRes(AbstractModel):
    """设备状态获取接口结果

    """

    def __init__(self):
        r"""
        :param _PageNumber: 第几页
        :type PageNumber: int
        :param _PageSize: 每页条数
        :type PageSize: int
        :param _TotalPage: 总页数
        :type TotalPage: int
        :param _TotalRow: 总条数
        :type TotalRow: int
        :param _DeviceStatusSet: 设备状态信息列表
        :type DeviceStatusSet: list of DeviceStatusInfo
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalPage = None
        self._TotalRow = None
        self._DeviceStatusSet = None

    @property
    def PageNumber(self):
        """第几页
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalPage(self):
        """总页数
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def TotalRow(self):
        """总条数
        :rtype: int
        """
        return self._TotalRow

    @TotalRow.setter
    def TotalRow(self, TotalRow):
        self._TotalRow = TotalRow

    @property
    def DeviceStatusSet(self):
        """设备状态信息列表
        :rtype: list of DeviceStatusInfo
        """
        return self._DeviceStatusSet

    @DeviceStatusSet.setter
    def DeviceStatusSet(self, DeviceStatusSet):
        self._DeviceStatusSet = DeviceStatusSet


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalPage = params.get("TotalPage")
        self._TotalRow = params.get("TotalRow")
        if params.get("DeviceStatusSet") is not None:
            self._DeviceStatusSet = []
            for item in params.get("DeviceStatusSet"):
                obj = DeviceStatusInfo()
                obj._deserialize(item)
                self._DeviceStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceStatusStatRes(AbstractModel):
    """设备状态统计结果

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间Id
        :type WorkspaceId: int
        :param _Total: 汇总数。在线（正常+故障） + 离线
        :type Total: int
        :param _NormalSum: 正常数
        :type NormalSum: int
        :param _OfflineSum: 离线数
        :type OfflineSum: int
        :param _FaultSum: 故障数
        :type FaultSum: int
        :param _DeviceTypeOverviewSet: 设备类型概览列表
        :type DeviceTypeOverviewSet: list of DeviceTypeOverview
        :param _StatLevelSet: 设备类型统计列表
        :type StatLevelSet: list of StatLevel
        """
        self._WorkspaceId = None
        self._Total = None
        self._NormalSum = None
        self._OfflineSum = None
        self._FaultSum = None
        self._DeviceTypeOverviewSet = None
        self._StatLevelSet = None

    @property
    def WorkspaceId(self):
        """工作空间Id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Total(self):
        """汇总数。在线（正常+故障） + 离线
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def NormalSum(self):
        """正常数
        :rtype: int
        """
        return self._NormalSum

    @NormalSum.setter
    def NormalSum(self, NormalSum):
        self._NormalSum = NormalSum

    @property
    def OfflineSum(self):
        """离线数
        :rtype: int
        """
        return self._OfflineSum

    @OfflineSum.setter
    def OfflineSum(self, OfflineSum):
        self._OfflineSum = OfflineSum

    @property
    def FaultSum(self):
        """故障数
        :rtype: int
        """
        return self._FaultSum

    @FaultSum.setter
    def FaultSum(self, FaultSum):
        self._FaultSum = FaultSum

    @property
    def DeviceTypeOverviewSet(self):
        """设备类型概览列表
        :rtype: list of DeviceTypeOverview
        """
        return self._DeviceTypeOverviewSet

    @DeviceTypeOverviewSet.setter
    def DeviceTypeOverviewSet(self, DeviceTypeOverviewSet):
        self._DeviceTypeOverviewSet = DeviceTypeOverviewSet

    @property
    def StatLevelSet(self):
        """设备类型统计列表
        :rtype: list of StatLevel
        """
        return self._StatLevelSet

    @StatLevelSet.setter
    def StatLevelSet(self, StatLevelSet):
        self._StatLevelSet = StatLevelSet


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._Total = params.get("Total")
        self._NormalSum = params.get("NormalSum")
        self._OfflineSum = params.get("OfflineSum")
        self._FaultSum = params.get("FaultSum")
        if params.get("DeviceTypeOverviewSet") is not None:
            self._DeviceTypeOverviewSet = []
            for item in params.get("DeviceTypeOverviewSet"):
                obj = DeviceTypeOverview()
                obj._deserialize(item)
                self._DeviceTypeOverviewSet.append(obj)
        if params.get("StatLevelSet") is not None:
            self._StatLevelSet = []
            for item in params.get("StatLevelSet"):
                obj = StatLevel()
                obj._deserialize(item)
                self._StatLevelSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceTagInfo(AbstractModel):
    """设备标签信息

    """

    def __init__(self):
        r"""
        :param _TagId: 标签Id
        :type TagId: int
        :param _TagName: 标签名字
        :type TagName: str
        """
        self._TagId = None
        self._TagName = None

    @property
    def TagId(self):
        """标签Id
        :rtype: int
        """
        return self._TagId

    @TagId.setter
    def TagId(self, TagId):
        self._TagId = TagId

    @property
    def TagName(self):
        """标签名字
        :rtype: str
        """
        return self._TagName

    @TagName.setter
    def TagName(self, TagName):
        self._TagName = TagName


    def _deserialize(self, params):
        self._TagId = params.get("TagId")
        self._TagName = params.get("TagName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceTagRes(AbstractModel):
    """设备标签列表查询结果

    """

    def __init__(self):
        r"""
        :param _PageNumber: 第几页
        :type PageNumber: int
        :param _PageSize: 每页条数
        :type PageSize: int
        :param _TotalPage: 总页数
        :type TotalPage: int
        :param _TotalRow: 总条数
        :type TotalRow: int
        :param _Set: 设备标签列表
        :type Set: list of DeviceTagInfo
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalPage = None
        self._TotalRow = None
        self._Set = None

    @property
    def PageNumber(self):
        """第几页
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalPage(self):
        """总页数
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def TotalRow(self):
        """总条数
        :rtype: int
        """
        return self._TotalRow

    @TotalRow.setter
    def TotalRow(self, TotalRow):
        self._TotalRow = TotalRow

    @property
    def Set(self):
        """设备标签列表
        :rtype: list of DeviceTagInfo
        """
        return self._Set

    @Set.setter
    def Set(self, Set):
        self._Set = Set


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalPage = params.get("TotalPage")
        self._TotalRow = params.get("TotalRow")
        if params.get("Set") is not None:
            self._Set = []
            for item in params.get("Set"):
                obj = DeviceTagInfo()
                obj._deserialize(item)
                self._Set.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceType(AbstractModel):
    """设备类型

    """

    def __init__(self):
        r"""
        :param _Code: 设备类型编码
        :type Code: str
        :param _Name: 设备类型名称
        :type Name: str
        :param _ParentCode: 父设备类型编码
        :type ParentCode: str
        :param _ParentName: 父设备类型名称
        :type ParentName: str
        :param _IsSubsystem: 是否子系统，1是

        :type IsSubsystem: int
        """
        self._Code = None
        self._Name = None
        self._ParentCode = None
        self._ParentName = None
        self._IsSubsystem = None

    @property
    def Code(self):
        """设备类型编码
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Name(self):
        """设备类型名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParentCode(self):
        """父设备类型编码
        :rtype: str
        """
        return self._ParentCode

    @ParentCode.setter
    def ParentCode(self, ParentCode):
        self._ParentCode = ParentCode

    @property
    def ParentName(self):
        """父设备类型名称
        :rtype: str
        """
        return self._ParentName

    @ParentName.setter
    def ParentName(self, ParentName):
        self._ParentName = ParentName

    @property
    def IsSubsystem(self):
        """是否子系统，1是

        :rtype: int
        """
        return self._IsSubsystem

    @IsSubsystem.setter
    def IsSubsystem(self, IsSubsystem):
        self._IsSubsystem = IsSubsystem


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Name = params.get("Name")
        self._ParentCode = params.get("ParentCode")
        self._ParentName = params.get("ParentName")
        self._IsSubsystem = params.get("IsSubsystem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceTypeOverview(AbstractModel):
    """设备类型概览信息

    """

    def __init__(self):
        r"""
        :param _DeviceType: 设备类型值
        :type DeviceType: str
        :param _Name: 设备类型名称
        :type Name: str
        :param _Total: 汇总数。在线（正常+故障） + 离线
        :type Total: int
        :param _Normal: 正常数
        :type Normal: int
        :param _Offline: 离线数
        :type Offline: int
        :param _Fault: 故障数
        :type Fault: int
        """
        self._DeviceType = None
        self._Name = None
        self._Total = None
        self._Normal = None
        self._Offline = None
        self._Fault = None

    @property
    def DeviceType(self):
        """设备类型值
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Name(self):
        """设备类型名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Total(self):
        """汇总数。在线（正常+故障） + 离线
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Normal(self):
        """正常数
        :rtype: int
        """
        return self._Normal

    @Normal.setter
    def Normal(self, Normal):
        self._Normal = Normal

    @property
    def Offline(self):
        """离线数
        :rtype: int
        """
        return self._Offline

    @Offline.setter
    def Offline(self, Offline):
        self._Offline = Offline

    @property
    def Fault(self):
        """故障数
        :rtype: int
        """
        return self._Fault

    @Fault.setter
    def Fault(self, Fault):
        self._Fault = Fault


    def _deserialize(self, params):
        self._DeviceType = params.get("DeviceType")
        self._Name = params.get("Name")
        self._Total = params.get("Total")
        self._Normal = params.get("Normal")
        self._Offline = params.get("Offline")
        self._Fault = params.get("Fault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceTypeSet(AbstractModel):
    """设备类型列表

    """

    def __init__(self):
        r"""
        :param _Set: 设备类型列表
        :type Set: list of DeviceType
        """
        self._Set = None

    @property
    def Set(self):
        """设备类型列表
        :rtype: list of DeviceType
        """
        return self._Set

    @Set.setter
    def Set(self, Set):
        self._Set = Set


    def _deserialize(self, params):
        if params.get("Set") is not None:
            self._Set = []
            for item in params.get("Set"):
                obj = DeviceType()
                obj._deserialize(item)
                self._Set.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ElementCoordinates(AbstractModel):
    """构件地理坐标

    """

    def __init__(self):
        r"""
        :param _Longitude: 经度
        :type Longitude: float
        :param _Latitude: 纬度
        :type Latitude: float
        :param _Altitude: 高程
        :type Altitude: float
        """
        self._Longitude = None
        self._Latitude = None
        self._Altitude = None

    @property
    def Longitude(self):
        """经度
        :rtype: float
        """
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Latitude(self):
        """纬度
        :rtype: float
        """
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude

    @property
    def Altitude(self):
        """高程
        :rtype: float
        """
        return self._Altitude

    @Altitude.setter
    def Altitude(self, Altitude):
        self._Altitude = Altitude


    def _deserialize(self, params):
        self._Longitude = params.get("Longitude")
        self._Latitude = params.get("Latitude")
        self._Altitude = params.get("Altitude")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ElementProfile(AbstractModel):
    """构件概要信息

    """

    def __init__(self):
        r"""
        :param _BuildingId: 建筑id
        :type BuildingId: str
        :param _ElementId: 构件id
        :type ElementId: str
        :param _EntityType: 构件类型
        :type EntityType: str
        :param _ElementName: 构件名称
        :type ElementName: str
        :param _Level: 构件空间级别
        :type Level: int
        :param _BottomHeight: 底部标高（单位mm）
        :type BottomHeight: int
        :param _Sort: 排序
        :type Sort: int
        :param _SpaceCode: 空间编码
        :type SpaceCode: str
        :param _SpaceTypeCode: 空间分类编码
        :type SpaceTypeCode: str
        :param _SpaceTypeName: 空间分类名称
        :type SpaceTypeName: str
        :param _ParentElementId: 父级构件id
        :type ParentElementId: str
        :param _SpacePoiId: 空间层级类型编码
        :type SpacePoiId: str
        :param _ElementDesc: 构件描述
        :type ElementDesc: str
        :param _IsDelete: 删除标记
        :type IsDelete: int
        """
        self._BuildingId = None
        self._ElementId = None
        self._EntityType = None
        self._ElementName = None
        self._Level = None
        self._BottomHeight = None
        self._Sort = None
        self._SpaceCode = None
        self._SpaceTypeCode = None
        self._SpaceTypeName = None
        self._ParentElementId = None
        self._SpacePoiId = None
        self._ElementDesc = None
        self._IsDelete = None

    @property
    def BuildingId(self):
        """建筑id
        :rtype: str
        """
        return self._BuildingId

    @BuildingId.setter
    def BuildingId(self, BuildingId):
        self._BuildingId = BuildingId

    @property
    def ElementId(self):
        """构件id
        :rtype: str
        """
        return self._ElementId

    @ElementId.setter
    def ElementId(self, ElementId):
        self._ElementId = ElementId

    @property
    def EntityType(self):
        """构件类型
        :rtype: str
        """
        return self._EntityType

    @EntityType.setter
    def EntityType(self, EntityType):
        self._EntityType = EntityType

    @property
    def ElementName(self):
        """构件名称
        :rtype: str
        """
        return self._ElementName

    @ElementName.setter
    def ElementName(self, ElementName):
        self._ElementName = ElementName

    @property
    def Level(self):
        """构件空间级别
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def BottomHeight(self):
        """底部标高（单位mm）
        :rtype: int
        """
        return self._BottomHeight

    @BottomHeight.setter
    def BottomHeight(self, BottomHeight):
        self._BottomHeight = BottomHeight

    @property
    def Sort(self):
        """排序
        :rtype: int
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def SpaceCode(self):
        """空间编码
        :rtype: str
        """
        return self._SpaceCode

    @SpaceCode.setter
    def SpaceCode(self, SpaceCode):
        self._SpaceCode = SpaceCode

    @property
    def SpaceTypeCode(self):
        """空间分类编码
        :rtype: str
        """
        return self._SpaceTypeCode

    @SpaceTypeCode.setter
    def SpaceTypeCode(self, SpaceTypeCode):
        self._SpaceTypeCode = SpaceTypeCode

    @property
    def SpaceTypeName(self):
        """空间分类名称
        :rtype: str
        """
        return self._SpaceTypeName

    @SpaceTypeName.setter
    def SpaceTypeName(self, SpaceTypeName):
        self._SpaceTypeName = SpaceTypeName

    @property
    def ParentElementId(self):
        """父级构件id
        :rtype: str
        """
        return self._ParentElementId

    @ParentElementId.setter
    def ParentElementId(self, ParentElementId):
        self._ParentElementId = ParentElementId

    @property
    def SpacePoiId(self):
        """空间层级类型编码
        :rtype: str
        """
        return self._SpacePoiId

    @SpacePoiId.setter
    def SpacePoiId(self, SpacePoiId):
        self._SpacePoiId = SpacePoiId

    @property
    def ElementDesc(self):
        """构件描述
        :rtype: str
        """
        return self._ElementDesc

    @ElementDesc.setter
    def ElementDesc(self, ElementDesc):
        self._ElementDesc = ElementDesc

    @property
    def IsDelete(self):
        """删除标记
        :rtype: int
        """
        return self._IsDelete

    @IsDelete.setter
    def IsDelete(self, IsDelete):
        self._IsDelete = IsDelete


    def _deserialize(self, params):
        self._BuildingId = params.get("BuildingId")
        self._ElementId = params.get("ElementId")
        self._EntityType = params.get("EntityType")
        self._ElementName = params.get("ElementName")
        self._Level = params.get("Level")
        self._BottomHeight = params.get("BottomHeight")
        self._Sort = params.get("Sort")
        self._SpaceCode = params.get("SpaceCode")
        self._SpaceTypeCode = params.get("SpaceTypeCode")
        self._SpaceTypeName = params.get("SpaceTypeName")
        self._ParentElementId = params.get("ParentElementId")
        self._SpacePoiId = params.get("SpacePoiId")
        self._ElementDesc = params.get("ElementDesc")
        self._IsDelete = params.get("IsDelete")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ElementProfilePageRes(AbstractModel):
    """构件分页查询响应体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 构件总数
        :type TotalCount: int
        :param _List: 构件列表
        :type List: list of ElementProfile
        """
        self._TotalCount = None
        self._List = None

    @property
    def TotalCount(self):
        """构件总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        """构件列表
        :rtype: list of ElementProfile
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ElementProfile()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ElementProfileTreeNode(AbstractModel):
    """构件树节点信息

    """

    def __init__(self):
        r"""
        :param _ElementProfile: 构件概要信息
        :type ElementProfile: :class:`tencentcloud.weilingwith.v20230427.models.ElementProfile`
        :param _Children: 子节点信息
        :type Children: list of ElementProfileTreeNode
        """
        self._ElementProfile = None
        self._Children = None

    @property
    def ElementProfile(self):
        """构件概要信息
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ElementProfile`
        """
        return self._ElementProfile

    @ElementProfile.setter
    def ElementProfile(self, ElementProfile):
        self._ElementProfile = ElementProfile

    @property
    def Children(self):
        """子节点信息
        :rtype: list of ElementProfileTreeNode
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children


    def _deserialize(self, params):
        if params.get("ElementProfile") is not None:
            self._ElementProfile = ElementProfile()
            self._ElementProfile._deserialize(params.get("ElementProfile"))
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = ElementProfileTreeNode()
                obj._deserialize(item)
                self._Children.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ElementProfileTreeRes(AbstractModel):
    """构件树响应体

    """

    def __init__(self):
        r"""
        :param _BuildingId: 建筑id
        :type BuildingId: str
        :param _ParentElementId: 父级构件id
        :type ParentElementId: str
        :param _Root: 构件树
        :type Root: :class:`tencentcloud.weilingwith.v20230427.models.ElementProfileTreeNode`
        """
        self._BuildingId = None
        self._ParentElementId = None
        self._Root = None

    @property
    def BuildingId(self):
        """建筑id
        :rtype: str
        """
        return self._BuildingId

    @BuildingId.setter
    def BuildingId(self, BuildingId):
        self._BuildingId = BuildingId

    @property
    def ParentElementId(self):
        """父级构件id
        :rtype: str
        """
        return self._ParentElementId

    @ParentElementId.setter
    def ParentElementId(self, ParentElementId):
        self._ParentElementId = ParentElementId

    @property
    def Root(self):
        """构件树
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ElementProfileTreeNode`
        """
        return self._Root

    @Root.setter
    def Root(self, Root):
        self._Root = Root


    def _deserialize(self, params):
        self._BuildingId = params.get("BuildingId")
        self._ParentElementId = params.get("ParentElementId")
        if params.get("Root") is not None:
            self._Root = ElementProfileTreeNode()
            self._Root._deserialize(params.get("Root"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ElementProperty(AbstractModel):
    """构件属性信息

    """

    def __init__(self):
        r"""
        :param _Name: 属性名称
        :type Name: str
        :param _Description: 属性描述
        :type Description: str
        :param _Content: 属性内容
        :type Content: str
        """
        self._Name = None
        self._Description = None
        self._Content = None

    @property
    def Name(self):
        """属性名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """属性描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Content(self):
        """属性内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ElementPropertyRes(AbstractModel):
    """构件属性信息响应体

    """

    def __init__(self):
        r"""
        :param _BuildingId: 建筑id
        :type BuildingId: str
        :param _ElementId: 构件id
        :type ElementId: str
        :param _PropertySet: 构件属性集合
        :type PropertySet: list of ElementProperty
        :param _Coordinates: 构件地理坐标
        :type Coordinates: :class:`tencentcloud.weilingwith.v20230427.models.ElementCoordinates`
        :param _Translate: 构件偏移量
        :type Translate: :class:`tencentcloud.weilingwith.v20230427.models.ElementTranslate`
        :param _ElementName: 构件名称
        :type ElementName: str
        :param _EntityTypeCode: 构件类型代码
        :type EntityTypeCode: str
        :param _EntityTypeName: 构件类型名称
        :type EntityTypeName: str
        """
        self._BuildingId = None
        self._ElementId = None
        self._PropertySet = None
        self._Coordinates = None
        self._Translate = None
        self._ElementName = None
        self._EntityTypeCode = None
        self._EntityTypeName = None

    @property
    def BuildingId(self):
        """建筑id
        :rtype: str
        """
        return self._BuildingId

    @BuildingId.setter
    def BuildingId(self, BuildingId):
        self._BuildingId = BuildingId

    @property
    def ElementId(self):
        """构件id
        :rtype: str
        """
        return self._ElementId

    @ElementId.setter
    def ElementId(self, ElementId):
        self._ElementId = ElementId

    @property
    def PropertySet(self):
        """构件属性集合
        :rtype: list of ElementProperty
        """
        return self._PropertySet

    @PropertySet.setter
    def PropertySet(self, PropertySet):
        self._PropertySet = PropertySet

    @property
    def Coordinates(self):
        """构件地理坐标
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ElementCoordinates`
        """
        return self._Coordinates

    @Coordinates.setter
    def Coordinates(self, Coordinates):
        self._Coordinates = Coordinates

    @property
    def Translate(self):
        """构件偏移量
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ElementTranslate`
        """
        return self._Translate

    @Translate.setter
    def Translate(self, Translate):
        self._Translate = Translate

    @property
    def ElementName(self):
        """构件名称
        :rtype: str
        """
        return self._ElementName

    @ElementName.setter
    def ElementName(self, ElementName):
        self._ElementName = ElementName

    @property
    def EntityTypeCode(self):
        """构件类型代码
        :rtype: str
        """
        return self._EntityTypeCode

    @EntityTypeCode.setter
    def EntityTypeCode(self, EntityTypeCode):
        self._EntityTypeCode = EntityTypeCode

    @property
    def EntityTypeName(self):
        """构件类型名称
        :rtype: str
        """
        return self._EntityTypeName

    @EntityTypeName.setter
    def EntityTypeName(self, EntityTypeName):
        self._EntityTypeName = EntityTypeName


    def _deserialize(self, params):
        self._BuildingId = params.get("BuildingId")
        self._ElementId = params.get("ElementId")
        if params.get("PropertySet") is not None:
            self._PropertySet = []
            for item in params.get("PropertySet"):
                obj = ElementProperty()
                obj._deserialize(item)
                self._PropertySet.append(obj)
        if params.get("Coordinates") is not None:
            self._Coordinates = ElementCoordinates()
            self._Coordinates._deserialize(params.get("Coordinates"))
        if params.get("Translate") is not None:
            self._Translate = ElementTranslate()
            self._Translate._deserialize(params.get("Translate"))
        self._ElementName = params.get("ElementName")
        self._EntityTypeCode = params.get("EntityTypeCode")
        self._EntityTypeName = params.get("EntityTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ElementTranslate(AbstractModel):
    """构件平移信息

    """

    def __init__(self):
        r"""
        :param _X: X方向偏移量
        :type X: float
        :param _Y: Y方向偏移量
        :type Y: float
        :param _Z: Z方向偏移量
        :type Z: float
        """
        self._X = None
        self._Y = None
        self._Z = None

    @property
    def X(self):
        """X方向偏移量
        :rtype: float
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        """Y方向偏移量
        :rtype: float
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Z(self):
        """Z方向偏移量
        :rtype: float
        """
        return self._Z

    @Z.setter
    def Z(self, Z):
        self._Z = Z


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Z = params.get("Z")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmptyRes(AbstractModel):
    """空结果返回

    """

    def __init__(self):
        r"""
        :param _Msg: 返回请求状态,成功ok，失败error
        :type Msg: str
        """
        self._Msg = None

    @property
    def Msg(self):
        """返回请求状态,成功ok，失败error
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Event(AbstractModel):
    """事件信息

    """

    def __init__(self):
        r"""
        :param _Id: 事件id或动作Id
        :type Id: int
        :param _Name: 事件名称或动作名称
        :type Name: str
        """
        self._Id = None
        self._Name = None

    @property
    def Id(self):
        """事件id或动作Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """事件名称或动作名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventDetail(AbstractModel):
    """事件详细信息

    """

    def __init__(self):
        r"""
        :param _Id: 事件id
        :type Id: int
        :param _Name: 事件名
        :type Name: str
        :param _TriggerType: 事件触发类型
        :type TriggerType: str
        :param _TriggerCondition: 事件触发条件，返回为x-json后的字段
        :type TriggerCondition: str
        :param _ValidPeriod: 有效期
        :type ValidPeriod: str
        :param _LinkRuleSet: 关联规则列表
        :type LinkRuleSet: list of LinkRule
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _DeviceType: 设备类型，当触发类型为deviceType时返回
        :type DeviceType: str
        :param _WID: 设备的wid，当触发类型是device返回
        :type WID: str
        """
        self._Id = None
        self._Name = None
        self._TriggerType = None
        self._TriggerCondition = None
        self._ValidPeriod = None
        self._LinkRuleSet = None
        self._CreateTime = None
        self._DeviceType = None
        self._WID = None

    @property
    def Id(self):
        """事件id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """事件名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TriggerType(self):
        """事件触发类型
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def TriggerCondition(self):
        """事件触发条件，返回为x-json后的字段
        :rtype: str
        """
        return self._TriggerCondition

    @TriggerCondition.setter
    def TriggerCondition(self, TriggerCondition):
        self._TriggerCondition = TriggerCondition

    @property
    def ValidPeriod(self):
        """有效期
        :rtype: str
        """
        return self._ValidPeriod

    @ValidPeriod.setter
    def ValidPeriod(self, ValidPeriod):
        self._ValidPeriod = ValidPeriod

    @property
    def LinkRuleSet(self):
        """关联规则列表
        :rtype: list of LinkRule
        """
        return self._LinkRuleSet

    @LinkRuleSet.setter
    def LinkRuleSet(self, LinkRuleSet):
        self._LinkRuleSet = LinkRuleSet

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
    def DeviceType(self):
        """设备类型，当触发类型为deviceType时返回
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def WID(self):
        """设备的wid，当触发类型是device返回
        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._TriggerType = params.get("TriggerType")
        self._TriggerCondition = params.get("TriggerCondition")
        self._ValidPeriod = params.get("ValidPeriod")
        if params.get("LinkRuleSet") is not None:
            self._LinkRuleSet = []
            for item in params.get("LinkRuleSet"):
                obj = LinkRule()
                obj._deserialize(item)
                self._LinkRuleSet.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._DeviceType = params.get("DeviceType")
        self._WID = params.get("WID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventObj(AbstractModel):
    """事件对象

    """

    def __init__(self):
        r"""
        :param _Id: 事件id
        :type Id: int
        :param _Name: 事件名称
        :type Name: str
        :param _Type: 事件触发类型名称
        :type Type: str
        :param _Condition: 时间触发条件
        :type Condition: str
        """
        self._Id = None
        self._Name = None
        self._Type = None
        self._Condition = None

    @property
    def Id(self):
        """事件id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """事件名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """事件触发类型名称
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Condition(self):
        """时间触发条件
        :rtype: str
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Condition = params.get("Condition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileDownloadURL(AbstractModel):
    """文件下载URL

    """

    def __init__(self):
        r"""
        :param _FileURL: 下载地址

        :type FileURL: str
        """
        self._FileURL = None

    @property
    def FileURL(self):
        """下载地址

        :rtype: str
        """
        return self._FileURL

    @FileURL.setter
    def FileURL(self, FileURL):
        self._FileURL = FileURL


    def _deserialize(self, params):
        self._FileURL = params.get("FileURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileInfo(AbstractModel):
    """文件信息

    """

    def __init__(self):
        r"""
        :param _FileId: 文件id

        :type FileId: str
        :param _ReportName: 名称
        :type ReportName: str
        """
        self._FileId = None
        self._ReportName = None

    @property
    def FileId(self):
        """文件id

        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def ReportName(self):
        """名称
        :rtype: str
        """
        return self._ReportName

    @ReportName.setter
    def ReportName(self, ReportName):
        self._ReportName = ReportName


    def _deserialize(self, params):
        self._FileId = params.get("FileId")
        self._ReportName = params.get("ReportName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileUploadURL(AbstractModel):
    """获取文件上传URL接口回包

    """

    def __init__(self):
        r"""
        :param _UploadURL: 上传地址
        :type UploadURL: str
        :param _FileId: 文件Id
        :type FileId: str
        :param _DownloadURL: 下载地址
        :type DownloadURL: str
        """
        self._UploadURL = None
        self._FileId = None
        self._DownloadURL = None

    @property
    def UploadURL(self):
        """上传地址
        :rtype: str
        """
        return self._UploadURL

    @UploadURL.setter
    def UploadURL(self, UploadURL):
        self._UploadURL = UploadURL

    @property
    def FileId(self):
        """文件Id
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def DownloadURL(self):
        """下载地址
        :rtype: str
        """
        return self._DownloadURL

    @DownloadURL.setter
    def DownloadURL(self, DownloadURL):
        self._DownloadURL = DownloadURL


    def _deserialize(self, params):
        self._UploadURL = params.get("UploadURL")
        self._FileId = params.get("FileId")
        self._DownloadURL = params.get("DownloadURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HandleRecordInfo(AbstractModel):
    """告警处理记录

    """

    def __init__(self):
        r"""
        :param _Id: 告警处理记录id

        :type Id: int
        :param _Description: 描述
        :type Description: str
        :param _Name: 名称
        :type Name: str
        :param _OperationType: 操作类型
        :type OperationType: str
        :param _Time: 处理时间
        :type Time: str
        :param _Type: 类型
        :type Type: str
        :param _FileSet: 文件列表

        :type FileSet: list of FileInfo
        :param _AppId: 应用appid
        :type AppId: int
        :param _ExtendOne: 扩展字段1，存非孪生中台用户id

        :type ExtendOne: str
        """
        self._Id = None
        self._Description = None
        self._Name = None
        self._OperationType = None
        self._Time = None
        self._Type = None
        self._FileSet = None
        self._AppId = None
        self._ExtendOne = None

    @property
    def Id(self):
        """告警处理记录id

        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Description(self):
        """描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        """名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OperationType(self):
        """操作类型
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def Time(self):
        """处理时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Type(self):
        """类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def FileSet(self):
        """文件列表

        :rtype: list of FileInfo
        """
        return self._FileSet

    @FileSet.setter
    def FileSet(self, FileSet):
        self._FileSet = FileSet

    @property
    def AppId(self):
        """应用appid
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ExtendOne(self):
        """扩展字段1，存非孪生中台用户id

        :rtype: str
        """
        return self._ExtendOne

    @ExtendOne.setter
    def ExtendOne(self, ExtendOne):
        self._ExtendOne = ExtendOne


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._OperationType = params.get("OperationType")
        self._Time = params.get("Time")
        self._Type = params.get("Type")
        if params.get("FileSet") is not None:
            self._FileSet = []
            for item in params.get("FileSet"):
                obj = FileInfo()
                obj._deserialize(item)
                self._FileSet.append(obj)
        self._AppId = params.get("AppId")
        self._ExtendOne = params.get("ExtendOne")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HandlerPersonInfo(AbstractModel):
    """告警处理人列表

    """

    def __init__(self):
        r"""
        :param _Id: 用户id
        :type Id: str
        :param _Name: 用户名
        :type Name: str
        """
        self._Id = None
        self._Name = None

    @property
    def Id(self):
        """用户id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """用户名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkRule(AbstractModel):
    """关联规则信息

    """

    def __init__(self):
        r"""
        :param _Id: 关联联动规则id
        :type Id: int
        :param _Name: 关联联动规则名字
        :type Name: str
        """
        self._Id = None
        self._Name = None

    @property
    def Id(self):
        """关联联动规则id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """关联联动规则名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinkRuleInfo(AbstractModel):
    """联动规则信息

    """

    def __init__(self):
        r"""
        :param _Id: 联动id
        :type Id: int
        :param _Name: 联动名称
        :type Name: str
        :param _EventSet: 事件列表
        :type EventSet: list of Event
        :param _ActionSet: 动作列表
        :type ActionSet: list of Action
        :param _Status: 状态：0开，-1关
        :type Status: int
        :param _BeginDate: 起始时间
        :type BeginDate: str
        :param _EndDate: 结束时间
        :type EndDate: str
        :param _ValidPeriod: 有效周期内容,有效字段为x-json后的字段
        :type ValidPeriod: str
        """
        self._Id = None
        self._Name = None
        self._EventSet = None
        self._ActionSet = None
        self._Status = None
        self._BeginDate = None
        self._EndDate = None
        self._ValidPeriod = None

    @property
    def Id(self):
        """联动id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """联动名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EventSet(self):
        """事件列表
        :rtype: list of Event
        """
        return self._EventSet

    @EventSet.setter
    def EventSet(self, EventSet):
        self._EventSet = EventSet

    @property
    def ActionSet(self):
        """动作列表
        :rtype: list of Action
        """
        return self._ActionSet

    @ActionSet.setter
    def ActionSet(self, ActionSet):
        self._ActionSet = ActionSet

    @property
    def Status(self):
        """状态：0开，-1关
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BeginDate(self):
        """起始时间
        :rtype: str
        """
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def EndDate(self):
        """结束时间
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def ValidPeriod(self):
        """有效周期内容,有效字段为x-json后的字段
        :rtype: str
        """
        return self._ValidPeriod

    @ValidPeriod.setter
    def ValidPeriod(self, ValidPeriod):
        self._ValidPeriod = ValidPeriod


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        if params.get("EventSet") is not None:
            self._EventSet = []
            for item in params.get("EventSet"):
                obj = Event()
                obj._deserialize(item)
                self._EventSet.append(obj)
        if params.get("ActionSet") is not None:
            self._ActionSet = []
            for item in params.get("ActionSet"):
                obj = Action()
                obj._deserialize(item)
                self._ActionSet.append(obj)
        self._Status = params.get("Status")
        self._BeginDate = params.get("BeginDate")
        self._EndDate = params.get("EndDate")
        self._ValidPeriod = params.get("ValidPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MessageProfile(AbstractModel):
    """上报消息概要

    """

    def __init__(self):
        r"""
        :param _AppType: 应用类型
        :type AppType: str
        :param _ModelId: 模型Id
        :type ModelId: str
        :param _PoiCode: 设备类型
        :type PoiCode: str
        """
        self._AppType = None
        self._ModelId = None
        self._PoiCode = None

    @property
    def AppType(self):
        """应用类型
        :rtype: str
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def ModelId(self):
        """模型Id
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def PoiCode(self):
        """设备类型
        :rtype: str
        """
        return self._PoiCode

    @PoiCode.setter
    def PoiCode(self, PoiCode):
        self._PoiCode = PoiCode


    def _deserialize(self, params):
        self._AppType = params.get("AppType")
        self._ModelId = params.get("ModelId")
        self._PoiCode = params.get("PoiCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelInfo(AbstractModel):
    """模型基础信息

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _ModelName: 模型名称
        :type ModelName: str
        :param _ModelId: 物模型id
        :type ModelId: str
        :param _RelatedProduct: 关联产品信息
        :type RelatedProduct: list of RelatedProduct
        :param _DeviceTypeName: 设备类型名
        :type DeviceTypeName: str
        :param _DeviceType: 设备类型id
        :type DeviceType: str
        :param _ModelType: 物模型类型，产品模型/标准模型
        :type ModelType: int
        :param _ModelParams: 模型参数内容,有效字段为"x-json:"后的字段
        :type ModelParams: str
        """
        self._WorkspaceId = None
        self._ModelName = None
        self._ModelId = None
        self._RelatedProduct = None
        self._DeviceTypeName = None
        self._DeviceType = None
        self._ModelType = None
        self._ModelParams = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

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
    def ModelId(self):
        """物模型id
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def RelatedProduct(self):
        """关联产品信息
        :rtype: list of RelatedProduct
        """
        return self._RelatedProduct

    @RelatedProduct.setter
    def RelatedProduct(self, RelatedProduct):
        self._RelatedProduct = RelatedProduct

    @property
    def DeviceTypeName(self):
        """设备类型名
        :rtype: str
        """
        return self._DeviceTypeName

    @DeviceTypeName.setter
    def DeviceTypeName(self, DeviceTypeName):
        self._DeviceTypeName = DeviceTypeName

    @property
    def DeviceType(self):
        """设备类型id
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def ModelType(self):
        """物模型类型，产品模型/标准模型
        :rtype: int
        """
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType

    @property
    def ModelParams(self):
        """模型参数内容,有效字段为"x-json:"后的字段
        :rtype: str
        """
        return self._ModelParams

    @ModelParams.setter
    def ModelParams(self, ModelParams):
        self._ModelParams = ModelParams


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._ModelName = params.get("ModelName")
        self._ModelId = params.get("ModelId")
        if params.get("RelatedProduct") is not None:
            self._RelatedProduct = []
            for item in params.get("RelatedProduct"):
                obj = RelatedProduct()
                obj._deserialize(item)
                self._RelatedProduct.append(obj)
        self._DeviceTypeName = params.get("DeviceTypeName")
        self._DeviceType = params.get("DeviceType")
        self._ModelType = params.get("ModelType")
        self._ModelParams = params.get("ModelParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelSet(AbstractModel):
    """模型列表查询结果

    """

    def __init__(self):
        r"""
        :param _PageNumber: 第几页
        :type PageNumber: int
        :param _PageSize: 每页条数
        :type PageSize: int
        :param _TotalPage: 总页数
        :type TotalPage: int
        :param _TotalRow: 总条数
        :type TotalRow: int
        :param _Set: 模型基础信息
        :type Set: list of ModelInfo
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalPage = None
        self._TotalRow = None
        self._Set = None

    @property
    def PageNumber(self):
        """第几页
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalPage(self):
        """总页数
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def TotalRow(self):
        """总条数
        :rtype: int
        """
        return self._TotalRow

    @TotalRow.setter
    def TotalRow(self, TotalRow):
        self._TotalRow = TotalRow

    @property
    def Set(self):
        """模型基础信息
        :rtype: list of ModelInfo
        """
        return self._Set

    @Set.setter
    def Set(self, Set):
        self._Set = Set


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalPage = params.get("TotalPage")
        self._TotalRow = params.get("TotalRow")
        if params.get("Set") is not None:
            self._Set = []
            for item in params.get("Set"):
                obj = ModelInfo()
                obj._deserialize(item)
                self._Set.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceFieldInfo(AbstractModel):
    """设备自定义值修改信息入参

    """

    def __init__(self):
        r"""
        :param _WID: 设备id
        :type WID: str
        :param _Key: 自定义字段key
        :type Key: str
        :param _Val: 自定义字段值
        :type Val: str
        """
        self._WID = None
        self._Key = None
        self._Val = None

    @property
    def WID(self):
        """设备id
        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID

    @property
    def Key(self):
        """自定义字段key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Val(self):
        """自定义字段值
        :rtype: str
        """
        return self._Val

    @Val.setter
    def Val(self, Val):
        self._Val = Val


    def _deserialize(self, params):
        self._WID = params.get("WID")
        self._Key = params.get("Key")
        self._Val = params.get("Val")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceFieldRequest(AbstractModel):
    """ModifyDeviceField请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _Set: 设备自定义字段修改信息集合
        :type Set: list of ModifyDeviceFieldInfo
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._WorkspaceId = None
        self._Set = None
        self._ApplicationToken = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Set(self):
        """设备自定义字段修改信息集合
        :rtype: list of ModifyDeviceFieldInfo
        """
        return self._Set

    @Set.setter
    def Set(self, Set):
        self._Set = Set

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        if params.get("Set") is not None:
            self._Set = []
            for item in params.get("Set"):
                obj = ModifyDeviceFieldInfo()
                obj._deserialize(item)
                self._Set.append(obj)
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceFieldResponse(AbstractModel):
    """ModifyDeviceField返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回请求结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回请求结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = EmptyRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyDeviceGroupInfo(AbstractModel):
    """设备组修改信息入参

    """

    def __init__(self):
        r"""
        :param _WID: 设备id
        :type WID: str
        :param _GroupId: 设备分组id
        :type GroupId: int
        """
        self._WID = None
        self._GroupId = None

    @property
    def WID(self):
        """设备id
        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID

    @property
    def GroupId(self):
        """设备分组id
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._WID = params.get("WID")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceGroupRequest(AbstractModel):
    """ModifyDeviceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _Set: 设备组修改信息集合	
        :type Set: list of ModifyDeviceGroupInfo
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._WorkspaceId = None
        self._Set = None
        self._ApplicationToken = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Set(self):
        """设备组修改信息集合	
        :rtype: list of ModifyDeviceGroupInfo
        """
        return self._Set

    @Set.setter
    def Set(self, Set):
        self._Set = Set

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        if params.get("Set") is not None:
            self._Set = []
            for item in params.get("Set"):
                obj = ModifyDeviceGroupInfo()
                obj._deserialize(item)
                self._Set.append(obj)
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceGroupResponse(AbstractModel):
    """ModifyDeviceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回请求结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回请求结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = EmptyRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyDeviceNameRequest(AbstractModel):
    """ModifyDeviceName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _Set: 设备修改信息集合
        :type Set: list of DeviceModifyInfo
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._WorkspaceId = None
        self._Set = None
        self._ApplicationToken = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Set(self):
        """设备修改信息集合
        :rtype: list of DeviceModifyInfo
        """
        return self._Set

    @Set.setter
    def Set(self, Set):
        self._Set = Set

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        if params.get("Set") is not None:
            self._Set = []
            for item in params.get("Set"):
                obj = DeviceModifyInfo()
                obj._deserialize(item)
                self._Set.append(obj)
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceNameResponse(AbstractModel):
    """ModifyDeviceName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回请求结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回请求结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = EmptyRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyDeviceTagInfo(AbstractModel):
    """设备标签修改信息入参

    """

    def __init__(self):
        r"""
        :param _WID: 设备id
        :type WID: str
        :param _NameSet: 设备标签名称集合
        :type NameSet: list of str
        """
        self._WID = None
        self._NameSet = None

    @property
    def WID(self):
        """设备id
        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID

    @property
    def NameSet(self):
        """设备标签名称集合
        :rtype: list of str
        """
        return self._NameSet

    @NameSet.setter
    def NameSet(self, NameSet):
        self._NameSet = NameSet


    def _deserialize(self, params):
        self._WID = params.get("WID")
        self._NameSet = params.get("NameSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceTagRequest(AbstractModel):
    """ModifyDeviceTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _Set: 设备标签修改信息集合
        :type Set: list of ModifyDeviceTagInfo
        :param _ApplicationToken: 应用token	
        :type ApplicationToken: str
        """
        self._WorkspaceId = None
        self._Set = None
        self._ApplicationToken = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Set(self):
        """设备标签修改信息集合
        :rtype: list of ModifyDeviceTagInfo
        """
        return self._Set

    @Set.setter
    def Set(self, Set):
        self._Set = Set

    @property
    def ApplicationToken(self):
        """应用token	
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        if params.get("Set") is not None:
            self._Set = []
            for item in params.get("Set"):
                obj = ModifyDeviceTagInfo()
                obj._deserialize(item)
                self._Set.append(obj)
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceTagResponse(AbstractModel):
    """ModifyDeviceTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回请求结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """返回请求结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = EmptyRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ProcessRecordInfo(AbstractModel):
    """处理记录项

    """

    def __init__(self):
        r"""
        :param _Id: 告警的id
        :type Id: str
        :param _ProcessTime: 处理时间，毫秒

        :type ProcessTime: int
        :param _ProcessType: 处理类型，此处操作类型固定填add_record

        :type ProcessType: str
        :param _Processor: 注:此字段填写的是孪生中台的用户，非孪生中台用户不填该字段
[{\"id\":\"123\",\"name\":\"tes\"}]

        :type Processor: str
        :param _ProcessDescription: 处理描述信息
        :type ProcessDescription: str
        :param _AttachedFileId: 附加文件标识
        :type AttachedFileId: str
        """
        self._Id = None
        self._ProcessTime = None
        self._ProcessType = None
        self._Processor = None
        self._ProcessDescription = None
        self._AttachedFileId = None

    @property
    def Id(self):
        """告警的id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ProcessTime(self):
        """处理时间，毫秒

        :rtype: int
        """
        return self._ProcessTime

    @ProcessTime.setter
    def ProcessTime(self, ProcessTime):
        self._ProcessTime = ProcessTime

    @property
    def ProcessType(self):
        """处理类型，此处操作类型固定填add_record

        :rtype: str
        """
        return self._ProcessType

    @ProcessType.setter
    def ProcessType(self, ProcessType):
        self._ProcessType = ProcessType

    @property
    def Processor(self):
        """注:此字段填写的是孪生中台的用户，非孪生中台用户不填该字段
[{\"id\":\"123\",\"name\":\"tes\"}]

        :rtype: str
        """
        return self._Processor

    @Processor.setter
    def Processor(self, Processor):
        self._Processor = Processor

    @property
    def ProcessDescription(self):
        """处理描述信息
        :rtype: str
        """
        return self._ProcessDescription

    @ProcessDescription.setter
    def ProcessDescription(self, ProcessDescription):
        self._ProcessDescription = ProcessDescription

    @property
    def AttachedFileId(self):
        """附加文件标识
        :rtype: str
        """
        return self._AttachedFileId

    @AttachedFileId.setter
    def AttachedFileId(self, AttachedFileId):
        self._AttachedFileId = AttachedFileId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ProcessTime = params.get("ProcessTime")
        self._ProcessType = params.get("ProcessType")
        self._Processor = params.get("Processor")
        self._ProcessDescription = params.get("ProcessDescription")
        self._AttachedFileId = params.get("AttachedFileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductInfo(AbstractModel):
    """产品信息

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _ProductId: 产品PID
        :type ProductId: int
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _DeviceTypeName: 设备类型
        :type DeviceTypeName: str
        :param _DeviceTypeId: 设备类型id
        :type DeviceTypeId: str
        :param _Attribute: 产品属性，如：网关（1）、直连设备（2）、子设备（3）
        :type Attribute: int
        :param _ProductType: 产品型号
        :type ProductType: str
        :param _ProductAbility: 产品能力:信令数据、音视频。二进制数值中第0位表示信令数据、第1位表示音视频 。1（信令数据），3（具有信令数据以及音视频能力）。
        :type ProductAbility: int
        :param _Manufacturer: 生产厂商
        :type Manufacturer: str
        :param _MaintenanceMfr: 维保厂商
        :type MaintenanceMfr: str
        :param _ModelName: 物模型名称
        :type ModelName: str
        :param _ModelId: 物模型id
        :type ModelId: str
        :param _ModelType: 物模型类型，产品模型/标准模型
        :type ModelType: int
        """
        self._WorkspaceId = None
        self._ProductId = None
        self._ProductName = None
        self._DeviceTypeName = None
        self._DeviceTypeId = None
        self._Attribute = None
        self._ProductType = None
        self._ProductAbility = None
        self._Manufacturer = None
        self._MaintenanceMfr = None
        self._ModelName = None
        self._ModelId = None
        self._ModelType = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ProductId(self):
        """产品PID
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        """产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def DeviceTypeName(self):
        """设备类型
        :rtype: str
        """
        return self._DeviceTypeName

    @DeviceTypeName.setter
    def DeviceTypeName(self, DeviceTypeName):
        self._DeviceTypeName = DeviceTypeName

    @property
    def DeviceTypeId(self):
        """设备类型id
        :rtype: str
        """
        return self._DeviceTypeId

    @DeviceTypeId.setter
    def DeviceTypeId(self, DeviceTypeId):
        self._DeviceTypeId = DeviceTypeId

    @property
    def Attribute(self):
        """产品属性，如：网关（1）、直连设备（2）、子设备（3）
        :rtype: int
        """
        return self._Attribute

    @Attribute.setter
    def Attribute(self, Attribute):
        self._Attribute = Attribute

    @property
    def ProductType(self):
        """产品型号
        :rtype: str
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def ProductAbility(self):
        """产品能力:信令数据、音视频。二进制数值中第0位表示信令数据、第1位表示音视频 。1（信令数据），3（具有信令数据以及音视频能力）。
        :rtype: int
        """
        return self._ProductAbility

    @ProductAbility.setter
    def ProductAbility(self, ProductAbility):
        self._ProductAbility = ProductAbility

    @property
    def Manufacturer(self):
        """生产厂商
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def MaintenanceMfr(self):
        """维保厂商
        :rtype: str
        """
        return self._MaintenanceMfr

    @MaintenanceMfr.setter
    def MaintenanceMfr(self, MaintenanceMfr):
        self._MaintenanceMfr = MaintenanceMfr

    @property
    def ModelName(self):
        """物模型名称
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ModelId(self):
        """物模型id
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelType(self):
        """物模型类型，产品模型/标准模型
        :rtype: int
        """
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        self._DeviceTypeName = params.get("DeviceTypeName")
        self._DeviceTypeId = params.get("DeviceTypeId")
        self._Attribute = params.get("Attribute")
        self._ProductType = params.get("ProductType")
        self._ProductAbility = params.get("ProductAbility")
        self._Manufacturer = params.get("Manufacturer")
        self._MaintenanceMfr = params.get("MaintenanceMfr")
        self._ModelName = params.get("ModelName")
        self._ModelId = params.get("ModelId")
        self._ModelType = params.get("ModelType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductSet(AbstractModel):
    """产品列表查询结果

    """

    def __init__(self):
        r"""
        :param _PageNumber: 第几页
        :type PageNumber: int
        :param _PageSize: 每页条数
        :type PageSize: int
        :param _TotalPage: 总页数
        :type TotalPage: int
        :param _TotalRow: 总条数
        :type TotalRow: int
        :param _Product: 产品信息列表
        :type Product: list of ProductInfo
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalPage = None
        self._TotalRow = None
        self._Product = None

    @property
    def PageNumber(self):
        """第几页
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalPage(self):
        """总页数
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def TotalRow(self):
        """总条数
        :rtype: int
        """
        return self._TotalRow

    @TotalRow.setter
    def TotalRow(self, TotalRow):
        self._TotalRow = TotalRow

    @property
    def Product(self):
        """产品信息列表
        :rtype: list of ProductInfo
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalPage = params.get("TotalPage")
        self._TotalRow = params.get("TotalRow")
        if params.get("Product") is not None:
            self._Product = []
            for item in params.get("Product"):
                obj = ProductInfo()
                obj._deserialize(item)
                self._Product.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RawInfo(AbstractModel):
    """视频流Raw协议信息

    """

    def __init__(self):
        r"""
        :param _SM4Vector: 加密向量（如果视频网关选择流为非加密传输这个参数可忽略）
        :type SM4Vector: str
        :param _NATIP: 专线ip (非专线接入可忽略)
        :type NATIP: str
        :param _StreamToken: 客户端握手鉴权参数
        :type StreamToken: str
        :param _Port: 拉流端口
        :type Port: int
        :param _StreamEnKey: 视频流加密key,目前为AES128加密KEY（如果视频网关选择流为非加密传输这个参数可忽略）
        :type StreamEnKey: str
        :param _IP: 拉流公网地址（非公网接入时，这个地址是内网地址）
        :type IP: str
        :param _InnerIP: 拉流内网地址
        :type InnerIP: str
        """
        self._SM4Vector = None
        self._NATIP = None
        self._StreamToken = None
        self._Port = None
        self._StreamEnKey = None
        self._IP = None
        self._InnerIP = None

    @property
    def SM4Vector(self):
        """加密向量（如果视频网关选择流为非加密传输这个参数可忽略）
        :rtype: str
        """
        return self._SM4Vector

    @SM4Vector.setter
    def SM4Vector(self, SM4Vector):
        self._SM4Vector = SM4Vector

    @property
    def NATIP(self):
        """专线ip (非专线接入可忽略)
        :rtype: str
        """
        return self._NATIP

    @NATIP.setter
    def NATIP(self, NATIP):
        self._NATIP = NATIP

    @property
    def StreamToken(self):
        """客户端握手鉴权参数
        :rtype: str
        """
        return self._StreamToken

    @StreamToken.setter
    def StreamToken(self, StreamToken):
        self._StreamToken = StreamToken

    @property
    def Port(self):
        """拉流端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def StreamEnKey(self):
        """视频流加密key,目前为AES128加密KEY（如果视频网关选择流为非加密传输这个参数可忽略）
        :rtype: str
        """
        return self._StreamEnKey

    @StreamEnKey.setter
    def StreamEnKey(self, StreamEnKey):
        self._StreamEnKey = StreamEnKey

    @property
    def IP(self):
        """拉流公网地址（非公网接入时，这个地址是内网地址）
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def InnerIP(self):
        """拉流内网地址
        :rtype: str
        """
        return self._InnerIP

    @InnerIP.setter
    def InnerIP(self, InnerIP):
        self._InnerIP = InnerIP


    def _deserialize(self, params):
        self._SM4Vector = params.get("SM4Vector")
        self._NATIP = params.get("NATIP")
        self._StreamToken = params.get("StreamToken")
        self._Port = params.get("Port")
        self._StreamEnKey = params.get("StreamEnKey")
        self._IP = params.get("IP")
        self._InnerIP = params.get("InnerIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordInfo(AbstractModel):
    """录像信息

    """

    def __init__(self):
        r"""
        :param _StartTime: 本录像片段开始时间（s）
        :type StartTime: int
        :param _EndTime: 本录像片段结束时间（s）
        :type EndTime: int
        :param _VideoURL: 录像片段文件url
        :type VideoURL: str
        """
        self._StartTime = None
        self._EndTime = None
        self._VideoURL = None

    @property
    def StartTime(self):
        """本录像片段开始时间（s）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """本录像片段结束时间（s）
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def VideoURL(self):
        """录像片段文件url
        :rtype: str
        """
        return self._VideoURL

    @VideoURL.setter
    def VideoURL(self, VideoURL):
        self._VideoURL = VideoURL


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._VideoURL = params.get("VideoURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelatedProduct(AbstractModel):
    """关联产品信息

    """

    def __init__(self):
        r"""
        :param _Id: 关联产品pid
        :type Id: int
        :param _Name: 关联产品名字
        :type Name: str
        """
        self._Id = None
        self._Name = None

    @property
    def Id(self):
        """关联产品pid
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """关联产品名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportAppMessage(AbstractModel):
    """单条消息上报请求

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间Id
        :type WorkspaceId: int
        :param _Profile: 消息定义
        :type Profile: :class:`tencentcloud.weilingwith.v20230427.models.MessageProfile`
        :param _ReportTs: 数据上报时间
        :type ReportTs: int
        :param _Properties: 属性定义 - KV，若为json格式，需在前加上x-json:，有效字段为x-json:后的字段
        :type Properties: str
        :param _EventSet: 事件定义 - KKV，若为json格式，需在前加上x-json:，有效字段为x-json:后的字段
        :type EventSet: str
        :param _ServiceSet: 服务定义 - KKV,若为json格式，需在前加上x-json:，有效字段为x-json:后的字段
        :type ServiceSet: str
        :param _ExtendTwo: 扩展字段2，如：算法上报id，若为json格式，需在前加上x-json:
        :type ExtendTwo: str
        :param _Echo: 透传信息，若为json格式，需在前加上x-json:，有效字段为x-json:后的字段
        :type Echo: str
        """
        self._WorkspaceId = None
        self._Profile = None
        self._ReportTs = None
        self._Properties = None
        self._EventSet = None
        self._ServiceSet = None
        self._ExtendTwo = None
        self._Echo = None

    @property
    def WorkspaceId(self):
        """工作空间Id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Profile(self):
        """消息定义
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.MessageProfile`
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def ReportTs(self):
        """数据上报时间
        :rtype: int
        """
        return self._ReportTs

    @ReportTs.setter
    def ReportTs(self, ReportTs):
        self._ReportTs = ReportTs

    @property
    def Properties(self):
        """属性定义 - KV，若为json格式，需在前加上x-json:，有效字段为x-json:后的字段
        :rtype: str
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def EventSet(self):
        """事件定义 - KKV，若为json格式，需在前加上x-json:，有效字段为x-json:后的字段
        :rtype: str
        """
        return self._EventSet

    @EventSet.setter
    def EventSet(self, EventSet):
        self._EventSet = EventSet

    @property
    def ServiceSet(self):
        """服务定义 - KKV,若为json格式，需在前加上x-json:，有效字段为x-json:后的字段
        :rtype: str
        """
        return self._ServiceSet

    @ServiceSet.setter
    def ServiceSet(self, ServiceSet):
        self._ServiceSet = ServiceSet

    @property
    def ExtendTwo(self):
        """扩展字段2，如：算法上报id，若为json格式，需在前加上x-json:
        :rtype: str
        """
        return self._ExtendTwo

    @ExtendTwo.setter
    def ExtendTwo(self, ExtendTwo):
        self._ExtendTwo = ExtendTwo

    @property
    def Echo(self):
        """透传信息，若为json格式，需在前加上x-json:，有效字段为x-json:后的字段
        :rtype: str
        """
        return self._Echo

    @Echo.setter
    def Echo(self, Echo):
        self._Echo = Echo


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        if params.get("Profile") is not None:
            self._Profile = MessageProfile()
            self._Profile._deserialize(params.get("Profile"))
        self._ReportTs = params.get("ReportTs")
        self._Properties = params.get("Properties")
        self._EventSet = params.get("EventSet")
        self._ServiceSet = params.get("ServiceSet")
        self._ExtendTwo = params.get("ExtendTwo")
        self._Echo = params.get("Echo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportAppMessageRequest(AbstractModel):
    """ReportAppMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间Id
        :type WorkspaceId: int
        :param _Profile: 消息定义
        :type Profile: :class:`tencentcloud.weilingwith.v20230427.models.MessageProfile`
        :param _ReportTs: 数据上报时间
        :type ReportTs: int
        :param _Properties: 属性定义 - KV的json格式,有效字段为x-json:后的字段
        :type Properties: str
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _EventSet: 事件定义 - KKV的json格式,有效字段为x-json:后的字段
        :type EventSet: str
        :param _ServiceSet: 服务定义 - KKV的json格式,有效字段为x-json:后的字段
        :type ServiceSet: str
        :param _ExtendTwo: 扩展字段2，如：算法上报id，若为json格式，需传x-json:{}，有效字段为x-json:后的字段
        :type ExtendTwo: str
        :param _Echo: 透传信息，若为json格式，需传x-json:{}，有效字段为x-json:后的字段
        :type Echo: str
        """
        self._WorkspaceId = None
        self._Profile = None
        self._ReportTs = None
        self._Properties = None
        self._ApplicationToken = None
        self._EventSet = None
        self._ServiceSet = None
        self._ExtendTwo = None
        self._Echo = None

    @property
    def WorkspaceId(self):
        """工作空间Id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Profile(self):
        """消息定义
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.MessageProfile`
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def ReportTs(self):
        """数据上报时间
        :rtype: int
        """
        return self._ReportTs

    @ReportTs.setter
    def ReportTs(self, ReportTs):
        self._ReportTs = ReportTs

    @property
    def Properties(self):
        """属性定义 - KV的json格式,有效字段为x-json:后的字段
        :rtype: str
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def EventSet(self):
        """事件定义 - KKV的json格式,有效字段为x-json:后的字段
        :rtype: str
        """
        return self._EventSet

    @EventSet.setter
    def EventSet(self, EventSet):
        self._EventSet = EventSet

    @property
    def ServiceSet(self):
        """服务定义 - KKV的json格式,有效字段为x-json:后的字段
        :rtype: str
        """
        return self._ServiceSet

    @ServiceSet.setter
    def ServiceSet(self, ServiceSet):
        self._ServiceSet = ServiceSet

    @property
    def ExtendTwo(self):
        """扩展字段2，如：算法上报id，若为json格式，需传x-json:{}，有效字段为x-json:后的字段
        :rtype: str
        """
        return self._ExtendTwo

    @ExtendTwo.setter
    def ExtendTwo(self, ExtendTwo):
        self._ExtendTwo = ExtendTwo

    @property
    def Echo(self):
        """透传信息，若为json格式，需传x-json:{}，有效字段为x-json:后的字段
        :rtype: str
        """
        return self._Echo

    @Echo.setter
    def Echo(self, Echo):
        self._Echo = Echo


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        if params.get("Profile") is not None:
            self._Profile = MessageProfile()
            self._Profile._deserialize(params.get("Profile"))
        self._ReportTs = params.get("ReportTs")
        self._Properties = params.get("Properties")
        self._ApplicationToken = params.get("ApplicationToken")
        self._EventSet = params.get("EventSet")
        self._ServiceSet = params.get("ServiceSet")
        self._ExtendTwo = params.get("ExtendTwo")
        self._Echo = params.get("Echo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportAppMessageResponse(AbstractModel):
    """ReportAppMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 上报单条信息结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """上报单条信息结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = EmptyRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ReportImg(AbstractModel):
    """上报图片列表

    """

    def __init__(self):
        r"""
        :param _Type: 类型
        :type Type: int
        :param _Data: 数据
        :type Data: str
        """
        self._Type = None
        self._Data = None

    @property
    def Type(self):
        """类型
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Data(self):
        """数据
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportMsgRes(AbstractModel):
    """上报消息结果

    """

    def __init__(self):
        r"""
        :param _ReportId: 上报消息对应下标的16位标识Id, 即第几个消息

        :type ReportId: str
        :param _ReportStatus: 上报消息结果，1表示成功推送，0表示推送失败

        :type ReportStatus: int
        """
        self._ReportId = None
        self._ReportStatus = None

    @property
    def ReportId(self):
        """上报消息对应下标的16位标识Id, 即第几个消息

        :rtype: str
        """
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def ReportStatus(self):
        """上报消息结果，1表示成功推送，0表示推送失败

        :rtype: int
        """
        return self._ReportStatus

    @ReportStatus.setter
    def ReportStatus(self, ReportStatus):
        self._ReportStatus = ReportStatus


    def _deserialize(self, params):
        self._ReportId = params.get("ReportId")
        self._ReportStatus = params.get("ReportStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleDetailRes(AbstractModel):
    """规则详情查询结果

    """

    def __init__(self):
        r"""
        :param _RuleId: 联动id
        :type RuleId: int
        :param _RuleName: 联动名称
        :type RuleName: str
        :param _RuleDesc: 联动说明
        :type RuleDesc: str
        :param _ValidType: 1 全天有效，0：固定时间段有效
        :type ValidType: int
        :param _ValidPeriod: 有效期，json字符串（全天有效时为空）
        :type ValidPeriod: str
        :param _BeginDate: 起始时间
        :type BeginDate: str
        :param _EndDate: 结束时间
        :type EndDate: str
        :param _Status: 启用状态。1-启用，0-停用
        :type Status: int
        :param _EventRule: 触发规则，事件的组合
        :type EventRule: str
        :param _EventInfoSet: 事件对象集合
        :type EventInfoSet: list of EventObj
        :param _ActionInfoSet: 动作对象集合
        :type ActionInfoSet: list of ActionObj
        """
        self._RuleId = None
        self._RuleName = None
        self._RuleDesc = None
        self._ValidType = None
        self._ValidPeriod = None
        self._BeginDate = None
        self._EndDate = None
        self._Status = None
        self._EventRule = None
        self._EventInfoSet = None
        self._ActionInfoSet = None

    @property
    def RuleId(self):
        """联动id
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        """联动名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleDesc(self):
        """联动说明
        :rtype: str
        """
        return self._RuleDesc

    @RuleDesc.setter
    def RuleDesc(self, RuleDesc):
        self._RuleDesc = RuleDesc

    @property
    def ValidType(self):
        """1 全天有效，0：固定时间段有效
        :rtype: int
        """
        return self._ValidType

    @ValidType.setter
    def ValidType(self, ValidType):
        self._ValidType = ValidType

    @property
    def ValidPeriod(self):
        """有效期，json字符串（全天有效时为空）
        :rtype: str
        """
        return self._ValidPeriod

    @ValidPeriod.setter
    def ValidPeriod(self, ValidPeriod):
        self._ValidPeriod = ValidPeriod

    @property
    def BeginDate(self):
        """起始时间
        :rtype: str
        """
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def EndDate(self):
        """结束时间
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Status(self):
        """启用状态。1-启用，0-停用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EventRule(self):
        """触发规则，事件的组合
        :rtype: str
        """
        return self._EventRule

    @EventRule.setter
    def EventRule(self, EventRule):
        self._EventRule = EventRule

    @property
    def EventInfoSet(self):
        """事件对象集合
        :rtype: list of EventObj
        """
        return self._EventInfoSet

    @EventInfoSet.setter
    def EventInfoSet(self, EventInfoSet):
        self._EventInfoSet = EventInfoSet

    @property
    def ActionInfoSet(self):
        """动作对象集合
        :rtype: list of ActionObj
        """
        return self._ActionInfoSet

    @ActionInfoSet.setter
    def ActionInfoSet(self, ActionInfoSet):
        self._ActionInfoSet = ActionInfoSet


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._RuleDesc = params.get("RuleDesc")
        self._ValidType = params.get("ValidType")
        self._ValidPeriod = params.get("ValidPeriod")
        self._BeginDate = params.get("BeginDate")
        self._EndDate = params.get("EndDate")
        self._Status = params.get("Status")
        self._EventRule = params.get("EventRule")
        if params.get("EventInfoSet") is not None:
            self._EventInfoSet = []
            for item in params.get("EventInfoSet"):
                obj = EventObj()
                obj._deserialize(item)
                self._EventInfoSet.append(obj)
        if params.get("ActionInfoSet") is not None:
            self._ActionInfoSet = []
            for item in params.get("ActionInfoSet"):
                obj = ActionObj()
                obj._deserialize(item)
                self._ActionInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaveDeviceGroupRequest(AbstractModel):
    """SaveDeviceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 分组名称
        :type Name: str
        :param _Description: 分组描述
        :type Description: str
        :param _WorkspaceId: 空间id
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _Id: 分组id, 携带则为修改, 不携带则为新增
        :type Id: int
        :param _ParentId: 分组父级id
        :type ParentId: int
        """
        self._Name = None
        self._Description = None
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._Id = None
        self._ParentId = None

    @property
    def Name(self):
        """分组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """分组描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def WorkspaceId(self):
        """空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def Id(self):
        """分组id, 携带则为修改, 不携带则为新增
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ParentId(self):
        """分组父级id
        :rtype: int
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        self._Id = params.get("Id")
        self._ParentId = params.get("ParentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaveDeviceGroupRes(AbstractModel):
    """保存or修改设备分组回包

    """

    def __init__(self):
        r"""
        :param _Id: 保存or修改设备分组回包信息
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        """保存or修改设备分组回包信息
        :rtype: int
        """
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
        


class SaveDeviceGroupResponse(AbstractModel):
    """SaveDeviceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 新增/修改的设备分组记录的id
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.SaveDeviceGroupRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """新增/修改的设备分组记录的id
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.SaveDeviceGroupRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = SaveDeviceGroupRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class SceneInfo(AbstractModel):
    """场景信息

    """

    def __init__(self):
        r"""
        :param _SceneId: 场景id
        :type SceneId: str
        :param _SceneName: 场景名称
        :type SceneName: str
        :param _Version: 场景版本
        :type Version: str
        """
        self._SceneId = None
        self._SceneName = None
        self._Version = None

    @property
    def SceneId(self):
        """场景id
        :rtype: str
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

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
    def Version(self):
        """场景版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._SceneId = params.get("SceneId")
        self._SceneName = params.get("SceneName")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SceneListRes(AbstractModel):
    """场景列表响应体

    """

    def __init__(self):
        r"""
        :param _SceneList: 场景列表
        :type SceneList: list of SceneInfo
        """
        self._SceneList = None

    @property
    def SceneList(self):
        """场景列表
        :rtype: list of SceneInfo
        """
        return self._SceneList

    @SceneList.setter
    def SceneList(self, SceneList):
        self._SceneList = SceneList


    def _deserialize(self, params):
        if params.get("SceneList") is not None:
            self._SceneList = []
            for item in params.get("SceneList"):
                obj = SceneInfo()
                obj._deserialize(item)
                self._SceneList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpaceDataListStatsRes(AbstractModel):
    """查询项目空间楼栋数量与建筑面积响应体

    """

    def __init__(self):
        r"""
        :param _List: 楼栋数量与建筑面积列表
        :type List: list of SpaceDataStats
        """
        self._List = None

    @property
    def List(self):
        """楼栋数量与建筑面积列表
        :rtype: list of SpaceDataStats
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = SpaceDataStats()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpaceDataStats(AbstractModel):
    """项目空间楼栋数量与建筑面积出参

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间ID
        :type WorkspaceId: str
        :param _WorkspaceName: 工作空间名称
        :type WorkspaceName: str
        :param _BuildingCount: 楼栋数量
        :type BuildingCount: int
        :param _BuildingArea: 建筑面积
        :type BuildingArea: float
        """
        self._WorkspaceId = None
        self._WorkspaceName = None
        self._BuildingCount = None
        self._BuildingArea = None

    @property
    def WorkspaceId(self):
        """工作空间ID
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def WorkspaceName(self):
        """工作空间名称
        :rtype: str
        """
        return self._WorkspaceName

    @WorkspaceName.setter
    def WorkspaceName(self, WorkspaceName):
        self._WorkspaceName = WorkspaceName

    @property
    def BuildingCount(self):
        """楼栋数量
        :rtype: int
        """
        return self._BuildingCount

    @BuildingCount.setter
    def BuildingCount(self, BuildingCount):
        self._BuildingCount = BuildingCount

    @property
    def BuildingArea(self):
        """建筑面积
        :rtype: float
        """
        return self._BuildingArea

    @BuildingArea.setter
    def BuildingArea(self, BuildingArea):
        self._BuildingArea = BuildingArea


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._WorkspaceName = params.get("WorkspaceName")
        self._BuildingCount = params.get("BuildingCount")
        self._BuildingArea = params.get("BuildingArea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpaceDataTotalStatsRes(AbstractModel):
    """查询租户楼栋数量和楼栋建筑面积相应体

    """

    def __init__(self):
        r"""
        :param _BuildingCount: 总楼栋数量
        :type BuildingCount: int
        :param _BuildingArea: 总建筑面积
        :type BuildingArea: float
        """
        self._BuildingCount = None
        self._BuildingArea = None

    @property
    def BuildingCount(self):
        """总楼栋数量
        :rtype: int
        """
        return self._BuildingCount

    @BuildingCount.setter
    def BuildingCount(self, BuildingCount):
        self._BuildingCount = BuildingCount

    @property
    def BuildingArea(self):
        """总建筑面积
        :rtype: float
        """
        return self._BuildingArea

    @BuildingArea.setter
    def BuildingArea(self, BuildingArea):
        self._BuildingArea = BuildingArea


    def _deserialize(self, params):
        self._BuildingCount = params.get("BuildingCount")
        self._BuildingArea = params.get("BuildingArea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpaceDeviceIdListRes(AbstractModel):
    """查询指定空间id列表响应

    """

    def __init__(self):
        r"""
        :param _DeviceIds: 设备id列表
        :type DeviceIds: list of str
        """
        self._DeviceIds = None

    @property
    def DeviceIds(self):
        """设备id列表
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
        


class SpaceDeviceRelation(AbstractModel):
    """设备-空间绑定关系

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备id
        :type DeviceId: str
        :param _ElementId: 构件id
        :type ElementId: str
        """
        self._DeviceId = None
        self._ElementId = None

    @property
    def DeviceId(self):
        """设备id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ElementId(self):
        """构件id
        :rtype: str
        """
        return self._ElementId

    @ElementId.setter
    def ElementId(self, ElementId):
        self._ElementId = ElementId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ElementId = params.get("ElementId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpaceDeviceRelationRes(AbstractModel):
    """设备-空间绑定关系响应体

    """

    def __init__(self):
        r"""
        :param _SpaceDeviceRelationList: 设备空间绑定关系列表
        :type SpaceDeviceRelationList: list of SpaceDeviceRelation
        """
        self._SpaceDeviceRelationList = None

    @property
    def SpaceDeviceRelationList(self):
        """设备空间绑定关系列表
        :rtype: list of SpaceDeviceRelation
        """
        return self._SpaceDeviceRelationList

    @SpaceDeviceRelationList.setter
    def SpaceDeviceRelationList(self, SpaceDeviceRelationList):
        self._SpaceDeviceRelationList = SpaceDeviceRelationList


    def _deserialize(self, params):
        if params.get("SpaceDeviceRelationList") is not None:
            self._SpaceDeviceRelationList = []
            for item in params.get("SpaceDeviceRelationList"):
                obj = SpaceDeviceRelation()
                obj._deserialize(item)
                self._SpaceDeviceRelationList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpaceInfo(AbstractModel):
    """项目空间详细信息

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 项目空间id
        :type WorkspaceId: int
        :param _TenantId: 租户id
        :type TenantId: int
        :param _EnglishName: 英文名
        :type EnglishName: str
        :param _ChineseName: 中文名
        :type ChineseName: str
        :param _Description: 项目空间描述
        :type Description: str
        :param _Status: 项目空间状态:0 启用 1 停用 -1 已删除
        :type Status: int
        :param _IsCommWorkspace: 是否是公共空间
        :type IsCommWorkspace: bool
        :param _ValidityStartTime: 有效期开始时间
        :type ValidityStartTime: str
        :param _ValidityEndTime: 有效期结束时间
        :type ValidityEndTime: str
        :param _Selected: 选中状态
        :type Selected: int
        :param _IsSystem: 系统生成状态
        :type IsSystem: int
        """
        self._WorkspaceId = None
        self._TenantId = None
        self._EnglishName = None
        self._ChineseName = None
        self._Description = None
        self._Status = None
        self._IsCommWorkspace = None
        self._ValidityStartTime = None
        self._ValidityEndTime = None
        self._Selected = None
        self._IsSystem = None

    @property
    def WorkspaceId(self):
        """项目空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def TenantId(self):
        """租户id
        :rtype: int
        """
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def EnglishName(self):
        """英文名
        :rtype: str
        """
        return self._EnglishName

    @EnglishName.setter
    def EnglishName(self, EnglishName):
        self._EnglishName = EnglishName

    @property
    def ChineseName(self):
        """中文名
        :rtype: str
        """
        return self._ChineseName

    @ChineseName.setter
    def ChineseName(self, ChineseName):
        self._ChineseName = ChineseName

    @property
    def Description(self):
        """项目空间描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        """项目空间状态:0 启用 1 停用 -1 已删除
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsCommWorkspace(self):
        """是否是公共空间
        :rtype: bool
        """
        return self._IsCommWorkspace

    @IsCommWorkspace.setter
    def IsCommWorkspace(self, IsCommWorkspace):
        self._IsCommWorkspace = IsCommWorkspace

    @property
    def ValidityStartTime(self):
        """有效期开始时间
        :rtype: str
        """
        return self._ValidityStartTime

    @ValidityStartTime.setter
    def ValidityStartTime(self, ValidityStartTime):
        self._ValidityStartTime = ValidityStartTime

    @property
    def ValidityEndTime(self):
        """有效期结束时间
        :rtype: str
        """
        return self._ValidityEndTime

    @ValidityEndTime.setter
    def ValidityEndTime(self, ValidityEndTime):
        self._ValidityEndTime = ValidityEndTime

    @property
    def Selected(self):
        """选中状态
        :rtype: int
        """
        return self._Selected

    @Selected.setter
    def Selected(self, Selected):
        self._Selected = Selected

    @property
    def IsSystem(self):
        """系统生成状态
        :rtype: int
        """
        return self._IsSystem

    @IsSystem.setter
    def IsSystem(self, IsSystem):
        self._IsSystem = IsSystem


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._TenantId = params.get("TenantId")
        self._EnglishName = params.get("EnglishName")
        self._ChineseName = params.get("ChineseName")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._IsCommWorkspace = params.get("IsCommWorkspace")
        self._ValidityStartTime = params.get("ValidityStartTime")
        self._ValidityEndTime = params.get("ValidityEndTime")
        self._Selected = params.get("Selected")
        self._IsSystem = params.get("IsSystem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpaceRelation(AbstractModel):
    """空间层级关系

    """

    def __init__(self):
        r"""
        :param _ElementId: 构件id
        :type ElementId: str
        :param _ElementName: 构件名称
        :type ElementName: str
        :param _Level: 空间层级
        :type Level: int
        :param _SpaceCode: 空间编码
        :type SpaceCode: str
        :param _ParentSpaceCode: 父级空间编码
        :type ParentSpaceCode: str
        :param _Children: 子构件信息
        :type Children: list of SpaceRelation
        """
        self._ElementId = None
        self._ElementName = None
        self._Level = None
        self._SpaceCode = None
        self._ParentSpaceCode = None
        self._Children = None

    @property
    def ElementId(self):
        """构件id
        :rtype: str
        """
        return self._ElementId

    @ElementId.setter
    def ElementId(self, ElementId):
        self._ElementId = ElementId

    @property
    def ElementName(self):
        """构件名称
        :rtype: str
        """
        return self._ElementName

    @ElementName.setter
    def ElementName(self, ElementName):
        self._ElementName = ElementName

    @property
    def Level(self):
        """空间层级
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def SpaceCode(self):
        """空间编码
        :rtype: str
        """
        return self._SpaceCode

    @SpaceCode.setter
    def SpaceCode(self, SpaceCode):
        self._SpaceCode = SpaceCode

    @property
    def ParentSpaceCode(self):
        """父级空间编码
        :rtype: str
        """
        return self._ParentSpaceCode

    @ParentSpaceCode.setter
    def ParentSpaceCode(self, ParentSpaceCode):
        self._ParentSpaceCode = ParentSpaceCode

    @property
    def Children(self):
        """子构件信息
        :rtype: list of SpaceRelation
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children


    def _deserialize(self, params):
        self._ElementId = params.get("ElementId")
        self._ElementName = params.get("ElementName")
        self._Level = params.get("Level")
        self._SpaceCode = params.get("SpaceCode")
        self._ParentSpaceCode = params.get("ParentSpaceCode")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = SpaceRelation()
                obj._deserialize(item)
                self._Children.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpaceRelationRes(AbstractModel):
    """空间层级关系响应体

    """

    def __init__(self):
        r"""
        :param _SpaceRelation: 空间层级关系
        :type SpaceRelation: :class:`tencentcloud.weilingwith.v20230427.models.SpaceRelation`
        """
        self._SpaceRelation = None

    @property
    def SpaceRelation(self):
        """空间层级关系
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.SpaceRelation`
        """
        return self._SpaceRelation

    @SpaceRelation.setter
    def SpaceRelation(self, SpaceRelation):
        self._SpaceRelation = SpaceRelation


    def _deserialize(self, params):
        if params.get("SpaceRelation") is not None:
            self._SpaceRelation = SpaceRelation()
            self._SpaceRelation._deserialize(params.get("SpaceRelation"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpaceType(AbstractModel):
    """空间分类

    """

    def __init__(self):
        r"""
        :param _SpaceTypeCode: 空间分类编码
        :type SpaceTypeCode: str
        :param _SpaceTypeName: 空间分类名称
        :type SpaceTypeName: str
        """
        self._SpaceTypeCode = None
        self._SpaceTypeName = None

    @property
    def SpaceTypeCode(self):
        """空间分类编码
        :rtype: str
        """
        return self._SpaceTypeCode

    @SpaceTypeCode.setter
    def SpaceTypeCode(self, SpaceTypeCode):
        self._SpaceTypeCode = SpaceTypeCode

    @property
    def SpaceTypeName(self):
        """空间分类名称
        :rtype: str
        """
        return self._SpaceTypeName

    @SpaceTypeName.setter
    def SpaceTypeName(self, SpaceTypeName):
        self._SpaceTypeName = SpaceTypeName


    def _deserialize(self, params):
        self._SpaceTypeCode = params.get("SpaceTypeCode")
        self._SpaceTypeName = params.get("SpaceTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpaceTypeListRes(AbstractModel):
    """空间分类列表响应体

    """

    def __init__(self):
        r"""
        :param _SpaceTypeList: 空间分类列表
        :type SpaceTypeList: list of SpaceType
        """
        self._SpaceTypeList = None

    @property
    def SpaceTypeList(self):
        """空间分类列表
        :rtype: list of SpaceType
        """
        return self._SpaceTypeList

    @SpaceTypeList.setter
    def SpaceTypeList(self, SpaceTypeList):
        self._SpaceTypeList = SpaceTypeList


    def _deserialize(self, params):
        if params.get("SpaceTypeList") is not None:
            self._SpaceTypeList = []
            for item in params.get("SpaceTypeList"):
                obj = SpaceType()
                obj._deserialize(item)
                self._SpaceTypeList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SsoDepartment(AbstractModel):
    """部门用户

    """

    def __init__(self):
        r"""
        :param _DepartmentId: 部门ID
        :type DepartmentId: str
        :param _Name: 部门名称
        :type Name: str
        :param _ParentDepartmentId: 父级部门ID
        :type ParentDepartmentId: str
        """
        self._DepartmentId = None
        self._Name = None
        self._ParentDepartmentId = None

    @property
    def DepartmentId(self):
        """部门ID
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def Name(self):
        """部门名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParentDepartmentId(self):
        """父级部门ID
        :rtype: str
        """
        return self._ParentDepartmentId

    @ParentDepartmentId.setter
    def ParentDepartmentId(self, ParentDepartmentId):
        self._ParentDepartmentId = ParentDepartmentId


    def _deserialize(self, params):
        self._DepartmentId = params.get("DepartmentId")
        self._Name = params.get("Name")
        self._ParentDepartmentId = params.get("ParentDepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SsoDepartmentsResult(AbstractModel):
    """部门用户结果

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Departments: 部门列表
        :type Departments: list of SsoDepartment
        """
        self._Total = None
        self._Departments = None

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
    def Departments(self):
        """部门列表
        :rtype: list of SsoDepartment
        """
        return self._Departments

    @Departments.setter
    def Departments(self, Departments):
        self._Departments = Departments


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Departments") is not None:
            self._Departments = []
            for item in params.get("Departments"):
                obj = SsoDepartment()
                obj._deserialize(item)
                self._Departments.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SsoTeamUser(AbstractModel):
    """部门用户

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        :param _RealName: 用户名称
        :type RealName: str
        :param _UserType: 用户类型，1-超级管理员；2-1号管理员；3-普通管理员；99-普通用户
        :type UserType: str
        :param _TenantId: 所属租户ID
        :type TenantId: str
        :param _Email: 邮箱
        :type Email: str
        :param _Phone: 电话
        :type Phone: str
        :param _Status: 用户状态
        :type Status: int
        :param _CreateAt: 创建时间
        :type CreateAt: int
        :param _DepartmentId: 部门ID
        :type DepartmentId: str
        :param _DepartmentName: 部门名称
        :type DepartmentName: str
        :param _LinkFilter: 是否关联权限
        :type LinkFilter: int
        """
        self._UserId = None
        self._RealName = None
        self._UserType = None
        self._TenantId = None
        self._Email = None
        self._Phone = None
        self._Status = None
        self._CreateAt = None
        self._DepartmentId = None
        self._DepartmentName = None
        self._LinkFilter = None

    @property
    def UserId(self):
        """用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RealName(self):
        """用户名称
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def UserType(self):
        """用户类型，1-超级管理员；2-1号管理员；3-普通管理员；99-普通用户
        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def TenantId(self):
        """所属租户ID
        :rtype: str
        """
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def Email(self):
        """邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Phone(self):
        """电话
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Status(self):
        """用户状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateAt(self):
        """创建时间
        :rtype: int
        """
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def DepartmentId(self):
        """部门ID
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def DepartmentName(self):
        """部门名称
        :rtype: str
        """
        return self._DepartmentName

    @DepartmentName.setter
    def DepartmentName(self, DepartmentName):
        self._DepartmentName = DepartmentName

    @property
    def LinkFilter(self):
        """是否关联权限
        :rtype: int
        """
        return self._LinkFilter

    @LinkFilter.setter
    def LinkFilter(self, LinkFilter):
        self._LinkFilter = LinkFilter


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._RealName = params.get("RealName")
        self._UserType = params.get("UserType")
        self._TenantId = params.get("TenantId")
        self._Email = params.get("Email")
        self._Phone = params.get("Phone")
        self._Status = params.get("Status")
        self._CreateAt = params.get("CreateAt")
        self._DepartmentId = params.get("DepartmentId")
        self._DepartmentName = params.get("DepartmentName")
        self._LinkFilter = params.get("LinkFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SsoTeamUserResult(AbstractModel):
    """空间用户结果

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Users: 部门用户列表
        :type Users: list of SsoTeamUser
        """
        self._Total = None
        self._Users = None

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
    def Users(self):
        """部门用户列表
        :rtype: list of SsoTeamUser
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = SsoTeamUser()
                obj._deserialize(item)
                self._Users.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SsoUser(AbstractModel):
    """用户结果

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        :param _UserName: 用户昵称
        :type UserName: str
        :param _RealName: 用户名称
        :type RealName: str
        :param _UserType: 用户类型，1-超级管理员；2-1号管理员；3-普通管理员；99-普通用户
        :type UserType: str
        :param _TenantId: 所属租户ID
        :type TenantId: str
        :param _UserGroup: 所属组ID
        :type UserGroup: str
        :param _Email: 邮箱
        :type Email: str
        :param _Phone: 电话
        :type Phone: str
        :param _Status: 用户状态，0待审核，1正常启用，2禁用
        :type Status: int
        :param _CreateAt: 创建时间
        :type CreateAt: int
        :param _UpdateAt: 更新时间
        :type UpdateAt: int
        :param _BelongTeam: 是否属于团队，0不可用，1属于，2不属
        :type BelongTeam: int
        :param _DepartmentId: 部门ID
        :type DepartmentId: str
        :param _DepartmentName: 部门名称
        :type DepartmentName: str
        :param _DepartmentUserId: 子账户ID
        :type DepartmentUserId: int
        :param _Password: 密码
        :type Password: str
        """
        self._UserId = None
        self._UserName = None
        self._RealName = None
        self._UserType = None
        self._TenantId = None
        self._UserGroup = None
        self._Email = None
        self._Phone = None
        self._Status = None
        self._CreateAt = None
        self._UpdateAt = None
        self._BelongTeam = None
        self._DepartmentId = None
        self._DepartmentName = None
        self._DepartmentUserId = None
        self._Password = None

    @property
    def UserId(self):
        """用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        """用户昵称
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        """用户名称
        :rtype: str
        """
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def UserType(self):
        """用户类型，1-超级管理员；2-1号管理员；3-普通管理员；99-普通用户
        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def TenantId(self):
        """所属租户ID
        :rtype: str
        """
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def UserGroup(self):
        """所属组ID
        :rtype: str
        """
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def Email(self):
        """邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Phone(self):
        """电话
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Status(self):
        """用户状态，0待审核，1正常启用，2禁用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateAt(self):
        """创建时间
        :rtype: int
        """
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        """更新时间
        :rtype: int
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt

    @property
    def BelongTeam(self):
        """是否属于团队，0不可用，1属于，2不属
        :rtype: int
        """
        return self._BelongTeam

    @BelongTeam.setter
    def BelongTeam(self, BelongTeam):
        self._BelongTeam = BelongTeam

    @property
    def DepartmentId(self):
        """部门ID
        :rtype: str
        """
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def DepartmentName(self):
        """部门名称
        :rtype: str
        """
        return self._DepartmentName

    @DepartmentName.setter
    def DepartmentName(self, DepartmentName):
        self._DepartmentName = DepartmentName

    @property
    def DepartmentUserId(self):
        """子账户ID
        :rtype: int
        """
        return self._DepartmentUserId

    @DepartmentUserId.setter
    def DepartmentUserId(self, DepartmentUserId):
        self._DepartmentUserId = DepartmentUserId

    @property
    def Password(self):
        """密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._RealName = params.get("RealName")
        self._UserType = params.get("UserType")
        self._TenantId = params.get("TenantId")
        self._UserGroup = params.get("UserGroup")
        self._Email = params.get("Email")
        self._Phone = params.get("Phone")
        self._Status = params.get("Status")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        self._BelongTeam = params.get("BelongTeam")
        self._DepartmentId = params.get("DepartmentId")
        self._DepartmentName = params.get("DepartmentName")
        self._DepartmentUserId = params.get("DepartmentUserId")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SsoUserResult(AbstractModel):
    """租户人员结果

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Users: 租户人员数据
        :type Users: list of SsoUser
        """
        self._Total = None
        self._Users = None

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
    def Users(self):
        """租户人员数据
        :rtype: list of SsoUser
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = SsoUser()
                obj._deserialize(item)
                self._Users.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatDeviceType(AbstractModel):
    """设备类型统计

    """

    def __init__(self):
        r"""
        :param _Total: 汇总数。在线（正常+故障） + 离线
        :type Total: int
        :param _Normal: 正常数
        :type Normal: int
        :param _Offline: 离线数
        :type Offline: int
        :param _Fault: 故障数
        :type Fault: int
        :param _Name: 设备名
        :type Name: str
        :param _DeviceType: 设备类型
        :type DeviceType: str
        """
        self._Total = None
        self._Normal = None
        self._Offline = None
        self._Fault = None
        self._Name = None
        self._DeviceType = None

    @property
    def Total(self):
        """汇总数。在线（正常+故障） + 离线
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Normal(self):
        """正常数
        :rtype: int
        """
        return self._Normal

    @Normal.setter
    def Normal(self, Normal):
        self._Normal = Normal

    @property
    def Offline(self):
        """离线数
        :rtype: int
        """
        return self._Offline

    @Offline.setter
    def Offline(self, Offline):
        self._Offline = Offline

    @property
    def Fault(self):
        """故障数
        :rtype: int
        """
        return self._Fault

    @Fault.setter
    def Fault(self, Fault):
        self._Fault = Fault

    @property
    def Name(self):
        """设备名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DeviceType(self):
        """设备类型
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Normal = params.get("Normal")
        self._Offline = params.get("Offline")
        self._Fault = params.get("Fault")
        self._Name = params.get("Name")
        self._DeviceType = params.get("DeviceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatLevel(AbstractModel):
    """层级统计

    """

    def __init__(self):
        r"""
        :param _Total: 汇总数。在线（正常+故障） + 离线
        :type Total: int
        :param _NormalSum: 正常数
        :type NormalSum: int
        :param _OfflineSum: 离线数
        :type OfflineSum: int
        :param _FaultSum: 故障数
        :type FaultSum: int
        :param _SpaceCode: 空间id
        :type SpaceCode: str
        :param _StatDeviceTypeSet: 设备类型统计列表
        :type StatDeviceTypeSet: list of StatDeviceType
        """
        self._Total = None
        self._NormalSum = None
        self._OfflineSum = None
        self._FaultSum = None
        self._SpaceCode = None
        self._StatDeviceTypeSet = None

    @property
    def Total(self):
        """汇总数。在线（正常+故障） + 离线
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def NormalSum(self):
        """正常数
        :rtype: int
        """
        return self._NormalSum

    @NormalSum.setter
    def NormalSum(self, NormalSum):
        self._NormalSum = NormalSum

    @property
    def OfflineSum(self):
        """离线数
        :rtype: int
        """
        return self._OfflineSum

    @OfflineSum.setter
    def OfflineSum(self, OfflineSum):
        self._OfflineSum = OfflineSum

    @property
    def FaultSum(self):
        """故障数
        :rtype: int
        """
        return self._FaultSum

    @FaultSum.setter
    def FaultSum(self, FaultSum):
        self._FaultSum = FaultSum

    @property
    def SpaceCode(self):
        """空间id
        :rtype: str
        """
        return self._SpaceCode

    @SpaceCode.setter
    def SpaceCode(self, SpaceCode):
        self._SpaceCode = SpaceCode

    @property
    def StatDeviceTypeSet(self):
        """设备类型统计列表
        :rtype: list of StatDeviceType
        """
        return self._StatDeviceTypeSet

    @StatDeviceTypeSet.setter
    def StatDeviceTypeSet(self, StatDeviceTypeSet):
        self._StatDeviceTypeSet = StatDeviceTypeSet


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._NormalSum = params.get("NormalSum")
        self._OfflineSum = params.get("OfflineSum")
        self._FaultSum = params.get("FaultSum")
        self._SpaceCode = params.get("SpaceCode")
        if params.get("StatDeviceTypeSet") is not None:
            self._StatDeviceTypeSet = []
            for item in params.get("StatDeviceTypeSet"):
                obj = StatDeviceType()
                obj._deserialize(item)
                self._StatDeviceTypeSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopVideoStreamingRequest(AbstractModel):
    """StopVideoStreaming请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Stream: 流的唯一标识，播放链接尾缀
        :type Stream: str
        :param _WID: 设备的唯一标识

        :type WID: str
        :param _WorkspaceId: 工作空间Id
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        """
        self._Stream = None
        self._WID = None
        self._WorkspaceId = None
        self._ApplicationToken = None

    @property
    def Stream(self):
        """流的唯一标识，播放链接尾缀
        :rtype: str
        """
        return self._Stream

    @Stream.setter
    def Stream(self, Stream):
        self._Stream = Stream

    @property
    def WID(self):
        """设备的唯一标识

        :rtype: str
        """
        return self._WID

    @WID.setter
    def WID(self, WID):
        self._WID = WID

    @property
    def WorkspaceId(self):
        """工作空间Id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken


    def _deserialize(self, params):
        self._Stream = params.get("Stream")
        self._WID = params.get("WID")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopVideoStreamingResponse(AbstractModel):
    """StopVideoStreaming返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 停流接口返回结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """停流接口返回结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = EmptyRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class UpdateWorkspaceParkAttributesRequest(AbstractModel):
    """UpdateWorkspaceParkAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        :param _ApplicationToken: 应用token
        :type ApplicationToken: str
        :param _ParkName: 园区简称
        :type ParkName: str
        :param _ParkNum: 园区编号
        :type ParkNum: str
        """
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._ParkName = None
        self._ParkNum = None

    @property
    def WorkspaceId(self):
        """工作空间id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        """应用token
        :rtype: str
        """
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def ParkName(self):
        """园区简称
        :rtype: str
        """
        return self._ParkName

    @ParkName.setter
    def ParkName(self, ParkName):
        self._ParkName = ParkName

    @property
    def ParkNum(self):
        """园区编号
        :rtype: str
        """
        return self._ParkNum

    @ParkNum.setter
    def ParkNum(self, ParkNum):
        self._ParkNum = ParkNum


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        self._ParkName = params.get("ParkName")
        self._ParkNum = params.get("ParkNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateWorkspaceParkAttributesResponse(AbstractModel):
    """UpdateWorkspaceParkAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 修改工作空间园区属性结果
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """修改工作空间园区属性结果
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.EmptyRes`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = EmptyRes()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class VideoCloudRecordRes(AbstractModel):
    """云录像接口结果

    """

    def __init__(self):
        r"""
        :param _TotalCount: 录像信息总数
        :type TotalCount: int
        :param _RecordSet: 录像信息列表
        :type RecordSet: list of RecordInfo
        """
        self._TotalCount = None
        self._RecordSet = None

    @property
    def TotalCount(self):
        """录像信息总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RecordSet(self):
        """录像信息列表
        :rtype: list of RecordInfo
        """
        return self._RecordSet

    @RecordSet.setter
    def RecordSet(self, RecordSet):
        self._RecordSet = RecordSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RecordSet") is not None:
            self._RecordSet = []
            for item in params.get("RecordSet"):
                obj = RecordInfo()
                obj._deserialize(item)
                self._RecordSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoRecordStreamRes(AbstractModel):
    """视频流查询结果

    """

    def __init__(self):
        r"""
        :param _FLV: FLV协议格式视频流
        :type FLV: str
        :param _RTMP: RTMP协议格式视频流
        :type RTMP: str
        :param _HLS: HLS协议格式视频流
        :type HLS: str
        :param _WebRTC: WebRtc协议格式视频流
        :type WebRTC: str
        :param _RAW: RAW协议格式视频流
        :type RAW: :class:`tencentcloud.weilingwith.v20230427.models.RawInfo`
        :param _Stream: 视频流的唯一标识
        :type Stream: str
        """
        self._FLV = None
        self._RTMP = None
        self._HLS = None
        self._WebRTC = None
        self._RAW = None
        self._Stream = None

    @property
    def FLV(self):
        """FLV协议格式视频流
        :rtype: str
        """
        return self._FLV

    @FLV.setter
    def FLV(self, FLV):
        self._FLV = FLV

    @property
    def RTMP(self):
        """RTMP协议格式视频流
        :rtype: str
        """
        return self._RTMP

    @RTMP.setter
    def RTMP(self, RTMP):
        self._RTMP = RTMP

    @property
    def HLS(self):
        """HLS协议格式视频流
        :rtype: str
        """
        return self._HLS

    @HLS.setter
    def HLS(self, HLS):
        self._HLS = HLS

    @property
    def WebRTC(self):
        """WebRtc协议格式视频流
        :rtype: str
        """
        return self._WebRTC

    @WebRTC.setter
    def WebRTC(self, WebRTC):
        self._WebRTC = WebRTC

    @property
    def RAW(self):
        """RAW协议格式视频流
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.RawInfo`
        """
        return self._RAW

    @RAW.setter
    def RAW(self, RAW):
        self._RAW = RAW

    @property
    def Stream(self):
        """视频流的唯一标识
        :rtype: str
        """
        return self._Stream

    @Stream.setter
    def Stream(self, Stream):
        self._Stream = Stream


    def _deserialize(self, params):
        self._FLV = params.get("FLV")
        self._RTMP = params.get("RTMP")
        self._HLS = params.get("HLS")
        self._WebRTC = params.get("WebRTC")
        if params.get("RAW") is not None:
            self._RAW = RawInfo()
            self._RAW._deserialize(params.get("RAW"))
        self._Stream = params.get("Stream")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceInfo(AbstractModel):
    """工作空间信息描述

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间Id
        :type WorkspaceId: int
        :param _ChineseName: 工作空间中文名字
        :type ChineseName: str
        :param _Description: 工作空间描述
        :type Description: str
        :param _Status: 工作空间是否删除状态
        :type Status: int
        :param _ParkName: 该工作空间绑定的区/县的行政区名字
        :type ParkName: str
        :param _ParkNum: 该工作空间绑定的区/县的行政区编码
        :type ParkNum: str
        :param _AdministrativeDetailSet: 获取该工作空间绑定的区/县的上级行政区划信息
        :type AdministrativeDetailSet: list of AdministrativeDetail
        """
        self._WorkspaceId = None
        self._ChineseName = None
        self._Description = None
        self._Status = None
        self._ParkName = None
        self._ParkNum = None
        self._AdministrativeDetailSet = None

    @property
    def WorkspaceId(self):
        """工作空间Id
        :rtype: int
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ChineseName(self):
        """工作空间中文名字
        :rtype: str
        """
        return self._ChineseName

    @ChineseName.setter
    def ChineseName(self, ChineseName):
        self._ChineseName = ChineseName

    @property
    def Description(self):
        """工作空间描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        """工作空间是否删除状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ParkName(self):
        """该工作空间绑定的区/县的行政区名字
        :rtype: str
        """
        return self._ParkName

    @ParkName.setter
    def ParkName(self, ParkName):
        self._ParkName = ParkName

    @property
    def ParkNum(self):
        """该工作空间绑定的区/县的行政区编码
        :rtype: str
        """
        return self._ParkNum

    @ParkNum.setter
    def ParkNum(self, ParkNum):
        self._ParkNum = ParkNum

    @property
    def AdministrativeDetailSet(self):
        """获取该工作空间绑定的区/县的上级行政区划信息
        :rtype: list of AdministrativeDetail
        """
        return self._AdministrativeDetailSet

    @AdministrativeDetailSet.setter
    def AdministrativeDetailSet(self, AdministrativeDetailSet):
        self._AdministrativeDetailSet = AdministrativeDetailSet


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._ChineseName = params.get("ChineseName")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._ParkName = params.get("ParkName")
        self._ParkNum = params.get("ParkNum")
        if params.get("AdministrativeDetailSet") is not None:
            self._AdministrativeDetailSet = []
            for item in params.get("AdministrativeDetailSet"):
                obj = AdministrativeDetail()
                obj._deserialize(item)
                self._AdministrativeDetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceInfoList(AbstractModel):
    """项目空间列表

    """

    def __init__(self):
        r"""
        :param _List: 项目空间列表
        :type List: list of SpaceInfo
        """
        self._List = None

    @property
    def List(self):
        """项目空间列表
        :rtype: list of SpaceInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = SpaceInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        