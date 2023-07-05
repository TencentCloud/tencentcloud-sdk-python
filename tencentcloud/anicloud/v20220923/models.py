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


class CheckAppidExistRequest(AbstractModel):
    """CheckAppidExist请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SDKAppid: 业务的appid
        :type SDKAppid: str
        :param _Type: sub product code
        :type Type: str
        """
        self._SDKAppid = None
        self._Type = None

    @property
    def SDKAppid(self):
        return self._SDKAppid

    @SDKAppid.setter
    def SDKAppid(self, SDKAppid):
        self._SDKAppid = SDKAppid

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._SDKAppid = params.get("SDKAppid")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAppidExistResponse(AbstractModel):
    """CheckAppidExist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Exist: appid是否存在
        :type Exist: bool
        :param _HasError: 请求是否成功
        :type HasError: bool
        :param _Msg: 出错消息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Exist = None
        self._HasError = None
        self._Msg = None
        self._RequestId = None

    @property
    def Exist(self):
        return self._Exist

    @Exist.setter
    def Exist(self, Exist):
        self._Exist = Exist

    @property
    def HasError(self):
        return self._HasError

    @HasError.setter
    def HasError(self, HasError):
        self._HasError = HasError

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Exist = params.get("Exist")
        self._HasError = params.get("HasError")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class GoodsDetail(AbstractModel):
    """购买详情

    """

    def __init__(self):
        r"""
        :param _ProductCode: 按照四层接入的产品需要传入产品标签,例如:p_cvm
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCode: str
        :param _SubProductCode: 四层定义的子产品标签,例如:sp_cvm_s1
注意：此字段可能返回 null，表示取不到有效值。
        :type SubProductCode: str
        :param _Type: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: list of str
        :param _GoodsNum: 资源数量
