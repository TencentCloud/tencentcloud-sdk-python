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
from tencentcloud.gwlb.v20240906 import models


class GwlbClient(AbstractClient):
    _apiVersion = '2024-09-06'
    _endpoint = 'gwlb.tencentcloudapi.com'
    _service = 'gwlb'


    def AssociateTargetGroups(self, request):
        """本接口(AssociateTargetGroups)用来将目标组绑定到负载均衡。
        本接口为异步接口，本接口返回成功后需以返回的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for AssociateTargetGroups.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.AssociateTargetGroupsRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.AssociateTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateTargetGroups", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateTargetGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGatewayLoadBalancer(self, request):
        """本接口(CreateGatewayLoadBalancer)用来创建网关负载均衡实例。为了使用网关负载均衡服务，您必须购买一个或多个网关负载均衡实例。成功调用该接口后，会返回网关负载均衡实例的唯一 ID。
        注意：单个账号在每个地域的默认购买配额为：10个。
        本接口为异步接口，接口成功返回后，可使用 DescribeGatewayLoadBalancers 接口查询负载均衡实例的状态（如创建中、正常），以确定是否创建成功。

        :param request: Request instance for CreateGatewayLoadBalancer.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.CreateGatewayLoadBalancerRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.CreateGatewayLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGatewayLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGatewayLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTargetGroup(self, request):
        """创建目标组。该功能正在内测中，如需使用，请通过[工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB&step=1)。

        :param request: Request instance for CreateTargetGroup.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.CreateTargetGroupRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.CreateTargetGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTargetGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTargetGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGatewayLoadBalancer(self, request):
        """DeleteGatewayLoadBalancer 接口用以删除指定的一个或多个网关负载均衡实例。成功删除后，会把网关负载均衡实例与后端服务解绑。
        本接口为异步接口，接口返回成功后，需以返回的 RequestId 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for DeleteGatewayLoadBalancer.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DeleteGatewayLoadBalancerRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DeleteGatewayLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGatewayLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGatewayLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTargetGroups(self, request):
        """删除目标组

        :param request: Request instance for DeleteTargetGroups.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DeleteTargetGroupsRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DeleteTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTargetGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTargetGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeregisterTargetGroupInstances(self, request):
        """从目标组中解绑服务器。
        本接口为异步接口，本接口返回成功后需以返回的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for DeregisterTargetGroupInstances.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DeregisterTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DeregisterTargetGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeregisterTargetGroupInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DeregisterTargetGroupInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewayLoadBalancers(self, request):
        """查询一个地域的网关负载均衡实例列表。

        :param request: Request instance for DescribeGatewayLoadBalancers.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DescribeGatewayLoadBalancersRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DescribeGatewayLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetGroupInstanceStatus(self, request):
        """查询目标组后端服务状态。目前仅支持网关负载均衡类型的目标组支持查询后端服务状态。

        :param request: Request instance for DescribeTargetGroupInstanceStatus.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DescribeTargetGroupInstanceStatusRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DescribeTargetGroupInstanceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetGroupInstanceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetGroupInstanceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetGroupInstances(self, request):
        """获取目标组绑定的服务器信息。

        :param request: Request instance for DescribeTargetGroupInstances.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DescribeTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DescribeTargetGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetGroupInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetGroupInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetGroupList(self, request):
        """获取目标组列表

        :param request: Request instance for DescribeTargetGroupList.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DescribeTargetGroupListRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DescribeTargetGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetGroups(self, request):
        """查询目标组信息

        :param request: Request instance for DescribeTargetGroups.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DescribeTargetGroupsRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DescribeTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskStatus(self, request):
        """本接口用于查询异步任务的执行状态，对于非查询类的接口（创建/删除负载均衡实例等），在接口调用成功后，都需要使用本接口查询任务最终是否执行成功。

        :param request: Request instance for DescribeTaskStatus.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DescribeTaskStatusRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DescribeTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateTargetGroups(self, request):
        """解除负载均衡和目标组的关联关系。
        本接口为异步接口，本接口返回成功后需以返回的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for DisassociateTargetGroups.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DisassociateTargetGroupsRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DisassociateTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateTargetGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateTargetGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceCreateGatewayLoadBalancer(self, request):
        """InquirePriceCreateGatewayLoadBalancer接口查询创建网关负载均衡的价格。

        :param request: Request instance for InquirePriceCreateGatewayLoadBalancer.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.InquirePriceCreateGatewayLoadBalancerRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.InquirePriceCreateGatewayLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceCreateGatewayLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceCreateGatewayLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGatewayLoadBalancerAttribute(self, request):
        """ModifyGatewayLoadBalancerAttribute 接口用于修改负载均衡实例的属性。支持修改负载均衡实例的名称、带宽上限。

        :param request: Request instance for ModifyGatewayLoadBalancerAttribute.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.ModifyGatewayLoadBalancerAttributeRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.ModifyGatewayLoadBalancerAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGatewayLoadBalancerAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGatewayLoadBalancerAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetGroupAttribute(self, request):
        """修改目标组的名称、健康探测等属性。

        :param request: Request instance for ModifyTargetGroupAttribute.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.ModifyTargetGroupAttributeRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.ModifyTargetGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetGroupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetGroupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetGroupInstancesWeight(self, request):
        """修改目标组的服务器权重。
        本接口为异步接口，本接口返回成功后需以返回的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for ModifyTargetGroupInstancesWeight.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.ModifyTargetGroupInstancesWeightRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.ModifyTargetGroupInstancesWeightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetGroupInstancesWeight", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetGroupInstancesWeightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterTargetGroupInstances(self, request):
        """注册服务器到目标组。
        本接口为异步接口，本接口返回成功后需以返回的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for RegisterTargetGroupInstances.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.RegisterTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.RegisterTargetGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterTargetGroupInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterTargetGroupInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))