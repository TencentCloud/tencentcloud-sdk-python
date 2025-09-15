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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AggregationObj(AbstractModel):
    r"""聚合类型

    """

    def __init__(self):
        r"""
        :param _Type: 类型
        :type Type: str
        :param _Bucket: 数组
        :type Bucket: list of Bucket
        """
        self._Type = None
        self._Bucket = None

    @property
    def Type(self):
        r"""类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Bucket(self):
        r"""数组
        :rtype: list of Bucket
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("Bucket") is not None:
            self._Bucket = []
            for item in params.get("Bucket"):
                obj = Bucket()
                obj._deserialize(item)
                self._Bucket.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlarmInfoRsp(AbstractModel):
    r"""用户威胁告警信息

    """

    def __init__(self):
        r"""
        :param _AttackEvent: 近7天威胁告警
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackEvent: list of AttackEvent
        """
        self._AttackEvent = None

    @property
    def AttackEvent(self):
        r"""近7天威胁告警
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AttackEvent
        """
        return self._AttackEvent

    @AttackEvent.setter
    def AttackEvent(self, AttackEvent):
        self._AttackEvent = AttackEvent


    def _deserialize(self, params):
        if params.get("AttackEvent") is not None:
            self._AttackEvent = []
            for item in params.get("AttackEvent"):
                obj = AttackEvent()
                obj._deserialize(item)
                self._AttackEvent.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertDetail(AbstractModel):
    r"""告警详情

    """

    def __init__(self):
        r"""
        :param _BaseInfo: 告警基础信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BaseInfo: :class:`tencentcloud.ssa.v20180608.models.AlertType`
        :param _Detail: 告警详情，json序列化
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: str
        """
        self._BaseInfo = None
        self._Detail = None

    @property
    def BaseInfo(self):
        r"""告警基础信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssa.v20180608.models.AlertType`
        """
        return self._BaseInfo

    @BaseInfo.setter
    def BaseInfo(self, BaseInfo):
        self._BaseInfo = BaseInfo

    @property
    def Detail(self):
        r"""告警详情，json序列化
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail


    def _deserialize(self, params):
        if params.get("BaseInfo") is not None:
            self._BaseInfo = AlertType()
            self._BaseInfo._deserialize(params.get("BaseInfo"))
        self._Detail = params.get("Detail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertListAggregations(AbstractModel):
    r"""空Aggregations结构体

    """

    def __init__(self):
        r"""
        :param _Name: 名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertListData(AbstractModel):
    r"""告警列表响应数据

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _AlertList: 返回列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertList: list of AlertType
        :param _Aggregations: 聚合参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Aggregations: :class:`tencentcloud.ssa.v20180608.models.AlertListAggregations`
        """
        self._Total = None
        self._AlertList = None
        self._Aggregations = None

    @property
    def Total(self):
        r"""总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AlertList(self):
        r"""返回列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AlertType
        """
        return self._AlertList

    @AlertList.setter
    def AlertList(self, AlertList):
        self._AlertList = AlertList

    @property
    def Aggregations(self):
        r"""聚合参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssa.v20180608.models.AlertListAggregations`
        """
        return self._Aggregations

    @Aggregations.setter
    def Aggregations(self, Aggregations):
        self._Aggregations = Aggregations


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("AlertList") is not None:
            self._AlertList = []
            for item in params.get("AlertList"):
                obj = AlertType()
                obj._deserialize(item)
                self._AlertList.append(obj)
        if params.get("Aggregations") is not None:
            self._Aggregations = AlertListAggregations()
            self._Aggregations._deserialize(params.get("Aggregations"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertType(AbstractModel):
    r"""告警字段

    """

    def __init__(self):
        r"""
        :param _AlertTime: 标准时间格式
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertTime: str
        :param _AlertId: 唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertId: str
        :param _AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param _AssetPrivateIp: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetPrivateIp: list of str
        :param _AlertName: 名字
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertName: str
        :param _Level: 告警级别  0:未知 1:低危 2:中危 3:高危 4:严重
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Source: 来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _AttackChain: 攻击字段1
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackChain: str
        :param _AttackId: 攻击字段2
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackId: str
        :param _Concerns: 关注点
注意：此字段可能返回 null，表示取不到有效值。
        :type Concerns: list of ConcernInfo
        :param _Action: 1：已防御，0,2：仅检测(0:告警类 1:拦截类 2:放行类 )
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: int
        :param _AttackResult: 0/空：未知，1：未成功，2：成功
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackResult: int
        :param _EventStatus: //调查状态  0/空：未启用，1：调查中，2：完成调查
注意：此字段可能返回 null，表示取不到有效值。
        :type EventStatus: int
        :param _EventId: //关联事件ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: str
        :param _Status: //处置状态  0：未关闭，1：已关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param _ConcernMaliciousCount: 恶意实体
注意：此字段可能返回 null，表示取不到有效值。
        :type ConcernMaliciousCount: int
        :param _ConcernVictimCount: 受害者实体
注意：此字段可能返回 null，表示取不到有效值。
        :type ConcernVictimCount: int
        :param _VictimAssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VictimAssetType: str
        :param _SubType: 告警子类
注意：此字段可能返回 null，表示取不到有效值。
        :type SubType: str
        :param _AttackName: 攻击技术名字
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackName: str
        :param _AssetPublicIp: 外网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetPublicIp: list of str
        :param _AttackTactic: 攻击战术名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackTactic: str
        :param _VictimAssetSub: 资产子网
注意：此字段可能返回 null，表示取不到有效值。
        :type VictimAssetSub: str
        :param _VictimAssetVpc: 资产vpc
注意：此字段可能返回 null，表示取不到有效值。
        :type VictimAssetVpc: str
        :param _Timestamp: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param _AssetGroupName: 资产组名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetGroupName: list of str
        :param _AssetProjectName: 资产项目名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetProjectName: str
        :param _VictimAssetContent: 失陷资产内容
注意：此字段可能返回 null，表示取不到有效值。
        :type VictimAssetContent: list of str
        :param _WrongReportStatus: 错误报告状态
注意：此字段可能返回 null，表示取不到有效值。
        :type WrongReportStatus: int
        :param _WrongReportConditionId: 错误报告Id
注意：此字段可能返回 null，表示取不到有效值。
        :type WrongReportConditionId: int
        """
        self._AlertTime = None
        self._AlertId = None
        self._AssetId = None
        self._AssetPrivateIp = None
        self._AlertName = None
        self._Level = None
        self._Type = None
        self._Source = None
        self._AttackChain = None
        self._AttackId = None
        self._Concerns = None
        self._Action = None
        self._AttackResult = None
        self._EventStatus = None
        self._EventId = None
        self._Status = None
        self._AssetName = None
        self._ConcernMaliciousCount = None
        self._ConcernVictimCount = None
        self._VictimAssetType = None
        self._SubType = None
        self._AttackName = None
        self._AssetPublicIp = None
        self._AttackTactic = None
        self._VictimAssetSub = None
        self._VictimAssetVpc = None
        self._Timestamp = None
        self._AssetGroupName = None
        self._AssetProjectName = None
        self._VictimAssetContent = None
        self._WrongReportStatus = None
        self._WrongReportConditionId = None

    @property
    def AlertTime(self):
        r"""标准时间格式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AlertTime

    @AlertTime.setter
    def AlertTime(self, AlertTime):
        self._AlertTime = AlertTime

    @property
    def AlertId(self):
        r"""唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AlertId

    @AlertId.setter
    def AlertId(self, AlertId):
        self._AlertId = AlertId

    @property
    def AssetId(self):
        r"""资产id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetPrivateIp(self):
        r"""内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AssetPrivateIp

    @AssetPrivateIp.setter
    def AssetPrivateIp(self, AssetPrivateIp):
        self._AssetPrivateIp = AssetPrivateIp

    @property
    def AlertName(self):
        r"""名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AlertName

    @AlertName.setter
    def AlertName(self, AlertName):
        self._AlertName = AlertName

    @property
    def Level(self):
        r"""告警级别  0:未知 1:低危 2:中危 3:高危 4:严重
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Type(self):
        r"""类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Source(self):
        r"""来源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def AttackChain(self):
        r"""攻击字段1
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttackChain

    @AttackChain.setter
    def AttackChain(self, AttackChain):
        self._AttackChain = AttackChain

    @property
    def AttackId(self):
        r"""攻击字段2
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttackId

    @AttackId.setter
    def AttackId(self, AttackId):
        self._AttackId = AttackId

    @property
    def Concerns(self):
        r"""关注点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ConcernInfo
        """
        return self._Concerns

    @Concerns.setter
    def Concerns(self, Concerns):
        self._Concerns = Concerns

    @property
    def Action(self):
        r"""1：已防御，0,2：仅检测(0:告警类 1:拦截类 2:放行类 )
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def AttackResult(self):
        r"""0/空：未知，1：未成功，2：成功
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AttackResult

    @AttackResult.setter
    def AttackResult(self, AttackResult):
        self._AttackResult = AttackResult

    @property
    def EventStatus(self):
        r"""//调查状态  0/空：未启用，1：调查中，2：完成调查
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EventStatus

    @EventStatus.setter
    def EventStatus(self, EventStatus):
        self._EventStatus = EventStatus

    @property
    def EventId(self):
        r"""//关联事件ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Status(self):
        r"""//处置状态  0：未关闭，1：已关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AssetName(self):
        r"""资产名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def ConcernMaliciousCount(self):
        r"""恶意实体
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ConcernMaliciousCount

    @ConcernMaliciousCount.setter
    def ConcernMaliciousCount(self, ConcernMaliciousCount):
        self._ConcernMaliciousCount = ConcernMaliciousCount

    @property
    def ConcernVictimCount(self):
        r"""受害者实体
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ConcernVictimCount

    @ConcernVictimCount.setter
    def ConcernVictimCount(self, ConcernVictimCount):
        self._ConcernVictimCount = ConcernVictimCount

    @property
    def VictimAssetType(self):
        r"""资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VictimAssetType

    @VictimAssetType.setter
    def VictimAssetType(self, VictimAssetType):
        self._VictimAssetType = VictimAssetType

    @property
    def SubType(self):
        r"""告警子类
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def AttackName(self):
        r"""攻击技术名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttackName

    @AttackName.setter
    def AttackName(self, AttackName):
        self._AttackName = AttackName

    @property
    def AssetPublicIp(self):
        r"""外网ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AssetPublicIp

    @AssetPublicIp.setter
    def AssetPublicIp(self, AssetPublicIp):
        self._AssetPublicIp = AssetPublicIp

    @property
    def AttackTactic(self):
        r"""攻击战术名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttackTactic

    @AttackTactic.setter
    def AttackTactic(self, AttackTactic):
        self._AttackTactic = AttackTactic

    @property
    def VictimAssetSub(self):
        r"""资产子网
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VictimAssetSub

    @VictimAssetSub.setter
    def VictimAssetSub(self, VictimAssetSub):
        self._VictimAssetSub = VictimAssetSub

    @property
    def VictimAssetVpc(self):
        r"""资产vpc
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VictimAssetVpc

    @VictimAssetVpc.setter
    def VictimAssetVpc(self, VictimAssetVpc):
        self._VictimAssetVpc = VictimAssetVpc

    @property
    def Timestamp(self):
        r"""时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def AssetGroupName(self):
        r"""资产组名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AssetGroupName

    @AssetGroupName.setter
    def AssetGroupName(self, AssetGroupName):
        self._AssetGroupName = AssetGroupName

    @property
    def AssetProjectName(self):
        r"""资产项目名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetProjectName

    @AssetProjectName.setter
    def AssetProjectName(self, AssetProjectName):
        self._AssetProjectName = AssetProjectName

    @property
    def VictimAssetContent(self):
        r"""失陷资产内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._VictimAssetContent

    @VictimAssetContent.setter
    def VictimAssetContent(self, VictimAssetContent):
        self._VictimAssetContent = VictimAssetContent

    @property
    def WrongReportStatus(self):
        r"""错误报告状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._WrongReportStatus

    @WrongReportStatus.setter
    def WrongReportStatus(self, WrongReportStatus):
        self._WrongReportStatus = WrongReportStatus

    @property
    def WrongReportConditionId(self):
        r"""错误报告Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._WrongReportConditionId

    @WrongReportConditionId.setter
    def WrongReportConditionId(self, WrongReportConditionId):
        self._WrongReportConditionId = WrongReportConditionId


    def _deserialize(self, params):
        self._AlertTime = params.get("AlertTime")
        self._AlertId = params.get("AlertId")
        self._AssetId = params.get("AssetId")
        self._AssetPrivateIp = params.get("AssetPrivateIp")
        self._AlertName = params.get("AlertName")
        self._Level = params.get("Level")
        self._Type = params.get("Type")
        self._Source = params.get("Source")
        self._AttackChain = params.get("AttackChain")
        self._AttackId = params.get("AttackId")
        if params.get("Concerns") is not None:
            self._Concerns = []
            for item in params.get("Concerns"):
                obj = ConcernInfo()
                obj._deserialize(item)
                self._Concerns.append(obj)
        self._Action = params.get("Action")
        self._AttackResult = params.get("AttackResult")
        self._EventStatus = params.get("EventStatus")
        self._EventId = params.get("EventId")
        self._Status = params.get("Status")
        self._AssetName = params.get("AssetName")
        self._ConcernMaliciousCount = params.get("ConcernMaliciousCount")
        self._ConcernVictimCount = params.get("ConcernVictimCount")
        self._VictimAssetType = params.get("VictimAssetType")
        self._SubType = params.get("SubType")
        self._AttackName = params.get("AttackName")
        self._AssetPublicIp = params.get("AssetPublicIp")
        self._AttackTactic = params.get("AttackTactic")
        self._VictimAssetSub = params.get("VictimAssetSub")
        self._VictimAssetVpc = params.get("VictimAssetVpc")
        self._Timestamp = params.get("Timestamp")
        self._AssetGroupName = params.get("AssetGroupName")
        self._AssetProjectName = params.get("AssetProjectName")
        self._VictimAssetContent = params.get("VictimAssetContent")
        self._WrongReportStatus = params.get("WrongReportStatus")
        self._WrongReportConditionId = params.get("WrongReportConditionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Asset(AbstractModel):
    r"""资产类型

    """

    def __init__(self):
        r"""
        :param _AssetType: 资产类型
        :type AssetType: str
        :param _Name: 名字
        :type Name: str
        :param _AssetRegionName: 区域
        :type AssetRegionName: str
        :param _AssetVpcid: 所属网络
        :type AssetVpcid: str
        :param _InstanceType: 主机类型
        :type InstanceType: str
        :param _InstanceState: 主机状态
        :type InstanceState: str
        :param _EngineVersion: 引擎版本
        :type EngineVersion: str
        :param _Id: 数据库标识
        :type Id: str
        :param _Tag: 标签
        :type Tag: list of Tag
        :param _AssetCspmRiskNum: 配置风险统计数
        :type AssetCspmRiskNum: int
        :param _PublicIpAddresses: 主机IP
        :type PublicIpAddresses: list of str
        :param _AssetUniqid: 资产唯一标识
        :type AssetUniqid: str
        :param _ChargeType: 付费类型
        :type ChargeType: str
        :param _AssetEventNum: 安全事件统计数
        :type AssetEventNum: int
        :param _AssetVulNum: 漏洞统计数
        :type AssetVulNum: int
        :param _PrivateIpAddresses: 主机IP内网
        :type PrivateIpAddresses: list of str
        :param _GroupName: 所属分组
        :type GroupName: str
        :param _SsaAssetDiscoverTime: 发现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaAssetDiscoverTime: str
        :param _SsaAssetDeleteTime: 下线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaAssetDeleteTime: str
        :param _IsNew: 是否是新增资产
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNew: bool
        :param _AssetSubnetId: 所属子网
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetSubnetId: str
        :param _AssetSubnetName: 子网名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetSubnetName: str
        :param _AssetVpcName: vpc名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetVpcName: str
        :param _ClusterType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: int
        :param _NameSpace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type NameSpace: str
        :param _LoadBalancerType: 负载均衡实例的网络类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerType: str
        :param _LoadBalancerVips: 负载均衡实例的vip列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerVips: list of str
        :param _AssetIpv6: ipv6信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetIpv6: list of str
        :param _SSHRisk: ssh端口暴露风险
注意：此字段可能返回 null，表示取不到有效值。
        :type SSHRisk: str
        :param _RDPRisk: rdp端口暴露风险
注意：此字段可能返回 null，表示取不到有效值。
        :type RDPRisk: str
        :param _EventRisk: 资产失陷事件风险
注意：此字段可能返回 null，表示取不到有效值。
        :type EventRisk: str
        """
        self._AssetType = None
        self._Name = None
        self._AssetRegionName = None
        self._AssetVpcid = None
        self._InstanceType = None
        self._InstanceState = None
        self._EngineVersion = None
        self._Id = None
        self._Tag = None
        self._AssetCspmRiskNum = None
        self._PublicIpAddresses = None
        self._AssetUniqid = None
        self._ChargeType = None
        self._AssetEventNum = None
        self._AssetVulNum = None
        self._PrivateIpAddresses = None
        self._GroupName = None
        self._SsaAssetDiscoverTime = None
        self._SsaAssetDeleteTime = None
        self._IsNew = None
        self._AssetSubnetId = None
        self._AssetSubnetName = None
        self._AssetVpcName = None
        self._ClusterType = None
        self._NameSpace = None
        self._LoadBalancerType = None
        self._LoadBalancerVips = None
        self._AssetIpv6 = None
        self._SSHRisk = None
        self._RDPRisk = None
        self._EventRisk = None

    @property
    def AssetType(self):
        r"""资产类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Name(self):
        r"""名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AssetRegionName(self):
        r"""区域
        :rtype: str
        """
        return self._AssetRegionName

    @AssetRegionName.setter
    def AssetRegionName(self, AssetRegionName):
        self._AssetRegionName = AssetRegionName

    @property
    def AssetVpcid(self):
        r"""所属网络
        :rtype: str
        """
        return self._AssetVpcid

    @AssetVpcid.setter
    def AssetVpcid(self, AssetVpcid):
        self._AssetVpcid = AssetVpcid

    @property
    def InstanceType(self):
        r"""主机类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceState(self):
        r"""主机状态
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def EngineVersion(self):
        r"""引擎版本
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def Id(self):
        r"""数据库标识
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Tag(self):
        r"""标签
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def AssetCspmRiskNum(self):
        r"""配置风险统计数
        :rtype: int
        """
        return self._AssetCspmRiskNum

    @AssetCspmRiskNum.setter
    def AssetCspmRiskNum(self, AssetCspmRiskNum):
        self._AssetCspmRiskNum = AssetCspmRiskNum

    @property
    def PublicIpAddresses(self):
        r"""主机IP
        :rtype: list of str
        """
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def AssetUniqid(self):
        r"""资产唯一标识
        :rtype: str
        """
        return self._AssetUniqid

    @AssetUniqid.setter
    def AssetUniqid(self, AssetUniqid):
        self._AssetUniqid = AssetUniqid

    @property
    def ChargeType(self):
        r"""付费类型
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def AssetEventNum(self):
        r"""安全事件统计数
        :rtype: int
        """
        return self._AssetEventNum

    @AssetEventNum.setter
    def AssetEventNum(self, AssetEventNum):
        self._AssetEventNum = AssetEventNum

    @property
    def AssetVulNum(self):
        r"""漏洞统计数
        :rtype: int
        """
        return self._AssetVulNum

    @AssetVulNum.setter
    def AssetVulNum(self, AssetVulNum):
        self._AssetVulNum = AssetVulNum

    @property
    def PrivateIpAddresses(self):
        r"""主机IP内网
        :rtype: list of str
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def GroupName(self):
        r"""所属分组
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def SsaAssetDiscoverTime(self):
        r"""发现时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SsaAssetDiscoverTime

    @SsaAssetDiscoverTime.setter
    def SsaAssetDiscoverTime(self, SsaAssetDiscoverTime):
        self._SsaAssetDiscoverTime = SsaAssetDiscoverTime

    @property
    def SsaAssetDeleteTime(self):
        r"""下线时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SsaAssetDeleteTime

    @SsaAssetDeleteTime.setter
    def SsaAssetDeleteTime(self, SsaAssetDeleteTime):
        self._SsaAssetDeleteTime = SsaAssetDeleteTime

    @property
    def IsNew(self):
        r"""是否是新增资产
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def AssetSubnetId(self):
        r"""所属子网
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetSubnetId

    @AssetSubnetId.setter
    def AssetSubnetId(self, AssetSubnetId):
        self._AssetSubnetId = AssetSubnetId

    @property
    def AssetSubnetName(self):
        r"""子网名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetSubnetName

    @AssetSubnetName.setter
    def AssetSubnetName(self, AssetSubnetName):
        self._AssetSubnetName = AssetSubnetName

    @property
    def AssetVpcName(self):
        r"""vpc名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetVpcName

    @AssetVpcName.setter
    def AssetVpcName(self, AssetVpcName):
        self._AssetVpcName = AssetVpcName

    @property
    def ClusterType(self):
        r"""集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def NameSpace(self):
        r"""命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NameSpace

    @NameSpace.setter
    def NameSpace(self, NameSpace):
        self._NameSpace = NameSpace

    @property
    def LoadBalancerType(self):
        r"""负载均衡实例的网络类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def LoadBalancerVips(self):
        r"""负载均衡实例的vip列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._LoadBalancerVips

    @LoadBalancerVips.setter
    def LoadBalancerVips(self, LoadBalancerVips):
        self._LoadBalancerVips = LoadBalancerVips

    @property
    def AssetIpv6(self):
        r"""ipv6信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AssetIpv6

    @AssetIpv6.setter
    def AssetIpv6(self, AssetIpv6):
        self._AssetIpv6 = AssetIpv6

    @property
    def SSHRisk(self):
        r"""ssh端口暴露风险
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SSHRisk

    @SSHRisk.setter
    def SSHRisk(self, SSHRisk):
        self._SSHRisk = SSHRisk

    @property
    def RDPRisk(self):
        r"""rdp端口暴露风险
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RDPRisk

    @RDPRisk.setter
    def RDPRisk(self, RDPRisk):
        self._RDPRisk = RDPRisk

    @property
    def EventRisk(self):
        r"""资产失陷事件风险
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EventRisk

    @EventRisk.setter
    def EventRisk(self, EventRisk):
        self._EventRisk = EventRisk


    def _deserialize(self, params):
        self._AssetType = params.get("AssetType")
        self._Name = params.get("Name")
        self._AssetRegionName = params.get("AssetRegionName")
        self._AssetVpcid = params.get("AssetVpcid")
        self._InstanceType = params.get("InstanceType")
        self._InstanceState = params.get("InstanceState")
        self._EngineVersion = params.get("EngineVersion")
        self._Id = params.get("Id")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._AssetCspmRiskNum = params.get("AssetCspmRiskNum")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._AssetUniqid = params.get("AssetUniqid")
        self._ChargeType = params.get("ChargeType")
        self._AssetEventNum = params.get("AssetEventNum")
        self._AssetVulNum = params.get("AssetVulNum")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._GroupName = params.get("GroupName")
        self._SsaAssetDiscoverTime = params.get("SsaAssetDiscoverTime")
        self._SsaAssetDeleteTime = params.get("SsaAssetDeleteTime")
        self._IsNew = params.get("IsNew")
        self._AssetSubnetId = params.get("AssetSubnetId")
        self._AssetSubnetName = params.get("AssetSubnetName")
        self._AssetVpcName = params.get("AssetVpcName")
        self._ClusterType = params.get("ClusterType")
        self._NameSpace = params.get("NameSpace")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._LoadBalancerVips = params.get("LoadBalancerVips")
        self._AssetIpv6 = params.get("AssetIpv6")
        self._SSHRisk = params.get("SSHRisk")
        self._RDPRisk = params.get("RDPRisk")
        self._EventRisk = params.get("EventRisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetDetail(AbstractModel):
    r"""资产详情信息

    """

    def __init__(self):
        r"""
        :param _AssetType: 资产类型
        :type AssetType: str
        :param _Name: 名字
        :type Name: str
        :param _Region: 区域
        :type Region: str
        :param _VpcId: 所属网络
        :type VpcId: str
        :param _InstanceType: 主机类型
        :type InstanceType: str
        :param _InstanceState: 主机状态
        :type InstanceState: str
        :param _PublicIpAddresses: 主机IP-公网
        :type PublicIpAddresses: list of str
        :param _EngineVersion: 引擎版本
        :type EngineVersion: str
        :param _Id: 标识
        :type Id: str
        :param _Tag: 标签
        :type Tag: list of Tag
        :param _Vip: 内网IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _LoadBalancerVips: 负载均衡示例的vip列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerVips: list of str
        :param _Uin: 账号ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: int
        :param _CreationDate: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationDate: str
        :param _Domain: 访问域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _AssetUniqid: 资产唯一id
        :type AssetUniqid: str
        :param _InstanceId: 关联实例
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _DiskType: 配置硬盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _DiskSize: 配置硬盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _AssetStatus: 云硬盘/证书状态
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetStatus: str
        :param _CertType: 证书类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CertType: str
        :param _ProjectName: 所属项目
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param _CertEndTime: 到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param _ProductType: nosql引擎/版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductType: int
        :param _PrivateIpAddresses: 主机IP-内网
        :type PrivateIpAddresses: list of str
        :param _ValidityPeriod: 证书有效期
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidityPeriod: str
        :param _GroupName: 分组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _Port: 端口服务数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: list of str
        :param _RiskConfig: 配置风险数组
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskConfig: list of str
        :param _Event: 相关待处理事件
注意：此字段可能返回 null，表示取不到有效值。
        :type Event: str
        :param _Vul: 相关待处理漏洞
注意：此字段可能返回 null，表示取不到有效值。
        :type Vul: str
        :param _SsaAssetDiscoverTime: 资产发现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaAssetDiscoverTime: str
        :param _AssetSubnetId: 所属子网
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetSubnetId: str
        :param _AssetSubnetName: 子网名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetSubnetName: str
        :param _AssetVpcName: vpc名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetVpcName: str
        :param _ClusterType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: int
        :param _NameSpace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type NameSpace: str
        :param _AssetCreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCreateTime: str
        :param _LoadBalancerType: 负载均衡网络类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerType: str
        :param _AssetIpv6: ipv6信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetIpv6: list of str
        :param _SSHRisk: ssh风险
注意：此字段可能返回 null，表示取不到有效值。
        :type SSHRisk: str
        :param _RDPRisk: rdp风险
注意：此字段可能返回 null，表示取不到有效值。
        :type RDPRisk: str
        :param _EventRisk: 安全事件风险
注意：此字段可能返回 null，表示取不到有效值。
        :type EventRisk: str
        :param _AssetVulNum: 漏洞数量
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetVulNum: int
        :param _AssetEventNum: 资产事件
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetEventNum: int
        :param _AssetCspmRiskNum: cspm风险
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCspmRiskNum: int
        :param _SsaAssetDeleteTime: 资产删除时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaAssetDeleteTime: str
        :param _ChargeType: 费用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: str
        :param _AssetRegionName: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetRegionName: str
        :param _AssetVpcid: vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetVpcid: str
        """
        self._AssetType = None
        self._Name = None
        self._Region = None
        self._VpcId = None
        self._InstanceType = None
        self._InstanceState = None
        self._PublicIpAddresses = None
        self._EngineVersion = None
        self._Id = None
        self._Tag = None
        self._Vip = None
        self._Status = None
        self._LoadBalancerVips = None
        self._Uin = None
        self._CreationDate = None
        self._Domain = None
        self._AssetUniqid = None
        self._InstanceId = None
        self._DiskType = None
        self._DiskSize = None
        self._AssetStatus = None
        self._CertType = None
        self._ProjectName = None
        self._CertEndTime = None
        self._ProductType = None
        self._PrivateIpAddresses = None
        self._ValidityPeriod = None
        self._GroupName = None
        self._Port = None
        self._RiskConfig = None
        self._Event = None
        self._Vul = None
        self._SsaAssetDiscoverTime = None
        self._AssetSubnetId = None
        self._AssetSubnetName = None
        self._AssetVpcName = None
        self._ClusterType = None
        self._NameSpace = None
        self._AssetCreateTime = None
        self._LoadBalancerType = None
        self._AssetIpv6 = None
        self._SSHRisk = None
        self._RDPRisk = None
        self._EventRisk = None
        self._AssetVulNum = None
        self._AssetEventNum = None
        self._AssetCspmRiskNum = None
        self._SsaAssetDeleteTime = None
        self._ChargeType = None
        self._AssetRegionName = None
        self._AssetVpcid = None

    @property
    def AssetType(self):
        r"""资产类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Name(self):
        r"""名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Region(self):
        r"""区域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        r"""所属网络
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def InstanceType(self):
        r"""主机类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceState(self):
        r"""主机状态
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def PublicIpAddresses(self):
        r"""主机IP-公网
        :rtype: list of str
        """
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def EngineVersion(self):
        r"""引擎版本
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def Id(self):
        r"""标识
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Tag(self):
        r"""标签
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Vip(self):
        r"""内网IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Status(self):
        r"""状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def LoadBalancerVips(self):
        r"""负载均衡示例的vip列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._LoadBalancerVips

    @LoadBalancerVips.setter
    def LoadBalancerVips(self, LoadBalancerVips):
        self._LoadBalancerVips = LoadBalancerVips

    @property
    def Uin(self):
        r"""账号ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def CreationDate(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreationDate

    @CreationDate.setter
    def CreationDate(self, CreationDate):
        self._CreationDate = CreationDate

    @property
    def Domain(self):
        r"""访问域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AssetUniqid(self):
        r"""资产唯一id
        :rtype: str
        """
        return self._AssetUniqid

    @AssetUniqid.setter
    def AssetUniqid(self, AssetUniqid):
        self._AssetUniqid = AssetUniqid

    @property
    def InstanceId(self):
        r"""关联实例
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DiskType(self):
        r"""配置硬盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""配置硬盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def AssetStatus(self):
        r"""云硬盘/证书状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetStatus

    @AssetStatus.setter
    def AssetStatus(self, AssetStatus):
        self._AssetStatus = AssetStatus

    @property
    def CertType(self):
        r"""证书类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def ProjectName(self):
        r"""所属项目
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def CertEndTime(self):
        r"""到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertEndTime

    @CertEndTime.setter
    def CertEndTime(self, CertEndTime):
        self._CertEndTime = CertEndTime

    @property
    def ProductType(self):
        r"""nosql引擎/版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def PrivateIpAddresses(self):
        r"""主机IP-内网
        :rtype: list of str
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def ValidityPeriod(self):
        r"""证书有效期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def GroupName(self):
        r"""分组名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Port(self):
        r"""端口服务数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def RiskConfig(self):
        r"""配置风险数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._RiskConfig

    @RiskConfig.setter
    def RiskConfig(self, RiskConfig):
        self._RiskConfig = RiskConfig

    @property
    def Event(self):
        r"""相关待处理事件
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Event

    @Event.setter
    def Event(self, Event):
        self._Event = Event

    @property
    def Vul(self):
        r"""相关待处理漏洞
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Vul

    @Vul.setter
    def Vul(self, Vul):
        self._Vul = Vul

    @property
    def SsaAssetDiscoverTime(self):
        r"""资产发现时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SsaAssetDiscoverTime

    @SsaAssetDiscoverTime.setter
    def SsaAssetDiscoverTime(self, SsaAssetDiscoverTime):
        self._SsaAssetDiscoverTime = SsaAssetDiscoverTime

    @property
    def AssetSubnetId(self):
        r"""所属子网
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetSubnetId

    @AssetSubnetId.setter
    def AssetSubnetId(self, AssetSubnetId):
        self._AssetSubnetId = AssetSubnetId

    @property
    def AssetSubnetName(self):
        r"""子网名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetSubnetName

    @AssetSubnetName.setter
    def AssetSubnetName(self, AssetSubnetName):
        self._AssetSubnetName = AssetSubnetName

    @property
    def AssetVpcName(self):
        r"""vpc名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetVpcName

    @AssetVpcName.setter
    def AssetVpcName(self, AssetVpcName):
        self._AssetVpcName = AssetVpcName

    @property
    def ClusterType(self):
        r"""集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def NameSpace(self):
        r"""命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NameSpace

    @NameSpace.setter
    def NameSpace(self, NameSpace):
        self._NameSpace = NameSpace

    @property
    def AssetCreateTime(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetCreateTime

    @AssetCreateTime.setter
    def AssetCreateTime(self, AssetCreateTime):
        self._AssetCreateTime = AssetCreateTime

    @property
    def LoadBalancerType(self):
        r"""负载均衡网络类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def AssetIpv6(self):
        r"""ipv6信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AssetIpv6

    @AssetIpv6.setter
    def AssetIpv6(self, AssetIpv6):
        self._AssetIpv6 = AssetIpv6

    @property
    def SSHRisk(self):
        r"""ssh风险
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SSHRisk

    @SSHRisk.setter
    def SSHRisk(self, SSHRisk):
        self._SSHRisk = SSHRisk

    @property
    def RDPRisk(self):
        r"""rdp风险
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RDPRisk

    @RDPRisk.setter
    def RDPRisk(self, RDPRisk):
        self._RDPRisk = RDPRisk

    @property
    def EventRisk(self):
        r"""安全事件风险
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EventRisk

    @EventRisk.setter
    def EventRisk(self, EventRisk):
        self._EventRisk = EventRisk

    @property
    def AssetVulNum(self):
        r"""漏洞数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AssetVulNum

    @AssetVulNum.setter
    def AssetVulNum(self, AssetVulNum):
        self._AssetVulNum = AssetVulNum

    @property
    def AssetEventNum(self):
        r"""资产事件
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AssetEventNum

    @AssetEventNum.setter
    def AssetEventNum(self, AssetEventNum):
        self._AssetEventNum = AssetEventNum

    @property
    def AssetCspmRiskNum(self):
        r"""cspm风险
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AssetCspmRiskNum

    @AssetCspmRiskNum.setter
    def AssetCspmRiskNum(self, AssetCspmRiskNum):
        self._AssetCspmRiskNum = AssetCspmRiskNum

    @property
    def SsaAssetDeleteTime(self):
        r"""资产删除时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SsaAssetDeleteTime

    @SsaAssetDeleteTime.setter
    def SsaAssetDeleteTime(self, SsaAssetDeleteTime):
        self._SsaAssetDeleteTime = SsaAssetDeleteTime

    @property
    def ChargeType(self):
        r"""费用类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def AssetRegionName(self):
        r"""地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetRegionName

    @AssetRegionName.setter
    def AssetRegionName(self, AssetRegionName):
        self._AssetRegionName = AssetRegionName

    @property
    def AssetVpcid(self):
        r"""vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetVpcid

    @AssetVpcid.setter
    def AssetVpcid(self, AssetVpcid):
        self._AssetVpcid = AssetVpcid


    def _deserialize(self, params):
        self._AssetType = params.get("AssetType")
        self._Name = params.get("Name")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._InstanceType = params.get("InstanceType")
        self._InstanceState = params.get("InstanceState")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._EngineVersion = params.get("EngineVersion")
        self._Id = params.get("Id")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._Vip = params.get("Vip")
        self._Status = params.get("Status")
        self._LoadBalancerVips = params.get("LoadBalancerVips")
        self._Uin = params.get("Uin")
        self._CreationDate = params.get("CreationDate")
        self._Domain = params.get("Domain")
        self._AssetUniqid = params.get("AssetUniqid")
        self._InstanceId = params.get("InstanceId")
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._AssetStatus = params.get("AssetStatus")
        self._CertType = params.get("CertType")
        self._ProjectName = params.get("ProjectName")
        self._CertEndTime = params.get("CertEndTime")
        self._ProductType = params.get("ProductType")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._ValidityPeriod = params.get("ValidityPeriod")
        self._GroupName = params.get("GroupName")
        self._Port = params.get("Port")
        self._RiskConfig = params.get("RiskConfig")
        self._Event = params.get("Event")
        self._Vul = params.get("Vul")
        self._SsaAssetDiscoverTime = params.get("SsaAssetDiscoverTime")
        self._AssetSubnetId = params.get("AssetSubnetId")
        self._AssetSubnetName = params.get("AssetSubnetName")
        self._AssetVpcName = params.get("AssetVpcName")
        self._ClusterType = params.get("ClusterType")
        self._NameSpace = params.get("NameSpace")
        self._AssetCreateTime = params.get("AssetCreateTime")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._AssetIpv6 = params.get("AssetIpv6")
        self._SSHRisk = params.get("SSHRisk")
        self._RDPRisk = params.get("RDPRisk")
        self._EventRisk = params.get("EventRisk")
        self._AssetVulNum = params.get("AssetVulNum")
        self._AssetEventNum = params.get("AssetEventNum")
        self._AssetCspmRiskNum = params.get("AssetCspmRiskNum")
        self._SsaAssetDeleteTime = params.get("SsaAssetDeleteTime")
        self._ChargeType = params.get("ChargeType")
        self._AssetRegionName = params.get("AssetRegionName")
        self._AssetVpcid = params.get("AssetVpcid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetList(AbstractModel):
    r"""资产列表

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _List: 资产数组
        :type List: list of Asset
        """
        self._Total = None
        self._List = None

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        r"""资产数组
        :rtype: list of Asset
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Asset()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetQueryFilter(AbstractModel):
    r"""资产查询过滤参数

    """

    def __init__(self):
        r"""
        :param _Filter: 查询参数
        :type Filter: list of QueryFilter
        :param _Logic: 查询连接符，1 and  ，2 or
        :type Logic: int
        """
        self._Filter = None
        self._Logic = None

    @property
    def Filter(self):
        r"""查询参数
        :rtype: list of QueryFilter
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Logic(self):
        r"""查询连接符，1 and  ，2 or
        :rtype: int
        """
        return self._Logic

    @Logic.setter
    def Logic(self, Logic):
        self._Logic = Logic


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = QueryFilter()
                obj._deserialize(item)
                self._Filter.append(obj)
        self._Logic = params.get("Logic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetTypeStatistic(AbstractModel):
    r"""资产测绘结果统计

    """

    def __init__(self):
        r"""
        :param _AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param _AssetCount: 统计计数
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetCount: int
        """
        self._AssetType = None
        self._AssetCount = None

    @property
    def AssetType(self):
        r"""资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def AssetCount(self):
        r"""统计计数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AssetCount

    @AssetCount.setter
    def AssetCount(self, AssetCount):
        self._AssetCount = AssetCount


    def _deserialize(self, params):
        self._AssetType = params.get("AssetType")
        self._AssetCount = params.get("AssetCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttackEvent(AbstractModel):
    r"""攻击事件

    """

    def __init__(self):
        r"""
        :param _SsaSrcIp: 来源ip
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaSrcIp: str
        :param _SsaDstIp: 目标ip
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaDstIp: str
        :param _SsaDstProvince: 目标省份
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaDstProvince: str
        :param _SsaDstCity: 目标城市
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaDstCity: str
        :param _SsaDstCountry: 目标国家
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaDstCountry: str
        :param _SsaSrcProvince: 来源省份
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaSrcProvince: str
        :param _SsaSrcCountry: 来源国家
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaSrcCountry: str
        :param _SsaSrcCity: 来源城市
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaSrcCity: str
        """
        self._SsaSrcIp = None
        self._SsaDstIp = None
        self._SsaDstProvince = None
        self._SsaDstCity = None
        self._SsaDstCountry = None
        self._SsaSrcProvince = None
        self._SsaSrcCountry = None
        self._SsaSrcCity = None

    @property
    def SsaSrcIp(self):
        r"""来源ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SsaSrcIp

    @SsaSrcIp.setter
    def SsaSrcIp(self, SsaSrcIp):
        self._SsaSrcIp = SsaSrcIp

    @property
    def SsaDstIp(self):
        r"""目标ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SsaDstIp

    @SsaDstIp.setter
    def SsaDstIp(self, SsaDstIp):
        self._SsaDstIp = SsaDstIp

    @property
    def SsaDstProvince(self):
        r"""目标省份
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SsaDstProvince

    @SsaDstProvince.setter
    def SsaDstProvince(self, SsaDstProvince):
        self._SsaDstProvince = SsaDstProvince

    @property
    def SsaDstCity(self):
        r"""目标城市
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SsaDstCity

    @SsaDstCity.setter
    def SsaDstCity(self, SsaDstCity):
        self._SsaDstCity = SsaDstCity

    @property
    def SsaDstCountry(self):
        r"""目标国家
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SsaDstCountry

    @SsaDstCountry.setter
    def SsaDstCountry(self, SsaDstCountry):
        self._SsaDstCountry = SsaDstCountry

    @property
    def SsaSrcProvince(self):
        r"""来源省份
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SsaSrcProvince

    @SsaSrcProvince.setter
    def SsaSrcProvince(self, SsaSrcProvince):
        self._SsaSrcProvince = SsaSrcProvince

    @property
    def SsaSrcCountry(self):
        r"""来源国家
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SsaSrcCountry

    @SsaSrcCountry.setter
    def SsaSrcCountry(self, SsaSrcCountry):
        self._SsaSrcCountry = SsaSrcCountry

    @property
    def SsaSrcCity(self):
        r"""来源城市
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SsaSrcCity

    @SsaSrcCity.setter
    def SsaSrcCity(self, SsaSrcCity):
        self._SsaSrcCity = SsaSrcCity


    def _deserialize(self, params):
        self._SsaSrcIp = params.get("SsaSrcIp")
        self._SsaDstIp = params.get("SsaDstIp")
        self._SsaDstProvince = params.get("SsaDstProvince")
        self._SsaDstCity = params.get("SsaDstCity")
        self._SsaDstCountry = params.get("SsaDstCountry")
        self._SsaSrcProvince = params.get("SsaSrcProvince")
        self._SsaSrcCountry = params.get("SsaSrcCountry")
        self._SsaSrcCity = params.get("SsaSrcCity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Bucket(AbstractModel):
    r"""es聚合数据类型

    """

    def __init__(self):
        r"""
        :param _Key: key
        :type Key: str
        :param _Count: 数量
        :type Count: int
        """
        self._Key = None
        self._Count = None

    @property
    def Key(self):
        r"""key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Count(self):
        r"""数量
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
        


class CheckAssetItem(AbstractModel):
    r"""检查项资产组每一项

    """

    def __init__(self):
        r"""
        :param _Id: 检查项下资产组ID
        :type Id: int
        :param _Instid: 资产组实例id
        :type Instid: str
        :param _Url: 处置跳转URL
        :type Url: str
        :param _Taskid: 检查任务id
        :type Taskid: str
        :param _Result: 检查结果
        :type Result: int
        :param _Updatetime: 更新时间
        :type Updatetime: str
        :param _Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: str
        :param _IsIgnore: 是否忽略
        :type IsIgnore: int
        :param _IsChecked: 检查状态
        :type IsChecked: int
        :param _AssetInfo: 资产组信息
        :type AssetInfo: str
        :param _AssetId: 资产组ES的_id
        :type AssetId: str
        :param _Detail: 详情
        :type Detail: str
        :param _Remarks: 备注内容
        :type Remarks: str
        """
        self._Id = None
        self._Instid = None
        self._Url = None
        self._Taskid = None
        self._Result = None
        self._Updatetime = None
        self._Tag = None
        self._IsIgnore = None
        self._IsChecked = None
        self._AssetInfo = None
        self._AssetId = None
        self._Detail = None
        self._Remarks = None

    @property
    def Id(self):
        r"""检查项下资产组ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Instid(self):
        r"""资产组实例id
        :rtype: str
        """
        return self._Instid

    @Instid.setter
    def Instid(self, Instid):
        self._Instid = Instid

    @property
    def Url(self):
        r"""处置跳转URL
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Taskid(self):
        r"""检查任务id
        :rtype: str
        """
        return self._Taskid

    @Taskid.setter
    def Taskid(self, Taskid):
        self._Taskid = Taskid

    @property
    def Result(self):
        r"""检查结果
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Updatetime(self):
        r"""更新时间
        :rtype: str
        """
        return self._Updatetime

    @Updatetime.setter
    def Updatetime(self, Updatetime):
        self._Updatetime = Updatetime

    @property
    def Tag(self):
        r"""标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def IsIgnore(self):
        r"""是否忽略
        :rtype: int
        """
        return self._IsIgnore

    @IsIgnore.setter
    def IsIgnore(self, IsIgnore):
        self._IsIgnore = IsIgnore

    @property
    def IsChecked(self):
        r"""检查状态
        :rtype: int
        """
        return self._IsChecked

    @IsChecked.setter
    def IsChecked(self, IsChecked):
        self._IsChecked = IsChecked

    @property
    def AssetInfo(self):
        r"""资产组信息
        :rtype: str
        """
        return self._AssetInfo

    @AssetInfo.setter
    def AssetInfo(self, AssetInfo):
        self._AssetInfo = AssetInfo

    @property
    def AssetId(self):
        r"""资产组ES的_id
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def Detail(self):
        r"""详情
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Remarks(self):
        r"""备注内容
        :rtype: str
        """
        return self._Remarks

    @Remarks.setter
    def Remarks(self, Remarks):
        self._Remarks = Remarks


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Instid = params.get("Instid")
        self._Url = params.get("Url")
        self._Taskid = params.get("Taskid")
        self._Result = params.get("Result")
        self._Updatetime = params.get("Updatetime")
        self._Tag = params.get("Tag")
        self._IsIgnore = params.get("IsIgnore")
        self._IsChecked = params.get("IsChecked")
        self._AssetInfo = params.get("AssetInfo")
        self._AssetId = params.get("AssetId")
        self._Detail = params.get("Detail")
        self._Remarks = params.get("Remarks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckConfigDetail(AbstractModel):
    r"""云安全配置检查项详情

    """

    def __init__(self):
        r"""
        :param _Id: 检查项Id
        :type Id: str
        :param _CheckName: 检查项名称
        :type CheckName: str
        :param _Content: 检查项内容
        :type Content: str
        :param _Method: 检查项处置方案
        :type Method: str
        :param _Doc: 检查项帮助文档
        :type Doc: str
        :param _ErrorCount: 未通过总数
        :type ErrorCount: int
        :param _IsPass: 是否通过检查
        :type IsPass: int
        :param _SafeCount: 通过检查项
        :type SafeCount: int
        :param _IgnoreCount: 忽略检查项
        :type IgnoreCount: int
        :param _RiskCount: 风险检查项
        :type RiskCount: int
        :param _NameEn: 检查项英文
        :type NameEn: str
        :param _AssetType: 检查项类型
        :type AssetType: str
        :param _ResCount: res_count
        :type ResCount: int
        :param _IsIgnore: 是否忽略
        :type IsIgnore: int
        """
        self._Id = None
        self._CheckName = None
        self._Content = None
        self._Method = None
        self._Doc = None
        self._ErrorCount = None
        self._IsPass = None
        self._SafeCount = None
        self._IgnoreCount = None
        self._RiskCount = None
        self._NameEn = None
        self._AssetType = None
        self._ResCount = None
        self._IsIgnore = None

    @property
    def Id(self):
        r"""检查项Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CheckName(self):
        r"""检查项名称
        :rtype: str
        """
        return self._CheckName

    @CheckName.setter
    def CheckName(self, CheckName):
        self._CheckName = CheckName

    @property
    def Content(self):
        r"""检查项内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Method(self):
        r"""检查项处置方案
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Doc(self):
        r"""检查项帮助文档
        :rtype: str
        """
        return self._Doc

    @Doc.setter
    def Doc(self, Doc):
        self._Doc = Doc

    @property
    def ErrorCount(self):
        r"""未通过总数
        :rtype: int
        """
        return self._ErrorCount

    @ErrorCount.setter
    def ErrorCount(self, ErrorCount):
        self._ErrorCount = ErrorCount

    @property
    def IsPass(self):
        r"""是否通过检查
        :rtype: int
        """
        return self._IsPass

    @IsPass.setter
    def IsPass(self, IsPass):
        self._IsPass = IsPass

    @property
    def SafeCount(self):
        r"""通过检查项
        :rtype: int
        """
        return self._SafeCount

    @SafeCount.setter
    def SafeCount(self, SafeCount):
        self._SafeCount = SafeCount

    @property
    def IgnoreCount(self):
        r"""忽略检查项
        :rtype: int
        """
        return self._IgnoreCount

    @IgnoreCount.setter
    def IgnoreCount(self, IgnoreCount):
        self._IgnoreCount = IgnoreCount

    @property
    def RiskCount(self):
        r"""风险检查项
        :rtype: int
        """
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def NameEn(self):
        r"""检查项英文
        :rtype: str
        """
        return self._NameEn

    @NameEn.setter
    def NameEn(self, NameEn):
        self._NameEn = NameEn

    @property
    def AssetType(self):
        r"""检查项类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def ResCount(self):
        r"""res_count
        :rtype: int
        """
        return self._ResCount

    @ResCount.setter
    def ResCount(self, ResCount):
        self._ResCount = ResCount

    @property
    def IsIgnore(self):
        r"""是否忽略
        :rtype: int
        """
        return self._IsIgnore

    @IsIgnore.setter
    def IsIgnore(self, IsIgnore):
        self._IsIgnore = IsIgnore


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CheckName = params.get("CheckName")
        self._Content = params.get("Content")
        self._Method = params.get("Method")
        self._Doc = params.get("Doc")
        self._ErrorCount = params.get("ErrorCount")
        self._IsPass = params.get("IsPass")
        self._SafeCount = params.get("SafeCount")
        self._IgnoreCount = params.get("IgnoreCount")
        self._RiskCount = params.get("RiskCount")
        self._NameEn = params.get("NameEn")
        self._AssetType = params.get("AssetType")
        self._ResCount = params.get("ResCount")
        self._IsIgnore = params.get("IsIgnore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplianceCheckDetail(AbstractModel):
    r"""等保资产组记录

    """

    def __init__(self):
        r"""
        :param _Id: 检查项ID
        :type Id: str
        :param _Category: 检查项类别
        :type Category: str
        :param _Type: 检查项类型
        :type Type: str
        :param _ErrorCount: 不通过总数
        :type ErrorCount: int
        :param _NameEn: 检查项英文名
        :type NameEn: str
        :param _CheckName: 检查项名称
        :type CheckName: str
        :param _Method: 检查项处置方式
        :type Method: str
        :param _Doc: 帮助文档
        :type Doc: str
        :param _SafeCount: 通过总数
        :type SafeCount: int
        :param _Content: 检查项检查内容
        :type Content: str
        :param _IsPass: 是否通过检测
        :type IsPass: int
        :param _IgnoreCount: 忽略总数
        :type IgnoreCount: int
        :param _RiskCount: 风险总数
        :type RiskCount: int
        :param _LastCheckTime: 最近一次检测时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastCheckTime: str
        :param _AssetType: 资产组类型
        :type AssetType: str
        :param _ResCount: res_count
        :type ResCount: int
        :param _UUID: 检查项UUID
        :type UUID: str
        :param _StandardItem: 标准项
注意：此字段可能返回 null，表示取不到有效值。
        :type StandardItem: str
        :param _Chapter: 章节
注意：此字段可能返回 null，表示取不到有效值。
        :type Chapter: str
        :param _AssetTypeDesc: 资产类型描述
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetTypeDesc: str
        :param _IsIgnore: 是否忽略
注意：此字段可能返回 null，表示取不到有效值。
        :type IsIgnore: int
        :param _RiskItem: 风险项
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskItem: str
        :param _Title: 合规检查项完整名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        """
        self._Id = None
        self._Category = None
        self._Type = None
        self._ErrorCount = None
        self._NameEn = None
        self._CheckName = None
        self._Method = None
        self._Doc = None
        self._SafeCount = None
        self._Content = None
        self._IsPass = None
        self._IgnoreCount = None
        self._RiskCount = None
        self._LastCheckTime = None
        self._AssetType = None
        self._ResCount = None
        self._UUID = None
        self._StandardItem = None
        self._Chapter = None
        self._AssetTypeDesc = None
        self._IsIgnore = None
        self._RiskItem = None
        self._Title = None

    @property
    def Id(self):
        r"""检查项ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Category(self):
        r"""检查项类别
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Type(self):
        r"""检查项类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ErrorCount(self):
        r"""不通过总数
        :rtype: int
        """
        return self._ErrorCount

    @ErrorCount.setter
    def ErrorCount(self, ErrorCount):
        self._ErrorCount = ErrorCount

    @property
    def NameEn(self):
        r"""检查项英文名
        :rtype: str
        """
        return self._NameEn

    @NameEn.setter
    def NameEn(self, NameEn):
        self._NameEn = NameEn

    @property
    def CheckName(self):
        r"""检查项名称
        :rtype: str
        """
        return self._CheckName

    @CheckName.setter
    def CheckName(self, CheckName):
        self._CheckName = CheckName

    @property
    def Method(self):
        r"""检查项处置方式
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Doc(self):
        r"""帮助文档
        :rtype: str
        """
        return self._Doc

    @Doc.setter
    def Doc(self, Doc):
        self._Doc = Doc

    @property
    def SafeCount(self):
        r"""通过总数
        :rtype: int
        """
        return self._SafeCount

    @SafeCount.setter
    def SafeCount(self, SafeCount):
        self._SafeCount = SafeCount

    @property
    def Content(self):
        r"""检查项检查内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def IsPass(self):
        r"""是否通过检测
        :rtype: int
        """
        return self._IsPass

    @IsPass.setter
    def IsPass(self, IsPass):
        self._IsPass = IsPass

    @property
    def IgnoreCount(self):
        r"""忽略总数
        :rtype: int
        """
        return self._IgnoreCount

    @IgnoreCount.setter
    def IgnoreCount(self, IgnoreCount):
        self._IgnoreCount = IgnoreCount

    @property
    def RiskCount(self):
        r"""风险总数
        :rtype: int
        """
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def LastCheckTime(self):
        r"""最近一次检测时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastCheckTime

    @LastCheckTime.setter
    def LastCheckTime(self, LastCheckTime):
        self._LastCheckTime = LastCheckTime

    @property
    def AssetType(self):
        r"""资产组类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def ResCount(self):
        r"""res_count
        :rtype: int
        """
        return self._ResCount

    @ResCount.setter
    def ResCount(self, ResCount):
        self._ResCount = ResCount

    @property
    def UUID(self):
        r"""检查项UUID
        :rtype: str
        """
        return self._UUID

    @UUID.setter
    def UUID(self, UUID):
        self._UUID = UUID

    @property
    def StandardItem(self):
        r"""标准项
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StandardItem

    @StandardItem.setter
    def StandardItem(self, StandardItem):
        self._StandardItem = StandardItem

    @property
    def Chapter(self):
        r"""章节
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Chapter

    @Chapter.setter
    def Chapter(self, Chapter):
        self._Chapter = Chapter

    @property
    def AssetTypeDesc(self):
        r"""资产类型描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetTypeDesc

    @AssetTypeDesc.setter
    def AssetTypeDesc(self, AssetTypeDesc):
        self._AssetTypeDesc = AssetTypeDesc

    @property
    def IsIgnore(self):
        r"""是否忽略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsIgnore

    @IsIgnore.setter
    def IsIgnore(self, IsIgnore):
        self._IsIgnore = IsIgnore

    @property
    def RiskItem(self):
        r"""风险项
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RiskItem

    @RiskItem.setter
    def RiskItem(self, RiskItem):
        self._RiskItem = RiskItem

    @property
    def Title(self):
        r"""合规检查项完整名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Category = params.get("Category")
        self._Type = params.get("Type")
        self._ErrorCount = params.get("ErrorCount")
        self._NameEn = params.get("NameEn")
        self._CheckName = params.get("CheckName")
        self._Method = params.get("Method")
        self._Doc = params.get("Doc")
        self._SafeCount = params.get("SafeCount")
        self._Content = params.get("Content")
        self._IsPass = params.get("IsPass")
        self._IgnoreCount = params.get("IgnoreCount")
        self._RiskCount = params.get("RiskCount")
        self._LastCheckTime = params.get("LastCheckTime")
        self._AssetType = params.get("AssetType")
        self._ResCount = params.get("ResCount")
        self._UUID = params.get("UUID")
        self._StandardItem = params.get("StandardItem")
        self._Chapter = params.get("Chapter")
        self._AssetTypeDesc = params.get("AssetTypeDesc")
        self._IsIgnore = params.get("IsIgnore")
        self._RiskItem = params.get("RiskItem")
        self._Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConcernInfo(AbstractModel):
    r"""关注点类型

    """

    def __init__(self):
        r"""
        :param _ConcernType: 关注点类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ConcernType: int
        :param _EntityType: 实体类型 1: 非云上IP，2: 云上IP，3: 域名，4: IP，5: 文件，6: 进程
注意：此字段可能返回 null，表示取不到有效值。
        :type EntityType: int
        :param _Concern: 关注点
注意：此字段可能返回 null，表示取不到有效值。
        :type Concern: str
        :param _StatisticsCount: 最近数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StatisticsCount: int
        :param _IpCountry: IP国家
注意：此字段可能返回 null，表示取不到有效值。
        :type IpCountry: str
        :param _IpProvince: IP省份
注意：此字段可能返回 null，表示取不到有效值。
        :type IpProvince: str
        :param _Result: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _Confidence: 置信度
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: int
        :param _IpIsp: 服务商
注意：此字段可能返回 null，表示取不到有效值。
        :type IpIsp: str
        :param _IpInfrastructure: 是否基础设施
注意：此字段可能返回 null，表示取不到有效值。
        :type IpInfrastructure: str
        :param _ThreatType: 威胁类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ThreatType: list of str
        :param _Groups: 威胁团伙
注意：此字段可能返回 null，表示取不到有效值。
        :type Groups: list of str
        :param _Status: 状态威胁情报接口
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Tags: 恶意标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param _VictimAssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VictimAssetType: str
        :param _VictimAssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type VictimAssetName: str
        :param _DomainRegistrant: 注册者
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainRegistrant: str
        :param _DomainRegisteredInstitution: 注册机构
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainRegisteredInstitution: str
        :param _DomainRegistrationTime: 注册时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainRegistrationTime: str
        :param _FileName: 文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _FileMd5: MD5
注意：此字段可能返回 null，表示取不到有效值。
        :type FileMd5: str
        :param _VirusName: 病毒名
注意：此字段可能返回 null，表示取不到有效值。
        :type VirusName: str
        :param _FilePath: 文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :type FilePath: str
        :param _FileSize: 文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: str
        :param _ProcName: 进程名
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcName: str
        :param _Pid: 进程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Pid: str
        :param _ProcPath: 进程路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcPath: str
        :param _ProcUser: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcUser: str
        :param _DefendedCount: 已防御
注意：此字段可能返回 null，表示取不到有效值。
        :type DefendedCount: int
        :param _DetectedCount: 仅检测
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectedCount: int
        :param _SearchData: 可疑关注点字段
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchData: str
        :param _IpCountryIso: 可疑关注点字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IpCountryIso: str
        :param _IpProvinceIso: 可疑关注点字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IpProvinceIso: str
        :param _IpCity: 可疑关注点字段
注意：此字段可能返回 null，表示取不到有效值。
        :type IpCity: str
        :param _EventSubType: 可疑关注点字段
注意：此字段可能返回 null，表示取不到有效值。
        :type EventSubType: str
        """
        self._ConcernType = None
        self._EntityType = None
        self._Concern = None
        self._StatisticsCount = None
        self._IpCountry = None
        self._IpProvince = None
        self._Result = None
        self._Confidence = None
        self._IpIsp = None
        self._IpInfrastructure = None
        self._ThreatType = None
        self._Groups = None
        self._Status = None
        self._Tags = None
        self._VictimAssetType = None
        self._VictimAssetName = None
        self._DomainRegistrant = None
        self._DomainRegisteredInstitution = None
        self._DomainRegistrationTime = None
        self._FileName = None
        self._FileMd5 = None
        self._VirusName = None
        self._FilePath = None
        self._FileSize = None
        self._ProcName = None
        self._Pid = None
        self._ProcPath = None
        self._ProcUser = None
        self._DefendedCount = None
        self._DetectedCount = None
        self._SearchData = None
        self._IpCountryIso = None
        self._IpProvinceIso = None
        self._IpCity = None
        self._EventSubType = None

    @property
    def ConcernType(self):
        r"""关注点类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ConcernType

    @ConcernType.setter
    def ConcernType(self, ConcernType):
        self._ConcernType = ConcernType

    @property
    def EntityType(self):
        r"""实体类型 1: 非云上IP，2: 云上IP，3: 域名，4: IP，5: 文件，6: 进程
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EntityType

    @EntityType.setter
    def EntityType(self, EntityType):
        self._EntityType = EntityType

    @property
    def Concern(self):
        r"""关注点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Concern

    @Concern.setter
    def Concern(self, Concern):
        self._Concern = Concern

    @property
    def StatisticsCount(self):
        r"""最近数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StatisticsCount

    @StatisticsCount.setter
    def StatisticsCount(self, StatisticsCount):
        self._StatisticsCount = StatisticsCount

    @property
    def IpCountry(self):
        r"""IP国家
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IpCountry

    @IpCountry.setter
    def IpCountry(self, IpCountry):
        self._IpCountry = IpCountry

    @property
    def IpProvince(self):
        r"""IP省份
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IpProvince

    @IpProvince.setter
    def IpProvince(self, IpProvince):
        self._IpProvince = IpProvince

    @property
    def Result(self):
        r"""结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Confidence(self):
        r"""置信度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def IpIsp(self):
        r"""服务商
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IpIsp

    @IpIsp.setter
    def IpIsp(self, IpIsp):
        self._IpIsp = IpIsp

    @property
    def IpInfrastructure(self):
        r"""是否基础设施
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IpInfrastructure

    @IpInfrastructure.setter
    def IpInfrastructure(self, IpInfrastructure):
        self._IpInfrastructure = IpInfrastructure

    @property
    def ThreatType(self):
        r"""威胁类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ThreatType

    @ThreatType.setter
    def ThreatType(self, ThreatType):
        self._ThreatType = ThreatType

    @property
    def Groups(self):
        r"""威胁团伙
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def Status(self):
        r"""状态威胁情报接口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        r"""恶意标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def VictimAssetType(self):
        r"""资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VictimAssetType

    @VictimAssetType.setter
    def VictimAssetType(self, VictimAssetType):
        self._VictimAssetType = VictimAssetType

    @property
    def VictimAssetName(self):
        r"""资产名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VictimAssetName

    @VictimAssetName.setter
    def VictimAssetName(self, VictimAssetName):
        self._VictimAssetName = VictimAssetName

    @property
    def DomainRegistrant(self):
        r"""注册者
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DomainRegistrant

    @DomainRegistrant.setter
    def DomainRegistrant(self, DomainRegistrant):
        self._DomainRegistrant = DomainRegistrant

    @property
    def DomainRegisteredInstitution(self):
        r"""注册机构
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DomainRegisteredInstitution

    @DomainRegisteredInstitution.setter
    def DomainRegisteredInstitution(self, DomainRegisteredInstitution):
        self._DomainRegisteredInstitution = DomainRegisteredInstitution

    @property
    def DomainRegistrationTime(self):
        r"""注册时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DomainRegistrationTime

    @DomainRegistrationTime.setter
    def DomainRegistrationTime(self, DomainRegistrationTime):
        self._DomainRegistrationTime = DomainRegistrationTime

    @property
    def FileName(self):
        r"""文件名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileMd5(self):
        r"""MD5
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileMd5

    @FileMd5.setter
    def FileMd5(self, FileMd5):
        self._FileMd5 = FileMd5

    @property
    def VirusName(self):
        r"""病毒名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VirusName

    @VirusName.setter
    def VirusName(self, VirusName):
        self._VirusName = VirusName

    @property
    def FilePath(self):
        r"""文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def FileSize(self):
        r"""文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def ProcName(self):
        r"""进程名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProcName

    @ProcName.setter
    def ProcName(self, ProcName):
        self._ProcName = ProcName

    @property
    def Pid(self):
        r"""进程ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def ProcPath(self):
        r"""进程路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProcPath

    @ProcPath.setter
    def ProcPath(self, ProcPath):
        self._ProcPath = ProcPath

    @property
    def ProcUser(self):
        r"""用户名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProcUser

    @ProcUser.setter
    def ProcUser(self, ProcUser):
        self._ProcUser = ProcUser

    @property
    def DefendedCount(self):
        r"""已防御
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DefendedCount

    @DefendedCount.setter
    def DefendedCount(self, DefendedCount):
        self._DefendedCount = DefendedCount

    @property
    def DetectedCount(self):
        r"""仅检测
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DetectedCount

    @DetectedCount.setter
    def DetectedCount(self, DetectedCount):
        self._DetectedCount = DetectedCount

    @property
    def SearchData(self):
        r"""可疑关注点字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SearchData

    @SearchData.setter
    def SearchData(self, SearchData):
        self._SearchData = SearchData

    @property
    def IpCountryIso(self):
        r"""可疑关注点字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IpCountryIso

    @IpCountryIso.setter
    def IpCountryIso(self, IpCountryIso):
        self._IpCountryIso = IpCountryIso

    @property
    def IpProvinceIso(self):
        r"""可疑关注点字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IpProvinceIso

    @IpProvinceIso.setter
    def IpProvinceIso(self, IpProvinceIso):
        self._IpProvinceIso = IpProvinceIso

    @property
    def IpCity(self):
        r"""可疑关注点字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IpCity

    @IpCity.setter
    def IpCity(self, IpCity):
        self._IpCity = IpCity

    @property
    def EventSubType(self):
        r"""可疑关注点字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EventSubType

    @EventSubType.setter
    def EventSubType(self, EventSubType):
        self._EventSubType = EventSubType


    def _deserialize(self, params):
        self._ConcernType = params.get("ConcernType")
        self._EntityType = params.get("EntityType")
        self._Concern = params.get("Concern")
        self._StatisticsCount = params.get("StatisticsCount")
        self._IpCountry = params.get("IpCountry")
        self._IpProvince = params.get("IpProvince")
        self._Result = params.get("Result")
        self._Confidence = params.get("Confidence")
        self._IpIsp = params.get("IpIsp")
        self._IpInfrastructure = params.get("IpInfrastructure")
        self._ThreatType = params.get("ThreatType")
        self._Groups = params.get("Groups")
        self._Status = params.get("Status")
        self._Tags = params.get("Tags")
        self._VictimAssetType = params.get("VictimAssetType")
        self._VictimAssetName = params.get("VictimAssetName")
        self._DomainRegistrant = params.get("DomainRegistrant")
        self._DomainRegisteredInstitution = params.get("DomainRegisteredInstitution")
        self._DomainRegistrationTime = params.get("DomainRegistrationTime")
        self._FileName = params.get("FileName")
        self._FileMd5 = params.get("FileMd5")
        self._VirusName = params.get("VirusName")
        self._FilePath = params.get("FilePath")
        self._FileSize = params.get("FileSize")
        self._ProcName = params.get("ProcName")
        self._Pid = params.get("Pid")
        self._ProcPath = params.get("ProcPath")
        self._ProcUser = params.get("ProcUser")
        self._DefendedCount = params.get("DefendedCount")
        self._DetectedCount = params.get("DetectedCount")
        self._SearchData = params.get("SearchData")
        self._IpCountryIso = params.get("IpCountryIso")
        self._IpProvinceIso = params.get("IpProvinceIso")
        self._IpCity = params.get("IpCity")
        self._EventSubType = params.get("EventSubType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataCheck(AbstractModel):
    r"""检查项详情对象

    """

    def __init__(self):
        r"""
        :param _Id: 检查项唯一标识符uuid
        :type Id: str
        :param _Name: 检查项名称
        :type Name: str
        :param _Type: 检查项类型
        :type Type: str
        :param _LastCheckTime: 最近一次检查时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastCheckTime: str
        :param _Status: 初始未检测状态0, 已通过为1，未通过为2
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _IsIgnored: 0-未忽略,1-已忽略
注意：此字段可能返回 null，表示取不到有效值。
        :type IsIgnored: int
        :param _RiskCount: 有风险的资源总数，未通过数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCount: int
        :param _IsChecked: 0-检测中,1-结束检测
注意：此字段可能返回 null，表示取不到有效值。
        :type IsChecked: int
        :param _AssetTotal: 总资产数
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetTotal: int
        :param _Remarks: 备注内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Remarks: str
        """
        self._Id = None
        self._Name = None
        self._Type = None
        self._LastCheckTime = None
        self._Status = None
        self._IsIgnored = None
        self._RiskCount = None
        self._IsChecked = None
        self._AssetTotal = None
        self._Remarks = None

    @property
    def Id(self):
        r"""检查项唯一标识符uuid
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""检查项名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""检查项类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def LastCheckTime(self):
        r"""最近一次检查时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastCheckTime

    @LastCheckTime.setter
    def LastCheckTime(self, LastCheckTime):
        self._LastCheckTime = LastCheckTime

    @property
    def Status(self):
        r"""初始未检测状态0, 已通过为1，未通过为2
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsIgnored(self):
        r"""0-未忽略,1-已忽略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsIgnored

    @IsIgnored.setter
    def IsIgnored(self, IsIgnored):
        self._IsIgnored = IsIgnored

    @property
    def RiskCount(self):
        r"""有风险的资源总数，未通过数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def IsChecked(self):
        r"""0-检测中,1-结束检测
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsChecked

    @IsChecked.setter
    def IsChecked(self, IsChecked):
        self._IsChecked = IsChecked

    @property
    def AssetTotal(self):
        r"""总资产数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AssetTotal

    @AssetTotal.setter
    def AssetTotal(self, AssetTotal):
        self._AssetTotal = AssetTotal

    @property
    def Remarks(self):
        r"""备注内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remarks

    @Remarks.setter
    def Remarks(self, Remarks):
        self._Remarks = Remarks


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._LastCheckTime = params.get("LastCheckTime")
        self._Status = params.get("Status")
        self._IsIgnored = params.get("IsIgnored")
        self._RiskCount = params.get("RiskCount")
        self._IsChecked = params.get("IsChecked")
        self._AssetTotal = params.get("AssetTotal")
        self._Remarks = params.get("Remarks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataCompliance(AbstractModel):
    r"""合规检查项详情对象

    """

    def __init__(self):
        r"""
        :param _Id: 等保唯一标识符
        :type Id: str
        :param _CheckItemId: 检查项唯一标识符
        :type CheckItemId: str
        :param _Name: 检查项名称
        :type Name: str
        :param _AssetType: 检查项资产类型
        :type AssetType: str
        :param _Type: 检查项类型
        :type Type: str
        :param _Category: 检查项类别
        :type Category: str
        :param _StandardItem: 检查项标准项
        :type StandardItem: str
        :param _Chapter: 检查项章节号
        :type Chapter: str
        :param _LastCheckTime: 最近一次检查时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastCheckTime: str
        :param _Status: 初始未检测状态0, 已通过为1，未通过为2
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _RiskCount: 有风险的资源总数，未通过数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCount: int
        :param _IsChecked: 0-检测中,1-结束检测
注意：此字段可能返回 null，表示取不到有效值。
        :type IsChecked: int
        :param _RiskItem: 检查项风险项
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskItem: str
        :param _IsIgnored: 0-未忽略,1-已忽略
注意：此字段可能返回 null，表示取不到有效值。
        :type IsIgnored: int
        :param _Title: 等保检查项完整名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param _AssetTotal: 资产总数
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetTotal: int
        :param _Remarks: 忽略内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Remarks: str
        """
        self._Id = None
        self._CheckItemId = None
        self._Name = None
        self._AssetType = None
        self._Type = None
        self._Category = None
        self._StandardItem = None
        self._Chapter = None
        self._LastCheckTime = None
        self._Status = None
        self._RiskCount = None
        self._IsChecked = None
        self._RiskItem = None
        self._IsIgnored = None
        self._Title = None
        self._AssetTotal = None
        self._Remarks = None

    @property
    def Id(self):
        r"""等保唯一标识符
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CheckItemId(self):
        r"""检查项唯一标识符
        :rtype: str
        """
        return self._CheckItemId

    @CheckItemId.setter
    def CheckItemId(self, CheckItemId):
        self._CheckItemId = CheckItemId

    @property
    def Name(self):
        r"""检查项名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AssetType(self):
        r"""检查项资产类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Type(self):
        r"""检查项类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Category(self):
        r"""检查项类别
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def StandardItem(self):
        r"""检查项标准项
        :rtype: str
        """
        return self._StandardItem

    @StandardItem.setter
    def StandardItem(self, StandardItem):
        self._StandardItem = StandardItem

    @property
    def Chapter(self):
        r"""检查项章节号
        :rtype: str
        """
        return self._Chapter

    @Chapter.setter
    def Chapter(self, Chapter):
        self._Chapter = Chapter

    @property
    def LastCheckTime(self):
        r"""最近一次检查时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastCheckTime

    @LastCheckTime.setter
    def LastCheckTime(self, LastCheckTime):
        self._LastCheckTime = LastCheckTime

    @property
    def Status(self):
        r"""初始未检测状态0, 已通过为1，未通过为2
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RiskCount(self):
        r"""有风险的资源总数，未通过数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def IsChecked(self):
        r"""0-检测中,1-结束检测
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsChecked

    @IsChecked.setter
    def IsChecked(self, IsChecked):
        self._IsChecked = IsChecked

    @property
    def RiskItem(self):
        r"""检查项风险项
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RiskItem

    @RiskItem.setter
    def RiskItem(self, RiskItem):
        self._RiskItem = RiskItem

    @property
    def IsIgnored(self):
        r"""0-未忽略,1-已忽略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsIgnored

    @IsIgnored.setter
    def IsIgnored(self, IsIgnored):
        self._IsIgnored = IsIgnored

    @property
    def Title(self):
        r"""等保检查项完整名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def AssetTotal(self):
        r"""资产总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AssetTotal

    @AssetTotal.setter
    def AssetTotal(self, AssetTotal):
        self._AssetTotal = AssetTotal

    @property
    def Remarks(self):
        r"""忽略内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remarks

    @Remarks.setter
    def Remarks(self, Remarks):
        self._Remarks = Remarks


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CheckItemId = params.get("CheckItemId")
        self._Name = params.get("Name")
        self._AssetType = params.get("AssetType")
        self._Type = params.get("Type")
        self._Category = params.get("Category")
        self._StandardItem = params.get("StandardItem")
        self._Chapter = params.get("Chapter")
        self._LastCheckTime = params.get("LastCheckTime")
        self._Status = params.get("Status")
        self._RiskCount = params.get("RiskCount")
        self._IsChecked = params.get("IsChecked")
        self._RiskItem = params.get("RiskItem")
        self._IsIgnored = params.get("IsIgnored")
        self._Title = params.get("Title")
        self._AssetTotal = params.get("AssetTotal")
        self._Remarks = params.get("Remarks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmStatRequest(AbstractModel):
    r"""DescribeAlarmStat请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
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
        


class DescribeAlarmStatResponse(AbstractModel):
    r"""DescribeAlarmStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 威胁告警信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ssa.v20180608.models.AlarmInfoRsp`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""威胁告警信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssa.v20180608.models.AlarmInfoRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AlarmInfoRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeAssetDetailListRequest(AbstractModel):
    r"""DescribeAssetDetailList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 查询条件，可支持的查询字段：AssetUniqid,AssetName,AssetIpAll,AssetVpcid,Tag
        :type Filter: list of AssetQueryFilter
        :param _Sorter: 排序条件，可支持的排序字段：
AssetCspmRiskNum,AssetVulNum,AssetEventNum,SsaAssetDiscoverTime
        :type Sorter: list of QuerySort
        :param _RiskTags: 风险标签
        :type RiskTags: list of str
        :param _Tags: 标签
        :type Tags: list of str
        :param _PageIndex: 页
        :type PageIndex: int
        :param _PageSize: 页大小
        :type PageSize: int
        """
        self._Filter = None
        self._Sorter = None
        self._RiskTags = None
        self._Tags = None
        self._PageIndex = None
        self._PageSize = None

    @property
    def Filter(self):
        r"""查询条件，可支持的查询字段：AssetUniqid,AssetName,AssetIpAll,AssetVpcid,Tag
        :rtype: list of AssetQueryFilter
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Sorter(self):
        r"""排序条件，可支持的排序字段：
