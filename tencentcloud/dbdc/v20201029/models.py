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


class AddNodesToDBCustomClusterRequest(AbstractModel):
    r"""AddNodesToDBCustomCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: <p>集群ID</p>
        :type ClusterId: str
        :param _NodeIds: <p>需上架的节点 ID 列表</p>
        :type NodeIds: list of str
        :param _ImageId: <p>节点上架后重设的操作系统镜像ID</p><p>取值参考：可通过&quot;DescribeDBCustomImages&quot;接口获取支持的镜像。</p>
        :type ImageId: str
        :param _LoginSettings: <p>实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。</p><p>入参限制：若选择密钥方式，KeyIds 仅支持单个 ID。三种方式必须且仅可以设置其中一种。</p>
        :type LoginSettings: :class:`tencentcloud.dbdc.v20201029.models.LoginSettings`
        """
        self._ClusterId = None
        self._NodeIds = None
        self._ImageId = None
        self._LoginSettings = None

    @property
    def ClusterId(self):
        r"""<p>集群ID</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodeIds(self):
        r"""<p>需上架的节点 ID 列表</p>
        :rtype: list of str
        """
        return self._NodeIds

    @NodeIds.setter
    def NodeIds(self, NodeIds):
        self._NodeIds = NodeIds

    @property
    def ImageId(self):
        r"""<p>节点上架后重设的操作系统镜像ID</p><p>取值参考：可通过&quot;DescribeDBCustomImages&quot;接口获取支持的镜像。</p>
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def LoginSettings(self):
        r"""<p>实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。</p><p>入参限制：若选择密钥方式，KeyIds 仅支持单个 ID。三种方式必须且仅可以设置其中一种。</p>
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.LoginSettings`
        """
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodeIds = params.get("NodeIds")
        self._ImageId = params.get("ImageId")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddNodesToDBCustomClusterResponse(AbstractModel):
    r"""AddNodesToDBCustomCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>上架节点的任务ID</p>
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>上架节点的任务ID</p>
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ApiServerNetwork(AbstractModel):
    r"""连通 DB Custom 集群 API Server 的网络配置。

    """

    def __init__(self):
        r"""
        :param _VpcId: <p>API Server的访问私有网络ID</p>
        :type VpcId: str
        :param _SubnetId: <p>API Server的访问私有网络子网ID</p>
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

    @property
    def VpcId(self):
        r"""<p>API Server的访问私有网络ID</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""<p>API Server的访问私有网络子网ID</p>
        :rtype: str
        """
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
        


