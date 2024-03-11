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


class Annotation(AbstractModel):
    """k8s中标注，一般以数组的方式存在

    """

    def __init__(self):
        r"""
        :param _Name: map表中的Name
        :type Name: str
        :param _Value: map表中的Value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoscalingAdded(AbstractModel):
    """自动扩所容的节点

    """

    def __init__(self):
        r"""
        :param _Joining: 正在加入中的节点数量
        :type Joining: int
        :param _Initializing: 初始化中的节点数量
        :type Initializing: int
        :param _Normal: 正常的节点数量
        :type Normal: int
        :param _Total: 节点总数
        :type Total: int
        """
        self._Joining = None
        self._Initializing = None
        self._Normal = None
        self._Total = None

    @property
    def Joining(self):
        return self._Joining

    @Joining.setter
    def Joining(self, Joining):
        self._Joining = Joining

    @property
    def Initializing(self):
        return self._Initializing

    @Initializing.setter
    def Initializing(self, Initializing):
        self._Initializing = Initializing

    @property
    def Normal(self):
        return self._Normal

    @Normal.setter
    def Normal(self, Normal):
        self._Normal = Normal

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Joining = params.get("Joining")
        self._Initializing = params.get("Initializing")
        self._Normal = params.get("Normal")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterInstancesRequest(AbstractModel):
    """DescribeClusterInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Filters: 过滤条件列表:
InstanceIds(实例ID),InstanceType(实例类型：Regular，Native，Virtual，External),VagueIpAddress(模糊匹配IP),Labels(k8s节点label),NodePoolNames(节点池名称),VagueInstanceName(模糊匹配节点名),InstanceStates(节点状态),Unschedulable(是否封锁),NodePoolIds(节点池ID)
        :type Filters: list of Filter
        :param _SortBy: 排序信息
        :type SortBy: :class:`tencentcloud.tke.v20220501.models.SortBy`
        """
        self._ClusterId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._SortBy = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("SortBy") is not None:
            self._SortBy = SortBy()
            self._SortBy._deserialize(params.get("SortBy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterInstancesResponse(AbstractModel):
    """DescribeClusterInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 集群中实例总数
        :type TotalCount: int
        :param _InstanceSet: 集群中实例列表
        :type InstanceSet: list of Instance
        :param _Errors: 错误信息集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Errors: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._Errors = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def Errors(self):
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._Errors = params.get("Errors")
        self._RequestId = params.get("RequestId")


class DescribeNodePoolsRequest(AbstractModel):
    """DescribeNodePools请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群 ID
        :type ClusterId: str
        :param _Filters: 查询过滤条件：
·  NodePoolsName
    按照【节点池名】进行过滤。
    类型：String
    必选：否

·  NodePoolsId
    按照【节点池id】进行过滤。
    类型：String
    必选：否

·  tags
    按照【标签键值对】进行过滤。
    类型：String
    必选：否

·  tag:tag-key
    按照【标签键值对】进行过滤。
    类型：String
    必选：否
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 最大输出条数，默认20，最大为100
        :type Limit: int
        """
        self._ClusterId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
        


class DescribeNodePoolsResponse(AbstractModel):
    """DescribeNodePools返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NodePools: 节点池列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodePools: list of NodePool
        :param _TotalCount: 资源总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NodePools = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NodePools(self):
        return self._NodePools

    @NodePools.setter
    def NodePools(self, NodePools):
        self._NodePools = NodePools

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
        if params.get("NodePools") is not None:
            self._NodePools = []
            for item in params.get("NodePools"):
                obj = NodePool()
                obj._deserialize(item)
                self._NodePools.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ExternalNodeInfo(AbstractModel):
    """第三方节点

    """

    def __init__(self):
        r"""
        :param _Name: 第三方节点名称
        :type Name: str
        :param _CPU: CPU核数，单位：核
注意：此字段可能返回 null，表示取不到有效值。
        :type CPU: int
        :param _Memory: 节点内存容量，单位：`GB`
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        :param _K8SVersion: 第三方节点kubelet版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type K8SVersion: str
        """
        self._Name = None
        self._CPU = None
        self._Memory = None
        self._K8SVersion = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def K8SVersion(self):
        return self._K8SVersion

    @K8SVersion.setter
    def K8SVersion(self, K8SVersion):
        self._K8SVersion = K8SVersion


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._K8SVersion = params.get("K8SVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalNodePoolInfo(AbstractModel):
    """第三方节点池信息

    """

    def __init__(self):
        r"""
        :param _RuntimeConfig: 第三方节点Runtime配置
        :type RuntimeConfig: :class:`tencentcloud.tke.v20220501.models.RuntimeConfig`
        :param _NodesNum: 节点数