AssetCspmRiskNum,AssetVulNum,AssetEventNum,SsaAssetDiscoverTime
        :rtype: list of QuerySort
        """
        return self._Sorter

    @Sorter.setter
    def Sorter(self, Sorter):
        self._Sorter = Sorter

    @property
    def RiskTags(self):
        r"""风险标签
        :rtype: list of str
        """
        return self._RiskTags

    @RiskTags.setter
    def RiskTags(self, RiskTags):
        self._RiskTags = RiskTags

    @property
    def Tags(self):
        r"""标签
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def PageIndex(self):
        r"""页
        :rtype: int
        """
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex

    @property
    def PageSize(self):
        r"""页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = AssetQueryFilter()
                obj._deserialize(item)
                self._Filter.append(obj)
        if params.get("Sorter") is not None:
            self._Sorter = []
            for item in params.get("Sorter"):
                obj = QuerySort()
                obj._deserialize(item)
                self._Sorter.append(obj)
        self._RiskTags = params.get("RiskTags")
        self._Tags = params.get("Tags")
        self._PageIndex = params.get("PageIndex")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetDetailListResponse(AbstractModel):
    r"""DescribeAssetDetailList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of AssetDetail
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""业务数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AssetDetail
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = AssetDetail()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeAssetDetailRequest(AbstractModel):
    r"""DescribeAssetDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Params: 查询过滤参数
        :type Params: str
        """
        self._Params = None

    @property
    def Params(self):
        r"""查询过滤参数
        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._Params = params.get("Params")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetDetailResponse(AbstractModel):
    r"""DescribeAssetDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 资产详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ssa.v20180608.models.AssetDetail`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""资产详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssa.v20180608.models.AssetDetail`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AssetDetail()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeAssetListRequest(AbstractModel):
    r"""DescribeAssetList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Params: 查询过滤参数
        :type Params: str
        """
        self._Params = None

    @property
    def Params(self):
        r"""查询过滤参数
        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._Params = params.get("Params")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetListResponse(AbstractModel):
    r"""DescribeAssetList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AssetList: 资产列表
        :type AssetList: :class:`tencentcloud.ssa.v20180608.models.AssetList`
        :param _AggregationData: 聚合数据
        :type AggregationData: list of AggregationObj
        :param _NamespaceData: 命名空间数据
        :type NamespaceData: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AssetList = None
        self._AggregationData = None
        self._NamespaceData = None
        self._RequestId = None

    @property
    def AssetList(self):
        r"""资产列表
        :rtype: :class:`tencentcloud.ssa.v20180608.models.AssetList`
        """
        return self._AssetList

    @AssetList.setter
    def AssetList(self, AssetList):
        self._AssetList = AssetList

    @property
    def AggregationData(self):
        r"""聚合数据
        :rtype: list of AggregationObj
        """
        return self._AggregationData

    @AggregationData.setter
    def AggregationData(self, AggregationData):
        self._AggregationData = AggregationData

    @property
    def NamespaceData(self):
        r"""命名空间数据
        :rtype: list of str
        """
        return self._NamespaceData

    @NamespaceData.setter
    def NamespaceData(self, NamespaceData):
        self._NamespaceData = NamespaceData

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AssetList") is not None:
            self._AssetList = AssetList()
            self._AssetList._deserialize(params.get("AssetList"))
        if params.get("AggregationData") is not None:
            self._AggregationData = []
            for item in params.get("AggregationData"):
                obj = AggregationObj()
                obj._deserialize(item)
                self._AggregationData.append(obj)
        self._NamespaceData = params.get("NamespaceData")
        self._RequestId = params.get("RequestId")


