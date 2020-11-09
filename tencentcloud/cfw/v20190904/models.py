# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


class CreateAcRulesRequest(AbstractModel):
    """CreateAcRules请求参数结构体

    """

    def __init__(self):
        """
        :param Data: 创建规则数据
        :type Data: list of RuleInfoData
        :param Type: 0：添加，1：插入
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


class DeleteAcRuleRequest(AbstractModel):
    """DeleteAcRule请求参数结构体

    """

    def __init__(self):
        """
        :param Id: id值
        :type Id: int
        :param Direction: 出站还是入站
        :type Direction: int
        :param EdgeId: EdgeId值
        :type EdgeId: str
        :param Area: NAT地域
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


class DeleteAcRuleResponse(AbstractModel):
    """DeleteAcRule返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 状态值
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
        :param Direction: 方向，0：出站，1：入站
        :type Direction: int
        :param EdgeId: VPC间防火墙开关ID
        :type EdgeId: str
        :param Area: nat地域
        :type Area: str
        """
        self.Direction = None
        self.EdgeId = None
        self.Area = None


    def _deserialize(self, params):
        self.Direction = params.get("Direction")
        self.EdgeId = params.get("EdgeId")
        self.Area = params.get("Area")


class DeleteAllAccessControlRuleResponse(AbstractModel):
    """DeleteAllAccessControlRule返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 状态值
        :type Status: int
        :param Info: 返回多余信息
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


class DescribeNatRuleOverviewRequest(AbstractModel):
    """DescribeNatRuleOverview请求参数结构体

    """

    def __init__(self):
        """
        :param Direction: 方向，0：出站，1：入站
        :type Direction: int
        :param Area: NAT地域
        :type Area: str
        """
        self.Direction = None
        self.Area = None


    def _deserialize(self, params):
        self.Direction = params.get("Direction")
        self.Area = params.get("Area")


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
        :param RemainNum: 访问规则剩余条数
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


class DescribeSwitchListsRequest(AbstractModel):
    """DescribeSwitchLists请求参数结构体

    """

    def __init__(self):
        """
        :param Status: 防火墙状态
        :type Status: int
        :param Type: 资产类型
        :type Type: str
        :param Area: 地域
        :type Area: str
        :param SearchValue: 搜索值
        :type SearchValue: str
        :param Limit: 条数
        :type Limit: int
        :param Offset: 偏移值
        :type Offset: int
        :param Order: 排序，desc：降序，asc：升序
        :type Order: str
        :param By: 排序字段
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


class DescribeSyncAssetStatusResponse(AbstractModel):
    """DescribeSyncAssetStatus返回参数结构体

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


class DescribeTableStatusRequest(AbstractModel):
    """DescribeTableStatus请求参数结构体

    """

    def __init__(self):
        """
        :param EdgeId: EdgeId值
        :type EdgeId: str
        :param Status: 状态值，0：检查表的状态
        :type Status: int
        :param Area: Nat所在地域
        :type Area: str
        :param Direction: 方向，0：出站，1：入站
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


class DescribeVpcRuleOverviewRequest(AbstractModel):
    """DescribeVpcRuleOverview请求参数结构体

    """

    def __init__(self):
        """
        :param EdgeId: 边id
        :type EdgeId: str
        """
        self.EdgeId = None


    def _deserialize(self, params):
        self.EdgeId = params.get("EdgeId")


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


class ModifyAcRuleResponse(AbstractModel):
    """ModifyAcRule返回参数结构体

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
        :param Type: 0: 边界防火墙开关，1：vpc防火墙开关
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


class ModifyAllSwitchStatusResponse(AbstractModel):
    """ModifyAllSwitchStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 开启或者关闭成功与否状态值
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
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
        :param Type: 0: 边界防火墙开关，1：vpc防火墙开关
        :type Type: int
        """
        self.Id = None
        self.Status = None
        self.Type = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        self.Type = params.get("Type")


class ModifyItemSwitchStatusResponse(AbstractModel):
    """ModifyItemSwitchStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 修改成功与否状态值
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
        :param Direction: 0：出向，1：入向
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


class ModifySequenceRulesResponse(AbstractModel):
    """ModifySequenceRules返回参数结构体

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


class ModifyTableStatusRequest(AbstractModel):
    """ModifyTableStatus请求参数结构体

    """

    def __init__(self):
        """
        :param EdgeId: EdgeId值
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
        :param Detail: 描述
        :type Detail: str
        :param Direction: 方向，0：出站，1：入站
        :type Direction: int
        :param SourceType: 源类型,1是ip,2是域名,3是ip地址簿，4是ip组地址簿
        :type SourceType: int
        :param TargetType: 目的类型,1是ip,2是域名,3是ip地址簿，4是ip组地址簿
        :type TargetType: int
        :param Port: 端口
        :type Port: str
        :param Id: id值
        :type Id: int
        :param LogId: log
        :type LogId: str
        :param City: 城市Code
        :type City: int
        :param Country: 国家Code
        :type Country: int
        :param CloudCode: 云厂商，支持多个，以逗号分隔， 1:腾讯云（仅海外）,2:阿里云,3:亚马逊云,4:华为云,5:微软云
        :type CloudCode: str
        :param IsRegion: 是否为地域
        :type IsRegion: int
        :param CityName: 地域名
        :type CityName: str
        :param CountryName: 地域名
        :type CountryName: str
        """
        self.OrderIndex = None
        self.SourceIp = None
        self.TargetIp = None
        self.Protocol = None
        self.Strategy = None
        self.Detail = None
        self.Direction = None
        self.SourceType = None
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
        self.Detail = params.get("Detail")
        self.Direction = params.get("Direction")
        self.SourceType = params.get("SourceType")
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