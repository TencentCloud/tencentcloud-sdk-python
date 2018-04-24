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


class CreateDBInstancesRequest(AbstractModel):
    """CreateDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID。
        :type ProjectId: int
        :param SpecCode: 售卖规格ID。该参数可以通过调用DescribeProductConfig的返回值中的SpecCode字段来获取。
        :type SpecCode: str
        :param DBVersion: PostgreSQL内核版本，目前只支持：9.3.5、9.5.4两种版本。
        :type DBVersion: str
        :param Storage: 实例容量大小，单位：GB。
        :type Storage: int
        :param InstanceCount: 一次性购买的实例数量。
        :type InstanceCount: int
        :param Period: 购买时长，单位：月。目前只支持1,2,3,4,5,6,7,8,9,10,11,12,24,36这些值。
        :type Period: int
        :param InstanceChargeType: 实例计费类型。目前只支持：PREPAID（预付费，即包年包月）。
        :type InstanceChargeType: str
        :param AutoVoucher: 是否自动使用代金券。1（是），0（否），默认不使用。
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        :param VpcId: 私有网络ID。
        :type VpcId: str
        :param SubnetId: 私有网络子网ID。
        :type SubnetId: str
        :param Zone: 可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。
        :type Zone: str
        """
        self.ProjectId = None
        self.SpecCode = None
        self.DBVersion = None
        self.Storage = None
        self.InstanceCount = None
        self.Period = None
        self.InstanceChargeType = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.VpcId = None
        self.SubnetId = None
        self.Zone = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.SpecCode = params.get("SpecCode")
        self.DBVersion = params.get("DBVersion")
        self.Storage = params.get("Storage")
        self.InstanceCount = params.get("InstanceCount")
        self.Period = params.get("Period")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Zone = params.get("Zone")


class CreateDBInstancesResponse(AbstractModel):
    """CreateDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param DealNames: 订单号列表。每个实例对应一个订单号。
        :type DealNames: list of str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")


class DBInstance(AbstractModel):
    """描述实例的详细信息

    """

    def __init__(self):
        """
        :param Region: 实例所属地域，如: ap-guangzhou，对应RegionSet的Region字段
        :type Region: str
        :param Zone: 实例所属可用区， 如：ap-guangzhou-3，对应ZoneSet的Zone字段
        :type Zone: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: SubnetId
        :type SubnetId: str
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param DBInstanceName: 实例名称
        :type DBInstanceName: str
        :param DBInstanceStatus: 实例状态
        :type DBInstanceStatus: str
        :param DBInstanceMemory: 实例分配的内存大小，单位：GB
        :type DBInstanceMemory: int
        :param DBInstanceStorage: 实例分配的存储空间大小，单位：GB
        :type DBInstanceStorage: int
        :param DBInstanceCpu: 实例分配的CPU数量，单位：个
        :type DBInstanceCpu: int
        :param DBInstanceClass: 售卖规格ID
        :type DBInstanceClass: str
        :param DBInstanceType: 实例类型，类型有：1、primary（主实例）；2、readonly（只读实例）；3、guard（灾备实例）；4、temp（临时实例）
        :type DBInstanceType: str
        :param DBInstanceVersion: 实例版本，目前只支持standard（双机高可用版, 一主一从）
        :type DBInstanceVersion: str
        :param DBCharset: 实例DB字符集
        :type DBCharset: str
        :param DBVersion: PostgreSQL内核版本
        :type DBVersion: str
        :param CreateTime: 实例创建时间
        :type CreateTime: str
        :param UpdateTime: 实例执行最后一次更新的时间
        :type UpdateTime: str
        :param ExpireTime: 实例到期时间
        :type ExpireTime: str
        :param IsolatedTime: 实例隔离时间
        :type IsolatedTime: str
        :param PayType: 计费模式，1、prepaid（包年包月,预付费）；2、postpaid（按量计费，后付费）
        :type PayType: str
        :param AutoRenew: 是否自动续费，1：自动续费，0：不自动续费
        :type AutoRenew: int
        :param DBInstanceNetInfo: 实例网络连接信息
        :type DBInstanceNetInfo: list of DBInstanceNetInfo
        """
        self.Region = None
        self.Zone = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.DBInstanceId = None
        self.DBInstanceName = None
        self.DBInstanceStatus = None
        self.DBInstanceMemory = None
        self.DBInstanceStorage = None
        self.DBInstanceCpu = None
        self.DBInstanceClass = None
        self.DBInstanceType = None
        self.DBInstanceVersion = None
        self.DBCharset = None
        self.DBVersion = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ExpireTime = None
        self.IsolatedTime = None
        self.PayType = None
        self.AutoRenew = None
        self.DBInstanceNetInfo = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DBInstanceId = params.get("DBInstanceId")
        self.DBInstanceName = params.get("DBInstanceName")
        self.DBInstanceStatus = params.get("DBInstanceStatus")
        self.DBInstanceMemory = params.get("DBInstanceMemory")
        self.DBInstanceStorage = params.get("DBInstanceStorage")
        self.DBInstanceCpu = params.get("DBInstanceCpu")
        self.DBInstanceClass = params.get("DBInstanceClass")
        self.DBInstanceType = params.get("DBInstanceType")
        self.DBInstanceVersion = params.get("DBInstanceVersion")
        self.DBCharset = params.get("DBCharset")
        self.DBVersion = params.get("DBVersion")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.IsolatedTime = params.get("IsolatedTime")
        self.PayType = params.get("PayType")
        self.AutoRenew = params.get("AutoRenew")
        if params.get("DBInstanceNetInfo") is not None:
            self.DBInstanceNetInfo = []
            for item in params.get("DBInstanceNetInfo"):
                obj = DBInstanceNetInfo()
                obj._deserialize(item)
                self.DBInstanceNetInfo.append(obj)


class DBInstanceNetInfo(AbstractModel):
    """描述实例的网络连接信息

    """

    def __init__(self):
        """
        :param Address: DNS域名
        :type Address: str
        :param Ip: Ip
        :type Ip: str
        :param Port: 连接Port地址
        :type Port: int
        :param NetType: 网络类型，1、inner（内网地址）；2、public（外网地址）
        :type NetType: str
        :param Status: 网络连接状态
        :type Status: str
        """
        self.Address = None
        self.Ip = None
        self.Port = None
        self.NetType = None
        self.Status = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.NetType = params.get("NetType")
        self.Status = params.get("Status")


class DescribeDBInstanceAttributeRequest(AbstractModel):
    """DescribeDBInstanceAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例ID。
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")


