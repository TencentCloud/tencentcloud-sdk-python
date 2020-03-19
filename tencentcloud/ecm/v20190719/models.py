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


class Area(AbstractModel):
    """区域信息

    """

    def __init__(self):
        """
        :param AreaId: 区域ID
        :type AreaId: str
        :param AreaName: 区域名称
        :type AreaName: str
        """
        self.AreaId = None
        self.AreaName = None


    def _deserialize(self, params):
        self.AreaId = params.get("AreaId")
        self.AreaName = params.get("AreaName")


class City(AbstractModel):
    """城市信息

    """

    def __init__(self):
        """
        :param CityId: 城市ID
        :type CityId: str
        :param CityName: 城市名称
        :type CityName: str
        """
        self.CityId = None
        self.CityName = None


    def _deserialize(self, params):
        self.CityId = params.get("CityId")
        self.CityName = params.get("CityName")


class Country(AbstractModel):
    """国家信息

    """

    def __init__(self):
        """
        :param CountryId: 国家ID
        :type CountryId: str
        :param CountryName: 国家名称
        :type CountryName: str
        """
        self.CountryId = None
        self.CountryName = None


    def _deserialize(self, params):
        self.CountryId = params.get("CountryId")
        self.CountryName = params.get("CountryName")


class CreateModuleRequest(AbstractModel):
    """CreateModule请求参数结构体

    """

    def __init__(self):
        """
        :param ModuleName: 模块名称，如视频直播模块。限制：模块名称不得以空格开头，长度不得超过60个字符。
        :type ModuleName: str
        :param DefaultBandWidth: 默认带宽，单位：M。范围不得超过带宽上下限，详看DescribeConfig。
        :type DefaultBandWidth: int
        :param DefaultImageId: 默认镜像，如img-qsdf3ff2。
        :type DefaultImageId: str
        :param InstanceType: 机型ID。
        :type InstanceType: str
        :param DefaultSystemDiskSize: 默认系统盘大小，单位：G，默认大小为50G。范围不得超过系统盘上下限制，详看DescribeConfig。
        :type DefaultSystemDiskSize: int
        :param DefaultDataDiskSize: 默认数据盘大小，单位：G。范围不得超过数据盘范围大小，详看DescribeConfig。
        :type DefaultDataDiskSize: int
        """
        self.ModuleName = None
        self.DefaultBandWidth = None
        self.DefaultImageId = None
        self.InstanceType = None
        self.DefaultSystemDiskSize = None
        self.DefaultDataDiskSize = None


    def _deserialize(self, params):
        self.ModuleName = params.get("ModuleName")
        self.DefaultBandWidth = params.get("DefaultBandWidth")
        self.DefaultImageId = params.get("DefaultImageId")
        self.InstanceType = params.get("InstanceType")
        self.DefaultSystemDiskSize = params.get("DefaultSystemDiskSize")
        self.DefaultDataDiskSize = params.get("DefaultDataDiskSize")


class CreateModuleResponse(AbstractModel):
    """CreateModule返回参数结构体

    """

    def __init__(self):
        """
        :param ModuleId: 模块ID，创建模块成功后分配给该模块的ID。
        :type ModuleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ModuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.RequestId = params.get("RequestId")


class DeleteImageRequest(AbstractModel):
    """DeleteImage请求参数结构体

    """

    def __init__(self):
        """
        :param ImageIDSet: 镜像ID列表。
        :type ImageIDSet: list of str
        """
        self.ImageIDSet = None


    def _deserialize(self, params):
        self.ImageIDSet = params.get("ImageIDSet")


class DeleteImageResponse(AbstractModel):
    """DeleteImage返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteModuleRequest(AbstractModel):
    """DeleteModule请求参数结构体

    """

    def __init__(self):
        """
        :param ModuleId: 模块ID。如：es-qn46snq8
        :type ModuleId: str
        """
        self.ModuleId = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")


class DeleteModuleResponse(AbstractModel):
    """DeleteModule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeBaseOverviewRequest(AbstractModel):
    """DescribeBaseOverview请求参数结构体

    """


class DescribeBaseOverviewResponse(AbstractModel):
    """DescribeBaseOverview返回参数结构体

    """

    def __init__(self):
        """
        :param ModuleNum: 模块数量，单位：个
        :type ModuleNum: int
        :param NodeNum: 节点数量，单位：个
        :type NodeNum: int
        :param VcpuNum: cpu核数，单位：个
        :type VcpuNum: int
        :param MemoryNum: 内存大小，单位：G
        :type MemoryNum: int
        :param StorageNum: 硬盘大小，单位：G
        :type StorageNum: int
        :param NetworkNum: 昨日网络峰值,单位：M
        :type NetworkNum: int
        :param InstanceNum: 实例数量，单位：台
        :type InstanceNum: int
        :param RunningNum: 运行中数量，单位：台
        :type RunningNum: int
        :param IsolationNum: 安全隔离数量，单位：台
        :type IsolationNum: int
        :param ExpiredNum: 过期实例数量，单位：台
        :type ExpiredNum: int
        :param WillExpireNum: 即将过期实例数量，单位：台
        :type WillExpireNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ModuleNum = None
        self.NodeNum = None
        self.VcpuNum = None
        self.MemoryNum = None
        self.StorageNum = None
        self.NetworkNum = None
        self.InstanceNum = None
        self.RunningNum = None
        self.IsolationNum = None
        self.ExpiredNum = None
        self.WillExpireNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModuleNum = params.get("ModuleNum")
        self.NodeNum = params.get("NodeNum")
        self.VcpuNum = params.get("VcpuNum")
        self.MemoryNum = params.get("MemoryNum")
        self.StorageNum = params.get("StorageNum")
        self.NetworkNum = params.get("NetworkNum")
        self.InstanceNum = params.get("InstanceNum")
        self.RunningNum = params.get("RunningNum")
        self.IsolationNum = params.get("IsolationNum")
        self.ExpiredNum = params.get("ExpiredNum")
        self.WillExpireNum = params.get("WillExpireNum")
        self.RequestId = params.get("RequestId")


class DescribeConfigRequest(AbstractModel):
    """DescribeConfig请求参数结构体

    """


class DescribeConfigResponse(AbstractModel):
    """DescribeConfig返回参数结构体

    """

    def __init__(self):
        """
        :param NetworkStorageRange: 网络带宽硬盘大小的范围信息。
        :type NetworkStorageRange: :class:`tencentcloud.ecm.v20190719.models.NetworkStorageRange`
        :param ImageWhiteSet: 镜像操作系统白名单
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageWhiteSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NetworkStorageRange = None
        self.ImageWhiteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkStorageRange") is not None:
            self.NetworkStorageRange = NetworkStorageRange()
            self.NetworkStorageRange._deserialize(params.get("NetworkStorageRange"))
        self.ImageWhiteSet = params.get("ImageWhiteSet")
        self.RequestId = params.get("RequestId")


class DescribeImageRequest(AbstractModel):
    """DescribeImage请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件，每次请求的Filters的上限为10，详细的过滤条件如下：
