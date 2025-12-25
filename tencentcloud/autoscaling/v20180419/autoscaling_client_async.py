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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.autoscaling.v20180419 import models
from typing import Dict


class AutoscalingClient(AbstractClient):
    _apiVersion = '2018-04-19'
    _endpoint = 'as.tencentcloudapi.com'
    _service = 'as'

    async def AttachInstances(
            self,
            request: models.AttachInstancesRequest,
            opts: Dict = None,
    ) -> models.AttachInstancesResponse:
        """
        本接口（AttachInstances）用于将 CVM 实例添加到伸缩组。
        * 仅支持添加处于`RUNNING`（运行中）或`STOPPED`（已关机）状态的 CVM 实例
        * 添加的 CVM 实例需要和伸缩组 VPC 网络一致
        """
        
        kwargs = {}
        kwargs["action"] = "AttachInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachLoadBalancers(
            self,
            request: models.AttachLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.AttachLoadBalancersResponse:
        """
        此接口（AttachLoadBalancers）用于将负载均衡器添加到伸缩组。
        """
        
        kwargs = {}
        kwargs["action"] = "AttachLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelInstanceRefresh(
            self,
            request: models.CancelInstanceRefreshRequest,
            opts: Dict = None,
    ) -> models.CancelInstanceRefreshResponse:
        """
        取消伸缩组的实例刷新活动。
        * 已刷新的批次不受影响，待刷新批次被取消
        * 如存在正在刷新的批次，不允许取消；可先暂停活动，等待当前批次结束后再取消
        * 刷新失败的实例保持备用中状态，需用户手动处理后尝试退出备用中状态或销毁
        * 取消后不允许回滚操作，也不支持恢复操作
        * 因 maxSurge 参数而临时扩容的实例在取消后会自动销毁
        * 进行缩容时，所有实例都已经更新完成，此时无法取消
        """
        
        kwargs = {}
        kwargs["action"] = "CancelInstanceRefresh"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelInstanceRefreshResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClearLaunchConfigurationAttributes(
            self,
            request: models.ClearLaunchConfigurationAttributesRequest,
            opts: Dict = None,
    ) -> models.ClearLaunchConfigurationAttributesResponse:
        """
        本接口（ClearLaunchConfigurationAttributes）用于将启动配置内的特定属性完全清空。
        """
        
        kwargs = {}
        kwargs["action"] = "ClearLaunchConfigurationAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearLaunchConfigurationAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CompleteLifecycleAction(
            self,
            request: models.CompleteLifecycleActionRequest,
            opts: Dict = None,
    ) -> models.CompleteLifecycleActionResponse:
        """
        本接口（CompleteLifecycleAction）用于完成生命周期动作。

        * 用户通过调用本接口，指定一个具体的生命周期挂钩的结果（“CONITNUE”或者“ABANDON”）。如果一直不调用本接口，则生命周期挂钩会在超时后按照“DefaultResult”进行处理。
        """
        
        kwargs = {}
        kwargs["action"] = "CompleteLifecycleAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompleteLifecycleActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAutoScalingGroup(
            self,
            request: models.CreateAutoScalingGroupRequest,
            opts: Dict = None,
    ) -> models.CreateAutoScalingGroupResponse:
        """
        本接口（CreateAutoScalingGroup）用于创建伸缩组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAutoScalingGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAutoScalingGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAutoScalingGroupFromInstance(
            self,
            request: models.CreateAutoScalingGroupFromInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateAutoScalingGroupFromInstanceResponse:
        """
        本接口（CreateAutoScalingGroupFromInstance）用于根据实例创建启动配置及伸缩组。

        说明：根据按包年包月计费的实例所创建的伸缩组，其扩容的实例为按量计费实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAutoScalingGroupFromInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAutoScalingGroupFromInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLaunchConfiguration(
            self,
            request: models.CreateLaunchConfigurationRequest,
            opts: Dict = None,
    ) -> models.CreateLaunchConfigurationResponse:
        """
        本接口（CreateLaunchConfiguration）用于创建新的启动配置。

        * 启动配置，可以通过 [ModifyLaunchConfigurationAttributes](https://cloud.tencent.com/document/api/377/31298) 修改少量字段。如需使用新的启动配置，建议重新创建启动配置。

        * 每个地域默认只能创建50个启动配置，详见[使用限制](https://cloud.tencent.com/document/product/377/3120)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLaunchConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLaunchConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLifecycleHook(
            self,
            request: models.CreateLifecycleHookRequest,
            opts: Dict = None,
    ) -> models.CreateLifecycleHookResponse:
        """
        本接口（CreateLifecycleHook）用于创建生命周期挂钩。

        * 您可以为生命周期挂钩配置消息通知或执行自动化助手命令。

        如果您配置了通知消息，弹性伸缩会通知您的TDMQ消息队列，通知内容形如：

        ```
        {
        	"Service": "Tencent Cloud Auto Scaling",
        	"Time": "2019-03-14T10:15:11Z",
        	"AppId": "1251783334",
        	"ActivityId": "asa-fznnvrja",
        	"AutoScalingGroupId": "asg-ft6y7u8n",
        	"LifecycleHookId": "ash-p9i7y6t5",
        	"LifecycleHookName": "my-hook",
        	"LifecycleActionToken": "3080e1c9-0efe-4dd7-ad3b-90cd6618298f",
        	"InstanceId": "ins-y6dr5e43",
        	"LifecycleTransition": "INSTANCE_LAUNCHING",
        	"NotificationMetadata": ""
        }
        ```
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLifecycleHook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLifecycleHookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNotificationConfiguration(
            self,
            request: models.CreateNotificationConfigurationRequest,
            opts: Dict = None,
    ) -> models.CreateNotificationConfigurationResponse:
        """
        本接口（CreateNotificationConfiguration）用于创建通知。
        通知到 CMQ 主题或队列时，消息内容如下：
        ```
        {
            "Service": "Tencent Cloud Auto Scaling",
            "CreatedTime": "2021-10-11T10:15:11Z", // 活动创建时间
            "AppId": "100000000",
            "ActivityId": "asa-fznnvrja", // 伸缩活动ID
            "AutoScalingGroupId": "asg-pc2oqu2z", // 伸缩组ID
            "ActivityType": "SCALE_OUT",  // 伸缩活动类型
            "StatusCode": "SUCCESSFUL",   // 伸缩活动结果
            "Description": "Activity was launched in response to a difference between desired capacity and actual capacity,
            scale out 1 instance(s).", // 伸缩活动描述
            "StartTime": "2021-10-11T10:15:11Z",  // 活动开始时间
            "EndTime": "2021-10-11T10:15:32Z",    // 活动结束时间
            "DetailedStatusMessageSet": [ // 活动内部错误集合（非空不代表活动失败）
                {
                    "Code": "InvalidInstanceType",
                    "Zone": "ap-guangzhou-6",
                    "InstanceId": "",
                    "InstanceChargeType": "POSTPAID_BY_HOUR",
                    "SubnetId": "subnet-4t5mgeuu",
                    "Message": "The specified instance type `S5.LARGE8` is invalid in `subnet-4t5mgeuu`, `ap-guangzhou-6`.",
                    "InstanceType": "S5.LARGE8"
                }
            ]
        }
        ```
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNotificationConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNotificationConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScalingPolicy(
            self,
            request: models.CreateScalingPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateScalingPolicyResponse:
        """
        本接口（CreateScalingPolicy）用于创建告警触发策略。
        - 目标追踪策略触发扩容的条件为，指定类型指标连续 3 个周期高于阈值（目标值），每个周期 1 分钟；触发缩容的条件为，指定类型指标连续 15 个周期低于阈值（目标值的80%），每个周期 1 分钟。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScalingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScalingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScheduledAction(
            self,
            request: models.CreateScheduledActionRequest,
            opts: Dict = None,
    ) -> models.CreateScheduledActionResponse:
        """
        本接口（CreateScheduledAction）用于创建定时任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScheduledAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScheduledActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAutoScalingGroup(
            self,
            request: models.DeleteAutoScalingGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteAutoScalingGroupResponse:
        """
        本接口（DeleteAutoScalingGroup）用于删除指定伸缩组，删除前提是伸缩组内无运行中（IN_SERVICE）状态的实例且当前未在执行伸缩活动。删除伸缩组后，创建失败（CREATION_FAILED）、中止失败（TERMINATION_FAILED）、解绑失败（DETACH_FAILED）等非运行中状态的实例不会被销毁。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAutoScalingGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAutoScalingGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLaunchConfiguration(
            self,
            request: models.DeleteLaunchConfigurationRequest,
            opts: Dict = None,
    ) -> models.DeleteLaunchConfigurationResponse:
        """
        本接口（DeleteLaunchConfiguration）用于删除启动配置。

        * 若启动配置在伸缩组中属于生效状态，则该启动配置不允许删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLaunchConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLaunchConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLifecycleHook(
            self,
            request: models.DeleteLifecycleHookRequest,
            opts: Dict = None,
    ) -> models.DeleteLifecycleHookResponse:
        """
        本接口（DeleteLifecycleHook）用于删除生命周期挂钩。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLifecycleHook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLifecycleHookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNotificationConfiguration(
            self,
            request: models.DeleteNotificationConfigurationRequest,
            opts: Dict = None,
    ) -> models.DeleteNotificationConfigurationResponse:
        """
        本接口（DeleteNotificationConfiguration）用于删除特定的通知。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNotificationConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNotificationConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteScalingPolicy(
            self,
            request: models.DeleteScalingPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteScalingPolicyResponse:
        """
        本接口（DeleteScalingPolicy）用于删除告警触发策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteScalingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteScalingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteScheduledAction(
            self,
            request: models.DeleteScheduledActionRequest,
            opts: Dict = None,
    ) -> models.DeleteScheduledActionResponse:
        """
        本接口（DeleteScheduledAction）用于删除特定的定时任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteScheduledAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteScheduledActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountLimits(
            self,
            request: models.DescribeAccountLimitsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountLimitsResponse:
        """
        本接口（DescribeAccountLimits）用于查询用户账户在弹性伸缩中的资源限制。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScalingActivities(
            self,
            request: models.DescribeAutoScalingActivitiesRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScalingActivitiesResponse:
        """
        本接口（DescribeAutoScalingActivities）用于查询伸缩组的伸缩活动记录。当前仅保存近两年的伸缩活动。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScalingActivities"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScalingActivitiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScalingAdvices(
            self,
            request: models.DescribeAutoScalingAdvicesRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScalingAdvicesResponse:
        """
        此接口用于查询伸缩组配置建议。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScalingAdvices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScalingAdvicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScalingGroupLastActivities(
            self,
            request: models.DescribeAutoScalingGroupLastActivitiesRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScalingGroupLastActivitiesResponse:
        """
        本接口（DescribeAutoScalingGroupLastActivities）用于查询伸缩组的最新一次伸缩活动记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScalingGroupLastActivities"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScalingGroupLastActivitiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScalingGroups(
            self,
            request: models.DescribeAutoScalingGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScalingGroupsResponse:
        """
        本接口（DescribeAutoScalingGroups）用于查询伸缩组信息。

        * 可以根据伸缩组ID、伸缩组名称或者启动配置ID等信息来查询伸缩组的详细信息。过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的伸缩组。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScalingGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScalingGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScalingInstances(
            self,
            request: models.DescribeAutoScalingInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScalingInstancesResponse:
        """
        本接口（DescribeAutoScalingInstances）用于查询弹性伸缩关联实例的信息。

        * 可以根据实例ID、伸缩组ID等信息来查询实例的详细信息。过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScalingInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScalingInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLaunchConfigurations(
            self,
            request: models.DescribeLaunchConfigurationsRequest,
            opts: Dict = None,
    ) -> models.DescribeLaunchConfigurationsResponse:
        """
        本接口（DescribeLaunchConfigurations）用于查询启动配置的信息。

        * 可以根据启动配置ID、启动配置名称等信息来查询启动配置的详细信息。过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的启动配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLaunchConfigurations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLaunchConfigurationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLifecycleHooks(
            self,
            request: models.DescribeLifecycleHooksRequest,
            opts: Dict = None,
    ) -> models.DescribeLifecycleHooksResponse:
        """
        本接口（DescribeLifecycleHooks）用于查询生命周期挂钩信息。

        * 可以根据伸缩组ID、生命周期挂钩ID或者生命周期挂钩名称等信息来查询生命周期挂钩的详细信息。过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的生命周期挂钩。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLifecycleHooks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLifecycleHooksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotificationConfigurations(
            self,
            request: models.DescribeNotificationConfigurationsRequest,
            opts: Dict = None,
    ) -> models.DescribeNotificationConfigurationsResponse:
        """
        本接口 (DescribeNotificationConfigurations) 用于查询一个或多个通知的详细信息。

        可以根据通知ID、伸缩组ID等信息来查询通知的详细信息。过滤信息详细请见过滤器`Filter`。
        如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的通知。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotificationConfigurations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotificationConfigurationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRefreshActivities(
            self,
            request: models.DescribeRefreshActivitiesRequest,
            opts: Dict = None,
    ) -> models.DescribeRefreshActivitiesResponse:
        """
        本接口（DescribeRefreshActivities）用于查询伸缩组的实例刷新活动记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRefreshActivities"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRefreshActivitiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScalingPolicies(
            self,
            request: models.DescribeScalingPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeScalingPoliciesResponse:
        """
        本接口（DescribeScalingPolicies）用于查询告警触发策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScalingPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScalingPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScheduledActions(
            self,
            request: models.DescribeScheduledActionsRequest,
            opts: Dict = None,
    ) -> models.DescribeScheduledActionsResponse:
        """
        本接口 (DescribeScheduledActions) 用于查询一个或多个定时任务的详细信息。

        * 可以根据定时任务ID、定时任务名称或者伸缩组ID等信息来查询定时任务的详细信息。过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的定时任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScheduledActions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScheduledActionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachInstances(
            self,
            request: models.DetachInstancesRequest,
            opts: Dict = None,
    ) -> models.DetachInstancesResponse:
        """
        本接口（DetachInstances）用于从伸缩组移出 CVM 实例，本接口不会销毁实例。
        * 如果移出指定实例后，伸缩组内处于`IN_SERVICE`状态的实例数量小于伸缩组最小值，接口将报错
        * 如果伸缩组处于`DISABLED`状态，移出操作不校验`IN_SERVICE`实例数量和最小值的关系
        * 对于伸缩组配置的 CLB，实例在离开伸缩组时，AS 会进行解挂载动作
        """
        
        kwargs = {}
        kwargs["action"] = "DetachInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachLoadBalancers(
            self,
            request: models.DetachLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.DetachLoadBalancersResponse:
        """
        本接口（DetachLoadBalancers）用于从伸缩组移出负载均衡器，本接口不会销毁负载均衡器。
        """
        
        kwargs = {}
        kwargs["action"] = "DetachLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableAutoScalingGroup(
            self,
            request: models.DisableAutoScalingGroupRequest,
            opts: Dict = None,
    ) -> models.DisableAutoScalingGroupResponse:
        """
        本接口（DisableAutoScalingGroup）用于停用指定伸缩组。
        * 停用伸缩组后，自动触发的伸缩活动不再进行，包括：
            - 告警策略触发的伸缩活动
            - 匹配期望实例数的伸缩活动
            - 不健康实例替换活动
            - 定时任务
        * 停用伸缩组后，手动触发的伸缩活动允许进行，包括：
            - 指定数量扩容实例（ScaleOutInstances）
            - 指定数量缩容实例（ScaleInInstances）
            - 从伸缩组中移出 CVM 实例（DetachInstances）
            - 从伸缩组中删除 CVM 实例（RemoveInstances）
            - 添加 CVM 实例到伸缩组（AttachInstances）
            - 关闭伸缩组内 CVM 实例（StopAutoScalingInstances）
            - 开启伸缩组内 CVM 实例（StartAutoScalingInstances）
        """
        
        kwargs = {}
        kwargs["action"] = "DisableAutoScalingGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableAutoScalingGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableAutoScalingGroup(
            self,
            request: models.EnableAutoScalingGroupRequest,
            opts: Dict = None,
    ) -> models.EnableAutoScalingGroupResponse:
        """
        本接口（EnableAutoScalingGroup）用于启用指定伸缩组。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableAutoScalingGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableAutoScalingGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnterStandby(
            self,
            request: models.EnterStandbyRequest,
            opts: Dict = None,
    ) -> models.EnterStandbyResponse:
        """
        伸缩组内实例进入备用中状态。
        * 备用中状态实例的 CLB 权重值为 0，不会被自动缩容、不健康替换、实例刷新操作选中
        * 调用弹性伸缩开关机接口会使得备用中状态发生变化，而云服务器开关机接口不会影响
        * 实例进入备用中状态后，伸缩组会尝试下调期望实例数，新期望数不会小于最小值
        """
        
        kwargs = {}
        kwargs["action"] = "EnterStandby"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnterStandbyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExecuteScalingPolicy(
            self,
            request: models.ExecuteScalingPolicyRequest,
            opts: Dict = None,
    ) -> models.ExecuteScalingPolicyResponse:
        """
        本接口（ExecuteScalingPolicy）用于执行伸缩策略。

        * 可以根据伸缩策略ID执行伸缩策略。
        * 伸缩策略所属伸缩组处于伸缩活动时，会拒绝执行伸缩策略。
        * 本接口不支持执行目标追踪策略。
        """
        
        kwargs = {}
        kwargs["action"] = "ExecuteScalingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExecuteScalingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExitStandby(
            self,
            request: models.ExitStandbyRequest,
            opts: Dict = None,
    ) -> models.ExitStandbyResponse:
        """
        伸缩组内实例退出备用中状态。
        * 退出备用中状态后，实例会进入运行中状态，CLB 权重值恢复为预设值
        * 调用弹性伸缩开关机接口会使得备用中状态发生变化，而云服务器开关机接口不会影响
        * 实例退出备用中状态后，伸缩组会上调期望实例数，新期望数不能大于最大值
        """
        
        kwargs = {}
        kwargs["action"] = "ExitStandby"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExitStandbyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoScalingGroup(
            self,
            request: models.ModifyAutoScalingGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoScalingGroupResponse:
        """
        本接口（ModifyAutoScalingGroup）用于修改伸缩组。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoScalingGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoScalingGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDesiredCapacity(
            self,
            request: models.ModifyDesiredCapacityRequest,
            opts: Dict = None,
    ) -> models.ModifyDesiredCapacityResponse:
        """
        本接口（ModifyDesiredCapacity）用于修改指定伸缩组的期望实例数
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDesiredCapacity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDesiredCapacityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLaunchConfigurationAttributes(
            self,
            request: models.ModifyLaunchConfigurationAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyLaunchConfigurationAttributesResponse:
        """
        本接口（ModifyLaunchConfigurationAttributes）用于修改启动配置部分属性。

        * 修改启动配置后，已经使用该启动配置扩容的存量实例不会发生变更，此后使用该启动配置的新增实例会按照新的配置进行扩容。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLaunchConfigurationAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLaunchConfigurationAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLifecycleHook(
            self,
            request: models.ModifyLifecycleHookRequest,
            opts: Dict = None,
    ) -> models.ModifyLifecycleHookResponse:
        """
        此接口用于修改生命周期挂钩。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLifecycleHook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLifecycleHookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancerTargetAttributes(
            self,
            request: models.ModifyLoadBalancerTargetAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancerTargetAttributesResponse:
        """
        本接口（ModifyLoadBalancerTargetAttributes）用于修改伸缩组内负载均衡器的目标规则属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancerTargetAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancerTargetAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancers(
            self,
            request: models.ModifyLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancersResponse:
        """
        本接口（ModifyLoadBalancers）用于修改伸缩组的负载均衡器。

        * 本接口用于为伸缩组指定新的负载均衡器配置，采用`完全覆盖`风格，无论之前配置如何，`统一按照接口参数配置为新的负载均衡器`。
        * 如果要为伸缩组清空负载均衡器，则在调用本接口时仅指定伸缩组ID，不指定具体负载均衡器。
        * 本接口会立即修改伸缩组的负载均衡器，并生成一个伸缩活动，异步修改存量实例的负载均衡器。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNotificationConfiguration(
            self,
            request: models.ModifyNotificationConfigurationRequest,
            opts: Dict = None,
    ) -> models.ModifyNotificationConfigurationResponse:
        """
        本接口（ModifyNotificationConfiguration）用于修改通知。
        * 通知的接收端类型不支持修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNotificationConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNotificationConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyScalingPolicy(
            self,
            request: models.ModifyScalingPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyScalingPolicyResponse:
        """
        本接口（ModifyScalingPolicy）用于修改告警触发策略。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyScalingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyScalingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyScheduledAction(
            self,
            request: models.ModifyScheduledActionRequest,
            opts: Dict = None,
    ) -> models.ModifyScheduledActionResponse:
        """
        本接口（ModifyScheduledAction）用于修改定时任务。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyScheduledAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyScheduledActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveInstances(
            self,
            request: models.RemoveInstancesRequest,
            opts: Dict = None,
    ) -> models.RemoveInstancesResponse:
        """
        本接口（RemoveInstances）用于从伸缩组删除 CVM 实例。根据当前的产品逻辑，如果实例由弹性伸缩自动创建，则实例会被销毁；如果实例系创建后加入伸缩组的，则会从伸缩组中移除，保留实例。
        * 如果删除指定实例后，伸缩组内处于`IN_SERVICE`状态的实例数量小于伸缩组最小值，接口将报错
        * 如果伸缩组处于`DISABLED`状态，删除操作不校验`IN_SERVICE`实例数量和最小值的关系
        * 对于伸缩组配置的 CLB，实例在离开伸缩组时，AS 会进行解挂载动作
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeInstanceRefresh(
            self,
            request: models.ResumeInstanceRefreshRequest,
            opts: Dict = None,
    ) -> models.ResumeInstanceRefreshResponse:
        """
        恢复暂停状态的实例刷新活动，使其重试当前批次刷新失败实例或继续刷新后续批次，非暂停状态下调用该接口无效。

        - 使用 MaxSurge 参数时活动可能会处于扩容或缩容失败导致的暂停状态，也可以使用该接口重试扩缩容。
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeInstanceRefresh"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeInstanceRefreshResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackInstanceRefresh(
            self,
            request: models.RollbackInstanceRefreshRequest,
            opts: Dict = None,
    ) -> models.RollbackInstanceRefreshResponse:
        """
        回滚操作会生成一个新的实例刷新活动，该活动也支持分批次刷新以及暂停、恢复、取消操作，接口返回回滚活动的 RefreshActivityId。
        * 原活动中待刷新实例变更为已取消，忽略不存在实例，其他状态实例进入回滚流程
        * 原活动中正在刷新的实例不会立刻终止，刷新结束后再执行回滚活动
        * 暂停状态或最近一次成功的刷新活动支持回滚，其他状态不支持回滚
        * 原活动刷新方式为重装实例时，对于 ImageId参数，会自动恢复到回滚前镜像 ID；对于 UserData、EnhancedService、LoginSettings、 HostName 参数，依然会从启动配置中读取，需用户在回滚前自行修改启动配置
        * 回滚活动暂不支持 MaxSurge 参数
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackInstanceRefresh"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackInstanceRefreshResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleInInstances(
            self,
            request: models.ScaleInInstancesRequest,
            opts: Dict = None,
    ) -> models.ScaleInInstancesResponse:
        """
        为伸缩组指定数量缩容实例，返回缩容活动的 ActivityId。
        * 伸缩组需要未处于活动中
        * 伸缩组处于停用状态时，该接口也会生效，可参考[停用伸缩组](https://cloud.tencent.com/document/api/377/20435)文档查看伸缩组停用状态的影响范围
        * 根据伸缩组的`TerminationPolicies`策略，选择被缩容的实例，可参考[缩容处理](https://cloud.tencent.com/document/product/377/8563)
        * 接口只会选择`IN_SERVICE`实例缩容，如果需要缩容其他状态实例，可以使用 [DetachInstances](https://cloud.tencent.com/document/api/377/20436) 或 [RemoveInstances](https://cloud.tencent.com/document/api/377/20431) 接口
        * 接口会减少期望实例数，新的期望实例数需要大于等于最小实例数
        * 缩容如果失败或者部分成功，最后期望实例数只会扣减实际缩容成功的实例数量
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleInInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleInInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleOutInstances(
            self,
            request: models.ScaleOutInstancesRequest,
            opts: Dict = None,
    ) -> models.ScaleOutInstancesResponse:
        """
        为伸缩组指定数量扩容实例，返回扩容活动的 ActivityId。
        * 伸缩组需要未处于活动中
        * 伸缩组处于停用状态时，该接口也会生效，可参考[停用伸缩组](https://cloud.tencent.com/document/api/377/20435)文档查看伸缩组停用状态的影响范围
        * 接口会增加期望实例数，新的期望实例数需要小于等于最大实例数
        * 扩容如果失败或者部分成功，最后期望实例数只会增加实际成功的实例数量
        * 竞价混合模式中一次扩容可能触发多个伸缩活动，该接口仅返回第一个伸缩活动的 ActivityId
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleOutInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleOutInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetInstancesProtection(
            self,
            request: models.SetInstancesProtectionRequest,
            opts: Dict = None,
    ) -> models.SetInstancesProtectionResponse:
        """
        本接口（SetInstancesProtection）用于设置实例保护。
        实例设置保护之后，当发生不健康替换、报警策略、期望值变更等自动缩容时，将不对此实例缩容操作；对于 [DetachInstances](https://cloud.tencent.com/document/api/377/20436) 和 [RemoveInstances](https://cloud.tencent.com/document/api/377/20431) 接口，允许指定移出被保护的实例。
        """
        
        kwargs = {}
        kwargs["action"] = "SetInstancesProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetInstancesProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartAutoScalingInstances(
            self,
            request: models.StartAutoScalingInstancesRequest,
            opts: Dict = None,
    ) -> models.StartAutoScalingInstancesResponse:
        """
        本接口（StartAutoScalingInstances）用于开启伸缩组内 CVM 实例。
        * 开机成功，实例转为`IN_SERVICE`状态后，会增加期望实例数，期望实例数不可超过设置的最大值
        * 本接口支持批量操作，每次请求开机实例的上限为100
        """
        
        kwargs = {}
        kwargs["action"] = "StartAutoScalingInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartAutoScalingInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartInstanceRefresh(
            self,
            request: models.StartInstanceRefreshRequest,
            opts: Dict = None,
    ) -> models.StartInstanceRefreshResponse:
        """
        根据启动配置中参数，刷新伸缩组内运行中状态 CVM 实例，返回实例刷新活动的 RefreshActivityId。
        * 对于重装实例的刷新方式（目前仅支持重装），重装时仅会从启动配置中获取 ImageId、UserData、EnhancedService、 HostName、LoginSettings 参数进行刷新，实例的其他参数不会刷新
        * 实例刷新期间（包括暂停状态），伸缩组会被停用。不建议刷新期间修改关联启动配置，否则会影响刷新参数，造成实例配置不一致
        * 滚动更新模式会分成多批次进行刷新实例，单批次中若存在刷新失败实例，活动会进入失败暂停状态
        * 若待刷新实例被移出或销毁，会被标记为 NOT_FOUND 状态，不阻塞实例刷新活动
        * 运行中状态实例与最新启动配置参数一致，实例也会再次刷新
        """
        
        kwargs = {}
        kwargs["action"] = "StartInstanceRefresh"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartInstanceRefreshResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopAutoScalingInstances(
            self,
            request: models.StopAutoScalingInstancesRequest,
            opts: Dict = None,
    ) -> models.StopAutoScalingInstancesResponse:
        """
        本接口（StopAutoScalingInstances）用于关闭伸缩组内 CVM 实例。
        * 关机方式采用`SOFT_FIRST`方式，表示在正常关闭失败后进行强制关闭
        * 关闭`IN_SERVICE`状态的实例，会减少期望实例数，期望实例数不可低于设置的最小值
        * 使用`STOP_CHARGING`选项关机，待关机的实例需要满足[关机不收费条件](https://cloud.tencent.com/document/product/213/19918)
        * 本接口支持批量操作，每次请求关机实例的上限为100
        """
        
        kwargs = {}
        kwargs["action"] = "StopAutoScalingInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopAutoScalingInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopInstanceRefresh(
            self,
            request: models.StopInstanceRefreshRequest,
            opts: Dict = None,
    ) -> models.StopInstanceRefreshResponse:
        """
        暂停正在执行的实例刷新活动。
        * 暂停状态下，伸缩组也会处于停用中状态
        * 当前正在更新或扩容的实例不会暂停，待更新的实例会暂停更新
        * 进行缩容时，所有实例都已经更新完成，此时无法暂停
        """
        
        kwargs = {}
        kwargs["action"] = "StopInstanceRefresh"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopInstanceRefreshResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeLaunchConfiguration(
            self,
            request: models.UpgradeLaunchConfigurationRequest,
            opts: Dict = None,
    ) -> models.UpgradeLaunchConfigurationResponse:
        """
        已有替代接口ModifyLaunchConfiguration。该接口存在覆盖参数风险，目前官网已隐藏

        本接口（UpgradeLaunchConfiguration）用于升级启动配置。

        * 本接口用于升级启动配置，采用“完全覆盖”风格，无论之前参数如何，统一按照接口参数设置为新的配置。对于非必填字段，不填写则按照默认值赋值。
        * 升级修改启动配置后，已经使用该启动配置扩容的存量实例不会发生变更，此后使用该启动配置的新增实例会按照新的配置进行扩容。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeLaunchConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeLaunchConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeLifecycleHook(
            self,
            request: models.UpgradeLifecycleHookRequest,
            opts: Dict = None,
    ) -> models.UpgradeLifecycleHookResponse:
        """
        本接口（UpgradeLifecycleHook）用于升级生命周期挂钩。

        * 本接口用于升级生命周期挂钩，采用“完全覆盖”风格，无论之前参数如何，统一按照接口参数设置为新的配置。对于非必填字段，不填写则按照默认值赋值。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeLifecycleHook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeLifecycleHookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)