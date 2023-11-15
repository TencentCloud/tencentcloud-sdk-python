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


class ActivityDetail(AbstractModel):
    """活动详情

    """

    def __init__(self):
        r"""
        :param _ActivityId: 活动id
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityId: int
        :param _ActivityName: 活动名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityName: str
        :param _ActivityState: 活动状态，10:未开始状态、20:已开始（进行中）状态、30:已结束状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityState: int
        :param _ActivityType: 活动类型，100:留资活动
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityType: int
        :param _StartTime: 活动开始时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param _EndTime: 活动结束时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param _MainPhoto: 活动主图
注意：此字段可能返回 null，表示取不到有效值。
        :type MainPhoto: str
        :param _PrivacyAgreementId: 协议编号
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivacyAgreementId: str
        :param _UpdateTime: 活动更新时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param _ActivityDataList: 活动数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityDataList: str
        """
        self._ActivityId = None
        self._ActivityName = None
        self._ActivityState = None
        self._ActivityType = None
        self._StartTime = None
        self._EndTime = None
        self._MainPhoto = None
        self._PrivacyAgreementId = None
        self._UpdateTime = None
        self._ActivityDataList = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def ActivityName(self):
        return self._ActivityName

    @ActivityName.setter
    def ActivityName(self, ActivityName):
        self._ActivityName = ActivityName

    @property
    def ActivityState(self):
        return self._ActivityState

    @ActivityState.setter
    def ActivityState(self, ActivityState):
        self._ActivityState = ActivityState

    @property
    def ActivityType(self):
        return self._ActivityType

    @ActivityType.setter
    def ActivityType(self, ActivityType):
        self._ActivityType = ActivityType

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
    def MainPhoto(self):
        return self._MainPhoto

    @MainPhoto.setter
    def MainPhoto(self, MainPhoto):
        self._MainPhoto = MainPhoto

    @property
    def PrivacyAgreementId(self):
        return self._PrivacyAgreementId

    @PrivacyAgreementId.setter
    def PrivacyAgreementId(self, PrivacyAgreementId):
        self._PrivacyAgreementId = PrivacyAgreementId

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ActivityDataList(self):
        return self._ActivityDataList

    @ActivityDataList.setter
    def ActivityDataList(self, ActivityDataList):
        self._ActivityDataList = ActivityDataList


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._ActivityName = params.get("ActivityName")
        self._ActivityState = params.get("ActivityState")
        self._ActivityType = params.get("ActivityType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MainPhoto = params.get("MainPhoto")
        self._PrivacyAgreementId = params.get("PrivacyAgreementId")
        self._UpdateTime = params.get("UpdateTime")
        self._ActivityDataList = params.get("ActivityDataList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivityJoinDetail(AbstractModel):
    """活动参与详情

    """

    def __init__(self):
        r"""
        :param _ActivityId: 活动id
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityId: int
        :param _ActivityName: 活动名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityName: str
        :param _SalesName: 销售姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type SalesName: str
        :param _SalesPhone: 销售电话
注意：此字段可能返回 null，表示取不到有效值。
        :type SalesPhone: str
        :param _JoinId: 参与id
注意：此字段可能返回 null，表示取不到有效值。
        :type JoinId: int
        :param _LiveCodeId: 活码id
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveCodeId: int
        :param _UserPhone: 用户电话
注意：此字段可能返回 null，表示取不到有效值。
        :type UserPhone: str
        :param _UserName: 用户姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _ActivityData: 活动数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityData: str
        :param _LeadId: 线索id
注意：此字段可能返回 null，表示取不到有效值。
        :type LeadId: int
        :param _JoinTime: 参与时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type JoinTime: int
        :param _Duplicate: 线索是否是重复创建， 0 ：新建、 1：合并、 2：重复， 默认为0
注意：此字段可能返回 null，表示取不到有效值。
        :type Duplicate: int
        :param _DuplicateLeadId: 重复线索id
注意：此字段可能返回 null，表示取不到有效值。
        :type DuplicateLeadId: int
        :param _JoinState: 是否为参与多次活动， 1：参与一次、2、参与多次，默认为0
注意：此字段可能返回 null，表示取不到有效值。
        :type JoinState: int
        :param _CreateTime: 创建时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _UpdateTime: 更新时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        """
        self._ActivityId = None
        self._ActivityName = None
        self._SalesName = None
        self._SalesPhone = None
        self._JoinId = None
        self._LiveCodeId = None
        self._UserPhone = None
        self._UserName = None
        self._ActivityData = None
        self._LeadId = None
        self._JoinTime = None
        self._Duplicate = None
        self._DuplicateLeadId = None
        self._JoinState = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def ActivityName(self):
        return self._ActivityName

    @ActivityName.setter
    def ActivityName(self, ActivityName):
        self._ActivityName = ActivityName

    @property
    def SalesName(self):
        return self._SalesName

    @SalesName.setter
    def SalesName(self, SalesName):
        self._SalesName = SalesName

    @property
    def SalesPhone(self):
        return self._SalesPhone

    @SalesPhone.setter
    def SalesPhone(self, SalesPhone):
        self._SalesPhone = SalesPhone

    @property
    def JoinId(self):
        return self._JoinId

    @JoinId.setter
    def JoinId(self, JoinId):
        self._JoinId = JoinId

    @property
    def LiveCodeId(self):
        return self._LiveCodeId

    @LiveCodeId.setter
    def LiveCodeId(self, LiveCodeId):
        self._LiveCodeId = LiveCodeId

    @property
    def UserPhone(self):
        return self._UserPhone

    @UserPhone.setter
    def UserPhone(self, UserPhone):
        self._UserPhone = UserPhone

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def ActivityData(self):
        return self._ActivityData

    @ActivityData.setter
    def ActivityData(self, ActivityData):
        self._ActivityData = ActivityData

    @property
    def LeadId(self):
        return self._LeadId

    @LeadId.setter
    def LeadId(self, LeadId):
        self._LeadId = LeadId

    @property
    def JoinTime(self):
        return self._JoinTime

    @JoinTime.setter
    def JoinTime(self, JoinTime):
        self._JoinTime = JoinTime

    @property
    def Duplicate(self):
        return self._Duplicate

    @Duplicate.setter
    def Duplicate(self, Duplicate):
        self._Duplicate = Duplicate

    @property
    def DuplicateLeadId(self):
        return self._DuplicateLeadId

    @DuplicateLeadId.setter
    def DuplicateLeadId(self, DuplicateLeadId):
        self._DuplicateLeadId = DuplicateLeadId

    @property
    def JoinState(self):
        return self._JoinState

    @JoinState.setter
    def JoinState(self, JoinState):
        self._JoinState = JoinState

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._ActivityName = params.get("ActivityName")
        self._SalesName = params.get("SalesName")
        self._SalesPhone = params.get("SalesPhone")
        self._JoinId = params.get("JoinId")
        self._LiveCodeId = params.get("LiveCodeId")
        self._UserPhone = params.get("UserPhone")
        self._UserName = params.get("UserName")
        self._ActivityData = params.get("ActivityData")
        self._LeadId = params.get("LeadId")
        self._JoinTime = params.get("JoinTime")
        self._Duplicate = params.get("Duplicate")
        self._DuplicateLeadId = params.get("DuplicateLeadId")
        self._JoinState = params.get("JoinState")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArrivalInfo(AbstractModel):
    """发生过到店的潜客到店信息

    """

    def __init__(self):
        r"""
        :param _ClueId: 线索id
        :type ClueId: int
        :param _CustomerId: 客户id
        :type CustomerId: int
        :param _UserName: 客户姓名
        :type UserName: str
        :param _Phone: 客户的手机号
        :type Phone: str
        :param _FirstArrival: 是否首次到店，0否，1是
        :type FirstArrival: int
        :param _ArrivalTime: 到店时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ArrivalTime: int
        :param _EventType: 发生事件
        :type EventType: int
        :param _EventTypeName: 发生事件名称
        :type EventTypeName: str
        :param _FollowRecord: 跟进记录
        :type FollowRecord: str
        """
        self._ClueId = None
        self._CustomerId = None
        self._UserName = None
        self._Phone = None
        self._FirstArrival = None
        self._ArrivalTime = None
        self._EventType = None
        self._EventTypeName = None
        self._FollowRecord = None

    @property
    def ClueId(self):
        return self._ClueId

    @ClueId.setter
    def ClueId(self, ClueId):
        self._ClueId = ClueId

    @property
    def CustomerId(self):
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def FirstArrival(self):
        return self._FirstArrival

    @FirstArrival.setter
    def FirstArrival(self, FirstArrival):
        self._FirstArrival = FirstArrival

    @property
    def ArrivalTime(self):
        return self._ArrivalTime

    @ArrivalTime.setter
    def ArrivalTime(self, ArrivalTime):
        self._ArrivalTime = ArrivalTime

    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def EventTypeName(self):
        return self._EventTypeName

    @EventTypeName.setter
    def EventTypeName(self, EventTypeName):
        self._EventTypeName = EventTypeName

    @property
    def FollowRecord(self):
        return self._FollowRecord

    @FollowRecord.setter
    def FollowRecord(self, FollowRecord):
        self._FollowRecord = FollowRecord


    def _deserialize(self, params):
        self._ClueId = params.get("ClueId")
        self._CustomerId = params.get("CustomerId")
        self._UserName = params.get("UserName")
        self._Phone = params.get("Phone")
        self._FirstArrival = params.get("FirstArrival")
        self._ArrivalTime = params.get("ArrivalTime")
        self._EventType = params.get("EventType")
        self._EventTypeName = params.get("EventTypeName")
        self._FollowRecord = params.get("FollowRecord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCodeInnerDetail(AbstractModel):
    """渠道活码详情

    """

    def __init__(self):
        r"""
        :param _Id: 渠道活码id
        :type Id: int
        :param _Type: 欢迎语类型，0：普通欢迎语、1:渠道欢迎语
        :type Type: int
        :param _Source: 渠道来源
        :type Source: str
        :param _SourceName: 渠道来源名称
        :type SourceName: str
        :param _Name: 二维码名称
        :type Name: str
        :param _UseUserIdList: 使用成员用户id集
        :type UseUserIdList: list of int
        :param _UseUserOpenIdList: 使用成员企微账号id集
        :type UseUserOpenIdList: list of str
        :param _TagList: 标签
        :type TagList: list of WeComTagDetail
        :param _SkipVerify: 自动通过好友，0：开启、1：关闭，默认0开启
        :type SkipVerify: int
        :param _Friends: 添加好友人数
        :type Friends: int
        :param _Remark: 备注
        :type Remark: str
        :param _MsgId: 欢迎语id（通过欢迎语新增返回的id）
        :type MsgId: int
        :param _ConfigId: 联系我config_id
        :type ConfigId: str
        :param _QrCodeUrl: 联系我二维码地址
        :type QrCodeUrl: str
        :param _RecStatus: 记录状态， 0：有效、1：无效
        :type RecStatus: int
        :param _AppId: 应用ID
        :type AppId: str
        """
        self._Id = None
        self._Type = None
        self._Source = None
        self._SourceName = None
        self._Name = None
        self._UseUserIdList = None
        self._UseUserOpenIdList = None
        self._TagList = None
        self._SkipVerify = None
        self._Friends = None
        self._Remark = None
        self._MsgId = None
        self._ConfigId = None
        self._QrCodeUrl = None
        self._RecStatus = None
        self._AppId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceName(self):
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def UseUserIdList(self):
        return self._UseUserIdList

    @UseUserIdList.setter
    def UseUserIdList(self, UseUserIdList):
        self._UseUserIdList = UseUserIdList

    @property
    def UseUserOpenIdList(self):
        return self._UseUserOpenIdList

    @UseUserOpenIdList.setter
    def UseUserOpenIdList(self, UseUserOpenIdList):
        self._UseUserOpenIdList = UseUserOpenIdList

    @property
    def TagList(self):
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def SkipVerify(self):
        return self._SkipVerify

    @SkipVerify.setter
    def SkipVerify(self, SkipVerify):
        self._SkipVerify = SkipVerify

    @property
    def Friends(self):
        return self._Friends

    @Friends.setter
    def Friends(self, Friends):
        self._Friends = Friends

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MsgId(self):
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def ConfigId(self):
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def QrCodeUrl(self):
        return self._QrCodeUrl

    @QrCodeUrl.setter
    def QrCodeUrl(self, QrCodeUrl):
        self._QrCodeUrl = QrCodeUrl

    @property
    def RecStatus(self):
        return self._RecStatus

    @RecStatus.setter
    def RecStatus(self, RecStatus):
        self._RecStatus = RecStatus

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Source = params.get("Source")
        self._SourceName = params.get("SourceName")
        self._Name = params.get("Name")
        self._UseUserIdList = params.get("UseUserIdList")
        self._UseUserOpenIdList = params.get("UseUserOpenIdList")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = WeComTagDetail()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._SkipVerify = params.get("SkipVerify")
        self._Friends = params.get("Friends")
        self._Remark = params.get("Remark")
        self._MsgId = params.get("MsgId")
        self._ConfigId = params.get("ConfigId")
        self._QrCodeUrl = params.get("QrCodeUrl")
        self._RecStatus = params.get("RecStatus")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelTag(AbstractModel):
    """客户渠道标签

    """

    def __init__(self):
        r"""
        :param _TagName: 该客户档案当前已成功关联的渠道标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TagName: str
        :param _TagId: 该客户档案当前已成功关联的渠道标签的id
注意：此字段可能返回 null，表示取不到有效值。
        :type TagId: str
        """
        self._TagName = None
        self._TagId = None

    @property
    def TagName(self):
        return self._TagName

    @TagName.setter
    def TagName(self, TagName):
        self._TagName = TagName

    @property
    def TagId(self):
        return self._TagId

    @TagId.setter
    def TagId(self, TagId):
        self._TagId = TagId


    def _deserialize(self, params):
        self._TagName = params.get("TagName")
        self._TagId = params.get("TagId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatArchivingDetail(AbstractModel):
    """会话存档数据详情

    """

    def __init__(self):
        r"""
        :param _MsgId: 消息id
        :type MsgId: str
        :param _Action: 动作名称，switch表示切换企微账号，send表示企微普通消息
        :type Action: str
        :param _MsgType: 消息类型，当Action != "switch"时存在，例如video, text, voice 等，和企微开放文档一一对应
https://open.work.weixin.qq.com/api/doc/90000/90135/91774
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgType: str
        :param _From: 消息发送人
注意：此字段可能返回 null，表示取不到有效值。
        :type From: str
        :param _ToList: 消息接收人列表，注意接收人可能只有一个
注意：此字段可能返回 null，表示取不到有效值。
        :type ToList: list of str
        :param _RoomId: 如果是群消息，则不为空
注意：此字段可能返回 null，表示取不到有效值。
        :type RoomId: str
        :param _MsgTime: 消息发送的时间戳，单位为秒
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgTime: int
        :param _Video: MsgType=video时的消息体，忽略此字段，见BodyJson字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Video: :class:`tencentcloud.wav.v20210129.models.ChatArchivingMsgTypeVideo`
        :param _BodyJson: 根据MsgType的不同取值，解析内容不同，参考：https://open.work.weixin.qq.com/api/doc/90000/90135/91774
注意：此字段可能返回 null，表示取不到有效值。
        :type BodyJson: str
        """
        self._MsgId = None
        self._Action = None
        self._MsgType = None
        self._From = None
        self._ToList = None
        self._RoomId = None
        self._MsgTime = None
        self._Video = None
        self._BodyJson = None

    @property
    def MsgId(self):
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def MsgType(self):
        return self._MsgType

    @MsgType.setter
    def MsgType(self, MsgType):
        self._MsgType = MsgType

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def ToList(self):
        return self._ToList

    @ToList.setter
    def ToList(self, ToList):
        self._ToList = ToList

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def MsgTime(self):
        return self._MsgTime

    @MsgTime.setter
    def MsgTime(self, MsgTime):
        self._MsgTime = MsgTime

    @property
    def Video(self):
        return self._Video

    @Video.setter
    def Video(self, Video):
        self._Video = Video

    @property
    def BodyJson(self):
        return self._BodyJson

    @BodyJson.setter
    def BodyJson(self, BodyJson):
        self._BodyJson = BodyJson


    def _deserialize(self, params):
        self._MsgId = params.get("MsgId")
        self._Action = params.get("Action")
        self._MsgType = params.get("MsgType")
        self._From = params.get("From")
        self._ToList = params.get("ToList")
        self._RoomId = params.get("RoomId")
        self._MsgTime = params.get("MsgTime")
        if params.get("Video") is not None:
            self._Video = ChatArchivingMsgTypeVideo()
            self._Video._deserialize(params.get("Video"))
        self._BodyJson = params.get("BodyJson")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatArchivingMsgTypeVideo(AbstractModel):
    """会话存档的视频消息类型

    """

    def __init__(self):
        r"""
        :param _PlayLength: 视频时长，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type PlayLength: int
        :param _FileSize: 文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param _CosKey: 视频资源对象Cos下载地址
        :type CosKey: str
        """
        self._PlayLength = None
        self._FileSize = None
        self._CosKey = None

    @property
    def PlayLength(self):
        return self._PlayLength

    @PlayLength.setter
    def PlayLength(self, PlayLength):
        self._PlayLength = PlayLength

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def CosKey(self):
        return self._CosKey

    @CosKey.setter
    def CosKey(self, CosKey):
        self._CosKey = CosKey


    def _deserialize(self, params):
        self._PlayLength = params.get("PlayLength")
        self._FileSize = params.get("FileSize")
        self._CosKey = params.get("CosKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClueInfoDetail(AbstractModel):
    """线索信息详情

    """

    def __init__(self):
        r"""
        :param _ClueId: 线索id，线索唯一识别编码
        :type ClueId: str
        :param _DealerId: 接待客户经销商顾问所属经销商code
        :type DealerId: str
        :param _EnquireTime: 线索获取时间，用户添加企业微信时间，单位是秒
        :type EnquireTime: int
        :param _UnionId: 客户在微信生态中唯一识别码
        :type UnionId: str
        :param _Name: 微信昵称
        :type Name: str
        :param _Phone: 联系方式
        :type Phone: str
        :param _SeriesCode: 车系编号
        :type SeriesCode: str
        :param _ModelCode: 车型编号
        :type ModelCode: str
        :param _ProvinceCode: 省份编号
        :type ProvinceCode: str
        :param _CityCode: 城市编号
        :type CityCode: str
        :param _SalesName: 顾问名称
        :type SalesName: str
        :param _SalesPhone: 顾问电话
        :type SalesPhone: str
        :param _Remark: 备注
        :type Remark: str
        :param _TagList: 标签
        :type TagList: list of str
        :param _UserName: 客户姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _LeadUserType: 线索属性，0：个人，1：企业
        :type LeadUserType: int
        :param _LeadType: 线索来源类型，1：线上，2：线下
        :type LeadType: int
        :param _ChannelId: 线索渠道对应ID
        :type ChannelId: int
        :param _ChannelName: 线索渠道类型，与线索来源对应的渠道名称
        :type ChannelName: str
        :param _SourceChannelName: 线索渠道名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceChannelName: str
        :param _Gender: 0：未知，1：男，2：女
        :type Gender: int
        :param _CreateTime: 线索创建时间戳，单位：秒
        :type CreateTime: str
        :param _UpdateTime: 线索创建时间戳，单位：秒
        :type UpdateTime: str
        :param _LeadStatus: 线索所处状态，101-待分配 201-待建档 301-已建档 401-已邀约 501-跟进中 601-已下订单 701-已成交 801-战败申请中 901-已战败 1001-未知状态 1101-转移申请中 1201-已完成
        :type LeadStatus: int
        :param _LevelCode: 线索意向等级
        :type LevelCode: str
        :param _ImportAtTime: 线索成功导入的时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type ImportAtTime: int
        :param _DistributeTime: 完成线索分配的时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type DistributeTime: int
        :param _CreateAtTime: 获取线索的时间戳，单位：秒
        :type CreateAtTime: int
        :param _WxId: 客户微信id
        :type WxId: str
        :param _BrandCode: 意向车型对应品牌code
        :type BrandCode: str
        :param _BuildTime: 建档时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BuildTime: int
        :param _OrderTime: 下订时间，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderTime: int
        :param _ArrivalTime: 到店时间，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type ArrivalTime: int
        :param _DeliveryTime: 交车时间，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type DeliveryTime: int
        :param _FollowTime: 上次跟进时间，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowTime: int
        :param _NextFollowTime: 下次跟进时间，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type NextFollowTime: int
        :param _OrgId: 线索所属组织id
        :type OrgId: int
        :param _OrgName: 线索所属组织名称
        :type OrgName: str
        :param _Introducer: 介绍人姓名
        :type Introducer: str
        :param _IntroducerPhone: 介绍人电话
        :type IntroducerPhone: str
        :param _IsBindWx: 是否关联微信 1 是 0 否
        :type IsBindWx: int
        :param _IsMerge: 是否经过合并 1 是 0 否
        :type IsMerge: int
        :param _IsInvalid: 是否无效  1 是 0 否
        :type IsInvalid: int
        :param _InvalidType: 无效类型
        :type InvalidType: str
        :param _InvalidTypeName: 无效类型枚举：
无意向购买、空错号、未接听、其他
        :type InvalidTypeName: str
        :param _InvalidRemark: 由顾问手动输入的无效原因文字
        :type InvalidRemark: str
        :param _InvalidTime: 无效时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InvalidTime: int
        :param _DealerName: 经销商名称
        :type DealerName: str
        :param _ShopId: 经销商下级门店ID
        :type ShopId: int
        :param _ShopName: 经销商下级门店名称
        :type ShopName: str
        :param _Position: 职位
        :type Position: str
        :param _CorpShopId: 自定义的门店id
        :type CorpShopId: str
        """
        self._ClueId = None
        self._DealerId = None
        self._EnquireTime = None
        self._UnionId = None
        self._Name = None
        self._Phone = None
        self._SeriesCode = None
        self._ModelCode = None
        self._ProvinceCode = None
        self._CityCode = None
        self._SalesName = None
        self._SalesPhone = None
        self._Remark = None
        self._TagList = None
        self._UserName = None
        self._LeadUserType = None
        self._LeadType = None
        self._ChannelId = None
        self._ChannelName = None
        self._SourceChannelName = None
        self._Gender = None
        self._CreateTime = None
        self._UpdateTime = None
        self._LeadStatus = None
        self._LevelCode = None
        self._ImportAtTime = None
        self._DistributeTime = None
        self._CreateAtTime = None
        self._WxId = None
        self._BrandCode = None
        self._BuildTime = None
        self._OrderTime = None
        self._ArrivalTime = None
        self._DeliveryTime = None
        self._FollowTime = None
        self._NextFollowTime = None
        self._OrgId = None
        self._OrgName = None
        self._Introducer = None
        self._IntroducerPhone = None
        self._IsBindWx = None
        self._IsMerge = None
        self._IsInvalid = None
        self._InvalidType = None
        self._InvalidTypeName = None
        self._InvalidRemark = None
        self._InvalidTime = None
        self._DealerName = None
        self._ShopId = None
        self._ShopName = None
        self._Position = None
        self._CorpShopId = None

    @property
    def ClueId(self):
        return self._ClueId

    @ClueId.setter
    def ClueId(self, ClueId):
        self._ClueId = ClueId

    @property
    def DealerId(self):
        return self._DealerId

    @DealerId.setter
    def DealerId(self, DealerId):
        self._DealerId = DealerId

    @property
    def EnquireTime(self):
        return self._EnquireTime

    @EnquireTime.setter
    def EnquireTime(self, EnquireTime):
        self._EnquireTime = EnquireTime

    @property
    def UnionId(self):
        return self._UnionId

    @UnionId.setter
    def UnionId(self, UnionId):
        self._UnionId = UnionId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def SeriesCode(self):
        return self._SeriesCode

    @SeriesCode.setter
    def SeriesCode(self, SeriesCode):
        self._SeriesCode = SeriesCode

    @property
    def ModelCode(self):
        return self._ModelCode

    @ModelCode.setter
    def ModelCode(self, ModelCode):
        self._ModelCode = ModelCode

    @property
    def ProvinceCode(self):
        return self._ProvinceCode

    @ProvinceCode.setter
    def ProvinceCode(self, ProvinceCode):
        self._ProvinceCode = ProvinceCode

    @property
    def CityCode(self):
        return self._CityCode

    @CityCode.setter
    def CityCode(self, CityCode):
        self._CityCode = CityCode

    @property
    def SalesName(self):
        return self._SalesName

    @SalesName.setter
    def SalesName(self, SalesName):
        self._SalesName = SalesName

    @property
    def SalesPhone(self):
        return self._SalesPhone

    @SalesPhone.setter
    def SalesPhone(self, SalesPhone):
        self._SalesPhone = SalesPhone

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TagList(self):
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def LeadUserType(self):
        return self._LeadUserType

    @LeadUserType.setter
    def LeadUserType(self, LeadUserType):
        self._LeadUserType = LeadUserType

    @property
    def LeadType(self):
        return self._LeadType

    @LeadType.setter
    def LeadType(self, LeadType):
        self._LeadType = LeadType

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
    def SourceChannelName(self):
        return self._SourceChannelName

    @SourceChannelName.setter
    def SourceChannelName(self, SourceChannelName):
        self._SourceChannelName = SourceChannelName

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def LeadStatus(self):
        return self._LeadStatus

    @LeadStatus.setter
    def LeadStatus(self, LeadStatus):
        self._LeadStatus = LeadStatus

    @property
    def LevelCode(self):
        return self._LevelCode

    @LevelCode.setter
    def LevelCode(self, LevelCode):
        self._LevelCode = LevelCode

    @property
    def ImportAtTime(self):
        return self._ImportAtTime

    @ImportAtTime.setter
    def ImportAtTime(self, ImportAtTime):
        self._ImportAtTime = ImportAtTime

    @property
    def DistributeTime(self):
        return self._DistributeTime

    @DistributeTime.setter
    def DistributeTime(self, DistributeTime):
        self._DistributeTime = DistributeTime

    @property
    def CreateAtTime(self):
        return self._CreateAtTime

    @CreateAtTime.setter
    def CreateAtTime(self, CreateAtTime):
        self._CreateAtTime = CreateAtTime

    @property
    def WxId(self):
        return self._WxId

    @WxId.setter
    def WxId(self, WxId):
        self._WxId = WxId

    @property
    def BrandCode(self):
        return self._BrandCode

    @BrandCode.setter
    def BrandCode(self, BrandCode):
        self._BrandCode = BrandCode

    @property
    def BuildTime(self):
        return self._BuildTime

    @BuildTime.setter
    def BuildTime(self, BuildTime):
        self._BuildTime = BuildTime

    @property
    def OrderTime(self):
        return self._OrderTime

    @OrderTime.setter
    def OrderTime(self, OrderTime):
        self._OrderTime = OrderTime

    @property
    def ArrivalTime(self):
        return self._ArrivalTime

    @ArrivalTime.setter
    def ArrivalTime(self, ArrivalTime):
        self._ArrivalTime = ArrivalTime

    @property
    def DeliveryTime(self):
        return self._DeliveryTime

    @DeliveryTime.setter
    def DeliveryTime(self, DeliveryTime):
        self._DeliveryTime = DeliveryTime

    @property
    def FollowTime(self):
        return self._FollowTime

    @FollowTime.setter
    def FollowTime(self, FollowTime):
        self._FollowTime = FollowTime

    @property
    def NextFollowTime(self):
        return self._NextFollowTime

    @NextFollowTime.setter
    def NextFollowTime(self, NextFollowTime):
        self._NextFollowTime = NextFollowTime

    @property
    def OrgId(self):
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def OrgName(self):
        return self._OrgName

    @OrgName.setter
    def OrgName(self, OrgName):
        self._OrgName = OrgName

    @property
    def Introducer(self):
        return self._Introducer

    @Introducer.setter
    def Introducer(self, Introducer):
        self._Introducer = Introducer

    @property
    def IntroducerPhone(self):
        return self._IntroducerPhone

    @IntroducerPhone.setter
    def IntroducerPhone(self, IntroducerPhone):
        self._IntroducerPhone = IntroducerPhone

    @property
    def IsBindWx(self):
        return self._IsBindWx

    @IsBindWx.setter
    def IsBindWx(self, IsBindWx):
        self._IsBindWx = IsBindWx

    @property
    def IsMerge(self):
        return self._IsMerge

    @IsMerge.setter
    def IsMerge(self, IsMerge):
        self._IsMerge = IsMerge

    @property
    def IsInvalid(self):
        return self._IsInvalid

    @IsInvalid.setter
    def IsInvalid(self, IsInvalid):
        self._IsInvalid = IsInvalid

    @property
    def InvalidType(self):
        return self._InvalidType

    @InvalidType.setter
    def InvalidType(self, InvalidType):
        self._InvalidType = InvalidType

    @property
    def InvalidTypeName(self):
        return self._InvalidTypeName

    @InvalidTypeName.setter
    def InvalidTypeName(self, InvalidTypeName):
        self._InvalidTypeName = InvalidTypeName

    @property
    def InvalidRemark(self):
        return self._InvalidRemark

    @InvalidRemark.setter
    def InvalidRemark(self, InvalidRemark):
        self._InvalidRemark = InvalidRemark

    @property
    def InvalidTime(self):
        return self._InvalidTime

    @InvalidTime.setter
    def InvalidTime(self, InvalidTime):
        self._InvalidTime = InvalidTime

    @property
    def DealerName(self):
        return self._DealerName

    @DealerName.setter
    def DealerName(self, DealerName):
        self._DealerName = DealerName

    @property
    def ShopId(self):
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def ShopName(self):
        return self._ShopName

    @ShopName.setter
    def ShopName(self, ShopName):
        self._ShopName = ShopName

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def CorpShopId(self):
        return self._CorpShopId

    @CorpShopId.setter
    def CorpShopId(self, CorpShopId):
        self._CorpShopId = CorpShopId


    def _deserialize(self, params):
        self._ClueId = params.get("ClueId")
        self._DealerId = params.get("DealerId")
        self._EnquireTime = params.get("EnquireTime")
        self._UnionId = params.get("UnionId")
        self._Name = params.get("Name")
        self._Phone = params.get("Phone")
        self._SeriesCode = params.get("SeriesCode")
        self._ModelCode = params.get("ModelCode")
        self._ProvinceCode = params.get("ProvinceCode")
        self._CityCode = params.get("CityCode")
        self._SalesName = params.get("SalesName")
        self._SalesPhone = params.get("SalesPhone")
        self._Remark = params.get("Remark")
        self._TagList = params.get("TagList")
        self._UserName = params.get("UserName")
        self._LeadUserType = params.get("LeadUserType")
        self._LeadType = params.get("LeadType")
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        self._SourceChannelName = params.get("SourceChannelName")
        self._Gender = params.get("Gender")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._LeadStatus = params.get("LeadStatus")
        self._LevelCode = params.get("LevelCode")
        self._ImportAtTime = params.get("ImportAtTime")
        self._DistributeTime = params.get("DistributeTime")
        self._CreateAtTime = params.get("CreateAtTime")
        self._WxId = params.get("WxId")
        self._BrandCode = params.get("BrandCode")
        self._BuildTime = params.get("BuildTime")
        self._OrderTime = params.get("OrderTime")
        self._ArrivalTime = params.get("ArrivalTime")
        self._DeliveryTime = params.get("DeliveryTime")
        self._FollowTime = params.get("FollowTime")
        self._NextFollowTime = params.get("NextFollowTime")
        self._OrgId = params.get("OrgId")
        self._OrgName = params.get("OrgName")
        self._Introducer = params.get("Introducer")
        self._IntroducerPhone = params.get("IntroducerPhone")
        self._IsBindWx = params.get("IsBindWx")
        self._IsMerge = params.get("IsMerge")
        self._IsInvalid = params.get("IsInvalid")
        self._InvalidType = params.get("InvalidType")
        self._InvalidTypeName = params.get("InvalidTypeName")
        self._InvalidRemark = params.get("InvalidRemark")
        self._InvalidTime = params.get("InvalidTime")
        self._DealerName = params.get("DealerName")
        self._ShopId = params.get("ShopId")
        self._ShopName = params.get("ShopName")
        self._Position = params.get("Position")
        self._CorpShopId = params.get("CorpShopId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CorpUserInfo(AbstractModel):
    """企业成员信息

    """

    def __init__(self):
        r"""
        :param _UserId: 企业成员UserId
        :type UserId: int
        :param _UserName: 企业成员在SaaS名片内填写的姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _UserOpenId: 企业成员在企微原生通讯录内的id
注意：此字段可能返回 null，表示取不到有效值。
        :type UserOpenId: str
        :param _DealerId: 成员所属经销商id，可为空
注意：此字段可能返回 null，表示取不到有效值。
        :type DealerId: int
        :param _ShopId: 成员所属门店id，可为空
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopId: int
        :param _Phone: 企业成员手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param _OrgIds: 成员所属部门id列表，仅返回该应用有查看权限的部门id；成员授权模式下，固定返回根部门id，即固定为1；多个部门使用逗号分割
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgIds: str
        :param _MainDepartment: 主部门，仅当应用对主部门有查看权限时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type MainDepartment: str
        :param _IsLeaderInDept: 是否为部门负责人，第三方应用可为空。与orgIds值一一对应，多个部门使用逗号隔开，0-否， 1-是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLeaderInDept: str
        :param _Status: 激活状态: 0=已激活，1=已禁用，-1=退出企业"
        :type Status: int
        :param _JobNumber: 工号
注意：此字段可能返回 null，表示取不到有效值。
        :type JobNumber: str
        """
        self._UserId = None
        self._UserName = None
        self._UserOpenId = None
        self._DealerId = None
        self._ShopId = None
        self._Phone = None
        self._OrgIds = None
        self._MainDepartment = None
        self._IsLeaderInDept = None
        self._Status = None
        self._JobNumber = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def UserOpenId(self):
        return self._UserOpenId

    @UserOpenId.setter
    def UserOpenId(self, UserOpenId):
        self._UserOpenId = UserOpenId

    @property
    def DealerId(self):
        return self._DealerId

    @DealerId.setter
    def DealerId(self, DealerId):
        self._DealerId = DealerId

    @property
    def ShopId(self):
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def OrgIds(self):
        return self._OrgIds

    @OrgIds.setter
    def OrgIds(self, OrgIds):
        self._OrgIds = OrgIds

    @property
    def MainDepartment(self):
        return self._MainDepartment

    @MainDepartment.setter
    def MainDepartment(self, MainDepartment):
        self._MainDepartment = MainDepartment

    @property
    def IsLeaderInDept(self):
        return self._IsLeaderInDept

    @IsLeaderInDept.setter
    def IsLeaderInDept(self, IsLeaderInDept):
        self._IsLeaderInDept = IsLeaderInDept

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def JobNumber(self):
        return self._JobNumber

    @JobNumber.setter
    def JobNumber(self, JobNumber):
        self._JobNumber = JobNumber


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._UserOpenId = params.get("UserOpenId")
        self._DealerId = params.get("DealerId")
        self._ShopId = params.get("ShopId")
        self._Phone = params.get("Phone")
        self._OrgIds = params.get("OrgIds")
        self._MainDepartment = params.get("MainDepartment")
        self._IsLeaderInDept = params.get("IsLeaderInDept")
        self._Status = params.get("Status")
        self._JobNumber = params.get("JobNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateChannelCodeRequest(AbstractModel):
    """CreateChannelCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 欢迎语类型:0普通欢迎语,1渠道欢迎语
        :type Type: int
        :param _UseUserId: 使用成员用户id集
        :type UseUserId: list of int
        :param _UseUserOpenId: 使用成员企微账号id集
        :type UseUserOpenId: list of str
        :param _AppIds: 应用ID,字典表中的APP_TYPE值,多个已逗号分隔
        :type AppIds: str
        :param _Source: 渠道来源
        :type Source: str
        :param _SourceName: 渠道来源名称
        :type SourceName: str
        :param _Name: 二维码名称
        :type Name: str
        :param _Tag: 标签
        :type Tag: list of WeComTagDetail
        :param _SkipVerify: 自动通过好友：0开启 1关闭, 默认开启
        :type SkipVerify: int
        :param _MsgId: 欢迎语id（通过欢迎语新增返回的id）
        :type MsgId: int
        :param _Remark: 备注
        :type Remark: str
        :param _SourceType: 渠道类型 0 未知 1 公域 2私域
        :type SourceType: int
        """
        self._Type = None
        self._UseUserId = None
        self._UseUserOpenId = None
        self._AppIds = None
        self._Source = None
        self._SourceName = None
        self._Name = None
        self._Tag = None
        self._SkipVerify = None
        self._MsgId = None
        self._Remark = None
        self._SourceType = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UseUserId(self):
        return self._UseUserId

    @UseUserId.setter
    def UseUserId(self, UseUserId):
        self._UseUserId = UseUserId

    @property
    def UseUserOpenId(self):
        return self._UseUserOpenId

    @UseUserOpenId.setter
    def UseUserOpenId(self, UseUserOpenId):
        self._UseUserOpenId = UseUserOpenId

    @property
    def AppIds(self):
        return self._AppIds

    @AppIds.setter
    def AppIds(self, AppIds):
        self._AppIds = AppIds

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceName(self):
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def SkipVerify(self):
        return self._SkipVerify

    @SkipVerify.setter
    def SkipVerify(self, SkipVerify):
        self._SkipVerify = SkipVerify

    @property
    def MsgId(self):
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._UseUserId = params.get("UseUserId")
        self._UseUserOpenId = params.get("UseUserOpenId")
        self._AppIds = params.get("AppIds")
        self._Source = params.get("Source")
        self._SourceName = params.get("SourceName")
        self._Name = params.get("Name")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = WeComTagDetail()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._SkipVerify = params.get("SkipVerify")
        self._MsgId = params.get("MsgId")
        self._Remark = params.get("Remark")
        self._SourceType = params.get("SourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateChannelCodeResponse(AbstractModel):
    """CreateChannelCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class CreateCorpTagRequest(AbstractModel):
    """CreateCorpTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 标签组名称，最长为15个字符
        :type GroupName: str
        :param _Tags: 标签信息数组
        :type Tags: list of TagInfo
        :param _Sort: 标签组次序值。sort值大的排序靠前。有效的值范围是[0, 2^32)
        :type Sort: int
        """
        self._GroupName = None
        self._Tags = None
        self._Sort = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCorpTagResponse(AbstractModel):
    """CreateCorpTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TagGroup: 标签组信息
        :type TagGroup: :class:`tencentcloud.wav.v20210129.models.TagGroup`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TagGroup = None
        self._RequestId = None

    @property
    def TagGroup(self):
        return self._TagGroup

    @TagGroup.setter
    def TagGroup(self, TagGroup):
        self._TagGroup = TagGroup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TagGroup") is not None:
            self._TagGroup = TagGroup()
            self._TagGroup._deserialize(params.get("TagGroup"))
        self._RequestId = params.get("RequestId")


class CreateLeadRequest(AbstractModel):
    """CreateLead请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChannelId: 来源ID
        :type ChannelId: int
        :param _ChannelName: 来源名称
        :type ChannelName: str
        :param _CreateTime: 创建时间， 单位毫秒
        :type CreateTime: int
        :param _SourceType: 线索类型：1-400呼入，2-常规留资
        :type SourceType: int
        :param _DealerId: 经销商id
        :type DealerId: int
        :param _BrandId: 品牌id
        :type BrandId: int
        :param _SeriesId: 车系id
        :type SeriesId: int
        :param _CustomerName: 客户姓名
        :type CustomerName: str
        :param _CustomerPhone: 客户手机号
        :type CustomerPhone: str
        :param _ModelId: 车型id
        :type ModelId: int
        :param _CustomerSex: 客户性别: 0-未知, 1-男, 2-女
        :type CustomerSex: int
        :param _SalesName: 销售姓名
        :type SalesName: str
        :param _SalesPhone: 销售手机号
        :type SalesPhone: str
        :param _CcName: Cc坐席姓名
        :type CcName: str
        :param _Remark: 备注
        :type Remark: str
        """
        self._ChannelId = None
        self._ChannelName = None
        self._CreateTime = None
        self._SourceType = None
        self._DealerId = None
        self._BrandId = None
        self._SeriesId = None
        self._CustomerName = None
        self._CustomerPhone = None
        self._ModelId = None
        self._CustomerSex = None
        self._SalesName = None
        self._SalesPhone = None
        self._CcName = None
        self._Remark = None

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
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def DealerId(self):
        return self._DealerId

    @DealerId.setter
    def DealerId(self, DealerId):
        self._DealerId = DealerId

    @property
    def BrandId(self):
        return self._BrandId

    @BrandId.setter
    def BrandId(self, BrandId):
        self._BrandId = BrandId

    @property
    def SeriesId(self):
        return self._SeriesId

    @SeriesId.setter
    def SeriesId(self, SeriesId):
        self._SeriesId = SeriesId

    @property
    def CustomerName(self):
        return self._CustomerName

    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self._CustomerName = CustomerName

    @property
    def CustomerPhone(self):
        return self._CustomerPhone

    @CustomerPhone.setter
    def CustomerPhone(self, CustomerPhone):
        self._CustomerPhone = CustomerPhone

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def CustomerSex(self):
        return self._CustomerSex

    @CustomerSex.setter
    def CustomerSex(self, CustomerSex):
        self._CustomerSex = CustomerSex

    @property
    def SalesName(self):
        return self._SalesName

    @SalesName.setter
    def SalesName(self, SalesName):
        self._SalesName = SalesName

    @property
    def SalesPhone(self):
        return self._SalesPhone

    @SalesPhone.setter
    def SalesPhone(self, SalesPhone):
        self._SalesPhone = SalesPhone

    @property
    def CcName(self):
        return self._CcName

    @CcName.setter
    def CcName(self, CcName):
        self._CcName = CcName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        self._CreateTime = params.get("CreateTime")
        self._SourceType = params.get("SourceType")
        self._DealerId = params.get("DealerId")
        self._BrandId = params.get("BrandId")
        self._SeriesId = params.get("SeriesId")
        self._CustomerName = params.get("CustomerName")
        self._CustomerPhone = params.get("CustomerPhone")
        self._ModelId = params.get("ModelId")
        self._CustomerSex = params.get("CustomerSex")
        self._SalesName = params.get("SalesName")
        self._SalesPhone = params.get("SalesPhone")
        self._CcName = params.get("CcName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLeadResponse(AbstractModel):
    """CreateLead返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessCode: 线索处理状态码： 0-表示创建成功， 1-表示线索合并，2-表示线索重复
        :type BusinessCode: int
        :param _BusinessMsg: 线索处理结果描述
        :type BusinessMsg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessCode = None
        self._BusinessMsg = None
        self._RequestId = None

    @property
    def BusinessCode(self):
        return self._BusinessCode

    @BusinessCode.setter
    def BusinessCode(self, BusinessCode):
        self._BusinessCode = BusinessCode

    @property
    def BusinessMsg(self):
        return self._BusinessMsg

    @BusinessMsg.setter
    def BusinessMsg(self, BusinessMsg):
        self._BusinessMsg = BusinessMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessCode = params.get("BusinessCode")
        self._BusinessMsg = params.get("BusinessMsg")
        self._RequestId = params.get("RequestId")


class CrmStatisticsData(AbstractModel):
    """CRM统计数据响应

    """

    def __init__(self):
        r"""
        :param _LeadCnt: 新增线索
        :type LeadCnt: int
        :param _BuildCnt: 新增建档
        :type BuildCnt: int
        :param _InvitedCnt: 新增到店
        :type InvitedCnt: int
        :param _OrderedCnt: 新增下订
        :type OrderedCnt: int
        :param _DeliveredCnt: 新增成交
        :type DeliveredCnt: int
        :param _DefeatCnt: 新增战败
        :type DefeatCnt: int
        :param _NewContactCnt: 新增好友
        :type NewContactCnt: int
        :param _StatisticalTime: 统计时间, 单位：天
        :type StatisticalTime: str
        """
        self._LeadCnt = None
        self._BuildCnt = None
        self._InvitedCnt = None
        self._OrderedCnt = None
        self._DeliveredCnt = None
        self._DefeatCnt = None
        self._NewContactCnt = None
        self._StatisticalTime = None

    @property
    def LeadCnt(self):
        return self._LeadCnt

    @LeadCnt.setter
    def LeadCnt(self, LeadCnt):
        self._LeadCnt = LeadCnt

    @property
    def BuildCnt(self):
        return self._BuildCnt

    @BuildCnt.setter
    def BuildCnt(self, BuildCnt):
        self._BuildCnt = BuildCnt

    @property
    def InvitedCnt(self):
        return self._InvitedCnt

    @InvitedCnt.setter
    def InvitedCnt(self, InvitedCnt):
        self._InvitedCnt = InvitedCnt

    @property
    def OrderedCnt(self):
        return self._OrderedCnt

    @OrderedCnt.setter
    def OrderedCnt(self, OrderedCnt):
        self._OrderedCnt = OrderedCnt

    @property
    def DeliveredCnt(self):
        return self._DeliveredCnt

    @DeliveredCnt.setter
    def DeliveredCnt(self, DeliveredCnt):
        self._DeliveredCnt = DeliveredCnt

    @property
    def DefeatCnt(self):
        return self._DefeatCnt

    @DefeatCnt.setter
    def DefeatCnt(self, DefeatCnt):
        self._DefeatCnt = DefeatCnt

    @property
    def NewContactCnt(self):
        return self._NewContactCnt

    @NewContactCnt.setter
    def NewContactCnt(self, NewContactCnt):
        self._NewContactCnt = NewContactCnt

    @property
    def StatisticalTime(self):
        return self._StatisticalTime

    @StatisticalTime.setter
    def StatisticalTime(self, StatisticalTime):
        self._StatisticalTime = StatisticalTime


    def _deserialize(self, params):
        self._LeadCnt = params.get("LeadCnt")
        self._BuildCnt = params.get("BuildCnt")
        self._InvitedCnt = params.get("InvitedCnt")
        self._OrderedCnt = params.get("OrderedCnt")
        self._DeliveredCnt = params.get("DeliveredCnt")
        self._DefeatCnt = params.get("DefeatCnt")
        self._NewContactCnt = params.get("NewContactCnt")
        self._StatisticalTime = params.get("StatisticalTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomerActionEventDetail(AbstractModel):
    """外部联系人SaaS使用明细数据

    """

    def __init__(self):
        r"""
        :param _EventCode: 事件码
        :type EventCode: str
        :param _EventType: 事件类型
        :type EventType: int
        :param _EventSource: 事件来源
        :type EventSource: int
        :param _ExternalUserId: 外部联系人id
        :type ExternalUserId: str
        :param _SalesId: 销售顾问id
        :type SalesId: int
        :param _MaterialType: 素材类型
        :type MaterialType: int
        :param _MaterialId: 素材编号id
        :type MaterialId: int
        :param _EventTime: 事件上报时间，单位：秒
        :type EventTime: int
        """
        self._EventCode = None
        self._EventType = None
        self._EventSource = None
        self._ExternalUserId = None
        self._SalesId = None
        self._MaterialType = None
        self._MaterialId = None
        self._EventTime = None

    @property
    def EventCode(self):
        return self._EventCode

    @EventCode.setter
    def EventCode(self, EventCode):
        self._EventCode = EventCode

    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def EventSource(self):
        return self._EventSource

    @EventSource.setter
    def EventSource(self, EventSource):
        self._EventSource = EventSource

    @property
    def ExternalUserId(self):
        return self._ExternalUserId

    @ExternalUserId.setter
    def ExternalUserId(self, ExternalUserId):
        self._ExternalUserId = ExternalUserId

    @property
    def SalesId(self):
        return self._SalesId

    @SalesId.setter
    def SalesId(self, SalesId):
        self._SalesId = SalesId

    @property
    def MaterialType(self):
        return self._MaterialType

    @MaterialType.setter
    def MaterialType(self, MaterialType):
        self._MaterialType = MaterialType

    @property
    def MaterialId(self):
        return self._MaterialId

    @MaterialId.setter
    def MaterialId(self, MaterialId):
        self._MaterialId = MaterialId

    @property
    def EventTime(self):
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime


    def _deserialize(self, params):
        self._EventCode = params.get("EventCode")
        self._EventType = params.get("EventType")
        self._EventSource = params.get("EventSource")
        self._ExternalUserId = params.get("ExternalUserId")
        self._SalesId = params.get("SalesId")
        self._MaterialType = params.get("MaterialType")
        self._MaterialId = params.get("MaterialId")
        self._EventTime = params.get("EventTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomerProfile(AbstractModel):
    """潜客客户档案信息

    """

    def __init__(self):
        r"""
        :param _CustomerId: 客户档案id，客户唯一识别编码
        :type CustomerId: int
        :param _DealerCode: 所属经销商id
        :type DealerCode: str
        :param _UnionId: 客户在微信生态中唯一识别码
        :type UnionId: str
        :param _CreateTime: 档案创建时间戳，单位：秒
        :type CreateTime: str
        :param _UserName: 客户姓名
        :type UserName: str
        :param _Gender: 0未知，1：男，2：女
        :type Gender: int
        :param _Phone: 客户联系手机号
        :type Phone: str
        :param _AgeRangeName: 客户年龄段名称
        :type AgeRangeName: str
        :param _JobTypeName: 客户行业类型名称信息，如教师、医生
        :type JobTypeName: str
        :param _Address: 客户居住地址
        :type Address: str
        :param _LeadsProcessStatus: 客户所处状态
 0:已分配 1:未分配 1 待建档, 2 已建档， 3 已到店 4 已经试驾 5 战败申请中 6 已战败 7 已成交 
        :type LeadsProcessStatus: int
        :param _LeadType: 客户来源类型，1：线上，2：线下
        :type LeadType: int
        :param _SourceName: 与客户来源类型对应的渠道名称
        :type SourceName: str
        :param _LeadsLevelCode: 客户购车的意向等级
        :type LeadsLevelCode: str
        :param _VehicleBrandCode: 客户意向品牌编号
        :type VehicleBrandCode: str
        :param _VehicleSeriesCode: 客户意向车系编号
        :type VehicleSeriesCode: str
        :param _VehicleTypeCode: 客户意向车型编号
        :type VehicleTypeCode: str
        :param _VehiclePurpose: 购车用途信息
        :type VehiclePurpose: :class:`tencentcloud.wav.v20210129.models.VehiclePurpose`
        :param _PurchaseConcern: 购车关注点信息
        :type PurchaseConcern: list of PurchaseConcern
        :param _SalesName: 客户所属顾问姓名
        :type SalesName: str
        :param _SalesPhone: 客户所属顾问手机号
        :type SalesPhone: str
        :param _RealArrivalTime: 客户实际到店时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type RealArrivalTime: int
        :param _CompleteTestDriveTime: 客户到店完成试乘试驾时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type CompleteTestDriveTime: str
        :param _OrderTime: 客户完成下订的时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderTime: int
        :param _DeliveryTime: 客户成交的时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type DeliveryTime: int
        :param _InvoiceTime: 开票时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type InvoiceTime: int
        :param _LoseTime: 完成对此客户战败审批的时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type LoseTime: int
        :param _CreatedAtTime: 线索成功获取的时间戳，单位：秒
        :type CreatedAtTime: int
        :param _ImportAtTime: 线索成功导入的时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type ImportAtTime: int
        :param _DistributeTime: 完成线索分配的时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type DistributeTime: int
        :param _LeadCreateTime: 线索成功创建的时间戳，单位：秒
        :type LeadCreateTime: int
        :param _Nickname: 线索关联微信昵称
        :type Nickname: str
        :param _OrgIdList: 线索归属部门节点
        :type OrgIdList: list of str
        :param _Introducer: 客户的介绍人姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type Introducer: str
        :param _IntroducerPhone: 客户的介绍人手机号码
注意：此字段可能返回 null，表示取不到有效值。
        :type IntroducerPhone: str
        :param _FollowTime: 最近一次完成跟进的时间戳，单位：秒
        :type FollowTime: int
        :param _NextFollowTime: 最近一次计划跟进的时间戳，单位：秒
        :type NextFollowTime: int
        :param _EnterpriseTags: 已为该客户添加的企业标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type EnterpriseTags: list of EnterpriseTag
        :param _ChannelTags: 已为该客户添加的渠道标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelTags: list of ChannelTag
        :param _LeadId: 关联线索id
        :type LeadId: int
        :param _WxId: 客户微信id
        :type WxId: str
        :param _Position: 顾问职位
        :type Position: str
        :param _IsBindWx: 是否关联微信 1 是 0 否
        :type IsBindWx: int
        :param _IsInvalid: 是否无效
        :type IsInvalid: int
        :param _InvalidType: 无效类型
        :type InvalidType: str
        :param _InvalidTypeName: 无效类型名称
        :type InvalidTypeName: str
        :param _InvalidTime: 无效时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InvalidTime: int
        :param _InvalidRemark: 由顾问手动输入的无效原因文字
        :type InvalidRemark: str
        :param _IsLose: 线索是否战败
        :type IsLose: int
        :param _LoseType: 战败类型
        :type LoseType: str
        :param _LoseTypeName: 战败类型名称
        :type LoseTypeName: str
        :param _LoseRemark: 战败申请原因
        :type LoseRemark: str
        """
        self._CustomerId = None
        self._DealerCode = None
        self._UnionId = None
        self._CreateTime = None
        self._UserName = None
        self._Gender = None
        self._Phone = None
        self._AgeRangeName = None
        self._JobTypeName = None
        self._Address = None
        self._LeadsProcessStatus = None
        self._LeadType = None
        self._SourceName = None
        self._LeadsLevelCode = None
        self._VehicleBrandCode = None
        self._VehicleSeriesCode = None
        self._VehicleTypeCode = None
        self._VehiclePurpose = None
        self._PurchaseConcern = None
        self._SalesName = None
        self._SalesPhone = None
        self._RealArrivalTime = None
        self._CompleteTestDriveTime = None
        self._OrderTime = None
        self._DeliveryTime = None
        self._InvoiceTime = None
        self._LoseTime = None
        self._CreatedAtTime = None
        self._ImportAtTime = None
        self._DistributeTime = None
        self._LeadCreateTime = None
        self._Nickname = None
        self._OrgIdList = None
        self._Introducer = None
        self._IntroducerPhone = None
        self._FollowTime = None
        self._NextFollowTime = None
        self._EnterpriseTags = None
        self._ChannelTags = None
        self._LeadId = None
        self._WxId = None
        self._Position = None
        self._IsBindWx = None
        self._IsInvalid = None
        self._InvalidType = None
        self._InvalidTypeName = None
        self._InvalidTime = None
        self._InvalidRemark = None
        self._IsLose = None
        self._LoseType = None
        self._LoseTypeName = None
        self._LoseRemark = None

    @property
    def CustomerId(self):
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def DealerCode(self):
        return self._DealerCode

    @DealerCode.setter
    def DealerCode(self, DealerCode):
        self._DealerCode = DealerCode

    @property
    def UnionId(self):
        return self._UnionId

    @UnionId.setter
    def UnionId(self, UnionId):
        self._UnionId = UnionId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def AgeRangeName(self):
        return self._AgeRangeName

    @AgeRangeName.setter
    def AgeRangeName(self, AgeRangeName):
        self._AgeRangeName = AgeRangeName

    @property
    def JobTypeName(self):
        return self._JobTypeName

    @JobTypeName.setter
    def JobTypeName(self, JobTypeName):
        self._JobTypeName = JobTypeName

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def LeadsProcessStatus(self):
        return self._LeadsProcessStatus

    @LeadsProcessStatus.setter
    def LeadsProcessStatus(self, LeadsProcessStatus):
        self._LeadsProcessStatus = LeadsProcessStatus

    @property
    def LeadType(self):
        return self._LeadType

    @LeadType.setter
    def LeadType(self, LeadType):
        self._LeadType = LeadType

    @property
    def SourceName(self):
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def LeadsLevelCode(self):
        return self._LeadsLevelCode

    @LeadsLevelCode.setter
    def LeadsLevelCode(self, LeadsLevelCode):
        self._LeadsLevelCode = LeadsLevelCode

    @property
    def VehicleBrandCode(self):
        return self._VehicleBrandCode

    @VehicleBrandCode.setter
    def VehicleBrandCode(self, VehicleBrandCode):
        self._VehicleBrandCode = VehicleBrandCode

    @property
    def VehicleSeriesCode(self):
        return self._VehicleSeriesCode

    @VehicleSeriesCode.setter
    def VehicleSeriesCode(self, VehicleSeriesCode):
        self._VehicleSeriesCode = VehicleSeriesCode

    @property
    def VehicleTypeCode(self):
        return self._VehicleTypeCode

    @VehicleTypeCode.setter
    def VehicleTypeCode(self, VehicleTypeCode):
        self._VehicleTypeCode = VehicleTypeCode

    @property
    def VehiclePurpose(self):
        return self._VehiclePurpose

    @VehiclePurpose.setter
    def VehiclePurpose(self, VehiclePurpose):
        self._VehiclePurpose = VehiclePurpose

    @property
    def PurchaseConcern(self):
        return self._PurchaseConcern

    @PurchaseConcern.setter
    def PurchaseConcern(self, PurchaseConcern):
        self._PurchaseConcern = PurchaseConcern

    @property
    def SalesName(self):
        return self._SalesName

    @SalesName.setter
    def SalesName(self, SalesName):
        self._SalesName = SalesName

    @property
    def SalesPhone(self):
        return self._SalesPhone

    @SalesPhone.setter
    def SalesPhone(self, SalesPhone):
        self._SalesPhone = SalesPhone

    @property
    def RealArrivalTime(self):
        return self._RealArrivalTime

    @RealArrivalTime.setter
    def RealArrivalTime(self, RealArrivalTime):
        self._RealArrivalTime = RealArrivalTime

    @property
    def CompleteTestDriveTime(self):
        return self._CompleteTestDriveTime

    @CompleteTestDriveTime.setter
    def CompleteTestDriveTime(self, CompleteTestDriveTime):
        self._CompleteTestDriveTime = CompleteTestDriveTime

    @property
    def OrderTime(self):
        return self._OrderTime

    @OrderTime.setter
    def OrderTime(self, OrderTime):
        self._OrderTime = OrderTime

    @property
    def DeliveryTime(self):
        return self._DeliveryTime

    @DeliveryTime.setter
    def DeliveryTime(self, DeliveryTime):
        self._DeliveryTime = DeliveryTime

    @property
    def InvoiceTime(self):
        return self._InvoiceTime

    @InvoiceTime.setter
    def InvoiceTime(self, InvoiceTime):
        self._InvoiceTime = InvoiceTime

    @property
    def LoseTime(self):
        return self._LoseTime

    @LoseTime.setter
    def LoseTime(self, LoseTime):
        self._LoseTime = LoseTime

    @property
    def CreatedAtTime(self):
        return self._CreatedAtTime

    @CreatedAtTime.setter
    def CreatedAtTime(self, CreatedAtTime):
        self._CreatedAtTime = CreatedAtTime

    @property
    def ImportAtTime(self):
        return self._ImportAtTime

    @ImportAtTime.setter
    def ImportAtTime(self, ImportAtTime):
        self._ImportAtTime = ImportAtTime

    @property
    def DistributeTime(self):
        return self._DistributeTime

    @DistributeTime.setter
    def DistributeTime(self, DistributeTime):
        self._DistributeTime = DistributeTime

    @property
    def LeadCreateTime(self):
        return self._LeadCreateTime

    @LeadCreateTime.setter
    def LeadCreateTime(self, LeadCreateTime):
        self._LeadCreateTime = LeadCreateTime

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def OrgIdList(self):
        return self._OrgIdList

    @OrgIdList.setter
    def OrgIdList(self, OrgIdList):
        self._OrgIdList = OrgIdList

    @property
    def Introducer(self):
        return self._Introducer

    @Introducer.setter
    def Introducer(self, Introducer):
        self._Introducer = Introducer

    @property
    def IntroducerPhone(self):
        return self._IntroducerPhone

    @IntroducerPhone.setter
    def IntroducerPhone(self, IntroducerPhone):
        self._IntroducerPhone = IntroducerPhone

    @property
    def FollowTime(self):
        return self._FollowTime

    @FollowTime.setter
    def FollowTime(self, FollowTime):
        self._FollowTime = FollowTime

    @property
    def NextFollowTime(self):
        return self._NextFollowTime

    @NextFollowTime.setter
    def NextFollowTime(self, NextFollowTime):
        self._NextFollowTime = NextFollowTime

    @property
    def EnterpriseTags(self):
        return self._EnterpriseTags

    @EnterpriseTags.setter
    def EnterpriseTags(self, EnterpriseTags):
        self._EnterpriseTags = EnterpriseTags

    @property
    def ChannelTags(self):
        return self._ChannelTags

    @ChannelTags.setter
    def ChannelTags(self, ChannelTags):
        self._ChannelTags = ChannelTags

    @property
    def LeadId(self):
        return self._LeadId

    @LeadId.setter
    def LeadId(self, LeadId):
        self._LeadId = LeadId

    @property
    def WxId(self):
        return self._WxId

    @WxId.setter
    def WxId(self, WxId):
        self._WxId = WxId

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def IsBindWx(self):
        return self._IsBindWx

    @IsBindWx.setter
    def IsBindWx(self, IsBindWx):
        self._IsBindWx = IsBindWx

    @property
    def IsInvalid(self):
        return self._IsInvalid

    @IsInvalid.setter
    def IsInvalid(self, IsInvalid):
        self._IsInvalid = IsInvalid

    @property
    def InvalidType(self):
        return self._InvalidType

    @InvalidType.setter
    def InvalidType(self, InvalidType):
        self._InvalidType = InvalidType

    @property
    def InvalidTypeName(self):
        return self._InvalidTypeName

    @InvalidTypeName.setter
    def InvalidTypeName(self, InvalidTypeName):
        self._InvalidTypeName = InvalidTypeName

    @property
    def InvalidTime(self):
        return self._InvalidTime

    @InvalidTime.setter
    def InvalidTime(self, InvalidTime):
        self._InvalidTime = InvalidTime

    @property
    def InvalidRemark(self):
        return self._InvalidRemark

    @InvalidRemark.setter
    def InvalidRemark(self, InvalidRemark):
        self._InvalidRemark = InvalidRemark

    @property
    def IsLose(self):
        return self._IsLose

    @IsLose.setter
    def IsLose(self, IsLose):
        self._IsLose = IsLose

    @property
    def LoseType(self):
        return self._LoseType

    @LoseType.setter
    def LoseType(self, LoseType):
        self._LoseType = LoseType

    @property
    def LoseTypeName(self):
        return self._LoseTypeName

    @LoseTypeName.setter
    def LoseTypeName(self, LoseTypeName):
        self._LoseTypeName = LoseTypeName

    @property
    def LoseRemark(self):
        return self._LoseRemark

    @LoseRemark.setter
    def LoseRemark(self, LoseRemark):
        self._LoseRemark = LoseRemark


    def _deserialize(self, params):
        self._CustomerId = params.get("CustomerId")
        self._DealerCode = params.get("DealerCode")
        self._UnionId = params.get("UnionId")
        self._CreateTime = params.get("CreateTime")
        self._UserName = params.get("UserName")
        self._Gender = params.get("Gender")
        self._Phone = params.get("Phone")
        self._AgeRangeName = params.get("AgeRangeName")
        self._JobTypeName = params.get("JobTypeName")
        self._Address = params.get("Address")
        self._LeadsProcessStatus = params.get("LeadsProcessStatus")
        self._LeadType = params.get("LeadType")
        self._SourceName = params.get("SourceName")
        self._LeadsLevelCode = params.get("LeadsLevelCode")
        self._VehicleBrandCode = params.get("VehicleBrandCode")
        self._VehicleSeriesCode = params.get("VehicleSeriesCode")
        self._VehicleTypeCode = params.get("VehicleTypeCode")
        if params.get("VehiclePurpose") is not None:
            self._VehiclePurpose = VehiclePurpose()
            self._VehiclePurpose._deserialize(params.get("VehiclePurpose"))
        if params.get("PurchaseConcern") is not None:
            self._PurchaseConcern = []
            for item in params.get("PurchaseConcern"):
                obj = PurchaseConcern()
                obj._deserialize(item)
                self._PurchaseConcern.append(obj)
        self._SalesName = params.get("SalesName")
        self._SalesPhone = params.get("SalesPhone")
        self._RealArrivalTime = params.get("RealArrivalTime")
        self._CompleteTestDriveTime = params.get("CompleteTestDriveTime")
        self._OrderTime = params.get("OrderTime")
        self._DeliveryTime = params.get("DeliveryTime")
        self._InvoiceTime = params.get("InvoiceTime")
        self._LoseTime = params.get("LoseTime")
        self._CreatedAtTime = params.get("CreatedAtTime")
        self._ImportAtTime = params.get("ImportAtTime")
        self._DistributeTime = params.get("DistributeTime")
        self._LeadCreateTime = params.get("LeadCreateTime")
        self._Nickname = params.get("Nickname")
        self._OrgIdList = params.get("OrgIdList")
        self._Introducer = params.get("Introducer")
        self._IntroducerPhone = params.get("IntroducerPhone")
        self._FollowTime = params.get("FollowTime")
        self._NextFollowTime = params.get("NextFollowTime")
        if params.get("EnterpriseTags") is not None:
            self._EnterpriseTags = []
            for item in params.get("EnterpriseTags"):
                obj = EnterpriseTag()
                obj._deserialize(item)
                self._EnterpriseTags.append(obj)
        if params.get("ChannelTags") is not None:
            self._ChannelTags = []
            for item in params.get("ChannelTags"):
                obj = ChannelTag()
                obj._deserialize(item)
                self._ChannelTags.append(obj)
        self._LeadId = params.get("LeadId")
        self._WxId = params.get("WxId")
        self._Position = params.get("Position")
        self._IsBindWx = params.get("IsBindWx")
        self._IsInvalid = params.get("IsInvalid")
        self._InvalidType = params.get("InvalidType")
        self._InvalidTypeName = params.get("InvalidTypeName")
        self._InvalidTime = params.get("InvalidTime")
        self._InvalidRemark = params.get("InvalidRemark")
        self._IsLose = params.get("IsLose")
        self._LoseType = params.get("LoseType")
        self._LoseTypeName = params.get("LoseTypeName")
        self._LoseRemark = params.get("LoseRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DealerInfo(AbstractModel):
    """经销商信息

    """

    def __init__(self):
        r"""
        :param _DealerId: 企微SaaS平台经销商id
        :type DealerId: int
        :param _DealerName: 经销商名称
        :type DealerName: str
        :param _ProvinceCode: 所属省份编号
注意：此字段可能返回 null，表示取不到有效值。
        :type ProvinceCode: str
        :param _CityCodeList: 所属城市编号列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CityCodeList: list of str
        :param _BrandIdList: 业务覆盖品牌id列表
注意：此字段可能返回 null，表示取不到有效值。
        :type BrandIdList: list of str
        """
        self._DealerId = None
        self._DealerName = None
        self._ProvinceCode = None
        self._CityCodeList = None
        self._BrandIdList = None

    @property
    def DealerId(self):
        return self._DealerId

    @DealerId.setter
    def DealerId(self, DealerId):
        self._DealerId = DealerId

    @property
    def DealerName(self):
        return self._DealerName

    @DealerName.setter
    def DealerName(self, DealerName):
        self._DealerName = DealerName

    @property
    def ProvinceCode(self):
        return self._ProvinceCode

    @ProvinceCode.setter
    def ProvinceCode(self, ProvinceCode):
        self._ProvinceCode = ProvinceCode

    @property
    def CityCodeList(self):
        return self._CityCodeList

    @CityCodeList.setter
    def CityCodeList(self, CityCodeList):
        self._CityCodeList = CityCodeList

    @property
    def BrandIdList(self):
        return self._BrandIdList

    @BrandIdList.setter
    def BrandIdList(self, BrandIdList):
        self._BrandIdList = BrandIdList


    def _deserialize(self, params):
        self._DealerId = params.get("DealerId")
        self._DealerName = params.get("DealerName")
        self._ProvinceCode = params.get("ProvinceCode")
        self._CityCodeList = params.get("CityCodeList")
        self._BrandIdList = params.get("BrandIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnterpriseTag(AbstractModel):
    """客户企业标签

    """

    def __init__(self):
        r"""
        :param _GroupName: 该客户档案当前已成功关联的企业标签分组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _TagName: 该客户档案当前已成功关联的企业标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TagName: str
        :param _TagId: 该客户档案当前已成功关联的企业标签的id
注意：此字段可能返回 null，表示取不到有效值。
        :type TagId: str
        """
        self._GroupName = None
        self._TagName = None
        self._TagId = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TagName(self):
        return self._TagName

    @TagName.setter
    def TagName(self, TagName):
        self._TagName = TagName

    @property
    def TagId(self):
        return self._TagId

    @TagId.setter
    def TagId(self, TagId):
        self._TagId = TagId


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._TagName = params.get("TagName")
        self._TagId = params.get("TagId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalContact(AbstractModel):
    """客户信息

    """

    def __init__(self):
        r"""
        :param _ExternalUserId: 外部联系人的userId
        :type ExternalUserId: str
        :param _Gender: 外部联系人性别 0-未知 1-男性 2-女性
        :type Gender: int
        :param _Name: 外部联系人的名称
        :type Name: str
        :param _Type: 外部联系人的类型，1表示该外部联系人是微信用户，2表示该外部联系人是企业微信用户
        :type Type: int
        :param _UnionId: 外部联系人在微信开放平台的唯一身份标识（微信unionid），通过此字段企业可将外部联系人与公众号/小程序用户关联起来。仅当联系人类型是微信用户，且企业或第三方服务商绑定了微信开发者ID有此字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnionId: str
        :param _Phone: 外部联系人联系电话
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        """
        self._ExternalUserId = None
        self._Gender = None
        self._Name = None
        self._Type = None
        self._UnionId = None
        self._Phone = None

    @property
    def ExternalUserId(self):
        return self._ExternalUserId

    @ExternalUserId.setter
    def ExternalUserId(self, ExternalUserId):
        self._ExternalUserId = ExternalUserId

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

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
    def UnionId(self):
        return self._UnionId

    @UnionId.setter
    def UnionId(self, UnionId):
        self._UnionId = UnionId

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone


    def _deserialize(self, params):
        self._ExternalUserId = params.get("ExternalUserId")
        self._Gender = params.get("Gender")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._UnionId = params.get("UnionId")
        self._Phone = params.get("Phone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalContactDetailPro(AbstractModel):
    """具备更多信息的外部联系人详细信息

    """

    def __init__(self):
        r"""
        :param _Customer: 客户信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Customer: :class:`tencentcloud.wav.v20210129.models.ExternalContact`
        :param _FollowUser: 添加了此外部联系人的企业成员信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowUser: list of FollowUserPro
        """
        self._Customer = None
        self._FollowUser = None

    @property
    def Customer(self):
        return self._Customer

    @Customer.setter
    def Customer(self, Customer):
        self._Customer = Customer

    @property
    def FollowUser(self):
        return self._FollowUser

    @FollowUser.setter
    def FollowUser(self, FollowUser):
        self._FollowUser = FollowUser


    def _deserialize(self, params):
        if params.get("Customer") is not None:
            self._Customer = ExternalContact()
            self._Customer._deserialize(params.get("Customer"))
        if params.get("FollowUser") is not None:
            self._FollowUser = []
            for item in params.get("FollowUser"):
                obj = FollowUserPro()
                obj._deserialize(item)
                self._FollowUser.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalContactSimpleInfo(AbstractModel):
    """外部联系人简短信息

    """

    def __init__(self):
        r"""
        :param _ExternalUserId: 外部联系人的userId
        :type ExternalUserId: str
        :param _UserId: 添加了此外部联系人的企业成员userId
        :type UserId: str
        :param _SalesName: 添加了此外部联系人的企业成员的姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type SalesName: str
        :param _DepartmentIdList: 添加了此外部联系人的企业成员的归属部门id列表
        :type DepartmentIdList: list of int
        """
        self._ExternalUserId = None
        self._UserId = None
        self._SalesName = None
        self._DepartmentIdList = None

    @property
    def ExternalUserId(self):
        return self._ExternalUserId

    @ExternalUserId.setter
    def ExternalUserId(self, ExternalUserId):
        self._ExternalUserId = ExternalUserId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SalesName(self):
        return self._SalesName

    @SalesName.setter
    def SalesName(self, SalesName):
        self._SalesName = SalesName

    @property
    def DepartmentIdList(self):
        return self._DepartmentIdList

    @DepartmentIdList.setter
    def DepartmentIdList(self, DepartmentIdList):
        self._DepartmentIdList = DepartmentIdList


    def _deserialize(self, params):
        self._ExternalUserId = params.get("ExternalUserId")
        self._UserId = params.get("UserId")
        self._SalesName = params.get("SalesName")
        self._DepartmentIdList = params.get("DepartmentIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalContactTag(AbstractModel):
    """外部联系人标签

    """

    def __init__(self):
        r"""
        :param _GroupName: 该成员添加此外部联系人所打标签的分组名称（标签功能需要企业微信升级到2.7.5及以上版本）
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _TagName: 该成员添加此外部联系人所打标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TagName: str
        :param _Type: 该成员添加此外部联系人所打标签类型, 1-企业设置, 2-用户自定义
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _TagId: 该成员添加此外部联系人所打企业标签的id，仅企业设置（type为1）的标签返回
注意：此字段可能返回 null，表示取不到有效值。
        :type TagId: str
        """
        self._GroupName = None
        self._TagName = None
        self._Type = None
        self._TagId = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TagName(self):
        return self._TagName

    @TagName.setter
    def TagName(self, TagName):
        self._TagName = TagName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TagId(self):
        return self._TagId

    @TagId.setter
    def TagId(self, TagId):
        self._TagId = TagId


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._TagName = params.get("TagName")
        self._Type = params.get("Type")
        self._TagId = params.get("TagId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalUserEventInfo(AbstractModel):
    """外部联系人事件信息

    """

    def __init__(self):
        r"""
        :param _EventCode: 事件编码, 添加外部联系人(ADD_EXTERNAL_CUSTOMER)/成员删除外部联系人(DELETE_EXTERNAL_CUSTOMER)/外部联系人删除成员(DELETE_FOLLOW_USER)
        :type EventCode: str
        :param _ExternalUserId: 外部联系人id
        :type ExternalUserId: str
        :param _SalesId: 企微SaaS的成员id
        :type SalesId: str
        :param _EventTime: 事件上报时间戳，单位：秒
        :type EventTime: int
        """
        self._EventCode = None
        self._ExternalUserId = None
        self._SalesId = None
        self._EventTime = None

    @property
    def EventCode(self):
        return self._EventCode

    @EventCode.setter
    def EventCode(self, EventCode):
        self._EventCode = EventCode

    @property
    def ExternalUserId(self):
        return self._ExternalUserId

    @ExternalUserId.setter
    def ExternalUserId(self, ExternalUserId):
        self._ExternalUserId = ExternalUserId

    @property
    def SalesId(self):
        return self._SalesId

    @SalesId.setter
    def SalesId(self, SalesId):
        self._SalesId = SalesId

    @property
    def EventTime(self):
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime


    def _deserialize(self, params):
        self._EventCode = params.get("EventCode")
        self._ExternalUserId = params.get("ExternalUserId")
        self._SalesId = params.get("SalesId")
        self._EventTime = params.get("EventTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalUserMappingInfo(AbstractModel):
    """外部联系人映射信息

    """

    def __init__(self):
        r"""
        :param _CorpExternalUserId: 企业主体对应的外部联系人userId
        :type CorpExternalUserId: str
        :param _ExternalUserId: 乐销车应用主体对应的外部联系人, 当不存在好友关系时，该字段值为空
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalUserId: str
        """
        self._CorpExternalUserId = None
        self._ExternalUserId = None

    @property
    def CorpExternalUserId(self):
        return self._CorpExternalUserId

    @CorpExternalUserId.setter
    def CorpExternalUserId(self, CorpExternalUserId):
        self._CorpExternalUserId = CorpExternalUserId

    @property
    def ExternalUserId(self):
        return self._ExternalUserId

    @ExternalUserId.setter
    def ExternalUserId(self, ExternalUserId):
        self._ExternalUserId = ExternalUserId


    def _deserialize(self, params):
        self._CorpExternalUserId = params.get("CorpExternalUserId")
        self._ExternalUserId = params.get("ExternalUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FollowInfo(AbstractModel):
    """发生过跟进的潜客信息

    """

    def __init__(self):
        r"""
        :param _ClueId: 线索id
        :type ClueId: int
        :param _CustomerId: 客户档案id
        :type CustomerId: int
        :param _UserName: 客户姓名
        :type UserName: str
        :param _Phone: 客户的手机号
        :type Phone: str
        :param _IsOverdue: 是否逾期
        :type IsOverdue: int
        :param _OverdueTime: 逾期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OverdueTime: int
        :param _EventType: 发生事件
        :type EventType: int
        :param _EventTypeName: 发生事件名称
        :type EventTypeName: str
        :param _FollowWayType: 跟进方式
        :type FollowWayType: str
        :param _FollowWayName: 跟进方式名称
        :type FollowWayName: str
        :param _FollowTime: 本次跟进时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowTime: int
        :param _NextFollowTime: 下次跟进时间
注意：此字段可能返回 null，表示取不到有效值。
        :type NextFollowTime: int
        :param _FollowRecord: 跟进记录
        :type FollowRecord: str
        """
        self._ClueId = None
        self._CustomerId = None
        self._UserName = None
        self._Phone = None
        self._IsOverdue = None
        self._OverdueTime = None
        self._EventType = None
        self._EventTypeName = None
        self._FollowWayType = None
        self._FollowWayName = None
        self._FollowTime = None
        self._NextFollowTime = None
        self._FollowRecord = None

    @property
    def ClueId(self):
        return self._ClueId

    @ClueId.setter
    def ClueId(self, ClueId):
        self._ClueId = ClueId

    @property
    def CustomerId(self):
        return self._CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId):
        self._CustomerId = CustomerId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def IsOverdue(self):
        return self._IsOverdue

    @IsOverdue.setter
    def IsOverdue(self, IsOverdue):
        self._IsOverdue = IsOverdue

    @property
    def OverdueTime(self):
        return self._OverdueTime

    @OverdueTime.setter
    def OverdueTime(self, OverdueTime):
        self._OverdueTime = OverdueTime

    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def EventTypeName(self):
        return self._EventTypeName

    @EventTypeName.setter
    def EventTypeName(self, EventTypeName):
        self._EventTypeName = EventTypeName

    @property
    def FollowWayType(self):
        return self._FollowWayType

    @FollowWayType.setter
    def FollowWayType(self, FollowWayType):
        self._FollowWayType = FollowWayType

    @property
    def FollowWayName(self):
        return self._FollowWayName

    @FollowWayName.setter
    def FollowWayName(self, FollowWayName):
        self._FollowWayName = FollowWayName

    @property
    def FollowTime(self):
        return self._FollowTime

    @FollowTime.setter
    def FollowTime(self, FollowTime):
        self._FollowTime = FollowTime

    @property
    def NextFollowTime(self):
        return self._NextFollowTime

    @NextFollowTime.setter
    def NextFollowTime(self, NextFollowTime):
        self._NextFollowTime = NextFollowTime

    @property
    def FollowRecord(self):
        return self._FollowRecord

    @FollowRecord.setter
    def FollowRecord(self, FollowRecord):
        self._FollowRecord = FollowRecord


    def _deserialize(self, params):
        self._ClueId = params.get("ClueId")
        self._CustomerId = params.get("CustomerId")
        self._UserName = params.get("UserName")
        self._Phone = params.get("Phone")
        self._IsOverdue = params.get("IsOverdue")
        self._OverdueTime = params.get("OverdueTime")
        self._EventType = params.get("EventType")
        self._EventTypeName = params.get("EventTypeName")
        self._FollowWayType = params.get("FollowWayType")
        self._FollowWayName = params.get("FollowWayName")
        self._FollowTime = params.get("FollowTime")
        self._NextFollowTime = params.get("NextFollowTime")
        self._FollowRecord = params.get("FollowRecord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FollowUser(AbstractModel):
    """添加了此外部联系人的企业成员信息

    """

    def __init__(self):
        r"""
        :param _UserId: 添加了此外部联系人的企业成员userid
        :type UserId: str
        :param _Remark: 该成员对此外部联系人的备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _Description: 该成员对此外部联系人的描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreateTime: 该成员添加此外部联系人的时间戳，单位为秒
        :type CreateTime: int
        :param _AddWay: 该成员添加此客户的来源，具体含义详见<a href="https://work.weixin.qq.com/api/doc/90000/90135/92114#%E6%9D%A5%E6%BA%90%E5%AE%9A%E4%B9%89">来源定义</a>
        :type AddWay: int
        :param _OperUserId: 发起添加的userid，如果成员主动添加，为成员的userid；如果是客户主动添加，则为客户的外部联系人userid；如果是内部成员共享/管理员分配，则为对应的成员/管理员userid
        :type OperUserId: str
        :param _Tags: 该成员添加此外部联系人所打标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of ExternalContactTag
        """
        self._UserId = None
        self._Remark = None
        self._Description = None
        self._CreateTime = None
        self._AddWay = None
        self._OperUserId = None
        self._Tags = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AddWay(self):
        return self._AddWay

    @AddWay.setter
    def AddWay(self, AddWay):
        self._AddWay = AddWay

    @property
    def OperUserId(self):
        return self._OperUserId

    @OperUserId.setter
    def OperUserId(self, OperUserId):
        self._OperUserId = OperUserId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Remark = params.get("Remark")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._AddWay = params.get("AddWay")
        self._OperUserId = params.get("OperUserId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ExternalContactTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FollowUserPro(AbstractModel):
    """具备更多信息的添加了此外部联系人的企业成员信息

    """

    def __init__(self):
        r"""
        :param _UserId: 添加了此外部联系人的企业成员userid
        :type UserId: str
        :param _Remark: 该成员对此外部联系人的备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _Description: 该成员对此外部联系人的描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreateTime: 该成员添加此外部联系人的时间戳，单位为秒
        :type CreateTime: int
        :param _AddWay: 该成员添加此客户的来源，具体含义详见<a href="https://work.weixin.qq.com/api/doc/90000/90135/92114#%E6%9D%A5%E6%BA%90%E5%AE%9A%E4%B9%89">来源定义</a>
        :type AddWay: int
        :param _OperUserId: 发起添加的userid，如果成员主动添加，为成员的userid；如果是客户主动添加，则为客户的外部联系人userid；如果是内部成员共享/管理员分配，则为对应的成员/管理员userid
        :type OperUserId: str
        :param _Tags: 该成员添加此外部联系人所打标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of ExternalContactTag
        :param _SalesName: 添加了此外部联系人的企业成员的姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type SalesName: str
        :param _DepartmentIdList: 企业成员的归属部门id列表
        :type DepartmentIdList: list of int
        """
        self._UserId = None
        self._Remark = None
        self._Description = None
        self._CreateTime = None
        self._AddWay = None
        self._OperUserId = None
        self._Tags = None
        self._SalesName = None
        self._DepartmentIdList = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AddWay(self):
        return self._AddWay

    @AddWay.setter
    def AddWay(self, AddWay):
        self._AddWay = AddWay

    @property
    def OperUserId(self):
        return self._OperUserId

    @OperUserId.setter
    def OperUserId(self, OperUserId):
        self._OperUserId = OperUserId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SalesName(self):
        return self._SalesName

    @SalesName.setter
    def SalesName(self, SalesName):
        self._SalesName = SalesName

    @property
    def DepartmentIdList(self):
        return self._DepartmentIdList

    @DepartmentIdList.setter
    def DepartmentIdList(self, DepartmentIdList):
        self._DepartmentIdList = DepartmentIdList


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Remark = params.get("Remark")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._AddWay = params.get("AddWay")
        self._OperUserId = params.get("OperUserId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ExternalContactTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SalesName = params.get("SalesName")
        self._DepartmentIdList = params.get("DepartmentIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicenseInfo(AbstractModel):
    """license相关信息

    """

    def __init__(self):
        r"""
        :param _License: license编号
        :type License: str
        :param _LicenseEdition: license版本；1-基础版，2-标准版，3-增值版
        :type LicenseEdition: int
        :param _ResourceStartTime: 生效开始时间, 格式yyyy-MM-dd HH:mm:ss
        :type ResourceStartTime: str
        :param _ResourceEndTime: 生效结束时间, 格式yyyy-MM-dd HH:mm:ss
        :type ResourceEndTime: str
        :param _IsolationDeadline: 隔离截止时间, 格式yyyy-MM-dd HH:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolationDeadline: str
        :param _DestroyTime: 资源计划销毁时间, 格式yyyy-MM-dd HH:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type DestroyTime: str
        :param _Status: 资源状态，1.正常，2.隔离，3.销毁
        :type Status: int
        :param _Extra: 扩展信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        """
        self._License = None
        self._LicenseEdition = None
        self._ResourceStartTime = None
        self._ResourceEndTime = None
        self._IsolationDeadline = None
        self._DestroyTime = None
        self._Status = None
        self._Extra = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def LicenseEdition(self):
        return self._LicenseEdition

    @LicenseEdition.setter
    def LicenseEdition(self, LicenseEdition):
        self._LicenseEdition = LicenseEdition

    @property
    def ResourceStartTime(self):
        return self._ResourceStartTime

    @ResourceStartTime.setter
    def ResourceStartTime(self, ResourceStartTime):
        self._ResourceStartTime = ResourceStartTime

    @property
    def ResourceEndTime(self):
        return self._ResourceEndTime

    @ResourceEndTime.setter
    def ResourceEndTime(self, ResourceEndTime):
        self._ResourceEndTime = ResourceEndTime

    @property
    def IsolationDeadline(self):
        return self._IsolationDeadline

    @IsolationDeadline.setter
    def IsolationDeadline(self, IsolationDeadline):
        self._IsolationDeadline = IsolationDeadline

    @property
    def DestroyTime(self):
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra


    def _deserialize(self, params):
        self._License = params.get("License")
        self._LicenseEdition = params.get("LicenseEdition")
        self._ResourceStartTime = params.get("ResourceStartTime")
        self._ResourceEndTime = params.get("ResourceEndTime")
        self._IsolationDeadline = params.get("IsolationDeadline")
        self._DestroyTime = params.get("DestroyTime")
        self._Status = params.get("Status")
        self._Extra = params.get("Extra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveCodeDetail(AbstractModel):
    """活动活码详情

    """

    def __init__(self):
        r"""
        :param _LiveCodeId: 活码id
        :type LiveCodeId: int
        :param _LiveCodeName: 活码名称
        :type LiveCodeName: str
        :param _ShortChainAddress: 短链url
注意：此字段可能返回 null，表示取不到有效值。
        :type ShortChainAddress: str
        :param _LiveCodePreview: 活码二维码
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveCodePreview: str
        :param _ActivityId: 活动id
        :type ActivityId: int
        :param _ActivityName: 活动名称
        :type ActivityName: str
        :param _LiveCodeState: 活码状态，-1：删除，0：启用，1禁用，默认为0
        :type LiveCodeState: int
        :param _LiveCodeData: 活码参数，每个活码参数都是不一样的， 这个的值对应的是字符串json类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveCodeData: str
        :param _CreateTime: 创建时间戳，单位为秒
        :type CreateTime: int
        :param _UpdateTime: 更新时间戳，单位为秒
        :type UpdateTime: int
        """
        self._LiveCodeId = None
        self._LiveCodeName = None
        self._ShortChainAddress = None
        self._LiveCodePreview = None
        self._ActivityId = None
        self._ActivityName = None
        self._LiveCodeState = None
        self._LiveCodeData = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def LiveCodeId(self):
        return self._LiveCodeId

    @LiveCodeId.setter
    def LiveCodeId(self, LiveCodeId):
        self._LiveCodeId = LiveCodeId

    @property
    def LiveCodeName(self):
        return self._LiveCodeName

    @LiveCodeName.setter
    def LiveCodeName(self, LiveCodeName):
        self._LiveCodeName = LiveCodeName

    @property
    def ShortChainAddress(self):
        return self._ShortChainAddress

    @ShortChainAddress.setter
    def ShortChainAddress(self, ShortChainAddress):
        self._ShortChainAddress = ShortChainAddress

    @property
    def LiveCodePreview(self):
        return self._LiveCodePreview

    @LiveCodePreview.setter
    def LiveCodePreview(self, LiveCodePreview):
        self._LiveCodePreview = LiveCodePreview

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def ActivityName(self):
        return self._ActivityName

    @ActivityName.setter
    def ActivityName(self, ActivityName):
        self._ActivityName = ActivityName

    @property
    def LiveCodeState(self):
        return self._LiveCodeState

    @LiveCodeState.setter
    def LiveCodeState(self, LiveCodeState):
        self._LiveCodeState = LiveCodeState

    @property
    def LiveCodeData(self):
        return self._LiveCodeData

    @LiveCodeData.setter
    def LiveCodeData(self, LiveCodeData):
        self._LiveCodeData = LiveCodeData

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._LiveCodeId = params.get("LiveCodeId")
        self._LiveCodeName = params.get("LiveCodeName")
        self._ShortChainAddress = params.get("ShortChainAddress")
        self._LiveCodePreview = params.get("LiveCodePreview")
        self._ActivityId = params.get("ActivityId")
        self._ActivityName = params.get("ActivityName")
        self._LiveCodeState = params.get("LiveCodeState")
        self._LiveCodeData = params.get("LiveCodeData")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaterialInfo(AbstractModel):
    """素材信息响应体

    """

    def __init__(self):
        r"""
        :param _MaterialId: 素材id
        :type MaterialId: int
        :param _MaterialName: 素材名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MaterialName: str
        :param _Status: 素材状态, -1: 删除 0: 启用 1: 禁用
        :type Status: int
        """
        self._MaterialId = None
        self._MaterialName = None
        self._Status = None

    @property
    def MaterialId(self):
        return self._MaterialId

    @MaterialId.setter
    def MaterialId(self, MaterialId):
        self._MaterialId = MaterialId

    @property
    def MaterialName(self):
        return self._MaterialName

    @MaterialName.setter
    def MaterialName(self, MaterialName):
        self._MaterialName = MaterialName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._MaterialId = params.get("MaterialId")
        self._MaterialName = params.get("MaterialName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MiniAppCodeInfo(AbstractModel):
    """小程序码信息

    """

    def __init__(self):
        r"""
        :param _Id: 主键id
        :type Id: int
        :param _MiniAppName: 小程序名称
        :type MiniAppName: str
        :param _MiniAppLogo: 小程序logo
        :type MiniAppLogo: str
        :param _MiniAdminUrl: 小程序管理端地址
        :type MiniAdminUrl: str
        :param _State: 状态：0正常，1删除
        :type State: int
        :param _CreateTime: 创建时间戳，单位为秒
        :type CreateTime: int
        :param _UpdateTime: 更新时间戳，单位为秒
        :type UpdateTime: int
        """
        self._Id = None
        self._MiniAppName = None
        self._MiniAppLogo = None
        self._MiniAdminUrl = None
        self._State = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MiniAppName(self):
        return self._MiniAppName

    @MiniAppName.setter
    def MiniAppName(self, MiniAppName):
        self._MiniAppName = MiniAppName

    @property
    def MiniAppLogo(self):
        return self._MiniAppLogo

    @MiniAppLogo.setter
    def MiniAppLogo(self, MiniAppLogo):
        self._MiniAppLogo = MiniAppLogo

    @property
    def MiniAdminUrl(self):
        return self._MiniAdminUrl

    @MiniAdminUrl.setter
    def MiniAdminUrl(self, MiniAdminUrl):
        self._MiniAdminUrl = MiniAdminUrl

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MiniAppName = params.get("MiniAppName")
        self._MiniAppLogo = params.get("MiniAppLogo")
        self._MiniAdminUrl = params.get("MiniAdminUrl")
        self._State = params.get("State")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurchaseConcern(AbstractModel):
    """购车关注点

    """

    def __init__(self):
        r"""
        :param _Code: 购车关注点code
        :type Code: str
        :param _Description: 购车关注点描述
        :type Description: str
        """
        self._Code = None
        self._Description = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryActivityJoinListRequest(AbstractModel):
    """QueryActivityJoinList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityId: 活动id
        :type ActivityId: int
        :param _Cursor: 分页游标，对应结果返回的NextCursor,首次请求保持为空
        :type Cursor: str
        :param _Limit: 单页数据限制
        :type Limit: int
        """
        self._ActivityId = None
        self._Cursor = None
        self._Limit = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryActivityJoinListResponse(AbstractModel):
    """QueryActivityJoinList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextCursor: 分页游标
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _PageData: 活码列表响应参数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of ActivityJoinDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextCursor = None
        self._PageData = None
        self._RequestId = None

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = ActivityJoinDetail()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._RequestId = params.get("RequestId")


class QueryActivityListRequest(AbstractModel):
    """QueryActivityList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Cursor: 分页游标，对应结果返回的NextCursor,首次请求保持为空
        :type Cursor: str
        :param _Limit: 单页数据限制
        :type Limit: int
        """
        self._Cursor = None
        self._Limit = None

    @property
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryActivityListResponse(AbstractModel):
    """QueryActivityList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextCursor: 分页游标
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _PageData: 活码列表响应参数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of ActivityDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextCursor = None
        self._PageData = None
        self._RequestId = None

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = ActivityDetail()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._RequestId = params.get("RequestId")


class QueryActivityLiveCodeListRequest(AbstractModel):
    """QueryActivityLiveCodeList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        :param _Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值
        :type Limit: int
        """
        self._Cursor = None
        self._Limit = None

    @property
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryActivityLiveCodeListResponse(AbstractModel):
    """QueryActivityLiveCodeList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _PageData: 活码列表响应参数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of LiveCodeDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextCursor = None
        self._PageData = None
        self._RequestId = None

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = LiveCodeDetail()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._RequestId = params.get("RequestId")


class QueryArrivalListRequest(AbstractModel):
    """QueryArrivalList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页，预期请求的数据量，取值范围 1 ~ 1000
        :type Limit: int
        :param _BeginTime: 查询开始时间， 单位秒
        :type BeginTime: int
        :param _EndTime: 查询结束时间， 单位秒
        :type EndTime: int
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        """
        self._Limit = None
        self._BeginTime = None
        self._EndTime = None
        self._Cursor = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

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
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Cursor = params.get("Cursor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryArrivalListResponse(AbstractModel):
    """QueryArrivalList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextCursor: 分页游标，下次调用带上该值，则从当前的位置继续往后拉，以实现增量拉取。
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _PageData: 潜客客户存档信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of ArrivalInfo
        :param _HasMore: 是否还有更多数据。0-否；1-是。
注意：此字段可能返回 null，表示取不到有效值。
        :type HasMore: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextCursor = None
        self._PageData = None
        self._HasMore = None
        self._RequestId = None

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def HasMore(self):
        return self._HasMore

    @HasMore.setter
    def HasMore(self, HasMore):
        self._HasMore = HasMore

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = ArrivalInfo()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._HasMore = params.get("HasMore")
        self._RequestId = params.get("RequestId")


class QueryChannelCodeListRequest(AbstractModel):
    """QueryChannelCodeList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        :param _Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值
        :type Limit: int
        """
        self._Cursor = None
        self._Limit = None

    @property
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryChannelCodeListResponse(AbstractModel):
    """QueryChannelCodeList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _PageData: 活码列表响应参数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of ChannelCodeInnerDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextCursor = None
        self._PageData = None
        self._RequestId = None

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = ChannelCodeInnerDetail()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._RequestId = params.get("RequestId")


class QueryChatArchivingListRequest(AbstractModel):
    """QueryChatArchivingList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        :param _Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值
        :type Limit: int
        """
        self._Cursor = None
        self._Limit = None

    @property
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryChatArchivingListResponse(AbstractModel):
    """QueryChatArchivingList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _PageData: 会话存档列表响应参数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of ChatArchivingDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextCursor = None
        self._PageData = None
        self._RequestId = None

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = ChatArchivingDetail()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._RequestId = params.get("RequestId")


class QueryClueInfoListRequest(AbstractModel):
    """QueryClueInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        :param _Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值
        :type Limit: int
        :param _BeginTime: 查询开始时间， 单位秒
        :type BeginTime: int
        :param _EndTime: 查询结束时间， 单位秒
        :type EndTime: int
        """
        self._Cursor = None
        self._Limit = None
        self._BeginTime = None
        self._EndTime = None

    @property
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

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
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryClueInfoListResponse(AbstractModel):
    """QueryClueInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PageData: 线索信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of ClueInfoDetail
        :param _NextCursor: 分页游标，下次调用带上该值，则从当前的位置继续往后拉，以实现增量拉取。
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _HasMore: 是否还有更多数据。0-否；1-是。
注意：此字段可能返回 null，表示取不到有效值。
        :type HasMore: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PageData = None
        self._NextCursor = None
        self._HasMore = None
        self._RequestId = None

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def HasMore(self):
        return self._HasMore

    @HasMore.setter
    def HasMore(self, HasMore):
        self._HasMore = HasMore

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = ClueInfoDetail()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._NextCursor = params.get("NextCursor")
        self._HasMore = params.get("HasMore")
        self._RequestId = params.get("RequestId")


class QueryCrmStatisticsRequest(AbstractModel):
    """QueryCrmStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 查询开始时间， 单位秒
        :type BeginTime: int
        :param _EndTime: 查询结束时间， 单位秒
        :type EndTime: int
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        :param _Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值
        :type Limit: int
        :param _SalesId: 请求的企业成员id，为空时默认全租户
        :type SalesId: str
        :param _OrgId: 请求的部门id，为空时默认全租户
        :type OrgId: int
        """
        self._BeginTime = None
        self._EndTime = None
        self._Cursor = None
        self._Limit = None
        self._SalesId = None
        self._OrgId = None

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
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SalesId(self):
        return self._SalesId

    @SalesId.setter
    def SalesId(self, SalesId):
        self._SalesId = SalesId

    @property
    def OrgId(self):
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        self._SalesId = params.get("SalesId")
        self._OrgId = params.get("OrgId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCrmStatisticsResponse(AbstractModel):
    """QueryCrmStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _PageData: CRM统计响应数据
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of CrmStatisticsData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextCursor = None
        self._PageData = None
        self._RequestId = None

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = CrmStatisticsData()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._RequestId = params.get("RequestId")


class QueryCustomerEventDetailStatisticsRequest(AbstractModel):
    """QueryCustomerEventDetailStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 查询开始时间， 单位秒
        :type BeginTime: int
        :param _EndTime: 查询结束时间， 单位秒
        :type EndTime: int
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        :param _Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值
        :type Limit: int
        """
        self._BeginTime = None
        self._EndTime = None
        self._Cursor = None
        self._Limit = None

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
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCustomerEventDetailStatisticsResponse(AbstractModel):
    """QueryCustomerEventDetailStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _PageData: 外部联系人SaaS使用明细统计响应数据
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of CustomerActionEventDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextCursor = None
        self._PageData = None
        self._RequestId = None

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = CustomerActionEventDetail()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._RequestId = params.get("RequestId")


class QueryCustomerProfileListRequest(AbstractModel):
    """QueryCustomerProfileList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页，预期请求的数据量，取值范围 1 ~ 1000
        :type Limit: int
        :param _BeginTime: 查询开始时间， 单位秒
        :type BeginTime: int
        :param _EndTime: 查询结束时间， 单位秒
        :type EndTime: int
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        """
        self._Limit = None
        self._BeginTime = None
        self._EndTime = None
        self._Cursor = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

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
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Cursor = params.get("Cursor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCustomerProfileListResponse(AbstractModel):
    """QueryCustomerProfileList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextCursor: 分页游标，下次调用带上该值，则从当前的位置继续往后拉，以实现增量拉取。
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _PageData: 潜客客户存档信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of CustomerProfile
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextCursor = None
        self._PageData = None
        self._RequestId = None

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = CustomerProfile()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._RequestId = params.get("RequestId")


class QueryDealerInfoListRequest(AbstractModel):
    """QueryDealerInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        :param _Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值
        :type Limit: int
        """
        self._Cursor = None
        self._Limit = None

    @property
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryDealerInfoListResponse(AbstractModel):
    """QueryDealerInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PageData: 经销商信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of DealerInfo
        :param _NextCursor: 分页游标，下次调用带上该值，则从当前的位置继续往后拉取新增的数据，以实现增量拉取。
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _HasMore: 是否还有更多数据。0-否；1-是。
注意：此字段可能返回 null，表示取不到有效值。
        :type HasMore: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PageData = None
        self._NextCursor = None
        self._HasMore = None
        self._RequestId = None

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def HasMore(self):
        return self._HasMore

    @HasMore.setter
    def HasMore(self, HasMore):
        self._HasMore = HasMore

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = DealerInfo()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._NextCursor = params.get("NextCursor")
        self._HasMore = params.get("HasMore")
        self._RequestId = params.get("RequestId")


class QueryExternalContactDetailByDateRequest(AbstractModel):
    """QueryExternalContactDetailByDate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 查询结束时间， 单位秒
        :type BeginTime: int
        :param _EndTime: 查询结束时间， 单位秒
        :type EndTime: int
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        :param _Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值
        :type Limit: int
        """
        self._BeginTime = None
        self._EndTime = None
        self._Cursor = None
        self._Limit = None

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
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryExternalContactDetailByDateResponse(AbstractModel):
    """QueryExternalContactDetailByDate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _PageData: 外部联系人详细信息
        :type PageData: list of ExternalContactDetailPro
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextCursor = None
        self._PageData = None
        self._RequestId = None

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = ExternalContactDetailPro()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._RequestId = params.get("RequestId")


class QueryExternalContactDetailRequest(AbstractModel):
    """QueryExternalContactDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ExternalUserId: 外部联系人的userid，注意不是企业成员的账号
        :type ExternalUserId: str
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填。当客户在企业内的跟进人超过500人时需要使用cursor参数进行分页获取
        :type Cursor: str
        :param _Limit: 当前接口Limit不需要传参， 保留Limit只是为了保持向后兼容性， Limit默认值为500，当返回结果超过500时， NextCursor才有返回值
        :type Limit: int
        """
        self._ExternalUserId = None
        self._Cursor = None
        self._Limit = None

    @property
    def ExternalUserId(self):
        return self._ExternalUserId

    @ExternalUserId.setter
    def ExternalUserId(self, ExternalUserId):
        self._ExternalUserId = ExternalUserId

    @property
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ExternalUserId = params.get("ExternalUserId")
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryExternalContactDetailResponse(AbstractModel):
    """QueryExternalContactDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _Customer: 客户信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Customer: :class:`tencentcloud.wav.v20210129.models.ExternalContact`
        :param _FollowUser: 添加了此外部联系人的企业成员信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowUser: list of FollowUser
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextCursor = None
        self._Customer = None
        self._FollowUser = None
        self._RequestId = None

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def Customer(self):
        return self._Customer

    @Customer.setter
    def Customer(self, Customer):
        self._Customer = Customer

    @property
    def FollowUser(self):
        return self._FollowUser

    @FollowUser.setter
    def FollowUser(self, FollowUser):
        self._FollowUser = FollowUser

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextCursor = params.get("NextCursor")
        if params.get("Customer") is not None:
            self._Customer = ExternalContact()
            self._Customer._deserialize(params.get("Customer"))
        if params.get("FollowUser") is not None:
            self._FollowUser = []
            for item in params.get("FollowUser"):
                obj = FollowUser()
                obj._deserialize(item)
                self._FollowUser.append(obj)
        self._RequestId = params.get("RequestId")


class QueryExternalContactListRequest(AbstractModel):
    """QueryExternalContactList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        :param _Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值
        :type Limit: int
        """
        self._Cursor = None
        self._Limit = None

    @property
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryExternalContactListResponse(AbstractModel):
    """QueryExternalContactList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PageData: 外部联系人信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of ExternalContactSimpleInfo
        :param _NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PageData = None
        self._NextCursor = None
        self._RequestId = None

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = ExternalContactSimpleInfo()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._NextCursor = params.get("NextCursor")
        self._RequestId = params.get("RequestId")


class QueryExternalUserEventListRequest(AbstractModel):
    """QueryExternalUserEventList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 查询开始时间， 单位秒
        :type BeginTime: int
        :param _EndTime: 查询结束时间， 单位秒
        :type EndTime: int
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        :param _Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值
        :type Limit: int
        """
        self._BeginTime = None
        self._EndTime = None
        self._Cursor = None
        self._Limit = None

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
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryExternalUserEventListResponse(AbstractModel):
    """QueryExternalUserEventList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _PageData: 外部联系人事件信息响应数据
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of ExternalUserEventInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextCursor = None
        self._PageData = None
        self._RequestId = None

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = ExternalUserEventInfo()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._RequestId = params.get("RequestId")


class QueryExternalUserMappingInfoRequest(AbstractModel):
    """QueryExternalUserMappingInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpExternalUserIdList: 企业主体对应的外部联系人id列表，列表长度限制最大为50。
        :type CorpExternalUserIdList: list of str
        """
        self._CorpExternalUserIdList = None

    @property
    def CorpExternalUserIdList(self):
        return self._CorpExternalUserIdList

    @CorpExternalUserIdList.setter
    def CorpExternalUserIdList(self, CorpExternalUserIdList):
        self._CorpExternalUserIdList = CorpExternalUserIdList


    def _deserialize(self, params):
        self._CorpExternalUserIdList = params.get("CorpExternalUserIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryExternalUserMappingInfoResponse(AbstractModel):
    """QueryExternalUserMappingInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExternalUserIdMapping: 外部联系人映射信息, 只返回映射成功的记录
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalUserIdMapping: list of ExternalUserMappingInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExternalUserIdMapping = None
        self._RequestId = None

    @property
    def ExternalUserIdMapping(self):
        return self._ExternalUserIdMapping

    @ExternalUserIdMapping.setter
    def ExternalUserIdMapping(self, ExternalUserIdMapping):
        self._ExternalUserIdMapping = ExternalUserIdMapping

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ExternalUserIdMapping") is not None:
            self._ExternalUserIdMapping = []
            for item in params.get("ExternalUserIdMapping"):
                obj = ExternalUserMappingInfo()
                obj._deserialize(item)
                self._ExternalUserIdMapping.append(obj)
        self._RequestId = params.get("RequestId")


class QueryFollowListRequest(AbstractModel):
    """QueryFollowList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页，预期请求的数据量，取值范围 1 ~ 1000
        :type Limit: int
        :param _BeginTime: 查询开始时间， 单位秒
        :type BeginTime: int
        :param _EndTime: 查询结束时间， 单位秒
        :type EndTime: int
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        """
        self._Limit = None
        self._BeginTime = None
        self._EndTime = None
        self._Cursor = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

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
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Cursor = params.get("Cursor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFollowListResponse(AbstractModel):
    """QueryFollowList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextCursor: 分页游标，下次调用带上该值，则从当前的位置继续往后拉，以实现增量拉取。
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _PageData: 潜客客户存档信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of FollowInfo
        :param _HasMore: 是否还有更多数据。0-否；1-是。
注意：此字段可能返回 null，表示取不到有效值。
        :type HasMore: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextCursor = None
        self._PageData = None
        self._HasMore = None
        self._RequestId = None

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def HasMore(self):
        return self._HasMore

    @HasMore.setter
    def HasMore(self, HasMore):
        self._HasMore = HasMore

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = FollowInfo()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._HasMore = params.get("HasMore")
        self._RequestId = params.get("RequestId")


class QueryLicenseInfoRequest(AbstractModel):
    """QueryLicenseInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: license编号
        :type License: str
        """
        self._License = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License


    def _deserialize(self, params):
        self._License = params.get("License")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryLicenseInfoResponse(AbstractModel):
    """QueryLicenseInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LicenseInfo: license响应信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseInfo: :class:`tencentcloud.wav.v20210129.models.LicenseInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LicenseInfo = None
        self._RequestId = None

    @property
    def LicenseInfo(self):
        return self._LicenseInfo

    @LicenseInfo.setter
    def LicenseInfo(self, LicenseInfo):
        self._LicenseInfo = LicenseInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LicenseInfo") is not None:
            self._LicenseInfo = LicenseInfo()
            self._LicenseInfo._deserialize(params.get("LicenseInfo"))
        self._RequestId = params.get("RequestId")


class QueryMaterialListRequest(AbstractModel):
    """QueryMaterialList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MaterialType: 素材类型：0-图片，1-视频，3-文章，10-车型，11-名片
        :type MaterialType: int
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        :param _Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值
        :type Limit: int
        """
        self._MaterialType = None
        self._Cursor = None
        self._Limit = None

    @property
    def MaterialType(self):
        return self._MaterialType

    @MaterialType.setter
    def MaterialType(self, MaterialType):
        self._MaterialType = MaterialType

    @property
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._MaterialType = params.get("MaterialType")
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMaterialListResponse(AbstractModel):
    """QueryMaterialList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _PageData: 企业素材列表响应数据
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of MaterialInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextCursor = None
        self._PageData = None
        self._RequestId = None

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = MaterialInfo()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._RequestId = params.get("RequestId")


class QueryMiniAppCodeListRequest(AbstractModel):
    """QueryMiniAppCodeList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        :param _Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值
        :type Limit: int
        """
        self._Cursor = None
        self._Limit = None

    @property
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMiniAppCodeListResponse(AbstractModel):
    """QueryMiniAppCodeList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _PageData: 小程序码列表响应数据
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of MiniAppCodeInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextCursor = None
        self._PageData = None
        self._RequestId = None

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = MiniAppCodeInfo()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._RequestId = params.get("RequestId")


class QueryStaffEventDetailStatisticsRequest(AbstractModel):
    """QueryStaffEventDetailStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 查询开始时间， 单位秒
        :type BeginTime: int
        :param _EndTime: 查询结束时间， 单位秒
        :type EndTime: int
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        :param _Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值
        :type Limit: int
        """
        self._BeginTime = None
        self._EndTime = None
        self._Cursor = None
        self._Limit = None

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
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryStaffEventDetailStatisticsResponse(AbstractModel):
    """QueryStaffEventDetailStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _PageData: 企业成员SaaS使用明细统计响应数据
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of SalesActionEventDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextCursor = None
        self._PageData = None
        self._RequestId = None

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = SalesActionEventDetail()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._RequestId = params.get("RequestId")


class QueryUserInfoListRequest(AbstractModel):
    """QueryUserInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        :param _Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值
        :type Limit: int
        """
        self._Cursor = None
        self._Limit = None

    @property
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryUserInfoListResponse(AbstractModel):
    """QueryUserInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _PageData: 企业成员信息列表响应数据
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of CorpUserInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextCursor = None
        self._PageData = None
        self._RequestId = None

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = CorpUserInfo()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._RequestId = params.get("RequestId")


class QueryVehicleInfoListRequest(AbstractModel):
    """QueryVehicleInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        :param _Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值
        :type Limit: int
        """
        self._Cursor = None
        self._Limit = None

    @property
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Cursor = params.get("Cursor")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryVehicleInfoListResponse(AbstractModel):
    """QueryVehicleInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PageData: 车系车型信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of VehicleInfo
        :param _NextCursor: 分页游标，下次调用带上该值，则从当前的位置继续往后拉取新增的数据，以实现增量拉取。
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param _HasMore: 是否还有更多数据。0-否；1-是。
注意：此字段可能返回 null，表示取不到有效值。
        :type HasMore: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PageData = None
        self._NextCursor = None
        self._HasMore = None
        self._RequestId = None

    @property
    def PageData(self):
        return self._PageData

    @PageData.setter
    def PageData(self, PageData):
        self._PageData = PageData

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def HasMore(self):
        return self._HasMore

    @HasMore.setter
    def HasMore(self, HasMore):
        self._HasMore = HasMore

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PageData") is not None:
            self._PageData = []
            for item in params.get("PageData"):
                obj = VehicleInfo()
                obj._deserialize(item)
                self._PageData.append(obj)
        self._NextCursor = params.get("NextCursor")
        self._HasMore = params.get("HasMore")
        self._RequestId = params.get("RequestId")


class SalesActionEventDetail(AbstractModel):
    """企业成员SaaS使用明细数据

    """

    def __init__(self):
        r"""
        :param _EventCode: 事件码
        :type EventCode: str
        :param _EventType: 事件类型
        :type EventType: int
        :param _EventSource: 事件来源
        :type EventSource: int
        :param _SalesId: 销售顾问id
        :type SalesId: int
        :param _MaterialType: 素材类型
        :type MaterialType: int
        :param _MaterialId: 素材编号id
        :type MaterialId: int
        :param _EventTime: 事件上报时间，单位：秒
        :type EventTime: int
        """
        self._EventCode = None
        self._EventType = None
        self._EventSource = None
        self._SalesId = None
        self._MaterialType = None
        self._MaterialId = None
        self._EventTime = None

    @property
    def EventCode(self):
        return self._EventCode

    @EventCode.setter
    def EventCode(self, EventCode):
        self._EventCode = EventCode

    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def EventSource(self):
        return self._EventSource

    @EventSource.setter
    def EventSource(self, EventSource):
        self._EventSource = EventSource

    @property
    def SalesId(self):
        return self._SalesId

    @SalesId.setter
    def SalesId(self, SalesId):
        self._SalesId = SalesId

    @property
    def MaterialType(self):
        return self._MaterialType

    @MaterialType.setter
    def MaterialType(self, MaterialType):
        self._MaterialType = MaterialType

    @property
    def MaterialId(self):
        return self._MaterialId

    @MaterialId.setter
    def MaterialId(self, MaterialId):
        self._MaterialId = MaterialId

    @property
    def EventTime(self):
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime


    def _deserialize(self, params):
        self._EventCode = params.get("EventCode")
        self._EventType = params.get("EventType")
        self._EventSource = params.get("EventSource")
        self._SalesId = params.get("SalesId")
        self._MaterialType = params.get("MaterialType")
        self._MaterialId = params.get("MaterialId")
        self._EventTime = params.get("EventTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagDetailInfo(AbstractModel):
    """标签详细信息

    """

    def __init__(self):
        r"""
        :param _TagName: 标签名称
        :type TagName: str
        :param _BizTagId: 标签业务ID
        :type BizTagId: str
        :param _TagId: 企微标签ID
        :type TagId: str
        :param _Sort: 标签排序的次序值，sort值大的排序靠前。有效的值范围是[0, 2^32)
        :type Sort: int
        :param _CreateTime: 标签创建时间,单位为秒
        :type CreateTime: int
        """
        self._TagName = None
        self._BizTagId = None
        self._TagId = None
        self._Sort = None
        self._CreateTime = None

    @property
    def TagName(self):
        return self._TagName

    @TagName.setter
    def TagName(self, TagName):
        self._TagName = TagName

    @property
    def BizTagId(self):
        return self._BizTagId

    @BizTagId.setter
    def BizTagId(self, BizTagId):
        self._BizTagId = BizTagId

    @property
    def TagId(self):
        return self._TagId

    @TagId.setter
    def TagId(self, TagId):
        self._TagId = TagId

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._TagName = params.get("TagName")
        self._BizTagId = params.get("BizTagId")
        self._TagId = params.get("TagId")
        self._Sort = params.get("Sort")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagGroup(AbstractModel):
    """标签组信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 企微标签组id
        :type GroupId: str
        :param _BizGroupId: 标签组业务id
        :type BizGroupId: str
        :param _GroupName: 企微标签组名称，不能超过15个字符
        :type GroupName: str
        :param _Sort: 标签组次序值。sort值大的排序靠前。有效的值范围是[0, 2^32)
        :type Sort: int
        :param _CreateTime: 标签组创建时间,单位为秒
        :type CreateTime: int
        :param _Tags: 标签组内的标签列表, 上限为20
        :type Tags: list of TagDetailInfo
        """
        self._GroupId = None
        self._BizGroupId = None
        self._GroupName = None
        self._Sort = None
        self._CreateTime = None
        self._Tags = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def BizGroupId(self):
        return self._BizGroupId

    @BizGroupId.setter
    def BizGroupId(self, BizGroupId):
        self._BizGroupId = BizGroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._BizGroupId = params.get("BizGroupId")
        self._GroupName = params.get("GroupName")
        self._Sort = params.get("Sort")
        self._CreateTime = params.get("CreateTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagDetailInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """标签信息

    """

    def __init__(self):
        r"""
        :param _TagName: 标签名称, 最大长度限制15个字符
        :type TagName: str
        :param _Sort: 标签组排序,值越大,排序越靠前
        :type Sort: int
        """
        self._TagName = None
        self._Sort = None

    @property
    def TagName(self):
        return self._TagName

    @TagName.setter
    def TagName(self, TagName):
        self._TagName = TagName

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._TagName = params.get("TagName")
        self._Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VehicleInfo(AbstractModel):
    """车型车系信息

    """

    def __init__(self):
        r"""
        :param _BrandId: 品牌id
        :type BrandId: int
        :param _BrandName: 品牌名称
        :type BrandName: str
        :param _SeriesId: 车系id
        :type SeriesId: int
        :param _SeriesName: 车系名称
        :type SeriesName: str
        :param _ModelId: 车型id
        :type ModelId: int
        :param _ModelName: 车型名称
        :type ModelName: str
        """
        self._BrandId = None
        self._BrandName = None
        self._SeriesId = None
        self._SeriesName = None
        self._ModelId = None
        self._ModelName = None

    @property
    def BrandId(self):
        return self._BrandId

    @BrandId.setter
    def BrandId(self, BrandId):
        self._BrandId = BrandId

    @property
    def BrandName(self):
        return self._BrandName

    @BrandName.setter
    def BrandName(self, BrandName):
        self._BrandName = BrandName

    @property
    def SeriesId(self):
        return self._SeriesId

    @SeriesId.setter
    def SeriesId(self, SeriesId):
        self._SeriesId = SeriesId

    @property
    def SeriesName(self):
        return self._SeriesName

    @SeriesName.setter
    def SeriesName(self, SeriesName):
        self._SeriesName = SeriesName

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelName(self):
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName


    def _deserialize(self, params):
        self._BrandId = params.get("BrandId")
        self._BrandName = params.get("BrandName")
        self._SeriesId = params.get("SeriesId")
        self._SeriesName = params.get("SeriesName")
        self._ModelId = params.get("ModelId")
        self._ModelName = params.get("ModelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VehiclePurpose(AbstractModel):
    """购车用途详细信息

    """

    def __init__(self):
        r"""
        :param _VehiclePurposeCode: 购车用途code
        :type VehiclePurposeCode: str
        :param _VehiclePurposeName: 购车用途名称
        :type VehiclePurposeName: str
        """
        self._VehiclePurposeCode = None
        self._VehiclePurposeName = None

    @property
    def VehiclePurposeCode(self):
        return self._VehiclePurposeCode

    @VehiclePurposeCode.setter
    def VehiclePurposeCode(self, VehiclePurposeCode):
        self._VehiclePurposeCode = VehiclePurposeCode

    @property
    def VehiclePurposeName(self):
        return self._VehiclePurposeName

    @VehiclePurposeName.setter
    def VehiclePurposeName(self, VehiclePurposeName):
        self._VehiclePurposeName = VehiclePurposeName


    def _deserialize(self, params):
        self._VehiclePurposeCode = params.get("VehiclePurposeCode")
        self._VehiclePurposeName = params.get("VehiclePurposeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeComTagDetail(AbstractModel):
    """企微个人标签信息,渠道活码使用

    """

    def __init__(self):
        r"""
        :param _GroupName: 标签分组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _BizGroupId: 标签分组业务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BizGroupId: str
        :param _TagName: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TagName: str
        :param _TagId: 标签ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TagId: str
        :param _BizTagId: 标签业务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BizTagId: str
        :param _Type: 标签分类，1：企业设置、2：用户自定义
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _BizTagIdStr: 标签业务ID字符串格式
注意：此字段可能返回 null，表示取不到有效值。
        :type BizTagIdStr: str
        """
        self._GroupName = None
        self._BizGroupId = None
        self._TagName = None
        self._TagId = None
        self._BizTagId = None
        self._Type = None
        self._BizTagIdStr = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def BizGroupId(self):
        return self._BizGroupId

    @BizGroupId.setter
    def BizGroupId(self, BizGroupId):
        self._BizGroupId = BizGroupId

    @property
    def TagName(self):
        return self._TagName

    @TagName.setter
    def TagName(self, TagName):
        self._TagName = TagName

    @property
    def TagId(self):
        return self._TagId

    @TagId.setter
    def TagId(self, TagId):
        self._TagId = TagId

    @property
    def BizTagId(self):
        return self._BizTagId

    @BizTagId.setter
    def BizTagId(self, BizTagId):
        self._BizTagId = BizTagId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def BizTagIdStr(self):
        return self._BizTagIdStr

    @BizTagIdStr.setter
    def BizTagIdStr(self, BizTagIdStr):
        self._BizTagIdStr = BizTagIdStr


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._BizGroupId = params.get("BizGroupId")
        self._TagName = params.get("TagName")
        self._TagId = params.get("TagId")
        self._BizTagId = params.get("BizTagId")
        self._Type = params.get("Type")
        self._BizTagIdStr = params.get("BizTagIdStr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        