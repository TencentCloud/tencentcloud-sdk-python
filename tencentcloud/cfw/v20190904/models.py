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


class AcListsData(AbstractModel):
    """访问控制列表对象

    """

    def __init__(self):
        """
        :param Id: 规则id
        :type Id: int
        :param SourceIp: 访问源
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceIp: str
        :param TargetIp: 访问目的
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetIp: str
        :param Protocol: 协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: str
        :param Strategy: 策略
注意：此字段可能返回 null，表示取不到有效值。
        :type Strategy: int
        :param Detail: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: str
        :param Count: 命中次数
        :type Count: int
        :param OrderIndex: 执行顺序
        :type OrderIndex: int
        :param LogId: 告警规则id
注意：此字段可能返回 null，表示取不到有效值。
        :type LogId: str
        """
        self.Id = None
        self.SourceIp = None
        self.TargetIp = None
        self.Protocol = None
        self.Port = None
        self.Strategy = None
        self.Detail = None
        self.Count = None
        self.OrderIndex = None
        self.LogId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.SourceIp = params.get("SourceIp")
        self.TargetIp = params.get("TargetIp")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.Strategy = params.get("Strategy")
        self.Detail = params.get("Detail")
        self.Count = params.get("Count")
        self.OrderIndex = params.get("OrderIndex")
        self.LogId = params.get("LogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociatedInstanceInfo(AbstractModel):
    """企业安全组关联实例信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param Type: 实例类型，3是cvm实例,4是clb实例,5是eni实例,6是云数据库
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param VpcId: 私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param VpcName: 私有网络名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param PublicIp: 公网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param Ip: 内网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param SecurityGroupCount: 关联安全组数量
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupCount: int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Type = None
        self.VpcId = None
        self.VpcName = None
        self.PublicIp = None
        self.Ip = None
        self.SecurityGroupCount = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Type = params.get("Type")
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.PublicIp = params.get("PublicIp")
        self.Ip = params.get("Ip")
        self.SecurityGroupCount = params.get("SecurityGroupCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CfwNatDnatRule(AbstractModel):
    """NAT防火墙Dnat规则

    """

    def __init__(self):
        """
        :param IpProtocol: 网络协议，可选值：TCP、UDP。
        :type IpProtocol: str
        :param PublicIpAddress: 弹性IP。
        :type PublicIpAddress: str
        :param PublicPort: 公网端口。
        :type PublicPort: int
        :param PrivateIpAddress: 内网地址。
        :type PrivateIpAddress: str
        :param PrivatePort: 内网端口。
        :type PrivatePort: int
        :param Description: NAT防火墙转发规则描述。
        :type Description: str
        """
        self.IpProtocol = None
        self.PublicIpAddress = None
        self.PublicPort = None
        self.PrivateIpAddress = None
        self.PrivatePort = None
        self.Description = None


    def _deserialize(self, params):
        self.IpProtocol = params.get("IpProtocol")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.PublicPort = params.get("PublicPort")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.PrivatePort = params.get("PrivatePort")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAcRulesRequest(AbstractModel):
    """CreateAcRules请求参数结构体

    """

    def __init__(self):
        """
        :param Data: 创建规则数据
        :type Data: list of RuleInfoData
        :param Type: 0：添加（默认），1：插入
        :type Type: int
        :param EdgeId: 边id
        :type EdgeId: str
        :param Enable: 访问控制规则状态
        :type Enable: int
        :param Overwrite: 0：添加，1：覆盖
        :type Overwrite: int
        :param InstanceId: NAT实例ID, 参数Area存在的时候这个必传
        :type InstanceId: str
        :param From: portScan: 来自于端口扫描, patchImport: 来自于批量导入
        :type From: str
        :param Area: NAT地域
        :type Area: str
        """
        self.Data = None
        self.Type = None
        self.EdgeId = None
        self.Enable = None
        self.Overwrite = None
        self.InstanceId = None
        self.From = None
        self.Area = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RuleInfoData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Type = params.get("Type")
        self.EdgeId = params.get("EdgeId")
        self.Enable = params.get("Enable")
        self.Overwrite = params.get("Overwrite")
        self.InstanceId = params.get("InstanceId")
        self.From = params.get("From")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAcRulesResponse(AbstractModel):
    """CreateAcRules返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 状态值，0:操作成功
        :type Status: int
        :param Info: 返回多余的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.RequestId = params.get("RequestId")


class CreateSecurityGroupApiRulesRequest(AbstractModel):
    """CreateSecurityGroupApiRules请求参数结构体

    """

    def __init__(self):
        """
        :param Data: 创建规则数据
        :type Data: list of SecurityGroupApiRuleData
        :param Direction: 方向，0：出站，1：入站
        :type Direction: int
        :param Type: 插入类型，0：后插，1：前插，2：中插
        :type Type: int
        :param Area: 腾讯云地域的英文简写
        :type Area: str
        """
        self.Data = None
        self.Direction = None
        self.Type = None
        self.Area = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecurityGroupApiRuleData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Direction = params.get("Direction")
        self.Type = params.get("Type")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupApiRulesResponse(AbstractModel):
    """CreateSecurityGroupApiRules返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 状态值，0:添加成功，非0：添加失败
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DeleteAcRuleRequest(AbstractModel):
    """DeleteAcRule请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 删除规则对应的id值, 对应获取规则列表接口的Id 值
        :type Id: int
        :param Direction: 方向，0：出站，1：入站
        :type Direction: int
        :param EdgeId: EdgeId值两个vpc间的边id
        :type EdgeId: str
        :param Area: NAT地域， 如ap-shanghai/ap-guangzhou/ap-chongqing等
        :type Area: str
        """
        self.Id = None
        self.Direction = None
        self.EdgeId = None
        self.Area = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Direction = params.get("Direction")
        self.EdgeId = params.get("EdgeId")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAcRuleResponse(AbstractModel):
    """DeleteAcRule返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 状态值 0: 删除成功, !0: 删除失败
        :type Status: int
        :param Info: 返回多余的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.RequestId = params.get("RequestId")


class DeleteAllAccessControlRuleRequest(AbstractModel):
    """DeleteAllAccessControlRule请求参数结构体

    """

    def __init__(self):
        """
        :param Direction: 方向，0：出站，1：入站  默认值是 0
        :type Direction: int
        :param EdgeId: VPC间防火墙开关ID  全部删除 EdgeId和Area只填写一个，不填写则不删除vpc间防火墙开关 ，默认值为‘’
        :type EdgeId: str
        :param Area: nat地域 全部删除 EdgeId和Area只填写一个，不填写则不删除nat防火墙开关 默认值为‘’
        :type Area: str
        """
        self.Direction = None
        self.EdgeId = None
        self.Area = None


    def _deserialize(self, params):
        self.Direction = params.get("Direction")
        self.EdgeId = params.get("EdgeId")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAllAccessControlRuleResponse(AbstractModel):
    """DeleteAllAccessControlRule返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 状态值 0: 修改成功, !0: 修改失败
        :type Status: int
        :param Info: 删除了几条访问控制规则
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.RequestId = params.get("RequestId")


class DeleteSecurityGroupAllRuleRequest(AbstractModel):
    """DeleteSecurityGroupAllRule请求参数结构体

    """

    def __init__(self):
        """
        :param Direction: 方向，0：出站，1：入站
        :type Direction: int
        :param Area: 腾讯云地域的英文简写
        :type Area: str
        """
        self.Direction = None
        self.Area = None


    def _deserialize(self, params):
        self.Direction = params.get("Direction")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityGroupAllRuleResponse(AbstractModel):
    """DeleteSecurityGroupAllRule返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 0: 操作成功，非0：操作失败
        :type Status: int
        :param Info: 返回数据的json字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.RequestId = params.get("RequestId")


class DeleteSecurityGroupRuleRequest(AbstractModel):
    """DeleteSecurityGroupRule请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 所需要删除规则的ID
        :type Id: int
        :param Area: 腾讯云地域的英文简写
        :type Area: str
        :param Direction: 方向，0：出站，1：入站
        :type Direction: int
        :param IsDelReverse: 是否删除反向规则，0：否，1：是
        :type IsDelReverse: int
        """
        self.Id = None
        self.Area = None
        self.Direction = None
        self.IsDelReverse = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Area = params.get("Area")
        self.Direction = params.get("Direction")
        self.IsDelReverse = params.get("IsDelReverse")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityGroupRuleResponse(AbstractModel):
    """DeleteSecurityGroupRule返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 状态值，0：成功，非0：失败
        :type Status: int
        :param Info: 返回多余的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.RequestId = params.get("RequestId")


class DescribeAcListsRequest(AbstractModel):
    """DescribeAcLists请求参数结构体

    """

    def __init__(self):
        """
        :param Protocol: 协议
        :type Protocol: str
        :param Strategy: 策略
        :type Strategy: str
        :param SearchValue: 搜索值
        :type SearchValue: str
        :param Limit: 每页条数
        :type Limit: int
        :param Offset: 偏移值
        :type Offset: int
        :param Direction: 出站还是入站，0：入站，1：出站
        :type Direction: int
        :param EdgeId: EdgeId值
        :type EdgeId: str
        :param Status: 规则是否开启，'0': 未开启，'1': 开启, 默认为'0'
        :type Status: str
        :param Area: 地域
        :type Area: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        """
        self.Protocol = None
        self.Strategy = None
        self.SearchValue = None
        self.Limit = None
        self.Offset = None
        self.Direction = None
        self.EdgeId = None
        self.Status = None
        self.Area = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Strategy = params.get("Strategy")
        self.SearchValue = params.get("SearchValue")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Direction = params.get("Direction")
        self.EdgeId = params.get("EdgeId")
        self.Status = params.get("Status")
        self.Area = params.get("Area")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAcListsResponse(AbstractModel):
    """DescribeAcLists返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 总条数
        :type Total: int
        :param Data: 访问控制列表数据
        :type Data: list of AcListsData
        :param AllTotal: 不算筛选条数的总条数
        :type AllTotal: int
        :param Enable: 访问控制规则全部启用/全部停用
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Data = None
        self.AllTotal = None
        self.Enable = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = AcListsData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.AllTotal = params.get("AllTotal")
        self.Enable = params.get("Enable")
        self.RequestId = params.get("RequestId")


class DescribeAssociatedInstanceListRequest(AbstractModel):
    """DescribeAssociatedInstanceList请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 列表偏移量
        :type Offset: int
        :param Limit: 每页记录条数
        :type Limit: int
        :param Area: 地域代码（例：ap-guangzhou）,支持腾讯云全地域
        :type Area: str
        :param SearchValue: 额外检索条件（JSON字符串）
        :type SearchValue: str
        :param By: 排序字段
        :type By: str
        :param Order: 排序方式（asc:升序,desc:降序）
        :type Order: str
        :param SecurityGroupId: 安全组ID
        :type SecurityGroupId: str
        :param Type: 实例类型,'3'是cvm实例,'4'是clb实例,'5'是eni实例,'6'是云数据库
        :type Type: str
        """
        self.Offset = None
        self.Limit = None
        self.Area = None
        self.SearchValue = None
        self.By = None
        self.Order = None
        self.SecurityGroupId = None
        self.Type = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Area = params.get("Area")
        self.SearchValue = params.get("SearchValue")
        self.By = params.get("By")
        self.Order = params.get("Order")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssociatedInstanceListResponse(AbstractModel):
    """DescribeAssociatedInstanceList返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Data: 实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of AssociatedInstanceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = AssociatedInstanceInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBlockByIpTimesListRequest(AbstractModel):
    """DescribeBlockByIpTimesList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Ip: ip查询条件
        :type Ip: str
        :param Zone: 地域
        :type Zone: str
        :param Direction: 方向
        :type Direction: str
        :param Source: 来源
        :type Source: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Ip = None
        self.Zone = None
        self.Direction = None
        self.Source = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Ip = params.get("Ip")
        self.Zone = params.get("Zone")
        self.Direction = params.get("Direction")
        self.Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlockByIpTimesListResponse(AbstractModel):
    """DescribeBlockByIpTimesList返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 返回数据
        :type Data: list of IpStatic
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = IpStatic()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBlockStaticListRequest(AbstractModel):
    """DescribeBlockStaticList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param QueryType: 类型
        :type QueryType: str
        :param Top: top数
        :type Top: int
        :param SearchValue: 查询条件
        :type SearchValue: str
        """
        self.StartTime = None
        self.EndTime = None
        self.QueryType = None
        self.Top = None
        self.SearchValue = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.QueryType = params.get("QueryType")
        self.Top = params.get("Top")
        self.SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlockStaticListResponse(AbstractModel):
    """DescribeBlockStaticList返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 无
        :type Data: list of StaticInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = StaticInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCfwEipsRequest(AbstractModel):
    """DescribeCfwEips请求参数结构体

    """

    def __init__(self):
        """
        :param Mode: 0：cfw新增模式，1：cfw接入模式
        :type Mode: int
        :param NatGatewayId: ALL：查询所有弹性公网ip; nat-xxxxx：接入模式场景指定网关的弹性公网ip
        :type NatGatewayId: str
        :param CfwInstance: 防火墙实例id
        :type CfwInstance: str
        """
        self.Mode = None
        self.NatGatewayId = None
        self.CfwInstance = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.NatGatewayId = params.get("NatGatewayId")
        self.CfwInstance = params.get("CfwInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCfwEipsResponse(AbstractModel):
    """DescribeCfwEips返回参数结构体

    """

    def __init__(self):
        """
        :param NatFwEipList: 返回值信息
        :type NatFwEipList: list of NatFwEipsInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NatFwEipList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NatFwEipList") is not None:
            self.NatFwEipList = []
            for item in params.get("NatFwEipList"):
                obj = NatFwEipsInfo()
                obj._deserialize(item)
                self.NatFwEipList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGuideScanInfoRequest(AbstractModel):
    """DescribeGuideScanInfo请求参数结构体

    """


class DescribeGuideScanInfoResponse(AbstractModel):
    """DescribeGuideScanInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 扫描信息
        :type Data: :class:`tencentcloud.cfw.v20190904.models.ScanInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ScanInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeNatRuleOverviewRequest(AbstractModel):
    """DescribeNatRuleOverview请求参数结构体

    """

    def __init__(self):
        """
        :param Direction: 方向，0：出站，1：入站 默认值：0
        :type Direction: int
        :param Area: NAT地域  这个是必填项，填入相关的英文，'ap-beijing-fsi': '北京金融',
        'ap-beijing': '北京',
        'ap-changsha-ec': '长沙EC',
        'ap-chengdu': '成都',
        'ap-chongqing': '重庆',
        'ap-fuzhou-ec': '福州EC',
        'ap-guangzhou-open': '广州Open',
        'ap-guangzhou': '广州',
        'ap-hangzhou-ec': '杭州EC',
        'ap-jinan-ec': '济南EC',
        'ap-nanjing': '南京',
        'ap-shanghai-fsi': '上海金融',
        'ap-shanghai': '上海',
        'ap-shenzhen-fsi': '深圳金融',
        'ap-shenzhen': '深圳',
        'ap-wuhan-ec': '武汉EC'
        :type Area: str
        """
        self.Direction = None
        self.Area = None


    def _deserialize(self, params):
        self.Direction = params.get("Direction")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNatRuleOverviewResponse(AbstractModel):
    """DescribeNatRuleOverview返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param EipList: 弹性IP列表
        :type EipList: list of str
        :param DnatNum: 端口转发规则数量
        :type DnatNum: int
        :param TotalNum: 访问控制规则总数
        :type TotalNum: int
        :param RemainNum: 访问控制规则剩余配额
        :type RemainNum: int
        :param BlockNum: 阻断规则条数
        :type BlockNum: int
        :param EnableNum: 启用规则条数
        :type EnableNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.EipList = None
        self.DnatNum = None
        self.TotalNum = None
        self.RemainNum = None
        self.BlockNum = None
        self.EnableNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.EipList = params.get("EipList")
        self.DnatNum = params.get("DnatNum")
        self.TotalNum = params.get("TotalNum")
        self.RemainNum = params.get("RemainNum")
        self.BlockNum = params.get("BlockNum")
        self.EnableNum = params.get("EnableNum")
        self.RequestId = params.get("RequestId")


class DescribeRuleOverviewRequest(AbstractModel):
    """DescribeRuleOverview请求参数结构体

    """

    def __init__(self):
        """
        :param Direction: 方向，0：出站，1：入站
        :type Direction: int
        """
        self.Direction = None


    def _deserialize(self, params):
        self.Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleOverviewResponse(AbstractModel):
    """DescribeRuleOverview返回参数结构体

    """

    def __init__(self):
        """
        :param AllTotal: 规则总数
注意：此字段可能返回 null，表示取不到有效值。
        :type AllTotal: int
        :param StrategyNum: 阻断策略规则数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyNum: int
        :param StartRuleNum: 启用规则数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRuleNum: int
        :param StopRuleNum: 停用规则数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StopRuleNum: int
        :param RemainingNum: 剩余配额
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainingNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AllTotal = None
        self.StrategyNum = None
        self.StartRuleNum = None
        self.StopRuleNum = None
        self.RemainingNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllTotal = params.get("AllTotal")
        self.StrategyNum = params.get("StrategyNum")
        self.StartRuleNum = params.get("StartRuleNum")
        self.StopRuleNum = params.get("StopRuleNum")
        self.RemainingNum = params.get("RemainingNum")
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupListRequest(AbstractModel):
    """DescribeSecurityGroupList请求参数结构体

    """

    def __init__(self):
        """
        :param Direction: 0: 出站规则，1：入站规则
        :type Direction: int
        :param Area: 地域代码（例: ap-guangzhou),支持腾讯云全部地域
        :type Area: str
        :param SearchValue: 搜索值
        :type SearchValue: str
        :param Limit: 每页条数，默认为10
        :type Limit: int
        :param Offset: 偏移值，默认为0
        :type Offset: int
        :param Status: 状态，'': 全部，'0'：筛选停用规则，'1'：筛选启用规则
        :type Status: str
        :param Filter: 0: 不过滤，1：过滤掉正常规则，保留下发异常规则
        :type Filter: int
        """
        self.Direction = None
        self.Area = None
        self.SearchValue = None
        self.Limit = None
        self.Offset = None
        self.Status = None
        self.Filter = None


    def _deserialize(self, params):
        self.Direction = params.get("Direction")
        self.Area = params.get("Area")
        self.SearchValue = params.get("SearchValue")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Status = params.get("Status")
        self.Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupListResponse(AbstractModel):
    """DescribeSecurityGroupList返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 列表当前规则总条数
        :type Total: int
        :param Data: 安全组规则列表数据
        :type Data: list of SecurityGroupListData
        :param AllTotal: 不算筛选条数的总条数
        :type AllTotal: int
        :param Enable: 访问控制规则全部启用/全部停用
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Data = None
        self.AllTotal = None
        self.Enable = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecurityGroupListData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.AllTotal = params.get("AllTotal")
        self.Enable = params.get("Enable")
        self.RequestId = params.get("RequestId")


class DescribeSwitchListsRequest(AbstractModel):
    """DescribeSwitchLists请求参数结构体

    """

    def __init__(self):
        """
        :param Status: 防火墙状态  0: 关闭，1：开启
        :type Status: int
        :param Type: 资产类型 CVM/NAT/VPN/CLB/其它
        :type Type: str
        :param Area: 地域 上海/重庆/广州，等等
        :type Area: str
        :param SearchValue: 搜索值  例子："{"common":"106.54.189.45"}"
        :type SearchValue: str
        :param Limit: 条数  默认值:10
        :type Limit: int
        :param Offset: 偏移值 默认值: 0
        :type Offset: int
        :param Order: 排序，desc：降序，asc：升序
        :type Order: str
        :param By: 排序字段 PortTimes(风险端口数)
        :type By: str
        """
        self.Status = None
        self.Type = None
        self.Area = None
        self.SearchValue = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Area = params.get("Area")
        self.SearchValue = params.get("SearchValue")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSwitchListsResponse(AbstractModel):
    """DescribeSwitchLists返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 总条数
        :type Total: int
        :param Data: 列表数据
        :type Data: list of SwitchListsData
        :param AreaLists: 区域列表
        :type AreaLists: list of str
        :param OnNum: 打开个数
注意：此字段可能返回 null，表示取不到有效值。
        :type OnNum: int
        :param OffNum: 关闭个数
注意：此字段可能返回 null，表示取不到有效值。
        :type OffNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Data = None
        self.AreaLists = None
        self.OnNum = None
        self.OffNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SwitchListsData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.AreaLists = params.get("AreaLists")
        self.OnNum = params.get("OnNum")
        self.OffNum = params.get("OffNum")
        self.RequestId = params.get("RequestId")


class DescribeSyncAssetStatusRequest(AbstractModel):
    """DescribeSyncAssetStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Type: 0: 互联网防火墙开关，1：vpc 防火墙开关
        :type Type: int
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSyncAssetStatusResponse(AbstractModel):
    """DescribeSyncAssetStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 1-更新中 2-更新完成 3、4-更新失败
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeTLogInfoRequest(AbstractModel):
    """DescribeTLogInfo请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param QueryType: 类型 1 告警 2阻断
        :type QueryType: str
        :param SearchValue: 查询条件
        :type SearchValue: str
        """
        self.StartTime = None
        self.EndTime = None
        self.QueryType = None
        self.SearchValue = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.QueryType = params.get("QueryType")
        self.SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTLogInfoResponse(AbstractModel):
    """DescribeTLogInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 无
        :type Data: :class:`tencentcloud.cfw.v20190904.models.TLogInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TLogInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeTLogIpListRequest(AbstractModel):
    """DescribeTLogIpList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param QueryType: 类型 1 告警 2阻断
        :type QueryType: str
        :param Top: top数
        :type Top: int
        :param SearchValue: 查询条件
        :type SearchValue: str
        """
        self.StartTime = None
        self.EndTime = None
        self.QueryType = None
        self.Top = None
        self.SearchValue = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.QueryType = params.get("QueryType")
        self.Top = params.get("Top")
        self.SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTLogIpListResponse(AbstractModel):
    """DescribeTLogIpList返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 数据集合
        :type Data: list of StaticInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = StaticInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTableStatusRequest(AbstractModel):
    """DescribeTableStatus请求参数结构体

    """

    def __init__(self):
        """
        :param EdgeId: EdgeId值两个vpc间的边id vpc填Edgeid，不要填Area；
        :type EdgeId: str
        :param Status: 状态值，0：检查表的状态 确实只有一个默认值
        :type Status: int
        :param Area: Nat所在地域 NAT填Area，不要填Edgeid；
        :type Area: str
        :param Direction: 方向，0：出站，1：入站 默认值为 0
        :type Direction: int
        """
        self.EdgeId = None
        self.Status = None
        self.Area = None
        self.Direction = None


    def _deserialize(self, params):
        self.EdgeId = params.get("EdgeId")
        self.Status = params.get("Status")
        self.Area = params.get("Area")
        self.Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableStatusResponse(AbstractModel):
    """DescribeTableStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 0：正常，其它：不正常
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeUnHandleEventTabListRequest(AbstractModel):
    """DescribeUnHandleEventTabList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param AssetID: 查询示例ID
        :type AssetID: str
        """
        self.StartTime = None
        self.EndTime = None
        self.AssetID = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.AssetID = params.get("AssetID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnHandleEventTabListResponse(AbstractModel):
    """DescribeUnHandleEventTabList返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 租户伪攻击链未处置事件
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cfw.v20190904.models.UnHandleEvent`
        :param ReturnCode: 错误码，0成功 非0错误
        :type ReturnCode: int
        :param ReturnMsg: 返回信息 success成功
        :type ReturnMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.ReturnCode = None
        self.ReturnMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = UnHandleEvent()
            self.Data._deserialize(params.get("Data"))
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMsg = params.get("ReturnMsg")
        self.RequestId = params.get("RequestId")


class DescribeVpcRuleOverviewRequest(AbstractModel):
    """DescribeVpcRuleOverview请求参数结构体

    """

    def __init__(self):
        """
        :param EdgeId: EdgeId值两个vpc间的边id  不是必填项可以为空，就是所有vpc间的访问控制规则
        :type EdgeId: str
        """
        self.EdgeId = None


    def _deserialize(self, params):
        self.EdgeId = params.get("EdgeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcRuleOverviewResponse(AbstractModel):
    """DescribeVpcRuleOverview返回参数结构体

    """

    def __init__(self):
        """
        :param StrategyNum: 阻断策略规则数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyNum: int
        :param StartRuleNum: 启用规则数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRuleNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StrategyNum = None
        self.StartRuleNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StrategyNum = params.get("StrategyNum")
        self.StartRuleNum = params.get("StartRuleNum")
        self.RequestId = params.get("RequestId")


class ExpandCfwVerticalRequest(AbstractModel):
    """ExpandCfwVertical请求参数结构体

    """

    def __init__(self):
        """
        :param FwType: nat：nat防火墙，ew：东西向防火墙
        :type FwType: str
        :param Width: 带宽值
        :type Width: int
        :param CfwInstance: 防火墙实例id
        :type CfwInstance: str
        """
        self.FwType = None
        self.Width = None
        self.CfwInstance = None


    def _deserialize(self, params):
        self.FwType = params.get("FwType")
        self.Width = params.get("Width")
        self.CfwInstance = params.get("CfwInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpandCfwVerticalResponse(AbstractModel):
    """ExpandCfwVertical返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class IocListData(AbstractModel):
    """黑白名单IOC列表

    """

    def __init__(self):
        """
        :param IP: 待处置IP地址，IP/Domain字段二选一
        :type IP: str
        :param Direction: 只能为0或者1   0代表出站 1代表入站
        :type Direction: int
        :param Domain: 待处置域名，IP/Domain字段二选一
        :type Domain: str
        """
        self.IP = None
        self.Direction = None
        self.Domain = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Direction = params.get("Direction")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpStatic(AbstractModel):
    """统计折线图通用结构体

    """

    def __init__(self):
        """
        :param Num: 值
        :type Num: int
        :param StatTime: 折线图横坐标时间
        :type StatTime: str
        """
        self.Num = None
        self.StatTime = None


    def _deserialize(self, params):
        self.Num = params.get("Num")
        self.StatTime = params.get("StatTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAcRuleRequest(AbstractModel):
    """ModifyAcRule请求参数结构体

    """

    def __init__(self):
        """
        :param Data: 规则数组
        :type Data: list of RuleInfoData
        :param EdgeId: EdgeId值
        :type EdgeId: str
        :param Enable: 访问规则状态
        :type Enable: int
        :param Area: NAT地域
        :type Area: str
        """
        self.Data = None
        self.EdgeId = None
        self.Enable = None
        self.Area = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RuleInfoData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.EdgeId = params.get("EdgeId")
        self.Enable = params.get("Enable")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAcRuleResponse(AbstractModel):
    """ModifyAcRule返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 状态值，0:操作成功，非0：操作失败
        :type Status: int
        :param Info: 返回多余的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.RequestId = params.get("RequestId")


class ModifyAllRuleStatusRequest(AbstractModel):
    """ModifyAllRuleStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Status: 状态，0：全部停用，1：全部启用
        :type Status: int
        :param Direction: 方向，0：出站，1：入站
        :type Direction: int
        :param EdgeId: Edge ID值
        :type EdgeId: str
        :param Area: NAT地域
        :type Area: str
        """
        self.Status = None
        self.Direction = None
        self.EdgeId = None
        self.Area = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Direction = params.get("Direction")
        self.EdgeId = params.get("EdgeId")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAllRuleStatusResponse(AbstractModel):
    """ModifyAllRuleStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 0: 修改成功, 其他: 修改失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifyAllSwitchStatusRequest(AbstractModel):
    """ModifyAllSwitchStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Status: 状态，0：关闭，1：开启
        :type Status: int
        :param Type: 0: 互联网边界防火墙开关，1：vpc防火墙开关
        :type Type: int
        :param Ids: 选中的防火墙开关Id
        :type Ids: list of str
        :param ChangeType: NAT开关切换类型，1,单个子网，2，同开同关，3，全部
        :type ChangeType: int
        :param Area: NAT实例所在地域
        :type Area: str
        """
        self.Status = None
        self.Type = None
        self.Ids = None
        self.ChangeType = None
        self.Area = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Ids = params.get("Ids")
        self.ChangeType = params.get("ChangeType")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAllSwitchStatusResponse(AbstractModel):
    """ModifyAllSwitchStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 修改成功与否的状态值 0：修改成功，非 0：修改失败
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifyBlockIgnoreListRequest(AbstractModel):
    """ModifyBlockIgnoreList请求参数结构体

    """

    def __init__(self):
        """
        :param RuleType: 1拦截列表 2 忽略列表
        :type RuleType: int
        :param IOC: IP、Domain二选一，不能同时为空
        :type IOC: list of IocListData
        :param IocAction: 可选值：delete（删除）、edit（编辑）、add（添加）  其他值无效
        :type IocAction: str
        :param StartTime: 时间格式：yyyy-MM-dd HH:mm:ss
        :type StartTime: str
        :param EndTime: 时间格式：yyyy-MM-dd HH:mm:ss
        :type EndTime: str
        """
        self.RuleType = None
        self.IOC = None
        self.IocAction = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        if params.get("IOC") is not None:
            self.IOC = []
            for item in params.get("IOC"):
                obj = IocListData()
                obj._deserialize(item)
                self.IOC.append(obj)
        self.IocAction = params.get("IocAction")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBlockIgnoreListResponse(AbstractModel):
    """ModifyBlockIgnoreList返回参数结构体

    """

    def __init__(self):
        """
        :param ReturnMsg: 接口返回信息
        :type ReturnMsg: str
        :param ReturnCode: 接口返回错误码，0请求成功  非0失败
        :type ReturnCode: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReturnMsg = None
        self.ReturnCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnMsg = params.get("ReturnMsg")
        self.ReturnCode = params.get("ReturnCode")
        self.RequestId = params.get("RequestId")


class ModifyBlockTopRequest(AbstractModel):
    """ModifyBlockTop请求参数结构体

    """

    def __init__(self):
        """
        :param UniqueId: 记录id
        :type UniqueId: str
        :param OpeType: 操作类型 1 置顶 0取消
        :type OpeType: str
        """
        self.UniqueId = None
        self.OpeType = None


    def _deserialize(self, params):
        self.UniqueId = params.get("UniqueId")
        self.OpeType = params.get("OpeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBlockTopResponse(AbstractModel):
    """ModifyBlockTop返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyItemSwitchStatusRequest(AbstractModel):
    """ModifyItemSwitchStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Id: id值
        :type Id: int
        :param Status: 状态值，0: 关闭 ,1:开启
        :type Status: int
        :param Type: 0: 互联网边界边界防火墙开关，1：vpc防火墙开关
        :type Type: int
        """
        self.Id = None
        self.Status = None
        self.Type = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyItemSwitchStatusResponse(AbstractModel):
    """ModifyItemSwitchStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 修改成功与否状态值 0：修改成功，非 0：修改失败
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifySecurityGroupAllRuleStatusRequest(AbstractModel):
    """ModifySecurityGroupAllRuleStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Status: 列表规则状态，0：全部停用，1：全部启用
        :type Status: int
        :param Direction: 方向，0：出站，1：入站
        :type Direction: int
        :param EdgeId: Edge ID值
        :type EdgeId: str
        :param Area: NAT地域, 腾讯云地域的英文简写
        :type Area: str
        """
        self.Status = None
        self.Direction = None
        self.EdgeId = None
        self.Area = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Direction = params.get("Direction")
        self.EdgeId = params.get("EdgeId")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupAllRuleStatusResponse(AbstractModel):
    """ModifySecurityGroupAllRuleStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 0: 修改成功, 其他: 修改失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifySequenceRulesRequest(AbstractModel):
    """ModifySequenceRules请求参数结构体

    """

    def __init__(self):
        """
        :param EdgeId: 边Id值
        :type EdgeId: str
        :param Data: 修改数据
        :type Data: list of SequenceData
        :param Area: NAT地域
        :type Area: str
        :param Direction: 方向，0：出向，1：入向
        :type Direction: int
        """
        self.EdgeId = None
        self.Data = None
        self.Area = None
        self.Direction = None


    def _deserialize(self, params):
        self.EdgeId = params.get("EdgeId")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SequenceData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Area = params.get("Area")
        self.Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySequenceRulesResponse(AbstractModel):
    """ModifySequenceRules返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 0: 修改成功, 非0: 修改失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifyTableStatusRequest(AbstractModel):
    """ModifyTableStatus请求参数结构体

    """

    def __init__(self):
        """
        :param EdgeId: EdgeId值两个vpc间的边id
        :type EdgeId: str
        :param Status: 状态值，1：锁表，2：解锁表
        :type Status: int
        :param Area: Nat所在地域
        :type Area: str
        :param Direction: 0： 出向，1：入向
        :type Direction: int
        """
        self.EdgeId = None
        self.Status = None
        self.Area = None
        self.Direction = None


    def _deserialize(self, params):
        self.EdgeId = params.get("EdgeId")
        self.Status = params.get("Status")
        self.Area = params.get("Area")
        self.Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableStatusResponse(AbstractModel):
    """ModifyTableStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 0：正常，-1：不正常
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class NatFwEipsInfo(AbstractModel):
    """Nat防火墙弹性公网ip列表

    """

    def __init__(self):
        """
        :param Eip: 弹性公网ip
        :type Eip: str
        :param NatGatewayId: 所属的Nat网关Id
注意：此字段可能返回 null，表示取不到有效值。
        :type NatGatewayId: str
        :param NatGatewayName: Nat网关名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NatGatewayName: str
        """
        self.Eip = None
        self.NatGatewayId = None
        self.NatGatewayName = None


    def _deserialize(self, params):
        self.Eip = params.get("Eip")
        self.NatGatewayId = params.get("NatGatewayId")
        self.NatGatewayName = params.get("NatGatewayName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInfoData(AbstractModel):
    """规则输入对象

    """

    def __init__(self):
        """
        :param OrderIndex: 执行顺序
        :type OrderIndex: int
        :param SourceIp: 访问源
        :type SourceIp: str
        :param TargetIp: 访问目的
        :type TargetIp: str
        :param Protocol: 协议
        :type Protocol: str
        :param Strategy: 策略
        :type Strategy: str
        :param SourceType: 访问源类型，1是IP，3是域名，4是IP地址模版，5是域名地址模版
        :type SourceType: int
        :param Direction: 方向，0：出站，1：入站
        :type Direction: int
        :param Detail: 描述
        :type Detail: str
        :param TargetType: 访问目的类型，1是IP，3是域名，4是IP地址模版，5是域名地址模版
        :type TargetType: int
        :param Port: 端口
        :type Port: str
        :param Id: id值
        :type Id: int
        :param LogId: 日志id，从告警处创建必传，其它为空
        :type LogId: str
        :param City: 城市Code
        :type City: int
        :param Country: 国家Code
        :type Country: int
        :param CloudCode: 云厂商，支持多个，以逗号分隔， 1:腾讯云（仅中国香港及海外）,2:阿里云,3:亚马逊云,4:华为云,5:微软云
        :type CloudCode: str
        :param IsRegion: 是否为地域
        :type IsRegion: int
        :param CityName: 城市名
        :type CityName: str
        :param CountryName: 国家名
        :type CountryName: str
        """
        self.OrderIndex = None
        self.SourceIp = None
        self.TargetIp = None
        self.Protocol = None
        self.Strategy = None
        self.SourceType = None
        self.Direction = None
        self.Detail = None
        self.TargetType = None
        self.Port = None
        self.Id = None
        self.LogId = None
        self.City = None
        self.Country = None
        self.CloudCode = None
        self.IsRegion = None
        self.CityName = None
        self.CountryName = None


    def _deserialize(self, params):
        self.OrderIndex = params.get("OrderIndex")
        self.SourceIp = params.get("SourceIp")
        self.TargetIp = params.get("TargetIp")
        self.Protocol = params.get("Protocol")
        self.Strategy = params.get("Strategy")
        self.SourceType = params.get("SourceType")
        self.Direction = params.get("Direction")
        self.Detail = params.get("Detail")
        self.TargetType = params.get("TargetType")
        self.Port = params.get("Port")
        self.Id = params.get("Id")
        self.LogId = params.get("LogId")
        self.City = params.get("City")
        self.Country = params.get("Country")
        self.CloudCode = params.get("CloudCode")
        self.IsRegion = params.get("IsRegion")
        self.CityName = params.get("CityName")
        self.CountryName = params.get("CountryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSyncAssetRequest(AbstractModel):
    """RunSyncAsset请求参数结构体

    """

    def __init__(self):
        """
        :param Type: 0: 互联网防火墙开关，1：vpc 防火墙开关
        :type Type: int
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSyncAssetResponse(AbstractModel):
    """RunSyncAsset返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 0：同步成功，1：资产更新中，2：后台同步调用失败
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ScanInfo(AbstractModel):
    """新手引导扫描信息

    """

    def __init__(self):
        """
        :param ScanResultInfo: 扫描结果信息
        :type ScanResultInfo: :class:`tencentcloud.cfw.v20190904.models.ScanResultInfo`
        :param ScanStatus: 扫描状态 0扫描中 1完成   2没赠送过扫描显示开启界面
        :type ScanStatus: int
        :param ScanPercent: 进度
        :type ScanPercent: float
        :param ScanTime: 预计完成时间
        :type ScanTime: str
        """
        self.ScanResultInfo = None
        self.ScanStatus = None
        self.ScanPercent = None
        self.ScanTime = None


    def _deserialize(self, params):
        if params.get("ScanResultInfo") is not None:
            self.ScanResultInfo = ScanResultInfo()
            self.ScanResultInfo._deserialize(params.get("ScanResultInfo"))
        self.ScanStatus = params.get("ScanStatus")
        self.ScanPercent = params.get("ScanPercent")
        self.ScanTime = params.get("ScanTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanResultInfo(AbstractModel):
    """新手引导扫描结果信息PortNum   int
    	LeakNum   int
    	IPNum     int
    	IPStatus  bool
    	IdpStatus bool
    	BanStatus bool

    """

    def __init__(self):
        """
        :param LeakNum: 暴漏漏洞数量
        :type LeakNum: int
        :param IPNum: 防护ip数量
        :type IPNum: int
        :param PortNum: 暴漏端口数量
        :type PortNum: int
        :param IPStatus: 是否开启防护
        :type IPStatus: bool
        :param IdpStatus: 是否拦截攻击
        :type IdpStatus: bool
        :param BanStatus: 是否禁封端口
        :type BanStatus: bool
        """
        self.LeakNum = None
        self.IPNum = None
        self.PortNum = None
        self.IPStatus = None
        self.IdpStatus = None
        self.BanStatus = None


    def _deserialize(self, params):
        self.LeakNum = params.get("LeakNum")
        self.IPNum = params.get("IPNum")
        self.PortNum = params.get("PortNum")
        self.IPStatus = params.get("IPStatus")
        self.IdpStatus = params.get("IdpStatus")
        self.BanStatus = params.get("BanStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupApiRuleData(AbstractModel):
    """添加安全组Api规则对象

    """

    def __init__(self):
        """
        :param SourceId: 访问源，入站时为Ip/Cidr，默认为0.0.0.0/0； 出站时当RuleType为1时，支持内网Ip/Cidr, 当RuleType为2时，填实例ID
        :type SourceId: str
        :param TargetId: 访问目的，出站时为Ip/Cidr，默认为0.0.0.0/0；入站时当RuleType为1时，支持内网Ip/Cidr, 当RuleType为2时，填实例ID
        :type TargetId: str
        :param Protocol: 协议，支持ANY/TCP/UDP/ICMP
        :type Protocol: str
        :param Port: 端口, 当Protocol为ANY或ICMP时，Port为-1/-1
        :type Port: str
        :param Strategy: 策略, 1：阻断，2：放行
        :type Strategy: str
        :param Detail: 描述
        :type Detail: str
        :param RuleType: 规则类型，1：VpcId+Ip/Cidr, 2: 实例ID，入站时为访问目的类型，出站时为访问源类型
        :type RuleType: int
        :param OrderIndex: 执行顺序，中间插入必传，前插、后插非必传
        :type OrderIndex: int
        :param VpcId: 私有网络ID，当RuleType为1时必传
        :type VpcId: str
        """
        self.SourceId = None
        self.TargetId = None
        self.Protocol = None
        self.Port = None
        self.Strategy = None
        self.Detail = None
        self.RuleType = None
        self.OrderIndex = None
        self.VpcId = None


    def _deserialize(self, params):
        self.SourceId = params.get("SourceId")
        self.TargetId = params.get("TargetId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.Strategy = params.get("Strategy")
        self.Detail = params.get("Detail")
        self.RuleType = params.get("RuleType")
        self.OrderIndex = params.get("OrderIndex")
        self.VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupListData(AbstractModel):
    """安全组列表数据

    """

    def __init__(self):
        """
        :param Id: 规则ID
        :type Id: int
        :param OrderIndex: 执行顺序
        :type OrderIndex: int
        :param SourceId: 访问源
        :type SourceId: str
        :param SourceType: 访问源类型，默认为0，1: VPC, 2: SUBNET, 3: CVM, 4: CLB, 5: ENI, 6: CDB
        :type SourceType: int
        :param TargetId: 访问目的
        :type TargetId: str
        :param TargetType: 访问目的类型，默认为0，1: VPC, 2: SUBNET, 3: CVM, 4: CLB, 5: ENI, 6: CDB
        :type TargetType: int
        :param Protocol: 协议
        :type Protocol: str
        :param Port: 目的端口
        :type Port: str
        :param Strategy: 策略, 1：阻断，2：放行
        :type Strategy: int
        :param Detail: 描述
        :type Detail: str
        :param Status: 是否开关开启，0：未开启，1：开启
        :type Status: int
        :param IsNew: 是否是正常规则，0：正常，1：异常
        :type IsNew: int
        :param BothWay: 单/双向下发，0:单向下发，1：双向下发
        :type BothWay: int
        :param VpcId: 私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param PublicIp: 公网IP，多个以英文逗号分隔
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param PrivateIp: 内网IP，多个以英文逗号分隔
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param Cidr: 掩码地址，多个以英文逗号分隔
注意：此字段可能返回 null，表示取不到有效值。
        :type Cidr: str
        """
        self.Id = None
        self.OrderIndex = None
        self.SourceId = None
        self.SourceType = None
        self.TargetId = None
        self.TargetType = None
        self.Protocol = None
        self.Port = None
        self.Strategy = None
        self.Detail = None
        self.Status = None
        self.IsNew = None
        self.BothWay = None
        self.VpcId = None
        self.SubnetId = None
        self.InstanceName = None
        self.PublicIp = None
        self.PrivateIp = None
        self.Cidr = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.OrderIndex = params.get("OrderIndex")
        self.SourceId = params.get("SourceId")
        self.SourceType = params.get("SourceType")
        self.TargetId = params.get("TargetId")
        self.TargetType = params.get("TargetType")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.Strategy = params.get("Strategy")
        self.Detail = params.get("Detail")
        self.Status = params.get("Status")
        self.IsNew = params.get("IsNew")
        self.BothWay = params.get("BothWay")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.InstanceName = params.get("InstanceName")
        self.PublicIp = params.get("PublicIp")
        self.PrivateIp = params.get("PrivateIp")
        self.Cidr = params.get("Cidr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SequenceData(AbstractModel):
    """执行顺序对象

    """

    def __init__(self):
        """
        :param Id: 规则Id值
        :type Id: int
        :param OrderIndex: 修改前执行顺序
        :type OrderIndex: int
        :param NewOrderIndex: 修改后执行顺序
        :type NewOrderIndex: int
        """
        self.Id = None
        self.OrderIndex = None
        self.NewOrderIndex = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.OrderIndex = params.get("OrderIndex")
        self.NewOrderIndex = params.get("NewOrderIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNatFwDnatRuleRequest(AbstractModel):
    """SetNatFwDnatRule请求参数结构体

    """

    def __init__(self):
        """
        :param Mode: 0：cfw新增模式，1：cfw接入模式。
        :type Mode: int
        :param OperationType: 操作类型，可选值：add，del，modify。
        :type OperationType: str
        :param CfwInstance: 防火墙实例id。
        :type CfwInstance: str
        :param AddOrDelDnatRules: 添加或删除操作的Dnat规则列表。
        :type AddOrDelDnatRules: list of CfwNatDnatRule
        :param OriginDnat: 修改操作的原始Dnat规则
        :type OriginDnat: :class:`tencentcloud.cfw.v20190904.models.CfwNatDnatRule`
        :param NewDnat: 修改操作的新的Dnat规则
        :type NewDnat: :class:`tencentcloud.cfw.v20190904.models.CfwNatDnatRule`
        """
        self.Mode = None
        self.OperationType = None
        self.CfwInstance = None
        self.AddOrDelDnatRules = None
        self.OriginDnat = None
        self.NewDnat = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.OperationType = params.get("OperationType")
        self.CfwInstance = params.get("CfwInstance")
        if params.get("AddOrDelDnatRules") is not None:
            self.AddOrDelDnatRules = []
            for item in params.get("AddOrDelDnatRules"):
                obj = CfwNatDnatRule()
                obj._deserialize(item)
                self.AddOrDelDnatRules.append(obj)
        if params.get("OriginDnat") is not None:
            self.OriginDnat = CfwNatDnatRule()
            self.OriginDnat._deserialize(params.get("OriginDnat"))
        if params.get("NewDnat") is not None:
            self.NewDnat = CfwNatDnatRule()
            self.NewDnat._deserialize(params.get("NewDnat"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNatFwDnatRuleResponse(AbstractModel):
    """SetNatFwDnatRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StaticInfo(AbstractModel):
    """StaticInfo 告警柱形图统计信息


    """

    def __init__(self):
        """
        :param Num: 数
        :type Num: int
        :param Port: 端口
        :type Port: str
        :param Ip: ip信息
        :type Ip: str
        :param Address: 地址
        :type Address: str
        :param InsID: 资产id
        :type InsID: str
        :param InsName: 资产名称
        :type InsName: str
        """
        self.Num = None
        self.Port = None
        self.Ip = None
        self.Address = None
        self.InsID = None
        self.InsName = None


    def _deserialize(self, params):
        self.Num = params.get("Num")
        self.Port = params.get("Port")
        self.Ip = params.get("Ip")
        self.Address = params.get("Address")
        self.InsID = params.get("InsID")
        self.InsName = params.get("InsName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchListsData(AbstractModel):
    """防火墙开关列表对象

    """

    def __init__(self):
        """
        :param PublicIp: 公网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIp: str
        :param IntranetIp: 内网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type IntranetIp: str
        :param InstanceName: 实例名
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param AssetType: 资产类型
        :type AssetType: str
        :param Area: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        :param Switch: 防火墙开关
        :type Switch: int
        :param Id: id值
        :type Id: int
        :param PublicIpType: 公网 IP 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpType: int
        :param PortTimes: 风险端口数
注意：此字段可能返回 null，表示取不到有效值。
        :type PortTimes: int
        :param LastTime: 最近扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTime: str
        :param ScanMode: 扫描深度
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanMode: str
        :param ScanStatus: 扫描状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanStatus: int
        """
        self.PublicIp = None
        self.IntranetIp = None
        self.InstanceName = None
        self.InstanceId = None
        self.AssetType = None
        self.Area = None
        self.Switch = None
        self.Id = None
        self.PublicIpType = None
        self.PortTimes = None
        self.LastTime = None
        self.ScanMode = None
        self.ScanStatus = None


    def _deserialize(self, params):
        self.PublicIp = params.get("PublicIp")
        self.IntranetIp = params.get("IntranetIp")
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.AssetType = params.get("AssetType")
        self.Area = params.get("Area")
        self.Switch = params.get("Switch")
        self.Id = params.get("Id")
        self.PublicIpType = params.get("PublicIpType")
        self.PortTimes = params.get("PortTimes")
        self.LastTime = params.get("LastTime")
        self.ScanMode = params.get("ScanMode")
        self.ScanStatus = params.get("ScanStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TLogInfo(AbstractModel):
    """告警中心概览数据

    """

    def __init__(self):
        """
        :param OutNum: 失陷主机
        :type OutNum: int
        :param HandleNum: 待处置告警
        :type HandleNum: int
        :param VulNum: 漏洞攻击
        :type VulNum: int
        :param NetworkNum: 网络探测
        :type NetworkNum: int
        :param BanNum: 封禁列表
        :type BanNum: int
        :param BruteForceNum: 暴力破解
        :type BruteForceNum: int
        """
        self.OutNum = None
        self.HandleNum = None
        self.VulNum = None
        self.NetworkNum = None
        self.BanNum = None
        self.BruteForceNum = None


    def _deserialize(self, params):
        self.OutNum = params.get("OutNum")
        self.HandleNum = params.get("HandleNum")
        self.VulNum = params.get("VulNum")
        self.NetworkNum = params.get("NetworkNum")
        self.BanNum = params.get("BanNum")
        self.BruteForceNum = params.get("BruteForceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnHandleEvent(AbstractModel):
    """未处置事件详情

    """

    def __init__(self):
        """
        :param EventTableListStruct: 伪攻击链类型
        :type EventTableListStruct: list of UnHandleEventDetail
        :param BaseLineUser: 1 是  0否
        :type BaseLineUser: int
        :param BaseLineInSwitch: 1 打开 0 关闭
        :type BaseLineInSwitch: int
        :param BaseLineOutSwitch: 1 打开 0 关闭
        :type BaseLineOutSwitch: int
        """
        self.EventTableListStruct = None
        self.BaseLineUser = None
        self.BaseLineInSwitch = None
        self.BaseLineOutSwitch = None


    def _deserialize(self, params):
        if params.get("EventTableListStruct") is not None:
            self.EventTableListStruct = []
            for item in params.get("EventTableListStruct"):
                obj = UnHandleEventDetail()
                obj._deserialize(item)
                self.EventTableListStruct.append(obj)
        self.BaseLineUser = params.get("BaseLineUser")
        self.BaseLineInSwitch = params.get("BaseLineInSwitch")
        self.BaseLineOutSwitch = params.get("BaseLineOutSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnHandleEventDetail(AbstractModel):
    """未处置事件信息汇总

    """

    def __init__(self):
        """
        :param EventName: 安全事件名称
        :type EventName: str
        :param Total: 未处置事件数量
        :type Total: int
        """
        self.EventName = None
        self.Total = None


    def _deserialize(self, params):
        self.EventName = params.get("EventName")
        self.Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        