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
from tencentcloud.tcb.v20180608 import models
from typing import Dict


class TcbClient(AbstractClient):
    _apiVersion = '2018-06-08'
    _endpoint = 'tcb.tencentcloudapi.com'
    _service = 'tcb'

    async def BindEnvGateway(
            self,
            request: models.BindEnvGatewayRequest,
            opts: Dict = None,
    ) -> models.BindEnvGatewayResponse:
        """
        绑定另外一个环境下的网关，callContainer请求可以访问到该网关
        """
        
        kwargs = {}
        kwargs["action"] = "BindEnvGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindEnvGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckTcbService(
            self,
            request: models.CheckTcbServiceRequest,
            opts: Dict = None,
    ) -> models.CheckTcbServiceResponse:
        """
        检查是否开通Tcb服务
        """
        
        kwargs = {}
        kwargs["action"] = "CheckTcbService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckTcbServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CommonServiceAPI(
            self,
            request: models.CommonServiceAPIRequest,
            opts: Dict = None,
    ) -> models.CommonServiceAPIResponse:
        """
        TCB云API统一入口
        """
        
        kwargs = {}
        kwargs["action"] = "CommonServiceAPI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CommonServiceAPIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAndDeployCloudBaseProject(
            self,
            request: models.CreateAndDeployCloudBaseProjectRequest,
            opts: Dict = None,
    ) -> models.CreateAndDeployCloudBaseProjectResponse:
        """
        创建云开发项目
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAndDeployCloudBaseProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAndDeployCloudBaseProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAuthDomain(
            self,
            request: models.CreateAuthDomainRequest,
            opts: Dict = None,
    ) -> models.CreateAuthDomainResponse:
        """
        增加安全域名
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuthDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuthDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudBaseRunResource(
            self,
            request: models.CreateCloudBaseRunResourceRequest,
            opts: Dict = None,
    ) -> models.CreateCloudBaseRunResourceResponse:
        """
        开通容器托管的资源，包括集群创建，VPC配置，异步任务创建，镜像托管，Coding等，查看创建结果需要根据DescribeCloudBaseRunResource接口来查看
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudBaseRunResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudBaseRunResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudBaseRunServerVersion(
            self,
            request: models.CreateCloudBaseRunServerVersionRequest,
            opts: Dict = None,
    ) -> models.CreateCloudBaseRunServerVersionResponse:
        """
        创建服务版本
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudBaseRunServerVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudBaseRunServerVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHostingDomain(
            self,
            request: models.CreateHostingDomainRequest,
            opts: Dict = None,
    ) -> models.CreateHostingDomainResponse:
        """
        创建托管域名
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHostingDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHostingDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePostpayPackage(
            self,
            request: models.CreatePostpayPackageRequest,
            opts: Dict = None,
    ) -> models.CreatePostpayPackageResponse:
        """
        开通后付费资源
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePostpayPackage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePostpayPackageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStandaloneGateway(
            self,
            request: models.CreateStandaloneGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateStandaloneGatewayResponse:
        """
        本接口（CreateStandaloneGateway）用于创建独立网关。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStandaloneGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStandaloneGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStaticStore(
            self,
            request: models.CreateStaticStoreRequest,
            opts: Dict = None,
    ) -> models.CreateStaticStoreResponse:
        """
        创建静态托管资源，包括COS和CDN，异步任务创建，查看创建结果需要根据DescribeStaticStore接口来查看
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStaticStore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStaticStoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWxCloudBaseRunEnv(
            self,
            request: models.CreateWxCloudBaseRunEnvRequest,
            opts: Dict = None,
    ) -> models.CreateWxCloudBaseRunEnvResponse:
        """
        创建微信云托管
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWxCloudBaseRunEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWxCloudBaseRunEnvResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWxCloudBaseRunServerDBCluster(
            self,
            request: models.CreateWxCloudBaseRunServerDBClusterRequest,
            opts: Dict = None,
    ) -> models.CreateWxCloudBaseRunServerDBClusterResponse:
        """
        开通微信云托管MySQL数据库服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWxCloudBaseRunServerDBCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWxCloudBaseRunServerDBClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudBaseProjectLatestVersion(
            self,
            request: models.DeleteCloudBaseProjectLatestVersionRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudBaseProjectLatestVersionResponse:
        """
        删除云项目
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudBaseProjectLatestVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudBaseProjectLatestVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudBaseRunServerVersion(
            self,
            request: models.DeleteCloudBaseRunServerVersionRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudBaseRunServerVersionResponse:
        """
        删除服务版本
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudBaseRunServerVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudBaseRunServerVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEndUser(
            self,
            request: models.DeleteEndUserRequest,
            opts: Dict = None,
    ) -> models.DeleteEndUserResponse:
        """
        删除终端用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEndUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEndUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGatewayVersion(
            self,
            request: models.DeleteGatewayVersionRequest,
            opts: Dict = None,
    ) -> models.DeleteGatewayVersionResponse:
        """
        删除网关某版本
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGatewayVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGatewayVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWxGatewayRoute(
            self,
            request: models.DeleteWxGatewayRouteRequest,
            opts: Dict = None,
    ) -> models.DeleteWxGatewayRouteResponse:
        """
        删除安全网关路由
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWxGatewayRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWxGatewayRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeActivityRecord(
            self,
            request: models.DescribeActivityRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeActivityRecordResponse:
        """
        查询活动记录信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeActivityRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeActivityRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuthDomains(
            self,
            request: models.DescribeAuthDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeAuthDomainsResponse:
        """
        获取安全域名列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuthDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuthDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaasPackageList(
            self,
            request: models.DescribeBaasPackageListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaasPackageListResponse:
        """
        获取新套餐列表，含详情，如果传了PackageId，则只获取指定套餐详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaasPackageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaasPackageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillingInfo(
            self,
            request: models.DescribeBillingInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeBillingInfoResponse:
        """
        获取计费相关信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillingInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillingInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCbrServerVersion(
            self,
            request: models.DescribeCbrServerVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeCbrServerVersionResponse:
        """
        查询服务版本的详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCbrServerVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCbrServerVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudBaseBuildService(
            self,
            request: models.DescribeCloudBaseBuildServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseBuildServiceResponse:
        """
        获取云托管代码上传url
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseBuildService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseBuildServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudBaseProjectLatestVersionList(
            self,
            request: models.DescribeCloudBaseProjectLatestVersionListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseProjectLatestVersionListResponse:
        """
        获取云开发项目列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseProjectLatestVersionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseProjectLatestVersionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudBaseProjectVersionList(
            self,
            request: models.DescribeCloudBaseProjectVersionListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseProjectVersionListResponse:
        """
        云项目部署列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseProjectVersionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseProjectVersionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudBaseRunAllVpcs(
            self,
            request: models.DescribeCloudBaseRunAllVpcsRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseRunAllVpcsResponse:
        """
        查询环境下所有的vpc列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseRunAllVpcs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseRunAllVpcsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudBaseRunConfForGateWay(
            self,
            request: models.DescribeCloudBaseRunConfForGateWayRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseRunConfForGateWayResponse:
        """
        独立网关中拉取云托管服务对应的配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseRunConfForGateWay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseRunConfForGateWayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudBaseRunOneClickTaskExternal(
            self,
            request: models.DescribeCloudBaseRunOneClickTaskExternalRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseRunOneClickTaskExternalResponse:
        """
        查询一键部署任务 （特定接口：外部查询使用）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseRunOneClickTaskExternal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseRunOneClickTaskExternalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudBaseRunOperationTypes(
            self,
            request: models.DescribeCloudBaseRunOperationTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseRunOperationTypesResponse:
        """
        查询服务、版本和操作类型
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseRunOperationTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseRunOperationTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudBaseRunPodList(
            self,
            request: models.DescribeCloudBaseRunPodListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseRunPodListResponse:
        """
        查询云托管服务版本容器列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseRunPodList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseRunPodListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudBaseRunResource(
            self,
            request: models.DescribeCloudBaseRunResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseRunResourceResponse:
        """
        查看容器托管的集群状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseRunResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseRunResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudBaseRunResourceForExtend(
            self,
            request: models.DescribeCloudBaseRunResourceForExtendRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseRunResourceForExtendResponse:
        """
        查看容器托管的集群状态扩展使用
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseRunResourceForExtend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseRunResourceForExtendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudBaseRunServer(
            self,
            request: models.DescribeCloudBaseRunServerRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseRunServerResponse:
        """
        查询单个服务的详情，版本以及详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseRunServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseRunServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudBaseRunServerDomainName(
            self,
            request: models.DescribeCloudBaseRunServerDomainNameRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseRunServerDomainNameResponse:
        """
        查询微信云托管服务域名
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseRunServerDomainName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseRunServerDomainNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudBaseRunServerVersion(
            self,
            request: models.DescribeCloudBaseRunServerVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseRunServerVersionResponse:
        """
        查询服务版本的详情，CPU和MEM  请使用CPUSize和MemSize
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseRunServerVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseRunServerVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudBaseRunVersion(
            self,
            request: models.DescribeCloudBaseRunVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseRunVersionResponse:
        """
        查询服务版本详情(新)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseRunVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseRunVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudBaseRunVersionRsByCondition(
            self,
            request: models.DescribeCloudBaseRunVersionRsByConditionRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseRunVersionRsByConditionResponse:
        """
        DescribeCloudBaseRunVersionRsByCondition 获取云托管详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseRunVersionRsByCondition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseRunVersionRsByConditionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudBaseRunVersionSnapshot(
            self,
            request: models.DescribeCloudBaseRunVersionSnapshotRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseRunVersionSnapshotResponse:
        """
        查询版本历史
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseRunVersionSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseRunVersionSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCurveData(
            self,
            request: models.DescribeCurveDataRequest,
            opts: Dict = None,
    ) -> models.DescribeCurveDataResponse:
        """
        根据用户传入的指标, 拉取一段时间内的监控数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCurveData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCurveDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseACL(
            self,
            request: models.DescribeDatabaseACLRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseACLResponse:
        """
        获取数据库权限
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDownloadFile(
            self,
            request: models.DescribeDownloadFileRequest,
            opts: Dict = None,
    ) -> models.DescribeDownloadFileResponse:
        """
        获取下载文件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDownloadFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDownloadFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEndUserLoginStatistic(
            self,
            request: models.DescribeEndUserLoginStatisticRequest,
            opts: Dict = None,
    ) -> models.DescribeEndUserLoginStatisticResponse:
        """
        获取环境终端用户新增与登录信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEndUserLoginStatistic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEndUserLoginStatisticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEndUserStatistic(
            self,
            request: models.DescribeEndUserStatisticRequest,
            opts: Dict = None,
    ) -> models.DescribeEndUserStatisticResponse:
        """
        获取终端用户总量与平台分布情况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEndUserStatistic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEndUserStatisticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEndUsers(
            self,
            request: models.DescribeEndUsersRequest,
            opts: Dict = None,
    ) -> models.DescribeEndUsersResponse:
        """
        获取终端用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEndUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEndUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvDealRegion(
            self,
            request: models.DescribeEnvDealRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvDealRegionResponse:
        """
        获取环境下单地域
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvDealRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvDealRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvFreeQuota(
            self,
            request: models.DescribeEnvFreeQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvFreeQuotaResponse:
        """
        查询后付费免费配额信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvFreeQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvFreeQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvLimit(
            self,
            request: models.DescribeEnvLimitRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvLimitResponse:
        """
        查询环境个数上限
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvPostpaidDeduct(
            self,
            request: models.DescribeEnvPostpaidDeductRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvPostpaidDeductResponse:
        """
        查询环境后付费计费详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvPostpaidDeduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvPostpaidDeductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvs(
            self,
            request: models.DescribeEnvsRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvsResponse:
        """
        获取环境列表，含环境下的各个资源信息。尤其是各资源的唯一标识，是请求各资源的关键参数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExtensionUploadInfo(
            self,
            request: models.DescribeExtensionUploadInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeExtensionUploadInfoResponse:
        """
        描述扩展上传文件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExtensionUploadInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExtensionUploadInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExtraPkgBillingInfo(
            self,
            request: models.DescribeExtraPkgBillingInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeExtraPkgBillingInfoResponse:
        """
        获取增值包计费相关信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExtraPkgBillingInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExtraPkgBillingInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayCurveData(
            self,
            request: models.DescribeGatewayCurveDataRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayCurveDataResponse:
        """
        查询网关监控数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayCurveData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayCurveDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayVersions(
            self,
            request: models.DescribeGatewayVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayVersionsResponse:
        """
        查询网关版本信息
        暂不鉴权
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGraphData(
            self,
            request: models.DescribeGraphDataRequest,
            opts: Dict = None,
    ) -> models.DescribeGraphDataResponse:
        """
        根据用户传入的指标, 拉取一段时间内的监控数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGraphData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGraphDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostingDomainTask(
            self,
            request: models.DescribeHostingDomainTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeHostingDomainTaskResponse:
        """
        查询静态托管域名任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostingDomainTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostingDomainTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePostpayFreeQuotas(
            self,
            request: models.DescribePostpayFreeQuotasRequest,
            opts: Dict = None,
    ) -> models.DescribePostpayFreeQuotasResponse:
        """
        查询后付费资源免费量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePostpayFreeQuotas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePostpayFreeQuotasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePostpayPackageFreeQuotas(
            self,
            request: models.DescribePostpayPackageFreeQuotasRequest,
            opts: Dict = None,
    ) -> models.DescribePostpayPackageFreeQuotasResponse:
        """
        获取后付费免费额度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePostpayPackageFreeQuotas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePostpayPackageFreeQuotasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQuotaData(
            self,
            request: models.DescribeQuotaDataRequest,
            opts: Dict = None,
    ) -> models.DescribeQuotaDataResponse:
        """
        查询指定指标的配额使用量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQuotaData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQuotaDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSmsQuotas(
            self,
            request: models.DescribeSmsQuotasRequest,
            opts: Dict = None,
    ) -> models.DescribeSmsQuotasResponse:
        """
        查询后付费短信资源量
        1 有免费包的返回SmsFreeQuota结构所有字段
        2 没有免费包，有付费包，付费返回复用SmsFreeQuota结构，其中只有 TodayUsedQuota 字段有效
        3 都没有返回为空数组
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSmsQuotas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSmsQuotasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpecialCostItems(
            self,
            request: models.DescribeSpecialCostItemsRequest,
            opts: Dict = None,
    ) -> models.DescribeSpecialCostItemsResponse:
        """
        查询环境1分钱抵扣信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpecialCostItems"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpecialCostItemsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStandaloneGateway(
            self,
            request: models.DescribeStandaloneGatewayRequest,
            opts: Dict = None,
    ) -> models.DescribeStandaloneGatewayResponse:
        """
        本接口（DescribeStandaloneGateway）查询小租户网关套餐信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStandaloneGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStandaloneGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStandaloneGatewayPackage(
            self,
            request: models.DescribeStandaloneGatewayPackageRequest,
            opts: Dict = None,
    ) -> models.DescribeStandaloneGatewayPackageResponse:
        """
        本接口（DescribeStandaloneGatewayPackage）用于查询小租户网关套餐信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStandaloneGatewayPackage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStandaloneGatewayPackageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserActivityInfo(
            self,
            request: models.DescribeUserActivityInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUserActivityInfoResponse:
        """
        查询用户活动信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserActivityInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserActivityInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWxCloudBaseRunEnvs(
            self,
            request: models.DescribeWxCloudBaseRunEnvsRequest,
            opts: Dict = None,
    ) -> models.DescribeWxCloudBaseRunEnvsResponse:
        """
        查询微信云托管环境信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWxCloudBaseRunEnvs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWxCloudBaseRunEnvsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWxCloudBaseRunSubNets(
            self,
            request: models.DescribeWxCloudBaseRunSubNetsRequest,
            opts: Dict = None,
    ) -> models.DescribeWxCloudBaseRunSubNetsResponse:
        """
        查询微信云托管子网
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWxCloudBaseRunSubNets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWxCloudBaseRunSubNetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWxGatewayRoutes(
            self,
            request: models.DescribeWxGatewayRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeWxGatewayRoutesResponse:
        """
        查看安全网关路由
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWxGatewayRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWxGatewayRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWxGateways(
            self,
            request: models.DescribeWxGatewaysRequest,
            opts: Dict = None,
    ) -> models.DescribeWxGatewaysResponse:
        """
        查看安全网关
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWxGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWxGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyEnv(
            self,
            request: models.DestroyEnvRequest,
            opts: Dict = None,
    ) -> models.DestroyEnvResponse:
        """
        销毁环境
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyEnvResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyStandaloneGateway(
            self,
            request: models.DestroyStandaloneGatewayRequest,
            opts: Dict = None,
    ) -> models.DestroyStandaloneGatewayResponse:
        """
        本接口（DestroyStandaloneGateway）用于销毁小租户网关。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyStandaloneGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyStandaloneGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyStaticStore(
            self,
            request: models.DestroyStaticStoreRequest,
            opts: Dict = None,
    ) -> models.DestroyStaticStoreResponse:
        """
        销毁静态托管资源，该接口创建异步销毁任务，资源最终状态可从DestroyStaticStore接口查看
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyStaticStore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyStaticStoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditAuthConfig(
            self,
            request: models.EditAuthConfigRequest,
            opts: Dict = None,
    ) -> models.EditAuthConfigResponse:
        """
        修改登录配置
        """
        
        kwargs = {}
        kwargs["action"] = "EditAuthConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditAuthConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EstablishCloudBaseRunServer(
            self,
            request: models.EstablishCloudBaseRunServerRequest,
            opts: Dict = None,
    ) -> models.EstablishCloudBaseRunServerResponse:
        """
        创建云应用服务
        """
        
        kwargs = {}
        kwargs["action"] = "EstablishCloudBaseRunServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EstablishCloudBaseRunServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EstablishWxGatewayRoute(
            self,
            request: models.EstablishWxGatewayRouteRequest,
            opts: Dict = None,
    ) -> models.EstablishWxGatewayRouteResponse:
        """
        创建或修改安全网关路由
        """
        
        kwargs = {}
        kwargs["action"] = "EstablishWxGatewayRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EstablishWxGatewayRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FreezeCloudBaseRunServers(
            self,
            request: models.FreezeCloudBaseRunServersRequest,
            opts: Dict = None,
    ) -> models.FreezeCloudBaseRunServersResponse:
        """
        批量冻结
        """
        
        kwargs = {}
        kwargs["action"] = "FreezeCloudBaseRunServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FreezeCloudBaseRunServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudBaseRunServerFlowConf(
            self,
            request: models.ModifyCloudBaseRunServerFlowConfRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudBaseRunServerFlowConfResponse:
        """
        修改容器内的版本流量配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudBaseRunServerFlowConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudBaseRunServerFlowConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudBaseRunServerVersion(
            self,
            request: models.ModifyCloudBaseRunServerVersionRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudBaseRunServerVersionResponse:
        """
        修改服务版本的副本数，环境变量
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudBaseRunServerVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudBaseRunServerVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClsTopic(
            self,
            request: models.ModifyClsTopicRequest,
            opts: Dict = None,
    ) -> models.ModifyClsTopicResponse:
        """
        修改日志主题
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClsTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClsTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatabaseACL(
            self,
            request: models.ModifyDatabaseACLRequest,
            opts: Dict = None,
    ) -> models.ModifyDatabaseACLResponse:
        """
        修改数据库权限
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatabaseACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatabaseACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEndUser(
            self,
            request: models.ModifyEndUserRequest,
            opts: Dict = None,
    ) -> models.ModifyEndUserResponse:
        """
        管理终端用户
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEndUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEndUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEnv(
            self,
            request: models.ModifyEnvRequest,
            opts: Dict = None,
    ) -> models.ModifyEnvResponse:
        """
        更新环境信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEnvResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGatewayVersionTraffic(
            self,
            request: models.ModifyGatewayVersionTrafficRequest,
            opts: Dict = None,
    ) -> models.ModifyGatewayVersionTrafficResponse:
        """
        设置网关版本的流量比例
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGatewayVersionTraffic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGatewayVersionTrafficResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReinstateEnv(
            self,
            request: models.ReinstateEnvRequest,
            opts: Dict = None,
    ) -> models.ReinstateEnvResponse:
        """
        针对已隔离的免费环境，可以通过本接口将其恢复访问。
        """
        
        kwargs = {}
        kwargs["action"] = "ReinstateEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReinstateEnvResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceActivityRecord(
            self,
            request: models.ReplaceActivityRecordRequest,
            opts: Dict = None,
    ) -> models.ReplaceActivityRecordResponse:
        """
        更新活动详情
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceActivityRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceActivityRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollUpdateCloudBaseRunServerVersion(
            self,
            request: models.RollUpdateCloudBaseRunServerVersionRequest,
            opts: Dict = None,
    ) -> models.RollUpdateCloudBaseRunServerVersionResponse:
        """
        针对特定的版本，进行滚动更新
        """
        
        kwargs = {}
        kwargs["action"] = "RollUpdateCloudBaseRunServerVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollUpdateCloudBaseRunServerVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchClsLog(
            self,
            request: models.SearchClsLogRequest,
            opts: Dict = None,
    ) -> models.SearchClsLogResponse:
        """
        搜索CLS日志，TCB角色密钥访问
        """
        
        kwargs = {}
        kwargs["action"] = "SearchClsLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchClsLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TurnOffStandaloneGateway(
            self,
            request: models.TurnOffStandaloneGatewayRequest,
            opts: Dict = None,
    ) -> models.TurnOffStandaloneGatewayResponse:
        """
        本接口（TurnOffStandaloneGateway）用于关闭小租户网关。
        """
        
        kwargs = {}
        kwargs["action"] = "TurnOffStandaloneGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TurnOffStandaloneGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TurnOnStandaloneGateway(
            self,
            request: models.TurnOnStandaloneGatewayRequest,
            opts: Dict = None,
    ) -> models.TurnOnStandaloneGatewayResponse:
        """
        本接口（TurnOnStandaloneGateway）用于开启小租户网关。
        """
        
        kwargs = {}
        kwargs["action"] = "TurnOnStandaloneGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TurnOnStandaloneGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnfreezeCloudBaseRunServers(
            self,
            request: models.UnfreezeCloudBaseRunServersRequest,
            opts: Dict = None,
    ) -> models.UnfreezeCloudBaseRunServersResponse:
        """
        批量解冻服务
        """
        
        kwargs = {}
        kwargs["action"] = "UnfreezeCloudBaseRunServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnfreezeCloudBaseRunServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)