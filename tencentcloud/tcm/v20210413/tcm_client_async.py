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
from tencentcloud.tcm.v20210413 import models
from typing import Dict


class TcmClient(AbstractClient):
    _apiVersion = '2021-04-13'
    _endpoint = 'tcm.tencentcloudapi.com'
    _service = 'tcm'

    async def CreateMesh(
            self,
            request: models.CreateMeshRequest,
            opts: Dict = None,
    ) -> models.CreateMeshResponse:
        """
        创建网格
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMesh"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMeshResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMesh(
            self,
            request: models.DeleteMeshRequest,
            opts: Dict = None,
    ) -> models.DeleteMeshResponse:
        """
        删除网格
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMesh"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMeshResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessLogConfig(
            self,
            request: models.DescribeAccessLogConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessLogConfigResponse:
        """
        获取AccessLog配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMesh(
            self,
            request: models.DescribeMeshRequest,
            opts: Dict = None,
    ) -> models.DescribeMeshResponse:
        """
        查询网格详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMesh"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMeshResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMeshList(
            self,
            request: models.DescribeMeshListRequest,
            opts: Dict = None,
    ) -> models.DescribeMeshListResponse:
        """
        查询网格列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMeshList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMeshListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LinkClusterList(
            self,
            request: models.LinkClusterListRequest,
            opts: Dict = None,
    ) -> models.LinkClusterListResponse:
        """
        关联集群
        """
        
        kwargs = {}
        kwargs["action"] = "LinkClusterList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LinkClusterListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LinkPrometheus(
            self,
            request: models.LinkPrometheusRequest,
            opts: Dict = None,
    ) -> models.LinkPrometheusResponse:
        """
        关联Prometheus
        """
        
        kwargs = {}
        kwargs["action"] = "LinkPrometheus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LinkPrometheusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccessLogConfig(
            self,
            request: models.ModifyAccessLogConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyAccessLogConfigResponse:
        """
        修改访问日志配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccessLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccessLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMesh(
            self,
            request: models.ModifyMeshRequest,
            opts: Dict = None,
    ) -> models.ModifyMeshResponse:
        """
        修改网格
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMesh"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMeshResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTracingConfig(
            self,
            request: models.ModifyTracingConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyTracingConfigResponse:
        """
        修改 Tracing 配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTracingConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTracingConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnlinkCluster(
            self,
            request: models.UnlinkClusterRequest,
            opts: Dict = None,
    ) -> models.UnlinkClusterResponse:
        """
        解关联集群
        """
        
        kwargs = {}
        kwargs["action"] = "UnlinkCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnlinkClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnlinkPrometheus(
            self,
            request: models.UnlinkPrometheusRequest,
            opts: Dict = None,
    ) -> models.UnlinkPrometheusResponse:
        """
        解除关联Prometheus
        """
        
        kwargs = {}
        kwargs["action"] = "UnlinkPrometheus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnlinkPrometheusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)