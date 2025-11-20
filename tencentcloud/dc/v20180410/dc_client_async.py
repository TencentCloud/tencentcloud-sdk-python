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
from tencentcloud.dc.v20180410 import models
from typing import Dict


class DcClient(AbstractClient):
    _apiVersion = '2018-04-10'
    _endpoint = 'dc.tencentcloudapi.com'
    _service = 'dc'

    async def AcceptDirectConnectTunnel(
            self,
            request: models.AcceptDirectConnectTunnelRequest,
            opts: Dict = None,
    ) -> models.AcceptDirectConnectTunnelResponse:
        """
        接受专用通道申请。
        """
        
        kwargs = {}
        kwargs["action"] = "AcceptDirectConnectTunnel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcceptDirectConnectTunnelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyInternetAddress(
            self,
            request: models.ApplyInternetAddressRequest,
            opts: Dict = None,
    ) -> models.ApplyInternetAddressResponse:
        """
        申请互联网CIDR地址
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyInternetAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyInternetAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudAttachService(
            self,
            request: models.CreateCloudAttachServiceRequest,
            opts: Dict = None,
    ) -> models.CreateCloudAttachServiceResponse:
        """
        创建敏捷上云服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudAttachService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudAttachServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDirectConnect(
            self,
            request: models.CreateDirectConnectRequest,
            opts: Dict = None,
    ) -> models.CreateDirectConnectResponse:
        """
        申请物理专线接入。
        调用该接口时，请注意：
        账号要进行实名认证，否则不允许申请物理专线；
        若账户下存在欠费状态的物理专线，则不能申请更多的物理专线。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDirectConnect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDirectConnectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDirectConnectTunnel(
            self,
            request: models.CreateDirectConnectTunnelRequest,
            opts: Dict = None,
    ) -> models.CreateDirectConnectTunnelResponse:
        """
        创建专用通道。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDirectConnectTunnel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDirectConnectTunnelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDirectConnect(
            self,
            request: models.DeleteDirectConnectRequest,
            opts: Dict = None,
    ) -> models.DeleteDirectConnectResponse:
        """
        删除物理专线。只能删除处于已连接状态的物理专线。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDirectConnect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDirectConnectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDirectConnectTunnel(
            self,
            request: models.DeleteDirectConnectTunnelRequest,
            opts: Dict = None,
    ) -> models.DeleteDirectConnectTunnelResponse:
        """
        删除专用通道。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDirectConnectTunnel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDirectConnectTunnelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessPoints(
            self,
            request: models.DescribeAccessPointsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessPointsResponse:
        """
        查询物理专线接入点。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessPoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessPointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDirectConnectTunnelExtra(
            self,
            request: models.DescribeDirectConnectTunnelExtraRequest,
            opts: Dict = None,
    ) -> models.DescribeDirectConnectTunnelExtraResponse:
        """
        查询专用通道扩展信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDirectConnectTunnelExtra"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDirectConnectTunnelExtraResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDirectConnectTunnels(
            self,
            request: models.DescribeDirectConnectTunnelsRequest,
            opts: Dict = None,
    ) -> models.DescribeDirectConnectTunnelsResponse:
        """
        查询专用通道列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDirectConnectTunnels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDirectConnectTunnelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDirectConnects(
            self,
            request: models.DescribeDirectConnectsRequest,
            opts: Dict = None,
    ) -> models.DescribeDirectConnectsResponse:
        """
        查询物理专线列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDirectConnects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDirectConnectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInternetAddress(
            self,
            request: models.DescribeInternetAddressRequest,
            opts: Dict = None,
    ) -> models.DescribeInternetAddressResponse:
        """
        获取用户互联网公网地址信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInternetAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInternetAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInternetAddressQuota(
            self,
            request: models.DescribeInternetAddressQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeInternetAddressQuotaResponse:
        """
        获取用户互联网公网地址配额
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInternetAddressQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInternetAddressQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInternetAddressStatistics(
            self,
            request: models.DescribeInternetAddressStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeInternetAddressStatisticsResponse:
        """
        获取用户互联网公网地址分配统计信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInternetAddressStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInternetAddressStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicDirectConnectTunnelRoutes(
            self,
            request: models.DescribePublicDirectConnectTunnelRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribePublicDirectConnectTunnelRoutesResponse:
        """
        查询互联网通道路由列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicDirectConnectTunnelRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicDirectConnectTunnelRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableInternetAddress(
            self,
            request: models.DisableInternetAddressRequest,
            opts: Dict = None,
    ) -> models.DisableInternetAddressResponse:
        """
        停用用户申请的公网互联网地址
        """
        
        kwargs = {}
        kwargs["action"] = "DisableInternetAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableInternetAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableInternetAddress(
            self,
            request: models.EnableInternetAddressRequest,
            opts: Dict = None,
    ) -> models.EnableInternetAddressResponse:
        """
        启用已停用的互联网公网地址
        """
        
        kwargs = {}
        kwargs["action"] = "EnableInternetAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableInternetAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDirectConnectAttribute(
            self,
            request: models.ModifyDirectConnectAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyDirectConnectAttributeResponse:
        """
        修改物理专线的属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDirectConnectAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDirectConnectAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDirectConnectTunnelAttribute(
            self,
            request: models.ModifyDirectConnectTunnelAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyDirectConnectTunnelAttributeResponse:
        """
        修改专用通道属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDirectConnectTunnelAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDirectConnectTunnelAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDirectConnectTunnelExtra(
            self,
            request: models.ModifyDirectConnectTunnelExtraRequest,
            opts: Dict = None,
    ) -> models.ModifyDirectConnectTunnelExtraResponse:
        """
        修改专用通道扩展信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDirectConnectTunnelExtra"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDirectConnectTunnelExtraResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RejectDirectConnectTunnel(
            self,
            request: models.RejectDirectConnectTunnelRequest,
            opts: Dict = None,
    ) -> models.RejectDirectConnectTunnelResponse:
        """
        拒绝专用通道申请。
        """
        
        kwargs = {}
        kwargs["action"] = "RejectDirectConnectTunnel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RejectDirectConnectTunnelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseInternetAddress(
            self,
            request: models.ReleaseInternetAddressRequest,
            opts: Dict = None,
    ) -> models.ReleaseInternetAddressResponse:
        """
        释放已申请的互联网地址
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseInternetAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseInternetAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)