注意：此字段可能返回 null，表示取不到有效值。
        :type NodesNum: int
        """
        self._RuntimeConfig = None
        self._NodesNum = None

    @property
    def RuntimeConfig(self):
        return self._RuntimeConfig

    @RuntimeConfig.setter
    def RuntimeConfig(self, RuntimeConfig):
        self._RuntimeConfig = RuntimeConfig

    @property
    def NodesNum(self):
        return self._NodesNum

    @NodesNum.setter
    def NodesNum(self, NodesNum):
        self._NodesNum = NodesNum


    def _deserialize(self, params):
        if params.get("RuntimeConfig") is not None:
            self._RuntimeConfig = RuntimeConfig()
            self._RuntimeConfig._deserialize(params.get("RuntimeConfig"))
        self._NodesNum = params.get("NodesNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class Instance(AbstractModel):
    """集群的实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceRole: 节点角色, MASTER, WORKER, ETCD, MASTER_ETCD,ALL, 默认为WORKER
        :type InstanceRole: str
        :param _FailedReason: 实例异常(或者处于初始化中)的原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedReason: str
        :param _InstanceState: 实例的状态
- initializing创建中
- running 运行中
- failed 异常
        :type InstanceState: str
        :param _Unschedulable: 是否不可调度
注意：此字段可能返回 null，表示取不到有效值。
        :type Unschedulable: bool
        :param _CreatedTime: 添加时间
        :type CreatedTime: str
        :param _LanIP: 节点内网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type LanIP: str
        :param _NodePoolId: 资源池ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NodePoolId: str
        :param _Native: 原生节点参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Native: :class:`tencentcloud.tke.v20220501.models.NativeNodeInfo`
        :param _Regular: 普通节点参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Regular: :class:`tencentcloud.tke.v20220501.models.RegularNodeInfo`
        :param _Super: 超级节点参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Super: :class:`tencentcloud.tke.v20220501.models.SuperNodeInfo`
        :param _External: 第三方节点参数
注意：此字段可能返回 null，表示取不到有效值。
        :type External: :class:`tencentcloud.tke.v20220501.models.ExternalNodeInfo`
        :param _NodeType: 节点类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: str
        """
        self._InstanceId = None
        self._InstanceRole = None
        self._FailedReason = None
        self._InstanceState = None
        self._Unschedulable = None
        self._CreatedTime = None
        self._LanIP = None
        self._NodePoolId = None
        self._Native = None
        self._Regular = None
        self._Super = None
        self._External = None
        self._NodeType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def FailedReason(self):
        return self._FailedReason

    @FailedReason.setter
    def FailedReason(self, FailedReason):
        self._FailedReason = FailedReason

    @property
    def InstanceState(self):
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def Unschedulable(self):
        return self._Unschedulable

    @Unschedulable.setter
    def Unschedulable(self, Unschedulable):
        self._Unschedulable = Unschedulable

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def LanIP(self):
        return self._LanIP

    @LanIP.setter
    def LanIP(self, LanIP):
        self._LanIP = LanIP

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def Native(self):
        return self._Native

    @Native.setter
    def Native(self, Native):
        self._Native = Native

    @property
    def Regular(self):
        return self._Regular

    @Regular.setter
    def Regular(self, Regular):
        self._Regular = Regular

    @property
    def Super(self):
        return self._Super

    @Super.setter
    def Super(self, Super):
        self._Super = Super

    @property
    def External(self):
        return self._External

    @External.setter
    def External(self, External):
        self._External = External

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceRole = params.get("InstanceRole")
        self._FailedReason = params.get("FailedReason")
        self._InstanceState = params.get("InstanceState")
        self._Unschedulable = params.get("Unschedulable")
        self._CreatedTime = params.get("CreatedTime")
        self._LanIP = params.get("LanIP")
        self._NodePoolId = params.get("NodePoolId")
        if params.get("Native") is not None:
            self._Native = NativeNodeInfo()
            self._Native._deserialize(params.get("Native"))
        if params.get("Regular") is not None:
            self._Regular = RegularNodeInfo()
            self._Regular._deserialize(params.get("Regular"))
        if params.get("Super") is not None:
            self._Super = SuperNodeInfo()
            self._Super._deserialize(params.get("Super"))
        if params.get("External") is not None:
            self._External = ExternalNodeInfo()
            self._External._deserialize(params.get("External"))
        self._NodeType = params.get("NodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAdvancedSettings(AbstractModel):
    """描述了k8s集群相关配置与信息。

    """

    def __init__(self):
        r"""
        :param _DesiredPodNumber: 该节点属于podCIDR大小自定义模式时，可指定节点上运行的pod数量上限
