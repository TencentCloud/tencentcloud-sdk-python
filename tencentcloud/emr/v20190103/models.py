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
        :param CosSecretId: COS SecretId
        :type CosSecretId: str
        :param CosSecretKey: COS SecrectKey
        :type CosSecretKey: str
        :param LogOnCosPath: 日志存储在COS上的路径
        :type LogOnCosPath: str
        """
        self.CosSecretId = None
        self.CosSecretKey = None
        self.LogOnCosPath = None


    def _deserialize(self, params):
        self.CosSecretId = params.get("CosSecretId")
        self.CosSecretKey = params.get("CosSecretKey")
        self.LogOnCosPath = params.get("LogOnCosPath")


class CdbInfo(AbstractModel):
    """出参

    """

    def __init__(self):
        """
        :param InstanceName: 数据库实例
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param Ip: 数据库IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param Port: 数据库端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param MemSize: 数据库内存规格
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param Volume: 数据库磁盘规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Volume: int
        :param Service: 服务标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: str
        :param ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param ApplyTime: 申请时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplyTime: str
        :param PayType: 付费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PayType: int
        :param ExpireFlag: 过期标识
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireFlag: bool
        :param Status: 数据库状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param IsAutoRenew: 续费标识
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAutoRenew: int
        :param SerialNo: 数据库字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type SerialNo: str
        :param ZoneId: ZoneId
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param RegionId: RegionId
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        """
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


class ClusterInstancesInfo(AbstractModel):
    """集群实例信息

    """

    def __init__(self):
        """
        :param Id: ID号
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param ClusterId: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param Ftitle: 标题
注意：此字段可能返回 null，表示取不到有效值。
        :type Ftitle: str
        :param ClusterName: 集群名
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param RegionId: 地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param ZoneId: 地区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param AppId: 用户APPID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param Uin: 用户UIN
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param ProjectId: 项目Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param VpcId: 集群VPCID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: int
        :param SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: int
        :param Status: 实例的状态码。取值范围：
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param AddTime: 添加时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param RunTime: 已经运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RunTime: str
        :param Config: 集群产品配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: :class:`tencentcloud.emr.v20190103.models.EmrProductConfigOutter`
        :param MasterIp: 主节点外网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterIp: str
        :param EmrVersion: EMR版本
注意：此字段可能返回 null，表示取不到有效值。
        :type EmrVersion: str
        :param ChargeType: 收费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: int
        :param TradeVersion: 交易版本
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeVersion: int
        :param ResourceOrderId: 资源订单ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceOrderId: int
        :param IsTradeCluster: 是否计费集群
注意：此字段可能返回 null，表示取不到有效值。
        :type IsTradeCluster: int
        :param AlarmInfo: 集群错误状态告警信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AlarmInfo: str
        :param IsWoodpeckerCluster: 是否采用新架构
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWoodpeckerCluster: int
        :param MetaDb: 元数据库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MetaDb: str
        :param Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param HiveMetaDb: Hive元数据信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HiveMetaDb: str
        :param ServiceClass: 集群类型:EMR,CLICKHOUSE,DRUID
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceClass: str
        :param AliasInfo: 集群所有节点的别名序列化