class DescribeDBInstanceAttributeResponse(AbstractModel):
    """DescribeDBInstanceAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param DBInstance: 实例详细信息。
        :type DBInstance: :class:`tencentcloud.postgres.v20170312.models.DBInstance`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DBInstance = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DBInstance") is not None:
            self.DBInstance = DBInstance()
            self.DBInstance._deserialize(params.get("DBInstance"))
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param PageSize: 每页显示数量，默认返回10条。
        :type PageSize: int
        :param PageNumber: 分页序号，从1开始。
        :type PageNumber: int
        :param Filters: 过滤条件，目前支持：db-instance-id、db-instance-name两种。
        :type Filters: list of Filter
        """
        self.PageSize = None
        self.PageNumber = None
        self.Filters = None


    def _deserialize(self, params):
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 查询到的实例数量。
        :type TotalCount: int
        :param DBInstanceSet: 实例详细信息集合。
        :type DBInstanceSet: list of DBInstance
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DBInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DBInstanceSet") is not None:
            self.DBInstanceSet = []
            for item in params.get("DBInstanceSet"):
                obj = DBInstance()
                obj._deserialize(item)
                self.DBInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProductConfigRequest(AbstractModel):
    """DescribeProductConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区名称
        :type Zone: str
        """
        self.Zone = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")


class DescribeProductConfigResponse(AbstractModel):
    """DescribeProductConfig返回参数结构体

    """

    def __init__(self):
        """
        :param SpecInfoList: 售卖规格列表。
        :type SpecInfoList: list of SpecInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.SpecInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpecInfoList") is not None:
            self.SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecInfo()
                obj._deserialize(item)
                self.SpecInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的结果数量。
        :type TotalCount: int
        :param RegionSet: 地域信息集合。
        :type RegionSet: list of RegionInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的结果数量。
        :type TotalCount: int
        :param ZoneSet: 可用区信息集合。
        :type ZoneSet: list of ZoneInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ZoneSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.ZoneSet.append(obj)
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称等
    * 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    * 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        """
        :param Name: 过滤键的名称。
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class InitDBInstancesRequest(AbstractModel):
    """InitDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceIdSet: 实例ID集合。
        :type DBInstanceIdSet: list of str
        :param AdminName: 实例根账号用户名。
        :type AdminName: str
        :param AdminPassword: 实例根账号用户名对应的密码。
        :type AdminPassword: str
        :param Charset: 实例字符集，目前只支持：UTF8、LATIN1。
        :type Charset: str
        """
        self.DBInstanceIdSet = None
        self.AdminName = None
        self.AdminPassword = None
        self.Charset = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.AdminName = params.get("AdminName")
        self.AdminPassword = params.get("AdminPassword")
        self.Charset = params.get("Charset")