注意：此字段可能返回 null，表示取不到有效值。
        :type DesiredPodNumber: int
        :param _PreStartUserScript: base64 编码的用户脚本，在初始化节点之前执行，目前只对添加已有节点生效
注意：此字段可能返回 null，表示取不到有效值。
        :type PreStartUserScript: str
        :param _RuntimeConfig: 运行时描述
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeConfig: :class:`tencentcloud.tke.v20220501.models.RuntimeConfig`
        :param _UserScript: base64 编码的用户脚本, 此脚本会在 k8s 组件运行后执行, 需要用户保证脚本的可重入及重试逻辑, 脚本及其生成的日志文件可在节点的 /data/ccs_userscript/ 路径查看, 如果要求节点需要在进行初始化完成后才可加入调度, 可配合 unschedulable 参数使用, 在 userScript 最后初始化完成后, 添加 kubectl uncordon nodename --kubeconfig=/root/.kube/config 命令使节点加入调度
注意：此字段可能返回 null，表示取不到有效值。
        :type UserScript: str
        :param _ExtraArgs: 节点相关的自定义参数信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraArgs: :class:`tencentcloud.tke.v20220501.models.InstanceExtraArgs`
        """
        self._DesiredPodNumber = None
        self._PreStartUserScript = None
        self._RuntimeConfig = None
        self._UserScript = None
        self._ExtraArgs = None

    @property
    def DesiredPodNumber(self):
        return self._DesiredPodNumber

    @DesiredPodNumber.setter
    def DesiredPodNumber(self, DesiredPodNumber):
        self._DesiredPodNumber = DesiredPodNumber

    @property
    def PreStartUserScript(self):
        return self._PreStartUserScript

    @PreStartUserScript.setter
    def PreStartUserScript(self, PreStartUserScript):
        self._PreStartUserScript = PreStartUserScript

    @property
    def RuntimeConfig(self):
        return self._RuntimeConfig

    @RuntimeConfig.setter
    def RuntimeConfig(self, RuntimeConfig):
        self._RuntimeConfig = RuntimeConfig

    @property
    def UserScript(self):
        return self._UserScript

    @UserScript.setter
    def UserScript(self, UserScript):
        self._UserScript = UserScript

    @property
    def ExtraArgs(self):
        return self._ExtraArgs

    @ExtraArgs.setter
    def ExtraArgs(self, ExtraArgs):
        self._ExtraArgs = ExtraArgs


    def _deserialize(self, params):
        self._DesiredPodNumber = params.get("DesiredPodNumber")
        self._PreStartUserScript = params.get("PreStartUserScript")
        if params.get("RuntimeConfig") is not None:
            self._RuntimeConfig = RuntimeConfig()
            self._RuntimeConfig._deserialize(params.get("RuntimeConfig"))
        self._UserScript = params.get("UserScript")
        if params.get("ExtraArgs") is not None:
            self._ExtraArgs = InstanceExtraArgs()
            self._ExtraArgs._deserialize(params.get("ExtraArgs"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceExtraArgs(AbstractModel):
    """节点自定义参数

    """

    def __init__(self):
        r"""
        :param _Kubelet: kubelet自定义参数，参数格式为["k1=v1", "k1=v2"]， 例如["root-dir=/var/lib/kubelet","feature-gates=PodShareProcessNamespace=true,DynamicKubeletConfig=true"]
