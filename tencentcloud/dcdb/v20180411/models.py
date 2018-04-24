# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
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


class AddShardConfig(AbstractModel):
    """升级实例 -- 新增分片类型

    """

    def __init__(self):
        """
        :param ShardCount: 新增分片的数量
        :type ShardCount: int
        :param ShardMemory: 分片内存大小，单位 GB
        :type ShardMemory: int
        :param ShardStorage: 分片存储大小，单位 GB
        :type ShardStorage: int
        """
        self.ShardCount = None
        self.ShardMemory = None
        self.ShardStorage = None


    def _deserialize(self, params):
        self.ShardCount = params.get("ShardCount")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")


class CreateDCDBInstanceRequest(AbstractModel):
    """CreateDCDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param Zones: 分片节点可用区分布，最多可填两个可用区。当分片规格为一主两从时，其中两个节点在第一个可用区。
        :type Zones: list of str
        :param Count: 欲购买实例的数量，目前只支持购买1个实例
        :type Count: int
        :param Period: 欲购买的时长，单位：月。
        :type Period: int
        :param ProjectId: 项目 ID，可以通过查看项目列表获取，不传则关联到默认项目
        :type ProjectId: int
        :param VpcId: 虚拟私有网络 ID，不传或传空表示创建为基础网络
        :type VpcId: str
        :param SubnetId: 虚拟私有网络子网 ID，VpcId不为空时必填
        :type SubnetId: str
        :param ShardMemory: 分片内存大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardMemory: int
        :param ShardStorage: 分片存储空间大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardStorage: int
        :param ShardNodeCount: 单个分片节点个数，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardNodeCount: int
        :param ShardCount: 实例分片个数，可选范围2-8，可以通过升级实例进行新增分片到最多64个分片。
        :type ShardCount: int
        :param DbVersionId: 数据库引擎版本，当前可选：10.0.10，10.1.9，5.7.17
        :type DbVersionId: str
        :param AutoVoucher: 是否自动使用代金券进行支付，默认不使用。
        :type AutoVoucher: bool
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        """
        self.Zones = None
        self.Count = None
        self.Period = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.ShardMemory = None
        self.ShardStorage = None
        self.ShardNodeCount = None
        self.ShardCount = None
        self.DbVersionId = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.Zones = params.get("Zones")
        self.Count = params.get("Count")
        self.Period = params.get("Period")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")
        self.ShardNodeCount = params.get("ShardNodeCount")
        self.ShardCount = params.get("ShardCount")
        self.DbVersionId = params.get("DbVersionId")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")