class InitDBInstancesResponse(AbstractModel):
    """InitDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceIdSet: 实例ID集合。
        :type DBInstanceIdSet: list of str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DBInstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.RequestId = params.get("RequestId")


class InquiryPriceCreateDBInstancesRequest(AbstractModel):
    """InquiryPriceCreateDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。
        :type Zone: str
        :param SpecCode: 规格ID。该参数可以通过调用DescribeProductConfig接口的返回值中的SpecCode字段来获取。
        :type SpecCode: str
        :param Storage: 存储容量大小，单位：GB。
        :type Storage: int
        :param InstanceCount: 实例数量。目前最大数量不超过100，如需一次性创建更多实例，请联系客服支持。
        :type InstanceCount: int
        :param Period: 购买时长，单位：月。目前只支持1,2,3,4,5,6,7,8,9,10,11,12,24,36这些值。
        :type Period: int
        :param Pid: 计费ID。该参数可以通过调用DescribeProductConfig接口的返回值中的Pid字段来获取。
        :type Pid: int
        :param InstanceChargeType: 实例计费类型。目前只支持：PREPAID（预付费，即包年包月）。
        :type InstanceChargeType: str
        """
        self.Zone = None
        self.SpecCode = None
        self.Storage = None
        self.InstanceCount = None
        self.Period = None
        self.Pid = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.SpecCode = params.get("SpecCode")
        self.Storage = params.get("Storage")
        self.InstanceCount = params.get("InstanceCount")
        self.Period = params.get("Period")
        self.Pid = params.get("Pid")
        self.InstanceChargeType = params.get("InstanceChargeType")


class InquiryPriceCreateDBInstancesResponse(AbstractModel):
    """InquiryPriceCreateDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 原始价格，单位：分
        :type OriginalPrice: int
        :param Price: 折后价格，单位：分
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


class RegionInfo(AbstractModel):
    """描述地域的编码和状态等信息

    """

    def __init__(self):
        """
        :param Region: 该地域对应的英文名称
        :type Region: str
        :param RegionName: 该地域对应的中文名称
        :type RegionName: str
        :param RegionId: 该地域对应的数字编号
        :type RegionId: int
        :param RegionState: 可用状态，UNAVAILABLE表示不可用，AVAILABLE表示可用
        :type RegionState: str
        """
        self.Region = None
        self.RegionName = None
        self.RegionId = None
        self.RegionState = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.RegionState = params.get("RegionState")


class SpecInfo(AbstractModel):
    """描述某个地域下某个可用区的可售卖规格详细信息。

    """

    def __init__(self):
        """
        :param Region: 地域英文编码，对应RegionSet的Region字段
        :type Region: str
        :param Zone: 区域英文编码，对应ZoneSet的Zone字段
        :type Zone: str
        :param SpecItemInfoList: 规格详细信息列表
        :type SpecItemInfoList: list of SpecItemInfo
        """
        self.Region = None
        self.Zone = None
        self.SpecItemInfoList = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        if params.get("SpecItemInfoList") is not None:
            self.SpecItemInfoList = []
            for item in params.get("SpecItemInfoList"):
                obj = SpecItemInfo()
                obj._deserialize(item)
                self.SpecItemInfoList.append(obj)


class SpecItemInfo(AbstractModel):
    """描述一种规格的信息信息

    """

    def __init__(self):
        """
        :param SpecCode: 规格ID
        :type SpecCode: str
        :param Version: PostgreSQL的内核版本编号
        :type Version: str
        :param VersionName: 内核编号对应的完整版本名称
        :type VersionName: str
        :param Cpu: CPU核数
        :type Cpu: list of int non-negative
        :param Memory: 内存大小，单位：MB
        :type Memory: list of int non-negative
        :param MaxStorage: 该规格所支持最大存储容量，单位：GB
        :type MaxStorage: int
        :param MinStorage: 该规格所支持最小存储容量，单位：GB
        :type MinStorage: int
        :param Qps: 该规格的预估QPS
        :type Qps: int
        :param Pid: 该规格对应的计费ID
        :type Pid: int
        """
        self.SpecCode = None
        self.Version = None
        self.VersionName = None
        self.Cpu = None
        self.Memory = None
        self.MaxStorage = None
        self.MinStorage = None
        self.Qps = None
        self.Pid = None


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.Version = params.get("Version")
        self.VersionName = params.get("VersionName")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.MaxStorage = params.get("MaxStorage")
        self.MinStorage = params.get("MinStorage")
        self.Qps = params.get("Qps")
        self.Pid = params.get("Pid")


class ZoneInfo(AbstractModel):
    """描述可用区的编码和状态信息

    """

    def __init__(self):
        """
        :param Zone: 该可用区的英文名称
        :type Zone: str
        :param ZoneName: 该可用区的中文名称
        :type ZoneName: str
        :param ZoneId: 该可用区对应的数字编号
        :type ZoneId: int
        :param ZoneState: 可用状态，UNAVAILABLE表示不可用，AVAILABLE表示可用
        :type ZoneState: str
        """
        self.Zone = None
        self.ZoneName = None
        self.ZoneId = None
        self.ZoneState = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.ZoneId = params.get("ZoneId")
        self.ZoneState = params.get("ZoneState")