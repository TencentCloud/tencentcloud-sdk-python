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


class AssociateTargetGroupsRequest(AbstractModel):
    """AssociateTargetGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Associations: 绑定的关系数组。一次请求最多支持20个。
        :type Associations: list of TargetGroupAssociation
        """
        self._Associations = None

    @property
    def Associations(self):
        return self._Associations

    @Associations.setter
    def Associations(self, Associations):
        self._Associations = Associations


    def _deserialize(self, params):
        if params.get("Associations") is not None:
            self._Associations = []
            for item in params.get("Associations"):
                obj = TargetGroupAssociation()
                obj._deserialize(item)
                self._Associations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateTargetGroupsResponse(AbstractModel):
    """AssociateTargetGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AssociationItem(AbstractModel):
    """目标组关联到的规则

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 关联到的网关负载均衡实例ID
        :type LoadBalancerId: str
        :param _LoadBalancerName: 网关负载均衡实例名称
        :type LoadBalancerName: str
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGatewayLoadBalancerRequest(AbstractModel):
    """CreateGatewayLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 网关负载均衡后端目标设备所属的私有网络 ID，如vpc-12345678，可以通过 DescribeVpcEx 接口获取。 不填此参数则默认为DefaultVPC。创建内网负载均衡实例时，此参数必填。
        :type VpcId: str
        :param _SubnetId: 网关负载均衡后端目标设备所属的私有网络的子网ID。
        :type SubnetId: str
        :param _LoadBalancerName: 网关负载均衡实例名称。可支持输入1-60个字符。不填写时默认自动生成。
        :type LoadBalancerName: str
        :param _Number: 创建网关负载均衡的个数，默认值为 1。批量创建数量最大支持10个。
        :type Number: int
        :param _Tags: 购买网关负载均衡的同时，给负载均衡打上标签，最大支持20个标签键值对。
        :type Tags: list of TagInfo
        :param _LBChargeType: 网关负载均衡实例计费类型，当前只支持传POSTPAID_BY_HOUR，默认是POSTPAID_BY_HOUR。
        :type LBChargeType: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._LoadBalancerName = None
        self._Number = None
        self._Tags = None
        self._LBChargeType = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def LBChargeType(self):
        return self._LBChargeType

    @LBChargeType.setter
    def LBChargeType(self, LBChargeType):
        self._LBChargeType = LBChargeType


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._Number = params.get("Number")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._LBChargeType = params.get("LBChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGatewayLoadBalancerResponse(AbstractModel):
    """CreateGatewayLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 由网关负载均衡实例唯一 ID 组成的数组。