注意：此字段可能返回 null，表示取不到有效值。
        :type AliasInfo: str
        :param ProductId: 集群版本Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: int
        """
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
        :type ProductId: int
        :param VPCSettings: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param Software: 部署的组件列表。不同的EMR产品ID（ProductId：具体含义参考入参ProductId字段）需要选择不同的必选组件：
<li>ProductId为1的时候，必选组件包括：hadoop-2.7.3、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId为2的时候，必选组件包括：hadoop-2.7.3、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId为4的时候，必选组件包括：hadoop-2.8.4、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId为7的时候，必选组件包括：hadoop-3.1.2、knox-1.2.0、zookeeper-3.4.9</li>
        :type Software: list of str
        :param ResourceSpec: 节点资源的规格。
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
        :param SupportHA: 是否开启节点高可用。取值范围：
<li>0：表示不开启节点高可用。</li>
<li>1：表示开启节点高可用。</li>
        :type SupportHA: int
        :param InstanceName: 实例名称。
<li>长度限制为6-36个字符。</li>
<li>只允许包含中文、字母、数字、-、_。</li>
        :type InstanceName: str
        :param PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param TimeSpan: 购买实例的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>
        :type TimeSpan: int
        :param TimeUnit: 购买实例的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>
        :type TimeUnit: str
        :param LoginSettings: 实例登录设置。通过该参数可以设置所购买节点的登录方式密码或者密钥。
<li>设置密钥时，密码仅用于组件原生WebUI快捷入口登录。</li>
<li>未设置密钥时，密码用于登录所购节点以及组件原生WebUI快捷入口登录。</li>
        :type LoginSettings: :class:`tencentcloud.emr.v20190103.models.LoginSettings`
        :param COSSettings: 开启COS访问需要设置的参数。
        :type COSSettings: :class:`tencentcloud.emr.v20190103.models.COSSettings`
        :param SgId: 实例所属安全组的ID，形如sg-xxxxxxxx。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的SecurityGroupId字段来获取。
        :type SgId: str
        :param PreExecutedFileSettings: 引导操作脚本设置。
        :type PreExecutedFileSettings: list of PreExecuteFileSettings
        :param AutoRenew: 包年包月实例是否自动续费。取值范围：
<li>0：表示不自动续费。</li>
<li>1：表示自动续费。</li>
        :type AutoRenew: int
        :param ClientToken: 客户端Token。
        :type ClientToken: str
        :param NeedMasterWan: 是否开启集群Master节点公网。取值范围：
<li>NEED_MASTER_WAN：表示开启集群Master节点公网。</li>
<li>NOT_NEED_MASTER_WAN：表示不开启。</li>默认开启集群Master节点公网。
        :type NeedMasterWan: str
        :param RemoteLoginAtCreate: 是否需要开启外网远程登录，即22号端口。在SgId不为空时，该参数无效。
        :type RemoteLoginAtCreate: int
        :param CheckSecurity: 是否开启安全集群。0表示不开启，非0表示开启。
        :type CheckSecurity: int
        :param ExtendFsField: 访问外部文件系统。
        :type ExtendFsField: str
        :param Tags: 标签描述列表。通过指定该参数可以同时绑定标签到相应的实例。
        :type Tags: list of Tag
        :param DisasterRecoverGroupIds: 分散置放群组ID列表，当前只支持指定一个。
        :type DisasterRecoverGroupIds: list of str
        :param CbsEncrypt: 集群维度CBS加密盘，默认0表示不加密，1表示加密
        :type CbsEncrypt: int
        :param MetaType: hive共享元数据库类型。取值范围：
<li>EMR_NEW_META：表示集群默认创建</li>
<li>EMR_EXIT_METE：表示集群使用指定EMR-MetaDB。</li>
<li>USER_CUSTOM_META：表示集群使用自定义MetaDB。</li>
        :type MetaType: str
        :param UnifyMetaInstanceId: EMR-MetaDB实例
        :type UnifyMetaInstanceId: str
        :param MetaDBInfo: 自定义MetaDB信息
        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`
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


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CustomMetaInfo(AbstractModel):
    """用户自建Hive-MetaDB信息

    """

    def __init__(self):
        """
        :param MetaDataJdbcUrl: 自定义MetaDB的JDBC连接，请以 jdbc:mysql:// 开头
        :type MetaDataJdbcUrl: str
        :param MetaDataUser: 自定义MetaDB用户名
        :type MetaDataUser: str
        :param MetaDataPass: 自定义MetaDB密码
        :type MetaDataPass: str
        """
        self.MetaDataJdbcUrl = None
        self.MetaDataUser = None
        self.MetaDataPass = None


    def _deserialize(self, params):
        self.MetaDataJdbcUrl = params.get("MetaDataJdbcUrl")
        self.MetaDataUser = params.get("MetaDataUser")
        self.MetaDataPass = params.get("MetaDataPass")


class DescribeClusterNodesRequest(AbstractModel):
    """DescribeClusterNodes请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 集群实例ID,实例ID形如: emr-xxxxxxxx
        :type InstanceId: str
        :param NodeFlag: 节点标识，取值为：
