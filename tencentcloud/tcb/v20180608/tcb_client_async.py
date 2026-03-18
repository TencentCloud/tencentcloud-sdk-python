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

    async def AddProvider(
            self,
            request: models.AddProviderRequest,
            opts: Dict = None,
    ) -> models.AddProviderResponse:
        """
        添加身份认证源。在指定云开发环境下创建一个新的身份认证源，支持 OAuth 2.0、OIDC、SAML 2.0 等标准协议，以及自定义登录和邮箱登录等多种认证方式。
        创建时需指定身份源协议类型（ProviderType）并配置对应的协议连接参数（Config）。若身份源 ID 已存在将返回错误。
        限制：一个环境最大可允许加入20个认证源。
        """
        
        kwargs = {}
        kwargs["action"] = "AddProvider"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddProviderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
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
        
    async def CreateEnvResource(
            self,
            request: models.CreateEnvResourceRequest,
            opts: Dict = None,
    ) -> models.CreateEnvResourceResponse:
        """
        **创建环境日志资源**

        环境开通后，若用户需要开启检索日志功能，需调用此接口进行日志资源的开通。

        > **注意**：日志资源的开通为**异步操作**，接口调用成功后并不代表日志资源已立即可用。

        **如何确认日志开通状态：**

        可通过 [DescribeEnvs](https://cloud.tencent.com/document/product/876/34820) 接口轮询查询日志开通结果，建议每 5 秒轮询一次，最长等待 5 分钟。在返回的数据结构 [EnvInfo](https://cloud.tencent.com/document/api/876/34822#EnvInfo) 中，检查 `LogServices` 字段下 `LogServiceInfo` 是否包含有效的日志主题（Topic）等相关信息，以此判断日志资源是否已成功开通：

        - **已开通**：`LogServiceInfo` 中存在日志主题 ID 等有效信息
        - **未开通 / 开通中**：`LogServiceInfo` 为空或相关字段缺失
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEnvResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEnvResourceResponse
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
        本接口（CreateMySQL）用于开通Mysql型数据库。

        开通后，可通过 [DescribeCreateMySQLResult ](https://cloud.tencent.com/document/api/876/128185) 查询开通结果，Mysql开通成功后，可通过接口设置数据库账号相关功能包括但不限于【创建账号、删除账号、查询可授权权限列表、查询账号已有权限、修改主机、修改配置、修改账号库表权限】、集群操作相关【查询集群参数、修改集群参数】，连接设置相关【关闭外网、开通外网、查询集群信息】，备份回档相关【创建手动回档、删除手动回档、修改自动备份配置信息、查询备份文件列表、集群回档、查询任务列表、获取table列表、获取集群数据库列表、查询备份下载地址】，相关功能接口文档：[TDSQL-C MySQL API文档](https://cloud.tencent.com/document/product/1003/48106)，可以通过 [RunSql](https://cloud.tencent.com/document/api/876/127880) 接口来执行 sql 命令，比如创建表格、插入数据、删除表格等 sql 命令。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMySQL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMySQLResponse
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
        本接口(CreateTable)用于创建文档型数据库表，支持创建capped类型集合，暂时不支持分片表。
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
        
    async def DeleteAuthDomain(
            self,
            request: models.DeleteAuthDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteAuthDomainResponse:
        """
        删除合法域名。
        云开发会校验网页应用请求的来源域名，您需要将来源域名加入到WEB安全域名列表中。
        可以通过接口 [DescribeAuthDomains](https://cloud.tencent.com/document/product/876/42151) 获取当前已绑定生效的安全域名，将对应安全域名的id填入Domainlds中

        注意⚠️
        安全域名被删除之后，可能会引起跨域问题，请谨慎操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuthDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuthDomainResponse
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
        
    async def DeleteProvider(
            self,
            request: models.DeleteProviderRequest,
            opts: Dict = None,
    ) -> models.DeleteProviderResponse:
        """
        删除认证源
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProvider"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProviderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTable(
            self,
            request: models.DeleteTableRequest,
            opts: Dict = None,
    ) -> models.DeleteTableResponse:
        """
        本接口(DeleteTable)用于删除文档型数据库表，删除表后表中数据将会被删除且无法恢复，请谨慎操作。

        接口入参中的 Tag 为文档型数据库的实例 Id，可以通过 [DescribeEnvs](https://cloud.tencent.com/document/api/876/34820) 接口返回的 EnvList[0].Databases[0].InstanceId 获取。
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
        
    async def DescribeClient(
            self,
            request: models.DescribeClientRequest,
            opts: Dict = None,
    ) -> models.DescribeClientResponse:
        """
        查询客户端详情。获取指定云开发环境下某个客户端的配置信息，包括客户端基本信息（名称、图标、描述）、OAuth 凭证（ClientId、ClientSecret）、安全域名、允许的 Scope 列表、Token 有效期、会话控制策略等。当客户端 ID 等于环境 ID 时，返回该环境的默认客户端配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClient"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClientResponse
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
        
    async def DescribeCreateMySQLResult(
            self,
            request: models.DescribeCreateMySQLResultRequest,
            opts: Dict = None,
    ) -> models.DescribeCreateMySQLResultResponse:
        """
        本接口（DescribeCreateMySQLResult）用于查询开通Mysql结果。

        `Response.Data.Status = "notexist"` 表示未开通，如果未开通，可以调用 [CreateMySQL](https://cloud.tencent.com/document/api/876/128186) 来开通
         `Response.Data. Status = "success"` 表示开通成功，Mysql开通成功后，可通过接口设置数据库账号相关功能包括但不限于【创建账号、删除账号、查询可授权权限列表、查询账号已有权限、修改主机、修改配置、修改账号库表权限】、集群操作相关【查询集群参数、修改集群参数】，连接设置相关【关闭外网、开通外网、查询集群信息】，备份回档相关【创建手动回档、删除手动回档、修改自动备份配置信息、查询备份文件列表、集群回档、查询任务列表、获取table列表、获取集群数据库列表、查询备份下载地址】，相关功能接口文档：[TDSQL-C MySQL API文档](https://cloud.tencent.com/document/product/1003/48106)，可以通过 [RunSql](https://cloud.tencent.com/document/api/876/127880) 接口来执行 sql 命令，比如创建表格、插入数据、删除表格等 MySql 命令。
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
        根据指定指标名称，查询某环境在指定时间范围内的监控数据，返回按统计粒度聚合后的时序数据。
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
        本接口（DescribeDatabaseACL）获取文档型数据库权限。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseACLResponse
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
        
    async def DescribeLoginConfig(
            self,
            request: models.DescribeLoginConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeLoginConfigResponse:
        """
        查询指定云开发环境的登录策略配置。包括手机号短信登录、邮箱登录、用户名密码登录和匿名登录方式的开启状态，同时包含短信验证码发送通道、MFA 多因子认证和密码的更新策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoginConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoginConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMySQLClusterDetail(
            self,
            request: models.DescribeMySQLClusterDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMySQLClusterDetailResponse:
        """
        本接口（DescribeMySQLClusterDetail）查询Mysql集群信息。

        调用该接口前需要先查询Mysql是否开通，可通过 [DescribeCreateMySQLResult ](https://cloud.tencent.com/document/api/876/128185) 查询，只有已开通的才能查到集群信息，Mysql开通成功后，可通过接口设置数据库账号相关功能包括但不限于【创建账号、删除账号、查询可授权权限列表、查询账号已有权限、修改主机、修改配置、修改账号库表权限】、集群操作相关【查询集群参数、修改集群参数】，连接设置相关【关闭外网、开通外网、查询集群信息】，备份回档相关【创建手动回档、删除手动回档、修改自动备份配置信息、查询备份文件列表、集群回档、查询任务列表、获取table列表、获取集群数据库列表、查询备份下载地址】，相关功能接口文档：[TDSQL-C MySQL API文档](https://cloud.tencent.com/document/product/1003/48106)，可以通过 [RunSql](https://cloud.tencent.com/document/api/876/127880) 接口来执行 MySql 命令，比如创建表格、插入数据、删除表格等 MySql 命令。
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
        本接口（DescribeMySQLTaskStatus）用于查询Mysql任务状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMySQLTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMySQLTaskStatusResponse
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
        本接口（DescribeTable）用于查询文档型数据库表的相关信息，包括索引等信息。

        接口入参中的 Tag 为文档型数据库的实例 Id，可以通过 [DescribeEnvs](https://cloud.tencent.com/document/api/876/34820) 接口返回的 EnvList[0].Databases[0].InstanceId 获取。
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
        本接口(DescribeTables)用于查询文档型数据库所有表信息，包括表名、表中数据条数、表中数据量、索引个数及索引的大小等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTablesResponse
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
        
    async def DescribeVmSpec(
            self,
            request: models.DescribeVmSpecRequest,
            opts: Dict = None,
    ) -> models.DescribeVmSpecResponse:
        """
        云服务器规格list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVmSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVmSpecResponse
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
        本接口（DestroyMySQL）用于销毁Mysql。

        销毁后可以通过 [DescribeMySQLTaskStatus](https://cloud.tencent.com/document/api/876/128183) 接口查询销毁结果，如果 `Response.Data. Status = FAILED ` 表示销毁失败，可以重新调用销毁接口重试。
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
        
    async def GetProviders(
            self,
            request: models.GetProvidersRequest,
            opts: Dict = None,
    ) -> models.GetProvidersResponse:
        """
        查询指定云开发环境下的身份认证源列表。返回该环境已配置的所有身份认证源信息，包括第三方登录（OAuth、OIDC、SAML）、微信小程序登录、自定义登录和邮箱登录等。返回结果包含认证源基本信息、关联应用、配置状态及启用情况。若自定义登录或邮箱登录的身份源尚未创建，接口会自动追加一个默认关闭状态的身份源记录。
        """
        
        kwargs = {}
        kwargs["action"] = "GetProviders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetProvidersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTables(
            self,
            request: models.ListTablesRequest,
            opts: Dict = None,
    ) -> models.ListTablesResponse:
        """
        本接口(ListTables)用于查询文档型数据库所有表信息，包括表名、表中数据条数、表中数据量、索引个数及索引的大小等。

        该接口跟 [DescribeTables](https://cloud.tencent.com/document/api/876/127962) 接口功能一致，后续该接口可能会下线，请使用 [DescribeTable](https://cloud.tencent.com/document/api/876/127962)接口。
        """
        
        kwargs = {}
        kwargs["action"] = "ListTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClient(
            self,
            request: models.ModifyClientRequest,
            opts: Dict = None,
    ) -> models.ModifyClientResponse:
        """
        修改客户端配置。采用增量更新策略，仅更新请求中传入的非空字段，未传入的字段保持原值不变。支持修改客户端基本信息（名称、图标、描述、主页地址）、安全域名、允许的 Scope 列表、Token 有效期、会话控制策略及启用状态等配置。
        Id、Secret、CreatedAt、Meta 等字段在该接口中不可修改，当客户端 ID 等于环境 ID 且客户端尚未创建时，将自动创建默认客户端配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClient"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClientResponse
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
        本接口（ModifyDatabaseACL）用于修改文档型数据库权限。
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
        
    async def ModifyLoginConfig(
            self,
            request: models.ModifyLoginConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyLoginConfigResponse:
        """
        修改指定云开发环境的登录策略配置。支持开启或关闭手机号短信登录、邮箱登录、用户名密码登录和匿名登录，同时可配置短信验证码发送通道、MFA 多因子认证和密码更新策略。
        修改后立即生效，影响该环境下所有终端用户的登录行为。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoginConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoginConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProvider(
            self,
            request: models.ModifyProviderRequest,
            opts: Dict = None,
    ) -> models.ModifyProviderResponse:
        """
        修改身份认证源。更新指定云开发环境下已有身份认证源的配置信息，支持修改基本信息（名称、图标、描述）、协议连接配置（ClientId、ClientSecret、端点地址等）、登录行为控制（透传模式、自动注册、邮箱/手机号自动关联）以及启用状态。
        对于 OIDC 类型身份源，修改 Issuer 后将自动通过 OpenID Connect Discovery 重新获取端点配置。
        若自定义登录（CUSTOM）或邮箱登录（EMAIL）身份源尚不存在，调用该接口时将自动创建。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProvider"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProviderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySafeRule(
            self,
            request: models.ModifySafeRuleRequest,
            opts: Dict = None,
    ) -> models.ModifySafeRuleResponse:
        """
        设置数据库安全规则。
        安全规则，用于控制C端用户的访问权限。详见 [安全规则介绍 ](https://cloud.tencent.com/document/product/876/123478)。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySafeRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySafeRuleResponse
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
        
    async def RunCommands(
            self,
            request: models.RunCommandsRequest,
            opts: Dict = None,
    ) -> models.RunCommandsResponse:
        """
        本接口（RunCommands）用于执行文档型数据库命令。
        """
        
        kwargs = {}
        kwargs["action"] = "RunCommands"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunCommandsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunSql(
            self,
            request: models.RunSqlRequest,
            opts: Dict = None,
    ) -> models.RunSqlResponse:
        """
        本接口（RunSql）用于执行MySQL语句。

        该接口用来执行 MySql 语句，比如创建表格、插入数据、修改数据、删除字段、添加索引等可以通过sql 语句实现的都可以使用该接口。

        调用该接口前需要先查询Mysql是否开通，可通过 [DescribeCreateMySQLResult ](https://cloud.tencent.com/document/api/876/128185) 查询，只有开通成功才能操作。
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
        
    async def UpdateTable(
            self,
            request: models.UpdateTableRequest,
            opts: Dict = None,
    ) -> models.UpdateTableResponse:
        """
        本接口(UpdateTable)用于修改文档型数据库表信息，当前可以支持创建和删除索引。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)