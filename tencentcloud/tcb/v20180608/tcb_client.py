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
from tencentcloud.tcb.v20180608 import models


class TcbClient(AbstractClient):
    _apiVersion = '2018-06-08'
    _endpoint = 'tcb.tencentcloudapi.com'
    _service = 'tcb'


    def AddProvider(self, request):
        r"""添加身份认证源。在指定云开发环境下创建一个新的身份认证源，支持 OAuth 2.0、OIDC、SAML 2.0 等标准协议，以及自定义登录和邮箱登录等多种认证方式。
        创建时需指定身份源协议类型（ProviderType）并配置对应的协议连接参数（Config）。若身份源 ID 已存在将返回错误。
        限制：一个环境最大可允许加入20个认证源。

        :param request: Request instance for AddProvider.
        :type request: :class:`tencentcloud.tcb.v20180608.models.AddProviderRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.AddProviderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddProvider", params, headers=headers)
            response = json.loads(body)
            model = models.AddProviderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AllocateEnv(self, request):
        r"""从环境池里立即取出1个环境

        :param request: Request instance for AllocateEnv.
        :type request: :class:`tencentcloud.tcb.v20180608.models.AllocateEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.AllocateEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AllocateEnv", params, headers=headers)
            response = json.loads(body)
            model = models.AllocateEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssumeRoleForAllocatedEnv(self, request):
        r"""白名单接口，申请Tcb角色临时凭证

        :param request: Request instance for AssumeRoleForAllocatedEnv.
        :type request: :class:`tencentcloud.tcb.v20180608.models.AssumeRoleForAllocatedEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.AssumeRoleForAllocatedEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssumeRoleForAllocatedEnv", params, headers=headers)
            response = json.loads(body)
            model = models.AssumeRoleForAllocatedEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindStorageSource(self, request):
        r"""为云存储绑定外部云存储源。
        将一个用户自有的 COS桶 作为外部存储源绑定到指定云开发环境的云存储。绑定后，该环境的云存储文件操作将指向此桶，通过 BasePath 路径前缀实现与其他环境的数据隔离。
        每个环境仅允许绑定 1 个外部云存储源。

        :param request: Request instance for BindStorageSource.
        :type request: :class:`tencentcloud.tcb.v20180608.models.BindStorageSourceRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.BindStorageSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindStorageSource", params, headers=headers)
            response = json.loads(body)
            model = models.BindStorageSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckTcbService(self, request):
        r"""检查是否开通Tcb服务

        :param request: Request instance for CheckTcbService.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CheckTcbServiceRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CheckTcbServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckTcbService", params, headers=headers)
            response = json.loads(body)
            model = models.CheckTcbServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAIModel(self, request):
        r"""创建 AI 模型配置分组。云开发标准版及以上套餐才可使用

        支持自定义类型（custom）：用户自行提供模型服务地址（baseUrl）和访问密钥，分组名可自由命名，适用于接入第三方或自建模型服务。

        注意：内置类型（builtin）分组由云开发平台统一创建和管理，不支持通过此接口创建。如需修改内置分组的模型列表或启用状态，请使用 [UpdateAIModel](https://cloud.tencent.com/document/product/876/131316) 接口。

        创建成功后，可通过 [DescribeAIModels](https://cloud.tencent.com/document/product/876/131318) 接口查询分组信息，并在云开发 AI+ 功能中使用所配置的模型。

        :param request: Request instance for CreateAIModel.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateAIModelRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateAIModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAIModel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAIModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApiKey(self, request):
        r"""创建云开发平台的API Key。在指定云开发环境下创建一个 API Key 访问凭证。支持两种类型：api_key（服务端管理员访问凭证，以管理员身份签发，可设置有效期，不设置有效期则永不过期，单个环境最多创建 5 个）和 publish_key（前端匿名访问凭证，固定有效期，每个环境仅保留一个）。创建成功后将返回 API Key 明文 Token，该值仅在创建时返回一次，请妥善保存。需要管理员权限。
        权限范围与注意事项：
         - api_key 是以"管理员身份"签发的访问凭证，持有该 Token 即拥有腾讯云云开发数据流（含数据库、云函数、云存储、托管等）资源的完整访问与操作权限。该凭证不区分子资源粒度，一旦泄露等同于环境管理员权限被泄露，请按"高敏感凭证"管理： 仅用于服务端调用、严禁下发到前端/客户端、严禁写入代码仓库或日志、定期轮换并回收闲置凭证。
         - 在为子账号 / 协作者 / RAM 子用户授权该接口权限时，须先评估该子账号是否有资格获得该环境的管理员级数据流权限，能创建 api_key ≈ 能拥有环境管理员权限。

        :param request: Request instance for CreateApiKey.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateApiKeyRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAuthDomain(self, request):
        r"""增加安全域名。
        云开发会校验网页应用请求的来源域名，您需要将来源域名加入到WEB安全域名列表中。
        可以通过接口 [DescribeAuthDomains](https://cloud.tencent.com/document/product/876/42151) 获取当前已绑定生效的安全域名。

        注意⚠️
          安全域名绑定成功之后，需要几分钟时间逐步生效。

        :param request: Request instance for CreateAuthDomain.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateAuthDomainRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateAuthDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAuthDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAuthDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBillDeal(self, request):
        r"""创建云开发产品计费订单，用于以下几种场景：
        1. 购买云开发环境
        2. 续费云开发环境
        3. 变更云开发环境套餐
        4. 购买云开发资源包
        5. 购买云开发大促包

        该接口支持下单并支付(CreateAndPay=true时)，此时会自动在腾讯云账户中扣除余额（余额不足会下单失败）。
        该接口支持自动扣除代金券（AutoVoucher=true时），符合条件的代金券会被自动扣除。

        :param request: Request instance for CreateBillDeal.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateBillDealRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateBillDealResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBillDeal", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBillDealResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomLoginKey(self, request):
        r"""创建自定义登录密钥。在指定云开发环境下生成一对 RSA 1024 位非对称密钥对，系统仅存储公钥，私钥仅在创建时返回一次且不可恢复，请妥善保存。创建新密钥后，该环境下原有未设置过期时间的旧密钥将被自动标记为 2 小时后过期，请确保客户端及时更新密钥配置。
        返回的 KeyID 和 PrivateKey 需与环境 ID 一起组装为 JSON 配置文件，供客户端 Admin SDK 初始化时使用，文件格式如下：
        {
          "private_key_id": "<返回的 KeyID>",
          "private_key": "<返回的 PrivateKey>",
          "env_id": "<请求时传入的 EnvId>"
        }

        :param request: Request instance for CreateCustomLoginKey.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateCustomLoginKeyRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateCustomLoginKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomLoginKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomLoginKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEnv(self, request):
        r"""本接口用于购买云开发环境。
        该接口会自动下单并支付，会在腾讯云账户中扣除余额（余额不足会下单失败）。
        该接口支持自动扣除代金券（AutoVoucher=true时），符合条件的代金券会被自动扣除。
        环境下单成功之后会返回EnvId。EnvId是全局唯一表示。
        环境发货是异步行为，后续可以通过接口 [DescribeEnvs ](https://cloud.tencent.com/document/product/876/34820) 查询环境状态和各项资源信息；通过 [DescribeBillingInfo](https://cloud.tencent.com/document/product/876/94390) 查询环境套餐信息，包括 到期时间、当前套餐等。

        :param request: Request instance for CreateEnv.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEnv", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEnvResource(self, request):
        r"""**创建环境日志资源**

        环境开通后，若用户需要开启检索日志功能，需调用此接口进行日志资源的开通。

        > **注意**：日志资源的开通为**异步操作**，接口调用成功后并不代表日志资源已立即可用。

        **如何确认日志开通状态：**

        可通过 [DescribeEnvs](https://cloud.tencent.com/document/product/876/34820) 接口轮询查询日志开通结果，建议每 5 秒轮询一次，最长等待 5 分钟。在返回的数据结构 [EnvInfo](https://cloud.tencent.com/document/api/876/34822#EnvInfo) 中，检查 `LogServices` 字段下 `LogServiceInfo` 是否包含有效的日志主题（Topic）等相关信息，以此判断日志资源是否已成功开通：

        - **已开通**：`LogServiceInfo` 中存在日志主题 ID 等有效信息
        - **未开通 / 开通中**：`LogServiceInfo` 为空或相关字段缺失

        :param request: Request instance for CreateEnvResource.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateEnvResourceRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateEnvResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEnvResource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEnvResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHTTPServiceRoute(self, request):
        r"""本接口CreateHTTPServiceRoute用于创建HTTP访问服务路由。如果不传Domain.Routes，仅创建域名信息。首次创建域名后需要调用DescribeHTTPServiceRoute查询域名状态，如果状态是PROCESSING，需要轮询查询域名状态直到SUCCESS或者FAIL。如果状态是FAIL，可以删除后重新创建。创建成功后域名可能无法访问，原因是异步下发的路由，可通过http或者https探测路由是否下发，如果http访问返回404或者https访问握手失败，可等待一会再试，直到访问正常。此外HTTP访问服务提供了默认域名，通过DescribeHTTPServiceRoute接口可直接获取默认域名。

        :param request: Request instance for CreateHTTPServiceRoute.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateHTTPServiceRouteRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateHTTPServiceRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHTTPServiceRoute", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHTTPServiceRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHostingDomain(self, request):
        r"""创建托管域名

        :param request: Request instance for CreateHostingDomain.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateHostingDomainRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateHostingDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHostingDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHostingDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMySQL(self, request):
        r"""本接口（CreateMySQL）用于开通Mysql型数据库。

        开通后，可通过 [DescribeCreateMySQLResult ](https://cloud.tencent.com/document/api/876/128185) 查询开通结果，Mysql开通成功后，可通过接口设置数据库账号相关功能包括但不限于【创建账号、删除账号、查询可授权权限列表、查询账号已有权限、修改主机、修改配置、修改账号库表权限】、集群操作相关【查询集群参数、修改集群参数】，连接设置相关【关闭外网、开通外网、查询集群信息】，备份回档相关【创建手动回档、删除手动回档、修改自动备份配置信息、查询备份文件列表、集群回档、查询任务列表、获取table列表、获取集群数据库列表、查询备份下载地址】，相关功能接口文档：[TDSQL-C MySQL API文档](https://cloud.tencent.com/document/product/1003/48106)，可以通过 [RunSql](https://cloud.tencent.com/document/api/876/127880) 接口来执行 sql 命令，比如创建表格、插入数据、删除表格等 sql 命令。

        :param request: Request instance for CreateMySQL.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateMySQLRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateMySQLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMySQL", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMySQLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStaticStore(self, request):
        r"""创建静态托管资源，包括COS和CDN，异步任务创建，查看创建结果需要根据DescribeStaticStore接口来查看

        :param request: Request instance for CreateStaticStore.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateStaticStoreRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateStaticStoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStaticStore", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStaticStoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTable(self, request):
        r"""本接口(CreateTable)用于创建文档型数据库表，支持创建capped类型集合，暂时不支持分片表。

        :param request: Request instance for CreateTable.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateTableRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUser(self, request):
        r"""创建tcb用户

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVmInstance(self, request):
        r"""创建虚拟服务器
        创建流程为先调用[DescribeVmSpec](https://cloud.tencent.com/document/product/876/129360)获取可购买的规格，同时调用[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)拉取镜像列表，选中一个规格和一个镜像后，调用[InquireVmPrice](https://cloud.tencent.com/document/product/876/129759)询价，如果价格可接受，调用此接口创建实例

        :param request: Request instance for CreateVmInstance.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateVmInstanceRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateVmInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVmInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVmInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAIModel(self, request):
        r"""删除 AI 模型配置分组，支持批量删除。内置分组无法删除。分组删除后，该分组下的所有模型配置将同步移除，针对该分组模型的请求将会失败，请在删除前确认业务侧已停止对该分组的调用。

        注意：
        此操作不可逆，删除后数据无法恢复，请谨慎操作。

        删除前建议通过 [DescribeAIModelList]() 接口确认分组当前状态。

        :param request: Request instance for DeleteAIModel.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteAIModelRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteAIModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAIModel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAIModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApiKey(self, request):
        r"""删除指定云开发环境下的某个 API Key 服务端访问凭证。删除后，该 API Key 对应的 Token 将被吊销，已使用该 Key 发起的请求将失败。该操作具有幂等性，若指定的 API Key 不存在则直接返回成功。需要管理员权限。

        :param request: Request instance for DeleteApiKey.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteApiKeyRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAuthDomain(self, request):
        r"""删除合法域名。
        云开发会校验网页应用请求的来源域名，您需要将来源域名加入到WEB安全域名列表中。
        可以通过接口 [DescribeAuthDomains](https://cloud.tencent.com/document/product/876/42151) 获取当前已绑定生效的安全域名，将对应安全域名的id填入Domainlds中

        注意⚠️
        安全域名被删除之后，可能会引起跨域问题，请谨慎操作。

        :param request: Request instance for DeleteAuthDomain.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteAuthDomainRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteAuthDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAuthDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuthDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteHTTPServiceRoute(self, request):
        r"""本接口DeleteHTTPServiceRoute用于删除HTTP访问服务域名或者路由。可批量删除多条path路由、删除域名及所有path路由，如果Paths字段为空则删除域名及所有path路由，如果Paths不为空则仅删除path路由。

        :param request: Request instance for DeleteHTTPServiceRoute.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteHTTPServiceRouteRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteHTTPServiceRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteHTTPServiceRoute", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteHTTPServiceRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProvider(self, request):
        r"""删除认证源

        :param request: Request instance for DeleteProvider.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteProviderRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteProviderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProvider", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProviderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTable(self, request):
        r"""本接口(DeleteTable)用于删除文档型数据库表，删除表后表中数据将会被删除且无法恢复，请谨慎操作。

        接口入参中的 Tag 为文档型数据库的实例 Id，可以通过 [DescribeEnvs](https://cloud.tencent.com/document/api/876/34820) 接口返回的 EnvList[0].Databases[0].InstanceId 获取。

        :param request: Request instance for DeleteTable.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteTableRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTable", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUsers(self, request):
        r"""删除tcb用户

        :param request: Request instance for DeleteUsers.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteUsersRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVmInstance(self, request):
        r"""销毁云服务器实例

        :param request: Request instance for DeleteVmInstance.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteVmInstanceRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteVmInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVmInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVmInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIModels(self, request):
        r"""查询指定云开发环境下已配置的 AI 模型分组列表。返回结果包含该环境下所有类型的模型分组（自定义类型 custom、内置类型 builtin），以及各分组下的模型列表、服务地址、启用状态等配置信息。

        通常在以下场景中使用：

        控制台展示：在云开发控制台 AI+ 功能 → 模型管理页面，展示当前环境已配置的模型分组列表。

        模型管理：在调用 [UpdateAIModel]() 或 [DeleteAIModel]() 接口前，通过本接口查询当前分组配置。

        业务集成：开发者查询可用模型列表，用于选择合适的模型接入 AI+ 功能。

        :param request: Request instance for DescribeAIModels.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeAIModelsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeAIModelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIModels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIModelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiKeyList(self, request):
        r"""查询 API Key 列表。分页查询指定云开发环境下的 API Key 访问凭证列表。支持按类型过滤（api_key 或 publish_key）。未指定类型时，默认仅返回 api_key 类型的记录。列表查询中 api_key 类型的令牌值将进行脱敏处理（仅保留前后各 6 位字符）；publish_key 类型始终返回完整明文。接口需要管理员权限。

        :param request: Request instance for DescribeApiKeyList.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeApiKeyListRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeApiKeyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiKeyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiKeyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuthDomains(self, request):
        r"""本接口用于获取当前环境的安全域名列表。
        云开发会校验网页应用请求的来源域名，您需要将来源域名加入到WEB安全域名列表中。
        可以通过接口 [CreateAuthDomain](https://cloud.tencent.com/document/product/876/42764) 增加安全域名。

        :param request: Request instance for DescribeAuthDomains.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeAuthDomainsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeAuthDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuthDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuthDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaasPackageList(self, request):
        r"""获取新套餐列表，含详情，如果传了PackageId，则只获取指定套餐详情

        :param request: Request instance for DescribeBaasPackageList.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeBaasPackageListRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeBaasPackageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaasPackageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaasPackageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillingInfo(self, request):
        r"""获取云开发环境的计费相关信息。
        包括环境的 状态、当前套餐、购买时间、到期时间 等。

        :param request: Request instance for DescribeBillingInfo.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeBillingInfoRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeBillingInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillingInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillingInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClient(self, request):
        r"""查询客户端详情。获取指定云开发环境下某个客户端的配置信息，包括客户端基本信息（名称、图标、描述）、OAuth 凭证（ClientId、ClientSecret）、安全域名、允许的 Scope 列表、Token 有效期、会话控制策略等。当客户端 ID 等于环境 ID 时，返回该环境的默认客户端配置。

        :param request: Request instance for DescribeClient.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeClientRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeClientResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClient", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClientResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudAppList(self, request):
        r"""查询云应用服务列表信息

        :param request: Request instance for DescribeCloudAppList.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudAppListRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudAppListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudAppList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudAppListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudBaseBuildService(self, request):
        r"""获取云托管代码上传url

        :param request: Request instance for DescribeCloudBaseBuildService.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseBuildServiceRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseBuildServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseBuildService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseBuildServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudBaseRunServerVersion(self, request):
        r"""查询服务版本的详情，CPU和MEM  请使用CPUSize和MemSize

        :param request: Request instance for DescribeCloudBaseRunServerVersion.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunServerVersionRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunServerVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseRunServerVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseRunServerVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCreateMySQLResult(self, request):
        r"""本接口（DescribeCreateMySQLResult）用于查询开通Mysql结果。

        `Response.Data.Status = "notexist"` 表示未开通，如果未开通，可以调用 [CreateMySQL](https://cloud.tencent.com/document/api/876/128186) 来开通
         `Response.Data. Status = "success"` 表示开通成功，Mysql开通成功后，可通过接口设置数据库账号相关功能包括但不限于【创建账号、删除账号、查询可授权权限列表、查询账号已有权限、修改主机、修改配置、修改账号库表权限】、集群操作相关【查询集群参数、修改集群参数】，连接设置相关【关闭外网、开通外网、查询集群信息】，备份回档相关【创建手动回档、删除手动回档、修改自动备份配置信息、查询备份文件列表、集群回档、查询任务列表、获取table列表、获取集群数据库列表、查询备份下载地址】，相关功能接口文档：[TDSQL-C MySQL API文档](https://cloud.tencent.com/document/product/1003/48106)，可以通过 [RunSql](https://cloud.tencent.com/document/api/876/127880) 接口来执行 sql 命令，比如创建表格、插入数据、删除表格等 MySql 命令。

        :param request: Request instance for DescribeCreateMySQLResult.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCreateMySQLResultRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCreateMySQLResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCreateMySQLResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCreateMySQLResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCreditsUsage(self, request):
        r"""查询资源点模式下的资源点用量

        :param request: Request instance for DescribeCreditsUsage.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCreditsUsageRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCreditsUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCreditsUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCreditsUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCreditsUsageDetail(self, request):
        r"""查询资源点模式下的资源点用量及原始用量明细

        :param request: Request instance for DescribeCreditsUsageDetail.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCreditsUsageDetailRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCreditsUsageDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCreditsUsageDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCreditsUsageDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCurveData(self, request):
        r"""根据指定指标名称，查询某环境在指定时间范围内的监控数据，返回按统计粒度聚合后的时序数据。

        :param request: Request instance for DescribeCurveData.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCurveDataRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCurveDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCurveData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCurveDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseACL(self, request):
        r"""本接口（DescribeDatabaseACL）获取文档型数据库权限。

        :param request: Request instance for DescribeDatabaseACL.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeDatabaseACLRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeDatabaseACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseACL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvAccountCircle(self, request):
        r"""查询环境计费周期。
        云开发环境的资源点都是按月结算的，每个月都有一定的抵扣额度。

        例如：
          某个环境在 2026-01-05 购买了3个月个人版(到期时间: 2026-04-05)，则他可以在以下3个周期内，分别享有40000资源点的额度：
          1. 2026-01-05 ~ 2026-02-05 23:59:59
          2. 2026-02-06 ~ 2026-03-05 23:59:59
          3. 2026-03-06 ~ 2026-04-05 23:59:59

        本接口，用于获取环境当前属于哪个计费周期内。

        :param request: Request instance for DescribeEnvAccountCircle.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvAccountCircleRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvAccountCircleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvAccountCircle", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvAccountCircleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvLimit(self, request):
        r"""查询环境个数上限

        :param request: Request instance for DescribeEnvLimit.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvLimitRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvPlans(self, request):
        r"""获取可售卖的新套餐列表，含详情，如果传了PackageId，则只获取指定套餐详情

        :param request: Request instance for DescribeEnvPlans.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvPlansRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvPlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvPlans", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvPlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvs(self, request):
        r"""获取环境列表，含环境下的各个资源信息。尤其是各资源的唯一标识，是请求各资源的关键参数

        :param request: Request instance for DescribeEnvs.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewayVersions(self, request):
        r"""查询网关版本信息
        暂不鉴权

        :param request: Request instance for DescribeGatewayVersions.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeGatewayVersionsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeGatewayVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHTTPServiceRoute(self, request):
        r"""本接口DescribeHTTPServiceRoute用于查询环境下HTTP访问服务路由信息。可通过Filters过滤。如果不存在不会返回错误。HTTP访问服务提供了默认域名，通过本接口可直接获取默认域名。

        :param request: Request instance for DescribeHTTPServiceRoute.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeHTTPServiceRouteRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeHTTPServiceRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHTTPServiceRoute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHTTPServiceRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostingDomainTask(self, request):
        r"""查询静态托管域名任务状态

        :param request: Request instance for DescribeHostingDomainTask.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeHostingDomainTaskRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeHostingDomainTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostingDomainTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostingDomainTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoginConfig(self, request):
        r"""查询指定云开发环境的登录策略配置。包括手机号短信登录、邮箱登录、用户名密码登录和匿名登录方式的开启状态，同时包含短信验证码发送通道、MFA 多因子认证和密码的更新策略。

        :param request: Request instance for DescribeLoginConfig.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeLoginConfigRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeLoginConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeManagedAIModelList(self, request):
        r"""查询云开发平台支持的托管类型 AI 模型列表。

        托管类型模型由云开发平台统一接入和管理，用户无需自行配置模型服务地址和访问密钥，开通后即可直接使用。返回结果按模型分组（Group）组织，包含各模型的规格参数（ModelSpec）和计费信息（ModelChargingInfo）。

        通常在以下场景中使用：

        开通托管模型前：通过本接口查询平台支持的托管模型及其规格，结合 [UpdateAIModel](https://cloud.tencent.com/document/product/876/131316) 接口完成模型配置。

        :param request: Request instance for DescribeManagedAIModelList.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeManagedAIModelListRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeManagedAIModelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeManagedAIModelList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeManagedAIModelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMySQLClusterDetail(self, request):
        r"""本接口（DescribeMySQLClusterDetail）查询Mysql集群信息。

        调用该接口前需要先查询Mysql是否开通，可通过 [DescribeCreateMySQLResult ](https://cloud.tencent.com/document/api/876/128185) 查询，只有已开通的才能查到集群信息，Mysql开通成功后，可通过接口设置数据库账号相关功能包括但不限于【创建账号、删除账号、查询可授权权限列表、查询账号已有权限、修改主机、修改配置、修改账号库表权限】、集群操作相关【查询集群参数、修改集群参数】，连接设置相关【关闭外网、开通外网、查询集群信息】，备份回档相关【创建手动回档、删除手动回档、修改自动备份配置信息、查询备份文件列表、集群回档、查询任务列表、获取table列表、获取集群数据库列表、查询备份下载地址】，相关功能接口文档：[TDSQL-C MySQL API文档](https://cloud.tencent.com/document/product/1003/48106)，可以通过 [RunSql](https://cloud.tencent.com/document/api/876/127880) 接口来执行 MySql 命令，比如创建表格、插入数据、删除表格等 MySql 命令。

        :param request: Request instance for DescribeMySQLClusterDetail.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeMySQLClusterDetailRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeMySQLClusterDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMySQLClusterDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMySQLClusterDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMySQLTaskStatus(self, request):
        r"""本接口（DescribeMySQLTaskStatus）用于查询Mysql任务状态。

        :param request: Request instance for DescribeMySQLTaskStatus.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeMySQLTaskStatusRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeMySQLTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMySQLTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMySQLTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePGUserMigration(self, request):
        r"""本接口（DescribePGUserMigration）用于查询目标环境指定 migration 详情。

        :param request: Request instance for DescribePGUserMigration.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribePGUserMigrationRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribePGUserMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePGUserMigration", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePGUserMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQuotaData(self, request):
        r"""查询指定指标的配额使用量

        :param request: Request instance for DescribeQuotaData.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeQuotaDataRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeQuotaDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQuotaData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQuotaDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourcePermission(self, request):
        r"""查询资源基础权限。

        查询云函数、云存储和数据库表的基础权限配置。支持单个资源查询和批量查询。

        :param request: Request instance for DescribeResourcePermission.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeResourcePermissionRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeResourcePermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourcePermission", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourcePermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSafeRule(self, request):
        r"""查询数据库安全规则。
        安全规则，用于控制C端用户的访问权限。详见 [安全规则介绍](https://cloud.tencent.com/document/product/876/123478) 。

        :param request: Request instance for DescribeSafeRule.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeSafeRuleRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeSafeRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSafeRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSafeRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStaticStore(self, request):
        r"""查看当前环境下静态托管资源信息，根据返回结果判断静态资源的状态

        :param request: Request instance for DescribeStaticStore.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeStaticStoreRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeStaticStoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStaticStore", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStaticStoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTable(self, request):
        r"""本接口（DescribeTable）用于查询文档型数据库表的相关信息，包括索引等信息。

        接口入参中的 Tag 为文档型数据库的实例 Id，可以通过 [DescribeEnvs](https://cloud.tencent.com/document/api/876/34820) 接口返回的 EnvList[0].Databases[0].InstanceId 获取。

        :param request: Request instance for DescribeTable.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeTableRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTables(self, request):
        r"""本接口(DescribeTables)用于查询文档型数据库所有表信息，包括表名、表中数据条数、表中数据量、索引个数及索引的大小等。

        :param request: Request instance for DescribeTables.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeTablesRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserList(self, request):
        r"""查询tcb用户列表

        :param request: Request instance for DescribeUserList.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeUserListRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVmInstances(self, request):
        r"""查询环境下的云服务器列表

        :param request: Request instance for DescribeVmInstances.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeVmInstancesRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeVmInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVmInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVmInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVmSpec(self, request):
        r"""云服务器规格list

        :param request: Request instance for DescribeVmSpec.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeVmSpecRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeVmSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVmSpec", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVmSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyEnv(self, request):
        r"""本接口用于销毁云开发环境。
        云开发环境遵循腾讯云包年包月预付费产品生命周期，因此环境销毁需要分两步：
        1. 资源退费。此时会根据当前环境剩余有效期，自动退还相关费用(代金券不退)。退款后，环境进入隔离期。
        2. 环境删除。环境在进入隔离期后15天会自动删除。也可以通过本接口，指定 IsForce=true 来强制删除隔离期环境。

        **注意**⚠️
          1. 环境退费后进入隔离期，则所有资源均无法访问，控制台无法操作和管理。
          2. 环境被彻底删除后，所有数据均无法找回。请谨慎操作。

        可以通过接口 [tcb:DescribeBillingInfo](https://cloud.tencent.com/document/product/876/94390) 查询环境计费状态。

        :param request: Request instance for DestroyEnv.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DestroyEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DestroyEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyEnv", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyMySQL(self, request):
        r"""本接口（DestroyMySQL）用于销毁Mysql。

        销毁后可以通过 [DescribeMySQLTaskStatus](https://cloud.tencent.com/document/api/876/128183) 接口查询销毁结果，如果 `Response.Data. Status = FAILED ` 表示销毁失败，可以重新调用销毁接口重试。

        :param request: Request instance for DestroyMySQL.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DestroyMySQLRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DestroyMySQLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyMySQL", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyMySQLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyStaticStore(self, request):
        r"""销毁静态托管资源，该接口创建异步销毁任务，资源最终状态可从DestroyStaticStore接口查看

        :param request: Request instance for DestroyStaticStore.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DestroyStaticStoreRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DestroyStaticStoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyStaticStore", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyStaticStoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExecutePGSql(self, request):
        r"""在Postgres数据库上执行SQL

        :param request: Request instance for ExecutePGSql.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ExecutePGSqlRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ExecutePGSqlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExecutePGSql", params, headers=headers)
            response = json.loads(body)
            model = models.ExecutePGSqlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetProviders(self, request):
        r"""查询指定云开发环境下的身份认证源列表。返回该环境已配置的所有身份认证源信息，包括第三方登录（OAuth、OIDC、SAML）、微信小程序登录、自定义登录和邮箱登录等。返回结果包含认证源基本信息、关联应用、配置状态及启用情况。若自定义登录或邮箱登录的身份源尚未创建，接口会自动追加一个默认关闭状态的身份源记录。

        :param request: Request instance for GetProviders.
        :type request: :class:`tencentcloud.tcb.v20180608.models.GetProvidersRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.GetProvidersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetProviders", params, headers=headers)
            response = json.loads(body)
            model = models.GetProvidersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquireVmPrice(self, request):
        r"""查询服务器价格

        :param request: Request instance for InquireVmPrice.
        :type request: :class:`tencentcloud.tcb.v20180608.models.InquireVmPriceRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.InquireVmPriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquireVmPrice", params, headers=headers)
            response = json.loads(body)
            model = models.InquireVmPriceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListPGUserMigrations(self, request):
        r"""本接口（ListPGUserMigrations）用于查询目标环境已应用的用户 migration 列表。

        :param request: Request instance for ListPGUserMigrations.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ListPGUserMigrationsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ListPGUserMigrationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListPGUserMigrations", params, headers=headers)
            response = json.loads(body)
            model = models.ListPGUserMigrationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTables(self, request):
        r"""本接口(ListTables)用于查询文档型数据库所有表信息，包括表名、表中数据条数、表中数据量、索引个数及索引的大小等。

        该接口跟 [DescribeTables](https://cloud.tencent.com/document/api/876/127962) 接口功能一致，后续该接口可能会下线，请使用 [DescribeTable](https://cloud.tencent.com/document/api/876/127962)接口。

        :param request: Request instance for ListTables.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ListTablesRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ListTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTables", params, headers=headers)
            response = json.loads(body)
            model = models.ListTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClient(self, request):
        r"""修改客户端配置。采用增量更新策略，仅更新请求中传入的非空字段，未传入的字段保持原值不变。支持修改客户端基本信息（名称、图标、描述、主页地址）、安全域名、允许的 Scope 列表、Token 有效期、会话控制策略及启用状态等配置。
        Id、Secret、CreatedAt、Meta 等字段在该接口中不可修改，当客户端 ID 等于环境 ID 且客户端尚未创建时，将自动创建默认客户端配置。

        :param request: Request instance for ModifyClient.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyClientRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyClientResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClient", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClientResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClsTopic(self, request):
        r"""修改日志主题

        :param request: Request instance for ModifyClsTopic.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyClsTopicRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyClsTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClsTopic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClsTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatabaseACL(self, request):
        r"""本接口（ModifyDatabaseACL）用于修改文档型数据库权限。

        :param request: Request instance for ModifyDatabaseACL.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyDatabaseACLRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyDatabaseACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatabaseACL", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatabaseACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEnv(self, request):
        r"""更新环境信息

        :param request: Request instance for ModifyEnv.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEnv", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEnvPlan(self, request):
        r"""本接口用于变更云开发环境套餐。
        该接口会自动下单并支付，会在腾讯云账户中扣除余额（余额不足会下单失败）。
        该接口支持自动扣除代金券（AutoVoucher=true时），符合条件的代金券会被自动扣除。

        :param request: Request instance for ModifyEnvPlan.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyEnvPlanRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyEnvPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEnvPlan", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEnvPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHTTPServiceRoute(self, request):
        r"""本接口ModifyHTTPServiceRoute用于修改HTTP访问服务路由。支持增量修改，对应字段不传参数则不修改

        :param request: Request instance for ModifyHTTPServiceRoute.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyHTTPServiceRouteRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyHTTPServiceRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHTTPServiceRoute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHTTPServiceRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoginConfig(self, request):
        r"""修改指定云开发环境的登录策略配置。支持开启或关闭手机号短信登录、邮箱登录、用户名密码登录和匿名登录，同时可配置短信验证码发送通道、MFA 多因子认证和密码更新策略。
        修改后立即生效，影响该环境下所有终端用户的登录行为。

        :param request: Request instance for ModifyLoginConfig.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyLoginConfigRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyLoginConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoginConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoginConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProvider(self, request):
        r"""修改身份认证源。更新指定云开发环境下已有身份认证源的配置信息，支持修改基本信息（名称、图标、描述）、协议连接配置（ClientId、ClientSecret、端点地址等）、登录行为控制（透传模式、自动注册、邮箱/手机号自动关联）以及启用状态。
        对于 OIDC 类型身份源，修改 Issuer 后将自动通过 OpenID Connect Discovery 重新获取端点配置。
        若自定义登录（CUSTOM）或邮箱登录（EMAIL）身份源尚不存在，调用该接口时将自动创建。

        :param request: Request instance for ModifyProvider.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyProviderRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyProviderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProvider", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProviderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourcePermission(self, request):
        r"""修改资源基础权限。

        修改云函数、云存储和数据库表的基础权限配置。支持预定义权限级别和自定义安全规则两种方式配置资源访问权限。

        :param request: Request instance for ModifyResourcePermission.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyResourcePermissionRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyResourcePermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourcePermission", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourcePermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySafeRule(self, request):
        r"""设置数据库安全规则。
        安全规则，用于控制C端用户的访问权限。详见 [安全规则介绍 ](https://cloud.tencent.com/document/product/876/123478)。

        :param request: Request instance for ModifySafeRule.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifySafeRuleRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifySafeRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySafeRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySafeRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStorageSource(self, request):
        r"""修改指定云开发环境已绑定的外部云存储源配置。
        修改之后，大约3~5分钟生效。

        注意⚠️
        本接口仅更新存储源绑定关系，不会迁移您的数据。

        :param request: Request instance for ModifyStorageSource.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyStorageSourceRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyStorageSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStorageSource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStorageSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUser(self, request):
        r"""修改tcb用户

        :param request: Request instance for ModifyUser.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyUserRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUser", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PreviewPGUserMigrations(self, request):
        r"""本接口（PreviewPGUserMigrations）用于预览SQL migrations 在远端的执行计划，不实际执行SQL。

        :param request: Request instance for PreviewPGUserMigrations.
        :type request: :class:`tencentcloud.tcb.v20180608.models.PreviewPGUserMigrationsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.PreviewPGUserMigrationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PreviewPGUserMigrations", params, headers=headers)
            response = json.loads(body)
            model = models.PreviewPGUserMigrationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PushPGUserMigrations(self, request):
        r"""本接口（PushPGUserMigrations）用于批量应用Migrations。

        :param request: Request instance for PushPGUserMigrations.
        :type request: :class:`tencentcloud.tcb.v20180608.models.PushPGUserMigrationsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.PushPGUserMigrationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PushPGUserMigrations", params, headers=headers)
            response = json.loads(body)
            model = models.PushPGUserMigrationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseEnv(self, request):
        r"""从环境池里立即取出1个环境

        :param request: Request instance for ReleaseEnv.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ReleaseEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ReleaseEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseEnv", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewEnv(self, request):
        r"""本接口用于云开发环境套餐续费。
        该接口会自动下单并支付，会在腾讯云账户中扣除余额（余额不足会下单失败）。
        该接口支持自动扣除代金券（AutoVoucher=true时），符合条件的代金券会被自动扣除。

        :param request: Request instance for RenewEnv.
        :type request: :class:`tencentcloud.tcb.v20180608.models.RenewEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.RenewEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewEnv", params, headers=headers)
            response = json.loads(body)
            model = models.RenewEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RepairPGUserMigrationHistory(self, request):
        r"""本接口（RepairPGUserMigrationHistory）用于受控修复 history，只修改 user_schema_migrations，不执行 SQL。

        :param request: Request instance for RepairPGUserMigrationHistory.
        :type request: :class:`tencentcloud.tcb.v20180608.models.RepairPGUserMigrationHistoryRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.RepairPGUserMigrationHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RepairPGUserMigrationHistory", params, headers=headers)
            response = json.loads(body)
            model = models.RepairPGUserMigrationHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackPGUserMigrations(self, request):
        r"""本接口（RollbackPGUserMigrations）用于按最近 N 条已应用 migration 倒序执行 rollback。

        :param request: Request instance for RollbackPGUserMigrations.
        :type request: :class:`tencentcloud.tcb.v20180608.models.RollbackPGUserMigrationsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.RollbackPGUserMigrationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackPGUserMigrations", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackPGUserMigrationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunCommands(self, request):
        r"""本接口（RunCommands）用于执行文档型数据库命令。

        :param request: Request instance for RunCommands.
        :type request: :class:`tencentcloud.tcb.v20180608.models.RunCommandsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.RunCommandsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunCommands", params, headers=headers)
            response = json.loads(body)
            model = models.RunCommandsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunSql(self, request):
        r"""本接口（RunSql）用于执行MySQL语句。

        该接口用来执行 MySql 语句，比如创建表格、插入数据、修改数据、删除字段、添加索引等可以通过sql 语句实现的都可以使用该接口。

        调用该接口前需要先查询Mysql是否开通，可通过 [DescribeCreateMySQLResult ](https://cloud.tencent.com/document/api/876/128185) 查询，只有开通成功才能操作。

        :param request: Request instance for RunSql.
        :type request: :class:`tencentcloud.tcb.v20180608.models.RunSqlRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.RunSqlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunSql", params, headers=headers)
            response = json.loads(body)
            model = models.RunSqlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchClsLog(self, request):
        r"""搜索用户调用日志

        :param request: Request instance for SearchClsLog.
        :type request: :class:`tencentcloud.tcb.v20180608.models.SearchClsLogRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.SearchClsLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchClsLog", params, headers=headers)
            response = json.loads(body)
            model = models.SearchClsLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindStorageSource(self, request):
        r"""从指定云开发环境中解绑已绑定的外部云存储源。解绑后，该环境将不再关联外部 存储源，云存储功能恢复为未绑定状态。
        解绑操作仅移除 CloudBase 侧的绑定关系，不会删除桶本身及桶内数据，桶仍由用户自行管理。

        注意⚠️
        解绑之后，会导致云存储不可用，请谨慎操作。

        :param request: Request instance for UnbindStorageSource.
        :type request: :class:`tencentcloud.tcb.v20180608.models.UnbindStorageSourceRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.UnbindStorageSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindStorageSource", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindStorageSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAIModel(self, request):
        r"""更新 AI 模型配置分组。支持修改分组的模型列表、服务地址、访问密钥、备注及启用状态。

        不同分组类型支持的更新操作如下：
        自定义类型（custom）：可更新模型服务地址（BaseUrl）、访问密钥（Secret）、模型列表及分组备注。
        内置类型（builtin）：默认由云开发平台统一管理服务地址和密钥。若同时传入自定义 BaseURL 和 Secret，该分组将自动转换为自定义类型（custom），后续使用用户自行提供的服务地址和访问密钥，平台不再托管其凭证。

        分组类型转换说明:
        调用本接口时，可通过传入 BaseURL 与 Secret 参数触发分组类型的自动转换，规则如下：
        (1) builtin → custom（内置转自定义）
        当分组当前类型（Type）为 builtin 时，若请求中同时传入有效的 BaseURL（非 http://default.tcb）和 Secret，系统将自动将该分组转换为自定义类型（Type = custom）。转换后，平台不再托管该分组的服务地址和访问密钥，后续将使用用户自行提供的 BaseUrl 与 Secret 对模型服务发起请求。

        (2) custom → builtin（自定义恢复内置托管）
        仅当分组的原始类型（OriginType）为 builtin 时，支持将分组恢复为内置托管类型。将 BaseUrl 传入固定值 http://default.tcb，且不传入 Secret，系统将自动将该分组转换回内置托管类型（Type = builtin），平台重新接管其服务地址和访问密钥。
        若 OriginType 为 CUSTOM（即用户通过 [CreateAIModel](https://cloud.tencent.com/document/product/876/131320) 接口自行创建的自定义分组），不支持恢复为内置托管类型。

        更新成功后，可通过 [DescribeAIModels](https://cloud.tencent.com/document/product/876/131318) 接口查询最新分组配置。

        :param request: Request instance for UpdateAIModel.
        :type request: :class:`tencentcloud.tcb.v20180608.models.UpdateAIModelRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.UpdateAIModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAIModel", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAIModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTable(self, request):
        r"""本接口(UpdateTable)用于修改文档型数据库表信息，当前可以支持创建和删除索引。

        :param request: Request instance for UpdateTable.
        :type request: :class:`tencentcloud.tcb.v20180608.models.UpdateTableRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.UpdateTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTable", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))