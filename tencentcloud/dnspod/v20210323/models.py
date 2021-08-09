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
        """
        :param RecordType: 记录类型, 详见 DescribeRecordType 接口。\n        :type RecordType: str\n        :param Value: 记录值。\n        :type Value: str\n        :param SubDomain: 子域名(主机记录)。\n        :type SubDomain: str\n        :param RecordLine: 解析记录的线路，详见 DescribeRecordLineList 接口。\n        :type RecordLine: str\n        :param RecordLineId: 解析记录的线路 ID，RecordLine和RecordLineId都有时，系统优先取 RecordLineId\n        :type RecordLineId: str\n        :param Weight: 记录权重值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Weight: int\n        :param MX: 记录的 MX 记录值，非 MX 记录类型，默认为 0，MX记录则必选\n        :type MX: int\n        :param TTL: 记录的 TTL 值，默认600\n        :type TTL: int\n        :param Enabled: 记录状态。0表示禁用，1表示启用，默认启用\n        :type Enabled: int\n        :param Remark: 记录别名\n        :type Remark: str\n        """
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
        """
        :param RecordId: 记录 ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordId: int\n        :param SubDomain: 子域名(主机记录)。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubDomain: str\n        :param RecordType: 记录类型, 详见 DescribeRecordType 接口
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordType: str\n        :param RecordLine: 解析记录的线路，详见 DescribeRecordLineList 接口
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordLine: str\n        :param Value: 记录值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        :param TTL: 记录的 TTL 值
注意：此字段可能返回 null，表示取不到有效值。\n        :type TTL: int\n        :param Status: 记录添加状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Operation: str\n        :param ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrMsg: str\n        :param Id: 此条记录在列表中的ID\n        :type Id: int\n        :param Enabled: 记录生效状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Enabled: int\n        :param MX: 记录的MX权重
注意：此字段可能返回 null，表示取不到有效值。\n        :type MX: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainAliasRequest(AbstractModel):
    """CreateDomainAlias请求参数结构体

    """

    def __init__(self):
        """
        :param DomainAlias: 域名别名\n        :type DomainAlias: str\n        :param Domain: 域名\n        :type Domain: str\n        :param DomainId: 域名ID，参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain\n        :type DomainId: int\n        """
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
        """
        :param DomainAliasId: 域名别名ID\n        :type DomainAliasId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DomainAliasId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DomainAliasId = params.get("DomainAliasId")
        self.RequestId = params.get("RequestId")