image-id - String - 是否必填： 否 - （过滤条件）按照镜像ID进行过滤
image-type - String - 是否必填： 否 - （过滤条件）按照镜像类型进行过滤。取值范围：
PRIVATE_IMAGE: 私有镜像 (本帐户创建的镜像) 
PUBLIC_IMAGE: 公共镜像 (腾讯云官方镜像)
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeImageResponse(AbstractModel):
    """DescribeImage返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 镜像总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ImageSet: 镜像数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageSet: list of Image
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ImageSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImageSet") is not None:
            self.ImageSet = []
            for item in params.get("ImageSet"):
                obj = Image()
                obj._deserialize(item)
                self.ImageSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceTypeConfigRequest(AbstractModel):
    """DescribeInstanceTypeConfig请求参数结构体

    """


class DescribeInstanceTypeConfigResponse(AbstractModel):
    """DescribeInstanceTypeConfig返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数
        :type TotalCount: int
        :param InstanceTypeConfigSet: 机型配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceTypeConfigSet: list of InstanceTypeConfig
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceTypeConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceTypeConfigSet") is not None:
            self.InstanceTypeConfigSet = []
            for item in params.get("InstanceTypeConfigSet"):
                obj = InstanceTypeConfig()
                obj._deserialize(item)
                self.InstanceTypeConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesDeniedActionsRequest(AbstractModel):
    """DescribeInstancesDeniedActions请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 无
        :type InstanceIdSet: list of str
        """
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")


class DescribeInstancesDeniedActionsResponse(AbstractModel):
    """DescribeInstancesDeniedActions返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceOperatorSet: 实例对应的禁止操作
        :type InstanceOperatorSet: list of InstanceOperator
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceOperatorSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceOperatorSet") is not None:
            self.InstanceOperatorSet = []
            for item in params.get("InstanceOperatorSet"):
                obj = InstanceOperator()
                obj._deserialize(item)
                self.InstanceOperatorSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件。
zone      String      是否必填：否     （过滤条件）按照可用区中文名过滤,支持模糊匹配。
module-id      String      是否必填：否     （过滤条件）按照模块ID过滤。
instance-id      String      是否必填：否      （过滤条件）按照实例ID过滤。
instance-name      String      是否必填：否      （过滤条件）按照实例名称过滤,支持模糊匹配。
ip-address      String      是否必填：否      （过滤条件）按照实例的内网/公网IP过滤。
instance-uuid   string 是否必填：否 （过滤条件）按照uuid过滤实例列表。
instance-state  string  是否必填：否 （过滤条件）按照实例状态更新实例列表。
internet-service-provider      String      是否必填：否      （过滤条件）按照实例公网IP所属的运营商进行过滤。
tag-key      String      是否必填：否      （过滤条件）按照标签键进行过滤。
tag:tag-key      String      是否必填：否      （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。
若不传Filters参数则表示查询所有相关的实例信息。
单次请求的Filter.Values的上限为5。
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为20(如果查询结果数目大于等于20)，最大值为100。
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的实例相关信息列表的长度。
        :type TotalCount: int
        :param InstanceSet: 返回的实例相关信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceSet: list of Instance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeModuleDetailRequest(AbstractModel):
    """DescribeModuleDetail请求参数结构体

    """

    def __init__(self):
        """
        :param ModuleId: 模块ID，如em-qn46snq8。
        :type ModuleId: str
        """
        self.ModuleId = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")


class DescribeModuleDetailResponse(AbstractModel):
    """DescribeModuleDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块的详细信息，详细见数据结构中的ModuleInfo。
注意：此字段可能返回 null，表示取不到有效值。
        :type Module: :class:`tencentcloud.ecm.v20190719.models.Module`
        :param ModuleCounter: 模块的统计信息，详细见数据结构中的ModuleCounterInfo。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModuleCounter: :class:`tencentcloud.ecm.v20190719.models.ModuleCounter`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Module = None
        self.ModuleCounter = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Module") is not None:
            self.Module = Module()
            self.Module._deserialize(params.get("Module"))
        if params.get("ModuleCounter") is not None:
            self.ModuleCounter = ModuleCounter()
            self.ModuleCounter._deserialize(params.get("ModuleCounter"))
        self.RequestId = params.get("RequestId")


class DescribeModuleRequest(AbstractModel):
    """DescribeModule请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件。
module-name - string - 是否必填：否 - （过滤条件）按照模块名称过滤。
module-id - string - 是否必填：否 - （过滤条件）按照模块ID过滤。
每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeModuleResponse(AbstractModel):
    """DescribeModule返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的模块数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ModuleItemSet: 模块详情信息的列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModuleItemSet: list of ModuleItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ModuleItemSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ModuleItemSet") is not None:
            self.ModuleItemSet = []
            for item in params.get("ModuleItemSet"):
                obj = ModuleItem()
                obj._deserialize(item)
                self.ModuleItemSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNodeRequest(AbstractModel):
    """DescribeNode请求参数结构体

    """


class DescribeNodeResponse(AbstractModel):
    """DescribeNode返回参数结构体

    """

    def __init__(self):
        """
        :param NodeSet: 节点详细信息的列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeSet: list of Node
        :param TotalCount: 所有的节点数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NodeSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NodeSet") is not None:
            self.NodeSet = []
            for item in params.get("NodeSet"):
                obj = Node()
                obj._deserialize(item)
                self.NodeSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePeakBaseOverviewRequest(AbstractModel):
    """DescribePeakBaseOverview请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间（xxxx-xx-xx）如2019-08-14，默认为一周之前的日期。
        :type StartTime: str
        :param EndTime: 结束时间（xxxx-xx-xx）如2019-08-14，默认为昨天。
        :type EndTime: str
        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribePeakBaseOverviewResponse(AbstractModel):
    """DescribePeakBaseOverview返回参数结构体

    """

    def __init__(self):
        """
        :param PeakFamilyInfoSet: 基础峰值列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type PeakFamilyInfoSet: list of PeakFamilyInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PeakFamilyInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PeakFamilyInfoSet") is not None:
            self.PeakFamilyInfoSet = []
            for item in params.get("PeakFamilyInfoSet"):
                obj = PeakFamilyInfo()
                obj._deserialize(item)
                self.PeakFamilyInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePeakNetworkOverviewRequest(AbstractModel):
    """DescribePeakNetworkOverview请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间（xxxx-xx-xx）如2019-08-14，默认为一周之前的日期。
        :type StartTime: str
        :param EndTime: 结束时间（xxxx-xx-xx）如2019-08-14，默认为昨天。
        :type EndTime: str
        :param Filters: 过滤条件。