存在某些场景，如创建出现延迟时，此字段可能返回为空；此时可以根据接口返回的RequestId或DealName参数，通过DescribeTaskStatus接口查询创建的资源ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerIds: list of str
        :param _DealName: 订单号。
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoadBalancerIds = None
        self._DealName = None
        self._RequestId = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class CreateTargetGroupRequest(AbstractModel):
    """CreateTargetGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupName: 目标组名称，限定60个字符。
        :type TargetGroupName: str
        :param _VpcId: 目标组的vpcid属性，不填则使用默认vpc
        :type VpcId: str
        :param _Port: 目标组的默认端口， 后续添加服务器时可使用该默认端口。Port和TargetGroupInstances.N中的port二者必填其一。
        :type Port: int
        :param _TargetGroupInstances: 目标组绑定的后端服务器
        :type TargetGroupInstances: list of TargetGroupInstance
        :param _Protocol: 网关负载均衡目标组协议。
- TENCENT_GENEVE ：GENEVE 标准协议
- AWS_GENEVE：GENEVE 兼容协议（需要提交工单申请开白）
        :type Protocol: str
        :param _HealthCheck: 健康检查设置。
        :type HealthCheck: :class:`tencentcloud.gwlb.v20240906.models.TargetGroupHealthCheck`
        :param _ScheduleAlgorithm: 均衡算法。
- IP_HASH_3_ELASTIC：弹性哈希
        :type ScheduleAlgorithm: str
        :param _AllDeadToAlive: 是否支持全死全活。默认支持。
        :type AllDeadToAlive: bool
        """
        self._TargetGroupName = None
        self._VpcId = None
        self._Port = None
        self._TargetGroupInstances = None
        self._Protocol = None
        self._HealthCheck = None
        self._ScheduleAlgorithm = None
        self._AllDeadToAlive = None

    @property
    def TargetGroupName(self):
        return self._TargetGroupName

    @TargetGroupName.setter
    def TargetGroupName(self, TargetGroupName):
        self._TargetGroupName = TargetGroupName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def TargetGroupInstances(self):
        return self._TargetGroupInstances

    @TargetGroupInstances.setter
    def TargetGroupInstances(self, TargetGroupInstances):
        self._TargetGroupInstances = TargetGroupInstances

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def ScheduleAlgorithm(self):
        return self._ScheduleAlgorithm

    @ScheduleAlgorithm.setter
    def ScheduleAlgorithm(self, ScheduleAlgorithm):
        self._ScheduleAlgorithm = ScheduleAlgorithm

    @property
    def AllDeadToAlive(self):
        return self._AllDeadToAlive

    @AllDeadToAlive.setter
    def AllDeadToAlive(self, AllDeadToAlive):
        self._AllDeadToAlive = AllDeadToAlive


    def _deserialize(self, params):
        self._TargetGroupName = params.get("TargetGroupName")
        self._VpcId = params.get("VpcId")
        self._Port = params.get("Port")
        if params.get("TargetGroupInstances") is not None:
            self._TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self._TargetGroupInstances.append(obj)
        self._Protocol = params.get("Protocol")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = TargetGroupHealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        self._ScheduleAlgorithm = params.get("ScheduleAlgorithm")
        self._AllDeadToAlive = params.get("AllDeadToAlive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTargetGroupResponse(AbstractModel):
    """CreateTargetGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 创建目标组后生成的id
        :type TargetGroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TargetGroupId = None
        self._RequestId = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._RequestId = params.get("RequestId")


class DeleteGatewayLoadBalancerRequest(AbstractModel):
    """DeleteGatewayLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 要删除的网关负载均衡实例 ID数组，数组大小最大支持20。
        :type LoadBalancerIds: list of str
        """
        self._LoadBalancerIds = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGatewayLoadBalancerResponse(AbstractModel):
    """DeleteGatewayLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTargetGroupsRequest(AbstractModel):
    """DeleteTargetGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupIds: 目标组ID列表。
        :type TargetGroupIds: list of str
        """
        self._TargetGroupIds = None

    @property
    def TargetGroupIds(self):
        return self._TargetGroupIds

    @TargetGroupIds.setter
    def TargetGroupIds(self, TargetGroupIds):
        self._TargetGroupIds = TargetGroupIds


    def _deserialize(self, params):
        self._TargetGroupIds = params.get("TargetGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTargetGroupsResponse(AbstractModel):
    """DeleteTargetGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeregisterTargetGroupInstancesRequest(AbstractModel):
    """DeregisterTargetGroupInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组ID。
        :type TargetGroupId: str
        :param _TargetGroupInstances: 待解绑的服务器信息。
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self._TargetGroupId = None
        self._TargetGroupInstances = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupInstances(self):
        return self._TargetGroupInstances

    @TargetGroupInstances.setter
    def TargetGroupInstances(self, TargetGroupInstances):
        self._TargetGroupInstances = TargetGroupInstances


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self._TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self._TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeregisterTargetGroupInstancesResponse(AbstractModel):
    """DeregisterTargetGroupInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeGatewayLoadBalancersRequest(AbstractModel):
    """DescribeGatewayLoadBalancers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 网关负载均衡实例ID。支持批量筛选的实例ID数量上限为20个。
        :type LoadBalancerIds: list of str
        :param _Limit: 一次批量返回网关负载均衡实例的数量，默认为20，最大值为100。
        :type Limit: int
        :param _Offset: 返回网关负载均衡实例列表的起始偏移量，默认0。
        :type Offset: int
        :param _Filters: 查询负载均衡详细信息列表的过滤条件，每次请求的Filters的上限为10，Filter.Values的上限为100。
Filter.Name和Filter.Values皆为必填项。详细的过滤条件如下：
- name - String - 是否必填：否 - （过滤条件）按照网关负载均衡实例名称过滤，如“gwlb-xxxx”。
- VpcId - String - 是否必填：否 - （过滤条件）按照网关负载均衡实例所属的私有网络过滤，如“vpc-bhqk****”。

        :type Filters: list of Filter
        :param _SearchKey: 搜索字段，模糊匹配名称、VIP。
        :type SearchKey: str
        """
        self._LoadBalancerIds = None
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._SearchKey = None

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayLoadBalancersResponse(AbstractModel):
    """DescribeGatewayLoadBalancers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 满足过滤条件的负载均衡实例总数。此数值与入参中的Limit无关。
        :type TotalCount: int
        :param _LoadBalancerSet: 返回的网关负载均衡实例数组。
        :type LoadBalancerSet: list of GatewayLoadBalancer
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._LoadBalancerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LoadBalancerSet(self):
        return self._LoadBalancerSet

    @LoadBalancerSet.setter
    def LoadBalancerSet(self, LoadBalancerSet):
        self._LoadBalancerSet = LoadBalancerSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("LoadBalancerSet") is not None:
            self._LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = GatewayLoadBalancer()
                obj._deserialize(item)
                self._LoadBalancerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTargetGroupInstanceStatusRequest(AbstractModel):
    """DescribeTargetGroupInstanceStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组唯一id
        :type TargetGroupId: str
        :param _TargetGroupInstanceIps: 目标组绑定的后端服务ip列表
        :type TargetGroupInstanceIps: list of str
        """
        self._TargetGroupId = None
        self._TargetGroupInstanceIps = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupInstanceIps(self):
        return self._TargetGroupInstanceIps

    @TargetGroupInstanceIps.setter
    def TargetGroupInstanceIps(self, TargetGroupInstanceIps):
        self._TargetGroupInstanceIps = TargetGroupInstanceIps


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._TargetGroupInstanceIps = params.get("TargetGroupInstanceIps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetGroupInstanceStatusResponse(AbstractModel):
    """DescribeTargetGroupInstanceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupInstanceSet: 健康检查后端rs状态列表
        :type TargetGroupInstanceSet: list of TargetGroupInstanceStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TargetGroupInstanceSet = None
        self._RequestId = None

    @property
    def TargetGroupInstanceSet(self):
        return self._TargetGroupInstanceSet

    @TargetGroupInstanceSet.setter
    def TargetGroupInstanceSet(self, TargetGroupInstanceSet):
        self._TargetGroupInstanceSet = TargetGroupInstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TargetGroupInstanceSet") is not None:
            self._TargetGroupInstanceSet = []
            for item in params.get("TargetGroupInstanceSet"):
                obj = TargetGroupInstanceStatus()
                obj._deserialize(item)
                self._TargetGroupInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTargetGroupInstancesRequest(AbstractModel):
    """DescribeTargetGroupInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件，当前仅支持TargetGroupId，BindIP，InstanceId过滤。
        :type Filters: list of Filter
        :param _Limit: 显示数量限制，默认20。
        :type Limit: int
        :param _Offset: 显示的偏移量，默认为0。
        :type Offset: int
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetGroupInstancesResponse(AbstractModel):
    """DescribeTargetGroupInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 本次查询的结果数量。
        :type TotalCount: int
        :param _TargetGroupInstanceSet: 绑定的服务器信息。
        :type TargetGroupInstanceSet: list of TargetGroupBackend
        :param _RealCount: 实际统计数量，不受Limit、Offset、CAM的影响。
        :type RealCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TargetGroupInstanceSet = None
        self._RealCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TargetGroupInstanceSet(self):
        return self._TargetGroupInstanceSet

    @TargetGroupInstanceSet.setter
    def TargetGroupInstanceSet(self, TargetGroupInstanceSet):
        self._TargetGroupInstanceSet = TargetGroupInstanceSet

    @property
    def RealCount(self):
        return self._RealCount

    @RealCount.setter
    def RealCount(self, RealCount):
        self._RealCount = RealCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TargetGroupInstanceSet") is not None:
            self._TargetGroupInstanceSet = []
            for item in params.get("TargetGroupInstanceSet"):
                obj = TargetGroupBackend()
                obj._deserialize(item)
                self._TargetGroupInstanceSet.append(obj)
        self._RealCount = params.get("RealCount")
        self._RequestId = params.get("RequestId")


class DescribeTargetGroupListRequest(AbstractModel):
    """DescribeTargetGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupIds: 目标组ID数组。
        :type TargetGroupIds: list of str
        :param _Filters: 过滤条件数组，支持TargetGroupVpcId和TargetGroupName。
        :type Filters: list of Filter
        :param _Offset: 显示的偏移起始量。
        :type Offset: int
        :param _Limit: 显示条数限制，默认为20。
        :type Limit: int
        """
        self._TargetGroupIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def TargetGroupIds(self):
        return self._TargetGroupIds

    @TargetGroupIds.setter
    def TargetGroupIds(self, TargetGroupIds):
        self._TargetGroupIds = TargetGroupIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._TargetGroupIds = params.get("TargetGroupIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetGroupListResponse(AbstractModel):
    """DescribeTargetGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 显示的结果数量。
        :type TotalCount: int
        :param _TargetGroupSet: 显示的目标组信息集合。
        :type TargetGroupSet: list of TargetGroupInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TargetGroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TargetGroupSet(self):
        return self._TargetGroupSet

    @TargetGroupSet.setter
    def TargetGroupSet(self, TargetGroupSet):
        self._TargetGroupSet = TargetGroupSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TargetGroupSet") is not None:
            self._TargetGroupSet = []
            for item in params.get("TargetGroupSet"):
                obj = TargetGroupInfo()
                obj._deserialize(item)
                self._TargetGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTargetGroupsRequest(AbstractModel):
    """DescribeTargetGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupIds: 目标组ID，与Filters互斥。
        :type TargetGroupIds: list of str
        :param _Limit: 显示条数限制，默认为20。
        :type Limit: int
        :param _Offset: 显示的偏移起始量。
        :type Offset: int
        :param _Filters: 过滤条件数组，支持TargetGroupVpcId和TargetGroupName。
        :type Filters: list of Filter
        """
        self._TargetGroupIds = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def TargetGroupIds(self):
        return self._TargetGroupIds

    @TargetGroupIds.setter
    def TargetGroupIds(self, TargetGroupIds):
        self._TargetGroupIds = TargetGroupIds

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._TargetGroupIds = params.get("TargetGroupIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetGroupsResponse(AbstractModel):
    """DescribeTargetGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 显示的结果数量。
        :type TotalCount: int
        :param _TargetGroupSet: 显示的目标组信息集合。
        :type TargetGroupSet: list of TargetGroupInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TargetGroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TargetGroupSet(self):
        return self._TargetGroupSet

    @TargetGroupSet.setter
    def TargetGroupSet(self, TargetGroupSet):
        self._TargetGroupSet = TargetGroupSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TargetGroupSet") is not None:
            self._TargetGroupSet = []
            for item in params.get("TargetGroupSet"):
                obj = TargetGroupInfo()
                obj._deserialize(item)
                self._TargetGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 请求ID，即接口返回的 RequestId 参数。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务的当前状态。 0：成功，1：失败，2：进行中。
        :type Status: int
        :param _LoadBalancerIds: 由负载均衡实例唯一 ID 组成的数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerIds: list of str
        :param _Message: 辅助描述信息，如失败原因等。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._LoadBalancerIds = None
        self._Message = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DisassociateTargetGroupsRequest(AbstractModel):
    """DisassociateTargetGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Associations: 待解绑的目标组列表。
        :type Associations: list of TargetGroupAssociation
        """
        self._Associations = None

    @property
    def Associations(self):
        return self._Associations

    @Associations.setter
    def Associations(self, Associations):
        self._Associations = Associations


    def _deserialize(self, params):
        if params.get("Associations") is not None:
            self._Associations = []
            for item in params.get("Associations"):
                obj = TargetGroupAssociation()
                obj._deserialize(item)
                self._Associations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateTargetGroupsResponse(AbstractModel):
    """DisassociateTargetGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """过滤器条件

    """

    def __init__(self):
        r"""
        :param _Name: 过滤器的名称
        :type Name: str
        :param _Values: 过滤器的值数组
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayLoadBalancer(AbstractModel):
    """网关负载均衡实例的信息

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 网关负载均衡实例 ID。
        :type LoadBalancerId: str
        :param _LoadBalancerName: 网关负载均衡实例的名称。
        :type LoadBalancerName: str
        :param _VpcId: 网关负载均衡所属私有网络。
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 网关负载均衡所属子网。
        :type SubnetId: str
        :param _Vips: 网关负载均衡提供服务的虚拟IP。
        :type Vips: list of str
        :param _Status: 网关负载均衡实例状态。
0：创建中，1：正常运行，3：删除中。
        :type Status: int
        :param _TargetGroupId: 关联的目标组唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetGroupId: str
        :param _DeleteProtect: 是否开启删除保护功能。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteProtect: bool
        :param _Tags: 负载均衡实例的标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagInfo
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _ChargeType: 网关负载均衡实例的计费类型，POSTPAID_BY_HOUR：按量计费
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: str
        :param _Isolation: 0：表示未被隔离，1：表示被隔离。
注意：此字段可能返回 null，表示取不到有效值。
        :type Isolation: int
        :param _IsolatedTime: 负载均衡实例被隔离的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedTime: str
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._VpcId = None
        self._SubnetId = None
        self._Vips = None
        self._Status = None
        self._TargetGroupId = None
        self._DeleteProtect = None
        self._Tags = None
        self._CreateTime = None
        self._ChargeType = None
        self._Isolation = None
        self._IsolatedTime = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Vips(self):
        return self._Vips

    @Vips.setter
    def Vips(self, Vips):
        self._Vips = Vips

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def DeleteProtect(self):
        return self._DeleteProtect

    @DeleteProtect.setter
    def DeleteProtect(self, DeleteProtect):
        self._DeleteProtect = DeleteProtect

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def Isolation(self):
        return self._Isolation

    @Isolation.setter
    def Isolation(self, Isolation):
        self._Isolation = Isolation

    @property
    def IsolatedTime(self):
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Vips = params.get("Vips")
        self._Status = params.get("Status")
        self._TargetGroupId = params.get("TargetGroupId")
        self._DeleteProtect = params.get("DeleteProtect")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._ChargeType = params.get("ChargeType")
        self._Isolation = params.get("Isolation")
        self._IsolatedTime = params.get("IsolatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateGatewayLoadBalancerRequest(AbstractModel):
    """InquirePriceCreateGatewayLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GoodsNum: 询价的网关负载均衡实例个数，默认为1
        :type GoodsNum: int
        """
        self._GoodsNum = None

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum


    def _deserialize(self, params):
        self._GoodsNum = params.get("GoodsNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateGatewayLoadBalancerResponse(AbstractModel):
    """InquirePriceCreateGatewayLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 该参数表示对应的价格。
        :type Price: :class:`tencentcloud.gwlb.v20240906.models.Price`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class ItemPrice(AbstractModel):
    """描述了单项的价格信息

    """

    def __init__(self):
        r"""
        :param _UnitPrice: 后付费单价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param _ChargeUnit: 后付费计价单元，可取值范围： HOUR：表示计价单元是按每小时来计算。当前涉及该计价单元的场景有：实例按小时后付费（POSTPAID_BY_HOUR）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeUnit: str
        :param _OriginalPrice: 预支费用的原价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalPrice: float
        :param _DiscountPrice: 预支费用的折扣价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountPrice: float
        :param _UnitPriceDiscount: 后付费的折扣单价，单位:元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: float
        :param _Discount: 折扣，如20.0代表2折。
注意：此字段可能返回 null，表示取不到有效值。
        :type Discount: float
        """
        self._UnitPrice = None
        self._ChargeUnit = None
        self._OriginalPrice = None
        self._DiscountPrice = None
        self._UnitPriceDiscount = None
        self._Discount = None

    @property
    def UnitPrice(self):
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def ChargeUnit(self):
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit

    @property
    def OriginalPrice(self):
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def UnitPriceDiscount(self):
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def Discount(self):
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount


    def _deserialize(self, params):
        self._UnitPrice = params.get("UnitPrice")
        self._ChargeUnit = params.get("ChargeUnit")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        self._Discount = params.get("Discount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGatewayLoadBalancerAttributeRequest(AbstractModel):
    """ModifyGatewayLoadBalancerAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 网关负载均衡的唯一ID。
        :type LoadBalancerId: str
        :param _LoadBalancerName: 网关负载均衡实例名称。可支持输入1-60个字符。
        :type LoadBalancerName: str
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGatewayLoadBalancerAttributeResponse(AbstractModel):
    """ModifyGatewayLoadBalancerAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTargetGroupAttributeRequest(AbstractModel):
    """ModifyTargetGroupAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组的ID。
        :type TargetGroupId: str
        :param _TargetGroupName: 目标组的新名称。
        :type TargetGroupName: str
        :param _HealthCheck: 健康检查详情。
        :type HealthCheck: :class:`tencentcloud.gwlb.v20240906.models.TargetGroupHealthCheck`
        :param _AllDeadToAlive: 是否支持全死全活。
        :type AllDeadToAlive: bool
        """
        self._TargetGroupId = None
        self._TargetGroupName = None
        self._HealthCheck = None
        self._AllDeadToAlive = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupName(self):
        return self._TargetGroupName

    @TargetGroupName.setter
    def TargetGroupName(self, TargetGroupName):
        self._TargetGroupName = TargetGroupName

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def AllDeadToAlive(self):
        return self._AllDeadToAlive

    @AllDeadToAlive.setter
    def AllDeadToAlive(self, AllDeadToAlive):
        self._AllDeadToAlive = AllDeadToAlive


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._TargetGroupName = params.get("TargetGroupName")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = TargetGroupHealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        self._AllDeadToAlive = params.get("AllDeadToAlive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetGroupAttributeResponse(AbstractModel):
    """ModifyTargetGroupAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTargetGroupInstancesWeightRequest(AbstractModel):
    """ModifyTargetGroupInstancesWeight请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组ID。
        :type TargetGroupId: str
        :param _TargetGroupInstances: 实例绑定配置数组。
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self._TargetGroupId = None
        self._TargetGroupInstances = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupInstances(self):
        return self._TargetGroupInstances

    @TargetGroupInstances.setter
    def TargetGroupInstances(self, TargetGroupInstances):
        self._TargetGroupInstances = TargetGroupInstances


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self._TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self._TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetGroupInstancesWeightResponse(AbstractModel):
    """ModifyTargetGroupInstancesWeight返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Price(AbstractModel):
    """表示网关负载均衡的价格

    """

    def __init__(self):
        r"""
        :param _InstancePrice: 描述了实例价格。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstancePrice: :class:`tencentcloud.gwlb.v20240906.models.ItemPrice`
        :param _LcuPrice: 描述了GLCU的价格。
注意：此字段可能返回 null，表示取不到有效值。
        :type LcuPrice: :class:`tencentcloud.gwlb.v20240906.models.ItemPrice`
        """
        self._InstancePrice = None
        self._LcuPrice = None

    @property
    def InstancePrice(self):
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def LcuPrice(self):
        return self._LcuPrice

    @LcuPrice.setter
    def LcuPrice(self, LcuPrice):
        self._LcuPrice = LcuPrice


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self._InstancePrice = ItemPrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("LcuPrice") is not None:
            self._LcuPrice = ItemPrice()
            self._LcuPrice._deserialize(params.get("LcuPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterTargetGroupInstancesRequest(AbstractModel):
    """RegisterTargetGroupInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param _TargetGroupInstances: 服务器实例数组
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self._TargetGroupId = None
        self._TargetGroupInstances = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupInstances(self):
        return self._TargetGroupInstances

    @TargetGroupInstances.setter
    def TargetGroupInstances(self, TargetGroupInstances):
        self._TargetGroupInstances = TargetGroupInstances


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self._TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self._TargetGroupInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterTargetGroupInstancesResponse(AbstractModel):
    """RegisterTargetGroupInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TagInfo(AbstractModel):
    """网关负载均衡的标签信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签的键
        :type TagKey: str
        :param _TagValue: 标签的值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupAssociation(AbstractModel):
    """规则与目标组的关联关系。

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 网关负载均衡实例ID。
        :type LoadBalancerId: str
        :param _TargetGroupId: 目标组ID。
        :type TargetGroupId: str
        """
        self._LoadBalancerId = None
        self._TargetGroupId = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._TargetGroupId = params.get("TargetGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupBackend(AbstractModel):
    """目标组绑定的后端服务器

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param _Type: 后端服务的类型，可取：CVM、ENI（即将支持）
        :type Type: str
        :param _InstanceId: 后端服务的唯一 ID
        :type InstanceId: str
        :param _Port: 后端服务的监听端口
        :type Port: int
        :param _Weight: 后端服务的转发权重，取值范围：[0, 100]，默认为 10。
        :type Weight: int
        :param _PublicIpAddresses: 后端服务的外网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param _PrivateIpAddresses: 后端服务的内网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIpAddresses: list of str
        :param _InstanceName: 后端服务的实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _RegisteredTime: 后端服务被绑定的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RegisteredTime: str
        :param _EniId: 弹性网卡唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EniId: str
        :param _ZoneId: 后端服务的可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        """
        self._TargetGroupId = None
        self._Type = None
        self._InstanceId = None
        self._Port = None
        self._Weight = None
        self._PublicIpAddresses = None
        self._PrivateIpAddresses = None
        self._InstanceName = None
        self._RegisteredTime = None
        self._EniId = None
        self._ZoneId = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def PublicIpAddresses(self):
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def PrivateIpAddresses(self):
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def RegisteredTime(self):
        return self._RegisteredTime

    @RegisteredTime.setter
    def RegisteredTime(self, RegisteredTime):
        self._RegisteredTime = RegisteredTime

    @property
    def EniId(self):
        return self._EniId

    @EniId.setter
    def EniId(self, EniId):
        self._EniId = EniId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._Type = params.get("Type")
        self._InstanceId = params.get("InstanceId")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._InstanceName = params.get("InstanceName")
        self._RegisteredTime = params.get("RegisteredTime")
        self._EniId = params.get("EniId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupHealthCheck(AbstractModel):
    """目标组健康检查详情

    """

    def __init__(self):
        r"""
        :param _HealthSwitch: 是否开启健康检查。
        :type HealthSwitch: bool
        :param _Protocol: 健康检查使用的协议。支持ping和tcp，默认为ping。

- PING: icmp
- TCP: tcp
        :type Protocol: str
        :param _Port: 健康检查端口，探测协议未tcp时，该参数必填。

        :type Port: int
        :param _Timeout: 健康检查超时时间。 默认为2秒。 可配置范围：2 - 30秒。
        :type Timeout: int
        :param _IntervalTime: 检测间隔时间。 默认为5秒。 可配置范围：2 - 300秒。
        :type IntervalTime: int
        :param _HealthNum: 检测健康阈值。 默认为3秒。 可配置范围：2 - 10次。
        :type HealthNum: int
        :param _UnHealthNum: 检测不健康阈值。 默认为3秒。 可配置范围：2 - 10次。
        :type UnHealthNum: int
        """
        self._HealthSwitch = None
        self._Protocol = None
        self._Port = None
        self._Timeout = None
        self._IntervalTime = None
        self._HealthNum = None
        self._UnHealthNum = None

    @property
    def HealthSwitch(self):
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def IntervalTime(self):
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HealthNum(self):
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def UnHealthNum(self):
        return self._UnHealthNum

    @UnHealthNum.setter
    def UnHealthNum(self, UnHealthNum):
        self._UnHealthNum = UnHealthNum


    def _deserialize(self, params):
        self._HealthSwitch = params.get("HealthSwitch")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._Timeout = params.get("Timeout")
        self._IntervalTime = params.get("IntervalTime")
        self._HealthNum = params.get("HealthNum")
        self._UnHealthNum = params.get("UnHealthNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupInfo(AbstractModel):
    """目标组信息

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组ID
        :type TargetGroupId: str
        :param _VpcId: 目标组的vpcid
        :type VpcId: str
        :param _TargetGroupName: 目标组的名字
        :type TargetGroupName: str
        :param _Port: 目标组的默认端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _CreatedTime: 目标组的创建时间
        :type CreatedTime: str
        :param _UpdatedTime: 目标组的修改时间
        :type UpdatedTime: str
        :param _AssociatedRule: 关联到的规则数组。在DescribeTargetGroupList接口调用时无法获取到该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociatedRule: list of AssociationItem
        :param _Protocol: 后端协议类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _ScheduleAlgorithm: 调度算法。
ip_hash_3：弹性哈希
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduleAlgorithm: str
        :param _HealthCheck: 健康检查详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheck: :class:`tencentcloud.gwlb.v20240906.models.TargetGroupHealthCheck`
        :param _AllDeadToAlive: 是否支持全死全活。
注意：此字段可能返回 null，表示取不到有效值。
        :type AllDeadToAlive: bool
        :param _AssociatedRuleCount: 目标组已关联的规则数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociatedRuleCount: int
        :param _RegisteredInstancesCount: 目标组内的实例数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type RegisteredInstancesCount: int
        """
        self._TargetGroupId = None
        self._VpcId = None
        self._TargetGroupName = None
        self._Port = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._AssociatedRule = None
        self._Protocol = None
        self._ScheduleAlgorithm = None
        self._HealthCheck = None
        self._AllDeadToAlive = None
        self._AssociatedRuleCount = None
        self._RegisteredInstancesCount = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def TargetGroupName(self):
        return self._TargetGroupName

    @TargetGroupName.setter
    def TargetGroupName(self, TargetGroupName):
        self._TargetGroupName = TargetGroupName

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def AssociatedRule(self):
        return self._AssociatedRule

    @AssociatedRule.setter
    def AssociatedRule(self, AssociatedRule):
        self._AssociatedRule = AssociatedRule

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ScheduleAlgorithm(self):
        return self._ScheduleAlgorithm

    @ScheduleAlgorithm.setter
    def ScheduleAlgorithm(self, ScheduleAlgorithm):
        self._ScheduleAlgorithm = ScheduleAlgorithm

    @property
    def HealthCheck(self):
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def AllDeadToAlive(self):
        return self._AllDeadToAlive

    @AllDeadToAlive.setter
    def AllDeadToAlive(self, AllDeadToAlive):
        self._AllDeadToAlive = AllDeadToAlive

    @property
    def AssociatedRuleCount(self):
        return self._AssociatedRuleCount

    @AssociatedRuleCount.setter
    def AssociatedRuleCount(self, AssociatedRuleCount):
        self._AssociatedRuleCount = AssociatedRuleCount

    @property
    def RegisteredInstancesCount(self):
        return self._RegisteredInstancesCount

    @RegisteredInstancesCount.setter
    def RegisteredInstancesCount(self, RegisteredInstancesCount):
        self._RegisteredInstancesCount = RegisteredInstancesCount


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._VpcId = params.get("VpcId")
        self._TargetGroupName = params.get("TargetGroupName")
        self._Port = params.get("Port")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        if params.get("AssociatedRule") is not None:
            self._AssociatedRule = []
            for item in params.get("AssociatedRule"):
                obj = AssociationItem()
                obj._deserialize(item)
                self._AssociatedRule.append(obj)
        self._Protocol = params.get("Protocol")
        self._ScheduleAlgorithm = params.get("ScheduleAlgorithm")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = TargetGroupHealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        self._AllDeadToAlive = params.get("AllDeadToAlive")
        self._AssociatedRuleCount = params.get("AssociatedRuleCount")
        self._RegisteredInstancesCount = params.get("RegisteredInstancesCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupInstance(AbstractModel):
    """目标组实例

    """

    def __init__(self):
        r"""
        :param _BindIP: 目标组实例的内网IP。
        :type BindIP: str
        :param _Port: 目标组实例的端口，只支持6081。
        :type Port: int
        :param _Weight: 目标组实例的权重，只支持0或16，非0统一按16处理。
        :type Weight: int
        """
        self._BindIP = None
        self._Port = None
        self._Weight = None

    @property
    def BindIP(self):
        return self._BindIP

    @BindIP.setter
    def BindIP(self, BindIP):
        self._BindIP = BindIP

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._BindIP = params.get("BindIP")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupInstanceStatus(AbstractModel):
    """用于目标组后端rs健康检查状态。

    """

    def __init__(self):
        r"""
        :param _InstanceIp: 后端rs的IP
        :type InstanceIp: str
        :param _Status: 健康检查状态，参数值及含义如下：
● on：表示探测中。
● off：表示健康检查关闭。
● health：表示健康。
● unhealth：表示异常。
        :type Status: str
        """
        self._InstanceIp = None
        self._Status = None

    @property
    def InstanceIp(self):
        return self._InstanceIp

    @InstanceIp.setter
    def InstanceIp(self, InstanceIp):
        self._InstanceIp = InstanceIp

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InstanceIp = params.get("InstanceIp")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        