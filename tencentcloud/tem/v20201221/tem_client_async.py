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
from tencentcloud.tem.v20201221 import models
from typing import Dict


class TemClient(AbstractClient):
    _apiVersion = '2020-12-21'
    _endpoint = 'tem.tencentcloudapi.com'
    _service = 'tem'

    async def CreateCosToken(
            self,
            request: models.CreateCosTokenRequest,
            opts: Dict = None,
    ) -> models.CreateCosTokenResponse:
        """
        生成Cos临时秘钥
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCosToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCosTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCosTokenV2(
            self,
            request: models.CreateCosTokenV2Request,
            opts: Dict = None,
    ) -> models.CreateCosTokenV2Response:
        """
        生成Cos临时秘钥
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCosTokenV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCosTokenV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNamespace(
            self,
            request: models.CreateNamespaceRequest,
            opts: Dict = None,
    ) -> models.CreateNamespaceResponse:
        """
        创建环境
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateResource(
            self,
            request: models.CreateResourceRequest,
            opts: Dict = None,
    ) -> models.CreateResourceResponse:
        """
        绑定云资源
        """
        
        kwargs = {}
        kwargs["action"] = "CreateResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateServiceV2(
            self,
            request: models.CreateServiceV2Request,
            opts: Dict = None,
    ) -> models.CreateServiceV2Response:
        """
        创建服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateServiceV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServiceV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIngress(
            self,
            request: models.DeleteIngressRequest,
            opts: Dict = None,
    ) -> models.DeleteIngressResponse:
        """
        删除 Ingress 规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIngress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIngressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeployServiceV2(
            self,
            request: models.DeployServiceV2Request,
            opts: Dict = None,
    ) -> models.DeployServiceV2Response:
        """
        服务部署
        """
        
        kwargs = {}
        kwargs["action"] = "DeployServiceV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeployServiceV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIngress(
            self,
            request: models.DescribeIngressRequest,
            opts: Dict = None,
    ) -> models.DescribeIngressResponse:
        """
        查询 Ingress 规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIngress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIngressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIngresses(
            self,
            request: models.DescribeIngressesRequest,
            opts: Dict = None,
    ) -> models.DescribeIngressesResponse:
        """
        查询 Ingress 规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIngresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIngressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNamespaces(
            self,
            request: models.DescribeNamespacesRequest,
            opts: Dict = None,
    ) -> models.DescribeNamespacesResponse:
        """
        获取租户环境列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRelatedIngresses(
            self,
            request: models.DescribeRelatedIngressesRequest,
            opts: Dict = None,
    ) -> models.DescribeRelatedIngressesResponse:
        """
        查询服务关联的 Ingress 规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRelatedIngresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRelatedIngressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceRunPodListV2(
            self,
            request: models.DescribeServiceRunPodListV2Request,
            opts: Dict = None,
    ) -> models.DescribeServiceRunPodListV2Response:
        """
        获取服务下面运行pod列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceRunPodListV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceRunPodListV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateDownloadUrl(
            self,
            request: models.GenerateDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.GenerateDownloadUrlResponse:
        """
        生成包预签名下载链接
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIngress(
            self,
            request: models.ModifyIngressRequest,
            opts: Dict = None,
    ) -> models.ModifyIngressResponse:
        """
        创建或者更新 Ingress 规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIngress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIngressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNamespace(
            self,
            request: models.ModifyNamespaceRequest,
            opts: Dict = None,
    ) -> models.ModifyNamespaceResponse:
        """
        编辑环境
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyServiceInfo(
            self,
            request: models.ModifyServiceInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyServiceInfoResponse:
        """
        修改服务基本信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyServiceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyServiceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartServiceRunPod(
            self,
            request: models.RestartServiceRunPodRequest,
            opts: Dict = None,
    ) -> models.RestartServiceRunPodResponse:
        """
        重启实例
        """
        
        kwargs = {}
        kwargs["action"] = "RestartServiceRunPod"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartServiceRunPodResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)