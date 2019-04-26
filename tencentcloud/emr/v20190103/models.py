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


class COSSettings(AbstractModel):
    """COS 相关配置

    """

    def __init__(self):
        """
        :param LogOnCosPath: 日志存储在COS上的路径
        :type LogOnCosPath: str
        :param CosSecretId: COS SecretId
        :type CosSecretId: str
        :param CosSecretKey: COS SecrectKey
        :type CosSecretKey: str
        """
        self.LogOnCosPath = None
        self.CosSecretId = None
        self.CosSecretKey = None


    def _deserialize(self, params):
        self.LogOnCosPath = params.get("LogOnCosPath")
        self.CosSecretId = params.get("CosSecretId")
        self.CosSecretKey = params.get("CosSecretKey")


class ClusterInfoResult(AbstractModel):
    """查询结果

    """

    def __init__(self):
        """
        :param TotalCnt: 数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCnt: int
        :param ClusterList: 集群信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterList: list of ClusterInstanceInfo
        """
        self.TotalCnt = None
        self.ClusterList = None


    def _deserialize(self, params):
        self.TotalCnt = params.get("TotalCnt")
        if params.get("ClusterList") is not None:
            self.ClusterList = []
            for item in params.get("ClusterList"):
                obj = ClusterInstanceInfo()
                obj._deserialize(item)
                self.ClusterList.append(obj)


