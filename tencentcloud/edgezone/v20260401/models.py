# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class ApplyPublicIpsRequest(AbstractModel):
    r"""ApplyPublicIps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInstanceId: 公网实例 ID（路由发布模式必须为 STATIC ）
        :type NetworkInstanceId: str
        :param _Count: 申请Ip数量，最小为 1
        :type Count: int
        :param _Type: 申请的Ip类型，枚举值：ipv4、ipv6
        :type Type: str
        """
        self._NetworkInstanceId = None
        self._Count = None
        self._Type = None

    @property
    def NetworkInstanceId(self):
        r"""公网实例 ID（路由发布模式必须为 STATIC ）
        :rtype: str
        """
        return self._NetworkInstanceId

    @NetworkInstanceId.setter
    def NetworkInstanceId(self, NetworkInstanceId):
        self._NetworkInstanceId = NetworkInstanceId

    @property
    def Count(self):
        r"""申请Ip数量，最小为 1
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Type(self):
        r"""申请的Ip类型，枚举值：ipv4、ipv6
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._NetworkInstanceId = params.get("NetworkInstanceId")
        self._Count = params.get("Count")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyPublicIpsResponse(AbstractModel):
    r"""ApplyPublicIps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IpList: 分配的公网 IP 地址列表
        :type IpList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IpList = None
        self._RequestId = None

    @property
    def IpList(self):
        r"""分配的公网 IP 地址列表
        :rtype: list of str
        """
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IpList = params.get("IpList")
        self._RequestId = params.get("RequestId")


class CreateEdgeNodeServiceRequest(AbstractModel):
    r"""CreateEdgeNodeService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区代码，如 ap-guangzhou-1。
        :type Zone: str
        """
        self._Zone = None

    @property
    def Zone(self):
        r"""可用区代码，如 ap-guangzhou-1。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeNodeServiceResponse(AbstractModel):
    r"""CreateEdgeNodeService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateInstancesRequest(AbstractModel):
    r"""CreateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: <p>可用区代码，如 ap-guangzhou-1。</p>
        :type Zone: str
        :param _InstanceType: <p>机型规格，如 BMS5.MEDIUM8。</p>
        :type InstanceType: str
        :param _PrivateNetworkId: <p>内网网络实例ID，格式如 net-xxx。</p>
        :type PrivateNetworkId: str
        :param _PublicNetworkId: <p>公网网络实例ID，格式如 net-xxx。</p>
        :type PublicNetworkId: str
        :param _InstanceName: <p>实例名称。</p>
        :type InstanceName: str
        :param _ImageId: <p>镜像ID，如 img-centos-7.9。</p>
        :type ImageId: str
        :param _InstanceCount: <p>创建数量，默认1，最大50。</p>
        :type InstanceCount: int
        :param _Password: <p>登录密码，与SSHKey二选一</p>
        :type Password: str
        :param _SSHKey: <p>SSH密钥公钥字符串，与Password二选一</p>
        :type SSHKey: str
        :param _VersionNumber: <p>镜像版本号，仅公共镜像有版本概念。</p>
        :type VersionNumber: str
        :param _EnableIpv6: <p>是否启用公网IPv6，默认false。启用后系统会在分配IPv4后额外分配一个IPv6地址。</p>
        :type EnableIpv6: bool
        """
        self._Zone = None
        self._InstanceType = None
        self._PrivateNetworkId = None
        self._PublicNetworkId = None
        self._InstanceName = None
        self._ImageId = None
        self._InstanceCount = None
        self._Password = None
        self._SSHKey = None
        self._VersionNumber = None
        self._EnableIpv6 = None

    @property
    def Zone(self):
        r"""<p>可用区代码，如 ap-guangzhou-1。</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        r"""<p>机型规格，如 BMS5.MEDIUM8。</p>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def PrivateNetworkId(self):
        r"""<p>内网网络实例ID，格式如 net-xxx。</p>
        :rtype: str
        """
        return self._PrivateNetworkId

    @PrivateNetworkId.setter
    def PrivateNetworkId(self, PrivateNetworkId):
        self._PrivateNetworkId = PrivateNetworkId

    @property
    def PublicNetworkId(self):
        r"""<p>公网网络实例ID，格式如 net-xxx。</p>
        :rtype: str
        """
        return self._PublicNetworkId

    @PublicNetworkId.setter
    def PublicNetworkId(self, PublicNetworkId):
        self._PublicNetworkId = PublicNetworkId

    @property
    def InstanceName(self):
        r"""<p>实例名称。</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ImageId(self):
        r"""<p>镜像ID，如 img-centos-7.9。</p>
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def InstanceCount(self):
        r"""<p>创建数量，默认1，最大50。</p>
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def Password(self):
        r"""<p>登录密码，与SSHKey二选一</p>
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def SSHKey(self):
        r"""<p>SSH密钥公钥字符串，与Password二选一</p>
        :rtype: str
        """
        return self._SSHKey

    @SSHKey.setter
    def SSHKey(self, SSHKey):
        self._SSHKey = SSHKey

    @property
    def VersionNumber(self):
        warnings.warn("parameter `VersionNumber` is deprecated", DeprecationWarning) 

        r"""<p>镜像版本号，仅公共镜像有版本概念。</p>
        :rtype: str
        """
        return self._VersionNumber

    @VersionNumber.setter
    def VersionNumber(self, VersionNumber):
        warnings.warn("parameter `VersionNumber` is deprecated", DeprecationWarning) 

        self._VersionNumber = VersionNumber

    @property
    def EnableIpv6(self):
        warnings.warn("parameter `EnableIpv6` is deprecated", DeprecationWarning) 

        r"""<p>是否启用公网IPv6，默认false。启用后系统会在分配IPv4后额外分配一个IPv6地址。</p>
        :rtype: bool
        """
        return self._EnableIpv6

    @EnableIpv6.setter
    def EnableIpv6(self, EnableIpv6):
        warnings.warn("parameter `EnableIpv6` is deprecated", DeprecationWarning) 

        self._EnableIpv6 = EnableIpv6


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceType = params.get("InstanceType")
        self._PrivateNetworkId = params.get("PrivateNetworkId")
        self._PublicNetworkId = params.get("PublicNetworkId")
        self._InstanceName = params.get("InstanceName")
        self._ImageId = params.get("ImageId")
        self._InstanceCount = params.get("InstanceCount")
        self._Password = params.get("Password")
        self._SSHKey = params.get("SSHKey")
        self._VersionNumber = params.get("VersionNumber")
        self._EnableIpv6 = params.get("EnableIpv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancesResponse(AbstractModel):
    r"""CreateInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: <p>创建成功的实例ID列表。</p>
        :type InstanceIdSet: list of str
        :param _FailedCount: <p>创建失败的实例个数。仅部分失败时返回，全部成功时不返回该字段。</p>
        :type FailedCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceIdSet = None
        self._FailedCount = None
        self._RequestId = None

    @property
    def InstanceIdSet(self):
        r"""<p>创建成功的实例ID列表。</p>
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def FailedCount(self):
        r"""<p>创建失败的实例个数。仅部分失败时返回，全部成功时不返回该字段。</p>
        :rtype: int
        """
        return self._FailedCount

    @FailedCount.setter
    def FailedCount(self, FailedCount):
        self._FailedCount = FailedCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._FailedCount = params.get("FailedCount")
        self._RequestId = params.get("RequestId")


class CreatePrivateNetworkInstanceRequest(AbstractModel):
    r"""CreatePrivateNetworkInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInstanceName: 新实例名称
        :type NetworkInstanceName: str
        :param _ZoneId: 可用区ID
        :type ZoneId: str
        :param _Network: 网络地址（host 位必须全为 0），必须落在以下 RFC 1918 私有范围之一：`10.0.0.0/8`、`172.16.0.0/12`、`192.168.0.0/16`
        :type Network: str
        :param _Mask: 掩码位数，上限统一为 `28`，下限随所属私有段而定：`10.0.0.0/8` 允许 `8~28`，`172.16.0.0/12` 允许 `12~28`，`192.168.0.0/16` 允许 `16~28`；需与 Network 共同构成合法网络地址（host 位全为 0）
        :type Mask: int
        """
        self._NetworkInstanceName = None
        self._ZoneId = None
        self._Network = None
        self._Mask = None

    @property
    def NetworkInstanceName(self):
        r"""新实例名称
        :rtype: str
        """
        return self._NetworkInstanceName

    @NetworkInstanceName.setter
    def NetworkInstanceName(self, NetworkInstanceName):
        self._NetworkInstanceName = NetworkInstanceName

    @property
    def ZoneId(self):
        r"""可用区ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Network(self):
        r"""网络地址（host 位必须全为 0），必须落在以下 RFC 1918 私有范围之一：`10.0.0.0/8`、`172.16.0.0/12`、`192.168.0.0/16`
        :rtype: str
        """
        return self._Network

    @Network.setter
    def Network(self, Network):
        self._Network = Network

    @property
    def Mask(self):
        r"""掩码位数，上限统一为 `28`，下限随所属私有段而定：`10.0.0.0/8` 允许 `8~28`，`172.16.0.0/12` 允许 `12~28`，`192.168.0.0/16` 允许 `16~28`；需与 Network 共同构成合法网络地址（host 位全为 0）
        :rtype: int
        """
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask


    def _deserialize(self, params):
        self._NetworkInstanceName = params.get("NetworkInstanceName")
        self._ZoneId = params.get("ZoneId")
        self._Network = params.get("Network")
        self._Mask = params.get("Mask")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateNetworkInstanceResponse(AbstractModel):
    r"""CreatePrivateNetworkInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInstanceId: 私网实例ID
        :type NetworkInstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NetworkInstanceId = None
        self._RequestId = None

    @property
    def NetworkInstanceId(self):
        r"""私网实例ID
        :rtype: str
        """
        return self._NetworkInstanceId

    @NetworkInstanceId.setter
    def NetworkInstanceId(self, NetworkInstanceId):
        self._NetworkInstanceId = NetworkInstanceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NetworkInstanceId = params.get("NetworkInstanceId")
        self._RequestId = params.get("RequestId")


class CreatePublicNetworkInstanceRequest(AbstractModel):
    r"""CreatePublicNetworkInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: <p>可用区</p>
        :type ZoneId: str
        :param _NetworkInstanceName: <p>公网实例名称</p>
        :type NetworkInstanceName: str
        :param _Line: <p>网络线路</p>
        :type Line: str
        :param _RouteMode: <p>路由模式</p>
        :type RouteMode: str
        :param _Bandwidth: <p>公网带宽（Mbps）</p>
        :type Bandwidth: int
        :param _BgpAsNumber: <p>BGP AS号</p>
        :type BgpAsNumber: int
        :param _BgpPassword: <p>BGP认证密码</p>
        :type BgpPassword: str
        :param _InstanceType: <p>公网实例类型</p><p>枚举值：</p><ul><li>standard： 标准型(默认)</li><li>custom： 自定义型(暂不支持创建)</li></ul>
        :type InstanceType: str
        """
        self._ZoneId = None
        self._NetworkInstanceName = None
        self._Line = None
        self._RouteMode = None
        self._Bandwidth = None
        self._BgpAsNumber = None
        self._BgpPassword = None
        self._InstanceType = None

    @property
    def ZoneId(self):
        r"""<p>可用区</p>
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def NetworkInstanceName(self):
        r"""<p>公网实例名称</p>
        :rtype: str
        """
        return self._NetworkInstanceName

    @NetworkInstanceName.setter
    def NetworkInstanceName(self, NetworkInstanceName):
        self._NetworkInstanceName = NetworkInstanceName

    @property
    def Line(self):
        r"""<p>网络线路</p>
        :rtype: str
        """
        return self._Line

    @Line.setter
    def Line(self, Line):
        self._Line = Line

    @property
    def RouteMode(self):
        r"""<p>路由模式</p>
        :rtype: str
        """
        return self._RouteMode

    @RouteMode.setter
    def RouteMode(self, RouteMode):
        self._RouteMode = RouteMode

    @property
    def Bandwidth(self):
        r"""<p>公网带宽（Mbps）</p>
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def BgpAsNumber(self):
        r"""<p>BGP AS号</p>
        :rtype: int
        """
        return self._BgpAsNumber

    @BgpAsNumber.setter
    def BgpAsNumber(self, BgpAsNumber):
        self._BgpAsNumber = BgpAsNumber

    @property
    def BgpPassword(self):
        r"""<p>BGP认证密码</p>
        :rtype: str
        """
        return self._BgpPassword

    @BgpPassword.setter
    def BgpPassword(self, BgpPassword):
        self._BgpPassword = BgpPassword

    @property
    def InstanceType(self):
        r"""<p>公网实例类型</p><p>枚举值：</p><ul><li>standard： 标准型(默认)</li><li>custom： 自定义型(暂不支持创建)</li></ul>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._NetworkInstanceName = params.get("NetworkInstanceName")
        self._Line = params.get("Line")
        self._RouteMode = params.get("RouteMode")
        self._Bandwidth = params.get("Bandwidth")
        self._BgpAsNumber = params.get("BgpAsNumber")
        self._BgpPassword = params.get("BgpPassword")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePublicNetworkInstanceResponse(AbstractModel):
    r"""CreatePublicNetworkInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInstanceId: <p>公网实例 ID</p>
        :type NetworkInstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NetworkInstanceId = None
        self._RequestId = None

    @property
    def NetworkInstanceId(self):
        r"""<p>公网实例 ID</p>
        :rtype: str
        """
        return self._NetworkInstanceId

    @NetworkInstanceId.setter
    def NetworkInstanceId(self, NetworkInstanceId):
        self._NetworkInstanceId = NetworkInstanceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NetworkInstanceId = params.get("NetworkInstanceId")
        self._RequestId = params.get("RequestId")


class DeletePrivateNetworkInstanceRequest(AbstractModel):
    r"""DeletePrivateNetworkInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInstanceId: 私网实例Id
        :type NetworkInstanceId: str
        """
        self._NetworkInstanceId = None

    @property
    def NetworkInstanceId(self):
        r"""私网实例Id
        :rtype: str
        """
        return self._NetworkInstanceId

    @NetworkInstanceId.setter
    def NetworkInstanceId(self, NetworkInstanceId):
        self._NetworkInstanceId = NetworkInstanceId


    def _deserialize(self, params):
        self._NetworkInstanceId = params.get("NetworkInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateNetworkInstanceResponse(AbstractModel):
    r"""DeletePrivateNetworkInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeletePublicNetworkInstanceRequest(AbstractModel):
    r"""DeletePublicNetworkInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInstanceId: 公网实例 ID
        :type NetworkInstanceId: str
        """
        self._NetworkInstanceId = None

    @property
    def NetworkInstanceId(self):
        r"""公网实例 ID
        :rtype: str
        """
        return self._NetworkInstanceId

    @NetworkInstanceId.setter
    def NetworkInstanceId(self, NetworkInstanceId):
        self._NetworkInstanceId = NetworkInstanceId


    def _deserialize(self, params):
        self._NetworkInstanceId = params.get("NetworkInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePublicNetworkInstanceResponse(AbstractModel):
    r"""DeletePublicNetworkInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeInstanceTypesRequest(AbstractModel):
    r"""DescribeInstanceTypes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区代码，如 ap-guangzhou-1；不传则返回账号下所有可用区的机型。
        :type Zone: str
        :param _Offset: 分页偏移量,默认0
        :type Offset: int
        :param _Limit: 分页大小，默认20，最大100
        :type Limit: int
        """
        self._Zone = None
        self._Offset = None
        self._Limit = None

    @property
    def Zone(self):
        r"""可用区代码，如 ap-guangzhou-1；不传则返回账号下所有可用区的机型。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Offset(self):
        r"""分页偏移量,默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页大小，默认20，最大100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceTypesResponse(AbstractModel):
    r"""DescribeInstanceTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceTypeQuotaSet: 机型配额列表。
        :type InstanceTypeQuotaSet: list of InstanceTypeQuota
        :param _TotalCount: 返回记录数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceTypeQuotaSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceTypeQuotaSet(self):
        r"""机型配额列表。
        :rtype: list of InstanceTypeQuota
        """
        return self._InstanceTypeQuotaSet

    @InstanceTypeQuotaSet.setter
    def InstanceTypeQuotaSet(self, InstanceTypeQuotaSet):
        self._InstanceTypeQuotaSet = InstanceTypeQuotaSet

    @property
    def TotalCount(self):
        r"""返回记录数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceTypeQuotaSet") is not None:
            self._InstanceTypeQuotaSet = []
            for item in params.get("InstanceTypeQuotaSet"):
                obj = InstanceTypeQuota()
                obj._deserialize(item)
                self._InstanceTypeQuotaSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    r"""DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: <p>实例ID列表，用于按实例ID筛选</p>
        :type InstanceIds: list of str
        :param _InstanceName: <p>实例名称，支持模糊匹配</p>
        :type InstanceName: str
        :param _Zone: <p>可用区代码，用于筛选指定可用区的实例</p>
        :type Zone: str
        :param _InstanceStatus: <p>实例状态列表，用于按状态筛选实例。可选值：allocating、running、isolating、isolated、terminating、error</p>
        :type InstanceStatus: list of str
        :param _PublicNetworkId: <p>公网网络ID</p>
        :type PublicNetworkId: str
        :param _PrivateNetworkId: <p>私有网络ID</p>
        :type PrivateNetworkId: str
        :param _PublicIps: <p>公网IPv4地址列表，用于按公网IP筛选实例</p>
        :type PublicIps: list of str
        :param _Offset: <p>偏移量，默认0</p>
        :type Offset: int
        :param _Limit: <p>返回数量，默认20，最大100</p>
        :type Limit: int
        """
        self._InstanceIds = None
        self._InstanceName = None
        self._Zone = None
        self._InstanceStatus = None
        self._PublicNetworkId = None
        self._PrivateNetworkId = None
        self._PublicIps = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        r"""<p>实例ID列表，用于按实例ID筛选</p>
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceName(self):
        r"""<p>实例名称，支持模糊匹配</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Zone(self):
        r"""<p>可用区代码，用于筛选指定可用区的实例</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceStatus(self):
        r"""<p>实例状态列表，用于按状态筛选实例。可选值：allocating、running、isolating、isolated、terminating、error</p>
        :rtype: list of str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def PublicNetworkId(self):
        r"""<p>公网网络ID</p>
        :rtype: str
        """
        return self._PublicNetworkId

    @PublicNetworkId.setter
    def PublicNetworkId(self, PublicNetworkId):
        self._PublicNetworkId = PublicNetworkId

    @property
    def PrivateNetworkId(self):
        r"""<p>私有网络ID</p>
        :rtype: str
        """
        return self._PrivateNetworkId

    @PrivateNetworkId.setter
    def PrivateNetworkId(self, PrivateNetworkId):
        self._PrivateNetworkId = PrivateNetworkId

    @property
    def PublicIps(self):
        r"""<p>公网IPv4地址列表，用于按公网IP筛选实例</p>
        :rtype: list of str
        """
        return self._PublicIps

    @PublicIps.setter
    def PublicIps(self, PublicIps):
        self._PublicIps = PublicIps

    @property
    def Offset(self):
        r"""<p>偏移量，默认0</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>返回数量，默认20，最大100</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceName = params.get("InstanceName")
        self._Zone = params.get("Zone")
        self._InstanceStatus = params.get("InstanceStatus")
        self._PublicNetworkId = params.get("PublicNetworkId")
        self._PrivateNetworkId = params.get("PrivateNetworkId")
        self._PublicIps = params.get("PublicIps")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    r"""DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceSet: <p>实例详细信息列表</p>
        :type InstanceSet: list of Instance
        :param _TotalCount: <p>符合条件的实例数量</p>
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceSet(self):
        r"""<p>实例详细信息列表</p>
        :rtype: list of Instance
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def TotalCount(self):
        r"""<p>符合条件的实例数量</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePrivateNetworkInstancesRequest(AbstractModel):
    r"""DescribePrivateNetworkInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInstanceId: 私网实例Id
        :type NetworkInstanceId: str
        :param _NetworkInstanceName: 新实例名称
        :type NetworkInstanceName: str
        :param _ZoneId: 可用区ID
        :type ZoneId: str
        :param _Offset: 分页偏移量，默认0
        :type Offset: int
        :param _Limit: 每页数量，默认 20，最大 100
        :type Limit: int
        """
        self._NetworkInstanceId = None
        self._NetworkInstanceName = None
        self._ZoneId = None
        self._Offset = None
        self._Limit = None

    @property
    def NetworkInstanceId(self):
        r"""私网实例Id
        :rtype: str
        """
        return self._NetworkInstanceId

    @NetworkInstanceId.setter
    def NetworkInstanceId(self, NetworkInstanceId):
        self._NetworkInstanceId = NetworkInstanceId

    @property
    def NetworkInstanceName(self):
        r"""新实例名称
        :rtype: str
        """
        return self._NetworkInstanceName

    @NetworkInstanceName.setter
    def NetworkInstanceName(self, NetworkInstanceName):
        self._NetworkInstanceName = NetworkInstanceName

    @property
    def ZoneId(self):
        r"""可用区ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Offset(self):
        r"""分页偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页数量，默认 20，最大 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._NetworkInstanceId = params.get("NetworkInstanceId")
        self._NetworkInstanceName = params.get("NetworkInstanceName")
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateNetworkInstancesResponse(AbstractModel):
    r"""DescribePrivateNetworkInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 私网实例总数
        :type TotalCount: int
        :param _PrivateNetworkInstanceSet: 私网实例集合
        :type PrivateNetworkInstanceSet: list of PrivateNetworkInstanceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._PrivateNetworkInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""私网实例总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PrivateNetworkInstanceSet(self):
        r"""私网实例集合
        :rtype: list of PrivateNetworkInstanceInfo
        """
        return self._PrivateNetworkInstanceSet

    @PrivateNetworkInstanceSet.setter
    def PrivateNetworkInstanceSet(self, PrivateNetworkInstanceSet):
        self._PrivateNetworkInstanceSet = PrivateNetworkInstanceSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("PrivateNetworkInstanceSet") is not None:
            self._PrivateNetworkInstanceSet = []
            for item in params.get("PrivateNetworkInstanceSet"):
                obj = PrivateNetworkInstanceInfo()
                obj._deserialize(item)
                self._PrivateNetworkInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePublicIpsRequest(AbstractModel):
    r"""DescribePublicIps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInstanceId: 按公网实例 ID 过滤（子串匹配，多个值取并集）
        :type NetworkInstanceId: list of str
        :param _ZoneId: 按可用区/机房过滤
        :type ZoneId: str
        :param _Ip: 按 IP 过滤（子串匹配，多个值取并集）
        :type Ip: list of str
        :param _State: 按状态过滤，可选值：`InUse`、`Unbound`（多个值取并集）
        :type State: list of str
        :param _Type: 按 IP 版本过滤，可选值：`Ipv4`、`Ipv6`（多个值取并集）
        :type Type: list of str
        :param _OrderByCreateTime: 按创建时间排序，可选值：`asc`、`desc`（默认 `desc`）
        :type OrderByCreateTime: str
        :param _OrderByUpdateTime: 按更新时间排序，可选值：`asc`、`desc`（优先级高于创建时间排序）
        :type OrderByUpdateTime: str
        :param _Offset: 分页偏移量，默认 0
        :type Offset: int
        :param _Limit: 每页数量，默认 20，最大 100
        :type Limit: int
        """
        self._NetworkInstanceId = None
        self._ZoneId = None
        self._Ip = None
        self._State = None
        self._Type = None
        self._OrderByCreateTime = None
        self._OrderByUpdateTime = None
        self._Offset = None
        self._Limit = None

    @property
    def NetworkInstanceId(self):
        r"""按公网实例 ID 过滤（子串匹配，多个值取并集）
        :rtype: list of str
        """
        return self._NetworkInstanceId

    @NetworkInstanceId.setter
    def NetworkInstanceId(self, NetworkInstanceId):
        self._NetworkInstanceId = NetworkInstanceId

    @property
    def ZoneId(self):
        r"""按可用区/机房过滤
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Ip(self):
        r"""按 IP 过滤（子串匹配，多个值取并集）
        :rtype: list of str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def State(self):
        r"""按状态过滤，可选值：`InUse`、`Unbound`（多个值取并集）
        :rtype: list of str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Type(self):
        r"""按 IP 版本过滤，可选值：`Ipv4`、`Ipv6`（多个值取并集）
        :rtype: list of str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def OrderByCreateTime(self):
        r"""按创建时间排序，可选值：`asc`、`desc`（默认 `desc`）
        :rtype: str
        """
        return self._OrderByCreateTime

    @OrderByCreateTime.setter
    def OrderByCreateTime(self, OrderByCreateTime):
        self._OrderByCreateTime = OrderByCreateTime

    @property
    def OrderByUpdateTime(self):
        r"""按更新时间排序，可选值：`asc`、`desc`（优先级高于创建时间排序）
        :rtype: str
        """
        return self._OrderByUpdateTime

    @OrderByUpdateTime.setter
    def OrderByUpdateTime(self, OrderByUpdateTime):
        self._OrderByUpdateTime = OrderByUpdateTime

    @property
    def Offset(self):
        r"""分页偏移量，默认 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页数量，默认 20，最大 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._NetworkInstanceId = params.get("NetworkInstanceId")
        self._ZoneId = params.get("ZoneId")
        self._Ip = params.get("Ip")
        self._State = params.get("State")
        self._Type = params.get("Type")
        self._OrderByCreateTime = params.get("OrderByCreateTime")
        self._OrderByUpdateTime = params.get("OrderByUpdateTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicIpsResponse(AbstractModel):
    r"""DescribePublicIps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 公网Ip总数
        :type TotalCount: int
        :param _IpInfoSet: 分配的公网 IP 地址列表
        :type IpInfoSet: list of IpInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._IpInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""公网Ip总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def IpInfoSet(self):
        r"""分配的公网 IP 地址列表
        :rtype: list of IpInfo
        """
        return self._IpInfoSet

    @IpInfoSet.setter
    def IpInfoSet(self, IpInfoSet):
        self._IpInfoSet = IpInfoSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("IpInfoSet") is not None:
            self._IpInfoSet = []
            for item in params.get("IpInfoSet"):
                obj = IpInfo()
                obj._deserialize(item)
                self._IpInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePublicNetworkInstancesRequest(AbstractModel):
    r"""DescribePublicNetworkInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInstanceId: 公网实例ID
        :type NetworkInstanceId: str
        :param _NetworkInstanceName: 公网实例名称
        :type NetworkInstanceName: str
        :param _ZoneId: 可用区Id
        :type ZoneId: str
        :param _Offset: 分页偏移量，默认 0
        :type Offset: int
        :param _Limit: 每页数量，默认 20，最大 100
        :type Limit: int
        """
        self._NetworkInstanceId = None
        self._NetworkInstanceName = None
        self._ZoneId = None
        self._Offset = None
        self._Limit = None

    @property
    def NetworkInstanceId(self):
        r"""公网实例ID
        :rtype: str
        """
        return self._NetworkInstanceId

    @NetworkInstanceId.setter
    def NetworkInstanceId(self, NetworkInstanceId):
        self._NetworkInstanceId = NetworkInstanceId

    @property
    def NetworkInstanceName(self):
        r"""公网实例名称
        :rtype: str
        """
        return self._NetworkInstanceName

    @NetworkInstanceName.setter
    def NetworkInstanceName(self, NetworkInstanceName):
        self._NetworkInstanceName = NetworkInstanceName

    @property
    def ZoneId(self):
        r"""可用区Id
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Offset(self):
        r"""分页偏移量，默认 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""每页数量，默认 20，最大 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._NetworkInstanceId = params.get("NetworkInstanceId")
        self._NetworkInstanceName = params.get("NetworkInstanceName")
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicNetworkInstancesResponse(AbstractModel):
    r"""DescribePublicNetworkInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 公网实例总数
        :type TotalCount: int
        :param _PublicNetworkInstanceSet: 公网实例集合
        :type PublicNetworkInstanceSet: list of PublicNetworkInstanceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._PublicNetworkInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""公网实例总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PublicNetworkInstanceSet(self):
        r"""公网实例集合
        :rtype: list of PublicNetworkInstanceInfo
        """
        return self._PublicNetworkInstanceSet

    @PublicNetworkInstanceSet.setter
    def PublicNetworkInstanceSet(self, PublicNetworkInstanceSet):
        self._PublicNetworkInstanceSet = PublicNetworkInstanceSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("PublicNetworkInstanceSet") is not None:
            self._PublicNetworkInstanceSet = []
            for item in params.get("PublicNetworkInstanceSet"):
                obj = PublicNetworkInstanceInfo()
                obj._deserialize(item)
                self._PublicNetworkInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZoneDataRequest(AbstractModel):
    r"""DescribeZoneData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: 区id
        :type Zone: str
        :param _MetricName: 指标名(inbw:入带宽，outbw:出带宽)
        :type MetricName: str
        :param _StartTime: 开始时间（UTC时间:0时区）
        :type StartTime: str
        :param _EndTime: 结束时间（UTC时间:0时区）,最多查询2天时间
        :type EndTime: str
        """
        self._Zone = None
        self._MetricName = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Zone(self):
        r"""区id
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def MetricName(self):
        r"""指标名(inbw:入带宽，outbw:出带宽)
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def StartTime(self):
        r"""开始时间（UTC时间:0时区）
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间（UTC时间:0时区）,最多查询2天时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._MetricName = params.get("MetricName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneDataResponse(AbstractModel):
    r"""DescribeZoneData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 统计数据,指标inbw|outbw单位为Mbps
        :type Data: list of SwitchData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""统计数据,指标inbw|outbw单位为Mbps
        :rtype: list of SwitchData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SwitchData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    r"""DescribeZones请求参数结构体

    """


class DescribeZonesResponse(AbstractModel):
    r"""DescribeZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneSet: <p>所有地域的可用区列表。</p>
        :type ZoneSet: list of ZoneInfo
        :param _TotalCount: <p>可用区总数量。</p>
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ZoneSet(self):
        r"""<p>所有地域的可用区列表。</p>
        :rtype: list of ZoneInfo
        """
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

    @property
    def TotalCount(self):
        r"""<p>可用区总数量。</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ZoneSet") is not None:
            self._ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self._ZoneSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class FailedInstance(AbstractModel):
    r"""操作失败的实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _ErrorCode: 错误码。
        :type ErrorCode: str
        :param _ErrorMessage: 错误信息。
        :type ErrorMessage: str
        """
        self._InstanceId = None
        self._ErrorCode = None
        self._ErrorMessage = None

    @property
    def InstanceId(self):
        r"""实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorCode(self):
        r"""错误码。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""错误信息。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    r"""描述物理机实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        :param _InstanceName: <p>实例名称</p>
        :type InstanceName: str
        :param _MachineId: <p>绑定的物理机ID</p>
        :type MachineId: str
        :param _InstanceType: <p>机型规格</p>
        :type InstanceType: str
        :param _Zone: <p>可用区代码</p>
        :type Zone: str
        :param _ImageId: <p>镜像ID</p>
        :type ImageId: str
        :param _VersionNumber: <p>镜像版本号</p>
        :type VersionNumber: str
        :param _InstanceStatus: <p>实例状态，可选值：allocating、running、isolating、isolated、terminating、error</p>
        :type InstanceStatus: str
        :param _OperateStatus: <p>操作状态，可选值：normal、starting、stopping、stopped、rebooting</p>
        :type OperateStatus: str
        :param _PrivateNetworkId: <p>私有网络ID</p>
        :type PrivateNetworkId: str
        :param _PrivateIp: <p>私有IPv4地址</p>
        :type PrivateIp: str
        :param _PrivateIpV6: <p>私有IPv6地址</p>
        :type PrivateIpV6: str
        :param _PublicNetworkId: <p>公网网络ID</p>
        :type PublicNetworkId: str
        :param _PublicIp: <p>公网IPv4地址</p>
        :type PublicIp: str
        :param _PublicIpV6: <p>公网IPv6地址</p>
        :type PublicIpV6: str
        :param _FileSystemType: <p>文件系统类型</p>
        :type FileSystemType: str
        :param _CreatedTime: <p>创建时间。按照ISO8601标准表示，并且使用UTC时间。格式为：YYYY-MM-DDThh:mm:ssZ。</p>
        :type CreatedTime: str
        :param _InstanceFamily: <p>机型族标识</p>
        :type InstanceFamily: str
        :param _InstanceFamilyName: <p>机型族名称</p>
        :type InstanceFamilyName: str
        :param _CpuType: <p>CPU 型号</p>
        :type CpuType: str
        :param _Cpu: <p>CPU 核数</p>
        :type Cpu: int
        :param _Memory: <p>内存大小</p>
        :type Memory: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._MachineId = None
        self._InstanceType = None
        self._Zone = None
        self._ImageId = None
        self._VersionNumber = None
        self._InstanceStatus = None
        self._OperateStatus = None
        self._PrivateNetworkId = None
        self._PrivateIp = None
        self._PrivateIpV6 = None
        self._PublicNetworkId = None
        self._PublicIp = None
        self._PublicIpV6 = None
        self._FileSystemType = None
        self._CreatedTime = None
        self._InstanceFamily = None
        self._InstanceFamilyName = None
        self._CpuType = None
        self._Cpu = None
        self._Memory = None

    @property
    def InstanceId(self):
        r"""<p>实例ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""<p>实例名称</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def MachineId(self):
        r"""<p>绑定的物理机ID</p>
        :rtype: str
        """
        return self._MachineId

    @MachineId.setter
    def MachineId(self, MachineId):
        self._MachineId = MachineId

    @property
    def InstanceType(self):
        r"""<p>机型规格</p>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Zone(self):
        r"""<p>可用区代码</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ImageId(self):
        r"""<p>镜像ID</p>
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def VersionNumber(self):
        warnings.warn("parameter `VersionNumber` is deprecated", DeprecationWarning) 

        r"""<p>镜像版本号</p>
        :rtype: str
        """
        return self._VersionNumber

    @VersionNumber.setter
    def VersionNumber(self, VersionNumber):
        warnings.warn("parameter `VersionNumber` is deprecated", DeprecationWarning) 

        self._VersionNumber = VersionNumber

    @property
    def InstanceStatus(self):
        r"""<p>实例状态，可选值：allocating、running、isolating、isolated、terminating、error</p>
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def OperateStatus(self):
        r"""<p>操作状态，可选值：normal、starting、stopping、stopped、rebooting</p>
        :rtype: str
        """
        return self._OperateStatus

    @OperateStatus.setter
    def OperateStatus(self, OperateStatus):
        self._OperateStatus = OperateStatus

    @property
    def PrivateNetworkId(self):
        r"""<p>私有网络ID</p>
        :rtype: str
        """
        return self._PrivateNetworkId

    @PrivateNetworkId.setter
    def PrivateNetworkId(self, PrivateNetworkId):
        self._PrivateNetworkId = PrivateNetworkId

    @property
    def PrivateIp(self):
        r"""<p>私有IPv4地址</p>
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PrivateIpV6(self):
        r"""<p>私有IPv6地址</p>
        :rtype: str
        """
        return self._PrivateIpV6

    @PrivateIpV6.setter
    def PrivateIpV6(self, PrivateIpV6):
        self._PrivateIpV6 = PrivateIpV6

    @property
    def PublicNetworkId(self):
        r"""<p>公网网络ID</p>
        :rtype: str
        """
        return self._PublicNetworkId

    @PublicNetworkId.setter
    def PublicNetworkId(self, PublicNetworkId):
        self._PublicNetworkId = PublicNetworkId

    @property
    def PublicIp(self):
        r"""<p>公网IPv4地址</p>
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PublicIpV6(self):
        r"""<p>公网IPv6地址</p>
        :rtype: str
        """
        return self._PublicIpV6

    @PublicIpV6.setter
    def PublicIpV6(self, PublicIpV6):
        self._PublicIpV6 = PublicIpV6

    @property
    def FileSystemType(self):
        r"""<p>文件系统类型</p>
        :rtype: str
        """
        return self._FileSystemType

    @FileSystemType.setter
    def FileSystemType(self, FileSystemType):
        self._FileSystemType = FileSystemType

    @property
    def CreatedTime(self):
        r"""<p>创建时间。按照ISO8601标准表示，并且使用UTC时间。格式为：YYYY-MM-DDThh:mm:ssZ。</p>
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def InstanceFamily(self):
        r"""<p>机型族标识</p>
        :rtype: str
        """
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def InstanceFamilyName(self):
        r"""<p>机型族名称</p>
        :rtype: str
        """
        return self._InstanceFamilyName

    @InstanceFamilyName.setter
    def InstanceFamilyName(self, InstanceFamilyName):
        self._InstanceFamilyName = InstanceFamilyName

    @property
    def CpuType(self):
        r"""<p>CPU 型号</p>
        :rtype: str
        """
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def Cpu(self):
        r"""<p>CPU 核数</p>
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        r"""<p>内存大小</p>
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._MachineId = params.get("MachineId")
        self._InstanceType = params.get("InstanceType")
        self._Zone = params.get("Zone")
        self._ImageId = params.get("ImageId")
        self._VersionNumber = params.get("VersionNumber")
        self._InstanceStatus = params.get("InstanceStatus")
        self._OperateStatus = params.get("OperateStatus")
        self._PrivateNetworkId = params.get("PrivateNetworkId")
        self._PrivateIp = params.get("PrivateIp")
        self._PrivateIpV6 = params.get("PrivateIpV6")
        self._PublicNetworkId = params.get("PublicNetworkId")
        self._PublicIp = params.get("PublicIp")
        self._PublicIpV6 = params.get("PublicIpV6")
        self._FileSystemType = params.get("FileSystemType")
        self._CreatedTime = params.get("CreatedTime")
        self._InstanceFamily = params.get("InstanceFamily")
        self._InstanceFamilyName = params.get("InstanceFamilyName")
        self._CpuType = params.get("CpuType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeQuota(AbstractModel):
    r"""账号在可用区下的机型配额信息，包含可用区、机型详情和配额数量。

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区代码。
        :type Zone: str
        :param _InstanceType: 机型规格。
        :type InstanceType: str
        :param _InstanceFamily: 机型家族。
        :type InstanceFamily: str
        :param _InstanceFamilyName: 机型族名称
        :type InstanceFamilyName: str
        :param _CpuCores: CPU核数。
        :type CpuCores: int
        :param _CpuType: CPU类型。
        :type CpuType: str
        :param _MemoryGb: 内存大小（GB）。
        :type MemoryGb: int
        :param _SystemDiskType: 系统盘类型。
        :type SystemDiskType: str
        :param _SystemDiskSize: 系统盘大小（GB）。
        :type SystemDiskSize: int
        :param _SystemDiskCount: 系统盘数量。
        :type SystemDiskCount: int
        :param _DataDiskType: 数据盘类型。
        :type DataDiskType: str
        :param _DataDiskSize: 数据盘大小（GB）。
        :type DataDiskSize: int
        :param _DataDiskCount: 数据盘数量。
        :type DataDiskCount: int
        :param _SecondaryDataDiskType: 第二组数据盘类型
        :type SecondaryDataDiskType: str
        :param _SecondaryDataDiskSize: 第二组数据盘大小(GB)
        :type SecondaryDataDiskSize: int
        :param _SecondaryDataDiskCount: 第二组数据盘数量
        :type SecondaryDataDiskCount: int
        :param _DiskType: 磁盘描述字符串（向后兼容）。
        :type DiskType: str
        :param _NetworkInterfaceType: 网络接口类型。
        :type NetworkInterfaceType: str
        :param _GpuType: GPU类型，无GPU时为空字符串。
        :type GpuType: str
        :param _Quota: 配额数量
        :type Quota: int
        """
        self._Zone = None
        self._InstanceType = None
        self._InstanceFamily = None
        self._InstanceFamilyName = None
        self._CpuCores = None
        self._CpuType = None
        self._MemoryGb = None
        self._SystemDiskType = None
        self._SystemDiskSize = None
        self._SystemDiskCount = None
        self._DataDiskType = None
        self._DataDiskSize = None
        self._DataDiskCount = None
        self._SecondaryDataDiskType = None
        self._SecondaryDataDiskSize = None
        self._SecondaryDataDiskCount = None
        self._DiskType = None
        self._NetworkInterfaceType = None
        self._GpuType = None
        self._Quota = None

    @property
    def Zone(self):
        r"""可用区代码。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        r"""机型规格。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceFamily(self):
        r"""机型家族。
        :rtype: str
        """
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def InstanceFamilyName(self):
        r"""机型族名称
        :rtype: str
        """
        return self._InstanceFamilyName

    @InstanceFamilyName.setter
    def InstanceFamilyName(self, InstanceFamilyName):
        self._InstanceFamilyName = InstanceFamilyName

    @property
    def CpuCores(self):
        r"""CPU核数。
        :rtype: int
        """
        return self._CpuCores

    @CpuCores.setter
    def CpuCores(self, CpuCores):
        self._CpuCores = CpuCores

    @property
    def CpuType(self):
        r"""CPU类型。
        :rtype: str
        """
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def MemoryGb(self):
        r"""内存大小（GB）。
        :rtype: int
        """
        return self._MemoryGb

    @MemoryGb.setter
    def MemoryGb(self, MemoryGb):
        self._MemoryGb = MemoryGb

    @property
    def SystemDiskType(self):
        r"""系统盘类型。
        :rtype: str
        """
        return self._SystemDiskType

    @SystemDiskType.setter
    def SystemDiskType(self, SystemDiskType):
        self._SystemDiskType = SystemDiskType

    @property
    def SystemDiskSize(self):
        r"""系统盘大小（GB）。
        :rtype: int
        """
        return self._SystemDiskSize

    @SystemDiskSize.setter
    def SystemDiskSize(self, SystemDiskSize):
        self._SystemDiskSize = SystemDiskSize

    @property
    def SystemDiskCount(self):
        r"""系统盘数量。
        :rtype: int
        """
        return self._SystemDiskCount

    @SystemDiskCount.setter
    def SystemDiskCount(self, SystemDiskCount):
        self._SystemDiskCount = SystemDiskCount

    @property
    def DataDiskType(self):
        r"""数据盘类型。
        :rtype: str
        """
        return self._DataDiskType

    @DataDiskType.setter
    def DataDiskType(self, DataDiskType):
        self._DataDiskType = DataDiskType

    @property
    def DataDiskSize(self):
        r"""数据盘大小（GB）。
        :rtype: int
        """
        return self._DataDiskSize

    @DataDiskSize.setter
    def DataDiskSize(self, DataDiskSize):
        self._DataDiskSize = DataDiskSize

    @property
    def DataDiskCount(self):
        r"""数据盘数量。
        :rtype: int
        """
        return self._DataDiskCount

    @DataDiskCount.setter
    def DataDiskCount(self, DataDiskCount):
        self._DataDiskCount = DataDiskCount

    @property
    def SecondaryDataDiskType(self):
        r"""第二组数据盘类型
        :rtype: str
        """
        return self._SecondaryDataDiskType

    @SecondaryDataDiskType.setter
    def SecondaryDataDiskType(self, SecondaryDataDiskType):
        self._SecondaryDataDiskType = SecondaryDataDiskType

    @property
    def SecondaryDataDiskSize(self):
        r"""第二组数据盘大小(GB)
        :rtype: int
        """
        return self._SecondaryDataDiskSize

    @SecondaryDataDiskSize.setter
    def SecondaryDataDiskSize(self, SecondaryDataDiskSize):
        self._SecondaryDataDiskSize = SecondaryDataDiskSize

    @property
    def SecondaryDataDiskCount(self):
        r"""第二组数据盘数量
        :rtype: int
        """
        return self._SecondaryDataDiskCount

    @SecondaryDataDiskCount.setter
    def SecondaryDataDiskCount(self, SecondaryDataDiskCount):
        self._SecondaryDataDiskCount = SecondaryDataDiskCount

    @property
    def DiskType(self):
        r"""磁盘描述字符串（向后兼容）。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def NetworkInterfaceType(self):
        r"""网络接口类型。
        :rtype: str
        """
        return self._NetworkInterfaceType

    @NetworkInterfaceType.setter
    def NetworkInterfaceType(self, NetworkInterfaceType):
        self._NetworkInterfaceType = NetworkInterfaceType

    @property
    def GpuType(self):
        r"""GPU类型，无GPU时为空字符串。
        :rtype: str
        """
        return self._GpuType

    @GpuType.setter
    def GpuType(self, GpuType):
        self._GpuType = GpuType

    @property
    def Quota(self):
        r"""配额数量
        :rtype: int
        """
        return self._Quota

    @Quota.setter
    def Quota(self, Quota):
        self._Quota = Quota


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceType = params.get("InstanceType")
        self._InstanceFamily = params.get("InstanceFamily")
        self._InstanceFamilyName = params.get("InstanceFamilyName")
        self._CpuCores = params.get("CpuCores")
        self._CpuType = params.get("CpuType")
        self._MemoryGb = params.get("MemoryGb")
        self._SystemDiskType = params.get("SystemDiskType")
        self._SystemDiskSize = params.get("SystemDiskSize")
        self._SystemDiskCount = params.get("SystemDiskCount")
        self._DataDiskType = params.get("DataDiskType")
        self._DataDiskSize = params.get("DataDiskSize")
        self._DataDiskCount = params.get("DataDiskCount")
        self._SecondaryDataDiskType = params.get("SecondaryDataDiskType")
        self._SecondaryDataDiskSize = params.get("SecondaryDataDiskSize")
        self._SecondaryDataDiskCount = params.get("SecondaryDataDiskCount")
        self._DiskType = params.get("DiskType")
        self._NetworkInterfaceType = params.get("NetworkInterfaceType")
        self._GpuType = params.get("GpuType")
        self._Quota = params.get("Quota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpInfo(AbstractModel):
    r"""公网Ip信息

    """

    def __init__(self):
        r"""
        :param _Ip: 10.100.0.20
        :type Ip: str
        :param _NetworkInstanceId: epn-asdfghjkl
        :type NetworkInstanceId: str
        :param _InstanceId: epm-asdfghjkl
        :type InstanceId: str
        :param _State: Unbound
        :type State: str
        :param _Type: Ipv4
        :type Type: str
        :param _CreatedAt: 2026-04-07T00:00:00
        :type CreatedAt: str
        :param _UpdatedAt: 2026-04-07T00:00:00
        :type UpdatedAt: str
        """
        self._Ip = None
        self._NetworkInstanceId = None
        self._InstanceId = None
        self._State = None
        self._Type = None
        self._CreatedAt = None
        self._UpdatedAt = None

    @property
    def Ip(self):
        r"""10.100.0.20
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def NetworkInstanceId(self):
        r"""epn-asdfghjkl
        :rtype: str
        """
        return self._NetworkInstanceId

    @NetworkInstanceId.setter
    def NetworkInstanceId(self, NetworkInstanceId):
        self._NetworkInstanceId = NetworkInstanceId

    @property
    def InstanceId(self):
        r"""epm-asdfghjkl
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def State(self):
        r"""Unbound
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Type(self):
        r"""Ipv4
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreatedAt(self):
        r"""2026-04-07T00:00:00
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""2026-04-07T00:00:00
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._NetworkInstanceId = params.get("NetworkInstanceId")
        self._InstanceId = params.get("InstanceId")
        self._State = params.get("State")
        self._Type = params.get("Type")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAttributeRequest(AbstractModel):
    r"""ModifyInstanceAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _InstanceName: 新的实例名称，1-60字符。与 NewPublicIp 至少传入一个。
        :type InstanceName: str
        :param _NewPublicIp: 新的公网IP（需从该实例所绑定公网实例的可用IP中选择）。与 InstanceName 至少传入一个。
        :type NewPublicIp: str
        :param _IpType: IP类型，ipv4 或 ipv6，默认 ipv4。仅在指定 NewPublicIp 时有效。
        :type IpType: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._NewPublicIp = None
        self._IpType = None

    @property
    def InstanceId(self):
        r"""实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""新的实例名称，1-60字符。与 NewPublicIp 至少传入一个。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def NewPublicIp(self):
        warnings.warn("parameter `NewPublicIp` is deprecated", DeprecationWarning) 

        r"""新的公网IP（需从该实例所绑定公网实例的可用IP中选择）。与 InstanceName 至少传入一个。
        :rtype: str
        """
        return self._NewPublicIp

    @NewPublicIp.setter
    def NewPublicIp(self, NewPublicIp):
        warnings.warn("parameter `NewPublicIp` is deprecated", DeprecationWarning) 

        self._NewPublicIp = NewPublicIp

    @property
    def IpType(self):
        warnings.warn("parameter `IpType` is deprecated", DeprecationWarning) 

        r"""IP类型，ipv4 或 ipv6，默认 ipv4。仅在指定 NewPublicIp 时有效。
        :rtype: str
        """
        return self._IpType

    @IpType.setter
    def IpType(self, IpType):
        warnings.warn("parameter `IpType` is deprecated", DeprecationWarning) 

        self._IpType = IpType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._NewPublicIp = params.get("NewPublicIp")
        self._IpType = params.get("IpType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAttributeResponse(AbstractModel):
    r"""ModifyInstanceAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPrivateNetworkInstanceRequest(AbstractModel):
    r"""ModifyPrivateNetworkInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInstanceId: 私网实例Id
        :type NetworkInstanceId: str
        :param _NetworkInstanceName: 新实例名称
        :type NetworkInstanceName: str
        """
        self._NetworkInstanceId = None
        self._NetworkInstanceName = None

    @property
    def NetworkInstanceId(self):
        r"""私网实例Id
        :rtype: str
        """
        return self._NetworkInstanceId

    @NetworkInstanceId.setter
    def NetworkInstanceId(self, NetworkInstanceId):
        self._NetworkInstanceId = NetworkInstanceId

    @property
    def NetworkInstanceName(self):
        r"""新实例名称
        :rtype: str
        """
        return self._NetworkInstanceName

    @NetworkInstanceName.setter
    def NetworkInstanceName(self, NetworkInstanceName):
        self._NetworkInstanceName = NetworkInstanceName


    def _deserialize(self, params):
        self._NetworkInstanceId = params.get("NetworkInstanceId")
        self._NetworkInstanceName = params.get("NetworkInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateNetworkInstanceResponse(AbstractModel):
    r"""ModifyPrivateNetworkInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPublicNetworkInstanceRequest(AbstractModel):
    r"""ModifyPublicNetworkInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInstanceId: 公网实例 ID
        :type NetworkInstanceId: str
        :param _NetworkInstanceName: 新实例名称
        :type NetworkInstanceName: str
        """
        self._NetworkInstanceId = None
        self._NetworkInstanceName = None

    @property
    def NetworkInstanceId(self):
        r"""公网实例 ID
        :rtype: str
        """
        return self._NetworkInstanceId

    @NetworkInstanceId.setter
    def NetworkInstanceId(self, NetworkInstanceId):
        self._NetworkInstanceId = NetworkInstanceId

    @property
    def NetworkInstanceName(self):
        r"""新实例名称
        :rtype: str
        """
        return self._NetworkInstanceName

    @NetworkInstanceName.setter
    def NetworkInstanceName(self, NetworkInstanceName):
        self._NetworkInstanceName = NetworkInstanceName


    def _deserialize(self, params):
        self._NetworkInstanceId = params.get("NetworkInstanceId")
        self._NetworkInstanceName = params.get("NetworkInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPublicNetworkInstanceResponse(AbstractModel):
    r"""ModifyPublicNetworkInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class PrivateNetworkInstanceInfo(AbstractModel):
    r"""私网实例信息

    """

    def __init__(self):
        r"""
        :param _NetworkInstanceId: 私网实例ID
        :type NetworkInstanceId: str
        :param _NetworkInstanceName: 私网实例名称
        :type NetworkInstanceName: str
        :param _ZoneId: 可用区ID
        :type ZoneId: str
        :param _Network: 网络地址
        :type Network: str
        :param _Mask: 网络掩码
        :type Mask: int
        :param _ServerCount: 关联物理机数量
        :type ServerCount: int
        :param _AvailableIpCount: 可用Ip数量
        :type AvailableIpCount: int
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        """
        self._NetworkInstanceId = None
        self._NetworkInstanceName = None
        self._ZoneId = None
        self._Network = None
        self._Mask = None
        self._ServerCount = None
        self._AvailableIpCount = None
        self._CreatedAt = None
        self._UpdatedAt = None

    @property
    def NetworkInstanceId(self):
        r"""私网实例ID
        :rtype: str
        """
        return self._NetworkInstanceId

    @NetworkInstanceId.setter
    def NetworkInstanceId(self, NetworkInstanceId):
        self._NetworkInstanceId = NetworkInstanceId

    @property
    def NetworkInstanceName(self):
        r"""私网实例名称
        :rtype: str
        """
        return self._NetworkInstanceName

    @NetworkInstanceName.setter
    def NetworkInstanceName(self, NetworkInstanceName):
        self._NetworkInstanceName = NetworkInstanceName

    @property
    def ZoneId(self):
        r"""可用区ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Network(self):
        r"""网络地址
        :rtype: str
        """
        return self._Network

    @Network.setter
    def Network(self, Network):
        self._Network = Network

    @property
    def Mask(self):
        r"""网络掩码
        :rtype: int
        """
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask

    @property
    def ServerCount(self):
        r"""关联物理机数量
        :rtype: int
        """
        return self._ServerCount

    @ServerCount.setter
    def ServerCount(self, ServerCount):
        self._ServerCount = ServerCount

    @property
    def AvailableIpCount(self):
        r"""可用Ip数量
        :rtype: int
        """
        return self._AvailableIpCount

    @AvailableIpCount.setter
    def AvailableIpCount(self, AvailableIpCount):
        self._AvailableIpCount = AvailableIpCount

    @property
    def CreatedAt(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._NetworkInstanceId = params.get("NetworkInstanceId")
        self._NetworkInstanceName = params.get("NetworkInstanceName")
        self._ZoneId = params.get("ZoneId")
        self._Network = params.get("Network")
        self._Mask = params.get("Mask")
        self._ServerCount = params.get("ServerCount")
        self._AvailableIpCount = params.get("AvailableIpCount")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicNetworkInstanceInfo(AbstractModel):
    r"""公网实例信息，包含实例ID、可用区ID、实例名称、线路、路由模式等信息

    """

    def __init__(self):
        r"""
        :param _NetworkInstanceId: 公网实例ID
        :type NetworkInstanceId: str
        :param _ZoneId: 可用区ID
        :type ZoneId: str
        :param _NetworkInstanceName: 公网实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkInstanceName: str
        :param _Bandwidth: 带宽，单位Mbps
注意：此字段可能返回 null，表示取不到有效值。
        :type Bandwidth: int
        :param _Line: 线路信息
        :type Line: str
        :param _RouteMode: 路由模式，枚举值：STATIC、BGP、OSPF
        :type RouteMode: str
        :param _ServerCount: 关联的物理服务器数量
        :type ServerCount: int
        :param _Ipv4Count: 已申请的Ipv4数量
        :type Ipv4Count: int
        :param _Ipv6Count: 已申请的Ipv6数量
        :type Ipv6Count: int
        :param _Ipv4CidrSet: 关联的Ipv4网段
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv4CidrSet: list of PublicNetworkSegment
        :param _Ipv6CidrSet: 关联的Ipv6网段
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6CidrSet: list of PublicNetworkSegment
        :param _CreatedAt: 公网实例创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 公网实例修改时间
        :type UpdatedAt: str
        """
        self._NetworkInstanceId = None
        self._ZoneId = None
        self._NetworkInstanceName = None
        self._Bandwidth = None
        self._Line = None
        self._RouteMode = None
        self._ServerCount = None
        self._Ipv4Count = None
        self._Ipv6Count = None
        self._Ipv4CidrSet = None
        self._Ipv6CidrSet = None
        self._CreatedAt = None
        self._UpdatedAt = None

    @property
    def NetworkInstanceId(self):
        r"""公网实例ID
        :rtype: str
        """
        return self._NetworkInstanceId

    @NetworkInstanceId.setter
    def NetworkInstanceId(self, NetworkInstanceId):
        self._NetworkInstanceId = NetworkInstanceId

    @property
    def ZoneId(self):
        r"""可用区ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def NetworkInstanceName(self):
        r"""公网实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NetworkInstanceName

    @NetworkInstanceName.setter
    def NetworkInstanceName(self, NetworkInstanceName):
        self._NetworkInstanceName = NetworkInstanceName

    @property
    def Bandwidth(self):
        r"""带宽，单位Mbps
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Line(self):
        r"""线路信息
        :rtype: str
        """
        return self._Line

    @Line.setter
    def Line(self, Line):
        self._Line = Line

    @property
    def RouteMode(self):
        r"""路由模式，枚举值：STATIC、BGP、OSPF
        :rtype: str
        """
        return self._RouteMode

    @RouteMode.setter
    def RouteMode(self, RouteMode):
        self._RouteMode = RouteMode

    @property
    def ServerCount(self):
        r"""关联的物理服务器数量
        :rtype: int
        """
        return self._ServerCount

    @ServerCount.setter
    def ServerCount(self, ServerCount):
        self._ServerCount = ServerCount

    @property
    def Ipv4Count(self):
        r"""已申请的Ipv4数量
        :rtype: int
        """
        return self._Ipv4Count

    @Ipv4Count.setter
    def Ipv4Count(self, Ipv4Count):
        self._Ipv4Count = Ipv4Count

    @property
    def Ipv6Count(self):
        r"""已申请的Ipv6数量
        :rtype: int
        """
        return self._Ipv6Count

    @Ipv6Count.setter
    def Ipv6Count(self, Ipv6Count):
        self._Ipv6Count = Ipv6Count

    @property
    def Ipv4CidrSet(self):
        r"""关联的Ipv4网段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PublicNetworkSegment
        """
        return self._Ipv4CidrSet

    @Ipv4CidrSet.setter
    def Ipv4CidrSet(self, Ipv4CidrSet):
        self._Ipv4CidrSet = Ipv4CidrSet

    @property
    def Ipv6CidrSet(self):
        r"""关联的Ipv6网段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PublicNetworkSegment
        """
        return self._Ipv6CidrSet

    @Ipv6CidrSet.setter
    def Ipv6CidrSet(self, Ipv6CidrSet):
        self._Ipv6CidrSet = Ipv6CidrSet

    @property
    def CreatedAt(self):
        r"""公网实例创建时间
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""公网实例修改时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._NetworkInstanceId = params.get("NetworkInstanceId")
        self._ZoneId = params.get("ZoneId")
        self._NetworkInstanceName = params.get("NetworkInstanceName")
        self._Bandwidth = params.get("Bandwidth")
        self._Line = params.get("Line")
        self._RouteMode = params.get("RouteMode")
        self._ServerCount = params.get("ServerCount")
        self._Ipv4Count = params.get("Ipv4Count")
        self._Ipv6Count = params.get("Ipv6Count")
        if params.get("Ipv4CidrSet") is not None:
            self._Ipv4CidrSet = []
            for item in params.get("Ipv4CidrSet"):
                obj = PublicNetworkSegment()
                obj._deserialize(item)
                self._Ipv4CidrSet.append(obj)
        if params.get("Ipv6CidrSet") is not None:
            self._Ipv6CidrSet = []
            for item in params.get("Ipv6CidrSet"):
                obj = PublicNetworkSegment()
                obj._deserialize(item)
                self._Ipv6CidrSet.append(obj)
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicNetworkSegment(AbstractModel):
    r"""公网网段信息，包含网段cidr和网关ip

    """

    def __init__(self):
        r"""
        :param _Cidr: 网段Cidr
        :type Cidr: str
        :param _Gateway: 网关Ip
        :type Gateway: str
        """
        self._Cidr = None
        self._Gateway = None

    @property
    def Cidr(self):
        r"""网段Cidr
        :rtype: str
        """
        return self._Cidr

    @Cidr.setter
    def Cidr(self, Cidr):
        self._Cidr = Cidr

    @property
    def Gateway(self):
        r"""网关Ip
        :rtype: str
        """
        return self._Gateway

    @Gateway.setter
    def Gateway(self, Gateway):
        self._Gateway = Gateway


    def _deserialize(self, params):
        self._Cidr = params.get("Cidr")
        self._Gateway = params.get("Gateway")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleasePublicIpRequest(AbstractModel):
    r"""ReleasePublicIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInstanceId: 公网实例 ID（路由发布模式为 STATIC ）
        :type NetworkInstanceId: str
        :param _Type: 待释放的Ip类型，枚举值：ipv4、ipv6
        :type Type: str
        :param _IpList: 待释放的 Ip 地址列表
        :type IpList: list of str
        """
        self._NetworkInstanceId = None
        self._Type = None
        self._IpList = None

    @property
    def NetworkInstanceId(self):
        r"""公网实例 ID（路由发布模式为 STATIC ）
        :rtype: str
        """
        return self._NetworkInstanceId

    @NetworkInstanceId.setter
    def NetworkInstanceId(self, NetworkInstanceId):
        self._NetworkInstanceId = NetworkInstanceId

    @property
    def Type(self):
        r"""待释放的Ip类型，枚举值：ipv4、ipv6
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IpList(self):
        r"""待释放的 Ip 地址列表
        :rtype: list of str
        """
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._NetworkInstanceId = params.get("NetworkInstanceId")
        self._Type = params.get("Type")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleasePublicIpResponse(AbstractModel):
    r"""ReleasePublicIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SwitchData(AbstractModel):
    r"""交换机数据

    """

    def __init__(self):
        r"""
        :param _Time: UTC时间
        :type Time: str
        :param _Value: 统计值
        :type Value: float
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        r"""UTC时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        r"""统计值
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesRequest(AbstractModel):
    r"""TerminateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: <p>实例ID列表，最多100个。</p>
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        r"""<p>实例ID列表，最多100个。</p>
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesResponse(AbstractModel):
    r"""TerminateInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: <p>销毁成功的实例ID列表。</p>
        :type InstanceIdSet: list of str
        :param _FailedInstanceSet: <p>销毁失败的实例信息列表（部分成功时返回）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedInstanceSet: list of FailedInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceIdSet = None
        self._FailedInstanceSet = None
        self._RequestId = None

    @property
    def InstanceIdSet(self):
        r"""<p>销毁成功的实例ID列表。</p>
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def FailedInstanceSet(self):
        r"""<p>销毁失败的实例信息列表（部分成功时返回）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FailedInstance
        """
        return self._FailedInstanceSet

    @FailedInstanceSet.setter
    def FailedInstanceSet(self, FailedInstanceSet):
        self._FailedInstanceSet = FailedInstanceSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        if params.get("FailedInstanceSet") is not None:
            self._FailedInstanceSet = []
            for item in params.get("FailedInstanceSet"):
                obj = FailedInstance()
                obj._deserialize(item)
                self._FailedInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class ZoneInfo(AbstractModel):
    r"""跨地域聚合后的可用区信息。

    """

    def __init__(self):
        r"""
        :param _ZoneId: 可用区ID。
        :type ZoneId: int
        :param _Zone: 可用区代码。
        :type Zone: str
        :param _ZoneName: 可用区中文名称。
        :type ZoneName: str
        :param _ZoneNameEn: 可用区英文名称。
        :type ZoneNameEn: str
        :param _Region: 地域代码。
        :type Region: str
        :param _Location: 区域代码。
        :type Location: str
        :param _LocationName: 区域名称。
        :type LocationName: str
        """
        self._ZoneId = None
        self._Zone = None
        self._ZoneName = None
        self._ZoneNameEn = None
        self._Region = None
        self._Location = None
        self._LocationName = None

    @property
    def ZoneId(self):
        r"""可用区ID。
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Zone(self):
        r"""可用区代码。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        r"""可用区中文名称。
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneNameEn(self):
        r"""可用区英文名称。
        :rtype: str
        """
        return self._ZoneNameEn

    @ZoneNameEn.setter
    def ZoneNameEn(self, ZoneNameEn):
        self._ZoneNameEn = ZoneNameEn

    @property
    def Region(self):
        r"""地域代码。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Location(self):
        r"""区域代码。
        :rtype: str
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def LocationName(self):
        r"""区域名称。
        :rtype: str
        """
        return self._LocationName

    @LocationName.setter
    def LocationName(self, LocationName):
        self._LocationName = LocationName


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._ZoneNameEn = params.get("ZoneNameEn")
        self._Region = params.get("Region")
        self._Location = params.get("Location")
        self._LocationName = params.get("LocationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        