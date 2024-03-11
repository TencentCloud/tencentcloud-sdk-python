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


class GetIndustryV1HomeMembersReqPayload(AbstractModel):
    """获取成员列表入参payload

    """

    def __init__(self):
        r"""
        :param _ID: 用户ID
        :type ID: str
        """
        self._ID = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetIndustryV1HomeMembersRequest(AbstractModel):
    """GetIndustryV1HomeMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Payload: 无
        :type Payload: :class:`tencentcloud.icr.v20211014.models.GetIndustryV1HomeMembersReqPayload`
        :param _Metadata: 无
        :type Metadata: :class:`tencentcloud.icr.v20211014.models.ReqMetadata`
        """
        self._Payload = None
        self._Metadata = None

    @property
    def Payload(self):
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def Metadata(self):
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata


    def _deserialize(self, params):
        if params.get("Payload") is not None:
            self._Payload = GetIndustryV1HomeMembersReqPayload()
            self._Payload._deserialize(params.get("Payload"))
        if params.get("Metadata") is not None:
            self._Metadata = ReqMetadata()
            self._Metadata._deserialize(params.get("Metadata"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetIndustryV1HomeMembersRespData(AbstractModel):
    """获取成员列表回包DataList

    """

    def __init__(self):
        r"""
        :param _EditTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EditTime: int
        :param _FeatureList: 功能列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FeatureList: :class:`tencentcloud.icr.v20211014.models.GetIndustryV1HomeMembersRespFeature`
        :param _ID: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        :param _IndustryType: 用户行业分类
注意：此字段可能返回 null，表示取不到有效值。
        :type IndustryType: str
        :param _MemberNum: 子用户数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberNum: int
        :param _ProductList: 机器人列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductList: :class:`tencentcloud.icr.v20211014.models.GetIndustryV1HomeMembersRespProduct`
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _Status: 是否有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _TypeList: 功能列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeList: :class:`tencentcloud.icr.v20211014.models.GetIndustryV1HomeMembersRespType`
        :param _UserAccount: 用户账号
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAccount: str
        """
        self._EditTime = None
        self._FeatureList = None
        self._ID = None
        self._IndustryType = None
        self._MemberNum = None
        self._ProductList = None
        self._Remark = None
        self._Status = None
        self._TypeList = None
        self._UserAccount = None

    @property
    def EditTime(self):
        return self._EditTime

    @EditTime.setter
    def EditTime(self, EditTime):
        self._EditTime = EditTime

    @property
    def FeatureList(self):
        return self._FeatureList

    @FeatureList.setter
    def FeatureList(self, FeatureList):
        self._FeatureList = FeatureList

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def IndustryType(self):
        return self._IndustryType

    @IndustryType.setter
    def IndustryType(self, IndustryType):
        self._IndustryType = IndustryType

    @property
    def MemberNum(self):
        return self._MemberNum

    @MemberNum.setter
    def MemberNum(self, MemberNum):
        self._MemberNum = MemberNum

    @property
    def ProductList(self):
        return self._ProductList

    @ProductList.setter
    def ProductList(self, ProductList):
        self._ProductList = ProductList

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TypeList(self):
        return self._TypeList

    @TypeList.setter
    def TypeList(self, TypeList):
        self._TypeList = TypeList

    @property
    def UserAccount(self):
        return self._UserAccount

    @UserAccount.setter
    def UserAccount(self, UserAccount):
        self._UserAccount = UserAccount


    def _deserialize(self, params):
        self._EditTime = params.get("EditTime")
        if params.get("FeatureList") is not None:
            self._FeatureList = GetIndustryV1HomeMembersRespFeature()
            self._FeatureList._deserialize(params.get("FeatureList"))
        self._ID = params.get("ID")
        self._IndustryType = params.get("IndustryType")
        self._MemberNum = params.get("MemberNum")
        if params.get("ProductList") is not None:
            self._ProductList = GetIndustryV1HomeMembersRespProduct()
            self._ProductList._deserialize(params.get("ProductList"))
        self._Remark = params.get("Remark")
        self._Status = params.get("Status")
        if params.get("TypeList") is not None:
            self._TypeList = GetIndustryV1HomeMembersRespType()
            self._TypeList._deserialize(params.get("TypeList"))
        self._UserAccount = params.get("UserAccount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetIndustryV1HomeMembersRespFeature(AbstractModel):
    """获取成员列表接口回包Feature

    """

    def __init__(self):
        r"""
        :param _FeatureName: 功能名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FeatureName: str
        :param _ID: 功能ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        """
        self._FeatureName = None
        self._ID = None

    @property
    def FeatureName(self):
        return self._FeatureName

    @FeatureName.setter
    def FeatureName(self, FeatureName):
        self._FeatureName = FeatureName

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._FeatureName = params.get("FeatureName")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetIndustryV1HomeMembersRespIndustry(AbstractModel):
    """获取成员列表回包Industry

    """

    def __init__(self):
        r"""
        :param _ID: 行业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        :param _IndustryName: 行业名称
注意：此字段可能返回 null，表示取不到有效值。
        :type IndustryName: str
        """
        self._ID = None
        self._IndustryName = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def IndustryName(self):
        return self._IndustryName

    @IndustryName.setter
    def IndustryName(self, IndustryName):
        self._IndustryName = IndustryName


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._IndustryName = params.get("IndustryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetIndustryV1HomeMembersRespPayload(AbstractModel):
    """获取成员列表回包Payload

    """

    def __init__(self):
        r"""
        :param _AccountLevel: 用户级别
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountLevel: str
        :param _DataList: 用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DataList: list of GetIndustryV1HomeMembersRespData
        :param _Limit: 每页数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Limit: int
        :param _Offset: 分页偏移量，从0开始
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: int
        :param _Total: 用户总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        """
        self._AccountLevel = None
        self._DataList = None
        self._Limit = None
        self._Offset = None
        self._Total = None

    @property
    def AccountLevel(self):
        return self._AccountLevel

    @AccountLevel.setter
    def AccountLevel(self, AccountLevel):
        self._AccountLevel = AccountLevel

    @property
    def DataList(self):
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._AccountLevel = params.get("AccountLevel")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = GetIndustryV1HomeMembersRespData()
                obj._deserialize(item)
                self._DataList.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetIndustryV1HomeMembersRespProduct(AbstractModel):
    """获取成员列表接口回包ProductList

    """

    def __init__(self):
        r"""
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _EditTime: 编辑时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EditTime: str
        :param _AppKey: 机器人ID（AppKey信息）
注意：此字段可能返回 null，表示取不到有效值。
        :type AppKey: str
        :param _Image: 机器人图标
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: str
        :param _Industry: 行业信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Industry: list of GetIndustryV1HomeMembersRespIndustry
        :param _OperatorList: 操作员列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorList: str
        :param _ProductName: 机器人名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _TemplateList: 模板列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateList: str
        """
        self._CreateTime = None
        self._EditTime = None
        self._AppKey = None
        self._Image = None
        self._Industry = None
        self._OperatorList = None
        self._ProductName = None
        self._Remark = None
        self._TemplateList = None

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EditTime(self):
        return self._EditTime

    @EditTime.setter
    def EditTime(self, EditTime):
        self._EditTime = EditTime

    @property
    def AppKey(self):
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Industry(self):
        return self._Industry

    @Industry.setter
    def Industry(self, Industry):
        self._Industry = Industry

    @property
    def OperatorList(self):
        return self._OperatorList

    @OperatorList.setter
    def OperatorList(self, OperatorList):
        self._OperatorList = OperatorList

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TemplateList(self):
        return self._TemplateList

    @TemplateList.setter
    def TemplateList(self, TemplateList):
        self._TemplateList = TemplateList


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._EditTime = params.get("EditTime")
        self._AppKey = params.get("AppKey")
        self._Image = params.get("Image")
        if params.get("Industry") is not None:
            self._Industry = []
            for item in params.get("Industry"):
                obj = GetIndustryV1HomeMembersRespIndustry()
                obj._deserialize(item)
                self._Industry.append(obj)
        self._OperatorList = params.get("OperatorList")
        self._ProductName = params.get("ProductName")
        self._Remark = params.get("Remark")
        self._TemplateList = params.get("TemplateList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetIndustryV1HomeMembersRespType(AbstractModel):
    """获取成员列表接口回包TypeList

    """

    def __init__(self):
        r"""
        :param _Type: 类型ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _TypeName: 类型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeName: str
        """
        self._Type = None
        self._TypeName = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TypeName(self):
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._TypeName = params.get("TypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetIndustryV1HomeMembersResponse(AbstractModel):
    """GetIndustryV1HomeMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Metadata: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Metadata: :class:`tencentcloud.icr.v20211014.models.RspMetadata`
        :param _Payload: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Payload: :class:`tencentcloud.icr.v20211014.models.GetIndustryV1HomeMembersRespPayload`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Metadata = None
        self._Payload = None
        self._RequestId = None

    @property
    def Metadata(self):
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def Payload(self):
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Metadata") is not None:
            self._Metadata = RspMetadata()
            self._Metadata._deserialize(params.get("Metadata"))
        if params.get("Payload") is not None:
            self._Payload = GetIndustryV1HomeMembersRespPayload()
            self._Payload._deserialize(params.get("Payload"))
        self._RequestId = params.get("RequestId")


class ReqMetadata(AbstractModel):
    """请求的Metadata

    """

    def __init__(self):
        r"""
        :param _ChannelID: 渠道
        :type ChannelID: str
        :param _BusinessName: 无
        :type BusinessName: str
        :param _GUID: 无
        :type GUID: str
        :param _AppKey: 无
        :type AppKey: str
        :param _LBS: 位置定位服务
        :type LBS: :class:`tencentcloud.icr.v20211014.models.ReqMetadataLBS`
        :param _Vagrants: 透传字段
        :type Vagrants: list of ReqMetadataVagrant
        """
        self._ChannelID = None
        self._BusinessName = None
        self._GUID = None
        self._AppKey = None
        self._LBS = None
        self._Vagrants = None

    @property
    def ChannelID(self):
        return self._ChannelID

    @ChannelID.setter
    def ChannelID(self, ChannelID):
        self._ChannelID = ChannelID

    @property
    def BusinessName(self):
        return self._BusinessName

    @BusinessName.setter
    def BusinessName(self, BusinessName):
        self._BusinessName = BusinessName

    @property
    def GUID(self):
        return self._GUID

    @GUID.setter
    def GUID(self, GUID):
        self._GUID = GUID

    @property
    def AppKey(self):
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def LBS(self):
        return self._LBS

    @LBS.setter
    def LBS(self, LBS):
        self._LBS = LBS

    @property
    def Vagrants(self):
        return self._Vagrants

    @Vagrants.setter
    def Vagrants(self, Vagrants):
        self._Vagrants = Vagrants


    def _deserialize(self, params):
        self._ChannelID = params.get("ChannelID")
        self._BusinessName = params.get("BusinessName")
        self._GUID = params.get("GUID")
        self._AppKey = params.get("AppKey")
        if params.get("LBS") is not None:
            self._LBS = ReqMetadataLBS()
            self._LBS._deserialize(params.get("LBS"))
        if params.get("Vagrants") is not None:
            self._Vagrants = []
            for item in params.get("Vagrants"):
                obj = ReqMetadataVagrant()
                obj._deserialize(item)
                self._Vagrants.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReqMetadataLBS(AbstractModel):
    """请求参数的lbs

    """

    def __init__(self):
        r"""
        :param _Latitude: 纬度
        :type Latitude: float
        :param _Longitude: 经度
        :type Longitude: float
        """
        self._Latitude = None
        self._Longitude = None

    @property
    def Latitude(self):
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude

    @property
    def Longitude(self):
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude


    def _deserialize(self, params):
        self._Latitude = params.get("Latitude")
        self._Longitude = params.get("Longitude")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReqMetadataVagrant(AbstractModel):
    """请求参数Vagrant

    """

    def __init__(self):
        r"""
        :param _Key: 无
        :type Key: str
        :param _Value: 无
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RspMetadata(AbstractModel):
    """回包的meta data

    """

    def __init__(self):
        r"""
        :param _Code: 无
        :type Code: int
        :param _Message: 无
        :type Message: str
        :param _SessionID: 无
        :type SessionID: str
        :param _SessionDelta: 无
        :type SessionDelta: str
        """
        self._Code = None
        self._Message = None
        self._SessionID = None
        self._SessionDelta = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def SessionID(self):
        return self._SessionID

    @SessionID.setter
    def SessionID(self, SessionID):
        self._SessionID = SessionID

    @property
    def SessionDelta(self):
        return self._SessionDelta

    @SessionDelta.setter
    def SessionDelta(self, SessionDelta):
        self._SessionDelta = SessionDelta


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._SessionID = params.get("SessionID")
        self._SessionDelta = params.get("SessionDelta")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        