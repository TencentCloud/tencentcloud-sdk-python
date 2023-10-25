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


class Activity(AbstractModel):
    """符合条件的伸缩活动相关信息。

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID。
        :type AutoScalingGroupId: str
        :param _ActivityId: 伸缩活动ID。
        :type ActivityId: str
        :param _ActivityType: 伸缩活动类型。取值如下：<br>
<li>SCALE_OUT：扩容活动<li>SCALE_IN：缩容活动<li>ATTACH_INSTANCES：添加实例<li>REMOVE_INSTANCES：销毁实例<li>DETACH_INSTANCES：移出实例<li>TERMINATE_INSTANCES_UNEXPECTEDLY：实例在CVM控制台被销毁<li>REPLACE_UNHEALTHY_INSTANCE：替换不健康实例
<li>START_INSTANCES：开启实例
<li>STOP_INSTANCES：关闭实例
<li>INVOKE_COMMAND：执行命令
        :type ActivityType: str
        :param _StatusCode: 伸缩活动状态。取值如下：<br>
<li>INIT：初始化中
<li>RUNNING：运行中
<li>SUCCESSFUL：活动成功
<li>PARTIALLY_SUCCESSFUL：活动部分成功
<li>FAILED：活动失败
<li>CANCELLED：活动取消
        :type StatusCode: str
        :param _StatusMessage: 伸缩活动状态描述。
        :type StatusMessage: str
        :param _Cause: 伸缩活动起因。
        :type Cause: str
        :param _Description: 伸缩活动描述。
        :type Description: str
        :param _StartTime: 伸缩活动开始时间。
        :type StartTime: str
        :param _EndTime: 伸缩活动结束时间。
        :type EndTime: str
        :param _CreatedTime: 伸缩活动创建时间。
        :type CreatedTime: str
        :param _ActivityRelatedInstanceSet: 该参数已废弃，请勿使用。
        :type ActivityRelatedInstanceSet: list of ActivtyRelatedInstance
        :param _StatusMessageSimplified: 伸缩活动状态简要描述。
        :type StatusMessageSimplified: str
        :param _LifecycleActionResultSet: 伸缩活动中生命周期挂钩的执行结果。
        :type LifecycleActionResultSet: list of LifecycleActionResultInfo
        :param _DetailedStatusMessageSet: 伸缩活动状态详细描述。
        :type DetailedStatusMessageSet: list of DetailedStatusMessage
        :param _InvocationResultSet: 执行命令结果。
        :type InvocationResultSet: list of InvocationResult
        :param _RelatedInstanceSet: 伸缩活动相关实例信息集合。
        :type RelatedInstanceSet: list of RelatedInstance
        """
        self._AutoScalingGroupId = None
        self._ActivityId = None
        self._ActivityType = None
        self._StatusCode = None
        self._StatusMessage = None
        self._Cause = None
        self._Description = None
        self._StartTime = None
        self._EndTime = None
        self._CreatedTime = None
        self._ActivityRelatedInstanceSet = None
        self._StatusMessageSimplified = None
        self._LifecycleActionResultSet = None
        self._DetailedStatusMessageSet = None
        self._InvocationResultSet = None
        self._RelatedInstanceSet = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def ActivityType(self):
        return self._ActivityType

    @ActivityType.setter
    def ActivityType(self, ActivityType):
        self._ActivityType = ActivityType

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def StatusMessage(self):
        return self._StatusMessage

    @StatusMessage.setter
    def StatusMessage(self, StatusMessage):
        self._StatusMessage = StatusMessage

    @property
    def Cause(self):
        return self._Cause

    @Cause.setter
    def Cause(self, Cause):
        self._Cause = Cause

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ActivityRelatedInstanceSet(self):
        warnings.warn("parameter `ActivityRelatedInstanceSet` is deprecated", DeprecationWarning) 

        return self._ActivityRelatedInstanceSet

    @ActivityRelatedInstanceSet.setter
    def ActivityRelatedInstanceSet(self, ActivityRelatedInstanceSet):
        warnings.warn("parameter `ActivityRelatedInstanceSet` is deprecated", DeprecationWarning) 

        self._ActivityRelatedInstanceSet = ActivityRelatedInstanceSet

    @property
    def StatusMessageSimplified(self):
        return self._StatusMessageSimplified

    @StatusMessageSimplified.setter
    def StatusMessageSimplified(self, StatusMessageSimplified):
        self._StatusMessageSimplified = StatusMessageSimplified

    @property
    def LifecycleActionResultSet(self):
        return self._LifecycleActionResultSet

    @LifecycleActionResultSet.setter
    def LifecycleActionResultSet(self, LifecycleActionResultSet):
        self._LifecycleActionResultSet = LifecycleActionResultSet

    @property
    def DetailedStatusMessageSet(self):
        return self._DetailedStatusMessageSet

    @DetailedStatusMessageSet.setter
    def DetailedStatusMessageSet(self, DetailedStatusMessageSet):
        self._DetailedStatusMessageSet = DetailedStatusMessageSet

    @property
    def InvocationResultSet(self):
        return self._InvocationResultSet

    @InvocationResultSet.setter
    def InvocationResultSet(self, InvocationResultSet):
        self._InvocationResultSet = InvocationResultSet

    @property
    def RelatedInstanceSet(self):
        return self._RelatedInstanceSet

    @RelatedInstanceSet.setter
    def RelatedInstanceSet(self, RelatedInstanceSet):
        self._RelatedInstanceSet = RelatedInstanceSet


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._ActivityId = params.get("ActivityId")
        self._ActivityType = params.get("ActivityType")
        self._StatusCode = params.get("StatusCode")
        self._StatusMessage = params.get("StatusMessage")
        self._Cause = params.get("Cause")
        self._Description = params.get("Description")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CreatedTime = params.get("CreatedTime")
        if params.get("ActivityRelatedInstanceSet") is not None:
            self._ActivityRelatedInstanceSet = []
            for item in params.get("ActivityRelatedInstanceSet"):
                obj = ActivtyRelatedInstance()
                obj._deserialize(item)
                self._ActivityRelatedInstanceSet.append(obj)
        self._StatusMessageSimplified = params.get("StatusMessageSimplified")
        if params.get("LifecycleActionResultSet") is not None:
            self._LifecycleActionResultSet = []
            for item in params.get("LifecycleActionResultSet"):
                obj = LifecycleActionResultInfo()
                obj._deserialize(item)
                self._LifecycleActionResultSet.append(obj)
        if params.get("DetailedStatusMessageSet") is not None:
            self._DetailedStatusMessageSet = []
            for item in params.get("DetailedStatusMessageSet"):
                obj = DetailedStatusMessage()
                obj._deserialize(item)
                self._DetailedStatusMessageSet.append(obj)
        if params.get("InvocationResultSet") is not None:
            self._InvocationResultSet = []
            for item in params.get("InvocationResultSet"):
                obj = InvocationResult()
                obj._deserialize(item)
                self._InvocationResultSet.append(obj)
        if params.get("RelatedInstanceSet") is not None:
            self._RelatedInstanceSet = []
            for item in params.get("RelatedInstanceSet"):
                obj = RelatedInstance()
                obj._deserialize(item)
                self._RelatedInstanceSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivtyRelatedInstance(AbstractModel):
    """与本次伸缩活动相关的实例信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _InstanceStatus: 实例在伸缩活动中的状态。取值如下：
<li>INIT：初始化中
<li>RUNNING：实例操作中
<li>SUCCESSFUL：活动成功
<li>FAILED：活动失败
        :type InstanceStatus: str
        """
        self._InstanceId = None
        self._InstanceStatus = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceStatus = params.get("InstanceStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Advice(AbstractModel):
    """伸缩配置建议。

    """

    def __init__(self):
        r"""
        :param _Problem: 问题描述。
        :type Problem: str
        :param _Detail: 问题详情。
        :type Detail: str
        :param _Solution: 建议解决方案。
        :type Solution: str
        :param _Level: 伸缩建议警告级别。取值范围：<br>
<li>WARNING：警告级别<br>
<li>CRITICAL：严重级别<br>
        :type Level: str
        """
        self._Problem = None
        self._Detail = None
        self._Solution = None
        self._Level = None

    @property
    def Problem(self):
        return self._Problem

    @Problem.setter
    def Problem(self, Problem):
        self._Problem = Problem

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Solution(self):
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level


    def _deserialize(self, params):
        self._Problem = params.get("Problem")
        self._Detail = params.get("Detail")
        self._Solution = params.get("Solution")
        self._Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachInstancesRequest(AbstractModel):
    """AttachInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _InstanceIds: CVM实例ID列表
        :type InstanceIds: list of str
        """
        self._AutoScalingGroupId = None
        self._InstanceIds = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachInstancesResponse(AbstractModel):
    """AttachInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityId: 伸缩活动ID
        :type ActivityId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class AttachLoadBalancersRequest(AbstractModel):
    """AttachLoadBalancers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _LoadBalancerIds: 传统型负载均衡器ID列表，每个伸缩组绑定传统型负载均衡器数量上限为20，LoadBalancerIds 和 ForwardLoadBalancers 二者同时最多只能指定一个
        :type LoadBalancerIds: list of str
        :param _ForwardLoadBalancers: 应用型负载均衡器列表，每个伸缩组绑定应用型负载均衡器数量上限为100，LoadBalancerIds 和 ForwardLoadBalancers 二者同时最多只能指定一个
        :type ForwardLoadBalancers: list of ForwardLoadBalancer
        """
        self._AutoScalingGroupId = None
        self._LoadBalancerIds = None
        self._ForwardLoadBalancers = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ForwardLoadBalancers(self):
        return self._ForwardLoadBalancers

    @ForwardLoadBalancers.setter
    def ForwardLoadBalancers(self, ForwardLoadBalancers):
        self._ForwardLoadBalancers = ForwardLoadBalancers


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        if params.get("ForwardLoadBalancers") is not None:
            self._ForwardLoadBalancers = []
            for item in params.get("ForwardLoadBalancers"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self._ForwardLoadBalancers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachLoadBalancersResponse(AbstractModel):
    """AttachLoadBalancers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityId: 伸缩活动ID
        :type ActivityId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class AutoScalingAdvice(AbstractModel):
    """伸缩组配置建议。

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID。
        :type AutoScalingGroupId: str
        :param _Level: 伸缩组警告级别。取值范围：<br>
<li>NORMAL：正常<br>
<li>WARNING：警告级别<br>
<li>CRITICAL：严重级别<br>
        :type Level: str
        :param _Advices: 伸缩组配置建议集合。
        :type Advices: list of Advice
        """
        self._AutoScalingGroupId = None
        self._Level = None
        self._Advices = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Advices(self):
        return self._Advices

    @Advices.setter
    def Advices(self, Advices):
        self._Advices = Advices


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._Level = params.get("Level")
        if params.get("Advices") is not None:
            self._Advices = []
            for item in params.get("Advices"):
                obj = Advice()
                obj._deserialize(item)
                self._Advices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScalingGroup(AbstractModel):
    """伸缩组

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _AutoScalingGroupName: 伸缩组名称
        :type AutoScalingGroupName: str
        :param _AutoScalingGroupStatus: 伸缩组当前状态。取值范围：<br>
<li>NORMAL：正常<br>
<li>CVM_ABNORMAL：启动配置异常<br>
<li>LB_ABNORMAL：负载均衡器异常<br>
<li>LB_LISTENER_ABNORMAL：负载均衡器监听器异常<br>
<li>LB_LOCATION_ABNORMAL：负载均衡器监听器转发配置异常<br>
<li>VPC_ABNORMAL：VPC网络异常<br>
<li>SUBNET_ABNORMAL：VPC子网异常<br>
<li>INSUFFICIENT_BALANCE：余额不足<br>
<li>LB_BACKEND_REGION_NOT_MATCH：CLB实例后端地域与AS服务所在地域不匹配<br>
<li>LB_BACKEND_VPC_NOT_MATCH：CLB实例VPC与伸缩组VPC不匹配
        :type AutoScalingGroupStatus: str
        :param _CreatedTime: 创建时间，采用UTC标准计时
        :type CreatedTime: str
        :param _DefaultCooldown: 默认冷却时间，单位秒
        :type DefaultCooldown: int
        :param _DesiredCapacity: 期望实例数
        :type DesiredCapacity: int
        :param _EnabledStatus: 启用状态，取值包括`ENABLED`和`DISABLED`
        :type EnabledStatus: str
        :param _ForwardLoadBalancerSet: 应用型负载均衡器列表
        :type ForwardLoadBalancerSet: list of ForwardLoadBalancer
        :param _InstanceCount: 实例数量
        :type InstanceCount: int
        :param _InServiceInstanceCount: 状态为`IN_SERVICE`实例的数量
        :type InServiceInstanceCount: int
        :param _LaunchConfigurationId: 启动配置ID
        :type LaunchConfigurationId: str
        :param _LaunchConfigurationName: 启动配置名称
        :type LaunchConfigurationName: str
        :param _LoadBalancerIdSet: 传统型负载均衡器ID列表
        :type LoadBalancerIdSet: list of str
        :param _MaxSize: 最大实例数
        :type MaxSize: int
        :param _MinSize: 最小实例数
        :type MinSize: int
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _SubnetIdSet: 子网ID列表
        :type SubnetIdSet: list of str
        :param _TerminationPolicySet: 销毁策略
        :type TerminationPolicySet: list of str
        :param _VpcId: VPC标识
        :type VpcId: str
        :param _ZoneSet: 可用区列表
        :type ZoneSet: list of str
        :param _RetryPolicy: 重试策略
        :type RetryPolicy: str
        :param _InActivityStatus: 伸缩组是否处于伸缩活动中，`IN_ACTIVITY`表示处于伸缩活动中，`NOT_IN_ACTIVITY`表示不处于伸缩活动中。
        :type InActivityStatus: str
        :param _Tags: 伸缩组标签列表
        :type Tags: list of Tag
        :param _ServiceSettings: 服务设置
        :type ServiceSettings: :class:`tencentcloud.autoscaling.v20180419.models.ServiceSettings`
        :param _Ipv6AddressCount: 实例具有IPv6地址数量的配置
        :type Ipv6AddressCount: int
        :param _MultiZoneSubnetPolicy: 多可用区/子网策略。
<br><li> PRIORITY，按照可用区/子网列表的顺序，作为优先级来尝试创建实例，如果优先级最高的可用区/子网可以创建成功，则总在该可用区/子网创建。
<br><li> EQUALITY：每次选择当前实例数最少的可用区/子网进行扩容，使得每个可用区/子网都有机会发生扩容，多次扩容出的实例会打散到多个可用区/子网。
        :type MultiZoneSubnetPolicy: str
        :param _HealthCheckType: 伸缩组实例健康检查类型，取值如下：<br><li>CVM：根据实例网络状态判断实例是否处于不健康状态，不健康的网络状态即发生实例 PING 不可达事件，详细判断标准可参考[实例健康检查](https://cloud.tencent.com/document/product/377/8553)<br><li>CLB：根据 CLB 的健康检查状态判断实例是否处于不健康状态，CLB健康检查原理可参考[健康检查](https://cloud.tencent.com/document/product/214/6097)
        :type HealthCheckType: str
        :param _LoadBalancerHealthCheckGracePeriod: CLB健康检查宽限期
        :type LoadBalancerHealthCheckGracePeriod: int
        :param _InstanceAllocationPolicy: 实例分配策略，取值包括 LAUNCH_CONFIGURATION 和 SPOT_MIXED。
<br><li> LAUNCH_CONFIGURATION，代表传统的按照启动配置模式。
<br><li> SPOT_MIXED，代表竞价混合模式。目前仅支持启动配置为按量计费模式时使用混合模式，混合模式下，伸缩组将根据设定扩容按量或竞价机型。使用混合模式时，关联的启动配置的计费类型不可被修改。
        :type InstanceAllocationPolicy: str
        :param _SpotMixedAllocationPolicy: 竞价混合模式下，各计费类型实例的分配策略。
仅当 InstanceAllocationPolicy 取 SPOT_MIXED 时才会返回有效值。
        :type SpotMixedAllocationPolicy: :class:`tencentcloud.autoscaling.v20180419.models.SpotMixedAllocationPolicy`
        :param _CapacityRebalance: 容量重平衡功能，仅对伸缩组内的竞价实例有效。取值范围：
<br><li> TRUE，开启该功能，当伸缩组内的竞价实例即将被竞价实例服务自动回收前，AS 主动发起竞价实例销毁流程，如果有配置过缩容 hook，则销毁前 hook 会生效。销毁流程启动后，AS 会异步开启一个扩容活动，用于补齐期望实例数。
<br><li> FALSE，不开启该功能，则 AS 等待竞价实例被销毁后才会去扩容补齐伸缩组期望实例数。
        :type CapacityRebalance: bool
        """
        self._AutoScalingGroupId = None
        self._AutoScalingGroupName = None
        self._AutoScalingGroupStatus = None
        self._CreatedTime = None
        self._DefaultCooldown = None
        self._DesiredCapacity = None
        self._EnabledStatus = None
        self._ForwardLoadBalancerSet = None
        self._InstanceCount = None
        self._InServiceInstanceCount = None
        self._LaunchConfigurationId = None
        self._LaunchConfigurationName = None
        self._LoadBalancerIdSet = None
        self._MaxSize = None
        self._MinSize = None
        self._ProjectId = None
        self._SubnetIdSet = None
        self._TerminationPolicySet = None
        self._VpcId = None
        self._ZoneSet = None
        self._RetryPolicy = None
        self._InActivityStatus = None
        self._Tags = None
        self._ServiceSettings = None
        self._Ipv6AddressCount = None
        self._MultiZoneSubnetPolicy = None
        self._HealthCheckType = None
        self._LoadBalancerHealthCheckGracePeriod = None
        self._InstanceAllocationPolicy = None
        self._SpotMixedAllocationPolicy = None
        self._CapacityRebalance = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def AutoScalingGroupName(self):
        return self._AutoScalingGroupName

    @AutoScalingGroupName.setter
    def AutoScalingGroupName(self, AutoScalingGroupName):
        self._AutoScalingGroupName = AutoScalingGroupName

    @property
    def AutoScalingGroupStatus(self):
        return self._AutoScalingGroupStatus

    @AutoScalingGroupStatus.setter
    def AutoScalingGroupStatus(self, AutoScalingGroupStatus):
        self._AutoScalingGroupStatus = AutoScalingGroupStatus

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def DefaultCooldown(self):
        return self._DefaultCooldown

    @DefaultCooldown.setter
    def DefaultCooldown(self, DefaultCooldown):
        self._DefaultCooldown = DefaultCooldown

    @property
    def DesiredCapacity(self):
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def EnabledStatus(self):
        return self._EnabledStatus

    @EnabledStatus.setter
    def EnabledStatus(self, EnabledStatus):
        self._EnabledStatus = EnabledStatus

    @property
    def ForwardLoadBalancerSet(self):
        return self._ForwardLoadBalancerSet

    @ForwardLoadBalancerSet.setter
    def ForwardLoadBalancerSet(self, ForwardLoadBalancerSet):
        self._ForwardLoadBalancerSet = ForwardLoadBalancerSet

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def InServiceInstanceCount(self):
        return self._InServiceInstanceCount

    @InServiceInstanceCount.setter
    def InServiceInstanceCount(self, InServiceInstanceCount):
        self._InServiceInstanceCount = InServiceInstanceCount

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def LaunchConfigurationName(self):
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def LoadBalancerIdSet(self):
        return self._LoadBalancerIdSet

    @LoadBalancerIdSet.setter
    def LoadBalancerIdSet(self, LoadBalancerIdSet):
        self._LoadBalancerIdSet = LoadBalancerIdSet

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SubnetIdSet(self):
        return self._SubnetIdSet

    @SubnetIdSet.setter
    def SubnetIdSet(self, SubnetIdSet):
        self._SubnetIdSet = SubnetIdSet

    @property
    def TerminationPolicySet(self):
        return self._TerminationPolicySet

    @TerminationPolicySet.setter
    def TerminationPolicySet(self, TerminationPolicySet):
        self._TerminationPolicySet = TerminationPolicySet

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ZoneSet(self):
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet

    @property
    def RetryPolicy(self):
        return self._RetryPolicy

    @RetryPolicy.setter
    def RetryPolicy(self, RetryPolicy):
        self._RetryPolicy = RetryPolicy

    @property
    def InActivityStatus(self):
        return self._InActivityStatus

    @InActivityStatus.setter
    def InActivityStatus(self, InActivityStatus):
        self._InActivityStatus = InActivityStatus

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ServiceSettings(self):
        return self._ServiceSettings

    @ServiceSettings.setter
    def ServiceSettings(self, ServiceSettings):
        self._ServiceSettings = ServiceSettings

    @property
    def Ipv6AddressCount(self):
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount

    @property
    def MultiZoneSubnetPolicy(self):
        return self._MultiZoneSubnetPolicy

    @MultiZoneSubnetPolicy.setter
    def MultiZoneSubnetPolicy(self, MultiZoneSubnetPolicy):
        self._MultiZoneSubnetPolicy = MultiZoneSubnetPolicy

    @property
    def HealthCheckType(self):
        return self._HealthCheckType

    @HealthCheckType.setter
    def HealthCheckType(self, HealthCheckType):
        self._HealthCheckType = HealthCheckType

    @property
    def LoadBalancerHealthCheckGracePeriod(self):
        return self._LoadBalancerHealthCheckGracePeriod

    @LoadBalancerHealthCheckGracePeriod.setter
    def LoadBalancerHealthCheckGracePeriod(self, LoadBalancerHealthCheckGracePeriod):
        self._LoadBalancerHealthCheckGracePeriod = LoadBalancerHealthCheckGracePeriod

    @property
    def InstanceAllocationPolicy(self):
        return self._InstanceAllocationPolicy

    @InstanceAllocationPolicy.setter
    def InstanceAllocationPolicy(self, InstanceAllocationPolicy):
        self._InstanceAllocationPolicy = InstanceAllocationPolicy

    @property
    def SpotMixedAllocationPolicy(self):
        return self._SpotMixedAllocationPolicy

    @SpotMixedAllocationPolicy.setter
    def SpotMixedAllocationPolicy(self, SpotMixedAllocationPolicy):
        self._SpotMixedAllocationPolicy = SpotMixedAllocationPolicy

    @property
    def CapacityRebalance(self):
        return self._CapacityRebalance

    @CapacityRebalance.setter
    def CapacityRebalance(self, CapacityRebalance):
        self._CapacityRebalance = CapacityRebalance


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._AutoScalingGroupName = params.get("AutoScalingGroupName")
        self._AutoScalingGroupStatus = params.get("AutoScalingGroupStatus")
        self._CreatedTime = params.get("CreatedTime")
        self._DefaultCooldown = params.get("DefaultCooldown")
        self._DesiredCapacity = params.get("DesiredCapacity")
        self._EnabledStatus = params.get("EnabledStatus")
        if params.get("ForwardLoadBalancerSet") is not None:
            self._ForwardLoadBalancerSet = []
            for item in params.get("ForwardLoadBalancerSet"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self._ForwardLoadBalancerSet.append(obj)
        self._InstanceCount = params.get("InstanceCount")
        self._InServiceInstanceCount = params.get("InServiceInstanceCount")
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._LaunchConfigurationName = params.get("LaunchConfigurationName")
        self._LoadBalancerIdSet = params.get("LoadBalancerIdSet")
        self._MaxSize = params.get("MaxSize")
        self._MinSize = params.get("MinSize")
        self._ProjectId = params.get("ProjectId")
        self._SubnetIdSet = params.get("SubnetIdSet")
        self._TerminationPolicySet = params.get("TerminationPolicySet")
        self._VpcId = params.get("VpcId")
        self._ZoneSet = params.get("ZoneSet")
        self._RetryPolicy = params.get("RetryPolicy")
        self._InActivityStatus = params.get("InActivityStatus")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("ServiceSettings") is not None:
            self._ServiceSettings = ServiceSettings()
            self._ServiceSettings._deserialize(params.get("ServiceSettings"))
        self._Ipv6AddressCount = params.get("Ipv6AddressCount")
        self._MultiZoneSubnetPolicy = params.get("MultiZoneSubnetPolicy")
        self._HealthCheckType = params.get("HealthCheckType")
        self._LoadBalancerHealthCheckGracePeriod = params.get("LoadBalancerHealthCheckGracePeriod")
        self._InstanceAllocationPolicy = params.get("InstanceAllocationPolicy")
        if params.get("SpotMixedAllocationPolicy") is not None:
            self._SpotMixedAllocationPolicy = SpotMixedAllocationPolicy()
            self._SpotMixedAllocationPolicy._deserialize(params.get("SpotMixedAllocationPolicy"))
        self._CapacityRebalance = params.get("CapacityRebalance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScalingGroupAbstract(AbstractModel):
    """伸缩组简明信息。

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID。
        :type AutoScalingGroupId: str
        :param _AutoScalingGroupName: 伸缩组名称。
        :type AutoScalingGroupName: str
        """
        self._AutoScalingGroupId = None
        self._AutoScalingGroupName = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def AutoScalingGroupName(self):
        return self._AutoScalingGroupName

    @AutoScalingGroupName.setter
    def AutoScalingGroupName(self, AutoScalingGroupName):
        self._AutoScalingGroupName = AutoScalingGroupName


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._AutoScalingGroupName = params.get("AutoScalingGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScalingNotification(AbstractModel):
    """弹性伸缩事件通知

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID。
        :type AutoScalingGroupId: str
        :param _NotificationUserGroupIds: 用户组ID列表。
        :type NotificationUserGroupIds: list of str
        :param _NotificationTypes: 通知事件列表。
        :type NotificationTypes: list of str
        :param _AutoScalingNotificationId: 事件通知ID。
        :type AutoScalingNotificationId: str
        :param _TargetType: 通知接收端类型。
        :type TargetType: str
        :param _QueueName: CMQ 队列名。
        :type QueueName: str
        :param _TopicName: CMQ 主题名。
        :type TopicName: str
        """
        self._AutoScalingGroupId = None
        self._NotificationUserGroupIds = None
        self._NotificationTypes = None
        self._AutoScalingNotificationId = None
        self._TargetType = None
        self._QueueName = None
        self._TopicName = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def NotificationUserGroupIds(self):
        return self._NotificationUserGroupIds

    @NotificationUserGroupIds.setter
    def NotificationUserGroupIds(self, NotificationUserGroupIds):
        self._NotificationUserGroupIds = NotificationUserGroupIds

    @property
    def NotificationTypes(self):
        return self._NotificationTypes

    @NotificationTypes.setter
    def NotificationTypes(self, NotificationTypes):
        self._NotificationTypes = NotificationTypes

    @property
    def AutoScalingNotificationId(self):
        return self._AutoScalingNotificationId

    @AutoScalingNotificationId.setter
    def AutoScalingNotificationId(self, AutoScalingNotificationId):
        self._AutoScalingNotificationId = AutoScalingNotificationId

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._NotificationUserGroupIds = params.get("NotificationUserGroupIds")
        self._NotificationTypes = params.get("NotificationTypes")
        self._AutoScalingNotificationId = params.get("AutoScalingNotificationId")
        self._TargetType = params.get("TargetType")
        self._QueueName = params.get("QueueName")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelInstanceRefreshRequest(AbstractModel):
    """CancelInstanceRefresh请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID。
        :type AutoScalingGroupId: str
        :param _RefreshActivityId: 刷新活动ID。
        :type RefreshActivityId: str
        """
        self._AutoScalingGroupId = None
        self._RefreshActivityId = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RefreshActivityId(self):
        return self._RefreshActivityId

    @RefreshActivityId.setter
    def RefreshActivityId(self, RefreshActivityId):
        self._RefreshActivityId = RefreshActivityId


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._RefreshActivityId = params.get("RefreshActivityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelInstanceRefreshResponse(AbstractModel):
    """CancelInstanceRefresh返回参数结构体

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


class ClearLaunchConfigurationAttributesRequest(AbstractModel):
    """ClearLaunchConfigurationAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LaunchConfigurationId: 启动配置ID。
        :type LaunchConfigurationId: str
        :param _ClearDataDisks: 是否清空数据盘信息，非必填，默认为 false。
填 true 代表清空“数据盘”信息，清空后基于此新创建的云主机将不含有任何数据盘。
        :type ClearDataDisks: bool
        :param _ClearHostNameSettings: 是否清空云服务器主机名相关设置信息，非必填，默认为 false。
填 true 代表清空主机名设置信息，清空后基于此新创建的云主机将不设置主机名。
        :type ClearHostNameSettings: bool
        :param _ClearInstanceNameSettings: 是否清空云服务器实例名相关设置信息，非必填，默认为 false。
填 true 代表清空主机名设置信息，清空后基于此新创建的云主机将按照“as-{{ 伸缩组AutoScalingGroupName }}”进行设置。
        :type ClearInstanceNameSettings: bool
        :param _ClearDisasterRecoverGroupIds: 是否清空置放群组信息，非必填，默认为 false。
填 true 代表清空置放群组信息，清空后基于此新创建的云主机将不指定任何置放群组。
        :type ClearDisasterRecoverGroupIds: bool
        """
        self._LaunchConfigurationId = None
        self._ClearDataDisks = None
        self._ClearHostNameSettings = None
        self._ClearInstanceNameSettings = None
        self._ClearDisasterRecoverGroupIds = None

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def ClearDataDisks(self):
        return self._ClearDataDisks

    @ClearDataDisks.setter
    def ClearDataDisks(self, ClearDataDisks):
        self._ClearDataDisks = ClearDataDisks

    @property
    def ClearHostNameSettings(self):
        return self._ClearHostNameSettings

    @ClearHostNameSettings.setter
    def ClearHostNameSettings(self, ClearHostNameSettings):
        self._ClearHostNameSettings = ClearHostNameSettings

    @property
    def ClearInstanceNameSettings(self):
        return self._ClearInstanceNameSettings

    @ClearInstanceNameSettings.setter
    def ClearInstanceNameSettings(self, ClearInstanceNameSettings):
        self._ClearInstanceNameSettings = ClearInstanceNameSettings

    @property
    def ClearDisasterRecoverGroupIds(self):
        return self._ClearDisasterRecoverGroupIds

    @ClearDisasterRecoverGroupIds.setter
    def ClearDisasterRecoverGroupIds(self, ClearDisasterRecoverGroupIds):
        self._ClearDisasterRecoverGroupIds = ClearDisasterRecoverGroupIds


    def _deserialize(self, params):
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._ClearDataDisks = params.get("ClearDataDisks")
        self._ClearHostNameSettings = params.get("ClearHostNameSettings")
        self._ClearInstanceNameSettings = params.get("ClearInstanceNameSettings")
        self._ClearDisasterRecoverGroupIds = params.get("ClearDisasterRecoverGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearLaunchConfigurationAttributesResponse(AbstractModel):
    """ClearLaunchConfigurationAttributes返回参数结构体

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


class CompleteLifecycleActionRequest(AbstractModel):
    """CompleteLifecycleAction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LifecycleHookId: 生命周期挂钩ID
        :type LifecycleHookId: str
        :param _LifecycleActionResult: 生命周期动作的结果，取值范围为“CONTINUE”或“ABANDON”
        :type LifecycleActionResult: str
        :param _InstanceId: 实例ID，“InstanceId”和“LifecycleActionToken”必须填充其中一个
        :type InstanceId: str
        :param _LifecycleActionToken: “InstanceId”和“LifecycleActionToken”必须填充其中一个
        :type LifecycleActionToken: str
        """
        self._LifecycleHookId = None
        self._LifecycleActionResult = None
        self._InstanceId = None
        self._LifecycleActionToken = None

    @property
    def LifecycleHookId(self):
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def LifecycleActionResult(self):
        return self._LifecycleActionResult

    @LifecycleActionResult.setter
    def LifecycleActionResult(self, LifecycleActionResult):
        self._LifecycleActionResult = LifecycleActionResult

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LifecycleActionToken(self):
        return self._LifecycleActionToken

    @LifecycleActionToken.setter
    def LifecycleActionToken(self, LifecycleActionToken):
        self._LifecycleActionToken = LifecycleActionToken


    def _deserialize(self, params):
        self._LifecycleHookId = params.get("LifecycleHookId")
        self._LifecycleActionResult = params.get("LifecycleActionResult")
        self._InstanceId = params.get("InstanceId")
        self._LifecycleActionToken = params.get("LifecycleActionToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteLifecycleActionResponse(AbstractModel):
    """CompleteLifecycleAction返回参数结构体

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


class CreateAutoScalingGroupFromInstanceRequest(AbstractModel):
    """CreateAutoScalingGroupFromInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupName: 伸缩组名称，在您账号中必须唯一。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超55个字节。
        :type AutoScalingGroupName: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _MinSize: 最小实例数，取值范围为0-2000。
        :type MinSize: int
        :param _MaxSize: 最大实例数，取值范围为0-2000。
        :type MaxSize: int
        :param _DesiredCapacity: 期望实例数，大小介于最小实例数和最大实例数之间。
        :type DesiredCapacity: int
        :param _InheritInstanceTag: 是否继承实例标签，默认值为False
        :type InheritInstanceTag: bool
        """
        self._AutoScalingGroupName = None
        self._InstanceId = None
        self._MinSize = None
        self._MaxSize = None
        self._DesiredCapacity = None
        self._InheritInstanceTag = None

    @property
    def AutoScalingGroupName(self):
        return self._AutoScalingGroupName

    @AutoScalingGroupName.setter
    def AutoScalingGroupName(self, AutoScalingGroupName):
        self._AutoScalingGroupName = AutoScalingGroupName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def DesiredCapacity(self):
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def InheritInstanceTag(self):
        return self._InheritInstanceTag

    @InheritInstanceTag.setter
    def InheritInstanceTag(self, InheritInstanceTag):
        self._InheritInstanceTag = InheritInstanceTag


    def _deserialize(self, params):
        self._AutoScalingGroupName = params.get("AutoScalingGroupName")
        self._InstanceId = params.get("InstanceId")
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        self._DesiredCapacity = params.get("DesiredCapacity")
        self._InheritInstanceTag = params.get("InheritInstanceTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoScalingGroupFromInstanceResponse(AbstractModel):
    """CreateAutoScalingGroupFromInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoScalingGroupId = None
        self._RequestId = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._RequestId = params.get("RequestId")


class CreateAutoScalingGroupRequest(AbstractModel):
    """CreateAutoScalingGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupName: 伸缩组名称，在您账号中必须唯一。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超55个字节。
        :type AutoScalingGroupName: str
        :param _LaunchConfigurationId: 启动配置ID
        :type LaunchConfigurationId: str
        :param _MaxSize: 最大实例数，取值范围为0-2000。
        :type MaxSize: int
        :param _MinSize: 最小实例数，取值范围为0-2000。
        :type MinSize: int
        :param _VpcId: VPC ID，基础网络则填空字符串
        :type VpcId: str
        :param _DefaultCooldown: 默认冷却时间，单位秒，默认值为300
        :type DefaultCooldown: int
        :param _DesiredCapacity: 期望实例数，大小介于最小实例数和最大实例数之间
        :type DesiredCapacity: int
        :param _LoadBalancerIds: 传统负载均衡器ID列表，目前长度上限为20，LoadBalancerIds 和 ForwardLoadBalancers 二者同时最多只能指定一个
        :type LoadBalancerIds: list of str
        :param _ProjectId: 伸缩组内实例所属项目ID。不填为默认项目。
        :type ProjectId: int
        :param _ForwardLoadBalancers: 应用型负载均衡器列表，目前长度上限为100，LoadBalancerIds 和 ForwardLoadBalancers 二者同时最多只能指定一个
        :type ForwardLoadBalancers: list of ForwardLoadBalancer
        :param _SubnetIds: 子网ID列表，VPC场景下必须指定子网。多个子网以填写顺序为优先级，依次进行尝试，直至可以成功创建实例。
        :type SubnetIds: list of str
        :param _TerminationPolicies: 销毁策略，目前长度上限为1。取值包括 OLDEST_INSTANCE 和 NEWEST_INSTANCE，默认取值为 OLDEST_INSTANCE。
<br><li> OLDEST_INSTANCE 优先销毁伸缩组中最旧的实例。
<br><li> NEWEST_INSTANCE，优先销毁伸缩组中最新的实例。
        :type TerminationPolicies: list of str
        :param _Zones: 可用区列表，基础网络场景下必须指定可用区。多个可用区以填写顺序为优先级，依次进行尝试，直至可以成功创建实例。
        :type Zones: list of str
        :param _RetryPolicy: 重试策略，取值包括 IMMEDIATE_RETRY、 INCREMENTAL_INTERVALS、NO_RETRY，默认取值为 IMMEDIATE_RETRY。部分成功的伸缩活动判定为一次失败活动。
<br><li> IMMEDIATE_RETRY，立即重试，在较短时间内快速重试，连续失败超过一定次数（5次）后不再重试。
<br><li> INCREMENTAL_INTERVALS，间隔递增重试，随着连续失败次数的增加，重试间隔逐渐增大，重试间隔从秒级到1天不等。
<br><li> NO_RETRY，不进行重试，直到再次收到用户调用或者告警信息后才会重试。
        :type RetryPolicy: str
        :param _ZonesCheckPolicy: 可用区校验策略，取值包括 ALL 和 ANY，默认取值为ANY。
<br><li> ALL，所有可用区（Zone）或子网（SubnetId）都可用则通过校验，否则校验报错。
<br><li> ANY，存在任何一个可用区（Zone）或子网（SubnetId）可用则通过校验，否则校验报错。

可用区或子网不可用的常见原因包括该可用区CVM实例类型售罄、该可用区CBS云盘售罄、该可用区配额不足、该子网IP不足等。
如果 Zones/SubnetIds 中可用区或者子网不存在，则无论 ZonesCheckPolicy 采用何种取值，都会校验报错。
        :type ZonesCheckPolicy: str
        :param _Tags: 标签描述列表。通过指定该参数可以支持绑定标签到伸缩组。同时绑定标签到相应的资源实例。每个伸缩组最多支持30个标签。
        :type Tags: list of Tag
        :param _ServiceSettings: 服务设置，包括云监控不健康替换等服务设置。
        :type ServiceSettings: :class:`tencentcloud.autoscaling.v20180419.models.ServiceSettings`
        :param _Ipv6AddressCount: 实例具有IPv6地址数量的配置，取值包括 0、1，默认值为0。
        :type Ipv6AddressCount: int
        :param _MultiZoneSubnetPolicy: 多可用区/子网策略，取值包括 PRIORITY 和 EQUALITY，默认为 PRIORITY。
<br><li> PRIORITY，按照可用区/子网列表的顺序，作为优先级来尝试创建实例，如果优先级最高的可用区/子网可以创建成功，则总在该可用区/子网创建。
<br><li> EQUALITY：扩容出的实例会打散到多个可用区/子网，保证扩容后的各个可用区/子网实例数相对均衡。

与本策略相关的注意点：
<br><li> 当伸缩组为基础网络时，本策略适用于多可用区；当伸缩组为VPC网络时，本策略适用于多子网，此时不再考虑可用区因素，例如四个子网ABCD，其中ABC处于可用区1，D处于可用区2，此时考虑子网ABCD进行排序，而不考虑可用区1、2。
<br><li> 本策略适用于多可用区/子网，不适用于启动配置的多机型。多机型按照优先级策略进行选择。
<br><li> 按照 PRIORITY 策略创建实例时，先保证多机型的策略，后保证多可用区/子网的策略。例如多机型A、B，多子网1、2、3，会按照A1、A2、A3、B1、B2、B3 进行尝试，如果A1售罄，会尝试A2（而非B1）。
        :type MultiZoneSubnetPolicy: str
        :param _HealthCheckType: 伸缩组实例健康检查类型，取值如下：<br><li>CVM：根据实例网络状态判断实例是否处于不健康状态，不健康的网络状态即发生实例 PING 不可达事件，详细判断标准可参考[实例健康检查](https://cloud.tencent.com/document/product/377/8553)<br><li>CLB：根据 CLB 的健康检查状态判断实例是否处于不健康状态，CLB健康检查原理可参考[健康检查](https://cloud.tencent.com/document/product/214/6097) <br>如果选择了`CLB`类型，伸缩组将同时检查实例网络状态与CLB健康检查状态，如果出现实例网络状态不健康，实例将被标记为 UNHEALTHY 状态；如果出现 CLB 健康检查状态异常，实例将被标记为CLB_UNHEALTHY 状态，如果两个异常状态同时出现，实例`HealthStatus`字段将返回 UNHEALTHY|CLB_UNHEALTHY。默认值：CLB
        :type HealthCheckType: str
        :param _LoadBalancerHealthCheckGracePeriod: CLB健康检查宽限期，当扩容的实例进入`IN_SERVICE`后，在宽限期时间范围内将不会被标记为不健康`CLB_UNHEALTHY`。<br>默认值：0。取值范围[0, 7200]，单位：秒。
        :type LoadBalancerHealthCheckGracePeriod: int
        :param _InstanceAllocationPolicy: 实例分配策略，取值包括 LAUNCH_CONFIGURATION 和 SPOT_MIXED，默认取 LAUNCH_CONFIGURATION。
<br><li> LAUNCH_CONFIGURATION，代表传统的按照启动配置模式。
<br><li> SPOT_MIXED，代表竞价混合模式。目前仅支持启动配置为按量计费模式时使用混合模式，混合模式下，伸缩组将根据设定扩容按量或竞价机型。使用混合模式时，关联的启动配置的计费类型不可被修改。
        :type InstanceAllocationPolicy: str
        :param _SpotMixedAllocationPolicy: 竞价混合模式下，各计费类型实例的分配策略。
仅当 InstanceAllocationPolicy 取 SPOT_MIXED 时可用。
        :type SpotMixedAllocationPolicy: :class:`tencentcloud.autoscaling.v20180419.models.SpotMixedAllocationPolicy`
        :param _CapacityRebalance: 容量重平衡功能，仅对伸缩组内的竞价实例有效。取值范围：
<br><li> TRUE，开启该功能，当伸缩组内的竞价实例即将被竞价实例服务自动回收前，AS 主动发起竞价实例销毁流程，如果有配置过缩容 hook，则销毁前 hook 会生效。销毁流程启动后，AS 会异步开启一个扩容活动，用于补齐期望实例数。
<br><li> FALSE，不开启该功能，则 AS 等待竞价实例被销毁后才会去扩容补齐伸缩组期望实例数。

默认取 FALSE。
        :type CapacityRebalance: bool
        """
        self._AutoScalingGroupName = None
        self._LaunchConfigurationId = None
        self._MaxSize = None
        self._MinSize = None
        self._VpcId = None
        self._DefaultCooldown = None
        self._DesiredCapacity = None
        self._LoadBalancerIds = None
        self._ProjectId = None
        self._ForwardLoadBalancers = None
        self._SubnetIds = None
        self._TerminationPolicies = None
        self._Zones = None
        self._RetryPolicy = None
        self._ZonesCheckPolicy = None
        self._Tags = None
        self._ServiceSettings = None
        self._Ipv6AddressCount = None
        self._MultiZoneSubnetPolicy = None
        self._HealthCheckType = None
        self._LoadBalancerHealthCheckGracePeriod = None
        self._InstanceAllocationPolicy = None
        self._SpotMixedAllocationPolicy = None
        self._CapacityRebalance = None

    @property
    def AutoScalingGroupName(self):
        return self._AutoScalingGroupName

    @AutoScalingGroupName.setter
    def AutoScalingGroupName(self, AutoScalingGroupName):
        self._AutoScalingGroupName = AutoScalingGroupName

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def DefaultCooldown(self):
        return self._DefaultCooldown

    @DefaultCooldown.setter
    def DefaultCooldown(self, DefaultCooldown):
        self._DefaultCooldown = DefaultCooldown

    @property
    def DesiredCapacity(self):
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ForwardLoadBalancers(self):
        return self._ForwardLoadBalancers

    @ForwardLoadBalancers.setter
    def ForwardLoadBalancers(self, ForwardLoadBalancers):
        self._ForwardLoadBalancers = ForwardLoadBalancers

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def TerminationPolicies(self):
        return self._TerminationPolicies

    @TerminationPolicies.setter
    def TerminationPolicies(self, TerminationPolicies):
        self._TerminationPolicies = TerminationPolicies

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RetryPolicy(self):
        return self._RetryPolicy

    @RetryPolicy.setter
    def RetryPolicy(self, RetryPolicy):
        self._RetryPolicy = RetryPolicy

    @property
    def ZonesCheckPolicy(self):
        return self._ZonesCheckPolicy

    @ZonesCheckPolicy.setter
    def ZonesCheckPolicy(self, ZonesCheckPolicy):
        self._ZonesCheckPolicy = ZonesCheckPolicy

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ServiceSettings(self):
        return self._ServiceSettings

    @ServiceSettings.setter
    def ServiceSettings(self, ServiceSettings):
        self._ServiceSettings = ServiceSettings

    @property
    def Ipv6AddressCount(self):
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount

    @property
    def MultiZoneSubnetPolicy(self):
        return self._MultiZoneSubnetPolicy

    @MultiZoneSubnetPolicy.setter
    def MultiZoneSubnetPolicy(self, MultiZoneSubnetPolicy):
        self._MultiZoneSubnetPolicy = MultiZoneSubnetPolicy

    @property
    def HealthCheckType(self):
        return self._HealthCheckType

    @HealthCheckType.setter
    def HealthCheckType(self, HealthCheckType):
        self._HealthCheckType = HealthCheckType

    @property
    def LoadBalancerHealthCheckGracePeriod(self):
        return self._LoadBalancerHealthCheckGracePeriod

    @LoadBalancerHealthCheckGracePeriod.setter
    def LoadBalancerHealthCheckGracePeriod(self, LoadBalancerHealthCheckGracePeriod):
        self._LoadBalancerHealthCheckGracePeriod = LoadBalancerHealthCheckGracePeriod

    @property
    def InstanceAllocationPolicy(self):
        return self._InstanceAllocationPolicy

    @InstanceAllocationPolicy.setter
    def InstanceAllocationPolicy(self, InstanceAllocationPolicy):
        self._InstanceAllocationPolicy = InstanceAllocationPolicy

    @property
    def SpotMixedAllocationPolicy(self):
        return self._SpotMixedAllocationPolicy

    @SpotMixedAllocationPolicy.setter
    def SpotMixedAllocationPolicy(self, SpotMixedAllocationPolicy):
        self._SpotMixedAllocationPolicy = SpotMixedAllocationPolicy

    @property
    def CapacityRebalance(self):
        return self._CapacityRebalance

    @CapacityRebalance.setter
    def CapacityRebalance(self, CapacityRebalance):
        self._CapacityRebalance = CapacityRebalance


    def _deserialize(self, params):
        self._AutoScalingGroupName = params.get("AutoScalingGroupName")
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._MaxSize = params.get("MaxSize")
        self._MinSize = params.get("MinSize")
        self._VpcId = params.get("VpcId")
        self._DefaultCooldown = params.get("DefaultCooldown")
        self._DesiredCapacity = params.get("DesiredCapacity")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._ProjectId = params.get("ProjectId")
        if params.get("ForwardLoadBalancers") is not None:
            self._ForwardLoadBalancers = []
            for item in params.get("ForwardLoadBalancers"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self._ForwardLoadBalancers.append(obj)
        self._SubnetIds = params.get("SubnetIds")
        self._TerminationPolicies = params.get("TerminationPolicies")
        self._Zones = params.get("Zones")
        self._RetryPolicy = params.get("RetryPolicy")
        self._ZonesCheckPolicy = params.get("ZonesCheckPolicy")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("ServiceSettings") is not None:
            self._ServiceSettings = ServiceSettings()
            self._ServiceSettings._deserialize(params.get("ServiceSettings"))
        self._Ipv6AddressCount = params.get("Ipv6AddressCount")
        self._MultiZoneSubnetPolicy = params.get("MultiZoneSubnetPolicy")
        self._HealthCheckType = params.get("HealthCheckType")
        self._LoadBalancerHealthCheckGracePeriod = params.get("LoadBalancerHealthCheckGracePeriod")
        self._InstanceAllocationPolicy = params.get("InstanceAllocationPolicy")
        if params.get("SpotMixedAllocationPolicy") is not None:
            self._SpotMixedAllocationPolicy = SpotMixedAllocationPolicy()
            self._SpotMixedAllocationPolicy._deserialize(params.get("SpotMixedAllocationPolicy"))
        self._CapacityRebalance = params.get("CapacityRebalance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoScalingGroupResponse(AbstractModel):
    """CreateAutoScalingGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoScalingGroupId = None
        self._RequestId = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._RequestId = params.get("RequestId")


class CreateLaunchConfigurationRequest(AbstractModel):
    """CreateLaunchConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LaunchConfigurationName: 启动配置显示名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。
        :type LaunchConfigurationName: str
        :param _ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-8toqc6s3`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，取返回信息中的`ImageId`字段。</li>
        :type ImageId: str
        :param _ProjectId: 启动配置所属项目ID。不填为默认项目。
注意：伸缩组内实例所属项目ID取伸缩组项目ID，与这里取值无关。
        :type ProjectId: int
        :param _InstanceType: 实例机型。不同实例机型指定了不同的资源规格，具体取值可通过调用接口 [DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749) 来获得最新的规格表或参见[实例类型](https://cloud.tencent.com/document/product/213/11518)描述。
`InstanceType`和`InstanceTypes`参数互斥，二者必填一个且只能填写一个。
        :type InstanceType: str
        :param _SystemDisk: 实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.autoscaling.v20180419.models.SystemDisk`
        :param _DataDisks: 实例数据盘配置信息。若不指定该参数，则默认不购买数据盘，最多支持指定11块数据盘。
        :type DataDisks: list of DataDisk
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        :param _LoginSettings: 实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。
        :type LoginSettings: :class:`tencentcloud.autoscaling.v20180419.models.LoginSettings`
        :param _SecurityGroupIds: 实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的`SecurityGroupId`字段来获取。若不指定该参数，则默认不绑定安全组。
        :type SecurityGroupIds: list of str
        :param _EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。
        :type EnhancedService: :class:`tencentcloud.autoscaling.v20180419.models.EnhancedService`
        :param _UserData: 经过 Base64 编码后的自定义数据，最大长度不超过16KB。
        :type UserData: str
        :param _InstanceChargeType: 实例计费类型，CVM默认值按照POSTPAID_BY_HOUR处理。
<br><li>POSTPAID_BY_HOUR：按小时后付费
<br><li>SPOTPAID：竞价付费
<br><li>PREPAID：预付费，即包年包月
        :type InstanceChargeType: str
        :param _InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数，若指定实例的付费模式为竞价付费则该参数必传。
        :type InstanceMarketOptions: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        :param _InstanceTypes: 实例机型列表，不同实例机型指定了不同的资源规格，最多支持10种实例机型。
`InstanceType`和`InstanceTypes`参数互斥，二者必填一个且只能填写一个。
        :type InstanceTypes: list of str
        :param _CamRoleName: CAM角色名称。可通过DescribeRoleList接口返回值中的roleName获取。
        :type CamRoleName: str
        :param _InstanceTypesCheckPolicy: 实例类型校验策略，取值包括 ALL 和 ANY，默认取值为ANY。
<br><li> ALL，所有实例类型（InstanceType）都可用则通过校验，否则校验报错。
<br><li> ANY，存在任何一个实例类型（InstanceType）可用则通过校验，否则校验报错。

实例类型不可用的常见原因包括该实例类型售罄、对应云盘售罄等。
如果 InstanceTypes 中一款机型不存在或者已下线，则无论 InstanceTypesCheckPolicy 采用何种取值，都会校验报错。
        :type InstanceTypesCheckPolicy: str
        :param _InstanceTags: 标签列表。通过指定该参数，可以为扩容的实例绑定标签。最多支持指定10个标签。
        :type InstanceTags: list of InstanceTag
        :param _Tags: 标签描述列表。通过指定该参数可以支持绑定标签到启动配置。每个启动配置最多支持30个标签。
        :type Tags: list of Tag
        :param _HostNameSettings: 云服务器主机名（HostName）的相关设置。
        :type HostNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.HostNameSettings`
        :param _InstanceNameSettings: 云服务器实例名（InstanceName）的相关设置。
如果用户在启动配置中设置此字段，则伸缩组创建出的实例 InstanceName 参照此字段进行设置，并传递给 CVM；如果用户未在启动配置中设置此字段，则伸缩组创建出的实例 InstanceName 按照“as-{{ 伸缩组AutoScalingGroupName }}”进行设置，并传递给 CVM。
        :type InstanceNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameSettings`
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.autoscaling.v20180419.models.InstanceChargePrepaid`
        :param _DiskTypePolicy: 云盘类型选择策略，默认取值 ORIGINAL，取值范围：
<br><li>ORIGINAL：使用设置的云盘类型
<br><li>AUTOMATIC：自动选择当前可用的云盘类型
        :type DiskTypePolicy: str
        :param _HpcClusterId: 高性能计算集群ID。<br>
注意：此字段默认为空。
        :type HpcClusterId: str
        :param _IPv6InternetAccessible: IPv6公网带宽相关信息设置。若新建实例包含IPv6地址，该参数可为新建实例的IPv6地址分配公网带宽。关联启动配置的伸缩组Ipv6AddressCount参数为0时，该参数不会生效。
        :type IPv6InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.IPv6InternetAccessible`
        :param _DisasterRecoverGroupIds: 置放群组id，仅支持指定一个。
        :type DisasterRecoverGroupIds: list of str
        """
        self._LaunchConfigurationName = None
        self._ImageId = None
        self._ProjectId = None
        self._InstanceType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._InternetAccessible = None
        self._LoginSettings = None
        self._SecurityGroupIds = None
        self._EnhancedService = None
        self._UserData = None
        self._InstanceChargeType = None
        self._InstanceMarketOptions = None
        self._InstanceTypes = None
        self._CamRoleName = None
        self._InstanceTypesCheckPolicy = None
        self._InstanceTags = None
        self._Tags = None
        self._HostNameSettings = None
        self._InstanceNameSettings = None
        self._InstanceChargePrepaid = None
        self._DiskTypePolicy = None
        self._HpcClusterId = None
        self._IPv6InternetAccessible = None
        self._DisasterRecoverGroupIds = None

    @property
    def LaunchConfigurationName(self):
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def InstanceTypesCheckPolicy(self):
        return self._InstanceTypesCheckPolicy

    @InstanceTypesCheckPolicy.setter
    def InstanceTypesCheckPolicy(self, InstanceTypesCheckPolicy):
        self._InstanceTypesCheckPolicy = InstanceTypesCheckPolicy

    @property
    def InstanceTags(self):
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HostNameSettings(self):
        return self._HostNameSettings

    @HostNameSettings.setter
    def HostNameSettings(self, HostNameSettings):
        self._HostNameSettings = HostNameSettings

    @property
    def InstanceNameSettings(self):
        return self._InstanceNameSettings

    @InstanceNameSettings.setter
    def InstanceNameSettings(self, InstanceNameSettings):
        self._InstanceNameSettings = InstanceNameSettings

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def DiskTypePolicy(self):
        return self._DiskTypePolicy

    @DiskTypePolicy.setter
    def DiskTypePolicy(self, DiskTypePolicy):
        self._DiskTypePolicy = DiskTypePolicy

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def IPv6InternetAccessible(self):
        return self._IPv6InternetAccessible

    @IPv6InternetAccessible.setter
    def IPv6InternetAccessible(self, IPv6InternetAccessible):
        self._IPv6InternetAccessible = IPv6InternetAccessible

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds


    def _deserialize(self, params):
        self._LaunchConfigurationName = params.get("LaunchConfigurationName")
        self._ImageId = params.get("ImageId")
        self._ProjectId = params.get("ProjectId")
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
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._UserData = params.get("UserData")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._InstanceTypes = params.get("InstanceTypes")
        self._CamRoleName = params.get("CamRoleName")
        self._InstanceTypesCheckPolicy = params.get("InstanceTypesCheckPolicy")
        if params.get("InstanceTags") is not None:
            self._InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTag()
                obj._deserialize(item)
                self._InstanceTags.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("HostNameSettings") is not None:
            self._HostNameSettings = HostNameSettings()
            self._HostNameSettings._deserialize(params.get("HostNameSettings"))
        if params.get("InstanceNameSettings") is not None:
            self._InstanceNameSettings = InstanceNameSettings()
            self._InstanceNameSettings._deserialize(params.get("InstanceNameSettings"))
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._DiskTypePolicy = params.get("DiskTypePolicy")
        self._HpcClusterId = params.get("HpcClusterId")
        if params.get("IPv6InternetAccessible") is not None:
            self._IPv6InternetAccessible = IPv6InternetAccessible()
            self._IPv6InternetAccessible._deserialize(params.get("IPv6InternetAccessible"))
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLaunchConfigurationResponse(AbstractModel):
    """CreateLaunchConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LaunchConfigurationId: 当通过本接口来创建启动配置时会返回该参数，表示启动配置ID。
        :type LaunchConfigurationId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LaunchConfigurationId = None
        self._RequestId = None

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._RequestId = params.get("RequestId")


class CreateLifecycleHookRequest(AbstractModel):
    """CreateLifecycleHook请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _LifecycleHookName: 生命周期挂钩名称。名称仅支持中文、英文、数字、下划线（_）、短横线（-）、小数点（.），最大长度不能超128个字节。
        :type LifecycleHookName: str
        :param _LifecycleTransition: 进行生命周期挂钩的场景，取值范围包括 INSTANCE_LAUNCHING 和 INSTANCE_TERMINATING
        :type LifecycleTransition: str
        :param _DefaultResult: 定义伸缩组在生命周期挂钩超时的情况下应采取的操作，取值范围是 CONTINUE 或 ABANDON，默认值为 CONTINUE
        :type DefaultResult: str
        :param _HeartbeatTimeout: 生命周期挂钩超时之前可以经过的最长时间（以秒为单位），范围从30到7200秒，默认值为300秒
        :type HeartbeatTimeout: int
        :param _NotificationMetadata: 弹性伸缩向通知目标发送的附加信息，配置通知时使用,默认值为空字符串""。最大长度不能超过1024个字节。
        :type NotificationMetadata: str
        :param _NotificationTarget: 通知目标。NotificationTarget和LifecycleCommand参数互斥，二者不可同时指定。
        :type NotificationTarget: :class:`tencentcloud.autoscaling.v20180419.models.NotificationTarget`
        :param _LifecycleTransitionType: 进行生命周期挂钩的场景类型，取值范围包括NORMAL 和 EXTENSION。说明：设置为EXTENSION值，在AttachInstances、DetachInstances、RemoveInstaces接口时会触发生命周期挂钩操作，值为NORMAL则不会在这些接口中触发生命周期挂钩。
        :type LifecycleTransitionType: str
        :param _LifecycleCommand: 远程命令执行对象。NotificationTarget和LifecycleCommand参数互斥，二者不可同时指定。
        :type LifecycleCommand: :class:`tencentcloud.autoscaling.v20180419.models.LifecycleCommand`
        """
        self._AutoScalingGroupId = None
        self._LifecycleHookName = None
        self._LifecycleTransition = None
        self._DefaultResult = None
        self._HeartbeatTimeout = None
        self._NotificationMetadata = None
        self._NotificationTarget = None
        self._LifecycleTransitionType = None
        self._LifecycleCommand = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def LifecycleHookName(self):
        return self._LifecycleHookName

    @LifecycleHookName.setter
    def LifecycleHookName(self, LifecycleHookName):
        self._LifecycleHookName = LifecycleHookName

    @property
    def LifecycleTransition(self):
        return self._LifecycleTransition

    @LifecycleTransition.setter
    def LifecycleTransition(self, LifecycleTransition):
        self._LifecycleTransition = LifecycleTransition

    @property
    def DefaultResult(self):
        return self._DefaultResult

    @DefaultResult.setter
    def DefaultResult(self, DefaultResult):
        self._DefaultResult = DefaultResult

    @property
    def HeartbeatTimeout(self):
        return self._HeartbeatTimeout

    @HeartbeatTimeout.setter
    def HeartbeatTimeout(self, HeartbeatTimeout):
        self._HeartbeatTimeout = HeartbeatTimeout

    @property
    def NotificationMetadata(self):
        return self._NotificationMetadata

    @NotificationMetadata.setter
    def NotificationMetadata(self, NotificationMetadata):
        self._NotificationMetadata = NotificationMetadata

    @property
    def NotificationTarget(self):
        return self._NotificationTarget

    @NotificationTarget.setter
    def NotificationTarget(self, NotificationTarget):
        self._NotificationTarget = NotificationTarget

    @property
    def LifecycleTransitionType(self):
        return self._LifecycleTransitionType

    @LifecycleTransitionType.setter
    def LifecycleTransitionType(self, LifecycleTransitionType):
        self._LifecycleTransitionType = LifecycleTransitionType

    @property
    def LifecycleCommand(self):
        return self._LifecycleCommand

    @LifecycleCommand.setter
    def LifecycleCommand(self, LifecycleCommand):
        self._LifecycleCommand = LifecycleCommand


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._LifecycleHookName = params.get("LifecycleHookName")
        self._LifecycleTransition = params.get("LifecycleTransition")
        self._DefaultResult = params.get("DefaultResult")
        self._HeartbeatTimeout = params.get("HeartbeatTimeout")
        self._NotificationMetadata = params.get("NotificationMetadata")
        if params.get("NotificationTarget") is not None:
            self._NotificationTarget = NotificationTarget()
            self._NotificationTarget._deserialize(params.get("NotificationTarget"))
        self._LifecycleTransitionType = params.get("LifecycleTransitionType")
        if params.get("LifecycleCommand") is not None:
            self._LifecycleCommand = LifecycleCommand()
            self._LifecycleCommand._deserialize(params.get("LifecycleCommand"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLifecycleHookResponse(AbstractModel):
    """CreateLifecycleHook返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LifecycleHookId: 生命周期挂钩ID
        :type LifecycleHookId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LifecycleHookId = None
        self._RequestId = None

    @property
    def LifecycleHookId(self):
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LifecycleHookId = params.get("LifecycleHookId")
        self._RequestId = params.get("RequestId")


class CreateNotificationConfigurationRequest(AbstractModel):
    """CreateNotificationConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID。
        :type AutoScalingGroupId: str
        :param _NotificationTypes: 通知类型，即为需要订阅的通知类型集合，取值范围如下：
<li>SCALE_OUT_SUCCESSFUL：扩容成功</li>
<li>SCALE_OUT_FAILED：扩容失败</li>
<li>SCALE_IN_SUCCESSFUL：缩容成功</li>
<li>SCALE_IN_FAILED：缩容失败</li>
<li>REPLACE_UNHEALTHY_INSTANCE_SUCCESSFUL：替换不健康子机成功</li>
<li>REPLACE_UNHEALTHY_INSTANCE_FAILED：替换不健康子机失败</li>
        :type NotificationTypes: list of str
        :param _NotificationUserGroupIds: 通知组ID，即为用户组ID集合，用户组ID可以通过[ListGroups](https://cloud.tencent.com/document/product/598/34589)查询。
        :type NotificationUserGroupIds: list of str
        :param _TargetType: 通知接收端类型，取值如下
<br><li>USER_GROUP：用户组
<br><li>CMQ_QUEUE：CMQ 队列
<br><li>CMQ_TOPIC：CMQ 主题
<br><li>TDMQ_CMQ_TOPIC：TDMQ CMQ 主题
<br><li>TDMQ_CMQ_QUEUE：TDMQ CMQ 队列

默认值为：`USER_GROUP`。
        :type TargetType: str
        :param _QueueName: CMQ 队列名称，如 TargetType 取值为 `CMQ_QUEUE` 或 `TDMQ_CMQ_QUEUE` 时，该字段必填。
        :type QueueName: str
        :param _TopicName: CMQ 主题名称，如 TargetType 取值为 `CMQ_TOPIC` 或 `TDMQ_CMQ_TOPIC` 时，该字段必填。
        :type TopicName: str
        """
        self._AutoScalingGroupId = None
        self._NotificationTypes = None
        self._NotificationUserGroupIds = None
        self._TargetType = None
        self._QueueName = None
        self._TopicName = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def NotificationTypes(self):
        return self._NotificationTypes

    @NotificationTypes.setter
    def NotificationTypes(self, NotificationTypes):
        self._NotificationTypes = NotificationTypes

    @property
    def NotificationUserGroupIds(self):
        return self._NotificationUserGroupIds

    @NotificationUserGroupIds.setter
    def NotificationUserGroupIds(self, NotificationUserGroupIds):
        self._NotificationUserGroupIds = NotificationUserGroupIds

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._NotificationTypes = params.get("NotificationTypes")
        self._NotificationUserGroupIds = params.get("NotificationUserGroupIds")
        self._TargetType = params.get("TargetType")
        self._QueueName = params.get("QueueName")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNotificationConfigurationResponse(AbstractModel):
    """CreateNotificationConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingNotificationId: 通知ID。
        :type AutoScalingNotificationId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoScalingNotificationId = None
        self._RequestId = None

    @property
    def AutoScalingNotificationId(self):
        return self._AutoScalingNotificationId

    @AutoScalingNotificationId.setter
    def AutoScalingNotificationId(self, AutoScalingNotificationId):
        self._AutoScalingNotificationId = AutoScalingNotificationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoScalingNotificationId = params.get("AutoScalingNotificationId")
        self._RequestId = params.get("RequestId")


class CreateScalingPolicyRequest(AbstractModel):
    """CreateScalingPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID。
        :type AutoScalingGroupId: str
        :param _ScalingPolicyName: 告警触发策略名称。
        :type ScalingPolicyName: str
        :param _ScalingPolicyType: 告警触发策略类型，默认类型为SIMPLE。取值范围：<br><li>SIMPLE：简单策略</li><li>TARGET_TRACKING：目标追踪策略</li>
        :type ScalingPolicyType: str
        :param _AdjustmentType: 告警触发后，期望实例数修改方式，仅适用于简单策略。取值范围：<br><li>CHANGE_IN_CAPACITY：增加或减少若干期望实例数</li><li>EXACT_CAPACITY：调整至指定期望实例数</li> <li>PERCENT_CHANGE_IN_CAPACITY：按百分比调整期望实例数</li>
        :type AdjustmentType: str
        :param _AdjustmentValue: 告警触发后，期望实例数的调整值，仅适用于简单策略。<br><li>当 AdjustmentType 为 CHANGE_IN_CAPACITY 时，AdjustmentValue 为正数表示告警触发后增加实例，为负数表示告警触发后减少实例 </li> <li> 当 AdjustmentType 为 EXACT_CAPACITY 时，AdjustmentValue 的值即为告警触发后新的期望实例数，需要大于或等于0 </li> <li> 当 AdjustmentType 为 PERCENT_CHANGE_IN_CAPACITY 时，AdjusmentValue 为正数表示告警触发后按百分比增加实例，为负数表示告警触发后按百分比减少实例，单位是：%。
        :type AdjustmentValue: int
        :param _Cooldown: 冷却时间，单位为秒，仅适用于简单策略。默认冷却时间300秒。
        :type Cooldown: int
        :param _MetricAlarm: 告警监控指标，仅适用于简单策略。
        :type MetricAlarm: :class:`tencentcloud.autoscaling.v20180419.models.MetricAlarm`
        :param _PredefinedMetricType: 预定义监控项，仅适用于目标追踪策略。取值范围：<br><li>ASG_AVG_CPU_UTILIZATION：平均CPU使用率</li><li>ASG_AVG_LAN_TRAFFIC_OUT：平均内网出带宽</li><li>ASG_AVG_LAN_TRAFFIC_IN：平均内网入带宽</li><li>ASG_AVG_WAN_TRAFFIC_OUT：平均外网出带宽</li><li>ASG_AVG_WAN_TRAFFIC_IN：平均外网出带宽</li>
        :type PredefinedMetricType: str
        :param _TargetValue: 目标值，仅适用于目标追踪策略。<br><li>ASG_AVG_CPU_UTILIZATION：[1, 100)，单位：%</li><li>ASG_AVG_LAN_TRAFFIC_OUT：>0，单位：Mbps</li><li>ASG_AVG_LAN_TRAFFIC_IN：>0，单位：Mbps</li><li>ASG_AVG_WAN_TRAFFIC_OUT：>0，单位：Mbps</li><li>ASG_AVG_WAN_TRAFFIC_IN：>0，单位：Mbps</li>
        :type TargetValue: int
        :param _EstimatedInstanceWarmup: 实例预热时间，单位为秒，仅适用于目标追踪策略。取值范围为0-3600，默认预热时间300秒。
        :type EstimatedInstanceWarmup: int
        :param _DisableScaleIn: 是否禁用缩容，仅适用于目标追踪策略，默认值为 false。取值范围：<br><li>true：目标追踪策略仅触发扩容</li><li>false：目标追踪策略触发扩容和缩容</li>
        :type DisableScaleIn: bool
        :param _NotificationUserGroupIds: 此参数已不再生效，请使用[创建通知](https://cloud.tencent.com/document/api/377/33185)。
通知组ID，即为用户组ID集合。
        :type NotificationUserGroupIds: list of str
        """
        self._AutoScalingGroupId = None
        self._ScalingPolicyName = None
        self._ScalingPolicyType = None
        self._AdjustmentType = None
        self._AdjustmentValue = None
        self._Cooldown = None
        self._MetricAlarm = None
        self._PredefinedMetricType = None
        self._TargetValue = None
        self._EstimatedInstanceWarmup = None
        self._DisableScaleIn = None
        self._NotificationUserGroupIds = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ScalingPolicyName(self):
        return self._ScalingPolicyName

    @ScalingPolicyName.setter
    def ScalingPolicyName(self, ScalingPolicyName):
        self._ScalingPolicyName = ScalingPolicyName

    @property
    def ScalingPolicyType(self):
        return self._ScalingPolicyType

    @ScalingPolicyType.setter
    def ScalingPolicyType(self, ScalingPolicyType):
        self._ScalingPolicyType = ScalingPolicyType

    @property
    def AdjustmentType(self):
        return self._AdjustmentType

    @AdjustmentType.setter
    def AdjustmentType(self, AdjustmentType):
        self._AdjustmentType = AdjustmentType

    @property
    def AdjustmentValue(self):
        return self._AdjustmentValue

    @AdjustmentValue.setter
    def AdjustmentValue(self, AdjustmentValue):
        self._AdjustmentValue = AdjustmentValue

    @property
    def Cooldown(self):
        return self._Cooldown

    @Cooldown.setter
    def Cooldown(self, Cooldown):
        self._Cooldown = Cooldown

    @property
    def MetricAlarm(self):
        return self._MetricAlarm

    @MetricAlarm.setter
    def MetricAlarm(self, MetricAlarm):
        self._MetricAlarm = MetricAlarm

    @property
    def PredefinedMetricType(self):
        return self._PredefinedMetricType

    @PredefinedMetricType.setter
    def PredefinedMetricType(self, PredefinedMetricType):
        self._PredefinedMetricType = PredefinedMetricType

    @property
    def TargetValue(self):
        return self._TargetValue

    @TargetValue.setter
    def TargetValue(self, TargetValue):
        self._TargetValue = TargetValue

    @property
    def EstimatedInstanceWarmup(self):
        return self._EstimatedInstanceWarmup

    @EstimatedInstanceWarmup.setter
    def EstimatedInstanceWarmup(self, EstimatedInstanceWarmup):
        self._EstimatedInstanceWarmup = EstimatedInstanceWarmup

    @property
    def DisableScaleIn(self):
        return self._DisableScaleIn

    @DisableScaleIn.setter
    def DisableScaleIn(self, DisableScaleIn):
        self._DisableScaleIn = DisableScaleIn

    @property
    def NotificationUserGroupIds(self):
        return self._NotificationUserGroupIds

    @NotificationUserGroupIds.setter
    def NotificationUserGroupIds(self, NotificationUserGroupIds):
        self._NotificationUserGroupIds = NotificationUserGroupIds


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._ScalingPolicyName = params.get("ScalingPolicyName")
        self._ScalingPolicyType = params.get("ScalingPolicyType")
        self._AdjustmentType = params.get("AdjustmentType")
        self._AdjustmentValue = params.get("AdjustmentValue")
        self._Cooldown = params.get("Cooldown")
        if params.get("MetricAlarm") is not None:
            self._MetricAlarm = MetricAlarm()
            self._MetricAlarm._deserialize(params.get("MetricAlarm"))
        self._PredefinedMetricType = params.get("PredefinedMetricType")
        self._TargetValue = params.get("TargetValue")
        self._EstimatedInstanceWarmup = params.get("EstimatedInstanceWarmup")
        self._DisableScaleIn = params.get("DisableScaleIn")
        self._NotificationUserGroupIds = params.get("NotificationUserGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScalingPolicyResponse(AbstractModel):
    """CreateScalingPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingPolicyId: 告警触发策略ID。
        :type AutoScalingPolicyId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoScalingPolicyId = None
        self._RequestId = None

    @property
    def AutoScalingPolicyId(self):
        return self._AutoScalingPolicyId

    @AutoScalingPolicyId.setter
    def AutoScalingPolicyId(self, AutoScalingPolicyId):
        self._AutoScalingPolicyId = AutoScalingPolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        self._RequestId = params.get("RequestId")


class CreateScheduledActionRequest(AbstractModel):
    """CreateScheduledAction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _ScheduledActionName: 定时任务名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。同一伸缩组下必须唯一。
        :type ScheduledActionName: str
        :param _MaxSize: 当定时任务触发时，设置的伸缩组最大实例数。
        :type MaxSize: int
        :param _MinSize: 当定时任务触发时，设置的伸缩组最小实例数。
        :type MinSize: int
        :param _DesiredCapacity: 当定时任务触发时，设置的伸缩组期望实例数。
        :type DesiredCapacity: int
        :param _StartTime: 定时任务的首次触发时间，取值为`北京时间`（UTC+8），按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ss+08:00`。
        :type StartTime: str
        :param _EndTime: 定时任务的结束时间，取值为`北京时间`（UTC+8），按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ss+08:00`。<br><br>此参数与`Recurrence`需要同时指定，到达结束时间之后，定时任务将不再生效。
        :type EndTime: str
        :param _Recurrence: 定时任务的重复方式。为标准 Cron 格式<br><br>此参数与`EndTime`需要同时指定。
        :type Recurrence: str
        """
        self._AutoScalingGroupId = None
        self._ScheduledActionName = None
        self._MaxSize = None
        self._MinSize = None
        self._DesiredCapacity = None
        self._StartTime = None
        self._EndTime = None
        self._Recurrence = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ScheduledActionName(self):
        return self._ScheduledActionName

    @ScheduledActionName.setter
    def ScheduledActionName(self, ScheduledActionName):
        self._ScheduledActionName = ScheduledActionName

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def DesiredCapacity(self):
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Recurrence(self):
        return self._Recurrence

    @Recurrence.setter
    def Recurrence(self, Recurrence):
        self._Recurrence = Recurrence


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._ScheduledActionName = params.get("ScheduledActionName")
        self._MaxSize = params.get("MaxSize")
        self._MinSize = params.get("MinSize")
        self._DesiredCapacity = params.get("DesiredCapacity")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Recurrence = params.get("Recurrence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScheduledActionResponse(AbstractModel):
    """CreateScheduledAction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScheduledActionId: 定时任务ID
        :type ScheduledActionId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScheduledActionId = None
        self._RequestId = None

    @property
    def ScheduledActionId(self):
        return self._ScheduledActionId

    @ScheduledActionId.setter
    def ScheduledActionId(self, ScheduledActionId):
        self._ScheduledActionId = ScheduledActionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ScheduledActionId = params.get("ScheduledActionId")
        self._RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """启动配置的数据盘配置信息。若不指定该参数，则默认不购买数据盘，当前仅支持购买的时候指定一个数据盘。

    """

    def __init__(self):
        r"""
        :param _DiskType: 数据盘类型。数据盘类型限制详见[云硬盘类型](https://cloud.tencent.com/document/product/362/2353)。取值范围：<br><li>LOCAL_BASIC：本地硬盘<br><li>LOCAL_SSD：本地SSD硬盘<br><li>CLOUD_BASIC：普通云硬盘<br><li>CLOUD_PREMIUM：高性能云硬盘<br><li>CLOUD_SSD：SSD云硬盘<br><li>CLOUD_HSSD：增强型SSD云硬盘<br><li>CLOUD_TSSD：极速型SSD云硬盘<br><br>默认取值与系统盘类型（SystemDisk.DiskType）保持一致。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _DiskSize: 数据盘大小，单位：GB。最小调整步长为10G，不同数据盘类型取值范围不同，具体限制详见：[CVM实例配置](https://cloud.tencent.com/document/product/213/2177)。默认值为0，表示不购买数据盘。更多限制详见产品文档。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _SnapshotId: 数据盘快照 ID，类似 `snap-l8psqwnt`。
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotId: str
        :param _DeleteWithInstance: 数据盘是否随子机销毁。取值范围：<br><li>TRUE：子机销毁时，销毁数据盘，只支持按小时后付费云盘<br><li>FALSE：子机销毁时，保留数据盘
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteWithInstance: bool
        :param _Encrypt: 数据盘是否加密。取值范围：<br><li>TRUE：加密<br><li>FALSE：不加密
注意：此字段可能返回 null，表示取不到有效值。
        :type Encrypt: bool
        :param _ThroughputPerformance: 云硬盘性能，单位：MB/s。使用此参数可给云硬盘购买额外的性能，功能介绍和类型限制详见：[增强型 SSD 云硬盘额外性能说明](https://cloud.tencent.com/document/product/362/51896#.E5.A2.9E.E5.BC.BA.E5.9E.8B-ssd-.E4.BA.91.E7.A1.AC.E7.9B.98.E9.A2.9D.E5.A4.96.E6.80.A7.E8.83.BD)。
当前仅支持极速型云盘（CLOUD_TSSD）和增强型SSD云硬盘（CLOUD_HSSD）且 需容量 > 460GB。
注意：此字段可能返回 null，表示取不到有效值。
        :type ThroughputPerformance: int
        """
        self._DiskType = None
        self._DiskSize = None
        self._SnapshotId = None
        self._DeleteWithInstance = None
        self._Encrypt = None
        self._ThroughputPerformance = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DeleteWithInstance(self):
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def Encrypt(self):
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def ThroughputPerformance(self):
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._SnapshotId = params.get("SnapshotId")
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._Encrypt = params.get("Encrypt")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoScalingGroupRequest(AbstractModel):
    """DeleteAutoScalingGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        """
        self._AutoScalingGroupId = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoScalingGroupResponse(AbstractModel):
    """DeleteAutoScalingGroup返回参数结构体

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


class DeleteLaunchConfigurationRequest(AbstractModel):
    """DeleteLaunchConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LaunchConfigurationId: 需要删除的启动配置ID。
        :type LaunchConfigurationId: str
        """
        self._LaunchConfigurationId = None

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId


    def _deserialize(self, params):
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLaunchConfigurationResponse(AbstractModel):
    """DeleteLaunchConfiguration返回参数结构体

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


class DeleteLifecycleHookRequest(AbstractModel):
    """DeleteLifecycleHook请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LifecycleHookId: 生命周期挂钩ID
        :type LifecycleHookId: str
        """
        self._LifecycleHookId = None

    @property
    def LifecycleHookId(self):
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId


    def _deserialize(self, params):
        self._LifecycleHookId = params.get("LifecycleHookId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLifecycleHookResponse(AbstractModel):
    """DeleteLifecycleHook返回参数结构体

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


class DeleteNotificationConfigurationRequest(AbstractModel):
    """DeleteNotificationConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingNotificationId: 待删除的通知ID。
        :type AutoScalingNotificationId: str
        """
        self._AutoScalingNotificationId = None

    @property
    def AutoScalingNotificationId(self):
        return self._AutoScalingNotificationId

    @AutoScalingNotificationId.setter
    def AutoScalingNotificationId(self, AutoScalingNotificationId):
        self._AutoScalingNotificationId = AutoScalingNotificationId


    def _deserialize(self, params):
        self._AutoScalingNotificationId = params.get("AutoScalingNotificationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNotificationConfigurationResponse(AbstractModel):
    """DeleteNotificationConfiguration返回参数结构体

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


class DeleteScalingPolicyRequest(AbstractModel):
    """DeleteScalingPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingPolicyId: 待删除的告警策略ID。
        :type AutoScalingPolicyId: str
        """
        self._AutoScalingPolicyId = None

    @property
    def AutoScalingPolicyId(self):
        return self._AutoScalingPolicyId

    @AutoScalingPolicyId.setter
    def AutoScalingPolicyId(self, AutoScalingPolicyId):
        self._AutoScalingPolicyId = AutoScalingPolicyId


    def _deserialize(self, params):
        self._AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteScalingPolicyResponse(AbstractModel):
    """DeleteScalingPolicy返回参数结构体

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


class DeleteScheduledActionRequest(AbstractModel):
    """DeleteScheduledAction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ScheduledActionId: 待删除的定时任务ID。
        :type ScheduledActionId: str
        """
        self._ScheduledActionId = None

    @property
    def ScheduledActionId(self):
        return self._ScheduledActionId

    @ScheduledActionId.setter
    def ScheduledActionId(self, ScheduledActionId):
        self._ScheduledActionId = ScheduledActionId


    def _deserialize(self, params):
        self._ScheduledActionId = params.get("ScheduledActionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteScheduledActionResponse(AbstractModel):
    """DeleteScheduledAction返回参数结构体

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


class DescribeAccountLimitsRequest(AbstractModel):
    """DescribeAccountLimits请求参数结构体

    """


class DescribeAccountLimitsResponse(AbstractModel):
    """DescribeAccountLimits返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MaxNumberOfLaunchConfigurations: 用户账户被允许创建的启动配置最大数量
        :type MaxNumberOfLaunchConfigurations: int
        :param _NumberOfLaunchConfigurations: 用户账户启动配置的当前数量
        :type NumberOfLaunchConfigurations: int
        :param _MaxNumberOfAutoScalingGroups: 用户账户被允许创建的伸缩组最大数量
        :type MaxNumberOfAutoScalingGroups: int
        :param _NumberOfAutoScalingGroups: 用户账户伸缩组的当前数量
        :type NumberOfAutoScalingGroups: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MaxNumberOfLaunchConfigurations = None
        self._NumberOfLaunchConfigurations = None
        self._MaxNumberOfAutoScalingGroups = None
        self._NumberOfAutoScalingGroups = None
        self._RequestId = None

    @property
    def MaxNumberOfLaunchConfigurations(self):
        return self._MaxNumberOfLaunchConfigurations

    @MaxNumberOfLaunchConfigurations.setter
    def MaxNumberOfLaunchConfigurations(self, MaxNumberOfLaunchConfigurations):
        self._MaxNumberOfLaunchConfigurations = MaxNumberOfLaunchConfigurations

    @property
    def NumberOfLaunchConfigurations(self):
        return self._NumberOfLaunchConfigurations

    @NumberOfLaunchConfigurations.setter
    def NumberOfLaunchConfigurations(self, NumberOfLaunchConfigurations):
        self._NumberOfLaunchConfigurations = NumberOfLaunchConfigurations

    @property
    def MaxNumberOfAutoScalingGroups(self):
        return self._MaxNumberOfAutoScalingGroups

    @MaxNumberOfAutoScalingGroups.setter
    def MaxNumberOfAutoScalingGroups(self, MaxNumberOfAutoScalingGroups):
        self._MaxNumberOfAutoScalingGroups = MaxNumberOfAutoScalingGroups

    @property
    def NumberOfAutoScalingGroups(self):
        return self._NumberOfAutoScalingGroups

    @NumberOfAutoScalingGroups.setter
    def NumberOfAutoScalingGroups(self, NumberOfAutoScalingGroups):
        self._NumberOfAutoScalingGroups = NumberOfAutoScalingGroups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MaxNumberOfLaunchConfigurations = params.get("MaxNumberOfLaunchConfigurations")
        self._NumberOfLaunchConfigurations = params.get("NumberOfLaunchConfigurations")
        self._MaxNumberOfAutoScalingGroups = params.get("MaxNumberOfAutoScalingGroups")
        self._NumberOfAutoScalingGroups = params.get("NumberOfAutoScalingGroups")
        self._RequestId = params.get("RequestId")


class DescribeAutoScalingActivitiesRequest(AbstractModel):
    """DescribeAutoScalingActivities请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityIds: 按照一个或者多个伸缩活动ID查询。伸缩活动ID形如：`asa-5l2ejpfo`。每次请求的上限为100。参数不支持同时指定`ActivityIds`和`Filters`。
        :type ActivityIds: list of str
        :param _Filters: 过滤条件。
<li> auto-scaling-group-id - String - 是否必填：否 -（过滤条件）按照伸缩组ID过滤。</li>
<li> activity-status-code - String - 是否必填：否 -（过滤条件）按照伸缩活动状态过滤。（INIT：初始化中|RUNNING：运行中|SUCCESSFUL：活动成功|PARTIALLY_SUCCESSFUL：活动部分成功|FAILED：活动失败|CANCELLED：活动取消）</li>
<li> activity-type - String - 是否必填：否 -（过滤条件）按照伸缩活动类型过滤。（SCALE_OUT：扩容活动|SCALE_IN：缩容活动|ATTACH_INSTANCES：添加实例|REMOVE_INSTANCES：销毁实例|DETACH_INSTANCES：移出实例|TERMINATE_INSTANCES_UNEXPECTEDLY：实例在CVM控制台被销毁|REPLACE_UNHEALTHY_INSTANCE：替换不健康实例|UPDATE_LOAD_BALANCERS：更新负载均衡器）</li>
<li> activity-id - String - 是否必填：否 -（过滤条件）按照伸缩活动ID过滤。</li>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`ActivityIds`和`Filters`。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _StartTime: 伸缩活动最早的开始时间，如果指定了ActivityIds，此参数将被忽略。取值为`UTC`时间，按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ssZ`。
        :type StartTime: str
        :param _EndTime: 伸缩活动最晚的结束时间，如果指定了ActivityIds，此参数将被忽略。取值为`UTC`时间，按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ssZ`。
        :type EndTime: str
        """
        self._ActivityIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ActivityIds(self):
        return self._ActivityIds

    @ActivityIds.setter
    def ActivityIds(self, ActivityIds):
        self._ActivityIds = ActivityIds

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

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ActivityIds = params.get("ActivityIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoScalingActivitiesResponse(AbstractModel):
    """DescribeAutoScalingActivities返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的伸缩活动数量。
        :type TotalCount: int
        :param _ActivitySet: 符合条件的伸缩活动信息集合。
        :type ActivitySet: list of Activity
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ActivitySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ActivitySet(self):
        return self._ActivitySet

    @ActivitySet.setter
    def ActivitySet(self, ActivitySet):
        self._ActivitySet = ActivitySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ActivitySet") is not None:
            self._ActivitySet = []
            for item in params.get("ActivitySet"):
                obj = Activity()
                obj._deserialize(item)
                self._ActivitySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAutoScalingAdvicesRequest(AbstractModel):
    """DescribeAutoScalingAdvices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupIds: 待查询的伸缩组列表，上限100。
        :type AutoScalingGroupIds: list of str
        """
        self._AutoScalingGroupIds = None

    @property
    def AutoScalingGroupIds(self):
        return self._AutoScalingGroupIds

    @AutoScalingGroupIds.setter
    def AutoScalingGroupIds(self, AutoScalingGroupIds):
        self._AutoScalingGroupIds = AutoScalingGroupIds


    def _deserialize(self, params):
        self._AutoScalingGroupIds = params.get("AutoScalingGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoScalingAdvicesResponse(AbstractModel):
    """DescribeAutoScalingAdvices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingAdviceSet: 伸缩组配置建议集合。
        :type AutoScalingAdviceSet: list of AutoScalingAdvice
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoScalingAdviceSet = None
        self._RequestId = None

    @property
    def AutoScalingAdviceSet(self):
        return self._AutoScalingAdviceSet

    @AutoScalingAdviceSet.setter
    def AutoScalingAdviceSet(self, AutoScalingAdviceSet):
        self._AutoScalingAdviceSet = AutoScalingAdviceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AutoScalingAdviceSet") is not None:
            self._AutoScalingAdviceSet = []
            for item in params.get("AutoScalingAdviceSet"):
                obj = AutoScalingAdvice()
                obj._deserialize(item)
                self._AutoScalingAdviceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAutoScalingGroupLastActivitiesRequest(AbstractModel):
    """DescribeAutoScalingGroupLastActivities请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupIds: 伸缩组ID列表
        :type AutoScalingGroupIds: list of str
        """
        self._AutoScalingGroupIds = None

    @property
    def AutoScalingGroupIds(self):
        return self._AutoScalingGroupIds

    @AutoScalingGroupIds.setter
    def AutoScalingGroupIds(self, AutoScalingGroupIds):
        self._AutoScalingGroupIds = AutoScalingGroupIds


    def _deserialize(self, params):
        self._AutoScalingGroupIds = params.get("AutoScalingGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoScalingGroupLastActivitiesResponse(AbstractModel):
    """DescribeAutoScalingGroupLastActivities返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivitySet: 符合条件的伸缩活动信息集合。说明：伸缩组伸缩活动不存在的则不返回，如传50个伸缩组ID，返回45条数据，说明其中有5个伸缩组伸缩活动不存在。
        :type ActivitySet: list of Activity
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivitySet = None
        self._RequestId = None

    @property
    def ActivitySet(self):
        return self._ActivitySet

    @ActivitySet.setter
    def ActivitySet(self, ActivitySet):
        self._ActivitySet = ActivitySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ActivitySet") is not None:
            self._ActivitySet = []
            for item in params.get("ActivitySet"):
                obj = Activity()
                obj._deserialize(item)
                self._ActivitySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAutoScalingGroupsRequest(AbstractModel):
    """DescribeAutoScalingGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupIds: 按照一个或者多个伸缩组ID查询。伸缩组ID形如：`asg-nkdwoui0`。每次请求的上限为100。参数不支持同时指定`AutoScalingGroupIds`和`Filters`。
        :type AutoScalingGroupIds: list of str
        :param _Filters: 过滤条件。
<li> auto-scaling-group-id - String - 是否必填：否 -（过滤条件）按照伸缩组ID过滤。</li>
<li> auto-scaling-group-name - String - 是否必填：否 -（过滤条件）按照伸缩组名称过滤。</li>
<li> vague-auto-scaling-group-name - String - 是否必填：否 -（过滤条件）按照伸缩组名称模糊搜索。</li>
<li> launch-configuration-id - String - 是否必填：否 -（过滤条件）按照启动配置ID过滤。</li>
<li> tag-key - String - 是否必填：否 -（过滤条件）按照标签键进行过滤。</li>
<li> tag-value - String - 是否必填：否 -（过滤条件）按照标签值进行过滤。</li>
<li> tag:tag-key - String - 是否必填：否 -（过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例2</li>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`AutoScalingGroupIds`和`Filters`。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        """
        self._AutoScalingGroupIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def AutoScalingGroupIds(self):
        return self._AutoScalingGroupIds

    @AutoScalingGroupIds.setter
    def AutoScalingGroupIds(self, AutoScalingGroupIds):
        self._AutoScalingGroupIds = AutoScalingGroupIds

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
        self._AutoScalingGroupIds = params.get("AutoScalingGroupIds")
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
        


class DescribeAutoScalingGroupsResponse(AbstractModel):
    """DescribeAutoScalingGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupSet: 伸缩组详细信息列表。
        :type AutoScalingGroupSet: list of AutoScalingGroup
        :param _TotalCount: 符合条件的伸缩组数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoScalingGroupSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AutoScalingGroupSet(self):
        return self._AutoScalingGroupSet

    @AutoScalingGroupSet.setter
    def AutoScalingGroupSet(self, AutoScalingGroupSet):
        self._AutoScalingGroupSet = AutoScalingGroupSet

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
        if params.get("AutoScalingGroupSet") is not None:
            self._AutoScalingGroupSet = []
            for item in params.get("AutoScalingGroupSet"):
                obj = AutoScalingGroup()
                obj._deserialize(item)
                self._AutoScalingGroupSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAutoScalingInstancesRequest(AbstractModel):
    """DescribeAutoScalingInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 待查询云服务器（CVM）的实例ID。每次请求的上限为100。参数不支持同时指定InstanceIds和Filters。
        :type InstanceIds: list of str
        :param _Filters: 过滤条件。
<li> instance-id - String - 是否必填：否 -（过滤条件）按照实例ID过滤。</li>
<li> auto-scaling-group-id - String - 是否必填：否 -（过滤条件）按照伸缩组ID过滤。</li>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`InstanceIds`和`Filters`。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self._InstanceIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

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
        self._InstanceIds = params.get("InstanceIds")
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
        


class DescribeAutoScalingInstancesResponse(AbstractModel):
    """DescribeAutoScalingInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingInstanceSet: 实例详细信息列表。
        :type AutoScalingInstanceSet: list of Instance
        :param _TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutoScalingInstanceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AutoScalingInstanceSet(self):
        return self._AutoScalingInstanceSet

    @AutoScalingInstanceSet.setter
    def AutoScalingInstanceSet(self, AutoScalingInstanceSet):
        self._AutoScalingInstanceSet = AutoScalingInstanceSet

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
        if params.get("AutoScalingInstanceSet") is not None:
            self._AutoScalingInstanceSet = []
            for item in params.get("AutoScalingInstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self._AutoScalingInstanceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeLaunchConfigurationsRequest(AbstractModel):
    """DescribeLaunchConfigurations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LaunchConfigurationIds: 按照一个或者多个启动配置ID查询。启动配置ID形如：`asc-ouy1ax38`。每次请求的上限为100。参数不支持同时指定`LaunchConfigurationIds`和`Filters`
        :type LaunchConfigurationIds: list of str
        :param _Filters: 过滤条件。
<li> launch-configuration-id - String - 是否必填：否 -（过滤条件）按照启动配置ID过滤。</li>
<li> launch-configuration-name - String - 是否必填：否 -（过滤条件）按照启动配置名称过滤。</li>
<li> vague-launch-configuration-name - String - 是否必填：否 -（过滤条件）按照启动配置名称模糊搜索。</li>
<li> tag-key - String - 是否必填：否 -（过滤条件）按照标签键进行过滤。</li>
<li> tag-value - String - 是否必填：否 -（过滤条件）按照标签值进行过滤。</li>
<li> tag:tag-key - String - 是否必填：否 -（过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例3
</li>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`LaunchConfigurationIds`和`Filters`。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        """
        self._LaunchConfigurationIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def LaunchConfigurationIds(self):
        return self._LaunchConfigurationIds

    @LaunchConfigurationIds.setter
    def LaunchConfigurationIds(self, LaunchConfigurationIds):
        self._LaunchConfigurationIds = LaunchConfigurationIds

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
        self._LaunchConfigurationIds = params.get("LaunchConfigurationIds")
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
        


class DescribeLaunchConfigurationsResponse(AbstractModel):
    """DescribeLaunchConfigurations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的启动配置数量。
        :type TotalCount: int
        :param _LaunchConfigurationSet: 启动配置详细信息列表。
        :type LaunchConfigurationSet: list of LaunchConfiguration
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._LaunchConfigurationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LaunchConfigurationSet(self):
        return self._LaunchConfigurationSet

    @LaunchConfigurationSet.setter
    def LaunchConfigurationSet(self, LaunchConfigurationSet):
        self._LaunchConfigurationSet = LaunchConfigurationSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("LaunchConfigurationSet") is not None:
            self._LaunchConfigurationSet = []
            for item in params.get("LaunchConfigurationSet"):
                obj = LaunchConfiguration()
                obj._deserialize(item)
                self._LaunchConfigurationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLifecycleHooksRequest(AbstractModel):
    """DescribeLifecycleHooks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LifecycleHookIds: 按照一个或者多个生命周期挂钩ID查询。生命周期挂钩ID形如：`ash-8azjzxcl`。每次请求的上限为100。参数不支持同时指定`LifecycleHookIds`和`Filters`。
        :type LifecycleHookIds: list of str
        :param _Filters: 过滤条件。
<li> lifecycle-hook-id - String - 是否必填：否 -（过滤条件）按照生命周期挂钩ID过滤。</li>
<li> lifecycle-hook-name - String - 是否必填：否 -（过滤条件）按照生命周期挂钩名称过滤。</li>
<li> auto-scaling-group-id - String - 是否必填：否 -（过滤条件）按照伸缩组ID过滤。</li>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`LifecycleHookIds `和`Filters`。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        """
        self._LifecycleHookIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def LifecycleHookIds(self):
        return self._LifecycleHookIds

    @LifecycleHookIds.setter
    def LifecycleHookIds(self, LifecycleHookIds):
        self._LifecycleHookIds = LifecycleHookIds

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
        self._LifecycleHookIds = params.get("LifecycleHookIds")
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
        


class DescribeLifecycleHooksResponse(AbstractModel):
    """DescribeLifecycleHooks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LifecycleHookSet: 生命周期挂钩数组
        :type LifecycleHookSet: list of LifecycleHook
        :param _TotalCount: 总体数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LifecycleHookSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def LifecycleHookSet(self):
        return self._LifecycleHookSet

    @LifecycleHookSet.setter
    def LifecycleHookSet(self, LifecycleHookSet):
        self._LifecycleHookSet = LifecycleHookSet

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
        if params.get("LifecycleHookSet") is not None:
            self._LifecycleHookSet = []
            for item in params.get("LifecycleHookSet"):
                obj = LifecycleHook()
                obj._deserialize(item)
                self._LifecycleHookSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeNotificationConfigurationsRequest(AbstractModel):
    """DescribeNotificationConfigurations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingNotificationIds: 按照一个或者多个通知ID查询。实例ID形如：asn-2sestqbr。每次请求的实例的上限为100。参数不支持同时指定`AutoScalingNotificationIds`和`Filters`。
        :type AutoScalingNotificationIds: list of str
        :param _Filters: 过滤条件。
<li> auto-scaling-notification-id - String - 是否必填：否 -（过滤条件）按照通知ID过滤。</li>
<li> auto-scaling-group-id - String - 是否必填：否 -（过滤条件）按照伸缩组ID过滤。</li>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`AutoScalingNotificationIds`和`Filters`。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        """
        self._AutoScalingNotificationIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def AutoScalingNotificationIds(self):
        return self._AutoScalingNotificationIds

    @AutoScalingNotificationIds.setter
    def AutoScalingNotificationIds(self, AutoScalingNotificationIds):
        self._AutoScalingNotificationIds = AutoScalingNotificationIds

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
        self._AutoScalingNotificationIds = params.get("AutoScalingNotificationIds")
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
        


class DescribeNotificationConfigurationsResponse(AbstractModel):
    """DescribeNotificationConfigurations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的通知数量。
        :type TotalCount: int
        :param _AutoScalingNotificationSet: 弹性伸缩事件通知详细信息列表。
        :type AutoScalingNotificationSet: list of AutoScalingNotification
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AutoScalingNotificationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AutoScalingNotificationSet(self):
        return self._AutoScalingNotificationSet

    @AutoScalingNotificationSet.setter
    def AutoScalingNotificationSet(self, AutoScalingNotificationSet):
        self._AutoScalingNotificationSet = AutoScalingNotificationSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AutoScalingNotificationSet") is not None:
            self._AutoScalingNotificationSet = []
            for item in params.get("AutoScalingNotificationSet"):
                obj = AutoScalingNotification()
                obj._deserialize(item)
                self._AutoScalingNotificationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRefreshActivitiesRequest(AbstractModel):
    """DescribeRefreshActivities请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RefreshActivityIds: 刷新活动ID列表。ID形如：`asr-5l2ejpfo`。每次请求的上限为100。参数不支持同时指定`RefreshActivityIds`和`Filters`。
        :type RefreshActivityIds: list of str
        :param _Filters: 过滤条件。
<li> auto-scaling-group-id - String - 是否必填：否 -（过滤条件）按照伸缩组ID过滤。</li>
<li> refresh-activity-status-code - String - 是否必填：否 -（过滤条件）按照刷新活动状态过滤。（INIT：初始化中 | RUNNING：运行中 | SUCCESSFUL：活动成功 | FAILED_PAUSE：失败暂停 | AUTO_PAUSE：自动暂停 | MANUAL_PAUSE：手动暂停 | CANCELLED：活动取消 | FAILED：活动失败）</li>
<li> refresh-activity-type - String - 是否必填：否 -（过滤条件）按照刷新活动类型过滤。（NORMAL：正常刷新活动 | ROLLBACK：回滚刷新活动）</li>
<li> refresh-activity-id - String - 是否必填：否 -（过滤条件）按照刷新活动ID过滤。</li>
<li> 每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定RefreshActivityIds和Filters。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        """
        self._RefreshActivityIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def RefreshActivityIds(self):
        return self._RefreshActivityIds

    @RefreshActivityIds.setter
    def RefreshActivityIds(self, RefreshActivityIds):
        self._RefreshActivityIds = RefreshActivityIds

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
        self._RefreshActivityIds = params.get("RefreshActivityIds")
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
        


class DescribeRefreshActivitiesResponse(AbstractModel):
    """DescribeRefreshActivities返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的刷新活动数量。
        :type TotalCount: int
        :param _RefreshActivitySet: 符合条件的刷新活动信息集合。
        :type RefreshActivitySet: list of RefreshActivity
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RefreshActivitySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RefreshActivitySet(self):
        return self._RefreshActivitySet

    @RefreshActivitySet.setter
    def RefreshActivitySet(self, RefreshActivitySet):
        self._RefreshActivitySet = RefreshActivitySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RefreshActivitySet") is not None:
            self._RefreshActivitySet = []
            for item in params.get("RefreshActivitySet"):
                obj = RefreshActivity()
                obj._deserialize(item)
                self._RefreshActivitySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScalingPoliciesRequest(AbstractModel):
    """DescribeScalingPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingPolicyIds: 按照一个或者多个告警策略ID查询。告警策略ID形如：asp-i9vkg894。每次请求的实例的上限为100。参数不支持同时指定`AutoScalingPolicyIds`和`Filters`。
        :type AutoScalingPolicyIds: list of str
        :param _Filters: 过滤条件。
<li> auto-scaling-policy-id - String - 是否必填：否 -（过滤条件）按照告警策略ID过滤。</li>
<li> auto-scaling-group-id - String - 是否必填：否 -（过滤条件）按照伸缩组ID过滤。</li>
<li> scaling-policy-name - String - 是否必填：否 -（过滤条件）按照告警策略名称过滤。</li>
<li> scaling-policy-type - String - 是否必填：否 -（过滤条件）按照告警策略类型过滤，取值范围为SIMPLE，TARGET_TRACKING。</li>
每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`AutoScalingPolicyIds`和`Filters`。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        """
        self._AutoScalingPolicyIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def AutoScalingPolicyIds(self):
        return self._AutoScalingPolicyIds

    @AutoScalingPolicyIds.setter
    def AutoScalingPolicyIds(self, AutoScalingPolicyIds):
        self._AutoScalingPolicyIds = AutoScalingPolicyIds

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
        self._AutoScalingPolicyIds = params.get("AutoScalingPolicyIds")
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
        


class DescribeScalingPoliciesResponse(AbstractModel):
    """DescribeScalingPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScalingPolicySet: 弹性伸缩告警触发策略详细信息列表。
        :type ScalingPolicySet: list of ScalingPolicy
        :param _TotalCount: 符合条件的通知数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScalingPolicySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ScalingPolicySet(self):
        return self._ScalingPolicySet

    @ScalingPolicySet.setter
    def ScalingPolicySet(self, ScalingPolicySet):
        self._ScalingPolicySet = ScalingPolicySet

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
        if params.get("ScalingPolicySet") is not None:
            self._ScalingPolicySet = []
            for item in params.get("ScalingPolicySet"):
                obj = ScalingPolicy()
                obj._deserialize(item)
                self._ScalingPolicySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeScheduledActionsRequest(AbstractModel):
    """DescribeScheduledActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ScheduledActionIds: 按照一个或者多个定时任务ID查询。实例ID形如：asst-am691zxo。每次请求的实例的上限为100。参数不支持同时指定ScheduledActionIds和Filters。
        :type ScheduledActionIds: list of str
        :param _Filters: 过滤条件。
<li> scheduled-action-id - String - 是否必填：否 -（过滤条件）按照定时任务ID过滤。</li>
<li> scheduled-action-name - String - 是否必填：否 - （过滤条件） 按照定时任务名称过滤。</li>
<li> auto-scaling-group-id - String - 是否必填：否 - （过滤条件） 按照伸缩组ID过滤。</li>
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self._ScheduledActionIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ScheduledActionIds(self):
        return self._ScheduledActionIds

    @ScheduledActionIds.setter
    def ScheduledActionIds(self, ScheduledActionIds):
        self._ScheduledActionIds = ScheduledActionIds

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
        self._ScheduledActionIds = params.get("ScheduledActionIds")
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
        


class DescribeScheduledActionsResponse(AbstractModel):
    """DescribeScheduledActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的定时任务数量。
        :type TotalCount: int
        :param _ScheduledActionSet: 定时任务详细信息列表。
        :type ScheduledActionSet: list of ScheduledAction
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ScheduledActionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ScheduledActionSet(self):
        return self._ScheduledActionSet

    @ScheduledActionSet.setter
    def ScheduledActionSet(self, ScheduledActionSet):
        self._ScheduledActionSet = ScheduledActionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ScheduledActionSet") is not None:
            self._ScheduledActionSet = []
            for item in params.get("ScheduledActionSet"):
                obj = ScheduledAction()
                obj._deserialize(item)
                self._ScheduledActionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DetachInstancesRequest(AbstractModel):
    """DetachInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _InstanceIds: CVM实例ID列表
        :type InstanceIds: list of str
        """
        self._AutoScalingGroupId = None
        self._InstanceIds = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachInstancesResponse(AbstractModel):
    """DetachInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityId: 伸缩活动ID
        :type ActivityId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class DetachLoadBalancersRequest(AbstractModel):
    """DetachLoadBalancers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _LoadBalancerIds: 传统负载均衡器ID列表，列表长度上限为20，LoadBalancerIds 和 ForwardLoadBalancerIdentifications 二者同时最多只能指定一个
        :type LoadBalancerIds: list of str
        :param _ForwardLoadBalancerIdentifications: 应用型负载均衡器标识信息列表，列表长度上限为100，LoadBalancerIds 和 ForwardLoadBalancerIdentifications二者同时最多只能指定一个
        :type ForwardLoadBalancerIdentifications: list of ForwardLoadBalancerIdentification
        """
        self._AutoScalingGroupId = None
        self._LoadBalancerIds = None
        self._ForwardLoadBalancerIdentifications = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ForwardLoadBalancerIdentifications(self):
        return self._ForwardLoadBalancerIdentifications

    @ForwardLoadBalancerIdentifications.setter
    def ForwardLoadBalancerIdentifications(self, ForwardLoadBalancerIdentifications):
        self._ForwardLoadBalancerIdentifications = ForwardLoadBalancerIdentifications


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        if params.get("ForwardLoadBalancerIdentifications") is not None:
            self._ForwardLoadBalancerIdentifications = []
            for item in params.get("ForwardLoadBalancerIdentifications"):
                obj = ForwardLoadBalancerIdentification()
                obj._deserialize(item)
                self._ForwardLoadBalancerIdentifications.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachLoadBalancersResponse(AbstractModel):
    """DetachLoadBalancers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityId: 伸缩活动ID
        :type ActivityId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class DetailedStatusMessage(AbstractModel):
    """伸缩活动状态详细描述。

    """

    def __init__(self):
        r"""
        :param _Code: 错误类型。
        :type Code: str
        :param _Zone: 可用区信息。
        :type Zone: str
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _InstanceChargeType: 实例计费类型。
        :type InstanceChargeType: str
        :param _SubnetId: 子网ID。
        :type SubnetId: str
        :param _Message: 错误描述。
        :type Message: str
        :param _InstanceType: 实例类型。
        :type InstanceType: str
        """
        self._Code = None
        self._Zone = None
        self._InstanceId = None
        self._InstanceChargeType = None
        self._SubnetId = None
        self._Message = None
        self._InstanceType = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Zone = params.get("Zone")
        self._InstanceId = params.get("InstanceId")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._SubnetId = params.get("SubnetId")
        self._Message = params.get("Message")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableAutoScalingGroupRequest(AbstractModel):
    """DisableAutoScalingGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        """
        self._AutoScalingGroupId = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableAutoScalingGroupResponse(AbstractModel):
    """DisableAutoScalingGroup返回参数结构体

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


class EnableAutoScalingGroupRequest(AbstractModel):
    """EnableAutoScalingGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        """
        self._AutoScalingGroupId = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableAutoScalingGroupResponse(AbstractModel):
    """EnableAutoScalingGroup返回参数结构体

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


class EnhancedService(AbstractModel):
    """描述了实例的增强服务启用情况与其设置，如云安全，云监控，自动化助手等实例 Agent。

    """

    def __init__(self):
        r"""
        :param _SecurityService: 开启云安全服务。若不指定该参数，则默认开启云安全服务。
        :type SecurityService: :class:`tencentcloud.autoscaling.v20180419.models.RunSecurityServiceEnabled`
        :param _MonitorService: 开启云监控服务。若不指定该参数，则默认开启云监控服务。
        :type MonitorService: :class:`tencentcloud.autoscaling.v20180419.models.RunMonitorServiceEnabled`
        :param _AutomationService: 该参数已废弃，查询时会返回空值，请勿使用。
        :type AutomationService: list of RunAutomationServiceEnabled
        :param _AutomationToolsService: 开启自动化助手服务。若不指定该参数，则默认逻辑与CVM保持一致。注意：此字段可能返回 null，表示取不到有效值。
        :type AutomationToolsService: :class:`tencentcloud.autoscaling.v20180419.models.RunAutomationServiceEnabled`
        """
        self._SecurityService = None
        self._MonitorService = None
        self._AutomationService = None
        self._AutomationToolsService = None

    @property
    def SecurityService(self):
        return self._SecurityService

    @SecurityService.setter
    def SecurityService(self, SecurityService):
        self._SecurityService = SecurityService

    @property
    def MonitorService(self):
        return self._MonitorService

    @MonitorService.setter
    def MonitorService(self, MonitorService):
        self._MonitorService = MonitorService

    @property
    def AutomationService(self):
        warnings.warn("parameter `AutomationService` is deprecated", DeprecationWarning) 

        return self._AutomationService

    @AutomationService.setter
    def AutomationService(self, AutomationService):
        warnings.warn("parameter `AutomationService` is deprecated", DeprecationWarning) 

        self._AutomationService = AutomationService

    @property
    def AutomationToolsService(self):
        return self._AutomationToolsService

    @AutomationToolsService.setter
    def AutomationToolsService(self, AutomationToolsService):
        self._AutomationToolsService = AutomationToolsService


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self._SecurityService = RunSecurityServiceEnabled()
            self._SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self._MonitorService = RunMonitorServiceEnabled()
            self._MonitorService._deserialize(params.get("MonitorService"))
        if params.get("AutomationService") is not None:
            self._AutomationService = []
            for item in params.get("AutomationService"):
                obj = RunAutomationServiceEnabled()
                obj._deserialize(item)
                self._AutomationService.append(obj)
        if params.get("AutomationToolsService") is not None:
            self._AutomationToolsService = RunAutomationServiceEnabled()
            self._AutomationToolsService._deserialize(params.get("AutomationToolsService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteScalingPolicyRequest(AbstractModel):
    """ExecuteScalingPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingPolicyId: 告警伸缩策略ID，不支持目标追踪策略。
        :type AutoScalingPolicyId: str
        :param _HonorCooldown: 是否检查伸缩组活动处于冷却时间内，默认值为false
        :type HonorCooldown: bool
        :param _TriggerSource: 执行伸缩策略的触发来源，取值包括 API 和 CLOUD_MONITOR，默认值为 API。CLOUD_MONITOR 专门供云监控触发调用。
        :type TriggerSource: str
        """
        self._AutoScalingPolicyId = None
        self._HonorCooldown = None
        self._TriggerSource = None

    @property
    def AutoScalingPolicyId(self):
        return self._AutoScalingPolicyId

    @AutoScalingPolicyId.setter
    def AutoScalingPolicyId(self, AutoScalingPolicyId):
        self._AutoScalingPolicyId = AutoScalingPolicyId

    @property
    def HonorCooldown(self):
        return self._HonorCooldown

    @HonorCooldown.setter
    def HonorCooldown(self, HonorCooldown):
        self._HonorCooldown = HonorCooldown

    @property
    def TriggerSource(self):
        return self._TriggerSource

    @TriggerSource.setter
    def TriggerSource(self, TriggerSource):
        self._TriggerSource = TriggerSource


    def _deserialize(self, params):
        self._AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        self._HonorCooldown = params.get("HonorCooldown")
        self._TriggerSource = params.get("TriggerSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteScalingPolicyResponse(AbstractModel):
    """ExecuteScalingPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityId: 伸缩活动ID
        :type ActivityId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class ExitStandbyRequest(AbstractModel):
    """ExitStandby请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组 ID。
        :type AutoScalingGroupId: str
        :param _InstanceIds: 备用中状态 CVM 实例列表。
        :type InstanceIds: list of str
        """
        self._AutoScalingGroupId = None
        self._InstanceIds = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExitStandbyResponse(AbstractModel):
    """ExitStandby返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityId: 伸缩活动ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """>描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    > * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。
    >
    > 以[DescribeInstances](https://cloud.tencent.com/document/api/213/15728)接口的`Filter`为例。若我们需要查询可用区（`zone`）为广州一区 ***并且*** 实例计费模式（`instance-charge-type`）为包年包月 ***或者*** 按量计费的实例时，可如下实现：
    ```
    Filters.0.Name=zone
    &Filters.0.Values.0=ap-guangzhou-1
    &Filters.1.Name=instance-charge-type
    &Filters.1.Values.0=PREPAID
    &Filters.1.Values.1=POSTPAID_BY_HOUR
    ```

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
        


class ForwardLoadBalancer(AbstractModel):
    """应用型负载均衡器

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡器ID
        :type LoadBalancerId: str
        :param _ListenerId: 应用型负载均衡监听器 ID
        :type ListenerId: str
        :param _TargetAttributes: 目标规则属性列表
        :type TargetAttributes: list of TargetAttribute
        :param _LocationId: 转发规则ID，注意：针对七层监听器此参数必填
        :type LocationId: str
        :param _Region: 负载均衡实例所属地域，默认取AS服务所在地域。格式与公共参数Region相同，如："ap-guangzhou"。
        :type Region: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._TargetAttributes = None
        self._LocationId = None
        self._Region = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def TargetAttributes(self):
        return self._TargetAttributes

    @TargetAttributes.setter
    def TargetAttributes(self, TargetAttributes):
        self._TargetAttributes = TargetAttributes

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("TargetAttributes") is not None:
            self._TargetAttributes = []
            for item in params.get("TargetAttributes"):
                obj = TargetAttribute()
                obj._deserialize(item)
                self._TargetAttributes.append(obj)
        self._LocationId = params.get("LocationId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForwardLoadBalancerIdentification(AbstractModel):
    """应用型负载均衡器标识信息

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡器ID
        :type LoadBalancerId: str
        :param _ListenerId: 应用型负载均衡监听器 ID
        :type ListenerId: str
        :param _LocationId: 转发规则ID，注意：针对七层监听器此参数必填
        :type LocationId: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._LocationId = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._LocationId = params.get("LocationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostNameSettings(AbstractModel):
    """云服务器主机名（HostName）的相关设置

    """

    def __init__(self):
        r"""
        :param _HostName: 云服务器的主机名。
<br><li> 点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。
<br><li> 不支持 Windows 实例。
<br><li> 其他类型（Linux 等）实例：字符长度为[2, 40]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。不允许为纯数字。
注意：此字段可能返回 null，表示取不到有效值。
        :type HostName: str
        :param _HostNameStyle: 云服务器主机名的风格，取值范围包括 ORIGINAL 和  UNIQUE，默认为 ORIGINAL。
<br><li> ORIGINAL，AS 直接将入参中所填的 HostName 传递给 CVM，CVM 可能会对 HostName 追加序列号，伸缩组中实例的 HostName 会出现冲突的情况。
<br><li> UNIQUE，入参所填的 HostName 相当于主机名前缀，AS 和 CVM 会对其进行拓展，伸缩组中实例的 HostName 可以保证唯一。
注意：此字段可能返回 null，表示取不到有效值。
        :type HostNameStyle: str
        """
        self._HostName = None
        self._HostNameStyle = None

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def HostNameStyle(self):
        return self._HostNameStyle

    @HostNameStyle.setter
    def HostNameStyle(self, HostNameStyle):
        self._HostNameStyle = HostNameStyle


    def _deserialize(self, params):
        self._HostName = params.get("HostName")
        self._HostNameStyle = params.get("HostNameStyle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPv6InternetAccessible(AbstractModel):
    """描述了启动配置创建实例的IPv6地址公网可访问性，声明了IPv6地址公网使用计费模式，最大带宽等

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: 网络计费模式。取值包括TRAFFIC_POSTPAID_BY_HOUR、BANDWIDTH_PACKAGE，默认取值为TRAFFIC_POSTPAID_BY_HOUR。查看当前账户类型可参考[账户类型说明](https://cloud.tencent.com/document/product/1199/49090#judge)。
<br><li> IPv6对标准账户类型支持TRAFFIC_POSTPAID_BY_HOUR。
<br><li> IPv6对传统账户类型支持BANDWIDTH_PACKAGE。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: 公网出带宽上限，单位：Mbps。<br>默认值：0，此时不为IPv6分配公网带宽。不同机型、可用区、计费模式的带宽上限范围不一致，具体限制详见[公网带宽上限](https://cloud.tencent.com/document/product/213/12523)。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetMaxBandwidthOut: int
        :param _BandwidthPackageId: 带宽包ID。可通过[DescribeBandwidthPackages](https://cloud.tencent.com/document/api/215/19209)接口返回值中的`BandwidthPackageId`获取。
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthPackageId: str
        """
        self._InternetChargeType = None
        self._InternetMaxBandwidthOut = None
        self._BandwidthPackageId = None

    @property
    def InternetChargeType(self):
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def BandwidthPackageId(self):
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId


    def _deserialize(self, params):
        self._InternetChargeType = params.get("InternetChargeType")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _LaunchConfigurationId: 启动配置ID
        :type LaunchConfigurationId: str
        :param _LaunchConfigurationName: 启动配置名称
        :type LaunchConfigurationName: str
        :param _LifeCycleState: 生命周期状态，取值如下：<br>
<li>IN_SERVICE：运行中
<li>CREATING：创建中
<li>CREATION_FAILED：创建失败
<li>TERMINATING：中止中
<li>TERMINATION_FAILED：中止失败
<li>ATTACHING：绑定中
<li>ATTACH_FAILED：绑定失败
<li>DETACHING：解绑中
<li>DETACH_FAILED：解绑失败
<li>ATTACHING_LB：绑定LB中
<li>DETACHING_LB：解绑LB中
<li>MODIFYING_LB：修改LB中
<li>STARTING：开机中
<li>START_FAILED：开机失败
<li>STOPPING：关机中
<li>STOP_FAILED：关机失败
<li>STOPPED：已关机
<li>IN_LAUNCHING_HOOK：扩容生命周期挂钩中
<li>IN_TERMINATING_HOOK：缩容生命周期挂钩中
        :type LifeCycleState: str
        :param _HealthStatus: 健康状态，取值包括HEALTHY和UNHEALTHY
        :type HealthStatus: str
        :param _ProtectedFromScaleIn: 是否加入缩容保护
        :type ProtectedFromScaleIn: bool
        :param _Zone: 可用区
        :type Zone: str
        :param _CreationType: 创建类型，取值包括AUTO_CREATION, MANUAL_ATTACHING。
        :type CreationType: str
        :param _AddTime: 实例加入时间
        :type AddTime: str
        :param _InstanceType: 实例类型
        :type InstanceType: str
        :param _VersionNumber: 版本号
        :type VersionNumber: int
        :param _AutoScalingGroupName: 伸缩组名称
        :type AutoScalingGroupName: str
        :param _WarmupStatus: 预热状态，取值如下：
<li>WAITING_ENTER_WARMUP：等待进入预热
<li>NO_NEED_WARMUP：无需预热
<li>IN_WARMUP：预热中
<li>AFTER_WARMUP：完成预热
        :type WarmupStatus: str
        :param _DisasterRecoverGroupIds: 置放群组id，仅支持指定一个。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisasterRecoverGroupIds: list of str
        """
        self._InstanceId = None
        self._AutoScalingGroupId = None
        self._LaunchConfigurationId = None
        self._LaunchConfigurationName = None
        self._LifeCycleState = None
        self._HealthStatus = None
        self._ProtectedFromScaleIn = None
        self._Zone = None
        self._CreationType = None
        self._AddTime = None
        self._InstanceType = None
        self._VersionNumber = None
        self._AutoScalingGroupName = None
        self._WarmupStatus = None
        self._DisasterRecoverGroupIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def LaunchConfigurationName(self):
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def LifeCycleState(self):
        return self._LifeCycleState

    @LifeCycleState.setter
    def LifeCycleState(self, LifeCycleState):
        self._LifeCycleState = LifeCycleState

    @property
    def HealthStatus(self):
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def ProtectedFromScaleIn(self):
        return self._ProtectedFromScaleIn

    @ProtectedFromScaleIn.setter
    def ProtectedFromScaleIn(self, ProtectedFromScaleIn):
        self._ProtectedFromScaleIn = ProtectedFromScaleIn

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CreationType(self):
        return self._CreationType

    @CreationType.setter
    def CreationType(self, CreationType):
        self._CreationType = CreationType

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def VersionNumber(self):
        return self._VersionNumber

    @VersionNumber.setter
    def VersionNumber(self, VersionNumber):
        self._VersionNumber = VersionNumber

    @property
    def AutoScalingGroupName(self):
        return self._AutoScalingGroupName

    @AutoScalingGroupName.setter
    def AutoScalingGroupName(self, AutoScalingGroupName):
        self._AutoScalingGroupName = AutoScalingGroupName

    @property
    def WarmupStatus(self):
        return self._WarmupStatus

    @WarmupStatus.setter
    def WarmupStatus(self, WarmupStatus):
        self._WarmupStatus = WarmupStatus

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._LaunchConfigurationName = params.get("LaunchConfigurationName")
        self._LifeCycleState = params.get("LifeCycleState")
        self._HealthStatus = params.get("HealthStatus")
        self._ProtectedFromScaleIn = params.get("ProtectedFromScaleIn")
        self._Zone = params.get("Zone")
        self._CreationType = params.get("CreationType")
        self._AddTime = params.get("AddTime")
        self._InstanceType = params.get("InstanceType")
        self._VersionNumber = params.get("VersionNumber")
        self._AutoScalingGroupName = params.get("AutoScalingGroupName")
        self._WarmupStatus = params.get("WarmupStatus")
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
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
        :param _Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :type Period: int
        :param _RenewFlag: 自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费<br><br>默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
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
        


class InstanceMarketOptionsRequest(AbstractModel):
    """CVM竞价请求相关选项

    """

    def __init__(self):
        r"""
        :param _SpotOptions: 竞价相关选项
        :type SpotOptions: :class:`tencentcloud.autoscaling.v20180419.models.SpotMarketOptions`
        :param _MarketType: 市场选项类型，当前只支持取值：spot
注意：此字段可能返回 null，表示取不到有效值。
        :type MarketType: str
        """
        self._SpotOptions = None
        self._MarketType = None

    @property
    def SpotOptions(self):
        return self._SpotOptions

    @SpotOptions.setter
    def SpotOptions(self, SpotOptions):
        self._SpotOptions = SpotOptions

    @property
    def MarketType(self):
        return self._MarketType

    @MarketType.setter
    def MarketType(self, MarketType):
        self._MarketType = MarketType


    def _deserialize(self, params):
        if params.get("SpotOptions") is not None:
            self._SpotOptions = SpotMarketOptions()
            self._SpotOptions._deserialize(params.get("SpotOptions"))
        self._MarketType = params.get("MarketType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNameSettings(AbstractModel):
    """云服务器实例名称（InstanceName）的相关设置

    """

    def __init__(self):
        r"""
        :param _InstanceName: 云服务器的实例名。字符长度为[2, 108]。
        :type InstanceName: str
        :param _InstanceNameStyle: 云服务器实例名的风格，取值范围包括 ORIGINAL 和 UNIQUE，默认为 ORIGINAL。

ORIGINAL，AS 直接将入参中所填的 InstanceName 传递给 CVM，CVM 可能会对 InstanceName 追加序列号，伸缩组中实例的 InstanceName 会出现冲突的情况。

UNIQUE，入参所填的 InstanceName 相当于实例名前缀，AS 和 CVM 会对其进行拓展，伸缩组中实例的 InstanceName 可以保证唯一。
        :type InstanceNameStyle: str
        """
        self._InstanceName = None
        self._InstanceNameStyle = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceNameStyle(self):
        return self._InstanceNameStyle

    @InstanceNameStyle.setter
    def InstanceNameStyle(self, InstanceNameStyle):
        self._InstanceNameStyle = InstanceNameStyle


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._InstanceNameStyle = params.get("InstanceNameStyle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTag(AbstractModel):
    """实例标签。通过指定该参数，可以为扩容的实例绑定标签。

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
        


class InternetAccessible(AbstractModel):
    """描述了启动配置创建实例的公网可访问性，声明了实例的公网使用计费模式，最大带宽等

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: 网络计费类型。取值范围：<br><li>BANDWIDTH_PREPAID：预付费按带宽结算<br><li>TRAFFIC_POSTPAID_BY_HOUR：流量按小时后付费<br><li>BANDWIDTH_POSTPAID_BY_HOUR：带宽按小时后付费<br><li>BANDWIDTH_PACKAGE：带宽包用户<br>默认取值：TRAFFIC_POSTPAID_BY_HOUR。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: 公网出带宽上限，单位：Mbps。默认值：0Mbps。不同机型带宽上限范围不一致，具体限制详见[购买网络带宽](https://cloud.tencent.com/document/product/213/509)。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetMaxBandwidthOut: int
        :param _PublicIpAssigned: 是否分配公网IP。取值范围：<br><li>TRUE：表示分配公网IP<br><li>FALSE：表示不分配公网IP<br><br>当公网带宽大于0Mbps时，可自由选择开通与否，默认开通公网IP；当公网带宽为0，则不允许分配公网IP。
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAssigned: bool
        :param _BandwidthPackageId: 带宽包ID。可通过[DescribeBandwidthPackages](https://cloud.tencent.com/document/api/215/19209)接口返回值中的`BandwidthPackageId`获取。
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthPackageId: str
        """
        self._InternetChargeType = None
        self._InternetMaxBandwidthOut = None
        self._PublicIpAssigned = None
        self._BandwidthPackageId = None

    @property
    def InternetChargeType(self):
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def PublicIpAssigned(self):
        return self._PublicIpAssigned

    @PublicIpAssigned.setter
    def PublicIpAssigned(self, PublicIpAssigned):
        self._PublicIpAssigned = PublicIpAssigned

    @property
    def BandwidthPackageId(self):
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
        


class InvocationResult(AbstractModel):
    """执行命令结果。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InvocationId: 执行活动ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type InvocationId: str
        :param _InvocationTaskId: 执行任务ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type InvocationTaskId: str
        :param _CommandId: 命令ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CommandId: str
        :param _TaskStatus: 执行任务状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskStatus: str
        :param _ErrorMessage: 执行异常信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        """
        self._InstanceId = None
        self._InvocationId = None
        self._InvocationTaskId = None
        self._CommandId = None
        self._TaskStatus = None
        self._ErrorMessage = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InvocationId(self):
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def InvocationTaskId(self):
        return self._InvocationTaskId

    @InvocationTaskId.setter
    def InvocationTaskId(self, InvocationTaskId):
        self._InvocationTaskId = InvocationTaskId

    @property
    def CommandId(self):
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InvocationId = params.get("InvocationId")
        self._InvocationTaskId = params.get("InvocationTaskId")
        self._CommandId = params.get("CommandId")
        self._TaskStatus = params.get("TaskStatus")
        self._ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaunchConfiguration(AbstractModel):
    """符合条件的启动配置信息的集合。

    """

    def __init__(self):
        r"""
        :param _ProjectId: 实例所属项目ID。
        :type ProjectId: int
        :param _LaunchConfigurationId: 启动配置ID。
        :type LaunchConfigurationId: str
        :param _LaunchConfigurationName: 启动配置名称。
        :type LaunchConfigurationName: str
        :param _InstanceType: 实例机型。
        :type InstanceType: str
        :param _SystemDisk: 实例系统盘配置信息。
        :type SystemDisk: :class:`tencentcloud.autoscaling.v20180419.models.SystemDisk`
        :param _DataDisks: 实例数据盘配置信息。
        :type DataDisks: list of DataDisk
        :param _LoginSettings: 实例登录设置。
        :type LoginSettings: :class:`tencentcloud.autoscaling.v20180419.models.LimitedLoginSettings`
        :param _InternetAccessible: 公网带宽相关信息设置。
        :type InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        :param _SecurityGroupIds: 实例所属安全组。
        :type SecurityGroupIds: list of str
        :param _AutoScalingGroupAbstractSet: 启动配置关联的伸缩组。
        :type AutoScalingGroupAbstractSet: list of AutoScalingGroupAbstract
        :param _UserData: 自定义数据。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserData: str
        :param _CreatedTime: 启动配置创建时间。
        :type CreatedTime: str
        :param _EnhancedService: 实例的增强服务启用情况与其设置。
        :type EnhancedService: :class:`tencentcloud.autoscaling.v20180419.models.EnhancedService`
        :param _ImageId: 镜像ID。
        :type ImageId: str
        :param _LaunchConfigurationStatus: 启动配置当前状态。取值范围：<br><li>NORMAL：正常<br><li>IMAGE_ABNORMAL：启动配置镜像异常<br><li>CBS_SNAP_ABNORMAL：启动配置数据盘快照异常<br><li>SECURITY_GROUP_ABNORMAL：启动配置安全组异常<br>
        :type LaunchConfigurationStatus: str
        :param _InstanceChargeType: 实例计费类型，CVM默认值按照POSTPAID_BY_HOUR处理。
<br><li>POSTPAID_BY_HOUR：按小时后付费
<br><li>SPOTPAID：竞价付费
        :type InstanceChargeType: str
        :param _InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数，若指定实例的付费模式为竞价付费则该参数必传。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceMarketOptions: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        :param _InstanceTypes: 实例机型列表。
        :type InstanceTypes: list of str
        :param _InstanceTags: 实例标签列表。扩容出来的实例会自动带上标签，最多支持10个标签。
        :type InstanceTags: list of InstanceTag
        :param _Tags: 标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _VersionNumber: 版本号。
        :type VersionNumber: int
        :param _UpdatedTime: 更新时间。
        :type UpdatedTime: str
        :param _CamRoleName: CAM角色名称。可通过DescribeRoleList接口返回值中的roleName获取。
        :type CamRoleName: str
        :param _LastOperationInstanceTypesCheckPolicy: 上次操作时，InstanceTypesCheckPolicy 取值。
        :type LastOperationInstanceTypesCheckPolicy: str
        :param _HostNameSettings: 云服务器主机名（HostName）的相关设置。
        :type HostNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.HostNameSettings`
        :param _InstanceNameSettings: 云服务器实例名（InstanceName）的相关设置。
        :type InstanceNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameSettings`
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.autoscaling.v20180419.models.InstanceChargePrepaid`
        :param _DiskTypePolicy: 云盘类型选择策略。取值范围：
<br><li>ORIGINAL：使用设置的云盘类型
<br><li>AUTOMATIC：自动选择当前可用区下可用的云盘类型
        :type DiskTypePolicy: str
        :param _HpcClusterId: 高性能计算集群ID。<br>
注意：此字段默认为空。
        :type HpcClusterId: str
        :param _IPv6InternetAccessible: IPv6公网带宽相关信息设置。
        :type IPv6InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.IPv6InternetAccessible`
        """
        self._ProjectId = None
        self._LaunchConfigurationId = None
        self._LaunchConfigurationName = None
        self._InstanceType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._LoginSettings = None
        self._InternetAccessible = None
        self._SecurityGroupIds = None
        self._AutoScalingGroupAbstractSet = None
        self._UserData = None
        self._CreatedTime = None
        self._EnhancedService = None
        self._ImageId = None
        self._LaunchConfigurationStatus = None
        self._InstanceChargeType = None
        self._InstanceMarketOptions = None
        self._InstanceTypes = None
        self._InstanceTags = None
        self._Tags = None
        self._VersionNumber = None
        self._UpdatedTime = None
        self._CamRoleName = None
        self._LastOperationInstanceTypesCheckPolicy = None
        self._HostNameSettings = None
        self._InstanceNameSettings = None
        self._InstanceChargePrepaid = None
        self._DiskTypePolicy = None
        self._HpcClusterId = None
        self._IPv6InternetAccessible = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def LaunchConfigurationName(self):
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def AutoScalingGroupAbstractSet(self):
        return self._AutoScalingGroupAbstractSet

    @AutoScalingGroupAbstractSet.setter
    def AutoScalingGroupAbstractSet(self, AutoScalingGroupAbstractSet):
        self._AutoScalingGroupAbstractSet = AutoScalingGroupAbstractSet

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def LaunchConfigurationStatus(self):
        return self._LaunchConfigurationStatus

    @LaunchConfigurationStatus.setter
    def LaunchConfigurationStatus(self, LaunchConfigurationStatus):
        self._LaunchConfigurationStatus = LaunchConfigurationStatus

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def InstanceTags(self):
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def VersionNumber(self):
        return self._VersionNumber

    @VersionNumber.setter
    def VersionNumber(self, VersionNumber):
        self._VersionNumber = VersionNumber

    @property
    def UpdatedTime(self):
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def LastOperationInstanceTypesCheckPolicy(self):
        return self._LastOperationInstanceTypesCheckPolicy

    @LastOperationInstanceTypesCheckPolicy.setter
    def LastOperationInstanceTypesCheckPolicy(self, LastOperationInstanceTypesCheckPolicy):
        self._LastOperationInstanceTypesCheckPolicy = LastOperationInstanceTypesCheckPolicy

    @property
    def HostNameSettings(self):
        return self._HostNameSettings

    @HostNameSettings.setter
    def HostNameSettings(self, HostNameSettings):
        self._HostNameSettings = HostNameSettings

    @property
    def InstanceNameSettings(self):
        return self._InstanceNameSettings

    @InstanceNameSettings.setter
    def InstanceNameSettings(self, InstanceNameSettings):
        self._InstanceNameSettings = InstanceNameSettings

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def DiskTypePolicy(self):
        return self._DiskTypePolicy

    @DiskTypePolicy.setter
    def DiskTypePolicy(self, DiskTypePolicy):
        self._DiskTypePolicy = DiskTypePolicy

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def IPv6InternetAccessible(self):
        return self._IPv6InternetAccessible

    @IPv6InternetAccessible.setter
    def IPv6InternetAccessible(self, IPv6InternetAccessible):
        self._IPv6InternetAccessible = IPv6InternetAccessible


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._LaunchConfigurationName = params.get("LaunchConfigurationName")
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
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LimitedLoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("AutoScalingGroupAbstractSet") is not None:
            self._AutoScalingGroupAbstractSet = []
            for item in params.get("AutoScalingGroupAbstractSet"):
                obj = AutoScalingGroupAbstract()
                obj._deserialize(item)
                self._AutoScalingGroupAbstractSet.append(obj)
        self._UserData = params.get("UserData")
        self._CreatedTime = params.get("CreatedTime")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._ImageId = params.get("ImageId")
        self._LaunchConfigurationStatus = params.get("LaunchConfigurationStatus")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._InstanceTypes = params.get("InstanceTypes")
        if params.get("InstanceTags") is not None:
            self._InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTag()
                obj._deserialize(item)
                self._InstanceTags.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._VersionNumber = params.get("VersionNumber")
        self._UpdatedTime = params.get("UpdatedTime")
        self._CamRoleName = params.get("CamRoleName")
        self._LastOperationInstanceTypesCheckPolicy = params.get("LastOperationInstanceTypesCheckPolicy")
        if params.get("HostNameSettings") is not None:
            self._HostNameSettings = HostNameSettings()
            self._HostNameSettings._deserialize(params.get("HostNameSettings"))
        if params.get("InstanceNameSettings") is not None:
            self._InstanceNameSettings = InstanceNameSettings()
            self._InstanceNameSettings._deserialize(params.get("InstanceNameSettings"))
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._DiskTypePolicy = params.get("DiskTypePolicy")
        self._HpcClusterId = params.get("HpcClusterId")
        if params.get("IPv6InternetAccessible") is not None:
            self._IPv6InternetAccessible = IPv6InternetAccessible()
            self._IPv6InternetAccessible._deserialize(params.get("IPv6InternetAccessible"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifecycleActionResultInfo(AbstractModel):
    """生命周期挂钩动作的执行结果信息。

    """

    def __init__(self):
        r"""
        :param _LifecycleHookId: 生命周期挂钩标识。
        :type LifecycleHookId: str
        :param _InstanceId: 实例标识。
        :type InstanceId: str
        :param _InvocationId: 执行活动ID。可通过TAT的[查询执行活动](https://cloud.tencent.com/document/api/1340/52679)API查询具体的执行结果。
        :type InvocationId: str
        :param _InvokeCommandResult: 命令调用的结果，表示执行TAT命令是否成功。<br>
<li>SUCCESSFUL 命令调用成功，不代表命令执行成功，执行的具体情况可根据InvocationId进行查询</li>
<li>FAILED 命令调用失败</li>
<li>NONE</li>
        :type InvokeCommandResult: str
        :param _NotificationResult: 通知的结果，表示通知CMQ/TDMQ是否成功。<br>
<li>SUCCESSFUL 通知成功</li>
<li>FAILED 通知失败</li>
<li>NONE</li>
        :type NotificationResult: str
        :param _LifecycleActionResult: 生命周期挂钩动作的执行结果，取值包括 CONTINUE、ABANDON。
        :type LifecycleActionResult: str
        :param _ResultReason: 结果的原因。<br>
<li>HEARTBEAT_TIMEOUT 由于心跳超时，结果根据DefaultResult设置。</li>
<li>NOTIFICATION_FAILURE 由于发送通知失败，结果根据DefaultResult设置。</li>
<li>CALL_INTERFACE 调用了接口CompleteLifecycleAction设置结果。</li>
<li>ANOTHER_ACTION_ABANDON 另一个生命周期操作的结果已设置为“ABANDON”。</li>
<li>COMMAND_CALL_FAILURE  由于命令调用失败，结果根据DefaultResult设置。</li>
<li>COMMAND_EXEC_FINISH  命令执行完成。</li>
<li>COMMAND_EXEC_FAILURE 由于命令执行失败，结果根据DefaultResult设置。</li>
<li>COMMAND_EXEC_RESULT_CHECK_FAILURE 由于命令结果检查失败，结果根据DefaultResult设置。</li>
        :type ResultReason: str
        """
        self._LifecycleHookId = None
        self._InstanceId = None
        self._InvocationId = None
        self._InvokeCommandResult = None
        self._NotificationResult = None
        self._LifecycleActionResult = None
        self._ResultReason = None

    @property
    def LifecycleHookId(self):
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InvocationId(self):
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def InvokeCommandResult(self):
        return self._InvokeCommandResult

    @InvokeCommandResult.setter
    def InvokeCommandResult(self, InvokeCommandResult):
        self._InvokeCommandResult = InvokeCommandResult

    @property
    def NotificationResult(self):
        return self._NotificationResult

    @NotificationResult.setter
    def NotificationResult(self, NotificationResult):
        self._NotificationResult = NotificationResult

    @property
    def LifecycleActionResult(self):
        return self._LifecycleActionResult

    @LifecycleActionResult.setter
    def LifecycleActionResult(self, LifecycleActionResult):
        self._LifecycleActionResult = LifecycleActionResult

    @property
    def ResultReason(self):
        return self._ResultReason

    @ResultReason.setter
    def ResultReason(self, ResultReason):
        self._ResultReason = ResultReason


    def _deserialize(self, params):
        self._LifecycleHookId = params.get("LifecycleHookId")
        self._InstanceId = params.get("InstanceId")
        self._InvocationId = params.get("InvocationId")
        self._InvokeCommandResult = params.get("InvokeCommandResult")
        self._NotificationResult = params.get("NotificationResult")
        self._LifecycleActionResult = params.get("LifecycleActionResult")
        self._ResultReason = params.get("ResultReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifecycleCommand(AbstractModel):
    """远程命令执行对象。

    """

    def __init__(self):
        r"""
        :param _CommandId: 远程命令ID。若选择执行命令，则此项必填。
注意：此字段可能返回 null，表示取不到有效值。
        :type CommandId: str
        :param _Parameters: 自定义参数。字段类型为 json encoded string。如：{"varA": "222"}。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
如果未提供该参数取值，将使用 Command 的 DefaultParameters 进行替换。
自定义参数最多20个。自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。
注意：此字段可能返回 null，表示取不到有效值。
        :type Parameters: str
        """
        self._CommandId = None
        self._Parameters = None

    @property
    def CommandId(self):
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters


    def _deserialize(self, params):
        self._CommandId = params.get("CommandId")
        self._Parameters = params.get("Parameters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifecycleHook(AbstractModel):
    """生命周期挂钩

    """

    def __init__(self):
        r"""
        :param _LifecycleHookId: 生命周期挂钩ID
        :type LifecycleHookId: str
        :param _LifecycleHookName: 生命周期挂钩名称
        :type LifecycleHookName: str
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _DefaultResult: 生命周期挂钩默认结果
        :type DefaultResult: str
        :param _HeartbeatTimeout: 生命周期挂钩等待超时时间
        :type HeartbeatTimeout: int
        :param _LifecycleTransition: 生命周期挂钩适用场景
        :type LifecycleTransition: str
        :param _NotificationMetadata: 通知目标的附加信息
        :type NotificationMetadata: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _NotificationTarget: 通知目标
        :type NotificationTarget: :class:`tencentcloud.autoscaling.v20180419.models.NotificationTarget`
        :param _LifecycleTransitionType: 生命周期挂钩适用场景
        :type LifecycleTransitionType: str
        :param _LifecycleCommand: 远程命令执行对象
注意：此字段可能返回 null，表示取不到有效值。
        :type LifecycleCommand: :class:`tencentcloud.autoscaling.v20180419.models.LifecycleCommand`
        """
        self._LifecycleHookId = None
        self._LifecycleHookName = None
        self._AutoScalingGroupId = None
        self._DefaultResult = None
        self._HeartbeatTimeout = None
        self._LifecycleTransition = None
        self._NotificationMetadata = None
        self._CreatedTime = None
        self._NotificationTarget = None
        self._LifecycleTransitionType = None
        self._LifecycleCommand = None

    @property
    def LifecycleHookId(self):
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def LifecycleHookName(self):
        return self._LifecycleHookName

    @LifecycleHookName.setter
    def LifecycleHookName(self, LifecycleHookName):
        self._LifecycleHookName = LifecycleHookName

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def DefaultResult(self):
        return self._DefaultResult

    @DefaultResult.setter
    def DefaultResult(self, DefaultResult):
        self._DefaultResult = DefaultResult

    @property
    def HeartbeatTimeout(self):
        return self._HeartbeatTimeout

    @HeartbeatTimeout.setter
    def HeartbeatTimeout(self, HeartbeatTimeout):
        self._HeartbeatTimeout = HeartbeatTimeout

    @property
    def LifecycleTransition(self):
        return self._LifecycleTransition

    @LifecycleTransition.setter
    def LifecycleTransition(self, LifecycleTransition):
        self._LifecycleTransition = LifecycleTransition

    @property
    def NotificationMetadata(self):
        return self._NotificationMetadata

    @NotificationMetadata.setter
    def NotificationMetadata(self, NotificationMetadata):
        self._NotificationMetadata = NotificationMetadata

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def NotificationTarget(self):
        return self._NotificationTarget

    @NotificationTarget.setter
    def NotificationTarget(self, NotificationTarget):
        self._NotificationTarget = NotificationTarget

    @property
    def LifecycleTransitionType(self):
        return self._LifecycleTransitionType

    @LifecycleTransitionType.setter
    def LifecycleTransitionType(self, LifecycleTransitionType):
        self._LifecycleTransitionType = LifecycleTransitionType

    @property
    def LifecycleCommand(self):
        return self._LifecycleCommand

    @LifecycleCommand.setter
    def LifecycleCommand(self, LifecycleCommand):
        self._LifecycleCommand = LifecycleCommand


    def _deserialize(self, params):
        self._LifecycleHookId = params.get("LifecycleHookId")
        self._LifecycleHookName = params.get("LifecycleHookName")
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._DefaultResult = params.get("DefaultResult")
        self._HeartbeatTimeout = params.get("HeartbeatTimeout")
        self._LifecycleTransition = params.get("LifecycleTransition")
        self._NotificationMetadata = params.get("NotificationMetadata")
        self._CreatedTime = params.get("CreatedTime")
        if params.get("NotificationTarget") is not None:
            self._NotificationTarget = NotificationTarget()
            self._NotificationTarget._deserialize(params.get("NotificationTarget"))
        self._LifecycleTransitionType = params.get("LifecycleTransitionType")
        if params.get("LifecycleCommand") is not None:
            self._LifecycleCommand = LifecycleCommand()
            self._LifecycleCommand._deserialize(params.get("LifecycleCommand"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LimitedLoginSettings(AbstractModel):
    """描述了实例登录相关配置与信息，出于安全性考虑，不会描述敏感信息。

    """

    def __init__(self):
        r"""
        :param _KeyIds: 密钥ID列表。
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
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
        :param _Password: 实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：<br><li>Linux实例密码必须8到16位，至少包括两项[a-z，A-Z]、[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? / ]中的特殊符号。<br><li>Windows实例密码必须12到16位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /]中的特殊符号。<br><br>若不指定该参数，则由系统随机生成密码，并通过站内信方式通知到用户。
        :type Password: str
        :param _KeyIds: 密钥ID列表。关联密钥后，就可以通过对应的私钥来访问实例；KeyId可通过接口DescribeKeyPairs获取，密钥与密码不能同时指定，同时Windows操作系统不支持指定密钥。当前仅支持购买的时候指定一个密钥。
        :type KeyIds: list of str
        :param _KeepImageLogin: 保持镜像的原始设置。该参数与Password或KeyIds.N不能同时指定。只有使用自定义镜像、共享镜像或外部导入镜像创建实例时才能指定该参数为TRUE。取值范围：<br><li>TRUE：表示保持镜像的登录设置<br><li>FALSE：表示不保持镜像的登录设置<br><br>默认取值：FALSE。
        :type KeepImageLogin: bool
        """
        self._Password = None
        self._KeyIds = None
        self._KeepImageLogin = None

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def KeepImageLogin(self):
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
        


class MetricAlarm(AbstractModel):
    """弹性伸缩告警指标

    """

    def __init__(self):
        r"""
        :param _ComparisonOperator: 比较运算符，可选值：<br><li>GREATER_THAN：大于</li><li>GREATER_THAN_OR_EQUAL_TO：大于或等于</li><li>LESS_THAN：小于</li><li> LESS_THAN_OR_EQUAL_TO：小于或等于</li><li> EQUAL_TO：等于</li> <li>NOT_EQUAL_TO：不等于</li>
        :type ComparisonOperator: str
        :param _MetricName: 指标名称，可选字段如下：<br><li>CPU_UTILIZATION：CPU利用率</li><li>MEM_UTILIZATION：内存利用率</li><li>LAN_TRAFFIC_OUT：内网出带宽</li><li>LAN_TRAFFIC_IN：内网入带宽</li><li>WAN_TRAFFIC_OUT：外网出带宽</li><li>WAN_TRAFFIC_IN：外网入带宽</li><li>TCP_CURR_ESTAB：TCP连接数</li>
        :type MetricName: str
        :param _Threshold: 告警阈值：<br><li>CPU_UTILIZATION：[1, 100]，单位：%</li><li>MEM_UTILIZATION：[1, 100]，单位：%</li><li>LAN_TRAFFIC_OUT：>0，单位：Mbps </li><li>LAN_TRAFFIC_IN：>0，单位：Mbps</li><li>WAN_TRAFFIC_OUT：>0，单位：Mbps</li><li>WAN_TRAFFIC_IN：>0，单位：Mbps</li><li>TCP_CURR_ESTAB：>0, 单位：Count</li>
        :type Threshold: int
        :param _Period: 时间周期，单位：秒，取值枚举值为60、300。
        :type Period: int
        :param _ContinuousTime: 重复次数。取值范围 [1, 10]
        :type ContinuousTime: int
        :param _Statistic: 统计类型，可选字段如下：<br><li>AVERAGE：平均值</li><li>MAXIMUM：最大值<li>MINIMUM：最小值</li><br> 默认取值：AVERAGE
        :type Statistic: str
        :param _PreciseThreshold: 精确告警阈值，本参数不作为入参输入，仅用作查询接口出参：<br><li>CPU_UTILIZATION：(0, 100]，单位：%</li><li>MEM_UTILIZATION：(0, 100]，单位：%</li><li>LAN_TRAFFIC_OUT：>0，单位：Mbps </li><li>LAN_TRAFFIC_IN：>0，单位：Mbps</li><li>WAN_TRAFFIC_OUT：>0，单位：Mbps</li><li>WAN_TRAFFIC_IN：>0，单位：Mbps</li><li>TCP_CURR_ESTAB：>0, 单位：Count</li>
        :type PreciseThreshold: float
        """
        self._ComparisonOperator = None
        self._MetricName = None
        self._Threshold = None
        self._Period = None
        self._ContinuousTime = None
        self._Statistic = None
        self._PreciseThreshold = None

    @property
    def ComparisonOperator(self):
        return self._ComparisonOperator

    @ComparisonOperator.setter
    def ComparisonOperator(self, ComparisonOperator):
        self._ComparisonOperator = ComparisonOperator

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ContinuousTime(self):
        return self._ContinuousTime

    @ContinuousTime.setter
    def ContinuousTime(self, ContinuousTime):
        self._ContinuousTime = ContinuousTime

    @property
    def Statistic(self):
        return self._Statistic

    @Statistic.setter
    def Statistic(self, Statistic):
        self._Statistic = Statistic

    @property
    def PreciseThreshold(self):
        return self._PreciseThreshold

    @PreciseThreshold.setter
    def PreciseThreshold(self, PreciseThreshold):
        self._PreciseThreshold = PreciseThreshold


    def _deserialize(self, params):
        self._ComparisonOperator = params.get("ComparisonOperator")
        self._MetricName = params.get("MetricName")
        self._Threshold = params.get("Threshold")
        self._Period = params.get("Period")
        self._ContinuousTime = params.get("ContinuousTime")
        self._Statistic = params.get("Statistic")
        self._PreciseThreshold = params.get("PreciseThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoScalingGroupRequest(AbstractModel):
    """ModifyAutoScalingGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _AutoScalingGroupName: 伸缩组名称，在您账号中必须唯一。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超55个字节。
        :type AutoScalingGroupName: str
        :param _DefaultCooldown: 默认冷却时间，单位秒，默认值为300
        :type DefaultCooldown: int
        :param _DesiredCapacity: 期望实例数，大小介于最小实例数和最大实例数之间
        :type DesiredCapacity: int
        :param _LaunchConfigurationId: 启动配置ID
        :type LaunchConfigurationId: str
        :param _MaxSize: 最大实例数，取值范围为0-2000。
        :type MaxSize: int
        :param _MinSize: 最小实例数，取值范围为0-2000。
        :type MinSize: int
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _SubnetIds: 子网ID列表
        :type SubnetIds: list of str
        :param _TerminationPolicies: 销毁策略，目前长度上限为1。取值包括 OLDEST_INSTANCE 和 NEWEST_INSTANCE。
<br><li> OLDEST_INSTANCE 优先销毁伸缩组中最旧的实例。
<br><li> NEWEST_INSTANCE，优先销毁伸缩组中最新的实例。
        :type TerminationPolicies: list of str
        :param _VpcId: VPC ID，基础网络则填空字符串。修改为具体VPC ID时，需指定相应的SubnetIds；修改为基础网络时，需指定相应的Zones。
        :type VpcId: str
        :param _Zones: 可用区列表
        :type Zones: list of str
        :param _RetryPolicy: 重试策略，取值包括 IMMEDIATE_RETRY、 INCREMENTAL_INTERVALS、NO_RETRY，默认取值为 IMMEDIATE_RETRY。部分成功的伸缩活动判定为一次失败活动。
<br><li>
IMMEDIATE_RETRY，立即重试，在较短时间内快速重试，连续失败超过一定次数（5次）后不再重试。
<br><li>
INCREMENTAL_INTERVALS，间隔递增重试，随着连续失败次数的增加，重试间隔逐渐增大，重试间隔从秒级到1天不等。
<br><li> NO_RETRY，不进行重试，直到再次收到用户调用或者告警信息后才会重试。
        :type RetryPolicy: str
        :param _ZonesCheckPolicy: 可用区校验策略，取值包括 ALL 和 ANY，默认取值为ANY。在伸缩组实际变更资源相关字段时（启动配置、可用区、子网）发挥作用。
<br><li> ALL，所有可用区（Zone）或子网（SubnetId）都可用则通过校验，否则校验报错。
<br><li> ANY，存在任何一个可用区（Zone）或子网（SubnetId）可用则通过校验，否则校验报错。

可用区或子网不可用的常见原因包括该可用区CVM实例类型售罄、该可用区CBS云盘售罄、该可用区配额不足、该子网IP不足等。
如果 Zones/SubnetIds 中可用区或者子网不存在，则无论 ZonesCheckPolicy 采用何种取值，都会校验报错。
        :type ZonesCheckPolicy: str
        :param _ServiceSettings: 服务设置，包括云监控不健康替换等服务设置。
        :type ServiceSettings: :class:`tencentcloud.autoscaling.v20180419.models.ServiceSettings`
        :param _Ipv6AddressCount: 实例具有IPv6地址数量的配置，取值包括0、1。
        :type Ipv6AddressCount: int
        :param _MultiZoneSubnetPolicy: 多可用区/子网策略，取值包括 PRIORITY 和 EQUALITY，默认为 PRIORITY。
<br><li> PRIORITY，按照可用区/子网列表的顺序，作为优先级来尝试创建实例，如果优先级最高的可用区/子网可以创建成功，则总在该可用区/子网创建。
<br><li> EQUALITY：扩容出的实例会打散到多个可用区/子网，保证扩容后的各个可用区/子网实例数相对均衡。

与本策略相关的注意点：
<br><li> 当伸缩组为基础网络时，本策略适用于多可用区；当伸缩组为VPC网络时，本策略适用于多子网，此时不再考虑可用区因素，例如四个子网ABCD，其中ABC处于可用区1，D处于可用区2，此时考虑子网ABCD进行排序，而不考虑可用区1、2。
<br><li> 本策略适用于多可用区/子网，不适用于启动配置的多机型。多机型按照优先级策略进行选择。
<br><li> 按照 PRIORITY 策略创建实例时，先保证多机型的策略，后保证多可用区/子网的策略。例如多机型A、B，多子网1、2、3，会按照A1、A2、A3、B1、B2、B3 进行尝试，如果A1售罄，会尝试A2（而非B1）。
        :type MultiZoneSubnetPolicy: str
        :param _HealthCheckType: 伸缩组实例健康检查类型，取值如下：<br><li>CVM：根据实例网络状态判断实例是否处于不健康状态，不健康的网络状态即发生实例 PING 不可达事件，详细判断标准可参考[实例健康检查](https://cloud.tencent.com/document/product/377/8553)<br><li>CLB：根据 CLB 的健康检查状态判断实例是否处于不健康状态，CLB健康检查原理可参考[健康检查](https://cloud.tencent.com/document/product/214/6097)
        :type HealthCheckType: str
        :param _LoadBalancerHealthCheckGracePeriod: CLB健康检查宽限期。
        :type LoadBalancerHealthCheckGracePeriod: int
        :param _InstanceAllocationPolicy: 实例分配策略，取值包括 LAUNCH_CONFIGURATION 和 SPOT_MIXED。
<br><li> LAUNCH_CONFIGURATION，代表传统的按照启动配置模式。
<br><li> SPOT_MIXED，代表竞价混合模式。目前仅支持启动配置为按量计费模式时使用混合模式，混合模式下，伸缩组将根据设定扩容按量或竞价机型。使用混合模式时，关联的启动配置的计费类型不可被修改。
        :type InstanceAllocationPolicy: str
        :param _SpotMixedAllocationPolicy: 竞价混合模式下，各计费类型实例的分配策略。
仅当 InstanceAllocationPolicy 取 SPOT_MIXED 时可用。
        :type SpotMixedAllocationPolicy: :class:`tencentcloud.autoscaling.v20180419.models.SpotMixedAllocationPolicy`
        :param _CapacityRebalance: 容量重平衡功能，仅对伸缩组内的竞价实例有效。取值范围：
<br><li> TRUE，开启该功能，当伸缩组内的竞价实例即将被竞价实例服务自动回收前，AS 主动发起竞价实例销毁流程，如果有配置过缩容 hook，则销毁前 hook 会生效。销毁流程启动后，AS 会异步开启一个扩容活动，用于补齐期望实例数。
<br><li> FALSE，不开启该功能，则 AS 等待竞价实例被销毁后才会去扩容补齐伸缩组期望实例数。
        :type CapacityRebalance: bool
        """
        self._AutoScalingGroupId = None
        self._AutoScalingGroupName = None
        self._DefaultCooldown = None
        self._DesiredCapacity = None
        self._LaunchConfigurationId = None
        self._MaxSize = None
        self._MinSize = None
        self._ProjectId = None
        self._SubnetIds = None
        self._TerminationPolicies = None
        self._VpcId = None
        self._Zones = None
        self._RetryPolicy = None
        self._ZonesCheckPolicy = None
        self._ServiceSettings = None
        self._Ipv6AddressCount = None
        self._MultiZoneSubnetPolicy = None
        self._HealthCheckType = None
        self._LoadBalancerHealthCheckGracePeriod = None
        self._InstanceAllocationPolicy = None
        self._SpotMixedAllocationPolicy = None
        self._CapacityRebalance = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def AutoScalingGroupName(self):
        return self._AutoScalingGroupName

    @AutoScalingGroupName.setter
    def AutoScalingGroupName(self, AutoScalingGroupName):
        self._AutoScalingGroupName = AutoScalingGroupName

    @property
    def DefaultCooldown(self):
        return self._DefaultCooldown

    @DefaultCooldown.setter
    def DefaultCooldown(self, DefaultCooldown):
        self._DefaultCooldown = DefaultCooldown

    @property
    def DesiredCapacity(self):
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def TerminationPolicies(self):
        return self._TerminationPolicies

    @TerminationPolicies.setter
    def TerminationPolicies(self, TerminationPolicies):
        self._TerminationPolicies = TerminationPolicies

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RetryPolicy(self):
        return self._RetryPolicy

    @RetryPolicy.setter
    def RetryPolicy(self, RetryPolicy):
        self._RetryPolicy = RetryPolicy

    @property
    def ZonesCheckPolicy(self):
        return self._ZonesCheckPolicy

    @ZonesCheckPolicy.setter
    def ZonesCheckPolicy(self, ZonesCheckPolicy):
        self._ZonesCheckPolicy = ZonesCheckPolicy

    @property
    def ServiceSettings(self):
        return self._ServiceSettings

    @ServiceSettings.setter
    def ServiceSettings(self, ServiceSettings):
        self._ServiceSettings = ServiceSettings

    @property
    def Ipv6AddressCount(self):
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount

    @property
    def MultiZoneSubnetPolicy(self):
        return self._MultiZoneSubnetPolicy

    @MultiZoneSubnetPolicy.setter
    def MultiZoneSubnetPolicy(self, MultiZoneSubnetPolicy):
        self._MultiZoneSubnetPolicy = MultiZoneSubnetPolicy

    @property
    def HealthCheckType(self):
        return self._HealthCheckType

    @HealthCheckType.setter
    def HealthCheckType(self, HealthCheckType):
        self._HealthCheckType = HealthCheckType

    @property
    def LoadBalancerHealthCheckGracePeriod(self):
        return self._LoadBalancerHealthCheckGracePeriod

    @LoadBalancerHealthCheckGracePeriod.setter
    def LoadBalancerHealthCheckGracePeriod(self, LoadBalancerHealthCheckGracePeriod):
        self._LoadBalancerHealthCheckGracePeriod = LoadBalancerHealthCheckGracePeriod

    @property
    def InstanceAllocationPolicy(self):
        return self._InstanceAllocationPolicy

    @InstanceAllocationPolicy.setter
    def InstanceAllocationPolicy(self, InstanceAllocationPolicy):
        self._InstanceAllocationPolicy = InstanceAllocationPolicy

    @property
    def SpotMixedAllocationPolicy(self):
        return self._SpotMixedAllocationPolicy

    @SpotMixedAllocationPolicy.setter
    def SpotMixedAllocationPolicy(self, SpotMixedAllocationPolicy):
        self._SpotMixedAllocationPolicy = SpotMixedAllocationPolicy

    @property
    def CapacityRebalance(self):
        return self._CapacityRebalance

    @CapacityRebalance.setter
    def CapacityRebalance(self, CapacityRebalance):
        self._CapacityRebalance = CapacityRebalance


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._AutoScalingGroupName = params.get("AutoScalingGroupName")
        self._DefaultCooldown = params.get("DefaultCooldown")
        self._DesiredCapacity = params.get("DesiredCapacity")
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._MaxSize = params.get("MaxSize")
        self._MinSize = params.get("MinSize")
        self._ProjectId = params.get("ProjectId")
        self._SubnetIds = params.get("SubnetIds")
        self._TerminationPolicies = params.get("TerminationPolicies")
        self._VpcId = params.get("VpcId")
        self._Zones = params.get("Zones")
        self._RetryPolicy = params.get("RetryPolicy")
        self._ZonesCheckPolicy = params.get("ZonesCheckPolicy")
        if params.get("ServiceSettings") is not None:
            self._ServiceSettings = ServiceSettings()
            self._ServiceSettings._deserialize(params.get("ServiceSettings"))
        self._Ipv6AddressCount = params.get("Ipv6AddressCount")
        self._MultiZoneSubnetPolicy = params.get("MultiZoneSubnetPolicy")
        self._HealthCheckType = params.get("HealthCheckType")
        self._LoadBalancerHealthCheckGracePeriod = params.get("LoadBalancerHealthCheckGracePeriod")
        self._InstanceAllocationPolicy = params.get("InstanceAllocationPolicy")
        if params.get("SpotMixedAllocationPolicy") is not None:
            self._SpotMixedAllocationPolicy = SpotMixedAllocationPolicy()
            self._SpotMixedAllocationPolicy._deserialize(params.get("SpotMixedAllocationPolicy"))
        self._CapacityRebalance = params.get("CapacityRebalance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoScalingGroupResponse(AbstractModel):
    """ModifyAutoScalingGroup返回参数结构体

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


class ModifyDesiredCapacityRequest(AbstractModel):
    """ModifyDesiredCapacity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _DesiredCapacity: 期望实例数
        :type DesiredCapacity: int
        :param _MinSize: 最小实例数，取值范围为0-2000。
        :type MinSize: int
        :param _MaxSize: 最大实例数，取值范围为0-2000。
        :type MaxSize: int
        """
        self._AutoScalingGroupId = None
        self._DesiredCapacity = None
        self._MinSize = None
        self._MaxSize = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def DesiredCapacity(self):
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._DesiredCapacity = params.get("DesiredCapacity")
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDesiredCapacityResponse(AbstractModel):
    """ModifyDesiredCapacity返回参数结构体

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


class ModifyLaunchConfigurationAttributesRequest(AbstractModel):
    """ModifyLaunchConfigurationAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LaunchConfigurationId: 启动配置ID
        :type LaunchConfigurationId: str
        :param _ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-8toqc6s3`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，取返回信息中的`ImageId`字段。</li>
        :type ImageId: str
        :param _InstanceTypes: 实例类型列表，不同实例机型指定了不同的资源规格，最多支持10种实例机型。
InstanceType 指定单一实例类型，通过设置 InstanceTypes可以指定多实例类型，并使原有的InstanceType失效。
        :type InstanceTypes: list of str
        :param _InstanceTypesCheckPolicy: 实例类型校验策略，在实际修改 InstanceTypes 时发挥作用，取值包括 ALL 和 ANY，默认取值为ANY。
<br><li> ALL，所有实例类型（InstanceType）都可用则通过校验，否则校验报错。
<br><li> ANY，存在任何一个实例类型（InstanceType）可用则通过校验，否则校验报错。

实例类型不可用的常见原因包括该实例类型售罄、对应云盘售罄等。
如果 InstanceTypes 中一款机型不存在或者已下线，则无论 InstanceTypesCheckPolicy 采用何种取值，都会校验报错。
        :type InstanceTypesCheckPolicy: str
        :param _LaunchConfigurationName: 启动配置显示名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。
        :type LaunchConfigurationName: str
        :param _UserData: 经过 Base64 编码后的自定义数据，最大长度不超过16KB。如果要清空UserData，则指定其为空字符串。
        :type UserData: str
        :param _SecurityGroupIds: 实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的`SecurityGroupId`字段来获取。
若指定该参数，请至少提供一个安全组，列表顺序有先后。
        :type SecurityGroupIds: list of str
        :param _InternetAccessible: 公网带宽相关信息设置。
当公网出带宽上限为0Mbps时，不支持修改为开通分配公网IP；相应的，当前为开通分配公网IP时，修改的公网出带宽上限值必须大于0Mbps。
        :type InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        :param _InstanceChargeType: 实例计费类型。具体取值范围如下：
<br><li>POSTPAID_BY_HOUR：按小时后付费
<br><li>SPOTPAID：竞价付费
<br><li>PREPAID：预付费，即包年包月
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。
若修改实例的付费模式为预付费，则该参数必传；从预付费修改为其他付费模式时，本字段原信息会自动丢弃。
当新增该字段时，必须传递购买实例的时长，其它未传递字段会设置为默认值。
当修改本字段时，当前付费模式必须为预付费。
        :type InstanceChargePrepaid: :class:`tencentcloud.autoscaling.v20180419.models.InstanceChargePrepaid`
        :param _InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数。
若修改实例的付费模式为竞价付费，则该参数必传；从竞价付费修改为其他付费模式时，本字段原信息会自动丢弃。
当新增该字段时，必须传递竞价相关选项下的竞价出价，其它未传递字段会设置为默认值。
当修改本字段时，当前付费模式必须为竞价付费。
        :type InstanceMarketOptions: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        :param _DiskTypePolicy: 云盘类型选择策略，取值范围：
<br><li>ORIGINAL：使用设置的云盘类型。
<br><li>AUTOMATIC：自动选择当前可用的云盘类型。
        :type DiskTypePolicy: str
        :param _SystemDisk: 实例系统盘配置信息。
        :type SystemDisk: :class:`tencentcloud.autoscaling.v20180419.models.SystemDisk`
        :param _DataDisks: 实例数据盘配置信息。
最多支持指定11块数据盘。采取整体修改，因此请提供修改后的全部值。
数据盘类型默认与系统盘类型保持一致。
        :type DataDisks: list of DataDisk
        :param _HostNameSettings: 云服务器主机名（HostName）的相关设置。
不支持windows实例设置主机名。
新增该属性时，必须传递云服务器的主机名，其它未传递字段会设置为默认值。
        :type HostNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.HostNameSettings`
        :param _InstanceNameSettings: 云服务器（InstanceName）实例名的相关设置。 
如果用户在启动配置中设置此字段，则伸缩组创建出的实例 InstanceName 参照此字段进行设置，并传递给 CVM；如果用户未在启动配置中设置此字段，则伸缩组创建出的实例 InstanceName 按照“as-{{ 伸缩组AutoScalingGroupName }}”进行设置，并传递给 CVM。
新增该属性时，必须传递云服务器的实例名称，其它未传递字段会设置为默认值。
        :type InstanceNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameSettings`
        :param _EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。
        :type EnhancedService: :class:`tencentcloud.autoscaling.v20180419.models.EnhancedService`
        :param _CamRoleName: CAM角色名称。可通过DescribeRoleList接口返回值中的roleName获取。
        :type CamRoleName: str
        :param _HpcClusterId: 高性能计算集群ID。<br>
注意：此字段默认为空。
        :type HpcClusterId: str
        :param _IPv6InternetAccessible: IPv6公网带宽相关信息设置。若新建实例包含IPv6地址，该参数可为新建实例的IPv6地址分配公网带宽。关联启动配置的伸缩组Ipv6AddressCount参数为0时，该参数不会生效。
        :type IPv6InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.IPv6InternetAccessible`
        :param _DisasterRecoverGroupIds: 置放群组id，仅支持指定一个。
        :type DisasterRecoverGroupIds: list of str
        :param _LoginSettings: 实例登录设置，包括密码、密钥或保持镜像的原始登录设置。<br>请注意，指定新的登录设置会覆盖原有登录设置。例如，如果您之前使用密码登录，使用该参数将登录设置修改为密钥，则原有密码被清除。
        :type LoginSettings: :class:`tencentcloud.autoscaling.v20180419.models.LoginSettings`
        """
        self._LaunchConfigurationId = None
        self._ImageId = None
        self._InstanceTypes = None
        self._InstanceTypesCheckPolicy = None
        self._LaunchConfigurationName = None
        self._UserData = None
        self._SecurityGroupIds = None
        self._InternetAccessible = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._InstanceMarketOptions = None
        self._DiskTypePolicy = None
        self._SystemDisk = None
        self._DataDisks = None
        self._HostNameSettings = None
        self._InstanceNameSettings = None
        self._EnhancedService = None
        self._CamRoleName = None
        self._HpcClusterId = None
        self._IPv6InternetAccessible = None
        self._DisasterRecoverGroupIds = None
        self._LoginSettings = None

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def InstanceTypesCheckPolicy(self):
        return self._InstanceTypesCheckPolicy

    @InstanceTypesCheckPolicy.setter
    def InstanceTypesCheckPolicy(self, InstanceTypesCheckPolicy):
        self._InstanceTypesCheckPolicy = InstanceTypesCheckPolicy

    @property
    def LaunchConfigurationName(self):
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def DiskTypePolicy(self):
        return self._DiskTypePolicy

    @DiskTypePolicy.setter
    def DiskTypePolicy(self, DiskTypePolicy):
        self._DiskTypePolicy = DiskTypePolicy

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def HostNameSettings(self):
        return self._HostNameSettings

    @HostNameSettings.setter
    def HostNameSettings(self, HostNameSettings):
        self._HostNameSettings = HostNameSettings

    @property
    def InstanceNameSettings(self):
        return self._InstanceNameSettings

    @InstanceNameSettings.setter
    def InstanceNameSettings(self, InstanceNameSettings):
        self._InstanceNameSettings = InstanceNameSettings

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HpcClusterId(self):
        return self._HpcClusterId

    @HpcClusterId.setter
    def HpcClusterId(self, HpcClusterId):
        self._HpcClusterId = HpcClusterId

    @property
    def IPv6InternetAccessible(self):
        return self._IPv6InternetAccessible

    @IPv6InternetAccessible.setter
    def IPv6InternetAccessible(self, IPv6InternetAccessible):
        self._IPv6InternetAccessible = IPv6InternetAccessible

    @property
    def DisasterRecoverGroupIds(self):
        return self._DisasterRecoverGroupIds

    @DisasterRecoverGroupIds.setter
    def DisasterRecoverGroupIds(self, DisasterRecoverGroupIds):
        self._DisasterRecoverGroupIds = DisasterRecoverGroupIds

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings


    def _deserialize(self, params):
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._ImageId = params.get("ImageId")
        self._InstanceTypes = params.get("InstanceTypes")
        self._InstanceTypesCheckPolicy = params.get("InstanceTypesCheckPolicy")
        self._LaunchConfigurationName = params.get("LaunchConfigurationName")
        self._UserData = params.get("UserData")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._DiskTypePolicy = params.get("DiskTypePolicy")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("HostNameSettings") is not None:
            self._HostNameSettings = HostNameSettings()
            self._HostNameSettings._deserialize(params.get("HostNameSettings"))
        if params.get("InstanceNameSettings") is not None:
            self._InstanceNameSettings = InstanceNameSettings()
            self._InstanceNameSettings._deserialize(params.get("InstanceNameSettings"))
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._CamRoleName = params.get("CamRoleName")
        self._HpcClusterId = params.get("HpcClusterId")
        if params.get("IPv6InternetAccessible") is not None:
            self._IPv6InternetAccessible = IPv6InternetAccessible()
            self._IPv6InternetAccessible._deserialize(params.get("IPv6InternetAccessible"))
        self._DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
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
        


class ModifyLaunchConfigurationAttributesResponse(AbstractModel):
    """ModifyLaunchConfigurationAttributes返回参数结构体

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


class ModifyLifecycleHookRequest(AbstractModel):
    """ModifyLifecycleHook请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LifecycleHookId: 生命周期挂钩ID。
        :type LifecycleHookId: str
        :param _LifecycleHookName: 生命周期挂钩名称。
        :type LifecycleHookName: str
        :param _LifecycleTransition: 进入生命周期挂钩场景，取值包括：
<li> INSTANCE_LAUNCHING：实例启动后
<li> INSTANCE_TERMINATING：实例销毁前
        :type LifecycleTransition: str
        :param _DefaultResult: 定义伸缩组在生命周期挂钩超时的情况下应采取的操作，取值包括：
<li> CONTINUE： 超时后继续伸缩活动
<li> ABANDON：超时后终止伸缩活动
        :type DefaultResult: str
        :param _HeartbeatTimeout: 生命周期挂钩超时之前可以经过的最长时间（以秒为单位），范围从 30 到 7200 秒。
        :type HeartbeatTimeout: int
        :param _NotificationMetadata: 弹性伸缩向通知目标发送的附加信息。
        :type NotificationMetadata: str
        :param _LifecycleTransitionType: 进行生命周期挂钩的场景类型，取值范围包括`NORMAL`和 `EXTENSION`。说明：设置为`EXTENSION`值，在AttachInstances、DetachInstances、RemoveInstances 接口时会触发生命周期挂钩操作，值为`NORMAL`则不会在这些接口中触发生命周期挂钩。
        :type LifecycleTransitionType: str
        :param _NotificationTarget: 通知目标信息。
        :type NotificationTarget: :class:`tencentcloud.autoscaling.v20180419.models.NotificationTarget`
        :param _LifecycleCommand: 远程命令执行对象。
        :type LifecycleCommand: :class:`tencentcloud.autoscaling.v20180419.models.LifecycleCommand`
        """
        self._LifecycleHookId = None
        self._LifecycleHookName = None
        self._LifecycleTransition = None
        self._DefaultResult = None
        self._HeartbeatTimeout = None
        self._NotificationMetadata = None
        self._LifecycleTransitionType = None
        self._NotificationTarget = None
        self._LifecycleCommand = None

    @property
    def LifecycleHookId(self):
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def LifecycleHookName(self):
        return self._LifecycleHookName

    @LifecycleHookName.setter
    def LifecycleHookName(self, LifecycleHookName):
        self._LifecycleHookName = LifecycleHookName

    @property
    def LifecycleTransition(self):
        return self._LifecycleTransition

    @LifecycleTransition.setter
    def LifecycleTransition(self, LifecycleTransition):
        self._LifecycleTransition = LifecycleTransition

    @property
    def DefaultResult(self):
        return self._DefaultResult

    @DefaultResult.setter
    def DefaultResult(self, DefaultResult):
        self._DefaultResult = DefaultResult

    @property
    def HeartbeatTimeout(self):
        return self._HeartbeatTimeout

    @HeartbeatTimeout.setter
    def HeartbeatTimeout(self, HeartbeatTimeout):
        self._HeartbeatTimeout = HeartbeatTimeout

    @property
    def NotificationMetadata(self):
        return self._NotificationMetadata

    @NotificationMetadata.setter
    def NotificationMetadata(self, NotificationMetadata):
        self._NotificationMetadata = NotificationMetadata

    @property
    def LifecycleTransitionType(self):
        return self._LifecycleTransitionType

    @LifecycleTransitionType.setter
    def LifecycleTransitionType(self, LifecycleTransitionType):
        self._LifecycleTransitionType = LifecycleTransitionType

    @property
    def NotificationTarget(self):
        return self._NotificationTarget

    @NotificationTarget.setter
    def NotificationTarget(self, NotificationTarget):
        self._NotificationTarget = NotificationTarget

    @property
    def LifecycleCommand(self):
        return self._LifecycleCommand

    @LifecycleCommand.setter
    def LifecycleCommand(self, LifecycleCommand):
        self._LifecycleCommand = LifecycleCommand


    def _deserialize(self, params):
        self._LifecycleHookId = params.get("LifecycleHookId")
        self._LifecycleHookName = params.get("LifecycleHookName")
        self._LifecycleTransition = params.get("LifecycleTransition")
        self._DefaultResult = params.get("DefaultResult")
        self._HeartbeatTimeout = params.get("HeartbeatTimeout")
        self._NotificationMetadata = params.get("NotificationMetadata")
        self._LifecycleTransitionType = params.get("LifecycleTransitionType")
        if params.get("NotificationTarget") is not None:
            self._NotificationTarget = NotificationTarget()
            self._NotificationTarget._deserialize(params.get("NotificationTarget"))
        if params.get("LifecycleCommand") is not None:
            self._LifecycleCommand = LifecycleCommand()
            self._LifecycleCommand._deserialize(params.get("LifecycleCommand"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLifecycleHookResponse(AbstractModel):
    """ModifyLifecycleHook返回参数结构体

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


class ModifyLoadBalancerTargetAttributesRequest(AbstractModel):
    """ModifyLoadBalancerTargetAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _ForwardLoadBalancers: 需修改目标规则属性的应用型负载均衡器列表，列表长度上限为100
        :type ForwardLoadBalancers: list of ForwardLoadBalancer
        """
        self._AutoScalingGroupId = None
        self._ForwardLoadBalancers = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ForwardLoadBalancers(self):
        return self._ForwardLoadBalancers

    @ForwardLoadBalancers.setter
    def ForwardLoadBalancers(self, ForwardLoadBalancers):
        self._ForwardLoadBalancers = ForwardLoadBalancers


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        if params.get("ForwardLoadBalancers") is not None:
            self._ForwardLoadBalancers = []
            for item in params.get("ForwardLoadBalancers"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self._ForwardLoadBalancers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerTargetAttributesResponse(AbstractModel):
    """ModifyLoadBalancerTargetAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityId: 伸缩活动ID
        :type ActivityId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class ModifyLoadBalancersRequest(AbstractModel):
    """ModifyLoadBalancers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _LoadBalancerIds: 传统负载均衡器ID列表，目前长度上限为20，LoadBalancerIds 和 ForwardLoadBalancers 二者同时最多只能指定一个
        :type LoadBalancerIds: list of str
        :param _ForwardLoadBalancers: 应用型负载均衡器列表，目前长度上限为100，LoadBalancerIds 和 ForwardLoadBalancers 二者同时最多只能指定一个
        :type ForwardLoadBalancers: list of ForwardLoadBalancer
        :param _LoadBalancersCheckPolicy: 负载均衡器校验策略，取值包括 ALL 和 DIFF，默认取值为 ALL。
<br><li> ALL，所有负载均衡器都合法则通过校验，否则校验报错。
<br><li> DIFF，仅校验负载均衡器参数中实际变化的部分，如果合法则通过校验，否则校验报错。
        :type LoadBalancersCheckPolicy: str
        """
        self._AutoScalingGroupId = None
        self._LoadBalancerIds = None
        self._ForwardLoadBalancers = None
        self._LoadBalancersCheckPolicy = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def LoadBalancerIds(self):
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ForwardLoadBalancers(self):
        return self._ForwardLoadBalancers

    @ForwardLoadBalancers.setter
    def ForwardLoadBalancers(self, ForwardLoadBalancers):
        self._ForwardLoadBalancers = ForwardLoadBalancers

    @property
    def LoadBalancersCheckPolicy(self):
        return self._LoadBalancersCheckPolicy

    @LoadBalancersCheckPolicy.setter
    def LoadBalancersCheckPolicy(self, LoadBalancersCheckPolicy):
        self._LoadBalancersCheckPolicy = LoadBalancersCheckPolicy


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        if params.get("ForwardLoadBalancers") is not None:
            self._ForwardLoadBalancers = []
            for item in params.get("ForwardLoadBalancers"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self._ForwardLoadBalancers.append(obj)
        self._LoadBalancersCheckPolicy = params.get("LoadBalancersCheckPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancersResponse(AbstractModel):
    """ModifyLoadBalancers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityId: 伸缩活动ID
        :type ActivityId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class ModifyNotificationConfigurationRequest(AbstractModel):
    """ModifyNotificationConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingNotificationId: 待修改的通知ID。
        :type AutoScalingNotificationId: str
        :param _NotificationTypes: 通知类型，即为需要订阅的通知类型集合，取值范围如下：
<li>SCALE_OUT_SUCCESSFUL：扩容成功</li>
<li>SCALE_OUT_FAILED：扩容失败</li>
<li>SCALE_IN_SUCCESSFUL：缩容成功</li>
<li>SCALE_IN_FAILED：缩容失败</li>
<li>REPLACE_UNHEALTHY_INSTANCE_SUCCESSFUL：替换不健康子机成功</li>
<li>REPLACE_UNHEALTHY_INSTANCE_FAILED：替换不健康子机失败</li>
        :type NotificationTypes: list of str
        :param _NotificationUserGroupIds: 通知组ID，即为用户组ID集合，用户组ID可以通过[ListGroups](https://cloud.tencent.com/document/product/598/34589)查询。
        :type NotificationUserGroupIds: list of str
        :param _QueueName: CMQ 队列或 TDMQ CMQ 队列名。
        :type QueueName: str
        :param _TopicName: CMQ 主题或 TDMQ CMQ 主题名。
        :type TopicName: str
        """
        self._AutoScalingNotificationId = None
        self._NotificationTypes = None
        self._NotificationUserGroupIds = None
        self._QueueName = None
        self._TopicName = None

    @property
    def AutoScalingNotificationId(self):
        return self._AutoScalingNotificationId

    @AutoScalingNotificationId.setter
    def AutoScalingNotificationId(self, AutoScalingNotificationId):
        self._AutoScalingNotificationId = AutoScalingNotificationId

    @property
    def NotificationTypes(self):
        return self._NotificationTypes

    @NotificationTypes.setter
    def NotificationTypes(self, NotificationTypes):
        self._NotificationTypes = NotificationTypes

    @property
    def NotificationUserGroupIds(self):
        return self._NotificationUserGroupIds

    @NotificationUserGroupIds.setter
    def NotificationUserGroupIds(self, NotificationUserGroupIds):
        self._NotificationUserGroupIds = NotificationUserGroupIds

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._AutoScalingNotificationId = params.get("AutoScalingNotificationId")
        self._NotificationTypes = params.get("NotificationTypes")
        self._NotificationUserGroupIds = params.get("NotificationUserGroupIds")
        self._QueueName = params.get("QueueName")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNotificationConfigurationResponse(AbstractModel):
    """ModifyNotificationConfiguration返回参数结构体

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


class ModifyScalingPolicyRequest(AbstractModel):
    """ModifyScalingPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingPolicyId: 告警策略ID。
        :type AutoScalingPolicyId: str
        :param _ScalingPolicyName: 告警策略名称。
        :type ScalingPolicyName: str
        :param _AdjustmentType: 告警触发后，期望实例数修改方式，仅适用于简单策略。取值范围：<br><li>CHANGE_IN_CAPACITY：增加或减少若干期望实例数</li><li>EXACT_CAPACITY：调整至指定期望实例数</li> <li>PERCENT_CHANGE_IN_CAPACITY：按百分比调整期望实例数</li>
        :type AdjustmentType: str
        :param _AdjustmentValue: 告警触发后，期望实例数的调整值，仅适用于简单策略。<br><li>当 AdjustmentType 为 CHANGE_IN_CAPACITY 时，AdjustmentValue 为正数表示告警触发后增加实例，为负数表示告警触发后减少实例 </li> <li> 当 AdjustmentType 为 EXACT_CAPACITY 时，AdjustmentValue 的值即为告警触发后新的期望实例数，需要大于或等于0 </li> <li> 当 AdjustmentType 为 PERCENT_CHANGE_IN_CAPACITY 时，AdjusmentValue 为正数表示告警触发后按百分比增加实例，为负数表示告警触发后按百分比减少实例，单位是：%。
        :type AdjustmentValue: int
        :param _Cooldown: 冷却时间，仅适用于简单策略，单位为秒。
        :type Cooldown: int
        :param _MetricAlarm: 告警监控指标，仅适用于简单策略。
        :type MetricAlarm: :class:`tencentcloud.autoscaling.v20180419.models.MetricAlarm`
        :param _PredefinedMetricType: 预定义监控项，仅适用于目标追踪策略。取值范围：<br><li>ASG_AVG_CPU_UTILIZATION：平均CPU使用率</li><li>ASG_AVG_LAN_TRAFFIC_OUT：平均内网出带宽</li><li>ASG_AVG_LAN_TRAFFIC_IN：平均内网入带宽</li><li>ASG_AVG_WAN_TRAFFIC_OUT：平均外网出带宽</li><li>ASG_AVG_WAN_TRAFFIC_IN：平均外网出带宽</li>
        :type PredefinedMetricType: str
        :param _TargetValue: 目标值，仅适用于目标追踪策略。<br><li>ASG_AVG_CPU_UTILIZATION：[1, 100)，单位：%</li><li>ASG_AVG_LAN_TRAFFIC_OUT：>0，单位：Mbps</li><li>ASG_AVG_LAN_TRAFFIC_IN：>0，单位：Mbps</li><li>ASG_AVG_WAN_TRAFFIC_OUT：>0，单位：Mbps</li><li>ASG_AVG_WAN_TRAFFIC_IN：>0，单位：Mbps</li>
        :type TargetValue: int
        :param _EstimatedInstanceWarmup: 实例预热时间，单位为秒，仅适用于目标追踪策略。取值范围为0-3600。
        :type EstimatedInstanceWarmup: int
        :param _DisableScaleIn: 是否禁用缩容，仅适用于目标追踪策略。取值范围：<br><li>true：目标追踪策略仅触发扩容</li><li>false：目标追踪策略触发扩容和缩容</li>
        :type DisableScaleIn: bool
        :param _NotificationUserGroupIds: 此参数已不再生效，请使用[创建通知](https://cloud.tencent.com/document/api/377/33185)。
通知组ID，即为用户组ID集合。
        :type NotificationUserGroupIds: list of str
        """
        self._AutoScalingPolicyId = None
        self._ScalingPolicyName = None
        self._AdjustmentType = None
        self._AdjustmentValue = None
        self._Cooldown = None
        self._MetricAlarm = None
        self._PredefinedMetricType = None
        self._TargetValue = None
        self._EstimatedInstanceWarmup = None
        self._DisableScaleIn = None
        self._NotificationUserGroupIds = None

    @property
    def AutoScalingPolicyId(self):
        return self._AutoScalingPolicyId

    @AutoScalingPolicyId.setter
    def AutoScalingPolicyId(self, AutoScalingPolicyId):
        self._AutoScalingPolicyId = AutoScalingPolicyId

    @property
    def ScalingPolicyName(self):
        return self._ScalingPolicyName

    @ScalingPolicyName.setter
    def ScalingPolicyName(self, ScalingPolicyName):
        self._ScalingPolicyName = ScalingPolicyName

    @property
    def AdjustmentType(self):
        return self._AdjustmentType

    @AdjustmentType.setter
    def AdjustmentType(self, AdjustmentType):
        self._AdjustmentType = AdjustmentType

    @property
    def AdjustmentValue(self):
        return self._AdjustmentValue

    @AdjustmentValue.setter
    def AdjustmentValue(self, AdjustmentValue):
        self._AdjustmentValue = AdjustmentValue

    @property
    def Cooldown(self):
        return self._Cooldown

    @Cooldown.setter
    def Cooldown(self, Cooldown):
        self._Cooldown = Cooldown

    @property
    def MetricAlarm(self):
        return self._MetricAlarm

    @MetricAlarm.setter
    def MetricAlarm(self, MetricAlarm):
        self._MetricAlarm = MetricAlarm

    @property
    def PredefinedMetricType(self):
        return self._PredefinedMetricType

    @PredefinedMetricType.setter
    def PredefinedMetricType(self, PredefinedMetricType):
        self._PredefinedMetricType = PredefinedMetricType

    @property
    def TargetValue(self):
        return self._TargetValue

    @TargetValue.setter
    def TargetValue(self, TargetValue):
        self._TargetValue = TargetValue

    @property
    def EstimatedInstanceWarmup(self):
        return self._EstimatedInstanceWarmup

    @EstimatedInstanceWarmup.setter
    def EstimatedInstanceWarmup(self, EstimatedInstanceWarmup):
        self._EstimatedInstanceWarmup = EstimatedInstanceWarmup

    @property
    def DisableScaleIn(self):
        return self._DisableScaleIn

    @DisableScaleIn.setter
    def DisableScaleIn(self, DisableScaleIn):
        self._DisableScaleIn = DisableScaleIn

    @property
    def NotificationUserGroupIds(self):
        return self._NotificationUserGroupIds

    @NotificationUserGroupIds.setter
    def NotificationUserGroupIds(self, NotificationUserGroupIds):
        self._NotificationUserGroupIds = NotificationUserGroupIds


    def _deserialize(self, params):
        self._AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        self._ScalingPolicyName = params.get("ScalingPolicyName")
        self._AdjustmentType = params.get("AdjustmentType")
        self._AdjustmentValue = params.get("AdjustmentValue")
        self._Cooldown = params.get("Cooldown")
        if params.get("MetricAlarm") is not None:
            self._MetricAlarm = MetricAlarm()
            self._MetricAlarm._deserialize(params.get("MetricAlarm"))
        self._PredefinedMetricType = params.get("PredefinedMetricType")
        self._TargetValue = params.get("TargetValue")
        self._EstimatedInstanceWarmup = params.get("EstimatedInstanceWarmup")
        self._DisableScaleIn = params.get("DisableScaleIn")
        self._NotificationUserGroupIds = params.get("NotificationUserGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyScalingPolicyResponse(AbstractModel):
    """ModifyScalingPolicy返回参数结构体

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


class ModifyScheduledActionRequest(AbstractModel):
    """ModifyScheduledAction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ScheduledActionId: 待修改的定时任务ID
        :type ScheduledActionId: str
        :param _ScheduledActionName: 定时任务名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。同一伸缩组下必须唯一。
        :type ScheduledActionName: str
        :param _MaxSize: 当定时任务触发时，设置的伸缩组最大实例数。
        :type MaxSize: int
        :param _MinSize: 当定时任务触发时，设置的伸缩组最小实例数。
        :type MinSize: int
        :param _DesiredCapacity: 当定时任务触发时，设置的伸缩组期望实例数。
        :type DesiredCapacity: int
        :param _StartTime: 定时任务的首次触发时间，取值为`北京时间`（UTC+8），按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ss+08:00`。
        :type StartTime: str
        :param _EndTime: 定时任务的结束时间，取值为`北京时间`（UTC+8），按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ss+08:00`。<br>此参数与`Recurrence`需要同时指定，到达结束时间之后，定时任务将不再生效。
        :type EndTime: str
        :param _Recurrence: 定时任务的重复方式。为标准 Cron 格式<br>此参数与`EndTime`需要同时指定。
        :type Recurrence: str
        """
        self._ScheduledActionId = None
        self._ScheduledActionName = None
        self._MaxSize = None
        self._MinSize = None
        self._DesiredCapacity = None
        self._StartTime = None
        self._EndTime = None
        self._Recurrence = None

    @property
    def ScheduledActionId(self):
        return self._ScheduledActionId

    @ScheduledActionId.setter
    def ScheduledActionId(self, ScheduledActionId):
        self._ScheduledActionId = ScheduledActionId

    @property
    def ScheduledActionName(self):
        return self._ScheduledActionName

    @ScheduledActionName.setter
    def ScheduledActionName(self, ScheduledActionName):
        self._ScheduledActionName = ScheduledActionName

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def DesiredCapacity(self):
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Recurrence(self):
        return self._Recurrence

    @Recurrence.setter
    def Recurrence(self, Recurrence):
        self._Recurrence = Recurrence


    def _deserialize(self, params):
        self._ScheduledActionId = params.get("ScheduledActionId")
        self._ScheduledActionName = params.get("ScheduledActionName")
        self._MaxSize = params.get("MaxSize")
        self._MinSize = params.get("MinSize")
        self._DesiredCapacity = params.get("DesiredCapacity")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Recurrence = params.get("Recurrence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyScheduledActionResponse(AbstractModel):
    """ModifyScheduledAction返回参数结构体

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


class NotificationTarget(AbstractModel):
    """通知目标

    """

    def __init__(self):
        r"""
        :param _TargetType: 目标类型，取值范围包括`CMQ_QUEUE`、`CMQ_TOPIC`、`TDMQ_CMQ_QUEUE`、`TDMQ_CMQ_TOPIC`。
<li> CMQ_QUEUE，指腾讯云消息队列-队列模型。</li>
<li> CMQ_TOPIC，指腾讯云消息队列-主题模型。</li>
<li> TDMQ_CMQ_QUEUE，指腾讯云 TDMQ 消息队列-队列模型。</li>
<li> TDMQ_CMQ_TOPIC，指腾讯云 TDMQ 消息队列-主题模型。</li>
        :type TargetType: str
        :param _QueueName: 队列名称，如果`TargetType`取值为`CMQ_QUEUE` 或 `TDMQ_CMQ_QUEUE`，则本字段必填。
        :type QueueName: str
        :param _TopicName: 主题名称，如果`TargetType`取值为`CMQ_TOPIC` 或 `TDMQ_CMQ_TOPIC`，则本字段必填。
        :type TopicName: str
        """
        self._TargetType = None
        self._QueueName = None
        self._TopicName = None

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._TargetType = params.get("TargetType")
        self._QueueName = params.get("QueueName")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefreshActivity(AbstractModel):
    """实例刷新活动。

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组 ID。
        :type AutoScalingGroupId: str
        :param _RefreshActivityId: 刷新活动 ID。
        :type RefreshActivityId: str
        :param _OriginRefreshActivityId: 原始刷新活动ID，仅在回滚刷新活动中存在。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginRefreshActivityId: str
        :param _RefreshBatchSet: 刷新批次信息列表。
        :type RefreshBatchSet: list of RefreshBatch
        :param _RefreshMode: 刷新模式。
        :type RefreshMode: str
        :param _RefreshSettings: 实例更新设置参数。
        :type RefreshSettings: :class:`tencentcloud.autoscaling.v20180419.models.RefreshSettings`
        :param _ActivityType: 刷新活动类型。取值如下：<br><li>NORMAL：正常刷新活动</li><li>ROLLBACK：回滚刷新活动
        :type ActivityType: str
        :param _Status: 刷新活动状态。取值如下：<br><li>INIT：初始化中</li><li>RUNNING：运行中</li><li>SUCCESSFUL：活动成功</li><li>FAILED_PAUSE：因刷新批次失败暂停</li><li>AUTO_PAUSE：因暂停策略自动暂停</li><li>MANUAL_PAUSE：手动暂停</li><li>CANCELLED：活动取消</li><li>FAILED：活动失败
        :type Status: str
        :param _CurrentRefreshBatchNum: 当前刷新批次序号。例如，2 表示当前活动正在刷新第二批次的实例。
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentRefreshBatchNum: int
        :param _StartTime: 刷新活动开始时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 刷新活动结束时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _CreatedTime: 刷新活动创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        """
        self._AutoScalingGroupId = None
        self._RefreshActivityId = None
        self._OriginRefreshActivityId = None
        self._RefreshBatchSet = None
        self._RefreshMode = None
        self._RefreshSettings = None
        self._ActivityType = None
        self._Status = None
        self._CurrentRefreshBatchNum = None
        self._StartTime = None
        self._EndTime = None
        self._CreatedTime = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RefreshActivityId(self):
        return self._RefreshActivityId

    @RefreshActivityId.setter
    def RefreshActivityId(self, RefreshActivityId):
        self._RefreshActivityId = RefreshActivityId

    @property
    def OriginRefreshActivityId(self):
        return self._OriginRefreshActivityId

    @OriginRefreshActivityId.setter
    def OriginRefreshActivityId(self, OriginRefreshActivityId):
        self._OriginRefreshActivityId = OriginRefreshActivityId

    @property
    def RefreshBatchSet(self):
        return self._RefreshBatchSet

    @RefreshBatchSet.setter
    def RefreshBatchSet(self, RefreshBatchSet):
        self._RefreshBatchSet = RefreshBatchSet

    @property
    def RefreshMode(self):
        return self._RefreshMode

    @RefreshMode.setter
    def RefreshMode(self, RefreshMode):
        self._RefreshMode = RefreshMode

    @property
    def RefreshSettings(self):
        return self._RefreshSettings

    @RefreshSettings.setter
    def RefreshSettings(self, RefreshSettings):
        self._RefreshSettings = RefreshSettings

    @property
    def ActivityType(self):
        return self._ActivityType

    @ActivityType.setter
    def ActivityType(self, ActivityType):
        self._ActivityType = ActivityType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CurrentRefreshBatchNum(self):
        return self._CurrentRefreshBatchNum

    @CurrentRefreshBatchNum.setter
    def CurrentRefreshBatchNum(self, CurrentRefreshBatchNum):
        self._CurrentRefreshBatchNum = CurrentRefreshBatchNum

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._RefreshActivityId = params.get("RefreshActivityId")
        self._OriginRefreshActivityId = params.get("OriginRefreshActivityId")
        if params.get("RefreshBatchSet") is not None:
            self._RefreshBatchSet = []
            for item in params.get("RefreshBatchSet"):
                obj = RefreshBatch()
                obj._deserialize(item)
                self._RefreshBatchSet.append(obj)
        self._RefreshMode = params.get("RefreshMode")
        if params.get("RefreshSettings") is not None:
            self._RefreshSettings = RefreshSettings()
            self._RefreshSettings._deserialize(params.get("RefreshSettings"))
        self._ActivityType = params.get("ActivityType")
        self._Status = params.get("Status")
        self._CurrentRefreshBatchNum = params.get("CurrentRefreshBatchNum")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefreshBatch(AbstractModel):
    """实例刷新批次信息，包含该批次的刷新状态、实例、起止时间等信息。

    """

    def __init__(self):
        r"""
        :param _RefreshBatchNum: 刷新批次序号。例如，2 表示当前批次实例会在第二批次进行实例刷新。
        :type RefreshBatchNum: int
        :param _RefreshBatchStatus: 刷新批次状态。取值如下：<br><li>WAITING：待刷新</li><li>INIT：初始化中</li><li>RUNNING：刷新中</li><li>FAILED:  刷新失败</li><li>PARTIALLY_SUCCESSFUL：批次部分成功</li><li>CANCELLED：已取消</li><li>SUCCESSFUL：刷新成功
        :type RefreshBatchStatus: str
        :param _RefreshBatchRelatedInstanceSet: 刷新批次关联实例列表。
        :type RefreshBatchRelatedInstanceSet: list of RefreshBatchRelatedInstance
        :param _StartTime: 刷新批次开始时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 刷新批次结束时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self._RefreshBatchNum = None
        self._RefreshBatchStatus = None
        self._RefreshBatchRelatedInstanceSet = None
        self._StartTime = None
        self._EndTime = None

    @property
    def RefreshBatchNum(self):
        return self._RefreshBatchNum

    @RefreshBatchNum.setter
    def RefreshBatchNum(self, RefreshBatchNum):
        self._RefreshBatchNum = RefreshBatchNum

    @property
    def RefreshBatchStatus(self):
        return self._RefreshBatchStatus

    @RefreshBatchStatus.setter
    def RefreshBatchStatus(self, RefreshBatchStatus):
        self._RefreshBatchStatus = RefreshBatchStatus

    @property
    def RefreshBatchRelatedInstanceSet(self):
        return self._RefreshBatchRelatedInstanceSet

    @RefreshBatchRelatedInstanceSet.setter
    def RefreshBatchRelatedInstanceSet(self, RefreshBatchRelatedInstanceSet):
        self._RefreshBatchRelatedInstanceSet = RefreshBatchRelatedInstanceSet

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._RefreshBatchNum = params.get("RefreshBatchNum")
        self._RefreshBatchStatus = params.get("RefreshBatchStatus")
        if params.get("RefreshBatchRelatedInstanceSet") is not None:
            self._RefreshBatchRelatedInstanceSet = []
            for item in params.get("RefreshBatchRelatedInstanceSet"):
                obj = RefreshBatchRelatedInstance()
                obj._deserialize(item)
                self._RefreshBatchRelatedInstanceSet.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefreshBatchRelatedInstance(AbstractModel):
    """刷新批次关联实例，包含单个实例的刷新活动状态、对应伸缩活动等信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID。
        :type InstanceId: str
        :param _InstanceStatus: 刷新实例状态。如果在刷新时实例被移出或销毁，状态会更新为 NOT_FOUND。取值如下：<br><li>WAITING：待刷新</li><li>INIT：初始化中</li><li>RUNNING：刷新中</li><li>FAILED：刷新失败</li><li>CANCELLED：已取消</li><li>SUCCESSFUL：刷新成功</li><li>NOT_FOUND：实例不存在
        :type InstanceStatus: str
        :param _LastActivityId: 实例刷新中最近一次伸缩活动 ID，可通过 DescribeAutoScalingActivities 接口查询。
需注意伸缩活动与实例刷新活动不同，一次实例刷新活动可能包括多次伸缩活动。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastActivityId: str
        :param _InstanceStatusMessage: 实例刷新状态信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStatusMessage: str
        """
        self._InstanceId = None
        self._InstanceStatus = None
        self._LastActivityId = None
        self._InstanceStatusMessage = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def LastActivityId(self):
        return self._LastActivityId

    @LastActivityId.setter
    def LastActivityId(self, LastActivityId):
        self._LastActivityId = LastActivityId

    @property
    def InstanceStatusMessage(self):
        return self._InstanceStatusMessage

    @InstanceStatusMessage.setter
    def InstanceStatusMessage(self, InstanceStatusMessage):
        self._InstanceStatusMessage = InstanceStatusMessage


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceStatus = params.get("InstanceStatus")
        self._LastActivityId = params.get("LastActivityId")
        self._InstanceStatusMessage = params.get("InstanceStatusMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefreshSettings(AbstractModel):
    """实例刷新设置。

    """

    def __init__(self):
        r"""
        :param _RollingUpdateSettings: 滚动更新设置参数。RefreshMode 为滚动更新该参数必须填写。
注意：此字段可能返回 null，表示取不到有效值。
        :type RollingUpdateSettings: :class:`tencentcloud.autoscaling.v20180419.models.RollingUpdateSettings`
        :param _CheckInstanceTargetHealth: 实例后端服务健康状态检查，默认为 FALSE。仅针对绑定应用型负载均衡器的伸缩组生效，开启该检查后，如刷新后实例未通过检查，负载均衡器端口权重始终为 0，且标记为刷新失败。取值范围如下：<br><li>TRUE：开启检查</li><li>FALSE：不开启检查
        :type CheckInstanceTargetHealth: bool
        """
        self._RollingUpdateSettings = None
        self._CheckInstanceTargetHealth = None

    @property
    def RollingUpdateSettings(self):
        return self._RollingUpdateSettings

    @RollingUpdateSettings.setter
    def RollingUpdateSettings(self, RollingUpdateSettings):
        self._RollingUpdateSettings = RollingUpdateSettings

    @property
    def CheckInstanceTargetHealth(self):
        return self._CheckInstanceTargetHealth

    @CheckInstanceTargetHealth.setter
    def CheckInstanceTargetHealth(self, CheckInstanceTargetHealth):
        self._CheckInstanceTargetHealth = CheckInstanceTargetHealth


    def _deserialize(self, params):
        if params.get("RollingUpdateSettings") is not None:
            self._RollingUpdateSettings = RollingUpdateSettings()
            self._RollingUpdateSettings._deserialize(params.get("RollingUpdateSettings"))
        self._CheckInstanceTargetHealth = params.get("CheckInstanceTargetHealth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelatedInstance(AbstractModel):
    """与本次伸缩活动相关的实例信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _InstanceStatus: 实例在伸缩活动中的状态。取值如下：
INIT：初始化中
RUNNING：实例操作中
SUCCESSFUL：活动成功
FAILED：活动失败
        :type InstanceStatus: str
        """
        self._InstanceId = None
        self._InstanceStatus = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceStatus = params.get("InstanceStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveInstancesRequest(AbstractModel):
    """RemoveInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _InstanceIds: CVM实例ID列表
        :type InstanceIds: list of str
        """
        self._AutoScalingGroupId = None
        self._InstanceIds = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveInstancesResponse(AbstractModel):
    """RemoveInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityId: 伸缩活动ID
        :type ActivityId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class ResumeInstanceRefreshRequest(AbstractModel):
    """ResumeInstanceRefresh请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID。
        :type AutoScalingGroupId: str
        :param _RefreshActivityId: 刷新活动ID。
        :type RefreshActivityId: str
        :param _ResumeMode: 当前批次刷新失败实例的恢复方式，如不存在失败实例，该参数无效。默认值为RETRY，取值范围如下：<br><li>RETRY: 重试当前批次刷新失败实例</li><li>CONTINUE: 跳过当前批次刷新失败实例
        :type ResumeMode: str
        """
        self._AutoScalingGroupId = None
        self._RefreshActivityId = None
        self._ResumeMode = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RefreshActivityId(self):
        return self._RefreshActivityId

    @RefreshActivityId.setter
    def RefreshActivityId(self, RefreshActivityId):
        self._RefreshActivityId = RefreshActivityId

    @property
    def ResumeMode(self):
        return self._ResumeMode

    @ResumeMode.setter
    def ResumeMode(self, ResumeMode):
        self._ResumeMode = ResumeMode


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._RefreshActivityId = params.get("RefreshActivityId")
        self._ResumeMode = params.get("ResumeMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeInstanceRefreshResponse(AbstractModel):
    """ResumeInstanceRefresh返回参数结构体

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


class RollbackInstanceRefreshRequest(AbstractModel):
    """RollbackInstanceRefresh请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID。
        :type AutoScalingGroupId: str
        :param _RefreshSettings: 刷新设置。
        :type RefreshSettings: :class:`tencentcloud.autoscaling.v20180419.models.RefreshSettings`
        :param _OriginRefreshActivityId: 原始刷新活动 ID。
        :type OriginRefreshActivityId: str
        :param _RefreshMode: 刷新模式，目前仅支持滚动更新，默认值为 ROLLING_UPDATE_RESET。
        :type RefreshMode: str
        """
        self._AutoScalingGroupId = None
        self._RefreshSettings = None
        self._OriginRefreshActivityId = None
        self._RefreshMode = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RefreshSettings(self):
        return self._RefreshSettings

    @RefreshSettings.setter
    def RefreshSettings(self, RefreshSettings):
        self._RefreshSettings = RefreshSettings

    @property
    def OriginRefreshActivityId(self):
        return self._OriginRefreshActivityId

    @OriginRefreshActivityId.setter
    def OriginRefreshActivityId(self, OriginRefreshActivityId):
        self._OriginRefreshActivityId = OriginRefreshActivityId

    @property
    def RefreshMode(self):
        return self._RefreshMode

    @RefreshMode.setter
    def RefreshMode(self, RefreshMode):
        self._RefreshMode = RefreshMode


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        if params.get("RefreshSettings") is not None:
            self._RefreshSettings = RefreshSettings()
            self._RefreshSettings._deserialize(params.get("RefreshSettings"))
        self._OriginRefreshActivityId = params.get("OriginRefreshActivityId")
        self._RefreshMode = params.get("RefreshMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackInstanceRefreshResponse(AbstractModel):
    """RollbackInstanceRefresh返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RefreshActivityId: 刷新活动 ID。
        :type RefreshActivityId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RefreshActivityId = None
        self._RequestId = None

    @property
    def RefreshActivityId(self):
        return self._RefreshActivityId

    @RefreshActivityId.setter
    def RefreshActivityId(self, RefreshActivityId):
        self._RefreshActivityId = RefreshActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RefreshActivityId = params.get("RefreshActivityId")
        self._RequestId = params.get("RequestId")


class RollingUpdateSettings(AbstractModel):
    """滚动更新设置。

    """

    def __init__(self):
        r"""
        :param _BatchNumber: 批次数量。批次数量为大于 0 的正整数，但不能大于待刷新实例数量。
        :type BatchNumber: int
        :param _BatchPause: 批次间暂停策略。默认值为 Automatic，取值范围如下：<br><li>FIRST_BATCH_PAUSE：第一批次更新完成后暂停</li><li>BATCH_INTERVAL_PAUSE：批次间暂停</li><li>AUTOMATIC：不暂停
        :type BatchPause: str
        """
        self._BatchNumber = None
        self._BatchPause = None

    @property
    def BatchNumber(self):
        return self._BatchNumber

    @BatchNumber.setter
    def BatchNumber(self, BatchNumber):
        self._BatchNumber = BatchNumber

    @property
    def BatchPause(self):
        return self._BatchPause

    @BatchPause.setter
    def BatchPause(self, BatchPause):
        self._BatchPause = BatchPause


    def _deserialize(self, params):
        self._BatchNumber = params.get("BatchNumber")
        self._BatchPause = params.get("BatchPause")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunAutomationServiceEnabled(AbstractModel):
    """描述了 “自动化助手” 服务相关的信息

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启[自动化助手](https://cloud.tencent.com/document/product/1340)服务。取值范围：<br><li>TRUE：表示开启自动化助手服务<br><li>FALSE：表示不开启自动化助手服务
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
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
    """描述了 “云监控” 服务相关的信息。

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启[云监控](https://cloud.tencent.com/document/product/248)服务。取值范围：<br><li>TRUE：表示开启云监控服务<br><li>FALSE：表示不开启云监控服务<br><br>默认取值：TRUE。
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
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
    """描述了 “云安全” 服务相关的信息

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启[云安全](https://cloud.tencent.com/document/product/296)服务。取值范围：<br><li>TRUE：表示开启云安全服务<br><li>FALSE：表示不开启云安全服务<br><br>默认取值：TRUE。
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
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
        


class ScaleInInstancesRequest(AbstractModel):
    """ScaleInInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID。
        :type AutoScalingGroupId: str
        :param _ScaleInNumber: 希望缩容的实例数量。
        :type ScaleInNumber: int
        """
        self._AutoScalingGroupId = None
        self._ScaleInNumber = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ScaleInNumber(self):
        return self._ScaleInNumber

    @ScaleInNumber.setter
    def ScaleInNumber(self, ScaleInNumber):
        self._ScaleInNumber = ScaleInNumber


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._ScaleInNumber = params.get("ScaleInNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleInInstancesResponse(AbstractModel):
    """ScaleInInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityId: 伸缩活动ID。
        :type ActivityId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class ScaleOutInstancesRequest(AbstractModel):
    """ScaleOutInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID。
        :type AutoScalingGroupId: str
        :param _ScaleOutNumber: 希望扩容的实例数量。
        :type ScaleOutNumber: int
        """
        self._AutoScalingGroupId = None
        self._ScaleOutNumber = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def ScaleOutNumber(self):
        return self._ScaleOutNumber

    @ScaleOutNumber.setter
    def ScaleOutNumber(self, ScaleOutNumber):
        self._ScaleOutNumber = ScaleOutNumber


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._ScaleOutNumber = params.get("ScaleOutNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutInstancesResponse(AbstractModel):
    """ScaleOutInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityId: 伸缩活动ID。
        :type ActivityId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class ScalingPolicy(AbstractModel):
    """告警触发策略。

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID。
        :type AutoScalingGroupId: str
        :param _AutoScalingPolicyId: 告警触发策略ID。
        :type AutoScalingPolicyId: str
        :param _ScalingPolicyType: 告警触发策略类型。取值：
- SIMPLE：简单策略
- TARGET_TRACKING：目标追踪策略
        :type ScalingPolicyType: str
        :param _ScalingPolicyName: 告警触发策略名称。
        :type ScalingPolicyName: str
        :param _AdjustmentType: 告警触发后，期望实例数修改方式，仅适用于简单策略。取值范围：<br><li>CHANGE_IN_CAPACITY：增加或减少若干期望实例数</li><li>EXACT_CAPACITY：调整至指定期望实例数</li> <li>PERCENT_CHANGE_IN_CAPACITY：按百分比调整期望实例数</li>
        :type AdjustmentType: str
        :param _AdjustmentValue: 告警触发后，期望实例数的调整值，仅适用于简单策略。
        :type AdjustmentValue: int
        :param _Cooldown: 冷却时间，仅适用于简单策略。
        :type Cooldown: int
        :param _MetricAlarm: 简单告警触发策略告警监控指标，仅适用于简单策略。
        :type MetricAlarm: :class:`tencentcloud.autoscaling.v20180419.models.MetricAlarm`
        :param _PredefinedMetricType: 预定义监控项，仅适用于目标追踪策略。取值范围：<br><li>ASG_AVG_CPU_UTILIZATION：平均CPU使用率</li><li>ASG_AVG_LAN_TRAFFIC_OUT：平均内网出带宽</li><li>ASG_AVG_LAN_TRAFFIC_IN：平均内网入带宽</li><li>ASG_AVG_WAN_TRAFFIC_OUT：平均外网出带宽</li><li>ASG_AVG_WAN_TRAFFIC_IN：平均外网出带宽</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type PredefinedMetricType: str
        :param _TargetValue: 目标值，仅适用于目标追踪策略。<br><li>ASG_AVG_CPU_UTILIZATION：[1, 100)，单位：%</li><li>ASG_AVG_LAN_TRAFFIC_OUT：>0，单位：Mbps</li><li>ASG_AVG_LAN_TRAFFIC_IN：>0，单位：Mbps</li><li>ASG_AVG_WAN_TRAFFIC_OUT：>0，单位：Mbps</li><li>ASG_AVG_WAN_TRAFFIC_IN：>0，单位：Mbps</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetValue: int
        :param _EstimatedInstanceWarmup: 实例预热时间，单位为秒，仅适用于目标追踪策略。取值范围为0-3600。
注意：此字段可能返回 null，表示取不到有效值。
        :type EstimatedInstanceWarmup: int
        :param _DisableScaleIn: 是否禁用缩容，仅适用于目标追踪策略。取值范围：<br><li>true：目标追踪策略仅触发扩容</li><li>false：目标追踪策略触发扩容和缩容</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type DisableScaleIn: bool
        :param _MetricAlarms: 告警监控指标列表，仅适用于目标追踪策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricAlarms: list of MetricAlarm
        :param _NotificationUserGroupIds: 通知组ID，即为用户组ID集合。
        :type NotificationUserGroupIds: list of str
        """
        self._AutoScalingGroupId = None
        self._AutoScalingPolicyId = None
        self._ScalingPolicyType = None
        self._ScalingPolicyName = None
        self._AdjustmentType = None
        self._AdjustmentValue = None
        self._Cooldown = None
        self._MetricAlarm = None
        self._PredefinedMetricType = None
        self._TargetValue = None
        self._EstimatedInstanceWarmup = None
        self._DisableScaleIn = None
        self._MetricAlarms = None
        self._NotificationUserGroupIds = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def AutoScalingPolicyId(self):
        return self._AutoScalingPolicyId

    @AutoScalingPolicyId.setter
    def AutoScalingPolicyId(self, AutoScalingPolicyId):
        self._AutoScalingPolicyId = AutoScalingPolicyId

    @property
    def ScalingPolicyType(self):
        return self._ScalingPolicyType

    @ScalingPolicyType.setter
    def ScalingPolicyType(self, ScalingPolicyType):
        self._ScalingPolicyType = ScalingPolicyType

    @property
    def ScalingPolicyName(self):
        return self._ScalingPolicyName

    @ScalingPolicyName.setter
    def ScalingPolicyName(self, ScalingPolicyName):
        self._ScalingPolicyName = ScalingPolicyName

    @property
    def AdjustmentType(self):
        return self._AdjustmentType

    @AdjustmentType.setter
    def AdjustmentType(self, AdjustmentType):
        self._AdjustmentType = AdjustmentType

    @property
    def AdjustmentValue(self):
        return self._AdjustmentValue

    @AdjustmentValue.setter
    def AdjustmentValue(self, AdjustmentValue):
        self._AdjustmentValue = AdjustmentValue

    @property
    def Cooldown(self):
        return self._Cooldown

    @Cooldown.setter
    def Cooldown(self, Cooldown):
        self._Cooldown = Cooldown

    @property
    def MetricAlarm(self):
        return self._MetricAlarm

    @MetricAlarm.setter
    def MetricAlarm(self, MetricAlarm):
        self._MetricAlarm = MetricAlarm

    @property
    def PredefinedMetricType(self):
        return self._PredefinedMetricType

    @PredefinedMetricType.setter
    def PredefinedMetricType(self, PredefinedMetricType):
        self._PredefinedMetricType = PredefinedMetricType

    @property
    def TargetValue(self):
        return self._TargetValue

    @TargetValue.setter
    def TargetValue(self, TargetValue):
        self._TargetValue = TargetValue

    @property
    def EstimatedInstanceWarmup(self):
        return self._EstimatedInstanceWarmup

    @EstimatedInstanceWarmup.setter
    def EstimatedInstanceWarmup(self, EstimatedInstanceWarmup):
        self._EstimatedInstanceWarmup = EstimatedInstanceWarmup

    @property
    def DisableScaleIn(self):
        return self._DisableScaleIn

    @DisableScaleIn.setter
    def DisableScaleIn(self, DisableScaleIn):
        self._DisableScaleIn = DisableScaleIn

    @property
    def MetricAlarms(self):
        return self._MetricAlarms

    @MetricAlarms.setter
    def MetricAlarms(self, MetricAlarms):
        self._MetricAlarms = MetricAlarms

    @property
    def NotificationUserGroupIds(self):
        return self._NotificationUserGroupIds

    @NotificationUserGroupIds.setter
    def NotificationUserGroupIds(self, NotificationUserGroupIds):
        self._NotificationUserGroupIds = NotificationUserGroupIds


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        self._ScalingPolicyType = params.get("ScalingPolicyType")
        self._ScalingPolicyName = params.get("ScalingPolicyName")
        self._AdjustmentType = params.get("AdjustmentType")
        self._AdjustmentValue = params.get("AdjustmentValue")
        self._Cooldown = params.get("Cooldown")
        if params.get("MetricAlarm") is not None:
            self._MetricAlarm = MetricAlarm()
            self._MetricAlarm._deserialize(params.get("MetricAlarm"))
        self._PredefinedMetricType = params.get("PredefinedMetricType")
        self._TargetValue = params.get("TargetValue")
        self._EstimatedInstanceWarmup = params.get("EstimatedInstanceWarmup")
        self._DisableScaleIn = params.get("DisableScaleIn")
        if params.get("MetricAlarms") is not None:
            self._MetricAlarms = []
            for item in params.get("MetricAlarms"):
                obj = MetricAlarm()
                obj._deserialize(item)
                self._MetricAlarms.append(obj)
        self._NotificationUserGroupIds = params.get("NotificationUserGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduledAction(AbstractModel):
    """描述定时任务的信息

    """

    def __init__(self):
        r"""
        :param _ScheduledActionId: 定时任务ID。
        :type ScheduledActionId: str
        :param _ScheduledActionName: 定时任务名称。
        :type ScheduledActionName: str
        :param _AutoScalingGroupId: 定时任务所在伸缩组ID。
        :type AutoScalingGroupId: str
        :param _StartTime: 定时任务的开始时间。取值为`北京时间`（UTC+8），按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ss+08:00`。
        :type StartTime: str
        :param _Recurrence: 定时任务的重复方式。
        :type Recurrence: str
        :param _EndTime: 定时任务的结束时间。取值为`北京时间`（UTC+8），按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ss+08:00`。
        :type EndTime: str
        :param _MaxSize: 定时任务设置的最大实例数。
        :type MaxSize: int
        :param _DesiredCapacity: 定时任务设置的期望实例数。
        :type DesiredCapacity: int
        :param _MinSize: 定时任务设置的最小实例数。
        :type MinSize: int
        :param _CreatedTime: 定时任务的创建时间。取值为`UTC`时间，按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ssZ`。
        :type CreatedTime: str
        :param _ScheduledType: 定时任务的执行类型。取值范围：<br><li>CRONTAB：代表定时任务为重复执行。<br><li>ONCE：代表定时任务为单次执行。
        :type ScheduledType: str
        """
        self._ScheduledActionId = None
        self._ScheduledActionName = None
        self._AutoScalingGroupId = None
        self._StartTime = None
        self._Recurrence = None
        self._EndTime = None
        self._MaxSize = None
        self._DesiredCapacity = None
        self._MinSize = None
        self._CreatedTime = None
        self._ScheduledType = None

    @property
    def ScheduledActionId(self):
        return self._ScheduledActionId

    @ScheduledActionId.setter
    def ScheduledActionId(self, ScheduledActionId):
        self._ScheduledActionId = ScheduledActionId

    @property
    def ScheduledActionName(self):
        return self._ScheduledActionName

    @ScheduledActionName.setter
    def ScheduledActionName(self, ScheduledActionName):
        self._ScheduledActionName = ScheduledActionName

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Recurrence(self):
        return self._Recurrence

    @Recurrence.setter
    def Recurrence(self, Recurrence):
        self._Recurrence = Recurrence

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def DesiredCapacity(self):
        return self._DesiredCapacity

    @DesiredCapacity.setter
    def DesiredCapacity(self, DesiredCapacity):
        self._DesiredCapacity = DesiredCapacity

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ScheduledType(self):
        return self._ScheduledType

    @ScheduledType.setter
    def ScheduledType(self, ScheduledType):
        self._ScheduledType = ScheduledType


    def _deserialize(self, params):
        self._ScheduledActionId = params.get("ScheduledActionId")
        self._ScheduledActionName = params.get("ScheduledActionName")
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._StartTime = params.get("StartTime")
        self._Recurrence = params.get("Recurrence")
        self._EndTime = params.get("EndTime")
        self._MaxSize = params.get("MaxSize")
        self._DesiredCapacity = params.get("DesiredCapacity")
        self._MinSize = params.get("MinSize")
        self._CreatedTime = params.get("CreatedTime")
        self._ScheduledType = params.get("ScheduledType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceSettings(AbstractModel):
    """服务设置

    """

    def __init__(self):
        r"""
        :param _ReplaceMonitorUnhealthy: 开启监控不健康替换服务。若开启则对于云监控标记为不健康的实例，弹性伸缩服务会进行替换。若不指定该参数，则默认为 False。
        :type ReplaceMonitorUnhealthy: bool
        :param _ScalingMode: 取值范围： 
CLASSIC_SCALING：经典方式，使用创建、销毁实例来实现扩缩容； 
WAKE_UP_STOPPED_SCALING：扩容优先开机。扩容时优先对已关机的实例执行开机操作，若开机后实例数仍低于期望实例数，则创建实例，缩容仍采用销毁实例的方式。用户可以使用StopAutoScalingInstances接口来关闭伸缩组内的实例。监控告警触发的扩容仍将创建实例
默认取值：CLASSIC_SCALING
        :type ScalingMode: str
        :param _ReplaceLoadBalancerUnhealthy: 开启负载均衡不健康替换服务。若开启则对于负载均衡健康检查判断不健康的实例，弹性伸缩服务会进行替换。若不指定该参数，则默认为 False。
        :type ReplaceLoadBalancerUnhealthy: bool
        """
        self._ReplaceMonitorUnhealthy = None
        self._ScalingMode = None
        self._ReplaceLoadBalancerUnhealthy = None

    @property
    def ReplaceMonitorUnhealthy(self):
        return self._ReplaceMonitorUnhealthy

    @ReplaceMonitorUnhealthy.setter
    def ReplaceMonitorUnhealthy(self, ReplaceMonitorUnhealthy):
        self._ReplaceMonitorUnhealthy = ReplaceMonitorUnhealthy

    @property
    def ScalingMode(self):
        return self._ScalingMode

    @ScalingMode.setter
    def ScalingMode(self, ScalingMode):
        self._ScalingMode = ScalingMode

    @property
    def ReplaceLoadBalancerUnhealthy(self):
        return self._ReplaceLoadBalancerUnhealthy

    @ReplaceLoadBalancerUnhealthy.setter
    def ReplaceLoadBalancerUnhealthy(self, ReplaceLoadBalancerUnhealthy):
        self._ReplaceLoadBalancerUnhealthy = ReplaceLoadBalancerUnhealthy


    def _deserialize(self, params):
        self._ReplaceMonitorUnhealthy = params.get("ReplaceMonitorUnhealthy")
        self._ScalingMode = params.get("ScalingMode")
        self._ReplaceLoadBalancerUnhealthy = params.get("ReplaceLoadBalancerUnhealthy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetInstancesProtectionRequest(AbstractModel):
    """SetInstancesProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID。
        :type AutoScalingGroupId: str
        :param _InstanceIds: 实例ID。
        :type InstanceIds: list of str
        :param _ProtectedFromScaleIn: 实例是否需要设置保护。
        :type ProtectedFromScaleIn: bool
        """
        self._AutoScalingGroupId = None
        self._InstanceIds = None
        self._ProtectedFromScaleIn = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ProtectedFromScaleIn(self):
        return self._ProtectedFromScaleIn

    @ProtectedFromScaleIn.setter
    def ProtectedFromScaleIn(self, ProtectedFromScaleIn):
        self._ProtectedFromScaleIn = ProtectedFromScaleIn


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._InstanceIds = params.get("InstanceIds")
        self._ProtectedFromScaleIn = params.get("ProtectedFromScaleIn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetInstancesProtectionResponse(AbstractModel):
    """SetInstancesProtection返回参数结构体

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


class SpotMarketOptions(AbstractModel):
    """竞价相关选项

    """

    def __init__(self):
        r"""
        :param _MaxPrice: 竞价出价，例如“1.05”
        :type MaxPrice: str
        :param _SpotInstanceType: 竞价请求类型，当前仅支持类型：one-time，默认值为one-time
注意：此字段可能返回 null，表示取不到有效值。
        :type SpotInstanceType: str
        """
        self._MaxPrice = None
        self._SpotInstanceType = None

    @property
    def MaxPrice(self):
        return self._MaxPrice

    @MaxPrice.setter
    def MaxPrice(self, MaxPrice):
        self._MaxPrice = MaxPrice

    @property
    def SpotInstanceType(self):
        return self._SpotInstanceType

    @SpotInstanceType.setter
    def SpotInstanceType(self, SpotInstanceType):
        self._SpotInstanceType = SpotInstanceType


    def _deserialize(self, params):
        self._MaxPrice = params.get("MaxPrice")
        self._SpotInstanceType = params.get("SpotInstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpotMixedAllocationPolicy(AbstractModel):
    """竞价混合模式下，各计费类型实例的分配策略。包括按量计费实例和竞价计费实例。

    """

    def __init__(self):
        r"""
        :param _BaseCapacity: 混合模式下，基础容量的大小，基础容量部分固定为按量计费实例。默认值 0，最大不可超过伸缩组的最大实例数。
注意：此字段可能返回 null，表示取不到有效值。
        :type BaseCapacity: int
        :param _OnDemandPercentageAboveBaseCapacity: 超出基础容量部分，按量计费实例所占的比例。取值范围 [0, 100]，0 代表超出基础容量的部分仅生产竞价实例，100 代表仅生产按量实例，默认值为 70。按百分比计算按量实例数时，向上取整。
比如，总期望实例数取 3，基础容量取 1，超基础部分按量百分比取 1，则最终按量 2 台（1 台来自基础容量，1 台按百分比向上取整得到），竞价 1台。
注意：此字段可能返回 null，表示取不到有效值。
        :type OnDemandPercentageAboveBaseCapacity: int
        :param _SpotAllocationStrategy: 混合模式下，竞价实例的分配策略。取值包括 COST_OPTIMIZED 和 CAPACITY_OPTIMIZED，默认取 COST_OPTIMIZED。
<br><li> COST_OPTIMIZED，成本优化策略。对于启动配置内的所有机型，按照各机型在各可用区的每核单价由小到大依次尝试。优先尝试购买每核单价最便宜的，如果购买失败则尝试购买次便宜的，以此类推。
<br><li> CAPACITY_OPTIMIZED，容量优化策略。对于启动配置内的所有机型，按照各机型在各可用区的库存情况由大到小依次尝试。优先尝试购买剩余库存最大的机型，这样可尽量降低竞价实例被动回收的发生概率。
注意：此字段可能返回 null，表示取不到有效值。
        :type SpotAllocationStrategy: str
        :param _CompensateWithBaseInstance: 按量实例替补功能。取值范围：
<br><li> TRUE，开启该功能，当所有竞价机型因库存不足等原因全部购买失败后，尝试购买按量实例。
<br><li> FALSE，不开启该功能，伸缩组在需要扩容竞价实例时仅尝试所配置的竞价机型。

默认取值： TRUE。
注意：此字段可能返回 null，表示取不到有效值。
        :type CompensateWithBaseInstance: bool
        """
        self._BaseCapacity = None
        self._OnDemandPercentageAboveBaseCapacity = None
        self._SpotAllocationStrategy = None
        self._CompensateWithBaseInstance = None

    @property
    def BaseCapacity(self):
        return self._BaseCapacity

    @BaseCapacity.setter
    def BaseCapacity(self, BaseCapacity):
        self._BaseCapacity = BaseCapacity

    @property
    def OnDemandPercentageAboveBaseCapacity(self):
        return self._OnDemandPercentageAboveBaseCapacity

    @OnDemandPercentageAboveBaseCapacity.setter
    def OnDemandPercentageAboveBaseCapacity(self, OnDemandPercentageAboveBaseCapacity):
        self._OnDemandPercentageAboveBaseCapacity = OnDemandPercentageAboveBaseCapacity

    @property
    def SpotAllocationStrategy(self):
        return self._SpotAllocationStrategy

    @SpotAllocationStrategy.setter
    def SpotAllocationStrategy(self, SpotAllocationStrategy):
        self._SpotAllocationStrategy = SpotAllocationStrategy

    @property
    def CompensateWithBaseInstance(self):
        return self._CompensateWithBaseInstance

    @CompensateWithBaseInstance.setter
    def CompensateWithBaseInstance(self, CompensateWithBaseInstance):
        self._CompensateWithBaseInstance = CompensateWithBaseInstance


    def _deserialize(self, params):
        self._BaseCapacity = params.get("BaseCapacity")
        self._OnDemandPercentageAboveBaseCapacity = params.get("OnDemandPercentageAboveBaseCapacity")
        self._SpotAllocationStrategy = params.get("SpotAllocationStrategy")
        self._CompensateWithBaseInstance = params.get("CompensateWithBaseInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAutoScalingInstancesRequest(AbstractModel):
    """StartAutoScalingInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _InstanceIds: 待开启的CVM实例ID列表
        :type InstanceIds: list of str
        """
        self._AutoScalingGroupId = None
        self._InstanceIds = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAutoScalingInstancesResponse(AbstractModel):
    """StartAutoScalingInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityId: 伸缩活动ID
        :type ActivityId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class StartInstanceRefreshRequest(AbstractModel):
    """StartInstanceRefresh请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID。
        :type AutoScalingGroupId: str
        :param _RefreshSettings: 刷新设置。
        :type RefreshSettings: :class:`tencentcloud.autoscaling.v20180419.models.RefreshSettings`
        :param _RefreshMode: 刷新模式，目前仅支持滚动更新，默认值为 ROLLING_UPDATE_RESET。
        :type RefreshMode: str
        """
        self._AutoScalingGroupId = None
        self._RefreshSettings = None
        self._RefreshMode = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RefreshSettings(self):
        return self._RefreshSettings

    @RefreshSettings.setter
    def RefreshSettings(self, RefreshSettings):
        self._RefreshSettings = RefreshSettings

    @property
    def RefreshMode(self):
        return self._RefreshMode

    @RefreshMode.setter
    def RefreshMode(self, RefreshMode):
        self._RefreshMode = RefreshMode


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        if params.get("RefreshSettings") is not None:
            self._RefreshSettings = RefreshSettings()
            self._RefreshSettings._deserialize(params.get("RefreshSettings"))
        self._RefreshMode = params.get("RefreshMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstanceRefreshResponse(AbstractModel):
    """StartInstanceRefresh返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RefreshActivityId: 刷新活动 ID。
        :type RefreshActivityId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RefreshActivityId = None
        self._RequestId = None

    @property
    def RefreshActivityId(self):
        return self._RefreshActivityId

    @RefreshActivityId.setter
    def RefreshActivityId(self, RefreshActivityId):
        self._RefreshActivityId = RefreshActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RefreshActivityId = params.get("RefreshActivityId")
        self._RequestId = params.get("RequestId")


class StopAutoScalingInstancesRequest(AbstractModel):
    """StopAutoScalingInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param _InstanceIds: 待关闭的CVM实例ID列表
        :type InstanceIds: list of str
        :param _StoppedMode: 关闭的实例是否收费，取值为：  
KEEP_CHARGING：关机继续收费  
STOP_CHARGING：关机停止收费
默认为 KEEP_CHARGING
        :type StoppedMode: str
        """
        self._AutoScalingGroupId = None
        self._InstanceIds = None
        self._StoppedMode = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def StoppedMode(self):
        return self._StoppedMode

    @StoppedMode.setter
    def StoppedMode(self, StoppedMode):
        self._StoppedMode = StoppedMode


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._InstanceIds = params.get("InstanceIds")
        self._StoppedMode = params.get("StoppedMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopAutoScalingInstancesResponse(AbstractModel):
    """StopAutoScalingInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActivityId: 伸缩活动ID
        :type ActivityId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActivityId = None
        self._RequestId = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._RequestId = params.get("RequestId")


class StopInstanceRefreshRequest(AbstractModel):
    """StopInstanceRefresh请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: 伸缩组ID。
        :type AutoScalingGroupId: str
        :param _RefreshActivityId: 刷新活动ID。
        :type RefreshActivityId: str
        """
        self._AutoScalingGroupId = None
        self._RefreshActivityId = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def RefreshActivityId(self):
        return self._RefreshActivityId

    @RefreshActivityId.setter
    def RefreshActivityId(self, RefreshActivityId):
        self._RefreshActivityId = RefreshActivityId


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._RefreshActivityId = params.get("RefreshActivityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstanceRefreshResponse(AbstractModel):
    """StopInstanceRefresh返回参数结构体

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


class SystemDisk(AbstractModel):
    """启动配置的系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。

    """

    def __init__(self):
        r"""
        :param _DiskType: 系统盘类型。系统盘类型限制详见[云硬盘类型](https://cloud.tencent.com/document/product/362/2353)。取值范围：<br><li>LOCAL_BASIC：本地硬盘<br><li>LOCAL_SSD：本地SSD硬盘<br><li>CLOUD_BASIC：普通云硬盘<br><li>CLOUD_PREMIUM：高性能云硬盘<br><li>CLOUD_SSD：SSD云硬盘<br><br>默认取值：CLOUD_PREMIUM。
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
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
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
    """资源类型及标签键值对

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
        :type Key: str
        :param _Value: 标签值
        :type Value: str
        :param _ResourceType: 标签绑定的资源类型，当前支持类型："auto-scaling-group
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        """
        self._Key = None
        self._Value = None
        self._ResourceType = None

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
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetAttribute(AbstractModel):
    """负载均衡器目标属性

    """

    def __init__(self):
        r"""
        :param _Port: 端口
        :type Port: int
        :param _Weight: 权重
        :type Weight: int
        """
        self._Port = None
        self._Weight = None

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
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeLaunchConfigurationRequest(AbstractModel):
    """UpgradeLaunchConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LaunchConfigurationId: 启动配置ID。
        :type LaunchConfigurationId: str
        :param _ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-8toqc6s3`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，取返回信息中的`ImageId`字段。</li>
        :type ImageId: str
        :param _InstanceTypes: 实例机型列表，不同实例机型指定了不同的资源规格，最多支持5种实例机型。
        :type InstanceTypes: list of str
        :param _LaunchConfigurationName: 启动配置显示名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。
        :type LaunchConfigurationName: str
        :param _DataDisks: 实例数据盘配置信息。若不指定该参数，则默认不购买数据盘，最多支持指定11块数据盘。
        :type DataDisks: list of DataDisk
        :param _EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。
        :type EnhancedService: :class:`tencentcloud.autoscaling.v20180419.models.EnhancedService`
        :param _InstanceChargeType: 实例计费类型，CVM默认值按照POSTPAID_BY_HOUR处理。
<br><li>POSTPAID_BY_HOUR：按小时后付费
<br><li>SPOTPAID：竞价付费
<br><li>PREPAID：预付费，即包年包月
        :type InstanceChargeType: str
        :param _InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数，若指定实例的付费模式为竞价付费则该参数必传。
        :type InstanceMarketOptions: :class:`tencentcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        :param _InstanceTypesCheckPolicy: 实例类型校验策略，取值包括 ALL 和 ANY，默认取值为ANY。
<br><li> ALL，所有实例类型（InstanceType）都可用则通过校验，否则校验报错。
<br><li> ANY，存在任何一个实例类型（InstanceType）可用则通过校验，否则校验报错。

实例类型不可用的常见原因包括该实例类型售罄、对应云盘售罄等。
如果 InstanceTypes 中一款机型不存在或者已下线，则无论 InstanceTypesCheckPolicy 采用何种取值，都会校验报错。
        :type InstanceTypesCheckPolicy: str
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.InternetAccessible`
        :param _LoginSettings: 该参数已失效，请勿使用。升级启动配置接口无法修改或覆盖 LoginSettings 参数，升级后 LoginSettings 不会发生变化。
        :type LoginSettings: :class:`tencentcloud.autoscaling.v20180419.models.LoginSettings`
        :param _ProjectId: 实例所属项目ID。不填为默认项目。
        :type ProjectId: int
        :param _SecurityGroupIds: 实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的`SecurityGroupId`字段来获取。若不指定该参数，则默认不绑定安全组。
        :type SecurityGroupIds: list of str
        :param _SystemDisk: 实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.autoscaling.v20180419.models.SystemDisk`
        :param _UserData: 经过 Base64 编码后的自定义数据，最大长度不超过16KB。
        :type UserData: str
        :param _InstanceTags: 标签列表。通过指定该参数，可以为扩容的实例绑定标签。最多支持指定10个标签。
        :type InstanceTags: list of InstanceTag
        :param _CamRoleName: CAM角色名称。可通过DescribeRoleList接口返回值中的roleName获取。
        :type CamRoleName: str
        :param _HostNameSettings: 云服务器主机名（HostName）的相关设置。
        :type HostNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.HostNameSettings`
        :param _InstanceNameSettings: 云服务器实例名（InstanceName）的相关设置。
        :type InstanceNameSettings: :class:`tencentcloud.autoscaling.v20180419.models.InstanceNameSettings`
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.autoscaling.v20180419.models.InstanceChargePrepaid`
        :param _DiskTypePolicy: 云盘类型选择策略，取值范围：
<br><li>ORIGINAL：使用设置的云盘类型
<br><li>AUTOMATIC：自动选择当前可用的云盘类型
        :type DiskTypePolicy: str
        :param _IPv6InternetAccessible: IPv6公网带宽相关信息设置。若新建实例包含IPv6地址，该参数可为新建实例的IPv6地址分配公网带宽。关联启动配置的伸缩组Ipv6AddressCount参数为0时，该参数不会生效。
        :type IPv6InternetAccessible: :class:`tencentcloud.autoscaling.v20180419.models.IPv6InternetAccessible`
        """
        self._LaunchConfigurationId = None
        self._ImageId = None
        self._InstanceTypes = None
        self._LaunchConfigurationName = None
        self._DataDisks = None
        self._EnhancedService = None
        self._InstanceChargeType = None
        self._InstanceMarketOptions = None
        self._InstanceTypesCheckPolicy = None
        self._InternetAccessible = None
        self._LoginSettings = None
        self._ProjectId = None
        self._SecurityGroupIds = None
        self._SystemDisk = None
        self._UserData = None
        self._InstanceTags = None
        self._CamRoleName = None
        self._HostNameSettings = None
        self._InstanceNameSettings = None
        self._InstanceChargePrepaid = None
        self._DiskTypePolicy = None
        self._IPv6InternetAccessible = None

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def LaunchConfigurationName(self):
        return self._LaunchConfigurationName

    @LaunchConfigurationName.setter
    def LaunchConfigurationName(self, LaunchConfigurationName):
        self._LaunchConfigurationName = LaunchConfigurationName

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceMarketOptions(self):
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def InstanceTypesCheckPolicy(self):
        return self._InstanceTypesCheckPolicy

    @InstanceTypesCheckPolicy.setter
    def InstanceTypesCheckPolicy(self, InstanceTypesCheckPolicy):
        self._InstanceTypesCheckPolicy = InstanceTypesCheckPolicy

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def UserData(self):
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def InstanceTags(self):
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def CamRoleName(self):
        return self._CamRoleName

    @CamRoleName.setter
    def CamRoleName(self, CamRoleName):
        self._CamRoleName = CamRoleName

    @property
    def HostNameSettings(self):
        return self._HostNameSettings

    @HostNameSettings.setter
    def HostNameSettings(self, HostNameSettings):
        self._HostNameSettings = HostNameSettings

    @property
    def InstanceNameSettings(self):
        return self._InstanceNameSettings

    @InstanceNameSettings.setter
    def InstanceNameSettings(self, InstanceNameSettings):
        self._InstanceNameSettings = InstanceNameSettings

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def DiskTypePolicy(self):
        return self._DiskTypePolicy

    @DiskTypePolicy.setter
    def DiskTypePolicy(self, DiskTypePolicy):
        self._DiskTypePolicy = DiskTypePolicy

    @property
    def IPv6InternetAccessible(self):
        return self._IPv6InternetAccessible

    @IPv6InternetAccessible.setter
    def IPv6InternetAccessible(self, IPv6InternetAccessible):
        self._IPv6InternetAccessible = IPv6InternetAccessible


    def _deserialize(self, params):
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._ImageId = params.get("ImageId")
        self._InstanceTypes = params.get("InstanceTypes")
        self._LaunchConfigurationName = params.get("LaunchConfigurationName")
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._InstanceTypesCheckPolicy = params.get("InstanceTypesCheckPolicy")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._ProjectId = params.get("ProjectId")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._UserData = params.get("UserData")
        if params.get("InstanceTags") is not None:
            self._InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTag()
                obj._deserialize(item)
                self._InstanceTags.append(obj)
        self._CamRoleName = params.get("CamRoleName")
        if params.get("HostNameSettings") is not None:
            self._HostNameSettings = HostNameSettings()
            self._HostNameSettings._deserialize(params.get("HostNameSettings"))
        if params.get("InstanceNameSettings") is not None:
            self._InstanceNameSettings = InstanceNameSettings()
            self._InstanceNameSettings._deserialize(params.get("InstanceNameSettings"))
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._DiskTypePolicy = params.get("DiskTypePolicy")
        if params.get("IPv6InternetAccessible") is not None:
            self._IPv6InternetAccessible = IPv6InternetAccessible()
            self._IPv6InternetAccessible._deserialize(params.get("IPv6InternetAccessible"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeLaunchConfigurationResponse(AbstractModel):
    """UpgradeLaunchConfiguration返回参数结构体

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


class UpgradeLifecycleHookRequest(AbstractModel):
    """UpgradeLifecycleHook请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LifecycleHookId: 生命周期挂钩ID
        :type LifecycleHookId: str
        :param _LifecycleHookName: 生命周期挂钩名称
        :type LifecycleHookName: str
        :param _LifecycleTransition: 进行生命周期挂钩的场景，取值范围包括“INSTANCE_LAUNCHING”和“INSTANCE_TERMINATING”
        :type LifecycleTransition: str
        :param _DefaultResult: 定义伸缩组在生命周期挂钩超时的情况下应采取的操作，取值范围是“CONTINUE”或“ABANDON”，默认值为“CONTINUE”
        :type DefaultResult: str
        :param _HeartbeatTimeout: 生命周期挂钩超时之前可以经过的最长时间（以秒为单位），范围从30到7200秒，默认值为300秒
        :type HeartbeatTimeout: int
        :param _NotificationMetadata: 弹性伸缩向通知目标发送的附加信息，配置通知时使用，默认值为空字符串""
        :type NotificationMetadata: str
        :param _NotificationTarget: 通知目标。NotificationTarget和LifecycleCommand参数互斥，二者不可同时指定。
        :type NotificationTarget: :class:`tencentcloud.autoscaling.v20180419.models.NotificationTarget`
        :param _LifecycleTransitionType: 进行生命周期挂钩的场景类型，取值范围包括NORMAL 和 EXTENSION。说明：设置为EXTENSION值，在AttachInstances、DetachInstances、RemoveInstaces接口时会触发生命周期挂钩操作，值为NORMAL则不会在这些接口中触发生命周期挂钩。
        :type LifecycleTransitionType: str
        :param _LifecycleCommand: 远程命令执行对象。NotificationTarget和LifecycleCommand参数互斥，二者不可同时指定。
        :type LifecycleCommand: :class:`tencentcloud.autoscaling.v20180419.models.LifecycleCommand`
        """
        self._LifecycleHookId = None
        self._LifecycleHookName = None
        self._LifecycleTransition = None
        self._DefaultResult = None
        self._HeartbeatTimeout = None
        self._NotificationMetadata = None
        self._NotificationTarget = None
        self._LifecycleTransitionType = None
        self._LifecycleCommand = None

    @property
    def LifecycleHookId(self):
        return self._LifecycleHookId

    @LifecycleHookId.setter
    def LifecycleHookId(self, LifecycleHookId):
        self._LifecycleHookId = LifecycleHookId

    @property
    def LifecycleHookName(self):
        return self._LifecycleHookName

    @LifecycleHookName.setter
    def LifecycleHookName(self, LifecycleHookName):
        self._LifecycleHookName = LifecycleHookName

    @property
    def LifecycleTransition(self):
        return self._LifecycleTransition

    @LifecycleTransition.setter
    def LifecycleTransition(self, LifecycleTransition):
        self._LifecycleTransition = LifecycleTransition

    @property
    def DefaultResult(self):
        return self._DefaultResult

    @DefaultResult.setter
    def DefaultResult(self, DefaultResult):
        self._DefaultResult = DefaultResult

    @property
    def HeartbeatTimeout(self):
        return self._HeartbeatTimeout

    @HeartbeatTimeout.setter
    def HeartbeatTimeout(self, HeartbeatTimeout):
        self._HeartbeatTimeout = HeartbeatTimeout

    @property
    def NotificationMetadata(self):
        return self._NotificationMetadata

    @NotificationMetadata.setter
    def NotificationMetadata(self, NotificationMetadata):
        self._NotificationMetadata = NotificationMetadata

    @property
    def NotificationTarget(self):
        return self._NotificationTarget

    @NotificationTarget.setter
    def NotificationTarget(self, NotificationTarget):
        self._NotificationTarget = NotificationTarget

    @property
    def LifecycleTransitionType(self):
        return self._LifecycleTransitionType

    @LifecycleTransitionType.setter
    def LifecycleTransitionType(self, LifecycleTransitionType):
        self._LifecycleTransitionType = LifecycleTransitionType

    @property
    def LifecycleCommand(self):
        return self._LifecycleCommand

    @LifecycleCommand.setter
    def LifecycleCommand(self, LifecycleCommand):
        self._LifecycleCommand = LifecycleCommand


    def _deserialize(self, params):
        self._LifecycleHookId = params.get("LifecycleHookId")
        self._LifecycleHookName = params.get("LifecycleHookName")
        self._LifecycleTransition = params.get("LifecycleTransition")
        self._DefaultResult = params.get("DefaultResult")
        self._HeartbeatTimeout = params.get("HeartbeatTimeout")
        self._NotificationMetadata = params.get("NotificationMetadata")
        if params.get("NotificationTarget") is not None:
            self._NotificationTarget = NotificationTarget()
            self._NotificationTarget._deserialize(params.get("NotificationTarget"))
        self._LifecycleTransitionType = params.get("LifecycleTransitionType")
        if params.get("LifecycleCommand") is not None:
            self._LifecycleCommand = LifecycleCommand()
            self._LifecycleCommand._deserialize(params.get("LifecycleCommand"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeLifecycleHookResponse(AbstractModel):
    """UpgradeLifecycleHook返回参数结构体

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