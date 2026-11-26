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
from tencentcloud.makers.v20261113 import models
from typing import Dict


class MakersClient(AbstractClient):
    _apiVersion = '2026-11-13'
    _endpoint = 'makers.tencentcloudapi.com'
    _service = 'makers'

    async def BlockProject(
            self,
            request: models.BlockProjectRequest,
            opts: Dict = None,
    ) -> models.BlockProjectResponse:
        """
        封禁或解封当前账号指定站点下的项目及域名。Status 支持 Ban或Normal。
        """
        
        kwargs = {}
        kwargs["action"] = "BlockProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BlockProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDeployment(
            self,
            request: models.CreateDeploymentRequest,
            opts: Dict = None,
    ) -> models.CreateDeploymentResponse:
        """
        创建部署。上传制品时 ViaMeta 和 Provider 传 Upload，TempBucketPath 传已上传对象的路径。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDeployment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeploymentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProject(
            self,
            request: models.CreateProjectRequest,
            opts: Dict = None,
    ) -> models.CreateProjectResponse:
        """
        创建项目。上传制品时 Provider 传 Upload，Channel 传 Custom。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateZoneCustomDomain(
            self,
            request: models.CreateZoneCustomDomainRequest,
            opts: Dict = None,
    ) -> models.CreateZoneCustomDomainResponse:
        """
        把一个自定义域名绑到项目的指定环境。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateZoneCustomDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateZoneCustomDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProject(
            self,
            request: models.DeleteProjectRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectResponse:
        """
        删除项目。进行中的构建会阻止删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProjectCustomDomains(
            self,
            request: models.DeleteProjectCustomDomainsRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectCustomDomainsResponse:
        """
        按域名解绑项目的自定义域名。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProjectCustomDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectCustomDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProjectEnvs(
            self,
            request: models.DeleteProjectEnvsRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectEnvsResponse:
        """
        按 EnvVars 删除环境变量。按 Id 或 Key 匹配。Value 必填但不参与匹配，可传任意值。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProjectEnvs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectEnvsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosTempToken(
            self,
            request: models.DescribeCosTempTokenRequest,
            opts: Dict = None,
    ) -> models.DescribeCosTempTokenResponse:
        """
        获取上传制品用的 COS 桶、地域、目标路径和临时密钥。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosTempToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosTempTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeploymentLog(
            self,
            request: models.DescribeDeploymentLogRequest,
            opts: Dict = None,
    ) -> models.DescribeDeploymentLogResponse:
        """
        返回构建日志的访问地址。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeploymentLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeploymentLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeployments(
            self,
            request: models.DescribeDeploymentsRequest,
            opts: Dict = None,
    ) -> models.DescribeDeploymentsResponse:
        """
        查询项目的部署记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeployments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeploymentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironments(
            self,
            request: models.DescribeEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentsResponse:
        """
        查询项目下的环境，含内置 Production、Preview 和自定义环境。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectEnvs(
            self,
            request: models.DescribeProjectEnvsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectEnvsResponse:
        """
        查询项目环境变量。不传 Env 时返回全部作用域。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectEnvs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectEnvsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjects(
            self,
            request: models.DescribeProjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectsResponse:
        """
        分页查询站点下的项目。Offset 是页码偏移，后端按 Offset * Limit 跳过。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZoneCustomDomains(
            self,
            request: models.DescribeZoneCustomDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeZoneCustomDomainsResponse:
        """
        查询项目在站点下的自定义域名和预设域名。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZoneCustomDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZoneCustomDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProject(
            self,
            request: models.ModifyProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyProjectResponse:
        """
        修改项目名称和构建配置。未传的字段保持原值。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProjectEnvs(
            self,
            request: models.ModifyProjectEnvsRequest,
            opts: Dict = None,
    ) -> models.ModifyProjectEnvsResponse:
        """
        按传入的 EnvVars 写入环境变量。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProjectEnvs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProjectEnvsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyZoneCustomDomainEnv(
            self,
            request: models.ModifyZoneCustomDomainEnvRequest,
            opts: Dict = None,
    ) -> models.ModifyZoneCustomDomainEnvResponse:
        """
        把已绑定的自定义域名切到另一个环境。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyZoneCustomDomainEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyZoneCustomDomainEnvResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)