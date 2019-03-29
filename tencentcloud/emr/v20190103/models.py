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


class InquiryPriceCreateInstanceRequest(AbstractModel):
    """InquiryPriceCreateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param TimeUnit: 时间单位
        :type TimeUnit: str
        :param TimeSpan: 时间长度
        :type TimeSpan: int
        :param ResourceSpec: 询价资源描述
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.ResourceSpec`
        :param Currency: 货币种类
        :type Currency: str
        :param PayMode: 计费类型
        :type PayMode: int
        :param SupportHA: 是否支持HA， 1 支持，0 不支持
        :type SupportHA: int
        :param Software: 软件列表
        :type Software: list of str
        :param Placement: 位置信息
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param VPCSettings: VPC信息
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.ResourceSpec = None
        self.Currency = None
        self.PayMode = None
        self.SupportHA = None
        self.Software = None
        self.Placement = None
        self.VPCSettings = None


    def _deserialize(self, params):
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        if params.get("ResourceSpec") is not None:
            self.ResourceSpec = ResourceSpec()
            self.ResourceSpec._deserialize(params.get("ResourceSpec"))
        self.Currency = params.get("Currency")
        self.PayMode = params.get("PayMode")
        self.SupportHA = params.get("SupportHA")
        self.Software = params.get("Software")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        if params.get("VPCSettings") is not None:
            self.VPCSettings = VPCSettings()
            self.VPCSettings._deserialize(params.get("VPCSettings"))


class InquiryPriceCreateInstanceResponse(AbstractModel):
    """InquiryPriceCreateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 询价结果
        :type Result: :class:`tencentcloud.emr.v20190103.models.InquiryPriceResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InquiryPriceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResult(AbstractModel):
    """用于询价输出

    """

    def __init__(self):
        """
        :param OriginalCost: 原始价格
        :type OriginalCost: float
        :param DiscountCost: 折扣后价格
        :type DiscountCost: float
        :param TimeUnit: 时间单位
        :type TimeUnit: str
        :param TimeSpan: 时间长度
        :type TimeSpan: int
        """
        self.OriginalCost = None
        self.DiscountCost = None
        self.TimeUnit = None
        self.TimeSpan = None


    def _deserialize(self, params):
        self.OriginalCost = params.get("OriginalCost")
        self.DiscountCost = params.get("DiscountCost")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")


class NodeSpec(AbstractModel):
    """节点描述

    """

    def __init__(self):
        """
        :param Memory: 内存容量,单位为M
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        :param CPUCores: CPU核数
注意：此字段可能返回 null，表示取不到有效值。
        :type CPUCores: int
        :param Volume: 数据盘容量
注意：此字段可能返回 null，表示取不到有效值。
        :type Volume: int
        :param DiskType: 磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param Spec: 节点规格描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Spec: str
        :param RootDiskVolume: 系统盘容量
注意：此字段可能返回 null，表示取不到有效值。
        :type RootDiskVolume: int
        :param StorageType: 存储类型
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param SpecName: 规格名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecName: str
        """
        self.Memory = None
        self.CPUCores = None
        self.Volume = None
        self.DiskType = None
        self.Spec = None
        self.RootDiskVolume = None
        self.StorageType = None
        self.SpecName = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.CPUCores = params.get("CPUCores")
        self.Volume = params.get("Volume")
        self.DiskType = params.get("DiskType")
        self.Spec = params.get("Spec")
        self.RootDiskVolume = params.get("RootDiskVolume")
        self.StorageType = params.get("StorageType")
        self.SpecName = params.get("SpecName")


class Placement(AbstractModel):
    """描述集实例位置信息

    """

    def __init__(self):
        """
        :param ProjectId: 实例所属项目ID。该参数可以通过调用 DescribeProject 的返回值中的 projectId 字段来获取。不填为默认项目。
        :type ProjectId: int
        :param Zone: 实例所属的可用区ID。该参数也可以通过调用 DescribeZones 的返回值中的Zone字段来获取。
        :type Zone: str
        """
        self.ProjectId = None
        self.Zone = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Zone = params.get("Zone")


class ResourceSpec(AbstractModel):
    """资源描述

    """

    def __init__(self):
        """
        :param CommonCount: Common节点数量
        :type CommonCount: int
        :param MasterResourceSpec: 描述Master节点资源
        :type MasterResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeSpec`
        :param CoreResourceSpec: 描述Core节点资源
        :type CoreResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeSpec`
        :param TaskResourceSpec: 描述Task节点资源
        :type TaskResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeSpec`
        :param MasterCount: Master节点数量
        :type MasterCount: int
        :param CoreCount: Core节点数量
        :type CoreCount: int
        :param TaskCount: Task节点数量
        :type TaskCount: int
        :param CommonResourceSpec: 描述Common节点资源
        :type CommonResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeSpec`
        """
        self.CommonCount = None
        self.MasterResourceSpec = None
        self.CoreResourceSpec = None
        self.TaskResourceSpec = None
        self.MasterCount = None
        self.CoreCount = None
        self.TaskCount = None
        self.CommonResourceSpec = None


    def _deserialize(self, params):
        self.CommonCount = params.get("CommonCount")
        if params.get("MasterResourceSpec") is not None:
            self.MasterResourceSpec = NodeSpec()
            self.MasterResourceSpec._deserialize(params.get("MasterResourceSpec"))
        if params.get("CoreResourceSpec") is not None:
            self.CoreResourceSpec = NodeSpec()
            self.CoreResourceSpec._deserialize(params.get("CoreResourceSpec"))
        if params.get("TaskResourceSpec") is not None:
            self.TaskResourceSpec = NodeSpec()
            self.TaskResourceSpec._deserialize(params.get("TaskResourceSpec"))
        self.MasterCount = params.get("MasterCount")
        self.CoreCount = params.get("CoreCount")
        self.TaskCount = params.get("TaskCount")
        if params.get("CommonResourceSpec") is not None:
            self.CommonResourceSpec = NodeSpec()
            self.CommonResourceSpec._deserialize(params.get("CommonResourceSpec"))


class VPCSettings(AbstractModel):
    """VPC 参数

    """

    def __init__(self):
        """
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")