class ClusterInstanceInfo(AbstractModel):
    """实例信息

    """

    def __init__(self):
        """
        :param ClusterId: clusterId
        :type ClusterId: str
        :param StatusDesc: 状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param ClusterName: 集群名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param ZoneId: 集群地域
        :type ZoneId: int
        :param AppId: 用户APPID
        :type AppId: int
        :param Addtime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Addtime: str
        :param Runtime: 运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Runtime: str
        :param Config: 集群配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: :class:`tencentcloud.emr.v20190103.models.EMRProductConfigSettings`
        :param MasterIp: 集群IP
        :type MasterIp: str
        :param EmrVersion: 集群版本
        :type EmrVersion: str
        :param ChargeType: 集群计费类型
        :type ChargeType: int
        """
        self.ClusterId = None
        self.StatusDesc = None
        self.ClusterName = None
        self.ZoneId = None
        self.AppId = None
        self.Addtime = None
        self.Runtime = None
        self.Config = None
        self.MasterIp = None
        self.EmrVersion = None
        self.ChargeType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.StatusDesc = params.get("StatusDesc")
        self.ClusterName = params.get("ClusterName")
        self.ZoneId = params.get("ZoneId")
        self.AppId = params.get("AppId")
        self.Addtime = params.get("Addtime")
        self.Runtime = params.get("Runtime")
        if params.get("Config") is not None:
            self.Config = EMRProductConfigSettings()
            self.Config._deserialize(params.get("Config"))
        self.MasterIp = params.get("MasterIp")
        self.EmrVersion = params.get("EmrVersion")
        self.ChargeType = params.get("ChargeType")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: int
        :param VPCSettings: VPC设置参数
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param Software: 软件列表
        :type Software: list of str
        :param ResourceSpec: 资源描述
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.ResourceSpec`
        :param SupportHA: 支持HA
        :type SupportHA: int
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param PayMode: 计费类型
        :type PayMode: int
        :param Placement: 集群位置信息
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param TimeSpan: 时间长度
        :type TimeSpan: int
        :param TimeUnit: 时间单位
        :type TimeUnit: str
        :param LoginSettings: 登陆配置
        :type LoginSettings: :class:`tencentcloud.emr.v20190103.models.LoginSettings`
        :param ClientToken: 客户端Token
        :type ClientToken: str
        :param COSSettings: COS设置参数
        :type COSSettings: :class:`tencentcloud.emr.v20190103.models.COSSettings`
        :param SgId: 安全组ID
        :type SgId: str
        :param PreExecutedFileSettings: 预执行脚本设置
        :type PreExecutedFileSettings: :class:`tencentcloud.emr.v20190103.models.PreExecuteFileSettings`
        :param AutoRenew: 自动续费
        :type AutoRenew: int
        """
        self.ProductId = None
        self.VPCSettings = None
        self.Software = None
        self.ResourceSpec = None
        self.SupportHA = None
        self.InstanceName = None
        self.PayMode = None
        self.Placement = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.LoginSettings = None
        self.ClientToken = None
        self.COSSettings = None
        self.SgId = None
        self.PreExecutedFileSettings = None
        self.AutoRenew = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        if params.get("VPCSettings") is not None:
            self.VPCSettings = VPCSettings()
            self.VPCSettings._deserialize(params.get("VPCSettings"))
        self.Software = params.get("Software")
        if params.get("ResourceSpec") is not None:
            self.ResourceSpec = ResourceSpec()
            self.ResourceSpec._deserialize(params.get("ResourceSpec"))
        self.SupportHA = params.get("SupportHA")
        self.InstanceName = params.get("InstanceName")
        self.PayMode = params.get("PayMode")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.ClientToken = params.get("ClientToken")
        if params.get("COSSettings") is not None:
            self.COSSettings = COSSettings()
            self.COSSettings._deserialize(params.get("COSSettings"))
        self.SgId = params.get("SgId")
        if params.get("PreExecutedFileSettings") is not None:
            self.PreExecutedFileSettings = PreExecuteFileSettings()
            self.PreExecutedFileSettings._deserialize(params.get("PreExecutedFileSettings"))
        self.AutoRenew = params.get("AutoRenew")


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建实例结果信息
        :type Result: :class:`tencentcloud.emr.v20190103.models.CreateInstanceResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateInstanceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateInstanceResult(AbstractModel):
    """创建接口返回值

    """

    def __init__(self):
        """
        :param ClientToken: 客户端TOKEN
        :type ClientToken: str
        :param InstanceName: 集群名称
        :type InstanceName: str
        :param DealNames: 订单列表
        :type DealNames: list of str
        """
        self.ClientToken = None
        self.InstanceName = None
        self.DealNames = None


    def _deserialize(self, params):
        self.ClientToken = params.get("ClientToken")
        self.InstanceName = params.get("InstanceName")
        self.DealNames = params.get("DealNames")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 查询列表,  如果不填写，返回该AppId下所有实例列表
        :type InstanceIds: list of str
        :param Offset: 查询偏移量，默认0
        :type Offset: int
        :param Limit: 查询结果限制，默认值10
        :type Limit: int
        """
        self.InstanceIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 实例数量
        :type Result: :class:`tencentcloud.emr.v20190103.models.ClusterInfoResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ClusterInfoResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class EMRProductConfigSettings(AbstractModel):
    """集群的config信息

    """

    def __init__(self):
        """
        :param SoftInfo: 集群软件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SoftInfo: list of str
        :param MasterNodeSize: master节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterNodeSize: int
        :param CoreNodeSize: core节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type CoreNodeSize: int
        :param TaskNodeSize: task节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskNodeSize: int
        :param ComNodeSize: common节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ComNodeSize: int
        :param MasterResourceSpec: master规格
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeSpec`
        :param CoreResourceSpec: core规格
注意：此字段可能返回 null，表示取不到有效值。
        :type CoreResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeSpec`
        :param TaskResourceSpec: task规格
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeSpec`
        :param CommonResourceSpec: common规格
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonResourceSpec: :class:`tencentcloud.emr.v20190103.models.NodeSpec`
        :param Oncos: 是否使用COS
注意：此字段可能返回 null，表示取不到有效值。
        :type Oncos: bool
        :param COSSettings: COS配置
注意：此字段可能返回 null，表示取不到有效值。
        :type COSSettings: :class:`tencentcloud.emr.v20190103.models.COSSettings`
        """
        self.SoftInfo = None
        self.MasterNodeSize = None
        self.CoreNodeSize = None
        self.TaskNodeSize = None
        self.ComNodeSize = None
        self.MasterResourceSpec = None
        self.CoreResourceSpec = None
        self.TaskResourceSpec = None
        self.CommonResourceSpec = None
        self.Oncos = None
        self.COSSettings = None


    def _deserialize(self, params):
        self.SoftInfo = params.get("SoftInfo")
        self.MasterNodeSize = params.get("MasterNodeSize")
        self.CoreNodeSize = params.get("CoreNodeSize")
        self.TaskNodeSize = params.get("TaskNodeSize")
        self.ComNodeSize = params.get("ComNodeSize")
        if params.get("MasterResourceSpec") is not None:
            self.MasterResourceSpec = NodeSpec()
            self.MasterResourceSpec._deserialize(params.get("MasterResourceSpec"))
        if params.get("CoreResourceSpec") is not None:
            self.CoreResourceSpec = NodeSpec()
            self.CoreResourceSpec._deserialize(params.get("CoreResourceSpec"))
        if params.get("TaskResourceSpec") is not None:
            self.TaskResourceSpec = NodeSpec()
            self.TaskResourceSpec._deserialize(params.get("TaskResourceSpec"))
        if params.get("CommonResourceSpec") is not None:
            self.CommonResourceSpec = NodeSpec()
            self.CommonResourceSpec._deserialize(params.get("CommonResourceSpec"))
        self.Oncos = params.get("Oncos")
        if params.get("COSSettings") is not None:
            self.COSSettings = COSSettings()
            self.COSSettings._deserialize(params.get("COSSettings"))


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


class InquiryPriceScaleOutInstanceRequest(AbstractModel):
    """InquiryPriceScaleOutInstance请求参数结构体

    """

    def __init__(self):
        """
        :param TimeUnit: 时间单位。s:按量用例单位。m:包年包月用例单位
        :type TimeUnit: str
        :param TimeSpan: 时间长度。按量用例长度为3600。
        :type TimeSpan: int
        :param ZoneId: Zone ID
        :type ZoneId: int
        :param PayMode: 计费类型
        :type PayMode: int
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param CoreCount: 扩容Core节点个数
        :type CoreCount: int
        :param TaskCount: 扩容Task节点个数
        :type TaskCount: int
        :param Currency: 货币种类
        :type Currency: str
        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.ZoneId = None
        self.PayMode = None
        self.InstanceId = None
        self.CoreCount = None
        self.TaskCount = None
        self.Currency = None


    def _deserialize(self, params):
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.ZoneId = params.get("ZoneId")
        self.PayMode = params.get("PayMode")
        self.InstanceId = params.get("InstanceId")
        self.CoreCount = params.get("CoreCount")
        self.TaskCount = params.get("TaskCount")
        self.Currency = params.get("Currency")


class InquiryPriceScaleOutInstanceResponse(AbstractModel):
    """InquiryPriceScaleOutInstance返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 扩容价格
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


class LoginSettings(AbstractModel):
    """登录设置

    """

    def __init__(self):
        """
        :param Password: Password
        :type Password: str
        :param PublicKeyId: Public Key
        :type PublicKeyId: str
        """
        self.Password = None
        self.PublicKeyId = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.PublicKeyId = params.get("PublicKeyId")


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


class PreExecuteFileSettings(AbstractModel):
    """预执行脚本配置

    """

    def __init__(self):
        """
        :param Path: 脚本在COS上路径
        :type Path: str
        :param Args: 执行脚本参数
        :type Args: list of str
        :param Bucket: COS的Bucket名称
        :type Bucket: str
        :param Region: COS的Region名称
        :type Region: str
        :param Domain: COS的Domain数据
        :type Domain: str
        """
        self.Path = None
        self.Args = None
        self.Bucket = None
        self.Region = None
        self.Domain = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Args = params.get("Args")
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Domain = params.get("Domain")


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


class ScaleOutInstanceRequest(AbstractModel):
    """ScaleOutInstance请求参数结构体

    """

    def __init__(self):
        """
        :param ClientToken: Token
        :type ClientToken: str
        :param TimeUnit: 时间单位
        :type TimeUnit: str
        :param TimeSpan: 时间长度
        :type TimeSpan: int
        :param InstanceId: 扩容实例ID
        :type InstanceId: str
        :param PayMode: 付费类型
        :type PayMode: int
        :param PreExecutedFileSettings: 预执行脚本设置
        :type PreExecutedFileSettings: :class:`tencentcloud.emr.v20190103.models.PreExecuteFileSettings`
        :param TaskCount: 扩容Task节点数量
        :type TaskCount: int
        :param CoreCount: 扩容Core节点数量
        :type CoreCount: int
        """
        self.ClientToken = None
        self.TimeUnit = None
        self.TimeSpan = None
        self.InstanceId = None
        self.PayMode = None
        self.PreExecutedFileSettings = None
        self.TaskCount = None
        self.CoreCount = None


    def _deserialize(self, params):
        self.ClientToken = params.get("ClientToken")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.InstanceId = params.get("InstanceId")
        self.PayMode = params.get("PayMode")
        if params.get("PreExecutedFileSettings") is not None:
            self.PreExecutedFileSettings = PreExecuteFileSettings()
            self.PreExecutedFileSettings._deserialize(params.get("PreExecutedFileSettings"))
        self.TaskCount = params.get("TaskCount")
        self.CoreCount = params.get("CoreCount")


class ScaleOutInstanceResponse(AbstractModel):
    """ScaleOutInstance返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 扩容结果
        :type Result: :class:`tencentcloud.emr.v20190103.models.ScaleOutInstanceResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ScaleOutInstanceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ScaleOutInstanceResult(AbstractModel):
    """扩容实例结果描述

    """

    def __init__(self):
        """
        :param ClientToken: 客户端调用时传入的TOKEN
        :type ClientToken: str
        :param InstanceId: 扩容实例ID
        :type InstanceId: str
        :param DealNames: 订单名称
        :type DealNames: list of str
        """
        self.ClientToken = None
        self.InstanceId = None
        self.DealNames = None


    def _deserialize(self, params):
        self.ClientToken = params.get("ClientToken")
        self.InstanceId = params.get("InstanceId")
        self.DealNames = params.get("DealNames")


class TerminateInstanceRequest(AbstractModel):
    """TerminateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 被销毁的实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class TerminateInstanceResponse(AbstractModel):
    """TerminateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 退单描述
        :type Result: :class:`tencentcloud.emr.v20190103.models.TerminateResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TerminateResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class TerminateResult(AbstractModel):
    """退单请求描述描述

    """

    def __init__(self):
        """
        :param InstanceId: 退单集群ID
        :type InstanceId: str
        :param ResourceIds: 资源资源ID
        :type ResourceIds: list of str
        """
        self.InstanceId = None
        self.ResourceIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceIds = params.get("ResourceIds")


class TerminateTasksRequest(AbstractModel):
    """TerminateTasks请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 销毁节点所属实例ID
        :type InstanceId: str
        :param ResourceIds: 销毁节点ID
        :type ResourceIds: list of str
        """
        self.InstanceId = None
        self.ResourceIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceIds = params.get("ResourceIds")


class TerminateTasksResponse(AbstractModel):
    """TerminateTasks返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 退单结果
        :type Result: :class:`tencentcloud.emr.v20190103.models.TerminateResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TerminateResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


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