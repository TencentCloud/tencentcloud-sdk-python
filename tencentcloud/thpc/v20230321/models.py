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


class AddClusterStorageOptionRequest(AbstractModel):
    """AddClusterStorageOption请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _StorageOption: 集群存储选项；集群已存在的节点和新增节点都会挂载此存储。
        :type StorageOption: :class:`tencentcloud.thpc.v20230321.models.StorageOption`
        """
        self._ClusterId = None
        self._StorageOption = None

    @property
    def ClusterId(self):
        """集群ID。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def StorageOption(self):
        """集群存储选项；集群已存在的节点和新增节点都会挂载此存储。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.StorageOption`
        """
        return self._StorageOption

    @StorageOption.setter
    def StorageOption(self, StorageOption):
        self._StorageOption = StorageOption


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("StorageOption") is not None:
            self._StorageOption = StorageOption()
            self._StorageOption._deserialize(params.get("StorageOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddClusterStorageOptionResponse(AbstractModel):
    """AddClusterStorageOption返回参数结构体

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


class AddNodesRequest(AbstractModel):
    """AddNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Placement: 集群中实例所在的位置。
        :type Placement: :class:`tencentcloud.thpc.v20230321.models.Placement`
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _VirtualPrivateCloud: 私有网络相关信息配置。
        :type VirtualPrivateCloud: :class:`tencentcloud.thpc.v20230321.models.VirtualPrivateCloud`
        :param _Count: 添加节点数量。
        :type Count: int
        :param _ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。目前支持部分公有镜像和自定义镜像。公共镜像请参考[镜像限制](https://cloud.tencent.com/document/product/1527/64818#.E9.95.9C.E5.83.8F)
        :type ImageId: str
        :param _InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月</li><li>POSTPAID_BY_HOUR：按小时后付费</li><li>SPOTPAID：竞价付费</li>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20230321.models.InstanceChargePrepaid`
        :param _InstanceType: 节点机型。不同实例机型指定了不同的资源规格。<br><li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。</li>
        :type InstanceType: str
        :param _SystemDisk: 节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.thpc.v20230321.models.SystemDisk`
        :param _DataDisks: 节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20230321.models.InternetAccessible`
        :param _InstanceName: 节点显示名称。
不指定节点显示名称则默认显示‘未命名’。
最多支持60个字符。
        :type InstanceName: str
        :param _LoginSettings: 集群登录设置。
        :type LoginSettings: :class:`tencentcloud.thpc.v20230321.models.LoginSettings`
        :param _SecurityGroupIds: 集群中实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。
        :type SecurityGroupIds: list of str
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param _QueueName: 队列名称。不指定则为默认队列。<li>SLURM默认队列为：compute。</li><li>SGE默认队列为：all.q。</li>

        :type QueueName: str
        :param _NodeRole: 添加节点角色。默认值：Compute<br><li>Compute：计算节点。</li><li>Login：登录节点。</li>
        :type NodeRole: str
        :param _DryRun: 是否只预检此次请求。