注意：此字段可能返回 null，表示取不到有效值。
        :type GoodsNum: int
        """
        self._ProductCode = None
        self._SubProductCode = None
        self._Type = None
        self._GoodsNum = None

    @property
    def ProductCode(self):
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def SubProductCode(self):
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum


    def _deserialize(self, params):
        self._ProductCode = params.get("ProductCode")
        self._SubProductCode = params.get("SubProductCode")
        self._Type = params.get("Type")
        self._GoodsNum = params.get("GoodsNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryResourceInfoRequest(AbstractModel):
    """QueryResourceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryResourceInfoResponse(AbstractModel):
    """QueryResourceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Resource: 资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: :class:`tencentcloud.anicloud.v20220923.models.Resource`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Resource = None
        self._RequestId = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Resource") is not None:
            self._Resource = Resource()
            self._Resource._deserialize(params.get("Resource"))
        self._RequestId = params.get("RequestId")


class QueryResourceRequest(AbstractModel):
    """QueryResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 0: sdk 1:material
        :type Type: int
        :param _PageNumber: 分页起始页
        :type PageNumber: int
        :param _PageSize: 分页大小
        :type PageSize: int
        """
        self._Type = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

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
        self._Type = params.get("Type")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryResourceResponse(AbstractModel):
    """QueryResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Resources: 资源信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Resources: list of Resource
        :param _Total: 总量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Resources = None
        self._Total = None
        self._RequestId = None

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self._Resources.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class Resource(AbstractModel):
    """资源信息

    """

    def __init__(self):
        r"""
        :param _UIN: 资源拥有者
注意：此字段可能返回 null，表示取不到有效值。
        :type UIN: str
        :param _AppId: 云平台应用ID，一般来说与uin存在一一对应的关系
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _ResourceId: 资源id，会展示到通知内容
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _ZoneId: 区域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _Status: 资源状态，1正常，2隔离，3销毁(如果资源已经删除或销毁，不需要返回)，4冻结/封禁
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _IsolatedTimestamp: 资源隔离时间，未隔离传"0000-00-00 00:00:00"，资源由隔离变回正常传"0000-00-00 00:00:00"
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedTimestamp: str
        :param _CreateTime: 资源创建时间，用于更新新购订单的资源开始时间，按时长退费时的资源结束时间取自订单的资源结束时间，
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _PayMode: 0后付费 1预付费 2预留实例
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: int
        :param _Alias: 资源名称，账单中资源别名，生命周期通知中的资源名称，不返回则通知中展示为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param _GoodsDetail: 购买详情
注意：此字段可能返回 null，表示取不到有效值。
        :type GoodsDetail: :class:`tencentcloud.anicloud.v20220923.models.GoodsDetail`
        :param _RenewFlag: 预付费必填 ，自动续费标记，0表示默认状态(用户未设置，即初始状态即手动续费，用户开通了预付费不停服特权也会进行自动续费)， 1表示自动续费，2表示明确不自动续费(用户设置)，若业务无续费概念或无需自动续费，需要设置为0
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param _ExpireTime: （仅预付费）资源到期时间，无到期概念传"0000-00-00 00:00:00"
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _Region: 地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: int
        :param _SdkAppId: sdk appid
注意：此字段可能返回 null，表示取不到有效值。
        :type SdkAppId: str
        :param _AppName: app名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AppName: str
        :param _PackageName: app的package名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param _URL: 资源链接
注意：此字段可能返回 null，表示取不到有效值。
        :type URL: str
        :param _Entry: app的entry
注意：此字段可能返回 null，表示取不到有效值。
        :type Entry: str
        :param _InstType: 0：sdk 1：素材
注意：此字段可能返回 null，表示取不到有效值。
        :type InstType: int
        :param _Key: license的秘钥
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        """
        self._UIN = None
        self._AppId = None
        self._ResourceId = None
        self._ZoneId = None
        self._Status = None
        self._IsolatedTimestamp = None
        self._CreateTime = None
        self._PayMode = None
        self._Alias = None
        self._GoodsDetail = None
        self._RenewFlag = None
        self._ExpireTime = None
        self._Region = None
        self._SdkAppId = None
        self._AppName = None
        self._PackageName = None
        self._URL = None
        self._Entry = None
        self._InstType = None
        self._Key = None

    @property
    def UIN(self):
        return self._UIN

    @UIN.setter
    def UIN(self, UIN):
        self._UIN = UIN

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsolatedTimestamp(self):
        return self._IsolatedTimestamp

    @IsolatedTimestamp.setter
    def IsolatedTimestamp(self, IsolatedTimestamp):
        self._IsolatedTimestamp = IsolatedTimestamp

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def GoodsDetail(self):
        return self._GoodsDetail

    @GoodsDetail.setter
    def GoodsDetail(self, GoodsDetail):
        self._GoodsDetail = GoodsDetail

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def URL(self):
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def Entry(self):
        return self._Entry

    @Entry.setter
    def Entry(self, Entry):
        self._Entry = Entry

    @property
    def InstType(self):
        return self._InstType

    @InstType.setter
    def InstType(self, InstType):
        self._InstType = InstType

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key


    def _deserialize(self, params):
        self._UIN = params.get("UIN")
        self._AppId = params.get("AppId")
        self._ResourceId = params.get("ResourceId")
        self._ZoneId = params.get("ZoneId")
        self._Status = params.get("Status")
        self._IsolatedTimestamp = params.get("IsolatedTimestamp")
        self._CreateTime = params.get("CreateTime")
        self._PayMode = params.get("PayMode")
        self._Alias = params.get("Alias")
        if params.get("GoodsDetail") is not None:
            self._GoodsDetail = GoodsDetail()
            self._GoodsDetail._deserialize(params.get("GoodsDetail"))
        self._RenewFlag = params.get("RenewFlag")
        self._ExpireTime = params.get("ExpireTime")
        self._Region = params.get("Region")
        self._SdkAppId = params.get("SdkAppId")
        self._AppName = params.get("AppName")
        self._PackageName = params.get("PackageName")
        self._URL = params.get("URL")
        self._Entry = params.get("Entry")
        self._InstType = params.get("InstType")
        self._Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        