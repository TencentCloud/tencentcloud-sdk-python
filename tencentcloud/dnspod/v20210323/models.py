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
        :param RecordType: 记录类型, 详见 DescribeRecordType 接口。
        :type RecordType: str
        :param Value: 记录值。
        :type Value: str
        :param SubDomain: 子域名(主机记录)，默认为@。
        :type SubDomain: str
        :param RecordLine: 解析记录的线路，详见 DescribeRecordLineList 接口，RecordLine和RecordLineId都未填时，默认为「默认」线路。
        :type RecordLine: str
        :param RecordLineId: 解析记录的线路 ID，RecordLine和RecordLineId都有时，系统优先取 RecordLineId。
        :type RecordLineId: str
        :param Weight: 记录权重值(暂未支持)。
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param MX: 记录的 MX 记录值，非 MX 记录类型，默认为 0，MX记录则必选。
        :type MX: int
        :param TTL: 记录的 TTL 值，默认600。
        :type TTL: int
        :param Enabled: 记录状态(暂未支持)。0表示禁用，1表示启用。默认启用。
        :type Enabled: int
        :param Remark: 记录备注(暂未支持)。
        :type Remark: str
        """
        self.RecordType = None
        self.Value = None
        self.SubDomain = None
        self.RecordLine = None
        self.RecordLineId = None
        self.Weight = None
        self.MX = None
        self.TTL = None
        self.Enabled = None
        self.Remark = None


    def _deserialize(self, params):
        self.RecordType = params.get("RecordType")
        self.Value = params.get("Value")
        self.SubDomain = params.get("SubDomain")
        self.RecordLine = params.get("RecordLine")
        self.RecordLineId = params.get("RecordLineId")
        self.Weight = params.get("Weight")
        self.MX = params.get("MX")
        self.TTL = params.get("TTL")
        self.Enabled = params.get("Enabled")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchRecordInfo(AbstractModel):
    """批量任务中的记录信息

    """

    def __init__(self):
        r"""
        :param RecordId: 记录 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordId: int
        :param SubDomain: 子域名(主机记录)。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubDomain: str
        :param RecordType: 记录类型, 详见 DescribeRecordType 接口
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordType: str
        :param RecordLine: 解析记录的线路，详见 DescribeRecordLineList 接口
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordLine: str
        :param Value: 记录值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param TTL: 记录的 TTL 值
注意：此字段可能返回 null，表示取不到有效值。
        :type TTL: int
        :param Status: 记录添加状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: str
        :param ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param Id: 此条记录在列表中的ID
        :type Id: int
        :param Enabled: 记录生效状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: int
        :param MX: 记录的MX权重
注意：此字段可能返回 null，表示取不到有效值。
        :type MX: int
        :param Weight: 记录权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        """
        self.RecordId = None
        self.SubDomain = None
        self.RecordType = None
        self.RecordLine = None
        self.Value = None
        self.TTL = None
        self.Status = None
        self.Operation = None
        self.ErrMsg = None
        self.Id = None
        self.Enabled = None
        self.MX = None
        self.Weight = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.SubDomain = params.get("SubDomain")
        self.RecordType = params.get("RecordType")
        self.RecordLine = params.get("RecordLine")
        self.Value = params.get("Value")
        self.TTL = params.get("TTL")
        self.Status = params.get("Status")
        self.Operation = params.get("Operation")
        self.ErrMsg = params.get("ErrMsg")
        self.Id = params.get("Id")
        self.Enabled = params.get("Enabled")
        self.MX = params.get("MX")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckRecordSnapshotRollbackRequest(AbstractModel):
    """CheckRecordSnapshotRollback请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param SnapshotId: 快照 ID
        :type SnapshotId: str
        :param Record: 解析记录信息
        :type Record: :class:`tencentcloud.dnspod.v20210323.models.SnapshotRecord`
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.SnapshotId = None
        self.Record = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.SnapshotId = params.get("SnapshotId")
        if params.get("Record") is not None:
            self.Record = SnapshotRecord()
            self.Record._deserialize(params.get("Record"))
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckRecordSnapshotRollbackResponse(AbstractModel):
    """CheckRecordSnapshotRollback返回参数结构体

    """

    def __init__(self):
        r"""
        :param Reason: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Reason = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Reason = params.get("Reason")
        self.RequestId = params.get("RequestId")


class CheckSnapshotRollbackRequest(AbstractModel):
    """CheckSnapshotRollback请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param SnapshotId: 快照记录 ID
        :type SnapshotId: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.SnapshotId = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.SnapshotId = params.get("SnapshotId")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckSnapshotRollbackResponse(AbstractModel):
    """CheckSnapshotRollback返回参数结构体

    """

    def __init__(self):
        r"""
        :param SnapshotId: 快照记录 ID
        :type SnapshotId: str
        :param CostMinutes: 回滚时长（分钟）
        :type CostMinutes: int
        :param Domain: 快照所属域名
        :type Domain: str
        :param Total: 解析记录总数
        :type Total: int
        :param Timeout: 值为 1，表示超时
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeout: int
        :param Failed: 检查失败数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Failed: int
        :param FailedRecordList: 失败记录信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedRecordList: list of SnapshotRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SnapshotId = None
        self.CostMinutes = None
        self.Domain = None
        self.Total = None
        self.Timeout = None
        self.Failed = None
        self.FailedRecordList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.CostMinutes = params.get("CostMinutes")
        self.Domain = params.get("Domain")
        self.Total = params.get("Total")
        self.Timeout = params.get("Timeout")
        self.Failed = params.get("Failed")
        if params.get("FailedRecordList") is not None:
            self.FailedRecordList = []
            for item in params.get("FailedRecordList"):
                obj = SnapshotRecord()
                obj._deserialize(item)
                self.FailedRecordList.append(obj)
        self.RequestId = params.get("RequestId")


class CreateDealRequest(AbstractModel):
    """CreateDeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param DealType: 询价类型，1 新购，2 续费，3 套餐升级（增值服务暂时只支持新购）
        :type DealType: int
        :param GoodsType: 商品类型，1 域名套餐 2 增值服务
        :type GoodsType: int
        :param GoodsChildType: 套餐类型：
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
        :param GoodsNum: 增值服务购买数量，如果是域名套餐固定为1，如果是增值服务则按以下规则：
负载均衡、D监控任务数、D监控备用 IP 数、自定义线路数、URL 转发（必须是5的正整数倍，如 5、10、15 等）
        :type GoodsNum: int
        :param AutoRenew: 是否开启自动续费，1 开启，2 不开启（增值服务暂不支持自动续费），默认值为 2 不开启
        :type AutoRenew: int
        :param Domain: 需要绑定套餐的域名，如 dnspod.cn，如果是续费或升级，domain 参数必须要传，新购可不传。
        :type Domain: str
        :param TimeSpan: 套餐时长：
1. 套餐以月为单位（按月只能是 3、6 还有 12 的倍数），套餐例如购买一年则传12，最大120 。（续费最低一年）
2. 升级套餐时不需要传。
3. 增值服务的时长单位为年，买一年传1（增值服务新购按年只能是 1，增值服务续费最大为 10）
        :type TimeSpan: int
        :param NewPackageType: 套餐类型，需要升级到的套餐类型，只有升级时需要。
        :type NewPackageType: str
        """
        self.DealType = None
        self.GoodsType = None
        self.GoodsChildType = None
        self.GoodsNum = None
        self.AutoRenew = None
        self.Domain = None
        self.TimeSpan = None
        self.NewPackageType = None


    def _deserialize(self, params):
        self.DealType = params.get("DealType")
        self.GoodsType = params.get("GoodsType")
        self.GoodsChildType = params.get("GoodsChildType")
        self.GoodsNum = params.get("GoodsNum")
        self.AutoRenew = params.get("AutoRenew")
        self.Domain = params.get("Domain")
        self.TimeSpan = params.get("TimeSpan")
        self.NewPackageType = params.get("NewPackageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDealResponse(AbstractModel):
    """CreateDeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param BigDealId: 大订单号，一个大订单号下可以有多个子订单，说明是同一次下单
        :type BigDealId: str
        :param DealList: 子订单列表
        :type DealList: list of Deals
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BigDealId = None
        self.DealList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BigDealId = params.get("BigDealId")
        if params.get("DealList") is not None:
            self.DealList = []
            for item in params.get("DealList"):
                obj = Deals()
                obj._deserialize(item)
                self.DealList.append(obj)
        self.RequestId = params.get("RequestId")


class CreateDomainAliasRequest(AbstractModel):
    """CreateDomainAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param DomainAlias: 域名别名
        :type DomainAlias: str
        :param Domain: 域名
        :type Domain: str
        :param DomainId: 域名ID，参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.DomainAlias = None
        self.Domain = None
        self.DomainId = None


    def _deserialize(self, params):
        self.DomainAlias = params.get("DomainAlias")
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainAliasResponse(AbstractModel):
    """CreateDomainAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param DomainAliasId: 域名别名ID
        :type DomainAliasId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainAliasId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DomainAliasId = params.get("DomainAliasId")
        self.RequestId = params.get("RequestId")