class CheckRoleAuthorizedRequest(AbstractModel):
    r"""CheckRoleAuthorized请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleName: <p>待检测的角色名字</p>
        :type RoleName: str
        """
        self._RoleName = None

    @property
    def RoleName(self):
        r"""<p>待检测的角色名字</p>
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckRoleAuthorizedResponse(AbstractModel):
    r"""CheckRoleAuthorized返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: <p>角色权限状态</p><p>枚举值：</p><ul><li>AUTHORIZED： 已经创建授权</li><li>NEED_GRANT： 未授权</li><li>ERROR： 报错</li></ul>
        :type Status: str
        :param _Message: <p>出错的错误信息</p>
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Message = None
        self._RequestId = None

    @property
    def Status(self):
        r"""<p>角色权限状态</p><p>枚举值：</p><ul><li>AUTHORIZED： 已经创建授权</li><li>NEED_GRANT： 未授权</li><li>ERROR： 报错</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        r"""<p>出错的错误信息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class ContainerNetwork(AbstractModel):
    r"""联通 DB Custom 集群中容器的网络配置。

    """

    def __init__(self):
        r"""
        :param _VpcId: <p>容器网络的虚拟网络ID</p>
        :type VpcId: str
        :param _SubnetIds: <p>容器网络的虚拟网络子网列表</p>
        :type SubnetIds: list of str
        """
        self._VpcId = None
        self._SubnetIds = None

    @property
    def VpcId(self):
        r"""<p>容器网络的虚拟网络ID</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        r"""<p>容器网络的虚拟网络子网列表</p>
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBCustomClusterRequest(AbstractModel):
    r"""CreateDBCustomCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ContainerNetwork: <p>容器网络，在此集群的所有 POD 与此网络连通</p>
        :type ContainerNetwork: :class:`tencentcloud.dbdc.v20201029.models.ContainerNetwork`
        :param _ClusterName: <p>集群名称</p><p>入参限制：最长128个字符，只能为中文，英文，下划线。</p>
        :type ClusterName: str
        :param _ApiServerNetwork: <p>集群的API Server的网络信息</p><p>入参限制：必须为此账号下拥有的网络地址，可以与容器网络保持一致。</p>
        :type ApiServerNetwork: :class:`tencentcloud.dbdc.v20201029.models.ApiServerNetwork`
        :param _ClusterDescription: <p>集群描述</p>
        :type ClusterDescription: str
        :param _Tags: <p>集群标签</p>
        :type Tags: list of Tag
        :param _ClientToken: <p>客户端Token</p>
        :type ClientToken: str
        """
        self._ContainerNetwork = None
        self._ClusterName = None
        self._ApiServerNetwork = None
        self._ClusterDescription = None
        self._Tags = None
        self._ClientToken = None

    @property
    def ContainerNetwork(self):
        r"""<p>容器网络，在此集群的所有 POD 与此网络连通</p>
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.ContainerNetwork`
        """
        return self._ContainerNetwork

    @ContainerNetwork.setter
    def ContainerNetwork(self, ContainerNetwork):
        self._ContainerNetwork = ContainerNetwork

    @property
    def ClusterName(self):
        r"""<p>集群名称</p><p>入参限制：最长128个字符，只能为中文，英文，下划线。</p>
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ApiServerNetwork(self):
        r"""<p>集群的API Server的网络信息</p><p>入参限制：必须为此账号下拥有的网络地址，可以与容器网络保持一致。</p>
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.ApiServerNetwork`
        """
        return self._ApiServerNetwork

    @ApiServerNetwork.setter
    def ApiServerNetwork(self, ApiServerNetwork):
        self._ApiServerNetwork = ApiServerNetwork

    @property
    def ClusterDescription(self):
        r"""<p>集群描述</p>
        :rtype: str
        """
        return self._ClusterDescription

    @ClusterDescription.setter
    def ClusterDescription(self, ClusterDescription):
        self._ClusterDescription = ClusterDescription

    @property
    def Tags(self):
        r"""<p>集群标签</p>
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ClientToken(self):
        r"""<p>客户端Token</p>
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken


    def _deserialize(self, params):
        if params.get("ContainerNetwork") is not None:
            self._ContainerNetwork = ContainerNetwork()
            self._ContainerNetwork._deserialize(params.get("ContainerNetwork"))
        self._ClusterName = params.get("ClusterName")
        if params.get("ApiServerNetwork") is not None:
            self._ApiServerNetwork = ApiServerNetwork()
            self._ApiServerNetwork._deserialize(params.get("ApiServerNetwork"))
        self._ClusterDescription = params.get("ClusterDescription")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ClientToken = params.get("ClientToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBCustomClusterResponse(AbstractModel):
    r"""CreateDBCustomCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: <p>本次创建的集群ID</p>
        :type ClusterId: str
        :param _TaskId: <p>本次创建集群的任务ID</p>
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def ClusterId(self):
        r"""<p>本次创建的集群ID</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TaskId(self):
        r"""<p>本次创建集群的任务ID</p>
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._ClusterId = params.get("ClusterId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateDBCustomNodesRequest(AbstractModel):
    r"""CreateDBCustomNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Zone: <p>产品支持的可用区</p><p>枚举值：</p><ul><li>ap-shanghai-5： 上海五区</li><li>ap-shanghai-8： 上海八区</li><li>ap-nanjing-3： 南京三区</li></ul>
        :type Zone: str
        :param _ImageId: <p>镜像ID</p><p>参数格式：img-xxxxxxx</p><p>入参限制：必须为当前账号下DB Custom 产品拥有的镜像</p><p>取值参考：可通过&quot;DescribeDBCustomImages&quot;接口获取支持的镜像。</p>
        :type ImageId: str
        :param _VpcId: <p>为节点打通SSH连接的VPC 网络ID。</p><p>参数格式：vpc-b4zgtest</p><p>入参限制：必须是当前账号下拥有的VPC 网络ID，且不能跨地域。</p><p>取值参考：可通过【查询VPC列表】接口获取：https://cloud.tencent.com/document/product/215/15778</p>
        :type VpcId: str
        :param _SubnetId: <p>为节点打通SSH连接的VPC 子网 ID。 </p><p>参数格式：subnet-t13dtest</p><p>入参限制：必须是VPC之下的子网，子网必须与可用区对应。</p><p>取值参考：可通过【查询子网列表】接口获取：https://cloud.tencent.com/document/product/215/15784</p>
        :type SubnetId: str
        :param _Period: <p>购买时长(月): 1/2/3/4/5/6/7/8/9/10/11/12/24/36</p><p>取值范围：[1, 36]</p><p>单位：月</p><p>默认值：1</p>
        :type Period: int
        :param _NodeType: <p>节点机型</p><p>枚举值：</p><ul><li>DB.AT5.32XLARGE512： 高IO型服务器：128核心512GB内存，8*7180GB本地NvME SSDB。</li><li>DB.AT5.64XLARGE1152： 高IO型服务器：256核心1152GB内存，12*7180GB本地NvME SSDB。</li><li>DB.AT5.128XLARGE2304： 高IO型服务器：512核心2304GB内存，24*7180GB本地NvME SSDB。</li><li>DB.AT5.16XLARGE256： 高IO型服务器：64核心256GB内存，4*7180GB本地NvME SSDB。</li><li>DB.AT5.8XLARGE128： 高IO型服务器：32核心128GB内存，2*7180GB本地NvME SSDB。</li></ul>
        :type NodeType: str
        :param _NodeCount: <p>购买的节点数量</p><p>取值范围：[1, 20]</p>
        :type NodeCount: int
        :param _LoginSettings: <p>实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。</p><p>入参限制：若选择密钥方式，KeyIds 仅支持单个 ID。三种方式必须且仅可以设置其中一种。</p>
        :type LoginSettings: :class:`tencentcloud.dbdc.v20201029.models.LoginSettings`
        :param _AutoRenew: <p>自动续费配置</p><p>枚举值：</p><ul><li>1： 自动续费</li><li>2： 不自动续费</li></ul><p>默认值：不自动续费</p>
        :type AutoRenew: int
        :param _NodeName: <p>节点名称</p><p>入参限制：最多128个字符</p>
        :type NodeName: str
        :param _AutoVoucher: <p>是否使用代金券自动抵扣</p><p>枚举值：</p><ul><li>1： 使用</li><li>0： 不使用</li></ul><p>默认值：0</p>
        :type AutoVoucher: int
        :param _VoucherIds: <p>代金券ID</p><p>入参限制：必须为当前账号下拥有的未抵扣的代金券ID。</p>
        :type VoucherIds: list of str
        :param _Tags: <p>标签</p>
        :type Tags: list of Tag
        :param _ClientToken: <p>用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。</p>
        :type ClientToken: str
        """
        self._Zone = None
        self._ImageId = None
        self._VpcId = None
        self._SubnetId = None
        self._Period = None
        self._NodeType = None
        self._NodeCount = None
        self._LoginSettings = None
        self._AutoRenew = None
        self._NodeName = None
        self._AutoVoucher = None
        self._VoucherIds = None
        self._Tags = None
        self._ClientToken = None

    @property
    def Zone(self):
        r"""<p>产品支持的可用区</p><p>枚举值：</p><ul><li>ap-shanghai-5： 上海五区</li><li>ap-shanghai-8： 上海八区</li><li>ap-nanjing-3： 南京三区</li></ul>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ImageId(self):
        r"""<p>镜像ID</p><p>参数格式：img-xxxxxxx</p><p>入参限制：必须为当前账号下DB Custom 产品拥有的镜像</p><p>取值参考：可通过&quot;DescribeDBCustomImages&quot;接口获取支持的镜像。</p>
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def VpcId(self):
        r"""<p>为节点打通SSH连接的VPC 网络ID。</p><p>参数格式：vpc-b4zgtest</p><p>入参限制：必须是当前账号下拥有的VPC 网络ID，且不能跨地域。</p><p>取值参考：可通过【查询VPC列表】接口获取：https://cloud.tencent.com/document/product/215/15778</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""<p>为节点打通SSH连接的VPC 子网 ID。 </p><p>参数格式：subnet-t13dtest</p><p>入参限制：必须是VPC之下的子网，子网必须与可用区对应。</p><p>取值参考：可通过【查询子网列表】接口获取：https://cloud.tencent.com/document/product/215/15784</p>
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Period(self):
        r"""<p>购买时长(月): 1/2/3/4/5/6/7/8/9/10/11/12/24/36</p><p>取值范围：[1, 36]</p><p>单位：月</p><p>默认值：1</p>
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def NodeType(self):
        r"""<p>节点机型</p><p>枚举值：</p><ul><li>DB.AT5.32XLARGE512： 高IO型服务器：128核心512GB内存，8*7180GB本地NvME SSDB。</li><li>DB.AT5.64XLARGE1152： 高IO型服务器：256核心1152GB内存，12*7180GB本地NvME SSDB。</li><li>DB.AT5.128XLARGE2304： 高IO型服务器：512核心2304GB内存，24*7180GB本地NvME SSDB。</li><li>DB.AT5.16XLARGE256： 高IO型服务器：64核心256GB内存，4*7180GB本地NvME SSDB。</li><li>DB.AT5.8XLARGE128： 高IO型服务器：32核心128GB内存，2*7180GB本地NvME SSDB。</li></ul>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeCount(self):
        r"""<p>购买的节点数量</p><p>取值范围：[1, 20]</p>
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def LoginSettings(self):
        r"""<p>实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。</p><p>入参限制：若选择密钥方式，KeyIds 仅支持单个 ID。三种方式必须且仅可以设置其中一种。</p>
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.LoginSettings`
        """
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def AutoRenew(self):
        r"""<p>自动续费配置</p><p>枚举值：</p><ul><li>1： 自动续费</li><li>2： 不自动续费</li></ul><p>默认值：不自动续费</p>
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def NodeName(self):
        r"""<p>节点名称</p><p>入参限制：最多128个字符</p>
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def AutoVoucher(self):
        r"""<p>是否使用代金券自动抵扣</p><p>枚举值：</p><ul><li>1： 使用</li><li>0： 不使用</li></ul><p>默认值：0</p>
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""<p>代金券ID</p><p>入参限制：必须为当前账号下拥有的未抵扣的代金券ID。</p>
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds

    @property
    def Tags(self):
        r"""<p>标签</p>
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ClientToken(self):
        r"""<p>用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。</p>
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ImageId = params.get("ImageId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Period = params.get("Period")
        self._NodeType = params.get("NodeType")
        self._NodeCount = params.get("NodeCount")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._AutoRenew = params.get("AutoRenew")
        self._NodeName = params.get("NodeName")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ClientToken = params.get("ClientToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBCustomNodesResponse(AbstractModel):
    r"""CreateDBCustomNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeIds: <p>节点ID列表</p>
        :type NodeIds: list of str
        :param _TaskId: <p>创建节点的任务ID</p>
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NodeIds = None
        self._TaskId = None
        self._RequestId = None

    @property
    def NodeIds(self):
        r"""<p>节点ID列表</p>
        :rtype: list of str
        """
        return self._NodeIds

    @NodeIds.setter
    def NodeIds(self, NodeIds):
        self._NodeIds = NodeIds

    @property
    def TaskId(self):
        r"""<p>创建节点的任务ID</p>
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._NodeIds = params.get("NodeIds")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DBCustomCluster(AbstractModel):
    r"""DB Custom 集群信息。

    """

    def __init__(self):
        r"""
        :param _ClusterId: <p>集群ID</p>
        :type ClusterId: str
        :param _ClusterName: <p>集群名称</p>
        :type ClusterName: str
        :param _Region: <p>集群支持的地域</p>
        :type Region: str
        :param _ClusterLevel: <p>集群规模</p><p>默认值：L500</p>
        :type ClusterLevel: str
        :param _ClusterStatus: <p>DB Custom 集群状态</p><p>枚举值：</p><ul><li>Creating： 创建中</li><li>Running： 运行中</li><li>Destroying： 销毁中</li></ul>
        :type ClusterStatus: str
        :param _ClusterVersion: <p>集群版本号</p>
        :type ClusterVersion: str
        :param _ClusterNodeNum: <p>集群中的节点数量</p><p>单位：台</p>
        :type ClusterNodeNum: int
        :param _ClusterDescription: <p>集群描述</p>
        :type ClusterDescription: str
        :param _CreatedTime: <p>创建时间</p>
        :type CreatedTime: str
        :param _Tags: <p>集群的标签信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Region = None
        self._ClusterLevel = None
        self._ClusterStatus = None
        self._ClusterVersion = None
        self._ClusterNodeNum = None
        self._ClusterDescription = None
        self._CreatedTime = None
        self._Tags = None

    @property
    def ClusterId(self):
        r"""<p>集群ID</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""<p>集群名称</p>
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Region(self):
        r"""<p>集群支持的地域</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ClusterLevel(self):
        r"""<p>集群规模</p><p>默认值：L500</p>
        :rtype: str
        """
        return self._ClusterLevel

    @ClusterLevel.setter
    def ClusterLevel(self, ClusterLevel):
        self._ClusterLevel = ClusterLevel

    @property
    def ClusterStatus(self):
        r"""<p>DB Custom 集群状态</p><p>枚举值：</p><ul><li>Creating： 创建中</li><li>Running： 运行中</li><li>Destroying： 销毁中</li></ul>
        :rtype: str
        """
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def ClusterVersion(self):
        r"""<p>集群版本号</p>
        :rtype: str
        """
        return self._ClusterVersion

    @ClusterVersion.setter
    def ClusterVersion(self, ClusterVersion):
        self._ClusterVersion = ClusterVersion

    @property
    def ClusterNodeNum(self):
        r"""<p>集群中的节点数量</p><p>单位：台</p>
        :rtype: int
        """
        return self._ClusterNodeNum

    @ClusterNodeNum.setter
    def ClusterNodeNum(self, ClusterNodeNum):
        self._ClusterNodeNum = ClusterNodeNum

    @property
    def ClusterDescription(self):
        r"""<p>集群描述</p>
        :rtype: str
        """
        return self._ClusterDescription

    @ClusterDescription.setter
    def ClusterDescription(self, ClusterDescription):
        self._ClusterDescription = ClusterDescription

    @property
    def CreatedTime(self):
        r"""<p>创建时间</p>
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Tags(self):
        r"""<p>集群的标签信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Region = params.get("Region")
        self._ClusterLevel = params.get("ClusterLevel")
        self._ClusterStatus = params.get("ClusterStatus")
        self._ClusterVersion = params.get("ClusterVersion")
        self._ClusterNodeNum = params.get("ClusterNodeNum")
        self._ClusterDescription = params.get("ClusterDescription")
        self._CreatedTime = params.get("CreatedTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBCustomClusterNode(AbstractModel):
    r"""DB Custom 集群节点信息。

    """

    def __init__(self):
        r"""
        :param _NodeId: <p>节点ID</p>
        :type NodeId: str
        :param _NodeName: <p>节点名称</p>
        :type NodeName: str
        :param _LanIP: <p>节点内网IP地址</p>
        :type LanIP: str
        :param _SSHEndpoint: <p>节点SSH 访问的Endpoint。格式为IP:Port.</p>
        :type SSHEndpoint: str
        :param _Status: <p>节点在集群中的实例状态</p>
        :type Status: str
        :param _Zone: <p>节点所属的地域</p>
        :type Zone: str
        :param _NodeType: <p>节点类型</p><p>枚举值：</p><ul><li>DB.AT5.32XLARGE512： 高IO型服务器：128核心512GB内存，8*7180GB本地NvME SSDB。</li><li>DB.AT5.64XLARGE1152： 高IO型服务器：256核心1152GB内存，12*7180GB本地NvME SSDB。</li><li>DB.AT5.128XLARGE2304： 高IO型服务器：512核心2304GB内存，24*7180GB本地NvME SSDB。</li><li>DB.AT5.16XLARGE256： 高IO型服务器：64核心256GB内存，4*7180GB本地NvME SSDB。</li><li>DB.AT5.8XLARGE128： 高IO型服务器：32核心128GB内存，2*7180GB本地NvME SSDB。</li></ul>
        :type NodeType: str
        """
        self._NodeId = None
        self._NodeName = None
        self._LanIP = None
        self._SSHEndpoint = None
        self._Status = None
        self._Zone = None
        self._NodeType = None

    @property
    def NodeId(self):
        r"""<p>节点ID</p>
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeName(self):
        r"""<p>节点名称</p>
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def LanIP(self):
        r"""<p>节点内网IP地址</p>
        :rtype: str
        """
        return self._LanIP

    @LanIP.setter
    def LanIP(self, LanIP):
        self._LanIP = LanIP

    @property
    def SSHEndpoint(self):
        r"""<p>节点SSH 访问的Endpoint。格式为IP:Port.</p>
        :rtype: str
        """
        return self._SSHEndpoint

    @SSHEndpoint.setter
    def SSHEndpoint(self, SSHEndpoint):
        self._SSHEndpoint = SSHEndpoint

    @property
    def Status(self):
        r"""<p>节点在集群中的实例状态</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Zone(self):
        r"""<p>节点所属的地域</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NodeType(self):
        r"""<p>节点类型</p><p>枚举值：</p><ul><li>DB.AT5.32XLARGE512： 高IO型服务器：128核心512GB内存，8*7180GB本地NvME SSDB。</li><li>DB.AT5.64XLARGE1152： 高IO型服务器：256核心1152GB内存，12*7180GB本地NvME SSDB。</li><li>DB.AT5.128XLARGE2304： 高IO型服务器：512核心2304GB内存，24*7180GB本地NvME SSDB。</li><li>DB.AT5.16XLARGE256： 高IO型服务器：64核心256GB内存，4*7180GB本地NvME SSDB。</li><li>DB.AT5.8XLARGE128： 高IO型服务器：32核心128GB内存，2*7180GB本地NvME SSDB。</li></ul>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeName = params.get("NodeName")
        self._LanIP = params.get("LanIP")
        self._SSHEndpoint = params.get("SSHEndpoint")
        self._Status = params.get("Status")
        self._Zone = params.get("Zone")
        self._NodeType = params.get("NodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBCustomImage(AbstractModel):
    r"""DB Custom 可选的镜像信息。

    """

    def __init__(self):
        r"""
        :param _ImageId: <p>镜像ID</p>
        :type ImageId: str
        :param _OsName: <p>操作系统名称</p>
        :type OsName: str
        :param _ImageType: <p>镜像类型</p><p>枚举值：</p><ul><li>PUBLIC_IMAGE： 公共镜像 (腾讯云官方镜像)</li><li>PRIVATE_IMAGE： 私有镜像 (客户专属镜像)</li></ul>
        :type ImageType: str
        :param _Architecture: <p>操作系统架构</p><p>枚举值：</p><ul><li>x86_64： X86 64位架构</li><li>arm64： ARM 64位机构</li></ul>
        :type Architecture: str
        """
        self._ImageId = None
        self._OsName = None
        self._ImageType = None
        self._Architecture = None

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
    def OsName(self):
        r"""<p>操作系统名称</p>
        :rtype: str
        """
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def ImageType(self):
        r"""<p>镜像类型</p><p>枚举值：</p><ul><li>PUBLIC_IMAGE： 公共镜像 (腾讯云官方镜像)</li><li>PRIVATE_IMAGE： 私有镜像 (客户专属镜像)</li></ul>
        :rtype: str
        """
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType

    @property
    def Architecture(self):
        r"""<p>操作系统架构</p><p>枚举值：</p><ul><li>x86_64： X86 64位架构</li><li>arm64： ARM 64位机构</li></ul>
        :rtype: str
        """
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._OsName = params.get("OsName")
        self._ImageType = params.get("ImageType")
        self._Architecture = params.get("Architecture")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBCustomNode(AbstractModel):
    r"""DB Custom 节点信息。

    """

    def __init__(self):
        r"""
        :param _NodeId: <p>节点ID</p>
        :type NodeId: str
        :param _NodeName: <p>节点名称</p>
        :type NodeName: str
        :param _SSHEndpoint: <p>访问此节点的SSH Endpoint，格式为IP:Port</p>
        :type SSHEndpoint: str
        :param _LanIP: <p>节点的内网通信IP地址</p>
        :type LanIP: str
        :param _ClusterId: <p>节点所属的集群ID</p>
        :type ClusterId: str
        :param _Zone: <p>节点所属的可用区</p>
        :type Zone: str
        :param _NodeType: <p>节点类型</p><p>枚举值：</p><ul><li>DB.AT5.32XLARGE512： 高IO型服务器：128核心512GB内存，8*7180GB本地NvME SSDB。</li><li>DB.AT5.64XLARGE1152： 高IO型服务器：256核心1152GB内存，12*7180GB本地NvME SSDB。</li><li>DB.AT5.128XLARGE2304： 高IO型服务器：512核心2304GB内存，24*7180GB本地NvME SSDB。</li><li>DB.AT5.16XLARGE256： 高IO型服务器：64核心256GB内存，4*7180GB本地NvME SSDB。</li><li>DB.AT5.8XLARGE128： 高IO型服务器：32核心128GB内存，2*7180GB本地NvME SSDB。</li></ul>
        :type NodeType: str
        :param _CPU: <p>节点CPU大小</p><p>单位：核</p>
        :type CPU: int
        :param _Memory: <p>节点内存</p><p>单位：GiB</p>
        :type Memory: int
        :param _SystemDisk: <p>系统盘信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemDisk: :class:`tencentcloud.dbdc.v20201029.models.SystemDisk`
        :param _DataDisks: <p>数据盘信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDisks: list of DataDisk
        :param _OsName: <p>节点的操作系统名称</p>
        :type OsName: str
        :param _ImageId: <p>节点的操作系统镜像ID</p>
        :type ImageId: str
        :param _VpcId: <p>节点SSH Endpoint 所属的VPC ID</p>
        :type VpcId: str
        :param _SubnetId: <p>节点SSH Endpoint 所属的VPC 子网ID</p>
        :type SubnetId: str
        :param _Status: <p>节点状态</p><p>枚举值：</p><ul><li>Creating： 创建中</li><li>Running： 运行中</li><li>Isolating： 隔离中</li><li>Isolated： 已隔离</li><li>Activating： 解除隔离中</li><li>Destroying： 销毁中</li></ul>
        :type Status: str
        :param _ChargeType: <p>付费类型</p><p>枚举值：</p><ul><li>PREPAID： 包年包月</li></ul>
        :type ChargeType: str
        :param _ExpireTime: <p>节点到期时间</p>
        :type ExpireTime: str
        :param _CreatedTime: <p>节点创建时间</p>
        :type CreatedTime: str
        :param _IsolatedTime: <p>节点隔离时间</p>
        :type IsolatedTime: str
        :param _Tags: <p>节点标签信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _AutoRenew: <p>节点是否自动续费标记</p><p>枚举值：</p><ul><li>1： 自动续费</li><li>0： 不自动续费</li></ul>
        :type AutoRenew: int
        :param _SwitchId: <p>交换机ID（已加密）</p>
        :type SwitchId: str
        :param _RackId: <p>机架ID（已加密）</p>
        :type RackId: str
        :param _HostIp: <p>底层物理机IP（已加密）</p>
        :type HostIp: str
        """
        self._NodeId = None
        self._NodeName = None
        self._SSHEndpoint = None
        self._LanIP = None
        self._ClusterId = None
        self._Zone = None
        self._NodeType = None
        self._CPU = None
        self._Memory = None
        self._SystemDisk = None
        self._DataDisks = None
        self._OsName = None
        self._ImageId = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._ChargeType = None
        self._ExpireTime = None
        self._CreatedTime = None
        self._IsolatedTime = None
        self._Tags = None
        self._AutoRenew = None
        self._SwitchId = None
        self._RackId = None
        self._HostIp = None

    @property
    def NodeId(self):
        r"""<p>节点ID</p>
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeName(self):
        r"""<p>节点名称</p>
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def SSHEndpoint(self):
        r"""<p>访问此节点的SSH Endpoint，格式为IP:Port</p>
        :rtype: str
        """
        return self._SSHEndpoint

    @SSHEndpoint.setter
    def SSHEndpoint(self, SSHEndpoint):
        self._SSHEndpoint = SSHEndpoint

    @property
    def LanIP(self):
        r"""<p>节点的内网通信IP地址</p>
        :rtype: str
        """
        return self._LanIP

    @LanIP.setter
    def LanIP(self, LanIP):
        self._LanIP = LanIP

    @property
    def ClusterId(self):
        r"""<p>节点所属的集群ID</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Zone(self):
        r"""<p>节点所属的可用区</p>
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NodeType(self):
        r"""<p>节点类型</p><p>枚举值：</p><ul><li>DB.AT5.32XLARGE512： 高IO型服务器：128核心512GB内存，8*7180GB本地NvME SSDB。</li><li>DB.AT5.64XLARGE1152： 高IO型服务器：256核心1152GB内存，12*7180GB本地NvME SSDB。</li><li>DB.AT5.128XLARGE2304： 高IO型服务器：512核心2304GB内存，24*7180GB本地NvME SSDB。</li><li>DB.AT5.16XLARGE256： 高IO型服务器：64核心256GB内存，4*7180GB本地NvME SSDB。</li><li>DB.AT5.8XLARGE128： 高IO型服务器：32核心128GB内存，2*7180GB本地NvME SSDB。</li></ul>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def CPU(self):
        r"""<p>节点CPU大小</p><p>单位：核</p>
        :rtype: int
        """
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        r"""<p>节点内存</p><p>单位：GiB</p>
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def SystemDisk(self):
        r"""<p>系统盘信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        r"""<p>数据盘信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def OsName(self):
        r"""<p>节点的操作系统名称</p>
        :rtype: str
        """
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def ImageId(self):
        r"""<p>节点的操作系统镜像ID</p>
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def VpcId(self):
        r"""<p>节点SSH Endpoint 所属的VPC ID</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""<p>节点SSH Endpoint 所属的VPC 子网ID</p>
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        r"""<p>节点状态</p><p>枚举值：</p><ul><li>Creating： 创建中</li><li>Running： 运行中</li><li>Isolating： 隔离中</li><li>Isolated： 已隔离</li><li>Activating： 解除隔离中</li><li>Destroying： 销毁中</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ChargeType(self):
        r"""<p>付费类型</p><p>枚举值：</p><ul><li>PREPAID： 包年包月</li></ul>
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ExpireTime(self):
        r"""<p>节点到期时间</p>
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def CreatedTime(self):
        r"""<p>节点创建时间</p>
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def IsolatedTime(self):
        r"""<p>节点隔离时间</p>
        :rtype: str
        """
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def Tags(self):
        r"""<p>节点标签信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoRenew(self):
        r"""<p>节点是否自动续费标记</p><p>枚举值：</p><ul><li>1： 自动续费</li><li>0： 不自动续费</li></ul>
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def SwitchId(self):
        r"""<p>交换机ID（已加密）</p>
        :rtype: str
        """
        return self._SwitchId

    @SwitchId.setter
    def SwitchId(self, SwitchId):
        self._SwitchId = SwitchId

    @property
    def RackId(self):
        r"""<p>机架ID（已加密）</p>
        :rtype: str
        """
        return self._RackId

    @RackId.setter
    def RackId(self, RackId):
        self._RackId = RackId

    @property
    def HostIp(self):
        r"""<p>底层物理机IP（已加密）</p>
        :rtype: str
        """
        return self._HostIp

    @HostIp.setter
    def HostIp(self, HostIp):
        self._HostIp = HostIp


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeName = params.get("NodeName")
        self._SSHEndpoint = params.get("SSHEndpoint")
        self._LanIP = params.get("LanIP")
        self._ClusterId = params.get("ClusterId")
        self._Zone = params.get("Zone")
        self._NodeType = params.get("NodeType")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        self._OsName = params.get("OsName")
        self._ImageId = params.get("ImageId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._ChargeType = params.get("ChargeType")
        self._ExpireTime = params.get("ExpireTime")
        self._CreatedTime = params.get("CreatedTime")
        self._IsolatedTime = params.get("IsolatedTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoRenew = params.get("AutoRenew")
        self._SwitchId = params.get("SwitchId")
        self._RackId = params.get("RackId")
        self._HostIp = params.get("HostIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstanceDetail(AbstractModel):
    r"""DB实例详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: DB实例Id
        :type InstanceId: str
        :param _InstanceName: DB实例名称
        :type InstanceName: str
        :param _Status: DB实例状态,-1:已隔离, 0:创建中, 1:流程中, 2:运行中, 3:未初始化
        :type Status: int
        :param _StatusDesc: DB实例状态描述,-1:已隔离, 0:创建中, 1:流程中, 2:运行中, 3:未初始化
        :type StatusDesc: str
        :param _DbVersion: DB实例版本
        :type DbVersion: str
        :param _Vip: Vip信息
        :type Vip: str
        :param _Vport: Vip使用的端口号
        :type Vport: int
        :param _UniqueVpcId: 字符串型的私有网络ID
        :type UniqueVpcId: str
        :param _UniqueSubnetId: 字符串型的私有网络子网ID
        :type UniqueSubnetId: str
        :param _Shard: 是否为分布式版本,0:否,1:是
        :type Shard: int
        :param _NodeNum: DB实例节点数
        :type NodeNum: int
        :param _Cpu: CPU规格(单位:核数)
        :type Cpu: int
        :param _Memory: 内存规格(单位:GB)
        :type Memory: int
        :param _Disk: 磁盘规格(单位:GB)
        :type Disk: int
        :param _ShardNum: 分布式类型的实例的分片数
        :type ShardNum: int
        :param _Region: 地域
        :type Region: str
        :param _Zone: 可用区
        :type Zone: str
        :param _DbHosts: Db所在主机列表, 格式: m1,s1|m2,s2
        :type DbHosts: str
        :param _HostRole: 主机角色, 1:主, 2:从, 3:主+从
        :type HostRole: int
        :param _DbEngine: DB引擎，MySQL,Percona,MariaDB
        :type DbEngine: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Zones: 可用区列表
        :type Zones: list of str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Status = None
        self._StatusDesc = None
        self._DbVersion = None
        self._Vip = None
        self._Vport = None
        self._UniqueVpcId = None
        self._UniqueSubnetId = None
        self._Shard = None
        self._NodeNum = None
        self._Cpu = None
        self._Memory = None
        self._Disk = None
        self._ShardNum = None
        self._Region = None
        self._Zone = None
        self._DbHosts = None
        self._HostRole = None
        self._DbEngine = None
        self._CreateTime = None
        self._Zones = None

    @property
    def InstanceId(self):
        r"""DB实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""DB实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Status(self):
        r"""DB实例状态,-1:已隔离, 0:创建中, 1:流程中, 2:运行中, 3:未初始化
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        r"""DB实例状态描述,-1:已隔离, 0:创建中, 1:流程中, 2:运行中, 3:未初始化
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def DbVersion(self):
        r"""DB实例版本
        :rtype: str
        """
        return self._DbVersion

    @DbVersion.setter
    def DbVersion(self, DbVersion):
        self._DbVersion = DbVersion

    @property
    def Vip(self):
        r"""Vip信息
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""Vip使用的端口号
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def UniqueVpcId(self):
        r"""字符串型的私有网络ID
        :rtype: str
        """
        return self._UniqueVpcId

    @UniqueVpcId.setter
    def UniqueVpcId(self, UniqueVpcId):
        self._UniqueVpcId = UniqueVpcId

    @property
    def UniqueSubnetId(self):
        r"""字符串型的私有网络子网ID
        :rtype: str
        """
        return self._UniqueSubnetId

    @UniqueSubnetId.setter
    def UniqueSubnetId(self, UniqueSubnetId):
        self._UniqueSubnetId = UniqueSubnetId

    @property
    def Shard(self):
        r"""是否为分布式版本,0:否,1:是
        :rtype: int
        """
        return self._Shard

    @Shard.setter
    def Shard(self, Shard):
        self._Shard = Shard

    @property
    def NodeNum(self):
        r"""DB实例节点数
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def Cpu(self):
        r"""CPU规格(单位:核数)
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        r"""内存规格(单位:GB)
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Disk(self):
        r"""磁盘规格(单位:GB)
        :rtype: int
        """
        return self._Disk

    @Disk.setter
    def Disk(self, Disk):
        self._Disk = Disk

    @property
    def ShardNum(self):
        r"""分布式类型的实例的分片数
        :rtype: int
        """
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DbHosts(self):
        r"""Db所在主机列表, 格式: m1,s1|m2,s2
        :rtype: str
        """
        return self._DbHosts

    @DbHosts.setter
    def DbHosts(self, DbHosts):
        self._DbHosts = DbHosts

    @property
    def HostRole(self):
        r"""主机角色, 1:主, 2:从, 3:主+从
        :rtype: int
        """
        return self._HostRole

    @HostRole.setter
    def HostRole(self, HostRole):
        self._HostRole = HostRole

    @property
    def DbEngine(self):
        r"""DB引擎，MySQL,Percona,MariaDB
        :rtype: str
        """
        return self._DbEngine

    @DbEngine.setter
    def DbEngine(self, DbEngine):
        self._DbEngine = DbEngine

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Zones(self):
        r"""可用区列表
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._DbVersion = params.get("DbVersion")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._UniqueVpcId = params.get("UniqueVpcId")
        self._UniqueSubnetId = params.get("UniqueSubnetId")
        self._Shard = params.get("Shard")
        self._NodeNum = params.get("NodeNum")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Disk = params.get("Disk")
        self._ShardNum = params.get("ShardNum")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._DbHosts = params.get("DbHosts")
        self._HostRole = params.get("HostRole")
        self._DbEngine = params.get("DbEngine")
        self._CreateTime = params.get("CreateTime")
        self._Zones = params.get("Zones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataDisk(AbstractModel):
    r"""DB Custom 节点数据盘信息。

    """

    def __init__(self):
        r"""
        :param _DiskType: <p>磁盘类型</p><p>枚举值：</p><ul><li>CLOUD_HSSD： 增强型云硬盘</li><li>LOCAL_NVME： 本地硬盘</li></ul>
        :type DiskType: str
        :param _DiskSize: <p>磁盘大小</p><p>单位：GiB</p>
        :type DiskSize: int
        :param _DiskName: <p>磁盘名称</p>
        :type DiskName: str
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskName = None

    @property
    def DiskType(self):
        r"""<p>磁盘类型</p><p>枚举值：</p><ul><li>CLOUD_HSSD： 增强型云硬盘</li><li>LOCAL_NVME： 本地硬盘</li></ul>
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""<p>磁盘大小</p><p>单位：GiB</p>
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskName(self):
        r"""<p>磁盘名称</p>
        :rtype: str
        """
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._DiskName = params.get("DiskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBCustomClusterDetailRequest(AbstractModel):
    r"""DescribeDBCustomClusterDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: <p>DB Custom 集群ID</p><p>入参限制：必须为此账号拥有的DB Custom集群</p>
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        r"""<p>DB Custom 集群ID</p><p>入参限制：必须为此账号拥有的DB Custom集群</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBCustomClusterDetailResponse(AbstractModel):
    r"""DescribeDBCustomClusterDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: <p>集群ID</p>
        :type ClusterId: str
        :param _ClusterName: <p>集群名称</p>
        :type ClusterName: str
        :param _ClusterDescription: <p>集群描述</p>
        :type ClusterDescription: str
        :param _Region: <p>集群所属地域</p><p>枚举值：</p><ul><li>ap-shanghai： 上海地域</li><li>ap-nanjing： 南京地域</li></ul>
        :type Region: str
        :param _ClusterStatus: <p>DB Custom 集群状态</p><p>枚举值：</p><ul><li>Creating： 创建中</li><li>Running： 运行中</li><li>Destroying： 销毁中</li></ul>
        :type ClusterStatus: str
        :param _ClusterVersion: <p>集群版本</p><p>枚举值：</p><ul><li>1.34.1： 集群版本1.34.1</li></ul><p>默认值：1.34.1</p>
        :type ClusterVersion: str
        :param _ClusterNodeNum: <p>集群下的节点数量</p>
        :type ClusterNodeNum: int
        :param _ClusterLevel: <p>集群规模</p>
        :type ClusterLevel: str
        :param _CreatedTime: <p>创建时间</p>
        :type CreatedTime: str
        :param _Tags: <p>集群标签信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _ApiServerNetwork: <p>集群的API Server的网络信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiServerNetwork: :class:`tencentcloud.dbdc.v20201029.models.ApiServerNetwork`
        :param _ContainerNetwork: <p>容器网络，在此集群中的所有Pod将与此网络连通</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerNetwork: :class:`tencentcloud.dbdc.v20201029.models.ContainerNetwork`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterId = None
        self._ClusterName = None
        self._ClusterDescription = None
        self._Region = None
        self._ClusterStatus = None
        self._ClusterVersion = None
        self._ClusterNodeNum = None
        self._ClusterLevel = None
        self._CreatedTime = None
        self._Tags = None
        self._ApiServerNetwork = None
        self._ContainerNetwork = None
        self._RequestId = None

    @property
    def ClusterId(self):
        r"""<p>集群ID</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""<p>集群名称</p>
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ClusterDescription(self):
        r"""<p>集群描述</p>
        :rtype: str
        """
        return self._ClusterDescription

    @ClusterDescription.setter
    def ClusterDescription(self, ClusterDescription):
        self._ClusterDescription = ClusterDescription

    @property
    def Region(self):
        r"""<p>集群所属地域</p><p>枚举值：</p><ul><li>ap-shanghai： 上海地域</li><li>ap-nanjing： 南京地域</li></ul>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ClusterStatus(self):
        r"""<p>DB Custom 集群状态</p><p>枚举值：</p><ul><li>Creating： 创建中</li><li>Running： 运行中</li><li>Destroying： 销毁中</li></ul>
        :rtype: str
        """
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def ClusterVersion(self):
        r"""<p>集群版本</p><p>枚举值：</p><ul><li>1.34.1： 集群版本1.34.1</li></ul><p>默认值：1.34.1</p>
        :rtype: str
        """
        return self._ClusterVersion

    @ClusterVersion.setter
    def ClusterVersion(self, ClusterVersion):
        self._ClusterVersion = ClusterVersion

    @property
    def ClusterNodeNum(self):
        r"""<p>集群下的节点数量</p>
        :rtype: int
        """
        return self._ClusterNodeNum

    @ClusterNodeNum.setter
    def ClusterNodeNum(self, ClusterNodeNum):
        self._ClusterNodeNum = ClusterNodeNum

    @property
    def ClusterLevel(self):
        r"""<p>集群规模</p>
        :rtype: str
        """
        return self._ClusterLevel

    @ClusterLevel.setter
    def ClusterLevel(self, ClusterLevel):
        self._ClusterLevel = ClusterLevel

    @property
    def CreatedTime(self):
        r"""<p>创建时间</p>
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Tags(self):
        r"""<p>集群标签信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ApiServerNetwork(self):
        r"""<p>集群的API Server的网络信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.ApiServerNetwork`
        """
        return self._ApiServerNetwork

    @ApiServerNetwork.setter
    def ApiServerNetwork(self, ApiServerNetwork):
        self._ApiServerNetwork = ApiServerNetwork

    @property
    def ContainerNetwork(self):
        r"""<p>容器网络，在此集群中的所有Pod将与此网络连通</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.ContainerNetwork`
        """
        return self._ContainerNetwork

    @ContainerNetwork.setter
    def ContainerNetwork(self, ContainerNetwork):
        self._ContainerNetwork = ContainerNetwork

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
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._ClusterDescription = params.get("ClusterDescription")
        self._Region = params.get("Region")
        self._ClusterStatus = params.get("ClusterStatus")
        self._ClusterVersion = params.get("ClusterVersion")
        self._ClusterNodeNum = params.get("ClusterNodeNum")
        self._ClusterLevel = params.get("ClusterLevel")
        self._CreatedTime = params.get("CreatedTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("ApiServerNetwork") is not None:
            self._ApiServerNetwork = ApiServerNetwork()
            self._ApiServerNetwork._deserialize(params.get("ApiServerNetwork"))
        if params.get("ContainerNetwork") is not None:
            self._ContainerNetwork = ContainerNetwork()
            self._ContainerNetwork._deserialize(params.get("ContainerNetwork"))
        self._RequestId = params.get("RequestId")


class DescribeDBCustomClusterKubeconfigRequest(AbstractModel):
    r"""DescribeDBCustomClusterKubeconfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: <p>集群ID</p><p>入参限制：必须为当前节点拥有的DB Custom 集群</p>
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        r"""<p>集群ID</p><p>入参限制：必须为当前节点拥有的DB Custom 集群</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBCustomClusterKubeconfigResponse(AbstractModel):
    r"""DescribeDBCustomClusterKubeconfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Kubeconfig: <p>集群APIServer信息</p>
        :type Kubeconfig: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Kubeconfig = None
        self._RequestId = None

    @property
    def Kubeconfig(self):
        r"""<p>集群APIServer信息</p>
        :rtype: str
        """
        return self._Kubeconfig

    @Kubeconfig.setter
    def Kubeconfig(self, Kubeconfig):
        self._Kubeconfig = Kubeconfig

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
        self._Kubeconfig = params.get("Kubeconfig")
        self._RequestId = params.get("RequestId")


class DescribeDBCustomClusterNodesRequest(AbstractModel):
    r"""DescribeDBCustomClusterNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: <p>DB Custom 集群ID</p>
        :type ClusterId: str
        :param _Filters: <p>查询筛选条件。支持的条件有：</p><ul><li>node-name：DB Custom 节点名称。</li></ul>
        :type Filters: list of Filter
        :param _Offset: <p>分页偏移量</p>
        :type Offset: int
        :param _Limit: <p>返回数量</p><p>取值范围：[1, 100]</p><p>默认值：20</p>
        :type Limit: int
        """
        self._ClusterId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        r"""<p>DB Custom 集群ID</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Filters(self):
        r"""<p>查询筛选条件。支持的条件有：</p><ul><li>node-name：DB Custom 节点名称。</li></ul>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""<p>分页偏移量</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>返回数量</p><p>取值范围：[1, 100]</p><p>默认值：20</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
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
        


class DescribeDBCustomClusterNodesResponse(AbstractModel):
    r"""DescribeDBCustomClusterNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>集群下总的节点数量</p>
        :type TotalCount: int
        :param _NodeSet: <p>分页后节点列表信息</p>
        :type NodeSet: list of DBCustomClusterNode
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._NodeSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>集群下总的节点数量</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NodeSet(self):
        r"""<p>分页后节点列表信息</p>
        :rtype: list of DBCustomClusterNode
        """
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

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
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = DBCustomClusterNode()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBCustomClustersRequest(AbstractModel):
    r"""DescribeDBCustomClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterIds: <p>按照一个或者多个 ClusterId 查询。</p><p>入参限制：每次请求的数量上限为100</p>
        :type ClusterIds: list of str
        :param _Filters: <p>查询筛选条件。支持的筛选条件包括：</p><ul><li>cluster-name：DB Custom 集群名称，精确匹配。</li><li>cluster-status：DB Custom 集群状态（Creating，Running，Destroying）。</li></ul>
        :type Filters: list of Filter
        :param _Tags: <p>根据标签的 Key 和 Value 筛选 DB Custom 集群</p>
        :type Tags: list of Tag
        :param _Offset: <p>集群列表分页偏移量</p>
        :type Offset: int
        :param _Limit: <p>返回数量</p><p>取值范围：[1, 100]</p><p>默认值：20</p>
        :type Limit: int
        """
        self._ClusterIds = None
        self._Filters = None
        self._Tags = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterIds(self):
        r"""<p>按照一个或者多个 ClusterId 查询。</p><p>入参限制：每次请求的数量上限为100</p>
        :rtype: list of str
        """
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def Filters(self):
        r"""<p>查询筛选条件。支持的筛选条件包括：</p><ul><li>cluster-name：DB Custom 集群名称，精确匹配。</li><li>cluster-status：DB Custom 集群状态（Creating，Running，Destroying）。</li></ul>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Tags(self):
        r"""<p>根据标签的 Key 和 Value 筛选 DB Custom 集群</p>
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Offset(self):
        r"""<p>集群列表分页偏移量</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>返回数量</p><p>取值范围：[1, 100]</p><p>默认值：20</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ClusterIds = params.get("ClusterIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBCustomClustersResponse(AbstractModel):
    r"""DescribeDBCustomClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>总集群数量</p>
        :type TotalCount: int
        :param _ClusterSet: <p>集群列表信息</p>
        :type ClusterSet: list of DBCustomCluster
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ClusterSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>总集群数量</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ClusterSet(self):
        r"""<p>集群列表信息</p>
        :rtype: list of DBCustomCluster
        """
        return self._ClusterSet

    @ClusterSet.setter
    def ClusterSet(self, ClusterSet):
        self._ClusterSet = ClusterSet

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
        if params.get("ClusterSet") is not None:
            self._ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = DBCustomCluster()
                obj._deserialize(item)
                self._ClusterSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBCustomImagesRequest(AbstractModel):
    r"""DescribeDBCustomImages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: <p>偏移量</p><p>默认值：0</p>
        :type Offset: int
        :param _Limit: <p>返回数量</p><p>取值范围：[1, 100]</p><p>默认值：20</p>
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        r"""<p>偏移量</p><p>默认值：0</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>返回数量</p><p>取值范围：[1, 100]</p><p>默认值：20</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBCustomImagesResponse(AbstractModel):
    r"""DescribeDBCustomImages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>总镜像数量</p>
        :type TotalCount: int
        :param _ImageSet: <p>支持的镜像列表信息</p>
        :type ImageSet: list of DBCustomImage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ImageSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>总镜像数量</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ImageSet(self):
        r"""<p>支持的镜像列表信息</p>
        :rtype: list of DBCustomImage
        """
        return self._ImageSet

    @ImageSet.setter
    def ImageSet(self, ImageSet):
        self._ImageSet = ImageSet

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
        if params.get("ImageSet") is not None:
            self._ImageSet = []
            for item in params.get("ImageSet"):
                obj = DBCustomImage()
                obj._deserialize(item)
                self._ImageSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBCustomNodesRequest(AbstractModel):
    r"""DescribeDBCustomNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeIds: <p>按照一个或者多个 NodeId 查询。</p><p>入参限制：每次请求的数量上限为100</p>
        :type NodeIds: list of str
        :param _Filters: <p>查询筛选条件。支持的筛选条件包括：</p><ul><li>cluster-id：按 DB Custom 集群进行过滤。</li><li>node-name：按 DB Custom 节点名称进行过滤，精确匹配。</li><li>status：按 DB Custom 节点状态进行过滤。（可选值：Creating，Running，Isolating，Isolated，Activating（解除隔离中），Destroying）</li><li>zone：按 DB Custom 节点所在可用区进行过滤。</li></ul>
        :type Filters: list of Filter
        :param _Tags: <p>根据标签的 Key 和 Value 筛选 DB Custom 节点</p>
        :type Tags: list of Tag
        :param _Offset: <p>分页偏移量</p>
        :type Offset: int
        :param _Limit: <p>返回数量</p><p>取值范围：[1, 100]</p><p>默认值：20</p>
        :type Limit: int
        """
        self._NodeIds = None
        self._Filters = None
        self._Tags = None
        self._Offset = None
        self._Limit = None

    @property
    def NodeIds(self):
        r"""<p>按照一个或者多个 NodeId 查询。</p><p>入参限制：每次请求的数量上限为100</p>
        :rtype: list of str
        """
        return self._NodeIds

    @NodeIds.setter
    def NodeIds(self, NodeIds):
        self._NodeIds = NodeIds

    @property
    def Filters(self):
        r"""<p>查询筛选条件。支持的筛选条件包括：</p><ul><li>cluster-id：按 DB Custom 集群进行过滤。</li><li>node-name：按 DB Custom 节点名称进行过滤，精确匹配。</li><li>status：按 DB Custom 节点状态进行过滤。（可选值：Creating，Running，Isolating，Isolated，Activating（解除隔离中），Destroying）</li><li>zone：按 DB Custom 节点所在可用区进行过滤。</li></ul>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Tags(self):
        r"""<p>根据标签的 Key 和 Value 筛选 DB Custom 节点</p>
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Offset(self):
        r"""<p>分页偏移量</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>返回数量</p><p>取值范围：[1, 100]</p><p>默认值：20</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._NodeIds = params.get("NodeIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBCustomNodesResponse(AbstractModel):
    r"""DescribeDBCustomNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>当前账号下拥有的DB Custom 节点总数</p>
        :type TotalCount: int
        :param _NodeSet: <p>当前账号下拥有的DB Custom 节点列表信息</p>
        :type NodeSet: list of DBCustomNode
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._NodeSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>当前账号下拥有的DB Custom 节点总数</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NodeSet(self):
        r"""<p>当前账号下拥有的DB Custom 节点列表信息</p>
        :rtype: list of DBCustomNode
        """
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

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
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = DBCustomNode()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBCustomTaskStatusRequest(AbstractModel):
    r"""DescribeDBCustomTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>DB Custom 任务ID</p>
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""<p>DB Custom 任务ID</p>
        :rtype: int
        """
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
        


class DescribeDBCustomTaskStatusResponse(AbstractModel):
    r"""DescribeDBCustomTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: <p>任务 ID</p><p>枚举值：</p><ul><li>Running： 运行中</li><li>Succeeded： 成功</li><li>Failed： 失败</li></ul>
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""<p>任务 ID</p><p>枚举值：</p><ul><li>Running： 运行中</li><li>Succeeded： 成功</li><li>Failed： 失败</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    r"""DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 独享集群实例Id
        :type InstanceId: str
        :param _HostId: 独享集群主机Id
        :type HostId: str
        :param _Limit: 分页返回数量
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _ShardType: 实例类型,0:mariadb, 1:tdsql
        :type ShardType: list of int
        """
        self._InstanceId = None
        self._HostId = None
        self._Limit = None
        self._Offset = None
        self._ShardType = None

    @property
    def InstanceId(self):
        r"""独享集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def HostId(self):
        r"""独享集群主机Id
        :rtype: str
        """
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId

    @property
    def Limit(self):
        r"""分页返回数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ShardType(self):
        r"""实例类型,0:mariadb, 1:tdsql
        :rtype: list of int
        """
        return self._ShardType

    @ShardType.setter
    def ShardType(self, ShardType):
        self._ShardType = ShardType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._HostId = params.get("HostId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ShardType = params.get("ShardType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesResponse(AbstractModel):
    r"""DescribeDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instances: 独享集群内的DB实例列表
        :type Instances: list of DBInstanceDetail
        :param _TotalCount: 独享集群内的DB实例总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instances = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Instances(self):
        r"""独享集群内的DB实例列表
        :rtype: list of DBInstanceDetail
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def TotalCount(self):
        r"""独享集群内的DB实例总数
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
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = DBInstanceDetail()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostListRequest(AbstractModel):
    r"""DescribeHostList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 独享集群实例Id
        :type InstanceId: str
        :param _Limit: 分页返回数量
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _AssignStatus: 分配状态过滤，0-可分配，1-禁止分配
        :type AssignStatus: list of int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._AssignStatus = None

    @property
    def InstanceId(self):
        r"""独享集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        r"""分页返回数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def AssignStatus(self):
        r"""分配状态过滤，0-可分配，1-禁止分配
        :rtype: list of int
        """
        return self._AssignStatus

    @AssignStatus.setter
    def AssignStatus(self, AssignStatus):
        self._AssignStatus = AssignStatus


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._AssignStatus = params.get("AssignStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostListResponse(AbstractModel):
    r"""DescribeHostList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 主机总数
        :type TotalCount: int
        :param _Hosts: 主机详情
        :type Hosts: list of HostDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Hosts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""主机总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Hosts(self):
        r"""主机详情
        :rtype: list of HostDetail
        """
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

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
        if params.get("Hosts") is not None:
            self._Hosts = []
            for item in params.get("Hosts"):
                obj = HostDetail()
                obj._deserialize(item)
                self._Hosts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceDetail(AbstractModel):
    r"""独享集群详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: 独享集群实例Id
        :type InstanceId: str
        :param _InstanceName: 独享集群实例名称
        :type InstanceName: str
        :param _Region: 地域
        :type Region: str
        :param _ProductId: 产品ID, 0:CDB, 1:TDSQL
        :type ProductId: int
        :param _Type: 集群类型, 0:公有云, 1:金融围笼, 2:CDC集群
        :type Type: int
        :param _HostType: 主机类型, 0:物理机, 1:CVM机型, 2:CDC机型
        :type HostType: int
        :param _AutoRenewFlag: 自动续费标志, 0:未设置, 1:自动续费, 2:到期不续费
        :type AutoRenewFlag: int
        :param _Status: 集群状态
        :type Status: int
        :param _StatusDesc: 集群状态描述
        :type StatusDesc: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _PeriodEndTime: 到期时间
        :type PeriodEndTime: str
        :param _HostNum: 主机数
        :type HostNum: int
        :param _DbNum: DB实例数
        :type DbNum: int
        :param _AssignStrategy: 分配策略, 0:紧凑, 1:均匀
        :type AssignStrategy: int
        :param _CpuSpec: 总主机CPU(单位:核数)
        :type CpuSpec: int
        :param _CpuAssigned: 总已分配CPU(单位:核数)
        :type CpuAssigned: int
        :param _CpuAssignable: 总可分配CPU(单位:核数)
        :type CpuAssignable: int
        :param _MemorySpec: 总主机内存(单位:GB)
        :type MemorySpec: int
        :param _MemoryAssigned: 总已分配内存(单位:GB)
        :type MemoryAssigned: int
        :param _MemoryAssignable: 总可分配内存(单位:GB)
        :type MemoryAssignable: int
        :param _DiskSpec: 总机器磁盘(单位:GB)
        :type DiskSpec: int
        :param _DiskAssigned: 总已分配磁盘(单位:GB)
        :type DiskAssigned: int
        :param _DiskAssignable: 总可分配磁盘(单位:GB)
        :type DiskAssignable: int
        :param _Zone: 可用区
        :type Zone: str
        :param _FenceId: 金融围笼ID
        :type FenceId: str
        :param _ClusterId: 所属集群ID(默认集群为空)
        :type ClusterId: str
        :param _ResourceTags: 实例标签
        :type ResourceTags: list of ResourceTag
        :param _CpuType: CPU类型：Intel/AMD,Hygon
        :type CpuType: str
        :param _Zones: 可用区列表
        :type Zones: list of str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None
        self._ProductId = None
        self._Type = None
        self._HostType = None
        self._AutoRenewFlag = None
        self._Status = None
        self._StatusDesc = None
        self._CreateTime = None
        self._PeriodEndTime = None
        self._HostNum = None
        self._DbNum = None
        self._AssignStrategy = None
        self._CpuSpec = None
        self._CpuAssigned = None
        self._CpuAssignable = None
        self._MemorySpec = None
        self._MemoryAssigned = None
        self._MemoryAssignable = None
        self._DiskSpec = None
        self._DiskAssigned = None
        self._DiskAssignable = None
        self._Zone = None
        self._FenceId = None
        self._ClusterId = None
        self._ResourceTags = None
        self._CpuType = None
        self._Zones = None

    @property
    def InstanceId(self):
        r"""独享集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""独享集群实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ProductId(self):
        r"""产品ID, 0:CDB, 1:TDSQL
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Type(self):
        r"""集群类型, 0:公有云, 1:金融围笼, 2:CDC集群
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def HostType(self):
        r"""主机类型, 0:物理机, 1:CVM机型, 2:CDC机型
        :rtype: int
        """
        return self._HostType

    @HostType.setter
    def HostType(self, HostType):
        self._HostType = HostType

    @property
    def AutoRenewFlag(self):
        r"""自动续费标志, 0:未设置, 1:自动续费, 2:到期不续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Status(self):
        r"""集群状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        r"""集群状态描述
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PeriodEndTime(self):
        r"""到期时间
        :rtype: str
        """
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def HostNum(self):
        r"""主机数
        :rtype: int
        """
        return self._HostNum

    @HostNum.setter
    def HostNum(self, HostNum):
        self._HostNum = HostNum

    @property
    def DbNum(self):
        r"""DB实例数
        :rtype: int
        """
        return self._DbNum

    @DbNum.setter
    def DbNum(self, DbNum):
        self._DbNum = DbNum

    @property
    def AssignStrategy(self):
        r"""分配策略, 0:紧凑, 1:均匀
        :rtype: int
        """
        return self._AssignStrategy

    @AssignStrategy.setter
    def AssignStrategy(self, AssignStrategy):
        self._AssignStrategy = AssignStrategy

    @property
    def CpuSpec(self):
        r"""总主机CPU(单位:核数)
        :rtype: int
        """
        return self._CpuSpec

    @CpuSpec.setter
    def CpuSpec(self, CpuSpec):
        self._CpuSpec = CpuSpec

    @property
    def CpuAssigned(self):
        r"""总已分配CPU(单位:核数)
        :rtype: int
        """
        return self._CpuAssigned

    @CpuAssigned.setter
    def CpuAssigned(self, CpuAssigned):
        self._CpuAssigned = CpuAssigned

    @property
    def CpuAssignable(self):
        r"""总可分配CPU(单位:核数)
        :rtype: int
        """
        return self._CpuAssignable

    @CpuAssignable.setter
    def CpuAssignable(self, CpuAssignable):
        self._CpuAssignable = CpuAssignable

    @property
    def MemorySpec(self):
        r"""总主机内存(单位:GB)
        :rtype: int
        """
        return self._MemorySpec

    @MemorySpec.setter
    def MemorySpec(self, MemorySpec):
        self._MemorySpec = MemorySpec

    @property
    def MemoryAssigned(self):
        r"""总已分配内存(单位:GB)
        :rtype: int
        """
        return self._MemoryAssigned

    @MemoryAssigned.setter
    def MemoryAssigned(self, MemoryAssigned):
        self._MemoryAssigned = MemoryAssigned

    @property
    def MemoryAssignable(self):
        r"""总可分配内存(单位:GB)
        :rtype: int
        """
        return self._MemoryAssignable

    @MemoryAssignable.setter
    def MemoryAssignable(self, MemoryAssignable):
        self._MemoryAssignable = MemoryAssignable

    @property
    def DiskSpec(self):
        r"""总机器磁盘(单位:GB)
        :rtype: int
        """
        return self._DiskSpec

    @DiskSpec.setter
    def DiskSpec(self, DiskSpec):
        self._DiskSpec = DiskSpec

    @property
    def DiskAssigned(self):
        r"""总已分配磁盘(单位:GB)
        :rtype: int
        """
        return self._DiskAssigned

    @DiskAssigned.setter
    def DiskAssigned(self, DiskAssigned):
        self._DiskAssigned = DiskAssigned

    @property
    def DiskAssignable(self):
        r"""总可分配磁盘(单位:GB)
        :rtype: int
        """
        return self._DiskAssignable

    @DiskAssignable.setter
    def DiskAssignable(self, DiskAssignable):
        self._DiskAssignable = DiskAssignable

    @property
    def Zone(self):
        r"""可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def FenceId(self):
        r"""金融围笼ID
        :rtype: str
        """
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

    @property
    def ClusterId(self):
        r"""所属集群ID(默认集群为空)
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ResourceTags(self):
        r"""实例标签
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def CpuType(self):
        r"""CPU类型：Intel/AMD,Hygon
        :rtype: str
        """
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def Zones(self):
        r"""可用区列表
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        self._ProductId = params.get("ProductId")
        self._Type = params.get("Type")
        self._HostType = params.get("HostType")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._CreateTime = params.get("CreateTime")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._HostNum = params.get("HostNum")
        self._DbNum = params.get("DbNum")
        self._AssignStrategy = params.get("AssignStrategy")
        self._CpuSpec = params.get("CpuSpec")
        self._CpuAssigned = params.get("CpuAssigned")
        self._CpuAssignable = params.get("CpuAssignable")
        self._MemorySpec = params.get("MemorySpec")
        self._MemoryAssigned = params.get("MemoryAssigned")
        self._MemoryAssignable = params.get("MemoryAssignable")
        self._DiskSpec = params.get("DiskSpec")
        self._DiskAssigned = params.get("DiskAssigned")
        self._DiskAssignable = params.get("DiskAssignable")
        self._Zone = params.get("Zone")
        self._FenceId = params.get("FenceId")
        self._ClusterId = params.get("ClusterId")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._CpuType = params.get("CpuType")
        self._Zones = params.get("Zones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDetailRequest(AbstractModel):
    r"""DescribeInstanceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 独享集群实例Id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""独享集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDetailResponse(AbstractModel):
    r"""DescribeInstanceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 独享集群实例Id
        :type InstanceId: str
        :param _InstanceName: 独享集群实例名称
        :type InstanceName: str
        :param _Region: 地域
        :type Region: str
        :param _ProductId: 产品ID, 0:CDB, 1:TDSQL
        :type ProductId: int
        :param _Type: 集群类型, 0:公有云, 1:金融围笼
        :type Type: int
        :param _HostType: 主机类型, 0:物理机, 1:cvm本地盘, 2:cvm云盘
        :type HostType: int
        :param _AutoRenewFlag: 自动续费标志, 0:未设置, 1:自动续费, 2:到期不续费
        :type AutoRenewFlag: int
        :param _Status: 集群状态
        :type Status: int
        :param _StatusDesc: 集群状态描述
        :type StatusDesc: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _PeriodEndTime: 到期时间
        :type PeriodEndTime: str
        :param _HostNum: 主机数
        :type HostNum: int
        :param _DbNum: Db实例数
        :type DbNum: int
        :param _AssignStrategy: 分配策略, 0:紧凑, 1:均匀
        :type AssignStrategy: int
        :param _CpuSpec: 总主机CPU(单位:核)
        :type CpuSpec: int
        :param _CpuAssigned: 总已分配CPU(单位:核)
        :type CpuAssigned: int
        :param _CpuAssignable: 总可分配CPU(单位:核)
        :type CpuAssignable: int
        :param _MemorySpec: 总主机内存(单位:GB)
        :type MemorySpec: int
        :param _MemoryAssigned: 总已分配内存(单位:GB)
        :type MemoryAssigned: int
        :param _MemoryAssignable: 总可分配内存(单位:GB)
        :type MemoryAssignable: int
        :param _DiskSpec: 总机器磁盘(单位:GB)
        :type DiskSpec: int
        :param _DiskAssigned: 总已分配磁盘(单位:GB)
        :type DiskAssigned: int
        :param _DiskAssignable: 总可分配磁盘(单位:GB)
        :type DiskAssignable: int
        :param _Zone: 可用区
        :type Zone: str
        :param _FenceId: 金融围笼ID
        :type FenceId: str
        :param _ClusterId: 所属集群ID(默认集群为空)
        :type ClusterId: str
        :param _ResourceTags: 独享集群的标签信息
        :type ResourceTags: list of ResourceTag
        :param _CpuType: CPU类型，Intel/AMD,Hygon
        :type CpuType: str
        :param _Zones: 可用区列表
        :type Zones: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None
        self._ProductId = None
        self._Type = None
        self._HostType = None
        self._AutoRenewFlag = None
        self._Status = None
        self._StatusDesc = None
        self._CreateTime = None
        self._PeriodEndTime = None
        self._HostNum = None
        self._DbNum = None
        self._AssignStrategy = None
        self._CpuSpec = None
        self._CpuAssigned = None
        self._CpuAssignable = None
        self._MemorySpec = None
        self._MemoryAssigned = None
        self._MemoryAssignable = None
        self._DiskSpec = None
        self._DiskAssigned = None
        self._DiskAssignable = None
        self._Zone = None
        self._FenceId = None
        self._ClusterId = None
        self._ResourceTags = None
        self._CpuType = None
        self._Zones = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""独享集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""独享集群实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ProductId(self):
        r"""产品ID, 0:CDB, 1:TDSQL
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Type(self):
        r"""集群类型, 0:公有云, 1:金融围笼
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def HostType(self):
        r"""主机类型, 0:物理机, 1:cvm本地盘, 2:cvm云盘
        :rtype: int
        """
        return self._HostType

    @HostType.setter
    def HostType(self, HostType):
        self._HostType = HostType

    @property
    def AutoRenewFlag(self):
        r"""自动续费标志, 0:未设置, 1:自动续费, 2:到期不续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Status(self):
        r"""集群状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        r"""集群状态描述
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PeriodEndTime(self):
        r"""到期时间
        :rtype: str
        """
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def HostNum(self):
        r"""主机数
        :rtype: int
        """
        return self._HostNum

    @HostNum.setter
    def HostNum(self, HostNum):
        self._HostNum = HostNum

    @property
    def DbNum(self):
        r"""Db实例数
        :rtype: int
        """
        return self._DbNum

    @DbNum.setter
    def DbNum(self, DbNum):
        self._DbNum = DbNum

    @property
    def AssignStrategy(self):
        r"""分配策略, 0:紧凑, 1:均匀
        :rtype: int
        """
        return self._AssignStrategy

    @AssignStrategy.setter
    def AssignStrategy(self, AssignStrategy):
        self._AssignStrategy = AssignStrategy

    @property
    def CpuSpec(self):
        r"""总主机CPU(单位:核)
        :rtype: int
        """
        return self._CpuSpec

    @CpuSpec.setter
    def CpuSpec(self, CpuSpec):
        self._CpuSpec = CpuSpec

    @property
    def CpuAssigned(self):
        r"""总已分配CPU(单位:核)
        :rtype: int
        """
        return self._CpuAssigned

    @CpuAssigned.setter
    def CpuAssigned(self, CpuAssigned):
        self._CpuAssigned = CpuAssigned

    @property
    def CpuAssignable(self):
        r"""总可分配CPU(单位:核)
        :rtype: int
        """
        return self._CpuAssignable

    @CpuAssignable.setter
    def CpuAssignable(self, CpuAssignable):
        self._CpuAssignable = CpuAssignable

    @property
    def MemorySpec(self):
        r"""总主机内存(单位:GB)
        :rtype: int
        """
        return self._MemorySpec

    @MemorySpec.setter
    def MemorySpec(self, MemorySpec):
        self._MemorySpec = MemorySpec

    @property
    def MemoryAssigned(self):
        r"""总已分配内存(单位:GB)
        :rtype: int
        """
        return self._MemoryAssigned

    @MemoryAssigned.setter
    def MemoryAssigned(self, MemoryAssigned):
        self._MemoryAssigned = MemoryAssigned

    @property
    def MemoryAssignable(self):
        r"""总可分配内存(单位:GB)
        :rtype: int
        """
        return self._MemoryAssignable

    @MemoryAssignable.setter
    def MemoryAssignable(self, MemoryAssignable):
        self._MemoryAssignable = MemoryAssignable

    @property
    def DiskSpec(self):
        r"""总机器磁盘(单位:GB)
        :rtype: int
        """
        return self._DiskSpec

    @DiskSpec.setter
    def DiskSpec(self, DiskSpec):
        self._DiskSpec = DiskSpec

    @property
    def DiskAssigned(self):
        r"""总已分配磁盘(单位:GB)
        :rtype: int
        """
        return self._DiskAssigned

    @DiskAssigned.setter
    def DiskAssigned(self, DiskAssigned):
        self._DiskAssigned = DiskAssigned

    @property
    def DiskAssignable(self):
        r"""总可分配磁盘(单位:GB)
        :rtype: int
        """
        return self._DiskAssignable

    @DiskAssignable.setter
    def DiskAssignable(self, DiskAssignable):
        self._DiskAssignable = DiskAssignable

    @property
    def Zone(self):
        r"""可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def FenceId(self):
        r"""金融围笼ID
        :rtype: str
        """
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

    @property
    def ClusterId(self):
        r"""所属集群ID(默认集群为空)
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ResourceTags(self):
        r"""独享集群的标签信息
        :rtype: list of ResourceTag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def CpuType(self):
        r"""CPU类型，Intel/AMD,Hygon
        :rtype: str
        """
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def Zones(self):
        r"""可用区列表
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

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
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        self._ProductId = params.get("ProductId")
        self._Type = params.get("Type")
        self._HostType = params.get("HostType")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._CreateTime = params.get("CreateTime")
        self._PeriodEndTime = params.get("PeriodEndTime")
        self._HostNum = params.get("HostNum")
        self._DbNum = params.get("DbNum")
        self._AssignStrategy = params.get("AssignStrategy")
        self._CpuSpec = params.get("CpuSpec")
        self._CpuAssigned = params.get("CpuAssigned")
        self._CpuAssignable = params.get("CpuAssignable")
        self._MemorySpec = params.get("MemorySpec")
        self._MemoryAssigned = params.get("MemoryAssigned")
        self._MemoryAssignable = params.get("MemoryAssignable")
        self._DiskSpec = params.get("DiskSpec")
        self._DiskAssigned = params.get("DiskAssigned")
        self._DiskAssignable = params.get("DiskAssignable")
        self._Zone = params.get("Zone")
        self._FenceId = params.get("FenceId")
        self._ClusterId = params.get("ClusterId")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._CpuType = params.get("CpuType")
        self._Zones = params.get("Zones")
        self._RequestId = params.get("RequestId")


class DescribeInstanceListRequest(AbstractModel):
    r"""DescribeInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页返回数量
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _OrderBy: 排序字段，createTime,instancename两者之一
        :type OrderBy: str
        :param _SortBy: 排序规则，desc,asc两者之一
        :type SortBy: str
        :param _ProductId: 按产品过滤，0:CDB, 1:TDSQL
        :type ProductId: list of int
        :param _InstanceId: 按实例ID过滤
        :type InstanceId: list of str
        :param _InstanceName: 按实例名称过滤
        :type InstanceName: list of str
        :param _FenceId: 按金融围笼ID过滤
        :type FenceId: list of str
        :param _Status: 按实例状态过滤, -1:已隔离, 0:创建中, 1:运行中, 2:扩容中, 3:删除中
        :type Status: list of int
        :param _ClusterId: 按所属集群ID过滤
        :type ClusterId: list of str
        """
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._SortBy = None
        self._ProductId = None
        self._InstanceId = None
        self._InstanceName = None
        self._FenceId = None
        self._Status = None
        self._ClusterId = None

    @property
    def Limit(self):
        r"""分页返回数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""排序字段，createTime,instancename两者之一
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def SortBy(self):
        r"""排序规则，desc,asc两者之一
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def ProductId(self):
        r"""按产品过滤，0:CDB, 1:TDSQL
        :rtype: list of int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def InstanceId(self):
        r"""按实例ID过滤
        :rtype: list of str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""按实例名称过滤
        :rtype: list of str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def FenceId(self):
        r"""按金融围笼ID过滤
        :rtype: list of str
        """
        return self._FenceId

    @FenceId.setter
    def FenceId(self, FenceId):
        self._FenceId = FenceId

    @property
    def Status(self):
        r"""按实例状态过滤, -1:已隔离, 0:创建中, 1:运行中, 2:扩容中, 3:删除中
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ClusterId(self):
        r"""按所属集群ID过滤
        :rtype: list of str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._SortBy = params.get("SortBy")
        self._ProductId = params.get("ProductId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._FenceId = params.get("FenceId")
        self._Status = params.get("Status")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceListResponse(AbstractModel):
    r"""DescribeInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instances: 独享集群列表
        :type Instances: list of DescribeInstanceDetail
        :param _TotalCount: 独享集群实例总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instances = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Instances(self):
        r"""独享集群列表
        :rtype: list of DescribeInstanceDetail
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def TotalCount(self):
        r"""独享集群实例总数
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
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = DescribeInstanceDetail()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    r"""DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceTypes: 集群类型: 0 一主一备, 1 一主两备...N-1 一主N备
        :type InstanceTypes: list of int
        :param _ProductIds: 产品ID:  0 MYSQL，1 TDSQL
        :type ProductIds: list of int
        :param _InstanceIds: 集群uuid: 如 dbdc-q810131s
        :type InstanceIds: list of str
        :param _FenceFlag: 是否按金融围笼标志搜索
        :type FenceFlag: bool
        :param _InstanceName: 按实例名字模糊匹配
        :type InstanceName: str
        :param _PageSize: 每页数目, 整型
        :type PageSize: int
        :param _PageNumber: 页码, 整型
        :type PageNumber: int
        :param _OrderBy: 排序字段，枚举：createtime,groupname
        :type OrderBy: str
        :param _OrderByType: 排序方式: asc升序, desc降序
        :type OrderByType: str
        :param _InstanceStatus: 集群状态: -2 已删除, -1 已隔离, 0 创建中, 1 运行中, 2 扩容中, 3 删除中
        :type InstanceStatus: int
        """
        self._InstanceTypes = None
        self._ProductIds = None
        self._InstanceIds = None
        self._FenceFlag = None
        self._InstanceName = None
        self._PageSize = None
        self._PageNumber = None
        self._OrderBy = None
        self._OrderByType = None
        self._InstanceStatus = None

    @property
    def InstanceTypes(self):
        r"""集群类型: 0 一主一备, 1 一主两备...N-1 一主N备
        :rtype: list of int
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def ProductIds(self):
        r"""产品ID:  0 MYSQL，1 TDSQL
        :rtype: list of int
        """
        return self._ProductIds

    @ProductIds.setter
    def ProductIds(self, ProductIds):
        self._ProductIds = ProductIds

    @property
    def InstanceIds(self):
        r"""集群uuid: 如 dbdc-q810131s
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def FenceFlag(self):
        r"""是否按金融围笼标志搜索
        :rtype: bool
        """
        return self._FenceFlag

    @FenceFlag.setter
    def FenceFlag(self, FenceFlag):
        self._FenceFlag = FenceFlag

    @property
    def InstanceName(self):
        r"""按实例名字模糊匹配
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PageSize(self):
        r"""每页数目, 整型
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""页码, 整型
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def OrderBy(self):
        r"""排序字段，枚举：createtime,groupname
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""排序方式: asc升序, desc降序
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def InstanceStatus(self):
        r"""集群状态: -2 已删除, -1 已隔离, 0 创建中, 1 运行中, 2 扩容中, 3 删除中
        :rtype: int
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus


    def _deserialize(self, params):
        self._InstanceTypes = params.get("InstanceTypes")
        self._ProductIds = params.get("ProductIds")
        self._InstanceIds = params.get("InstanceIds")
        self._FenceFlag = params.get("FenceFlag")
        self._InstanceName = params.get("InstanceName")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._InstanceStatus = params.get("InstanceStatus")
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
        :param _TotalCount: 集群数量
        :type TotalCount: int
        :param _Instances: 集群扩展信息
        :type Instances: list of InstanceExpand
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Instances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""集群数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Instances(self):
        r"""集群扩展信息
        :rtype: list of InstanceExpand
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

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
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = InstanceExpand()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyDBCustomClusterRequest(AbstractModel):
    r"""DestroyDBCustomCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: <p>待销毁的集群ID</p><p>入参限制：待销毁的集群必须无任何节点在此集群中。</p>
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        r"""<p>待销毁的集群ID</p><p>入参限制：待销毁的集群必须无任何节点在此集群中。</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyDBCustomClusterResponse(AbstractModel):
    r"""DestroyDBCustomCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>销毁集群的任务ID</p>
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>销毁集群的任务ID</p>
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DestroyDBCustomNodeRequest(AbstractModel):
    r"""DestroyDBCustomNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeId: <p>DB Custom 节点ID</p>
        :type NodeId: str
        """
        self._NodeId = None

    @property
    def NodeId(self):
        r"""<p>DB Custom 节点ID</p>
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyDBCustomNodeResponse(AbstractModel):
    r"""DestroyDBCustomNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>任务ID</p>
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>任务ID</p>
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeviceInfo(AbstractModel):
    r"""设备信息

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
        :type DeviceId: int
        :param _DeviceNo: 设备No
        :type DeviceNo: str
        :param _DevClass: 设备类型
        :type DevClass: str
        :param _MaxMemory: 设备总内存，单位GB
        :type MaxMemory: float
        :param _MaxDisk: 设备总磁盘，单位GB
        :type MaxDisk: float
        :param _RestMemory: 设备剩余内存，单位GB
        :type RestMemory: float
        :param _RestDisk: 设备剩余磁盘，单位GB
        :type RestDisk: float
        :param _RawDeviceNum: 设备机器个数
        :type RawDeviceNum: int
        :param _InstanceNum: 数据库实例个数
        :type InstanceNum: int
        """
        self._DeviceId = None
        self._DeviceNo = None
        self._DevClass = None
        self._MaxMemory = None
        self._MaxDisk = None
        self._RestMemory = None
        self._RestDisk = None
        self._RawDeviceNum = None
        self._InstanceNum = None

    @property
    def DeviceId(self):
        r"""设备ID
        :rtype: int
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceNo(self):
        r"""设备No
        :rtype: str
        """
        return self._DeviceNo

    @DeviceNo.setter
    def DeviceNo(self, DeviceNo):
        self._DeviceNo = DeviceNo

    @property
    def DevClass(self):
        r"""设备类型
        :rtype: str
        """
        return self._DevClass

    @DevClass.setter
    def DevClass(self, DevClass):
        self._DevClass = DevClass

    @property
    def MaxMemory(self):
        r"""设备总内存，单位GB
        :rtype: float
        """
        return self._MaxMemory

    @MaxMemory.setter
    def MaxMemory(self, MaxMemory):
        self._MaxMemory = MaxMemory

    @property
    def MaxDisk(self):
        r"""设备总磁盘，单位GB
        :rtype: float
        """
        return self._MaxDisk

    @MaxDisk.setter
    def MaxDisk(self, MaxDisk):
        self._MaxDisk = MaxDisk

    @property
    def RestMemory(self):
        r"""设备剩余内存，单位GB
        :rtype: float
        """
        return self._RestMemory

    @RestMemory.setter
    def RestMemory(self, RestMemory):
        self._RestMemory = RestMemory

    @property
    def RestDisk(self):
        r"""设备剩余磁盘，单位GB
        :rtype: float
        """
        return self._RestDisk

    @RestDisk.setter
    def RestDisk(self, RestDisk):
        self._RestDisk = RestDisk

    @property
    def RawDeviceNum(self):
        r"""设备机器个数
        :rtype: int
        """
        return self._RawDeviceNum

    @RawDeviceNum.setter
    def RawDeviceNum(self, RawDeviceNum):
        self._RawDeviceNum = RawDeviceNum

    @property
    def InstanceNum(self):
        r"""数据库实例个数
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceNo = params.get("DeviceNo")
        self._DevClass = params.get("DevClass")
        self._MaxMemory = params.get("MaxMemory")
        self._MaxDisk = params.get("MaxDisk")
        self._RestMemory = params.get("RestMemory")
        self._RestDisk = params.get("RestDisk")
        self._RawDeviceNum = params.get("RawDeviceNum")
        self._InstanceNum = params.get("InstanceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""描述键值对过滤器，用于条件过滤查询。

    """

    def __init__(self):
        r"""
        :param _Name: <p>筛选条件</p>
        :type Name: str
        :param _Values: <p>过滤字段对应的参数值</p>
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""<p>筛选条件</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""<p>过滤字段对应的参数值</p>
        :rtype: list of str
        """
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
        


class HostDetail(AbstractModel):
    r"""主机详情

    """

    def __init__(self):
        r"""
        :param _HostId: 主机Id
        :type HostId: str
        :param _HostName: 主机名称
        :type HostName: str
        :param _Zone: 可用区
        :type Zone: str
        :param _Status: 主机状态
        :type Status: int
        :param _AssignStatus: 分配DB实例状态,0:可分配,1:不可分配
        :type AssignStatus: int
        :param _HostType: 主机类型, 0:物理机, 1:cvm本地盘, 2:cvm云盘
        :type HostType: int
        :param _DbNum: DB实例数
        :type DbNum: int
        :param _CpuSpec: 主机CPU(单位:核数)
        :type CpuSpec: int
        :param _CpuAssigned: 已分配CPU(单位:核数)
        :type CpuAssigned: int
        :param _CpuAssignable: 可分配CPU(单位:核数)
        :type CpuAssignable: int
        :param _MemorySpec: 主机内存(单位:GB)
        :type MemorySpec: int
        :param _MemoryAssigned: 已分配内存(单位:GB)
        :type MemoryAssigned: int
        :param _MemoryAssignable: 可分配内存(单位:GB)
        :type MemoryAssignable: int
        :param _DiskSpec: 主机磁盘(单位:GB)
        :type DiskSpec: int
        :param _DiskAssigned: 已分配磁盘(单位:GB)
        :type DiskAssigned: int
        :param _DiskAssignable: 可分配磁盘(GB)
        :type DiskAssignable: int
        :param _CpuRatio: CPU分配比
        :type CpuRatio: float
        :param _MemoryRatio: 内存分配比
        :type MemoryRatio: float
        :param _DiskRatio: 磁盘分配比
        :type DiskRatio: float
        :param _MachineName: 机型名称
        :type MachineName: str
        :param _MachineType: 机型类别
        :type MachineType: str
        :param _PidTag: 计费标签
        :type PidTag: str
        :param _Pid: 计费ID
        :type Pid: int
        :param _InstanceId: 独享集群实例Id
        :type InstanceId: str
        :param _Zones: 可用区列表
        :type Zones: list of str
        """
        self._HostId = None
        self._HostName = None
        self._Zone = None
        self._Status = None
        self._AssignStatus = None
        self._HostType = None
        self._DbNum = None
        self._CpuSpec = None
        self._CpuAssigned = None
        self._CpuAssignable = None
        self._MemorySpec = None
        self._MemoryAssigned = None
        self._MemoryAssignable = None
        self._DiskSpec = None
        self._DiskAssigned = None
        self._DiskAssignable = None
        self._CpuRatio = None
        self._MemoryRatio = None
        self._DiskRatio = None
        self._MachineName = None
        self._MachineType = None
        self._PidTag = None
        self._Pid = None
        self._InstanceId = None
        self._Zones = None

    @property
    def HostId(self):
        r"""主机Id
        :rtype: str
        """
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId

    @property
    def HostName(self):
        r"""主机名称
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def Zone(self):
        r"""可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Status(self):
        r"""主机状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AssignStatus(self):
        r"""分配DB实例状态,0:可分配,1:不可分配
        :rtype: int
        """
        return self._AssignStatus

    @AssignStatus.setter
    def AssignStatus(self, AssignStatus):
        self._AssignStatus = AssignStatus

    @property
    def HostType(self):
        r"""主机类型, 0:物理机, 1:cvm本地盘, 2:cvm云盘
        :rtype: int
        """
        return self._HostType

    @HostType.setter
    def HostType(self, HostType):
        self._HostType = HostType

    @property
    def DbNum(self):
        r"""DB实例数
        :rtype: int
        """
        return self._DbNum

    @DbNum.setter
    def DbNum(self, DbNum):
        self._DbNum = DbNum

    @property
    def CpuSpec(self):
        r"""主机CPU(单位:核数)
        :rtype: int
        """
        return self._CpuSpec

    @CpuSpec.setter
    def CpuSpec(self, CpuSpec):
        self._CpuSpec = CpuSpec

    @property
    def CpuAssigned(self):
        r"""已分配CPU(单位:核数)
        :rtype: int
        """
        return self._CpuAssigned

    @CpuAssigned.setter
    def CpuAssigned(self, CpuAssigned):
        self._CpuAssigned = CpuAssigned

    @property
    def CpuAssignable(self):
        r"""可分配CPU(单位:核数)
        :rtype: int
        """
        return self._CpuAssignable

    @CpuAssignable.setter
    def CpuAssignable(self, CpuAssignable):
        self._CpuAssignable = CpuAssignable

    @property
    def MemorySpec(self):
        r"""主机内存(单位:GB)
        :rtype: int
        """
        return self._MemorySpec

    @MemorySpec.setter
    def MemorySpec(self, MemorySpec):
        self._MemorySpec = MemorySpec

    @property
    def MemoryAssigned(self):
        r"""已分配内存(单位:GB)
        :rtype: int
        """
        return self._MemoryAssigned

    @MemoryAssigned.setter
    def MemoryAssigned(self, MemoryAssigned):
        self._MemoryAssigned = MemoryAssigned

    @property
    def MemoryAssignable(self):
        r"""可分配内存(单位:GB)
        :rtype: int
        """
        return self._MemoryAssignable

    @MemoryAssignable.setter
    def MemoryAssignable(self, MemoryAssignable):
        self._MemoryAssignable = MemoryAssignable

    @property
    def DiskSpec(self):
        r"""主机磁盘(单位:GB)
        :rtype: int
        """
        return self._DiskSpec

    @DiskSpec.setter
    def DiskSpec(self, DiskSpec):
        self._DiskSpec = DiskSpec

    @property
    def DiskAssigned(self):
        r"""已分配磁盘(单位:GB)
        :rtype: int
        """
        return self._DiskAssigned

    @DiskAssigned.setter
    def DiskAssigned(self, DiskAssigned):
        self._DiskAssigned = DiskAssigned

    @property
    def DiskAssignable(self):
        r"""可分配磁盘(GB)
        :rtype: int
        """
        return self._DiskAssignable

    @DiskAssignable.setter
    def DiskAssignable(self, DiskAssignable):
        self._DiskAssignable = DiskAssignable

    @property
    def CpuRatio(self):
        r"""CPU分配比
        :rtype: float
        """
        return self._CpuRatio

    @CpuRatio.setter
    def CpuRatio(self, CpuRatio):
        self._CpuRatio = CpuRatio

    @property
    def MemoryRatio(self):
        r"""内存分配比
        :rtype: float
        """
        return self._MemoryRatio

    @MemoryRatio.setter
    def MemoryRatio(self, MemoryRatio):
        self._MemoryRatio = MemoryRatio

    @property
    def DiskRatio(self):
        r"""磁盘分配比
        :rtype: float
        """
        return self._DiskRatio

    @DiskRatio.setter
    def DiskRatio(self, DiskRatio):
        self._DiskRatio = DiskRatio

    @property
    def MachineName(self):
        r"""机型名称
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def MachineType(self):
        r"""机型类别
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def PidTag(self):
        r"""计费标签
        :rtype: str
        """
        return self._PidTag

    @PidTag.setter
    def PidTag(self, PidTag):
        self._PidTag = PidTag

    @property
    def Pid(self):
        r"""计费ID
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def InstanceId(self):
        r"""独享集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Zones(self):
        r"""可用区列表
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones


    def _deserialize(self, params):
        self._HostId = params.get("HostId")
        self._HostName = params.get("HostName")
        self._Zone = params.get("Zone")
        self._Status = params.get("Status")
        self._AssignStatus = params.get("AssignStatus")
        self._HostType = params.get("HostType")
        self._DbNum = params.get("DbNum")
        self._CpuSpec = params.get("CpuSpec")
        self._CpuAssigned = params.get("CpuAssigned")
        self._CpuAssignable = params.get("CpuAssignable")
        self._MemorySpec = params.get("MemorySpec")
        self._MemoryAssigned = params.get("MemoryAssigned")
        self._MemoryAssignable = params.get("MemoryAssignable")
        self._DiskSpec = params.get("DiskSpec")
        self._DiskAssigned = params.get("DiskAssigned")
        self._DiskAssignable = params.get("DiskAssignable")
        self._CpuRatio = params.get("CpuRatio")
        self._MemoryRatio = params.get("MemoryRatio")
        self._DiskRatio = params.get("DiskRatio")
        self._MachineName = params.get("MachineName")
        self._MachineType = params.get("MachineType")
        self._PidTag = params.get("PidTag")
        self._Pid = params.get("Pid")
        self._InstanceId = params.get("InstanceId")
        self._Zones = params.get("Zones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetail(AbstractModel):
    r"""集群容量信息。

    """

    def __init__(self):
        r"""
        :param _Status: 集群状态，0：运行中，1：不在运行
        :type Status: int
        :param _ReadWriteTotalLeaveMemory: 读写集群剩余内存容量，单位GB
        :type ReadWriteTotalLeaveMemory: float
        :param _ReadWriteTotalLeaveDisk: 读写集群剩余磁盘容量，单位GB
        :type ReadWriteTotalLeaveDisk: float
        :param _ReadWriteTotalMemory: 读写集群总内存容量，单位GB
        :type ReadWriteTotalMemory: float
        :param _ReadWriteTotalDisk: 读写集群总磁盘容量，单位GB
        :type ReadWriteTotalDisk: float
        :param _ReadOnlyTotalLeaveMemory: 只读集群剩余内存容量，单位GB
        :type ReadOnlyTotalLeaveMemory: float
        :param _ReadOnlyTotalLeaveDisk: 只读集群剩余磁盘容量，单位GB
        :type ReadOnlyTotalLeaveDisk: float
        :param _ReadOnlyTotalMemory: 只读集群总内存容量，单位GB
        :type ReadOnlyTotalMemory: float
        :param _ReadOnlyTotalDisk: 只读集群总磁盘容量，单位GB
        :type ReadOnlyTotalDisk: float
        :param _InstanceDeviceInfos: 集群设备详情
        :type InstanceDeviceInfos: list of InstanceDeviceInfo
        """
        self._Status = None
        self._ReadWriteTotalLeaveMemory = None
        self._ReadWriteTotalLeaveDisk = None
        self._ReadWriteTotalMemory = None
        self._ReadWriteTotalDisk = None
        self._ReadOnlyTotalLeaveMemory = None
        self._ReadOnlyTotalLeaveDisk = None
        self._ReadOnlyTotalMemory = None
        self._ReadOnlyTotalDisk = None
        self._InstanceDeviceInfos = None

    @property
    def Status(self):
        r"""集群状态，0：运行中，1：不在运行
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ReadWriteTotalLeaveMemory(self):
        r"""读写集群剩余内存容量，单位GB
        :rtype: float
        """
        return self._ReadWriteTotalLeaveMemory

    @ReadWriteTotalLeaveMemory.setter
    def ReadWriteTotalLeaveMemory(self, ReadWriteTotalLeaveMemory):
        self._ReadWriteTotalLeaveMemory = ReadWriteTotalLeaveMemory

    @property
    def ReadWriteTotalLeaveDisk(self):
        r"""读写集群剩余磁盘容量，单位GB
        :rtype: float
        """
        return self._ReadWriteTotalLeaveDisk

    @ReadWriteTotalLeaveDisk.setter
    def ReadWriteTotalLeaveDisk(self, ReadWriteTotalLeaveDisk):
        self._ReadWriteTotalLeaveDisk = ReadWriteTotalLeaveDisk

    @property
    def ReadWriteTotalMemory(self):
        r"""读写集群总内存容量，单位GB
        :rtype: float
        """
        return self._ReadWriteTotalMemory

    @ReadWriteTotalMemory.setter
    def ReadWriteTotalMemory(self, ReadWriteTotalMemory):
        self._ReadWriteTotalMemory = ReadWriteTotalMemory

    @property
    def ReadWriteTotalDisk(self):
        r"""读写集群总磁盘容量，单位GB
        :rtype: float
        """
        return self._ReadWriteTotalDisk

    @ReadWriteTotalDisk.setter
    def ReadWriteTotalDisk(self, ReadWriteTotalDisk):
        self._ReadWriteTotalDisk = ReadWriteTotalDisk

    @property
    def ReadOnlyTotalLeaveMemory(self):
        r"""只读集群剩余内存容量，单位GB
        :rtype: float
        """
        return self._ReadOnlyTotalLeaveMemory

    @ReadOnlyTotalLeaveMemory.setter
    def ReadOnlyTotalLeaveMemory(self, ReadOnlyTotalLeaveMemory):
        self._ReadOnlyTotalLeaveMemory = ReadOnlyTotalLeaveMemory

    @property
    def ReadOnlyTotalLeaveDisk(self):
        r"""只读集群剩余磁盘容量，单位GB
        :rtype: float
        """
        return self._ReadOnlyTotalLeaveDisk

    @ReadOnlyTotalLeaveDisk.setter
    def ReadOnlyTotalLeaveDisk(self, ReadOnlyTotalLeaveDisk):
        self._ReadOnlyTotalLeaveDisk = ReadOnlyTotalLeaveDisk

    @property
    def ReadOnlyTotalMemory(self):
        r"""只读集群总内存容量，单位GB
        :rtype: float
        """
        return self._ReadOnlyTotalMemory

    @ReadOnlyTotalMemory.setter
    def ReadOnlyTotalMemory(self, ReadOnlyTotalMemory):
        self._ReadOnlyTotalMemory = ReadOnlyTotalMemory

    @property
    def ReadOnlyTotalDisk(self):
        r"""只读集群总磁盘容量，单位GB
        :rtype: float
        """
        return self._ReadOnlyTotalDisk

    @ReadOnlyTotalDisk.setter
    def ReadOnlyTotalDisk(self, ReadOnlyTotalDisk):
        self._ReadOnlyTotalDisk = ReadOnlyTotalDisk

    @property
    def InstanceDeviceInfos(self):
        r"""集群设备详情
        :rtype: list of InstanceDeviceInfo
        """
        return self._InstanceDeviceInfos

    @InstanceDeviceInfos.setter
    def InstanceDeviceInfos(self, InstanceDeviceInfos):
        self._InstanceDeviceInfos = InstanceDeviceInfos


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ReadWriteTotalLeaveMemory = params.get("ReadWriteTotalLeaveMemory")
        self._ReadWriteTotalLeaveDisk = params.get("ReadWriteTotalLeaveDisk")
        self._ReadWriteTotalMemory = params.get("ReadWriteTotalMemory")
        self._ReadWriteTotalDisk = params.get("ReadWriteTotalDisk")
        self._ReadOnlyTotalLeaveMemory = params.get("ReadOnlyTotalLeaveMemory")
        self._ReadOnlyTotalLeaveDisk = params.get("ReadOnlyTotalLeaveDisk")
        self._ReadOnlyTotalMemory = params.get("ReadOnlyTotalMemory")
        self._ReadOnlyTotalDisk = params.get("ReadOnlyTotalDisk")
        if params.get("InstanceDeviceInfos") is not None:
            self._InstanceDeviceInfos = []
            for item in params.get("InstanceDeviceInfos"):
                obj = InstanceDeviceInfo()
                obj._deserialize(item)
                self._InstanceDeviceInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDeviceInfo(AbstractModel):
    r"""集群设备组信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _ReadWriteDevice: 读写设备组
        :type ReadWriteDevice: list of DeviceInfo
        :param _ReadOnlyDevice: 只读设备组
        :type ReadOnlyDevice: list of DeviceInfo
        :param _FreeDevice: 空闲设备组
        :type FreeDevice: list of DeviceInfo
        """
        self._InstanceId = None
        self._ReadWriteDevice = None
        self._ReadOnlyDevice = None
        self._FreeDevice = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReadWriteDevice(self):
        r"""读写设备组
        :rtype: list of DeviceInfo
        """
        return self._ReadWriteDevice

    @ReadWriteDevice.setter
    def ReadWriteDevice(self, ReadWriteDevice):
        self._ReadWriteDevice = ReadWriteDevice

    @property
    def ReadOnlyDevice(self):
        r"""只读设备组
        :rtype: list of DeviceInfo
        """
        return self._ReadOnlyDevice

    @ReadOnlyDevice.setter
    def ReadOnlyDevice(self, ReadOnlyDevice):
        self._ReadOnlyDevice = ReadOnlyDevice

    @property
    def FreeDevice(self):
        r"""空闲设备组
        :rtype: list of DeviceInfo
        """
        return self._FreeDevice

    @FreeDevice.setter
    def FreeDevice(self, FreeDevice):
        self._FreeDevice = FreeDevice


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ReadWriteDevice") is not None:
            self._ReadWriteDevice = []
            for item in params.get("ReadWriteDevice"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self._ReadWriteDevice.append(obj)
        if params.get("ReadOnlyDevice") is not None:
            self._ReadOnlyDevice = []
            for item in params.get("ReadOnlyDevice"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self._ReadOnlyDevice.append(obj)
        if params.get("FreeDevice") is not None:
            self._FreeDevice = []
            for item in params.get("FreeDevice"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self._FreeDevice.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceExpand(AbstractModel):
    r"""集群扩展信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _InstanceName: 集群名称
        :type InstanceName: str
        :param _AppId: 用户ID
        :type AppId: int
        :param _Region: 地域
        :type Region: str
        :param _Zone: 可用区
        :type Zone: str
        :param _InstanceType: 集群类型： 0：一主一备，1：一主两备
        :type InstanceType: int
        :param _InstanceStatus: 集群状态: 0 集群创建中, 1 集群有效, 2 集群扩容中, 3 集群删除中, 4 集群缩容中 -1 集群已隔离 -2 集群已删除
        :type InstanceStatus: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _AutoRenewFlag: 实例自动续费标识： 0正常续费 1自动续费 2到期不续费
        :type AutoRenewFlag: int
        :param _Machine: 机型
        :type Machine: str
        :param _PeriodEndTime: 过期时间
        :type PeriodEndTime: str
        :param _InstanceDetail: 集群信息
        :type InstanceDetail: :class:`tencentcloud.dbdc.v20201029.models.InstanceDetail`
        :param _Pid: 计费侧的产品ID
        :type Pid: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._AppId = None
        self._Region = None
        self._Zone = None
        self._InstanceType = None
        self._InstanceStatus = None
        self._CreateTime = None
        self._AutoRenewFlag = None
        self._Machine = None
        self._PeriodEndTime = None
        self._InstanceDetail = None
        self._Pid = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""集群名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AppId(self):
        r"""用户ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        r"""集群类型： 0：一主一备，1：一主两备
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceStatus(self):
        r"""集群状态: 0 集群创建中, 1 集群有效, 2 集群扩容中, 3 集群删除中, 4 集群缩容中 -1 集群已隔离 -2 集群已删除
        :rtype: int
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AutoRenewFlag(self):
        r"""实例自动续费标识： 0正常续费 1自动续费 2到期不续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Machine(self):
        r"""机型
        :rtype: str
        """
        return self._Machine

    @Machine.setter
    def Machine(self, Machine):
        self._Machine = Machine

    @property
    def PeriodEndTime(self):
        r"""过期时间
        :rtype: str
        """
        return self._PeriodEndTime

    @PeriodEndTime.setter
    def PeriodEndTime(self, PeriodEndTime):
        self._PeriodEndTime = PeriodEndTime

    @property
    def InstanceDetail(self):
        r"""集群信息
        :rtype: :class:`tencentcloud.dbdc.v20201029.models.InstanceDetail`
        """
        return self._InstanceDetail

    @InstanceDetail.setter
    def InstanceDetail(self, InstanceDetail):
        self._InstanceDetail = InstanceDetail

    @property
    def Pid(self):
        r"""计费侧的产品ID
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AppId = params.get("AppId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._InstanceType = params.get("InstanceType")
        self._InstanceStatus = params.get("InstanceStatus")
        self._CreateTime = params.get("CreateTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._Machine = params.get("Machine")
        self._PeriodEndTime = params.get("PeriodEndTime")
        if params.get("InstanceDetail") is not None:
            self._InstanceDetail = InstanceDetail()
            self._InstanceDetail._deserialize(params.get("InstanceDetail"))
        self._Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBCustomNodeRequest(AbstractModel):
    r"""IsolateDBCustomNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeId: <p>DB Custom 节点ID</p>
        :type NodeId: str
        """
        self._NodeId = None

    @property
    def NodeId(self):
        r"""<p>DB Custom 节点ID</p>
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBCustomNodeResponse(AbstractModel):
    r"""IsolateDBCustomNode返回参数结构体

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


class LoginSettings(AbstractModel):
    r"""DB Custom 节点登录相关配置。

    """

    def __init__(self):
        r"""
        :param _Password: <p>实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下： Linux实例密码必须8到30位，至少包括两项[a-z]，[A-Z]、[0-9] 和 [( ) <code>~ ! @ # $ % ^ &amp; * - + = | { } [ ] : ; &#39; , . ? / ]中的特殊符号。 Windows实例密码必须12到30位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( )</code> ~ ! @ # $ % ^ &amp; * - + = | { } [ ] : ; &#39; , . ? /]中的特殊符号。</p>
        :type Password: str
        :param _KeyIds: <p>密钥ID列表。关联密钥后，就可以通过对应的私钥来访问实例；KeyId可通过接口 DescribeKeyPairs获取，密钥与密码不能同时指定，同时Windows操作系统不支持指定密钥。</p><p>入参限制：当前仅支持设置单个 ID。</p>
        :type KeyIds: list of str
        :param _KeepImageLogin: <p>保持镜像的原始设置。该参数与Password或KeyIds.N不能同时指定。只有使用自定义镜像、共享镜像或外部导入镜像创建实例时才能指定该参数为true。</p><p>枚举值：</p><ul><li>true： 表示保持镜像的登录设置</li><li>false： 表示不保持镜像的登录设置</li></ul>
        :type KeepImageLogin: str
        """
        self._Password = None
        self._KeyIds = None
        self._KeepImageLogin = None

    @property
    def Password(self):
        r"""<p>实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下： Linux实例密码必须8到30位，至少包括两项[a-z]，[A-Z]、[0-9] 和 [( ) <code>~ ! @ # $ % ^ &amp; * - + = | { } [ ] : ; &#39; , . ? / ]中的特殊符号。 Windows实例密码必须12到30位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( )</code> ~ ! @ # $ % ^ &amp; * - + = | { } [ ] : ; &#39; , . ? /]中的特殊符号。</p>
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def KeyIds(self):
        r"""<p>密钥ID列表。关联密钥后，就可以通过对应的私钥来访问实例；KeyId可通过接口 DescribeKeyPairs获取，密钥与密码不能同时指定，同时Windows操作系统不支持指定密钥。</p><p>入参限制：当前仅支持设置单个 ID。</p>
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def KeepImageLogin(self):
        r"""<p>保持镜像的原始设置。该参数与Password或KeyIds.N不能同时指定。只有使用自定义镜像、共享镜像或外部导入镜像创建实例时才能指定该参数为true。</p><p>枚举值：</p><ul><li>true： 表示保持镜像的登录设置</li><li>false： 表示不保持镜像的登录设置</li></ul>
        :rtype: str
        """
        return self._KeepImageLogin

    @KeepImageLogin.setter
    def KeepImageLogin(self, KeepImageLogin):
        self._KeepImageLogin = KeepImageLogin


    def _deserialize(self, params):
        self._Password = params.get("Password")
        self._KeyIds = params.get("KeyIds")
        self._KeepImageLogin = params.get("KeepImageLogin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBCustomClusterTagsRequest(AbstractModel):
    r"""ModifyDBCustomClusterTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: <p>DB Custom 集群ID</p><p>参数格式：dbcc-xxxxxxxx</p>
        :type ClusterId: str
        :param _AddTags: <p>为 DB Custom 集群绑定的标签信息</p><p>入参限制：参考标签平台的限制策略</p>
        :type AddTags: list of Tag
        :param _DeleteTagKeys: <p>为 DB Custom 集群删除的标签Key</p>
        :type DeleteTagKeys: list of str
        """
        self._ClusterId = None
        self._AddTags = None
        self._DeleteTagKeys = None

    @property
    def ClusterId(self):
        r"""<p>DB Custom 集群ID</p><p>参数格式：dbcc-xxxxxxxx</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AddTags(self):
        r"""<p>为 DB Custom 集群绑定的标签信息</p><p>入参限制：参考标签平台的限制策略</p>
        :rtype: list of Tag
        """
        return self._AddTags

    @AddTags.setter
    def AddTags(self, AddTags):
        self._AddTags = AddTags

    @property
    def DeleteTagKeys(self):
        r"""<p>为 DB Custom 集群删除的标签Key</p>
        :rtype: list of str
        """
        return self._DeleteTagKeys

    @DeleteTagKeys.setter
    def DeleteTagKeys(self, DeleteTagKeys):
        self._DeleteTagKeys = DeleteTagKeys


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("AddTags") is not None:
            self._AddTags = []
            for item in params.get("AddTags"):
                obj = Tag()
                obj._deserialize(item)
                self._AddTags.append(obj)
        self._DeleteTagKeys = params.get("DeleteTagKeys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBCustomClusterTagsResponse(AbstractModel):
    r"""ModifyDBCustomClusterTags返回参数结构体

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


class ModifyDBCustomNodeTagsRequest(AbstractModel):
    r"""ModifyDBCustomNodeTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeId: <p>DB Custom 节点ID</p><p>参数格式：dbcn-0zan5xxk</p>
        :type NodeId: str
        :param _AddTags: <p>为节点绑定的标签信息</p><p>入参限制：参考标签侧的限制</p>
        :type AddTags: list of Tag
        :param _DeleteTagKeys: <p>需要删除的标签Key</p>
        :type DeleteTagKeys: list of str
        """
        self._NodeId = None
        self._AddTags = None
        self._DeleteTagKeys = None

    @property
    def NodeId(self):
        r"""<p>DB Custom 节点ID</p><p>参数格式：dbcn-0zan5xxk</p>
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def AddTags(self):
        r"""<p>为节点绑定的标签信息</p><p>入参限制：参考标签侧的限制</p>
        :rtype: list of Tag
        """
        return self._AddTags

    @AddTags.setter
    def AddTags(self, AddTags):
        self._AddTags = AddTags

    @property
    def DeleteTagKeys(self):
        r"""<p>需要删除的标签Key</p>
        :rtype: list of str
        """
        return self._DeleteTagKeys

    @DeleteTagKeys.setter
    def DeleteTagKeys(self, DeleteTagKeys):
        self._DeleteTagKeys = DeleteTagKeys


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        if params.get("AddTags") is not None:
            self._AddTags = []
            for item in params.get("AddTags"):
                obj = Tag()
                obj._deserialize(item)
                self._AddTags.append(obj)
        self._DeleteTagKeys = params.get("DeleteTagKeys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBCustomNodeTagsResponse(AbstractModel):
    r"""ModifyDBCustomNodeTags返回参数结构体

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


class ModifyInstanceNameRequest(AbstractModel):
    r"""ModifyInstanceName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 独享集群实例Id
        :type InstanceId: str
        :param _InstanceName: 独享集群实例名称
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        r"""独享集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""独享集群实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceNameResponse(AbstractModel):
    r"""ModifyInstanceName返回参数结构体

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


class RemoveNodesFromDBCustomClusterRequest(AbstractModel):
    r"""RemoveNodesFromDBCustomCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: <p>DB Custom 集群ID</p>
        :type ClusterId: str
        :param _NodeIds: <p>要下架的 DB Custom 节点ID列表</p>
        :type NodeIds: list of str
        """
        self._ClusterId = None
        self._NodeIds = None

    @property
    def ClusterId(self):
        r"""<p>DB Custom 集群ID</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodeIds(self):
        r"""<p>要下架的 DB Custom 节点ID列表</p>
        :rtype: list of str
        """
        return self._NodeIds

    @NodeIds.setter
    def NodeIds(self, NodeIds):
        self._NodeIds = NodeIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodeIds = params.get("NodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveNodesFromDBCustomClusterResponse(AbstractModel):
    r"""RemoveNodesFromDBCustomCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>任务ID</p>
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>任务ID</p>
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class RenewDBCustomNodeRequest(AbstractModel):
    r"""RenewDBCustomNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeId: <p>节点ID</p>
        :type NodeId: str
        :param _Period: <p>续费周期</p><p>取值范围：[1, 36]</p><p>单位：月</p><p>默认值：1</p>
        :type Period: int
        :param _AutoRenew: <p>是否开启自动续费</p><p>枚举值：</p><ul><li>0： 不自动续费</li><li>1： 自动续费</li></ul><p>默认值：1</p>
        :type AutoRenew: int
        :param _AutoVoucher: <p>是否自动使用代金券</p>
        :type AutoVoucher: int
        :param _VoucherIds: <p>代金券ID</p>
        :type VoucherIds: list of str
        """
        self._NodeId = None
        self._Period = None
        self._AutoRenew = None
        self._AutoVoucher = None
        self._VoucherIds = None

    @property
    def NodeId(self):
        r"""<p>节点ID</p>
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Period(self):
        r"""<p>续费周期</p><p>取值范围：[1, 36]</p><p>单位：月</p><p>默认值：1</p>
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoRenew(self):
        r"""<p>是否开启自动续费</p><p>枚举值：</p><ul><li>0： 不自动续费</li><li>1： 自动续费</li></ul><p>默认值：1</p>
        :rtype: int
        """
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def AutoVoucher(self):
        r"""<p>是否自动使用代金券</p>
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def VoucherIds(self):
        r"""<p>代金券ID</p>
        :rtype: list of str
        """
        return self._VoucherIds

    @VoucherIds.setter
    def VoucherIds(self, VoucherIds):
        self._VoucherIds = VoucherIds


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Period = params.get("Period")
        self._AutoRenew = params.get("AutoRenew")
        self._AutoVoucher = params.get("AutoVoucher")
        self._VoucherIds = params.get("VoucherIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDBCustomNodeResponse(AbstractModel):
    r"""RenewDBCustomNode返回参数结构体

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


class ResourceTag(AbstractModel):
    r"""标签对象，包含tagKey & tagValue

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值
        :rtype: str
        """
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
        


class SystemDisk(AbstractModel):
    r"""DB Custom 节点系统盘信息。

    """

    def __init__(self):
        r"""
        :param _DiskType: <p>磁盘类型</p><p>枚举值：</p><ul><li>CLOUD_HSSD： 增强型云硬盘</li></ul>
        :type DiskType: str
        :param _DiskSize: <p>磁盘大小</p><p>单位：GiB</p>
        :type DiskSize: int
        """
        self._DiskType = None
        self._DiskSize = None

    @property
    def DiskType(self):
        r"""<p>磁盘类型</p><p>枚举值：</p><ul><li>CLOUD_HSSD： 增强型云硬盘</li></ul>
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""<p>磁盘大小</p><p>单位：GiB</p>
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""标签键值对。

    """

    def __init__(self):
        r"""
        :param _Key: <p>标签键</p>
        :type Key: str
        :param _Value: <p>标签值</p>
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""<p>标签键</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>标签值</p>
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        