class CreateDomainBatchDetail(AbstractModel):
    """批量添加域名返回结构

    """

    def __init__(self):
        """
        :param RecordList: 见RecordInfoBatch
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordList: list of CreateDomainBatchRecord\n        :param Id: 任务编号\n        :type Id: int\n        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。\n        :type Domain: str\n        :param DomainGrade: 域名等级
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainGrade: str\n        :param ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrMsg: str\n        :param Status: 该条任务运行状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Operation: str\n        """
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
        """
        :param SubDomain: 子域名(主机记录)。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubDomain: str\n        :param RecordType: 记录类型, 详见 DescribeRecordType 接口
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordType: str\n        :param RecordLine: 解析记录的线路，详见 DescribeRecordLineList 接口
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordLine: str\n        :param Value: 记录值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        :param TTL: 记录的 TTL 值
注意：此字段可能返回 null，表示取不到有效值。\n        :type TTL: int\n        :param Status: 记录添加状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Operation: str\n        :param ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrMsg: str\n        :param Id: 此条记录在列表中的ID\n        :type Id: int\n        """
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
        """
        :param DomainList: 域名数组\n        :type DomainList: list of str\n        :param RecordValue: 每个域名添加 @ 和 www 的 A 记录值，记录值为IP，如果不传此参数或者传空，将只添加域名，不添加记录。\n        :type RecordValue: str\n        """
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
        """
        :param DetailList: 批量添加域名信息\n        :type DetailList: list of CreateDomainBatchDetail\n        :param JobId: 批量任务的ID\n        :type JobId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param GroupName: 域名分组\n        :type GroupName: str\n        """
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
        """
        :param GroupId: 域名分组ID\n        :type GroupId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreateDomainRequest(AbstractModel):
    """CreateDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param GroupId: 域名分组ID\n        :type GroupId: int\n        :param IsMark: 是否星标域名，”yes”、”no” 分别代表是和否。\n        :type IsMark: str\n        """
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
        """
        :param DomainInfo: 域名信息\n        :type DomainInfo: :class:`tencentcloud.dnspod.v20210323.models.DomainCreateInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RecordList: 见RecordInfoBatch
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordList: list of CreateRecordBatchRecord\n        :param Id: 任务编号\n        :type Id: int\n        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。\n        :type Domain: str\n        :param DomainGrade: 域名等级
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainGrade: str\n        :param ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrMsg: str\n        :param Status: 该条任务运行状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Operation: str\n        :param DomainId: 域名ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainId: int\n        """
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
        """
        :param SubDomain: 子域名(主机记录)。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubDomain: str\n        :param RecordType: 记录类型, 详见 DescribeRecordType 接口
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordType: str\n        :param RecordLine: 解析记录的线路，详见 DescribeRecordLineList 接口
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordLine: str\n        :param Value: 记录值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        :param TTL: 记录的 TTL 值
注意：此字段可能返回 null，表示取不到有效值。\n        :type TTL: int\n        :param Status: 记录添加状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Operation: str\n        :param ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrMsg: str\n        :param Id: 此条记录在列表中的ID\n        :type Id: int\n        :param MX: 记录的MX权重
注意：此字段可能返回 null，表示取不到有效值。\n        :type MX: int\n        """
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
        """
        :param DomainIdList: 域名ID，多个 domain_id 用英文逗号进行分割。\n        :type DomainIdList: list of str\n        :param RecordList: 记录数组\n        :type RecordList: list of AddRecordBatch\n        """
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
        """
        :param DetailList: 批量添加域名信息\n        :type DetailList: list of CreateRecordBatchDetail\n        :param JobId: 批量任务的ID\n        :type JobId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class CreateRecordRequest(AbstractModel):
    """CreateRecord请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param RecordType: 记录类型，通过 API 记录类型获得，大写英文，比如：A 。\n        :type RecordType: str\n        :param RecordLine: 记录线路，通过 API 记录线路获得，中文，比如：默认。\n        :type RecordLine: str\n        :param Value: 记录值，如 IP : 200.200.200.200， CNAME : cname.dnspod.com.， MX : mail.dnspod.com.。\n        :type Value: str\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        :param SubDomain: 主机记录，如 www，如果不传，默认为 @。\n        :type SubDomain: str\n        :param RecordLineId: 线路的 ID，通过 API 记录线路获得，英文字符串，比如：10=1。参数RecordLineId优先级高于RecordLine，如果同时传递二者，优先使用RecordLineId参数。\n        :type RecordLineId: str\n        :param MX: MX 优先级，当记录类型是 MX 时有效，范围1-20，MX 记录时必选。\n        :type MX: int\n        :param TTL: TTL，范围1-604800，不同等级域名最小值不同。\n        :type TTL: int\n        :param Weight: 权重信息，0到100的整数。仅企业 VIP 域名可用，0 表示关闭，不传该参数，表示不设置权重信息。\n        :type Weight: int\n        :param Status: 记录初始状态，取值范围为 ENABLE 和 DISABLE 。默认为 ENABLE ，如果传入 DISABLE，解析不会生效，也不会验证负载均衡的限制。\n        :type Status: str\n        """
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
        """
        :param RecordId: 记录ID\n        :type RecordId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.RequestId = params.get("RequestId")


class DeleteDomainAliasRequest(AbstractModel):
    """DeleteDomainAlias请求参数结构体

    """

    def __init__(self):
        """
        :param DomainAliasId: 域名别名ID\n        :type DomainAliasId: int\n        :param Domain: 域名\n        :type Domain: str\n        :param DomainId: 域名ID，参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain\n        :type DomainId: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDomainRequest(AbstractModel):
    """DeleteDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRecordRequest(AbstractModel):
    """DeleteRecord请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param RecordId: 记录 ID 。\n        :type RecordId: int\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteShareDomainRequest(AbstractModel):
    """DeleteShareDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param Account: 域名共享的账号\n        :type Account: str\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeBatchTaskDetail(AbstractModel):
    """查看任务详情返回结构

    """

    def __init__(self):
        """
        :param RecordList: 见BatchRecordInfo
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordList: list of BatchRecordInfo\n        :param Id: 任务编号\n        :type Id: int\n        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。\n        :type Domain: str\n        :param DomainGrade: 域名等级
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainGrade: str\n        :param ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrMsg: str\n        :param Status: 该条任务运行状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Operation: str\n        :param DomainId: 域名ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainId: int\n        """
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
        """
        :param JobId: 任务ID\n        :type JobId: int\n        """
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
        """
        :param DetailList: 批量任务详情\n        :type DetailList: list of DescribeBatchTaskDetail\n        :param TotalCount: 总任务条数\n        :type TotalCount: int\n        :param SuccessCount: 成功条数\n        :type SuccessCount: int\n        :param FailCount: 失败条数\n        :type FailCount: int\n        :param JobType: 批量任务类型\n        :type JobType: str\n        :param CreatedAt: 任务创建时间\n        :type CreatedAt: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeDomainListRequest(AbstractModel):
    """DescribeDomainList请求参数结构体

    """

    def __init__(self):
        """
        :param Type: 域名分组类型，默认为ALL。可取值为ALL，MINE，SHARE，ISMARK，PAUSE，VIP，RECENT，SHARE_OUT。\n        :type Type: str\n        :param Offset: 记录开始的偏移, 第一条记录为 0, 依次类推。默认值为0。\n        :type Offset: int\n        :param Limit: 要获取的域名数量, 比如获取20个, 则为20。默认值为3000。\n        :type Limit: int\n        :param GroupId: 分组ID, 获取指定分组的域名\n        :type GroupId: int\n        :param Keyword: 根据关键字搜索域名\n        :type Keyword: str\n        """
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
        """
        :param DomainCountInfo: 列表页统计信息\n        :type DomainCountInfo: :class:`tencentcloud.dnspod.v20210323.models.DomainCountInfo`\n        :param DomainList: 域名列表\n        :type DomainList: list of DomainListItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Domain: 域名\n        :type Domain: str\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        :param Offset: 记录开始的偏移，第一条记录为 0，依次类推，默认为0\n        :type Offset: int\n        :param Limit: 共要获取的日志条数，比如获取20条，则为20，默认为500条，单次最多获取500条。\n        :type Limit: int\n        """
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
        """
        :param LogList: 域名信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type LogList: list of str\n        :param PageSize: 分页大小\n        :type PageSize: int\n        :param TotalCount: 日志总条数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LogList = None
        self.PageSize = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogList = params.get("LogList")
        self.PageSize = params.get("PageSize")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDomainPurviewRequest(AbstractModel):
    """DescribeDomainPurview请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        """
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
        """
        :param PurviewList: 域名权限列表\n        :type PurviewList: list of PurviewInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Domain: 域名\n        :type Domain: str\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        """
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
        """
        :param DomainInfo: 域名信息\n        :type DomainInfo: :class:`tencentcloud.dnspod.v20210323.models.DomainInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Domain: 域名\n        :type Domain: str\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        """
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
        """
        :param ShareList: 域名共享信息\n        :type ShareList: list of DomainShareInfo\n        :param Owner: 域名拥有者账号\n        :type Owner: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeRecordLineListRequest(AbstractModel):
    """DescribeRecordLineList请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名。\n        :type Domain: str\n        :param DomainGrade: 域名等级。
+ 旧套餐：D_FREE、D_PLUS、D_EXTRA、D_EXPERT、D_ULTRA 分别对应免费套餐、个人豪华、企业1、企业2、企业3。
+ 新套餐：DP_FREE、DP_PLUS、DP_EXTRA、DP_EXPERT、DP_ULTRA 分别对应新免费、个人专业版、企业创业版、企业标准版、企业旗舰版。\n        :type DomainGrade: str\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        """
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
        """
        :param LineList: 线路列表。\n        :type LineList: list of LineInfo\n        :param LineGroupList: 线路分组列表。\n        :type LineGroupList: list of LineGroupInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Domain: 要获取的解析记录所属的域名\n        :type Domain: str\n        :param DomainId: 要获取的解析记录所属的域名Id，如果传了DomainId，系统将会忽略Domain参数\n        :type DomainId: int\n        :param Subdomain: 解析记录的主机头，如果传了此参数，则只会返回此主机头对应的解析记录\n        :type Subdomain: str\n        :param RecordType: 获取某种类型的解析记录，如 A，CNAME，NS，AAAA，显性URL，隐性URL，CAA，SPF等\n        :type RecordType: str\n        :param RecordLine: 获取某条线路名称的解析记录\n        :type RecordLine: str\n        :param RecordLineId: 获取某个线路Id对应的解析记录，如果传RecordLineId，系统会忽略RecordLine参数\n        :type RecordLineId: str\n        :param GroupId: 获取某个分组下的解析记录时，传这个分组Id\n        :type GroupId: int\n        :param Keyword: 通过关键字搜索解析记录，当前支持搜索主机头和记录值\n        :type Keyword: str\n        :param SortField: 排序字段，支持 name,line,type,value,weight,mx,ttl,updated_on 几个字段。\n        :type SortField: str\n        :param SortType: 排序方式，正序：ASC，逆序：DESC。默认值为ASC。\n        :type SortType: str\n        :param Offset: 偏移量，默认值为0。\n        :type Offset: int\n        :param Limit: 限制数量，当前Limit最大支持3000。默认值为100。\n        :type Limit: int\n        """
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
        """
        :param RecordCountInfo: 记录的数量统计信息\n        :type RecordCountInfo: :class:`tencentcloud.dnspod.v20210323.models.RecordCountInfo`\n        :param RecordList: 获取的记录列表\n        :type RecordList: list of RecordListItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Domain: 域名\n        :type Domain: str\n        :param RecordId: 记录 ID 。\n        :type RecordId: int\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        """
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
        """
        :param RecordInfo: 记录信息\n        :type RecordInfo: :class:`tencentcloud.dnspod.v20210323.models.RecordInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RecordInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RecordInfo") is not None:
            self.RecordInfo = RecordInfo()
            self.RecordInfo._deserialize(params.get("RecordInfo"))
        self.RequestId = params.get("RequestId")


class DescribeRecordTypeRequest(AbstractModel):
    """DescribeRecordType请求参数结构体

    """

    def __init__(self):
        """
        :param DomainGrade: 域名等级。
