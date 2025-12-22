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
from tencentcloud.tcbr.v20220217 import models
from typing import Dict


class TcbrClient(AbstractClient):
    _apiVersion = '2022-02-17'
    _endpoint = 'tcbr.tencentcloudapi.com'
    _service = 'tcbr'

    async def CreateCloudRunEnv(
            self,
            request: models.CreateCloudRunEnvRequest,
            opts: Dict = None,
    ) -> models.CreateCloudRunEnvResponse:
        """
        创建云托管环境，并开通资源。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudRunEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudRunEnvResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudRunServer(
            self,
            request: models.CreateCloudRunServerRequest,
            opts: Dict = None,
    ) -> models.CreateCloudRunServerResponse:
        """
        创建云托管服务接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudRunServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudRunServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudRunServer(
            self,
            request: models.DeleteCloudRunServerRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudRunServerResponse:
        """
        删除云托管服务：包括服务下的版本，镜像，流水线
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudRunServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudRunServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudRunVersions(
            self,
            request: models.DeleteCloudRunVersionsRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudRunVersionsResponse:
        """
        批量删除版本
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudRunVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudRunVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudRunDeployRecord(
            self,
            request: models.DescribeCloudRunDeployRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudRunDeployRecordResponse:
        """
        查询云托管部署记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudRunDeployRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudRunDeployRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudRunEnvs(
            self,
            request: models.DescribeCloudRunEnvsRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudRunEnvsResponse:
        """
        获取环境列表，含环境下的各个资源信息。尤其是各资源的唯一标识，是请求各资源的关键参数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudRunEnvs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudRunEnvsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudRunPodList(
            self,
            request: models.DescribeCloudRunPodListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudRunPodListResponse:
        """
        查询云托管Pod实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudRunPodList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudRunPodListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudRunProcessLog(
            self,
            request: models.DescribeCloudRunProcessLogRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudRunProcessLogResponse:
        """
        查询运行日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudRunProcessLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudRunProcessLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudRunServerDetail(
            self,
            request: models.DescribeCloudRunServerDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudRunServerDetailResponse:
        """
        查询云托管服务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudRunServerDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudRunServerDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudRunServers(
            self,
            request: models.DescribeCloudRunServersRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudRunServersResponse:
        """
        查询云托管服务列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudRunServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudRunServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvBaseInfo(
            self,
            request: models.DescribeEnvBaseInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvBaseInfoResponse:
        """
        查询环境基础信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvBaseInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvBaseInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReleaseOrder(
            self,
            request: models.DescribeReleaseOrderRequest,
            opts: Dict = None,
    ) -> models.DescribeReleaseOrderResponse:
        """
        查询发布单
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReleaseOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReleaseOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServerManageTask(
            self,
            request: models.DescribeServerManageTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeServerManageTaskResponse:
        """
        查询服务管理任务信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServerManageTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServerManageTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVersionDetail(
            self,
            request: models.DescribeVersionDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVersionDetailResponse:
        """
        查询版本详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVersionDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVersionDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OperateServerManage(
            self,
            request: models.OperateServerManageRequest,
            opts: Dict = None,
    ) -> models.OperateServerManageResponse:
        """
        操作发布单
        """
        
        kwargs = {}
        kwargs["action"] = "OperateServerManage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OperateServerManageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseGray(
            self,
            request: models.ReleaseGrayRequest,
            opts: Dict = None,
    ) -> models.ReleaseGrayResponse:
        """
        灰度发布
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseGray"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseGrayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchClsLog(
            self,
            request: models.SearchClsLogRequest,
            opts: Dict = None,
    ) -> models.SearchClsLogResponse:
        """
        查询日志信息
        """
        
        kwargs = {}
        kwargs["action"] = "SearchClsLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchClsLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitServerRollback(
            self,
            request: models.SubmitServerRollbackRequest,
            opts: Dict = None,
    ) -> models.SubmitServerRollbackResponse:
        """
        回滚版本
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitServerRollback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitServerRollbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCloudRunServer(
            self,
            request: models.UpdateCloudRunServerRequest,
            opts: Dict = None,
    ) -> models.UpdateCloudRunServerResponse:
        """
        更新云托管服务
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCloudRunServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCloudRunServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)