class DescribeCheckConfigAssetListRequest(AbstractModel):
    r"""DescribeCheckConfigAssetList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 检查项UUID
        :type Id: str
        :param _Offset: 页码
        :type Offset: int
        :param _Limit: 每页列表数
        :type Limit: int
        :param _Search: db搜索条件
        :type Search: list of Filter
        :param _Filter: ES过滤条件
        :type Filter: list of Filter
        """
        self._Id = None
        self._Offset = None
        self._Limit = None
        self._Search = None
        self._Filter = None

    @property
    def Id(self):
        r"""检查项UUID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Offset(self):
        r"""页码
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页列表数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Search(self):
        r"""db搜索条件
        :rtype: list of Filter
        """
        return self._Search

    @Search.setter
    def Search(self, Search):
        self._Search = Search

    @property
    def Filter(self):
        r"""ES过滤条件
        :rtype: list of Filter
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Search") is not None:
            self._Search = []
            for item in params.get("Search"):
                obj = Filter()
                obj._deserialize(item)
                self._Search.append(obj)
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self._Filter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCheckConfigAssetListResponse(AbstractModel):
    r"""DescribeCheckConfigAssetList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 资产列表总数
        :type Total: int
        :param _CheckAssetsList: 资产列表项
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckAssetsList: list of CheckAssetItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._CheckAssetsList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""资产列表总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def CheckAssetsList(self):
        r"""资产列表项
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CheckAssetItem
        """
        return self._CheckAssetsList

    @CheckAssetsList.setter
    def CheckAssetsList(self, CheckAssetsList):
        self._CheckAssetsList = CheckAssetsList

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("CheckAssetsList") is not None:
            self._CheckAssetsList = []
            for item in params.get("CheckAssetsList"):
                obj = CheckAssetItem()
                obj._deserialize(item)
                self._CheckAssetsList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCheckConfigDetailRequest(AbstractModel):
    r"""DescribeCheckConfigDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 检查项ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        r"""检查项ID
        :rtype: str
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
        