<li>all：表示获取全部类型节点，cdb信息除外。</li>
<li>master：表示获取master节点信息。</li>
<li>core：表示获取core节点信息。</li>
<li>task：表示获取task节点信息。</li>
<li>common：表示获取common节点信息。</li>
<li>router：表示获取router节点信息。</li>
<li>db：表示获取正常状态的cdb信息。</li>
<li>recyle：表示获取回收站隔离中的节点信息，包括cdb信息。</li>
<li>renew：表示获取所有待续费的节点信息，包括cdb信息，自动续费节点不会返回。</li>
注意：现在只支持以上取值，输入其他值会导致错误。
        :type NodeFlag: str
        :param Offset: 页编号，默认值为0，表示第一页。
        :type Offset: int
        :param Limit: 每页返回数量，默认值为100，最大值为100。
        :type Limit: int
        """
        self.InstanceId = None
        self.NodeFlag = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NodeFlag = params.get("NodeFlag")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeClusterNodesResponse(AbstractModel):
    """DescribeClusterNodes返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCnt: 查询到的节点总数
        :type TotalCnt: int
        :param NodeList: 节点详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeList: list of NodeHardwareInfo
        :param TagKeys: 用户所有的标签键列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKeys: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCnt = None
        self.NodeList = None
        self.TagKeys = None
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
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        """
        :param DisplayStrategy: 集群筛选策略。取值范围：
<li>clusterList：表示查询除了已销毁集群之外的集群列表。</li>
<li>monitorManage：表示查询除了已销毁、创建中以及创建失败的集群之外的集群列表。</li>
<li>cloudHardwareManage/componentManage：目前这两个取值为预留取值，暂时和monitorManage表示同样的含义。</li>
        :type DisplayStrategy: str
        :param InstanceIds: 按照一个或者多个实例ID查询。实例ID形如: emr-xxxxxxxx 。(此参数的具体格式可参考API[简介](https://cloud.tencent.com/document/api/213/15688)的 Ids.N 一节)。如果不填写实例ID，返回该APPID下所有实例列表。
        :type InstanceIds: list of str
        :param Offset: 页编号，默认值为0，表示第一页。
        :type Offset: int
        :param Limit: 每页返回数量，默认值为10，最大值为100。
        :type Limit: int
        :param ProjectId: 建议必填-1，表示拉取所有项目下的集群。
不填默认值为0，表示拉取默认项目下的集群。
实例所属项目ID。该参数可以通过调用 [DescribeProject](https://cloud.tencent.com/document/api/378/4400) 的返回值中的 projectId 字段来获取。
        :type ProjectId: int
        :param OrderField: 排序字段。取值范围：
<li>clusterId：表示按照实例ID排序。</li>
<li>addTime：表示按照实例创建时间排序。</li>
<li>status：表示按照实例的状态码排序。</li>
        :type OrderField: str
        :param Asc: 按照OrderField升序或者降序进行排序。取值范围：
<li>0：表示降序。</li>
<li>1：表示升序。</li>默认值为0。
        :type Asc: int
        """
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


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCnt: 符合条件的实例总数。
        :type TotalCnt: int
        :param ClusterList: EMR实例详细信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterList: list of ClusterInstancesInfo
        :param TagKeys: 实例关联的标签键列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKeys: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class EmrProductConfigOutter(AbstractModel):
    """EMR产品配置

    """

    def __init__(self):
        """
        :param SoftInfo: 软件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SoftInfo: list of str
        :param MasterNodeSize: Master节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterNodeSize: int
        :param CoreNodeSize: Core节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type CoreNodeSize: int
        :param TaskNodeSize: Task节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskNodeSize: int
        :param ComNodeSize: Common节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ComNodeSize: int
        :param MasterResource: Master节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param CoreResource: Core节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type CoreResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param TaskResource: Task节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param ComResource: Common节点资源
注意：此字段可能返回 null，表示取不到有效值。
        :type ComResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param OnCos: 是否使用COS
注意：此字段可能返回 null，表示取不到有效值。
        :type OnCos: bool
        :param ChargeType: 收费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: int
        :param RouterNodeSize: Router节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type RouterNodeSize: int
        :param SupportHA: 是否支持HA
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportHA: bool
        :param SecurityOn: 是否支持安全模式
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityOn: bool
        :param SecurityGroup: 安全组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroup: str
        :param CbsEncrypt: 是否开启Cbs加密
注意：此字段可能返回 null，表示取不到有效值。
        :type CbsEncrypt: int
        """
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