region    String      是否必填：否     （过滤条件）按照region过滤,不支持模糊匹配。
        :type Filters: list of Filter
        """
        self.StartTime = None
        self.EndTime = None
        self.Filters = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribePeakNetworkOverviewResponse(AbstractModel):
    """DescribePeakNetworkOverview返回参数结构体

    """

    def __init__(self):
        """
        :param PeakNetworkRegionSet: 网络峰值数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type PeakNetworkRegionSet: list of PeakNetworkRegionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PeakNetworkRegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PeakNetworkRegionSet") is not None:
            self.PeakNetworkRegionSet = []
            for item in params.get("PeakNetworkRegionSet"):
                obj = PeakNetworkRegionInfo()
                obj._deserialize(item)
                self.PeakNetworkRegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DiskInfo(AbstractModel):
    """磁盘信息

    """

    def __init__(self):
        """
        :param DiskType: 磁盘类型：LOCAL_BASIC
        :type DiskType: str
        :param DiskId: 磁盘ID
        :type DiskId: str
        :param DiskSize: 磁盘大小（GB）
        :type DiskSize: int
        """
        self.DiskType = None
        self.DiskId = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")


class EnhancedService(AbstractModel):
    """增强服务

    """

    def __init__(self):
        """
        :param SecurityService: 是否开启云镜服务。
        :type SecurityService: :class:`tencentcloud.ecm.v20190719.models.RunSecurityServiceEnabled`
        :param MonitorService: 是否开启云监控服务。
        :type MonitorService: :class:`tencentcloud.ecm.v20190719.models.RunMonitorServiceEnabled`
        """
        self.SecurityService = None
        self.MonitorService = None


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self.SecurityService = RunSecurityServiceEnabled()
            self.SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self.MonitorService = RunMonitorServiceEnabled()
            self.MonitorService._deserialize(params.get("MonitorService"))


