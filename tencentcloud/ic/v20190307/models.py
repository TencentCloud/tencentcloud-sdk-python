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


class AppInfo(AbstractModel):
    r"""物联网卡应用信息详情

    """

    def __init__(self):
        r"""
        :param _Sdkappid: 应用ID
        :type Sdkappid: str
        :param _Appkey: 应用key
        :type Appkey: str
        :param _CloudAppid: 用户appid
        :type CloudAppid: str
        :param _Name: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: 应用描述
        :type Description: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _BizType: 应用类型
        :type BizType: int
        :param _Uin: 用户Uin
        :type Uin: str
        """
        self._Sdkappid = None
        self._Appkey = None
        self._CloudAppid = None
        self._Name = None
        self._Description = None
        self._CreatedTime = None
        self._BizType = None
        self._Uin = None

    @property
    def Sdkappid(self):
        r"""应用ID
        :rtype: str
        """
        return self._Sdkappid

    @Sdkappid.setter
    def Sdkappid(self, Sdkappid):
        self._Sdkappid = Sdkappid

    @property
    def Appkey(self):
        r"""应用key
        :rtype: str
        """
        return self._Appkey

    @Appkey.setter
    def Appkey(self, Appkey):
        self._Appkey = Appkey

    @property
    def CloudAppid(self):
        r"""用户appid
        :rtype: str
        """
        return self._CloudAppid

    @CloudAppid.setter
    def CloudAppid(self, CloudAppid):
        self._CloudAppid = CloudAppid

    @property
    def Name(self):
        r"""应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""应用描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreatedTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def BizType(self):
        r"""应用类型
        :rtype: int
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Uin(self):
        r"""用户Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin


    def _deserialize(self, params):
        self._Sdkappid = params.get("Sdkappid")
        self._Appkey = params.get("Appkey")
        self._CloudAppid = params.get("CloudAppid")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._CreatedTime = params.get("CreatedTime")
        self._BizType = params.get("BizType")
        self._Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CardInfo(AbstractModel):
    r"""卡片详细信息

    """

    def __init__(self):
        r"""
        :param _Iccid: 卡片ID
        :type Iccid: str
        :param _Msisdn: 卡电话号码
注意：此字段可能返回 null，表示取不到有效值。
        :type Msisdn: str
        :param _Imsi: 卡imsi
注意：此字段可能返回 null，表示取不到有效值。
        :type Imsi: str
        :param _Imei: 卡imei
注意：此字段可能返回 null，表示取不到有效值。
        :type Imei: str
        :param _Sdkappid: 应用ID
        :type Sdkappid: str
        :param _Teleoperator: 运营商编号
        :type Teleoperator: int
        :param _CardStatus: 卡片状态 1:未激活 2：激活 3：停卡 5：销卡
        :type CardStatus: int
        :param _NetworkStatus: 网络状态
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkStatus: int
        :param _ActivitedTime: 激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivitedTime: str
        :param _Type: 资费类型，1 单卡，2 流量池
        :type Type: int
        :param _ProductId: 套餐类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _PoolId: 流量池ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PoolId: str
        :param _DataUsedInPeriod: 周期套餐流量使用
注意：此字段可能返回 null，表示取不到有效值。
        :type DataUsedInPeriod: float
        :param _DataTotalInPeriod: 周期套餐总量
注意：此字段可能返回 null，表示取不到有效值。
        :type DataTotalInPeriod: float
        :param _ProductExpiredTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductExpiredTime: str
        :param _Description: 描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _ModifiedTime: 修改时间
        :type ModifiedTime: str
        :param _PreorderCnt: 套餐周期
注意：此字段可能返回 null，表示取不到有效值。
        :type PreorderCnt: int
        :param _IsActivated: 激活被回调标志
