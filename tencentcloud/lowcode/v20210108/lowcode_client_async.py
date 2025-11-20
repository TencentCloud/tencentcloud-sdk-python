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
from tencentcloud.lowcode.v20210108 import models
from typing import Dict


class LowcodeClient(AbstractClient):
    _apiVersion = '2021-01-08'
    _endpoint = 'lowcode.tencentcloudapi.com'
    _service = 'lowcode'

    async def CheckDeployApp(
            self,
            request: models.CheckDeployAppRequest,
            opts: Dict = None,
    ) -> models.CheckDeployAppResponse:
        """
        检查应用发布状态
        """
        
        kwargs = {}
        kwargs["action"] = "CheckDeployApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckDeployAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateKnowledgeSet(
            self,
            request: models.CreateKnowledgeSetRequest,
            opts: Dict = None,
    ) -> models.CreateKnowledgeSetResponse:
        """
        创建知识库
        """
        
        kwargs = {}
        kwargs["action"] = "CreateKnowledgeSet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateKnowledgeSetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAppBindWxApp(
            self,
            request: models.DeleteAppBindWxAppRequest,
            opts: Dict = None,
    ) -> models.DeleteAppBindWxAppResponse:
        """
        删除应用绑定小程序
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAppBindWxApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAppBindWxAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteKnowledgeDocumentSet(
            self,
            request: models.DeleteKnowledgeDocumentSetRequest,
            opts: Dict = None,
    ) -> models.DeleteKnowledgeDocumentSetResponse:
        """
        删除知识库下文档
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteKnowledgeDocumentSet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteKnowledgeDocumentSetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteKnowledgeSet(
            self,
            request: models.DeleteKnowledgeSetRequest,
            opts: Dict = None,
    ) -> models.DeleteKnowledgeSetResponse:
        """
        删除知识库
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteKnowledgeSet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteKnowledgeSetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeployApp(
            self,
            request: models.DeployAppRequest,
            opts: Dict = None,
    ) -> models.DeployAppResponse:
        """
        发布应用
        """
        
        kwargs = {}
        kwargs["action"] = "DeployApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeployAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApps(
            self,
            request: models.DescribeAppsRequest,
            opts: Dict = None,
    ) -> models.DescribeAppsResponse:
        """
        分页获取当前用户的应用列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataSourceList(
            self,
            request: models.DescribeDataSourceListRequest,
            opts: Dict = None,
    ) -> models.DescribeDataSourceListResponse:
        """
        获取数据源详情列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataSourceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataSourceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKnowledgeDocumentSetDetail(
            self,
            request: models.DescribeKnowledgeDocumentSetDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeKnowledgeDocumentSetDetailResponse:
        """
        获取知识库下文档详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKnowledgeDocumentSetDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKnowledgeDocumentSetDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKnowledgeDocumentSetList(
            self,
            request: models.DescribeKnowledgeDocumentSetListRequest,
            opts: Dict = None,
    ) -> models.DescribeKnowledgeDocumentSetListResponse:
        """
        查询知识库下文件集合
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKnowledgeDocumentSetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKnowledgeDocumentSetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKnowledgeSetList(
            self,
            request: models.DescribeKnowledgeSetListRequest,
            opts: Dict = None,
    ) -> models.DescribeKnowledgeSetListResponse:
        """
        查询知识库
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKnowledgeSetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKnowledgeSetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRelatedUsers(
            self,
            request: models.DescribeRelatedUsersRequest,
            opts: Dict = None,
    ) -> models.DescribeRelatedUsersResponse:
        """
        获取角色关联的用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRelatedUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRelatedUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceRoleList(
            self,
            request: models.DescribeResourceRoleListRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceRoleListResponse:
        """
        查询资源关联的角色列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceRoleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceRoleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutWxAppIdToWeApp(
            self,
            request: models.PutWxAppIdToWeAppRequest,
            opts: Dict = None,
    ) -> models.PutWxAppIdToWeAppResponse:
        """
        接口提供应用绑定微信ID功能。
        """
        
        kwargs = {}
        kwargs["action"] = "PutWxAppIdToWeApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutWxAppIdToWeAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchDocList(
            self,
            request: models.SearchDocListRequest,
            opts: Dict = None,
    ) -> models.SearchDocListResponse:
        """
        知识库文档搜索接口
        """
        
        kwargs = {}
        kwargs["action"] = "SearchDocList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchDocListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateKnowledgeSet(
            self,
            request: models.UpdateKnowledgeSetRequest,
            opts: Dict = None,
    ) -> models.UpdateKnowledgeSetResponse:
        """
        更新知识库
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateKnowledgeSet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateKnowledgeSetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadKnowledgeDocumentSet(
            self,
            request: models.UploadKnowledgeDocumentSetRequest,
            opts: Dict = None,
    ) -> models.UploadKnowledgeDocumentSetResponse:
        """
        更新知识库
        """
        
        kwargs = {}
        kwargs["action"] = "UploadKnowledgeDocumentSet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadKnowledgeDocumentSetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)