class CreateDCDBInstanceResponse(AbstractModel):
    """CreateDCDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealName: 长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :type DealName: str
        :param InstanceIds: 订单对应的实例 ID 列表，如果此处没有返回实例 ID，可以通过订单查询接口获取。还可通过实例查询接口查询实例是否创建完成。
        :type InstanceIds: list of str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class DCDBInstanceInfo(AbstractModel):
    """分布式数据库实例信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param AppId: APPID
        :type AppId: int
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param Region: 地域
        :type Region: str
        :param Zone: 可用区
        :type Zone: str
        :param VpcId: VPC数字ID
        :type VpcId: int
        :param SubnetId: Subnet数字ID
        :type SubnetId: int
        :param StatusDesc: 状态中文描述
        :type StatusDesc: str
        :param Status: 状态
        :type Status: int
        :param Vip: 内网IP
        :type Vip: str
        :param Vport: 内网端口
        :type Vport: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param AutoRenewFlag: 自动续费标志
        :type AutoRenewFlag: int
        :param Memory: 内存大小，单位 GB
        :type Memory: int
        :param Storage: 存储大小，单位 GB
        :type Storage: int
        :param ShardCount: 分片个数
        :type ShardCount: int
        :param PeriodEndTime: 到期时间
        :type PeriodEndTime: str
        :param IsolatedTimestamp: 隔离时间
        :type IsolatedTimestamp: str
        :param Uin: UIN
        :type Uin: str
        :param ShardDetail: 分片详情
        :type ShardDetail: list of ShardInfo
        """
        self.InstanceId = None
        self.InstanceName = None
        self.AppId = None
        self.ProjectId = None
        self.Region = None
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None
        self.StatusDesc = None
        self.Status = None
        self.Vip = None
        self.Vport = None
        self.CreateTime = None
        self.AutoRenewFlag = None
        self.Memory = None
        self.Storage = None
        self.ShardCount = None
        self.PeriodEndTime = None
        self.IsolatedTimestamp = None
        self.Uin = None
        self.ShardDetail = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.AppId = params.get("AppId")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.StatusDesc = params.get("StatusDesc")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.CreateTime = params.get("CreateTime")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.ShardCount = params.get("ShardCount")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.IsolatedTimestamp = params.get("IsolatedTimestamp")
        self.Uin = params.get("Uin")
        if params.get("ShardDetail") is not None:
            self.ShardDetail = []
            for item in params.get("ShardDetail"):
                obj = ShardInfo()
                obj._deserialize(item)
                self.ShardDetail.append(obj)


class Deal(AbstractModel):
    """订单信息

    """

    def __init__(self):
        """
        :param DealName: 订单号
        :type DealName: str
        :param OwnerUin: 所属账号
        :type OwnerUin: str
        :param Count: 商品数量
        :type Count: int
        :param FlowId: 关联的流程 Id，可用于查询流程执行状态
        :type FlowId: int
        :param InstanceIds: 只有创建实例的订单会填充该字段，表示该订单创建的实例的 ID。
        :type InstanceIds: list of str
        """
        self.DealName = None
        self.OwnerUin = None
        self.Count = None
        self.FlowId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.OwnerUin = params.get("OwnerUin")
        self.Count = params.get("Count")
        self.FlowId = params.get("FlowId")
        self.InstanceIds = params.get("InstanceIds")


class DescribeDBLogFilesRequest(AbstractModel):
    """DescribeDBLogFiles请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        :param ShardId: 分片 ID，形如：shard-7noic7tv
        :type ShardId: str
        :param Type: 请求日志类型，取值只能为1、2、3或者4。1-binlog，2-冷备，3-errlog，4-slowlog。
        :type Type: int
        """
        self.InstanceId = None
        self.ShardId = None
        self.Type = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ShardId = params.get("ShardId")
        self.Type = params.get("Type")


class DescribeDBLogFilesResponse(AbstractModel):
    """DescribeDBLogFiles返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDCDBInstancesRequest(AbstractModel):
    """DescribeDCDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 按照一个或者多个实例 ID 查询。实例 ID 形如：dcdbt-2t4cf98d
        :type InstanceIds: list of str
        :param SearchName: 搜索的字段名，当前支持的值有：instancename、vip、all。传 instancename 表示按实例名进行搜索；传 vip 表示按内网IP进行搜索；传 all 将会按实例ID、实例名和内网IP进行搜索。
        :type SearchName: str
        :param SearchKey: 搜索的关键字，支持模糊搜索。多个关键字使用换行符（'\n'）分割。
        :type SearchKey: str
        :param ProjectIds: 按项目 ID 查询
        :type ProjectIds: list of int
        :param IsFilterVpc: 是否根据 VPC 网络来搜索，0 为否，1 为是
        :type IsFilterVpc: list of int
        :param VpcId: 私有网络 ID， IsFilterVpc 为 1 时有效
        :type VpcId: str
        :param SubnetId: 私有网络的子网 ID， IsFilterVpc 为 1 时有效
        :type SubnetId: str
        :param OrderBy: 排序字段， projectId， createtime， instancename 三者之一
        :type OrderBy: str
        :param OrderByType: 排序类型， desc 或者 asc
        :type OrderByType: str
        :param Offset: 偏移量，默认为 0
        :type Offset: int
        :param Limit: 返回数量，默认为 10，最大值为 100。
        :type Limit: int
        """
        self.InstanceIds = None
        self.SearchName = None
        self.SearchKey = None
        self.ProjectIds = None
        self.IsFilterVpc = None
        self.VpcId = None
        self.SubnetId = None
        self.OrderBy = None
        self.OrderByType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.SearchName = params.get("SearchName")
        self.SearchKey = params.get("SearchKey")
        self.ProjectIds = params.get("ProjectIds")
        self.IsFilterVpc = params.get("IsFilterVpc")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDCDBInstancesResponse(AbstractModel):
    """DescribeDCDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量
        :type TotalCount: int
        :param Instances: 实例详细信息列表
        :type Instances: list of DCDBInstanceInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = DCDBInstanceInfo()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDCDBPriceRequest(AbstractModel):
    """DescribeDCDBPrice请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 欲新购实例的可用区ID。
        :type Zone: str
        :param Count: 欲购买实例的数量，目前只支持购买1个实例
        :type Count: int
        :param Period: 欲购买的时长，单位：月。
        :type Period: int
        :param ShardNodeCount: 单个分片节点个数大小，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardNodeCount: int
        :param ShardMemory: 分片内存大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardMemory: int
        :param ShardStorage: 分片存储空间大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardStorage: int
        :param ShardCount: 实例分片个数，可选范围2-8，可以通过升级实例进行新增分片到最多64个分片。
        :type ShardCount: int
        """
        self.Zone = None
        self.Count = None
        self.Period = None
        self.ShardNodeCount = None
        self.ShardMemory = None
        self.ShardStorage = None
        self.ShardCount = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Count = params.get("Count")
        self.Period = params.get("Period")
        self.ShardNodeCount = params.get("ShardNodeCount")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")
        self.ShardCount = params.get("ShardCount")


class DescribeDCDBPriceResponse(AbstractModel):
    """DescribeDCDBPrice返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 原价，单位：分
        :type OriginalPrice: int
        :param Price: 实际价格，单位：分。受折扣等影响，可能和原价不同。
        :type Price: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class DescribeDCDBRenewalPriceRequest(AbstractModel):
    """DescribeDCDBRenewalPrice请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待续费的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param Period: 续费时长，单位：月。不传则默认为1个月。
        :type Period: int
        """
        self.InstanceId = None
        self.Period = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Period = params.get("Period")