class DescribeCheckConfigDetailResponse(AbstractModel):
    r"""DescribeCheckConfigDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CheckConfigDetail: 检查项详情
        :type CheckConfigDetail: :class:`tencentcloud.ssa.v20180608.models.CheckConfigDetail`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CheckConfigDetail = None
        self._RequestId = None

    @property
    def CheckConfigDetail(self):
        r"""检查项详情
        :rtype: :class:`tencentcloud.ssa.v20180608.models.CheckConfigDetail`
        """
        return self._CheckConfigDetail

    @CheckConfigDetail.setter
    def CheckConfigDetail(self, CheckConfigDetail):
        self._CheckConfigDetail = CheckConfigDetail

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CheckConfigDetail") is not None:
            self._CheckConfigDetail = CheckConfigDetail()
            self._CheckConfigDetail._deserialize(params.get("CheckConfigDetail"))
        self._RequestId = params.get("RequestId")


class DescribeComplianceAssetListRequest(AbstractModel):
    r"""DescribeComplianceAssetList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页码
        :type Offset: int
        :param _Limit: 每页数量
        :type Limit: int
        :param _Id: 检查项uuid
        :type Id: str
        :param _Filter: 过滤条件
        :type Filter: list of Filter
        :param _Search: 查询条件
        :type Search: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Id = None
        self._Filter = None
        self._Search = None

    @property
    def Offset(self):
        r"""页码
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Id(self):
        r"""检查项uuid
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Filter(self):
        r"""过滤条件
        :rtype: list of Filter
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Search(self):
        r"""查询条件
        :rtype: list of Filter
        """
        return self._Search

    @Search.setter
    def Search(self, Search):
        self._Search = Search


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Id = params.get("Id")
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self._Filter.append(obj)
        if params.get("Search") is not None:
            self._Search = []
            for item in params.get("Search"):
                obj = Filter()
                obj._deserialize(item)
                self._Search.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComplianceAssetListResponse(AbstractModel):
    r"""DescribeComplianceAssetList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CheckAssetsList: 资产组列表
        :type CheckAssetsList: list of CheckAssetItem
        :param _Total: 资产组列表总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CheckAssetsList = None
        self._Total = None
        self._RequestId = None

    @property
    def CheckAssetsList(self):
        r"""资产组列表
        :rtype: list of CheckAssetItem
        """
        return self._CheckAssetsList

    @CheckAssetsList.setter
    def CheckAssetsList(self, CheckAssetsList):
        self._CheckAssetsList = CheckAssetsList

    @property
    def Total(self):
        r"""资产组列表总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CheckAssetsList") is not None:
            self._CheckAssetsList = []
            for item in params.get("CheckAssetsList"):
                obj = CheckAssetItem()
                obj._deserialize(item)
                self._CheckAssetsList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeComplianceDetailRequest(AbstractModel):
    r"""DescribeComplianceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 检查项uuid
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        r"""检查项uuid
        :rtype: str
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
        


class DescribeComplianceDetailResponse(AbstractModel):
    r"""DescribeComplianceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CheckConfigDetail: 合规管理检查项详情
        :type CheckConfigDetail: :class:`tencentcloud.ssa.v20180608.models.ComplianceCheckDetail`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CheckConfigDetail = None
        self._RequestId = None

    @property
    def CheckConfigDetail(self):
        r"""合规管理检查项详情
        :rtype: :class:`tencentcloud.ssa.v20180608.models.ComplianceCheckDetail`
        """
        return self._CheckConfigDetail

    @CheckConfigDetail.setter
    def CheckConfigDetail(self, CheckConfigDetail):
        self._CheckConfigDetail = CheckConfigDetail

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CheckConfigDetail") is not None:
            self._CheckConfigDetail = ComplianceCheckDetail()
            self._CheckConfigDetail._deserialize(params.get("CheckConfigDetail"))
        self._RequestId = params.get("RequestId")


