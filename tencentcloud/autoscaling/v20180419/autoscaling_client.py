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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.autoscaling.v20180419 import models


class AutoscalingClient(AbstractClient):
    _apiVersion = '2018-04-19'
    _endpoint = 'as.tencentcloudapi.com'
    _service = 'as'


    def AttachInstances(self, request):
        """本接口（AttachInstances）用于将 CVM 实例添加到伸缩组。

        :param request: Request instance for AttachInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.AttachInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.AttachInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ClearLaunchConfigurationAttributes(self, request):
        """本接口（ClearLaunchConfigurationAttributes）用于将启动配置内的特定属性完全清空。

        :param request: Request instance for ClearLaunchConfigurationAttributes.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ClearLaunchConfigurationAttributesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ClearLaunchConfigurationAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ClearLaunchConfigurationAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ClearLaunchConfigurationAttributesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CompleteLifecycleAction(self, request):
        """本接口（CompleteLifecycleAction）用于完成生命周期动作。

        * 用户通过调用本接口，指定一个具体的生命周期挂钩的结果（“CONITNUE”或者“ABANDON”）。如果一直不调用本接口，则生命周期挂钩会在超时后按照“DefaultResult”进行处理。

        :param request: Request instance for CompleteLifecycleAction.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CompleteLifecycleActionRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CompleteLifecycleActionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CompleteLifecycleAction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CompleteLifecycleActionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAutoScalingGroup(self, request):
        """本接口（CreateAutoScalingGroup）用于创建伸缩组

        :param request: Request instance for CreateAutoScalingGroup.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateAutoScalingGroupRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAutoScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAutoScalingGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAutoScalingGroupFromInstance(self, request):
        """本接口（CreateAutoScalingGroupFromInstance）用于根据实例创建启动配置及伸缩组。

        说明：根据按包年包月计费的实例所创建的伸缩组，其扩容的实例为按量计费实例。

        :param request: Request instance for CreateAutoScalingGroupFromInstance.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateAutoScalingGroupFromInstanceRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateAutoScalingGroupFromInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAutoScalingGroupFromInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAutoScalingGroupFromInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLaunchConfiguration(self, request):
        """本接口（CreateLaunchConfiguration）用于创建新的启动配置。

        * 启动配置，可以通过 `ModifyLaunchConfigurationAttributes` 修改少量字段。如需使用新的启动配置，建议重新创建启动配置。

        * 每个项目最多只能创建20个启动配置，详见[使用限制](https://cloud.tencent.com/document/product/377/3120)。

        :param request: Request instance for CreateLaunchConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateLaunchConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateLaunchConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLaunchConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLaunchConfigurationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLifecycleHook(self, request):
        """本接口（CreateLifecycleHook）用于创建生命周期挂钩。

        * 您可以为生命周期挂钩配置消息通知，弹性伸缩会通知您的CMQ消息队列，通知内容形如：

        ```
        {
        	"Service": "Tencent Cloud Auto Scaling",
        	"Time": "2019-03-14T10:15:11Z",
        	"AppId": "1251783334",
        	"ActivityId": "asa-fznnvrja",
        	"AutoScalingGroupId": "asg-rrrrtttt",
        	"LifecycleHookId": "ash-xxxxyyyy",
        	"LifecycleHookName": "my-hook",
        	"LifecycleActionToken": "3080e1c9-0efe-4dd7-ad3b-90cd6618298f",
        	"InstanceId": "ins-aaaabbbb",
        	"LifecycleTransition": "INSTANCE_LAUNCHING",
        	"NotificationMetadata": ""
        }
        ```

        :param request: Request instance for CreateLifecycleHook.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateLifecycleHookRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateLifecycleHookResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLifecycleHook", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLifecycleHookResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNotificationConfiguration(self, request):
        """本接口（CreateNotificationConfiguration）用于创建通知。

        :param request: Request instance for CreateNotificationConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateNotificationConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateNotificationConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNotificationConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNotificationConfigurationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePaiInstance(self, request):
        """本接口 (CreatePaiInstance) 用于创建一个指定配置的PAI实例。

        :param request: Request instance for CreatePaiInstance.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreatePaiInstanceRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreatePaiInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePaiInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePaiInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateScalingPolicy(self, request):
        """本接口（CreateScalingPolicy）用于创建告警触发策略。

        :param request: Request instance for CreateScalingPolicy.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateScalingPolicyRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateScalingPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateScalingPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateScheduledAction(self, request):
        """本接口（CreateScheduledAction）用于创建定时任务。

        :param request: Request instance for CreateScheduledAction.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.CreateScheduledActionRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.CreateScheduledActionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateScheduledAction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateScheduledActionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAutoScalingGroup(self, request):
        """本接口（DeleteAutoScalingGroup）用于删除指定伸缩组，删除前提是伸缩组内无实例且当前未在执行伸缩活动。

        :param request: Request instance for DeleteAutoScalingGroup.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteAutoScalingGroupRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAutoScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAutoScalingGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLaunchConfiguration(self, request):
        """本接口（DeleteLaunchConfiguration）用于删除启动配置。

        * 若启动配置在伸缩组中属于生效状态，则该启动配置不允许删除。

        :param request: Request instance for DeleteLaunchConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteLaunchConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteLaunchConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLaunchConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLaunchConfigurationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLifecycleHook(self, request):
        """本接口（DeleteLifecycleHook）用于删除生命周期挂钩。

        :param request: Request instance for DeleteLifecycleHook.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteLifecycleHookRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteLifecycleHookResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLifecycleHook", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLifecycleHookResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNotificationConfiguration(self, request):
        """本接口（DeleteNotificationConfiguration）用于删除特定的通知。

        :param request: Request instance for DeleteNotificationConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteNotificationConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteNotificationConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNotificationConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNotificationConfigurationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteScalingPolicy(self, request):
        """本接口（DeleteScalingPolicy）用于删除告警触发策略。

        :param request: Request instance for DeleteScalingPolicy.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteScalingPolicyRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteScalingPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteScalingPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteScheduledAction(self, request):
        """本接口（DeleteScheduledAction）用于删除特定的定时任务。

        :param request: Request instance for DeleteScheduledAction.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DeleteScheduledActionRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DeleteScheduledActionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteScheduledAction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteScheduledActionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccountLimits(self, request):
        """本接口（DescribeAccountLimits）用于查询用户账户在弹性伸缩中的资源限制。

        :param request: Request instance for DescribeAccountLimits.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAccountLimitsRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAccountLimitsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccountLimits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountLimitsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAutoScalingActivities(self, request):
        """本接口（DescribeAutoScalingActivities）用于查询伸缩组的伸缩活动记录。

        :param request: Request instance for DescribeAutoScalingActivities.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingActivitiesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingActivitiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAutoScalingActivities", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutoScalingActivitiesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAutoScalingGroupLastActivities(self, request):
        """本接口（DescribeAutoScalingGroupLastActivities）用于查询伸缩组的最新一次伸缩活动记录。

        :param request: Request instance for DescribeAutoScalingGroupLastActivities.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingGroupLastActivitiesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingGroupLastActivitiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAutoScalingGroupLastActivities", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutoScalingGroupLastActivitiesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAutoScalingGroups(self, request):
        """本接口（DescribeAutoScalingGroups）用于查询伸缩组信息。

        * 可以根据伸缩组ID、伸缩组名称或者启动配置ID等信息来查询伸缩组的详细信息。过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的伸缩组。

        :param request: Request instance for DescribeAutoScalingGroups.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingGroupsRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAutoScalingGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutoScalingGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAutoScalingInstances(self, request):
        """本接口（DescribeAutoScalingInstances）用于查询弹性伸缩关联实例的信息。

        * 可以根据实例ID、伸缩组ID等信息来查询实例的详细信息。过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的实例。

        :param request: Request instance for DescribeAutoScalingInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeAutoScalingInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAutoScalingInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutoScalingInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLaunchConfigurations(self, request):
        """本接口（DescribeLaunchConfigurations）用于查询启动配置的信息。

        * 可以根据启动配置ID、启动配置名称等信息来查询启动配置的详细信息。过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的启动配置。

        :param request: Request instance for DescribeLaunchConfigurations.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeLaunchConfigurationsRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeLaunchConfigurationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLaunchConfigurations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLaunchConfigurationsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLifecycleHooks(self, request):
        """本接口（DescribeLifecycleHooks）用于查询生命周期挂钩信息。

        * 可以根据伸缩组ID、生命周期挂钩ID或者生命周期挂钩名称等信息来查询生命周期挂钩的详细信息。过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的生命周期挂钩。

        :param request: Request instance for DescribeLifecycleHooks.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeLifecycleHooksRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeLifecycleHooksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLifecycleHooks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLifecycleHooksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNotificationConfigurations(self, request):
        """本接口 (DescribeNotificationConfigurations) 用于查询一个或多个通知的详细信息。

        可以根据通知ID、伸缩组ID等信息来查询通知的详细信息。过滤信息详细请见过滤器`Filter`。
        如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的通知。

        :param request: Request instance for DescribeNotificationConfigurations.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeNotificationConfigurationsRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeNotificationConfigurationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNotificationConfigurations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNotificationConfigurationsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePaiInstances(self, request):
        """本接口（DescribePaiInstances）用于查询PAI实例信息。

        * 可以根据实例ID、实例域名等信息来查询PAI实例的详细信息。过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的PAI实例。

        :param request: Request instance for DescribePaiInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribePaiInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribePaiInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePaiInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePaiInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeScalingPolicies(self, request):
        """本接口（DescribeScalingPolicies）用于查询告警触发策略。

        :param request: Request instance for DescribeScalingPolicies.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeScalingPoliciesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeScalingPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScalingPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScalingPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeScheduledActions(self, request):
        """本接口 (DescribeScheduledActions) 用于查询一个或多个定时任务的详细信息。

        * 可以根据定时任务ID、定时任务名称或者伸缩组ID等信息来查询定时任务的详细信息。过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的定时任务。

        :param request: Request instance for DescribeScheduledActions.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DescribeScheduledActionsRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DescribeScheduledActionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScheduledActions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScheduledActionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachInstances(self, request):
        """本接口（DetachInstances）用于从伸缩组移出 CVM 实例，本接口不会销毁实例。
        * 如果移出指定实例后，伸缩组内处于`IN_SERVICE`状态的实例数量小于伸缩组最小值，接口将报错
        * 如果伸缩组处于`DISABLED`状态，移出操作不校验`IN_SERVICE`实例数量和最小值的关系
        * 对于伸缩组配置的 CLB，实例在离开伸缩组时，AS 会进行解挂载动作

        :param request: Request instance for DetachInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DetachInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DetachInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableAutoScalingGroup(self, request):
        """本接口（DisableAutoScalingGroup）用于停用指定伸缩组。

        :param request: Request instance for DisableAutoScalingGroup.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.DisableAutoScalingGroupRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.DisableAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableAutoScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableAutoScalingGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableAutoScalingGroup(self, request):
        """本接口（EnableAutoScalingGroup）用于启用指定伸缩组。

        :param request: Request instance for EnableAutoScalingGroup.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.EnableAutoScalingGroupRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.EnableAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableAutoScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableAutoScalingGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ExecuteScalingPolicy(self, request):
        """本接口（ExecuteScalingPolicy）用于执行伸缩策略。

        * 可以根据伸缩策略ID执行伸缩策略。
        * 伸缩策略所属伸缩组处于伸缩活动时，会拒绝执行伸缩策略。

        :param request: Request instance for ExecuteScalingPolicy.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ExecuteScalingPolicyRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ExecuteScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExecuteScalingPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExecuteScalingPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAutoScalingGroup(self, request):
        """本接口（ModifyAutoScalingGroup）用于修改伸缩组。

        :param request: Request instance for ModifyAutoScalingGroup.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyAutoScalingGroupRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAutoScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAutoScalingGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDesiredCapacity(self, request):
        """本接口（ModifyDesiredCapacity）用于修改指定伸缩组的期望实例数

        :param request: Request instance for ModifyDesiredCapacity.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyDesiredCapacityRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyDesiredCapacityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDesiredCapacity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDesiredCapacityResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLaunchConfigurationAttributes(self, request):
        """本接口（ModifyLaunchConfigurationAttributes）用于修改启动配置部分属性。

        * 修改启动配置后，已经使用该启动配置扩容的存量实例不会发生变更，此后使用该启动配置的新增实例会按照新的配置进行扩容。
        * 本接口支持修改部分简单类型。

        :param request: Request instance for ModifyLaunchConfigurationAttributes.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyLaunchConfigurationAttributesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyLaunchConfigurationAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLaunchConfigurationAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLaunchConfigurationAttributesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLoadBalancers(self, request):
        """本接口（ModifyLoadBalancers）用于修改伸缩组的负载均衡器。

        * 本接口用于为伸缩组指定新的负载均衡器配置，采用“完全覆盖”风格，无论之前配置如何，统一按照接口参数配置为新的负载均衡器。
        * 如果要为伸缩组清空负载均衡器，则在调用本接口时仅指定伸缩组ID，不指定具体负载均衡器。
        * 本接口会立即修改伸缩组的负载均衡器，并生成一个伸缩活动，异步修改存量实例的负载均衡器。

        :param request: Request instance for ModifyLoadBalancers.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyLoadBalancersRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLoadBalancers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLoadBalancersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNotificationConfiguration(self, request):
        """本接口（ModifyNotificationConfiguration）用于修改通知。

        :param request: Request instance for ModifyNotificationConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyNotificationConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyNotificationConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNotificationConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNotificationConfigurationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyScalingPolicy(self, request):
        """本接口（ModifyScalingPolicy）用于修改告警触发策略。

        :param request: Request instance for ModifyScalingPolicy.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyScalingPolicyRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyScalingPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyScalingPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyScheduledAction(self, request):
        """本接口（ModifyScheduledAction）用于修改定时任务。

        :param request: Request instance for ModifyScheduledAction.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ModifyScheduledActionRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ModifyScheduledActionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyScheduledAction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyScheduledActionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PreviewPaiDomainName(self, request):
        """本接口（PreviewPaiDomainName）用于预览PAI实例域名。

        :param request: Request instance for PreviewPaiDomainName.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.PreviewPaiDomainNameRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.PreviewPaiDomainNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PreviewPaiDomainName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PreviewPaiDomainNameResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemoveInstances(self, request):
        """本接口（RemoveInstances）用于从伸缩组删除 CVM 实例。根据当前的产品逻辑，如果实例由弹性伸缩自动创建，则实例会被销毁；如果实例系创建后加入伸缩组的，则会从伸缩组中移除，保留实例。
        * 如果删除指定实例后，伸缩组内处于`IN_SERVICE`状态的实例数量小于伸缩组最小值，接口将报错
        * 如果伸缩组处于`DISABLED`状态，删除操作不校验`IN_SERVICE`实例数量和最小值的关系
        * 对于伸缩组配置的 CLB，实例在离开伸缩组时，AS 会进行解挂载动作

        :param request: Request instance for RemoveInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.RemoveInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.RemoveInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ScaleInInstances(self, request):
        """为伸缩组指定数量缩容实例，返回缩容活动的 ActivityId。
        * 伸缩组需要未处于活动中
        * 根据伸缩组的`TerminationPolicies`策略，选择被缩容的实例，可参考[缩容处理](https://cloud.tencent.com/document/product/377/8563)
        * 接口只会选择`IN_SERVICE`实例缩容，如果需要缩容其他状态实例，可以使用 [DetachInstances](https://cloud.tencent.com/document/api/377/20436) 或 [RemoveInstances](https://cloud.tencent.com/document/api/377/20431) 接口
        * 接口会减少期望实例数，新的期望实例数需要大于等于最小实例数
        * 缩容如果失败或者部分成功，最后期望实例数只会扣减实际缩容成功的实例数量

        :param request: Request instance for ScaleInInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ScaleInInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ScaleInInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ScaleInInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScaleInInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ScaleOutInstances(self, request):
        """为伸缩组指定数量扩容实例，返回扩容活动的 ActivityId。
        * 伸缩组需要未处于活动中
        * 接口会增加期望实例数，新的期望实例数需要小于等于最大实例数
        * 扩容如果失败或者部分成功，最后期望实例数只会增加实际成功的实例数量

        :param request: Request instance for ScaleOutInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.ScaleOutInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.ScaleOutInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ScaleOutInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScaleOutInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetInstancesProtection(self, request):
        """本接口（SetInstancesProtection）用于设置实例保护。
        实例设置保护之后，当发生不健康替换、报警策略、期望值变更等触发缩容时，将不对此实例缩容操作。

        :param request: Request instance for SetInstancesProtection.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.SetInstancesProtectionRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.SetInstancesProtectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetInstancesProtection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetInstancesProtectionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartAutoScalingInstances(self, request):
        """本接口（StartAutoScalingInstances）用于开启伸缩组内 CVM 实例。
        * 开机成功，实例转为`IN_SERVICE`状态后，会增加期望实例数，期望实例数不可超过设置的最大值
        * 本接口支持批量操作，每次请求开机实例的上限为100

        :param request: Request instance for StartAutoScalingInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.StartAutoScalingInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.StartAutoScalingInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartAutoScalingInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartAutoScalingInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopAutoScalingInstances(self, request):
        """本接口（StopAutoScalingInstances）用于关闭伸缩组内 CVM 实例。
        * 关机方式采用`SOFT_FIRST`方式，表示在正常关闭失败后进行强制关闭
        * 关闭`IN_SERVICE`状态的实例，会减少期望实例数，期望实例数不可低于设置的最小值
        * 使用`STOP_CHARGING`选项关机，待关机的实例需要满足[关机不收费条件](https://cloud.tencent.com/document/product/213/19918)
        * 本接口支持批量操作，每次请求关机实例的上限为100

        :param request: Request instance for StopAutoScalingInstances.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.StopAutoScalingInstancesRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.StopAutoScalingInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopAutoScalingInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopAutoScalingInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpgradeLaunchConfiguration(self, request):
        """本接口（UpgradeLaunchConfiguration）用于升级启动配置。

        * 本接口用于升级启动配置，采用“完全覆盖”风格，无论之前参数如何，统一按照接口参数设置为新的配置。对于非必填字段，不填写则按照默认值赋值。
        * 升级修改启动配置后，已经使用该启动配置扩容的存量实例不会发生变更，此后使用该启动配置的新增实例会按照新的配置进行扩容。

        :param request: Request instance for UpgradeLaunchConfiguration.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.UpgradeLaunchConfigurationRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.UpgradeLaunchConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeLaunchConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeLaunchConfigurationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpgradeLifecycleHook(self, request):
        """本接口（UpgradeLifecycleHook）用于升级生命周期挂钩。

        * 本接口用于升级生命周期挂钩，采用“完全覆盖”风格，无论之前参数如何，统一按照接口参数设置为新的配置。对于非必填字段，不填写则按照默认值赋值。

        :param request: Request instance for UpgradeLifecycleHook.
        :type request: :class:`tencentcloud.autoscaling.v20180419.models.UpgradeLifecycleHookRequest`
        :rtype: :class:`tencentcloud.autoscaling.v20180419.models.UpgradeLifecycleHookResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeLifecycleHook", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeLifecycleHookResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)