class Filter(AbstractModel):
    """过滤器Filter;由Name和ValueSet组成，是string的key和字符串数组的value

    """

    def __init__(self):
        """
        :param Name: 过滤字段名称
        :type Name: str
        :param Values: 过滤字段内容数组
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class ISP(AbstractModel):
    """运营商信息

    """

    def __init__(self):
        """
        :param ISPId: 运营商ID
        :type ISPId: str
        :param ISPName: 运营商名称
        :type ISPName: str
        """
        self.ISPId = None
        self.ISPName = None


    def _deserialize(self, params):
        self.ISPId = params.get("ISPId")
        self.ISPName = params.get("ISPName")


class ISPCounter(AbstractModel):
    """运行商统计信息

    """

    def __init__(self):
        """
        :param ProviderName: 运营商名称
        :type ProviderName: str
        :param ProviderNodeNum: 节点数量
        :type ProviderNodeNum: int
        :param ProvederInstanceNum: 实例数量
        :type ProvederInstanceNum: int
        :param ZoneInstanceInfoSet: Zone实例信息结构体数组
        :type ZoneInstanceInfoSet: list of ZoneInstanceInfo
        """
        self.ProviderName = None
        self.ProviderNodeNum = None
        self.ProvederInstanceNum = None
        self.ZoneInstanceInfoSet = None


    def _deserialize(self, params):
        self.ProviderName = params.get("ProviderName")
        self.ProviderNodeNum = params.get("ProviderNodeNum")
        self.ProvederInstanceNum = params.get("ProvederInstanceNum")
        if params.get("ZoneInstanceInfoSet") is not None:
            self.ZoneInstanceInfoSet = []
            for item in params.get("ZoneInstanceInfoSet"):
                obj = ZoneInstanceInfo()
                obj._deserialize(item)
                self.ZoneInstanceInfoSet.append(obj)


class Image(AbstractModel):
    """镜像信息

    """

    def __init__(self):
        """
        :param ImageId: 镜像ID
        :type ImageId: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param ImageState: 镜像状态
        :type ImageState: str
        :param ImageType: 镜像类型
        :type ImageType: str
        :param ImageOsName: 操作系统名称
        :type ImageOsName: str
        :param ImageDescription: 镜像描述
        :type ImageDescription: str
        :param ImageCreateTime: 镜像导入时间
        :type ImageCreateTime: str
        :param Architecture: 操作系统位数
        :type Architecture: str
        :param OsType: 操作系统类型
        :type OsType: str
        :param OsVersion: 操作系统版本
        :type OsVersion: str
        :param Platform: 操作系统平台
        :type Platform: str
        :param ImageOwner: 镜像所有者
        :type ImageOwner: int
        :param ImageSize: 镜像大小。单位：GB
        :type ImageSize: int
        :param SrcImage: 镜像来源信息
        :type SrcImage: :class:`tencentcloud.ecm.v20190719.models.SrcImage`
        """
        self.ImageId = None
        self.ImageName = None
        self.ImageState = None
        self.ImageType = None
        self.ImageOsName = None
        self.ImageDescription = None
        self.ImageCreateTime = None
        self.Architecture = None
        self.OsType = None
        self.OsVersion = None
        self.Platform = None
        self.ImageOwner = None
        self.ImageSize = None
        self.SrcImage = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ImageState = params.get("ImageState")
        self.ImageType = params.get("ImageType")
        self.ImageOsName = params.get("ImageOsName")
        self.ImageDescription = params.get("ImageDescription")
        self.ImageCreateTime = params.get("ImageCreateTime")
        self.Architecture = params.get("Architecture")
        self.OsType = params.get("OsType")
        self.OsVersion = params.get("OsVersion")
        self.Platform = params.get("Platform")
        self.ImageOwner = params.get("ImageOwner")
        self.ImageSize = params.get("ImageSize")
        if params.get("SrcImage") is not None:
            self.SrcImage = SrcImage()
            self.SrcImage._deserialize(params.get("SrcImage"))


class Instance(AbstractModel):
    """用于描述实例相关的信息。

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param InstanceName: 实例名称，如ens-34241f3s。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param InstanceState: 实例状态。取值范围：
PENDING：表示创建中
LAUNCH_FAILED：表示创建失败
RUNNING：表示运行中
STOPPED：表示关机
STARTING：表示开机中
STOPPING：表示关机中
REBOOTING：表示重启中
SHUTDOWN：表示停止待销毁
TERMINATING：表示销毁中。
        :type InstanceState: str
        :param Image: 实例当前使用的镜像的信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: :class:`tencentcloud.ecm.v20190719.models.Image`
        :param SimpleModule: 实例当前所属的模块简要信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SimpleModule: :class:`tencentcloud.ecm.v20190719.models.SimpleModule`
        :param Position: 实例所在的位置相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: :class:`tencentcloud.ecm.v20190719.models.Position`
        :param Internet: 实例的网络相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Internet: :class:`tencentcloud.ecm.v20190719.models.Internet`
        :param InstanceTypeConfig: 实例的配置相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceTypeConfig`
        :param CreateTime: 实例的创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param TagSet: 实例的标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSet: list of Tag
        :param LatestOperation: 实例最后一次操作。
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperation: str
        :param LatestOperationState: 实例最后一次操作结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperationState: str
        :param RestrictState: 实例业务状态。取值范围：
NORMAL：表示正常状态的实例
EXPIRED：表示过期的实例
PROTECTIVELY_ISOLATED：表示被安全隔离的实例。
注意：此字段可能返回 null，表示取不到有效值。
        :type RestrictState: str
        :param SystemDiskSize: 系统盘大小，单位GB。
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemDiskSize: int
        :param DataDiskSize: 数据盘大小，单位GB。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDiskSize: int
        :param UUID: UUID
注意：此字段可能返回 null，表示取不到有效值。
        :type UUID: str
        :param PayMode: 付费方式。
    0为后付费。
    1为预付费。
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: int
        :param ExpireTime: 过期时间。格式为yyyy-mm-dd HH:mm:ss。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param IsolatedTime: 隔离时间。格式为yyyy-mm-dd HH:mm:ss。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedTime: str
        :param RenewFlag: 是否自动续费。
      0为不自动续费。
      1为自动续费。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param ExpireState: 过期状态。
    NORMAL 表示机器运行正常。
    WILL_EXPIRE 表示即将过期。
    EXPIRED 表示已过期。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireState: str
        :param SystemDisk: 系统盘信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.DiskInfo`
        :param DataDisks: 数据盘信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDisks: list of DiskInfo
        """
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceState = None
        self.Image = None
        self.SimpleModule = None
        self.Position = None
        self.Internet = None
        self.InstanceTypeConfig = None
        self.CreateTime = None
        self.TagSet = None
        self.LatestOperation = None
        self.LatestOperationState = None
        self.RestrictState = None
        self.SystemDiskSize = None
        self.DataDiskSize = None
        self.UUID = None
        self.PayMode = None
        self.ExpireTime = None
        self.IsolatedTime = None
        self.RenewFlag = None
        self.ExpireState = None
        self.SystemDisk = None
        self.DataDisks = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceState = params.get("InstanceState")
        if params.get("Image") is not None:
            self.Image = Image()
            self.Image._deserialize(params.get("Image"))
        if params.get("SimpleModule") is not None:
            self.SimpleModule = SimpleModule()
            self.SimpleModule._deserialize(params.get("SimpleModule"))
        if params.get("Position") is not None:
            self.Position = Position()
            self.Position._deserialize(params.get("Position"))
        if params.get("Internet") is not None:
            self.Internet = Internet()
            self.Internet._deserialize(params.get("Internet"))
        if params.get("InstanceTypeConfig") is not None:
            self.InstanceTypeConfig = InstanceTypeConfig()
            self.InstanceTypeConfig._deserialize(params.get("InstanceTypeConfig"))
        self.CreateTime = params.get("CreateTime")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.LatestOperation = params.get("LatestOperation")
        self.LatestOperationState = params.get("LatestOperationState")
        self.RestrictState = params.get("RestrictState")
        self.SystemDiskSize = params.get("SystemDiskSize")
        self.DataDiskSize = params.get("DataDiskSize")
        self.UUID = params.get("UUID")
        self.PayMode = params.get("PayMode")
        self.ExpireTime = params.get("ExpireTime")
        self.IsolatedTime = params.get("IsolatedTime")
        self.RenewFlag = params.get("RenewFlag")
        self.ExpireState = params.get("ExpireState")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = DiskInfo()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DiskInfo()
                obj._deserialize(item)
                self.DataDisks.append(obj)


class InstanceFamilyConfig(AbstractModel):
    """机型族配置

    """

    def __init__(self):
        """
        :param InstanceFamilyName: 机型名称
        :type InstanceFamilyName: str
        :param InstanceFamily: 机型ID
        :type InstanceFamily: str
        """
        self.InstanceFamilyName = None
        self.InstanceFamily = None


    def _deserialize(self, params):
        self.InstanceFamilyName = params.get("InstanceFamilyName")
        self.InstanceFamily = params.get("InstanceFamily")


class InstanceFamilyTypeConfig(AbstractModel):
    """实例系列类型配置

    """

    def __init__(self):
        """
        :param InstanceFamilyType: 实例机型系列类型Id
        :type InstanceFamilyType: str
        :param InstanceFamilyTypeName: 实例机型系列类型名称
        :type InstanceFamilyTypeName: str
        """
        self.InstanceFamilyType = None
        self.InstanceFamilyTypeName = None


    def _deserialize(self, params):
        self.InstanceFamilyType = params.get("InstanceFamilyType")
        self.InstanceFamilyTypeName = params.get("InstanceFamilyTypeName")


class InstanceOperator(AbstractModel):
    """实例可执行操作

    """

    def __init__(self):
        """
        :param InstanceId: 实例id
        :type InstanceId: str
        :param DeniedActions: 实例禁止的操作
