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

    async def BindCloudBaseAccessDomain(
            self,
            request: models.BindCloudBaseAccessDomainRequest,
            opts: Dict = None,
    ) -> models.BindCloudBaseAccessDomainResponse:
        """
        绑定云开发自定义域名，用于云接入和静态托管
        """
        
        kwargs = {}
        kwargs["action"] = "BindCloudBaseAccessDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindCloudBaseAccessDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindCloudBaseGWDomain(
            self,
            request: models.BindCloudBaseGWDomainRequest,
            opts: Dict = None,
    ) -> models.BindCloudBaseGWDomainResponse:
        """
        绑定自定义域名
        """
        
        kwargs = {}
        kwargs["action"] = "BindCloudBaseGWDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindCloudBaseGWDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
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
        增加安全域名。
        云开发会校验网页应用请求的来源域名，您需要将来源域名加入到WEB安全域名列表中。
        可以通过接口 [DescribeAuthDomains](https://cloud.tencent.com/document/product/876/42151) 获取当前已绑定生效的安全域名。

        注意⚠️
          安全域名绑定成功之后，需要几分钟时间逐步生效。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuthDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuthDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBillDeal(
            self,
            request: models.CreateBillDealRequest,
            opts: Dict = None,
    ) -> models.CreateBillDealResponse:
        """
        创建云开发产品计费订单，用于以下几种场景：
        1. 购买云开发环境
        2. 续费云开发环境
        3. 变更云开发环境套餐
        4. 购买云开发资源包
        5. 购买云开发大促包

        该接口支持下单并支付(CreateAndPay=true时)，此时会自动在腾讯云账户中扣除余额（余额不足会下单失败）。
        该接口支持自动扣除代金券（AutoVoucher=true时），符合条件的代金券会被自动扣除。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBillDeal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBillDealResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudBaseGWAPI(
            self,
            request: models.CreateCloudBaseGWAPIRequest,
            opts: Dict = None,
    ) -> models.CreateCloudBaseGWAPIResponse:
        """
        创建云开发网关API
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudBaseGWAPI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudBaseGWAPIResponse
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
        
    async def CreateEnv(
            self,
            request: models.CreateEnvRequest,
            opts: Dict = None,
    ) -> models.CreateEnvResponse:
        """
        本接口用于购买云开发环境。
        该接口会自动下单并支付，会在腾讯云账户中扣除余额（余额不足会下单失败）。
        该接口支持自动扣除代金券（AutoVoucher=true时），符合条件的代金券会被自动扣除。
        环境下单成功之后会返回EnvId。EnvId是全局唯一表示。
        环境发货是异步行为，后续可以通过接口 [DescribeEnvs ](https://cloud.tencent.com/document/product/876/34820) 查询环境状态和各项资源信息；通过 [DescribeBillingInfo](https://cloud.tencent.com/document/product/876/94390) 查询环境套餐信息，包括 到期时间、当前套餐等。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEnvResponse
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
        
    async def CreateMySQL(
            self,
            request: models.CreateMySQLRequest,
            opts: Dict = None,
    ) -> models.CreateMySQLResponse:
        """
        开通Mysql
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMySQL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMySQLResponse
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
        
    async def CreateTable(
            self,
            request: models.CreateTableRequest,
            opts: Dict = None,
    ) -> models.CreateTableResponse:
        """
        本接口(CreateTable)用于创建表，支持创建capped类型集合，暂时不支持分片表
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUser(
            self,
            request: models.CreateUserRequest,
            opts: Dict = None,
    ) -> models.CreateUserResponse:
        """
        创建tcb用户
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudBaseGWAPI(
            self,
            request: models.DeleteCloudBaseGWAPIRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudBaseGWAPIResponse:
        """
        删除网关API
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudBaseGWAPI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudBaseGWAPIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudBaseGWDomain(
            self,
            request: models.DeleteCloudBaseGWDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudBaseGWDomainResponse:
        """
        删除网关域名
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudBaseGWDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudBaseGWDomainResponse
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
        
    async def DeleteTable(
            self,
            request: models.DeleteTableRequest,
            opts: Dict = None,
    ) -> models.DeleteTableResponse:
        """
        本接口(DeleteTable)用于删除表，删除表后表中数据将会被删除且无法恢复，请谨慎操作
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUsers(
            self,
            request: models.DeleteUsersRequest,
            opts: Dict = None,
    ) -> models.DeleteUsersResponse:
        """
        删除tcb用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUsersResponse
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
        本接口用于获取当前环境的安全域名列表。
        云开发会校验网页应用请求的来源域名，您需要将来源域名加入到WEB安全域名列表中。
        可以通过接口 [CreateAuthDomain](https://cloud.tencent.com/document/product/876/42764) 增加安全域名。
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
        
    async def DescribeCloudBaseGWAPI(
            self,
            request: models.DescribeCloudBaseGWAPIRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseGWAPIResponse:
        """
        获取网关API列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseGWAPI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseGWAPIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudBaseGWService(
            self,
            request: models.DescribeCloudBaseGWServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudBaseGWServiceResponse:
        """
        获取网关服务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudBaseGWService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudBaseGWServiceResponse
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
        
    async def DescribeCreateMySQLResult(
            self,
            request: models.DescribeCreateMySQLResultRequest,
            opts: Dict = None,
    ) -> models.DescribeCreateMySQLResultResponse:
        """
        查询开通Mysql结果，Mysql开通成功后，可通过接口设置数据库账号相关功能包括但不限于【创建账号、删除账号、查询可授权权限列表、查询账号已有权限、修改主机、修改配置、修改账号库表权限】、集群操作相关【查询集群参数、修改集群参数】，连接设置相关【关闭外网、开通外网、查询集群信息】，备份回档相关【创建手动回档、删除手动回档、修改自动备份配置信息、查询备份文件列表、集群回档、查询任务列表、获取table列表、获取集群数据库列表、查询备份下载地址】，相关功能接口文档：[TDSQL-C MySQL API文档](https://cloud.tencent.com/document/product/1003/48106)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCreateMySQLResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCreateMySQLResultResponse
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
        
    async def DescribeEnvAccountCircle(
            self,
            request: models.DescribeEnvAccountCircleRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvAccountCircleResponse:
        """
        查询环境计费周期。
        云开发环境的资源点都是按月结算的，每个月都有一定的抵扣额度。

        例如：
          某个环境在 2026-01-05 购买了3个月个人版(到期时间: 2026-04-05)，则他可以在以下3个周期内，分别享有40000资源点的额度：
          1. 2026-01-05 ~ 2026-02-05 23:59:59
          2. 2026-02-06 ~ 2026-03-05 23:59:59
          3. 2026-03-06 ~ 2026-04-05 23:59:59

        本接口，用于获取环境当前属于哪个计费周期内。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvAccountCircle"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvAccountCircleResponse
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
        
    async def DescribeMySQLClusterDetail(
            self,
            request: models.DescribeMySQLClusterDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMySQLClusterDetailResponse:
        """
        销毁Mysql
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMySQLClusterDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMySQLClusterDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMySQLTaskStatus(
            self,
            request: models.DescribeMySQLTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeMySQLTaskStatusResponse:
        """
        查询Mysql任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMySQLTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMySQLTaskStatusResponse
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
        
    async def DescribeSafeRule(
            self,
            request: models.DescribeSafeRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeSafeRuleResponse:
        """
        查询数据库安全规则。
        安全规则，用于控制C端用户的访问权限。详见 [安全规则介绍](https://cloud.tencent.com/document/product/876/123478) 。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSafeRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSafeRuleResponse
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
        
    async def DescribeStaticStore(
            self,
            request: models.DescribeStaticStoreRequest,
            opts: Dict = None,
    ) -> models.DescribeStaticStoreResponse:
        """
        查看当前环境下静态托管资源信息，根据返回结果判断静态资源的状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStaticStore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStaticStoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTable(
            self,
            request: models.DescribeTableRequest,
            opts: Dict = None,
    ) -> models.DescribeTableResponse:
        """
        查询表的相关信息，包括索引等信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTables(
            self,
            request: models.DescribeTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeTablesResponse:
        """
        本接口(ListTables)用于查询所有表信息，包括表名、表中数据条数、表中数据量、索引个数及索引的大小等
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTablesResponse
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
        
    async def DescribeUserList(
            self,
            request: models.DescribeUserListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserListResponse:
        """
        查询tcb用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserListResponse
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
        本接口用于销毁云开发环境。
        云开发环境遵循腾讯云包年包月预付费产品生命周期，因此环境销毁需要分两步：
        1. 资源退费。此时会根据当前环境剩余有效期，自动退还相关费用(代金券不退)。退款后，环境进入隔离期。
        2. 环境删除。环境在进入隔离期后15天会自动删除。也可以通过本接口，指定 IsForce=true 来强制删除隔离期环境。

        **注意**⚠️
          1. 环境退费后进入隔离期，则所有资源均无法访问，控制台无法操作和管理。
          2. 环境被彻底删除后，所有数据均无法找回。请谨慎操作。

        可以通过接口 [tcb:DescribeBillingInfo](https://cloud.tencent.com/document/product/876/94390) 查询环境计费状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyEnvResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyMySQL(
            self,
            request: models.DestroyMySQLRequest,
            opts: Dict = None,
    ) -> models.DestroyMySQLResponse:
        """
        销毁Mysql
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyMySQL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyMySQLResponse
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
        
    async def ListTables(
            self,
            request: models.ListTablesRequest,
            opts: Dict = None,
    ) -> models.ListTablesResponse:
        """
        本接口(ListTables)用于查询所有表信息，包括表名、表中数据条数、表中数据量、索引个数及索引的大小等
        """
        
        kwargs = {}
        kwargs["action"] = "ListTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudBaseGWAPI(
            self,
            request: models.ModifyCloudBaseGWAPIRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudBaseGWAPIResponse:
        """
        修改云开发网关API
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudBaseGWAPI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudBaseGWAPIResponse
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
        
    async def ModifyEnvPlan(
            self,
            request: models.ModifyEnvPlanRequest,
            opts: Dict = None,
    ) -> models.ModifyEnvPlanResponse:
        """
        本接口用于变更云开发环境套餐。
        该接口会自动下单并支付，会在腾讯云账户中扣除余额（余额不足会下单失败）。
        该接口支持自动扣除代金券（AutoVoucher=true时），符合条件的代金券会被自动扣除。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEnvPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEnvPlanResponse
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
        
    async def ModifyUser(
            self,
            request: models.ModifyUserRequest,
            opts: Dict = None,
    ) -> models.ModifyUserResponse:
        """
        修改tcb用户
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserResponse
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
        
    async def RenewEnv(
            self,
            request: models.RenewEnvRequest,
            opts: Dict = None,
    ) -> models.RenewEnvResponse:
        """
        本接口用于云开发环境套餐续费。
        该接口会自动下单并支付，会在腾讯云账户中扣除余额（余额不足会下单失败）。
        该接口支持自动扣除代金券（AutoVoucher=true时），符合条件的代金券会被自动扣除。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewEnvResponse
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
        
    async def RunSql(
            self,
            request: models.RunSqlRequest,
            opts: Dict = None,
    ) -> models.RunSqlResponse:
        """
        执行SQL语句
        """
        
        kwargs = {}
        kwargs["action"] = "RunSql"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunSqlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchClsLog(
            self,
            request: models.SearchClsLogRequest,
            opts: Dict = None,
    ) -> models.SearchClsLogResponse:
        """
        搜索用户调用日志
        """
        
        kwargs = {}
        kwargs["action"] = "SearchClsLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchClsLogResponse
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
        
    async def UpdateTable(
            self,
            request: models.UpdateTableRequest,
            opts: Dict = None,
    ) -> models.UpdateTableResponse:
        """
        本接口(UpdateTable)用于修改表信息，当前可以支持创建和删除索引
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)