class DescribeComplianceListRequest(AbstractModel):
    r"""DescribeComplianceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 搜索过滤条件
        :type Filter: str
        """
        self._Filter = None

    @property
    def Filter(self):
        r"""搜索过滤条件
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComplianceListResponse(AbstractModel):
    r"""DescribeComplianceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 检查项列表
        :type Data: list of DataCompliance
        :param _AssetTotalNum: 总检查资产数
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetTotalNum: int
        :param _ConfigTotalNum: 总检查项
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigTotalNum: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._AssetTotalNum = None
        self._ConfigTotalNum = None
        self._RequestId = None

    @property
    def Data(self):
        r"""检查项列表
        :rtype: list of DataCompliance
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def AssetTotalNum(self):
        r"""总检查资产数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AssetTotalNum

    @AssetTotalNum.setter
    def AssetTotalNum(self, AssetTotalNum):
        self._AssetTotalNum = AssetTotalNum

    @property
    def ConfigTotalNum(self):
        r"""总检查项
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ConfigTotalNum

    @ConfigTotalNum.setter
    def ConfigTotalNum(self, ConfigTotalNum):
        self._ConfigTotalNum = ConfigTotalNum

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = DataCompliance()
                obj._deserialize(item)
                self._Data.append(obj)
        self._AssetTotalNum = params.get("AssetTotalNum")
        self._ConfigTotalNum = params.get("ConfigTotalNum")
        self._RequestId = params.get("RequestId")


class DescribeConfigListRequest(AbstractModel):
    r"""DescribeConfigList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 搜索过滤条件
        :type Filter: str
        """
        self._Filter = None

    @property
    def Filter(self):
        r"""搜索过滤条件
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigListResponse(AbstractModel):
    r"""DescribeConfigList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 检查项列表
        :type Data: list of DataCheck
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""检查项列表
        :rtype: list of DataCheck
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = DataCheck()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainListRequest(AbstractModel):
    r"""DescribeDomainList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 起始，从0开始(只支持32位)
        :type Offset: int
        :param _Limit: limit,最大值200(只支持32位)
        :type Limit: int
        :param _AssetBasicType: 资产大类，根据此字段时返回不同的子结构,AssetBasicType(只支持32位)
        :type AssetBasicType: int
        :param _Filter: 过滤条件
        :type Filter: list of QueryFilterV3
        :param _Order: 排序
        :type Order: str
        :param _By: 排序字段
        :type By: str
        :param _Field: 导出字段
        :type Field: list of str
        :param _TimeRange: 时间范围(只支持32位)
        :type TimeRange: int
        :param _Logic: 逻辑字段(只支持32位)
        :type Logic: int
        :param _GroupByField: 聚合字段  
        :type GroupByField: str
        :param _Task: -
        :type Task: str
        :param _RequestFrom: 0:cfw 1:vss 2.soc 3.waf 4.cwp
        :type RequestFrom: int
        """
        self._Offset = None
        self._Limit = None
        self._AssetBasicType = None
        self._Filter = None
        self._Order = None
        self._By = None
        self._Field = None
        self._TimeRange = None
        self._Logic = None
        self._GroupByField = None
        self._Task = None
        self._RequestFrom = None

    @property
    def Offset(self):
        r"""起始，从0开始(只支持32位)
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""limit,最大值200(只支持32位)
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AssetBasicType(self):
        r"""资产大类，根据此字段时返回不同的子结构,AssetBasicType(只支持32位)
        :rtype: int
        """
        return self._AssetBasicType

    @AssetBasicType.setter
    def AssetBasicType(self, AssetBasicType):
        self._AssetBasicType = AssetBasicType

    @property
    def Filter(self):
        r"""过滤条件
        :rtype: list of QueryFilterV3
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Order(self):
        r"""排序
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""排序字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def Field(self):
        r"""导出字段
        :rtype: list of str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def TimeRange(self):
        r"""时间范围(只支持32位)
        :rtype: int
        """
        return self._TimeRange

    @TimeRange.setter
    def TimeRange(self, TimeRange):
        self._TimeRange = TimeRange

    @property
    def Logic(self):
        r"""逻辑字段(只支持32位)
        :rtype: int
        """
        return self._Logic

    @Logic.setter
    def Logic(self, Logic):
        self._Logic = Logic

    @property
    def GroupByField(self):
        r"""聚合字段  
        :rtype: str
        """
        return self._GroupByField

    @GroupByField.setter
    def GroupByField(self, GroupByField):
        self._GroupByField = GroupByField

    @property
    def Task(self):
        r"""-
        :rtype: str
        """
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

    @property
    def RequestFrom(self):
        r"""0:cfw 1:vss 2.soc 3.waf 4.cwp
        :rtype: int
        """
        return self._RequestFrom

    @RequestFrom.setter
    def RequestFrom(self, RequestFrom):
        self._RequestFrom = RequestFrom


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AssetBasicType = params.get("AssetBasicType")
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = QueryFilterV3()
                obj._deserialize(item)
                self._Filter.append(obj)
        self._Order = params.get("Order")
        self._By = params.get("By")
        self._Field = params.get("Field")
        self._TimeRange = params.get("TimeRange")
        self._Logic = params.get("Logic")
        self._GroupByField = params.get("GroupByField")
        self._Task = params.get("Task")
        self._RequestFrom = params.get("RequestFrom")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainListResponse(AbstractModel):
    r"""DescribeDomainList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 无
        :type Total: int
        :param _DomainInfoCollection: 无
        :type DomainInfoCollection: list of DomainInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._DomainInfoCollection = None
        self._RequestId = None

    @property
    def Total(self):
        r"""无
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def DomainInfoCollection(self):
        r"""无
        :rtype: list of DomainInfo
        """
        return self._DomainInfoCollection

    @DomainInfoCollection.setter
    def DomainInfoCollection(self, DomainInfoCollection):
        self._DomainInfoCollection = DomainInfoCollection

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("DomainInfoCollection") is not None:
            self._DomainInfoCollection = []
            for item in params.get("DomainInfoCollection"):
                obj = DomainInfo()
                obj._deserialize(item)
                self._DomainInfoCollection.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEventDetailRequest(AbstractModel):
    r"""DescribeEventDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Index: 事件索引名
        :type Index: str
        :param _Id: 事件id
        :type Id: str
        :param _Source: 事件来源
        :type Source: str
        :param _SubEventType: 事件子类型
        :type SubEventType: int
        :param _Name: 事件名称
        :type Name: str
        """
        self._Index = None
        self._Id = None
        self._Source = None
        self._SubEventType = None
        self._Name = None

    @property
    def Index(self):
        r"""事件索引名
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Id(self):
        r"""事件id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Source(self):
        r"""事件来源
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SubEventType(self):
        r"""事件子类型
        :rtype: int
        """
        return self._SubEventType

    @SubEventType.setter
    def SubEventType(self, SubEventType):
        self._SubEventType = SubEventType

    @property
    def Name(self):
        r"""事件名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Id = params.get("Id")
        self._Source = params.get("Source")
        self._SubEventType = params.get("SubEventType")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEventDetailResponse(AbstractModel):
    r"""DescribeEventDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 事件详情
        :type Data: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""事件详情
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeLeakDetectionListRequest(AbstractModel):
    r"""DescribeLeakDetectionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 筛选条件
        :type Filters: list of Filter
        :param _Limit: 每页数量
        :type Limit: int
        :param _Page: 页码
        :type Page: int
        :param _StartTime: 起始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        """
        self._Filters = None
        self._Limit = None
        self._Page = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Filters(self):
        r"""筛选条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""每页数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Page(self):
        r"""页码
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def StartTime(self):
        r"""起始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Page = params.get("Page")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLeakDetectionListResponse(AbstractModel):
    r"""DescribeLeakDetectionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _List: 数据列表
        :type List: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._List = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        r"""数据列表
        :rtype: list of str
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._List = params.get("List")
        self._RequestId = params.get("RequestId")


class DescribeMappingResultsRequest(AbstractModel):
    r"""DescribeMappingResults请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 过滤条件，FilterKey 取值范围：AssetId，AssetIp，PrivateIp，Protocol，Service，OS，Process，Component，AssetType，Domain，Port，LastMappingTime，MappingType，Disposal，Vpc
        :type Filter: list of AssetQueryFilter
        :param _Sorter: 排序条件，SortKey取值范围：CreateTime，LastMappingTime
        :type Sorter: list of QuerySort
        :param _PageIndex: 页码
        :type PageIndex: int
        :param _PageSize: 页大小，默认大小20
        :type PageSize: int
        """
        self._Filter = None
        self._Sorter = None
        self._PageIndex = None
        self._PageSize = None

    @property
    def Filter(self):
        r"""过滤条件，FilterKey 取值范围：AssetId，AssetIp，PrivateIp，Protocol，Service，OS，Process，Component，AssetType，Domain，Port，LastMappingTime，MappingType，Disposal，Vpc
        :rtype: list of AssetQueryFilter
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Sorter(self):
        r"""排序条件，SortKey取值范围：CreateTime，LastMappingTime
        :rtype: list of QuerySort
        """
        return self._Sorter

    @Sorter.setter
    def Sorter(self, Sorter):
        self._Sorter = Sorter

    @property
    def PageIndex(self):
        r"""页码
        :rtype: int
        """
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex

    @property
    def PageSize(self):
        r"""页大小，默认大小20
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = AssetQueryFilter()
                obj._deserialize(item)
                self._Filter.append(obj)
        if params.get("Sorter") is not None:
            self._Sorter = []
            for item in params.get("Sorter"):
                obj = QuerySort()
                obj._deserialize(item)
                self._Sorter.append(obj)
        self._PageIndex = params.get("PageIndex")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMappingResultsResponse(AbstractModel):
    r"""DescribeMappingResults返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Data: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ssa.v20180608.models.Results`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        r"""列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssa.v20180608.models.Results`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = Results()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeSocAlertDetailsRequest(AbstractModel):
    r"""DescribeSocAlertDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AlertId: 告警id
        :type AlertId: str
        :param _AlertTimestamp: 告警时间，取Timestamp字段
        :type AlertTimestamp: str
        """
        self._AlertId = None
        self._AlertTimestamp = None

    @property
    def AlertId(self):
        r"""告警id
        :rtype: str
        """
        return self._AlertId

    @AlertId.setter
    def AlertId(self, AlertId):
        self._AlertId = AlertId

    @property
    def AlertTimestamp(self):
        r"""告警时间，取Timestamp字段
        :rtype: str
        """
        return self._AlertTimestamp

    @AlertTimestamp.setter
    def AlertTimestamp(self, AlertTimestamp):
        self._AlertTimestamp = AlertTimestamp


    def _deserialize(self, params):
        self._AlertId = params.get("AlertId")
        self._AlertTimestamp = params.get("AlertTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSocAlertDetailsResponse(AbstractModel):
    r"""DescribeSocAlertDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回详情数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ssa.v20180608.models.AlertDetail`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""返回详情数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssa.v20180608.models.AlertDetail`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AlertDetail()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeSocAlertListRequest(AbstractModel):
    r"""DescribeSocAlertList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageSize: 页大小
        :type PageSize: int
        :param _PageIndex: 页码
        :type PageIndex: int
        :param _Scenes: 1:急需关注 2.重保监控 3.全量告警
        :type Scenes: int
        :param _Filter: 查询参数
        :type Filter: list of QueryFilter
        :param _Sorter: 排序参数
        :type Sorter: list of QuerySort
        :param _ExportFlag: 是否导出；默认为否，如量级超过1000，则使用单独的导出接口
        :type ExportFlag: bool
        """
        self._PageSize = None
        self._PageIndex = None
        self._Scenes = None
        self._Filter = None
        self._Sorter = None
        self._ExportFlag = None

    @property
    def PageSize(self):
        r"""页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageIndex(self):
        r"""页码
        :rtype: int
        """
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex

    @property
    def Scenes(self):
        r"""1:急需关注 2.重保监控 3.全量告警
        :rtype: int
        """
        return self._Scenes

    @Scenes.setter
    def Scenes(self, Scenes):
        self._Scenes = Scenes

    @property
    def Filter(self):
        r"""查询参数
        :rtype: list of QueryFilter
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Sorter(self):
        r"""排序参数
        :rtype: list of QuerySort
        """
        return self._Sorter

    @Sorter.setter
    def Sorter(self, Sorter):
        self._Sorter = Sorter

    @property
    def ExportFlag(self):
        r"""是否导出；默认为否，如量级超过1000，则使用单独的导出接口
        :rtype: bool
        """
        return self._ExportFlag

    @ExportFlag.setter
    def ExportFlag(self, ExportFlag):
        self._ExportFlag = ExportFlag


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageIndex = params.get("PageIndex")
        self._Scenes = params.get("Scenes")
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = QueryFilter()
                obj._deserialize(item)
                self._Filter.append(obj)
        if params.get("Sorter") is not None:
            self._Sorter = []
            for item in params.get("Sorter"):
                obj = QuerySort()
                obj._deserialize(item)
                self._Sorter.append(obj)
        self._ExportFlag = params.get("ExportFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSocAlertListResponse(AbstractModel):
    r"""DescribeSocAlertList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务数据
        :type Data: :class:`tencentcloud.ssa.v20180608.models.AlertListData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""业务数据
        :rtype: :class:`tencentcloud.ssa.v20180608.models.AlertListData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AlertListData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeSocCheckItemListRequest(AbstractModel):
    r"""DescribeSocCheckItemList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 查询参数,可支持的排序字段:Name,Type,AssetType,Level,Standard,IsFree
        :type Filter: list of QueryFilter
        :param _Sorter: 排序参数:无
        :type Sorter: list of QuerySort
        :param _PageSize: 当前页码数据，默认值为10
        :type PageSize: int
        :param _PageIndex: 当前页面索引，默认值为0
        :type PageIndex: int
        """
        self._Filter = None
        self._Sorter = None
        self._PageSize = None
        self._PageIndex = None

    @property
    def Filter(self):
        r"""查询参数,可支持的排序字段:Name,Type,AssetType,Level,Standard,IsFree
        :rtype: list of QueryFilter
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Sorter(self):
        r"""排序参数:无
        :rtype: list of QuerySort
        """
        return self._Sorter

    @Sorter.setter
    def Sorter(self, Sorter):
        self._Sorter = Sorter

    @property
    def PageSize(self):
        r"""当前页码数据，默认值为10
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageIndex(self):
        r"""当前页面索引，默认值为0
        :rtype: int
        """
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = QueryFilter()
                obj._deserialize(item)
                self._Filter.append(obj)
        if params.get("Sorter") is not None:
            self._Sorter = []
            for item in params.get("Sorter"):
                obj = QuerySort()
                obj._deserialize(item)
                self._Sorter.append(obj)
        self._PageSize = params.get("PageSize")
        self._PageIndex = params.get("PageIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSocCheckItemListResponse(AbstractModel):
    r"""DescribeSocCheckItemList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 检查项列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ssa.v20180608.models.DescribeSocCheckItemListRspRsp`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""检查项列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssa.v20180608.models.DescribeSocCheckItemListRspRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeSocCheckItemListRspRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeSocCheckItemListRspRsp(AbstractModel):
    r"""云安全配置检查项列表

    """

    def __init__(self):
        r"""
        :param _List: 检查项详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of SocCheckItemV1
        :param _Total: 检查项总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        """
        self._List = None
        self._Total = None

    @property
    def List(self):
        r"""检查项详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SocCheckItemV1
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        r"""检查项总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = SocCheckItemV1()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSocCheckResultListRequest(AbstractModel):
    r"""DescribeSocCheckResultList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 查询参数,可支持的查询参数：
Name,Type,AssetType,Result,PloyName,PloyId
        :type Filter: list of QueryFilter
        :param _Sorter: 排序参数,可支持的排序参数：CheckStatus,RiskCount
        :type Sorter: list of QuerySort
        :param _PageSize: 当前页码数据，默认值为10
        :type PageSize: int
        :param _PageIndex: 当前页面索引，默认值为0
        :type PageIndex: int
        :param _AssetId: 资产id
        :type AssetId: str
        """
        self._Filter = None
        self._Sorter = None
        self._PageSize = None
        self._PageIndex = None
        self._AssetId = None

    @property
    def Filter(self):
        r"""查询参数,可支持的查询参数：
Name,Type,AssetType,Result,PloyName,PloyId
        :rtype: list of QueryFilter
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Sorter(self):
        r"""排序参数,可支持的排序参数：CheckStatus,RiskCount
        :rtype: list of QuerySort
        """
        return self._Sorter

    @Sorter.setter
    def Sorter(self, Sorter):
        self._Sorter = Sorter

    @property
    def PageSize(self):
        r"""当前页码数据，默认值为10
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageIndex(self):
        r"""当前页面索引，默认值为0
        :rtype: int
        """
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex

    @property
    def AssetId(self):
        r"""资产id
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = QueryFilter()
                obj._deserialize(item)
                self._Filter.append(obj)
        if params.get("Sorter") is not None:
            self._Sorter = []
            for item in params.get("Sorter"):
                obj = QuerySort()
                obj._deserialize(item)
                self._Sorter.append(obj)
        self._PageSize = params.get("PageSize")
        self._PageIndex = params.get("PageIndex")
        self._AssetId = params.get("AssetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSocCheckResultListResponse(AbstractModel):
    r"""DescribeSocCheckResultList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ssa.v20180608.models.DescribeSocCheckResultListRspRsp`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""无
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssa.v20180608.models.DescribeSocCheckResultListRspRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeSocCheckResultListRspRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeSocCheckResultListRspRsp(AbstractModel):
    r"""检查项结果详情列表

    """

    def __init__(self):
        r"""
        :param _List: 具体检查项详情
        :type List: list of SocCheckResult
        :param _Total: 检查结果总数
        :type Total: int
        :param _LowTotal: 低危个数
        :type LowTotal: int
        :param _MiddleTotal: 中危个数
        :type MiddleTotal: int
        :param _HighTotal: 高危个数
        :type HighTotal: int
        :param _NormalTotal: 正常个数
        :type NormalTotal: int
        """
        self._List = None
        self._Total = None
        self._LowTotal = None
        self._MiddleTotal = None
        self._HighTotal = None
        self._NormalTotal = None

    @property
    def List(self):
        r"""具体检查项详情
        :rtype: list of SocCheckResult
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        r"""检查结果总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def LowTotal(self):
        r"""低危个数
        :rtype: int
        """
        return self._LowTotal

    @LowTotal.setter
    def LowTotal(self, LowTotal):
        self._LowTotal = LowTotal

    @property
    def MiddleTotal(self):
        r"""中危个数
        :rtype: int
        """
        return self._MiddleTotal

    @MiddleTotal.setter
    def MiddleTotal(self, MiddleTotal):
        self._MiddleTotal = MiddleTotal

    @property
    def HighTotal(self):
        r"""高危个数
        :rtype: int
        """
        return self._HighTotal

    @HighTotal.setter
    def HighTotal(self, HighTotal):
        self._HighTotal = HighTotal

    @property
    def NormalTotal(self):
        r"""正常个数
        :rtype: int
        """
        return self._NormalTotal

    @NormalTotal.setter
    def NormalTotal(self, NormalTotal):
        self._NormalTotal = NormalTotal


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = SocCheckResult()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._LowTotal = params.get("LowTotal")
        self._MiddleTotal = params.get("MiddleTotal")
        self._HighTotal = params.get("HighTotal")
        self._NormalTotal = params.get("NormalTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSocCspmComplianceRequest(AbstractModel):
    r"""DescribeSocCspmCompliance请求参数结构体

    """


class DescribeSocCspmComplianceResponse(AbstractModel):
    r"""DescribeSocCspmCompliance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ssa.v20180608.models.SocComplianceInfoResp`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssa.v20180608.models.SocComplianceInfoResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = SocComplianceInfoResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeVulDetailRequest(AbstractModel):
    r"""DescribeVulDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UniqId: 漏洞唯一标识符
        :type UniqId: str
        :param _Source: 查看详情来源
        :type Source: str
        """
        self._UniqId = None
        self._Source = None

    @property
    def UniqId(self):
        r"""漏洞唯一标识符
        :rtype: str
        """
        return self._UniqId

    @UniqId.setter
    def UniqId(self, UniqId):
        self._UniqId = UniqId

    @property
    def Source(self):
        r"""查看详情来源
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source


    def _deserialize(self, params):
        self._UniqId = params.get("UniqId")
        self._Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulDetailResponse(AbstractModel):
    r"""DescribeVulDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VulType: 漏洞类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VulType: int
        :param _SubVulType: 漏洞子类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SubVulType: str
        :param _CvssScore: cvss分数
注意：此字段可能返回 null，表示取不到有效值。
        :type CvssScore: str
        :param _Cvss: cvss值
注意：此字段可能返回 null，表示取不到有效值。
        :type Cvss: str
        :param _Cve: cve编号
注意：此字段可能返回 null，表示取不到有效值。
        :type Cve: str
        :param _Cnvd: cnvd编号
注意：此字段可能返回 null，表示取不到有效值。
        :type Cnvd: str
        :param _Cnnvd: cnnvd编号
注意：此字段可能返回 null，表示取不到有效值。
        :type Cnnvd: str
        :param _Desc: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param _Reference: 参考
注意：此字段可能返回 null，表示取不到有效值。
        :type Reference: str
        :param _Repair: 修复意见
注意：此字段可能返回 null，表示取不到有效值。
        :type Repair: str
        :param _ReleaseTime: 披露时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Name: 漏洞名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Level: 等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _ImpactAsset: 受影响资产唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type ImpactAsset: str
        :param _ImpactAssetName: 受影响资产名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ImpactAssetName: str
        :param _IsAssetDeleted: 受影响资产是否已删除
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAssetDeleted: bool
        :param _Source: 漏洞来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _VulUrl: 漏洞URL
注意：此字段可能返回 null，表示取不到有效值。
        :type VulUrl: str
        :param _SsaAssetCategory: 资产归属
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaAssetCategory: int
        :param _VulPath: 资产文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :type VulPath: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VulType = None
        self._SubVulType = None
        self._CvssScore = None
        self._Cvss = None
        self._Cve = None
        self._Cnvd = None
        self._Cnnvd = None
        self._Desc = None
        self._Reference = None
        self._Repair = None
        self._ReleaseTime = None
        self._UpdateTime = None
        self._Name = None
        self._Level = None
        self._Status = None
        self._ImpactAsset = None
        self._ImpactAssetName = None
        self._IsAssetDeleted = None
        self._Source = None
        self._VulUrl = None
        self._SsaAssetCategory = None
        self._VulPath = None
        self._RequestId = None

    @property
    def VulType(self):
        r"""漏洞类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._VulType

    @VulType.setter
    def VulType(self, VulType):
        self._VulType = VulType

    @property
    def SubVulType(self):
        r"""漏洞子类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubVulType

    @SubVulType.setter
    def SubVulType(self, SubVulType):
        self._SubVulType = SubVulType

    @property
    def CvssScore(self):
        r"""cvss分数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CvssScore

    @CvssScore.setter
    def CvssScore(self, CvssScore):
        self._CvssScore = CvssScore

    @property
    def Cvss(self):
        r"""cvss值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Cvss

    @Cvss.setter
    def Cvss(self, Cvss):
        self._Cvss = Cvss

    @property
    def Cve(self):
        r"""cve编号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Cve

    @Cve.setter
    def Cve(self, Cve):
        self._Cve = Cve

    @property
    def Cnvd(self):
        r"""cnvd编号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Cnvd

    @Cnvd.setter
    def Cnvd(self, Cnvd):
        self._Cnvd = Cnvd

    @property
    def Cnnvd(self):
        r"""cnnvd编号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Cnnvd

    @Cnnvd.setter
    def Cnnvd(self, Cnnvd):
        self._Cnnvd = Cnnvd

    @property
    def Desc(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Reference(self):
        r"""参考
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Reference

    @Reference.setter
    def Reference(self, Reference):
        self._Reference = Reference

    @property
    def Repair(self):
        r"""修复意见
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Repair

    @Repair.setter
    def Repair(self, Repair):
        self._Repair = Repair

    @property
    def ReleaseTime(self):
        r"""披露时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ReleaseTime

    @ReleaseTime.setter
    def ReleaseTime(self, ReleaseTime):
        self._ReleaseTime = ReleaseTime

    @property
    def UpdateTime(self):
        r"""更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Name(self):
        r"""漏洞名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Level(self):
        r"""等级
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Status(self):
        r"""状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ImpactAsset(self):
        r"""受影响资产唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ImpactAsset

    @ImpactAsset.setter
    def ImpactAsset(self, ImpactAsset):
        self._ImpactAsset = ImpactAsset

    @property
    def ImpactAssetName(self):
        r"""受影响资产名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ImpactAssetName

    @ImpactAssetName.setter
    def ImpactAssetName(self, ImpactAssetName):
        self._ImpactAssetName = ImpactAssetName

    @property
    def IsAssetDeleted(self):
        r"""受影响资产是否已删除
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsAssetDeleted

    @IsAssetDeleted.setter
    def IsAssetDeleted(self, IsAssetDeleted):
        self._IsAssetDeleted = IsAssetDeleted

    @property
    def Source(self):
        r"""漏洞来源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def VulUrl(self):
        r"""漏洞URL
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VulUrl

    @VulUrl.setter
    def VulUrl(self, VulUrl):
        self._VulUrl = VulUrl

    @property
    def SsaAssetCategory(self):
        r"""资产归属
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SsaAssetCategory

    @SsaAssetCategory.setter
    def SsaAssetCategory(self, SsaAssetCategory):
        self._SsaAssetCategory = SsaAssetCategory

    @property
    def VulPath(self):
        r"""资产文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VulPath

    @VulPath.setter
    def VulPath(self, VulPath):
        self._VulPath = VulPath

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VulType = params.get("VulType")
        self._SubVulType = params.get("SubVulType")
        self._CvssScore = params.get("CvssScore")
        self._Cvss = params.get("Cvss")
        self._Cve = params.get("Cve")
        self._Cnvd = params.get("Cnvd")
        self._Cnnvd = params.get("Cnnvd")
        self._Desc = params.get("Desc")
        self._Reference = params.get("Reference")
        self._Repair = params.get("Repair")
        self._ReleaseTime = params.get("ReleaseTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Name = params.get("Name")
        self._Level = params.get("Level")
        self._Status = params.get("Status")
        self._ImpactAsset = params.get("ImpactAsset")
        self._ImpactAssetName = params.get("ImpactAssetName")
        self._IsAssetDeleted = params.get("IsAssetDeleted")
        self._Source = params.get("Source")
        self._VulUrl = params.get("VulUrl")
        self._SsaAssetCategory = params.get("SsaAssetCategory")
        self._VulPath = params.get("VulPath")
        self._RequestId = params.get("RequestId")


class DescribeVulListRequest(AbstractModel):
    r"""DescribeVulList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Params: 查询过滤参数:(json序列化的结果）
        :type Params: str
        """
        self._Params = None

    @property
    def Params(self):
        r"""查询过滤参数:(json序列化的结果）
        :rtype: str
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._Params = params.get("Params")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulListResponse(AbstractModel):
    r"""DescribeVulList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 漏洞列表
        :type Data: :class:`tencentcloud.ssa.v20180608.models.VulList`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""漏洞列表
        :rtype: :class:`tencentcloud.ssa.v20180608.models.VulList`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = VulList()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DomainInfo(AbstractModel):
    r"""域名列表

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _ResolveAddr: 解析地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ResolveAddr: list of str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: list of str
        :param _AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: list of str
        :param _RiskVulCount: 漏洞风险
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskVulCount: int
        :param _SensitiveCount: 敏感内容
注意：此字段可能返回 null，表示取不到有效值。
        :type SensitiveCount: int
        :param _HorseLinkCount: 挂马暗链
注意：此字段可能返回 null，表示取不到有效值。
        :type HorseLinkCount: int
        :param _WebModifyCount: 网页篡改
        :type WebModifyCount: int
        :param _ScanTime: 上次扫描时间
        :type ScanTime: str
        :param _DiscoverTime: 最近发现时间
        :type DiscoverTime: str
        :param _ScanTaskCount: 扫描次数
        :type ScanTaskCount: int
        :param _PortRisk: 端口
        :type PortRisk: int
        :param _WeekPwdCount: 弱口令
        :type WeekPwdCount: int
        :param _AssetLocation: 资产归属
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetLocation: str
        :param _NetworkRisk: 网络风险
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkRisk: int
        :param _NetworkAttack: 网络攻击
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkAttack: int
        :param _BotVisit: bot访问
注意：此字段可能返回 null，表示取不到有效值。
        :type BotVisit: int
        :param _NetworkAccess: 网络访问

注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkAccess: int
        :param _CreateTime: 资产创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _WafStatus: waf状态
注意：此字段可能返回 null，表示取不到有效值。
        :type WafStatus: int
        :param _LastScanTime: 最近扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastScanTime: str
        :param _AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: list of str
        :param _AssetName: 资产名
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: list of str
        :param _SourceType: 类别
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceType: str
        :param _IsNotCore: 是否核心资产
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNotCore: int
        :param _IsCloud: 是否云外资产
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCloud: int
        """
        self._Domain = None
        self._ResolveAddr = None
        self._Region = None
        self._AssetType = None
        self._RiskVulCount = None
        self._SensitiveCount = None
        self._HorseLinkCount = None
        self._WebModifyCount = None
        self._ScanTime = None
        self._DiscoverTime = None
        self._ScanTaskCount = None
        self._PortRisk = None
        self._WeekPwdCount = None
        self._AssetLocation = None
        self._NetworkRisk = None
        self._NetworkAttack = None
        self._BotVisit = None
        self._NetworkAccess = None
        self._CreateTime = None
        self._WafStatus = None
        self._LastScanTime = None
        self._AssetId = None
        self._AssetName = None
        self._SourceType = None
        self._IsNotCore = None
        self._IsCloud = None

    @property
    def Domain(self):
        r"""域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ResolveAddr(self):
        r"""解析地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ResolveAddr

    @ResolveAddr.setter
    def ResolveAddr(self, ResolveAddr):
        self._ResolveAddr = ResolveAddr

    @property
    def Region(self):
        r"""地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AssetType(self):
        r"""资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def RiskVulCount(self):
        r"""漏洞风险
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RiskVulCount

    @RiskVulCount.setter
    def RiskVulCount(self, RiskVulCount):
        self._RiskVulCount = RiskVulCount

    @property
    def SensitiveCount(self):
        r"""敏感内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SensitiveCount

    @SensitiveCount.setter
    def SensitiveCount(self, SensitiveCount):
        self._SensitiveCount = SensitiveCount

    @property
    def HorseLinkCount(self):
        r"""挂马暗链
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._HorseLinkCount

    @HorseLinkCount.setter
    def HorseLinkCount(self, HorseLinkCount):
        self._HorseLinkCount = HorseLinkCount

    @property
    def WebModifyCount(self):
        r"""网页篡改
        :rtype: int
        """
        return self._WebModifyCount

    @WebModifyCount.setter
    def WebModifyCount(self, WebModifyCount):
        self._WebModifyCount = WebModifyCount

    @property
    def ScanTime(self):
        r"""上次扫描时间
        :rtype: str
        """
        return self._ScanTime

    @ScanTime.setter
    def ScanTime(self, ScanTime):
        self._ScanTime = ScanTime

    @property
    def DiscoverTime(self):
        r"""最近发现时间
        :rtype: str
        """
        return self._DiscoverTime

    @DiscoverTime.setter
    def DiscoverTime(self, DiscoverTime):
        self._DiscoverTime = DiscoverTime

    @property
    def ScanTaskCount(self):
        r"""扫描次数
        :rtype: int
        """
        return self._ScanTaskCount

    @ScanTaskCount.setter
    def ScanTaskCount(self, ScanTaskCount):
        self._ScanTaskCount = ScanTaskCount

    @property
    def PortRisk(self):
        r"""端口
        :rtype: int
        """
        return self._PortRisk

    @PortRisk.setter
    def PortRisk(self, PortRisk):
        self._PortRisk = PortRisk

    @property
    def WeekPwdCount(self):
        r"""弱口令
        :rtype: int
        """
        return self._WeekPwdCount

    @WeekPwdCount.setter
    def WeekPwdCount(self, WeekPwdCount):
        self._WeekPwdCount = WeekPwdCount

    @property
    def AssetLocation(self):
        r"""资产归属
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetLocation

    @AssetLocation.setter
    def AssetLocation(self, AssetLocation):
        self._AssetLocation = AssetLocation

    @property
    def NetworkRisk(self):
        r"""网络风险
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NetworkRisk

    @NetworkRisk.setter
    def NetworkRisk(self, NetworkRisk):
        self._NetworkRisk = NetworkRisk

    @property
    def NetworkAttack(self):
        r"""网络攻击
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NetworkAttack

    @NetworkAttack.setter
    def NetworkAttack(self, NetworkAttack):
        self._NetworkAttack = NetworkAttack

    @property
    def BotVisit(self):
        r"""bot访问
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BotVisit

    @BotVisit.setter
    def BotVisit(self, BotVisit):
        self._BotVisit = BotVisit

    @property
    def NetworkAccess(self):
        r"""网络访问

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NetworkAccess

    @NetworkAccess.setter
    def NetworkAccess(self, NetworkAccess):
        self._NetworkAccess = NetworkAccess

    @property
    def CreateTime(self):
        r"""资产创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def WafStatus(self):
        r"""waf状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._WafStatus

    @WafStatus.setter
    def WafStatus(self, WafStatus):
        self._WafStatus = WafStatus

    @property
    def LastScanTime(self):
        r"""最近扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def AssetId(self):
        r"""资产id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def AssetName(self):
        r"""资产名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def SourceType(self):
        r"""类别
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def IsNotCore(self):
        r"""是否核心资产
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsNotCore

    @IsNotCore.setter
    def IsNotCore(self, IsNotCore):
        self._IsNotCore = IsNotCore

    @property
    def IsCloud(self):
        r"""是否云外资产
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsCloud

    @IsCloud.setter
    def IsCloud(self, IsCloud):
        self._IsCloud = IsCloud


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._ResolveAddr = params.get("ResolveAddr")
        self._Region = params.get("Region")
        self._AssetType = params.get("AssetType")
        self._RiskVulCount = params.get("RiskVulCount")
        self._SensitiveCount = params.get("SensitiveCount")
        self._HorseLinkCount = params.get("HorseLinkCount")
        self._WebModifyCount = params.get("WebModifyCount")
        self._ScanTime = params.get("ScanTime")
        self._DiscoverTime = params.get("DiscoverTime")
        self._ScanTaskCount = params.get("ScanTaskCount")
        self._PortRisk = params.get("PortRisk")
        self._WeekPwdCount = params.get("WeekPwdCount")
        self._AssetLocation = params.get("AssetLocation")
        self._NetworkRisk = params.get("NetworkRisk")
        self._NetworkAttack = params.get("NetworkAttack")
        self._BotVisit = params.get("BotVisit")
        self._NetworkAccess = params.get("NetworkAccess")
        self._CreateTime = params.get("CreateTime")
        self._WafStatus = params.get("WafStatus")
        self._LastScanTime = params.get("LastScanTime")
        self._AssetId = params.get("AssetId")
        self._AssetName = params.get("AssetName")
        self._SourceType = params.get("SourceType")
        self._IsNotCore = params.get("IsNotCore")
        self._IsCloud = params.get("IsCloud")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param _Name: 过滤键的名称。
        :type Name: str
        :param _Values: 一个或者多个过滤值。
        :type Values: list of str
        :param _ExactMatch: 是否需要精确匹配
        :type ExactMatch: bool
        """
        self._Name = None
        self._Values = None
        self._ExactMatch = None

    @property
    def Name(self):
        r"""过滤键的名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""一个或者多个过滤值。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def ExactMatch(self):
        r"""是否需要精确匹配
        :rtype: bool
        """
        return self._ExactMatch

    @ExactMatch.setter
    def ExactMatch(self, ExactMatch):
        self._ExactMatch = ExactMatch


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDataSaEventPub(AbstractModel):
    r"""DataSaEventPub

    """

    def __init__(self):
        r"""
        :param _Time: 时间
        :type Time: str
        :param _EventType1: 安全事件1级分类
        :type EventType1: int
        :param _EventType2: 安全事件2级分类
        :type EventType2: int
        :param _EventName: 安全事件名称
        :type EventName: str
        :param _Level: 风险等级
        :type Level: int
        :param _Status: 安全事件状态
        :type Status: int
        :param _SrcIp: 攻击源ip
        :type SrcIp: str
        :param _DstIp: 攻击目标ip
        :type DstIp: str
        :param _DstPort: 攻击目标端口
        :type DstPort: int
        :param _Asset: 受影响资产
        :type Asset: str
        :param _OldIdMd5: 私有字段和公有字段映射的原始采集数据唯一标识的MD5值
        :type OldIdMd5: str
        """
        self._Time = None
        self._EventType1 = None
        self._EventType2 = None
        self._EventName = None
        self._Level = None
        self._Status = None
        self._SrcIp = None
        self._DstIp = None
        self._DstPort = None
        self._Asset = None
        self._OldIdMd5 = None

    @property
    def Time(self):
        r"""时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def EventType1(self):
        r"""安全事件1级分类
        :rtype: int
        """
        return self._EventType1

    @EventType1.setter
    def EventType1(self, EventType1):
        self._EventType1 = EventType1

    @property
    def EventType2(self):
        r"""安全事件2级分类
        :rtype: int
        """
        return self._EventType2

    @EventType2.setter
    def EventType2(self, EventType2):
        self._EventType2 = EventType2

    @property
    def EventName(self):
        r"""安全事件名称
        :rtype: str
        """
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def Level(self):
        r"""风险等级
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Status(self):
        r"""安全事件状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SrcIp(self):
        r"""攻击源ip
        :rtype: str
        """
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def DstIp(self):
        r"""攻击目标ip
        :rtype: str
        """
        return self._DstIp

    @DstIp.setter
    def DstIp(self, DstIp):
        self._DstIp = DstIp

    @property
    def DstPort(self):
        r"""攻击目标端口
        :rtype: int
        """
        return self._DstPort

    @DstPort.setter
    def DstPort(self, DstPort):
        self._DstPort = DstPort

    @property
    def Asset(self):
        r"""受影响资产
        :rtype: str
        """
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset

    @property
    def OldIdMd5(self):
        r"""私有字段和公有字段映射的原始采集数据唯一标识的MD5值
        :rtype: str
        """
        return self._OldIdMd5

    @OldIdMd5.setter
    def OldIdMd5(self, OldIdMd5):
        self._OldIdMd5 = OldIdMd5


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._EventType1 = params.get("EventType1")
        self._EventType2 = params.get("EventType2")
        self._EventName = params.get("EventName")
        self._Level = params.get("Level")
        self._Status = params.get("Status")
        self._SrcIp = params.get("SrcIp")
        self._DstIp = params.get("DstIp")
        self._DstPort = params.get("DstPort")
        self._Asset = params.get("Asset")
        self._OldIdMd5 = params.get("OldIdMd5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MappingResult(AbstractModel):
    r"""测绘记录

    """

    def __init__(self):
        r"""
        :param _AssetName: 资产名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetName: str
        :param _AssetIp: 公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetIp: str
        :param _PrivateIp: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param _AssetId: 资产id
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetId: str
        :param _Protocol: 协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: str
        :param _Service: 服务
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: str
        :param _Component: 组件
注意：此字段可能返回 null，表示取不到有效值。
        :type Component: str
        :param _Process: 进程
注意：此字段可能返回 null，表示取不到有效值。
        :type Process: str
        :param _OS: 操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :type OS: str
        :param _LastMappingTime: 测绘时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastMappingTime: str
        :param _DisposalRecommendations: 处置建议
注意：此字段可能返回 null，表示取不到有效值。
        :type DisposalRecommendations: str
        :param _DisposalRecommendationDetails: 处置建议详情
注意：此字段可能返回 null，表示取不到有效值。
        :type DisposalRecommendationDetails: str
        :param _AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param _Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _MappingStatus: 测绘状态
注意：此字段可能返回 null，表示取不到有效值。
        :type MappingStatus: int
        :param _Region: 区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _SecurityStatus: 安全防护状态
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityStatus: list of SecurityStatus
        :param _DisposalRecommendation: 处置建议
注意：此字段可能返回 null，表示取不到有效值。
        :type DisposalRecommendation: int
        :param _MappingType: 测绘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type MappingType: str
        """
        self._AssetName = None
        self._AssetIp = None
        self._PrivateIp = None
        self._AssetId = None
        self._Protocol = None
        self._Port = None
        self._Service = None
        self._Component = None
        self._Process = None
        self._OS = None
        self._LastMappingTime = None
        self._DisposalRecommendations = None
        self._DisposalRecommendationDetails = None
        self._AssetType = None
        self._Domain = None
        self._MappingStatus = None
        self._Region = None
        self._SecurityStatus = None
        self._DisposalRecommendation = None
        self._MappingType = None

    @property
    def AssetName(self):
        r"""资产名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetName

    @AssetName.setter
    def AssetName(self, AssetName):
        self._AssetName = AssetName

    @property
    def AssetIp(self):
        r"""公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetIp

    @AssetIp.setter
    def AssetIp(self, AssetIp):
        self._AssetIp = AssetIp

    @property
    def PrivateIp(self):
        r"""内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def AssetId(self):
        r"""资产id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def Protocol(self):
        r"""协议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        r"""端口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Service(self):
        r"""服务
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Component(self):
        r"""组件
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Component

    @Component.setter
    def Component(self, Component):
        self._Component = Component

    @property
    def Process(self):
        r"""进程
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Process

    @Process.setter
    def Process(self, Process):
        self._Process = Process

    @property
    def OS(self):
        r"""操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OS

    @OS.setter
    def OS(self, OS):
        self._OS = OS

    @property
    def LastMappingTime(self):
        r"""测绘时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastMappingTime

    @LastMappingTime.setter
    def LastMappingTime(self, LastMappingTime):
        self._LastMappingTime = LastMappingTime

    @property
    def DisposalRecommendations(self):
        r"""处置建议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DisposalRecommendations

    @DisposalRecommendations.setter
    def DisposalRecommendations(self, DisposalRecommendations):
        self._DisposalRecommendations = DisposalRecommendations

    @property
    def DisposalRecommendationDetails(self):
        r"""处置建议详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DisposalRecommendationDetails

    @DisposalRecommendationDetails.setter
    def DisposalRecommendationDetails(self, DisposalRecommendationDetails):
        self._DisposalRecommendationDetails = DisposalRecommendationDetails

    @property
    def AssetType(self):
        r"""资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Domain(self):
        r"""域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def MappingStatus(self):
        r"""测绘状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MappingStatus

    @MappingStatus.setter
    def MappingStatus(self, MappingStatus):
        self._MappingStatus = MappingStatus

    @property
    def Region(self):
        r"""区域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SecurityStatus(self):
        r"""安全防护状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SecurityStatus
        """
        return self._SecurityStatus

    @SecurityStatus.setter
    def SecurityStatus(self, SecurityStatus):
        self._SecurityStatus = SecurityStatus

    @property
    def DisposalRecommendation(self):
        r"""处置建议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DisposalRecommendation

    @DisposalRecommendation.setter
    def DisposalRecommendation(self, DisposalRecommendation):
        self._DisposalRecommendation = DisposalRecommendation

    @property
    def MappingType(self):
        r"""测绘类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MappingType

    @MappingType.setter
    def MappingType(self, MappingType):
        self._MappingType = MappingType


    def _deserialize(self, params):
        self._AssetName = params.get("AssetName")
        self._AssetIp = params.get("AssetIp")
        self._PrivateIp = params.get("PrivateIp")
        self._AssetId = params.get("AssetId")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._Service = params.get("Service")
        self._Component = params.get("Component")
        self._Process = params.get("Process")
        self._OS = params.get("OS")
        self._LastMappingTime = params.get("LastMappingTime")
        self._DisposalRecommendations = params.get("DisposalRecommendations")
        self._DisposalRecommendationDetails = params.get("DisposalRecommendationDetails")
        self._AssetType = params.get("AssetType")
        self._Domain = params.get("Domain")
        self._MappingStatus = params.get("MappingStatus")
        self._Region = params.get("Region")
        if params.get("SecurityStatus") is not None:
            self._SecurityStatus = []
            for item in params.get("SecurityStatus"):
                obj = SecurityStatus()
                obj._deserialize(item)
                self._SecurityStatus.append(obj)
        self._DisposalRecommendation = params.get("DisposalRecommendation")
        self._MappingType = params.get("MappingType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjDataSaEventPub(AbstractModel):
    r"""DataSaEventPub

    """

    def __init__(self):
        r"""
        :param _Count: Count
        :type Count: int
        :param _List: List
        :type List: list of ListDataSaEventPub
        """
        self._Count = None
        self._List = None

    @property
    def Count(self):
        r"""Count
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def List(self):
        r"""List
        :rtype: list of ListDataSaEventPub
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._Count = params.get("Count")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ListDataSaEventPub()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFilter(AbstractModel):
    r"""过滤条件

    """

    def __init__(self):
        r"""
        :param _FilterKey: 过滤key
        :type FilterKey: str
        :param _FilterOperatorType: 操作符(只支持32位)
        :type FilterOperatorType: int
        :param _FilterValue: 过滤value
        :type FilterValue: str
        """
        self._FilterKey = None
        self._FilterOperatorType = None
        self._FilterValue = None

    @property
    def FilterKey(self):
        r"""过滤key
        :rtype: str
        """
        return self._FilterKey

    @FilterKey.setter
    def FilterKey(self, FilterKey):
        self._FilterKey = FilterKey

    @property
    def FilterOperatorType(self):
        r"""操作符(只支持32位)
        :rtype: int
        """
        return self._FilterOperatorType

    @FilterOperatorType.setter
    def FilterOperatorType(self, FilterOperatorType):
        self._FilterOperatorType = FilterOperatorType

    @property
    def FilterValue(self):
        r"""过滤value
        :rtype: str
        """
        return self._FilterValue

    @FilterValue.setter
    def FilterValue(self, FilterValue):
        self._FilterValue = FilterValue


    def _deserialize(self, params):
        self._FilterKey = params.get("FilterKey")
        self._FilterOperatorType = params.get("FilterOperatorType")
        self._FilterValue = params.get("FilterValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFilterV3(AbstractModel):
    r"""过滤

    """

    def __init__(self):
        r"""
        :param _Filter: 过滤条件
        :type Filter: :class:`tencentcloud.ssa.v20180608.models.QueryFilter`
        :param _HasSub: 有无子条件
        :type HasSub: bool
        :param _SubFilters: 查询条件
        :type SubFilters: list of QueryFilter
        :param _Logic: 逻辑操作(只支持32位)
        :type Logic: int
        """
        self._Filter = None
        self._HasSub = None
        self._SubFilters = None
        self._Logic = None

    @property
    def Filter(self):
        r"""过滤条件
        :rtype: :class:`tencentcloud.ssa.v20180608.models.QueryFilter`
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def HasSub(self):
        r"""有无子条件
        :rtype: bool
        """
        return self._HasSub

    @HasSub.setter
    def HasSub(self, HasSub):
        self._HasSub = HasSub

    @property
    def SubFilters(self):
        r"""查询条件
        :rtype: list of QueryFilter
        """
        return self._SubFilters

    @SubFilters.setter
    def SubFilters(self, SubFilters):
        self._SubFilters = SubFilters

    @property
    def Logic(self):
        r"""逻辑操作(只支持32位)
        :rtype: int
        """
        return self._Logic

    @Logic.setter
    def Logic(self, Logic):
        self._Logic = Logic


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = QueryFilter()
            self._Filter._deserialize(params.get("Filter"))
        self._HasSub = params.get("HasSub")
        if params.get("SubFilters") is not None:
            self._SubFilters = []
            for item in params.get("SubFilters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self._SubFilters.append(obj)
        self._Logic = params.get("Logic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuerySort(AbstractModel):
    r"""排序的字段

    """

    def __init__(self):
        r"""
        :param _SortKey: 排序字段
        :type SortKey: str
        :param _SortType: 顺序，1升序2降序
        :type SortType: int
        """
        self._SortKey = None
        self._SortType = None

    @property
    def SortKey(self):
        r"""排序字段
        :rtype: str
        """
        return self._SortKey

    @SortKey.setter
    def SortKey(self, SortKey):
        self._SortKey = SortKey

    @property
    def SortType(self):
        r"""顺序，1升序2降序
        :rtype: int
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType


    def _deserialize(self, params):
        self._SortKey = params.get("SortKey")
        self._SortType = params.get("SortType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Results(AbstractModel):
    r"""测绘结果

    """

    def __init__(self):
        r"""
        :param _Statistics: 测绘类型统计
注意：此字段可能返回 null，表示取不到有效值。
        :type Statistics: list of AssetTypeStatistic
        :param _Result: 测绘结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of MappingResult
        :param _TaskCount: 测绘任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskCount: int
        :param _TaskMaxCount: 最大测绘任务数
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskMaxCount: int
        """
        self._Statistics = None
        self._Result = None
        self._TaskCount = None
        self._TaskMaxCount = None

    @property
    def Statistics(self):
        r"""测绘类型统计
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AssetTypeStatistic
        """
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics

    @property
    def Result(self):
        r"""测绘结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MappingResult
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def TaskCount(self):
        r"""测绘任务数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TaskCount

    @TaskCount.setter
    def TaskCount(self, TaskCount):
        self._TaskCount = TaskCount

    @property
    def TaskMaxCount(self):
        r"""最大测绘任务数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TaskMaxCount

    @TaskMaxCount.setter
    def TaskMaxCount(self, TaskMaxCount):
        self._TaskMaxCount = TaskMaxCount


    def _deserialize(self, params):
        if params.get("Statistics") is not None:
            self._Statistics = []
            for item in params.get("Statistics"):
                obj = AssetTypeStatistic()
                obj._deserialize(item)
                self._Statistics.append(obj)
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = MappingResult()
                obj._deserialize(item)
                self._Result.append(obj)
        self._TaskCount = params.get("TaskCount")
        self._TaskMaxCount = params.get("TaskMaxCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaDivulgeScanRuleMutateRequest(AbstractModel):
    r"""SaDivulgeScanRuleMutate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: Id
        :type Id: str
        :param _DivulgeSoure: DivulgeSoure
        :type DivulgeSoure: str
        :param _DivulgeSoureUrl: DivulgeSoureUrl
        :type DivulgeSoureUrl: str
        :param _RuleName: RuleName
        :type RuleName: str
        :param _RuleWord: RuleWord
        :type RuleWord: str
        :param _ScanStatus: ScanStatus
        :type ScanStatus: str
        :param _DivulgeType: DivulgeType
        :type DivulgeType: str
        :param _RepairAdvice: RepairAdvice
        :type RepairAdvice: str
        """
        self._Id = None
        self._DivulgeSoure = None
        self._DivulgeSoureUrl = None
        self._RuleName = None
        self._RuleWord = None
        self._ScanStatus = None
        self._DivulgeType = None
        self._RepairAdvice = None

    @property
    def Id(self):
        r"""Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DivulgeSoure(self):
        r"""DivulgeSoure
        :rtype: str
        """
        return self._DivulgeSoure

    @DivulgeSoure.setter
    def DivulgeSoure(self, DivulgeSoure):
        self._DivulgeSoure = DivulgeSoure

    @property
    def DivulgeSoureUrl(self):
        r"""DivulgeSoureUrl
        :rtype: str
        """
        return self._DivulgeSoureUrl

    @DivulgeSoureUrl.setter
    def DivulgeSoureUrl(self, DivulgeSoureUrl):
        self._DivulgeSoureUrl = DivulgeSoureUrl

    @property
    def RuleName(self):
        r"""RuleName
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleWord(self):
        r"""RuleWord
        :rtype: str
        """
        return self._RuleWord

    @RuleWord.setter
    def RuleWord(self, RuleWord):
        self._RuleWord = RuleWord

    @property
    def ScanStatus(self):
        r"""ScanStatus
        :rtype: str
        """
        return self._ScanStatus

    @ScanStatus.setter
    def ScanStatus(self, ScanStatus):
        self._ScanStatus = ScanStatus

    @property
    def DivulgeType(self):
        r"""DivulgeType
        :rtype: str
        """
        return self._DivulgeType

    @DivulgeType.setter
    def DivulgeType(self, DivulgeType):
        self._DivulgeType = DivulgeType

    @property
    def RepairAdvice(self):
        r"""RepairAdvice
        :rtype: str
        """
        return self._RepairAdvice

    @RepairAdvice.setter
    def RepairAdvice(self, RepairAdvice):
        self._RepairAdvice = RepairAdvice


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DivulgeSoure = params.get("DivulgeSoure")
        self._DivulgeSoureUrl = params.get("DivulgeSoureUrl")
        self._RuleName = params.get("RuleName")
        self._RuleWord = params.get("RuleWord")
        self._ScanStatus = params.get("ScanStatus")
        self._DivulgeType = params.get("DivulgeType")
        self._RepairAdvice = params.get("RepairAdvice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaDivulgeScanRuleMutateResponse(AbstractModel):
    r"""SaDivulgeScanRuleMutate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: Data
        :type Data: :class:`tencentcloud.ssa.v20180608.models.SaDivulgeScanRuleSetList`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Data
        :rtype: :class:`tencentcloud.ssa.v20180608.models.SaDivulgeScanRuleSetList`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = SaDivulgeScanRuleSetList()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class SaDivulgeScanRuleSetList(AbstractModel):
    r"""设置_泄露监测产品监测扫描规则策略

    """

    def __init__(self):
        r"""
        :param _Value: Value
        :type Value: str
        :param _Code: Code
        :type Code: int
        :param _Message: Message
        :type Message: str
        """
        self._Value = None
        self._Code = None
        self._Message = None

    @property
    def Value(self):
        r"""Value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Code(self):
        r"""Code
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""Message
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Value = params.get("Value")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaEventPubRequest(AbstractModel):
    r"""SaEventPub请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Asset: 受影响资产
        :type Asset: str
        :param _EventName: 安全事件名称
        :type EventName: str
        :param _EventType1: 安全事件1级分类，-1:未知 0:全部 1:攻击事件 2:侦查事件 3:僵木蠕毒 4:违规策略
        :type EventType1: int
        :param _EventType2: 安全事件2级分类，-1:未知 0:全部 1:DDOS事件 2:Web攻击 3:木马 4:异地登录 5:密码破解
        :type EventType2: int
        :param _Level: 风险等级，-1:未知 0:全部 1:低危 2:中危 3:高危 4:严重，可多选，如：1,2
        :type Level: str
        :param _Status: 安全事件状态，-1:未知 0:全部 1:待处理 2:已处理 3:误报 4:已忽略 5:已知晓 6:已信任
        :type Status: int
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _Offset: 查询起始地址
        :type Offset: int
        :param _Limit: 查询个数
        :type Limit: int
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _OldIdMd5: 私有字段和公有字段映射的原始采集数据唯一标识的MD5值
        :type OldIdMd5: str
        """
        self._Asset = None
        self._EventName = None
        self._EventType1 = None
        self._EventType2 = None
        self._Level = None
        self._Status = None
        self._StartTime = None
        self._Offset = None
        self._Limit = None
        self._EndTime = None
        self._OldIdMd5 = None

    @property
    def Asset(self):
        r"""受影响资产
        :rtype: str
        """
        return self._Asset

    @Asset.setter
    def Asset(self, Asset):
        self._Asset = Asset

    @property
    def EventName(self):
        r"""安全事件名称
        :rtype: str
        """
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def EventType1(self):
        r"""安全事件1级分类，-1:未知 0:全部 1:攻击事件 2:侦查事件 3:僵木蠕毒 4:违规策略
        :rtype: int
        """
        return self._EventType1

    @EventType1.setter
    def EventType1(self, EventType1):
        self._EventType1 = EventType1

    @property
    def EventType2(self):
        r"""安全事件2级分类，-1:未知 0:全部 1:DDOS事件 2:Web攻击 3:木马 4:异地登录 5:密码破解
        :rtype: int
        """
        return self._EventType2

    @EventType2.setter
    def EventType2(self, EventType2):
        self._EventType2 = EventType2

    @property
    def Level(self):
        r"""风险等级，-1:未知 0:全部 1:低危 2:中危 3:高危 4:严重，可多选，如：1,2
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Status(self):
        r"""安全事件状态，-1:未知 0:全部 1:待处理 2:已处理 3:误报 4:已忽略 5:已知晓 6:已信任
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Offset(self):
        r"""查询起始地址
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询个数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def OldIdMd5(self):
        r"""私有字段和公有字段映射的原始采集数据唯一标识的MD5值
        :rtype: str
        """
        return self._OldIdMd5

    @OldIdMd5.setter
    def OldIdMd5(self, OldIdMd5):
        self._OldIdMd5 = OldIdMd5


    def _deserialize(self, params):
        self._Asset = params.get("Asset")
        self._EventName = params.get("EventName")
        self._EventType1 = params.get("EventType1")
        self._EventType2 = params.get("EventType2")
        self._Level = params.get("Level")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._EndTime = params.get("EndTime")
        self._OldIdMd5 = params.get("OldIdMd5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaEventPubResponse(AbstractModel):
    r"""SaEventPub返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataSaEventPub: DataSaEventPub
        :type DataSaEventPub: :class:`tencentcloud.ssa.v20180608.models.ObjDataSaEventPub`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataSaEventPub = None
        self._RequestId = None

    @property
    def DataSaEventPub(self):
        r"""DataSaEventPub
        :rtype: :class:`tencentcloud.ssa.v20180608.models.ObjDataSaEventPub`
        """
        return self._DataSaEventPub

    @DataSaEventPub.setter
    def DataSaEventPub(self, DataSaEventPub):
        self._DataSaEventPub = DataSaEventPub

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataSaEventPub") is not None:
            self._DataSaEventPub = ObjDataSaEventPub()
            self._DataSaEventPub._deserialize(params.get("DataSaEventPub"))
        self._RequestId = params.get("RequestId")


class SecurityStatus(AbstractModel):
    r"""安全放回状态

    """


class SocCheckItem(AbstractModel):
    r"""SocCheckItem类型

    """

    def __init__(self):
        r"""
        :param _Name: 名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _LevelId: 唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type LevelId: str
        :param _SuccessCount: 成功数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCount: int
        :param _FailCount: 失败数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailCount: int
        """
        self._Name = None
        self._LevelId = None
        self._SuccessCount = None
        self._FailCount = None

    @property
    def Name(self):
        r"""名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LevelId(self):
        r"""唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LevelId

    @LevelId.setter
    def LevelId(self, LevelId):
        self._LevelId = LevelId

    @property
    def SuccessCount(self):
        r"""成功数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def FailCount(self):
        r"""失败数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FailCount

    @FailCount.setter
    def FailCount(self, FailCount):
        self._FailCount = FailCount


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._LevelId = params.get("LevelId")
        self._SuccessCount = params.get("SuccessCount")
        self._FailCount = params.get("FailCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SocCheckItemV1(AbstractModel):
    r"""检查项相关信息

    """

    def __init__(self):
        r"""
        :param _CheckId: 检查项id
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckId: str
        :param _Name: 配置要求
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Type: 检查项类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _AssetType: 检查对象
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param _Level: 默认风险等级 2:低危 3:中危 4:高危
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param _Standard: 相关规范
注意：此字段可能返回 null，表示取不到有效值。
        :type Standard: str
        :param _IsFree: 检查项是否付费 1:免费 2:付费
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFree: int
        """
        self._CheckId = None
        self._Name = None
        self._Type = None
        self._AssetType = None
        self._Level = None
        self._Standard = None
        self._IsFree = None

    @property
    def CheckId(self):
        r"""检查项id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CheckId

    @CheckId.setter
    def CheckId(self, CheckId):
        self._CheckId = CheckId

    @property
    def Name(self):
        r"""配置要求
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""检查项类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AssetType(self):
        r"""检查对象
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Level(self):
        r"""默认风险等级 2:低危 3:中危 4:高危
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Standard(self):
        r"""相关规范
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Standard

    @Standard.setter
    def Standard(self, Standard):
        self._Standard = Standard

    @property
    def IsFree(self):
        r"""检查项是否付费 1:免费 2:付费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsFree

    @IsFree.setter
    def IsFree(self, IsFree):
        self._IsFree = IsFree


    def _deserialize(self, params):
        self._CheckId = params.get("CheckId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._AssetType = params.get("AssetType")
        self._Level = params.get("Level")
        self._Standard = params.get("Standard")
        self._IsFree = params.get("IsFree")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SocCheckResult(AbstractModel):
    r"""云安全配置检测结果

    """

    def __init__(self):
        r"""
        :param _CheckId: 检查项的uuid
        :type CheckId: str
        :param _Name: 配置要求
        :type Name: str
        :param _Type: 检查项的类型
        :type Type: str
        :param _AssetType: 检查对象
        :type AssetType: str
        :param _PloyName: 策略名
        :type PloyName: str
        :param _PloyId: 策略id
        :type PloyId: int
        :param _Result: 正常,低危,中危,高危
        :type Result: str
        :param _FailAssetNum: 不符合数
        :type FailAssetNum: int
        :param _TotalAssetNum: 总数
        :type TotalAssetNum: int
        :param _DealUrl: 处置建议url链接
        :type DealUrl: str
        """
        self._CheckId = None
        self._Name = None
        self._Type = None
        self._AssetType = None
        self._PloyName = None
        self._PloyId = None
        self._Result = None
        self._FailAssetNum = None
        self._TotalAssetNum = None
        self._DealUrl = None

    @property
    def CheckId(self):
        r"""检查项的uuid
        :rtype: str
        """
        return self._CheckId

    @CheckId.setter
    def CheckId(self, CheckId):
        self._CheckId = CheckId

    @property
    def Name(self):
        r"""配置要求
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""检查项的类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AssetType(self):
        r"""检查对象
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def PloyName(self):
        r"""策略名
        :rtype: str
        """
        return self._PloyName

    @PloyName.setter
    def PloyName(self, PloyName):
        self._PloyName = PloyName

    @property
    def PloyId(self):
        r"""策略id
        :rtype: int
        """
        return self._PloyId

    @PloyId.setter
    def PloyId(self, PloyId):
        self._PloyId = PloyId

    @property
    def Result(self):
        r"""正常,低危,中危,高危
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def FailAssetNum(self):
        r"""不符合数
        :rtype: int
        """
        return self._FailAssetNum

    @FailAssetNum.setter
    def FailAssetNum(self, FailAssetNum):
        self._FailAssetNum = FailAssetNum

    @property
    def TotalAssetNum(self):
        r"""总数
        :rtype: int
        """
        return self._TotalAssetNum

    @TotalAssetNum.setter
    def TotalAssetNum(self, TotalAssetNum):
        self._TotalAssetNum = TotalAssetNum

    @property
    def DealUrl(self):
        r"""处置建议url链接
        :rtype: str
        """
        return self._DealUrl

    @DealUrl.setter
    def DealUrl(self, DealUrl):
        self._DealUrl = DealUrl


    def _deserialize(self, params):
        self._CheckId = params.get("CheckId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._AssetType = params.get("AssetType")
        self._PloyName = params.get("PloyName")
        self._PloyId = params.get("PloyId")
        self._Result = params.get("Result")
        self._FailAssetNum = params.get("FailAssetNum")
        self._TotalAssetNum = params.get("TotalAssetNum")
        self._DealUrl = params.get("DealUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SocComplianceInfoResp(AbstractModel):
    r"""返回结构

    """

    def __init__(self):
        r"""
        :param _Items: 合格项
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of SocComplianceItem
        """
        self._Items = None

    @property
    def Items(self):
        r"""合格项
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SocComplianceItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SocComplianceItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SocComplianceItem(AbstractModel):
    r"""soc合规信息

    """

    def __init__(self):
        r"""
        :param _Item: 唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type Item: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _StandardItem: 分类
注意：此字段可能返回 null，表示取不到有效值。
        :type StandardItem: str
        :param _Result: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: int
        :param _Suggestion: 建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param _ProStr: 产品字符
注意：此字段可能返回 null，表示取不到有效值。
        :type ProStr: str
        :param _Production: 产品数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Production: list of SocProductionItem
        :param _CheckItems: 配置项数组
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckItems: list of SocCheckItem
        """
        self._Item = None
        self._Description = None
        self._StandardItem = None
        self._Result = None
        self._Suggestion = None
        self._ProStr = None
        self._Production = None
        self._CheckItems = None

    @property
    def Item(self):
        r"""唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Item

    @Item.setter
    def Item(self, Item):
        self._Item = Item

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def StandardItem(self):
        r"""分类
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StandardItem

    @StandardItem.setter
    def StandardItem(self, StandardItem):
        self._StandardItem = StandardItem

    @property
    def Result(self):
        r"""结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Suggestion(self):
        r"""建议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def ProStr(self):
        r"""产品字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProStr

    @ProStr.setter
    def ProStr(self, ProStr):
        self._ProStr = ProStr

    @property
    def Production(self):
        r"""产品数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SocProductionItem
        """
        return self._Production

    @Production.setter
    def Production(self, Production):
        self._Production = Production

    @property
    def CheckItems(self):
        r"""配置项数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SocCheckItem
        """
        return self._CheckItems

    @CheckItems.setter
    def CheckItems(self, CheckItems):
        self._CheckItems = CheckItems


    def _deserialize(self, params):
        self._Item = params.get("Item")
        self._Description = params.get("Description")
        self._StandardItem = params.get("StandardItem")
        self._Result = params.get("Result")
        self._Suggestion = params.get("Suggestion")
        self._ProStr = params.get("ProStr")
        if params.get("Production") is not None:
            self._Production = []
            for item in params.get("Production"):
                obj = SocProductionItem()
                obj._deserialize(item)
                self._Production.append(obj)
        if params.get("CheckItems") is not None:
            self._CheckItems = []
            for item in params.get("CheckItems"):
                obj = SocCheckItem()
                obj._deserialize(item)
                self._CheckItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SocProductionItem(AbstractModel):
    r"""soc产品购买信息

    """

    def __init__(self):
        r"""
        :param _Name: 名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Index: 标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: int
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self._Name = None
        self._Index = None
        self._Status = None

    @property
    def Name(self):
        r"""名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Index(self):
        r"""标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Status(self):
        r"""状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Index = params.get("Index")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""标签

    """

    def __init__(self):
        r"""
        :param _Fid: 数据库标识
        :type Fid: int
        :param _Fname: 标签名称字段
        :type Fname: str
        """
        self._Fid = None
        self._Fname = None

    @property
    def Fid(self):
        r"""数据库标识
        :rtype: int
        """
        return self._Fid

    @Fid.setter
    def Fid(self, Fid):
        self._Fid = Fid

    @property
    def Fname(self):
        r"""标签名称字段
        :rtype: str
        """
        return self._Fname

    @Fname.setter
    def Fname(self, Fname):
        self._Fname = Fname


    def _deserialize(self, params):
        self._Fid = params.get("Fid")
        self._Fname = params.get("Fname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulItem(AbstractModel):
    r"""漏洞管理漏洞数据

    """

    def __init__(self):
        r"""
        :param _Id: 标识
        :type Id: str
        :param _VulName: 漏洞名称
        :type VulName: str
        :param _Type: 漏洞类型
        :type Type: int
        :param _Level: 风险等级
        :type Level: int
        :param _Status: 处理状态
        :type Status: int
        :param _Time: 发现时间
        :type Time: str
        :param _ImpactAssetNum: 影响资产数
        :type ImpactAssetNum: int
        :param _ImpactAsset: 影响资产id
        :type ImpactAsset: str
        :param _ImpactAssetName: 影响资产名称
        :type ImpactAssetName: str
        :param _VulDetail: 漏洞描述
        :type VulDetail: str
        :param _VulRefLink: 参考链接
        :type VulRefLink: str
        :param _OldIdMd5: Md5值
        :type OldIdMd5: str
        :param _UniqId: 漏洞唯一标识
        :type UniqId: str
        :param _OperateTime: 忽略时间
        :type OperateTime: str
        :param _IsAssetDeleted: 受影响资产是否下线
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAssetDeleted: str
        :param _DiscoverTime: 漏洞首次发现时间
        :type DiscoverTime: str
        :param _OriginId: 主机源信息标识符
        :type OriginId: int
        :param _Region: 资产区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Vpcid: 资产所属网络
注意：此字段可能返回 null，表示取不到有效值。
        :type Vpcid: str
        :param _AssetType: 资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetType: str
        :param _AssetSubType: 资产子类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetSubType: str
        :param _AssetIpAll: 资产IP
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetIpAll: list of str
        :param _PublicIpAddresses: cvm类型的公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param _PrivateIpAddresses: cvm类型的内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIpAddresses: list of str
        :param _VulSource: 漏洞来源
注意：此字段可能返回 null，表示取不到有效值。
        :type VulSource: str
        :param _AffectedUrl: 影响URL
注意：此字段可能返回 null，表示取不到有效值。
        :type AffectedUrl: str
        :param _SsaAssetCategory: 资产归属
注意：此字段可能返回 null，表示取不到有效值。
        :type SsaAssetCategory: int
        :param _VulUrl: 影响url
注意：此字段可能返回 null，表示取不到有效值。
        :type VulUrl: str
        :param _IsOpen: 是否扫描
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOpen: bool
        :param _YzHostId: 御知主机id
注意：此字段可能返回 null，表示取不到有效值。
        :type YzHostId: int
        :param _VulRepairPlan: 漏洞描述
注意：此字段可能返回 null，表示取不到有效值。
        :type VulRepairPlan: str
        :param _VulPath: 漏洞文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :type VulPath: str
        """
        self._Id = None
        self._VulName = None
        self._Type = None
        self._Level = None
        self._Status = None
        self._Time = None
        self._ImpactAssetNum = None
        self._ImpactAsset = None
        self._ImpactAssetName = None
        self._VulDetail = None
        self._VulRefLink = None
        self._OldIdMd5 = None
        self._UniqId = None
        self._OperateTime = None
        self._IsAssetDeleted = None
        self._DiscoverTime = None
        self._OriginId = None
        self._Region = None
        self._Vpcid = None
        self._AssetType = None
        self._AssetSubType = None
        self._AssetIpAll = None
        self._PublicIpAddresses = None
        self._PrivateIpAddresses = None
        self._VulSource = None
        self._AffectedUrl = None
        self._SsaAssetCategory = None
        self._VulUrl = None
        self._IsOpen = None
        self._YzHostId = None
        self._VulRepairPlan = None
        self._VulPath = None

    @property
    def Id(self):
        r"""标识
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def VulName(self):
        r"""漏洞名称
        :rtype: str
        """
        return self._VulName

    @VulName.setter
    def VulName(self, VulName):
        self._VulName = VulName

    @property
    def Type(self):
        r"""漏洞类型
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Level(self):
        r"""风险等级
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Status(self):
        r"""处理状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Time(self):
        r"""发现时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def ImpactAssetNum(self):
        r"""影响资产数
        :rtype: int
        """
        return self._ImpactAssetNum

    @ImpactAssetNum.setter
    def ImpactAssetNum(self, ImpactAssetNum):
        self._ImpactAssetNum = ImpactAssetNum

    @property
    def ImpactAsset(self):
        r"""影响资产id
        :rtype: str
        """
        return self._ImpactAsset

    @ImpactAsset.setter
    def ImpactAsset(self, ImpactAsset):
        self._ImpactAsset = ImpactAsset

    @property
    def ImpactAssetName(self):
        r"""影响资产名称
        :rtype: str
        """
        return self._ImpactAssetName

    @ImpactAssetName.setter
    def ImpactAssetName(self, ImpactAssetName):
        self._ImpactAssetName = ImpactAssetName

    @property
    def VulDetail(self):
        r"""漏洞描述
        :rtype: str
        """
        return self._VulDetail

    @VulDetail.setter
    def VulDetail(self, VulDetail):
        self._VulDetail = VulDetail

    @property
    def VulRefLink(self):
        r"""参考链接
        :rtype: str
        """
        return self._VulRefLink

    @VulRefLink.setter
    def VulRefLink(self, VulRefLink):
        self._VulRefLink = VulRefLink

    @property
    def OldIdMd5(self):
        r"""Md5值
        :rtype: str
        """
        return self._OldIdMd5

    @OldIdMd5.setter
    def OldIdMd5(self, OldIdMd5):
        self._OldIdMd5 = OldIdMd5

    @property
    def UniqId(self):
        r"""漏洞唯一标识
        :rtype: str
        """
        return self._UniqId

    @UniqId.setter
    def UniqId(self, UniqId):
        self._UniqId = UniqId

    @property
    def OperateTime(self):
        r"""忽略时间
        :rtype: str
        """
        return self._OperateTime

    @OperateTime.setter
    def OperateTime(self, OperateTime):
        self._OperateTime = OperateTime

    @property
    def IsAssetDeleted(self):
        r"""受影响资产是否下线
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsAssetDeleted

    @IsAssetDeleted.setter
    def IsAssetDeleted(self, IsAssetDeleted):
        self._IsAssetDeleted = IsAssetDeleted

    @property
    def DiscoverTime(self):
        r"""漏洞首次发现时间
        :rtype: str
        """
        return self._DiscoverTime

    @DiscoverTime.setter
    def DiscoverTime(self, DiscoverTime):
        self._DiscoverTime = DiscoverTime

    @property
    def OriginId(self):
        r"""主机源信息标识符
        :rtype: int
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def Region(self):
        r"""资产区域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Vpcid(self):
        r"""资产所属网络
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Vpcid

    @Vpcid.setter
    def Vpcid(self, Vpcid):
        self._Vpcid = Vpcid

    @property
    def AssetType(self):
        r"""资产类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def AssetSubType(self):
        r"""资产子类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssetSubType

    @AssetSubType.setter
    def AssetSubType(self, AssetSubType):
        self._AssetSubType = AssetSubType

    @property
    def AssetIpAll(self):
        r"""资产IP
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AssetIpAll

    @AssetIpAll.setter
    def AssetIpAll(self, AssetIpAll):
        self._AssetIpAll = AssetIpAll

    @property
    def PublicIpAddresses(self):
        r"""cvm类型的公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def PrivateIpAddresses(self):
        r"""cvm类型的内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def VulSource(self):
        r"""漏洞来源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VulSource

    @VulSource.setter
    def VulSource(self, VulSource):
        self._VulSource = VulSource

    @property
    def AffectedUrl(self):
        r"""影响URL
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AffectedUrl

    @AffectedUrl.setter
    def AffectedUrl(self, AffectedUrl):
        self._AffectedUrl = AffectedUrl

    @property
    def SsaAssetCategory(self):
        r"""资产归属
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SsaAssetCategory

    @SsaAssetCategory.setter
    def SsaAssetCategory(self, SsaAssetCategory):
        self._SsaAssetCategory = SsaAssetCategory

    @property
    def VulUrl(self):
        r"""影响url
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VulUrl

    @VulUrl.setter
    def VulUrl(self, VulUrl):
        self._VulUrl = VulUrl

    @property
    def IsOpen(self):
        r"""是否扫描
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsOpen

    @IsOpen.setter
    def IsOpen(self, IsOpen):
        self._IsOpen = IsOpen

    @property
    def YzHostId(self):
        r"""御知主机id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._YzHostId

    @YzHostId.setter
    def YzHostId(self, YzHostId):
        self._YzHostId = YzHostId

    @property
    def VulRepairPlan(self):
        r"""漏洞描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VulRepairPlan

    @VulRepairPlan.setter
    def VulRepairPlan(self, VulRepairPlan):
        self._VulRepairPlan = VulRepairPlan

    @property
    def VulPath(self):
        r"""漏洞文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VulPath

    @VulPath.setter
    def VulPath(self, VulPath):
        self._VulPath = VulPath


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._VulName = params.get("VulName")
        self._Type = params.get("Type")
        self._Level = params.get("Level")
        self._Status = params.get("Status")
        self._Time = params.get("Time")
        self._ImpactAssetNum = params.get("ImpactAssetNum")
        self._ImpactAsset = params.get("ImpactAsset")
        self._ImpactAssetName = params.get("ImpactAssetName")
        self._VulDetail = params.get("VulDetail")
        self._VulRefLink = params.get("VulRefLink")
        self._OldIdMd5 = params.get("OldIdMd5")
        self._UniqId = params.get("UniqId")
        self._OperateTime = params.get("OperateTime")
        self._IsAssetDeleted = params.get("IsAssetDeleted")
        self._DiscoverTime = params.get("DiscoverTime")
        self._OriginId = params.get("OriginId")
        self._Region = params.get("Region")
        self._Vpcid = params.get("Vpcid")
        self._AssetType = params.get("AssetType")
        self._AssetSubType = params.get("AssetSubType")
        self._AssetIpAll = params.get("AssetIpAll")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._VulSource = params.get("VulSource")
        self._AffectedUrl = params.get("AffectedUrl")
        self._SsaAssetCategory = params.get("SsaAssetCategory")
        self._VulUrl = params.get("VulUrl")
        self._IsOpen = params.get("IsOpen")
        self._YzHostId = params.get("YzHostId")
        self._VulRepairPlan = params.get("VulRepairPlan")
        self._VulPath = params.get("VulPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulList(AbstractModel):
    r"""漏洞管理漏洞列表

    """

    def __init__(self):
        r"""
        :param _List: 列表
        :type List: list of VulItem
        :param _Total: 总数
        :type Total: int
        """
        self._List = None
        self._Total = None

    @property
    def List(self):
        r"""列表
        :rtype: list of VulItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = VulItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        