注意：此字段可能返回 null，表示取不到有效值。
        :type DeniedActions: list of OperatorAction
        """
        self.InstanceId = None
        self.DeniedActions = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DeniedActions") is not None:
            self.DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = OperatorAction()
                obj._deserialize(item)
                self.DeniedActions.append(obj)


class InstanceTypeConfig(AbstractModel):
    """机型配置

    """

    def __init__(self):
        """
        :param InstanceFamilyConfig: 机型族配置信息
        :type InstanceFamilyConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyConfig`
        :param InstanceType: 机型
        :type InstanceType: str
        :param Vcpu: CPU核数
        :type Vcpu: int
        :param Memory: 内存大小
        :type Memory: int
        :param Frequency: 主频
        :type Frequency: str
        :param CpuModelName: 处理器型号
        :type CpuModelName: str
        :param InstanceFamilyTypeConfig: 机型族类别配置信息
        :type InstanceFamilyTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyTypeConfig`
        :param ExtInfo: 机型额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtInfo: str
        """
        self.InstanceFamilyConfig = None
        self.InstanceType = None
        self.Vcpu = None
        self.Memory = None
        self.Frequency = None
        self.CpuModelName = None
        self.InstanceFamilyTypeConfig = None
        self.ExtInfo = None


    def _deserialize(self, params):
        if params.get("InstanceFamilyConfig") is not None:
            self.InstanceFamilyConfig = InstanceFamilyConfig()
            self.InstanceFamilyConfig._deserialize(params.get("InstanceFamilyConfig"))
        self.InstanceType = params.get("InstanceType")
        self.Vcpu = params.get("Vcpu")
        self.Memory = params.get("Memory")
        self.Frequency = params.get("Frequency")
        self.CpuModelName = params.get("CpuModelName")
        if params.get("InstanceFamilyTypeConfig") is not None:
            self.InstanceFamilyTypeConfig = InstanceFamilyTypeConfig()
            self.InstanceFamilyTypeConfig._deserialize(params.get("InstanceFamilyTypeConfig"))
        self.ExtInfo = params.get("ExtInfo")


class Internet(AbstractModel):
    """实例的网络相关信息。

    """

    def __init__(self):
        """
        :param PrivateIPAddressSet: 实例的内网相关信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIPAddressSet: list of PrivateIPAddressInfo
        :param PublicIPAddressSet: 实例的公网相关信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIPAddressSet: list of PublicIPAddressInfo
        """
        self.PrivateIPAddressSet = None
        self.PublicIPAddressSet = None


    def _deserialize(self, params):
        if params.get("PrivateIPAddressSet") is not None:
            self.PrivateIPAddressSet = []
            for item in params.get("PrivateIPAddressSet"):
                obj = PrivateIPAddressInfo()
                obj._deserialize(item)
                self.PrivateIPAddressSet.append(obj)
        if params.get("PublicIPAddressSet") is not None:
            self.PublicIPAddressSet = []
            for item in params.get("PublicIPAddressSet"):
                obj = PublicIPAddressInfo()
                obj._deserialize(item)
                self.PublicIPAddressSet.append(obj)


class ModifyInstancesAttributeRequest(AbstractModel):
    """ModifyInstancesAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待修改的实例ID列表。在单次请求的过程中，请求实例数上限为100。
        :type InstanceIdSet: list of str
        :param InstanceName: 修改成功后显示的实例名称，不得超过60个字符，不传则名称显示为空。
        :type InstanceName: str
        """
        self.InstanceIdSet = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.InstanceName = params.get("InstanceName")


class ModifyInstancesAttributeResponse(AbstractModel):
    """ModifyInstancesAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleImageRequest(AbstractModel):
    """ModifyModuleImage请求参数结构体

    """

    def __init__(self):
        """
        :param DefaultImageId: 默认镜像ID
        :type DefaultImageId: str
        :param ModuleId: 模块ID
        :type ModuleId: str
        """
        self.DefaultImageId = None
        self.ModuleId = None


    def _deserialize(self, params):
        self.DefaultImageId = params.get("DefaultImageId")
        self.ModuleId = params.get("ModuleId")


class ModifyModuleImageResponse(AbstractModel):
    """ModifyModuleImage返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleNameRequest(AbstractModel):
    """ModifyModuleName请求参数结构体

    """

    def __init__(self):
        """
        :param ModuleId: 模块ID。
        :type ModuleId: str
        :param ModuleName: 模块名称。
        :type ModuleName: str
        """
        self.ModuleId = None
        self.ModuleName = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.ModuleName = params.get("ModuleName")


class ModifyModuleNameResponse(AbstractModel):
    """ModifyModuleName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleNetworkRequest(AbstractModel):
    """ModifyModuleNetwork请求参数结构体

    """

    def __init__(self):
        """
        :param ModuleId: 模块Id
        :type ModuleId: str
        :param DefaultBandwidth: 默认带宽上限
        :type DefaultBandwidth: int
        """
        self.ModuleId = None
        self.DefaultBandwidth = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.DefaultBandwidth = params.get("DefaultBandwidth")


class ModifyModuleNetworkResponse(AbstractModel):
    """ModifyModuleNetwork返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Module(AbstractModel):
    """模块信息

    """

    def __init__(self):
        """
        :param ModuleId: 模块Id
        :type ModuleId: str
        :param ModuleName: 模块名称
        :type ModuleName: str
        :param ModuleState: 模块状态：
