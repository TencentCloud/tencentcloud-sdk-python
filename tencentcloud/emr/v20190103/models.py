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


class BootstrapAction(AbstractModel):
    """引导脚本

    """

    def __init__(self):
        """
        :param Path: 脚本位置，支持cos上的文件，且只支持https协议。\n        :type Path: str\n        :param WhenRun: 执行时间。
resourceAfter 表示在机器资源申请成功后执行。
clusterBefore 表示在集群初始化前执行。
clusterAfter 表示在集群初始化后执行。\n        :type WhenRun: str\n        :param Args: 脚本参数\n        :type Args: list of str\n        """
        self.Path = None
        self.WhenRun = None
        self.Args = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.WhenRun = params.get("WhenRun")
        self.Args = params.get("Args")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class COSSettings(AbstractModel):
    """COS 相关配置

    """

    def __init__(self):
        """
        :param CosSecretId: COS SecretId\n        :type CosSecretId: str\n        :param CosSecretKey: COS SecrectKey\n        :type CosSecretKey: str\n        :param LogOnCosPath: 日志存储在COS上的路径\n        :type LogOnCosPath: str\n        """
        self.CosSecretId = None
        self.CosSecretKey = None
        self.LogOnCosPath = None


    def _deserialize(self, params):
        self.CosSecretId = params.get("CosSecretId")
        self.CosSecretKey = params.get("CosSecretKey")
        self.LogOnCosPath = params.get("LogOnCosPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdbInfo(AbstractModel):
    """出参

    """

    def __init__(self):
        """
        :param InstanceName: 数据库实例
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceName: str\n        :param Ip: 数据库IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ip: str\n        :param Port: 数据库端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type Port: int\n        :param MemSize: 数据库内存规格
注意：此字段可能返回 null，表示取不到有效值。\n        :type MemSize: int\n        :param Volume: 数据库磁盘规格
注意：此字段可能返回 null，表示取不到有效值。\n        :type Volume: int\n        :param Service: 服务标识
注意：此字段可能返回 null，表示取不到有效值。\n        :type Service: str\n        :param ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExpireTime: str\n        :param ApplyTime: 申请时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplyTime: str\n        :param PayType: 付费类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type PayType: int\n        :param ExpireFlag: 过期标识
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExpireFlag: bool\n        :param Status: 数据库状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param IsAutoRenew: 续费标识
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsAutoRenew: int\n        :param SerialNo: 数据库字符串
注意：此字段可能返回 null，表示取不到有效值。\n        :type SerialNo: str\n        :param ZoneId: ZoneId
注意：此字段可能返回 null，表示取不到有效值。\n        :type ZoneId: int\n        :param RegionId: RegionId
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegionId: int\n        """
        self.InstanceName = None
        self.Ip = None
        self.Port = None
        self.MemSize = None
        self.Volume = None
        self.Service = None
        self.ExpireTime = None
        self.ApplyTime = None
        self.PayType = None
        self.ExpireFlag = None
        self.Status = None
        self.IsAutoRenew = None
        self.SerialNo = None
        self.ZoneId = None
        self.RegionId = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.MemSize = params.get("MemSize")
        self.Volume = params.get("Volume")
        self.Service = params.get("Service")
        self.ExpireTime = params.get("ExpireTime")
        self.ApplyTime = params.get("ApplyTime")
        self.PayType = params.get("PayType")
        self.ExpireFlag = params.get("ExpireFlag")
        self.Status = params.get("Status")
        self.IsAutoRenew = params.get("IsAutoRenew")
        self.SerialNo = params.get("SerialNo")
        self.ZoneId = params.get("ZoneId")
        self.RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterInstancesInfo(AbstractModel):
    """集群实例信息

    """

    def __init__(self):
        """
        :param Id: ID号
注意：此字段可能返回 null，表示取不到有效值。\n        :type Id: int\n        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param Ftitle: 标题
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ftitle: str\n        :param ClusterName: 集群名
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterName: str\n        :param RegionId: 地域ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegionId: int\n        :param ZoneId: 地区ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ZoneId: int\n        :param AppId: 用户APPID
注意：此字段可能返回 null，表示取不到有效值。\n        :type AppId: int\n        :param Uin: 用户UIN
注意：此字段可能返回 null，表示取不到有效值。\n        :type Uin: str\n        :param ProjectId: 项目Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectId: int\n        :param VpcId: 集群VPCID
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcId: int\n        :param SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetId: int\n        :param Status: 实例的状态码。取值范围：
<li>2：表示集群运行中。</li>
<li>3：表示集群创建中。</li>
<li>4：表示集群扩容中。</li>
<li>5：表示集群增加router节点中。</li>
<li>6：表示集群安装组件中。</li>
<li>7：表示集群执行命令中。</li>
<li>8：表示重启服务中。</li>
<li>9：表示进入维护中。</li>
<li>10：表示服务暂停中。</li>
<li>11：表示退出维护中。</li>
<li>12：表示退出暂停中。</li>
<li>13：表示配置下发中。</li>
<li>14：表示销毁集群中。</li>
<li>15：表示销毁core节点中。</li>
<li>16：销毁task节点中。</li>
<li>17：表示销毁router节点中。</li>
<li>18：表示更改webproxy密码中。</li>
<li>19：表示集群隔离中。</li>
<li>20：表示集群冲正中。</li>
<li>21：表示集群回收中。</li>
<li>22：表示变配等待中。</li>
<li>23：表示集群已隔离。</li>
<li>24：表示缩容节点中。</li>
<li>33：表示集群等待退费中。</li>
<li>34：表示集群已退费。</li>
<li>301：表示创建失败。</li>
<li>302：表示扩容失败。</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param AddTime: 添加时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type AddTime: str\n        :param RunTime: 已经运行时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type RunTime: str\n        :param Config: 集群产品配置信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Config: :class:`tencentcloud.emr.v20190103.models.EmrProductConfigOutter`\n        :param MasterIp: 主节点外网IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type MasterIp: str\n        :param EmrVersion: EMR版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type EmrVersion: str\n        :param ChargeType: 收费类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ChargeType: int\n        :param TradeVersion: 交易版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type TradeVersion: int\n        :param ResourceOrderId: 资源订单ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceOrderId: int\n        :param IsTradeCluster: 是否计费集群
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsTradeCluster: int\n        :param AlarmInfo: 集群错误状态告警信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type AlarmInfo: str\n        :param IsWoodpeckerCluster: 是否采用新架构
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsWoodpeckerCluster: int\n        :param MetaDb: 元数据库信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type MetaDb: str\n        :param Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        :param HiveMetaDb: Hive元数据信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type HiveMetaDb: str\n        :param ServiceClass: 集群类型:EMR,CLICKHOUSE,DRUID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceClass: str\n        :param AliasInfo: 集群所有节点的别名序列化
注意：此字段可能返回 null，表示取不到有效值。\n        :type AliasInfo: str\n        :param ProductId: 集群版本Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductId: int\n        :param Zone: 地区ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type Zone: str\n        """
        self.Id = None
        self.ClusterId = None
        self.Ftitle = None
        self.ClusterName = None
        self.RegionId = None
        self.ZoneId = None
        self.AppId = None
        self.Uin = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.AddTime = None
        self.RunTime = None
        self.Config = None
        self.MasterIp = None
        self.EmrVersion = None
        self.ChargeType = None
        self.TradeVersion = None
        self.ResourceOrderId = None
        self.IsTradeCluster = None
        self.AlarmInfo = None
        self.IsWoodpeckerCluster = None
        self.MetaDb = None
        self.Tags = None
        self.HiveMetaDb = None
        self.ServiceClass = None
        self.AliasInfo = None
        self.ProductId = None
        self.Zone = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ClusterId = params.get("ClusterId")
        self.Ftitle = params.get("Ftitle")
        self.ClusterName = params.get("ClusterName")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.AddTime = params.get("AddTime")
        self.RunTime = params.get("RunTime")
        if params.get("Config") is not None:
            self.Config = EmrProductConfigOutter()
            self.Config._deserialize(params.get("Config"))
        self.MasterIp = params.get("MasterIp")
        self.EmrVersion = params.get("EmrVersion")
        self.ChargeType = params.get("ChargeType")
        self.TradeVersion = params.get("TradeVersion")
        self.ResourceOrderId = params.get("ResourceOrderId")
        self.IsTradeCluster = params.get("IsTradeCluster")
        self.AlarmInfo = params.get("AlarmInfo")
        self.IsWoodpeckerCluster = params.get("IsWoodpeckerCluster")
        self.MetaDb = params.get("MetaDb")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.HiveMetaDb = params.get("HiveMetaDb")
        self.ServiceClass = params.get("ServiceClass")
        self.AliasInfo = params.get("AliasInfo")
        self.ProductId = params.get("ProductId")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterSetting(AbstractModel):
    """集群配置。

    """

    def __init__(self):
        """
        :param InstanceChargeType: 付费方式。
PREPAID 包年包月。
POSTPAID_BY_HOUR 按量计费，默认方式。\n        :type InstanceChargeType: str\n        :param SupportHA: 是否为HA集群。\n        :type SupportHA: bool\n        :param SecurityGroupIds: 集群所使用的安全组，目前仅支持一个。\n        :type SecurityGroupIds: list of str\n        :param Placement: 实例位置。\n        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`\n        :param VPCSettings: 实例所在VPC。\n        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`\n        :param LoginSettings: 实例登录配置。\n        :type LoginSettings: :class:`tencentcloud.emr.v20190103.models.LoginSettings`\n        :param TagSpecification: 实例标签。\n        :type TagSpecification: list of str\n        :param MetaDB: 元数据库配置。\n        :type MetaDB: :class:`tencentcloud.emr.v20190103.models.MetaDbInfo`\n        :param ResourceSpec: 实例硬件配置。\n        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.JobFlowResourceSpec`\n        :param PublicIpAssigned: 是否申请公网IP，默认为false。\n        :type PublicIpAssigned: bool\n        :param InstanceChargePrepaid: 包年包月配置，只对包年包月集群生效。\n        :type InstanceChargePrepaid: :class:`tencentcloud.emr.v20190103.models.InstanceChargePrepaid`\n        :param DisasterRecoverGroupIds: 集群置放群组。\n        :type DisasterRecoverGroupIds: str\n        :param CbsEncryptFlag: 是否使用cbs加密。\n        :type CbsEncryptFlag: bool\n        :param RemoteTcpDefaultPort: 是否使用远程登录，默认为false。\n        :type RemoteTcpDefaultPort: bool\n        """
        self.InstanceChargeType = None
        self.SupportHA = None
        self.SecurityGroupIds = None
        self.Placement = None
        self.VPCSettings = None
        self.LoginSettings = None
        self.TagSpecification = None
        self.MetaDB = None
        self.ResourceSpec = None
        self.PublicIpAssigned = None
        self.InstanceChargePrepaid = None
        self.DisasterRecoverGroupIds = None
        self.CbsEncryptFlag = None
        self.RemoteTcpDefaultPort = None


    def _deserialize(self, params):
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.SupportHA = params.get("SupportHA")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        if params.get("VPCSettings") is not None:
            self.VPCSettings = VPCSettings()
            self.VPCSettings._deserialize(params.get("VPCSettings"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.TagSpecification = params.get("TagSpecification")
        if params.get("MetaDB") is not None:
            self.MetaDB = MetaDbInfo()
            self.MetaDB._deserialize(params.get("MetaDB"))
        if params.get("ResourceSpec") is not None:
            self.ResourceSpec = JobFlowResourceSpec()
            self.ResourceSpec._deserialize(params.get("ResourceSpec"))
        self.PublicIpAssigned = params.get("PublicIpAssigned")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self.CbsEncryptFlag = params.get("CbsEncryptFlag")
        self.RemoteTcpDefaultPort = params.get("RemoteTcpDefaultPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Configuration(AbstractModel):
    """自定义配置参数

    """

    def __init__(self):
        """
        :param Classification: 配置文件名，支持SPARK、HIVE、HDFS、YARN的部分配置文件自定义。\n        :type Classification: str\n        :param Properties: 配置参数通过KV的形式传入，部分文件支持自定义，可以通过特殊的键"content"传入所有内容。\n        :type Properties: str\n        """
        self.Classification = None
        self.Properties = None


    def _deserialize(self, params):
        self.Classification = params.get("Classification")
        self.Properties = params.get("Properties")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID，不同产品ID表示不同的EMR产品版本。取值范围：
<li>1：表示EMR-V1.3.1。</li>
<li>2：表示EMR-V2.0.1。</li>
<li>4：表示EMR-V2.1.0。</li>
<li>7：表示EMR-V3.0.0。</li>
<li>9：表示EMR-V2.2.0。</li>
<li>11：表示CLICKHOUSE-V1.0.0。</li>
<li>13：表示DRUID-V1.0.0。</li>
<li>15：表示EMR-V2.2.1。</li>
<li>16：表示EMR-V2.3.0。</li>
<li>17：表示CLICKHOUSE-V1.1.0。</li>
<li>19：表示EMR-V2.4.0。</li>
<li>20：表示EMR-V2.5.0。</li>
<li>22：表示CLICKHOUSE-V1.2.0。</li>
<li>24：表示EMR-TianQiong-V1.0.0。</li>
<li>25：表示EMR-V3.1.0。</li>
<li>26：表示DORIS-V1.0.0。</li>
<li>27：表示KAFKA-V1.0.0。</li>
<li>28：表示EMR-V3.2.0。</li>
<li>29：表示EMR-V2.5.1。</li>
<li>30：表示EMR-V2.6.0。</li>\n        :type ProductId: int\n        :param VPCSettings: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。\n        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`\n        :param Software: 部署的组件列表。不同的EMR产品ID（ProductId：具体含义参考入参ProductId字段）对应不同可选组件列表，不同产品版本可选组件列表查询：[组件版本](https://cloud.tencent.com/document/product/589/20279) ；
填写实例值：hive、flink。\n        :type Software: list of str\n        :param ResourceSpec: 节点资源的规格。\n        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`\n        :param SupportHA: 是否开启节点高可用。取值范围：
<li>0：表示不开启节点高可用。</li>
<li>1：表示开启节点高可用。</li>\n        :type SupportHA: int\n        :param InstanceName: 实例名称。
<li>长度限制为6-36个字符。</li>
<li>只允许包含中文、字母、数字、-、_。</li>\n        :type InstanceName: str\n        :param PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>\n        :type PayMode: int\n        :param Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。\n        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`\n        :param TimeSpan: 购买实例的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>\n        :type TimeSpan: int\n        :param TimeUnit: 购买实例的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>\n        :type TimeUnit: str\n        :param LoginSettings: 实例登录设置。通过该参数可以设置所购买节点的登录方式密码或者密钥。
<li>设置密钥时，密码仅用于组件原生WebUI快捷入口登录。</li>
<li>未设置密钥时，密码用于登录所购节点以及组件原生WebUI快捷入口登录。</li>\n        :type LoginSettings: :class:`tencentcloud.emr.v20190103.models.LoginSettings`\n        :param COSSettings: 开启COS访问需要设置的参数。\n        :type COSSettings: :class:`tencentcloud.emr.v20190103.models.COSSettings`\n        :param SgId: 实例所属安全组的ID，形如sg-xxxxxxxx。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的SecurityGroupId字段来获取。\n        :type SgId: str\n        :param PreExecutedFileSettings: [引导操作](https://cloud.tencent.com/document/product/589/35656)脚本设置。\n        :type PreExecutedFileSettings: list of PreExecuteFileSettings\n        :param AutoRenew: 包年包月实例是否自动续费。取值范围：
<li>0：表示不自动续费。</li>
<li>1：表示自动续费。</li>\n        :type AutoRenew: int\n        :param ClientToken: 客户端Token。\n        :type ClientToken: str\n        :param NeedMasterWan: 是否开启集群Master节点公网。取值范围：
<li>NEED_MASTER_WAN：表示开启集群Master节点公网。</li>
<li>NOT_NEED_MASTER_WAN：表示不开启。</li>默认开启集群Master节点公网。\n        :type NeedMasterWan: str\n        :param RemoteLoginAtCreate: 是否需要开启外网远程登录，即22号端口。在SgId不为空时，该参数无效。\n        :type RemoteLoginAtCreate: int\n        :param CheckSecurity: 是否开启安全集群。0表示不开启，非0表示开启。\n        :type CheckSecurity: int\n        :param ExtendFsField: 访问外部文件系统。\n        :type ExtendFsField: str\n        :param Tags: 标签描述列表。通过指定该参数可以同时绑定标签到相应的实例。\n        :type Tags: list of Tag\n        :param DisasterRecoverGroupIds: 分散置放群组ID列表，当前只支持指定一个。
该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/product/213/15486 ) 的返回值中的SecurityGroupId字段来获取。\n        :type DisasterRecoverGroupIds: list of str\n        :param CbsEncrypt: 集群维度CBS加密盘，默认0表示不加密，1表示加密\n        :type CbsEncrypt: int\n        :param MetaType: hive共享元数据库类型。取值范围：
<li>EMR_NEW_META：表示集群默认创建</li>
<li>EMR_EXIT_META：表示集群使用指定EMR-MetaDB。</li>
<li>USER_CUSTOM_META：表示集群使用自定义MetaDB。</li>\n        :type MetaType: str\n        :param UnifyMetaInstanceId: EMR-MetaDB实例\n        :type UnifyMetaInstanceId: str\n        :param MetaDBInfo: 自定义MetaDB信息\n        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`\n        :param ApplicationRole: 自定义应用角色。\n        :type ApplicationRole: str\n        """
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
        self.COSSettings = None
        self.SgId = None
        self.PreExecutedFileSettings = None
        self.AutoRenew = None
        self.ClientToken = None
        self.NeedMasterWan = None
        self.RemoteLoginAtCreate = None
        self.CheckSecurity = None
        self.ExtendFsField = None
        self.Tags = None
        self.DisasterRecoverGroupIds = None
        self.CbsEncrypt = None
        self.MetaType = None
        self.UnifyMetaInstanceId = None
        self.MetaDBInfo = None
        self.ApplicationRole = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        if params.get("VPCSettings") is not None:
            self.VPCSettings = VPCSettings()
            self.VPCSettings._deserialize(params.get("VPCSettings"))
        self.Software = params.get("Software")
        if params.get("ResourceSpec") is not None:
            self.ResourceSpec = NewResourceSpec()
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
        if params.get("COSSettings") is not None:
            self.COSSettings = COSSettings()
            self.COSSettings._deserialize(params.get("COSSettings"))
        self.SgId = params.get("SgId")
        if params.get("PreExecutedFileSettings") is not None:
            self.PreExecutedFileSettings = []
            for item in params.get("PreExecutedFileSettings"):
                obj = PreExecuteFileSettings()
                obj._deserialize(item)
                self.PreExecutedFileSettings.append(obj)
        self.AutoRenew = params.get("AutoRenew")
        self.ClientToken = params.get("ClientToken")
        self.NeedMasterWan = params.get("NeedMasterWan")
        self.RemoteLoginAtCreate = params.get("RemoteLoginAtCreate")
        self.CheckSecurity = params.get("CheckSecurity")
        self.ExtendFsField = params.get("ExtendFsField")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self.CbsEncrypt = params.get("CbsEncrypt")
        self.MetaType = params.get("MetaType")
        self.UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        if params.get("MetaDBInfo") is not None:
            self.MetaDBInfo = CustomMetaInfo()
            self.MetaDBInfo._deserialize(params.get("MetaDBInfo"))
        self.ApplicationRole = params.get("ApplicationRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class CustomMetaInfo(AbstractModel):
    """用户自建Hive-MetaDB信息

    """

    def __init__(self):
        """
        :param MetaDataJdbcUrl: 自定义MetaDB的JDBC连接，请以 jdbc:mysql:// 开头\n        :type MetaDataJdbcUrl: str\n        :param MetaDataUser: 自定义MetaDB用户名\n        :type MetaDataUser: str\n        :param MetaDataPass: 自定义MetaDB密码\n        :type MetaDataPass: str\n        """
        self.MetaDataJdbcUrl = None
        self.MetaDataUser = None
        self.MetaDataPass = None


    def _deserialize(self, params):
        self.MetaDataJdbcUrl = params.get("MetaDataJdbcUrl")
        self.MetaDataUser = params.get("MetaDataUser")
        self.MetaDataPass = params.get("MetaDataPass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterNodesRequest(AbstractModel):
    """DescribeClusterNodes请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 集群实例ID,实例ID形如: emr-xxxxxxxx\n        :type InstanceId: str\n        :param NodeFlag: 节点标识，取值为：
<li>all：表示获取全部类型节点，cdb信息除外。</li>
<li>master：表示获取master节点信息。</li>
<li>core：表示获取core节点信息。</li>
<li>task：表示获取task节点信息。</li>
<li>common：表示获取common节点信息。</li>
<li>router：表示获取router节点信息。</li>
<li>db：表示获取正常状态的cdb信息。</li>
<li>recyle：表示获取回收站隔离中的节点信息，包括cdb信息。</li>
<li>renew：表示获取所有待续费的节点信息，包括cdb信息，自动续费节点不会返回。</li>
注意：现在只支持以上取值，输入其他值会导致错误。\n        :type NodeFlag: str\n        :param Offset: 页编号，默认值为0，表示第一页。\n        :type Offset: int\n        :param Limit: 每页返回数量，默认值为100，最大值为100。\n        :type Limit: int\n        :param HardwareResourceType: 资源类型:支持all/host/pod，默认为all\n        :type HardwareResourceType: str\n        :param SearchFields: 支持搜索的字段\n        :type SearchFields: list of SearchItem\n        """
        self.InstanceId = None
        self.NodeFlag = None
        self.Offset = None
        self.Limit = None
        self.HardwareResourceType = None
        self.SearchFields = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NodeFlag = params.get("NodeFlag")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.HardwareResourceType = params.get("HardwareResourceType")
        if params.get("SearchFields") is not None:
            self.SearchFields = []
            for item in params.get("SearchFields"):
                obj = SearchItem()
                obj._deserialize(item)
                self.SearchFields.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterNodesResponse(AbstractModel):
    """DescribeClusterNodes返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCnt: 查询到的节点总数\n        :type TotalCnt: int\n        :param NodeList: 节点详细信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type NodeList: list of NodeHardwareInfo\n        :param TagKeys: 用户所有的标签键列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagKeys: list of str\n        :param HardwareResourceTypeList: 资源类型列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type HardwareResourceTypeList: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCnt = None
        self.NodeList = None
        self.TagKeys = None
        self.HardwareResourceTypeList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCnt = params.get("TotalCnt")
        if params.get("NodeList") is not None:
            self.NodeList = []
            for item in params.get("NodeList"):
                obj = NodeHardwareInfo()
                obj._deserialize(item)
                self.NodeList.append(obj)
        self.TagKeys = params.get("TagKeys")
        self.HardwareResourceTypeList = params.get("HardwareResourceTypeList")
        self.RequestId = params.get("RequestId")


class DescribeCvmQuotaRequest(AbstractModel):
    """DescribeCvmQuota请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: EMR集群ID\n        :type ClusterId: str\n        :param ZoneId: 区ID\n        :type ZoneId: int\n        """
        self.ClusterId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCvmQuotaResponse(AbstractModel):
    """DescribeCvmQuota返回参数结构体

    """

    def __init__(self):
        """
        :param PostPaidQuotaSet: 后付费配额列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type PostPaidQuotaSet: list of QuotaEntity\n        :param SpotPaidQuotaSet: 竞价实例配额列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type SpotPaidQuotaSet: list of QuotaEntity\n        :param EksQuotaSet: eks配额
注意：此字段可能返回 null，表示取不到有效值。\n        :type EksQuotaSet: list of PodSaleSpec\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PostPaidQuotaSet = None
        self.SpotPaidQuotaSet = None
        self.EksQuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PostPaidQuotaSet") is not None:
            self.PostPaidQuotaSet = []
            for item in params.get("PostPaidQuotaSet"):
                obj = QuotaEntity()
                obj._deserialize(item)
                self.PostPaidQuotaSet.append(obj)
        if params.get("SpotPaidQuotaSet") is not None:
            self.SpotPaidQuotaSet = []
            for item in params.get("SpotPaidQuotaSet"):
                obj = QuotaEntity()
                obj._deserialize(item)
                self.SpotPaidQuotaSet.append(obj)
        if params.get("EksQuotaSet") is not None:
            self.EksQuotaSet = []
            for item in params.get("EksQuotaSet"):
                obj = PodSaleSpec()
                obj._deserialize(item)
                self.EksQuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceRenewNodesRequest(AbstractModel):
    """DescribeInstanceRenewNodes请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 集群实例ID,实例ID形如: emr-xxxxxxxx\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceRenewNodesResponse(AbstractModel):
    """DescribeInstanceRenewNodes返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCnt: 查询到的节点总数\n        :type TotalCnt: int\n        :param NodeList: 节点详细信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type NodeList: list of RenewInstancesInfo\n        :param MetaInfo: 用户所有的标签键列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type MetaInfo: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCnt = None
        self.NodeList = None
        self.MetaInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCnt = params.get("TotalCnt")
        if params.get("NodeList") is not None:
            self.NodeList = []
            for item in params.get("NodeList"):
                obj = RenewInstancesInfo()
                obj._deserialize(item)
                self.NodeList.append(obj)
        self.MetaInfo = params.get("MetaInfo")
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        """
        :param DisplayStrategy: 集群筛选策略。取值范围：
<li>clusterList：表示查询除了已销毁集群之外的集群列表。</li>
<li>monitorManage：表示查询除了已销毁、创建中以及创建失败的集群之外的集群列表。</li>
<li>cloudHardwareManage/componentManage：目前这两个取值为预留取值，暂时和monitorManage表示同样的含义。</li>\n        :type DisplayStrategy: str\n        :param InstanceIds: 按照一个或者多个实例ID查询。实例ID形如: emr-xxxxxxxx 。(此参数的具体格式可参考API[简介](https://cloud.tencent.com/document/api/213/15688)的 Ids.N 一节)。如果不填写实例ID，返回该APPID下所有实例列表。\n        :type InstanceIds: list of str\n        :param Offset: 页编号，默认值为0，表示第一页。\n        :type Offset: int\n        :param Limit: 每页返回数量，默认值为10，最大值为100。\n        :type Limit: int\n        :param ProjectId: 建议必填-1，表示拉取所有项目下的集群。
不填默认值为0，表示拉取默认项目下的集群。
实例所属项目ID。该参数可以通过调用 [DescribeProject](https://cloud.tencent.com/document/api/378/4400) 的返回值中的 projectId 字段来获取。\n        :type ProjectId: int\n        :param OrderField: 排序字段。取值范围：
<li>clusterId：表示按照实例ID排序。</li>
<li>addTime：表示按照实例创建时间排序。</li>
<li>status：表示按照实例的状态码排序。</li>\n        :type OrderField: str\n        :param Asc: 按照OrderField升序或者降序进行排序。取值范围：
<li>0：表示降序。</li>
<li>1：表示升序。</li>默认值为0。\n        :type Asc: int\n        """
        self.DisplayStrategy = None
        self.InstanceIds = None
        self.Offset = None
        self.Limit = None
        self.ProjectId = None
        self.OrderField = None
        self.Asc = None


    def _deserialize(self, params):
        self.DisplayStrategy = params.get("DisplayStrategy")
        self.InstanceIds = params.get("InstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProjectId = params.get("ProjectId")
        self.OrderField = params.get("OrderField")
        self.Asc = params.get("Asc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCnt: 符合条件的实例总数。\n        :type TotalCnt: int\n        :param ClusterList: EMR实例详细信息列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterList: list of ClusterInstancesInfo\n        :param TagKeys: 实例关联的标签键列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagKeys: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCnt = None
        self.ClusterList = None
        self.TagKeys = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCnt = params.get("TotalCnt")
        if params.get("ClusterList") is not None:
            self.ClusterList = []
            for item in params.get("ClusterList"):
                obj = ClusterInstancesInfo()
                obj._deserialize(item)
                self.ClusterList.append(obj)
        self.TagKeys = params.get("TagKeys")
        self.RequestId = params.get("RequestId")


class DescribeJobFlowRequest(AbstractModel):
    """DescribeJobFlow请求参数结构体

    """

    def __init__(self):
        """
        :param JobFlowId: 流程任务Id，RunJobFlow接口返回的值。\n        :type JobFlowId: int\n        """
        self.JobFlowId = None


    def _deserialize(self, params):
        self.JobFlowId = params.get("JobFlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobFlowResponse(AbstractModel):
    """DescribeJobFlow返回参数结构体

    """

    def __init__(self):
        """
        :param State: 流程任务状态，可以为以下值：
JobFlowInit，流程任务初始化。
JobFlowResourceApplied，资源申请中，通常为JobFlow需要新建集群时的状态。
JobFlowResourceReady，执行流程任务的资源就绪。
JobFlowStepsRunning，流程任务步骤已提交。
JobFlowStepsComplete，流程任务步骤已完成。
JobFlowTerminating，流程任务所需资源销毁中。
JobFlowFinish，流程任务已完成。\n        :type State: str\n        :param Details: 流程任务步骤结果。\n        :type Details: list of JobResult\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.State = None
        self.Details = None
        self.RequestId = None


    def _deserialize(self, params):
        self.State = params.get("State")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = JobResult()
                obj._deserialize(item)
                self.Details.append(obj)
        self.RequestId = params.get("RequestId")


class DiskGroup(AbstractModel):
    """磁盘组。

    """

    def __init__(self):
        """
        :param Spec: 磁盘规格。\n        :type Spec: :class:`tencentcloud.emr.v20190103.models.DiskSpec`\n        :param Count: 同类型磁盘数量。\n        :type Count: int\n        """
        self.Spec = None
        self.Count = None


    def _deserialize(self, params):
        if params.get("Spec") is not None:
            self.Spec = DiskSpec()
            self.Spec._deserialize(params.get("Spec"))
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskSpec(AbstractModel):
    """磁盘描述。

    """

    def __init__(self):
        """
        :param DiskType: 磁盘类型。
LOCAL_BASIC  本地盘。
CLOUD_BASIC 云硬盘。
LOCAL_SSD 本地SSD。
CLOUD_SSD 云SSD。
CLOUD_PREMIUM 高效云盘。
CLOUD_HSSD 增强型云SSD。\n        :type DiskType: str\n        :param DiskSize: 磁盘大小，单位GB。\n        :type DiskSize: int\n        """
        self.DiskType = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DynamicPodSpec(AbstractModel):
    """POD浮动规格

    """

    def __init__(self):
        """
        :param RequestCpu: 需求最小cpu核数\n        :type RequestCpu: float\n        :param LimitCpu: 需求最大cpu核数\n        :type LimitCpu: float\n        :param RequestMemory: 需求最小memory，单位MB\n        :type RequestMemory: float\n        :param LimitMemory: 需求最大memory，单位MB\n        :type LimitMemory: float\n        """
        self.RequestCpu = None
        self.LimitCpu = None
        self.RequestMemory = None
        self.LimitMemory = None


    def _deserialize(self, params):
        self.RequestCpu = params.get("RequestCpu")
        self.LimitCpu = params.get("LimitCpu")
        self.RequestMemory = params.get("RequestMemory")
        self.LimitMemory = params.get("LimitMemory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmrProductConfigOutter(AbstractModel):
    """EMR产品配置

    """

    def __init__(self):
        """
        :param SoftInfo: 软件信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type SoftInfo: list of str\n        :param MasterNodeSize: Master节点个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MasterNodeSize: int\n        :param CoreNodeSize: Core节点个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type CoreNodeSize: int\n        :param TaskNodeSize: Task节点个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskNodeSize: int\n        :param ComNodeSize: Common节点个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ComNodeSize: int\n        :param MasterResource: Master节点资源
注意：此字段可能返回 null，表示取不到有效值。\n        :type MasterResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`\n        :param CoreResource: Core节点资源
注意：此字段可能返回 null，表示取不到有效值。\n        :type CoreResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`\n        :param TaskResource: Task节点资源
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`\n        :param ComResource: Common节点资源
注意：此字段可能返回 null，表示取不到有效值。\n        :type ComResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`\n        :param OnCos: 是否使用COS
注意：此字段可能返回 null，表示取不到有效值。\n        :type OnCos: bool\n        :param ChargeType: 收费类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ChargeType: int\n        :param RouterNodeSize: Router节点个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type RouterNodeSize: int\n        :param SupportHA: 是否支持HA
注意：此字段可能返回 null，表示取不到有效值。\n        :type SupportHA: bool\n        :param SecurityOn: 是否支持安全模式
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecurityOn: bool\n        :param SecurityGroup: 安全组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecurityGroup: str\n        :param CbsEncrypt: 是否开启Cbs加密
注意：此字段可能返回 null，表示取不到有效值。\n        :type CbsEncrypt: int\n        :param ApplicationRole: 自定义应用角色。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplicationRole: str\n        :param SecurityGroups: 安全组
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecurityGroups: list of str\n        """
        self.SoftInfo = None
        self.MasterNodeSize = None
        self.CoreNodeSize = None
        self.TaskNodeSize = None
        self.ComNodeSize = None
        self.MasterResource = None
        self.CoreResource = None
        self.TaskResource = None
        self.ComResource = None
        self.OnCos = None
        self.ChargeType = None
        self.RouterNodeSize = None
        self.SupportHA = None
        self.SecurityOn = None
        self.SecurityGroup = None
        self.CbsEncrypt = None
        self.ApplicationRole = None
        self.SecurityGroups = None


    def _deserialize(self, params):
        self.SoftInfo = params.get("SoftInfo")
        self.MasterNodeSize = params.get("MasterNodeSize")
        self.CoreNodeSize = params.get("CoreNodeSize")
        self.TaskNodeSize = params.get("TaskNodeSize")
        self.ComNodeSize = params.get("ComNodeSize")
        if params.get("MasterResource") is not None:
            self.MasterResource = OutterResource()
            self.MasterResource._deserialize(params.get("MasterResource"))
        if params.get("CoreResource") is not None:
            self.CoreResource = OutterResource()
            self.CoreResource._deserialize(params.get("CoreResource"))
        if params.get("TaskResource") is not None:
            self.TaskResource = OutterResource()
            self.TaskResource._deserialize(params.get("TaskResource"))
        if params.get("ComResource") is not None:
            self.ComResource = OutterResource()
            self.ComResource._deserialize(params.get("ComResource"))
        self.OnCos = params.get("OnCos")
        self.ChargeType = params.get("ChargeType")
        self.RouterNodeSize = params.get("RouterNodeSize")
        self.SupportHA = params.get("SupportHA")
        self.SecurityOn = params.get("SecurityOn")
        self.SecurityGroup = params.get("SecurityGroup")
        self.CbsEncrypt = params.get("CbsEncrypt")
        self.ApplicationRole = params.get("ApplicationRole")
        self.SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Execution(AbstractModel):
    """执行动作。

    """

    def __init__(self):
        """
        :param JobType: 任务类型，目前支持以下类型。
1. “MR”，将通过hadoop jar的方式提交。
2. "HIVE"，将通过hive -f的方式提交。
3. "SPARK"，将通过spark-submit的方式提交。\n        :type JobType: str\n        :param Args: 任务参数，提供除提交指令以外的参数。\n        :type Args: list of str\n        """
        self.JobType = None
        self.Args = None


    def _deserialize(self, params):
        self.JobType = params.get("JobType")
        self.Args = params.get("Args")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostVolumeContext(AbstractModel):
    """Pod HostPath挂载方式描述

    """

    def __init__(self):
        """
        :param VolumePath: Pod挂载宿主机的目录。资源对宿主机的挂载点，指定的挂载点对应了宿主机的路径，该挂载点在Pod中作为数据存储目录使用
注意：此字段可能返回 null，表示取不到有效值。\n        :type VolumePath: str\n        """
        self.VolumePath = None


    def _deserialize(self, params):
        self.VolumePath = params.get("VolumePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewEmrRequest(AbstractModel):
    """InquirePriceRenewEmr请求参数结构体

    """

    def __init__(self):
        """
        :param TimeSpan: 实例续费的时长。需要结合TimeUnit一起使用。1表示续费1一个月\n        :type TimeSpan: int\n        :param InstanceId: 待续费集群ID列表。\n        :type InstanceId: str\n        :param Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。\n        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`\n        :param PayMode: 实例计费模式。此处只支持取值为1，表示包年包月。\n        :type PayMode: int\n        :param TimeUnit: 实例续费的时间单位。取值范围：
<li>m：表示月份。</li>\n        :type TimeUnit: str\n        :param Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>\n        :type Currency: str\n        """
        self.TimeSpan = None
        self.InstanceId = None
        self.Placement = None
        self.PayMode = None
        self.TimeUnit = None
        self.Currency = None


    def _deserialize(self, params):
        self.TimeSpan = params.get("TimeSpan")
        self.InstanceId = params.get("InstanceId")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.PayMode = params.get("PayMode")
        self.TimeUnit = params.get("TimeUnit")
        self.Currency = params.get("Currency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewEmrResponse(AbstractModel):
    """InquirePriceRenewEmr返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginalCost: float\n        :param DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiscountCost: float\n        :param TimeUnit: 实例续费的时间单位。取值范围：
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeUnit: str\n        :param TimeSpan: 实例续费的时长。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeSpan: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.OriginalCost = None
        self.DiscountCost = None
        self.TimeUnit = None
        self.TimeSpan = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalCost = params.get("OriginalCost")
        self.DiscountCost = params.get("DiscountCost")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.RequestId = params.get("RequestId")


class InquiryPriceCreateInstanceRequest(AbstractModel):
    """InquiryPriceCreateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param TimeUnit: 购买实例的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>\n        :type TimeUnit: str\n        :param TimeSpan: 购买实例的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>\n        :type TimeSpan: int\n        :param ResourceSpec: 询价的节点规格。\n        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`\n        :param Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>\n        :type Currency: str\n        :param PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>\n        :type PayMode: int\n        :param SupportHA: 是否开启节点高可用。取值范围：
<li>0：表示不开启节点高可用。</li>
<li>1：表示开启节点高可用。</li>\n        :type SupportHA: int\n        :param Software: 部署的组件列表。不同的EMR产品ID（ProductId：具体含义参考入参ProductId字段）需要选择不同的必选组件：
<li>ProductId为1的时候，必选组件包括：hadoop-2.7.3、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId为2的时候，必选组件包括：hadoop-2.7.3、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId为4的时候，必选组件包括：hadoop-2.8.4、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId为7的时候，必选组件包括：hadoop-3.1.2、knox-1.2.0、zookeeper-3.4.9</li>\n        :type Software: list of str\n        :param Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。\n        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`\n        :param VPCSettings: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。\n        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`\n        :param MetaType: hive共享元数据库类型。取值范围：
<li>EMR_NEW_META：表示集群默认创建</li>
<li>EMR_EXIT_METE：表示集群使用指定EMR-MetaDB。</li>
<li>USER_CUSTOM_META：表示集群使用自定义MetaDB。</li>\n        :type MetaType: str\n        :param UnifyMetaInstanceId: EMR-MetaDB实例\n        :type UnifyMetaInstanceId: str\n        :param MetaDBInfo: 自定义MetaDB信息\n        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`\n        :param ProductId: 产品ID，不同产品ID表示不同的EMR产品版本。取值范围：
<li>1：表示EMR-V1.3.1。</li>
<li>2：表示EMR-V2.0.1。</li>
<li>4：表示EMR-V2.1.0。</li>
<li>7：表示EMR-V3.0.0。</li>\n        :type ProductId: int\n        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.ResourceSpec = None
        self.Currency = None
        self.PayMode = None
        self.SupportHA = None
        self.Software = None
        self.Placement = None
        self.VPCSettings = None
        self.MetaType = None
        self.UnifyMetaInstanceId = None
        self.MetaDBInfo = None
        self.ProductId = None


    def _deserialize(self, params):
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        if params.get("ResourceSpec") is not None:
            self.ResourceSpec = NewResourceSpec()
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
        self.MetaType = params.get("MetaType")
        self.UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        if params.get("MetaDBInfo") is not None:
            self.MetaDBInfo = CustomMetaInfo()
            self.MetaDBInfo._deserialize(params.get("MetaDBInfo"))
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateInstanceResponse(AbstractModel):
    """InquiryPriceCreateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginalCost: float\n        :param DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiscountCost: float\n        :param TimeUnit: 购买实例的时间单位。取值范围：
<li>s：表示秒。</li>
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeUnit: str\n        :param TimeSpan: 购买实例的时长。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeSpan: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.OriginalCost = None
        self.DiscountCost = None
        self.TimeUnit = None
        self.TimeSpan = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalCost = params.get("OriginalCost")
        self.DiscountCost = params.get("DiscountCost")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.RequestId = params.get("RequestId")


class InquiryPriceRenewInstanceRequest(AbstractModel):
    """InquiryPriceRenewInstance请求参数结构体

    """

    def __init__(self):
        """
        :param TimeSpan: 实例续费的时长。需要结合TimeUnit一起使用。1表示续费1一个月\n        :type TimeSpan: int\n        :param ResourceIds: 待续费节点的资源ID列表。资源ID形如：emr-vm-xxxxxxxx。有效的资源ID可通过登录[控制台](https://console.cloud.tencent.com/emr/static/hardware)查询。\n        :type ResourceIds: list of str\n        :param Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。\n        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`\n        :param PayMode: 实例计费模式。此处只支持取值为1，表示包年包月。\n        :type PayMode: int\n        :param TimeUnit: 实例续费的时间单位。取值范围：
<li>m：表示月份。</li>\n        :type TimeUnit: str\n        :param Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>\n        :type Currency: str\n        :param ModifyPayMode: 是否按量转包年包月。0：否，1：是。\n        :type ModifyPayMode: int\n        """
        self.TimeSpan = None
        self.ResourceIds = None
        self.Placement = None
        self.PayMode = None
        self.TimeUnit = None
        self.Currency = None
        self.ModifyPayMode = None


    def _deserialize(self, params):
        self.TimeSpan = params.get("TimeSpan")
        self.ResourceIds = params.get("ResourceIds")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.PayMode = params.get("PayMode")
        self.TimeUnit = params.get("TimeUnit")
        self.Currency = params.get("Currency")
        self.ModifyPayMode = params.get("ModifyPayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewInstanceResponse(AbstractModel):
    """InquiryPriceRenewInstance返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginalCost: float\n        :param DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiscountCost: float\n        :param TimeUnit: 实例续费的时间单位。取值范围：
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeUnit: str\n        :param TimeSpan: 实例续费的时长。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeSpan: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.OriginalCost = None
        self.DiscountCost = None
        self.TimeUnit = None
        self.TimeSpan = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalCost = params.get("OriginalCost")
        self.DiscountCost = params.get("DiscountCost")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.RequestId = params.get("RequestId")


class InquiryPriceScaleOutInstanceRequest(AbstractModel):
    """InquiryPriceScaleOutInstance请求参数结构体

    """

    def __init__(self):
        """
        :param TimeUnit: 扩容的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>\n        :type TimeUnit: str\n        :param TimeSpan: 扩容的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>\n        :type TimeSpan: int\n        :param ZoneId: 实例所属的可用区ID，例如100003。该参数可以通过调用 [DescribeZones](https://cloud.tencent.com/document/api/213/15707) 的返回值中的ZoneId字段来获取。\n        :type ZoneId: int\n        :param PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>\n        :type PayMode: int\n        :param InstanceId: 实例ID。\n        :type InstanceId: str\n        :param CoreCount: 扩容的Core节点数量。\n        :type CoreCount: int\n        :param TaskCount: 扩容的Task节点数量。\n        :type TaskCount: int\n        :param Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>\n        :type Currency: str\n        :param RouterCount: 扩容的Router节点数量。\n        :type RouterCount: int\n        :param MasterCount: 扩容的Master节点数量。\n        :type MasterCount: int\n        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.ZoneId = None
        self.PayMode = None
        self.InstanceId = None
        self.CoreCount = None
        self.TaskCount = None
        self.Currency = None
        self.RouterCount = None
        self.MasterCount = None


    def _deserialize(self, params):
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.ZoneId = params.get("ZoneId")
        self.PayMode = params.get("PayMode")
        self.InstanceId = params.get("InstanceId")
        self.CoreCount = params.get("CoreCount")
        self.TaskCount = params.get("TaskCount")
        self.Currency = params.get("Currency")
        self.RouterCount = params.get("RouterCount")
        self.MasterCount = params.get("MasterCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceScaleOutInstanceResponse(AbstractModel):
    """InquiryPriceScaleOutInstance返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginalCost: str\n        :param DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiscountCost: str\n        :param Unit: 扩容的时间单位。取值范围：
<li>s：表示秒。</li>
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type Unit: str\n        :param PriceSpec: 询价的节点规格。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PriceSpec: :class:`tencentcloud.emr.v20190103.models.PriceResource`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.OriginalCost = None
        self.DiscountCost = None
        self.Unit = None
        self.PriceSpec = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalCost = params.get("OriginalCost")
        self.DiscountCost = params.get("DiscountCost")
        self.Unit = params.get("Unit")
        if params.get("PriceSpec") is not None:
            self.PriceSpec = PriceResource()
            self.PriceSpec._deserialize(params.get("PriceSpec"))
        self.RequestId = params.get("RequestId")


class InquiryPriceUpdateInstanceRequest(AbstractModel):
    """InquiryPriceUpdateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param TimeUnit: 变配的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>\n        :type TimeUnit: str\n        :param TimeSpan: 变配的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>\n        :type TimeSpan: int\n        :param UpdateSpec: 节点变配的目标配置。\n        :type UpdateSpec: :class:`tencentcloud.emr.v20190103.models.UpdateInstanceSettings`\n        :param PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>\n        :type PayMode: int\n        :param Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。\n        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`\n        :param Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>\n        :type Currency: str\n        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.UpdateSpec = None
        self.PayMode = None
        self.Placement = None
        self.Currency = None


    def _deserialize(self, params):
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        if params.get("UpdateSpec") is not None:
            self.UpdateSpec = UpdateInstanceSettings()
            self.UpdateSpec._deserialize(params.get("UpdateSpec"))
        self.PayMode = params.get("PayMode")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.Currency = params.get("Currency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceUpdateInstanceResponse(AbstractModel):
    """InquiryPriceUpdateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginalCost: float\n        :param DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiscountCost: float\n        :param TimeUnit: 变配的时间单位。取值范围：
<li>s：表示秒。</li>
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeUnit: str\n        :param TimeSpan: 变配的时长。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeSpan: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.OriginalCost = None
        self.DiscountCost = None
        self.TimeUnit = None
        self.TimeSpan = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalCost = params.get("OriginalCost")
        self.DiscountCost = params.get("DiscountCost")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.RequestId = params.get("RequestId")


class InstanceChargePrepaid(AbstractModel):
    """实例预付费参数，只有在付费类型为PREPAID时生效。

    """

    def __init__(self):
        """
        :param Period: 包年包月时间，默认为1，单位：月。
取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 24, 36, 48, 60。\n        :type Period: int\n        :param RenewFlag: 是否自动续费，默认为否。\n        :type RenewFlag: bool\n        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobFlowResource(AbstractModel):
    """机器资源描述。

    """

    def __init__(self):
        """
        :param Spec: 机器类型描述。\n        :type Spec: str\n        :param InstanceType: 机器类型描述，可参考CVM的该含义。\n        :type InstanceType: str\n        :param Tags: 标签KV对。\n        :type Tags: list of Tag\n        :param DiskGroups: 磁盘描述列表。\n        :type DiskGroups: list of DiskGroup\n        """
        self.Spec = None
        self.InstanceType = None
        self.Tags = None
        self.DiskGroups = None


    def _deserialize(self, params):
        self.Spec = params.get("Spec")
        self.InstanceType = params.get("InstanceType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("DiskGroups") is not None:
            self.DiskGroups = []
            for item in params.get("DiskGroups"):
                obj = DiskGroup()
                obj._deserialize(item)
                self.DiskGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobFlowResourceSpec(AbstractModel):
    """流程作业资源描述

    """

    def __init__(self):
        """
        :param MasterCount: 主节点数量。\n        :type MasterCount: int\n        :param MasterResourceSpec: 主节点配置。\n        :type MasterResourceSpec: :class:`tencentcloud.emr.v20190103.models.JobFlowResource`\n        :param CoreCount: Core节点数量\n        :type CoreCount: int\n        :param CoreResourceSpec: Core节点配置。\n        :type CoreResourceSpec: :class:`tencentcloud.emr.v20190103.models.JobFlowResource`\n        :param TaskCount: Task节点数量。\n        :type TaskCount: int\n        :param CommonCount: Common节点数量。\n        :type CommonCount: int\n        :param TaskResourceSpec: Task节点配置。\n        :type TaskResourceSpec: :class:`tencentcloud.emr.v20190103.models.JobFlowResource`\n        :param CommonResourceSpec: Common节点配置。\n        :type CommonResourceSpec: :class:`tencentcloud.emr.v20190103.models.JobFlowResource`\n        """
        self.MasterCount = None
        self.MasterResourceSpec = None
        self.CoreCount = None
        self.CoreResourceSpec = None
        self.TaskCount = None
        self.CommonCount = None
        self.TaskResourceSpec = None
        self.CommonResourceSpec = None


    def _deserialize(self, params):
        self.MasterCount = params.get("MasterCount")
        if params.get("MasterResourceSpec") is not None:
            self.MasterResourceSpec = JobFlowResource()
            self.MasterResourceSpec._deserialize(params.get("MasterResourceSpec"))
        self.CoreCount = params.get("CoreCount")
        if params.get("CoreResourceSpec") is not None:
            self.CoreResourceSpec = JobFlowResource()
            self.CoreResourceSpec._deserialize(params.get("CoreResourceSpec"))
        self.TaskCount = params.get("TaskCount")
        self.CommonCount = params.get("CommonCount")
        if params.get("TaskResourceSpec") is not None:
            self.TaskResourceSpec = JobFlowResource()
            self.TaskResourceSpec._deserialize(params.get("TaskResourceSpec"))
        if params.get("CommonResourceSpec") is not None:
            self.CommonResourceSpec = JobFlowResource()
            self.CommonResourceSpec._deserialize(params.get("CommonResourceSpec"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobResult(AbstractModel):
    """任务步骤结果描述

    """

    def __init__(self):
        """
        :param Name: 任务步骤名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param ActionOnFailure: 任务步骤失败时的处理策略，可以为以下值：
"CONTINUE"，跳过当前失败步骤，继续后续步骤。
“TERMINATE_CLUSTER”，终止当前及后续步骤，并销毁集群。
“CANCEL_AND_WAIT”，取消当前步骤并阻塞等待处理。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActionOnFailure: str\n        :param JobState: 当前步骤的状态，可以为以下值：
“JobFlowStepStatusInit”，初始化状态，等待执行。
“JobFlowStepStatusRunning”，任务步骤正在执行。
“JobFlowStepStatusFailed”，任务步骤执行失败。
“JobFlowStepStatusSucceed”，任务步骤执行成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type JobState: str\n        """
        self.Name = None
        self.ActionOnFailure = None
        self.JobState = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ActionOnFailure = params.get("ActionOnFailure")
        self.JobState = params.get("JobState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginSettings(AbstractModel):
    """登录设置

    """

    def __init__(self):
        """
        :param Password: Password\n        :type Password: str\n        :param PublicKeyId: Public Key\n        :type PublicKeyId: str\n        """
        self.Password = None
        self.PublicKeyId = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.PublicKeyId = params.get("PublicKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetaDbInfo(AbstractModel):
    """元数据库信息

    """

    def __init__(self):
        """
        :param MetaType: 元数据类型。\n        :type MetaType: str\n        :param UnifyMetaInstanceId: 统一元数据库实例ID。\n        :type UnifyMetaInstanceId: str\n        :param MetaDBInfo: 自建元数据库信息。\n        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`\n        """
        self.MetaType = None
        self.UnifyMetaInstanceId = None
        self.MetaDBInfo = None


    def _deserialize(self, params):
        self.MetaType = params.get("MetaType")
        self.UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        if params.get("MetaDBInfo") is not None:
            self.MetaDBInfo = CustomMetaInfo()
            self.MetaDBInfo._deserialize(params.get("MetaDBInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiDisk(AbstractModel):
    """多云盘参数

    """

    def __init__(self):
        """
        :param DiskType: 云盘类型
<li>CLOUD_SSD：表示云SSD。</li>
<li>CLOUD_PREMIUM：表示高效云盘。</li>
<li>CLOUD_HSSD：表示增强型SSD云硬盘。</li>\n        :type DiskType: str\n        :param Volume: 云盘大小\n        :type Volume: int\n        :param Count: 该类型云盘个数\n        :type Count: int\n        """
        self.DiskType = None
        self.Volume = None
        self.Count = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.Volume = params.get("Volume")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiDiskMC(AbstractModel):
    """多云盘参数

    """

    def __init__(self):
        """
        :param Count: 该类型云盘个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Count: int\n        :param Type: 磁盘类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: int\n        :param Volume: 云盘大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type Volume: int\n        """
        self.Count = None
        self.Type = None
        self.Volume = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Type = params.get("Type")
        self.Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewResourceSpec(AbstractModel):
    """资源描述

    """

    def __init__(self):
        """
        :param MasterResourceSpec: 描述Master节点资源\n        :type MasterResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`\n        :param CoreResourceSpec: 描述Core节点资源\n        :type CoreResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`\n        :param TaskResourceSpec: 描述Task节点资源\n        :type TaskResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`\n        :param MasterCount: Master节点数量\n        :type MasterCount: int\n        :param CoreCount: Core节点数量\n        :type CoreCount: int\n        :param TaskCount: Task节点数量\n        :type TaskCount: int\n        :param CommonResourceSpec: 描述Common节点资源\n        :type CommonResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`\n        :param CommonCount: Common节点数量\n        :type CommonCount: int\n        """
        self.MasterResourceSpec = None
        self.CoreResourceSpec = None
        self.TaskResourceSpec = None
        self.MasterCount = None
        self.CoreCount = None
        self.TaskCount = None
        self.CommonResourceSpec = None
        self.CommonCount = None


    def _deserialize(self, params):
        if params.get("MasterResourceSpec") is not None:
            self.MasterResourceSpec = Resource()
            self.MasterResourceSpec._deserialize(params.get("MasterResourceSpec"))
        if params.get("CoreResourceSpec") is not None:
            self.CoreResourceSpec = Resource()
            self.CoreResourceSpec._deserialize(params.get("CoreResourceSpec"))
        if params.get("TaskResourceSpec") is not None:
            self.TaskResourceSpec = Resource()
            self.TaskResourceSpec._deserialize(params.get("TaskResourceSpec"))
        self.MasterCount = params.get("MasterCount")
        self.CoreCount = params.get("CoreCount")
        self.TaskCount = params.get("TaskCount")
        if params.get("CommonResourceSpec") is not None:
            self.CommonResourceSpec = Resource()
            self.CommonResourceSpec._deserialize(params.get("CommonResourceSpec"))
        self.CommonCount = params.get("CommonCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeHardwareInfo(AbstractModel):
    """节点硬件信息

    """

    def __init__(self):
        """
        :param AppId: 用户APPID
注意：此字段可能返回 null，表示取不到有效值。\n        :type AppId: int\n        :param SerialNo: 序列号
注意：此字段可能返回 null，表示取不到有效值。\n        :type SerialNo: str\n        :param OrderNo: 机器实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type OrderNo: str\n        :param WanIp: master节点绑定外网IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type WanIp: str\n        :param Flag: 节点类型。0:common节点；1:master节点
；2:core节点；3:task节点
注意：此字段可能返回 null，表示取不到有效值。\n        :type Flag: int\n        :param Spec: 节点规格
注意：此字段可能返回 null，表示取不到有效值。\n        :type Spec: str\n        :param CpuNum: 节点核数
注意：此字段可能返回 null，表示取不到有效值。\n        :type CpuNum: int\n        :param MemSize: 节点内存
注意：此字段可能返回 null，表示取不到有效值。\n        :type MemSize: int\n        :param MemDesc: 节点内存描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type MemDesc: str\n        :param RegionId: 节点所在region
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegionId: int\n        :param ZoneId: 节点所在Zone
注意：此字段可能返回 null，表示取不到有效值。\n        :type ZoneId: int\n        :param ApplyTime: 申请时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplyTime: str\n        :param FreeTime: 释放时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type FreeTime: str\n        :param DiskSize: 硬盘大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskSize: str\n        :param NameTag: 节点描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type NameTag: str\n        :param Services: 节点部署服务
注意：此字段可能返回 null，表示取不到有效值。\n        :type Services: str\n        :param StorageType: 磁盘类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type StorageType: int\n        :param RootSize: 系统盘大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type RootSize: int\n        :param ChargeType: 付费类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ChargeType: int\n        :param CdbIp: 数据库IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type CdbIp: str\n        :param CdbPort: 数据库端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type CdbPort: int\n        :param HwDiskSize: 硬盘容量
注意：此字段可能返回 null，表示取不到有效值。\n        :type HwDiskSize: int\n        :param HwDiskSizeDesc: 硬盘容量描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type HwDiskSizeDesc: str\n        :param HwMemSize: 内存容量
注意：此字段可能返回 null，表示取不到有效值。\n        :type HwMemSize: int\n        :param HwMemSizeDesc: 内存容量描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type HwMemSizeDesc: str\n        :param ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExpireTime: str\n        :param EmrResourceId: 节点资源ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type EmrResourceId: str\n        :param IsAutoRenew: 续费标志
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsAutoRenew: int\n        :param DeviceClass: 设备标识
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeviceClass: str\n        :param Mutable: 支持变配
注意：此字段可能返回 null，表示取不到有效值。\n        :type Mutable: int\n        :param MCMultiDisk: 多云盘
注意：此字段可能返回 null，表示取不到有效值。\n        :type MCMultiDisk: list of MultiDiskMC\n        :param CdbNodeInfo: 数据库信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type CdbNodeInfo: :class:`tencentcloud.emr.v20190103.models.CdbInfo`\n        :param Ip: 内网IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ip: str\n        :param Destroyable: 此节点是否可销毁，1可销毁，0不可销毁
注意：此字段可能返回 null，表示取不到有效值。\n        :type Destroyable: int\n        :param Tags: 节点绑定的标签
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        :param AutoFlag: 是否是自动扩缩容节点，0为普通节点，1为自动扩缩容节点。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AutoFlag: int\n        :param HardwareResourceType: 资源类型, host/pod
注意：此字段可能返回 null，表示取不到有效值。\n        :type HardwareResourceType: str\n        :param IsDynamicSpec: 是否浮动规格，1是，0否
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsDynamicSpec: int\n        :param DynamicPodSpec: 浮动规格值json字符串
注意：此字段可能返回 null，表示取不到有效值。\n        :type DynamicPodSpec: str\n        :param SupportModifyPayMode: 是否支持变更计费类型 1是，0否
注意：此字段可能返回 null，表示取不到有效值。\n        :type SupportModifyPayMode: int\n        """
        self.AppId = None
        self.SerialNo = None
        self.OrderNo = None
        self.WanIp = None
        self.Flag = None
        self.Spec = None
        self.CpuNum = None
        self.MemSize = None
        self.MemDesc = None
        self.RegionId = None
        self.ZoneId = None
        self.ApplyTime = None
        self.FreeTime = None
        self.DiskSize = None
        self.NameTag = None
        self.Services = None
        self.StorageType = None
        self.RootSize = None
        self.ChargeType = None
        self.CdbIp = None
        self.CdbPort = None
        self.HwDiskSize = None
        self.HwDiskSizeDesc = None
        self.HwMemSize = None
        self.HwMemSizeDesc = None
        self.ExpireTime = None
        self.EmrResourceId = None
        self.IsAutoRenew = None
        self.DeviceClass = None
        self.Mutable = None
        self.MCMultiDisk = None
        self.CdbNodeInfo = None
        self.Ip = None
        self.Destroyable = None
        self.Tags = None
        self.AutoFlag = None
        self.HardwareResourceType = None
        self.IsDynamicSpec = None
        self.DynamicPodSpec = None
        self.SupportModifyPayMode = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.SerialNo = params.get("SerialNo")
        self.OrderNo = params.get("OrderNo")
        self.WanIp = params.get("WanIp")
        self.Flag = params.get("Flag")
        self.Spec = params.get("Spec")
        self.CpuNum = params.get("CpuNum")
        self.MemSize = params.get("MemSize")
        self.MemDesc = params.get("MemDesc")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.ApplyTime = params.get("ApplyTime")
        self.FreeTime = params.get("FreeTime")
        self.DiskSize = params.get("DiskSize")
        self.NameTag = params.get("NameTag")
        self.Services = params.get("Services")
        self.StorageType = params.get("StorageType")
        self.RootSize = params.get("RootSize")
        self.ChargeType = params.get("ChargeType")
        self.CdbIp = params.get("CdbIp")
        self.CdbPort = params.get("CdbPort")
        self.HwDiskSize = params.get("HwDiskSize")
        self.HwDiskSizeDesc = params.get("HwDiskSizeDesc")
        self.HwMemSize = params.get("HwMemSize")
        self.HwMemSizeDesc = params.get("HwMemSizeDesc")
        self.ExpireTime = params.get("ExpireTime")
        self.EmrResourceId = params.get("EmrResourceId")
        self.IsAutoRenew = params.get("IsAutoRenew")
        self.DeviceClass = params.get("DeviceClass")
        self.Mutable = params.get("Mutable")
        if params.get("MCMultiDisk") is not None:
            self.MCMultiDisk = []
            for item in params.get("MCMultiDisk"):
                obj = MultiDiskMC()
                obj._deserialize(item)
                self.MCMultiDisk.append(obj)
        if params.get("CdbNodeInfo") is not None:
            self.CdbNodeInfo = CdbInfo()
            self.CdbNodeInfo._deserialize(params.get("CdbNodeInfo"))
        self.Ip = params.get("Ip")
        self.Destroyable = params.get("Destroyable")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoFlag = params.get("AutoFlag")
        self.HardwareResourceType = params.get("HardwareResourceType")
        self.IsDynamicSpec = params.get("IsDynamicSpec")
        self.DynamicPodSpec = params.get("DynamicPodSpec")
        self.SupportModifyPayMode = params.get("SupportModifyPayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutterResource(AbstractModel):
    """资源详情

    """

    def __init__(self):
        """
        :param Spec: 规格
注意：此字段可能返回 null，表示取不到有效值。\n        :type Spec: str\n        :param SpecName: 规格名
注意：此字段可能返回 null，表示取不到有效值。\n        :type SpecName: str\n        :param StorageType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type StorageType: int\n        :param DiskType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskType: str\n        :param RootSize: 系统盘大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type RootSize: int\n        :param MemSize: 内存大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type MemSize: int\n        :param Cpu: CPU个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cpu: int\n        :param DiskSize: 硬盘大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskSize: int\n        :param InstanceType: 规格
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceType: str\n        """
        self.Spec = None
        self.SpecName = None
        self.StorageType = None
        self.DiskType = None
        self.RootSize = None
        self.MemSize = None
        self.Cpu = None
        self.DiskSize = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Spec = params.get("Spec")
        self.SpecName = params.get("SpecName")
        self.StorageType = params.get("StorageType")
        self.DiskType = params.get("DiskType")
        self.RootSize = params.get("RootSize")
        self.MemSize = params.get("MemSize")
        self.Cpu = params.get("Cpu")
        self.DiskSize = params.get("DiskSize")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersistentVolumeContext(AbstractModel):
    """Pod PVC存储方式描述

    """

    def __init__(self):
        """
        :param DiskSize: 磁盘大小，单位为GB。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskSize: int\n        :param DiskType: 磁盘类型。CLOUD_PREMIUM;CLOUD_SSD
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskType: str\n        :param DiskNum: 磁盘数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskNum: int\n        """
        self.DiskSize = None
        self.DiskType = None
        self.DiskNum = None


    def _deserialize(self, params):
        self.DiskSize = params.get("DiskSize")
        self.DiskType = params.get("DiskType")
        self.DiskNum = params.get("DiskNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Placement(AbstractModel):
    """描述集群实例位置信息

    """

    def __init__(self):
        """
        :param ProjectId: 实例所属项目ID。该参数可以通过调用 DescribeProject 的返回值中的 projectId 字段来获取。填0为默认项目。\n        :type ProjectId: int\n        :param Zone: 实例所属的可用区，例如ap-guangzhou-1。该参数也可以通过调用 DescribeZones 的返回值中的Zone字段来获取。\n        :type Zone: str\n        """
        self.ProjectId = None
        self.Zone = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodParameter(AbstractModel):
    """POD自定义权限和自定义参数

    """

    def __init__(self):
        """
        :param ClusterId: TKE或EKS集群ID\n        :type ClusterId: str\n        :param Config: 自定义权限
如：
{
  "apiVersion": "v1",
  "clusters": [
    {
      "cluster": {
        "certificate-authority-data": "xxxxxx==",
        "server": "https://xxxxx.com"
      },
      "name": "cls-xxxxx"
    }
  ],
  "contexts": [
    {
      "context": {
        "cluster": "cls-xxxxx",
        "user": "100014xxxxx"
      },
      "name": "cls-a44yhcxxxxxxxxxx"
    }
  ],
  "current-context": "cls-a4xxxx-context-default",
  "kind": "Config",
  "preferences": {},
  "users": [
    {
      "name": "100014xxxxx",
      "user": {
        "client-certificate-data": "xxxxxx",
        "client-key-data": "xxxxxx"
      }
    }
  ]
}\n        :type Config: str\n        :param Parameter: 自定义参数
如：
{
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
      "name": "test-deployment",
      "labels": {
        "app": "test"
      }
    },
    "spec": {
      "replicas": 3,
      "selector": {
        "matchLabels": {
          "app": "test-app"
        }
      },
      "template": {
        "metadata": {
          "annotations": {
            "your-organization.com/department-v1": "test-example-v1",
            "your-organization.com/department-v2": "test-example-v2"
          },
          "labels": {
            "app": "test-app",
            "environment": "production"
          }
        },
        "spec": {
          "nodeSelector": {
            "your-organization/node-test": "test-node"
          },
          "containers": [
            {
              "name": "nginx",
              "image": "nginx:1.14.2",
              "ports": [
                {
                  "containerPort": 80
                }
              ]
            }
          ],
          "affinity": {
            "nodeAffinity": {
              "requiredDuringSchedulingIgnoredDuringExecution": {
                "nodeSelectorTerms": [
                  {
                    "matchExpressions": [
                      {
                        "key": "disk-type",
                        "operator": "In",
                        "values": [
                          "ssd",
                          "sas"
                        ]
                      },
                      {
                        "key": "cpu-num",
                        "operator": "Gt",
                        "values": [
                          "6"
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          }
        }
      }
    }
  }\n        :type Parameter: str\n        """
        self.ClusterId = None
        self.Config = None
        self.Parameter = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Config = params.get("Config")
        self.Parameter = params.get("Parameter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodSaleSpec(AbstractModel):
    """Pod资源售卖规格

    """

    def __init__(self):
        """
        :param NodeType: 可售卖的资源规格，仅为以下值:"TASK","CORE","MASTER","ROUTER"。\n        :type NodeType: str\n        :param Cpu: Cpu核数。\n        :type Cpu: int\n        :param Memory: 内存数量，单位为GB。\n        :type Memory: int\n        :param Number: 该规格资源可申请的最大数量。\n        :type Number: int\n        """
        self.NodeType = None
        self.Cpu = None
        self.Memory = None
        self.Number = None


    def _deserialize(self, params):
        self.NodeType = params.get("NodeType")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodSpec(AbstractModel):
    """扩容容器资源时的资源描述

    """

    def __init__(self):
        """
        :param ResourceProviderIdentifier: 外部资源提供者的标识符，例如"cls-a1cd23fa"。\n        :type ResourceProviderIdentifier: str\n        :param ResourceProviderType: 外部资源提供者类型，例如"tke",当前仅支持"tke"。\n        :type ResourceProviderType: str\n        :param NodeType: 资源的用途，即节点类型，当前仅支持"TASK"。\n        :type NodeType: str\n        :param Cpu: CPU核数。\n        :type Cpu: int\n        :param Memory: 内存大小，单位为GB。\n        :type Memory: int\n        :param DataVolumes: 资源对宿主机的挂载点，指定的挂载点对应了宿主机的路径，该挂载点在Pod中作为数据存储目录使用。弃用\n        :type DataVolumes: list of str\n        :param CpuType: Eks集群-CPU类型，当前支持"intel"和"amd"\n        :type CpuType: str\n        :param PodVolumes: Pod节点数据目录挂载信息。\n        :type PodVolumes: list of PodVolume\n        :param IsDynamicSpec: 是否浮动规格，1是，0否\n        :type IsDynamicSpec: int\n        :param DynamicPodSpec: 浮动规格
注意：此字段可能返回 null，表示取不到有效值。\n        :type DynamicPodSpec: :class:`tencentcloud.emr.v20190103.models.DynamicPodSpec`\n        :param VpcId: 代表vpc网络唯一id
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcId: str\n        :param SubnetId: 代表vpc子网唯一id
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetId: str\n        """
        self.ResourceProviderIdentifier = None
        self.ResourceProviderType = None
        self.NodeType = None
        self.Cpu = None
        self.Memory = None
        self.DataVolumes = None
        self.CpuType = None
        self.PodVolumes = None
        self.IsDynamicSpec = None
        self.DynamicPodSpec = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.ResourceProviderIdentifier = params.get("ResourceProviderIdentifier")
        self.ResourceProviderType = params.get("ResourceProviderType")
        self.NodeType = params.get("NodeType")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.DataVolumes = params.get("DataVolumes")
        self.CpuType = params.get("CpuType")
        if params.get("PodVolumes") is not None:
            self.PodVolumes = []
            for item in params.get("PodVolumes"):
                obj = PodVolume()
                obj._deserialize(item)
                self.PodVolumes.append(obj)
        self.IsDynamicSpec = params.get("IsDynamicSpec")
        if params.get("DynamicPodSpec") is not None:
            self.DynamicPodSpec = DynamicPodSpec()
            self.DynamicPodSpec._deserialize(params.get("DynamicPodSpec"))
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodState(AbstractModel):
    """单个pod状态

    """

    def __init__(self):
        """
        :param Name: pod的名称\n        :type Name: str\n        :param Uuid: pod uuid\n        :type Uuid: str\n        :param State: pod的状态\n        :type State: str\n        :param Reason: pod处于该状态原因\n        :type Reason: str\n        :param OwnerCluster: pod所属集群\n        :type OwnerCluster: str\n        :param Memory: pod内存大小\n        :type Memory: int\n        """
        self.Name = None
        self.Uuid = None
        self.State = None
        self.Reason = None
        self.OwnerCluster = None
        self.Memory = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Uuid = params.get("Uuid")
        self.State = params.get("State")
        self.Reason = params.get("Reason")
        self.OwnerCluster = params.get("OwnerCluster")
        self.Memory = params.get("Memory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodVolume(AbstractModel):
    """Pod的存储设备描述信息。

    """

    def __init__(self):
        """
        :param VolumeType: 存储类型，可为"pvc"，"hostpath"。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VolumeType: str\n        :param PVCVolume: 当VolumeType为"pvc"时，该字段生效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PVCVolume: :class:`tencentcloud.emr.v20190103.models.PersistentVolumeContext`\n        :param HostVolume: 当VolumeType为"hostpath"时，该字段生效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type HostVolume: :class:`tencentcloud.emr.v20190103.models.HostVolumeContext`\n        """
        self.VolumeType = None
        self.PVCVolume = None
        self.HostVolume = None


    def _deserialize(self, params):
        self.VolumeType = params.get("VolumeType")
        if params.get("PVCVolume") is not None:
            self.PVCVolume = PersistentVolumeContext()
            self.PVCVolume._deserialize(params.get("PVCVolume"))
        if params.get("HostVolume") is not None:
            self.HostVolume = HostVolumeContext()
            self.HostVolume._deserialize(params.get("HostVolume"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreExecuteFileSettings(AbstractModel):
    """预执行脚本配置

    """

    def __init__(self):
        """
        :param Path: 脚本在COS上路径，已废弃\n        :type Path: str\n        :param Args: 执行脚本参数\n        :type Args: list of str\n        :param Bucket: COS的Bucket名称，已废弃\n        :type Bucket: str\n        :param Region: COS的Region名称，已废弃\n        :type Region: str\n        :param Domain: COS的Domain数据，已废弃\n        :type Domain: str\n        :param RunOrder: 执行顺序\n        :type RunOrder: int\n        :param WhenRun: resourceAfter 或 clusterAfter\n        :type WhenRun: str\n        :param CosFileName: 脚本文件名，已废弃\n        :type CosFileName: str\n        :param CosFileURI: 脚本的cos地址\n        :type CosFileURI: str\n        :param CosSecretId: cos的SecretId\n        :type CosSecretId: str\n        :param CosSecretKey: Cos的SecretKey\n        :type CosSecretKey: str\n        :param AppId: cos的appid，已废弃\n        :type AppId: str\n        """
        self.Path = None
        self.Args = None
        self.Bucket = None
        self.Region = None
        self.Domain = None
        self.RunOrder = None
        self.WhenRun = None
        self.CosFileName = None
        self.CosFileURI = None
        self.CosSecretId = None
        self.CosSecretKey = None
        self.AppId = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Args = params.get("Args")
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Domain = params.get("Domain")
        self.RunOrder = params.get("RunOrder")
        self.WhenRun = params.get("WhenRun")
        self.CosFileName = params.get("CosFileName")
        self.CosFileURI = params.get("CosFileURI")
        self.CosSecretId = params.get("CosSecretId")
        self.CosSecretKey = params.get("CosSecretKey")
        self.AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PriceResource(AbstractModel):
    """询价资源

    """

    def __init__(self):
        """
        :param Spec: 需要的规格
注意：此字段可能返回 null，表示取不到有效值。\n        :type Spec: str\n        :param StorageType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type StorageType: int\n        :param DiskType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskType: str\n        :param RootSize: 系统盘大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type RootSize: int\n        :param MemSize: 内存大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type MemSize: int\n        :param Cpu: 核心数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cpu: int\n        :param DiskSize: 硬盘大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskSize: int\n        :param MultiDisks: 云盘列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type MultiDisks: list of MultiDisk\n        :param DiskCnt: 磁盘数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskCnt: int\n        :param InstanceType: 规格
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceType: str\n        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        :param DiskNum: 磁盘数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskNum: int\n        :param LocalDiskNum: 本地盘的数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type LocalDiskNum: int\n        """
        self.Spec = None
        self.StorageType = None
        self.DiskType = None
        self.RootSize = None
        self.MemSize = None
        self.Cpu = None
        self.DiskSize = None
        self.MultiDisks = None
        self.DiskCnt = None
        self.InstanceType = None
        self.Tags = None
        self.DiskNum = None
        self.LocalDiskNum = None


    def _deserialize(self, params):
        self.Spec = params.get("Spec")
        self.StorageType = params.get("StorageType")
        self.DiskType = params.get("DiskType")
        self.RootSize = params.get("RootSize")
        self.MemSize = params.get("MemSize")
        self.Cpu = params.get("Cpu")
        self.DiskSize = params.get("DiskSize")
        if params.get("MultiDisks") is not None:
            self.MultiDisks = []
            for item in params.get("MultiDisks"):
                obj = MultiDisk()
                obj._deserialize(item)
                self.MultiDisks.append(obj)
        self.DiskCnt = params.get("DiskCnt")
        self.InstanceType = params.get("InstanceType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DiskNum = params.get("DiskNum")
        self.LocalDiskNum = params.get("LocalDiskNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuotaEntity(AbstractModel):
    """获取CVM配额

    """

    def __init__(self):
        """
        :param UsedQuota: 已使用配额
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsedQuota: int\n        :param RemainingQuota: 剩余配额
注意：此字段可能返回 null，表示取不到有效值。\n        :type RemainingQuota: int\n        :param TotalQuota: 总配额
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalQuota: int\n        :param Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。\n        :type Zone: str\n        """
        self.UsedQuota = None
        self.RemainingQuota = None
        self.TotalQuota = None
        self.Zone = None


    def _deserialize(self, params):
        self.UsedQuota = params.get("UsedQuota")
        self.RemainingQuota = params.get("RemainingQuota")
        self.TotalQuota = params.get("TotalQuota")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstancesInfo(AbstractModel):
    """集群续费实例信息

    """

    def __init__(self):
        """
        :param EmrResourceId: 节点资源ID\n        :type EmrResourceId: str\n        :param Flag: 节点类型。0:common节点；1:master节点
；2:core节点；3:task节点\n        :type Flag: int\n        :param Ip: 内网IP\n        :type Ip: str\n        :param MemDesc: 节点内存描述\n        :type MemDesc: str\n        :param CpuNum: 节点核数\n        :type CpuNum: int\n        :param DiskSize: 硬盘大小\n        :type DiskSize: str\n        :param ExpireTime: 过期时间\n        :type ExpireTime: str\n        :param Spec: 节点规格\n        :type Spec: str\n        :param StorageType: 磁盘类型\n        :type StorageType: int\n        """
        self.EmrResourceId = None
        self.Flag = None
        self.Ip = None
        self.MemDesc = None
        self.CpuNum = None
        self.DiskSize = None
        self.ExpireTime = None
        self.Spec = None
        self.StorageType = None


    def _deserialize(self, params):
        self.EmrResourceId = params.get("EmrResourceId")
        self.Flag = params.get("Flag")
        self.Ip = params.get("Ip")
        self.MemDesc = params.get("MemDesc")
        self.CpuNum = params.get("CpuNum")
        self.DiskSize = params.get("DiskSize")
        self.ExpireTime = params.get("ExpireTime")
        self.Spec = params.get("Spec")
        self.StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Resource(AbstractModel):
    """资源详情

    """

    def __init__(self):
        """
        :param Spec: 节点规格描述，如CVM.SA2。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Spec: str\n        :param StorageType: 存储类型
取值范围：
<li>4：表示云SSD。</li>
<li>5：表示高效云盘。</li>
<li>6：表示增强型SSD云硬盘。</li>
<li>11：表示吞吐型云硬盘。</li>
<li>12：表示极速型SSD云硬盘。</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type StorageType: int\n        :param DiskType: 磁盘类型
取值范围：
<li>CLOUD_SSD：表示云SSD。</li>
<li>CLOUD_PREMIUM：表示高效云盘。</li>
<li>CLOUD_BASIC：表示云硬盘。</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskType: str\n        :param MemSize: 内存容量,单位为M
注意：此字段可能返回 null，表示取不到有效值。\n        :type MemSize: int\n        :param Cpu: CPU核数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cpu: int\n        :param DiskSize: 数据盘容量
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskSize: int\n        :param RootSize: 系统盘容量
注意：此字段可能返回 null，表示取不到有效值。\n        :type RootSize: int\n        :param MultiDisks: 云盘列表，当数据盘为一块云盘时，直接使用DiskType和DiskSize参数，超出部分使用MultiDisks
注意：此字段可能返回 null，表示取不到有效值。\n        :type MultiDisks: list of MultiDisk\n        :param Tags: 需要绑定的标签列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        :param InstanceType: 规格类型，如S2.MEDIUM8
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceType: str\n        :param LocalDiskNum: 本地盘数量，该字段已废弃
注意：此字段可能返回 null，表示取不到有效值。\n        :type LocalDiskNum: int\n        :param DiskNum: 本地盘数量，如2
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskNum: int\n        """
        self.Spec = None
        self.StorageType = None
        self.DiskType = None
        self.MemSize = None
        self.Cpu = None
        self.DiskSize = None
        self.RootSize = None
        self.MultiDisks = None
        self.Tags = None
        self.InstanceType = None
        self.LocalDiskNum = None
        self.DiskNum = None


    def _deserialize(self, params):
        self.Spec = params.get("Spec")
        self.StorageType = params.get("StorageType")
        self.DiskType = params.get("DiskType")
        self.MemSize = params.get("MemSize")
        self.Cpu = params.get("Cpu")
        self.DiskSize = params.get("DiskSize")
        self.RootSize = params.get("RootSize")
        if params.get("MultiDisks") is not None:
            self.MultiDisks = []
            for item in params.get("MultiDisks"):
                obj = MultiDisk()
                obj._deserialize(item)
                self.MultiDisks.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceType = params.get("InstanceType")
        self.LocalDiskNum = params.get("LocalDiskNum")
        self.DiskNum = params.get("DiskNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunJobFlowRequest(AbstractModel):
    """RunJobFlow请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 作业名称。\n        :type Name: str\n        :param CreateCluster: 是否新创建集群。
true，新创建集群，则使用Instance中的参数进行集群创建。
false，使用已有集群，则通过InstanceId传入。\n        :type CreateCluster: bool\n        :param Steps: 作业流程执行步骤。\n        :type Steps: list of Step\n        :param InstancePolicy: 作业流程正常完成时，集群的处理方式，可选择:
Terminate 销毁集群。
Reserve 保留集群。\n        :type InstancePolicy: str\n        :param ProductVersion: 只有CreateCluster为true时生效，目前只支持EMR版本，例如EMR-2.2.0，不支持ClickHouse和Druid版本。\n        :type ProductVersion: str\n        :param SecurityClusterFlag: 只在CreateCluster为true时生效。
true 表示安装kerberos，false表示不安装kerberos。\n        :type SecurityClusterFlag: bool\n        :param Software: 只在CreateCluster为true时生效。
新建集群时，要安装的软件列表。\n        :type Software: list of str\n        :param BootstrapActions: 引导脚本。\n        :type BootstrapActions: list of BootstrapAction\n        :param Configurations: 指定配置创建集群。\n        :type Configurations: list of Configuration\n        :param LogUri: 作业日志保存地址。\n        :type LogUri: str\n        :param InstanceId: 只在CreateCluster为false时生效。\n        :type InstanceId: str\n        :param ApplicationRole: 自定义应用角色，大数据应用访问外部服务时使用的角色，默认为"EME_QCSRole"。\n        :type ApplicationRole: str\n        :param ClientToken: 重入标签，用来可重入检查，防止在一段时间内，创建相同的流程作业。\n        :type ClientToken: str\n        :param Instance: 只在CreateCluster为true时生效，使用该配置创建集群。\n        :type Instance: :class:`tencentcloud.emr.v20190103.models.ClusterSetting`\n        """
        self.Name = None
        self.CreateCluster = None
        self.Steps = None
        self.InstancePolicy = None
        self.ProductVersion = None
        self.SecurityClusterFlag = None
        self.Software = None
        self.BootstrapActions = None
        self.Configurations = None
        self.LogUri = None
        self.InstanceId = None
        self.ApplicationRole = None
        self.ClientToken = None
        self.Instance = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CreateCluster = params.get("CreateCluster")
        if params.get("Steps") is not None:
            self.Steps = []
            for item in params.get("Steps"):
                obj = Step()
                obj._deserialize(item)
                self.Steps.append(obj)
        self.InstancePolicy = params.get("InstancePolicy")
        self.ProductVersion = params.get("ProductVersion")
        self.SecurityClusterFlag = params.get("SecurityClusterFlag")
        self.Software = params.get("Software")
        if params.get("BootstrapActions") is not None:
            self.BootstrapActions = []
            for item in params.get("BootstrapActions"):
                obj = BootstrapAction()
                obj._deserialize(item)
                self.BootstrapActions.append(obj)
        if params.get("Configurations") is not None:
            self.Configurations = []
            for item in params.get("Configurations"):
                obj = Configuration()
                obj._deserialize(item)
                self.Configurations.append(obj)
        self.LogUri = params.get("LogUri")
        self.InstanceId = params.get("InstanceId")
        self.ApplicationRole = params.get("ApplicationRole")
        self.ClientToken = params.get("ClientToken")
        if params.get("Instance") is not None:
            self.Instance = ClusterSetting()
            self.Instance._deserialize(params.get("Instance"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunJobFlowResponse(AbstractModel):
    """RunJobFlow返回参数结构体

    """

    def __init__(self):
        """
        :param JobFlowId: 作业流程ID。\n        :type JobFlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.JobFlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobFlowId = params.get("JobFlowId")
        self.RequestId = params.get("RequestId")


class ScaleOutInstanceRequest(AbstractModel):
    """ScaleOutInstance请求参数结构体

    """

    def __init__(self):
        """
        :param TimeUnit: 扩容的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>\n        :type TimeUnit: str\n        :param TimeSpan: 扩容的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>\n        :type TimeSpan: int\n        :param InstanceId: 实例ID。\n        :type InstanceId: str\n        :param PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>\n        :type PayMode: int\n        :param ClientToken: 客户端Token。\n        :type ClientToken: str\n        :param PreExecutedFileSettings: 引导操作脚本设置。\n        :type PreExecutedFileSettings: list of PreExecuteFileSettings\n        :param TaskCount: 扩容的Task节点数量。\n        :type TaskCount: int\n        :param CoreCount: 扩容的Core节点数量。\n        :type CoreCount: int\n        :param UnNecessaryNodeList: 扩容时不需要安装的进程。\n        :type UnNecessaryNodeList: list of int non-negative\n        :param RouterCount: 扩容的Router节点数量。\n        :type RouterCount: int\n        :param SoftDeployInfo: 部署的服务。
<li>SoftDeployInfo和ServiceNodeInfo是同组参数，和UnNecessaryNodeList参数互斥。</li>
<li>建议使用SoftDeployInfo和ServiceNodeInfo组合。</li>\n        :type SoftDeployInfo: list of int non-negative\n        :param ServiceNodeInfo: 启动的进程。\n        :type ServiceNodeInfo: list of int non-negative\n        :param DisasterRecoverGroupIds: 分散置放群组ID列表，当前仅支持指定一个。\n        :type DisasterRecoverGroupIds: list of str\n        :param Tags: 扩容节点绑定标签列表。\n        :type Tags: list of Tag\n        :param HardwareResourceType: 扩容所选资源类型，可选范围为"host","pod"，host为普通的CVM资源，Pod为TKE集群或EKS集群提供的资源\n        :type HardwareResourceType: str\n        :param PodSpec: 使用Pod资源扩容时，指定的Pod规格以及来源等信息\n        :type PodSpec: :class:`tencentcloud.emr.v20190103.models.PodSpec`\n        :param ClickHouseClusterName: 使用clickhouse集群扩容时，选择的机器分组名称\n        :type ClickHouseClusterName: str\n        :param ClickHouseClusterType: 使用clickhouse集群扩容时，选择的机器分组类型。new为新增，old为选择旧分组\n        :type ClickHouseClusterType: str\n        :param YarnNodeLabel: 规则扩容指定 yarn node label\n        :type YarnNodeLabel: str\n        :param PodParameter: POD自定义权限和自定义参数\n        :type PodParameter: :class:`tencentcloud.emr.v20190103.models.PodParameter`\n        :param MasterCount: 扩容的Master节点的数量。
使用clickhouse集群扩容时，该参数不生效。
使用kafka集群扩容时，该参数不生效。
当HardwareResourceType=POD时，该参数不生效。\n        :type MasterCount: int\n        :param StartServiceAfterScaleOut: 扩容后是否启动服务，true：启动，false：不启动\n        :type StartServiceAfterScaleOut: str\n        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.InstanceId = None
        self.PayMode = None
        self.ClientToken = None
        self.PreExecutedFileSettings = None
        self.TaskCount = None
        self.CoreCount = None
        self.UnNecessaryNodeList = None
        self.RouterCount = None
        self.SoftDeployInfo = None
        self.ServiceNodeInfo = None
        self.DisasterRecoverGroupIds = None
        self.Tags = None
        self.HardwareResourceType = None
        self.PodSpec = None
        self.ClickHouseClusterName = None
        self.ClickHouseClusterType = None
        self.YarnNodeLabel = None
        self.PodParameter = None
        self.MasterCount = None
        self.StartServiceAfterScaleOut = None


    def _deserialize(self, params):
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.InstanceId = params.get("InstanceId")
        self.PayMode = params.get("PayMode")
        self.ClientToken = params.get("ClientToken")
        if params.get("PreExecutedFileSettings") is not None:
            self.PreExecutedFileSettings = []
            for item in params.get("PreExecutedFileSettings"):
                obj = PreExecuteFileSettings()
                obj._deserialize(item)
                self.PreExecutedFileSettings.append(obj)
        self.TaskCount = params.get("TaskCount")
        self.CoreCount = params.get("CoreCount")
        self.UnNecessaryNodeList = params.get("UnNecessaryNodeList")
        self.RouterCount = params.get("RouterCount")
        self.SoftDeployInfo = params.get("SoftDeployInfo")
        self.ServiceNodeInfo = params.get("ServiceNodeInfo")
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.HardwareResourceType = params.get("HardwareResourceType")
        if params.get("PodSpec") is not None:
            self.PodSpec = PodSpec()
            self.PodSpec._deserialize(params.get("PodSpec"))
        self.ClickHouseClusterName = params.get("ClickHouseClusterName")
        self.ClickHouseClusterType = params.get("ClickHouseClusterType")
        self.YarnNodeLabel = params.get("YarnNodeLabel")
        if params.get("PodParameter") is not None:
            self.PodParameter = PodParameter()
            self.PodParameter._deserialize(params.get("PodParameter"))
        self.MasterCount = params.get("MasterCount")
        self.StartServiceAfterScaleOut = params.get("StartServiceAfterScaleOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutInstanceResponse(AbstractModel):
    """ScaleOutInstance返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID。\n        :type InstanceId: str\n        :param DealNames: 订单号。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DealNames: list of str\n        :param ClientToken: 客户端Token。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientToken: str\n        :param FlowId: 扩容流程ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FlowId: int\n        :param BillId: 大订单号。
注意：此字段可能返回 null，表示取不到有效值。\n        :type BillId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.DealNames = None
        self.ClientToken = None
        self.FlowId = None
        self.BillId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DealNames = params.get("DealNames")
        self.ClientToken = params.get("ClientToken")
        self.FlowId = params.get("FlowId")
        self.BillId = params.get("BillId")
        self.RequestId = params.get("RequestId")


class SearchItem(AbstractModel):
    """搜索字段

    """

    def __init__(self):
        """
        :param SearchType: 支持搜索的类型\n        :type SearchType: str\n        :param SearchValue: 支持搜索的值\n        :type SearchValue: str\n        """
        self.SearchType = None
        self.SearchValue = None


    def _deserialize(self, params):
        self.SearchType = params.get("SearchType")
        self.SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Step(AbstractModel):
    """执行步骤

    """

    def __init__(self):
        """
        :param Name: 执行步骤名称。\n        :type Name: str\n        :param ExecutionStep: 执行动作。\n        :type ExecutionStep: :class:`tencentcloud.emr.v20190103.models.Execution`\n        :param ActionOnFailure: 执行失败策略。
1. TERMINATE_CLUSTER 执行失败时退出并销毁集群。
2. CANCEL_AND_WAIT 执行失败时阻塞等待。
3. CONTINUE 执行失败时跳过并执行后续步骤。\n        :type ActionOnFailure: str\n        :param User: 指定执行Step时的用户名，非必须，默认为hadoop。\n        :type User: str\n        """
        self.Name = None
        self.ExecutionStep = None
        self.ActionOnFailure = None
        self.User = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("ExecutionStep") is not None:
            self.ExecutionStep = Execution()
            self.ExecutionStep._deserialize(params.get("ExecutionStep"))
        self.ActionOnFailure = params.get("ActionOnFailure")
        self.User = params.get("User")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncPodStateRequest(AbstractModel):
    """SyncPodState请求参数结构体

    """

    def __init__(self):
        """
        :param Message: EmrService中pod状态信息\n        :type Message: :class:`tencentcloud.emr.v20190103.models.PodState`\n        """
        self.Message = None


    def _deserialize(self, params):
        if params.get("Message") is not None:
            self.Message = PodState()
            self.Message._deserialize(params.get("Message"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncPodStateResponse(AbstractModel):
    """SyncPodState返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        """
        :param TagKey: 标签键\n        :type TagKey: str\n        :param TagValue: 标签值\n        :type TagValue: str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstanceRequest(AbstractModel):
    """TerminateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID。\n        :type InstanceId: str\n        :param ResourceIds: 销毁节点ID。该参数为预留参数，用户无需配置。\n        :type ResourceIds: list of str\n        """
        self.InstanceId = None
        self.ResourceIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceIds = params.get("ResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstanceResponse(AbstractModel):
    """TerminateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateTasksRequest(AbstractModel):
    """TerminateTasks请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID。\n        :type InstanceId: str\n        :param ResourceIds: 待销毁节点的资源ID列表。资源ID形如：emr-vm-xxxxxxxx。有效的资源ID可通过登录[控制台](https://console.cloud.tencent.com/emr/static/hardware)查询。\n        :type ResourceIds: list of str\n        """
        self.InstanceId = None
        self.ResourceIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceIds = params.get("ResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateTasksResponse(AbstractModel):
    """TerminateTasks返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateInstanceSettings(AbstractModel):
    """变配资源规格

    """

    def __init__(self):
        """
        :param Memory: 内存容量，单位为G\n        :type Memory: int\n        :param CPUCores: CPU核数\n        :type CPUCores: int\n        :param ResourceId: 机器资源ID（EMR测资源标识）\n        :type ResourceId: str\n        :param InstanceType: 变配机器规格\n        :type InstanceType: str\n        """
        self.Memory = None
        self.CPUCores = None
        self.ResourceId = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.CPUCores = params.get("CPUCores")
        self.ResourceId = params.get("ResourceId")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VPCSettings(AbstractModel):
    """VPC 参数

    """

    def __init__(self):
        """
        :param VpcId: VPC ID\n        :type VpcId: str\n        :param SubnetId: Subnet ID\n        :type SubnetId: str\n        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        