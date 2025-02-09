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


class AcceptTccVpcEndPointConnectRequest(AbstractModel):
    """AcceptTccVpcEndPointConnect请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EndPointServiceId: 终端节点服务Id
        :type EndPointServiceId: str
        :param _EndPointId: 终端节点id
        :type EndPointId: list of str
        :param _AcceptFlag: 是否接受连接
        :type AcceptFlag: bool
        """
        self._EndPointServiceId = None
        self._EndPointId = None
        self._AcceptFlag = None

    @property
    def EndPointServiceId(self):
        """终端节点服务Id
        :rtype: str
        """
        return self._EndPointServiceId

    @EndPointServiceId.setter
    def EndPointServiceId(self, EndPointServiceId):
        self._EndPointServiceId = EndPointServiceId

    @property
    def EndPointId(self):
        """终端节点id
        :rtype: list of str
        """
        return self._EndPointId

    @EndPointId.setter
    def EndPointId(self, EndPointId):
        self._EndPointId = EndPointId

    @property
    def AcceptFlag(self):
        """是否接受连接
        :rtype: bool
        """
        return self._AcceptFlag

    @AcceptFlag.setter
    def AcceptFlag(self, AcceptFlag):
        self._AcceptFlag = AcceptFlag


    def _deserialize(self, params):
        self._EndPointServiceId = params.get("EndPointServiceId")
        self._EndPointId = params.get("EndPointId")
        self._AcceptFlag = params.get("AcceptFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcceptTccVpcEndPointConnectResponse(AbstractModel):
    """AcceptTccVpcEndPointConnect返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BindTccVpcEndPointServiceWhiteListRequest(AbstractModel):
    """BindTccVpcEndPointServiceWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EndPointServiceId: 终端节点服务Id
        :type EndPointServiceId: str
        :param _UserUin: 需要开白的用户Uin
        :type UserUin: str
        :param _Description: 用户描述
        :type Description: str
        """
        self._EndPointServiceId = None
        self._UserUin = None
        self._Description = None

    @property
    def EndPointServiceId(self):
        """终端节点服务Id
        :rtype: str
        """
        return self._EndPointServiceId

    @EndPointServiceId.setter
    def EndPointServiceId(self, EndPointServiceId):
        self._EndPointServiceId = EndPointServiceId

    @property
    def UserUin(self):
        """需要开白的用户Uin
        :rtype: str
        """
        return self._UserUin

    @UserUin.setter
    def UserUin(self, UserUin):
        self._UserUin = UserUin

    @property
    def Description(self):
        """用户描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._EndPointServiceId = params.get("EndPointServiceId")
        self._UserUin = params.get("UserUin")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindTccVpcEndPointServiceWhiteListResponse(AbstractModel):
    """BindTccVpcEndPointServiceWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeTccCatalogRequest(AbstractModel):
    """DescribeTccCatalog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CatalogId: 数据目录Id
        :type CatalogId: str
        """
        self._CatalogId = None

    @property
    def CatalogId(self):
        """数据目录Id
        :rtype: str
        """
        return self._CatalogId

    @CatalogId.setter
    def CatalogId(self, CatalogId):
        self._CatalogId = CatalogId


    def _deserialize(self, params):
        self._CatalogId = params.get("CatalogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTccCatalogResponse(AbstractModel):
    """DescribeTccCatalog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TccCatalog: Tcc数据目录信息
        :type TccCatalog: :class:`tencentcloud.tccatalog.v20241024.models.TccCatalogConfig`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TccCatalog = None
        self._RequestId = None

    @property
    def TccCatalog(self):
        """Tcc数据目录信息
        :rtype: :class:`tencentcloud.tccatalog.v20241024.models.TccCatalogConfig`
        """
        return self._TccCatalog

    @TccCatalog.setter
    def TccCatalog(self, TccCatalog):
        self._TccCatalog = TccCatalog

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TccCatalog") is not None:
            self._TccCatalog = TccCatalogConfig()
            self._TccCatalog._deserialize(params.get("TccCatalog"))
        self._RequestId = params.get("RequestId")


class DescribeTccCatalogsRequest(AbstractModel):
    """DescribeTccCatalogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CatalogId: 数据目录Id
        :type CatalogId: str
        :param _Name: 数据目录名称
        :type Name: str
        :param _Type: 数据目录类型,当前支持：TCC-HIVE
        :type Type: str
        :param _Status: 状态信息：注册中0，待测试1，连接成功2，连接失败3，删除中4，已删除5
        :type Status: int
        :param _Operator: 操作人uin
        :type Operator: str
        """
        self._CatalogId = None
        self._Name = None
        self._Type = None
        self._Status = None
        self._Operator = None

    @property
    def CatalogId(self):
        """数据目录Id
        :rtype: str
        """
        return self._CatalogId

    @CatalogId.setter
    def CatalogId(self, CatalogId):
        self._CatalogId = CatalogId

    @property
    def Name(self):
        """数据目录名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """数据目录类型,当前支持：TCC-HIVE
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        """状态信息：注册中0，待测试1，连接成功2，连接失败3，删除中4，已删除5
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operator(self):
        """操作人uin
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._CatalogId = params.get("CatalogId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTccCatalogsResponse(AbstractModel):
    """DescribeTccCatalogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TccCatalogSet: 数据目录列表
        :type TccCatalogSet: list of TccCatalogSet
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TccCatalogSet = None
        self._Total = None
        self._RequestId = None

    @property
    def TccCatalogSet(self):
        """数据目录列表
        :rtype: list of TccCatalogSet
        """
        return self._TccCatalogSet

    @TccCatalogSet.setter
    def TccCatalogSet(self, TccCatalogSet):
        self._TccCatalogSet = TccCatalogSet

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TccCatalogSet") is not None:
            self._TccCatalogSet = []
            for item in params.get("TccCatalogSet"):
                obj = TccCatalogSet()
                obj._deserialize(item)
                self._TccCatalogSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class NetWork(AbstractModel):
    """网络配置信息

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc实例id
        :type VpcId: str
        :param _VpcCidrBlock: vpc网段
        :type VpcCidrBlock: str
        :param _SubnetId: 子网实例id
        :type SubnetId: str
        :param _SubnetCidrBlock: 子网网段
        :type SubnetCidrBlock: str
        :param _ClbIp: 服务clbip
        :type ClbIp: str
        :param _ClbPort: 服务clbPort
        :type ClbPort: str
        """
        self._VpcId = None
        self._VpcCidrBlock = None
        self._SubnetId = None
        self._SubnetCidrBlock = None
        self._ClbIp = None
        self._ClbPort = None

    @property
    def VpcId(self):
        """vpc实例id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcCidrBlock(self):
        """vpc网段
        :rtype: str
        """
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def SubnetId(self):
        """子网实例id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetCidrBlock(self):
        """子网网段
        :rtype: str
        """
        return self._SubnetCidrBlock

    @SubnetCidrBlock.setter
    def SubnetCidrBlock(self, SubnetCidrBlock):
        self._SubnetCidrBlock = SubnetCidrBlock

    @property
    def ClbIp(self):
        """服务clbip
        :rtype: str
        """
        return self._ClbIp

    @ClbIp.setter
    def ClbIp(self, ClbIp):
        self._ClbIp = ClbIp

    @property
    def ClbPort(self):
        """服务clbPort
        :rtype: str
        """
        return self._ClbPort

    @ClbPort.setter
    def ClbPort(self, ClbPort):
        self._ClbPort = ClbPort


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._SubnetId = params.get("SubnetId")
        self._SubnetCidrBlock = params.get("SubnetCidrBlock")
        self._ClbIp = params.get("ClbIp")
        self._ClbPort = params.get("ClbPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TccCatalogConfig(AbstractModel):
    """Tcc数据目录信息

    """

    def __init__(self):
        r"""
        :param _Id: 数据目录唯一id
        :type Id: str
        :param _Name: 数据目录名字
        :type Name: str
        :param _Type: 数据目录类型,当前支持：TCC-HIVE
        :type Type: str
        :param _Comment: 描述信息
        :type Comment: str
        :param _Status: 状态信息：注册中0，待测试1，连接成功2，连接失败3，删除中4，已删除5
        :type Status: int
        :param _Connection: Tcc数据目录连接信息
        :type Connection: :class:`tencentcloud.tccatalog.v20241024.models.TccConnectionConfig`
        :param _Operator: 操作人uin
        :type Operator: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self._Id = None
        self._Name = None
        self._Type = None
        self._Comment = None
        self._Status = None
        self._Connection = None
        self._Operator = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Id(self):
        """数据目录唯一id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """数据目录名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """数据目录类型,当前支持：TCC-HIVE
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Comment(self):
        """描述信息
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Status(self):
        """状态信息：注册中0，待测试1，连接成功2，连接失败3，删除中4，已删除5
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Connection(self):
        """Tcc数据目录连接信息
        :rtype: :class:`tencentcloud.tccatalog.v20241024.models.TccConnectionConfig`
        """
        return self._Connection

    @Connection.setter
    def Connection(self, Connection):
        self._Connection = Connection

    @property
    def Operator(self):
        """操作人uin
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Comment = params.get("Comment")
        self._Status = params.get("Status")
        if params.get("Connection") is not None:
            self._Connection = TccConnectionConfig()
            self._Connection._deserialize(params.get("Connection"))
        self._Operator = params.get("Operator")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TccCatalogSet(AbstractModel):
    """Tcc数据目录信息集合

    """

    def __init__(self):
        r"""
        :param _Id: 数据目录唯一id
        :type Id: str
        :param _Name: 数据目录名字
        :type Name: str
        :param _Type: 数据目录类型,当前支持：TCC-HIVE
        :type Type: str
        :param _Status: 状态信息：注册中0，待测试1，连接成功2，连接失败3，删除中4，已删除5
        :type Status: int
        :param _Operator: 操作人uin
        :type Operator: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self._Id = None
        self._Name = None
        self._Type = None
        self._Status = None
        self._Operator = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Id(self):
        """数据目录唯一id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """数据目录名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """数据目录类型,当前支持：TCC-HIVE
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        """状态信息：注册中0，待测试1，连接成功2，连接失败3，删除中4，已删除5
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operator(self):
        """操作人uin
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._Operator = params.get("Operator")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TccConnection(AbstractModel):
    """Tcc数据目录连接配置

    """

    def __init__(self):
        r"""
        :param _EndpointServiceId: 引擎终端节点服务Id
        :type EndpointServiceId: str
        :param _MetaStoreUrl: 元数据连接串
        :type MetaStoreUrl: str
        :param _NetWork: 网络信息
        :type NetWork: :class:`tencentcloud.tccatalog.v20241024.models.NetWork`
        :param _HiveVersion: hive版本
        :type HiveVersion: str
        :param _Location: hive location
        :type Location: str
        :param _HmsEndpointServiceId: HMS终端节点服务
        :type HmsEndpointServiceId: str
        """
        self._EndpointServiceId = None
        self._MetaStoreUrl = None
        self._NetWork = None
        self._HiveVersion = None
        self._Location = None
        self._HmsEndpointServiceId = None

    @property
    def EndpointServiceId(self):
        """引擎终端节点服务Id
        :rtype: str
        """
        return self._EndpointServiceId

    @EndpointServiceId.setter
    def EndpointServiceId(self, EndpointServiceId):
        self._EndpointServiceId = EndpointServiceId

    @property
    def MetaStoreUrl(self):
        """元数据连接串
        :rtype: str
        """
        return self._MetaStoreUrl

    @MetaStoreUrl.setter
    def MetaStoreUrl(self, MetaStoreUrl):
        self._MetaStoreUrl = MetaStoreUrl

    @property
    def NetWork(self):
        """网络信息
        :rtype: :class:`tencentcloud.tccatalog.v20241024.models.NetWork`
        """
        return self._NetWork

    @NetWork.setter
    def NetWork(self, NetWork):
        self._NetWork = NetWork

    @property
    def HiveVersion(self):
        """hive版本
        :rtype: str
        """
        return self._HiveVersion

    @HiveVersion.setter
    def HiveVersion(self, HiveVersion):
        self._HiveVersion = HiveVersion

    @property
    def Location(self):
        """hive location
        :rtype: str
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def HmsEndpointServiceId(self):
        """HMS终端节点服务
        :rtype: str
        """
        return self._HmsEndpointServiceId

    @HmsEndpointServiceId.setter
    def HmsEndpointServiceId(self, HmsEndpointServiceId):
        self._HmsEndpointServiceId = HmsEndpointServiceId


    def _deserialize(self, params):
        self._EndpointServiceId = params.get("EndpointServiceId")
        self._MetaStoreUrl = params.get("MetaStoreUrl")
        if params.get("NetWork") is not None:
            self._NetWork = NetWork()
            self._NetWork._deserialize(params.get("NetWork"))
        self._HiveVersion = params.get("HiveVersion")
        self._Location = params.get("Location")
        self._HmsEndpointServiceId = params.get("HmsEndpointServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TccConnectionConfig(AbstractModel):
    """Tcc数据目录连接信息

    """

    def __init__(self):
        r"""
        :param _TccHive: Tcc数据目录连接配置
        :type TccHive: :class:`tencentcloud.tccatalog.v20241024.models.TccConnection`
        """
        self._TccHive = None

    @property
    def TccHive(self):
        """Tcc数据目录连接配置
        :rtype: :class:`tencentcloud.tccatalog.v20241024.models.TccConnection`
        """
        return self._TccHive

    @TccHive.setter
    def TccHive(self, TccHive):
        self._TccHive = TccHive


    def _deserialize(self, params):
        if params.get("TccHive") is not None:
            self._TccHive = TccConnection()
            self._TccHive._deserialize(params.get("TccHive"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        