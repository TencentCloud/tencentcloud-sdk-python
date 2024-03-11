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


class BindEipAclsRequest(AbstractModel):
    """BindEipAcls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EipIdAclIdList: 待关联的 EIP 与 ACL关系列表
        :type EipIdAclIdList: list of EipAclMap
        """
        self._EipIdAclIdList = None

    @property
    def EipIdAclIdList(self):
        return self._EipIdAclIdList

    @EipIdAclIdList.setter
    def EipIdAclIdList(self, EipIdAclIdList):
        self._EipIdAclIdList = EipIdAclIdList


    def _deserialize(self, params):
        if params.get("EipIdAclIdList") is not None:
            self._EipIdAclIdList = []
            for item in params.get("EipIdAclIdList"):
                obj = EipAclMap()
                obj._deserialize(item)
                self._EipIdAclIdList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindEipAclsResponse(AbstractModel):
    """BindEipAcls返回参数结构体

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


class BindHostedRequest(AbstractModel):
    """BindHosted请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EipId: Eip实例ID，可通过DescribeBmEip 接口返回字段中的 eipId获取。Eip和EipId参数必须要填写一个。
        :type EipId: str
        :param _InstanceId: 托管机器实例ID
        :type InstanceId: str
        """
        self._EipId = None
        self._InstanceId = None

    @property
    def EipId(self):
        return self._EipId

    @EipId.setter
    def EipId(self, EipId):
        self._EipId = EipId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._EipId = params.get("EipId")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindHostedResponse(AbstractModel):
    """BindHosted返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID，可以通过EipBmQueryTask查询任务状态
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class BindRsRequest(AbstractModel):
    """BindRs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EipId: Eip实例ID
        :type EipId: str
        :param _InstanceId: 物理服务器实例ID
        :type InstanceId: str
        """
        self._EipId = None
        self._InstanceId = None

    @property
    def EipId(self):
        return self._EipId

    @EipId.setter
    def EipId(self, EipId):
        self._EipId = EipId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._EipId = params.get("EipId")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRsResponse(AbstractModel):
    """BindRs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 绑定黑石物理机异步任务ID，可以通过DescribeEipTask查询任务状态
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class BindVpcIpRequest(AbstractModel):
    """BindVpcIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EipId: Eip实例ID
        :type EipId: str
        :param _VpcId: EIP归属VpcId，例如vpc-k7j1t2x1
        :type VpcId: str
        :param _VpcIp: 绑定的VPC内IP地址
        :type VpcIp: str
        """
        self._EipId = None
        self._VpcId = None
        self._VpcIp = None

    @property
    def EipId(self):
        return self._EipId

    @EipId.setter
    def EipId(self, EipId):
        self._EipId = EipId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcIp(self):
        return self._VpcIp

    @VpcIp.setter
    def VpcIp(self, VpcIp):
        self._VpcIp = VpcIp


    def _deserialize(self, params):
        self._EipId = params.get("EipId")
        self._VpcId = params.get("VpcId")
        self._VpcIp = params.get("VpcIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindVpcIpResponse(AbstractModel):
    """BindVpcIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: EIP绑定VPC网络IP异步任务ID，可以通过查询EIP任务状态查询任务状态
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CreateEipAclRequest(AbstractModel):
    """CreateEipAcl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AclName: ACL 名称
        :type AclName: str
        :param _Status: ACL 状态 0：无状态，1：有状态
        :type Status: int
        """
        self._AclName = None
        self._Status = None

    @property
    def AclName(self):
        return self._AclName

    @AclName.setter
    def AclName(self, AclName):
        self._AclName = AclName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._AclName = params.get("AclName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEipAclResponse(AbstractModel):
    """CreateEipAcl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AclId: ACL 实例 ID
        :type AclId: str
        :param _Status: ACL 实例状态
        :type Status: int
        :param _AclName: ACL 实例名称
        :type AclName: str
        :param _CreatedAt: ACL 实例创建时间
        :type CreatedAt: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AclId = None
        self._Status = None
        self._AclName = None
        self._CreatedAt = None
        self._RequestId = None

    @property
    def AclId(self):
        return self._AclId

    @AclId.setter
    def AclId(self, AclId):
        self._AclId = AclId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AclName(self):
        return self._AclName

    @AclName.setter
    def AclName(self, AclName):
        self._AclName = AclName

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AclId = params.get("AclId")
        self._Status = params.get("Status")
        self._AclName = params.get("AclName")
        self._CreatedAt = params.get("CreatedAt")
        self._RequestId = params.get("RequestId")


class CreateEipRequest(AbstractModel):
    """CreateEip请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GoodsNum: 申请数量，默认为1, 最大 20
        :type GoodsNum: int
        :param _PayMode: EIP计费方式，flow-流量计费；bandwidth-带宽计费
        :type PayMode: str
        :param _Bandwidth: 带宽设定值（只在带宽计费时生效）
        :type Bandwidth: int
        :param _SetType: EIP模式，目前支持tunnel和fullnat
        :type SetType: str
        :param _Exclusive: 是否使用独占集群，0：不使用，1：使用。默认为0
        :type Exclusive: int
        :param _VpcId: EIP归属私有网络ID，例如vpc-k7j1t2x1
        :type VpcId: str
        :param _IpList: 指定申请的IP列表
        :type IpList: list of str
        """
        self._GoodsNum = None
        self._PayMode = None
        self._Bandwidth = None
        self._SetType = None
        self._Exclusive = None
        self._VpcId = None
        self._IpList = None

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def SetType(self):
        return self._SetType

    @SetType.setter
    def SetType(self, SetType):
        self._SetType = SetType

    @property
    def Exclusive(self):
        return self._Exclusive

    @Exclusive.setter
    def Exclusive(self, Exclusive):
        self._Exclusive = Exclusive

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._GoodsNum = params.get("GoodsNum")
        self._PayMode = params.get("PayMode")
        self._Bandwidth = params.get("Bandwidth")
        self._SetType = params.get("SetType")
        self._Exclusive = params.get("Exclusive")
        self._VpcId = params.get("VpcId")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEipResponse(AbstractModel):
    """CreateEip返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EipIds: EIP列表
        :type EipIds: list of str
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EipIds = None
        self._TaskId = None
        self._RequestId = None

    @property
    def EipIds(self):
        return self._EipIds

    @EipIds.setter
    def EipIds(self, EipIds):
        self._EipIds = EipIds

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
        self._EipIds = params.get("EipIds")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteEipAclRequest(AbstractModel):
    """DeleteEipAcl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AclId: 待删除的 ACL 实例 ID
        :type AclId: str
        """
        self._AclId = None

    @property
    def AclId(self):
        return self._AclId

    @AclId.setter
    def AclId(self, AclId):
        self._AclId = AclId


    def _deserialize(self, params):
        self._AclId = params.get("AclId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEipAclResponse(AbstractModel):
    """DeleteEipAcl返回参数结构体

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


class DeleteEipRequest(AbstractModel):
    """DeleteEip请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EipIds: Eip实例ID列表
        :type EipIds: list of str
        """
        self._EipIds = None

    @property
    def EipIds(self):
        return self._EipIds

    @EipIds.setter
    def EipIds(self, EipIds):
        self._EipIds = EipIds


    def _deserialize(self, params):
        self._EipIds = params.get("EipIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEipResponse(AbstractModel):
    """DeleteEip返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务Id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeEipAclsRequest(AbstractModel):
    """DescribeEipAcls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AclName: ACL 名称，支持模糊查找
        :type AclName: str
        :param _AclIds: ACL 实例 ID 列表，数组下标从 0 开始
        :type AclIds: list of str
        :param _Offset: 分页参数。偏移量，默认为 0
        :type Offset: int
        :param _Limit: 分页参数。每一页的 EIPACL 列表数目
        :type Limit: int
        :param _EipIds: EIP实例ID列表
        :type EipIds: list of str
        :param _EipIps: EIP IP地址列表
        :type EipIps: list of str
        :param _EipNames: EIP名称列表
        :type EipNames: list of str
        :param _OrderField: 排序字段
        :type OrderField: str
        :param _Order: 排序方式，取值：0:增序(默认)，1:降序
        :type Order: int
        :param _AclNames: ACL名称列表，支持模糊查找
        :type AclNames: list of str
        """
        self._AclName = None
        self._AclIds = None
        self._Offset = None
        self._Limit = None
        self._EipIds = None
        self._EipIps = None
        self._EipNames = None
        self._OrderField = None
        self._Order = None
        self._AclNames = None

    @property
    def AclName(self):
        return self._AclName

    @AclName.setter
    def AclName(self, AclName):
        self._AclName = AclName

    @property
    def AclIds(self):
        return self._AclIds

    @AclIds.setter
    def AclIds(self, AclIds):
        self._AclIds = AclIds

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
    def EipIds(self):
        return self._EipIds

    @EipIds.setter
    def EipIds(self, EipIds):
        self._EipIds = EipIds

    @property
    def EipIps(self):
        return self._EipIps

    @EipIps.setter
    def EipIps(self, EipIps):
        self._EipIps = EipIps

    @property
    def EipNames(self):
        return self._EipNames

    @EipNames.setter
    def EipNames(self, EipNames):
        self._EipNames = EipNames

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def AclNames(self):
        return self._AclNames

    @AclNames.setter
    def AclNames(self, AclNames):
        self._AclNames = AclNames


    def _deserialize(self, params):
        self._AclName = params.get("AclName")
        self._AclIds = params.get("AclIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._EipIds = params.get("EipIds")
        self._EipIps = params.get("EipIps")
        self._EipNames = params.get("EipNames")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        self._AclNames = params.get("AclNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEipAclsResponse(AbstractModel):
    """DescribeEipAcls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回 EIPACL 列表总数
        :type TotalCount: int
        :param _EipAclList: EIPACL列表
        :type EipAclList: list of EipAcl
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._EipAclList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EipAclList(self):
        return self._EipAclList

    @EipAclList.setter
    def EipAclList(self, EipAclList):
        self._EipAclList = EipAclList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("EipAclList") is not None:
            self._EipAclList = []
            for item in params.get("EipAclList"):
                obj = EipAcl()
                obj._deserialize(item)
                self._EipAclList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEipQuotaRequest(AbstractModel):
    """DescribeEipQuota请求参数结构体

    """


class DescribeEipQuotaResponse(AbstractModel):
    """DescribeEipQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EipNumQuota: 能拥有的EIP个数的总配额，默认是100个
        :type EipNumQuota: int
        :param _CurrentEipNum: 当前已使用的EIP个数，包括创建中、绑定中、已绑定、解绑中、未绑定几种状态的EIP个数总和
        :type CurrentEipNum: int
        :param _DailyApplyCount: 当天申请EIP次数
        :type DailyApplyCount: int
        :param _DailyApplyQuota: 每日申请EIP的次数限制
        :type DailyApplyQuota: int
        :param _BatchApplyMax: BatchApplyMax
        :type BatchApplyMax: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EipNumQuota = None
        self._CurrentEipNum = None
        self._DailyApplyCount = None
        self._DailyApplyQuota = None
        self._BatchApplyMax = None
        self._RequestId = None

    @property
    def EipNumQuota(self):
        return self._EipNumQuota

    @EipNumQuota.setter
    def EipNumQuota(self, EipNumQuota):
        self._EipNumQuota = EipNumQuota

    @property
    def CurrentEipNum(self):
        return self._CurrentEipNum

    @CurrentEipNum.setter
    def CurrentEipNum(self, CurrentEipNum):
        self._CurrentEipNum = CurrentEipNum

    @property
    def DailyApplyCount(self):
        return self._DailyApplyCount

    @DailyApplyCount.setter
    def DailyApplyCount(self, DailyApplyCount):
        self._DailyApplyCount = DailyApplyCount

    @property
    def DailyApplyQuota(self):
        return self._DailyApplyQuota

    @DailyApplyQuota.setter
    def DailyApplyQuota(self, DailyApplyQuota):
        self._DailyApplyQuota = DailyApplyQuota

    @property
    def BatchApplyMax(self):
        return self._BatchApplyMax

    @BatchApplyMax.setter
    def BatchApplyMax(self, BatchApplyMax):
        self._BatchApplyMax = BatchApplyMax

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EipNumQuota = params.get("EipNumQuota")
        self._CurrentEipNum = params.get("CurrentEipNum")
        self._DailyApplyCount = params.get("DailyApplyCount")
        self._DailyApplyQuota = params.get("DailyApplyQuota")
        self._BatchApplyMax = params.get("BatchApplyMax")
        self._RequestId = params.get("RequestId")


class DescribeEipTaskRequest(AbstractModel):
    """DescribeEipTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: EIP查询任务ID
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
        


class DescribeEipTaskResponse(AbstractModel):
    """DescribeEipTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 当前任务状态码：0-成功，1-失败，2-进行中
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeEipsRequest(AbstractModel):
    """DescribeEips请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EipIds: EIP实例ID列表
        :type EipIds: list of str
        :param _Eips: EIP IP 列表
        :type Eips: list of str
        :param _InstanceIds: 主机实例ID 列表
        :type InstanceIds: list of str
        :param _SearchKey: EIP名称,模糊匹配
        :type SearchKey: str
        :param _Status: 状态列表, 默认所有
        :type Status: list of int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回EIP数量，默认 20, 最大值 100
        :type Limit: int
        :param _OrderField: 排序字段，支持： EipId,Eip,Status, InstanceId,CreatedAt
        :type OrderField: str
        :param _Order: 排序方式 0:递增 1:递减(默认)
        :type Order: int
        :param _PayMode: 计费模式,流量：flow，带宽：bandwidth
        :type PayMode: str
        :param _VpcId: EIP归属VpcId，例如vpc-k7j1t2x1
        :type VpcId: str
        :param _BindTypes: 绑定类型，-1：未绑定，0：物理机，1：nat网关，2：虚拟IP, 3:托管机器
        :type BindTypes: list of int
        :param _ExclusiveTag: 独占标志，0：共享，1：独占
        :type ExclusiveTag: int
        :param _AclId: EIP ACL实例ID
        :type AclId: str
        :param _BindAcl: 搜索条件，是否绑定了EIP ACL， 0：未绑定，1：绑定
        :type BindAcl: int
        """
        self._EipIds = None
        self._Eips = None
        self._InstanceIds = None
        self._SearchKey = None
        self._Status = None
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._Order = None
        self._PayMode = None
        self._VpcId = None
        self._BindTypes = None
        self._ExclusiveTag = None
        self._AclId = None
        self._BindAcl = None

    @property
    def EipIds(self):
        return self._EipIds

    @EipIds.setter
    def EipIds(self, EipIds):
        self._EipIds = EipIds

    @property
    def Eips(self):
        return self._Eips

    @Eips.setter
    def Eips(self, Eips):
        self._Eips = Eips

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def BindTypes(self):
        return self._BindTypes

    @BindTypes.setter
    def BindTypes(self, BindTypes):
        self._BindTypes = BindTypes

    @property
    def ExclusiveTag(self):
        return self._ExclusiveTag

    @ExclusiveTag.setter
    def ExclusiveTag(self, ExclusiveTag):
        self._ExclusiveTag = ExclusiveTag

    @property
    def AclId(self):
        return self._AclId

    @AclId.setter
    def AclId(self, AclId):
        self._AclId = AclId

    @property
    def BindAcl(self):
        return self._BindAcl

    @BindAcl.setter
    def BindAcl(self, BindAcl):
        self._BindAcl = BindAcl


    def _deserialize(self, params):
        self._EipIds = params.get("EipIds")
        self._Eips = params.get("Eips")
        self._InstanceIds = params.get("InstanceIds")
        self._SearchKey = params.get("SearchKey")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        self._PayMode = params.get("PayMode")
        self._VpcId = params.get("VpcId")
        self._BindTypes = params.get("BindTypes")
        self._ExclusiveTag = params.get("ExclusiveTag")
        self._AclId = params.get("AclId")
        self._BindAcl = params.get("BindAcl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEipsResponse(AbstractModel):
    """DescribeEips返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EipSet: 返回EIP信息数组
        :type EipSet: list of EipInfo
        :param _TotalCount: 返回EIP数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EipSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def EipSet(self):
        return self._EipSet

    @EipSet.setter
    def EipSet(self, EipSet):
        self._EipSet = EipSet

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
        if params.get("EipSet") is not None:
            self._EipSet = []
            for item in params.get("EipSet"):
                obj = EipInfo()
                obj._deserialize(item)
                self._EipSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class EipAcl(AbstractModel):
    """EipAcl信息

    """

    def __init__(self):
        r"""
        :param _AclId: ACL 实例 ID。
        :type AclId: str
        :param _AclName: ACL 实例名称
        :type AclName: str
        :param _Status: ACL 状态。0：无状态，1：有状态
        :type Status: str
        :param _CreatedAt: EIPACL 创建时间
        :type CreatedAt: str
        :param _EipNum: EIPACL 已关联的 eip 数目
        :type EipNum: int
        :param _OutRules: 出站规则
        :type OutRules: list of EipAclRule
        :param _InRules: 入站规则
        :type InRules: list of EipAclRule
        """
        self._AclId = None
        self._AclName = None
        self._Status = None
        self._CreatedAt = None
        self._EipNum = None
        self._OutRules = None
        self._InRules = None

    @property
    def AclId(self):
        return self._AclId

    @AclId.setter
    def AclId(self, AclId):
        self._AclId = AclId

    @property
    def AclName(self):
        return self._AclName

    @AclName.setter
    def AclName(self, AclName):
        self._AclName = AclName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def EipNum(self):
        return self._EipNum

    @EipNum.setter
    def EipNum(self, EipNum):
        self._EipNum = EipNum

    @property
    def OutRules(self):
        return self._OutRules

    @OutRules.setter
    def OutRules(self, OutRules):
        self._OutRules = OutRules

    @property
    def InRules(self):
        return self._InRules

    @InRules.setter
    def InRules(self, InRules):
        self._InRules = InRules


    def _deserialize(self, params):
        self._AclId = params.get("AclId")
        self._AclName = params.get("AclName")
        self._Status = params.get("Status")
        self._CreatedAt = params.get("CreatedAt")
        self._EipNum = params.get("EipNum")
        if params.get("OutRules") is not None:
            self._OutRules = []
            for item in params.get("OutRules"):
                obj = EipAclRule()
                obj._deserialize(item)
                self._OutRules.append(obj)
        if params.get("InRules") is not None:
            self._InRules = []
            for item in params.get("InRules"):
                obj = EipAclRule()
                obj._deserialize(item)
                self._InRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipAclMap(AbstractModel):
    """eipid与aclid关联关系

    """

    def __init__(self):
        r"""
        :param _EipId: EIP 实例 ID
        :type EipId: str
        :param _AclId: ACL 实例 ID
        :type AclId: str
        """
        self._EipId = None
        self._AclId = None

    @property
    def EipId(self):
        return self._EipId

    @EipId.setter
    def EipId(self, EipId):
        self._EipId = EipId

    @property
    def AclId(self):
        return self._AclId

    @AclId.setter
    def AclId(self, AclId):
        self._AclId = AclId


    def _deserialize(self, params):
        self._EipId = params.get("EipId")
        self._AclId = params.get("AclId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipAclRule(AbstractModel):
    """eipacl规则

    """

    def __init__(self):
        r"""
        :param _Ip: 源 IP
        :type Ip: str
        :param _Port: 目标端口
        :type Port: str
        :param _Protocol: 协议(TCP/UDP/ICMP/ANY)
        :type Protocol: str
        :param _Action: 策略（accept/drop）
        :type Action: str
        :param _Description: 备注
        :type Description: str
        """
        self._Ip = None
        self._Port = None
        self._Protocol = None
        self._Action = None
        self._Description = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        self._Action = params.get("Action")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipInfo(AbstractModel):
    """Eip信息

    """

    def __init__(self):
        r"""
        :param _EipId: EIP实例ID
        :type EipId: str
        :param _EipName: EIP名称
        :type EipName: str
        :param _Eip: EIP地址
        :type Eip: str
        :param _IspId: 运营商ID 0：电信； 1：联通； 2：移动； 3：教育网； 4：盈科； 5：BGP； 6：中国香港
        :type IspId: int
        :param _Status: 状态 0：创建中； 1：绑定中； 2：已绑定； 3：解绑中； 4：未绑定； 6：下线中； 9：创建失败
        :type Status: int
        :param _Arrears: 是否欠费隔离 1： 欠费隔离； 0： 正常。处在欠费隔离情况下的EIP不能进行任何管理操作。
        :type Arrears: int
        :param _InstanceId: EIP所绑定的服务器实例ID，未绑定则为空
        :type InstanceId: str
        :param _InstanceAlias: 服务器别名
        :type InstanceAlias: str
        :param _FreeAt: EIP解绑时间
        :type FreeAt: str
        :param _CreatedAt: EIP创建时间
        :type CreatedAt: str
        :param _UpdatedAt: EIP更新时间
        :type UpdatedAt: str
        :param _FreeSecond: EIP未绑定服务器时长（单位：秒）
        :type FreeSecond: int
        :param _Type: EIP所绑定的资源类型，-1：未绑定资源；0：黑石物理机，字段对应unInstanceId；1：Nat网关，字段对应natUid；2：云服务器字段对应vpcIp; 3: 托管机器，字段对应HInstanceId, HInstanceAlias
        :type Type: int
        :param _PayMode: EIP计费模式，"flow"：流量计费； "bandwidth"：带宽计费
        :type PayMode: str
        :param _Bandwidth: EIP带宽计费模式下的带宽上限（单位：MB）
        :type Bandwidth: int
        :param _LatestPayMode: 最近一次操作变更的EIP计费模式，"flow"：流量计费； "bandwidth"：带宽计费
        :type LatestPayMode: str
        :param _LatestBandwidth: 最近一次操作变更的EIP计费模式对应的带宽上限值，仅在带宽计费模式下有效（单位：MB）
        :type LatestBandwidth: int
        :param _VpcName: 私有网络名称
        :type VpcName: str
        :param _NatId: EIP所绑定的NAT网关的数字ID，形如：1001,，未绑定则为空
        :type NatId: int
        :param _NatUid: EIP所绑定的NAT网关实例ID，形如："nat-n47xxxxx"，未绑定则为空
        :type NatUid: str
        :param _VpcIp: EIP所绑定的云服务器IP(托管或者云服务器的IP），形如："10.1.1.3"。 注意：IP资源需要通过bmvpc模块注册或者申请后才可以绑定eip，接口使用申请子网IP和注册子网IP：,未绑定则为空
        :type VpcIp: str
        :param _VpcId: 私有网络实例ID
        :type VpcId: str
        :param _Exclusive: 是否为独占类型EIP
        :type Exclusive: int
        :param _VpcCidr: 私有网络的cidr
        :type VpcCidr: str
        :param _AclId: EIP ACL实例ID
        :type AclId: str
        :param _AclName: EIP ACL名称
        :type AclName: str
        :param _HInstanceId: 托管机器实例ID
        :type HInstanceId: str
        :param _HInstanceAlias: 托管机器别名
        :type HInstanceAlias: str
        """
        self._EipId = None
        self._EipName = None
        self._Eip = None
        self._IspId = None
        self._Status = None
        self._Arrears = None
        self._InstanceId = None
        self._InstanceAlias = None
        self._FreeAt = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._FreeSecond = None
        self._Type = None
        self._PayMode = None
        self._Bandwidth = None
        self._LatestPayMode = None
        self._LatestBandwidth = None
        self._VpcName = None
        self._NatId = None
        self._NatUid = None
        self._VpcIp = None
        self._VpcId = None
        self._Exclusive = None
        self._VpcCidr = None
        self._AclId = None
        self._AclName = None
        self._HInstanceId = None
        self._HInstanceAlias = None

    @property
    def EipId(self):
        return self._EipId

    @EipId.setter
    def EipId(self, EipId):
        self._EipId = EipId

    @property
    def EipName(self):
        return self._EipName

    @EipName.setter
    def EipName(self, EipName):
        self._EipName = EipName

    @property
    def Eip(self):
        return self._Eip

    @Eip.setter
    def Eip(self, Eip):
        self._Eip = Eip

    @property
    def IspId(self):
        return self._IspId

    @IspId.setter
    def IspId(self, IspId):
        self._IspId = IspId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Arrears(self):
        return self._Arrears

    @Arrears.setter
    def Arrears(self, Arrears):
        self._Arrears = Arrears

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceAlias(self):
        return self._InstanceAlias

    @InstanceAlias.setter
    def InstanceAlias(self, InstanceAlias):
        self._InstanceAlias = InstanceAlias

    @property
    def FreeAt(self):
        return self._FreeAt

    @FreeAt.setter
    def FreeAt(self, FreeAt):
        self._FreeAt = FreeAt

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def FreeSecond(self):
        return self._FreeSecond

    @FreeSecond.setter
    def FreeSecond(self, FreeSecond):
        self._FreeSecond = FreeSecond

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def LatestPayMode(self):
        return self._LatestPayMode

    @LatestPayMode.setter
    def LatestPayMode(self, LatestPayMode):
        self._LatestPayMode = LatestPayMode

    @property
    def LatestBandwidth(self):
        return self._LatestBandwidth

    @LatestBandwidth.setter
    def LatestBandwidth(self, LatestBandwidth):
        self._LatestBandwidth = LatestBandwidth

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def NatId(self):
        return self._NatId

    @NatId.setter
    def NatId(self, NatId):
        self._NatId = NatId

    @property
    def NatUid(self):
        return self._NatUid

    @NatUid.setter
    def NatUid(self, NatUid):
        self._NatUid = NatUid

    @property
    def VpcIp(self):
        return self._VpcIp

    @VpcIp.setter
    def VpcIp(self, VpcIp):
        self._VpcIp = VpcIp

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Exclusive(self):
        return self._Exclusive

    @Exclusive.setter
    def Exclusive(self, Exclusive):
        self._Exclusive = Exclusive

    @property
    def VpcCidr(self):
        return self._VpcCidr

    @VpcCidr.setter
    def VpcCidr(self, VpcCidr):
        self._VpcCidr = VpcCidr

    @property
    def AclId(self):
        return self._AclId

    @AclId.setter
    def AclId(self, AclId):
        self._AclId = AclId

    @property
    def AclName(self):
        return self._AclName

    @AclName.setter
    def AclName(self, AclName):
        self._AclName = AclName

    @property
    def HInstanceId(self):
        return self._HInstanceId

    @HInstanceId.setter
    def HInstanceId(self, HInstanceId):
        self._HInstanceId = HInstanceId

    @property
    def HInstanceAlias(self):
        return self._HInstanceAlias

    @HInstanceAlias.setter
    def HInstanceAlias(self, HInstanceAlias):
        self._HInstanceAlias = HInstanceAlias


    def _deserialize(self, params):
        self._EipId = params.get("EipId")
        self._EipName = params.get("EipName")
        self._Eip = params.get("Eip")
        self._IspId = params.get("IspId")
        self._Status = params.get("Status")
        self._Arrears = params.get("Arrears")
        self._InstanceId = params.get("InstanceId")
        self._InstanceAlias = params.get("InstanceAlias")
        self._FreeAt = params.get("FreeAt")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._FreeSecond = params.get("FreeSecond")
        self._Type = params.get("Type")
        self._PayMode = params.get("PayMode")
        self._Bandwidth = params.get("Bandwidth")
        self._LatestPayMode = params.get("LatestPayMode")
        self._LatestBandwidth = params.get("LatestBandwidth")
        self._VpcName = params.get("VpcName")
        self._NatId = params.get("NatId")
        self._NatUid = params.get("NatUid")
        self._VpcIp = params.get("VpcIp")
        self._VpcId = params.get("VpcId")
        self._Exclusive = params.get("Exclusive")
        self._VpcCidr = params.get("VpcCidr")
        self._AclId = params.get("AclId")
        self._AclName = params.get("AclName")
        self._HInstanceId = params.get("HInstanceId")
        self._HInstanceAlias = params.get("HInstanceAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipRsMap(AbstractModel):
    """EipId与InstanceId绑定关系

    """

    def __init__(self):
        r"""
        :param _EipId: EIP实例 ID
        :type EipId: str
        :param _InstanceId: 黑石物理机实例ID
        :type InstanceId: str
        """
        self._EipId = None
        self._InstanceId = None

    @property
    def EipId(self):
        return self._EipId

    @EipId.setter
    def EipId(self, EipId):
        self._EipId = EipId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._EipId = params.get("EipId")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEipAclRequest(AbstractModel):
    """ModifyEipAcl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AclId: ACL 实例 ID
        :type AclId: str
        :param _AclName: ACL 名称
        :type AclName: str
        :param _Status: ACL 状态。0：无状态 1：有状态
        :type Status: int
        :param _Type: 规则类型（in/out）。in：入站规则 out：出站规则
        :type Type: str
        :param _Rules: ACL规则列表
        :type Rules: list of EipAclRule
        """
        self._AclId = None
        self._AclName = None
        self._Status = None
        self._Type = None
        self._Rules = None

    @property
    def AclId(self):
        return self._AclId

    @AclId.setter
    def AclId(self, AclId):
        self._AclId = AclId

    @property
    def AclName(self):
        return self._AclName

    @AclName.setter
    def AclName(self, AclName):
        self._AclName = AclName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._AclId = params.get("AclId")
        self._AclName = params.get("AclName")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = EipAclRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEipAclResponse(AbstractModel):
    """ModifyEipAcl返回参数结构体

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


class ModifyEipChargeRequest(AbstractModel):
    """ModifyEipCharge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PayMode: EIP计费方式，flow-流量计费；bandwidth-带宽计费
        :type PayMode: str
        :param _EipIds: Eip实例ID列表
        :type EipIds: list of str
        :param _Bandwidth: 带宽设定值（只在带宽计费时生效）
        :type Bandwidth: int
        """
        self._PayMode = None
        self._EipIds = None
        self._Bandwidth = None

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def EipIds(self):
        return self._EipIds

    @EipIds.setter
    def EipIds(self, EipIds):
        self._EipIds = EipIds

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth


    def _deserialize(self, params):
        self._PayMode = params.get("PayMode")
        self._EipIds = params.get("EipIds")
        self._Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEipChargeResponse(AbstractModel):
    """ModifyEipCharge返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 修改计费模式的异步任务ID，可以通过查询EIP任务状态查询任务状态
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyEipNameRequest(AbstractModel):
    """ModifyEipName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EipId: Eip实例ID，可通过/v2/DescribeEip 接口返回字段中的 eipId获取
        :type EipId: str
        :param _EipName: EIP 实例别名
        :type EipName: str
        """
        self._EipId = None
        self._EipName = None

    @property
    def EipId(self):
        return self._EipId

    @EipId.setter
    def EipId(self, EipId):
        self._EipId = EipId

    @property
    def EipName(self):
        return self._EipName

    @EipName.setter
    def EipName(self, EipName):
        self._EipName = EipName


    def _deserialize(self, params):
        self._EipId = params.get("EipId")
        self._EipName = params.get("EipName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEipNameResponse(AbstractModel):
    """ModifyEipName返回参数结构体

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


class UnbindEipAclsRequest(AbstractModel):
    """UnbindEipAcls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EipIdAclIdList: 待解关联的 EIP 与 ACL列表
        :type EipIdAclIdList: list of EipAclMap
        """
        self._EipIdAclIdList = None

    @property
    def EipIdAclIdList(self):
        return self._EipIdAclIdList

    @EipIdAclIdList.setter
    def EipIdAclIdList(self, EipIdAclIdList):
        self._EipIdAclIdList = EipIdAclIdList


    def _deserialize(self, params):
        if params.get("EipIdAclIdList") is not None:
            self._EipIdAclIdList = []
            for item in params.get("EipIdAclIdList"):
                obj = EipAclMap()
                obj._deserialize(item)
                self._EipIdAclIdList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindEipAclsResponse(AbstractModel):
    """UnbindEipAcls返回参数结构体

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


class UnbindHostedRequest(AbstractModel):
    """UnbindHosted请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 托管机器实例ID
        :type InstanceId: str
        :param _EipId: Eip实例ID，可通过DescribeBmEip 接口返回字段中的 eipId获取。Eip和EipId参数必须要填写一个。
        :type EipId: str
        :param _Eip: 弹性IP。Eip和EipId参数必须要填写一个。
        :type Eip: str
        """
        self._InstanceId = None
        self._EipId = None
        self._Eip = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EipId(self):
        return self._EipId

    @EipId.setter
    def EipId(self, EipId):
        self._EipId = EipId

    @property
    def Eip(self):
        return self._Eip

    @Eip.setter
    def Eip(self, Eip):
        self._Eip = Eip


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EipId = params.get("EipId")
        self._Eip = params.get("Eip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindHostedResponse(AbstractModel):
    """UnbindHosted返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID，可以通过EipBmQueryTask查询任务状态
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class UnbindRsListRequest(AbstractModel):
    """UnbindRsList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EipRsList: 物理机绑定的EIP列表
        :type EipRsList: list of EipRsMap
        """
        self._EipRsList = None

    @property
    def EipRsList(self):
        return self._EipRsList

    @EipRsList.setter
    def EipRsList(self, EipRsList):
        self._EipRsList = EipRsList


    def _deserialize(self, params):
        if params.get("EipRsList") is not None:
            self._EipRsList = []
            for item in params.get("EipRsList"):
                obj = EipRsMap()
                obj._deserialize(item)
                self._EipRsList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindRsListResponse(AbstractModel):
    """UnbindRsList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 解绑操作的异步任务ID，可以通过查询EIP任务状态查询任务状态
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class UnbindRsRequest(AbstractModel):
    """UnbindRs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EipId: Eip实例ID
        :type EipId: str
        :param _InstanceId: 物理服务器实例ID
        :type InstanceId: str
        """
        self._EipId = None
        self._InstanceId = None

    @property
    def EipId(self):
        return self._EipId

    @EipId.setter
    def EipId(self, EipId):
        self._EipId = EipId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._EipId = params.get("EipId")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindRsResponse(AbstractModel):
    """UnbindRs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 解绑操作的异步任务ID，可以通过查询EIP任务状态查询任务状态
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class UnbindVpcIpRequest(AbstractModel):
    """UnbindVpcIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EipId: Eip实例ID
        :type EipId: str
        :param _VpcId: EIP归属VpcId，例如vpc-k7j1t2x1
        :type VpcId: str
        :param _VpcIp: 绑定的VPC内IP地址
        :type VpcIp: str
        """
        self._EipId = None
        self._VpcId = None
        self._VpcIp = None

    @property
    def EipId(self):
        return self._EipId

    @EipId.setter
    def EipId(self, EipId):
        self._EipId = EipId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcIp(self):
        return self._VpcIp

    @VpcIp.setter
    def VpcIp(self, VpcIp):
        self._VpcIp = VpcIp


    def _deserialize(self, params):
        self._EipId = params.get("EipId")
        self._VpcId = params.get("VpcId")
        self._VpcIp = params.get("VpcIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindVpcIpResponse(AbstractModel):
    """UnbindVpcIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 绑定黑石物理机异步任务ID，可以通过查询EIP任务状态查询任务状态
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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