true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和云服务器库存。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId.
false（默认）：发送正常请求，通过检查后直接创建实例
        :type DryRun: bool
        :param _NodeType: 添加节点类型。默认取值：STATIC。<li>STATIC：静态节点，不会参与弹性伸缩流程。</li><li>DYNAMIC：弹性节点，会被弹性缩容的节点。管控节点和登录节点不支持此参数。</li>
        :type NodeType: str
        :param _ProjectId: 实例所属项目ID。该参数可以通过调用 [DescribeProject](https://cloud.tencent.com/document/api/651/78725) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :type ProjectId: int
        :param _ResourceType: 要新增节点的资源类型。<li>CVM：CVM实例类型资源</li><li>WORKSPACE：工作空间类型实例资源</li>默认值：CVM。
        :type ResourceType: str
        """
        self._Placement = None
        self._ClusterId = None
        self._VirtualPrivateCloud = None
        self._Count = None
        self._ImageId = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._InstanceType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._InternetAccessible = None
        self._InstanceName = None
        self._LoginSettings = None
        self._SecurityGroupIds = None
        self._ClientToken = None
        self._QueueName = None
        self._NodeRole = None
        self._DryRun = None
        self._NodeType = None
        self._ProjectId = None
        self._ResourceType = None

    @property
    def Placement(self):
        """集群中实例所在的位置。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def ClusterId(self):
        """集群ID。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def VirtualPrivateCloud(self):
        """私有网络相关信息配置。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.VirtualPrivateCloud`
        """
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def Count(self):
        """添加节点数量。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ImageId(self):
        """指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。目前支持部分公有镜像和自定义镜像。公共镜像请参考[镜像限制](https://cloud.tencent.com/document/product/1527/64818#.E9.95.9C.E5.83.8F)
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def InstanceChargeType(self):
        """节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月</li><li>POSTPAID_BY_HOUR：按小时后付费</li><li>SPOTPAID：竞价付费</li>默认值：POSTPAID_BY_HOUR。
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        """预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def InstanceType(self):
        """节点机型。不同实例机型指定了不同的资源规格。<br><li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。</li>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        """节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def InternetAccessible(self):
        """公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceName(self):
        """节点显示名称。
不指定节点显示名称则默认显示‘未命名’。
最多支持60个字符。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def LoginSettings(self):
        """集群登录设置。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.LoginSettings`
        """
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SecurityGroupIds(self):
        """集群中实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def ClientToken(self):
        """用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def QueueName(self):
        """队列名称。不指定则为默认队列。<li>SLURM默认队列为：compute。</li><li>SGE默认队列为：all.q。</li>

        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def NodeRole(self):
        """添加节点角色。默认值：Compute<br><li>Compute：计算节点。</li><li>Login：登录节点。</li>
        :rtype: str
        """
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def DryRun(self):
        """是否只预检此次请求。
true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和云服务器库存。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId.
false（默认）：发送正常请求，通过检查后直接创建实例
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def NodeType(self):
        """添加节点类型。默认取值：STATIC。<li>STATIC：静态节点，不会参与弹性伸缩流程。</li><li>DYNAMIC：弹性节点，会被弹性缩容的节点。管控节点和登录节点不支持此参数。</li>
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def ProjectId(self):
        """实例所属项目ID。该参数可以通过调用 [DescribeProject](https://cloud.tencent.com/document/api/651/78725) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ResourceType(self):
        """要新增节点的资源类型。<li>CVM：CVM实例类型资源</li><li>WORKSPACE：工作空间类型实例资源</li>默认值：CVM。
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._ClusterId = params.get("ClusterId")
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self._Count = params.get("Count")
        self._ImageId = params.get("ImageId")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._ClientToken = params.get("ClientToken")
        self._QueueName = params.get("QueueName")
        self._NodeRole = params.get("NodeRole")
        self._DryRun = params.get("DryRun")
        self._NodeType = params.get("NodeType")
        self._ProjectId = params.get("ProjectId")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddNodesResponse(AbstractModel):
    """AddNodes返回参数结构体

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


class AddQueueRequest(AbstractModel):
    """AddQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _QueueName: 队列名称。<br><li>最多支持32个字符。
        :type QueueName: str
        """
        self._ClusterId = None
        self._QueueName = None

    @property
    def ClusterId(self):
        """集群ID。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def QueueName(self):
        """队列名称。<br><li>最多支持32个字符。
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddQueueResponse(AbstractModel):
    """AddQueue返回参数结构体

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


class AttachNodesRequest(AbstractModel):
    """AttachNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _ResourceSet: 节点的实例id列表
        :type ResourceSet: list of str
        :param _QueueName: 队列名称。不指定则为默认队列：
SLURM默认队列为：compute。 
SGE默认队列为：all.q。
        :type QueueName: str
        :param _ImageId: 指定有效的镜像ID，格式形如img-xxx。目前仅支持公有镜像和特定自定义镜像。如不指定，则该字段是默认镜像。
        :type ImageId: str
        :param _ResourceType: 要新增节点的资源类型。<li>CVM：CVM实例类型资源</li><li>WORKSPACE：工作空间类型实例资源</li>默认值：CVM。
        :type ResourceType: str
        """
        self._ClusterId = None
        self._ResourceSet = None
        self._QueueName = None
        self._ImageId = None
        self._ResourceType = None

    @property
    def ClusterId(self):
        """集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ResourceSet(self):
        """节点的实例id列表
        :rtype: list of str
        """
        return self._ResourceSet

    @ResourceSet.setter
    def ResourceSet(self, ResourceSet):
        self._ResourceSet = ResourceSet

    @property
    def QueueName(self):
        """队列名称。不指定则为默认队列：
SLURM默认队列为：compute。 
SGE默认队列为：all.q。
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def ImageId(self):
        """指定有效的镜像ID，格式形如img-xxx。目前仅支持公有镜像和特定自定义镜像。如不指定，则该字段是默认镜像。
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ResourceType(self):
        """要新增节点的资源类型。<li>CVM：CVM实例类型资源</li><li>WORKSPACE：工作空间类型实例资源</li>默认值：CVM。
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ResourceSet = params.get("ResourceSet")
        self._QueueName = params.get("QueueName")
        self._ImageId = params.get("ImageId")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachNodesResponse(AbstractModel):
    """AttachNodes返回参数结构体

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


class CFSOption(AbstractModel):
    """描述CFS文件系统版本和挂载信息

    """

    def __init__(self):
        r"""
        :param _LocalPath: 文件系统本地挂载路径。
        :type LocalPath: str
        :param _RemotePath: 文件系统远程挂载ip及路径。
        :type RemotePath: str
        :param _Protocol: 文件系统协议类型，默认值NFS 3.0。
<li>NFS 3.0。
<li>NFS 4.0。
<li>TURBO。
        :type Protocol: str
        :param _StorageType: 文件系统存储类型，默认值SD；其中 SD 为通用标准型标准型存储， HP为通用性能型存储， TB为turbo标准型， TP 为turbo性能型。
        :type StorageType: str
        :param _MountOption: 文件系统挂载挂载命令参数选项。

- NFS 3.0默认值：vers=3,nolock,proto=tcp,noresvport
- NFS 4.0默认值：vers=4.0,noresvport
- TURBO默认值：user_xattr
        :type MountOption: str
        """
        self._LocalPath = None
        self._RemotePath = None
        self._Protocol = None
        self._StorageType = None
        self._MountOption = None

    @property
    def LocalPath(self):
        """文件系统本地挂载路径。
        :rtype: str
        """
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath

    @property
    def RemotePath(self):
        """文件系统远程挂载ip及路径。
        :rtype: str
        """
        return self._RemotePath

    @RemotePath.setter
    def RemotePath(self, RemotePath):
        self._RemotePath = RemotePath

    @property
    def Protocol(self):
        """文件系统协议类型，默认值NFS 3.0。
<li>NFS 3.0。
<li>NFS 4.0。
<li>TURBO。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def StorageType(self):
        """文件系统存储类型，默认值SD；其中 SD 为通用标准型标准型存储， HP为通用性能型存储， TB为turbo标准型， TP 为turbo性能型。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def MountOption(self):
        """文件系统挂载挂载命令参数选项。

- NFS 3.0默认值：vers=3,nolock,proto=tcp,noresvport
- NFS 4.0默认值：vers=4.0,noresvport
- TURBO默认值：user_xattr
        :rtype: str
        """
        return self._MountOption

    @MountOption.setter
    def MountOption(self, MountOption):
        self._MountOption = MountOption


    def _deserialize(self, params):
        self._LocalPath = params.get("LocalPath")
        self._RemotePath = params.get("RemotePath")
        self._Protocol = params.get("Protocol")
        self._StorageType = params.get("StorageType")
        self._MountOption = params.get("MountOption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CFSOptionOverview(AbstractModel):
    """CFS存储选项概览信息。

    """

    def __init__(self):
        r"""
        :param _LocalPath: 文件系统本地挂载路径。
        :type LocalPath: str
        :param _RemotePath: 文件系统远程挂载ip及路径。
        :type RemotePath: str
        :param _Protocol: 文件系统协议类型。
<li>NFS 3.0。
<li>NFS 4.0。
<li>TURBO。
        :type Protocol: str
        :param _StorageType: 文件系统存储类型，默认值SD；其中 SD 为通用标准型标准型存储， HP为通用性能型存储， TB为turbo标准型， TP 为turbo性能型。
        :type StorageType: str
        :param _MountOption: 文件系统挂载命令参数选项。
        :type MountOption: str
        """
        self._LocalPath = None
        self._RemotePath = None
        self._Protocol = None
        self._StorageType = None
        self._MountOption = None

    @property
    def LocalPath(self):
        """文件系统本地挂载路径。
        :rtype: str
        """
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath

    @property
    def RemotePath(self):
        """文件系统远程挂载ip及路径。
        :rtype: str
        """
        return self._RemotePath

    @RemotePath.setter
    def RemotePath(self, RemotePath):
        self._RemotePath = RemotePath

    @property
    def Protocol(self):
        """文件系统协议类型。
<li>NFS 3.0。
<li>NFS 4.0。
<li>TURBO。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def StorageType(self):
        """文件系统存储类型，默认值SD；其中 SD 为通用标准型标准型存储， HP为通用性能型存储， TB为turbo标准型， TP 为turbo性能型。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def MountOption(self):
        """文件系统挂载命令参数选项。
        :rtype: str
        """
        return self._MountOption

    @MountOption.setter
    def MountOption(self, MountOption):
        self._MountOption = MountOption


    def _deserialize(self, params):
        self._LocalPath = params.get("LocalPath")
        self._RemotePath = params.get("RemotePath")
        self._Protocol = params.get("Protocol")
        self._StorageType = params.get("StorageType")
        self._MountOption = params.get("MountOption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterActivity(AbstractModel):
    """符合条件的集群活动信息。

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _ActivityId: 集群活动ID。
        :type ActivityId: str
        :param _ActivityType: 集群活动类型。取值范围：<br><li>CreateAndAddNodes：创建实例并添加进集群</li><br><li>RemoveNodesFromCluster：从集群移除实例</li><br><li>TerminateNodes：销毁实例</li><br><li>MountStorageOption：增加挂载选项并进行挂载</li><br><li>UmountStorageOption：删除集群挂载存储选项并解挂载</li>
        :type ActivityType: str
        :param _ActivityStatus: 集群活动状态。取值范围：<br><li>PENDING：等待运行</li><br><li>RUNNING：运行中</li><br><li>SUCCESSFUL：活动成功</li><br><li>PARTIALLY_SUCCESSFUL：活动部分成功</li><br><li>FAILED：活动失败</li>
        :type ActivityStatus: str
        :param _ActivityStatusCode: 集群活动状态码。
        :type ActivityStatusCode: str
        :param _ResultDetail: 集群活动结果详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultDetail: str
        :param _Cause: 集群活动起因。
        :type Cause: str
        :param _Description: 集群活动描述。
        :type Description: str
        :param _RelatedNodeActivitySet: 集群活动相关节点活动集合。
        :type RelatedNodeActivitySet: list of NodeActivity
        :param _StartTime: 集群活动开始时间。
        :type StartTime: str
        :param _EndTime: 集群活动结束时间。
        :type EndTime: str
        """
        self._ClusterId = None
        self._ActivityId = None
        self._ActivityType = None
        self._ActivityStatus = None
        self._ActivityStatusCode = None
        self._ResultDetail = None
        self._Cause = None
        self._Description = None
        self._RelatedNodeActivitySet = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ClusterId(self):
        """集群ID。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ActivityId(self):
        """集群活动ID。
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def ActivityType(self):
        """集群活动类型。取值范围：<br><li>CreateAndAddNodes：创建实例并添加进集群</li><br><li>RemoveNodesFromCluster：从集群移除实例</li><br><li>TerminateNodes：销毁实例</li><br><li>MountStorageOption：增加挂载选项并进行挂载</li><br><li>UmountStorageOption：删除集群挂载存储选项并解挂载</li>
        :rtype: str
        """
        return self._ActivityType

    @ActivityType.setter
    def ActivityType(self, ActivityType):
        self._ActivityType = ActivityType

    @property
    def ActivityStatus(self):
        """集群活动状态。取值范围：<br><li>PENDING：等待运行</li><br><li>RUNNING：运行中</li><br><li>SUCCESSFUL：活动成功</li><br><li>PARTIALLY_SUCCESSFUL：活动部分成功</li><br><li>FAILED：活动失败</li>
        :rtype: str
        """
        return self._ActivityStatus

    @ActivityStatus.setter
    def ActivityStatus(self, ActivityStatus):
        self._ActivityStatus = ActivityStatus

    @property
    def ActivityStatusCode(self):
        """集群活动状态码。
        :rtype: str
        """
        return self._ActivityStatusCode

    @ActivityStatusCode.setter
    def ActivityStatusCode(self, ActivityStatusCode):
        self._ActivityStatusCode = ActivityStatusCode

    @property
    def ResultDetail(self):
        """集群活动结果详情。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultDetail

    @ResultDetail.setter
    def ResultDetail(self, ResultDetail):
        self._ResultDetail = ResultDetail

    @property
    def Cause(self):
        """集群活动起因。
        :rtype: str
        """
        return self._Cause

    @Cause.setter
    def Cause(self, Cause):
        self._Cause = Cause

    @property
    def Description(self):
        """集群活动描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RelatedNodeActivitySet(self):
        """集群活动相关节点活动集合。
        :rtype: list of NodeActivity
        """
        return self._RelatedNodeActivitySet

    @RelatedNodeActivitySet.setter
    def RelatedNodeActivitySet(self, RelatedNodeActivitySet):
        self._RelatedNodeActivitySet = RelatedNodeActivitySet

    @property
    def StartTime(self):
        """集群活动开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """集群活动结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ActivityId = params.get("ActivityId")
        self._ActivityType = params.get("ActivityType")
        self._ActivityStatus = params.get("ActivityStatus")
        self._ActivityStatusCode = params.get("ActivityStatusCode")
        self._ResultDetail = params.get("ResultDetail")
        self._Cause = params.get("Cause")
        self._Description = params.get("Description")
        if params.get("RelatedNodeActivitySet") is not None:
            self._RelatedNodeActivitySet = []
            for item in params.get("RelatedNodeActivitySet"):
                obj = NodeActivity()
                obj._deserialize(item)
                self._RelatedNodeActivitySet.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterOverview(AbstractModel):
    """集群概览信息。

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _ClusterStatus: 集群状态。取值范围：<li>PENDING：创建中</li><li>INITING：初始化中</li><li>INIT_FAILED：初始化失败</li><li>RUNNING：运行中</li><li>TERMINATING：销毁中</li>
        :type ClusterStatus: str
        :param _ClusterName: 集群名称。
        :type ClusterName: str
        :param _Placement: 集群位置信息。
        :type Placement: :class:`tencentcloud.thpc.v20230321.models.Placement`
        :param _CreateTime: 集群创建时间。
        :type CreateTime: str
        :param _SchedulerType: 集群调度器。
        :type SchedulerType: str
        :param _SchedulerVersion: 集群调度器版本。
        :type SchedulerVersion: str
        :param _ComputeNodeCount: 计算节点数量。
        :type ComputeNodeCount: int
        :param _ComputeNodeSet: 计算节点概览。
        :type ComputeNodeSet: list of ComputeNodeOverview
        :param _ManagerNodeCount: 管控节点数量。
        :type ManagerNodeCount: int
        :param _ManagerNodeSet: 管控节点概览。
        :type ManagerNodeSet: list of ManagerNodeOverview
        :param _LoginNodeSet: 登录节点概览。
        :type LoginNodeSet: list of LoginNodeOverview
        :param _LoginNodeCount: 登录节点数量。
        :type LoginNodeCount: int
        :param _AutoScalingType: 弹性伸缩类型。
        :type AutoScalingType: str
        :param _VpcId: 集群所属私有网络ID。
        :type VpcId: str
        :param _ClusterType: 集群类型
        :type ClusterType: str
        """
        self._ClusterId = None
        self._ClusterStatus = None
        self._ClusterName = None
        self._Placement = None
        self._CreateTime = None
        self._SchedulerType = None
        self._SchedulerVersion = None
        self._ComputeNodeCount = None
        self._ComputeNodeSet = None
        self._ManagerNodeCount = None
        self._ManagerNodeSet = None
        self._LoginNodeSet = None
        self._LoginNodeCount = None
        self._AutoScalingType = None
        self._VpcId = None
        self._ClusterType = None

    @property
    def ClusterId(self):
        """集群ID。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterStatus(self):
        """集群状态。取值范围：<li>PENDING：创建中</li><li>INITING：初始化中</li><li>INIT_FAILED：初始化失败</li><li>RUNNING：运行中</li><li>TERMINATING：销毁中</li>
        :rtype: str
        """
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def ClusterName(self):
        """集群名称。
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Placement(self):
        """集群位置信息。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def CreateTime(self):
        """集群创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SchedulerType(self):
        """集群调度器。
        :rtype: str
        """
        return self._SchedulerType

    @SchedulerType.setter
    def SchedulerType(self, SchedulerType):
        self._SchedulerType = SchedulerType

    @property
    def SchedulerVersion(self):
        """集群调度器版本。
        :rtype: str
        """
        return self._SchedulerVersion

    @SchedulerVersion.setter
    def SchedulerVersion(self, SchedulerVersion):
        self._SchedulerVersion = SchedulerVersion

    @property
    def ComputeNodeCount(self):
        """计算节点数量。
        :rtype: int
        """
        return self._ComputeNodeCount

    @ComputeNodeCount.setter
    def ComputeNodeCount(self, ComputeNodeCount):
        self._ComputeNodeCount = ComputeNodeCount

    @property
    def ComputeNodeSet(self):
        """计算节点概览。
        :rtype: list of ComputeNodeOverview
        """
        return self._ComputeNodeSet

    @ComputeNodeSet.setter
    def ComputeNodeSet(self, ComputeNodeSet):
        self._ComputeNodeSet = ComputeNodeSet

    @property
    def ManagerNodeCount(self):
        """管控节点数量。
        :rtype: int
        """
        return self._ManagerNodeCount

    @ManagerNodeCount.setter
    def ManagerNodeCount(self, ManagerNodeCount):
        self._ManagerNodeCount = ManagerNodeCount

    @property
    def ManagerNodeSet(self):
        """管控节点概览。
        :rtype: list of ManagerNodeOverview
        """
        return self._ManagerNodeSet

    @ManagerNodeSet.setter
    def ManagerNodeSet(self, ManagerNodeSet):
        self._ManagerNodeSet = ManagerNodeSet

    @property
    def LoginNodeSet(self):
        """登录节点概览。
        :rtype: list of LoginNodeOverview
        """
        return self._LoginNodeSet

    @LoginNodeSet.setter
    def LoginNodeSet(self, LoginNodeSet):
        self._LoginNodeSet = LoginNodeSet

    @property
    def LoginNodeCount(self):
        """登录节点数量。
        :rtype: int
        """
        return self._LoginNodeCount

    @LoginNodeCount.setter
    def LoginNodeCount(self, LoginNodeCount):
        self._LoginNodeCount = LoginNodeCount

    @property
    def AutoScalingType(self):
        """弹性伸缩类型。
        :rtype: str
        """
        return self._AutoScalingType

    @AutoScalingType.setter
    def AutoScalingType(self, AutoScalingType):
        self._AutoScalingType = AutoScalingType

    @property
    def VpcId(self):
        """集群所属私有网络ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ClusterType(self):
        """集群类型
        :rtype: str
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterStatus = params.get("ClusterStatus")
        self._ClusterName = params.get("ClusterName")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._CreateTime = params.get("CreateTime")
        self._SchedulerType = params.get("SchedulerType")
        self._SchedulerVersion = params.get("SchedulerVersion")
        self._ComputeNodeCount = params.get("ComputeNodeCount")
        if params.get("ComputeNodeSet") is not None:
            self._ComputeNodeSet = []
            for item in params.get("ComputeNodeSet"):
                obj = ComputeNodeOverview()
                obj._deserialize(item)
                self._ComputeNodeSet.append(obj)
        self._ManagerNodeCount = params.get("ManagerNodeCount")
        if params.get("ManagerNodeSet") is not None:
            self._ManagerNodeSet = []
            for item in params.get("ManagerNodeSet"):
                obj = ManagerNodeOverview()
                obj._deserialize(item)
                self._ManagerNodeSet.append(obj)
        if params.get("LoginNodeSet") is not None:
            self._LoginNodeSet = []
            for item in params.get("LoginNodeSet"):
                obj = LoginNodeOverview()
                obj._deserialize(item)
                self._LoginNodeSet.append(obj)
        self._LoginNodeCount = params.get("LoginNodeCount")
        self._AutoScalingType = params.get("AutoScalingType")
        self._VpcId = params.get("VpcId")
        self._ClusterType = params.get("ClusterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeNode(AbstractModel):
    """计算节点信息。

    """

    def __init__(self):
        r"""
        :param _InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<li>PREPAID：预付费，即包年包月</li><li>POSTPAID_BY_HOUR：按小时后付费</li><li>SPOTPAID：竞价付费</li>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20230321.models.InstanceChargePrepaid`
        :param _InstanceType: 节点机型。不同实例机型指定了不同的资源规格。<li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。</li>
        :type InstanceType: str
        :param _SystemDisk: 节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.thpc.v20230321.models.SystemDisk`
        :param _DataDisks: 节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20230321.models.InternetAccessible`
        :param _InstanceName: 节点显示名称。<li>不指定节点显示名称则默认显示‘未命名’。
最多支持60个字符。</li>
        :type InstanceName: str
        :param _ProjectId: 实例所属项目ID。该参数可以通过调用 [DescribeProject](https://cloud.tencent.com/document/api/651/78725) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :type ProjectId: int
        :param _ResourceType: 实例资源类型，默认是CVM资源
        :type ResourceType: str
        """
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._InstanceType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._InternetAccessible = None
        self._InstanceName = None
        self._ProjectId = None
        self._ResourceType = None

    @property
    def InstanceChargeType(self):
        """节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<li>PREPAID：预付费，即包年包月</li><li>POSTPAID_BY_HOUR：按小时后付费</li><li>SPOTPAID：竞价付费</li>默认值：POSTPAID_BY_HOUR。
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        """预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def InstanceType(self):
        """节点机型。不同实例机型指定了不同的资源规格。<li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。</li>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        """节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def InternetAccessible(self):
        """公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceName(self):
        """节点显示名称。<li>不指定节点显示名称则默认显示‘未命名’。
最多支持60个字符。</li>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ProjectId(self):
        """实例所属项目ID。该参数可以通过调用 [DescribeProject](https://cloud.tencent.com/document/api/651/78725) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ResourceType(self):
        """实例资源类型，默认是CVM资源
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceName = params.get("InstanceName")
        self._ProjectId = params.get("ProjectId")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeNodeOverview(AbstractModel):
    """计算节点概览。

    """

    def __init__(self):
        r"""
        :param _NodeId: 计算节点ID。
        :type NodeId: str
        """
        self._NodeId = None

    @property
    def NodeId(self):
        """计算节点ID。
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
        


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Placement: 集群中实例所在的位置。
        :type Placement: :class:`tencentcloud.thpc.v20230321.models.Placement`
        :param _ManagerNode: 指定管理节点。
        :type ManagerNode: :class:`tencentcloud.thpc.v20230321.models.ManagerNode`
        :param _ManagerNodeCount: 指定管理节点的数量。默认取值：1。取值范围：1～2。
        :type ManagerNodeCount: int
        :param _ComputeNode: 指定计算节点。
        :type ComputeNode: :class:`tencentcloud.thpc.v20230321.models.ComputeNode`
        :param _ComputeNodeCount: 指定计算节点的数量。默认取值：0。
        :type ComputeNodeCount: int
        :param _SchedulerType: 调度器类型。默认取值：SLURM。<li>SGE：SGE调度器。</li><li>SLURM：SLURM调度器。</li>
        :type SchedulerType: str
        :param _SchedulerVersion: 创建调度器的版本号，可填写版本号为“latest” 和 各调度器支持的版本号；如果是"latest", 则代表创建的是平台当前支持的该类型调度器最新版本。如果不填写，默认创建的是“latest”版本调度器
各调度器支持的集群版本：
<li>SLURM：21.08.8、23.11.7</li>
<li>SGE：     8.1.9</li>
        :type SchedulerVersion: str
        :param _ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。目前支持部分公有镜像和自定义镜像。公共镜像请参考[镜像限制](https://cloud.tencent.com/document/product/1527/64818#.E9.95.9C.E5.83.8F)
        :type ImageId: str
        :param _VirtualPrivateCloud: 私有网络相关信息配置。
        :type VirtualPrivateCloud: :class:`tencentcloud.thpc.v20230321.models.VirtualPrivateCloud`
        :param _LoginSettings: 集群登录设置。
        :type LoginSettings: :class:`tencentcloud.thpc.v20230321.models.LoginSettings`
        :param _SecurityGroupIds: 集群中实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。
        :type SecurityGroupIds: list of str
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param _DryRun: 是否只预检此次请求。
true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和云服务器库存。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId.
false（默认）：发送正常请求，通过检查后直接创建实例
        :type DryRun: bool
        :param _AccountType: 域名字服务类型。默认取值：NIS。
<li>NIS：NIS域名字服务。</li>
        :type AccountType: str
        :param _ClusterName: 集群显示名称。
        :type ClusterName: str
        :param _StorageOption: 集群存储选项
        :type StorageOption: :class:`tencentcloud.thpc.v20230321.models.StorageOption`
        :param _LoginNode: 指定登录节点。
        :type LoginNode: :class:`tencentcloud.thpc.v20230321.models.LoginNode`
        :param _LoginNodeCount: 指定登录节点的数量。默认取值：0。取值范围：0～10。
        :type LoginNodeCount: int
        :param _Tags: 创建集群时同时绑定的标签对说明。
        :type Tags: list of Tag
        :param _AutoScalingType: 弹性伸缩类型。默认值：THPC_AS
        :type AutoScalingType: str
        :param _InitNodeScripts: 节点初始化脚本信息列表。
        :type InitNodeScripts: list of NodeScript
        :param _HpcClusterId: 高性能计算集群ID。若创建的实例为高性能计算实例，需指定实例放置的集群，否则不可指定。
        :type HpcClusterId: str
        """
        self._Placement = None
        self._ManagerNode = None
        self._ManagerNodeCount = None
        self._ComputeNode = None
        self._ComputeNodeCount = None
        self._SchedulerType = None
        self._SchedulerVersion = None
        self._ImageId = None
        self._VirtualPrivateCloud = None
        self._LoginSettings = None
        self._SecurityGroupIds = None
        self._ClientToken = None
        self._DryRun = None
        self._AccountType = None
        self._ClusterName = None
        self._StorageOption = None
        self._LoginNode = None
        self._LoginNodeCount = None
        self._Tags = None
        self._AutoScalingType = None
        self._InitNodeScripts = None
        self._HpcClusterId = None

    @property
    def Placement(self):
        """集群中实例所在的位置。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def ManagerNode(self):
        """指定管理节点。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.ManagerNode`
        """
        return self._ManagerNode

    @ManagerNode.setter
    def ManagerNode(self, ManagerNode):
        self._ManagerNode = ManagerNode

    @property
    def ManagerNodeCount(self):
        """指定管理节点的数量。默认取值：1。取值范围：1～2。
        :rtype: int
        """
        return self._ManagerNodeCount

    @ManagerNodeCount.setter
    def ManagerNodeCount(self, ManagerNodeCount):
        self._ManagerNodeCount = ManagerNodeCount

    @property
    def ComputeNode(self):
        """指定计算节点。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.ComputeNode`
        """
        return self._ComputeNode

    @ComputeNode.setter
    def ComputeNode(self, ComputeNode):
        self._ComputeNode = ComputeNode

    @property
    def ComputeNodeCount(self):
        """指定计算节点的数量。默认取值：0。
        :rtype: int
        """
        return self._ComputeNodeCount

    @ComputeNodeCount.setter
    def ComputeNodeCount(self, ComputeNodeCount):
        self._ComputeNodeCount = ComputeNodeCount

    @property
    def SchedulerType(self):
        """调度器类型。默认取值：SLURM。<li>SGE：SGE调度器。</li><li>SLURM：SLURM调度器。</li>
        :rtype: str
        """
        return self._SchedulerType

    @SchedulerType.setter
    def SchedulerType(self, SchedulerType):
        self._SchedulerType = SchedulerType

    @property
    def SchedulerVersion(self):
        """创建调度器的版本号，可填写版本号为“latest” 和 各调度器支持的版本号；如果是"latest", 则代表创建的是平台当前支持的该类型调度器最新版本。如果不填写，默认创建的是“latest”版本调度器
各调度器支持的集群版本：
<li>SLURM：21.08.8、23.11.7</li>
<li>SGE：     8.1.9</li>
        :rtype: str
        """
        return self._SchedulerVersion

    @SchedulerVersion.setter
    def SchedulerVersion(self, SchedulerVersion):
        self._SchedulerVersion = SchedulerVersion

    @property
    def ImageId(self):
        """指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。目前支持部分公有镜像和自定义镜像。公共镜像请参考[镜像限制](https://cloud.tencent.com/document/product/1527/64818#.E9.95.9C.E5.83.8F)
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def VirtualPrivateCloud(self):
        """私有网络相关信息配置。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.VirtualPrivateCloud`
        """
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def LoginSettings(self):
        """集群登录设置。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.LoginSettings`
        """
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SecurityGroupIds(self):
        """集群中实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def ClientToken(self):
        """用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        """是否只预检此次请求。
true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和云服务器库存。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId.
false（默认）：发送正常请求，通过检查后直接创建实例
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def AccountType(self):
        """域名字服务类型。默认取值：NIS。
<li>NIS：NIS域名字服务。</li>
        :rtype: str
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def ClusterName(self):
        """集群显示名称。
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def StorageOption(self):
        """集群存储选项
        :rtype: :class:`tencentcloud.thpc.v20230321.models.StorageOption`
        """
        return self._StorageOption

    @StorageOption.setter
    def StorageOption(self, StorageOption):
        self._StorageOption = StorageOption

    @property
    def LoginNode(self):
        """指定登录节点。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.LoginNode`
        """
        return self._LoginNode

    @LoginNode.setter
    def LoginNode(self, LoginNode):
        self._LoginNode = LoginNode

    @property
    def LoginNodeCount(self):
        """指定登录节点的数量。默认取值：0。取值范围：0～10。
        :rtype: int
        """
        return self._LoginNodeCount

    @LoginNodeCount.setter
    def LoginNodeCount(self, LoginNodeCount):
        self._LoginNodeCount = LoginNodeCount

    @property
    def Tags(self):
        """创建集群时同时绑定的标签对说明。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoScalingType(self):
        """弹性伸缩类型。默认值：THPC_AS
        :rtype: str
        """
        return self._AutoScalingType

    @AutoScalingType.setter
    def AutoScalingType(self, AutoScalingType):
        self._AutoScalingType = AutoScalingType

    @property
    def InitNodeScripts(self):
        """节点初始化脚本信息列表。
        :rtype: list of NodeScript
        """
        return self._InitNodeScripts

    @InitNodeScripts.setter
    def InitNodeScripts(self, InitNodeScripts):
        self._InitNodeScripts = InitNodeScripts

    @property
    def HpcClusterId(self):
        """高性能计算集群ID。若创建的实例为高性能计算实例，需指定实例放置的集群，否则不可指定。
        :rtype: str
        """
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        if params.get("ManagerNode") is not None:
            self._ManagerNode = ManagerNode()
            self._ManagerNode._deserialize(params.get("ManagerNode"))
        self._ManagerNodeCount = params.get("ManagerNodeCount")
        if params.get("ComputeNode") is not None:
            self._ComputeNode = ComputeNode()
            self._ComputeNode._deserialize(params.get("ComputeNode"))
        self._ComputeNodeCount = params.get("ComputeNodeCount")
        self._SchedulerType = params.get("SchedulerType")
        self._SchedulerVersion = params.get("SchedulerVersion")
        self._ImageId = params.get("ImageId")
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        self._AccountType = params.get("AccountType")
        self._ClusterName = params.get("ClusterName")
        if params.get("StorageOption") is not None:
            self._StorageOption = StorageOption()
            self._StorageOption._deserialize(params.get("StorageOption"))
        if params.get("LoginNode") is not None:
            self._LoginNode = LoginNode()
            self._LoginNode._deserialize(params.get("LoginNode"))
        self._LoginNodeCount = params.get("LoginNodeCount")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoScalingType = params.get("AutoScalingType")
        if params.get("InitNodeScripts") is not None:
            self._InitNodeScripts = []
            for item in params.get("InitNodeScripts"):
                obj = NodeScript()
                obj._deserialize(item)
                self._InitNodeScripts.append(obj)
        self._HpcClusterId = params.get("HpcClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterId = None
        self._RequestId = None

    @property
    def ClusterId(self):
        """集群ID。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
        self._ClusterId = params.get("ClusterId")
        self._RequestId = params.get("RequestId")


class CreateWorkspacesRequest(AbstractModel):
    """CreateWorkspaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目，所属宿主机（在专用宿主机上创建子机时指定）等属性。 <b>注：如果您不指定LaunchTemplate参数，则Placement为必选参数。若同时传递Placement和LaunchTemplate，则默认覆盖LaunchTemplate中对应的Placement的值。</b>
        :type Placement: :class:`tencentcloud.thpc.v20230321.models.SpacePlacement`
        :param _SpaceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type SpaceChargePrepaid: :class:`tencentcloud.thpc.v20230321.models.SpaceChargePrepaid`
        :param _SpaceChargeType: 工作空间计费类型，包括：PREPAID，UNDERWRITE。工作空间计费类型，包括：PREPAID，UNDERWRITE。
        :type SpaceChargeType: str
        :param _SpaceType: 工作空间规格
        :type SpaceType: str
        :param _ImageId: 镜像ID
        :type ImageId: str
        :param _SystemDisk: 工作空间系统盘信息
        :type SystemDisk: :class:`tencentcloud.thpc.v20230321.models.SpaceSystemDisk`
        :param _DataDisks: 工作空间数据盘信息
        :type DataDisks: list of SpaceDataDisk
        :param _VirtualPrivateCloud: 私有网络相关信息
        :type VirtualPrivateCloud: :class:`tencentcloud.thpc.v20230321.models.SpaceVirtualPrivateCloud`
        :param _InternetAccessible: 公网带宽相关信息设置
        :type InternetAccessible: :class:`tencentcloud.thpc.v20230321.models.SpaceInternetAccessible`
        :param _SpaceCount: 购买工作空间数量
        :type SpaceCount: int
        :param _SpaceName: 工作空间显示名称
        :type SpaceName: str
        :param _LoginSettings: 工作空间登陆设置
        :type LoginSettings: :class:`tencentcloud.thpc.v20230321.models.LoginSettings`
        :param _SecurityGroupIds: 工作空间所属安全组
        :type SecurityGroupIds: list of str
        :param _EnhancedService: 增强服务
        :type EnhancedService: :class:`tencentcloud.thpc.v20230321.models.EnhancedService`
        :param _DryRun: 是否只预检此次请求
        :type DryRun: bool
        :param _UserData: 提供给工作空间使用的用户数据
        :type UserData: str
        :param _DisasterRecoverGroupIds: 置放群组id
        :type DisasterRecoverGroupIds: list of str
        :param _TagSpecification: 标签描述列表
        :type TagSpecification: list of TagSpecification
        :param _HpcClusterId: 高性能计算集群ID
        :type HpcClusterId: str
        :param _CamRoleName: CAM角色名称
        :type CamRoleName: str
        :param _HostName: 实例主机名。<br><li>点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。</li><br><li>Windows 实例：主机名名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。</li><br><li>其他类型（Linux 等）实例：主机名字符长度为[2, 60]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。</li><br><li>购买多台实例，如果指定模式串`{R:x}`，表示生成数字`[x, x+n-1]`，其中`n`表示购买实例的数量，例如`server{R:3}`，购买1台时，实例主机名为`server3`；购买2台时，实例主机名分别为`server3`，`server4`。支持指定多个模式串`{R:x}`。</li><br><li>购买多台实例，如果不指定模式串，则在实例主机名添加后缀`1、2...n`，其中`n`表示购买实例的数量，例如`server`，购买2台时，实例主机名分别为`server1`，`server2`。</li>
        :type HostName: str
        """
        self._ClientToken = None
        self._Placement = None
        self._SpaceChargePrepaid = None
        self._SpaceChargeType = None
        self._SpaceType = None
        self._ImageId = None
        self._SystemDisk = None
        self._DataDisks = None
        self._VirtualPrivateCloud = None
        self._InternetAccessible = None
        self._SpaceCount = None
        self._SpaceName = None
        self._LoginSettings = None
        self._SecurityGroupIds = None
        self._EnhancedService = None
        self._DryRun = None
        self._UserData = None
        self._DisasterRecoverGroupIds = None
        self._TagSpecification = None
        self._HpcClusterId = None
        self._CamRoleName = None
        self._HostName = None

    @property
    def ClientToken(self):
        """用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def Placement(self):
        """实例所在的位置。通过该参数可以指定实例所属可用区，所属项目，所属宿主机（在专用宿主机上创建子机时指定）等属性。 <b>注：如果您不指定LaunchTemplate参数，则Placement为必选参数。若同时传递Placement和LaunchTemplate，则默认覆盖LaunchTemplate中对应的Placement的值。</b>
        :rtype: :class:`tencentcloud.thpc.v20230321.models.SpacePlacement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def SpaceChargePrepaid(self):
        """预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.SpaceChargePrepaid`
        """
        return self._SpaceChargePrepaid

    @SpaceChargePrepaid.setter
    def SpaceChargePrepaid(self, SpaceChargePrepaid):
        self._SpaceChargePrepaid = SpaceChargePrepaid

    @property
    def SpaceChargeType(self):
        """工作空间计费类型，包括：PREPAID，UNDERWRITE。工作空间计费类型，包括：PREPAID，UNDERWRITE。
        :rtype: str
        """
        return self._SpaceChargeType

    @SpaceChargeType.setter
    def SpaceChargeType(self, SpaceChargeType):
        self._SpaceChargeType = SpaceChargeType

    @property
    def SpaceType(self):
        """工作空间规格
        :rtype: str
        """
        return self._SpaceType

    @SpaceType.setter
    def SpaceType(self, SpaceType):
        self._SpaceType = SpaceType

    @property
    def ImageId(self):
        """镜像ID
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def SystemDisk(self):
        """工作空间系统盘信息
        :rtype: :class:`tencentcloud.thpc.v20230321.models.SpaceSystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """工作空间数据盘信息
        :rtype: list of SpaceDataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def VirtualPrivateCloud(self):
        """私有网络相关信息
        :rtype: :class:`tencentcloud.thpc.v20230321.models.SpaceVirtualPrivateCloud`
        """
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def InternetAccessible(self):
        """公网带宽相关信息设置
        :rtype: :class:`tencentcloud.thpc.v20230321.models.SpaceInternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def SpaceCount(self):
        """购买工作空间数量
        :rtype: int
        """
        return self._SpaceCount

    @SpaceCount.setter
    def SpaceCount(self, SpaceCount):
        self._SpaceCount = SpaceCount

    @property
    def SpaceName(self):
        """工作空间显示名称
        :rtype: str
        """
        return self._SpaceName

    @SpaceName.setter
    def SpaceName(self, SpaceName):
        self._SpaceName = SpaceName

    @property
    def LoginSettings(self):
        """工作空间登陆设置
        :rtype: :class:`tencentcloud.thpc.v20230321.models.LoginSettings`
        """
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SecurityGroupIds(self):
        """工作空间所属安全组
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def EnhancedService(self):
        """增强服务
        :rtype: :class:`tencentcloud.thpc.v20230321.models.EnhancedService`
        """
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def DryRun(self):
        """是否只预检此次请求
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def UserData(self):
        """提供给工作空间使用的用户数据
        :rtype: str
        """
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def DisasterRecoverGroupIds(self):
        """置放群组id
        :rtype: list of str
        """
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def TagSpecification(self):
        """标签描述列表
        :rtype: list of TagSpecification
        """
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def HpcClusterId(self):
        """高性能计算集群ID
        :rtype: str
        """
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def CamRoleName(self):
        """CAM角色名称
        :rtype: str
        """
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HostName(self):
        """实例主机名。<br><li>点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。</li><br><li>Windows 实例：主机名名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。</li><br><li>其他类型（Linux 等）实例：主机名字符长度为[2, 60]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。</li><br><li>购买多台实例，如果指定模式串`{R:x}`，表示生成数字`[x, x+n-1]`，其中`n`表示购买实例的数量，例如`server{R:3}`，购买1台时，实例主机名为`server3`；购买2台时，实例主机名分别为`server3`，`server4`。支持指定多个模式串`{R:x}`。</li><br><li>购买多台实例，如果不指定模式串，则在实例主机名添加后缀`1、2...n`，其中`n`表示购买实例的数量，例如`server`，购买2台时，实例主机名分别为`server1`，`server2`。</li>
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName


    def _deserialize(self, params):
        self._ClientToken = params.get("ClientToken")
        if params.get("Placement") is not None:
            self._Placement = SpacePlacement()
            self._Placement._deserialize(params.get("Placement"))
        if params.get("SpaceChargePrepaid") is not None:
            self._SpaceChargePrepaid = SpaceChargePrepaid()
            self._SpaceChargePrepaid._deserialize(params.get("SpaceChargePrepaid"))
        self._SpaceChargeType = params.get("SpaceChargeType")
        self._SpaceType = params.get("SpaceType")
        self._ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SpaceSystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = SpaceDataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = SpaceVirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = SpaceInternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._SpaceCount = params.get("SpaceCount")
        self._SpaceName = params.get("SpaceName")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._DryRun = params.get("DryRun")
        self._UserData = params.get("UserData")
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._HpcClusterId = params.get("HpcClusterId")
        self._CamRoleName = params.get("CamRoleName")
        self._HostName = params.get("HostName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkspacesResponse(AbstractModel):
    """CreateWorkspaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceIdSet: 工作空间ID
        :type SpaceIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SpaceIdSet = None
        self._RequestId = None

    @property
    def SpaceIdSet(self):
        """工作空间ID
        :rtype: list of str
        """
        return self._SpaceIdSet

    @SpaceIdSet.setter
    def SpaceIdSet(self, SpaceIdSet):
        self._SpaceIdSet = SpaceIdSet

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
        self._SpaceIdSet = params.get("SpaceIdSet")
        self._RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """描述了数据盘的信息

    """

    def __init__(self):
        r"""
        :param _DiskSize: 数据盘大小，单位：GB。最小调整步长为10G，不同数据盘类型取值范围不同，具体限制详见：[存储概述](https://cloud.tencent.com/document/product/213/4952)。默认值为0，表示不购买数据盘。更多限制详见产品文档。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _DiskType: 数据盘类型。数据盘类型限制详见[存储概述](https://cloud.tencent.com/document/product/213/4952)。取值范围：<br><li>LOCAL_NVME：本地NVME硬盘，与InstanceType强相关，不支持指定<br><li>LOCAL_PRO：本地HDD硬盘，与InstanceType强相关，不支持指定<br><li>CLOUD_BASIC：普通云硬盘<br><li>CLOUD_PREMIUM：高性能云硬盘<br><li>CLOUD_SSD：SSD云硬盘<br><li>CLOUD_HSSD：增强型SSD云硬盘<br><li>CLOUD_TSSD：极速型SSD云硬盘<br><li>CLOUD_BSSD：通用型SSD云硬盘
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        """
        self._DiskSize = None
        self._DiskType = None

    @property
    def DiskSize(self):
        """数据盘大小，单位：GB。最小调整步长为10G，不同数据盘类型取值范围不同，具体限制详见：[存储概述](https://cloud.tencent.com/document/product/213/4952)。默认值为0，表示不购买数据盘。更多限制详见产品文档。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskType(self):
        """数据盘类型。数据盘类型限制详见[存储概述](https://cloud.tencent.com/document/product/213/4952)。取值范围：<br><li>LOCAL_NVME：本地NVME硬盘，与InstanceType强相关，不支持指定<br><li>LOCAL_PRO：本地HDD硬盘，与InstanceType强相关，不支持指定<br><li>CLOUD_BASIC：普通云硬盘<br><li>CLOUD_PREMIUM：高性能云硬盘<br><li>CLOUD_SSD：SSD云硬盘<br><li>CLOUD_HSSD：增强型SSD云硬盘<br><li>CLOUD_TSSD：极速型SSD云硬盘<br><li>CLOUD_BSSD：通用型SSD云硬盘
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType


    def _deserialize(self, params):
        self._DiskSize = params.get("DiskSize")
        self._DiskType = params.get("DiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        """集群ID。
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
        


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster返回参数结构体

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


class DeleteClusterStorageOptionRequest(AbstractModel):
    """DeleteClusterStorageOption请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _LocalPath: 本地挂载路径。
        :type LocalPath: str
        """
        self._ClusterId = None
        self._LocalPath = None

    @property
    def ClusterId(self):
        """集群ID。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def LocalPath(self):
        """本地挂载路径。
        :rtype: str
        """
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._LocalPath = params.get("LocalPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterStorageOptionResponse(AbstractModel):
    """DeleteClusterStorageOption返回参数结构体

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


class DeleteNodesRequest(AbstractModel):
    """DeleteNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _NodeIds: 节点ID。
        :type NodeIds: list of str
        """
        self._ClusterId = None
        self._NodeIds = None

    @property
    def ClusterId(self):
        """集群ID。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodeIds(self):
        """节点ID。
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
        


class DeleteNodesResponse(AbstractModel):
    """DeleteNodes返回参数结构体

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


class DeleteQueueRequest(AbstractModel):
    """DeleteQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _QueueName: 队列名称。<br><li>最多支持32个字符。
        :type QueueName: str
        """
        self._ClusterId = None
        self._QueueName = None

    @property
    def ClusterId(self):
        """集群ID。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def QueueName(self):
        """队列名称。<br><li>最多支持32个字符。
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQueueResponse(AbstractModel):
    """DeleteQueue返回参数结构体

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


class DescribeAutoScalingConfigurationRequest(AbstractModel):
    """DescribeAutoScalingConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。	
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        """集群ID。	
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
        


class DescribeAutoScalingConfigurationResponse(AbstractModel):
    """DescribeAutoScalingConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _ExpansionBusyTime: 任务连续等待时间，队列的任务处于连续等待的时间。单位秒。
        :type ExpansionBusyTime: int
        :param _ShrinkIdleTime: 节点连续空闲（未运行作业）时间，一个节点连续处于空闲状态时间。
        :type ShrinkIdleTime: int
        :param _QueueConfigs: 扩容队列配置概览列表。
        :type QueueConfigs: list of QueueConfigOverview
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterId = None
        self._ExpansionBusyTime = None
        self._ShrinkIdleTime = None
        self._QueueConfigs = None
        self._RequestId = None

    @property
    def ClusterId(self):
        """集群ID。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ExpansionBusyTime(self):
        """任务连续等待时间，队列的任务处于连续等待的时间。单位秒。
        :rtype: int
        """
        return self._ExpansionBusyTime

    @ExpansionBusyTime.setter
    def ExpansionBusyTime(self, ExpansionBusyTime):
        self._ExpansionBusyTime = ExpansionBusyTime

    @property
    def ShrinkIdleTime(self):
        """节点连续空闲（未运行作业）时间，一个节点连续处于空闲状态时间。
        :rtype: int
        """
        return self._ShrinkIdleTime

    @ShrinkIdleTime.setter
    def ShrinkIdleTime(self, ShrinkIdleTime):
        self._ShrinkIdleTime = ShrinkIdleTime

    @property
    def QueueConfigs(self):
        """扩容队列配置概览列表。
        :rtype: list of QueueConfigOverview
        """
        return self._QueueConfigs

    @QueueConfigs.setter
    def QueueConfigs(self, QueueConfigs):
        self._QueueConfigs = QueueConfigs

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
        self._ClusterId = params.get("ClusterId")
        self._ExpansionBusyTime = params.get("ExpansionBusyTime")
        self._ShrinkIdleTime = params.get("ShrinkIdleTime")
        if params.get("QueueConfigs") is not None:
            self._QueueConfigs = []
            for item in params.get("QueueConfigs"):
                obj = QueueConfigOverview()
                obj._deserialize(item)
                self._QueueConfigs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterActivitiesRequest(AbstractModel):
    """DescribeClusterActivities请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。通过该参数指定需要查询活动历史记录的集群。
        :type ClusterId: str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self._ClusterId = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        """集群ID。通过该参数指定需要查询活动历史记录的集群。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Offset(self):
        """偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterActivitiesResponse(AbstractModel):
    """DescribeClusterActivities返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterActivitySet: 集群活动历史记录列表。
        :type ClusterActivitySet: list of ClusterActivity
        :param _TotalCount: 集群活动历史记录数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterActivitySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ClusterActivitySet(self):
        """集群活动历史记录列表。
        :rtype: list of ClusterActivity
        """
        return self._ClusterActivitySet

    @ClusterActivitySet.setter
    def ClusterActivitySet(self, ClusterActivitySet):
        self._ClusterActivitySet = ClusterActivitySet

    @property
    def TotalCount(self):
        """集群活动历史记录数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("ClusterActivitySet") is not None:
            self._ClusterActivitySet = []
            for item in params.get("ClusterActivitySet"):
                obj = ClusterActivity()
                obj._deserialize(item)
                self._ClusterActivitySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeClusterStorageOptionRequest(AbstractModel):
    """DescribeClusterStorageOption请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        """集群ID。
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
        


class DescribeClusterStorageOptionResponse(AbstractModel):
    """DescribeClusterStorageOption返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StorageOption: 集群存储选项信息概览。
        :type StorageOption: :class:`tencentcloud.thpc.v20230321.models.StorageOptionOverview`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StorageOption = None
        self._RequestId = None

    @property
    def StorageOption(self):
        """集群存储选项信息概览。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.StorageOptionOverview`
        """
        return self._StorageOption

    @StorageOption.setter
    def StorageOption(self, StorageOption):
        self._StorageOption = StorageOption

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
        if params.get("StorageOption") is not None:
            self._StorageOption = StorageOptionOverview()
            self._StorageOption._deserialize(params.get("StorageOption"))
        self._RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterIds: 集群ID列表。通过该参数可以指定需要查询信息的集群列表。<br>如果您不指定该参数，则返回Limit数量以内的集群信息。
        :type ClusterIds: list of str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Filters: <ul>
    <li><strong>cluster-type</strong>
        <p style="padding-left: 30px;">按照【<strong>集群类型</strong>】进行过滤</p>
        <p style="padding-left: 30px;">类型：String</p>
        <p style="padding-left: 30px;">必选：否</p>
    </li>
</ul>
<p style="padding-left: 30px;">每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。</p>
        :type Filters: list of Filter
        """
        self._ClusterIds = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ClusterIds(self):
        """集群ID列表。通过该参数可以指定需要查询信息的集群列表。<br>如果您不指定该参数，则返回Limit数量以内的集群信息。
        :rtype: list of str
        """
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

    @property
    def Offset(self):
        """偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """<ul>
    <li><strong>cluster-type</strong>
        <p style="padding-left: 30px;">按照【<strong>集群类型</strong>】进行过滤</p>
        <p style="padding-left: 30px;">类型：String</p>
        <p style="padding-left: 30px;">必选：否</p>
    </li>
</ul>
<p style="padding-left: 30px;">每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ClusterIds = params.get("ClusterIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterSet: 集群概览信息列表。
        :type ClusterSet: list of ClusterOverview
        :param _TotalCount: 集群数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ClusterSet(self):
        """集群概览信息列表。
        :rtype: list of ClusterOverview
        """
        return self._ClusterSet

    @ClusterSet.setter
    def ClusterSet(self, ClusterSet):
        self._ClusterSet = ClusterSet

    @property
    def TotalCount(self):
        """集群数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("ClusterSet") is not None:
            self._ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = ClusterOverview()
                obj._deserialize(item)
                self._ClusterSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeInitNodeScriptsRequest(AbstractModel):
    """DescribeInitNodeScripts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        """集群ID。
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
        


class DescribeInitNodeScriptsResponse(AbstractModel):
    """DescribeInitNodeScripts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InitNodeScriptSet: 节点初始化脚本列表。
        :type InitNodeScriptSet: list of NodeScript
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InitNodeScriptSet = None
        self._RequestId = None

    @property
    def InitNodeScriptSet(self):
        """节点初始化脚本列表。
        :rtype: list of NodeScript
        """
        return self._InitNodeScriptSet

    @InitNodeScriptSet.setter
    def InitNodeScriptSet(self, InitNodeScriptSet):
        self._InitNodeScriptSet = InitNodeScriptSet

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
        if params.get("InitNodeScriptSet") is not None:
            self._InitNodeScriptSet = []
            for item in params.get("InitNodeScriptSet"):
                obj = NodeScript()
                obj._deserialize(item)
                self._InitNodeScriptSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNodesRequest(AbstractModel):
    """DescribeNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _Filters: <ul>
    <li><strong>queue-name</strong>
        <p style="padding-left: 30px;">按照【<strong>队列名称</strong>】进行过滤。队列名称形如：compute。</p>
        <p style="padding-left: 30px;">类型：String</p>
        <p style="padding-left: 30px;">必选：否</p>
    </li>
    <li><strong>node-role</strong>
        <p style="padding-left: 30px;">按照【<strong>节点角色</strong>】进行过滤。节点角色形如：Manager。（Manager：管控节点。Compute：计算节点。Login：登录节点。ManagerBackup：备用管控节点。）</p>
        <p style="padding-left: 30px;">类型：String</p>
        <p style="padding-left: 30px;">必选：否</p>
    </li>
    <li><strong>node-type</strong>
        <p style="padding-left: 30px;">按照【<strong>节点类型</strong>】进行过滤。节点类型形如：STATIC。(STATIC：静态节点。DYNAMIC：弹性节点。)</p>
        <p style="padding-left: 30px;">类型：String</p>
        <p style="padding-left: 30px;">必选：否</p>
    </li>
</ul>
<p style="padding-left: 30px;">每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。</p>
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self._ClusterId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        """集群ID。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Filters(self):
        """<ul>
    <li><strong>queue-name</strong>
        <p style="padding-left: 30px;">按照【<strong>队列名称</strong>】进行过滤。队列名称形如：compute。</p>
        <p style="padding-left: 30px;">类型：String</p>
        <p style="padding-left: 30px;">必选：否</p>
    </li>
    <li><strong>node-role</strong>
        <p style="padding-left: 30px;">按照【<strong>节点角色</strong>】进行过滤。节点角色形如：Manager。（Manager：管控节点。Compute：计算节点。Login：登录节点。ManagerBackup：备用管控节点。）</p>
        <p style="padding-left: 30px;">类型：String</p>
        <p style="padding-left: 30px;">必选：否</p>
    </li>
    <li><strong>node-type</strong>
        <p style="padding-left: 30px;">按照【<strong>节点类型</strong>】进行过滤。节点类型形如：STATIC。(STATIC：静态节点。DYNAMIC：弹性节点。)</p>
        <p style="padding-left: 30px;">类型：String</p>
        <p style="padding-left: 30px;">必选：否</p>
    </li>
</ul>
<p style="padding-left: 30px;">每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
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
        


class DescribeNodesResponse(AbstractModel):
    """DescribeNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeSet: 节点概览信息列表。
        :type NodeSet: list of NodeOverview
        :param _TotalCount: 符合条件的节点数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NodeSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NodeSet(self):
        """节点概览信息列表。
        :rtype: list of NodeOverview
        """
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def TotalCount(self):
        """符合条件的节点数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = NodeOverview()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeQueuesRequest(AbstractModel):
    """DescribeQueues请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self._ClusterId = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        """集群ID。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Offset(self):
        """偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQueuesResponse(AbstractModel):
    """DescribeQueues返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueSet: 队列概览信息列表。
        :type QueueSet: list of QueueOverview
        :param _TotalCount: 符合条件的队列数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QueueSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def QueueSet(self):
        """队列概览信息列表。
        :rtype: list of QueueOverview
        """
        return self._QueueSet

    @QueueSet.setter
    def QueueSet(self, QueueSet):
        self._QueueSet = QueueSet

    @property
    def TotalCount(self):
        """符合条件的队列数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("QueueSet") is not None:
            self._QueueSet = []
            for item in params.get("QueueSet"):
                obj = QueueOverview()
                obj._deserialize(item)
                self._QueueSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeWorkspacesRequest(AbstractModel):
    """DescribeWorkspaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceIds: 集群ID列表。通过该参数可以指定需要查询信息的集群列表。<br>如果您不指定该参数，则返回Limit数量以内的集群信息。
        :type SpaceIds: list of str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Filters: 过滤列表
        :type Filters: list of Filter
        """
        self._SpaceIds = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def SpaceIds(self):
        """集群ID列表。通过该参数可以指定需要查询信息的集群列表。<br>如果您不指定该参数，则返回Limit数量以内的集群信息。
        :rtype: list of str
        """
        return self._SpaceIds

    @SpaceIds.setter
    def SpaceIds(self, SpaceIds):
        self._SpaceIds = SpaceIds

    @property
    def Offset(self):
        """偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """过滤列表
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._SpaceIds = params.get("SpaceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeWorkspacesResponse(AbstractModel):
    """DescribeWorkspaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceSet: 集群概览信息列表
        :type SpaceSet: list of SpaceInfo
        :param _TotalCount: 集群数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SpaceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SpaceSet(self):
        """集群概览信息列表
        :rtype: list of SpaceInfo
        """
        return self._SpaceSet

    @SpaceSet.setter
    def SpaceSet(self, SpaceSet):
        self._SpaceSet = SpaceSet

    @property
    def TotalCount(self):
        """集群数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("SpaceSet") is not None:
            self._SpaceSet = []
            for item in params.get("SpaceSet"):
                obj = SpaceInfo()
                obj._deserialize(item)
                self._SpaceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DetachNodesRequest(AbstractModel):
    """DetachNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _NodeIds: 集群中的节点id
        :type NodeIds: list of str
        """
        self._ClusterId = None
        self._NodeIds = None

    @property
    def ClusterId(self):
        """集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodeIds(self):
        """集群中的节点id
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
        


class DetachNodesResponse(AbstractModel):
    """DetachNodes返回参数结构体

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


class EnhancedService(AbstractModel):
    """描述了实例的增强服务启用情况与其设置，如云安全，腾讯云可观测平台等实例 Agent

    """

    def __init__(self):
        r"""
        :param _SecurityService: 开启云安全服务。若不指定该参数，则默认开启云安全服务。
        :type SecurityService: :class:`tencentcloud.thpc.v20230321.models.RunSecurityServiceEnabled`
        :param _MonitorService: 开启腾讯云可观测平台服务。若不指定该参数，则默认开启腾讯云可观测平台服务。
        :type MonitorService: :class:`tencentcloud.thpc.v20230321.models.RunMonitorServiceEnabled`
        :param _AutomationService: 开启云自动化助手服务（TencentCloud Automation Tools，TAT）。若不指定该参数，默认开启云自动化助手服务。
        :type AutomationService: :class:`tencentcloud.thpc.v20230321.models.RunAutomationServiceEnabled`
        """
        self._SecurityService = None
        self._MonitorService = None
        self._AutomationService = None

    @property
    def SecurityService(self):
        """开启云安全服务。若不指定该参数，则默认开启云安全服务。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.RunSecurityServiceEnabled`
        """
        return self._SecurityService

    @SecurityService.setter
    def SecurityService(self, SecurityService):
        self._SecurityService = SecurityService

    @property
    def MonitorService(self):
        """开启腾讯云可观测平台服务。若不指定该参数，则默认开启腾讯云可观测平台服务。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.RunMonitorServiceEnabled`
        """
        return self._MonitorService

    @MonitorService.setter
    def MonitorService(self, MonitorService):
        self._MonitorService = MonitorService

    @property
    def AutomationService(self):
        """开启云自动化助手服务（TencentCloud Automation Tools，TAT）。若不指定该参数，默认开启云自动化助手服务。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.RunAutomationServiceEnabled`
        """
        return self._AutomationService

    @AutomationService.setter
    def AutomationService(self, AutomationService):
        self._AutomationService = AutomationService


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self._SecurityService = RunSecurityServiceEnabled()
            self._SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self._MonitorService = RunMonitorServiceEnabled()
            self._MonitorService._deserialize(params.get("MonitorService"))
        if params.get("AutomationService") is not None:
            self._AutomationService = RunAutomationServiceEnabled()
            self._AutomationService._deserialize(params.get("AutomationService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpansionNodeConfig(AbstractModel):
    """弹性扩容节点配置信息。

    """

    def __init__(self):
        r"""
        :param _Placement: 扩容实例所在的位置。
        :type Placement: :class:`tencentcloud.thpc.v20230321.models.Placement`
        :param _InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月</li><br><li>POSTPAID_BY_HOUR：按小时后付费</li><br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。</li>
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20230321.models.InstanceChargePrepaid`
        :param _InstanceType: 节点机型。不同实例机型指定了不同的资源规格。
<br><li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。</li>
        :type InstanceType: str
        :param _VirtualPrivateCloud: 私有网络相关信息配置。
        :type VirtualPrivateCloud: :class:`tencentcloud.thpc.v20230321.models.VirtualPrivateCloud`
        :param _ProjectId: 实例所属项目ID。该参数可以通过调用 [DescribeProject](https://cloud.tencent.com/document/api/651/78725) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :type ProjectId: int
        """
        self._Placement = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._InstanceType = None
        self._VirtualPrivateCloud = None
        self._ProjectId = None

    @property
    def Placement(self):
        """扩容实例所在的位置。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def InstanceChargeType(self):
        """节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月</li><br><li>POSTPAID_BY_HOUR：按小时后付费</li><br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。</li>
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        """预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def InstanceType(self):
        """节点机型。不同实例机型指定了不同的资源规格。
<br><li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。</li>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def VirtualPrivateCloud(self):
        """私有网络相关信息配置。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.VirtualPrivateCloud`
        """
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def ProjectId(self):
        """实例所属项目ID。该参数可以通过调用 [DescribeProject](https://cloud.tencent.com/document/api/651/78725) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._InstanceType = params.get("InstanceType")
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpansionNodeConfigOverview(AbstractModel):
    """扩容节点配置信息概览。

    """

    def __init__(self):
        r"""
        :param _InstanceType: 节点机型。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _Placement: 扩容实例所在的位置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Placement: :class:`tencentcloud.thpc.v20230321.models.Placement`
        :param _InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20230321.models.InstanceChargePrepaid`
        :param _VirtualPrivateCloud: 私有网络相关信息配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualPrivateCloud: :class:`tencentcloud.thpc.v20230321.models.VirtualPrivateCloud`
        :param _ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param _InternetAccessible: 公网带宽相关信息设置。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20230321.models.InternetAccessible`
        :param _SystemDisk: 节点系统盘配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemDisk: :class:`tencentcloud.thpc.v20230321.models.SystemDisk`
        :param _DataDisks: 节点数据盘配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDisks: list of DataDisk
        """
        self._InstanceType = None
        self._Placement = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._VirtualPrivateCloud = None
        self._ImageId = None
        self._InternetAccessible = None
        self._SystemDisk = None
        self._DataDisks = None

    @property
    def InstanceType(self):
        """节点机型。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Placement(self):
        """扩容实例所在的位置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def InstanceChargeType(self):
        """节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        """预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def VirtualPrivateCloud(self):
        """私有网络相关信息配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.VirtualPrivateCloud`
        """
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def ImageId(self):
        """指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def InternetAccessible(self):
        """公网带宽相关信息设置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def SystemDisk(self):
        """节点系统盘配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """节点数据盘配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self._ImageId = params.get("ImageId")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """>描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    > * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。

    """

    def __init__(self):
        r"""
        :param _Name: 需要过滤的字段。
        :type Name: str
        :param _Values: 字段的过滤值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """需要过滤的字段。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """字段的过滤值。
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
        


class GooseFSOption(AbstractModel):
    """描述GooseFS挂载信息

    """

    def __init__(self):
        r"""
        :param _LocalPath: 文件系统本地挂载路径。
        :type LocalPath: str
        :param _RemotePath: 文件系统远程挂载路径。
        :type RemotePath: str
        :param _Masters: 文件系统master的ip和端口。
        :type Masters: list of str
        """
        self._LocalPath = None
        self._RemotePath = None
        self._Masters = None

    @property
    def LocalPath(self):
        """文件系统本地挂载路径。
        :rtype: str
        """
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath

    @property
    def RemotePath(self):
        """文件系统远程挂载路径。
        :rtype: str
        """
        return self._RemotePath

    @RemotePath.setter
    def RemotePath(self, RemotePath):
        self._RemotePath = RemotePath

    @property
    def Masters(self):
        """文件系统master的ip和端口。
        :rtype: list of str
        """
        return self._Masters

    @Masters.setter
    def Masters(self, Masters):
        self._Masters = Masters


    def _deserialize(self, params):
        self._LocalPath = params.get("LocalPath")
        self._RemotePath = params.get("RemotePath")
        self._Masters = params.get("Masters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GooseFSOptionOverview(AbstractModel):
    """GooseFS存储选项概览信息。

    """

    def __init__(self):
        r"""
        :param _LocalPath: 文件系统本地挂载路径。
        :type LocalPath: str
        :param _RemotePath: 文件系统远程挂载路径。
        :type RemotePath: str
        :param _Masters: 文件系统master的ip和端口。
        :type Masters: list of str
        """
        self._LocalPath = None
        self._RemotePath = None
        self._Masters = None

    @property
    def LocalPath(self):
        """文件系统本地挂载路径。
        :rtype: str
        """
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath

    @property
    def RemotePath(self):
        """文件系统远程挂载路径。
        :rtype: str
        """
        return self._RemotePath

    @RemotePath.setter
    def RemotePath(self, RemotePath):
        self._RemotePath = RemotePath

    @property
    def Masters(self):
        """文件系统master的ip和端口。
        :rtype: list of str
        """
        return self._Masters

    @Masters.setter
    def Masters(self, Masters):
        self._Masters = Masters


    def _deserialize(self, params):
        self._LocalPath = params.get("LocalPath")
        self._RemotePath = params.get("RemotePath")
        self._Masters = params.get("Masters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GooseFSxOption(AbstractModel):
    """描述GooseFSx挂载信息

    """

    def __init__(self):
        r"""
        :param _Masters: 文件系统master的ip和端口列表。
        :type Masters: list of str
        :param _LocalPath: 文件系统的本地挂载路径。GooseFSx目前只支持挂载在/goosefsx/{文件系统ID}_proxy/目录下。
        :type LocalPath: str
        """
        self._Masters = None
        self._LocalPath = None

    @property
    def Masters(self):
        """文件系统master的ip和端口列表。
        :rtype: list of str
        """
        return self._Masters

    @Masters.setter
    def Masters(self, Masters):
        self._Masters = Masters

    @property
    def LocalPath(self):
        """文件系统的本地挂载路径。GooseFSx目前只支持挂载在/goosefsx/{文件系统ID}_proxy/目录下。
        :rtype: str
        """
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath


    def _deserialize(self, params):
        self._Masters = params.get("Masters")
        self._LocalPath = params.get("LocalPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GooseFSxOptionOverview(AbstractModel):
    """GooseFSx存储选项概览信息。

    """

    def __init__(self):
        r"""
        :param _Masters: 文件系统master的ip和端口列表。
        :type Masters: list of str
        :param _LocalPath: 文件系统的本地挂载路径。GooseFSx目前只支持挂载在/goosefsx/{文件系统ID}_proxy/目录下。
        :type LocalPath: str
        """
        self._Masters = None
        self._LocalPath = None

    @property
    def Masters(self):
        """文件系统master的ip和端口列表。
        :rtype: list of str
        """
        return self._Masters

    @Masters.setter
    def Masters(self, Masters):
        self._Masters = Masters

    @property
    def LocalPath(self):
        """文件系统的本地挂载路径。GooseFSx目前只支持挂载在/goosefsx/{文件系统ID}_proxy/目录下。
        :rtype: str
        """
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath


    def _deserialize(self, params):
        self._Masters = params.get("Masters")
        self._LocalPath = params.get("LocalPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargePrepaid(AbstractModel):
    """描述了实例的计费模式

    """

    def __init__(self):
        r"""
        :param _Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60。
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: int
        :param _RenewFlag: 自动续费标识。取值范围：
NOTIFY_AND_AUTO_RENEW：通知过期且自动续费
NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费
DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费

默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        """购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        """自动续费标识。取值范围：
NOTIFY_AND_AUTO_RENEW：通知过期且自动续费
NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费
DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费

默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAccessible(AbstractModel):
    """描述了实例的公网可访问性，声明了实例的公网使用计费模式，最大带宽等

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: 网络计费类型。取值范围：
BANDWIDTH_PREPAID：预付费按带宽结算
TRAFFIC_POSTPAID_BY_HOUR：流量按小时后付费
BANDWIDTH_POSTPAID_BY_HOUR：带宽按小时后付费
BANDWIDTH_PACKAGE：带宽包用户
默认取值：非带宽包用户默认与子机付费类型保持一致。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: 公网出带宽上限，单位：Mbps。默认值：0Mbps。不同机型带宽上限范围不一致，具体限制详见购买网络带宽。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetMaxBandwidthOut: int
        """
        self._InternetChargeType = None
        self._InternetMaxBandwidthOut = None

    @property
    def InternetChargeType(self):
        """网络计费类型。取值范围：
BANDWIDTH_PREPAID：预付费按带宽结算
TRAFFIC_POSTPAID_BY_HOUR：流量按小时后付费
BANDWIDTH_POSTPAID_BY_HOUR：带宽按小时后付费
BANDWIDTH_PACKAGE：带宽包用户
默认取值：非带宽包用户默认与子机付费类型保持一致。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        """公网出带宽上限，单位：Mbps。默认值：0Mbps。不同机型带宽上限范围不一致，具体限制详见购买网络带宽。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut


    def _deserialize(self, params):
        self._InternetChargeType = params.get("InternetChargeType")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginNode(AbstractModel):
    """登录节点信息。

    """

    def __init__(self):
        r"""
        :param _InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月</li><br><li>POSTPAID_BY_HOUR：按小时后付费</li><br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。</li>
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20230321.models.InstanceChargePrepaid`
        :param _InstanceType: 节点机型。不同实例机型指定了不同的资源规格。
<br><li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。</li>
        :type InstanceType: str
        :param _SystemDisk: 节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.thpc.v20230321.models.SystemDisk`
        :param _DataDisks: 节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20230321.models.InternetAccessible`
        :param _InstanceName: 节点显示名称。<br><li>
不指定节点显示名称则默认显示‘未命名’。
最多支持60个字符。</li>
        :type InstanceName: str
        :param _ProjectId: 实例所属项目ID。该参数可以通过调用 [DescribeProject](https://cloud.tencent.com/document/api/651/78725) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :type ProjectId: int
        """
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._InstanceType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._InternetAccessible = None
        self._InstanceName = None
        self._ProjectId = None

    @property
    def InstanceChargeType(self):
        """节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月</li><br><li>POSTPAID_BY_HOUR：按小时后付费</li><br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。</li>
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        """预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def InstanceType(self):
        """节点机型。不同实例机型指定了不同的资源规格。
<br><li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。</li>
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        """节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def InternetAccessible(self):
        """公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceName(self):
        """节点显示名称。<br><li>
不指定节点显示名称则默认显示‘未命名’。
最多支持60个字符。</li>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ProjectId(self):
        """实例所属项目ID。该参数可以通过调用 [DescribeProject](https://cloud.tencent.com/document/api/651/78725) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceName = params.get("InstanceName")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginNodeOverview(AbstractModel):
    """登录节点概览。

    """

    def __init__(self):
        r"""
        :param _NodeId: 登录节点ID。
        :type NodeId: str
        """
        self._NodeId = None

    @property
    def NodeId(self):
        """登录节点ID。
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
        


class LoginSettings(AbstractModel):
    """描述了实例登录相关配置与信息。

    """

    def __init__(self):
        r"""
        :param _Password: 实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：<br><li>Linux实例密码必须8到30位，至少包括两项[a-z]，[A-Z]、[0-9] 和 [( ) \` ~ ! @ # $ % ^ & *  - + = | { } [ ] : ; ' , . ? / ]中的特殊符号。</li><br><li>Windows实例密码必须12到30位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) \` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? /]中的特殊符号。</li><br><br>若不指定该参数，则由系统随机生成密码，并通过站内信方式通知到用户。
        :type Password: str
        :param _KeyIds: 实例登录密钥
        :type KeyIds: list of str
        """
        self._Password = None
        self._KeyIds = None

    @property
    def Password(self):
        """实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：<br><li>Linux实例密码必须8到30位，至少包括两项[a-z]，[A-Z]、[0-9] 和 [( ) \` ~ ! @ # $ % ^ & *  - + = | { } [ ] : ; ' , . ? / ]中的特殊符号。</li><br><li>Windows实例密码必须12到30位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) \` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? /]中的特殊符号。</li><br><br>若不指定该参数，则由系统随机生成密码，并通过站内信方式通知到用户。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def KeyIds(self):
        """实例登录密钥
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._Password = params.get("Password")
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagerNode(AbstractModel):
    """管控节点信息

    """

    def __init__(self):
        r"""
        :param _InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月</li><br><li>POSTPAID_BY_HOUR：按小时后付费</li><br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。</li>	
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20230321.models.InstanceChargePrepaid`
        :param _InstanceType: 节点机型。不同实例机型指定了不同的资源规格。 <br><li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。</li>	
        :type InstanceType: str
        :param _SystemDisk: 节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.thpc.v20230321.models.SystemDisk`
        :param _DataDisks: 节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20230321.models.InternetAccessible`
        :param _InstanceName: 节点显示名称。<br><li> 不指定节点显示名称则默认显示‘未命名’。 </li><li>购买多个节点，如果指定模式串`{R:x}`，表示生成数字[`[x, x+n-1]`，其中`n`表示购买节点的数量，例如`server_{R:3}`，购买1个时，节点显示名称为`server_3`；购买2个时，节点显示名称分别为`server_3`，`server_4`。支持指定多个模式串`{R:x}`。 购买多个节点，如果不指定模式串，则在节点显示名称添加后缀`1、2...n`，其中`n`表示购买节点的数量，例如`server_`，购买2个时，节点显示名称分别为`server_1`，`server_2`。</li><li> 最多支持60个字符（包含模式串）。</li>
        :type InstanceName: str
        :param _ProjectId: 实例所属项目ID。该参数可以通过调用 [DescribeProject](https://cloud.tencent.com/document/api/651/78725) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :type ProjectId: int
        :param _EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、腾讯云可观测平台等服务。若不指定该参数，则默认开启腾讯云可观测平台、云安全服务、自动化助手服务。
        :type EnhancedService: :class:`tencentcloud.thpc.v20230321.models.EnhancedService`
        """
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._InstanceType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._InternetAccessible = None
        self._InstanceName = None
        self._ProjectId = None
        self._EnhancedService = None

    @property
    def InstanceChargeType(self):
        """节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月</li><br><li>POSTPAID_BY_HOUR：按小时后付费</li><br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。</li>	
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        """预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def InstanceType(self):
        """节点机型。不同实例机型指定了不同的资源规格。 <br><li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。</li>	
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        """节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def InternetAccessible(self):
        """公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceName(self):
        """节点显示名称。<br><li> 不指定节点显示名称则默认显示‘未命名’。 </li><li>购买多个节点，如果指定模式串`{R:x}`，表示生成数字[`[x, x+n-1]`，其中`n`表示购买节点的数量，例如`server_{R:3}`，购买1个时，节点显示名称为`server_3`；购买2个时，节点显示名称分别为`server_3`，`server_4`。支持指定多个模式串`{R:x}`。 购买多个节点，如果不指定模式串，则在节点显示名称添加后缀`1、2...n`，其中`n`表示购买节点的数量，例如`server_`，购买2个时，节点显示名称分别为`server_1`，`server_2`。</li><li> 最多支持60个字符（包含模式串）。</li>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ProjectId(self):
        """实例所属项目ID。该参数可以通过调用 [DescribeProject](https://cloud.tencent.com/document/api/651/78725) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def EnhancedService(self):
        """增强服务。通过该参数可以指定是否开启云安全、腾讯云可观测平台等服务。若不指定该参数，则默认开启腾讯云可观测平台、云安全服务、自动化助手服务。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.EnhancedService`
        """
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService


    def _deserialize(self, params):
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceName = params.get("InstanceName")
        self._ProjectId = params.get("ProjectId")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagerNodeOverview(AbstractModel):
    """管控节点概览。

    """

    def __init__(self):
        r"""
        :param _NodeId: 管控节点ID。
        :type NodeId: str
        """
        self._NodeId = None

    @property
    def NodeId(self):
        """管控节点ID。
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
        


class ModifyInitNodeScriptsRequest(AbstractModel):
    """ModifyInitNodeScripts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _InitNodeScripts: 节点初始化脚本信息列表。
        :type InitNodeScripts: list of NodeScript
        """
        self._ClusterId = None
        self._InitNodeScripts = None

    @property
    def ClusterId(self):
        """集群ID。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InitNodeScripts(self):
        """节点初始化脚本信息列表。
        :rtype: list of NodeScript
        """
        return self._InitNodeScripts

    @InitNodeScripts.setter
    def InitNodeScripts(self, InitNodeScripts):
        self._InitNodeScripts = InitNodeScripts


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("InitNodeScripts") is not None:
            self._InitNodeScripts = []
            for item in params.get("InitNodeScripts"):
                obj = NodeScript()
                obj._deserialize(item)
                self._InitNodeScripts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInitNodeScriptsResponse(AbstractModel):
    """ModifyInitNodeScripts返回参数结构体

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


class ModifyWorkspacesAttributeRequest(AbstractModel):
    """ModifyWorkspacesAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceIds: 工作空间列表
        :type SpaceIds: list of str
        :param _SpaceName: 修改后的工作空间名称。可任意命名，但不得超过60个字符。
        :type SpaceName: str
        """
        self._SpaceIds = None
        self._SpaceName = None

    @property
    def SpaceIds(self):
        """工作空间列表
        :rtype: list of str
        """
        return self._SpaceIds

    @SpaceIds.setter
    def SpaceIds(self, SpaceIds):
        self._SpaceIds = SpaceIds

    @property
    def SpaceName(self):
        """修改后的工作空间名称。可任意命名，但不得超过60个字符。
        :rtype: str
        """
        return self._SpaceName

    @SpaceName.setter
    def SpaceName(self, SpaceName):
        self._SpaceName = SpaceName


    def _deserialize(self, params):
        self._SpaceIds = params.get("SpaceIds")
        self._SpaceName = params.get("SpaceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkspacesAttributeResponse(AbstractModel):
    """ModifyWorkspacesAttribute返回参数结构体

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


class NodeActivity(AbstractModel):
    """节点活动信息。

    """

    def __init__(self):
        r"""
        :param _NodeInstanceId: 节点活动所在的实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeInstanceId: str
        :param _NodeActivityStatus: 节点活动状态。取值范围：<br><li>RUNNING：运行中</li><br><li>SUCCESSFUL：活动成功</li><br><li>FAILED：活动失败</li>
        :type NodeActivityStatus: str
        :param _NodeActivityStatusCode: 节点活动状态码。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeActivityStatusCode: str
        :param _NodeActivityStatusReason: 节点活动状态原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeActivityStatusReason: str
        """
        self._NodeInstanceId = None
        self._NodeActivityStatus = None
        self._NodeActivityStatusCode = None
        self._NodeActivityStatusReason = None

    @property
    def NodeInstanceId(self):
        """节点活动所在的实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeInstanceId

    @NodeInstanceId.setter
    def NodeInstanceId(self, NodeInstanceId):
        self._NodeInstanceId = NodeInstanceId

    @property
    def NodeActivityStatus(self):
        """节点活动状态。取值范围：<br><li>RUNNING：运行中</li><br><li>SUCCESSFUL：活动成功</li><br><li>FAILED：活动失败</li>
        :rtype: str
        """
        return self._NodeActivityStatus

    @NodeActivityStatus.setter
    def NodeActivityStatus(self, NodeActivityStatus):
        self._NodeActivityStatus = NodeActivityStatus

    @property
    def NodeActivityStatusCode(self):
        """节点活动状态码。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeActivityStatusCode

    @NodeActivityStatusCode.setter
    def NodeActivityStatusCode(self, NodeActivityStatusCode):
        self._NodeActivityStatusCode = NodeActivityStatusCode

    @property
    def NodeActivityStatusReason(self):
        """节点活动状态原因。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeActivityStatusReason

    @NodeActivityStatusReason.setter
    def NodeActivityStatusReason(self, NodeActivityStatusReason):
        self._NodeActivityStatusReason = NodeActivityStatusReason


    def _deserialize(self, params):
        self._NodeInstanceId = params.get("NodeInstanceId")
        self._NodeActivityStatus = params.get("NodeActivityStatus")
        self._NodeActivityStatusCode = params.get("NodeActivityStatusCode")
        self._NodeActivityStatusReason = params.get("NodeActivityStatusReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeOverview(AbstractModel):
    """节点概览信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 节点实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _Zone: 节点所在可用区信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _NodeState: 节点状态。<li>SUBMITTED：已完成提交。</li><li>CREATING：创建中。</li><li>CREATED：完成创建。</li><li>INITING：初始化中。</li><li>INIT_FAILED：初始化失败。</li><li>RUNNING：运行中。</li><li>DELETING：销毁中。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeState: str
        :param _ImageId: 镜像ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param _QueueName: 节点所属队列名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueName: str
        :param _NodeRole: 节点角色。<li>Manager：管控节点。</li><li>Compute：计算节点。</li><li>Login：登录节点。</li><li>ManagerBackup：备用管控节点。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeRole: str
        :param _NodeType: 节点类型。<li>STATIC：静态节点。</li><li>DYNAMIC：弹性节点。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: str
        :param _NodeId: thpc集群节点id
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: str
        :param _NodeAllocateState: 节点的工作状态
        :type NodeAllocateState: str
        """
        self._InstanceId = None
        self._Zone = None
        self._NodeState = None
        self._ImageId = None
        self._QueueName = None
        self._NodeRole = None
        self._NodeType = None
        self._NodeId = None
        self._NodeAllocateState = None

    @property
    def InstanceId(self):
        """节点实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Zone(self):
        """节点所在可用区信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NodeState(self):
        """节点状态。<li>SUBMITTED：已完成提交。</li><li>CREATING：创建中。</li><li>CREATED：完成创建。</li><li>INITING：初始化中。</li><li>INIT_FAILED：初始化失败。</li><li>RUNNING：运行中。</li><li>DELETING：销毁中。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeState

    @NodeState.setter
    def NodeState(self, NodeState):
        self._NodeState = NodeState

    @property
    def ImageId(self):
        """镜像ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def QueueName(self):
        """节点所属队列名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def NodeRole(self):
        """节点角色。<li>Manager：管控节点。</li><li>Compute：计算节点。</li><li>Login：登录节点。</li><li>ManagerBackup：备用管控节点。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def NodeType(self):
        """节点类型。<li>STATIC：静态节点。</li><li>DYNAMIC：弹性节点。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeId(self):
        """thpc集群节点id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeAllocateState(self):
        """节点的工作状态
        :rtype: str
        """
        return self._NodeAllocateState

    @NodeAllocateState.setter
    def NodeAllocateState(self, NodeAllocateState):
        self._NodeAllocateState = NodeAllocateState


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Zone = params.get("Zone")
        self._NodeState = params.get("NodeState")
        self._ImageId = params.get("ImageId")
        self._QueueName = params.get("QueueName")
        self._NodeRole = params.get("NodeRole")
        self._NodeType = params.get("NodeType")
        self._NodeId = params.get("NodeId")
        self._NodeAllocateState = params.get("NodeAllocateState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeScript(AbstractModel):
    """描述节点执行脚本信息。

    """

    def __init__(self):
        r"""
        :param _ScriptPath: 节点执行脚本获取地址。
目前仅支持cos地址。地址最大长度：255。
        :type ScriptPath: str
        :param _Timeout: 脚本执行超时时间（包含拉取脚本的时间）。单位秒，默认值：30。取值范围：10～1200。
        :type Timeout: int
        """
        self._ScriptPath = None
        self._Timeout = None

    @property
    def ScriptPath(self):
        """节点执行脚本获取地址。
目前仅支持cos地址。地址最大长度：255。
        :rtype: str
        """
        return self._ScriptPath

    @ScriptPath.setter
    def ScriptPath(self, ScriptPath):
        self._ScriptPath = ScriptPath

    @property
    def Timeout(self):
        """脚本执行超时时间（包含拉取脚本的时间）。单位秒，默认值：30。取值范围：10～1200。
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout


    def _deserialize(self, params):
        self._ScriptPath = params.get("ScriptPath")
        self._Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Placement(AbstractModel):
    """描述了实例的抽象位置

    """

    def __init__(self):
        r"""
        :param _Zone: 实例所属的可用区名称。该参数可以通过调用  [DescribeZones](https://cloud.tencent.com/document/product/213/15707) 的返回值中的Zone字段来获取。
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        """
        self._Zone = None

    @property
    def Zone(self):
        """实例所属的可用区名称。该参数可以通过调用  [DescribeZones](https://cloud.tencent.com/document/product/213/15707) 的返回值中的Zone字段来获取。
注意：此字段可能返回 null，表示取不到有效值。
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
        


class QueueConfig(AbstractModel):
    """扩容队列配置。

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名称。
        :type QueueName: str
        :param _MinSize: 队列中弹性节点数量最小值。默认值：0。取值范围：0～200。
        :type MinSize: int
        :param _MaxSize: 队列中弹性节点数量最大值。默认值：10。取值范围：0～200。
        :type MaxSize: int
        :param _EnableAutoExpansion: 是否开启自动扩容。
        :type EnableAutoExpansion: bool
        :param _EnableAutoShrink: 是否开启自动缩容。
        :type EnableAutoShrink: bool
        :param _ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。目前仅支持公有镜和特定自定义镜像。
        :type ImageId: str
        :param _SystemDisk: 节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.thpc.v20230321.models.SystemDisk`
        :param _DataDisks: 节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20230321.models.InternetAccessible`
        :param _ExpansionNodeConfigs: 扩容节点配置信息。
        :type ExpansionNodeConfigs: list of ExpansionNodeConfig
        :param _DesiredIdleNodeCapacity: 队列中期望的空闲节点数量（包含弹性节点和静态节点）。默认值：0。队列中，处于空闲状态的节点小于此值，集群会扩容弹性节点；处于空闲状态的节点大于此值，集群会缩容弹性节点。
        :type DesiredIdleNodeCapacity: int
        :param _DesiredNodeCount: 队列中期望的总节点数。
        :type DesiredNodeCount: int
        :param _ScaleOutRatio: 扩容比例。默认值：100。取值范围：1～100。
如果扩容比例为50，那么每轮只会扩容当前作业负载所需的50%数量的节点。
        :type ScaleOutRatio: int
        :param _ScaleOutNodeThreshold: 比例扩容阈值。默认值：0。取值范围：0～200。
当作业负载需要扩容节点数量大于此值，当前扩容轮次按照ScaleOutRatio配置的比例进行扩容。当作业负载需要扩容节点数量小于此值，当前扩容轮次扩容当前作业负载所需数量的节点。
此参数配合ScaleOutRatio参数进行使用，用于比例扩容场景下，在作业负载所需节点数量较小时，加快收敛速度。
        :type ScaleOutNodeThreshold: int
        :param _MaxNodesPerCycle: 每轮扩容最大节点个数。默认值：100。取值范围：1～100。
        :type MaxNodesPerCycle: int
        :param _ScaleUpMemRatio: 扩容过程中，作业的内存在匹配实例机型时增大比例（不会影响作业提交的内存大小，只影响匹配计算过程）。<br/>
针对场景：由于实例机型的总内存会大于实例内部的可用内存，16GB内存规格的实例，实例操作系统内的可用内存只有约14.9GB内存。假设此时提交一个需要15GB内存的作业，

- 当ScaleUpMemRatio=0时，会匹配到16GB内存规格的实例,但是由于操作系统内的可用内存为14.9GB小于作业所需的15GB，扩容出来的实例作业无法运行起来。
- 当ScaleUpMemRatio=10时，匹配实例规格会按照15*(1+10%)=16.5GB来进行实例规格匹配，则不会匹配到16GB的实例，而是更大内存规格的实例来保证作业能够被运行起来。
        :type ScaleUpMemRatio: int
        :param _EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、腾讯云可观测平台等服务。若不指定该参数，则默认开启腾讯云可观测平台、云安全服务、自动化助手服务。
        :type EnhancedService: :class:`tencentcloud.thpc.v20230321.models.EnhancedService`
        """
        self._QueueName = None
        self._MinSize = None
        self._MaxSize = None
        self._EnableAutoExpansion = None
        self._EnableAutoShrink = None
        self._ImageId = None
        self._SystemDisk = None
        self._DataDisks = None
        self._InternetAccessible = None
        self._ExpansionNodeConfigs = None
        self._DesiredIdleNodeCapacity = None
        self._DesiredNodeCount = None
        self._ScaleOutRatio = None
        self._ScaleOutNodeThreshold = None
        self._MaxNodesPerCycle = None
        self._ScaleUpMemRatio = None
        self._EnhancedService = None

    @property
    def QueueName(self):
        """队列名称。
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def MinSize(self):
        """队列中弹性节点数量最小值。默认值：0。取值范围：0～200。
        :rtype: int
        """
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        """队列中弹性节点数量最大值。默认值：10。取值范围：0～200。
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def EnableAutoExpansion(self):
        """是否开启自动扩容。
        :rtype: bool
        """
        return self._EnableAutoExpansion

    @EnableAutoExpansion.setter
    def EnableAutoExpansion(self, EnableAutoExpansion):
        self._EnableAutoExpansion = EnableAutoExpansion

    @property
    def EnableAutoShrink(self):
        """是否开启自动缩容。
        :rtype: bool
        """
        return self._EnableAutoShrink

    @EnableAutoShrink.setter
    def EnableAutoShrink(self, EnableAutoShrink):
        self._EnableAutoShrink = EnableAutoShrink

    @property
    def ImageId(self):
        """指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。目前仅支持公有镜和特定自定义镜像。
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def SystemDisk(self):
        """节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def InternetAccessible(self):
        """公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def ExpansionNodeConfigs(self):
        """扩容节点配置信息。
        :rtype: list of ExpansionNodeConfig
        """
        return self._ExpansionNodeConfigs

    @ExpansionNodeConfigs.setter
    def ExpansionNodeConfigs(self, ExpansionNodeConfigs):
        self._ExpansionNodeConfigs = ExpansionNodeConfigs

    @property
    def DesiredIdleNodeCapacity(self):
        """队列中期望的空闲节点数量（包含弹性节点和静态节点）。默认值：0。队列中，处于空闲状态的节点小于此值，集群会扩容弹性节点；处于空闲状态的节点大于此值，集群会缩容弹性节点。
        :rtype: int
        """
        return self._DesiredIdleNodeCapacity

    @DesiredIdleNodeCapacity.setter
    def DesiredIdleNodeCapacity(self, DesiredIdleNodeCapacity):
        self._DesiredIdleNodeCapacity = DesiredIdleNodeCapacity

    @property
    def DesiredNodeCount(self):
        """队列中期望的总节点数。
        :rtype: int
        """
        return self._DesiredNodeCount

    @DesiredNodeCount.setter
    def DesiredNodeCount(self, DesiredNodeCount):
        self._DesiredNodeCount = DesiredNodeCount

    @property
    def ScaleOutRatio(self):
        """扩容比例。默认值：100。取值范围：1～100。
如果扩容比例为50，那么每轮只会扩容当前作业负载所需的50%数量的节点。
        :rtype: int
        """
        return self._ScaleOutRatio

    @ScaleOutRatio.setter
    def ScaleOutRatio(self, ScaleOutRatio):
        self._ScaleOutRatio = ScaleOutRatio

    @property
    def ScaleOutNodeThreshold(self):
        """比例扩容阈值。默认值：0。取值范围：0～200。
当作业负载需要扩容节点数量大于此值，当前扩容轮次按照ScaleOutRatio配置的比例进行扩容。当作业负载需要扩容节点数量小于此值，当前扩容轮次扩容当前作业负载所需数量的节点。
此参数配合ScaleOutRatio参数进行使用，用于比例扩容场景下，在作业负载所需节点数量较小时，加快收敛速度。
        :rtype: int
        """
        return self._ScaleOutNodeThreshold

    @ScaleOutNodeThreshold.setter
    def ScaleOutNodeThreshold(self, ScaleOutNodeThreshold):
        self._ScaleOutNodeThreshold = ScaleOutNodeThreshold

    @property
    def MaxNodesPerCycle(self):
        """每轮扩容最大节点个数。默认值：100。取值范围：1～100。
        :rtype: int
        """
        return self._MaxNodesPerCycle

    @MaxNodesPerCycle.setter
    def MaxNodesPerCycle(self, MaxNodesPerCycle):
        self._MaxNodesPerCycle = MaxNodesPerCycle

    @property
    def ScaleUpMemRatio(self):
        """扩容过程中，作业的内存在匹配实例机型时增大比例（不会影响作业提交的内存大小，只影响匹配计算过程）。<br/>
针对场景：由于实例机型的总内存会大于实例内部的可用内存，16GB内存规格的实例，实例操作系统内的可用内存只有约14.9GB内存。假设此时提交一个需要15GB内存的作业，

- 当ScaleUpMemRatio=0时，会匹配到16GB内存规格的实例,但是由于操作系统内的可用内存为14.9GB小于作业所需的15GB，扩容出来的实例作业无法运行起来。
- 当ScaleUpMemRatio=10时，匹配实例规格会按照15*(1+10%)=16.5GB来进行实例规格匹配，则不会匹配到16GB的实例，而是更大内存规格的实例来保证作业能够被运行起来。
        :rtype: int
        """
        return self._ScaleUpMemRatio

    @ScaleUpMemRatio.setter
    def ScaleUpMemRatio(self, ScaleUpMemRatio):
        self._ScaleUpMemRatio = ScaleUpMemRatio

    @property
    def EnhancedService(self):
        """增强服务。通过该参数可以指定是否开启云安全、腾讯云可观测平台等服务。若不指定该参数，则默认开启腾讯云可观测平台、云安全服务、自动化助手服务。
        :rtype: :class:`tencentcloud.thpc.v20230321.models.EnhancedService`
        """
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        self._EnableAutoExpansion = params.get("EnableAutoExpansion")
        self._EnableAutoShrink = params.get("EnableAutoShrink")
        self._ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("ExpansionNodeConfigs") is not None:
            self._ExpansionNodeConfigs = []
            for item in params.get("ExpansionNodeConfigs"):
                obj = ExpansionNodeConfig()
                obj._deserialize(item)
                self._ExpansionNodeConfigs.append(obj)
        self._DesiredIdleNodeCapacity = params.get("DesiredIdleNodeCapacity")
        self._DesiredNodeCount = params.get("DesiredNodeCount")
        self._ScaleOutRatio = params.get("ScaleOutRatio")
        self._ScaleOutNodeThreshold = params.get("ScaleOutNodeThreshold")
        self._MaxNodesPerCycle = params.get("MaxNodesPerCycle")
        self._ScaleUpMemRatio = params.get("ScaleUpMemRatio")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueueConfigOverview(AbstractModel):
    """扩容队列配置概览。

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名称。
        :type QueueName: str
        :param _MinSize: 队列中弹性节点数量最小值。取值范围0～200。
        :type MinSize: int
        :param _MaxSize: 队列中弹性节点数量最大值。取值范围0～200。
        :type MaxSize: int
        :param _EnableAutoExpansion: 是否开启自动扩容。
        :type EnableAutoExpansion: bool
        :param _EnableAutoShrink: 是否开启自动缩容。
        :type EnableAutoShrink: bool
        :param _ExpansionNodeConfigs: 扩容节点配置信息。
        :type ExpansionNodeConfigs: list of ExpansionNodeConfigOverview
        :param _DesiredIdleNodeCapacity: 队列中期望的空闲节点数量（包含弹性节点和静态节点）。默认值：0。队列中，处于空闲状态的节点小于此值，集群会扩容弹性节点；处于空闲状态的节点大于此值，集群会缩容弹性节点。
        :type DesiredIdleNodeCapacity: int
        :param _DesiredNodeCount: 队列中期望的总节点数。
        :type DesiredNodeCount: int
        :param _ScaleOutRatio: 扩容比例。默认值：100。取值范围：1～100。
如果扩容比例为50，那么每轮只会扩容当前作业负载所需的50%数量的节点。
        :type ScaleOutRatio: int
        :param _ScaleOutNodeThreshold: 比例扩容阈值。默认值：0。取值范围：0～200。
当作业负载需要扩容节点数量大于此值，当前扩容轮次按照ScaleOutRatio配置的的比例进行扩容。当作业负载需要扩容节点数量小于此值，当前扩容轮次扩容当前作业负载所需数量的节点。
此参数配合ScaleOutRatio参数进行使用，用于比例扩容场景下，在作业负载所需节点数量较小时，加快收敛速度。
        :type ScaleOutNodeThreshold: int
        :param _MaxNodesPerCycle: 每轮扩容最大节点个数。
        :type MaxNodesPerCycle: int
        :param _ScaleUpMemRatio: 扩容过程中，作业的内存在匹配实例机型时增大比例（不会影响作业提交的内存大小，只影响匹配计算过程）。<br/>
针对场景：由于实例机型的总内存会大于实例内部的可用内存，16GB内存规格的实例，实例操作系统内的可用内存只有约14.9GB内存。假设此时提交一个需要15GB内存的作业，

- 当ScaleUpMemRatio=0时，会匹配到16GB内存规格的实例,但是由于操作系统内的可用内存为14.9GB小于作业所需的15GB，扩容出来的实例作业无法运行起来。
- 当ScaleUpMemRatio=10时，匹配实例规格会按照15*(1+10%)=16.5GB来进行实例规格匹配，则不会匹配到16GB的实例，而是更大内存规格的实例来保证作业能够被运行起来。
        :type ScaleUpMemRatio: int
        """
        self._QueueName = None
        self._MinSize = None
        self._MaxSize = None
        self._EnableAutoExpansion = None
        self._EnableAutoShrink = None
        self._ExpansionNodeConfigs = None
        self._DesiredIdleNodeCapacity = None
        self._DesiredNodeCount = None
        self._ScaleOutRatio = None
        self._ScaleOutNodeThreshold = None
        self._MaxNodesPerCycle = None
        self._ScaleUpMemRatio = None

    @property
    def QueueName(self):
        """队列名称。
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def MinSize(self):
        """队列中弹性节点数量最小值。取值范围0～200。
        :rtype: int
        """
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        """队列中弹性节点数量最大值。取值范围0～200。
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def EnableAutoExpansion(self):
        """是否开启自动扩容。
        :rtype: bool
        """
        return self._EnableAutoExpansion

    @EnableAutoExpansion.setter
    def EnableAutoExpansion(self, EnableAutoExpansion):
        self._EnableAutoExpansion = EnableAutoExpansion

    @property
    def EnableAutoShrink(self):
        """是否开启自动缩容。
        :rtype: bool
        """
        return self._EnableAutoShrink

    @EnableAutoShrink.setter
    def EnableAutoShrink(self, EnableAutoShrink):
        self._EnableAutoShrink = EnableAutoShrink

    @property
    def ExpansionNodeConfigs(self):
        """扩容节点配置信息。
        :rtype: list of ExpansionNodeConfigOverview
        """
        return self._ExpansionNodeConfigs

    @ExpansionNodeConfigs.setter
    def ExpansionNodeConfigs(self, ExpansionNodeConfigs):
        self._ExpansionNodeConfigs = ExpansionNodeConfigs

    @property
    def DesiredIdleNodeCapacity(self):
        """队列中期望的空闲节点数量（包含弹性节点和静态节点）。默认值：0。队列中，处于空闲状态的节点小于此值，集群会扩容弹性节点；处于空闲状态的节点大于此值，集群会缩容弹性节点。
        :rtype: int
        """
        return self._DesiredIdleNodeCapacity

    @DesiredIdleNodeCapacity.setter
    def DesiredIdleNodeCapacity(self, DesiredIdleNodeCapacity):
        self._DesiredIdleNodeCapacity = DesiredIdleNodeCapacity

    @property
    def DesiredNodeCount(self):
        """队列中期望的总节点数。
        :rtype: int
        """
        return self._DesiredNodeCount

    @DesiredNodeCount.setter
    def DesiredNodeCount(self, DesiredNodeCount):
        self._DesiredNodeCount = DesiredNodeCount

    @property
    def ScaleOutRatio(self):
        """扩容比例。默认值：100。取值范围：1～100。
如果扩容比例为50，那么每轮只会扩容当前作业负载所需的50%数量的节点。
        :rtype: int
        """
        return self._ScaleOutRatio

    @ScaleOutRatio.setter
    def ScaleOutRatio(self, ScaleOutRatio):
        self._ScaleOutRatio = ScaleOutRatio

    @property
    def ScaleOutNodeThreshold(self):
        """比例扩容阈值。默认值：0。取值范围：0～200。
当作业负载需要扩容节点数量大于此值，当前扩容轮次按照ScaleOutRatio配置的的比例进行扩容。当作业负载需要扩容节点数量小于此值，当前扩容轮次扩容当前作业负载所需数量的节点。
此参数配合ScaleOutRatio参数进行使用，用于比例扩容场景下，在作业负载所需节点数量较小时，加快收敛速度。
        :rtype: int
        """
        return self._ScaleOutNodeThreshold

    @ScaleOutNodeThreshold.setter
    def ScaleOutNodeThreshold(self, ScaleOutNodeThreshold):
        self._ScaleOutNodeThreshold = ScaleOutNodeThreshold

    @property
    def MaxNodesPerCycle(self):
        """每轮扩容最大节点个数。
        :rtype: int
        """
        return self._MaxNodesPerCycle

    @MaxNodesPerCycle.setter
    def MaxNodesPerCycle(self, MaxNodesPerCycle):
        self._MaxNodesPerCycle = MaxNodesPerCycle

    @property
    def ScaleUpMemRatio(self):
        """扩容过程中，作业的内存在匹配实例机型时增大比例（不会影响作业提交的内存大小，只影响匹配计算过程）。<br/>
针对场景：由于实例机型的总内存会大于实例内部的可用内存，16GB内存规格的实例，实例操作系统内的可用内存只有约14.9GB内存。假设此时提交一个需要15GB内存的作业，

- 当ScaleUpMemRatio=0时，会匹配到16GB内存规格的实例,但是由于操作系统内的可用内存为14.9GB小于作业所需的15GB，扩容出来的实例作业无法运行起来。
- 当ScaleUpMemRatio=10时，匹配实例规格会按照15*(1+10%)=16.5GB来进行实例规格匹配，则不会匹配到16GB的实例，而是更大内存规格的实例来保证作业能够被运行起来。
        :rtype: int
        """
        return self._ScaleUpMemRatio

    @ScaleUpMemRatio.setter
    def ScaleUpMemRatio(self, ScaleUpMemRatio):
        self._ScaleUpMemRatio = ScaleUpMemRatio


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        self._EnableAutoExpansion = params.get("EnableAutoExpansion")
        self._EnableAutoShrink = params.get("EnableAutoShrink")
        if params.get("ExpansionNodeConfigs") is not None:
            self._ExpansionNodeConfigs = []
            for item in params.get("ExpansionNodeConfigs"):
                obj = ExpansionNodeConfigOverview()
                obj._deserialize(item)
                self._ExpansionNodeConfigs.append(obj)
        self._DesiredIdleNodeCapacity = params.get("DesiredIdleNodeCapacity")
        self._DesiredNodeCount = params.get("DesiredNodeCount")
        self._ScaleOutRatio = params.get("ScaleOutRatio")
        self._ScaleOutNodeThreshold = params.get("ScaleOutNodeThreshold")
        self._MaxNodesPerCycle = params.get("MaxNodesPerCycle")
        self._ScaleUpMemRatio = params.get("ScaleUpMemRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueueOverview(AbstractModel):
    """队列信息概览。

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名称。
        :type QueueName: str
        """
        self._QueueName = None

    @property
    def QueueName(self):
        """队列名称。
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunAutomationServiceEnabled(AbstractModel):
    """描述了 “云自动化助手” 服务相关的信息。

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启云自动化助手。取值范围：<br><li>TRUE：表示开启云自动化助手服务</li><br><li>FALSE：表示不开启云自动化助手服务</li><br><br>默认取值：TRUE。
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        """是否开启云自动化助手。取值范围：<br><li>TRUE：表示开启云自动化助手服务</li><br><li>FALSE：表示不开启云自动化助手服务</li><br><br>默认取值：TRUE。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunMonitorServiceEnabled(AbstractModel):
    """描述了 “腾讯云可观测平台” 服务相关的信息。

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启[腾讯云可观测平台](/document/product/248)服务。取值范围：<br><li>TRUE：表示开启腾讯云可观测平台服务</li><br><li>FALSE：表示不开启腾讯云可观测平台服务</li><br><br>默认取值：TRUE。
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        """是否开启[腾讯云可观测平台](/document/product/248)服务。取值范围：<br><li>TRUE：表示开启腾讯云可观测平台服务</li><br><li>FALSE：表示不开启腾讯云可观测平台服务</li><br><br>默认取值：TRUE。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSecurityServiceEnabled(AbstractModel):
    """描述了 “云安全” 服务相关的信息。

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启[云安全](/document/product/296)服务。取值范围：<br><li>TRUE：表示开启云安全服务</li><br><li>FALSE：表示不开启云安全服务</li><br><br>默认取值：TRUE。
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        """是否开启[云安全](/document/product/296)服务。取值范围：<br><li>TRUE：表示开启云安全服务</li><br><li>FALSE：表示不开启云安全服务</li><br><br>默认取值：TRUE。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAutoScalingConfigurationRequest(AbstractModel):
    """SetAutoScalingConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _ExpansionBusyTime: 任务连续等待时间，队列的任务处于连续等待的时间。单位秒。默认值120。
        :type ExpansionBusyTime: int
        :param _ShrinkIdleTime: 节点连续空闲（未运行作业）时间，一个节点连续处于空闲状态时间。单位秒。默认值300。
        :type ShrinkIdleTime: int
        :param _QueueConfigs: 扩容队列配置列表。
        :type QueueConfigs: list of QueueConfig
        :param _DryRun: 是否只预检此次请求。
true：发送检查请求，不会绑定弹性伸缩组。检查项包括是否填写了必需参数，请求格式，业务限制。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId。
false（默认）：发送正常请求，通过检查后直接绑定弹性伸缩组。
        :type DryRun: bool
        """
        self._ClusterId = None
        self._ExpansionBusyTime = None
        self._ShrinkIdleTime = None
        self._QueueConfigs = None
        self._DryRun = None

    @property
    def ClusterId(self):
        """集群ID。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ExpansionBusyTime(self):
        """任务连续等待时间，队列的任务处于连续等待的时间。单位秒。默认值120。
        :rtype: int
        """
        return self._ExpansionBusyTime

    @ExpansionBusyTime.setter
    def ExpansionBusyTime(self, ExpansionBusyTime):
        self._ExpansionBusyTime = ExpansionBusyTime

    @property
    def ShrinkIdleTime(self):
        """节点连续空闲（未运行作业）时间，一个节点连续处于空闲状态时间。单位秒。默认值300。
        :rtype: int
        """
        return self._ShrinkIdleTime

    @ShrinkIdleTime.setter
    def ShrinkIdleTime(self, ShrinkIdleTime):
        self._ShrinkIdleTime = ShrinkIdleTime

    @property
    def QueueConfigs(self):
        """扩容队列配置列表。
        :rtype: list of QueueConfig
        """
        return self._QueueConfigs

    @QueueConfigs.setter
    def QueueConfigs(self, QueueConfigs):
        self._QueueConfigs = QueueConfigs

    @property
    def DryRun(self):
        """是否只预检此次请求。
true：发送检查请求，不会绑定弹性伸缩组。检查项包括是否填写了必需参数，请求格式，业务限制。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId。
false（默认）：发送正常请求，通过检查后直接绑定弹性伸缩组。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ExpansionBusyTime = params.get("ExpansionBusyTime")
        self._ShrinkIdleTime = params.get("ShrinkIdleTime")
        if params.get("QueueConfigs") is not None:
            self._QueueConfigs = []
            for item in params.get("QueueConfigs"):
                obj = QueueConfig()
                obj._deserialize(item)
                self._QueueConfigs.append(obj)
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAutoScalingConfigurationResponse(AbstractModel):
    """SetAutoScalingConfiguration返回参数结构体

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


class SpaceChargePrepaid(AbstractModel):
    """描述了工作空间的计费模式

    """

    def __init__(self):
        r"""
        :param _Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 12, 24, 36。默认取值为1。
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: int
        :param _RenewFlag: 自动续费标识。取值范围：

NOTIFY_AND_AUTO_RENEW：通知过期且自动续费

NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费

DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费


默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        """购买实例的时长，单位：月。取值范围：1, 2, 3, 12, 24, 36。默认取值为1。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        """自动续费标识。取值范围：

NOTIFY_AND_AUTO_RENEW：通知过期且自动续费

NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费

DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费


默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpaceDataDisk(AbstractModel):
    """工作空间数据盘配置

    """

    def __init__(self):
        r"""
        :param _DiskType: 数据盘类型。数据盘类型限制详见[存储概述](https://cloud.tencent.com/document/product/213/4952)。取值范围：<br />
<li>
  LOCAL_BASIC：本地硬盘<br />
  <li>
    LOCAL_SSD：本地SSD硬盘<br />
    <li>
      LOCAL_NVME：本地NVME硬盘，与InstanceType强相关，不支持指定<br />
      <li>
        LOCAL_PRO：本地HDD硬盘，与InstanceType强相关，不支持指定<br />
        <li>
          CLOUD_BASIC：普通云硬盘<br />
          <li>
            CLOUD_PREMIUM：高性能云硬盘<br />
            <li>
              CLOUD_SSD：SSD云硬盘<br />
              <li>
                CLOUD_HSSD：增强型SSD云硬盘<br />
                <li>
                  CLOUD_TSSD：极速型SSD云硬盘<br />
                  <li>
                    CLOUD_BSSD：通用型SSD云硬盘<br /><br />默认取值：LOCAL_BASIC。<br /><br />该参数对`ResizeInstanceDisk`接口无效。
                  </li>
                </li>
              </li>
            </li>
          </li>
        </li>
      </li>
    </li>
  </li>
</li>
        :type DiskType: str
        :param _DiskId: 数据盘
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskId: str
        :param _DiskSize: 数据盘大小，单位：GB。最小调整步长为10G，不同数据盘类型取值范围不同，具体限制详见：[存储概述](https://cloud.tencent.com/document/product/213/4952)。默认值为0，表示不购买数据盘。更多限制详见产品文档。
        :type DiskSize: int
        :param _DeleteWithInstance: 数据盘是否随子机销毁。取值范围：
<li>TRUE：子机销毁时，销毁数据盘，只支持按小时后付费云盘</li>
<li>
  FALSE：子机销毁时，保留数据盘<br />
  默认取值：TRUE<br />
  该参数目前仅用于 `RunInstances` 接口。
</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteWithInstance: bool
        :param _SnapshotId: 数据盘快照ID。选择的数据盘快照大小需小于数据盘大小。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotId: str
        :param _Encrypt: 数据盘是加密。取值范围：
<li>true：加密</li>
<li>
  false：不加密<br />
  默认取值：false<br />
  该参数目前仅用于 `RunInstances` 接口。
</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Encrypt: bool
        :param _KmsKeyId: 自定义CMK对应的ID，取值为UUID或者类似kms-abcd1234。用于加密云盘。

该参数目前仅用于 `CreateWorkspaces` 接口。
注意：此字段可能返回 null，表示取不到有效值。
        :type KmsKeyId: str
        :param _ThroughputPerformance: 云硬盘性能，单位：MB/s
注意：此字段可能返回 null，表示取不到有效值。
        :type ThroughputPerformance: int
        :param _BurstPerformance: 突发性能

注：内测中。
注意：此字段可能返回 null，表示取不到有效值。
        :type BurstPerformance: bool
        """
        self._DiskType = None
        self._DiskId = None
        self._DiskSize = None
        self._DeleteWithInstance = None
        self._SnapshotId = None
        self._Encrypt = None
        self._KmsKeyId = None
        self._ThroughputPerformance = None
        self._BurstPerformance = None

    @property
    def DiskType(self):
        """数据盘类型。数据盘类型限制详见[存储概述](https://cloud.tencent.com/document/product/213/4952)。取值范围：<br />
<li>
  LOCAL_BASIC：本地硬盘<br />
  <li>
    LOCAL_SSD：本地SSD硬盘<br />
    <li>
      LOCAL_NVME：本地NVME硬盘，与InstanceType强相关，不支持指定<br />
      <li>
        LOCAL_PRO：本地HDD硬盘，与InstanceType强相关，不支持指定<br />
        <li>
          CLOUD_BASIC：普通云硬盘<br />
          <li>
            CLOUD_PREMIUM：高性能云硬盘<br />
            <li>
              CLOUD_SSD：SSD云硬盘<br />
              <li>
                CLOUD_HSSD：增强型SSD云硬盘<br />
                <li>
                  CLOUD_TSSD：极速型SSD云硬盘<br />
                  <li>
                    CLOUD_BSSD：通用型SSD云硬盘<br /><br />默认取值：LOCAL_BASIC。<br /><br />该参数对`ResizeInstanceDisk`接口无效。
                  </li>
                </li>
              </li>
            </li>
          </li>
        </li>
      </li>
    </li>
  </li>
</li>
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskId(self):
        """数据盘
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskSize(self):
        """数据盘大小，单位：GB。最小调整步长为10G，不同数据盘类型取值范围不同，具体限制详见：[存储概述](https://cloud.tencent.com/document/product/213/4952)。默认值为0，表示不购买数据盘。更多限制详见产品文档。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DeleteWithInstance(self):
        """数据盘是否随子机销毁。取值范围：
<li>TRUE：子机销毁时，销毁数据盘，只支持按小时后付费云盘</li>
<li>
  FALSE：子机销毁时，保留数据盘<br />
  默认取值：TRUE<br />
  该参数目前仅用于 `RunInstances` 接口。
</li>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def SnapshotId(self):
        """数据盘快照ID。选择的数据盘快照大小需小于数据盘大小。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def Encrypt(self):
        """数据盘是加密。取值范围：
<li>true：加密</li>
<li>
  false：不加密<br />
  默认取值：false<br />
  该参数目前仅用于 `RunInstances` 接口。
</li>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def KmsKeyId(self):
        """自定义CMK对应的ID，取值为UUID或者类似kms-abcd1234。用于加密云盘。

该参数目前仅用于 `CreateWorkspaces` 接口。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def ThroughputPerformance(self):
        """云硬盘性能，单位：MB/s
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def BurstPerformance(self):
        """突发性能

注：内测中。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._BurstPerformance

    @BurstPerformance.setter
    def BurstPerformance(self, BurstPerformance):
        self._BurstPerformance = BurstPerformance


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskId = params.get("DiskId")
        self._DiskSize = params.get("DiskSize")
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._SnapshotId = params.get("SnapshotId")
        self._Encrypt = params.get("Encrypt")
        self._KmsKeyId = params.get("KmsKeyId")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        self._BurstPerformance = params.get("BurstPerformance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpaceInfo(AbstractModel):
    """描述工作空间的信息

    """

    def __init__(self):
        r"""
        :param _SpaceId: 工作空间ID
        :type SpaceId: str
        :param _SpaceFamily: 工作空间类型
        :type SpaceFamily: str
        :param _SpaceType: 工作空间规格
        :type SpaceType: str
        :param _SpaceName: 工作空间名称
        :type SpaceName: str
        :param _SpaceState: 工作空间状态。取值范围：<br><li>PENDING：表示创建中<br></li><li>LAUNCH_FAILED：表示创建失败<br></li><li>ONLINE：表示运行中<br></li><li>ARREARS：表示隔离中<br></li><li>TERMINATING：表示销毁中。<br></li>
        :type SpaceState: str
        :param _SpaceChargeType: 工作空间计费模式
        :type SpaceChargeType: str
        :param _ResourceId: 工作空间对应资源ID
        :type ResourceId: str
        :param _RenewFlag: 自动续费标识
        :type RenewFlag: str
        :param _Tags: 工作空间关联的工作列表
        :type Tags: list of Tag
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _ExpiredTime: 到期时间
        :type ExpiredTime: str
        :param _Placement: 工作空间所在位置
        :type Placement: :class:`tencentcloud.thpc.v20230321.models.Placement`
        :param _LatestOperation: 工作空间的最新操作
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperation: str
        :param _LatestOperationState: 工作空间的最新操作状态
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperationState: str
        """
        self._SpaceId = None
        self._SpaceFamily = None
        self._SpaceType = None
        self._SpaceName = None
        self._SpaceState = None
        self._SpaceChargeType = None
        self._ResourceId = None
        self._RenewFlag = None
        self._Tags = None
        self._CreatedTime = None
        self._ExpiredTime = None
        self._Placement = None
        self._LatestOperation = None
        self._LatestOperationState = None

    @property
    def SpaceId(self):
        """工作空间ID
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def SpaceFamily(self):
        """工作空间类型
        :rtype: str
        """
        return self._SpaceFamily

    @SpaceFamily.setter
    def SpaceFamily(self, SpaceFamily):
        self._SpaceFamily = SpaceFamily

    @property
    def SpaceType(self):
        """工作空间规格
        :rtype: str
        """
        return self._SpaceType

    @SpaceType.setter
    def SpaceType(self, SpaceType):
        self._SpaceType = SpaceType

    @property
    def SpaceName(self):
        """工作空间名称
        :rtype: str
        """
        return self._SpaceName

    @SpaceName.setter
    def SpaceName(self, SpaceName):
        self._SpaceName = SpaceName

    @property
    def SpaceState(self):
        """工作空间状态。取值范围：<br><li>PENDING：表示创建中<br></li><li>LAUNCH_FAILED：表示创建失败<br></li><li>ONLINE：表示运行中<br></li><li>ARREARS：表示隔离中<br></li><li>TERMINATING：表示销毁中。<br></li>
        :rtype: str
        """
        return self._SpaceState

    @SpaceState.setter
    def SpaceState(self, SpaceState):
        self._SpaceState = SpaceState

    @property
    def SpaceChargeType(self):
        """工作空间计费模式
        :rtype: str
        """
        return self._SpaceChargeType

    @SpaceChargeType.setter
    def SpaceChargeType(self, SpaceChargeType):
        self._SpaceChargeType = SpaceChargeType

    @property
    def ResourceId(self):
        """工作空间对应资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def RenewFlag(self):
        """自动续费标识
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Tags(self):
        """工作空间关联的工作列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CreatedTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ExpiredTime(self):
        """到期时间
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def Placement(self):
        """工作空间所在位置
        :rtype: :class:`tencentcloud.thpc.v20230321.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def LatestOperation(self):
        """工作空间的最新操作
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LatestOperation

    @LatestOperation.setter
    def LatestOperation(self, LatestOperation):
        self._LatestOperation = LatestOperation

    @property
    def LatestOperationState(self):
        """工作空间的最新操作状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LatestOperationState

    @LatestOperationState.setter
    def LatestOperationState(self, LatestOperationState):
        self._LatestOperationState = LatestOperationState


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._SpaceFamily = params.get("SpaceFamily")
        self._SpaceType = params.get("SpaceType")
        self._SpaceName = params.get("SpaceName")
        self._SpaceState = params.get("SpaceState")
        self._SpaceChargeType = params.get("SpaceChargeType")
        self._ResourceId = params.get("ResourceId")
        self._RenewFlag = params.get("RenewFlag")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._CreatedTime = params.get("CreatedTime")
        self._ExpiredTime = params.get("ExpiredTime")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._LatestOperation = params.get("LatestOperation")
        self._LatestOperationState = params.get("LatestOperationState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpaceInternetAccessible(AbstractModel):
    """描述了工作空间的公网可访问性，声明了工作空间的公网使用计费模式，最大带宽等

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: 网络计费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: 公网出带宽上限，默认为0
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetMaxBandwidthOut: int
        :param _PublicIpAssigned: 是否分配公网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAssigned: bool
        :param _BandwidthPackageId: 带宽包ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthPackageId: str
        """
        self._InternetChargeType = None
        self._InternetMaxBandwidthOut = None
        self._PublicIpAssigned = None
        self._BandwidthPackageId = None

    @property
    def InternetChargeType(self):
        """网络计费类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        """公网出带宽上限，默认为0
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def PublicIpAssigned(self):
        """是否分配公网IP
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._PublicIpAssigned

    @PublicIpAssigned.setter
    def PublicIpAssigned(self, PublicIpAssigned):
        self._PublicIpAssigned = PublicIpAssigned

    @property
    def BandwidthPackageId(self):
        """带宽包ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId


    def _deserialize(self, params):
        self._InternetChargeType = params.get("InternetChargeType")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._PublicIpAssigned = params.get("PublicIpAssigned")
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpacePlacement(AbstractModel):
    """描述了实例的抽象位置，包括其所在的可用区，所属的项目

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _ProjectId: 项目，默认是0
        :type ProjectId: int
        """
        self._Zone = None
        self._ProjectId = None

    @property
    def Zone(self):
        """可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ProjectId(self):
        """项目，默认是0
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpaceSystemDisk(AbstractModel):
    """工作空间系统盘配置

    """

    def __init__(self):
        r"""
        :param _DiskType: 系统盘类型。系统盘类型限制详见[存储概述](https://cloud.tencent.com/document/product/213/4952)。取值范围：<ul><li>LOCAL_BASIC：本地硬盘</li><li>LOCAL_SSD：本地SSD硬盘</li><li>CLOUD_BASIC：普通云硬盘</li><li>CLOUD_SSD：SSD云硬盘</li><li>CLOUD_PREMIUM：高性能云硬盘</li><li>CLOUD_BSSD：通用性SSD云硬盘</li><li>CLOUD_HSSD：增强型SSD云硬盘</li><li>CLOUD_TSSD：极速型SSD云硬盘</li></ul>默认取值：当前有库存的硬盘类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _DiskSize: 系统盘大小，单位：GB。默认值为 50
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        """
        self._DiskType = None
        self._DiskSize = None

    @property
    def DiskType(self):
        """系统盘类型。系统盘类型限制详见[存储概述](https://cloud.tencent.com/document/product/213/4952)。取值范围：<ul><li>LOCAL_BASIC：本地硬盘</li><li>LOCAL_SSD：本地SSD硬盘</li><li>CLOUD_BASIC：普通云硬盘</li><li>CLOUD_SSD：SSD云硬盘</li><li>CLOUD_PREMIUM：高性能云硬盘</li><li>CLOUD_BSSD：通用性SSD云硬盘</li><li>CLOUD_HSSD：增强型SSD云硬盘</li><li>CLOUD_TSSD：极速型SSD云硬盘</li></ul>默认取值：当前有库存的硬盘类型。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """系统盘大小，单位：GB。默认值为 50
注意：此字段可能返回 null，表示取不到有效值。
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
        


class SpaceVirtualPrivateCloud(AbstractModel):
    """描述了工作空间VPC相关信息，包括子网，IP信息等

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 私有网络子网ID
        :type SubnetId: str
        :param _AsVpcGateway: 是否用作公网网关
        :type AsVpcGateway: bool
        :param _PrivateIpAddresses: 私有网络子网 IP 数组
        :type PrivateIpAddresses: list of str
        :param _Ipv6AddressCount: 为弹性网卡指定随机生成
        :type Ipv6AddressCount: int
        """
        self._VpcId = None
        self._SubnetId = None
        self._AsVpcGateway = None
        self._PrivateIpAddresses = None
        self._Ipv6AddressCount = None

    @property
    def VpcId(self):
        """私有网络ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """私有网络子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def AsVpcGateway(self):
        """是否用作公网网关
        :rtype: bool
        """
        return self._AsVpcGateway

    @AsVpcGateway.setter
    def AsVpcGateway(self, AsVpcGateway):
        self._AsVpcGateway = AsVpcGateway

    @property
    def PrivateIpAddresses(self):
        """私有网络子网 IP 数组
        :rtype: list of str
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def Ipv6AddressCount(self):
        """为弹性网卡指定随机生成
        :rtype: int
        """
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._AsVpcGateway = params.get("AsVpcGateway")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._Ipv6AddressCount = params.get("Ipv6AddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageOption(AbstractModel):
    """描述集群文件系统选项

    """

    def __init__(self):
        r"""
        :param _CFSOptions: 集群挂载CFS文件系统选项。
        :type CFSOptions: list of CFSOption
        :param _GooseFSOptions: 集群挂载GooseFS文件系统选项。
        :type GooseFSOptions: list of GooseFSOption
        :param _GooseFSxOptions: 集群挂载GooseFSx文件系统选项。
        :type GooseFSxOptions: list of GooseFSxOption
        """
        self._CFSOptions = None
        self._GooseFSOptions = None
        self._GooseFSxOptions = None

    @property
    def CFSOptions(self):
        """集群挂载CFS文件系统选项。
        :rtype: list of CFSOption
        """
        return self._CFSOptions

    @CFSOptions.setter
    def CFSOptions(self, CFSOptions):
        self._CFSOptions = CFSOptions

    @property
    def GooseFSOptions(self):
        """集群挂载GooseFS文件系统选项。
        :rtype: list of GooseFSOption
        """
        return self._GooseFSOptions

    @GooseFSOptions.setter
    def GooseFSOptions(self, GooseFSOptions):
        self._GooseFSOptions = GooseFSOptions

    @property
    def GooseFSxOptions(self):
        """集群挂载GooseFSx文件系统选项。
        :rtype: list of GooseFSxOption
        """
        return self._GooseFSxOptions

    @GooseFSxOptions.setter
    def GooseFSxOptions(self, GooseFSxOptions):
        self._GooseFSxOptions = GooseFSxOptions


    def _deserialize(self, params):
        if params.get("CFSOptions") is not None:
            self._CFSOptions = []
            for item in params.get("CFSOptions"):
                obj = CFSOption()
                obj._deserialize(item)
                self._CFSOptions.append(obj)
        if params.get("GooseFSOptions") is not None:
            self._GooseFSOptions = []
            for item in params.get("GooseFSOptions"):
                obj = GooseFSOption()
                obj._deserialize(item)
                self._GooseFSOptions.append(obj)
        if params.get("GooseFSxOptions") is not None:
            self._GooseFSxOptions = []
            for item in params.get("GooseFSxOptions"):
                obj = GooseFSxOption()
                obj._deserialize(item)
                self._GooseFSxOptions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageOptionOverview(AbstractModel):
    """集群存储选项概览信息。

    """

    def __init__(self):
        r"""
        :param _CFSOptions: CFS存储选项概览信息列表。
        :type CFSOptions: list of CFSOptionOverview
        :param _GooseFSOptions: GooseFS存储选项概览信息列表。
        :type GooseFSOptions: list of GooseFSOptionOverview
        :param _GooseFSxOptions: GooseFSx存储选项概览信息列表。
        :type GooseFSxOptions: list of GooseFSxOptionOverview
        """
        self._CFSOptions = None
        self._GooseFSOptions = None
        self._GooseFSxOptions = None

    @property
    def CFSOptions(self):
        """CFS存储选项概览信息列表。
        :rtype: list of CFSOptionOverview
        """
        return self._CFSOptions

    @CFSOptions.setter
    def CFSOptions(self, CFSOptions):
        self._CFSOptions = CFSOptions

    @property
    def GooseFSOptions(self):
        """GooseFS存储选项概览信息列表。
        :rtype: list of GooseFSOptionOverview
        """
        return self._GooseFSOptions

    @GooseFSOptions.setter
    def GooseFSOptions(self, GooseFSOptions):
        self._GooseFSOptions = GooseFSOptions

    @property
    def GooseFSxOptions(self):
        """GooseFSx存储选项概览信息列表。
        :rtype: list of GooseFSxOptionOverview
        """
        return self._GooseFSxOptions

    @GooseFSxOptions.setter
    def GooseFSxOptions(self, GooseFSxOptions):
        self._GooseFSxOptions = GooseFSxOptions


    def _deserialize(self, params):
        if params.get("CFSOptions") is not None:
            self._CFSOptions = []
            for item in params.get("CFSOptions"):
                obj = CFSOptionOverview()
                obj._deserialize(item)
                self._CFSOptions.append(obj)
        if params.get("GooseFSOptions") is not None:
            self._GooseFSOptions = []
            for item in params.get("GooseFSOptions"):
                obj = GooseFSOptionOverview()
                obj._deserialize(item)
                self._GooseFSOptions.append(obj)
        if params.get("GooseFSxOptions") is not None:
            self._GooseFSxOptions = []
            for item in params.get("GooseFSxOptions"):
                obj = GooseFSxOptionOverview()
                obj._deserialize(item)
                self._GooseFSxOptions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SystemDisk(AbstractModel):
    """描述了操作系统所在块设备即系统盘的信息

    """

    def __init__(self):
        r"""
        :param _DiskType: 系统盘类型。系统盘类型限制详见存储概述。取值范围：
CLOUD_BASIC：普通云硬盘
CLOUD_SSD：SSD云硬盘
CLOUD_PREMIUM：高性能云硬盘

默认取值：当前有库存的硬盘类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _DiskSize: 系统盘大小，单位：GB。默认值为 50
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        """
        self._DiskType = None
        self._DiskSize = None

    @property
    def DiskType(self):
        """系统盘类型。系统盘类型限制详见存储概述。取值范围：
CLOUD_BASIC：普通云硬盘
CLOUD_SSD：SSD云硬盘
CLOUD_PREMIUM：高性能云硬盘

默认取值：当前有库存的硬盘类型。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """系统盘大小，单位：GB。默认值为 50
注意：此字段可能返回 null，表示取不到有效值。
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
    """标签键值对。

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
        :type Key: str
        :param _Value: 标签值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """标签值
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
        


class TagSpecification(AbstractModel):
    """创建资源工作空间时同时绑定的标签对说明

    """

    def __init__(self):
        r"""
        :param _ResourceType: 标签绑定的资源类型
        :type ResourceType: str
        :param _Tags: 标签对列表
        :type Tags: list of Tag
        """
        self._ResourceType = None
        self._Tags = None

    @property
    def ResourceType(self):
        """标签绑定的资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Tags(self):
        """标签对列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
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
        


class TerminateWorkspacesRequest(AbstractModel):
    """TerminateWorkspaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceIds: 工作空间ID
        :type SpaceIds: list of str
        :param _ReleasePrepaidDataDisks: 释放空间挂载的包年包月数据盘。true表示销毁空间同时释放包年包月数据盘，false表示只销毁空间。
        :type ReleasePrepaidDataDisks: bool
        """
        self._SpaceIds = None
        self._ReleasePrepaidDataDisks = None

    @property
    def SpaceIds(self):
        """工作空间ID
        :rtype: list of str
        """
        return self._SpaceIds

    @SpaceIds.setter
    def SpaceIds(self, SpaceIds):
        self._SpaceIds = SpaceIds

    @property
    def ReleasePrepaidDataDisks(self):
        """释放空间挂载的包年包月数据盘。true表示销毁空间同时释放包年包月数据盘，false表示只销毁空间。
        :rtype: bool
        """
        return self._ReleasePrepaidDataDisks

    @ReleasePrepaidDataDisks.setter
    def ReleasePrepaidDataDisks(self, ReleasePrepaidDataDisks):
        self._ReleasePrepaidDataDisks = ReleasePrepaidDataDisks


    def _deserialize(self, params):
        self._SpaceIds = params.get("SpaceIds")
        self._ReleasePrepaidDataDisks = params.get("ReleasePrepaidDataDisks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateWorkspacesResponse(AbstractModel):
    """TerminateWorkspaces返回参数结构体

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


class VirtualPrivateCloud(AbstractModel):
    """描述了VPC相关信息

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络ID，形如`vpc-xxx`。有效的VpcId可通过登录[控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)查询；也可以调用接口 [DescribeVpcEx](/document/api/215/1372) ，从接口返回中的`unVpcId`字段获取。若在创建子机时VpcId与SubnetId同时传入`DEFAULT`，则强制使用默认vpc网络。
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 私有网络子网ID，形如`subnet-xxx`。有效的私有网络子网ID可通过登录[控制台](https://console.cloud.tencent.com/vpc/subnet?rid=1)查询；也可以调用接口  [DescribeSubnets](/document/api/215/15784) ，从接口返回中的`unSubnetId`字段获取。若在创建子机时SubnetId与VpcId同时传入`DEFAULT`，则强制使用默认vpc网络。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

    @property
    def VpcId(self):
        """私有网络ID，形如`vpc-xxx`。有效的VpcId可通过登录[控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)查询；也可以调用接口 [DescribeVpcEx](/document/api/215/1372) ，从接口返回中的`unVpcId`字段获取。若在创建子机时VpcId与SubnetId同时传入`DEFAULT`，则强制使用默认vpc网络。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """私有网络子网ID，形如`subnet-xxx`。有效的私有网络子网ID可通过登录[控制台](https://console.cloud.tencent.com/vpc/subnet?rid=1)查询；也可以调用接口  [DescribeSubnets](/document/api/215/15784) ，从接口返回中的`unSubnetId`字段获取。若在创建子机时SubnetId与VpcId同时传入`DEFAULT`，则强制使用默认vpc网络。
注意：此字段可能返回 null，表示取不到有效值。
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
        