注意：此字段可能返回 null，表示取不到有效值。
        :type IsActivated: int
        :param _OrderId: 订单ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param _AutoRenew: 是否自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenew: int
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _AllowArrears: 0 不需要开通达量不停卡 1 需要开通达量不停卡
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowArrears: int
        :param _NeedSms: 是否开通短信0:未开短信 1:开通短信
        :type NeedSms: int
        :param _Provider: 供应商
        :type Provider: int
        :param _CertificationState: 实名认证 0:无 1:未实名 2:已实名
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificationState: int
        :param _OtherData: 其他流量信息,流量分离统计其他流量
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherData: float
        """
        self._Iccid = None
        self._Msisdn = None
        self._Imsi = None
        self._Imei = None
        self._Sdkappid = None
        self._Teleoperator = None
        self._CardStatus = None
        self._NetworkStatus = None
        self._ActivitedTime = None
        self._Type = None
        self._ProductId = None
        self._PoolId = None
        self._DataUsedInPeriod = None
        self._DataTotalInPeriod = None
        self._ProductExpiredTime = None
        self._Description = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._PreorderCnt = None
        self._IsActivated = None
        self._OrderId = None
        self._AutoRenew = None
        self._Remark = None
        self._AllowArrears = None
        self._NeedSms = None
        self._Provider = None
        self._CertificationState = None
        self._OtherData = None

    @property
    def Iccid(self):
        r"""卡片ID
        :rtype: str
        """
        return self._Iccid

    @Iccid.setter
    def Iccid(self, Iccid):
        self._Iccid = Iccid

    @property
    def Msisdn(self):
        r"""卡电话号码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Msisdn

    @Msisdn.setter
    def Msisdn(self, Msisdn):
        self._Msisdn = Msisdn

    @property
    def Imsi(self):
        r"""卡imsi
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Imsi

    @Imsi.setter
    def Imsi(self, Imsi):
        self._Imsi = Imsi

    @property
    def Imei(self):
        r"""卡imei
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def Sdkappid(self):
        r"""应用ID
        :rtype: str
        """
        return self._Sdkappid

    @Sdkappid.setter
    def Sdkappid(self, Sdkappid):
        self._Sdkappid = Sdkappid

    @property
    def Teleoperator(self):
        r"""运营商编号
        :rtype: int
        """
        return self._Teleoperator

    @Teleoperator.setter
    def Teleoperator(self, Teleoperator):
        self._Teleoperator = Teleoperator

    @property
    def CardStatus(self):
        r"""卡片状态 1:未激活 2：激活 3：停卡 5：销卡
        :rtype: int
        """
        return self._CardStatus

    @CardStatus.setter
    def CardStatus(self, CardStatus):
        self._CardStatus = CardStatus

    @property
    def NetworkStatus(self):
        r"""网络状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NetworkStatus

    @NetworkStatus.setter
    def NetworkStatus(self, NetworkStatus):
        self._NetworkStatus = NetworkStatus

    @property
    def ActivitedTime(self):
        r"""激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ActivitedTime

    @ActivitedTime.setter
    def ActivitedTime(self, ActivitedTime):
        self._ActivitedTime = ActivitedTime

    @property
    def Type(self):
        r"""资费类型，1 单卡，2 流量池
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ProductId(self):
        r"""套餐类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def PoolId(self):
        r"""流量池ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PoolId

    @PoolId.setter
    def PoolId(self, PoolId):
        self._PoolId = PoolId

    @property
    def DataUsedInPeriod(self):
        r"""周期套餐流量使用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._DataUsedInPeriod

    @DataUsedInPeriod.setter
    def DataUsedInPeriod(self, DataUsedInPeriod):
        self._DataUsedInPeriod = DataUsedInPeriod

    @property
    def DataTotalInPeriod(self):
        r"""周期套餐总量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._DataTotalInPeriod

    @DataTotalInPeriod.setter
    def DataTotalInPeriod(self, DataTotalInPeriod):
        self._DataTotalInPeriod = DataTotalInPeriod

    @property
    def ProductExpiredTime(self):
        r"""过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductExpiredTime

    @ProductExpiredTime.setter
    def ProductExpiredTime(self, ProductExpiredTime):
        self._ProductExpiredTime = ProductExpiredTime

    @property
    def Description(self):
        r"""描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreatedTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        r"""修改时间
        :rtype: str
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def PreorderCnt(self):
        r"""套餐周期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PreorderCnt

    @PreorderCnt.setter
    def PreorderCnt(self, PreorderCnt):
        self._PreorderCnt = PreorderCnt

    @property
    def IsActivated(self):
        r"""激活被回调标志
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsActivated

    @IsActivated.setter
    def IsActivated(self, IsActivated):
        self._IsActivated = IsActivated

    @property
    def OrderId(self):
        r"""订单ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def AutoRenew(self):
        r"""是否自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def Remark(self):
        r"""备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def AllowArrears(self):
        r"""0 不需要开通达量不停卡 1 需要开通达量不停卡
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AllowArrears

    @AllowArrears.setter
    def AllowArrears(self, AllowArrears):
        self._AllowArrears = AllowArrears

    @property
    def NeedSms(self):
        r"""是否开通短信0:未开短信 1:开通短信
        :rtype: int
        """
        return self._NeedSms

    @NeedSms.setter
    def NeedSms(self, NeedSms):
        self._NeedSms = NeedSms

    @property
    def Provider(self):
        r"""供应商
        :rtype: int
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def CertificationState(self):
        r"""实名认证 0:无 1:未实名 2:已实名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CertificationState

    @CertificationState.setter
    def CertificationState(self, CertificationState):
        self._CertificationState = CertificationState

    @property
    def OtherData(self):
        r"""其他流量信息,流量分离统计其他流量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._OtherData

    @OtherData.setter
    def OtherData(self, OtherData):
        self._OtherData = OtherData


    def _deserialize(self, params):
        self._Iccid = params.get("Iccid")
        self._Msisdn = params.get("Msisdn")
        self._Imsi = params.get("Imsi")
        self._Imei = params.get("Imei")
        self._Sdkappid = params.get("Sdkappid")
        self._Teleoperator = params.get("Teleoperator")
        self._CardStatus = params.get("CardStatus")
        self._NetworkStatus = params.get("NetworkStatus")
        self._ActivitedTime = params.get("ActivitedTime")
        self._Type = params.get("Type")
        self._ProductId = params.get("ProductId")
        self._PoolId = params.get("PoolId")
        self._DataUsedInPeriod = params.get("DataUsedInPeriod")
        self._DataTotalInPeriod = params.get("DataTotalInPeriod")
        self._ProductExpiredTime = params.get("ProductExpiredTime")
        self._Description = params.get("Description")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._PreorderCnt = params.get("PreorderCnt")
        self._IsActivated = params.get("IsActivated")
        self._OrderId = params.get("OrderId")
        self._AutoRenew = params.get("AutoRenew")
        self._Remark = params.get("Remark")
        self._AllowArrears = params.get("AllowArrears")
        self._NeedSms = params.get("NeedSms")
        self._Provider = params.get("Provider")
        self._CertificationState = params.get("CertificationState")
        self._OtherData = params.get("OtherData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CardList(AbstractModel):
    r"""卡片列表数据

    """

    def __init__(self):
        r"""
        :param _Total: 卡片总数
        :type Total: str
        :param _List: 卡片列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of CardInfo
        """
        self._Total = None
        self._List = None

    @property
    def Total(self):
        r"""卡片总数
        :rtype: str
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        r"""卡片列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CardInfo
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
                obj = CardInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppRequest(AbstractModel):
    r"""DescribeApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Sdkappid: 物联卡应用ID
        :type Sdkappid: int
        """
        self._Sdkappid = None

    @property
    def Sdkappid(self):
        r"""物联卡应用ID
        :rtype: int
        """
        return self._Sdkappid

    @Sdkappid.setter
    def Sdkappid(self, Sdkappid):
        self._Sdkappid = Sdkappid


    def _deserialize(self, params):
        self._Sdkappid = params.get("Sdkappid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppResponse(AbstractModel):
    r"""DescribeApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 应用信息详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ic.v20190307.models.AppInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""应用信息详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ic.v20190307.models.AppInfo`
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
            self._Data = AppInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCardRequest(AbstractModel):
    r"""DescribeCard请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Sdkappid: 应用ID
        :type Sdkappid: int
        :param _Iccid: 卡片ID
        :type Iccid: str
        """
        self._Sdkappid = None
        self._Iccid = None

    @property
    def Sdkappid(self):
        r"""应用ID
        :rtype: int
        """
        return self._Sdkappid

    @Sdkappid.setter
    def Sdkappid(self, Sdkappid):
        self._Sdkappid = Sdkappid

    @property
    def Iccid(self):
        r"""卡片ID
        :rtype: str
        """
        return self._Iccid

    @Iccid.setter
    def Iccid(self, Iccid):
        self._Iccid = Iccid


    def _deserialize(self, params):
        self._Sdkappid = params.get("Sdkappid")
        self._Iccid = params.get("Iccid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCardResponse(AbstractModel):
    r"""DescribeCard返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 卡片详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ic.v20190307.models.CardInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""卡片详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ic.v20190307.models.CardInfo`
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
            self._Data = CardInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCardsRequest(AbstractModel):
    r"""DescribeCards请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Sdkappid: 应用ID
        :type Sdkappid: str
        :param _Offset: 偏移值
        :type Offset: int
        :param _Limit: 列表限制
        :type Limit: int
        """
        self._Sdkappid = None
        self._Offset = None
        self._Limit = None

    @property
    def Sdkappid(self):
        r"""应用ID
        :rtype: str
        """
        return self._Sdkappid

    @Sdkappid.setter
    def Sdkappid(self, Sdkappid):
        self._Sdkappid = Sdkappid

    @property
    def Offset(self):
        r"""偏移值
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""列表限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Sdkappid = params.get("Sdkappid")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCardsResponse(AbstractModel):
    r"""DescribeCards返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 卡片列表信息
        :type Data: :class:`tencentcloud.ic.v20190307.models.CardList`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""卡片列表信息
        :rtype: :class:`tencentcloud.ic.v20190307.models.CardList`
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
            self._Data = CardList()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeSmsRequest(AbstractModel):
    r"""DescribeSms请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Sdkappid: 应用ID
        :type Sdkappid: int
        :param _Iccid: 卡片ID
        :type Iccid: str
        :param _Msisdn: 卡片号码
        :type Msisdn: str
        :param _SmsType: 短信类型
        :type SmsType: int
        :param _BeginTime: 开始时间  YYYY-MM-DD HH:mm:ss
        :type BeginTime: str
        :param _EndTime: 结束时间  YYYY-MM-DD HH:mm:ss
        :type EndTime: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 小于200
        :type Limit: int
        """
        self._Sdkappid = None
        self._Iccid = None
        self._Msisdn = None
        self._SmsType = None
        self._BeginTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def Sdkappid(self):
        r"""应用ID
        :rtype: int
        """
        return self._Sdkappid

    @Sdkappid.setter
    def Sdkappid(self, Sdkappid):
        self._Sdkappid = Sdkappid

    @property
    def Iccid(self):
        r"""卡片ID
        :rtype: str
        """
        return self._Iccid

    @Iccid.setter
    def Iccid(self, Iccid):
        self._Iccid = Iccid

    @property
    def Msisdn(self):
        r"""卡片号码
        :rtype: str
        """
        return self._Msisdn

    @Msisdn.setter
    def Msisdn(self, Msisdn):
        self._Msisdn = Msisdn

    @property
    def SmsType(self):
        r"""短信类型
        :rtype: int
        """
        return self._SmsType

    @SmsType.setter
    def SmsType(self, SmsType):
        self._SmsType = SmsType

    @property
    def BeginTime(self):
        r"""开始时间  YYYY-MM-DD HH:mm:ss
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""结束时间  YYYY-MM-DD HH:mm:ss
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""小于200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Sdkappid = params.get("Sdkappid")
        self._Iccid = params.get("Iccid")
        self._Msisdn = params.get("Msisdn")
        self._SmsType = params.get("SmsType")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsResponse(AbstractModel):
    r"""DescribeSms返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _List: 短信列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of ResSms
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

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
    def List(self):
        r"""短信列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ResSms
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
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ResSms()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyUserCardRemarkRequest(AbstractModel):
    r"""ModifyUserCardRemark请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Sdkappid: 应用ID
        :type Sdkappid: int
        :param _Iccid: 物联卡ICCID
        :type Iccid: str
        :param _Remark: 备注信息，限50字
        :type Remark: str
        """
        self._Sdkappid = None
        self._Iccid = None
        self._Remark = None

    @property
    def Sdkappid(self):
        r"""应用ID
        :rtype: int
        """
        return self._Sdkappid

    @Sdkappid.setter
    def Sdkappid(self, Sdkappid):
        self._Sdkappid = Sdkappid

    @property
    def Iccid(self):
        r"""物联卡ICCID
        :rtype: str
        """
        return self._Iccid

    @Iccid.setter
    def Iccid(self, Iccid):
        self._Iccid = Iccid

    @property
    def Remark(self):
        r"""备注信息，限50字
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Sdkappid = params.get("Sdkappid")
        self._Iccid = params.get("Iccid")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserCardRemarkResponse(AbstractModel):
    r"""ModifyUserCardRemark返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class PayForExtendDataRequest(AbstractModel):
    r"""PayForExtendData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Iccid: 卡片ICCID
        :type Iccid: str
        :param _ExtentData: 套外流量,单位MB
        :type ExtentData: int
        :param _Sdkappid: 应用ID
        :type Sdkappid: int
        """
        self._Iccid = None
        self._ExtentData = None
        self._Sdkappid = None

    @property
    def Iccid(self):
        r"""卡片ICCID
        :rtype: str
        """
        return self._Iccid

    @Iccid.setter
    def Iccid(self, Iccid):
        self._Iccid = Iccid

    @property
    def ExtentData(self):
        r"""套外流量,单位MB
        :rtype: int
        """
        return self._ExtentData

    @ExtentData.setter
    def ExtentData(self, ExtentData):
        self._ExtentData = ExtentData

    @property
    def Sdkappid(self):
        r"""应用ID
        :rtype: int
        """
        return self._Sdkappid

    @Sdkappid.setter
    def Sdkappid(self, Sdkappid):
        self._Sdkappid = Sdkappid


    def _deserialize(self, params):
        self._Iccid = params.get("Iccid")
        self._ExtentData = params.get("ExtentData")
        self._Sdkappid = params.get("Sdkappid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayForExtendDataResponse(AbstractModel):
    r"""PayForExtendData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 订单号
        :type Data: :class:`tencentcloud.ic.v20190307.models.ResOrderIds`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""订单号
        :rtype: :class:`tencentcloud.ic.v20190307.models.ResOrderIds`
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
            self._Data = ResOrderIds()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class RenewCardsRequest(AbstractModel):
    r"""RenewCards请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Sdkappid: 应用ID
        :type Sdkappid: int
        :param _Iccids: 续费的iccid
        :type Iccids: list of str
        :param _RenewNum: 续费的周期（单位：月）
        :type RenewNum: int
        """
        self._Sdkappid = None
        self._Iccids = None
        self._RenewNum = None

    @property
    def Sdkappid(self):
        r"""应用ID
        :rtype: int
        """
        return self._Sdkappid

    @Sdkappid.setter
    def Sdkappid(self, Sdkappid):
        self._Sdkappid = Sdkappid

    @property
    def Iccids(self):
        r"""续费的iccid
        :rtype: list of str
        """
        return self._Iccids

    @Iccids.setter
    def Iccids(self, Iccids):
        self._Iccids = Iccids

    @property
    def RenewNum(self):
        r"""续费的周期（单位：月）
        :rtype: int
        """
        return self._RenewNum

    @RenewNum.setter
    def RenewNum(self, RenewNum):
        self._RenewNum = RenewNum


    def _deserialize(self, params):
        self._Sdkappid = params.get("Sdkappid")
        self._Iccids = params.get("Iccids")
        self._RenewNum = params.get("RenewNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewCardsResponse(AbstractModel):
    r"""RenewCards返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 续费成功的订单id
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ic.v20190307.models.ResRenew`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""续费成功的订单id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ic.v20190307.models.ResRenew`
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
            self._Data = ResRenew()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ResOrderIds(AbstractModel):
    r"""订单ID集合

    """

    def __init__(self):
        r"""
        :param _OrderIds: 每一张续费卡片的订单ID数组
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderIds: list of str
        """
        self._OrderIds = None

    @property
    def OrderIds(self):
        r"""每一张续费卡片的订单ID数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._OrderIds

    @OrderIds.setter
    def OrderIds(self, OrderIds):
        self._OrderIds = OrderIds


    def _deserialize(self, params):
        self._OrderIds = params.get("OrderIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResRenew(AbstractModel):
    r"""云api 卡片续费

    """

    def __init__(self):
        r"""
        :param _OrderIds: 每一张续费卡片的订单ID数组
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderIds: list of str
        """
        self._OrderIds = None

    @property
    def OrderIds(self):
        r"""每一张续费卡片的订单ID数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._OrderIds

    @OrderIds.setter
    def OrderIds(self, OrderIds):
        self._OrderIds = OrderIds


    def _deserialize(self, params):
        self._OrderIds = params.get("OrderIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResSms(AbstractModel):
    r"""查询短信列表

    """

    def __init__(self):
        r"""
        :param _Iccid: 卡片ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Iccid: str
        :param _Msisdn: 卡片号码
注意：此字段可能返回 null，表示取不到有效值。
        :type Msisdn: str
        :param _SdkAppid: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SdkAppid: int
        :param _Content: 短信内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _SmsType: 短信类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SmsType: int
        :param _SendTime: 发送时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SendTime: str
        :param _ReportTime: 推送时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportTime: str
        :param _Remark: SUCC：成功  FAIL 失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _Status: 回执状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self._Iccid = None
        self._Msisdn = None
        self._SdkAppid = None
        self._Content = None
        self._SmsType = None
        self._SendTime = None
        self._ReportTime = None
        self._Remark = None
        self._Status = None

    @property
    def Iccid(self):
        r"""卡片ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Iccid

    @Iccid.setter
    def Iccid(self, Iccid):
        self._Iccid = Iccid

    @property
    def Msisdn(self):
        r"""卡片号码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Msisdn

    @Msisdn.setter
    def Msisdn(self, Msisdn):
        self._Msisdn = Msisdn

    @property
    def SdkAppid(self):
        r"""应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SdkAppid

    @SdkAppid.setter
    def SdkAppid(self, SdkAppid):
        self._SdkAppid = SdkAppid

    @property
    def Content(self):
        r"""短信内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def SmsType(self):
        r"""短信类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SmsType

    @SmsType.setter
    def SmsType(self, SmsType):
        self._SmsType = SmsType

    @property
    def SendTime(self):
        r"""发送时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SendTime

    @SendTime.setter
    def SendTime(self, SendTime):
        self._SendTime = SendTime

    @property
    def ReportTime(self):
        r"""推送时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ReportTime

    @ReportTime.setter
    def ReportTime(self, ReportTime):
        self._ReportTime = ReportTime

    @property
    def Remark(self):
        r"""SUCC：成功  FAIL 失败
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Status(self):
        r"""回执状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Iccid = params.get("Iccid")
        self._Msisdn = params.get("Msisdn")
        self._SdkAppid = params.get("SdkAppid")
        self._Content = params.get("Content")
        self._SmsType = params.get("SmsType")
        self._SendTime = params.get("SendTime")
        self._ReportTime = params.get("ReportTime")
        self._Remark = params.get("Remark")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMultiSmsRequest(AbstractModel):
    r"""SendMultiSms请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Sdkappid: 应用ID
        :type Sdkappid: str
        :param _Iccids: 卡片列表
        :type Iccids: list of str
        :param _Content: 短信内容 长度限制 70
        :type Content: str
        """
        self._Sdkappid = None
        self._Iccids = None
        self._Content = None

    @property
    def Sdkappid(self):
        r"""应用ID
        :rtype: str
        """
        return self._Sdkappid

    @Sdkappid.setter
    def Sdkappid(self, Sdkappid):
        self._Sdkappid = Sdkappid

    @property
    def Iccids(self):
        r"""卡片列表
        :rtype: list of str
        """
        return self._Iccids

    @Iccids.setter
    def Iccids(self, Iccids):
        self._Iccids = Iccids

    @property
    def Content(self):
        r"""短信内容 长度限制 70
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Sdkappid = params.get("Sdkappid")
        self._Iccids = params.get("Iccids")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMultiSmsResponse(AbstractModel):
    r"""SendMultiSms返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 短信流水数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SmsRet
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""短信流水数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SmsRet
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
                obj = SmsRet()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class SendSmsRequest(AbstractModel):
    r"""SendSms请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Sdkappid: 应用ID
        :type Sdkappid: int
        :param _Iccid: 卡片ID
        :type Iccid: str
        :param _Content: 短信内容长度70限制
        :type Content: str
        """
        self._Sdkappid = None
        self._Iccid = None
        self._Content = None

    @property
    def Sdkappid(self):
        r"""应用ID
        :rtype: int
        """
        return self._Sdkappid

    @Sdkappid.setter
    def Sdkappid(self, Sdkappid):
        self._Sdkappid = Sdkappid

    @property
    def Iccid(self):
        r"""卡片ID
        :rtype: str
        """
        return self._Iccid

    @Iccid.setter
    def Iccid(self, Iccid):
        self._Iccid = Iccid

    @property
    def Content(self):
        r"""短信内容长度70限制
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Sdkappid = params.get("Sdkappid")
        self._Iccid = params.get("Iccid")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendSmsResponse(AbstractModel):
    r"""SendSms返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 短信流水信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ic.v20190307.models.SmsSid`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""短信流水信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ic.v20190307.models.SmsSid`
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
            self._Data = SmsSid()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class SmsRet(AbstractModel):
    r"""短信流水信息

    """

    def __init__(self):
        r"""
        :param _Code: 该iccid请求状态
        :type Code: str
        :param _Msg: 短信发送返回信息
        :type Msg: str
        :param _Iccid: 卡片ID
        :type Iccid: str
        :param _Sid: 流水ID
        :type Sid: str
        """
        self._Code = None
        self._Msg = None
        self._Iccid = None
        self._Sid = None

    @property
    def Code(self):
        r"""该iccid请求状态
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        r"""短信发送返回信息
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Iccid(self):
        r"""卡片ID
        :rtype: str
        """
        return self._Iccid

    @Iccid.setter
    def Iccid(self, Iccid):
        self._Iccid = Iccid

    @property
    def Sid(self):
        r"""流水ID
        :rtype: str
        """
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._Iccid = params.get("Iccid")
        self._Sid = params.get("Sid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsSid(AbstractModel):
    r"""短信流水信息

    """

    def __init__(self):
        r"""
        :param _Iccid: 卡片ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Iccid: str
        :param _Sid: 信息流水ID
        :type Sid: str
        """
        self._Iccid = None
        self._Sid = None

    @property
    def Iccid(self):
        r"""卡片ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Iccid

    @Iccid.setter
    def Iccid(self, Iccid):
        self._Iccid = Iccid

    @property
    def Sid(self):
        r"""信息流水ID
        :rtype: str
        """
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid


    def _deserialize(self, params):
        self._Iccid = params.get("Iccid")
        self._Sid = params.get("Sid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        