class CreateDomainBatchDetail(AbstractModel):
    """批量添加域名返回结构

    """

    def __init__(self):
        r"""
        :param RecordList: 见RecordInfoBatch
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordList: list of CreateDomainBatchRecord
        :param Id: 任务编号
        :type Id: int
        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param DomainGrade: 域名等级
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainGrade: str
        :param ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param Status: 该条任务运行状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: str
        """
        self.RecordList = None
        self.Id = None
        self.Domain = None
        self.DomainGrade = None
        self.ErrMsg = None
        self.Status = None
        self.Operation = None


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = CreateDomainBatchRecord()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.Id = params.get("Id")
        self.Domain = params.get("Domain")
        self.DomainGrade = params.get("DomainGrade")
        self.ErrMsg = params.get("ErrMsg")
        self.Status = params.get("Status")
        self.Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainBatchRecord(AbstractModel):
    """批量添加域名任务中的记录信息

    """

    def __init__(self):
        r"""
        :param SubDomain: 子域名(主机记录)。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubDomain: str
        :param RecordType: 记录类型, 详见 DescribeRecordType 接口
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordType: str
        :param RecordLine: 解析记录的线路，详见 DescribeRecordLineList 接口
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordLine: str
        :param Value: 记录值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param TTL: 记录的 TTL 值
注意：此字段可能返回 null，表示取不到有效值。
        :type TTL: int
        :param Status: 记录添加状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: str
        :param ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param Id: 此条记录在列表中的ID
        :type Id: int
        """
        self.SubDomain = None
        self.RecordType = None
        self.RecordLine = None
        self.Value = None
        self.TTL = None
        self.Status = None
        self.Operation = None
        self.ErrMsg = None
        self.Id = None


    def _deserialize(self, params):
        self.SubDomain = params.get("SubDomain")
        self.RecordType = params.get("RecordType")
        self.RecordLine = params.get("RecordLine")
        self.Value = params.get("Value")
        self.TTL = params.get("TTL")
        self.Status = params.get("Status")
        self.Operation = params.get("Operation")
        self.ErrMsg = params.get("ErrMsg")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainBatchRequest(AbstractModel):
    """CreateDomainBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param DomainList: 域名数组
        :type DomainList: list of str
        :param RecordValue: 每个域名添加 @ 和 www 的 A 记录值，记录值为IP，如果不传此参数或者传空，将只添加域名，不添加记录。
        :type RecordValue: str
        """
        self.DomainList = None
        self.RecordValue = None


    def _deserialize(self, params):
        self.DomainList = params.get("DomainList")
        self.RecordValue = params.get("RecordValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainBatchResponse(AbstractModel):
    """CreateDomainBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param DetailList: 批量添加域名信息
        :type DetailList: list of CreateDomainBatchDetail
        :param JobId: 批量任务的ID
        :type JobId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DetailList = None
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailList") is not None:
            self.DetailList = []
            for item in params.get("DetailList"):
                obj = CreateDomainBatchDetail()
                obj._deserialize(item)
                self.DetailList.append(obj)
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class CreateDomainGroupRequest(AbstractModel):
    """CreateDomainGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupName: 域名分组
        :type GroupName: str
        """
        self.GroupName = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainGroupResponse(AbstractModel):
    """CreateDomainGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 域名分组ID
        :type GroupId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreateDomainRequest(AbstractModel):
    """CreateDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param GroupId: 域名分组ID。可以通过接口DescribeDomainGroupList查看当前域名分组信息
        :type GroupId: int
        :param IsMark: 是否星标域名，”yes”、”no” 分别代表是和否。
        :type IsMark: str
        """
        self.Domain = None
        self.GroupId = None
        self.IsMark = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.GroupId = params.get("GroupId")
        self.IsMark = params.get("IsMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainResponse(AbstractModel):
    """CreateDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param DomainInfo: 域名信息
        :type DomainInfo: :class:`tencentcloud.dnspod.v20210323.models.DomainCreateInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self.DomainInfo = DomainCreateInfo()
            self.DomainInfo._deserialize(params.get("DomainInfo"))
        self.RequestId = params.get("RequestId")


class CreateRecordBatchDetail(AbstractModel):
    """批量添加记录返回结构

    """

    def __init__(self):
        r"""
        :param RecordList: 见RecordInfoBatch
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordList: list of CreateRecordBatchRecord
        :param Id: 任务编号
        :type Id: int
        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param DomainGrade: 域名等级
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainGrade: str
        :param ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param Status: 该条任务运行状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: str
        :param DomainId: 域名ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainId: int
        """
        self.RecordList = None
        self.Id = None
        self.Domain = None
        self.DomainGrade = None
        self.ErrMsg = None
        self.Status = None
        self.Operation = None
        self.DomainId = None


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = CreateRecordBatchRecord()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.Id = params.get("Id")
        self.Domain = params.get("Domain")
        self.DomainGrade = params.get("DomainGrade")
        self.ErrMsg = params.get("ErrMsg")
        self.Status = params.get("Status")
        self.Operation = params.get("Operation")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordBatchRecord(AbstractModel):
    """批量添加记录任务中的记录信息

    """

    def __init__(self):
        r"""
        :param SubDomain: 子域名(主机记录)。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubDomain: str
        :param RecordType: 记录类型, 详见 DescribeRecordType 接口
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordType: str
        :param RecordLine: 解析记录的线路，详见 DescribeRecordLineList 接口
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordLine: str
        :param Value: 记录值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param TTL: 记录的 TTL 值
注意：此字段可能返回 null，表示取不到有效值。
        :type TTL: int
        :param Status: 记录添加状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: str
        :param ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param Id: 此条记录在列表中的ID
        :type Id: int
        :param MX: 记录的MX权重
注意：此字段可能返回 null，表示取不到有效值。
        :type MX: int
        """
        self.SubDomain = None
        self.RecordType = None
        self.RecordLine = None
        self.Value = None
        self.TTL = None
        self.Status = None
        self.Operation = None
        self.ErrMsg = None
        self.Id = None
        self.MX = None


    def _deserialize(self, params):
        self.SubDomain = params.get("SubDomain")
        self.RecordType = params.get("RecordType")
        self.RecordLine = params.get("RecordLine")
        self.Value = params.get("Value")
        self.TTL = params.get("TTL")
        self.Status = params.get("Status")
        self.Operation = params.get("Operation")
        self.ErrMsg = params.get("ErrMsg")
        self.Id = params.get("Id")
        self.MX = params.get("MX")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordBatchRequest(AbstractModel):
    """CreateRecordBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param DomainIdList: 域名ID，多个 domain_id 用英文逗号进行分割。
        :type DomainIdList: list of str
        :param RecordList: 记录数组
        :type RecordList: list of AddRecordBatch
        """
        self.DomainIdList = None
        self.RecordList = None


    def _deserialize(self, params):
        self.DomainIdList = params.get("DomainIdList")
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = AddRecordBatch()
                obj._deserialize(item)
                self.RecordList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordBatchResponse(AbstractModel):
    """CreateRecordBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param DetailList: 批量添加域名信息
        :type DetailList: list of CreateRecordBatchDetail
        :param JobId: 批量任务的ID
        :type JobId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DetailList = None
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailList") is not None:
            self.DetailList = []
            for item in params.get("DetailList"):
                obj = CreateRecordBatchDetail()
                obj._deserialize(item)
                self.DetailList.append(obj)
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class CreateRecordGroupRequest(AbstractModel):
    """CreateRecordGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param GroupName: 分组名称
        :type GroupName: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.GroupName = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.GroupName = params.get("GroupName")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordGroupResponse(AbstractModel):
    """CreateRecordGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 新增的分组 ID
        :type GroupId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreateRecordRequest(AbstractModel):
    """CreateRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param RecordType: 记录类型，通过 API 记录类型获得，大写英文，比如：A 。
        :type RecordType: str
        :param RecordLine: 记录线路，通过 API 记录线路获得，中文，比如：默认。
        :type RecordLine: str
        :param Value: 记录值，如 IP : 200.200.200.200， CNAME : cname.dnspod.com.， MX : mail.dnspod.com.。
        :type Value: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        :param SubDomain: 主机记录，如 www，如果不传，默认为 @。
        :type SubDomain: str
        :param RecordLineId: 线路的 ID，通过 API 记录线路获得，英文字符串，比如：10=1。参数RecordLineId优先级高于RecordLine，如果同时传递二者，优先使用RecordLineId参数。
        :type RecordLineId: str
        :param MX: MX 优先级，当记录类型是 MX 时有效，范围1-20，MX 记录时必选。
        :type MX: int
        :param TTL: TTL，范围1-604800，不同等级域名最小值不同。
        :type TTL: int
        :param Weight: 权重信息，0到100的整数。仅企业 VIP 域名可用，0 表示关闭，不传该参数，表示不设置权重信息。
        :type Weight: int
        :param Status: 记录初始状态，取值范围为 ENABLE 和 DISABLE 。默认为 ENABLE ，如果传入 DISABLE，解析不会生效，也不会验证负载均衡的限制。
        :type Status: str
        """
        self.Domain = None
        self.RecordType = None
        self.RecordLine = None
        self.Value = None
        self.DomainId = None
        self.SubDomain = None
        self.RecordLineId = None
        self.MX = None
        self.TTL = None
        self.Weight = None
        self.Status = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RecordType = params.get("RecordType")
        self.RecordLine = params.get("RecordLine")
        self.Value = params.get("Value")
        self.DomainId = params.get("DomainId")
        self.SubDomain = params.get("SubDomain")
        self.RecordLineId = params.get("RecordLineId")
        self.MX = params.get("MX")
        self.TTL = params.get("TTL")
        self.Weight = params.get("Weight")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordResponse(AbstractModel):
    """CreateRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param RecordId: 记录ID
        :type RecordId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.RequestId = params.get("RequestId")


class CreateSnapshotRequest(AbstractModel):
    """CreateSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSnapshotResponse(AbstractModel):
    """CreateSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Deals(AbstractModel):
    """子订单号列表

    """

    def __init__(self):
        r"""
        :param DealId: 子订单ID
        :type DealId: str
        :param DealName: 子订单号
        :type DealName: str
        """
        self.DealId = None
        self.DealName = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.DealName = params.get("DealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainAliasRequest(AbstractModel):
    """DeleteDomainAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param DomainAliasId: 域名别名ID。可以通过接口DescribeDomainAliasList查到所有的域名别名列表以及对应的ID
        :type DomainAliasId: int
        :param Domain: 域名
        :type Domain: str
        :param DomainId: 域名ID，参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.DomainAliasId = None
        self.Domain = None
        self.DomainId = None


    def _deserialize(self, params):
        self.DomainAliasId = params.get("DomainAliasId")
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainAliasResponse(AbstractModel):
    """DeleteDomainAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDomainBatchDetail(AbstractModel):
    """批量删除域名详情

    """

    def __init__(self):
        r"""
        :param DomainId: 域名 ID
        :type DomainId: int
        :param Domain: 域名
        :type Domain: str
        :param Error: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: str
        :param Status: 删除状态
        :type Status: str
        :param Operation: 操作
        :type Operation: str
        """
        self.DomainId = None
        self.Domain = None
        self.Error = None
        self.Status = None
        self.Operation = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")
        self.Domain = params.get("Domain")
        self.Error = params.get("Error")
        self.Status = params.get("Status")
        self.Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainBatchRequest(AbstractModel):
    """DeleteDomainBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param DomainList: 域名数组
        :type DomainList: list of str
        """
        self.DomainList = None


    def _deserialize(self, params):
        self.DomainList = params.get("DomainList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainBatchResponse(AbstractModel):
    """DeleteDomainBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务 ID
        :type JobId: int
        :param DetailList: 任务详情数组
        :type DetailList: list of DeleteDomainBatchDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.DetailList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("DetailList") is not None:
            self.DetailList = []
            for item in params.get("DetailList"):
                obj = DeleteDomainBatchDetail()
                obj._deserialize(item)
                self.DetailList.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteDomainRequest(AbstractModel):
    """DeleteDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainResponse(AbstractModel):
    """DeleteDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRecordGroupRequest(AbstractModel):
    """DeleteRecordGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param GroupId: 分组 ID
        :type GroupId: int
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.GroupId = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.GroupId = params.get("GroupId")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordGroupResponse(AbstractModel):
    """DeleteRecordGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRecordRequest(AbstractModel):
    """DeleteRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param RecordId: 记录 ID 。可以通过接口DescribeRecordList查到所有的解析记录列表以及对应的RecordId
        :type RecordId: int
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.RecordId = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RecordId = params.get("RecordId")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordResponse(AbstractModel):
    """DeleteRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteShareDomainRequest(AbstractModel):
    """DeleteShareDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param Account: 域名共享的账号
        :type Account: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.Account = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Account = params.get("Account")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteShareDomainResponse(AbstractModel):
    """DeleteShareDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSnapshotRequest(AbstractModel):
    """DeleteSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param SnapshotId: 快照记录 ID
        :type SnapshotId: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.SnapshotId = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.SnapshotId = params.get("SnapshotId")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSnapshotResponse(AbstractModel):
    """DeleteSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeBatchTaskDetail(AbstractModel):
    """查看任务详情返回结构

    """

    def __init__(self):
        r"""
        :param RecordList: 见BatchRecordInfo
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordList: list of BatchRecordInfo
        :param Id: 任务编号
        :type Id: int
        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param DomainGrade: 域名等级
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainGrade: str
        :param ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param Status: 该条任务运行状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: str
        :param DomainId: 域名ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainId: int
        """
        self.RecordList = None
        self.Id = None
        self.Domain = None
        self.DomainGrade = None
        self.ErrMsg = None
        self.Status = None
        self.Operation = None
        self.DomainId = None


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = BatchRecordInfo()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.Id = params.get("Id")
        self.Domain = params.get("Domain")
        self.DomainGrade = params.get("DomainGrade")
        self.ErrMsg = params.get("ErrMsg")
        self.Status = params.get("Status")
        self.Operation = params.get("Operation")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchTaskRequest(AbstractModel):
    """DescribeBatchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID。操作批量接口时会返回JobId
        :type JobId: int
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchTaskResponse(AbstractModel):
    """DescribeBatchTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param DetailList: 批量任务详情
        :type DetailList: list of DescribeBatchTaskDetail
        :param TotalCount: 总任务条数
        :type TotalCount: int
        :param SuccessCount: 成功条数
        :type SuccessCount: int
        :param FailCount: 失败条数
        :type FailCount: int
        :param JobType: 批量任务类型
        :type JobType: str
        :param CreatedAt: 任务创建时间
        :type CreatedAt: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DetailList = None
        self.TotalCount = None
        self.SuccessCount = None
        self.FailCount = None
        self.JobType = None
        self.CreatedAt = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailList") is not None:
            self.DetailList = []
            for item in params.get("DetailList"):
                obj = DescribeBatchTaskDetail()
                obj._deserialize(item)
                self.DetailList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.SuccessCount = params.get("SuccessCount")
        self.FailCount = params.get("FailCount")
        self.JobType = params.get("JobType")
        self.CreatedAt = params.get("CreatedAt")
        self.RequestId = params.get("RequestId")


class DescribeDomainAliasListRequest(AbstractModel):
    """DescribeDomainAliasList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param DomainId: 域名ID,域名ID，参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainAliasListResponse(AbstractModel):
    """DescribeDomainAliasList返回参数结构体

    """

    def __init__(self):
        r"""
        :param DomainAliasList: 域名别名列表
        :type DomainAliasList: list of DomainAliasInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainAliasList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainAliasList") is not None:
            self.DomainAliasList = []
            for item in params.get("DomainAliasList"):
                obj = DomainAliasInfo()
                obj._deserialize(item)
                self.DomainAliasList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDomainAnalyticsRequest(AbstractModel):
    """DescribeDomainAnalytics请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 要查询解析量的域名
        :type Domain: str
        :param StartDate: 查询的开始时间，格式：YYYY-MM-DD
        :type StartDate: str
        :param EndDate: 查询的结束时间，格式：YYYY-MM-DD
        :type EndDate: str
        :param DnsFormat: DATE:按天维度统计 HOUR:按小时维度统计
        :type DnsFormat: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.StartDate = None
        self.EndDate = None
        self.DnsFormat = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.DnsFormat = params.get("DnsFormat")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainAnalyticsResponse(AbstractModel):
    """DescribeDomainAnalytics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 当前统计维度解析量小计
        :type Data: list of DomainAnalyticsDetail
        :param Info: 域名解析量统计查询信息
        :type Info: :class:`tencentcloud.dnspod.v20210323.models.DomainAnalyticsInfo`
        :param AliasData: 域名别名解析量统计信息
        :type AliasData: list of DomainAliasAnalyticsItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Info = None
        self.AliasData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DomainAnalyticsDetail()
                obj._deserialize(item)
                self.Data.append(obj)
        if params.get("Info") is not None:
            self.Info = DomainAnalyticsInfo()
            self.Info._deserialize(params.get("Info"))
        if params.get("AliasData") is not None:
            self.AliasData = []
            for item in params.get("AliasData"):
                obj = DomainAliasAnalyticsItem()
                obj._deserialize(item)
                self.AliasData.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDomainGroupListRequest(AbstractModel):
    """DescribeDomainGroupList请求参数结构体

    """


class DescribeDomainGroupListResponse(AbstractModel):
    """DescribeDomainGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupList: 分组列表
        :type GroupList: list of GroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.GroupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDomainListRequest(AbstractModel):
    """DescribeDomainList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 域名分组类型，默认为ALL。可取值为ALL，MINE，SHARE，ISMARK，PAUSE，VIP，RECENT，SHARE_OUT。
        :type Type: str
        :param Offset: 记录开始的偏移, 第一条记录为 0, 依次类推。默认值为0。
        :type Offset: int
        :param Limit: 要获取的域名数量, 比如获取20个, 则为20。默认值为3000。
        :type Limit: int
        :param GroupId: 分组ID, 获取指定分组的域名
        :type GroupId: int
        :param Keyword: 根据关键字搜索域名
        :type Keyword: str
        """
        self.Type = None
        self.Offset = None
        self.Limit = None
        self.GroupId = None
        self.Keyword = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.GroupId = params.get("GroupId")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainListResponse(AbstractModel):
    """DescribeDomainList返回参数结构体

    """

    def __init__(self):
        r"""
        :param DomainCountInfo: 列表页统计信息
        :type DomainCountInfo: :class:`tencentcloud.dnspod.v20210323.models.DomainCountInfo`
        :param DomainList: 域名列表
        :type DomainList: list of DomainListItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainCountInfo = None
        self.DomainList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainCountInfo") is not None:
            self.DomainCountInfo = DomainCountInfo()
            self.DomainCountInfo._deserialize(params.get("DomainCountInfo"))
        if params.get("DomainList") is not None:
            self.DomainList = []
            for item in params.get("DomainList"):
                obj = DomainListItem()
                obj._deserialize(item)
                self.DomainList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDomainLogListRequest(AbstractModel):
    """DescribeDomainLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        :param Offset: 记录开始的偏移，第一条记录为 0，依次类推，默认为0
        :type Offset: int
        :param Limit: 共要获取的日志条数，比如获取20条，则为20，默认为500条，单次最多获取500条。
        :type Limit: int
        """
        self.Domain = None
        self.DomainId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainLogListResponse(AbstractModel):
    """DescribeDomainLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogList: 域名信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LogList: list of str
        :param PageSize: 分页大小
        :type PageSize: int
        :param TotalCount: 日志总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogList = None
        self.PageSize = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogList = params.get("LogList")
        self.PageSize = params.get("PageSize")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDomainPreviewRequest(AbstractModel):
    """DescribeDomainPreview请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainPreviewResponse(AbstractModel):
    """DescribeDomainPreview返回参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名概览信息
        :type Domain: :class:`tencentcloud.dnspod.v20210323.models.PreviewDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Domain = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domain") is not None:
            self.Domain = PreviewDetail()
            self.Domain._deserialize(params.get("Domain"))
        self.RequestId = params.get("RequestId")


class DescribeDomainPurviewRequest(AbstractModel):
    """DescribeDomainPurview请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainPurviewResponse(AbstractModel):
    """DescribeDomainPurview返回参数结构体

    """

    def __init__(self):
        r"""
        :param PurviewList: 域名权限列表
        :type PurviewList: list of PurviewInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PurviewList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PurviewList") is not None:
            self.PurviewList = []
            for item in params.get("PurviewList"):
                obj = PurviewInfo()
                obj._deserialize(item)
                self.PurviewList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDomainRequest(AbstractModel):
    """DescribeDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainResponse(AbstractModel):
    """DescribeDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param DomainInfo: 域名信息
        :type DomainInfo: :class:`tencentcloud.dnspod.v20210323.models.DomainInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self.DomainInfo = DomainInfo()
            self.DomainInfo._deserialize(params.get("DomainInfo"))
        self.RequestId = params.get("RequestId")


class DescribeDomainShareInfoRequest(AbstractModel):
    """DescribeDomainShareInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainShareInfoResponse(AbstractModel):
    """DescribeDomainShareInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param ShareList: 域名共享信息
        :type ShareList: list of DomainShareInfo
        :param Owner: 域名拥有者账号
        :type Owner: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ShareList = None
        self.Owner = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ShareList") is not None:
            self.ShareList = []
            for item in params.get("ShareList"):
                obj = DomainShareInfo()
                obj._deserialize(item)
                self.ShareList.append(obj)
        self.Owner = params.get("Owner")
        self.RequestId = params.get("RequestId")


class DescribeDomainWhoisRequest(AbstractModel):
    """DescribeDomainWhois请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainWhoisResponse(AbstractModel):
    """DescribeDomainWhois返回参数结构体

    """

    def __init__(self):
        r"""
        :param Info: 域名Whois信息
        :type Info: :class:`tencentcloud.dnspod.v20210323.models.WhoisInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = WhoisInfo()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class DescribePackageDetailRequest(AbstractModel):
    """DescribePackageDetail请求参数结构体

    """


class DescribePackageDetailResponse(AbstractModel):
    """DescribePackageDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Info: 套餐配置详情
        :type Info: list of PackageDetailItem
        :param LevelMap: 套餐代码列表
        :type LevelMap: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Info = None
        self.LevelMap = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = []
            for item in params.get("Info"):
                obj = PackageDetailItem()
                obj._deserialize(item)
                self.Info.append(obj)
        self.LevelMap = params.get("LevelMap")
        self.RequestId = params.get("RequestId")


class DescribeRecordExistExceptDefaultNSRequest(AbstractModel):
    """DescribeRecordExistExceptDefaultNS请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordExistExceptDefaultNSResponse(AbstractModel):
    """DescribeRecordExistExceptDefaultNS返回参数结构体

    """

    def __init__(self):
        r"""
        :param Exist: true 是 false 否
        :type Exist: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Exist = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Exist = params.get("Exist")
        self.RequestId = params.get("RequestId")


class DescribeRecordGroupListRequest(AbstractModel):
    """DescribeRecordGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        :param Offset: 分页开始位置
        :type Offset: int
        :param Limit: 分页每页数
        :type Limit: int
        """
        self.Domain = None
        self.DomainId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordGroupListResponse(AbstractModel):
    """DescribeRecordGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupList: 分组列表
        :type GroupList: list of RecordGroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = RecordGroupInfo()
                obj._deserialize(item)
                self.GroupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRecordLineListRequest(AbstractModel):
    """DescribeRecordLineList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名。
        :type Domain: str
        :param DomainGrade: 域名等级。
+ 旧套餐：D_FREE、D_PLUS、D_EXTRA、D_EXPERT、D_ULTRA 分别对应免费套餐、个人豪华、企业1、企业2、企业3。
+ 新套餐：DP_FREE、DP_PLUS、DP_EXTRA、DP_EXPERT、DP_ULTRA 分别对应新免费、个人专业版、企业创业版、企业标准版、企业旗舰版。
        :type DomainGrade: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.DomainGrade = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainGrade = params.get("DomainGrade")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordLineListResponse(AbstractModel):
    """DescribeRecordLineList返回参数结构体

    """

    def __init__(self):
        r"""
        :param LineList: 线路列表。
        :type LineList: list of LineInfo
        :param LineGroupList: 线路分组列表。
        :type LineGroupList: list of LineGroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LineList = None
        self.LineGroupList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LineList") is not None:
            self.LineList = []
            for item in params.get("LineList"):
                obj = LineInfo()
                obj._deserialize(item)
                self.LineList.append(obj)
        if params.get("LineGroupList") is not None:
            self.LineGroupList = []
            for item in params.get("LineGroupList"):
                obj = LineGroupInfo()
                obj._deserialize(item)
                self.LineGroupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRecordListRequest(AbstractModel):
    """DescribeRecordList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 要获取的解析记录所属的域名
        :type Domain: str
        :param DomainId: 要获取的解析记录所属的域名Id，如果传了DomainId，系统将会忽略Domain参数。 可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        :param Subdomain: 解析记录的主机头，如果传了此参数，则只会返回此主机头对应的解析记录
        :type Subdomain: str
        :param RecordType: 获取某种类型的解析记录，如 A，CNAME，NS，AAAA，显性URL，隐性URL，CAA，SPF等
        :type RecordType: str
        :param RecordLine: 获取某条线路名称的解析记录。可以通过接口DescribeRecordLineList查看当前域名允许的线路信息
        :type RecordLine: str
        :param RecordLineId: 获取某个线路Id对应的解析记录，如果传RecordLineId，系统会忽略RecordLine参数。可以通过接口DescribeRecordLineList查看当前域名允许的线路信息
        :type RecordLineId: str
        :param GroupId: 获取某个分组下的解析记录时，传这个分组Id。
        :type GroupId: int
        :param Keyword: 通过关键字搜索解析记录，当前支持搜索主机头和记录值
        :type Keyword: str
        :param SortField: 排序字段，支持 name,line,type,value,weight,mx,ttl,updated_on 几个字段。
        :type SortField: str
        :param SortType: 排序方式，正序：ASC，逆序：DESC。默认值为ASC。
        :type SortType: str
        :param Offset: 偏移量，默认值为0。
        :type Offset: int
        :param Limit: 限制数量，当前Limit最大支持3000。默认值为100。
        :type Limit: int
        """
        self.Domain = None
        self.DomainId = None
        self.Subdomain = None
        self.RecordType = None
        self.RecordLine = None
        self.RecordLineId = None
        self.GroupId = None
        self.Keyword = None
        self.SortField = None
        self.SortType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        self.Subdomain = params.get("Subdomain")
        self.RecordType = params.get("RecordType")
        self.RecordLine = params.get("RecordLine")
        self.RecordLineId = params.get("RecordLineId")
        self.GroupId = params.get("GroupId")
        self.Keyword = params.get("Keyword")
        self.SortField = params.get("SortField")
        self.SortType = params.get("SortType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordListResponse(AbstractModel):
    """DescribeRecordList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RecordCountInfo: 记录的数量统计信息
        :type RecordCountInfo: :class:`tencentcloud.dnspod.v20210323.models.RecordCountInfo`
        :param RecordList: 获取的记录列表
        :type RecordList: list of RecordListItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecordCountInfo = None
        self.RecordList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RecordCountInfo") is not None:
            self.RecordCountInfo = RecordCountInfo()
            self.RecordCountInfo._deserialize(params.get("RecordCountInfo"))
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = RecordListItem()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRecordRequest(AbstractModel):
    """DescribeRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param RecordId: 记录 ID 。可以通过接口DescribeRecordList查到所有的解析记录列表以及对应的RecordId
        :type RecordId: int
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.RecordId = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RecordId = params.get("RecordId")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordResponse(AbstractModel):
    """DescribeRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param RecordInfo: 记录信息
        :type RecordInfo: :class:`tencentcloud.dnspod.v20210323.models.RecordInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecordInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RecordInfo") is not None:
            self.RecordInfo = RecordInfo()
            self.RecordInfo._deserialize(params.get("RecordInfo"))
        self.RequestId = params.get("RequestId")


class DescribeRecordSnapshotRollbackResultRequest(AbstractModel):
    """DescribeRecordSnapshotRollbackResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param JobId: 回滚任务 ID
        :type JobId: int
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.JobId = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.JobId = params.get("JobId")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordSnapshotRollbackResultResponse(AbstractModel):
    """DescribeRecordSnapshotRollbackResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 回滚任务 ID
        :type JobId: int
        :param Status: 回滚状态
        :type Status: str
        :param FailedRecordList: 失败的记录信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedRecordList: list of SnapshotRecord
        :param Domain: 所属域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Progress: 回滚进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: int
        :param LeftMinutes: 回滚剩余时间（单位：分钟）
注意：此字段可能返回 null，表示取不到有效值。
        :type LeftMinutes: int
        :param Total: 总记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Failed: 失败记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type Failed: int
        :param Success: 成功记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type Success: int
        :param CosUrl: 快照下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CosUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.Status = None
        self.FailedRecordList = None
        self.Domain = None
        self.Progress = None
        self.LeftMinutes = None
        self.Total = None
        self.Failed = None
        self.Success = None
        self.CosUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Status = params.get("Status")
        if params.get("FailedRecordList") is not None:
            self.FailedRecordList = []
            for item in params.get("FailedRecordList"):
                obj = SnapshotRecord()
                obj._deserialize(item)
                self.FailedRecordList.append(obj)
        self.Domain = params.get("Domain")
        self.Progress = params.get("Progress")
        self.LeftMinutes = params.get("LeftMinutes")
        self.Total = params.get("Total")
        self.Failed = params.get("Failed")
        self.Success = params.get("Success")
        self.CosUrl = params.get("CosUrl")
        self.RequestId = params.get("RequestId")


class DescribeRecordTypeRequest(AbstractModel):
    """DescribeRecordType请求参数结构体

    """

    def __init__(self):
        r"""
        :param DomainGrade: 域名等级。
+ 旧套餐：D_FREE、D_PLUS、D_EXTRA、D_EXPERT、D_ULTRA 分别对应免费套餐、个人豪华、企业1、企业2、企业3。
+ 新套餐：DP_FREE、DP_PLUS、DP_EXTRA、DP_EXPERT、DP_ULTRA 分别对应新免费、个人专业版、企业创业版、企业标准版、企业旗舰版。
        :type DomainGrade: str
        """
        self.DomainGrade = None


    def _deserialize(self, params):
        self.DomainGrade = params.get("DomainGrade")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordTypeResponse(AbstractModel):
    """DescribeRecordType返回参数结构体

    """

    def __init__(self):
        r"""
        :param TypeList: 记录类型列表
        :type TypeList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TypeList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TypeList = params.get("TypeList")
        self.RequestId = params.get("RequestId")


class DescribeSnapshotConfigRequest(AbstractModel):
    """DescribeSnapshotConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotConfigResponse(AbstractModel):
    """DescribeSnapshotConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param SnapshotConfig: 解析快照配置
        :type SnapshotConfig: :class:`tencentcloud.dnspod.v20210323.models.SnapshotConfig`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SnapshotConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SnapshotConfig") is not None:
            self.SnapshotConfig = SnapshotConfig()
            self.SnapshotConfig._deserialize(params.get("SnapshotConfig"))
        self.RequestId = params.get("RequestId")


class DescribeSnapshotListRequest(AbstractModel):
    """DescribeSnapshotList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotListResponse(AbstractModel):
    """DescribeSnapshotList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Info: 分页信息
        :type Info: :class:`tencentcloud.dnspod.v20210323.models.SnapshotPageInfo`
        :param SnapshotList: 快照列表
        :type SnapshotList: list of SnapshotInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Info = None
        self.SnapshotList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = SnapshotPageInfo()
            self.Info._deserialize(params.get("Info"))
        if params.get("SnapshotList") is not None:
            self.SnapshotList = []
            for item in params.get("SnapshotList"):
                obj = SnapshotInfo()
                obj._deserialize(item)
                self.SnapshotList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotRollbackResultRequest(AbstractModel):
    """DescribeSnapshotRollbackResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param TaskId: 快照回滚任务 ID
        :type TaskId: int
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.TaskId = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.TaskId = params.get("TaskId")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotRollbackResultResponse(AbstractModel):
    """DescribeSnapshotRollbackResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 快照所属域名
        :type Domain: str
        :param LeftMinutes: 回滚剩余时间（分钟）
        :type LeftMinutes: int
        :param Progress: 回滚进度百分比
        :type Progress: int
        :param SnapshotId: 快照 ID
        :type SnapshotId: str
        :param Status: 回滚状态
        :type Status: str
        :param TaskId: 快照回滚任务 ID
        :type TaskId: int
        :param Success: 成功数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Success: int
        :param Failed: 失败数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Failed: int
        :param Total: 总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param FailedRecordList: 失败详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedRecordList: list of SnapshotRecord
        :param CosUrl: 快照的下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CosUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Domain = None
        self.LeftMinutes = None
        self.Progress = None
        self.SnapshotId = None
        self.Status = None
        self.TaskId = None
        self.Success = None
        self.Failed = None
        self.Total = None
        self.FailedRecordList = None
        self.CosUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.LeftMinutes = params.get("LeftMinutes")
        self.Progress = params.get("Progress")
        self.SnapshotId = params.get("SnapshotId")
        self.Status = params.get("Status")
        self.TaskId = params.get("TaskId")
        self.Success = params.get("Success")
        self.Failed = params.get("Failed")
        self.Total = params.get("Total")
        if params.get("FailedRecordList") is not None:
            self.FailedRecordList = []
            for item in params.get("FailedRecordList"):
                obj = SnapshotRecord()
                obj._deserialize(item)
                self.FailedRecordList.append(obj)
        self.CosUrl = params.get("CosUrl")
        self.RequestId = params.get("RequestId")


class DescribeSnapshotRollbackTaskRequest(AbstractModel):
    """DescribeSnapshotRollbackTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotRollbackTaskResponse(AbstractModel):
    """DescribeSnapshotRollbackTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 快照所属域名
        :type Domain: str
        :param SnapshotId: 快照 ID
        :type SnapshotId: str
        :param Status: 回滚状态
        :type Status: str
        :param TaskId: 快照回滚任务 ID
        :type TaskId: int
        :param RecordCount: 总数量
        :type RecordCount: int
        :param CreatedOn: 开始回滚时间
        :type CreatedOn: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Domain = None
        self.SnapshotId = None
        self.Status = None
        self.TaskId = None
        self.RecordCount = None
        self.CreatedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.SnapshotId = params.get("SnapshotId")
        self.Status = params.get("Status")
        self.TaskId = params.get("TaskId")
        self.RecordCount = params.get("RecordCount")
        self.CreatedOn = params.get("CreatedOn")
        self.RequestId = params.get("RequestId")


class DescribeSubdomainAnalyticsRequest(AbstractModel):
    """DescribeSubdomainAnalytics请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 要查询解析量的域名
        :type Domain: str
        :param StartDate: 查询的开始时间，格式：YYYY-MM-DD
        :type StartDate: str
        :param EndDate: 查询的结束时间，格式：YYYY-MM-DD
        :type EndDate: str
        :param Subdomain: 要查询解析量的子域名
        :type Subdomain: str
        :param DnsFormat: DATE:按天维度统计 HOUR:按小时维度统计
        :type DnsFormat: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.StartDate = None
        self.EndDate = None
        self.Subdomain = None
        self.DnsFormat = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Subdomain = params.get("Subdomain")
        self.DnsFormat = params.get("DnsFormat")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubdomainAnalyticsResponse(AbstractModel):
    """DescribeSubdomainAnalytics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 当前统计维度解析量小计
        :type Data: list of DomainAnalyticsDetail
        :param Info: 子域名解析量统计查询信息
        :type Info: :class:`tencentcloud.dnspod.v20210323.models.SubdomainAnalyticsInfo`
        :param AliasData: 子域名别名解析量统计信息
        :type AliasData: list of SubdomainAliasAnalyticsItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Info = None
        self.AliasData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DomainAnalyticsDetail()
                obj._deserialize(item)
                self.Data.append(obj)
        if params.get("Info") is not None:
            self.Info = SubdomainAnalyticsInfo()
            self.Info._deserialize(params.get("Info"))
        if params.get("AliasData") is not None:
            self.AliasData = []
            for item in params.get("AliasData"):
                obj = SubdomainAliasAnalyticsItem()
                obj._deserialize(item)
                self.AliasData.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserDetailRequest(AbstractModel):
    """DescribeUserDetail请求参数结构体

    """


class DescribeUserDetailResponse(AbstractModel):
    """DescribeUserDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param UserInfo: 帐户信息
        :type UserInfo: :class:`tencentcloud.dnspod.v20210323.models.UserInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self.UserInfo = UserInfo()
            self.UserInfo._deserialize(params.get("UserInfo"))
        self.RequestId = params.get("RequestId")


class DescribeVASStatisticRequest(AbstractModel):
    """DescribeVASStatistic请求参数结构体

    """

    def __init__(self):
        r"""
        :param DomainId: 域名ID
        :type DomainId: int
        """
        self.DomainId = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVASStatisticResponse(AbstractModel):
    """DescribeVASStatistic返回参数结构体

    """

    def __init__(self):
        r"""
        :param VASList: 增值服务用量列表
        :type VASList: list of VASStatisticItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VASList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VASList") is not None:
            self.VASList = []
            for item in params.get("VASList"):
                obj = VASStatisticItem()
                obj._deserialize(item)
                self.VASList.append(obj)
        self.RequestId = params.get("RequestId")


class DomainAliasAnalyticsItem(AbstractModel):
    """域名别名解析量统计信息

    """

    def __init__(self):
        r"""
        :param Info: 域名解析量统计查询信息
        :type Info: :class:`tencentcloud.dnspod.v20210323.models.DomainAnalyticsInfo`
        :param Data: 当前统计维度解析量小计
        :type Data: list of DomainAnalyticsDetail
        """
        self.Info = None
        self.Data = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = DomainAnalyticsInfo()
            self.Info._deserialize(params.get("Info"))
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DomainAnalyticsDetail()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainAliasInfo(AbstractModel):
    """域名别名信息

    """

    def __init__(self):
        r"""
        :param Id: 域名别名ID
        :type Id: int
        :param DomainAlias: 域名别名
        :type DomainAlias: str
        """
        self.Id = None
        self.DomainAlias = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.DomainAlias = params.get("DomainAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainAnalyticsDetail(AbstractModel):
    """当前统计维度解析量小计

    """

    def __init__(self):
        r"""
        :param Num: 当前统计维度解析量小计
        :type Num: int
        :param DateKey: 按天统计时，为统计日期
        :type DateKey: str
        :param HourKey: 按小时统计时，为统计的当前时间的小时数(0-23)，例：HourKey为23时，统计周期为22点-23点的解析量
注意：此字段可能返回 null，表示取不到有效值。
        :type HourKey: int
        """
        self.Num = None
        self.DateKey = None
        self.HourKey = None


    def _deserialize(self, params):
        self.Num = params.get("Num")
        self.DateKey = params.get("DateKey")
        self.HourKey = params.get("HourKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainAnalyticsInfo(AbstractModel):
    """域名解析量统计查询信息

    """

    def __init__(self):
        r"""
        :param DnsFormat: DATE:按天维度统计 HOUR:按小时维度统计
        :type DnsFormat: str
        :param DnsTotal: 当前统计周期解析量总计
        :type DnsTotal: int
        :param Domain: 当前查询的域名
        :type Domain: str
        :param StartDate: 当前统计周期开始时间
        :type StartDate: str
        :param EndDate: 当前统计周期结束时间
        :type EndDate: str
        """
        self.DnsFormat = None
        self.DnsTotal = None
        self.Domain = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.DnsFormat = params.get("DnsFormat")
        self.DnsTotal = params.get("DnsTotal")
        self.Domain = params.get("Domain")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainCountInfo(AbstractModel):
    """列表页分页统计信息

    """

    def __init__(self):
        r"""
        :param DomainTotal: 符合条件的域名数量
        :type DomainTotal: int
        :param AllTotal: 用户可以查看的所有域名数量
        :type AllTotal: int
        :param MineTotal: 用户账号添加的域名数量
        :type MineTotal: int
        :param ShareTotal: 共享给用户的域名数量
        :type ShareTotal: int
        :param VipTotal: 付费域名数量
        :type VipTotal: int
        :param PauseTotal: 暂停的域名数量
        :type PauseTotal: int
        :param ErrorTotal: dns设置错误的域名数量
        :type ErrorTotal: int
        :param LockTotal: 锁定的域名数量
        :type LockTotal: int
        :param SpamTotal: 封禁的域名数量
        :type SpamTotal: int
        :param VipExpire: 30天内即将到期的域名数量
        :type VipExpire: int
        :param ShareOutTotal: 分享给其它人的域名数量
        :type ShareOutTotal: int
        :param GroupTotal: 指定分组内的域名数量
        :type GroupTotal: int
        """
        self.DomainTotal = None
        self.AllTotal = None
        self.MineTotal = None
        self.ShareTotal = None
        self.VipTotal = None
        self.PauseTotal = None
        self.ErrorTotal = None
        self.LockTotal = None
        self.SpamTotal = None
        self.VipExpire = None
        self.ShareOutTotal = None
        self.GroupTotal = None


    def _deserialize(self, params):
        self.DomainTotal = params.get("DomainTotal")
        self.AllTotal = params.get("AllTotal")
        self.MineTotal = params.get("MineTotal")
        self.ShareTotal = params.get("ShareTotal")
        self.VipTotal = params.get("VipTotal")
        self.PauseTotal = params.get("PauseTotal")
        self.ErrorTotal = params.get("ErrorTotal")
        self.LockTotal = params.get("LockTotal")
        self.SpamTotal = params.get("SpamTotal")
        self.VipExpire = params.get("VipExpire")
        self.ShareOutTotal = params.get("ShareOutTotal")
        self.GroupTotal = params.get("GroupTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainCreateInfo(AbstractModel):
    """域名信息（创建域名时返回）

    """

    def __init__(self):
        r"""
        :param Id: 域名ID
        :type Id: int
        :param Domain: 域名
        :type Domain: str
        :param Punycode: 域名的punycode
        :type Punycode: str
        :param GradeNsList: 域名的NS列表
        :type GradeNsList: list of str
        """
        self.Id = None
        self.Domain = None
        self.Punycode = None
        self.GradeNsList = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Domain = params.get("Domain")
        self.Punycode = params.get("Punycode")
        self.GradeNsList = params.get("GradeNsList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainInfo(AbstractModel):
    """域名详情

    """

    def __init__(self):
        r"""
        :param DomainId: 域名ID
        :type DomainId: int
        :param Status: 域名状态
        :type Status: str
        :param Grade: 域名套餐等级
        :type Grade: str
        :param GroupId: 域名分组ID
        :type GroupId: int
        :param IsMark: 是否星标域名
        :type IsMark: str
        :param TTL: TTL(DNS记录缓存时间)
        :type TTL: int
        :param CnameSpeedup: cname加速启用状态
        :type CnameSpeedup: str
        :param Remark: 域名备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param Punycode: 域名Punycode
        :type Punycode: str
        :param DnsStatus: 域名DNS状态
        :type DnsStatus: str
        :param DnspodNsList: 域名的NS列表
        :type DnspodNsList: list of str
        :param Domain: 域名
        :type Domain: str
        :param GradeLevel: 域名等级代号
        :type GradeLevel: int
        :param UserId: 域名所属的用户ID
        :type UserId: int
        :param IsVip: 是否为付费域名
        :type IsVip: str
        :param Owner: 域名所有者的账号
        :type Owner: str
        :param GradeTitle: 域名等级的描述
        :type GradeTitle: str
        :param CreatedOn: 域名创建时间
        :type CreatedOn: str
        :param UpdatedOn: 最后操作时间
        :type UpdatedOn: str
        :param Uin: 腾讯云账户Uin
        :type Uin: str
        :param ActualNsList: 域名实际使用的NS列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ActualNsList: list of str
        :param RecordCount: 域名的记录数量
        :type RecordCount: int
        :param OwnerNick: 域名所有者的账户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerNick: str
        """
        self.DomainId = None
        self.Status = None
        self.Grade = None
        self.GroupId = None
        self.IsMark = None
        self.TTL = None
        self.CnameSpeedup = None
        self.Remark = None
        self.Punycode = None
        self.DnsStatus = None
        self.DnspodNsList = None
        self.Domain = None
        self.GradeLevel = None
        self.UserId = None
        self.IsVip = None
        self.Owner = None
        self.GradeTitle = None
        self.CreatedOn = None
        self.UpdatedOn = None
        self.Uin = None
        self.ActualNsList = None
        self.RecordCount = None
        self.OwnerNick = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")
        self.Status = params.get("Status")
        self.Grade = params.get("Grade")
        self.GroupId = params.get("GroupId")
        self.IsMark = params.get("IsMark")
        self.TTL = params.get("TTL")
        self.CnameSpeedup = params.get("CnameSpeedup")
        self.Remark = params.get("Remark")
        self.Punycode = params.get("Punycode")
        self.DnsStatus = params.get("DnsStatus")
        self.DnspodNsList = params.get("DnspodNsList")
        self.Domain = params.get("Domain")
        self.GradeLevel = params.get("GradeLevel")
        self.UserId = params.get("UserId")
        self.IsVip = params.get("IsVip")
        self.Owner = params.get("Owner")
        self.GradeTitle = params.get("GradeTitle")
        self.CreatedOn = params.get("CreatedOn")
        self.UpdatedOn = params.get("UpdatedOn")
        self.Uin = params.get("Uin")
        self.ActualNsList = params.get("ActualNsList")
        self.RecordCount = params.get("RecordCount")
        self.OwnerNick = params.get("OwnerNick")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainListItem(AbstractModel):
    """域名列表元素

    """

    def __init__(self):
        r"""
        :param DomainId: 系统分配给域名的唯一标识
        :type DomainId: int
        :param Name: 域名的原始格式
        :type Name: str
        :param Status: 域名的状态，正常：ENABLE，暂停：PAUSE，封禁：SPAM
        :type Status: str
        :param TTL: 域名默认的解析记录默认TTL值
        :type TTL: int
        :param CNAMESpeedup: 是否开启CNAME加速，开启：ENABLE，未开启：DISABLE
        :type CNAMESpeedup: str
        :param DNSStatus: DNS 设置状态，错误：DNSERROR，正常：空字符串
        :type DNSStatus: str
        :param Grade: 域名的套餐等级代码
        :type Grade: str
        :param GroupId: 域名所属的分组Id
        :type GroupId: int
        :param SearchEnginePush: 是否开启搜索引擎推送优化，是：YES，否：NO
        :type SearchEnginePush: str
        :param Remark: 域名备注说明
        :type Remark: str
        :param Punycode: 经过punycode编码后的域名格式
        :type Punycode: str
        :param EffectiveDNS: 系统为域名分配的有效DNS
        :type EffectiveDNS: list of str
        :param GradeLevel: 域名套餐等级对应的序号
        :type GradeLevel: int
        :param GradeTitle: 套餐名称
        :type GradeTitle: str
        :param IsVip: 是否是付费套餐
        :type IsVip: str
        :param VipStartAt: 付费套餐开通时间
        :type VipStartAt: str
        :param VipEndAt: 付费套餐到期时间
        :type VipEndAt: str
        :param VipAutoRenew: 域名是否开通VIP自动续费，是：YES，否：NO，默认：DEFAULT
        :type VipAutoRenew: str
        :param RecordCount: 域名下的记录数量
        :type RecordCount: int
        :param CreatedOn: 域名添加时间
        :type CreatedOn: str
        :param UpdatedOn: 域名更新时间
        :type UpdatedOn: str
        :param Owner: 域名所属账号
        :type Owner: str
        """
        self.DomainId = None
        self.Name = None
        self.Status = None
        self.TTL = None
        self.CNAMESpeedup = None
        self.DNSStatus = None
        self.Grade = None
        self.GroupId = None
        self.SearchEnginePush = None
        self.Remark = None
        self.Punycode = None
        self.EffectiveDNS = None
        self.GradeLevel = None
        self.GradeTitle = None
        self.IsVip = None
        self.VipStartAt = None
        self.VipEndAt = None
        self.VipAutoRenew = None
        self.RecordCount = None
        self.CreatedOn = None
        self.UpdatedOn = None
        self.Owner = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.TTL = params.get("TTL")
        self.CNAMESpeedup = params.get("CNAMESpeedup")
        self.DNSStatus = params.get("DNSStatus")
        self.Grade = params.get("Grade")
        self.GroupId = params.get("GroupId")
        self.SearchEnginePush = params.get("SearchEnginePush")
        self.Remark = params.get("Remark")
        self.Punycode = params.get("Punycode")
        self.EffectiveDNS = params.get("EffectiveDNS")
        self.GradeLevel = params.get("GradeLevel")
        self.GradeTitle = params.get("GradeTitle")
        self.IsVip = params.get("IsVip")
        self.VipStartAt = params.get("VipStartAt")
        self.VipEndAt = params.get("VipEndAt")
        self.VipAutoRenew = params.get("VipAutoRenew")
        self.RecordCount = params.get("RecordCount")
        self.CreatedOn = params.get("CreatedOn")
        self.UpdatedOn = params.get("UpdatedOn")
        self.Owner = params.get("Owner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainShareInfo(AbstractModel):
    """域名共享信息

    """

    def __init__(self):
        r"""
        :param ShareTo: 域名共享对象的账号
        :type ShareTo: str
        :param Mode: 共享模式，“rw”：可读写。 “r”:：只读
        :type Mode: str
        :param Status: 共享状态“enabled”：共享成功。“pending”：共享到的账号不存在, 等待注册
        :type Status: str
        """
        self.ShareTo = None
        self.Mode = None
        self.Status = None


    def _deserialize(self, params):
        self.ShareTo = params.get("ShareTo")
        self.Mode = params.get("Mode")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadSnapshotRequest(AbstractModel):
    """DownloadSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param SnapshotId: 快照记录 ID
        :type SnapshotId: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.SnapshotId = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.SnapshotId = params.get("SnapshotId")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadSnapshotResponse(AbstractModel):
    """DownloadSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param CosUrl: 快照下载链接
        :type CosUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CosUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CosUrl = params.get("CosUrl")
        self.RequestId = params.get("RequestId")


class GroupInfo(AbstractModel):
    """域名分组列表

    """

    def __init__(self):
        r"""
        :param GroupId: 分组ID
        :type GroupId: int
        :param GroupName: 分组名称
        :type GroupName: str
        :param GroupType: 分组类型
        :type GroupType: str
        :param Size: 该分组中域名个数
        :type Size: int
        """
        self.GroupId = None
        self.GroupName = None
        self.GroupType = None
        self.Size = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.GroupType = params.get("GroupType")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    """键值对

    """

    def __init__(self):
        r"""
        :param Key: 键
        :type Key: str
        :param Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LineGroupInfo(AbstractModel):
    """线路分组信息

    """

    def __init__(self):
        r"""
        :param LineId: 线路分组ID
        :type LineId: str
        :param Name: 线路分组名称
        :type Name: str
        :param Type: 分组类型
        :type Type: str
        :param LineList: 线路分组包含的线路列表
        :type LineList: list of str
        """
        self.LineId = None
        self.Name = None
        self.Type = None
        self.LineList = None


    def _deserialize(self, params):
        self.LineId = params.get("LineId")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.LineList = params.get("LineList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LineInfo(AbstractModel):
    """解析线路信息

    """

    def __init__(self):
        r"""
        :param Name: 线路名称
        :type Name: str
        :param LineId: 线路ID
        :type LineId: str
        """
        self.Name = None
        self.LineId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.LineId = params.get("LineId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LockInfo(AbstractModel):
    """域名锁定信息

    """

    def __init__(self):
        r"""
        :param DomainId: 域名 ID
        :type DomainId: int
        :param LockCode: 域名解锁码
        :type LockCode: str
        :param LockEnd: 域名自动解锁日期
        :type LockEnd: str
        """
        self.DomainId = None
        self.LockCode = None
        self.LockEnd = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")
        self.LockCode = params.get("LockCode")
        self.LockEnd = params.get("LockEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainLockRequest(AbstractModel):
    """ModifyDomainLock请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param LockDays: 域名要锁定的天数，最多可锁定的天数可以通过获取域名权限接口获取。
        :type LockDays: int
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.LockDays = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.LockDays = params.get("LockDays")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainLockResponse(AbstractModel):
    """ModifyDomainLock返回参数结构体

    """

    def __init__(self):
        r"""
        :param LockInfo: 域名锁定信息
        :type LockInfo: :class:`tencentcloud.dnspod.v20210323.models.LockInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LockInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LockInfo") is not None:
            self.LockInfo = LockInfo()
            self.LockInfo._deserialize(params.get("LockInfo"))
        self.RequestId = params.get("RequestId")


class ModifyDomainOwnerRequest(AbstractModel):
    """ModifyDomainOwner请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param Account: 域名需要转入的账号，支持Uin或者邮箱格式
        :type Account: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.Account = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Account = params.get("Account")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainOwnerResponse(AbstractModel):
    """ModifyDomainOwner返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDomainRemarkRequest(AbstractModel):
    """ModifyDomainRemark请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        :param Remark: 域名备注，删除备注请提交空内容。
        :type Remark: str
        """
        self.Domain = None
        self.DomainId = None
        self.Remark = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainRemarkResponse(AbstractModel):
    """ModifyDomainRemark返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDomainStatusRequest(AbstractModel):
    """ModifyDomainStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param Status: 域名状态，”enable” 、”disable” 分别代表启用和暂停
        :type Status: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.Status = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Status = params.get("Status")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainStatusResponse(AbstractModel):
    """ModifyDomainStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDomainUnlockRequest(AbstractModel):
    """ModifyDomainUnlock请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param LockCode: 域名解锁码，锁定的时候会返回。
        :type LockCode: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.LockCode = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.LockCode = params.get("LockCode")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainUnlockResponse(AbstractModel):
    """ModifyDomainUnlock返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDynamicDNSRequest(AbstractModel):
    """ModifyDynamicDNS请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param RecordId: 记录ID。 可以通过接口DescribeRecordList查到所有的解析记录列表以及对应的RecordId
        :type RecordId: int
        :param RecordLine: 记录线路，通过 API 记录线路获得，中文，比如：默认。
        :type RecordLine: str
        :param Value: 记录值，如 IP : 200.200.200.200， CNAME : cname.dnspod.com.， MX : mail.dnspod.com.。
        :type Value: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        :param SubDomain: 主机记录，如 www，如果不传，默认为 @。
        :type SubDomain: str
        :param RecordLineId: 线路的 ID，通过 API 记录线路获得，英文字符串，比如：10=1。参数RecordLineId优先级高于RecordLine，如果同时传递二者，优先使用RecordLineId参数。
        :type RecordLineId: str
        :param Ttl: TTL值，如果不传，默认为域名的TTL值。
        :type Ttl: int
        """
        self.Domain = None
        self.RecordId = None
        self.RecordLine = None
        self.Value = None
        self.DomainId = None
        self.SubDomain = None
        self.RecordLineId = None
        self.Ttl = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RecordId = params.get("RecordId")
        self.RecordLine = params.get("RecordLine")
        self.Value = params.get("Value")
        self.DomainId = params.get("DomainId")
        self.SubDomain = params.get("SubDomain")
        self.RecordLineId = params.get("RecordLineId")
        self.Ttl = params.get("Ttl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDynamicDNSResponse(AbstractModel):
    """ModifyDynamicDNS返回参数结构体

    """

    def __init__(self):
        r"""
        :param RecordId: 记录ID
        :type RecordId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.RequestId = params.get("RequestId")


class ModifyPackageAutoRenewRequest(AbstractModel):
    """ModifyPackageAutoRenew请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源ID。可以在控制台查看所有的资源
        :type ResourceId: str
        :param Status: enable 开启自动续费；disable 关闭自动续费
        :type Status: str
        """
        self.ResourceId = None
        self.Status = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPackageAutoRenewResponse(AbstractModel):
    """ModifyPackageAutoRenew返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRecordBatchDetail(AbstractModel):
    """批量添加记录返回结构

    """

    def __init__(self):
        r"""
        :param RecordList: 见RecordInfoBatchModify
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordList: list of BatchRecordInfo
        :param Id: 任务编号
        :type Id: int
        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param DomainGrade: 域名等级
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainGrade: str
        :param ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param Status: 该条任务运行状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: str
        :param DomainId: 域名ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainId: int
        """
        self.RecordList = None
        self.Id = None
        self.Domain = None
        self.DomainGrade = None
        self.ErrMsg = None
        self.Status = None
        self.Operation = None
        self.DomainId = None


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = BatchRecordInfo()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.Id = params.get("Id")
        self.Domain = params.get("Domain")
        self.DomainGrade = params.get("DomainGrade")
        self.ErrMsg = params.get("ErrMsg")
        self.Status = params.get("Status")
        self.Operation = params.get("Operation")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordBatchRequest(AbstractModel):
    """ModifyRecordBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param RecordIdList: 记录ID数组。可以通过接口DescribeRecordList查到所有的解析记录列表以及对应的RecordId
        :type RecordIdList: list of int non-negative
        :param Change: 要修改的字段，可选值为 [“sub_domain”、”record_type”、”area”、”value”、”mx”、”ttl”、”status”] 中的某一个。
        :type Change: str
        :param ChangeTo: 修改为，具体依赖 change 字段，必填参数。
        :type ChangeTo: str
        :param Value: 要修改到的记录值，仅当 change 字段为 “record_type” 时为必填参数。
        :type Value: str
        :param MX: MX记录优先级，仅当修改为 MX 记录时为必填参数。
        :type MX: str
        """
        self.RecordIdList = None
        self.Change = None
        self.ChangeTo = None
        self.Value = None
        self.MX = None


    def _deserialize(self, params):
        self.RecordIdList = params.get("RecordIdList")
        self.Change = params.get("Change")
        self.ChangeTo = params.get("ChangeTo")
        self.Value = params.get("Value")
        self.MX = params.get("MX")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordBatchResponse(AbstractModel):
    """ModifyRecordBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 批量任务ID
        :type JobId: int
        :param DetailList: 见modifyRecordBatchDetail
        :type DetailList: list of ModifyRecordBatchDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.DetailList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("DetailList") is not None:
            self.DetailList = []
            for item in params.get("DetailList"):
                obj = ModifyRecordBatchDetail()
                obj._deserialize(item)
                self.DetailList.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyRecordFieldsRequest(AbstractModel):
    """ModifyRecordFields请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param RecordId: 记录 ID 。
        :type RecordId: int
        :param FieldList: 要修改的记录属性和值，支持：sub_domain，record_line，record_line_id，record_type，value，ttl，status，mx，weight
        :type FieldList: list of KeyValue
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.RecordId = None
        self.FieldList = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RecordId = params.get("RecordId")
        if params.get("FieldList") is not None:
            self.FieldList = []
            for item in params.get("FieldList"):
                obj = KeyValue()
                obj._deserialize(item)
                self.FieldList.append(obj)
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordFieldsResponse(AbstractModel):
    """ModifyRecordFields返回参数结构体

    """

    def __init__(self):
        r"""
        :param RecordId: 记录ID
        :type RecordId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.RequestId = params.get("RequestId")


class ModifyRecordGroupRequest(AbstractModel):
    """ModifyRecordGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param GroupName: 分组名称
        :type GroupName: str
        :param GroupId: 要修改的分组 ID
        :type GroupId: int
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.GroupName = None
        self.GroupId = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordGroupResponse(AbstractModel):
    """ModifyRecordGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 修改的分组 ID
        :type GroupId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class ModifyRecordRemarkRequest(AbstractModel):
    """ModifyRecordRemark请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param RecordId: 记录 ID 。可以通过接口DescribeRecordList查到所有的解析记录列表以及对应的RecordId
        :type RecordId: int
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        :param Remark: 解析记录备注，删除备注请提交空内容。
        :type Remark: str
        """
        self.Domain = None
        self.RecordId = None
        self.DomainId = None
        self.Remark = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RecordId = params.get("RecordId")
        self.DomainId = params.get("DomainId")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordRemarkResponse(AbstractModel):
    """ModifyRecordRemark返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRecordRequest(AbstractModel):
    """ModifyRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param RecordType: 记录类型，通过 API 记录类型获得，大写英文，比如：A 。
        :type RecordType: str
        :param RecordLine: 记录线路，通过 API 记录线路获得，中文，比如：默认。
        :type RecordLine: str
        :param Value: 记录值，如 IP : 200.200.200.200， CNAME : cname.dnspod.com.， MX : mail.dnspod.com.。
        :type Value: str
        :param RecordId: 记录 ID 。可以通过接口DescribeRecordList查到所有的解析记录列表以及对应的RecordId
        :type RecordId: int
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        :param SubDomain: 主机记录，如 www，如果不传，默认为 @。
        :type SubDomain: str
        :param RecordLineId: 线路的 ID，通过 API 记录线路获得，英文字符串，比如：10=1。参数RecordLineId优先级高于RecordLine，如果同时传递二者，优先使用RecordLineId参数。
        :type RecordLineId: str
        :param MX: MX 优先级，当记录类型是 MX 时有效，范围1-20，MX 记录时必选。
        :type MX: int
        :param TTL: TTL，范围1-604800，不同等级域名最小值不同。
        :type TTL: int
        :param Weight: 权重信息，0到100的整数。仅企业 VIP 域名可用，0 表示关闭，不传该参数，表示不设置权重信息。
        :type Weight: int
        :param Status: 记录初始状态，取值范围为 ENABLE 和 DISABLE 。默认为 ENABLE ，如果传入 DISABLE，解析不会生效，也不会验证负载均衡的限制。
        :type Status: str
        """
        self.Domain = None
        self.RecordType = None
        self.RecordLine = None
        self.Value = None
        self.RecordId = None
        self.DomainId = None
        self.SubDomain = None
        self.RecordLineId = None
        self.MX = None
        self.TTL = None
        self.Weight = None
        self.Status = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RecordType = params.get("RecordType")
        self.RecordLine = params.get("RecordLine")
        self.Value = params.get("Value")
        self.RecordId = params.get("RecordId")
        self.DomainId = params.get("DomainId")
        self.SubDomain = params.get("SubDomain")
        self.RecordLineId = params.get("RecordLineId")
        self.MX = params.get("MX")
        self.TTL = params.get("TTL")
        self.Weight = params.get("Weight")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordResponse(AbstractModel):
    """ModifyRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param RecordId: 记录ID
        :type RecordId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.RequestId = params.get("RequestId")


class ModifyRecordStatusRequest(AbstractModel):
    """ModifyRecordStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param RecordId: 记录 ID 。可以通过接口DescribeRecordList查到所有的解析记录列表以及对应的RecordId
        :type RecordId: int
        :param Status: 记录的状态。取值范围为 ENABLE 和 DISABLE。如果传入 DISABLE，解析不会生效，也不会验证负载均衡的限制。
        :type Status: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        """
        self.Domain = None
        self.RecordId = None
        self.Status = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RecordId = params.get("RecordId")
        self.Status = params.get("Status")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordStatusResponse(AbstractModel):
    """ModifyRecordStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RecordId: 记录ID。
        :type RecordId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.RequestId = params.get("RequestId")


class ModifyRecordToGroupRequest(AbstractModel):
    """ModifyRecordToGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param GroupId: 分组 ID
        :type GroupId: int
        :param RecordId: 记录 ID，多个 ID 用竖线“|”分割
        :type RecordId: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.GroupId = None
        self.RecordId = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.GroupId = params.get("GroupId")
        self.RecordId = params.get("RecordId")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordToGroupResponse(AbstractModel):
    """ModifyRecordToGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySnapshotConfigRequest(AbstractModel):
    """ModifySnapshotConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param Period: 备件间隔：空字符串-不备份，half_hour-每半小时，hourly-每小时，daily-每天，monthly-每月
        :type Period: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.Period = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Period = params.get("Period")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotConfigResponse(AbstractModel):
    """ModifySnapshotConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubdomainStatusRequest(AbstractModel):
    """ModifySubdomainStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param RecordType: 记录类型。允许的值为A、CNAME、MX、TXT、NS、AAAA、SPF、SRV、CAA、URL、URL1。若要传多个，用英文逗号分隔，例如A,TXT,CNAME。
        :type RecordType: str
        :param Status: 记录状态。允许的值为disable。
        :type Status: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。可以通过接口DescribeDomainList查到所有的Domain以及DomainId
        :type DomainId: int
        :param SubDomain: 主机记录，如 www，如果不传，默认为 @。
        :type SubDomain: str
        """
        self.Domain = None
        self.RecordType = None
        self.Status = None
        self.DomainId = None
        self.SubDomain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RecordType = params.get("RecordType")
        self.Status = params.get("Status")
        self.DomainId = params.get("DomainId")
        self.SubDomain = params.get("SubDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubdomainStatusResponse(AbstractModel):
    """ModifySubdomainStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVasAutoRenewStatusRequest(AbstractModel):
    """ModifyVasAutoRenewStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源ID。可以从控制台查看所有的资源
        :type ResourceId: str
        :param Status: enable 开启自动续费；disable 关闭自动续费
        :type Status: str
        """
        self.ResourceId = None
        self.Status = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVasAutoRenewStatusResponse(AbstractModel):
    """ModifyVasAutoRenewStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PackageDetailItem(AbstractModel):
    """套餐配置明细

    """

    def __init__(self):
        r"""
        :param RealPrice: 套餐原价
        :type RealPrice: int
        :param ChangedTimes: 可更换域名次数
        :type ChangedTimes: int
        :param MinTtl: 允许设置的最小 TTL 值
        :type MinTtl: int
        :param RecordRoll: 负载均衡数量
        :type RecordRoll: int
        :param SubDomainLevel: 子域名级数
        :type SubDomainLevel: int
        :param MaxWildcard: 泛解析级数
        :type MaxWildcard: int
        :param DnsServerRegion: DNS 服务集群个数
        :type DnsServerRegion: str
        :param DomainGradeCn: 套餐名称
        :type DomainGradeCn: str
        :param GradeLevel: 套餐代号
        :type GradeLevel: int
        :param Ns: 套餐对应的 NS
        :type Ns: list of str
        :param DomainGrade: 套餐代码
        :type DomainGrade: str
        """
        self.RealPrice = None
        self.ChangedTimes = None
        self.MinTtl = None
        self.RecordRoll = None
        self.SubDomainLevel = None
        self.MaxWildcard = None
        self.DnsServerRegion = None
        self.DomainGradeCn = None
        self.GradeLevel = None
        self.Ns = None
        self.DomainGrade = None


    def _deserialize(self, params):
        self.RealPrice = params.get("RealPrice")
        self.ChangedTimes = params.get("ChangedTimes")
        self.MinTtl = params.get("MinTtl")
        self.RecordRoll = params.get("RecordRoll")
        self.SubDomainLevel = params.get("SubDomainLevel")
        self.MaxWildcard = params.get("MaxWildcard")
        self.DnsServerRegion = params.get("DnsServerRegion")
        self.DomainGradeCn = params.get("DomainGradeCn")
        self.GradeLevel = params.get("GradeLevel")
        self.Ns = params.get("Ns")
        self.DomainGrade = params.get("DomainGrade")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayOrderWithBalanceRequest(AbstractModel):
    """PayOrderWithBalance请求参数结构体

    """

    def __init__(self):
        r"""
        :param BigDealIdList: 需要支付的大订单号数组
        :type BigDealIdList: list of str
        :param VoucherIdList: 代金券ID数组。可以从控制台查到拥有的代金券
        :type VoucherIdList: list of str
        """
        self.BigDealIdList = None
        self.VoucherIdList = None


    def _deserialize(self, params):
        self.BigDealIdList = params.get("BigDealIdList")
        self.VoucherIdList = params.get("VoucherIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayOrderWithBalanceResponse(AbstractModel):
    """PayOrderWithBalance返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealIdList: 此次操作支付成功的订单id数组
        :type DealIdList: list of str
        :param BigDealIdList: 此次操作支付成功的大订单号数组
        :type BigDealIdList: list of str
        :param DealNameList: 此次操作支付成功的订单号数组
        :type DealNameList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealIdList = None
        self.BigDealIdList = None
        self.DealNameList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealIdList = params.get("DealIdList")
        self.BigDealIdList = params.get("BigDealIdList")
        self.DealNameList = params.get("DealNameList")
        self.RequestId = params.get("RequestId")


class PreviewDetail(AbstractModel):
    """域名概览明细

    """

    def __init__(self):
        r"""
        :param Name: 域名
        :type Name: str
        :param Grade: 域名套餐代码
        :type Grade: str
        :param GradeTitle: 域名套餐名称
        :type GradeTitle: str
        :param Records: 域名记录数
        :type Records: int
        :param DomainParkingStatus: 域名停靠状态。0 未开启 1 已开启 2 已暂停
        :type DomainParkingStatus: int
        :param LineCount: 自定义线路数量
        :type LineCount: int
        :param LineGroupCount: 自定义线路分组数量
        :type LineGroupCount: int
        :param AliasCount: 域名别名数量
        :type AliasCount: int
        :param MaxAliasCount: 允许添加的最大域名别名数量
        :type MaxAliasCount: int
        :param ResolveCount: 昨天的解析量
        :type ResolveCount: int
        :param VASCount: 增值服务数量
        :type VASCount: int
        """
        self.Name = None
        self.Grade = None
        self.GradeTitle = None
        self.Records = None
        self.DomainParkingStatus = None
        self.LineCount = None
        self.LineGroupCount = None
        self.AliasCount = None
        self.MaxAliasCount = None
        self.ResolveCount = None
        self.VASCount = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Grade = params.get("Grade")
        self.GradeTitle = params.get("GradeTitle")
        self.Records = params.get("Records")
        self.DomainParkingStatus = params.get("DomainParkingStatus")
        self.LineCount = params.get("LineCount")
        self.LineGroupCount = params.get("LineGroupCount")
        self.AliasCount = params.get("AliasCount")
        self.MaxAliasCount = params.get("MaxAliasCount")
        self.ResolveCount = params.get("ResolveCount")
        self.VASCount = params.get("VASCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurviewInfo(AbstractModel):
    """域名权限项

    """

    def __init__(self):
        r"""
        :param Name: 权限名称
        :type Name: str
        :param Value: 权限值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordCountInfo(AbstractModel):
    """查询记录列表的数量统计信息

    """

    def __init__(self):
        r"""
        :param SubdomainCount: 子域名数量
        :type SubdomainCount: int
        :param ListCount: 列表返回的记录数
        :type ListCount: int
        :param TotalCount: 总的记录数
        :type TotalCount: int
        """
        self.SubdomainCount = None
        self.ListCount = None
        self.TotalCount = None


    def _deserialize(self, params):
        self.SubdomainCount = params.get("SubdomainCount")
        self.ListCount = params.get("ListCount")
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordGroupInfo(AbstractModel):
    """解析记录分组信息

    """

    def __init__(self):
        r"""
        :param GroupId: 分组 ID
        :type GroupId: int
        :param GroupName: 分组名称
        :type GroupName: str
        :param GroupType: 分组类型：system-系统；user-用户
        :type GroupType: str
        """
        self.GroupId = None
        self.GroupName = None
        self.GroupType = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.GroupType = params.get("GroupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordInfo(AbstractModel):
    """记录信息

    """

    def __init__(self):
        r"""
        :param Id: 记录 ID 。
        :type Id: int
        :param SubDomain: 子域名(主机记录)。
        :type SubDomain: str
        :param RecordType: 记录类型, 详见 DescribeRecordType 接口。
        :type RecordType: str
        :param RecordLine: 解析记录的线路，详见 DescribeRecordLineList 接口。
        :type RecordLine: str
        :param RecordLineId: 解析记录的线路 ID ，详见 DescribeRecordLineList 接口。
        :type RecordLineId: str
        :param Value: 记录值。
        :type Value: str
        :param Weight: 记录权重值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param MX: 记录的 MX 记录值，非 MX 记录类型，默认为 0。
        :type MX: int
        :param TTL: 记录的 TTL 值。
        :type TTL: int
        :param Enabled: 记录状态。0表示禁用，1表示启用。
        :type Enabled: int
        :param MonitorStatus: 该记录的 D 监控状态。
"Ok" : 服务器正常。
"Warn" : 该记录有报警, 服务器返回 4XX。
"Down" : 服务器宕机。
"" : 该记录未开启 D 监控。
        :type MonitorStatus: str
        :param Remark: 记录的备注。
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param UpdatedOn: 记录最后更新时间。
        :type UpdatedOn: str
        :param DomainId: 域名 ID 。
        :type DomainId: int
        """
        self.Id = None
        self.SubDomain = None
        self.RecordType = None
        self.RecordLine = None
        self.RecordLineId = None
        self.Value = None
        self.Weight = None
        self.MX = None
        self.TTL = None
        self.Enabled = None
        self.MonitorStatus = None
        self.Remark = None
        self.UpdatedOn = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.SubDomain = params.get("SubDomain")
        self.RecordType = params.get("RecordType")
        self.RecordLine = params.get("RecordLine")
        self.RecordLineId = params.get("RecordLineId")
        self.Value = params.get("Value")
        self.Weight = params.get("Weight")
        self.MX = params.get("MX")
        self.TTL = params.get("TTL")
        self.Enabled = params.get("Enabled")
        self.MonitorStatus = params.get("MonitorStatus")
        self.Remark = params.get("Remark")
        self.UpdatedOn = params.get("UpdatedOn")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordListItem(AbstractModel):
    """记录列表元素

    """

    def __init__(self):
        r"""
        :param RecordId: 记录Id
        :type RecordId: int
        :param Value: 记录值
        :type Value: str
        :param Status: 记录状态，启用：ENABLE，暂停：DISABLE
        :type Status: str
        :param UpdatedOn: 更新时间
        :type UpdatedOn: str
        :param Name: 主机名
        :type Name: str
        :param Line: 记录线路
        :type Line: str
        :param LineId: 线路Id
        :type LineId: str
        :param Type: 记录类型
        :type Type: str
        :param Weight: 记录权重，用于负载均衡记录
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param MonitorStatus: 记录监控状态，正常：OK，告警：WARN，宕机：DOWN，未设置监控或监控暂停则为空
        :type MonitorStatus: str
        :param Remark: 记录备注说明
        :type Remark: str
        :param TTL: 记录缓存时间
        :type TTL: int
        :param MX: MX值，只有MX记录有
注意：此字段可能返回 null，表示取不到有效值。
        :type MX: int
        :param DefaultNS: 是否是默认的ns记录
        :type DefaultNS: bool
        """
        self.RecordId = None
        self.Value = None
        self.Status = None
        self.UpdatedOn = None
        self.Name = None
        self.Line = None
        self.LineId = None
        self.Type = None
        self.Weight = None
        self.MonitorStatus = None
        self.Remark = None
        self.TTL = None
        self.MX = None
        self.DefaultNS = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.Value = params.get("Value")
        self.Status = params.get("Status")
        self.UpdatedOn = params.get("UpdatedOn")
        self.Name = params.get("Name")
        self.Line = params.get("Line")
        self.LineId = params.get("LineId")
        self.Type = params.get("Type")
        self.Weight = params.get("Weight")
        self.MonitorStatus = params.get("MonitorStatus")
        self.Remark = params.get("Remark")
        self.TTL = params.get("TTL")
        self.MX = params.get("MX")
        self.DefaultNS = params.get("DefaultNS")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackRecordSnapshotRequest(AbstractModel):
    """RollbackRecordSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param SnapshotId: 快照 ID
        :type SnapshotId: str
        :param RecordList: 解析记录信息
        :type RecordList: list of SnapshotRecord
        :param TaskId: 之前的快照回滚任务 ID
        :type TaskId: int
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.SnapshotId = None
        self.RecordList = None
        self.TaskId = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.SnapshotId = params.get("SnapshotId")
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = SnapshotRecord()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.TaskId = params.get("TaskId")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackRecordSnapshotResponse(AbstractModel):
    """RollbackRecordSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 回滚任务 ID
        :type JobId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class RollbackSnapshotRequest(AbstractModel):
    """RollbackSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param SnapshotId: 快照记录 ID
        :type SnapshotId: str
        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。
        :type DomainId: int
        """
        self.Domain = None
        self.SnapshotId = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.SnapshotId = params.get("SnapshotId")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackSnapshotResponse(AbstractModel):
    """RollbackSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 回滚任务 ID，用来查询回滚状态
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SnapshotConfig(AbstractModel):
    """域名解析快照配置

    """

    def __init__(self):
        r"""
        :param Config: 配置类型：空字符串-不备份，half_hour-每半小时，hourly-每小时，daily-每天，monthly-每月
        :type Config: str
        :param CreatedOn: 添加时间
        :type CreatedOn: str
        :param DomainId: 所属域名 ID
        :type DomainId: str
        :param Id: 配置 ID
        :type Id: str
        :param SnapshotCount: 快照数量
        :type SnapshotCount: int
        :param Status: 状态：enable-启用，disable-禁用
        :type Status: str
        :param UpdatedOn: 更新时间
        :type UpdatedOn: str
        """
        self.Config = None
        self.CreatedOn = None
        self.DomainId = None
        self.Id = None
        self.SnapshotCount = None
        self.Status = None
        self.UpdatedOn = None


    def _deserialize(self, params):
        self.Config = params.get("Config")
        self.CreatedOn = params.get("CreatedOn")
        self.DomainId = params.get("DomainId")
        self.Id = params.get("Id")
        self.SnapshotCount = params.get("SnapshotCount")
        self.Status = params.get("Status")
        self.UpdatedOn = params.get("UpdatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotInfo(AbstractModel):
    """快照信息

    """

    def __init__(self):
        r"""
        :param CosUrl: 快照的对象存储地址
        :type CosUrl: str
        :param CreatedOn: 添加时间
        :type CreatedOn: str
        :param Domain: 所属域名
        :type Domain: str
        :param Id: 快照记录 ID
        :type Id: str
        :param RecordCount: 域名解析记录数
        :type RecordCount: str
        :param Status: 状态：normal-正常，create-备份中
        :type Status: str
        """
        self.CosUrl = None
        self.CreatedOn = None
        self.Domain = None
        self.Id = None
        self.RecordCount = None
        self.Status = None


    def _deserialize(self, params):
        self.CosUrl = params.get("CosUrl")
        self.CreatedOn = params.get("CreatedOn")
        self.Domain = params.get("Domain")
        self.Id = params.get("Id")
        self.RecordCount = params.get("RecordCount")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotPageInfo(AbstractModel):
    """快照列表分页信息

    """

    def __init__(self):
        r"""
        :param Total: 快照总数
        :type Total: int
        """
        self.Total = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotRecord(AbstractModel):
    """快照解析记录

    """

    def __init__(self):
        r"""
        :param SubDomain: 子域名
        :type SubDomain: str
        :param RecordType: 记录类型
        :type RecordType: str
        :param RecordLine: 解析线路
        :type RecordLine: str
        :param Value: 解析值
        :type Value: str
        :param TTL: TTL(秒)
        :type TTL: str
        :param RecordId: 解析记录 ID
        :type RecordId: str
        :param MX: MX优先级
注意：此字段可能返回 null，表示取不到有效值。
        :type MX: str
        """
        self.SubDomain = None
        self.RecordType = None
        self.RecordLine = None
        self.Value = None
        self.TTL = None
        self.RecordId = None
        self.MX = None


    def _deserialize(self, params):
        self.SubDomain = params.get("SubDomain")
        self.RecordType = params.get("RecordType")
        self.RecordLine = params.get("RecordLine")
        self.Value = params.get("Value")
        self.TTL = params.get("TTL")
        self.RecordId = params.get("RecordId")
        self.MX = params.get("MX")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubdomainAliasAnalyticsItem(AbstractModel):
    """子域名别名解析量统计信息

    """

    def __init__(self):
        r"""
        :param Info: 子域名解析量统计查询信息
        :type Info: :class:`tencentcloud.dnspod.v20210323.models.SubdomainAnalyticsInfo`
        :param Data: 当前统计维度解析量小计
        :type Data: list of DomainAnalyticsDetail
        """
        self.Info = None
        self.Data = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = SubdomainAnalyticsInfo()
            self.Info._deserialize(params.get("Info"))
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DomainAnalyticsDetail()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubdomainAnalyticsInfo(AbstractModel):
    """子域名解析量统计查询信息

    """

    def __init__(self):
        r"""
        :param DnsFormat: DATE:按天维度统计 HOUR:按小时维度统计
        :type DnsFormat: str
        :param DnsTotal: 当前统计周期解析量总计
        :type DnsTotal: int
        :param Domain: 当前查询的域名
        :type Domain: str
        :param StartDate: 当前统计周期开始时间
        :type StartDate: str
        :param EndDate: 当前统计周期结束时间
        :type EndDate: str
        :param Subdomain: 当前统计的子域名
        :type Subdomain: str
        """
        self.DnsFormat = None
        self.DnsTotal = None
        self.Domain = None
        self.StartDate = None
        self.EndDate = None
        self.Subdomain = None


    def _deserialize(self, params):
        self.DnsFormat = params.get("DnsFormat")
        self.DnsTotal = params.get("DnsTotal")
        self.Domain = params.get("Domain")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Subdomain = params.get("Subdomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param Nick: 用户昵称
        :type Nick: str
        :param Id: 用户ID
        :type Id: int
        :param Email: 用户账号, 邮箱格式
        :type Email: str
        :param Status: 账号状态：”enabled”: 正常；”disabled”: 被封禁
        :type Status: str
        :param Telephone: 电话号码
        :type Telephone: str
        :param EmailVerified: 邮箱是否通过验证：”yes”: 通过；”no”: 未通过
        :type EmailVerified: str
        :param TelephoneVerified: 手机是否通过验证：”yes”: 通过；”no”: 未通过
        :type TelephoneVerified: str
        :param UserGrade: 账号等级, 按照用户账号下域名等级排序, 选取一个最高等级为账号等级, 具体对应情况参见域名等级。
        :type UserGrade: str
        :param RealName: 用户名称, 企业用户对应为公司名称
        :type RealName: str
        :param WechatBinded: 是否绑定微信：”yes”: 通过；”no”: 未通过
        :type WechatBinded: str
        :param Uin: 用户UIN
        :type Uin: int
        :param FreeNs: 所属 DNS 服务器
        :type FreeNs: list of str
        """
        self.Nick = None
        self.Id = None
        self.Email = None
        self.Status = None
        self.Telephone = None
        self.EmailVerified = None
        self.TelephoneVerified = None
        self.UserGrade = None
        self.RealName = None
        self.WechatBinded = None
        self.Uin = None
        self.FreeNs = None


    def _deserialize(self, params):
        self.Nick = params.get("Nick")
        self.Id = params.get("Id")
        self.Email = params.get("Email")
        self.Status = params.get("Status")
        self.Telephone = params.get("Telephone")
        self.EmailVerified = params.get("EmailVerified")
        self.TelephoneVerified = params.get("TelephoneVerified")
        self.UserGrade = params.get("UserGrade")
        self.RealName = params.get("RealName")
        self.WechatBinded = params.get("WechatBinded")
        self.Uin = params.get("Uin")
        self.FreeNs = params.get("FreeNs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VASStatisticItem(AbstractModel):
    """域名增值服务用量

    """

    def __init__(self):
        r"""
        :param Name: 增值服务名称
        :type Name: str
        :param Key: 增值服务标识
        :type Key: str
        :param LimitCount: 增值服务最大用量
        :type LimitCount: int
        :param UseCount: 增值服务已使用的用量
        :type UseCount: int
        """
        self.Name = None
        self.Key = None
        self.LimitCount = None
        self.UseCount = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Key = params.get("Key")
        self.LimitCount = params.get("LimitCount")
        self.UseCount = params.get("UseCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhoisContact(AbstractModel):
    """Whois联系信息

    """

    def __init__(self):
        r"""
        :param Admin: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Admin: :class:`tencentcloud.dnspod.v20210323.models.WhoisContactAddress`
        :param Billing: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Billing: :class:`tencentcloud.dnspod.v20210323.models.WhoisContactAddress`
        :param Registrant: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Registrant: :class:`tencentcloud.dnspod.v20210323.models.WhoisContactAddress`
        :param Tech: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Tech: :class:`tencentcloud.dnspod.v20210323.models.WhoisContactAddress`
        """
        self.Admin = None
        self.Billing = None
        self.Registrant = None
        self.Tech = None


    def _deserialize(self, params):
        if params.get("Admin") is not None:
            self.Admin = WhoisContactAddress()
            self.Admin._deserialize(params.get("Admin"))
        if params.get("Billing") is not None:
            self.Billing = WhoisContactAddress()
            self.Billing._deserialize(params.get("Billing"))
        if params.get("Registrant") is not None:
            self.Registrant = WhoisContactAddress()
            self.Registrant._deserialize(params.get("Registrant"))
        if params.get("Tech") is not None:
            self.Tech = WhoisContactAddress()
            self.Tech._deserialize(params.get("Tech"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhoisContactAddress(AbstractModel):
    """Whois联系信息地址

    """

    def __init__(self):
        r"""
        :param City: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param Country: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Country: str
        :param Email: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param Fax: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Fax: str
        :param FaxExt: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type FaxExt: str
        :param Handle: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Handle: str
        :param Name: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Organization: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Organization: str
        :param Phone: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param PostalCode: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type PostalCode: str
        :param State: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param Street: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Street: str
        """
        self.City = None
        self.Country = None
        self.Email = None
        self.Fax = None
        self.FaxExt = None
        self.Handle = None
        self.Name = None
        self.Organization = None
        self.Phone = None
        self.PostalCode = None
        self.State = None
        self.Street = None


    def _deserialize(self, params):
        self.City = params.get("City")
        self.Country = params.get("Country")
        self.Email = params.get("Email")
        self.Fax = params.get("Fax")
        self.FaxExt = params.get("FaxExt")
        self.Handle = params.get("Handle")
        self.Name = params.get("Name")
        self.Organization = params.get("Organization")
        self.Phone = params.get("Phone")
        self.PostalCode = params.get("PostalCode")
        self.State = params.get("State")
        self.Street = params.get("Street")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhoisInfo(AbstractModel):
    """Whois信息

    """

    def __init__(self):
        r"""
        :param Contacts: 联系信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Contacts: :class:`tencentcloud.dnspod.v20210323.models.WhoisContact`
        :param CreationDate: 域名注册时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationDate: str
        :param ExpirationDate: 域名到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpirationDate: str
        :param IsQcloud: 是否是在腾讯云注册的域名
注意：此字段可能返回 null，表示取不到有效值。
        :type IsQcloud: bool
        :param IsQcloudOwner: 是否当前操作帐号注册的域名
注意：此字段可能返回 null，表示取不到有效值。
        :type IsQcloudOwner: bool
        :param NameServers: 域名配置的NS
注意：此字段可能返回 null，表示取不到有效值。
        :type NameServers: list of str
        :param Raw: Whois原始信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Raw: list of str
        :param Registrar: 域名注册商
注意：此字段可能返回 null，表示取不到有效值。
        :type Registrar: list of str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: list of str
        :param UpdatedDate: 更新日期
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedDate: str
        """
        self.Contacts = None
        self.CreationDate = None
        self.ExpirationDate = None
        self.IsQcloud = None
        self.IsQcloudOwner = None
        self.NameServers = None
        self.Raw = None
        self.Registrar = None
        self.Status = None
        self.UpdatedDate = None


    def _deserialize(self, params):
        if params.get("Contacts") is not None:
            self.Contacts = WhoisContact()
            self.Contacts._deserialize(params.get("Contacts"))
        self.CreationDate = params.get("CreationDate")
        self.ExpirationDate = params.get("ExpirationDate")
        self.IsQcloud = params.get("IsQcloud")
        self.IsQcloudOwner = params.get("IsQcloudOwner")
        self.NameServers = params.get("NameServers")
        self.Raw = params.get("Raw")
        self.Registrar = params.get("Registrar")
        self.Status = params.get("Status")
        self.UpdatedDate = params.get("UpdatedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        