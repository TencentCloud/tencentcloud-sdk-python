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


class AddRecordBatch(AbstractModel):
    """批量添加的记录

    """

    def __init__(self):
        r"""
        :param _RecordType: 记录类型, 详见 DescribeRecordType 接口。
        :type RecordType: str
        :param _Value: 记录值。
        :type Value: str
        :param _SubDomain: 子域名(主机记录)，默认为@。
        :type SubDomain: str
        :param _RecordLine: 解析记录的线路，详见 DescribeRecordLineList 接口，RecordLine和RecordLineId都未填时，默认为「默认」线路。
        :type RecordLine: str
        :param _RecordLineId: 解析记录的线路 ID，RecordLine和RecordLineId都有时，系统优先取 RecordLineId。
        :type RecordLineId: str
        :param _Weight: 记录权重值(暂未支持)。
        :type Weight: int
        :param _MX: 记录的 MX 记录值，非 MX 记录类型，默认为 0，MX记录则必选。
        :type MX: int
        :param _TTL: 记录的 TTL 值，默认600。
        :type TTL: int
        :param _Enabled: 记录状态(暂未支持)。0表示禁用，1表示启用。默认启用。
        :type Enabled: int
        :param _Remark: 记录备注(暂未支持)。
        :type Remark: str
        """
        self._RecordType = None
        self._Value = None
        self._SubDomain = None
        self._RecordLine = None
        self._RecordLineId = None
        self._Weight = None
        self._MX = None
        self._TTL = None
        self._Enabled = None
        self._Remark = None

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def RecordLineId(self):
        return self._RecordLineId

    @RecordLineId.setter
    def RecordLineId(self, RecordLineId):
        self._RecordLineId = RecordLineId

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._RecordType = params.get("RecordType")
        self._Value = params.get("Value")
        self._SubDomain = params.get("SubDomain")
        self._RecordLine = params.get("RecordLine")
        self._RecordLineId = params.get("RecordLineId")
        self._Weight = params.get("Weight")
        self._MX = params.get("MX")
        self._TTL = params.get("TTL")
        self._Enabled = params.get("Enabled")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchRecordInfo(AbstractModel):
    """批量任务中的记录信息

    """

    def __init__(self):
        r"""
        :param _RecordId: 记录 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordId: int
        :param _SubDomain: 子域名(主机记录)。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubDomain: str
        :param _RecordType: 记录类型, 详见 DescribeRecordType 接口
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordType: str
        :param _RecordLine: 解析记录的线路，详见 DescribeRecordLineList 接口
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordLine: str
        :param _Value: 记录值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _TTL: 记录的 TTL 值
注意：此字段可能返回 null，表示取不到有效值。
        :type TTL: int
        :param _Status: 记录添加状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: str
        :param _ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param _Id: 此条记录在列表中的ID
        :type Id: int
        :param _Enabled: 记录生效状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: int
        :param _MX: 记录的MX权重
注意：此字段可能返回 null，表示取不到有效值。
        :type MX: int
        :param _Weight: 记录权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param _Remark: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self._RecordId = None
        self._SubDomain = None
        self._RecordType = None
        self._RecordLine = None
        self._Value = None
        self._TTL = None
        self._Status = None
        self._Operation = None
        self._ErrMsg = None
        self._Id = None
        self._Enabled = None
        self._MX = None
        self._Weight = None
        self._Remark = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._SubDomain = params.get("SubDomain")
        self._RecordType = params.get("RecordType")
        self._RecordLine = params.get("RecordLine")
        self._Value = params.get("Value")
        self._TTL = params.get("TTL")
        self._Status = params.get("Status")
        self._Operation = params.get("Operation")
        self._ErrMsg = params.get("ErrMsg")
        self._Id = params.get("Id")
        self._Enabled = params.get("Enabled")
        self._MX = params.get("MX")
        self._Weight = params.get("Weight")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckRecordSnapshotRollbackRequest(AbstractModel):
    """CheckRecordSnapshotRollback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _SnapshotId: 快照 ID
        :type SnapshotId: str
        :param _Record: 解析记录信息
        :type Record: :class:`tencentcloud.dnspod.v20210323.models.SnapshotRecord`
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self._Domain = None
        self._SnapshotId = None
        self._Record = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def Record(self):
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._SnapshotId = params.get("SnapshotId")
        if params.get("Record") is not None:
            self._Record = SnapshotRecord()
            self._Record._deserialize(params.get("Record"))
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckRecordSnapshotRollbackResponse(AbstractModel):
    """CheckRecordSnapshotRollback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Reason: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Reason = None
        self._RequestId = None

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Reason = params.get("Reason")
        self._RequestId = params.get("RequestId")


class CheckSnapshotRollbackRequest(AbstractModel):
    """CheckSnapshotRollback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _SnapshotId: 快照记录 ID
        :type SnapshotId: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self._Domain = None
        self._SnapshotId = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._SnapshotId = params.get("SnapshotId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckSnapshotRollbackResponse(AbstractModel):
    """CheckSnapshotRollback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotId: 快照记录 ID
        :type SnapshotId: str
        :param _CostMinutes: 回滚时长（分钟）
        :type CostMinutes: int
        :param _Domain: 快照所属域名
        :type Domain: str
        :param _Total: 解析记录总数
        :type Total: int
        :param _Timeout: 值为 1，表示超时
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeout: int
        :param _Failed: 检查失败数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Failed: int
        :param _FailedRecordList: 失败记录信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedRecordList: list of SnapshotRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SnapshotId = None
        self._CostMinutes = None
        self._Domain = None
        self._Total = None
        self._Timeout = None
        self._Failed = None
        self._FailedRecordList = None
        self._RequestId = None

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def CostMinutes(self):
        return self._CostMinutes

    @CostMinutes.setter
    def CostMinutes(self, CostMinutes):
        self._CostMinutes = CostMinutes

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Failed(self):
        return self._Failed

    @Failed.setter
    def Failed(self, Failed):
        self._Failed = Failed

    @property
    def FailedRecordList(self):
        return self._FailedRecordList

    @FailedRecordList.setter
    def FailedRecordList(self, FailedRecordList):
        self._FailedRecordList = FailedRecordList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SnapshotId = params.get("SnapshotId")
        self._CostMinutes = params.get("CostMinutes")
        self._Domain = params.get("Domain")
        self._Total = params.get("Total")
        self._Timeout = params.get("Timeout")
        self._Failed = params.get("Failed")
        if params.get("FailedRecordList") is not None:
            self._FailedRecordList = []
            for item in params.get("FailedRecordList"):
                obj = SnapshotRecord()
                obj._deserialize(item)
                self._FailedRecordList.append(obj)
        self._RequestId = params.get("RequestId")


class CreateDealRequest(AbstractModel):
    """CreateDeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DealType: 询价类型，1 新购，2 续费，3 套餐升级（增值服务暂时只支持新购）
        :type DealType: int
        :param _GoodsType: 商品类型，1 域名套餐 2 增值服务
        :type GoodsType: int
        :param _GoodsChildType: 套餐类型：
DP_PLUS：专业版
DP_EXPERT：企业版
DP_ULTRA：尊享版

增值服务类型
LB：负载均衡
URL：URL转发
DMONITOR_TASKS：D监控任务数
DMONITOR_IP：D监控备用 IP 数
CUSTOMLINE：自定义线路数
        :type GoodsChildType: str
        :param _GoodsNum: 增值服务购买数量，如果是域名套餐固定为1，如果是增值服务则按以下规则：
负载均衡、D监控任务数、D监控备用 IP 数、自定义线路数、URL 转发（必须是5的正整数倍，如 5、10、15 等）
        :type GoodsNum: int
        :param _AutoRenew: 是否开启自动续费，1 开启，2 不开启（增值服务暂不支持自动续费），默认值为 2 不开启
        :type AutoRenew: int
        :param _Domain: 需要绑定套餐的域名，如 dnspod.cn，如果是续费或升级，domain 参数必须要传，新购可不传。
        :type Domain: str
        :param _TimeSpan: 套餐时长：
1. 套餐以月为单位（按月只能是 3、6 还有 12 的倍数），套餐例如购买一年则传12，最大120 。（续费最低一年）
2. 升级套餐时不需要传。
3. 增值服务的时长单位为年，买一年传1（增值服务新购按年只能是 1，增值服务续费最大为 10）
        :type TimeSpan: int
        :param _NewPackageType: 套餐类型，需要升级到的套餐类型，只有升级时需要。
        :type NewPackageType: str
        """
        self._DealType = None
        self._GoodsType = None
        self._GoodsChildType = None
        self._GoodsNum = None
        self._AutoRenew = None
        self._Domain = None
        self._TimeSpan = None
        self._NewPackageType = None

    @property
    def DealType(self):
        return self._DealType

    @DealType.setter
    def DealType(self, DealType):
        self._DealType = DealType

    @property
    def GoodsType(self):
        return self._GoodsType

    @GoodsType.setter
    def GoodsType(self, GoodsType):
        self._GoodsType = GoodsType

    @property
    def GoodsChildType(self):
        return self._GoodsChildType

    @GoodsChildType.setter
    def GoodsChildType(self, GoodsChildType):
        self._GoodsChildType = GoodsChildType

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def NewPackageType(self):
        return self._NewPackageType

    @NewPackageType.setter
    def NewPackageType(self, NewPackageType):
        self._NewPackageType = NewPackageType


    def _deserialize(self, params):
        self._DealType = params.get("DealType")
        self._GoodsType = params.get("GoodsType")
        self._GoodsChildType = params.get("GoodsChildType")
        self._GoodsNum = params.get("GoodsNum")
        self._AutoRenew = params.get("AutoRenew")
        self._Domain = params.get("Domain")
        self._TimeSpan = params.get("TimeSpan")
        self._NewPackageType = params.get("NewPackageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDealResponse(AbstractModel):
    """CreateDeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BigDealId: 大订单号，一个大订单号下可以有多个子订单，说明是同一次下单
        :type BigDealId: str
        :param _DealList: 子订单列表
        :type DealList: list of Deals
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BigDealId = None
        self._DealList = None
        self._RequestId = None

    @property
    def BigDealId(self):
        return self._BigDealId

    @BigDealId.setter
    def BigDealId(self, BigDealId):
        self._BigDealId = BigDealId

    @property
    def DealList(self):
        return self._DealList

    @DealList.setter
    def DealList(self, DealList):
        self._DealList = DealList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BigDealId = params.get("BigDealId")
        if params.get("DealList") is not None:
            self._DealList = []
            for item in params.get("DealList"):
                obj = Deals()
                obj._deserialize(item)
                self._DealList.append(obj)
        self._RequestId = params.get("RequestId")


class CreateDomainAliasRequest(AbstractModel):
    """CreateDomainAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainAlias: 域名别名
        :type DomainAlias: str
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名ID，参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._DomainAlias = None
        self._Domain = None
        self._DomainId = None

    @property
    def DomainAlias(self):
        return self._DomainAlias

    @DomainAlias.setter
    def DomainAlias(self, DomainAlias):
        self._DomainAlias = DomainAlias

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._DomainAlias = params.get("DomainAlias")
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainAliasResponse(AbstractModel):
    """CreateDomainAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainAliasId: 域名别名ID
        :type DomainAliasId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainAliasId = None
        self._RequestId = None

    @property
    def DomainAliasId(self):
        return self._DomainAliasId

    @DomainAliasId.setter
    def DomainAliasId(self, DomainAliasId):
        self._DomainAliasId = DomainAliasId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DomainAliasId = params.get("DomainAliasId")
        self._RequestId = params.get("RequestId")


class CreateDomainBatchDetail(AbstractModel):
    """批量添加域名返回结构

    """

    def __init__(self):
        r"""
        :param _RecordList: 见RecordInfoBatch
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordList: list of CreateDomainBatchRecord
        :param _Id: 任务编号
        :type Id: int
        :param _Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _DomainGrade: 域名等级
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainGrade: str
        :param _ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param _Status: 该条任务运行状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: str
        """
        self._RecordList = None
        self._Id = None
        self._Domain = None
        self._DomainGrade = None
        self._ErrMsg = None
        self._Status = None
        self._Operation = None

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainGrade(self):
        return self._DomainGrade

    @DomainGrade.setter
    def DomainGrade(self, DomainGrade):
        self._DomainGrade = DomainGrade

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = CreateDomainBatchRecord()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._Id = params.get("Id")
        self._Domain = params.get("Domain")
        self._DomainGrade = params.get("DomainGrade")
        self._ErrMsg = params.get("ErrMsg")
        self._Status = params.get("Status")
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainBatchRecord(AbstractModel):
    """批量添加域名任务中的记录信息

    """

    def __init__(self):
        r"""
        :param _SubDomain: 子域名(主机记录)。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubDomain: str
        :param _RecordType: 记录类型, 详见 DescribeRecordType 接口
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordType: str
        :param _RecordLine: 解析记录的线路，详见 DescribeRecordLineList 接口
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordLine: str
        :param _Value: 记录值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _TTL: 记录的 TTL 值
注意：此字段可能返回 null，表示取不到有效值。
        :type TTL: int
        :param _Status: 记录添加状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: str
        :param _ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param _Id: 此条记录在列表中的ID
        :type Id: int
        """
        self._SubDomain = None
        self._RecordType = None
        self._RecordLine = None
        self._Value = None
        self._TTL = None
        self._Status = None
        self._Operation = None
        self._ErrMsg = None
        self._Id = None

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._SubDomain = params.get("SubDomain")
        self._RecordType = params.get("RecordType")
        self._RecordLine = params.get("RecordLine")
        self._Value = params.get("Value")
        self._TTL = params.get("TTL")
        self._Status = params.get("Status")
        self._Operation = params.get("Operation")
        self._ErrMsg = params.get("ErrMsg")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainBatchRequest(AbstractModel):
    """CreateDomainBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainList: 域名数组
        :type DomainList: list of str
        :param _RecordValue: 每个域名添加 @ 和 www 的 A 记录值，记录值为IP，如果不传此参数或者传空，将只添加域名，不添加记录。
        :type RecordValue: str
        """
        self._DomainList = None
        self._RecordValue = None

    @property
    def DomainList(self):
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def RecordValue(self):
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue


    def _deserialize(self, params):
        self._DomainList = params.get("DomainList")
        self._RecordValue = params.get("RecordValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainBatchResponse(AbstractModel):
    """CreateDomainBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DetailList: 批量添加域名信息
        :type DetailList: list of CreateDomainBatchDetail
        :param _JobId: 批量任务的ID
        :type JobId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DetailList = None
        self._JobId = None
        self._RequestId = None

    @property
    def DetailList(self):
        return self._DetailList

    @DetailList.setter
    def DetailList(self, DetailList):
        self._DetailList = DetailList

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DetailList") is not None:
            self._DetailList = []
            for item in params.get("DetailList"):
                obj = CreateDomainBatchDetail()
                obj._deserialize(item)
                self._DetailList.append(obj)
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class CreateDomainGroupRequest(AbstractModel):
    """CreateDomainGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 域名分组
        :type GroupName: str
        """
        self._GroupName = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainGroupResponse(AbstractModel):
    """CreateDomainGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 域名分组ID
        :type GroupId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateDomainRequest(AbstractModel):
    """CreateDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _GroupId: 域名分组ID。可以通过接口DescribeDomainGroupList查看当前域名分组信息
        :type GroupId: int
        :param _IsMark: 是否星标域名，”yes”、”no” 分别代表是和否。
        :type IsMark: str
        :param _TransferSubDomain: 添加子域名时，是否迁移相关父域名的解析记录。不传默认为 true
        :type TransferSubDomain: bool
        :param _Tags: 域名绑定的标签
        :type Tags: list of TagItem
        """
        self._Domain = None
        self._GroupId = None
        self._IsMark = None
        self._TransferSubDomain = None
        self._Tags = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def IsMark(self):
        return self._IsMark

    @IsMark.setter
    def IsMark(self, IsMark):
        self._IsMark = IsMark

    @property
    def TransferSubDomain(self):
        return self._TransferSubDomain

    @TransferSubDomain.setter
    def TransferSubDomain(self, TransferSubDomain):
        self._TransferSubDomain = TransferSubDomain

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._GroupId = params.get("GroupId")
        self._IsMark = params.get("IsMark")
        self._TransferSubDomain = params.get("TransferSubDomain")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainResponse(AbstractModel):
    """CreateDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainInfo: 域名信息
        :type DomainInfo: :class:`tencentcloud.dnspod.v20210323.models.DomainCreateInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainInfo = None
        self._RequestId = None

    @property
    def DomainInfo(self):
        return self._DomainInfo

    @DomainInfo.setter
    def DomainInfo(self, DomainInfo):
        self._DomainInfo = DomainInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self._DomainInfo = DomainCreateInfo()
            self._DomainInfo._deserialize(params.get("DomainInfo"))
        self._RequestId = params.get("RequestId")


class CreateRecordBatchDetail(AbstractModel):
    """批量添加记录返回结构

    """

    def __init__(self):
        r"""
        :param _RecordList: 见RecordInfoBatch
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordList: list of CreateRecordBatchRecord
        :param _Id: 任务编号
        :type Id: int
        :param _Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _DomainGrade: 域名等级
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainGrade: str
        :param _ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param _Status: 该条任务运行状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: str
        :param _DomainId: 域名ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainId: int
        """
        self._RecordList = None
        self._Id = None
        self._Domain = None
        self._DomainGrade = None
        self._ErrMsg = None
        self._Status = None
        self._Operation = None
        self._DomainId = None

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainGrade(self):
        return self._DomainGrade

    @DomainGrade.setter
    def DomainGrade(self, DomainGrade):
        self._DomainGrade = DomainGrade

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = CreateRecordBatchRecord()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._Id = params.get("Id")
        self._Domain = params.get("Domain")
        self._DomainGrade = params.get("DomainGrade")
        self._ErrMsg = params.get("ErrMsg")
        self._Status = params.get("Status")
        self._Operation = params.get("Operation")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordBatchRecord(AbstractModel):
    """批量添加记录任务中的记录信息

    """

    def __init__(self):
        r"""
        :param _SubDomain: 子域名(主机记录)。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubDomain: str
        :param _RecordType: 记录类型, 详见 DescribeRecordType 接口
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordType: str
        :param _RecordLine: 解析记录的线路，详见 DescribeRecordLineList 接口
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordLine: str
        :param _Value: 记录值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _TTL: 记录的 TTL 值
注意：此字段可能返回 null，表示取不到有效值。
        :type TTL: int
        :param _Status: 记录添加状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: str
        :param _ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param _Id: 此条记录在列表中的ID
        :type Id: int
        :param _MX: 记录的MX权重
注意：此字段可能返回 null，表示取不到有效值。
        :type MX: int
        :param _Weight: 记录的权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        """
        self._SubDomain = None
        self._RecordType = None
        self._RecordLine = None
        self._Value = None
        self._TTL = None
        self._Status = None
        self._Operation = None
        self._ErrMsg = None
        self._Id = None
        self._MX = None
        self._Weight = None

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._SubDomain = params.get("SubDomain")
        self._RecordType = params.get("RecordType")
        self._RecordLine = params.get("RecordLine")
        self._Value = params.get("Value")
        self._TTL = params.get("TTL")
        self._Status = params.get("Status")
        self._Operation = params.get("Operation")
        self._ErrMsg = params.get("ErrMsg")
        self._Id = params.get("Id")
        self._MX = params.get("MX")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordBatchRequest(AbstractModel):
    """CreateRecordBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainIdList: 域名ID，多个 domain_id 用英文逗号进行分割。
        :type DomainIdList: list of str
        :param _RecordList: 记录数组
        :type RecordList: list of AddRecordBatch
        """
        self._DomainIdList = None
        self._RecordList = None

    @property
    def DomainIdList(self):
        return self._DomainIdList

    @DomainIdList.setter
    def DomainIdList(self, DomainIdList):
        self._DomainIdList = DomainIdList

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList


    def _deserialize(self, params):
        self._DomainIdList = params.get("DomainIdList")
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = AddRecordBatch()
                obj._deserialize(item)
                self._RecordList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordBatchResponse(AbstractModel):
    """CreateRecordBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DetailList: 批量添加域名信息
        :type DetailList: list of CreateRecordBatchDetail
        :param _JobId: 批量任务的ID
        :type JobId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DetailList = None
        self._JobId = None
        self._RequestId = None

    @property
    def DetailList(self):
        return self._DetailList

    @DetailList.setter
    def DetailList(self, DetailList):
        self._DetailList = DetailList

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DetailList") is not None:
            self._DetailList = []
            for item in params.get("DetailList"):
                obj = CreateRecordBatchDetail()
                obj._deserialize(item)
                self._DetailList.append(obj)
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class CreateRecordGroupRequest(AbstractModel):
    """CreateRecordGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _GroupName: 分组名称
        :type GroupName: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self._Domain = None
        self._GroupName = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._GroupName = params.get("GroupName")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordGroupResponse(AbstractModel):
    """CreateRecordGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 新增的分组 ID
        :type GroupId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateRecordRequest(AbstractModel):
    """CreateRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _RecordType: 记录类型，通过 API 记录类型获得，大写英文，比如：A 。
        :type RecordType: str
        :param _RecordLine: 记录线路，通过 API 记录线路获得，中文，比如：默认。
        :type RecordLine: str
        :param _Value: 记录值，如 IP : 200.200.200.200， CNAME : cname.dnspod.com.， MX : mail.dnspod.com.。
        :type Value: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        :param _SubDomain: 主机记录，如 www，如果不传，默认为 @。
        :type SubDomain: str
        :param _RecordLineId: 线路的 ID，通过 API 记录线路获得，英文字符串，比如：10=1。参数RecordLineId优先级高于RecordLine，如果同时传递二者，优先使用RecordLineId参数。
        :type RecordLineId: str
        :param _MX: MX 优先级，当记录类型是 MX 时有效，范围1-20，MX 记录时必选。
        :type MX: int
        :param _TTL: TTL，范围1-604800，不同等级域名最小值不同。
        :type TTL: int
        :param _Weight: 权重信息，0到100的整数。仅企业 VIP 域名可用，0 表示关闭，不传该参数，表示不设置权重信息。
        :type Weight: int
        :param _Status: 记录初始状态，取值范围为 ENABLE 和 DISABLE 。默认为 ENABLE ，如果传入 DISABLE，解析不会生效，也不会验证负载均衡的限制。
        :type Status: str
        :param _Remark: 备注
        :type Remark: str
        """
        self._Domain = None
        self._RecordType = None
        self._RecordLine = None
        self._Value = None
        self._DomainId = None
        self._SubDomain = None
        self._RecordLineId = None
        self._MX = None
        self._TTL = None
        self._Weight = None
        self._Status = None
        self._Remark = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordLineId(self):
        return self._RecordLineId

    @RecordLineId.setter
    def RecordLineId(self, RecordLineId):
        self._RecordLineId = RecordLineId

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RecordType = params.get("RecordType")
        self._RecordLine = params.get("RecordLine")
        self._Value = params.get("Value")
        self._DomainId = params.get("DomainId")
        self._SubDomain = params.get("SubDomain")
        self._RecordLineId = params.get("RecordLineId")
        self._MX = params.get("MX")
        self._TTL = params.get("TTL")
        self._Weight = params.get("Weight")
        self._Status = params.get("Status")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordResponse(AbstractModel):
    """CreateRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordId: 记录ID
        :type RecordId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordId = None
        self._RequestId = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._RequestId = params.get("RequestId")


class CreateSnapshotRequest(AbstractModel):
    """CreateSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self._Domain = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSnapshotResponse(AbstractModel):
    """CreateSnapshot返回参数结构体

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


class Deals(AbstractModel):
    """子订单号列表

    """

    def __init__(self):
        r"""
        :param _DealId: 子订单ID
        :type DealId: str
        :param _DealName: 子订单号
        :type DealName: str
        """
        self._DealId = None
        self._DealName = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._DealName = params.get("DealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainAliasRequest(AbstractModel):
    """DeleteDomainAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainAliasId: 域名别名ID。可以通过接口DescribeDomainAliasList查到所有的域名别名列表以及对应的ID
        :type DomainAliasId: int
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名ID，参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._DomainAliasId = None
        self._Domain = None
        self._DomainId = None

    @property
    def DomainAliasId(self):
        return self._DomainAliasId

    @DomainAliasId.setter
    def DomainAliasId(self, DomainAliasId):
        self._DomainAliasId = DomainAliasId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._DomainAliasId = params.get("DomainAliasId")
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainAliasResponse(AbstractModel):
    """DeleteDomainAlias返回参数结构体

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


class DeleteDomainBatchDetail(AbstractModel):
    """批量删除域名详情

    """

    def __init__(self):
        r"""
        :param _DomainId: 域名 ID
        :type DomainId: int
        :param _Domain: 域名
        :type Domain: str
        :param _Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: str
        :param _Status: 删除状态
        :type Status: str
        :param _Operation: 操作
        :type Operation: str
        """
        self._DomainId = None
        self._Domain = None
        self._Error = None
        self._Status = None
        self._Operation = None

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._Domain = params.get("Domain")
        self._Error = params.get("Error")
        self._Status = params.get("Status")
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainBatchRequest(AbstractModel):
    """DeleteDomainBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainList: 域名数组
        :type DomainList: list of str
        """
        self._DomainList = None

    @property
    def DomainList(self):
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList


    def _deserialize(self, params):
        self._DomainList = params.get("DomainList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainBatchResponse(AbstractModel):
    """DeleteDomainBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务 ID
        :type JobId: int
        :param _DetailList: 任务详情数组
        :type DetailList: list of DeleteDomainBatchDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._DetailList = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def DetailList(self):
        return self._DetailList

    @DetailList.setter
    def DetailList(self, DetailList):
        self._DetailList = DetailList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        if params.get("DetailList") is not None:
            self._DetailList = []
            for item in params.get("DetailList"):
                obj = DeleteDomainBatchDetail()
                obj._deserialize(item)
                self._DetailList.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteDomainRequest(AbstractModel):
    """DeleteDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
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


class DeleteRecordBatchDetail(AbstractModel):
    """批量删除记录详情

    """

    def __init__(self):
        r"""
        :param _DomainId: 域名 ID
        :type DomainId: int
        :param _Domain: 域名
        :type Domain: str
        :param _Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: str
        :param _Status: 删除状态
        :type Status: str
        :param _Operation: 操作
        :type Operation: str
        :param _RecordList: 解析记录列表，json 序列化之后的字符串形式
        :type RecordList: str
        """
        self._DomainId = None
        self._Domain = None
        self._Error = None
        self._Status = None
        self._Operation = None
        self._RecordList = None

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._Domain = params.get("Domain")
        self._Error = params.get("Error")
        self._Status = params.get("Status")
        self._Operation = params.get("Operation")
        self._RecordList = params.get("RecordList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordBatchRequest(AbstractModel):
    """DeleteRecordBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordIdList: 解析记录 ID 数组
        :type RecordIdList: list of int non-negative
        """
        self._RecordIdList = None

    @property
    def RecordIdList(self):
        return self._RecordIdList

    @RecordIdList.setter
    def RecordIdList(self, RecordIdList):
        self._RecordIdList = RecordIdList


    def _deserialize(self, params):
        self._RecordIdList = params.get("RecordIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordBatchResponse(AbstractModel):
    """DeleteRecordBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 批量任务 ID
        :type JobId: int
        :param _DetailList: 任务详情
        :type DetailList: list of DeleteRecordBatchDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._DetailList = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def DetailList(self):
        return self._DetailList

    @DetailList.setter
    def DetailList(self, DetailList):
        self._DetailList = DetailList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        if params.get("DetailList") is not None:
            self._DetailList = []
            for item in params.get("DetailList"):
                obj = DeleteRecordBatchDetail()
                obj._deserialize(item)
                self._DetailList.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteRecordGroupRequest(AbstractModel):
    """DeleteRecordGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _GroupId: 分组 ID
        :type GroupId: int
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self._Domain = None
        self._GroupId = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._GroupId = params.get("GroupId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordGroupResponse(AbstractModel):
    """DeleteRecordGroup返回参数结构体

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


class DeleteRecordRequest(AbstractModel):
    """DeleteRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _RecordId: 记录 ID 。可以通过接口DescribeRecordList查到所有的解析记录列表以及对应的RecordId
        :type RecordId: int
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._RecordId = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RecordId = params.get("RecordId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordResponse(AbstractModel):
    """DeleteRecord返回参数结构体

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


class DeleteShareDomainRequest(AbstractModel):
    """DeleteShareDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Account: 域名共享的账号
        :type Account: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._Account = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Account = params.get("Account")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteShareDomainResponse(AbstractModel):
    """DeleteShareDomain返回参数结构体

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


class DeleteSnapshotRequest(AbstractModel):
    """DeleteSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _SnapshotId: 快照记录 ID
        :type SnapshotId: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self._Domain = None
        self._SnapshotId = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._SnapshotId = params.get("SnapshotId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSnapshotResponse(AbstractModel):
    """DeleteSnapshot返回参数结构体

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


class DescribeBatchTaskDetail(AbstractModel):
    """查看任务详情返回结构

    """

    def __init__(self):
        r"""
        :param _RecordList: 见BatchRecordInfo
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordList: list of BatchRecordInfo
        :param _Id: 任务编号
        :type Id: int
        :param _Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _DomainGrade: 域名等级
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainGrade: str
        :param _ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param _Status: 该条任务运行状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: str
        :param _DomainId: 域名ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainId: int
        """
        self._RecordList = None
        self._Id = None
        self._Domain = None
        self._DomainGrade = None
        self._ErrMsg = None
        self._Status = None
        self._Operation = None
        self._DomainId = None

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainGrade(self):
        return self._DomainGrade

    @DomainGrade.setter
    def DomainGrade(self, DomainGrade):
        self._DomainGrade = DomainGrade

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = BatchRecordInfo()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._Id = params.get("Id")
        self._Domain = params.get("Domain")
        self._DomainGrade = params.get("DomainGrade")
        self._ErrMsg = params.get("ErrMsg")
        self._Status = params.get("Status")
        self._Operation = params.get("Operation")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchTaskRequest(AbstractModel):
    """DescribeBatchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。操作批量接口时会返回JobId
        :type JobId: int
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchTaskResponse(AbstractModel):
    """DescribeBatchTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DetailList: 批量任务详情
        :type DetailList: list of DescribeBatchTaskDetail
        :param _TotalCount: 总任务条数
        :type TotalCount: int
        :param _SuccessCount: 成功条数
        :type SuccessCount: int
        :param _FailCount: 失败条数
        :type FailCount: int
        :param _JobType: 批量任务类型
        :type JobType: str
        :param _CreatedAt: 任务创建时间
        :type CreatedAt: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DetailList = None
        self._TotalCount = None
        self._SuccessCount = None
        self._FailCount = None
        self._JobType = None
        self._CreatedAt = None
        self._RequestId = None

    @property
    def DetailList(self):
        return self._DetailList

    @DetailList.setter
    def DetailList(self, DetailList):
        self._DetailList = DetailList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
    def JobType(self):
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DetailList") is not None:
            self._DetailList = []
            for item in params.get("DetailList"):
                obj = DescribeBatchTaskDetail()
                obj._deserialize(item)
                self._DetailList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._SuccessCount = params.get("SuccessCount")
        self._FailCount = params.get("FailCount")
        self._JobType = params.get("JobType")
        self._CreatedAt = params.get("CreatedAt")
        self._RequestId = params.get("RequestId")


class DescribeDomainAliasListRequest(AbstractModel):
    """DescribeDomainAliasList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名ID,域名ID，参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainAliasListResponse(AbstractModel):
    """DescribeDomainAliasList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainAliasList: 域名别名列表
        :type DomainAliasList: list of DomainAliasInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainAliasList = None
        self._RequestId = None

    @property
    def DomainAliasList(self):
        return self._DomainAliasList

    @DomainAliasList.setter
    def DomainAliasList(self, DomainAliasList):
        self._DomainAliasList = DomainAliasList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainAliasList") is not None:
            self._DomainAliasList = []
            for item in params.get("DomainAliasList"):
                obj = DomainAliasInfo()
                obj._deserialize(item)
                self._DomainAliasList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainAnalyticsRequest(AbstractModel):
    """DescribeDomainAnalytics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 要查询解析量的域名
        :type Domain: str
        :param _StartDate: 查询的开始时间，格式：YYYY-MM-DD
        :type StartDate: str
        :param _EndDate: 查询的结束时间，格式：YYYY-MM-DD
        :type EndDate: str
        :param _DnsFormat: DATE:按天维度统计 HOUR:按小时维度统计
        :type DnsFormat: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._StartDate = None
        self._EndDate = None
        self._DnsFormat = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def DnsFormat(self):
        return self._DnsFormat

    @DnsFormat.setter
    def DnsFormat(self, DnsFormat):
        self._DnsFormat = DnsFormat

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._DnsFormat = params.get("DnsFormat")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainAnalyticsResponse(AbstractModel):
    """DescribeDomainAnalytics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 当前统计维度解析量小计
        :type Data: list of DomainAnalyticsDetail
        :param _Info: 域名解析量统计查询信息
        :type Info: :class:`tencentcloud.dnspod.v20210323.models.DomainAnalyticsInfo`
        :param _AliasData: 域名别名解析量统计信息
        :type AliasData: list of DomainAliasAnalyticsItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Info = None
        self._AliasData = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def AliasData(self):
        return self._AliasData

    @AliasData.setter
    def AliasData(self, AliasData):
        self._AliasData = AliasData

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
                obj = DomainAnalyticsDetail()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("Info") is not None:
            self._Info = DomainAnalyticsInfo()
            self._Info._deserialize(params.get("Info"))
        if params.get("AliasData") is not None:
            self._AliasData = []
            for item in params.get("AliasData"):
                obj = DomainAliasAnalyticsItem()
                obj._deserialize(item)
                self._AliasData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainFilterListRequest(AbstractModel):
    """DescribeDomainFilterList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 根据域名分组类型获取域名。可取值为 ALL，MINE，SHARE，RECENT。
ALL：全部
MINE：我的域名
SHARE：共享给我的域名
RECENT：最近操作过的域名
        :type Type: str
        :param _Offset: 记录开始的偏移, 第一条记录为 0, 依次类推。默认值为 0。
        :type Offset: int
        :param _Limit: 要获取的域名数量, 比如获取 20 个, 则为 20。默认值为 5000。如果账户中的域名数量超过了 5000, 将会强制分页并且只返回前 5000 条, 这时需要通过 Offset 和 Limit 参数去获取其它域名。
        :type Limit: int
        :param _GroupId: 根据域名分组 id 获取域名，可通过 DescribeDomain 或 DescribeDomainList 接口 GroupId 字段获取。
        :type GroupId: list of int
        :param _Keyword: 根据关键字获取域名。
        :type Keyword: str
        :param _SortField: 排序字段。可取值为 NAME，STATUS，RECORDS，GRADE，UPDATED_ON。
NAME：域名名称
STATUS：域名状态
RECORDS：记录数量
GRADE：套餐等级
UPDATED_ON：更新时间
        :type SortField: str
        :param _SortType: 排序类型，升序：ASC，降序：DESC。
        :type SortType: str
        :param _Status: 根据域名状态获取域名。可取值为 ENABLE，LOCK，PAUSE，SPAM。
ENABLE：正常
LOCK：锁定
PAUSE：暂停
SPAM：封禁
        :type Status: list of str
        :param _Package: 根据套餐获取域名，可通过 DescribeDomain 或 DescribeDomainList 接口 Grade 字段获取。
        :type Package: list of str
        :param _Remark: 根据备注信息获取域名。
        :type Remark: str
        :param _UpdatedAtBegin: 要获取域名的更新时间起始时间点，如 '2021-05-01 03:00:00'。
        :type UpdatedAtBegin: str
        :param _UpdatedAtEnd: 要获取域名的更新时间终止时间点，如 '2021-05-10 20:00:00'。
        :type UpdatedAtEnd: str
        :param _RecordCountBegin: 要获取域名的记录数查询区间起点。
        :type RecordCountBegin: int
        :param _RecordCountEnd: 要获取域名的记录数查询区间终点。
        :type RecordCountEnd: int
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _Tags: 标签过滤
        :type Tags: list of TagItemFilter
        """
        self._Type = None
        self._Offset = None
        self._Limit = None
        self._GroupId = None
        self._Keyword = None
        self._SortField = None
        self._SortType = None
        self._Status = None
        self._Package = None
        self._Remark = None
        self._UpdatedAtBegin = None
        self._UpdatedAtEnd = None
        self._RecordCountBegin = None
        self._RecordCountEnd = None
        self._ProjectId = None
        self._Tags = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def SortField(self):
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortType(self):
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Package(self):
        return self._Package

    @Package.setter
    def Package(self, Package):
        self._Package = Package

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def UpdatedAtBegin(self):
        return self._UpdatedAtBegin

    @UpdatedAtBegin.setter
    def UpdatedAtBegin(self, UpdatedAtBegin):
        self._UpdatedAtBegin = UpdatedAtBegin

    @property
    def UpdatedAtEnd(self):
        return self._UpdatedAtEnd

    @UpdatedAtEnd.setter
    def UpdatedAtEnd(self, UpdatedAtEnd):
        self._UpdatedAtEnd = UpdatedAtEnd

    @property
    def RecordCountBegin(self):
        return self._RecordCountBegin

    @RecordCountBegin.setter
    def RecordCountBegin(self, RecordCountBegin):
        self._RecordCountBegin = RecordCountBegin

    @property
    def RecordCountEnd(self):
        return self._RecordCountEnd

    @RecordCountEnd.setter
    def RecordCountEnd(self, RecordCountEnd):
        self._RecordCountEnd = RecordCountEnd

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._GroupId = params.get("GroupId")
        self._Keyword = params.get("Keyword")
        self._SortField = params.get("SortField")
        self._SortType = params.get("SortType")
        self._Status = params.get("Status")
        self._Package = params.get("Package")
        self._Remark = params.get("Remark")
        self._UpdatedAtBegin = params.get("UpdatedAtBegin")
        self._UpdatedAtEnd = params.get("UpdatedAtEnd")
        self._RecordCountBegin = params.get("RecordCountBegin")
        self._RecordCountEnd = params.get("RecordCountEnd")
        self._ProjectId = params.get("ProjectId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItemFilter()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainFilterListResponse(AbstractModel):
    """DescribeDomainFilterList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainCountInfo: 列表页统计信息
        :type DomainCountInfo: :class:`tencentcloud.dnspod.v20210323.models.DomainCountInfo`
        :param _DomainList: 域名列表
        :type DomainList: list of DomainListItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainCountInfo = None
        self._DomainList = None
        self._RequestId = None

    @property
    def DomainCountInfo(self):
        return self._DomainCountInfo

    @DomainCountInfo.setter
    def DomainCountInfo(self, DomainCountInfo):
        self._DomainCountInfo = DomainCountInfo

    @property
    def DomainList(self):
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainCountInfo") is not None:
            self._DomainCountInfo = DomainCountInfo()
            self._DomainCountInfo._deserialize(params.get("DomainCountInfo"))
        if params.get("DomainList") is not None:
            self._DomainList = []
            for item in params.get("DomainList"):
                obj = DomainListItem()
                obj._deserialize(item)
                self._DomainList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainGroupListRequest(AbstractModel):
    """DescribeDomainGroupList请求参数结构体

    """


class DescribeDomainGroupListResponse(AbstractModel):
    """DescribeDomainGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupList: 分组列表
        :type GroupList: list of GroupInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupList = None
        self._RequestId = None

    @property
    def GroupList(self):
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self._GroupList = []
            for item in params.get("GroupList"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._GroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainListRequest(AbstractModel):
    """DescribeDomainList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 域名分组类型，默认为ALL。可取值为ALL，MINE，SHARE，ISMARK，PAUSE，VIP，RECENT，SHARE_OUT，FREE。
        :type Type: str
        :param _Offset: 记录开始的偏移, 第一条记录为 0, 依次类推。默认值为0。
        :type Offset: int
        :param _Limit: 要获取的域名数量, 比如获取20个, 则为20。默认值为3000。
        :type Limit: int
        :param _GroupId: 分组ID, 获取指定分组的域名
        :type GroupId: int
        :param _Keyword: 根据关键字搜索域名
        :type Keyword: str
        :param _Tags: 标签过滤
        :type Tags: list of TagItemFilter
        """
        self._Type = None
        self._Offset = None
        self._Limit = None
        self._GroupId = None
        self._Keyword = None
        self._Tags = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._GroupId = params.get("GroupId")
        self._Keyword = params.get("Keyword")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagItemFilter()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainListResponse(AbstractModel):
    """DescribeDomainList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainCountInfo: 列表页统计信息
        :type DomainCountInfo: :class:`tencentcloud.dnspod.v20210323.models.DomainCountInfo`
        :param _DomainList: 域名列表
        :type DomainList: list of DomainListItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainCountInfo = None
        self._DomainList = None
        self._RequestId = None

    @property
    def DomainCountInfo(self):
        return self._DomainCountInfo

    @DomainCountInfo.setter
    def DomainCountInfo(self, DomainCountInfo):
        self._DomainCountInfo = DomainCountInfo

    @property
    def DomainList(self):
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainCountInfo") is not None:
            self._DomainCountInfo = DomainCountInfo()
            self._DomainCountInfo._deserialize(params.get("DomainCountInfo"))
        if params.get("DomainList") is not None:
            self._DomainList = []
            for item in params.get("DomainList"):
                obj = DomainListItem()
                obj._deserialize(item)
                self._DomainList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainLogListRequest(AbstractModel):
    """DescribeDomainLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        :param _Offset: 记录开始的偏移，第一条记录为 0，依次类推，默认为0
        :type Offset: int
        :param _Limit: 共要获取的日志条数，比如获取20条，则为20，默认为500条，单次最多获取500条。
        :type Limit: int
        """
        self._Domain = None
        self._DomainId = None
        self._Offset = None
        self._Limit = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainLogListResponse(AbstractModel):
    """DescribeDomainLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LogList: 域名信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LogList: list of str
        :param _PageSize: 分页大小
        :type PageSize: int
        :param _TotalCount: 日志总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LogList = None
        self._PageSize = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def LogList(self):
        return self._LogList

    @LogList.setter
    def LogList(self, LogList):
        self._LogList = LogList

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
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogList = params.get("LogList")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDomainPreviewRequest(AbstractModel):
    """DescribeDomainPreview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainPreviewResponse(AbstractModel):
    """DescribeDomainPreview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名概览信息
        :type Domain: :class:`tencentcloud.dnspod.v20210323.models.PreviewDetail`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Domain = None
        self._RequestId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Domain") is not None:
            self._Domain = PreviewDetail()
            self._Domain._deserialize(params.get("Domain"))
        self._RequestId = params.get("RequestId")


class DescribeDomainPurviewRequest(AbstractModel):
    """DescribeDomainPurview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainPurviewResponse(AbstractModel):
    """DescribeDomainPurview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PurviewList: 域名权限列表
        :type PurviewList: list of PurviewInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PurviewList = None
        self._RequestId = None

    @property
    def PurviewList(self):
        return self._PurviewList

    @PurviewList.setter
    def PurviewList(self, PurviewList):
        self._PurviewList = PurviewList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PurviewList") is not None:
            self._PurviewList = []
            for item in params.get("PurviewList"):
                obj = PurviewInfo()
                obj._deserialize(item)
                self._PurviewList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainRequest(AbstractModel):
    """DescribeDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainResponse(AbstractModel):
    """DescribeDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainInfo: 域名信息
        :type DomainInfo: :class:`tencentcloud.dnspod.v20210323.models.DomainInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainInfo = None
        self._RequestId = None

    @property
    def DomainInfo(self):
        return self._DomainInfo

    @DomainInfo.setter
    def DomainInfo(self, DomainInfo):
        self._DomainInfo = DomainInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self._DomainInfo = DomainInfo()
            self._DomainInfo._deserialize(params.get("DomainInfo"))
        self._RequestId = params.get("RequestId")


class DescribeDomainShareInfoRequest(AbstractModel):
    """DescribeDomainShareInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainShareInfoResponse(AbstractModel):
    """DescribeDomainShareInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ShareList: 域名共享信息
        :type ShareList: list of DomainShareInfo
        :param _Owner: 域名拥有者账号
        :type Owner: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ShareList = None
        self._Owner = None
        self._RequestId = None

    @property
    def ShareList(self):
        return self._ShareList

    @ShareList.setter
    def ShareList(self, ShareList):
        self._ShareList = ShareList

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ShareList") is not None:
            self._ShareList = []
            for item in params.get("ShareList"):
                obj = DomainShareInfo()
                obj._deserialize(item)
                self._ShareList.append(obj)
        self._Owner = params.get("Owner")
        self._RequestId = params.get("RequestId")


class DescribeDomainWhoisRequest(AbstractModel):
    """DescribeDomainWhois请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainWhoisResponse(AbstractModel):
    """DescribeDomainWhois返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Info: 域名Whois信息
        :type Info: :class:`tencentcloud.dnspod.v20210323.models.WhoisInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = WhoisInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribePackageDetailRequest(AbstractModel):
    """DescribePackageDetail请求参数结构体

    """


class DescribePackageDetailResponse(AbstractModel):
    """DescribePackageDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Info: 套餐配置详情
        :type Info: list of PackageDetailItem
        :param _LevelMap: 套餐代码列表
        :type LevelMap: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Info = None
        self._LevelMap = None
        self._RequestId = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def LevelMap(self):
        return self._LevelMap

    @LevelMap.setter
    def LevelMap(self, LevelMap):
        self._LevelMap = LevelMap

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = []
            for item in params.get("Info"):
                obj = PackageDetailItem()
                obj._deserialize(item)
                self._Info.append(obj)
        self._LevelMap = params.get("LevelMap")
        self._RequestId = params.get("RequestId")


class DescribeRecordExistExceptDefaultNSRequest(AbstractModel):
    """DescribeRecordExistExceptDefaultNS请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordExistExceptDefaultNSResponse(AbstractModel):
    """DescribeRecordExistExceptDefaultNS返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Exist: true 是 false 否
        :type Exist: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Exist = None
        self._RequestId = None

    @property
    def Exist(self):
        return self._Exist

    @Exist.setter
    def Exist(self, Exist):
        self._Exist = Exist

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Exist = params.get("Exist")
        self._RequestId = params.get("RequestId")


class DescribeRecordFilterListRequest(AbstractModel):
    """DescribeRecordFilterList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 要获取的解析记录所属的域名。
        :type Domain: str
        :param _DomainId: 要获取的解析记录所属的域名 Id，如果传了 DomainId，系统将会忽略 Domain 参数。 可以通过接口 DescribeDomainList 查到所有的 Domain 以及 DomainId。
        :type DomainId: int
        :param _SubDomain: 根据解析记录的主机头获取解析记录。默认模糊匹配。可以通过设置 IsExactSubdomain 参数为 true 进行精确查找。
        :type SubDomain: str
        :param _RecordType: 获取某些类型的解析记录，如 A，CNAME，NS，AAAA，显性URL，隐性URL，CAA，SPF等。
        :type RecordType: list of str
        :param _RecordLine: 获取某些线路ID的解析记录。可以通过接口 DescribeRecordLineList 查看当前域名允许的线路信息。
        :type RecordLine: list of str
        :param _GroupId: 获取某些分组下的解析记录时，传这个分组 Id。可以通过接口 DescribeRecordGroupList 接口 GroupId 字段获取。
        :type GroupId: list of int non-negative
        :param _Keyword: 通过关键字搜索解析记录，当前支持搜索主机头和记录值
        :type Keyword: str
        :param _SortField: 排序字段，支持 NAME，LINE，TYPE，VALUE，WEIGHT，MX，TTL，UPDATED_ON 几个字段。
NAME：解析记录的主机头
LINE：解析记录线路
TYPE：解析记录类型
VALUE：解析记录值
WEIGHT：权重
MX：MX 优先级
TTL：解析记录缓存时间
UPDATED_ON：解析记录更新时间

        :type SortField: str
        :param _SortType: 排序方式，升序：ASC，降序：DESC。默认值为ASC。
        :type SortType: str
        :param _Offset: 偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 限制数量，当前Limit最大支持3000。默认值为100。
        :type Limit: int
        :param _RecordValue: 根据解析记录的值获取解析记录
        :type RecordValue: str
        :param _RecordStatus: 根据解析记录的状态获取解析记录。可取值为 ENABLE，DISABLE。
ENABLE：正常 
DISABLE：暂停 
        :type RecordStatus: list of str
        :param _WeightBegin: 要获取解析记录权重查询区间起点。
        :type WeightBegin: int
        :param _WeightEnd: 要获取解析记录权重查询区间终点。
        :type WeightEnd: int
        :param _MXBegin: 要获取解析记录 MX 优先级查询区间起点。
        :type MXBegin: int
        :param _MXEnd: 要获取解析记录 MX 优先级查询区间终点。
        :type MXEnd: int
        :param _TTLBegin: 要获取解析记录 TTL 查询区间起点。
        :type TTLBegin: int
        :param _TTLEnd: 要获取解析记录 TTL 查询区间终点。
        :type TTLEnd: int
        :param _UpdatedAtBegin: 要获取解析记录更新时间查询区间起点。
        :type UpdatedAtBegin: str
        :param _UpdatedAtEnd: 要获取解析记录更新时间查询区间终点。
        :type UpdatedAtEnd: str
        :param _Remark: 根据解析记录的备注获取解析记录。
        :type Remark: str
        :param _IsExactSubDomain: 是否根据 Subdomain 参数进行精确查找。
        :type IsExactSubDomain: bool
        :param _ProjectId: 项目ID
        :type ProjectId: int
        """
        self._Domain = None
        self._DomainId = None
        self._SubDomain = None
        self._RecordType = None
        self._RecordLine = None
        self._GroupId = None
        self._Keyword = None
        self._SortField = None
        self._SortType = None
        self._Offset = None
        self._Limit = None
        self._RecordValue = None
        self._RecordStatus = None
        self._WeightBegin = None
        self._WeightEnd = None
        self._MXBegin = None
        self._MXEnd = None
        self._TTLBegin = None
        self._TTLEnd = None
        self._UpdatedAtBegin = None
        self._UpdatedAtEnd = None
        self._Remark = None
        self._IsExactSubDomain = None
        self._ProjectId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def SortField(self):
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortType(self):
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def RecordValue(self):
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue

    @property
    def RecordStatus(self):
        return self._RecordStatus

    @RecordStatus.setter
    def RecordStatus(self, RecordStatus):
        self._RecordStatus = RecordStatus

    @property
    def WeightBegin(self):
        return self._WeightBegin

    @WeightBegin.setter
    def WeightBegin(self, WeightBegin):
        self._WeightBegin = WeightBegin

    @property
    def WeightEnd(self):
        return self._WeightEnd

    @WeightEnd.setter
    def WeightEnd(self, WeightEnd):
        self._WeightEnd = WeightEnd

    @property
    def MXBegin(self):
        return self._MXBegin

    @MXBegin.setter
    def MXBegin(self, MXBegin):
        self._MXBegin = MXBegin

    @property
    def MXEnd(self):
        return self._MXEnd

    @MXEnd.setter
    def MXEnd(self, MXEnd):
        self._MXEnd = MXEnd

    @property
    def TTLBegin(self):
        return self._TTLBegin

    @TTLBegin.setter
    def TTLBegin(self, TTLBegin):
        self._TTLBegin = TTLBegin

    @property
    def TTLEnd(self):
        return self._TTLEnd

    @TTLEnd.setter
    def TTLEnd(self, TTLEnd):
        self._TTLEnd = TTLEnd

    @property
    def UpdatedAtBegin(self):
        return self._UpdatedAtBegin

    @UpdatedAtBegin.setter
    def UpdatedAtBegin(self, UpdatedAtBegin):
        self._UpdatedAtBegin = UpdatedAtBegin

    @property
    def UpdatedAtEnd(self):
        return self._UpdatedAtEnd

    @UpdatedAtEnd.setter
    def UpdatedAtEnd(self, UpdatedAtEnd):
        self._UpdatedAtEnd = UpdatedAtEnd

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def IsExactSubDomain(self):
        return self._IsExactSubDomain

    @IsExactSubDomain.setter
    def IsExactSubDomain(self, IsExactSubDomain):
        self._IsExactSubDomain = IsExactSubDomain

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._SubDomain = params.get("SubDomain")
        self._RecordType = params.get("RecordType")
        self._RecordLine = params.get("RecordLine")
        self._GroupId = params.get("GroupId")
        self._Keyword = params.get("Keyword")
        self._SortField = params.get("SortField")
        self._SortType = params.get("SortType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._RecordValue = params.get("RecordValue")
        self._RecordStatus = params.get("RecordStatus")
        self._WeightBegin = params.get("WeightBegin")
        self._WeightEnd = params.get("WeightEnd")
        self._MXBegin = params.get("MXBegin")
        self._MXEnd = params.get("MXEnd")
        self._TTLBegin = params.get("TTLBegin")
        self._TTLEnd = params.get("TTLEnd")
        self._UpdatedAtBegin = params.get("UpdatedAtBegin")
        self._UpdatedAtEnd = params.get("UpdatedAtEnd")
        self._Remark = params.get("Remark")
        self._IsExactSubDomain = params.get("IsExactSubDomain")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordFilterListResponse(AbstractModel):
    """DescribeRecordFilterList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordCountInfo: 记录的数量统计信息
        :type RecordCountInfo: :class:`tencentcloud.dnspod.v20210323.models.RecordCountInfo`
        :param _RecordList: 获取的记录列表
        :type RecordList: list of RecordListItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordCountInfo = None
        self._RecordList = None
        self._RequestId = None

    @property
    def RecordCountInfo(self):
        return self._RecordCountInfo

    @RecordCountInfo.setter
    def RecordCountInfo(self, RecordCountInfo):
        self._RecordCountInfo = RecordCountInfo

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RecordCountInfo") is not None:
            self._RecordCountInfo = RecordCountInfo()
            self._RecordCountInfo._deserialize(params.get("RecordCountInfo"))
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = RecordListItem()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordGroupListRequest(AbstractModel):
    """DescribeRecordGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        :param _Offset: 分页开始位置
        :type Offset: int
        :param _Limit: 分页每页数
        :type Limit: int
        """
        self._Domain = None
        self._DomainId = None
        self._Offset = None
        self._Limit = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordGroupListResponse(AbstractModel):
    """DescribeRecordGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupList: 分组列表
        :type GroupList: list of RecordGroupInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupList = None
        self._RequestId = None

    @property
    def GroupList(self):
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self._GroupList = []
            for item in params.get("GroupList"):
                obj = RecordGroupInfo()
                obj._deserialize(item)
                self._GroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordLineListRequest(AbstractModel):
    """DescribeRecordLineList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名。
        :type Domain: str
        :param _DomainGrade: 域名等级。
+ 旧套餐：D_FREE、D_PLUS、D_EXTRA、D_EXPERT、D_ULTRA 分别对应免费套餐、个人豪华、企业1、企业2、企业3。
+ 新套餐：DP_FREE、DP_PLUS、DP_EXTRA、DP_EXPERT、DP_ULTRA 分别对应新免费、个人专业版、企业创业版、企业标准版、企业旗舰版。
        :type DomainGrade: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._DomainGrade = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainGrade(self):
        return self._DomainGrade

    @DomainGrade.setter
    def DomainGrade(self, DomainGrade):
        self._DomainGrade = DomainGrade

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainGrade = params.get("DomainGrade")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordLineListResponse(AbstractModel):
    """DescribeRecordLineList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LineList: 线路列表。
        :type LineList: list of LineInfo
        :param _LineGroupList: 线路分组列表。
        :type LineGroupList: list of LineGroupInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LineList = None
        self._LineGroupList = None
        self._RequestId = None

    @property
    def LineList(self):
        return self._LineList

    @LineList.setter
    def LineList(self, LineList):
        self._LineList = LineList

    @property
    def LineGroupList(self):
        return self._LineGroupList

    @LineGroupList.setter
    def LineGroupList(self, LineGroupList):
        self._LineGroupList = LineGroupList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LineList") is not None:
            self._LineList = []
            for item in params.get("LineList"):
                obj = LineInfo()
                obj._deserialize(item)
                self._LineList.append(obj)
        if params.get("LineGroupList") is not None:
            self._LineGroupList = []
            for item in params.get("LineGroupList"):
                obj = LineGroupInfo()
                obj._deserialize(item)
                self._LineGroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordListRequest(AbstractModel):
    """DescribeRecordList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 要获取的解析记录所属的域名
        :type Domain: str
        :param _DomainId: 要获取的解析记录所属的域名Id，如果传了DomainId，系统将会忽略Domain参数。 可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        :param _Subdomain: 解析记录的主机头，如果传了此参数，则只会返回此主机头对应的解析记录
        :type Subdomain: str
        :param _RecordType: 获取某种类型的解析记录，如 A，CNAME，NS，AAAA，显性URL，隐性URL，CAA，SPF等
        :type RecordType: str
        :param _RecordLine: 获取某条线路名称的解析记录。可以通过接口DescribeRecordLineList查看当前域名允许的线路信息
        :type RecordLine: str
        :param _RecordLineId: 获取某个线路Id对应的解析记录，如果传RecordLineId，系统会忽略RecordLine参数。可以通过接口DescribeRecordLineList查看当前域名允许的线路信息
        :type RecordLineId: str
        :param _GroupId: 获取某个分组下的解析记录时，传这个分组Id。
        :type GroupId: int
        :param _Keyword: 通过关键字搜索解析记录，当前支持搜索主机头和记录值
        :type Keyword: str
        :param _SortField: 排序字段，支持 name,line,type,value,weight,mx,ttl,updated_on 几个字段。
        :type SortField: str
        :param _SortType: 排序方式，正序：ASC，逆序：DESC。默认值为ASC。
        :type SortType: str
        :param _Offset: 偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 限制数量，当前Limit最大支持3000。默认值为100。
        :type Limit: int
        """
        self._Domain = None
        self._DomainId = None
        self._Subdomain = None
        self._RecordType = None
        self._RecordLine = None
        self._RecordLineId = None
        self._GroupId = None
        self._Keyword = None
        self._SortField = None
        self._SortType = None
        self._Offset = None
        self._Limit = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Subdomain(self):
        return self._Subdomain

    @Subdomain.setter
    def Subdomain(self, Subdomain):
        self._Subdomain = Subdomain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def RecordLineId(self):
        return self._RecordLineId

    @RecordLineId.setter
    def RecordLineId(self, RecordLineId):
        self._RecordLineId = RecordLineId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def SortField(self):
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortType(self):
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._Subdomain = params.get("Subdomain")
        self._RecordType = params.get("RecordType")
        self._RecordLine = params.get("RecordLine")
        self._RecordLineId = params.get("RecordLineId")
        self._GroupId = params.get("GroupId")
        self._Keyword = params.get("Keyword")
        self._SortField = params.get("SortField")
        self._SortType = params.get("SortType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordListResponse(AbstractModel):
    """DescribeRecordList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordCountInfo: 记录的数量统计信息
        :type RecordCountInfo: :class:`tencentcloud.dnspod.v20210323.models.RecordCountInfo`
        :param _RecordList: 获取的记录列表
        :type RecordList: list of RecordListItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordCountInfo = None
        self._RecordList = None
        self._RequestId = None

    @property
    def RecordCountInfo(self):
        return self._RecordCountInfo

    @RecordCountInfo.setter
    def RecordCountInfo(self, RecordCountInfo):
        self._RecordCountInfo = RecordCountInfo

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RecordCountInfo") is not None:
            self._RecordCountInfo = RecordCountInfo()
            self._RecordCountInfo._deserialize(params.get("RecordCountInfo"))
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = RecordListItem()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordRequest(AbstractModel):
    """DescribeRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _RecordId: 记录 ID 。可以通过接口DescribeRecordList查到所有的解析记录列表以及对应的RecordId
        :type RecordId: int
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._RecordId = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RecordId = params.get("RecordId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordResponse(AbstractModel):
    """DescribeRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordInfo: 记录信息
        :type RecordInfo: :class:`tencentcloud.dnspod.v20210323.models.RecordInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordInfo = None
        self._RequestId = None

    @property
    def RecordInfo(self):
        return self._RecordInfo

    @RecordInfo.setter
    def RecordInfo(self, RecordInfo):
        self._RecordInfo = RecordInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RecordInfo") is not None:
            self._RecordInfo = RecordInfo()
            self._RecordInfo._deserialize(params.get("RecordInfo"))
        self._RequestId = params.get("RequestId")


class DescribeRecordSnapshotRollbackResultRequest(AbstractModel):
    """DescribeRecordSnapshotRollbackResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _JobId: 回滚任务 ID
        :type JobId: int
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self._Domain = None
        self._JobId = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._JobId = params.get("JobId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordSnapshotRollbackResultResponse(AbstractModel):
    """DescribeRecordSnapshotRollbackResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 回滚任务 ID
        :type JobId: int
        :param _Status: 回滚状态
        :type Status: str
        :param _FailedRecordList: 失败的记录信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedRecordList: list of SnapshotRecord
        :param _Domain: 所属域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _Progress: 回滚进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        :param _LeftMinutes: 回滚剩余时间（单位：分钟）
注意：此字段可能返回 null，表示取不到有效值。
        :type LeftMinutes: int
        :param _Total: 总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Failed: 失败记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type Failed: int
        :param _Success: 成功记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type Success: int
        :param _CosUrl: 快照下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CosUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._Status = None
        self._FailedRecordList = None
        self._Domain = None
        self._Progress = None
        self._LeftMinutes = None
        self._Total = None
        self._Failed = None
        self._Success = None
        self._CosUrl = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailedRecordList(self):
        return self._FailedRecordList

    @FailedRecordList.setter
    def FailedRecordList(self, FailedRecordList):
        self._FailedRecordList = FailedRecordList

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def LeftMinutes(self):
        return self._LeftMinutes

    @LeftMinutes.setter
    def LeftMinutes(self, LeftMinutes):
        self._LeftMinutes = LeftMinutes

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Failed(self):
        return self._Failed

    @Failed.setter
    def Failed(self, Failed):
        self._Failed = Failed

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def CosUrl(self):
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Status = params.get("Status")
        if params.get("FailedRecordList") is not None:
            self._FailedRecordList = []
            for item in params.get("FailedRecordList"):
                obj = SnapshotRecord()
                obj._deserialize(item)
                self._FailedRecordList.append(obj)
        self._Domain = params.get("Domain")
        self._Progress = params.get("Progress")
        self._LeftMinutes = params.get("LeftMinutes")
        self._Total = params.get("Total")
        self._Failed = params.get("Failed")
        self._Success = params.get("Success")
        self._CosUrl = params.get("CosUrl")
        self._RequestId = params.get("RequestId")


class DescribeRecordTypeRequest(AbstractModel):
    """DescribeRecordType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainGrade: 域名等级。
+ 旧套餐：D_FREE、D_PLUS、D_EXTRA、D_EXPERT、D_ULTRA 分别对应免费套餐、个人豪华、企业1、企业2、企业3。
+ 新套餐：DP_FREE、DP_PLUS、DP_EXTRA、DP_EXPERT、DP_ULTRA 分别对应新免费、个人专业版、企业创业版、企业标准版、企业旗舰版。
        :type DomainGrade: str
        """
        self._DomainGrade = None

    @property
    def DomainGrade(self):
        return self._DomainGrade

    @DomainGrade.setter
    def DomainGrade(self, DomainGrade):
        self._DomainGrade = DomainGrade


    def _deserialize(self, params):
        self._DomainGrade = params.get("DomainGrade")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordTypeResponse(AbstractModel):
    """DescribeRecordType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TypeList: 记录类型列表
        :type TypeList: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TypeList = None
        self._RequestId = None

    @property
    def TypeList(self):
        return self._TypeList

    @TypeList.setter
    def TypeList(self, TypeList):
        self._TypeList = TypeList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TypeList = params.get("TypeList")
        self._RequestId = params.get("RequestId")


class DescribeSnapshotConfigRequest(AbstractModel):
    """DescribeSnapshotConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self._Domain = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotConfigResponse(AbstractModel):
    """DescribeSnapshotConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotConfig: 解析快照配置
        :type SnapshotConfig: :class:`tencentcloud.dnspod.v20210323.models.SnapshotConfig`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SnapshotConfig = None
        self._RequestId = None

    @property
    def SnapshotConfig(self):
        return self._SnapshotConfig

    @SnapshotConfig.setter
    def SnapshotConfig(self, SnapshotConfig):
        self._SnapshotConfig = SnapshotConfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SnapshotConfig") is not None:
            self._SnapshotConfig = SnapshotConfig()
            self._SnapshotConfig._deserialize(params.get("SnapshotConfig"))
        self._RequestId = params.get("RequestId")


class DescribeSnapshotListRequest(AbstractModel):
    """DescribeSnapshotList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self._Domain = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotListResponse(AbstractModel):
    """DescribeSnapshotList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Info: 分页信息
        :type Info: :class:`tencentcloud.dnspod.v20210323.models.SnapshotPageInfo`
        :param _SnapshotList: 快照列表
        :type SnapshotList: list of SnapshotInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Info = None
        self._SnapshotList = None
        self._RequestId = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def SnapshotList(self):
        return self._SnapshotList

    @SnapshotList.setter
    def SnapshotList(self, SnapshotList):
        self._SnapshotList = SnapshotList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = SnapshotPageInfo()
            self._Info._deserialize(params.get("Info"))
        if params.get("SnapshotList") is not None:
            self._SnapshotList = []
            for item in params.get("SnapshotList"):
                obj = SnapshotInfo()
                obj._deserialize(item)
                self._SnapshotList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSnapshotRollbackResultRequest(AbstractModel):
    """DescribeSnapshotRollbackResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _TaskId: 快照回滚任务 ID
        :type TaskId: int
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self._Domain = None
        self._TaskId = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._TaskId = params.get("TaskId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotRollbackResultResponse(AbstractModel):
    """DescribeSnapshotRollbackResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 快照所属域名
        :type Domain: str
        :param _LeftMinutes: 回滚剩余时间（分钟）
        :type LeftMinutes: int
        :param _Progress: 回滚进度百分比
        :type Progress: int
        :param _SnapshotId: 快照 ID
        :type SnapshotId: str
        :param _Status: 回滚状态
        :type Status: str
        :param _TaskId: 快照回滚任务 ID
        :type TaskId: int
        :param _Success: 成功数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Success: int
        :param _Failed: 失败数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Failed: int
        :param _Total: 总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _FailedRecordList: 失败详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedRecordList: list of SnapshotRecord
        :param _CosUrl: 快照的下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CosUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Domain = None
        self._LeftMinutes = None
        self._Progress = None
        self._SnapshotId = None
        self._Status = None
        self._TaskId = None
        self._Success = None
        self._Failed = None
        self._Total = None
        self._FailedRecordList = None
        self._CosUrl = None
        self._RequestId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LeftMinutes(self):
        return self._LeftMinutes

    @LeftMinutes.setter
    def LeftMinutes(self, LeftMinutes):
        self._LeftMinutes = LeftMinutes

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def Failed(self):
        return self._Failed

    @Failed.setter
    def Failed(self, Failed):
        self._Failed = Failed

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def FailedRecordList(self):
        return self._FailedRecordList

    @FailedRecordList.setter
    def FailedRecordList(self, FailedRecordList):
        self._FailedRecordList = FailedRecordList

    @property
    def CosUrl(self):
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._LeftMinutes = params.get("LeftMinutes")
        self._Progress = params.get("Progress")
        self._SnapshotId = params.get("SnapshotId")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._Success = params.get("Success")
        self._Failed = params.get("Failed")
        self._Total = params.get("Total")
        if params.get("FailedRecordList") is not None:
            self._FailedRecordList = []
            for item in params.get("FailedRecordList"):
                obj = SnapshotRecord()
                obj._deserialize(item)
                self._FailedRecordList.append(obj)
        self._CosUrl = params.get("CosUrl")
        self._RequestId = params.get("RequestId")


class DescribeSnapshotRollbackTaskRequest(AbstractModel):
    """DescribeSnapshotRollbackTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self._Domain = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotRollbackTaskResponse(AbstractModel):
    """DescribeSnapshotRollbackTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 快照所属域名
        :type Domain: str
        :param _SnapshotId: 快照 ID
        :type SnapshotId: str
        :param _Status: 回滚状态
        :type Status: str
        :param _TaskId: 快照回滚任务 ID
        :type TaskId: int
        :param _RecordCount: 总数量
        :type RecordCount: int
        :param _CreatedOn: 开始回滚时间
        :type CreatedOn: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Domain = None
        self._SnapshotId = None
        self._Status = None
        self._TaskId = None
        self._RecordCount = None
        self._CreatedOn = None
        self._RequestId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RecordCount(self):
        return self._RecordCount

    @RecordCount.setter
    def RecordCount(self, RecordCount):
        self._RecordCount = RecordCount

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._SnapshotId = params.get("SnapshotId")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._RecordCount = params.get("RecordCount")
        self._CreatedOn = params.get("CreatedOn")
        self._RequestId = params.get("RequestId")


class DescribeSubdomainAnalyticsRequest(AbstractModel):
    """DescribeSubdomainAnalytics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 要查询解析量的域名
        :type Domain: str
        :param _StartDate: 查询的开始时间，格式：YYYY-MM-DD
        :type StartDate: str
        :param _EndDate: 查询的结束时间，格式：YYYY-MM-DD
        :type EndDate: str
        :param _Subdomain: 要查询解析量的子域名
        :type Subdomain: str
        :param _DnsFormat: DATE:按天维度统计 HOUR:按小时维度统计
        :type DnsFormat: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._StartDate = None
        self._EndDate = None
        self._Subdomain = None
        self._DnsFormat = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Subdomain(self):
        return self._Subdomain

    @Subdomain.setter
    def Subdomain(self, Subdomain):
        self._Subdomain = Subdomain

    @property
    def DnsFormat(self):
        return self._DnsFormat

    @DnsFormat.setter
    def DnsFormat(self, DnsFormat):
        self._DnsFormat = DnsFormat

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Subdomain = params.get("Subdomain")
        self._DnsFormat = params.get("DnsFormat")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubdomainAnalyticsResponse(AbstractModel):
    """DescribeSubdomainAnalytics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 当前统计维度解析量小计
        :type Data: list of DomainAnalyticsDetail
        :param _Info: 子域名解析量统计查询信息
        :type Info: :class:`tencentcloud.dnspod.v20210323.models.SubdomainAnalyticsInfo`
        :param _AliasData: 子域名别名解析量统计信息
        :type AliasData: list of SubdomainAliasAnalyticsItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Info = None
        self._AliasData = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def AliasData(self):
        return self._AliasData

    @AliasData.setter
    def AliasData(self, AliasData):
        self._AliasData = AliasData

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
                obj = DomainAnalyticsDetail()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("Info") is not None:
            self._Info = SubdomainAnalyticsInfo()
            self._Info._deserialize(params.get("Info"))
        if params.get("AliasData") is not None:
            self._AliasData = []
            for item in params.get("AliasData"):
                obj = SubdomainAliasAnalyticsItem()
                obj._deserialize(item)
                self._AliasData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserDetailRequest(AbstractModel):
    """DescribeUserDetail请求参数结构体

    """


class DescribeUserDetailResponse(AbstractModel):
    """DescribeUserDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserInfo: 账户信息
        :type UserInfo: :class:`tencentcloud.dnspod.v20210323.models.UserInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserInfo = None
        self._RequestId = None

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = UserInfo()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._RequestId = params.get("RequestId")


class DescribeVASStatisticRequest(AbstractModel):
    """DescribeVASStatistic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainId: 域名ID
        :type DomainId: int
        """
        self._DomainId = None

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVASStatisticResponse(AbstractModel):
    """DescribeVASStatistic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VASList: 增值服务用量列表
        :type VASList: list of VASStatisticItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VASList = None
        self._RequestId = None

    @property
    def VASList(self):
        return self._VASList

    @VASList.setter
    def VASList(self, VASList):
        self._VASList = VASList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("VASList") is not None:
            self._VASList = []
            for item in params.get("VASList"):
                obj = VASStatisticItem()
                obj._deserialize(item)
                self._VASList.append(obj)
        self._RequestId = params.get("RequestId")


class DomainAliasAnalyticsItem(AbstractModel):
    """域名别名解析量统计信息

    """

    def __init__(self):
        r"""
        :param _Info: 域名解析量统计查询信息
        :type Info: :class:`tencentcloud.dnspod.v20210323.models.DomainAnalyticsInfo`
        :param _Data: 当前统计维度解析量小计
        :type Data: list of DomainAnalyticsDetail
        """
        self._Info = None
        self._Data = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = DomainAnalyticsInfo()
            self._Info._deserialize(params.get("Info"))
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DomainAnalyticsDetail()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainAliasInfo(AbstractModel):
    """域名别名信息

    """

    def __init__(self):
        r"""
        :param _Id: 域名别名ID
        :type Id: int
        :param _DomainAlias: 域名别名
        :type DomainAlias: str
        :param _Status: 别名状态：1-DNS不正确；2-正常；3-封禁。
        :type Status: int
        """
        self._Id = None
        self._DomainAlias = None
        self._Status = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DomainAlias(self):
        return self._DomainAlias

    @DomainAlias.setter
    def DomainAlias(self, DomainAlias):
        self._DomainAlias = DomainAlias

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DomainAlias = params.get("DomainAlias")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainAnalyticsDetail(AbstractModel):
    """当前统计维度解析量小计

    """

    def __init__(self):
        r"""
        :param _Num: 当前统计维度解析量小计
        :type Num: int
        :param _DateKey: 按天统计时，为统计日期
        :type DateKey: str
        :param _HourKey: 按小时统计时，为统计的当前时间的小时数(0-23)，例：HourKey为23时，统计周期为22点-23点的解析量
注意：此字段可能返回 null，表示取不到有效值。
        :type HourKey: int
        """
        self._Num = None
        self._DateKey = None
        self._HourKey = None

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def DateKey(self):
        return self._DateKey

    @DateKey.setter
    def DateKey(self, DateKey):
        self._DateKey = DateKey

    @property
    def HourKey(self):
        return self._HourKey

    @HourKey.setter
    def HourKey(self, HourKey):
        self._HourKey = HourKey


    def _deserialize(self, params):
        self._Num = params.get("Num")
        self._DateKey = params.get("DateKey")
        self._HourKey = params.get("HourKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainAnalyticsInfo(AbstractModel):
    """域名解析量统计查询信息

    """

    def __init__(self):
        r"""
        :param _DnsFormat: DATE:按天维度统计 HOUR:按小时维度统计
        :type DnsFormat: str
        :param _DnsTotal: 当前统计周期解析量总计
        :type DnsTotal: int
        :param _Domain: 当前查询的域名
        :type Domain: str
        :param _StartDate: 当前统计周期开始时间
        :type StartDate: str
        :param _EndDate: 当前统计周期结束时间
        :type EndDate: str
        """
        self._DnsFormat = None
        self._DnsTotal = None
        self._Domain = None
        self._StartDate = None
        self._EndDate = None

    @property
    def DnsFormat(self):
        return self._DnsFormat

    @DnsFormat.setter
    def DnsFormat(self, DnsFormat):
        self._DnsFormat = DnsFormat

    @property
    def DnsTotal(self):
        return self._DnsTotal

    @DnsTotal.setter
    def DnsTotal(self, DnsTotal):
        self._DnsTotal = DnsTotal

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._DnsFormat = params.get("DnsFormat")
        self._DnsTotal = params.get("DnsTotal")
        self._Domain = params.get("Domain")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainCountInfo(AbstractModel):
    """列表页分页统计信息

    """

    def __init__(self):
        r"""
        :param _DomainTotal: 符合条件的域名数量
        :type DomainTotal: int
        :param _AllTotal: 用户可以查看的所有域名数量
        :type AllTotal: int
        :param _MineTotal: 用户账号添加的域名数量
        :type MineTotal: int
        :param _ShareTotal: 共享给用户的域名数量
        :type ShareTotal: int
        :param _VipTotal: 付费域名数量
        :type VipTotal: int
        :param _PauseTotal: 暂停的域名数量
        :type PauseTotal: int
        :param _ErrorTotal: dns设置错误的域名数量
        :type ErrorTotal: int
        :param _LockTotal: 锁定的域名数量
        :type LockTotal: int
        :param _SpamTotal: 封禁的域名数量
        :type SpamTotal: int
        :param _VipExpire: 30天内即将到期的域名数量
        :type VipExpire: int
        :param _ShareOutTotal: 分享给其它人的域名数量
        :type ShareOutTotal: int
        :param _GroupTotal: 指定分组内的域名数量
        :type GroupTotal: int
        """
        self._DomainTotal = None
        self._AllTotal = None
        self._MineTotal = None
        self._ShareTotal = None
        self._VipTotal = None
        self._PauseTotal = None
        self._ErrorTotal = None
        self._LockTotal = None
        self._SpamTotal = None
        self._VipExpire = None
        self._ShareOutTotal = None
        self._GroupTotal = None

    @property
    def DomainTotal(self):
        return self._DomainTotal

    @DomainTotal.setter
    def DomainTotal(self, DomainTotal):
        self._DomainTotal = DomainTotal

    @property
    def AllTotal(self):
        return self._AllTotal

    @AllTotal.setter
    def AllTotal(self, AllTotal):
        self._AllTotal = AllTotal

    @property
    def MineTotal(self):
        return self._MineTotal

    @MineTotal.setter
    def MineTotal(self, MineTotal):
        self._MineTotal = MineTotal

    @property
    def ShareTotal(self):
        return self._ShareTotal

    @ShareTotal.setter
    def ShareTotal(self, ShareTotal):
        self._ShareTotal = ShareTotal

    @property
    def VipTotal(self):
        return self._VipTotal

    @VipTotal.setter
    def VipTotal(self, VipTotal):
        self._VipTotal = VipTotal

    @property
    def PauseTotal(self):
        return self._PauseTotal

    @PauseTotal.setter
    def PauseTotal(self, PauseTotal):
        self._PauseTotal = PauseTotal

    @property
    def ErrorTotal(self):
        return self._ErrorTotal

    @ErrorTotal.setter
    def ErrorTotal(self, ErrorTotal):
        self._ErrorTotal = ErrorTotal

    @property
    def LockTotal(self):
        return self._LockTotal

    @LockTotal.setter
    def LockTotal(self, LockTotal):
        self._LockTotal = LockTotal

    @property
    def SpamTotal(self):
        return self._SpamTotal

    @SpamTotal.setter
    def SpamTotal(self, SpamTotal):
        self._SpamTotal = SpamTotal

    @property
    def VipExpire(self):
        return self._VipExpire

    @VipExpire.setter
    def VipExpire(self, VipExpire):
        self._VipExpire = VipExpire

    @property
    def ShareOutTotal(self):
        return self._ShareOutTotal

    @ShareOutTotal.setter
    def ShareOutTotal(self, ShareOutTotal):
        self._ShareOutTotal = ShareOutTotal

    @property
    def GroupTotal(self):
        return self._GroupTotal

    @GroupTotal.setter
    def GroupTotal(self, GroupTotal):
        self._GroupTotal = GroupTotal


    def _deserialize(self, params):
        self._DomainTotal = params.get("DomainTotal")
        self._AllTotal = params.get("AllTotal")
        self._MineTotal = params.get("MineTotal")
        self._ShareTotal = params.get("ShareTotal")
        self._VipTotal = params.get("VipTotal")
        self._PauseTotal = params.get("PauseTotal")
        self._ErrorTotal = params.get("ErrorTotal")
        self._LockTotal = params.get("LockTotal")
        self._SpamTotal = params.get("SpamTotal")
        self._VipExpire = params.get("VipExpire")
        self._ShareOutTotal = params.get("ShareOutTotal")
        self._GroupTotal = params.get("GroupTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainCreateInfo(AbstractModel):
    """域名信息（创建域名时返回）

    """

    def __init__(self):
        r"""
        :param _Id: 域名ID
        :type Id: int
        :param _Domain: 域名
        :type Domain: str
        :param _Punycode: 域名的punycode
        :type Punycode: str
        :param _GradeNsList: 域名的NS列表
        :type GradeNsList: list of str
        """
        self._Id = None
        self._Domain = None
        self._Punycode = None
        self._GradeNsList = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Punycode(self):
        return self._Punycode

    @Punycode.setter
    def Punycode(self, Punycode):
        self._Punycode = Punycode

    @property
    def GradeNsList(self):
        return self._GradeNsList

    @GradeNsList.setter
    def GradeNsList(self, GradeNsList):
        self._GradeNsList = GradeNsList


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Domain = params.get("Domain")
        self._Punycode = params.get("Punycode")
        self._GradeNsList = params.get("GradeNsList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainInfo(AbstractModel):
    """域名详情

    """

    def __init__(self):
        r"""
        :param _DomainId: 域名ID
        :type DomainId: int
        :param _Status: 域名状态
        :type Status: str
        :param _Grade: 域名套餐等级
        :type Grade: str
        :param _GroupId: 域名分组ID
        :type GroupId: int
        :param _IsMark: 是否星标域名
        :type IsMark: str
        :param _TTL: TTL(DNS记录缓存时间)
        :type TTL: int
        :param _CnameSpeedup: cname加速启用状态
        :type CnameSpeedup: str
        :param _Remark: 域名备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _Punycode: 域名Punycode
        :type Punycode: str
        :param _DnsStatus: 域名DNS状态
        :type DnsStatus: str
        :param _DnspodNsList: 域名的NS列表
        :type DnspodNsList: list of str
        :param _Domain: 域名
        :type Domain: str
        :param _GradeLevel: 域名等级代号
        :type GradeLevel: int
        :param _UserId: 域名所属的用户ID
        :type UserId: int
        :param _IsVip: 是否为付费域名
        :type IsVip: str
        :param _Owner: 域名所有者的账号
        :type Owner: str
        :param _GradeTitle: 域名等级的描述
        :type GradeTitle: str
        :param _CreatedOn: 域名创建时间
        :type CreatedOn: str
        :param _UpdatedOn: 最后操作时间
        :type UpdatedOn: str
        :param _Uin: 腾讯云账户Uin
        :type Uin: str
        :param _ActualNsList: 域名实际使用的NS列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ActualNsList: list of str
        :param _RecordCount: 域名的记录数量
        :type RecordCount: int
        :param _OwnerNick: 域名所有者的账户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerNick: str
        :param _IsGracePeriod: 是否在付费套餐宽限期
注意：此字段可能返回 null，表示取不到有效值。
        :type IsGracePeriod: str
        :param _VipBuffered: 是否在付费套餐缓冲期
注意：此字段可能返回 null，表示取不到有效值。
        :type VipBuffered: str
        :param _VipStartAt: VIP套餐有效期开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type VipStartAt: str
        :param _VipEndAt: VIP套餐有效期结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type VipEndAt: str
        :param _VipAutoRenew: VIP套餐自动续费标识。可能的值为：default-默认；no-不自动续费；yes-自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type VipAutoRenew: str
        :param _VipResourceId: VIP套餐资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VipResourceId: str
        :param _IsSubDomain: 是否是子域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSubDomain: bool
        :param _TagList: 域名关联的标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of TagItem
        :param _SearchEnginePush: 是否启用搜索引擎推送
        :type SearchEnginePush: str
        """
        self._DomainId = None
        self._Status = None
        self._Grade = None
        self._GroupId = None
        self._IsMark = None
        self._TTL = None
        self._CnameSpeedup = None
        self._Remark = None
        self._Punycode = None
        self._DnsStatus = None
        self._DnspodNsList = None
        self._Domain = None
        self._GradeLevel = None
        self._UserId = None
        self._IsVip = None
        self._Owner = None
        self._GradeTitle = None
        self._CreatedOn = None
        self._UpdatedOn = None
        self._Uin = None
        self._ActualNsList = None
        self._RecordCount = None
        self._OwnerNick = None
        self._IsGracePeriod = None
        self._VipBuffered = None
        self._VipStartAt = None
        self._VipEndAt = None
        self._VipAutoRenew = None
        self._VipResourceId = None
        self._IsSubDomain = None
        self._TagList = None
        self._SearchEnginePush = None

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Grade(self):
        return self._Grade

    @Grade.setter
    def Grade(self, Grade):
        self._Grade = Grade

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def IsMark(self):
        return self._IsMark

    @IsMark.setter
    def IsMark(self, IsMark):
        self._IsMark = IsMark

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def CnameSpeedup(self):
        return self._CnameSpeedup

    @CnameSpeedup.setter
    def CnameSpeedup(self, CnameSpeedup):
        self._CnameSpeedup = CnameSpeedup

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Punycode(self):
        return self._Punycode

    @Punycode.setter
    def Punycode(self, Punycode):
        self._Punycode = Punycode

    @property
    def DnsStatus(self):
        return self._DnsStatus

    @DnsStatus.setter
    def DnsStatus(self, DnsStatus):
        self._DnsStatus = DnsStatus

    @property
    def DnspodNsList(self):
        return self._DnspodNsList

    @DnspodNsList.setter
    def DnspodNsList(self, DnspodNsList):
        self._DnspodNsList = DnspodNsList

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def GradeLevel(self):
        return self._GradeLevel

    @GradeLevel.setter
    def GradeLevel(self, GradeLevel):
        self._GradeLevel = GradeLevel

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def IsVip(self):
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def GradeTitle(self):
        return self._GradeTitle

    @GradeTitle.setter
    def GradeTitle(self, GradeTitle):
        self._GradeTitle = GradeTitle

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ActualNsList(self):
        return self._ActualNsList

    @ActualNsList.setter
    def ActualNsList(self, ActualNsList):
        self._ActualNsList = ActualNsList

    @property
    def RecordCount(self):
        return self._RecordCount

    @RecordCount.setter
    def RecordCount(self, RecordCount):
        self._RecordCount = RecordCount

    @property
    def OwnerNick(self):
        return self._OwnerNick

    @OwnerNick.setter
    def OwnerNick(self, OwnerNick):
        self._OwnerNick = OwnerNick

    @property
    def IsGracePeriod(self):
        return self._IsGracePeriod

    @IsGracePeriod.setter
    def IsGracePeriod(self, IsGracePeriod):
        self._IsGracePeriod = IsGracePeriod

    @property
    def VipBuffered(self):
        return self._VipBuffered

    @VipBuffered.setter
    def VipBuffered(self, VipBuffered):
        self._VipBuffered = VipBuffered

    @property
    def VipStartAt(self):
        return self._VipStartAt

    @VipStartAt.setter
    def VipStartAt(self, VipStartAt):
        self._VipStartAt = VipStartAt

    @property
    def VipEndAt(self):
        return self._VipEndAt

    @VipEndAt.setter
    def VipEndAt(self, VipEndAt):
        self._VipEndAt = VipEndAt

    @property
    def VipAutoRenew(self):
        return self._VipAutoRenew

    @VipAutoRenew.setter
    def VipAutoRenew(self, VipAutoRenew):
        self._VipAutoRenew = VipAutoRenew

    @property
    def VipResourceId(self):
        return self._VipResourceId

    @VipResourceId.setter
    def VipResourceId(self, VipResourceId):
        self._VipResourceId = VipResourceId

    @property
    def IsSubDomain(self):
        return self._IsSubDomain

    @IsSubDomain.setter
    def IsSubDomain(self, IsSubDomain):
        self._IsSubDomain = IsSubDomain

    @property
    def TagList(self):
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def SearchEnginePush(self):
        return self._SearchEnginePush

    @SearchEnginePush.setter
    def SearchEnginePush(self, SearchEnginePush):
        self._SearchEnginePush = SearchEnginePush


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._Status = params.get("Status")
        self._Grade = params.get("Grade")
        self._GroupId = params.get("GroupId")
        self._IsMark = params.get("IsMark")
        self._TTL = params.get("TTL")
        self._CnameSpeedup = params.get("CnameSpeedup")
        self._Remark = params.get("Remark")
        self._Punycode = params.get("Punycode")
        self._DnsStatus = params.get("DnsStatus")
        self._DnspodNsList = params.get("DnspodNsList")
        self._Domain = params.get("Domain")
        self._GradeLevel = params.get("GradeLevel")
        self._UserId = params.get("UserId")
        self._IsVip = params.get("IsVip")
        self._Owner = params.get("Owner")
        self._GradeTitle = params.get("GradeTitle")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        self._Uin = params.get("Uin")
        self._ActualNsList = params.get("ActualNsList")
        self._RecordCount = params.get("RecordCount")
        self._OwnerNick = params.get("OwnerNick")
        self._IsGracePeriod = params.get("IsGracePeriod")
        self._VipBuffered = params.get("VipBuffered")
        self._VipStartAt = params.get("VipStartAt")
        self._VipEndAt = params.get("VipEndAt")
        self._VipAutoRenew = params.get("VipAutoRenew")
        self._VipResourceId = params.get("VipResourceId")
        self._IsSubDomain = params.get("IsSubDomain")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagItem()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._SearchEnginePush = params.get("SearchEnginePush")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainListItem(AbstractModel):
    """域名列表元素

    """

    def __init__(self):
        r"""
        :param _DomainId: 系统分配给域名的唯一标识
        :type DomainId: int
        :param _Name: 域名的原始格式
        :type Name: str
        :param _Status: 域名的状态，正常：ENABLE，暂停：PAUSE，封禁：SPAM
        :type Status: str
        :param _TTL: 域名默认的解析记录默认TTL值
        :type TTL: int
        :param _CNAMESpeedup: 是否开启CNAME加速，开启：ENABLE，未开启：DISABLE
        :type CNAMESpeedup: str
        :param _DNSStatus: DNS 设置状态，错误：DNSERROR，正常：空字符串
        :type DNSStatus: str
        :param _Grade: 域名的套餐等级代码
        :type Grade: str
        :param _GroupId: 域名所属的分组Id
        :type GroupId: int
        :param _SearchEnginePush: 是否开启搜索引擎推送优化，是：YES，否：NO
        :type SearchEnginePush: str
        :param _Remark: 域名备注说明
        :type Remark: str
        :param _Punycode: 经过punycode编码后的域名格式
        :type Punycode: str
        :param _EffectiveDNS: 系统为域名分配的有效DNS
        :type EffectiveDNS: list of str
        :param _GradeLevel: 域名套餐等级对应的序号
        :type GradeLevel: int
        :param _GradeTitle: 套餐名称
        :type GradeTitle: str
        :param _IsVip: 是否是付费套餐
        :type IsVip: str
        :param _VipStartAt: 付费套餐开通时间
        :type VipStartAt: str
        :param _VipEndAt: 付费套餐到期时间
        :type VipEndAt: str
        :param _VipAutoRenew: 域名是否开通VIP自动续费，是：YES，否：NO，默认：DEFAULT
        :type VipAutoRenew: str
        :param _RecordCount: 域名下的记录数量
        :type RecordCount: int
        :param _CreatedOn: 域名添加时间
        :type CreatedOn: str
        :param _UpdatedOn: 域名更新时间
        :type UpdatedOn: str
        :param _Owner: 域名所属账号
        :type Owner: str
        :param _TagList: 域名关联的标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of TagItem
        """
        self._DomainId = None
        self._Name = None
        self._Status = None
        self._TTL = None
        self._CNAMESpeedup = None
        self._DNSStatus = None
        self._Grade = None
        self._GroupId = None
        self._SearchEnginePush = None
        self._Remark = None
        self._Punycode = None
        self._EffectiveDNS = None
        self._GradeLevel = None
        self._GradeTitle = None
        self._IsVip = None
        self._VipStartAt = None
        self._VipEndAt = None
        self._VipAutoRenew = None
        self._RecordCount = None
        self._CreatedOn = None
        self._UpdatedOn = None
        self._Owner = None
        self._TagList = None

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

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
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def CNAMESpeedup(self):
        return self._CNAMESpeedup

    @CNAMESpeedup.setter
    def CNAMESpeedup(self, CNAMESpeedup):
        self._CNAMESpeedup = CNAMESpeedup

    @property
    def DNSStatus(self):
        return self._DNSStatus

    @DNSStatus.setter
    def DNSStatus(self, DNSStatus):
        self._DNSStatus = DNSStatus

    @property
    def Grade(self):
        return self._Grade

    @Grade.setter
    def Grade(self, Grade):
        self._Grade = Grade

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SearchEnginePush(self):
        return self._SearchEnginePush

    @SearchEnginePush.setter
    def SearchEnginePush(self, SearchEnginePush):
        self._SearchEnginePush = SearchEnginePush

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Punycode(self):
        return self._Punycode

    @Punycode.setter
    def Punycode(self, Punycode):
        self._Punycode = Punycode

    @property
    def EffectiveDNS(self):
        return self._EffectiveDNS

    @EffectiveDNS.setter
    def EffectiveDNS(self, EffectiveDNS):
        self._EffectiveDNS = EffectiveDNS

    @property
    def GradeLevel(self):
        return self._GradeLevel

    @GradeLevel.setter
    def GradeLevel(self, GradeLevel):
        self._GradeLevel = GradeLevel

    @property
    def GradeTitle(self):
        return self._GradeTitle

    @GradeTitle.setter
    def GradeTitle(self, GradeTitle):
        self._GradeTitle = GradeTitle

    @property
    def IsVip(self):
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def VipStartAt(self):
        return self._VipStartAt

    @VipStartAt.setter
    def VipStartAt(self, VipStartAt):
        self._VipStartAt = VipStartAt

    @property
    def VipEndAt(self):
        return self._VipEndAt

    @VipEndAt.setter
    def VipEndAt(self, VipEndAt):
        self._VipEndAt = VipEndAt

    @property
    def VipAutoRenew(self):
        return self._VipAutoRenew

    @VipAutoRenew.setter
    def VipAutoRenew(self, VipAutoRenew):
        self._VipAutoRenew = VipAutoRenew

    @property
    def RecordCount(self):
        return self._RecordCount

    @RecordCount.setter
    def RecordCount(self, RecordCount):
        self._RecordCount = RecordCount

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def TagList(self):
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._TTL = params.get("TTL")
        self._CNAMESpeedup = params.get("CNAMESpeedup")
        self._DNSStatus = params.get("DNSStatus")
        self._Grade = params.get("Grade")
        self._GroupId = params.get("GroupId")
        self._SearchEnginePush = params.get("SearchEnginePush")
        self._Remark = params.get("Remark")
        self._Punycode = params.get("Punycode")
        self._EffectiveDNS = params.get("EffectiveDNS")
        self._GradeLevel = params.get("GradeLevel")
        self._GradeTitle = params.get("GradeTitle")
        self._IsVip = params.get("IsVip")
        self._VipStartAt = params.get("VipStartAt")
        self._VipEndAt = params.get("VipEndAt")
        self._VipAutoRenew = params.get("VipAutoRenew")
        self._RecordCount = params.get("RecordCount")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        self._Owner = params.get("Owner")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagItem()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainShareInfo(AbstractModel):
    """域名共享信息

    """

    def __init__(self):
        r"""
        :param _ShareTo: 域名共享对象的账号
        :type ShareTo: str
        :param _Mode: 共享模式，“rw”：可读写。 “r”:：只读
        :type Mode: str
        :param _Status: 共享状态“enabled”：共享成功。“pending”：共享到的账号不存在, 等待注册
        :type Status: str
        """
        self._ShareTo = None
        self._Mode = None
        self._Status = None

    @property
    def ShareTo(self):
        return self._ShareTo

    @ShareTo.setter
    def ShareTo(self, ShareTo):
        self._ShareTo = ShareTo

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ShareTo = params.get("ShareTo")
        self._Mode = params.get("Mode")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadSnapshotRequest(AbstractModel):
    """DownloadSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _SnapshotId: 快照记录 ID
        :type SnapshotId: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self._Domain = None
        self._SnapshotId = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._SnapshotId = params.get("SnapshotId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadSnapshotResponse(AbstractModel):
    """DownloadSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CosUrl: 快照下载链接
        :type CosUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CosUrl = None
        self._RequestId = None

    @property
    def CosUrl(self):
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CosUrl = params.get("CosUrl")
        self._RequestId = params.get("RequestId")


class GroupInfo(AbstractModel):
    """域名分组列表

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组ID
        :type GroupId: int
        :param _GroupName: 分组名称
        :type GroupName: str
        :param _GroupType: 分组类型
        :type GroupType: str
        :param _Size: 该分组中域名个数
        :type Size: int
        """
        self._GroupId = None
        self._GroupName = None
        self._GroupType = None
        self._Size = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupType(self):
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._GroupType = params.get("GroupType")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    """键值对

    """

    def __init__(self):
        r"""
        :param _Key: 键
        :type Key: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
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
        


class LineGroupInfo(AbstractModel):
    """线路分组信息

    """

    def __init__(self):
        r"""
        :param _LineId: 线路分组ID
        :type LineId: str
        :param _Name: 线路分组名称
        :type Name: str
        :param _Type: 分组类型
        :type Type: str
        :param _LineList: 线路分组包含的线路列表
        :type LineList: list of str
        """
        self._LineId = None
        self._Name = None
        self._Type = None
        self._LineList = None

    @property
    def LineId(self):
        return self._LineId

    @LineId.setter
    def LineId(self, LineId):
        self._LineId = LineId

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
    def LineList(self):
        return self._LineList

    @LineList.setter
    def LineList(self, LineList):
        self._LineList = LineList


    def _deserialize(self, params):
        self._LineId = params.get("LineId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._LineList = params.get("LineList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LineInfo(AbstractModel):
    """解析线路信息

    """

    def __init__(self):
        r"""
        :param _Name: 线路名称
        :type Name: str
        :param _LineId: 线路ID
        :type LineId: str
        """
        self._Name = None
        self._LineId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LineId(self):
        return self._LineId

    @LineId.setter
    def LineId(self, LineId):
        self._LineId = LineId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._LineId = params.get("LineId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LockInfo(AbstractModel):
    """域名锁定信息

    """

    def __init__(self):
        r"""
        :param _DomainId: 域名 ID
        :type DomainId: int
        :param _LockCode: 域名解锁码
        :type LockCode: str
        :param _LockEnd: 域名自动解锁日期
        :type LockEnd: str
        """
        self._DomainId = None
        self._LockCode = None
        self._LockEnd = None

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def LockCode(self):
        return self._LockCode

    @LockCode.setter
    def LockCode(self, LockCode):
        self._LockCode = LockCode

    @property
    def LockEnd(self):
        return self._LockEnd

    @LockEnd.setter
    def LockEnd(self, LockEnd):
        self._LockEnd = LockEnd


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._LockCode = params.get("LockCode")
        self._LockEnd = params.get("LockEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainLockRequest(AbstractModel):
    """ModifyDomainLock请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _LockDays: 域名要锁定的天数，最多可锁定的天数可以通过获取域名权限接口获取。
        :type LockDays: int
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._LockDays = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LockDays(self):
        return self._LockDays

    @LockDays.setter
    def LockDays(self, LockDays):
        self._LockDays = LockDays

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._LockDays = params.get("LockDays")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainLockResponse(AbstractModel):
    """ModifyDomainLock返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LockInfo: 域名锁定信息
        :type LockInfo: :class:`tencentcloud.dnspod.v20210323.models.LockInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LockInfo = None
        self._RequestId = None

    @property
    def LockInfo(self):
        return self._LockInfo

    @LockInfo.setter
    def LockInfo(self, LockInfo):
        self._LockInfo = LockInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LockInfo") is not None:
            self._LockInfo = LockInfo()
            self._LockInfo._deserialize(params.get("LockInfo"))
        self._RequestId = params.get("RequestId")


class ModifyDomainOwnerRequest(AbstractModel):
    """ModifyDomainOwner请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Account: 域名需要转入的账号，支持Uin或者邮箱格式
        :type Account: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._Account = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Account = params.get("Account")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainOwnerResponse(AbstractModel):
    """ModifyDomainOwner返回参数结构体

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


class ModifyDomainRemarkRequest(AbstractModel):
    """ModifyDomainRemark请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        :param _Remark: 域名备注，删除备注请提交空内容。
        :type Remark: str
        """
        self._Domain = None
        self._DomainId = None
        self._Remark = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainRemarkResponse(AbstractModel):
    """ModifyDomainRemark返回参数结构体

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


class ModifyDomainStatusRequest(AbstractModel):
    """ModifyDomainStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Status: 域名状态，”enable” 、”disable” 分别代表启用和暂停
        :type Status: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._Status = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Status = params.get("Status")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainStatusResponse(AbstractModel):
    """ModifyDomainStatus返回参数结构体

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


class ModifyDomainUnlockRequest(AbstractModel):
    """ModifyDomainUnlock请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _LockCode: 域名解锁码，锁定的时候会返回。
        :type LockCode: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._LockCode = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LockCode(self):
        return self._LockCode

    @LockCode.setter
    def LockCode(self, LockCode):
        self._LockCode = LockCode

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._LockCode = params.get("LockCode")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainUnlockResponse(AbstractModel):
    """ModifyDomainUnlock返回参数结构体

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


class ModifyDynamicDNSRequest(AbstractModel):
    """ModifyDynamicDNS请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _RecordId: 记录ID。 可以通过接口DescribeRecordList查到所有的解析记录列表以及对应的RecordId
        :type RecordId: int
        :param _RecordLine: 记录线路，通过 API 记录线路获得，中文，比如：默认。
        :type RecordLine: str
        :param _Value: 记录值，如 IP : 200.200.200.200， CNAME : cname.dnspod.com.， MX : mail.dnspod.com.。
        :type Value: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        :param _SubDomain: 主机记录，如 www，如果不传，默认为 @。
        :type SubDomain: str
        :param _RecordLineId: 线路的 ID，通过 API 记录线路获得，英文字符串，比如：10=1。参数RecordLineId优先级高于RecordLine，如果同时传递二者，优先使用RecordLineId参数。
        :type RecordLineId: str
        :param _Ttl: TTL值，如果不传，默认为域名的TTL值。
        :type Ttl: int
        """
        self._Domain = None
        self._RecordId = None
        self._RecordLine = None
        self._Value = None
        self._DomainId = None
        self._SubDomain = None
        self._RecordLineId = None
        self._Ttl = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordLineId(self):
        return self._RecordLineId

    @RecordLineId.setter
    def RecordLineId(self, RecordLineId):
        self._RecordLineId = RecordLineId

    @property
    def Ttl(self):
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RecordId = params.get("RecordId")
        self._RecordLine = params.get("RecordLine")
        self._Value = params.get("Value")
        self._DomainId = params.get("DomainId")
        self._SubDomain = params.get("SubDomain")
        self._RecordLineId = params.get("RecordLineId")
        self._Ttl = params.get("Ttl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDynamicDNSResponse(AbstractModel):
    """ModifyDynamicDNS返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordId: 记录ID
        :type RecordId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordId = None
        self._RequestId = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._RequestId = params.get("RequestId")


class ModifyPackageAutoRenewRequest(AbstractModel):
    """ModifyPackageAutoRenew请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID。可以在控制台查看所有的资源
        :type ResourceId: str
        :param _Status: enable 开启自动续费；disable 关闭自动续费
        :type Status: str
        """
        self._ResourceId = None
        self._Status = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPackageAutoRenewResponse(AbstractModel):
    """ModifyPackageAutoRenew返回参数结构体

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


class ModifyRecordBatchDetail(AbstractModel):
    """批量添加记录返回结构

    """

    def __init__(self):
        r"""
        :param _RecordList: 见RecordInfoBatchModify
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordList: list of BatchRecordInfo
        :param _Id: 任务编号
        :type Id: int
        :param _Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _DomainGrade: 域名等级
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainGrade: str
        :param _ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param _Status: 该条任务运行状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: str
        :param _DomainId: 域名ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainId: int
        """
        self._RecordList = None
        self._Id = None
        self._Domain = None
        self._DomainGrade = None
        self._ErrMsg = None
        self._Status = None
        self._Operation = None
        self._DomainId = None

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainGrade(self):
        return self._DomainGrade

    @DomainGrade.setter
    def DomainGrade(self, DomainGrade):
        self._DomainGrade = DomainGrade

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = BatchRecordInfo()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._Id = params.get("Id")
        self._Domain = params.get("Domain")
        self._DomainGrade = params.get("DomainGrade")
        self._ErrMsg = params.get("ErrMsg")
        self._Status = params.get("Status")
        self._Operation = params.get("Operation")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordBatchRequest(AbstractModel):
    """ModifyRecordBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordIdList: 记录ID数组。可以通过接口DescribeRecordList查到所有的解析记录列表以及对应的RecordId
        :type RecordIdList: list of int non-negative
        :param _Change: 要修改的字段，可选值为 [“sub_domain”、”record_type”、”area”、”value”、”mx”、”ttl”、”status”] 中的某一个。
        :type Change: str
        :param _ChangeTo: 修改为，具体依赖 change 字段，必填参数。
        :type ChangeTo: str
        :param _Value: 要修改到的记录值，仅当 change 字段为 “record_type” 时为必填参数。
        :type Value: str
        :param _MX: MX记录优先级，仅当修改为 MX 记录时为必填参数。
        :type MX: str
        """
        self._RecordIdList = None
        self._Change = None
        self._ChangeTo = None
        self._Value = None
        self._MX = None

    @property
    def RecordIdList(self):
        return self._RecordIdList

    @RecordIdList.setter
    def RecordIdList(self, RecordIdList):
        self._RecordIdList = RecordIdList

    @property
    def Change(self):
        return self._Change

    @Change.setter
    def Change(self, Change):
        self._Change = Change

    @property
    def ChangeTo(self):
        return self._ChangeTo

    @ChangeTo.setter
    def ChangeTo(self, ChangeTo):
        self._ChangeTo = ChangeTo

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX


    def _deserialize(self, params):
        self._RecordIdList = params.get("RecordIdList")
        self._Change = params.get("Change")
        self._ChangeTo = params.get("ChangeTo")
        self._Value = params.get("Value")
        self._MX = params.get("MX")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordBatchResponse(AbstractModel):
    """ModifyRecordBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 批量任务ID
        :type JobId: int
        :param _DetailList: 见modifyRecordBatchDetail
        :type DetailList: list of ModifyRecordBatchDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._DetailList = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def DetailList(self):
        return self._DetailList

    @DetailList.setter
    def DetailList(self, DetailList):
        self._DetailList = DetailList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        if params.get("DetailList") is not None:
            self._DetailList = []
            for item in params.get("DetailList"):
                obj = ModifyRecordBatchDetail()
                obj._deserialize(item)
                self._DetailList.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyRecordFieldsRequest(AbstractModel):
    """ModifyRecordFields请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _RecordId: 记录 ID 。
        :type RecordId: int
        :param _FieldList: 要修改的记录属性和值，支持：sub_domain，record_line，record_line_id，record_type，value，ttl，status，mx，weight
        :type FieldList: list of KeyValue
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self._Domain = None
        self._RecordId = None
        self._FieldList = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def FieldList(self):
        return self._FieldList

    @FieldList.setter
    def FieldList(self, FieldList):
        self._FieldList = FieldList

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RecordId = params.get("RecordId")
        if params.get("FieldList") is not None:
            self._FieldList = []
            for item in params.get("FieldList"):
                obj = KeyValue()
                obj._deserialize(item)
                self._FieldList.append(obj)
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordFieldsResponse(AbstractModel):
    """ModifyRecordFields返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordId: 记录ID
        :type RecordId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordId = None
        self._RequestId = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._RequestId = params.get("RequestId")


class ModifyRecordGroupRequest(AbstractModel):
    """ModifyRecordGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _GroupName: 分组名称
        :type GroupName: str
        :param _GroupId: 要修改的分组 ID
        :type GroupId: int
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self._Domain = None
        self._GroupName = None
        self._GroupId = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._GroupName = params.get("GroupName")
        self._GroupId = params.get("GroupId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordGroupResponse(AbstractModel):
    """ModifyRecordGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 修改的分组 ID
        :type GroupId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class ModifyRecordRemarkRequest(AbstractModel):
    """ModifyRecordRemark请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _RecordId: 记录 ID 。可以通过接口DescribeRecordList查到所有的解析记录列表以及对应的RecordId
        :type RecordId: int
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        :param _Remark: 解析记录备注，删除备注请提交空内容。
        :type Remark: str
        """
        self._Domain = None
        self._RecordId = None
        self._DomainId = None
        self._Remark = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RecordId = params.get("RecordId")
        self._DomainId = params.get("DomainId")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordRemarkResponse(AbstractModel):
    """ModifyRecordRemark返回参数结构体

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


class ModifyRecordRequest(AbstractModel):
    """ModifyRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _RecordType: 记录类型，通过 API 记录类型获得，大写英文，比如：A 。
        :type RecordType: str
        :param _RecordLine: 记录线路，通过 API 记录线路获得，中文，比如：默认。
        :type RecordLine: str
        :param _Value: 记录值，如 IP : 200.200.200.200， CNAME : cname.dnspod.com.， MX : mail.dnspod.com.。
        :type Value: str
        :param _RecordId: 记录 ID 。可以通过接口DescribeRecordList查到所有的解析记录列表以及对应的RecordId
        :type RecordId: int
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        :param _SubDomain: 主机记录，如 www，如果不传，默认为 @。
        :type SubDomain: str
        :param _RecordLineId: 线路的 ID，通过 API 记录线路获得，英文字符串，比如：10=1。参数RecordLineId优先级高于RecordLine，如果同时传递二者，优先使用RecordLineId参数。
        :type RecordLineId: str
        :param _MX: MX 优先级，当记录类型是 MX 时有效，范围1-20，MX 记录时必选。
        :type MX: int
        :param _TTL: TTL，范围1-604800，不同等级域名最小值不同。
        :type TTL: int
        :param _Weight: 权重信息，0到100的整数。仅企业 VIP 域名可用，0 表示关闭，不传该参数，表示不设置权重信息。
        :type Weight: int
        :param _Status: 记录初始状态，取值范围为 ENABLE 和 DISABLE 。默认为 ENABLE ，如果传入 DISABLE，解析不会生效，也不会验证负载均衡的限制。
        :type Status: str
        """
        self._Domain = None
        self._RecordType = None
        self._RecordLine = None
        self._Value = None
        self._RecordId = None
        self._DomainId = None
        self._SubDomain = None
        self._RecordLineId = None
        self._MX = None
        self._TTL = None
        self._Weight = None
        self._Status = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordLineId(self):
        return self._RecordLineId

    @RecordLineId.setter
    def RecordLineId(self, RecordLineId):
        self._RecordLineId = RecordLineId

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RecordType = params.get("RecordType")
        self._RecordLine = params.get("RecordLine")
        self._Value = params.get("Value")
        self._RecordId = params.get("RecordId")
        self._DomainId = params.get("DomainId")
        self._SubDomain = params.get("SubDomain")
        self._RecordLineId = params.get("RecordLineId")
        self._MX = params.get("MX")
        self._TTL = params.get("TTL")
        self._Weight = params.get("Weight")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordResponse(AbstractModel):
    """ModifyRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordId: 记录ID
        :type RecordId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordId = None
        self._RequestId = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._RequestId = params.get("RequestId")


class ModifyRecordStatusRequest(AbstractModel):
    """ModifyRecordStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _RecordId: 记录 ID 。可以通过接口DescribeRecordList查到所有的解析记录列表以及对应的RecordId
        :type RecordId: int
        :param _Status: 记录的状态。取值范围为 ENABLE 和 DISABLE。如果传入 DISABLE，解析不会生效，也不会验证负载均衡的限制。
        :type Status: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self._Domain = None
        self._RecordId = None
        self._Status = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RecordId = params.get("RecordId")
        self._Status = params.get("Status")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordStatusResponse(AbstractModel):
    """ModifyRecordStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordId: 记录ID。
        :type RecordId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordId = None
        self._RequestId = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._RequestId = params.get("RequestId")


class ModifyRecordToGroupRequest(AbstractModel):
    """ModifyRecordToGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _GroupId: 分组 ID
        :type GroupId: int
        :param _RecordId: 记录 ID，多个 ID 用竖线“|”分割
        :type RecordId: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self._Domain = None
        self._GroupId = None
        self._RecordId = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._GroupId = params.get("GroupId")
        self._RecordId = params.get("RecordId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordToGroupResponse(AbstractModel):
    """ModifyRecordToGroup返回参数结构体

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


class ModifySnapshotConfigRequest(AbstractModel):
    """ModifySnapshotConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Period: 备件间隔：空字符串-不备份，half_hour-每半小时，hourly-每小时，daily-每天，monthly-每月
        :type Period: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self._Domain = None
        self._Period = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Period = params.get("Period")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotConfigResponse(AbstractModel):
    """ModifySnapshotConfig返回参数结构体

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


class ModifySubdomainStatusRequest(AbstractModel):
    """ModifySubdomainStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _RecordType: 记录类型。允许的值为A、CNAME、MX、TXT、NS、AAAA、SPF、SRV、CAA、URL、URL1。若要传多个，用英文逗号分隔，例如A,TXT,CNAME。
        :type RecordType: str
        :param _Status: 记录状态。允许的值为disable。
        :type Status: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        :param _SubDomain: 主机记录，如 www，如果不传，默认为 @。
        :type SubDomain: str
        """
        self._Domain = None
        self._RecordType = None
        self._Status = None
        self._DomainId = None
        self._SubDomain = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RecordType = params.get("RecordType")
        self._Status = params.get("Status")
        self._DomainId = params.get("DomainId")
        self._SubDomain = params.get("SubDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubdomainStatusResponse(AbstractModel):
    """ModifySubdomainStatus返回参数结构体

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


class ModifyVasAutoRenewStatusRequest(AbstractModel):
    """ModifyVasAutoRenewStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID。可以从控制台查看所有的资源
        :type ResourceId: str
        :param _Status: enable 开启自动续费；disable 关闭自动续费
        :type Status: str
        """
        self._ResourceId = None
        self._Status = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVasAutoRenewStatusResponse(AbstractModel):
    """ModifyVasAutoRenewStatus返回参数结构体

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


class PackageDetailItem(AbstractModel):
    """套餐配置明细

    """

    def __init__(self):
        r"""
        :param _RealPrice: 套餐原价
        :type RealPrice: int
        :param _ChangedTimes: 可更换域名次数
        :type ChangedTimes: int
        :param _MinTtl: 允许设置的最小 TTL 值
        :type MinTtl: int
        :param _RecordRoll: 负载均衡数量
        :type RecordRoll: int
        :param _SubDomainLevel: 子域名级数
        :type SubDomainLevel: int
        :param _MaxWildcard: 泛解析级数
        :type MaxWildcard: int
        :param _DnsServerRegion: DNS 服务集群个数
        :type DnsServerRegion: str
        :param _DomainGradeCn: 套餐名称
        :type DomainGradeCn: str
        :param _GradeLevel: 套餐代号
        :type GradeLevel: int
        :param _Ns: 套餐对应的 NS
        :type Ns: list of str
        :param _DomainGrade: 套餐代码
        :type DomainGrade: str
        """
        self._RealPrice = None
        self._ChangedTimes = None
        self._MinTtl = None
        self._RecordRoll = None
        self._SubDomainLevel = None
        self._MaxWildcard = None
        self._DnsServerRegion = None
        self._DomainGradeCn = None
        self._GradeLevel = None
        self._Ns = None
        self._DomainGrade = None

    @property
    def RealPrice(self):
        return self._RealPrice

    @RealPrice.setter
    def RealPrice(self, RealPrice):
        self._RealPrice = RealPrice

    @property
    def ChangedTimes(self):
        return self._ChangedTimes

    @ChangedTimes.setter
    def ChangedTimes(self, ChangedTimes):
        self._ChangedTimes = ChangedTimes

    @property
    def MinTtl(self):
        return self._MinTtl

    @MinTtl.setter
    def MinTtl(self, MinTtl):
        self._MinTtl = MinTtl

    @property
    def RecordRoll(self):
        return self._RecordRoll

    @RecordRoll.setter
    def RecordRoll(self, RecordRoll):
        self._RecordRoll = RecordRoll

    @property
    def SubDomainLevel(self):
        return self._SubDomainLevel

    @SubDomainLevel.setter
    def SubDomainLevel(self, SubDomainLevel):
        self._SubDomainLevel = SubDomainLevel

    @property
    def MaxWildcard(self):
        return self._MaxWildcard

    @MaxWildcard.setter
    def MaxWildcard(self, MaxWildcard):
        self._MaxWildcard = MaxWildcard

    @property
    def DnsServerRegion(self):
        return self._DnsServerRegion

    @DnsServerRegion.setter
    def DnsServerRegion(self, DnsServerRegion):
        self._DnsServerRegion = DnsServerRegion

    @property
    def DomainGradeCn(self):
        return self._DomainGradeCn

    @DomainGradeCn.setter
    def DomainGradeCn(self, DomainGradeCn):
        self._DomainGradeCn = DomainGradeCn

    @property
    def GradeLevel(self):
        return self._GradeLevel

    @GradeLevel.setter
    def GradeLevel(self, GradeLevel):
        self._GradeLevel = GradeLevel

    @property
    def Ns(self):
        return self._Ns

    @Ns.setter
    def Ns(self, Ns):
        self._Ns = Ns

    @property
    def DomainGrade(self):
        return self._DomainGrade

    @DomainGrade.setter
    def DomainGrade(self, DomainGrade):
        self._DomainGrade = DomainGrade


    def _deserialize(self, params):
        self._RealPrice = params.get("RealPrice")
        self._ChangedTimes = params.get("ChangedTimes")
        self._MinTtl = params.get("MinTtl")
        self._RecordRoll = params.get("RecordRoll")
        self._SubDomainLevel = params.get("SubDomainLevel")
        self._MaxWildcard = params.get("MaxWildcard")
        self._DnsServerRegion = params.get("DnsServerRegion")
        self._DomainGradeCn = params.get("DomainGradeCn")
        self._GradeLevel = params.get("GradeLevel")
        self._Ns = params.get("Ns")
        self._DomainGrade = params.get("DomainGrade")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayOrderWithBalanceRequest(AbstractModel):
    """PayOrderWithBalance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BigDealIdList: 需要支付的大订单号数组
        :type BigDealIdList: list of str
        :param _VoucherIdList: 代金券ID数组。可以从控制台查到拥有的代金券
        :type VoucherIdList: list of str
        """
        self._BigDealIdList = None
        self._VoucherIdList = None

    @property
    def BigDealIdList(self):
        return self._BigDealIdList

    @BigDealIdList.setter
    def BigDealIdList(self, BigDealIdList):
        self._BigDealIdList = BigDealIdList

    @property
    def VoucherIdList(self):
        return self._VoucherIdList

    @VoucherIdList.setter
    def VoucherIdList(self, VoucherIdList):
        self._VoucherIdList = VoucherIdList


    def _deserialize(self, params):
        self._BigDealIdList = params.get("BigDealIdList")
        self._VoucherIdList = params.get("VoucherIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayOrderWithBalanceResponse(AbstractModel):
    """PayOrderWithBalance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealIdList: 此次操作支付成功的订单id数组
        :type DealIdList: list of str
        :param _BigDealIdList: 此次操作支付成功的大订单号数组
        :type BigDealIdList: list of str
        :param _DealNameList: 此次操作支付成功的订单号数组
        :type DealNameList: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealIdList = None
        self._BigDealIdList = None
        self._DealNameList = None
        self._RequestId = None

    @property
    def DealIdList(self):
        return self._DealIdList

    @DealIdList.setter
    def DealIdList(self, DealIdList):
        self._DealIdList = DealIdList

    @property
    def BigDealIdList(self):
        return self._BigDealIdList

    @BigDealIdList.setter
    def BigDealIdList(self, BigDealIdList):
        self._BigDealIdList = BigDealIdList

    @property
    def DealNameList(self):
        return self._DealNameList

    @DealNameList.setter
    def DealNameList(self, DealNameList):
        self._DealNameList = DealNameList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealIdList = params.get("DealIdList")
        self._BigDealIdList = params.get("BigDealIdList")
        self._DealNameList = params.get("DealNameList")
        self._RequestId = params.get("RequestId")


class PreviewDetail(AbstractModel):
    """域名概览明细

    """

    def __init__(self):
        r"""
        :param _Name: 域名
        :type Name: str
        :param _Grade: 域名套餐代码
        :type Grade: str
        :param _GradeTitle: 域名套餐名称
        :type GradeTitle: str
        :param _Records: 域名记录数
        :type Records: int
        :param _DomainParkingStatus: 域名停靠状态。0 未开启 1 已开启 2 已暂停
        :type DomainParkingStatus: int
        :param _LineCount: 自定义线路数量
        :type LineCount: int
        :param _LineGroupCount: 自定义线路分组数量
        :type LineGroupCount: int
        :param _AliasCount: 域名别名数量
        :type AliasCount: int
        :param _MaxAliasCount: 允许添加的最大域名别名数量
        :type MaxAliasCount: int
        :param _ResolveCount: 昨天的解析量
        :type ResolveCount: int
        :param _VASCount: 增值服务数量
        :type VASCount: int
        """
        self._Name = None
        self._Grade = None
        self._GradeTitle = None
        self._Records = None
        self._DomainParkingStatus = None
        self._LineCount = None
        self._LineGroupCount = None
        self._AliasCount = None
        self._MaxAliasCount = None
        self._ResolveCount = None
        self._VASCount = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Grade(self):
        return self._Grade

    @Grade.setter
    def Grade(self, Grade):
        self._Grade = Grade

    @property
    def GradeTitle(self):
        return self._GradeTitle

    @GradeTitle.setter
    def GradeTitle(self, GradeTitle):
        self._GradeTitle = GradeTitle

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def DomainParkingStatus(self):
        return self._DomainParkingStatus

    @DomainParkingStatus.setter
    def DomainParkingStatus(self, DomainParkingStatus):
        self._DomainParkingStatus = DomainParkingStatus

    @property
    def LineCount(self):
        return self._LineCount

    @LineCount.setter
    def LineCount(self, LineCount):
        self._LineCount = LineCount

    @property
    def LineGroupCount(self):
        return self._LineGroupCount

    @LineGroupCount.setter
    def LineGroupCount(self, LineGroupCount):
        self._LineGroupCount = LineGroupCount

    @property
    def AliasCount(self):
        return self._AliasCount

    @AliasCount.setter
    def AliasCount(self, AliasCount):
        self._AliasCount = AliasCount

    @property
    def MaxAliasCount(self):
        return self._MaxAliasCount

    @MaxAliasCount.setter
    def MaxAliasCount(self, MaxAliasCount):
        self._MaxAliasCount = MaxAliasCount

    @property
    def ResolveCount(self):
        return self._ResolveCount

    @ResolveCount.setter
    def ResolveCount(self, ResolveCount):
        self._ResolveCount = ResolveCount

    @property
    def VASCount(self):
        return self._VASCount

    @VASCount.setter
    def VASCount(self, VASCount):
        self._VASCount = VASCount


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Grade = params.get("Grade")
        self._GradeTitle = params.get("GradeTitle")
        self._Records = params.get("Records")
        self._DomainParkingStatus = params.get("DomainParkingStatus")
        self._LineCount = params.get("LineCount")
        self._LineGroupCount = params.get("LineGroupCount")
        self._AliasCount = params.get("AliasCount")
        self._MaxAliasCount = params.get("MaxAliasCount")
        self._ResolveCount = params.get("ResolveCount")
        self._VASCount = params.get("VASCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurviewInfo(AbstractModel):
    """域名权限项

    """

    def __init__(self):
        r"""
        :param _Name: 权限名称
        :type Name: str
        :param _Value: 权限值
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
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
        


class RecordCountInfo(AbstractModel):
    """查询记录列表的数量统计信息

    """

    def __init__(self):
        r"""
        :param _SubdomainCount: 子域名数量
        :type SubdomainCount: int
        :param _ListCount: 列表返回的记录数
        :type ListCount: int
        :param _TotalCount: 总的记录数
        :type TotalCount: int
        """
        self._SubdomainCount = None
        self._ListCount = None
        self._TotalCount = None

    @property
    def SubdomainCount(self):
        return self._SubdomainCount

    @SubdomainCount.setter
    def SubdomainCount(self, SubdomainCount):
        self._SubdomainCount = SubdomainCount

    @property
    def ListCount(self):
        return self._ListCount

    @ListCount.setter
    def ListCount(self, ListCount):
        self._ListCount = ListCount

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._SubdomainCount = params.get("SubdomainCount")
        self._ListCount = params.get("ListCount")
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordGroupInfo(AbstractModel):
    """解析记录分组信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 分组 ID
        :type GroupId: int
        :param _GroupName: 分组名称
        :type GroupName: str
        :param _GroupType: 分组类型：system-系统；user-用户
        :type GroupType: str
        """
        self._GroupId = None
        self._GroupName = None
        self._GroupType = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupType(self):
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._GroupType = params.get("GroupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordInfo(AbstractModel):
    """记录信息

    """

    def __init__(self):
        r"""
        :param _Id: 记录 ID 。
        :type Id: int
        :param _SubDomain: 子域名(主机记录)。
        :type SubDomain: str
        :param _RecordType: 记录类型, 详见 DescribeRecordType 接口。
        :type RecordType: str
        :param _RecordLine: 解析记录的线路，详见 DescribeRecordLineList 接口。
        :type RecordLine: str
        :param _RecordLineId: 解析记录的线路 ID ，详见 DescribeRecordLineList 接口。
        :type RecordLineId: str
        :param _Value: 记录值。
        :type Value: str
        :param _Weight: 记录权重值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param _MX: 记录的 MX 记录值，非 MX 记录类型，默认为 0。
        :type MX: int
        :param _TTL: 记录的 TTL 值。
        :type TTL: int
        :param _Enabled: 记录状态。0表示禁用，1表示启用。
        :type Enabled: int
        :param _MonitorStatus: 该记录的 D 监控状态。
"Ok" : 服务器正常。
"Warn" : 该记录有报警, 服务器返回 4XX。
"Down" : 服务器宕机。
"" : 该记录未开启 D 监控。
        :type MonitorStatus: str
        :param _Remark: 记录的备注。
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _UpdatedOn: 记录最后更新时间。
        :type UpdatedOn: str
        :param _DomainId: 域名 ID 。
        :type DomainId: int
        """
        self._Id = None
        self._SubDomain = None
        self._RecordType = None
        self._RecordLine = None
        self._RecordLineId = None
        self._Value = None
        self._Weight = None
        self._MX = None
        self._TTL = None
        self._Enabled = None
        self._MonitorStatus = None
        self._Remark = None
        self._UpdatedOn = None
        self._DomainId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def RecordLineId(self):
        return self._RecordLineId

    @RecordLineId.setter
    def RecordLineId(self, RecordLineId):
        self._RecordLineId = RecordLineId

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def MonitorStatus(self):
        return self._MonitorStatus

    @MonitorStatus.setter
    def MonitorStatus(self, MonitorStatus):
        self._MonitorStatus = MonitorStatus

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def UpdatedOn(self):
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._SubDomain = params.get("SubDomain")
        self._RecordType = params.get("RecordType")
        self._RecordLine = params.get("RecordLine")
        self._RecordLineId = params.get("RecordLineId")
        self._Value = params.get("Value")
        self._Weight = params.get("Weight")
        self._MX = params.get("MX")
        self._TTL = params.get("TTL")
        self._Enabled = params.get("Enabled")
        self._MonitorStatus = params.get("MonitorStatus")
        self._Remark = params.get("Remark")
        self._UpdatedOn = params.get("UpdatedOn")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordListItem(AbstractModel):
    """记录列表元素

    """

    def __init__(self):
        r"""
        :param _RecordId: 记录Id
        :type RecordId: int
        :param _Value: 记录值
        :type Value: str
        :param _Status: 记录状态，启用：ENABLE，暂停：DISABLE
        :type Status: str
        :param _UpdatedOn: 更新时间
        :type UpdatedOn: str
        :param _Name: 主机名
        :type Name: str
        :param _Line: 记录线路
        :type Line: str
        :param _LineId: 线路Id
        :type LineId: str
        :param _Type: 记录类型
        :type Type: str
        :param _Weight: 记录权重，用于负载均衡记录
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param _MonitorStatus: 记录监控状态，正常：OK，告警：WARN，宕机：DOWN，未设置监控或监控暂停则为空
        :type MonitorStatus: str
        :param _Remark: 记录备注说明
        :type Remark: str
        :param _TTL: 记录缓存时间
        :type TTL: int
        :param _MX: MX值，只有MX记录有
注意：此字段可能返回 null，表示取不到有效值。
        :type MX: int
        :param _DefaultNS: 是否是默认的ns记录
        :type DefaultNS: bool
        """
        self._RecordId = None
        self._Value = None
        self._Status = None
        self._UpdatedOn = None
        self._Name = None
        self._Line = None
        self._LineId = None
        self._Type = None
        self._Weight = None
        self._MonitorStatus = None
        self._Remark = None
        self._TTL = None
        self._MX = None
        self._DefaultNS = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpdatedOn(self):
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Line(self):
        return self._Line

    @Line.setter
    def Line(self, Line):
        self._Line = Line

    @property
    def LineId(self):
        return self._LineId

    @LineId.setter
    def LineId(self, LineId):
        self._LineId = LineId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def MonitorStatus(self):
        return self._MonitorStatus

    @MonitorStatus.setter
    def MonitorStatus(self, MonitorStatus):
        self._MonitorStatus = MonitorStatus

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def DefaultNS(self):
        return self._DefaultNS

    @DefaultNS.setter
    def DefaultNS(self, DefaultNS):
        self._DefaultNS = DefaultNS


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._Value = params.get("Value")
        self._Status = params.get("Status")
        self._UpdatedOn = params.get("UpdatedOn")
        self._Name = params.get("Name")
        self._Line = params.get("Line")
        self._LineId = params.get("LineId")
        self._Type = params.get("Type")
        self._Weight = params.get("Weight")
        self._MonitorStatus = params.get("MonitorStatus")
        self._Remark = params.get("Remark")
        self._TTL = params.get("TTL")
        self._MX = params.get("MX")
        self._DefaultNS = params.get("DefaultNS")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackRecordSnapshotRequest(AbstractModel):
    """RollbackRecordSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _SnapshotId: 快照 ID
        :type SnapshotId: str
        :param _RecordList: 解析记录信息
        :type RecordList: list of SnapshotRecord
        :param _TaskId: 之前的快照回滚任务 ID
        :type TaskId: int
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self._Domain = None
        self._SnapshotId = None
        self._RecordList = None
        self._TaskId = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._SnapshotId = params.get("SnapshotId")
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = SnapshotRecord()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._TaskId = params.get("TaskId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackRecordSnapshotResponse(AbstractModel):
    """RollbackRecordSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 回滚任务 ID
        :type JobId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class RollbackSnapshotRequest(AbstractModel):
    """RollbackSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _SnapshotId: 快照记录 ID
        :type SnapshotId: str
        :param _DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        :param _RecordList: 指定需要回滚的记录
        :type RecordList: list of SnapshotRecord
        """
        self._Domain = None
        self._SnapshotId = None
        self._DomainId = None
        self._RecordList = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._SnapshotId = params.get("SnapshotId")
        self._DomainId = params.get("DomainId")
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = SnapshotRecord()
                obj._deserialize(item)
                self._RecordList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackSnapshotResponse(AbstractModel):
    """RollbackSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 回滚任务 ID，用来查询回滚状态
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SnapshotConfig(AbstractModel):
    """域名解析快照配置

    """

    def __init__(self):
        r"""
        :param _Config: 配置类型：空字符串-不备份，half_hour-每半小时，hourly-每小时，daily-每天，monthly-每月
        :type Config: str
        :param _CreatedOn: 添加时间
        :type CreatedOn: str
        :param _DomainId: 所属域名 ID
        :type DomainId: str
        :param _Id: 配置 ID
        :type Id: str
        :param _SnapshotCount: 快照数量
        :type SnapshotCount: int
        :param _Status: 状态：enable-启用，disable-禁用
        :type Status: str
        :param _UpdatedOn: 更新时间
        :type UpdatedOn: str
        """
        self._Config = None
        self._CreatedOn = None
        self._DomainId = None
        self._Id = None
        self._SnapshotCount = None
        self._Status = None
        self._UpdatedOn = None

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SnapshotCount(self):
        return self._SnapshotCount

    @SnapshotCount.setter
    def SnapshotCount(self, SnapshotCount):
        self._SnapshotCount = SnapshotCount

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpdatedOn(self):
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn


    def _deserialize(self, params):
        self._Config = params.get("Config")
        self._CreatedOn = params.get("CreatedOn")
        self._DomainId = params.get("DomainId")
        self._Id = params.get("Id")
        self._SnapshotCount = params.get("SnapshotCount")
        self._Status = params.get("Status")
        self._UpdatedOn = params.get("UpdatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotInfo(AbstractModel):
    """快照信息

    """

    def __init__(self):
        r"""
        :param _CosUrl: 快照的对象存储地址
        :type CosUrl: str
        :param _CreatedOn: 添加时间
        :type CreatedOn: str
        :param _Domain: 所属域名
        :type Domain: str
        :param _Id: 快照记录 ID
        :type Id: str
        :param _RecordCount: 域名解析记录数
        :type RecordCount: str
        :param _Status: 状态：normal-正常，create-备份中
        :type Status: str
        """
        self._CosUrl = None
        self._CreatedOn = None
        self._Domain = None
        self._Id = None
        self._RecordCount = None
        self._Status = None

    @property
    def CosUrl(self):
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RecordCount(self):
        return self._RecordCount

    @RecordCount.setter
    def RecordCount(self, RecordCount):
        self._RecordCount = RecordCount

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._CosUrl = params.get("CosUrl")
        self._CreatedOn = params.get("CreatedOn")
        self._Domain = params.get("Domain")
        self._Id = params.get("Id")
        self._RecordCount = params.get("RecordCount")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotPageInfo(AbstractModel):
    """快照列表分页信息

    """

    def __init__(self):
        r"""
        :param _Total: 快照总数
        :type Total: int
        """
        self._Total = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotRecord(AbstractModel):
    """快照解析记录

    """

    def __init__(self):
        r"""
        :param _SubDomain: 子域名
        :type SubDomain: str
        :param _RecordType: 记录类型
        :type RecordType: str
        :param _RecordLine: 解析线路
        :type RecordLine: str
        :param _Value: 解析值
        :type Value: str
        :param _TTL: TTL(秒)
        :type TTL: str
        :param _RecordId: 解析记录 ID
        :type RecordId: str
        :param _MX: MX优先级
注意：此字段可能返回 null，表示取不到有效值。
        :type MX: str
        :param _Weight: 权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: str
        :param _Reason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        """
        self._SubDomain = None
        self._RecordType = None
        self._RecordLine = None
        self._Value = None
        self._TTL = None
        self._RecordId = None
        self._MX = None
        self._Weight = None
        self._Reason = None

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._SubDomain = params.get("SubDomain")
        self._RecordType = params.get("RecordType")
        self._RecordLine = params.get("RecordLine")
        self._Value = params.get("Value")
        self._TTL = params.get("TTL")
        self._RecordId = params.get("RecordId")
        self._MX = params.get("MX")
        self._Weight = params.get("Weight")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubdomainAliasAnalyticsItem(AbstractModel):
    """子域名别名解析量统计信息

    """

    def __init__(self):
        r"""
        :param _Info: 子域名解析量统计查询信息
        :type Info: :class:`tencentcloud.dnspod.v20210323.models.SubdomainAnalyticsInfo`
        :param _Data: 当前统计维度解析量小计
        :type Data: list of DomainAnalyticsDetail
        """
        self._Info = None
        self._Data = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = SubdomainAnalyticsInfo()
            self._Info._deserialize(params.get("Info"))
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DomainAnalyticsDetail()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubdomainAnalyticsInfo(AbstractModel):
    """子域名解析量统计查询信息

    """

    def __init__(self):
        r"""
        :param _DnsFormat: DATE:按天维度统计 HOUR:按小时维度统计
        :type DnsFormat: str
        :param _DnsTotal: 当前统计周期解析量总计
        :type DnsTotal: int
        :param _Domain: 当前查询的域名
        :type Domain: str
        :param _StartDate: 当前统计周期开始时间
        :type StartDate: str
        :param _EndDate: 当前统计周期结束时间
        :type EndDate: str
        :param _Subdomain: 当前统计的子域名
        :type Subdomain: str
        """
        self._DnsFormat = None
        self._DnsTotal = None
        self._Domain = None
        self._StartDate = None
        self._EndDate = None
        self._Subdomain = None

    @property
    def DnsFormat(self):
        return self._DnsFormat

    @DnsFormat.setter
    def DnsFormat(self, DnsFormat):
        self._DnsFormat = DnsFormat

    @property
    def DnsTotal(self):
        return self._DnsTotal

    @DnsTotal.setter
    def DnsTotal(self, DnsTotal):
        self._DnsTotal = DnsTotal

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Subdomain(self):
        return self._Subdomain

    @Subdomain.setter
    def Subdomain(self, Subdomain):
        self._Subdomain = Subdomain


    def _deserialize(self, params):
        self._DnsFormat = params.get("DnsFormat")
        self._DnsTotal = params.get("DnsTotal")
        self._Domain = params.get("Domain")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Subdomain = params.get("Subdomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagItem(AbstractModel):
    """标签项

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagItemFilter(AbstractModel):
    """标签过滤条件

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签键
        :type TagValue: list of str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param _Nick: 用户昵称
        :type Nick: str
        :param _Id: 用户ID
        :type Id: int
        :param _Email: 用户账号, 邮箱格式
        :type Email: str
        :param _Status: 账号状态：”enabled”: 正常；”disabled”: 被封禁
        :type Status: str
        :param _Telephone: 电话号码
        :type Telephone: str
        :param _EmailVerified: 邮箱是否通过验证：”yes”: 通过；”no”: 未通过
        :type EmailVerified: str
        :param _TelephoneVerified: 手机是否通过验证：”yes”: 通过；”no”: 未通过
        :type TelephoneVerified: str
        :param _UserGrade: 账号等级, 按照用户账号下域名等级排序, 选取一个最高等级为账号等级, 具体对应情况参见域名等级。
        :type UserGrade: str
        :param _RealName: 用户名称, 企业用户对应为公司名称
        :type RealName: str
        :param _WechatBinded: 是否绑定微信：”yes”: 通过；”no”: 未通过
        :type WechatBinded: str
        :param _Uin: 用户UIN
        :type Uin: int
        :param _FreeNs: 所属 DNS 服务器
        :type FreeNs: list of str
        """
        self._Nick = None
        self._Id = None
        self._Email = None
        self._Status = None
        self._Telephone = None
        self._EmailVerified = None
        self._TelephoneVerified = None
        self._UserGrade = None
        self._RealName = None
        self._WechatBinded = None
        self._Uin = None
        self._FreeNs = None

    @property
    def Nick(self):
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Telephone(self):
        return self._Telephone

    @Telephone.setter
    def Telephone(self, Telephone):
        self._Telephone = Telephone

    @property
    def EmailVerified(self):
        return self._EmailVerified

    @EmailVerified.setter
    def EmailVerified(self, EmailVerified):
        self._EmailVerified = EmailVerified

    @property
    def TelephoneVerified(self):
        return self._TelephoneVerified

    @TelephoneVerified.setter
    def TelephoneVerified(self, TelephoneVerified):
        self._TelephoneVerified = TelephoneVerified

    @property
    def UserGrade(self):
        return self._UserGrade

    @UserGrade.setter
    def UserGrade(self, UserGrade):
        self._UserGrade = UserGrade

    @property
    def RealName(self):
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def WechatBinded(self):
        return self._WechatBinded

    @WechatBinded.setter
    def WechatBinded(self, WechatBinded):
        self._WechatBinded = WechatBinded

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def FreeNs(self):
        return self._FreeNs

    @FreeNs.setter
    def FreeNs(self, FreeNs):
        self._FreeNs = FreeNs


    def _deserialize(self, params):
        self._Nick = params.get("Nick")
        self._Id = params.get("Id")
        self._Email = params.get("Email")
        self._Status = params.get("Status")
        self._Telephone = params.get("Telephone")
        self._EmailVerified = params.get("EmailVerified")
        self._TelephoneVerified = params.get("TelephoneVerified")
        self._UserGrade = params.get("UserGrade")
        self._RealName = params.get("RealName")
        self._WechatBinded = params.get("WechatBinded")
        self._Uin = params.get("Uin")
        self._FreeNs = params.get("FreeNs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VASStatisticItem(AbstractModel):
    """域名增值服务用量

    """

    def __init__(self):
        r"""
        :param _Name: 增值服务名称
        :type Name: str
        :param _Key: 增值服务标识
        :type Key: str
        :param _LimitCount: 增值服务最大用量
        :type LimitCount: int
        :param _UseCount: 增值服务已使用的用量
        :type UseCount: int
        """
        self._Name = None
        self._Key = None
        self._LimitCount = None
        self._UseCount = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def LimitCount(self):
        return self._LimitCount

    @LimitCount.setter
    def LimitCount(self, LimitCount):
        self._LimitCount = LimitCount

    @property
    def UseCount(self):
        return self._UseCount

    @UseCount.setter
    def UseCount(self, UseCount):
        self._UseCount = UseCount


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Key = params.get("Key")
        self._LimitCount = params.get("LimitCount")
        self._UseCount = params.get("UseCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhoisContact(AbstractModel):
    """Whois联系信息

    """

    def __init__(self):
        r"""
        :param _Admin: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Admin: :class:`tencentcloud.dnspod.v20210323.models.WhoisContactAddress`
        :param _Billing: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Billing: :class:`tencentcloud.dnspod.v20210323.models.WhoisContactAddress`
        :param _Registrant: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Registrant: :class:`tencentcloud.dnspod.v20210323.models.WhoisContactAddress`
        :param _Tech: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Tech: :class:`tencentcloud.dnspod.v20210323.models.WhoisContactAddress`
        """
        self._Admin = None
        self._Billing = None
        self._Registrant = None
        self._Tech = None

    @property
    def Admin(self):
        return self._Admin

    @Admin.setter
    def Admin(self, Admin):
        self._Admin = Admin

    @property
    def Billing(self):
        return self._Billing

    @Billing.setter
    def Billing(self, Billing):
        self._Billing = Billing

    @property
    def Registrant(self):
        return self._Registrant

    @Registrant.setter
    def Registrant(self, Registrant):
        self._Registrant = Registrant

    @property
    def Tech(self):
        return self._Tech

    @Tech.setter
    def Tech(self, Tech):
        self._Tech = Tech


    def _deserialize(self, params):
        if params.get("Admin") is not None:
            self._Admin = WhoisContactAddress()
            self._Admin._deserialize(params.get("Admin"))
        if params.get("Billing") is not None:
            self._Billing = WhoisContactAddress()
            self._Billing._deserialize(params.get("Billing"))
        if params.get("Registrant") is not None:
            self._Registrant = WhoisContactAddress()
            self._Registrant._deserialize(params.get("Registrant"))
        if params.get("Tech") is not None:
            self._Tech = WhoisContactAddress()
            self._Tech._deserialize(params.get("Tech"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhoisContactAddress(AbstractModel):
    """Whois联系信息地址

    """

    def __init__(self):
        r"""
        :param _City: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param _Country: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Country: str
        :param _Email: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _Fax: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Fax: str
        :param _FaxExt: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type FaxExt: str
        :param _Handle: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Handle: str
        :param _Name: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Organization: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Organization: str
        :param _Phone: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param _PostalCode: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type PostalCode: str
        :param _State: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param _Street: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Street: str
        """
        self._City = None
        self._Country = None
        self._Email = None
        self._Fax = None
        self._FaxExt = None
        self._Handle = None
        self._Name = None
        self._Organization = None
        self._Phone = None
        self._PostalCode = None
        self._State = None
        self._Street = None

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Country(self):
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Fax(self):
        return self._Fax

    @Fax.setter
    def Fax(self, Fax):
        self._Fax = Fax

    @property
    def FaxExt(self):
        return self._FaxExt

    @FaxExt.setter
    def FaxExt(self, FaxExt):
        self._FaxExt = FaxExt

    @property
    def Handle(self):
        return self._Handle

    @Handle.setter
    def Handle(self, Handle):
        self._Handle = Handle

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Organization(self):
        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        self._Organization = Organization

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def PostalCode(self):
        return self._PostalCode

    @PostalCode.setter
    def PostalCode(self, PostalCode):
        self._PostalCode = PostalCode

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Street(self):
        return self._Street

    @Street.setter
    def Street(self, Street):
        self._Street = Street


    def _deserialize(self, params):
        self._City = params.get("City")
        self._Country = params.get("Country")
        self._Email = params.get("Email")
        self._Fax = params.get("Fax")
        self._FaxExt = params.get("FaxExt")
        self._Handle = params.get("Handle")
        self._Name = params.get("Name")
        self._Organization = params.get("Organization")
        self._Phone = params.get("Phone")
        self._PostalCode = params.get("PostalCode")
        self._State = params.get("State")
        self._Street = params.get("Street")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhoisInfo(AbstractModel):
    """Whois信息

    """

    def __init__(self):
        r"""
        :param _Contacts: 联系信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Contacts: :class:`tencentcloud.dnspod.v20210323.models.WhoisContact`
        :param _CreationDate: 域名注册时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationDate: str
        :param _ExpirationDate: 域名到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpirationDate: str
        :param _IsQcloud: 是否是在腾讯云注册的域名
注意：此字段可能返回 null，表示取不到有效值。
        :type IsQcloud: bool
        :param _IsQcloudOwner: 是否当前操作账号注册的域名
注意：此字段可能返回 null，表示取不到有效值。
        :type IsQcloudOwner: bool
        :param _NameServers: 域名配置的NS
注意：此字段可能返回 null，表示取不到有效值。
        :type NameServers: list of str
        :param _Raw: Whois原始信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Raw: list of str
        :param _Registrar: 域名注册商
注意：此字段可能返回 null，表示取不到有效值。
        :type Registrar: list of str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: list of str
        :param _UpdatedDate: 更新日期
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedDate: str
        :param _Dnssec: dnssec
注意：此字段可能返回 null，表示取不到有效值。
        :type Dnssec: str
        """
        self._Contacts = None
        self._CreationDate = None
        self._ExpirationDate = None
        self._IsQcloud = None
        self._IsQcloudOwner = None
        self._NameServers = None
        self._Raw = None
        self._Registrar = None
        self._Status = None
        self._UpdatedDate = None
        self._Dnssec = None

    @property
    def Contacts(self):
        return self._Contacts

    @Contacts.setter
    def Contacts(self, Contacts):
        self._Contacts = Contacts

    @property
    def CreationDate(self):
        return self._CreationDate

    @CreationDate.setter
    def CreationDate(self, CreationDate):
        self._CreationDate = CreationDate

    @property
    def ExpirationDate(self):
        return self._ExpirationDate

    @ExpirationDate.setter
    def ExpirationDate(self, ExpirationDate):
        self._ExpirationDate = ExpirationDate

    @property
    def IsQcloud(self):
        return self._IsQcloud

    @IsQcloud.setter
    def IsQcloud(self, IsQcloud):
        self._IsQcloud = IsQcloud

    @property
    def IsQcloudOwner(self):
        return self._IsQcloudOwner

    @IsQcloudOwner.setter
    def IsQcloudOwner(self, IsQcloudOwner):
        self._IsQcloudOwner = IsQcloudOwner

    @property
    def NameServers(self):
        return self._NameServers

    @NameServers.setter
    def NameServers(self, NameServers):
        self._NameServers = NameServers

    @property
    def Raw(self):
        return self._Raw

    @Raw.setter
    def Raw(self, Raw):
        self._Raw = Raw

    @property
    def Registrar(self):
        return self._Registrar

    @Registrar.setter
    def Registrar(self, Registrar):
        self._Registrar = Registrar

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpdatedDate(self):
        return self._UpdatedDate

    @UpdatedDate.setter
    def UpdatedDate(self, UpdatedDate):
        self._UpdatedDate = UpdatedDate

    @property
    def Dnssec(self):
        return self._Dnssec

    @Dnssec.setter
    def Dnssec(self, Dnssec):
        self._Dnssec = Dnssec


    def _deserialize(self, params):
        if params.get("Contacts") is not None:
            self._Contacts = WhoisContact()
            self._Contacts._deserialize(params.get("Contacts"))
        self._CreationDate = params.get("CreationDate")
        self._ExpirationDate = params.get("ExpirationDate")
        self._IsQcloud = params.get("IsQcloud")
        self._IsQcloudOwner = params.get("IsQcloudOwner")
        self._NameServers = params.get("NameServers")
        self._Raw = params.get("Raw")
        self._Registrar = params.get("Registrar")
        self._Status = params.get("Status")
        self._UpdatedDate = params.get("UpdatedDate")
        self._Dnssec = params.get("Dnssec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        