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
from tencentcloud.scf.v20180416 import models
from typing import Dict


class ScfClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'scf.tencentcloudapi.com'
    _service = 'scf'

    async def CopyFunction(
            self,
            request: models.CopyFunctionRequest,
            opts: Dict = None,
    ) -> models.CopyFunctionResponse:
        """
        复制一个函数，您可以选择将复制出的新函数放置在特定的Region和Namespace。
        注：本接口**不会**复制函数的以下对象或属性：
        1. 函数的触发器
        2. 除了$LATEST以外的其它版本
        3. 函数配置的日志投递到的CLS目标。

        如有需要，您可以在复制后手动配置新函数。
        """
        
        kwargs = {}
        kwargs["action"] = "CopyFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlias(
            self,
            request: models.CreateAliasRequest,
            opts: Dict = None,
    ) -> models.CreateAliasResponse:
        """
        为某个函数版本创建一个别名，您可以使用别名来标记特定的函数版本，如DEV/RELEASE版本，也可以随时修改别名指向的版本。
        一个别名必须指向一个主版本，此外还可以同时指向一个附加版本。调用函数时指定特定的别名，则请求会被发送到别名指向的版本上，您可以配置请求发送到主版本和附加版本的比例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomDomain(
            self,
            request: models.CreateCustomDomainRequest,
            opts: Dict = None,
    ) -> models.CreateCustomDomainResponse:
        """
        创建自定义域名
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFunction(
            self,
            request: models.CreateFunctionRequest,
            opts: Dict = None,
    ) -> models.CreateFunctionResponse:
        """
        该接口根据传入参数创建新的函数。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNamespace(
            self,
            request: models.CreateNamespaceRequest,
            opts: Dict = None,
    ) -> models.CreateNamespaceResponse:
        """
        该接口根据传入的参数创建命名空间。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTrigger(
            self,
            request: models.CreateTriggerRequest,
            opts: Dict = None,
    ) -> models.CreateTriggerResponse:
        """
        该接口根据参数输入设置新的触发方式。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlias(
            self,
            request: models.DeleteAliasRequest,
            opts: Dict = None,
    ) -> models.DeleteAliasResponse:
        """
        删除一个函数版本的别名
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCustomDomain(
            self,
            request: models.DeleteCustomDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteCustomDomainResponse:
        """
        删除自定义域名
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCustomDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCustomDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFunction(
            self,
            request: models.DeleteFunctionRequest,
            opts: Dict = None,
    ) -> models.DeleteFunctionResponse:
        """
        该接口根据传入参数删除函数。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFunctionVersion(
            self,
            request: models.DeleteFunctionVersionRequest,
            opts: Dict = None,
    ) -> models.DeleteFunctionVersionResponse:
        """
        该接口根据传入参数删除函数的指定版本。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFunctionVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFunctionVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLayerVersion(
            self,
            request: models.DeleteLayerVersionRequest,
            opts: Dict = None,
    ) -> models.DeleteLayerVersionResponse:
        """
        删除指定层的指定版本，被删除的版本无法再关联到函数上，但不会影响正在引用这个层的函数。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLayerVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLayerVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNamespace(
            self,
            request: models.DeleteNamespaceRequest,
            opts: Dict = None,
    ) -> models.DeleteNamespaceResponse:
        """
        该接口根据传入的参数删除命名空间。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProvisionedConcurrencyConfig(
            self,
            request: models.DeleteProvisionedConcurrencyConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteProvisionedConcurrencyConfigResponse:
        """
        删除函数版本的预置并发配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProvisionedConcurrencyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProvisionedConcurrencyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReservedConcurrencyConfig(
            self,
            request: models.DeleteReservedConcurrencyConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteReservedConcurrencyConfigResponse:
        """
        删除函数的最大独占配额配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReservedConcurrencyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReservedConcurrencyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTrigger(
            self,
            request: models.DeleteTriggerRequest,
            opts: Dict = None,
    ) -> models.DeleteTriggerResponse:
        """
        该接口根据参数传入删除已有的触发方式。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAccount(
            self,
            request: models.GetAccountRequest,
            opts: Dict = None,
    ) -> models.GetAccountResponse:
        """
        获取账户信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAlias(
            self,
            request: models.GetAliasRequest,
            opts: Dict = None,
    ) -> models.GetAliasResponse:
        """
        获取别名的详细信息，包括名称、描述、版本、路由信息等。
        """
        
        kwargs = {}
        kwargs["action"] = "GetAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAsyncEventStatus(
            self,
            request: models.GetAsyncEventStatusRequest,
            opts: Dict = None,
    ) -> models.GetAsyncEventStatusResponse:
        """
        获取函数异步执行事件状态，事件状态保留 3 * 24 小时（从事件完成开始计时）。
        """
        
        kwargs = {}
        kwargs["action"] = "GetAsyncEventStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAsyncEventStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCustomDomain(
            self,
            request: models.GetCustomDomainRequest,
            opts: Dict = None,
    ) -> models.GetCustomDomainResponse:
        """
        查看云函数自定义域名详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetCustomDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCustomDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFunction(
            self,
            request: models.GetFunctionRequest,
            opts: Dict = None,
    ) -> models.GetFunctionResponse:
        """
        该接口获取某个函数的详细信息，包括名称、代码、处理方法、关联触发器和超时时间等字段。
        """
        
        kwargs = {}
        kwargs["action"] = "GetFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFunctionAddress(
            self,
            request: models.GetFunctionAddressRequest,
            opts: Dict = None,
    ) -> models.GetFunctionAddressResponse:
        """
        该接口用于获取函数代码包的下载地址。
        """
        
        kwargs = {}
        kwargs["action"] = "GetFunctionAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFunctionAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFunctionEventInvokeConfig(
            self,
            request: models.GetFunctionEventInvokeConfigRequest,
            opts: Dict = None,
    ) -> models.GetFunctionEventInvokeConfigResponse:
        """
        获取函数异步重试配置，包括重试次数和消息保留时间
        """
        
        kwargs = {}
        kwargs["action"] = "GetFunctionEventInvokeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFunctionEventInvokeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFunctionLogs(
            self,
            request: models.GetFunctionLogsRequest,
            opts: Dict = None,
    ) -> models.GetFunctionLogsResponse:
        """
        该接口根据指定的日志查询条件返回函数运行日志。该接口已下线，查询函数请求运行的返回信息，请使用 [GetRequestStatus](https://cloud.tencent.com/document/product/583/65348)。查询函数运行日志，请参考[日志检索教程](https://cloud.tencent.com/document/product/583/52637)。
        """
        
        kwargs = {}
        kwargs["action"] = "GetFunctionLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFunctionLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLayerVersion(
            self,
            request: models.GetLayerVersionRequest,
            opts: Dict = None,
    ) -> models.GetLayerVersionResponse:
        """
        获取层版本详细信息，包括用于下载层中文件的链接。
        """
        
        kwargs = {}
        kwargs["action"] = "GetLayerVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLayerVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetProvisionedConcurrencyConfig(
            self,
            request: models.GetProvisionedConcurrencyConfigRequest,
            opts: Dict = None,
    ) -> models.GetProvisionedConcurrencyConfigResponse:
        """
        获取函数或函数某一版本的预置并发详情。
        """
        
        kwargs = {}
        kwargs["action"] = "GetProvisionedConcurrencyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetProvisionedConcurrencyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRequestStatus(
            self,
            request: models.GetRequestStatusRequest,
            opts: Dict = None,
    ) -> models.GetRequestStatusResponse:
        """
        该接口根据指定的查询条件返回函数单个请求运行状态。
        """
        
        kwargs = {}
        kwargs["action"] = "GetRequestStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRequestStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetReservedConcurrencyConfig(
            self,
            request: models.GetReservedConcurrencyConfigRequest,
            opts: Dict = None,
    ) -> models.GetReservedConcurrencyConfigResponse:
        """
        获取函数的最大独占配额详情。
        """
        
        kwargs = {}
        kwargs["action"] = "GetReservedConcurrencyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetReservedConcurrencyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def Invoke(
            self,
            request: models.InvokeRequest,
            opts: Dict = None,
    ) -> models.InvokeResponse:
        """
        该接口用于运行函数。
        """
        
        kwargs = {}
        kwargs["action"] = "Invoke"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvokeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InvokeFunction(
            self,
            request: models.InvokeFunctionRequest,
            opts: Dict = None,
    ) -> models.InvokeFunctionResponse:
        """
        SCF同步调用函数接口。
        """
        
        kwargs = {}
        kwargs["action"] = "InvokeFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvokeFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAliases(
            self,
            request: models.ListAliasesRequest,
            opts: Dict = None,
    ) -> models.ListAliasesResponse:
        """
        返回一个函数下的全部别名，可以根据特定函数版本过滤。
        """
        
        kwargs = {}
        kwargs["action"] = "ListAliases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAliasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAsyncEvents(
            self,
            request: models.ListAsyncEventsRequest,
            opts: Dict = None,
    ) -> models.ListAsyncEventsResponse:
        """
        拉取函数异步事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAsyncEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAsyncEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListCustomDomains(
            self,
            request: models.ListCustomDomainsRequest,
            opts: Dict = None,
    ) -> models.ListCustomDomainsResponse:
        """
        遍历域名列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListCustomDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCustomDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListFunctions(
            self,
            request: models.ListFunctionsRequest,
            opts: Dict = None,
    ) -> models.ListFunctionsResponse:
        """
        该接口根据传入的查询参数返回相关函数信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ListFunctions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListFunctionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListLayerVersions(
            self,
            request: models.ListLayerVersionsRequest,
            opts: Dict = None,
    ) -> models.ListLayerVersionsResponse:
        """
        返回指定层的全部版本的信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListLayerVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListLayerVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListLayers(
            self,
            request: models.ListLayersRequest,
            opts: Dict = None,
    ) -> models.ListLayersResponse:
        """
        返回全部层的列表，其中包含了每个层最新版本的信息，可以通过适配运行时进行过滤。
        """
        
        kwargs = {}
        kwargs["action"] = "ListLayers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListLayersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListNamespaces(
            self,
            request: models.ListNamespacesRequest,
            opts: Dict = None,
    ) -> models.ListNamespacesResponse:
        """
        列出命名空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTriggers(
            self,
            request: models.ListTriggersRequest,
            opts: Dict = None,
    ) -> models.ListTriggersResponse:
        """
        获取函数触发器列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListTriggers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTriggersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListVersionByFunction(
            self,
            request: models.ListVersionByFunctionRequest,
            opts: Dict = None,
    ) -> models.ListVersionByFunctionResponse:
        """
        该接口根据传入的参数查询函数的版本。
        """
        
        kwargs = {}
        kwargs["action"] = "ListVersionByFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListVersionByFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PublishLayerVersion(
            self,
            request: models.PublishLayerVersionRequest,
            opts: Dict = None,
    ) -> models.PublishLayerVersionResponse:
        """
        使用给定的zip文件或cos对象创建一个层的新版本，每次使用相同的层的名称调用本接口，都会生成一个新版本。
        """
        
        kwargs = {}
        kwargs["action"] = "PublishLayerVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PublishLayerVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PublishVersion(
            self,
            request: models.PublishVersionRequest,
            opts: Dict = None,
    ) -> models.PublishVersionResponse:
        """
        该接口用于用户发布新版本函数。
        """
        
        kwargs = {}
        kwargs["action"] = "PublishVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PublishVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutProvisionedConcurrencyConfig(
            self,
            request: models.PutProvisionedConcurrencyConfigRequest,
            opts: Dict = None,
    ) -> models.PutProvisionedConcurrencyConfigResponse:
        """
        设置函数某一非$LATEST版本的预置并发。
        """
        
        kwargs = {}
        kwargs["action"] = "PutProvisionedConcurrencyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutProvisionedConcurrencyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutReservedConcurrencyConfig(
            self,
            request: models.PutReservedConcurrencyConfigRequest,
            opts: Dict = None,
    ) -> models.PutReservedConcurrencyConfigResponse:
        """
        设置函数最大独占配额
        """
        
        kwargs = {}
        kwargs["action"] = "PutReservedConcurrencyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutReservedConcurrencyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutTotalConcurrencyConfig(
            self,
            request: models.PutTotalConcurrencyConfigRequest,
            opts: Dict = None,
    ) -> models.PutTotalConcurrencyConfigResponse:
        """
        修改账号并发限制配额
        """
        
        kwargs = {}
        kwargs["action"] = "PutTotalConcurrencyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutTotalConcurrencyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateAsyncEvent(
            self,
            request: models.TerminateAsyncEventRequest,
            opts: Dict = None,
    ) -> models.TerminateAsyncEventResponse:
        """
        终止正在运行中的函数异步事件
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateAsyncEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateAsyncEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAlias(
            self,
            request: models.UpdateAliasRequest,
            opts: Dict = None,
    ) -> models.UpdateAliasResponse:
        """
        更新别名的配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCustomDomain(
            self,
            request: models.UpdateCustomDomainRequest,
            opts: Dict = None,
    ) -> models.UpdateCustomDomainResponse:
        """
        更新自定义域名相关配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCustomDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCustomDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateFunctionCode(
            self,
            request: models.UpdateFunctionCodeRequest,
            opts: Dict = None,
    ) -> models.UpdateFunctionCodeResponse:
        """
        该接口根据传入参数更新函数代码。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateFunctionCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateFunctionCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateFunctionConfiguration(
            self,
            request: models.UpdateFunctionConfigurationRequest,
            opts: Dict = None,
    ) -> models.UpdateFunctionConfigurationResponse:
        """
        该接口根据传入参数更新函数配置。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateFunctionConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateFunctionConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateFunctionEventInvokeConfig(
            self,
            request: models.UpdateFunctionEventInvokeConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateFunctionEventInvokeConfigResponse:
        """
        更新函数的异步重试配置，包括重试次数和消息保留时间
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateFunctionEventInvokeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateFunctionEventInvokeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateNamespace(
            self,
            request: models.UpdateNamespaceRequest,
            opts: Dict = None,
    ) -> models.UpdateNamespaceResponse:
        """
        更新命名空间
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTrigger(
            self,
            request: models.UpdateTriggerRequest,
            opts: Dict = None,
    ) -> models.UpdateTriggerResponse:
        """
        支持触发器配置更新。
        默认接口请求频率限制：20次/秒

        注意：目前只支持timer触发器和ckafka触发器更新！

        timer触发器和ckafka触发器支持更新字段有：Enable、TriggerDesc、Description、CustomArgument。

        timer触发器TriggerDesc支持5段式和7段式的更新。

        ckafka触发器TriggerDesc支持Retry、MaxMsgNum、TimeOut参数更新，不传值表示原值不变，传值不能为空。

        Enable 触发器开启或关闭，传参为OPEN为开启，CLOSE为关闭。不传值表示原值不变，传值不能为空。

        Description 触发器描述，不传值保持原值不变，传值为空则为空。

        CustomArgument 触发器用户附加信息（注意：只有timer触发器展示），不传值保持原值不变，传值为空则为空。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTrigger"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTriggerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTriggerStatus(
            self,
            request: models.UpdateTriggerStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateTriggerStatusResponse:
        """
        更新触发器状态的值
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTriggerStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTriggerStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)