class InquiryPriceCreateInstanceRequest(AbstractModel):
    """InquiryPriceCreateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param TimeUnit: 购买实例的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>
        :type TimeUnit: str
        :param TimeSpan: 购买实例的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>
        :type TimeSpan: int
        :param ResourceSpec: 询价的节点规格。
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
        :param Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>
        :type Currency: str
        :param PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param SupportHA: 是否开启节点高可用。取值范围：
<li>0：表示不开启节点高可用。</li>
<li>1：表示开启节点高可用。</li>
        :type SupportHA: int
        :param Software: 部署的组件列表。不同的EMR产品ID（ProductId：具体含义参考入参ProductId字段）需要选择不同的必选组件：
<li>ProductId为1的时候，必选组件包括：hadoop-2.7.3、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId为2的时候，必选组件包括：hadoop-2.7.3、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId为4的时候，必选组件包括：hadoop-2.8.4、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId为7的时候，必选组件包括：hadoop-3.1.2、knox-1.2.0、zookeeper-3.4.9</li>
        :type Software: list of str
        :param Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param VPCSettings: 私有网络相关信息配置。通过该参数可以指定私有网络的ID，子网ID等信息。
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param MetaType: hive共享元数据库类型。取值范围：
<li>EMR_NEW_META：表示集群默认创建</li>
<li>EMR_EXIT_METE：表示集群使用指定EMR-MetaDB。</li>
<li>USER_CUSTOM_META：表示集群使用自定义MetaDB。</li>
        :type MetaType: str
        :param UnifyMetaInstanceId: EMR-MetaDB实例
        :type UnifyMetaInstanceId: str
        :param MetaDBInfo: 自定义MetaDB信息
        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`
        :param ProductId: 产品ID，不同产品ID表示不同的EMR产品版本。取值范围：
<li>1：表示EMR-V1.3.1。</li>
<li>2：表示EMR-V2.0.1。</li>
<li>4：表示EMR-V2.1.0。</li>
<li>7：表示EMR-V3.0.0。</li>
        :type ProductId: int
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


class InquiryPriceCreateInstanceResponse(AbstractModel):
    """InquiryPriceCreateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: float
        :param DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountCost: float
        :param TimeUnit: 购买实例的时间单位。取值范围：
