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


class AppInfo(AbstractModel):
    """物联网卡应用信息详情

    """

    def __init__(self):
        r"""
        :param Sdkappid: 应用ID
        :type Sdkappid: str
        :param Appkey: 应用key
        :type Appkey: str
        :param CloudAppid: 用户appid
        :type CloudAppid: str
        :param Name: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Description: 应用描述
        :type Description: str
        :param CreatedTime: 创建时间
        :type CreatedTime: str
        :param BizType: 应用类型
        :type BizType: int
        :param Uin: 用户Uin
        :type Uin: str
        """
        self.Sdkappid = None
        self.Appkey = None
        self.CloudAppid = None
        self.Name = None
        self.Description = None
        self.CreatedTime = None
        self.BizType = None
        self.Uin = None


    def _deserialize(self, params):
        self.Sdkappid = params.get("Sdkappid")
        self.Appkey = params.get("Appkey")
        self.CloudAppid = params.get("CloudAppid")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreatedTime = params.get("CreatedTime")
        self.BizType = params.get("BizType")
        self.Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CardInfo(AbstractModel):
    """卡片详细信息

    """

    def __init__(self):
        r"""
        :param Iccid: 卡片ID
        :type Iccid: str
        :param Msisdn: 卡电话号码
注意：此字段可能返回 null，表示取不到有效值。
        :type Msisdn: str
        :param Imsi: 卡imsi
注意：此字段可能返回 null，表示取不到有效值。
        :type Imsi: str
        :param Imei: 卡imei
注意：此字段可能返回 null，表示取不到有效值。
        :type Imei: str
        :param Sdkappid: 应用ID
        :type Sdkappid: str
        :param Teleoperator: 运营商编号
        :type Teleoperator: int
        :param CardStatus: 卡片状态 1:未激活 2：激活 3：停卡 5：销卡
        :type CardStatus: int
        :param NetworkStatus: 网络状态
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkStatus: int
        :param ActivitedTime: 激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivitedTime: str
        :param Type: 资费类型，1 单卡，2 流量池
        :type Type: int
        :param ProductId: 套餐类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param PoolId: 流量池ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PoolId: str
        :param DataUsedInPeriod: 周期套餐流量使用
注意：此字段可能返回 null，表示取不到有效值。
        :type DataUsedInPeriod: float
        :param DataTotalInPeriod: 周期套餐总量
注意：此字段可能返回 null，表示取不到有效值。
        :type DataTotalInPeriod: float
        :param ProductExpiredTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductExpiredTime: str
        :param Description: 描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreatedTime: 创建时间
        :type CreatedTime: str
        :param ModifiedTime: 修改时间
        :type ModifiedTime: str
        :param PreorderCnt: 套餐周期
注意：此字段可能返回 null，表示取不到有效值。
        :type PreorderCnt: int
        :param IsActivated: 激活被回调标志
注意：此字段可能返回 null，表示取不到有效值。
        :type IsActivated: int
        :param OrderId: 订单ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param AutoRenew: 是否自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenew: int
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param AllowArrears: 0 不需要开通达量不停卡 1 需要开通达量不停卡
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowArrears: int
        :param NeedSms: 是否开通短信0:未开短信 1:开通短信
        :type NeedSms: int
        :param Provider: 供应商
        :type Provider: int
        :param CertificationState: 实名认证 0:无 1:未实名 2:已实名
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificationState: int
        :param OtherData: 其他流量信息,流量分离统计其他流量
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherData: float
        """
        self.Iccid = None
        self.Msisdn = None
        self.Imsi = None
        self.Imei = None
        self.Sdkappid = None
        self.Teleoperator = None
        self.CardStatus = None
        self.NetworkStatus = None
        self.ActivitedTime = None
        self.Type = None
        self.ProductId = None
        self.PoolId = None
        self.DataUsedInPeriod = None
        self.DataTotalInPeriod = None
        self.ProductExpiredTime = None
        self.Description = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.PreorderCnt = None
        self.IsActivated = None
        self.OrderId = None
        self.AutoRenew = None
        self.Remark = None
        self.AllowArrears = None
        self.NeedSms = None
        self.Provider = None
        self.CertificationState = None
        self.OtherData = None


    def _deserialize(self, params):
        self.Iccid = params.get("Iccid")
        self.Msisdn = params.get("Msisdn")
        self.Imsi = params.get("Imsi")
        self.Imei = params.get("Imei")
        self.Sdkappid = params.get("Sdkappid")
        self.Teleoperator = params.get("Teleoperator")
        self.CardStatus = params.get("CardStatus")
        self.NetworkStatus = params.get("NetworkStatus")
        self.ActivitedTime = params.get("ActivitedTime")
        self.Type = params.get("Type")
        self.ProductId = params.get("ProductId")
        self.PoolId = params.get("PoolId")
        self.DataUsedInPeriod = params.get("DataUsedInPeriod")
        self.DataTotalInPeriod = params.get("DataTotalInPeriod")
        self.ProductExpiredTime = params.get("ProductExpiredTime")
        self.Description = params.get("Description")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.PreorderCnt = params.get("PreorderCnt")
        self.IsActivated = params.get("IsActivated")
        self.OrderId = params.get("OrderId")
        self.AutoRenew = params.get("AutoRenew")
        self.Remark = params.get("Remark")
        self.AllowArrears = params.get("AllowArrears")
        self.NeedSms = params.get("NeedSms")
        self.Provider = params.get("Provider")
        self.CertificationState = params.get("CertificationState")
        self.OtherData = params.get("OtherData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CardList(AbstractModel):
    """卡片列表数据

    """

    def __init__(self):
        r"""
        :param Total: 卡片总数
        :type Total: str
        :param List: 卡片列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of CardInfo
        """
        self.Total = None
        self.List = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = CardInfo()
                obj._deserialize(item)
                self.List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppRequest(AbstractModel):
    """DescribeApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param Sdkappid: 物联卡应用ID
        :type Sdkappid: int
        """
        self.Sdkappid = None


    def _deserialize(self, params):
        self.Sdkappid = params.get("Sdkappid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppResponse(AbstractModel):
    """DescribeApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 应用信息详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ic.v20190307.models.AppInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = AppInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeCardRequest(AbstractModel):
    """DescribeCard请求参数结构体

    """

    def __init__(self):
        r"""
        :param Sdkappid: 应用ID
        :type Sdkappid: int
        :param Iccid: 卡片ID
        :type Iccid: str
        """
        self.Sdkappid = None
        self.Iccid = None


    def _deserialize(self, params):
        self.Sdkappid = params.get("Sdkappid")
        self.Iccid = params.get("Iccid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCardResponse(AbstractModel):
    """DescribeCard返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 卡片详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ic.v20190307.models.CardInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CardInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeCardsRequest(AbstractModel):
    """DescribeCards请求参数结构体

    """

    def __init__(self):
        r"""
        :param Sdkappid: 应用ID
        :type Sdkappid: str
        :param Offset: 偏移值
        :type Offset: int
        :param Limit: 列表限制
        :type Limit: int
        """
        self.Sdkappid = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Sdkappid = params.get("Sdkappid")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCardsResponse(AbstractModel):
    """DescribeCards返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 卡片列表信息
        :type Data: :class:`tencentcloud.ic.v20190307.models.CardList`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CardList()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeSmsRequest(AbstractModel):
    """DescribeSms请求参数结构体

    """

    def __init__(self):
        r"""
        :param Sdkappid: 应用ID
        :type Sdkappid: int
        :param Iccid: 卡片ID
        :type Iccid: str
        :param Msisdn: 卡片号码
        :type Msisdn: str
        :param SmsType: 短信类型
        :type SmsType: int
        :param BeginTime: 开始时间  YYYY-MM-DD HH:mm:ss
        :type BeginTime: str
        :param EndTime: 结束时间  YYYY-MM-DD HH:mm:ss
        :type EndTime: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 小于200
        :type Limit: int
        """
        self.Sdkappid = None
        self.Iccid = None
        self.Msisdn = None
        self.SmsType = None
        self.BeginTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Sdkappid = params.get("Sdkappid")
        self.Iccid = params.get("Iccid")
        self.Msisdn = params.get("Msisdn")
        self.SmsType = params.get("SmsType")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsResponse(AbstractModel):
    """DescribeSms返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param List: 短信列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of ResSms
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ResSms()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyUserCardRemarkRequest(AbstractModel):
    """ModifyUserCardRemark请求参数结构体

    """

    def __init__(self):
        r"""
        :param Sdkappid: 应用ID
        :type Sdkappid: int
        :param Iccid: 物联卡ICCID
        :type Iccid: str
        :param Remark: 备注信息，限50字
        :type Remark: str
        """
        self.Sdkappid = None
        self.Iccid = None
        self.Remark = None


    def _deserialize(self, params):
        self.Sdkappid = params.get("Sdkappid")
        self.Iccid = params.get("Iccid")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserCardRemarkResponse(AbstractModel):
    """ModifyUserCardRemark返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PayForExtendDataRequest(AbstractModel):
    """PayForExtendData请求参数结构体

    """

    def __init__(self):
        r"""
        :param Iccid: 卡片ICCID
        :type Iccid: str
        :param ExtentData: 套外流量,单位MB
        :type ExtentData: int
        :param Sdkappid: 应用ID
        :type Sdkappid: int
        """
        self.Iccid = None
        self.ExtentData = None
        self.Sdkappid = None


    def _deserialize(self, params):
        self.Iccid = params.get("Iccid")
        self.ExtentData = params.get("ExtentData")
        self.Sdkappid = params.get("Sdkappid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayForExtendDataResponse(AbstractModel):
    """PayForExtendData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 订单号
        :type Data: :class:`tencentcloud.ic.v20190307.models.ResOrderIds`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ResOrderIds()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class RenewCardsRequest(AbstractModel):
    """RenewCards请求参数结构体

    """

    def __init__(self):
        r"""
        :param Sdkappid: 应用ID
        :type Sdkappid: int
        :param Iccids: 续费的iccid
        :type Iccids: list of str
        :param RenewNum: 续费的周期（单位：月）
        :type RenewNum: int
        """
        self.Sdkappid = None
        self.Iccids = None
        self.RenewNum = None


    def _deserialize(self, params):
        self.Sdkappid = params.get("Sdkappid")
        self.Iccids = params.get("Iccids")
        self.RenewNum = params.get("RenewNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewCardsResponse(AbstractModel):
    """RenewCards返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 续费成功的订单id
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ic.v20190307.models.ResRenew`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ResRenew()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class ResOrderIds(AbstractModel):
    """订单ID集合

    """

    def __init__(self):
        r"""
        :param OrderIds: 每一张续费卡片的订单ID数组
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderIds: list of str
        """
        self.OrderIds = None


    def _deserialize(self, params):
        self.OrderIds = params.get("OrderIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResRenew(AbstractModel):
    """云api 卡片续费

    """

    def __init__(self):
        r"""
        :param OrderIds: 每一张续费卡片的订单ID数组
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderIds: list of str
        """
        self.OrderIds = None


    def _deserialize(self, params):
        self.OrderIds = params.get("OrderIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResSms(AbstractModel):
    """查询短信列表

    """

    def __init__(self):
        r"""
        :param Iccid: 卡片ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Iccid: str
        :param Msisdn: 卡片号码
注意：此字段可能返回 null，表示取不到有效值。
        :type Msisdn: str
        :param SdkAppid: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SdkAppid: int
        :param Content: 短信内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param SmsType: 短信类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SmsType: int
        :param SendTime: 发送时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SendTime: str
        :param ReportTime: 推送时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportTime: str
        :param Remark: SUCC：成功  FAIL 失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param Status: 回执状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self.Iccid = None
        self.Msisdn = None
        self.SdkAppid = None
        self.Content = None
        self.SmsType = None
        self.SendTime = None
        self.ReportTime = None
        self.Remark = None
        self.Status = None


    def _deserialize(self, params):
        self.Iccid = params.get("Iccid")
        self.Msisdn = params.get("Msisdn")
        self.SdkAppid = params.get("SdkAppid")
        self.Content = params.get("Content")
        self.SmsType = params.get("SmsType")
        self.SendTime = params.get("SendTime")
        self.ReportTime = params.get("ReportTime")
        self.Remark = params.get("Remark")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMultiSmsRequest(AbstractModel):
    """SendMultiSms请求参数结构体

    """

    def __init__(self):
        r"""
        :param Sdkappid: 应用ID
        :type Sdkappid: str
        :param Iccids: 卡片列表
        :type Iccids: list of str
        :param Content: 短信内容 长度限制 70
        :type Content: str
        """
        self.Sdkappid = None
        self.Iccids = None
        self.Content = None


    def _deserialize(self, params):
        self.Sdkappid = params.get("Sdkappid")
        self.Iccids = params.get("Iccids")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMultiSmsResponse(AbstractModel):
    """SendMultiSms返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 短信流水数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SmsRet
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SmsRet()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class SendSmsRequest(AbstractModel):
    """SendSms请求参数结构体

    """

    def __init__(self):
        r"""
        :param Sdkappid: 应用ID
        :type Sdkappid: int
        :param Iccid: 卡片ID
        :type Iccid: str
        :param Content: 短信内容长度70限制
        :type Content: str
        """
        self.Sdkappid = None
        self.Iccid = None
        self.Content = None


    def _deserialize(self, params):
        self.Sdkappid = params.get("Sdkappid")
        self.Iccid = params.get("Iccid")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendSmsResponse(AbstractModel):
    """SendSms返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 短信流水信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ic.v20190307.models.SmsSid`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SmsSid()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class SmsRet(AbstractModel):
    """短信流水信息

    """

    def __init__(self):
        r"""
        :param Code: 该iccid请求状态
        :type Code: str
        :param Msg: 短信发送返回信息
        :type Msg: str
        :param Iccid: 卡片ID
        :type Iccid: str
        :param Sid: 流水ID
        :type Sid: str
        """
        self.Code = None
        self.Msg = None
        self.Iccid = None
        self.Sid = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Iccid = params.get("Iccid")
        self.Sid = params.get("Sid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsSid(AbstractModel):
    """短信流水信息

    """

    def __init__(self):
        r"""
        :param Iccid: 卡片ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Iccid: str
        :param Sid: 信息流水ID
        :type Sid: str
        """
        self.Iccid = None
        self.Sid = None


    def _deserialize(self, params):
        self.Iccid = params.get("Iccid")
        self.Sid = params.get("Sid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        