NORMAL：正常
DELETING：删除中 
DELETEFAILED：删除失败
        :type ModuleState: str
        :param DefaultSystemDiskSize: 默认系统盘大小
        :type DefaultSystemDiskSize: int
        :param DefaultDataDiskSize: 默认数据盘大小
        :type DefaultDataDiskSize: int
        :param InstanceTypeConfig: 默认机型
        :type InstanceTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceTypeConfig`
        :param DefaultImage: 默认镜像
        :type DefaultImage: :class:`tencentcloud.ecm.v20190719.models.Image`
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param DefaultBandwidth: 默认带宽
        :type DefaultBandwidth: int
        """
        self.ModuleId = None
        self.ModuleName = None
        self.ModuleState = None
        self.DefaultSystemDiskSize = None
        self.DefaultDataDiskSize = None
        self.InstanceTypeConfig = None
        self.DefaultImage = None
        self.CreateTime = None
        self.DefaultBandwidth = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.ModuleName = params.get("ModuleName")
        self.ModuleState = params.get("ModuleState")
        self.DefaultSystemDiskSize = params.get("DefaultSystemDiskSize")
        self.DefaultDataDiskSize = params.get("DefaultDataDiskSize")
        if params.get("InstanceTypeConfig") is not None:
            self.InstanceTypeConfig = InstanceTypeConfig()
            self.InstanceTypeConfig._deserialize(params.get("InstanceTypeConfig"))
        if params.get("DefaultImage") is not None:
            self.DefaultImage = Image()
            self.DefaultImage._deserialize(params.get("DefaultImage"))
        self.CreateTime = params.get("CreateTime")
        self.DefaultBandwidth = params.get("DefaultBandwidth")


class ModuleCounter(AbstractModel):
    """节点统计数据

    """

    def __init__(self):
        """
        :param ISPCounterSet: 运营商统计信息列表
        :type ISPCounterSet: list of ISPCounter
        :param ProvinceNum: 省份数量
        :type ProvinceNum: int
        :param CityNum: 城市数量
        :type CityNum: int
        :param NodeNum: 节点数量
        :type NodeNum: int
        :param InstanceNum: 实例数量
        :type InstanceNum: int
        """
        self.ISPCounterSet = None
        self.ProvinceNum = None
        self.CityNum = None
        self.NodeNum = None
        self.InstanceNum = None


    def _deserialize(self, params):
        if params.get("ISPCounterSet") is not None:
            self.ISPCounterSet = []
            for item in params.get("ISPCounterSet"):
                obj = ISPCounter()
                obj._deserialize(item)
                self.ISPCounterSet.append(obj)
        self.ProvinceNum = params.get("ProvinceNum")
        self.CityNum = params.get("CityNum")
        self.NodeNum = params.get("NodeNum")
        self.InstanceNum = params.get("InstanceNum")


class ModuleItem(AbstractModel):
    """模块列表Item信息

    """

    def __init__(self):
        """
        :param NodeInstanceNum: 节点实例统计信息
        :type NodeInstanceNum: :class:`tencentcloud.ecm.v20190719.models.NodeInstanceNum`
        :param Module: 模块信息
        :type Module: :class:`tencentcloud.ecm.v20190719.models.Module`
        """
        self.NodeInstanceNum = None
        self.Module = None


    def _deserialize(self, params):
        if params.get("NodeInstanceNum") is not None:
            self.NodeInstanceNum = NodeInstanceNum()
            self.NodeInstanceNum._deserialize(params.get("NodeInstanceNum"))
        if params.get("Module") is not None:
            self.Module = Module()
            self.Module._deserialize(params.get("Module"))


class NetworkStorageRange(AbstractModel):
    """网络硬盘上下限数据

    """

    def __init__(self):
        """
        :param MaxBandwidth: 网络带宽上限
        :type MaxBandwidth: int
        :param MaxSystemDiskSize: 数据盘上限
        :type MaxSystemDiskSize: int
        :param MinBandwidth: 网络带宽下限
        :type MinBandwidth: int
        :param MinSystemDiskSize: 数据盘下限
        :type MinSystemDiskSize: int
        :param MaxDataDiskSize: 最大数据盘大小
        :type MaxDataDiskSize: int
        :param MinDataDiskSize: 最小数据盘大小
        :type MinDataDiskSize: int
        :param SuggestBandwidth: 建议带宽
        :type SuggestBandwidth: int
        :param SuggestDataDiskSize: 建议硬盘大小
        :type SuggestDataDiskSize: int
        :param SuggestSystemDiskSize: 建议系统盘大小
        :type SuggestSystemDiskSize: int
        :param MaxVcpu: Cpu核数峰值
        :type MaxVcpu: int
        :param MinVcpu: Cpu核最小值
        :type MinVcpu: int
        :param MaxVcpuPerReq: 单次请求最大cpu核数
        :type MaxVcpuPerReq: int
        :param PerBandwidth: 带宽步长
        :type PerBandwidth: int
        :param PerDataDisk: 数据盘步长
        :type PerDataDisk: int
        :param MaxModuleNum: 总模块数量
        :type MaxModuleNum: int
        """
        self.MaxBandwidth = None
        self.MaxSystemDiskSize = None
        self.MinBandwidth = None
        self.MinSystemDiskSize = None
        self.MaxDataDiskSize = None
        self.MinDataDiskSize = None
        self.SuggestBandwidth = None
        self.SuggestDataDiskSize = None
        self.SuggestSystemDiskSize = None
        self.MaxVcpu = None
        self.MinVcpu = None
        self.MaxVcpuPerReq = None
        self.PerBandwidth = None
        self.PerDataDisk = None
        self.MaxModuleNum = None


    def _deserialize(self, params):
        self.MaxBandwidth = params.get("MaxBandwidth")
        self.MaxSystemDiskSize = params.get("MaxSystemDiskSize")
        self.MinBandwidth = params.get("MinBandwidth")
        self.MinSystemDiskSize = params.get("MinSystemDiskSize")
        self.MaxDataDiskSize = params.get("MaxDataDiskSize")
        self.MinDataDiskSize = params.get("MinDataDiskSize")
        self.SuggestBandwidth = params.get("SuggestBandwidth")
        self.SuggestDataDiskSize = params.get("SuggestDataDiskSize")
        self.SuggestSystemDiskSize = params.get("SuggestSystemDiskSize")
        self.MaxVcpu = params.get("MaxVcpu")
        self.MinVcpu = params.get("MinVcpu")
        self.MaxVcpuPerReq = params.get("MaxVcpuPerReq")
        self.PerBandwidth = params.get("PerBandwidth")
        self.PerDataDisk = params.get("PerDataDisk")
        self.MaxModuleNum = params.get("MaxModuleNum")


class Node(AbstractModel):
    """节点信息

    """

    def __init__(self):
        """
        :param ZoneInfo: zone信息
        :type ZoneInfo: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        :param Country: 国家信息
        :type Country: :class:`tencentcloud.ecm.v20190719.models.Country`
        :param Area: 区域信息
        :type Area: :class:`tencentcloud.ecm.v20190719.models.Area`
        :param Province: 省份信息
        :type Province: :class:`tencentcloud.ecm.v20190719.models.Province`
        :param City: 城市信息
        :type City: :class:`tencentcloud.ecm.v20190719.models.City`
        :param RegionInfo: Region信息
        :type RegionInfo: :class:`tencentcloud.ecm.v20190719.models.RegionInfo`
        :param ISPSet: 运营商列表
        :type ISPSet: list of ISP
        :param ISPNum: 运营商数量
        :type ISPNum: int
        """
        self.ZoneInfo = None
        self.Country = None
        self.Area = None
        self.Province = None
        self.City = None
        self.RegionInfo = None
        self.ISPSet = None
        self.ISPNum = None


    def _deserialize(self, params):
        if params.get("ZoneInfo") is not None:
            self.ZoneInfo = ZoneInfo()
            self.ZoneInfo._deserialize(params.get("ZoneInfo"))
        if params.get("Country") is not None:
            self.Country = Country()
            self.Country._deserialize(params.get("Country"))
        if params.get("Area") is not None:
            self.Area = Area()
            self.Area._deserialize(params.get("Area"))
        if params.get("Province") is not None:
            self.Province = Province()
            self.Province._deserialize(params.get("Province"))
        if params.get("City") is not None:
            self.City = City()
            self.City._deserialize(params.get("City"))
        if params.get("RegionInfo") is not None:
            self.RegionInfo = RegionInfo()
            self.RegionInfo._deserialize(params.get("RegionInfo"))
        if params.get("ISPSet") is not None:
            self.ISPSet = []
            for item in params.get("ISPSet"):
                obj = ISP()
                obj._deserialize(item)
                self.ISPSet.append(obj)
        self.ISPNum = params.get("ISPNum")


class NodeInstanceNum(AbstractModel):
    """节点实例数量信息

    """

    def __init__(self):
        """
        :param NodeNum: 节点数量
        :type NodeNum: int
        :param InstanceNum: 实例数量
        :type InstanceNum: int
        """
        self.NodeNum = None
        self.InstanceNum = None


    def _deserialize(self, params):
        self.NodeNum = params.get("NodeNum")
        self.InstanceNum = params.get("InstanceNum")


class OperatorAction(AbstractModel):
    """操作Action

    """

    def __init__(self):
        """
        :param Action: 可执行操作
        :type Action: str
        :param Code: 编码Code
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param Message: 具体信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self.Action = None
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Code = params.get("Code")
        self.Message = params.get("Message")


class PeakBase(AbstractModel):
    """峰值信息

    """

    def __init__(self):
        """
        :param PeakCpuNum: CPU峰值
        :type PeakCpuNum: int
        :param PeakMemoryNum: 内存峰值
        :type PeakMemoryNum: int
        :param PeakStorageNum: 硬盘峰值
        :type PeakStorageNum: int
        :param RecordTime: 记录时间
        :type RecordTime: str
        """
        self.PeakCpuNum = None
        self.PeakMemoryNum = None
        self.PeakStorageNum = None
        self.RecordTime = None


    def _deserialize(self, params):
        self.PeakCpuNum = params.get("PeakCpuNum")
        self.PeakMemoryNum = params.get("PeakMemoryNum")
        self.PeakStorageNum = params.get("PeakStorageNum")
        self.RecordTime = params.get("RecordTime")


class PeakFamilyInfo(AbstractModel):
    """PeakFamilyInfo 按机型类别分类的cpu等数据的峰值信息

    """

    def __init__(self):
        """
        :param InstanceFamily: 机型类别信息。
        :type InstanceFamily: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyTypeConfig`
        :param PeakBaseSet: 基础数据峰值信息。
        :type PeakBaseSet: list of PeakBase
        """
        self.InstanceFamily = None
        self.PeakBaseSet = None


    def _deserialize(self, params):
        if params.get("InstanceFamily") is not None:
            self.InstanceFamily = InstanceFamilyTypeConfig()
            self.InstanceFamily._deserialize(params.get("InstanceFamily"))
        if params.get("PeakBaseSet") is not None:
            self.PeakBaseSet = []
            for item in params.get("PeakBaseSet"):
                obj = PeakBase()
                obj._deserialize(item)
                self.PeakBaseSet.append(obj)


class PeakNetwork(AbstractModel):
    """峰值网络数据

    """

    def __init__(self):
        """
        :param RecordTime: 记录时间。
        :type RecordTime: str
        :param PeakInNetwork: 入带宽数据。
        :type PeakInNetwork: str
        :param PeakOutNetwork: 出带宽数据。
        :type PeakOutNetwork: str
        """
        self.RecordTime = None
        self.PeakInNetwork = None
        self.PeakOutNetwork = None


    def _deserialize(self, params):
        self.RecordTime = params.get("RecordTime")
        self.PeakInNetwork = params.get("PeakInNetwork")
        self.PeakOutNetwork = params.get("PeakOutNetwork")


class PeakNetworkRegionInfo(AbstractModel):
    """region维度的网络峰值信息

    """

    def __init__(self):
        """
        :param Region: region信息
        :type Region: str
        :param PeakNetworkSet: 网络峰值集合