注意：此字段可能返回 null，表示取不到有效值。
        :type Kubelet: list of str
        """
        self._Kubelet = None

    @property
    def Kubelet(self):
        return self._Kubelet

    @Kubelet.setter
    def Kubelet(self, Kubelet):
        self._Kubelet = Kubelet


    def _deserialize(self, params):
        self._Kubelet = params.get("Kubelet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAccessible(AbstractModel):
    """公网带宽

    """

    def __init__(self):
        r"""
        :param _MaxBandwidthOut: 带宽
        :type MaxBandwidthOut: int
        :param _ChargeType: 网络计费方式
        :type ChargeType: str
        :param _BandwidthPackageId: 带宽包 ID
        :type BandwidthPackageId: str
        """
        self._MaxBandwidthOut = None
        self._ChargeType = None
        self._BandwidthPackageId = None

    @property
    def MaxBandwidthOut(self):
        return self._MaxBandwidthOut

    @MaxBandwidthOut.setter
    def MaxBandwidthOut(self, MaxBandwidthOut):
        self._MaxBandwidthOut = MaxBandwidthOut

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def BandwidthPackageId(self):
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId


    def _deserialize(self, params):
        self._MaxBandwidthOut = params.get("MaxBandwidthOut")
        self._ChargeType = params.get("ChargeType")
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    """k8s中标签，一般以数组的方式存在

    """

    def __init__(self):
        r"""
        :param _Name: map表中的Name
        :type Name: str
        :param _Value: map表中的Value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManuallyAdded(AbstractModel):
    """手动加入的节点

    """

    def __init__(self):
        r"""
        :param _Joining: 加入中的节点数量
        :type Joining: int
        :param _Initializing: 初始化中的节点数量
        :type Initializing: int
        :param _Normal: 正常的节点数量
        :type Normal: int
        :param _Total: 节点总数
        :type Total: int
        """
        self._Joining = None
        self._Initializing = None
        self._Normal = None
        self._Total = None

    @property
    def Joining(self):
        return self._Joining

    @Joining.setter
    def Joining(self, Joining):
        self._Joining = Joining

    @property
    def Initializing(self):
        return self._Initializing

    @Initializing.setter
    def Initializing(self, Initializing):
        self._Initializing = Initializing

    @property
    def Normal(self):
        return self._Normal

    @Normal.setter
    def Normal(self, Normal):
        self._Normal = Normal

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Joining = params.get("Joining")
        self._Initializing = params.get("Initializing")
        self._Normal = params.get("Normal")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NativeNodeInfo(AbstractModel):
    """节点信息

    """

    def __init__(self):
        r"""
        :param _MachineName: 节点名称
        :type MachineName: str
        :param _MachineState: Machine 状态
        :type MachineState: str
        :param _Zone: Machine 所在可用区
        :type Zone: str
        :param _InstanceChargeType: 节点计费类型。PREPAID：包年包月；POSTPAID_BY_HOUR：按量计费（默认）；
        :type InstanceChargeType: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _LoginStatus: Machine 登录状态
注意：此字段可能返回 null，表示取不到有效值。
        :type LoginStatus: str
        :param _IsProtectedFromScaleIn: 是否开启缩容保护
注意：此字段可能返回 null，表示取不到有效值。
        :type IsProtectedFromScaleIn: bool
        :param _DisplayName: Machine 名字
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param _CPU: CPU核数，单位：核
        :type CPU: int
        :param _GPU: GPU核数，单位：核
注意：此字段可能返回 null，表示取不到有效值。
        :type GPU: int
        :param _RenewFlag: 自动续费标识
        :type RenewFlag: str
        :param _PayMode: 节点计费模式（已弃用）
        :type PayMode: str
        :param _Memory: 节点内存容量，单位：`GB`
        :type Memory: int
        :param _InternetAccessible: 公网带宽相关信息设置
        :type InternetAccessible: :class:`tencentcloud.tke.v20220501.models.InternetAccessible`
        :param _InstanceFamily: 机型所属机型族
        :type InstanceFamily: str
        :param _LanIp: 节点内网 IP
        :type LanIp: str
        :param _InstanceType: 机型
        :type InstanceType: str
        :param _ExpiredTime: 包年包月节点计费过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredTime: str
        :param _SecurityGroupIDs: 安全组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupIDs: list of str
        :param _VpcId: VPC 唯一 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网唯一 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _OsImage: OS的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OsImage: str
        """
        self._MachineName = None
        self._MachineState = None
        self._Zone = None
        self._InstanceChargeType = None
        self._CreatedAt = None
        self._LoginStatus = None
        self._IsProtectedFromScaleIn = None
        self._DisplayName = None
        self._CPU = None
        self._GPU = None
        self._RenewFlag = None
        self._PayMode = None
        self._Memory = None
        self._InternetAccessible = None
        self._InstanceFamily = None
        self._LanIp = None
        self._InstanceType = None
        self._ExpiredTime = None
        self._SecurityGroupIDs = None
        self._VpcId = None
        self._SubnetId = None
        self._OsImage = None

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def MachineState(self):
        return self._MachineState

    @MachineState.setter
    def MachineState(self, MachineState):
        self._MachineState = MachineState

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def LoginStatus(self):
        return self._LoginStatus

    @LoginStatus.setter
    def LoginStatus(self, LoginStatus):
        self._LoginStatus = LoginStatus

    @property
    def IsProtectedFromScaleIn(self):
        return self._IsProtectedFromScaleIn

    @IsProtectedFromScaleIn.setter
    def IsProtectedFromScaleIn(self, IsProtectedFromScaleIn):
        self._IsProtectedFromScaleIn = IsProtectedFromScaleIn

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def GPU(self):
        return self._GPU

    @GPU.setter
    def GPU(self, GPU):
        self._GPU = GPU

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceFamily(self):
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def LanIp(self):
        return self._LanIp

    @LanIp.setter
    def LanIp(self, LanIp):
        self._LanIp = LanIp

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def SecurityGroupIDs(self):
        return self._SecurityGroupIDs

    @SecurityGroupIDs.setter
    def SecurityGroupIDs(self, SecurityGroupIDs):
        self._SecurityGroupIDs = SecurityGroupIDs

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
    def OsImage(self):
        return self._OsImage

    @OsImage.setter
    def OsImage(self, OsImage):
        self._OsImage = OsImage


    def _deserialize(self, params):
        self._MachineName = params.get("MachineName")
        self._MachineState = params.get("MachineState")
        self._Zone = params.get("Zone")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._CreatedAt = params.get("CreatedAt")
        self._LoginStatus = params.get("LoginStatus")
        self._IsProtectedFromScaleIn = params.get("IsProtectedFromScaleIn")
        self._DisplayName = params.get("DisplayName")
        self._CPU = params.get("CPU")
        self._GPU = params.get("GPU")
        self._RenewFlag = params.get("RenewFlag")
        self._PayMode = params.get("PayMode")
        self._Memory = params.get("Memory")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceFamily = params.get("InstanceFamily")
        self._LanIp = params.get("LanIp")
        self._InstanceType = params.get("InstanceType")
        self._ExpiredTime = params.get("ExpiredTime")
        self._SecurityGroupIDs = params.get("SecurityGroupIDs")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._OsImage = params.get("OsImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NativeNodePoolInfo(AbstractModel):
    """原生节点池信息

    """

    def __init__(self):
        r"""
        :param _SubnetIds: 子网列表
        :type SubnetIds: list of str
        :param _SecurityGroupIds: 安全组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupIds: list of str
        """
        self._SubnetIds = None
        self._SecurityGroupIds = None

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._SubnetIds = params.get("SubnetIds")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeCountSummary(AbstractModel):
    """节点统计列表

    """

    def __init__(self):
        r"""
        :param _ManuallyAdded: 手动管理的节点
注意：此字段可能返回 null，表示取不到有效值。
        :type ManuallyAdded: :class:`tencentcloud.tke.v20220501.models.ManuallyAdded`
        :param _AutoscalingAdded: 自动管理的节点
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoscalingAdded: :class:`tencentcloud.tke.v20220501.models.AutoscalingAdded`
        """
        self._ManuallyAdded = None
        self._AutoscalingAdded = None

    @property
    def ManuallyAdded(self):
        return self._ManuallyAdded

    @ManuallyAdded.setter
    def ManuallyAdded(self, ManuallyAdded):
        self._ManuallyAdded = ManuallyAdded

    @property
    def AutoscalingAdded(self):
        return self._AutoscalingAdded

    @AutoscalingAdded.setter
    def AutoscalingAdded(self, AutoscalingAdded):
        self._AutoscalingAdded = AutoscalingAdded


    def _deserialize(self, params):
        if params.get("ManuallyAdded") is not None:
            self._ManuallyAdded = ManuallyAdded()
            self._ManuallyAdded._deserialize(params.get("ManuallyAdded"))
        if params.get("AutoscalingAdded") is not None:
            self._AutoscalingAdded = AutoscalingAdded()
            self._AutoscalingAdded._deserialize(params.get("AutoscalingAdded"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodePool(AbstractModel):
    """节点池信息

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群 ID
        :type ClusterId: str
        :param _NodePoolId: 节点池 ID
        :type NodePoolId: str
        :param _Taints: 节点污点
注意：此字段可能返回 null，表示取不到有效值。
        :type Taints: list of Taint
        :param _DeletionProtection: 是否开启删除保护
注意：此字段可能返回 null，表示取不到有效值。
        :type DeletionProtection: bool
        :param _Type: 节点池类型
        :type Type: str
        :param _Labels: 节点  Labels
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of Label
        :param _LifeState: 节点池状态
        :type LifeState: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _Name: 节点池名称
        :type Name: str
        :param _Native: 原生节点池参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Native: :class:`tencentcloud.tke.v20220501.models.NativeNodePoolInfo`
        :param _Annotations: 节点 Annotation 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Annotations: list of Annotation
        :param _Super: 超级节点池参数，在Type等于Super该字段才有值
注意：此字段可能返回 null，表示取不到有效值。
        :type Super: :class:`tencentcloud.tke.v20220501.models.SuperNodePoolInfo`
        :param _Regular: 普通节点池参数，在Type等于Regular该字段才有值
注意：此字段可能返回 null，表示取不到有效值。
        :type Regular: :class:`tencentcloud.tke.v20220501.models.RegularNodePoolInfo`
        :param _External: 第三方节点池参数，在Type等于External该字段才有值
注意：此字段可能返回 null，表示取不到有效值。
        :type External: :class:`tencentcloud.tke.v20220501.models.ExternalNodePoolInfo`
        """
        self._ClusterId = None
        self._NodePoolId = None
        self._Taints = None
        self._DeletionProtection = None
        self._Type = None
        self._Labels = None
        self._LifeState = None
        self._CreatedAt = None
        self._Name = None
        self._Native = None
        self._Annotations = None
        self._Super = None
        self._Regular = None
        self._External = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def Taints(self):
        return self._Taints

    @Taints.setter
    def Taints(self, Taints):
        self._Taints = Taints

    @property
    def DeletionProtection(self):
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def LifeState(self):
        return self._LifeState

    @LifeState.setter
    def LifeState(self, LifeState):
        self._LifeState = LifeState

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Native(self):
        return self._Native

    @Native.setter
    def Native(self, Native):
        self._Native = Native

    @property
    def Annotations(self):
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations

    @property
    def Super(self):
        return self._Super

    @Super.setter
    def Super(self, Super):
        self._Super = Super

    @property
    def Regular(self):
        return self._Regular

    @Regular.setter
    def Regular(self, Regular):
        self._Regular = Regular

    @property
    def External(self):
        return self._External

    @External.setter
    def External(self, External):
        self._External = External


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodePoolId = params.get("NodePoolId")
        if params.get("Taints") is not None:
            self._Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self._Taints.append(obj)
        self._DeletionProtection = params.get("DeletionProtection")
        self._Type = params.get("Type")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._LifeState = params.get("LifeState")
        self._CreatedAt = params.get("CreatedAt")
        self._Name = params.get("Name")
        if params.get("Native") is not None:
            self._Native = NativeNodePoolInfo()
            self._Native._deserialize(params.get("Native"))
        if params.get("Annotations") is not None:
            self._Annotations = []
            for item in params.get("Annotations"):
                obj = Annotation()
                obj._deserialize(item)
                self._Annotations.append(obj)
        if params.get("Super") is not None:
            self._Super = SuperNodePoolInfo()
            self._Super._deserialize(params.get("Super"))
        if params.get("Regular") is not None:
            self._Regular = RegularNodePoolInfo()
            self._Regular._deserialize(params.get("Regular"))
        if params.get("External") is not None:
            self._External = ExternalNodePoolInfo()
            self._External._deserialize(params.get("External"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegularNodeInfo(AbstractModel):
    """普通节点信息

    """

    def __init__(self):
        r"""
        :param _InstanceAdvancedSettings: 节点配置
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20220501.models.InstanceAdvancedSettings`
        :param _AutoscalingGroupId: 自动伸缩组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoscalingGroupId: str
        """
        self._InstanceAdvancedSettings = None
        self._AutoscalingGroupId = None

    @property
    def InstanceAdvancedSettings(self):
        return self._InstanceAdvancedSettings

    @InstanceAdvancedSettings.setter
    def InstanceAdvancedSettings(self, InstanceAdvancedSettings):
        self._InstanceAdvancedSettings = InstanceAdvancedSettings

    @property
    def AutoscalingGroupId(self):
        return self._AutoscalingGroupId

    @AutoscalingGroupId.setter
    def AutoscalingGroupId(self, AutoscalingGroupId):
        self._AutoscalingGroupId = AutoscalingGroupId


    def _deserialize(self, params):
        if params.get("InstanceAdvancedSettings") is not None:
            self._InstanceAdvancedSettings = InstanceAdvancedSettings()
            self._InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        self._AutoscalingGroupId = params.get("AutoscalingGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegularNodePoolInfo(AbstractModel):
    """普通节点池信息

    """

    def __init__(self):
        r"""
        :param _LaunchConfigurationId: LaunchConfigurationId 配置
        :type LaunchConfigurationId: str
        :param _AutoscalingGroupId: AutoscalingGroupId 分组id
        :type AutoscalingGroupId: str
        :param _NodeCountSummary: NodeCountSummary 节点列表
        :type NodeCountSummary: :class:`tencentcloud.tke.v20220501.models.NodeCountSummary`
        :param _AutoscalingGroupStatus: 状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoscalingGroupStatus: str
        :param _MaxNodesNum: 最大节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxNodesNum: int
        :param _MinNodesNum: 最小节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MinNodesNum: int
        :param _DesiredNodesNum: 期望的节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DesiredNodesNum: int
        :param _NodePoolOs: 节点池osName
注意：此字段可能返回 null，表示取不到有效值。
        :type NodePoolOs: str
        :param _InstanceAdvancedSettings: 节点配置
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20220501.models.InstanceAdvancedSettings`
        """
        self._LaunchConfigurationId = None
        self._AutoscalingGroupId = None
        self._NodeCountSummary = None
        self._AutoscalingGroupStatus = None
        self._MaxNodesNum = None
        self._MinNodesNum = None
        self._DesiredNodesNum = None
        self._NodePoolOs = None
        self._InstanceAdvancedSettings = None

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def AutoscalingGroupId(self):
        return self._AutoscalingGroupId

    @AutoscalingGroupId.setter
    def AutoscalingGroupId(self, AutoscalingGroupId):
        self._AutoscalingGroupId = AutoscalingGroupId

    @property
    def NodeCountSummary(self):
        return self._NodeCountSummary

    @NodeCountSummary.setter
    def NodeCountSummary(self, NodeCountSummary):
        self._NodeCountSummary = NodeCountSummary

    @property
    def AutoscalingGroupStatus(self):
        return self._AutoscalingGroupStatus

    @AutoscalingGroupStatus.setter
    def AutoscalingGroupStatus(self, AutoscalingGroupStatus):
        self._AutoscalingGroupStatus = AutoscalingGroupStatus

    @property
    def MaxNodesNum(self):
        return self._MaxNodesNum

    @MaxNodesNum.setter
    def MaxNodesNum(self, MaxNodesNum):
        self._MaxNodesNum = MaxNodesNum

    @property
    def MinNodesNum(self):
        return self._MinNodesNum

    @MinNodesNum.setter
    def MinNodesNum(self, MinNodesNum):
        self._MinNodesNum = MinNodesNum

    @property
    def DesiredNodesNum(self):
        return self._DesiredNodesNum

    @DesiredNodesNum.setter
    def DesiredNodesNum(self, DesiredNodesNum):
        self._DesiredNodesNum = DesiredNodesNum

    @property
    def NodePoolOs(self):
        return self._NodePoolOs

    @NodePoolOs.setter
    def NodePoolOs(self, NodePoolOs):
        self._NodePoolOs = NodePoolOs

    @property
    def InstanceAdvancedSettings(self):
        return self._InstanceAdvancedSettings

    @InstanceAdvancedSettings.setter
    def InstanceAdvancedSettings(self, InstanceAdvancedSettings):
        self._InstanceAdvancedSettings = InstanceAdvancedSettings


    def _deserialize(self, params):
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._AutoscalingGroupId = params.get("AutoscalingGroupId")
        if params.get("NodeCountSummary") is not None:
            self._NodeCountSummary = NodeCountSummary()
            self._NodeCountSummary._deserialize(params.get("NodeCountSummary"))
        self._AutoscalingGroupStatus = params.get("AutoscalingGroupStatus")
        self._MaxNodesNum = params.get("MaxNodesNum")
        self._MinNodesNum = params.get("MinNodesNum")
        self._DesiredNodesNum = params.get("DesiredNodesNum")
        self._NodePoolOs = params.get("NodePoolOs")
        if params.get("InstanceAdvancedSettings") is not None:
            self._InstanceAdvancedSettings = InstanceAdvancedSettings()
            self._InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuntimeConfig(AbstractModel):
    """运行时配置

    """

    def __init__(self):
        r"""
        :param _RuntimeType: 运行时类型
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeType: str
        :param _RuntimeVersion: 运行时版本
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeVersion: str
        :param _RuntimeRootDir: 运行时根目录
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeRootDir: str
        """
        self._RuntimeType = None
        self._RuntimeVersion = None
        self._RuntimeRootDir = None

    @property
    def RuntimeType(self):
        return self._RuntimeType

    @RuntimeType.setter
    def RuntimeType(self, RuntimeType):
        self._RuntimeType = RuntimeType

    @property
    def RuntimeVersion(self):
        return self._RuntimeVersion

    @RuntimeVersion.setter
    def RuntimeVersion(self, RuntimeVersion):
        self._RuntimeVersion = RuntimeVersion

    @property
    def RuntimeRootDir(self):
        return self._RuntimeRootDir

    @RuntimeRootDir.setter
    def RuntimeRootDir(self, RuntimeRootDir):
        self._RuntimeRootDir = RuntimeRootDir


    def _deserialize(self, params):
        self._RuntimeType = params.get("RuntimeType")
        self._RuntimeVersion = params.get("RuntimeVersion")
        self._RuntimeRootDir = params.get("RuntimeRootDir")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SortBy(AbstractModel):
    """排序信息

    """

    def __init__(self):
        r"""
        :param _FieldName: 排序指标
        :type FieldName: str
        :param _OrderType: 排序方式
        :type OrderType: str
        """
        self._FieldName = None
        self._OrderType = None

    @property
    def FieldName(self):
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._FieldName = params.get("FieldName")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuperNodeInfo(AbstractModel):
    """超级节点信息

    """

    def __init__(self):
        r"""
        :param _Name: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _AutoRenewFlag: 自动续费标识
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param _ResourceType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _CPU: 节点的 CPU 规格，单位：核。
注意：此字段可能返回 null，表示取不到有效值。
        :type CPU: float
        :param _UsedCPU: 节点上 Pod 的 CPU总和，单位：核。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedCPU: float
        :param _Memory: 节点的内存规格，单位：Gi。
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: float
        :param _UsedMemory: 节点上 Pod 的内存总和，单位：Gi。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedMemory: float
        :param _Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _VpcId: VPC 唯一 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网唯一 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _ActiveAt: 生效时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveAt: str
        :param _ExpireAt: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireAt: str
        :param _MaxCPUScheduledPod: 可调度的单 Pod 最大 CPU 规格
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxCPUScheduledPod: int
        :param _InstanceAttribute: 实例属性
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceAttribute: str
        """
        self._Name = None
        self._AutoRenewFlag = None
        self._ResourceType = None
        self._CPU = None
        self._UsedCPU = None
        self._Memory = None
        self._UsedMemory = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._ActiveAt = None
        self._ExpireAt = None
        self._MaxCPUScheduledPod = None
        self._InstanceAttribute = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def UsedCPU(self):
        return self._UsedCPU

    @UsedCPU.setter
    def UsedCPU(self, UsedCPU):
        self._UsedCPU = UsedCPU

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def UsedMemory(self):
        return self._UsedMemory

    @UsedMemory.setter
    def UsedMemory(self, UsedMemory):
        self._UsedMemory = UsedMemory

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

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
    def ActiveAt(self):
        return self._ActiveAt

    @ActiveAt.setter
    def ActiveAt(self, ActiveAt):
        self._ActiveAt = ActiveAt

    @property
    def ExpireAt(self):
        return self._ExpireAt

    @ExpireAt.setter
    def ExpireAt(self, ExpireAt):
        self._ExpireAt = ExpireAt

    @property
    def MaxCPUScheduledPod(self):
        return self._MaxCPUScheduledPod

    @MaxCPUScheduledPod.setter
    def MaxCPUScheduledPod(self, MaxCPUScheduledPod):
        self._MaxCPUScheduledPod = MaxCPUScheduledPod

    @property
    def InstanceAttribute(self):
        return self._InstanceAttribute

    @InstanceAttribute.setter
    def InstanceAttribute(self, InstanceAttribute):
        self._InstanceAttribute = InstanceAttribute


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._ResourceType = params.get("ResourceType")
        self._CPU = params.get("CPU")
        self._UsedCPU = params.get("UsedCPU")
        self._Memory = params.get("Memory")
        self._UsedMemory = params.get("UsedMemory")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ActiveAt = params.get("ActiveAt")
        self._ExpireAt = params.get("ExpireAt")
        self._MaxCPUScheduledPod = params.get("MaxCPUScheduledPod")
        self._InstanceAttribute = params.get("InstanceAttribute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuperNodePoolInfo(AbstractModel):
    """虚拟节点池信息

    """

    def __init__(self):
        r"""
        :param _SubnetIds: 子网列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of str
        :param _SecurityGroupIds: 安全组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupIds: list of str
        """
        self._SubnetIds = None
        self._SecurityGroupIds = None

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._SubnetIds = params.get("SubnetIds")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Taint(AbstractModel):
    """kubernetes Taint

    """

    def __init__(self):
        r"""
        :param _Key: Taint的Key
        :type Key: str
        :param _Value: Taint的Value
        :type Value: str
        :param _Effect: Taint的Effect
        :type Effect: str
        """
        self._Key = None
        self._Value = None
        self._Effect = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Effect(self):
        return self._Effect

    @Effect.setter
    def Effect(self, Effect):
        self._Effect = Effect


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Effect = params.get("Effect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        