<li>s：表示秒。</li>
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param TimeSpan: 购买实例的时长。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSpan: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param TimeSpan: 实例续费的时长。需要结合TimeUnit一起使用。1表示续费1一个月
        :type TimeSpan: int
        :param ResourceIds: 待续费节点的资源ID列表。资源ID形如：emr-vm-xxxxxxxx。有效的资源ID可通过登录[控制台](https://console.cloud.tencent.com/emr/static/hardware)查询。
        :type ResourceIds: list of str
        :param Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param PayMode: 实例计费模式。此处只支持取值为1，表示包年包月。
        :type PayMode: int
        :param TimeUnit: 实例续费的时间单位。取值范围：
<li>m：表示月份。</li>
        :type TimeUnit: str
        :param Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>
        :type Currency: str
        """
        self.TimeSpan = None
        self.ResourceIds = None
        self.Placement = None
        self.PayMode = None
        self.TimeUnit = None
        self.Currency = None


    def _deserialize(self, params):
        self.TimeSpan = params.get("TimeSpan")
        self.ResourceIds = params.get("ResourceIds")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.PayMode = params.get("PayMode")
        self.TimeUnit = params.get("TimeUnit")
        self.Currency = params.get("Currency")


class InquiryPriceRenewInstanceResponse(AbstractModel):
    """InquiryPriceRenewInstance返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: float
        :param DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountCost: float
        :param TimeUnit: 实例续费的时间单位。取值范围：
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param TimeSpan: 实例续费的时长。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSpan: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>
        :type TimeUnit: str
        :param TimeSpan: 扩容的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>
        :type TimeSpan: int
        :param ZoneId: 实例所属的可用区ID，例如100003。该参数可以通过调用 [DescribeZones](https://cloud.tencent.com/document/api/213/15707) 的返回值中的ZoneId字段来获取。
        :type ZoneId: int
        :param PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param CoreCount: 扩容的Core节点数量。
        :type CoreCount: int
        :param TaskCount: 扩容的Task节点数量。
        :type TaskCount: int
        :param Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>
        :type Currency: str
        :param RouterCount: 扩容的Router节点数量。
        :type RouterCount: int
        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.ZoneId = None
        self.PayMode = None
        self.InstanceId = None
        self.CoreCount = None
        self.TaskCount = None
        self.Currency = None
        self.RouterCount = None


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


class InquiryPriceScaleOutInstanceResponse(AbstractModel):
    """InquiryPriceScaleOutInstance返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: str
        :param DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountCost: str
        :param Unit: 扩容的时间单位。取值范围：
<li>s：表示秒。</li>
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param PriceSpec: 询价的节点规格。
注意：此字段可能返回 null，表示取不到有效值。
        :type PriceSpec: :class:`tencentcloud.emr.v20190103.models.PriceResource`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>
        :type TimeUnit: str
        :param TimeSpan: 变配的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>
        :type TimeSpan: int
        :param UpdateSpec: 节点变配的目标配置。
        :type UpdateSpec: :class:`tencentcloud.emr.v20190103.models.UpdateInstanceSettings`
        :param PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目等属性。
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param Currency: 货币种类。取值范围：
<li>CNY：表示人民币。</li>
        :type Currency: str
        """
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


class InquiryPriceUpdateInstanceResponse(AbstractModel):
    """InquiryPriceUpdateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalCost: 原价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalCost: float
        :param DiscountCost: 折扣价，单位为元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountCost: float
        :param TimeUnit: 变配的时间单位。取值范围：
<li>s：表示秒。</li>
<li>m：表示月份。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param TimeSpan: 变配的时长。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSpan: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class MultiDisk(AbstractModel):
    """多云盘参数

    """

    def __init__(self):
        """
        :param DiskType: 云盘类型("CLOUD_PREMIUM","CLOUD_SSD","CLOUD_BASIC")的一种
        :type DiskType: str
        :param Volume: 云盘大小
        :type Volume: int
        :param Count: 该类型云盘个数
        :type Count: int
        """
        self.DiskType = None
        self.Volume = None
        self.Count = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.Volume = params.get("Volume")
        self.Count = params.get("Count")


class MultiDiskMC(AbstractModel):
    """多云盘参数

    """

    def __init__(self):
        """
        :param Count: 该类型云盘个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param Type: 磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param Volume: 云盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Volume: int
        """
        self.Count = None
        self.Type = None
        self.Volume = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Type = params.get("Type")
        self.Volume = params.get("Volume")


class NewResourceSpec(AbstractModel):
    """资源描述

    """

    def __init__(self):
        """
        :param MasterResourceSpec: 描述Master节点资源
        :type MasterResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param CoreResourceSpec: 描述Core节点资源
        :type CoreResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param TaskResourceSpec: 描述Task节点资源
        :type TaskResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param MasterCount: Master节点数量
        :type MasterCount: int
        :param CoreCount: Core节点数量
        :type CoreCount: int
        :param TaskCount: Task节点数量
        :type TaskCount: int
        :param CommonResourceSpec: 描述Common节点资源
        :type CommonResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param CommonCount: Common节点数量
        :type CommonCount: int
        """
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


class NodeHardwareInfo(AbstractModel):
    """节点硬件信息

    """

    def __init__(self):
        """
        :param AppId: 用户APPID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param SerialNo: 序列号
注意：此字段可能返回 null，表示取不到有效值。
        :type SerialNo: str
        :param OrderNo: 机器实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderNo: str
        :param WanIp: master节点绑定外网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type WanIp: str
        :param Flag: 节点类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Flag: int
        :param Spec: 节点规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Spec: str
        :param CpuNum: 节点核数
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuNum: int
        :param MemSize: 节点内存
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param MemDesc: 节点内存描述
注意：此字段可能返回 null，表示取不到有效值。
        :type MemDesc: str
        :param RegionId: 节点所在region
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param ZoneId: 节点所在Zone
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param ApplyTime: 申请时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplyTime: str
        :param FreeTime: 释放时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeTime: str
        :param DiskSize: 硬盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: str
        :param NameTag: 节点描述
注意：此字段可能返回 null，表示取不到有效值。
        :type NameTag: str
        :param Services: 节点部署服务
注意：此字段可能返回 null，表示取不到有效值。
        :type Services: str
        :param StorageType: 磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param RootSize: 系统盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type RootSize: int
        :param ChargeType: 付费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: int
        :param CdbIp: 数据库IP
注意：此字段可能返回 null，表示取不到有效值。
        :type CdbIp: str
        :param CdbPort: 数据库端口
注意：此字段可能返回 null，表示取不到有效值。
        :type CdbPort: int
        :param HwDiskSize: 硬盘容量
注意：此字段可能返回 null，表示取不到有效值。
        :type HwDiskSize: int
        :param HwDiskSizeDesc: 硬盘容量描述
注意：此字段可能返回 null，表示取不到有效值。
        :type HwDiskSizeDesc: str
        :param HwMemSize: 内存容量
注意：此字段可能返回 null，表示取不到有效值。
        :type HwMemSize: int
        :param HwMemSizeDesc: 内存容量描述
注意：此字段可能返回 null，表示取不到有效值。
        :type HwMemSizeDesc: str
        :param ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param EmrResourceId: 节点资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EmrResourceId: str
        :param IsAutoRenew: 续费标志
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAutoRenew: int
        :param DeviceClass: 设备标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceClass: str
        :param Mutable: 支持变配
注意：此字段可能返回 null，表示取不到有效值。
        :type Mutable: int
        :param MCMultiDisk: 多云盘
注意：此字段可能返回 null，表示取不到有效值。
        :type MCMultiDisk: list of MultiDiskMC
        :param CdbNodeInfo: 数据库信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CdbNodeInfo: :class:`tencentcloud.emr.v20190103.models.CdbInfo`
        :param Ip: 内网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param Destroyable: 此节点是否可销毁，1可销毁，0不可销毁
注意：此字段可能返回 null，表示取不到有效值。
        :type Destroyable: int
        :param Tags: 节点绑定的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param AutoFlag: 是否是自动扩缩容节点，0为普通节点，1为自动扩缩容节点。
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoFlag: int
        """
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


class OutterResource(AbstractModel):
    """资源详情

    """

    def __init__(self):
        """
        :param Spec: 规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Spec: str
        :param SpecName: 规格名
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecName: str
        :param StorageType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param DiskType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param RootSize: 系统盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type RootSize: int
        :param MemSize: 内存大小
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param Cpu: CPU个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param DiskSize: 硬盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param InstanceType: 规格
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        """
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


class Placement(AbstractModel):
    """描述集群实例位置信息

    """

    def __init__(self):
        """
        :param ProjectId: 实例所属项目ID。该参数可以通过调用 DescribeProject 的返回值中的 projectId 字段来获取。填0为默认项目。
        :type ProjectId: int
        :param Zone: 实例所属的可用区，例如ap-guangzhou-1。该参数也可以通过调用 DescribeZones 的返回值中的Zone字段来获取。
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
        :param Path: 脚本在COS上路径，已废弃
        :type Path: str
        :param Args: 执行脚本参数
        :type Args: list of str
        :param Bucket: COS的Bucket名称，已废弃
        :type Bucket: str
        :param Region: COS的Region名称，已废弃
        :type Region: str
        :param Domain: COS的Domain数据，已废弃
        :type Domain: str
        :param RunOrder: 执行顺序
        :type RunOrder: int
        :param WhenRun: resourceAfter 或 clusterAfter
        :type WhenRun: str
        :param CosFileName: 脚本文件名，已废弃
        :type CosFileName: str
        :param CosFileURI: 脚本的cos地址
        :type CosFileURI: str
        :param CosSecretId: cos的SecretId
        :type CosSecretId: str
        :param CosSecretKey: Cos的SecretKey
        :type CosSecretKey: str
        :param AppId: cos的appid，已废弃
        :type AppId: str
        """
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


class PriceResource(AbstractModel):
    """询价资源

    """

    def __init__(self):
        """
        :param Spec: 需要的规格
注意：此字段可能返回 null，表示取不到有效值。
        :type Spec: str
        :param StorageType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param DiskType: 硬盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param RootSize: 系统盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type RootSize: int
        :param MemSize: 内存大小
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param Cpu: 核心数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param DiskSize: 硬盘大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param MultiDisks: 云盘列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiDisks: list of MultiDisk
        :param DiskCnt: 磁盘数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskCnt: int
        :param InstanceType: 规格
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param DiskNum: 磁盘数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskNum: int
        :param LocalDiskNum: 本地盘的数量
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalDiskNum: int
        """
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


class Resource(AbstractModel):
    """资源详情

    """

    def __init__(self):
        """
        :param Spec: 节点规格描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Spec: str
        :param StorageType: 存储类型
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param DiskType: 磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param MemSize: 内存容量,单位为M
注意：此字段可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param Cpu: CPU核数
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param DiskSize: 数据盘容量
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param RootSize: 系统盘容量
注意：此字段可能返回 null，表示取不到有效值。
        :type RootSize: int
        :param MultiDisks: 云盘列表，当数据盘为一块云盘时，直接使用DiskType和DiskSize参数，超出部分使用MultiDisks
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiDisks: list of MultiDisk
        :param Tags: 需要绑定的标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param InstanceType: 规格类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param LocalDiskNum: 本地盘数量
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalDiskNum: int
        :param DiskNum: 盘数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskNum: int
        """
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


class ScaleOutInstanceRequest(AbstractModel):
    """ScaleOutInstance请求参数结构体

    """

    def __init__(self):
        """
        :param TimeUnit: 扩容的时间单位。取值范围：
<li>s：表示秒。PayMode取值为0时，TimeUnit只能取值为s。</li>
<li>m：表示月份。PayMode取值为1时，TimeUnit只能取值为m。</li>
        :type TimeUnit: str
        :param TimeSpan: 扩容的时长。结合TimeUnit一起使用。
<li>TimeUnit为s时，该参数只能填写3600，表示按量计费实例。</li>
<li>TimeUnit为m时，该参数填写的数字表示包年包月实例的购买时长，如1表示购买一个月</li>
        :type TimeSpan: int
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param PayMode: 实例计费模式。取值范围：
<li>0：表示按量计费。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param ClientToken: 客户端Token。
        :type ClientToken: str
        :param PreExecutedFileSettings: 引导操作脚本设置。
        :type PreExecutedFileSettings: list of PreExecuteFileSettings
        :param TaskCount: 扩容的Task节点数量。
        :type TaskCount: int
        :param CoreCount: 扩容的Core节点数量。
        :type CoreCount: int
        :param UnNecessaryNodeList: 扩容时不需要安装的进程。
        :type UnNecessaryNodeList: list of int non-negative
        :param RouterCount: 扩容的Router节点数量。
        :type RouterCount: int
        :param SoftDeployInfo: 部署的服务。
<li>SoftDeployInfo和ServiceNodeInfo是同组参数，和UnNecessaryNodeList参数互斥。</li>
<li>建议使用SoftDeployInfo和ServiceNodeInfo组合。</li>
        :type SoftDeployInfo: list of int non-negative
        :param ServiceNodeInfo: 启动的进程。
        :type ServiceNodeInfo: list of int non-negative
        :param DisasterRecoverGroupIds: 分散置放群组ID列表，当前仅支持指定一个。
        :type DisasterRecoverGroupIds: list of str
        :param Tags: 扩容节点绑定标签列表。
        :type Tags: list of Tag
        """
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


class ScaleOutInstanceResponse(AbstractModel):
    """ScaleOutInstance返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param DealNames: 订单号。
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param ClientToken: 客户端Token。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientToken: str
        :param FlowId: 扩容流程ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param BillId: 大订单号。
注意：此字段可能返回 null，表示取不到有效值。
        :type BillId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        """
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class TerminateInstanceRequest(AbstractModel):
    """TerminateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param ResourceIds: 销毁节点ID。该参数为预留参数，用户无需配置。
        :type ResourceIds: list of str
        """
        self.InstanceId = None
        self.ResourceIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceIds = params.get("ResourceIds")


class TerminateInstanceResponse(AbstractModel):
    """TerminateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateTasksRequest(AbstractModel):
    """TerminateTasks请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param ResourceIds: 待销毁节点的资源ID列表。资源ID形如：emr-vm-xxxxxxxx。有效的资源ID可通过登录[控制台](https://console.cloud.tencent.com/emr/static/hardware)查询。
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateInstanceSettings(AbstractModel):
    """变配资源规格

    """

    def __init__(self):
        """
        :param Memory: 内存容量，单位为G
        :type Memory: int
        :param CPUCores: CPU核数
        :type CPUCores: int
        :param ResourceId: 机器资源ID（EMR测资源标识）
        :type ResourceId: str
        :param InstanceType: 变配机器规格
        :type InstanceType: str
        """
        self.Memory = None
        self.CPUCores = None
        self.ResourceId = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.CPUCores = params.get("CPUCores")
        self.ResourceId = params.get("ResourceId")
        self.InstanceType = params.get("InstanceType")


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