注意：此字段可能返回 null，表示取不到有效值。
        :type PeakNetworkSet: list of PeakNetwork
        """
        self.Region = None
        self.PeakNetworkSet = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        if params.get("PeakNetworkSet") is not None:
            self.PeakNetworkSet = []
            for item in params.get("PeakNetworkSet"):
                obj = PeakNetwork()
                obj._deserialize(item)
                self.PeakNetworkSet.append(obj)


class Position(AbstractModel):
    """描述实例的位置相关信息。

    """

    def __init__(self):
        """
        :param ZoneInfo: 实例所在的Zone的信息。
        :type ZoneInfo: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        :param Country: 实例所在的国家的信息。
        :type Country: :class:`tencentcloud.ecm.v20190719.models.Country`
        :param Area: 实例所在的Area的信息。
        :type Area: :class:`tencentcloud.ecm.v20190719.models.Area`
        :param Province: 实例所在的省份的信息。
        :type Province: :class:`tencentcloud.ecm.v20190719.models.Province`
        :param City: 实例所在的城市的信息。
        :type City: :class:`tencentcloud.ecm.v20190719.models.City`
        :param RegionInfo: 实例所在的Region的信息。
        :type RegionInfo: :class:`tencentcloud.ecm.v20190719.models.RegionInfo`
        """
        self.ZoneInfo = None
        self.Country = None
        self.Area = None
        self.Province = None
        self.City = None
        self.RegionInfo = None


    def _deserialize(self, params):
        if params.get("ZoneInfo") is not None:
            self.ZoneInfo = ZoneInfo()
            self.ZoneInfo._deserialize(params.get("ZoneInfo"))
        if params.get("Country") is not None:
            self.Country = Country()
            self.Country._deserialize(params.get("Country"))
        if params.get("Area") is not None:
            self.Area = Area()
            self.Area._deserialize(params.get("Area"))
        if params.get("Province") is not None:
            self.Province = Province()
            self.Province._deserialize(params.get("Province"))
        if params.get("City") is not None:
            self.City = City()
            self.City._deserialize(params.get("City"))
        if params.get("RegionInfo") is not None:
            self.RegionInfo = RegionInfo()
            self.RegionInfo._deserialize(params.get("RegionInfo"))


class PrivateIPAddressInfo(AbstractModel):
    """实例的内网ip相关信息。

    """

    def __init__(self):
        """
        :param PrivateIPAddress: 实例的内网ip。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIPAddress: str
        """
        self.PrivateIPAddress = None


    def _deserialize(self, params):
        self.PrivateIPAddress = params.get("PrivateIPAddress")


class Province(AbstractModel):
    """省份信息

    """

    def __init__(self):
        """
        :param ProvinceId: 省份Id
        :type ProvinceId: str
        :param ProvinceName: 省份名称
        :type ProvinceName: str
        """
        self.ProvinceId = None
        self.ProvinceName = None


    def _deserialize(self, params):
        self.ProvinceId = params.get("ProvinceId")
        self.ProvinceName = params.get("ProvinceName")


class PublicIPAddressInfo(AbstractModel):
    """实例的公网ip相关信息。

    """

    def __init__(self):
        """
        :param ChargeMode: 计费模式。
        :type ChargeMode: str
        :param PublicIPAddress: 实例的公网ip。
        :type PublicIPAddress: str
        :param ISP: 实例的公网ip所属的运营商。
        :type ISP: :class:`tencentcloud.ecm.v20190719.models.ISP`
        :param MaxBandwidthOut: 实例的最大出带宽上限。
        :type MaxBandwidthOut: int
        """
        self.ChargeMode = None
        self.PublicIPAddress = None
        self.ISP = None
        self.MaxBandwidthOut = None


    def _deserialize(self, params):
        self.ChargeMode = params.get("ChargeMode")
        self.PublicIPAddress = params.get("PublicIPAddress")
        if params.get("ISP") is not None:
            self.ISP = ISP()
            self.ISP._deserialize(params.get("ISP"))
        self.MaxBandwidthOut = params.get("MaxBandwidthOut")


class RebootInstancesRequest(AbstractModel):
    """RebootInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待重启的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。
        :type InstanceIdSet: list of str
        :param ForceReboot: 是否在正常重启失败后选择强制重启实例。取值范围：