class DescribeDCDBRenewalPriceResponse(AbstractModel):
    """DescribeDCDBRenewalPrice返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 原价，单位：分
        :type OriginalPrice: int
        :param Price: 实际价格，单位：分。受折扣等影响，可能和原价不同。
        :type Price: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class DescribeDCDBSaleInfoRequest(AbstractModel):
    """DescribeDCDBSaleInfo请求参数结构体

    """


class DescribeDCDBSaleInfoResponse(AbstractModel):
    """DescribeDCDBSaleInfo返回参数结构体

    """

    def __init__(self):
        """
        :param RegionList: 可售卖地域信息列表
        :type RegionList: list of RegionInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RegionList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionList") is not None:
            self.RegionList = []
            for item in params.get("RegionList"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDCDBUpgradePriceRequest(AbstractModel):
    """DescribeDCDBUpgradePrice请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待升级的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param UpgradeType: 升级类型，取值范围: 
<li> ADD: 新增分片 </li> 
 <li> EXPAND: 升级实例中的已有分片 </li> 
 <li> SPLIT: 将已有分片中的数据切分到新增分片上</li>
        :type UpgradeType: str
        :param AddShardConfig: 新增分片配置，当UpgradeType为ADD时生效。
        :type AddShardConfig: :class:`tencentcloud.dcdb.v20180411.models.AddShardConfig`
        :param ExpandShardConfig: 扩容分片配置，当UpgradeType为EXPAND时生效。
        :type ExpandShardConfig: :class:`tencentcloud.dcdb.v20180411.models.ExpandShardConfig`
        :param SplitShardConfig: 切分分片配置，当UpgradeType为SPLIT时生效。
        :type SplitShardConfig: :class:`tencentcloud.dcdb.v20180411.models.SplitShardConfig`
        """
        self.InstanceId = None
        self.UpgradeType = None
        self.AddShardConfig = None
        self.ExpandShardConfig = None
        self.SplitShardConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UpgradeType = params.get("UpgradeType")
        if params.get("AddShardConfig") is not None:
            self.AddShardConfig = AddShardConfig()
            self.AddShardConfig._deserialize(params.get("AddShardConfig"))
        if params.get("ExpandShardConfig") is not None:
            self.ExpandShardConfig = ExpandShardConfig()
            self.ExpandShardConfig._deserialize(params.get("ExpandShardConfig"))
        if params.get("SplitShardConfig") is not None:
            self.SplitShardConfig = SplitShardConfig()
            self.SplitShardConfig._deserialize(params.get("SplitShardConfig"))


class DescribeDCDBUpgradePriceResponse(AbstractModel):
    """DescribeDCDBUpgradePrice返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 原价，单位：分
        :type OriginalPrice: int
        :param Price: 实际价格，单位：分。受折扣等影响，可能和原价不同。
        :type Price: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders请求参数结构体

    """

    def __init__(self):
        """
        :param DealNames: 待查询的长订单号列表，创建实例、续费实例、扩容实例接口返回。
        :type DealNames: list of str
        """
        self.DealNames = None


    def _deserialize(self, params):
        self.DealNames = params.get("DealNames")


class DescribeOrdersResponse(AbstractModel):
    """DescribeOrders返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的订单数量。
        :type TotalCount: list of int
        :param Deals: 订单信息列表。
        :type Deals: list of Deal
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Deals = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Deals") is not None:
            self.Deals = []
            for item in params.get("Deals"):
                obj = Deal()
                obj._deserialize(item)
                self.Deals.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeShardSpecRequest(AbstractModel):
    """DescribeShardSpec请求参数结构体

    """


class DescribeShardSpecResponse(AbstractModel):
    """DescribeShardSpec返回参数结构体

    """

    def __init__(self):
        """
        :param SpecConfig: 按机型分类的可售卖规格列表
        :type SpecConfig: list of SpecConfig
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.SpecConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpecConfig") is not None:
            self.SpecConfig = []
            for item in params.get("SpecConfig"):
                obj = SpecConfig()
                obj._deserialize(item)
                self.SpecConfig.append(obj)
        self.RequestId = params.get("RequestId")


class ExpandShardConfig(AbstractModel):
    """升级实例 -- 扩容分片类型

    """

    def __init__(self):
        """
        :param ShardInstanceIds: 分片ID数组
        :type ShardInstanceIds: list of str
        :param ShardMemory: 分片内存大小，单位 GB
        :type ShardMemory: int
        :param ShardStorage: 分片存储大小，单位 GB
        :type ShardStorage: int
        """
        self.ShardInstanceIds = None
        self.ShardMemory = None
        self.ShardStorage = None


    def _deserialize(self, params):
        self.ShardInstanceIds = params.get("ShardInstanceIds")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")


class RegionInfo(AbstractModel):
    """售卖可用区信息

    """

    def __init__(self):
        """
        :param Region: 地域英文ID
        :type Region: str
        :param RegionId: 地域数字ID
        :type RegionId: int
        :param RegionName: 地域中文名
        :type RegionName: str
        :param ZoneList: 可用区列表
        :type ZoneList: list of ZonesInfo
        :param AvailableChoice: 可选择的主可用区和从可用区
        :type AvailableChoice: list of ShardZoneChooseInfo
        """
        self.Region = None
        self.RegionId = None
        self.RegionName = None
        self.ZoneList = None
        self.AvailableChoice = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        if params.get("ZoneList") is not None:
            self.ZoneList = []
            for item in params.get("ZoneList"):
                obj = ZonesInfo()
                obj._deserialize(item)
                self.ZoneList.append(obj)
        if params.get("AvailableChoice") is not None:
            self.AvailableChoice = []
            for item in params.get("AvailableChoice"):
                obj = ShardZoneChooseInfo()
                obj._deserialize(item)
                self.AvailableChoice.append(obj)


class RenewDCDBInstanceRequest(AbstractModel):
    """RenewDCDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待续费的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param Period: 续费时长，单位：月。
        :type Period: int
        :param AutoVoucher: 是否自动使用代金券进行支付，默认不使用。
        :type AutoVoucher: bool
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        """
        self.InstanceId = None
        self.Period = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Period = params.get("Period")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")


class RenewDCDBInstanceResponse(AbstractModel):
    """RenewDCDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealName: 长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :type DealName: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class ShardInfo(AbstractModel):
    """分片信息

    """

    def __init__(self):
        """
        :param ShardInstanceId: 分片ID
        :type ShardInstanceId: str
        :param ShardSerialId: 分片Set ID
        :type ShardSerialId: str
        :param Status: 状态
        :type Status: int
        :param Createtime: 创建时间
        :type Createtime: str
        :param Memory: 内存大小，单位 GB
        :type Memory: int
        :param Storage: 存储大小，单位 GB
        :type Storage: int
        :param ShardId: 分片数字ID
        :type ShardId: int
        """
        self.ShardInstanceId = None
        self.ShardSerialId = None
        self.Status = None
        self.Createtime = None
        self.Memory = None
        self.Storage = None
        self.ShardId = None


    def _deserialize(self, params):
        self.ShardInstanceId = params.get("ShardInstanceId")
        self.ShardSerialId = params.get("ShardSerialId")
        self.Status = params.get("Status")
        self.Createtime = params.get("Createtime")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.ShardId = params.get("ShardId")


class ShardZoneChooseInfo(AbstractModel):
    """分片节点可用区选择

    """

    def __init__(self):
        """
        :param MasterZone: 主可用区
        :type MasterZone: :class:`tencentcloud.dcdb.v20180411.models.ZonesInfo`
        :param SlaveZones: 可选的从可用区
        :type SlaveZones: list of ZonesInfo
        """
        self.MasterZone = None
        self.SlaveZones = None


    def _deserialize(self, params):
        if params.get("MasterZone") is not None:
            self.MasterZone = ZonesInfo()
            self.MasterZone._deserialize(params.get("MasterZone"))
        if params.get("SlaveZones") is not None:
            self.SlaveZones = []
            for item in params.get("SlaveZones"):
                obj = ZonesInfo()
                obj._deserialize(item)
                self.SlaveZones.append(obj)


class SpecConfig(AbstractModel):
    """按机型分类的规格配置

    """

    def __init__(self):
        """
        :param Machine: 规格机型
        :type Machine: str
        :param SpecConfigInfos: 规格列表
        :type SpecConfigInfos: list of SpecConfigInfo
        """
        self.Machine = None
        self.SpecConfigInfos = None


    def _deserialize(self, params):
        self.Machine = params.get("Machine")
        if params.get("SpecConfigInfos") is not None:
            self.SpecConfigInfos = []
            for item in params.get("SpecConfigInfos"):
                obj = SpecConfigInfo()
                obj._deserialize(item)
                self.SpecConfigInfos.append(obj)


class SpecConfigInfo(AbstractModel):
    """实例可售卖规格详细信息，创建实例和扩容实例时 NodeCount、Memory 确定售卖规格，硬盘大小可用区间为[MinStorage,MaxStorage]

    """

    def __init__(self):
        """
        :param NodeCount: 节点个数，2 表示一主一从，3 表示一主二从
        :type NodeCount: int
        :param Memory: 内存大小，单位 GB
        :type Memory: int
        :param MinStorage: 数据盘规格最小值，单位 GB
        :type MinStorage: int
        :param MaxStorage: 数据盘规格最大值，单位 GB
        :type MaxStorage: int
        :param SuitInfo: 推荐的使用场景
        :type SuitInfo: str
        :param Pid: 产品类型 Id
        :type Pid: int
        :param Qps: 最大 Qps 值
        :type Qps: int
        """
        self.NodeCount = None
        self.Memory = None
        self.MinStorage = None
        self.MaxStorage = None
        self.SuitInfo = None
        self.Pid = None
        self.Qps = None


    def _deserialize(self, params):
        self.NodeCount = params.get("NodeCount")
        self.Memory = params.get("Memory")
        self.MinStorage = params.get("MinStorage")
        self.MaxStorage = params.get("MaxStorage")
        self.SuitInfo = params.get("SuitInfo")
        self.Pid = params.get("Pid")
        self.Qps = params.get("Qps")


class SplitShardConfig(AbstractModel):
    """升级实例 -- 切分分片类型

    """

    def __init__(self):
        """
        :param ShardInstanceIds: 分片ID数组
        :type ShardInstanceIds: list of str
        :param SplitRate: 数据切分比例
        :type SplitRate: int
        :param ShardMemory: 分片内存大小，单位 GB
        :type ShardMemory: int
        :param ShardStorage: 分片存储大小，单位 GB
        :type ShardStorage: int
        """
        self.ShardInstanceIds = None
        self.SplitRate = None
        self.ShardMemory = None
        self.ShardStorage = None


    def _deserialize(self, params):
        self.ShardInstanceIds = params.get("ShardInstanceIds")
        self.SplitRate = params.get("SplitRate")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")


class UpgradeDCDBInstanceRequest(AbstractModel):
    """UpgradeDCDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待升级的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param UpgradeType: 升级类型，取值范围: 
<li> ADD: 新增分片 </li> 
 <li> EXPAND: 升级实例中的已有分片 </li> 
 <li> SPLIT: 将已有分片中的数据切分到新增分片上</li>
        :type UpgradeType: str
        :param AddShardConfig: 新增分片配置，当UpgradeType为ADD时生效。
        :type AddShardConfig: :class:`tencentcloud.dcdb.v20180411.models.AddShardConfig`
        :param ExpandShardConfig: 扩容分片配置，当UpgradeType为EXPAND时生效。
        :type ExpandShardConfig: :class:`tencentcloud.dcdb.v20180411.models.ExpandShardConfig`
        :param SplitShardConfig: 切分分片配置，当UpgradeType为SPLIT时生效。
        :type SplitShardConfig: :class:`tencentcloud.dcdb.v20180411.models.SplitShardConfig`
        :param AutoVoucher: 是否自动使用代金券进行支付，默认不使用。
        :type AutoVoucher: bool
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        """
        self.InstanceId = None
        self.UpgradeType = None
        self.AddShardConfig = None
        self.ExpandShardConfig = None
        self.SplitShardConfig = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UpgradeType = params.get("UpgradeType")
        if params.get("AddShardConfig") is not None:
            self.AddShardConfig = AddShardConfig()
            self.AddShardConfig._deserialize(params.get("AddShardConfig"))
        if params.get("ExpandShardConfig") is not None:
            self.ExpandShardConfig = ExpandShardConfig()
            self.ExpandShardConfig._deserialize(params.get("ExpandShardConfig"))
        if params.get("SplitShardConfig") is not None:
            self.SplitShardConfig = SplitShardConfig()
            self.SplitShardConfig._deserialize(params.get("SplitShardConfig"))
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")


class UpgradeDCDBInstanceResponse(AbstractModel):
    """UpgradeDCDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealName: 长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :type DealName: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class ZonesInfo(AbstractModel):
    """可用区信息

    """

    def __init__(self):
        """
        :param Zone: 可用区英文ID
        :type Zone: str
        :param ZoneId: 可用区数字ID
        :type ZoneId: int
        :param ZoneName: 可用区中文名
        :type ZoneName: str
        """
        self.Zone = None
        self.ZoneId = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")