+ 旧套餐：D_FREE、D_PLUS、D_EXTRA、D_EXPERT、D_ULTRA 分别对应免费套餐、个人豪华、企业1、企业2、企业3。
+ 新套餐：DP_FREE、DP_PLUS、DP_EXTRA、DP_EXPERT、DP_ULTRA 分别对应新免费、个人专业版、企业创业版、企业标准版、企业旗舰版。\n        :type DomainGrade: str\n        """
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
        """
        :param TypeList: 记录类型列表\n        :type TypeList: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TypeList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TypeList = params.get("TypeList")
        self.RequestId = params.get("RequestId")


class DescribeUserDetailRequest(AbstractModel):
    """DescribeUserDetail请求参数结构体

    """


class DescribeUserDetailResponse(AbstractModel):
    """DescribeUserDetail返回参数结构体

    """

    def __init__(self):
        """
        :param UserInfo: 帐户信息\n        :type UserInfo: :class:`tencentcloud.dnspod.v20210323.models.UserInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.UserInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self.UserInfo = UserInfo()
            self.UserInfo._deserialize(params.get("UserInfo"))
        self.RequestId = params.get("RequestId")


class DomainCountInfo(AbstractModel):
    """列表页分页统计信息

    """

    def __init__(self):
        """
        :param DomainTotal: 符合条件的域名数量\n        :type DomainTotal: int\n        :param AllTotal: 用户可以查看的所有域名数量\n        :type AllTotal: int\n        :param MineTotal: 用户账号添加的域名数量\n        :type MineTotal: int\n        :param ShareTotal: 共享给用户的域名数量\n        :type ShareTotal: int\n        :param VipTotal: 付费域名数量\n        :type VipTotal: int\n        :param PauseTotal: 暂停的域名数量\n        :type PauseTotal: int\n        :param ErrorTotal: dns设置错误的域名数量\n        :type ErrorTotal: int\n        :param LockTotal: 锁定的域名数量\n        :type LockTotal: int\n        :param SpamTotal: 封禁的域名数量\n        :type SpamTotal: int\n        :param VipExpire: 30天内即将到期的域名数量\n        :type VipExpire: int\n        :param ShareOutTotal: 分享给其它人的域名数量\n        :type ShareOutTotal: int\n        :param GroupTotal: 指定分组内的域名数量\n        :type GroupTotal: int\n        """
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
        """
        :param Id: 域名ID\n        :type Id: int\n        :param Domain: 域名\n        :type Domain: str\n        :param Punycode: 域名的punycode\n        :type Punycode: str\n        :param GradeNsList: 域名的NS列表\n        :type GradeNsList: list of str\n        """
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
        """
        :param DomainId: 域名ID\n        :type DomainId: int\n        :param Status: 域名状态\n        :type Status: str\n        :param Grade: 域名套餐等级\n        :type Grade: str\n        :param GroupId: 域名分组ID\n        :type GroupId: int\n        :param IsMark: 是否星标域名\n        :type IsMark: str\n        :param TTL: TTL(DNS记录缓存时间)\n        :type TTL: int\n        :param CnameSpeedup: cname加速启用状态\n        :type CnameSpeedup: str\n        :param Remark: 域名备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        :param Punycode: 域名Punycode\n        :type Punycode: str\n        :param DnsStatus: 域名DNS状态\n        :type DnsStatus: str\n        :param DnspodNsList: 域名的NS列表\n        :type DnspodNsList: list of str\n        :param Domain: 域名\n        :type Domain: str\n        :param GradeLevel: 域名等级代号\n        :type GradeLevel: int\n        :param UserId: 域名所属的用户ID\n        :type UserId: int\n        :param IsVip: 是否为付费域名\n        :type IsVip: str\n        :param Owner: 域名所有者的账号\n        :type Owner: str\n        :param GradeTitle: 域名等级的描述\n        :type GradeTitle: str\n        :param CreatedOn: 域名创建时间\n        :type CreatedOn: str\n        :param UpdatedOn: 最后操作时间\n        :type UpdatedOn: str\n        :param Uin: 腾讯云账户Uin\n        :type Uin: str\n        :param ActualNsList: 域名实际使用的NS列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActualNsList: list of str\n        :param RecordCount: 域名的记录数量\n        :type RecordCount: int\n        :param OwnerNick: 域名所有者的账户昵称