TRUE：表示在正常重启失败后进行强制重启；
FALSE：表示在正常重启失败后不进行强制重启；
默认取值：FALSE。
        :type ForceReboot: bool
        :param StopType: 关机类型。取值范围：
SOFT：表示软关机
HARD：表示硬关机
SOFT_FIRST：表示优先软关机，失败再执行硬关机

默认取值：SOFT。
        :type StopType: str
        """
        self.InstanceIdSet = None
        self.ForceReboot = None
        self.StopType = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.ForceReboot = params.get("ForceReboot")
        self.StopType = params.get("StopType")


class RebootInstancesResponse(AbstractModel):
    """RebootInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """Region和RegionName

    """

    def __init__(self):
        """
        :param Region: Region
        :type Region: str
        :param RegionName: Region名称
        :type RegionName: str
        :param RegionId: RegionID
        :type RegionId: int
        """
        self.Region = None
        self.RegionName = None
        self.RegionId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")


class ResetInstancesMaxBandwidthRequest(AbstractModel):
    """ResetInstancesMaxBandwidth请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待重置带宽上限的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。
        :type InstanceIdSet: list of str
        :param MaxBandwidthOut: 修改后的最大带宽上限。
        :type MaxBandwidthOut: int
        """
        self.InstanceIdSet = None
        self.MaxBandwidthOut = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.MaxBandwidthOut = params.get("MaxBandwidthOut")


class ResetInstancesMaxBandwidthResponse(AbstractModel):
    """ResetInstancesMaxBandwidth返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesRequest(AbstractModel):
    """ResetInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待重装的实例ID列表。
        :type InstanceIdSet: list of str
        :param ImageId: 重装使用的镜像ID，若未指定，则使用各个实例当前的镜像进行重装。
        :type ImageId: str
        :param Password: 密码设置，若未指定，则后续将以站内信的形式通知密码。
        :type Password: str
        :param EnhancedService: 是否开启云监控和云镜服务，未指定时默认开启。
        :type EnhancedService: :class:`tencentcloud.ecm.v20190719.models.EnhancedService`
        """
        self.InstanceIdSet = None
        self.ImageId = None
        self.Password = None
        self.EnhancedService = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.ImageId = params.get("ImageId")
        self.Password = params.get("Password")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))


class ResetInstancesResponse(AbstractModel):
    """ResetInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunMonitorServiceEnabled(AbstractModel):
    """云监控服务

    """

    def __init__(self):
        """
        :param Enabled: 是否开启。
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")


class RunSecurityServiceEnabled(AbstractModel):
    """云镜服务；

    """

    def __init__(self):
        """
        :param Enabled: 是否开启。
        :type Enabled: bool
        :param Version: 云镜版本：0 基础版，1 专业版
        :type Version: int
        """
        self.Enabled = None
        self.Version = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.Version = params.get("Version")


class SimpleModule(AbstractModel):
    """Module的简要信息

    """

    def __init__(self):
        """
        :param ModuleId: 模块ID
        :type ModuleId: str
        :param ModuleName: 模块名称
        :type ModuleName: str
        """
        self.ModuleId = None
        self.ModuleName = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.ModuleName = params.get("ModuleName")


class SrcImage(AbstractModel):
    """镜像来源信息

    """

    def __init__(self):
        """
        :param ImageId: 镜像id
        :type ImageId: str
        :param ImageName: 镜像名称
        :type ImageName: str
        :param ImageOsName: 系统名称
        :type ImageOsName: str
        :param ImageDescription: 镜像描述
        :type ImageDescription: str
        :param Region: 区域
        :type Region: str
        :param RegionID: 区域ID
        :type RegionID: int
        :param RegionName: 区域名称
        :type RegionName: str
        """
        self.ImageId = None
        self.ImageName = None
        self.ImageOsName = None
        self.ImageDescription = None
        self.Region = None
        self.RegionID = None
        self.RegionName = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ImageOsName = params.get("ImageOsName")
        self.ImageDescription = params.get("ImageDescription")
        self.Region = params.get("Region")
        self.RegionID = params.get("RegionID")
        self.RegionName = params.get("RegionName")


class Tag(AbstractModel):
    """标签信息。

    """

    def __init__(self):
        """
        :param Key: 标签的键。
        :type Key: str
        :param Value: 标签的值。
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class TerminateInstancesRequest(AbstractModel):
    """TerminateInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待销毁的实例ID列表。
        :type InstanceIdSet: list of str
        :param TerminateDelay: 是否定时销毁，默认为否。
        :type TerminateDelay: bool
        :param TerminateTime: 定时销毁的时间，格式形如："2019-08-05 12:01:30"，若非定时销毁，则此参数被忽略。
        :type TerminateTime: str
        """
        self.InstanceIdSet = None
        self.TerminateDelay = None
        self.TerminateTime = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.TerminateDelay = params.get("TerminateDelay")
        self.TerminateTime = params.get("TerminateTime")


class TerminateInstancesResponse(AbstractModel):
    """TerminateInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ZoneInfo(AbstractModel):
    """Zone信息

    """

    def __init__(self):
        """
        :param ZoneId: ZoneId
        :type ZoneId: int
        :param ZoneName: ZoneName
        :type ZoneName: str
        :param Zone: Zone
        :type Zone: str
        """
        self.ZoneId = None
        self.ZoneName = None
        self.Zone = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.Zone = params.get("Zone")


class ZoneInstanceInfo(AbstractModel):
    """Zone的实例信息

    """

    def __init__(self):
        """
        :param ZoneName: Zone名称
        :type ZoneName: str
        :param InstanceNum: 实例数量
        :type InstanceNum: int
        """
        self.ZoneName = None
        self.InstanceNum = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        self.InstanceNum = params.get("InstanceNum")