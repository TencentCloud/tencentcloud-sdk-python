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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.edgezone.v20260401 import models


class EdgezoneClient(AbstractClient):
    _apiVersion = '2026-04-01'
    _endpoint = 'edgezone.tencentcloudapi.com'
    _service = 'edgezone'


    def ApplyPublicIps(self, request):
        r"""从静态 IP 池为指定公网实例批量申请多个 Ip 地址（随机分配）。申请前需检查用户配额。
        此接口仅适用于 `RouteMode=static` 的公网实例。BGP/OSPF 实例调用此接口将返回错误。

        :param request: Request instance for ApplyPublicIps.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.ApplyPublicIpsRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.ApplyPublicIpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyPublicIps", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyPublicIpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdgeNodeService(self, request):
        r"""开通边缘节点计费服务。

        :param request: Request instance for CreateEdgeNodeService.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.CreateEdgeNodeServiceRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.CreateEdgeNodeServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdgeNodeService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdgeNodeServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstances(self, request):
        r"""创建物理机实例，系统自动分配物理机资源并完成装机。如果用户未在当前可用区开通计费，系统自动开通。支持并发分配物理机资源，异步执行网络分配和装机任务。

        :param request: Request instance for CreateInstances.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.CreateInstancesRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.CreateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrivateNetworkInstance(self, request):
        r"""创建私网实例，一个用户在一个可用区仅支持创建一个私网实例，网络地址由 Network（网络号）和 Mask（掩码位数）两个参数共同决定子网范围。Network 必须是三个 RFC 1918 私有地址段之一的合法网络地址：10.0.0.0/8、172.16.0.0/12 或 192.168.0.0/16，且 host 位必须全为 0（即Network 与 Mask 组合后不能有主机位被置位，例如 10.0.0.1/24 是非法的，应填 10.0.0.0/24）。Mask 的上限统一为 28，下限由所属地址段决定：10.x.x.x 段允许 8～28，172.16.x.x 段允许 12～28，192.168.x.x 段允许 16～28。

        :param request: Request instance for CreatePrivateNetworkInstance.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.CreatePrivateNetworkInstanceRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.CreatePrivateNetworkInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrivateNetworkInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrivateNetworkInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePublicNetworkInstance(self, request):
        r"""用户输入可用区ID、公网实例名称、网络线路、路由模式以创建公网实例，一个用户在一个可用区仅支持创建一个公网实例
        路由模式为 **静态** 的公网实例需要用户主动申请和释放公网IP
        路由模式为 **OSPF、BGP** 的公网实例在创建时自动分配公网IP段，销毁时自动释放公网IP段

        :param request: Request instance for CreatePublicNetworkInstance.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.CreatePublicNetworkInstanceRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.CreatePublicNetworkInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePublicNetworkInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePublicNetworkInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivateNetworkInstance(self, request):
        r"""删除私网实例

        :param request: Request instance for DeletePrivateNetworkInstance.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DeletePrivateNetworkInstanceRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DeletePrivateNetworkInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivateNetworkInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivateNetworkInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePublicNetworkInstance(self, request):
        r"""修改公网实例信息

        :param request: Request instance for DeletePublicNetworkInstance.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DeletePublicNetworkInstanceRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DeletePublicNetworkInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePublicNetworkInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePublicNetworkInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceTypes(self, request):
        r"""根据 AppId 查询账号下可用区维度的机型配额列表；若传入 Zone，则仅返回指定可用区下的机型配额；若不传，则返回账号下所有可用区的机型配额。

        :param request: Request instance for DescribeInstanceTypes.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DescribeInstanceTypesRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DescribeInstanceTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        r"""查询物理机实例列表，支持按实例ID、实例名称、可用区、实例状态等条件筛选，并支持分页查询。

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivateNetworkInstances(self, request):
        r"""查询私网实例，支持通过私网实例ID、私网实例名称、可用区ID等参数进行查询

        :param request: Request instance for DescribePrivateNetworkInstances.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DescribePrivateNetworkInstancesRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DescribePrivateNetworkInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateNetworkInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivateNetworkInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicIps(self, request):
        r"""查询用户的公网Ip信息，对于路由模式为Static的公网实例，会返回所有已申请的公网Ip信息，对于路由模式为Ospf和Bgp的公网实例，会直接返回网段信息

        :param request: Request instance for DescribePublicIps.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DescribePublicIpsRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DescribePublicIpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicIps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicIpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicNetworkInstances(self, request):
        r"""查询公网实例列表，支持按实例ID、实例名称、可用区等条件筛选，并支持分页查询。

        :param request: Request instance for DescribePublicNetworkInstances.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DescribePublicNetworkInstancesRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DescribePublicNetworkInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicNetworkInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicNetworkInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneData(self, request):
        r"""按指标名，查询统计数据。数据按1分钟间隔统计

        :param request: Request instance for DescribeZoneData.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DescribeZoneDataRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DescribeZoneDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        r"""跨地域聚合查询所有已配置 region 下的可用区列表。支持通过 FilterByAppId 参数控制是否按账号过滤：默认仅返回账号关联的可用区，设为 False 时返回所有可用区。本地域直查数据库，远程地域并发 HTTP 请求后合并返回。

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceAttribute(self, request):
        r"""修改物理机实例的属性，支持修改实例名称、变更公网IP（IPv4/IPv6）。InstanceName 和 NewPublicIp 至少传入一个。

        :param request: Request instance for ModifyInstanceAttribute.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.ModifyInstanceAttributeRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.ModifyInstanceAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPrivateNetworkInstance(self, request):
        r"""修改私网实例信息

        :param request: Request instance for ModifyPrivateNetworkInstance.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.ModifyPrivateNetworkInstanceRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.ModifyPrivateNetworkInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrivateNetworkInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrivateNetworkInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPublicNetworkInstance(self, request):
        r"""修改公网实例信息

        :param request: Request instance for ModifyPublicNetworkInstance.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.ModifyPublicNetworkInstanceRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.ModifyPublicNetworkInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPublicNetworkInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPublicNetworkInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleasePublicIp(self, request):
        r"""批量释放已分配给 STATIC 公网实例但**未绑定物理服务器**的 IPv4 地址
        此接口仅适用于 STATIC 模式实例。BGP/OSPF 实例的 CIDR 在实例删除时自动归还，无需手动释放单个 IP。

        :param request: Request instance for ReleasePublicIp.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.ReleasePublicIpRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.ReleasePublicIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleasePublicIp", params, headers=headers)
            response = json.loads(body)
            model = models.ReleasePublicIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateInstances(self, request):
        r"""销毁物理机实例，释放资源。接口同步释放网络资源（IP回收）并更新状态为 terminating，后台异步执行磁盘清理。支持部分成功。

        :param request: Request instance for TerminateInstances.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.TerminateInstancesRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.TerminateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))