注意：此字段可能返回 null，表示取不到有效值。\n        :type OwnerNick: str\n        """
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
        """
        :param DomainId: 系统分配给域名的唯一标识\n        :type DomainId: int\n        :param Name: 域名的原始格式\n        :type Name: str\n        :param Status: 域名的状态，正常：ENABLE，暂停：PAUSE，封禁：SPAM\n        :type Status: str\n        :param TTL: 域名默认的解析记录默认TTL值\n        :type TTL: int\n        :param CNAMESpeedup: 是否开启CNAME加速，开启：ENABLE，未开启：DISABLE\n        :type CNAMESpeedup: str\n        :param DNSStatus: DNS 设置状态，错误：DNSERROR，正常：空字符串\n        :type DNSStatus: str\n        :param Grade: 域名的套餐等级代码\n        :type Grade: str\n        :param GroupId: 域名所属的分组Id\n        :type GroupId: int\n        :param SearchEnginePush: 是否开启搜索引擎推送优化，是：YES，否：NO\n        :type SearchEnginePush: str\n        :param Remark: 域名备注说明\n        :type Remark: str\n        :param Punycode: 经过punycode编码后的域名格式\n        :type Punycode: str\n        :param EffectiveDNS: 系统为域名分配的有效DNS\n        :type EffectiveDNS: list of str\n        :param GradeLevel: 域名套餐等级对应的序号\n        :type GradeLevel: int\n        :param GradeTitle: 套餐名称\n        :type GradeTitle: str\n        :param IsVip: 是否是付费套餐\n        :type IsVip: str\n        :param VipStartAt: 付费套餐开通时间\n        :type VipStartAt: str\n        :param VipEndAt: 付费套餐到期时间\n        :type VipEndAt: str\n        :param VipAutoRenew: 域名是否开通VIP自动续费，是：YES，否：NO，默认：DEFAULT\n        :type VipAutoRenew: str\n        :param RecordCount: 域名下的记录数量\n        :type RecordCount: int\n        :param CreatedOn: 域名添加时间\n        :type CreatedOn: str\n        :param UpdatedOn: 域名更新时间\n        :type UpdatedOn: str\n        :param Owner: 域名所属账号\n        :type Owner: str\n        """
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
        """
        :param ShareTo: 域名共享对象的账号\n        :type ShareTo: str\n        :param Mode: 共享模式，“rw”：可读写。 “r”:：只读\n        :type Mode: str\n        :param Status: 共享状态“enabled”：共享成功。“pending”：共享到的账号不存在, 等待注册\n        :type Status: str\n        """
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
        


class LineGroupInfo(AbstractModel):
    """线路分组信息

    """

    def __init__(self):
        """
        :param LineId: 线路分组ID\n        :type LineId: str\n        :param Name: 线路分组名称\n        :type Name: str\n        :param Type: 分组类型\n        :type Type: str\n        :param LineList: 线路分组包含的线路列表\n        :type LineList: list of str\n        """
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
        """
        :param Name: 线路名称\n        :type Name: str\n        :param LineId: 线路ID\n        :type LineId: str\n        """
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
        """
        :param DomainId: 域名 ID\n        :type DomainId: int\n        :param LockCode: 域名解锁码\n        :type LockCode: str\n        :param LockEnd: 域名自动解锁日期\n        :type LockEnd: str\n        """
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
        """
        :param Domain: 域名\n        :type Domain: str\n        :param LockDays: 域名要锁定的天数，最多可锁定的天数可以通过获取域名权限接口获取。\n        :type LockDays: int\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        """
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
        """
        :param LockInfo: 域名锁定信息\n        :type LockInfo: :class:`tencentcloud.dnspod.v20210323.models.LockInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Domain: 域名\n        :type Domain: str\n        :param Account: 域名需要转入的账号，支持Uin或者邮箱格式\n        :type Account: str\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDomainRemarkRequest(AbstractModel):
    """ModifyDomainRemark请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        :param Remark: 域名备注，删除备注请提交空内容。\n        :type Remark: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDomainStatusRequest(AbstractModel):
    """ModifyDomainStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param Status: 域名状态，”enable” 、”disable” 分别代表启用和暂停\n        :type Status: str\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDomainUnlockRequest(AbstractModel):
    """ModifyDomainUnlock请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param LockCode: 域名解锁码，锁定的时候会返回。\n        :type LockCode: str\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDynamicDNSRequest(AbstractModel):
    """ModifyDynamicDNS请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param RecordId: 记录ID。\n        :type RecordId: int\n        :param RecordLine: 记录线路，通过 API 记录线路获得，中文，比如：默认。\n        :type RecordLine: str\n        :param Value: 记录值，如 IP : 200.200.200.200， CNAME : cname.dnspod.com.， MX : mail.dnspod.com.。\n        :type Value: str\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        :param SubDomain: 主机记录，如 www，如果不传，默认为 @。\n        :type SubDomain: str\n        :param RecordLineId: 线路的 ID，通过 API 记录线路获得，英文字符串，比如：10=1。参数RecordLineId优先级高于RecordLine，如果同时传递二者，优先使用RecordLineId参数。\n        :type RecordLineId: str\n        """
        self.Domain = None
        self.RecordId = None
        self.RecordLine = None
        self.Value = None
        self.DomainId = None
        self.SubDomain = None
        self.RecordLineId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RecordId = params.get("RecordId")
        self.RecordLine = params.get("RecordLine")
        self.Value = params.get("Value")
        self.DomainId = params.get("DomainId")
        self.SubDomain = params.get("SubDomain")
        self.RecordLineId = params.get("RecordLineId")
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
        """
        :param RecordId: 记录ID\n        :type RecordId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.RequestId = params.get("RequestId")


class ModifyRecordBatchDetail(AbstractModel):
    """批量添加记录返回结构

    """

    def __init__(self):
        """
        :param RecordList: 见RecordInfoBatchModify
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordList: list of BatchRecordInfo\n        :param Id: 任务编号\n        :type Id: int\n        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。\n        :type Domain: str\n        :param DomainGrade: 域名等级
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainGrade: str\n        :param ErrMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrMsg: str\n        :param Status: 该条任务运行状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param Operation: 操作类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Operation: str\n        :param DomainId: 域名ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainId: int\n        """
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
        """
        :param RecordIdList: 记录ID数组\n        :type RecordIdList: list of int non-negative\n        :param Change: 要修改的字段，可选值为 [“sub_domain”、”record_type”、”area”、”value”、”mx”、”ttl”、”status”] 中的某一个。\n        :type Change: str\n        :param ChangeTo: 修改为，具体依赖 change 字段，必填参数。\n        :type ChangeTo: str\n        :param Value: 要修改到的记录值，仅当 change 字段为 “record_type” 时为必填参数。\n        :type Value: str\n        :param MX: MX记录优先级，仅当修改为 MX 记录时为必填参数。\n        :type MX: str\n        """
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
        """
        :param JobId: 批量任务ID\n        :type JobId: int\n        :param DetailList: 见modifyRecordBatchDetail\n        :type DetailList: list of ModifyRecordBatchDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class ModifyRecordRemarkRequest(AbstractModel):
    """ModifyRecordRemark请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param RecordId: 记录 ID 。\n        :type RecordId: int\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        :param Remark: 解析记录备注，删除备注请提交空内容。\n        :type Remark: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRecordRequest(AbstractModel):
    """ModifyRecord请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param RecordType: 记录类型，通过 API 记录类型获得，大写英文，比如：A 。\n        :type RecordType: str\n        :param RecordLine: 记录线路，通过 API 记录线路获得，中文，比如：默认。\n        :type RecordLine: str\n        :param Value: 记录值，如 IP : 200.200.200.200， CNAME : cname.dnspod.com.， MX : mail.dnspod.com.。\n        :type Value: str\n        :param RecordId: 记录 ID 。\n        :type RecordId: int\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        :param SubDomain: 主机记录，如 www，如果不传，默认为 @。\n        :type SubDomain: str\n        :param RecordLineId: 线路的 ID，通过 API 记录线路获得，英文字符串，比如：10=1。参数RecordLineId优先级高于RecordLine，如果同时传递二者，优先使用RecordLineId参数。\n        :type RecordLineId: str\n        :param MX: MX 优先级，当记录类型是 MX 时有效，范围1-20，MX 记录时必选。\n        :type MX: int\n        :param TTL: TTL，范围1-604800，不同等级域名最小值不同。\n        :type TTL: int\n        :param Weight: 权重信息，0到100的整数。仅企业 VIP 域名可用，0 表示关闭，不传该参数，表示不设置权重信息。\n        :type Weight: int\n        :param Status: 记录初始状态，取值范围为 ENABLE 和 DISABLE 。默认为 ENABLE ，如果传入 DISABLE，解析不会生效，也不会验证负载均衡的限制。\n        :type Status: str\n        """
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
        """
        :param RecordId: 记录ID\n        :type RecordId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.RequestId = params.get("RequestId")


class ModifyRecordStatusRequest(AbstractModel):
    """ModifyRecordStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param RecordId: 记录 ID 。\n        :type RecordId: int\n        :param Status: 记录的状态。取值范围为 ENABLE 和 DISABLE。如果传入 DISABLE，解析不会生效，也不会验证负载均衡的限制。\n        :type Status: str\n        :param DomainId: 域名 ID 。参数 DomainId 优先级比参数 Domain 高，如果传递参数 DomainId 将忽略参数 Domain 。\n        :type DomainId: int\n        """
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
        """
        :param RecordId: 记录ID。\n        :type RecordId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.RequestId = params.get("RequestId")


class PurviewInfo(AbstractModel):
    """域名权限项

    """

    def __init__(self):
        """
        :param Name: 权限名称\n        :type Name: str\n        :param Value: 权限值\n        :type Value: str\n        """
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
        """
        :param SubdomainCount: 子域名数量\n        :type SubdomainCount: int\n        :param ListCount: 列表返回的记录数\n        :type ListCount: int\n        :param TotalCount: 总的记录数\n        :type TotalCount: int\n        """
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
        


class RecordInfo(AbstractModel):
    """记录信息

    """

    def __init__(self):
        """
        :param Id: 记录 ID 。\n        :type Id: int\n        :param SubDomain: 子域名(主机记录)。\n        :type SubDomain: str\n        :param RecordType: 记录类型, 详见 DescribeRecordType 接口。\n        :type RecordType: str\n        :param RecordLine: 解析记录的线路，详见 DescribeRecordLineList 接口。\n        :type RecordLine: str\n        :param RecordLineId: 解析记录的线路 ID ，详见 DescribeRecordLineList 接口。\n        :type RecordLineId: str\n        :param Value: 记录值。\n        :type Value: str\n        :param Weight: 记录权重值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Weight: int\n        :param MX: 记录的 MX 记录值，非 MX 记录类型，默认为 0。\n        :type MX: int\n        :param TTL: 记录的 TTL 值。\n        :type TTL: int\n        :param Enabled: 记录状态。0表示禁用，1表示启用。\n        :type Enabled: int\n        :param MonitorStatus: 该记录的 D 监控状态。
"Ok" : 服务器正常。
"Warn" : 该记录有报警, 服务器返回 4XX。
"Down" : 服务器宕机。
"" : 该记录未开启 D 监控。\n        :type MonitorStatus: str\n        :param Remark: 记录的备注。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        :param UpdatedOn: 记录最后更新时间。\n        :type UpdatedOn: str\n        :param DomainId: 域名 ID 。\n        :type DomainId: int\n        """
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
        """
        :param RecordId: 记录Id\n        :type RecordId: int\n        :param Value: 记录值\n        :type Value: str\n        :param Status: 记录状态，启用：ENABLE，暂停：DISABLE\n        :type Status: str\n        :param UpdatedOn: 更新时间\n        :type UpdatedOn: str\n        :param Name: 主机名\n        :type Name: str\n        :param Line: 记录线路\n        :type Line: str\n        :param LineId: 线路Id\n        :type LineId: str\n        :param Type: 记录类型\n        :type Type: str\n        :param Weight: 记录权重，用于负载均衡记录
注意：此字段可能返回 null，表示取不到有效值。\n        :type Weight: int\n        :param MonitorStatus: 记录监控状态，正常：OK，告警：WARN，宕机：DOWN，未设置监控或监控暂停则为空\n        :type MonitorStatus: str\n        :param Remark: 记录备注说明\n        :type Remark: str\n        :param TTL: 记录缓存时间\n        :type TTL: int\n        :param MX: MX值，只有MX记录有
注意：此字段可能返回 null，表示取不到有效值。\n        :type MX: int\n        """
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
        """
        :param Nick: 用户昵称\n        :type Nick: str\n        :param Id: 用户ID\n        :type Id: int\n        :param Email: 用户账号, 邮箱格式\n        :type Email: str\n        :param Status: 账号状态：”enabled”: 正常；”disabled”: 被封禁\n        :type Status: str\n        :param Telephone: 电话号码\n        :type Telephone: str\n        :param EmailVerified: 邮箱是否通过验证：”yes”: 通过；”no”: 未通过\n        :type EmailVerified: str\n        :param TelephoneVerified: 手机是否通过验证：”yes”: 通过；”no”: 未通过\n        :type TelephoneVerified: str\n        :param UserGrade: 账号等级, 按照用户账号下域名等级排序, 选取一个最高等级为账号等级, 具体对应情况参见域名等级。\n        :type UserGrade: str\n        :param RealName: 用户名称, 企业用户对应为公司名称\n        :type RealName: str\n        :param WechatBinded: 是否绑定微信：”yes”: 通过；”no”: 未通过\n        :type WechatBinded: str\n        :param Uin: 用户UIN\n        :type Uin: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        