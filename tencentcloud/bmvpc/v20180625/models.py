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


class AcceptVpcPeerConnectionRequest(AbstractModel):
    """AcceptVpcPeerConnection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcPeerConnectionId: 黑石对等连接实例ID
        :type VpcPeerConnectionId: str
        """
        self._VpcPeerConnectionId = None

    @property
    def VpcPeerConnectionId(self):
        return self._VpcPeerConnectionId

    @VpcPeerConnectionId.setter
    def VpcPeerConnectionId(self, VpcPeerConnectionId):
        self._VpcPeerConnectionId = VpcPeerConnectionId


    def _deserialize(self, params):
        self._VpcPeerConnectionId = params.get("VpcPeerConnectionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcceptVpcPeerConnectionResponse(AbstractModel):
    """AcceptVpcPeerConnection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class AsyncRegisterIpsRequest(AbstractModel):
    """AsyncRegisterIps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络的唯一ID。
        :type VpcId: str
        :param _SubnetId: 子网唯一ID。
        :type SubnetId: str
        :param _Ips: 需要注册的IP列表。
        :type Ips: list of str
        """
        self._VpcId = None
        self._SubnetId = None
        self._Ips = None

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
    def Ips(self):
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Ips = params.get("Ips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsyncRegisterIpsResponse(AbstractModel):
    """AsyncRegisterIps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class BindEipsToNatGatewayRequest(AbstractModel):
    """BindEipsToNatGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param _VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param _AssignedEips: 已分配的EIP列表；AssignedEips和AutoAllocEipNum至少输入一个
        :type AssignedEips: list of str
        :param _AutoAllocEipNum: 新建EIP数目，系统将会按您的要求生产该数目个数EIP；AssignedEips和AutoAllocEipNum至少输入一个
        :type AutoAllocEipNum: int
        """
        self._NatId = None
        self._VpcId = None
        self._AssignedEips = None
        self._AutoAllocEipNum = None

    @property
    def NatId(self):
        return self._NatId

    @NatId.setter
    def NatId(self, NatId):
        self._NatId = NatId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def AssignedEips(self):
        return self._AssignedEips

    @AssignedEips.setter
    def AssignedEips(self, AssignedEips):
        self._AssignedEips = AssignedEips

    @property
    def AutoAllocEipNum(self):
        return self._AutoAllocEipNum

    @AutoAllocEipNum.setter
    def AutoAllocEipNum(self, AutoAllocEipNum):
        self._AutoAllocEipNum = AutoAllocEipNum


    def _deserialize(self, params):
        self._NatId = params.get("NatId")
        self._VpcId = params.get("VpcId")
        self._AssignedEips = params.get("AssignedEips")
        self._AutoAllocEipNum = params.get("AutoAllocEipNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindEipsToNatGatewayResponse(AbstractModel):
    """BindEipsToNatGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class BindIpsToNatGatewayRequest(AbstractModel):
    """BindIpsToNatGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param _VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param _IpInfoSet: 部分IP信息，子网下只有该部分IP将加入NAT，仅当网关转发模式为IP方式有效
        :type IpInfoSet: list of IpInfo
        """
        self._NatId = None
        self._VpcId = None
        self._IpInfoSet = None

    @property
    def NatId(self):
        return self._NatId

    @NatId.setter
    def NatId(self, NatId):
        self._NatId = NatId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def IpInfoSet(self):
        return self._IpInfoSet

    @IpInfoSet.setter
    def IpInfoSet(self, IpInfoSet):
        self._IpInfoSet = IpInfoSet


    def _deserialize(self, params):
        self._NatId = params.get("NatId")
        self._VpcId = params.get("VpcId")
        if params.get("IpInfoSet") is not None:
            self._IpInfoSet = []
            for item in params.get("IpInfoSet"):
                obj = IpInfo()
                obj._deserialize(item)
                self._IpInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindIpsToNatGatewayResponse(AbstractModel):
    """BindIpsToNatGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class BindSubnetsToNatGatewayRequest(AbstractModel):
    """BindSubnetsToNatGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param _VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param _SubnetIds: 子网ID列表，子网下全部IP将加入NAT，不区分网关转发方式
        :type SubnetIds: list of str
        """
        self._NatId = None
        self._VpcId = None
        self._SubnetIds = None

    @property
    def NatId(self):
        return self._NatId

    @NatId.setter
    def NatId(self, NatId):
        self._NatId = NatId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds


    def _deserialize(self, params):
        self._NatId = params.get("NatId")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindSubnetsToNatGatewayResponse(AbstractModel):
    """BindSubnetsToNatGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateCustomerGatewayRequest(AbstractModel):
    """CreateCustomerGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomerGatewayName: 对端网关名称，可任意命名，但不得超过60个字符。
        :type CustomerGatewayName: str
        :param _IpAddress: 对端网关公网IP。
        :type IpAddress: str
        :param _Zone: 可用区ID
        :type Zone: str
        """
        self._CustomerGatewayName = None
        self._IpAddress = None
        self._Zone = None

    @property
    def CustomerGatewayName(self):
        return self._CustomerGatewayName

    @CustomerGatewayName.setter
    def CustomerGatewayName(self, CustomerGatewayName):
        self._CustomerGatewayName = CustomerGatewayName

    @property
    def IpAddress(self):
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._CustomerGatewayName = params.get("CustomerGatewayName")
        self._IpAddress = params.get("IpAddress")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomerGatewayResponse(AbstractModel):
    """CreateCustomerGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomerGateway: 对端网关对象
        :type CustomerGateway: :class:`tencentcloud.bmvpc.v20180625.models.CustomerGateway`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CustomerGateway = None
        self._RequestId = None

    @property
    def CustomerGateway(self):
        return self._CustomerGateway

    @CustomerGateway.setter
    def CustomerGateway(self, CustomerGateway):
        self._CustomerGateway = CustomerGateway

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CustomerGateway") is not None:
            self._CustomerGateway = CustomerGateway()
            self._CustomerGateway._deserialize(params.get("CustomerGateway"))
        self._RequestId = params.get("RequestId")


class CreateDockerSubnetWithVlanRequest(AbstractModel):
    """CreateDockerSubnetWithVlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 系统分配的私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param _SubnetSet: 子网信息
        :type SubnetSet: list of SubnetCreateInputInfo
        """
        self._VpcId = None
        self._SubnetSet = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetSet(self):
        return self._SubnetSet

    @SubnetSet.setter
    def SubnetSet(self, SubnetSet):
        self._SubnetSet = SubnetSet


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        if params.get("SubnetSet") is not None:
            self._SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = SubnetCreateInputInfo()
                obj._deserialize(item)
                self._SubnetSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDockerSubnetWithVlanResponse(AbstractModel):
    """CreateDockerSubnetWithVlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateHostedInterfaceRequest(AbstractModel):
    """CreateHostedInterface请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 托管机器唯一ID 数组
        :type InstanceIds: list of str
        :param _VpcId: 私有网络ID或者私有网络统一ID，建议使用统一ID
        :type VpcId: str
        :param _SubnetId: 子网ID或者子网统一ID，建议使用统一ID
        :type SubnetId: str
        """
        self._InstanceIds = None
        self._VpcId = None
        self._SubnetId = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

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


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHostedInterfaceResponse(AbstractModel):
    """CreateHostedInterface返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID
        :type TaskId: int
        :param _ResourceIds: 黑石托管机器ID
        :type ResourceIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._ResourceIds = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ResourceIds = params.get("ResourceIds")
        self._RequestId = params.get("RequestId")


class CreateInterfacesRequest(AbstractModel):
    """CreateInterfaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 物理机实例ID列表
        :type InstanceIds: list of str
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        """
        self._InstanceIds = None
        self._VpcId = None
        self._SubnetId = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

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


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInterfacesResponse(AbstractModel):
    """CreateInterfaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateNatGatewayRequest(AbstractModel):
    """CreateNatGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ForwardMode: 转发模式，其中0表示IP方式，1表示网段方式；通过cidr方式可支持更多的IP接入到NAT网关
        :type ForwardMode: str
        :param _VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param _NatName: NAT名称
        :type NatName: str
        :param _MaxConcurrent: 并发连接数规格；取值为1000000、3000000、10000000，分别对应小型、中型、大型NAT网关
        :type MaxConcurrent: int
        :param _SubnetIds: 子网ID列表，子网下全部IP将加入NAT，不区分网关转发方式
        :type SubnetIds: list of str
        :param _IpInfoSet: 部分IP信息，子网下只有该部分IP将加入NAT，仅当网关转发模式为IP方式有效；IpInfoSet和SubnetIds中的子网ID不能同时存在
        :type IpInfoSet: list of IpInfo
        :param _AssignedEips: 已分配的EIP列表, AssignedEips和AutoAllocEipNum至少输入一个
        :type AssignedEips: list of str
        :param _AutoAllocEipNum: 新建EIP数目，系统将会按您的要求生产该数目个数EIP, AssignedEips和AutoAllocEipNum至少输入一个
        :type AutoAllocEipNum: int
        :param _Exclusive: 独占标识，取值为0和1，默认值为0；0和1分别表示创建共享型NAT网关和独占NAT型网关；由于同一个VPC网络内，指向NAT集群的默认路由只有一条，因此VPC内只能创建一种类型NAT网关；创建独占型NAT网关时，需联系对应架构师进行独占NAT集群搭建，否则无法创建独占型NAT网关。
        :type Exclusive: int
        """
        self._ForwardMode = None
        self._VpcId = None
        self._NatName = None
        self._MaxConcurrent = None
        self._SubnetIds = None
        self._IpInfoSet = None
        self._AssignedEips = None
        self._AutoAllocEipNum = None
        self._Exclusive = None

    @property
    def ForwardMode(self):
        return self._ForwardMode

    @ForwardMode.setter
    def ForwardMode(self, ForwardMode):
        self._ForwardMode = ForwardMode

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def NatName(self):
        return self._NatName

    @NatName.setter
    def NatName(self, NatName):
        self._NatName = NatName

    @property
    def MaxConcurrent(self):
        return self._MaxConcurrent

    @MaxConcurrent.setter
    def MaxConcurrent(self, MaxConcurrent):
        self._MaxConcurrent = MaxConcurrent

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def IpInfoSet(self):
        return self._IpInfoSet

    @IpInfoSet.setter
    def IpInfoSet(self, IpInfoSet):
        self._IpInfoSet = IpInfoSet

    @property
    def AssignedEips(self):
        return self._AssignedEips

    @AssignedEips.setter
    def AssignedEips(self, AssignedEips):
        self._AssignedEips = AssignedEips

    @property
    def AutoAllocEipNum(self):
        return self._AutoAllocEipNum

    @AutoAllocEipNum.setter
    def AutoAllocEipNum(self, AutoAllocEipNum):
        self._AutoAllocEipNum = AutoAllocEipNum

    @property
    def Exclusive(self):
        return self._Exclusive

    @Exclusive.setter
    def Exclusive(self, Exclusive):
        self._Exclusive = Exclusive


    def _deserialize(self, params):
        self._ForwardMode = params.get("ForwardMode")
        self._VpcId = params.get("VpcId")
        self._NatName = params.get("NatName")
        self._MaxConcurrent = params.get("MaxConcurrent")
        self._SubnetIds = params.get("SubnetIds")
        if params.get("IpInfoSet") is not None:
            self._IpInfoSet = []
            for item in params.get("IpInfoSet"):
                obj = IpInfo()
                obj._deserialize(item)
                self._IpInfoSet.append(obj)
        self._AssignedEips = params.get("AssignedEips")
        self._AutoAllocEipNum = params.get("AutoAllocEipNum")
        self._Exclusive = params.get("Exclusive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNatGatewayResponse(AbstractModel):
    """CreateNatGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateRoutePoliciesRequest(AbstractModel):
    """CreateRoutePolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteTableId: 路由表ID
        :type RouteTableId: str
        :param _RoutePolicySet: 新增的路由
        :type RoutePolicySet: list of RoutePolicy
        """
        self._RouteTableId = None
        self._RoutePolicySet = None

    @property
    def RouteTableId(self):
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def RoutePolicySet(self):
        return self._RoutePolicySet

    @RoutePolicySet.setter
    def RoutePolicySet(self, RoutePolicySet):
        self._RoutePolicySet = RoutePolicySet


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        if params.get("RoutePolicySet") is not None:
            self._RoutePolicySet = []
            for item in params.get("RoutePolicySet"):
                obj = RoutePolicy()
                obj._deserialize(item)
                self._RoutePolicySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoutePoliciesResponse(AbstractModel):
    """CreateRoutePolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateSubnetRequest(AbstractModel):
    """CreateSubnet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 系统分配的私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param _SubnetSet: 子网信息
        :type SubnetSet: list of SubnetCreateInputInfo
        """
        self._VpcId = None
        self._SubnetSet = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetSet(self):
        return self._SubnetSet

    @SubnetSet.setter
    def SubnetSet(self, SubnetSet):
        self._SubnetSet = SubnetSet


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        if params.get("SubnetSet") is not None:
            self._SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = SubnetCreateInputInfo()
                obj._deserialize(item)
                self._SubnetSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubnetResponse(AbstractModel):
    """CreateSubnet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateVirtualSubnetWithVlanRequest(AbstractModel):
    """CreateVirtualSubnetWithVlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 系统分配的私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param _SubnetSet: 子网信息
        :type SubnetSet: list of SubnetCreateInputInfo
        """
        self._VpcId = None
        self._SubnetSet = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetSet(self):
        return self._SubnetSet

    @SubnetSet.setter
    def SubnetSet(self, SubnetSet):
        self._SubnetSet = SubnetSet


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        if params.get("SubnetSet") is not None:
            self._SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = SubnetCreateInputInfo()
                obj._deserialize(item)
                self._SubnetSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVirtualSubnetWithVlanResponse(AbstractModel):
    """CreateVirtualSubnetWithVlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateVpcPeerConnectionRequest(AbstractModel):
    """CreateVpcPeerConnection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 本端VPC唯一ID
        :type VpcId: str
        :param _PeerVpcId: 对端VPC唯一ID
        :type PeerVpcId: str
        :param _PeerRegion: 对端地域，取值范围为gz,sh,bj,hk,cd,de,sh_bm,gz_bm,bj_bm,cq_bm等
        :type PeerRegion: str
        :param _VpcPeerConnectionName: 对等连接名称
        :type VpcPeerConnectionName: str
        :param _PeerUin: 对端账户OwnerUin（默认值为本端账户）
        :type PeerUin: str
        :param _Bandwidth: 跨地域必传，带宽上限值
        :type Bandwidth: int
        """
        self._VpcId = None
        self._PeerVpcId = None
        self._PeerRegion = None
        self._VpcPeerConnectionName = None
        self._PeerUin = None
        self._Bandwidth = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def PeerVpcId(self):
        return self._PeerVpcId

    @PeerVpcId.setter
    def PeerVpcId(self, PeerVpcId):
        self._PeerVpcId = PeerVpcId

    @property
    def PeerRegion(self):
        return self._PeerRegion

    @PeerRegion.setter
    def PeerRegion(self, PeerRegion):
        self._PeerRegion = PeerRegion

    @property
    def VpcPeerConnectionName(self):
        return self._VpcPeerConnectionName

    @VpcPeerConnectionName.setter
    def VpcPeerConnectionName(self, VpcPeerConnectionName):
        self._VpcPeerConnectionName = VpcPeerConnectionName

    @property
    def PeerUin(self):
        return self._PeerUin

    @PeerUin.setter
    def PeerUin(self, PeerUin):
        self._PeerUin = PeerUin

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._PeerVpcId = params.get("PeerVpcId")
        self._PeerRegion = params.get("PeerRegion")
        self._VpcPeerConnectionName = params.get("VpcPeerConnectionName")
        self._PeerUin = params.get("PeerUin")
        self._Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpcPeerConnectionResponse(AbstractModel):
    """CreateVpcPeerConnection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateVpcRequest(AbstractModel):
    """CreateVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcName: 私有网络的名称
        :type VpcName: str
        :param _CidrBlock: 私有网络的CIDR
        :type CidrBlock: str
        :param _Zone: 私有网络的可用区
        :type Zone: str
        :param _SubnetSet: 子网信息
        :type SubnetSet: list of VpcSubnetCreateInfo
        :param _EnableMonitoring: 是否启用内网监控
        :type EnableMonitoring: bool
        """
        self._VpcName = None
        self._CidrBlock = None
        self._Zone = None
        self._SubnetSet = None
        self._EnableMonitoring = None

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SubnetSet(self):
        return self._SubnetSet

    @SubnetSet.setter
    def SubnetSet(self, SubnetSet):
        self._SubnetSet = SubnetSet

    @property
    def EnableMonitoring(self):
        return self._EnableMonitoring

    @EnableMonitoring.setter
    def EnableMonitoring(self, EnableMonitoring):
        self._EnableMonitoring = EnableMonitoring


    def _deserialize(self, params):
        self._VpcName = params.get("VpcName")
        self._CidrBlock = params.get("CidrBlock")
        self._Zone = params.get("Zone")
        if params.get("SubnetSet") is not None:
            self._SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = VpcSubnetCreateInfo()
                obj._deserialize(item)
                self._SubnetSet.append(obj)
        self._EnableMonitoring = params.get("EnableMonitoring")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpcResponse(AbstractModel):
    """CreateVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CustomerGateway(AbstractModel):
    """对端网关

    """

    def __init__(self):
        r"""
        :param _CustomerGatewayId: 用户网关唯一ID
        :type CustomerGatewayId: str
        :param _CustomerGatewayName: 网关名称
        :type CustomerGatewayName: str
        :param _IpAddress: 公网地址
        :type IpAddress: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _VpnConnNum: VPN通道引用个数
注意：此字段可能返回 null，表示取不到有效值。
        :type VpnConnNum: int
        """
        self._CustomerGatewayId = None
        self._CustomerGatewayName = None
        self._IpAddress = None
        self._CreateTime = None
        self._VpnConnNum = None

    @property
    def CustomerGatewayId(self):
        return self._CustomerGatewayId

    @CustomerGatewayId.setter
    def CustomerGatewayId(self, CustomerGatewayId):
        self._CustomerGatewayId = CustomerGatewayId

    @property
    def CustomerGatewayName(self):
        return self._CustomerGatewayName

    @CustomerGatewayName.setter
    def CustomerGatewayName(self, CustomerGatewayName):
        self._CustomerGatewayName = CustomerGatewayName

    @property
    def IpAddress(self):
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def VpnConnNum(self):
        return self._VpnConnNum

    @VpnConnNum.setter
    def VpnConnNum(self, VpnConnNum):
        self._VpnConnNum = VpnConnNum


    def _deserialize(self, params):
        self._CustomerGatewayId = params.get("CustomerGatewayId")
        self._CustomerGatewayName = params.get("CustomerGatewayName")
        self._IpAddress = params.get("IpAddress")
        self._CreateTime = params.get("CreateTime")
        self._VpnConnNum = params.get("VpnConnNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomerGatewayRequest(AbstractModel):
    """DeleteCustomerGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomerGatewayId: 对端网关ID，例如：bmcgw-2wqq41m9，可通过DescribeCustomerGateways接口查询对端网关。
        :type CustomerGatewayId: str
        """
        self._CustomerGatewayId = None

    @property
    def CustomerGatewayId(self):
        return self._CustomerGatewayId

    @CustomerGatewayId.setter
    def CustomerGatewayId(self, CustomerGatewayId):
        self._CustomerGatewayId = CustomerGatewayId


    def _deserialize(self, params):
        self._CustomerGatewayId = params.get("CustomerGatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomerGatewayResponse(AbstractModel):
    """DeleteCustomerGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DeleteHostedInterfaceRequest(AbstractModel):
    """DeleteHostedInterface请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 托管机器唯一ID 数组
        :type InstanceIds: list of str
        :param _VpcId: 私有网络ID或者私有网络统一ID，建议使用统一ID
        :type VpcId: str
        :param _SubnetId: 子网ID或者子网统一ID，建议使用统一ID
        :type SubnetId: str
        """
        self._InstanceIds = None
        self._VpcId = None
        self._SubnetId = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

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


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHostedInterfaceResponse(AbstractModel):
    """DeleteHostedInterface返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID
        :type TaskId: int
        :param _ResourceIds: 黑石托管机器ID
        :type ResourceIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._ResourceIds = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ResourceIds = params.get("ResourceIds")
        self._RequestId = params.get("RequestId")


class DeleteHostedInterfacesRequest(AbstractModel):
    """DeleteHostedInterfaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 物理机ID
        :type InstanceId: str
        :param _SubnetIds: 物理机ID
        :type SubnetIds: list of str
        """
        self._InstanceId = None
        self._SubnetIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SubnetIds = params.get("SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHostedInterfacesResponse(AbstractModel):
    """DeleteHostedInterfaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteInterfacesRequest(AbstractModel):
    """DeleteInterfaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 物理机ID
        :type InstanceId: str
        :param _SubnetIds: 子网的唯一ID列表
        :type SubnetIds: list of str
        """
        self._InstanceId = None
        self._SubnetIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SubnetIds = params.get("SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInterfacesResponse(AbstractModel):
    """DeleteInterfaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteNatGatewayRequest(AbstractModel):
    """DeleteNatGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param _VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        """
        self._NatId = None
        self._VpcId = None

    @property
    def NatId(self):
        return self._NatId

    @NatId.setter
    def NatId(self, NatId):
        self._NatId = NatId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._NatId = params.get("NatId")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNatGatewayResponse(AbstractModel):
    """DeleteNatGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteRoutePolicyRequest(AbstractModel):
    """DeleteRoutePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteTableId: 路由表ID
        :type RouteTableId: str
        :param _RoutePolicyId: 路由表策略ID
        :type RoutePolicyId: str
        """
        self._RouteTableId = None
        self._RoutePolicyId = None

    @property
    def RouteTableId(self):
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def RoutePolicyId(self):
        return self._RoutePolicyId

    @RoutePolicyId.setter
    def RoutePolicyId(self, RoutePolicyId):
        self._RoutePolicyId = RoutePolicyId


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        self._RoutePolicyId = params.get("RoutePolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoutePolicyResponse(AbstractModel):
    """DeleteRoutePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteSubnetRequest(AbstractModel):
    """DeleteSubnet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :type VpcId: str
        :param _SubnetId: 子网实例ID。可通过DescribeSubnets接口返回值中的SubnetId获取。
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

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


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSubnetResponse(AbstractModel):
    """DeleteSubnet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteVirtualIpRequest(AbstractModel):
    """DeleteVirtualIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络唯一ID。
        :type VpcId: str
        :param _Ips: 退还的IP列表。
        :type Ips: list of str
        """
        self._VpcId = None
        self._Ips = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Ips(self):
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._Ips = params.get("Ips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVirtualIpResponse(AbstractModel):
    """DeleteVirtualIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteVpcPeerConnectionRequest(AbstractModel):
    """DeleteVpcPeerConnection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcPeerConnectionId: 黑石对等连接实例ID
        :type VpcPeerConnectionId: str
        """
        self._VpcPeerConnectionId = None

    @property
    def VpcPeerConnectionId(self):
        return self._VpcPeerConnectionId

    @VpcPeerConnectionId.setter
    def VpcPeerConnectionId(self, VpcPeerConnectionId):
        self._VpcPeerConnectionId = VpcPeerConnectionId


    def _deserialize(self, params):
        self._VpcPeerConnectionId = params.get("VpcPeerConnectionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpcPeerConnectionResponse(AbstractModel):
    """DeleteVpcPeerConnection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteVpcRequest(AbstractModel):
    """DeleteVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :type VpcId: str
        """
        self._VpcId = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpcResponse(AbstractModel):
    """DeleteVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteVpnConnectionRequest(AbstractModel):
    """DeleteVpnConnection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpnConnectionId: VPN通道实例ID。形如：bmvpnx-f49l6u0z。
        :type VpnConnectionId: str
        """
        self._VpnConnectionId = None

    @property
    def VpnConnectionId(self):
        return self._VpnConnectionId

    @VpnConnectionId.setter
    def VpnConnectionId(self, VpnConnectionId):
        self._VpnConnectionId = VpnConnectionId


    def _deserialize(self, params):
        self._VpnConnectionId = params.get("VpnConnectionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpnConnectionResponse(AbstractModel):
    """DeleteVpnConnection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteVpnGatewayRequest(AbstractModel):
    """DeleteVpnGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpnGatewayId: VPN网关实例ID。
        :type VpnGatewayId: str
        """
        self._VpnGatewayId = None

    @property
    def VpnGatewayId(self):
        return self._VpnGatewayId

    @VpnGatewayId.setter
    def VpnGatewayId(self, VpnGatewayId):
        self._VpnGatewayId = VpnGatewayId


    def _deserialize(self, params):
        self._VpnGatewayId = params.get("VpnGatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpnGatewayResponse(AbstractModel):
    """DeleteVpnGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeregisterIpsRequest(AbstractModel):
    """DeregisterIps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _IpSet: 注销指定IP的列表
        :type IpSet: list of str
        :param _SubnetId: 私有网络子网ID
        :type SubnetId: str
        """
        self._VpcId = None
        self._IpSet = None
        self._SubnetId = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def IpSet(self):
        return self._IpSet

    @IpSet.setter
    def IpSet(self, IpSet):
        self._IpSet = IpSet

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._IpSet = params.get("IpSet")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeregisterIpsResponse(AbstractModel):
    """DeregisterIps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeCustomerGatewaysRequest(AbstractModel):
    """DescribeCustomerGateways请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomerGatewayIds: 对端网关ID，例如：bmcgw-2wqq41m9。每次请求的实例的上限为100。参数不支持同时指定CustomerGatewayIds和Filters。
        :type CustomerGatewayIds: list of str
        :param _Filters: 过滤条件，详见下表：实例过滤条件表。每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定CustomerGatewayIds和Filters。
<li>customergateway-name - String - （过滤条件）对端网关名称。</li>
<li>ip-address - String - （过滤条件)对端网关地址。</li>
<li>customergateway-id - String - （过滤条件）对端网关唯一ID。</li>
<li>zone - String - （过滤条件）对端所在可用区，形如：ap-guangzhou-2。</li>
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _OrderField: 排序字段, 支持"CreateTime"排序
        :type OrderField: str
        :param _OrderDirection: 排序方向, “asc”、“desc”
        :type OrderDirection: str
        """
        self._CustomerGatewayIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._OrderDirection = None

    @property
    def CustomerGatewayIds(self):
        return self._CustomerGatewayIds

    @CustomerGatewayIds.setter
    def CustomerGatewayIds(self, CustomerGatewayIds):
        self._CustomerGatewayIds = CustomerGatewayIds

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

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._CustomerGatewayIds = params.get("CustomerGatewayIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomerGatewaysResponse(AbstractModel):
    """DescribeCustomerGateways返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomerGatewaySet: 对端网关对象列表
        :type CustomerGatewaySet: list of CustomerGateway
        :param _TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CustomerGatewaySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def CustomerGatewaySet(self):
        return self._CustomerGatewaySet

    @CustomerGatewaySet.setter
    def CustomerGatewaySet(self, CustomerGatewaySet):
        self._CustomerGatewaySet = CustomerGatewaySet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CustomerGatewaySet") is not None:
            self._CustomerGatewaySet = []
            for item in params.get("CustomerGatewaySet"):
                obj = CustomerGateway()
                obj._deserialize(item)
                self._CustomerGatewaySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeNatGatewaysRequest(AbstractModel):
    """DescribeNatGateways请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param _NatName: NAT名称
        :type NatName: str
        :param _SearchKey: 搜索字段
        :type SearchKey: str
        :param _VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param _Offset: 起始值
        :type Offset: int
        :param _Limit: 偏移值，默认值为 20
        :type Limit: int
        :param _Zone: NAT所在可用区，形如：ap-guangzhou-2。
        :type Zone: str
        :param _OrderField: 排序字段, 支持"CreateTime"排序
        :type OrderField: str
        :param _OrderDirection: 排序方向, “asc”、“desc”
        :type OrderDirection: str
        """
        self._NatId = None
        self._NatName = None
        self._SearchKey = None
        self._VpcId = None
        self._Offset = None
        self._Limit = None
        self._Zone = None
        self._OrderField = None
        self._OrderDirection = None

    @property
    def NatId(self):
        return self._NatId

    @NatId.setter
    def NatId(self, NatId):
        self._NatId = NatId

    @property
    def NatName(self):
        return self._NatName

    @NatName.setter
    def NatName(self, NatName):
        self._NatName = NatName

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

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

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._NatId = params.get("NatId")
        self._NatName = params.get("NatName")
        self._SearchKey = params.get("SearchKey")
        self._VpcId = params.get("VpcId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Zone = params.get("Zone")
        self._OrderField = params.get("OrderField")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNatGatewaysResponse(AbstractModel):
    """DescribeNatGateways返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NatGatewayInfoSet: NAT网关信息列表
        :type NatGatewayInfoSet: list of NatGatewayInfo
        :param _TotalCount: 总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NatGatewayInfoSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NatGatewayInfoSet(self):
        return self._NatGatewayInfoSet

    @NatGatewayInfoSet.setter
    def NatGatewayInfoSet(self, NatGatewayInfoSet):
        self._NatGatewayInfoSet = NatGatewayInfoSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NatGatewayInfoSet") is not None:
            self._NatGatewayInfoSet = []
            for item in params.get("NatGatewayInfoSet"):
                obj = NatGatewayInfo()
                obj._deserialize(item)
                self._NatGatewayInfoSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeNatSubnetsRequest(AbstractModel):
    """DescribeNatSubnets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param _VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        """
        self._NatId = None
        self._VpcId = None

    @property
    def NatId(self):
        return self._NatId

    @NatId.setter
    def NatId(self, NatId):
        self._NatId = NatId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._NatId = params.get("NatId")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNatSubnetsResponse(AbstractModel):
    """DescribeNatSubnets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NatSubnetInfoSet: NAT子网信息
        :type NatSubnetInfoSet: list of NatSubnetInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NatSubnetInfoSet = None
        self._RequestId = None

    @property
    def NatSubnetInfoSet(self):
        return self._NatSubnetInfoSet

    @NatSubnetInfoSet.setter
    def NatSubnetInfoSet(self, NatSubnetInfoSet):
        self._NatSubnetInfoSet = NatSubnetInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NatSubnetInfoSet") is not None:
            self._NatSubnetInfoSet = []
            for item in params.get("NatSubnetInfoSet"):
                obj = NatSubnetInfo()
                obj._deserialize(item)
                self._NatSubnetInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRoutePoliciesRequest(AbstractModel):
    """DescribeRoutePolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteTableId: 路由表实例ID，例如：rtb-afg8md3c。
        :type RouteTableId: str
        :param _RoutePolicyIds: 路由策略实例ID，例如：rti-azd4dt1c。
        :type RoutePolicyIds: list of str
        :param _Filters: 过滤条件，参数不支持同时指定RoutePolicyIds和Filters。
route-table-id - String - （过滤条件）路由表实例ID。
vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。
route-policy-id - String - （过滤条件）路由策略ID。
route-policy-description-like - String -（过滤条件）路由项备注。
route-policy-type - String - （过滤条件）路由项策略类型。
destination-cidr-like - String - （过滤条件）路由项目的地址。
gateway-id-like - String - （过滤条件）路由项下一跳网关。
gateway-type - String - （过滤条件）路由项下一条网关类型。
enable - Bool - （过滤条件）路由策略是否启用。
        :type Filters: list of Filter
        :param _Offset: 初始行的偏移量，默认为0。
        :type Offset: int
        :param _Limit: 每页行数，默认为20。
        :type Limit: int
        """
        self._RouteTableId = None
        self._RoutePolicyIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def RouteTableId(self):
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def RoutePolicyIds(self):
        return self._RoutePolicyIds

    @RoutePolicyIds.setter
    def RoutePolicyIds(self, RoutePolicyIds):
        self._RoutePolicyIds = RoutePolicyIds

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
        self._RouteTableId = params.get("RouteTableId")
        self._RoutePolicyIds = params.get("RoutePolicyIds")
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
        


class DescribeRoutePoliciesResponse(AbstractModel):
    """DescribeRoutePolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 路由策略数
        :type TotalCount: int
        :param _RoutePolicySet: 路由策略列表
        :type RoutePolicySet: list of RoutePolicy
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RoutePolicySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RoutePolicySet(self):
        return self._RoutePolicySet

    @RoutePolicySet.setter
    def RoutePolicySet(self, RoutePolicySet):
        self._RoutePolicySet = RoutePolicySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RoutePolicySet") is not None:
            self._RoutePolicySet = []
            for item in params.get("RoutePolicySet"):
                obj = RoutePolicy()
                obj._deserialize(item)
                self._RoutePolicySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRouteTablesRequest(AbstractModel):
    """DescribeRouteTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteTableIds: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableIds: list of str
        :param _Filters: 过滤条件，参数不支持同时指定RouteTableIds和Filters。
route-table-id - String - （过滤条件）路由表实例ID。
route-table-name - String - （过滤条件）路由表名称。
route-table-id-like - String - （模糊过滤条件）路由表实例ID。
route-table-name-like - String - （模糊过滤条件）路由表名称。
vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。
zone - String - （过滤条件）可用区。
        :type Filters: list of Filter
        :param _Offset: 初始行的偏移量，默认为0。
        :type Offset: int
        :param _Limit: 每页行数，默认为20。
        :type Limit: int
        :param _OrderField: 排序字段, 支持按“RouteTableId”，“VpcId”, "RouteTableName", "CreateTime"
        :type OrderField: str
        :param _OrderDirection: 排序方向, “asc”、“desc”
        :type OrderDirection: str
        """
        self._RouteTableIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._OrderDirection = None

    @property
    def RouteTableIds(self):
        return self._RouteTableIds

    @RouteTableIds.setter
    def RouteTableIds(self, RouteTableIds):
        self._RouteTableIds = RouteTableIds

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

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._RouteTableIds = params.get("RouteTableIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteTablesResponse(AbstractModel):
    """DescribeRouteTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 路由表个数
        :type TotalCount: int
        :param _RouteTableSet: 路由表列表
        :type RouteTableSet: list of RouteTable
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RouteTableSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RouteTableSet(self):
        return self._RouteTableSet

    @RouteTableSet.setter
    def RouteTableSet(self, RouteTableSet):
        self._RouteTableSet = RouteTableSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RouteTableSet") is not None:
            self._RouteTableSet = []
            for item in params.get("RouteTableSet"):
                obj = RouteTable()
                obj._deserialize(item)
                self._RouteTableSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubnetAvailableIpsRequest(AbstractModel):
    """DescribeSubnetAvailableIps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubnetId: 私有网络子网ID
        :type SubnetId: str
        :param _Cidr: CIDR前缀，例如10.0.1
        :type Cidr: str
        """
        self._SubnetId = None
        self._Cidr = None

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Cidr(self):
        return self._Cidr

    @Cidr.setter
    def Cidr(self, Cidr):
        self._Cidr = Cidr


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._Cidr = params.get("Cidr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubnetAvailableIpsResponse(AbstractModel):
    """DescribeSubnetAvailableIps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IpSet: 可用IP的范围列表
        :type IpSet: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IpSet = None
        self._RequestId = None

    @property
    def IpSet(self):
        return self._IpSet

    @IpSet.setter
    def IpSet(self, IpSet):
        self._IpSet = IpSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IpSet = params.get("IpSet")
        self._RequestId = params.get("RequestId")


class DescribeSubnetByDeviceRequest(AbstractModel):
    """DescribeSubnetByDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 物理机ID
        :type InstanceId: str
        :param _Types: 子网类型。0: 物理机子网; 7: DOCKER子网 8: 虚拟子网
        :type Types: list of int non-negative
        :param _Offset: 查询的起始位置。
        :type Offset: int
        :param _Limit: 查询的个数。
        :type Limit: int
        """
        self._InstanceId = None
        self._Types = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Types(self):
        return self._Types

    @Types.setter
    def Types(self, Types):
        self._Types = Types

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
        self._InstanceId = params.get("InstanceId")
        self._Types = params.get("Types")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubnetByDeviceResponse(AbstractModel):
    """DescribeSubnetByDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 子网个数
        :type TotalCount: int
        :param _Data: 子网列表
        :type Data: list of SubnetInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SubnetInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubnetByHostedDeviceRequest(AbstractModel):
    """DescribeSubnetByHostedDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 托管机器ID, 如chm-xasdfx2j
        :type InstanceId: str
        :param _Types: 子网类型。0: 物理机子网; 7: DOCKER子网 8: 虚拟子网
        :type Types: list of int non-negative
        :param _Offset: 查询的起始位置。
        :type Offset: int
        :param _Limit: 查询的个数。
        :type Limit: int
        """
        self._InstanceId = None
        self._Types = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Types(self):
        return self._Types

    @Types.setter
    def Types(self, Types):
        self._Types = Types

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
        self._InstanceId = params.get("InstanceId")
        self._Types = params.get("Types")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubnetByHostedDeviceResponse(AbstractModel):
    """DescribeSubnetByHostedDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 子网个数
        :type TotalCount: int
        :param _Data: 子网列表
        :type Data: list of SubnetInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SubnetInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubnetsRequest(AbstractModel):
    """DescribeSubnets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubnetIds: 子网实例ID查询。形如：subnet-pxir56ns。参数不支持同时指定SubnetIds和Filters。
        :type SubnetIds: list of str
        :param _Filters: 过滤条件，参数不支持同时指定SubnetIds和Filters。
subnet-id - String - （过滤条件）Subnet实例名称。
vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。
cidr-block - String - （过滤条件）vpc的cidr。
subnet-name - String - （过滤条件）子网名称。
zone - String - （过滤条件）可用区。
        :type Filters: list of Filter
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回数量
        :type Limit: int
        :param _OrderField: 排序字段, 支持按“CreateTime”，“VlanId”
        :type OrderField: str
        :param _OrderDirection: 排序方向, “asc”、“desc”
        :type OrderDirection: str
        """
        self._SubnetIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._OrderDirection = None

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

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

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._SubnetIds = params.get("SubnetIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubnetsResponse(AbstractModel):
    """DescribeSubnets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubnetSet: 子网列表信息
        :type SubnetSet: list of SubnetInfo
        :param _TotalCount: 返回的子网总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubnetSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SubnetSet(self):
        return self._SubnetSet

    @SubnetSet.setter
    def SubnetSet(self, SubnetSet):
        self._SubnetSet = SubnetSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SubnetSet") is not None:
            self._SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = SubnetInfo()
                obj._deserialize(item)
                self._SubnetSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
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
        :param _Status: 任务状态，其中0表示任务执行成功，1表示任务执行失败，2表示任务正在执行中
        :type Status: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeVpcPeerConnectionsRequest(AbstractModel):
    """DescribeVpcPeerConnections请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcPeerConnectionIds: 对等连接实例ID
        :type VpcPeerConnectionIds: list of str
        :param _Filters: 过滤条件，详见下表：实例过滤条件表。每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定VpcPeerConnectionIds和Filters。
过滤条件，参数不支持同时指定VpcPeerConnectionIds和Filters。
<li>peer-name - String - （过滤条件）对等连接名称。</li>
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _VpcId: 私有网络ID
        :type VpcId: str
        """
        self._VpcPeerConnectionIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._VpcId = None

    @property
    def VpcPeerConnectionIds(self):
        return self._VpcPeerConnectionIds

    @VpcPeerConnectionIds.setter
    def VpcPeerConnectionIds(self, VpcPeerConnectionIds):
        self._VpcPeerConnectionIds = VpcPeerConnectionIds

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

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._VpcPeerConnectionIds = params.get("VpcPeerConnectionIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcPeerConnectionsResponse(AbstractModel):
    """DescribeVpcPeerConnections返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param _VpcPeerConnectionSet: 对等连接实例。
        :type VpcPeerConnectionSet: list of VpcPeerConnection
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VpcPeerConnectionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VpcPeerConnectionSet(self):
        return self._VpcPeerConnectionSet

    @VpcPeerConnectionSet.setter
    def VpcPeerConnectionSet(self, VpcPeerConnectionSet):
        self._VpcPeerConnectionSet = VpcPeerConnectionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("VpcPeerConnectionSet") is not None:
            self._VpcPeerConnectionSet = []
            for item in params.get("VpcPeerConnectionSet"):
                obj = VpcPeerConnection()
                obj._deserialize(item)
                self._VpcPeerConnectionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVpcQuotaRequest(AbstractModel):
    """DescribeVpcQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TypeIds: 类型
        :type TypeIds: list of int non-negative
        """
        self._TypeIds = None

    @property
    def TypeIds(self):
        return self._TypeIds

    @TypeIds.setter
    def TypeIds(self, TypeIds):
        self._TypeIds = TypeIds


    def _deserialize(self, params):
        self._TypeIds = params.get("TypeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcQuotaResponse(AbstractModel):
    """DescribeVpcQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcQuotaSet: 配额信息
        :type VpcQuotaSet: list of VpcQuota
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VpcQuotaSet = None
        self._RequestId = None

    @property
    def VpcQuotaSet(self):
        return self._VpcQuotaSet

    @VpcQuotaSet.setter
    def VpcQuotaSet(self, VpcQuotaSet):
        self._VpcQuotaSet = VpcQuotaSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("VpcQuotaSet") is not None:
            self._VpcQuotaSet = []
            for item in params.get("VpcQuotaSet"):
                obj = VpcQuota()
                obj._deserialize(item)
                self._VpcQuotaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVpcResourceRequest(AbstractModel):
    """DescribeVpcResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcIds: 私有网络实例ID
        :type VpcIds: list of str
        :param _Filters: 过滤条件，参数不支持同时指定SubnetIds和Filters。
vpc-id - String - （过滤条件）私有网络实例ID，形如：vpc-f49l6u0z。
vpc-name - String - （过滤条件）私有网络名称。
zone - String - （过滤条件）可用区。
state - String - （过滤条件）VPC状态。available: 运营中; pending: 创建中; failed: 创建失败; deleting: 删除中
        :type Filters: list of Filter
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回数量
        :type Limit: int
        :param _OrderField: 排序字段
        :type OrderField: str
        :param _OrderDirection: 排序方向, “asc”、“desc”
        :type OrderDirection: str
        """
        self._VpcIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._OrderDirection = None

    @property
    def VpcIds(self):
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

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

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._VpcIds = params.get("VpcIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcResourceResponse(AbstractModel):
    """DescribeVpcResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcResourceSet: VPC数据
        :type VpcResourceSet: list of VpcResource
        :param _TotalCount: VPC个数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VpcResourceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def VpcResourceSet(self):
        return self._VpcResourceSet

    @VpcResourceSet.setter
    def VpcResourceSet(self, VpcResourceSet):
        self._VpcResourceSet = VpcResourceSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("VpcResourceSet") is not None:
            self._VpcResourceSet = []
            for item in params.get("VpcResourceSet"):
                obj = VpcResource()
                obj._deserialize(item)
                self._VpcResourceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeVpcViewRequest(AbstractModel):
    """DescribeVpcView请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络唯一ID
        :type VpcId: str
        """
        self._VpcId = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcViewResponse(AbstractModel):
    """DescribeVpcView返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcView: VPC视图信息
        :type VpcView: :class:`tencentcloud.bmvpc.v20180625.models.VpcViewInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VpcView = None
        self._RequestId = None

    @property
    def VpcView(self):
        return self._VpcView

    @VpcView.setter
    def VpcView(self, VpcView):
        self._VpcView = VpcView

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("VpcView") is not None:
            self._VpcView = VpcViewInfo()
            self._VpcView._deserialize(params.get("VpcView"))
        self._RequestId = params.get("RequestId")


class DescribeVpcsRequest(AbstractModel):
    """DescribeVpcs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcIds: VPC实例ID。形如：vpc-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpcIds和Filters。
        :type VpcIds: list of str
        :param _Filters: 过滤条件，参数不支持同时指定VpcIds和Filters。
vpc-name - String - （过滤条件）VPC实例名称。
vpc-id - String - （过滤条件）VPC实例ID形如：vpc-f49l6u0z。
cidr-block - String - （过滤条件）vpc的cidr。
state - String - （过滤条件）VPC状态。(pending | available).
zone -  String - （过滤条件）VPC的可用区。
        :type Filters: list of Filter
        :param _Offset: 初始行的偏移量，默认为0。
        :type Offset: int
        :param _Limit: 每页行数，默认为20。
        :type Limit: int
        """
        self._VpcIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def VpcIds(self):
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

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
        self._VpcIds = params.get("VpcIds")
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
        


class DescribeVpcsResponse(AbstractModel):
    """DescribeVpcs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcSet: VPC列表
        :type VpcSet: list of VpcInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VpcSet = None
        self._RequestId = None

    @property
    def VpcSet(self):
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVpnConnectionsRequest(AbstractModel):
    """DescribeVpnConnections请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpnConnectionIds: VPN通道实例ID。形如：bmvpnx-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpnConnectionIds和Filters。
        :type VpnConnectionIds: list of str
        :param _Filters: 过滤条件，详见下表：实例过滤条件表。每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定VpnConnectionIds和Filters。
<li>vpc-id - String - （过滤条件）VPC实例ID形如：vpc-f49l6u0z。</li>
<li>state - String - （过滤条件 VPN状态：creating，available，createfailed，changing，changefailed，deleting，deletefailed。</li>
<li>zone - String - （过滤条件）VPN所在可用区，形如：ap-guangzhou-2。</li>
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _VpnGatewayId: VPN网关实例ID
        :type VpnGatewayId: str
        :param _VpnConnectionName: VPN通道名称
        :type VpnConnectionName: str
        :param _OrderField: 排序字段, 支持"CreateTime"排序
        :type OrderField: str
        :param _OrderDirection: 排序方向, “asc”、“desc”
        :type OrderDirection: str
        """
        self._VpnConnectionIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._VpnGatewayId = None
        self._VpnConnectionName = None
        self._OrderField = None
        self._OrderDirection = None

    @property
    def VpnConnectionIds(self):
        return self._VpnConnectionIds

    @VpnConnectionIds.setter
    def VpnConnectionIds(self, VpnConnectionIds):
        self._VpnConnectionIds = VpnConnectionIds

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

    @property
    def VpnGatewayId(self):
        return self._VpnGatewayId

    @VpnGatewayId.setter
    def VpnGatewayId(self, VpnGatewayId):
        self._VpnGatewayId = VpnGatewayId

    @property
    def VpnConnectionName(self):
        return self._VpnConnectionName

    @VpnConnectionName.setter
    def VpnConnectionName(self, VpnConnectionName):
        self._VpnConnectionName = VpnConnectionName

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._VpnConnectionIds = params.get("VpnConnectionIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._VpnGatewayId = params.get("VpnGatewayId")
        self._VpnConnectionName = params.get("VpnConnectionName")
        self._OrderField = params.get("OrderField")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpnConnectionsResponse(AbstractModel):
    """DescribeVpnConnections返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param _VpnConnectionSet: VPN通道实例。
        :type VpnConnectionSet: list of VpnConnection
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VpnConnectionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VpnConnectionSet(self):
        return self._VpnConnectionSet

    @VpnConnectionSet.setter
    def VpnConnectionSet(self, VpnConnectionSet):
        self._VpnConnectionSet = VpnConnectionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("VpnConnectionSet") is not None:
            self._VpnConnectionSet = []
            for item in params.get("VpnConnectionSet"):
                obj = VpnConnection()
                obj._deserialize(item)
                self._VpnConnectionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVpnGatewaysRequest(AbstractModel):
    """DescribeVpnGateways请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpnGatewayIds: VPN网关实例ID。形如：bmvpngw-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpnGatewayIds和Filters。
        :type VpnGatewayIds: list of str
        :param _Filters: 过滤条件，参数不支持同时指定VpnGatewayIds和Filters。
<li>vpc-id - String - （过滤条件）VPC实例ID形如：vpc-f49l6u0z。</li>
<li>state - String - （过滤条件 VPN状态：creating，available，createfailed，changing，changefailed，deleting，deletefailed。</li>
<li>zone - String - （过滤条件）VPN所在可用区，形如：ap-guangzhou-2。</li>
<li>vpngw-name - String - （过滤条件）vpn网关名称。</li>
        :type Filters: list of Filter
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 请求对象个数
        :type Limit: int
        :param _OrderField: 排序字段, 支持"CreateTime"排序
        :type OrderField: str
        :param _OrderDirection: 排序方向, “asc”、“desc”
        :type OrderDirection: str
        """
        self._VpnGatewayIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._OrderDirection = None

    @property
    def VpnGatewayIds(self):
        return self._VpnGatewayIds

    @VpnGatewayIds.setter
    def VpnGatewayIds(self, VpnGatewayIds):
        self._VpnGatewayIds = VpnGatewayIds

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

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        self._VpnGatewayIds = params.get("VpnGatewayIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpnGatewaysResponse(AbstractModel):
    """DescribeVpnGateways返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param _VpnGatewaySet: VPN网关实例详细信息列表。
        :type VpnGatewaySet: list of VpnGateway
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VpnGatewaySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VpnGatewaySet(self):
        return self._VpnGatewaySet

    @VpnGatewaySet.setter
    def VpnGatewaySet(self, VpnGatewaySet):
        self._VpnGatewaySet = VpnGatewaySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("VpnGatewaySet") is not None:
            self._VpnGatewaySet = []
            for item in params.get("VpnGatewaySet"):
                obj = VpnGateway()
                obj._deserialize(item)
                self._VpnGatewaySet.append(obj)
        self._RequestId = params.get("RequestId")


class DownloadCustomerGatewayConfigurationRequest(AbstractModel):
    """DownloadCustomerGatewayConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpnConnectionId: VPN通道实例ID。形如：bmvpnx-f49l6u0z。
        :type VpnConnectionId: str
        :param _VendorName: 厂商,取值 h3c，cisco
        :type VendorName: str
        """
        self._VpnConnectionId = None
        self._VendorName = None

    @property
    def VpnConnectionId(self):
        return self._VpnConnectionId

    @VpnConnectionId.setter
    def VpnConnectionId(self, VpnConnectionId):
        self._VpnConnectionId = VpnConnectionId

    @property
    def VendorName(self):
        return self._VendorName

    @VendorName.setter
    def VendorName(self, VendorName):
        self._VendorName = VendorName


    def _deserialize(self, params):
        self._VpnConnectionId = params.get("VpnConnectionId")
        self._VendorName = params.get("VendorName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadCustomerGatewayConfigurationResponse(AbstractModel):
    """DownloadCustomerGatewayConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomerGatewayConfiguration: 配置信息。
        :type CustomerGatewayConfiguration: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CustomerGatewayConfiguration = None
        self._RequestId = None

    @property
    def CustomerGatewayConfiguration(self):
        return self._CustomerGatewayConfiguration

    @CustomerGatewayConfiguration.setter
    def CustomerGatewayConfiguration(self, CustomerGatewayConfiguration):
        self._CustomerGatewayConfiguration = CustomerGatewayConfiguration

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CustomerGatewayConfiguration = params.get("CustomerGatewayConfiguration")
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """过滤器

    """

    def __init__(self):
        r"""
        :param _Name: 属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Name: str
        :param _Values: 属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。
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
        


class IKEOptionsSpecification(AbstractModel):
    """IKE配置（Internet Key Exchange，因特网密钥交换），IKE具有一套自我保护机制，用户配置网络安全协议

    """

    def __init__(self):
        r"""
        :param _PropoEncryAlgorithm: 加密算法，可选值：'3DES-CBC', 'AES-CBC-128', 'AES-CBC-192', 'AES-CBC-256', 'DES-CBC'，默认为3DES-CBC
        :type PropoEncryAlgorithm: str
        :param _PropoAuthenAlgorithm: 认证算法：可选值：'MD5', 'SHA1'，默认为MD5
        :type PropoAuthenAlgorithm: str
        :param _ExchangeMode: 协商模式：可选值：'AGGRESSIVE', 'MAIN'，默认为MAIN
        :type ExchangeMode: str
        :param _LocalIdentity: 本端标识类型：可选值：'ADDRESS', 'FQDN'，默认为ADDRESS
        :type LocalIdentity: str
        :param _RemoteIdentity: 对端标识类型：可选值：'ADDRESS', 'FQDN'，默认为ADDRESS
        :type RemoteIdentity: str
        :param _LocalAddress: 本端标识，当LocalIdentity选为ADDRESS时，LocalAddress必填。localAddress默认为vpn网关公网IP
        :type LocalAddress: str
        :param _RemoteAddress: 对端标识，当RemoteIdentity选为ADDRESS时，RemoteAddress必填
        :type RemoteAddress: str
        :param _LocalFqdnName: 本端标识，当LocalIdentity选为FQDN时，LocalFqdnName必填
        :type LocalFqdnName: str
        :param _RemoteFqdnName: 对端标识，当remoteIdentity选为FQDN时，RemoteFqdnName必填
        :type RemoteFqdnName: str
        :param _DhGroupName: DH group，指定IKE交换密钥时使用的DH组，可选值：'GROUP1', 'GROUP2', 'GROUP5', 'GROUP14', 'GROUP24'，
        :type DhGroupName: str
        :param _IKESaLifetimeSeconds: IKE SA Lifetime，单位：秒，设置IKE SA的生存周期，取值范围：60-604800
        :type IKESaLifetimeSeconds: int
        :param _IKEVersion: IKE版本
        :type IKEVersion: str
        """
        self._PropoEncryAlgorithm = None
        self._PropoAuthenAlgorithm = None
        self._ExchangeMode = None
        self._LocalIdentity = None
        self._RemoteIdentity = None
        self._LocalAddress = None
        self._RemoteAddress = None
        self._LocalFqdnName = None
        self._RemoteFqdnName = None
        self._DhGroupName = None
        self._IKESaLifetimeSeconds = None
        self._IKEVersion = None

    @property
    def PropoEncryAlgorithm(self):
        return self._PropoEncryAlgorithm

    @PropoEncryAlgorithm.setter
    def PropoEncryAlgorithm(self, PropoEncryAlgorithm):
        self._PropoEncryAlgorithm = PropoEncryAlgorithm

    @property
    def PropoAuthenAlgorithm(self):
        return self._PropoAuthenAlgorithm

    @PropoAuthenAlgorithm.setter
    def PropoAuthenAlgorithm(self, PropoAuthenAlgorithm):
        self._PropoAuthenAlgorithm = PropoAuthenAlgorithm

    @property
    def ExchangeMode(self):
        return self._ExchangeMode

    @ExchangeMode.setter
    def ExchangeMode(self, ExchangeMode):
        self._ExchangeMode = ExchangeMode

    @property
    def LocalIdentity(self):
        return self._LocalIdentity

    @LocalIdentity.setter
    def LocalIdentity(self, LocalIdentity):
        self._LocalIdentity = LocalIdentity

    @property
    def RemoteIdentity(self):
        return self._RemoteIdentity

    @RemoteIdentity.setter
    def RemoteIdentity(self, RemoteIdentity):
        self._RemoteIdentity = RemoteIdentity

    @property
    def LocalAddress(self):
        return self._LocalAddress

    @LocalAddress.setter
    def LocalAddress(self, LocalAddress):
        self._LocalAddress = LocalAddress

    @property
    def RemoteAddress(self):
        return self._RemoteAddress

    @RemoteAddress.setter
    def RemoteAddress(self, RemoteAddress):
        self._RemoteAddress = RemoteAddress

    @property
    def LocalFqdnName(self):
        return self._LocalFqdnName

    @LocalFqdnName.setter
    def LocalFqdnName(self, LocalFqdnName):
        self._LocalFqdnName = LocalFqdnName

    @property
    def RemoteFqdnName(self):
        return self._RemoteFqdnName

    @RemoteFqdnName.setter
    def RemoteFqdnName(self, RemoteFqdnName):
        self._RemoteFqdnName = RemoteFqdnName

    @property
    def DhGroupName(self):
        return self._DhGroupName

    @DhGroupName.setter
    def DhGroupName(self, DhGroupName):
        self._DhGroupName = DhGroupName

    @property
    def IKESaLifetimeSeconds(self):
        return self._IKESaLifetimeSeconds

    @IKESaLifetimeSeconds.setter
    def IKESaLifetimeSeconds(self, IKESaLifetimeSeconds):
        self._IKESaLifetimeSeconds = IKESaLifetimeSeconds

    @property
    def IKEVersion(self):
        return self._IKEVersion

    @IKEVersion.setter
    def IKEVersion(self, IKEVersion):
        self._IKEVersion = IKEVersion


    def _deserialize(self, params):
        self._PropoEncryAlgorithm = params.get("PropoEncryAlgorithm")
        self._PropoAuthenAlgorithm = params.get("PropoAuthenAlgorithm")
        self._ExchangeMode = params.get("ExchangeMode")
        self._LocalIdentity = params.get("LocalIdentity")
        self._RemoteIdentity = params.get("RemoteIdentity")
        self._LocalAddress = params.get("LocalAddress")
        self._RemoteAddress = params.get("RemoteAddress")
        self._LocalFqdnName = params.get("LocalFqdnName")
        self._RemoteFqdnName = params.get("RemoteFqdnName")
        self._DhGroupName = params.get("DhGroupName")
        self._IKESaLifetimeSeconds = params.get("IKESaLifetimeSeconds")
        self._IKEVersion = params.get("IKEVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPSECOptionsSpecification(AbstractModel):
    """IPSec配置，腾讯云提供IPSec安全会话设置

    """

    def __init__(self):
        r"""
        :param _PfsDhGroup: PFS：可选值：'NULL', 'DH-GROUP1', 'DH-GROUP2', 'DH-GROUP5', 'DH-GROUP14', 'DH-GROUP24'，默认为NULL
        :type PfsDhGroup: str
        :param _IPSECSaLifetimeTraffic: IPsec SA lifetime(KB)：单位KB，取值范围：2560-604800
        :type IPSECSaLifetimeTraffic: int
        :param _EncryptAlgorithm: 加密算法，可选值：'3DES-CBC', 'AES-CBC-128', 'AES-CBC-192', 'AES-CBC-256', 'DES-CBC', 'NULL'， 默认为AES-CBC-128
        :type EncryptAlgorithm: str
        :param _IntegrityAlgorith: 认证算法：可选值：'MD5', 'SHA1'，默认为
        :type IntegrityAlgorith: str
        :param _IPSECSaLifetimeSeconds: IPsec SA lifetime(s)：单位秒，取值范围：180-604800
        :type IPSECSaLifetimeSeconds: int
        :param _SecurityProto: 安全协议，默认为ESP
        :type SecurityProto: str
        :param _EncapMode: 报文封装模式:默认为Tunnel
        :type EncapMode: str
        """
        self._PfsDhGroup = None
        self._IPSECSaLifetimeTraffic = None
        self._EncryptAlgorithm = None
        self._IntegrityAlgorith = None
        self._IPSECSaLifetimeSeconds = None
        self._SecurityProto = None
        self._EncapMode = None

    @property
    def PfsDhGroup(self):
        return self._PfsDhGroup

    @PfsDhGroup.setter
    def PfsDhGroup(self, PfsDhGroup):
        self._PfsDhGroup = PfsDhGroup

    @property
    def IPSECSaLifetimeTraffic(self):
        return self._IPSECSaLifetimeTraffic

    @IPSECSaLifetimeTraffic.setter
    def IPSECSaLifetimeTraffic(self, IPSECSaLifetimeTraffic):
        self._IPSECSaLifetimeTraffic = IPSECSaLifetimeTraffic

    @property
    def EncryptAlgorithm(self):
        return self._EncryptAlgorithm

    @EncryptAlgorithm.setter
    def EncryptAlgorithm(self, EncryptAlgorithm):
        self._EncryptAlgorithm = EncryptAlgorithm

    @property
    def IntegrityAlgorith(self):
        return self._IntegrityAlgorith

    @IntegrityAlgorith.setter
    def IntegrityAlgorith(self, IntegrityAlgorith):
        self._IntegrityAlgorith = IntegrityAlgorith

    @property
    def IPSECSaLifetimeSeconds(self):
        return self._IPSECSaLifetimeSeconds

    @IPSECSaLifetimeSeconds.setter
    def IPSECSaLifetimeSeconds(self, IPSECSaLifetimeSeconds):
        self._IPSECSaLifetimeSeconds = IPSECSaLifetimeSeconds

    @property
    def SecurityProto(self):
        return self._SecurityProto

    @SecurityProto.setter
    def SecurityProto(self, SecurityProto):
        self._SecurityProto = SecurityProto

    @property
    def EncapMode(self):
        return self._EncapMode

    @EncapMode.setter
    def EncapMode(self, EncapMode):
        self._EncapMode = EncapMode


    def _deserialize(self, params):
        self._PfsDhGroup = params.get("PfsDhGroup")
        self._IPSECSaLifetimeTraffic = params.get("IPSECSaLifetimeTraffic")
        self._EncryptAlgorithm = params.get("EncryptAlgorithm")
        self._IntegrityAlgorith = params.get("IntegrityAlgorith")
        self._IPSECSaLifetimeSeconds = params.get("IPSECSaLifetimeSeconds")
        self._SecurityProto = params.get("SecurityProto")
        self._EncapMode = params.get("EncapMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpInfo(AbstractModel):
    """NAT IP信息

    """

    def __init__(self):
        r"""
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _Ips: IP列表
        :type Ips: list of str
        """
        self._SubnetId = None
        self._Ips = None

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Ips(self):
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._Ips = params.get("Ips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomerGatewayAttributeRequest(AbstractModel):
    """ModifyCustomerGatewayAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomerGatewayId: 对端网关ID，例如：bmcgw-2wqq41m9，可通过DescribeCustomerGateways接口查询对端网关。
        :type CustomerGatewayId: str
        :param _CustomerGatewayName: 对端网关名称，可任意命名，但不得超过60个字符。
        :type CustomerGatewayName: str
        """
        self._CustomerGatewayId = None
        self._CustomerGatewayName = None

    @property
    def CustomerGatewayId(self):
        return self._CustomerGatewayId

    @CustomerGatewayId.setter
    def CustomerGatewayId(self, CustomerGatewayId):
        self._CustomerGatewayId = CustomerGatewayId

    @property
    def CustomerGatewayName(self):
        return self._CustomerGatewayName

    @CustomerGatewayName.setter
    def CustomerGatewayName(self, CustomerGatewayName):
        self._CustomerGatewayName = CustomerGatewayName


    def _deserialize(self, params):
        self._CustomerGatewayId = params.get("CustomerGatewayId")
        self._CustomerGatewayName = params.get("CustomerGatewayName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomerGatewayAttributeResponse(AbstractModel):
    """ModifyCustomerGatewayAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyRoutePolicyRequest(AbstractModel):
    """ModifyRoutePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteTableId: 路由表ID
        :type RouteTableId: str
        :param _RoutePolicy: 修改的路由
        :type RoutePolicy: :class:`tencentcloud.bmvpc.v20180625.models.RoutePolicy`
        """
        self._RouteTableId = None
        self._RoutePolicy = None

    @property
    def RouteTableId(self):
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def RoutePolicy(self):
        return self._RoutePolicy

    @RoutePolicy.setter
    def RoutePolicy(self, RoutePolicy):
        self._RoutePolicy = RoutePolicy


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        if params.get("RoutePolicy") is not None:
            self._RoutePolicy = RoutePolicy()
            self._RoutePolicy._deserialize(params.get("RoutePolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoutePolicyResponse(AbstractModel):
    """ModifyRoutePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyRouteTableRequest(AbstractModel):
    """ModifyRouteTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteTableId: 路由表ID
        :type RouteTableId: str
        :param _RouteTableName: 路由表名称
        :type RouteTableName: str
        """
        self._RouteTableId = None
        self._RouteTableName = None

    @property
    def RouteTableId(self):
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def RouteTableName(self):
        return self._RouteTableName

    @RouteTableName.setter
    def RouteTableName(self, RouteTableName):
        self._RouteTableName = RouteTableName


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        self._RouteTableName = params.get("RouteTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRouteTableResponse(AbstractModel):
    """ModifyRouteTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifySubnetAttributeRequest(AbstractModel):
    """ModifySubnetAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _SubnetName: 子网名称
        :type SubnetName: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._SubnetName = None

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
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubnetAttributeResponse(AbstractModel):
    """ModifySubnetAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifySubnetDHCPRelayRequest(AbstractModel):
    """ModifySubnetDHCPRelay请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _EnableDHCP: 是否开启DHCP Relay
        :type EnableDHCP: bool
        :param _ServerIps: DHCP服务器IP
        :type ServerIps: list of str
        :param _ReservedIpCount: 预留IP个数
        :type ReservedIpCount: int
        """
        self._VpcId = None
        self._SubnetId = None
        self._EnableDHCP = None
        self._ServerIps = None
        self._ReservedIpCount = None

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
    def EnableDHCP(self):
        return self._EnableDHCP

    @EnableDHCP.setter
    def EnableDHCP(self, EnableDHCP):
        self._EnableDHCP = EnableDHCP

    @property
    def ServerIps(self):
        return self._ServerIps

    @ServerIps.setter
    def ServerIps(self, ServerIps):
        self._ServerIps = ServerIps

    @property
    def ReservedIpCount(self):
        return self._ReservedIpCount

    @ReservedIpCount.setter
    def ReservedIpCount(self, ReservedIpCount):
        self._ReservedIpCount = ReservedIpCount


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._EnableDHCP = params.get("EnableDHCP")
        self._ServerIps = params.get("ServerIps")
        self._ReservedIpCount = params.get("ReservedIpCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubnetDHCPRelayResponse(AbstractModel):
    """ModifySubnetDHCPRelay返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyVpcAttributeRequest(AbstractModel):
    """ModifyVpcAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _VpcName: 私有网络名称
        :type VpcName: str
        :param _EnableMonitor: 是否开启内网监控，0为关闭，1为开启
        :type EnableMonitor: bool
        """
        self._VpcId = None
        self._VpcName = None
        self._EnableMonitor = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def EnableMonitor(self):
        return self._EnableMonitor

    @EnableMonitor.setter
    def EnableMonitor(self, EnableMonitor):
        self._EnableMonitor = EnableMonitor


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._EnableMonitor = params.get("EnableMonitor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpcAttributeResponse(AbstractModel):
    """ModifyVpcAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyVpcPeerConnectionRequest(AbstractModel):
    """ModifyVpcPeerConnection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcPeerConnectionId: 黑石对等连接唯一ID
        :type VpcPeerConnectionId: str
        :param _Bandwidth: 对等连接带宽
        :type Bandwidth: int
        :param _VpcPeerConnectionName: 对等连接名称
        :type VpcPeerConnectionName: str
        """
        self._VpcPeerConnectionId = None
        self._Bandwidth = None
        self._VpcPeerConnectionName = None

    @property
    def VpcPeerConnectionId(self):
        return self._VpcPeerConnectionId

    @VpcPeerConnectionId.setter
    def VpcPeerConnectionId(self, VpcPeerConnectionId):
        self._VpcPeerConnectionId = VpcPeerConnectionId

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def VpcPeerConnectionName(self):
        return self._VpcPeerConnectionName

    @VpcPeerConnectionName.setter
    def VpcPeerConnectionName(self, VpcPeerConnectionName):
        self._VpcPeerConnectionName = VpcPeerConnectionName


    def _deserialize(self, params):
        self._VpcPeerConnectionId = params.get("VpcPeerConnectionId")
        self._Bandwidth = params.get("Bandwidth")
        self._VpcPeerConnectionName = params.get("VpcPeerConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpcPeerConnectionResponse(AbstractModel):
    """ModifyVpcPeerConnection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyVpnConnectionAttributeRequest(AbstractModel):
    """ModifyVpnConnectionAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpnConnectionId: VPN通道实例ID。形如：bmvpnx-f49l6u0z。
        :type VpnConnectionId: str
        :param _VpcId: VPC实例ID
        :type VpcId: str
        :param _VpnConnectionName: VPN通道名称，可任意命名，但不得超过60个字符。
        :type VpnConnectionName: str
        :param _PreShareKey: 预共享密钥。
        :type PreShareKey: str
        :param _SecurityPolicyDatabases: SPD策略组，例如：{"10.0.0.5/24":["172.123.10.5/16"]}，10.0.0.5/24是vpc内网段172.123.10.5/16是IDC网段。用户指定VPC内哪些网段可以和您IDC中哪些网段通信。
        :type SecurityPolicyDatabases: list of SecurityPolicyDatabase
        :param _IKEOptionsSpecification: IKE配置（Internet Key Exchange，因特网密钥交换），IKE具有一套自我保护机制，用户配置网络安全协议。
        :type IKEOptionsSpecification: :class:`tencentcloud.bmvpc.v20180625.models.IKEOptionsSpecification`
        :param _IPSECOptionsSpecification: IPSec配置，腾讯云提供IPSec安全会话设置。
        :type IPSECOptionsSpecification: :class:`tencentcloud.bmvpc.v20180625.models.IPSECOptionsSpecification`
        """
        self._VpnConnectionId = None
        self._VpcId = None
        self._VpnConnectionName = None
        self._PreShareKey = None
        self._SecurityPolicyDatabases = None
        self._IKEOptionsSpecification = None
        self._IPSECOptionsSpecification = None

    @property
    def VpnConnectionId(self):
        return self._VpnConnectionId

    @VpnConnectionId.setter
    def VpnConnectionId(self, VpnConnectionId):
        self._VpnConnectionId = VpnConnectionId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpnConnectionName(self):
        return self._VpnConnectionName

    @VpnConnectionName.setter
    def VpnConnectionName(self, VpnConnectionName):
        self._VpnConnectionName = VpnConnectionName

    @property
    def PreShareKey(self):
        return self._PreShareKey

    @PreShareKey.setter
    def PreShareKey(self, PreShareKey):
        self._PreShareKey = PreShareKey

    @property
    def SecurityPolicyDatabases(self):
        return self._SecurityPolicyDatabases

    @SecurityPolicyDatabases.setter
    def SecurityPolicyDatabases(self, SecurityPolicyDatabases):
        self._SecurityPolicyDatabases = SecurityPolicyDatabases

    @property
    def IKEOptionsSpecification(self):
        return self._IKEOptionsSpecification

    @IKEOptionsSpecification.setter
    def IKEOptionsSpecification(self, IKEOptionsSpecification):
        self._IKEOptionsSpecification = IKEOptionsSpecification

    @property
    def IPSECOptionsSpecification(self):
        return self._IPSECOptionsSpecification

    @IPSECOptionsSpecification.setter
    def IPSECOptionsSpecification(self, IPSECOptionsSpecification):
        self._IPSECOptionsSpecification = IPSECOptionsSpecification


    def _deserialize(self, params):
        self._VpnConnectionId = params.get("VpnConnectionId")
        self._VpcId = params.get("VpcId")
        self._VpnConnectionName = params.get("VpnConnectionName")
        self._PreShareKey = params.get("PreShareKey")
        if params.get("SecurityPolicyDatabases") is not None:
            self._SecurityPolicyDatabases = []
            for item in params.get("SecurityPolicyDatabases"):
                obj = SecurityPolicyDatabase()
                obj._deserialize(item)
                self._SecurityPolicyDatabases.append(obj)
        if params.get("IKEOptionsSpecification") is not None:
            self._IKEOptionsSpecification = IKEOptionsSpecification()
            self._IKEOptionsSpecification._deserialize(params.get("IKEOptionsSpecification"))
        if params.get("IPSECOptionsSpecification") is not None:
            self._IPSECOptionsSpecification = IPSECOptionsSpecification()
            self._IPSECOptionsSpecification._deserialize(params.get("IPSECOptionsSpecification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpnConnectionAttributeResponse(AbstractModel):
    """ModifyVpnConnectionAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyVpnGatewayAttributeRequest(AbstractModel):
    """ModifyVpnGatewayAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpnGatewayId: VPN网关实例ID。
        :type VpnGatewayId: str
        :param _VpnGatewayName: VPN网关名称，最大长度不能超过60个字节。
        :type VpnGatewayName: str
        """
        self._VpnGatewayId = None
        self._VpnGatewayName = None

    @property
    def VpnGatewayId(self):
        return self._VpnGatewayId

    @VpnGatewayId.setter
    def VpnGatewayId(self, VpnGatewayId):
        self._VpnGatewayId = VpnGatewayId

    @property
    def VpnGatewayName(self):
        return self._VpnGatewayName

    @VpnGatewayName.setter
    def VpnGatewayName(self, VpnGatewayName):
        self._VpnGatewayName = VpnGatewayName


    def _deserialize(self, params):
        self._VpnGatewayId = params.get("VpnGatewayId")
        self._VpnGatewayName = params.get("VpnGatewayName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpnGatewayAttributeResponse(AbstractModel):
    """ModifyVpnGatewayAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class NatGatewayInfo(AbstractModel):
    """NAT详情

    """

    def __init__(self):
        r"""
        :param _NatId: NAT网关ID
        :type NatId: str
        :param _NatName: 网关名称
        :type NatName: str
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _VpcName: 私有网络名称
        :type VpcName: str
        :param _ProductionStatus: 网关创建状态，其中0表示创建中，1表示运行中，2表示创建失败
        :type ProductionStatus: int
        :param _Eips: EIP列表
        :type Eips: list of str
        :param _MaxConcurrent: 并发连接数规格，取值为1000000, 3000000, 10000000
        :type MaxConcurrent: int
        :param _Zone: 可用区
        :type Zone: str
        :param _Exclusive: 独占标识，其中0表示共享，1表示独占，默认值为0
        :type Exclusive: int
        :param _ForwardMode: 转发模式，其中0表示IP方式，1表示网段方式
        :type ForwardMode: int
        :param _VpcCidrBlock: 私有网络网段
        :type VpcCidrBlock: str
        :param _Type: 网关类型，取值为 small，middle，big，分别对应小型、中型、大型
        :type Type: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _State: 网关启用状态，1为禁用，0为启用。
        :type State: int
        :param _IntVpcId: 私有网络整型ID
        :type IntVpcId: int
        :param _NatResourceId: NAT资源ID
        :type NatResourceId: int
        """
        self._NatId = None
        self._NatName = None
        self._VpcId = None
        self._VpcName = None
        self._ProductionStatus = None
        self._Eips = None
        self._MaxConcurrent = None
        self._Zone = None
        self._Exclusive = None
        self._ForwardMode = None
        self._VpcCidrBlock = None
        self._Type = None
        self._CreateTime = None
        self._State = None
        self._IntVpcId = None
        self._NatResourceId = None

    @property
    def NatId(self):
        return self._NatId

    @NatId.setter
    def NatId(self, NatId):
        self._NatId = NatId

    @property
    def NatName(self):
        return self._NatName

    @NatName.setter
    def NatName(self, NatName):
        self._NatName = NatName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def ProductionStatus(self):
        return self._ProductionStatus

    @ProductionStatus.setter
    def ProductionStatus(self, ProductionStatus):
        self._ProductionStatus = ProductionStatus

    @property
    def Eips(self):
        return self._Eips

    @Eips.setter
    def Eips(self, Eips):
        self._Eips = Eips

    @property
    def MaxConcurrent(self):
        return self._MaxConcurrent

    @MaxConcurrent.setter
    def MaxConcurrent(self, MaxConcurrent):
        self._MaxConcurrent = MaxConcurrent

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Exclusive(self):
        return self._Exclusive

    @Exclusive.setter
    def Exclusive(self, Exclusive):
        self._Exclusive = Exclusive

    @property
    def ForwardMode(self):
        return self._ForwardMode

    @ForwardMode.setter
    def ForwardMode(self, ForwardMode):
        self._ForwardMode = ForwardMode

    @property
    def VpcCidrBlock(self):
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def IntVpcId(self):
        return self._IntVpcId

    @IntVpcId.setter
    def IntVpcId(self, IntVpcId):
        self._IntVpcId = IntVpcId

    @property
    def NatResourceId(self):
        return self._NatResourceId

    @NatResourceId.setter
    def NatResourceId(self, NatResourceId):
        self._NatResourceId = NatResourceId


    def _deserialize(self, params):
        self._NatId = params.get("NatId")
        self._NatName = params.get("NatName")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._ProductionStatus = params.get("ProductionStatus")
        self._Eips = params.get("Eips")
        self._MaxConcurrent = params.get("MaxConcurrent")
        self._Zone = params.get("Zone")
        self._Exclusive = params.get("Exclusive")
        self._ForwardMode = params.get("ForwardMode")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._Type = params.get("Type")
        self._CreateTime = params.get("CreateTime")
        self._State = params.get("State")
        self._IntVpcId = params.get("IntVpcId")
        self._NatResourceId = params.get("NatResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NatSubnetInfo(AbstractModel):
    """NAT子网信息

    """

    def __init__(self):
        r"""
        :param _Name: 子网名称
        :type Name: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _SubnetNatType: NAT子网类型，其中0表示绑定部分IP的NAT子网，1表示绑定全部IP的NAT子网，2表示绑定网关方式的NAT子网
        :type SubnetNatType: int
        :param _CidrBlock: 子网网段
        :type CidrBlock: str
        """
        self._Name = None
        self._SubnetId = None
        self._SubnetNatType = None
        self._CidrBlock = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetNatType(self):
        return self._SubnetNatType

    @SubnetNatType.setter
    def SubnetNatType(self, SubnetNatType):
        self._SubnetNatType = SubnetNatType

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._SubnetId = params.get("SubnetId")
        self._SubnetNatType = params.get("SubnetNatType")
        self._CidrBlock = params.get("CidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectVpcPeerConnectionRequest(AbstractModel):
    """RejectVpcPeerConnection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcPeerConnectionId: 黑石对等连接实例ID
        :type VpcPeerConnectionId: str
        """
        self._VpcPeerConnectionId = None

    @property
    def VpcPeerConnectionId(self):
        return self._VpcPeerConnectionId

    @VpcPeerConnectionId.setter
    def VpcPeerConnectionId(self, VpcPeerConnectionId):
        self._VpcPeerConnectionId = VpcPeerConnectionId


    def _deserialize(self, params):
        self._VpcPeerConnectionId = params.get("VpcPeerConnectionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectVpcPeerConnectionResponse(AbstractModel):
    """RejectVpcPeerConnection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ResetVpnConnectionRequest(AbstractModel):
    """ResetVpnConnection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC唯一ID
        :type VpcId: str
        :param _VpnConnectionId: VPN通道实例ID。形如：bmvpnx-f49l6u0z。
        :type VpnConnectionId: str
        """
        self._VpcId = None
        self._VpnConnectionId = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpnConnectionId(self):
        return self._VpnConnectionId

    @VpnConnectionId.setter
    def VpnConnectionId(self, VpnConnectionId):
        self._VpnConnectionId = VpnConnectionId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpnConnectionId = params.get("VpnConnectionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetVpnConnectionResponse(AbstractModel):
    """ResetVpnConnection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class RoutePolicy(AbstractModel):
    """路由条目

    """

    def __init__(self):
        r"""
        :param _DestinationCidrBlock: 目的网段
        :type DestinationCidrBlock: str
        :param _GatewayType: 下一跳类型，目前我们支持的类型有：
LOCAL：物理机默认路由；
VPN：VPN网关；
PEERCONNECTION：对等连接；
CPM：物理机自定义路由；
CCN：云联网；
TGW：公网默认路由；
SSLVPN : SSH SSL VPN网关。
        :type GatewayType: str
        :param _GatewayId: 下一跳地址，这里只需要指定不同下一跳类型的网关ID，系统会自动匹配到下一跳地址。
        :type GatewayId: str
        :param _RouteDescription: 路由策略描述。
        :type RouteDescription: str
        :param _RoutePolicyId: 路由策略ID
        :type RoutePolicyId: str
        :param _RoutePolicyType: 路由类型，目前我们支持的类型有：
USER：用户自定义路由；
NETD：网络探测路由，创建网络探测实例时，系统默认下发，不可编辑与删除；
CCN：云联网路由，系统默认下发，不可编辑与删除。
用户只能添加和编辑USER 类型的路由。
        :type RoutePolicyType: str
        :param _Enabled: 是否启用
        :type Enabled: bool
        """
        self._DestinationCidrBlock = None
        self._GatewayType = None
        self._GatewayId = None
        self._RouteDescription = None
        self._RoutePolicyId = None
        self._RoutePolicyType = None
        self._Enabled = None

    @property
    def DestinationCidrBlock(self):
        return self._DestinationCidrBlock

    @DestinationCidrBlock.setter
    def DestinationCidrBlock(self, DestinationCidrBlock):
        self._DestinationCidrBlock = DestinationCidrBlock

    @property
    def GatewayType(self):
        return self._GatewayType

    @GatewayType.setter
    def GatewayType(self, GatewayType):
        self._GatewayType = GatewayType

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def RouteDescription(self):
        return self._RouteDescription

    @RouteDescription.setter
    def RouteDescription(self, RouteDescription):
        self._RouteDescription = RouteDescription

    @property
    def RoutePolicyId(self):
        return self._RoutePolicyId

    @RoutePolicyId.setter
    def RoutePolicyId(self, RoutePolicyId):
        self._RoutePolicyId = RoutePolicyId

    @property
    def RoutePolicyType(self):
        return self._RoutePolicyType

    @RoutePolicyType.setter
    def RoutePolicyType(self, RoutePolicyType):
        self._RoutePolicyType = RoutePolicyType

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._DestinationCidrBlock = params.get("DestinationCidrBlock")
        self._GatewayType = params.get("GatewayType")
        self._GatewayId = params.get("GatewayId")
        self._RouteDescription = params.get("RouteDescription")
        self._RoutePolicyId = params.get("RoutePolicyId")
        self._RoutePolicyType = params.get("RoutePolicyType")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTable(AbstractModel):
    """路由表对象

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC实例ID。
        :type VpcId: str
        :param _VpcName: VPC的名称
        :type VpcName: str
        :param _VpcCidrBlock: VPC的CIDR
        :type VpcCidrBlock: str
        :param _Zone: 可用区
        :type Zone: str
        :param _RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param _RouteTableName: 路由表名称。
        :type RouteTableName: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        """
        self._VpcId = None
        self._VpcName = None
        self._VpcCidrBlock = None
        self._Zone = None
        self._RouteTableId = None
        self._RouteTableName = None
        self._CreateTime = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcCidrBlock(self):
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def RouteTableId(self):
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def RouteTableName(self):
        return self._RouteTableName

    @RouteTableName.setter
    def RouteTableName(self, RouteTableName):
        self._RouteTableName = RouteTableName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._Zone = params.get("Zone")
        self._RouteTableId = params.get("RouteTableId")
        self._RouteTableName = params.get("RouteTableName")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicyDatabase(AbstractModel):
    """SecurityPolicyDatabase策略

    """

    def __init__(self):
        r"""
        :param _LocalCidrBlock: 本端网段
        :type LocalCidrBlock: str
        :param _RemoteCidrBlock: 对端网段
        :type RemoteCidrBlock: list of str
        """
        self._LocalCidrBlock = None
        self._RemoteCidrBlock = None

    @property
    def LocalCidrBlock(self):
        return self._LocalCidrBlock

    @LocalCidrBlock.setter
    def LocalCidrBlock(self, LocalCidrBlock):
        self._LocalCidrBlock = LocalCidrBlock

    @property
    def RemoteCidrBlock(self):
        return self._RemoteCidrBlock

    @RemoteCidrBlock.setter
    def RemoteCidrBlock(self, RemoteCidrBlock):
        self._RemoteCidrBlock = RemoteCidrBlock


    def _deserialize(self, params):
        self._LocalCidrBlock = params.get("LocalCidrBlock")
        self._RemoteCidrBlock = params.get("RemoteCidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubnetCreateInputInfo(AbstractModel):
    """创建子网时的子网类型

    """

    def __init__(self):
        r"""
        :param _SubnetName: 子网名称，可任意命名，但不得超过60个字符
        :type SubnetName: str
        :param _CidrBlock: 子网网段，子网网段必须在VPC网段内，相同VPC内子网网段不能重叠
        :type CidrBlock: str
        :param _DistributedFlag: 是否开启子网分布式网关，默认传1，传0为关闭子网分布式网关。关闭分布式网关子网用于云服务器化子网，此子网中只能有一台物理机，同时此物理机及其上子机只能在此子网中
        :type DistributedFlag: int
        :param _DhcpEnable: 是否开启dhcp relay ，关闭为0，开启为1。默认为0
        :type DhcpEnable: int
        :param _DhcpServerIp: DHCP SERVER 的IP地址数组。IP地址为相同VPC的子网内分配的IP
        :type DhcpServerIp: list of str
        :param _IpReserve: 预留的IP个数。从该子网的最大可分配IP倒序分配N个IP 用于DHCP 动态分配使用的地址段
        :type IpReserve: int
        :param _VlanId: 子网绑定的vlanId。VlanId取值范围为2000-2999。创建物理机子网，VlanId默认为5; 创建docker子网或者虚拟子网，VlanId默认会分配2000--2999未使用的数值。
        :type VlanId: int
        :param _Zone: 黑石子网的可用区
        :type Zone: str
        :param _IsSmartNic: 是否25G子网，1为是，0为否。
        :type IsSmartNic: int
        """
        self._SubnetName = None
        self._CidrBlock = None
        self._DistributedFlag = None
        self._DhcpEnable = None
        self._DhcpServerIp = None
        self._IpReserve = None
        self._VlanId = None
        self._Zone = None
        self._IsSmartNic = None

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def DistributedFlag(self):
        return self._DistributedFlag

    @DistributedFlag.setter
    def DistributedFlag(self, DistributedFlag):
        self._DistributedFlag = DistributedFlag

    @property
    def DhcpEnable(self):
        return self._DhcpEnable

    @DhcpEnable.setter
    def DhcpEnable(self, DhcpEnable):
        self._DhcpEnable = DhcpEnable

    @property
    def DhcpServerIp(self):
        return self._DhcpServerIp

    @DhcpServerIp.setter
    def DhcpServerIp(self, DhcpServerIp):
        self._DhcpServerIp = DhcpServerIp

    @property
    def IpReserve(self):
        return self._IpReserve

    @IpReserve.setter
    def IpReserve(self, IpReserve):
        self._IpReserve = IpReserve

    @property
    def VlanId(self):
        return self._VlanId

    @VlanId.setter
    def VlanId(self, VlanId):
        self._VlanId = VlanId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def IsSmartNic(self):
        return self._IsSmartNic

    @IsSmartNic.setter
    def IsSmartNic(self, IsSmartNic):
        self._IsSmartNic = IsSmartNic


    def _deserialize(self, params):
        self._SubnetName = params.get("SubnetName")
        self._CidrBlock = params.get("CidrBlock")
        self._DistributedFlag = params.get("DistributedFlag")
        self._DhcpEnable = params.get("DhcpEnable")
        self._DhcpServerIp = params.get("DhcpServerIp")
        self._IpReserve = params.get("IpReserve")
        self._VlanId = params.get("VlanId")
        self._Zone = params.get("Zone")
        self._IsSmartNic = params.get("IsSmartNic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubnetInfo(AbstractModel):
    """黑石子网的信息

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络的唯一ID。
        :type VpcId: str
        :param _VpcName: VPC的名称。
        :type VpcName: str
        :param _VpcCidrBlock: VPC的CIDR。
        :type VpcCidrBlock: str
        :param _SubnetId: 私有网络的唯一ID
        :type SubnetId: str
        :param _SubnetName: 子网名称。
        :type SubnetName: str
        :param _CidrBlock: 子网CIDR。
        :type CidrBlock: str
        :param _Type: 子网类型。0: 黑石物理机子网; 6: ccs子网; 7 Docker子网; 8: 虚拟机子网
        :type Type: int
        :param _ZoneId: 子网可用区ID。
        :type ZoneId: int
        :param _CpmNum: 子网物理机的个数
        :type CpmNum: int
        :param _VlanId: 子网的VlanId。
        :type VlanId: int
        :param _DistributedFlag: 是否开启分布式网关 ，关闭为0，开启为1。
        :type DistributedFlag: int
        :param _DhcpEnable: 是否开启dhcp relay ，关闭为0，开启为1。默认为0。
        :type DhcpEnable: int
        :param _DhcpServerIp: DHCP SERVER 的IP地址数组。IP地址为相同VPC的子网内分配的IP。
        :type DhcpServerIp: list of str
        :param _IpReserve: 预留的IP个数。从该子网的最大可分配IP倒序分配N个IP 用于DHCP 动态分配使用的地址段。
        :type IpReserve: int
        :param _AvailableIpNum: 子网中可用的IP个数
        :type AvailableIpNum: int
        :param _TotalIpNum: 子网中总共的IP个数
        :type TotalIpNum: int
        :param _SubnetCreateTime: 子网创建时间
        :type SubnetCreateTime: str
        :param _IsSmartNic: 25G子网标识
        :type IsSmartNic: int
        :param _Zone: 子网可用区。
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _VpcZoneId: VPC所在可用区ID
        :type VpcZoneId: int
        :param _VpcZone: VPC所在可用区
        :type VpcZone: str
        :param _BroadcastFlag: 是否开启广播，关闭为0，开启为1。
        :type BroadcastFlag: int
        """
        self._VpcId = None
        self._VpcName = None
        self._VpcCidrBlock = None
        self._SubnetId = None
        self._SubnetName = None
        self._CidrBlock = None
        self._Type = None
        self._ZoneId = None
        self._CpmNum = None
        self._VlanId = None
        self._DistributedFlag = None
        self._DhcpEnable = None
        self._DhcpServerIp = None
        self._IpReserve = None
        self._AvailableIpNum = None
        self._TotalIpNum = None
        self._SubnetCreateTime = None
        self._IsSmartNic = None
        self._Zone = None
        self._VpcZoneId = None
        self._VpcZone = None
        self._BroadcastFlag = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcCidrBlock(self):
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def CpmNum(self):
        return self._CpmNum

    @CpmNum.setter
    def CpmNum(self, CpmNum):
        self._CpmNum = CpmNum

    @property
    def VlanId(self):
        return self._VlanId

    @VlanId.setter
    def VlanId(self, VlanId):
        self._VlanId = VlanId

    @property
    def DistributedFlag(self):
        return self._DistributedFlag

    @DistributedFlag.setter
    def DistributedFlag(self, DistributedFlag):
        self._DistributedFlag = DistributedFlag

    @property
    def DhcpEnable(self):
        return self._DhcpEnable

    @DhcpEnable.setter
    def DhcpEnable(self, DhcpEnable):
        self._DhcpEnable = DhcpEnable

    @property
    def DhcpServerIp(self):
        return self._DhcpServerIp

    @DhcpServerIp.setter
    def DhcpServerIp(self, DhcpServerIp):
        self._DhcpServerIp = DhcpServerIp

    @property
    def IpReserve(self):
        return self._IpReserve

    @IpReserve.setter
    def IpReserve(self, IpReserve):
        self._IpReserve = IpReserve

    @property
    def AvailableIpNum(self):
        return self._AvailableIpNum

    @AvailableIpNum.setter
    def AvailableIpNum(self, AvailableIpNum):
        self._AvailableIpNum = AvailableIpNum

    @property
    def TotalIpNum(self):
        return self._TotalIpNum

    @TotalIpNum.setter
    def TotalIpNum(self, TotalIpNum):
        self._TotalIpNum = TotalIpNum

    @property
    def SubnetCreateTime(self):
        return self._SubnetCreateTime

    @SubnetCreateTime.setter
    def SubnetCreateTime(self, SubnetCreateTime):
        self._SubnetCreateTime = SubnetCreateTime

    @property
    def IsSmartNic(self):
        return self._IsSmartNic

    @IsSmartNic.setter
    def IsSmartNic(self, IsSmartNic):
        self._IsSmartNic = IsSmartNic

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcZoneId(self):
        return self._VpcZoneId

    @VpcZoneId.setter
    def VpcZoneId(self, VpcZoneId):
        self._VpcZoneId = VpcZoneId

    @property
    def VpcZone(self):
        return self._VpcZone

    @VpcZone.setter
    def VpcZone(self, VpcZone):
        self._VpcZone = VpcZone

    @property
    def BroadcastFlag(self):
        return self._BroadcastFlag

    @BroadcastFlag.setter
    def BroadcastFlag(self, BroadcastFlag):
        self._BroadcastFlag = BroadcastFlag


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        self._CidrBlock = params.get("CidrBlock")
        self._Type = params.get("Type")
        self._ZoneId = params.get("ZoneId")
        self._CpmNum = params.get("CpmNum")
        self._VlanId = params.get("VlanId")
        self._DistributedFlag = params.get("DistributedFlag")
        self._DhcpEnable = params.get("DhcpEnable")
        self._DhcpServerIp = params.get("DhcpServerIp")
        self._IpReserve = params.get("IpReserve")
        self._AvailableIpNum = params.get("AvailableIpNum")
        self._TotalIpNum = params.get("TotalIpNum")
        self._SubnetCreateTime = params.get("SubnetCreateTime")
        self._IsSmartNic = params.get("IsSmartNic")
        self._Zone = params.get("Zone")
        self._VpcZoneId = params.get("VpcZoneId")
        self._VpcZone = params.get("VpcZone")
        self._BroadcastFlag = params.get("BroadcastFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindEipsFromNatGatewayRequest(AbstractModel):
    """UnbindEipsFromNatGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param _VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param _AssignedEips: 已分配的EIP列表
        :type AssignedEips: list of str
        """
        self._NatId = None
        self._VpcId = None
        self._AssignedEips = None

    @property
    def NatId(self):
        return self._NatId

    @NatId.setter
    def NatId(self, NatId):
        self._NatId = NatId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def AssignedEips(self):
        return self._AssignedEips

    @AssignedEips.setter
    def AssignedEips(self, AssignedEips):
        self._AssignedEips = AssignedEips


    def _deserialize(self, params):
        self._NatId = params.get("NatId")
        self._VpcId = params.get("VpcId")
        self._AssignedEips = params.get("AssignedEips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindEipsFromNatGatewayResponse(AbstractModel):
    """UnbindEipsFromNatGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class UnbindIpsFromNatGatewayRequest(AbstractModel):
    """UnbindIpsFromNatGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param _VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param _IpInfoSet: 部分IP信息；子网须以部分IP将加入NAT网关
        :type IpInfoSet: list of IpInfo
        """
        self._NatId = None
        self._VpcId = None
        self._IpInfoSet = None

    @property
    def NatId(self):
        return self._NatId

    @NatId.setter
    def NatId(self, NatId):
        self._NatId = NatId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def IpInfoSet(self):
        return self._IpInfoSet

    @IpInfoSet.setter
    def IpInfoSet(self, IpInfoSet):
        self._IpInfoSet = IpInfoSet


    def _deserialize(self, params):
        self._NatId = params.get("NatId")
        self._VpcId = params.get("VpcId")
        if params.get("IpInfoSet") is not None:
            self._IpInfoSet = []
            for item in params.get("IpInfoSet"):
                obj = IpInfo()
                obj._deserialize(item)
                self._IpInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindIpsFromNatGatewayResponse(AbstractModel):
    """UnbindIpsFromNatGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class UnbindSubnetsFromNatGatewayRequest(AbstractModel):
    """UnbindSubnetsFromNatGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param _VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param _SubnetIds: 子网ID列表，子网不区分加入NAT网关的转发方式
        :type SubnetIds: list of str
        """
        self._NatId = None
        self._VpcId = None
        self._SubnetIds = None

    @property
    def NatId(self):
        return self._NatId

    @NatId.setter
    def NatId(self, NatId):
        self._NatId = NatId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds


    def _deserialize(self, params):
        self._NatId = params.get("NatId")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindSubnetsFromNatGatewayResponse(AbstractModel):
    """UnbindSubnetsFromNatGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class UpgradeNatGatewayRequest(AbstractModel):
    """UpgradeNatGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param _VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param _MaxConcurrent: 并发连接数规格；取值为1000000、3000000、10000000，分别对应小型、中型、大型NAT网关
        :type MaxConcurrent: int
        """
        self._NatId = None
        self._VpcId = None
        self._MaxConcurrent = None

    @property
    def NatId(self):
        return self._NatId

    @NatId.setter
    def NatId(self, NatId):
        self._NatId = NatId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def MaxConcurrent(self):
        return self._MaxConcurrent

    @MaxConcurrent.setter
    def MaxConcurrent(self, MaxConcurrent):
        self._MaxConcurrent = MaxConcurrent


    def _deserialize(self, params):
        self._NatId = params.get("NatId")
        self._VpcId = params.get("VpcId")
        self._MaxConcurrent = params.get("MaxConcurrent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeNatGatewayResponse(AbstractModel):
    """UpgradeNatGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class VpcInfo(AbstractModel):
    """VPC信息

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络的唯一ID。
        :type VpcId: str
        :param _VpcName: VPC的名称。
        :type VpcName: str
        :param _CidrBlock: VPC的CIDR。
        :type CidrBlock: str
        :param _Zone: 可用区
        :type Zone: str
        :param _State: VPC状态
        :type State: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _IntVpcId: 整型私有网络ID。
        :type IntVpcId: int
        """
        self._VpcId = None
        self._VpcName = None
        self._CidrBlock = None
        self._Zone = None
        self._State = None
        self._CreateTime = None
        self._IntVpcId = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IntVpcId(self):
        return self._IntVpcId

    @IntVpcId.setter
    def IntVpcId(self, IntVpcId):
        self._IntVpcId = IntVpcId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._CidrBlock = params.get("CidrBlock")
        self._Zone = params.get("Zone")
        self._State = params.get("State")
        self._CreateTime = params.get("CreateTime")
        self._IntVpcId = params.get("IntVpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcPeerConnection(AbstractModel):
    """对等连接对象

    """

    def __init__(self):
        r"""
        :param _VpcId: 本端VPC唯一ID
        :type VpcId: str
        :param _PeerVpcId: 对端VPC唯一ID
        :type PeerVpcId: str
        :param _AppId: 本端APPID
        :type AppId: str
        :param _PeerAppId: 对端APPID
        :type PeerAppId: str
        :param _VpcPeerConnectionId: 对等连接唯一ID
        :type VpcPeerConnectionId: str
        :param _VpcPeerConnectionName: 对等连接名称
        :type VpcPeerConnectionName: str
        :param _State: 对等连接状态。pending:申请中,available:运行中,expired:已过期,rejected:已拒绝,deleted:已删除
        :type State: str
        :param _VpcZone: 本端VPC所属可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcZone: str
        :param _PeerVpcZone: 对端VPC所属可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type PeerVpcZone: str
        :param _Uin: 本端Uin
        :type Uin: int
        :param _PeerUin: 对端Uin
        :type PeerUin: int
        :param _PeerType: 对等连接类型
        :type PeerType: int
        :param _Bandwidth: 对等连接带宽
        :type Bandwidth: int
        :param _Region: 本端VPC地域
        :type Region: str
        :param _PeerRegion: 对端VPC地域
        :type PeerRegion: str
        :param _DeleteFlag: 是否允许删除
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteFlag: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._VpcId = None
        self._PeerVpcId = None
        self._AppId = None
        self._PeerAppId = None
        self._VpcPeerConnectionId = None
        self._VpcPeerConnectionName = None
        self._State = None
        self._VpcZone = None
        self._PeerVpcZone = None
        self._Uin = None
        self._PeerUin = None
        self._PeerType = None
        self._Bandwidth = None
        self._Region = None
        self._PeerRegion = None
        self._DeleteFlag = None
        self._CreateTime = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def PeerVpcId(self):
        return self._PeerVpcId

    @PeerVpcId.setter
    def PeerVpcId(self, PeerVpcId):
        self._PeerVpcId = PeerVpcId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def PeerAppId(self):
        return self._PeerAppId

    @PeerAppId.setter
    def PeerAppId(self, PeerAppId):
        self._PeerAppId = PeerAppId

    @property
    def VpcPeerConnectionId(self):
        return self._VpcPeerConnectionId

    @VpcPeerConnectionId.setter
    def VpcPeerConnectionId(self, VpcPeerConnectionId):
        self._VpcPeerConnectionId = VpcPeerConnectionId

    @property
    def VpcPeerConnectionName(self):
        return self._VpcPeerConnectionName

    @VpcPeerConnectionName.setter
    def VpcPeerConnectionName(self, VpcPeerConnectionName):
        self._VpcPeerConnectionName = VpcPeerConnectionName

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def VpcZone(self):
        return self._VpcZone

    @VpcZone.setter
    def VpcZone(self, VpcZone):
        self._VpcZone = VpcZone

    @property
    def PeerVpcZone(self):
        return self._PeerVpcZone

    @PeerVpcZone.setter
    def PeerVpcZone(self, PeerVpcZone):
        self._PeerVpcZone = PeerVpcZone

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def PeerUin(self):
        return self._PeerUin

    @PeerUin.setter
    def PeerUin(self, PeerUin):
        self._PeerUin = PeerUin

    @property
    def PeerType(self):
        return self._PeerType

    @PeerType.setter
    def PeerType(self, PeerType):
        self._PeerType = PeerType

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PeerRegion(self):
        return self._PeerRegion

    @PeerRegion.setter
    def PeerRegion(self, PeerRegion):
        self._PeerRegion = PeerRegion

    @property
    def DeleteFlag(self):
        return self._DeleteFlag

    @DeleteFlag.setter
    def DeleteFlag(self, DeleteFlag):
        self._DeleteFlag = DeleteFlag

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._PeerVpcId = params.get("PeerVpcId")
        self._AppId = params.get("AppId")
        self._PeerAppId = params.get("PeerAppId")
        self._VpcPeerConnectionId = params.get("VpcPeerConnectionId")
        self._VpcPeerConnectionName = params.get("VpcPeerConnectionName")
        self._State = params.get("State")
        self._VpcZone = params.get("VpcZone")
        self._PeerVpcZone = params.get("PeerVpcZone")
        self._Uin = params.get("Uin")
        self._PeerUin = params.get("PeerUin")
        self._PeerType = params.get("PeerType")
        self._Bandwidth = params.get("Bandwidth")
        self._Region = params.get("Region")
        self._PeerRegion = params.get("PeerRegion")
        self._DeleteFlag = params.get("DeleteFlag")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcQuota(AbstractModel):
    """VPC限额信息

    """

    def __init__(self):
        r"""
        :param _TypeId: 配额类型ID
        :type TypeId: int
        :param _Quota: 配额
        :type Quota: int
        """
        self._TypeId = None
        self._Quota = None

    @property
    def TypeId(self):
        return self._TypeId

    @TypeId.setter
    def TypeId(self, TypeId):
        self._TypeId = TypeId

    @property
    def Quota(self):
        return self._Quota

    @Quota.setter
    def Quota(self, Quota):
        self._Quota = Quota


    def _deserialize(self, params):
        self._TypeId = params.get("TypeId")
        self._Quota = params.get("Quota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcResource(AbstractModel):
    """VPC占用资源

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _VpcName: 私有网络名称
        :type VpcName: str
        :param _CidrBlock: 私有网络的CIDR
        :type CidrBlock: str
        :param _SubnetNum: 子网个数
        :type SubnetNum: int
        :param _NatNum: NAT个数
        :type NatNum: int
        :param _State: VPC状态
        :type State: str
        :param _MonitorFlag: 是否开启监控
        :type MonitorFlag: bool
        :param _CpmNum: 物理机个数
        :type CpmNum: int
        :param _LeaveIpNum: 可用IP个数
        :type LeaveIpNum: int
        :param _LbNum: 负载均衡个数
        :type LbNum: int
        :param _TrafficMirrorNum: 流量镜像网关个数
        :type TrafficMirrorNum: int
        :param _EipNum: 弹性IP个数
        :type EipNum: int
        :param _PlgwNum: 专线网关个数
        :type PlgwNum: int
        :param _PlvpNum: 专线通道个数
        :type PlvpNum: int
        :param _SslVpnGwNum: ssl vpn网关个数
        :type SslVpnGwNum: int
        :param _VpcPeerNum: 对等链接个数
        :type VpcPeerNum: int
        :param _IpsecVpnGwNum: ipsec vpn网关个数
        :type IpsecVpnGwNum: int
        :param _Zone: 可用区
        :type Zone: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _IsOld: 是否老专区VPC
        :type IsOld: bool
        :param _CcnServiceNum: 云联网服务个数
注意：此字段可能返回 null，表示取不到有效值。
        :type CcnServiceNum: int
        :param _VpcPeerLimitToAllRegion: VPC允许创建的对等连接个数
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcPeerLimitToAllRegion: int
        :param _VpcPeerLimitToSameRegion: VPC允许创建的同地域的对等连接的个数
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcPeerLimitToSameRegion: int
        :param _IntVpcId: 整型私有网络ID
        :type IntVpcId: int
        """
        self._VpcId = None
        self._VpcName = None
        self._CidrBlock = None
        self._SubnetNum = None
        self._NatNum = None
        self._State = None
        self._MonitorFlag = None
        self._CpmNum = None
        self._LeaveIpNum = None
        self._LbNum = None
        self._TrafficMirrorNum = None
        self._EipNum = None
        self._PlgwNum = None
        self._PlvpNum = None
        self._SslVpnGwNum = None
        self._VpcPeerNum = None
        self._IpsecVpnGwNum = None
        self._Zone = None
        self._CreateTime = None
        self._IsOld = None
        self._CcnServiceNum = None
        self._VpcPeerLimitToAllRegion = None
        self._VpcPeerLimitToSameRegion = None
        self._IntVpcId = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def SubnetNum(self):
        return self._SubnetNum

    @SubnetNum.setter
    def SubnetNum(self, SubnetNum):
        self._SubnetNum = SubnetNum

    @property
    def NatNum(self):
        return self._NatNum

    @NatNum.setter
    def NatNum(self, NatNum):
        self._NatNum = NatNum

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def MonitorFlag(self):
        return self._MonitorFlag

    @MonitorFlag.setter
    def MonitorFlag(self, MonitorFlag):
        self._MonitorFlag = MonitorFlag

    @property
    def CpmNum(self):
        return self._CpmNum

    @CpmNum.setter
    def CpmNum(self, CpmNum):
        self._CpmNum = CpmNum

    @property
    def LeaveIpNum(self):
        return self._LeaveIpNum

    @LeaveIpNum.setter
    def LeaveIpNum(self, LeaveIpNum):
        self._LeaveIpNum = LeaveIpNum

    @property
    def LbNum(self):
        return self._LbNum

    @LbNum.setter
    def LbNum(self, LbNum):
        self._LbNum = LbNum

    @property
    def TrafficMirrorNum(self):
        return self._TrafficMirrorNum

    @TrafficMirrorNum.setter
    def TrafficMirrorNum(self, TrafficMirrorNum):
        self._TrafficMirrorNum = TrafficMirrorNum

    @property
    def EipNum(self):
        return self._EipNum

    @EipNum.setter
    def EipNum(self, EipNum):
        self._EipNum = EipNum

    @property
    def PlgwNum(self):
        return self._PlgwNum

    @PlgwNum.setter
    def PlgwNum(self, PlgwNum):
        self._PlgwNum = PlgwNum

    @property
    def PlvpNum(self):
        return self._PlvpNum

    @PlvpNum.setter
    def PlvpNum(self, PlvpNum):
        self._PlvpNum = PlvpNum

    @property
    def SslVpnGwNum(self):
        return self._SslVpnGwNum

    @SslVpnGwNum.setter
    def SslVpnGwNum(self, SslVpnGwNum):
        self._SslVpnGwNum = SslVpnGwNum

    @property
    def VpcPeerNum(self):
        return self._VpcPeerNum

    @VpcPeerNum.setter
    def VpcPeerNum(self, VpcPeerNum):
        self._VpcPeerNum = VpcPeerNum

    @property
    def IpsecVpnGwNum(self):
        return self._IpsecVpnGwNum

    @IpsecVpnGwNum.setter
    def IpsecVpnGwNum(self, IpsecVpnGwNum):
        self._IpsecVpnGwNum = IpsecVpnGwNum

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsOld(self):
        return self._IsOld

    @IsOld.setter
    def IsOld(self, IsOld):
        self._IsOld = IsOld

    @property
    def CcnServiceNum(self):
        return self._CcnServiceNum

    @CcnServiceNum.setter
    def CcnServiceNum(self, CcnServiceNum):
        self._CcnServiceNum = CcnServiceNum

    @property
    def VpcPeerLimitToAllRegion(self):
        return self._VpcPeerLimitToAllRegion

    @VpcPeerLimitToAllRegion.setter
    def VpcPeerLimitToAllRegion(self, VpcPeerLimitToAllRegion):
        self._VpcPeerLimitToAllRegion = VpcPeerLimitToAllRegion

    @property
    def VpcPeerLimitToSameRegion(self):
        return self._VpcPeerLimitToSameRegion

    @VpcPeerLimitToSameRegion.setter
    def VpcPeerLimitToSameRegion(self, VpcPeerLimitToSameRegion):
        self._VpcPeerLimitToSameRegion = VpcPeerLimitToSameRegion

    @property
    def IntVpcId(self):
        return self._IntVpcId

    @IntVpcId.setter
    def IntVpcId(self, IntVpcId):
        self._IntVpcId = IntVpcId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._CidrBlock = params.get("CidrBlock")
        self._SubnetNum = params.get("SubnetNum")
        self._NatNum = params.get("NatNum")
        self._State = params.get("State")
        self._MonitorFlag = params.get("MonitorFlag")
        self._CpmNum = params.get("CpmNum")
        self._LeaveIpNum = params.get("LeaveIpNum")
        self._LbNum = params.get("LbNum")
        self._TrafficMirrorNum = params.get("TrafficMirrorNum")
        self._EipNum = params.get("EipNum")
        self._PlgwNum = params.get("PlgwNum")
        self._PlvpNum = params.get("PlvpNum")
        self._SslVpnGwNum = params.get("SslVpnGwNum")
        self._VpcPeerNum = params.get("VpcPeerNum")
        self._IpsecVpnGwNum = params.get("IpsecVpnGwNum")
        self._Zone = params.get("Zone")
        self._CreateTime = params.get("CreateTime")
        self._IsOld = params.get("IsOld")
        self._CcnServiceNum = params.get("CcnServiceNum")
        self._VpcPeerLimitToAllRegion = params.get("VpcPeerLimitToAllRegion")
        self._VpcPeerLimitToSameRegion = params.get("VpcPeerLimitToSameRegion")
        self._IntVpcId = params.get("IntVpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcSubnetCreateInfo(AbstractModel):
    """创建VPC下默认子网

    """

    def __init__(self):
        r"""
        :param _SubnetName: 子网名称
        :type SubnetName: str
        :param _CidrBlock: 子网的CIDR
        :type CidrBlock: str
        :param _Zone: 子网的可用区
        :type Zone: str
        """
        self._SubnetName = None
        self._CidrBlock = None
        self._Zone = None

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._SubnetName = params.get("SubnetName")
        self._CidrBlock = params.get("CidrBlock")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcSubnetViewInfo(AbstractModel):
    """VPC视图子网信息

    """

    def __init__(self):
        r"""
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _SubnetName: 子网名称
        :type SubnetName: str
        :param _CidrBlock: 子网CIDR
        :type CidrBlock: str
        :param _CpmNum: 子网下设备个数
        :type CpmNum: int
        :param _LbNum: 内网负载均衡个数
        :type LbNum: int
        :param _Zone: 子网所在可用区
        :type Zone: str
        """
        self._SubnetId = None
        self._SubnetName = None
        self._CidrBlock = None
        self._CpmNum = None
        self._LbNum = None
        self._Zone = None

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetName(self):
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def CpmNum(self):
        return self._CpmNum

    @CpmNum.setter
    def CpmNum(self, CpmNum):
        self._CpmNum = CpmNum

    @property
    def LbNum(self):
        return self._LbNum

    @LbNum.setter
    def LbNum(self, LbNum):
        self._LbNum = LbNum

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        self._CidrBlock = params.get("CidrBlock")
        self._CpmNum = params.get("CpmNum")
        self._LbNum = params.get("LbNum")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcViewInfo(AbstractModel):
    """VPC视图信息

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _VpcName: 私有网络名称
        :type VpcName: str
        :param _CidrBlock: 私有网络CIDR
        :type CidrBlock: str
        :param _Zone: 私有网络所在可用区
        :type Zone: str
        :param _LbNum: 外网负载均衡个数
        :type LbNum: int
        :param _EipNum: 弹性公网IP个数
        :type EipNum: int
        :param _NatNum: NAT网关个数
        :type NatNum: int
        :param _SubnetSet: 子网列表
        :type SubnetSet: list of VpcSubnetViewInfo
        """
        self._VpcId = None
        self._VpcName = None
        self._CidrBlock = None
        self._Zone = None
        self._LbNum = None
        self._EipNum = None
        self._NatNum = None
        self._SubnetSet = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def CidrBlock(self):
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def LbNum(self):
        return self._LbNum

    @LbNum.setter
    def LbNum(self, LbNum):
        self._LbNum = LbNum

    @property
    def EipNum(self):
        return self._EipNum

    @EipNum.setter
    def EipNum(self, EipNum):
        self._EipNum = EipNum

    @property
    def NatNum(self):
        return self._NatNum

    @NatNum.setter
    def NatNum(self, NatNum):
        self._NatNum = NatNum

    @property
    def SubnetSet(self):
        return self._SubnetSet

    @SubnetSet.setter
    def SubnetSet(self, SubnetSet):
        self._SubnetSet = SubnetSet


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._CidrBlock = params.get("CidrBlock")
        self._Zone = params.get("Zone")
        self._LbNum = params.get("LbNum")
        self._EipNum = params.get("EipNum")
        self._NatNum = params.get("NatNum")
        if params.get("SubnetSet") is not None:
            self._SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = VpcSubnetViewInfo()
                obj._deserialize(item)
                self._SubnetSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpnConnection(AbstractModel):
    """VPN通道对象。

    """

    def __init__(self):
        r"""
        :param _VpnConnectionId: 通道实例ID。
        :type VpnConnectionId: str
        :param _VpnConnectionName: 通道名称。
        :type VpnConnectionName: str
        :param _VpcId: VPC实例ID。
        :type VpcId: str
        :param _VpnGatewayId: VPN网关实例ID。
        :type VpnGatewayId: str
        :param _CustomerGatewayId: 对端网关实例ID。
        :type CustomerGatewayId: str
        :param _PreShareKey: 预共享密钥。
        :type PreShareKey: str
        :param _VpnProto: 通道传输协议。
        :type VpnProto: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _State: 通道的生产状态
        :type State: str
        :param _NetStatus: 通道连接状态
        :type NetStatus: str
        :param _SecurityPolicyDatabaseSet: SPD。
        :type SecurityPolicyDatabaseSet: list of SecurityPolicyDatabase
        :param _IKEOptionsSpecification: IKE选项。
        :type IKEOptionsSpecification: :class:`tencentcloud.bmvpc.v20180625.models.IKEOptionsSpecification`
        :param _IPSECOptionsSpecification: IPSEC选项。
        :type IPSECOptionsSpecification: :class:`tencentcloud.bmvpc.v20180625.models.IPSECOptionsSpecification`
        :param _Zone: 可用区
        :type Zone: str
        :param _VpcCidrBlock: VPC网段
        :type VpcCidrBlock: str
        :param _VpcName: VPC名称
        :type VpcName: str
        :param _VpnGatewayName: VPN网关名称
        :type VpnGatewayName: str
        :param _CustomerGatewayName: 对端网关名称
        :type CustomerGatewayName: str
        :param _DestinationCidr: IPSEC VPN通道路由策略目的端地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DestinationCidr: list of str
        :param _SourceCidr: IPSEC VPN通道路由策略源端地址
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceCidr: list of str
        """
        self._VpnConnectionId = None
        self._VpnConnectionName = None
        self._VpcId = None
        self._VpnGatewayId = None
        self._CustomerGatewayId = None
        self._PreShareKey = None
        self._VpnProto = None
        self._CreateTime = None
        self._State = None
        self._NetStatus = None
        self._SecurityPolicyDatabaseSet = None
        self._IKEOptionsSpecification = None
        self._IPSECOptionsSpecification = None
        self._Zone = None
        self._VpcCidrBlock = None
        self._VpcName = None
        self._VpnGatewayName = None
        self._CustomerGatewayName = None
        self._DestinationCidr = None
        self._SourceCidr = None

    @property
    def VpnConnectionId(self):
        return self._VpnConnectionId

    @VpnConnectionId.setter
    def VpnConnectionId(self, VpnConnectionId):
        self._VpnConnectionId = VpnConnectionId

    @property
    def VpnConnectionName(self):
        return self._VpnConnectionName

    @VpnConnectionName.setter
    def VpnConnectionName(self, VpnConnectionName):
        self._VpnConnectionName = VpnConnectionName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpnGatewayId(self):
        return self._VpnGatewayId

    @VpnGatewayId.setter
    def VpnGatewayId(self, VpnGatewayId):
        self._VpnGatewayId = VpnGatewayId

    @property
    def CustomerGatewayId(self):
        return self._CustomerGatewayId

    @CustomerGatewayId.setter
    def CustomerGatewayId(self, CustomerGatewayId):
        self._CustomerGatewayId = CustomerGatewayId

    @property
    def PreShareKey(self):
        return self._PreShareKey

    @PreShareKey.setter
    def PreShareKey(self, PreShareKey):
        self._PreShareKey = PreShareKey

    @property
    def VpnProto(self):
        return self._VpnProto

    @VpnProto.setter
    def VpnProto(self, VpnProto):
        self._VpnProto = VpnProto

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def NetStatus(self):
        return self._NetStatus

    @NetStatus.setter
    def NetStatus(self, NetStatus):
        self._NetStatus = NetStatus

    @property
    def SecurityPolicyDatabaseSet(self):
        return self._SecurityPolicyDatabaseSet

    @SecurityPolicyDatabaseSet.setter
    def SecurityPolicyDatabaseSet(self, SecurityPolicyDatabaseSet):
        self._SecurityPolicyDatabaseSet = SecurityPolicyDatabaseSet

    @property
    def IKEOptionsSpecification(self):
        return self._IKEOptionsSpecification

    @IKEOptionsSpecification.setter
    def IKEOptionsSpecification(self, IKEOptionsSpecification):
        self._IKEOptionsSpecification = IKEOptionsSpecification

    @property
    def IPSECOptionsSpecification(self):
        return self._IPSECOptionsSpecification

    @IPSECOptionsSpecification.setter
    def IPSECOptionsSpecification(self, IPSECOptionsSpecification):
        self._IPSECOptionsSpecification = IPSECOptionsSpecification

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcCidrBlock(self):
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpnGatewayName(self):
        return self._VpnGatewayName

    @VpnGatewayName.setter
    def VpnGatewayName(self, VpnGatewayName):
        self._VpnGatewayName = VpnGatewayName

    @property
    def CustomerGatewayName(self):
        return self._CustomerGatewayName

    @CustomerGatewayName.setter
    def CustomerGatewayName(self, CustomerGatewayName):
        self._CustomerGatewayName = CustomerGatewayName

    @property
    def DestinationCidr(self):
        return self._DestinationCidr

    @DestinationCidr.setter
    def DestinationCidr(self, DestinationCidr):
        self._DestinationCidr = DestinationCidr

    @property
    def SourceCidr(self):
        return self._SourceCidr

    @SourceCidr.setter
    def SourceCidr(self, SourceCidr):
        self._SourceCidr = SourceCidr


    def _deserialize(self, params):
        self._VpnConnectionId = params.get("VpnConnectionId")
        self._VpnConnectionName = params.get("VpnConnectionName")
        self._VpcId = params.get("VpcId")
        self._VpnGatewayId = params.get("VpnGatewayId")
        self._CustomerGatewayId = params.get("CustomerGatewayId")
        self._PreShareKey = params.get("PreShareKey")
        self._VpnProto = params.get("VpnProto")
        self._CreateTime = params.get("CreateTime")
        self._State = params.get("State")
        self._NetStatus = params.get("NetStatus")
        if params.get("SecurityPolicyDatabaseSet") is not None:
            self._SecurityPolicyDatabaseSet = []
            for item in params.get("SecurityPolicyDatabaseSet"):
                obj = SecurityPolicyDatabase()
                obj._deserialize(item)
                self._SecurityPolicyDatabaseSet.append(obj)
        if params.get("IKEOptionsSpecification") is not None:
            self._IKEOptionsSpecification = IKEOptionsSpecification()
            self._IKEOptionsSpecification._deserialize(params.get("IKEOptionsSpecification"))
        if params.get("IPSECOptionsSpecification") is not None:
            self._IPSECOptionsSpecification = IPSECOptionsSpecification()
            self._IPSECOptionsSpecification._deserialize(params.get("IPSECOptionsSpecification"))
        self._Zone = params.get("Zone")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._VpcName = params.get("VpcName")
        self._VpnGatewayName = params.get("VpnGatewayName")
        self._CustomerGatewayName = params.get("CustomerGatewayName")
        self._DestinationCidr = params.get("DestinationCidr")
        self._SourceCidr = params.get("SourceCidr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpnGateway(AbstractModel):
    """VPN网关对象。

    """

    def __init__(self):
        r"""
        :param _VpnGatewayId: 网关实例ID。
        :type VpnGatewayId: str
        :param _VpcId: VPC实例ID。
        :type VpcId: str
        :param _VpnGatewayName: 网关实例名称。
        :type VpnGatewayName: str
        :param _VpcCidrBlock: VPC网段
        :type VpcCidrBlock: str
        :param _VpcName: VPC名称
        :type VpcName: str
        :param _InternetMaxBandwidthOut: 网关出带宽。
        :type InternetMaxBandwidthOut: int
        :param _State: 网关实例状态
        :type State: str
        :param _PublicIpAddress: 网关公网IP。
        :type PublicIpAddress: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _Zone: 可用区，如：ap-guangzhou
        :type Zone: str
        :param _VpnConnNum: VPN网关的通道数
        :type VpnConnNum: int
        """
        self._VpnGatewayId = None
        self._VpcId = None
        self._VpnGatewayName = None
        self._VpcCidrBlock = None
        self._VpcName = None
        self._InternetMaxBandwidthOut = None
        self._State = None
        self._PublicIpAddress = None
        self._CreateTime = None
        self._Zone = None
        self._VpnConnNum = None

    @property
    def VpnGatewayId(self):
        return self._VpnGatewayId

    @VpnGatewayId.setter
    def VpnGatewayId(self, VpnGatewayId):
        self._VpnGatewayId = VpnGatewayId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpnGatewayName(self):
        return self._VpnGatewayName

    @VpnGatewayName.setter
    def VpnGatewayName(self, VpnGatewayName):
        self._VpnGatewayName = VpnGatewayName

    @property
    def VpcCidrBlock(self):
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def PublicIpAddress(self):
        return self._PublicIpAddress

    @PublicIpAddress.setter
    def PublicIpAddress(self, PublicIpAddress):
        self._PublicIpAddress = PublicIpAddress

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpnConnNum(self):
        return self._VpnConnNum

    @VpnConnNum.setter
    def VpnConnNum(self, VpnConnNum):
        self._VpnConnNum = VpnConnNum


    def _deserialize(self, params):
        self._VpnGatewayId = params.get("VpnGatewayId")
        self._VpcId = params.get("VpcId")
        self._VpnGatewayName = params.get("VpnGatewayName")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._VpcName = params.get("VpcName")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._State = params.get("State")
        self._PublicIpAddress = params.get("PublicIpAddress")
        self._CreateTime = params.get("CreateTime")
        self._Zone = params.get("Zone")
        self._VpnConnNum = params.get("VpnConnNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        